# -*- coding: utf-8 -*-
"""MJ-09s — «Qorongʻida yuz tanga»   MANTIQ JUMBOGʻI · 9, SAVOL

100 coins on a table, exactly 10 heads up. Blindfolded -- you can neither see
nor feel which side is up -- split them into two piles with the SAME number of
heads. Today: splitting 50/50 is a gamble (6 vs 4 here). Tomorrow (mj09j):
take any 10, flip all of them. Gate: verify_batch2.py.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate
from scenes import ask, fact, outro
from _sk import scene, S
from _dark import Coins, HEADS
import stagekit as K


def table(appear=None, blind=False, halves=False):
    st = K.Stage()
    Coins(st, appear=appear)
    if appear is not None:
        st.end = appear + 1.2
    if blind:
        cur = st.add('<div class="sk-blind" data-backdrop></div>', 540, 960, 1080, 1920, z=9, o=0)
        cur.to(0.6, 0.8, o=0.93)
        st.end = 1.6
    if halves:
        st.add('<div class="sk-cut"></div>', 540, 1189, 8, 860, z=5, o=0).to(0.4, 0.4, o=1)
        left = sum(1 for i in HEADS if i % 10 < 5)
        st.tag(f"{left} ta", 335, 790, 1.4, red=True)
        st.tag(f"{10 - left} ta", 745, 790, 1.8, red=True)
        st.end = 2.4
    return st


cover = scene("cover", table(), (S("Mantiq jumbogʻi · 9", "bk-kick", anim="none")
                                 + S("100 tanga", "bk-hero", anim="none")
                                 + S("Koʻzingiz bogʻliq", "bk-slab", anim="none")), hold=3.4)

VIDEO = Video(
    slug="mj09s", lesson="Mantiq jumbogʻi 9 — savol",
    title="Qorongʻida yuz tanga", story="MJ-09 · savol (javobi: mj09j)",
    subject="logic",
    scenes=[
        cover,
        scene("yuz tanga", table(appear=0.4), S("10 tasi — gerb ★ tomoni bilan", "bk-txt", at=0.2), hold=1.4),
        scene("koʻz bogʻliq", table(blind=True), S("Koʻrmaysiz · paypaslab ham bilmaysiz", "bk-txt", at=1.2), hold=1.4),
        scene("vazifa", table(), S("Ikki toʻda — gerb soni teng boʻlsin", "bk-slab", at=0.3, anim="pop"), hold=2.6),
        scene("yarmidan", table(halves=True), S("Teng ikkiga boʻlsak?", "bk-txt", at=0.0, anim="fade")
              + S("Kafolat yoʻq!", "bk-hero bk-red", at=2.4, anim="pop", dur=0.5), hold=2.0),
        ask("Koʻrmasdan qanday qilib teng qilasiz?", head="Yoʻli bor!", dur=5.8,
            note="Javobni aytmang: istalgan 10 tasini ajratib, hammasini aylantirish — ertaga."),
        fact("Ertaga", "yechimini koʻrsatamiz", cap="Javobingizni izohga yozing!",
             dark=True, dur=5.0, cam="push"),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Salom, aqlli boshlar! || Bugungi jumboq — qorongʻida.",
    "Stolda yuzta tanga. | Oʻntasi gerb tomoni bilan yuqoriga qarab turibdi.",
    "Koʻzingiz bogʻlangan: | tangalarni koʻrmaysiz, | paypaslab ham bilmaysiz.",
    "Vazifa: tangalarni ikki toʻdaga ajrating — | ikkalasida gerb soni teng boʻlsin.",
    "Teng ikkiga boʻlsak-chi? | Omad kulsa — balki. || Lekin kafolat yoʻq!",
    "Koʻrmasdan qanday qilib teng qilasiz? || Oʻylab koʻring!",
    "Javobingizni izohga yozing. || Yechimi — ertaga!",
    None,
])
