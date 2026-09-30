# -*- coding: utf-8 -*-
"""Throwaway: the same cover in all three badge layouts, for choosing between.

Not a film. Delete once the layout is picked.
"""
from spec import Video, narrate
from scenes import cover

WRONG = "호랑이"

VIDEO = Video(
    slug="_badgedemo",
    title="Badge layouts",
    subject="korean",
    scenes=[
        cover(WRONG, "Bizda — boʻri",
              kicker="Bir maqol, ikki til", ko="한국어",
              track="속담", n=7, badge="pills", strike=False,
              context="Koreys maqolida — yoʻlbars:",
              note="A — ikkita pill"),
        cover(WRONG, "Bizda — boʻri",
              kicker="Bir maqol, ikki til", ko="한국어",
              track="속담", n=7, badge="combined", strike=False,
              context="Koreys maqolida — yoʻlbars:",
              note="B — bitta qoʻshilgan pill"),
        cover(WRONG, "Bizda — boʻri",
              kicker="Bir maqol, ikki til", ko="한국어",
              track="속담", n=7, badge="big", strike=False,
              context="Koreys maqolida — yoʻlbars:",
              note="C — katta raqam"),
    ],
)

narrate(VIDEO, ["A", "B", "C"])
