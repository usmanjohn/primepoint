# -*- coding: utf-8 -*-
"""MO-4 — «Ulugʻbek bir yilning uzunligini qanday oʻlchagan»  MATEMATIKA OLAMI

Manba: _stories_matematika_olami_13_15.py, order 4.

Bu filmning dvigateli — KATTALIK. Sekstant nega qirq metr? Chunki yoy qancha
katta boʻlsa, bir gradusga toʻgʻri keladigan boʻlak shuncha uzun, uni esa
daqiqa va sekundlarga boʻlish mumkin. Kattalik — bu aniqlik degani edi.

Film ikki marta yopiladi: birinchi marta 1449-yilda (rasadxona vayron boʻladi),
ikkinchi marta 1908-yilda (Vyatkin uni yer ostidan topadi). Oxirgi qorongʻi
karta — oʻsha topilma.
"""

from spec import Video, Scene
from scenes import era, portrait, fact, versus, check, rule, ask, outro
import primitives as P

why = Scene(
    9.6,
    P.line("nega bunchalik katta?", "lbl", at=0.0, anim="fade")
    + P.card(P.card_expr("yoy katta  →  bir gradus uzun  →  boʻlish mumkin"),
             at=0.7, cls="card--gold", dur=0.55)
    + P.line("Kattalik — bu aniqlik degani edi", "ttl grn",
             at=2.4, anim="pop", dur=0.7),
    cam="push", name="nega-katta",
    note="Yoyning radiusi qancha katta boʻlsa, bir gradusga toʻgʻri keladigan "
         "masofa shuncha uzun. Uzun boʻlakni daqiqa va sekundlarga boʻlish mumkin.")

VIDEO = Video(
    slug="mo04",
    lesson="Matematika olami",
    title="Ulugʻbek bir yilning uzunligini qanday oʻlchagan",
    story="Matematika olami — order 4",
    scenes=[
        fact("365", "kun — taxminiy javob",
             cap="Aniq javob uchun butun boshli rasadxona kerak.",
             dur=6.6, cam="push",
             note="Ochilish: hamma biladigan son — va u taxminiy."),

        era("Samarqand", "1424", "Mirzo Ulugʻbek rasadxona qurishni boshladi",
            dur=6.4),

        portrait("Ulugʻbek", name="Mirzo Ulugʻbek",
                 dates="1394 — 1449",
                 caption="Amir Temurning nabirasi",
                 dur=7.2,
                 note="Rasadxonaga butun mintaqadan olimlar toʻplandi."),

        fact("40", "metr — Fahriy sekstantining radiusi",
             cap="Yer ustiga emas, maxsus qazilgan xandaqqa qurilgan.",
             dur=7.0,
             note="Bunday balandlikdagi asbobni shamol qimirlatib yuborardi."),

        why,

        fact("1018", "yulduzning oʻrni yozilgan",
             cap="«Ziji jadidi Koʻragoniy» — ikki asr davomida dunyodagi eng aniq jadval.",
             dur=7.2, dark=True,
             note="Oʻn yillar davomida osmonni kuzatishdi."),

        versus({"name": "Ulugʻbek oʻlchagan", "qty": "10 daq 8 sek",
                "price": "365 kun 6 soatdan ortiq", "tag": "1440-yillar",
                "cls": "win"},
               {"name": "hozirgi qiymat", "qty": "9 daq 10 sek",
                "price": "365 kun 6 soatdan ortiq", "tag": "bugun", "cls": "win"},
               title="Yulduz yilining uzunligi",
               unit_label="sekundlarga keltiramiz",
               verdict="608 va 550 sekund.", dur=10.5,
               note="Farqni koʻrish uchun ikkalasini bir xil birlikka keltiramiz."),

        check("608 − 550 = 58",
              parts=["10 daqiqa 8 sekund = 608 sekund", "9 daqiqa 10 sekund = 550 sekund"],
              verdict="Butun bir yilda — bir daqiqadan kam xatolik.",
              title="Farqni hisoblaymiz", dur=8.6,
              note="Teleskop hali ixtiro qilinmagan edi."),

        era("Samarqand", "1908", "Arxeolog Vyatkin sekstantni yer ostidan topdi",
            dur=6.8,
            note="Rasadxona vayron boʻlgan, oʻrni ham unutilgan edi. "
                 "Sekstantning saqlanib qolgan qismi bugun ham oʻsha yerda turibdi."),

        rule("Bor-yoʻgʻi bitta ulkan yoy, koʻp yillik sabr va yaxshi matematika",
             strip="kattalik  →  aniqlik",
             meaning="Teleskopsiz olingan jadval ikki asr davomida dunyoda eng aniqi boʻlib qoldi.",
             head="Nima qoldi", dur=9.6,
             note="Filmning oxirgi gapi."),

        ask("Sekstant ikki barobar katta boʻlganda, aniqlik qanday oʻzgarardi?",
            dur=7.0, note="Javobni aytmang."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Bir yil necha kun davom etadi? *365* degan javob taxminiy. "
    "|| Aniq javob uchun butun boshli rasadxona kerak.",

    "Samarqand, 1424-yil. | Mirzo Ulugʻbek shu yerda rasadxona qurishni "
    "boshladi.",

    "U Amir Temurning nabirasi edi.",

    "Asosiy asbobi — *Fahriy sekstanti*: radiusi 40 metrga yaqin ulkan yoy. "
    "| Xandaqqa qurilgan, chunki uni shamol qimirlatardi.",

    "Nega bunchalik katta? || Yoy qancha katta boʻlsa, bir gradusga toʻgʻri "
    "keladigan boʻlak shuncha uzun. | *Kattalik — bu aniqlik degani edi.*",

    "Oʻn yillar osmonni kuzatishdi. 1018 ta yulduz yozilgan katalog tuzildi. "
    "|| Ikki asr dunyodagi eng aniq jadval boʻlib qoldi.",

    "Endi yulduz yili. Ulugʻbek uni 365 kun 6 soat 10 daqiqa 8 sekund deb "
    "oʻlchagan. | Bugungi qiymat — 9 daqiqa 10 sekund.",

    "Sekundlarga keltiramiz: 608 va 550. Ayirma — *58 sekund*. || Butun bir "
    "yilda bir daqiqadan kam xatolik.",

    "Rasadxona vayron boʻldi, oʻrni unutildi. | Faqat 1908-yilda arxeolog "
    "Vyatkin uning yer ostidagi qismini topdi.",

    "Teleskop yoʻq edi. Bor-yoʻgʻi bitta ulkan yoy, koʻp yillik sabr va "
    "yaxshi matematika.",

    "Endi oʻzingiz oʻylang. Sekstant ikki barobar katta boʻlganda, aniqlik "
    "qanday oʻzgarardi? || Izohda kutamiz.",

    None,   # outro — jim
])
