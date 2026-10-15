"""
Analytics engine for the portfolio report — the "album" edition.

The report is a stack of A4 landscape pages, one chart per page. Every page has the
chart on the left and a panel on the right: what the chart shows, what every colour
means, and the findings read straight out of the numbers ("крупнейший департамент —
kk, 45% портфеля"). The same file prints cleanly: Ctrl+P → A4, landscape, margins
"None", background graphics on.

IMPORTANT — the one rule that matters when editing this file:

    NOTHING may execute at import time.

Django imports this module when it loads views.py, which happens on every
`runserver`, every autoreload, and every `manage.py` command. If something that loads
8M rows sits at module level, every one of those becomes a two-minute hang.
The only entry point is run().

Everything you are likely to want to change lives in the НАСТРОЙКИ block right below.
"""
from __future__ import annotations

import hashlib
import html as _html
import math
import re
import datetime as dt
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio


# ==========================================================================
# НАСТРОЙКИ — меняйте здесь
# ==========================================================================
TITLE, BANK = "Обзор кредитного портфеля", "Kapitalbank"

# Departments: the order they appear in everywhere (legends, B06), and one colour each.
# Keys are matched case-insensitively, Cyrillic к/м/р/с count as k/m/r/s.
DEPARTMENTS = ["kk", "mk", "rk", "sk"]
DEPT_COLORS = {"kk": "#1F4E79", "mk": "#2E7D7A", "rk": "#7A4E9A", "sk": "#C9971A"}
DEPT_NAMES = {}            # e.g. {"kk": "Корпоративный"}; empty = show the value from the data
EXTRA_COLORS = ["#5E5A52", "#4F7CAC", "#A88BC4", "#6FA8A3"]   # a department not listed above

# Meaning colours: the same thing is the same colour on every page.
COLORS = {
    "npl": "#B3341F",        # NPL 90+, defaults, anything bad
    "watch": "#E08A1E",      # risk zone
    "good": "#2F6B4F",       # cured, issued, coverage
    "neutral": "#8A867C",    # "others", repayments, residuals
    "light": "#D9D4C7",      # background stacks
    "ink": "#1A1A1E",        # totals, bank-wide lines
}
CURRENCY_COLORS = {"Сум": "#D6D1C4", "USD": "#5E5A52", "EUR": "#1A1A1E"}

# Delinquency: the risk zone shown on A01/A13 and the KPI, and the report's buckets.
WATCH_DPD = (61, 90)
REPORT_BUCKETS = (
    (0, 0, "CUR"), (1, 30, "B01_30"), (31, 90, "B31_90"), (91, 180, "B91_180"),
    (181, 365, "B181_365"), (366, 10**9, "B365P"),
)
BUCKET_COLORS = {"CUR": "#2F6B4F", "B01_30": "#F2C230", "B31_90": "#E08A1E",
                 "B91_180": "#C2591F", "B181_365": "#A33418", "B365P": "#6E1F0E"}
SHOW_CURRENT_BUCKET = False   # False: the "0 дней" bucket is left out of A03/B02/B07

# Top clients (A-page dynamics + B08 table).
TOP_CLIENTS = 50
TOP_CLIENTS_EXCLUDE = ["rk"]  # these departments' clients are never ranked or named
COURT_DEPARTMENT = "rk"       # B10 looks at this department only

# Branches whose name means "unknown" are left out of every branch chart.
NO_BRANCH = ["nodata", "no data", "нет данных", "", "nan", "none", "<na>"]
BRANCHES_PER_PAGE = 24        # longer branch lists continue on the next page

# Dates. The data for September is the state on 1 October, so by default every reporting
# date is labelled by its report_date month: September's portfolio shows as «окт».
# Issue months (cohorts: A07, A08, B03) are never shifted — a loan issued in September
# was issued in September. False = label by the month the data describes.
LABEL_BY_REPORT_DATE = True

TOP_PASSPORTS, TOP_PRODUCTS, TOP_OKED = 7, 15, 10
UNIT, UNIT_NAME = 1e9, "млрд сум"

# Page geometry (A4 landscape) and type sizes. Chart is CHART_W × CHART_H pixels.
CHART_W, CHART_H = 735, 600
FONT = "Segoe UI, Roboto, Arial, sans-serif"
FONT_SIZE, LABEL_SIZE = 13, 12
MAX_LABELS = 12               # value labels per line/series, so they never overlap


# ==========================================================================
# Technical constants (rarely changed)
# ==========================================================================
NPL_CATEGORIES = (3, 4, 5)
MIN_COHORT = 30
MIN_BALANCE = 0               # static section keeps only exposure > this
VINTAGE_MARKS = ((30, 3), (30, 6), (90, 9), (90, 12))

# Fine buckets, used only for migration (A09): "from 61-90 into 90+" needs them.
MIGRATION_BUCKETS = (
    (-10**9, 0, "CUR"), (1, 30, "B01_30"), (31, 60, "B31_60"), (61, 90, "B61_90"),
    (91, 180, "B91_180"), (181, 360, "B181_360"), (361, 10**9, "B360P"),
)
MIGRATION_ORDER = [b[2] for b in MIGRATION_BUCKETS] + ["EXIT"]
DEFAULT_BUCKETS = ("B91_180", "B181_360", "B360P")
BUCKET_ORDER = [b[2] for b in REPORT_BUCKETS]

MOB_BINS = [-1, 3, 6, 12, 24, 36, 10**9]
MOB_LABELS = ["0-3 мес.", "4-6 мес.", "7-12 мес.", "13-24 мес.", "25-36 мес.", "36+ мес."]
CURRENCY_NAMES = {0: "Сум", 840: "USD", 978: "EUR"}

MONTHS_RU = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
LABEL = {
    "CUR": "Без просрочки", "B01_30": "1–30 дн.", "B31_90": "31–90 дн.",
    "B91_180": "91–180 дн.", "B181_365": "181–365 дн.", "B365P": "365+ дн.",
    "non_auto": "Не авто", "pervichka": "Авто: первичка", "vtorichka": "Авто: вторичка",
    "norm": "Норма (без суда)", "neofficial": "Неофициальная (досудебная)",
    "official": "Официальная (в суде)",
}
SUD_ALIASES = {"unofficial": "neofficial", "neoficial": "neofficial", "neofficial": "neofficial",
               "official": "official", "oficial": "official", "norm": "norm", "normal": "norm"}
SUD_ORDER = ["norm", "neofficial", "official"]
SUD_COLORS = {"norm": "#D9D4C7", "neofficial": "#E08A1E", "official": "#B3341F"}

CANONICAL = [
    "contragent", "anketa", "filial", "tobo", "valuta", "dogovor_sana", "vidacha_sana",
    "department", "department_number", "passport", "contragent_name",
    "brutto_95_summa", "brutto_summa", "protsent_16309_summa", "protsent_16377_summa",
    "protsent_16379_summa", "spisat_95413_summa", "spisat_91501_summa", "reserve_summa",
    "vidacha_tekushiy_summa", "pogashen_tekushiy_summa", "maks_dni", "kategoriya_origin",
    "kategoriya_npl_90", "straxovka_summa", "straxovka_brutto_95_summa",
    "kategoriya_straxovka", "sud", "avto", "report_date", "all_time_given_amount",
]
OPTIONAL = ["oked_name"]
RENAME = {
    "vidacha_tm_summa": "vidacha_tekushiy_summa",
    "pogashen_tm_summa": "pogashen_tekushiy_summa",
    "vidacha_alltime_summa": "all_time_given_amount",
}
DATE_COLS = ("dogovor_sana", "vidacha_sana", "report_date")
AMOUNT_COLS = [c for c in CANONICAL if c.endswith("_summa") or c == "all_time_given_amount"]

PCFG = {"displaylogo": False, "responsive": False,
        "modeBarButtonsToRemove": ["select2d", "lasso2d", "autoScale2d",
                                   "hoverClosestCartesian", "hoverCompareCartesian",
                                   "toggleSpikelines", "zoomIn2d", "zoomOut2d"],
        "toImageButtonOptions": {"format": "png", "scale": 2}}

KINDS = {"СТОК": "СТОК · снимок на дату", "ПОТОК": "ПОТОК · за месяц",
         "КОГОРТЫ": "КОГОРТЫ · по месяцу выдачи", "СРЕЗ": "СРЕЗ · одна дата",
         "ТАБЛИЦА": "ТАБЛИЦА · одна дата"}

_TEMPLATE_READY = False


def _ensure_template():
    """Registering the plotly template is cheap but still deferred out of import."""
    global _TEMPLATE_READY
    if _TEMPLATE_READY:
        return
    rule = "#E4E1D8"
    pio.templates["kb"] = go.layout.Template(layout=go.Layout(
        font=dict(family=FONT, size=FONT_SIZE, color=COLORS["ink"]),
        paper_bgcolor="white", plot_bgcolor="white",
        margin=dict(l=70, r=70, t=34, b=56),
        hoverlabel=dict(bgcolor=COLORS["ink"], font_color="white", font_size=13),
        xaxis=dict(showgrid=False, linecolor=rule, ticks="outside", tickcolor=rule,
                   tickfont=dict(size=12), automargin=True),
        yaxis=dict(gridcolor=rule, zerolinecolor=rule, tickfont=dict(size=12),
                   automargin=True),
        showlegend=False, width=CHART_W, height=CHART_H,
        uniformtext=dict(minsize=9, mode="hide"),
    ))
    pio.templates.default = "kb"
    _TEMPLATE_READY = True


# ==========================================================================
# HELPERS
# ==========================================================================
def vlabel(p):
    """An issue month (cohort) — never shifted."""
    y, m = divmod(int(p), 100)
    return f"{MONTHS_RU[m - 1]} {str(y)[2:]}"


def vlabel_full(p):
    y, m = divmod(int(p), 100)
    return f"{MONTHS_RU[m - 1]} {y}"


def _shown(p):
    return shift_p(p, -1) if LABEL_BY_REPORT_DATE else int(p)


def plabel(p):
    """A reporting date: period 202609 (September's data) is shown as «окт 26»."""
    return vlabel(_shown(p))


def plabel_full(p):
    return vlabel_full(_shown(p))


def shift_p(p, k):
    """p moved k months back (k > 0) or forward (k < 0)."""
    i = (int(p) // 100) * 12 + int(p) % 100 - 1 - k
    return (i // 12) * 100 + i % 12 + 1


def lab(k):
    return LABEL.get(str(k), str(k))


def money(v):
    return np.asarray(v, dtype="float64") / UNIT


def _ok(v):
    try:
        return v is not None and np.isfinite(float(v))
    except (TypeError, ValueError):
        return False


def fnum(v, dec=1):
    return f"{float(v):,.{dec}f}".replace(",", " ") if _ok(v) else ""


def fpct(v, dec=1):
    """v is already in percent (3.2 → '3.2%')."""
    return f"{float(v):.{dec}f}%" if _ok(v) else ""


def fpp(v, dec=2):
    """Percentage-point change, signed: +0.40 п.п."""
    return f"{float(v):+.{dec}f} п.п." if _ok(v) else "н/д"


def fchg(new, old, dec=1):
    """Relative change, signed: +12.3%."""
    if not (_ok(new) and _ok(old)) or float(old) == 0:
        return "н/д"
    return f"{(float(new) / float(old) - 1) * 100:+.{dec}f}%"


def _e(s):
    return _html.escape(str(s))


def thin(values, fmt=lambda v: fnum(v, 1), max_labels=None, keep_last=True):
    """Label every k-th point (and the last) so labels never collide."""
    vals = list(values)
    return [fmt(v) if _ok(v) and i in _label_idx(len(vals), max_labels, keep_last) else ""
            for i, v in enumerate(vals)]


def _label_idx(n, max_labels=None, keep_last=True):
    """Which positions get a label: every k-th, plus the last — dropping the one before
    the last when the two would sit closer than ~half a step."""
    step = max(1, math.ceil(n / (max_labels or MAX_LABELS)))
    idx = set(range(0, n, step))
    if keep_last and n:
        prev = max(i for i in idx if i <= n - 1)
        if prev != n - 1 and (n - 1 - prev) < step * 0.6:
            idx.discard(prev)
        idx.add(n - 1)
    return idx


def famt(v):
    """Money label: no decimals from 100 up, so big totals stay short."""
    return fnum(v, 0 if _ok(v) and abs(float(v)) >= 100 else 1)


def headroom(line_max, factor=2.6):
    top = float(line_max) * factor if _ok(line_max) and line_max > 0 else 1.0
    return dict(range=[0, top])


def _safemax(s, default=1.0):
    try:
        v = float(np.nanmax(np.asarray(s, dtype="float64")))
        return v if np.isfinite(v) and v > 0 else default
    except (ValueError, TypeError):
        return default


def nan0(s):
    """Zeros → NaN, so a department that did not exist yet draws nothing, not a 0."""
    return pd.Series(s).replace(0, np.nan)


_CYR = str.maketrans("кмрсКМРС", "kmrsKMRS")


def dkey(v):
    return str(v).strip().translate(_CYR).lower()


def dname(v):
    return DEPT_NAMES.get(dkey(v), str(v))


def dcolor(v):
    k = dkey(v)
    if k in DEPT_COLORS:
        return DEPT_COLORS[k]
    return EXTRA_COLORS[sum(map(ord, k)) % len(EXTRA_COLORS)]


def dept_sorted(values):
    """Departments in the configured order; unknown ones after, alphabetically."""
    def key(v):
        k = dkey(v)
        return (DEPARTMENTS.index(k) if k in DEPARTMENTS else len(DEPARTMENTS), k)
    return sorted({str(v) for v in values if pd.notna(v)}, key=key)


def is_no_branch(v):
    return pd.isna(v) or str(v).strip().lower() in NO_BRANCH


def shades(hexc, n):
    """n tints of one colour, darkest first — products of one department share its hue."""
    r, g, b = (int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    out = []
    for i in range(n):
        t = 0 if n == 1 else 0.70 * i / (n - 1)
        out.append("#%02x%02x%02x" % tuple(round(c + (255 - c) * t) for c in (r, g, b)))
    return out


def text_on(hexc):
    """White text on dark fills, ink on light ones."""
    r, g, b = (int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    return "white" if (0.299 * r + 0.587 * g + 0.114 * b) < 150 else COLORS["ink"]


def order_at(piv, sel):
    """Columns ordered by their value at sel, largest first (= bottom of a stack)."""
    row = piv.loc[sel] if sel in piv.index else piv.iloc[-1]
    return list(row.fillna(-1).sort_values(ascending=False).index)


def at(s, p):
    """Value of a period-indexed series at p, or NaN."""
    try:
        v = s.get(p)
    except AttributeError:
        return np.nan
    return float(v) if _ok(v) else np.nan


def chunks(seq, n):
    seq = list(seq)
    return [seq[i:i + n] for i in range(0, len(seq), n)] or [[]]


def base(f, **layout):
    f.update_layout(**layout)
    for tr in f.data:
        if tr.type == "bar" and tr.textposition == "outside":
            tr.constraintext = "none"      # otherwise plotly hides labels wider than the bar
    return f


def split(top_title, top_max, frac=.30):
    """Lines get their own strip above the bars, so a line never runs across a bar."""
    return dict(yaxis2=dict(domain=[1 - frac, 1], anchor="x", title=dict(text=top_title, font=dict(size=11)),
                            range=[0, (top_max or 1) * 1.35], showgrid=True, gridcolor="#EFECE4",
                            tickfont=dict(size=11), zeroline=False),
                yaxis_domain=[0, 1 - frac - .07])


def page(fig, *, what, legend=(), insights=(), terms=(), title=None, body_html=None):
    """
    One album page. legend: (colour, name, meaning, shape) with shape in
    bar/line/dash/dot; insights: HTML strings (escape data with _e()); terms: GLOSSARY keys.
    """
    return {"fig": fig, "what": what, "legend": list(legend), "insights": [i for i in insights if i],
            "terms": list(terms), "title": title, "body_html": body_html}


def _wz():
    a, b = WATCH_DPD
    return f"{a}–{b}"


def glossary():
    a, b = WATCH_DPD
    return {
        "stock": ("Сток", "остаток на отчётную дату — снимок. Соседние месяцы не складываются: "
                          "это та же книга, снятая заново."),
        "flow": ("Поток", "то, что произошло внутри месяца (выдачи, погашения). Месяцы можно складывать."
                          + (" Подпись — отчётная дата: «окт» = выдачи за сентябрь." if LABEL_BY_REPORT_DATE else "")),
        "dates": ("Даты", ("отчётные: «окт 2026» = состояние на 1 октября 2026, то есть итог сентября. "
                           "Месяцы выдачи (когорты) не сдвигаются: «сен» = выдано в сентябре.")
                          if LABEL_BY_REPORT_DATE else
                          "месяц, который описывают данные: «сен 2026» = итог сентября."),
        "npl": ("NPL 90+", "кредиты в категориях качества 3–5 (как правило, просрочка больше 90 дней). "
                           "Доля NPL = сумма NPL / весь портфель."),
        "watch": (f"Зона риска {a}–{b}", f"кредиты с просрочкой {a}–{b} дней, ещё не ставшие NPL. "
                                         "Через месяц часть из них перейдёт в NPL — это ранний сигнал."),
        "overdue": ("Корзины просрочки", "дни просрочки на отчётную дату: 1–30, 31–90, 91–180, "
                                         "181–365, 365+. «0 дней» на графиках не показан."),
        "pp": ("п.п.", "процентный пункт — разница двух процентов: 3.2% → 3.5% = +0.3 п.п."),
        "cohort": ("Когорта", "все кредиты, выданные в одном месяце."),
        "mob": ("MOB", "month on book — возраст кредита в месяцах с даты выдачи."),
        "gl": ("GL90+@12MOB", "из 100 кредитов когорты — сколько хотя бы раз ушли в просрочку больше "
                              "90 дней за первые 12 месяцев жизни. GL30+@6MOB — то же для 30 дней и "
                              "6 месяцев. Считается по числу кредитов."),
        "coverage": ("Покрытие", "резервы / NPL 90+. 100% — резервы равны проблемному долгу."),
        "migration": ("Миграция", "куда кредит перешёл через месяц: из 61–90 дней в 90+ (дефолт) "
                                  "или обратно в норму."),
        "insurance": ("NPL без страховки", "каким был бы NPL, если бы страховая не платила: "
                                           "категория до учёта страховых выплат."),
        "court": ("Судебная стадия", "норма — без судебной работы; неофициальная — досудебная работа "
                                     "с должником; официальная — иск подан в суд."),
        "top": (f"Топ-{TOP_CLIENTS}", f"{TOP_CLIENTS} крупнейших клиентов месяца по сумме остатка. "
                                      "Клиенты департамента " + ", ".join(TOP_CLIENTS_EXCLUDE)
                                      + " не учитываются и не называются."),
        "vintage": ("Месяц выдачи", "когорта: все кредиты, выданные в этом месяце."),
    }


# ==========================================================================
# LOAD
# ==========================================================================
def normalise(df):
    df = df.rename(columns=lambda c: str(c).strip().lower().replace(" ", "_")).rename(columns=RENAME)
    missing = [c for c in CANONICAL if c not in df.columns]
    if missing:
        raise KeyError("в данных не хватает колонок: " + ", ".join(missing))

    have_opt = [c for c in OPTIONAL if c in df.columns]
    df = df[CANONICAL + have_opt].copy()

    for c in DATE_COLS:
        df[c] = pd.to_datetime(df[c], errors="coerce")
    for c in AMOUNT_COLS:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0)
    df["maks_dni"] = pd.to_numeric(df["maks_dni"], errors="coerce").fillna(0).astype("int32")
    for c in ("kategoriya_origin", "kategoriya_npl_90", "kategoriya_straxovka"):
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype("int8")
    df["valuta"] = pd.to_numeric(df["valuta"], errors="coerce").fillna(0).astype("int32")
    for c in ("anketa", "contragent"):
        df[c] = pd.to_numeric(df[c], errors="coerce").astype("int64")
    for c in ["filial", "tobo", "department", "department_number", "passport",
              "contragent_name", "sud", "avto"] + have_opt:
        df[c] = df[c].astype("string").str.strip()

    df["avto"] = df["avto"].fillna("0").replace(
        {"0": "non_auto", "0.0": "non_auto", "": "non_auto",
         "nan": "non_auto", "None": "non_auto", "<NA>": "non_auto"})
    df.loc[~df["avto"].isin(["pervichka", "vtorichka"]), "avto"] = "non_auto"
    # spelling variants of the court stage collapse onto three keys; unknown values stay as they are
    s = df["sud"].fillna("norm").str.lower()
    df["sud"] = s.map(lambda v: SUD_ALIASES.get(v, v)).astype("string")
    if have_opt:
        df["oked_name"] = df["oked_name"].fillna("Не указано").replace({"": "Не указано"})
    return df


def _file_range(path):
    """
    Rough period range a file covers, from its name. Used only to skip files
    we definitely don't need — rows are filtered exactly after reading, so a
    range that is too WIDE is harmless and too NARROW loses data. When in
    doubt, return None and the file gets read.

        history_2023.parquet     -> whole of 2023
        history_10.2026.parquet  -> October 2026
    """
    s = path.stem
    years = re.findall(r"20\d{2}", s)
    if not years:
        return None
    year = int(years[-1])
    months = [int(m) for m in re.findall(r"\d{1,2}", re.sub(r"20\d{2}", " ", s))
              if 1 <= int(m) <= 12]
    if months:
        # pad two months each way: the filename may be the stamp, not the period.
        # Count in months, not YYYYMM — 202701 - 2 is 202611, not 202699.
        k = year * 12 + months[0] - 1
        return ((k - 2) // 12) * 100 + (k - 2) % 12 + 1, ((k + 2) // 12) * 100 + (k + 2) % 12 + 1
    return (year - 1) * 100 + 11, (year + 1) * 100 + 1


def _row_period(report_date):
    """report_date is the 1st of the NEXT month, so the period is the day before."""
    a = pd.to_datetime(report_date, errors="coerce") - pd.Timedelta(days=1)
    return a.dt.year * 100 + a.dt.month


def read_months(data_dir, period_from=None, period_to=None):
    """
    Read only the files the request can need, then filter rows exactly.

    history_2023.parquet holds twelve months, history_10.2026.parquet one —
    so choosing files is only a first cut; the row filter is what makes
    202501–202603 not silently include all of 2023.
    """
    files = sorted(Path(data_dir).glob("*.parquet"))
    if not files:
        raise FileNotFoundError(f"нет parquet-файлов в {data_dir}")

    chosen = []
    for f in files:
        rng = _file_range(f)
        if rng is None:
            chosen.append(f)
            continue
        lo, hi = rng
        if period_from and hi < int(period_from):
            continue
        if period_to and lo > int(period_to):
            continue
        chosen.append(f)
    if not chosen:
        raise ValueError(f"нет файлов за период {period_from}–{period_to}")

    df = normalise(pd.concat([pd.read_parquet(f) for f in chosen], ignore_index=True))

    per = _row_period(df["report_date"])
    keep = pd.Series(True, index=df.index)
    if period_from:
        keep &= per >= int(period_from)
    if period_to:
        keep &= per <= int(period_to)
    df = df[keep]
    if df.empty:
        raise ValueError(f"нет данных за период {period_from}–{period_to}")
    return df


def data_fingerprint(data_dir):
    """
    Identity of the input set: name, size and mtime of every parquet file.
    Changes the moment a file is added, replaced or re-saved — which is exactly
    when a cached report stops being valid.
    """
    parts = []
    for f in sorted(Path(str(data_dir)).glob("*.parquet")):
        st = f.stat()
        parts.append(f"{f.name}:{int(st.st_mtime)}:{st.st_size}")
    return hashlib.sha256("|".join(parts).encode()).hexdigest()[:20]


def _code_fingerprint():
    """This file's own content: changing a chart or a setting must not serve an old report."""
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:12]


def run_fingerprint(data_dir, period_from, period_to, selected_period):
    """Same parameters + same files + same code = same report. No need to rebuild it."""
    key = (f"{data_fingerprint(data_dir)}|{_code_fingerprint()}|"
           f"{period_from}|{period_to}|{selected_period}")
    return hashlib.sha256(key.encode()).hexdigest()[:32]


_PERIODS_CACHE = {}


def available_periods(data_dir):
    """
    For the dropdown. Reads only the report_date column, so a yearly file
    costs almost nothing — but it still opens every file, so the answer is
    cached under the data fingerprint: a new upload changes the fingerprint
    and the next call rescans by itself. No cache_clear(), no restart.
    """
    key = data_fingerprint(data_dir)
    if key not in _PERIODS_CACHE:
        out = set()
        for f in sorted(Path(str(data_dir)).glob("*.parquet")):
            try:
                s = pd.read_parquet(f, columns=["report_date"])["report_date"]
            except Exception:
                continue
            out |= set(_row_period(s).dropna().astype(int).unique().tolist())
        _PERIODS_CACHE.clear()
        _PERIODS_CACHE[key] = sorted(int(p) for p in out)
    return _PERIODS_CACHE[key]


# ==========================================================================
# PANEL
# ==========================================================================
def _bucketise(dpd, buckets, order):
    edges = np.array([b[0] for b in buckets[1:]])
    labels = [b[2] for b in buckets]
    idx = np.searchsorted(edges, np.asarray(dpd), side="right")
    return pd.Categorical([labels[i] for i in idx], categories=order, ordered=True)


def build_panel(raw):
    d = raw.copy()
    a = d["report_date"] - pd.Timedelta(days=1)
    d["period"] = (a.dt.year * 100 + a.dt.month).astype("int32")
    v = d["vidacha_sana"]
    d["vintage"] = (v.dt.year * 100 + v.dt.month).astype("Int32")
    d["mob"] = ((a.dt.year - v.dt.year) * 12 + (a.dt.month - v.dt.month)).astype("Int32")

    d["exposure"] = d["brutto_95_summa"]
    d["reserve"] = d["reserve_summa"]
    d["disbursed"] = d["vidacha_tekushiy_summa"]
    d["repaid"] = d["pogashen_tekushiy_summa"]
    d["written_amt"] = d["spisat_95413_summa"]
    d["insurance_paid"] = d["straxovka_summa"]

    d["dpd"] = d["maks_dni"].clip(lower=0)
    d["bucket"] = _bucketise(d["dpd"], REPORT_BUCKETS, BUCKET_ORDER)
    d["mbucket"] = _bucketise(d["dpd"], MIGRATION_BUCKETS, MIGRATION_ORDER)
    d["mob_band"] = pd.cut(d["mob"].astype("float"), MOB_BINS, labels=MOB_LABELS)

    d["is_npl"] = d["kategoriya_npl_90"].isin(NPL_CATEGORIES)
    d["is_watch"] = (~d["is_npl"]) & d["dpd"].between(*WATCH_DPD)
    d["is_new"] = d["disbursed"] > 0
    d["in_court"] = d["sud"].eq("official")

    d["is_npl_gross"] = d["kategoriya_straxovka"].isin(NPL_CATEGORIES)
    d["exposure_gross"] = d["straxovka_brutto_95_summa"].where(
        d["straxovka_brutto_95_summa"] > 0, d["exposure"])

    d["npl_exposure"] = np.where(d["is_npl"], d["exposure"], 0.0)
    d["watch_exposure"] = np.where(d["is_watch"], d["exposure"], 0.0)
    d["npl_gross_exp"] = np.where(d["is_npl_gross"], d["exposure_gross"], 0.0)
    d["cur_name"] = d["valuta"].map(CURRENCY_NAMES).fillna(d["valuta"].astype(str))
    uniq = d["department"].dropna().unique()
    d["dkey"] = d["department"].map({u: dkey(u) for u in uniq}).astype("string")

    has_oked = "oked_name" in d.columns
    keep = ["anketa", "contragent", "contragent_name", "period", "vintage", "mob", "mob_band",
            "dpd", "bucket", "mbucket", "is_npl", "is_watch", "is_new", "is_npl_gross",
            "in_court", "exposure", "exposure_gross", "npl_exposure", "watch_exposure",
            "npl_gross_exp", "reserve", "disbursed", "repaid", "written_amt",
            "insurance_paid", "filial", "department", "dkey", "passport", "avto",
            "valuta", "cur_name", "sud"] + (["oked_name"] if has_oked else [])
    p = d[keep].sort_values(["anketa", "period"], kind="stable").reset_index(drop=True)

    g = p.groupby("anketa", sort=False)
    p["mi"] = (p["period"] // 100) * 12 + (p["period"] % 100)
    p["peak_dpd"] = g["dpd"].cummax()
    prev_mi, next_mi = g["mi"].shift(1), g["mi"].shift(-1)
    back, fwd = prev_mi.eq(p["mi"] - 1), next_mi.eq(p["mi"] + 1)
    p["prev_is_npl"] = g["is_npl"].shift(1).where(back)
    p["prev_exposure"] = g["exposure"].shift(1).where(back)
    p["next_mbucket"] = g["mbucket"].shift(-1).astype("object").where(fwd, "EXIT")
    p["exited_after"] = ~fwd
    return p


# ==========================================================================
# MARTS
# ==========================================================================
def by_period(p, dim=None):
    keys = ["period"] + ([dim] if dim else [])
    g = p.groupby(keys, observed=True)
    court = p["exposure"].where(p["in_court"], 0.0)
    m = pd.DataFrame({
        # --- STOCK: measured on the reporting date, never summed across months
        "exposure": g["exposure"].sum(), "npl_exposure": g["npl_exposure"].sum(),
        "watch_exposure": g["watch_exposure"].sum(),
        "npl_gross_exp": g["npl_gross_exp"].sum(),
        "exposure_gross": g["exposure_gross"].sum(), "reserve": g["reserve"].sum(),
        "n_loans": g["anketa"].size(), "n_clients": g["contragent"].nunique(),
        "court_exp": court.groupby([p[k] for k in keys], observed=True).sum(),
        # --- FLOW: happened inside the month, summing across months is correct
        "disbursed": g["disbursed"].sum(), "repaid": g["repaid"].sum(),
        "written_amt": g["written_amt"].sum(), "n_disbursed": g["is_new"].sum(),
    }).reset_index()
    nz = lambda s: s.replace(0, np.nan)
    m["npl_ratio"] = m["npl_exposure"] / nz(m["exposure"])
    m["watch_ratio"] = m["watch_exposure"] / nz(m["exposure"])
    m["npl_ratio_gross"] = m["npl_gross_exp"] / nz(m["exposure_gross"])
    m["coverage"] = m["reserve"] / nz(m["npl_exposure"])
    m["court_share"] = m["court_exp"] / nz(m["exposure"])
    m["avg_ticket"] = m["exposure"] / nz(m["n_loans"])
    if dim:
        m = m.rename(columns={dim: "dim_value"})
        m["dim_value"] = m["dim_value"].astype("string")
    return m


def top_clients(panel, totals):
    """
    Each month's TOP_CLIENTS largest clients by balance, departments in
    TOP_CLIENTS_EXCLUDE left out entirely (their clients are never ranked or named).
    Returns (all clients ranked per period, top rows, per-period summary, top by department).
    """
    excl = {dkey(x) for x in TOP_CLIENTS_EXCLUDE}
    p = panel[(panel["exposure"] > MIN_BALANCE) & ~panel["dkey"].isin(excl)]
    g = (p.groupby(["period", "contragent"], observed=True)
          .agg(exposure=("exposure", "sum"), npl=("npl_exposure", "sum"),
               dpd=("dpd", "max"), n_loans=("anketa", "size"),
               name=("contragent_name", "first"))
          .reset_index()
          .sort_values(["period", "exposure"], ascending=[True, False], kind="stable"))
    g["rank"] = g.groupby("period").cumcount() + 1
    top = g[g["rank"] <= TOP_CLIENTS].copy()

    keys = top[["period", "contragent"]]
    sub = p.merge(keys, on=["period", "contragent"], how="inner")
    deps = (sub.groupby(["period", "contragent"], observed=True)["department"]
               .agg(lambda s: ", ".join(dept_sorted(s.unique()))).rename("deps").reset_index())
    top = top.merge(deps, on=["period", "contragent"], how="left")
    by_dep = (sub.groupby(["period", "department"], observed=True)["exposure"].sum()
                 .reset_index().rename(columns={"department": "dim_value"}))
    by_dep["dim_value"] = by_dep["dim_value"].astype("string")

    tot = totals.set_index("period")["exposure"]
    periods = sorted(top["period"].unique())
    rows, prev = [], None
    for per in periods:
        t = top[top["period"] == per]
        ids = set(t["contragent"])
        rows.append({"period": per, "exposure": float(t["exposure"].sum()),
                     "share": float(t["exposure"].sum()) / float(tot.get(per, np.nan) or np.nan),
                     "top1_share": float(t["exposure"].max()) / float(tot.get(per, np.nan) or np.nan),
                     "newcomers": len(ids - prev) if prev is not None else np.nan})
        prev = ids
    return g, top, pd.DataFrame(rows), by_dep


def build_marts(panel, snap, periods, sel, has_oked):
    # ---------------- Direction A: dynamics ----------------
    A = {"total": by_period(panel).sort_values("period")}
    for d in ["department", "filial", "cur_name"] + (["oked_name"] if has_oked else []):
        A[d] = by_period(panel, d)

    # delinquency mix as shares of the WHOLE month's portfolio
    g = panel.groupby(["period", "bucket"], observed=True)["exposure"].sum().reset_index()
    g["share"] = g["exposure"] / g.groupby("period", observed=True)["exposure"].transform("sum")
    A["bucket_mix"] = g

    # stock/flow
    t = A["total"].copy().reset_index(drop=True)
    t["prev_exposure"] = t["exposure"].shift(1)
    t["delta"] = t["exposure"] - t["prev_exposure"]
    A["stock_flow"] = t

    # NPL bridge: closing = opening + inflow - cured - exited + residual
    stock = panel.groupby("period", observed=True)["npl_exposure"].sum()
    q = panel[panel["prev_is_npl"].notna()]
    inflow = q[q["is_npl"] & ~q["prev_is_npl"].astype(bool)] \
        .groupby("period", observed=True)["exposure"].sum()
    cured = q[~q["is_npl"] & q["prev_is_npl"].astype(bool)] \
        .groupby("period", observed=True)["prev_exposure"].sum()
    exited = (panel[panel["is_npl"] & panel["exited_after"]]
              .assign(np_=lambda x: x["period"].map(lambda v: shift_p(v, -1)))
              .groupby("np_", observed=True)["exposure"].sum())
    rows = []
    for i, per in enumerate(periods[1:], 1):
        op, cl = float(stock.get(periods[i - 1], 0)), float(stock.get(per, 0))
        inf, cu, ex = (float(inflow.get(per, 0)), float(cured.get(per, 0)),
                       float(exited.get(per, 0)))
        rows.append({"period": per, "opening": op, "inflow": inf, "cured": -cu,
                     "exited": -ex, "residual": cl - (op + inf - cu - ex), "closing": cl})
    A["bridge"] = pd.DataFrame(rows)

    # migration between the FINE buckets, month over month
    tr = panel[panel["next_mbucket"].notna()]
    tr = pd.DataFrame({"period": tr["period"], "from_b": tr["mbucket"].astype("string"),
                       "to_b": tr["next_mbucket"].astype("string"), "anketa": tr["anketa"]})
    gg = tr.groupby(["period", "from_b", "to_b"], observed=True)["anketa"] \
           .size().reset_index(name="n")
    gg["rate"] = gg["n"] / gg.groupby(["period", "from_b"], observed=True)["n"].transform("sum")
    A["transitions"] = gg

    # vintages — cohorts are keyed on origination month, so they ignore the window
    vv = panel[panel["vintage"].notna() & panel["mob"].between(0, 36)].copy()
    THRS = sorted({t_ for t_, _ in VINTAGE_MARKS})
    for thr in THRS:
        vv[f"ever_{thr}"] = vv["peak_dpd"] > thr
    gv = vv.groupby(["vintage", "mob"], observed=True)
    vin = pd.DataFrame({"n_loans": gv["anketa"].size()})
    for thr in THRS:
        vin[f"gl{thr}"] = gv[f"ever_{thr}"].sum() / gv["anketa"].size()
    vin = vin.reset_index()
    vin["reliable"] = vin["n_loans"] >= MIN_COHORT
    A["vin_marks"] = pd.concat(
        [vin[vin["mob"] == mob].assign(metric=f"GL{thr}+@{mob}MOB", rate=vin[f"gl{thr}"])
            [["vintage", "metric", "rate", "n_loans", "reliable"]]
         for thr, mob in VINTAGE_MARKS], ignore_index=True)

    # products per department, chosen and ORDERED by their standing at SEL
    top_pass = {}
    for dep in dept_sorted(snap["department"].dropna().unique()):
        s = (snap[snap["department"] == dep]
             .groupby("passport", observed=True)["exposure"].sum()
             .sort_values(ascending=False))
        top_pass[str(dep)] = [str(x) for x in s.head(TOP_PASSPORTS).index]
    pp = panel[["period", "department", "passport", "exposure", "npl_exposure"]].copy()
    pp["passport_grp"] = pp["passport"].astype("string")
    for dep, keep in top_pass.items():
        mask = (pp["department"] == dep) & (~pp["passport"].isin(keep))
        pp.loc[mask, "passport_grp"] = "Прочие"
    gp = pp.groupby(["period", "department", "passport_grp"], observed=True)
    A["passport_dep"] = pd.DataFrame({"exposure": gp["exposure"].sum(),
                                      "npl_exposure": gp["npl_exposure"].sum()}).reset_index()

    A["clients_ranked"], A["top"], A["top_summary"], A["top_by_dep"] = \
        top_clients(panel, A["total"])

    # ---------------- Direction B: one reporting date ----------------
    tot_exp = float(snap["exposure"].sum())
    tot_npl = float(snap["npl_exposure"].sum())

    def structure(dim):
        gg = snap.groupby(dim, observed=True)
        m = pd.DataFrame({
            "exposure": gg["exposure"].sum(), "npl_exposure": gg["npl_exposure"].sum(),
            "reserve": gg["reserve"].sum(),
            "n_loans": gg["anketa"].size(), "n_clients": gg["contragent"].nunique(),
        }).reset_index().rename(columns={dim: "name"})
        m["name"] = m["name"].astype("string")
        nz = lambda x: x.replace(0, np.nan)
        m["share"] = m["exposure"] / tot_exp if tot_exp else np.nan
        m["npl_ratio"] = m["npl_exposure"] / nz(m["exposure"])
        m["npl_contrib"] = m["npl_exposure"] / tot_npl if tot_npl else np.nan
        m["avg_ticket"] = m["exposure"] / nz(m["n_loans"])
        return m.sort_values("exposure", ascending=False)

    B = {"_tot_exp": tot_exp, "_tot_npl": tot_npl,
         "_n_clients": int(snap["contragent"].nunique()), "_n_loans": int(len(snap))}
    for d in ["department", "filial", "passport", "bucket", "mob_band"] \
            + (["oked_name"] if has_oked else []):
        B[d] = structure(d)

    # branch × department, for the stacked branch chart
    fd = snap.groupby(["filial", "department"], observed=True)["exposure"].sum().reset_index()
    B["filial_dep"] = fd

    # what the book is made of, by origination month
    vg = snap.groupby("vintage", observed=True)
    vm = pd.DataFrame({"exposure": vg["exposure"].sum(),
                       "npl_exposure": vg["npl_exposure"].sum(),
                       "n_loans": vg["anketa"].size()}).reset_index()
    vm["share"] = vm["exposure"] / tot_exp if tot_exp else np.nan
    vm["npl_ratio"] = vm["npl_exposure"] / vm["exposure"].replace(0, np.nan)
    B["vintage_mix"] = vm

    # branch × bucket, as shares of each branch's own portfolio
    fb = snap.groupby(["filial", "bucket"], observed=True)["exposure"].sum().reset_index()
    fb["share"] = fb["exposure"] / fb.groupby("filial", observed=True)["exposure"] \
                                     .transform("sum").replace(0, np.nan)
    B["filial_bucket"] = fb

    # client burden — the average behaviour of a client holding N loans
    cnt = snap.groupby("contragent", observed=True).agg(
        n_loans=("anketa", "size"), exposure=("exposure", "sum"),
        npl=("npl_exposure", "sum")).reset_index()
    cnt["burden"] = pd.cut(cnt["n_loans"], [0, 1, 2, 3, 4, 10**9],
                           labels=["1", "2", "3", "4", "5+"])
    bg = cnt.groupby("burden", observed=True)
    bd = pd.DataFrame({"n_clients": bg["contragent"].size(),
                       "exposure": bg["exposure"].sum(),
                       "avg_exposure": bg["exposure"].mean(),
                       "npl": bg["npl"].sum()}).reset_index()
    bd["client_share"] = bd["n_clients"] / max(bd["n_clients"].sum(), 1)
    bd["exposure_share"] = bd["exposure"] / (bd["exposure"].sum() or 1)
    bd["npl_ratio"] = bd["npl"] / bd["exposure"].replace(0, np.nan)
    B["burden"] = bd

    # passport × department at SEL
    pdm = snap.groupby(["department", "passport"], observed=True)
    bpd = pd.DataFrame({"exposure": pdm["exposure"].sum(),
                        "npl_exposure": pdm["npl_exposure"].sum(),
                        "n_loans": pdm["anketa"].size()}).reset_index()
    bpd["npl_ratio"] = bpd["npl_exposure"] / bpd["exposure"].replace(0, np.nan)
    bpd["share"] = bpd["exposure"] / tot_exp if tot_exp else np.nan
    B["passport_dep"] = bpd

    # court stage × auto segment, one department only
    ck = dkey(COURT_DEPARTMENT)
    cs = snap[snap["dkey"] == ck]
    B["court"] = (cs.groupby(["avto", "sud"], observed=True)
                    .agg(exposure=("exposure", "sum"), n_loans=("anketa", "size"))
                    .reset_index())
    B["court_dep_name"] = (str(cs["department"].iloc[0]) if len(cs) else COURT_DEPARTMENT)

    return A, B, top_pass


# ==========================================================================
# CHARTS
#
# Every builder has the same shape: fn(A, B, ctx) -> page(...) or a list of
# pages (long branch lists continue on the next page). They take marts as
# arguments rather than reading globals, because two requests can be running
# with different periods at the same time.
# ==========================================================================
def _x(periods):
    return [plabel(p) for p in periods]


def _piv(df, val, agg="sum"):
    return df.pivot_table(index="period", columns="dim_value", values=val, aggfunc=agg)


def _total(A):
    return A["total"].set_index("period")


def _trend(name, s, sel, dec=2, pp=True):
    """'NPL 90+: 3.21% (за месяц +0.12 п.п., за год −0.40 п.п.)' from a % series."""
    now, m1, y1 = at(s, sel), at(s, shift_p(sel, 1)), at(s, shift_p(sel, 12))
    if not _ok(now):
        return ""
    parts = []
    if _ok(m1):
        parts.append(f"за месяц {fpp(now - m1, dec)}" if pp else f"за месяц {fchg(now, m1)}")
    if _ok(y1):
        parts.append(f"за год {fpp(now - y1, dec)}" if pp else f"за год {fchg(now, y1)}")
    tail = f" ({', '.join(parts)})" if parts else ""
    return f"{name}: <b>{fpct(now, dec)}</b>{tail}."


def _dept_legend(names, shares=None):
    out = []
    for d in names:
        sh = f" — {fpct(shares.get(d) * 100)} на дату" if shares is not None and _ok(shares.get(d)) else ""
        out.append((dcolor(d), _e(dname(d)), f"департамент{sh}", "bar"))
    return out


def _stack_text(v, share, step, i, n, min_share=10):
    return f"{share:.0f}%" if _ok(share) and share >= min_share and (i % step == 0 or i == n - 1) else ""


# ---------------------------------------------------------------- A: dynamics
def a01_portfolio(A, B, ctx):
    sel = ctx["sel"]
    piv = _piv(A["department"], "exposure")
    t = _total(A).reindex(piv.index)
    order = order_at(piv, sel)
    x = _x(piv.index)
    n, step = len(x), max(1, math.ceil(len(x) / MAX_LABELS))
    tot = money(t["exposure"])
    f = go.Figure()
    for dep in order:
        y = money(nan0(piv[dep]))
        sh = piv[dep] / t["exposure"] * 100
        f.add_bar(x=x, y=y, name=dname(dep), marker_color=dcolor(dep),
                  text=[_stack_text(v, s, step, i, n) for i, (v, s) in enumerate(zip(y, sh))],
                  textposition="inside", insidetextanchor="middle",
                  textfont=dict(size=11, color=text_on(dcolor(dep))),
                  customdata=sh, hovertemplate="%{x} · " + _e(dname(dep)) +
                  "<br>%{y:,.1f} " + UNIT_NAME + " (%{customdata:.1f}%)<extra></extra>")
    f.add_scatter(x=x, y=tot, mode="text", text=thin(tot, famt), textposition="top center",
                  textfont=dict(size=LABEL_SIZE, color=COLORS["ink"]), hoverinfo="skip")
    npl, wat = t["npl_ratio"] * 100, t["watch_ratio"] * 100
    f.add_scatter(x=x, y=npl, name="NPL 90+, %", yaxis="y2", mode="lines+markers+text",
                  line=dict(color=COLORS["npl"], width=3), marker=dict(size=5),
                  text=thin(npl, lambda v: f"{v:.2f}%", max_labels=8), textposition="top center",
                  textfont=dict(size=11, color=COLORS["npl"]),
                  hovertemplate="%{x}<br>NPL 90+: %{y:.2f}%<extra></extra>")
    f.add_scatter(x=x, y=wat, name=f"Зона риска {_wz()}, %", yaxis="y2", mode="lines",
                  line=dict(color=COLORS["watch"], width=2.2, dash="dot"),
                  hovertemplate="%{x}<br>зона риска: %{y:.2f}%<extra></extra>")
    base(f, barmode="stack", bargap=.25, yaxis=dict(title=UNIT_NAME, range=[0, _safemax(tot) * 1.12]),
         **split("NPL и зона риска, %", max(_safemax(npl), _safemax(wat))))

    T = _total(A)
    shares = (piv.loc[sel] / T.loc[sel, "exposure"]) if sel in piv.index else None
    big = order[0] if order else None
    ins = [
        f"Портфель на {plabel_full(sel)}: <b>{fnum(at(T['exposure'], sel) / UNIT)} {UNIT_NAME}</b> "
        f"(за месяц {fchg(at(T['exposure'], sel), at(T['exposure'], shift_p(sel, 1)))}, "
        f"за год {fchg(at(T['exposure'], sel), at(T['exposure'], shift_p(sel, 12)))}).",
        (f"Крупнейший департамент — <b>{_e(dname(big))}</b>: {fpct(shares.get(big) * 100)} портфеля."
         if big is not None and shares is not None else ""),
        _trend("Доля NPL 90+", T["npl_ratio"] * 100, sel),
        _trend(f"Зона риска {_wz()}", T["watch_ratio"] * 100, sel),
    ]
    return page(f, what="Остаток кредитного портфеля на каждую отчётную дату, разделённый по "
                        "департаментам (столбцы, левая шкала), и его качество (линии в полосе сверху, %).",
                legend=_dept_legend(order, shares) + [
                    (COLORS["ink"], "Число над столбцом", f"весь портфель банка, {UNIT_NAME}", "text"),
                    (COLORS["npl"], "Красная линия", "доля NPL 90+ в портфеле, %", "line"),
                    (COLORS["watch"], "Оранжевый пунктир",
                     f"зона риска: просрочка {_wz()} дней, ещё не NPL", "dot")],
                insights=ins, terms=["dates", "npl", "watch"])


def a02_stock_flow(A, B, ctx):
    sel = ctx["sel"]
    d = A["stock_flow"]
    x = _x(d["period"])
    dis, rep = money(d["disbursed"]), money(d["repaid"])
    f = go.Figure()
    f.add_bar(x=x, y=dis, name="Выдано", marker_color=COLORS["good"],
              text=thin(dis, max_labels=8), textposition="outside", cliponaxis=False,
              textfont=dict(size=11, color=COLORS["good"]),
              hovertemplate="%{x}<br>выдано %{y:,.1f} " + UNIT_NAME + "<extra></extra>")
    f.add_bar(x=x, y=rep, name="Погашено", marker_color=COLORS["neutral"],
              text=thin(rep, max_labels=8), textposition="outside", cliponaxis=False,
              textfont=dict(size=11, color=COLORS["neutral"]),
              hovertemplate="%{x}<br>погашено %{y:,.1f} " + UNIT_NAME + "<extra></extra>")
    base(f, barmode="group", bargap=.22, bargroupgap=.05, yaxis=dict(title=UNIT_NAME))

    s = d.set_index("period")
    best = s["disbursed"].idxmax() if s["disbursed"].notna().any() else None
    dl, rl = at(s["disbursed"], sel), at(s["repaid"], sel)
    ins = [
        f"За период выдано <b>{fnum(s['disbursed'].sum() / UNIT)}</b>, погашено "
        f"<b>{fnum(s['repaid'].sum() / UNIT)} {UNIT_NAME}</b>.",
        (f"В {plabel_full(sel)} выдачи {'превысили' if dl >= rl else 'уступили'} погашениям на "
         f"<b>{fnum(abs(dl - rl) / UNIT)} {UNIT_NAME}</b>." if _ok(dl) and _ok(rl) else ""),
        (f"Рекордный месяц по выдачам — {plabel_full(best)}: {fnum(s.loc[best, 'disbursed'] / UNIT)} "
         f"{UNIT_NAME}." if best is not None else ""),
    ]
    return page(f, what="Сколько денег банк выдал и сколько клиенты вернули в каждом месяце. "
                        "Списания и прочие изменения остатка здесь не показаны.",
                legend=[(COLORS["good"], "Выдано", "новые кредиты, выданные за месяц", "bar"),
                        (COLORS["neutral"], "Погашено", "основной долг, возвращённый за месяц", "bar")],
                insights=ins, terms=["flow"])


def _bucket_cols(piv):
    keep = [b for b in BUCKET_ORDER if b in piv.columns]
    return keep if SHOW_CURRENT_BUCKET else [b for b in keep if b != "CUR"]


def a03_bucket_mix(A, B, ctx):
    sel = ctx["sel"]
    piv = A["bucket_mix"].pivot_table(index="period", columns="bucket",
                                      values="share", aggfunc="sum", observed=True).fillna(0) * 100
    cols = _bucket_cols(piv)
    x = _x(piv.index)
    n, step = len(x), max(1, math.ceil(len(x) / MAX_LABELS))
    f = go.Figure()
    for b in cols:
        v = piv[b]
        f.add_bar(x=x, y=v, name=lab(b), marker_color=BUCKET_COLORS[b],
                  text=[f"{z:.1f}" if (i % step == 0 or i == n - 1) and z >= .6 else ""
                        for i, z in enumerate(v)],
                  textposition="inside", insidetextanchor="middle",
                  textfont=dict(size=11, color=text_on(BUCKET_COLORS[b])),
                  hovertemplate="%{x}<br>" + lab(b) + ": %{y:.2f}% портфеля<extra></extra>")
    bad = piv[cols].sum(axis=1)
    f.add_scatter(x=x, y=bad, mode="lines+markers+text", line=dict(color=COLORS["ink"], width=2),
                  marker=dict(size=4), text=thin(bad, lambda v: f"{v:.1f}%"),
                  textposition="top center", textfont=dict(size=LABEL_SIZE),
                  hovertemplate="%{x}<br>всего с просрочкой: %{y:.2f}%<extra></extra>")
    base(f, barmode="stack", bargap=.25,
         yaxis=dict(title="% всего портфеля", range=[0, _safemax(bad) * 1.18]))

    deep = [b for b in cols if b in ("B91_180", "B181_365", "B365P")]
    cur_share = at(piv["CUR"], sel) if "CUR" in piv.columns else np.nan
    biggest = piv.loc[sel, cols].idxmax() if sel in piv.index and cols else None
    ins = [
        _trend("Всего с просрочкой", bad, sel),
        (f"Без просрочки — {fpct(cur_share)} портфеля (на графике не показан, чтобы были "
         f"видны остальные корзины)." if _ok(cur_share) and not SHOW_CURRENT_BUCKET else ""),
        (f"Крупнейшая корзина на {plabel_full(sel)} — <b>{lab(biggest)}</b>: "
         f"{fpct(piv.loc[sel, biggest])} портфеля." if biggest is not None else ""),
        _trend("Глубокая просрочка 90+ дней", piv[deep].sum(axis=1), sel) if deep else "",
    ]
    return page(f, what="Какая часть портфеля просрочена и насколько глубоко — по каждому месяцу. "
                        "Высота столбца = доля всего портфеля с любой просрочкой.",
                legend=[(BUCKET_COLORS[b], lab(b), "просрочка столько дней, % всего портфеля", "bar")
                        for b in cols] +
                       [(COLORS["ink"], "Чёрная линия", "сумма всех корзин — весь просроченный портфель", "line")],
                insights=ins, terms=["overdue", "pp"])


def a04_npl_departments(A, B, ctx):
    sel = ctx["sel"]
    piv = _piv(A["department"], "npl_ratio", "mean") * 100
    deps = dept_sorted(piv.columns)
    x = _x(piv.index)
    f = go.Figure()
    for dep in deps:
        v = piv[dep]
        f.add_scatter(x=x, y=v, name=dname(dep), mode="lines+markers+text",
                      line=dict(width=3, color=dcolor(dep)), marker=dict(size=4),
                      text=thin(v, lambda z: f"{z:.1f}", max_labels=7),
                      textposition="top center", textfont=dict(size=11, color=dcolor(dep)),
                      hovertemplate="%{x} · " + _e(dname(dep)) + "<br>NPL %{y:.2f}%<extra></extra>")
    tv = _total(A).reindex(piv.index)["npl_ratio"] * 100
    f.add_scatter(x=x, y=tv, name="Банк", mode="lines",
                  line=dict(color=COLORS["ink"], width=1.8, dash="dash"),
                  hovertemplate="%{x}<br>банк: %{y:.2f}%<extra></extra>")
    base(f, yaxis=dict(title="NPL 90+, % портфеля департамента"))

    row = piv.loc[sel].dropna() if sel in piv.index else pd.Series(dtype=float)
    ins = []
    if len(row):
        worst, best = row.idxmax(), row.idxmin()
        ins.append(f"Самый высокий NPL на {plabel_full(sel)} — <b>{_e(dname(worst))}</b>: "
                   f"{fpct(row[worst], 2)}; самый низкий — {_e(dname(best))}: {fpct(row[best], 2)}.")
        bank = at(tv, sel)
        above = [dname(d) for d in deps if _ok(row.get(d)) and row[d] > bank]
        if above and _ok(bank):
            ins.append(f"Выше банка ({fpct(bank, 2)}): {_e(', '.join(above))}.")
        y1 = piv.loc[shift_p(sel, 12)] if shift_p(sel, 12) in piv.index else None
        if y1 is not None:
            moves = (row - y1).dropna()
            if len(moves):
                w = moves.idxmax()
                ins.append(f"Сильнее всего за год вырос NPL у {_e(dname(w))}: {fpp(moves[w])}.")
    new = [dname(d) for d in deps if piv[d].first_valid_index() not in (None, piv.index[0])]
    if new:
        ins.append(f"Линия {_e(', '.join(new))} начинается позже: департамент появился в данных не с начала периода.")
    return page(f, what="Доля NPL 90+ внутри каждого департамента: какая часть его собственного "
                        "портфеля проблемная. Пунктир — банк целиком, для сравнения.",
                legend=[(dcolor(d), _e(dname(d)), "NPL департамента, % его портфеля", "line") for d in deps] +
                       [(COLORS["ink"], "Пунктир", "NPL банка целиком", "dash")],
                insights=ins, terms=["npl", "pp"])


def _branch_hidden_note(df, name_col="dim_value", val="exposure", sel=None):
    m = df[df[name_col].map(is_no_branch)]
    if sel is not None and "period" in m.columns:
        m = m[m["period"] == sel]
    v = float(m[val].sum()) if len(m) else 0.0
    return (f"Кредиты без филиала (Nodata): {fnum(v / UNIT)} {UNIT_NAME} — на графике не показаны."
            if v > 0 else "")


def a05_branch_heatmap(A, B, ctx):
    sel = ctx["sel"]
    fil = A["filial"][~A["filial"]["dim_value"].map(is_no_branch)]
    piv = _piv(fil, "npl_ratio", "mean") * 100
    if piv.empty:
        raise ValueError("нет данных по филиалам")
    last = piv.loc[sel] if sel in piv.index else piv.iloc[-1]
    order = list(last.sort_values(ascending=False).index)
    x = _x(piv.index)
    ncol = len(x)
    step = 1 if ncol <= 18 else max(1, math.ceil(ncol / 12))
    bank = _total(A)["npl_ratio"] * 100
    zmax = float(np.nanpercentile(piv.to_numpy(dtype=float), 98)) if np.isfinite(piv.to_numpy(dtype=float)).any() else 1

    y1 = shift_p(sel, 12)
    move = (piv.loc[sel] - piv.loc[y1]).dropna() if sel in piv.index and y1 in piv.index else pd.Series(dtype=float)
    above = int((last > at(bank, sel)).sum()) if _ok(at(bank, sel)) else 0
    ins = [f"Хуже всего на {plabel_full(sel)}: " + "; ".join(
               f"<b>{_e(b)}</b> {fpct(last[b])}" for b in order[:3] if _ok(last.get(b))) + ".",
           f"Выше среднего по банку ({fpct(at(bank, sel), 2)}): {above} из {len(order)} филиалов.",
           (f"Сильнее всего за год ухудшился {_e(move.idxmax())}: {fpp(move.max(), 1)}."
            if len(move) and move.max() > 0 else ""),
           _branch_hidden_note(A["filial"], sel=sel)]

    pages_ = []
    parts = chunks(order, BRANCHES_PER_PAGE)
    for k, part in enumerate(parts, 1):
        sub = piv[part]
        z = sub.T.to_numpy(dtype=float)
        keep = _label_idx(ncol, None if ncol > 18 else ncol)
        txt = [[f"{z[r, c]:.1f}" if c in keep and np.isfinite(z[r, c]) else ""
                for c in range(ncol)] for r in range(z.shape[0])]
        f = go.Figure(go.Heatmap(
            z=z, x=x, y=part, text=txt, texttemplate="%{text}", textfont=dict(size=10),
            zmin=0, zmax=max(zmax, .1),
            colorscale=[[0, "#FFFFFF"], [.25, "#F6E3A8"], [.6, COLORS["watch"]], [1, COLORS["npl"]]],
            colorbar=dict(title="NPL, %", thickness=12, len=.8),
            xgap=1, ygap=1, hovertemplate="%{y}<br>%{x}: NPL %{z:.2f}%<extra></extra>"))
        base(f, yaxis=dict(autorange="reversed", tickfont=dict(size=11)),
             xaxis=dict(side="top", tickangle=-45 if ncol > 18 else 0))
        sfx = f" ({k}/{len(parts)})" if len(parts) > 1 else ""
        pages_.append(page(
            f, title=f"Доля NPL 90+ по филиалам и месяцам{sfx}",
            what="Каждая клетка — доля NPL 90+ в портфеле филиала за месяц. Филиалы отсортированы "
                 f"по {plabel_full(sel)}: худшие сверху.",
            legend=[("#FFFFFF", "Белый", "NPL близок к нулю", "bar"),
                    (COLORS["watch"], "Оранжевый", "средний уровень", "bar"),
                    (COLORS["npl"], "Красный", f"высокий NPL (≈{zmax:.0f}% и выше)", "bar")],
            insights=ins if k == 1 else ["Продолжение списка филиалов — порядок тот же."] + ins[-1:],
            terms=["npl"]))
    return pages_


def a06_bridge(A, B, ctx):
    sel = ctx["sel"]
    d = A["bridge"]
    x = _x(d["period"])
    delta = money(d["closing"] - d["opening"])
    f = go.Figure()
    spec = (("inflow", COLORS["npl"], "Новые NPL (+)", "кредиты, которые в этом месяце стали NPL"),
            ("cured", COLORS["good"], "Вылечились (−)", "были NPL, стали нормальными"),
            ("exited", "#4F7CAC", "Ушли с баланса (−)", "NPL-кредиты закрыты или списаны"),
            ("residual", COLORS["light"], "Погашения и прочее", "частичные погашения внутри NPL"))
    for k, c, n, _ in spec:
        f.add_bar(x=x, y=money(d[k]), name=n, marker_color=c,
                  hovertemplate="%{x}<br>" + n + ": %{y:,.2f} " + UNIT_NAME + "<extra></extra>")
    f.add_scatter(x=x, y=delta, mode="lines+markers+text", line=dict(color=COLORS["ink"], width=2.6),
                  marker=dict(size=5), text=thin(delta, lambda v: fnum(v, 1)),
                  textposition="top center", textfont=dict(size=LABEL_SIZE),
                  hovertemplate="%{x}<br>итог: %{y:+,.2f} " + UNIT_NAME + "<extra></extra>")
    base(f, barmode="relative", bargap=.25, yaxis=dict(title=UNIT_NAME))

    s = d.set_index("period")
    ins = []
    if sel in s.index:
        r = s.loc[sel]
        ins.append(f"В {plabel_full(sel)}: новых NPL <b>{fnum(r.inflow / UNIT, 2)}</b>, вылечились "
                   f"{fnum(-r.cured / UNIT, 2)}, ушли с баланса {fnum(-r.exited / UNIT, 2)} {UNIT_NAME}. "
                   f"Итог: NPL {'вырос' if r.closing >= r.opening else 'снизился'} на "
                   f"<b>{fnum(abs(r.closing - r.opening) / UNIT, 2)} {UNIT_NAME}</b>.")
    if len(s):
        cure_rate = -s["cured"].sum() / s["inflow"].sum() if s["inflow"].sum() else np.nan
        ins.append(f"За период на каждые 100 сум новых NPL вылечилось {fnum(cure_rate * 100, 0)} сум.")
        w = s["inflow"].idxmax()
        ins.append(f"Больше всего новых NPL — в {plabel_full(w)}: {fnum(s.loc[w, 'inflow'] / UNIT, 2)} {UNIT_NAME}.")
    return page(f, what="Почему изменилась сумма NPL за месяц: сколько добавилось, сколько вылечилось "
                        "и сколько ушло с баланса. Чёрная линия — итоговое изменение.",
                legend=[(c, n, m, "bar") for _, c, n, m in spec] +
                       [(COLORS["ink"], "Чёрная линия", "итог: на сколько изменился NPL за месяц", "line")],
                insights=ins, terms=["npl", "flow"])


def a07_vintage_quality(A, B, ctx):
    vm = A["vin_marks"]
    vm = vm[vm.reliable]
    m12 = vm[vm.metric == "GL90+@12MOB"].set_index("vintage")["rate"] * 100
    m6 = vm[vm.metric == "GL30+@6MOB"].set_index("vintage")["rate"] * 100
    idx = sorted(set(m12.index) | set(m6.index))
    if not idx:
        raise ValueError("нет когорт с достаточным числом кредитов")
    x = [vlabel(v) for v in idx]
    v12, v6 = m12.reindex(idx), m6.reindex(idx)
    f = go.Figure()
    f.add_bar(x=x, y=v6, name="GL30+@6MOB", marker_color=COLORS["watch"],
              text=thin(v6, lambda z: f"{z:.1f}", max_labels=10), textposition="outside",
              cliponaxis=False, textfont=dict(size=11, color=COLORS["watch"]),
              hovertemplate="выдача %{x}<br>GL30+@6MOB: %{y:.1f}%<extra></extra>")
    f.add_bar(x=x, y=v12, name="GL90+@12MOB", marker_color=COLORS["npl"],
              text=thin(v12, lambda z: f"{z:.1f}", max_labels=10), textposition="outside",
              cliponaxis=False, textfont=dict(size=11, color=COLORS["npl"]),
              hovertemplate="выдача %{x}<br>GL90+@12MOB: %{y:.1f}%<extra></extra>")
    avg = float(np.nanmean(v12)) if v12.notna().sum() else np.nan
    if _ok(avg):
        f.add_hline(y=avg, line=dict(color=COLORS["ink"], width=1.2, dash="dot"),
                    annotation_text=f"среднее GL90+@12MOB: {avg:.1f}%",
                    annotation_position="top left", annotation_font_size=12)
    base(f, barmode="group", bargap=.2, xaxis=dict(title="месяц выдачи кредита"),
         yaxis=dict(title="% кредитов когорты"))

    ins = []
    ex = v12.dropna()
    if len(ex):
        v = ex.index[-1]
        ins.append(f"Пример: из 100 кредитов, выданных в {vlabel_full(v)}, <b>{ex.iloc[-1]:.0f}</b> "
                   f"хотя бы раз ушли в просрочку больше 90 дней за первые 12 месяцев.")
        w = ex.idxmax()
        ins.append(f"Худшая когорта — {vlabel_full(w)}: {fpct(ex[w])}; среднее {fpct(avg)}.")
        if len(ex) >= 12:
            a_, b_ = ex.iloc[-6:].mean(), ex.iloc[-12:-6].mean()
            ins.append(f"Последние 6 когорт в среднем {fpct(a_)} против {fpct(b_)} у предыдущих 6 — "
                       f"выдачи {'ухудшаются' if a_ > b_ else 'улучшаются'}.")
    ins.append("Правые месяцы без красного столбца — когорты ещё не прожили 12 месяцев, это не ноль.")
    return page(f, what="Качество выдач: как ведёт себя каждая когорта — все кредиты, выданные в один месяц. "
                        "Чем ниже столбцы, тем лучше выдавали.",
                legend=[(COLORS["watch"], "GL30+@6MOB",
                         "из 100 кредитов — сколько допустили просрочку больше 30 дней в первые 6 месяцев", "bar"),
                        (COLORS["npl"], "GL90+@12MOB",
                         "из 100 кредитов — сколько допустили просрочку больше 90 дней в первые 12 месяцев", "bar"),
                        (COLORS["ink"], "Пунктир", "средний уровень GL90+@12MOB", "dash")],
                insights=ins, terms=["gl", "cohort"])


def a08_vintage_heat(A, B, ctx):
    vm = A["vin_marks"]
    vm = vm[vm.reliable]
    piv = vm.pivot_table(index="metric", columns="vintage", values="rate", aggfunc="mean") * 100
    order = [f"GL{a_}+@{b_}MOB" for a_, b_ in VINTAGE_MARKS]
    piv = piv.reindex([o for o in order if o in piv.index])
    if piv.empty:
        raise ValueError("нет когорт с достаточным числом кредитов")
    z = piv.to_numpy(dtype=float)
    ncol = z.shape[1]
    step = 1 if ncol <= 18 else max(1, math.ceil(ncol / 14))
    keep = _label_idx(ncol, 14 if ncol > 18 else ncol)
    txt = [[f"{z[r, c]:.1f}" if c in keep and np.isfinite(z[r, c]) else ""
            for c in range(ncol)] for r in range(z.shape[0])]
    nice = {o: o.replace("@", " к ").replace("MOB", "-му мес.") for o in order}
    f = go.Figure(go.Heatmap(
        z=z, x=[vlabel(v) for v in piv.columns], y=[nice[o] for o in piv.index], text=txt, texttemplate="%{text}",
        textfont=dict(size=11), xgap=1, ygap=2,
        colorscale=[[0, "#FFFFFF"], [.3, "#F6E3A8"], [.65, COLORS["watch"]], [1, COLORS["npl"]]],
        colorbar=dict(title="%", thickness=12),
        hovertemplate="%{y}<br>выдача %{x}: %{z:.1f}%<extra></extra>"))
    base(f, height=min(CHART_H, 420), xaxis=dict(title="месяц выдачи", tickangle=-45 if ncol > 18 else 0),
         yaxis=dict(autorange="reversed"))
    ins = []
    for o in piv.index:
        s = piv.loc[o].dropna()
        if len(s):
            ins.append(f"{nice[o]}: последняя когорта ({vlabel_full(s.index[-1])}) — <b>{fpct(s.iloc[-1])}</b>, "
                       f"среднее {fpct(s.mean())}.")
    return page(f, what="Четыре контрольные точки качества для каждой когорты выдач. Строка — правило, "
                        "столбец — месяц выдачи, число — % кредитов когорты.",
                legend=[(COLORS["watch"], "GL30+ к 3/6-му мес.", "ранний сигнал: просрочка больше 30 дней", "bar"),
                        (COLORS["npl"], "GL90+ к 9/12-му мес.", "дефолт: просрочка больше 90 дней", "bar"),
                        ("#FFFFFF", "Пустая клетка", f"когорта ещё не дожила или в ней меньше {MIN_COHORT} кредитов", "bar")],
                insights=ins, terms=["gl", "mob"])


def a09_migration(A, B, ctx):
    sel = ctx["sel"]
    tr = A["transitions"]
    per = A["total"]["period"]
    to_default = (tr[(tr.from_b == "B61_90") & tr.to_b.isin(DEFAULT_BUCKETS)]
                  .groupby("period", observed=True)["rate"].sum().reindex(per) * 100)
    cured = (tr[(tr.from_b == "B01_30") & (tr.to_b == "CUR")]
             .groupby("period", observed=True)["rate"].sum().reindex(per) * 100)
    x = _x(per)
    f = go.Figure()
    f.add_bar(x=x, y=to_default, name="61–90 → дефолт", marker_color=COLORS["npl"],
              text=thin(to_default, lambda v: f"{v:.0f}"), textposition="outside", cliponaxis=False,
              textfont=dict(size=11, color=COLORS["npl"]),
              hovertemplate="%{x}<br>%{y:.1f} из 100 кредитов ушли в 90+<extra></extra>")
    f.add_scatter(x=x, y=cured, name="1–30 → норма", mode="lines+markers+text",
                  line=dict(color=COLORS["good"], width=2.6), marker=dict(size=4),
                  text=thin(cured, lambda v: f"{v:.0f}"), textposition="top center",
                  textfont=dict(size=11, color=COLORS["good"]),
                  hovertemplate="%{x}<br>%{y:.1f} из 100 вернулись в норму<extra></extra>")
    base(f, bargap=.3, yaxis=dict(title="кредитов из 100", range=[0, max(_safemax(to_default), _safemax(cured)) * 1.15]))
    p_ = shift_p(sel, 1)   # the transition is recorded on the month it started from
    td = to_default.set_axis(list(per))
    cu = cured.set_axis(list(per))
    ins = [
        (f"Из 100 кредитов, стоявших в {plabel_full(p_)} в корзине 61–90 дней, через месяц "
         f"<b>{td.get(p_):.0f}</b> ушли в дефолт (90+)." if _ok(td.get(p_)) else ""),
        f"В среднем за период: {fnum(td.mean(), 0)} из 100 уходят в дефолт, "
        f"{fnum(cu.mean(), 0)} из 100 из корзины 1–30 возвращаются в норму.",
        "Этот показатель опережает долю NPL примерно на квартал: рост красных столбцов сегодня — "
        "рост NPL через 2–3 месяца.",
    ]
    return page(f, what="Скорость ухода в дефолт: из каждых 100 кредитов корзины — сколько через месяц "
                        "перешли в следующую. Месяц на оси — месяц, из которого кредит переходил.",
                legend=[(COLORS["npl"], "Красный столбец", "из 100 кредитов с просрочкой 61–90 — сколько ушли в 90+", "bar"),
                        (COLORS["good"], "Зелёная линия", "из 100 кредитов с просрочкой 1–30 — сколько вернулись в норму", "line")],
                insights=ins, terms=["migration"])


def a10_currency(A, B, ctx):
    sel = ctx["sel"]
    piv = _piv(A["cur_name"], "exposure")
    piv = piv.div(piv.sum(axis=1), axis=0) * 100
    order = order_at(piv, sel)
    x = _x(piv.index)
    n, step = len(x), max(1, math.ceil(len(x) / MAX_LABELS))
    pal = list(CURRENCY_COLORS.values())
    f = go.Figure()
    for i, c in enumerate(order):
        col = CURRENCY_COLORS.get(c, pal[i % len(pal)])
        v = nan0(piv[c])
        f.add_bar(x=x, y=v, name=c, marker_color=col,
                  text=[f"{z:.1f}" if _ok(z) and z >= 3 and (j % step == 0 or j == n - 1) else ""
                        for j, z in enumerate(v)],
                  textposition="inside", insidetextanchor="middle",
                  textfont=dict(size=11, color=text_on(col)),
                  hovertemplate="%{x}<br>" + c + ": %{y:.2f}%<extra></extra>")
    fx = 100 - piv.get("Сум", pd.Series(0.0, index=piv.index)).fillna(0)
    f.add_scatter(x=x, y=fx, yaxis="y2", mode="lines+markers+text", line=dict(color=COLORS["npl"], width=2.4),
                  marker=dict(size=4), text=thin(fx, lambda v: f"{v:.1f}%"), textposition="top center",
                  textfont=dict(size=11, color=COLORS["npl"]),
                  hovertemplate="%{x}<br>валютная часть: %{y:.2f}%<extra></extra>")
    base(f, barmode="stack", bargap=.25, yaxis=dict(title="% портфеля", range=[0, 100]),
         **split("валютная часть, %", _safemax(fx)))
    return page(f, what="Из каких валют состоит портфель: доли внутри каждого месяца (сумма = 100%). "
                        "Красная линия сверху — вся валютная часть на своей шкале, чтобы были видны изменения.",
                legend=[(CURRENCY_COLORS.get(c, pal[i % len(pal)]), _e(c), "доля валюты в портфеле", "bar")
                        for i, c in enumerate(order)] +
                       [(COLORS["npl"], "Красная линия", "все валюты кроме сума, % (полоса сверху)", "line")],
                insights=[_trend("Валютная часть портфеля", fx, sel),
                          "Суммы в источнике уже в сумах; рост валютной части — валютный риск заёмщиков, "
                          "который возвращается к банку кредитным риском."],
                terms=["stock", "pp"])


def a11_origination(A, B, ctx):
    sel = ctx["sel"]
    piv = _piv(A["department"], "disbursed")
    order = order_at(piv, sel)
    x = _x(piv.index)
    tot = money(piv.sum(axis=1))
    f = go.Figure()
    for dep in order:
        f.add_bar(x=x, y=money(nan0(piv[dep])), name=dname(dep), marker_color=dcolor(dep),
                  hovertemplate="%{x} · " + _e(dname(dep)) + "<br>%{y:,.1f} " + UNIT_NAME + "<extra></extra>")
    f.add_scatter(x=x, y=tot, mode="text", text=thin(tot, famt), textposition="top center",
                  textfont=dict(size=LABEL_SIZE, color=COLORS["ink"]), hoverinfo="skip")
    base(f, barmode="stack", bargap=.25, yaxis=dict(title=UNIT_NAME, range=[0, _safemax(tot) * 1.12]))
    s = piv.sum(axis=1)
    row = piv.loc[sel] if sel in piv.index else None
    ins = [f"Выдано в {plabel_full(sel)}: <b>{fnum(at(s, sel) / UNIT)} {UNIT_NAME}</b> "
           f"(год назад {fnum(at(s, shift_p(sel, 12)) / UNIT)})."]
    if row is not None and row.sum() > 0:
        top = row.idxmax()
        ins.append(f"Больше всего выдал {_e(dname(top))}: {fpct(row[top] / row.sum() * 100)} выдач месяца.")
    ins.append(f"Выдано за весь период: {fnum(s.sum() / UNIT)} {UNIT_NAME}.")
    return page(f, what="Сколько новых кредитов выдал каждый департамент за месяц. Это поток: месяцы "
                        "можно складывать.",
                legend=_dept_legend(order) + [(COLORS["ink"], "Число над столбцом", "всего выдано за месяц", "text")],
                insights=ins, terms=["flow"])


def a12_coverage(A, B, ctx):
    sel = ctx["sel"]
    d = A["total"]
    x = _x(d["period"])
    cov, crt = d.coverage * 100, d.court_share * 100
    f = go.Figure()
    f.add_scatter(x=x, y=cov, name="Покрытие", mode="lines+markers+text",
                  line=dict(color=COLORS["good"], width=3), marker=dict(size=4),
                  text=thin(cov, lambda v: f"{v:.0f}%"), textposition="top center",
                  textfont=dict(size=11, color=COLORS["good"]),
                  hovertemplate="%{x}<br>покрытие %{y:.0f}%<extra></extra>")
    f.add_scatter(x=x, y=crt, name="В суде", yaxis="y2", mode="lines+markers+text",
                  line=dict(color=COLORS["npl"], width=2.2, dash="dot"), marker=dict(size=4),
                  text=thin(crt, lambda v: f"{v:.1f}%"), textposition="bottom center",
                  textfont=dict(size=11, color=COLORS["npl"]),
                  hovertemplate="%{x}<br>в суде %{y:.2f}% портфеля<extra></extra>")
    f.add_hline(y=100, line=dict(color=COLORS["neutral"], width=1, dash="dash"),
                annotation_text="100% — резервы равны NPL", annotation_position="top right",
                annotation_font_size=11)
    base(f, yaxis=dict(title="покрытие, %", range=[0, max(_safemax(cov), 100) * 1.15]),
         yaxis2=dict(overlaying="y", side="right", title="в суде, % портфеля", showgrid=False,
                     **headroom(_safemax(crt), 2.4)))
    s = d.set_index("period")
    ins = [_trend("Покрытие NPL резервами", s["coverage"] * 100, sel, dec=0),
           _trend("Доля портфеля в суде", s["court_share"] * 100, sel),
           ("Покрытие ниже 100%: часть проблемного долга ещё не закрыта резервами."
            if _ok(at(s["coverage"], sel)) and at(s["coverage"], sel) < 1 else "")]
    return page(f, what="Хватает ли резервов на проблемный долг (зелёная линия, левая шкала) и какая "
                        "часть портфеля уже в суде (красный пунктир, правая шкала).",
                legend=[(COLORS["good"], "Зелёная линия", "покрытие = резервы / NPL 90+", "line"),
                        (COLORS["npl"], "Красный пунктир", "доля портфеля с официальной судебной стадией", "dot"),
                        (COLORS["neutral"], "Серый пунктир", "уровень 100%", "dash")],
                insights=ins, terms=["coverage", "court"])


def a13_insurance(A, B, ctx):
    sel = ctx["sel"]
    d = A["total"]
    x = _x(d["period"])
    npl, gross, watch = d.npl_ratio * 100, d.npl_ratio_gross * 100, d.watch_ratio * 100
    f = go.Figure()
    f.add_scatter(x=x, y=gross, name="NPL без страховки", mode="lines",
                  line=dict(color=COLORS["npl"], width=2.6, dash="dash"),
                  hovertemplate="%{x}<br>без страховки: %{y:.2f}%<extra></extra>")
    f.add_scatter(x=x, y=npl, name="NPL фактический", mode="lines+markers+text",
                  line=dict(color=COLORS["npl"], width=3), marker=dict(size=4),
                  fill="tonexty", fillcolor="rgba(242,194,48,.35)",
                  text=thin(npl, lambda v: f"{v:.2f}"), textposition="bottom center",
                  textfont=dict(size=11, color=COLORS["npl"]),
                  hovertemplate="%{x}<br>фактический: %{y:.2f}%<extra></extra>")
    f.add_scatter(x=x, y=watch, name=f"Зона риска {_wz()}", mode="lines",
                  line=dict(color=COLORS["watch"], width=2, dash="dot"),
                  hovertemplate="%{x}<br>зона риска: %{y:.2f}%<extra></extra>")
    base(f, yaxis=dict(title="% портфеля", range=[0, max(_safemax(gross), _safemax(npl), _safemax(watch)) * 1.2]))
    s = d.set_index("period")
    g, n_ = at(s["npl_ratio_gross"] * 100, sel), at(s["npl_ratio"] * 100, sel)
    ins = [(f"На {plabel_full(sel)} страховка снижает NPL с <b>{fpct(g, 2)}</b> до <b>{fpct(n_, 2)}</b> "
            f"({fpp(n_ - g)})." if _ok(g) and _ok(n_) else ""),
           _trend(f"Зона риска {_wz()}", s["watch_ratio"] * 100, sel)]
    return page(f, what="Что страховка удерживает от NPL. Жёлтая заливка между линиями — NPL, который "
                        "был бы на балансе, если бы страховая не платила.",
                legend=[(COLORS["npl"], "Красный пунктир", "NPL без учёта страховых выплат", "dash"),
                        (COLORS["npl"], "Красная линия", "NPL фактический", "line"),
                        ("#F2C230", "Жёлтая заливка", "эффект страховки", "bar"),
                        (COLORS["watch"], "Оранжевый пунктир", f"зона риска {_wz()} дней", "dot")],
                insights=ins, terms=["insurance", "watch"])


def _passport_chart(dep):
    """One stacked chart per department; products fixed and ordered by their standing at SEL."""
    def fn(A, B, ctx):
        sel = ctx["sel"]
        d = A["passport_dep"]
        d = d[d.department == dep]
        if d.empty:
            raise ValueError(f"нет данных по департаменту «{dep}»")
        piv = d.pivot_table(index="period", columns="passport_grp", values="exposure",
                            aggfunc="sum").fillna(0)
        tot_all = piv.sum(axis=1)
        piv = piv[tot_all > 0]                         # a new department starts where it starts
        if piv.empty:
            raise ValueError(f"у департамента «{dep}» нет остатка")
        named = [c for c in order_at(piv, sel) if c != "Прочие"]
        cols = named + (["Прочие"] if "Прочие" in piv.columns else [])
        cmap = dict(zip(named, shades(dcolor(dep), max(len(named), 1))))
        cmap["Прочие"] = COLORS["light"]
        x = _x(piv.index)
        tot = money(piv.sum(axis=1))
        f = go.Figure()
        for c in cols:
            f.add_bar(x=x, y=money(nan0(piv[c])), name=str(c), marker_color=cmap[c],
                      hovertemplate="%{x}<br>" + _e(c) + ": %{y:,.1f} " + UNIT_NAME + "<extra></extra>")
        f.add_scatter(x=x, y=tot, mode="text", text=thin(tot, famt), textposition="top center",
                      textfont=dict(size=LABEL_SIZE, color=COLORS["ink"]), hoverinfo="skip")
        g = d.groupby("period", observed=True)[["npl_exposure", "exposure"]].sum().reindex(piv.index)
        nplr = g.npl_exposure / g.exposure.replace(0, np.nan) * 100
        f.add_scatter(x=x, y=nplr, yaxis="y2", mode="lines+markers+text",
                      line=dict(color=COLORS["npl"], width=2.6), marker=dict(size=4),
                      text=thin(nplr, lambda v: f"{v:.1f}%", max_labels=8), textposition="top center",
                      textfont=dict(size=11, color=COLORS["npl"]),
                      hovertemplate="%{x}<br>NPL департамента %{y:.2f}%<extra></extra>")
        base(f, barmode="stack", bargap=.25, yaxis=dict(title=UNIT_NAME, range=[0, _safemax(tot) * 1.12]),
             **split("NPL, %", _safemax(nplr)))

        row = piv.loc[sel] if sel in piv.index else piv.iloc[-1]
        share = row / row.sum() * 100 if row.sum() else row
        ins = [f"Портфель {_e(dname(dep))} на {plabel_full(sel)}: <b>{fnum(row.sum() / UNIT)} {UNIT_NAME}</b>."]
        if named:
            ins.append(f"Крупнейший продукт — <b>{_e(named[0])}</b>: {fpct(share[named[0]])} портфеля департамента.")
        y1 = shift_p(sel, 12)
        if y1 in piv.index:
            gr = ((piv.loc[sel, named] - piv.loc[y1, named]) / UNIT).dropna() if sel in piv.index else pd.Series(dtype=float)
            if len(gr):
                ins.append(f"Сильнее всего за год вырос «{_e(gr.idxmax())}»: +{fnum(gr.max())} {UNIT_NAME}.")
        ins.append(_trend("NPL департамента", nplr, sel))
        if piv.index[0] != ctx["periods"][0]:
            ins.append(f"Департамент появился в данных с {plabel_full(piv.index[0])} — раньше месяцев нет.")
        leg = [(cmap[c], _e(c), f"{fpct(share.get(c))} на дату", "bar") for c in cols]
        leg.append((COLORS["npl"], "Красная линия", "NPL 90+ департамента, % (полоса сверху)", "line"))
        return page(f, title=f"«{dname(dep)}»: портфель по продуктам",
                    what=f"Остаток портфеля департамента {dname(dep)} по продуктам. Порядок полос — по доле на "
                         f"{plabel_full(sel)}: самый крупный продукт внизу и на том же месте в каждом месяце.",
                    legend=leg, insights=ins, terms=["stock", "npl"])
    return fn


def _series_palette(n):
    pal = [DEPT_COLORS[k] for k in DEPARTMENTS if k in DEPT_COLORS] + EXTRA_COLORS
    return [pal[i % len(pal)] if i < len(pal) else shades(pal[i % len(pal)], 2)[1] for i in range(n)]


def a_oked_dynamics(A, B, ctx):
    sel = ctx["sel"]
    top = list(B["oked_name"].head(TOP_OKED)["name"])
    d = A["oked_name"].copy()
    d["grp"] = np.where(d.dim_value.isin(top), d.dim_value, "Прочие отрасли")
    piv = d.pivot_table(index="period", columns="grp", values="exposure", aggfunc="sum").fillna(0)
    piv = piv.div(piv.sum(axis=1), axis=0) * 100
    named = [c for c in order_at(piv, sel) if c != "Прочие отрасли"]
    cols = named + (["Прочие отрасли"] if "Прочие отрасли" in piv.columns else [])
    cmap = dict(zip(named, _series_palette(len(named))))
    cmap["Прочие отрасли"] = COLORS["light"]
    x = _x(piv.index)
    n, step = len(x), max(1, math.ceil(len(x) / 10))
    f = go.Figure()
    for c in cols:
        v = nan0(piv[c])
        f.add_bar(x=x, y=v, name=str(c), marker_color=cmap[c],
                  text=[f"{z:.0f}" if _ok(z) and z >= 5 and (j % step == 0 or j == n - 1) else ""
                        for j, z in enumerate(v)],
                  textposition="inside", insidetextanchor="middle",
                  textfont=dict(size=10.5, color=text_on(cmap[c])),
                  hovertemplate="%{x}<br>" + _e(c) + ": %{y:.2f}%<extra></extra>")
    base(f, barmode="stack", bargap=.25, yaxis=dict(title="% портфеля", range=[0, 100]))
    row = piv.loc[sel] if sel in piv.index else piv.iloc[-1]
    ins = [f"Крупнейшая отрасль на {plabel_full(sel)} — <b>{_e(named[0])}</b>: {fpct(row[named[0]])}."
           if named else "",
           f"Топ-3 отрасли вместе — {fpct(row[named[:3]].sum())} портфеля." if len(named) >= 3 else ""]
    return page(f, title="Отраслевая структура портфеля (ОКЭД)",
                what=f"Доли отраслей в портфеле по месяцам (сумма = 100%). Топ-{TOP_OKED} отраслей на "
                     f"{plabel_full(sel)}, крупнейшая внизу; остальные — серые «Прочие».",
                legend=[(cmap[c], _e(c), f"{fpct(row.get(c))} на дату", "bar") for c in cols],
                insights=ins, terms=["stock"])


def a_top_clients(A, B, ctx):
    sel = ctx["sel"]
    s = A["top_summary"].set_index("period")
    if s.empty:
        raise ValueError("нет клиентов для рейтинга")
    piv = _piv(A["top_by_dep"], "exposure").reindex(s.index)
    order = order_at(piv, sel)
    x = _x(s.index)
    tot = money(s["exposure"])
    f = go.Figure()
    for dep in order:
        f.add_bar(x=x, y=money(nan0(piv[dep])), name=dname(dep), marker_color=dcolor(dep),
                  hovertemplate="%{x} · " + _e(dname(dep)) + "<br>%{y:,.1f} " + UNIT_NAME + "<extra></extra>")
    f.add_scatter(x=x, y=tot, mode="text", text=thin(tot, famt), textposition="top center",
                  textfont=dict(size=LABEL_SIZE), hoverinfo="skip")
    sh = s["share"] * 100
    f.add_scatter(x=x, y=sh, yaxis="y2", mode="lines+markers+text", line=dict(color=COLORS["npl"], width=2.6),
                  marker=dict(size=4), text=thin(sh, lambda v: f"{v:.1f}%", max_labels=8),
                  textposition="top center", textfont=dict(size=11, color=COLORS["npl"]),
                  hovertemplate="%{x}<br>доля в портфеле банка: %{y:.2f}%<extra></extra>")
    base(f, barmode="stack", bargap=.25, yaxis=dict(title=UNIT_NAME, range=[0, _safemax(tot) * 1.12]),
         **split("% портфеля банка", _safemax(sh)))
    ex = ", ".join(TOP_CLIENTS_EXCLUDE)
    ins = [_trend(f"Доля топ-{TOP_CLIENTS} в портфеле банка", sh, sel),
           (f"Крупнейший клиент — {fpct(at(s['top1_share'] * 100, sel), 2)} портфеля банка."
            if _ok(at(s["top1_share"], sel)) else ""),
           (f"За месяц в топ-{TOP_CLIENTS} вошли <b>{int(at(s['newcomers'], sel))}</b> новых клиентов."
            if _ok(at(s["newcomers"], sel)) else ""),
           f"Клиенты департамента {_e(ex)} не участвуют в рейтинге; их место занимают следующие по размеру."]
    return page(f, title=f"Топ-{TOP_CLIENTS} клиентов по месяцам",
                what=f"Сумма остатка {TOP_CLIENTS} крупнейших клиентов каждого месяца (столбцы, по департаментам) "
                     f"и их доля во всём портфеле банка (красная линия). Состав топ-{TOP_CLIENTS} в каждом "
                     f"месяце свой. Список на дату — на странице B08.",
                legend=_dept_legend(order) + [
                    (COLORS["ink"], "Число над столбцом", f"сумма топ-{TOP_CLIENTS}, {UNIT_NAME}", "text"),
                    (COLORS["npl"], "Красная линия", "их доля во всём портфеле банка, % (полоса сверху)", "line")],
                insights=ins, terms=["top"])


# ---------------------------------------------------------------- B: structure
def _hbar_height(n, per_row=24, minimum=360):
    return int(min(CHART_H, max(minimum, 70 + per_row * n)))


def b01_dep_filial(A, B, ctx):
    sel = ctx["sel"]
    fd = B["filial_dep"]
    fd = fd[~fd["filial"].map(is_no_branch)]
    piv = fd.pivot_table(index="filial", columns="department", values="exposure", aggfunc="sum").fillna(0)
    tot = piv.sum(axis=1).sort_values(ascending=False)
    deps = list(piv.sum().sort_values(ascending=False).index)   # biggest department leftmost
    fil = B["filial"].set_index("name")
    hidden = _branch_hidden_note(B["filial"].assign(dim_value=B["filial"]["name"]))
    bank_tot = B["_tot_exp"]
    ins = [f"Филиалов с остатком: {len(tot)}. Крупнейшие: " +
           "; ".join(f"<b>{_e(b)}</b> {fpct(v / bank_tot * 100)}" for b, v in tot.head(3).items()) + ".",
           f"Топ-5 филиалов вместе — {fpct(tot.head(5).sum() / bank_tot * 100)} портфеля банка.",
           hidden]
    parts = chunks(list(tot.index), BRANCHES_PER_PAGE)
    pages_ = []
    for k, part in enumerate(parts, 1):
        rows = list(reversed(part))             # largest at the top
        f = go.Figure()
        for dep in deps:
            v = money(piv.loc[rows, dep])
            f.add_bar(y=rows, x=nan0(v), orientation="h", name=dname(dep), marker_color=dcolor(dep),
                      hovertemplate="%{y} · " + _e(dname(dep)) + "<br>%{x:,.1f} " + UNIT_NAME + "<extra></extra>")
        lbl = [f"  {fnum(tot[r] / UNIT)} · {fpct(tot[r] / bank_tot * 100)} · NPL {fpct(fil.loc[r, 'npl_ratio'] * 100)}"
               if r in fil.index else "" for r in rows]
        f.add_scatter(y=rows, x=money(tot[rows]), mode="text", text=lbl, textposition="middle right",
                      textfont=dict(size=11), hoverinfo="skip", cliponaxis=False)
        base(f, barmode="stack", height=_hbar_height(len(rows)), margin=dict(r=190),
             xaxis=dict(title=UNIT_NAME), yaxis=dict(tickfont=dict(size=11)))
        sfx = f" ({k}/{len(parts)})" if len(parts) > 1 else ""
        pages_.append(page(
            f, title=f"Портфель по филиалам, {plabel_full(sel)}{sfx}",
            what="Остаток портфеля каждого филиала, разделённый по департаментам. Подпись: сумма · доля "
                 "портфеля банка · NPL 90+ филиала.",
            legend=_dept_legend(deps) + [(COLORS["ink"], "Подпись справа",
                                          f"{UNIT_NAME} · % портфеля банка · NPL филиала", "text")],
            insights=ins if k == 1 else ["Продолжение списка филиалов."] + [hidden],
            terms=["npl"]))
    return pages_


def b02_buckets(A, B, ctx):
    sel = ctx["sel"]
    d = B["bucket"].copy()
    d["ord"] = d["name"].map({b: i for i, b in enumerate(BUCKET_ORDER)})
    d = d.sort_values("ord")
    cur = d[d.name == "CUR"]
    if not SHOW_CURRENT_BUCKET:
        d = d[d.name != "CUR"]
    amt = money(d.exposure)
    f = go.Figure()
    f.add_bar(x=[lab(n) for n in d["name"]], y=amt,
              marker_color=[BUCKET_COLORS.get(n, COLORS["neutral"]) for n in d["name"]],
              text=[f"<b>{fnum(v, 1)}</b><br>{s:.1%}<br>{int(n):,} кред.".replace(",", " ")
                    for v, s, n in zip(amt, d["share"], d["n_loans"])],
              textposition="outside", cliponaxis=False, textfont=dict(size=LABEL_SIZE),
              hovertemplate="<b>%{x}</b><br>%{y:,.2f} " + UNIT_NAME + "<extra></extra>")
    base(f, bargap=.35, yaxis=dict(title=UNIT_NAME, range=[0, _safemax(amt) * 1.3]))
    od = d["share"].sum()
    deep = d[d.name.isin(["B91_180", "B181_365", "B365P"])]
    ins = [f"С просрочкой — <b>{od:.1%}</b> портфеля: {fnum(d.exposure.sum() / UNIT)} {UNIT_NAME}, "
           f"{int(d.n_loans.sum()):,} кредитов.".replace(",", " "),
           (f"Без просрочки — {float(cur['share'].sum()):.1%} портфеля "
            f"({fnum(float(cur['exposure'].sum()) / UNIT)} {UNIT_NAME}); на графике не показан."
            if len(cur) and not SHOW_CURRENT_BUCKET else ""),
           f"Просрочка 90+ дней — {deep['share'].sum():.1%} портфеля; 1–90 дней — "
           f"{d[d.name.isin(['B01_30', 'B31_90'])]['share'].sum():.1%}: это кандидаты в NPL следующих месяцев."]
    return page(f, title=f"Просроченный портфель по корзинам, {plabel_full(sel)}",
                what="Сколько денег стоит в каждой корзине просрочки на дату. Подпись: сумма · доля всего "
                     "портфеля · число кредитов.",
                legend=[(BUCKET_COLORS[b], lab(b), "кредиты с такой просрочкой на дату", "bar")
                        for b in d["name"] if b in BUCKET_COLORS],
                insights=ins, terms=["overdue"])


def b03_vintage_mix(A, B, ctx):
    sel = ctx["sel"]
    d = B["vintage_mix"].dropna(subset=["vintage"]).sort_values("vintage")
    d = d[d.vintage >= int(d.vintage.max()) - 300]
    x = [vlabel(v) for v in d.vintage]
    amt, nplr = money(d.exposure), d.npl_ratio * 100
    f = go.Figure()
    f.add_bar(x=x, y=amt, marker_color=COLORS["neutral"], text=thin(amt, max_labels=10),
              textposition="outside", cliponaxis=False, textfont=dict(size=11),
              customdata=np.stack([d["share"] * 100, d["n_loans"]], axis=-1),
              hovertemplate="выдача %{x}<br>%{y:,.1f} " + UNIT_NAME +
                            "<br>%{customdata[0]:.1f}% портфеля<br>кредитов %{customdata[1]:,}<extra></extra>")
    f.add_scatter(x=x, y=nplr, yaxis="y2", mode="lines+markers+text", line=dict(color=COLORS["npl"], width=2.4),
                  marker=dict(size=4), text=thin(nplr, lambda v: f"{v:.1f}%", max_labels=8),
                  textposition="top center", textfont=dict(size=11, color=COLORS["npl"]),
                  hovertemplate="выдача %{x}<br>NPL когорты %{y:.2f}%<extra></extra>")
    base(f, bargap=.2, xaxis=dict(title="месяц выдачи"), yaxis=dict(title=UNIT_NAME, range=[0, _safemax(amt) * 1.15]),
         **split("NPL когорты, %", _safemax(nplr)))
    recent = d[d.vintage >= shift_p(sel, 11)]
    worst = d.loc[d.npl_ratio.idxmax()] if d.npl_ratio.notna().any() else None
    ins = [f"Выдачи последних 12 месяцев — <b>{fpct(recent.exposure.sum() / B['_tot_exp'] * 100)}</b> портфеля.",
           (f"Самая проблемная когорта — {vlabel_full(worst.vintage)}: NPL {fpct(worst.npl_ratio * 100)}, "
            f"остаток {fnum(worst.exposure / UNIT)} {UNIT_NAME}." if worst is not None else ""),
           "Высокий столбец с высокой красной линией — недавняя крупная выдача, которая уже портится."]
    return page(f, title=f"Из выдач каких месяцев состоит портфель на {plabel_full(sel)}",
                what="Сколько денег из выдач каждого месяца ещё на балансе (столбцы) и насколько плохо ведёт себя "
                     "именно эта когорта (красная линия). Последние три года.",
                legend=[(COLORS["neutral"], "Серый столбец", f"остаток кредитов этого месяца выдачи, {UNIT_NAME}", "bar"),
                        (COLORS["npl"], "Красная линия", "NPL 90+ этой когорты, % (полоса сверху)", "line")],
                insights=ins, terms=["vintage", "npl"])


def b04_mob_profile(A, B, ctx):
    sel = ctx["sel"]
    d = B["mob_band"].copy()
    d["ord"] = d["name"].map({m: i for i, m in enumerate(MOB_LABELS)})
    d = d.sort_values("ord")
    nplr = d.npl_ratio * 100
    f = go.Figure()
    f.add_bar(x=d["name"], y=d["share"] * 100, marker_color=COLORS["neutral"],
              text=[f"<b>{s:.1%}</b><br>{fnum(e / UNIT, 1)} {UNIT_NAME}" for s, e in zip(d["share"], d["exposure"])],
              textposition="outside", cliponaxis=False, textfont=dict(size=LABEL_SIZE),
              hovertemplate="%{x}<br>%{y:.1f}% портфеля<extra></extra>")
    f.add_scatter(x=d["name"], y=nplr, yaxis="y2", mode="lines+markers+text",
                  line=dict(color=COLORS["npl"], width=2.6), marker=dict(size=8),
                  text=[fpct(v, 2) for v in nplr], textposition="top center",
                  textfont=dict(size=LABEL_SIZE, color=COLORS["npl"]))
    base(f, bargap=.35, yaxis=dict(title="% портфеля", range=[0, _safemax(d["share"] * 100) * 1.3]),
         yaxis2=dict(overlaying="y", side="right", title="NPL, %", showgrid=False, **headroom(_safemax(nplr), 1.6)))
    big = d.loc[d["share"].idxmax()] if len(d) else None
    bad = d.loc[d["npl_ratio"].idxmax()] if d["npl_ratio"].notna().any() else None
    ins = [(f"Больше всего денег в кредитах возраста <b>{big['name']}</b>: {big['share']:.1%} портфеля."
            if big is not None else ""),
           (f"Самый высокий NPL — у кредитов возраста {bad['name']}: {fpct(bad['npl_ratio'] * 100, 2)}."
            if bad is not None else ""),
           "Высокий NPL у молодых кредитов — вопрос к правилам выдачи; у старых — накопленное наследство."]
    return page(f, title=f"Возраст кредитов в портфеле, {plabel_full(sel)}",
                what="Как портфель распределён по возрасту кредита — сколько месяцев прошло с выдачи — "
                     "и какое качество у каждой возрастной группы.",
                legend=[(COLORS["neutral"], "Столбец", "доля портфеля в этой возрастной группе", "bar"),
                        (COLORS["npl"], "Красная линия", "NPL 90+ группы, % (правая шкала)", "line")],
                insights=ins, terms=["mob"])


def b05_products(A, B, ctx):
    sel = ctx["sel"]
    pd_ = B["passport_dep"]
    top = B["passport"].head(TOP_PRODUCTS)
    deps_of = (pd_.sort_values("exposure", ascending=False).groupby("passport", observed=True)["department"]
                  .agg(lambda s: list(dict.fromkeys(str(v) for v in s))))
    d = top.sort_values("exposure")
    names = [f"{n} ({', '.join(dname(x) for x in deps_of.get(n, []))})" for n in d["name"]]
    cols = [dcolor(deps_of.get(n, [""])[0]) for n in d["name"]]
    f = go.Figure()
    f.add_bar(x=money(d.exposure), y=names, orientation="h", marker_color=cols,
              text=[f"  {fnum(v / UNIT, 1)} · {sh:.1%} · NPL {fpct(n * 100)}"
                    for v, sh, n in zip(d.exposure, d.share, d.npl_ratio)],
              textposition="outside", cliponaxis=False, textfont=dict(size=11),
              customdata=np.stack([d["n_loans"], d["avg_ticket"] / 1e6], axis=-1),
              hovertemplate="<b>%{y}</b><br>%{x:,.1f} " + UNIT_NAME +
                            "<br>кредитов %{customdata[0]:,}<br>средний чек %{customdata[1]:,.1f} млн<extra></extra>")
    base(f, height=_hbar_height(len(d), 30), margin=dict(r=200), xaxis=dict(title=UNIT_NAME),
         yaxis=dict(tickfont=dict(size=11)))
    t = top.iloc[0] if len(top) else None
    bank_npl = B["_tot_npl"] / B["_tot_exp"] * 100 if B["_tot_exp"] else np.nan
    risky = top[top.npl_ratio * 100 > bank_npl] if _ok(bank_npl) else top.iloc[0:0]
    ins = [(f"Крупнейший продукт — <b>{_e(t['name'])}</b>: {t['share']:.1%} портфеля банка." if t is not None else ""),
           f"Топ-{TOP_PRODUCTS} продуктов — {top['share'].sum():.1%} портфеля.",
           (f"NPL выше банка ({fpct(bank_npl, 2)}) у {len(risky)} из {len(top)}: "
            + _e(", ".join(risky.sort_values("npl_ratio", ascending=False)["name"].head(4))) + "."
            if len(risky) else "")]
    deps = dept_sorted({x for v in deps_of.values for x in v})
    return page(f, title=f"Топ-{TOP_PRODUCTS} продуктов по объёму, {plabel_full(sel)}",
                what="Крупнейшие продукты банка. В скобках — департамент(ы), в которых продукт выдаётся; цвет — "
                     "главный из них. Подпись: сумма · доля портфеля · NPL продукта.",
                legend=_dept_legend(deps) + [(COLORS["ink"], "Подпись справа",
                                              f"{UNIT_NAME} · % портфеля банка · NPL 90+", "text")],
                insights=ins, terms=["npl"])


def b06_passport_dep(A, B, ctx):
    sel = ctx["sel"]
    d = B["passport_dep"].copy()
    deps = dept_sorted(d["department"].dropna().unique())
    rows, cols, names = [], [], []
    for dep in deps:
        g = d[d.department == dep].nlargest(TOP_PASSPORTS, "exposure")
        rows.append(g)
    d = pd.concat(rows) if rows else d.iloc[0:0]
    d["tag"] = d["passport"].astype(str) + "  ·  " + d["department"].map(dname)
    order = list(d["tag"])                         # kk first, largest first inside each department
    f = go.Figure()
    for dep in deps:
        s = d[d.department == dep]
        f.add_bar(x=money(s.exposure), y=s["tag"], orientation="h", name=dname(dep), marker_color=dcolor(dep),
                  text=[f"  {fnum(v / UNIT, 1)} · NPL {fpct(n * 100)}" for v, n in zip(s.exposure, s.npl_ratio)],
                  textposition="outside", cliponaxis=False, textfont=dict(size=10.5),
                  customdata=np.stack([s["n_loans"], s["share"] * 100], axis=-1),
                  hovertemplate="<b>%{y}</b><br>%{x:,.1f} " + UNIT_NAME +
                                "<br>кредитов %{customdata[0]:,}<br>%{customdata[1]:.1f}% портфеля банка<extra></extra>")
    base(f, height=_hbar_height(len(d), 20), margin=dict(r=160), xaxis=dict(title=UNIT_NAME),
         yaxis=dict(categoryorder="array", categoryarray=list(reversed(order)), tickfont=dict(size=10.5)))
    ins = []
    for dep in deps:
        s = d[d.department == dep]
        if len(s):
            r = s.iloc[0]
            ins.append(f"{_e(dname(dep))}: крупнейший продукт — <b>{_e(r.passport)}</b>, "
                       f"{fnum(r.exposure / UNIT)} {UNIT_NAME}, NPL {fpct(r.npl_ratio * 100)}.")
    return page(f, title=f"Топ-{TOP_PASSPORTS} продуктов каждого департамента, {plabel_full(sel)}",
                what="Крупнейшие продукты внутри каждого департамента, в порядке " + ", ".join(dname(x) for x in deps) +
                     ". Подпись: сумма и NPL продукта.",
                legend=_dept_legend(deps), insights=ins, terms=["npl"])


def b07_filial_bucket(A, B, ctx):
    sel = ctx["sel"]
    fb = B["filial_bucket"]
    hidden_v = float(fb[fb["filial"].map(is_no_branch)]["exposure"].sum())
    fb = fb[~fb["filial"].map(is_no_branch)]
    piv = fb.pivot_table(index="filial", columns="bucket", values="share", aggfunc="sum",
                         observed=True).fillna(0) * 100
    cols = _bucket_cols(piv)
    deep = [c for c in cols if c in ("B91_180", "B181_365", "B365P")]
    order = list(piv[deep].sum(axis=1).sort_values(ascending=False).index) if deep else list(piv.index)
    od = piv[cols].sum(axis=1)
    ins = [f"Хуже всего по просрочке 90+: " + "; ".join(
               f"<b>{_e(b)}</b> {fpct(piv.loc[b, deep].sum())}" for b in order[:3]) + "." if deep else "",
           f"Больше всего просрочки в целом — {_e(od.idxmax())}: {fpct(od.max())} портфеля филиала." if len(od) else "",
           (f"Кредиты без филиала (Nodata): {fnum(hidden_v / UNIT)} {UNIT_NAME} — не показаны." if hidden_v > 0 else "")]
    parts = chunks(order, BRANCHES_PER_PAGE)
    pages_ = []
    for k, part in enumerate(parts, 1):
        rows = list(reversed(part))
        f = go.Figure()
        for b in cols:
            v = piv.loc[rows, b]
            f.add_bar(y=rows, x=v, orientation="h", name=lab(b), marker_color=BUCKET_COLORS[b],
                      text=[f"{z:.1f}" if z >= 1.5 else "" for z in v], textposition="inside",
                      insidetextanchor="middle", textfont=dict(size=10.5, color=text_on(BUCKET_COLORS[b])),
                      hovertemplate="%{y}<br>" + lab(b) + ": %{x:.2f}%<extra></extra>")
        lbl = [f"  {fpct(od[r])}" for r in rows]
        f.add_scatter(y=rows, x=od[rows], mode="text", text=lbl, textposition="middle right",
                      textfont=dict(size=11), hoverinfo="skip", cliponaxis=False)
        base(f, barmode="stack", height=_hbar_height(len(rows)), margin=dict(r=70),
             xaxis=dict(title="% портфеля филиала", range=[0, _safemax(od) * 1.12]),
             yaxis=dict(tickfont=dict(size=11)))
        sfx = f" ({k}/{len(parts)})" if len(parts) > 1 else ""
        pages_.append(page(
            f, title=f"Структура просрочки внутри каждого филиала, {plabel_full(sel)}{sfx}",
            what="Какая часть портфеля филиала просрочена и насколько глубоко. Доли от портфеля своего "
                 "филиала, поэтому большие и маленькие филиалы сравнимы. Сортировка — по просрочке 90+: худшие сверху.",
            legend=[(BUCKET_COLORS[b], lab(b), "% портфеля филиала с такой просрочкой", "bar") for b in cols] +
                   [(COLORS["ink"], "Число справа", "вся просрочка филиала, %", "text")],
            insights=ins if k == 1 else ["Продолжение списка филиалов."] + ins[-1:],
            terms=["overdue"]))
    return pages_


def b08_top_table(A, B, ctx):
    sel = ctx["sel"]
    g = A["clients_ranked"]
    top = A["top"]
    t = top[top["period"] == sel].sort_values("rank")
    if t.empty:
        raise ValueError("нет клиентов на дату")
    prev = g[g["period"] == shift_p(sel, 1)].set_index("contragent")["rank"]
    bank = B["_tot_exp"]
    t = t.assign(share=t["exposure"] / bank * 100)
    t["cum"] = t["share"].cumsum()

    def move(r):
        p_ = prev.get(r.contragent)
        if p_ is None or not _ok(p_):
            return '<span class="mv new">новый</span>'
        dlt = int(p_) - int(r["rank"])
        if dlt > 0:
            return f'<span class="mv up">▲{dlt}</span>'
        if dlt < 0:
            return f'<span class="mv dn">▼{-dlt}</span>'
        return '<span class="mv">—</span>'

    def table(rows):
        body = "".join(
            f"<tr><td class='n'>{int(r['rank'])}</td><td>{move(r)}</td>"
            f"<td class='nm'>{_e(r['name'] if pd.notna(r['name']) else r.contragent)}</td>"
            f"<td>{_e(', '.join(dname(x.strip()) for x in str(r.deps).split(',')))}</td>"
            f"<td class='n'>{fnum(r.exposure / UNIT, 2)}</td><td class='n'>{fpct(r.share, 2)}</td>"
            f"<td class='n'>{fpct(r.cum, 1)}</td>"
            f"<td class='n{' bad' if r.dpd > 90 else (' warn' if r.dpd > 0 else '')}'>{int(r.dpd)}</td></tr>"
            for _, r in rows.iterrows())
        return ("<table class='tt'><thead><tr><th>#</th><th>Δ</th><th>Клиент</th><th>Деп.</th>"
                f"<th>{UNIT_NAME}</th><th>% банка</th><th>накоп.</th><th>дн.</th></tr></thead>"
                f"<tbody>{body}</tbody></table>")

    half = math.ceil(len(t) / 2)
    html_ = f"<div class='tt2'>{table(t.iloc[:half])}{table(t.iloc[half:])}</div>"
    newc = sum(1 for _, r in t.iterrows() if prev.get(r.contragent) is None)
    late = t[t.dpd > 0]
    ins = [f"Топ-{len(t)} держат <b>{fpct(t['share'].sum(), 1)}</b> портфеля банка; топ-10 — {fpct(t['share'].head(10).sum(), 1)}.",
           f"Новых в списке по сравнению с {plabel_full(shift_p(sel, 1))}: {newc}.",
           (f"С просрочкой на дату: {len(late)} клиентов ({fnum(late.exposure.sum() / UNIT, 2)} {UNIT_NAME})."
            if len(late) else "Ни у одного клиента из списка нет просрочки на дату."),
           f"Департамент {_e(', '.join(TOP_CLIENTS_EXCLUDE))} не участвует в рейтинге."]
    return page(None, title=f"Топ-{TOP_CLIENTS} клиентов на {plabel_full(sel)}",
                what=f"Крупнейшие клиенты по сумме остатка. Δ — изменение места по сравнению с прошлым месяцем; "
                     f"«накоп.» — доля портфеля банка у клиентов с 1-го по этот; «дн.» — максимальная просрочка, дней.",
                legend=[(COLORS["good"], "▲ / ▼", "клиент поднялся / опустился в рейтинге", "text"),
                        ("#4F7CAC", "новый", "в прошлом месяце не был в топе", "text"),
                        (COLORS["npl"], "Красное число дней", "просрочка больше 90 дней", "text")],
                insights=ins, terms=["top"], body_html=html_)


def b09_npl_contribution(A, B, ctx):
    sel = ctx["sel"]
    allf = B["filial"]
    d = allf[~allf["name"].map(is_no_branch)].sort_values("npl_exposure", ascending=False).head(12).iloc[::-1]
    f = go.Figure()
    f.add_bar(x=d.npl_contrib * 100, y=d["name"], orientation="h", marker_color=COLORS["npl"],
              text=[f"  {fpct(v)} · {fnum(e / UNIT, 1)} {UNIT_NAME} · свой NPL {fpct(r)}"
                    for v, e, r in zip(d.npl_contrib * 100, d.npl_exposure, d.npl_ratio * 100)],
              textposition="outside", cliponaxis=False, textfont=dict(size=11),
              hovertemplate="<b>%{y}</b><br>вклад в NPL банка: %{x:.1f}%<extra></extra>")
    base(f, height=_hbar_height(len(d), 34), margin=dict(r=260), xaxis=dict(title="% от всего NPL банка"))
    top3 = float(d.tail(3).npl_contrib.sum())
    nod = allf[allf["name"].map(is_no_branch)]
    ins = [f"Три филиала дают <b>{top3:.0%}</b> всего NPL банка: " + _e(", ".join(d.tail(3)["name"][::-1])) + ".",
           f"Всего NPL банка на дату: {fnum(B['_tot_npl'] / UNIT, 1)} {UNIT_NAME}.",
           (f"NPL кредитов без филиала (Nodata): {fnum(nod.npl_exposure.sum() / UNIT, 2)} {UNIT_NAME} — не показан."
            if len(nod) and nod.npl_exposure.sum() > 0 else ""),
           "Это не «худшее качество»: крупный филиал со средним NPL весит больше маленького с плохим."]
    return page(f, title=f"Кто формирует общий NPL банка, {plabel_full(sel)}",
                what="Какая доля всего NPL банка лежит в каждом филиале (12 крупнейших). Подпись: доля · сумма · "
                     "NPL внутри самого филиала.",
                legend=[(COLORS["npl"], "Красный столбец", "доля филиала во всём NPL банка", "bar")],
                insights=ins, terms=["npl"])


def b10_auto_court(A, B, ctx):
    sel = ctx["sel"]
    c = B["court"]
    dep = B["court_dep_name"]
    if c.empty:
        raise ValueError(f"нет кредитов департамента «{COURT_DEPARTMENT}» на дату")
    seg = {"pervichka": "Первичка<br>(новые авто)", "vtorichka": "Вторичка<br>(с пробегом)",
           "non_auto": "Прочие<br>(не авто)"}
    piv = c.pivot_table(index="avto", columns="sud", values="exposure", aggfunc="sum").fillna(0)
    piv = piv.reindex([k for k in seg if k in piv.index])
    piv.loc["all"] = piv.sum()
    stages = [s for s in SUD_ORDER if s in piv.columns] + [s for s in piv.columns if s not in SUD_ORDER]
    xs = [seg.get(k, f"Все кредиты<br>{_e(dname(dep))}") for k in piv.index]
    totals = piv.sum(axis=1)
    f = go.Figure()
    for s in stages:
        v = money(piv[s])
        sh = piv[s] / totals.replace(0, np.nan) * 100
        f.add_bar(x=xs, y=v, name=lab(s), marker_color=SUD_COLORS.get(s, COLORS["neutral"]),
                  text=[f"{fnum(a, 1)} · {fpct(p)}" if _ok(p) and p >= 6 else "" for a, p in zip(v, sh)],
                  textposition="inside", insidetextanchor="middle",
                  textfont=dict(size=11, color=text_on(SUD_COLORS.get(s, COLORS["neutral"]))),
                  customdata=sh, hovertemplate="%{x}<br>" + lab(s) + ": %{y:,.2f} " + UNIT_NAME +
                                              " (%{customdata:.1f}%)<extra></extra>")
    for i, k in enumerate(piv.index):
        tot = totals[k]
        parts = [f"{lab(s).split(' (')[0]}: {fpct(piv.loc[k, s] / tot * 100)}" for s in stages
                 if s != "norm" and tot]
        f.add_annotation(x=xs[i], y=money(tot), yshift=10, showarrow=False, yanchor="bottom",
                         text=f"<b>{fnum(tot / UNIT, 1)}</b><br>" + "<br>".join(parts),
                         font=dict(size=11))
    base(f, barmode="stack", bargap=.35, yaxis=dict(title=UNIT_NAME, range=[0, _safemax(money(totals)) * 1.3]))
    a_ = piv.loc["all"]
    tot_all = a_.sum()
    rate = {k: (piv.loc[k].drop("norm", errors="ignore").sum() / totals[k] * 100 if totals[k] else np.nan)
            for k in piv.index if k != "all"}
    worst = max(rate, key=lambda k: rate[k] if _ok(rate[k]) else -1) if rate else None
    ins = [f"Весь портфель {_e(dname(dep))}: {fnum(tot_all / UNIT)} {UNIT_NAME}; в судебной работе "
           f"(официальная + неофициальная) — <b>{fpct(a_.drop('norm', errors='ignore').sum() / tot_all * 100)}</b>."
           if tot_all else "",
           (f"Чаще всего до суда доходит сегмент «{seg[worst].split('<br>')[0]}»: "
            f"{fpct(rate[worst])} его портфеля." if worst else ""),
           (f"Официально в суде: {fnum(a_.get('official', 0) / UNIT, 2)} {UNIT_NAME}, неофициально: "
            f"{fnum(a_.get('neofficial', 0) / UNIT, 2)} {UNIT_NAME}.")]
    return page(f, title=f"Автокредиты и судебная стадия, департамент {dname(dep)}, {plabel_full(sel)}",
                what=f"Портфель департамента {dname(dep)}: автокредиты на первичном и вторичном рынке, остальные "
                     "кредиты и все вместе. Каждый столбец разделён по судебной стадии. Над столбцом — сумма и "
                     "доли судебных стадий.",
                legend=[(SUD_COLORS.get(s, COLORS["neutral"]), lab(s), {
                    "norm": "кредит обслуживается без судебной работы",
                    "neofficial": "досудебная работа с должником",
                    "official": "иск подан в суд"}.get(s, "стадия из данных"), "bar") for s in stages],
                insights=ins, terms=["court"])


def b11_client_profile(A, B, ctx):
    sel = ctx["sel"]
    d = B["burden"].copy()
    labels = [f"{t} кредит" + ("" if str(t) == "1" else "а" if str(t) in "234" else "ов") for t in d["burden"].astype(str)]
    avg = d["avg_exposure"] / 1e6
    f = go.Figure()
    f.add_bar(x=labels, y=avg, marker_color=COLORS["neutral"], text=[f"<b>{fnum(v, 1)} млн</b>" for v in avg],
              textposition="outside", cliponaxis=False, textfont=dict(size=LABEL_SIZE),
              hovertemplate="%{x}<br>средний долг %{y:,.1f} млн сум<extra></extra>")
    f.add_scatter(x=labels, y=d["client_share"] * 100, yaxis="y2", mode="lines+markers+text",
                  line=dict(color="#4F7CAC", width=2.4), marker=dict(size=9),
                  text=[f"{v:.1%}" for v in d["client_share"]], textposition="top center",
                  textfont=dict(size=LABEL_SIZE, color="#4F7CAC"))
    f.add_scatter(x=labels, y=d["exposure_share"] * 100, yaxis="y2", mode="lines+markers+text",
                  line=dict(color=COLORS["npl"], width=2.4), marker=dict(size=9),
                  text=[f"{v:.1%}" for v in d["exposure_share"]], textposition="bottom center",
                  textfont=dict(size=LABEL_SIZE, color=COLORS["npl"]))
    for i, r in enumerate(d.itertuples()):
        f.add_annotation(x=labels[i], y=0, yshift=-40, showarrow=False,
                         text=f"{int(r.n_clients):,} клиентов".replace(",", " "),
                         font=dict(size=11, color=COLORS["neutral"]))
    base(f, bargap=.4, margin=dict(b=80), yaxis=dict(title="средний долг клиента, млн сум",
                                                    range=[0, _safemax(avg) * 1.25]),
         yaxis2=dict(overlaying="y", side="right", title="%", showgrid=False, range=[0, 100]))
    multi = d[d["burden"].astype(str) != "1"]
    return page(f, title=f"Портрет клиента по числу кредитов, {plabel_full(sel)}",
                what="Клиенты сгруппированы по тому, сколько у них кредитов: средний долг одного клиента "
                     "(столбцы), доля клиентов и доля портфеля (линии, правая шкала).",
                legend=[(COLORS["neutral"], "Столбец", "средний долг одного клиента группы, млн сум", "bar"),
                        ("#4F7CAC", "Синяя линия", "доля всех клиентов в группе", "line"),
                        (COLORS["npl"], "Красная линия", "доля портфеля в группе", "line")],
                insights=[f"Клиенты с несколькими кредитами — {multi.client_share.sum():.1%} клиентов, но "
                          f"<b>{multi.exposure_share.sum():.1%}</b> портфеля.",
                          "Чем дальше красная линия от синей, тем сильнее кредитная нагрузка на одного клиента."],
                terms=[])


def b12_oked(A, B, ctx):
    sel = ctx["sel"]
    d = B["oked_name"].head(TOP_OKED).sort_values("exposure")
    bank_npl = B["_tot_npl"] / B["_tot_exp"] * 100 if B["_tot_exp"] else np.nan
    cols = [COLORS["npl"] if _ok(v) and v * 100 > bank_npl else COLORS["neutral"] for v in d.npl_ratio]
    f = go.Figure()
    f.add_bar(x=money(d.exposure), y=d["name"], orientation="h", marker_color=cols,
              text=[f"  {fnum(v / UNIT, 1)} · {sh:.1%} · NPL {fpct(n * 100)}"
                    for v, sh, n in zip(d.exposure, d.share, d.npl_ratio)],
              textposition="outside", cliponaxis=False, textfont=dict(size=11),
              customdata=np.stack([d["n_loans"], d["n_clients"]], axis=-1),
              hovertemplate="<b>%{y}</b><br>%{x:,.1f} " + UNIT_NAME +
                            "<br>кредитов %{customdata[0]:,}<br>клиентов %{customdata[1]:,}<extra></extra>")
    base(f, height=_hbar_height(len(d), 36), margin=dict(r=200), xaxis=dict(title=UNIT_NAME))
    top3 = float(d.tail(3)["share"].sum())
    return page(f, title=f"Топ-{TOP_OKED} отраслей по объёму (ОКЭД), {plabel_full(sel)}",
                what="Крупнейшие отрасли заёмщиков. Подпись: сумма · доля портфеля · NPL отрасли.",
                legend=[(COLORS["neutral"], "Серый", f"NPL отрасли не выше банка ({fpct(bank_npl, 2)})", "bar"),
                        (COLORS["npl"], "Красный", "NPL отрасли выше, чем у банка", "bar")],
                insights=[f"Три крупнейшие отрасли — <b>{top3:.0%}</b> портфеля.",
                          "Отрасль падает целиком и сразу во всех филиалах — поэтому отраслевая концентрация "
                          "опаснее филиальной."],
                terms=["npl"])


# ---------------------------------------------------------------- registry
CHARTS_A_BASE = [
    ("A01", "СТОК", "Портфель и качество по отчётным датам", a01_portfolio),
    ("A02", "ПОТОК", "Выдачи и погашения за месяц", a02_stock_flow),
    ("A03", "СТОК", "Структура просрочки по месяцам", a03_bucket_mix),
    ("A04", "СТОК", "Доля NPL 90+ по департаментам", a04_npl_departments),
    ("A05", "СТОК", "Доля NPL 90+ по филиалам и месяцам", a05_branch_heatmap),
    ("A06", "ПОТОК", "Почему изменился NPL", a06_bridge),
    ("A07", "КОГОРТЫ", "Качество выдач по месяцу выдачи", a07_vintage_quality),
    ("A08", "КОГОРТЫ", "Контрольные точки качества выдач", a08_vintage_heat),
    ("A09", "ПОТОК", "Скорость ухода в дефолт", a09_migration),
    ("A10", "СТОК", "Доля валют в портфеле", a10_currency),
    ("A11", "ПОТОК", "Выдачи за месяц по департаментам", a11_origination),
    ("A12", "СТОК", "Покрытие резервами и судебная работа", a12_coverage),
    ("A13", "СТОК", "Эффект страхового покрытия", a13_insurance),
]

CHARTS_B_BASE = [
    ("B01", "СРЕЗ", "Портфель по филиалам и департаментам", b01_dep_filial),
    ("B02", "СРЕЗ", "Просроченный портфель по корзинам", b02_buckets),
    ("B03", "СРЕЗ", "Из выдач каких месяцев состоит портфель", b03_vintage_mix),
    ("B04", "СРЕЗ", "Возраст кредитов в портфеле", b04_mob_profile),
    ("B05", "СРЕЗ", "Топ продуктов по объёму", b05_products),
    ("B06", "СРЕЗ", "Продукты по департаментам", b06_passport_dep),
    ("B07", "СРЕЗ", "Структура просрочки внутри филиала", b07_filial_bucket),
    ("B08", "ТАБЛИЦА", "Топ клиентов на дату", b08_top_table),
    ("B09", "СРЕЗ", "Кто формирует общий NPL банка", b09_npl_contribution),
    ("B10", "СРЕЗ", "Автокредиты и судебная стадия", b10_auto_court),
    ("B11", "СРЕЗ", "Портрет клиента по числу кредитов", b11_client_profile),
]


def chart_registry(ctx):
    """
    Build the chart list for this run. Per-department charts can only be known
    once we have seen the data, so the list is assembled here rather than at
    import time. Fixed charts keep their numbers; the data-driven ones follow.
    """
    a = list(CHARTS_A_BASE)
    for dep in ctx.get("departments", []):
        a.append((f"A{len(a) + 1:02d}", "СТОК", f"«{dname(dep)}»: портфель по продуктам", _passport_chart(dep)))
    if ctx.get("has_oked"):
        a.append((f"A{len(a) + 1:02d}", "СТОК", "Отраслевая структура портфеля (ОКЭД)", a_oked_dynamics))
    a.append((f"A{len(a) + 1:02d}", "СТОК", f"Топ-{TOP_CLIENTS} клиентов по месяцам", a_top_clients))

    b = list(CHARTS_B_BASE)
    if ctx.get("has_oked"):
        b.append(("B12", "СРЕЗ", "Отраслевая концентрация (ОКЭД)", b12_oked))
    return a, b


# ==========================================================================
# HTML — the album: A4 landscape pages, one chart per page
# ==========================================================================
CSS = """
:root{--ink:#1A1A1E;--soft:#3A3A40;--gold:#F2C230;--gd:#C9971A;--rule:#E4E1D8;
--muted:#8A867C;--bad:#B3341F;--good:#2F6B4F;--paper:#fff;--desk:#E9E6DF}
*{box-sizing:border-box}
html,body{margin:0;background:var(--desk);color:var(--ink);
font-family:"Segoe UI",Roboto,Arial,sans-serif;font-size:13px;line-height:1.45}
.page{width:297mm;height:210mm;margin:14px auto;background:var(--paper);position:relative;
box-shadow:0 2px 14px rgba(0,0,0,.12);padding:9mm 10mm 0;display:flex;flex-direction:column;overflow:hidden}
.ph{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;
border-bottom:2px solid var(--ink);padding-bottom:6px}
.ph-l{display:flex;align-items:baseline;gap:12px;min-width:0}
.cid{font-size:12px;font-weight:700;letter-spacing:.08em;color:#fff;background:var(--ink);
padding:3px 8px;border-radius:3px;white-space:nowrap}
.ph h2{margin:0;font-size:20px;font-weight:600;line-height:1.2}
.ph-r{display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end;font-size:11px;white-space:nowrap}
.chip{border:1px solid var(--rule);border-radius:20px;padding:2px 9px;color:var(--soft)}
.chip.k{border-color:var(--gd);color:var(--gd);font-weight:600}
.pb{flex:1;display:flex;gap:14px;padding-top:8px;min-height:0}
.pc{flex:0 0 auto;width:""" + str(CHART_W) + """px}
.pa{flex:1;min-width:0;border-left:1px solid var(--rule);padding-left:13px;overflow:hidden;font-size:12px}
.pa h4{margin:8px 0 4px;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--gd)}
.pa h4:first-child{margin-top:0}
.pa p{margin:0 0 4px}
.lg,.ins{list-style:none;margin:0;padding:0}
.lg li{display:flex;gap:7px;align-items:flex-start;margin:0 0 4px}
.lg b{font-weight:600}
.sw{flex:0 0 22px;height:12px;margin-top:3px;border-radius:2px;display:inline-block}
.sw.bar{border:1px solid rgba(0,0,0,.15)}
.sw.line{height:4px;margin-top:7px}
.sw.dash{height:0;margin-top:8px;border-top:3px dashed}
.sw.dot{height:0;margin-top:8px;border-top:3px dotted}
.sw.text{height:auto;margin-top:0;font-size:10px;font-weight:700;text-align:center}
.ins li{position:relative;padding-left:14px;margin:0 0 5px}
.ins li:before{content:"";position:absolute;left:0;top:7px;width:6px;height:6px;background:var(--gold);border-radius:50%}
.ins b{font-weight:700}
.terms{margin:0}.terms div{margin:0 0 4px}.terms dt{display:inline;font-weight:700}
.terms dd{display:inline;margin:0;color:var(--soft)}
.pf{display:flex;justify-content:space-between;font-size:10px;color:var(--muted);
border-top:1px solid var(--rule);padding:4px 0 5mm;margin-top:auto}
.err{color:var(--bad);padding:30px;border:1px dashed var(--bad)}
/* cover */
.cover{background:var(--ink);color:#fff}
.cover .pf{color:#8E8A80;border-color:#333}
.eyebrow{font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);margin-top:6mm}
.cover h1{font-weight:400;font-size:40px;margin:8px 0 4px}
.meta{color:#B9B5AB;font-size:13px}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:#33333A;margin-top:8mm;
border-top:2px solid var(--gold)}
.kpi{background:var(--ink);padding:13px 14px;position:relative;cursor:help}
.kpi .k{font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:#A8A397}
.kpi .k:after{content:" ⓘ";color:var(--gold)}
.kpi .v{font-size:27px;margin-top:5px}
.kpi .d{font-size:12px;margin-top:2px}
.kpi .s{font-size:11px;color:#8E8A80;margin-top:5px;line-height:1.35}
.up{color:#E6A6A6}.dn{color:#9FD3B6}.flat{color:#A8A397}
.tip{display:none;position:absolute;left:8px;right:8px;top:100%;z-index:5;background:#fff;color:var(--ink);
border-radius:6px;padding:10px 12px;font-size:12px;box-shadow:0 6px 24px rgba(0,0,0,.35);line-height:1.45}
.tip b{display:block;margin-bottom:3px}
.kpi:hover .tip{display:block}
.headline{margin-top:7mm;font-size:14px;color:#E8E5DD}
.headline ul{margin:0;padding-left:18px;display:grid;grid-template-columns:1fr 1fr;gap:4px 34px}
.headline h3{column-span:all;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);
font-weight:600;margin:0 0 8px}
.headline li{margin:0 0 6px;break-inside:avoid}
.headline b{color:#fff}
/* contents & legend pages */
.toc{columns:2;column-gap:30px;margin-top:8px}
.toc h3{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gd);margin:6px 0 6px}
.toc a{display:flex;gap:10px;color:var(--ink);text-decoration:none;padding:3px 0;border-bottom:1px dotted var(--rule);
break-inside:avoid;font-size:12.5px}
.toc a .n{font-weight:700;width:36px}.toc a .p{margin-left:auto;color:var(--muted)}
.key{display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px;margin-top:10px}
.key h3{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gd);margin:0 0 8px}
.gl{columns:2;column-gap:26px;margin-top:8px;font-size:12px}
.gl div{break-inside:avoid;margin:0 0 7px}.gl dt{font-weight:700;display:inline}.gl dd{display:inline;margin:0}
/* top table */
.tt2{display:flex;gap:12px;width:""" + str(CHART_W) + """px}
.tt{border-collapse:collapse;font-size:10.5px;width:50%}
.tt th{background:var(--ink);color:#fff;font-weight:600;padding:3px 4px;text-align:left;font-size:10px}
.tt td{padding:2px 4px;border-bottom:1px solid var(--rule);white-space:nowrap}
.tt td.nm{white-space:normal;max-width:120px;overflow:hidden;text-overflow:ellipsis}
.tt td.n{text-align:right;font-variant-numeric:tabular-nums}
.tt td.bad{color:var(--bad);font-weight:700}.tt td.warn{color:#B86E0A}
.mv{font-size:10px;color:var(--muted)}.mv.up{color:var(--good)}.mv.dn{color:var(--bad)}
.mv.new{color:#4F7CAC;font-weight:600}
@page{size:A4 landscape;margin:0}
@media print{html,body{background:#fff}
.page{margin:0;box-shadow:none;break-after:page;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page:last-child{break-after:auto}.tip{display:none!important}
.cover{background:#fff;color:var(--ink)}.cover .meta,.kpi .k,.kpi .s{color:#5E5A52}
.kpis{background:var(--rule)}.kpi{background:#fff}.headline{color:var(--ink)}.headline b{color:var(--ink)}
.up{color:var(--bad)}.dn{color:var(--good)}.flat{color:var(--muted)}}
@media screen and (max-width:1150px){body{overflow-x:auto}}
"""


def _kpis(A, B, sel):
    T = _total(A)
    bm = A["bucket_mix"]
    od = (bm[bm["bucket"] != "CUR"].groupby("period", observed=True)["share"].sum())
    od.index = od.index.astype(int)
    a, b = WATCH_DPD

    def row(key, label, series, kind, dec, short, tip, bad_up=True):
        now, m1, y1 = at(series, sel), at(series, shift_p(sel, 1)), at(series, shift_p(sel, 12))
        if kind == "pct":
            val = fpct(now * 100, dec)
            dm = fpp((now - m1) * 100, 2) if _ok(m1) else ""
            dy = fpp((now - y1) * 100, 2) if _ok(y1) else ""
        elif kind == "money":
            val = fnum(now / UNIT, 1)
            dm, dy = (fchg(now, m1) if _ok(m1) else ""), (fchg(now, y1) if _ok(y1) else "")
        else:
            val = fnum(now, dec)
            dm, dy = (fchg(now, m1) if _ok(m1) else ""), (fchg(now, y1) if _ok(y1) else "")
        def worse(old):
            return None if not (_ok(now) and _ok(old)) or now == old else (now > old) == bad_up
        return {"key": key, "label": label, "value": val, "dm": dm, "dy": dy,
                "wm": worse(m1), "wy": worse(y1),
                "short": short, "tip": tip}

    ncl = T["n_clients"]
    lpc = T["n_loans"] / T["n_clients"].replace(0, np.nan)
    return [
        row("exp", f"Портфель, {UNIT_NAME}", T["exposure"], "money", 1,
            "остаток всех кредитов на дату",
            "<b>Кредитный портфель</b>Сумма основного долга (brutto_95) всех кредитов на отчётную дату. "
            "Это снимок: портфели разных месяцев не складываются. Под значением — изменение за месяц и за год.",
            bad_up=False),
        row("npl", "Доля NPL 90+", T["npl_ratio"], "pct", 2,
            "проблемные кредиты, % портфеля",
            "<b>NPL 90+</b>Кредиты в категориях качества 3–5 — как правило, просрочка больше 90 дней. "
            "Доля = сумма NPL / весь портфель. Рост — плохо (красным). Изменение в п.п.: 3.2% → 3.5% = +0.30 п.п."),
        row("watch", f"Зона риска {a}–{b}", T["watch_ratio"], "pct", 2,
            f"просрочка {a}–{b} дней, ещё не NPL",
            f"<b>Зона риска</b>Кредиты с просрочкой {a}–{b} дней, которые ещё не стали NPL. Это ранний сигнал: "
            "через месяц часть из них перейдёт в NPL. Растёт зона риска сегодня — растёт NPL завтра."),
        row("od", "Просрочка 1+ дней", od, "pct", 2,
            "любая просрочка, % портфеля",
            "<b>Вся просрочка</b>Доля портфеля с просрочкой хотя бы 1 день на отчётную дату — от «чуть опоздал» "
            "до безнадёжных. Включает и NPL, и зону риска."),
        row("cov", "Покрытие резервами", T["coverage"], "pct", 0,
            "резервы / NPL 90+",
            "<b>Покрытие</b>Сколько резервов создано на каждый сум проблемного долга: резервы / NPL 90+. "
            "100% — резервы равны NPL; ниже 100% — часть потерь ещё не признана. Падение — плохо.",
            bad_up=False),
        row("court", "Портфель в суде", T["court_share"], "pct", 2,
            "официальная судебная стадия",
            "<b>В суде</b>Доля портфеля, по которой подан иск (sud = official). Не включает досудебную работу."),
        row("cl", "Клиентов", ncl, "num", 0,
            "уникальных заёмщиков на дату",
            "<b>Клиенты</b>Число уникальных заёмщиков (contragent) с кредитом на отчётную дату.",
            bad_up=False),
        row("lpc", "Кредитов на клиента", lpc, "num", 2,
            "среднее число кредитов у заёмщика",
            "<b>Кредитная нагрузка</b>Сколько кредитов в среднем у одного клиента. Рост означает, что клиенты "
            "берут новые кредиты, не закрыв старые."),
    ]


def _headline(kpis, sel):
    by = {k["key"]: k for k in kpis}
    out = []
    e = by["exp"]
    out.append(f"Портфель на {plabel_full(sel)} — <b>{e['value']} {UNIT_NAME}</b>"
               + (f": за месяц {e['dm']}, за год {e['dy']}." if e["dm"] else "."))
    n = by["npl"]
    out.append(f"Доля NPL 90+ — <b>{n['value']}</b>" + (f" ({n['dm']} за месяц, {n['dy']} за год)." if n["dm"] else "."))
    w = by["watch"]
    out.append(f"В зоне риска — <b>{w['value']}</b> портфеля" + (f" ({w['dm']} за месяц)." if w["dm"] else "."))
    c = by["cov"]
    out.append(f"Покрытие NPL резервами — <b>{c['value']}</b>" + (f" ({c['dm']} за месяц)." if c["dm"] else "."))
    return out


def _legend_html(items):
    out = []
    for col, name, meaning, shape in items:
        if shape == "text":
            sw = f'<i class="sw text" style="color:{col}">123</i>'
        elif shape in ("dash", "dot"):
            sw = f'<i class="sw {shape}" style="border-color:{col}"></i>'
        else:
            sw = f'<i class="sw {shape}" style="background:{col}"></i>'
        out.append(f"<li>{sw}<span><b>{name}</b> — {_e(meaning)}</span></li>")
    return "<ul class='lg'>" + "".join(out) + "</ul>"


def _page_html(pg, cid, kind, section, unit, footer, pno, plotly_first):
    G = glossary()
    head = (f"<header class='ph'><div class='ph-l'><span class='cid'>{cid}</span>"
            f"<h2>{_e(pg['title'])}</h2></div><div class='ph-r'><span class='chip'>{_e(section)}</span>"
            f"<span class='chip k'>{_e(KINDS.get(kind, kind))}</span>"
            + (f"<span class='chip'>{_e(unit)}</span>" if unit else "") + "</div></header>")
    if pg.get("error"):
        body = f"<div class='err'>График не построен: {_e(pg['error'])}</div>"
    elif pg.get("body_html"):
        body = pg["body_html"]
    else:
        body = pg["fig"].to_html(full_html=False, include_plotlyjs=False, config=PCFG,
                                 default_width=f"{CHART_W}px", default_height=f"{pg['fig'].layout.height or CHART_H}px")
    terms = "".join(f"<div><dt>{_e(G[t][0])}</dt> <dd>— {_e(G[t][1])}</dd></div>"
                    for t in pg.get("terms", []) if t in G)
    aside = (f"<h4>Что показано</h4><p>{_e(pg.get('what', ''))}</p>"
             + (f"<h4>Как читать</h4>{_legend_html(pg['legend'])}" if pg.get("legend") else "")
             + (f"<h4>Главное</h4><ul class='ins'>" + "".join(f"<li>{i}</li>" for i in pg["insights"]) + "</ul>"
                if pg.get("insights") else "")
             + (f"<h4>Термины</h4><dl class='terms'>{terms}</dl>"
                if terms and len(pg.get("legend", [])) + len(pg.get("insights", [])) <= 11 else ""))
    return (f"<section class='page' id='{cid}'>{head}<div class='pb'><div class='pc'>{body}</div>"
            f"<aside class='pa'>{aside}</aside></div>"
            f"<footer class='pf'><span>{_e(footer)}</span><span>стр. {pno}</span></footer></section>")


def _render_pages(charts, A, B, ctx, progress):
    """Run every chart builder; a failing chart becomes an error page, never a failed report."""
    out = []
    for cid, kind, title, fn in charts:
        if progress:
            progress(f"график {cid}")
        try:
            res = fn(A, B, ctx)
            res = res if isinstance(res, list) else [res]
        except Exception as exc:
            res = [{"fig": None, "error": f"{type(exc).__name__}: {exc}", "what": "", "legend": [],
                    "insights": [], "terms": []}]
        for k, pg in enumerate(res):
            pg["title"] = pg.get("title") or title
            out.append((cid if len(res) == 1 or k == 0 else f"{cid}·{k + 1}", kind, pg))
    return out


def build_html(A, B, ctx, out_path, progress=None):
    sel, periods = ctx["sel"], ctx["periods"]
    charts_a, charts_b = chart_registry(ctx)
    pages_a = _render_pages(charts_a, A, B, ctx, progress)
    pages_b = _render_pages(charts_b, A, B, ctx, progress)

    stamp = dt.datetime.now().strftime("%d.%m.%Y %H:%M")
    footer = f"{BANK} · {TITLE} · {plabel_full(sel)} · сформировано {stamp}"
    sec_a = f"A · Динамика {plabel(periods[0])} — {plabel(periods[-1])}"
    sec_b = f"B · Структура на {plabel_full(sel)}"
    first_chart_page = 4

    # cover ---------------------------------------------------------------
    kp = _kpis(A, B, sel)
    def kcls(w):
        return "flat" if w is None else ("up" if w else "dn")
    kpi = "".join(
        f"<div class='kpi'><div class='k'>{_e(k['label'])}</div><div class='v'>{k['value'] or '—'}</div>"
        "<div class='d'>" + (f"<span class='{kcls(k['wm'])}'>мес.: {k['dm']}</span>" if k["dm"] else "&nbsp;")
        + (f" · <span class='{kcls(k['wy'])}'>год: {k['dy']}</span>" if k["dy"] else "") + "</div>"
        f"<div class='s'>{_e(k['short'])}</div><div class='tip'>{k['tip']}</div></div>" for k in kp)
    head = "".join(f"<li>{h}</li>" for h in _headline(kp, sel))
    cover = (f"<section class='page cover' id='cover'><div class='eyebrow'>{_e(BANK)} · аналитический отчёт</div>"
             f"<h1>{_e(TITLE)}</h1><div class='meta'>Динамика: {plabel_full(periods[0])} — {plabel_full(periods[-1])}"
             f" &nbsp;·&nbsp; Структура на: {plabel_full(sel)} &nbsp;·&nbsp; {len(periods)} отчётных дат"
             f" &nbsp;·&nbsp; Сформировано: {stamp}"
             + ("<br>Даты отчётные: «" + plabel_full(sel) + "» — состояние на 1-е число этого месяца."
                if LABEL_BY_REPORT_DATE else "") + f"</div><div class='kpis'>{kpi}</div>"
             f"<div class='headline'><h3>Главное на {plabel_full(sel)}</h3><ul>{head}</ul></div>"
             f"<footer class='pf'><span>Наведите курсор на показатель — появится объяснение. "
             f"Под значением: изменение за месяц и за год; красным — ухудшение, зелёным — улучшение.</span>"
             f"<span>стр. 1</span></footer></section>")

    # contents --------------------------------------------------------------
    def toc(pages, start):
        return "".join(f"<a href='#{_e(cid)}'><span class='n'>{_e(cid)}</span><span>{_e(pg['title'])}</span>"
                       f"<span class='p'>{start + i}</span></a>" for i, (cid, _, pg) in enumerate(pages))
    contents = (f"<section class='page' id='contents'><header class='ph'><div class='ph-l'><span class='cid'>≡</span>"
                f"<h2>Содержание</h2></div></header><div class='toc'>"
                f"<h3>{_e(sec_a)}</h3>{toc(pages_a, first_chart_page)}"
                f"<h3>{_e(sec_b)}</h3>{toc(pages_b, first_chart_page + len(pages_a))}</div>"
                f"<footer class='pf'><span>{_e(footer)}</span><span>стр. 2</span></footer></section>")

    # how to read -----------------------------------------------------------
    deps = ctx.get("departments", [])
    k1 = _legend_html(_dept_legend(deps))
    k2 = _legend_html([(COLORS["npl"], "Красный", "NPL, дефолты — всё, что плохо", "bar"),
                       (COLORS["watch"], "Оранжевый", f"зона риска {_wz()}, ранние сигналы", "bar"),
                       (COLORS["good"], "Зелёный", "выдачи, выздоровление, покрытие", "bar"),
                       (COLORS["neutral"], "Серый", "погашения, «прочие», фон", "bar"),
                       (COLORS["ink"], "Чёрный", "итоги и банк целиком", "line")])
    k3 = _legend_html([(BUCKET_COLORS[b], lab(b), "корзина просрочки", "bar") for b in BUCKET_ORDER
                       if b != "CUR" or SHOW_CURRENT_BUCKET])
    G = glossary()
    gl = "".join(f"<div><dt>{_e(t)}</dt> <dd>— {_e(d)}</dd></div>" for t, d in G.values())
    howto = (f"<section class='page' id='howto'><header class='ph'><div class='ph-l'><span class='cid'>?</span>"
             f"<h2>Как читать отчёт</h2></div></header>"
             f"<div class='key'><div><h3>Департаменты</h3>{k1}</div><div><h3>Смысл цвета</h3>{k2}</div>"
             f"<div><h3>Просрочка</h3>{k3}</div></div>"
             f"<p style='margin:12px 0 0;color:#3A3A40'>Один цвет всегда означает одно и то же. Каждая страница — "
             f"один график: слева картинка, справа «Что показано», «Как читать» и «Главное» — выводы, посчитанные "
             f"из данных. Раздел A — динамика по месяцам, раздел B — структура на одну дату ({plabel_full(sel)}). "
             f"Суммы — в {UNIT_NAME}.</p><h4 style='font-size:11px;letter-spacing:.2em;text-transform:uppercase;"
             f"color:#C9971A;margin:14px 0 4px'>Словарь</h4><dl class='gl'>{gl}</dl>"
             f"<footer class='pf'><span>Печать: Ctrl+P → A4, альбомная, поля «Нет», «Фон» включён.</span>"
             f"<span>стр. 3</span></footer></section>")

    # chart pages -------------------------------------------------------------
    body, pno = [], first_chart_page
    for section, pages in ((sec_a, pages_a), (sec_b, pages_b)):
        for cid, kind, pg in pages:
            if progress:
                progress(f"страница {cid}")
            unit = "" if kind in ("КОГОРТЫ",) else UNIT_NAME
            body.append(_page_html(pg, cid, kind, section, unit, footer, pno, False))
            pno += 1

    try:
        from plotly.offline import get_plotlyjs_version
        pver = get_plotlyjs_version()
    except Exception:
        pver = "2.35.2"
    doc = (f"<!doctype html><html lang='ru'><head><meta charset='utf-8'>"
           f"<meta name='viewport' content='width=device-width,initial-scale=1'>"
           f"<title>{_e(TITLE)} — {plabel_full(sel)}</title>"
           f"<script src='https://cdn.plot.ly/plotly-{pver}.min.js'></script>"
           f"<style>{CSS}</style></head><body>{cover}{contents}{howto}{''.join(body)}</body></html>")
    Path(out_path).write_text(doc, encoding="utf-8")
    return len(pages_a) + len(pages_b)


# ==========================================================================
# ENTRY POINT — the only thing Django calls
# ==========================================================================
def run(data_dir, out_path, period_from=None, period_to=None,
        selected_period=None, progress=None):
    """
    Full pipeline. Returns a dict of facts the caller can store.

    progress: optional callable(str) so the web layer can show a live status.
    """
    say = progress or (lambda *_: None)
    _ensure_template()

    say("чтение файлов")
    raw = read_months(data_dir, period_from, period_to)
    has_oked = "oked_name" in raw.columns

    say("построение панели")
    panel = build_panel(raw)
    periods = sorted(int(p) for p in panel["period"].unique())
    if not periods:
        raise ValueError("нет данных за выбранный период")

    sel = int(selected_period) if selected_period else int(periods[-1])
    if sel not in periods:
        raise ValueError(f"период {sel} отсутствует в выбранном диапазоне "
                         f"{periods[0]}–{periods[-1]}")

    # Closed loans linger at zero balance: they inflate client counts and averages.
    snap = panel[(panel["period"] == sel) & (panel["exposure"] > MIN_BALANCE)].copy()
    dropped = int((panel["period"] == sel).sum()) - len(snap)

    say("расчёт витрин")
    A, B, top_pass = build_marts(panel, snap, periods, sel, has_oked)
    ctx = {"sel": sel, "periods": periods, "has_oked": has_oked,
           "departments": list(top_pass.keys()), "top_pass": top_pass}

    say("сборка отчёта")
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    n_pages = build_html(A, B, ctx, out_path, progress=say)

    T = _total(A)
    return {
        "html_path": str(out_path),
        "selected_period": sel,
        "period_from": int(periods[0]),
        "period_to": int(periods[-1]),
        "n_periods": len(periods),
        "n_rows": int(len(panel)),
        "n_loans": int(B["_n_loans"]),
        "n_clients": int(B["_n_clients"]),
        "exposure": float(B["_tot_exp"]),
        "npl_ratio": at(T["npl_ratio"], sel) if _ok(at(T["npl_ratio"], sel)) else None,   # JSON has no NaN
        "dropped_zero_balance": dropped,
        "n_charts": sum(len(x) for x in chart_registry(ctx)),
        "n_pages": n_pages + 3,
    }
