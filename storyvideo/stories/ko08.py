# -*- coding: utf-8 -*-
"""KO-8 — «Bormayman» va «bora olmayman»  ·  TUTILGAN XATO

Manba: Prime Korean PK-21 va PK-22 (Inkor: 안 + feʼl, 못 + feʼl).

The social-cost shape, the same as ko04: nothing ungrammatical happens, and the
damage is entirely in what the listener hears.

    안 + feʼl   qilmayman      -- a CHOICE
    못 + feʼl   qila olmayman  -- an INABILITY

Uzbek keeps them apart with whole different words (bormayman / bora olmayman),
so the pupil has the concept and only needs the two syllables. What they do not
have is the instinct that picking the wrong one is not a grammar slip but an
insult: 안 가요 to an invitation means "I am choosing not to come."

The `ask` is the one that makes the distinction stick, because it inverts the
film: a vegetarian says 안 먹어요, not 못 먹어요 -- the choice is the whole point
of being one, and nothing is stopping them.
"""

from spec import Video, narrate
from scenes import cover, says, consequence, correct, versus, echo, rule, ask, practice, outro

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:80px">%s</span>'

VIDEO = Video(
    slug="ko08",
    lesson="PK-22",
    title="«Bormayman» va «bora olmayman»",
    story="Prime Korean PK-21, PK-22",
    subject="korean",
    scenes=[
        cover("안 가요", "Rad etgan boʻlib qoldi",
              kicker="Tutilgan xato",
              context="Kelolmasligini aytmoqchi edi:",
              note="MUQOVA: grammatik xato yoʻq — shuning uchun vaʼda "
                   "grammatikadan emas, natijadan gapiradi."),

        says("Jasur", [("Afsona tugʻilgan kuniga chaqirdi.", "lbl"),
                       ("안 가요", "expr ko")],
             mood="smile",
             note="Jasurning ertaga imtihoni bor. U «bora olmayman» "
                  "demoqchi edi."),

        echo("안 가요", gloss="«bormayman» — bu tanlov",
             head="Jasur aytgan gap",
             note="JIM sahna. Shakl toʻgʻri, maʼnosi esa Jasur "
                  "moʻljallaganidan boshqa."),

        consequence("Afsona", "Kelishni xohlamadi.",
                    mood="sad",
                    note="Xatoning bahosi bitta yuzda, va u grammatik "
                         "emas — Afsona rad javobini eshitdi."),

        correct("안", "못",
                because="Imkoni yoʻq boʻlsa — 못",
                lead="__ 가요",
                note="Bitta boʻgʻin. Tanlovni imkonsizlikka aylantiradi."),

        versus({"name": "TANLOV",
                "qty": KQ % "안",
                "price": K % "안 가요",
                "tag": "bormayman"},
               {"name": "IMKONI YOʻQ",
                "qty": KQ % "못",
                "price": K % "못 가요",
                "tag": "bora olmayman"},
               title="Bitta inkor emas — ikkita",
               dur=12.0,
               note="Oʻzbekchada bu ikkitasi butunlay boshqa soʻzlar, "
                    "shuning uchun tushuncha pupilda bor — faqat ikki "
                    "boʻgʻin kerak."),

        echo("못 가요", gloss="«bora olmayman» — imkoni yoʻq",
             note="JIM sahna. Jasur aytishi kerak boʻlgan gap."),

        rule("Xohlamaslik bilan imkonsizlikni koreys tili ajratadi",
             strip=K % "안" + " → tanlov   ·   " + K % "못" + " → imkoniyat",
             meaning="Oʻzbek tilida bu farq soʻzning ichida turadi: "
                     "bormayman va bora olmayman. Koreys tilida esa "
                     "feʼldan oldingi bitta boʻgʻinda.",
             dur=9.6),

        ask("Vegetarian odam goʻsht haqida nima deydi — "
            "«안 먹어요» yoki «못 먹어요»?",
            dur=7.6,
            note="Javobni aytmang. Uni hech kim toʻxtatmayapti — "
                 "jadvaldagi birinchi ustun ishora bergan."),

        practice("Prime Korean · PK-22",
                 sub="Inkor — xohlamaslik va imkonsizlik", dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Afsona Jasurni tugʻilgan kuniga chaqirdi. | Jasurning ertaga imtihoni "
    "bor edi. || U *안 가요* dedi.",

    "Grammatikada hech qanday xato yoʻq. | Shuning uchun bu xatoni hech "
    "kim tuzatmaydi ham.",

    None,   # echo(안 가요) — jim sahna, koreyscha ovoz

    "Ammo Afsona rad javobini eshitdi. || Chunki *안* — bu tanlov.",

    "Almashadigan narsa bitta boʻgʻin. | *안* emas, *못*.",

    "Qarang. *안 가요* — bormayman, yaʼni oʻzim xohlamayman. | *못 가요* — "
    "bora olmayman, yaʼni imkonim yoʻq. || Oʻzbekchada bu ikkitasi "
    "butunlay boshqa soʻzlar, shuning uchun farqni siz allaqachon "
    "bilasiz.",

    None,   # echo(못 가요) — jim sahna, koreyscha ovoz

    "Shuning uchun koreys tilida xohlamaslik bilan imkonsizlik "
    "ajratiladi. || Oʻzbekchada bu farq soʻzning ichida, koreyschada esa "
    "feʼldan oldingi bitta boʻgʻinda turadi.",

    "Endi oʻzingiz oʻylang. Vegetarian odam goʻsht haqida nima deydi? "
    "|| Izohda kutamiz.",

    "Inkor shakllari Powertyda: Praym Korean, yigirma ikkinchi dars.",

    None,   # outro — jim
])
