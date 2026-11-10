# -*- coding: utf-8 -*-
"""MJ-06j — «Ming soʻm: javob — hech qayerga ketmagan»   MANTIQ JUMBOGʻI · 6, JAVOB

Follow the money: choyxonachi 25 000, waiter 2 000, friends 3 000 = 30 000.
The 27 000 the friends paid already CONTAINS the waiter's 2 000
(27 000 = 25 000 + 2 000), so adding it again counts it twice. The right sums:
27 000 − 2 000 = 25 000, or 27 000 + 3 000 = 30 000.
Gate: verify_batch2.py (scratchpad).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate, Scene
from scenes import check, rule, ask, practice, outro
from _sk import scene, S
from _som import room, FRIENDS, OWNER, WAITER, FEET
import stagekit as K
import primitives as P


def piles(anim=True):
    st = K.Stage()
    room(st)
    at = 0.6 if anim else -500
    spots = [(OWNER[1], "25 000"), (WAITER[1], "2 000")] + [(x, "1 000") for _, x in FRIENDS]
    for i, (x, amt) in enumerate(spots):
        b = st.add(K.bill(amt, 165, 78), x, FEET - 330, 165, 78, z=5, o=0, s=0.6)
        b.to(at + i * 0.6, 0.4, o=1, s=1.0)
        if anim:
            st.mark("ck-drop", at + i * 0.6 + 0.4)
    st.end = max(st.end, at + 5 * 0.6 + 0.4)
    hud = K.counter("Jami", [(at + i * 0.6 + 0.4, v) for i, v in
                             enumerate([25, 27, 28, 29, 30])], "ming soʻm")
    return st, hud


st, hud = piles(anim=False)
cover = scene("cover", st, (S("Mantiq jumbogʻi · 6 · javob", "bk-kick", anim="none")
                            + S("Hech qayerga!", "bk-hero sk-hero2 bk-grn", anim="none")
                            + S("Savol notoʻgʻri qoʻshgan", "bk-slab", anim="none")), hold=3.4, hud=hud)

st, hud = piles()
follow = scene("pulni kuzatamiz", st, S("Pulni kuzatamiz", "bk-txt", at=0.0, anim="fade"),
               hold=1.4, hud=hud)

inside = Scene(
    8.0,
    P.line("27 000 ning ichida nima bor?", "ttl", at=0.0, anim="rise", dur=0.6)
    + P.solve([("25 000", "choyxonachida"), ("2 000", "ofitsiantda")], at=1.2, step=0.9)[0]
    + P.line("2 000 allaqachon ichida!", "ttl red", at=3.4, anim="pop", dur=0.6),
    cam="push", name="ichida", claims=["25 000 + 2 000 = 27 000"])

VIDEO = Video(
    slug="mj06j", lesson="Mantiq jumbogʻi 6 — javob",
    title="Ming soʻm: javob — hech qayerga ketmagan", story="MJ-06 · javob (savoli: mj06s)",
    subject="logic",
    scenes=[
        cover,
        scene("eslatma", K.Stage(), S("Kecha: 27 000 + 2 000 = 29 000", "bk-txt", at=0.2)
              + S("1 000 yoʻqoldimi?", "bk-hero bk-red", at=1.0, anim="pop", dur=0.6), hold=2.2),
        follow,
        inside,
        check("27 000 + 3 000 = 30 000", parts=["27 000 − 2 000 = 25 000",
                                              "27 000 + 2 000 — ikki marta sanash"],
              verdict="Hech narsa yoʻqolmagan!", title="Toʻgʻri hisob", dur=8.0),
        rule("Savolning oʻzi xato boʻlishi mumkin",
             meaning="Raqamni emas — u nimani anglatishini tekshiring.", dur=7.4),
        ask("Shunday «yoʻqolgan pul» jumbogʻini yana bilasizmi?", head="Izohda yozing",
            dur=5.6),
        practice("Mantiq maydoni", sub="powerty.uz → Mantiq maydoni", dur=5.0),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Xayrli tong, hisobchilar! || Ming soʻm hech qayerga ketmagan!",
    "Kecha: yigirma yetti ming plyus ikki ming — yigirma toʻqqiz ming. | Ming soʻm yoʻqoldimi?",
    "Pulni kuzatamiz: | choyxonachida yigirma besh ming, | ofitsiantda ikki ming, | doʻstlarda uch ming.",
    "Doʻstlar toʻlagan yigirma yetti mingning ichida | ofitsiantning ikki mingi allaqachon bor!",
    "Uni yana qoʻshish — ikki marta sanash. || Toʻgʻrisi: yigirma yetti ming plyus uch ming — oʻttiz ming.",
    "Qoida: | baʼzan savolning oʻzi xato boʻladi.",
    "Shunday jumboqni yana bilasizmi? || Izohda yozing!",
    "Har hafta yangi jumboqlar — Powertyda, Mantiq maydonida.",
    None,
])
