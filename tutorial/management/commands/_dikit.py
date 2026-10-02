# -*- coding: utf-8 -*-
"""Data Insights kit for Prime GMAT (GMAT-31…35): tables, charts and I/II/III statements.

NOT a Django management command — the leading underscore keeps it out of `manage.py help`
(same arrangement as _svgkit.py and _romaji.py). Lesson and practice data files load it by
path, so the same table or chart is drawn the same way everywhere:

    import importlib.util, os
    _p = os.path.join(os.path.dirname(os.path.abspath(__file__)), ..., '_dikit.py')

Charts are never hand-typed: a bar whose height disagrees with its number is a lying figure.
The batch gate (verify_gmat_31_35.py) re-measures every bar and every dot from the SVG back
to the data, independently of this module.

Geometry: viewBox 0 0 320 210; plot area x 46…300, baseline y = 160, top y = 30, so a value v
on an axis running 0…ymax is drawn at height v / ymax × 130.
"""
from fractions import Fraction

BASE, TOP, LEFT, RIGHT = 160, 30, 46, 300
PLOT_H = BASE - TOP          # 130
PLOT_W = RIGHT - LEFT        # 254

ROMAN = ['I', 'II', 'III']
COMBOS = {
    'I': 'I only', 'II': 'II only', 'III': 'III only',
    'I,II': 'I and II only', 'I,III': 'I and III only', 'II,III': 'II and III only',
    'I,II,III': 'I, II and III', '': 'None of the statements',
}


def _num(v):
    """Print a number the American way: 1,200 and 3.5 — no trailing .0."""
    v = Fraction(v).limit_denominator(1000)
    if v.denominator == 1:
        return f'{v.numerator:,}'
    return f'{float(v):,.10g}'


def _f(v):
    r = round(float(v), 1)
    return str(int(r)) if r == int(r) else str(r)


def table(headers, rows):
    """A data table in the pm-word style, wrapped so it scrolls sideways on a phone."""
    head = ''.join(f'<th>{h}</th>' for h in headers)
    body = ''.join('<tr>' + ''.join(f'<td>{c if isinstance(c, str) else _num(c)}</td>' for c in r) + '</tr>'
                   for r in rows)
    return f'<div class="pe-table-wrap"><table class="pm-word"><tr>{head}</tr>{body}</table></div>'


def _frame(ymax, step, unit):
    out = []
    v = step
    while v <= ymax:
        y = BASE - Fraction(v, 1) / ymax * PLOT_H
        out.append(f'<line class="pm-ch__grid" x1="{LEFT}" y1="{_f(y)}" x2="{RIGHT}" y2="{_f(y)}"/>')
        out.append(f'<text class="pm-ch__cap" x="{LEFT - 6}" y="{_f(y + 4)}" text-anchor="end">{_num(v)}</text>')
        v += step
    out.append(f'<line class="pm-ch__ax" x1="{LEFT}" y1="{BASE}" x2="{RIGHT}" y2="{BASE}"/>')
    out.append(f'<text class="pm-ch__cap" x="{LEFT - 6}" y="{BASE + 4}" text-anchor="end">0</text>')
    if unit:
        out.append(f'<text class="pm-ch__cap" x="{LEFT}" y="16">{unit}</text>')
    return out


def bar_chart(labels, values, ymax, step, caption, aria, unit=''):
    """One-series bar chart: every bar the same colour, every bar labelled with its value."""
    n = len(values)
    band = Fraction(PLOT_W, n)
    w = band * Fraction(3, 5)
    parts = _frame(ymax, step, unit)
    for i, (lab, v) in enumerate(zip(labels, values)):
        h = Fraction(v) / ymax * PLOT_H
        x = LEFT + band * i + (band - w) / 2
        cx = x + w / 2
        parts.append(f'<rect class="pm-ch__bar" x="{_f(x)}" y="{_f(BASE - h)}" width="{_f(w)}" height="{_f(h)}" data-v="{v}"/>')
        parts.append(f'<text class="pm-ch__val" x="{_f(cx)}" y="{_f(BASE - h - 5)}" text-anchor="middle">{_num(v)}</text>')
        parts.append(f'<text class="pm-ch__lbl" x="{_f(cx)}" y="{BASE + 16}" text-anchor="middle">{lab}</text>')
    svg = '\n    '.join(parts)
    return (f'<figure class="pm-fig">\n  <svg viewBox="0 0 320 210" role="img" aria-label="{aria}">\n    {svg}\n  </svg>\n'
            f'  <figcaption>{caption}</figcaption>\n</figure>')


def line_chart(labels, values, ymax, step, caption, aria, unit=''):
    """One-series line chart with a labelled dot at every point."""
    n = len(values)
    gap = Fraction(PLOT_W, n)
    parts = _frame(ymax, step, unit)
    pts = []
    for i, v in enumerate(values):
        x = LEFT + gap * i + gap / 2
        y = BASE - Fraction(v) / ymax * PLOT_H
        pts.append((x, y, v))
    parts.append('<polyline class="pm-ch__line" points="' + ' '.join(f'{_f(x)},{_f(y)}' for x, y, _ in pts) + '"/>')
    for (x, y, v), lab in zip(pts, labels):
        parts.append(f'<circle class="pm-ch__dot" cx="{_f(x)}" cy="{_f(y)}" r="4" data-v="{v}"/>')
        parts.append(f'<text class="pm-ch__val" x="{_f(x)}" y="{_f(y - 9)}" text-anchor="middle">{_num(v)}</text>')
        parts.append(f'<text class="pm-ch__lbl" x="{_f(x)}" y="{BASE + 16}" text-anchor="middle">{lab}</text>')
    svg = '\n    '.join(parts)
    return (f'<figure class="pm-fig">\n  <svg viewBox="0 0 320 210" role="img" aria-label="{aria}">\n    {svg}\n  </svg>\n'
            f'  <figcaption>{caption}</figcaption>\n</figure>')


def statements(items):
    """The I / II / III block used by Table Analysis and Multi-Source questions."""
    return ''.join(f'<p><b>{r}.</b> {s}</p>' for r, s in zip(ROMAN, items))


def combo(true_set):
    """The answer text for a set of true statements, e.g. {'I', 'III'} → 'I and III only'."""
    key = ','.join(r for r in ROMAN if r in true_set)
    return COMBOS[key]


def pair(a_label, a, b_label, b):
    """A Two-Part Analysis answer: one value for each column."""
    return f'{a_label}: {a} · {b_label}: {b}'


if __name__ == '__main__':
    # self-test: geometry of a known bar and dot
    svg = bar_chart(['a', 'b'], [50, 100], 100, 25, 'cap', 'aria')
    assert 'height="65"' in svg and 'height="130"' in svg, svg
    svg = line_chart(['a'], [25], 100, 25, 'cap', 'aria')
    assert 'cy="127.5"' in svg, svg
    assert combo({'I', 'III'}) == 'I and III only' and combo(set()) == 'None of the statements'
    assert _num(1200) == '1,200' and _num(Fraction(7, 2)) == '3.5'
    print('dikit self-test: ok')
