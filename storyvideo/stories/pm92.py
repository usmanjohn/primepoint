# -*- coding: utf-8 -*-
"""PM-92 — «Katta paket haqiqatan arzonmi?»  (birlik narx)

Manba: corner/management/commands/_stories_prime_math_90_92.py, order 92.

Hikoyaning butun gapi: «tejamkor paket» yozuvi qoida emas, taxmin. Shuning uchun
videoning markazi — ikkita taqqoslash: birinchisida katta paket rost arzon
chiqadi, ikkinchisida esa qimmat. Ikkinchisi kutilmagan boʻlishi shart.
"""

from spec import Video
from scenes import hook, says, beat, versus, check, rule, outro

VIDEO = Video(
    slug="pm92",
    lesson="PM-92",
    title="Katta paket haqiqatan arzonmi?",
    story="Prime Math Readings — order 92",
    scenes=[
        hook("«Tejamkor", "paket»", "?", "haqiqatan arzonmi",
             "Ikki marta tekshiramiz.", dur=4.8),

        says("Afsona", [("Umumiy narxga qarab", "lbl"),
                        ("hukm chiqarib boʻlmaydi", "expr gold"),
                        ("paketlarda har xil miqdor bor", "ask")],
             dur=6.8, size=250, mood="think",
             note="Paketlarda har xil miqdor bor. Solishtirish uchun bir xil "
                  "oʻlchovga keltirish kerak — bir kilogrammga."),

        # 1-mahsulot: yozuv rost chiqadi.
        versus({"name": "kichik paket", "qty": "400 g", "price": "12 000 soʻm",
                "tag": "30 000<br><span class='cmp__k'>soʻm/kg</span>",
                "cls": "lose", "claim": "12 000 ÷ 0,4 = 30 000"},
               {"name": "katta paket", "qty": "1 kg", "price": "27 000 soʻm",
                "tag": "27 000<br><span class='cmp__k'>soʻm/kg</span>",
                "cls": "win", "claim": "27 000 ÷ 1 = 27 000"},
               title="Yogurt", unit_label="bir kilogrammga keltiramiz",
               verdict="Rost — katta paket arzon.", dur=10.5,
               note="Yogurt. 400 g — bu 0,4 kg. 12 000 ÷ 0,4 = 30 000. "
                    "Katta paket 27 000. Kilosiga 3 000 soʻm farq."),

        beat(4.0, note="Endi ikkinchisi. Xuddi shu yozuv turibdi. Rostmi?"),

        # 2-mahsulot: xuddi shu yozuv, teskari natija.
        versus({"name": "kichik paket", "qty": "600 g", "price": "21 000 soʻm",
                "tag": "35 000<br><span class='cmp__k'>soʻm/kg</span>",
                "cls": "win", "claim": "21 000 ÷ 0,6 = 35 000"},
               {"name": "katta paket", "qty": "3 kg", "price": "111 000 soʻm",
                "tag": "37 000<br><span class='cmp__k'>soʻm/kg</span>",
                "cls": "lose", "claim": "111 000 ÷ 3 = 37 000"},
               title="Yuvish kukuni", unit_label="xuddi shu yoʻl bilan",
               verdict="Katta paket 2 000 soʻm QIMMAT.", dur=11.0,
               note="Kukun. 21 000 ÷ 0,6 = 35 000. Katta paket 111 000 ÷ 3 = "
                    "37 000. Ustida esa oʻsha «tejamkor» yozuvi turardi."),

        check("111 000 ÷ 3 = 37 000",
              parts=["katta paketning umumiy narxi baland", "shuning uchun jiddiy koʻrinadi"],
              verdict="Yolgʻon emas — taassurot notoʻgʻri.",
              title="Nega shunday koʻrinadi?", dur=8.0,
              note="Hech kim «arzonroq» deb yozmagan. Umumiy narxi baland "
                   "boʻlgani uchun koʻzga foydali koʻrinadi."),

        rule("Katta paket arzon — bu qoida emas, taxmin",
             strip="birlik narx = qiymat ÷ miqdor",
             meaning="Har safar tekshiring. Buning uchun bitta boʻlish yetadi.",
             dur=9.2,
             note="Bir boʻlish — bir necha soniya, foydasi esa har oy takrorlanadi."),

        outro(),
    ],
)
