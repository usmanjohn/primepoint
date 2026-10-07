# -*- coding: utf-8 -*-
"""KO-41 — «Katta qovoq»  ·  NEGA SHUNDAY?  ·  KOREYA OLAMI

Koreyslarning eng mashhur hayqirigʻi 대박 va uning qovogʻi. Foydalanuvchining
iltimosi (2026-10-08): kulgili soʻzlar — «oshqovoqchalar» — va koreyscha
hayqiriqlar (아이고, 헐). Bu film ikkalasini bitta mavzuga aylantiradi:
박 — aynan qovoq.

Faktlar va ularning darajasi:
- 대 = 大 «katta» — bankda bor (examprep VocabRoot 대: 대부분, 대중…).
  Lugʻat 대박 ni «大 + 박» deb beradi.
- 박 = qovoq (idish qilinadigan qovoq, 바가지 shundan) — lugʻat maʼnosi.
- 흥부와 놀부 — koreys xalq ertagi (판소리 «흥부가»): mehribon Hungbu
  qaldirgʻochning singan oyogʻini bogʻlaydi, qaldirgʻoch qovoq urugʻini olib
  keladi, qovoqlardan boylik chiqadi; xasis aka Noʻlbu qaldirgʻochning
  oyogʻini oʻzi sindiradi va uning qovoqlaridan balo chiqadi.
- ⚠️ 대박 ning kelib chiqishi ANIQ EMAS. Ertakka bogʻlash — bir nechta
  izohdan eng mashhuri. Film buni «bitta mashhur izohga koʻra» deb aytadi va
  qoida kartasida «aniq emas» deb yozadi. Fakt sifatida aytilmaydi.
- 쪽박 — kichik (singan) qovoq; 쪽박(을) 차다 = qashshoq boʻlib qolmoq.
  Bu ask ning javobi, videoda aytilmaydi.

Shakl: «Nega shunday?» (SERIES §3) — ko02 (Sejong) traction olgan kelib
chiqish hikoyasi shaklining koreyscha davomi.
"""

from spec import Video, narrate
from scenes import (cover, build, says, fact, pairs, echo, rule, ask,
                    practice, outro)

K = '<span class="ko">%s</span>'

VIDEO = Video(
    slug="ko41",
    lesson="Koreya olami",
    title="Katta qovoq",
    story="Koreya olami — 대박 va 흥부와 놀부",
    subject="korean",
    scenes=[
        cover("대박!", "Bu — katta qovoq",
              kicker="Nega shunday?", ko="한국어",
              context="Koreyslar hayratda qolganda aytadi:",
              strike=False,
              note="MUQOVA: gʻalati narsa — «zoʻr!» degan soʻz aslida "
                   "qovoq. Vaʼda uch soʻz."),

        build([("대", "katta", True), ("박", "qovoq", False)],
              "대박", gloss="zoʻr! omad!",
              head="Ikki boʻgʻin",
              dur=8.5,
              note="대 = 大, bankdagi ildiz. 박 — qovoq."),

        says("Sherbek", [("TOPIK natijasi keldi…", "lbl"),
                         ("대박!", "expr ko")],
             mood="laugh", dur=6.0,
             note="Kundalik ishlatilishi: kutilmagan omad."),

        echo("대박", gloss="zoʻr! omad!",
             note="JIM sahna. Ikki boʻgʻin."),

        fact("흥부와 놀부", "Koreys xalq ertagi",
             cap="Mehribon Hungbu va xasis Noʻlbu",
             dur=7.0, dark=True,
             note="Burilish: qovoq qayerdan keldi."),

        pairs([("Qaldirgʻoch", "singan oyogʻini Hungbu bogʻlaydi"),
               ("Bahorda", "qovoq urugʻini olib keladi"),
               ("Kuzda", "qovoqlardan boylik chiqadi")],
              head="Hungbuning qovoqlari",
              tail="Katta qovoq — katta omad.",
              dur=12.5,
              note="Ertak — xronologik tartibda."),

        pairs([("흥부", "qaldirgʻochni davoladi → boylik"),
               ("놀부", "oyogʻini oʻzi sindirdi → balo")],
              head="Ikki aka-uka, ikki xil qovoq",
              tail="Ochkoʻzning qovogʻidan — balo.",
              dur=10.5,
              note="Kulgili payoff: xasis aka ham qovoq istadi."),

        pairs([("대박!", "Zoʻr! Omad!"),
               ("아이고!", "Voy! Ey Xudoyim!"),
               ("헐!", "Nima?! Shunaqasi ham boʻladimi?!")],
              head="Koreys hayqiriqlari",
              tail="Har xalqning oʻz «voy»i bor.",
              dur=12.0,
              note="Foydalanuvchi soʻragan hayqiriqlar."),

        echo("아이고", gloss="voy!",
             note="JIM sahna, ikkinchisi. Haqiqiy soʻz — echo qoidasi "
                  "buzilmaydi."),

        rule("대박 = 대 (katta) + 박 (qovoq)",
             strip=K % "대박" + " — zoʻr   ·   " + K % "아이고"
                   + " — voy   ·   " + K % "헐" + " — nima?!",
             meaning="Bugun 대박 — «zoʻr, katta omad». Kelib chiqishi aniq "
                     "emas; eng mashhur izoh — Hungbuning omad qovoqlari. "
                     "대 esa 大: 대부분, 대중 soʻzlarida ham «katta».",
             dur=11.0),

        ask("Katta qovoq — 대박, omad. "
            "Kichkina, singan qovoq-chi?",
            dur=7.0,
            note="Javobni aytmang (쪽박 — qashshoqlik; 쪽박 차다). "
                 "Videoda yoʻq."),

        practice("Burchak · Koreya olami",
                 sub="powerty.uz → Burchak → Koreya olami",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreyslar hayratda qolsa, 대박 deydi. "
    "|| Soʻzma-soʻz esa — katta qovoq.",

    "Oldingi boʻgʻin — katta. | Keyingisi — qovoq. "
    "|| Qovoq qanday qilib «zoʻr» boʻlib qoldi?",

    "Sherbek TOPIK natijasini koʻrdi: [excited] 대박! "
    "|| Yaʼni — zoʻr, omad keldi.",

    None,   # echo(대박)

    "Bitta mashhur izoh — eski ertakdan. "
    "|| Hungbu va Noʻlbu: mehribon uka va xasis aka.",

    "Hungbu qaldirgʻochning singan oyogʻini bogʻlaydi. "
    "| Bahorda qaldirgʻoch qovoq urugʻini olib keladi. "
    "|| Kuzda qovoqlardan boylik chiqadi!",

    "Xasis Noʻlbu ham qovoq istadi | va qaldirgʻochning oyogʻini oʻzi "
    "sindirdi. || Uning qovoqlaridan balo chiqdi. [laughs]",

    "Koreys hayqiriqlari: | 아이고 — voy! | 헐 — nima?! "
    "|| Va 대박 — zoʻr!",

    None,   # echo(아이고)

    "Kelib chiqishi aniq emas, | lekin ertak — eng mashhur izoh. "
    "|| Oldingi boʻgʻin esa doim katta.",

    "Endi oʻzingiz, oshqovoqchalar: katta qovoq — omad. "
    "| Kichkina, singan qovoq-chi? || Izohda kutamiz.",

    "Koreya haqidagi boshqa hikoyalar — Powertyda, Burchak boʻlimida.",

    None,   # outro
])
