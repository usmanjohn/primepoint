# -*- coding: utf-8 -*-
"""KO-28 — «Bir xil boʻgʻin, boshqa ildiz»  ·  BITTA SOʻZ

Manba: examprep VocabRoot 인(人), TOPIK track — oltita soʻz 人 li, va
bankning yettinchi soʻzi 원인 boshqa belgi bilan yoziladi: 原因.

The film that adds the caveat ko01, ko10, ko20 and ko24 were all too pleased
with themselves to give. Four films have now said «find the root and the words
come free». This one says the other half: a Korean syllable is a SOUND, and
two different Chinese characters can arrive at the same sound. 인간 and 원인
both say «in» and only one of them is about people.

So the arc is a discovery film that turns into a correction: the family is
counted as usual, the pupil is invited to feel clever -- and then 원인 walks
in and the rule gets its exception. That is the honest shape of the method,
and it is a better film than a fifth round of applause.

⚠️ The family scene counts SIX words, not the bank's seven, and that is
deliberate: the counter counts what is drawn, and only six of the seven are
人. The seventh is the `versus` card.
"""

from spec import Video, narrate
from scenes import (cover, word, build, word_family, echo, versus,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:88px">%s</span>'

VIDEO = Video(
    slug="ko28",
    lesson="Koreya olami",
    title="Bir xil boʻgʻin, boshqa ildiz",
    story="examprep VocabRoot 인(人)",
    subject="korean",
    scenes=[
        cover("인 ≠ 인", "Ikkalasi bir emas",
              kicker="Bitta soʻz",
              ko="한국어",
              context="Ikkala soʻzda ham «in» eshitiladi:",
              strike=False,
              note="MUQOVA: gʻalati narsa — oʻziga oʻzi teng boʻlmagan "
                   "boʻgʻin. Vaʼda uch soʻz va u qarama-qarshilikdan iborat."),

        word("인간", gloss="inson", hanja="人間",
             head="Eng koʻp soʻz ochadigan ildizlardan", dur=6.4,
             note="Boshlanish nuqtasi: eng tanish soʻz."),

        build([("인", "odam", True), ("간", "oraliq", False)],
              "인간", gloss="«odamlar orasi» — inson",
              head="Ikkita boʻgʻin, ikkita maʼno",
              dur=9.5,
              note="YANGI BEAT. Oltin plitka — bugungi ildiz."),

        word_family(
            "인",
            [("인간", "人間", "inson"),
             ("개인", "個人", "shaxs, yakka odam"),
             ("성인", "成人", "voyaga yetgan kishi"),
             ("인기", "人氣", "mashhurlik"),
             ("인생", "人生", "umr — odam hayoti"),
             ("인공지능", "人工知能", "sunʼiy intellekt")],
            hanja="人", meaning="odam — inson", label="ta soʻz",
            cols=1, dur=12.0,
            note="Oltitasi ham 人 bilan yoziladi. Eng qadimgi ildiz eng "
                 "yangi soʻzning ichida ham turibdi: 인공지능."),

        echo("인기", gloss="mashhurlik",
             note="JIM sahna. «Odam + kayfiyat» — odamlarning kayfiyati."),

        word("원인", gloss="sabab", hanja="原因",
             head="Endi bu soʻzga qarang", dur=7.4, dark=True,
             note="Burilish nuqtasi. Xuddi shunday «in» eshitiladi — "
                  "lekin belgisi boshqa. Qorongʻi karta: bu sahna "
                  "oldingilarini toʻxtatadi."),

        versus({"name": "人 — odam",
                "qty": KQ % "인간",
                "price": "inson",
                "tag": "개인 · 성인 · 인생"},
               {"name": "因 — sabab",
                "qty": KQ % "원인",
                "price": "sabab",
                "tag": "odamga hech qanday aloqasi yoʻq"},
               title="Bir xil ovoz, boshqa belgi",
               verdict="Boʻgʻin bir — ildiz boshqa",
               dur=12.5,
               note="Filmning butun gapi. Toʻrtta film ildizning kuchini "
                    "koʻrsatdi; bu sahna uning chegarasini koʻrsatadi."),

        echo("원인", gloss="sabab",
             note="JIM sahna. Oilaga kirmaydigan soʻz."),

        rule("Bir xil boʻgʻin har doim bir xil ildiz emas",
             strip=K % "인간" + " → 人   ·   " + K % "원인" + " → 因",
             meaning="Ildiz usuli ishlaydi, lekin u taxmin beradi, kafolat "
                     "emas. Yangi soʻz koʻrganda ildizni toping va keyin "
                     "maʼnosi mos kelyaptimi — tekshiring. Mos kelmasa, "
                     "boshqa belgi.",
             dur=10.5),

        ask("«인기» — mashhurlik, yaʼni «odam + kayfiyat». "
            "Unda «인기가 많다» nima degani?",
            dur=7.6,
            note="Javobni aytmang. Videoda 인기 bor, 많다 yoʻq."),

        practice("TOPIK lugʻat · soʻz oilalari",
                 sub="powerty.uz → Examprep → Lugʻat → Soʻz oilalari",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreysda ikkita soʻz bor, ikkalasida ham «in» eshitiladi. "
    "|| Lekin ular bitta ildizdan emas.",

    "*인간* — inson degani.",

    "Ochamiz. *인* — odam. | *간* — oraliq. || Yaʼni «odamlar orasi».",

    "Va oʻsha *인* yana beshta soʻzni ochadi: shaxs, katta yoshli odam, "
    "mashhurlik, umr. || Va sunʼiy intellekt.",

    None,   # echo(인기) — jim sahna, koreyscha ovoz

    "Endi mana bu soʻzga qarang: *원인*. | Sabab degani. "
    "|| Unda ham «in» bor.",

    "Lekin belgisi boshqa. || Ovoz bir xil, ildiz boshqa — va maʼnosining "
    "odamga hech qanday aloqasi yoʻq.",

    None,   # echo(원인) — jim sahna, koreyscha ovoz

    "Demak ildiz usuli taxmin beradi, kafolat emas. || Ildizni toping, "
    "keyin maʼnosi mos kelyaptimi — tekshiring.",

    "Endi oʻzingiz oʻylang. *인기* mashhurlik boʻlsa, *인기가 많다* nima "
    "degani? || Izohda kutamiz.",

    "Ellik bitta ildizning hammasi Powertyda: Examprep, lugʻat, "
    "soʻz oilalari.",

    None,   # outro — jim
])
