# -*- coding: utf-8 -*-
"""KO-4 — «고마워» xatosi  ·  TUTILGAN XATO

Manba: Prime Korean PK-11 (Nutq darajalari: 존댓말 va 반말).

The first film in the «Tutilgan xato» series and the first with a `cover`.
Its job is to prove the format travels: the maths films catch a wrong divisor,
this one catches a wrong speech level, and the arc is unchanged --
`says -> consequence -> correct`. Nothing about `claim -> consequence ->
correct` was ever about arithmetic; it was about a mistake with a cost.

The mistake is real and extremely common: Korean drama dialogue is almost all
반말, because the characters are close. A pupil who learns «rahmat» from a
drama learns the one form they must never use on a manager. Uzbek gives the
lever for free -- senlash/sizlash is exactly the distinction, so the cost
lands in one sentence with nothing to explain.
"""

from spec import Video, narrate
from scenes import cover, says, consequence, correct, pairs, echo, rule, ask, practice, outro

K = '<span class="ko">%s</span>'

VIDEO = Video(
    slug="ko04",
    lesson="PK-11",
    title="«고마워» xatosi",
    story="Prime Korean PK-11",
    subject="korean",
    scenes=[
        cover("고마워", "Bu — qoʻpollik",
              kicker="Tutilgan xato",
              context="Sardor buni direktoriga aytdi:",
              note="MUQOVA = eskiz. Notoʻgʻri soʻz chizib tashlangan, "
                   "vaʼda esa toʻrt soʻzdan kam."),

        says("Sardor", [("Serialda shunday deyishardi:", "lbl"),
                        ("고마워", "expr ko")],
             mood="smile",
             note="Xato tugʻilgan joy: serial qahramonlari bir-biriga "
                  "yaqin, shuning uchun hammasi 반말da gapiradi."),

        consequence("Nodira opa", "Xodimim menga «sen»lab gapirdi.",
                    mood="oh",
                    note="Xatoning bahosi bitta yuzda. Grammatik xato emas — "
                         "odob xatosi."),

        correct("고마워", "감사합니다",
                because="Rahbarga, ustozga, mijozga — har doim hurmat shakli",
                lead="Kimga aytilgani muhim",
                note="Chizib tashlangani — 반말, oʻrniga kelgani — 존댓말."),

        pairs([("고마워",     "doʻstga va ukaga"),
               ("고마워요",   "tanish odamga, xushmuomala"),
               ("감사합니다", "rahbarga, ustozga, mijozga"),
               ("고맙습니다", "xuddi shu — ammo issiqroq")],
              head="Bitta «rahmat», toʻrtta daraja",
              tail="Kim bilan gaplashyapsiz — shu tanlaydi",
              note="Jadval dalil keltiradi: tanlov soʻzda emas, "
                   "tinglovchida."),

        echo("감사합니다", gloss="rahmat", size=120,
             note="JIM sahna. Koreyscha ovoz ikki marta aytadi."),

        rule("Koreys tilida shunchaki rahmat degan soʻz yoʻq",
             strip=K % "고마워" + "  ·  " + K % "고마워요" + "  ·  " + K % "감사합니다",
             meaning="Har bir «rahmat» kimga aytilganini oʻzida saqlaydi. "
                     "Oʻzbekchada ham «rahmat» va «katta rahmat, ustoz» bir "
                     "xil emas — farqi koreys tilida feʼlning shaklida turadi.",
             dur=9.6),

        ask("Koreys odami tanishganda darhol yoshingizni soʻraydi. "
            "Nega bu savol eng birinchi beriladi?",
            dur=7.4,
            note="Javobni aytmang — video uni koʻrsatdi, aytmadi."),

        practice("Prime Korean · PK-11",
                 sub="Nutq darajalari — kimga qanday gapirasiz", dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Sardor koreys serialidan bitta soʻz oʻrgandi: *고마워*. "
    "|| Va uni direktoriga aytdi.",

    "Serialda qahramonlar bir-biriga shunday deyishadi. | Sardor esa buni "
    "shunchaki «rahmat» deb yodlab qoʻygan edi.",

    "Direktorning yuzi oʻzgardi. || Chunki Sardor unga *sen*lab gapirgan edi.",

    "*고마워* — bu yaqin odamga aytiladigan shakl. | Doʻstga, ukaga. "
    "|| Rahbarga esa *감사합니다*.",

    "Bitta «rahmat» — toʻrtta daraja. Doʻstga *고마워*. | Tanish odamga "
    "*고마워요*. | Rahbarga, ustozga, mijozga *감사합니다*. || Toʻrtinchisi "
    "ham bor: *고맙습니다* — xuddi shu maʼno, ammo issiqroq.",

    None,   # echo — jim sahna, koreyscha ovoz

    "Shuning uchun koreys tilida shunchaki «rahmat» degan soʻz yoʻq. "
    "|| Oʻzbekchada ham «rahmat» va «katta rahmat, ustoz» bir xil emas. "
    "| Koreys tilida bu farq feʼlning oxirida turadi.",

    "Endi oʻzingiz oʻylang. Koreys odami tanishganda darhol yoshingizni "
    "soʻraydi. || Nega bu savol eng birinchi beriladi? Izohda kutamiz.",

    "Nutq darajalari Powertyda: Prime Korean, 11-dars.",

    None,   # outro — jim
])
