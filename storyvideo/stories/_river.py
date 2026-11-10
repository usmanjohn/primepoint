# -*- coding: utf-8 -*-
"""Shared by mj03s / mj03j: one river, replayed to where a scene starts."""
from spec import Scene
import rivkit as RK


def river(name, before=(), now=(), msg="", hold=0.8, start=0.5):
    rv = RK.River()
    t = -90.0
    for item in before:
        t = rv.trip(item, t)
    rv.extra, rv.end = [], start
    t = start
    for item in now:
        t = rv.trip(item, t)
    return Scene(round(rv.end + hold, 2), rv.html(msg=msg), cam="hold", name=name), rv
