# -*- coding: utf-8 -*-
"""The balance scale — «Mantiq jumbogʻi» #2, nine coins (2026-10-29).

Nine numbered gold coins, one of them a lighter fake that looks exactly like
the rest, and a brass balance. Same contract as bridgekit: `Table` plays a
sequence of weighings as data-kf tracks, and every scene is the same table
at a later moment (cam="hold"), so the cuts disappear.

The scale is physical enough to read at a glance: the beam tips with an
overshoot and settles, the pans hang plumb from the beam ends, and the coins
ride in the pans. The lighter side goes UP -- that is the whole signal.
"""

import math

from bridgekit import _kf, _mark, say      # noqa: F401  (say is re-exported)

W, H = 1080, 1920
PIVOT = (540, 940)
HALF = 300                 # half beam length
STRING = 220               # hook to pan rim
TILT = 11.0                # degrees, lighter side up
COIN = 92                  # diameter
ROW_Y = 1530               # coin row centre on the table
ROW_X = [76 + i * 116 for i in range(9)]
# where coins sit inside a pan, relative to the pan's hook point
PAN_SLOTS = {1: [(0, 0)], 2: [(-50, 0), (50, 0)], 3: [(-50, 0), (50, 0), (0, -84)],
             4: [(-50, 0), (50, 0), (-50, -84), (50, -84)]}
PAN_FLOOR = STRING - 12    # coin centre height below the hook, bottom row


def _ends(deg):
    a = math.radians(deg)
    dx, dy = HALF * math.cos(a), HALF * math.sin(a)
    return (PIVOT[0] - dx, PIVOT[1] - dy), (PIVOT[0] + dx, PIVOT[1] + dy)


_UID = 0


def _backdrop():
    global _UID
    _UID += 1
    u = f"{_UID}"
    s = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
         '<defs><linearGradient id="ck-wood-{u}" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#b47a45"/><stop offset="1" stop-color="#7d4f2a"/>'
         '</linearGradient>'
         '<linearGradient id="ck-brass-{u}" x1="0" y1="0" x2="1" y2="0">'
         '<stop offset="0" stop-color="#9c7326"/><stop offset=".5" stop-color="#e8c36a"/>'
         '<stop offset="1" stop-color="#9c7326"/></linearGradient></defs>',
         f'<rect width="{W}" height="{H}" fill="#f3ebdd"/>']
    for x in range(0, W, 90):                       # a plastered wall, faint panels
        s.append(f'<rect x="{x + 8}" y="0" width="74" height="1290" rx="6" '
                 f'fill="#efe5d4"/>')
    # an arch window behind the scale, so the frame has a place
    s.append('<path d="M330 1180 L330 640 Q540 470 750 640 L750 1180 Z" fill="#e4d6bf"/>'
             '<path d="M360 1180 L360 655 Q540 510 720 655 L720 1180 Z" fill="#d9e6ee"/>'
             '<path d="M540 540 L540 1180 M360 860 L720 860" stroke="#c9b494" '
             'stroke-width="10"/>')
    # the table
    s.append('<rect x="0" y="1290" width="1080" height="34" fill="#8a5a31"/>'
             '<rect x="0" y="1320" width="1080" height="600" fill="url(#ck-wood-{u})"/>')
    for y in (1400, 1520, 1650, 1790):
        s.append(f'<path d="M0 {y} Q 540 {y - 14} 1080 {y + 6}" stroke="#6e4423" '
                 f'stroke-opacity=".35" stroke-width="3" fill="none"/>')
    # the scale's base and column (they never move)
    px, py = PIVOT
    s.append(f'<ellipse cx="{px}" cy="1300" rx="150" ry="22" fill="#5d4013" opacity=".35"/>'
             f'<path d="M{px - 120} 1300 Q {px} 1240 {px + 120} 1300 Z" fill="url(#ck-brass-{u})"/>'
             f'<rect x="{px - 13}" y="{py}" width="26" height="{1262 - py}" rx="8" '
             f'fill="url(#ck-brass-{u})"/>')
    s.append('</svg>')
    # ids must be unique per scene: every scene's drawing sits in one page, and
    # url(#id) resolves to the FIRST match -- inside a hidden scene, so it paints nothing
    return "".join(s).replace("{u}", u)


_BEAM = (f'<svg viewBox="0 0 {2 * HALF + 40} 150" width="{2 * HALF + 40}" height="150">'
         '<path d="M{c} 128 L{c} 20" stroke="#5d4013" stroke-width="6" stroke-linecap="round"/>'
         '<rect x="14" y="120" width="{w}" height="18" rx="9" fill="#c99a3f" '
         'stroke="#7a5716" stroke-width="3"/>'
         '<circle cx="20" cy="129" r="12" fill="#a87c2c"/><circle cx="{e}" cy="129" r="12" '
         'fill="#a87c2c"/>'
         '<circle cx="{c}" cy="129" r="19" fill="#e8c36a" stroke="#7a5716" stroke-width="4"/>'
         '</svg>').format(c=HALF + 20, w=2 * HALF + 12, e=2 * HALF + 20)

_PAN = ('<svg viewBox="-120 -10 240 {h}" width="240" height="{hh}">'
        '<path d="M0 0 L-100 {s} M0 0 L100 {s} M0 0 L0 {s}" stroke="#6b5530" '
        'stroke-width="3"/>'
        '<path d="M-112 {s} Q 0 {d} 112 {s} Z" fill="#d4a94f" stroke="#7a5716" '
        'stroke-width="4"/></svg>').format(s=STRING, d=STRING + 70,
                                            h=STRING + 84, hh=STRING + 84)


class Table:
    """Nine coins and a balance. Call weigh()/back()/dim()/reveal() in order,
    then html(). Times are scene-relative seconds."""

    def __init__(self, fake=7, n=9, home=None):
        self.n, self.fake = n, fake
        self.pos = {c: (ROW_X[c - 1], ROW_Y) for c in range(1, n + 1)}
        if home:
            self.pos.update(home)
        # Initial keys sit far in the past: a scene replays what came before it
        # at negative times, and keys must stay in time order.
        T0 = -999
        self.tr = {c: {"x": [[T0, x]], "y": [[T0, y]], "o": [[T0, 1]]}
                   for c, (x, y) in self.pos.items()}
        self.ring = {c: {"o": [[T0, 0]]} for c in self.pos}
        self.beam = {"r": [[T0, 0]]}
        L, R = _ends(0)
        self.pans = [{"x": [[T0, L[0]]], "y": [[T0, L[1]]]},
                     {"x": [[T0, R[0]]], "y": [[T0, R[1]]]}]
        self.count, self.counter = 0, {"n": [[T0, 0]]}
        self.extra, self.inpan, self.angle = [], {}, 0.0

    def _move(self, c, t0, dur, to, lift=150):
        (x0, y0), (x1, y1) = self.pos[c], to
        top = min(y0, y1) - lift
        for f, x, y in ((0, x0, y0), (.3, x0 + (x1 - x0) * .15, top),
                        (.75, x1, top + 20), (1, x1, y1)):
            self.tr[c]["x"].append([t0 + f * dur, x])
            self.tr[c]["y"].append([t0 + f * dur, y])
        self.pos[c] = to

    def weigh(self, left, right, at, load=0.75, step=0.14, settle=1.2, label=True):
        """Load both pans, release the beam, let it settle. Returns end time."""
        L, R = _ends(self.angle)
        t = at
        for side, group, end in ((0, left, L), (1, right, R)):
            for k, c in enumerate(group):
                dx, dy = PAN_SLOTS[len(group)][k]
                self._move(c, t + k * step, load, (end[0] + dx, end[1] + PAN_FLOOR + dy))
                self.inpan[c] = (side, dx, dy)
                self.extra.append(_mark("ck-drop", t + k * step + load))
        t += max(len(left), len(right)) * step + load + 0.25
        wl = sum(0.9 if c == self.fake else 1 for c in left)
        wr = sum(0.9 if c == self.fake else 1 for c in right)
        target = 0.0 if abs(wl - wr) < 1e-9 else (TILT if wr > wl else -TILT)
        # the counter ticks as the beam is released
        self.count += 1
        self.counter["n"] += [[t - 0.01, self.count - 1], [t, self.count]]
        self.extra.append(_mark("ck-tip", t))
        # overshoot and settle; a balanced beam still wobbles before it rests
        keys = [(0, self.angle), (.35, target * 1.35 if target else 4),
                (.65, target * .82 if target else -2.5), (1, target)]
        for f, a in keys:
            tt = t + f * settle
            self.beam["r"].append([tt, a])
            l, r = _ends(a)
            for i, e in enumerate((l, r)):
                self.pans[i]["x"].append([tt, e[0]])
                self.pans[i]["y"].append([tt, e[1]])
            for c, (side, dx, dy) in self.inpan.items():
                e = (l, r)[side]
                self.tr[c]["x"].append([tt, e[0] + dx])
                self.tr[c]["y"].append([tt, e[1] + PAN_FLOOR + dy])
                self.pos[c] = (e[0] + dx, e[1] + PAN_FLOOR + dy)
        self.angle = target
        t += settle
        if label:
            l, r = _ends(target)
            if target == 0:
                txt, x, y, cls = "teng", PIVOT[0], PIVOT[1] - 150, "ck-tag ck-tag--eq"
            else:
                up = l if target > 0 else r
                txt, x, y, cls = "yengil", up[0], up[1] - 64, "ck-tag"
            self.extra.append(f'<div class="{cls}" style="left:{x:.0f}px;top:{y:.0f}px" '
                              f'data-at="{t - 0.2:.3f}" data-dur="0.45" data-anim="pop">'
                              f'<span>{txt}</span></div>')
        self.end = t
        return t

    def back(self, at, coins=None, step=0.08, dur=0.6):
        """Coins out of the pans, back to their places in the row."""
        coins = coins or list(self.inpan)
        for k, c in enumerate(sorted(coins)):
            self._move(c, at + k * step, dur, (ROW_X[c - 1], ROW_Y), lift=90)
            self.inpan.pop(c, None)
        t = at + len(coins) * step + dur + 0.2
        # the beam comes level once the pans are empty
        if not self.inpan and self.angle:
            self.beam["r"] += [[t - 0.3, self.angle], [t + 0.3, 0]]
            l, r = _ends(0)
            for i, e in enumerate(_ends(self.angle)):
                self.pans[i]["x"].append([t - 0.3, e[0]]); self.pans[i]["y"].append([t - 0.3, e[1]])
            for i, e in enumerate((l, r)):
                self.pans[i]["x"].append([t + 0.3, e[0]]); self.pans[i]["y"].append([t + 0.3, e[1]])
            self.angle = 0.0
            t += 0.3
        self.end = t
        return t

    def dim(self, coins, at, to=0.28):
        """Coins proved genuine fade back."""
        for c in coins:
            self.tr[c]["o"] += [[at, self.tr[c]["o"][-1][1]], [at + 0.4, to]]
        return at + 0.4

    def reveal(self, at):
        c = self.fake
        self.ring[c]["o"] += [[at, 0], [at + 0.3, 1]]
        self.extra.append(_mark("ck-found", at))
        return at + 0.3

    def html(self, msg="", hud=True, limit=2):
        h = ['<div class="ck">', f'<div class="ck-bg" data-backdrop>{_backdrop()}</div>']
        bx, by = PIVOT[0] - HALF - 20, PIVOT[1] - 129
        h.append(f'<div class="ck-beam" style="left:{bx}px;top:{by}px" {_kf(self.beam)}>'
                 f'{_BEAM}</div>')
        for p in self.pans:
            h.append(f'<div class="ck-pan" {_kf(p)}><div class="ck-pan__in">{_PAN}</div></div>')
        for c in sorted(self.tr):
            h.append(f'<div class="ck-coin" {_kf(self.tr[c])}><div class="ck-coin__in">'
                     f'<i class="ck-ring" {_kf(self.ring[c])}></i><b>{c}</b></div></div>')
        if hud:
            h.append(f'<div class="ck-hud"><span class="ck-hud__l">Tortish</span>'
                     f'<b class="ck-n" {_kf(self.counter)}>0</b>'
                     f'<span class="ck-hud__of">/ {limit}</span></div>')
        if msg:
            h.append(f'<div class="bk-msg ck-msg">{msg}</div>')
        h += self.extra
        h.append(_mark("ck-end", getattr(self, "end", 0.5)))
        h.append('</div>')
        return "".join(h)
