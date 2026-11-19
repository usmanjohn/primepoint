"""Synthetic «svod» files for the dashboard demo — NO real data.

    python3 make_fake_svod.py OUT_DIR [--months 12] [--seed 7]

Writes OUT_DIR/svod_<date>.parquet for the first day of each of the last N months,
with the same columns process_portfel_best() produces (its groupby keys + the sums),
so the portfolio pages run unchanged on top of it.

Every number here is invented: the scale, the branch mix, the NPL shares. They are
chosen to look like a mid-size bank, not like any real one.
"""
import argparse
import datetime as dt
import pathlib

import numpy as np
import pandas as pd

# Branches: Tashkent districts + regional cities — plain place names, no bank's branch names.
# CITY must match region_t in portfel/functions.py (it splits Tashkent / regions).
CITY = ['Центр', 'Чиланзар', 'Юнусабад', 'Мирабад', 'Сергели', 'Яшнабад', 'Алмазар', 'Учтепа']
REGION = ['Наманган', 'Фергана', 'Бухара', 'Самарканд', 'Коканд', 'Термез',
          'Нукус', 'Андижан', 'Ургенч', 'Карши']
BRANCHES = CITY + REGION

# Department → (share of portfolio, products with weights, base NPL share, avg rate %)
DEPTS = {
    'kk': (0.45, {'корпоратив кредит': 1.0}, 0.030, 21.0),
    'rk': (0.35, {'ипотека вторичный рынок': .22, 'ипотека первичный рынок': .14,
                  'автокредит первичный рынок': .18, 'автокредит вторичный рынок': .10,
                  'потребительский кредит': .14, 'микрозаем': .10,
                  'кредитная карта прочая': .07, 'тезкор авто': .05}, 0.045, 25.0),
    'mk': (0.20, {'оборотный капитал': .30, 'основной капитал': .18, 'бизнес ипотека': .14,
                  'микрокредит ип': .14, 'кредит ип': .12, 'свободный бизнес': .12},
           0.060, 24.0),
}
OVERDUE = ['0-30', '30-90', '90-180', '181-364', '365+']
TOTAL_PORTFOLIO = 2.4e12   # invented scale, deliberately round


def one_month(rng, date, drift):
    rows = []
    branch_risk = rng.uniform(0.6, 1.6, len(BRANCHES))       # some branches are worse
    size = np.array([3.0 if b == 'Центр' else 1.6 if b in CITY else 1.0 for b in BRANCHES])
    for dept, (share, products, npl_base, rate) in DEPTS.items():
        # each department has its own branch mix; the centre is the biggest office
        branch_w = rng.dirichlet(size * 4)
        for b, branch in enumerate(BRANCHES):
            for product, pw in products.items():
                base = TOTAL_PORTFOLIO * drift * share * branch_w[b] * pw
                if base < 1e8:
                    continue
                npl_share = min(0.35, npl_base * branch_risk[b] * rng.uniform(0.7, 1.3))
                # split the cell into overdue buckets → categories → NPL flag
                good = 1 - npl_share
                watch = good * rng.uniform(0.02, 0.06)
                parts = {'0-30': good - watch, '30-90': watch,
                         '90-180': npl_share * .45, '181-364': npl_share * .35,
                         '365+': npl_share * .20}
                cat_of = {'0-30': 1, '30-90': 2, '90-180': 3, '181-364': 4, '365+': 5}
                for od, part in parts.items():
                    for currency, cshare in (('local', .82), ('global', .18)):
                        amount = base * part * cshare * rng.uniform(0.9, 1.1)
                        if amount < 5e6:
                            continue
                        cat = cat_of[od]
                        reserve_rate = {1: .01, 2: .10, 3: .25, 4: .50, 5: 1.0}[cat]
                        r = rate if currency == 'local' else rate * .45
                        written_off = amount * .15 if cat == 5 else 0.0
                        months_back = int(rng.integers(1, 60))
                        given = (pd.Timestamp(date) - pd.DateOffset(months=months_back)).strftime('%Y-%m')
                        rows.append({
                            'given_date': given, 'branch': branch, 'toboid': 1000 + b,
                            'department': dept, 'passport': product, 'currency': currency,
                            'oked': '96000' if dept == 'rk' else str(int(rng.choice([46900, 47110, 41200, 10710, 49410]))),
                            'category': cat, 'npl_category': cat, 'overdue_days': od,
                            'is_corporate': 'yes' if dept == 'kk' else 'no', 'has_any_amount': 'yes',
                            'given_amount': amount * rng.uniform(1.1, 1.6),
                            'brutto_95_amount': amount + written_off,
                            'brutto_amount': amount,
                            '95413_amount': written_off,
                            '91501_amount': 0.0,
                            'reserve_main_amount': amount * reserve_rate,
                            'reserve_int_amount': amount * reserve_rate * .05,
                            'reserve_comission_amount': 0.0,
                            'court_main_amount': amount * .3 if cat >= 4 else 0.0,
                            'court_int_amount': 0.0, '16405_amount': 0.0,
                            'overdue_main_amount': amount * (.1 if cat == 2 else .6 if cat >= 3 else 0),
                            'int_amount': amount * r / 1200,
                            '16377_amount': 0.0, '16377_2_amount': 0.0,
                            'peresmotren_amount': amount * .05 if cat >= 3 else 0.0,
                            'discount_amount': 0.0,
                            'int_rate_amount': (amount + written_off) * r / 100,
                            'deal_count': int(max(1, amount / {'kk': 4e9, 'rk': 6e7, 'mk': 2.5e8}[dept])),
                        })
    df = pd.DataFrame(rows)
    df['critical_amounts'] = df[[c for c in df.columns if c.endswith('_amount')
                                 and c not in ('int_rate_amount', 'has_any_amount')]].sum(axis=1)
    return df


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out_dir')
    ap.add_argument('--months', type=int, default=12)
    ap.add_argument('--seed', type=int, default=7)
    a = ap.parse_args()
    out = pathlib.Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(a.seed)
    first = dt.date.today().replace(day=1)
    for k in range(a.months - 1, -1, -1):
        date = (pd.Timestamp(first) - pd.DateOffset(months=k)).date()
        drift = 1 + 0.015 * (a.months - 1 - k)      # the book grows ~1.5% a month
        df = one_month(rng, date, drift)
        path = out / f'svod_{date}.parquet'
        df.to_parquet(path, index=False)
        npl = df.loc[df.npl_category >= 3, 'brutto_amount'].sum() / df.brutto_amount.sum()
        print(f'{path.name}: {len(df):5d} rows · portfolio {df.brutto_amount.sum()/1e12:.2f} трлн · NPL {npl:.1%}')


if __name__ == '__main__':
    main()
