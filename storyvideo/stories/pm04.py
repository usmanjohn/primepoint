# -*- coding: utf-8 -*-
"""PM-4 — «Oʻttiz yetti kishi, oltitadan stol»  (qoldiqli boʻlish)

Manba: corner/management/commands/_stories_prime_math_04_06.py, order 4.

Hikoyaning butun gapi: boʻlish toʻgʻri bajarildi, javob esa notoʻgʻri chiqdi,
chunki qoldiqdagi bitta bola unutilgan edi. Shuning uchun videoning markazi —
36 ta oʻrindiq toʻlgani va Bekzod tik turib qolgani.
"""

from spec import Video
from scenes import hook, count_in, says, beat, claim, fill, consequence, \
                   correct, check, rule, outro

# Bekzod qoldiqdagi bola: olomonda ham, stollarda ham oxirgi oʻrinda tursin.
NAMED = {0: "Sardor", 1: "Afsona", 36: "Bekzod"}

VIDEO = Video(
    slug="pm04",
    lesson="PM-4",
    title="Oʻttiz yetti kishi, oltitadan stol",
    story="Prime Math Readings — order 4",
    scenes=[
        hook("37", "bola", "6", "kishilik stol", "Nechta stol kerak?", dur=4.8),

        count_in(37, "bola", named=NAMED, size=104, per_row=7, dur=9.2,
                 note="Nodira opa sinfni kafega olib bordi. Bolalar 37 nafar edi."),

        says("ofitsiant", [("Bizda stollar", "lbl"),
                           ("6 kishilik", "expr gold"),
                           ("Nechtasini tayyorlaymiz?", "ask")],
             dur=6.4, size=270,
             note="Kafe eshigida ofitsiant kutib oldi: stollar olti kishilik."),

        beat(4.2, note="Jim turing. Tomoshabin oʻzi boʻlsin: 37 ni 6 ga."),

        claim("Sardor", "37 ÷ 6", "6", "Toʻgʻrimi?", dur=8.6,
              note="Sardor darrov hisobladi va «6» dedi. Boʻlishning oʻzi toʻgʻri."),

        fill(36, 6, named=NAMED, cols=2, dur=11.0,
             tail="6 × 6 = 36",
             note="Bolalar oʻtira boshlashdi. Oltita stol toʻldi — 36 bola."),

        consequence("Bekzod", "unga oʻrindiq yetmadi", above="36",
                    above_label="oʻtirdi", dur=7.2,
                    note="Bekzod turgan joyida qoldi. Bitta bolaga oʻrindiq yetmadi."),

        correct("6", "7", "37 ÷ 6 = 6, qoldiq 1", lead="37 ÷ 6", dur=8.6,
                note="Hisobing toʻgʻri edi, lekin qoldiqni unutding. Javob 6 emas, 7."),

        fill(37, 6, named=NAMED, cols=2, dur=9.6,
             tail="Bekzodga ham stol kerak",
             note="Ofitsiant yettinchi stolni surdi. Bekzod yolgʻiz oʻtirdi."),

        check("6 × 6 + 1 = 37",
              parts=["6 stol × 6 bola", "+ 1 qoldiq"],
              verdict="Hammasi joyida.", dur=7.6,
              note="Tekshiramiz: boʻlinma × boʻluvchi + qoldiq = boʻlinuvchi."),

        rule("Kamida nechta kerak?", strip="qoldiq bor  →  +1",
             meaning="Teng boʻlinish har doim ham chiqavermaydi.", dur=8.8,
             note="Masala «kamida nechta kerak?» desa, qoldiq uchun doim yana bitta."),

        outro(),
    ],
)
