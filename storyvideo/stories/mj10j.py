# -*- coding: utf-8 -*-
"""MJ-10j — «Ikki qorovul: javob — «sherigingiz nima derdi?»»   MANTIQ JUMBOGʻI · 10, JAVOB

Ask either guard: «Which door would the OTHER guard say leads to freedom?»
Truthful guard: reports the liar's (wrong) answer truthfully -> the lion.
Liar: the truthful one would say freedom; he lies about that -> the lion.
Both point at the lion, so take the other door.
Ask: why is «Are you the honest one?» useless? (both say yes.)
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from spec import Video, narrate
from scenes import rule, ask, practice, outro
from _sk import scene, S
from _guards import hall, bubble, point, FREE, DX
import stagekit as K

LION = "R" if FREE == "L" else "L"
Q = "«Sherigingiz qaysi eshikni koʻrsatardi?»"

cover = scene("cover", hall(reveal=True, open_free=-50), (S("Mantiq jumbogʻi · 10 · javob", "bk-kick", anim="none")
                                                          + S("Teskarisini!", "bk-hero bk-grn", anim="none")
                                                          + S("«U nima derdi?»", "bk-slab", anim="none")), hold=3.4)


def case(who, name, hold=1.4):
    st = hall(labels={"L": "?", "R": "?"})
    bubble(st, Q, 540, 820, 0.4)
    st.tag("rostgoʻy" if who == "truth" else "yolgʻonchi", DX["L" if who == "truth" else "R"], 1420, 1.6,
           red=(who != "truth"))
    point(st, LION, 2.6)
    return scene(name, st, S("Rostgoʻydan soʻrasak" if who == "truth" else "Yolgʻonchidan soʻrasak",
                             "bk-txt", at=0.0, anim="fade"), hold=hold)


st = hall(reveal=True, open_free=1.6)
point(st, LION, 0.4)
final = scene("teskarisi", st, S("Ikkalasi ham — sherni koʻrsatadi", "bk-txt", at=0.0, anim="fade")
              + S("Teskarisini tanlang!", "bk-txt bk-grn", at=1.6), hold=1.8)

VIDEO = Video(
    slug="mj10j", lesson="Mantiq jumbogʻi 10 — javob",
    title="Ikki qorovul: javob", story="MJ-10 · javob (savoli: mj10s)",
    subject="logic",
    scenes=[
        cover,
        scene("eslatma", hall(), S("Kecha: oddiy savol — xavfli", "bk-txt", at=0.2), hold=1.6),
        scene("savol", hall(), S("Istalganidan soʻrang:", "bk-txt", at=0.2)
              + S(Q, "bk-slab", at=0.9, anim="pop", dur=0.5), hold=2.4),
        case("truth", "rostgoʻy"),
        case("lie", "yolgʻonchi"),
        final,
        rule("Ikkala holatda bir xil javob beradigan savol bering",
             meaning="Rost va yolgʻon bir-birini «oʻrab» olsa — doim bir xil xato chiqadi.", dur=7.6),
        ask("«Siz rostgoʻymisiz?» deb soʻrash nega befoyda?", head="Endi siz", dur=5.8,
            note="Javob: ikkalasi ham «ha» deydi."),
        practice("Mantiq maydoni", sub="powerty.uz → Mantiq maydoni", dur=5.0),
        outro(line2="mantiq jumboqlari"),
    ],
)

narrate(VIDEO, [
    "Xayrli tong, azizlar! || Javob — bitta ayyor savol.",
    "Kecha: oddiy savol yolgʻonchiga duch kelsa — sherga olib boradi.",
    "Istalgan qorovuldan soʻrang: | «Sherigingiz qaysi eshikni koʻrsatardi?»",
    "Rostgoʻydan soʻrasangiz: | u yolgʻonchining notoʻgʻri javobini rostdan aytadi — | sher eshigini.",
    "Yolgʻonchidan soʻrasangiz: | rostgoʻy ozodlikni koʻrsatardi, | yolgʻonchi esa buni ham buradi — | yana sher!",
    "Ikkalasi ham bir xil eshikni koʻrsatadi. || Demak, teskarisini tanlang — ozodlik!",
    "Qoida: | ikkala holatda bir xil javob beradigan savol bering.",
    "Endi siz: | «Siz rostgoʻymisiz?» deb soʻrash nega befoyda? || Izohda yozing!",
    "Har hafta yangi jumboqlar — Powertyda, Mantiq maydonida.",
    None,
])
