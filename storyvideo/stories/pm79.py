# -*- coding: utf-8 -*-
"""PM-79 — «Oʻrtacha maosh qanday aldaydi»   SHAKL: TESKARI NATIJA

Manba: _stories_prime_math_79_81.py, order 79.

Bu videoning dvigateli — ustunlar. Sakkiztasi punktir chiziqdan pastda, bittasi
esa ekrandan chiqib ketgudek baland. Buni aytib berish shart emas: «oʻrtacha
rost, lekin sizga tegishli emas» degan gap koʻrinib turadi.

Hech kim yolgʻon gapirmaydi — videoning butun gapi shu. Aldov notoʻgʻri
tanlangan ROST sondan tugʻiladi.
"""

from spec import Video, Scene
from scenes import hook, says, beat, count_in, claim, consequence, correct, \
                   check, rule, ask, outro
import primitives as P

_bars, sb = P.bars(
    [(4, "", ""), (4, "", ""), (4, "", ""), (5, "", ""), (5, "", ""),
     (6, "", ""), (6, "", ""), (7, "", ""), (49, "direktor", "up")],
    ref=10, ref_label="oʻrtacha 10", at=0.5, step=0.62)

chart = Scene(
    11.5,
    _bars
    + P.line("toʻqqizdan sakkiztasi chiziqdan pastda", "lbl lbl--sm",
             at=0.5 + sb + 0.4, anim="fade")
    + P.line("bitta son hammasini yuqoriga tortdi", "ttl red",
             at=0.5 + sb + 1.0, anim="pop", dur=0.7),
    cam="push", name="chart",
    note="Maoshlar: 4, 4, 4, 5, 5, 6, 6, 7 va 49. Punktir chiziq — oʻrtacha "
         "10 million. Sakkiz ustun undan pastda.")

VIDEO = Video(
    slug="pm79",
    lesson="PM-79",
    title="Oʻrtacha maosh qanday aldaydi",
    story="Prime Math Readings — order 79",
    scenes=[
        hook("10", "million — oʻrtacha maosh", "?", "shuncha olamanmi",
             "Eʼlonni tekshiramiz.", dur=5.0),

        says("Jasur", [("Eʼlonda yozilgan:", "lbl"),
                       ("oʻrtacha maosh 10 million", "expr gold"),
                       ("Demak men ham shuncha olaman", "ask")],
             dur=6.8, size=250,
             note="Jasur ish eʼlonini oʻqidi va xursand boʻldi."),

        beat(4.2, note="Jim turing. Eʼlon yolgʻon gapiryaptimi?"),

        count_in(9, "xodim", size=104, per_row=5, dur=8.4,
                 note="Kichik korxona. U yerda toʻqqiz kishi ishlaydi."),

        claim("Jasur", "90 ÷ 9", "10", "Hisob toʻgʻri-ku?", dur=8.0,
              note="Maoshlar yigʻindisi 90 million. Toʻqqizga boʻlsak — 10."),

        chart,

        consequence("Jasur", "sakkiztasi oʻrtachadan kam oladi", dur=7.2, mood="oh",
                    note="Jasur ustunlarga qarab turib qoldi."),

        correct("10", "5", "saralab, oʻrtadagisini olamiz",
                lead="oʻrtacha emas — mediana", dur=8.6,
                note="Toʻqqizta son saralansa, beshinchisi oʻrtada turadi — 5 million."),

        check("4 + 4 + 4 + 5 + 5 + 6 + 6 + 7 + 49 = 90",
              parts=["yigʻindi 90, toʻqqiz kishi", "oʻrtacha 10 — rost son"],
              verdict="Yolgʻon yoʻq. Tanlov notoʻgʻri.", title="Hisob toʻgʻrimi?",
              dur=8.4,
              note="Hech kim yolgʻon yozmagan. Faqat notoʻgʻri oʻrtacha tanlangan."),

        rule("Qaysi oʻrtacha?",
             strip="oʻrtacha 10  ·  mediana 5  ·  moda 4",
             meaning="Uchalasi ham rost, lekin uch xil hikoya aytadi.",
             dur=9.4,
             note="Shuning uchun hisobotlarda oʻrtacha bilan birga mediana ham "
                  "beriladi."),

        ask("Direktorning maoshi 49 emas, 490 million boʻlsa — mediana oʻzgaradimi?",
            dur=7.0, note="Javobni aytmang. Oʻzlari oʻylab koʻrsin."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Ish eʼlonida shunday yozilgan: bizda oʻrtacha maosh 10 million soʻm. "
    "|| Bu rostmi?",

    "Jasur eʼlonni oʻqidi va xursand boʻldi. Oʻrtacha 10 million — demak u "
    "ham shuncha oladi.",

    "Bir soniya. || Eʼlon yolgʻon gapiryaptimi?",

    "Korxonaga kiramiz. Sanaymiz — bir, ikki, uch... | toʻqqiz nafar xodim "
    "ishlaydi.",

    "Maoshlar yigʻindisi 90 million. Toʻqqizga boʻlamiz — *10 million*. "
    "Hisob mutlaqo toʻgʻri.",

    "Endi maoshlarni yonma-yon qoʻyamiz. 4, 4, 4, 5, 5, 6, 6, 7 | va 49. "
    "Oxirgisi direktorniki. || Punktir chiziq — oʻrtacha. Sakkizta ustun "
    "undan pastda turibdi.",

    "Jasur diqqat qildi. || Toʻqqiz kishidan *sakkiztasi* oʻrtachadan kam oladi.",

    "Bitta juda katta son butun maʼlumotni yuqoriga tortib ketdi. Endi "
    "saralaymiz va roppa-rosa oʻrtadagisini olamiz — *5 million*. "
    "Bu son mediana deyiladi.",

    "Hisobni tekshiramiz. 4, 4, 4, 5, 5, 6, 6, 7 va 49 — yigʻindi 90. "
    "Toʻqqizga boʻlsak 10. | Yolgʻon yoʻq. Faqat notoʻgʻri oʻrtacha tanlangan.",

    "Esda tutinglar. || Oʻrtacha 10, mediana 5, moda 4. *Uchalasi ham rost.* "
    "Shuning uchun eʼlonni oʻqiganda soʻrang: qaysi oʻrtacha?",

    "Endi oʻzingiz oʻylang. Direktorning maoshi 49 emas, 490 million boʻlsa, "
    "mediana oʻzgaradimi? || Izohda kutamiz.",

    None,   # outro — jim
])
