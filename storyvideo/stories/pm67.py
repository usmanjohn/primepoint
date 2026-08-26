# -*- coding: utf-8 -*-
"""PM-67 — «Bogʻga panjara»  (perimetr)

Manba: corner/management/commands/_stories_prime_math_66_68.py, order 67.

Hikoyaning butun gapi: Sherbek ikkita tomonni qoʻshdi va toʻxtadi. Shuning uchun
videoning markazi — chegara boʻylab aylanish: metrlar 28 dan oʻtib ketadi va
xato koʻzga koʻrinadi.
"""

from spec import Video
from scenes import hook, says, beat, claim, walk, consequence, correct, \
                   check, rule, outro
import primitives as P

VIDEO = Video(
    slug="pm67",
    lesson="PM-67",
    title="Bogʻga panjara",
    story="Prime Math Readings — order 67",
    scenes=[
        hook("18", "metr uzunlik", "10", "metr en",
             "Necha metr panjara kerak?", dur=4.8),

        says("Sherbek", [("Oʻlchadim:", "lbl"),
                         ("18 + 10 = 28", "expr"),
                         ("Yigirma sakkiz metr bering", "ask")],
             dur=6.6, size=250, mood="smile",
             note="Sherbek bogʻni oʻlchadi, ikkita tomonni qoʻshdi va doʻkonga bordi."),

        beat(4.0, note="Jim turing. Sherbek nimani unutdi?"),

        says("Nodira opa", [("Bogʻing toʻrtburchakmi?", "lbl"),
                            ("Menga perimetri kerak", "expr gold"),
                            ("Sen faqat ikkita tomonni qoʻshibsan", "ask")],
             dur=7.0, size=250, mood="think",
             note="Doʻkonchi Nodira opa xatoni darrov koʻrdi: perimetr — bu chegara."),

        # Chegara boʻylab aylanamiz. Hisoblagich yonayotgan tomonlarni QOʻSHADI,
        # shuning uchun 28 dan oʻtib ketishi ekranda koʻrinadi.
        walk(18, 10, dur=11.0, step=0.95, total_label="metr",
             tail="Chegara boʻylab bir marta",
             note="Har bir tomonni yoqamiz. 18 → 28 → 46 → 56. Mana, 28 da toʻxtash xato edi."),

        correct("28", "56", "2 × (18 + 10) = 2 × 28 = 56 m", lead="P = 2 × (a + b)",
                dur=8.6,
                note="Qarama-qarshi tomonlar teng, demak har bir son ikki marta."),

        consequence("Sherbek", "bogʻning yarmi ochiq qolardi", dur=6.6, mood="sad",
                    note="Yigirma sakkiz metr olganida bogʻning yarmi ochiq qolar edi."),

        check("56 − 4 = 52", parts=["darvoza 4 m — panjara kerak emas"],
              verdict="52 metr panjara.", title="Darvoza-chi?", dur=7.2,
              note="Darvoza 4 metr. U yerga panjara kerak emas: 56 − 4 = 52."),

        check("52 × 25 000 = 1 300 000", parts=["bir metri 25 000 soʻm"],
              verdict="1 300 000 soʻm.", title="Narxi", dur=7.2,
              note="Uzunlikni narxga koʻpaytiramiz. Bir metr ham ortiqcha emas."),

        rule("Perimetr — bu chegara, ikkita tomon emas",
             strip="P = 2 × (a + b)",
             meaning="Qarama-qarshi tomonlar teng, shuning uchun har bir son ikki marta qoʻshiladi.",
             dur=9.0,
             note="Sherbek daftariga yozib qoʻydi: perimetr — bu chegara."),

        outro(),
    ],
)
