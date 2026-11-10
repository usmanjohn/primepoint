# -*- coding: utf-8 -*-
"""Shared by mj07s / mj07j — ants on a one-metre stick.

The motion is computed the honest way: every ant is a 'ghost' walking straight
at 1 cm/s; real ants never pass each other, so at any moment the k-th real ant
(left to right) stands where the k-th ghost does. When ghosts cross, the real
ants turn round -- which IS the collision rule. The scratchpad gate checks this
against a step-by-step bounce simulation (verify_batch2.py).
"""
import stagekit as K

X0, X1, Y = 90, 990, 1240          # the stick, 100 cm
CM = (X1 - X0) / 100
SPS = 0.075                         # real seconds per puzzle second
# (position cm, direction) -- chosen so the last ant leaves at 94 s
ANTS = [(6, 1), (18, -1), (30, 1), (42, -1), (55, 1), (66, -1), (78, 1), (90, -1)]


def ghosts_at(t):
    return [p + d * t for p, d in ANTS]


def last_fall():
    return max((100 - p) if d > 0 else p for p, d in ANTS)


def stick_stage(t_end, at=0.6, colour_swap=False, ghosts=False, upto=None):
    """Play puzzle seconds 0..t_end from scene time `at` (real seconds)."""
    st = K.Stage()
    st.add('<div class="sk-stick"></div>', (X0 + X1) / 2, Y + 22, X1 - X0, 24)
    for c in range(0, 101, 10):
        st.extra.append(f'<i class="sk-tickm" style="left:{X0 + c * CM:.0f}px;top:{Y + 40}px"></i>')
    n = len(ANTS)
    real = [st.add(K.ant(col=("#3b2a20" if i % 2 else "#a23b2a") if colour_swap else "#3b2a20"),
                   X0 + ANTS[i][0] * CM, Y - 6, 56, 34, s=1.8, z=3) for i in range(n)]
    for i, a in enumerate(real):
        a.set(-900, sx=ANTS[i][1])
    gone = set()
    steps = int(t_end / 0.25) + 1
    for k in range(steps + 1):
        tp = min(k * 0.25, t_end)
        tr = at + tp * SPS
        g = sorted((p + d * tp, d) for p, d in ANTS)
        on = [(x, d) for x, d in g if 0 < x < 100]
        left_out = sum(1 for x, _ in g if x <= 0)
        for i, a in enumerate(real):
            j = i - left_out
            if i in gone:
                continue
            if 0 <= j < len(on):
                x, d = on[j]
                a.tr["x"].append([tr, X0 + x * CM]); a.cur["x"] = X0 + x * CM
                if a.cur["sx"] != d:
                    a.set(tr, sx=d)
            else:                                   # this ant has walked off an end
                gone.add(i)
                a.to(tr, 0.35, y=Y + 320, o=0)
                st.mark("ck-drop", tr)
    if ghosts:
        for p, d in ANTS:
            gh = st.add(K.ant(col="#3b6ea5"), X0 + p * CM, Y - 90, 56, 34, o=0.4, s=1.5)
            gh.set(-900, sx=d)
            out = (100 - p) if d > 0 else p              # when this ghost leaves the stick
            gh.to(at, out * SPS, x=X1 if d > 0 else X0)
            gh.to(at + out * SPS, 0.3, o=0)
    st.end = at + t_end * SPS + 0.4
    clock = K.counter("Vaqt", [(at, 0), (at + t_end * SPS, round(t_end))], "soniya")
    return st, clock
