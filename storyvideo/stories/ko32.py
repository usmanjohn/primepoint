# -*- coding: utf-8 -*-
"""KO-32 — «Maymun ham yiqiladi»  ·  BIR MAQOL, IKKI TIL  ·  속담 07

Manba: Burchak → 속담 이야기 (Koreys maqollari) — 원숭이도 나무에서 떨어진다.

Seriyaning yettinchisi. Arc oʻsha: vaziyat → gʻalati tasvir → tekislash →
egizak → qoida.

⛔ SERIES.md ning qatʼiy qoidasi: maymun va ot bir-birining tarjimasi EMAS.
Ular egizak maqollar, hayvonlari esa egizak emas. Umumiysi — VAZIFA: har bir
xalq oʻz olamidagi eng ustasini oladi. Koreysda daraxtga chiqishning ustasi —
maymun; oʻzbekda oyoq ustasi — ot. Filmda aynan shu aytiladi.

TIL DARSI (maqol hikmatining oʻzi emas — SERIES.md talabi): **도 = «ham»**.
Bitta boʻgʻin olib tashlansa, maqol yoʻqoladi va oddiy xabar qoladi:
«maymun daraxtdan yiqiladi». Maqolni yasaydigan soʻz — 도. PK-16.
"""

from spec import Video, narrate
from scenes import (cover, order, pairs, echo, rule, ask, practice, outro)

VIDEO = Video(
    slug="ko32",
    lesson="PK-16",
    title="Maymun ham yiqiladi",
    story="속담 이야기 — 원숭이도 나무에서 떨어진다",
    subject="korean",
    scenes=[
        cover("원숭이", "Bizda — ot",
              kicker="Bir maqol, ikki til", ko="한국어",
              track="속담", n=7, badge="big",
              context="Koreys maqolida — maymun:",
              strike=False,
              note="MUQOVA: gʻalati narsa — maqolda maymun. Vaʼda ikki "
                   "soʻz va u qarama-qarshilik emas, juftlik."),

        order([("Koreyscha", [("원숭이도", "s"), ("나무에서", "o"),
                              ("떨어진다", "v")], True),
               ("Soʻzma-soʻz", [("Maymun ham", "s"), ("daraxtdan", "o"),
                                ("yiqiladi", "v")], False),
               ("Oʻzbek egizagi", [("Otning ham", "s"), ("oyogʻi", "o"),
                                   ("toyadi", "v")], False)],
              head="Bir maqol, ikki til",
              verdict="Hayvon boshqa. Vazifa bitta.",
              dur=13.5,
              note="Uchinchi qator tushganda maqol tanish boʻlib qoladi. "
                   "Hayvonlar tarjima emas: har bir xalq oʻz olamidagi "
                   "eng ustasini oladi."),

        echo("원숭이도", gloss="maymun ham",
             note="JIM sahna. Toʻrt boʻgʻin — echo chegarasi ichida."),

        pairs([("원숭이 떨어진다", "«maymun yiqiladi» — oddiy xabar"),
               ("원숭이도 떨어진다", "«maymun ham yiqiladi» — maqol"),
               ("도", "«ham» — maqolni yasaydigan bitta boʻgʻin")],
              head="Bitta boʻgʻinni olib tashlang",
              tail="Maqolni hikmat emas, 도 yasaydi.",
              dur=13.0,
              note="Filmning TIL darsi. Ikkinchi qator birinchisidan faqat "
                   "bitta boʻgʻin bilan farq qiladi, va maʼnosi butunlay "
                   "boshqa."),

        echo("나무에서", gloss="daraxtdan — 에서 ning «-dan» vazifasi",
             note="JIM sahna, ikkinchisi. KO-5 aynan shu vazifani "
                  "oldindan aytib qoʻygan edi."),

        rule("도 qoʻshilsa, xabar maqolga aylanadi",
             strip="원숭이 = maymun   ·   원숭이도 = maymun ham",
             meaning="도 — oʻzbekcha «ham». U «hatto bu ham» degan maʼno "
                     "beradi, va aynan shu maqolning butun kuchi: gap "
                     "maymun haqida emas, ustaning ham xato qilishi haqida.",
             dur=10.5),

        ask("저도 학생이에요 — bu gapda 도 nimani bildiryapti? "
            "| Gapiruvchi yana kim haqida oʻylayapti?",
            dur=7.4,
            note="Javobni aytmang. Videoda 도 maqolda koʻrsatilgan, "
                 "oddiy gapda emas."),

        practice("Burchak · Koreys maqollari",
                 sub="powerty.uz → Burchak → 속담 이야기",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreys maqolida maymun bor. || Bizda esa — ot.",

    "원숭이도 나무에서 떨어진다. "
    "| Soʻzma-soʻz: maymun ham daraxtdan yiqiladi. "
    "|| Otning ham oyogʻi toyadi. "
    "| Hayvon boshqa, vazifa bitta: har bir xalq oʻz olamidagi eng "
    "ustasini oladi.",

    None,   # echo(원숭이도)

    "Endi bitta boʻgʻinni olib tashlang. "
    "| 원숭이 떨어진다 — maymun yiqiladi. Oddiy xabar. "
    "|| 원숭이도 떨어진다 — maymun *ham* yiqiladi. Maqol. "
    "| Maqolni hikmat emas, mana shu bitta boʻgʻin yasaydi.",

    None,   # echo(나무에서)

    "도 — oʻzbekcha «ham». | Va maqolning butun kuchi shu soʻzda: "
    "gap maymun haqida emas, ustaning ham xato qilishi haqida.",

    "Endi oʻzingiz oʻylang. 저도 학생이에요 — bu gapda 도 nimani "
    "bildiryapti? || Izohda kutamiz.",

    "Koreys maqollari — Powertyda, Burchak boʻlimida.",

    None,   # outro
])
