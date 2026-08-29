# -*- coding: utf-8 -*-
"""PM-90 — «Ikki usta, bitta devor»  (birgalikdagi ish)   SHAKL: TUTILGAN XATO

Manba: _stories_prime_math_88_90.py, order 90.

Bu videoning dvigateli — bitta savol: «demak sen kelsang ish sekinlashadimi?»
Oʻrtachalash xatosini rad etish uchun hisob shart emas — 12,5 kun 10 kundan
katta, va buni har kim koʻradi. Hisob keyin, javobni topish uchun keladi.
"""

from spec import Video, Scene
from scenes import hook, says, beat, consequence, correct, check, rule, ask, outro
import primitives as P

_ladder, ls = P.solve([
    ("butun devor = 1", "ishni bir deb olamiz"),
    ("Karim aka: 1/10", "bir kunlik ulushi"),
    ("Bekzod: 1/15", "bir kunlik ulushi"),
    ("3/30 + 2/30 = 5/30", "umumiy maxraj — 30"),
    ("5/30 = 1/6", "birga bir kunda shuncha"),
], at=0.6, step=1.5)

ladder = Scene(
    11.5,
    P.counters(P.counter(5, "qadam", at=0.6, dur=ls, counts=".solve__row"))
    + _ladder,
    cam="sink", top=True, name="ladder", counts=[5],
    note="Vaqtlarni qoʻshib ham, oʻrtachalab ham boʻlmaydi. Bir kunda kim "
         "qanchasini qilishini sanaymiz.")

VIDEO = Video(
    slug="pm90",
    lesson="PM-90",
    title="Ikki usta, bitta devor",
    story="Prime Math Readings — order 90",
    scenes=[
        hook("10", "kun — Karim aka", "15", "kun — Bekzod",
             "Birga qancha vaqt ketadi?", dur=5.0),

        says("Bekzod", [("Oʻn va oʻn besh…", "lbl"),
                        ("oʻrtachasi 12,5 kun", "expr"),
                        ("Shundaymi?", "ask")],
             dur=6.8, size=250,
             note="Bekzod bir zum oʻyladi va vaqtlarni oʻrtachaladi."),

        beat(4.2, note="Shu yerda toʻxtang. Bu javob toʻgʻri boʻlishi mumkinmi?"),

        consequence("Bekzod", "demak yordam ishni sekinlashtiradimi?",
                    dur=7.4, mood="oh",
                    note="Karim aka kuldi: yolgʻiz oʻzi 10 kunda qurardi-ku."),

        ladder,

        correct("12,5", "6", "30 ÷ 5 = 6", lead="vaqt qoʻshilmaydi", dur=8.6,
                note="Bir kunda oltidan bir qism qilinsa, butun devorga olti kun."),

        check("0,6 + 0,4 = 1",
              parts=["Karim aka olti kunda 0,6 qismini", "Bekzod 0,4 qismini"],
              verdict="Roppa-rosa butun devor.", dur=8.2,
              note="Olti kunda ikkovi butun devorni bitiradi."),

        rule("Vaqt qoʻshilmaydi, unumdorlik qoʻshiladi",
             strip="bir kunlik ulush = 1 ÷ yolgʻiz bitirish vaqti",
             meaning="Birga ishlaganda bir kunlik ulushlar qoʻshiladi, vaqtlar emas.",
             dur=9.4,
             note="Bekzod daftariga shuni yozib qoʻydi."),

        ask("Uchinchi usta ham kelsa va u yolgʻiz 30 kunda bitirsa — uchovi qancha vaqtda?",
            dur=7.0, note="Javobni aytmang. Xuddi shu usul bilan topsin."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Karim aka devorni yolgʻiz 10 kunda quradi. Shogirdi Bekzod esa 15 kunda. "
    "|| Birga qurishsa, qancha vaqt ketadi?",

    "Bekzod bir zum oʻyladi. Oʻn va oʻn besh — oʻrtachasi 12 yarim kun.",

    "Shu yerda toʻxtang. || Bu javob toʻgʻri boʻlishi mumkinmi?",

    "Karim aka kuldi. || Demak sen kelganingdan keyin ish *sekinlashadimi*? "
    "Yolgʻiz oʻzim 10 kunda qurardim-ku.",

    "Sherbek daftar bilan chiqdi. Vaqtlarni qoʻshib ham, oʻrtachalab ham "
    "boʻlmaydi — bir kunda kim qanchasini qilishini sanash kerak. "
    "| Butun devorni bir deb olamiz. Karim aka bir kunda oʻndan bir qismini "
    "quradi, Bekzod oʻn beshdan bir qismini. || Birga ishlaganda ulushlar "
    "qoʻshiladi: oltidan bir qism.",

    "Javob 12 yarim emas. || Bir kunda oltidan bir qism qilinsa, butun "
    "devorga *olti kun* kerak.",

    "Tekshiramiz. Olti kunda Karim aka devorning 0,6 qismini quradi, "
    "Bekzod 0,4 qismini. | Yigʻindisi 1 — roppa-rosa butun devor.",

    "Esda tutinglar. || *Vaqt qoʻshilmaydi, unumdorlik qoʻshiladi.* "
    "Har kimning bir kunlik ulushi — butun ishni yolgʻiz bitirish vaqtiga "
    "boʻlish bilan topiladi.",

    "Endi oʻzingiz oʻylang. Uchinchi usta ham kelsa va u yolgʻiz 30 kunda "
    "bitirsa, uchovi necha kunda bitiradi? || Izohda kutamiz.",

    None,   # outro — jim
])
