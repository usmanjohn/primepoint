# -*- coding: utf-8 -*-
"""MJ-05s — «Ming shisha, bitta uyqu dori»   MANTIQ JUMBOGʻI · 5, SAVOL

1000 bottles, one with a sleeping draught that acts after 24 hours; the feast
is tomorrow. Fewest mice to find it in ONE round? Today: one mouse per bottle
(1000) and halving (10 days) both fail. Tomorrow (mj05j): 10 mice, binary.
Gate: verify_batch2.py (scratchpad).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate
from scenes import ask, fact, outro
from _sk import scene, bottle_grid, S
import stagekit as K


def grid_scene(name, msg, anim="rise", hold=1.5):
    st = K.Stage()
    st.extra.append(bottle_grid(at=0.4, anim=anim))
    st.end = 0.4 + 25 * 0.05 + 0.3
    return scene(name, st, msg, hold)


cover = grid_scene("cover", (S("Mantiq jumbogʻi · 5", "bk-kick", anim="none")
                             + S("1000 shisha", "bk-hero sk-hero2", anim="none")
                             + S("Bittasida — uyqu dori", "bk-slab", anim="none")),
                   anim="none", hold=3.0)

# a mouse drinks, a day passes, it falls asleep
st = K.Stage()
b = st.add(K.bottle(), 220, 1180, 70, 150, s=1.7)
awake = st.add(K.mouse(), 560, 1260, 150, 110, s=2.6)
sleep = st.add(K.mouse(asleep=True), 560, 1260, 150, 110, s=2.6, o=0)
z = st.add(K.zzz(), 900, 1020, 120, 70, o=0, s=1.6)
st.mark("ck-drop", 1.0)
awake.to(3.0, 0.4, o=0); sleep.to(3.0, 0.4, o=1); z.to(3.3, 0.5, o=1, y=960)
st.mark("ck-tip", 3.0); st.end = 4.0
drink = scene("24 soat", st, S("24 soatdan keyin — uxlab qoladi", "bk-txt", at=0.3)
              + S("Bazm — ertaga!", "bk-hero bk-red", at=4.2, anim="stamp", dur=0.6), hold=1.6)

# naive 1: a mouse per bottle
st = K.Stage()
for i in range(48):
    m = st.add(K.mouse(), 130 + (i % 8) * 118, 900 + (i // 8) * 110, 150, 110, s=0.62, o=0)
    m.to(0.5 + i * 0.05, 0.25, o=1)
st.end = 3.2
many = scene("1000 sichqon", st, S("1000 ta sichqon?!", "bk-hero bk-red", at=3.0, anim="pop", dur=0.5),
             hold=2.0, hud=K.counter("Sichqon", [(0.5, 0), (3.0, 1000)]))

# naive 2: halve every day
halve = grid_scene("yarmidan", (S("Yarmini tekshirsak?", "bk-txt", at=0.2, anim="fade")
                                + S("1000 → 500 → 250 → 125 → 63", "bk-txt", at=1.0)
                                + S("→ 32 → 16 → 8 → 4 → 2 → 1", "bk-txt", at=2.0)
                                + S("10 kun!", "bk-hero bk-red", at=3.4, anim="stamp", dur=0.6)),
                   anim="none", hold=2.4)

VIDEO = Video(
    slug="mj05s", lesson="Mantiq jumbogʻi 5 — savol",
    title="Ming shisha, bitta uyqu dori", story="MJ-05 · savol (javobi: mj05j)",
    subject="logic",
    scenes=[
        cover,
        grid_scene("ming shisha", S("Podsho saroyida — 1000 shisha sharbat", "bk-txt", at=0.0, anim="fade")),
        drink, many, halve,
        ask("Bir kunda topish uchun eng kamida nechta sichqon kerak?", head="Siz nechta deysiz?",
            dur=6.0, note="Javobni aytmang: 10 — ertaga."),
        fact("Ertaga", "yechimini koʻrsatamiz", cap="Raqamingizni izohga yozing!",
             dark=True, dur=5.0, cam="push"),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Salom, gumbokchalar! || Bugungi jumboq — chinakam qiyin.",
    "Podsho saroyida ming shisha sharbat. | Bittasiga uyqu dori qoʻshilgan.",
    "Dori yigirma toʻrt soatdan keyin taʼsir qiladi: | ichgan sichqon uxlab qoladi. || Bazm esa — ertaga!",
    "Har shishaga bittadan sichqonmi? | Ming sichqon! || [laughs] Saroy sichqonxonaga aylanadi.",
    "Yarmini, keyin yarmining yarmini tekshirsak-chi? | Oʻn kun ketadi.",
    "Bir kunda topish uchun eng kamida nechta sichqon kerak? || Oʻylab koʻring!",
    "Raqamingizni izohga yozing. || Yechimi — ertaga!",
    None,
])
