"""
Everything between the database and the page: save, read, clean, count.

THE ROAD OF THE DATA
1. save_today()     Oracle (the state right now) → datasets/collateral/collateral_<today>.parquet.
                     Runs only when someone presses «Обновить из базы». A second run on
                     the same day overwrites that day's file. The file keeps raw text.
2. read_day(day)     parquet → prepare() → a clean pandas table, kept in memory,
                     so clicking around the page does not read the file again.
                     The page opens the newest file (latest_day) unless a date is clicked.
3. prepare(table)    numbers become numbers, dates become dates, spelling variants of
                     the same brand are merged, and the extra columns the page groups by
                     are added (brand, age_group, area_group, dep_term ...).
4. build_page(...)   the filtered table → KPIs, cards, the list of deals.

THE TABLE (one row = one collateral deal)
    kind       car / property / other
    subkind    for «other»: equipment, deposit, insurance ... (see queries.OTHERS)
    dealid, mfo, tobo, parent_id, currency, amount, market, subtype, note
    + one column per parameter (names from the dicts in queries.py)
    + the extra columns made by prepare()

All the settings you may want to change are in the block just below.
"""
import numbers
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
         "sec_issue", "sec_pay_date", "goods_list_date", "goods_act_date", "policy_date"]

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


def names(groups):
    """[(4, 'до 3 лет'), (8, '4–7 лет')] → ['до 3 лет', '4–7 лет']"""
    return [name for limit, name in groups]


# The order of the rows in the cards sorted by "label": buckets go small → big, not A → Z.
ORDER = {
    "age_group": names(AGE_GROUPS), "area_group": names(AREA_GROUPS),
    "size_group": names(SIZE_GROUPS), "dep_term": names(TERM_GROUPS),
    "sec_term": names(TERM_GROUPS), "pasp_state": names(PASP_GROUPS),
    "built_decade": ["до 1960"],
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
}


# ═══════════════════════════════ 1. SAVE ═══════════════════════════════════════════

def file_for(day):
    """datasets/collateral/collateral_2026-10-01.parquet"""
    return DATA_DIR / f"collateral_{day.isoformat()}.parquet"


def saved_days():
    """Dates that already have a file, newest first: [{'day': date, 'size': '12.3 МБ'}]."""
    days = []
    for path in sorted(DATA_DIR.glob("collateral_*.parquet"), reverse=True):
        try:
            day = date.fromisoformat(path.stem.replace("collateral_", ""))
        except ValueError:
            continue
        days.append({"day": day, "size": f"{path.stat().st_size / 1e6:.1f} МБ"})
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


def save_today():
    """Ask Oracle for the three kinds (state right now) and save them as ONE file, today's date."""
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
    # write to a temporary file first, then swap: nobody ever reads a half-written file
    temporary = DATA_DIR / "collateral_writing.tmp"
    table.to_parquet(temporary, index=False)
    temporary.replace(file_for(day))
    return day


# ═══════════════════════════════ 2. READ ═══════════════════════════════════════════

# The last table read, so clicking around the page does not read the file every time.
# It is read again when the file changes (a new download from Oracle).
MEMORY = {"key": None, "table": None}


def read_day(day):
    """The clean table of the file saved on `day` (the file must exist)."""
    path = file_for(day)
    key = (str(path), path.stat().st_mtime)
    if MEMORY["key"] != key:
        MEMORY["table"] = prepare(pd.read_parquet(path), day)
        MEMORY["key"] = key
    return MEMORY["table"]


# ═══════════════════════════════ 3. PREPARE ════════════════════════════════════════

def to_number(column):
    """'1 234,56' / '1234.56' / 1234.56 → 1234.56 ; anything else → empty."""
    text = column.astype("string").str.replace(r"[\s ]", "", regex=True)
    text = text.str.replace(",", ".", regex=False)
    return pd.to_numeric(text, errors="coerce")


def to_date(column):
    """Text in any of DATE_FORMATS → a date; anything else → empty."""
    text = column.astype("string").str.strip()
    result = pd.Series(pd.NaT, index=column.index, dtype="datetime64[ns]")
    for fmt in DATE_FORMATS:
        missing = result.isna() & text.notna()
        if not missing.any():
            break
        result[missing] = pd.to_datetime(text[missing], format=fmt, errors="coerce")
    return result


def to_year(column, day):
    """'2019' / '2019.0' / '01.01.2019' → 2019 ; a year outside 1900 … next year → empty."""
    years = to_number(column)
    from_dates = to_date(column).dt.year
    years = years.fillna(from_dates)
    return years.where((years >= 1900) & (years <= day.year + 1))


def same_spelling(column):
    """
    'CHEVROLET', 'Chevrolet ', 'chevrolet' are one brand: all three get the spelling
    used most often. Empty → EMPTY, so the cards have a «не указано» row.
    """
    text = as_text(column)
    key = text.str.upper()
    pairs = pd.DataFrame({"key": key, "text": text}).dropna()
    counts = pairs.groupby(["key", "text"]).size().reset_index(name="n")
    best = counts.sort_values("n", ascending=False).drop_duplicates("key")
    return key.map(best.set_index("key")["text"]).fillna(EMPTY)


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
    return years.map(lambda y: EMPTY if pd.isna(y) else str(int(y)))


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


def prepare(table, day):
    """The raw text from the file → a table ready for counting. Read top to bottom."""
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

    # the group of «others»: the first group in queries.OTHERS that has a filled parameter
    table["subkind"] = pd.Series(pd.NA, index=table.index, dtype="object")
    for name, params in queries.OTHERS.items():
        columns = [column for column, label in params.values() if column in table]
        if columns:
            has_any = table[columns].notna().any(axis=1)
            table["subkind"] = table["subkind"].mask(table["subkind"].isna() & has_any, name)
    table["subkind"] = table["subkind"].map(lambda s: SUBKINDS[s]["label"] if s in SUBKINDS else None)
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
        table["rooms_group"] = table["rooms"].map(
            lambda r: EMPTY if pd.isna(r) or r <= 0 else ("5 и больше" if r >= 5 else str(int(r))))
    if "built_year" in table:
        table["built_decade"] = table["built_year"].map(
            lambda y: EMPTY if pd.isna(y) else ("до 1960" if y < 1960 else f"{int(y) // 10 * 10}-е"))
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
    table["currency_name"] = table["currency"].map(lambda c: codes.get(c, c) if pd.notna(c) else EMPTY)
    for column, names in CODES.items():
        if column != "currency" and column in table:
            table[column] = table[column].map(lambda c: names.get(c, c) if pd.notna(c) else c)

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
    table["kind_name"] = table["kind"].map(lambda k: KINDS[k]["label"])

    # the checks («Проверка данных»): one True/False column per check
    for code, (label, rows) in find_problems(table, day).items():
        table["problem_" + code] = rows.fillna(False).astype(bool)
    return table


def find_problems(t, day):
    """
    The data checks: code → (what is wrong, which rows). Add your own here — it appears
    on the page and becomes a filter by itself.
    """
    today = pd.Timestamp(day)
    car, prop, other = t["kind"] == "car", t["kind"] == "property", t["kind"] == "other"

    def has(column):
        """True where the column is filled (and False everywhere if it does not exist)."""
        if column not in t:
            return pd.Series(False, index=t.index)
        return t[column].notna() & (t[column] != EMPTY)

    def before_day(column):
        """True where the date in the column is already in the past."""
        if column not in t:
            return pd.Series(False, index=t.index)
        return t[column] < today

    return {
        "no_market":    ("Нет рыночной стоимости", t["market"].isna() | (t["market"] <= 0)),
        "over_market":  ("Сумма залога больше рыночной стоимости", t["amount"] > t["market"]),
        "no_parent":    ("Не привязан к анкете / РНК", t["parent_id"].isna()),
        "car_no_plate": ("Авто без госномера", car & ~has("plate")),
        "car_no_year":  ("Авто без года выпуска", car & ~has("made_year")),
        "car_pasp_old": ("Техпаспорт просрочен", car & before_day("pasp_end")),
        "prop_no_cad":  ("Недвижимость без кадастрового номера", prop & ~has("cadastre_no")),
        "prop_no_area": ("Недвижимость без площади", prop & ~(t.get("total_area", pd.Series(0, index=t.index)) > 0)),
        "dep_expired":  ("Депозит в залоге уже истёк", other & before_day("dep_end")),
        "sec_expired":  ("Ценная бумага уже погашена", other & before_day("sec_pay_date")),
    }


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
    groups = part.groupby(column).agg(count=("dealid", "size"), amount=("amount", "sum"))
    groups = groups.reset_index()
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
    tiles = []
    for key, info in KINDS.items():
        rows = part[part["kind"] == key]
        tiles.append({"key": key, "label": info["label"], "icon": info["icon"],
                      "count": number(len(rows)), "amount": mln(rows["amount"].sum()),
                      "market": mln(rows["market"].sum()),
                      "share": number(percent(rows["amount"].sum(), total), 1),
                      "width": percent(rows["amount"].sum(), total)})
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
    ]
    if kind == "car" and "made_year" in part:
        years = pd.to_numeric(part["made_year"], errors="coerce")
        ages = day.year - years
        old = (ages > 10).sum()
        out.append({"label": "Средний возраст", "value": number(ages.mean(), 1) + " г.",
                    "icon": "fa-hourglass-half", "note": f"старше 10 лет: {number(old)}"})
        if "mileage" in part:
            out.append({"label": "Средний пробег", "value": number(part["mileage"].mean()),
                        "icon": "fa-road", "note": "км"})
        bad = int(part["problem_car_pasp_old"].sum())
        out.append({"label": "Техпаспорт просрочен", "value": number(bad), "icon": "fa-id-card",
                    "note": "на дату файла", "bad": bad > 0})
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
            soon = part["dep_term"].isin(["истёк", "до 30 дней"]).sum()
            out.append({"label": "Депозиты: истекают", "value": number(soon), "icon": "fa-piggy-bank",
                        "note": "истёк или до 30 дней", "bad": soon > 0})
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
    empty = pd.DataFrame({"kind": [], "market": [], "amount": [], "parent_id": []})
    return {code: label for code, (label, rows) in find_problems(empty, date.today()).items()}


def deal_list(part, kind, page):
    """One page of the deals list, biggest first."""
    columns = [(c, h) for c, h in LIST_COLUMNS.get(kind or "all", []) if c in part]
    part = part.sort_values("amount", ascending=False)
    pages = max(1, -(-len(part) // PAGE_SIZE))          # rounded up
    page = min(max(1, page), pages)
    rows = []
    for _, r in part.iloc[(page - 1) * PAGE_SIZE: page * PAGE_SIZE].iterrows():
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
                     "warn": bool(pd.notna(r["market"]) and r["amount"] > r["market"])})
    return {"headers": [h for c, h in columns], "rows": rows, "page": page, "pages": pages,
            "total": number(len(part))}


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


def deal_card(table, dealid):
    """All filled fields of one deal, in sections: [{'title', 'rows': [(label, value)]}]."""
    rows = table[table["dealid"] == dealid]
    if rows.empty:
        return None
    r = rows.iloc[0]
    names = labels()
    main = ["kind_name", "subkind", "dealid", "mfo", "tobo", "parent_id", "currency_name",
            "amount", "market", "subtype", "source", "note"]
    names["kind_name"] = "Вид обеспечения"
    sections = [{"title": "Основное", "icon": "fa-circle-info",
                 "rows": [(names.get(c, c), show(r.get(c))) for c in main if show(r.get(c))]}]
    params = {"car": queries.CARS, "property": queries.PROPERTY}.get(r["kind"], queries.others_flat())
    filled = [(label, show(r.get(column))) for column, label in params.values() if show(r.get(column))]
    sections.append({"title": "Параметры", "icon": "fa-list", "rows": filled})
    issues = [label for code, label in find_problems_labels().items() if r.get("problem_" + code)]
    return {"dealid": dealid, "kind": KINDS[r["kind"]], "title": show(r.get("title")),
            "amount": number(r["amount"]), "market": number(r["market"]),
            "sections": sections, "issues": issues}


def excel_table(table, filters):
    """The filtered rows with Russian headers, only the columns that have something in them."""
    part = apply_filters(table, filters).sort_values("amount", ascending=False)
    names = labels()
    skip = {"title", "kind_name"} | {c for c in part.columns if c.startswith("problem_")}
    columns = [c for c in part.columns if c not in skip and part[c].notna().any()
               and not (part[c] == EMPTY).all()]
    out = part[columns].copy()
    for c in columns:
        if pd.api.types.is_datetime64_any_dtype(out[c]):
            out[c] = out[c].dt.date
        elif out[c].dtype == object or str(out[c].dtype) == "string":
            out[c] = out[c].replace(EMPTY, None)
    out["kind"] = out["kind"].map(lambda k: KINDS[k]["label"])
    return out.rename(columns=names)
