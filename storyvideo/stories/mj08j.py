# -*- coding: utf-8 -*-
"""MJ-08j — «Qaroqchilar: javob — 98 tanga»   MANTIQ JUMBOGʻI · 8, JAVOB

Backward induction, one pirate at a time from the end: 2 left -> 100-0;
3 -> 99-0-1; 4 -> 99-0-1-0; 5 -> 98-0-1-0-1 (pirates 3 and 5 vote yes, because
one coin beats the nothing they would get otherwise). Ask: six pirates? (98.)
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate, Scene
from scenes import rule, ask, practice, outro
from _sk import scene, S
from _pir import deck, split
import primitives as P


def stage_n(n, hold=1.0, msg=""):
    a = split(n)
    votes = [1] + [1 if a[i] > split(n - 1)[i - 1] else 0 for i in range(1, n)]
    return scene(f"{n} qaroqchi", deck(n_from=5 - n, alloc=a, votes=votes), msg, hold=hold)


A5 = split(5)
cover = scene("cover", deck(alloc=A5, votes=[1, 0, 1, 0, 1], at=-50),
              (S("Mantiq jumbogʻi · 8 · javob", "bk-kick", anim="none")
               + S("98 tanga!", "bk-hero bk-grn", anim="none")
               + S("Sir — oxiridan boshlang", "bk-slab", anim="none")), hold=3.4)

secret = Scene(
    6.6,
    P.line("Sir", "lbl lbl--sm", at=0.0, anim="fade")
    + P.line("Oxiridan boshlab oʻylang", "ttl", at=0.4, anim="rise", dur=0.6)
    + P.line("2 → 3 → 4 → 5 qaroqchi", "big gold", at=1.8, anim="pop", dur=0.6),
    cam="push", dark=True, name="sir")

VIDEO = Video(
    slug="mj08j", lesson="Mantiq jumbogʻi 8 — javob",
    title="Qaroqchilar: javob — 98 tanga", story="MJ-08 · javob (savoli: mj08s)",
    subject="logic",
    scenes=[
        cover,
        scene("eslatma", deck(), S("Kecha: «hammasi menga» → dengizga", "bk-txt", at=0.2), hold=1.6),
        secret,
        stage_n(2, msg=S("Ikkita qolsa", "bk-txt", at=0.0, anim="fade")),
        stage_n(3, msg=S("Uchta qolsa", "bk-txt", at=0.0, anim="fade")),
        stage_n(4, msg=S("Toʻrtta qolsa", "bk-txt", at=0.0, anim="fade")),
        stage_n(5, hold=1.6, msg=S("Beshta — hammasi", "bk-txt", at=0.0, anim="fade")),
        rule("Murakkab qarorda — oxiridan orqaga yuring",
             meaning="Shaxmatchilar ham, iqtisodchilar ham shunday oʻylaydi.", dur=7.4),
        ask("Qaroqchilar 6 ta boʻlsa-chi? Kapitan qancha oladi?", head="Endi siz", dur=5.8,
            note="Javob: yana 98 (98-0-1-0-1-0)."),
        practice("Mantiq maydoni", sub="powerty.uz → Mantiq maydoni", dur=5.0),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Xayrli tong, qaroqchilar! || Javob: kapitan toʻqson sakkiz tanga oladi!",
    "Kecha kapitan «hammasi menga» dedi — va dengizga uchdi.",
    "Sir: | oxiridan boshlab oʻylang.",
    "Faqat ikkitasi qolsa: | toʻrtinchi hammasini oladi. || Uning bitta ovozi — yarmi.",
    "Uchta qolsa: | uchinchi beshinchiga bitta tanga beradi. | Aks holda u hech narsa olmaydi.",
    "Toʻrtta qolsa: | ikkinchi toʻrtinchiga bitta tanga beradi.",
    "Beshta: | kapitan uchinchi va beshinchiga bittadan beradi. || Uch ovoz — qabul! Kapitanga — toʻqson sakkiz!",
    "Qoida: | murakkab qarorda — oxiridan orqaga yuring.",
    "Endi siz: | qaroqchilar oltita boʻlsa, kapitan qancha oladi? || Izohda yozing!",
    "Har hafta yangi jumboqlar — Powertyda, Mantiq maydonida.",
    None,
])
