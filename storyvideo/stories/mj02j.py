# -*- coding: utf-8 -*-
"""MJ-02j — «Toʻqqizta tanga: javob — uchta guruh»   MANTIQ JUMBOGʻI · 2, JAVOB

Split into three groups of three. 1,2,3 vs 4,5,6 balances, so the fake is in
7,8,9; then 7 vs 8 -- the left pan rises, #7 is the fake. The insight said
out loud: a balance gives THREE answers (left, right, level), so each weighing
cuts the suspects by three: 9 -> 3 -> 1. Ask: 27 coins? (3 weighings.)
Gate: verify_coins9.py (scratchpad).
Sprinkles (noworry.txt): «ismlaring yaxshimi?», the «Hunarni asrabon» couplet.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate, Scene
from scenes import check, rule, ask, outro
from _coins import table, W, B, D, R
import bridgekit as BK
import primitives as P

S = BK.say
W1, W2 = W([1, 2, 3], [4, 5, 6]), W([7], [8])
ALL = [W1, D([1, 2, 3, 4, 5, 6]), B(), W2, R()]

cover = table("cover", before=ALL, hold=3.6, msg=(
    S("Mantiq jumbogʻi · 2 · javob", "bk-kick", anim="none")
    + S("2 tortish", "bk-hero", anim="none")
    + S("Sir — 3 ta guruh", "bk-slab", anim="none")))
cover.note = "MUQOVA: qalbaki 7-tanga qizil halqada, tarozi chapga koʻtarilgan."

groups = Scene(
    7.5,
    P.line("Sir", "lbl lbl--sm", at=0.0, anim="fade")
    + P.line("Ikkiga emas — UCHGA boʻling", "ttl", at=0.4, anim="rise", dur=0.6)
    + P.solve([("1 2 3", "1-guruh"), ("4 5 6", "2-guruh"), ("7 8 9", "3-guruh")],
              at=1.6, step=0.7)[0],
    cam="push", name="uch guruh")

three = Scene(
    8.0,
    P.line("Tarozi 3 xil javob beradi", "ttl", at=0.0, anim="rise", dur=0.6)
    + P.solve([("chap yengil", "qalbaki: 1, 2, 3"), ("oʻng yengil", "qalbaki: 4, 5, 6"),
               ("teng", "qalbaki: 7, 8, 9")], at=1.0, step=0.9)[0],
    cam="push", name="uch javob")

poem = Scene(
    7.0,
    P.line("Hunarni asrabon netgumdir oxir,", "ttl", at=0.3, anim="rise", dur=0.7)
    + P.line("olib tuprogʻimga ketgumdir oxir.", "ttl", at=1.5, anim="rise", dur=0.7)
    + P.line("Yechimni doʻstingizga ulashing!", "lbl gold", at=3.2, anim="pop", dur=0.6),
    cam="push", dark=True, name="baytt")

VIDEO = Video(
    slug="mj02j",
    lesson="Mantiq jumbogʻi 2 — javob",
    title="Toʻqqizta tanga: javob — uchta guruh",
    story="MJ-02 · javob (savoli: mj02s)",
    subject="logic",
    scenes=[
        cover,
        table("eslatma", hold=1.6, msg=S("Kecha: 4 ga 4 → 3 tortish", "bk-txt", at=0.2)),
        groups,
        table("3 ga 3", now=[W1, D([1, 2, 3, 4, 5, 6])], hold=1.2,
              msg=S("Teng! Qalbaki — 7, 8, 9 ichida", "bk-txt", at=3.4)),
        three,
        table("7 ga 8", before=[W1, D([1, 2, 3, 4, 5, 6])], now=[B(), W2, R()], hold=1.6,
              msg=(S("7-tanga!", "bk-hero bk-red", at=4.0, anim="stamp", dur=0.6)
                   + S("Teng chiqsa — 9-tanga boʻlardi", "bk-txt", at=4.8))),
        check("3 × 3 = 9", parts=["1-tortish: 9 → 3", "2-tortish: 3 → 1"],
              verdict="2 tortish yetarli!", title="Nega ishlaydi", dur=7.4),
        rule("Har tortish — uchta javob: chap, oʻng, teng",
             meaning="Shubhalilarni har safar uchga boʻling.", dur=7.6),
        ask("27 ta tanga boʻlsa-chi? Necha tortish kerak?", head="Endi siz",
            dur=6.0, note="Javob: 3 (3 × 3 × 3 = 27) — aytmang."),
        poem,
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Salom, azizlar, ismlaring yaxshimi? || Kechagi toʻqqizta tangaga javob!",

    "Kecha toʻrttaga toʻrtta qoʻydik — | uch marta tortishga toʻgʻri keldi.",

    "Sir: tangalarni ikkiga emas, uchga boʻling. || Har guruhda uchtadan.",

    "Birinchi guruhni ikkinchisiga qoʻyamiz. || Teng! | Demak, qalbaki — uchinchi guruhda.",

    "Tarozi uch xil javob beradi: | chap, oʻng yoki teng. || Shuning uchun uchga boʻlamiz.",

    "Endi yettiga sakkiz. | Chap tomon yengil! || Qalbaki — yettinchi tanga.",

    "Har tortish shubhalilarni uch barobar kamaytiradi: | toʻqqiz, uch, bir.",

    "Qoida: | tarozi uch xil javob beradi — | uchalasidan ham foydalaning.",

    "Endi siz: | yigirma yettita tanga boʻlsa, necha tortish kerak? || Izohda yozing!",

    "Hunarni asrabon netgumdir oxir, | olib tuprogʻimga ketgumdir oxir. || Yechimni doʻstingizga ham yuboring!",

    None,
])
