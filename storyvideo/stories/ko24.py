# -*- coding: utf-8 -*-
"""KO-24 — «사회 va 회사»  ·  BITTA SOʻZ

Manba: examprep VocabRoot 회(會), TOPIK track — beshta soʻz bankning oʻziniki.

The root film with the best single frame in the whole register: 社會 and 會社
are the same two characters in opposite order, and they mean «society» and
«company». Nothing else in the bank shows so cheaply that a Sino-Korean word
is not a lump -- it is an ORDERED pair, and the order is the meaning.

That is also the caveat ko01 and ko10 never gave. Those films taught that a
root unlocks words; this one adds the second half of the rule, which is that
knowing the two syllables is not yet knowing the word. A learner who reads
회사 as «jamiyat» has done the arithmetic right and got the wrong answer.

Two `build` beats back to back do the work: the same two tiles walk in twice,
in opposite orders, and land on two different words. The Uzbek viewer has an
exact parallel to hand -- *ish boshi* and *bosh ish* -- and the narration says
so, because that is the sentence only this channel can say.
"""

from spec import Video, narrate
from scenes import (cover, word, word_family, build, echo, versus,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:88px">%s</span>'

VIDEO = Video(
    slug="ko24",
    lesson="Koreya olami",
    title="사회 va 회사",
    story="examprep VocabRoot 회(會)",
    subject="korean",
    scenes=[
        cover("사회 · 회사", "Ikkisi bir xil emas",
              kicker="Bitta soʻz",
              ko="한국어",
              context="Bir xil ikki boʻgʻin, teskari tartibda:",
              strike=False,
              note="MUQOVA: gʻalati narsa — koʻzga aynan bir xil koʻringan "
                   "ikki soʻz. Vaʼda ularni inkor qiladi."),

        word("회", gloss="yigʻilish — jamoa, uchrashuv", hanja="會",
             head="Bugungi ildiz", dur=6.4, size=220,
             note="Oʻzi soʻz emas — soʻz yasaydi. Xuddi 출 va 입 kabi."),

        word_family(
            "회",
            [("회사", "會社", "kompaniya, firma"),
             ("사회", "社會", "jamiyat"),
             ("회의", "會議", "yigʻilish, majlis"),
             ("기회", "機會", "imkoniyat, fursat"),
             ("회원", "會員", "aʼzo")],
            hanja="會", meaning="yigʻilish", label="ta soʻz",
            cols=1, dur=11.5,
            note="Beshtasi ham bitta ildizdan. Birinchi ikkitasi esa "
                 "bir-birining teskarisi — sanagich buni koʻrsatmaydi, "
                 "keyingi sahna koʻrsatadi."),

        echo("기회", gloss="imkoniyat, fursat",
             note="JIM sahna. Oilaning eng koʻp ishlatiladigan soʻzi."),

        build([("사", "jamoa", False), ("회", "yigʻilish", True)],
              "사회", gloss="jamiyat",
              head="Avval jamoa, keyin yigʻilish",
              dur=9.5,
              note="YANGI BEAT. Ikkita plitka, bitta tartib."),

        build([("회", "yigʻilish", True), ("사", "jamoa", False)],
              "회사", gloss="kompaniya",
              head="Endi teskarisi",
              caption="Bir xil ikkita belgi — boshqa soʻz",
              dur=11.0,
              note="Filmning butun dalili: AYNAN oʻsha ikkita plitka, "
                   "joyi almashgan, maʼnosi butunlay boshqa."),

        versus({"name": "社會",
                "qty": KQ % "사회",
                "price": "jamiyat",
                "tag": "odamlar yigʻilgan joy"},
               {"name": "會社",
                "qty": KQ % "회사",
                "price": "kompaniya",
                "tag": "yigʻilib ish qiladigan joy"},
               title="Tartib maʼnoni oʻzgartiradi",
               verdict="Ildizni bilish — hali soʻzni bilish emas",
               dur=12.0,
               note="Ehtiyot qoidasi. ko01 va ko10 ildizning kuchini "
                    "koʻrsatgan edi; bu sahna uning chegarasini koʻrsatadi."),

        echo("회사", gloss="kompaniya",
             note="JIM sahna. Ikkinchi tartib."),

        rule("Xitoycha soʻzda tartib — maʼnoning bir qismi",
             strip=K % "사" + " + " + K % "회" + " = jamiyat   ·   "
                   + K % "회" + " + " + K % "사" + " = kompaniya",
             meaning="Oʻzbekchada ham shunday: «ish boshi» va «bosh ish» "
                     "bir xil ikkita soʻzdan tuzilgan, lekin bitta narsani "
                     "anglatmaydi. Ildizni toping — keyin tartibiga qarang.",
             dur=10.5),

        ask("«회원» — aʼzo. Unda «회비» qanday pul boʻladi?",
            dur=7.2,
            note="Javobni aytmang. 회 videoda bor, 비 yoʻq."),

        practice("TOPIK lugʻat · soʻz oilalari",
                 sub="powerty.uz → Examprep → Lugʻat → Soʻz oilalari",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreysda ikkita soʻz bor: *사회* va *회사*. "
    "|| Bir xil ikkita boʻgʻin. Ikkita butunlay boshqa maʼno.",

    "Ildiz — *회*, maʼnosi: yigʻilish.",

    "U beshta soʻzni ochadi: kompaniya, jamiyat, majlis, imkoniyat, "
    "aʼzo. || Beshtasi ham bitta ildizdan.",

    None,   # echo(기회) — jim sahna, koreyscha ovoz

    "Endi diqqat: *사* jamoa, *회* yigʻilish. || Birgalikda — jamiyat.",

    "Endi ularni almashtiramiz. || Va soʻz kompaniyaga aylandi.",

    "Demak ildizni bilish hali soʻzni bilish emas. || Tartibi ham "
    "maʼnoning bir qismi.",

    None,   # echo(회사) — jim sahna, koreyscha ovoz

    "Bizda ham shunday: «ish boshi» va «bosh ish». | Bir xil ikkita soʻz, "
    "boshqa maʼno.",

    "Endi oʻzingiz oʻylang. *회원* aʼzo boʻlsa, *회비* qanday pul? "
    "|| Izohda kutamiz.",

    "Ellik bitta ildizning hammasi Powertyda: Examprep, lugʻat, "
    "soʻz oilalari.",

    None,   # outro — jim
])
