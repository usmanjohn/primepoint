# -*- coding: utf-8 -*-
"""KO-16 — «Yoʻlbars ham keladi»  ·  BIR MAQOL, IKKI TIL

속담: 호랑이도 제 말 하면 온다 — «yoʻlbars ham oʻzi haqida gapirsang keladi».
Oʻzbekchasi: «Boʻrini yoʻqlasang, qulogʻi koʻrinar.»

The first film of a new series, and the series exists because of one
observation the channel is uniquely placed to make: a Korean proverb and an
Uzbek proverb are very often the SAME proverb with a different animal in it.
An English-language Korean channel cannot say that. This one can, and the
`order` beat proves it in columns before a word of narration -- three cells
wide, three rows deep, and only the middle row is a translation.

So the shape is not «Tutilgan xato». Nobody is wrong here. The arc is
    situation -> the strange picture -> the alignment -> the twin -> the rule
and the turn is the moment the Uzbek row lands underneath and matches.

⚠️ The narration never says 호랑이 and «boʻri» in the same breath as if one
were the translation of the other. It is not: the proverbs are twins, the
animals are not. What they share is the JOB -- the most feared animal in the
listener's own hills -- and saying that is the film.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, echo, order, versus,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:88px">%s</span>'

VIDEO = Video(
    slug="ko16",
    lesson="속담",
    title="Yoʻlbars ham keladi",
    story="Koreys maqollari",
    subject="korean",
    scenes=[
        cover("호랑이도 온다", "Bizda bu — boʻri",
              kicker="Bir maqol, ikki til",
              context="Koreys maqoli:",
              strike=False,
              note="MUQOVA: chiziq yoʻq — bu xato emas, gʻalati narsa. "
                   "Yoʻlbars keladigan maqol aylanib oʻtilmaydi."),

        says("Sherbek", [("Sardor haqida gapirayotgan edik:", "lbl"),
                         ("호랑이도 제 말 하면 온다", "expr ko")],
             mood="smile",
             note="Vaziyat: kimnidir gapirib turibsiz. Koreys shu paytda "
                  "shu maqolni aytadi."),

        consequence("Sardor", "Meni chaqirdingizmi?",
                    mood="smile",
                    cam="pull",
                    note="Maqolning oʻzi roʻy berdi. «Consequence» beati bu "
                         "yerda xatoning bahosi emas — kutilmagan kirish."),

        echo("호랑이", gloss="yoʻlbars",
             head="Maqoldagi hayvon",
             note="JIM sahna. Avval hayvonning oʻz nomi."),

        order([("Koreyscha", [("호랑이도", "s"), ("제 말 하면", "o"),
                              ("온다", "v")], True),
               ("Soʻzma-soʻz", [("yoʻlbars ham", "s"), ("gapirsang", "o"),
                                ("keladi", "v")], False),
               ("Oʻzbekcha", [("boʻrini", "s"), ("yoʻqlasang", "o"),
                              ("qulogʻi koʻrinar", "v")], False)],
              head="Bitta maqol, ikkita til",
              verdict="Faqat hayvon almashgan",
              dur=13.0,
              note="Filmning butun dalili shu setkada: uchta ustun, "
                   "uchta qator, va oʻzbekcha qator tagiga aynan tushadi."),

        versus({"name": "KOREYADA",
                "qty": KQ % "호랑이",
                "price": "togʻda",
                "tag": "eng qoʻrqinchli jonivor"},
               {"name": "BIZDA",
                "qty": '<span style="font-size:76px">Boʻri</span>',
                "price": "dashtda",
                "tag": "eng qoʻrqinchli jonivor"},
               title="Nega boshqa hayvon",
               verdict="Maqol tarjima qilinmaydi — almashtiriladi",
               dur=12.5,
               note="Ikkala hayvon ham bitta ishni bajaradi: tinglovchining "
                    "oʻz togʻidagi eng qoʻrqinchli jonivor."),

        echo("호랑이도 온다", gloss="yoʻlbars ham keladi", size=112,
             note="JIM sahna. Maqolning qisqargan, kundalik shakli. "
                  "`size=` berilgan: .pron__k oʻzi kichraymaydi."),

        rule("Yoʻlbars ham oʻzi haqida gapirsang keladi",
             strip=K % "호랑이" + " → yoʻlbars   ·   " + K % "온다" + " → keladi",
             meaning="Maqolni soʻzma-soʻz oʻgirish uni oʻldiradi. Koreys "
                     "yoʻlbarsni togʻda koʻrgan, biz boʻrini dashtda "
                     "koʻrganmiz — gap hayvonda emas, qoʻrquvda.",
             dur=10.0),

        ask("Koreyada ayiq ham bor. Nega maqolda aynan yoʻlbars turibdi?",
            dur=7.4,
            note="Javobni aytmang. Filmda sabab bor, javob yoʻq."),

        practice("Prime Korean · 100 dars",
                 sub="Koreys tili noldan, oʻzbekchada", dur=5.4,
                 note="Maqolni tushunish uchun avval til kerak."),

        outro(line2="koreys tili · 속담"),
    ],
)

narrate(VIDEO, [
    "Koreysda shunday maqol bor: *호랑이도 제 말 하면 온다*. "
    "|| Yaʼni: yoʻlbars ham oʻzi haqida gapirsang keladi.",

    "Sherbek uni Sardor haqida gapirayotganda aytdi.",

    "Va Sardor eshikdan kirdi.",

    None,   # echo(호랑이) — jim sahna, koreyscha ovoz

    "Endi qarang: har bir boʻlagining tagida oʻzbekcha qatori turibdi.",

    "Boʻrini yoʻqlasang, qulogʻi koʻrinar. || Bir xil maqol. "
    "Faqat hayvon almashgan.",

    None,   # echo(호랑이도 온다) — jim sahna, koreyscha ovoz

    "Chunki maqol soʻzma-soʻz oʻgirilmaydi — almashtiriladi. "
    "|| Koreys yoʻlbarsni togʻda koʻrgan, biz boʻrini dashtda koʻrganmiz.",

    "Endi oʻzingiz oʻylang. Koreyada ayiq ham bor. "
    "|| Nega maqolda aynan yoʻlbars turibdi? Izohda kutamiz.",

    "Koreys tili noldan Powertyda: Praym Korean, yuzta dars. "
    "| Havola profilda.",

    None,   # outro — jim
])
