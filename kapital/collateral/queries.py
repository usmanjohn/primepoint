"""
All the SQL of the collateral app, and nothing else.

HOW IT WORKS
Your three old scripts (others / nedvijimost / avto) were three long SQLs with the same
skeleton and a different list of parameters. Here the skeleton is written ONCE
(the function make_sql) and the parameters are three Python dicts:

    CARS       → «avto»
    PROPERTY   → «nedvijimost»
    OTHERS     → «others», split into small groups (equipment, deposit, insurance ...)

Each line of a dict is:   "NAME_IN_DATABASE": ("column_name", "Название по-русски"),
To add a field: add one line. The SQL, the Excel file and the deal page pick it up.
To see which parameters exist at all, open the «Параметры» page of the app.

WHAT TO CHANGE FOR YOUR DATABASE
1. The import line of get_oracle_connection (just below).
2. The three table names (DEAL_TABLE, PARAM_TABLE, PARENT_TABLE).
3. ON_DATE, if your tables have no date_from column (see the comment there).

To run a query by hand in your SQL tool: open the «Параметры» page, it prints the
finished SQL. Replace :pdate with a date, e.g.  date '2026-10-01'.
"""
import pandas as pd

# ⚠️ Change this one line to wherever your get_oracle_connection() lives.
from main.oracle import get_oracle_connection


# ── 1. TABLES (placeholders: put your real schema.table here) ──────────────────────
DEAL_TABLE = "schema1.second_deal"              # the collateral itself: amount, currency ...
PARAM_TABLE = "schema1.second_deal_dop_param"   # extra parameters: dealid, paramname, paramvalue
PARENT_TABLE = "schema2.deal"                   # link to the анкета/РНК and ТОБО
COLLATERAL_TYPE = 357                           # dealtypeid of a collateral deal in PARENT_TABLE


# ── 2. WHICH VERSION OF A ROW COUNTS ON THE CHOSEN DATE ────────────────────────────
# Both tables keep history: a new row every time something changes, closed by date_to.
# The row that was valid on :pdate is the one with  date_from <= :pdate < date_to.
# If your tables have NO date_from column, use this line instead (it takes every version
# still open on the date, and the newest of them wins):
#     ON_DATE = "{t}.date_to > :pdate"
ON_DATE = "{t}.date_from <= :pdate and {t}.date_to > :pdate"


# ── 3. PARAMETERS ──────────────────────────────────────────────────────────────────
# "NAME_IN_DATABASE": ("column_name", "Название по-русски")
# column_name: short, latin, at most 30 characters (Oracle's limit for an alias).

CARS = {
    "TRANSPORT_TYPE":      ("transport_type", "Тип транспорта"),
    "TRANS_MAN_NEW":       ("brand_main", "Марка"),
    "TRANSP_МАРКА":        ("brand_other", "Марка (если другое)"),   # yes, МАРКА is Cyrillic in the database
    "TRANS_MOD_NEW":       ("model_main", "Модель"),
    "TRANSP_MODEL":        ("model_other", "Модель (если другое)"),
    "COMPLECT":            ("trim", "Модель и комплектация"),
    "LICENSE_PLATE":       ("plate", "Госномер"),
    "PRODUCTION_YEAR":     ("made_year", "Год производства"),
    "TRANSMISSION_TYPE":   ("gearbox", "Коробка передач"),
    "TRANSP_COLOR":        ("color", "Цвет"),
    "TYPE OF FUEL":        ("fuel", "Вид топлива"),
    "TECH_PASP_SN":        ("pasp_sn", "Серия и номер техпаспорта"),
    "TECH_PASP_D":         ("pasp_date", "Дата техпаспорта"),
    "TECH_PASP_EXP_D":     ("pasp_end", "Техпаспорт действует до"),
    "TECH_SERIAL":         ("pasp_serial", "Серия техпаспорта"),
    "TECH_NUM":            ("pasp_number", "Номер техпаспорта"),
    "TECH_ISSUE":          ("pasp_issuer", "Кто выдал техпаспорт"),
    "BODY_N":              ("body_no", "Номер кузова"),
    "ENGINE_NUMBER":       ("engine_no", "Номер двигателя"),
    "CHASSIS_N":           ("chassis_no", "Номер шасси"),
    "INVENTORY_N":         ("inventory_no", "Инвентарный номер"),
    "TRANSP_RUN":          ("mileage", "Пробег"),
    "ORIG_COUNTRY":        ("country", "Страна производителя"),
    "CAR_PURCHASE_MARKET": ("buy_market", "Рынок приобретения"),
    "CARPRICE":            ("car_price", "Стоимость по договору купли-продажи"),
    "VEHICLE_ID":          ("vehicle_id", "Уникальный код ТС"),
    "TYPEREGNEWCAR":       ("reg_type", "Вид регистрации нового авто"),
    "VEHICLE_ADD_INFO":    ("car_info", "Доп. информация о ТС"),
}

PROPERTY = {
    "ECONOM_ZONE":         ("econ_zone", "Экономическая зона"),
    "REGISTR_ORG_CADASTR": ("cadastre_org", "Регистрирующий орган кадастра"),
    "CADASTR_N":           ("cadastre_no", "Кадастровый номер"),
    "CADASTRAMOUNT":       ("cadastre_value", "Кадастровая стоимость"),
    "BUILDING_KIND":       ("building_kind", "Вид недвижимости"),
    "BUILDING_TYPE":       ("building_type", "Тип недвижимости"),
    "TO_EXPL_D":           ("in_use_date", "Дата ввода в эксплуатацию"),
    "YEAR_CONSTRUCTION":   ("built_year", "Год постройки"),
    "PROPERTY_AREA":       ("total_area", "Общая площадь, м²"),
    "LAND_AREA":           ("land_area", "Площадь участка, м²"),
    "BUILT_UP_AREA":       ("built_area", "Площадь застройки, м²"),
    "EFFECTIVE_AREA":      ("useful_area", "Полезная площадь, м²"),
    "LIVING_SPACE":        ("living_area", "Жилая площадь, м²"),
    "ROOM_CNT":            ("rooms", "Количество комнат"),
    # The address is not in your old script. Find its real name on the «Параметры» page
    # (look for ADDR / ADRES / REGION / DISTRICT), then remove the # here:
    # "ADDRESS":           ("address", "Адрес"),
}

# «Others» is many small kinds of collateral. Each group is one kind; a deal belongs to
# the FIRST group (in this order) that has at least one of its parameters filled.
OTHERS = {
    "equipment": {
        "EQUIPMENT_TYPE":         ("eq_type", "Тип оборудования"),
        "EQUIPMENT_NAME":         ("eq_name", "Наименование оборудования"),
        "EQUIP_BRAND_MODEL":      ("eq_model", "Марка / модель"),
        "EQUIP_MANUFACTURER":     ("eq_maker", "Производитель"),
        "EQUIP_ORIG_COUNTRY":     ("eq_country", "Страна производства"),
        "EQUIP_ORIG_Y":           ("eq_year", "Год производства"),
        "EQUIP_ORIG_N":           ("eq_serial", "Заводской номер"),
        "EQUIP_BEG_TO_EXPL_D":    ("eq_in_use", "Дата ввода в эксплуатацию"),
        "EQUIP_TITLE_DOC_N":      ("eq_doc_no", "Номер правоустанавливающего документа"),
        "EQUIP_TITLE_DOC_D":      ("eq_doc_date", "Дата правоустанавливающего документа"),
        "EQUIP_UQ_ACC_NUMBER":    ("eq_uid", "Уникальный учётный номер"),
        "EQUIP_ACQUISITION COST": ("eq_cost", "Стоимость приобретения"),
    },
    "deposit": {
        "DEPOSIT_TYPE_N":    ("dep_type", "Код типа депозита"),
        "DEPOSIT_NAME":      ("dep_name", "Наименование депозита"),
        "DEPOSIT_ENDDATE":   ("dep_end", "Дата истечения депозита"),
        "DEP_BANK_BRANCH_N": ("dep_branch", "Отделение, где размещён депозит"),
    },
    "securities": {
        "SEC_NAME":            ("sec_name", "Наименование ценной бумаги"),
        "SEC_TOTAL_CNT":       ("sec_count", "Количество ценных бумаг"),
        "NOMINAL_VAL_ONE_SEC": ("sec_nominal", "Номинал одной бумаги"),
        "SEC_TOTAL_AMOUNT":    ("sec_total", "Общая сумма ценных бумаг"),
        "DISCOUNT_AMOUNT":     ("sec_discount", "Сумма дисконта"),
        "SEC_ISSUE_DATE":      ("sec_issue", "Дата выпуска"),
        "SEC_PAY_DATE":        ("sec_pay_date", "Дата погашения"),
        "DEPOSITORY":          ("depository", "Депозитарий"),
        "ACC_IN_DEPOSITORY":   ("sec_account", "Счёт в депозитарии"),
    },
    "goods": {
        "PRODUCTNAME":         ("goods_name", "Наименование товара"),
        "BOOKVALUE":           ("goods_book", "Балансовая стоимость ТМЦ (валюта залога)"),
        "BOOKVALUEEQUIVALENT": ("goods_book_eq", "Балансовая стоимость ТМЦ (эквивалент)"),
        "DESCRIPDATE":         ("goods_list_date", "Дата расшифровки остатка ТМЦ"),
        "ACTDATE":             ("goods_act_date", "Дата акта согласования стоимости"),
    },
    "insurance": {
        "POLIS_NUM":  ("policy_no", "Номер страхового полиса"),
        "POLIS_DATE": ("policy_date", "Дата страхового полиса"),
    },
    "land": {
        "LAND_LEASE_CADASTR_N": ("land_cadastre_no", "Кадастровый номер (аренда земли)"),
        "LAND_LEASE_AREA":      ("land_lease_area", "Площадь (аренда земли)"),
    },
    "harvest": {
        "FUTURE_HARVEST_AREA":      ("harvest_area", "Площадь (будущий урожай)"),
        "FUTURE_HARVEST_CROP_AREA": ("harvest_crop_area", "Посевная площадь, га"),
    },
    "jewelry": {
        "JEWELRY_CNT":    ("jewel_count", "Количество изделий"),
        "JEWELRY_WEIGHT": ("jewel_weight", "Вес"),
    },
    "rights": {
        "REQUIREMENTOBJECT": ("rights_object", "Объект имущественного права"),
        "NAMEACQUIRED":      ("rights_asset", "Приобретаемое имущество"),
    },
    "guarantee": {
        "SET_GARANT_DEP_ACC": ("guarantee_on_dep", "Гарантия внесена на депозитный счёт"),
        "IS_SUP_DOCUMENTS":   ("has_documents", "Есть подтверждающие документы"),
    },
}

# Parameters every kind can have. They are fetched too, but having ONLY these
# does not make a deal a car / a property / an «other».
COMMON = {
    "PROVISION_SOURCE": ("source", "Источник приобретения обеспечения"),
}


def others_flat():
    """All the «others» groups as one dict, like CARS and PROPERTY."""
    flat = {}
    for group in OTHERS.values():
        flat.update(group)
    return flat


def all_labels():
    """column_name → Russian label, for every parameter (used by the deal page and Excel)."""
    labels = {}
    for params in [CARS, PROPERTY, others_flat(), COMMON]:
        for column, label in params.values():
            labels[column] = label
    return labels


def quoted(names):
    """['A', 'B'] → "'A', 'B'"  (for an IN list)."""
    return ", ".join("'" + name + "'" for name in names)


def make_sql(params):
    """
    The one skeleton behind all three queries. One row per collateral deal that has
    at least one of `params` filled on :pdate, with each parameter in its own column.

      deals   — the collateral row valid on the date (amount, currency, branch ...)
      params  — the parameter values valid on the date, one row per (deal, parameter)
      wide    — the same values turned into columns: one row per deal
    """
    names = list(params) + list(COMMON)
    columns = ",\n           ".join(
        f"max(case when paramname = '{name}' then paramvalue end) as {column}"
        for name, (column, label) in {**params, **COMMON}.items()
    )
    return f"""
with deals as (
    select id, siteid, currencyid, amounteq, marketamount, creditnbusupplyid, securitydescription
    from (
        select d.*,
               row_number() over (partition by d.id order by d.date_to desc) as rn
        from   {DEAL_TABLE} d
        where  {ON_DATE.format(t='d')}
    )
    where rn = 1
),
params as (
    select dealid, paramname, paramvalue
    from (
        select v.dealid, v.paramname, v.paramvalue,
               row_number() over (partition by v.dealid, v.paramname order by v.date_to desc) as rn
        from   {PARAM_TABLE} v
        where  {ON_DATE.format(t='v')}
        and    v.paramname in ({quoted(names)})
    )
    where rn = 1
),
wide as (
    select dealid,
           {columns}
    from   params
    group by dealid
    having count(case when paramname in ({quoted(params)}) then 1 end) > 0
)
select w.*,
       d.siteid                  as mfo,
       p.toboid                  as tobo,
       p.parentid                as parent_id,
       d.currencyid              as currency,
       d.amounteq / 100          as amount,
       d.marketamount / 100      as market,
       d.creditnbusupplyid       as subtype,
       d.securitydescription     as note
from   wide w
left join deals d          on d.id = w.dealid
left join {PARENT_TABLE} p on p.id = w.dealid and p.dealtypeid = {COLLATERAL_TYPE}
"""


SQL_CARS = make_sql(CARS)
SQL_PROPERTY = make_sql(PROPERTY)
SQL_OTHERS = make_sql(others_flat())

# Every parameter name that exists on the date, how many collateral deals have it and
# one example value. Shown on the «Параметры» page: that is where you find the address.
SQL_PARAM_NAMES = f"""
select v.paramname,
       count(distinct v.dealid) as deals,
       max(v.paramvalue)        as example
from   {PARAM_TABLE} v
where  {ON_DATE.format(t='v')}
and    v.dealid in (select id from {PARENT_TABLE} where dealtypeid = {COLLATERAL_TYPE})
group by v.paramname
order by deals desc
"""


def run(cursor, sql, pdate):
    """Run one query and return it as a pandas table with lower-case column names."""
    cursor.arraysize = 5000                     # fetch in big packs: much faster on 100 000+ rows
    cursor.execute(sql, {"pdate": pdate})
    columns = [c[0].lower() for c in cursor.description]
    return pd.DataFrame(cursor.fetchall(), columns=columns)


def load_day(pdate):
    """The three queries for one date: {'car': table, 'property': table, 'other': table}."""
    with get_oracle_connection() as conn:
        cursor = conn.cursor()
        return {
            "car": run(cursor, SQL_CARS, pdate),
            "property": run(cursor, SQL_PROPERTY, pdate),
            "other": run(cursor, SQL_OTHERS, pdate),
        }


def load_param_names(pdate):
    """The «Параметры» page: every parameter name on the date."""
    with get_oracle_connection() as conn:
        return run(conn.cursor(), SQL_PARAM_NAMES, pdate)
