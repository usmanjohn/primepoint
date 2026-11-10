# -*- coding: utf-8 -*-
"""MJ-03j — «Boʻri, echki va karam: javob — echki ortga qaytadi»   MANTIQ JUMBOGʻI · 3, JAVOB

Seven crossings: goat →, back, wolf →, GOAT ←, cabbage →, back, goat →.
The twist said out loud: to go forward you sometimes carry something BACK.
rivkit's simulation checks every step -- an unsafe plan would show the loss.
Ask: a boat for two passengers? (3 crossings.) Gate: verify_river.py.
Sprinkles (noworry.txt): «oshqovoqchalar», «eshitayotgandinglarmi?»
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate
from scenes import rule, ask, practice, outro
from _river import river
import bridgekit as BK

S = BK.say
PLAN = ["G", None, "W", "G", "C", None, "G"]


def step(name, k, msg="", hold=0.8):
    sc, rv = river(name, before=PLAN[:k], now=[PLAN[k]], msg=msg, hold=hold)
    assert not rv.eaten, f"{name}: something got eaten -- the plan is wrong"
    return sc


cover, rv = river("cover", before=PLAN, hold=3.6, msg=(
    S("Mantiq jumbogʻi · 3 · javob", "bk-kick", anim="none")
    + S("7 qatnov", "bk-hero", anim="none")
    + S("Sir: echki ortga qaytadi", "bk-slab", anim="none")))
assert not rv.eaten and all(v == 1 for v in rv.side.values())
cover.note = "MUQOVA: hammasi narigi qirgʻoqda, butun-sogʻ. Pastda 7 ta chip."

recap, _ = river("eslatma", hold=1.8, msg=(
    S("Kecha: avval boʻri → karam ketdi", "bk-txt", at=0.2)
    + S("avval karam → echki ketdi", "bk-txt", at=1.3)))

VIDEO = Video(
    slug="mj03j",
    lesson="Mantiq jumbogʻi 3 — javob",
    title="Boʻri, echki va karam: javob",
    story="MJ-03 · javob (savoli: mj03s)",
    subject="logic",
    scenes=[
        cover, recap,
        step("echki →", 0, msg=S("1. Echki — narigi tomonga", "bk-txt", at=0.2)),
        step("← boʻsh", 1, msg=S("2. Yolgʻiz qaytadi", "bk-txt", at=0.2)),
        step("boʻri →", 2, msg=S("3. Boʻri — narigi tomonga", "bk-txt", at=0.2)),
        step("echki ←", 3, hold=1.4, msg=(
            S("Sir!", "bk-hero bk-grn", at=0.2, anim="stamp", dur=0.6)
            + S("4. Echki — ORTGA", "bk-txt", at=0.9))),
        step("karam →", 4, msg=S("5. Karam — boʻrining yoniga", "bk-txt", at=0.2)),
        step("← boʻsh 2", 5, msg=S("6. Yana yolgʻiz qaytadi", "bk-txt", at=0.2)),
        step("echki → oxirgi", 6, hold=2.0, msg=(
            S("7. Echki — va tamom!", "bk-txt", at=0.2)
            + S("Hammasi butun!", "bk-hero bk-grn", at=4.2, anim="pop", dur=0.6))),
        rule("Baʼzan oldinga yurish uchun orqaga qaytish kerak",
             meaning="Echkini qaytarish — yechimning kaliti.", dur=7.6),
        ask("Qayiqqa ikki yuk sigʻsa-chi? Necha qatnov kerak?", head="Endi siz",
            dur=6.0, note="Javob: 3 — aytmang."),
        practice("Mantiq maydoni", sub="powerty.uz → Mantiq maydoni", dur=5.0),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Salom, oshqovoqchalar! || Kechagi daryo jumbogʻiga javob!",

    "Kecha: avval boʻri — karam yeb qoʻyildi. | Avval karam — echki yeb qoʻyildi.",

    "Yagona xavfsiz birinchi qadam: echkini olib oʻtish. | Boʻri karamga tegmaydi.",

    "Anvar aka yolgʻiz qaytadi.",

    "Endi boʻrini olib oʻtadi... | lekin narigi tomonda echki kutyapti!",

    "Sir shu: | echkini ORTGA olib qaytadi! || [excited] Ana, gap qayerda!",

    "Karamni boʻrining yoniga qoʻyadi. | Boʻri karam yemaydi.",

    "Yana yolgʻiz qaytadi.",

    "Va nihoyat — echki. || Yetti qatnov, hammasi butun-sogʻ!",

    "Qoida: | baʼzan oldinga yurish uchun orqaga qaytish kerak.",

    "Endi siz: | qayiqqa ikkita yuk sigʻsa, necha qatnov kerak? || Izohda yozing!",

    "Har hafta yangi jumboqlar — Powertyda, Mantiq maydonida. | Eshitayotgandinglarmi?",

    None,
])
