"""Inline-SVG figure builders for Logic Arena puzzles.

A logic puzzle usually needs a picture — nine coins, a river, a mutilated
chessboard — but a picture must not cost the page anything. So every figure is
inline SVG built here: a few hundred bytes of markup, no upload, no HTTP
request, and it scales on a phone and prints on a worksheet.

Two conventions hold the kit together:

* **structure is drawn, objects are emoji.** Lines, rectangles and circles carry
  the geometry the solver has to reason about; a wolf, a goat and a cabbage are
  ``<text>`` emoji. That keeps a river-crossing figure to six elements instead
  of sixty paths, and it stays legible at any size.
* **no colours in the markup.** Everything uses the ``lg-*`` classes from
  static/css/style.css (`lg-ln`, `lg-fill`, `lg-lbl`), so a figure restyles with
  the section rather than carrying its own palette. The one exception is a
  puzzle where colour *is* the content — the chessboard's light and dark
  squares, which are the whole argument.

Every builder returns a bare ``<svg>`` string. `fig()` wraps one in the framed,
captioned block that goes into a puzzle body — call it twice, once per language,
around the same SVG.
"""
from html import escape


def fig(svg, caption=''):
    """Wrap an SVG in the framed figure block, with an optional caption."""
    cap = f'<p class="lg-fig__cap">{escape(caption)}</p>' if caption else ''
    return f'<div class="lg-fig">{svg}{cap}</div>'


def _svg(width, height, body):
    return (f'<svg viewBox="0 0 {width} {height}" width="100%" '
            f'style="max-width:{width}px" role="img" xmlns="http://www.w3.org/2000/svg">'
            f'{body}</svg>')


def _text(x, y, content, cls='lg-lbl', size=None):
    style = f' style="font-size:{size}px"' if size else ''
    return f'<text x="{x}" y="{y}" class="{cls}"{style}>{content}</text>'


def _glyph(x, y, emoji, size=26):
    """An emoji as a centred SVG glyph — the cheapest possible illustration."""
    return (f'<text x="{x}" y="{y}" text-anchor="middle" '
            f'style="font-size:{size}px">{emoji}</text>')


# ── balance scale ───────────────────────────────────────────────────────────

def balance(left='', right='', tilt=0, caption_left='', caption_right=''):
    """A two-pan balance.

    `tilt` is -1 (left pan sinks), 0 (level) or +1 (right pan sinks) — the three
    outcomes every weighing puzzle turns on, which is why the same picture is
    reused with a different tilt instead of three separate drawings.
    """
    ly, ry = 52 - 16 * tilt, 52 + 16 * tilt
    return _svg(330, 170, ''.join([
        # stand
        '<path d="M165 130 L165 52" class="lg-ln lg-ln--th"/>',
        '<path d="M130 132 L200 132" class="lg-ln lg-ln--th"/>',
        f'<circle cx="165" cy="50" r="5" class="lg-fill"/>',
        # beam
        f'<path d="M55 {ly} L275 {ry}" class="lg-ln lg-ln--th"/>',
        # hangers + pans
        f'<path d="M55 {ly} L55 {ly + 26}" class="lg-ln"/>',
        f'<path d="M275 {ry} L275 {ry + 26}" class="lg-ln"/>',
        f'<path d="M20 {ly + 26} Q55 {ly + 52} 90 {ly + 26} Z" class="lg-fill"/>',
        f'<path d="M240 {ry + 26} Q275 {ry + 52} 310 {ry + 26} Z" class="lg-fill"/>',
        # what is in each pan
        _text(55, ly + 14, escape(left)),
        _text(275, ry + 14, escape(right)),
        _text(55, 158, escape(caption_left), 'lg-lbl lg-lbl--sm'),
        _text(275, 158, escape(caption_right), 'lg-lbl lg-lbl--sm'),
    ]))


# ── rows of things ──────────────────────────────────────────────────────────

def coins(count, groups=None, labels=None, glyph='🪙'):
    """A row of identical coins, optionally fenced into groups.

    `groups` is a list of sizes, e.g. [3, 3, 3] — the fences are what make the
    "split it into three" idea visible before a word of the solution is read.
    """
    per, gap, pad = 34, 22, 16
    sizes = groups or [count]
    width = pad * 2 + count * per + gap * (len(sizes) - 1)
    parts, x, i = [], pad, 0
    for g, size in enumerate(sizes):
        box_w = size * per
        parts.append(f'<rect x="{x - 6}" y="14" width="{box_w + 12}" height="46" '
                     f'rx="10" class="lg-ln" style="fill:none;stroke-dasharray:4 3"/>')
        for _ in range(size):
            parts.append(_glyph(x + per // 2, 46, glyph, 24))
            i += 1
            x += per
        if labels and g < len(labels):
            parts.append(_text(x - box_w // 2, 76, escape(labels[g]), 'lg-lbl lg-lbl--sm'))
        x += gap
    return _svg(width, 88, ''.join(parts))


def row(items, caption_row=None, glyph_size=30, box=True):
    """A labelled row of emoji objects — sacks, doors, jugs, horses."""
    per = 62
    width = 24 + len(items) * per
    parts = []
    for i, item in enumerate(items):
        x = 24 + i * per
        if box:
            parts.append(f'<rect x="{x - 4}" y="10" width="{per - 12}" height="52" '
                         f'rx="10" class="lg-fill"/>')
        parts.append(_glyph(x + (per - 12) // 2 - 4, 46, item, glyph_size))
        if caption_row and i < len(caption_row):
            parts.append(_text(x + (per - 12) // 2 - 4, 80, escape(caption_row[i]),
                               'lg-lbl lg-lbl--sm'))
    return _svg(width, 92, ''.join(parts))


# ── scenes ──────────────────────────────────────────────────────────────────

def river(left_items, right_items, boat='🛶', left_label='', right_label=''):
    """Two banks with a strip of water between them."""
    parts = [
        # banks
        '<rect x="0" y="20" width="120" height="90" rx="8" class="lg-fill--mint"/>',
        '<rect x="280" y="20" width="120" height="90" rx="8" class="lg-fill--mint"/>',
        # water
        '<rect x="120" y="20" width="160" height="90" class="lg-fill"/>',
        '<path d="M132 62 q14 -8 28 0 t28 0 t28 0 t28 0 t28 0" class="lg-ln"/>',
        _glyph(200, 96, boat, 26),
        _text(60, 136, escape(left_label), 'lg-lbl lg-lbl--sm'),
        _text(340, 136, escape(right_label), 'lg-lbl lg-lbl--sm'),
    ]
    for i, item in enumerate(left_items):
        parts.append(_glyph(30 + i * 32, 52, item, 24))
    for i, item in enumerate(right_items):
        parts.append(_glyph(310 + i * 32, 52, item, 24))
    return _svg(400, 148, ''.join(parts))


def chessboard(cut_corners=True, domino=True):
    """An 8×8 board, optionally with two opposite corners cut out.

    This is the one figure that keeps real colours: the whole proof is that the
    two removed corners share a colour, so light and dark squares have to be
    literally light and dark rather than themed.
    """
    cell, pad = 30, 14
    parts = []
    for r in range(8):
        for c in range(8):
            if cut_corners and ((r == 0 and c == 0) or (r == 7 and c == 7)):
                parts.append(f'<rect x="{pad + c * cell}" y="{pad + r * cell}" '
                             f'width="{cell}" height="{cell}" fill="#fee2e2" '
                             f'stroke="#ef4444" stroke-width="1.5" '
                             f'stroke-dasharray="4 3"/>')
                continue
            dark = (r + c) % 2 == 1
            parts.append(f'<rect x="{pad + c * cell}" y="{pad + r * cell}" '
                         f'width="{cell}" height="{cell}" '
                         f'fill="{"#64748b" if dark else "#f1f5f9"}"/>')
    parts.append(f'<rect x="{pad}" y="{pad}" width="{8 * cell}" height="{8 * cell}" '
                 f'class="lg-ln" style="fill:none"/>')
    if domino:
        # one domino laid across two squares, to say what a "cover" means
        parts.append(f'<rect x="{pad + 8 * cell + 18}" y="{pad + 60}" width="{cell * 2}" '
                     f'height="{cell}" rx="6" class="lg-fill--gold"/>')
        parts.append(_text(pad + 8 * cell + 18 + cell, pad + 108, '1 × 2',
                           'lg-lbl lg-lbl--sm'))
    return _svg(pad * 2 + 8 * cell + 90, pad * 2 + 8 * cell, ''.join(parts))


def bookshelf(volumes=10, page_side='right'):
    """Volumes standing in order, with the first and last pages marked.

    The trap in the bookworm puzzle is *where page 1 actually is* once the books
    are on a shelf, so the figure marks it rather than describing it — this is
    the one place where the picture is the puzzle.
    """
    w, gap, top, h = 26, 3, 16, 86
    width = 30 + volumes * (w + gap) + 60
    parts = ['<path d="M12 %d L%d %d" class="lg-ln lg-ln--th"/>' % (top + h + 6, width - 12, top + h + 6)]
    for i in range(volumes):
        x = 24 + i * (w + gap)
        parts.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="3" '
                     f'class="lg-fill"/>')
        parts.append(f'<text x="{x + w // 2}" y="{top + h // 2 + 5}" class="lg-lbl lg-lbl--sm" '
                     f'text-anchor="middle">{i + 1}</text>')
    first_x = 24 + w if page_side == 'right' else 24
    last_x = 24 + (volumes - 1) * (w + gap) if page_side == 'right' else 24 + volumes * (w + gap)
    parts += [
        f'<path d="M{first_x} {top - 6} L{first_x} {top + h + 4}" '
        f'stroke="#e11d48" stroke-width="3"/>',
        f'<path d="M{last_x} {top - 6} L{last_x} {top + h + 4}" '
        f'stroke="#e11d48" stroke-width="3"/>',
        _text(first_x, top - 12, 'p.1', 'lg-lbl lg-lbl--sm'),
        _text(last_x, top - 12, 'last', 'lg-lbl lg-lbl--sm'),
    ]
    return _svg(width, top + h + 20, ''.join(parts))


def ropes(count=2, labels=None):
    """Ropes drawn as bars with a flame at each end that can be lit."""
    parts = []
    for i in range(count):
        y = 26 + i * 46
        parts.append(f'<rect x="60" y="{y}" width="220" height="14" rx="7" '
                     f'class="lg-fill--gold"/>')
        parts.append(_glyph(46, y + 14, '🔥', 18))
        parts.append(_glyph(294, y + 14, '🔥', 18))
        if labels and i < len(labels):
            parts.append(_text(170, y + 34, escape(labels[i]), 'lg-lbl lg-lbl--sm'))
    return _svg(340, 26 + count * 46 + 16, ''.join(parts))


def jugs(sizes, labels=None):
    """Jugs as open-topped containers, each captioned with its capacity."""
    parts, x = [], 24
    for i, size in enumerate(sizes):
        w = 46 + size * 6
        parts.append(f'<path d="M{x} 20 L{x} 96 Q{x} 104 {x + 8} 104 '
                     f'L{x + w - 8} 104 Q{x + w} 104 {x + w} 96 L{x + w} 20" '
                     f'class="lg-fill"/>')
        parts.append(_text(x + w // 2, 68, f'{size} L'))
        if labels and i < len(labels):
            parts.append(_text(x + w // 2, 124, escape(labels[i]), 'lg-lbl lg-lbl--sm'))
        x += w + 34
    return _svg(x, 138, ''.join(parts))


def bridge(times, glyph='🚶'):
    """The night-crossing bridge: a span, a torch, and four walkers with times."""
    parts = [
        '<path d="M20 92 L120 92" class="lg-ln lg-ln--th"/>',
        '<path d="M280 92 L380 92" class="lg-ln lg-ln--th"/>',
        '<path d="M120 92 L280 92" class="lg-ln lg-ln--th" stroke-dasharray="8 5"/>',
        '<path d="M120 92 L120 62 M280 92 L280 62" class="lg-ln"/>',
        '<path d="M120 62 L280 62" class="lg-ln"/>',
        _glyph(200, 50, '🔦', 22),
        _text(200, 116, '1 torch · 2 people at a time', 'lg-lbl lg-lbl--sm'),
    ]
    for i, t in enumerate(times):
        x = 26 + i * 26
        parts.append(_glyph(x, 84, glyph, 20))
        parts.append(_text(x, 108, str(t), 'lg-lbl lg-lbl--sm'))
    return _svg(400, 128, ''.join(parts))
