# -*- coding: utf-8 -*-
"""MO-27 — «Gazetadagi diagrammaga nega ishonmaslik kerak»  MATEMATIKA OLAMI

Manba: Matematika olami, order 27.

The only film on this shelf whose subject is a LIE, which makes it the only one
where the kit has to be able to tell one. `P.bars(base=...)` was added for it:
the same two numbers, 48 and 52, drawn twice.

    base = 0    ->  the bars stand 1.08 to 1
    base = 45   ->  the bars stand 2.33 to 1

Nothing about the data changed. That ratio is manufactured entirely by where
the axis begins, and a viewer who has watched it happen once will never look at
a bar chart the same way again -- which is the whole point of putting it on a
shelf people read for pleasure.

The film is careful to blame the CHART and not the numbers: 48 and 52 are true
in both pictures, and the narration says so. A film that cried "statistics
lie" would teach cynicism; this one teaches where to look.
"""

from spec import Video, narrate, Scene
from scenes import cover, beat, check, rule, ask, outro
import primitives as P

_lie, ls = P.bars([(48, "A mahsulot", ""), (52, "B mahsulot", "win")],
                  at=0.7, step=1.0, base=45)
lie = Scene(
    9.0,
    P.line("Reklamadagi diagramma", "lbl lbl--sm", at=0.0, anim="fade")
    + _lie
    + P.line("«Ikki baravar koʻp tanlanadi»", "ttl", at=0.7 + ls, anim="pop", dur=0.6),
    cam="push", top=True, name="yolgʻon",
    note="Oʻqning boshi 45 da. Hech kim buni yozmaydi, va hech kim "
         "soʻramaydi.")

_true, ts = P.bars([(48, "A mahsulot", ""), (52, "B mahsulot", "win")],
                   at=0.7, step=1.0, base=0)
true = Scene(
    9.4,
    P.line("Oʻq noldan boshlansa", "lbl lbl--sm", at=0.0, anim="fade")
    + _true
    + P.line("Bir xil ikkita son, boshqa surat", "ttl grn",
             at=0.7 + ts, anim="pop", dur=0.6),
    cam="push", top=True, name="haqiqat",
    note="AYNI OʻSHA ikkita son. Faqat oʻqning boshi oʻzgardi.")

# `.solve__r` is pushed right with margin-left:auto inside a 900px row, so the
# two columns share one budget -- a long LEFT column silently squeezes the right
# one off the frame. Both stay short.
_how, hs = P.solve([
    ("Oʻqning boshi", "noldan boshlanadimi?"),
    ("Sonlar",        "chizmada yozilganmi?"),
    ("52 − 48",       "farqni oʻzingiz ayiring"),
], at=0.7, step=1.5)

how = Scene(
    9.6,
    P.line("Uchta savol — uch soniya", "lbl lbl--sm", at=0.0, anim="fade") + _how,
    cam="sink", top=True, name="uchta savol",
    note="Amaliy qism: tomoshabin ertaga koʻchada shu uchta savolni "
         "beradi.")

VIDEO = Video(
    slug="mo27",
    lesson="Matematika olami",
    title="Gazetadagi diagrammaga nega ishonmaslik kerak",
    story="Matematika olami — order 27",
    subject="math",
    scenes=[
        cover("52 va 48", "Farq — atigi 4",
              kicker="Matematika olami",
              context="Diagrammada bittasi ikki baravar katta:",
              strike=False,
              note="MUQOVA: ikkita zararsiz son, va ular orasidagi haqiqiy "
                   "farq. Tomoshabin «ikki baravar» qayerdan chiqqanini "
                   "bilmaguncha keta olmaydi."),

        lie,

        beat(dur=4.2, n=3,
             note="ATAYLAB JIM. Tomoshabin suratga ishonib ulgursin — "
                  "keyin oʻsha ishonch olib qoʻyiladi."),

        true,

        check("52 − 48 = 4",
              parts=["Ikkala diagrammada ham sonlar bir xil",
                     "Oʻzgargani — oʻqning boshlanishi"],
              verdict="Yolgʻon sonlarda emas, suratda",
              title="Sonlarni solishtiramiz",
              dur=8.6,
              note="Muhim nuqta: sonlar rost. Aldaydigan narsa — chizma."),

        how,

        rule("Diagrammaga qarasangiz, avval oʻqning boshini toping",
             strip="oʻq noldan boshlanmasa — nisbat yasalgan",
             meaning="Diagramma sonlarni koʻrsatish uchun emas, ularni "
                     "TUSHUNTIRISH uchun chiziladi. Shuning uchun uni "
                     "chizgan odamning niyati doim rasmning ichida turadi.",
             dur=9.6),

        ask("Reklama «ikki baravar tez» deydi, lekin diagramma yoʻq. "
            "Nimani soʻraysiz?",
            dur=7.4,
            note="Javobni aytmang. Uchta savoldan biri bu yerda ham ishlaydi."),

        outro(),
    ],
)

narrate(VIDEO, [
    "Ikkita son: 48 va 52. || Diagrammada bittasi ikki baravar katta "
    "koʻrinadi. | Ammo ular orasidagi farq — atigi 4.",

    "Reklamada shunday diagramma chiqdi. | Oʻng ustun chapdan ikki baravar "
    "balandroq. || «Bizning mahsulot ikki baravar koʻp tanlanadi.»",

    None,   # beat — jim sahna, tomoshabin suratga ishonadi

    "Endi xuddi oʻsha ikkita sonni qaytadan chizamiz. | Bu safar oʻq noldan "
    "boshlanadi. || Ustunlar deyarli bir xil.",

    "Sonlar oʻzgarmadi. 48 — 48 boʻlib qoldi, 52 — 52. | Ayirsak, farq "
    "toʻrtta. || Oʻzgargan narsa bitta: oʻqning qayerdan boshlangani.",

    "Shuning uchun diagrammaga qaraganda uchta savol bering. | Oʻq "
    "qayerdan boshlanadi? | Sonlar yozilganmi? || Va farqni oʻzingiz "
    "ayiring.",

    "Diagramma sonlarni koʻrsatish uchun emas, ularni tushuntirish uchun "
    "chiziladi. || Shuning uchun uni chizgan odamning niyati doim rasmning "
    "ichida turadi.",

    "Endi oʻzingiz oʻylang. Reklama «ikki baravar tez» deydi, lekin "
    "diagramma yoʻq. || Nimani soʻraysiz? Izohda kutamiz.",

    None,   # outro — jim
])
