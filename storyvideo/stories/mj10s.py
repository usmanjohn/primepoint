# -*- coding: utf-8 -*-
"""MJ-10s — «Ikki eshik, ikki qorovul»   MANTIQ JUMBOGʻI · 10, SAVOL

One door leads to freedom, the other to a lion. One guard always tells the
truth, the other always lies; you don't know which. ONE question to ONE guard.
Today: «which door is freedom?» fails -- the liar would point at the lion.
Tomorrow (mj10j): «which door would the OTHER guard point to?» -- then take the
other door. Gate: verify_batch2.py.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate
from scenes import ask, fact, outro
from _sk import scene, S
from _guards import hall, bubble, point
import stagekit as K

cover = scene("cover", hall(), (S("Mantiq jumbogʻi · 10", "bk-kick", anim="none")
                                + S("1 savol", "bk-hero", anim="none")
                                + S("Qaysi eshik — ozodlik?", "bk-slab", anim="none")), hold=3.4)

st = hall()
naive_q = bubble(st, "«Qaysi eshik ozodlikka?»", 540, 820, 0.5)
point(st, "R", 2.0)
st.tag("rostmi? yolgʻonmi?", 790, 760, 2.8, red=True)
naive = scene("oddiy savol", st, S("1-urinish: oddiy savol", "bk-txt", at=0.0, anim="fade"), hold=1.6)

VIDEO = Video(
    slug="mj10s", lesson="Mantiq jumbogʻi 10 — savol",
    title="Ikki eshik, ikki qorovul", story="MJ-10 · savol (javobi: mj10j)",
    subject="logic",
    scenes=[
        cover,
        scene("eshiklar", hall(), S("Biri — ozodlik, biri — sher", "bk-txt", at=0.2), hold=1.8),
        scene("qorovullar", hall(), S("Biri doim rost gapiradi", "bk-txt bk-grn", at=0.2)
              + S("biri doim yolgʻon", "bk-txt bk-red", at=1.2)
              + S("Qaysi biri — bilmaysiz", "bk-txt", at=2.2), hold=1.4),
        naive,
        scene("bitta savol", hall(), S("Faqat BITTA savol", "bk-slab", at=0.2, anim="pop", dur=0.5), hold=2.0),
        ask("Qanday savol berasiz?", head="Yoʻli bor!", dur=5.4,
            note="Javobni aytmang: «sherigingiz qaysi eshikni koʻrsatardi?» — ertaga."),
        fact("Ertaga", "yechimini koʻrsatamiz", cap="Savolingizni izohga yozing!",
             dark=True, dur=5.0, cam="push"),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Salom, gumbokchalar! Ismlaring yaxshimi? || Bugun — eng mashhur jumboqlardan biri.",
    "Ikki eshik: | biri — ozodlikka, | ikkinchisi — sher qafasiga.",
    "Har birining oldida qorovul. | Biri doim rost gapiradi, ikkinchisi doim yolgʻon. || Qaysi biri ekanini bilmaysiz.",
    "«Qaysi eshik ozodlikka?» deb soʻrasangiz-chi? || Yolgʻonchiga duch kelsangiz — sherga!",
    "Sizda faqat bitta savol bor.",
    "Qanday savol berasiz? || Oʻylab koʻring!",
    "Savolingizni izohga yozing. || Yechimi — ertaga!",
    None,
])
