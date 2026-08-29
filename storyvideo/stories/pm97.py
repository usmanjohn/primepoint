# -*- coding: utf-8 -*-
"""PM-97 — «Toshkentda ikki kishining sochi bir xil»   SHAKL: KASHFIYOT

Manba: _stories_prime_math_96_98.py, order 97.

Bu videoning dvigateli — birinchi jumla. U ishonarsiz eshitiladi va isbot
atigi ikkita sondan iborat. Hech kimning sochini sanash shart emas — mana shu
«sanamasdan bilish» videoning butun zavqi.

Oxirida xulosa kuchayadi: kamida ikkita emas, kamida OʻN BESH kishi. Va eng
muhimi — prinsip ularning kimligini aytmaydi. Isbot bor, odam yoʻq.
"""

from spec import Video, Scene
from scenes import hook, says, beat, check, rule, ask, outro
import primitives as P

# Chap ustun qisqa boʻlishi shart — .solve__l nowrap, 62px (pm84 ga qarang).
_ladder, ls = P.solve([
    ("0 … 200 000", "soch tolalari soni — ehtiyot boʻlib olingan chegara"),
    ("200 001 uya", "shuncha xil son mavjud"),
    ("3 000 000", "shuncha toshkentlik bor"),
    ("uyalar kam", "demak bir uyada ikkita odam"),
], at=0.6, step=1.7)

ladder = Scene(
    11.5,
    P.counters(P.counter(4, "qadam", at=0.6, dur=ls, counts=".solve__row"))
    + _ladder
    + P.line("birorta ham sochni sanamadik", "ttl grn",
             at=0.6 + ls + 0.6, anim="pop", dur=0.7)
    # ── Hazil, lekin bejiz emas ──────────────────────────────────────────
    # Kal odamning sochi 0 ta — va aynan shuning uchun variantlar soni
    # 200 001, 200 000 emas: nol ham sanoqqa kiradi. U oʻsha «+1» ning oʻzi.
    # Ovozda hech narsa oʻzgarmaydi; u jim turadi va jim ketadi.
    + f'<div class="spot" data-at="{0.6 + ls + 1.5:.3f}" data-dur="0.55" '
      f'data-anim="pop">{P._people.figure("Kal aka", size=185, mood="smile")}</div>'
    + P.line("u ham hisobda: 0 ta", "lbl lbl--sm",
             at=0.6 + ls + 2.2, anim="rise"),
    cam="sink", top=True, name="ladder", counts=[4],
    note="Har bir odamni sochlari soniga qarab bitta uyaga joylashtiramiz. "
         "Uyalar 200 001 ta, odamlar 3 000 000 ta. Oxirida kal odam chiqadi — "
         "u nolinchi uyada, va aynan shuning uchun 200 001.")

VIDEO = Video(
    slug="pm97",
    lesson="PM-97",
    title="Toshkentda ikki kishining sochi bir xil",
    story="Prime Math Readings — order 97",
    scenes=[
        hook("3 000 000", "toshkentlik", "200 001", "xil son",
             "Nima kelib chiqadi?", dur=5.2),

        says("Afsona", [("Toshkentda sochlari soni", "lbl"),
                        ("bir xil ikki kishi bor", "expr gold"),
                        ("Hech kimni koʻrmasdan aytaman", "ask")],
             dur=6.8, size=250,
             note="Ishonarsiz eshitiladi. Isbot esa atigi ikkita sondan iborat."),

        beat(4.2, note="Jim turing. Buni qanday isbotlash mumkin?"),

        ladder,

        # Teskari faraz — isbotning oʻzi.
        check("200 001 × 1 = 200 001",
              parts=["aytaylik, hammada har xil son boʻlsin", "unda shaharda shuncha odam boʻlardi"],
              verdict="Lekin 3 000 000 kishi bor. Ziddiyat.",
              title="Teskari faraz", dur=8.6,
              note="Har uyada koʻpi bilan bitta odam boʻlsa, shahar 200 001 kishidan "
                   "oshmasdi."),

        check("200 001 × 14 = 2 800 014",
              parts=["har uyada koʻpi bilan 14 kishi boʻlsa", "bu uch milliondan kam"],
              verdict="Demak kamida 15 kishi.", title="Aslida kuchliroq", dur=8.6,
              note="Xulosa ikkitadan ancha kuchli: kamida oʻn besh kishi."),

        rule("Obyektlar uyalardan koʻp boʻlsa, bir uyada kamida ikkitasi bor",
             strip="Dirixle prinsipi",
             meaning="Prinsip ularni topib bermaydi — faqat borligini kafolatlaydi.",
             dur=9.6,
             note="Isbot bor, odam yoʻq. Matematikada bunday isbot ham qabul qilinadi."),

        ask("13 oʻquvchi bor. Nega ulardan kamida ikkitasi bir oyda tugʻilgan?",
            dur=7.0, note="Javobni aytmang — oʻsha prinsipni oʻzlari qoʻllasin."),

        outro(),
    ],
)

# ── Ovoz uchun matn (TTS). Raqamlar avtomatik soʻzga aylantiriladi. ──
from spec import narrate

narrate(VIDEO, [
    "Toshkentda soch tolalari soni roppa-rosa bir xil boʻlgan kamida ikki "
    "kishi bor. || Buni isbotlash uchun birorta ham sochni sanash shart emas.",

    "Umuman hech kimni koʻrish ham shart emas. | Yetarli — ikkita son.",

    "Bir soniya oʻylab koʻring. || Qaysi ikkita son?",

    "Birinchisi: odam boshidagi soch tolalari 200 mingdan oshmaydi — demak "
    "*200 001 xil variant*. | Ikkinchisi: Toshkent aholisi *3 million*. "
    "|| Har kimni sochlari soniga qarab bitta uyaga joylashtiramiz. "
    "Odamlar uyalardan koʻp.",

    "Teskari faraz qilamiz: aytaylik, hammada har xil son boʻlsin. | Unda "
    "shaharda 200 001 dan ortiq odam boʻlmasdi. || Lekin 3 million kishi "
    "bor. *Ziddiyat* — faraz notoʻgʻri.",

    "Aslida xulosa ancha kuchliroq. Agar har uyada koʻpi bilan 14 kishi "
    "boʻlganda, jami 2 million 800 mingdan oshmasdi. | Bu esa uch milliondan "
    "kam. || Demak biror uyada *kamida 15 kishi* bor.",

    "Esda tutinglar. || Prinsip bu odamlarning kimligini *aytmaydi*. U ularni "
    "topib bermaydi, ismini bilmaydi. U faqat bitta narsani aytadi: "
    "bunday odamlar bor.",

    "Endi oʻzingiz oʻylang. Sinfda 13 oʻquvchi bor. Nega ulardan kamida "
    "ikkitasi bir oyda tugʻilgan? || Izohda kutamiz.",

    None,   # outro — jim
])
