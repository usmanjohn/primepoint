# -*- coding: utf-8 -*-
"""PM-99 — «Gaussning bolaligi»  (1 dan 100 gacha)   SHAKL: KASHFIYOT

Manba: _stories_prime_math_97_99.py, order 99.

Bu videoning dvigateli — juftlash. Uchta qator yetadi: 1 va 100, 2 va 99,
3 va 98 — hammasi 101. Toʻrtinchi qatorni koʻrsatish shart emas, tomoshabin
oʻzi davom ettiradi. Kashfiyot shu yerda sodir boʻladi, formulada emas.

Videoning oxirgi gapi tezlik haqida emas: Gauss tezroq qoʻshmagan, u savolni
oʻzgartirgan.
"""

from spec import Video, Scene
from scenes import hook, says, beat, claim, check, rule, ask, outro
import primitives as P

_pairs, ps = P.solve([
    ("1 + 100 = 101", "eng chekkadagi ikkitasi"),
    ("2 + 99 = 101", "yana 101"),
    ("3 + 98 = 101", "yana 101"),
    ("50 ta juftlik", "biri oshadi, biri kamayadi"),
], at=0.6, step=1.7)

pairing = Scene(
    11.5,
    P.counters(P.counter(4, "qator", at=0.6, dur=ps, counts=".solve__row"))
    + _pairs
    + P.line("yigʻindi oʻzgarmaydi", "ttl grn", at=0.6 + ps + 0.6,
             anim="pop", dur=0.7),
    cam="sink", top=True, name="pairing", counts=[4],
    claims=["1 + 100 = 101", "2 + 99 = 101", "3 + 98 = 101"],
    note="Qatorni ikki uchidan juftlaymiz. Bir tomondan son oshadi, ikkinchi "
         "tomondan kamayadi — yigʻindi oʻzgarmaydi.")

VIDEO = Video(
    slug="pm99",
    lesson="PM-99",
    title="Gaussning bolaligi",
    story="Prime Math Readings — order 99",
    scenes=[
        hook("1 + 2 + … + 100", "qoʻshing", "1", "soat",
             "Bola bir necha soniyada aytdi.", dur=5.2),

        says("Nodira opa", [("Bir dan yuzgacha", "lbl"),
                            ("hamma sonni qoʻshing", "expr"),
                            ("Vaqtingiz — bir soat", "ask")],
             dur=6.6, size=250,
             note="Rivoyat: oʻqituvchi sinfni bir soatga band qilmoqchi edi."),

        beat(4.2, note="Jim turing. Siz qanday boshlardingiz?"),

        claim("Sardor", "1 + 2 + 3 + 4", "10", "…va yana 96 ta son", dur=8.2,
              note="Sardor birma-bir qoʻshib bordi. Bir soat ham yetmasligi mumkin."),

        pairing,

        check("50 × 101 = 5050",
              parts=["100 ta son → 50 ta juftlik", "har juftlik — 101"],
              verdict="5050.", title="Juftliklarni sanaymiz", dur=8.2,
              note="Ellik juftlik, har biri 101. Javob — 5050."),

        check("10 × 11 ÷ 2 = 55",
              parts=["1 dan 10 gacha qoʻshsak — 55", "formula ham shuni beradi"],
              verdict="Har qanday son uchun ishlaydi.",
              title="Kichik sonda tekshiramiz", dur=8.4,
              note="Usul faqat 100 uchun emas. Kichik sonda tekshirish oson."),

        rule("Gauss tezroq qoʻshmagan — savolni oʻzgartirgan",
             strip="1 + 2 + … + n = n × (n + 1) ÷ 2",
             meaning="Bitta masalani yechish bitta masalani hal qiladi. Namunani koʻrish — cheksiz koʻpini.",
             dur=9.6,
             note="Umumlashtirish — matematikaning yuragi."),

        ask("1 dan 1000 gacha boʻlgan sonlar yigʻindisi qancha boʻladi?",
            dur=6.8, note="Javobni aytmang — formula bilan oʻzlari topsin."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Oʻqituvchi sinfga uzoq davom etadigan vazifa berdi: 1 dan 100 gacha "
    "boʻlgan hamma sonni qoʻshing. || Bu bir soatlik ish edi.",

    "Rivoyat qilishlaricha, kichkina Gauss oʻshanda boshlangʻich sinfda "
    "oʻqir edi. | Oʻqituvchi vazifani aytdi va bolalar qoʻsha boshladi.",

    "Siz qanday qilardingiz? || Birma-bir qoʻshib chiqarmidingiz?",

    "Sardor birinchisidan boshladi: bir, uch, olti, oʻn... | va oldinda yana "
    "toʻqson olti ta son turardi.",

    "Gauss tezroq qoʻshmagan. || U sonlarni *boshqacha joylashtirgan*: "
    "qatorni ikki uchidan juftlagan. 1 va 100 — 101. 2 va 99 — yana 101. "
    "3 va 98 — yana 101. | Biri oshadi, biri kamayadi. Yigʻindi *oʻzgarmaydi*.",

    "Yuzta son ikkitadan juftlansa, 50 ta juftlik chiqadi. Har birining "
    "yigʻindisi 101. | Ellikni 101 ga koʻpaytiramiz — *5050*.",

    "Bu usul faqat 100 uchun emas — istalgan son uchun ishlaydi. "
    "| Tekshiramiz: 1 dan 10 gacha. 10 ni 11 ga koʻpaytirib ikkiga "
    "boʻlsak, *55*.",

    "Esda tutinglar. || Gauss *savolni oʻzgartirgan*. Bitta masalani yechish "
    "bitta masalani hal qiladi. Namunani koʻrish esa cheksiz koʻpini.",

    "Endi oʻzingiz oʻylang. 1 dan 1000 gacha boʻlgan sonlar yigʻindisi "
    "qancha boʻladi? || Izohda kutamiz.",

    None,   # outro — jim
])
