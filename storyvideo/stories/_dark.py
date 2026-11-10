# -*- coding: utf-8 -*-
"""Shared by mj09s / mj09j — 100 coins, 10 heads ('gerb'), a blindfold.

Every coin is two faces at one spot; a flip squeezes the visible face to sx=0,
swaps which face shows, and opens the other -- a real turn, not a fade.
"""
import random
import stagekit as K

R = random.Random(14)   # seed chosen so the 50/50 split is UNEVEN (6 vs 4)
HEADS = set(R.sample(range(100), 10))
# the ten coins taken aside in the answer: exactly 3 of them heads
_h = sorted(HEADS)[:3]
_t = [i for i in R.sample(range(100), 40) if i not in HEADS][:7]
PICK = sorted(_h + _t)
D, GAP = 66, 82


def pos(i):
    return 171 + (i % 10) * GAP, 880 + (i // 10) * GAP


def row_pos(k):
    return 171 + k * GAP, 1735


class Coins:
    def __init__(self, st, appear=None):
        self.st, self.c = st, {}
        for i in range(100):
            x, y = pos(i)
            h = st.add(K.coin_face(True, D), x, y, D, D, o=1 if i in HEADS else 0, z=2)
            t = st.add(K.coin_face(False, D), x, y, D, D, o=0 if i in HEADS else 1, z=2)
            if appear is not None:
                for f in (h, t):
                    f.set(-900, s=0.2)
                    f.to(appear + (i // 10) * 0.08, 0.25, s=1.0)
            self.c[i] = [h, t, i in HEADS]

    def move(self, i, t, x, y, dur=0.5):
        for f in self.c[i][:2]:
            f.to(t, dur, x=x, y=y)

    def flip(self, i, t, dur=0.36):
        h, tl, up = self.c[i]
        show, hide = (tl, h) if up else (h, tl)
        hide.to(t, dur / 2, sx=0)
        hide.set(t + dur / 2, o=0)
        show.set(t, sx=0)
        show.set(t + dur / 2, o=1)
        show.to(t + dur / 2, dur / 2, sx=1)
        self.c[i][2] = not up
        self.st.mark("ck-drop", t + dur / 2)
