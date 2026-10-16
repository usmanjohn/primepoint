"""
Analytics engine for the portfolio report — the "album" edition.

The report is a stack of A4 landscape pages, one chart per page. Every page has the
chart across the page and a panel under it: what the chart shows, what every colour
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
import pyarrow.parquet as pq
from pandas.api.types import union_categoricals


# ==========================================================================
# НАСТРОЙКИ — меняйте здесь
# ==========================================================================
TITLE, BANK = "Обзор кредитного портфеля", "Kapitalbank"

# Departments: the order they appear in everywhere (legends, B06), and one colour each.
# Keys are matched case-insensitively, Cyrillic к/м/р/с count as k/m/r/s.
DEPARTMENTS = ["kk", "mk", "rk", "sk"]
DEPT_COLORS = {"kk": "#F2C230", "mk": "#2A2A2E", "rk": "#C9971A", "sk": "#8A867C"}   # Kapitalbank yellow first
DEPT_NAMES = {}            # e.g. {"kk": "Корпоративный"}; empty = show the value from the data
EXTRA_COLORS = ["#5E5A52", "#E0A526", "#B9B5AB", "#8C6A12"]   # a department not listed above

# Meaning colours: the same thing is the same colour on every page. Kapitalbank's yellow leads;
# red is ONLY for NPL, orange only for the risk zone.
COLORS = {
    "npl": "#B3341F",        # NPL 90+, defaults — the only red
    "watch": "#E08A1E",      # risk zone, early warnings
    "good": "#F2C230",       # Kapitalbank yellow: issued, cured, reserves, "fine"
    "good_text": "#8C6A12",  # the same idea as TEXT (yellow letters cannot be read on white)
    "gold": "#C9971A",       # deep gold, the second brand tone
    "neutral": "#8A867C",    # "others", repayments, residuals
    "light": "#D9D4C7",      # background stacks, «Прочие»
    "ink": "#1A1A1E",        # totals, bank-wide lines
    "char": "#2A2A2E",       # charcoal, the dark brand tone
}
CURRENCY_COLORS = {"Сум": "#F2C230", "USD": "#2A2A2E", "EUR": "#C9971A"}
# Products inside one department (A14…): clearly different colours, largest first.
# No red — red is the NPL line drawn over them. "Прочие" is always light grey.
PRODUCT_COLORS = ["#F2C230", "#2A2A2E", "#C9971A", "#8A867C", "#F7E3A1", "#8C6A12", "#5E5A52", "#E0A526"]

# Delinquency: the risk zone shown on A01/A13 and the KPI, and the report's buckets.
WATCH_DPD = (61, 90)
REPORT_BUCKETS = (
    (0, 0, "CUR"), (1, 30, "B01_30"), (31, 90, "B31_90"), (91, 180, "B91_180"),
    (181, 365, "B181_365"), (366, 10**9, "B365P"),
)
BUCKET_COLORS = {"CUR": "#F7E3A1", "B01_30": "#F2C230", "B31_90": "#E08A1E",
                 "B91_180": "#C2591F", "B181_365": "#A33418", "B365P": "#6E1F0E"}
SHOW_CURRENT_BUCKET = False   # False: the "0 дней" bucket is left out of A03/B02/B07

# Top clients (A-page dynamics + B08 table).
TOP_CLIENTS = 50
TOP_CLIENTS_EXCLUDE = ["rk"]  # a client whose loans are ONLY in these departments is never ranked
                              # or named; a client with loans here AND elsewhere counts in full
COURT_DEPARTMENT = "rk"       # B10 looks at this department only
WRITE_OFF_COL = "spisat_95413_summa"   # B10: the bad part INSIDE a loan's balance. It is carved out
                                       # first; what is left stays in the loan's court stage

# Branches whose name means "unknown" are left out of every branch chart.
NO_BRANCH = ["nodata", "no data", "нет данных", "", "nan", "none", "<na>"]
BRANCHES_PER_PAGE = 18        # longer branch lists continue on the next page

# Dates. The data for September is the state on 1 October, so by default every reporting
# date is labelled by its report_date month: September's portfolio shows as «окт».
# Issue months (cohorts: A07, A08, B03) are never shifted — a loan issued in September
# was issued in September. False = label by the month the data describes.
LABEL_BY_REPORT_DATE = True

TOP_PASSPORTS, TOP_PRODUCTS, TOP_OKED = 5, 15, 10   # department pages: top 5 products + «Прочие»
TOP_PER_DEPT = 5              # products page: this many per department, departments in DEPARTMENTS order
# Rename products (passport) everywhere in the report: {"name in the data": "name to show"}.
# Case, extra spaces and Latin look-alike letters do not matter on the left. If the new name
# already exists as a product, the two are counted as one.
PASSPORT_RENAME = {
    "корпоратив кредит": "уполномоченный орган",
}
# «Из 100 клиентов» (B11): which icon stands for each department, and what the department is.
DEPT_ICONS = {"rk": "person", "kk": "building", "mk": "shop", "sk": "card"}   # person/building/shop/card
DEPT_ABOUT = {"rk": "физические лица", "kk": "корпоративные клиенты", "mk": "малый бизнес",
              "sk": "онлайн-кредиты физлицам"}
B10_SHOW_ALL = False
SHOW_DATA_CHECK = True
SHOW_BRANCH_MAP = False       # the branch scatter (NPL level × change); off by request, True brings it back        # last page «Проверка данных»: unreadable amounts/dates, merged spellings, jumps          # B10: also draw the «все кредиты» bar (it is big and squeezes the other three)
A07_MARKS = ((30, 3), (30, 6), (90, 12))   # A07 checkpoints; the ones with too few cohorts are skipped

# Top-50 names. A small table YOU fill (Excel or CSV), in the folder above the data folder
# (datasets/dynamics/top50_names.xlsx or .csv), columns:
#     report_date | contragent | name | aloqador
# report_date empty = the row is valid for every month; aloqador 1 / да / ha / x = related company.
# Every report writes top50_template.csv next to itself, with all its top-50 ids, to start from.
TOP_NAMES_FILE = "top50_names"

# Regulation (from the kapital/laws pages). CBU 3937 minimum reserve by quality category;
# collateral may lower the required reserve, so being under the minimum is a question, not a breach.
RESERVE_MIN = {1: 1, 2: 10, 3: 25, 4: 50, 5: 100}
CATEGORY_NAMES = {1: "Стандартный", 2: "Субстандартный", 3: "Неудовлетворительный",
                  4: "Сомнительный", 5: "Безнадёжный"}
# CBU 3283: one borrower ≤ 25% of Tier 1 capital, "large" from 10%. Put the bank's Tier 1 capital
# here (in сум, e.g. 2_500e9) to switch the large-exposure page on; None keeps it off.
TIER1_CAPITAL = None
LARGE_LIMIT, LARGE_FROM = 25, 10
SHOW_OKED = False             # True brings back both industry (ОКЭД) pages: the monthly one and B12

# Lines drawn through the bars use the right-hand % scale; it reaches LINE_HEADROOM × the
# line's highest value, so a bigger number puts the line lower. 1.0 = the line touches the top.
LINE_HEADROOM = 1.75
UNIT, UNIT_NAME = 1e9, "млрд сум"

# Page geometry (A4 landscape): the chart spans the page, the explanation sits under it.
CHART_W, CHART_H = 1045, 420
FONT = "Segoe UI, Roboto, Arial, sans-serif"
FONT_SIZE, LABEL_SIZE = 13, 12
LABEL_PX = 34                 # room one value label needs; labels per series = chart width / this,
                              # so every month is labelled when it fits, every 2nd when it does not


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
    "non_auto": "Не авто", "pervichka": "pervichka (новые авто)", "vtorichka": "vtorichka (с пробегом)",
    "norm": "Норма (без суда)", "neofficial": "Неофициальная (досудебная)",
    "official": "Официальная (в суде)",
    # the fine buckets, used by the migration matrix
    "B31_60": "31–60 дн.", "B61_90": "61–90 дн.", "B181_360": "181–360 дн.", "B360P": "360+ дн.",
    "EXIT": "Закрыт",
}
SUD_ALIASES = {"unofficial": "neofficial", "neoficial": "neofficial", "neofficial": "neofficial",
               "official": "official", "oficial": "official", "norm": "norm", "normal": "norm"}
SUD_ORDER = ["norm", "neofficial", "official"]
SUD_COLORS = {"norm": "#D9D4C7", "neofficial": "#E08A1E", "official": "#B3341F"}
WRITE_OFF_COLOR = "#3A3A40"

# Only the columns the report reads. Anything else in a file (tobo, dogovor_sana, protsent_*,
# spisat_91501…) is never loaded: on the server 17M rows × every column did not fit in 15 GB.
CANONICAL = [
    "contragent", "anketa", "filial", "valuta", "vidacha_sana",
    "department", "passport",
    "brutto_95_summa", "brutto_summa", "spisat_95413_summa", "reserve_summa",
    "vidacha_tekushiy_summa", "pogashen_tekushiy_summa", "maks_dni",
    "kategoriya_npl_90", "straxovka_summa", "straxovka_brutto_95_summa",
    "kategoriya_straxovka", "sud", "avto", "report_date",
]
# contragent_name may be missing (names come from your top50_names file anyway);
# oked_name is read only when the OKED pages are on.
OPTIONAL = ["contragent_name"] + (["oked_name"] if SHOW_OKED else [])
RENAME = {
    "vidacha_tm_summa": "vidacha_tekushiy_summa",
    "pogashen_tm_summa": "pogashen_tekushiy_summa",
}
DATE_COLS = ("vidacha_sana", "report_date")
AMOUNT_COLS = [c for c in CANONICAL if c.endswith("_summa")]
# Text columns are held as pandas categories: 17M copies of «Ташкент Центр» become 17M small
# integers pointing at one string. Cleaning (strip, spelling merge) then runs per distinct value.
TEXT_COLS = ["filial", "department", "passport", "contragent_name", "sud", "avto", "oked_name"]

PCFG = {"displaylogo": False, "responsive": False,
        "modeBarButtonsToRemove": ["select2d", "lasso2d", "autoScale2d",
                                   "hoverClosestCartesian", "hoverCompareCartesian",
                                   "toggleSpikelines", "zoomIn2d", "zoomOut2d"],
        "toImageButtonOptions": {"format": "png", "scale": 2}}

KINDS = {"ИТОГИ": "ИТОГИ · месяц к месяцу", "СТОК": "СТОК · снимок на дату", "ПОТОК": "ПОТОК · за месяц",
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
                   tickfont=dict(size=12), automargin=True, hoverformat=",.2f"),
        yaxis=dict(gridcolor=rule, zerolinecolor=rule, tickfont=dict(size=12),
                   automargin=True, hoverformat=",.2f"),
        showlegend=False, width=CHART_W, height=CHART_H,
        # paper first: a hover never shows 12.3456789 — two decimals at most
        hovermode="closest",
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


def fit(px=None):
    """How many labels of ~px pixels fit side by side across the plot area."""
    return max(4, int((CHART_W - 150) / (px or LABEL_PX)))


def thin(values, fmt=lambda v: fnum(v, 1), max_labels=None, keep_last=True):
    """Label every k-th point (and the last) so labels never collide."""
    vals = list(values)
    return [fmt(v) if _ok(v) and i in _label_idx(len(vals), max_labels, keep_last) else ""
            for i, v in enumerate(vals)]


def _label_idx(n, max_labels=None, keep_last=True):
    """Which positions get a label: every k-th, plus the last — dropping the one before
    the last when the two would sit closer than ~half a step."""
    step = max(1, math.ceil(n / (max_labels or fit())))
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
        if tr.type in ("bar", "scatter"):
            for ax in ("x", "y"):
                v = getattr(tr, ax)
                if v is not None:
                    arr = np.asarray(v, dtype=object)
                    if arr.size and all(isinstance(z, (int, float, np.number)) or z is None for z in arr):
                        setattr(tr, ax, [round(float(z), 3) if z is not None and np.isfinite(float(z)) else None for z in arr])
        if tr.type in ("bar", "scatter") and tr.hovertemplate is None and tr.hoverinfo != "skip":
            h = getattr(tr, "orientation", None) == "h"
            tr.hovertemplate = ("%{y}<br>%{x:,.2f}" if h else "%{x}<br>%{y:,.2f}") + "<extra></extra>"
        if tr.type == "bar" and tr.textposition == "outside":
            tr.constraintext = "none"      # otherwise plotly hides labels wider than the bar
        if tr.type == "bar" and tr.textposition == "inside" and tr.textangle is None:
            tr.textangle = 0               # never auto-rotated ("%16"); hidden if it does not fit
    for tr in list(f.data):
        if tr.type == "scatter" and tr.yaxis == "y2" and tr.text is not None and "text" in (tr.mode or ""):
            pos = tr.textposition if isinstance(tr.textposition, (list, tuple)) else [tr.textposition] * len(tr.x)
            col = (tr.line.color if tr.line and tr.line.color else COLORS["ink"])
            for xi, yi, ti, ps in zip(tr.x, tr.y, tr.text, pos):
                if ti and _ok(yi):
                    f.add_annotation(x=xi, y=yi, yref="y2", text=ti, showarrow=False,
                                     yshift=11 if str(ps).startswith("top") else -11,
                                     font=dict(size=10.5, color=col), bgcolor="rgba(255,255,255,.88)",
                                     borderpad=1)
            tr.mode = tr.mode.replace("+text", "").replace("text+", "")
            tr.text = None
    return f


def overlay(bar_max, *lines, pct_title="%"):
    """
    The classic two-scale chart: amounts on the left, percent on the right, and the line
    drawn straight through the bars. Line values get white labels (see base()), so they
    stay readable on top of a dark bar.
    """
    vals = np.concatenate([np.asarray(l, dtype=float) for l in lines]) if lines else np.array([1.0])
    vals = vals[np.isfinite(vals)]
    hi = float(vals.max()) if len(vals) else 1.0
    return dict(yaxis=dict(range=[0, (bar_max or 1) * 1.12]),
                yaxis2=dict(overlaying="y", side="right", range=[0, (hi or 1) * LINE_HEADROOM], ticksuffix="%",
                            showgrid=False, zeroline=False, tickfont=dict(size=11, color=COLORS["npl"]),
                            title=dict(text=pct_title, font=dict(size=11, color=COLORS["npl"]))))


def nice_ticks(top, n=4):
    """Round tick values from 0 up to `top` only — the bar scale stops where the bars stop."""
    if not _ok(top) or top <= 0:
        return [0]
    raw = top / n
    mag = 10 ** math.floor(math.log10(raw))
    step = next(m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= raw)
    return [round(i * step, 10) for i in range(int(top // step) + 1)]


def line_text(vals, fmt):
    """A value on every point: labels alternate above/below the line, so neighbours never touch."""
    text = thin(vals, fmt, max_labels=fit(17))
    pos = ["top center" if i % 2 == 0 else "bottom center" for i in range(len(text))]
    return text, pos


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
                                      "Клиенты, у которых кредиты только в " + ", ".join(TOP_CLIENTS_EXCLUDE)
                                      + ", не учитываются и не называются; у клиентов с кредитами и там, "
                                        "и в других департаментах считается весь долг."),
        "vintage": ("Месяц выдачи", "когорта: все кредиты, выданные в этом месяце."),
    }


# ==========================================================================
# LOAD
# ==========================================================================
def _norm_name(c):
    return RENAME.get(str(c).strip().lower().replace(" ", "_"), str(c).strip().lower().replace(" ", "_"))


def normalise(df):
    """One file's rows -> the report's types. Runs per file, so only one raw file is in memory."""
    df = df.rename(columns=_norm_name)
    missing = [c for c in CANONICAL if c not in df.columns]
    if missing:
        raise KeyError("в данных не хватает колонок: " + ", ".join(missing))
    df = df[CANONICAL + [c for c in OPTIONAL if c in df.columns]].copy()
    if "contragent_name" not in df.columns:
        df["contragent_name"] = _empty_cat(len(df))

    # amounts and dates may arrive as text ("1 234,56", "01.12.2025") in some months: read them
    # all, and remember which rows could not be read — the data-check page counts them
    bad_num = np.zeros(len(df), dtype=bool)
    for c in AMOUNT_COLS:
        raw_ = df[c]
        if pd.api.types.is_numeric_dtype(raw_):
            df[c] = raw_.astype("float64").fillna(0.0)      # a real number column has nothing unreadable
            continue
        num = _to_num(raw_)
        bad_num |= (num.isna() & raw_.notna() & (raw_.astype("string").str.strip() != "")).to_numpy()
        df[c] = num.fillna(0.0).astype("float64")   # plain float, like the months that arrive as numbers
    bad_date = np.zeros(len(df), dtype=bool)
    for c in DATE_COLS:
        raw_ = df[c]
        df[c] = _to_date(raw_)
        if c == "vidacha_sana":
            bad_date |= (df[c].isna() & raw_.notna()).to_numpy()
    df["_badnum"], df["_baddate"] = bad_num, bad_date
    df["maks_dni"] = _to_num(df["maks_dni"]).fillna(0).astype("int32")
    for c in ("kategoriya_npl_90", "kategoriya_straxovka"):
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype("int8")
    df["valuta"] = pd.to_numeric(df["valuta"], errors="coerce").fillna(0).astype("int32")
    for c in ("anketa", "contragent"):
        df[c] = pd.to_numeric(df[c], errors="coerce").astype("int64")

    for c in TEXT_COLS:
        if c in df.columns:
            df[c] = _recode(df[c], lambda v: str(v).strip())
    # avto: Latin pervichka / vtorichka (any case); everything else — 0, empty, other — is "not auto"
    df["avto"] = _recode(df["avto"], lambda v: v.lower() if v.lower() in ("pervichka", "vtorichka")
                         else "non_auto", na="non_auto")
    # spelling variants of the court stage collapse onto three keys; unknown values stay as they are
    df["sud"] = _recode(df["sud"], lambda v: SUD_ALIASES.get(v.lower(), v.lower()), na="norm")
    if "oked_name" in df.columns:
        df["oked_name"] = _recode(df["oked_name"], lambda v: v or "Не указано", na="Не указано")
    return df


def _empty_cat(n):
    return pd.Categorical.from_codes(np.full(n, -1, dtype="int8"), categories=pd.Index([], dtype=object))


def _recode(s, fn, na=None):
    """
    A text column as a category, with fn applied to each DISTINCT value instead of each row.
    Values that fn makes equal merge into one category; na (if given) replaces missing values.
    """
    c = s if isinstance(s.dtype, pd.CategoricalDtype) else s.astype("category")
    cats = c.cat.categories
    labels = [fn(str(v)) for v in cats]
    codes = c.cat.codes.to_numpy()
    if na is not None:
        labels.append(na)
        codes = np.where(codes < 0, len(cats), codes)
    if not labels:
        return pd.Series(_empty_cat(len(c)), index=c.index)
    remap, uniq = pd.factorize(pd.Index(labels, dtype=object))
    new = np.where(codes < 0, -1, remap[np.maximum(codes, 0)])
    return pd.Series(pd.Categorical.from_codes(new, categories=pd.Index(uniq, dtype=object)),
                     index=c.index)


def _to_num(s):
    """Numbers that may be text: spaces / non-breaking spaces as thousands, comma as decimal."""
    if pd.api.types.is_numeric_dtype(s):
        return s.astype("float64")
    t = s.astype("string").str.replace("[\\s\u00a0\u202f]", "", regex=True).str.replace(",", ".", regex=False)
    return pd.to_numeric(t, errors="coerce")


def _to_date(s):
    """Dates that may be mixed: real dates, '2025-12-01', '01.12.2025' — each value read on its own."""
    if pd.api.types.is_datetime64_any_dtype(s):
        return s.dt.tz_localize(None) if getattr(s.dt, "tz", None) is not None else s
    return pd.to_datetime(s, errors="coerce", format="mixed", dayfirst=True)


_LOOK = str.maketrans("acekmopxyhtb", "асекморхуhтв")   # Latin letters that look Cyrillic


def _name_key(v):
    return re.sub(r"[\s«»\"'`.]+", " ", str(v).casefold().translate(_LOOK)).strip()


def _canonical(col):
    """Merge spelling variants; each name takes its most common spelling. Returns (column, merges)."""
    vc = col.value_counts(dropna=True)
    vc = vc[vc > 0]
    if vc.empty:
        return col, {}
    keys = pd.Series({v: _name_key(v) for v in vc.index})
    best, merged = {}, {}
    for k, grp in keys.groupby(keys):
        variants = vc.reindex(grp.index).sort_values(ascending=False)
        for v in variants.index:
            best[v] = variants.index[0]
        if len(variants) > 1:
            merged[variants.index[0]] = {str(v): int(n) for v, n in variants.items()}
    return _recode(col, lambda v: best.get(v, v)), merged


def _sorted_cats(col):
    """Categories in alphabetical order, so grouping and sorting behave exactly like plain text."""
    cats = col.cat.categories
    return col.cat.reorder_categories(sorted(cats, key=str)) if len(cats) else col


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

    need = set(CANONICAL) | set(OPTIONAL)
    parts_ = []
    files_info = []
    for f in chosen:
        # only the columns the report uses — reading every column is what ran the server out of RAM
        names = pq.read_schema(f).names
        x_ = pd.read_parquet(f, columns=[c for c in names if _norm_name(c) in need])
        x_ = normalise(x_)
        rd = x_["report_date"]
        files_info.append({"file": f.name, "rows": len(x_), "bad_report_date": int(rd.isna().sum()),
                           "first": rd.min(), "last": rd.max()})
        # drop the months outside the window now, before the next file is read
        per = _row_period(rd)
        keep = np.ones(len(x_), dtype=bool)
        if period_from:
            keep &= (per >= int(period_from)).to_numpy()
        if period_to:
            keep &= (per <= int(period_to)).to_numpy()
        if not keep.all():
            x_ = x_[keep]
        parts_.append(x_)
        del x_

    # glue the files: text columns are unioned as categories (pd.concat would turn them into
    # plain strings again), everything else is concatenated as is
    text = [c for c in TEXT_COLS if all(c in p_.columns for p_ in parts_)]
    cats = {c: union_categoricals([p_[c] for p_ in parts_], ignore_order=True) for c in text}
    df = pd.concat([p_.drop(columns=text) for p_ in parts_], ignore_index=True)
    del parts_
    for c in text:
        df[c] = _sorted_cats(pd.Series(cats.pop(c), index=df.index))

    # one name, one spelling: "Микрокредит самозанятым", "микрокредит  самозанятым " and the same
    # words typed with a Latin «с» are ONE product (else it changes colour and leaks to «Прочие»)
    merges = {}
    for c in ["department", "filial", "passport"] + [c for c in ("oked_name",) if c in df.columns]:
        df[c], merges[c] = _canonical(df[c])
        df[c] = _sorted_cats(df[c])
    if PASSPORT_RENAME:
        ren = {_name_key(k): v for k, v in PASSPORT_RENAME.items()}
        df["passport"] = _sorted_cats(_recode(df["passport"], lambda v: ren.get(_name_key(v), v)))
    if df.empty:
        raise ValueError(f"нет данных за период {period_from}–{period_to}")
    df.attrs["merges"], df.attrs["files"] = merges, files_info
    return df


def data_fingerprint(data_dir):
    """
    Identity of the input set: name, size and mtime of every parquet file.
    Changes the moment a file is added, replaced or re-saved — which is exactly
    when a cached report stops being valid.
    """
    parts = []
    for f in sorted(Path(str(data_dir)).glob("*.parquet")) + [f for f in _names_files(data_dir) if f.exists()]:
        st = f.stat()
        parts.append(f"{f.name}:{int(st.st_mtime)}:{st.st_size}")   # your names table counts too
    return hashlib.sha256("|".join(parts).encode()).hexdigest()[:20]


def _names_files(data_dir):
    base = Path(str(data_dir)).parent / TOP_NAMES_FILE
    return [base.with_suffix(e) for e in (".xlsx", ".xls", ".csv")]


_TRUE = {"1", "да", "д", "ha", "xa", "yes", "y", "true", "x", "+", "1.0"}


def load_names(data_dir):
    """
    Your top-50 names table -> ({(period, id): (name, related)}, {id: (name, related)}, file).
    A row without report_date counts for every month. Unreadable or missing file = no names.
    """
    df, used = None, None
    for f in _names_files(data_dir):
        if not f.exists():
            continue
        try:
            if f.suffix == ".csv":
                for enc in ("utf-8-sig", "cp1251"):
                    try:
                        df = pd.read_csv(f, sep=None, engine="python", encoding=enc, dtype=str)
                        break
                    except UnicodeDecodeError:
                        continue
            else:
                df = pd.read_excel(f, dtype=str)
        except Exception:
            df = None
        if df is not None:
            used = f
            break
    if df is None:
        return {}, {}, None
    df.columns = [re.sub(r"[\W_]", "", str(c).strip().lower()) for c in df.columns]
    pick = lambda *ns: next((c for c in df.columns if c in ns), None)
    cd = pick("reportdate", "date", "дата", "отчетнаядата", "отчётнаядата")
    cc = pick("contragent", "контрагент", "id", "clientid")
    cn = pick("name", "имя", "название", "наименование", "nomi")
    ca = pick("aloqador", "связанная", "связанный", "related")
    by_pc, by_c = {}, {}
    if cc is None:
        return by_pc, by_c, used
    for _, r in df.iterrows():
        raw = str(r[cc] if pd.notna(r[cc]) else "").strip().replace(" ", "")
        if not re.fullmatch(r"\d+(\.0+)?", raw):
            continue
        cid = int(float(raw))
        name = str(r[cn]).strip() if cn and pd.notna(r[cn]) and str(r[cn]).strip() else None
        rel = str(r[ca]).strip().lower() in _TRUE if ca and pd.notna(r[ca]) else False
        dval = str(r[cd]).strip() if cd and pd.notna(r[cd]) else ""
        if dval:
            d = pd.to_datetime(dval, dayfirst="." in dval, errors="coerce")
            if pd.isna(d):
                continue
            d -= pd.Timedelta(days=1)                       # report_date 1st of next month -> period
            by_pc[(d.year * 100 + d.month, cid)] = (name, rel)
        else:
            by_c[cid] = (name, rel)
    return by_pc, by_c, used


def apply_names(A, names):
    """Give every top-50 row a shown name and the «связанная» flag from your table."""
    by_pc, by_c, _ = names
    t = A["top"]
    shown, rel = [], []
    for per, cid, nm in zip(t["period"], t["contragent"], t["name"]):
        n_, r_ = by_pc.get((int(per), int(cid)), by_c.get(int(cid), (None, False)))
        base_name = nm if pd.notna(nm) and str(nm).strip() and not str(nm).strip().isdigit() else None
        shown.append(n_ or base_name or f"ID {int(cid)}")
        rel.append(bool(r_))
    A["top"] = t.assign(shown=shown, rel=rel)
    rs = A["top"].groupby("period")[["exposure"]].apply(
        lambda g: pd.Series({"rel_exp": float(g.loc[A["top"].loc[g.index, "rel"], "exposure"].sum()),
                             "n_rel": int(A["top"].loc[g.index, "rel"].sum())}))
    A["top_summary"] = A["top_summary"].merge(rs.reset_index(), on="period", how="left")
    A["has_rel"] = bool(A["top"]["rel"].any())


def write_top_template(A, out_dir):
    """top50_template.csv: every top-50 id of this report, ready to fill (Excel opens it as is)."""
    t = A["top"].sort_values(["period", "rank"])
    rd = [f"{shift_p(p_, -1) // 100}-{shift_p(p_, -1) % 100:02d}-01" for p_ in t["period"]]
    out = pd.DataFrame({"report_date": rd, "contragent": t["contragent"].astype(int),
                        "name": [n if not str(n).startswith("ID ") else "" for n in t["shown"]],
                        "aloqador": ["1" if r else "" for r in t["rel"]], "rank": t["rank"],
                        "exposure_mln": (t["exposure"] / 1e6).round(1)})
    f = Path(out_dir) / "top50_template.csv"
    out.to_csv(f, sep=";", index=False, encoding="utf-8-sig")
    return f


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
    """
    The loan × month panel. Takes OWNERSHIP of raw: call it as build_panel(read_months(...)),
    so the raw table can be freed the moment the panel is built.
    """
    d = raw.copy(deep=False)        # new columns go on d only; no second copy of 17M rows
    attrs = dict(raw.attrs)
    del raw
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
    d["writeoff"] = d[WRITE_OFF_COL]
    d["insurance_paid"] = d["straxovka_summa"]

    d["dpd"] = d["maks_dni"].clip(lower=0)
    d["bucket"] = _bucketise(d["dpd"], REPORT_BUCKETS, BUCKET_ORDER)
    d["mbucket"] = _bucketise(d["dpd"], MIGRATION_BUCKETS, MIGRATION_ORDER)
    d["mob_band"] = pd.cut(d["mob"].astype("float"), MOB_BINS, labels=MOB_LABELS)

    d["kat"] = d["kategoriya_npl_90"]
    d["on_balance"] = d["brutto_summa"]
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
    vals = d["valuta"].unique()
    d["cur_name"] = d["valuta"].map({v: CURRENCY_NAMES.get(v, str(v)) for v in vals}).astype("category")
    uniq = d["department"].dropna().unique()
    d["dkey"] = d["department"].map({u: dkey(u) for u in uniq}).astype("category")

    has_oked = "oked_name" in d.columns
    keep = ["anketa", "contragent", "contragent_name", "period", "vintage", "mob", "mob_band",
            "dpd", "bucket", "mbucket", "is_npl", "is_watch", "is_new", "is_npl_gross",
            "in_court", "exposure", "exposure_gross", "npl_exposure", "watch_exposure",
            "npl_gross_exp", "reserve", "disbursed", "repaid", "written_amt", "writeoff",
            "insurance_paid", "filial", "department", "dkey", "passport", "avto",
            "valuta", "cur_name", "sud", "kat", "on_balance", "_badnum", "_baddate"] + (["oked_name"] if has_oked else [])
    order = np.lexsort((d["period"].to_numpy(), d["anketa"].to_numpy()))   # = stable sort by anketa, period
    p = d[keep].take(order).reset_index(drop=True)
    del d
    p.attrs.update(attrs)

    g = p.groupby("anketa", sort=False)
    p["mi"] = (p["period"] // 100) * 12 + (p["period"] % 100)
    p["peak_dpd"] = g["dpd"].cummax()
    prev_mi, next_mi = g["mi"].shift(1), g["mi"].shift(-1)
    back, fwd = prev_mi.eq(p["mi"] - 1), next_mi.eq(p["mi"] + 1)
    p["prev_is_npl"] = g["is_npl"].shift(1).where(back).astype("float32")   # 1 / 0 / NaN = no previous month
    p["prev_exposure"] = g["exposure"].shift(1).where(back)
    p["next_mbucket"] = g["mbucket"].shift(-1).where(fwd, "EXIT")     # a category: EXIT is one of them
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
    Each month's TOP_CLIENTS largest clients by balance. A client whose loans are only in
    TOP_CLIENTS_EXCLUDE is left out (never ranked or named); a client with loans there and
    elsewhere is ranked on the whole balance.
    Returns (all clients ranked per period, top rows, per-period summary, top by department).
    """
    excl = {dkey(x) for x in TOP_CLIENTS_EXCLUDE}
    p = panel.loc[(panel["exposure"] > MIN_BALANCE).to_numpy(),
                  ["period", "contragent", "anketa", "dkey", "department", "exposure", "npl_exposure",
                   "dpd", "contragent_name"]]
    # keep a client in a month only if they hold at least one loan OUTSIDE the excluded
    # departments that month; then all their loans count, the excluded ones included
    elsewhere = (~p["dkey"].isin(excl)).groupby([p["period"], p["contragent"]], observed=True).transform("any")
    p = p[elsewhere.to_numpy()]
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


def _plain_text(obj):
    """
    The marts are small, so text goes back to plain strings before the charts see it: the
    category trick is for the 17M-row panel only. Ordered categories (buckets, MOB bands)
    are real orderings and stay as they are.
    """
    if isinstance(obj, dict):
        return {k: _plain_text(v) for k, v in obj.items()}
    if isinstance(obj, pd.DataFrame):
        cols = [c for c in obj.columns
                if isinstance(obj[c].dtype, pd.CategoricalDtype) and not obj[c].dtype.ordered]
        return obj.astype({c: "string" for c in cols}) if cols else obj
    if isinstance(obj, pd.Series) and isinstance(obj.dtype, pd.CategoricalDtype) and not obj.dtype.ordered:
        return obj.astype("string")
    return obj


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
    # (masks on single columns: panel[mask] would copy every column of 17M rows)
    stock = panel.groupby("period", observed=True)["npl_exposure"].sum()
    has_prev = panel["prev_is_npl"].notna().to_numpy()
    was_npl = panel["prev_is_npl"].where(has_prev, False).astype(bool).to_numpy()
    is_npl = panel["is_npl"].to_numpy()
    m_in, m_cu = has_prev & is_npl & ~was_npl, has_prev & ~is_npl & was_npl
    inflow = panel.loc[m_in, "exposure"].groupby(panel.loc[m_in, "period"]).sum()
    cured = panel.loc[m_cu, "prev_exposure"].groupby(panel.loc[m_cu, "period"]).sum()
    m_ex = is_npl & panel["exited_after"].to_numpy()
    exited = (panel.loc[m_ex, ["period", "exposure"]]
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
    m_tr = panel["next_mbucket"].notna().to_numpy()
    gg = (panel.loc[m_tr, ["period", "mbucket", "next_mbucket", "anketa"]]
          .rename(columns={"mbucket": "from_b", "next_mbucket": "to_b"})
          .groupby(["period", "from_b", "to_b"], observed=True)["anketa"].size().reset_index(name="n"))
    gg = gg.astype({"from_b": "string", "to_b": "string"}) \
           .sort_values(["period", "from_b", "to_b"], kind="stable").reset_index(drop=True)
    gg["rate"] = gg["n"] / gg.groupby(["period", "from_b"], observed=True)["n"].transform("sum")
    A["transitions"] = gg

    # COHORTS. Only loans ISSUED inside the window (an older loan's first months are missing).
    # The denominator is every loan of the cohort — a loan that closed at month 4 still counts
    # at month 6, otherwise short products (microloans) shrink to a handful of "survivors" and
    # the 6- and 12-month checkpoints vanish. A checkpoint m is shown once the cohort is m
    # months old at the LAST month of data.
    marks_all = sorted(set(VINTAGE_MARKS) | set(A07_MARKS))
    vv = panel.loc[(panel["vintage"].notna() & (panel["vintage"] >= periods[0])
                    & panel["mob"].between(0, 36)).to_numpy(),
                   ["anketa", "vintage", "department", "peak_dpd", "mob"]]
    last = int(periods[-1])
    rows = []
    if len(vv):
        lo = vv.groupby("anketa", observed=True).agg(vintage=("vintage", "first"),
                                                    department=("department", "first"))
        for thr in sorted({t_ for t_, _ in marks_all} | {30, 90}):
            lo[f"fb{thr}"] = vv[vv["peak_dpd"] > thr].groupby("anketa")["mob"].min()   # first month it went bad
        lo["age"] = lo["vintage"].map(lambda v: (last // 100 - v // 100) * 12 + last % 100 - v % 100)
        for v_, g_ in lo.groupby("vintage"):
            n_ = len(g_)
            age_ = int(g_["age"].iloc[0])
            for thr, mob in marks_all:
                if age_ >= mob:
                    rows.append({"vintage": int(v_), "metric": f"GL{thr}+@{mob}MOB", "n_loans": n_,
                                 "rate": float((g_[f"fb{thr}"] <= mob).sum() / n_), "reliable": n_ >= MIN_COHORT})
        # early defaults: of each month's issues, % 30+ late within the first 3 months
        e = lo[lo["age"] >= 3]
        ge = e.groupby(["vintage", "department"], observed=True)
        ed = pd.DataFrame({"n": ge.size(), "bad": ge["fb30"].apply(lambda s_: int((s_ <= 3).sum()))}).reset_index()
        ed["rate"] = ed["bad"] / ed["n"]
        A["early"] = ed[ed["n"] >= MIN_COHORT]
    else:
        A["early"] = pd.DataFrame(columns=["vintage", "department", "n", "bad", "rate"])
    A["vin_marks"] = pd.DataFrame(rows, columns=["vintage", "metric", "rate", "n_loans", "reliable"]) \
        .astype({"reliable": bool})

    # data check (last page): rows, amounts that could not be read, products per month
    gq = panel.groupby("period", observed=True)
    A["quality"] = pd.DataFrame({"rows": gq.size(), "loans": gq["anketa"].nunique(),
                                 "badnum": gq["_badnum"].sum(), "baddate": gq["_baddate"].sum(),
                                 "products": gq["passport"].nunique()}).reset_index()

    # month-on-month pieces for the «что изменилось» page
    A["passport"] = by_period(panel, "passport")
    newnpl = panel.loc[((panel["period"] == sel) & panel["is_npl"]
                        & (panel["prev_is_npl"] == False)).to_numpy(), ["department", "exposure"]]  # noqa: E712
    A["inflow_dep"] = newnpl.groupby("department", observed=True)["exposure"].sum()

    # products per department, chosen and ORDERED by their standing at SEL
    top_pass = {}
    for dep in dept_sorted(snap["department"].dropna().unique()):
        s = (snap[snap["department"] == dep]
             .groupby("passport", observed=True)["exposure"].sum()
             .sort_values(ascending=False))
        top_pass[str(dep)] = [str(x) for x in s.head(TOP_PASSPORTS).index]
    other = np.zeros(len(panel), dtype=bool)
    for dep, keep in top_pass.items():
        other |= ((panel["department"] == dep) & (~panel["passport"].isin(keep))).to_numpy()
    grp = panel["passport"]
    if "Прочие" not in grp.cat.categories:
        grp = grp.cat.add_categories(["Прочие"])
    grp = grp.mask(other, "Прочие").rename("passport_grp")
    gp = panel[["period", "department", "exposure", "npl_exposure"]].assign(passport_grp=grp) \
        .groupby(["period", "department", "passport_grp"], observed=True)
    pdp = pd.DataFrame({"exposure": gp["exposure"].sum(),
                        "npl_exposure": gp["npl_exposure"].sum()}).reset_index()
    A["passport_dep"] = pdp.astype({"department": "string", "passport_grp": "string"}) \
        .sort_values(["period", "department", "passport_grp"], kind="stable").reset_index(drop=True)

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
    # the write-off is the bad part INSIDE the balance: take it out first (never more than the
    # balance itself), and only the remainder stays in the loan's court stage
    wo = cs["writeoff"].clip(lower=0).where(lambda v: v <= cs["exposure"], cs["exposure"])
    parts = pd.concat([
        pd.DataFrame({"avto": cs["avto"], "stage": cs["sud"].astype("string"), "amount": cs["exposure"] - wo}),
        pd.DataFrame({"avto": cs["avto"], "stage": "writeoff", "amount": wo}),
    ])
    B["court"] = parts.groupby(["avto", "stage"], observed=True)["amount"].sum().reset_index()
    B["court_dep_name"] = (str(cs["department"].iloc[0]) if len(cs) else COURT_DEPARTMENT)

    # client status by department (worst loan wins): on time / overdue / NPL
    cl = snap.groupby(["department", "contragent"], observed=True).agg(npl=("is_npl", "max"), dpd=("dpd", "max"))
    cl["st"] = np.where(cl["npl"], "npl", np.where(cl["dpd"] > 0, "late", "ok"))
    B["client_status"] = cl.reset_index().groupby(["department", "st"], observed=True).size().unstack(fill_value=0)

    # reserves by quality category (CBU 3937)
    rc = snap.groupby("kat", observed=True).agg(exposure=("exposure", "sum"), reserve=("reserve", "sum"),
                                                on_balance=("on_balance", "sum"), writeoff=("writeoff", "sum"),
                                                n_loans=("anketa", "size")).reset_index()
    B["reserve_cat"] = rc[rc["kat"].isin(list(RESERVE_MIN))]

    # branch map: NPL now against NPL a year (or the window's start) earlier
    b0 = shift_p(sel, 12) if shift_p(sel, 12) in periods else periods[0]
    fp = A["filial"]
    then = fp[fp["period"] == b0].set_index("dim_value")["npl_ratio"]
    bm = B["filial"].copy()
    bm["npl_then"] = bm["name"].map(then)
    dom = fd.sort_values("exposure").groupby("filial", observed=True)["department"].last()
    bm["dep"] = bm["name"].map(dom)
    B["branch_map"], B["branch_map_base"] = bm, b0

    # largest single borrowers, every department (CBU 3283 limits are on the whole exposure)
    ex = {dkey(x) for x in TOP_CLIENTS_EXCLUDE}
    cg = snap.groupby("contragent", observed=True).agg(exposure=("exposure", "sum"), name=("contragent_name", "first"),
                                                       only_ex=("dkey", lambda v: set(v) <= ex))
    B["borrowers"] = cg.sort_values("exposure", ascending=False).head(20).reset_index()

    return A, B, top_pass


# ==========================================================================
# CHARTS
#
# Every builder has the same shape: fn(A, B, ctx) -> page(...) or a list of
# pages (long branch lists continue on the next page). They take marts as
# arguments rather than reading globals, because two requests can be running
# with different periods at the same time.
# ==========================================================================
class Notice(Exception):
    """Not an error: the chart has nothing to show for this window. Rendered as a calm note."""


def _ref(ctx, fn_name):
    """The page number another page has in THIS run (pages renumber when one is switched off)."""
    return ctx.get("cid_of", {}).get(fn_name, "—")


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


def dept_start(exposure_series, frac=.005):
    """First period a department really has a portfolio (≥ 0.5% of its peak) — no zeros before it."""
    s_ = exposure_series.fillna(0)
    if not len(s_) or s_.max() <= 0:
        return None
    hit = s_[s_ >= s_.max() * frac]
    return hit.index[0] if len(hit) else None


def _stack_text(v, share, step, i, n, min_share=10):
    return f"{share:.0f}%" if _ok(share) and share >= min_share and (i % step == 0 or i == n - 1) else ""


# ---------------------------------------------------------------- A: dynamics
def a01_portfolio(A, B, ctx):
    sel = ctx["sel"]
    piv = _piv(A["department"], "exposure")
    t = _total(A).reindex(piv.index)
    order = order_at(piv, sel)
    x = _x(piv.index)
    n, step = len(x), max(1, math.ceil(len(x) / fit(36)))
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
    t_, p_ = line_text(npl, lambda v: f"{v:.2f}%")
    f.add_scatter(x=x, y=npl, name="NPL 90+, %", yaxis="y2", mode="lines+markers+text",
                  line=dict(color=COLORS["npl"], width=3), marker=dict(size=5),
                  text=t_, textposition=p_,
                  textfont=dict(size=11, color=COLORS["npl"]),
                  hovertemplate="%{x}<br>NPL 90+: %{y:.2f}%<extra></extra>")
    f.add_scatter(x=x, y=wat, name=f"Зона риска {_wz()}, %", yaxis="y2", mode="lines",
                  line=dict(color=COLORS["watch"], width=2.2, dash="dot"),
                  hovertemplate="%{x}<br>зона риска: %{y:.2f}%<extra></extra>")
    ov = overlay(_safemax(tot), npl, wat, pct_title="NPL и зона риска, %")
    ov["yaxis"]["title"] = UNIT_NAME
    base(f, barmode="stack", bargap=.25, **ov)

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
                        "департаментам (столбцы, левая шкала), и его качество (линии, правая шкала, %).",
                legend=_dept_legend(order, shares) + [
                    (COLORS["ink"], "Число над столбцом", f"весь портфель банка, {UNIT_NAME}", "text"),
                    (COLORS["npl"], "Красная линия", "доля NPL 90+ в портфеле, %", "line"),
                    (COLORS["watch"], "Оранжевый пунктир",
                     f"зона риска: просрочка {_wz()} дней, ещё не NPL", "dot")],
                insights=ins, terms=["dates", "npl"])



def _bucket_cols(piv):
    keep = [b for b in BUCKET_ORDER if b in piv.columns]
    return keep if SHOW_CURRENT_BUCKET else [b for b in keep if b != "CUR"]


def a03_bucket_mix(A, B, ctx):
    sel = ctx["sel"]
    piv = A["bucket_mix"].pivot_table(index="period", columns="bucket",
                                      values="share", aggfunc="sum", observed=True).fillna(0) * 100
    cols = _bucket_cols(piv)
    x = _x(piv.index)
    n, step = len(x), max(1, math.ceil(len(x) / fit(36)))
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
                legend=[(BUCKET_COLORS[b], lab(b), "% всего портфеля", "bar")
                        for b in cols] +
                       [(COLORS["ink"], "Чёрная линия", "весь просроченный портфель", "line")],
                insights=ins, terms=["overdue", "pp"])


def a04_npl_departments(A, B, ctx):
    sel = ctx["sel"]
    ratio = _piv(A["department"], "npl_ratio", "mean") * 100
    amt = _piv(A["department"], "npl_exposure")
    expo = _piv(A["department"], "exposure")
    deps = dept_sorted(ratio.columns)
    for dep in deps:                                   # a new department starts where it starts
        st = dept_start(expo[dep]) if dep in expo else None
        if st is not None:
            ratio.loc[ratio.index < st, dep] = np.nan
            amt.loc[amt.index < st, dep] = np.nan
    x = _x(ratio.index)
    totn = amt.sum(axis=1)
    share = amt.div(totn.replace(0, np.nan), axis=0) * 100
    order = order_at(amt, sel)
    f = go.Figure()
    n_, step = len(x), max(1, math.ceil(len(x) / fit(36)))
    for dep in order:
        light = shades(dcolor(dep), 3)[2]
        f.add_bar(x=x, y=money(nan0(amt[dep])), name=dname(dep), marker_color=light,
                  customdata=share[dep], hovertemplate="%{x} · " + _e(dname(dep)) + "<br>NPL %{y:,.1f} " + UNIT_NAME
                                                      + " — %{customdata:.1f}% всего NPL<extra></extra>")
    lines = []
    tv0 = _total(A).reindex(ratio.index)["npl_ratio"] * 100
    for dep in deps:
        v = ratio[dep]
        lines.append(v)
        lab_ = thin(v, lambda z: f"{z:.1f}%", max_labels=fit(70))
        lab_ = [t if not (_ok(a) and _ok(b) and abs(a - b) < .4) else "" for t, a, b in zip(lab_, v, tv0)]  # bank's label wins
        f.add_scatter(x=x, y=v, name=dname(dep), yaxis="y2", mode="lines+markers+text",
                      line=dict(width=3, color=dcolor(dep)), marker=dict(size=4),
                      text=lab_, textposition="top center",
                      hovertemplate="%{x} · " + _e(dname(dep)) + "<br>NPL %{y:.2f}% своего портфеля<extra></extra>")
    tv = _total(A).reindex(ratio.index)["npl_ratio"] * 100
    t_, p_ = line_text(tv, lambda v: f"{v:.2f}%")
    f.add_scatter(x=x, y=tv, name="Банк", yaxis="y2", mode="lines+markers+text",
                  line=dict(color=COLORS["ink"], width=2, dash="dash"), marker=dict(size=4),
                  text=t_, textposition=p_, hovertemplate="%{x}<br>банк: %{y:.2f}%<extra></extra>")
    ov = overlay(_safemax(money(totn)), tv, *lines, pct_title="NPL, % своего портфеля")
    ov["yaxis"]["title"] = "NPL, " + UNIT_NAME
    ov["yaxis2"]["tickfont"]["color"] = COLORS["ink"]
    ov["yaxis2"]["title"]["font"]["color"] = COLORS["ink"]
    base(f, barmode="stack", bargap=.25, **ov)

    row = ratio.loc[sel].dropna() if sel in ratio.index else pd.Series(dtype=float)
    sh = share.loc[sel].dropna() if sel in share.index else pd.Series(dtype=float)
    ins = []
    if len(row):
        worst, best = row.idxmax(), row.idxmin()
        ins.append(f"Самый высокий NPL своего портфеля — <b>{_e(dname(worst))}</b>: {fpct(row[worst], 2)}; "
                   f"самый низкий — {_e(dname(best))}: {fpct(row[best], 2)}.")
    if len(sh):
        top_c = sh.idxmax()
        ins.append(f"Больше всего NPL банка — у <b>{_e(dname(top_c))}</b>: {fpct(sh[top_c])} всей суммы NPL "
                   f"({fnum(at(amt[top_c], sel) / UNIT)} {UNIT_NAME}).")
    if shift_p(sel, 12) in ratio.index and len(row):
        moves = (row - ratio.loc[shift_p(sel, 12)]).dropna()
        if len(moves):
            ins.append(f"Сильнее всего за год вырос NPL у {_e(dname(moves.idxmax()))}: {fpp(moves.max())}.")
    ins.append(_trend("NPL банка", tv, sel))
    return page(f, what="Столбцы — сумма NPL банка, разделённая по департаментам (левая шкала). Линии — NPL "
                        "внутри каждого департамента, % его портфеля; пунктир с цифрами — NPL банка целиком "
                        "(правая шкала).",
                legend=[(dcolor(d), _e(dname(d)), "светлый столбец — его NPL, " + UNIT_NAME
                         + "; линия — NPL % его портфеля", "line") for d in deps] +
                       [(COLORS["ink"], "Пунктир с цифрами", "NPL банка целиком, % — значение в каждом месяце", "dash")],
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
        keep = _label_idx(ncol, fit(28))
        txt = [[f"{z[r, c]:.1f}" if c in keep and np.isfinite(z[r, c]) else ""
                for c in range(ncol)] for r in range(z.shape[0])]
        f = go.Figure(go.Heatmap(
            z=z, x=x, y=part, text=txt, texttemplate="%{text}", textfont=dict(size=10),
            zmin=0, zmax=max(zmax, .1),
            colorscale=[[0, "#FFFFFF"], [.25, "#F6E3A8"], [.6, COLORS["watch"]], [1, COLORS["npl"]]],
            colorbar=dict(title="NPL, %", thickness=12, len=.8),
            xgap=1, ygap=1, hovertemplate="%{y}<br>%{x}: NPL %{z:.2f}%<extra></extra>"))
        base(f, yaxis=dict(autorange="reversed", tickfont=dict(size=11)),
             xaxis=dict(side="top", tickangle=-45 if ncol > fit(48) else 0))
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
            ("exited", COLORS["char"], "Ушли с баланса (−)", "NPL-кредиты закрыты или списаны"),
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
    vm = vm[vm["reliable"].astype(bool)]           # .astype: an empty object column would select COLUMNS
    cols = {(30, 3): "#F2C230", (30, 6): COLORS["watch"], (60, 6): "#C2591F", (90, 9): "#A33418", (90, 12): COLORS["npl"]}
    series = []
    for thr, mob in A07_MARKS:
        sr = vm[vm.metric == f"GL{thr}+@{mob}MOB"].set_index("vintage")["rate"] * 100
        if sr.notna().sum() >= 3:                      # a checkpoint with < 3 cohorts says nothing
            series.append((thr, mob, sr))
    if not series:
        raise Notice("Период слишком короткий для когорт: кредиту нужно прожить хотя бы 3 месяца внутри "
                     "выбранного периода, и таких месяцев выдачи должно быть не меньше трёх.")
    idx = sorted(set().union(*[set(sr.index) for *_, sr in series]))
    x = [vlabel(v) for v in idx]
    f = go.Figure()
    for thr, mob, sr in series:
        v = sr.reindex(idx)
        name = f"GL{thr}+@{mob}MOB"
        f.add_bar(x=x, y=v, name=name, marker_color=cols.get((thr, mob), COLORS["neutral"]),
                  text=thin(v, lambda z: f"{z:.1f}", max_labels=fit(16 if len(series) < 3 else 12)),
                  textposition="outside", textangle=-90, cliponaxis=False,
                  textfont=dict(size=10.5, color=COLORS["ink"]),
                  hovertemplate="выдача %{x}<br>" + name + ": %{y:.1f}%<extra></extra>")
    top = max(_safemax(sr) for *_, sr in series)
    base(f, barmode="group", bargap=.2, xaxis=dict(title="месяц выдачи кредита"),
         yaxis=dict(title="% кредитов когорты", range=[0, top * 1.25]))

    main = series[-1]                                  # the deepest checkpoint the window allows
    thr, mob, sr = main
    ex = sr.dropna()
    ins = [f"Пример: из 100 кредитов, выданных в {vlabel_full(ex.index[-1])}, <b>{ex.iloc[-1]:.0f}</b> хотя бы раз "
           f"ушли в просрочку больше {thr} дней за первые {mob} месяцев.",
           f"Худшая когорта по GL{thr}+@{mob}MOB — {vlabel_full(ex.idxmax())}: {fpct(ex.max())}; в среднем {fpct(ex.mean())}."]
    if len(ex) >= 6:
        a_, b_ = ex.iloc[-3:].mean(), ex.iloc[-6:-3].mean()
        ins.append(f"Последние 3 когорты — {fpct(a_)} против {fpct(b_)} у трёх предыдущих: выдачи "
                   f"{'ухудшаются' if a_ > b_ else 'улучшаются или стабильны'}.")
    skipped = [f"GL{t_}+@{m_}MOB" for t_, m_ in A07_MARKS if not any(t_ == a and m_ == b for a, b, _ in series)]
    if skipped:
        ins.append(f"{', '.join(skipped)} не показан: в выбранном периоде меньше трёх когорт дожили до этой точки.")
    if not skipped:
        ins.append("Пустое место справа — молодые когорты ещё не дожили до контрольной точки; это не ноль.")
    meaning = {(30, 3): "просрочка больше 30 дней в первые 3 месяца — самый ранний сигнал",
               (30, 6): "просрочка больше 30 дней в первые 6 месяцев",
               (90, 12): "просрочка больше 90 дней (дефолт) в первые 12 месяцев"}
    return page(f, what="Качество выдач: как ведёт себя каждая когорта — все кредиты, выданные в один месяц. "
                        "Чем ниже столбцы, тем лучше выдавали. Ранние точки (3–6 месяцев) работают даже на "
                        "коротком периоде.",
                legend=[(cols.get((t_, m_), COLORS["neutral"]), f"GL{t_}+@{m_}MOB",
                         "из 100 кредитов: " + meaning.get((t_, m_), f"просрочка больше {t_} дней за {m_} мес."), "bar")
                        for t_, m_, _ in series],
                insights=ins, terms=["gl", "cohort"])


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
                  textfont=dict(size=11, color=COLORS["good_text"]),
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
                        (COLORS["good"], "Жёлтая линия", "из 100 кредитов с просрочкой 1–30 — сколько вернулись в норму", "line")],
                insights=ins, terms=["migration"])


def a10_currency(A, B, ctx):
    sel = ctx["sel"]
    piv = _piv(A["cur_name"], "exposure")
    piv = piv.div(piv.sum(axis=1), axis=0) * 100
    order = order_at(piv, sel)
    x = _x(piv.index)
    n, step = len(x), max(1, math.ceil(len(x) / fit(36)))
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
    t_, p_ = line_text(fx, lambda v: f"{v:.1f}%")
    f.add_scatter(x=x, y=fx, yaxis="y2", mode="lines+markers+text", line=dict(color=COLORS["npl"], width=2.4),
                  marker=dict(size=4), text=t_, textposition=p_,
                  textfont=dict(size=11, color=COLORS["npl"]),
                  hovertemplate="%{x}<br>валютная часть: %{y:.2f}%<extra></extra>")
    ov = overlay(100, fx, pct_title="валютная часть, %")
    ov["yaxis"].update(title="% портфеля", range=[0, 100])
    base(f, barmode="stack", bargap=.25, **ov)
    return page(f, what="Из каких валют состоит портфель: доли внутри каждого месяца (сумма = 100%). "
                        "Красная линия — вся валютная часть на правой шкале, со значением в каждом месяце.",
                legend=[(CURRENCY_COLORS.get(c, pal[i % len(pal)]), _e(c), "доля валюты в портфеле", "bar")
                        for i, c in enumerate(order)] +
                       [(COLORS["npl"], "Красная линия", "все валюты кроме сума, % (правая шкала)", "line")],
                insights=[_trend("Валютная часть портфеля", fx, sel),
                          "Суммы в источнике уже в сумах; рост валютной части — валютный риск заёмщиков, "
                          "который возвращается к банку кредитным риском."],
                terms=["stock", "pp"])




def a13_insurance(A, B, ctx):
    sel = ctx["sel"]
    d = A["total"]
    x = _x(d["period"])
    npl, gross, watch = d.npl_ratio * 100, d.npl_ratio_gross * 100, d.watch_ratio * 100
    f = go.Figure()
    f.add_scatter(x=x, y=gross, name="NPL без страховки", mode="lines+markers+text",
                  line=dict(color=COLORS["npl"], width=2.6, dash="dash"), marker=dict(size=4),
                  text=thin(gross, lambda v: f"{v:.2f}", max_labels=fit(36)), textposition="top center",
                  textfont=dict(size=10.5, color=COLORS["npl"]),
                  hovertemplate="%{x}<br>без страховки: %{y:.2f}%<extra></extra>")
    f.add_scatter(x=x, y=npl, name="NPL фактический", mode="lines+markers+text",
                  line=dict(color=COLORS["npl"], width=3), marker=dict(size=4),
                  fill="tonexty", fillcolor="rgba(242,194,48,.35)",
                  text=thin(npl, lambda v: f"{v:.2f}"), textposition="bottom center",
                  textfont=dict(size=11, color=COLORS["npl"]),
                  hovertemplate="%{x}<br>фактический: %{y:.2f}%<extra></extra>")
    f.add_scatter(x=x, y=watch, name=f"Зона риска {_wz()}", mode="lines+markers+text",
                  line=dict(color=COLORS["watch"], width=2, dash="dot"), marker=dict(size=4),
                  text=thin(watch, lambda v: f"{v:.2f}", max_labels=fit(44)), textposition="bottom center",
                  textfont=dict(size=10.5, color="#B86E0A"),
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
        st = dept_start(piv.sum(axis=1))
        piv = piv[piv.index >= st] if st is not None else piv.iloc[0:0]   # a new department starts where it starts
        if piv.empty:
            raise ValueError(f"у департамента «{dep}» нет остатка")
        named = [c for c in order_at(piv, sel) if c != "Прочие"]
        cols = named + (["Прочие"] if "Прочие" in piv.columns else [])
        cmap = {c: PRODUCT_COLORS[i % len(PRODUCT_COLORS)] for i, c in enumerate(named)}
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
        t_, p_ = line_text(nplr, lambda v: f"{v:.1f}%")
        f.add_scatter(x=x, y=nplr, yaxis="y2", mode="lines+markers+text",
                      line=dict(color=COLORS["npl"], width=2.6), marker=dict(size=4),
                      text=t_, textposition=p_,
                      textfont=dict(size=11, color=COLORS["npl"]),
                      hovertemplate="%{x}<br>NPL департамента %{y:.2f}%<extra></extra>")
        ov = overlay(_safemax(tot), nplr, pct_title="NPL, %")
        ov["yaxis"]["title"] = UNIT_NAME
        base(f, barmode="stack", bargap=.25, **ov)

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
        leg.append((COLORS["npl"], "Красная линия", "NPL 90+ департамента, % (правая шкала)", "line"))
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
    n, step = len(x), max(1, math.ceil(len(x) / fit(36)))
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
    t_, p_ = line_text(sh, lambda v: f"{v:.1f}%")
    f.add_scatter(x=x, y=sh, yaxis="y2", mode="lines+markers+text", line=dict(color=COLORS["npl"], width=2.6),
                  marker=dict(size=4), text=t_, textposition=p_, textfont=dict(size=11, color=COLORS["npl"]),
                  hovertemplate="%{x}<br>доля в портфеле банка: %{y:.2f}%<extra></extra>")
    rel = s["rel_exp"] / s["exposure"].replace(0, np.nan) * 100 if A.get("has_rel") else None
    if rel is not None:
        t2, p2 = line_text(rel, lambda v: f"{v:.1f}%" if v > 0 else "")   # no «0.0%» row along the axis
        f.add_scatter(x=x, y=rel, yaxis="y2", mode="lines+markers+text", line=dict(color=COLORS["char"], width=2.4, dash="dash"),
                      marker=dict(size=4), text=t2, textposition=p2,
                      hovertemplate="%{x}<br>связанные: %{y:.1f}% суммы топ-50<extra></extra>")
    ov = overlay(_safemax(tot), sh, *([rel] if rel is not None else []), pct_title="%")
    ov["yaxis"]["title"] = UNIT_NAME
    base(f, barmode="stack", bargap=.25, **ov)
    ex = ", ".join(TOP_CLIENTS_EXCLUDE)
    ins = [_trend(f"Доля топ-{TOP_CLIENTS} в портфеле банка", sh, sel),
           (f"Крупнейший клиент — {fpct(at(s['top1_share'] * 100, sel), 2)} портфеля банка."
            if _ok(at(s["top1_share"], sel)) else ""),
           (f"За месяц в топ-{TOP_CLIENTS} вошли <b>{int(at(s['newcomers'], sel))}</b> новых клиентов."
            if _ok(at(s["newcomers"], sel)) else ""),
           (f"Связанные компании (aloqador) — <b>{fpct(at(rel, sel))}</b> суммы топ-{TOP_CLIENTS}, "
            f"{int(at(s['n_rel'], sel) or 0)} клиентов." if rel is not None and _ok(at(rel, sel)) else
            f"Связанные компании появятся, когда вы отметите их в файле {TOP_NAMES_FILE}.xlsx (см. {_ref(ctx, 'b08_top_table')})."),
           f"Клиенты только с кредитами {_e(ex)} в рейтинге не участвуют; у клиентов, которые есть и в {_e(ex)}, "
           f"и в других департаментах, считается весь долг."]
    return page(f, title=f"Топ-{TOP_CLIENTS} клиентов по месяцам",
                what=f"Сумма остатка {TOP_CLIENTS} крупнейших клиентов каждого месяца (столбцы, по департаментам) "
                     f"и их доля во всём портфеле банка (красная линия). Состав топ-{TOP_CLIENTS} в каждом "
                     f"месяце свой. Список на дату — на странице {_ref(ctx, 'b08_top_table')}.",
                legend=_dept_legend(order) + [
                    (COLORS["ink"], "Число над столбцом", f"сумма топ-{TOP_CLIENTS}, {UNIT_NAME}", "text"),
                    (COLORS["npl"], "Красная линия", "их доля во всём портфеле банка, % (правая шкала)", "line")]
                + ([(COLORS["char"], "Тёмный пунктир", "доля связанных компаний в сумме топ-50, %", "dash")]
                   if rel is not None else []),
                insights=ins, terms=["top"])


# ---------------------------------------------------------------- B: structure
def _hbar_height(n, per_row=20, minimum=300):
    """Horizontal bar charts always use the full height: a short list gets thicker bars, not
    an empty half-page. (n/per_row kept so callers stay readable.)"""
    return CHART_H


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
    f.add_bar(x=x, y=amt, marker_color=COLORS["neutral"], text=thin(amt, famt, max_labels=fit(36)),
              textposition="outside", cliponaxis=False, textfont=dict(size=11),
              customdata=np.stack([d["share"] * 100, d["n_loans"]], axis=-1),
              hovertemplate="выдача %{x}<br>%{y:,.1f} " + UNIT_NAME +
                            "<br>%{customdata[0]:.1f}% портфеля<br>кредитов %{customdata[1]:,}<extra></extra>")
    t_, p_ = line_text(nplr, lambda v: f"{v:.1f}%")
    f.add_scatter(x=x, y=nplr, yaxis="y2", mode="lines+markers+text", line=dict(color=COLORS["npl"], width=2.4),
                  marker=dict(size=4), text=t_, textposition=p_, textfont=dict(size=11, color=COLORS["npl"]),
                  hovertemplate="выдача %{x}<br>NPL когорты %{y:.2f}%<extra></extra>")
    ov = overlay(_safemax(amt), nplr, pct_title="NPL когорты, %")
    ov["yaxis"]["title"] = UNIT_NAME
    base(f, bargap=.2, xaxis=dict(title="месяц выдачи"), **ov)
    recent = d[d.vintage >= shift_p(sel, 11)]
    worst = d.loc[d.npl_ratio.idxmax()] if d.npl_ratio.notna().any() else None
    ins = [f"Выдачи последних 12 месяцев — <b>{fpct(recent.exposure.sum() / B['_tot_exp'] * 100)}</b> портфеля.",
           (f"Самая проблемная когорта — {vlabel_full(worst.vintage)}: NPL {fpct(worst.npl_ratio * 100)}, "
            f"остаток {fnum(worst.exposure / UNIT)} {UNIT_NAME}." if worst is not None else ""),
           "Высокий столбец с высокой красной линией — недавняя крупная выдача, которая уже портится."]
    mb = B["mob_band"]
    if len(mb):
        big = mb.loc[mb["share"].idxmax()]
        ins.append(f"По возрасту больше всего денег в кредитах {big['name']}: {big['share']:.1%} портфеля"
                   + (f"; самый высокий NPL — у {mb.loc[mb['npl_ratio'].idxmax(), 'name']} "
                      f"({fpct(mb['npl_ratio'].max() * 100, 2)})." if mb["npl_ratio"].notna().any() else "."))
    return page(f, title=f"Из выдач каких месяцев состоит портфель на {plabel_full(sel)}",
                what="Сколько денег из выдач каждого месяца ещё на балансе (столбцы) и насколько плохо ведёт себя "
                     "именно эта когорта (красная линия). Последние три года.",
                legend=[(COLORS["neutral"], "Серый столбец", f"остаток кредитов этого месяца выдачи, {UNIT_NAME}", "bar"),
                        (COLORS["npl"], "Красная линия", "NPL 90+ этой когорты, % (правая шкала)", "line")],
                insights=ins, terms=["vintage", "npl"])





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
            f"<td class='nm{' rel' if r.rel else ''}'>{_e(r.shown)}</td><td>{'●' if r.rel else ''}</td>"
            f"<td>{_e(', '.join(dname(x.strip()) for x in str(r.deps).split(',')))}</td>"
            f"<td class='n'>{fnum(r.exposure / UNIT, 2)}</td><td class='n'>{fpct(r.share, 2)}</td>"
            f"<td class='n'>{fpct(r.cum, 1)}</td>"
            f"<td class='n{' bad' if r.dpd > 90 else (' warn' if r.dpd > 0 else '')}'>{int(r.dpd)}</td></tr>"
            for _, r in rows.iterrows())
        return ("<table class='tt'><thead><tr><th>#</th><th>Δ</th><th>Клиент</th><th>св.</th><th>Деп.</th>"
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
           (f"Связанные компании (●): <b>{int(t.rel.sum())}</b> из {len(t)}, {fpct(t[t.rel].share.sum(), 1)} портфеля банка."
            if t.rel.any() else
            f"Имена и связанные компании берутся из вашего файла {TOP_NAMES_FILE}.xlsx (или .csv) рядом с папкой "
            f"данных; заготовка со всеми ID — top50_template.csv рядом с отчётом."),
           f"Клиенты только с кредитами {_e(', '.join(TOP_CLIENTS_EXCLUDE))} не участвуют; смешанные — со всем долгом."]
    return page(None, title=f"Топ-{TOP_CLIENTS} клиентов на {plabel_full(sel)}",
                what=f"Крупнейшие клиенты по сумме остатка. Δ — изменение места по сравнению с прошлым месяцем; "
                     f"«накоп.» — доля портфеля банка у клиентов с 1-го по этот; «дн.» — максимальная просрочка, дней.",
                legend=[(COLORS["good_text"], "▲ / ▼", "клиент поднялся / опустился в рейтинге", "text"),
                        (COLORS["gold"], "новый", "в прошлом месяце не был в топе", "text"),
                        (COLORS["npl"], "Красное число дней", "просрочка больше 90 дней", "text"),
                        (COLORS["good_text"], "● в «св.»", "связанная компания (aloqador) — из вашего файла", "text")],
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
    seg = {"pervichka": "pervichka<br>(новые авто)", "vtorichka": "vtorichka<br>(с пробегом)",
           "non_auto": "Прочие<br>(не авто)"}
    piv = c.pivot_table(index="avto", columns="stage", values="amount", aggfunc="sum").fillna(0)
    piv = piv.reindex([k for k in seg if k in piv.index])
    all_row = piv.sum()
    if B10_SHOW_ALL:
        piv.loc["all"] = all_row
    order = ["norm", "neofficial", "official", "writeoff"]      # bottom → top; bad on top
    stages = [s_ for s_ in order if s_ in piv.columns] + [s_ for s_ in piv.columns if s_ not in order]
    colors = dict(SUD_COLORS, writeoff=WRITE_OFF_COLOR)
    names = dict(writeoff="Списано")
    xs = [seg.get(k, f"Все кредиты<br>{_e(dname(dep))}") for k in piv.index]
    totals = piv.sum(axis=1)                                    # = the segment's portfolio
    share = piv.div(totals.replace(0, np.nan), axis=0) * 100
    f = go.Figure()
    for s_ in stages:
        v = money(piv[s_])
        col = colors.get(s_, COLORS["neutral"])
        f.add_bar(x=xs, y=v, name=names.get(s_, lab(s_)), marker_color=col,
                  text=[f"{fnum(a, 1)} · {fpct(p_)}" if _ok(p_) and p_ >= 6 else "" for a, p_ in zip(v, share[s_])],
                  textposition="inside", insidetextanchor="middle", textfont=dict(size=11, color=text_on(col)),
                  customdata=share[s_], hovertemplate="%{x}<br>" + names.get(s_, lab(s_)) + ": %{y:,.2f} "
                                                      + UNIT_NAME + " (%{customdata:.1f}%)<extra></extra>")
    short = {"writeoff": "Списано", "official": "Официальная", "neofficial": "Неофициальная"}
    for i, k in enumerate(piv.index):
        lines = [f"{short[s_]}: {fpct(share.loc[k, s_])}" for s_ in ("writeoff", "official", "neofficial")
                 if s_ in share.columns]
        if lines:
            lines[0] = f"<b>{lines[0]}</b>" if "writeoff" in share.columns else lines[0]
        f.add_annotation(x=xs[i], y=money(totals[k]), yshift=10, showarrow=False, yanchor="bottom",
                         text=f"<b>{fnum(totals[k] / UNIT, 1)}</b><br>" + "<br>".join(lines), font=dict(size=11))
    base(f, barmode="stack", bargap=.35, yaxis=dict(title=UNIT_NAME, range=[0, _safemax(money(totals)) * 1.35]))

    a_ = all_row
    tot_all = float(a_.sum())
    bad = [x for x in ("writeoff", "official", "neofficial") if x in piv.columns]
    rate = {k: piv.loc[k, bad].sum() / totals[k] * 100 for k in piv.index if k != "all" and totals[k]}
    worst = max(rate, key=rate.get) if rate else None
    ins = [(f"Весь портфель {_e(dname(dep))}: {fnum(tot_all / UNIT)} {UNIT_NAME}; из них норма — "
            f"<b>{fpct(a_.get('norm', 0) / tot_all * 100)}</b>, остальное — списано или в судебной работе."
            if tot_all else ""),
           (f"Списано: <b>{fnum(a_.get('writeoff', 0) / UNIT, 2)} {UNIT_NAME}</b> — {fpct(a_.get('writeoff', 0) / tot_all * 100)} портфеля."
            if tot_all and "writeoff" in piv.columns else ""),
           (f"Официально в суде: {fnum(a_.get('official', 0) / UNIT, 2)}, неофициально: "
            f"{fnum(a_.get('neofficial', 0) / UNIT, 2)} {UNIT_NAME}."),
           (f"Хуже всех сегмент «{seg[worst].split('<br>')[0]}»: списано или в суде {fpct(rate[worst])} его портфеля."
            if worst else "")]
    meaning = {"norm": "хорошие кредиты: без суда и без списанной части",
               "neofficial": "досудебная работа с должником (без списанной части)",
               "official": "иск подан в суд (без списанной части)",
               "writeoff": f"плохая часть долга ({WRITE_OFF_COL}) — вынесена из своей стадии первой"}
    return page(f, title=f"Автокредиты и судебная стадия, департамент {dname(dep)}, {plabel_full(sel)}",
                what=f"Портфель департамента {dname(dep)}: автокредиты на первичном и вторичном рынке, остальные "
                     "кредиты и все вместе. Сначала из каждого кредита выделена списанная часть, остаток — по "
                     "судебной стадии. Четыре цвета вместе = весь портфель сегмента.",
                legend=[(colors.get(s_, COLORS["neutral"]), names.get(s_, lab(s_)), meaning.get(s_, "стадия из данных"), "bar")
                        for s_ in reversed(stages)],
                insights=ins, terms=["court"])



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


def a00_changes(A, B, ctx):
    sel = ctx["sel"]
    prev = shift_p(sel, 1)
    if prev not in ctx["periods"]:
        raise Notice("Для сравнения месяц к месяцу нужен хотя бы один предыдущий месяц в периоде.")
    bank = B["_tot_exp"]
    T = _total(A)

    def movers(df, label_col="dim_value", hide=lambda v: False):
        d = df[~df[label_col].map(hide)]
        n = d.pivot_table(index="dim_value", columns="period", values="npl_ratio", aggfunc="mean")
        e = d.pivot_table(index="dim_value", columns="period", values="exposure", aggfunc="sum")
        if sel not in n.columns or prev not in n.columns:
            return pd.DataFrame()
        out = pd.DataFrame({"npl": n[sel] * 100, "dnpl": (n[sel] - n[prev]) * 100,
                            "exp": e[sel], "dexp": e[sel] - e[prev].fillna(0)})
        return out[out["exp"] >= bank * 0.005].dropna(subset=["dnpl"])

    br = movers(A["filial"], hide=is_no_branch)
    pr = movers(A["passport"])

    def tbl(title, rows, cols):
        head = "".join(f"<th>{c}</th>" for c in cols)
        body = "".join("<tr>" + "".join(f"<td{' class=n' if i else ''}>{c}</td>" for i, c in enumerate(r)) + "</tr>"
                       for r in rows) or f"<tr><td colspan={len(cols)}>нет данных</td></tr>"
        return f"<div><h5>{title}</h5><table class='tt chg'><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>"

    def pp_cell(v):
        cls = "bad" if v > 0 else "good"
        return f"<span class='{cls}'>{fpp(v)}</span>"

    t1 = tbl("Филиалы: сильнее всего вырос NPL", [
        (_e(k), fpct(r.npl, 2), pp_cell(r.dnpl), fnum(r.exp / UNIT)) for k, r in br.sort_values("dnpl", ascending=False).head(5).iterrows()],
        ["Филиал", "NPL", "за месяц", UNIT_NAME])
    t2 = tbl("Продукты: сильнее всего вырос NPL", [
        (_e(k), fpct(r.npl, 2), pp_cell(r.dnpl), fnum(r.exp / UNIT)) for k, r in pr.sort_values("dnpl", ascending=False).head(5).iterrows()],
        ["Продукт", "NPL", "за месяц", UNIT_NAME])
    g = br.sort_values("dexp")
    t3 = tbl("Филиалы: самое большое изменение портфеля", [
        (_e(k), f"{'+' if r.dexp >= 0 else '−'}{fnum(abs(r.dexp) / UNIT)}", fchg(r.exp, r.exp - r.dexp), fnum(r.exp / UNIT))
        for k, r in pd.concat([g.tail(3).iloc[::-1], g.head(2)]).iterrows()],
        ["Филиал", "за месяц", "в %", UNIT_NAME])
    inf = A["inflow_dep"]
    tot_inf = float(inf.sum())
    t4 = tbl(f"Новые NPL за месяц: {fnum(tot_inf / UNIT, 2)} {UNIT_NAME}", [
        (_e(dname(k)), fnum(v / UNIT, 2), fpct(v / tot_inf * 100) if tot_inf else "—")
        for k, v in sorted(inf.items(), key=lambda kv: -kv[1])], ["Департамент", UNIT_NAME, "доля"])
    html_ = f"<div class='chg-grid'>{t1}{t2}{t3}{t4}</div>"

    w = br.sort_values("dnpl", ascending=False).head(1)
    ins = [_trend("NPL банка", T["npl_ratio"] * 100, sel),
           (f"Сильнее всего ухудшился филиал <b>{_e(w.index[0])}</b>: {fpp(w.dnpl.iloc[0])} за месяц."
            if len(w) and w.dnpl.iloc[0] > 0 else "Ни у одного крупного филиала NPL за месяц не вырос."),
           (f"Новые NPL — <b>{fnum(tot_inf / UNIT, 2)} {UNIT_NAME}</b>, больше всего у {_e(dname(inf.idxmax()))} "
            f"({fpct(inf.max() / tot_inf * 100)})." if tot_inf else ""),
           f"В таблицы попадают только филиалы и продукты от 0.5% портфеля банка — мелкие колебания не шумят."]
    return page(None, title=f"Что изменилось за месяц: {plabel_full(prev)} → {plabel_full(sel)}",
                what="Главные движения последнего месяца в четырёх таблицах: где вырос NPL, где больше всего "
                     "изменился портфель и откуда пришли новые проблемные кредиты. Подробности — на страницах ниже.",
                legend=[(COLORS["npl"], "Красное изменение", "ухудшение: NPL вырос", "text"),
                        (COLORS["good_text"], "Тёмно-жёлтое изменение", "улучшение: NPL снизился", "text")],
                insights=ins, terms=["npl", "pp"], body_html=html_)


def a02_issue_repay(A, B, ctx):
    sel = ctx["sel"]
    piv = _piv(A["department"], "disbursed")
    order = order_at(piv, sel)
    x = _x(piv.index)
    tot = money(piv.sum(axis=1))
    rep_ = money(_total(A).reindex(piv.index)["repaid"])
    f = go.Figure()
    for dep in order:
        f.add_bar(x=x, y=money(nan0(piv[dep])), name=dname(dep), marker_color=dcolor(dep),
                  hovertemplate="%{x} · " + _e(dname(dep)) + "<br>выдано %{y:,.1f} " + UNIT_NAME + "<extra></extra>")
    f.add_scatter(x=x, y=tot, mode="text", text=thin(tot, famt), textposition="top center",
                  textfont=dict(size=LABEL_SIZE, color=COLORS["ink"]), hoverinfo="skip")
    t_ = thin(rep_, famt, max_labels=fit(68))
    p_ = "bottom center"
    f.add_scatter(x=x, y=rep_, name="Погашено", mode="lines+markers+text", line=dict(color=COLORS["ink"], width=2.4, dash="dot"),
                  marker=dict(size=4), text=t_, textposition=p_, textfont=dict(size=10.5, color=COLORS["ink"]),
                  hovertemplate="%{x}<br>погашено %{y:,.1f} " + UNIT_NAME + "<extra></extra>")
    base(f, barmode="stack", bargap=.25, yaxis=dict(title=UNIT_NAME, range=[0, max(_safemax(tot), _safemax(rep_)) * 1.15]))
    s = piv.sum(axis=1)
    r = _total(A)["repaid"]
    row = piv.loc[sel] if sel in piv.index else None
    ins = [f"В {plabel_full(sel)} выдано <b>{fnum(at(s, sel) / UNIT)}</b>, погашено {fnum(at(r, sel) / UNIT)} {UNIT_NAME}: "
           f"выдачи {'больше' if at(s, sel) >= at(r, sel) else 'меньше'} погашений на {fnum(abs(at(s, sel) - at(r, sel)) / UNIT)}.",
           (f"Больше всего выдал {_e(dname(row.idxmax()))}: {fpct(row.max() / row.sum() * 100)} выдач месяца."
            if row is not None and row.sum() > 0 else ""),
           f"За весь период выдано {fnum(s.sum() / UNIT)}, погашено {fnum(r.reindex(piv.index).sum() / UNIT)} {UNIT_NAME}."]
    return page(f, what="Сколько выдал каждый департамент за месяц (столбцы) и сколько клиенты вернули (пунктир). "
                        "Когда столбец выше пунктира — портфель растёт за счёт новых выдач.",
                legend=_dept_legend(order) + [(COLORS["ink"], "Число над столбцом", "всего выдано за месяц", "text"),
                                              (COLORS["ink"], "Чёрный пунктир", "погашено за месяц", "dot")],
                insights=ins, terms=["flow"])





def a_early_defaults(A, B, ctx):
    e = A["early"]
    if e.empty:
        raise Notice("Период слишком короткий: кредиту нужно прожить 3 месяца внутри выбранного периода.")
    piv = e.pivot_table(index="vintage", columns="department", values="rate", aggfunc="mean") * 100
    deps = dept_sorted(piv.columns)
    x = [vlabel(v) for v in piv.index]
    f = go.Figure()
    for dep in deps:
        v = piv[dep]
        t_, p_ = line_text(v, lambda z: f"{z:.1f}")
        f.add_scatter(x=x, y=v, name=dname(dep), mode="lines+markers+text", line=dict(color=dcolor(dep), width=2.6),
                      marker=dict(size=4), text=t_ if len(deps) <= 2 else thin(v, lambda z: f"{z:.1f}", max_labels=fit(80)),
                      textposition=p_ if len(deps) <= 2 else "top center", textfont=dict(size=10.5, color=dcolor(dep)),
                      connectgaps=False, hovertemplate="выдача %{x} · " + _e(dname(dep)) + "<br>%{y:.1f}% ушли в 30+<extra></extra>")
    base(f, xaxis=dict(title="месяц выдачи"), yaxis=dict(title="% выдач с просрочкой 30+ за 3 месяца", rangemode="tozero"))
    ins = []
    for dep in deps:
        s_ = piv[dep].dropna()
        if len(s_) >= 6:
            a_, b_ = s_.iloc[-3:].mean(), s_.iloc[-6:-3].mean()
            ins.append(f"{_e(dname(dep))}: последние 3 месяца выдач — <b>{fpct(a_)}</b> (до этого {fpct(b_)}) — "
                       f"{'хуже' if a_ > b_ else 'лучше или так же'}.")
    missing = [dname(x) for x in ctx.get("departments", []) if x not in piv.columns]
    ins.append(f"Месяцы, где выдано меньше {MIN_COHORT} кредитов, не показаны — там проценты случайны"
               + (f"; поэтому нет линии {_e(', '.join(missing))} (мало выдач в месяц)." if missing else "."))
    return page(f, what="Самый ранний сигнал качества выдач: из кредитов, выданных в месяц, — какая доля уже в первые "
                        "3 месяца допустила просрочку больше 30 дней. Растёт линия — стали выдавать хуже. "
                        "Опережает NPL на 6–9 месяцев.",
                legend=[(dcolor(d), _e(dname(d)), "% выдач департамента с ранней просрочкой", "line") for d in deps],
                insights=ins, terms=["cohort"])


def a12_reserves(A, B, ctx):
    sel = ctx["sel"]
    d = A["total"]
    x = _x(d["period"])
    npl, res = money(d["npl_exposure"]), money(d["reserve"])
    cov = d["coverage"] * 100
    f = go.Figure()
    f.add_bar(x=x, y=npl, name="NPL 90+", marker_color=COLORS["npl"],
              text=thin(npl, famt, max_labels=fit(16)), textposition="outside", textangle=-90, cliponaxis=False,
              textfont=dict(size=10.5, color=COLORS["npl"]),
              hovertemplate="%{x}<br>NPL %{y:,.1f} " + UNIT_NAME + "<extra></extra>")
    f.add_bar(x=x, y=res, name="Резервы", marker_color=COLORS["good"],
              text=thin(res, famt, max_labels=fit(16)), textposition="outside", textangle=-90, cliponaxis=False,
              textfont=dict(size=10.5, color=COLORS["good_text"]),
              hovertemplate="%{x}<br>резервы %{y:,.1f} " + UNIT_NAME + "<extra></extra>")
    t_, p_ = line_text(cov, lambda v: f"{v:.0f}%")
    f.add_scatter(x=x, y=cov, name="Покрытие", yaxis="y2", mode="lines+markers+text",
                  line=dict(color=COLORS["ink"], width=2.4), marker=dict(size=4), text=t_, textposition=p_,
                  hovertemplate="%{x}<br>покрытие %{y:.0f}%<extra></extra>")
    ov = overlay(max(_safemax(npl), _safemax(res)) * 1.15, cov, pct_title="покрытие, %")
    ov["yaxis"]["title"] = UNIT_NAME
    ov["yaxis2"]["tickfont"] = dict(size=11, color=COLORS["ink"])
    ov["yaxis2"]["title"]["font"]["color"] = COLORS["ink"]
    base(f, barmode="group", bargap=.25, bargroupgap=.05, **ov)
    s = d.set_index("period")
    ins = [_trend("Покрытие NPL резервами", s["coverage"] * 100, sel, dec=0),
           f"На {plabel_full(sel)}: NPL {fnum(at(s['npl_exposure'], sel) / UNIT)}, резервы {fnum(at(s['reserve'], sel) / UNIT)} {UNIT_NAME}.",
           ("Жёлтый столбец ниже красного: резервов меньше, чем проблемного долга — часть потерь ещё не признана."
            if _ok(at(s["coverage"], sel)) and at(s["coverage"], sel) < 1 else
            "Резервы покрывают NPL полностью."),
           f"Судебная работа — на странице {_ref(ctx, 'b10_auto_court')}."]
    return page(f, what="Хватает ли резервов на проблемный долг: красный столбец — NPL, жёлтый — созданные резервы, "
                        "чёрная линия — покрытие (резервы / NPL) на правой шкале.",
                legend=[(COLORS["npl"], "Красный", "NPL 90+, " + UNIT_NAME, "bar"),
                        (COLORS["good"], "Жёлтый", "резервы, " + UNIT_NAME, "bar"),
                        (COLORS["ink"], "Чёрная линия", "покрытие = резервы / NPL, % (правая шкала)", "line")],
                insights=ins, terms=["coverage"])


def b_products(A, B, ctx):
    sel = ctx["sel"]
    d = B["passport_dep"].copy()
    deps = dept_sorted(d["department"].dropna().unique())
    g = pd.concat([d[d.department == dep].nlargest(TOP_PER_DEPT, "exposure") for dep in deps]) if deps else d.iloc[0:0]
    g = g.assign(tag=g["passport"].astype(str) + "  ·  " + g["department"].map(dname))
    order = list(g["tag"])
    f = go.Figure()
    for dep in deps:
        sub = g[g.department == dep]
        f.add_bar(x=money(sub.exposure), y=sub["tag"], orientation="h", name=dname(dep), marker_color=dcolor(dep),
                  text=[f"  {fnum(v / UNIT, 1)} · {sh:.1%} · NPL {fpct(n * 100)}" for v, sh, n in zip(sub.exposure, sub.share, sub.npl_ratio)],
                  textposition="outside", cliponaxis=False, textfont=dict(size=11),
                  customdata=np.stack([sub["n_loans"], sub["share"] * 100], axis=-1),
                  hovertemplate="<b>%{y}</b><br>%{x:,.1f} " + UNIT_NAME +
                                "<br>кредитов %{customdata[0]:,}<br>%{customdata[1]:.1f}% портфеля банка<extra></extra>")
    base(f, margin=dict(r=210), xaxis=dict(title=UNIT_NAME),
         yaxis=dict(categoryorder="array", categoryarray=list(reversed(order)), tickfont=dict(size=11)))
    bank_npl = B["_tot_npl"] / B["_tot_exp"] * 100 if B["_tot_exp"] else np.nan
    ins = []
    for dep in deps:
        sub = g[g.department == dep]
        if len(sub):
            r = sub.iloc[0]
            ins.append(f"{_e(dname(dep))}: <b>{_e(r.passport)}</b> — {fnum(r.exposure / UNIT)} {UNIT_NAME}, NPL {fpct(r.npl_ratio * 100)}.")
    risky = g[g.npl_ratio * 100 > bank_npl] if _ok(bank_npl) else g.iloc[0:0]
    if len(risky):
        ins.append(f"NPL выше банка ({fpct(bank_npl, 2)}): " + _e(", ".join(risky.sort_values("npl_ratio", ascending=False)["passport"].head(4))) + ".")
    return page(f, title=f"Крупнейшие продукты каждого департамента, {plabel_full(sel)}",
                what=f"До {TOP_PER_DEPT} крупнейших продуктов каждого департамента на одном графике, в порядке "
                     + ", ".join(dname(x) for x in deps) + ". Подпись: сумма · доля портфеля банка · NPL продукта.",
                legend=_dept_legend(deps) + [(COLORS["ink"], "Подпись справа", f"{UNIT_NAME} · % портфеля банка · NPL", "text")],
                insights=ins, terms=["npl"])


def b_branch_map(A, B, ctx):
    sel = ctx["sel"]
    d = B["branch_map"]
    d = d[~d["name"].map(is_no_branch)].dropna(subset=["npl_ratio", "npl_then"])
    if d.empty:
        raise Notice("Для карты филиалов нужен хотя бы один более ранний месяц.")
    # rank: portfolio and NPL % together = the NPL money a branch carries; 1 = the best, the last = the worst
    d = d.sort_values(["npl_exposure", "npl_ratio"]).assign(num=lambda z: range(1, len(z) + 1))
    b0 = B["branch_map_base"]
    x, y = d["npl_ratio"] * 100, (d["npl_ratio"] - d["npl_then"]) * 100
    size = 20 + 14 * np.sqrt(d["exposure"] / d["exposure"].max())       # small enough to stay apart
    bank = B["_tot_npl"] / B["_tot_exp"] * 100 if B["_tot_exp"] else np.nan
    ncol = max(1, math.ceil(len(d) / 22))
    list_w = 210 * ncol
    f = go.Figure()
    for dep in dept_sorted(d["dep"].dropna().unique()):
        m = d["dep"] == dep
        f.add_scatter(x=x[m], y=y[m], mode="markers+text", name=dname(dep), text=d["num"][m].astype(str),
                      hovertext=d["name"][m], textposition="middle center", textfont=dict(size=10.5, color="white"),
                      marker=dict(size=size[m], color=dcolor(dep), opacity=.9, line=dict(color="white", width=1.5)),
                      customdata=np.stack([money(d["exposure"][m])], axis=-1),
                      hovertemplate="<b>%{hovertext}</b><br>NPL %{x:.2f}%<br>изменение %{y:+.2f} п.п.<br>%{customdata[0]:,.1f} "
                                    + UNIT_NAME + "<extra></extra>")
    if _ok(bank):
        f.add_vline(x=bank, line=dict(color=COLORS["ink"], width=1, dash="dash"),
                    annotation_text=f"NPL банка {bank:.2f}%", annotation_position="top", annotation_font_size=11)
    f.add_hline(y=0, line=dict(color=COLORS["neutral"], width=1))
    xr, yr = [0, _safemax(x) * 1.12], [min(float(y.min()), 0) * 1.15 - .5, max(float(y.max()), 0) * 1.15 + .5]
    f.add_annotation(x=xr[1], y=yr[1], text="плохо и ухудшается", showarrow=False, xanchor="right", yanchor="top",
                     font=dict(size=12, color=COLORS["npl"]))
    f.add_annotation(x=xr[0], y=yr[0], text="хорошо и улучшается", showarrow=False, xanchor="left", yanchor="bottom",
                     font=dict(size=12, color=COLORS["good_text"]))
    base(f, width=CHART_W - list_w - 10, xaxis=dict(title=f"NPL 90+ филиала на {plabel_full(sel)}, %", range=xr,
                                                   showgrid=True, gridcolor="#EFECE4"),
         yaxis=dict(title=f"изменение с {plabel_full(b0)}, п.п.", range=yr))
    rows = "".join(f"<li><b style='background:{dcolor(r.dep)}'>{r.num}</b><span>{_e(r.name)}</span>"
                   f"<em>{fpct(r.npl_ratio * 100)} · {'+' if yy >= 0 else ''}{yy:.1f} · {fnum(r.npl_exposure / UNIT, 1)}</em></li>"
                   for r, yy in zip(d.itertuples(), y))
    plot = f.to_html(full_html=False, include_plotlyjs=False, config=PCFG,
                     default_width=f"{CHART_W - list_w - 10}px", default_height=f"{CHART_H}px")
    html_ = f"<div class='bm'>{plot}<ol class='bm-list' style='width:{list_w}px;columns:{ncol}'>{rows}</ol></div>"
    hot = d[(x > bank) & (y > 0)] if _ok(bank) else d.iloc[0:0]
    ins = [(f"В зоне «плохо и ухудшается» — <b>{len(hot)}</b> из {len(d)} филиалов: " +
            _e(", ".join(f"{r.num} {r.name}" for r in hot.head(5).itertuples())) + "." if len(hot) else
            "Ни один филиал не находится одновременно выше NPL банка и в ухудшении."),
           f"Сильнее всего ухудшился {_e(d.loc[y.idxmax(), 'name'])}: {fpp(y.max())}." if y.max() > 0 else "",
           f"Сильнее всего улучшился {_e(d.loc[y.idxmin(), 'name'])}: {fpp(y.min())}." if y.min() < 0 else "",
           "Номер — место филиала от лучшего к худшему по сумме NPL (портфель × доля NPL): 1 — лучший; "
           "в списке справа: NPL % · изменение, п.п. · NPL, " + UNIT_NAME + "."]
    return page(None, title=f"Карта филиалов: уровень NPL и его изменение, {plabel_full(sel)}",
                what=f"Каждый круг — филиал, номер — его место от лучшего к худшему по сумме NPL. Вправо — выше NPL сейчас, вверх — сильнее "
                     f"рост NPL с {plabel_full(b0)}. Пунктир — NPL банка. Правый верхний угол — первые на разбор.",
                legend=_dept_legend(dept_sorted(d["dep"].dropna().unique())) +
                       [(COLORS["ink"], "Список справа", "номер · филиал · NPL % · изменение, п.п. · NPL, " + UNIT_NAME, "text")],
                insights=ins, terms=["npl", "pp"], body_html=html_)


def b_migration_matrix(A, B, ctx):
    sel = ctx["sel"]
    frm = shift_p(sel, 1)
    tr = A["transitions"]
    t = tr[tr["period"] == frm]
    if t.empty:
        raise Notice("Для матрицы миграции нужен предыдущий месяц в периоде.")
    rows = [b for b in MIGRATION_ORDER if b != "EXIT" and b in set(t["from_b"])]
    cols = [b for b in MIGRATION_ORDER if b in set(t["to_b"])]
    piv = t.pivot_table(index="from_b", columns="to_b", values="rate", aggfunc="sum").reindex(index=rows, columns=cols).fillna(0) * 100
    n = t.groupby("from_b")["n"].sum().reindex(rows)
    z = piv.to_numpy(dtype=float)
    txt = [[f"{v:.1f}" if v >= .05 else "" for v in r] for r in z]
    f = go.Figure(go.Heatmap(z=z, x=[lab(c) for c in cols], y=[f"{lab(r)} ({int(n[r]):,})".replace(",", " ") for r in rows],
                             text=txt, texttemplate="%{text}", textfont=dict(size=12), xgap=2, ygap=2, zmin=0, zmax=100,
                             colorscale=[[0, "#FFFFFF"], [.15, "#F6E3A8"], [.5, COLORS["watch"]], [1, COLORS["npl"]]],
                             colorbar=dict(title="%", thickness=12),
                             hovertemplate="из %{y}<br>в %{x}: %{z:.1f}%<extra></extra>"))
    base(f, xaxis=dict(title=f"где кредит оказался на {plabel_full(sel)}", side="top"),
         yaxis=dict(title=f"где кредит был на {plabel_full(frm)} (кредитов)", autorange="reversed"))

    def rate(a_, b_list):
        return float(piv.loc[a_, [b for b in b_list if b in piv.columns]].sum()) if a_ in piv.index else np.nan
    ins = [(f"Из корзины 1–30: <b>{fpct(rate('B01_30', ['CUR']))}</b> вернулись в норму, "
            f"{fpct(rate('B01_30', ['B31_60']))} ушли глубже." if "B01_30" in piv.index else ""),
           (f"Из корзины 61–90: <b>{fpct(rate('B61_90', DEFAULT_BUCKETS))}</b> ушли в 90+ за один месяц." if "B61_90" in piv.index else ""),
           (f"Без просрочки остались {fpct(rate('CUR', ['CUR']))} хороших кредитов; "
            f"{fpct(rate('CUR', ['B01_30']))} впервые опоздали." if "CUR" in piv.index else ""),
           "Диагональ — кредиты, оставшиеся в своей корзине; правее диагонали — ухудшение, левее — выздоровление."]
    return page(f, title=f"Матрица миграции: {plabel_full(frm)} → {plabel_full(sel)}",
                what="Куда перешёл каждый кредит за последний месяц. Строка — корзина просрочки месяц назад, столбец — "
                     "сейчас, число — % кредитов строки. Строка в сумме даёт 100%.",
                legend=[("#FFFFFF", "Белый", "почти никто не перешёл", "bar"),
                        (COLORS["watch"], "Оранжевый", "заметная доля", "bar"),
                        (COLORS["npl"], "Красный", "большинство кредитов строки", "bar")],
                insights=ins, terms=["migration"])


def b_client_icons(A, B, ctx):
    sel = ctx["sel"]
    st = B["client_status"]
    if st.empty:
        raise ValueError("нет клиентов на дату")
    deps = dept_sorted(st.index)
    colors = {"ok": COLORS["good"], "late": COLORS["watch"], "npl": COLORS["npl"]}
    words = {"ok": "платят вовремя", "late": "с просрочкой 1–90 дней", "npl": "в NPL 90+"}
    person = ("<svg viewBox='0 0 20 20' width='19' height='19'><circle cx='10' cy='5' r='3.7' fill='{c}'/>"
              "<path d='M3.2 19.5c0-4.6 3-7.8 6.8-7.8s6.8 3.2 6.8 7.8z' fill='{c}'/></svg>")
    building = ("<svg viewBox='0 0 20 20' width='19' height='19'><path d='M2.5 19.5V3.5l8-2v18zM11.5 19.5V7.5h6v12z' fill='{c}'/>"
                "<g fill='#fff'><rect x='4.6' y='5.5' width='1.7' height='1.7'/><rect x='7.6' y='5.5' width='1.7' height='1.7'/>"
                "<rect x='4.6' y='9.5' width='1.7' height='1.7'/><rect x='7.6' y='9.5' width='1.7' height='1.7'/>"
                "<rect x='4.6' y='13.5' width='1.7' height='1.7'/><rect x='7.6' y='13.5' width='1.7' height='1.7'/>"
                "<rect x='13.4' y='10' width='1.6' height='1.6'/><rect x='13.4' y='14' width='1.6' height='1.6'/></g></svg>")

    def hundred(counts):
        """Largest-remainder rounding: the icons always add up to exactly 100."""
        tot = sum(counts.values()) or 1
        raw = {k: v * 100 / tot for k, v in counts.items()}
        out = {k: int(v) for k, v in raw.items()}
        for k in sorted(raw, key=lambda k: raw[k] - out[k], reverse=True)[:100 - sum(out.values())]:
            out[k] += 1
        return out, raw

    shop = ("<svg viewBox='0 0 20 20' width='19' height='19'><path d='M2.5 9h15v10.5h-15z' fill='{c}'/>"
            "<path d='M1 3.5h18l-1.3 5.5H2.3z' fill='{c}'/><path d='M6.5 3.5 5.6 9M10 3.5V9M13.5 3.5l.9 5.5' "
            "stroke='#fff' stroke-width='1'/><rect x='8.2' y='12.5' width='3.6' height='7' fill='#fff'/></svg>")
    card = ("<svg viewBox='0 0 20 20' width='19' height='19'><rect x='1' y='4' width='18' height='12.5' rx='2' fill='{c}'/>"
            "<rect x='1' y='6.8' width='18' height='2.4' fill='#fff' opacity='.9'/>"
            "<rect x='3' y='11.6' width='5.5' height='2.2' rx='.6' fill='#fff' opacity='.9'/></svg>")
    shapes = {"person": person, "building": building, "shop": shop, "card": card}
    blocks, ins = [], []
    for dep in deps:
        counts = {k: int(st.loc[dep].get(k, 0)) for k in ("ok", "late", "npl")}
        icons, raw = hundred(counts)
        shape = shapes.get(DEPT_ICONS.get(dkey(dep), "building"), building)
        cells = "".join(shape.format(c=colors[k]) for k in ("ok", "late", "npl") for _ in range(icons[k]))
        cap = "".join(f"<div><i style='background:{colors[k]}'></i><b>{icons[k] if icons[k] or not counts[k] else '&lt;1'}</b> "
                      f"{words[k]}</div>" for k in ("ok", "late", "npl"))
        total = sum(counts.values())
        about = DEPT_ABOUT.get(dkey(dep))
        blocks.append(f"<div class='ic'><h5>{_e(dname(dep))}{' — ' + _e(about) if about else ''} <span>· {total:,}</span></h5>"
                      f"<div class='ic-grid'>{cells}</div><div class='ic-cap'>{cap}</div></div>".replace(",", " "))
        ins.append(f"{_e(dname(dep))}: из 100 клиентов <b>{icons['npl']}</b> в NPL и {icons['late']} с просрочкой "
                   f"(точно: {raw['npl']:.1f}% и {raw['late']:.1f}%).")
    html_ = f"<div class='ic-row'>{''.join(blocks)}</div>"
    ins.append("Клиент считается по своему худшему кредиту; клиент двух департаментов есть в обоих.")
    return page(None, title=f"Из каждых 100 клиентов: кто платит, кто опаздывает, {plabel_full(sel)}",
                what="Каждый значок — 1% клиентов департамента: человек — физлица, здание — корпоративные, "
                     "магазин — малый бизнес, карта — онлайн-кредиты. Цвет — состояние худшего кредита клиента на дату.",
                legend=[(colors[k], {"ok": "Платят вовремя", "late": "С просрочкой 1–90 дней",
                                     "npl": "В NPL 90+"}[k], {"ok": "ни одного дня просрочки",
                                                            "late": "просрочка, но ещё не NPL",
                                                            "npl": "хотя бы один кредит в NPL"}[k], "bar")
                        for k in ("ok", "late", "npl")],
                insights=ins, terms=["npl"], body_html=html_)


def b_reserve_norms(A, B, ctx):
    sel = ctx["sel"]
    d = B["reserve_cat"].sort_values("kat")
    if d.empty:
        raise ValueError("нет категорий качества на дату")
    # base = ON-BALANCE debt (brutto_summa): the written-off part is off balance and needs no reserve
    gone = d[d["on_balance"] <= 0]                 # e.g. category 5 this month: all of it written off
    d = d[d["on_balance"] > 0]
    if d.empty:
        raise ValueError("нет долга на балансе на дату")
    d = d.assign(rate=d["reserve"] / d["on_balance"] * 100, need=d["kat"].map(RESERVE_MIN))
    names = [f"{int(k)} · {CATEGORY_NAMES.get(int(k), k)}" for k in d["kat"]]
    ok = d["rate"] >= d["need"] - 1e-9
    # the scale follows categories 1–4; category 5 (100%) is drawn to the top, hatched, its value written
    small = d[d["kat"] < 5]
    top = max(_safemax(small["rate"]), _safemax(small["need"])) * 1.55 if len(small) else 110
    cut = d["rate"] > top * .92
    shown = np.where(cut, top * .92, d["rate"])
    f = go.Figure()
    f.add_bar(x=names, y=shown, marker=dict(color=[COLORS["good"] if o else COLORS["watch"] for o in ok],
                                            pattern=dict(shape=["/" if c_ else "" for c_ in cut], fgcolor="white")),
              customdata=d["rate"], hovertemplate="%{x}<br>резерв %{customdata:.1f}% от долга на балансе<extra></extra>")
    for nm, r, n_, b_, c_, y_ in zip(names, d["rate"], d["need"], d["on_balance"], cut, shown):
        f.add_annotation(x=nm, y=y_, yshift=4, yanchor="bottom", showarrow=False, font=dict(size=11),
                         text=f"<b>{fpct(r)}</b>{' ↑' if c_ else ''} · мин. {int(n_)}%<br>на балансе {fnum(b_ / UNIT, 1)} {UNIT_NAME}")
    keep = ~cut
    f.add_scatter(x=[n for n, k in zip(names, keep) if k], y=d["need"][keep.to_numpy()], mode="markers", hoverinfo="skip",
                  marker=dict(symbol="line-ew-open", size=70, color=COLORS["ink"], line=dict(width=3, color=COLORS["ink"])))
    wsum = float(B["reserve_cat"]["writeoff"].sum())
    base(f, bargap=.45, yaxis=dict(title="резерв, % от долга на балансе", range=[0, top], ticksuffix="%"))
    short = d[~ok]
    ins = [(f"Ниже минимума: " + "; ".join(f"<b>{CATEGORY_NAMES.get(int(r.kat))}</b> — {fpct(r.rate)} при {int(r.need)}%"
                                        for r in short.itertuples()) + "." if len(short) else
            "Во всех категориях резерв не ниже минимальной ставки."),
           "Залог законно уменьшает требуемый резерв (Положение ЦБ № 3937), поэтому «ниже минимума» — повод "
           "проверить залоги, а не обязательно нарушение.",
           (f"Не показано: {', '.join(CATEGORY_NAMES.get(int(k), str(k)) for k in gone['kat'])} — на дату на балансе "
            "ничего нет (всё списано)." if len(gone) else ""),
           (f"Списано (spisat_95413_summa): {fnum(wsum / UNIT, 2)} {UNIT_NAME} — за балансом, резерв на него "
            "не создаётся, поэтому в процентах резерва не участвует." if wsum > 0 else ""),
           ("Столбец со штриховкой и ↑ обрезан, чтобы не сжимать остальные: его значение подписано." if cut.any() else "")]
    return page(f, title=f"Резервы против минимума ЦБ (№ 3937), {plabel_full(sel)}",
                what="Резерв как % от долга НА БАЛАНСЕ (brutto_summa) в каждой категории качества и минимальная "
                     "ставка Положения ЦБ № 3937 до учёта залога (чёрная черта): 1 / 10 / 25 / 50 / 100%. "
                     "Списанная часть за балансом в расчёт не входит.",
                legend=[(COLORS["good"], "Жёлтый", "резерв не ниже минимальной ставки", "bar"),
                        (COLORS["watch"], "Оранжевый", "ниже минимума — проверить залоги", "bar"),
                        (COLORS["ink"], "Черта", "минимальная ставка резерва категории", "line")],
                insights=ins, terms=["coverage"])


def b_large_exposures(A, B, ctx):
    sel = ctx["sel"]
    d = B["borrowers"].copy()
    d["pct"] = d["exposure"] / TIER1_CAPITAL * 100
    d["label"] = [f"клиент {int(c)}" if oe else str(n) for c, n, oe in zip(d["contragent"], d["name"], d["only_ex"])]
    d = d.iloc[::-1]
    f = go.Figure()
    f.add_bar(x=d["pct"], y=d["label"], orientation="h",
              marker_color=[COLORS["npl"] if v > LARGE_LIMIT else (COLORS["watch"] if v >= LARGE_FROM else COLORS["neutral"]) for v in d["pct"]],
              text=[f"  {fpct(v)} · {fnum(e / UNIT, 1)} {UNIT_NAME}" for v, e in zip(d["pct"], d["exposure"])],
              textposition="outside", cliponaxis=False, textfont=dict(size=11),
              hovertemplate="%{y}<br>%{x:.1f}% капитала I уровня<extra></extra>")
    for v, t in ((LARGE_FROM, f"{LARGE_FROM}% — крупный риск"), (LARGE_LIMIT, f"{LARGE_LIMIT}% — предел")):
        f.add_vline(x=v, line=dict(color=COLORS["ink"] if v == LARGE_LIMIT else COLORS["watch"], width=1.4, dash="dash"),
                    annotation_text=t, annotation_position="top", annotation_font_size=11)
    base(f, margin=dict(r=170), xaxis=dict(title="% капитала I уровня", range=[0, max(_safemax(d["pct"]), LARGE_LIMIT) * 1.2]))
    large = d[d["pct"] >= LARGE_FROM]
    ins = [f"Крупных рисков (от {LARGE_FROM}% капитала): <b>{len(large)}</b>, вместе {fpct(large.pct.sum())} капитала "
           f"(предел суммы — 500%).",
           (f"Выше предела {LARGE_LIMIT}%: " + _e(", ".join(d[d.pct > LARGE_LIMIT]["label"])) + "." if (d.pct > LARGE_LIMIT).any()
            else f"Ни один заёмщик не превышает {LARGE_LIMIT}% капитала."),
           "Считается по отдельному клиенту; группы связанных заёмщиков, гарантии и забалансовые обязательства "
           "здесь не учтены — для них нужны данные, которых нет в выгрузке."]
    return page(f, title=f"Крупнейшие заёмщики против лимитов ЦБ (№ 3283), {plabel_full(sel)}",
                what=f"20 крупнейших заёмщиков как доля капитала I уровня ({fnum(TIER1_CAPITAL / UNIT, 0)} {UNIT_NAME}, "
                     "из НАСТРОЕК). Один заёмщик — не больше 25%; от 10% риск считается крупным.",
                legend=[(COLORS["neutral"], "Серый", f"меньше {LARGE_FROM}%", "bar"),
                        (COLORS["watch"], "Оранжевый", f"крупный риск: {LARGE_FROM}–{LARGE_LIMIT}%", "bar"),
                        (COLORS["npl"], "Красный", f"выше предела {LARGE_LIMIT}%", "bar")],
                insights=ins, terms=["top"])


def q_data_check(A, B, ctx):
    """Appendix: is the data itself sound, month by month? Catches the month that "looks low"."""
    q = A["quality"].merge(A["total"][["period", "exposure", "npl_ratio"]], on="period", how="left").sort_values("period")
    ex = q["exposure"]
    nb = (ex.shift(1) + ex.shift(-1)) / 2                     # the neighbours' average
    q["jump"] = (ex / nb - 1) * 100
    def row(r):
        flag = []
        if r.badnum:
            flag.append(f"{int(r.badnum):,} строк с нечитаемой суммой".replace(",", " "))
        if r.baddate:
            flag.append(f"{int(r.baddate):,} без даты выдачи".replace(",", " "))
        if _ok(r.jump) and abs(r.jump) >= 15:
            flag.append(f"портфель {r.jump:+.0f}% к соседним месяцам")
        cls = " class='bad'" if flag else ""
        return (f"<tr{cls}><td>{plabel_full(r.period)}</td><td class='n'>{int(r.rows):,}</td><td class='n'>{int(r.loans):,}</td>"
                f"<td class='n'>{fnum(r.exposure / UNIT)}</td><td class='n'>{fpct(r.npl_ratio * 100, 2)}</td>"
                f"<td class='n'>{int(r.products)}</td><td>{_e('; '.join(flag)) or '—'}</td></tr>").replace(",", " ")
    head = ("<table class='tt chg qc'><thead><tr><th>Дата</th><th>строк</th><th>кредитов</th><th>" + UNIT_NAME +
            "</th><th>NPL</th><th>прод.</th><th>замечания</th></tr></thead><tbody>")
    recs = list(q.itertuples())
    halves = chunks(recs, math.ceil(len(recs) / 2)) if len(recs) > 22 else [recs]
    t1 = "".join(head + "".join(row(r) for r in h_) + "</tbody></table>" for h_ in halves)
    merges = ctx.get("merges", {})
    mrows = "".join(f"<tr><td>{_e({'passport': 'продукт', 'filial': 'филиал', 'department': 'департамент'}.get(c, c))}</td>"
                    f"<td>{_e(main)}</td><td>{_e(' | '.join(f'{v} ({n:,})'.replace(',', ' ') for v, n in var.items()))}</td></tr>"
                    for c, m in merges.items() for main, var in m.items())
    t2 = ("<table class='tt chg'><thead><tr><th>Поле</th><th>Принято как</th><th>Найденные написания (строк)</th></tr></thead>"
          f"<tbody>{mrows or '<tr><td colspan=3>разных написаний одного имени не найдено</td></tr>'}</tbody></table>")
    files = ctx.get("files", [])
    frows = "".join(f"<tr><td>{_e(f_['file'])}</td><td class='n'>{f_['rows']:,}</td><td class='n'>{f_['bad_report_date']:,}</td>"
                    f"<td>{f_['first'].date() if pd.notna(f_['first']) else '—'} … {f_['last'].date() if pd.notna(f_['last']) else '—'}</td></tr>"
                    .replace(",", " ") for f_ in files)
    t3 = ("<table class='tt chg'><thead><tr><th>Файл</th><th>строк</th><th>без report_date</th><th>report_date</th></tr></thead>"
          f"<tbody>{frows}</tbody></table>")
    html_ = (f"<div class='qc-wrap'><div class='qc-months'><h5>По месяцам</h5><div class='qc-two'>{t1}</div></div>"
             f"<div class='qc-side'><h5>Прочитанные файлы</h5>{t3}<h5 style='margin-top:8px'>Объединённые написания</h5>{t2}</div></div>")
    bad = q[(q.badnum > 0) | (q.baddate > 0) | (q.jump.abs() >= 15)]
    ins = [(f"Месяцы с замечаниями: <b>{_e(', '.join(plabel_full(p_) for p_ in bad.period))}</b> — проверьте выгрузку за них."
            if len(bad) else "Замечаний нет: все суммы и даты прочитаны, резких скачков портфеля нет."),
           (f"Объединено разных написаний одного имени: {sum(len(m) for m in merges.values())}. Без этого один продукт "
            "выглядел бы двумя (другой цвет, часть уходит в «Прочие»)." if any(merges.values()) else ""),
           "Скачок ±15% к соседним месяцам — не обязательно ошибка, но такой месяц стоит сверить с балансом."]
    return page(None, title="Проверка данных", what="Служебная страница: всё ли прочитано из файлов. Месяц с нечитаемыми "
                "суммами или датами, или с резким скачком портфеля, выделен красным — графики за него стоит перепроверить.",
                legend=[(COLORS["npl"], "Красная строка", "месяц с замечаниями", "text")], insights=ins, body_html=html_)


# ---------------------------------------------------------------- registry
CHARTS_A_BASE = [
    ("СТОК", "Портфель и качество по отчётным датам", a01_portfolio),
    ("ПОТОК", "Выдачи по департаментам и погашения", a02_issue_repay),
    ("СТОК", "Структура просрочки по месяцам", a03_bucket_mix),
    ("СТОК", "Доля NPL 90+ по департаментам", a04_npl_departments),
    ("СТОК", "Доля NPL 90+ по филиалам и месяцам", a05_branch_heatmap),
    ("ПОТОК", "Почему изменился NPL", a06_bridge),
    ("КОГОРТЫ", "Качество выдач по месяцу выдачи", a07_vintage_quality),
    ("КОГОРТЫ", "Ранние дефолты по департаментам", a_early_defaults),
    ("ПОТОК", "Скорость ухода в дефолт", a09_migration),
    ("СТОК", "Доля валют в портфеле", a10_currency),
    ("СТОК", "Резервы против NPL", a12_reserves),
    ("СТОК", "Эффект страхового покрытия", a13_insurance),
]

CHARTS_B_BASE = [
    ("СРЕЗ", "Портфель по филиалам и департаментам", b01_dep_filial),
    ("СРЕЗ", "Просроченный портфель по корзинам", b02_buckets),
    ("СРЕЗ", "Из выдач каких месяцев состоит портфель", b03_vintage_mix),
    ("СРЕЗ", "Крупнейшие продукты каждого департамента", b_products),
    ("СРЕЗ", "Структура просрочки внутри филиала", b07_filial_bucket),
    ("ТАБЛИЦА", "Топ клиентов на дату", b08_top_table),
    ("СРЕЗ", "Кто формирует общий NPL банка", b09_npl_contribution),
    ("СРЕЗ", "Матрица миграции", b_migration_matrix),
    ("СРЕЗ", "Автокредиты и судебная стадия", b10_auto_court),
    ("СРЕЗ", "Из каждых 100 клиентов", b_client_icons),
    ("СРЕЗ", "Резервы против минимума ЦБ", b_reserve_norms),
]


def chart_registry(ctx):
    """
    Build the chart list for this run, numbered without gaps. Per-department pages can only
    be known once we have seen the data, so the list is assembled here, not at import time.
    """
    a = [("A00", "ИТОГИ", "Что изменилось за месяц", a00_changes)]
    a += [(f"A{i:02d}", k, t, fn) for i, (k, t, fn) in enumerate(CHARTS_A_BASE, 1)]
    for dep in ctx.get("departments", []):
        if len(ctx.get("top_pass", {}).get(dep, [])) < 2:
            continue                                  # one product (sk) — a stack of one colour says nothing
        a.append((f"A{len(a):02d}", "СТОК", f"«{dname(dep)}»: портфель по продуктам", _passport_chart(dep)))
    if ctx.get("has_oked") and SHOW_OKED:
        a.append((f"A{len(a):02d}", "СТОК", "Отраслевая структура портфеля (ОКЭД)", a_oked_dynamics))
    a.append((f"A{len(a):02d}", "СТОК", f"Топ-{TOP_CLIENTS} клиентов по месяцам", a_top_clients))

    base_b = list(CHARTS_B_BASE)
    if SHOW_BRANCH_MAP:
        base_b.insert(5, ("СРЕЗ", "Карта филиалов", b_branch_map))
    b = [(f"B{i:02d}", k, t, fn) for i, (k, t, fn) in enumerate(base_b, 1)]
    if ctx.get("has_oked") and SHOW_OKED:
        b.append((f"B{len(b) + 1:02d}", "СРЕЗ", "Отраслевая концентрация (ОКЭД)", b12_oked))
    if TIER1_CAPITAL:
        b.append((f"B{len(b) + 1:02d}", "СРЕЗ", "Крупнейшие заёмщики против лимитов ЦБ", b_large_exposures))
    if SHOW_DATA_CHECK:
        b.append(("Q1", "ТАБЛИЦА", "Проверка данных", q_data_check))
    return a, b


# ==========================================================================
# HTML — the album: A4 landscape pages, one chart per page
# ==========================================================================
CSS = """
:root{--ink:#1A1A1E;--soft:#3A3A40;--gold:#F2C230;--gd:#C9971A;--rule:#E4E1D8;
--muted:#8A867C;--bad:#B3341F;--good:#8C6A12;--paper:#fff;--desk:#E9E6DF}
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
.pb{flex:1;display:flex;flex-direction:column;gap:6px;padding-top:6px;min-height:0}
.pc{flex:0 0 auto;width:100%;display:flex;justify-content:center}
.pa{flex:1;min-height:0;border-top:1px solid var(--rule);padding-top:7px;overflow:hidden;font-size:11px;
display:grid;grid-template-columns:1fr 1.15fr 1.45fr;gap:0 18px}
.pa>div{min-width:0;overflow:hidden}
.pa>div+div{border-left:1px solid var(--rule);padding-left:14px}
.pa h4{margin:8px 0 4px;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--gd)}
.pa h4:first-child{margin-top:0}
.pa p{margin:0 0 4px}
.lg,.ins{list-style:none;margin:0;padding:0}
.lg li{display:flex;gap:7px;align-items:flex-start;margin:0 0 4px;break-inside:avoid}
.lg.two{columns:2;column-gap:12px}
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
.notice{color:var(--soft);padding:40px 60px;margin:40px auto;max-width:640px;font-size:15px;
border:1px solid var(--rule);background:#FCFAF4;border-radius:6px;text-align:center}
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
.up{color:#E6A6A6}.dn{color:#F2C230}.flat{color:#A8A397}
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
/* changes page */
.chg-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px 22px;width:""" + str(CHART_W) + """px}
.chg-grid h5,.ic h5{margin:0 0 4px;font-size:12.5px}
.tt.chg{width:100%;font-size:11.5px}.tt.chg td{padding:2px 6px}
.qc-wrap{display:flex;gap:14px;width:""" + str(CHART_W) + """px}.qc-months{flex:1.9;min-width:0}.qc-side{flex:1;min-width:0}
.qc-two{display:flex;gap:10px}.tt.qc{font-size:10px}.tt.qc td{padding:1px 4px;line-height:1.25}
.qc-side .tt.chg{font-size:10px}.qc-side .tt.chg td{padding:1px 4px;white-space:normal}.tt.chg tr.bad td{color:var(--bad);font-weight:600}
.good{color:var(--good);font-weight:600}.bad{color:var(--bad);font-weight:600}
/* icon arrays */
.ic-row{display:flex;gap:26px;justify-content:center;width:""" + str(CHART_W) + """px;padding-top:6px}
.ic h5 span{font-weight:400;color:var(--muted)}
.ic-grid{display:grid;grid-template-columns:repeat(10,19px);gap:3px}
.ic-grid svg{display:block}
.ic-cap{margin-top:8px;font-size:11.5px}.ic-cap div{display:flex;align-items:center;gap:6px;margin:2px 0}
.ic-cap i{width:10px;height:10px;border-radius:50%;display:inline-block}
/* branch map list */
.bm{display:flex;gap:10px;width:""" + str(CHART_W) + """px;align-items:flex-start}
.bm-list{list-style:none;margin:6px 0 0;padding:0;font-size:11px;column-gap:10px}
.bm-list li{display:flex;align-items:center;gap:5px;margin:0 0 3px;break-inside:avoid}
.bm-list b{flex:0 0 18px;height:18px;border-radius:50%;color:#fff;font-size:9.5px;display:flex;
align-items:center;justify-content:center}
.bm-list span{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.bm-list em{font-style:normal;color:var(--soft);white-space:nowrap;font-variant-numeric:tabular-nums}
.tt td.rel{color:#8C6A12;font-weight:700}
/* top table */
.tt2{display:flex;gap:16px;width:""" + str(CHART_W) + """px}
.tt{border-collapse:collapse;font-size:10.5px;width:50%}
.tt th{background:var(--ink);color:#fff;font-weight:600;padding:3px 4px;text-align:left;font-size:10px}
.tt td{padding:1px 5px;border-bottom:1px solid var(--rule);white-space:nowrap;line-height:1.3}
.tt td.nm{max-width:190px;overflow:hidden;text-overflow:ellipsis}
.tt td.n{text-align:right;font-variant-numeric:tabular-nums}
.tt td.bad{color:var(--bad);font-weight:700}.tt td.warn{color:#B86E0A}
.mv{font-size:10px;color:var(--muted)}.mv.up{color:var(--good)}.mv.dn{color:var(--bad)}
.mv.new{color:#C9971A;font-weight:600}
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
    return f"<ul class='lg{' two' if len(out) > 5 else ''}'>" + "".join(out) + "</ul>"


def _page_html(pg, cid, kind, section, unit, footer, pno, plotly_first):
    G = glossary()
    head = (f"<header class='ph'><div class='ph-l'><span class='cid'>{cid}</span>"
            f"<h2>{_e(pg['title'])}</h2></div><div class='ph-r'><span class='chip'>{_e(section)}</span>"
            f"<span class='chip k'>{_e(KINDS.get(kind, kind))}</span>"
            + (f"<span class='chip'>{_e(unit)}</span>" if unit else "") + "</div></header>")
    if pg.get("error"):
        body = f"<div class='err'>График не построен: {_e(pg['error'])}</div>"
    elif pg.get("notice"):
        body = f"<div class='notice'>{_e(pg['notice'])}</div>"
    elif pg.get("body_html"):
        body = pg["body_html"]
    else:
        body = pg["fig"].to_html(full_html=False, include_plotlyjs=False, config=PCFG,
                                 default_width=f"{CHART_W}px", default_height=f"{pg['fig'].layout.height or CHART_H}px")
    terms = "".join(f"<div><dt>{_e(G[t][0])}</dt> <dd>— {_e(G[t][1])}</dd></div>"
                    for t in pg.get("terms", [])[:2] if t in G)   # two fit under the text; all are on page 3
    tblock = f"<h4>Термины</h4><dl class='terms'>{terms}</dl>" if terms else ""
    # the glossary goes under whichever text column is shorter, so it is never cut off
    tl = sum(len(G[t][0]) + len(G[t][1]) for t in pg.get("terms", [])[:2] if t in G)
    left = (len(pg.get("what", "")) + tl) / 1.0                       # column widths 1 : 1.45
    right = (sum(len(re.sub("<[^>]+>", "", i)) + 25 for i in pg.get("insights", [])) + tl) / 1.45
    terms_left = left * 1.25 <= right      # the left column is also the one with less height to spare
    col1 = f"<h4>Что показано</h4><p>{_e(pg.get('what', ''))}</p>" + (tblock if terms_left else "")
    col2 = f"<h4>Как читать</h4>{_legend_html(pg['legend'])}" if pg.get("legend") else ""
    col3 = ((f"<h4>Главное</h4><ul class='ins'>" + "".join(f"<li>{i}</li>" for i in pg["insights"]) + "</ul>"
             if pg.get("insights") else "") + ("" if terms_left else tblock))
    aside = f"<div>{col1}</div><div>{col2}</div><div>{col3}</div>"
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
        except Notice as exc:
            res = [{"fig": None, "notice": str(exc), "what": "", "legend": [], "insights": [], "terms": []}]
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
    ctx["cid_of"] = {getattr(fn, "__name__", ""): cid for cid, _, _, fn in charts_a + charts_b}
    pages_a = _render_pages(charts_a, A, B, ctx, progress)
    pages_b = _render_pages(charts_b, A, B, ctx, progress)
    # the album opens straight into the charts; contents, how-to and «что изменилось» close it
    tail = [x for x in pages_a if x[0] == "A00"]
    pages_a = [x for x in pages_a if x[0] != "A00"]

    stamp = dt.datetime.now().strftime("%d.%m.%Y %H:%M")
    footer = f"{BANK} · {TITLE} · {plabel_full(sel)} · сформировано {stamp}"
    sec_a = f"A · Динамика {plabel(periods[0])} — {plabel(periods[-1])}"
    sec_b = f"B · Структура на {plabel_full(sel)}"
    first_chart_page = 2
    n_body = len(pages_a) + len(pages_b)
    p_contents, p_howto = first_chart_page + n_body, first_chart_page + n_body + 1
    p_tail = p_howto + 1

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
             f"Под значением: изменение за месяц и за год; красным — ухудшение, тёмно-жёлтым — улучшение. Содержание — в конце.</span>"
             f"<span>стр. 1</span></footer></section>")

    # contents --------------------------------------------------------------
    def toc(pages, start):
        return "".join(f"<a href='#{_e(cid)}'><span class='n'>{_e(cid)}</span><span>{_e(pg['title'])}</span>"
                       f"<span class='p'>{start + i}</span></a>" for i, (cid, _, pg) in enumerate(pages))
    contents = (f"<section class='page' id='contents'><header class='ph'><div class='ph-l'><span class='cid'>≡</span>"
                f"<h2>Содержание</h2></div></header><div class='toc'>"
                f"<h3>{_e(sec_a)}</h3>{toc(pages_a, first_chart_page)}"
                f"<h3>{_e(sec_b)}</h3>{toc(pages_b, first_chart_page + len(pages_a))}"
                f"<h3>Приложение</h3><a href='#contents'><span class='n'>≡</span><span>Содержание</span><span class='p'>{p_contents}</span></a>"
                f"<a href='#howto'><span class='n'>?</span><span>Как читать отчёт</span><span class='p'>{p_howto}</span></a>"
                f"{toc(tail, p_tail)}</div>"
                f"<footer class='pf'><span>{_e(footer)}</span><span>стр. {p_contents}</span></footer></section>")

    # how to read -----------------------------------------------------------
    deps = ctx.get("departments", [])
    k1 = _legend_html(_dept_legend(deps))
    k2 = _legend_html([(COLORS["npl"], "Красный", "NPL, дефолты — всё, что плохо", "bar"),
                       (COLORS["watch"], "Оранжевый", f"зона риска {_wz()}, ранние сигналы", "bar"),
                       (COLORS["good"], "Жёлтый — Kapitalbank", "главный цвет: kk, выдачи, сум, крупнейший продукт, «хорошо»", "bar"),
                       (COLORS["char"], "Тёмный / золотой / серый", "второй, третий, четвёртый ряд", "bar"),
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
             f"один график: сверху картинка во всю ширину, под ней «Что показано», «Как читать» и «Главное» — выводы, посчитанные "
             f"из данных. Раздел A — динамика по месяцам, раздел B — структура на одну дату ({plabel_full(sel)}). "
             f"Суммы — в {UNIT_NAME}.</p><h4 style='font-size:11px;letter-spacing:.2em;text-transform:uppercase;"
             f"color:#C9971A;margin:14px 0 4px'>Словарь</h4><dl class='gl'>{gl}</dl>"
             f"<footer class='pf'><span>Печать: Ctrl+P → A4, альбомная, поля «Нет», «Фон» включён.</span>"
             f"<span>стр. {p_howto}</span></footer></section>")

    # chart pages -------------------------------------------------------------
    body, pno = [], first_chart_page
    for section, pages in ((sec_a, pages_a), (sec_b, pages_b)):
        for cid, kind, pg in pages:
            if progress:
                progress(f"страница {cid}")
            unit = "" if kind in ("КОГОРТЫ",) else UNIT_NAME
            body.append(_page_html(pg, cid, kind, section, unit, footer, pno, False))
            pno += 1
    tail_html = "".join(_page_html(pg, cid, kind, "Приложение", UNIT_NAME, footer, p_tail + i, False)
                        for i, (cid, kind, pg) in enumerate(tail))

    try:
        from plotly.offline import get_plotlyjs_version
        pver = get_plotlyjs_version()
    except Exception:
        pver = "2.35.2"
    doc = (f"<!doctype html><html lang='ru'><head><meta charset='utf-8'>"
           f"<meta name='viewport' content='width=device-width,initial-scale=1'>"
           f"<title>{_e(TITLE)} — {plabel_full(sel)}</title>"
           f"<script src='https://cdn.plot.ly/plotly-{pver}.min.js'></script>"
           f"<style>{CSS}</style></head><body>{cover}{''.join(body)}{contents}{howto}{tail_html}</body></html>")
    Path(out_path).write_text(doc, encoding="utf-8")
    return n_body + len(tail)


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

    say("чтение файлов и построение панели")
    # read straight into the panel: no name keeps the raw table alive, so it is freed as soon as
    # the panel exists (on 17M rows that is gigabytes)
    panel = build_panel(read_months(data_dir, period_from, period_to))
    has_oked = "oked_name" in panel.columns and SHOW_OKED
    merges, files = panel.attrs.get("merges", {}), panel.attrs.get("files", [])
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
    A, B = _plain_text(A), _plain_text(B)
    names = load_names(data_dir)                  # your top-50 names / aloqador table, if present
    apply_names(A, names)
    ctx = {"sel": sel, "periods": periods, "has_oked": has_oked,
           "departments": list(top_pass.keys()), "top_pass": top_pass,
           "merges": merges, "files": files}

    say("сборка отчёта")
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    n_pages = build_html(A, B, ctx, out_path, progress=say)
    try:
        write_top_template(A, Path(out_path).parent)
    except Exception:
        pass                                      # a template is a convenience, never a reason to fail

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
        "names_file": str(names[2]) if names[2] else None,
    }
