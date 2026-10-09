# -*- coding: utf-8 -*-
"""MO-34 — «Tungi koʻprik: toʻrt kishi va bitta fonar»   MATEMATIKA OLAMI · jumboq

Manba: Matematika olami, order 34.  Subject: logic.

The greedy plan (the fastest person escorts everyone) is the plausible wrong
answer and lands on screen as a claim: 10 + 1 + 5 + 1 + 2 = 19. The fix is to
send the two slowest TOGETHER: 2 + 1 + 10 + 2 + 2 = 17, which is optimal for
{1, 2, 5, 10} (verified by BFS over all states in the scratchpad gate).

The ask (grandfather walks 3 minutes instead of 10) has answer 12 -- and both
plans tie there, which is the comment-section discussion we want.
"""

from spec import Video, narrate, Scene
from scenes import cover, beat, claim, check, fact, rule, ask, practice, outro
import primitives as P

_who, whs = P.solve([
    ("Jasur",   "1 daqiqa"),
    ("Afsona",  "2 daqiqa"),
    ("Sherbek", "5 daqiqa"),
    ("Bobo",    "10 daqiqa"),
], at=0.7, step=0.9)
speeds = Scene(
    8.6,
    P.line("Kim qancha yuradi", "lbl lbl--sm", at=0.0, anim="fade") + _who
    + P.line("Juftlik — sekinrogʻining tezligida", "ttl", at=0.7 + whs + 0.3,
             anim="pop", dur=0.6),
    cam="sink", top=True, name="tezliklar")

_smart, sms = P.solve([
    ("2",  "Jasur + Afsona oʻtadi"),
    ("1",  "Jasur fonarni qaytaradi"),
    ("10", "Sherbek + Bobo BIRGA oʻtadi"),
    ("2",  "Afsona fonarni qaytaradi"),
    ("2",  "Jasur + Afsona oʻtadi"),
], at=0.7, step=1.1)
smart = Scene(
    10.4,
    P.line("Ikki eng sekinni birga yuboring", "lbl lbl--sm", at=0.0, anim="fade")
    + _smart,
    cam="sink", top=True, name="aqlli reja",
    note="Fonarni qaytaradigan tez odam narigi tomonda OLDINDAN turibdi.")

VIDEO = Video(
    slug="mo34",
    lesson="Matematika olami",
    title="Tungi koʻprik: toʻrt kishi va bitta fonar",
    story="Matematika olami — order 34",
    subject="logic",
    scenes=[
        cover("19 daqiqa", "Aslida — 17",
              kicker="Mantiq jumbogʻi",
              context="Toʻrt kishi, bitta fonar, tor koʻprik:",
              note="MUQOVA: hamma topadigan 19 chizilgan; vaʼda — 17."),

        fact("2 kishi", "koʻprik bir vaqtda koʻtaradi",
             cap="Tun. Fonar bitta. Fonarsiz koʻprikka chiqib boʻlmaydi.",
             dur=6.6, cam="pull"),

        speeds,

        beat(dur=4.4, n=3,
             note="ATAYLAB JIM. Eng tez yoʻl qancha? Tomoshabin hisoblasin."),

        claim("Jasur", "10 + 1 + 5 + 1 + 2", "19 daqiqa",
              doubt="Eng tez odam hammani kuzatadi",
              dur=8.4),

        fact("10 + 5", "ikkalasi ham toʻliq sarflandi",
             cap="Bobo va Sherbek alohida oʻtyapti — isrof shu yerda.",
             dur=7.0, cam="push"),

        smart,

        check("2 + 1 + 10 + 2 + 2 = 17",
              parts=["Bobo va Sherbek — birga, 10 daqiqa",
                     "Bundan tez yoʻl yoʻq"],
              verdict="17 daqiqa",
              title="Endi sanaymiz",
              dur=8.0),

        rule("Har qadamda eng yaxshisi — eng yaxshi natija emas",
             strip="19  →  17",
             meaning="Kompyuter olimlari bu jumboqni optimallash "
                     "masalalarining namunasi sifatida koʻrsatadi.",
             dur=9.0),

        ask("Bobo 10 emas, 3 daqiqada yursa-chi? Eng tez yoʻl qancha?",
            dur=7.0,
            note="Javobni aytmang: 12 — va ikkala reja ham 12 beradi."),

        practice("Burchak · Matematika olami",
                 sub="powerty.uz → Burchak → Matematika olami",
                 dur=5.2),

        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Tun. Toʻrt kishi tor koʻprik oldida turibdi. || Ularda bitta fonar bor.",

    "Koʻprik faqat ikki kishini koʻtaradi. "
    "|| Fonarni esa kimdir qaytarib olib kelishi kerak.",

    "Jasur bir daqiqada oʻtadi. | Afsona ikki, Sherbek besh, bobo esa oʻn daqiqada. "
    "|| Juftlik sekinrogʻining tezligida yuradi.",

    None,   # beat

    "Birinchi reja: eng tez Jasur hammani bittalab kuzatadi. "
    "|| Jami — oʻn toʻqqiz daqiqa.",

    "Ammo bu rejada isrof bor. | Bobo va Sherbek alohida oʻtyapti. "
    "|| Ikkala sekin vaqt ham toʻliq ketadi.",

    "Sir: ikki eng sekinni birga yuboring. "
    "|| Faqat narigi tomonda fonarni qaytaradigan tez odam tursin.",

    "Sanaymiz: ikki, bir, oʻn, ikki, ikki. "
    "|| Jami — oʻn yetti daqiqa. [excited] Bundan tez yoʻl yoʻq!",

    "Har qadamda eng yaxshisini qilish — har doim eng yaxshi natija emas. "
    "|| Buni optimallash deyishadi.",

    "Endi siz, aqlli boshlar: | bobo uch daqiqada yursa-chi? "
    "|| Eng tez yoʻl qancha? Izohda kutamiz.",

    "Bunday jumboqlar — Powertyda, Burchak boʻlimida.",

    None,   # outro
])
