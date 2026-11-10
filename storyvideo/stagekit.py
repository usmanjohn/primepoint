# -*- coding: utf-8 -*-
"""A free stage for the «Mantiq jumbogʻi» films that need no world of their own
(batch 2, 2026-10-29: wine, missing soʻm, ants, pirates, coins in the dark, guards).

`Stage` holds Things -- drawn assets placed by their CENTRE -- and every Thing
moves by data-kf tracks (x, y, o, s, sx, r). `to()` appends a move from wherever
the thing is to a new state, so a spec reads as a list of actions. Initial keys
sit at T0 = -999 (see coinkit: replayed keys must stay in time order).
The assets below are drawn here, in the house style: flat, warm, readable at
120 px.
"""
from bridgekit import _kf, _mark, say          # noqa: F401
import people as _people

T0 = -999


class Thing:
    def __init__(self, html, x, y, w, h, z=0, o=1.0, s=1.0, cls=""):
        self.html, self.w, self.h, self.z, self.cls = html, w, h, z, cls
        self.cur = {"x": x, "y": y, "o": o, "s": s, "sx": 1.0, "r": 0.0}
        self.tr = {k: [[T0, v]] for k, v in self.cur.items()}

    def to(self, t, dur=0.5, **kw):
        for k, v in kw.items():
            self.tr[k] += [[t, self.cur[k]], [t + dur, v]]
            self.cur[k] = v
        return t + dur

    def set(self, t, **kw):
        return self.to(t, 0.001, **kw)

    def render(self):
        rest = {"s": 1.0, "sx": 1.0, "r": 0.0}
        tr = {k: v for k, v in self.tr.items()
              if len(v) > 1 or k in ("x", "y", "o") or v[0][1] != rest.get(k)}
        return (f'<div class="sk-t {self.cls}" style="z-index:{self.z}" {_kf(tr)}>'
                f'<div class="sk-in" style="left:{-self.w / 2:.0f}px;top:{-self.h / 2:.0f}px;'
                f'width:{self.w}px;height:{self.h}px">{self.html}</div></div>')


class Stage:
    def __init__(self, bg="paper"):
        self.bg, self.things, self.extra, self.end = bg, [], [], 0.5

    def add(self, *a, **k):
        t = Thing(*a, **k)
        self.things.append(t)
        return t

    def mark(self, cls, at):
        self.extra.append(_mark(cls, at))
        self.end = max(self.end, at)

    def tag(self, text, x, y, at, red=False):
        self.extra.append(f'<div class="ck-tag" style="left:{x:.0f}px;top:{y:.0f}px" '
                          f'data-at="{at:.3f}" data-dur="0.45" data-anim="pop">'
                          f'<span{" class=rk-bad" if red else ""}>{text}</span></div>')
        self.end = max(self.end, at + 0.5)

    def html(self, msg="", hud=""):
        h = [f'<div class="sk sk--{self.bg}">']
        h += [t.render() for t in self.things]
        if hud:
            h.append(hud)
        if msg:
            h.append(f'<div class="bk-msg {"ck-msg" if self.bg != "dark" else "rp-msg"}">{msg}</div>')
        h += self.extra
        h.append(_mark("sk-end", self.end))
        h.append('</div>')
        return "".join(h)


def counter(label, keys, unit="", x=64, y=80):
    """A HUD number driven by keys [(t, value)] -- a readout, not an animation."""
    return (f'<div class="ck-hud" style="left:{x}px;top:{y}px"><span class="ck-hud__l">{label}</span>'
            f'<b class="ck-n" {_kf({"n": [[T0, keys[0][1]]] + [list(k) for k in keys]})}>'
            f'{keys[0][1]}</b><span class="ck-hud__of">{unit}</span></div>')


# ───────────────────────────────────────────────────────────── assets ──
def bottle(label="", w=70, h=150, poison=False):
    lab = f'<b class="sk-lab">{label}</b>' if label else ""
    liq = "#c0392b" if poison else "#8e44ad"
    return (f'<svg viewBox="0 0 70 150" width="{w}" height="{h}">'
            f'<rect x="26" y="0" width="18" height="12" rx="3" fill="#7a5230"/>'
            f'<path d="M28 12 L42 12 L42 40 Q 64 52 64 76 L64 140 Q64 148 56 148 L14 148 Q6 148 6 140 '
            f'L6 76 Q6 52 28 40 Z" fill="#e8f1f5" stroke="#5f7d8c" stroke-width="3"/>'
            f'<path d="M9 86 L61 86 L61 140 Q61 145 55 145 L15 145 Q9 145 9 140 Z" fill="{liq}" '
            f'opacity=".85"/></svg>{lab}')


def mouse(asleep=False, w=150, h=110):
    eye = ('<path d="M108 44 Q114 48 120 44" stroke="#222" stroke-width="3" fill="none"/>'
           if asleep else '<circle cx="114" cy="44" r="5" fill="#222"/>')
    return (f'<svg viewBox="0 0 150 110" width="{w}" height="{h}">'
            '<path d="M18 74 Q -6 60 6 34" stroke="#d9a6ad" stroke-width="5" fill="none"/>'
            '<ellipse cx="66" cy="70" rx="52" ry="32" fill="#9aa3ab"/>'
            '<circle cx="96" cy="30" r="20" fill="#9aa3ab"/><circle cx="96" cy="30" r="11" fill="#e8b4bc"/>'
            '<ellipse cx="114" cy="52" rx="30" ry="24" fill="#a9b2ba"/>'
            '<circle cx="142" cy="58" r="6" fill="#e07a8a"/>' + eye +
            '<path d="M60 100 L54 108 M84 100 L90 108" stroke="#7b848c" stroke-width="5"/></svg>')


def zzz():
    return '<b class="sk-zzz">Zzz</b>'


def bill(amount, w=210, h=100):
    return (f'<div class="sk-bill" style="width:{w}px;height:{h}px"><span>{amount}</span></div>')


def ant(w=56, h=34, col="#3b2a20"):
    return (f'<svg viewBox="0 0 56 34" width="{w}" height="{h}">'
            f'<ellipse cx="12" cy="18" rx="11" ry="9" fill="{col}"/><ellipse cx="28" cy="18" rx="7" ry="6" fill="{col}"/>'
            f'<circle cx="44" cy="16" r="9" fill="{col}"/>'
            f'<path d="M22 22 L16 33 M28 23 L28 34 M34 22 L40 33 M48 9 L54 1 M44 8 L46 0" stroke="{col}" '
            f'stroke-width="2.5" fill="none"/><circle cx="47" cy="14" r="2" fill="#fff"/></svg>')


def coin_face(heads=True, d=72):
    if heads:
        return (f'<div class="sk-coin" style="width:{d}px;height:{d}px"><span>★</span></div>')
    return (f'<div class="sk-coin sk-coin--t" style="width:{d}px;height:{d}px"><span>1</span></div>')


def pirate(who, size=200, mood="smile", rank=""):
    fig = _people.figure(who, size=size, mood=mood)
    w = round(size * 100 / 175)
    hat = (f'<svg class="sk-hat" viewBox="0 0 100 50" width="{w * 1.25:.0f}" '
           f'style="left:{-w * 0.125:.0f}px;top:{-size * 0.02:.0f}px">'
           '<path d="M4 40 Q 50 -6 96 40 Q 50 30 4 40 Z" fill="#1d1d1f"/>'
           '<circle cx="50" cy="24" r="7" fill="#f4efe6"/>'
           '<path d="M45 20 L55 28 M55 20 L45 28" stroke="#1d1d1f" stroke-width="2"/></svg>')
    r = f'<b class="sk-rank">{rank}</b>' if rank else ""
    return f'<div class="sk-pir" style="width:{w}px;height:{size}px">{fig}{hat}{r}</div>'


def guard(who, size=260, mood="smile"):
    fig = _people.figure(who, size=size, mood=mood)
    w = round(size * 100 / 175)
    helm = (f'<svg class="sk-hat" viewBox="0 0 100 60" width="{w:.0f}" style="left:0;top:{-size * 0.05:.0f}px">'
            '<path d="M14 46 Q 14 6 50 6 Q 86 6 86 46 Z" fill="#8a8f96"/>'
            '<rect x="8" y="42" width="84" height="10" rx="5" fill="#6d7279"/>'
            '<path d="M50 6 L50 -2" stroke="#c0392b" stroke-width="8"/></svg>')
    return f'<div class="sk-pir" style="width:{w}px;height:{size}px">{fig}{helm}</div>'


def door(label, w=230, h=380, col="#8a5a31"):
    return (f'<svg viewBox="0 0 230 380" width="{w}" height="{h}">'
            f'<path d="M10 380 L10 90 Q 115 -10 220 90 L220 380 Z" fill="{col}" stroke="#4d3019" stroke-width="8"/>'
            '<path d="M40 370 L40 110 Q 115 40 190 110 L190 370" stroke="#4d3019" stroke-width="4" fill="none" opacity=".5"/>'
            '<circle cx="180" cy="240" r="10" fill="#e8c36a"/></svg>'
            f'<b class="sk-doorlab">{label}</b>')
