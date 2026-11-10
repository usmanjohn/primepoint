# -*- coding: utf-8 -*-
"""MJ-03s — «Boʻri, echki va karam»   MANTIQ JUMBOGʻI · 3, SAVOL

Anvar aka must take a wolf, a goat and a cabbage across a river. The boat holds
him and ONE passenger. Left alone, the wolf eats the goat and the goat eats the
cabbage. Today: the obvious first move (take the wolf) fails on screen -- the
simulation in rivkit.py decides that, not the script. Tomorrow (mj03j): seven
crossings, and the goat goes BACK.
Gate: verify_river.py (scratchpad) -- BFS: minimum 7 crossings; every first
move except the goat loses something.
Sprinkle (noworry.txt): «Familiyam necha edi?»
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate
from scenes import ask, fact, outro
from _river import river
import bridgekit as BK

S = BK.say

cover, _ = river("cover", hold=3.4, msg=(
    S("Mantiq jumbogʻi · 3", "bk-kick", anim="none")
    + S("Boʻri, echki, karam", "bk-slab", anim="none")
    + S("Hammasi butun oʻtsin!", "bk-txt", anim="none")))
cover.note = "MUQOVA: daryo boʻyida Anvar aka, boʻri, echki, karam va qayiq."

intro, _ = river("kimlar", hold=2.0, msg=S("Qayiqqa: dehqon + bitta yuk", "bk-txt", at=0.3))
rules, _ = river("xavf", hold=2.0, msg=(
    S("Boʻri + echki → echki yoʻq", "bk-txt bk-red", at=0.3)
    + S("Echki + karam → karam yoʻq", "bk-txt bk-red", at=1.5)))
wolf, rv = river("avval boʻri", now=["W"], hold=1.6, msg=S(
    "1-urinish: avval boʻri", "bk-txt", at=0.0, anim="fade"))
assert rv.eaten == {"C"}, "the wolf-first plan must lose the cabbage"
cab, rv = river("avval karam", now=["C"], hold=1.6, msg=S(
    "2-urinish: avval karam", "bk-txt", at=0.0, anim="fade"))
assert rv.eaten == {"G"}, "the cabbage-first plan must lose the goat"

VIDEO = Video(
    slug="mj03s",
    lesson="Mantiq jumbogʻi 3 — savol",
    title="Boʻri, echki va karam",
    story="MJ-03 · savol (javobi: mj03j)",
    subject="logic",
    scenes=[
        cover, intro, rules, wolf, cab,
        fact("Echki", "birinchi oʻtsa-chi?",
             cap="Keyingi qadamda yana muammo chiqadi…", dark=True, dur=5.4, cam="push"),
        ask("Hammasini butun-sogʻ qanday oʻtkazasiz?", head="Yoʻli bor!", dur=6.0,
            note="Javobni aytmang: 7 qatnov, echki ORTGA qaytadi — ertaga."),
        fact("Ertaga", "yechimini koʻrsatamiz",
             cap="Javobingizni izohga yozing!", dark=True, dur=5.0, cam="push"),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Salom, doʻstlar! Familiyam necha edi? || [laughs] Mayli. Bugun — daryo jumbogʻi.",

    "Anvar aka boʻri, echki va karamni daryodan oʻtkazishi kerak. "
    "| Qayiqqa — u va bitta yuk.",

    "Lekin yolgʻiz qolsa: | boʻri echkini yeydi, | echki esa karamni.",

    "Avval boʻrini olib oʻtsa-chi? || [gasps] Voy! Karamni echki yeb qoʻydi!",

    "Unda avval karamni... || Endi boʻri echkini yedi!",

    "Echki birinchi oʻtsa-chi? | Keyingi qadamda yana muammo.",

    "Hammasini butun-sogʻ qanday oʻtkazadi? || Oʻylab koʻring!",

    "Javobingizni izohga yozing. || Yechimi — ertaga!",

    None,
])
