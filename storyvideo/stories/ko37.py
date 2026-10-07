# -*- coding: utf-8 -*-
"""KO-37 — «Devorning ham qulogʻi bor»  ·  BIR MAQOL, IKKI TIL  ·  속담 08

Manba: Burchak → 속담 이야기 (order 7) — 낮말은 새가 듣고 밤말은 쥐가 듣는다.
Oʻzbek egizagi va «nega qush va sichqon» izohi oʻsha hikoyaning oʻzidan:
eski koreys uyi yogʻoch va qogʻozdan, devori yupqa; hovlida qush, devor va
pol tagida sichqon.

Seriyaning sakkizinchisi. Arc oʻsha: vaziyat → gʻalati tasvir → tekislash →
egizak → qoida.

⛔ SERIES.md: hayvonlar tarjima EMAS. Bu safar oʻzbek egizagida hayvon umuman
yoʻq — quloqni DEVORNING OʻZIGA berganmiz; koreyslar esa devor ichida va
atrofida yashaydiganlarga. Filmda aynan shu aytiladi.

TIL DARSI: **은/는 = «esa»** (KO-29 «Men esa keldim» bilan bir oila).
낮말을 새가 듣는다 — oddiy xabar; 낮말은 새가 듣고 — qarama-qarshilik, va
tinglovchi ikkinchi yarmini kutadi. Maqolning ikki yarmini aynan shu ikki
은 bogʻlaydi.
"""

from spec import Video, narrate
from scenes import (cover, order, echo, pairs, rule, ask, practice, outro)

VIDEO = Video(
    slug="ko37",
    lesson="Burchak · 속담",
    title="Devorning ham qulogʻi bor",
    story="속담 이야기 — 낮말은 새가 듣고 밤말은 쥐가 듣는다",
    subject="korean",
    scenes=[
        cover("쥐가 듣는다", "Bizda — devor",
              kicker="Bir maqol, ikki til", ko="한국어",
              track="속담", n=8, badge="big",
              context="Koreys maqolida gapni sichqon eshitadi:",
              strike=False,
              note="MUQOVA: gʻalati narsa — gapni sichqon eshitadi. "
                   "Vaʼda ikki soʻz, juftlik."),

        order([("Kunduz", [("낮말은", "s"), ("새가", "o"),
                           ("듣고", "v")], True),
               ("Kecha", [("밤말은", "s"), ("쥐가", "o"),
                          ("듣는다", "v")], True),
               ("Soʻzma-soʻz", [("Kechasi gapni", "s"), ("sichqon", "o"),
                                ("eshitadi", "v")], False)],
              head="Bir maqol, ikki yarim",
              verdict="Kunduz — qush. Kecha — sichqon.",
              dur=12.5,
              note="Ikki koreys qatori bir xil qurilgan — bu keyin til "
                   "darsiga aylanadi."),

        echo("쥐가 듣는다", gloss="sichqon eshitadi",
             note="JIM sahna. Besh boʻgʻin — echo chegarasi ichida."),

        pairs([("새 — qush", "kunduzi hovlida"),
               ("쥐 — sichqon", "kechasi pol tagida"),
               ("Devor", "yogʻoch va qogʻozdan, yupqa")],
              head="Nega aynan qush va sichqon?",
              tail="Oʻzbekcha: «Devorning ham qulogʻi bor».",
              dur=12.5,
              note="Egizak: biz quloqni devorga berganmiz, koreyslar devor "
                   "atrofidagi jonzotlarga. Tarjima emas — vazifa bitta."),

        pairs([("낮말을 새가 듣는다", "kunduzgi gapni — oddiy xabar"),
               ("낮말은 새가 듣고", "kunduzgi gapni ESA — davomi bor"),
               ("은 · 는", "«esa»: ikkinchi yarmini chaqiradi")],
              head="Bitta boʻgʻinni almashtiring",
              tail="을 — xabar. 은 — qarama-qarshilik.",
              dur=12.5,
              note="Filmning TIL darsi. 은 qoʻyilganda tinglovchi «kechasi-chi?» "
                   "deb kutadi — maqol aynan shu kutishga qurilgan."),

        echo("낮말은", gloss="kunduzgi gap esa",
             note="JIM sahna, ikkinchisi."),

        rule("은/는 — «esa»: gapni ikki yarimga boʻladi",
             strip="낮말은 … 밤말은 … = kunduzgisini … kechasini esa …",
             meaning="을 qoʻyilsa — oddiy xabar. 은 qoʻyilsa — qarama-qarshilik "
                     "boshlanadi va tinglovchi ikkinchi yarmini kutadi. Maqol "
                     "aynan shunday qurilgan: kunduz — qush, kecha — sichqon.",
             dur=10.5),

        ask("커피는 좋아해요 — «qahvani esa yoqtiraman». "
            "Bu gap yana nimani aytmasdan aytyapti?",
            dur=7.4,
            note="Javobni aytmang (boshqa narsani yoqtirmasligini). "
                 "Videoda 은/는 faqat maqolda koʻrsatilgan."),

        practice("Burchak · Koreys maqollari",
                 sub="powerty.uz → Burchak → Koreys maqollari",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreys maqolida gapingizni sichqon eshitadi. || Bizda esa — devor.",

    "낮말은 새가 듣고, 밤말은 쥐가 듣는다. "
    "|| Kunduzgi gapni qush, kechasi gapni sichqon eshitadi.",

    None,   # echo(쥐가 듣는다)

    "Nega aynan ular? | Eski koreys uyi yogʻoch va qogʻozdan, devori yupqa. "
    "|| Bizda esa quloqni devorning oʻziga berishgan.",

    "Endi tilga qarang. | 낮말을 — kunduzgi gapni: oddiy xabar. "
    "|| 낮말은 — kunduzgi gapni esa, va davomi bor.",

    None,   # echo(낮말은)

    "Maqolning ikki yarmini bitta boʻgʻin bogʻlaydi: esa. "
    "|| Kunduzi qush eshitadi, kechasi esa sichqon.",

    "Endi oʻzingiz oʻylang. 커피는 좋아해요 — qahvani esa yoqtiraman. "
    "| Bu gap yana nimani aytyapti? || Izohda kutamiz.",

    "Bu maqolning toʻliq hikoyasi — Powertyda, Burchak boʻlimida.",

    None,   # outro
])
