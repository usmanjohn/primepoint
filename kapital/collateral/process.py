"""
Everything between the database and the page: save, read, clean, count.

THE ROAD OF THE DATA
1. save_today()     Oracle (the state right now) → prepare() → to_summary() →
                     datasets/collateral/collateral_<today>.parquet (the SUMMARY only).
                     Runs only when someone presses «Обновить из базы». A second run on
                     the same day overwrites that day's file.
   save_accounts()   the same moment: the 945xx accounts → accounts_<today>.parquet.
2. read_day(day)     the summary parquet, kept in memory (it is small), so clicking around the
                     page does not read the file again. The page opens the newest file
                     (latest_day) unless a date is clicked.
3. prepare(table)    numbers become numbers, dates become dates, spelling variants of
                     the same brand are merged, and the extra columns the page groups by
                     are added (brand, age_group, area_group, dep_term ...).
4. build_page(...)   the filtered table → KPIs and cards (summaries only: no list of deals).
5. accounts_page()   collateral against the 945xx accounts (the «Счета 945xx» page).
   delete_day(day)   «Удалить выбранные»: every file of an old day.

THE DEALS TABLE (only in memory, only during «Обновить»: one row = one collateral deal)
    kind       car / property / other
    subkind    for «other»: equipment, deposit, insurance ... (see queries.OTHERS)
    dealid, mfo, tobo, parent_id, currency, amount, market, subtype
    + one column per parameter (names from the dicts in queries.py)
    + the extra columns made by prepare()
    In memory only SUMMARY_COLUMNS + the cards' columns stay (see «SUMMARY ONLY» above).

SUMMARY ONLY, ACTIVE ONLY (2026-11-10). The server ran out of memory (ОЗУ): every gunicorn
worker kept its own copy of a table with every field of every deal, closed ones too. Now
    * Oracle returns active collateral only (queries.NOT_CLOSED), and prepare() drops any
      closed row an older file still has;
    * NOTHING per deal is saved or kept. «Обновить из базы» cleans the deals in memory once,
      counts the checks, and then to_summary() folds them into a SUMMARY: one row per
      combination of the cards' values (brand, year, МФО, size ... and the checks), with
      `n` = how many deals and the sums (amount, market ...). Only that is written to disk
      and read by the pages. No deal ids, анкета fields, VINs or free text anywhere.
      Every count on the page is a sum of `n`, never a number of rows.
    * A file saved before this change (one row per deal) is folded into a summary the
      first time it is opened, and the detailed file is overwritten.
    * Changed a card, a bucket or a check? Press «Обновить из базы»: a saved summary
      cannot be cleaned again, there are no deals left in it.

All the settings you may want to change are in the block just below.
"""
import io
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

# The columns kept after prepare(): the cards' columns (all_cards), the problem_* checks
# and these. Everything else (ids, анкета fields) is dropped.
SUMMARY_COLUMNS = ["kind", "subkind", "status", "amount", "market", "mileage", "total_area",
                   "cadastre_value", "jewel_weight", "harvest_crop_area",
                   "acc_count", "acc_balance", "acc_diff", "acc_right", "acc_shared"]

# What the summary SUMS for each combination of values (see to_summary). n = deals.
MEASURES = ["n", "amount", "market", "mileage", "mileage_n", "total_area", "area_m2", "market_m2",
            "cadastre_value", "jewel_weight", "harvest_crop_area", "acc_count", "acc_balance"]

# Excel files are slow to write (about 50 000 cells a second), CSV is about 10× faster.
# Cells = rows × columns of the download:
#   up to EXCEL_MAX_CELLS  → .xlsx   (≈ 10 seconds at most)
#   up to CSV_MAX_CELLS    → .csv    (opens in Excel too; ≈ 15 seconds at most)
#   more                   → no file: the page asks to narrow the view (Excel cannot open
#                            a million rows anyway). Gunicorn stops a request after 30 s.
EXCEL_MAX_CELLS = 600_000
CSV_MAX_CELLS = 15_000_000


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

# ═══════════════════════════════ 1. SAVE ═══════════════════════════════════════════
# Each «Обновить из базы» writes, for its day:
#     collateral_<day>.parquet        the SUMMARY (to_summary): counts and sums, no deals
#     accounts_<day>.parquet          the 945xx accounts, only if queries.CHECK_ACCOUNTS
#                                     (or accounts_<day>.error.txt if that query failed)
# (collateral_<day>.ready.parquet was a cleaned per-deal copy before 2026-11-10: it is
#  deleted when its day is opened or deleted.)

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
    if queries.CHECK_ACCOUNTS:
        save_accounts(day)
    else:                  # switched off: no 945xx file for this day, the pages work without it
        accounts_file(day).unlink(missing_ok=True)
        accounts_error_file(day).unlink(missing_ok=True)
    # the deals live only here, in this one request: cleaned, counted, folded, forgotten
    summary = to_summary(prepare(table, day, read_accounts(day)))
    del table
    write(summary, file_for(day))
    ready_file(day).unlink(missing_ok=True)
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

def read_day(day):
    """The summary of the file saved on `day` (the file must exist)."""
    path = file_for(day)
    if not is_summary(path):           # saved before 2026-11-10: one row per deal
        fold_old_file(day)
    key = (str(path), path.stat().st_mtime)
    if MEMORY["key"] != key:
        MEMORY["accounts"] = read_accounts(day)
        MEMORY["table"] = pd.read_parquet(path)
        MEMORY["key"] = key
    return MEMORY["table"]


def is_summary(path):
    """True if the file is a summary (it has the `n` column), False if it is one row per deal."""
    import pyarrow.parquet
    return "n" in pyarrow.parquet.read_schema(path).names


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


def read_raw(path):
    """
    An old per-deal file (saved before 2026-11-10), only the columns queries.py still asks
    for: the анкета fields (VIN, engine number ...) in it are not even read.
    """
    import pyarrow.parquet
    wanted = {"dealid", "kind", "mfo", "tobo", "parent_id", "currency", "amount", "market",
              "subtype", "closedate"}
    for params in [queries.CARS, queries.PROPERTY, queries.others_flat(), queries.COMMON]:
        wanted |= {column for column, label in params.values()}
    present = pyarrow.parquet.read_schema(path).names
    return pd.read_parquet(path, columns=[c for c in present if c in wanted])


def fold_old_file(day):
    """An old per-deal file → its summary, written over it (the deals are gone from disk)."""
    summary = to_summary(prepare(read_raw(file_for(day)), day, read_accounts(day)))
    write(summary, file_for(day))
    ready_file(day).unlink(missing_ok=True)


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
    table = table[table["status"] == ACTIVE].copy()      # active only (older files have closed rows)

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

    # the 945xx accounts: balance, account number, is it the right account
    if accounts is not None:
        table = add_accounts(table, accounts)

    # the checks («Проверка данных»): one True/False column per check
    for code, (label, rows) in find_problems(table, day).items():
        table["problem_" + code] = rows.fillna(False).astype(bool)

    # summaries only: drop every column the cards and KPIs do not use (see SUMMARY_COLUMNS)
    keep = set(SUMMARY_COLUMNS) | {column for column, title, icon, order in all_cards()}
    table = table[[c for c in table.columns if c in keep or c.startswith("problem_")]]
    table = table.reset_index(drop=True)

    # Text columns → «category»: each different value is kept once and the rows only point
    # to it. A million rows of brands, colours, branches take ~15 times less memory
    # (every gunicorn worker keeps its own copy!) and grouping them is faster.
    for column in table.columns:
        if table[column].dtype == object or pd.api.types.is_string_dtype(table[column]):
            table[column] = table[column].astype("category")
    return table


def to_summary(t):
    """
    The cleaned deals → the SUMMARY that is saved: one row per combination of the cards'
    values and the checks, with n (how many deals) and the sums of MEASURES. A card is
    then a sum over these rows, exactly as it was a count over the deals.
    """
    t = t.copy()
    t["n"] = 1
    if "mileage" in t:
        t["mileage_n"] = t["mileage"].notna().astype(int)        # for the average mileage
    if "total_area" in t:                                         # for the price of 1 m²
        both = (t["total_area"] > 0) & (t["market"] > 0)
        t["area_m2"] = t["total_area"].where(both, 0.0)
        t["market_m2"] = t["market"].where(both, 0.0)
    dims = []
    for column in ["kind", "subkind"] + [c for c, title, icon, order in all_cards()] \
            + [c for c in t.columns if c.startswith("problem_")]:
        if column in t and column not in dims:
            dims.append(column)
    for column in dims:
        if not pd.api.types.is_bool_dtype(t[column]):
            t[column] = t[column].astype("object").fillna(EMPTY)
    measures = [m for m in MEASURES if m in t]
    out = t.groupby(dims, sort=False, dropna=False)[measures].sum().reset_index()
    out["n"] = out["n"].astype("int64")
    for column in dims:              # text (object, or «str» in pandas 3) → category: each value once
        if not pd.api.types.is_bool_dtype(out[column]) and not pd.api.types.is_numeric_dtype(out[column]):
            out[column] = out[column].astype("category")
    return out


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
    groups = part.groupby(column, observed=True).agg(count=("n", "sum"), amount=("amount", "sum"))
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
    sums = part.groupby("kind", observed=True).agg(count=("n", "sum"), amount=("amount", "sum"),
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
                          "count": number(rows["n"].sum()), "amount": mln(rows["amount"].sum())})
    return tiles


def kpis(part, kind, day):
    """The numbers at the top: [{'label', 'value', 'note', 'icon', 'bad'}]. Counts = sums of n."""
    deals = part["n"].sum()
    amount, market = part["amount"].sum(), part["market"].sum()

    def deals_where(rows):
        return part.loc[rows, "n"].sum()

    out = [
        {"label": "Сделок обеспечения", "value": number(deals), "icon": "fa-file-signature",
         "note": "действующих"},
        {"label": "Сумма залога", "value": mln(amount), "icon": "fa-scale-balanced",
         "note": "млн сум, эквивалент"},
        {"label": "Рыночная стоимость", "value": mln(market), "icon": "fa-tags",
         "note": "млн сум"},
        {"label": "Залог / рынок", "value": number(percent(amount, market), 1) + " %",
         "icon": "fa-percent", "note": "сколько от рыночной цены принято в залог"},
        {"label": "Средний залог", "value": mln(amount / deals) if deals else "—",
         "icon": "fa-equals", "note": "млн сум на сделку"},
    ]
    if "acc_balance" in part:
        gap = part["acc_balance"].sum() - amount
        out.append({"label": "На счетах 945xx", "value": mln(part["acc_balance"].sum()),
                    "icon": "fa-book", "note": f"у действующих; разница {mln(gap)} млн",
                    "bad": abs(gap) >= TOLERANCE})
    if kind == "car" and "made_year" in part:
        years = pd.to_numeric(part["made_year"].astype("object"), errors="coerce")
        ages = day.year - years
        known = part["n"][ages.notna()].sum()
        average = (ages * part["n"]).sum() / known if known else None
        out.append({"label": "Средний возраст", "value": number(average, 1) + " г.",
                    "icon": "fa-hourglass-half", "note": f"старше 10 лет: {number(deals_where(ages > 10))}"})
        if "mileage" in part:
            known = part["mileage_n"].sum()
            out.append({"label": "Средний пробег", "value": number(part["mileage"].sum() / known if known else None),
                        "icon": "fa-road", "note": "км"})
        bad = int(deals_where(part["problem_car_pasp_old"]))
        out.append({"label": "Техпаспорт просрочен", "value": number(bad), "icon": "fa-id-card",
                    "note": "у действующих залогов", "bad": bad > 0})
    if kind == "property" and "total_area" in part:
        per_m2 = part["market_m2"].sum() / part["area_m2"].sum() if part["area_m2"].sum() else None
        out.append({"label": "Общая площадь", "value": number(part["total_area"].sum()), "icon": "fa-ruler-combined",
                    "note": "м²"})
        out.append({"label": "Цена за м²", "value": number(per_m2), "icon": "fa-house",
                    "note": "сум, рыночная стоимость / площадь"})
        if "cadastre_value" in part:
            out.append({"label": "Кадастровая стоимость", "value": mln(part["cadastre_value"].sum()),
                        "icon": "fa-landmark", "note": "млн сум"})
    if kind == "other":
        if "dep_term" in part:
            soon = int(deals_where(part["dep_term"].isin(["истёк", "до 30 дней"])))
            out.append({"label": "Депозиты: истекают", "value": number(soon), "icon": "fa-piggy-bank",
                        "note": "истёк или до 30 дней, у действующих", "bad": soon > 0})
        if "jewel_weight" in part and part["jewel_weight"].sum():
            out.append({"label": "Вес ювелирных изделий", "value": number(part["jewel_weight"].sum(), 1),
                        "icon": "fa-gem", "note": "сумма по полю «Вес»"})
        if "harvest_crop_area" in part and part["harvest_crop_area"].sum():
            out.append({"label": "Посевная площадь", "value": number(part["harvest_crop_area"].sum(), 1),
                        "icon": "fa-wheat-awn", "note": "га, будущий урожай"})
    return out


def problems(part):
    """The «Проверка данных» list for the rows on the page."""
    out = []
    labels = find_problems_labels()
    for code, label in labels.items():
        n = int(part.loc[part["problem_" + code], "n"].sum()) if "problem_" + code in part else 0
        if n:
            out.append({"code": code, "label": label, "count": number(n),
                        "share": number(percent(n, part["n"].sum()), 1)})
    return out


def find_problems_labels():
    """code → label of every check, without computing them (an empty table is enough)."""
    empty = pd.DataFrame({"kind": [], "market": [], "amount": [], "parent_id": [], "status": []})
    return {code: label for code, (label, rows) in find_problems(empty, date.today()).items()}


def build_page(table, day, filters):
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


# ═══════════════════════════════ 5. EXCEL (THE SUMMARY) ═══════════════════════════

def show(value):
    """One value as text (the 945xx accounts page)."""
    if value is None or (not isinstance(value, str) and pd.isna(value)):
        return None
    if isinstance(value, pd.Timestamp):
        return value.strftime("%d.%m.%Y")
    if isinstance(value, numbers.Number):
        return number(value, 2 if value % 1 else 0)
    if value == EMPTY:
        return None
    return str(value)


def summary_excel(table, filters):
    """
    The current view as a summary for Excel: one block per card of the page (every row,
    not only the top 12), plus «Итого» first. Never a row per deal.
    """
    part = apply_filters(table, filters)
    total = part["amount"].sum()
    rows = [{"Разрез": "Итого", "Значение": "", "Сделок": int(part["n"].sum()), "Сумма залога, сум": total,
             "Рыночная стоимость, сум": part["market"].sum(), "Доля суммы, %": 100.0 if len(part) else 0}]
    breakdowns = [("kind_name", "Вид обеспечения")] if not dict(filters).get("kind") else []
    breakdowns += [(column, title) for column, title, icon, order in cards_for(filters) if column in part]
    for column, title in breakdowns:
        if column == "kind_name":
            groups = part.groupby("kind", observed=True)
        else:
            groups = part.groupby(column, observed=True)
        sums = groups.agg(count=("n", "sum"), amount=("amount", "sum"), market=("market", "sum"))
        for value, g in sums.sort_values("amount", ascending=False).iterrows():
            if column == "kind_name":
                value = KINDS[value]["label"]
            rows.append({"Разрез": title, "Значение": str(value), "Сделок": int(g["count"]),
                         "Сумма залога, сум": g["amount"], "Рыночная стоимость, сум": g["market"],
                         "Доля суммы, %": percent(g["amount"], total)})
    return pd.DataFrame(rows)


def to_xlsx(table, sheet):
    """The table as .xlsx bytes. openpyxl's write-only mode: about 3× faster than table.to_excel."""
    import openpyxl
    book = openpyxl.Workbook(write_only=True)
    page = book.create_sheet(sheet[:31])
    page.append([str(c) for c in table.columns])
    for row in table.astype(object).where(table.notna(), None).itertuples(index=False):
        page.append(list(row))
    buffer = io.BytesIO()
    book.save(buffer)
    return buffer.getvalue()


def to_csv(table):
    """The table as CSV text that Excel opens right: «;» between columns, BOM for the Russian letters."""
    return "\ufeff" + table.to_csv(index=False, sep=";", decimal=",")


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
    active = table                       # the summary holds active collateral only
    ours = accounts[accounts["code"].isin(list(queries.ACCOUNT_CODES))]
    # every account once (an account linked to two deals is in `accounts` twice)
    once = ours.drop_duplicates("accountid")
    lost = orphans(accounts)
    gap = once["balance"].sum() - active["amount"].sum()

    kpis = [
        {"label": "Залог, действующий", "value": mln(active["amount"].sum()), "icon": "fa-scale-balanced",
         "note": f"млн сум · {number(active['n'].sum())} сделок"},
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
            checks.append({"code": code, "label": label, "count": number(rows["n"].sum()),
                           "amount": mln(rows["amount"].sum()),
                           "balance": mln(rows["acc_balance"].sum()), "bad": rows["n"].sum() > 0})

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
