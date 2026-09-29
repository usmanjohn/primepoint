# -*- coding: utf-8 -*-
"""KO-27 — «Sabr tagi — sariq oltin»  ·  BIR MAQOL, IKKI TIL

속담: 고생 끝에 낙이 온다 — «mashaqqat oxirida zavq keladi».
Oʻzbekchasi: «Sabr tagi — sariq oltin.»

The fifth proverb film, and the one whose language lever is the hardest fact
in the whole register: 낙 is 樂, and the SAME character read 악 is the 악 of
음악, music. One character, two Korean readings, two unrelated meanings --
which is exactly why `korean.py` refuses to romanise a hanja and why the
vocabulary films teach the SYLLABLE rather than the character.

So this film quietly explains the pipeline's own rule to the audience, in the
one place they will remember it: a proverb about patience. 고생 also opens
with 생, ko20's root, so a viewer who saw that film reads half of this one
before the narration gets there.

⚠️ The Uzbek twin is not a translation and the film never presents it as one.
Korean counts the hardship and the joy; Uzbek weighs patience against gold.
The shared job is the same promise -- keep going -- and saying exactly that is
what the series is for.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, order, echo, versus,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:120px">%s</span>'

VIDEO = Video(
    slug="ko27",
    lesson="속담",
    title="Sabr tagi — sariq oltin",
    story="Koreys maqollari",
    subject="korean",
    scenes=[
        cover("樂", "Bitta belgi, ikkita ovoz",
              kicker="Bir maqol, ikki til",
              ko="한국어",
              context="Koreysda bu belgi ikki xil oʻqiladi:",
              strike=False,
              note="MUQOVA: gʻalati narsa — bitta xitoycha belgi, va uning "
                   "ustiga qoʻyilgan daʼvo. Hech qanday chiziq yoʻq, "
                   "chunki bu xato emas."),

        says("Sherbek", [("Uch yil dam olmadi:", "lbl"),
                         ("Charchadim.", "expr")],
             mood="sad",
             note="Vaziyat: mashaqqatning oʻrtasi. Maqol aynan shu "
                  "nuqtada aytiladi."),

        consequence("Sherbek", "Toʻrtinchi yili — oʻz doʻkoni.",
                    mood="laugh", close=True, cam="pull",
                    note="Maqolning ikkinchi yarmi roʻy berdi. YANGI: "
                         "yaqin plan va kulgi — seriyada birinchi marta "
                         "yakun quvonchli."),

        echo("고생 끝에", gloss="mashaqqat oxirida",
             head="Maqolning birinchi yarmi",
             note="JIM sahna. 고생 ning 생 i — ko20 dagi «hayot» ildizi."),

        order([("Koreyscha", [("고생 끝에", "s"), ("낙이", "o"),
                              ("온다", "v")], True),
               ("Soʻzma-soʻz", [("mashaqqat oxirida", "s"), ("zavq", "o"),
                                ("keladi", "v")], False),
               ("Oʻzbekcha", [("sabr", "s"), ("tagi", "o"),
                              ("sariq oltin", "v")], False)],
              head="Bitta vaʼda, ikkita til",
              verdict="Tasvir boshqa, vaʼda bitta",
              dur=13.0,
              note="Koreys sanaydi: mashaqqat, keyin zavq. Biz oʻlchaymiz: "
                   "sabr va oltin. Uchinchi qator tarjima emas — egizak."),

        versus({"name": "樂 → 낙",
                "qty": KQ % "낙",
                "price": "zavq, rohat",
                "tag": "고생 끝에 낙이 온다"},
               {"name": "樂 → 악",
                "qty": KQ % "악",
                "price": "musiqa",
                "tag": "음악 · 악기"},
               title="Bitta belgi, ikkita oʻqilish",
               verdict="Shuning uchun belgini emas — boʻgʻinni oʻrganamiz",
               dur=12.5,
               note="Filmning til haqidagi dalili, va butun soʻz oilasi "
                    "seriyasining ehtiyot qoidasi: xitoycha belgining "
                    "koreyscha oʻqilishi bittadan koʻp boʻlishi mumkin."),

        echo("낙이 온다", gloss="zavq keladi",
             note="JIM sahna. Maqolning ikkinchi yarmi — vaʼdasi."),

        rule("Sabr tagi — sariq oltin",
             strip=K % "고생" + " → mashaqqat   ·   " + K % "낙"
                   + " → zavq   ·   " + K % "온다" + " → keladi",
             meaning="Koreys maqoli vaqtni sanaydi: avval mashaqqat, keyin "
                     "zavq. Bizniki qiymat oʻlchaydi: sabr — oltin. Ikkala "
                     "xalq ham bir narsani aytadi, boshqa-boshqa tarozida.",
             dur=10.5),

        ask("«음악» — musiqa. Unda «악기» qanday narsa?",
            dur=7.2,
            note="Javobni aytmang. Videoda 악 bor, 기 yoʻq."),

        practice("Prime Korean · 100 dars",
                 sub="Koreys tili noldan, oʻzbekchada", dur=5.4,
                 note="Maqol — tilning ustidagi qavat."),

        outro(line2="koreys tili · 속담"),
    ],
)

narrate(VIDEO, [
    "Koreysda bitta xitoycha belgi bor, va u ikki xil oʻqiladi. "
    "|| Birinchisi maqolda turibdi.",

    "Sherbek uch yil dam olmay ishladi.",

    "Toʻrtinchi yili oʻz doʻkonini ochdi.",

    None,   # echo(고생 끝에) — jim sahna, koreyscha ovoz

    "Maqol shunday: *고생 끝에 낙이 온다*. || Mashaqqat oxirida zavq keladi.",

    "Endi oʻsha belgi. | *낙* boʻlib oʻqilsa — zavq. "
    "|| *악* boʻlib oʻqilsa — musiqa. Aynan bitta belgi.",

    None,   # echo(낙이 온다) — jim sahna, koreyscha ovoz

    "Bizda esa: sabr tagi — sariq oltin. || Koreys vaqtni sanaydi, biz "
    "qiymat oʻlchaymiz. Vaʼda esa bitta.",

    "Endi oʻzingiz oʻylang. *음악* musiqa boʻlsa, *악기* qanday narsa? "
    "|| Izohda kutamiz.",

    "Koreys tili noldan Powertyda: Praym Korean, yuzta dars. "
    "| Havola profilda.",

    None,   # outro — jim
])
