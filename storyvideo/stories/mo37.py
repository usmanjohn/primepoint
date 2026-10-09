# -*- coding: utf-8 -*-
"""MO-37 — «Tugʻilgan kun paradoksi: 23 kishi yetarli»   MATEMATIKA OLAMI · jumboq

Manba: Matematika olami, order 37 (the football-pitch framing).

The turn: our intuition hears «someone shares MY birthday» (253 people for
50 %), but the question is «ANY two» -- and 23 people make 253 pairs. Same
number, the reading's own coincidence.

Percentages, recomputed exactly in the scratchpad gate (365 days):
    10 -> 11,7 %   23 -> 50,7 %   30 -> 70,6 %   70 -> 99,9 %
Bars show whole numbers rounded: 12 · 51 · 71, and 99 for 70 people (99,9 %
truncated, never 100 -- it is not certain).
"""

from spec import Video, narrate, Scene
from scenes import cover, claim, beat, fact, versus, rule, ask, practice, outro
import primitives as P

_pairs, ps = P.solve([
    ("23 × 22 = 506", "har kim qolgan 22 kishi bilan juft"),
    ("506 ÷ 2 = 253", "har juft ikki marta sanalgan"),
], at=0.7, step=1.5)
pairs = Scene(
    9.0,
    P.line("Istalgan ikki kishi: juftliklarni sanaymiz", "lbl lbl--sm",
           at=0.0, anim="fade")
    + _pairs
    + P.line("253 ta juftlik — 253 ta imkoniyat", "ttl grn",
             at=0.7 + ps + 0.3, anim="pop", dur=0.6),
    cam="sink", top=True, name="juftliklar",
    claims=["23 × 22 = 506", "506 ÷ 2 = 253"])

_b, bs = P.bars([(12, "10 kishi", ""), (51, "23 kishi", "win"),
                 (71, "30 kishi", ""), (99, "70 kishi", "")],
                at=0.7, step=0.8)
growth = Scene(
    8.6,
    P.line("Mos tushish ehtimoli, %", "lbl lbl--sm", at=0.0, anim="fade") + _b,
    cam="push", top=True, name="oʻsish",
    note="70 kishida 99,9 % — 100 emas, lekin deyarli.")

VIDEO = Video(
    slug="mo37",
    lesson="Matematika olami",
    title="Tugʻilgan kun paradoksi: 23 kishi yetarli",
    story="Matematika olami — order 37",
    subject="math",
    scenes=[
        cover("5 %", "Aslida — yarmidan koʻp",
              kicker="Matematika olami",
              context="23 kishi. Ikkitasining tugʻilgan kuni bir kunda:",
              note="MUQOVA: hamma aytadigan «5 %» chizilgan."),

        claim("Sardor", "365 kun, 23 kishi", "5 %",
              doubt="Juda kam-ku?", dur=7.8),

        beat(dur=4.0, n=3,
             note="ATAYLAB JIM. Tomoshabin oʻz taxminini qilsin."),

        fact("50,7 %", "23 kishida",
             cap="Har ikki futbol oʻyinidan birida maydonda bir kunda tugʻilgan ikki kishi bor.",
             dur=7.0, cam="pull"),

        versus({"name": "«mening kunimda»", "qty": "253",
                "price": "kishi kerak", "tag": "bitta odamga bogʻlab", "cls": "lose"},
               {"name": "«istalgan ikkitasi»", "qty": "23",
                "price": "kishi yetadi", "tag": "har bir juftlik", "cls": "win"},
               title="Sezgimiz boshqa savolni eshitadi",
               dur=9.4),

        pairs,

        growth,

        rule("Odamlar sekin koʻpayadi, juftliklar — tez",
             strip="juftliklar = n × (n − 1) ÷ 2",
             meaning="Muhandislar ikki kompyuter kodi tasodifan bir xil "
                     "chiqishini xuddi shu hisob bilan baholaydi.",
             dur=9.0),

        ask("Sinfingizda 30 kishi boʻlsa, ertaga tekshiring: "
            "bir kunda tugʻilganlar bormi?",
            dur=7.0),

        practice("Burchak · Matematika olami",
                 sub="powerty.uz → Burchak → Matematika olami",
                 dur=5.2),

        outro(),
    ],
)

narrate(VIDEO, [
    "Futbol maydonida yigirma uch kishi. "
    "|| Ikkitasining tugʻilgan kuni bir kunda boʻlishi ehtimoli qancha?",

    "Koʻpchilik aytadi: yilda uch yuz oltmish besh kun, odam atigi yigirma uch. "
    "|| Nari borsa besh foiz.",

    None,   # beat

    "Toʻgʻri javob — [gasps] ellik foizdan koʻp. "
    "|| Har ikki oʻyindan birida.",

    "Biz savolni oʻzimizga bogʻlaymiz: kimdir aynan mening kunimda "
    "tugʻilganmi? || Bunga koʻp odam kerak.",

    "Savol esa — istalgan ikki kishi. | Har bir juftlik — yangi imkoniyat. "
    "|| Yigirma uch kishida ikki yuz ellik uch juftlik bor.",

    "Odam koʻpaygan sari ehtimol tez oʻsadi. | Oʻttiz kishida — yetmish bir "
    "foiz. || Yetmish kishida — deyarli yuz.",

    "Odamlar sekin koʻpayadi, juftliklar esa tez. "
    "|| Shuning uchun sezgimiz adashadi.",

    "Sinfingizda oʻttiz kishi boʻlsa, ertaga tekshirib koʻring, jonginalar. "
    "|| Natijani izohda yozing.",

    "Bunday hikoyalar — Powertyda, Burchak boʻlimida.",

    None,   # outro
])
