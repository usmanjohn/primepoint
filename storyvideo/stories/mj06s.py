# -*- coding: utf-8 -*-
"""MJ-06s — «Ming soʻm qayerga ketdi?»   MANTIQ JUMBOGʻI · 6, SAVOL

The missing-dollar riddle, in a choyxona: osh for 30 000, each friend pays
10 000; the choyxonachi gives 5 000 back via the waiter, who keeps 2 000 and
returns 1 000 each. 3 × 9 000 = 27 000, + 2 000 = 29 000. Where is 1 000?
Tomorrow (mj06j): nowhere -- the 2 000 is already inside the 27 000.
Gate: verify_batch2.py (scratchpad).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate
from scenes import ask, fact, outro
from _sk import scene, S
from _som import room, FRIENDS, OWNER, WAITER, FEET
import stagekit as K

TOP = FEET - 300


def base(step):
    """step 0: before paying; 1: paid; 2: 5 000 to the waiter; 3: change returned."""
    st = K.Stage()
    room(st)
    tens = [st.add(K.bill("10 000", 170, 80), x, TOP, 170, 80, z=5) for _, x in FRIENDS]
    if step >= 1:
        T = 0.5 if step == 1 else -500
        for i, b in enumerate(tens):
            b.to(T + i * 0.35, 0.8, x=OWNER[1] + (i - 1) * 24, y=FEET - 160 - i * 14, s=0.7)
            if step == 1:
                st.mark("ck-drop", T + i * 0.35 + 0.8)
        st.end = max(st.end, 2.2 if step == 1 else 0.5)
    if step >= 2:
        five = st.add(K.bill("5 000", 170, 80), OWNER[1], FEET - 180, 170, 80, z=6, o=0)
        T = 0.5 if step == 2 else -400
        five.set(T, o=1)
        five.to(T + 0.3, 0.9, x=WAITER[1], y=TOP)
        if step == 2:
            st.mark("rp-light", T + 0.3); st.end = max(st.end, 1.8)
    if step >= 3:
        five.to(0.4, 0.3, o=0)
        two = st.add(K.bill("2 000"), WAITER[1], TOP, 190, 90, z=6, o=0)
        two.set(0.4, o=1)
        two.to(1.0, 0.6, y=FEET - 120, s=0.6)
        st.tag("choʻntakka!", WAITER[1], FEET - 300, 1.4, red=True)
        for i, (_, x) in enumerate(FRIENDS):
            one = st.add(K.bill("1 000"), WAITER[1], TOP, 170, 80, z=6, o=0)
            one.set(1.8 + i * 0.4, o=1)
            one.to(1.8 + i * 0.4, 0.7, x=x, y=TOP - 40)
            st.mark("ck-drop", 2.5 + i * 0.4)
        st.end = max(st.end, 3.6)
    return st


cover = scene("cover", base(0), (S("Mantiq jumbogʻi · 6", "bk-kick", anim="none")
                                 + S("1 000 soʻm", "bk-hero", anim="none")
                                 + S("Qayerga ketdi?", "bk-slab", anim="none")), hold=3.4)

sumst = K.Stage()
sumst.end = 4.6
total = scene("hisob", sumst, (S("Har biri: 10 000 − 1 000 = 9 000", "bk-txt", at=0.3)
                               + S("9 000 × 3 = 27 000", "bk-txt", at=1.3)
                               + S("27 000 + 2 000 = 29 000", "bk-txt", at=2.4)
                               + S("1 000 qayerda?!", "bk-hero bk-red", at=3.6, anim="stamp", dur=0.6)),
              hold=2.2)

VIDEO = Video(
    slug="mj06s", lesson="Mantiq jumbogʻi 6 — savol",
    title="Ming soʻm qayerga ketdi?", story="MJ-06 · savol (javobi: mj06j)",
    subject="logic",
    scenes=[
        cover,
        scene("toʻlov", base(1), S("Osh — 30 000 soʻm", "bk-txt", at=0.2)),
        scene("chegirma", base(2), S("Chegirma: 25 000!", "bk-txt bk-grn", at=0.2), hold=1.2),
        scene("qaytim", base(3), S("2 000 — choʻntakka, 3 × 1 000 — qaytim", "bk-txt", at=0.2), hold=1.0),
        total,
        ask("Ming soʻm qayerga ketdi?", head="Qani, hisobchilar?", dur=5.6,
            note="Javobni aytmang: hech qayerga — savol notoʻgʻri qoʻshgan. Ertaga."),
        fact("Ertaga", "yechimini koʻrsatamiz", cap="Javobingizni izohga yozing!",
             dark=True, dur=5.0, cam="push"),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Assalomu alaykum, yapaloqqushlar! || Bugun — pul jumbogʻi.",
    "Uch doʻst choyxonada osh yedi. | Hisob — oʻttiz ming soʻm, | har biri oʻn mingdan berdi.",
    "Choyxonachi: «Bugun chegirma — yigirma besh ming!» | Besh mingni qaytarishni buyurdi.",
    "Ofitsiant ikki mingni choʻntagiga soldi, | har biriga mingtadan qaytardi.",
    "Demak, har biri toʻqqiz mingdan toʻladi — | yigirma yetti ming. | Ofitsiantda ikki ming. || Jami — yigirma toʻqqiz ming!",
    "Unda ming soʻm qayerga ketdi? || Oʻylab koʻring!",
    "Javobingizni izohga yozing. || Yechimi — ertaga!",
    None,
])
