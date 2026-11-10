# -*- coding: utf-8 -*-
"""MJ-02s — «Toʻqqizta tanga, bittasi qalbaki»   MANTIQ JUMBOGʻI · 2, SAVOL

Nine coins, one lighter fake, a balance, two weighings. Today the plan
everybody tries first -- four against four -- plays out with the fake at #7 and
needs a THIRD weighing. Tomorrow (mj02j): three groups of three.
Gate: verify_coins9.py (scratchpad) -- every fake 1..9 found in 2 weighings by
the 3-3-3 strategy; the 4-4 strategy needs 3 for fakes 1..8.
Sprinkles (noworry.txt): the «gumbokchalar» greeting, the Diyor riddle.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate
from scenes import ask, fact, outro
from _coins import table, W, B, D
import bridgekit as BK

S = BK.say
W1, W2, W3 = W([1, 2, 3, 4], [5, 6, 7, 8]), W([5, 6], [7, 8]), W([7], [8])

cover = table("cover", hold=3.4, msg=(
    S("Mantiq jumbogʻi · 2", "bk-kick", anim="none")
    + S("9 tanga", "bk-hero", anim="none")
    + S("Qaysi biri qalbaki?", "bk-slab", anim="none")))
cover.note = "MUQOVA: toʻqqizta raqamli tanga va tarozi. Qalbakisi koʻrinmaydi."

VIDEO = Video(
    slug="mj02s",
    lesson="Mantiq jumbogʻi 2 — savol",
    title="Toʻqqizta tanga, bittasi qalbaki",
    story="MJ-02 · savol (javobi: mj02j)",
    subject="logic",
    scenes=[
        cover,
        table("bittasi qalbaki", hold=2.0,
              msg=S("Bittasi qalbaki — sal yengilroq", "bk-txt", at=0.3)),
        table("qoida", hold=2.0, msg=(
            S("Tarozida tortish:", "bk-txt", at=0.2)
            + S("faqat 2 marta", "bk-hero", at=0.7, anim="pop", dur=0.6))),
        table("4 ga 4", now=[W1], hold=1.0,
              msg=S("1-urinish: toʻrttaga toʻrtta", "bk-txt", at=0.0, anim="fade")),
        table("2 ga 2", before=[W1], now=[B(), D([1, 2, 3, 4, 9]), W2], hold=1.0),
        table("uchinchi tortish", before=[W1, B(), D([1, 2, 3, 4, 9]), W2],
              now=[B(), D([5, 6]), W3], limit=2, hold=2.4, msg=(
                  S("3-tortish!", "bk-hero bk-red", at=4.2, anim="stamp", dur=0.6)
                  + S("Ikki martada boʻlmadi", "bk-txt", at=4.9))),
        ask("Faqat ikki tortishda qalbakini qanday topasiz?",
            head="Yoʻli bor!", dur=6.0, note="Javobni aytmang: 3 ta guruh — ertaga."),
        fact("Bonus", "Diyor yoʻlda ketayotgan ekan, kiyib olibdi.",
             cap="Nimani kiyib olibdi? 😄", dark=True, dur=6.0, cam="push",
             note="Hazil: «ketayotgan» → «ketani». Javobi ovozda."),
        fact("Ertaga", "yechimini koʻrsatamiz",
             cap="Javobingizni izohga yozing!", dark=True, dur=5.0, cam="push"),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Salom, gumbokchalar! Sogʻliqlar qayerda? || Bugun — toʻqqizta tanga.",

    "Bittasi qalbaki: | u boshqalaridan sal yengilroq. || Koʻrinishi esa bir xil.",

    "Tarozida faqat ikki marta tortish mumkin. | Qalbakini qanday topamiz?",

    "Birinchi fikr: toʻrttaga toʻrtta qoʻyamiz. || Oʻng tomon yengil!",

    "Demak, qalbaki beshdan sakkizgacha. | Ikkitaga ikkita... || Yana oʻng tomon yengil.",

    "Yettinchimi, sakkizinchimi? | Bilish uchun yana tortish kerak. || [sighs] Ikki martada boʻlmadi!",

    "Ikki marta tortishda topishning yoʻli bor. || Qanday?",

    "Bonus: Diyor yoʻlda ketayotgan ekan, kiyib olibdi. | Nimani kiyib olibdi? || [laughs] Ketani!",

    "Javobingizni izohga yozing. || Yechimi — ertaga!",

    None,
])
