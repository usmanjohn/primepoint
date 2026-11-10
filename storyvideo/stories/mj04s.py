# -*- coding: utf-8 -*-
"""MJ-04s — «Ikki arqon, 45 daqiqa»   MANTIQ JUMBOGʻI · 4, SAVOL

Two ropes, each burns out in exactly an hour but unevenly; only matches. How to
measure exactly 45 minutes? Today: rope A lit at one end races through its
first half in 10 minutes and crawls through the rest -- cutting it in half
measures nothing. Tomorrow (mj04j): light A at both ends.
Gate: verify_ropes.py (scratchpad) -- profiles sum to 60, half of A = 10 min,
the answer's burn-outs at 30 and 45, A's fronts meet off-centre.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate, Scene
from scenes import ask, fact, outro
import ropekit as RP
import bridgekit as BK

S = BK.say
SPM = 0.12


def ropes(name, lights, m0, m1, msg="", hold=0.8, at=0.6, **kw):
    r = RP.Ropes(lights)
    end = at + (m1 - m0) * SPM
    return Scene(round(end + hold, 2), r.html(m0, m1, at=at, spm=SPM, msg=msg, **kw),
                 cam="hold", name=name)


cover = ropes("cover", [], 0, 0, hold=3.4, msg=(
    S("Mantiq jumbogʻi · 4", "bk-kick", anim="none")
    + S("45 daqiqa", "bk-hero", anim="none")
    + S("Soatsiz qanday oʻlchaysiz?", "bk-slab", anim="none")))
cover.note = "MUQOVA: qorongʻi stol, ikki arqon A va B."

AT = 0.8
demo = ropes("notekis", [(0, "A", "L")], 0, 60, at=AT, hold=1.2, mid=True, msg=(
    S("Yarmi — atigi 10 daqiqa!", "bk-txt bk-red", at=AT + 10 * SPM + 0.1)
    + S("qolgani — 50 daqiqa", "bk-txt", at=AT + 60 * SPM)))

VIDEO = Video(
    slug="mj04s",
    lesson="Mantiq jumbogʻi 4 — savol",
    title="Ikki arqon, 45 daqiqa",
    story="MJ-04 · savol (javobi: mj04j)",
    subject="logic",
    scenes=[
        cover,
        ropes("ikki arqon", [], 0, 0, hold=2.0, msg=S("Har biri — roppa-rosa 1 soat", "bk-txt", at=0.3)),
        ropes("faqat gugurt", [], 0, 0, hold=2.0, msg=(
            S("Faqat gugurt", "bk-hero", at=0.2, anim="pop", dur=0.6)
            + S("soat yoʻq, chizgʻich yoʻq", "bk-txt", at=0.9))),
        demo,
        ask("Qanday qilib aniq 45 daqiqani oʻlchaysiz?", head="Yoʻli bor!", dur=6.0,
            note="Javobni aytmang: ikki uchidan yoqish — ertaga."),
        fact("Ertaga", "yechimini koʻrsatamiz",
             cap="Javobingizni izohga yozing!", dark=True, dur=5.0, cam="push"),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Assalomu alaykum, aqlli boshlar! || Bugun — olov bilan jumboq.",

    "Ikkita arqon bor. | Har biri roppa-rosa bir soatda yonib tugaydi.",

    "Qoʻlingizda faqat gugurt. | Soat ham, chizgʻich ham yoʻq.",

    "Lekin arqon notekis yonadi: | yarmi oʻn daqiqada, qolgani ellik daqiqada. "
    "|| Uni kesish ham yordam bermaydi!",

    "Qanday qilib aniq qirq besh daqiqani oʻlchaysiz? | Oʻylab koʻring!",

    "Javobingizni izohga yozing. || Yechimi — ertaga, xoʻpmi?",

    None,
])
