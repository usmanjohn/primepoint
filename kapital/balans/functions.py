# -*- coding: utf-8 -*-
"""
Аналитический баланс: every number on the result page is calculated here.

The file has two halves:
  1. RULES  - plain lists you can edit (what to exclude, which accounts form a group).
  2. MATHS  - build_report(df) turns the balance file into the numbers for the page.

How an account is matched to a group
------------------------------------
By the beginning of its 5-digit number. The LONGEST matching beginning wins,
so ("177", ...) and ("17701", ...) can live side by side: 17701 goes to the
second one, 17705 to the first. The order of the lists does not matter.
An account that matches nothing goes to the section's "Прочие ..." group.

Sign in the database
--------------------
Assets (class 1) and expenses (class 5) come out NEGATIVE, liabilities,
equity and income POSITIVE. SIGN below turns them all into normal positive
money. A reserve (12599, 16399 ...) then comes out negative by itself and is
subtracted from its group without any special code.
If the bank ever changes this, change SIGN - nothing else.
"""
import datetime

import pandas as pd

# =====================================================================
# 1. RULES
# =====================================================================

SIGN = {'1': -1, '2': 1, '3': 1, '4': 1, '5': -1}

# Accounts left out of the totals (by the beginning of the account number).
EXCLUDE = {
    '1': ['161',     # Bosh ofis/filiallardan olinadigan mablag'lar - due FROM head office / branches
          '175'],    # Hukumat hisobvaraqlari - government accounts (pair of 23416)
    '2': ['222',     # Bosh ofis/filiallarga to'lanadigan mablag'lar - due TO head office / branches
          '23416'],  # Maxsus maqsadlar fondi - special purpose fund (pair of 175)
}

# Pairs that should cancel each other out. The page shows both sides and the difference.
PAIRS = [
    ('161', '222', 'Межфилиальные расчёты (161 ↔ 222)'),
    ('175', '23416', 'Счета правительства (175 ↔ 23416)'),
]

# (name, Font Awesome icon, account beginnings)
ASSET_GROUPS = [
    ('Касса', 'fa-money-bill-wave', ['101']),
    ('Средства в ЦБ', 'fa-building-columns', ['103']),
    ('Средства в других банках', 'fa-landmark', ['105']),
    ('Ценные бумаги и РЕПО', 'fa-file-contract', ['107', '108', '118', '159']),
    ('Инвестиции в дочерние и ассоциированные', 'fa-sitemap', ['158']),
    ('Кредитный портфель', 'fa-hand-holding-dollar',
     ['111', '119', '12', '13', '14', '150', '151', '152', '153', '154', '155', '156', '157', '17701']),
    ('Начисленные проценты и доходы', 'fa-percent', ['163', '164', '17703']),
    ('Основные средства и НМА', 'fa-building', ['165', '166']),
    ('Имущество банка (в т.ч. по залогу)', 'fa-house-circle-check', ['167']),
]
OTHER_ASSETS = ('Прочие активы', 'fa-boxes-stacked')

LIABILITY_GROUPS = [
    ('Депозиты до востребования', 'fa-wallet', ['202']),
    ('Сберегательные депозиты', 'fa-piggy-bank', ['204']),
    ('Срочные депозиты', 'fa-clock', ['206']),
    ('Прочие депозиты клиентов', 'fa-credit-card', ['226']),
    ('Средства ЦБ', 'fa-building-columns', ['208']),
    ('Средства других банков', 'fa-landmark', ['210']),
    ('Полученные кредиты', 'fa-file-invoice-dollar', ['216', '220']),
    ('Выпущенные ценные бумаги', 'fa-file-signature', ['236']),
    ('Субординированный долг', 'fa-layer-group', ['237']),
    ('Начисленные проценты к уплате', 'fa-percent', ['224']),
]
OTHER_LIABILITIES = ('Прочие обязательства', 'fa-list')

EQUITY_GROUPS = [
    ('Уставный капитал', 'fa-certificate', ['303']),
    ('Добавленный капитал', 'fa-plus', ['306']),
    ('Резервный капитал', 'fa-shield-halved', ['309']),
    ('Нераспределённая прибыль прошлых лет', 'fa-box-archive', ['31203']),
    ('Прибыль текущего года', 'fa-chart-line', ['31206']),
]
OTHER_EQUITY = ('Прочий капитал', 'fa-layer-group')

# P&L: (name, icon, account beginnings, kind). The kind decides where the line goes in
# "Как складывается прибыль": int = interest, nonint = other income/expense,
# opex = operating expenses, reserve = provisions, tax = profit tax.
INCOME_GROUPS = [
    ('Процентные доходы', 'fa-arrow-trend-up', ['40', '41', '42', '43', '44', '450', '451'], 'int'),
    ('Комиссии и прочие беспроцентные доходы', 'fa-coins', ['452', '459'], 'nonint'),
    ('Доходы от валютных операций', 'fa-dollar-sign', ['454'], 'nonint'),
    ('Торговые операции и инвестиции', 'fa-chart-pie', ['456', '457', '458'], 'nonint'),
]
OTHER_INCOME = ('Прочие доходы', 'fa-circle-plus', 'nonint')

EXPENSE_GROUPS = [
    ('Процентные расходы', 'fa-arrow-trend-down', ['50', '51', '52', '53', '54'], 'int'),
    ('Комиссии и прочие беспроцентные расходы', 'fa-receipt', ['551', '559'], 'nonint'),
    ('Убытки по валютным операциям', 'fa-dollar-sign', ['553'], 'nonint'),
    ('Убытки по торговым операциям и инвестициям', 'fa-chart-pie', ['556', '557', '558'], 'nonint'),
    ('Персонал', 'fa-users', ['561'], 'opex'),
    ('Аренда и содержание', 'fa-house', ['562'], 'opex'),
    ('Командировки и транспорт', 'fa-car', ['563'], 'opex'),
    ('Административные расходы', 'fa-briefcase', ['564'], 'opex'),
    ('Представительские и благотворительность', 'fa-handshake', ['565'], 'opex'),
    ('Амортизация', 'fa-building', ['566'], 'opex'),
    ('Страхование и налоги (кроме налога на прибыль)', 'fa-file-shield', ['567'], 'opex'),
    ('Резервы на возможные убытки', 'fa-shield-halved', ['568', '577'], 'reserve'),
    ('Налог на прибыль', 'fa-landmark-dome', ['569'], 'tax'),
]
OTHER_EXPENSES = ('Прочие расходы', 'fa-circle-minus', 'nonint')

# Groups used by the ratios (names must match the lists above).
LOANS = 'Кредитный портфель'
DEPOSITS = ['Депозиты до востребования', 'Сберегательные депозиты', 'Срочные депозиты', 'Прочие депозиты клиентов']
LIQUID = ['Касса', 'Средства в ЦБ', 'Средства в других банках']

# Contra accounts: reserves, depreciation, discounts, own shares. These REDUCE their group.
# This is the official list - every account the CBU chart of accounts (reg. 3336) marks
# "kontr-aktiv" / "kontr-passiv" in classes 1-3. Used only to show "брутто / резервы" per
# group: the totals are right without it, because the sign already subtracts them.
CONTRA = {
    '10599', '10791', '10799', '10891', '10899', '10999', '11195', '11199', '11599', '11899',
    '12199', '12399', '12599', '12699', '12799', '12899', '12999', '13099', '13199', '13299',
    '13399', '14399', '14499', '14599', '14799', '14999', '15099', '15199', '15299', '15399',
    '15499', '15599', '15799', '15899', '15991', '15999', '16398', '16399', '16498', '16499',
    '16511', '16519', '16531', '16539', '16543', '16551', '16563', '16593', '16605', '16699',
    '16713', '16799', '16899', '17700', '17701', '17703', '17705', '19911', '19933', '19945',
    '19999',
    '23698', '23798',                        # discount on issued securities / subordinated debt
    '30303', '30306', '30321', '30324',      # unpaid subscription, own shares bought back
}

CURRENCIES = {'000': 'UZS', '840': 'USD', '978': 'EUR', '643': 'RUB', '156': 'CNY',
              '826': 'GBP', '392': 'JPY', '756': 'CHF', '398': 'KZT'}
# one fixed colour per currency, so UZS / USD look the same on the assets and the liabilities bar
CURRENCY_COLOURS = {'UZS': '#F2C230', 'USD': '#2A2A2E', 'EUR': '#C9971A', 'RUB': '#8A867C', 'CNY': '#F7DC85'}

# Colours for the stacked bars (Kapitalbank palette: yellow first, then charcoal, gold, greys).
PALETTE = ['#F2C230', '#2A2A2E', '#C9971A', '#8A867C', '#F7DC85', '#55524B',
           '#E8B923', '#B9B5AB', '#6E5410', '#D9D5CB', '#3F3D38', '#FFF0B8']

# =====================================================================
# 2. MATHS
# =====================================================================


def match(acc, groups, other):
    """The group whose account beginning is the longest match; `other` if none."""
    best, best_len = other, 0
    for g in groups:
        for p in g[2]:
            if acc.startswith(p) and len(p) > best_len:
                best, best_len = g, len(p)
    return best


def starts(series, prefixes):
    return series.str.startswith(tuple(prefixes)) if prefixes else series.str.startswith('\0')


def pct(part, whole):
    return part / whole * 100 if whole else 0.0


def width(p):
    """Bar width for CSS - always a dot, never a locale comma ("12.5" not "12,5")."""
    return f'{max(0.0, min(100.0, p)):.2f}'


def section_rows(d, groups, other, total):
    """One row per group of a section: gross, reserves, net, share of the total."""
    rows = []
    for (name, icon), part in d.groupby(['grp', 'icon'], sort=False):
        net = part['money'].sum()
        contra = part.loc[part['contra'], 'money'].sum()
        rows.append({'name': name, 'icon': icon, 'net': net,
                     'gross': net - contra, 'reserve': -contra, 'has_reserve': abs(contra) > 0.5,
                     'pct': pct(net, total), 'w': width(pct(abs(net), total))})
    rows = [r for r in rows if abs(r['net']) > 0.5 or r['has_reserve']]
    rows.sort(key=lambda r: r['net'], reverse=True)
    for i, r in enumerate(rows):
        r['colour'] = PALETTE[i % len(PALETTE)]
    return rows


def label_groups(d, groups, other):
    picked = d['acc'].map(lambda a: match(a, groups, other))
    d = d.copy()
    d['grp'] = picked.map(lambda g: g[0])
    d['icon'] = picked.map(lambda g: g[1])
    if len(other) == 3:                               # P&L groups also carry a kind
        d['kind'] = picked.map(lambda g: g[-1])
    return d


def top_accounts(d, total, n=10):
    by = d.groupby('acc', as_index=False).agg(money=('money', 'sum'), grp=('grp', 'first'))
    by = by.reindex(by['money'].abs().sort_values(ascending=False).index).head(n)
    return [{'acc': r.acc, 'grp': r.grp, 'money': r.money, 'pct': pct(r.money, total)}
            for r in by.itertuples()]


def currency_split(d, total):
    by = d.groupby('cur')['money'].sum().sort_values(ascending=False)
    out = []
    for i, (cur, money) in enumerate(by.items()):
        if abs(money) > 0.5:
            out.append({'cur': cur, 'money': money, 'pct': pct(money, total),
                        'w': width(pct(money, total)),
                        'colour': CURRENCY_COLOURS.get(cur, PALETTE[(i + 5) % len(PALETTE)])})
    return out


def waterfall(steps):
    """steps: [(label, delta, is_subtotal)] -> rows with bar offsets for a CSS waterfall."""
    run, points = 0.0, []
    for label, delta, is_sub in steps:
        start = 0.0 if is_sub else run
        end = delta if is_sub else run + delta
        if not is_sub:
            run = end
        points.append((label, delta, is_sub, start, end))
    lo = min([0.0] + [min(s, e) for *_, s, e in points])
    hi = max([0.0] + [max(s, e) for *_, s, e in points])
    span = (hi - lo) or 1.0
    rows = []
    for label, delta, is_sub, start, end in points:
        left = (min(start, end) - lo) / span * 100
        rows.append({'label': label, 'value': end if is_sub else delta, 'is_sub': is_sub,
                     'neg': (end if is_sub else delta) < 0,
                     'left': width(left), 'w': width(max(abs(end - start) / span * 100, 0.4))})
    return rows


def build_report(df, date_str):
    """df: arcdate, account, currency, amount (as saved by balans_get). Returns the page context."""
    d = df.copy()
    d['acc'] = d['account'].astype(str).str.strip().str.replace(r'\.0$', '', regex=True).str[:5]
    d['cls'] = d['acc'].str[0]
    d['money'] = d['amount'].astype(float) * d['cls'].map(SIGN).fillna(0)
    d['contra'] = d['acc'].isin(CONTRA)
    cur = d['currency'].astype(str).str.strip().str.replace(r'\.0$', '', regex=True).str.zfill(3)
    d['cur'] = cur.map(CURRENCIES).fillna(cur)

    excluded = pd.Series(False, index=d.index)
    for cls, prefixes in EXCLUDE.items():
        excluded |= (d['cls'] == cls) & starts(d['acc'], prefixes)

    A = label_groups(d[(d['cls'] == '1') & ~excluded], ASSET_GROUPS, OTHER_ASSETS)
    L = label_groups(d[(d['cls'] == '2') & ~excluded], LIABILITY_GROUPS, OTHER_LIABILITIES)
    E = label_groups(d[d['cls'] == '3'], EQUITY_GROUPS, OTHER_EQUITY)
    I = label_groups(d[d['cls'] == '4'], INCOME_GROUPS, OTHER_INCOME)
    X = label_groups(d[d['cls'] == '5'], EXPENSE_GROUPS, OTHER_EXPENSES)

    assets, liabs, equity = A['money'].sum(), L['money'].sum(), E['money'].sum()
    income, expenses = I['money'].sum(), X['money'].sum()
    profit = income - expenses
    passive = liabs + equity

    asset_rows = section_rows(A, ASSET_GROUPS, OTHER_ASSETS, assets)
    liab_rows = section_rows(L, LIABILITY_GROUPS, OTHER_LIABILITIES, passive)
    equity_rows = section_rows(E, EQUITY_GROUPS, OTHER_EQUITY, passive)
    income_rows = section_rows(I, INCOME_GROUPS, OTHER_INCOME, income)
    expense_rows = section_rows(X, EXPENSE_GROUPS, OTHER_EXPENSES, expenses)

    # passive side bar = liabilities in their colours, then equity as one charcoal-free block
    passive_bar = [dict(r) for r in liab_rows] + [{'name': 'Капитал', 'net': equity, 'colour': '#0B0B0C',
                                                   'pct': pct(equity, passive), 'w': width(pct(equity, passive))}]
    for r in passive_bar:
        r['w'] = width(pct(r['net'], passive))

    # --- the checks -----------------------------------------------------------------
    def money_of(prefix):
        return d.loc[d['acc'].str.startswith(prefix), 'money'].sum()

    gap = assets - passive
    tolerance = max(1.0, abs(assets) * 1e-6)
    pairs = [{'label': label, 'a_val': money_of(a), 'l_val': money_of(l), 'diff': money_of(a) - money_of(l)}
             for a, l, label in PAIRS]
    for p in pairs:
        p['ok'] = abs(p['diff']) <= tolerance
    balance_ok = abs(gap) <= tolerance
    gap_is_profit = not balance_ok and abs(gap + profit) <= max(tolerance, abs(profit) * 1e-6)
    # leaving a pair out moves the balance by -(asset side - liability side)
    pairs_gap = -sum(p['diff'] for p in pairs)
    gap_is_pairs = not balance_ok and abs(gap - pairs_gap) <= tolerance

    # --- P&L by kind and the waterfall --------------------------------------------
    def kind_sum(frame, kind):
        return frame.loc[frame['kind'] == kind, 'money'].sum()

    int_inc, int_exp = kind_sum(I, 'int'), kind_sum(X, 'int')
    non_inc, non_exp = kind_sum(I, 'nonint'), kind_sum(X, 'nonint')
    opex, reserves_exp, tax = kind_sum(X, 'opex'), kind_sum(X, 'reserve'), kind_sum(X, 'tax')
    nii = int_inc - int_exp
    op_income = nii + non_inc - non_exp
    pre_provision = op_income - opex
    pre_tax = pre_provision - reserves_exp
    steps = waterfall([
        ('Процентные доходы', int_inc, False),
        ('Процентные расходы', -int_exp, False),
        ('Чистый процентный доход', nii, True),
        ('Беспроцентные доходы', non_inc, False),
        ('Беспроцентные расходы', -non_exp, False),
        ('Операционный доход', op_income, True),
        ('Операционные расходы', -opex, False),
        ('Прибыль до резервов', pre_provision, True),
        ('Резервы на возможные убытки', -reserves_exp, False),
        ('Прибыль до налога', pre_tax, True),
        ('Налог на прибыль', -tax, False),
        ('Чистая прибыль', pre_tax - tax, True),
    ])

    # --- ratios ---------------------------------------------------------------------
    loan = next((r for r in asset_rows if r['name'] == LOANS), None)
    gross_loans = loan['gross'] if loan else 0.0
    loan_reserves = loan['reserve'] if loan else 0.0
    deposits = sum(r['net'] for r in liab_rows if r['name'] in DEPOSITS)
    liquid = sum(r['net'] for r in asset_rows if r['name'] in LIQUID)
    try:
        day = datetime.date.fromisoformat(str(date_str)[:10])
        year_factor = 365 / day.timetuple().tm_yday       # P&L accounts run from 1 January
    except ValueError:
        year_factor = 1.0
    ratios = [
        {'name': 'Кредиты / Депозиты (LDR)', 'value': pct(gross_loans, deposits), 'icon': 'fa-scale-balanced',
         'how': 'Кредитный портфель брутто / депозиты клиентов (202, 204, 206, 226)'},
        {'name': 'Капитал / Активы', 'value': pct(equity, assets), 'icon': 'fa-shield',
         'how': 'Бухгалтерский капитал / активы. Это НЕ норматив адекватности капитала ЦБ (3697)'},
        {'name': 'Ликвидные активы / Активы', 'value': pct(liquid, assets), 'icon': 'fa-droplet',
         'how': 'Касса + ЦБ + другие банки (нетто) / активы'},
        {'name': 'Cost / Income (CIR)', 'value': pct(opex, op_income), 'icon': 'fa-gauge',
         'how': 'Операционные расходы (561–567) / операционный доход (без резервов и налога)'},
        {'name': 'Резервы / Кредиты', 'value': pct(loan_reserves, gross_loans), 'icon': 'fa-umbrella',
         'how': 'Резервы по кредитам (…99, 17701) / кредитный портфель брутто'},
        {'name': 'ROA (годовых)', 'value': pct(profit * year_factor, assets), 'icon': 'fa-percent',
         'how': 'Прибыль с начала года, приведённая к году / активы'},
        {'name': 'ROE (годовых)', 'value': pct(profit * year_factor, equity), 'icon': 'fa-chart-line',
         'how': 'Прибыль с начала года, приведённая к году / капитал'},
    ]

    rules = {
        'assets': ', '.join(EXCLUDE.get('1', [])) or '—',
        'liabilities': ', '.join(EXCLUDE.get('2', [])) or '—',
    }

    return {
        'date_str': date_str,
        'date_display': '.'.join(reversed(str(date_str)[:10].split('-'))),
        'total_assets': assets, 'total_liabilities': liabs, 'total_equity': equity, 'total_passive': passive,
        'total_income': income, 'total_expenses': expenses, 'net_profit': profit,
        'assets_structure': asset_rows, 'liabilities_structure': liab_rows, 'equity_structure': equity_rows,
        'income_structure': income_rows, 'expense_structure': expense_rows,
        'passive_bar': passive_bar,
        'liab_w': width(pct(liabs, passive)), 'equity_w': width(pct(equity, passive)),
        'equity_pct': pct(equity, passive),
        'balance_gap': gap, 'balance_ok': balance_ok, 'gap_is_profit': gap_is_profit,
        'pairs': pairs, 'gap_is_pairs': gap_is_pairs,
        'waterfall': steps, 'ratios': ratios, 'rules': rules,
        'top_assets': top_accounts(A, assets), 'top_liabilities': top_accounts(L, passive),
        'assets_by_currency': currency_split(A, assets), 'liabs_by_currency': currency_split(L, liabs),
    }
