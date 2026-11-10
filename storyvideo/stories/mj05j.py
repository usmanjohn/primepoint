# -*- coding: utf-8 -*-
"""MJ-05j — «Ming shisha: javob — 10 ta sichqon»   MANTIQ JUMBOGʻI · 5, JAVOB

Shown small first: 8 bottles numbered 0-7 in binary, 3 mice. Mouse A drinks from
every bottle whose FIRST digit is 1, B the second, C the third. Bottle 5 = 101:
A and C fall asleep, B does not -> read 1 0 1 = 5. Each mouse doubles what can
be told apart: 10 mice -> 1024 >= 1000. Ask: two days? (7 mice, 3^7 = 2187.)
Gate: verify_batch2.py (scratchpad).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate, Scene
from scenes import rule, ask, practice, outro
from _sk import scene, S
import stagekit as K
import primitives as P

POISON = 5
BX = [120 + i * 120 for i in range(8)]
MX = {"A": 250, "B": 540, "C": 830}
DIGIT = {"A": 2, "B": 1, "C": 0}            # which binary digit each mouse tastes


def lab(i):
    return format(i, "03b")


def lab_html(i, mouse=None):
    if not mouse:
        return lab(i)
    k = 2 - DIGIT[mouse]
    s = lab(i)
    return s[:k] + f'<span class="gold">{s[k]}</span>' + s[k + 1:]


def demo(stage_upto, name, msg="", hold=0.8):
    """stage_upto: 0 = set out, 1 = mice drink, 2 = next morning."""
    st = K.Stage()
    bots = [st.add(K.bottle(lab(i), poison=False), BX[i], 820, 70, 150) for i in range(8)]
    awake, asleep = {}, {}
    for m, x in MX.items():
        awake[m] = st.add(K.mouse(), x, 1380, 150, 110, s=1.15)
        asleep[m] = st.add(K.mouse(asleep=True), x, 1380, 150, 110, s=1.15, o=0)
        st.extra.append(f'<div class="ck-tag ck-tag--eq" style="left:{x}px;top:1300px" '
                        f'data-at="0.000" data-dur="0.01" data-anim="none"><span>{m}</span></div>')
    t = 0.5
    if stage_upto >= 1:
        T = 0.4 if stage_upto == 1 else -500
        for m in "ABC":
            for i in range(8):
                if (i >> DIGIT[m]) & 1:
                    d = st.add('<i class="sk-drop"></i>', BX[i], 760, 26, 26, o=0)
                    d.set(T, o=1)
                    d.to(T + 0.02, 0.5, x=MX[m], y=1330)
                    d.to(T + 0.52, 0.15, o=0)
                    st.mark("ck-drop", T + 0.5) if stage_upto == 1 else None
                    T += 0.12
            T += 0.35
        t = max(t, T)
    if stage_upto >= 2:
        for m in "ABC":
            if (POISON >> DIGIT[m]) & 1:
                awake[m].to(0.6, 0.4, o=0)
                asleep[m].to(0.6, 0.4, o=1)
                z = st.add(K.zzz(), MX[m] + 105, 1290, 120, 70, o=0)
                z.to(0.9, 0.4, o=1)
        st.mark("ck-tip", 0.6)
        for j, m in enumerate("ABC"):
            bit = (POISON >> DIGIT[m]) & 1
            st.extra.append(f'<div class="sk-t" style="transform:translate({MX[m]}px,1530px)">'
                            f'<div data-at="{2.0 + j * 0.5:.3f}" data-dur="0.45" data-anim="pop">'
                            f'<b class="sk-big sk-bit">{bit}</b></div></div>')
        bots[POISON].to(3.8, 0.5, s=1.35)
        st.tag("zaharli!", BX[POISON], 680, 3.9, red=True)
        st.mark("ck-found", 3.8)
        t = 4.4
    st.end = max(st.end, t)
    return scene(name, st, msg, hold)


cover_st = K.Stage()
for i in range(10):
    x = 100 + i * 98
    a = (i in (0, 2, 3, 5, 9))
    cover_st.add(K.mouse(asleep=a), x, 1420, 150, 110, s=0.62)
cover = scene("cover", cover_st, (S("Mantiq jumbogʻi · 5 · javob", "bk-kick", anim="none")
                                  + S("10 sichqon", "bk-hero sk-hero2", anim="none")
                                  + S("Sir — ikkilik sanoq", "bk-slab", anim="none")), hold=3.4)

doubling = Scene(
    8.0,
    P.line("Har sichqon — ikki barobar", "ttl", at=0.0, anim="rise", dur=0.6)
    + P.solve([("3 ta", "8 ta shisha"), ("5 ta", "32 ta shisha"), ("8 ta", "256 ta shisha"),
               ("10 ta", "1024 ta shisha")], at=1.0, step=0.8)[0],
    cam="push", name="ikki barobar")

VIDEO = Video(
    slug="mj05j", lesson="Mantiq jumbogʻi 5 — javob",
    title="Ming shisha: javob — 10 ta sichqon", story="MJ-05 · javob (savoli: mj05s)",
    subject="logic",
    scenes=[
        cover,
        demo(0, "8 ta shisha", S("Kichikdan: 8 shisha, 3 sichqon", "bk-txt", at=0.2)),
        demo(1, "ichadi", S("Har sichqon — oʻz raqamidan", "bk-txt", at=0.0, anim="fade"), hold=1.0),
        demo(2, "ertasi kuni", S("Ertasi kuni…", "bk-txt", at=0.0, anim="fade")
             + S("1 0 1 → 5-shisha!", "bk-txt bk-grn", at=3.4, anim="pop", dur=0.5), hold=1.8),
        doubling,
        rule("Har sichqon — bitta «ha yoki yoʻq» savoli",
             meaning="10 ta savol — 1024 xil javob. 1000 tasiga yetadi.", dur=7.6),
        ask("Ikki kun vaqt boʻlsa-chi? Nechta sichqon yetadi?", head="Endi siz", dur=6.0,
            note="Javob: 7 (har sichqon 3 holat: 1-kun, 2-kun, hech qachon; 3^7 = 2187)."),
        practice("Mantiq maydoni", sub="powerty.uz → Mantiq maydoni", dur=5.0),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Xayrli tong, oshqovoqchalar! || Javob: atigi oʻnta sichqon!",
    "Kichikdan boshlaymiz: | sakkizta shisha, uchta sichqon. | Har shishaning raqami — ikkilik sanoqda.",
    "A — birinchi raqami bir boʻlganlardan ichadi. | B — ikkinchisi, C — uchinchisi.",
    "Ertasi kuni: A va C uxlab qoldi, B — bedor. || Bir, nol, bir — bu besh!",
    "Har yangi sichqon shishalar sonini ikki barobar oshiradi. || Oʻnta sichqon — ming yigirma toʻrtta shisha!",
    "Qoida: | har sichqon — bitta «ha yoki yoʻq» savoli.",
    "Endi siz: | ikki kun vaqt boʻlsa, nechta sichqon yetadi? || Izohda yozing!",
    "Har hafta yangi jumboqlar — Powertyda, Mantiq maydonida.",
    None,
])
