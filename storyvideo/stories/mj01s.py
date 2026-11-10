# -*- coding: utf-8 -*-
"""MJ-01s — «Tungi koʻprik: besh kishi, 30 soniya»   MANTIQ JUMBOGʻI · 1-kun, SAVOL

The first «Bugun savol — ertaga javob» film (2026-10-29). Today: the puzzle,
and the plan everybody tries first, played out until the lantern dies.
Tomorrow (mj01j): the solution, 29 seconds.

Not mo34. That film is the four-person 1-2-5-10 version, solved on screen in
one go. This is the five-person version with a lantern that runs OUT --
1, 3, 6, 8, 12 against 30 seconds -- and the greedy plan really does fail:
12 + 1 + 8 + 1 + 6 + 1 + 3 = 32, and the lantern dies one second into the last
trip, with Jasur and Afsona on the bridge. Gate: scratchpad verify_bridge5.py
(Dijkstra over every state: the optimum is 29, the greedy plan 32).
"""

from spec import Video, narrate, Scene
from scenes import ask, fact, outro
import bridgekit as BK

CAST = [("Jasur", 1), ("Afsona", 3), ("Sherbek", 6), ("Nodira opa", 8), ("Bobo", 12)]
# Jasur leads every trip: he carries the lantern over and brings it back.
GREEDY = [(0, 4), (0,), (0, 3), (0,), (0, 2), (0,), (0, 1)]


def bridge(name, show=(0, 0), msg="", hold=0.6, **kw):
    html, end, info = BK.world(CAST, GREEDY, show=show, msg=msg, **kw)
    return Scene(round(end + hold, 2), html, cam="hold", name=name), info


S = BK.say
cover, _ = bridge(
    "cover",
    msg=(S("Mantiq jumbogʻi · 1", "bk-kick", anim="none")
         + S("30 soniya", "bk-hero", anim="none")
         + S("Hammasi oʻta oladimi?", "bk-slab", anim="none")),
    hold=3.4)
cover.note = "MUQOVA: tungi koʻprik, besh kishi, fonar. «30 soniya» — vaʼda: hammasi oʻta oladimi?"

intro, _ = bridge("kim qancha", intro=0.55, hold=2.2,
                  msg=S("Kim necha soniyada oʻtadi?", "bk-txt", at=0.0, anim="fade"))

rules, _ = bridge("qoidalar", hold=1.5, msg=(
    S("Koʻprikda — koʻpi bilan 2 kishi", "bk-txt", at=0.2)
    + S("Fonarsiz yurib boʻlmaydi", "bk-txt", at=1.4)
    + S("Juftlik — sekinrogʻi tezligida", "bk-txt", at=2.6)))

lamp, _ = bridge("fonar", hold=3.0, msg=(
    S("Fonar", "bk-txt", at=0.0, anim="fade")
    + S("30 soniya", "bk-hero", at=0.4, anim="pop", dur=0.7)
    + S("yonadi — keyin oʻchadi", "bk-txt", at=1.1)))

tryA, _ = bridge("urinish: bobo", show=(0, 2), at=1.6, msg=S(
    "1-urinish: Jasur hammani kuzatadi", "bk-txt", at=0.0, anim="fade"))
tryB, _ = bridge("urinish: Nodira, Sherbek", show=(2, 6), at=0.4)

# The death scene is built twice: once to learn WHEN the lantern dies, once
# with the verdict timed to that moment.
_, info = bridge("fonar oʻchdi", show=(6, 7), at=3.2)
d = info["died"]
dead, _ = bridge("fonar oʻchdi", show=(6, 7), at=3.2, hold=2.6, msg=(
    S("Fonar oʻchdi!", "bk-hero bk-red", at=d + 0.35, anim="stamp", dur=0.6)
    + S("Kerak edi: 32 soniya", "bk-txt", at=d + 1.3)))
dead.note = "Jasur va Afsona koʻprik oʻrtasida, qorongʻida. 12+1+8+1+6+1+3 = 32 > 30."

VIDEO = Video(
    slug="mj01s",
    lesson="Mantiq jumbogʻi 1 — savol",
    title="Tungi koʻprik: besh kishi, 30 soniya",
    story="MJ-01 · savol (javobi: mj01j)",
    subject="logic",
    scenes=[
        cover,
        intro,
        rules,
        lamp,
        tryA,
        tryB,
        dead,
        ask("Fonar oʻchmasdan hammasi oʻta oladimi?",
            head="Yoʻli bor. Qanday?", dur=6.4,
            note="Javobni aytmang: 29 soniya — ertaga."),
        fact("Ertaga", "yechimini koʻrsatamiz",
             cap="Javobingizni izohga yozing: necha soniya?",
             dark=True, dur=5.6, cam="push"),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    # v2 (2026-10-29): the playful register he asked for -- fun address words,
    # one "adashib ketdim" aside. v1 is kept as tts_scripts/mj01s_tts_one_v1.txt.
    # noworry.txt: the comeback joke opens the very first post of the series.
    "Agar ketganingni hech kim sezmagan boʻlsa, | demak bekorga ketmagan ekansan. "
    "|| [laughs] Men qaytdim, azizlar!",

    "Tun. Besh kishi tor koʻprik oldida. | Jasur — bir soniya, Afsona — uch, Sherbek — olti. "
    "| Nodira opa — sakkiz, bobo — oʻn ikki.",

    "Koʻprik faqat ikki kishini koʻtaradi. | Fonarsiz yurib boʻlmaydi. "
    "| Juftlik sekinrogʻining tezligida yuradi.",

    "Eng yomoni: | fonar oʻttiz soniyadan keyin oʻchadi. || [playful] Voy-voy, qiyin-ku!",

    "Jasur aytdi: | «Hammani oʻzim olib oʻtaman!» | Avval bobo bilan.",

    "Jasur har safar fonarni qaytaradi... | [confused] adashib ketdim, nimalar deyapman oʻzi? "
    "|| Ha, toʻgʻri!",

    "Oxirgisi Afsona. | Vaqt esa yigirma toʻqqiz soniya. || [gasps] Fonar oʻchdi!",

    "Xoʻsh, yapaloqqushlar, bu yoʻl yaramadi. || Qanday qilib hammasi oʻtadi?",

    "Javobni izohga yozinglar. || Yechimi — ertaga! | Eshitayotgandinglarmi?",

    None,   # outro
])
