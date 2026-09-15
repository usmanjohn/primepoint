# -*- coding: utf-8 -*-
"""MO-31 — «A4 qogʻozning sirli oʻlchami»   MATEMATIKA OLAMI

Manba: Matematika olami, order 31.

The most tangible film on the shelf: the viewer is almost certainly within arm's
reach of the object, and the claim can be tested by folding it. That is rare and
worth protecting — so the beat sits right after the question, before any number
is given, and the narration tells them to pick a sheet up.

The whole design is one requirement: fold it in half and the new sheet must have
the SAME proportions. Only one rectangle satisfies that, and its sides stand in
the ratio √2. So 210 and 297 were never chosen — they were computed.

⚠️ 297 ÷ 210 = 1.414285…, and √2 = 1.414213…, so they are NOT equal. The film
never writes that as an equation: the arithmetic gate would (correctly) fail it,
and a pupil told they are equal has been taught something false. `check` shows
the division and the verdict says «√2 ga juda yaqin».
"""

from spec import Video, narrate, Scene
from scenes import cover, fact, beat, check, versus, rule, ask, outro
import primitives as P

_series, ss = P.solve([
    ("A0", "yuzasi ≈ 1 kvadrat metr"),
    ("A0 → A1", "ikkiga buklandi"),
    ("A1 → A2", "yana ikkiga"),
    ("A4 gacha", "toʻrtta buklash"),
], at=0.7, step=1.35)

series = Scene(
    9.8,
    P.line("Butun qator bittadan boshlanadi", "lbl lbl--sm", at=0.0, anim="fade")
    + _series
    + P.line("2 × 2 × 2 × 2 = 16 marta kichik", "ttl grn",
             at=0.7 + ss + 0.5, anim="pop", dur=0.6),
    cam="sink", top=True, name="A qatori",
    claims=["2 × 2 × 2 × 2 = 16"],
    note="A0 dan A4 gacha toʻrtta buklash bor, demak yuza 16 marta "
         "kichrayadi. Bu keyingi sahnadagi 5 grammning sababi.")

VIDEO = Video(
    slug="mo31",
    lesson="Matematika olami",
    title="A4 qogʻozning sirli oʻlchami",
    story="Matematika olami — order 31",
    subject="math",
    scenes=[
        cover("210 × 297", "Nega bunday gʻalati?",
              kicker="Matematika olami",
              context="A4 qogʻozning tomonlari, millimetrda:",
              strike=False,
              note="MUQOVA: har kim koʻrgan qogʻoz, va hech kim "
                   "soʻramagan savol. Sonlar gʻalati koʻrinishi — "
                   "butun filmning yoqilgʻisi."),

        fact("200 × 300", "nega shunday emas?",
             cap="Printerdan bir varaq oling — u qoʻlingizda turibdi.",
             dur=6.8, cam="pull",
             note="Taqqoslash savolni oʻtkir qiladi: yumaloq sonlar "
                  "tanlangan boʻlardi, bular esa hisoblangan."),

        beat(dur=4.4, n=3,
             note="ATAYLAB JIM. Tomoshabin qogʻozni olib buklab koʻrsin — "
                  "bu shelfda tekshirib boʻladigan yagona daʼvo."),

        check("297 ÷ 210",
              parts=["Talab bitta edi: buklangan varaq",
                     "avvalgisining aynan nisbatida boʻlsin"],
              verdict="√2 ga juda yaqin chiqadi",
              title="Uzun tomonni qisqasiga boʻlamiz",
              dur=8.6,
              note="TENGLIK YOʻQ: 297 ÷ 210 = 1,414285…, √2 = 1,414213… "
                   "Ular teng emas, va film ularni teng deb aytmaydi."),

        versus({"name": "A4",
                "qty": '<span style="font-size:70px">210 × 297</span>',
                "price": "millimetr",
                "tag": "nisbat √2"},
               {"name": "A5 — ikkiga buklangan",
                "qty": '<span style="font-size:70px">148 × 210</span>',
                "price": "millimetr",
                "tag": "nisbat √2", "cls": "win"},
               title="Buklang — nisbat oʻzgarmaydi",
               dur=11.0,
               note="Butun tizimning yuragi: shakl oʻziga oʻxshab qoladi. "
                    "Buni qanoatlantiradigan boshqa toʻrtburchak yoʻq."),

        series,

        fact("71", "foiz — nusxa koʻchirgichdagi tugma",
             cap="A4 ni A5 ga kichraytiradi. Bu — √2 ning teskarisi.",
             dur=7.0, dark=True,
             note="Kundalik hayotdagi iz: tugma tasodifiy son emas."),

        rule("210 va 297 tanlanmagan — hisoblab chiqarilgan",
             strip="buklansa ham nisbat oʻsha  →  tomonlar nisbati √2",
             meaning="Bitta talab — buklangan varaq avvalgisiga oʻxshash "
                     "boʻlsin — butun bir standartni keltirib chiqardi. "
                     "Shuning uchun qogʻozdagi gʻalati sonlar aslida "
                     "javobning oʻzi.",
             dur=9.8),

        ask("A3 — A4 dan bir marta katta buklash. "
            "Unda uning yuzasi necha marta katta?",
            dur=7.2,
            note="Javobni aytmang. A qatoridagi sahna ishora bergan."),

        outro(),
    ],
)

narrate(VIDEO, [
    "A4 qogʻozning tomonlari 210 va 297 millimetr. || Gʻalati sonlar, "
    "shunday emasmi?",

    "Nega 200 va 300 emas? || Chunki bu sonlar tanlanmagan — ular "
    "hisoblab chiqarilgan.",

    None,   # beat — jim sahna, varaqni olib buklab koʻrsin

    "Talab bitta edi: buklangan varaq avvalgisining aynan nisbatida "
    "boʻlsin. || Javob — ikkining kvadrat ildizi.",

    "Ikkiga buklaymiz. || Nisbat oʻsha qoldi — shakl oʻziga oʻxshaydi, "
    "faqat kichrayadi.",

    "Butun qator A0 dan boshlanadi — yuzasi bir kvadrat metr. || A4 "
    "gacha toʻrtta buklash bor.",

    "Nusxa koʻchirgichda A4 ni A5 ga kichraytirish uchun apparat 71 "
    "foizni tanlaydi.",

    "Shuning uchun bu sonlar tanlanmagan — hisoblab chiqarilgan. "
    "|| Bitta talab butun bir standartni keltirib chiqardi.",

    "Endi oʻzingiz oʻylang. | A3 — A4 dan bir marta katta buklash, "
    "yuzasi necha marta katta? || Izohda kutamiz.",

    None,   # outro — jim
])
