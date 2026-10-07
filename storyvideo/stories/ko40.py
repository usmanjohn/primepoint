# -*- coding: utf-8 -*-
"""KO-40 — «Eshagidan toʻshagi qimmat»  ·  BIR MAQOL, IKKI TIL  ·  속담 09

Manba: Burchak → 속담 이야기 (order 14) — 배보다 배꼽이 더 크다.
Vaziyat ham, oʻzbek egizagi ham oʻsha hikoyaning oʻzidan: Jisu uch ming
vonlik telefon gʻilofini topadi, yetkazib berish — besh ming von;
«Oʻzbekchada: Eshagidan toʻshagi qimmat». Filmda qahramon Afsona (pupil).

Seriyaning toʻqqizinchisi. Arc: vaziyat → gʻalati tasvir → tekislash →
egizak → qoida.

⛔ SERIES.md: kindik va toʻshak bir-birining tarjimasi EMAS. Ularning
umumiy tomoni — vazifa: asosiy narsa va unga ilashgan kichik narsa. Filmda
aynan shu aytiladi.

TIL DARSI: **배 — uchta soʻz, bitta yozuv**: qorin, nok, kema (KO-17 dagi
말 = soʻz/ot gomografi bilan bir oila). Ikkinchi, kichikroq dars rule
satrida: 보다 = oʻzbekcha «-dan» — taqqoslash ham oʻzbekcha tartibda.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, order, echo, pairs, rule, ask,
                    practice, outro)

VIDEO = Video(
    slug="ko40",
    lesson="Burchak · 속담",
    title="Eshagidan toʻshagi qimmat",
    story="속담 이야기 — 배보다 배꼽이 더 크다",
    subject="korean",
    scenes=[
        cover("배꼽이 더 크다", "Bizda — toʻshak",
              kicker="Bir maqol, ikki til", ko="한국어",
              track="속담", n=9, badge="big",
              context="Koreys maqolida kindik qorindan katta:",
              strike=False, size=124,
              note="MUQOVA: gʻalati narsa — kindik qorindan katta. Vaʼda "
                   "ikki soʻz, juftlik (ko37 «Bizda — devor» bilan bir xil)."),

        says("Afsona", [("Telefon gʻilofi: 3 000 von", "lbl"),
                        ("Yetkazib berish: 5 000 von", "expr")],
             mood="smile", dur=6.6,
             note="Hikoyadagi raqamlar: 삼천 원 va 오천 원."),

        consequence("Afsona",
                    "아이고! Gʻilofdan pochtasi qimmat!",
                    mood="shock", close=True, dur=6.4,
                    note="Yaqin plan, hayqiriq — foydalanuvchi soʻragan "
                         "koreyscha 아이고."),

        order([("Koreyscha", [("배보다", "s"), ("배꼽이", "o"),
                              ("더 크다", "v")], True),
               ("Soʻzma-soʻz", [("Qorindan", "s"), ("kindik", "o"),
                                ("kattaroq", "v")], False),
               ("Oʻzbekcha", [("Eshagidan", "s"), ("toʻshagi", "o"),
                              ("qimmat", "v")], False)],
              head="Bir maqol, ikki til",
              verdict="Qorin — eshak. Kindik — toʻshak.",
              dur=13.0,
              note="Uch qator bir xil ustunlarda — oʻzbekcha qator koreyscha "
                   "bilan soʻzma-soʻz tekislanadi: -dan · ega · kesim."),

        echo("배꼽", gloss="kindik",
             note="JIM sahna. Ikki boʻgʻin."),

        pairs([("배 — qorin", "배가 아파요 — qornim ogʻriyapti"),
               ("배 — nok", "배가 달아요 — nok shirin"),
               ("배 — kema", "배를 타요 — kemaga chiqaman")],
              head="배 — uchta soʻz, bitta yozuv",
              tail="Qaysi biri ekanini gap aytadi.",
              dur=13.0,
              note="Filmning TIL darsi: gomograf. ko17 ning 말 si bilan "
                   "bir oila."),

        pairs([("배 — qorin", "asosiy narsa"),
               ("배꼽 — kindik", "undagi kichkina nuqta"),
               ("Eshak · toʻshak", "bizda — oʻsha juftlik")],
              head="Nega aynan kindik?",
              tail="Qoʻshimcha asosiydan oshib ketdi — ish teskari.",
              dur=12.0,
              note="⛔ Tarjima emas: vazifa bitta — asosiy va unga "
                   "ilashgan kichik narsa."),

        echo("배보다 배꼽", gloss="qorindan kindik",
             note="JIM sahna, ikkinchisi. Besh boʻgʻin — chegara ichida."),

        rule("배보다 배꼽이 더 크다 — qoʻshimcha asosiydan katta",
             strip='배 = qorin   ·   배꼽 = kindik   ·   보다 = <span style="white-space:nowrap">«-dan»</span>',
             meaning="Asosiy narsadan unga ilashgani qimmatroq boʻlib "
                     "ketsa, koreys shu maqolni aytadi. 보다 esa oʻzbekcha "
                     '<span style="white-space:nowrap">«-dan»</span>: '
                     "qorin-DAN, 배-보다 — taqqoslash ham bizning "
                     "tartibda.",
             dur=11.0),

        ask("배를 먹었어요. "
            "Qaysi 배 — qorin, nok yoki kema?",
            dur=6.8,
            note="Javobni aytmang (nok). Kema va qorinni yeb boʻlmaydi — "
                 "kulgili savol."),

        practice("Burchak · Koreys maqollari",
                 sub="powerty.uz → Burchak → Koreys maqollari",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreys maqolida kindik qorindan katta. "
    "|| Bizda esa — toʻshak eshakdan qimmat.",

    "Afsona internetda telefon gʻilofi topdi: 3 000 von. "
    "| Yetkazib berish esa — 5 000.",

    "[gasps] 아이고! || Gʻilofdan pochtasi qimmat.",

    "Koreyslar buni shunday deydi: 배보다 배꼽이 더 크다. "
    "| Qorindan kindik katta. || Bizda: eshagidan toʻshagi qimmat.",

    None,   # echo(배꼽)

    "Endi tilga qarang. | 배 — qorin. | 배 — nok. "
    "|| 배 — kema ham. Uchalasi bir xil yoziladi.",

    "Qorin — asosiy, kindik — undagi kichkina nuqta. "
    "|| Bizda bu juftlik — eshak va uning toʻshagi.",

    None,   # echo(배보다 배꼽)

    "Qoʻshimcha asosiydan oshib ketsa — shu maqol. "
    "|| 배보다 — qorindan: taqqoslash ham bizning tartibda.",

    "Endi oʻzingiz, oshqovoqchalar: 배를 먹었어요. "
    "| Qaysi birini yedi? [laughs] || Izohda kutamiz.",

    "Bu maqolning toʻliq hikoyasi — Powertyda, Burchak boʻlimida.",

    None,   # outro
])
