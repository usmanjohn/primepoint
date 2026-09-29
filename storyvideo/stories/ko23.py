# -*- coding: utf-8 -*-
"""KO-23 — «Yuz eshitish, bir koʻrish»  ·  BIR MAQOL, IKKI TIL

속담: 백문이 불여일견 (百聞不如一見) — «yuz marta eshitish bir marta
koʻrishcha emas». Oʻzbekchasi: «Yuz marta eshitgandan, bir marta koʻrgan
afzal.»

The fourth proverb film, and the one that joins the two series together. Every
other 속담 in the set is native Korean; this one is Chinese, and it is built
out of exactly the machinery the root films sell: 백 is a hundred, 일 is one,
문 is hearing, 견 is seeing. So the proverb is not memorised, it is READ --
which is the whole claim of ko01, ko10 and ko20, arriving in a place nobody
expects an argument about vocabulary.

That is why the mechanism beat is two `build`s rather than an `order`: the
alignment with the Uzbek twin is almost exact, so there is nothing to discover
in a column grid. The discovery is inside the four syllables.

⚠️ 百聞不如一見 is six characters, so it is NOT a 사자성어 (which means four).
The film calls it a 한자성어 and the narration calls it «xitoycha ibora».
Getting that wrong would be a claim about Korean made by somebody who had not
counted, in a film whose entire subject is counting syllables.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, build, echo, versus,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:92px">%s</span>'

VIDEO = Video(
    slug="ko23",
    lesson="속담",
    title="Yuz eshitish, bir koʻrish",
    story="Koreys maqollari · 한자성어",
    subject="korean",
    scenes=[
        cover("불여일견", "Bu — arifmetika",
              kicker="Bir maqol, ikki til",
              ko="한국어",
              context="«백문이 불여일견» — ichida ikkita son bor:",
              strike=False,
              note="MUQOVA: gʻalati narsa — maqolda son bor deyish. "
                   "Vaʼda uch soʻz va u savol uygʻotadi: qaysi sonlar?"),

        says("Bekzod", [("Oʻn daqiqa tushuntirdi:", "lbl"),
                        ("Metroda toʻrtinchi chiqish…", "expr")],
             mood="think",
             note="Vaziyat: gapirish bilan tushuntirishga urinish."),

        consequence("Jasur", "Xaritani koʻrsating.",
                    mood="oh", close=True,
                    note="Maqolning oʻzi roʻy berdi. Bir qarash oʻn "
                         "daqiqalik gapdan ustun chiqdi."),

        build([("백", "yuz — 100", False), ("문", "eshitish", True)],
              "백문", gloss="yuz marta eshitish",
              head="Maqolning birinchi yarmi",
              dur=9.5,
              note="YANGI BEAT. Ikkita boʻgʻin, ikkita xitoycha ildiz. "
                   "Oltin plitka — maʼno koʻtarib turgani."),

        build([("일", "bir — 1", False), ("견", "koʻrish", True)],
              "일견", gloss="bir marta koʻrish",
              head="Ikkinchi yarmi",
              caption="Oʻrtada turgan soʻz: 불여 — «…cha emas»",
              dur=11.0,
              note="Ikkinchi qurilish. Endi tomoshabin maqolning toʻrtta "
                   "boʻlagini ham biladi va uni oʻzi oʻqiy oladi."),

        echo("백문이", gloss="yuz marta eshitish",
             note="JIM sahna. Maqolning boshi."),

        versus({"name": "백문",
                "qty": KQ % "100",
                "price": "marta eshitish",
                "tag": "gapirib tushuntirish"},
               {"name": "일견",
                "qty": KQ % "1",
                "price": "marta koʻrish",
                "tag": "koʻrsatib tushuntirish"},
               title="Maqol — taqqoslash",
               verdict="Yuztasi bittasiga yetmaydi",
               dur=12.0,
               note="Filmning yuragi: son bilan yozilgan hikmat. Chap "
                    "ustun katta son, oʻng ustun kichik — va yutadigani "
                    "oʻng ustun."),

        echo("불여일견", gloss="bir koʻrishcha emas",
             note="JIM sahna. Maqolning ikkinchi yarmi."),

        rule("Yuz marta eshitgandan, bir marta koʻrgan afzal",
             strip=K % "백" + " → yuz   ·   " + K % "일" + " → bir   ·   "
                   + K % "불" + " → emas",
             meaning="Bu maqolni yodlash shart emas. Toʻrtta boʻgʻinning "
                     "maʼnosini bilgan odam uni birinchi koʻrishda oʻqiydi — "
                     "xuddi soʻz oilalaridagidek.",
             dur=10.5),

        ask("«불» — «emas» degani. Unda «불가능» nima degani?",
            dur=7.2,
            note="Javobni aytmang. Film 불 ni berdi, 가능 ni bermadi. "
                 "⚠️ OVOZDA 불 YOLGʻIZ AYTILMAYDI: u «pul» boʻlib "
                 "romanizatsiya qilinadi — oʻzbekcha nutq oʻrtasida "
                 "«pul» degan soʻz. Ekranda esa 한글 turibdi."),

        practice("Prime Korean · 100 dars",
                 sub="Koreys tili noldan, oʻzbekchada", dur=5.4,
                 note="Maqol — tilning ustidagi qavat."),

        outro(line2="koreys tili · 속담"),
    ],
)

narrate(VIDEO, [
    "Koreysda shunday maqol bor: *백문이 불여일견*. "
    "|| Va uning ichida ikkita son yashiringan.",

    "Bekzod Jasurga metro yoʻlini oʻn daqiqa tushuntirdi.",

    "Jasur bitta narsa soʻradi: xaritani.",

    "Endi maqolni ochamiz. *백* — yuz. | *문* — eshitish. "
    "|| Yaʼni: yuz marta eshitish.",

    "Keyingisi: *일* — bir. | *견* — koʻrish. || Bir marta koʻrish.",

    None,   # echo(백문이) — jim sahna, koreyscha ovoz

    "Demak maqol taqqoslayapti. Yuz marta eshitish — bir marta "
    "koʻrishcha emas.",

    None,   # echo(불여일견) — jim sahna, koreyscha ovoz

    "Bizda ham xuddi shu maqol bor: yuz marta eshitgandan, bir marta "
    "koʻrgan afzal. || Buni yodlash shart emas — oʻqib chiqarsa boʻladi.",

    "Endi oʻzingiz oʻylang. Maqoldagi uchinchi boʻgʻin «emas» degani. "
    "|| Unda *불가능* nima degani? Izohda kutamiz.",

    "Koreys tili noldan Powertyda: Praym Korean, yuzta dars. "
    "| Havola profilda.",

    None,   # outro — jim
])
