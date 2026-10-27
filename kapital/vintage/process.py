"""
Vintage analysis of the loan portfolio.

THE IDEA
Loans are grouped by the month they were issued (the «поколение», vintage). Each group is
followed month by month — MOB, «месяц жизни» = months since issue — and we ask: what share
of this group has EVER been bad by MOB k? Ever, not "this month": a loan that went 90+ and
was then written off or cured must stay counted, or old vintages look cleaner than they were.

Two analyses, the same machinery, a different "bad":
    просрочка  — maks_dni ≥ 30 / 60 / 90   (90+ is the main one)
    NPL        — npl_category ≥ 3

Each is measured two ways:
    по количеству — bad loans / loans issued in that month
    по сумме      — the balance the loan had when it first went bad / the amount ISSUED in
                    that vintage (given_amount; the first month's balance if it is missing).
                    Dividing by what was issued matters: today's balance shrinks with
                    repayments, and the rate would grow by itself.

Everything is built three times — all passports together and each passport (pervichka,
vtorichka) on its own — and the page switches with ?seg=.

HOW IT RUNS
    python manage.py build_vintage      reads datasets/vintage/input/*.parquet (tens of
                                        millions of rows: polars, in its own process — never
                                        inside gunicorn) and saves the small results to
                                        datasets/vintage/result/
    the page                            reads only those small results, so it is instant.

THE SECTIONS OF THIS FILE
    1. Settings                 — everything you may want to change is here
    2. Building (the command)   — input → loan-months → triangles, transitions, today's book
    3. Reading the results
    4. The projection           — finishing the young vintages (the chain-ladder idea)
    5. Insights                 — the sentences at the top of the page
    6. The plan                 — expected new 90+ / NPL for the next months
    7. Page helpers             — colours, the curves picture, number formats
    8. Excel
"""
import datetime as dt
import io
import json
import os
import time
from pathlib import Path

import numpy as np
import polars as pl
from django.conf import settings

# ═══════════════════════════════════ 1. SETTINGS ═══════════════════════════════════════

BASE = Path(settings.BASE_DIR) / "datasets" / "vintage"
INPUT_DIR = BASE / "input"            # put your parquet file(s) here — all *.parquet are read
RESULT_DIR = BASE / "result"
STATUS_FILE = BASE / "status.json"
LOG_FILE = BASE / "build.log"

# our name → the column name in YOUR parquet. Change the right-hand side if yours differ.
COLUMNS = {
    "date": "report_date",              # the 1st of the month
    "anketa": "anketa",                 # the loan id (repeats every month)
    "issue_date": "valuedate",          # when the loan was issued
    "maks_dni": "maks_dni",             # overdue days in the period
    "npl_category": "npl_category",     # 1…5 (0 is read as 1)
    "portfel_amount": "brutto_95_summa",# the balance in the period
    "given_amount": "given_amount",     # the amount issued (the «по сумме» denominator)
    "passport": "passport",             # the product: every analysis is built for all + each passport
}
# How the passport values are shown. A value not listed here is shown as it is.
PASSPORTS = {"pervichka": "Первичка", "vtorichka": "Вторичка"}
ALL = "all"                            # the «все паспорта» key in the address (?seg=all)
# 2024-02-01 in the file means the portfolio at the end of JANUARY. True = shift back a month.
DATE_IS_NEXT_MONTH = True

NPL_FROM = 3                           # NPL = category ≥ 3
KINDS = {
    "dpd30": {"label": "Просрочка 30+", "group": "dpd", "rule": ("dpd", 30)},
    "dpd60": {"label": "Просрочка 60+", "group": "dpd", "rule": ("dpd", 60)},
    "dpd90": {"label": "Просрочка 90+", "group": "dpd", "rule": ("dpd", 90)},
    "npl":   {"label": f"NPL (категория ≥ {NPL_FROM})", "group": "npl", "rule": ("cat", NPL_FROM)},
}
MAIN = {"dpd": "dpd90", "npl": "npl"}  # what the plan and the early signal predict
MEASURES = {"amount": "по сумме", "count": "по количеству"}

# overdue buckets for the transitions table: (from days, name)
DPD_BUCKETS = [(90, "90+"), (60, "60–89"), (30, "30–59"), (1, "1–29"), (0, "0")]
NPL_STATES = ["1", "2", "3", "4", "5"]
GONE = "вышел"                         # not in the portfolio next month: repaid, written off, sold

RECENT_VINTAGES = 12     # the projection learns each month's step from the 12 newest vintages that reached it
MIGRATION_MONTHS = 12    # the transitions table uses the last 12 months
PLAN_MONTHS = 12
EARLY_MOB = 3            # the early signal: 30+ at month 3 …
LATE_MOB = 12            # … predicts 90+ / NPL at month 12
MOB_SHOWN = list(range(0, 25)) + [30, 36, 42, 48, 54, 60, 66, 72, 78]   # triangle columns

AMOUNT_DIVISOR = 1_000_000
AMOUNT_UNIT = "млн"

# ═══════════════════════════ 2. BUILDING (the command) ══════════════════════════════════


def input_files():
    return sorted(INPUT_DIR.glob("*.parquet"))


def add_months(day, n):
    m = day.year * 12 + day.month - 1 + n
    return dt.date(m // 12, m % 12 + 1, 1)


def months_between(a, b):
    return (b.year - a.year) * 12 + b.month - a.month


def mob_expr(month, start):
    return ((pl.col(month).dt.year().cast(pl.Int32) - pl.col(start).dt.year().cast(pl.Int32)) * 12
            + pl.col(month).dt.month().cast(pl.Int32) - pl.col(start).dt.month().cast(pl.Int32))


def dpd_bucket(col):
    expr = pl.when(pl.col(col) >= DPD_BUCKETS[0][0]).then(pl.lit(DPD_BUCKETS[0][1]))
    for days, name in DPD_BUCKETS[1:]:
        expr = expr.when(pl.col(col) >= days).then(pl.lit(name))
    return expr.otherwise(pl.lit("0"))


def bad_expr(kind):
    col, edge = KINDS[kind]["rule"]
    return pl.col(col) >= edge


def read_loan_months(files, log=print):
    """Every file → one row per loan per month: month, anketa, issue, dpd, cat, amount, given, passport."""
    c = COLUMNS
    month = pl.col("date").cast(pl.Date)
    if DATE_IS_NEXT_MONTH:
        month = month.dt.offset_by("-1mo")
    lf = (pl.scan_parquet([str(f) for f in files])
          .select(pl.col(c["date"]).alias("date"), pl.col(c["anketa"]).alias("anketa"),
                  pl.col(c["issue_date"]).cast(pl.Date).alias("issue"),
                  pl.col(c["maks_dni"]).cast(pl.Float64).fill_null(0).alias("dpd"),
                  pl.col(c["npl_category"]).cast(pl.Float64).fill_null(1).alias("cat"),
                  pl.col(c["portfel_amount"]).cast(pl.Float64).fill_null(0).alias("amount"),
                  pl.col(c["given_amount"]).cast(pl.Float64).alias("given"),
                  pl.col(c["passport"]).cast(pl.Utf8).str.strip_chars().alias("passport"))
          .with_columns(month.dt.truncate("1mo").alias("month"),
                        pl.col("issue").dt.truncate("1mo"),
                        pl.col("cat").clip(1, 5).cast(pl.Int8)))
    rows = lf.select(pl.len()).collect().item()
    log(f"rows in the files: {rows:,}")
    # one row per loan and month: several accounts of one loan are added up (the balance);
    # the issued amount is the same on every row of a loan, so it is not added up
    lm = (lf.group_by("anketa", "month")
            .agg(pl.col("issue").min(), pl.col("dpd").max(), pl.col("cat").max(), pl.col("amount").sum(),
                 pl.col("given").max(), pl.col("passport").drop_nulls().first())
            .collect()
            .sort("anketa", "month"))
    log(f"loan-months: {lm.height:,}")
    return lm, rows


def month_index(col):
    """A month as one number (year × 12 + month) — easy to compare and to add MOBs to."""
    return pl.col(col).dt.year().cast(pl.Int32) * 12 + pl.col(col).dt.month().cast(pl.Int32) - 1


def transitions(lm, last_month, data_months):
    """Where each loan was the next month, for the last MIGRATION_MONTHS months: count,
    the balance at the start (for the shares) and the balance a month later (for the forecast).
    Only months whose NEXT month is in the data: across a quarterly gap every loan would look «вышел»."""
    first = add_months(last_month, -MIGRATION_MONTHS)
    has_next = [m for m in data_months if add_months(m, 1) in set(data_months)]
    nxt = lm.with_columns(pl.col("month").shift(-1).over("anketa").alias("next_month"),
                          pl.col("dpd").shift(-1).over("anketa").alias("next_dpd"),
                          pl.col("cat").shift(-1).over("anketa").alias("next_cat"),
                          pl.col("amount").shift(-1).over("anketa").alias("next_amount"))
    pairs = nxt.filter((pl.col("month") >= first) & (pl.col("month") < last_month) & pl.col("month").is_in(has_next))
    stayed = pl.col("next_month") == pl.col("month").dt.offset_by("1mo")
    out = []
    for group, frm, to in [
        ("dpd", dpd_bucket("dpd"), dpd_bucket("next_dpd")),
        ("npl", pl.col("cat").cast(pl.Utf8), pl.col("next_cat").cast(pl.Utf8)),
    ]:
        t = (pairs.with_columns(frm.alias("from"),
                                pl.when(stayed).then(to).otherwise(pl.lit(GONE)).alias("to"),
                                pl.when(stayed).then(pl.col("next_amount")).otherwise(0.0).alias("next_amount"))
             .group_by("from", "to")
             .agg(pl.len().alias("count"), pl.col("amount").sum(), pl.col("next_amount").sum())
             .with_columns(pl.lit(group).alias("group")))
        out.append(t)
    return pl.concat(out)


def book_today(lm, last_month):
    """The portfolio in the last month by state — where the transitions forecast starts."""
    now = lm.filter(pl.col("month") == last_month)
    return pl.concat([
        now.with_columns(dpd_bucket("dpd").alias("state")).group_by("state")
           .agg(pl.len().alias("count"), pl.col("amount").sum()).with_columns(pl.lit("dpd").alias("group")),
        now.with_columns(pl.col("cat").cast(pl.Utf8).alias("state")).group_by("state")
           .agg(pl.len().alias("count"), pl.col("amount").sum()).with_columns(pl.lit("npl").alias("group")),
    ])


def triangles(lm, first_month, last_month, data_months):
    """The vintage triangles: for every vintage and MOB, how many loans (and how much balance)
    have EVER been bad by that month. Only cells whose calendar month is in the data: in the
    quarterly years (2020–2021) a vintage has a value every third month, the cells between
    are left out (empty in the table), never guessed."""
    v = lm.filter(pl.col("issue") >= first_month).with_columns(mob_expr("month", "issue").alias("mob"))
    v = v.filter(pl.col("mob") >= 0)
    loans = v.group_by("anketa").agg(
        pl.col("issue").first().alias("vintage"),
        # the base of «по сумме»: the issued amount; the first month's balance if it is missing
        pl.when(pl.col("given").first() > 0).then(pl.col("given").first())
          .otherwise(pl.col("amount").first()).alias("start_amount"),   # rows are sorted by month
        *[pl.col("mob").filter(bad_expr(k)).min().alias(f"{k}_mob") for k in KINDS],
        *[pl.col("amount").filter(bad_expr(k)).first().alias(f"{k}_amount") for k in KINDS],
    )
    vint = (loans.group_by("vintage").agg(pl.len().alias("loans"), pl.col("start_amount").sum().alias("base"))
            .with_columns(((last_month.year - pl.col("vintage").dt.year().cast(pl.Int32)) * 12
                           + last_month.month - pl.col("vintage").dt.month().cast(pl.Int32)).alias("age")))
    k_max = months_between(first_month, last_month)
    grid = (vint.join(pl.DataFrame({"mob": list(range(k_max + 1))}, schema={"mob": pl.Int32}), how="cross")
            .filter(pl.col("mob") <= pl.col("age"))
            .filter((month_index("vintage") + pl.col("mob")).is_in([m.year * 12 + m.month - 1 for m in data_months])))
    out = []
    for k in KINDS:
        ev = (loans.filter(pl.col(f"{k}_mob").is_not_null())
              .group_by("vintage", pl.col(f"{k}_mob").cast(pl.Int32).alias("mob"))
              .agg(pl.len().alias("new_count"), pl.col(f"{k}_amount").sum().alias("new_amount")))
        t = (grid.join(ev, on=["vintage", "mob"], how="left")
             .with_columns(pl.col("new_count").fill_null(0), pl.col("new_amount").fill_null(0.0))
             .sort("vintage", "mob")
             .with_columns(pl.col("new_count").cum_sum().over("vintage").alias("bad_count"),
                           pl.col("new_amount").cum_sum().over("vintage").alias("bad_amount"))
             .with_columns(pl.lit(k).alias("kind")))
        out.append(t)
    return pl.concat(out).select("kind", "vintage", "mob", "loans", "base", "bad_count", "bad_amount")


def build(log=print):
    """The whole build: input files → datasets/vintage/result/. Returns the meta dict."""
    started = time.time()
    files = input_files()
    if not files:
        raise FileNotFoundError(f"нет файлов *.parquet в {INPUT_DIR}")
    lm, rows = read_loan_months(files, log)
    checks = {"Строк в файлах": rows, "Строк объединено (один кредит дважды в месяц)": rows - lm.height}

    no_issue = lm.filter(pl.col("issue").is_null())["anketa"].n_unique()
    lm = lm.with_columns(pl.col("issue").min().over("anketa"))       # one issue month per loan
    first_month, last_month = lm["month"].min(), lm["month"].max()
    data_months = sorted(lm["month"].unique().to_list())
    missing = [add_months(first_month, i) for i in range(months_between(first_month, last_month) + 1)
               if add_months(first_month, i) not in set(data_months)]
    checks["Кредитов без даты выдачи (не попали в поколения)"] = no_issue
    before = lm.filter(pl.col("issue") < first_month)["anketa"].n_unique()
    checks[f"Кредитов, выданных до {first_month:%m.%Y} (нет начала истории — не в поколениях, но в переходах)"] = before
    wrong = lm.filter(pl.col("month") < pl.col("issue"))["anketa"].n_unique()
    checks["Кредитов с отчётом раньше даты выдачи (эти месяцы пропущены)"] = wrong
    checks["Месяцев без данных (квартальные годы — пустые клетки в треугольнике)"] = len(missing)

    # one passport per loan: the latest one it had (and how many loans changed it)
    pas = (lm.filter(pl.col("passport").is_not_null()).group_by("anketa")
             .agg(pl.col("passport").last(), pl.col("passport").n_unique().alias("passports")))
    checks["Кредитов, сменивших паспорт (взят последний)"] = pas.filter(pl.col("passports") > 1).height
    lm = lm.drop("passport").join(pas.select("anketa", "passport"), on="anketa", how="left") \
           .with_columns(pl.col("passport").fill_null("не указан")).sort("anketa", "month")
    checks["Кредитов без суммы выдачи (база «по сумме» = остаток 1-го месяца)"] = \
        lm.filter(~(pl.col("given") > 0))["anketa"].n_unique()
    counts = lm.group_by("passport").agg(pl.col("anketa").n_unique().alias("loans")).sort("loans", descending=True)
    segments = [{"key": ALL, "label": "Все паспорта", "loans": int(lm["anketa"].n_unique())}] + \
               [{"key": r["passport"], "label": PASSPORTS.get(r["passport"], r["passport"]), "loans": int(r["loans"])}
                for r in counts.iter_rows(named=True)]

    tri, tr, bk = [], [], []
    for seg in segments:
        part = lm if seg["key"] == ALL else lm.filter(pl.col("passport") == seg["key"])
        log(f"{seg['label']}: {seg['loans']:,} loans — transitions, today's book, triangles …")
        tag = pl.lit(seg["key"]).alias("seg")
        tr.append(transitions(part, last_month, data_months).with_columns(tag))
        bk.append(book_today(part, last_month).with_columns(tag))
        tri.append(triangles(part, first_month, last_month, data_months).with_columns(tag))
    tri, tr, bk = pl.concat(tri), pl.concat(tr), pl.concat(bk)

    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    for name, table in [("triangle", tri), ("transitions", tr), ("book", bk)]:
        tmp = RESULT_DIR / f"{name}.parquet.tmp"
        table.write_parquet(tmp)
        os.replace(tmp, RESULT_DIR / f"{name}.parquet")
    meta = {
        "first_month": first_month.isoformat(), "last_month": last_month.isoformat(),
        "built_at": dt.datetime.now().isoformat(timespec="seconds"),
        "seconds": round(time.time() - started, 1),
        "loans": int(lm["anketa"].n_unique()),
        "segments": segments,
        "files": [f.name for f in files], "checks": checks,
        "missing_from": missing[0].isoformat() if missing else None,
        "missing_to": missing[-1].isoformat() if missing else None,
    }
    (RESULT_DIR / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1))
    log(f"done in {meta['seconds']} s")
    return meta


# ═══════════════════════════════ 3. READING THE RESULTS ════════════════════════════════

CACHE = {"stamp": None, "data": None}


def results():
    """The saved results (None if never built). Read once, re-read when the build changes them."""
    meta_file = RESULT_DIR / "meta.json"
    if not meta_file.exists():
        return None
    stamp = meta_file.stat().st_mtime
    if CACHE["stamp"] != stamp:
        meta = json.loads(meta_file.read_text())
        meta["first_month"] = dt.date.fromisoformat(meta["first_month"])
        meta["last_month"] = dt.date.fromisoformat(meta["last_month"])
        for key in ("missing_from", "missing_to"):
            meta[key] = dt.date.fromisoformat(meta[key]) if meta.get(key) else None
        CACHE["data"] = {
            "meta": meta,
            "triangle": pl.read_parquet(RESULT_DIR / "triangle.parquet"),
            "transitions": pl.read_parquet(RESULT_DIR / "transitions.parquet"),
            "book": pl.read_parquet(RESULT_DIR / "book.parquet"),
        }
        CACHE["stamp"] = stamp
    return CACHE["data"]


def matrix(res, kind, measure, seg=ALL):
    """The triangle as numbers: vintages (list of dates), R[vintage, mob] (NaN = not reached
    yet), weight per vintage (issued amount or number of loans). seg = a passport or ALL."""
    t = res["triangle"].filter((pl.col("kind") == kind) & (pl.col("seg") == seg)).sort("vintage", "mob")
    vint = t.group_by("vintage").agg(pl.col("loans").first(), pl.col("base").first()).sort("vintage")
    vintages = vint["vintage"].to_list()
    k = months_between(res["meta"]["first_month"], res["meta"]["last_month"]) + 1
    R = np.full((len(vintages), k), np.nan)
    pos = {v: i for i, v in enumerate(vintages)}
    vi = np.array([pos[v] for v in t["vintage"].to_list()], dtype=int)
    mi = t["mob"].to_numpy()
    if measure == "amount":
        base = t["base"].to_numpy()
        R[vi, mi] = np.divide(t["bad_amount"].to_numpy(), base, out=np.zeros(len(base)), where=base > 0)
        weight = vint["base"].to_numpy().astype(float)
    else:
        R[vi, mi] = t["bad_count"].to_numpy() / t["loans"].to_numpy()
        weight = vint["loans"].to_numpy().astype(float)
    return vintages, R, weight


# ═══════════════════════════════════ 4. THE PROJECTION ═════════════════════════════════
#
# A young vintage has only a few months. To finish its row we borrow the STEPS of the older
# rows: on average, how much does the rate grow from month k-1 to month k? (taken from the
# RECENT_VINTAGES newest vintages that have reached month k, weighted by their size). The young
# row then continues from its own last real value by those average steps — so a bad vintage
# stays bad, it just ages like the others. This is the chain-ladder idea in its additive form,
# which does not break when early months are 0.

def average_steps(R, weight):
    k = R.shape[1]
    steps = np.zeros(k)
    reached = np.zeros(k, dtype=int)
    inc = np.diff(R, axis=1, prepend=0.0)          # inc[:, 0] = R[:, 0]
    for m in range(k):
        rows = np.where(~np.isnan(inc[:, m]))[0][-RECENT_VINTAGES:]
        reached[m] = len(rows)
        if len(rows) and weight[rows].sum() > 0:
            steps[m] = np.average(inc[rows, m], weights=weight[rows])
    return steps, reached


def projected(R, steps, extra=0):
    """R continued AFTER each row's last real value by the average steps (and `extra` months
    beyond the longest history, where the curve stays flat). Empty cells BEFORE the last real
    value (the quarterly years) stay empty: they are the past, not something to forecast.
    Returns (P, is_projected)."""
    v, k = R.shape
    steps = np.concatenate([steps, np.zeros(extra)])
    P = np.concatenate([R, np.full((v, extra), np.nan)], axis=1)
    proj = np.zeros(P.shape, dtype=bool)
    for i in range(v):
        real = np.where(~np.isnan(R[i]))[0]
        for m in range(real[-1] + 1 if len(real) else 0, k + extra):
            P[i, m] = min(1.0, (P[i, m - 1] if m else 0.0) + steps[m])
            proj[i, m] = True
    return P, proj


def typical_curve(steps):
    """The expected curve of a NEW vintage: month 0, 1, 2 … (cumulative average steps)."""
    return np.minimum(1.0, np.cumsum(steps))


# ═══════════════════════════════════ 5. INSIGHTS ═══════════════════════════════════════

def reference_mob(R):
    """The month to compare vintages at: 12 if at least 6 vintages reached it, else 6, else 3."""
    reached = (~np.isnan(R)).sum(axis=0)
    for m in (12, 6, 3, 1):
        if m < R.shape[1] and reached[m] >= 6:
            return m
    return 0


def pct(x, digits=2):
    return "—" if x is None or np.isnan(x) else f"{x * 100:.{digits}f}%".replace(".", ",")


def num(x, digits=2):
    return f"{x:.{digits}f}".replace(".", ",")


def month_name(day):
    return f"{day:%m.%Y}"


RU_MONTHS = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август",
             "сентябрь", "октябрь", "ноябрь", "декабрь"]


def insights(vintages, R, weight, steps, kind, measure):
    """A few sentences a manager can read without the table."""
    label = KINDS[kind]["label"]
    out = []
    ref = reference_mob(R)
    col = R[:, ref]
    seen = ~np.isnan(col)
    if seen.sum() >= 3:
        avg = np.average(col[seen], weights=weight[seen]) if weight[seen].sum() else col[seen].mean()
        worst, best = np.nanargmax(np.where(seen, col, -1)), np.nanargmin(np.where(seen, col, 2))
        out.append(f"На {ref}-м месяце жизни в среднем {pct(avg)} кредитов ({MEASURES[measure]}) уже были в «{label}». "
                   f"Хуже всех — выданные в {month_name(vintages[worst])}: {pct(col[worst])}, "
                   f"лучше всех — {month_name(vintages[best])}: {pct(col[best])}.")
        idx = np.where(seen)[0]
        if len(idx) >= 12:
            new, old = idx[-6:], idx[-18:-6]
            a = np.average(col[new], weights=weight[new]) if weight[new].sum() else col[new].mean()
            b = np.average(col[old], weights=weight[old]) if weight[old].sum() else col[old].mean()
            word = "хуже" if a > b else "лучше"
            out.append(f"Последние 6 поколений, дошедших до {ref}-го месяца ({month_name(vintages[new[0]])}–"
                       f"{month_name(vintages[new[-1]])}): {pct(a)} против {pct(b)} у 12 предыдущих — "
                       f"{word} на {num(abs(a - b) * 100)} п.п.")
    curve = typical_curve(steps)
    if len(curve) > 24 and curve[24] > 0:
        out.append(f"Типичное поколение к 6-му месяцу набирает {curve[6] / curve[24] * 100:.0f}% того, что наберёт "
                   f"к 24-му, к 12-му — {curve[12] / curve[24] * 100:.0f}%. Значит, о новом поколении можно "
                   f"судить уже через полгода–год.")
    if len(steps) > 2 and steps[1:].max() > 0:
        peak = int(np.argmax(steps[1:]) + 1)
        out.append(f"Больше всего новых случаев появляется на {peak}-м месяце жизни "
                   f"(+{num(steps[peak] * 100)} п.п. за этот месяц).")
    season = seasonality(vintages, R, weight, ref)
    if season:
        top = max(season, key=lambda s: s["raw"])
        low = min(season, key=lambda s: s["raw"])
        out.append(f"По месяцу выдачи: хуже всего — кредиты, выданные в месяц «{top['name']}» ({top['value']} на "
                   f"{ref}-м месяце), лучше всего — «{low['name']}» ({low['value']}).")
    return out, ref


def seasonality(vintages, R, weight, ref):
    """The rate at month `ref` averaged by the calendar month of issue (only if every calendar
    month has at least 2 vintages)."""
    col = R[:, ref]
    rows = []
    for m in range(1, 13):
        idx = [i for i, v in enumerate(vintages) if v.month == m and not np.isnan(col[i])]
        if len(idx) < 2:
            return []
        w = weight[idx]
        raw = float(np.average(col[idx], weights=w)) if w.sum() else float(col[idx].mean())
        rows.append({"name": RU_MONTHS[m - 1], "raw": raw, "value": pct(raw), "n": len(idx)})
    top = max(r["raw"] for r in rows) or 1
    for r in rows:
        r["bar"] = round(r["raw"] / top * 100)
    return rows


def early_signal(res, late_kind, seg=ALL):
    """Does 30+ at month EARLY_MOB predict LATE_MOB? Fitted on the vintages that reached
    LATE_MOB, then used on the young ones. Returns None when there is too little history."""
    vintages, X, w = matrix(res, "dpd30", "amount", seg)
    _, Y, _ = matrix(res, late_kind, "amount", seg)
    if X.shape[1] <= LATE_MOB:
        return None
    x, y = X[:, EARLY_MOB], Y[:, LATE_MOB]
    fit = ~np.isnan(x) & ~np.isnan(y)
    if fit.sum() < 8 or np.std(x[fit]) == 0:
        return None
    b, a = np.polyfit(x[fit], y[fit], 1)
    r = float(np.corrcoef(x[fit], y[fit])[0, 1])
    steps, _ = average_steps(Y, w)
    P, _ = projected(Y, steps)
    young = [i for i in range(len(vintages)) if not np.isnan(x[i]) and np.isnan(y[i])]
    rows = [{"vintage": month_name(vintages[i]), "early": pct(x[i]),
             "by_signal": pct(max(0.0, a + b * x[i])), "by_curve": pct(P[i, LATE_MOB])} for i in young]
    strength = "сильная" if abs(r) >= 0.7 else "средняя" if abs(r) >= 0.4 else "слабая"
    return {"r": num(r), "strength": strength, "n": int(fit.sum()),
            "formula": f"{KINDS[late_kind]['label']} на {LATE_MOB}-м мес. ≈ {num(a * 100)}% + "
                       f"{num(b)} × (30+ на {EARLY_MOB}-м мес.)",
            "rows": rows[-12:], "late_label": KINDS[late_kind]["label"]}


def segments(res):
    """[{'key', 'label', 'loans'}] — ALL first, then each passport, biggest first."""
    return res["meta"]["segments"]


def segment_label(res, seg):
    return next((s["label"] for s in segments(res) if s["key"] == seg), seg)


def loans_in_vintages(res, seg=ALL):
    t = res["triangle"].filter((pl.col("kind") == "dpd90") & (pl.col("seg") == seg))
    return int(t.group_by("vintage").agg(pl.col("loans").first())["loans"].sum())


COMPARE_MOBS = (6, 12, 24)


def compare(res, kind, measure):
    """The passports side by side: each one's typical curve (how a vintage issued today is
    expected to age) and the actual average of its vintages that reached MOB 6 / 12 / 24.
    Returns None when there is only one passport."""
    segs = [s for s in segments(res) if s["key"] != ALL]
    if len(segs) < 2:
        return None
    rows, lines = [], []
    for n, s in enumerate(segments(res)):
        vintages, R, w = matrix(res, kind, measure, s["key"])
        if not vintages:
            continue
        steps, _ = average_steps(R, w)
        curve = typical_curve(steps)
        cells = []
        for m in COMPARE_MOBS:
            seen = [i for i in range(len(vintages)) if m < R.shape[1] and not np.isnan(R[i, m])][-RECENT_VINTAGES:]
            fact = np.average(R[seen, m], weights=w[seen]) if seen and w[seen].sum() else np.nan
            cells.append({"curve": pct(curve[m]) if m < len(curve) else "—", "fact": pct(fact)})
        rows.append({"key": s["key"], "label": s["label"], "loans": f"{s['loans']:,}".replace(",", " "),
                     "cells": cells, "raw12": curve[12] if len(curve) > 12 else np.nan, "all": s["key"] == ALL})
        lines.append({"name": s["label"], "colour": "#0B0B0C" if s["key"] == ALL else COLOURS[(n + 1) % len(COLOURS)],
                      "pts": list(enumerate(curve[:37])), "dashed": s["key"] == ALL})
    sentence = None
    a, b = [r for r in rows if not r["all"]][:2]
    if a["raw12"] > 0 and b["raw12"] > 0:
        worse, better = (a, b) if a["raw12"] > b["raw12"] else (b, a)
        sentence = (f"«{worse['label']}» хуже: по типичной кривой к 12-му месяцу {pct(worse['raw12'])} против "
                    f"{pct(better['raw12'])} у «{better['label']}» — в {num(worse['raw12'] / better['raw12'], 1)} раза.")
    return {"rows": rows, "mobs": COMPARE_MOBS, "chart": chart(lines, 37), "sentence": sentence}


# ═══════════════════════════════════ 6. THE PLAN ═══════════════════════════════════════
#
# Two parts, both in money (the amount issued in each vintage):
#   from today's book  — each existing vintage continues along its finished row (section 4);
#                        the growth of its rate in month t × its issued amount = new bad money
#   from new lending   — each planned month of lending follows the typical curve.
# The result is a FLOW: how much balance newly reaches 90+ / NPL in each future month.

def default_lending(res, kind, seg=ALL):
    """The average monthly issuance of the last 12 months (the plan's starting suggestion)."""
    t = res["triangle"].filter((pl.col("kind") == kind) & (pl.col("seg") == seg))
    vint = t.group_by("vintage").agg(pl.col("base").first()).sort("vintage")
    return float(vint["base"].tail(12).mean()) if vint.height else 0.0


def plan(res, kind, lending, growth, seg=ALL, months=PLAN_MONTHS):
    vintages, R, weight = matrix(res, kind, "amount", seg)
    steps, _ = average_steps(R, weight)
    P, _ = projected(R, steps, extra=months + 1)
    curve = typical_curve(np.concatenate([steps, np.zeros(months + 1)]))
    last = res["meta"]["last_month"]
    ages = np.array([months_between(v, last) for v in vintages])
    rows, total_cum = [], 0.0
    issued = [lending * (1 + growth) ** s for s in range(months)]
    for t in range(1, months + 1):
        book = float(np.sum(weight * (P[np.arange(len(vintages)), ages + t] - P[np.arange(len(vintages)), ages + t - 1])))
        new = 0.0
        for s in range(1, t + 1):                         # lending of month s is at month t - s of its life
            m = t - s
            new += issued[s - 1] * (curve[m] - (curve[m - 1] if m else 0.0))
        total_cum += book + new
        rows.append({"month": add_months(last, t), "book": book, "new": new, "total": book + new,
                     "cum": total_cum, "lending": issued[t - 1]})
    return rows


def markov(res, group, lending, growth, seg=ALL, months=PLAN_MONTHS):
    """The second route: today's book by state, moved month by month with the transitions
    table (balance a month later / balance now), plus the new lending entering the best state.
    Gives the SHARE of bad balance in the portfolio — a stock, where the plan above is a flow."""
    states = [n for _, n in reversed(DPD_BUCKETS)] if group == "dpd" else NPL_STATES
    bad = {"90+"} if group == "dpd" else set(NPL_STATES[NPL_FROM - 1:])
    tr = res["transitions"].filter((pl.col("group") == group) & (pl.col("seg") == seg))
    M = np.zeros((len(states), len(states)))
    for row in tr.iter_rows(named=True):
        if row["from"] in states and row["to"] in states:
            M[states.index(row["from"]), states.index(row["to"])] += row["next_amount"]
    out_of = np.zeros(len(states))
    for row in tr.iter_rows(named=True):
        if row["from"] in states:
            out_of[states.index(row["from"])] += row["amount"]
    M = np.divide(M, out_of[:, None], out=np.zeros_like(M), where=out_of[:, None] > 0)
    book = res["book"].filter((pl.col("group") == group) & (pl.col("seg") == seg))
    s = np.zeros(len(states))
    for row in book.iter_rows(named=True):
        if row["state"] in states:
            s[states.index(row["state"])] = row["amount"]
    last = res["meta"]["last_month"]
    bad_idx = [states.index(b) for b in bad]
    rows = [{"month": last, "share": s[bad_idx].sum() / s.sum() if s.sum() else 0, "total": s.sum(),
             "bad": s[bad_idx].sum(), "fact": True}]
    for t in range(1, months + 1):
        s = s @ M
        s[0] += lending * (1 + growth) ** (t - 1)
        rows.append({"month": add_months(last, t), "share": s[bad_idx].sum() / s.sum() if s.sum() else 0,
                     "total": s.sum(), "bad": s[bad_idx].sum(), "fact": False})
    return rows


# ═══════════════════════════════════ 7. PAGE HELPERS ═══════════════════════════════════

def money(x):
    return f"{x / AMOUNT_DIVISOR:,.1f}".replace(",", " ").replace(".", ",")


def heat(x, top):
    """White → Kapital yellow → red as the rate goes from 0 to `top`."""
    if x is None or np.isnan(x) or top <= 0:
        return "#FFFFFF", "#0B0B0C"
    f = max(0.0, min(1.0, x / top))
    stops = [(0.0, (255, 255, 255)), (0.5, (242, 194, 48)), (1.0, (179, 52, 31))]
    for (f0, c0), (f1, c1) in zip(stops, stops[1:]):
        if f <= f1:
            g = (f - f0) / (f1 - f0)
            rgb = [round(a + (b - a) * g) for a, b in zip(c0, c1)]
            break
    return "#%02X%02X%02X" % tuple(rgb), ("#FFFFFF" if f > 0.75 else "#0B0B0C")


def triangle_table(vintages, R, P, proj):
    """Rows for the template: vintage, cells (text, background, colour, projected?)."""
    mobs = [m for m in MOB_SHOWN if m < R.shape[1]]
    shown = P[:, mobs]
    positive = shown[shown > 0]
    top = float(np.percentile(positive, 95)) if positive.size else 0
    rows = []
    for i, v in enumerate(vintages):
        cells = []
        for m in mobs:
            if np.isnan(P[i, m]):                         # a month the data does not have (quarterly years)
                cells.append({"text": "", "gap": True})
                continue
            bg, fg = heat(P[i, m], top)
            cells.append({"text": f"{P[i, m] * 100:.2f}".replace(".", ","), "bg": bg, "fg": fg, "proj": bool(proj[i, m])})
        rows.append({"vintage": month_name(v), "year_start": v.month == 1, "cells": cells})
    return mobs, rows[::-1]                              # newest on top


COLOURS = ["#8A867C", "#2A6F97", "#2E7D4F", "#C9971A", "#7B4FA0", "#B3341F", "#0B0B0C", "#D2691E", "#4F8A8B"]


def curves_svg(vintages, R, weight, steps, last_month):
    """The picture: one line per issue year (the weighted average of its vintages, real data
    only) and the dashed typical curve the projection uses.
    In the quarterly years only a third of a year's vintages have a value in any given month,
    so a month is skipped when none has one, and the line stops when fewer than half the
    year's vintages are old enough."""
    k = min(R.shape[1], 61)
    years = sorted({v.year for v in vintages})
    lines = []
    for n, y in enumerate(years):
        idx = [i for i, v in enumerate(vintages) if v.year == y]
        pts = []
        for m in range(k):
            old_enough = [i for i in idx if months_between(vintages[i], last_month) >= m]
            if len(old_enough) < max(1, len(idx) // 2):
                break
            ok = [i for i in old_enough if not np.isnan(R[i, m])]
            if not ok:
                continue
            w = weight[ok]
            pts.append((m, float(np.average(R[ok, m], weights=w)) if w.sum() else float(R[ok, m].mean())))
        if pts:
            lines.append({"name": str(y), "colour": COLOURS[n % len(COLOURS)], "pts": pts})
    lines.append({"name": "типичная кривая", "colour": "#0B0B0C", "dashed": True,
                  "pts": list(enumerate(typical_curve(steps)[:k]))})
    return chart(lines, k)


def chart(lines, k):
    """Lines [{'name', 'colour', 'pts': [(mob, rate)], 'dashed'?}] → everything the template
    needs to draw a plain SVG (no JavaScript): polylines, the y grid and the x ticks."""
    top = max([r for line in lines for _, r in line["pts"]] + [1e-9]) * 1.1
    W, H, L, B = 900, 320, 52, 30

    def xy(m, r):
        return L + m / max(k - 1, 1) * (W - L - 10), H - B - r / top * (H - B - 10)

    for line in lines:
        line["points"] = " ".join("%.1f,%.1f" % xy(m, r) for m, r in line["pts"])
    grid = [{"y": "%.1f" % xy(0, top * g / 4)[1], "label": pct(top * g / 4, 1)} for g in range(5)]
    ticks = [{"x": "%.1f" % xy(m, 0)[0], "label": m} for m in range(0, k, 6)]
    return {"lines": lines, "grid": grid, "ticks": ticks,
            "W": W, "H": H, "L": L, "B": B, "x_end": W - 10, "y_axis": H - B}


def transitions_table(res, group, measure, seg=ALL):
    """The transitions as shares of each row, plus the key flows in words."""
    states = [n for _, n in reversed(DPD_BUCKETS)] if group == "dpd" else NPL_STATES
    cols = states + [GONE]
    tr = res["transitions"].filter((pl.col("group") == group) & (pl.col("seg") == seg))
    value = "amount" if measure == "amount" else "count"
    cell = {(r["from"], r["to"]): r[value] for r in tr.iter_rows(named=True)}
    rows, share = [], {}
    for s in states:
        total = sum(cell.get((s, c), 0) for c in cols)
        cells = []
        for c in cols:
            x = cell.get((s, c), 0) / total if total else np.nan
            share[(s, c)] = x
            bg, fg = ("#FFF6D6", "#0B0B0C") if s == c else heat(x, 0.5)
            cells.append({"text": "—" if np.isnan(x) else f"{x * 100:.1f}".replace(".", ","), "bg": bg, "fg": fg,
                          "diag": s == c})
        rows.append({"state": s, "cells": cells,
                     "total": money(total) if measure == "amount" else f"{int(total):,}".replace(",", " ")})

    def flow(frm, to):
        num = sum(cell.get((f, t), 0) for f in frm for t in to)
        den = sum(cell.get((f, c), 0) for f in frm for c in cols)
        return pct(num / den, 1) if den else "—"

    if group == "dpd":
        key = [("Из 1–29 вернулись в 0 (вылечились)", flow(["1–29"], ["0"])),
               ("Из 0 ушли в просрочку", flow(["0"], ["1–29", "30–59", "60–89", "90+"])),
               ("Из 60–89 перешли в 90+", flow(["60–89"], ["90+"])),
               ("Из 90+ вернулись в 0", flow(["90+"], ["0"]))]
    else:
        good, bad = NPL_STATES[:NPL_FROM - 1], NPL_STATES[NPL_FROM - 1:]
        key = [(f"Из {NPL_FROM - 1} перешли в NPL (≥ {NPL_FROM})", flow([str(NPL_FROM - 1)], bad)),
               ("Из 1 сразу в NPL", flow(["1"], bad)),
               ("Из NPL вернулись в 1–2 (вылечились)", flow(bad, good)),
               ("NPL вышли из портфеля за месяц", flow(bad, [GONE]))]
    return {"cols": cols, "rows": rows, "key": key}


# ═══════════════════════════════════════ 8. EXCEL ══════════════════════════════════════

def xlsx(sheets):
    """[(sheet name, header row, rows)] → .xlsx bytes."""
    import openpyxl
    book = openpyxl.Workbook(write_only=True)
    for name, header, rows in sheets:
        page = book.create_sheet(name[:31])
        page.append(header)
        for row in rows:
            page.append(row)
    buffer = io.BytesIO()
    book.save(buffer)
    return buffer.getvalue()


def excel_sheets(res, kind, measure, seg=ALL):
    vintages, R, weight = matrix(res, kind, measure, seg)
    steps, reached = average_steps(R, weight)
    P, _ = projected(R, steps)
    k = R.shape[1]
    header = ["Поколение", "Кредитов" if measure == "count" else "Выдано"] + [f"MOB {m}" for m in range(k)]

    def grid(A):
        return [[month_name(v), float(weight[i])] + [None if np.isnan(x) else round(float(x), 6) for x in A[i]]
                for i, v in enumerate(vintages)]

    sheets = [("Факт", header, grid(R)), ("Факт + прогноз", header, grid(P)),
              ("Средняя кривая", ["MOB", "Шаг", "Накоплено", "Поколений дошло"],
               [[m, round(float(steps[m]), 6), round(float(c), 6), int(reached[m])]
                for m, c in enumerate(typical_curve(steps))])]
    tr = res["transitions"].filter((pl.col("group") == KINDS[kind]["group"]) & (pl.col("seg") == seg)).sort("from", "to")
    sheets.append(("Переходы", ["Из", "В", "Кредитов", "Сумма (начало)", "Сумма (через месяц)"],
                   [[r["from"], r["to"], r["count"], r["amount"], r["next_amount"]] for r in tr.iter_rows(named=True)]))
    return sheets
