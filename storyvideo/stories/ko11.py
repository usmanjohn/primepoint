# -*- coding: utf-8 -*-
"""KO-11 — «Men oʻquvchiman» va «oʻquvchim bor»  ·  TUTILGAN XATO

Manba: Prime Korean PK-13 (있다 / 없다 — bor va yoʻq).

The most-made beginner mistake in Korean and the funniest cost in the series:
이에요 is «to BE» and 있어요 is «to HAVE / to EXIST», and a learner who reaches
for the wrong one does not produce a grammar error — they produce a different,
perfectly grammatical sentence about a student they employ.

    저는 학생이에요      men oʻquvchiman
    저는 학생이 있어요   mening oʻquvchim bor

Uzbek does not cause this one: «-man» and «bor» are nothing alike. It is caused
by both Korean forms sitting in the same slot after the same noun, which is why
the mechanism scene is a `versus` of two whole sentences rather than two
particles -- the difference is not a syllable here, it is a verb.

The `check` deliberately teaches 있어요 as the RIGHT answer for a new sentence.
A film that left a pupil thinking 있어요 is the wrong word would have taught
half a lesson: both are correct, each in its own place.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, correct, versus, echo, check,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:64px">%s</span>'

VIDEO = Video(
    slug="ko11",
    lesson="PK-13",
    title="«Men oʻquvchiman» va «oʻquvchim bor»",
    story="Prime Korean PK-13",
    subject="korean",
    scenes=[
        cover('학생이 <span class="strike">있어요</span>', "Oʻquvchisi bor boʻlib qoldi",
              kicker="Tutilgan xato",
              context="«Men oʻquvchiman» demoqchi edi:",
              strike=False,
              note="MUQOVA: qizil chiziq faqat feʼldan oʻtadi — ot toʻgʻri, "
                   "feʼl boshqa. Vaʼda natijani aytadi, grammatikani emas."),

        says("Sherbek", [("Oʻzini tanishtirmoqchi edi:", "lbl"),
                         ("저는 학생이 있어요", "expr ko")],
             mood="smile",
             note="Gap grammatik jihatdan mukammal. Faqat maʼnosi boshqa."),

        echo("저는 학생이 있어요", gloss="mening oʻquvchim bor", size=96,
             head="Sherbek aytgan gap",
             note="JIM sahna. Shakl notoʻgʻri emas — maʼnosi boshqa, "
                  "shuning uchun uni eshitish zarar qilmaydi."),

        consequence("Nodira opa", "Oʻquvchisi bormi?",
                    mood="think",
                    note="Xatoning bahosi: rahbar uni oʻqituvchi deb "
                         "tushundi."),

        correct("있어요", "이에요",
                because="«...man» desangiz — 이에요",
                lead="학생 + __",
                note="Bu yerda almashadigan narsa qoʻshimcha emas — FEʼL."),

        versus({"name": "BOʻLMOQ",
                "qty": KQ % "이에요",
                "price": K % "저는 학생이에요",
                "tag": "men oʻquvchiman"},
               {"name": "BOR BOʻLMOQ",
                "qty": KQ % "있어요",
                "price": K % "학생이 있어요",
                "tag": "oʻquvchim bor"},
               title="Bitta otdan keyin ikkita feʼl",
               dur=12.0,
               note="Ikkisi ham bir joyda turadi, shuning uchun quloq "
                    "ularni farqlashni oʻrganishi kerak."),

        echo("저는 학생이에요", gloss="men oʻquvchiman", size=104,
             note="JIM sahna. Aytilishi kerak boʻlgan gap."),

        check("시간이 __",
              parts=["«Vaqtim bor» — bu bor boʻlmoq",
                     "Demak bu yerda 있어요 toʻgʻri"],
              verdict=K % "시간이 있어요",
              title="Endi 있어요 ning oʻz joyi",
              dur=8.4,
              note="Muhim: 있어요 notoʻgʻri soʻz emas. Bu sahna uni oʻz "
                   "joyiga qaytaradi, aks holda film yarim dars boʻlib "
                   "qoladi."),

        rule("Men ...man va Menda ... bor — ikkita boshqa feʼl",
             strip=K % "이에요" + " → boʻlmoq   ·   " + K % "있어요" + " → bor boʻlmoq",
             meaning="Oʻzbek tili bu xatoni keltirmaydi: «-man» va «bor» "
                     "bir-biriga oʻxshamaydi. Xato koreys tilining oʻzidan "
                     "keladi — ikkala feʼl ham bir xil otdan keyin turadi.",
             dur=9.8),

        ask("«Menda vaqt yoʻq» qanday aytiladi?",
            dur=7.0,
            note="Javobni aytmang. 있어요 ning inkori darsda bor, videoda "
                 "esa yoʻq — koʻchirma savol shu."),

        practice("Prime Korean · PK-13",
                 sub="Bor va yoʻq", dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Sherbek oʻzini tanishtirmoqchi edi va *저는 학생이 있어요* dedi. "
    "|| Grammatikada xato yoʻq. Maʼnosi esa boshqa.",

    "U «men oʻquvchiman» demoqchi edi. | Aytgani esa — mening oʻquvchim "
    "bor.",

    None,   # echo(저는 학생이 있어요) — jim sahna, koreyscha ovoz

    "Shuning uchun rahbar uni oʻqituvchi deb tushundi.",

    "Bu yerda almashadigan narsa qoʻshimcha emas. | Feʼl. || *있어요* "
    "emas, *이에요*.",

    "Qarang. *저는 학생이에요* — men oʻquvchiman. | *학생이 있어요* — "
    "mening oʻquvchim bor. || Ikkala feʼl ham bir xil otdan keyin turadi, "
    "shuning uchun quloq ularni farqlashni oʻrganishi kerak.",

    None,   # echo(저는 학생이에요) — jim sahna, koreyscha ovoz

    "Ammo *있어요* notoʻgʻri soʻz emas. | «Vaqtim bor» desangiz, bu — bor "
    "boʻlmoq. || Demak *시간이 있어요*. Bu yerda u toʻgʻri.",

    "Shuning uchun bu ikkitasi boshqa-boshqa feʼl. || Bu xato ona "
    "tilingizdan kelmaydi — koreys tilining oʻzidan keladi.",

    "Endi oʻzingiz oʻylang. «Menda vaqt yoʻq» qanday aytiladi? "
    "|| Izohda kutamiz.",

    "Bor va yoʻq Powertyda: Praym Korean, oʻn uchinchi dars.",

    None,   # outro — jim
])
