# -*- coding: utf-8 -*-
"""KO-12 — Bitta boʻgʻin, teskari maʼno  ·  TUTILGAN XATO

Manba: Prime Korean PK-16 (도, 만, 부터, 까지 — qolgan asosiy qoʻshimchalar).

The sharpest mistake in the series: 도 and 만 are one syllable each and they
mean opposite things.

    저도 갔어요   men HAM bordim      -- includes everyone else
    저만 갔어요   FAQAT men bordim    -- excludes everyone else

So the cost is not a shade of politeness (ko04) or a confused listener (ko07) —
it is the opposite of what was meant, said fluently. Uzbek keeps «ham» and
«faqat» as separate words, so the concept is already the pupil's; what is new
is that the whole distinction rides on one syllable glued to the noun.

⚠️ The narration never says 도 or 만 ALONE. In isolation korean.py romanises
도 as `toʻ` (word-initial, hard) but as `doʻ` inside 저도 — both correct, and a
pupil hearing the pair would wonder which. So every mention in the voice is
attached to a word; the bare particles live on screen, where the Hangul is
unambiguous.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, correct, versus, echo, pairs,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:86px">%s</span>'

VIDEO = Video(
    slug="ko12",
    lesson="PK-16",
    title="Bitta boʻgʻin, teskari maʼno",
    story="Prime Korean PK-16",
    subject="korean",
    scenes=[
        cover('저<span class="strike">만</span> 갔어요', "Hammani inkor qildi",
              kicker="Tutilgan xato",
              context="«Men ham bordim» demoqchi edi:",
              strike=False,
              note="MUQOVA: chiziq bitta boʻgʻindan oʻtadi, vaʼda esa "
                   "natijani aytadi. Seriyadagi eng keskin xato — maʼno "
                   "teskarisiga aylanadi."),

        says("Jasur", [("«Men ham bordim» demoqchi edi:", "lbl"),
                       ("저만 갔어요", "expr ko")],
             mood="smile",
             note="Ravon aytdi, hech kim tuzatmadi."),

        consequence("Afsona", "Faqat u borganmi?",
                    mood="oh",
                    note="Xatoning bahosi: Jasur qolganlarning hammasini "
                         "inkor qilgan boʻlib chiqdi."),

        correct("만", "도",
                because="«Ham» — 도. «Faqat» — 만.",
                lead="저__ 갔어요",
                note="Bitta boʻgʻin, va maʼno teskarisiga oʻgiriladi."),

        versus({"name": "HAM — qoʻshadi",
                "qty": KQ % "도",
                "price": K % "저도 갔어요",
                "tag": "men ham bordim"},
               {"name": "FAQAT — ayiradi",
                "qty": KQ % "만",
                "price": K % "저만 갔어요",
                "tag": "faqat men bordim"},
               title="Bir boʻgʻin, ikki tomon",
               dur=12.0,
               note="Chap ustun odam qoʻshadi, oʻng ustun hammasini "
                    "ayiradi. Oʻrtasi yoʻq."),

        echo("저도 갔어요", gloss="men ham bordim",
             note="JIM sahna. Jasur aytishi kerak boʻlgan gap."),

        pairs([("저도",   "men ham"),
               ("저만",   "faqat men"),
               ("친구도", "doʻstim ham"),
               ("물만",   "faqat suv")],
              head="Har qanday otga yopishadi",
              tail="Qoʻshimcha otga yopishadi, gap tartibi oʻzgarmaydi",
              note="Toʻrtta misol: qoʻshimcha otga yopishadi, gap tartibi "
                   "oʻzgarmaydi."),

        echo("저만 갔어요", gloss="faqat men bordim",
             note="JIM sahna. Notoʻgʻri emas — boshqa maʼno. Ikkalasini "
                  "yonma-yon eshitish farqni mixlaydi."),

        rule("Oʻzbekchada ikkita soʻz, koreyschada ikkita boʻgʻin",
             strip=K % "도" + " → ham   ·   " + K % "만" + " → faqat",
             meaning="Farqni siz allaqachon bilasiz — «men ham» va «faqat "
                     "men» oʻzbekchada ham teskari. Yangi narsa shu: butun "
                     "maʼno otga yopishgan bitta boʻgʻinda turadi.",
             dur=9.8),

        ask("Restoranda «faqat suv» demoqchisiz. "
            "Qaysi boʻgʻinni qoʻyasiz?",
            dur=7.0,
            note="Javobni aytmang. Jadvalning oxirgi qatorida turgan."),

        practice("Prime Korean · PK-16",
                 sub="Qolgan asosiy qoʻshimchalar", dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Jasur «men ham bordim» demoqchi edi va *저만 갔어요* dedi. "
    "|| Ravon aytdi. Maʼnosi esa teskari.",

    "Afsona uni chaqirgan edi va javobni eshitdi.",

    "Chunki Jasur qolganlarning hammasini inkor qilgan boʻlib chiqdi.",

    "Almashadigan narsa bitta boʻgʻin. || *저만* emas, *저도*.",

    "Qarang. *저도 갔어요* — men ham bordim, yaʼni boshqalar ham borgan. "
    "| *저만 갔어요* — faqat men bordim, yaʼni boshqalar bormagan. "
    "|| Chap tomon odam qoʻshadi, oʻng tomon hammasini ayiradi.",

    None,   # echo(저도 갔어요) — jim sahna, koreyscha ovoz

    "Bu qoʻshimchalar har qanday otga yopishadi. | *저도* — men ham. "
    "| *친구도* — doʻstim ham. || *물만* — faqat suv.",

    None,   # echo(저만 갔어요) — jim sahna, koreyscha ovoz

    "Farqni siz allaqachon bilasiz: «men ham» va «faqat men» oʻzbekchada "
    "ham teskari. || Yangi narsa shu — butun maʼno otga yopishgan bitta "
    "boʻgʻinda turadi.",

    "Endi oʻzingiz oʻylang. Restoranda «faqat suv» demoqchisiz. "
    "|| Qaysi boʻgʻinni qoʻyasiz? Izohda kutamiz.",

    "Qoʻshimchalar Powertyda: Praym Korean, oʻn oltinchi dars.",

    None,   # outro — jim
])
