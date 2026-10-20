"""
What an account is, from the first 5 digits of its number.

Source: the CBU chart of accounts for commercial banks, lex.uz/ru/docs/-5744540.
Account number = CCCCC VVV K SSSSSSSS NNN
                 balance  currency  check  client code  serial
                 account  (3)       digit  (8)          (3)

classify('13105') -> {'section': 'loan', 'status': 'overdue', 'label': 'Краткосрочный · Юрлица', ...}

Sections: loan · interest · deposit · offbalance · other.
Change a name or add an account here: nothing else needs to know.
"""

# ── Loans: main account (first 3 digits) → (term, borrower) ─────────────────────────
SHORT = {
    '121': 'Банки', '123': 'Правительство', '124': 'Бюджетные организации',
    '125': 'Физлица', '126': 'ИП', '127': 'Госпредприятия', '128': 'Фонд развития МСБ',
    '130': 'ННО', '131': 'Юрлица', '132': 'НБФИ', '133': 'Сельхозпроизводители',
}
LONG = {
    '144': 'Фонд развития МСБ', '145': 'Банки', '147': 'Правительство',
    '148': 'Бюджетные организации', '149': 'Физлица', '150': 'ИП', '151': 'Госпредприятия',
    '152': 'ННО', '153': 'Предприятия с иностр. инвест.', '154': 'НБФИ', '155': 'Юрлица',
}
LEASING_BORROWER = {   # 156xx: the last two digits say who the lessee is
    '01': 'Банки', '05': 'ИП', '07': 'Госпредприятия', '09': 'Предприятия с иностр. инвест.',
    '11': 'ННО', '13': 'Юрлица', '15': 'НБФИ',
}
COURT_BORROWER = {'01': 'Юрлица', '03': 'Физлица', '05': 'Лизинг', '07': 'ИП'}  # 157xx

# A few sub-accounts worth naming on their own.
LOAN_PRODUCT = {
    '12503': 'карта', '14913': 'карта',
    '12504': 'ипотека (госпрограмма)', '14903': 'ипотека (госпрограмма)',
    '12531': 'самозанятые', '14931': 'самозанятые',
}

# ── Accrued interest receivable (163xx) ──────────────────────────────────────────────
INTEREST = {
    '16309': ('current', 'Начисленные проценты по кредитам'),
    '16323': ('current', 'Начисленные проценты по лизингу'),
    '16377': ('overdue', 'Просроченные проценты'),
    '16379': ('restructured', 'Проценты с продлённым сроком'),
    '16398': ('reserve', 'Резерв по прочим активам'),
    '16399': ('reserve', 'Резерв по процентам'),
}

# ── Deposits ─────────────────────────────────────────────────────────────────────────
DEPOSIT_KIND = {'202': 'До востребования', '204': 'Сберегательный', '206': 'Срочный'}
DEPOSITOR = {   # last two digits of 202xx / 204xx / 206xx
    '02': 'гос. внебюджетные фонды', '03': 'бюджетные организации', '04': 'бюджетные организации',
    '05': 'внебюджетные фонды', '06': 'физлица', '08': 'частные предприятия',
    '10': 'госпредприятия', '12': 'ННО', '14': 'предприятия с иностр. инвест.',
    '16': 'НБФИ', '18': 'ИП', '96': 'прочие',
}
DEPOSIT_OTHER = {
    '22602': 'Покрытие по аккредитиву', '22606': 'Покрытие по импортным векселям',
    '22613': 'Средства на конвертацию', '22614': 'Сконвертированные средства',
    '22616': 'Средства ДБО физлиц', '22617': 'Карта пенсионера', '22618': 'Карта физлица',
    '22619': 'Карта ИП', '22620': 'Корпоративная карта', '22621': 'Карта самозанятого',
    '22650': 'Депонент',
}

# ── Off-balance (9xxxx) → (kind, name) ───────────────────────────────────────────────
OFFBALANCE = {
    '91809': ('unused', 'Неиспользованные кредитные линии'),
    '91901': ('commitment', 'Обязательства заёмщика: краткосрочные'),
    '91905': ('commitment', 'Обязательства заёмщика: долгосрочные'),
    '91907': ('commitment', 'Обязательства заёмщика: госкредиты'),
    '94501': ('collateral', 'Залог: ценные бумаги'),
    '94502': ('collateral', 'Залог: имущество и права'),
    '94503': ('collateral', 'Залог: гарантии и поручительства'),
    '94511': ('collateral', 'Залог по прочим активам: ценные бумаги'),
    '94512': ('collateral', 'Залог по прочим активам: имущество'),
    '94513': ('collateral', 'Залог по прочим активам: гарантии'),
    '90993': ('guarantee', 'Выданные гарантии и поручительства'),
    '91501': ('interest_off', 'Проценты вне баланса'),
    '91503': ('interest_off', 'Проценты с продлённым сроком (вне баланса)'),
    '91505': ('interest_off', 'Проценты и комиссии вне баланса'),
    '95409': ('claim', 'Требования, предъявленные должнику'),
    '95413': ('written_off', 'Списанные кредиты, лизинг, факторинг'),
    '95415': ('written_off', 'Прочие списанные активы'),
}

STATUS_NAMES = {
    'current': 'Срочные', 'restructured': 'Реструкт.', 'overdue': 'Просрочка',
    'court': 'Суд', 'reserve': 'Резерв',
}


def _loan(code):
    main, sub = code[:3], code[3:]
    if main in SHORT:
        status = {'05': 'overdue', '09': 'restructured', '99': 'reserve'}.get(sub, 'current')
        label = 'Краткосрочный · ' + SHORT[main]
    elif main in LONG:
        # long-term has no overdue sub-account: 05 is RESTRUCTURED here
        status = {'05': 'restructured', '99': 'reserve'}.get(sub, 'current')
        label = 'Долгосрочный · ' + LONG[main]
    elif main == '156':
        status = {'17': 'overdue', '19': 'restructured', '99': 'reserve'}.get(sub, 'current')
        label = 'Лизинг · ' + LEASING_BORROWER.get(sub, 'прочие')
    elif main == '157':
        status = 'reserve' if sub == '99' else 'court'
        label = 'Суд / принудительное взыскание · ' + COURT_BORROWER.get(sub, 'прочие')
    elif main == '111':
        status = {'03': 'overdue', '05': 'court', '99': 'reserve'}.get(sub, 'current')
        label = 'Факторинг'
    else:
        return None
    if code in LOAN_PRODUCT:
        label += ' (' + LOAN_PRODUCT[code] + ')'
    return {'section': 'loan', 'status': status, 'label': label}


def classify(code):
    """5-digit balance account -> dict with section, status/kind and a Russian label."""
    code = (code or '')[:5]

    loan = _loan(code)
    if loan:
        return loan

    if code.startswith('163'):
        status, label = INTEREST.get(code, ('current', 'Прочие начисленные проценты'))
        return {'section': 'interest', 'status': status, 'label': label}

    if code[:3] in DEPOSIT_KIND:
        who = DEPOSITOR.get(code[3:], 'прочие')
        return {'section': 'deposit', 'kind': code[:3], 'label': f'{DEPOSIT_KIND[code[:3]]} · {who}'}
    if code in DEPOSIT_OTHER:
        return {'section': 'deposit', 'kind': '226', 'label': DEPOSIT_OTHER[code]}
    if code.startswith('224'):
        return {'section': 'deposit', 'kind': '224', 'label': 'Начисленные проценты к выплате'}

    if code in OFFBALANCE:
        kind, label = OFFBALANCE[code]
        return {'section': 'offbalance', 'kind': kind, 'label': label}
    if code.startswith('909'):
        return {'section': 'offbalance', 'kind': 'trade', 'label': 'Аккредитивы и инкассо'}
    if code.startswith('9'):
        return {'section': 'offbalance', 'kind': 'other', 'label': 'Прочие внебалансовые'}

    return {'section': 'other', 'label': 'Прочие счета'}


def client_type(codes):
    """Guess the client type from the accounts he has: company, IP or person."""
    codes = set(codes)
    if codes & {'20208', '20210', '20212', '20214', '20216', '22620'} or any(
            c[:3] in ('131', '155') for c in codes):
        return 'Юридическое лицо'
    if codes & {'20218', '22619'} or any(c[:3] in ('126', '150') for c in codes):
        return 'Индивидуальный предприниматель'
    if codes & {'20206', '20406', '20606', '22617', '22618'} or any(
            c[:3] in ('125', '149') for c in codes):
        return 'Физическое лицо'
    return '—'
