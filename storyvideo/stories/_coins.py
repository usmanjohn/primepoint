# -*- coding: utf-8 -*-
"""Shared by mj02s / mj02j: one table, replayed to the state a scene starts in.

A scene's Table replays everything before it at negative times (so the coins
are already where the last scene left them) and then plays its own steps from
t = 0.5. The replay's labels and sound marks are dropped -- they belong to the
scene that played them.
"""
from spec import Scene
import coinkit as CK

FAKE = 7


def W(left, right, label=True):
    return lambda tb, t: tb.weigh(left, right, t, label=label)


def B(coins=None):
    return lambda tb, t: tb.back(t, coins)


def D(coins):
    return lambda tb, t: tb.dim(coins, t)


def R():
    return lambda tb, t: tb.reveal(t)


def table(name, before=(), now=(), msg="", hold=0.8, limit=2, start=0.5):
    tb = CK.Table(fake=FAKE)
    t = -90.0
    for f in before:
        t = f(tb, t)
    tb.extra, tb.end = [], start
    t = start
    for f in now:
        t = f(tb, t)
    return Scene(round(tb.end + hold, 2), tb.html(msg=msg, limit=limit),
                 cam="hold", name=name)
