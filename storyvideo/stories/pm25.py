# -*- coding: utf-8 -*-
"""PM-25 — «Narx oshdi, keyin tushdi»   SHAKL: TUTILGAN XATO

Manba: _stories_prime_math_25_27.py, order 25.

Bu videoning dvigateli — ustunlar. Dilnoza «eski narx» deb hisoblaydi; uchinchi
ustun esa punktir chiziqdan PASTDA toʻxtaydi. Buni aytib berish shart emas —
koʻrinib turadi. Qaytim esa xatoning qoʻlga ilinadigan isboti.
"""

from spec import Video, Scene
from scenes import hook, says, beat, claim, consequence, correct, check, \
                   rule, ask, outro
import primitives as P

_bars, sb = P.bars(
    [(20000, "iyun", ""), (25000, "iyul", "up"), (18750, "oktyabr", "down")],
    ref=20000, ref_label="eski narx", at=0.6, step=1.5)

chart = Scene(
    11.5,
    _bars
    + P.line("uchinchi ustun punktirdan pastda", "lbl lbl--sm",
             at=0.6 + sb + 0.4, anim="fade")
    + P.line("18 750 — eski narxdan ham arzon", "ttl grn",
             at=0.6 + sb + 1.0, anim="pop", dur=0.7),
    cam="push", name="chart",
    claims=["20 000 × 1,25 = 25 000", "25 000 × 0,75 = 18 750"],
    note="Iyun 20 000. Iyul 25 000. Oktyabr 18 750. Punktir chiziq — eski narx. "
         "Uchinchi ustun undan pastda toʻxtadi.")

VIDEO = Video(
    slug="pm25",
    lesson="PM-25",
    title="Narx oshdi, keyin tushdi",
    story="Prime Math Readings — order 25",
    scenes=[
        hook("+25%", "yozda oshdi", "−25%", "kuzda tushdi",
             "Eski narxga qaytdimi?", dur=5.0),

        says("Dilnoza", [("25 foiz oshgan edi,", "lbl"),
                         ("25 foiz tushdi", "expr"),
                         ("Demak eski narx — 20 000", "ask")],
             dur=6.8, size=250,
             note="Dilnoza eʼlonni oʻqidi va hisobladi. Hamyoniga roppa-rosa "
                  "20 000 soʻm solib doʻkonga bordi."),

        beat(4.4, note="Jim turing. Siz ham shunday oʻylaysizmi?"),

        claim("Dilnoza", "20 000 × 1,25", "25 000", dur=7.4,
              note="Iyul oxirida narx 25 foizga koʻtarildi: 20 000 dan 25 000 ga."),

        chart,

        # Xato qoʻlga ilinadi: qaytim.
        consequence("Dilnoza", "kassir 1250 soʻm qaytim berdi", dur=7.2, mood="oh",
                    note="Dilnoza qaytimga qarab turib qoldi — u umuman qaytim "
                         "kutmagan edi."),

        correct("20 000", "18 750", "1,25 × 0,75 = 0,9375",
                lead="eski narx emas", dur=8.6,
                note="Koʻpaytuvchilar koʻpaytiriladi. Yangi narx eskining 93,75 foizi."),

        check("25 000 − 18 750 = 6250",
              parts=["oshish 20 000 dan olingan: 5000", "tushish 25 000 dan olingan: 6250"],
              verdict="Shuning uchun narx pastroq tushdi.", title="Nega bunday?",
              dur=8.2,
              note="Bir xil «25 foiz» ikki xil sondan olingan. Kattasidan olingani "
                   "koʻproq — 6250, kichigidan olingani 5000."),

        rule("Bir xil foiz — bir xil pul emas",
             strip="ketma-ket oʻzgarish → koʻpaytuvchilar koʻpaytiriladi",
             meaning="Bir xil foizga oshib, keyin tushgan narx hech qachon eski darajaga qaytmaydi.",
             dur=9.2,
             note="Buni bilgan xaridor eʼlonga emas, yorliqdagi narxga qaraydi."),

        ask("Avval 25 foizga tushib, keyin 25 foizga koʻtarilsa — natija boshqacha boʻladimi?",
            dur=7.0, note="Javobni aytmang. Tartib muhimmi — oʻzlari oʻylab koʻrsin."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Yozda narx 25 foizga oshdi. Kuzda 25 foizga tushdi. "
    "Savol oddiy: || narx *eski darajaga qaytdimi*?",

    "Dilnoza eʼlonni oʻqidi. 25 foiz oshdi, 25 foiz tushdi — "
    "demak *eski narx*. Hamyoniga roppa-rosa 20 000 soʻm solib "
    "doʻkonga bordi.",

    "Bir soniya oʻylab koʻring. || Siz ham shunday hisoblarmidingiz?",

    "Iyun oyida bir litr yogʻ 20 000 soʻm edi. Iyul oxirida narx "
    "25 foizga koʻtarildi va 25 000 soʻm boʻldi.",

    "Uchta oyni yonma-yon qoʻyamiz. Iyunda 20 000. Iyulda 25 000. "
    "Oktyabrda esa 18 750. | Punktir chiziq — eski narx. "
    "Uchinchi ustun undan pastda toʻxtadi.",

    "Dilnoza kassaga 20 000 soʻm berdi. Kassir unga *1250 soʻm qaytim* berdi. "
    "Dilnoza qaytimga qarab qoldi — u qaytim kutmagan edi.",

    "Demak narx *eski darajaga qaytmagan*. Ketma-ket oʻzgarishda "
    "koʻpaytuvchilar koʻpaytiriladi.",

    "Nega bunday boʻldi? Oshish 20 000 dan olingan: 5000 soʻm. "
    "Tushish esa 25 000 dan: 6250 soʻm. "
    "|| *Katta sondan olingan foiz koʻproq.*",

    "Esda tutinglar. || *Bir xil foiz — bir xil pul emas.* Bir xil foizga "
    "oshib, keyin tushgan narx eski darajaga qaytmaydi.",

    "Endi oʻzingiz oʻylang. Agar narx avval 25 foizga tushib, keyin "
    "koʻtarilsa — natija boshqacha boʻladimi? || Javobni izohda yozing.",

    None,   # outro — jim, yozuvning oʻzi yetarli
])
