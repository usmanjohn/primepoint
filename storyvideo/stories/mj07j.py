# -*- coding: utf-8 -*-
"""MJ-07j — «Chumolilar: javob — 100 soniya»   MANTIQ JUMBOGʻI · 7, JAVOB

Two ants that bounce look exactly like two ants that walk THROUGH each other --
only the names swap. So forget the collisions: every ant just walks straight,
and the slowest possible is one walking the whole metre: 100 s. The same
starting position as yesterday, replayed with ghost ants walking straight above
the real ones: the last real ant falls exactly when the last ghost does (94 s).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate
from scenes import rule, ask, practice, outro
from _sk import scene, S
from _ants import stick_stage, last_fall
import stagekit as K

T = last_fall()
st, clk = stick_stage(T)
cover = scene("cover", st, (S("Mantiq jumbogʻi · 7 · javob", "bk-kick", anim="none")
                            + S("100 soniya", "bk-hero bk-grn", anim="none")
                            + S("Sir — ular «oʻtib ketadi»", "bk-slab", anim="none")), hold=3.4)


def pair(swap):
    st = K.Stage()
    st.add('<div class="sk-stick"></div>', 540, 1262, 900, 24)
    a = st.add(K.ant(col="#a23b2a"), 300, 1240, 56, 34, s=1.6)
    b = st.add(K.ant(), 780, 1240, 56, 34, s=1.6)
    b.set(-900, sx=-1)
    a.to(0.6, 1.6, x=510); b.to(0.6, 1.6, x=570)
    if swap:          # pass through: each keeps walking the same way
        a.to(2.2, 1.6, x=780); b.to(2.2, 1.6, x=300)
    else:
        a.set(2.25, sx=-1); b.set(2.25, sx=1)
        a.to(2.3, 1.6, x=300); b.to(2.3, 1.6, x=780)
    st.end = 4.0
    return st


st, clk = stick_stage(T, at=0.6, ghosts=True)
replay = scene("arvohlar", st, S("Koʻk — «oʻtib ketuvchi» chumolilar", "bk-txt", at=0.2)
               + S(f"Oxirgisi — {T} soniyada", "bk-txt bk-grn", at=0.6 + T * 0.075 + 0.2), hold=1.6, hud=clk)

VIDEO = Video(
    slug="mj07j", lesson="Mantiq jumbogʻi 7 — javob",
    title="Chumolilar: javob — 100 soniya", story="MJ-07 · javob (savoli: mj07s)",
    subject="logic",
    scenes=[
        cover,
        scene("qaytadi", pair(False), S("Qaytadi…", "bk-txt", at=0.2), hold=0.8),
        scene("oʻtib ketadi", pair(True), S("…yoki oʻtib ketadi?", "bk-txt", at=0.2)
              + S("Rangsiz — farqi yoʻq!", "bk-slab", at=3.9, anim="pop", dur=0.5), hold=1.6),
        replay,
        scene("eng uzoq", stick_stage(0)[0], S("Eng uzoq yoʻl — butun tayoq", "bk-txt", at=0.2)
              + S("100 sm ÷ 1 sm/s = 100 s", "bk-slab", at=1.0, anim="pop", dur=0.6), hold=2.4),
        rule("Murakkab koʻrinsa — boshqa koʻz bilan qarang",
             meaning="Toʻqnashuvni «oʻtib ketish» deb koʻrsangiz, jumboq yoʻqoladi.", dur=7.6),
        ask("Chumolilar 1000 ta boʻlsa-chi?", head="Endi siz", dur=5.6,
            note="Javob: baribir 100 soniya."),
        practice("Mantiq maydoni", sub="powerty.uz → Mantiq maydoni", dur=5.0),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Xayrli tong, aqlli boshlar! || Javob: eng koʻpi bilan yuz soniya!",
    "Ikki chumoli uchrashib, orqaga qaytdi...",
    "Endi tasavvur qiling: ular bir-biridan oʻtib ketdi. || Rangini olib tashlasangiz — farqi yoʻq!",
    "Demak, toʻqnashuvni unuting: | har bir chumoli toʻgʻri yuradi, | xuddi koʻk chumolilardek.",
    "Eng uzoq yoʻl — tayoqning bir chetidan ikkinchisiga: | yuz santimetr, yuz soniya.",
    "Qoida: | murakkab koʻrinsa — boshqa koʻz bilan qarang.",
    "Endi siz: | chumolilar ming ta boʻlsa-chi? || Izohda yozing!",
    "Har hafta yangi jumboqlar — Powertyda, Mantiq maydonida.",
    None,
])
