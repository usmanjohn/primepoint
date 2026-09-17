# -*- coding: utf-8 -*-
"""KO-18 — «Chang yigʻilsa, togʻ boʻladi»  ·  BIR MAQOL, IKKI TIL

속담: 티끌 모아 태산 — «chang zarralarini yigʻsang, 태산 boʻladi».
Oʻzbekchasi: «Tomchi tomchi yigʻilib, koʻl boʻlar.»

The third proverb film, and the one that argues with a PICTURE rather than
a translation: two bars, 600 against 3 650, and the small one is what a
200-words-a-day plan actually produces after three days.

That is the proverb doing work instead of being admired. Every learner has
tried Bekzod's month, and the film's claim is arithmetic, not moral -- so
both sums are on screen and `lint` recomputes them: 200 × 3 = 600 and
10 × 365 = 3 650.

⚠️ 태산 is a real mountain (泰山, Xitoyda), and the film says so rather than
glossing it as «katta togʻ» and leaving a pupil to wonder why a Korean
proverb ends in a Chinese name. The hanja is on the card and never in the
narration -- 出 and 泰 have several readings, so the gate refuses them.

⛔ No claim about how many words any TOPIK level needs. 3 650 is what the
arithmetic gives; what it is ENOUGH for is not something this film knows.
"""

from spec import Video, Scene, narrate
from scenes import (cover, says, consequence, pairs, echo, check,
                    rule, ask, practice, outro)
import primitives as P

K = '<span class="ko">%s</span>'

# Two bars, base 0: the honest axis, and the one the proverb needs. 600 next
# to 3 650 is literally a speck next to a mountain -- the picture is the
# argument, and nothing has to be said over it.
_bars, _sb = P.bars([(600, "3 kun", ""), (3650, "1 yil", "win")],
                    at=0.6, step=1.4)

chart = Scene(
    10.0,
    _bars
    + P.line("chapda kuniga 200 ta · oʻngda kuniga 10 ta", "lbl lbl--sm",
             at=0.6 + _sb + 0.3, anim="fade")
    + P.line("Tikkul — chapdagi emas, oʻngdagi", "ttl grn",
             at=0.6 + _sb + 0.9, anim="pop", dur=0.7),
    cam="push", name="chart",
    claims=["200 × 3 = 600", "10 × 365 = 3 650"],
    note="Chap ustun — uch kunlik gʻayrat. Oʻng ustun — bir yillik odat. "
         "Ikkalasi ham bitta odamning daftari.")

VIDEO = Video(
    slug="ko18",
    lesson="속담",
    title="Chang yigʻilsa, togʻ boʻladi",
    story="Koreys maqollari",
    subject="korean",
    scenes=[
        cover("티끌 → 태산", "Chang yigʻilsa — togʻ",
              kicker="Bir maqol, ikki til",
              context="Koreys maqoli:",
              strike=False,
              note="MUQOVA: chiziq yoʻq — gʻalati narsa koʻrsatiladi. "
                   "Changdan togʻ chiqadigan strelka aylanib oʻtilmaydi."),

        says("Bekzod", [("Imtihonga bir oy qoldi:", "lbl"),
                        ("Kuniga 200 ta soʻz!", "expr")],
             mood="smile",
             note="Har bir oʻquvchi bir marta shunday reja tuzgan."),

        consequence("Bekzod", "Uchinchi kuni tashladim.",
                    mood="sad",
                    note="Reja katta boʻlgani uchun emas — kunlik boʻlmagani "
                         "uchun qulaydi."),

        pairs([("티끌", "chang zarrasi"),
               ("모아", "yigʻilib"),
               ("태산", "ulkan togʻ")],
              head="Soʻzma-soʻz",
              tail="Uch soʻz — butun bir gap",
              note="Koreys maqollari qisqa: feʼl ham, qoʻshimcha ham "
                   "tushib qoladi."),

        echo("태산", gloss="ulkan togʻ", hanja="泰山",
             head="Xitoydagi haqiqiy togʻ nomi",
             note="JIM sahna. 泰山 ekranda turadi, ovozda esa hech qachon: "
                  "hanjaning bir nechta oʻqilishi bor."),

        check("10 × 365 = 3 650",
              parts=["Kuniga oʻnta soʻz — besh daqiqa",
                     "Bir yil davomida, har kuni"],
              verdict="3 650 ta soʻz",
              title="Tikkul nechta boʻladi",
              dur=9.4,
              note="Filmning dalili — koʻpaytirish. Kichik son katta "
                   "koʻpaytuvchini yutadi."),

        chart,

        echo("티끌 모아 태산", gloss="chang yigʻilib togʻ boʻladi", size=104,
             note="JIM sahna. Maqolning oʻzi, toʻliq."),

        rule("Tomchi tomchi yigʻilib, koʻl boʻlar",
             strip=K % "티끌" + " → chang   ·   " + K % "태산" + " → togʻ",
             meaning="Bizda ham xuddi shu maqol bor, faqat suvdan: tomchi "
                     "yigʻilib koʻl boʻladi. Ikkala xalq ham bir narsani "
                     "aytmoqchi — kichik boʻlsin, lekin har kuni boʻlsin.",
             dur=10.0),

        ask("Sizning bugungi «bitta tikkul»ingiz nima boʻladi?",
            dur=7.0,
            note="Javobni aytmang. Bu — koʻchirma savol: javobi "
                 "tomoshabinning oʻz kunida."),

        practice("TOPIK · Lugʻat banki",
                 sub="Soʻz oilalari va ildizlar", dur=5.4,
                 note="Har kuni oʻnta soʻz uchun joy — ildiz oilalari."),

        outro(line2="koreys tili · 속담"),
    ],
)

narrate(VIDEO, [
    "Koreysda shunday maqol bor: *티끌 모아 태산*.",

    "Bekzod boshqacha yoʻl tanladi: kuniga ikki yuzta soʻz.",

    "Uchinchi kuni tashladi. || Reja katta boʻlgani uchun emas — "
    "kunlik boʻlmagani uchun.",

    "*티끌* — chang zarrasi. | *모아* — yigʻilib. | *태산* — ulkan togʻ.",

    None,   # echo(태산) — jim sahna, koreyscha ovoz

    "Endi sanaymiz. Kuniga oʻnta soʻz, besh daqiqa vaqt. "
    "|| Bir yilda — uch ming olti yuz ellikta soʻz.",

    "Bekzodning uch kuni esa olti yuzta. || Bir xil odam, bir xil daftar.",

    None,   # echo(티끌 모아 태산) — jim sahna, koreyscha ovoz

    "Bizda ham shu maqol bor, faqat suvdan: tomchi tomchi yigʻilib, koʻl "
    "boʻlar. || Kichik boʻlsin, lekin har kuni boʻlsin.",

    "Endi oʻzingiz oʻylang. Bugungi bitta tikkulingiz nima boʻladi? "
    "|| Izohda kutamiz.",

    "Har kunlik oʻnta soʻz Powertyda: Topik, lugʻat banki. "
    "| Havola profilda.",

    None,   # outro — jim
])
