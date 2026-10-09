# -*- coding: utf-8 -*-
"""MO-23 — «Nega lyuk qopqogʻi dumaloq»   MATEMATIKA OLAMI · kundalik hayot

Manba: Matematika olami, order 23.

The famous interview question, answered with a picture: a square lid has one
width that is longer than its hole (the diagonal), a round lid has none. The
film draws the square's diagonal in red and then the circle's four diameters,
all labelled the same -- "constant width" is watched, not stated.

Arithmetic (and the gate recomputes the check line):
    60 × 60 + 60 × 60 = 7 200,  √7 200 ≈ 84,85  ->  ≈ 85 sm  >  60 sm
"""

from spec import Video, narrate, Scene
from scenes import cover, beat, check, fact, rule, ask, practice, outro
import primitives as P

_sq, sq_s = P.widths("square", 60, 85, at=0.6, step=1.6, w=380)
square = Scene(
    8.4,
    P.line("Kvadrat qopqoq, tomoni 60 sm", "lbl lbl--sm", at=0.0, anim="fade")
    + _sq
    + P.line("85 &gt; 60 — tushadi!", "ttl red", at=0.6 + sq_s + 0.4,
             anim="pop", dur=0.6),
    cam="push", top=True, name="kvadrat",
    note="Qizil chiziq — diagonal. Teshikdan uzun yagona «en».")

_ci, ci_s = P.widths("circle", 60, at=0.6, step=0.9, w=380)
circle = Scene(
    8.6,
    P.line("Doira: istalgan tomondan oʻlchang", "lbl lbl--sm", at=0.0, anim="fade")
    + _ci
    + P.line("Hamma «en» bir xil", "ttl grn", at=0.6 + ci_s + 0.3,
             anim="pop", dur=0.6),
    cam="push", top=True, name="doira",
    note="Toʻrtta diametr, hammasi 60 sm. Zaif joy yoʻq.")

_why, ws = P.solve([
    ("Burchak yoʻq", "istalgan tomonga qoʻyib yopiladi"),
    ("Dumalaydi",    "ogʻir temirni koʻtarmay siljitsa boʻladi"),
], at=0.7, step=1.4)
more = Scene(
    8.0,
    P.line("Yana ikki foyda", "lbl lbl--sm", at=0.0, anim="fade") + _why,
    cam="sink", top=True, name="yana ikki foyda",
    note="Ishchi uchun qulaylik — geometriyaning ikkinchi sovgʻasi.")

VIDEO = Video(
    slug="mo23",
    lesson="Matematika olami",
    title="Nega lyuk qopqogʻi dumaloq",
    story="Matematika olami — order 23",
    subject="math",
    scenes=[
        cover("Kvadrat", "Tushib ketadi",
              kicker="Matematika olami",
              context="Nega lyuk qopqogʻi hech qachon kvadrat emas?",
              note="MUQOVA: kvadrat qopqoq chizilgan — u xavfli. "
                   "Vaʼda: u quduqqa tushib ketadi."),

        fact("60 sm", "kvadrat qopqoqning tomoni",
             cap="Ishchi uni koʻtardi va qaytarib yopmoqchi. Sal qiyshaytirsa-chi?",
             dur=6.4, cam="pull"),

        beat(dur=4.0, n=3,
             note="ATAYLAB JIM. Tomoshabin oʻzi oʻylasin: nima boʻladi?"),

        square,

        check("60 × 60 + 60 × 60 = 7 200",
              parts=["Pifagor: diagonal = √7 200 ≈ 85 sm",
                     "Teshikning eni esa — 60 sm"],
              verdict="Kvadrat qopqoq quduqqa tushadi",
              title="Pifagor bilan tekshiramiz",
              dur=8.4),

        circle,

        fact("Doimiy kenglik", "matematiklar shunday ataydi",
             cap="Qanday burang, qanday qiyshaytiring — doira oʻz teshigidan oʻtmaydi.",
             dur=7.0, cam="push"),

        more,

        rule("Shaklning geometriyasi — amaliy natija",
             strip="kvadrat: 85 &gt; 60  ·  doira: 60 = 60",
             meaning="Bu savolni bir paytlar ish suhbatlarida berishgan. "
                     "Kutilgani — tayyor javob emas, fikrlash yoʻli edi.",
             dur=9.0),

        ask("Doiradan boshqa shakl ham oʻz teshigiga tushmasligi mumkinmi?",
            dur=7.0,
            note="Javobni aytmang: Reulo uchburchagi. Izohlarda chiqadi."),

        practice("Burchak · Matematika olami",
                 sub="powerty.uz → Burchak → Matematika olami",
                 dur=5.2),

        outro(),
    ],
)

narrate(VIDEO, [
    "Lyuk qopqoqlari deyarli har doim dumaloq. || Bu tasodif emas.",

    "Qopqoq kvadrat boʻlsin, tomoni 60 santimetr. "
    "|| Ishchi uni sal qiyshaytirsa nima boʻladi?",

    None,   # beat

    "Kvadratning diagonali tomondan uzun. | Taxminan 85 santimetr. "
    "|| Teshikning eni esa atigi oltmish.",

    "Pifagor teoremasi buni tasdiqlaydi. "
    "|| Qiyshaygan kvadrat qopqoq quduqqa tushib ketadi. [gasps]",

    "Doirada bunday zaif joy yoʻq. "
    "|| Uning eni qaysi tomondan oʻlchasangiz ham bir xil.",

    "Matematiklar buni doimiy kenglikdagi shakl deydi. "
    "|| Dumaloq qopqoq oʻz teshigidan hech qachon oʻtmaydi.",

    "Yana ikki foyda bor. | Burchakma-burchak toʻgʻrilash shart emas. "
    "|| Ogʻir temirni dumalatib olib borsa boʻladi.",

    "Bu savolni bir paytlar ish suhbatlarida berishgan. "
    "|| Kutilgani — tayyor javob emas, fikrlash yoʻli.",

    "Endi oʻylang, aqllilar: | doiradan boshqa shunday shakl bormi? "
    "|| Izohda kutamiz.",

    "Bunday hikoyalar — Powertyda, Burchak boʻlimida.",

    None,   # outro
])
