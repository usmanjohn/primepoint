# -*- coding: utf-8 -*-
"""MJ-01j — «Tungi koʻprik: javob — 29 soniya»   MANTIQ JUMBOGʻI · 2-kun, JAVOB

Yesterday (mj01s): five people (1, 3, 6, 8, 12 s), one lantern that burns 30 s,
and the greedy plan dying at 32. Today: the plan that makes it in 29.

    →3 (Jasur+Afsona) ←1 (Jasur) →12 (Nodira opa+bobo) ←3 (Afsona)
    →3 (Jasur+Afsona) ←1 (Jasur) →6 (Jasur+Sherbek)  = 29

The two ideas, said in this order: the two slowest walk TOGETHER (8 hides
inside 12), and a fast walker must already be waiting on the far side to bring
the lantern back. Gate: scratchpad verify_bridge5.py -- Dijkstra over every
state proves 29 is the minimum (8 different plans reach it, none beats it).
"""

from spec import Video, narrate, Scene
from scenes import check, fact, rule, ask, practice, outro
import bridgekit as BK
import primitives as P

CAST = [("Jasur", 1), ("Afsona", 3), ("Sherbek", 6), ("Nodira opa", 8), ("Bobo", 12)]
PLAN = [(0, 1), (0,), (3, 4), (1,), (0, 1), (0,), (0, 2)]
S = BK.say


def bridge(name, show=(0, 0), msg="", hold=0.6, **kw):
    html, end, _ = BK.world(CAST, PLAN, show=show, msg=msg, **kw)
    return Scene(round(end + hold, 2), html, cam="hold", name=name)


cover = bridge(
    "cover", show=(7, 7), hold=3.6,
    msg=(S("Mantiq jumbogʻi · 1 · javob", "bk-kick", anim="none")
         + S("<span class='bk-red'>32</span> → 29", "bk-hero", anim="none")
         + S("Fonar oʻchmadi!", "bk-slab", anim="none")))
cover.note = "MUQOVA: hamma narigi tomonda, soat 29. Kechagi 32 → bugungi 29."

recap = bridge("eslatma", hold=2.0, msg=(
    S("Kecha: Jasur hammani kuzatdi", "bk-txt", at=0.2)
    + S("32 soniya — fonar oʻchdi", "bk-txt bk-red", at=1.4)))

secret = Scene(
    8.0,
    P.line("Sir", "lbl lbl--sm", at=0.0, anim="fade")
    + P.line("Ikki eng sekin — BIRGA", "ttl", at=0.4, anim="rise", dur=0.6)
    + P.expr("8 + 12 = 20", at=1.6, cls="strike", anim="shake", dur=0.6)
    + P.line("alohida yursa", "lbl lbl--sm", at=2.0, anim="fade")
    + P.expr("12", at=3.2, cls="grn", anim="stamp", dur=0.6)
    + P.line("birga yursa: 8 soniya 12 ichida yoʻqoladi", "cap", at=3.8, anim="rise"),
    cam="push", dark=True, name="sir", claims=["8 + 12 = 20"])

tripA = bridge("Jasur+Afsona, Jasur", show=(0, 2), at=0.5)
tripB = bridge("Nodira opa+bobo", show=(2, 3), at=1.4)
tripC = bridge("Afsona qaytadi", show=(3, 4), at=0.5)
tripD = bridge("oxirgi uchta", show=(4, 7), at=0.9, total=True, hold=1.2)

VIDEO = Video(
    slug="mj01j",
    lesson="Mantiq jumbogʻi 1 — javob",
    title="Tungi koʻprik: javob — 29 soniya",
    story="MJ-01 · javob (savoli: mj01s)",
    subject="logic",
    scenes=[
        cover,
        recap,
        secret,
        tripA,
        tripB,
        tripC,
        tripD,
        check("3 + 1 + 12 + 3 + 3 + 1 + 6 = 29",
              parts=["Fonar — 30 soniya", "1 soniya ortib ham qoldi"],
              verdict="Ulgurdi!", title="Sanaymiz", dur=7.6),
        fact("29", "bundan tez yoʻl yoʻq",
             cap="Kompyuter hamma variantni sinadi: eng kami — 29.",
             dark=True, dur=6.0),
        rule("Sekinlar birga yursin, tezlar fonar tashisin",
             meaning="Alohida: 8 + 12 soniya. Birga: atigi 12.", dur=8.0),
        ask("Siz topdingizmi? Izohda yozing!", head="Kechqurun — yangi jumboq",
            dur=5.6),
        practice("Mantiq maydoni", sub="powerty.uz → Mantiq maydoni", dur=5.0),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Xayrli tong, azizlarim! Yaxshi uxladingizmi? || Kechagi koʻprik jumbogʻiga javob!",

    "Kecha Jasur hammani bittalab kuzatdi. | Oʻttiz ikki soniya — fonar yetmadi.",

    "Sir: ikki eng sekin odam birga yursin. || Unda sakkiz soniya oʻn ikki ichiga yashirinadi.",

    "Avval ikki eng tezi oʻtadi: Jasur va Afsona — uch soniya. | Jasur fonarni qaytaradi — bir.",

    "Endi ikki eng sekini birga: | Nodira opa va bobo — oʻn ikki soniya.",

    "Fonarni Afsona qaytaradi — uch soniya. | U narigi tomonda shu uchun kutib turgandi!",

    "Qolgani oson: | Jasur va Afsona — uch, Jasur qaytadi — bir, | Jasur va Sherbek — olti.",

    "Sanaymiz: | uch, bir, oʻn ikki, uch, uch, bir, olti. || Yigirma toʻqqiz! [excited] Ulgurdi!",

    "Bundan tezroq yoʻl yoʻq — | kompyuter hamma variantni sinab chiqdi.",

    "Qoida: | sekinlar birga yursin, | tezlar esa fonarni tashisin.",

    "Siz topdingizmi, aqlli boshlar? Izohda yozing. || Kechqurun — yangi jumboq!",

    "Har hafta yangi jumboqlar — Powertyda, Mantiq maydonida.",

    None,   # outro
])
