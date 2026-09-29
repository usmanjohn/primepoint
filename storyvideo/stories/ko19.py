# -*- coding: utf-8 -*-
"""KO-19 — «Chiroq tagi»  ·  BIR MAQOL, IKKI TIL

속담: 등잔 밑이 어둡다 — «chiroq tagi qorongʻi».
Oʻzbekchasi: «Chiroq tagi qorongʻi.»

The third proverb film, and the one that breaks its own series' rule on
purpose. ko16 ended on «faqat hayvon almashgan» and ko17 on «tasvir boshqa,
fikr bitta» -- both of them are films about the DIFFERENCE between the twins.
This pair has no difference at all: the lamp is a lamp, the under is the
under, the dark is the dark. So the `order` beat's verdict is the opposite
one, and it is stronger for having two films behind it.

⚠️ A proverb film has to teach the LANGUAGE, not only the wisdom (SERIES.md
§3). Here it is 밑: a place word in Korean is a NOUN standing AFTER the thing,
and it takes the particle -- 등잔 밑**이**. What is dark is not the lamp, it is
the under. Uzbek does exactly the same with «tag+i», which is why this proverb
comes out word for word and the English one («the darkest place is under the
candlestick») does not.

The pronunciation is the reason korean.py grew 구개음화 proper on 2026-09-22:
밑이 is [미치], and the romaniser said «miti» until the case was written.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, order, pairs, echo,
                    rule, ask, practice, outro)

K = '<span class="ko">%s</span>'

VIDEO = Video(
    slug="ko19",
    lesson="속담",
    title="Chiroq tagi",
    story="Koreys maqollari",
    subject="korean",
    scenes=[
        cover("등잔 밑", "Chiroq tagi qorongʻi",
              kicker="Bir maqol, ikki til",
              ko="한국어",
              context="Koreys maqolining boshi:",
              strike=False,
              note="MUQOVA: gʻalati narsa — ikkita begona til, bitta maqol. "
                   "Vaʼda aynan oʻzbekcha maqolning oʻzi."),

        says("Afsona", [("Butun uyni agʻdardi:", "lbl"),
                        ("Koʻzoynagim qani?", "expr")],
             mood="think",
             note="Vaziyat. Hamma joyga qaradi — bitta joydan boshqa."),

        consequence("Afsona", "Peshonasida turgan ekan.",
                    mood="laugh", close=True, cam="pull",
                    note="Maqolning oʻzi roʻy berdi. YANGI: yaqin plan "
                         "(`close=True`) va yangi kayfiyat (`laugh`) — "
                         "reaksiya kadri butun ekranni egallaydi."),

        echo("등잔 밑", gloss="chiroq tagi",
             head="Maqoldagi joy",
             note="JIM sahna. Talaffuziga eʼtibor bering: 밑이 — «michi»."),

        order([("Koreyscha", [("등잔", "s"), ("밑이", "o"),
                              ("어둡다", "v")], True),
               ("Soʻzma-soʻz", [("chiroq", "s"), ("tagi", "o"),
                                ("qorongʻi", "v")], False),
               ("Oʻzbekcha", [("chiroq", "s"), ("tagi", "o"),
                              ("qorongʻi", "v")], False)],
              head="Bitta maqol, ikkita til",
              verdict="Bu safar hech narsa almashmagan",
              dur=13.0,
              note="Seriyaning eng kuchli kadri: pastki ikki qator "
                   "bir-biriga AYNAN teng. ko16 da faqat hayvon almashgan "
                   "edi — bu yerda hatto u ham yoʻq."),

        pairs([("등잔 밑", "chiroq tagi"),
               ("책상 밑", "stol tagi"),
               ("다리 밑", "koʻprik tagi"),
               ("밑이 어둡다", "tagi qorongʻi")],
              head="«밑» — oldin emas, keyin turadi",
              tail="Joy soʻzi — ot, va qoʻshimcha oladi",
              note="Filmning til haqidagi dalili. Koreysda ham, oʻzbekchada "
                   "ham joy soʻzi narsadan KEYIN turadi va oʻzi ot boʻladi: "
                   "밑+이 = tag+i. Inglizchada «under» oldin keladi."),

        echo("어둡다", gloss="qorongʻi",
             note="JIM sahna. Maqolning ikkinchi yarmi."),

        rule("Chiroq tagi qorongʻi",
             strip=K % "등잔 밑" + " → chiroq tagi   ·   " + K % "어둡다"
                   + " → qorongʻi",
             meaning="Eng yaqin narsani koʻrmaslik — ikkala xalqning ham "
                     "bir xil kuzatuvi. Shuning uchun bu maqolni tarjima "
                     "qilish kerak emas: u allaqachon oʻzbekcha.",
             dur=10.0),

        ask("«밑» tag boʻlsa, «위» nima degani? 책상 위 qanday joy?",
            dur=7.4,
            note="Javobni aytmang. Jadval qoidani berdi, bu soʻzni bermadi."),

        practice("Prime Korean · 100 dars",
                 sub="Koreys tili noldan, oʻzbekchada", dur=5.4,
                 note="Maqol — tilning ustidagi qavat. Avval tilning oʻzi."),

        outro(line2="koreys tili · 속담"),
    ],
)

narrate(VIDEO, [
    "Koreysda shunday maqol bor: *등잔 밑이 어둡다*. "
    "|| Chiroq tagi qorongʻi.",

    "Afsona koʻzoynagini butun uydan qidirdi.",

    "U peshonasida turgan edi.",

    None,   # echo(등잔 밑) — jim sahna, koreyscha ovoz

    "Endi qarang. Har bir boʻlagining tagida oʻzbekchasi turibdi.",

    "*밑* — tag degani. | Va u narsadan keyin turadi: *책상 밑* — stol tagi. "
    "|| Xuddi bizdagidek.",

    None,   # echo(어둡다) — jim sahna, koreyscha ovoz

    "Oldingi maqollarda hayvon almashardi. | Bu yerda esa hech narsa "
    "almashmagan. || Maqol allaqachon oʻzbekcha.",

    "Endi oʻzingiz oʻylang. *밑* tag boʻlsa, *위* nima degani? "
    "|| Izohda kutamiz.",

    "Koreys tili noldan Powertyda: Praym Korean, yuzta dars. "
    "| Havola profilda.",

    None,   # outro — jim
])
