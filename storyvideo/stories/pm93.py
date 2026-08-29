# -*- coding: utf-8 -*-
"""PM-93 — «Ota va oʻgʻil»  (yoshlar masalasi)   SHAKL: TUTILGAN XATO

Manba: _stories_prime_math_93_95.py, order 93.

Bu videoning dvigateli — Jasurning TOʻGʻRI javobi. U «toʻrt martadan ikki
martaga, demak yarmi» deb yigirmani topadi va oʻzi ham bilmaydiki, usuli
notoʻgʻri. Ikkinchi savol (yetti marta) oʻsha usulni sindiradi — mana shu yerda
tomoshabin nima uchun hisob kerakligini tushunadi.

Markazda «vs» sahnasi: kelajak va oʻtmish, nisbat oʻzgargan, farq esa oʻsha 30.
"""

from spec import Video, Scene
from scenes import hook, says, beat, claim, versus, check, rule, ask, outro
import primitives as P

_l1, s1 = P.solve([
    ("40 + x = 2(10 + x)", "x — oʻtadigan yillar"),
    ("40 + x = 20 + 2x", "qavsni ochamiz"),
    ("x = 20", "yigirma yildan keyin"),
], at=0.6, step=1.6)

first = Scene(
    9.6,
    P.counters(P.counter(3, "qadam", at=0.6, dur=s1, counts=".solve__row"))
    + _l1
    + P.line("60 va 30", "ttl grn", at=0.6 + s1 + 0.5, anim="pop", dur=0.6),
    cam="sink", top=True, name="tenglama1", counts=[3],
    claims=["40 + 20 = 60", "10 + 20 = 30"],
    note="x ikkalasiga ham qoʻshiladi — vaqt hamma uchun bir xil oʻtadi.")

_l2, s2 = P.solve([
    ("40 − x = 7(10 − x)", "bu safar ayiriladi"),
    ("40 − x = 70 − 7x", "qavsni ochamiz"),
    ("6x = 30,  x = 5", "besh yil oldin"),
], at=0.6, step=1.6)

second = Scene(
    9.6,
    P.counters(P.counter(3, "qadam", at=0.6, dur=s2, counts=".solve__row"))
    + _l2
    + P.line("35 va 5", "ttl grn", at=0.6 + s2 + 0.5, anim="pop", dur=0.6),
    cam="sink", top=True, name="tenglama2", counts=[3],
    claims=["40 − 5 = 35", "10 − 5 = 5"],
    note="Oʻtmish uchun x ayiriladi. Besh yil oldin ota 35, oʻgʻil 5 yoshda edi.")

VIDEO = Video(
    slug="pm93",
    lesson="PM-93",
    title="Ota va oʻgʻil",
    story="Prime Math Readings — order 93",
    scenes=[
        hook("40", "ota", "10", "oʻgʻil", "Qachon ikki marta katta boʻladi?",
             dur=5.2),

        says("Bobo", [("Hozir ota", "lbl"),
                      ("toʻrt marta katta", "expr gold"),
                      ("Qachon ikki marta boʻladi?", "ask")],
             dur=6.8, size=270,
             note="Bobo nevarasiga oʻzi bolaligida eshitgan jumboqni berdi."),

        beat(4.2, note="Jim turing. Tomoshabin oʻzi taxmin qilsin."),

        claim("Jasur", "toʻrtdan ikkiga", "20 yil", "Yarmi-da?", dur=8.0,
              note="Jasur darrov taxmin qildi — va toʻgʻri javob aytdi. "
                   "Lekin usuli notoʻgʻri edi."),

        first,

        # Ikkinchi savol taxminni sindiradi.
        says("Bobo", [("Endi ikkinchi savol:", "lbl"),
                      ("necha yil OLDIN", "expr"),
                      ("yetti marta katta edi?", "ask")],
             dur=6.8, size=270, mood="think",
             note="Oʻtmish haqidagi savol taxmin bilan yechilmaydi."),

        second,

        versus({"name": "20 yil keyin", "qty": "60 va 30", "price": "nisbat 2",
                "tag": "farq 30", "cls": "win"},
               {"name": "5 yil oldin", "qty": "35 va 5", "price": "nisbat 7",
                "tag": "farq 30", "cls": "win"},
               title="Nima oʻzgardi, nima oʻzgarmadi?",
               unit_label="nisbat har safar boshqa",
               verdict="Farq esa doim 30.", dur=10.5,
               note="Videoning butun gapi shu ikki ustunda."),

        check("40 − 10 = 30",
              parts=["hozir ham 30", "60 − 30 ham 30", "35 − 5 ham 30"],
              verdict="Oʻzgarmas son.", title="Farqni tekshiramiz", dur=8.4,
              note="Yillar oʻtganda ham, orqaga qaytganda ham farq oʻzgarmaydi."),

        rule("Farq oʻzgarmaydi, nisbat oʻzgaradi",
             strip="vaqt ikkalasiga bir xil qoʻshiladi",
             meaning="Yoshlar masalasining kaliti — nimaning oʻzgarmasligini topish.",
             dur=9.4,
             note="Bobo: mana endi jumboqni yechding."),

        ask("Ota oʻgʻlidan roppa-rosa uch marta katta boʻladigan yil qaysi?",
            dur=7.0, note="Javobni aytmang — javob kutilmagan tomonda."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Ota 40 yoshda, oʻgʻli 10 da — toʻrt marta katta. || Qachon roppa-rosa "
    "ikki marta katta boʻladi?",

    "Bu jumboqni bobo nevarasiga berdi — oʻzi bolaligida eshitgan ekan.",

    "Bir soniya oʻylab koʻring. || Siz qanday javob berardingiz?",

    "Jasur darrov taxmin qildi: toʻrt martadan ikki martaga, demak yarmi — "
    "*20 yil*. | Javob toʻgʻri, lekin taxmin bilan.",

    "Endi bilib aytamiz. Oʻtadigan yillar ikkalasiga ham qoʻshiladi — vaqt "
    "hamma uchun bir xil. | Qavsni ochamiz: *20*. Ota 60, oʻgʻil 30 boʻladi.",

    "Bobo ikkinchi savolni berdi. Necha yil *oldin* ota oʻgʻlidan yetti "
    "marta katta edi? || Bu safar yarmi ishlamaydi.",

    "Endi yillar ayiriladi. Qavsni ochamiz: *besh*. | Besh yil oldin ota 35, "
    "oʻgʻil 5 edi — roppa-rosa yetti marta.",

    "Yonma-yon qoʻyamiz. Keyin — 60 va 30, nisbat ikki. | Oldin — 35 va 5, "
    "nisbat yetti. || Nisbat boshqa, farq esa *har doim 30*.",

    "Tekshiramiz. 40 va 10 — farq 30. 60 va 30 — yana 30. 35 va 5 — yana 30.",

    "Esda tutinglar. || *Farq oʻzgarmaydi, nisbat oʻzgaradi.* Yoshlar "
    "masalasining kaliti — nimaning oʻzgarmasligini topish.",

    "Endi oʻzingiz oʻylang. Ota oʻgʻlidan roppa-rosa uch marta katta "
    "boʻladigan yil qaysi? || Izohda kutamiz.",

    None,   # outro — jim
])
