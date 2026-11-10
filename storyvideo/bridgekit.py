# -*- coding: utf-8 -*-
"""The night bridge — the drawing kit of the «Mantiq jumbogʻi» films.

Built 2026-10-29 for the two-day logic-puzzle series: the question one day,
the solution the next. The first puzzle is the five-person bridge: 1, 3, 6, 8
and 12 seconds, one lantern, and the lantern burns for 30 seconds.

The whole kit is ONE picture, `world()`, that can play any stretch of a
crossing plan. Every scene of a film is the same world at a later moment, so
the cut between two scenes is invisible (all bridge scenes use cam="hold") and
each scene can carry its own narration line — the voice says one trip while
the picture walks that trip. retime() then gives the scene whichever is
longer, the sentence or the walk.

Honest time is the rule: a walker crosses in exactly `sec × cost` seconds, the
clock in the corner counts the same seconds, and the lantern's fuel burns with
it. Jasur's 1-second dash really is twelve times faster than bobo's walk,
because that difference IS the puzzle.

The animation lives in anim.js `data-kf` tracks: piecewise linear, a pure
function of t like everything else in this package.
"""

import json
import random

import people as _people

W, H = 1080, 1920
BANK_Y = 1240                    # feet on both banks
BX0, BX1 = 350, 730              # where the deck starts and ends
MID, HW = (BX0 + BX1) / 2, (BX1 - BX0) / 2
SAG = 34                         # the deck hangs this far in the middle
SLOTS = {0: [300, 240, 180, 120, 60],        # left bank, nearest the bridge first
         1: [780, 840, 900, 960, 1020]}      # right bank
REST = {0: 334, 1: 746}          # the lantern on the ground, by the posts
LAG = 62                         # a follower walks this far behind the lead
STEP_PX = 40                     # one footstep per this many px of deck

# Badge colour by speed rank: the fastest green, the slowest red.
RANK = ["#3d7a5c", "#5f8a35", "#c9923a", "#c8703a", "#b84444"]


def deck_y(x):
    """The deck is the parabola a quadratic Bézier with its control point at
    2×SAG draws, so feet and planks agree exactly."""
    if BX0 <= x <= BX1:
        return BANK_Y + SAG * (1 - ((x - MID) / HW) ** 2)
    return BANK_Y


def _kf(tracks):
    """data-kf attribute. Times rounded so the stage stays small."""
    clean = {k: [[round(t, 3), round(v, 2)] for t, v in vs] for k, vs in tracks.items()}
    return f"data-kf='{json.dumps(clean, separators=(',', ':'))}'"


def _mark(cls, at, extra=""):
    return (f'<i class="{cls}" data-at="{at:.3f}" data-dur="0.01" '
            f'data-anim="none"{extra}></i>')


# ─────────────────────────────────────────────────────────── scenery ──
_UID = 0


def _backdrop(seed=7):
    rng = random.Random(seed)
    global _UID
    _UID += 1
    u = f"{_UID}"
    s = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
         '<defs><linearGradient id="bk-sky-{u}" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#08121c"/><stop offset=".5" stop-color="#132538"/>'
         '<stop offset=".7" stop-color="#1d3346"/><stop offset="1" stop-color="#0b1520"/>'
         '</linearGradient>'
         '<radialGradient id="bk-moon-{u}"><stop offset=".35" stop-color="#f5ecd2" stop-opacity=".30"/>'
         '<stop offset="1" stop-color="#f5ecd2" stop-opacity="0"/></radialGradient>'
         '<linearGradient id="bk-river-{u}" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#21466a"/><stop offset="1" stop-color="#10263a"/>'
         '</linearGradient></defs>',
         f'<rect width="{W}" height="{H}" fill="url(#bk-sky-{u})"/>']
    for _ in range(90):
        x, y = rng.uniform(0, W), rng.uniform(0, 1000)
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rng.uniform(1.0, 2.6):.1f}" '
                 f'fill="#fff" opacity="{rng.uniform(.25, .85):.2f}"/>')
    # moon, with a halo and two craters
    s.append('<circle cx="830" cy="400" r="170" fill="url(#bk-moon-{u})"/>'
             '<circle cx="830" cy="400" r="58" fill="#f4ecd6"/>'
             '<circle cx="813" cy="386" r="11" fill="#e3d9bd"/>'
             '<circle cx="847" cy="418" r="7" fill="#e3d9bd"/>')
    # far mountains, near hills
    s.append('<path d="M0 1010 L90 935 L170 985 L265 895 L360 968 L450 912 L560 985 '
             'L655 900 L760 972 L860 925 L960 992 L1080 938 L1080 1320 L0 1320 Z" '
             'fill="#172a3b"/>')
    s.append('<path d="M0 1120 Q 210 1040 430 1104 T 830 1092 T 1080 1078 '
             'L1080 1320 L0 1320 Z" fill="#111e2a"/>')
    # the gorge and its river
    s.append(f'<rect x="300" y="{BANK_Y}" width="480" height="{H - BANK_Y}" fill="#0a131c"/>')
    s.append('<path d="M300 1830 Q 540 1800 780 1830 L780 1920 L300 1920 Z" '
             'fill="url(#bk-river-{u})"/>')
    # cliffs (right one mirrored)
    left = [(0, BANK_Y), (BX0 + 2, BANK_Y), (366, 1300), (338, 1392), (372, 1500),
            (336, 1622), (362, 1760), (330, 1920), (0, 1920)]
    for pts in (left, [(W - x, y) for x, y in left]):
        s.append('<path d="M' + " L".join(f"{x} {y}" for x, y in pts) + ' Z" fill="#29231f"/>')
    for side in (1, -1):
        cx = 0 if side == 1 else W
        for y0 in (1330, 1450, 1580, 1700):
            x1 = cx + side * rng.uniform(40, 120)
            x2 = cx + side * rng.uniform(220, 300)
            s.append(f'<path d="M{x1:.0f} {y0} Q {(x1 + x2) / 2:.0f} {y0 - 18} '
                     f'{x2:.0f} {y0 + 6}" stroke="#1c1815" stroke-width="5" fill="none"/>')
    s.append(f'<rect x="0" y="{BANK_Y - 6}" width="{BX0 + 4}" height="14" rx="6" fill="#36553a"/>'
             f'<rect x="{BX1 - 4}" y="{BANK_Y - 6}" width="{W - BX1 + 4}" height="14" rx="6" '
             f'fill="#36553a"/>')
    # the bridge: posts, two hand ropes, planks, hangers
    for px in (BX0, BX1):
        s.append(f'<rect x="{px - 7}" y="1148" width="14" height="{BANK_Y - 1148 + 8}" '
                 f'rx="5" fill="#6b4a2e"/><circle cx="{px}" cy="1148" r="9" fill="#7d5a38"/>')
    for ry, sw in ((1160, 5), (1198, 4)):
        s.append(f'<path d="M{BX0} {ry} Q {MID} {ry + 2 * SAG} {BX1} {ry}" '
                 f'stroke="#9a7a55" stroke-width="{sw}" fill="none"/>')
    for x in range(BX0 + 20, BX1, 38):
        rope = 1160 + SAG * (1 - ((x - MID) / HW) ** 2)
        s.append(f'<line x1="{x}" y1="{rope:.1f}" x2="{x}" y2="{deck_y(x):.1f}" '
                 f'stroke="#7d6244" stroke-width="2.5"/>')
    s.append(f'<path d="M{BX0} {BANK_Y + 6} Q {MID} {BANK_Y + 6 + 2 * SAG} {BX1} {BANK_Y + 6}" '
             f'stroke="#4d3520" stroke-width="5" fill="none"/>')
    for x in range(BX0 + 2, BX1 - 10, 17):
        y = deck_y(x + 6)
        s.append(f'<rect x="{x}" y="{y - 1:.1f}" width="13" height="9" rx="2" '
                 f'fill="#8b6239" stroke="#5a3e24" stroke-width="1.5"/>')
    s.append('</svg>')
    # ids must be unique per scene: every scene's drawing sits in one page, and
    # url(#id) resolves to the FIRST match -- inside a hidden scene, so it paints nothing
    return "".join(s).replace("{u}", u)


def _ambient(span=60.0):
    """Stars that breathe and a river that moves, so a held frame is never dead."""
    rng = random.Random(11)
    out = []
    for i in range(9):
        x, y = rng.uniform(40, 640), rng.uniform(380, 950)
        per = rng.uniform(1.6, 3.2)
        keys, t = [], rng.uniform(0, per)
        while t < span:
            keys += [[t, 0.25], [t + per / 2, 1.0]]
            t += per
        out.append(f'<i class="bk-star" style="left:{x:.0f}px;top:{y:.0f}px" '
                   f'{_kf({"o": keys})}></i>')
    for i, (x, y, w) in enumerate([(330, 1846, 90), (470, 1870, 120), (610, 1852, 80),
                                   (400, 1895, 70), (660, 1898, 60)]):
        drift = 26 if i % 2 else -26
        keys, t, k = [], 0.0, 0
        while t < span:
            keys.append([t, x + (drift if k % 2 else 0)])
            t += 2.4
            k += 1
        out.append(f'<i class="bk-shim" style="top:{y}px;width:{w}px" '
                   f'{_kf({"x": keys})}></i>')
    return '<div class="bk-amb" data-backdrop>' + "".join(out) + '</div>'


_LAMP = ('<svg class="bk-lampsvg" viewBox="0 0 50 72" width="50" height="72">'
         '<path d="M14 12 Q25 -2 36 12" stroke="#3b2c1e" stroke-width="3.5" fill="none"/>'
         '<rect x="11" y="12" width="28" height="7" rx="3" fill="#4a3624"/>'
         '<rect x="13" y="19" width="24" height="38" rx="6" fill="#ffe7a8" fill-opacity=".28" '
         'stroke="#4a3624" stroke-width="3"/>'
         '<rect x="9" y="57" width="32" height="9" rx="3" fill="#4a3624"/></svg>')

_CLOCK = ('<svg viewBox="0 0 60 60" width="64" height="64"><circle cx="30" cy="32" r="24" '
          'fill="none" stroke="#f6d58e" stroke-width="5"/><rect x="24" y="1" width="12" '
          'height="7" rx="3" fill="#f6d58e"/><path d="M30 32 L30 17 M30 32 L40 38" '
          'stroke="#f6d58e" stroke-width="5" stroke-linecap="round"/></svg>')


# ──────────────────────────────────────────────────────────── a trip ──
def _path(frm, to, entry, exit_, fa, fb):
    """Position at progress u: walk to the deck, cross it, walk to the slot."""
    def at(u):
        if u <= fa:
            x = frm + (entry - frm) * (u / fa if fa else 1)
            return x, BANK_Y
        if u <= fa + fb:
            x = entry + (exit_ - entry) * ((u - fa) / fb)
            return x, deck_y(x)
        x = exit_ + (to - exit_) * ((u - fa - fb) / max(1 - fa - fb, 1e-6))
        return x, BANK_Y
    return at


ZOOM, FOCUS_Y = 1.4, 1300       # the follow camera: how close, where the banks sit


def _cam(keys):
    """[(t, z, cx)] -> kf tracks for the camera layer, clamped so the picture
    never shows past the edge of the drawn world."""
    xs, ys, ss = [], [], []
    for t, z, cx in keys:
        half = W / (2 * z)
        cx = min(max(cx, half), W - half)
        xs.append([t, W / 2 - z * cx])
        ys.append([t, min(0, max(H - z * H, FOCUS_Y - z * BANK_Y))])
        ss.append([t, z])
    return {"x": xs, "y": ys, "s": ss}


def world(cast, plan, show=(0, 0), lamp=30, at=0.6, sec=0.45, gap=0.55,
          intro=None, hud=True, ledger=True, total=False, msg="", light=True,
          zoom=ZOOM, cam=None):
    """The whole bridge picture, playing trips show[0]..show[1]-1 of `plan`.

    cast   [("Jasur", 1), ("Afsona", 3), ...]   index = position in this list
    plan   [(0, 1), (0,), (3, 4), ...]          who crosses on each trip; the
           first index of a pair is the LEAD -- he carries the lantern
    show   which trips this scene animates; earlier ones are already done
    intro  seconds between people dropping in one by one (None = all present)
    msg    HTML put in the sky above the bridge (titles, verdicts)
    zoom   the follow camera: it holds this zoom and pans with the lantern
    cam    [(t, z, cx)] to drive the camera by hand instead (a pull-back)

    Returns (html, end_seconds, info) -- info has the clock total and, if the
    lantern ran out, the moment it did.
    """
    n = len(cast)
    secs = [c for _, c in cast]
    order = sorted(range(n), key=lambda i: secs[i])
    slot_of = {p: order.index(p) for p in range(n)}
    side = [0] * n
    lamp_side, cum = 0, 0
    for grp in plan[:show[0]]:
        for p in grp:
            side[p] = 1 - side[p]
        lamp_side = 1 - lamp_side
        cum += max(secs[p] for p in grp)

    def home(p):
        return SLOTS[side[p]][slot_of[p]]

    tr = {p: {"x": [[0, home(p)]], "y": [[0, BANK_Y]], "m": [[0, 0]]} for p in range(n)}
    lx0 = REST[lamp_side]
    lampk = {"x": [[0, lx0]], "y": [[0, BANK_Y]], "m": [[0, 0]]}
    lightk = {"--lx": [[0, lx0]], "--ly": [[0, BANK_Y - 40]],
              "--lr": [[0, 360 if light else 0]]}
    clock = {"n": [[0, cum]]}
    fuel = {"--fuel": [[0, max(0, (lamp - cum) / lamp * 100)]]}
    flame = {"s": [[0, 1]]}
    marks, chips = [], []

    # chips for the trips already walked
    for k, grp in enumerate(plan[:show[0]]):
        chips.append(_chip(k, grp, secs, None))

    t, died, end = at, None, at
    for k in range(show[0], show[1]):
        grp = plan[k]
        cost = max(secs[p] for p in grp)
        D = cost * sec
        s = 1 if lamp_side == 0 else -1
        lead = grp[0]
        entry = BX0 + 10 if s > 0 else BX1 - 10
        exit_ = entry + s * (BX1 - BX0)
        frm = home(lead)
        to = SLOTS[1 - side[lead]][slot_of[lead]]
        dA, dB, dC = abs(entry - frm), abs(exit_ - entry), abs(to - exit_)
        tot = dA + dB + dC
        fa, fb = dA / tot, dB / tot

        cut = 1.0
        if cum + cost > lamp:
            cut = (lamp - cum) / cost
            died = t + cut * D

        chips.append(_chip(k, grp, secs, t))
        for j, p in enumerate(grp):
            off = -s * LAG * j
            f = _path(home(p), SLOTS[1 - side[p]][slot_of[p]],
                      entry + off, exit_ + off, fa, fb)
            us = sorted({i / 28 for i in range(29)} | {fa, fa + fb})
            us = [u for u in us if u <= cut] + ([cut] if cut < 1 else [])
            for u in us:
                x, y = f(u)
                tr[p]["x"].append([t + u * D, x])
                tr[p]["y"].append([t + u * D, y])
            ramp = min(0.12, D / 4)
            stop = t + cut * D
            tr[p]["m"] += [[t, 0], [t + ramp, 1], [stop - ramp, 1], [stop, 0]]

        # the lantern: on the ground, then in the lead's hand on the deck,
        # then on the ground at the far post
        lead_f = _path(frm, to, entry, exit_, fa, fb)
        hand = lambda u: (lead_f(u)[0] + s * 40, lead_f(u)[1] - 18)
        pick, drop = t + fa * D, t + (fa + fb) * D
        lampk["x"].append([max(pick - 0.08, t), REST[lamp_side]])
        lampk["y"].append([max(pick - 0.08, t), BANK_Y])
        for u in [fa + fb * i / 20 for i in range(21)]:
            if u > cut:
                break
            hx, hy = hand(u)
            lampk["x"].append([t + u * D, hx])
            lampk["y"].append([t + u * D, hy])
        lampk["m"] += [[pick, 0], [pick + 0.05, 1],
                       [min(drop, t + cut * D) - 0.05, 1], [min(drop, t + cut * D), 0]]
        if cut >= 1:
            lampk["x"].append([drop + 0.1, REST[1 - lamp_side]])
            lampk["y"].append([drop + 0.1, BANK_Y])
        else:
            hx, hy = hand(cut)
            lampk["x"].append([t + cut * D, hx])
            lampk["y"].append([t + cut * D, hy])
        for key in ("x", "y"):
            lightk["--l" + key] += [[tt, v - (40 if key == "y" else 0)]
                                   for tt, v in lampk[key][-(len(lampk[key]) - 1):]
                                   if tt >= t]

        # footsteps: knocks on the planks, read off the lead's walk
        if dB:
            for i in range(1, int(dB // STEP_PX) + 1):
                u = fa + fb * (i * STEP_PX / dB)
                if u <= cut:
                    marks.append(_mark("bk-step", t + u * D))

        stop = t + cut * D
        clock["n"] += [[t, cum], [stop, cum + cost * cut]]
        fuel["--fuel"] += [[t, max(0, (lamp - cum) / lamp * 100)],
                           [stop, max(0, (lamp - cum - cost * cut) / lamp * 100)]]
        if died:
            flame["s"] += [[died, 1], [died + 0.5, 0]]
            lightk["--lr"] += [[died, 360], [died + 0.7, 0]]
            marks.append(_mark("bk-out", died))
            end = died + 0.8
            break
        for p in grp:
            side[p] = 1 - side[p]
        lamp_side = 1 - lamp_side
        cum += cost
        end = t + D
        t += D + gap

    if total and not died:
        chips.append(f'<span class="bk-tot{" bk-grn" if cum <= lamp else " bk-red"}" '
                     f'data-at="{end + 0.25:.3f}" data-dur="0.45" data-anim="pop">= {cum}</span>')
        end += 0.7

    # ── assemble, back to front ──
    if cam is None:
        cam = [(tt, zoom, x) for tt, x in lampk["x"]]
    h = ['<div class="bk">', f'<div class="bk-cam" data-camera {_kf(_cam(cam))}>',
         '<div class="bk-bg" data-backdrop>', _backdrop(), '</div>', _ambient()]
    for p in sorted(range(n), key=lambda p: -secs[p]):
        who, c = cast[p]
        size = 192 if _people.CAST.get(who, {}).get("adult") else 166
        w = round(size * 100 / 175)
        fig = (f'<div class="bk-fig" style="left:{-w / 2:.0f}px;top:{-size}px;width:{w}px">'
               f'{_people.figure(who, size=size)}'
               f'<span class="bk-num" style="background:{RANK[min(order.index(p), 4)]}">'
               f'{c}</span></div>')
        person = f'<div class="bk-p" {_kf(tr[p])}>{fig}</div>'
        if intro is not None:
            person = (f'<div class="bk-in" data-at="{at + intro * order.index(p):.3f}" '
                      f'data-dur="0.5" data-anim="drop">{person}</div>')
        h.append(person)
    h.append(f'<div class="bk-dark" data-backdrop {_kf(lightk)}></div>')
    h.append(f'<div class="bk-p bk-lamp" {_kf(lampk)}>'
             f'<i class="bk-glow" {_kf({"o": [[t_, v] for t_, v in flame["s"]]})}></i>'
             f'{_LAMP}<i class="bk-flame" {_kf(flame)}></i></div>')
    h.append('</div>')          # end of the camera layer; the HUD does not move
    if hud:
        h.append('<div class="bk-hud">'
                 f'<div class="bk-clk">{_CLOCK}<b class="bk-n" {_kf(clock)}>{cum}</b>'
                 f'<span class="bk-of">/ {lamp} soniya</span></div>'
                 '<div class="bk-fuel"><span class="bk-fuel__l">fonar</span>'
                 f'<div class="bk-bar"><i class="bk-fill" {_kf(fuel)}></i></div></div>'
                 '</div>')
    if ledger:
        h.append('<div class="bk-ledger">' + "".join(chips) + '</div>')
    if msg:
        h.append(f'<div class="bk-msg">{msg}</div>')
    h += marks
    h.append(_mark("bk-end", end))
    h.append('</div>')
    return "".join(h), end, {"clock": cum, "died": died}


def _chip(k, grp, secs, at):
    cost = max(secs[p] for p in grp)
    arrow = "→" if k % 2 == 0 else "←"
    cls = "bk-led" + (" bk-led--back" if k % 2 else "")
    tm = (f'data-at="{at:.3f}" data-dur="0.4" data-anim="pop"' if at is not None
          else 'data-at="0.000" data-dur="0.01" data-anim="none"')
    return f'<span class="{cls}" {tm}>{arrow} {cost}</span>'


# ───────────────────────────────────────────────────── sky messages ──
def say(text, cls="bk-txt", at=0.0, anim="rise", dur=0.5):
    """One line in the sky. cls: bk-kick | bk-hero | bk-slab | bk-txt (+ bk-red/bk-grn)."""
    return (f'<div class="{cls}" data-at="{at:.3f}" data-dur="{dur:.2f}" '
            f'data-anim="{anim}">{text}</div>')
