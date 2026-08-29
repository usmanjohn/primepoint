# -*- coding: utf-8 -*-
"""MO-1 — «Algoritm soʻzi qayerdan kelgan»   MATEMATIKA OLAMI · tarixiy

Manba: _stories_matematika_olami_01_03.py, order 1.

Bu film dars emas. Shuning uchun yoʻlni xatodan emas, SOʻZDAN boshlaymiz:
tomoshabin har kuni koʻradigan «algoritm» soʻzi ekranda turadi va uning ostidan
oʻn ikki asr chiqadi.

Kompozitsiya doiraviy: birinchi kadr — telefon ekranidagi soʻz, oxirgi kadr —
oʻsha soʻz, endi ismga aylangan. Oraligʻida ikkita qorongʻi «bob» kartasi turadi.
"""

from spec import Video
from scenes import era, portrait, fact, versus, rule, ask, outro, Scene
import primitives as P

_words, ws = P.solve([
    ("al-jabr", "→ algebra — butun bir fanning nomi"),
    ("Algoritmi", "→ algoritm — aniq qadamlar ketma-ketligi"),
], at=0.6, step=2.0)

words = Scene(
    9.4,
    P.line("kitob nomidan qolgan ikki soʻz", "lbl lbl--sm", at=0.0, anim="fade")
    + _words
    + P.line("biri — fan, ikkinchisi — olimning ismi", "ttl grn",
             at=0.6 + ws + 0.6, anim="pop", dur=0.7),
    cam="sink", top=True, name="words",
    note="Kitob nomida ikkita amal bor edi. Birinchisi fan nomiga aylandi, "
         "ikkinchisi esa olimning oʻz ismidan qoldi.")

VIDEO = Video(
    slug="mo01",
    lesson="Matematika olami",
    title="Algoritm soʻzi qayerdan kelgan",
    story="Matematika olami — order 1",
    scenes=[
        fact("algoritm", "telefoningiz har kuni koʻrsatadigan soʻz",
             cap="U IT sohasidan kelmagan.", dur=6.4, cam="push",
             note="Ochilish: hamma biladigan soʻz. Keyin uning tagi ochiladi."),

        era("Xorazm", "≈780", "Muhammad ibn Muso al-Xorazmiy shu yerda tugʻilgan",
            dur=6.4),

        portrait("Al-Xorazmiy", name="Al-Xorazmiy",
                 dates="≈780 — ≈850",
                 caption="Umrining katta qismi Bagʻdodda, «Donishmandlik uyi»da oʻtgan",
                 dur=7.6,
                 note="Bayt ul-hikma: butun dunyodan kelgan kitoblar tarjima "
                      "qilinar, olimlar oʻz asarlarini yozar edi."),

        era("Bagʻdod", "≈820", "U bir kitob yozdi — nomida ikkita amal bor edi",
            dur=6.4),

        words,

        # Nega bu muhim: raqamlar tizimi.
        # Qisqa matn ataylab: compare bloki balandlashsa, sahna markazlashgani
        # uchun sarlavha yuqoriga siljiydi va PIP doirasiga tushib qoladi.
        versus({"name": "rim raqamlari", "qty": "MCMXLVIII",
                "price": "qoʻshish qiyin", "tag": "ogʻir", "cls": "lose"},
               {"name": "hind raqamlari", "qty": "1948",
                "price": "oʻnta raqam", "tag": "yengil", "cls": "win"},
               title="Uning ikkinchi kitobi", unit_label="bir xil son, ikki xil yozuv",
               verdict="Biz ikkinchisini ishlatamiz.", dur=10.5,
               note="Oʻsha paytda Yevropa rim raqamlari bilan hisoblardi."),

        fact("nol", "eng sokin, eng kuchli belgi",
             cap="Razryadli tizim aynan shu belgi bilan ishlaydi.",
             dur=6.8, dark=True,
             note="Nol boʻlmasa razryad ishlamaydi — 205 bilan 25 ni ajratib "
                  "boʻlmaydi."),

        rule("Bugun daftardagi son ham, telefondagi tavsiya ham — bitta ishning davomi",
             strip="al-jabr → algebra  ·  Algoritmi → algoritm",
             meaning="Oʻn ikki asr oldin Xorazmda tugʻilgan odamning ismi har kuni ekraningizda turadi.",
             head="Nima qoldi", dur=9.6,
             note="Doira yopiladi: film boshlangan soʻzga qaytamiz."),

        ask("Rim raqamlari bilan 1948 ni 12 ga boʻlishga urinib koʻring — nega qiyin?",
            dur=7.0, note="Javobni aytmang."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Telefoningiz qaysi videoni koʻrsatishni tanlaganda, ekranda *algoritm* "
    "degan soʻz paydo boʻladi. || Bu soʻz IT sohasidan kelmagan.",

    "Xorazm, taxminan 780-yil. | Muhammad ibn Muso al-Xorazmiy shu yerda "
    "tugʻilgan. Nomining oʻzi buni aytib turibdi.",

    "Umrining katta qismi Bagʻdodda, *Donishmandlik uyi*da oʻtdi. | U yerda "
    "butun dunyodan kelgan kitoblar tarjima qilinardi.",

    "Taxminan 820-yil. || U bir kitob yozdi, va uning nomida ikkita amal "
    "bor edi: al-jabr va al-muqobala.",

    "Birinchi soʻz butun bir fanning nomiga aylandi: *algebra*. | Ikkinchisi "
    "esa olimning ismidan qoldi: Yevropada uning nomi lotinchada *Algoritmi* "
    "deb yozilgan edi. || Keyin maʼnosi kengaydi — natijaga olib boradigan "
    "aniq qadamlar ketma-ketligi.",

    "Yana bir kitobi hind raqamlari haqida edi. Oʻshanda Yevropa rim "
    "raqamlari bilan hisoblardi — bunday yozuvda ustunda qoʻshish deyarli "
    "imkonsiz. || Biz bugun ishlatadigan razryadli tizim aynan shu kitoblar "
    "orqali tarqaldi.",

    "Uning ichida esa eng sokin va eng kuchli belgi bor edi: || *nol*.",

    "Bugun daftarda son yozganingizda ham, telefoningiz sizga video "
    "tanlaganda ham — || ikkalasining orqasida bitta xorazmlik olimning "
    "ishi turibdi.",

    "Endi oʻzingiz oʻylang. Rim raqamlari bilan boʻlish amalini bajarishga "
    "urinib koʻring — nega bunchalik qiyin? || Izohda kutamiz.",

    None,   # outro — jim
])
