# -*- coding: utf-8 -*-
"""MJ-08s — «Besh qaroqchi va yuz tanga»   MANTIQ JUMBOGʻI · 8, SAVOL

Five ranked pirates, 100 gold coins. The captain proposes a split, everyone
votes; at least half in favour (his own vote counts) -> accepted, otherwise he
goes overboard and the next proposes. Pirates are clever, greedy, and when it
makes no difference to their gold, they prefer a splash. Today: «all for me»
gets one vote and a splash. Tomorrow (mj08j): backward induction, 98-0-1-0-1.
Gate: verify_batch2.py + _pir.split (same induction, asserted).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate
from scenes import ask, fact, outro
from _sk import scene, S
from _pir import deck

cover = scene("cover", deck(), (S("Mantiq jumbogʻi · 8", "bk-kick", anim="none")
                                + S("100 tanga", "bk-hero", anim="none")
                                + S("Kapitan qancha oladi?", "bk-slab", anim="none")), hold=3.4)

VIDEO = Video(
    slug="mj08s", lesson="Mantiq jumbogʻi 8 — savol",
    title="Besh qaroqchi va yuz tanga", story="MJ-08 · savol (javobi: mj08j)",
    subject="logic",
    scenes=[
        cover,
        scene("qoida", deck(), S("Kapitan taklif qiladi — hamma ovoz beradi", "bk-txt", at=0.2)
              + S("Yarmi «ha» desa — qabul", "bk-txt bk-grn", at=1.4)
              + S("Aks holda — dengizga!", "bk-txt bk-red", at=2.6), hold=1.6),
        scene("feʼl", deck(), S("Aqlli · ochkoʻz · rahmsiz", "bk-slab", at=0.3, anim="pop"), hold=2.0),
        scene("hammasi menga", deck(alloc=[100, 0, 0, 0, 0], votes=[1, 0, 0, 0, 0], overboard=True),
              S("«Hammasi menga!»", "bk-txt", at=0.2), hold=1.2),
        ask("Kapitan qanday boʻlsa, ham tirik qoladi, ham eng koʻp oladi?",
            head="Siz qanday boʻlardingiz?", dur=6.2, note="Javobni aytmang: 98 — ertaga."),
        fact("Ertaga", "yechimini koʻrsatamiz", cap="Taqsimotingizni izohga yozing!",
             dark=True, dur=5.0, cam="push"),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Salom, oshqovoqchalar! || Bugun — qaroqchilar jumbogʻi. | Bu juda qiyin!",
    "Beshta qaroqchi yuzta oltin tanga topdi. | Kapitan boʻlishni taklif qiladi, hamma ovoz beradi. "
    "|| Yarmi rozi boʻlsa — qabul, | boʻlmasa — kapitan dengizga!",
    "Ular aqlli, ochkoʻz va rahmsiz: | teng boʻlsa — dengizga otishni afzal koʻradi.",
    "Kapitan: «Hammasi menga!» || Bitta ovoz... | [laughs] Toʻppa-toʻgʻri dengizga!",
    "Kapitan qanday boʻlsa, | ham tirik qoladi, ham eng koʻp oladi?",
    "Taqsimotingizni izohga yozing. || Yechimi — ertaga!",
    None,
])
