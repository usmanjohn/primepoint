# -*- coding: utf-8 -*-
"""Shared by mj10s / mj10j — two doors, two guards, one question."""
import stagekit as K

DX = {"L": 290, "R": 790}
FREE = "L"                         # the door to freedom (the viewer learns it at the end)
GUARD = {"L": "Anvar aka", "R": "Farrux"}


def hall(reveal=False, open_free=None, labels=None):
    st = K.Stage()
    doors = {}
    for side, x in DX.items():
        light = st.add('<div class="sk-light"></div>', x, 1170, 200, 340, o=0, z=0)
        d = st.add(K.door(""), x, 1170, 230, 380, z=1)
        doors[side] = (d, light)
        lab = (labels or {}).get(side) or ("?" if not reveal else ("ozodlik" if side == FREE else "sher"))
        st.extra.append(f'<div class="ck-tag{" ck-tag--eq" if lab == "?" else ""}" '
                        f'style="left:{x}px;top:{970}px" data-at="0.000" data-dur="0.01" '
                        f'data-anim="none"><span{" class=rk-bad" if lab == "sher" else ""}>{lab}</span></div>')
        st.add(K.guard(GUARD[side], size=300), x, 1585, 171, 300, z=3)
    if open_free is not None:
        d, light = doors[FREE]
        light.to(open_free, 0.3, o=1)
        d.to(open_free, 0.8, sx=0.12, x=DX[FREE] - 100)
        st.mark("ck-found", open_free + 0.4)
        st.end = max(st.end, open_free + 1.0)
    return st


def bubble(st, text, x, y, at):
    b = st.add(f'<div class="sk-bubble">{text}</div>', x, y, 980, 90, z=6, o=0, s=0.6)
    b.to(at, 0.35, o=1, s=1.0)
    st.mark("rp-light", at)
    st.end = max(st.end, at + 0.5)
    return b


def point(st, side, at, red=True):
    """The guard's answer: an arrow landing on a door."""
    a = st.add('<b class="sk-arrow">▼</b>', DX[side], 790, 80, 80, z=6, o=0)
    a.to(at, 0.3, o=1)
    a.to(at, 0.5, y=925)
    st.mark("ck-tip", at + 0.4)
    st.end = max(st.end, at + 0.8)
