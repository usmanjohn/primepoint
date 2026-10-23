"""
Everything between the database and the page: save, read, clean, count.

THE ROAD OF THE DATA
1. save_today()     Oracle (the state right now) → datasets/collateral/collateral_<today>.parquet.
                     Runs only when someone presses «Обновить из базы». A second run on
                     the same day overwrites that day's file. The file keeps raw text.
   save_accounts()   the same moment: the 945xx accounts → accounts_<today>.parquet.
2. read_day(day)     parquet → prepare() → a clean pandas table, kept in memory,
                     so clicking around the page does not read the file again.
                     The cleaned table is ALSO saved (collateral_<day>.ready.parquet): a gunicorn
                     worker that has not seen the day yet reads it in ~2 s instead of cleaning
                     for ~20-50 s. Change process.py or queries.py and it is made again by itself.
                     The page opens the newest file (latest_day) unless a date is clicked.
3. prepare(table)    numbers become numbers, dates become dates, spelling variants of
                     the same brand are merged, and the extra columns the page groups by
                     are added (brand, age_group, area_group, dep_term ...).
4. build_page(...)   the filtered table → KPIs, cards, the list of deals.
5. accounts_page()   collateral against the 945xx accounts (the «Счета 945xx» page).
   delete_day(day)   «Удалить выбранные»: every file of an old day.

THE TABLE (one row = one collateral deal)
    kind       car / property / other
    subkind    for «other»: equipment, deposit, insurance ... (see queries.OTHERS)
    dealid, mfo, tobo, parent_id, currency, amount, market, subtype, note
    + one column per parameter (names from the dicts in queries.py)
    + the extra columns made by prepare()

All the settings you may want to change are in the block just below.
"""
import numbers
import os
from datetime import date, datetime
from pathlib import Path

import pandas as pd
from django.conf import settings

from . import queries


# ═══════════════════════════════ SETTINGS ═══════════════════════════════════════════

DATA_DIR = Path(settings.BASE_DIR) / "datasets" / "collateral"
TOP = 12              # rows in a card; the rest goes into «Остальные»
PAGE_SIZE = 50        # deals per page in the list
EMPTY = "не указано"  # what an empty value is called in the cards
ACTIVE, CLOSED = "Действующее", "Закрыто"   # the «Статус» card (see prepare: closedate)

KINDS = {
    "car":      {"label": "Автотранспорт", "icon": "fa-car"},
    "property": {"label": "Недвижимость", "icon": "fa-building"},
    "other":    {"label": "Прочее обеспечение", "icon": "fa-layer-group"},
}

# The groups of «others» (same keys as queries.OTHERS): name and icon.
SUBKINDS = {
    "equipment":  {"label": "Оборудование", "icon": "fa-gears"},
    "deposit":    {"label": "Депозиты", "icon": "fa-piggy-bank"},
    "securities": {"label": "Ценные бумаги", "icon": "fa-chart-line"},
    "goods":      {"label": "Товары в обороте (ТМЦ)", "icon": "fa-boxes-stacked"},
    "insurance":  {"label": "Страховые полисы", "icon": "fa-shield-halved"},
    "land":       {"label": "Право аренды земли", "icon": "fa-map-location-dot"},
    "harvest":    {"label": "Будущий урожай", "icon": "fa-wheat-awn"},
    "jewelry":    {"label": "Ювелирные изделия", "icon": "fa-gem"},
    "rights":     {"label": "Имущественные права", "icon": "fa-file-contract"},
    "guarantee":  {"label": "Гарантии", "icon": "fa-handshake"},
}

# Parameters that are money in TIYIN (divided by 100), as in the old scripts.
# If another one turns out to be in tiyin too (BOOKVALUE?), add its column here.
MONEY = ["car_price", "cadastre_value", "eq_cost", "sec_discount"]

# Parameters that are plain numbers (areas, counts, mileage ...).
NUMBERS = ["mileage", "total_area", "land_area", "built_area", "useful_area", "living_area",
           "rooms", "sec_count", "sec_nominal", "sec_total", "goods_book", "goods_book_eq",
           "land_lease_area", "harvest_area", "harvest_crop_area", "jewel_count", "jewel_weight"]

YEARS = ["made_year", "built_year", "eq_year"]

DATES = ["pasp_date", "pasp_end", "in_use_date", "eq_in_use", "eq_doc_date", "dep_end",
         "sec_issue", "sec_pay_date", "goods_list_date", "goods_act_date", "policy_date",
         "closedate"]

# The ways a date may be written in paramvalue. The first that fits wins.
DATE_FORMATS = ["%d.%m.%Y", "%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%d.%m.%Y %H:%M:%S", "%d/%m/%Y"]

# Codes → names. If a column holds codes (1, 2, 3 ...) instead of words, add it here:
#     "fuel": {"1": "Бензин", "2": "Метан", "3": "Пропан"},
CODES = {
    "currency": {"0": "UZS", "000": "UZS", "860": "UZS", "840": "USD", "978": "EUR",
                 "643": "RUB", "826": "GBP", "756": "CHF", "156": "CNY", "392": "JPY",
                 "398": "KZT"},
}

# Words that mean «look in the other column» (Марка = «Другое» → take «Марка (если другое)»).
OTHER_WORDS = ["ДРУГОЕ", "ДРУГАЯ", "ДРУГОЙ", "ПРОЧЕЕ", "ПРОЧИЕ", "BOSHQA", "OTHER"]

# Values that mean «nothing here».
BLANKS = ["", "-", "—", "NULL", "null", "None", "none", "nan", "N/A"]

# THE CARDS. Each card is one breakdown: (column, title, icon, order)
#   order "amount" = biggest sum first;  "label" = in the natural order (years, buckets).
CARS_CARDS = [
    ("brand", "Марка", "fa-car", "amount"),
    ("model", "Модель", "fa-car-side", "amount"),
    ("made_year", "Год выпуска", "fa-calendar", "label"),
    ("age_group", "Возраст автомобиля", "fa-hourglass-half", "label"),
    ("transport_type", "Тип транспорта", "fa-truck", "amount"),
    ("fuel", "Вид топлива", "fa-gas-pump", "amount"),
    ("gearbox", "Коробка передач", "fa-gears", "amount"),
    ("color", "Цвет", "fa-palette", "amount"),
    ("country", "Страна производителя", "fa-earth-asia", "amount"),
    ("buy_market", "Рынок приобретения", "fa-store", "amount"),
    ("pasp_state", "Техпаспорт", "fa-id-card", "label"),
]
PROPERTY_CARDS = [
    ("building_kind", "Вид недвижимости", "fa-house", "amount"),
    ("building_type", "Тип недвижимости", "fa-city", "amount"),
    ("area_group", "Общая площадь", "fa-ruler-combined", "label"),
    ("rooms_group", "Комнат", "fa-door-open", "label"),
    ("built_decade", "Год постройки", "fa-calendar", "label"),
    ("econ_zone", "Экономическая зона", "fa-map", "amount"),
    ("cadastre_org", "Регистрирующий орган", "fa-landmark", "amount"),
    ("address", "Адрес", "fa-location-dot", "amount"),     # shows once ADDRESS is in queries.py
]
OTHERS_CARDS = [
    ("subkind", "Вид обеспечения", "fa-layer-group", "amount"),
]
# Extra cards when one group of «others» is open.
SUBKIND_CARDS = {
    "equipment": [("eq_type", "Тип оборудования", "fa-gears", "amount"),
                  ("eq_maker", "Производитель", "fa-industry", "amount"),
                  ("eq_country", "Страна производства", "fa-earth-asia", "amount"),
                  ("eq_year", "Год производства", "fa-calendar", "label")],
    "deposit":   [("dep_type", "Тип депозита", "fa-piggy-bank", "amount"),
                  ("dep_term", "До истечения депозита", "fa-hourglass-half", "label"),
                  ("dep_branch", "Отделение депозита", "fa-building-columns", "amount")],
    "securities": [("sec_name", "Ценная бумага", "fa-chart-line", "amount"),
                   ("depository", "Депозитарий", "fa-vault", "amount"),
                   ("sec_term", "До погашения", "fa-hourglass-half", "label")],
    "goods":     [("goods_name", "Товар", "fa-boxes-stacked", "amount")],
    "insurance": [("policy_year", "Год полиса", "fa-calendar", "label")],
    "rights":    [("rights_object", "Объект права", "fa-file-contract", "amount")],
    "guarantee": [("guarantee_on_dep", "Гарантия на депозитном счёте", "fa-handshake", "amount"),
                  ("has_documents", "Подтверждающие документы", "fa-file-circle-check", "amount")],
}
# Cards on every page.
COMMON_CARDS = [
    ("status", "Статус", "fa-lock-open", "label"),
    ("size_group", "Сумма залога", "fa-scale-balanced", "label"),
    ("currency_name", "Валюта", "fa-coins", "amount"),
    ("mfo", "Филиал (МФО)", "fa-building-columns", "amount"),
    ("source", "Источник приобретения", "fa-hand-holding-dollar", "amount"),
]

# Buckets: (upper limit, name). A value goes into the first bucket whose limit it is under.
AGE_GROUPS = [(4, "до 3 лет"), (8, "4–7 лет"), (13, "8–12 лет"), (21, "13–20 лет"), (999, "старше 20 лет")]
AREA_GROUPS = [(50, "до 50 м²"), (100, "50–100 м²"), (200, "100–200 м²"), (500, "200–500 м²"),
               (1000, "500–1 000 м²"), (10**12, "больше 1 000 м²")]
SIZE_GROUPS = [(50e6, "до 50 млн"), (100e6, "50–100 млн"), (300e6, "100–300 млн"),
               (1e9, "300 млн – 1 млрд"), (5e9, "1–5 млрд"), (1e18, "больше 5 млрд")]
TERM_GROUPS = [(0, "истёк"), (31, "до 30 дней"), (91, "31–90 дней"), (366, "91–365 дней"),
               (10**6, "больше года")]
PASP_GROUPS = [(0, "истёк"), (91, "истекает в 90 дней"), (10**6, "действует")]

# THE 945xx ACCOUNTS (the codes and their names are in queries.ACCOUNT_CODES).
# Which account the law expects for each kind of collateral: car, property, or a group of
# «others» (keys of SUBKINDS). A kind not listed here is expected on DEFAULT_ACCOUNTS.
EXPECTED_ACCOUNTS = {
    "securities": ["94501", "94511"],
    "insurance":  ["94503", "94513"],
    "guarantee":  ["94503", "94513"],
}
DEFAULT_ACCOUNTS = ["94502", "94512"]    # cars, property, equipment, deposits, goods ...
TOLERANCE = 1.0                          # сум: a smaller difference is rounding, not a mismatch


def names(groups):
    """[(4, 'до 3 лет'), (8, '4–7 лет')] → ['до 3 лет', '4–7 лет']"""
    return [name for limit, name in groups]


# The order of the rows in the cards sorted by "label": buckets go small → big, not A → Z.
ORDER = {
    "age_group": names(AGE_GROUPS), "area_group": names(AREA_GROUPS),
    "size_group": names(SIZE_GROUPS), "dep_term": names(TERM_GROUPS),
    "sec_term": names(TERM_GROUPS), "pasp_state": names(PASP_GROUPS),
    "built_decade": ["до 1960"], "status": [ACTIVE, CLOSED],
}

# The deals list: which columns to show for each kind (column, header).
LIST_COLUMNS = {
    "car": [("brand", "Марка"), ("model", "Модель"), ("made_year", "Год"), ("plate", "Госномер")],
    "property": [("building_kind", "Вид"), ("cadastre_no", "Кадастровый номер"),
                 ("total_area", "Площадь, м²"), ("rooms", "Комнат"), ("address", "Адрес")],
    "other": [("subkind", "Вид"), ("title", "Описание")],
    "all": [("kind", "Вид"), ("title", "Описание")],
}

# Names of the extra columns made by prepare(), for the deal page and Excel.
EXTRA_LABELS = {
    "kind": "Вид обеспечения", "subkind": "Группа", "dealid": "Код сделки обеспечения",
    "mfo": "МФО", "tobo": "Код ТОБО", "parent_id": "Код анкеты / РНК",
    "currency": "Код валюты", "currency_name": "Валюта", "amount": "Сумма обеспечения, экв.",
    "market": "Рыночная стоимость", "subtype": "Подтип обеспечения",
    "note": "Дополнительная информация", "brand": "Марка (итог)", "model": "Модель (итог)",
    "age_group": "Возраст автомобиля", "pasp_state": "Техпаспорт", "area_group": "Площадь",
    "rooms_group": "Комнат", "built_decade": "Год постройки", "size_group": "Сумма залога",
    "dep_term": "До истечения депозита", "sec_term": "До погашения", "policy_year": "Год полиса",
    "title": "Описание", "issue": "Проверка данных",
    "status": "Статус", "closedate": "Дата закрытия",
    "acc_count": "Счетов 945xx", "acc_balance": "Остаток на 945xx", "acc_no": "Счёт 945xx",
    "acc_diff": "Остаток 945xx минус сумма залога", "acc_right": "Счёт нужной группы",
    "acc_shared": "Счёт общий с другим залогом",
}


# ═══════════════════════════════ 1. SAVE ═══════════════════════════════════════════
# Each «Обновить из базы» writes, for its day:
#     collateral_<day>.parquet        what Oracle returned (raw text) — the «Parquet» button
#     accounts_<day>.parquet          the 945xx accounts (or accounts_<day>.error.txt if that query failed)
#     collateral_<day>.ready.parquet  the same table already CLEANED by prepare(): opening a day
#                                     reads this one in a second instead of cleaning for half a minute.
#                                     It is only a copy: delete it and it is made again.

def file_for(day):
    """datasets/collateral/collateral_2026-10-01.parquet"""
    return DATA_DIR / f"collateral_{day.isoformat()}.parquet"


def accounts_file(day):
    return DATA_DIR / f"accounts_{day.isoformat()}.parquet"


def accounts_error_file(day):
    return DATA_DIR / f"accounts_{day.isoformat()}.error.txt"


def ready_file(day):
    return DATA_DIR / f"collateral_{day.isoformat()}.ready.parquet"


def files_of(day):
    """Every file that belongs to `day` (the ones that exist)."""
    paths = [file_for(day), accounts_file(day), accounts_error_file(day), ready_file(day)]
    return [path for path in paths if path.exists()]


def saved_days():
    """Dates that already have a file, newest first: [{'day': date, 'size': '12.3 МБ'}]."""
    days = []
    for path in sorted(DATA_DIR.glob("collateral_*.parquet"), reverse=True):
        try:
            day = date.fromisoformat(path.stem.replace("collateral_", ""))
        except ValueError:                       # collateral_<day>.ready.parquet and the like
            continue
        size = sum(f.stat().st_size for f in files_of(day))
        days.append({"day": day, "size": f"{size / 1e6:.1f} МБ", "bytes": size})
    return days


def latest_day():
    """The newest saved date, or None if nothing was downloaded yet."""
    days = saved_days()
    return days[0]["day"] if days else None


def updated_at(day):
    """When the file of `day` was written (date and time)."""
    return datetime.fromtimestamp(file_for(day).stat().st_mtime)


def as_text(column):
    """
    Any column → text, without surprises:
    numbers from Oracle (12345 or 12345.0) → '12345'; extra spaces removed; '', '-', 'NULL' → empty.
    Text is never turned into a number, so '01' and 'AB 0012' keep their zeros.
    """
    if pd.api.types.is_numeric_dtype(column):
        return column.round().astype("Int64").astype("string")
    text = column.astype("string").str.strip().str.replace(r"\s+", " ", regex=True)
    return text.mask(text.isin(BLANKS))


def write(table, path):
    """
    Save a table as parquet. zstd packs our text about 2.5 times smaller than the default.
    Written to a temporary file first, then swapped: nobody ever reads a half-written file
    (the process id in the name: two workers may write the same file at once).
    """
    temporary = path.with_name(f"{path.name}.{os.getpid()}.tmp")
    table.to_parquet(temporary, index=False, compression="zstd")
    temporary.replace(path)


def save_today():
    """Ask Oracle for the three kinds and the accounts (state right now), save under today's date."""
    day = date.today()
    parts = queries.load_all()
    frames = []
    for kind in ["car", "property", "other"]:        # this order matters: see drop_duplicates
        part = parts[kind]
        part["kind"] = kind
        frames.append(part)
    table = pd.concat(frames, ignore_index=True)

    # A deal with car AND property parameters is counted once, as the first kind.
    table = table.drop_duplicates("dealid", keep="first")

    for column in table.columns:
        if column in ["amount", "market"]:
            table[column] = pd.to_numeric(table[column], errors="coerce")
        else:
            table[column] = as_text(table[column])

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    write(table, file_for(day))
    save_accounts(day)
    read_day(day)          # clean it now and write the ready copy: the first click is then fast
    return day


def save_accounts(day):
    """
    The 945xx accounts of `day`. If the query fails (a table name not set yet ...),
    the collateral is still saved and the error is kept in a small text file for the page.
    """
    accounts_error_file(day).unlink(missing_ok=True)
    try:
        accounts = queries.load_accounts()
    except Exception as error:
        accounts_file(day).unlink(missing_ok=True)
        accounts_error_file(day).write_text(str(error), encoding="utf-8")
        return
    for column in accounts.columns:
        if column == "balance":
            accounts[column] = pd.to_numeric(accounts[column], errors="coerce")
        else:
            accounts[column] = as_text(accounts[column])
    write(accounts, accounts_file(day))


def delete_day(day):
    """Remove every file of `day`. The newest day is never removed: it is the current data."""
    if day == latest_day():
        return False
    for path in files_of(day):
        path.unlink()
    return True


# ═══════════════════════════════ 2. READ ═══════════════════════════════════════════

# The last table read, so clicking around the page does not read the file every time.
# Each gunicorn worker keeps its own; a new download (the file changes) is read again.
MEMORY = {"key": None, "table": None, "accounts": None}

# If one of these files is newer than a ready copy, the copy is out of date (you changed a
# setting, a card, a check ...) and is made again.
CODE_FILES = [Path(__file__), Path(queries.__file__)]


def read_day(day):
    """The clean table of the file saved on `day` (the file must exist)."""
    path = file_for(day)
    key = (str(path), path.stat().st_mtime)
    if MEMORY["key"] != key:
        MEMORY["accounts"] = read_accounts(day)
        MEMORY["table"] = read_ready(day, MEMORY["accounts"])
        MEMORY["key"] = key
    return MEMORY["table"]


def accounts_of(day):
    """The 945xx accounts of `day` (None if they were not loaded). Call read_day first."""
    read_day(day)
    return MEMORY["accounts"]


def read_accounts(day):
    """accounts_<day>.parquet → a table with the first 5 digits as «code»; None if there is no file."""
    path = accounts_file(day)
    if not path.exists():
        return None
    accounts = pd.read_parquet(path)
    accounts["accountno"] = accounts["accountno"].astype("string")
    accounts["dealid"] = accounts["dealid"].astype("string")
    accounts["code"] = accounts["accountno"].str[:5]
    accounts["arcdate"] = to_date(accounts["arcdate"])
    # An off-balance account may keep its balance with a minus sign; we compare the size.
    accounts["balance"] = accounts["balance"].abs()
    return accounts


def read_ready(day, accounts):
    """The cleaned table: from the ready copy if it is fresh, otherwise clean now and save the copy."""
    ready = ready_file(day)
    inputs = [file_for(day), accounts_file(day)] + CODE_FILES
    newest_input = max(path.stat().st_mtime for path in inputs if path.exists())
    if ready.exists() and ready.stat().st_mtime > newest_input:
        return pd.read_parquet(ready)
    table = prepare(pd.read_parquet(file_for(day)), day, accounts)
    try:
        write(table, ready)
    except Exception:          # no space, no rights ...: the page works without the copy, only slower
        pass
    return table


# ═══════════════════════════════ 3. PREPARE ════════════════════════════════════════

def to_number(column):
    """'1 234,56' / '1234.56' / 1234.56 → 1234.56 ; anything else → empty."""
    text = column.astype("string").str.replace(r"[\s ]", "", regex=True)
    text = text.str.replace(",", ".", regex=False)
    return pd.to_numeric(text, errors="coerce")


def to_date(column):
    """
    Text in any of DATE_FORMATS → a date; anything else → empty.
    A year outside 1900 … 2100 is a typo ('19.10.0218') → empty too: pandas 3 reads year 218
    happily, but it does not fit in a date column and the whole page crashed on it.
    """
    text = column.astype("string").str.strip()
    result = pd.Series(pd.NaT, index=column.index, dtype="datetime64[ns]")
    for fmt in DATE_FORMATS:
        missing = result.isna() & text.notna()
        if not missing.any():
            break
        parsed = pd.to_datetime(text[missing], format=fmt, errors="coerce")
        parsed = parsed[parsed.dt.year.between(1900, 2100)]
        result[parsed.index] = parsed.astype("datetime64[ns]")
    return result


def to_year(column, day):
    """'2019' / '2019.0' / '01.01.2019' → 2019 ; a year outside 1900 … next year → empty."""
    years = to_number(column)
    from_dates = to_date(column).dt.year
    years = years.fillna(from_dates)
    return years.where((years >= 1900) & (years <= day.year + 1))


def relabel(column, new_value, empty=EMPTY):
    """
    column.map(new_value), but new_value is called once per DIFFERENT value, not once per
    row: a million rows hold only a few hundred different brands, so this takes a moment
    where .map() takes seconds. Empty cells become `empty`.
    """
    codes, values = pd.factorize(column)     # codes: row → number of its value, -1 = empty
    done = [new_value(v) for v in values] + [empty]     # code -1 picks the last one
    return pd.Series(pd.array(done, dtype="object")[codes], index=column.index, dtype="object")


def same_spelling(column):
    """
    'CHEVROLET', 'Chevrolet ', 'chevrolet' are one brand: all three get the spelling
    used most often. Empty → EMPTY, so the cards have a «не указано» row.
    """
    text = column.astype("string")               # already cleaned by as_text when saved
    best = {}                                    # 'CHEVROLET' → 'Chevrolet'
    for spelling in text.value_counts().index:   # most frequent first
        best.setdefault(spelling.upper(), spelling)
    return relabel(text, lambda spelling: best[spelling.upper()])


def bucket(values, groups):
    """Numbers → bucket names, e.g. 7 years → '4–7 лет'. Empty → EMPTY."""
    result = pd.Series(EMPTY, index=values.index, dtype="object")
    done = values.isna()
    for limit, name in groups:
        here = ~done & (values < limit)
        result[here] = name
        done = done | here
    return result


def year_text(years):
    """2019.0 → '2019' (as text: a number would be printed as '2 019' by Django)."""
    return years.round().astype("Int64").astype("string").astype("object").fillna(EMPTY)


def days_left(dates, day):
    """How many days from `day` until each date (negative = already past)."""
    return (dates - pd.Timestamp(day)).dt.days


def first_filled(table, columns):
    """For each row: the first of `columns` that is not empty."""
    result = pd.Series(pd.NA, index=table.index, dtype="object")
    for column in columns:
        if column in table:
            result = result.fillna(table[column].mask(table[column] == EMPTY))
    return result


def prepare(table, day, accounts=None):
    """
    The raw text from the file → a table ready for counting. Read top to bottom.
    `accounts`: the 945xx accounts of the same day (or None) — see add_accounts.
    """
    table = table.copy()

    # numbers, dates, years
    for column in MONEY:
        if column in table:
            table[column] = to_number(table[column]) / 100
    for column in NUMBERS:
        if column in table:
            table[column] = to_number(table[column])
    for column in DATES:
        if column in table:
            table[column] = to_date(table[column])
    for column in YEARS:
        if column in table:
            table[column] = to_year(table[column], day)

    # closed = closedate is filled and not later than the day of the file; else active.
    # (Files saved before closedate was added have no such column: all active.)
    table["status"] = ACTIVE
    if "closedate" in table:
        table.loc[table["closedate"] <= pd.Timestamp(day), "status"] = CLOSED

    # the group of «others»: the first group in queries.OTHERS that has a filled parameter
    table["subkind"] = pd.Series(pd.NA, index=table.index, dtype="object")
    for name, params in queries.OTHERS.items():
        columns = [column for column, label in params.values() if column in table]
        if columns:
            has_any = table[columns].notna().any(axis=1)
            table["subkind"] = table["subkind"].mask(table["subkind"].isna() & has_any, name)
    table["subkind_key"] = table["subkind"]      # 'deposit' — the account check needs the key
    table["subkind"] = relabel(table["subkind"], lambda s: SUBKINDS[s]["label"] if s in SUBKINDS else None,
                               empty=None)
    table.loc[table["kind"] != "other", "subkind"] = EMPTY
    table["subkind"] = table["subkind"].fillna("Без параметров")

    # cars: brand and model («Другое» → the free-text column), age, tech passport
    for name in ["brand", "model"]:
        main, other = table.get(name + "_main"), table.get(name + "_other")
        if main is not None:
            use_other = main.isna() | main.str.upper().isin(OTHER_WORDS)
            table[name] = main.mask(use_other, other) if other is not None else main
    if "made_year" in table:
        table["age_group"] = bucket(day.year - table["made_year"], AGE_GROUPS)
        table["made_year"] = year_text(table["made_year"])
    if "pasp_end" in table:
        left = days_left(table["pasp_end"], day)
        table["pasp_state"] = bucket(left, PASP_GROUPS)

    # property: area, rooms, decade
    if "total_area" in table:
        table["area_group"] = bucket(table["total_area"], AREA_GROUPS)
    if "rooms" in table:
        table["rooms_group"] = relabel(table["rooms"].where(table["rooms"] > 0),
            lambda r: "5 и больше" if r >= 5 else str(int(r)))
    if "built_year" in table:
        table["built_decade"] = relabel(table["built_year"],
            lambda y: "до 1960" if y < 1960 else f"{int(y) // 10 * 10}-е")
        table["built_year"] = year_text(table["built_year"])

    # others: terms of deposits and securities, year of the policy, equipment year
    if "dep_end" in table:
        table["dep_term"] = bucket(days_left(table["dep_end"], day), TERM_GROUPS)
    if "sec_pay_date" in table:
        table["sec_term"] = bucket(days_left(table["sec_pay_date"], day), TERM_GROUPS)
    if "policy_date" in table:
        table["policy_year"] = year_text(table["policy_date"].dt.year)
    if "eq_year" in table:
        table["eq_year"] = year_text(table["eq_year"])

    # every page: size of the collateral, currency name
    table["size_group"] = bucket(table["amount"], SIZE_GROUPS)
    codes = CODES["currency"]
    table["currency_name"] = relabel(table["currency"], lambda c: codes.get(c, c))
    for column, names in CODES.items():
        if column != "currency" and column in table:
            table[column] = relabel(table[column], lambda c: names.get(c, c), empty=None)

    # every column a card groups by: one spelling, EMPTY for blanks
    for column, title, icon, order in all_cards():
        if column in table and column not in ["kind", "subkind"]:
            table[column] = same_spelling(table[column])

    # a short description for the deals list (after the spelling merge: «Chevrolet», not «CHEVROLET»)
    table["title"] = first_filled(table, [
        "eq_name", "dep_name", "sec_name", "goods_name", "rights_asset", "rights_object",
        "policy_no", "land_cadastre_no", "brand", "building_kind", "note"])
    if "model" in table:                                   # cars: «Chevrolet Malibu»
        car = (table["kind"] == "car") & (table["model"] != EMPTY)
        table.loc[car, "title"] = table.loc[car, "brand"] + " " + table.loc[car, "model"]
    table["kind_name"] = relabel(table["kind"], lambda k: KINDS[k]["label"])

    # the 945xx accounts: balance, account number, is it the right account
    if accounts is not None:
        table = add_accounts(table, accounts)

    # the checks («Проверка данных»): one True/False column per check
    for code, (label, rows) in find_problems(table, day).items():
        table["problem_" + code] = rows.fillna(False).astype(bool)

    # Text columns → «category»: each different value is kept once and the rows only point
    # to it. A million rows of brands, colours, branches take ~15 times less memory
    # (every gunicorn worker keeps its own copy!) and grouping them is faster.
    for column in table.columns:
        if table[column].dtype == object or pd.api.types.is_string_dtype(table[column]):
            table[column] = table[column].astype("category")
    return table


def add_accounts(table, accounts):
    """
    Per collateral deal, from its 945xx accounts:
        acc_count    how many accounts are linked to it
        acc_balance  the balance on them together (сум)
        acc_no       the account number (the first one, if several)
        acc_right    True if at least one of them is the account the law expects (EXPECTED_ACCOUNTS)
        acc_shared   True if one of its accounts is linked to another collateral deal too
    """
    linked = accounts[accounts["dealid"].notna()].copy()
    # dealid → 'car' / 'property' / the group of «others» ('deposit' ...)
    kind = table["kind"].where(table["kind"] != "other", table["subkind_key"])
    kind_of = pd.Series(kind.to_numpy(dtype=object), index=table["dealid"].to_numpy(dtype=object))
    linked["kind"] = linked["dealid"].astype("object").map(kind_of)
    # an «other» without parameters: we do not know what it is, so we do not judge its account
    linked["right"] = [pd.isna(kind) or code in EXPECTED_ACCOUNTS.get(kind, DEFAULT_ACCOUNTS)
                       for code, kind in zip(linked["code"], linked["kind"])]
    linked["shared"] = linked.groupby("accountid")["dealid"].transform("nunique") > 1
    per_deal = linked.groupby("dealid", observed=True).agg(
        acc_count=("accountno", "size"), acc_balance=("balance", "sum"),
        acc_no=("accountno", "first"), acc_right=("right", "any"), acc_shared=("shared", "any"))
    table = table.merge(per_deal, left_on="dealid", right_index=True, how="left")
    table["acc_count"] = table["acc_count"].fillna(0).astype(int)
    table["acc_balance"] = table["acc_balance"].fillna(0.0)
    for column in ["acc_right", "acc_shared"]:
        table[column] = table[column].astype("boolean").fillna(False).astype(bool)
    table["acc_diff"] = table["acc_balance"] - table["amount"].fillna(0)
    return table


def find_problems(t, day):
    """
    The data checks: code → (what is wrong, which rows). Add your own here — it appears
    on the page and becomes a filter by itself.
    """
    today = pd.Timestamp(day)
    car, prop, other = t["kind"] == "car", t["kind"] == "property", t["kind"] == "other"
    active = t["status"] == ACTIVE if "status" in t else pd.Series(True, index=t.index)

    def has(column):
        """True where the column is filled (and False everywhere if it does not exist)."""
        if column not in t:
            return pd.Series(False, index=t.index)
        return t[column].notna() & (t[column] != EMPTY)

    def before_day(column, days=0):
        """True where the date in the column is more than `days` days in the past."""
        if column not in t:
            return pd.Series(False, index=t.index)
        return t[column] < today - pd.Timedelta(days=days)

    checks = {
        "no_market":    ("Нет рыночной стоимости", t["market"].isna() | (t["market"] <= 0)),
        "over_market":  ("Сумма залога больше рыночной стоимости", t["amount"] > t["market"]),
        "no_parent":    ("Не привязан к анкете / РНК", t["parent_id"].isna()),
        "car_no_plate": ("Авто без госномера", car & ~has("plate")),
        "car_no_year":  ("Авто без года выпуска", car & ~has("made_year")),
        "car_pasp_old": ("Техпаспорт просрочен, а залог действует", car & active & before_day("pasp_end")),
        "prop_no_cad":  ("Недвижимость без кадастрового номера", prop & ~has("cadastre_no")),
        "prop_no_area": ("Недвижимость без площади", prop & ~(t.get("total_area", pd.Series(0, index=t.index)) > 0)),
        "dep_expired":  ("Депозит истёк, а залог действует", other & active & before_day("dep_end")),
        "sec_expired":  ("Ценная бумага погашена, а залог действует", other & active & before_day("sec_pay_date")),
        # A policy is usually for one year; the table only has the date it was issued.
        "policy_old":   ("Полису больше года, а залог действует",
                         other & active & before_day("policy_date", days=365)),
    }

    # Against the 945xx accounts (only when they were loaded: see add_accounts).
    nothing = pd.Series(False, index=t.index)
    loaded = "acc_count" in t
    linked = t["acc_count"] > 0 if loaded else nothing
    differs = (t["acc_diff"].abs() >= TOLERANCE) if loaded else nothing
    checks.update({
        "acc_none":   ("Залог действует, а счёта 945xx нет", active & ~linked if loaded else nothing),
        "acc_diff":   ("Остаток на 945xx не равен сумме залога", active & linked & differs),
        "acc_wrong":  ("Залог на счёте не той группы 945xx", linked & ~t["acc_right"] if loaded else nothing),
        "acc_shared": ("Один счёт 945xx на несколько залогов", t["acc_shared"] if loaded else nothing),
    })
    return checks


def all_cards():
    """Every card of every page (used to know which columns to clean)."""
    cards = CARS_CARDS + PROPERTY_CARDS + OTHERS_CARDS + COMMON_CARDS
    for extra in SUBKIND_CARDS.values():
        cards = cards + extra
    return cards


# ═══════════════════════════════ 4. COUNT ══════════════════════════════════════════

def number(x, digits=0):
    """1234567.891 → '1 234 568' (digits=0) or '1 234 567,9' (digits=1). Empty → '—'."""
    if x is None or pd.isna(x):
        return "—"
    x = round(x, digits) + 0          # + 0 turns -0.0 into 0.0, so no «-0»
    text = f"{x:,.{digits}f}"
    return text.replace(",", " ").replace(".", ",")


def mln(x):
    """Money in millions: 1 234 567 890 → '1 234,6'."""
    return number(x / 1e6, 1) if x is not None and not pd.isna(x) else "—"


def percent(part, whole):
    return round(part / whole * 100, 1) if whole else 0


def filter_keys():
    """Every word allowed as a filter in the address (?brand=…&made_year=…)."""
    keys = {"kind", "issue"}
    for column, title, icon, order in all_cards():
        keys.add(column)
    return keys


def apply_filters(table, filters):
    """Keep only the rows that match every (column, value) in `filters`."""
    for column, value in filters:
        if column == "issue":
            if "problem_" + value in table:
                table = table[table["problem_" + value]]
        elif column in table:
            table = table[table[column] == value]
    return table


def cards_for(filters):
    """Which cards a page shows, depending on what is already chosen."""
    chosen = dict(filters)
    kind = chosen.get("kind")
    if kind == "car":
        cards = CARS_CARDS
    elif kind == "property":
        cards = PROPERTY_CARDS
    elif kind == "other":
        cards = OTHERS_CARDS
        for key, info in SUBKINDS.items():
            if chosen.get("subkind") == info["label"]:
                cards = cards + SUBKIND_CARDS.get(key, [])
    else:
        cards = []
    return cards + COMMON_CARDS


def make_card(part, column, title, icon, order, filters):
    """
    One breakdown card: the rows of `part` grouped by `column`, each row with count, sum,
    share of the sum and the bar width. Returns None if the column does not exist.
    """
    if column not in part:
        return None
    # observed=True: only the values that are in `part` (a category column knows them all)
    groups = part.groupby(column, observed=True).agg(count=("dealid", "size"), amount=("amount", "sum"))
    groups = groups.reset_index()
    groups[column] = groups[column].astype("object")   # sort as words, not in category order
    total = part["amount"].sum()

    if order == "label":
        known = ORDER.get(column, [])
        groups["empty"] = groups[column] == EMPTY        # «не указано» always at the bottom
        groups["place"] = groups[column].map(lambda v: known.index(v) if v in known else len(known))
        groups = groups.sort_values(["empty", "place", column])
        shown, rest = groups.head(40), groups.iloc[40:]
    else:
        groups = groups.sort_values("amount", ascending=False)
        shown, rest = groups.head(TOP), groups.iloc[TOP:]

    chosen = dict(filters)
    biggest = shown["amount"].max() if len(shown) else 0
    rows = []
    for _, g in shown.iterrows():
        rows.append({
            "label": g[column],
            "value": g[column],
            "count": number(g["count"]),
            "amount": mln(g["amount"]),
            "share": number(percent(g["amount"], total), 1),
            "width": percent(g["amount"], biggest) if biggest else 0,
            "active": chosen.get(column) == g[column],
            "empty": g[column] == EMPTY,
        })
    card = {"column": column, "title": title, "icon": icon, "rows": rows,
            "clickable": column not in chosen,
            "nothing": len(rows) == 1 and rows[0]["empty"]}
    if len(rest):
        card["rest"] = {"n": len(rest), "count": number(rest["count"].sum()),
                        "amount": mln(rest["amount"].sum()),
                        "share": number(percent(rest["amount"].sum(), total), 1)}
    return card


def kind_tiles(part):
    """The three big tiles on the first page: cars / property / other."""
    total = part["amount"].sum()
    sums = part.groupby("kind", observed=True).agg(count=("dealid", "size"), amount=("amount", "sum"),
                                    market=("market", "sum"))
    tiles = []
    for key, info in KINDS.items():
        count, amount, market = sums.loc[key] if key in sums.index else (0, 0, 0)
        tiles.append({"key": key, "label": info["label"], "icon": info["icon"],
                      "count": number(count), "amount": mln(amount), "market": mln(market),
                      "share": number(percent(amount, total), 1),
                      "width": percent(amount, total)})
    return tiles


def subkind_tiles(part):
    """Small tiles for the groups of «others»."""
    tiles = []
    for key, info in SUBKINDS.items():
        rows = part[part["subkind"] == info["label"]]
        if len(rows):
            tiles.append({"label": info["label"], "icon": info["icon"],
                          "count": number(len(rows)), "amount": mln(rows["amount"].sum())})
    return tiles


def kpis(part, kind, day):
    """The numbers at the top: [{'label', 'value', 'note', 'icon', 'bad'}]."""
    amount, market = part["amount"].sum(), part["market"].sum()
    out = [
        {"label": "Сделок обеспечения", "value": number(len(part)), "icon": "fa-file-signature",
         "note": "строк в файле"},
        {"label": "Сумма залога", "value": mln(amount), "icon": "fa-scale-balanced",
         "note": "млн сум, эквивалент"},
        {"label": "Рыночная стоимость", "value": mln(market), "icon": "fa-tags",
         "note": "млн сум"},
        {"label": "Залог / рынок", "value": number(percent(amount, market), 1) + " %",
         "icon": "fa-percent", "note": "сколько от рыночной цены принято в залог"},
        {"label": "Средний залог", "value": mln(amount / len(part)) if len(part) else "—",
         "icon": "fa-equals", "note": "млн сум на сделку"},
        {"label": "Действующих", "value": number((part["status"] == ACTIVE).sum()),
         "icon": "fa-lock-open", "note": f"закрыто: {number((part['status'] == CLOSED).sum())}"},
    ]
    if "acc_balance" in part:
        active = part[part["status"] == ACTIVE]
        gap = active["acc_balance"].sum() - active["amount"].sum()
        out.append({"label": "На счетах 945xx", "value": mln(active["acc_balance"].sum()),
                    "icon": "fa-book", "note": f"у действующих; разница {mln(gap)} млн",
                    "bad": abs(gap) >= TOLERANCE})
    if kind == "car" and "made_year" in part:
        years = pd.to_numeric(part["made_year"].astype("object"), errors="coerce")
        ages = day.year - years
        old = (ages > 10).sum()
        out.append({"label": "Средний возраст", "value": number(ages.mean(), 1) + " г.",
                    "icon": "fa-hourglass-half", "note": f"старше 10 лет: {number(old)}"})
        if "mileage" in part:
            out.append({"label": "Средний пробег", "value": number(part["mileage"].mean()),
                        "icon": "fa-road", "note": "км"})
        bad = int(part["problem_car_pasp_old"].sum())
        out.append({"label": "Техпаспорт просрочен", "value": number(bad), "icon": "fa-id-card",
                    "note": "у действующих залогов", "bad": bad > 0})
    if kind == "property" and "total_area" in part:
        area = part["total_area"].sum()
        both = part[(part["total_area"] > 0) & (part["market"] > 0)]
        per_m2 = both["market"].sum() / both["total_area"].sum() if len(both) else None
        out.append({"label": "Общая площадь", "value": number(area), "icon": "fa-ruler-combined",
                    "note": "м²"})
        out.append({"label": "Цена за м²", "value": number(per_m2), "icon": "fa-house",
                    "note": "сум, рыночная стоимость / площадь"})
        if "cadastre_value" in part:
            out.append({"label": "Кадастровая стоимость", "value": mln(part["cadastre_value"].sum()),
                        "icon": "fa-landmark", "note": "млн сум"})
    if kind == "other":
        if "dep_end" in part:
            soon = (part["dep_term"].isin(["истёк", "до 30 дней"]) & (part["status"] == ACTIVE)).sum()
            out.append({"label": "Депозиты: истекают", "value": number(soon), "icon": "fa-piggy-bank",
                        "note": "истёк или до 30 дней, у действующих", "bad": soon > 0})
        if "jewel_weight" in part and part["jewel_weight"].notna().any():
            out.append({"label": "Вес ювелирных изделий", "value": number(part["jewel_weight"].sum(), 1),
                        "icon": "fa-gem", "note": "сумма по полю «Вес»"})
        if "harvest_crop_area" in part and part["harvest_crop_area"].notna().any():
            out.append({"label": "Посевная площадь", "value": number(part["harvest_crop_area"].sum(), 1),
                        "icon": "fa-wheat-awn", "note": "га, будущий урожай"})
    return out


def problems(part):
    """The «Проверка данных» list for the rows on the page."""
    out = []
    labels = find_problems_labels()
    for code, label in labels.items():
        n = int(part["problem_" + code].sum()) if "problem_" + code in part else 0
        if n:
            out.append({"code": code, "label": label, "count": number(n),
                        "share": number(percent(n, len(part)), 1)})
    return out


def find_problems_labels():
    """code → label of every check, without computing them (an empty table is enough)."""
    empty = pd.DataFrame({"kind": [], "market": [], "amount": [], "parent_id": [], "status": []})
    return {code: label for code, (label, rows) in find_problems(empty, date.today()).items()}


def deal_list(part, kind, page):
    """One page of the deals list, biggest first."""
    columns = [(c, h) for c, h in LIST_COLUMNS.get(kind or "all", []) if c in part]
    pages = max(1, -(-len(part) // PAGE_SIZE))          # rounded up
    page = min(max(1, page), pages)
    # sort only the amount column, then take the 50 rows of this page (sorting the whole
    # table would copy every column of every row: seconds on a million rows)
    order = part["amount"].sort_values(ascending=False).index
    rows = []
    for _, r in part.loc[order[(page - 1) * PAGE_SIZE: page * PAGE_SIZE]].iterrows():
        cells = []
        for column, header in columns:
            value = r[column]
            if column == "kind":
                value = KINDS[value]["label"]
            elif isinstance(value, numbers.Number) and not pd.isna(value):
                value = number(value, 1 if value % 1 else 0)
            cells.append("—" if value is None or (not isinstance(value, str) and pd.isna(value)) else value)
        rows.append({"dealid": r["dealid"], "mfo": r["mfo"] if pd.notna(r["mfo"]) else "—",
                     "cells": cells, "amount": number(r["amount"]),
                     "market": number(r["market"]),
                     "warn": bool(pd.notna(r["market"]) and r["amount"] > r["market"]),
                     "balance": number(r["acc_balance"]) if "acc_balance" in r else None,
                     "off": "acc_diff" in r and abs(r["acc_diff"]) >= TOLERANCE})
    return {"headers": [h for c, h in columns], "rows": rows, "page": page, "pages": pages,
            "total": number(len(part)), "accounts": "acc_balance" in part}


def build_page(table, day, filters, page=1):
    """Everything the page shows for the chosen date and filters."""
    part = apply_filters(table, filters)
    kind = dict(filters).get("kind")
    cards = []
    for column, title, icon, order in cards_for(filters):
        card = make_card(part, column, title, icon, order, filters)
        if card:
            cards.append(card)
    context = {
        "kind": kind,
        "kind_info": KINDS.get(kind),
        "kpis": kpis(part, kind, day),
        "cards": cards,
        "problems": problems(part),
        "deals": deal_list(part, kind, page),
        "empty": len(part) == 0,
    }
    if not kind:
        context["tiles"] = kind_tiles(part)
    if kind == "other" and "subkind" not in dict(filters):
        context["subtiles"] = subkind_tiles(part)
    for info in SUBKINDS.values():                      # a group of «others» is open
        if dict(filters).get("subkind") == info["label"]:
            context["kind_info"] = info
    return context


def filter_label(column, value):
    """What a chosen filter is called in the breadcrumbs: ('Марка', 'Chevrolet')."""
    if column == "kind":
        return "Вид", KINDS.get(value, {}).get("label", value)
    if column == "issue":
        return "Проверка", find_problems_labels().get(value, value)
    for c, title, icon, order in all_cards():
        if c == column:
            return title, value
    return column, value


# ═══════════════════════════════ 5. ONE DEAL, EXCEL ════════════════════════════════

def labels():
    """column → Russian name, for every column that may be in the table."""
    return {**EXTRA_LABELS, **queries.all_labels()}


def show(value):
    """One value as text for the deal page and Excel."""
    if value is None or (not isinstance(value, str) and pd.isna(value)):
        return None
    if isinstance(value, pd.Timestamp):
        return value.strftime("%d.%m.%Y")
    if isinstance(value, numbers.Number):
        return number(value, 2 if value % 1 else 0)
    if value == EMPTY:
        return None
    return str(value)


def deal_card(table, dealid, accounts=None):
    """All filled fields of one deal, in sections: [{'title', 'rows': [(label, value)]}]."""
    rows = table[table["dealid"] == dealid]
    if rows.empty:
        return None
    r = rows.iloc[0]
    names = labels()
    main = ["kind_name", "subkind", "status", "closedate", "dealid", "mfo", "tobo", "parent_id", "currency_name",
            "amount", "market", "subtype", "source", "note"]
    names["kind_name"] = "Вид обеспечения"
    sections = [{"title": "Основное", "icon": "fa-circle-info",
                 "rows": [(names.get(c, c), show(r.get(c))) for c in main if show(r.get(c))]}]
    params = {"car": queries.CARS, "property": queries.PROPERTY}.get(r["kind"], queries.others_flat())
    filled = [(label, show(r.get(column))) for column, label in params.values() if show(r.get(column))]
    sections.append({"title": "Параметры", "icon": "fa-list", "rows": filled})
    issues = [label for code, label in find_problems_labels().items() if r.get("problem_" + code)]
    card = {"dealid": dealid, "kind": KINDS[r["kind"]], "title": show(r.get("title")),
            "amount": number(r["amount"]), "market": number(r["market"]),
            "sections": sections, "issues": issues}
    if accounts is not None and r["status"] == ACTIVE:      # only active collateral is compared
        mine = accounts[accounts["dealid"] == dealid]
        card["accounts"] = [{"no": a.accountno, "code_name": queries.ACCOUNT_CODES.get(a.code, "не 945xx"),
                             "name": show(a.account_name) or "", "balance": number(a.balance, 2),
                             "arcdate": show(a.arcdate) or "—"} for a in mine.itertuples()]
        card["balance"] = number(mine["balance"].sum())
        card["gap"] = number(mine["balance"].sum() - (r["amount"] if pd.notna(r["amount"]) else 0))
        card["gap_bad"] = abs(mine["balance"].sum() - (r["amount"] if pd.notna(r["amount"]) else 0)) >= TOLERANCE
    return card


def excel_table(table, filters):
    """The filtered rows with Russian headers, only the columns that have something in them."""
    part = apply_filters(table, filters).sort_values("amount", ascending=False)
    names = labels()
    skip = {"title", "kind_name", "subkind_key"} | {c for c in part.columns if c.startswith("problem_")}
    columns = [c for c in part.columns if c not in skip and part[c].notna().any()
               and not (part[c] == EMPTY).all()]
    out = part[columns].copy()
    for c in columns:
        if pd.api.types.is_datetime64_any_dtype(out[c]):
            out[c] = out[c].dt.date
        elif isinstance(out[c].dtype, pd.CategoricalDtype) or pd.api.types.is_string_dtype(out[c]):
            out[c] = out[c].astype("object").replace(EMPTY, None)
    out["kind"] = out["kind"].astype("object").map(lambda k: KINDS[k]["label"])
    return out.rename(columns=names)


# ═══════════════════════════════ 6. THE 945xx ACCOUNTS PAGE ════════════════════════

def orphans(accounts):
    """945xx accounts with a balance but no collateral deal linked to them, biggest first."""
    rows = accounts[accounts["dealid"].isna() & (accounts["balance"] >= TOLERANCE)
                    & accounts["code"].isin(list(queries.ACCOUNT_CODES))]
    return rows.sort_values("balance", ascending=False)


def accounts_page(table, accounts):
    """
    Collateral against the 945xx accounts: totals, one row per account code, the checks
    (they link to the main page, already filtered), and the accounts nobody claims.
    """
    active = table[table["status"] == ACTIVE]
    ours = accounts[accounts["code"].isin(list(queries.ACCOUNT_CODES))]
    # every account once (an account linked to two deals is in `accounts` twice)
    once = ours.drop_duplicates("accountid")
    lost = orphans(accounts)
    gap = once["balance"].sum() - active["amount"].sum()

    kpis = [
        {"label": "Залог, действующий", "value": mln(active["amount"].sum()), "icon": "fa-scale-balanced",
         "note": f"млн сум · {number(len(active))} сделок"},
        {"label": "Остаток на 945xx", "value": mln(once["balance"].sum()), "icon": "fa-book",
         "note": f"млн сум · {number(len(once))} счетов"},
        {"label": "Разница", "value": mln(gap), "icon": "fa-not-equal",
         "note": "остаток на счетах минус залог", "bad": abs(gap) >= TOLERANCE},
        {"label": "Счета без залога", "value": number(len(lost)), "icon": "fa-circle-question",
         "note": f"с остатком {mln(lost['balance'].sum())} млн", "bad": len(lost) > 0},
    ]
    if not queries.FIND_ORPHANS:
        kpis[-1].update(value="—", note="поиск выключен (FIND_ORPHANS)", bad=False)

    codes = []
    for code, name in queries.ACCOUNT_CODES.items():
        here = once[once["code"] == code]
        lost_here = lost[lost["code"] == code]
        codes.append({"code": code, "name": name, "count": number(len(here)),
                      "balance": mln(here["balance"].sum()),
                      "linked": number(here["dealid"].notna().sum()),
                      "lost": number(len(lost_here)), "lost_amount": mln(lost_here["balance"].sum())})
    elsewhere = accounts[~accounts["code"].isin(list(queries.ACCOUNT_CODES))].drop_duplicates("accountid")

    checks = []
    for code, label in find_problems_labels().items():
        if code.startswith("acc_"):
            rows = table[table["problem_" + code]]
            checks.append({"code": code, "label": label, "count": number(len(rows)),
                           "amount": mln(rows["amount"].sum()),
                           "balance": mln(rows["acc_balance"].sum()), "bad": len(rows) > 0})

    by_kind = []
    for key, info in KINDS.items():
        rows = active[active["kind"] == key]
        by_kind.append({"key": key, "label": info["label"], "icon": info["icon"],
                        "amount": mln(rows["amount"].sum()), "balance": mln(rows["acc_balance"].sum()),
                        "gap": mln(rows["acc_balance"].sum() - rows["amount"].sum()),
                        "bad": abs(rows["acc_balance"].sum() - rows["amount"].sum()) >= TOLERANCE})

    return {"kpis": kpis, "codes": codes, "checks": checks, "by_kind": by_kind,
            "elsewhere": {"count": number(len(elsewhere)), "balance": mln(elsewhere["balance"].sum())},
            "lost_total": number(len(lost)), "find_orphans": queries.FIND_ORPHANS,
            "lost": [{"no": a.accountno, "name": show(a.account_name) or "", "balance": number(a.balance, 2),
                      "arcdate": show(a.arcdate) or "—"} for a in lost.head(100).itertuples()]}


def orphans_excel(accounts):
    """Every 945xx account with a balance and no collateral deal, for Excel."""
    out = orphans(accounts)[["accountno", "account_name", "balance", "arcdate", "accountid"]].copy()
    out["arcdate"] = out["arcdate"].dt.date
    return out.rename(columns={"accountno": "Счёт", "account_name": "Наименование",
                               "balance": "Остаток, сум", "arcdate": "Дата остатка",
                               "accountid": "ID счёта"})
