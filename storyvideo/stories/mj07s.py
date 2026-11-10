# -*- coding: utf-8 -*-
"""MJ-07s — «Tayoqdagi chumolilar»   MANTIQ JUMBOGʻI · 7, SAVOL

A one-metre stick, ants walking 1 cm/s; two that meet both turn round; an ant
at an end falls off. However they start, what is the LONGEST it can take for
all of them to fall? Today: the bouncing looks hopeless. Tomorrow (mj07j):
treat a bounce as passing through -> at most 100 s.
Gate: verify_batch2.py (bounce sim == pass-through, 200 random configs).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate
from scenes import ask, fact, outro
from _sk import scene, S
from _ants import stick_stage
import stagekit as K

st, clk = stick_stage(0)
cover = scene("cover", st, (S("Mantiq jumbogʻi · 7", "bk-kick", anim="none")
                            + S("1 metr", "bk-hero", anim="none")
                            + S("Qachon hammasi tushadi?", "bk-slab", anim="none")), hold=3.4)

# two ants meet and both turn round
two = K.Stage()
two.add('<div class="sk-stick"></div>', 540, 1262, 900, 24)
a = two.add(K.ant(col="#a23b2a"), 300, 1240, 56, 34, s=1.6)
b = two.add(K.ant(), 780, 1240, 56, 34, s=1.6)
b.set(-900, sx=-1)
a.to(0.6, 1.6, x=510); b.to(0.6, 1.6, x=570)
two.mark("ck-tip", 2.2)
a.set(2.25, sx=-1); b.set(2.25, sx=1)
a.to(2.3, 1.6, x=300); b.to(2.3, 1.6, x=780)
two.end = 4.0
bounce = scene("toʻqnashuv", two, S("Uchrashsa — ikkalasi orqaga qaytadi", "bk-txt", at=0.2), hold=1.0)

st, clk = stick_stage(40, at=0.6)
chaos = scene("tartibsizlik", st, S("Toʻqnashuv ketidan toʻqnashuv…", "bk-txt", at=0.2), hold=1.2, hud=clk)

VIDEO = Video(
    slug="mj07s", lesson="Mantiq jumbogʻi 7 — savol",
    title="Tayoqdagi chumolilar", story="MJ-07 · savol (javobi: mj07j)",
    subject="logic",
    scenes=[
        cover,
        scene("tayoq", stick_stage(0)[0], S("Har chumoli — 1 sm / soniya", "bk-txt", at=0.2), hold=1.6),
        bounce,
        chaos,
        ask("Qanday boshlashmasin — hammasi eng koʻpi bilan necha soniyada tushadi?",
            head="Eng uzoq vaqt?", dur=6.4, note="Javobni aytmang: 100 soniya — ertaga."),
        fact("Ertaga", "yechimini koʻrsatamiz", cap="Raqamingizni izohga yozing!",
             dark=True, dur=5.0, cam="push"),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Salom, doʻstlar! Sogʻliqlar joyidami? || Bugun — chumolilar jumbogʻi.",
    "Bir metrlik tayoqda chumolilar bor. | Har biri sekundiga bir santimetr yuradi.",
    "Ikki chumoli uchrashsa, | ikkalasi ham orqaga burilib ketadi. | Chetga yetgani — pastga tushadi.",
    "Toʻqnashuv ketidan toʻqnashuv... || [laughs] Boshim aylanib ketdi!",
    "Qanday boshlashmasin, | hammasi eng koʻpi bilan necha soniyada tushadi?",
    "Raqamingizni izohga yozing. || Yechimi — ertaga!",
    None,
])
