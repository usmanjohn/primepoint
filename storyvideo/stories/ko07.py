# -*- coding: utf-8 -*-
"""KO-7 — «Xayr» ikkiga boʻlinadi  ·  TUTILGAN XATO

Manba: Prime Korean PK-9 (Salomlashish, xayrlashish va oʻzini tanishtirish).

The same shape as ko05 and for the same reason: Uzbek has ONE word where Korean
has two, so the pupil's own language hides the distinction and the mistake is
not carelessness. There the collision was `-da`; here it is «xayr».

    안녕히 가세요   "yaxshi BORING"  -> to the one who is LEAVING
    안녕히 계세요   "yaxshi TURING"  -> to the one who is STAYING

So the form depends on who walks out of the room, and a learner who only knows
가세요 (which is the one every drama says, because the camera stays behind)
tells their own boss to leave the office. That is the film.

The `versus` scene carries the argument: the two cards are not two phrases, they
are two DIRECTIONS, and the tags say which way each one points.
"""

from spec import Video, narrate
from scenes import cover, says, consequence, correct, versus, echo, rule, ask, practice, outro

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:60px">%s</span>'

VIDEO = Video(
    slug="ko07",
    lesson="PK-9",
    title="«Xayr» ikkiga boʻlinadi",
    story="Prime Korean PK-9",
    subject="korean",
    scenes=[
        cover("안녕히 가세요", "Teskarisini aytdi",
              kicker="Tutilgan xato",
              context="Sardor oʻzi ketayotib aytdi:",
              note="MUQOVA: gap toʻgʻri, vaziyat teskari. Shuning uchun butun "
                   "ibora chizib tashlanadi — bu yerda xato bitta harfda emas."),

        says("Sardor", [("Ishdan chiqayotib:", "lbl"),
                        ("안녕히 가세요", "expr ko")],
             mood="smile",
             note="Serialda shu shakl koʻp eshitiladi, chunki kamera "
                  "qoladigan odam bilan qoladi — ketadigani esa aytmaydi."),

        echo("안녕히 가세요", gloss="«yaxshi boring» — ketayotgan odamga",
             head="Sardor aytgan gap", size=120,
             note="JIM sahna. Shakl notoʻgʻri emas — vaziyati notoʻgʻri, "
                  "shuning uchun uni eshitish zarar qilmaydi."),

        consequence("Nodira opa", "Men ketyapmanmi?",
                    mood="think",
                    note="Xatoning bahosi: rahbar oʻzini ketishga "
                         "chaqirilgan deb tushundi."),

        correct("가세요", "계세요",
                because="Ketayotgan odam «계세요» deydi",
                lead="안녕히 __",
                note="Faqat bitta boʻgʻin almashadi, maʼno esa teskari "
                     "tomonga oʻgiriladi."),

        versus({"name": "siz QOLASIZ",
                "qty": KQ % "안녕히 가세요",
                "price": "«yaxshi boring»",
                "tag": "ketayotgan odamga"},
               {"name": "siz KETASIZ",
                "qty": KQ % "안녕히 계세요",
                "price": "«yaxshi turing»",
                "tag": "qoladigan odamga"},
               title="Ikkalasi ham oʻzbekchada «xayr»",
               dur=12.5,
               note="Bu ikkita ibora emas — ikkita YOʻNALISH. Kim eshikdan "
                    "chiqayotgani shaklni tanlaydi."),

        echo("안녕히 계세요", gloss="«yaxshi turing» — oʻzingiz ketayotganda",
             size=120,
             note="JIM sahna. Aynan shu shaklni oʻrganish kerak: 가세요 ni "
                  "pupil allaqachon serialdan biladi."),

        rule("Xayrni kim ketayotganiga qarab tanlaysiz",
             strip=K % "가세요" + " → u ketadi   ·   " + K % "계세요" + " → siz ketasiz",
             meaning="Oʻzbekcha «xayr» ikkalasiga ham yetadi, shuning uchun "
                     "quloq bu farqni qidirmaydi. Bir marta yoʻnalish sifatida "
                     "tushunsangiz, boshqa adashmaysiz.",
             dur=9.6),

        ask("Ikkovingiz ham bir vaqtda, birga chiqib ketyapsiz. "
            "Unda bir-biringizga nima deysiz?",
            dur=7.6,
            note="Javobni aytmang. Ikkalasi ham ketayotgani uchun "
                 "yoʻnalish ikki tomonga ham bir xil — jadval ishora bergan."),

        practice("Prime Korean · PK-9",
                 sub="Salomlashish va xayrlashish", dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Sardor ishdan chiqayotib rahbariga *안녕히 가세요* dedi. "
    "|| Gap toʻgʻri. Vaziyat esa teskari.",

    "Bu shaklni serialda koʻp eshitasiz. | Chunki kamera qoladigan odam "
    "bilan qoladi.",

    None,   # echo(안녕히 가세요) — jim sahna, koreyscha ovoz

    "Rahbarning yuzi savolga toʻldi. || Chunki Sardor unga *ketavering* "
    "degan edi.",

    "Almashadigan narsa bitta boʻgʻin. | *가세요* emas, *계세요*.",

    "Qarang. Agar SIZ qolsangiz, ketayotgan odamga *안녕히 가세요* deysiz — "
    "yaxshi boring. | Agar SIZ ketsangiz, qoladigan odamga *안녕히 계세요* "
    "deysiz — yaxshi turing. || Oʻzbekchada ikkalasi ham «xayr».",

    None,   # echo(안녕히 계세요) — jim sahna, koreyscha ovoz

    "Shuning uchun koreyscha xayrni kim ketayotganiga qarab tanlaysiz. "
    "|| Oʻzbekcha «xayr» ikkalasiga ham yetadi, shuning uchun quloq bu "
    "farqni umuman qidirmaydi.",

    "Endi oʻzingiz oʻylang. Ikkovingiz ham bir vaqtda, birga chiqib "
    "ketyapsiz. || Unda bir-biringizga nima deysiz? Izohda kutamiz.",

    "Salomlashish va xayrlashish Powertyda: Prime Korean, toʻqqizinchi dars.",

    None,   # outro — jim
])
