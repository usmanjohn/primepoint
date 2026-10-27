"""
Fake data in the bank's shape, to see the pages before the real file exists:

    python manage.py build_vintage --fake

writes datasets/vintage/input/fake.parquet (only if there is no other input file) and builds.
Delete fake.parquet when the real file is in the folder.

What is planted, so you can check the pages find it:
  * loans issued from March to December 2024 go overdue twice as often (a bad policy year);
  * loans issued in December are 30% worse (holiday lending);
  * a few loans are restructured into category 3 without being 90+ (NPL ≠ 90+);
  * loans issued in 2019 appear from the first month (no start of history);
  * some loans have two rows in a month (two accounts), and some categories are 0;
  * like the bank's file, 2020–2021 are QUARTERLY: 01.01.2020, 01.04.2020 … 01.01.2022, then monthly;
  * two passports: 40% «vtorichka», which goes overdue 1.5 times as often as «pervichka».
"""
import datetime as dt

import numpy as np
import polars as pl


def first_of(month_index):
    return dt.date(2019 + month_index // 12, month_index % 12 + 1, 1)


def make(path, seed=7, last=(2026, 9), monthly_from=dt.date(2022, 1, 1)):
    rng = np.random.default_rng(seed)
    n_months = (last[0] - 2019) * 12 + last[1]          # month 0 = Jan 2019
    issue_m, amount, term = [], [], []
    for m in range(n_months):
        season = {12: 1.3, 1: 0.8}.get(m % 12 + 1, 1.0)
        n = int(500 * (1 + 0.012 * m) * season)
        issue_m += [m] * n
        amount += list(rng.lognormal(np.log(30e6), 0.6, n))
        term += list(rng.choice([12, 24, 36], n))
    issue_m, amount, term = np.array(issue_m), np.array(amount), np.array(term)
    n = len(issue_m)
    risk = np.ones(n)
    passport = np.where(rng.random(n) < 0.4, "vtorichka", "pervichka")
    issued = [first_of(m) for m in range(n_months)]
    for i, m in enumerate(range(n_months)):
        d = issued[m]
        factor = 1.0
        if dt.date(2024, 3, 1) <= d <= dt.date(2024, 12, 1):
            factor *= 2.0
        if d.year == 2021:
            factor *= 0.8
        if d.month == 12:
            factor *= 1.3
        risk[issue_m == m] = factor
    risk = risk * np.where(passport == "vtorichka", 1.5, 1.0)

    dpd = np.zeros(n)
    alive = np.ones(n, dtype=bool)
    restr = np.zeros(n)                                 # months left in a restructuring
    rows = []
    cure = {1: 0.5, 30: 0.25, 60: 0.12, 90: 0.03}
    for m in range(n_months):
        live = np.where(alive & (issue_m <= m))[0]
        age = m - issue_m[live]
        # repaid, prepaid, written off
        done = (age >= term[live]) | (rng.random(len(live)) < 0.012) | (dpd[live] >= 450)
        alive[live[done]] = False
        live, age = live[~done], age[~done]
        if m < 11:                                      # 2019: issued, but the data starts with 01.01.2020
            continue
        d = dpd[live]
        new_dpd = d.copy()
        p_in = 0.03 * risk[live] * np.where(age < 2, 0.3, 1.0)
        start = (d == 0) & (rng.random(len(live)) < p_in)
        new_dpd[start] = 15
        late = d > 0
        p_cure = np.select([d >= 90, d >= 60, d >= 30], [cure[90], cure[60], cure[30]], cure[1])
        cured = late & (rng.random(len(live)) < p_cure)
        new_dpd[late & cured] = 0
        new_dpd[late & ~cured] = d[late & ~cured] + 30
        dpd[live] = new_dpd
        r = restr[live]
        newly = (new_dpd == 0) & (r == 0) & (rng.random(len(live)) < 0.002)
        r[newly] = 6
        r[r > 0] -= 1
        restr[live] = r
        cat = np.select([new_dpd >= 270, new_dpd >= 180, new_dpd >= 90, new_dpd >= 30], [5, 4, 3, 2], 1)
        cat = np.where((r > 0) & (cat < 3), 3, cat)
        cat = np.where((cat == 1) & (rng.random(len(live)) < 0.05), 0, cat)        # 0 means 1
        balance = amount[live] * np.clip(1 - age / term[live], 0.02, 1)
        report = first_of(m + 1)                        # the 1st of the NEXT month
        if report < monthly_from and report.month not in (1, 4, 7, 10):
            continue                                    # quarterly years: no file for this month
        rows.append(pl.DataFrame({          # the bank's column names
            "report_date": [report] * len(live), "anketa": live + 100000,
            "valuedate": [issued[k] + dt.timedelta(days=int(k % 27)) for k in issue_m[live]],
            "maks_dni": new_dpd.astype(int), "npl_category": cat.astype(int), "brutto_95_summa": balance.round(2),
            "given_amount": amount[live].round(2), "passport": passport[live],
        }))
    df = pl.concat(rows)
    twice = df.sample(fraction=0.01, seed=seed).with_columns(pl.col("brutto_95_summa") * 0.1)
    df = pl.concat([df, twice])
    path.parent.mkdir(parents=True, exist_ok=True)
    df.write_parquet(path)
    return df.height
