# -*- coding: utf-8 -*-
"""PM-55 — «Tovuq va quyon»  (ikki nomaʼlum)   SHAKL: KASHFIYOT

Manba: _stories_prime_math_55_57.py, order 55.

Bu videoning dvigateli — «hammasi tovuq boʻlsa» degan faraz. Sistema yozmasdan
ham javob chiqadi: farqni sanaysan va almashtirasan. Shuning uchun markazda
zinapoya turadi — har bir qadamning sababi yonida.

Sardorning teng boʻlishi ataylab tanlangan: u eng tabiiy notoʻgʻri harakat, va
oyoqlarni sanaganda darrov qoʻlga tushadi.
"""

from spec import Video, Scene
from scenes import hook, says, beat, claim, check, correct, rule, ask, outro
import primitives as P

_ladder, ls = P.solve([
    ("35 × 2 = 70", "hammasi tovuq boʻlsa"),
    ("94 − 70 = 24", "shuncha oyoq yetishmaydi"),
    ("24 ÷ 2 = 12", "har bir quyon 2 ta koʻp beradi"),
    ("35 − 12 = 23", "qolgani — tovuq"),
], at=0.6, step=1.6)

ladder = Scene(
    11.0,
    P.counters(P.counter(4, "qadam", at=0.6, dur=ls, counts=".solve__row"))
    + _ladder,
    cam="sink", top=True, name="ladder", counts=[4],
    claims=["35 × 2 = 70", "94 − 70 = 24", "24 ÷ 2 = 12", "35 − 12 = 23"],
    note="Hammasi tovuq deb faraz qilamiz — 70 oyoq. 24 tasi yetishmaydi. "
         "Har bir quyon ikkitadan koʻp beradi, demak 12 ta quyon.")

VIDEO = Video(
    slug="pm55",
    lesson="PM-55",
    title="Tovuq va quyon",
    story="Prime Math Readings — order 55",
    scenes=[
        hook("35", "bosh", "94", "oyoq", "Nechta tovuq, nechta quyon?", dur=5.0),

        says("Nodira opa", [("Ming besh yuz yil avval", "lbl"),
                            ("Xitoy kitobida", "expr"),
                            ("shu masala yozilgan", "ask")],
             dur=6.6, size=250,
             note="Masala «Sun-szi suan-szin» kitobidan. Yaponiyada uni turna va "
                  "toshbaqa masalasi deyishadi."),

        beat(4.2, note="Jim turing. Tomoshabin oʻzi boshlasin."),

        claim("Sardor", "35 ÷ 2", "17 va 18", "Teng boʻlsa-chi?", dur=8.2,
              note="Sardor teng boʻlishga urindi — eng tabiiy notoʻgʻri harakat."),

        check("17 × 2 + 18 × 4 = 106", parts=["kerak edi — 94 ta oyoq"],
              verdict="12 tasi ortiqcha.", title="Sardorni tekshiramiz", dur=7.8,
              note="Oyoqlarni sanaymiz: 34 va 72 — jami 106. Koʻp chiqdi."),

        ladder,

        # Qisqa sonlar ataylab: correct() ikkala sonni bitta qatorga sigʻdiradi,
        # shuning uchun «17 va 18» kabi uzun matn kichrayib, leaddan pastroq
        # koʻrinib qoladi. Bu yerda faqat quyonlar soni almashadi.
        correct("18", "12", "24 ÷ 2 = 12", lead="quyonlar soni", dur=8.4,
                note="Sardor 18 ta quyon degan edi — aslida 12 ta."),

        check("23 × 2 + 12 × 4 = 94",
              parts=["23 tovuq × 2 oyoq = 46", "12 quyon × 4 oyoq = 48"],
              verdict="Boshlar ham 35 ta.", dur=8.0,
              note="46 va 48 — jami 94. Boshlar: 23 va 12 — 35."),

        rule("Hammasi bir xil deb faraz qil",
             strip="farqni sana  →  almashtir",
             meaning="Ikki nomaʼlumli masala bitta farazdan keyin bitta boʻlishga aylanadi.",
             dur=9.0,
             note="Sistema yozish ham mumkin, lekin faraz usuli qogʻozsiz ishlaydi."),

        ask("Agar 35 ta bosh va 100 ta oyoq boʻlsa, nechta quyon boʻlardi?",
            dur=6.8, note="Javobni aytmang — oʻzlari sanab koʻrsin."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Qafasda tovuqlar va quyonlar bor. Yuqoridan 35 ta bosh koʻrinadi, "
    "pastdan 94 ta oyoq. || Nechta tovuq, nechta quyon?",

    "Bu masala ming besh yuz yil avval Xitoyda yozilgan. | Yaponiyada uni "
    "turna va toshbaqa masalasi deyishadi — matematikasi bir xil.",

    "Bir soniya oʻylab koʻring. || Siz qanday boshlagan boʻlardingiz?",

    "Sardor teng boʻlishga urindi: 17 ta tovuq va 18 ta quyon.",

    "Oyoqlarni sanaymiz. 17 ta tovuqda 34 ta oyoq, 18 ta quyonda 72 ta. "
    "| Jami 106. || Kerak edi *94*. Oʻn ikkitasi ortiqcha.",

    "Faraz qilaylik — *hammasi tovuq*. Unda 70 ta oyoq boʻlardi. | Lekin 94 "
    "kerak: 24 tasi yetishmaydi. || Har bir quyon ikkita koʻp oyoq beradi. "
    "Demak 12 ta quyon, 23 tasi tovuq.",

    "Quyonlar 18 ta emas — *12 ta*. | Qolgan 23 tasi esa tovuq.",

    "Tekshiramiz. 23 ta tovuqning 46 ta oyogʻi, 12 ta quyonning 48 ta oyogʻi. "
    "| Jami 94. Boshlar ham 35 ta.",

    "Esda tutinglar. || *Hammasi bir xil deb faraz qiling*, keyin farqni "
    "sanab almashtiring. Ikki nomaʼlum shu bilan bittaga aylanadi.",

    "Endi oʻzingiz oʻylang. Agar 35 ta bosh va 100 ta oyoq boʻlsa, nechta "
    "quyon boʻlardi? || Izohda kutamiz.",

    None,   # outro — jim
])
