# -*- coding: utf-8 -*-
"""MO-41 — «Qogʻozni 42 marta buklasangiz, Oyga yetasiz»   MATEMATIKA OLAMI

Manba: Matematika olami, order 41.

Exponential growth, made physical. Thickness after n folds = 0,1 mm × 2^n,
recomputed in the scratchpad gate:
    7 -> 12,8 mm   10 -> 102 mm   14 -> 1,64 m   20 -> 105 m
    27 -> 13,4 km  30 -> 107 km   41 -> 219 902 km   42 -> 439 805 km
Moon: 384 400 km (mean distance). Record: Britney Gallivan, 2002, 12 folds of
a ~1,2 km paper strip.

The check line 2 × 220 000 = 440 000 uses the rounded figures the screen shows.
"""

from spec import Video, narrate, Scene
from scenes import cover, claim, beat, fact, versus, check, rule, ask, practice, outro
import primitives as P

_low, ls = P.solve([
    ("7 marta",  "128 qavat ≈ 1,3 sm — daftar"),
    ("10 marta", "1 024 qavat ≈ 10 sm — gʻisht"),
    ("14 marta", "≈ 1,6 m — sizning boʻyingiz"),
    ("20 marta", "≈ 105 m — 30 qavatli bino"),
], at=0.7, step=1.2)
low = Scene(
    9.6,
    P.line("Har buklash — ikki barobar", "lbl lbl--sm", at=0.0, anim="fade") + _low,
    cam="sink", top=True, name="sekin boshlanish")

_high, hs = P.solve([
    ("27 marta", "≈ 13 km — Everestdan baland"),
    ("30 marta", "≈ 107 km — bu allaqachon koinot"),
    ("42 marta", "≈ 440 000 km"),
], at=0.7, step=1.4)
high = Scene(
    9.0,
    P.line("Endi tezlik keskin oshadi", "lbl lbl--sm", at=0.0, anim="fade") + _high,
    cam="sink", top=True, name="portlash")

VIDEO = Video(
    slug="mo41",
    lesson="Matematika olami",
    title="Qogʻozni 42 marta buklasangiz, Oyga yetasiz",
    story="Matematika olami — order 41",
    subject="math",
    scenes=[
        cover("1 metr", "Oygacha yetadi",
              kicker="Matematika olami",
              context="Qogʻozni 42 marta buklasangiz, qalinligi:",
              note="MUQOVA: hamma aytadigan «bir metr» chizilgan."),

        claim("Jasur", "42 marta buklash", "≈ 1 metr",
              doubt="Nari borsa?", dur=7.4),

        beat(dur=4.0, n=3,
             note="ATAYLAB JIM. Tomoshabin oʻz taxminini qilsin."),

        fact("× 2", "har bir buklashda",
             cap="Varaq qalinligi — 0,1 mm. Har buklash qavatlarni ikki barobar oshiradi.",
             dur=6.6, cam="pull"),

        low,

        high,

        versus({"name": "Oygacha", "qty": "384 ming",
                "price": "km"},
               {"name": "42 buklash", "qty": "440 ming",
                "price": "km", "tag": "Oydan ham nari", "cls": "win"},
               title="Qogʻoz Oyni ortda qoldiradi",
               dur=8.6),

        check("2 × 220 000 = 440 000",
              parts=["41-buklashdan keyin ≈ 220 000 km",
                     "Oxirgi buklashning oʻzi yana shuncha qoʻshadi"],
              verdict="Har qadam — oldingilarning hammasicha",
              title="Sir — ikki barobar oʻsishda",
              dur=8.6),

        fact("12", "marta — jahon rekordi",
             cap="2002-yil. Britni Gallivan 1 km dan uzun qogʻoz tasmasini 12 marta bukladi.",
             dur=7.4, cam="push"),

        rule("Ikki barobar oʻsadigan narsa boshida arzimas koʻrinadi",
             strip="0,1 mm × 2 × 2 × … ≈ 440 000 km",
             meaning="Mikrob, mish-mish yoki jamgʻarma — keyin bir zumda "
                     "hammasini egallab oladi.",
             dur=9.0),

        ask("Oʻt koʻlni 30 kunda qoplaydi, har kuni ikki barobar oʻsib. "
            "Yarmini qachon qoplagan?",
            dur=7.4,
            note="Javobni aytmang: 29-kuni."),

        practice("Burchak · Matematika olami",
                 sub="powerty.uz → Burchak → Matematika olami",
                 dur=5.2),

        outro(),
    ],
)

narrate(VIDEO, [
    "Bir varaq qogʻozni qirq ikki marta buklasangiz, "
    "|| qalinligi qancha boʻladi?",

    "Koʻpchilik aytadi: bir necha santimetr, nari borsa bir metr. "
    "|| Toʻgʻri javob esa — Oygacha.",

    None,   # beat

    "Varaq qalinligi — millimetrning oʻndan biri. "
    "|| Har bir buklash uni ikki barobar oshiradi.",

    "Yetti marta — daftar qalinligi. | Oʻn marta — gʻisht. "
    "|| Yigirma marta — oʻttiz qavatli bino.",

    "Keyin tezlik keskin oshadi. | Yigirma yetti marta — Everestdan baland. "
    "|| Oʻttiz marta — allaqachon koinot.",

    "Qirq ikki marta — toʻrt yuz qirq ming kilometr. "
    "|| Oygacha esa — uch yuz sakson toʻrt ming. [gasps]",

    "Sir shunda: har yangi buklash oldingi hammasicha qalinlik qoʻshadi. "
    "|| Oxirgisining oʻzi — ikki yuz yigirma ming kilometr.",

    "Amalda qogʻozni yetti-sakkiz martadan koʻp buklab boʻlmaydi. "
    "|| Rekord — oʻn ikki marta.",

    "Ikki barobar oʻsadigan narsa boshida arzimas koʻrinadi. "
    "|| Keyin esa bir zumda hammasini egallaydi.",

    "Endi oʻylang, aqlli boshlar: | oʻt koʻlni oʻttiz kunda qoplaydi. "
    "|| Yarmini qachon qoplagan? Izohda kutamiz.",

    "Bunday hikoyalar — Powertyda, Burchak boʻlimida.",

    None,   # outro
])
