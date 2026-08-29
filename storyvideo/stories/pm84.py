# -*- coding: utf-8 -*-
"""PM-84 — «Lotereya nega yutqazadi»   SHAKL: TESKARI NATIJA

Manba: _stories_prime_math_82_84.py, order 84.

Bu videoning dvigateli — oxirgi son. Ehtimollik (2,8 foiz) tomoshabinni
hayratlantirmaydi: hamma lotereyada yutish qiyinligini biladi. Hayratlanarlisi —
oʻrtacha qaytim: 5 000 soʻmlik biletga 2 000 soʻm. Yutqazish omadga emas,
SHARTGA kiritilgan.

Shuning uchun oxirida Sherbek baribir bitta bilet oladi va yutadi — hikoya
lotereyani qoralamaydi, faqat sonini koʻrsatadi.
"""

from spec import Video, Scene
from scenes import hook, says, beat, claim, check, versus, rule, ask, outro
import primitives as P

# ⚠️ .solve__l is `white-space: nowrap` at 62px inside a 900px box, so a long
# expression on the LEFT pushes the reason column clean off the frame. Keep the
# left side to a result (~14 chars) and put the sum in the right column, which
# is 36px and allowed to wrap.
_ladder, ls = P.solve([
    ("1 000 000", "5 ta quloqchin × 200 000"),
    ("1 500 000", "50 ta kitob × 30 000"),
    ("4 000 000", "velosiped bilan — yutuq fondi"),
    ("10 000 000", "2 000 bilet × 5 000 soʻm"),
], at=0.6, step=1.6)

ladder = Scene(
    11.2,
    P.counters(P.counter(4, "qator", at=0.6, dur=ls, counts=".solve__row"))
    + _ladder,
    cam="sink", top=True, name="ladder", counts=[4],
    claims=["5 × 200 000 = 1 000 000", "50 × 30 000 = 1 500 000",
            "2 000 × 5 000 = 10 000 000"],
    note="Sherbek daftariga koʻchirdi: yutuq fondi 4 million, tushum 10 million.")

VIDEO = Video(
    slug="pm84",
    lesson="PM-84",
    title="Lotereya nega yutqazadi",
    story="Prime Math Readings — order 84",
    scenes=[
        hook("2 000", "bilet", "5 000", "soʻm", "Yutish ehtimoli qancha?", dur=5.2),

        says("Sherbek", [("Bitta velosiped, beshta quloqchin,", "lbl"),
                         ("ellikta kitob", "expr gold"),
                         ("Hammasi devorga yozilgan", "ask")],
             dur=6.8, size=250,
             note="Maktab hovlisida lotereya. Hamma son ochiq yozilgan edi."),

        beat(4.2, note="Jim turing. Sizningcha, yutish ehtimoli qancha?"),

        ladder,

        claim("Sherbek", "56 ÷ 2 000", "0,028", "yaʼni 2,8 foiz", dur=8.2,
              note="Yutuqli biletlar: bir, besh va ellik — jami 56 ta."),

        check("1 − 0,028 = 0,972",
              parts=["teskari hodisa qoidasi", "yaʼni 97,2 foiz"],
              verdict="Deyarli hamma yutqazadi.", title="Yutmaslik ehtimolligi",
              dur=8.2,
              note="Yutmaslikni sanab oʻtirish shart emas — bittadan ayiramiz."),

        # Videoning eng muhim soni shu yerda.
        check("4 000 000 ÷ 2 000 = 2 000",
              parts=["yutuq fondini biletlarga boʻlamiz"],
              verdict="Bitta biletga 2 000 soʻm qaytadi.",
              title="Endi eng qizigʻi", dur=8.2,
              note="Bu — bitta biletga toʻgʻri keladigan oʻrtacha qaytim."),

        versus({"name": "bilet narxi", "qty": "5 000", "price": "soʻm",
                "tag": "toʻlaysiz", "cls": "lose"},
               {"name": "oʻrtacha qaytim", "qty": "2 000", "price": "soʻm",
                "tag": "qaytadi", "cls": "win"},
               title="Har bir bilet uchun", unit_label="farqi — 3 000 soʻm",
               # Uzun ifoda uch qatorga boʻlinib, sonning oʻrtasidan uzilib
               # qolardi — verdict qisqa jumla boʻlishi kerak.
               verdict="Tashkilotchida 6 000 000 soʻm.", dur=10.5,
               note="Har 5 000 soʻmdan 3 000 soʻm tashkilotchida qoladi."),

        rule("Yutqazish oʻyinning shartiga kiritilgan",
             strip="oʻrtacha qaytim = yutuq fondi ÷ biletlar soni",
             meaning="Yutqazish uchun omadsiz boʻlish shart emas.",
             dur=9.4,
             note="Sherbek baribir bitta bilet oldi va kitob yutdi — tasodif "
                  "2,8 foizni ham baʼzan tanlaydi."),

        ask("Tashkilotchi 6 000 000 soʻm oldi. Bu pul aynan qayerdan chiqdi?",
            dur=7.0, note="Javobni aytmang."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Maktab hovlisida lotereya. Jami 2 000 ta bilet, har biri 5 000 soʻm. "
    "|| Yutish ehtimoli qancha?",

    "Yutuqlar devorga ochiq yozilgan: bitta velosiped, beshta quloqchin, "
    "ellikta kitob.",

    "Bir soniya oʻylab koʻring. || Sizningcha, yutish ehtimoli qancha?",

    "Avval yutuq fondini topamiz. Quloqchinlar — bir million, kitoblar — bir "
    "yarim million. | Velosiped bilan birga *4 million*. || Tushum esa 10 million.",

    "Yutuqli biletlar — jami 56 ta. 56 ni 2 000 ga boʻlamiz: *2,8 foiz*.",

    "Yutmaslikni sanab oʻtirish shart emas: bittadan ayiramiz — *97,2 foiz*.",

    "Endi eng qizigʻi. Yutuq fondini biletlar soniga boʻlamiz: 4 million "
    "boʻlinadi 2 000 ga. | Bitta biletga *2 000 soʻm* qaytadi.",

    "Bilet 5 000 soʻm turadi, qaytim esa 2 000. || Har bir biletdan "
    "*3 000 soʻm* tashkilotchida qoladi. Hammasi boʻlib 6 million soʻm.",

    "Esda tutinglar. || *Yutqazish uchun omadsiz boʻlish shart emas* — u oʻyin "
    "shartiga kiritilgan. | Sherbek baribir bilet oldi va kitob yutdi: tasodif "
    "2,8 foizni ham tanlaydi.",

    "Endi oʻzingiz oʻylang. Tashkilotchi olgan 6 million soʻm aynan qayerdan "
    "chiqdi? || Izohda kutamiz.",

    None,   # outro — jim
])
