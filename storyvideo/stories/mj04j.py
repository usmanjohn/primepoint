# -*- coding: utf-8 -*-
"""MJ-04j — «Ikki arqon: javob — ikki uchidan yoqing»   MANTIQ JUMBOGʻI · 4, JAVOB

Light A at BOTH ends and B at one end, together. A burns out at 30 minutes --
and its fronts meet far from the middle, which is the point: speed does not
matter, only the total. At that moment light B's other end: its remaining 30
minutes burn from both sides, 15 more. 30 + 15 = 45.
Ask (open, for comments): which other times can the two ropes measure?
Gate: verify_ropes.py (scratchpad).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate, Scene
from scenes import check, rule, ask, practice, outro
import ropekit as RP
import bridgekit as BK
import primitives as P

S = BK.say
SPM = 0.15
L = [(0, "A", "L"), (0, "A", "R"), (0, "B", "L"), (30, "B", "R")]


def ropes(name, lights, m0, m1, msg="", hold=0.8, at=0.6, **kw):
    r = RP.Ropes(lights)
    end = at + (m1 - m0) * SPM
    return Scene(round(end + hold, 2), r.html(m0, m1, at=at, spm=SPM, msg=msg, **kw),
                 cam="hold", name=name)


cover = ropes("cover", L, 45, 45, hold=3.6, msg=(
    S("Mantiq jumbogʻi · 4 · javob", "bk-kick", anim="none")
    + S("45 daqiqa", "bk-hero bk-grn", anim="none")
    + S("Sir: ikki uchidan yoqing", "bk-slab", anim="none")))
cover.note = "MUQOVA: ikkala arqon kul, soat 45."

secret = Scene(
    7.0,
    P.line("Sir", "lbl lbl--sm", at=0.0, anim="fade")
    + P.line("Arqonni IKKI uchidan yoqing", "ttl", at=0.4, anim="rise", dur=0.6)
    + P.line("1 soatlik arqon → 30 daqiqa", "big gold", at=1.8, anim="pop", dur=0.6),
    cam="push", dark=True, name="sir")

AT = 0.8
VIDEO = Video(
    slug="mj04j",
    lesson="Mantiq jumbogʻi 4 — javob",
    title="Ikki arqon: javob — ikki uchidan yoqing",
    story="MJ-04 · javob (savoli: mj04s)",
    subject="logic",
    scenes=[
        cover,
        ropes("eslatma", [], 0, 0, hold=1.8,
              msg=S("Kecha: notekis yonadi — kesib boʻlmaydi", "bk-txt", at=0.2)),
        secret,
        ropes("0 → 30", L, 0, 30, at=AT, hold=1.4, mid=True, msg=(
            S("A tugadi — 30 daqiqa!", "bk-txt bk-grn", at=AT + 30 * SPM + 0.1)
            + S("oʻrtada emas — muhim emas!", "bk-txt", at=AT + 30 * SPM + 0.9))),
        ropes("30 → 45", L, 30, 45, at=AT, hold=1.6, msg=(
            S("B ning ikkinchi uchi!", "bk-txt", at=0.2)
            + S("45!", "bk-hero bk-grn", at=AT + 15 * SPM + 0.1, anim="stamp", dur=0.6))),
        check("30 + 15 = 45", parts=["A: ikki uchidan — 30 daqiqa", "B: qolgan 30 → 15 daqiqa"],
              verdict="Aniq 45 daqiqa!", title="Sanaymiz", dur=7.4),
        rule("Ikki uchidan yoqilgan arqon ikki baravar tez tugaydi",
             meaning="Tezlik notekis boʻlsa ham — umumiy vaqt yarmiga tushadi.", dur=7.6),
        ask("Shu ikki arqon bilan yana qaysi vaqtlarni oʻlchash mumkin?", head="Endi siz",
            dur=6.0, note="Ochiq savol: 15, 30, 45, 60, 75, 90, 120… — izohlar uchun."),
        practice("Mantiq maydoni", sub="powerty.uz → Mantiq maydoni", dur=5.0),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Salom, yapaloqqushlar! || Kechagi arqon jumbogʻiga javob!",

    "Kecha: arqon notekis yonadi — | yarmini kesib, vaqtni oʻlchab boʻlmaydi.",

    "Sir: arqonni ikki uchidan yoqing. || Bir soatlik arqon oʻttiz daqiqada tugaydi.",

    "A ni ikki uchidan, B ni bitta uchidan yoqamiz. || A oʻttiz daqiqada tugaydi — | qarang, oʻrtada emas!",

    "Shu zahoti B ning ikkinchi uchini yoqamiz. | Qolgani ikki baravar tez yonadi. || [excited] Qirq besh!",

    "Oʻttiz qoʻshuv oʻn besh — | roppa-rosa qirq besh daqiqa.",

    "Qoida: | ikki uchidan yoqilgan arqon | ikki baravar tez tugaydi.",

    "Endi siz: | shu ikki arqon bilan yana qaysi vaqtlarni oʻlchash mumkin? || Izohda yozing!",

    "Har hafta yangi jumboqlar — Powertyda, Mantiq maydonida.",

    None,
])
