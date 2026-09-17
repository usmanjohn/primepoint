# -*- coding: utf-8 -*-
"""KO-17 — «Ketayotgan soʻz»  ·  BIR MAQOL, IKKI TIL

속담: 가는 말이 고와야 오는 말이 곱다 — «ketayotgan soʻz chiroyli boʻlsa,
kelayotgan soʻz ham chiroyli boʻladi». Oʻzbekchasi: «Qanday salom bersang,
shunday alik olasan.»

The second proverb film, and its shape is deliberately not ko16's. ko16 was
an ALIGNMENT -- two proverbs in columns, only the animal different. This one
is a WORD: 말 is both «soʻz» and «ot», written identically, and a learner who
meets the proverb before the homonym reads it as a sentence about horses.

So the cover is one enormous 말 and a three-word promise, and the mechanism
scene is a `versus` of the same character against itself. That is the whole
reason this proverb is worth a film rather than a caption: it teaches a fact
about the language, not only a piece of wisdom.

⚠️ The two 말 are homographs, not one word with two senses, and the film says
exactly that -- «bitta yozuv, ikkita soʻz». (Careful speech separates them by
vowel length as well; that is left out, because an Uzbek transliteration
cannot show it and the film would be making a claim the picture cannot back.)
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, versus, pairs, echo,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:96px">%s</span>'

VIDEO = Video(
    slug="ko17",
    lesson="속담",
    title="Ketayotgan soʻz",
    story="Koreys maqollari",
    subject="korean",
    scenes=[
        cover("말", "Ot emas — soʻz",
              kicker="Bir maqol, ikki til",
              context="Koreys maqolidagi eng muhim soʻz:",
              strike=False,
              note="MUQOVA: bitta ulkan belgi va uch soʻzlik vaʼda. Gʻalati "
                   "narsa — maqolda ot bordek koʻrinadi, aslida yoʻq."),

        says("Jasur", [("Kafeda shunday dedi:", "lbl"),
                       ("Tez boʻling!", "expr")],
             mood="oh",
             note="Ketayotgan soʻz. Hech qanday grammatik xato yoʻq."),

        consequence("Ofitsiant", "Navbat bor, koʻrmayapsizmi?",
                    mood="sad",
                    note="Kelayotgan soʻz. Maqol aynan shu ikki gap "
                         "orasidagi bogʻliqlik haqida."),

        versus({"name": "말 ①",
                "qty": KQ % "말",
                "price": "soʻz",
                "tag": "gapiriladigan narsa"},
               {"name": "말 ②",
                "qty": KQ % "말",
                "price": "ot",
                "tag": "minadigan hayvon"},
               title="Bitta yozuv, ikkita soʻz",
               verdict="Maqolda — birinchisi",
               dur=12.5,
               note="Filmning tili haqidagi dalili: bir xil yoziladi, "
                    "ikki xil soʻz. Maqolni ot haqida deb oʻqish oson."),

        pairs([("가는 말", "ketayotgan soʻz"),
               ("고와야", "chiroyli boʻlsa"),
               ("오는 말", "kelayotgan soʻz"),
               ("곱다", "chiroyli boʻladi")],
              head="Soʻzma-soʻz",
              tail="Soʻz ketadi va qaytadi — xuddi odamdek",
              note="Toʻrt boʻlak. «Ketmoq» va «kelmoq» feʼllari soʻzning "
                   "oʻziga ishlatilgani — maqolning butun tasviri."),

        echo("가는 말", gloss="ketayotgan soʻz",
             head="Avval ketadigani",
             note="JIM sahna. Maqolning birinchi yarmi."),

        rule("Qanday salom bersang, shunday alik olasan",
             strip=K % "가는 말" + " → ketayotgan   ·   " + K % "오는 말"
                   + " → kelayotgan",
             meaning="Oʻzbekchada ham xuddi shu maqol bor, faqat tasvir "
                     "boshqa: bizda salom va alik, koreysda ketayotgan va "
                     "kelayotgan soʻz. Fikr bitta — boshlagan siz boʻlasiz.",
             dur=10.0),

        echo("오는 말이 곱다", gloss="kelayotgan soʻz chiroyli", size=112,
             note="JIM sahna. Maqolning ikkinchi yarmi — javob."),

        ask("«곱다» — chiroyli. Unda «고운 말» nima degani?",
            dur=7.2,
            note="Javobni aytmang. Sifatning oʻzi filmda bor, bu shakli yoʻq."),

        practice("Prime Korean · 100 dars",
                 sub="Koreys tili noldan, oʻzbekchada", dur=5.4,
                 note="Maqol — tilning ustidagi qavat. Avval tilning oʻzi."),

        outro(line2="koreys tili · 속담"),
    ],
)

narrate(VIDEO, [
    "Koreyschada *말* degan soʻz bor. || Va u ikkita boshqa-boshqa soʻz.",

    "Jasur kafeda «tez boʻling» dedi.",

    "Javobini ham xuddi shunday oldi.",

    "*말* — soʻz degani. | Va ayni oʻsha yozuv ot degani ham. "
    "|| Maqolda esa birinchisi turibdi.",

    "Maqol shunday: *가는 말이 고와야 오는 말이 곱다*. "
    "|| Yaʼni ketayotgan soʻz chiroyli boʻlsa, kelayotgani ham chiroyli "
    "boʻladi.",

    None,   # echo(가는 말) — jim sahna, koreyscha ovoz

    "Bizda ham xuddi shu maqol bor: qanday salom bersang, shunday alik "
    "olasan. || Tasvir boshqa, fikr bitta.",

    None,   # echo(오는 말이 곱다) — jim sahna, koreyscha ovoz

    "Endi oʻzingiz oʻylang. *곱다* — chiroyli. "
    "|| Unda *고운 말* nima degani? Izohda kutamiz.",

    "Koreys tili noldan Powertyda: Praym Korean, yuzta dars. "
    "| Havola profilda.",

    None,   # outro — jim
])
