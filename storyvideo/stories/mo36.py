# -*- coding: utf-8 -*-
"""MO-36 — «Monti Xoll: eshikni almashtirasizmi?»   MATEMATIKA OLAMI · jumboq

Manba: Matematika olami, order 36.  Subject: logic.

The most argued-about probability puzzle there is. The film's turn is the
reading's own: make it 100 doors, and the intuition flips by itself. Facts as
in the reading: Marilyn vos Savant, «Parade», 1990, ~10 000 letters, Erdős
unconvinced until a simulation (hedged: «aytishlaricha»).

Gate: the scratchpad simulates and enumerates all (car, pick) cases --
switching wins exactly 6 of 9 = 2/3.
"""

from spec import Video, narrate, Scene
from scenes import cover, says, beat, claim, fact, versus, check, rule, ask, practice, outro

VIDEO = Video(
    slug="mo36",
    lesson="Matematika olami",
    title="Monti Xoll: eshikni almashtirasizmi?",
    story="Matematika olami — order 36",
    subject="logic",
    scenes=[
        cover("Yarmi-yarmi", "Almashtiring!",
              kicker="Mantiq jumbogʻi",
              context="Uchta eshik, bitta mashina. Ikkitasi qoldi:",
              note="MUQOVA: hamma aytadigan «yarmi-yarmi» chizilgan."),

        says("Anvar aka", [("3-eshikda — echki!", "lbl"),
                           ("Almashtirasizmi?", "ttl")],
             mood="smile", size=230,
             note="Boshlovchi mashina qayerdaligini BILADI."),

        beat(dur=4.2, n=3,
             note="ATAYLAB JIM. Tomoshabin oʻzi qaror qilsin."),

        claim("Sherbek", "2 ta eshik qoldi", "50 %",
              doubt="Farqi yoʻq-ku?", dur=7.6),

        fact("10 000", "ta gʻazabli xat",
             cap="1990-yil, «Parade» jurnali. Merilin vos Savant: «Almashtiring!»",
             dur=7.0, cam="pull"),

        fact("100", "ta eshik",
             cap="Siz bittasini tanlaysiz. Boshlovchi 98 tasini ochadi — hammasida echki.",
             dur=7.4, cam="push"),

        versus({"name": "sizning eshik", "qty": "1/3",
                "price": "ehtimol", "tag": "qolish", "cls": "lose"},
               {"name": "qolgan eshik", "qty": "2/3",
                "price": "ehtimol", "tag": "almashish", "cls": "win"},
               title="Uch eshikda ham xuddi shunday",
               dur=9.0),

        check("1/3 + 2/3 = 1",
              parts=["Boshlovchi tasodifan ochmaydi",
                     "Uning tanlovi — sizga maʼlumot"],
              verdict="Almashtiring: 2/3",
              title="Sir qayerda",
              dur=8.2),

        rule("Boshlovchining tanlovi — sizga berilgan maʼlumot",
             strip="qolsangiz 1/3  ·  almashtirsangiz 2/3",
             meaning="Aytishlaricha, buyuk matematik Pol Erdyosh ham "
                     "kompyuter simulyatsiyasini koʻrmaguncha ishonmagan.",
             dur=9.0),

        ask("Uchta stakan va bitta tanga bilan 20 marta oʻynang. "
            "Almashtirib nechta yutdingiz?",
            dur=7.0),

        practice("Burchak · Matematika olami",
                 sub="powerty.uz → Burchak → Matematika olami",
                 dur=5.2),

        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Uchta eshik. Bittasining ortida mashina, ikkitasida — echki. "
    "|| Siz bittasini tanlaysiz.",

    "Boshlovchi mashina qayerdaligini biladi. | U boshqa eshikni ochadi — echki. "
    "|| Endi almashtirasizmi?",

    None,   # beat

    "Koʻpchilik shunday deydi: ikkita eshik qoldi, demak yarmi-yarmi. "
    "|| Farqi yoʻq.",

    "Merilin vos Savant jurnalda «almashtiring» deb yozdi. "
    "|| Unga oʻn mingga yaqin gʻazabli xat keldi. [laughs]",

    "Oʻyinni kattalashtiramiz: yuzta eshik. "
    "|| Boshlovchi qolganlarining hammasini ochadi, bittasidan boshqa.",

    "Birinchi tanlovingiz — uchdan bir. "
    "|| Qolgan eshiklarda esa — uchdan ikki.",

    "Boshlovchi tasodifan ochmaydi. | U echkini bilib ochadi. "
    "|| Uchdan ikki butunicha yopiq eshikka oʻtadi.",

    "Aytishlaricha, buyuk matematik Pol Erdyosh ham simulyatsiyani "
    "koʻrmaguncha ishonmagan.",

    "Ishonmayapsizmi, aqlli boshlar? | Stakan va tanga bilan yigirma marta "
    "oʻynab koʻring. || Natijani izohda yozing.",

    "Bunday jumboqlar — Powertyda, Burchak boʻlimida.",

    None,   # outro
])
