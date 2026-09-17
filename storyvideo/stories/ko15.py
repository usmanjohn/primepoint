# -*- coding: utf-8 -*-
"""KO-15 — «Bitta katak»  ·  TUTILGAN XATO  ·  TOPIK

Manba: examprep TOPIK — «TOPIK II — Kirish (1-qism)», 7-blok, oʻsha darsning
oʻz ogohlantirishi: «Bitta siljish keyingi barcha javoblarni buzadi.»

The third TOPIK film, and the cheapest disaster on the whole test: nothing
here is about Korean at all. A candidate skips a hard question meaning to
come back, marks the NEXT question's answer in the skipped question's row,
and every answer after it is one box out. Twenty-eight questions, fifty-six
points, all of them known.

That is why it closes the TOPIK band. ko13 costs you a register you never
learned; ko14 costs you a clock you never watched; this one costs you
answers you actually had. The arithmetic is the whole argument, so it is on
screen and `lint` recomputes it: (50 − 22) × 2 = 56.

⚠️ Nothing is invented about the exam room: the film names the answer sheet
and the habit of checking a number against a number, and stops. Pens, papers
and permitted items differ by centre and by year, and a film cannot be
re-recorded when they change.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, check, correct, pairs, echo,
                    rule, ask, practice, outro)

K = '<span class="ko">%s</span>'

VIDEO = Video(
    slug="ko15",
    lesson="TOPIK 답안지",
    title="Bitta katak",
    story="examprep TOPIK — strategiya",
    subject="korean",
    scenes=[
        cover("−56 ball", "Javob varagʻi siljib ketdi",
              kicker="Tutilgan xato · TOPIK",
              context="Bitta savolni tashlab ketdi:",
              strike=False,
              note="MUQOVA: gʻalati narsa — manfiy son. Chiziq yoʻq, chunki "
                   "xato javobda emas, varaqda."),

        says("Afsona", [("23-savol qiyin edi:", "lbl"),
                        ("Keyinroq belgilayman", "expr")],
             mood="smile",
             note="Qaror oqilona koʻrinadi. Xato keyingi harakatda."),

        consequence("Afsona", "Hamma javobim bitta katak surilgan.",
                    mood="oh",
                    note="24-savolning javobi 23-katakka tushdi. Shundan "
                         "keyin hammasi surildi."),

        check("(50 − 22) × 2 = 56",
              parts=["23-savoldan oxirigacha — 28 ta savol",
                     "Har biri 2 ball"],
              verdict="56 ball — bilgan javoblari uchun",
              title="Bitta siljish nima turadi",
              dur=9.6,
              note="Filmning butun dalili shu amalda. Bu ball bilim "
                   "yetishmaganidan emas, qatordan adashganidan ketdi."),

        correct("Keyinroq", "Hoziroq",
                because="Savolni tashlasangiz, katakni ham tashlang.",
                lead="Qiyin savol uchun qoida",
                note="Tuzatish bitta soʻzda: boʻsh savolning katagi ham "
                     "boʻsh qolsin."),

        pairs([("10-savol", "10-katak"),
               ("20-savol", "20-katak"),
               ("30-savol", "30-katak"),
               ("40-savol", "40-katak")],
              head="Har oʻn savolda bir marta",
              tail="Raqamni raqam bilan solishtiring, javobni emas",
              note="Odatning oʻzi: oʻn savolda bir marta ikkita raqamga "
                   "qarash. Siljish shunda bitta qatorda ushlanadi."),

        echo("답안지", gloss="javob varagʻi",
             head="Imtihon xonasidagi soʻz",
             note="JIM sahna. Imtihonda eshitiladigan soʻz."),

        rule("Belgilash ham imtihonning bir qismi",
             strip="Savol raqami" + " = " + "katak raqami",
             meaning="Koreys tilini bilish yetarli emas: ballni varaq "
                     "hisoblaydi. Bitta qatordan adashish ellik oltita "
                     "ballni yoʻq qiladi, va buni hech kim aytmaydi — "
                     "natija kelganda bilinadi.",
             dur=10.0),

        echo("확인하세요", gloss="tekshiring",
             note="JIM sahna. Filmning oʻz maslahati koreyscha."),

        ask("듣기 audiosi bir marta yangraydi. Belgilashni qachon "
            "qilasiz — eshitayotib, yoki keyinmi?",
            dur=7.6,
            note="Javobni aytmang. Ikkala tomonning ham bahosi bor, "
                 "shuning uchun bu haqiqiy koʻchirma savol."),

        practice("TOPIK · Imtihon kuni",
                 sub="Javob varagʻi, vaqt va darajalar", dur=5.4,
                 note="Powertydagi kirish darsining 7-bloki shu haqda."),

        outro(line2="koreys tili · TOPIK"),
    ],
)

narrate(VIDEO, [
    "Afsona yigirma uchinchi savolni qiyin deb tashlab ketdi. "
    "|| Keyinroq belgilayman, dedi.",

    "Keyingi savolning javobini esa boʻsh qatorga belgiladi.",

    "Shundan keyin hamma javobi bitta katak surildi.",

    "Sanaymiz. Yigirma uchinchidan ellikkacha — yigirma sakkizta savol. "
    "|| Har biri ikki ball. Ellik olti ball.",

    "U bu javoblarni bilardi. || Ketgani bilim emas, qator edi.",

    "Qoida bitta: savolni tashlasangiz, katagini ham tashlang. "
    "|| Va har oʻn savolda bir marta ikkita raqamga qarang.",

    None,   # echo(답안지) — jim sahna, koreyscha ovoz

    "Chunki ballni koreys tili emas, varaq hisoblaydi. || Bitta qatordan "
    "adashganingizni esa natija kelganda bilasiz.",

    None,   # echo(확인하세요) — jim sahna, koreyscha ovoz

    "Endi oʻzingiz oʻylang. Tinglash audiosi bir marta yangraydi. "
    "|| Belgilashni eshitayotib qilasizmi, yoki keyin? Izohda kutamiz.",

    "Imtihon kuni haqida hammasi Powertyda: Topik, strategiya. "
    "| Havola profilda.",

    None,   # outro — jim
])
