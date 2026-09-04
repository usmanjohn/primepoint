# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-41 … SAT-45.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context & interpretation ·
      15–16 trap-spotting · 17–18 Module 2 level · 19–20 word problems.

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_41_45.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Math",
    "description": "SAT Math — Prime SAT darslarining mashqlari",
    "icon":        "bi-calculator",
    "color":       "#4f46e5",
}

DEFAULTS = {
    "level":                "easy",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# SAT-41 — rational expressions & polynomial division
# =====================================================================

Q_SAT41 = [
    {
        "text": "<p>Simplify: (<i>x</i><sup>2</sup> − 4) ÷ (<i>x</i> − 2), where "
                "<i>x</i> ≠ 2</p>",
        "choices": ["x + 2", "x − 2", "x² − 2", "2"],
        "correct": "x + 2",
        "explanation": "<p><strong>x + 2.</strong> Surat (x − 2)(x + 2), va (x − 2) "
                       "qisqaradi.</p>"
                       "<p><strong>x − 2</strong> — qisqargan qavs javobga "
                       "koʻchirilgan; qoladigani ikkinchisi.</p>",
    },
    {
        "text": "<p>Simplify: (<i>x</i><sup>2</sup> − 36) ÷ (<i>x</i> + 6), where "
                "<i>x</i> ≠ −6</p>",
        "choices": ["x − 6", "x + 6", "x² − 6", "6"],
        "correct": "x − 6",
        "explanation": "<p><strong>x − 6.</strong> Surat (x − 6)(x + 6).</p>"
                       "<p>Tekshiruv: x = 7 da (49 − 36) ÷ 13 = 1, va 7 − 6 = 1 ✓</p>",
    },
    {
        "text": "<p>Simplify: (<i>x</i><sup>2</sup> + 7<i>x</i> + 12) ÷ "
                "(<i>x</i> + 3)</p>",
        "choices": ["x + 4", "x + 3", "x + 12", "x + 7"],
        "correct": "x + 4",
        "explanation": "<p><strong>x + 4.</strong> Surat (x + 3)(x + 4) — 3 × 4 = 12 "
                       "va 3 + 4 = 7.</p>"
                       "<p>Tekshiruv: x = 0 da 12 ÷ 3 = 4 ✓</p>",
    },
    {
        "text": "<p>Can (<i>x</i> + 7) ÷ 7 be simplified to <i>x</i>?</p>",
        "choices": ["No — 7 is a term, not a factor", "Yes", "Yes, but only if x ≠ 0",
                    "No — but it equals x + 1"],
        "correct": "No — 7 is a term, not a factor",
        "explanation": "<p><strong>Yoʻq.</strong> Suratda qoʻshish turibdi; faqat "
                       "koʻpaytuvchi qisqaradi.</p>"
                       "<p>Tekshiruv: x = 7 da asl ifoda 2, x esa 7.</p>",
    },
    {
        "text": "<p>Simplify: (2<i>x</i><sup>2</sup> + 5<i>x</i> − 3) ÷ "
                "(<i>x</i> + 3)</p>",
        "choices": ["2x − 1", "2x + 1", "2x − 3", "x − 1"],
        "correct": "2x − 1",
        "explanation": "<p><strong>2x − 1.</strong> Surat (x + 3)(2x − 1) — oching: "
                       "2x² − x + 6x − 3 ✓</p>"
                       "<p>Tekshiruv: x = 0 da −3 ÷ 3 = −1, va 2(0) − 1 = −1 ✓</p>",
    },
    {
        "text": "<p>Simplify: (3<i>x</i><sup>2</sup> − 12) ÷ (<i>x</i> − 2)</p>",
        "choices": ["3x + 6", "3x − 6", "3x + 2", "x + 6"],
        "correct": "3x + 6",
        "explanation": "<p><strong>3x + 6.</strong> Avval 3 ni chiqaring: "
                       "3(x² − 4) = 3(x − 2)(x + 2), demak javob 3(x + 2).</p>"
                       "<p>Umumiy koʻpaytuvchini oldin chiqarish ishni "
                       "yengillashtiradi (SAT-29).</p>",
    },
    {
        "text": "<p>Which expression is equivalent to (<i>x</i><sup>2</sup> + "
                "4<i>x</i> + 6) ÷ (<i>x</i> + 2)?</p>",
        "choices": ["x + 2 + 2 ÷ (x + 2)", "x + 2", "x + 3", "x + 4 + 6 ÷ (x + 2)"],
        "correct": "x + 2 + 2 ÷ (x + 2)",
        "explanation": "<p><strong>x + 2 + 2 ÷ (x + 2).</strong> "
                       "(x + 2)(x + 2) = x² + 4x + 4, va suratda 6 bor — qoldiq 2.</p>"
                       "<p>Tekshiruv x = 0 da: 6 ÷ 2 = 3, va 2 + 1 = 3 ✓</p>",
    },
    {
        "text": "<p>What is the remainder when <i>x</i><sup>2</sup> + 6<i>x</i> + 10 "
                "is divided by <i>x</i> + 2?</p>",
        "choices": ["2", "0", "10", "6"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> (x + 2)(x + 4) = x² + 6x + 8, va "
                       "10 − 8 = 2.</p>"
                       "<p>SAT-42 da buni yanada tezroq yoʻl bilan topamiz.</p>",
    },
    {
        "text": "<p>Simplify: (<i>x</i><sup>2</sup> − <i>x</i> − 6) ÷ "
                "(<i>x</i> − 3)</p>",
        "choices": ["x + 2", "x − 2", "x + 3", "x − 6"],
        "correct": "x + 2",
        "explanation": "<p><strong>x + 2.</strong> Surat (x − 3)(x + 2).</p>"
                       "<p>Tekshiruv: x = 0 da −6 ÷ (−3) = 2, va 0 + 2 = 2 ✓</p>",
    },
    {
        "text": "<p>Simplify: (4<i>x</i><sup>2</sup> − 9) ÷ (2<i>x</i> − 3)</p>",
        "choices": ["2x + 3", "2x − 3", "4x + 3", "2x + 9"],
        "correct": "2x + 3",
        "explanation": "<p><strong>2x + 3.</strong> Kvadratlar ayirmasi: "
                       "(2x − 3)(2x + 3) (SAT-30).</p>"
                       "<p>Tekshiruv: x = 2 da (16 − 9) ÷ 1 = 7, va 4 + 3 = 7 ✓</p>",
    },
    {
        "text": "<p>For which value of <i>x</i> is (<i>x</i><sup>2</sup> − 9) ÷ "
                "(<i>x</i> − 3) undefined?</p>",
        "choices": ["x = 3", "x = −3", "x = 9", "It is defined everywhere"],
        "correct": "x = 3",
        "explanation": "<p><strong>x = 3.</strong> Maxraj nolga aylanadi.</p>"
                       "<p>Qisqartirilganda x + 3 chiqadi, lekin qisqartirish taqiqni "
                       "oʻchirmaydi (SAT-40).</p>",
    },
    {
        "text": "<p>The expression (<i>x</i><sup>2</sup> − 1) ÷ (<i>x</i> − 1) equals "
                "<i>x</i> + 1 for every value of <i>x</i> except which one?</p>",
        "choices": ["x = 1", "x = −1", "x = 0", "There is no exception"],
        "correct": "x = 1",
        "explanation": "<p><strong>x = 1.</strong> U yerda asl ifoda aniqlanmagan, "
                       "x + 1 esa 2 beradi.</p>"
                       "<p>Ikki ifoda «deyarli» teng — bitta nuqtadan tashqari.</p>",
    },
    {
        "text": "<p>Why can (<i>x</i><sup>2</sup> + 9) ÷ (<i>x</i> + 3) not be "
                "simplified?</p>",
        "choices": ["A sum of squares does not factor",
                    "The denominator is too small",
                    "x² + 9 equals (x + 3)(x + 3)",
                    "It can be simplified to x + 3"],
        "correct": "A sum of squares does not factor",
        "explanation": "<p><strong>Kvadratlar yigʻindisi ajralmaydi.</strong> Faqat "
                       "ayirmasi ajraladi (SAT-30).</p>"
                       "<p>(x + 3)(x + 3) = x² + 6x + 9 — oʻrtadagi had bor.</p>",
    },
    {
        "text": "<p>A rectangle has area <i>x</i><sup>2</sup> + 9<i>x</i> + 20 and "
                "width <i>x</i> + 4. What is its length?</p>",
        "choices": ["x + 5", "x + 4", "x + 20", "x + 9"],
        "correct": "x + 5",
        "explanation": "<p><strong>x + 5.</strong> Yuzani enga boʻlish — bu "
                       "ajratishning oʻzi: (x + 4)(x + 5).</p>"
                       "<p>Tekshiruv: x = 1 da yuza 30, en 5, uzunlik 6 ✓</p>",
    },
    {
        "text": "<p>A student simplifies (<i>x</i> + 6) ÷ (<i>x</i> + 3) to 2. What "
                "is wrong?</p>",
        "choices": ["Terms cannot be cancelled — only factors",
                    "The answer should be 3",
                    "The answer should be x",
                    "Nothing — the student is right"],
        "correct": "Terms cannot be cancelled — only factors",
        "explanation": "<p><strong>Hadni qisqartirib boʻlmaydi.</strong> Oʻquvchi "
                       "6 ni 3 ga boʻlgan, lekin ular koʻpaytuvchi emas.</p>"
                       "<p>Tekshiruv: x = 0 da 6 ÷ 3 = 2 ✓ lekin x = 3 da 9 ÷ 6 = "
                       "1.5 ✗ — bitta son yetarli emas, ifoda hamma joyda teng "
                       "boʻlishi kerak.</p>",
    },
    {
        "text": "<p>A student writes (<i>x</i><sup>2</sup> + 5<i>x</i> + 8) ÷ "
                "(<i>x</i> + 2) = <i>x</i> + 3. What is the correct answer?</p>",
        "choices": ["x + 3 + 2 ÷ (x + 2)", "x + 3", "x + 4", "x + 3 − 2 ÷ (x + 2)"],
        "correct": "x + 3 + 2 ÷ (x + 2)",
        "explanation": "<p><strong>Qoldiq unutilgan.</strong> "
                       "(x + 2)(x + 3) = x² + 5x + 6, va 8 − 6 = 2.</p>"
                       "<p>Tekshiruv x = 0 da: 8 ÷ 2 = 4, va 3 + 1 = 4 ✓</p>",
    },
    {
        "text": "<p>Which expression is equivalent to (2<i>x</i><sup>2</sup> + "
                "3<i>x</i> + 4) ÷ (<i>x</i> + 1)?</p>",
        "choices": ["2x + 1 + 3 ÷ (x + 1)", "2x + 1", "2x + 3 + 1 ÷ (x + 1)", "2x + 4"],
        "correct": "2x + 1 + 3 ÷ (x + 1)",
        "explanation": "<p><strong>2x + 1 + 3 ÷ (x + 1).</strong> "
                       "(x + 1)(2x + 1) = 2x² + 3x + 1, va 4 − 1 = 3.</p>"
                       "<p>Tekshiruv x = 0 da: 4 ÷ 1 = 4, va 1 + 3 = 4 ✓</p>",
    },
    {
        "text": "<p>Simplify: (<i>x</i><sup>3</sup> − <i>x</i>) ÷ (<i>x</i><sup>2</sup> "
                "− <i>x</i>)</p>",
        "choices": ["x + 1", "x − 1", "x", "x² + 1"],
        "correct": "x + 1",
        "explanation": "<p><strong>x + 1.</strong> Surat x(x − 1)(x + 1), maxraj "
                       "x(x − 1) — ikkita umumiy koʻpaytuvchi qisqaradi.</p>"
                       "<p>Tekshiruv: x = 2 da 6 ÷ 2 = 3, va 2 + 1 = 3 ✓</p>",
    },
    {
        "text": "<p>A box holds <i>x</i><sup>2</sup> + 11<i>x</i> + 24 pencils packed "
                "in rows of <i>x</i> + 3. How many rows are there?</p>",
        "choices": ["x + 8", "x + 3", "x + 24", "x + 11"],
        "correct": "x + 8",
        "explanation": "<p><strong>x + 8.</strong> 24 = 3 × 8 va 3 + 8 = 11.</p>"
                       "<p>Tekshiruv: x = 1 da 36 qalam, qatorda 4 ta → 9 qator, va "
                       "1 + 8 = 9 ✓</p>",
    },
    {
        "text": "<p>A garden of area <i>x</i><sup>2</sup> + 5<i>x</i> + 9 square "
                "metres is divided into strips of width <i>x</i> + 2 metres. How much "
                "area is left over?</p>",
        "choices": ["3 square metres", "9 square metres", "2 square metres",
                    "1 square metre"],
        "correct": "3 square metres",
        "explanation": "<p><strong>3 m².</strong> (x + 2)(x + 3) = x² + 5x + 6, va "
                       "9 − 6 = 3 — bu qoldiq.</p>"
                       "<p>Qoldiq — «sigʻmay qolgan» qism, xuddi 17 ÷ 5 dagi 2 "
                       "kabi.</p>",
    },
]


# =====================================================================
# SAT-42 — remainder and factor theorems
# =====================================================================

Q_SAT42 = [
    {
        "text": "<p>What is the remainder when <i>P</i>(<i>x</i>) = "
                "<i>x</i><sup>2</sup> + 3<i>x</i> + 5 is divided by <i>x</i> − 1?</p>",
        "choices": ["9", "5", "3", "0"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> P(1) = 1 + 3 + 5 = 9.</p>"
                       "<p>Boʻlish umuman qilinmadi — bitta qoʻyish yetarli.</p>",
    },
    {
        "text": "<p>What is the remainder when <i>P</i>(<i>x</i>) = "
                "<i>x</i><sup>2</sup> + 3<i>x</i> + 5 is divided by <i>x</i> + 1?</p>",
        "choices": ["3", "9", "5", "−3"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> (x + 1) → x = −1: 1 − 3 + 5 = 3.</p>"
                       "<p><strong>9</strong> — P(1) hisoblangan; ishora "
                       "almashtirilmagan.</p>",
    },
    {
        "text": "<p>If <i>P</i>(5) = 0, which expression is a factor of "
                "<i>P</i>(<i>x</i>)?</p>",
        "choices": ["(x − 5)", "(x + 5)", "5", "(5x)"],
        "correct": "(x − 5)",
        "explanation": "<p><strong>(x − 5).</strong> Koʻpaytuvchi teoremasi: "
                       "P(a) = 0 ⟺ (x − a) koʻpaytuvchi.</p>"
                       "<p>Koʻpaytuvchi — qavs, son emas; 5 esa nol deyiladi.</p>",
    },
    {
        "text": "<p>Is (<i>x</i> − 2) a factor of <i>P</i>(<i>x</i>) = "
                "<i>x</i><sup>3</sup> − 3<i>x</i><sup>2</sup> + 4?</p>",
        "choices": ["Yes — P(2) = 0", "No — P(2) = 4", "Yes — P(−2) = 0",
                    "No — P(2) = 8"],
        "correct": "Yes — P(2) = 0",
        "explanation": "<p><strong>Ha.</strong> P(2) = 8 − 12 + 4 = 0.</p>"
                       "<p>Qoldiq nol — demak boʻlinish toʻliq.</p>",
    },
    {
        "text": "<p>What is the remainder when <i>P</i>(<i>x</i>) = "
                "<i>x</i><sup>3</sup> + 2<i>x</i> − 3 is divided by <i>x</i> − 2?</p>",
        "choices": ["9", "5", "−3", "13"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> P(2) = 8 + 4 − 3 = 9.</p>"
                       "<p>Kubik boʻlsa ham amal bir xil — bitta qoʻyish.</p>",
    },
    {
        "text": "<p>What is the remainder when <i>P</i>(<i>x</i>) = "
                "2<i>x</i><sup>3</sup> − <i>x</i> + 4 is divided by <i>x</i> + 2?</p>",
        "choices": ["−10", "18", "10", "−18"],
        "correct": "−10",
        "explanation": "<p><strong>−10.</strong> x = −2: 2(−8) + 2 + 4 = "
                       "−16 + 6 = −10.</p>"
                       "<p><strong>18</strong> — P(2) hisoblangan: 16 − 2 + 4.</p>",
    },
    {
        "text": "<p>Is (<i>x</i> + 1) a factor of <i>P</i>(<i>x</i>) = "
                "<i>x</i><sup>3</sup> + <i>x</i><sup>2</sup> − <i>x</i> − 1?</p>",
        "choices": ["Yes — P(−1) = 0", "No — P(−1) = 2", "Yes — P(1) = 0",
                    "No — P(1) = 0"],
        "correct": "Yes — P(−1) = 0",
        "explanation": "<p><strong>Ha.</strong> P(−1) = −1 + 1 + 1 − 1 = 0.</p>"
                       "<p>P(1) = 0 ham toʻgʻri, lekin u (x − 1) haqida gapiradi.</p>",
    },
    {
        "text": "<p>In <i>P</i>(<i>x</i>) = <i>x</i><sup>2</sup> + <i>kx</i> − 6, "
                "(<i>x</i> − 2) is a factor. What is <i>k</i>?</p>",
        "choices": ["1", "−1", "2", "3"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> P(2) = 4 + 2k − 6 = 0 → 2k = 2.</p>"
                       "<p>Tekshiruv: x² + x − 6 = (x − 2)(x + 3) ✓</p>",
    },
    {
        "text": "<p>In <i>P</i>(<i>x</i>) = <i>x</i><sup>3</sup> + <i>kx</i> + 6, "
                "(<i>x</i> + 1) is a factor. What is <i>k</i>?</p>",
        "choices": ["5", "−5", "7", "−7"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> P(−1) = −1 − k + 6 = 0 → k = 5.</p>"
                       "<p>Ishora ikki marta almashadi — avval x = −1, keyin "
                       "−k.</p>",
    },
    {
        "text": "<p>Which of these numbers is worth testing first as a possible zero "
                "of <i>P</i>(<i>x</i>) = <i>x</i><sup>3</sup> − 2<i>x</i><sup>2</sup> "
                "− 5<i>x</i> + 6?</p>",
        "choices": ["1, 2, 3 or 6 — the factors of the constant term",
                    "Any number at all", "Only 0", "Only negative numbers"],
        "correct": "1, 2, 3 or 6 — the factors of the constant term",
        "explanation": "<p><strong>Erkin hadning boʻluvchilari.</strong> Butun "
                       "ildizlar faqat shular orasidan chiqadi.</p>"
                       "<p>Bu yerda P(1) = 0, demak (x − 1) koʻpaytuvchi.</p>",
    },
    {
        "text": "<p>The graph of <i>P</i> crosses the <i>x</i>-axis at <i>x</i> = 3. "
                "Which must be true?</p>",
        "choices": ["P(3) = 0 and (x − 3) is a factor",
                    "P(0) = 3", "The remainder on dividing by x − 3 is 3",
                    "(x + 3) is a factor"],
        "correct": "P(3) = 0 and (x − 3) is a factor",
        "explanation": "<p><strong>P(3) = 0.</strong> Kesishish nuqtasi — nol, va nol "
                       "koʻpaytuvchini beradi.</p>"
                       "<p>«Nol», «ildiz», «koʻpaytuvchi», «kesishish» — bitta "
                       "faktning toʻrt nomi.</p>",
    },
    {
        "text": "<p><i>P</i>(<i>x</i>) leaves a remainder of 4 when divided by "
                "<i>x</i> − 1. What is <i>P</i>(1)?</p>",
        "choices": ["4", "0", "1", "−4"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Qoldiq teoremasi teskari tomonga ham "
                       "ishlaydi: qoldiq = P(1).</p>"
                       "<p>Savol koʻpincha shu yoʻnalishda beriladi.</p>",
    },
    {
        "text": "<p>A cubic polynomial has zeros at 1, −2 and 3. Which is a factor?</p>",
        "choices": ["(x + 2)", "(x − 2)", "(x + 1)", "(x + 3)"],
        "correct": "(x + 2)",
        "explanation": "<p><strong>(x + 2).</strong> Nol −2 boʻlsa, koʻpaytuvchi "
                       "(x − (−2)) = (x + 2).</p>"
                       "<p>Toʻliq koʻrinishi: (x − 1)(x + 2)(x − 3).</p>",
    },
    {
        "text": "<p>If <i>P</i>(<i>x</i>) = (<i>x</i> − 4)<i>Q</i>(<i>x</i>) + 7, what "
                "is <i>P</i>(4)?</p>",
        "choices": ["7", "0", "4", "It cannot be determined"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> x = 4 da birinchi qoʻshiluvchi nolga "
                       "aylanadi va faqat 7 qoladi.</p>"
                       "<p>Bu qoldiq teoremasining isboti — bir qatorda.</p>",
    },
    {
        "text": "<p>A student finds the remainder of <i>P</i>(<i>x</i>) = "
                "<i>x</i><sup>2</sup> + 4 divided by <i>x</i> + 3 by computing "
                "<i>P</i>(3) = 13. What is the correct remainder?</p>",
        "choices": ["13", "−13", "5", "−5"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> P(−3) = 9 + 4 = 13 — bu safar "
                       "javob bir xil chiqdi, chunki x kvadratda.</p>"
                       "<p>Lekin usul notoʻgʻri edi: (x + 3) uchun x = −3 qoʻyiladi. "
                       "Toq darajali hadli koʻphadda bu xato javobni buzadi.</p>",
    },
    {
        "text": "<p>A student says that because <i>P</i>(2) = 0, the number 2 is a "
                "factor of <i>P</i>. What is the correct statement?</p>",
        "choices": ["(x − 2) is a factor, and 2 is a zero",
                    "2 is a factor and a zero",
                    "(x + 2) is a factor",
                    "P has no factors"],
        "correct": "(x − 2) is a factor, and 2 is a zero",
        "explanation": "<p><strong>Koʻpaytuvchi — qavs.</strong> 2 esa nol (yoki "
                       "ildiz) deyiladi.</p>"
                       "<p>Bu atama farqi SAT savollarida ataylab ishlatiladi.</p>",
    },
    {
        "text": "<p>In <i>P</i>(<i>x</i>) = 2<i>x</i><sup>3</sup> + <i>kx</i><sup>2</sup> "
                "− 8, (<i>x</i> − 2) is a factor. What is <i>k</i>?</p>",
        "choices": ["−2", "2", "−4", "4"],
        "correct": "−2",
        "explanation": "<p><strong>−2.</strong> P(2) = 16 + 4k − 8 = 0 → 4k = −8.</p>"
                       "<p>Tekshiruv: 2x³ − 2x² − 8 da P(2) = 16 − 8 − 8 = 0 ✓</p>",
    },
    {
        "text": "<p><i>P</i>(<i>x</i>) = <i>x</i><sup>3</sup> − 6<i>x</i><sup>2</sup> "
                "+ 11<i>x</i> − 6 has a zero at <i>x</i> = 1. What are the other two "
                "zeros?</p>",
        "choices": ["2 and 3", "−2 and −3", "1 and 6", "6 and 11"],
        "correct": "2 and 3",
        "explanation": "<p><strong>2 va 3.</strong> P(2) = 8 − 24 + 22 − 6 = 0 ✓ va "
                       "P(3) = 27 − 54 + 33 − 6 = 0 ✓</p>"
                       "<p>Demak P(x) = (x − 1)(x − 2)(x − 3).</p>",
    },
    {
        "text": "<p>A company's profit is modelled by <i>P</i>(<i>x</i>) = "
                "<i>x</i><sup>3</sup> − 4<i>x</i><sup>2</sup> + <i>x</i> + 6, where "
                "<i>x</i> is the number of years. In which year does the profit first "
                "reach zero, for <i>x</i> greater than zero?</p>",
        "choices": ["Year 2", "Year 1", "Year 3", "Year 6"],
        "correct": "Year 2",
        "explanation": "<p><strong>2-yil.</strong> P(1) = 4, P(2) = 8 − 16 + 2 + 6 = "
                       "0 ✓</p>"
                       "<p>P(3) = 0 ham toʻgʻri, lekin savol <b>birinchi</b> "
                       "yilni soʻragan.</p>",
    },
    {
        "text": "<p>A tank's volume is <i>V</i>(<i>x</i>) = <i>x</i><sup>3</sup> + "
                "2<i>x</i><sup>2</sup> − 5<i>x</i> − 6 cubic metres. One dimension is "
                "(<i>x</i> + 1) metres. Is that consistent?</p>",
        "choices": ["Yes — V(−1) = 0, so (x + 1) is a factor",
                    "No — V(1) is not zero",
                    "Yes — V(1) = 0",
                    "It cannot be determined"],
        "correct": "Yes — V(−1) = 0, so (x + 1) is a factor",
        "explanation": "<p><strong>Ha.</strong> V(−1) = −1 + 2 + 5 − 6 = 0.</p>"
                       "<p>Oʻlcham koʻpaytuvchi boʻlishi kerak, va koʻpaytuvchi "
                       "teoremasi buni bir qadamda tasdiqlaydi.</p>",
    },
]


# =====================================================================
# SAT-43 — higher-degree graphs
# =====================================================================

Q_SAT43 = [
    {
        "text": "<p>What is the degree of <i>y</i> = (<i>x</i> − 2)<sup>3</sup>"
                "(<i>x</i> + 5)?</p>",
        "choices": ["4", "3", "5", "2"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Karraliliklar yigʻindisi: 3 + 1.</p>"
                       "<p>Qavslarni ochish shart emas.</p>",
    },
    {
        "text": "<p>Describe the end behavior of <i>y</i> = <i>x</i><sup>3</sup> − "
                "4<i>x</i>.</p>",
        "choices": ["Down on the left, up on the right", "Up on both ends",
                    "Down on both ends", "Up on the left, down on the right"],
        "correct": "Down on the left, up on the right",
        "explanation": "<p><strong>Chapda pastga, oʻngda yuqoriga.</strong> Toq "
                       "daraja, musbat bosh koeffitsient.</p>"
                       "<p>Toq daraja — chekkalar qarama-qarshi.</p>",
    },
    {
        "text": "<p>Describe the end behavior of <i>y</i> = −<i>x</i><sup>4</sup> + "
                "2<i>x</i><sup>2</sup>.</p>",
        "choices": ["Down on both ends", "Up on both ends",
                    "Down on the left, up on the right", "Up on the left, down on the right"],
        "correct": "Down on both ends",
        "explanation": "<p><strong>Ikkala chekka ham pastga.</strong> Juft daraja, "
                       "manfiy bosh koeffitsient.</p>"
                       "<p>Juft daraja — chekkalar bir xil tomonda.</p>",
    },
    {
        "text": "<p>At which zero does the graph of <i>y</i> = <i>x</i>"
                "(<i>x</i> − 4)<sup>2</sup> touch the <i>x</i>-axis without crossing "
                "it?</p>",
        "choices": ["x = 4", "x = 0", "x = −4", "x = 2"],
        "correct": "x = 4",
        "explanation": "<p><strong>x = 4.</strong> Karraliligi 2 — juft, demak "
                       "urinish.</p>"
                       "<p>x = 0 da karralilik 1 — toq, demak kesish.</p>",
    },
    {
        "text": "<p>At which zero does the graph of <i>y</i> = (<i>x</i> + 3)"
                "<sup>2</sup>(<i>x</i> − 1) cross the <i>x</i>-axis?</p>",
        "choices": ["x = 1", "x = −3", "x = 3", "x = −1"],
        "correct": "x = 1",
        "explanation": "<p><strong>x = 1.</strong> Karraliligi 1 — toq.</p>"
                       "<p>x = −3 da karralilik 2, grafik tegib qaytadi.</p>",
    },
    {
        "text": "<p>A polynomial graph has 3 turning points. What is the least "
                "possible degree?</p>",
        "choices": ["4", "3", "2", "5"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Burilishlar soni koʻpi bilan "
                       "daraja − 1.</p>"
                       "<p>Uch burilish uchun daraja kamida 4 boʻlishi kerak.</p>",
    },
    {
        "text": "<p>What are the zeros of <i>y</i> = (<i>x</i> − 5)(<i>x</i> + 1)"
                "<sup>2</sup>?</p>",
        "choices": ["5 and −1", "−5 and 1", "5 and 1", "−5 and −1"],
        "correct": "5 and −1",
        "explanation": "<p><strong>5 va −1.</strong> Har bir qavsni nolga "
                       "tenglashtiring.</p>"
                       "<p>Karralilik nollarning <b>oʻrnini</b> oʻzgartirmaydi, faqat "
                       "grafikning ulardagi xatti-harakatini belgilaydi.</p>",
    },
    {
        "text": "<p>How many <i>x</i>-intercepts does <i>y</i> = (<i>x</i> − 2)"
                "<sup>2</sup>(<i>x</i> + 3)<sup>2</sup> have?</p>",
        "choices": ["Two", "Four", "One", "Zero"],
        "correct": "Two",
        "explanation": "<p><strong>Ikkita.</strong> Nollar 2 va −3 — daraja 4 "
                       "boʻlsa ham, turli nollar ikkita.</p>"
                       "<p>Grafik ikkalasida ham tegib qaytadi, kesmaydi.</p>",
    },
    {
        "text": "<p>For <i>y</i> = 3<i>x</i><sup>5</sup> − <i>x</i> + 7, what happens "
                "as <i>x</i> decreases without bound?</p>",
        "choices": ["y decreases without bound", "y increases without bound",
                    "y approaches 7", "y approaches zero"],
        "correct": "y decreases without bound",
        "explanation": "<p><strong>Pastga cheksiz ketadi.</strong> Toq daraja, musbat "
                       "bosh koeffitsient → chap chekka pastda.</p>"
                       "<p><strong>approaches 7</strong> — erkin had chekkaga "
                       "taʼsir qilmaydi.</p>",
    },
    {
        "text": "<p>Which polynomial has a graph that touches the <i>x</i>-axis at "
                "<i>x</i> = 2 and crosses it at <i>x</i> = −1?</p>",
        "choices": ["y = (x − 2)²(x + 1)", "y = (x + 2)²(x − 1)",
                    "y = (x − 2)(x + 1)²", "y = (x − 2)(x + 1)"],
        "correct": "y = (x − 2)²(x + 1)",
        "explanation": "<p><strong>(x − 2)²(x + 1).</strong> x = 2 juft karralilik "
                       "(urinish), x = −1 toq (kesish).</p>"
                       "<p>Uchinchi variantda rollar almashgan.</p>",
    },
    {
        "text": "<p>A graph goes down on the left and up on the right. What can you "
                "say about the polynomial?</p>",
        "choices": ["Odd degree with a positive leading coefficient",
                    "Even degree with a positive leading coefficient",
                    "Odd degree with a negative leading coefficient",
                    "Even degree with a negative leading coefficient"],
        "correct": "Odd degree with a positive leading coefficient",
        "explanation": "<p><strong>Toq daraja, musbat bosh koeffitsient.</strong></p>"
                       "<p>Chekkalar qarama-qarshi → toq; oʻng chekka yuqorida → "
                       "musbat.</p>",
    },
    {
        "text": "<p>Which feature of a polynomial determines its end behavior?</p>",
        "choices": ["The degree and the leading coefficient",
                    "The constant term", "The number of zeros",
                    "The number of turning points"],
        "correct": "The degree and the leading coefficient",
        "explanation": "<p><strong>Daraja va bosh koeffitsient.</strong> Katta x da "
                       "bosh had qolgan hamma haddan ustun keladi.</p>"
                       "<p>Erkin had faqat y oʻqidagi nuqtani beradi.</p>",
    },
    {
        "text": "<p>The graph of a polynomial goes up on both ends and has 3 "
                "<i>x</i>-intercepts. What is the least possible degree?</p>",
        "choices": ["4", "3", "5", "6"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Ikkala chekka bir xil → juft daraja; "
                       "eng kichik juft daraja uchta nolni koʻtara oladigani 4.</p>"
                       "<p>3 boʻlishi mumkin emas — u toq daraja.</p>",
    },
    {
        "text": "<p>What is the <i>y</i>-intercept of <i>y</i> = (<i>x</i> − 2)"
                "(<i>x</i> + 3)(<i>x</i> − 1)?</p>",
        "choices": ["(0, 6)", "(0, −6)", "(0, 0)", "(6, 0)"],
        "correct": "(0, 6)",
        "explanation": "<p><strong>(0, 6).</strong> x = 0 qoʻying: "
                       "(−2)(3)(−1) = 6.</p>"
                       "<p>Ikkita minus koʻpaytmasi plyus beradi.</p>",
    },
    {
        "text": "<p>A student says the graph of <i>y</i> = (<i>x</i> + 4)<sup>2</sup>"
                "(<i>x</i> − 1) touches the axis at <i>x</i> = 4. What is the correct "
                "answer?</p>",
        "choices": ["x = −4", "x = 4", "x = 1", "x = −1"],
        "correct": "x = −4",
        "explanation": "<p><strong>x = −4.</strong> Qavsning noli — ichidagi sonning "
                       "qarama-qarshisi.</p>"
                       "<p>Karralilik toʻgʻri aniqlangan, faqat ishora "
                       "koʻchirilmagan.</p>",
    },
    {
        "text": "<p>A student says that <i>y</i> = −2<i>x</i><sup>3</sup> + 7 "
                "approaches 7 at both ends. What actually happens?</p>",
        "choices": ["It goes up on the left and down on the right",
                    "It approaches 7", "It goes down on both ends",
                    "It goes up on both ends"],
        "correct": "It goes up on the left and down on the right",
        "explanation": "<p><strong>Chapda yuqoriga, oʻngda pastga.</strong> Toq "
                       "daraja, manfiy bosh koeffitsient.</p>"
                       "<p>Erkin had 7 faqat y oʻqidagi nuqtani beradi, chekkani "
                       "emas.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = <i>a</i>(<i>x</i> − 1)<sup>2</sup>"
                "(<i>x</i> + 2) passes through (0, 4). What is the value of "
                "<i>a</i>?</p>",
        "choices": ["2", "4", "−2", "1"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> x = 0: a(1)(2) = 2a = 4 → a = 2.</p>"
                       "<p>(0 − 1)² = 1, (0 + 2) = 2 — ishoralarga eʼtibor "
                       "bering.</p>",
    },
    {
        "text": "<p>A polynomial has zeros at −2, 1 and 3, with 1 having multiplicity "
                "2. What is its degree?</p>",
        "choices": ["4", "3", "5", "2"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Karraliliklar: 1 + 2 + 1.</p>"
                       "<p>Uchta turli nol, lekin daraja toʻrt — grafik x oʻqiga "
                       "toʻrt marta «tegadi», uch joyda.</p>",
    },
    {
        "text": "<p>A profit model <i>P</i>(<i>x</i>) has zeros at <i>x</i> = 2 and "
                "<i>x</i> = 8, and <i>P</i> is negative outside that interval. What "
                "can you say about the graph?</p>",
        "choices": ["It opens downward and profit is positive only between 2 and 8",
                    "It opens upward",
                    "Profit is always positive",
                    "It touches the axis at 2 and 8"],
        "correct": "It opens downward and profit is positive only between 2 and 8",
        "explanation": "<p><strong>Pastga ochiladi.</strong> Ikki nol tashqarisida "
                       "manfiy — demak grafikning uchi yuqorida.</p>"
                       "<p>Kontekstda: faqat 2 va 8 orasida foyda bor.</p>",
    },
    {
        "text": "<p>A container's volume is <i>V</i>(<i>x</i>) = <i>x</i>"
                "(10 − 2<i>x</i>)<sup>2</sup> cubic centimetres. For which positive "
                "value of <i>x</i> is the volume zero?</p>",
        "choices": ["5", "10", "2", "0"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 10 − 2x = 0 → x = 5.</p>"
                       "<p>x = 0 ham nol beradi, lekin savol <b>musbat</b> qiymatni "
                       "soʻragan.</p>",
    },
]


# =====================================================================
# SAT-44 — exponential vs linear
# =====================================================================

Q_SAT44 = [
    {
        "text": "<p>Is the sequence 3, 7, 11, 15 linear or exponential?</p>",
        "choices": ["Linear — it adds 4 each time", "Exponential — it multiplies by 4",
                    "Neither", "Exponential — it multiplies by 2"],
        "correct": "Linear — it adds 4 each time",
        "explanation": "<p><strong>Chiziqli.</strong> Ayirmalar 4, 4, 4 — bir xil.</p>"
                       "<p>Nisbatlar esa 2.33, 1.57, 1.36 — bir xil emas.</p>",
    },
    {
        "text": "<p>Is the sequence 3, 6, 12, 24 linear or exponential?</p>",
        "choices": ["Exponential — it multiplies by 2", "Linear — it adds 3",
                    "Linear — it adds 6", "Neither"],
        "correct": "Exponential — it multiplies by 2",
        "explanation": "<p><strong>Koʻrsatkichli.</strong> Nisbatlar 2, 2, 2.</p>"
                       "<p>Ayirmalar 3, 6, 12 — oʻsib boradi, demak chiziqli "
                       "emas.</p>",
    },
    {
        "text": "<p>A savings account grows by 4% each year. Which model is this?</p>",
        "choices": ["Exponential", "Linear", "Neither", "Both"],
        "correct": "Exponential",
        "explanation": "<p><strong>Koʻrsatkichli.</strong> Foiz — koʻpaytirish.</p>"
                       "<p>Har yili qoʻshiladigan pul oʻsib boradi, chunki foiz "
                       "kattaroq summadan olinadi.</p>",
    },
    {
        "text": "<p>A worker earns 200,000 som plus 50,000 som for each hour worked. "
                "Which model is this?</p>",
        "choices": ["Linear", "Exponential", "Neither", "Exponential decay"],
        "correct": "Linear",
        "explanation": "<p><strong>Chiziqli.</strong> Har soatga bir xil miqdor "
                       "qoʻshiladi.</p>"
                       "<p>200,000 — boshlangʻich qiymat, 50,000 — qiyalik "
                       "(SAT-5).</p>",
    },
    {
        "text": "<p>A table shows 6, 18, 54, 162. Which model fits?</p>",
        "choices": ["Exponential, ratio 3", "Linear, difference 12",
                    "Linear, difference 3", "Neither"],
        "correct": "Exponential, ratio 3",
        "explanation": "<p><strong>Koʻrsatkichli, nisbat 3.</strong></p>"
                       "<p><strong>difference 12</strong> — faqat birinchi qadamda "
                       "toʻgʻri; keyingisi 36.</p>",
    },
    {
        "text": "<p>A table shows 100, 85, 70, 55. Which model fits?</p>",
        "choices": ["Linear, decreasing by 15", "Exponential, ratio 0.85",
                    "Exponential, ratio 0.15", "Neither"],
        "correct": "Linear, decreasing by 15",
        "explanation": "<p><strong>Chiziqli.</strong> Har safar 15 ayiriladi — "
                       "ayirmalar bir xil.</p>"
                       "<p><strong>ratio 0.85</strong> boʻlsa 100, 85, 72.25 "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>A table shows 100, 85, 72.25, 61.4125. Which model fits?</p>",
        "choices": ["Exponential, ratio 0.85", "Linear, decreasing by 15",
                    "Exponential, ratio 0.15", "Neither"],
        "correct": "Exponential, ratio 0.85",
        "explanation": "<p><strong>Koʻrsatkichli, nisbat 0.85.</strong> Har safar "
                       "15 foizdan tushadi.</p>"
                       "<p>Ayirmalar 15, 12.75, 10.8375 — kichrayib boradi, demak "
                       "chiziqli emas.</p>",
    },
    {
        "text": "<p>A population doubles every 5 years. Which model is this?</p>",
        "choices": ["Exponential", "Linear", "Neither", "Linear with slope 2"],
        "correct": "Exponential",
        "explanation": "<p><strong>Koʻrsatkichli.</strong> «Doubles» — koʻpaytirish.</p>"
                       "<p>Davr 5 yil boʻlishi modelni oʻzgartirmaydi, faqat "
                       "koʻrsatkichni (SAT-45).</p>",
    },
    {
        "text": "<p>Two models start at 10. One adds 5 each step; the other multiplies "
                "by 1.5. Which is larger after 2 steps?</p>",
        "choices": ["The linear one — 20 against 22.5",
                    "The exponential one — 22.5 against 20",
                    "They are equal", "The linear one — 20 against 15"],
        "correct": "The exponential one — 22.5 against 20",
        "explanation": "<p><strong>Koʻrsatkichli.</strong> 10 → 15 → 22.5, "
                       "chiziqli esa 10 → 15 → 20.</p>"
                       "<p>Birinchi qadamda ikkalasi ham 15 — keyin yoʻllar "
                       "ajraladi.</p>",
    },
    {
        "text": "<p>Which statement about exponential and linear growth is true?</p>",
        "choices": ["Exponential growth eventually exceeds any linear growth",
                    "Linear growth is always faster",
                    "They always cross exactly once at the start",
                    "Exponential growth is faster from the very first step"],
        "correct": "Exponential growth eventually exceeds any linear growth",
        "explanation": "<p><strong>Oxir-oqibat ortda qoldiradi.</strong> Boshlanishi "
                       "qanchalik kichik boʻlsa ham.</p>"
                       "<p>Boshida chiziqli koʻpincha oldinda boʻladi — bu "
                       "«eventually» soʻzining maʼnosi.</p>",
    },
    {
        "text": "<p>A phone's value falls from 800 to 640 to 512 dollars in "
                "successive years. What is happening?</p>",
        "choices": ["It loses 20% of its value each year",
                    "It loses 160 dollars each year",
                    "It loses 20 dollars each year",
                    "It loses 80% of its value each year"],
        "correct": "It loses 20% of its value each year",
        "explanation": "<p><strong>Har yili 20 foizdan.</strong> 640 ÷ 800 = 0.8 va "
                       "512 ÷ 640 = 0.8.</p>"
                       "<p><strong>160 dollar</strong> — faqat birinchi yil; "
                       "ikkinchisida 128.</p>",
    },
    {
        "text": "<p>Which situation is best modelled by a linear function?</p>",
        "choices": ["A tank drains 4 litres every minute",
                    "A bacteria colony triples every hour",
                    "An investment grows 7% a year",
                    "A drug's concentration halves every 6 hours"],
        "correct": "A tank drains 4 litres every minute",
        "explanation": "<p><strong>Bak.</strong> Har daqiqada bir xil <b>miqdor</b> "
                       "ketadi.</p>"
                       "<p>Qolgan uchtasi — koʻpaytirish (uch barobar, foiz, "
                       "yarmi).</p>",
    },
    {
        "text": "<p>The graph of an exponential growth function looks almost flat at "
                "first. What does this mean?</p>",
        "choices": ["Nothing about the model — it will still overtake a line later",
                    "The model is actually linear",
                    "The growth rate is negative",
                    "The graph will stay flat"],
        "correct": "Nothing about the model — it will still overtake a line later",
        "explanation": "<p><strong>Hech narsani.</strong> Koʻrsatkichli oʻsish boshida "
                       "sekin koʻrinadi.</p>"
                       "<p>Rasmning chap tomoniga qarab xulosa chiqarmang.</p>",
    },
    {
        "text": "<p>A city's population rises from 50,000 by 2,000 people each year. "
                "Which model is this?</p>",
        "choices": ["Linear", "Exponential growth", "Exponential decay", "Neither"],
        "correct": "Linear",
        "explanation": "<p><strong>Chiziqli.</strong> «2,000 people» — miqdor, foiz "
                       "emas.</p>"
                       "<p>«by 4% each year» boʻlganda koʻrsatkichli boʻlardi.</p>",
    },
    {
        "text": "<p>A student says 2, 6, 18, 54 is linear because it increases by 4 "
                "then 12. What is the correct description?</p>",
        "choices": ["Exponential with ratio 3", "Linear with difference 4",
                    "Linear with difference 12", "Neither"],
        "correct": "Exponential with ratio 3",
        "explanation": "<p><strong>Koʻrsatkichli, nisbat 3.</strong> Oʻquvchi "
                       "ayirmalar bir xil emasligini payqagan, lekin xulosa "
                       "chiqarmagan.</p>"
                       "<p>Ayirmalar bir xil boʻlmasa, nisbatlarni tekshiring.</p>",
    },
    {
        "text": "<p>A student says that a 5% yearly rise means adding 5 each year. "
                "For a starting value of 200, what is added in the second year?</p>",
        "choices": ["10.50", "10", "5", "20"],
        "correct": "10.50",
        "explanation": "<p><strong>10.50.</strong> Birinchi yil 200 × 0.05 = 10, "
                       "demak yangi qiymat 210; ikkinchi yil 210 × 0.05 = 10.50.</p>"
                       "<p>Qoʻshiladigan son har yili oʻsadi — bu koʻrsatkichli "
                       "modelning belgisi.</p>",
    },
    {
        "text": "<p>Two accounts start at 1,000. Account A adds 100 a year; account B "
                "grows 8% a year. Which is larger after 1 year?</p>",
        "choices": ["Account A — 1,100 against 1,080",
                    "Account B — 1,080 against 1,100",
                    "They are equal",
                    "Account B — 1,800 against 1,100"],
        "correct": "Account A — 1,100 against 1,080",
        "explanation": "<p><strong>A.</strong> 1,000 + 100 = 1,100, va "
                       "1,000 × 1.08 = 1,080.</p>"
                       "<p>Chiziqli boshida oldinda — lekin B keyinroq oʻzib "
                       "ketadi.</p>",
    },
    {
        "text": "<p>For those same two accounts, which is larger after 10 years?</p>",
        "choices": ["Account B — about 2,159 against 2,000",
                    "Account A — 2,000 against 1,800",
                    "They are equal",
                    "Account A — 2,000 against 1,080"],
        "correct": "Account B — about 2,159 against 2,000",
        "explanation": "<p><strong>B.</strong> 1,000 × 1.08 oʻn marta ≈ 2,159, "
                       "A esa 1,000 + 1,000 = 2,000.</p>"
                       "<p>Koʻrsatkichli oʻsish oxir-oqibat oʻzib ketdi — bu "
                       "SAT-44 ning asosiy gʻoyasi.</p>",
    },
    {
        "text": "<p>A pond's algae cover doubles every week, starting from 1 square "
                "metre. After how many weeks does it first exceed 100 square "
                "metres?</p>",
        "choices": ["7 weeks", "50 weeks", "10 weeks", "100 weeks"],
        "correct": "7 weeks",
        "explanation": "<p><strong>7 hafta.</strong> 1, 2, 4, 8, 16, 32, 64, 128 — "
                       "yettinchi haftada 128.</p>"
                       "<p>Oltinchi haftada hali 64 — yuzdan kam.</p>",
    },
    {
        "text": "<p>A car bought for 30,000 dollars is worth 24,000 after one year "
                "and 19,200 after two. What will it be worth after three years?</p>",
        "choices": ["15,360 dollars", "14,400 dollars", "16,000 dollars",
                    "18,000 dollars"],
        "correct": "15,360 dollars",
        "explanation": "<p><strong>15,360.</strong> Nisbat 24,000 ÷ 30,000 = 0.8, "
                       "demak 19,200 × 0.8.</p>"
                       "<p><strong>14,400</strong> — har yili 4,800 ayirilgan, "
                       "yaʼni chiziqli hisoblangan.</p>",
    },
]


# =====================================================================
# SAT-45 — writing exponential functions
# =====================================================================

Q_SAT45 = [
    {
        "text": "<p>A colony starts with 400 bacteria and doubles every hour. Which "
                "function gives the number after <i>t</i> hours?</p>",
        "choices": ["400(2)^t", "400(0.5)^t", "400 + 2t", "2(400)^t"],
        "correct": "400(2)^t",
        "explanation": "<p><strong>400(2)^t.</strong> a = 400, b = 2.</p>"
                       "<p><strong>2(400)^t</strong> — a va b oʻrin almashgan; "
                       "u t = 0 da 2 beradi.</p>",
    },
    {
        "text": "<p>A 900-dollar phone loses 10% of its value each year. Which "
                "function gives its value after <i>t</i> years?</p>",
        "choices": ["900(0.9)^t", "900(1.1)^t", "900(0.1)^t", "900 − 10t"],
        "correct": "900(0.9)^t",
        "explanation": "<p><strong>900(0.9)^t.</strong> b = 1 − 0.1 = 0.9.</p>"
                       "<p>Tekshiruv: bir yildan keyin 810 — bu 900 ning 10 foizi "
                       "kamaygani ✓</p>",
    },
    {
        "text": "<p>An investment of 2,000 grows by 6% each year. What is <i>b</i> in "
                "the model?</p>",
        "choices": ["1.06", "0.06", "6", "0.94"],
        "correct": "1.06",
        "explanation": "<p><strong>1.06.</strong> Eskisi (1) + qoʻshimchasi "
                       "(0.06).</p>"
                       "<p><strong>0.06</strong> — bu model har yili 94 foizni "
                       "yoʻqotardi.</p>",
    },
    {
        "text": "<p>A quantity decreases by 25% each period. What is <i>b</i>?</p>",
        "choices": ["0.75", "1.25", "0.25", "−0.25"],
        "correct": "0.75",
        "explanation": "<p><strong>0.75.</strong> 1 − 0.25 — chorak ketadi, uch "
                       "chorak qoladi.</p>"
                       "<p>Kamayishda b har doim 0 va 1 orasida.</p>",
    },
    {
        "text": "<p>A town of 5,000 grows by 2% a year. What is its population after "
                "1 year?</p>",
        "choices": ["5,100", "5,002", "5,200", "5,020"],
        "correct": "5,100",
        "explanation": "<p><strong>5,100.</strong> 5,000 × 1.02 = 5,100.</p>"
                       "<p>2 foiz 5,000 dan — bu 100 kishi.</p>",
    },
    {
        "text": "<p>For that same town, what is the population after 2 years, to the "
                "nearest whole number?</p>",
        "choices": ["5,202", "5,200", "5,204", "5,100"],
        "correct": "5,202",
        "explanation": "<p><strong>5,202.</strong> 5,100 × 1.02 = 5,202.</p>"
                       "<p><strong>5,200</strong> — har yili 100 qoʻshilgan, yaʼni "
                       "chiziqli; ikkinchi yilda 102 qoʻshilishi kerak.</p>",
    },
    {
        "text": "<p>A 1,600-dollar machine loses a quarter of its value each year. "
                "What is it worth after 2 years?</p>",
        "choices": ["900 dollars", "800 dollars", "1,200 dollars", "400 dollars"],
        "correct": "900 dollars",
        "explanation": "<p><strong>900.</strong> 1,600 × 0.75 = 1,200, keyin "
                       "1,200 × 0.75 = 900.</p>"
                       "<p><strong>800</strong> — har yili 400 ayirilgan, chiziqli "
                       "hisob.</p>",
    },
    {
        "text": "<p>In the model <i>y</i> = 250(1.04)^<i>t</i>, what does 250 "
                "represent?</p>",
        "choices": ["The initial value", "The yearly increase",
                    "The growth rate", "The value after one year"],
        "correct": "The initial value",
        "explanation": "<p><strong>Boshlangʻich qiymat.</strong> t = 0 da har qanday "
                       "son nol darajada 1, demak y = 250.</p>"
                       "<p>Bir yildan keyingi qiymat esa 260.</p>",
    },
    {
        "text": "<p>In the model <i>y</i> = 250(1.04)^<i>t</i>, what is the yearly "
                "percentage increase?</p>",
        "choices": ["4%", "1.04%", "104%", "0.04%"],
        "correct": "4%",
        "explanation": "<p><strong>4%.</strong> b = 1 + r, demak r = 0.04.</p>"
                       "<p>Koeffitsientdan foizni qaytarish uchun 1 ni ayiring.</p>",
    },
    {
        "text": "<p>In the model <i>y</i> = 80(0.7)^<i>t</i>, what is the yearly "
                "percentage decrease?</p>",
        "choices": ["30%", "70%", "0.7%", "7%"],
        "correct": "30%",
        "explanation": "<p><strong>30%.</strong> 1 − 0.7 = 0.3.</p>"
                       "<p><strong>70%</strong> — bu <b>qoladigan</b> qism, "
                       "yoʻqolgani emas.</p>",
    },
    {
        "text": "<p>Which model describes a quantity that halves every period?</p>",
        "choices": ["y = a(0.5)^t", "y = a(2)^t", "y = a(1.5)^t", "y = a − 0.5t"],
        "correct": "y = a(0.5)^t",
        "explanation": "<p><strong>a(0.5)^t.</strong> Yarmi qoladi.</p>"
                       "<p>Bu model dori miqdori yoki radioaktiv yemirilish uchun "
                       "ishlatiladi.</p>",
    },
    {
        "text": "<p>A quantity is modelled by <i>y</i> = 60(1.5)^<i>t</i>. What is "
                "<i>y</i> when <i>t</i> = 0?</p>",
        "choices": ["60", "90", "1.5", "0"],
        "correct": "60",
        "explanation": "<p><strong>60.</strong> 1.5 nol darajada 1 ga teng.</p>"
                       "<p>Bu modelni tekshirishning eng tez usuli.</p>",
    },
    {
        "text": "<p>A bacteria colony of 200 doubles every 4 hours. How many are there "
                "after 12 hours?</p>",
        "choices": ["1,600", "800", "600", "2,400"],
        "correct": "1,600",
        "explanation": "<p><strong>1,600.</strong> 12 ÷ 4 = 3 marta ikkilanadi: "
                       "400, 800, 1,600.</p>"
                       "<p><strong>800</strong> — ikki marta ikkilangan; 12 soatda "
                       "uch davr bor.</p>",
    },
    {
        "text": "<p>A medicine's concentration halves every 6 hours, starting at "
                "80 mg. How much is left after 18 hours?</p>",
        "choices": ["10 mg", "20 mg", "40 mg", "5 mg"],
        "correct": "10 mg",
        "explanation": "<p><strong>10 mg.</strong> Uch davr: 40, 20, 10.</p>"
                       "<p>18 ÷ 6 = 3 — davrlar sonini sanang.</p>",
    },
    {
        "text": "<p>A student models '500 increasing by 8% a year' as "
                "500(0.08)^<i>t</i>. What is the correct model?</p>",
        "choices": ["500(1.08)^t", "500(0.08)^t", "500(8)^t", "500 + 8t"],
        "correct": "500(1.08)^t",
        "explanation": "<p><strong>500(1.08)^t.</strong> Oʻquvchining modeli bir "
                       "yildan keyin 40 beradi — 92 foiz yoʻqolgan boʻlardi.</p>"
                       "<p>Oʻsishda b har doim birdan katta.</p>",
    },
    {
        "text": "<p>A student says a 12% yearly decrease gives <i>b</i> = 1.12. What "
                "is the correct value?</p>",
        "choices": ["0.88", "1.12", "0.12", "−0.12"],
        "correct": "0.88",
        "explanation": "<p><strong>0.88.</strong> Kamayishda b = 1 − 0.12.</p>"
                       "<p>1.12 oʻsishni bildiradi — ishora teskari.</p>",
    },
    {
        "text": "<p>A quantity grows from 300 to 363 in two years at a constant "
                "percentage rate. What is the yearly rate?</p>",
        "choices": ["10%", "21%", "11%", "5%"],
        "correct": "10%",
        "explanation": "<p><strong>10%.</strong> 300 × 1.1 = 330, va "
                       "330 × 1.1 = 363 ✓</p>"
                       "<p><strong>21%</strong> — bu ikki yillik umumiy oʻsish, "
                       "yillik emas.</p>",
    },
    {
        "text": "<p>Which function models a population of 12,000 falling by 3% each "
                "year for <i>t</i> years?</p>",
        "choices": ["12,000(0.97)^t", "12,000(1.03)^t", "12,000(0.03)^t",
                    "12,000 − 3t"],
        "correct": "12,000(0.97)^t",
        "explanation": "<p><strong>12,000(0.97)^t.</strong> b = 1 − 0.03.</p>"
                       "<p>Tekshiruv: bir yildan keyin 11,640 — 360 kishi kam, "
                       "bu 12,000 ning 3 foizi ✓</p>",
    },
    {
        "text": "<p>A rumour starts with 3 people and the number who have heard it "
                "triples each day. How many have heard it after 4 days?</p>",
        "choices": ["243", "81", "12", "729"],
        "correct": "243",
        "explanation": "<p><strong>243.</strong> 3 → 9 → 27 → 81 → 243.</p>"
                       "<p>Toʻrt kun — toʻrt marta uchlanish, boshlangʻich 3 dan "
                       "boshlab.</p>",
    },
    {
        "text": "<p>A forest of 4,000 trees loses 5% each year to disease. How many "
                "remain after 2 years, to the nearest whole number?</p>",
        "choices": ["3,610", "3,600", "3,800", "3,620"],
        "correct": "3,610",
        "explanation": "<p><strong>3,610.</strong> 4,000 × 0.95 = 3,800, keyin "
                       "3,800 × 0.95 = 3,610.</p>"
                       "<p><strong>3,600</strong> — har yili 200 ayirilgan; "
                       "ikkinchi yilda 190 ketishi kerak edi.</p>",
    },
]


# =====================================================================
# Testlar
# =====================================================================

PRACTICES = [
    {
        "title":       "SAT-41 Practice: Simplifying Rational Expressions & Polynomial Division",
        "description": "20 ta SAT uslubidagi savol — ajratib qisqartirish, had va "
                       "koʻpaytuvchi farqi, qoldiqli koʻrinish.",
        "tutorial":    "SAT-41:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT41,
    },
    {
        "title":       "SAT-42 Practice: The Remainder Theorem and the Factor Theorem",
        "description": "20 ta SAT uslubidagi savol — qoldiq P(a), koʻpaytuvchi "
                       "teoremasi, ishora tuzogʻi va noma'lum koeffitsient.",
        "tutorial":    "SAT-42:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT42,
    },
    {
        "title":       "SAT-43 Practice: Graphs of Higher-Degree Polynomials — End Behavior & Multiplicity",
        "description": "20 ta SAT uslubidagi savol — chekka xatti-harakati, "
                       "karralilik, burilishlar soni va daraja.",
        "tutorial":    "SAT-43:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT43,
    },
    {
        "title":       "SAT-44 Practice: Exponential vs. Linear Growth",
        "description": "20 ta SAT uslubidagi savol — jadvalni ayirish va boʻlish, "
                       "foiz va miqdor farqi, koʻrsatkichlining ustunligi.",
        "tutorial":    "SAT-44:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT44,
    },
    {
        "title":       "SAT-45 Practice: Writing Exponential Functions (y = ab^x) from Word Problems",
        "description": "20 ta SAT uslubidagi savol — a va b ni matndan olish, foizni "
                       "koeffitsientga aylantirish, davrlarni sanash.",
        "tutorial":    "SAT-45:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT45,
    },
]
