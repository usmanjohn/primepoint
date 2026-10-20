"""
The portfolio: takes the raw rows from queries.load_client() and builds what the page shows.

No SQL here and no HTML: plain Python lists and dicts, so every number can be checked by hand.

Sign: in the database loans are negative and deposits positive. Here every amount is shown
as a positive number (abs), and the section says what it is.
"""
from collections import defaultdict
from datetime import date, datetime, timedelta

from .accounts import STATUS_NAMES, classify, client_type

MONTHS_RU = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
             'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
TURNOVER_MONTHS = 6
SOON_DAYS = 30          # a deal closing within this many days gets a yellow badge


def _day(v):
    """Oracle gives datetime; we compare dates."""
    return v.date() if isinstance(v, datetime) else v


def _pct(part, whole):
    return round(100 * part / whole, 1) if whole else None


def _pct_txt(part, whole):
    """'1,2%' the Russian way, for the KPI notes."""
    return f'{_pct(part, whole) or 0}%'.replace('.', ',')


def _month_end(first):
    """date(2026, 2, 1) -> date(2026, 2, 28)"""
    nxt = date(first.year + first.month // 12, first.month % 12 + 1, 1)
    return nxt - timedelta(days=1)


def _month_starts(pdate, n):
    """The n full months before pdate's month, oldest first: [date(2026,4,1), ..., date(2026,9,1)]."""
    y, m = pdate.year, pdate.month
    out = []
    for _ in range(n):
        m -= 1
        if m == 0:
            y, m = y - 1, 12
        out.append(date(y, m, 1))
    return out[::-1]


def _loans_table(loans):
    """One row per product (term · borrower): columns by status, plus the gross total."""
    rows = defaultdict(lambda: {k: 0.0 for k in STATUS_NAMES})
    for a in loans:
        rows[a['label']][a['status']] += a['amount']
    out = []
    for label, r in sorted(rows.items()):
        gross = r['current'] + r['restructured'] + r['overdue'] + r['court']
        out.append({'label': label, **r, 'gross': gross, 'net': gross - r['reserve']})
    return out


def _sum_by_label(accs):
    rows = defaultdict(lambda: {'amount': 0.0, 'count': 0})
    for a in accs:
        rows[a['label']]['amount'] += a['amount']
        rows[a['label']]['count'] += 1
    total = sum(r['amount'] for r in rows.values())
    return [{'label': k, **v, 'share': _pct(v['amount'], total)}
            for k, v in sorted(rows.items(), key=lambda kv: -kv[1]['amount'])], total


def _overdue(facts, pdate, months):
    """Overdue days from dealfact.

    Per month: for every overdue episode that touches the month, days = (episode end, or the
    last day of the month if it was still open then) − start + 1 (the first day counts).
    The month gets the MAX,
    separately for principal (type 1) and interest (type 2).
    Per deal: days overdue ON pdate (episodes still open that day).
    """
    per_month = []
    for start in months:
        end = _month_end(start)
        worst = {1: 0, 2: 0}
        for f in facts:
            began, ended = _day(f['valuedate']), _day(f['tilldate'])
            if began > end or ended < start:
                continue                                  # episode not in this month
            days = (min(ended, end) - began).days + 1
            worst[f['dealfacttypeid']] = max(worst[f['dealfacttypeid']], days)
        per_month.append(worst)

    now = defaultdict(int)
    for f in facts:
        began, ended = _day(f['valuedate']), _day(f['tilldate'])
        if began <= pdate < ended:
            now[f['dealid']] = max(now[f['dealid']], (pdate - began).days + 1)
    return per_month, now


def _deals(deals, links, by_id, pdate, overdue_now):
    """Each ACTIVE deal (balance > 0) with the balances of its own accounts."""
    accounts_of = defaultdict(set)
    for l in links:
        accounts_of[l['dealid']].add(l['accountid'])

    out = []
    for d in deals:
        accs = [by_id[i] for i in accounts_of[d['dealid']] if i in by_id]
        loan = [a for a in accs if a['section'] == 'loan' and a['status'] != 'reserve']
        balance = sum(a['amount'] for a in loan)
        overdue = sum(a['amount'] for a in loan if a['status'] in ('overdue', 'court'))
        interest = sum(a['amount'] for a in accs
                       if a['section'] == 'interest' and a['status'] != 'reserve')
        unused = sum(a['amount'] for a in accs
                     if a['section'] == 'offbalance' and a['kind'] == 'unused')
        if balance <= 0:
            continue                                      # nothing left on it: not shown
        given = d['given_amount_eq'] or 0
        overdue_days = overdue_now.get(d['dealid'], 0)
        close = _day(d['close_date'])
        days_left = (close - pdate).days if close else None

        if overdue or overdue_days:
            flag = ('danger', 'Просрочка')
        elif days_left is not None and days_left < 0 and balance:
            flag = ('danger', 'Срок истёк')
        elif days_left is not None and days_left <= SOON_DAYS:
            flag = ('warning', 'Скоро закрытие')
        else:
            flag = None

        out.append({
            'dealid': d['dealid'], 'rnk_dealid': d['rnk_dealid'], 'currencyid': d['currencyid'],
            'given': given, 'given_fx': d['given_amount'], 'balance': balance,
            'overdue': overdue, 'overdue_days': overdue_days, 'interest': interest, 'unused': unused,
            'close_date': close, 'days_left': days_left, 'flag': flag,
            'loan_accounts': sorted(a['accountno'] for a in loan),
            'account_ids': {a['account_id'] for a in loan},
        })
    out.sort(key=lambda x: -x['balance'])
    return out


def _rnk(deals):
    """Deals with the same facilitydealid = one credit line (RNK). No limit: just what was given."""
    groups = defaultdict(list)
    for d in deals:
        if d['rnk_dealid']:
            groups[d['rnk_dealid']].append(d)
    out = []
    for rnk, ds in groups.items():
        closes = [d['close_date'] for d in ds if d['close_date']]
        out.append({
            'rnk_dealid': rnk, 'deals': len(ds),
            'given': sum(d['given'] for d in ds), 'balance': sum(d['balance'] for d in ds),
            'overdue': sum(d['overdue'] for d in ds), 'unused': sum(d['unused'] for d in ds),
            'last_close': max(closes) if closes else None,
            'days_left': max(d['days_left'] for d in ds if d['days_left'] is not None)
            if closes else None,
        })
    out.sort(key=lambda x: -x['balance'])
    return out


def _turnover(rows, pdate):
    months = _month_starts(pdate, TURNOVER_MONTHS)
    data = {m: {'in': 0.0, 'out': 0.0, 'in_docs': 0, 'out_docs': 0} for m in months}
    for r in rows:
        m = _day(r['month'])
        if m in data:
            key = 'in' if r['direction'] == 'IN' else 'out'
            data[m][key] = float(r['amount'] or 0)
            data[m][key + '_docs'] = r['docs']
    top = max([max(v['in'], v['out']) for v in data.values()] + [0]) or 1
    out = []
    for m in months:
        v = data[m]
        out.append({'label': f'{MONTHS_RU[m.month - 1]} {m.year}', **v,
                    'net': v['in'] - v['out'],
                    'in_w': round(100 * v['in'] / top), 'out_w': round(100 * v['out'] / top)})
    return out


def build(data, contragentid, pdate):
    """The whole portfolio as one dict for the template and the Excel file."""
    accounts = data['accounts']
    for a in accounts:
        a.update(classify(a['bal_acc']))
        a['saldo'] = float(a['saldo'] or 0)
        a['amount'] = abs(a['saldo'])
    by_id = {a['account_id']: a for a in accounts}
    of = lambda section: [a for a in accounts if a['section'] == section]

    # ── loans ──
    loans = of('loan')
    loan_rows = _loans_table(loans)
    gross = sum(r['gross'] for r in loan_rows)
    overdue = sum(r['overdue'] for r in loan_rows)
    court = sum(r['court'] for r in loan_rows)
    restructured = sum(r['restructured'] for r in loan_rows)
    reserve = sum(r['reserve'] for r in loan_rows)
    interest = of('interest')
    interest_due = sum(a['amount'] for a in interest if a['status'] != 'reserve')
    interest_overdue = sum(a['amount'] for a in interest if a['status'] == 'overdue')

    # ── deposits and off-balance ──
    deposit_rows, deposits = _sum_by_label(of('deposit'))
    off = of('offbalance')
    off_rows, _ = _sum_by_label(off)
    off_sum = lambda kind: sum(a['amount'] for a in off if a['kind'] == kind)
    collateral = off_sum('collateral')

    # ── deals and credit lines ──
    months = _month_starts(pdate, TURNOVER_MONTHS)
    overdue_months, overdue_now = _overdue(data.get('overdue', []), pdate, months)
    deals = _deals(data['deals'], data['links'], by_id, pdate, overdue_now)
    rnk = _rnk(deals)
    in_deals = set().union(*(d['account_ids'] for d in deals)) if deals else set()
    loose = [a for a in loans if a['status'] != 'reserve' and a['account_id'] not in in_deals]

    # ── turnover ──
    turnover = _turnover(data['turnover'], pdate)
    for row, worst in zip(turnover, overdue_months):     # same 6 months, same order
        row['od_days'], row['pr_days'] = worst[1], worst[2]
    max_overdue_days = max([max(w.values()) for w in overdue_months] + [0])
    avg_in = sum(t['in'] for t in turnover) / TURNOVER_MONTHS
    avg_out = sum(t['out'] for t in turnover) / TURNOVER_MONTHS

    kpis = [
        {'label': 'Кредиты (брутто)', 'value': gross, 'note': f'{len(deals)} сделок'},
        {'label': 'Просрочка + суд', 'value': overdue + court,
         'note': _pct_txt(overdue + court, gross) + ' портфеля',
         'bad': bool(overdue + court)},
        {'label': 'Резервы', 'value': reserve, 'note': _pct_txt(reserve, gross) + ' портфеля'},
        {'label': 'Депозиты и счета', 'value': deposits, 'note': 'все пассивы клиента'},
        {'label': 'Чистая позиция', 'value': deposits - gross,
         'note': 'депозиты − кредиты', 'bad': deposits - gross < 0},
        {'label': 'Обеспечение', 'value': collateral,
         'note': 'покрытие ' + _pct_txt(collateral, gross) if gross else 'кредитов нет'},
        {'label': 'Поступления в мес.', 'value': avg_in, 'note': f'среднее за {TURNOVER_MONTHS} мес.'},
    ]

    return {
        'contragentid': contragentid, 'pdate': pdate, 'name': data['name'] or '—',
        'client_type': client_type(a['bal_acc'] for a in accounts),
        'kpis': kpis,
        'loans': {
            'rows': loan_rows, 'gross': gross, 'net': gross - reserve, 'reserve': reserve,
            'current': sum(r['current'] for r in loan_rows), 'restructured': restructured,
            'overdue': overdue, 'court': court,
            'problem_pct': _pct(overdue + court, gross),
            'interest_due': interest_due, 'interest_overdue': interest_overdue,
            'written_off': off_sum('written_off'),
        },
        'deals': deals, 'rnk': rnk, 'loose': loose,
        'deposits': {'rows': deposit_rows, 'total': deposits},
        'offbalance': {'rows': off_rows, 'collateral': collateral,
                       'coverage_pct': _pct(collateral, gross), 'unused': off_sum('unused'),
                       'guarantees': off_sum('guarantee')},
        'turnover': {'months': turnover, 'avg_in': avg_in, 'avg_out': avg_out,
                     'total_in': avg_in * TURNOVER_MONTHS,
                     # "the debt equals N months of income"
                     'max_overdue_days': max_overdue_days,
                     'debt_months': round(gross / avg_in, 1) if avg_in and gross else None},
        'accounts': accounts,
    }
