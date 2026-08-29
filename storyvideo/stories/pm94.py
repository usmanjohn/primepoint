# -*- coding: utf-8 -*-
"""PM-94 — «Retseptdagi xato»  (birlik miqdor)   SHAKL: TUTILGAN XATO

Manba: _stories_prime_math_93_95.py, order 94.

Bu videoning dvigateli — bir kishiga toʻgʻri keladigan son. «5 kg» yozuvi oʻzi
turganda hech narsa demaydi; bir kishiga boʻlingandan keyin esa darrov kulgili
boʻlib qoladi. Shuning uchun markazda ikki ustun turadi: 1250 gramm va 125.

Xato arifmetikada emas — koʻchirishda. Vergul tushib qolgan.
"""

from spec import Video, Scene
from scenes import hook, says, beat, versus, correct, check, rule, ask, outro
import primitives as P

_ladder, ls = P.solve([
    ("1,5 kg = 1500 g", "bitta birlikka keltiramiz"),
    ("1500 ÷ 12 = 125", "bir kishiga shuncha gramm"),
    ("4 × 125 = 500", "toʻrt kishiga"),
    ("500 g = 0,5 kg", "yarim kilogramm"),
], at=0.6, step=1.6)

ladder = Scene(
    11.0,
    P.counters(P.counter(4, "qadam", at=0.6, dur=ls, counts=".solve__row"))
    + _ladder,
    cam="sink", top=True, name="ladder", counts=[4],
    claims=["1500 ÷ 12 = 125", "4 × 125 = 500"],
    note="Bir yarim kilogramm — 1500 gramm. 12 kishiga boʻlsak bir kishiga "
         "125 gramm. Toʻrt kishiga 500 gramm.")

VIDEO = Video(
    slug="pm94",
    lesson="PM-94",
    title="Retseptdagi xato",
    story="Prime Math Readings — order 94",
    scenes=[
        hook("5", "kg — roʻyxatda", "0,5", "kg — retseptda",
             "Qaysi biri toʻgʻri?", dur=5.0),

        says("Nodira opa", [("Retsept 12 kishiga:", "lbl"),
                            ("1,5 kg guruch", "expr gold"),
                            ("Sen toʻrt kishiga qil", "ask")],
             dur=6.8, size=250,
             note="Nodira opa Sherbekka oilaviy retseptni berdi."),

        says("Sherbek", [("Roʻyxatda:", "lbl"),
                         ("guruch — 5 kg", "expr red"),
                         ("Balki toʻgʻridir?", "ask")],
             dur=6.8, size=250, mood="think",
             note="Doʻkondan qaytgach roʻyxatga qaradi va toʻxtab qoldi."),

        beat(4.2, note="Jim turing. Qanday tekshirish mumkin?"),

        ladder,

        versus({"name": "roʻyxat boʻyicha", "qty": "5 kg", "price": "4 kishiga",
                "tag": "1250<br><span class='cmp__k'>g / kishi</span>",
                "cls": "lose", "claim": "5000 ÷ 4 = 1250"},
               {"name": "retsept boʻyicha", "qty": "0,5 kg", "price": "4 kishiga",
                "tag": "125<br><span class='cmp__k'>g / kishi</span>",
                "cls": "win", "claim": "500 ÷ 4 = 125"},
               title="Bir kishiga qancha?", unit_label="bitta birlikka keltiramiz",
               verdict="Oʻn barobar farq.", dur=10.5,
               note="Roʻyxat boʻyicha bir kishiga 1250 gramm — bir yarim kiloga "
                    "yaqin guruch. Retsept boʻyicha 125."),

        correct("5 kg", "0,5 kg", "5000 ÷ 4 = 1250", lead="vergul tushib qolgan",
                dur=8.6,
                note="Ukasi koʻchirayotib vergulni tushirib qoldirgan — yarim "
                     "kilo besh kiloga aylangan."),

        check("4 × 125 = 500", parts=["bir kishiga 125 g", "toʻrt kishiga 500 g"],
              verdict="Yarim kilogramm.", dur=7.8,
              note="Mantiqiy son: bir kishiga bir yarim kosacha guruch."),

        rule("Bir kishiga qancha toʻgʻri keladi?",
             strip="birlik miqdor = jami ÷ kishilar soni",
             meaning="Bu son birlik xatosini darrov fosh qiladi — uni oʻz tajribangiz bilan solishtira olasiz.",
             dur=9.4,
             note="Eng oson tekshirish yoʻli — bittaga keltirish."),

        ask("Retseptdagi «40 daqiqa» yozuvi guruch hisobida nega kerak boʻlmadi?",
            dur=7.0, note="Javobni aytmang. Ortiqcha maʼlumot haqida oʻylashsin."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Roʻyxatda guruch 5 kilogramm deb yozilgan. Retsept boʻyicha esa yarim "
    "kilo chiqishi kerak edi. || Qaysi biri toʻgʻri?",

    "Nodira opa Sherbekka oilaviy retseptni berdi. Retsept 12 kishiga: "
    "bir yarim kilogramm guruch. | Sherbek esa toʻrt kishiga tayyorlashi kerak.",

    "Doʻkondan qaytgach roʻyxatga qaradi va toʻxtab qoldi. Birinchi qatorda: "
    "guruch — 5 kilogramm. | Bir zum ikkilandi. Balki toʻgʻridir?",

    "Siz nima qilardingiz? || Buni qanday tekshirish mumkin?",

    "Bir kishiga qancha toʻgʻri kelishini sanaymiz. Bir yarim kilogramm — "
    "1500 gramm. | 12 kishiga boʻlsak, bir kishiga 125 gramm. "
    "|| Toʻrt kishiga 500 gramm, yaʼni yarim kilo.",

    "Endi ikkalasini bir kishiga keltiramiz. Roʻyxat boʻyicha bir kishiga "
    "1250 gramm toʻgʻri kelardi. | Retsept boʻyicha esa 125. "
    "|| *Oʻn barobar farq.*",

    "Xato topildi. Ukasi koʻchirayotib *vergulni tushirib qoldirgan* — "
    "yarim kilo besh kiloga aylanib qolgan.",

    "Tekshiramiz. Bir kishiga 125 gramm, toʻrt kishiga 500 gramm. "
    "| Yarim kilogramm — mantiqiy son.",

    "Esda tutinglar. || *Bir kishiga qancha toʻgʻri kelishini hisoblang.* "
    "Bu son birlik xatosini darrov fosh qiladi — uni oʻz tajribangiz bilan "
    "solishtira olasiz.",

    "Endi oʻzingiz oʻylang. Retseptdagi 40 daqiqa yozuvi guruch hisobida "
    "nega kerak boʻlmadi? || Izohda kutamiz.",

    None,   # outro — jim
])
