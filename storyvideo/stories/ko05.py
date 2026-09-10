# -*- coding: utf-8 -*-
"""KO-5 — Oʻzbekcha «-da» ikkiga boʻlinadi  ·  TUTILGAN XATO

Manba: Prime Korean PK-14 (에 va 에서 — joy va vaqt qoʻshimchalari).

The second «Tutilgan xato», and the one only an Uzbek channel can make. Every
English-language course teaches 에/에서 as "at versus in/from", which is a
translation problem an English speaker has to memorise. An Uzbek speaker has
the opposite problem, and a sharper one: `uyda turaman` and `uyda oʻqiyman`
take the SAME suffix, so the pupil's own language actively hides the
distinction. The mistake is therefore not carelessness -- it is Uzbek working
correctly.

That is why the mechanism scene is a `versus` and not a rule card: the two
Korean sentences sit side by side under one Uzbek word, and the argument is
made by the column, not by the narration.
"""

from spec import Video, narrate
from scenes import (cover, says, versus, correct, pairs, echo, check,
                    rule, ask, practice, outro)

K = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:74px">%s</span>'

VIDEO = Video(
    slug="ko05",
    lesson="PK-14",
    title="Oʻzbekcha «-da» ikkiga boʻlinadi",
    story="Prime Korean PK-14",
    subject="korean",
    scenes=[
        cover('집<span class="strike">에</span> 공부해요', "«-da» ikkiga boʻlinadi",
              kicker="Tutilgan xato",
              context="«Uyda oʻqiyman» — shundaymi?",
              strike=False,
              note="MUQOVA: qizil chiziq faqat bitta qoʻshimchadan oʻtadi — "
                   "gap toʻgʻri, qoʻshimcha xato. Setkada shu oʻqiladi."),

        says("Afsona", [("Uyda oʻqiyman:", "lbl"),
                        ("집에 공부해요", "expr ko")],
             mood="smile",
             note="Xato oʻzbek tilidan keladi: «uyda» — bitta soʻz, "
                  "shuning uchun bitta qoʻshimcha izlanadi."),

        versus({"name": "joyning oʻzi",
                "qty": KQ % "에",
                "price": K % "집에 있어요",
                "tag": "uyda BORMAN"},
               {"name": "ish bajarilgan joy",
                "qty": KQ % "에서",
                "price": K % "집에서 공부해요",
                "tag": "uyda OʻQIYMAN"},
               title="Ikkalasi ham oʻzbekchada «uyda»",
               dur=12.0,
               note="Butun dalil shu ustunlarda: chapda ham «uyda», oʻngda "
                    "ham «uyda», koreyschada esa ikki xil qoʻshimcha."),

        correct("에", "에서",
                because="Feʼl ish bildirsa — 에서",
                lead="집__ 공부해요",
                note="Faqat qoʻshimcha almashadi, gap oʻzgarmaydi."),

        pairs([("에",   "bor · yoʻq · boradi · keladi"),
               ("에서", "oʻqiydi · ishlaydi · yeydi"),
               ("에서", "va yana «-dan»: uydan chiqdim")],
              head="Feʼlga qarang, qoʻshimcha oʻzi maʼlum boʻladi",
              tail="Joy — 에. Ish — 에서.",
              note="Uchinchi qator ataylab: 에서 ning ikkinchi vazifasi "
                   "oxirgi savolga kerak boʻladi."),

        echo("집에서 공부해요", gloss="uyda oʻqiyman", size=104,
             note="JIM sahna. Koreyscha ovoz ikki marta aytadi."),

        check("학교__ 공부해요",
              parts=["Feʼl: 공부해요 — bu ish",
                     "Ish bajarilgan joy → 에서"],
              verdict=K % "학교에서 공부해요",
              title="Endi yangi gapda sinaymiz",
              dur=8.0,
              note="Qoidani oʻzi qoʻllagan bo'lsin — shuning uchun boshqa gap."),

        rule("Oʻzbekcha -da koreyschada ikkiga boʻlinadi",
             strip="joy → " + K % "에" + "   ·   ish → " + K % "에서",
             meaning="Oʻzbek tili bu farqni koʻrsatmaydi, shuning uchun xato "
                     "eʼtiborsizlikdan emas — ona tilidan keladi. Bir marta "
                     "ajratib olsangiz, boshqa adashmaysiz.",
             dur=9.6),

        ask("«어디에서 왔어요?» — «qaerdan keldingiz?» "
            "Nega bu yerda 에 emas, 에서 turadi?",
            dur=7.6,
            note="Javobni aytmang. Jadvalning uchinchi qatori ishora bergan."),

        practice("Prime Korean · PK-14",
                 sub="Joy va vaqt qoʻshimchalari", dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "«Uyda oʻqiyman» degan gapni koreyschaga oʻgiring. || Koʻpchilik "
    "shunday yozadi — va bitta harfda adashadi.",

    "Afsona ham shunday qildi. | Oʻzbekchada «uyda» — bitta soʻz, "
    "shuning uchun u bitta qoʻshimcha qidirdi.",

    "Ammo qarang. Chapda: *집에 있어요* — uyda borman. | Oʻngda: "
    "*집에서 공부해요* — uyda oʻqiyman. || Oʻzbekchada ikkalasi ham «uyda». "
    "Koreyschada esa ikki xil qoʻshimcha.",

    "Farqi feʼlda. | Agar feʼl ish bildirsa — *에서* qoʻyiladi.",

    "Qoida oddiy. *에* — joyning oʻzi: bor, yoʻq, boradi, keladi. "
    "| *에서* — ish bajarilgan joy: oʻqiydi, ishlaydi, yeydi. "
    "|| Va *에서* ning yana bitta vazifasi bor — «-dan». Uydan chiqdim.",

    None,   # echo — jim sahna, koreyscha ovoz

    "Endi yangi gapda sinaymiz. Maktabda oʻqiyman. | Feʼl — oʻqiyman, "
    "bu ish. || Demak *학교에서 공부해요*.",

    "Shuning uchun oʻzbekcha «-da» koreyschada ikkiga boʻlinadi. "
    "|| Bu xato eʼtiborsizlikdan emas, ona tilidan keladi. Bir marta "
    "ajratib olsangiz, boshqa adashmaysiz.",

    "Endi oʻzingiz oʻylang. *어디에서 왔어요* — qaerdan keldingiz. "
    "|| Nega bu yerda *에서* turadi? Izohda kutamiz.",

    "Joy qoʻshimchalari Powertyda: Prime Korean, 14-dars.",

    None,   # outro — jim
])
