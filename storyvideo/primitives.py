# -*- coding: utf-8 -*-
"""The maths kit.

Named as siblings of the lesson kit in static/css/style.css (pm-solve, pm-model,
pm-num...) so the video vocabulary and the lesson vocabulary match.

Every builder here returns an HTML string and takes scene-relative times in
`at=` seconds; anim.js resolve() turns those into absolute ones.

THE COUNTABILITY RULE: anything that shows a quantity emits n discrete elements
AND a counter that ticks in lockstep with them. lint.py fails a scene that shows
a quantity without one, because "every quantity countable on screen" is the whole
point of the format.
"""

import people as _people


def _t(at):
    return f'data-at="{at:.3f}"'


# ─────────────────────────────────────────────────────────── counters ──
def counter(to, label, at=0.0, dur=1.0, cls="", frm=0, per=None, total=None,
            counts=None):
    """A number that counts up while the things it counts appear.

    per/total turn it into a derived count: ceil(total*progress / per), used for
    "how many tables are in use" so it can never disagree with the picture.
    """
    derived = f'data-per="{per}" data-count-total="{total}" ' if per else ""
    # What this number is a count OF -- lint.py counts the matching visible
    # elements at several moments and fails if the picture disagrees.
    if counts:
        derived += f'data-counts="{counts}" '
    return (f'<div class="count"><b class="counter {cls}" {derived}'
            f'data-from="{frm}" data-to="{to}" '
            f'data-count-dur="{dur:.3f}" data-dur="0.4" data-anim="pop" '
            f'data-at="{at:.3f}">{frm}</b>'
            f'<span class="lbl lbl--sm">{label}</span></div>')


def counters(*items):
    return f'<div class="counters">{"".join(items)}</div>'


# ─────────────────────────────────────────────────────────────── crowd ──
def crowd(n, at=0.0, step=0.14, size=104, named=None, per_row=7, mood="smile"):
    """n people appearing one at a time. The countable primitive.

    named: {index: "Bekzod"} pins specific cast members into the crowd.
    Returns (html, total_seconds) so the caller can size the scene and the
    counter to the exact same duration.
    """
    named = named or {}
    cells = []
    for i in range(n):
        fig = _people.figure(named.get(i), size=size, i=i, mood=mood)
        cells.append(f'<div class="crowd__c" {_t(at + i * step)} data-dur="0.30" '
                     f'data-anim="pop">{fig}</div>')
    style = f"max-width:{per_row * (size * 100 // 175 + 26)}px"
    return f'<div class="crowd" style="{style}">{"".join(cells)}</div>', n * step


# ─────────────────────────────────────────────────────────────── table ──
def table(seats=6, filled=0, at=0.0, step=0.16, first_index=0, named=None,
          dim=False, seat_size=58):
    """One table with `seats` chairs TUCKED AGAINST IT, three per side.

    The sample video drew seats as ellipses flung far from the table, so six
    children at a table read as children floating in puddles. Here the chairs
    touch the table edge and the seated figures overlap it, which is what makes
    "six at this table" legible at a glance.
    """
    named = named or {}
    half = (seats + 1) // 2

    def row(idxs, side):
        out = []
        for k, si in enumerate(idxs):
            gi = first_index + si
            if si < filled:
                body = _people.seated(named.get(gi), i=gi, size=seat_size)
                cls = "seat seat--full"
                tm = f'{_t(at + si * step)} data-dur="0.28" data-anim="pop"'
            else:
                body, cls, tm = "", "seat", ""
            out.append(f'<div class="{cls}" {tm}>{body}</div>')
        return f'<div class="tbl__row tbl__row--{side}">{"".join(out)}</div>'

    top = row(list(range(half)), "top")
    bot = row(list(range(half, seats)), "bot")
    return (f'<div class="tbl{" tbl--dim" if dim else ""}">{top}'
            f'<div class="tbl__top"></div>{bot}</div>')


def tables(total, per, at=0.0, step=0.16, named=None, cols=2, seat_size=58):
    """`total` people seated `per` table, filling seat by seat, left to right.

    Returns (html, seconds, n_tables, leftover) -- leftover is the remainder,
    which in this course is nearly always the point of the story.
    """
    n_tables = -(-total // per)          # ceil
    leftover = total % per
    boxes = []
    for ti in range(n_tables):
        seated_here = min(per, total - ti * per)
        t0 = at + ti * per * step
        inner = table(seats=per, filled=seated_here, at=t0, step=step,
                      first_index=ti * per, named=named, seat_size=seat_size)
        # A table arrives when its first guest does. Drawing all seven up front
        # would put seven tables on screen while the counter still said one.
        boxes.append(f'<div class="tblbox" data-at="{max(t0 - 0.22, 0):.3f}" '
                     f'data-dur="0.42" data-anim="pop">{inner}</div>')
    html = f'<div class="tblgrid" style="--cols:{cols}">{"".join(boxes)}</div>'
    return html, total * step, n_tables, leftover


# ────────────────────────────────────────────────────────── solve ladder ──
def solve(rows, at=0.0, step=0.9):
    """The pm-solve ladder: each line appears with the reason it happened."""
    out = []
    for i, r in enumerate(rows):
        left, why = (r if isinstance(r, (tuple, list)) else (r, ""))
        out.append(f'<div class="solve__row" {_t(at + i * step)} data-dur="0.45" '
                   f'data-anim="rise"><span class="solve__l">{left}</span>'
                   f'<span class="solve__r">{why}</span></div>')
    return f'<div class="solve">{"".join(out)}</div>', len(rows) * step


# ──────────────────────────────────────────────────────────────── bits ──
# Playfair digits run about 0.56em wide, and a scene has ~940px of usable
# width. Long sums ("52 × 25 000 = 1 300 000") have to come down in size or they
# run off both edges -- which is exactly what they did before lint caught it.
EXPR_MAX_W = 880
EXPR_MAX_PX = 128


def expr_size(text, max_w=EXPR_MAX_W):
    import re as _re
    n = len(_re.sub(r"<[^>]+>", "", text))
    return max(46, min(EXPR_MAX_PX, int(max_w / (n * 0.56)))) if n else EXPR_MAX_PX


def expr(text, at=0.0, cls="", anim="pop", dur=0.5, max_w=EXPR_MAX_W):
    px = expr_size(text, max_w)
    return (f'<div class="expr {cls}" style="font-size:{px}px" {_t(at)} '
            f'data-dur="{dur}" data-anim="{anim}">{text}</div>')


# base px, em advance, how many lines the class may wrap to. Headings wrap
# rather than shrink -- a rule set at 41px to fit one line reads as an
# afterthought, which is the opposite of what a closing card is for.
_FIT = {"hero": (360, 0.63, 1), "big": (200, 0.63, 1),
        "ttl": (84, 0.55, 3), "ask": (74, 0.55, 2)}


def fit_px(text, cls="hero", fit=880):
    """The px size a display class needs to fit `text` into `fit` pixels."""
    import re as _re
    base, em, lines = _FIT.get(cls, (84, 0.55, 1))
    n = len(_re.sub(r"<[^>]+>", "", text))
    return max(40, min(base, int(fit * lines / (n * em)))) if n else base


def line(text, cls="lbl", at=0.0, anim="rise", dur=0.45, fit=880):
    """A line of type. Display classes shrink to fit rather than run off frame."""
    import re as _re
    style = ""
    key = next((k for k in _FIT if k in cls.split()), None)
    if key and fit:
        base, em, lines = _FIT[key]
        n = len(_re.sub(r"<[^>]+>", "", text))
        if n:
            px = max(40, min(base, int(fit * lines / (n * em))))
            if px < base:
                style = f' style="font-size:{px}px"'
    return (f'<div class="{cls}"{style} {_t(at)} data-dur="{dur}" '
            f'data-anim="{anim}">{text}</div>')


def card_expr(text, max_w=760):
    """An expression sized for the inside of a card, which is narrower than the
    frame. Without this a card's contents keep the full-frame default and wrap
    into a five-line stack."""
    return f'<div class="expr" style="font-size:{expr_size(text, max_w)}px">{text}</div>'


def card(inner, at=0.0, cls="", anim="pop", dur=0.5):
    return f'<div class="card {cls}" {_t(at)} data-dur="{dur}" data-anim="{anim}">{inner}</div>'


def bubble(lines, at=0.0, dur=0.5):
    def one(tx, c):
        if "expr" in c:
            return f'<div class="{c}" style="font-size:{expr_size(tx, 720)}px">{tx}</div>'
        return f'<div class="{c}">{tx}</div>'
    body = "".join(one(tx, c) for tx, c in lines)
    return f'<div class="bubble" {_t(at)} data-dur="{dur}" data-anim="pop">{body}</div>'


def person(who=None, size=170, mood="smile", arms="down", at=0.0, i=0,
           anim="rise", dur=0.5):
    return (f'<div class="figbox" {_t(at)} data-dur="{dur}" data-anim="{anim}">'
            f'{_people.figure(who, size=size, mood=mood, arms=arms, i=i)}</div>')


def ticks(n, at=0.0, step=1.1):
    """A silent thinking beat: dots that tick over while the viewer divides."""
    d = "".join(f'<span class="tick" data-in="0" {_t(at + i * step)}></span>' for i in range(n))
    return f'<div class="ticks">{d}</div>'


# ──────────────────────────────────────────────── geometry figures ──
def rect_walk(a, b, at=0.0, step=0.85, unit="m", w=620, label_a="uzunlik",
              label_b="en", gate=None):
    """A rectangle whose four sides light up one at a time as you walk it.

    Perimeter is the one topic where the countable thing is not objects but
    LENGTH, so the counter sums the sides that are lit rather than counting
    them: 18 -> 28 -> 46 -> 56. Watching the total climb past 28 is the whole
    correction of PM-67, made visible instead of asserted.

    Returns (html, seconds).
    """
    pad, ww, hh = 96, w, round(w * b / a)
    W_, H_ = ww + pad * 2, hh + pad * 2
    x0, y0, x1, y1 = pad, pad, pad + ww, pad + hh

    sides = [
        ("top",   x0, y0, x1, y0, a),
        ("right", x1, y0, x1, y1, b),
        ("bot",   x1, y1, x0, y1, a),
        ("left",  x0, y1, x0, y0, b),
    ]
    seg = "".join(
        f'<line class="side side--{n}" data-val="{v}" x1="{ax}" y1="{ay}" '
        f'x2="{bx}" y2="{by}" data-at="{at + i * step:.3f}" data-dur="0.42" '
        f'data-anim="fade"/>'
        for i, (n, ax, ay, bx, by, v) in enumerate(sides))

    labels = (
        f'<text class="dim" x="{(x0+x1)/2}" y="{y0-30}" text-anchor="middle">{a} {unit}</text>'
        f'<text class="dim" x="{(x0+x1)/2}" y="{y1+62}" text-anchor="middle">{a} {unit}</text>'
        f'<text class="dim" x="{x0-30}" y="{(y0+y1)/2}" text-anchor="end" '
        f'dominant-baseline="middle">{b} {unit}</text>'
        f'<text class="dim" x="{x1+30}" y="{(y0+y1)/2}" text-anchor="start" '
        f'dominant-baseline="middle">{b} {unit}</text>'
        f'<text class="dim dim--soft" x="{(x0+x1)/2}" y="{(y0+y1)/2-14}" '
        f'text-anchor="middle">{label_a} {a} {unit}</text>'
        f'<text class="dim dim--soft" x="{(x0+x1)/2}" y="{(y0+y1)/2+46}" '
        f'text-anchor="middle">{label_b} {b} {unit}</text>')

    ghost = (f'<rect x="{x0}" y="{y0}" width="{ww}" height="{hh}" class="ghost"/>')
    gatemark = ""
    if gate:
        gl = ww * gate / a
        gatemark = (f'<line class="gate" x1="{x0 + (ww-gl)/2}" y1="{y1}" '
                    f'x2="{x0 + (ww+gl)/2}" y2="{y1}" data-at="{at + 4*step + 0.3:.3f}" '
                    f'data-dur="0.4" data-anim="fade"/>')

    svg = (f'<svg class="fig fig--rect" viewBox="0 0 {W_} {H_}">'
           f'{ghost}{seg}{gatemark}{labels}</svg>')

    # The sum writes itself as each side lights, so the running total is not
    # just a number in the corner -- the viewer sees which side added what.
    terms = "".join(
        f'<span class="term" data-at="{at + i * step:.3f}" data-dur="0.35" '
        f'data-anim="pop">{"" if i == 0 else "+ "}{v}</span>'
        for i, (_n, _ax, _ay, _bx, _by, v) in enumerate(sides))
    return (f'<div class="figwrap">{svg}<div class="terms">{terms}</div></div>',
            4 * step)


# ─────────────────────────────────────────────────────── comparison ──
def compare(left, right, at=0.0, step=1.1, verdict=None, unit_label=""):
    """Two options side by side, each resolved to the SAME unit.

    left/right: {"name","qty","price","unit","tag"} -- tag is the computed
    per-unit figure, revealed after both totals so the viewer can guess first.
    """
    def side(d, i, cls):
        rows = [f'<div class="cmp__n">{d["name"]}</div>',
                f'<div class="cmp__q" data-at="{at + i*0.25:.3f}" data-dur="0.4" '
                f'data-anim="pop">{d["qty"]}</div>',
                f'<div class="cmp__p" data-at="{at + 0.5 + i*0.25:.3f}" data-dur="0.4" '
                f'data-anim="rise">{d["price"]}</div>']
        if d.get("tag"):
            rows.append(f'<div class="cmp__u {cls}" data-at="{at + step + i*0.3:.3f}" '
                        f'data-dur="0.5" data-anim="pop">{d["tag"]}</div>')
        return f'<div class="cmp__side">{"".join(rows)}</div>'

    body = (f'<div class="cmp">{side(left, 0, left.get("cls",""))}'
            f'<div class="cmp__v">vs</div>{side(right, 1, right.get("cls",""))}</div>')
    if unit_label:
        body += (f'<div class="lbl lbl--sm" data-at="{at + step + 0.9:.3f}" '
                 f'data-dur="0.4" data-anim="fade">{unit_label}</div>')
    if verdict:
        body += (f'<div class="ttl" data-at="{at + step + 1.6:.3f}" data-dur="0.5" '
                 f'data-anim="pop">{verdict}</div>')
    return body, step + 2.4


# ─────────────────────────────────────────────────── multiples chips ──
def multiples(n, count, at=0.0, step=0.55, hit=None, label=""):
    """The multiples of n, written out one at a time: 12, 24, 36, 48.

    This is literally what Bekzod does in PM-8 — opens his notebook and lists
    them — so the video shows the method, not just its answer. The shared value
    lights up in both rows at once.
    """
    chips = []
    for i in range(1, count + 1):
        v = n * i
        cls = "chip chip--hit" if hit is not None and v == hit else "chip"
        chips.append(f'<span class="{cls}" data-val="{v}" {_t(at + (i - 1) * step)} '
                     f'data-dur="0.32" data-anim="pop">{v}</span>')
    head = f'<span class="chips__l">{label}</span>' if label else ""
    return f'<div class="chips">{head}{"".join(chips)}</div>', count * step


# ───────────────────────────────────────────────────────────── packs ──
def packs(n, contents, at=0.0, step=0.3, note=""):
    """n identical packets, each showing exactly what is inside.

    contents: [(count, emoji), ...]. Emoji is the escape hatch for the long tail
    of props -- flowers, sweets, boxes -- that are not worth hand-drawing and
    that Chrome renders perfectly well.
    """
    inner = "".join(
        f'<span class="pack__row">{"".join(f"<i>{ch}</i>" for _ in range(c))}</span>'
        for c, ch in contents)
    boxes = "".join(
        f'<div class="pack" {_t(at + i * step)} data-dur="0.36" data-anim="pop">'
        f'{inner}</div>' for i in range(n))
    tail = f'<div class="lbl lbl--sm packs__n">{note}</div>' if note else ""
    return f'<div class="packs">{boxes}</div>{tail}', n * step


# ───────────────────────────────────────────────────────── chessboard ──
def board(lit=8, at=0.0, step=0.5, cols=8, rows=8, show_upto=8):
    """A chessboard whose squares fill one at a time, doubling as they go.

    The first eight squares can still be believed. That is the whole trick of
    PM-12: the picture stays innocent while the number stops being innocent.
    """
    cells = []
    for i in range(cols * rows):
        r, c = divmod(i, cols)
        dark = (r + c) % 2 == 1
        cls = "sq sq--d" if dark else "sq"
        if i < lit:
            n = 2 ** i
            txt = f'<b>{n}</b>' if i < show_upto else ""
            cells.append(f'<div class="{cls} sq--on" {_t(at + i * step)} '
                         f'data-dur="0.34" data-anim="pop">{txt}</div>')
        else:
            cells.append(f'<div class="{cls}"></div>')
    return (f'<div class="board" style="--c:{cols}">{"".join(cells)}</div>',
            lit * step)


# ────────────────────────────────────────────────────────────── bars ──
def bars(items, ref=None, ref_label="", at=0.0, step=1.1, unit=""):
    """Value bars with a dashed reference line.

    items: [(value, label, css_class), ...]. `ref` draws the original level
    across the whole chart, which is what makes PM-25 land: you do not have to
    be told the last bar came out below where it started -- you can see it.
    """
    top = max(v for v, *_ in items) * 1.12
    cols = []
    for i, (v, lab, *rest) in enumerate(items):
        cls = rest[0] if rest else ""
        h = v / top * 100
        cols.append(
            f'<div class="bar__col">'
            f'<div class="bar__v" {_t(at + i * step + 0.28)} data-dur="0.3" '
            f'data-anim="fade">{v:,}</div>'.replace(",", " ") +
            f'<div class="bar__b {cls}" style="height:{h:.1f}%" '
            f'{_t(at + i * step)} data-dur="0.55" data-anim="grow"></div>'
            f'<div class="bar__l">{lab}</div></div>')
    refline = ""
    if ref is not None:
        y = ref / top * 100
        refline = (f'<div class="bar__ref" style="bottom:calc({y:.1f}% + 46px)" '
                   f'{_t(at + 0.9)} data-dur="0.5" data-anim="widen">'
                   f'<span>{ref_label}</span></div>')
    return (f'<div class="bars">{refline}{"".join(cols)}</div>',
            len(items) * step + 0.6)
