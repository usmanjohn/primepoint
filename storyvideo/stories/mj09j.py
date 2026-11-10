# -*- coding: utf-8 -*-
"""MJ-09j — «Qorongʻida yuz tanga: javob — 10 tasini aylantiring»   MANTIQ JUMBOGʻI · 9, JAVOB

Take ANY 10 coins aside. If k of them are heads, the other 90 hold 10 − k.
Flip all ten: they now hold 10 − k heads. Equal, without ever knowing k.
Shown with k = 3 (the seed in _dark.py is chosen for it), counters on both piles.
Ask: 20 heads among 100? (take 20, flip them.) Gate: verify_batch2.py.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate, Scene
from scenes import rule, ask, practice, outro
from _sk import scene, S
from _dark import Coins, HEADS, PICK, row_pos
import stagekit as K
import primitives as P

K_IN = len(set(PICK) & HEADS)


def table(step, hud=True):
    """0 = all on table; 1 = ten taken aside; 2 = ten flipped."""
    st = K.Stage()
    c = Coins(st)
    big = [(0, 10)]
    small = [(0, 0)]
    if step >= 1:
        T = 0.5 if step == 1 else -500
        for k, i in enumerate(PICK):
            c.move(i, T + k * 0.12, *row_pos(k))
        st.end = max(st.end, T + 10 * 0.12 + 0.6)
        big, small = [(T + 1.8, 10 - K_IN)], [(T + 1.8, K_IN)]
    if step >= 2:
        for k, i in enumerate(PICK):
            c.flip(i, 0.6 + k * 0.18)
        st.end = max(st.end, 0.6 + 10 * 0.18 + 0.6)
        small = [(-1, K_IN), (2.6, 10 - K_IN)]
    h = ""
    if hud:
        h = (K.counter("Katta toʻp", big, "gerb", y=70)
             + K.counter("10 talik", small, "gerb", y=200))
    return st, h


# the cover must show the finished state at t=0
st0, h0 = table(2)
for t in st0.things:
    for k in t.tr:
        t.tr[k] = [[kk - 100 if kk > -900 else kk, v] for kk, v in t.tr[k]]
st0.extra = []; st0.end = 0.5
cover = scene("cover", st0, (S("Mantiq jumbogʻi · 9 · javob", "bk-kick", anim="none")
                             + S("Aylantiring!", "bk-hero bk-grn", anim="none")
                             + S("Istalgan 10 tasini", "bk-slab", anim="none")), hold=3.4,
              hud=K.counter("Katta toʻp", [(0, 10 - K_IN)], "gerb", y=70)
              + K.counter("10 talik", [(0, 10 - K_IN)], "gerb", y=200))

st, h = table(1)
aside = scene("ajrating", st, S("Istalgan 10 tasini ajrating", "bk-txt", at=0.0, anim="fade"), hold=1.4, hud=h)
st, h = table(2)
flip = scene("aylantiring", st, S("…va hammasini aylantiring!", "bk-txt", at=0.0, anim="fade")
             + S("7 = 7", "bk-hero bk-grn", at=2.8, anim="stamp", dur=0.6), hold=1.6, hud=h)

why = Scene(
    8.0,
    P.line("Nega har doim ishlaydi?", "ttl", at=0.0, anim="rise", dur=0.6)
    + P.solve([("k ta", "10 talikdagi gerb"), ("10 − k", "katta toʻpdagi gerb"),
               ("10 − k", "aylantirgandan keyin 10 talikda")], at=1.0, step=1.0)[0],
    cam="push", name="nega")

VIDEO = Video(
    slug="mj09j", lesson="Mantiq jumbogʻi 9 — javob",
    title="Qorongʻida yuz tanga: javob", story="MJ-09 · javob (savoli: mj09s)",
    subject="logic",
    scenes=[
        cover,
        scene("eslatma", table(0, hud=False)[0], S("Kecha: teng ikkiga boʻlish — omadga bogʻliq", "bk-txt", at=0.2), hold=1.6),
        aside, flip, why,
        rule("Nechtaligini bilish shart emas — tuzilma yetadi",
             meaning="Qaysi tanga gerb ekanini bilmay turib ham — tenglik kafolatlangan.", dur=7.4),
        ask("100 tadan 20 tasi gerb boʻlsa-chi?", head="Endi siz", dur=5.6,
            note="Javob: istalgan 20 tasini ajratib, hammasini aylantirish."),
        practice("Mantiq maydoni", sub="powerty.uz → Mantiq maydoni", dur=5.0),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Xayrli tong, sehrgarlar! || Javob — juda oddiy va juda chiroyli.",
    "Kecha: teng ikkiga boʻlish faqat omadga bogʻliq edi.",
    "Istalgan oʻnta tangani ajrating. | Masalan, ichida uchta gerb bor — | qolganlarida yettita.",
    "Endi oʻsha oʻntaning hammasini aylantiring! || Uchta gerb — pastga, | yettita raqam — gerbga. | Yettiga yetti!",
    "Ajratilganda nechta gerb boʻlsa ham, | aylantirgandan keyin qolganlari bilan teng boʻladi.",
    "Qoida: | nechtaligini bilish shart emas — | tuzilma yetadi.",
    "Endi siz: | gerb yigirmata boʻlsa-chi? || Izohda yozing!",
    "Har hafta yangi jumboqlar — Powertyda, Mantiq maydonida.",
    None,
])
