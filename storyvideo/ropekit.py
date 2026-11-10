# -*- coding: utf-8 -*-
"""Two burning ropes — «Mantiq jumbogʻi» #4: measure 45 minutes.

Each rope burns out in exactly 60 minutes but UNEVENLY: a rope here is a list
of segments with their own burn times, so a fire front crawls on one stretch
and races on the next. A rope lit at both ends has two fronts; they meet
wherever the burn time on each side is equal -- after 30 minutes, and almost
never in the middle. That non-middle meeting point is the picture that sells
the answer, so it is computed, never placed by hand.

`Ropes.html(m0, m1, at, spm)` shows the state at minute m0 and animates
minutes m0..m1 starting at scene time `at`, `spm` real seconds per minute.
Same data-kf contract as the other kits.
"""

from bridgekit import _kf, _mark, say      # noqa: F401

X0, X1 = 130, 950
Y = {"A": 980, "B": 1250}
# minutes per segment (equal lengths). Both sum to 60.
PROFILE = {"A": [3, 7, 32, 18], "B": [22, 14, 9, 15]}
T0 = -999


def _pos_from_left(rope, minutes):
    """Where a front lit at the LEFT end is after `minutes`."""
    segs = PROFILE[rope]
    seg_len = (X1 - X0) / len(segs)
    x, m = X0, minutes
    for c in segs:
        if m <= c:
            return x + seg_len * m / c
        m -= c
        x += seg_len
    return X1


def _pos_from_right(rope, minutes):
    segs = PROFILE[rope][::-1]
    seg_len = (X1 - X0) / len(segs)
    x, m = X1, minutes
    for c in segs:
        if m <= c:
            return x - seg_len * m / c
        m -= c
        x -= seg_len
    return X0


def _flicker(seed, span=60.0):
    """A flame never holds still. Periodic, but each flame on its own beat."""
    keys, t, k = [[T0, 1]], 0.0, seed % 3
    while t < span:
        keys.append([t, (1.0, 0.82, 1.12, 0.9)[k % 4]])
        t += 0.11 + 0.03 * ((k * 7 + seed) % 3)
        k += 1
    return {"s": keys}


class Ropes:
    def __init__(self, lights):
        """lights: [(minute, "A"|"B", "L"|"R")] -- when each end is set alight."""
        self.lights = lights

    def state(self, rope, m):
        """(left_edge, right_edge, left_burning, right_burning, done) at minute m."""
        lt = [mm for mm, r, e in self.lights if r == rope and e == "L" and mm <= m]
        rt = [mm for mm, r, e in self.lights if r == rope and e == "R" and mm <= m]
        a = _pos_from_left(rope, m - lt[0]) if lt else X0
        b = _pos_from_right(rope, m - rt[0]) if rt else X1
        if a >= b:                                   # the fronts have met
            return a, a, False, False, True
        return a, b, bool(lt), bool(rt), False

    def burnout(self, rope, step=0.01):
        m = 0.0
        while m < 200:
            if self.state(rope, m)[4]:
                return round(m, 2)
            m += step
        return None

    def html(self, m0, m1, at=0.5, spm=0.12, msg="", hud=True, mid=False):
        grid = [m0 + (m1 - m0) * i / 240 for i in range(241)] if m1 > m0 else [m0]
        events = sorted({mm for mm, _, _ in self.lights if m0 < mm <= m1}
                        | {self.burnout(r) or 999 for r in "AB"})
        grid = sorted(set(grid) | {e for e in events if m0 <= e <= m1})
        rt = lambda m: at + (m - m0) * spm
        h = ['<div class="rp">', '<div class="rp-bg" data-backdrop></div>']
        if mid:
            h.append(f'<div class="rp-mid" style="left:{(X0 + X1) / 2:.0f}px" '
                     f'data-at="{at:.3f}" data-dur="0.4" data-anim="fade">'
                     f'<span>oʻrtasi</span></div>')
        for r in "AB":
            ka = {"--a": [[T0, X0]], "--b": [[T0, X1]]}
            fl = {"x": [[T0, X0]], "o": [[T0, 0]]}
            fr = {"x": [[T0, X1]], "o": [[T0, 0]]}
            for i, m in enumerate(grid):
                a, b, lb, rb, done = self.state(r, m)
                t = T0 + 1 if i == 0 else rt(m)
                if i == 0:
                    ka = {"--a": [[T0, a]], "--b": [[T0, b]]}
                    fl = {"x": [[T0, a]], "o": [[T0, 1 if lb else 0]]}
                    fr = {"x": [[T0, b]], "o": [[T0, 1 if rb else 0]]}
                    continue
                ka["--a"].append([t, a]); ka["--b"].append([t, b])
                fl["x"].append([t, a]); fl["o"].append([t, 1 if lb else 0])
                fr["x"].append([t, b]); fr["o"].append([t, 1 if rb else 0])
            y = Y[r]
            h.append(f'<div class="rp-ash" style="top:{y + 7}px;left:{X0}px;width:{X1 - X0}px"></div>')
            h.append(f'<div class="rp-rope" style="top:{y}px" {_kf(ka)}></div>')
            h.append(f'<b class="rp-name" style="top:{y - 30}px">{r}</b>')
            for f in (fl, fr):
                h.append(f'<div class="rp-fire" style="top:{y + 10}px" {_kf(f)}>'
                         f'<i class="rp-flame" {_kf(_flicker(len(h)))}></i></div>')
            # lighting and burning-out moments, for the sound layer
            for mm, rr, _ in self.lights:
                if rr == r and m0 < mm <= m1:
                    h.append(_mark("rp-light", rt(mm)))
            bo = self.burnout(r)
            if bo and m0 < bo <= m1:
                h.append(_mark("rp-out", rt(bo)))
        if hud:
            clock = {"n": [[T0, m0]], }
            if m1 > m0:
                clock["n"] += [[at, m0], [rt(m1), m1]]
            h.append('<div class="bk-hud"><div class="bk-clk">'
                     '<svg viewBox="0 0 60 60" width="64" height="64"><circle cx="30" cy="32" r="24" '
                     'fill="none" stroke="#f6d58e" stroke-width="5"/><path d="M30 32 L30 17 M30 32 '
                     'L40 38" stroke="#f6d58e" stroke-width="5" stroke-linecap="round"/></svg>'
                     f'<b class="bk-n" {_kf(clock)}>{m0}</b><span class="bk-of">daqiqa</span>'
                     '</div></div>')
        if msg:
            h.append(f'<div class="bk-msg rp-msg">{msg}</div>')
        h.append(_mark("rp-end", rt(m1) if m1 > m0 else at))
        h.append('</div>')
        return "".join(h)
