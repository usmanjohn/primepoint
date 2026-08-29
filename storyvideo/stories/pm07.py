# -*- coding: utf-8 -*-
"""PM-7 — «Tub sonlar sirni qanday saqlaydi»   SHAKL: KASHFIYOT

Manba: _stories_prime_math_07_09.py, order 7.

Bu videoning dvigateli — bitta kichik xato va uning ulkan oqibati. Sherbek 91 ni
tub son deb ataydi; Afsona bitta savol bilan uni agʻdaradi. Keyin xuddi shu
qiyinchilik — koʻpaytirish oson, ajratish qiyin — butun internetni ushlab
turadigan narsa boʻlib chiqadi.

Videoning eng muhim kadri — «vs» sahnasi: bir xil ikki son, ikki tomonga
yurilganda butunlay boshqa qiyinlik.
"""

from spec import Video, Scene
from scenes import hook, says, beat, correct, versus, rule, ask, outro
import primitives as P

big = Scene(
    9.8,
    P.line("endi har biri 100 xonali ikkita tub son", "lbl", at=0.0, anim="rise")
    + P.expr("koʻpaytirish — hamon bir zum", at=0.8, anim="pop", dur=0.6)
    + P.line("ajratish", "lbl lbl--sm", at=3.0, anim="fade")
    + P.line("dunyodagi eng kuchli kompyuter ham ulgurmaydi", "ttl red",
             at=3.7, anim="pop", dur=0.7)
    + P.card(P.card_expr("ochiq kalit — koʻpaytma · maxfiy kalit — ikki tub son"),
             at=6.0, cls="card--gold", dur=0.55),
    cam="push", name="bigprimes",
    note="Sonlar kattalashsa, ikki tomon orasidagi farq portlaydi. Telefoningiz "
         "bankka ulanganda aynan shu farqqa tayanadi.")

VIDEO = Video(
    slug="pm07",
    lesson="PM-7",
    title="Tub sonlar sirni qanday saqlaydi",
    story="Prime Math Readings — order 7",
    scenes=[
        hook("91", "tub sonmi?", "7 × 13", "yoki shu", "Internet shu savolga tayanadi.",
             dur=5.2),

        says("Sherbek", [("91 — tub son", "expr"),
                         ("2 ga ham, 3 ga ham,", "lbl"),
                         ("5 ga ham boʻlinmaydi", "ask")],
             dur=6.6, size=250,
             note="Sherbek doskaga 91 deb yozdi va uni tub son deb atadi."),

        beat(4.2, note="Jim turing. Siz nimani sinab koʻrardingiz?"),

        says("Afsona", [("Yettiga", "lbl"),
                        ("urinib koʻrdingmi?", "expr gold")],
             dur=6.0, size=250, mood="think",
             note="Afsona bitta savol berdi — va shu savol hammasini agʻdardi."),

        correct("tub", "murakkab", "91 ÷ 7 = 13", lead="91 = 7 × 13", dur=8.4,
                note="91 tub emas ekan. Yetti va oʻn uch — mana ular."),

        versus({"name": "koʻpaytirish", "qty": "7 × 13", "price": "bir soniya",
                "tag": "OSON", "cls": "win", "claim": "7 × 13 = 91"},
               {"name": "ajratish", "qty": "91 = ? × ?",
                "price": "2, 3, 5, 7… sinash",
                "tag": "QIYIN", "cls": "lose"},
               title="Bir xil ikki son, ikki yoʻl",
               unit_label="qaysi tomonga yurishingizga bogʻliq",
               verdict="Teskari yoʻl har doim ogʻirroq.", dur=10.5,
               note="Koʻpaytirish bir soniya. Teskarisi — sinab koʻrish."),

        big,

        rule("Koʻpaytirish oson, ajratish qiyin",
             strip="katta koʻpaytma ochiq · ikki tub son yashirin",
             meaning="Ikki ming yil oldin qiziqish uchun oʻrganilgan tub sonlar bugun har kuni milliardlab marta ishlatiladi.",
             dur=9.6,
             note="Eratosfen gʻalvir tuzganda buni bilmagan edi."),

        ask("91 ni sinaganda nega 10 dan katta sonlarni tekshirish shart emas?",
            dur=7.0, note="Javobni aytmang — ildiz haqida oʻylashsin."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Sherbek doskaga 91 deb yozdi va uni tub son deb atadi. "
    "|| Rostdan ham shundaymi?",

    "Ikkiga boʻlinmaydi. Uchga ham, beshga ham boʻlinmaydi. "
    "| Demak tub son, degan xulosa chiqardi.",

    "Bir soniya oʻylab koʻring. || Siz yana nimani sinab koʻrardingiz?",

    "Afsona bitta savol berdi: *yettiga urinib koʻrdingmi*?",

    "91 ni yettiga boʻlamiz — 13 chiqadi. | Demak 91 tub emas, *murakkab son*: "
    "yetti karra oʻn uch.",

    "Endi eng qizigʻi. Yetti va oʻn uchni koʻpaytirish uchun bir soniya kerak. "
    "| Teskari yoʻl esa — 91 ni koʻrib turib undan yetti bilan oʻn uchni topish — "
    "sinab koʻrishni talab qiladi. || Bir xil ikki son, ikki xil qiyinlik.",

    "Endi tasavvur qiling: har biri *100 xonali* ikkita tub son. Ularni "
    "koʻpaytirish kompyuter uchun hamon bir zumlik ish. | Ajratish esa shunchalik "
    "ogʻirki, dunyodagi eng kuchli kompyuterlar ham uddalay olmaydi.",

    "Esda tutinglar. || Telefoningiz bankka ulanganda aynan shu qoidadan "
    "foydalanadi. Katta koʻpaytma hammaga ochiq, uni hosil qilgan ikkita tub son "
    "esa yashirin qoladi.",

    "Endi oʻzingiz oʻylang. 91 ni sinab koʻrayotganda nega 10 dan katta sonlarni "
    "tekshirish shart emas? || Izohda kutamiz.",

    None,   # outro — jim
])
