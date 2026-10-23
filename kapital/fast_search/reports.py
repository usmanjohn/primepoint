"""
FAST SEARCH — a folder of .sql files is the whole app. Nothing is saved: the query runs,
the page shows the result, the Excel button downloads it.

TO ADD A REPORT: put one file in fast_search/sql/, for example client_deals.sql:

    -- Сделки клиента
    -- Все сделки контрагента на дату архива.
    select d.id         as "ID сделки",
           d.amounteq   as "Сумма"
    from   schema2.deal d
    where  d.contragentid = :contragentid
      and  trunc(d.arcdate) = :arcdate

That is all. Open /fast-search/ and it is there.
  - the FIRST comment line is the title, the next comment lines are the description;
  - the file name (client_deals) is the address: /fast-search/client_deals/;
  - the form is made from the parameters in the SQL (:contragentid, :arcdate). A parameter
    that is not in the SQL is not in the form, so there is nothing to switch on or off;
  - column names: write them in Russian with double quotes (as "Сумма") and the page and
    Excel show them like that.

AN OPTIONAL PARAMETER (empty field = everything) is written like this:

      and  (:siteid is null or d.siteid = :siteid)

EXTRA PYTHON (optional): a function in process.py with the SAME NAME as the file gets the
table and the form values and returns the table to show. See process.py.
"""
import re
import time
from datetime import date
from pathlib import Path

import pandas as pd

from main.oracle import get_oracle_connection

from . import process

SQL_DIR = Path(__file__).resolve().parent / "sql"

# The parameters you use often: name in the SQL → (label on the form, type).
# type "date" = a calendar field; "text" = a text field (ids, codes ...).
# A parameter that is not here still works: a text field (or a date if its name ends in "date").
FIELDS = {
    "pdate":        ("Дата", "date"),
    "arcdate":      ("Дата архива", "date"),
    "startdate":    ("Дата с", "date"),
    "enddate":      ("Дата по", "date"),
    "contragentid": ("ID контрагента", "text"),
    "dealid":       ("ID сделки", "text"),
    "siteid":       ("МФО (siteid)", "text"),
}

SHOW_ROWS = 500          # rows shown on the page; Excel always gets them all
EXCEL_MAX_ROWS = 1_000_000   # Excel holds 1 048 576 rows: a bigger result is given as CSV


# ═══════════════════════════════ THE REPORTS ═══════════════════════════════════════

def all_reports():
    """Every .sql file in the folder, sorted by title."""
    reports = [read_report(path.stem) for path in SQL_DIR.glob("*.sql")]
    return sorted(reports, key=lambda r: r["title"].lower())


def read_report(name):
    """One report by its file name, or None if there is no such file."""
    path = SQL_DIR / f"{name}.sql"
    if not name.replace("_", "").replace("-", "").isalnum() or not path.exists():
        return None
    text = path.read_text(encoding="utf-8")

    comments = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("--"):
            comments.append(line[2:].strip())
        elif line:
            break

    params = find_params(text)
    return {
        "name": name,
        "title": comments[0] if comments else name,
        "description": " ".join(comments[1:]),
        "sql": text.strip().rstrip(";"),       # SQL Developer's «;» at the end breaks oracledb
        "params": params,
        "fields": [field(p) for p in params],
    }


def find_params(sql):
    """The :names in the SQL, in the order of FIELDS first, then as they come.
    Comments and 'text in quotes' are skipped, so to_char(x, 'HH24:MI') is not a parameter."""
    clean = re.sub(r"/\*.*?\*/", " ", sql, flags=re.S)
    clean = re.sub(r"--[^\n]*", " ", clean)
    clean = re.sub(r"'[^']*'", " ", clean)
    found = []
    for name in re.findall(r"(?<![:\w]):([A-Za-z_]\w*)", clean):
        if name.lower() not in found:
            found.append(name.lower())
    known = [p for p in FIELDS if p in found]
    return known + [p for p in found if p not in known]


def field(name):
    """The form field of one parameter: name, label, type."""
    label, kind = FIELDS.get(name, (name, "date" if name.endswith("date") else "text"))
    return {"name": name, "label": label, "type": kind}


def read_values(report, data):
    """The form values (request.GET) → {param: value} for Oracle, and a list of errors.
    An empty field is None (NULL in the SQL)."""
    values, errors = {}, []
    for f in report["fields"]:
        raw = data.get(f["name"], "").strip()
        if not raw:
            values[f["name"]] = None
        elif f["type"] == "date":
            try:
                values[f["name"]] = date.fromisoformat(raw)
            except ValueError:
                errors.append(f"«{f['label']}»: не дата ({raw})")
        else:
            values[f["name"]] = raw
    return values, errors


# ═══════════════════════════════ RUN ═══════════════════════════════════════════════

# The last result, so the Excel button does not run the same query again.
# Each gunicorn worker keeps its own one (in memory only, never on disk).
MEMORY = {"key": None, "table": None, "seconds": None}


def get_table(report, values):
    """The result of the report for these values: from MEMORY if it was just run, else from Oracle."""
    key = (report["name"], report["sql"], tuple(sorted((k, str(v)) for k, v in values.items())))
    if MEMORY["key"] != key:
        started = time.time()
        table = run(report["sql"], values)
        extra = getattr(process, report["name"], None)
        if extra is not None:
            table = extra(table, values)
        MEMORY.update(key=key, table=table, seconds=time.time() - started)
    return MEMORY["table"], MEMORY["seconds"]


def run(sql, values):
    """Run one query and return it as a pandas table."""
    with get_oracle_connection() as conn:
        cursor = conn.cursor()
        cursor.arraysize = 5000                 # fetch in big packs: much faster on big results
        cursor.execute(sql, values)
        # Oracle gives unquoted names in CAPITALS: make them small. "Сумма" in quotes stays.
        columns = [c[0].lower() if c[0].isascii() and c[0].isupper() else c[0] for c in cursor.description]
        return pd.DataFrame(cursor.fetchall(), columns=columns)


# ═══════════════════════════════ SHOW ══════════════════════════════════════════════

def show(value):
    """One cell for the page: 1 234 567,89 · 31.12.2025 · empty for NULL."""
    if value is None or (not isinstance(value, str) and pd.isna(value)):
        return ""
    if isinstance(value, bool):
        return "да" if value else "нет"
    if isinstance(value, (int, float)) or hasattr(value, "as_integer_ratio"):
        if float(value).is_integer() and abs(value) < 1e15:
            return f"{int(value):,}".replace(",", " ")
        return f"{value:,.2f}".replace(",", " ").replace(".", ",")
    if hasattr(value, "strftime"):
        if getattr(value, "hour", 0) or getattr(value, "minute", 0):
            return value.strftime("%d.%m.%Y %H:%M")
        return value.strftime("%d.%m.%Y")
    return str(value)


def preview(table):
    """The first SHOW_ROWS rows, ready for the template; numbers are right-aligned."""
    head = table.head(SHOW_ROWS)
    numeric = [pd.api.types.is_numeric_dtype(table[c]) and not pd.api.types.is_bool_dtype(table[c])
               for c in table.columns]
    return {
        "columns": [{"name": str(c), "num": n} for c, n in zip(table.columns, numeric)],
        "rows": [[{"v": show(v), "num": n} for v, n in zip(row, numeric)]
                 for row in head.itertuples(index=False)],
        "total": len(table),
        "cut": len(table) > SHOW_ROWS,
    }
