# -*- coding: utf-8 -*-
"""KO-21 — «Kim qilmadi?»  ·  TUTILGAN XATO

Manba: Prime Korean PK-12 (은/는 va 이/가 — mavzu va ega orasidagi farq).

The mistake every Korean course promises to explain and almost none explains
usefully, because the usual explanation («topic vs subject») is a grammar term
standing in for a feeling. This film does not explain it. It gives one rule
that is mechanical, checkable and right far more often than a beginner's
instinct: **a question asked with 이/가 is answered with 이/가.**

The shape is «social cost», like ko04 and ko08 -- nothing ungrammatical
happens. 저는 안 했어요 is a perfectly good sentence. It just means something
the speaker did not intend: 은/는 carries contrast, so answering «누가 안
했어요?» with it says «as for ME, I didn't» -- which points, silently, at
everybody else in the room.

⚠️ The narration never says «mavzu» and «ega» as a pair of terms. The pupil
who needs this film is not helped by two more words; they are helped by
hearing the question and the answer wear the same ending.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, correct, versus, pairs, echo,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:88px">%s</span>'

VIDEO = Video(
    slug="ko21",
    lesson="PK-12",
    title="Kim qilmadi?",
    story="Prime Korean PK-12",
    subject="korean",
    scenes=[
        cover('저<span class="strike">는</span>', "Butun sinfga shama",
              kicker="Tutilgan xato",
              ko="한국어",
              context="«누가 안 했어요?» — «저는 안 했어요»",
              strike=False,
              note="MUQOVA: chiziq faqat bitta harfdan oʻtadi — gap toʻgʻri, "
                   "qoʻshimcha notoʻgʻri. Vaʼda bahoni emas, oqibatni aytadi."),

        says("Nodira opa", [("Sinfdan soʻradi:", "lbl"),
                            ("누가 숙제를 안 했어요?", "expr ko")],
             mood="think",
             note="Savol *이/가* bilan qoʻyilgan: 누**가**. Film shu bitta "
                  "harfga qaraydi."),

        says("Bekzod", [("Rostini aytdi:", "lbl"),
                        ("저는 안 했어요", "expr ko")],
             mood="smile",
             note="Hech qanday grammatik xato yoʻq. Bekzod halol javob "
                  "berdi — va boshqa narsa aytib qoʻydi."),

        consequence("Nodira opa", "Demak qolganlar qilgan?",
                    mood="cross", close=True,
                    note="Xatoning bahosi: *는* qarama-qarshilik koʻtaradi. "
                         "YANGI: yaqin plan — bu sahna faqat yuz uchun bor."),

        correct("저는 안 했어요", "제가 안 했어요",
                because="Savol «kim?» — javob ham «men» bilan.",
                lead="누가 안 했어요?",
                shake=True,
                note="YANGI: xato qimirlaydi (`shake`), toʻgʻrisi esa "
                     "tepadan tushib qotadi (`stamp`). Almashadigan narsa "
                     "bitta harf."),

        versus({"name": "은/는",
                "qty": KQ % "저는",
                "price": "«men esa…»",
                "tag": "boshqalarga qarshi qoʻyadi"},
               {"name": "이/가",
                "qty": KQ % "제가",
                "price": "«aynan men»",
                "tag": "savolga javob beradi"},
               title="Bitta harf, ikkita maʼno",
               verdict="Savolga javob — har doim 이/가",
               dur=12.0,
               note="Chap ustun taqqoslaydi, oʻng ustun koʻrsatadi. "
                    "Oʻrtasi yoʻq."),

        echo("제가 했어요", gloss="men qildim",
             note="JIM sahna. Javobning toʻgʻri shakli."),

        pairs([("누가 왔어요?", "제가 왔어요"),
               ("뭐가 맛있어요?", "김치가 맛있어요"),
               ("어디가 아파요?", "머리가 아파요"),
               ("언제가 좋아요?", "내일이 좋아요")],
              head="Savolda 이/가 — javobda ham 이/가",
              tail="Savol qanday kiyinsa, javob ham shunday",
              note="Toʻrtta juft. Har qatorda savol ham, javob ham "
                   "*이/가* kiyadi — qoida koʻz bilan koʻrinadi."),

        echo("누가 왔어요", gloss="kim keldi?",
             note="JIM sahna. Savolning oʻzi — qoidaning boshlanish nuqtasi."),

        rule("Savol 이/가 bilan kelsa, javob ham 이/가 bilan ketadi",
             strip=K % "누가" + " → " + K % "제가" + "   ·   "
                   + K % "저는" + " → «men esa…»",
             meaning="Oʻzbekchada egaga hech qanday qoʻshimcha qoʻyilmaydi, "
                     "shuning uchun oʻrganuvchi ikkitasidan birini tavakkal "
                     "tanlaydi. Savolning oʻziga qarash — eng ishonchli yoʻl.",
             dur=10.0),

        ask("Unda «저는 안 했어요» qachon toʻgʻri boʻladi?",
            dur=7.2,
            note="Javobni aytmang. Film *는* ning maʼnosini koʻrsatdi, "
                 "lekin qaysi vaziyatda kerakligini aytmadi."),

        practice("Prime Korean · PK-12",
                 sub="은/는 va 이/가 — mavzu va ega", dur=5.4,
                 note="Darsning oʻzi Powertyda, mashqlari bilan."),

        outro(line2="koreys tili · grammatika"),
    ],
)

narrate(VIDEO, [
    "Nodira opa sinfdan soʻradi: *누가 숙제를 안 했어요*? "
    "|| Yaʼni: uy vazifasini kim qilmadi?",

    "Savolda bitta muhim harf bor: *누가*.",

    "Bekzod rostini aytdi: *저는 안 했어요*.",

    "Va butun sinf unga qaradi. || Chunki u «men esa qilmadim» degan edi.",

    "Almashadigan narsa bitta harf. | *저는* emas, *제가*.",

    "*저는* — boshqalarga qarshi qoʻyadi. || *제가* — savolga javob beradi.",

    None,   # echo(제가 했어요) — jim sahna, koreyscha ovoz

    "Qoida oddiy. Savolda *가* boʻlsa, javobda ham *가*. "
    "|| *누가 왔어요* — *제가 왔어요*.",

    None,   # echo(누가 왔어요) — jim sahna, koreyscha ovoz

    "Oʻzbekchada egaga hech narsa qoʻshilmaydi. | Shuning uchun biz "
    "ikkitasidan birini tavakkal tanlaymiz. || Savolning oʻziga qarang.",

    "Endi oʻzingiz oʻylang. *저는 안 했어요* qachon toʻgʻri boʻladi? "
    "|| Izohda kutamiz.",

    "Oʻn ikkinchi darsning oʻzi Powertyda: Praym Korean. "
    "| Havola profilda.",

    None,   # outro — jim
])
