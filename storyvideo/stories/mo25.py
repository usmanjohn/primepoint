# -*- coding: utf-8 -*-
"""MO-25 — «Shtrix-koddagi oxirgi raqam nima uchun kerak»  MATEMATIKA OLAMI

Manba: Matematika olami, order 25.

An everyday object nobody has ever asked about, and the answer is arithmetic
doing a job: the last of the thirteen digits carries no information at all. It
is computed from the other twelve, and its whole purpose is to disagree when the
scanner misreads.

Worked example, recomputed here and checked by the arithmetic gate:

    476123456789            the first twelve (476 = Uzbekistan's GS1 prefix)
    odd places   4+6+2+4+6+8 = 30
    even places  7+1+3+5+7+9 = 32,  x3 = 96
    total        30 + 96 = 126
    check digit  130 - 126 = 4      ->  4761234567894

⚠️ THE 13-DIGIT CODE NEVER GOES INTO THE NARRATION. `speech.py` turns every
digit run into Uzbek words, and 4761234567894 would come out as "toʻrt ming
yetti yuz oltmish bir milliard..." — a minute of word salad. The code lives on
SCREEN; the voice says "oʻn uchta raqam" and speaks only the small sums.

That is the same class as the Hangul and Roman-numeral rules: whatever the
engine cannot say properly, the picture carries instead.
"""

from spec import Video, narrate, Scene
from scenes import cover, fact, beat, check, versus, rule, ask, outro
import primitives as P

_sum, ms = P.solve([
    ("toq oʻrinlar",  "4 + 6 + 2 + 4 + 6 + 8 = 30"),
    ("juft oʻrinlar", "7 + 1 + 3 + 5 + 7 + 9 = 32"),
    ("× 3",           "32 × 3 = 96"),
    ("jami",          "30 + 96 = 126"),
], at=0.7, step=1.4)

summing = Scene(
    10.2,
    P.line("Raqamlar navbatma-navbat 1 ga va 3 ga koʻpaytiriladi",
           "lbl lbl--sm", at=0.0, anim="fade") + _sum,
    cam="sink", top=True, name="hisob",
    claims=["4 + 6 + 2 + 4 + 6 + 8 = 30",
            "7 + 1 + 3 + 5 + 7 + 9 = 32",
            "32 × 3 = 96",
            "30 + 96 = 126"],
    note="Butun hisob toʻrt qatorda. `.solve__l` 62px va nowrap, shuning "
         "uchun chap ustun qisqa — uzun ifodalar oʻng ustunda.")

VIDEO = Video(
    slug="mo25",
    lesson="Matematika olami",
    title="Shtrix-koddagi oxirgi raqam nima uchun kerak",
    story="Matematika olami — order 25",
    subject="math",
    scenes=[
        cover("4", "Hech narsani bildirmaydi",
              kicker="Matematika olami",
              context="4761234567894 — eng oxirgi raqam:",
              strike=False,
              note="MUQOVA: oʻn uch xonali kod 102px ga tushadi va setkada "
                   "oʻqilmaydi (120px darvozasi), shuning uchun kod "
                   "kontekst satrida, ekranda esa bitta raqam."),

        fact("13", "ta raqam",
             cap="Dastlabki uchtasi mamlakatni bildiradi. Oʻzbekiston — 476.",
             dur=6.8, cam="pull",
             note="Keyingilari ishlab chiqaruvchini va mahsulotni "
                  "koʻrsatadi. Oxirgisi esa butunlay boshqa ish qiladi."),

        beat(dur=4.2, n=3,
             note="ATAYLAB JIM. Savol berildi — oxirgi raqam nega kerak? — "
                  "va tomoshabin taxmin qilib koʻrsin."),

        summing,

        check("130 − 126 = 4",
              parts=["Yigʻindini keyingi oʻnlikkacha toʻldiramiz",
                     "Yetmagan son — nazorat raqami"],
              verdict="Oxirgi raqam — 4",
              title="Endi oxirgi raqamni topamiz",
              dur=8.4,
              note="Shu bitta amal butun kodni yopadi."),

        versus({"name": "skaner toʻgʻri oʻqidi",
                "qty": "126",
                "price": "nazorat raqami — 4",
                "tag": "kod mos keldi", "cls": "win"},
               {"name": "bitta raqam xato",
                "qty": "≠ 126",
                "price": "nazorat raqami boshqa",
                "tag": "kompyuter xato beradi", "cls": "lose"},
               title="Skaner adashsa nima boʻladi",
               dur=11.0,
               note="Filmning javobi: oxirgi raqam maʼlumot tashimaydi, "
                    "u qolganlarini TEKSHIRADI."),

        rule("Oxirgi raqam maʼlumot emas — u qorovul",
             strip="oʻn ikkitasi maʼlumot  ·  oʻn uchinchisi tekshiruv",
             meaning="Xuddi shunday nazorat tizimi bank kartalarida ham, "
                     "pasport raqamlarida ham ishlaydi. Kassadagi «bip» — "
                     "aslida bir necha amalning tovushi.",
             dur=9.6),

        ask("Eng koʻp uchraydigan xato — oʻrin almashish: 45 oʻrniga 54. "
            "Nazorat raqami buni nega tutadi?",
            dur=7.8,
            note="Javobni aytmang. Toq va juft oʻrinlar har xil "
                 "koʻpaytirilgani — hisob sahnasida koʻrsatilgan."),

        outro(),
    ],
)

narrate(VIDEO, [
    "Har bir shtrix-kodda oʻn uchta raqam bor. || Eng oxirgisi esa hech "
    "qanday maʼlumot bermaydi.",

    "Keyingi raqamlar ishlab chiqaruvchini va mahsulotni koʻrsatadi. "
    "|| Oxirgisi esa butunlay boshqa ish qiladi.",

    None,   # beat — jim sahna, tomoshabin taxmin qilsin

    "U qolgan oʻn ikkitasidan hisoblab chiqariladi. | Raqamlar "
    "navbatma-navbat birga va uchga koʻpaytiriladi, keyin qoʻshiladi.",

    "Yigʻindini keyingi oʻnlikkacha toʻldiramiz. | 130 dan 126 ni "
    "ayirsak — oxirgi raqam toʻrt.",

    "Endi eng qizigʻi. | Agar skaner bitta raqamni xato oʻqisa, nazorat "
    "raqami boshqa chiqadi.",

    "Shuning uchun oxirgi raqam maʼlumot emas — u qorovul. || Xuddi "
    "shunday tizim bank kartalarida ham, pasport raqamlarida ham ishlaydi.",

    "Endi oʻzingiz oʻylang. | 45 oʻrniga 54 yozilsa, nazorat raqami buni "
    "nega tutadi? || Izohda kutamiz.",

    None,   # outro — jim
])
