# -*- coding: utf-8 -*-
"""Shared by mj06s / mj06j — the choyxona and the money that moves in it."""
import stagekit as K
import people as _people

FRIENDS = [("Jasur", 150), ("Sherbek", 330), ("Otabek", 510)]
OWNER, WAITER = ("Anvar aka", 900), ("Ofitsiant", 720)
FEET = 1560


def person(st, who, x, size=230, mood="smile"):
    w = round(size * 100 / 175)
    return st.add(_people.figure(who, size=size, mood=mood), x, FEET - size / 2, w, size)


def room(st):
    for who, x in FRIENDS:
        person(st, who, x)
    person(st, *WAITER)
    person(st, *OWNER, size=250)
    st.add('<div class="sk-desk"></div>', OWNER[1], FEET - 70, 220, 140, z=2)
