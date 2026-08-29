# -*- coding: utf-8 -*-
"""MO-3 — «Beruniy Yerni bir togʻdan turib oʻlchagan»   MATEMATIKA OLAMI · tarixiy

Manba: _stories_matematika_olami_09.py, order 3.

Bu filmning dvigateli — nisbat. Bir odam, bitta togʻ, bitta burchak oʻlchagich —
va Yerning radiusi. Shuning uchun markazda ufqning ogʻishi turadi: u bir
gradusdan ham kichik, va aynan shu kichkina son butun sayyorani oʻlchaydi.

Oxiri maqtov emas, TEKSHIRUV: 31 kilometr farq — yarim foizdan kam.
"""

from spec import Video, Scene
from scenes import era, portrait, fact, versus, check, rule, ask, outro
import primitives as P

_steps, ss = P.solve([
    ("1-qadam", "togʻning balandligi — ikki joydan burchak oʻlchash"),
    ("2-qadam", "choʻqqiga chiqib ufqqa qarash"),
    ("ogʻish", "bir gradusdan ham kichik burchak"),
    ("radius", "shu ikki sondan hisoblanadi"),
], at=0.6, step=1.6)

method = Scene(
    11.0,
    P.counters(P.counter(4, "qadam", at=0.6, dur=ss, counts=".solve__row"))
    + _steps,
    cam="sink", top=True, name="usul", counts=[4],
    note="Eski usul katta sahro va koʻp odam talab qilardi. Beruniy undan voz "
         "kechdi va ikki qadamli yoʻl oʻyladi.")

VIDEO = Video(
    slug="mo03",
    lesson="Matematika olami",
    title="Beruniy Yerni bir togʻdan turib oʻlchagan",
    story="Matematika olami — order 3",
    scenes=[
        fact("6371", "kilometr — Yerning radiusi",
             cap="Buni kosmik kemasiz qanday bilish mumkin?", dur=6.6, cam="push",
             note="Ochilish: hamma biladigan son, lekin uni qanday oʻlchagan?"),

        era("Kat, Xorazm", "973", "Abu Rayhon Beruniy shu yerda tugʻilgan", dur=6.4),

        portrait("Beruniy", name="Abu Rayhon Beruniy",
                 dates="973 — 1048",
                 caption="Astronomiya, geografiya, tarix va matematika",
                 dur=7.4,
                 note="Yer radiusini oʻlchash gʻoyasi uni yoshligidan qiziqtirgan."),

        # Rad etilgan usul — filmning «toʻsigʻi».
        fact("2", "shahar, katta sahro, koʻp odam",
             cap="Eski usul shuni talab qilardi. Beruniy undan voz kechdi.",
             dur=6.6, dark=True,
             note="Ikki shahar orasidagi masofani oʻlchab, quyosh balandligini "
                  "taqqoslash — ogʻir va qimmat yoʻl."),

        method,

        fact("1°", "dan ham kichik",
             cap="Yer yassi boʻlganida ufq roppa-rosa koʻz balandligida turardi.",
             dur=7.0,
             note="Yer sharsimon boʻlgani uchun ufq sal pastda koʻrinadi. "
                  "Filmning eng chiroyli gʻoyasi shu."),

        versus({"name": "Beruniy hisobi", "qty": "6340", "price": "kilometr",
                "tag": "≈1030-yil", "cls": "win"},
               {"name": "bugungi qiymat", "qty": "6371", "price": "kilometr",
                "tag": "bugun", "cls": "win"},
               title="Ming yildan keyin tekshiramiz",
               unit_label="farq — atigi 31 kilometr",
               verdict="Sunʼiy yoʻldoshsiz olingan son.", dur=10.5,
               note="Usulini «Al-Qonun al-Masʼudiy» kitobida yozib qoldirgan — "
                    "shuning uchun bu rivoyat emas, hujjat."),

        check("6371 − 6340 = 31",
              parts=["31 ni 6371 ga boʻlamiz", "≈ 0,005"],
              verdict="Yarim foizdan kam xatolik.", title="Xatolikni oʻlchaymiz",
              dur=8.4,
              note="Quruq «31 kilometr» soni shu boʻlishdan keyin bahoga aylanadi."),

        rule("Yaxshi matematika yetib boʻlmaydigan narsani oʻlchab beradi",
             strip="bitta togʻ · bitta burchak · koʻp sabr",
             meaning="Sunʼiy yoʻldoshsiz, kompyutersiz, hatto teleskopsiz.",
             head="Nima qoldi", dur=9.6,
             note="Filmning oxirgi gapi."),

        ask("Ufq nega pastda koʻrinadi — va togʻ balandroq boʻlsa, u qanday oʻzgaradi?",
            dur=7.0, note="Javobni aytmang."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Yerning radiusi — 6371 kilometr. || Buni bilish uchun nima kerak? "
    "Kosmik kema? Sunʼiy yoʻldosh?",

    "Kat shahri, Xorazm. 973-yil. | Abu Rayhon Beruniy shu yerda tugʻilgan.",

    "Astronomiya, geografiya, tarix va matematika. | Yer radiusini oʻlchash "
    "gʻoyasi uni yoshligidan qiziqtirgan.",

    "Avval eski usulni sinab koʻrdi: ikki shahar orasidagi masofani oʻlchash. "
    "| Bu katta sahro va koʻp odam talab qilardi. || Beruniy undan voz kechdi.",

    "Yangi usul ikki qadamdan iborat. Birinchisi — togʻning balandligi: unga "
    "ikki joydan qarab burchak oʻlchadi. | Ikkinchisi — eng chiroylisi.",

    "U choʻqqiga chiqdi va ufqqa qaradi. Yer yassi boʻlganida ufq roppa-rosa "
    "koʻz balandligida turardi. | Lekin Yer sharsimon — ufq sal pastda "
    "koʻrinadi. || Beruniy oʻsha ogʻishni oʻlchadi: bir gradusdan ham kichik.",

    "Shu ikki son yetdi. Uning javobi hozirgi oʻlchovlarda taxminan "
    "6340 kilometrga toʻgʻri keladi. | Bugungi qiymat esa 6371.",

    "Farqni oʻlchaymiz: 31 kilometr. Uni 6371 ga boʻlsak, || *yarim foizdan "
    "ham kam*.",

    "Sunʼiy yoʻldoshsiz, kompyutersiz, teleskopsiz. || Bitta togʻ va yaxshi "
    "oʻylangan usul. *Yaxshi matematika yetib boʻlmaydigan narsani oʻlchab "
    "beradi.*",

    "Endi oʻzingiz oʻylang. Togʻ balandroq boʻlsa, ufqning ogʻishi qanday "
    "oʻzgaradi? || Izohda kutamiz.",

    None,   # outro — jim
])
