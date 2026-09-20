"""Digital-SAT scaled scoring: raw correct -> 200–800 per section, 400–1600 total.

Two things make this not a percentage:

  * the curve is not linear — the last few raw points are worth far more than
    the ones in the middle;
  * which module 2 you were routed into changes the ceiling. A taker who never
    left the lower module cannot reach 800, however clean their paper is. That
    is the whole point of an adaptive test, and it is the number a pupil most
    needs to see honestly.

The anchors below are modelled on the published scoring tables for the
released digital practice tests. They are an approximation — College Board
equates every real form separately and does not publish the formula — so a
score here is a good estimate of a band, not a promise of a number.
"""

# raw correct -> scaled, at the anchor points; everything between is linear.
CURVES = {
    ('rw', 'hard'): [(0, 200), (5, 280), (10, 350), (15, 410), (20, 460), (25, 510),
                     (30, 560), (35, 610), (40, 660), (45, 710), (50, 760), (54, 800)],
    ('rw', 'easy'): [(0, 200), (5, 260), (10, 310), (15, 350), (20, 390), (25, 420),
                     (30, 450), (35, 480), (40, 510), (45, 540), (50, 570), (54, 600)],
    ('math', 'hard'): [(0, 200), (4, 270), (8, 340), (12, 400), (16, 450), (20, 500),
                       (24, 550), (28, 600), (32, 650), (36, 700), (40, 750), (44, 800)],
    ('math', 'easy'): [(0, 200), (4, 250), (8, 300), (12, 340), (16, 380), (20, 410),
                       (24, 440), (28, 470), (32, 500), (36, 530), (40, 560), (44, 590)],
}

SECTION_LABELS = {
    'rw': 'Reading and Writing',
    'math': 'Math',
}


def scale(kind, route, raw):
    """raw correct across BOTH modules of a section -> 200–800, in steps of 10."""
    anchors = CURVES.get((kind, route or 'easy'))
    if not anchors:
        return None
    raw = max(0, min(raw, anchors[-1][0]))
    for (x0, y0), (x1, y1) in zip(anchors, anchors[1:]):
        if x0 <= raw <= x1:
            if x1 == x0:
                value = y0
            else:
                value = y0 + (y1 - y0) * (raw - x0) / (x1 - x0)
            return int(round(value / 10.0) * 10)
    return anchors[-1][1]


def band(total):
    """A one-line reading of a 400–1600 total, in Uzbek."""
    if total is None:
        return ''
    if total >= 1400:
        return "Juda kuchli — eng tanlangan universitetlar darajasi."
    if total >= 1200:
        return "Kuchli — koʻpchilik universitetlar uchun yetarli."
    if total >= 1000:
        return "Oʻrtacha — ishlash kerak boʻlgan mavzular aniq koʻrinadi."
    if total >= 800:
        return "Poydevor qurilmoqda — asosiy mavzularga qayting."
    return "Boshlangʻich — kursni boshidan, tartib bilan oʻqing."
