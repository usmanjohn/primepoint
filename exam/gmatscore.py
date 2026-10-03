"""GMAT Focus Edition scoring: raw correct -> 60–90 per section, 205–805 total.

What is official (mba.com, checked 2026-10-02):

  * three sections — Quantitative Reasoning (21 questions), Verbal Reasoning (23)
    and Data Insights (20), 45 minutes each;
  * each section is reported on a 60–90 scale, the total on 205–805 in steps of
    ten (every total ends in 5), and the three sections weigh equally.

What is NOT official, and why this module is an estimate: the real test is
adaptive question by question and GMAC does not publish how raw performance or
the section scores turn into the total. A fixed-form mock cannot reproduce that.
So the curve below is a modelled approximation — monotonic, harsher at the top,
with a mid-paper performance landing near the published section medians — and
every page that shows a number calls it *taxminiy* (estimated). A score here
reads a band, never a promise.
"""

SECTION_KINDS = ('quant', 'verbal', 'di')

SECTION_LABELS = {
    'quant': 'Quantitative Reasoning',
    'verbal': 'Verbal Reasoning',
    'di': 'Data Insights',
}

SECTION_LABELS_UZ = {
    'quant': 'Miqdoriy mulohaza (Quant)',
    'verbal': 'Ogʻzaki mulohaza (Verbal)',
    'di': 'Maʼlumotlar tahlili (Data Insights)',
}

# share of the section answered correctly -> section score; linear in between.
ANCHORS = [(0.00, 60), (0.25, 66), (0.40, 71), (0.50, 75), (0.60, 78),
           (0.70, 81), (0.80, 84), (0.90, 87), (1.00, 90)]


def section(raw, total):
    """Raw correct out of `total` -> an integer section score, 60–90."""
    if not total:
        return None
    share = max(0.0, min(1.0, raw / total))
    for (x0, y0), (x1, y1) in zip(ANCHORS, ANCHORS[1:]):
        if x0 <= share <= x1:
            return int(round(y0 + (y1 - y0) * (share - x0) / (x1 - x0)))
    return ANCHORS[-1][1]


def total(quant, verbal, di):
    """Three section scores (60–90) -> a total, 205–805, ending in 5.

    The three sections weigh equally, so the total is a linear map of their sum
    (180–270) onto 205–805, rounded to the reporting step of ten.
    """
    if None in (quant, verbal, di):
        return None
    combined = quant + verbal + di
    value = 205 + (combined - 180) * 600 / 90
    return int(205 + round((value - 205) / 10.0) * 10)


def band(score):
    """A one-line, honest reading of an estimated 205–805 total, in Uzbek."""
    if score is None:
        return ''
    if score >= 705:
        return "Juda kuchli — eng tanlangan biznes maktablari darajasi (taxminiy baho)."
    if score >= 645:
        return "Kuchli — koʻplab yaxshi MBA dasturlari uchun raqobatbardosh (taxminiy baho)."
    if score >= 555:
        return "Oʻrtacha atrofida — zaif boʻlim aniq koʻrinadi, oʻsha yerdan boshlang (taxminiy baho)."
    if score >= 455:
        return "Poydevor qurilmoqda — Prime GMAT darslarini tartib bilan takrorlang (taxminiy baho)."
    return "Boshlangʻich — kursni boshidan oʻqing; bu mock bir necha oydan keyin yana yechiladi (taxminiy baho)."
