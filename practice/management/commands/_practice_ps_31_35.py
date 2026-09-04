# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-31 … SAT-35.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context & interpretation ·
      15–16 trap-spotting · 17–18 Module 2 level · 19–20 word problems.

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_31_35.py --master=prime \\
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
# SAT-31 — factoring x² + bx + c
# =====================================================================

Q_SAT31 = [
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> + 5<i>x</i> + 6</p>",
        "choices": ["(x + 2)(x + 3)", "(x + 1)(x + 6)", "(x − 2)(x − 3)", "(x + 5)(x + 6)"],
        "correct": "(x + 2)(x + 3)",
        "explanation": "<p><strong>(x + 2)(x + 3).</strong> 2 × 3 = 6 va 2 + 3 = 5 ✓</p>"
                       "<p><strong>(x + 1)(x + 6)</strong> — koʻpaytmasi 6, lekin "
                       "yigʻindisi 7. Ikkala shart ham bajarilishi kerak.</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> + 7<i>x</i> + 10</p>",
        "choices": ["(x + 2)(x + 5)", "(x + 1)(x + 10)", "(x − 2)(x − 5)", "(x + 3)(x + 4)"],
        "correct": "(x + 2)(x + 5)",
        "explanation": "<p><strong>(x + 2)(x + 5).</strong> 2 × 5 = 10 va 2 + 5 = 7 ✓</p>"
                       "<p><strong>(x + 3)(x + 4)</strong> — yigʻindisi 7 ✓ lekin "
                       "koʻpaytmasi 12, 10 emas.</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> − 4<i>x</i> + 3</p>",
        "choices": ["(x − 1)(x − 3)", "(x + 1)(x + 3)", "(x − 1)(x + 3)", "(x + 1)(x − 3)"],
        "correct": "(x − 1)(x − 3)",
        "explanation": "<p><strong>(x − 1)(x − 3).</strong> c musbat, b manfiy — demak "
                       "ikkala son ham manfiy.</p>"
                       "<p><strong>(x + 1)(x − 3)</strong> ochilganda x² − 2x − 3 "
                       "beradi.</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> − 9<i>x</i> + 20</p>",
        "choices": ["(x − 4)(x − 5)", "(x + 4)(x + 5)", "(x − 2)(x − 10)", "(x − 1)(x − 20)"],
        "correct": "(x − 4)(x − 5)",
        "explanation": "<p><strong>(x − 4)(x − 5).</strong> (−4)(−5) = 20 va "
                       "−4 + (−5) = −9 ✓</p>"
                       "<p><strong>(x − 2)(x − 10)</strong> — koʻpaytmasi 20, "
                       "yigʻindisi −12.</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> + <i>x</i> − 6</p>",
        "choices": ["(x + 3)(x − 2)", "(x − 3)(x + 2)", "(x + 6)(x − 1)", "(x + 3)(x + 2)"],
        "correct": "(x + 3)(x − 2)",
        "explanation": "<p><strong>(x + 3)(x − 2).</strong> c manfiy → ishoralar har "
                       "xil; b = +1 boʻlgani uchun kattarogʻi musbat.</p>"
                       "<p><strong>(x − 3)(x + 2)</strong> — ishoralar teskari, u "
                       "x² − x − 6 beradi.</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> − <i>x</i> − 20</p>",
        "choices": ["(x − 5)(x + 4)", "(x + 5)(x − 4)", "(x − 5)(x − 4)", "(x − 10)(x + 2)"],
        "correct": "(x − 5)(x + 4)",
        "explanation": "<p><strong>(x − 5)(x + 4).</strong> (−5)(4) = −20 va "
                       "−5 + 4 = −1 ✓</p>"
                       "<p><strong>(x + 5)(x − 4)</strong> x² + x − 20 beradi — "
                       "oʻrta hadning ishorasi teskari.</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> + 11<i>x</i> + 24</p>",
        "choices": ["(x + 3)(x + 8)", "(x + 4)(x + 6)", "(x + 2)(x + 12)", "(x + 1)(x + 24)"],
        "correct": "(x + 3)(x + 8)",
        "explanation": "<p><strong>(x + 3)(x + 8).</strong> 24 ning juftliklari: 1·24, "
                       "2·12, 3·8, 4·6 — yigʻindisi 11 boʻlgani 3 va 8.</p>"
                       "<p><strong>(x + 4)(x + 6)</strong> — yigʻindisi 10.</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> − 13<i>x</i> + 40</p>",
        "choices": ["(x − 5)(x − 8)", "(x − 4)(x − 10)", "(x + 5)(x + 8)", "(x − 2)(x − 20)"],
        "correct": "(x − 5)(x − 8)",
        "explanation": "<p><strong>(x − 5)(x − 8).</strong> 40 = 5 × 8 va 5 + 8 = 13; "
                       "b manfiy, demak ikkala son ham manfiy.</p>"
                       "<p><strong>(x − 4)(x − 10)</strong> — yigʻindisi −14.</p>",
    },
    {
        "text": "<p>What are the solutions to <i>x</i><sup>2</sup> + 5<i>x</i> + 6 = 0?</p>",
        "choices": ["x = −2 and x = −3", "x = 2 and x = 3", "x = −1 and x = −6",
                    "x = 2 and x = −3"],
        "correct": "x = −2 and x = −3",
        "explanation": "<p><strong>x = −2 va x = −3.</strong> (x + 2)(x + 3) = 0 — "
                       "ildizlar qavsdagi sonlarning qarama-qarshisi.</p>"
                       "<p><strong>x = 2 va x = 3</strong> — ishora almashtirilmagan: "
                       "4 + 10 + 6 = 20, nol emas.</p>",
    },
    {
        "text": "<p>What are the solutions to <i>x</i><sup>2</sup> − 7<i>x</i> + 12 = 0?</p>",
        "choices": ["x = 3 and x = 4", "x = −3 and x = −4", "x = 2 and x = 6",
                    "x = 1 and x = 12"],
        "correct": "x = 3 and x = 4",
        "explanation": "<p><strong>x = 3 va x = 4.</strong> (x − 3)(x − 4) = 0.</p>"
                       "<p>Tekshiruv: 9 − 21 + 12 = 0 ✓ va 16 − 28 + 12 = 0 ✓</p>",
    },
    {
        "text": "<p>What are the solutions to <i>x</i><sup>2</sup> + 2<i>x</i> − 8 = 0?</p>",
        "choices": ["x = 2 and x = −4", "x = −2 and x = 4", "x = 2 and x = 4",
                    "x = −2 and x = −4"],
        "correct": "x = 2 and x = −4",
        "explanation": "<p><strong>x = 2 va x = −4.</strong> (x − 2)(x + 4) = 0.</p>"
                       "<p>Tekshiruv: 4 + 4 − 8 = 0 ✓ va 16 − 8 − 8 = 0 ✓</p>",
    },
    {
        "text": "<p>Which of the following is a factor of "
                "<i>x</i><sup>2</sup> + 9<i>x</i> + 18?</p>",
        "choices": ["(x + 3)", "(x + 2)", "(x − 3)", "(x + 9)"],
        "correct": "(x + 3)",
        "explanation": "<p><strong>(x + 3).</strong> x² + 9x + 18 = (x + 3)(x + 6), "
                       "chunki 3 × 6 = 18 va 3 + 6 = 9.</p>"
                       "<p><strong>(x + 2)</strong> — 2 juftlikda yoʻq: 18 ÷ 2 = 9, "
                       "lekin 2 + 9 = 11.</p>",
    },
    {
        "text": "<p>What is the sum of the solutions to "
                "<i>x</i><sup>2</sup> − 6<i>x</i> + 8 = 0?</p>",
        "choices": ["6", "8", "−6", "2"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Ildizlar 2 va 4, ularning yigʻindisi 6.</p>"
                       "<p><strong>8</strong> — bu ildizlarning koʻpaytmasi. Savol "
                       "«sum» deb soʻragan.</p>",
    },
    {
        "text": "<p>What is the product of the solutions to "
                "<i>x</i><sup>2</sup> − 6<i>x</i> + 8 = 0?</p>",
        "choices": ["8", "6", "−8", "4"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Ildizlar 2 va 4 → 2 × 4 = 8.</p>"
                       "<p>Bu tasodif emas: (x − p)(x − q) ochilganda erkin had pq "
                       "boʻladi.</p>",
    },
    {
        "text": "<p>A student writes <i>x</i><sup>2</sup> − 5<i>x</i> + 6 = "
                "(<i>x</i> + 2)(<i>x</i> + 3). What is the correct factorization?</p>",
        "choices": ["(x − 2)(x − 3)", "(x + 2)(x − 3)", "(x − 2)(x + 3)", "(x + 2)(x + 3)"],
        "correct": "(x − 2)(x − 3)",
        "explanation": "<p><strong>(x − 2)(x − 3).</strong> Oʻquvchi faqat koʻpaytmani "
                       "tekshirgan; b manfiy boʻlgani uchun ikkala son ham manfiy.</p>"
                       "<p>Uning javobi ochilganda x² + 5x + 6 beradi — oʻrta hadning "
                       "ishorasi notoʻgʻri.</p>",
    },
    {
        "text": "<p>What are the solutions to (<i>x</i> + 4)(<i>x</i> − 7) = 0?</p>",
        "choices": ["x = −4 and x = 7", "x = 4 and x = −7", "x = 4 and x = 7",
                    "x = −4 and x = −7"],
        "correct": "x = −4 and x = 7",
        "explanation": "<p><strong>x = −4 va x = 7.</strong> Har bir qavsni nolga "
                       "tenglashtiring: x + 4 = 0 → x = −4; x − 7 = 0 → x = 7.</p>"
                       "<p><strong>x = 4 va x = −7</strong> — ikkala ishora ham "
                       "notoʻgʻri koʻchirilgan.</p>",
    },
    {
        "text": "<p>In the expression <i>x</i><sup>2</sup> + <i>bx</i> + 15, "
                "(<i>x</i> + 3) is a factor. What is the value of <i>b</i>?</p>",
        "choices": ["8", "5", "12", "18"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Ikkinchi koʻpaytuvchi (x + 5), chunki "
                       "3 × 5 = 15. Demak b = 3 + 5 = 8.</p>"
                       "<p><strong>5</strong> — bu ikkinchi son, b emas.</p>",
    },
    {
        "text": "<p>If <i>x</i><sup>2</sup> − <i>kx</i> + 12 = (<i>x</i> − 3)"
                "(<i>x</i> − 4), what is the value of <i>k</i>?</p>",
        "choices": ["7", "−7", "12", "1"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Oʻng tomon x² − 7x + 12 beradi, va "
                       "chap tomonda oʻrta had −kx. Demak −k = −7 → k = 7.</p>"
                       "<p><strong>−7</strong> — ishora ikki marta almashtirilgan.</p>",
    },
    {
        "text": "<p>A rectangular garden has an area of 24 square metres and a "
                "perimeter of 20 metres. What are its dimensions?</p>",
        "choices": ["4 m by 6 m", "3 m by 8 m", "2 m by 12 m", "5 m by 5 m"],
        "correct": "4 m by 6 m",
        "explanation": "<p><strong>4 m × 6 m.</strong> Yarim perimetr 10, demak "
                       "yigʻindisi 10 va koʻpaytmasi 24 boʻlgan ikki son kerak: 4 va 6.</p>"
                       "<p><strong>3 m × 8 m</strong> — yuzasi 24 ✓ lekin perimetri "
                       "22.</p>",
    },
    {
        "text": "<p>Two numbers have a sum of 9 and a product of 18. What is the "
                "larger number?</p>",
        "choices": ["6", "3", "9", "18"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> x² − 9x + 18 = 0 → (x − 3)(x − 6) = 0, "
                       "demak sonlar 3 va 6.</p>"
                       "<p><strong>3</strong> — bu kichigi; savol kattasini "
                       "soʻragan.</p>",
    },
]


# =====================================================================
# SAT-32 — factoring ax² + bx + c
# =====================================================================

Q_SAT32 = [
    {
        "text": "<p>Factor: 2<i>x</i><sup>2</sup> + 3<i>x</i> + 1</p>",
        "choices": ["(2x + 1)(x + 1)", "(2x + 3)(x + 1)", "(x + 1)(x + 1)", "(2x + 1)(x + 3)"],
        "correct": "(2x + 1)(x + 1)",
        "explanation": "<p><strong>(2x + 1)(x + 1).</strong> Oching: "
                       "2x² + 2x + x + 1 ✓</p>"
                       "<p><strong>(2x + 1)(x + 3)</strong> 2x² + 7x + 3 beradi.</p>",
    },
    {
        "text": "<p>Factor: 3<i>x</i><sup>2</sup> + 4<i>x</i> + 1</p>",
        "choices": ["(3x + 1)(x + 1)", "(3x + 4)(x + 1)", "(x + 1)(x + 1)", "(3x + 1)(x + 4)"],
        "correct": "(3x + 1)(x + 1)",
        "explanation": "<p><strong>(3x + 1)(x + 1).</strong> ac = 3, juftlik 3 va 1: "
                       "3x² + 3x + x + 1.</p>"
                       "<p><strong>(3x + 1)(x + 4)</strong> ochilganda 13x beradi.</p>",
    },
    {
        "text": "<p>Factor: 2<i>x</i><sup>2</sup> + 9<i>x</i> + 4</p>",
        "choices": ["(2x + 1)(x + 4)", "(2x + 4)(x + 1)", "(2x + 2)(x + 2)", "(x + 4)(x + 5)"],
        "correct": "(2x + 1)(x + 4)",
        "explanation": "<p><strong>(2x + 1)(x + 4).</strong> ac = 8, juftlik 8 va 1: "
                       "2x² + 8x + x + 4 ✓</p>"
                       "<p><strong>(2x + 4)(x + 1)</strong> 2x² + 6x + 4 beradi — "
                       "bundan tashqari (2x + 4) da 2 ajralib turibdi.</p>",
    },
    {
        "text": "<p>Factor: 5<i>x</i><sup>2</sup> + 7<i>x</i> + 2</p>",
        "choices": ["(5x + 2)(x + 1)", "(5x + 1)(x + 2)", "(5x + 7)(x + 2)", "(x + 2)(x + 5)"],
        "correct": "(5x + 2)(x + 1)",
        "explanation": "<p><strong>(5x + 2)(x + 1).</strong> Oching: "
                       "5x² + 5x + 2x + 2 ✓</p>"
                       "<p><strong>(5x + 1)(x + 2)</strong> 5x² + 11x + 2 beradi — "
                       "sonlar oʻrin almashgan.</p>",
    },
    {
        "text": "<p>Factor: 2<i>x</i><sup>2</sup> − 5<i>x</i> + 3</p>",
        "choices": ["(2x − 3)(x − 1)", "(2x − 1)(x − 3)", "(2x + 3)(x + 1)", "(2x − 3)(x + 1)"],
        "correct": "(2x − 3)(x − 1)",
        "explanation": "<p><strong>(2x − 3)(x − 1).</strong> ac = 6, juftlik −2 va −3: "
                       "2x² − 2x − 3x + 3 ✓</p>"
                       "<p><strong>(2x − 1)(x − 3)</strong> 2x² − 7x + 3 beradi.</p>",
    },
    {
        "text": "<p>Factor: 3<i>x</i><sup>2</sup> − 8<i>x</i> + 4</p>",
        "choices": ["(3x − 2)(x − 2)", "(3x − 4)(x − 1)", "(3x − 1)(x − 4)", "(3x + 2)(x + 2)"],
        "correct": "(3x − 2)(x − 2)",
        "explanation": "<p><strong>(3x − 2)(x − 2).</strong> ac = 12, juftlik −6 va −2: "
                       "3x² − 6x − 2x + 4 ✓</p>"
                       "<p><strong>(3x − 4)(x − 1)</strong> 3x² − 7x + 4 beradi.</p>",
    },
    {
        "text": "<p>Factor: 2<i>x</i><sup>2</sup> + <i>x</i> − 6</p>",
        "choices": ["(2x − 3)(x + 2)", "(2x + 3)(x − 2)", "(2x − 2)(x + 3)", "(2x + 1)(x − 6)"],
        "correct": "(2x − 3)(x + 2)",
        "explanation": "<p><strong>(2x − 3)(x + 2).</strong> Oching: "
                       "2x² + 4x − 3x − 6 = 2x² + x − 6 ✓</p>"
                       "<p><strong>(2x + 3)(x − 2)</strong> 2x² − x − 6 beradi — minus "
                       "notoʻgʻri qavsda.</p>",
    },
    {
        "text": "<p>Factor: 3<i>x</i><sup>2</sup> + 5<i>x</i> − 2</p>",
        "choices": ["(3x − 1)(x + 2)", "(3x + 1)(x − 2)", "(3x − 2)(x + 1)", "(3x + 2)(x − 1)"],
        "correct": "(3x − 1)(x + 2)",
        "explanation": "<p><strong>(3x − 1)(x + 2).</strong> Oching: "
                       "3x² + 6x − x − 2 ✓</p>"
                       "<p><strong>(3x + 1)(x − 2)</strong> 3x² − 5x − 2 beradi.</p>",
    },
    {
        "text": "<p>Factor: 4<i>x</i><sup>2</sup> + 8<i>x</i> + 3</p>",
        "choices": ["(2x + 1)(2x + 3)", "(4x + 1)(x + 3)", "(4x + 3)(x + 1)", "(2x + 3)(2x − 1)"],
        "correct": "(2x + 1)(2x + 3)",
        "explanation": "<p><strong>(2x + 1)(2x + 3).</strong> ac = 12, juftlik 6 va 2: "
                       "4x² + 6x + 2x + 3 ✓</p>"
                       "<p><strong>(4x + 1)(x + 3)</strong> 4x² + 13x + 3 beradi.</p>",
    },
    {
        "text": "<p>Factor: 6<i>x</i><sup>2</sup> + 7<i>x</i> + 2</p>",
        "choices": ["(3x + 2)(2x + 1)", "(6x + 1)(x + 2)", "(3x + 1)(2x + 2)", "(6x + 2)(x + 1)"],
        "correct": "(3x + 2)(2x + 1)",
        "explanation": "<p><strong>(3x + 2)(2x + 1).</strong> Oching: "
                       "6x² + 3x + 4x + 2 ✓</p>"
                       "<p><strong>(6x + 1)(x + 2)</strong> 6x² + 13x + 2 beradi.</p>",
    },
    {
        "text": "<p>When factoring 3<i>x</i><sup>2</sup> + 7<i>x</i> + 2 by the AC "
                "method, what is the value of <i>a</i> · <i>c</i>?</p>",
        "choices": ["6", "7", "5", "21"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> a = 3 va c = 2, demak ac = 6.</p>"
                       "<p><strong>7</strong> — bu b, yaʼni izlanayotgan juftlikning "
                       "<b>yigʻindisi</b>, koʻpaytmasi emas.</p>",
    },
    {
        "text": "<p>To factor 2<i>x</i><sup>2</sup> + 7<i>x</i> + 6 by the AC method, "
                "which pair of numbers should you use?</p>",
        "choices": ["3 and 4", "2 and 6", "1 and 6", "2 and 5"],
        "correct": "3 and 4",
        "explanation": "<p><strong>3 va 4.</strong> ac = 12 va b = 7: 3 × 4 = 12 ✓ va "
                       "3 + 4 = 7 ✓</p>"
                       "<p><strong>2 va 6</strong> — koʻpaytmasi 12 ✓ lekin yigʻindisi "
                       "8.</p>",
    },
    {
        "text": "<p>What are the solutions to 2<i>x</i><sup>2</sup> + 5<i>x</i> + 2 = 0?</p>",
        "choices": ["x = −1/2 and x = −2", "x = 1/2 and x = 2", "x = −1 and x = −2",
                    "x = −2 and x = −5"],
        "correct": "x = −1/2 and x = −2",
        "explanation": "<p><strong>x = −1/2 va x = −2.</strong> (2x + 1)(x + 2) = 0; "
                       "2x + 1 = 0 → x = −1/2.</p>"
                       "<p>Tekshiruv: 2(0.25) − 2.5 + 2 = 0 ✓</p>",
    },
    {
        "text": "<p>What are the solutions to 3<i>x</i><sup>2</sup> − 7<i>x</i> + 2 = 0?</p>",
        "choices": ["x = 1/3 and x = 2", "x = −1/3 and x = −2", "x = 3 and x = 2",
                    "x = 1/2 and x = 3"],
        "correct": "x = 1/3 and x = 2",
        "explanation": "<p><strong>x = 1/3 va x = 2.</strong> (3x − 1)(x − 2) = 0.</p>"
                       "<p>Tekshiruv: 3(4) − 14 + 2 = 0 ✓ va 3(1/9) − 7/3 + 2 = 0 ✓</p>",
    },
    {
        "text": "<p>A student writes 2<i>x</i><sup>2</sup> + 7<i>x</i> + 3 = "
                "(2<i>x</i> + 3)(<i>x</i> + 1). What is the correct factorization?</p>",
        "choices": ["(2x + 1)(x + 3)", "(2x + 3)(x + 1)", "(2x + 7)(x + 3)", "(x + 3)(x + 1)"],
        "correct": "(2x + 1)(x + 3)",
        "explanation": "<p><strong>(2x + 1)(x + 3).</strong> Oʻquvchining javobi "
                       "2x² + 5x + 3 beradi — sonlar oʻrin almashgan.</p>"
                       "<p>a ≠ 1 boʻlganda sonlarning oʻrni oʻrta hadni "
                       "oʻzgartiradi.</p>",
    },
    {
        "text": "<p>Which of the following is a factor of "
                "6<i>x</i><sup>2</sup> + 11<i>x</i> − 10?</p>",
        "choices": ["(3x − 2)", "(2x − 5)", "(3x + 2)", "(6x − 5)"],
        "correct": "(3x − 2)",
        "explanation": "<p><strong>(3x − 2).</strong> Toʻgʻri ajratma "
                       "(3x − 2)(2x + 5).</p>"
                       "<p><strong>(2x − 5)</strong> — oʻsha sonlar, boshqa qavsda: "
                       "(2x − 5)(3x + 2) ochilganda 6x² − 11x − 10 beradi.</p>",
    },
    {
        "text": "<p>Factor: 6<i>x</i><sup>2</sup> − <i>x</i> − 12</p>",
        "choices": ["(3x + 4)(2x − 3)", "(3x − 4)(2x + 3)", "(6x + 4)(x − 3)", "(3x + 2)(2x − 6)"],
        "correct": "(3x + 4)(2x − 3)",
        "explanation": "<p><strong>(3x + 4)(2x − 3).</strong> Oching: "
                       "6x² − 9x + 8x − 12 = 6x² − x − 12 ✓</p>"
                       "<p><strong>(3x − 4)(2x + 3)</strong> 6x² + x − 12 beradi.</p>",
    },
    {
        "text": "<p>Factor: 4<i>x</i><sup>2</sup> − 4<i>x</i> − 15</p>",
        "choices": ["(2x + 3)(2x − 5)", "(2x − 3)(2x + 5)", "(4x + 3)(x − 5)", "(4x − 5)(x + 3)"],
        "correct": "(2x + 3)(2x − 5)",
        "explanation": "<p><strong>(2x + 3)(2x − 5).</strong> Oching: "
                       "4x² − 10x + 6x − 15 = 4x² − 4x − 15 ✓</p>"
                       "<p><strong>(2x − 3)(2x + 5)</strong> 4x² + 4x − 15 beradi.</p>",
    },
    {
        "text": "<p>A rectangle has an area of 2<i>x</i><sup>2</sup> + 11<i>x</i> + 12 "
                "square metres. Which pair could be its dimensions?</p>",
        "choices": ["(2x + 3) and (x + 4)", "(2x + 4) and (x + 3)", "(2x + 1) and (x + 12)",
                    "(2x + 6) and (x + 2)"],
        "correct": "(2x + 3) and (x + 4)",
        "explanation": "<p><strong>(2x + 3) va (x + 4).</strong> Oching: "
                       "2x² + 8x + 3x + 12 ✓</p>"
                       "<p><strong>(2x + 4)(x + 3)</strong> 2x² + 10x + 12 beradi.</p>",
    },
    {
        "text": "<p>The area of a rectangular field is 3<i>x</i><sup>2</sup> + "
                "10<i>x</i> + 8 square metres. If its width is (<i>x</i> + 2) metres, "
                "what is its length?</p>",
        "choices": ["(3x + 4) metres", "(3x + 8) metres", "(3x + 2) metres", "(x + 4) metres"],
        "correct": "(3x + 4) metres",
        "explanation": "<p><strong>(3x + 4) metr.</strong> "
                       "3x² + 10x + 8 = (3x + 4)(x + 2) ✓</p>"
                       "<p><strong>(3x + 8)</strong> ni (x + 2) ga koʻpaytirsangiz "
                       "3x² + 14x + 16 chiqadi.</p>",
    },
]


# =====================================================================
# SAT-33 — the quadratic formula
# =====================================================================

Q_SAT33 = [
    {
        "text": "<p>What is the discriminant of <i>x</i><sup>2</sup> + 5<i>x</i> + 6 = 0?</p>",
        "choices": ["1", "49", "−1", "25"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> b² − 4ac = 25 − 24 = 1.</p>"
                       "<p><strong>25</strong> — faqat b² hisoblangan, −4ac "
                       "qoʻshilmagan.</p>",
    },
    {
        "text": "<p>What is the discriminant of 2<i>x</i><sup>2</sup> + 3<i>x</i> − 2 = 0?</p>",
        "choices": ["25", "−7", "9", "16"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> 9 − 4(2)(−2) = 9 + 16 = 25.</p>"
                       "<p><strong>−7</strong> — c manfiy ekani hisobga olinmagan: "
                       "ikki minus plyus beradi.</p>",
    },
    {
        "text": "<p>What is the discriminant of <i>x</i><sup>2</sup> − 4<i>x</i> + 1 = 0?</p>",
        "choices": ["12", "20", "−12", "16"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> (−4)² − 4(1)(1) = 16 − 4 = 12.</p>"
                       "<p>12 toʻliq kvadrat emas — demak bu tenglama butun sonlar "
                       "bilan ajratilmaydi.</p>",
    },
    {
        "text": "<p>What is the discriminant of 3<i>x</i><sup>2</sup> − 2<i>x</i> + 4 = 0?</p>",
        "choices": ["−44", "44", "52", "−52"],
        "correct": "−44",
        "explanation": "<p><strong>−44.</strong> (−2)² − 4(3)(4) = 4 − 48 = −44.</p>"
                       "<p>Manfiy — demak haqiqiy yechim yoʻq (SAT-34).</p>",
    },
    {
        "text": "<p>What are the solutions to <i>x</i><sup>2</sup> + 7<i>x</i> + 12 = 0?</p>",
        "choices": ["x = −3 and x = −4", "x = 3 and x = 4", "x = −2 and x = −6",
                    "x = −1 and x = −12"],
        "correct": "x = −3 and x = −4",
        "explanation": "<p><strong>x = −3 va x = −4.</strong> Diskriminant 49 − 48 = 1, "
                       "demak x = (−7 ± 1) ÷ 2.</p>"
                       "<p>Tekshiruv: 9 − 21 + 12 = 0 ✓</p>",
    },
    {
        "text": "<p>What are the solutions to 2<i>x</i><sup>2</sup> − 7<i>x</i> + 3 = 0?</p>",
        "choices": ["x = 3 and x = 1/2", "x = −3 and x = −1/2", "x = 3 and x = 2",
                    "x = 1 and x = 3"],
        "correct": "x = 3 and x = 1/2",
        "explanation": "<p><strong>x = 3 va x = 1/2.</strong> Diskriminant "
                       "49 − 24 = 25, demak x = (7 ± 5) ÷ 4.</p>"
                       "<p>Tekshiruv: 18 − 21 + 3 = 0 ✓</p>",
    },
    {
        "text": "<p>What are the solutions to <i>x</i><sup>2</sup> − 2<i>x</i> − 3 = 0?</p>",
        "choices": ["x = 3 and x = −1", "x = −3 and x = 1", "x = 3 and x = 1",
                    "x = −3 and x = −1"],
        "correct": "x = 3 and x = −1",
        "explanation": "<p><strong>x = 3 va x = −1.</strong> Diskriminant 4 + 12 = 16, "
                       "demak x = (2 ± 4) ÷ 2.</p>"
                       "<p>Tekshiruv: 9 − 6 − 3 = 0 ✓ va 1 + 2 − 3 = 0 ✓</p>",
    },
    {
        "text": "<p>What are the solutions to <i>x</i><sup>2</sup> + 6<i>x</i> + 4 = 0?</p>",
        "choices": ["x = −3 ± √5", "x = 3 ± √5", "x = −3 ± √20", "x = −6 ± √5"],
        "correct": "x = −3 ± √5",
        "explanation": "<p><strong>x = −3 ± √5.</strong> Diskriminant 36 − 16 = 20, "
                       "va x = (−6 ± 2√5) ÷ 2.</p>"
                       "<p><strong>−3 ± √20</strong> — ildiz qismi qisqartirilmagan: "
                       "boʻlish ikkala hadga qoʻllanadi.</p>",
    },
    {
        "text": "<p>What are the solutions to <i>x</i><sup>2</sup> − 10<i>x</i> + 23 = 0?</p>",
        "choices": ["x = 5 ± √2", "x = 5 ± √8", "x = 10 ± √2", "x = −5 ± √2"],
        "correct": "x = 5 ± √2",
        "explanation": "<p><strong>x = 5 ± √2.</strong> Diskriminant 100 − 92 = 8, "
                       "va x = (10 ± 2√2) ÷ 2.</p>"
                       "<p><strong>5 ± √8</strong> — √8 = 2√2 soddalashtirilmagan va "
                       "boʻlinmagan.</p>",
    },
    {
        "text": "<p>What are the solutions to 2<i>x</i><sup>2</sup> + 4<i>x</i> − 1 = 0?</p>",
        "choices": ["x = (−2 ± √6) ÷ 2", "x = (−4 ± √6) ÷ 2", "x = −2 ± √6",
                    "x = (−2 ± √24) ÷ 2"],
        "correct": "x = (−2 ± √6) ÷ 2",
        "explanation": "<p><strong>(−2 ± √6) ÷ 2.</strong> Diskriminant 16 + 8 = 24, "
                       "x = (−4 ± 2√6) ÷ 4, keyin 2 ga qisqardi.</p>"
                       "<p>Taxminan −0.775 va −3.225 ✓</p>",
    },
    {
        "text": "<p>What is the positive solution to <i>x</i><sup>2</sup> − 4<i>x</i> "
                "− 5 = 0?</p>",
        "choices": ["5", "−1", "4", "1"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Ildizlar 5 va −1; savol musbatini "
                       "soʻragan.</p>"
                       "<p><strong>−1</strong> — bu ikkinchi ildiz, lekin u "
                       "manfiy.</p>",
    },
    {
        "text": "<p>In the quadratic formula applied to 3<i>x</i><sup>2</sup> + "
                "2<i>x</i> − 5 = 0, what is the value of the denominator 2<i>a</i>?</p>",
        "choices": ["6", "4", "−10", "2"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> a = 3, demak 2a = 6.</p>"
                       "<p><strong>4</strong> — 2b hisoblangan (b = 2). Maxrajda a "
                       "turadi.</p>",
    },
    {
        "text": "<p>What is the discriminant of 5<i>x</i><sup>2</sup> − 3<i>x</i> "
                "+ 1 = 0?</p>",
        "choices": ["−11", "11", "29", "−29"],
        "correct": "−11",
        "explanation": "<p><strong>−11.</strong> 9 − 20 = −11.</p>"
                       "<p><strong>29</strong> — c musbat boʻlsa −4ac <b>ayiriladi</b>; "
                       "qoʻshish faqat c manfiy boʻlganda boʻladi.</p>",
    },
    {
        "text": "<p>A ball's height in metres is <i>h</i> = −5<i>t</i><sup>2</sup> + "
                "20<i>t</i>, where <i>t</i> is in seconds. At what times is the ball "
                "at ground level?</p>",
        "choices": ["t = 0 and t = 4", "t = 0 and t = 20", "t = 2 and t = 4",
                    "t = 4 only"],
        "correct": "t = 0 and t = 4",
        "explanation": "<p><strong>t = 0 va t = 4.</strong> −5t(t − 4) = 0.</p>"
                       "<p>t = 0 — tashlangan payt, t = 4 — yerga tushgan payt. "
                       "Ikkalasi ham haqiqiy javob.</p>",
    },
    {
        "text": "<p>A student computes the discriminant of <i>x</i><sup>2</sup> + "
                "4<i>x</i> − 5 = 0 as 16 − 20 = −4. What is the correct value?</p>",
        "choices": ["36", "−4", "4", "−36"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> c = −5, demak −4ac = −4(1)(−5) = "
                       "<b>+20</b>: 16 + 20 = 36.</p>"
                       "<p>Oʻquvchi c ning minusini eʼtiborsiz qoldirgan — bu "
                       "formuladagi eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to (6 ± √20) ÷ 2?</p>",
        "choices": ["3 ± √5", "3 ± √20", "3 ± 2√5", "6 ± √5"],
        "correct": "3 ± √5",
        "explanation": "<p><strong>3 ± √5.</strong> √20 = 2√5, keyin (6 ± 2√5) ÷ 2 = "
                       "3 ± √5.</p>"
                       "<p><strong>3 ± √20</strong> — faqat 6 boʻlingan; boʻlish "
                       "<b>ikkala</b> hadga qoʻllanadi.</p>",
    },
    {
        "text": "<p>What are the solutions to 2<i>x</i><sup>2</sup> − 6<i>x</i> + 3 = 0?</p>",
        "choices": ["x = (3 ± √3) ÷ 2", "x = (6 ± √3) ÷ 2", "x = 3 ± √3",
                    "x = (3 ± √12) ÷ 2"],
        "correct": "x = (3 ± √3) ÷ 2",
        "explanation": "<p><strong>(3 ± √3) ÷ 2.</strong> Diskriminant 36 − 24 = 12, "
                       "x = (6 ± 2√3) ÷ 4, hamma hadni 2 ga qisqartirdik.</p>"
                       "<p>Taxminan 2.366 va 0.634 ✓</p>",
    },
    {
        "text": "<p>What are the solutions to <i>x</i><sup>2</sup> − 8<i>x</i> + 13 = 0?</p>",
        "choices": ["x = 4 ± √3", "x = 4 ± √12", "x = 8 ± √3", "x = −4 ± √3"],
        "correct": "x = 4 ± √3",
        "explanation": "<p><strong>x = 4 ± √3.</strong> Diskriminant 64 − 52 = 12, "
                       "x = (8 ± 2√3) ÷ 2.</p>"
                       "<p>Taxminan 5.73 va 2.27; ikkalasining yigʻindisi 8 ✓</p>",
    },
    {
        "text": "<p>The length of a rectangle is 2 metres more than its width, and its "
                "area is 15 square metres. What is the width?</p>",
        "choices": ["3 metres", "5 metres", "2 metres", "7.5 metres"],
        "correct": "3 metres",
        "explanation": "<p><strong>3 metr.</strong> w(w + 2) = 15 → w² + 2w − 15 = 0 → "
                       "(w + 5)(w − 3) = 0.</p>"
                       "<p><strong>5 metr</strong> — bu uzunlik. w = −5 esa "
                       "uzunlik boʻla olmaydi.</p>",
    },
    {
        "text": "<p>A ball is thrown from a 20-metre platform and its height is "
                "<i>h</i> = −5<i>t</i><sup>2</sup> + 15<i>t</i> + 20 metres. After how "
                "many seconds does it hit the ground?</p>",
        "choices": ["4 seconds", "3 seconds", "5 seconds", "1 second"],
        "correct": "4 seconds",
        "explanation": "<p><strong>4 soniya.</strong> −5t² + 15t + 20 = 0 → "
                       "t² − 3t − 4 = 0 → (t − 4)(t + 1) = 0.</p>"
                       "<p>t = −1 ham ildiz, lekin vaqt manfiy boʻlmaydi — kontekst "
                       "javobni tanlaydi.</p>",
    },
]


# =====================================================================
# SAT-34 — the discriminant: number and type of roots
# =====================================================================

Q_SAT34 = [
    {
        "text": "<p>How many real solutions does <i>x</i><sup>2</sup> + 2<i>x</i> + 5 "
                "= 0 have?</p>",
        "choices": ["Zero", "One", "Two", "Infinitely many"],
        "correct": "Zero",
        "explanation": "<p><strong>Zero.</strong> D = 4 − 20 = −16 &lt; 0.</p>"
                       "<p>Grafik tilida: parabola x oʻqini umuman kesmaydi.</p>",
    },
    {
        "text": "<p>How many real solutions does <i>x</i><sup>2</sup> − 4<i>x</i> + 4 "
                "= 0 have?</p>",
        "choices": ["One", "Zero", "Two", "Three"],
        "correct": "One",
        "explanation": "<p><strong>One.</strong> D = 16 − 16 = 0 — bitta takrorlanuvchi "
                       "ildiz, x = 2.</p>"
                       "<p>Bu (x − 2)², toʻliq kvadrat uchhad (SAT-30).</p>",
    },
    {
        "text": "<p>How many real solutions does <i>x</i><sup>2</sup> − 3<i>x</i> − 4 "
                "= 0 have?</p>",
        "choices": ["Two", "One", "Zero", "Four"],
        "correct": "Two",
        "explanation": "<p><strong>Two.</strong> D = 9 + 16 = 25 &gt; 0.</p>"
                       "<p>25 toʻliq kvadrat, demak ildizlar butun: 4 va −1.</p>",
    },
    {
        "text": "<p>How many real solutions does 2<i>x</i><sup>2</sup> + <i>x</i> + 3 "
                "= 0 have?</p>",
        "choices": ["Zero", "One", "Two", "Cannot be determined"],
        "correct": "Zero",
        "explanation": "<p><strong>Zero.</strong> D = 1 − 24 = −23 &lt; 0.</p>"
                       "<p><strong>Cannot be determined</strong> — diskriminant har "
                       "doim aniq javob beradi.</p>",
    },
    {
        "text": "<p>How many real solutions does 9<i>x</i><sup>2</sup> − 6<i>x</i> + 1 "
                "= 0 have?</p>",
        "choices": ["One", "Two", "Zero", "Nine"],
        "correct": "One",
        "explanation": "<p><strong>One.</strong> D = 36 − 36 = 0; bu "
                       "(3x − 1)².</p>"
                       "<p>Ildiz x = 1/3, va u ikki marta takrorlanadi.</p>",
    },
    {
        "text": "<p>How many real solutions does <i>x</i><sup>2</sup> + <i>x</i> − 1 "
                "= 0 have?</p>",
        "choices": ["Two", "One", "Zero", "Two, both integers"],
        "correct": "Two",
        "explanation": "<p><strong>Two.</strong> D = 1 + 4 = 5 &gt; 0.</p>"
                       "<p>5 toʻliq kvadrat emas, demak ildizlarda √ qoladi — butun "
                       "son emas.</p>",
    },
    {
        "text": "<p>If the discriminant of a quadratic equation equals 0, how many "
                "real solutions does it have?</p>",
        "choices": ["Exactly one", "None", "Exactly two", "Infinitely many"],
        "correct": "Exactly one",
        "explanation": "<p><strong>Exactly one.</strong> √0 = 0, demak ± hech narsani "
                       "oʻzgartirmaydi va bitta javob qoladi.</p>"
                       "<p><strong>None</strong> — bu D <b>manfiy</b> boʻlgandagi "
                       "holat.</p>",
    },
    {
        "text": "<p>The discriminant of a quadratic is negative. What does its graph "
                "look like?</p>",
        "choices": ["It does not cross the x-axis", "It touches the x-axis once",
                    "It crosses the x-axis twice", "It is a straight line"],
        "correct": "It does not cross the x-axis",
        "explanation": "<p><strong>x oʻqini kesmaydi.</strong> Kesishish nuqtasi — bu "
                       "haqiqiy ildiz; ildiz yoʻq boʻlsa, kesishish ham yoʻq.</p>"
                       "<p>Parabola x oʻqidan butunlay yuqorida yoki butunlay pastda "
                       "turadi.</p>",
    },
    {
        "text": "<p>A quadratic has a discriminant of 49. What does this tell you?</p>",
        "choices": ["It has two rational solutions and can be factored",
                    "It has no real solutions",
                    "It has exactly one solution",
                    "Its solutions contain a radical"],
        "correct": "It has two rational solutions and can be factored",
        "explanation": "<p><strong>Ikkita ratsional yechim.</strong> 49 musbat va "
                       "toʻliq kvadrat (7²), demak butun sonlar bilan ajratiladi.</p>"
                       "<p>Ildiz faqat D toʻliq kvadrat <b>boʻlmaganda</b> "
                       "qoladi.</p>",
    },
    {
        "text": "<p>Can <i>x</i><sup>2</sup> + 5<i>x</i> + 3 be factored using "
                "integers?</p>",
        "choices": ["No — the discriminant is 13, not a perfect square",
                    "Yes — it factors as (x + 1)(x + 3)",
                    "Yes — it factors as (x + 5)(x + 3)",
                    "No — the discriminant is negative"],
        "correct": "No — the discriminant is 13, not a perfect square",
        "explanation": "<p><strong>Yoʻq.</strong> D = 25 − 12 = 13 — musbat, demak "
                       "ikkita haqiqiy ildiz bor, lekin toʻliq kvadrat emas.</p>"
                       "<p>Bunday tenglamada formulani ishlating (SAT-33).</p>",
    },
    {
        "text": "<p>Can 2<i>x</i><sup>2</sup> + 7<i>x</i> + 3 be factored using "
                "integers?</p>",
        "choices": ["Yes — the discriminant is 25", "No — the discriminant is 25",
                    "No — the discriminant is negative", "Yes — but only with radicals"],
        "correct": "Yes — the discriminant is 25",
        "explanation": "<p><strong>Ha.</strong> D = 49 − 24 = 25 = 5², toʻliq kvadrat "
                       "→ (2x + 1)(x + 3).</p>"
                       "<p>Diskriminantni oldindan hisoblash behuda izlanishdan "
                       "saqlaydi.</p>",
    },
    {
        "text": "<p>The graph of a quadratic touches the <i>x</i>-axis at exactly one "
                "point. What is its discriminant?</p>",
        "choices": ["0", "Positive", "Negative", "1"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Bitta tegish nuqtasi — bitta "
                       "takrorlanuvchi ildiz.</p>"
                       "<p><strong>1</strong> — D = 1 boʻlsa <b>ikkita</b> ildiz "
                       "boʻladi, chunki 1 musbat.</p>",
    },
    {
        "text": "<p>The graph of a quadratic has two <i>x</i>-intercepts. What must be "
                "true about its discriminant?</p>",
        "choices": ["It is positive", "It is zero", "It is negative", "It equals 2"],
        "correct": "It is positive",
        "explanation": "<p><strong>Musbat.</strong> Ikkita kesishish nuqtasi — ikkita "
                       "haqiqiy ildiz → D &gt; 0.</p>"
                       "<p><strong>It equals 2</strong> — D ning qiymati emas, "
                       "<b>ishorasi</b> muhim.</p>",
    },
    {
        "text": "<p>In <i>x</i><sup>2</sup> + <i>kx</i> + 9 = 0, <i>k</i> is a "
                "constant. If the equation has exactly one real solution, what is the "
                "positive value of <i>k</i>?</p>",
        "choices": ["6", "3", "9", "36"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> D = 0 → k² − 36 = 0 → k = ±6.</p>"
                       "<p><strong>3</strong> — √9 = 3 deb toʻxtab qolgan javob; "
                       "kerakli tenglama k² = 4ac = 36 edi.</p>",
    },
    {
        "text": "<p>A student says that a discriminant of 0 means the equation has no "
                "solutions. What is the correct statement?</p>",
        "choices": ["It has exactly one real solution",
                    "It has two real solutions",
                    "The student is right",
                    "It has infinitely many solutions"],
        "correct": "It has exactly one real solution",
        "explanation": "<p><strong>Aynan bitta haqiqiy yechim.</strong> Yechim "
                       "boʻlmasligi uchun D <b>manfiy</b> boʻlishi kerak.</p>"
                       "<p>D = 0 da parabola x oʻqiga urinadi — bir marta "
                       "tegadi.</p>",
    },
    {
        "text": "<p>How many real solutions does <i>x</i><sup>2</sup> + 4<i>x</i> + 5 "
                "= 0 have?</p>",
        "choices": ["Zero", "Two", "One", "Two, both negative"],
        "correct": "Zero",
        "explanation": "<p><strong>Zero.</strong> D = 16 − 20 = −4 &lt; 0.</p>"
                       "<p><strong>Two, both negative</strong> — b va c musbat "
                       "boʻlgani ildizlar borligini anglatmaydi. Avval D ni "
                       "hisoblang.</p>",
    },
    {
        "text": "<p>In <i>x</i><sup>2</sup> + <i>kx</i> + 16 = 0, the equation has "
                "exactly one real solution. What is the positive value of <i>k</i>?</p>",
        "choices": ["8", "4", "16", "64"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> k² = 4(1)(16) = 64 → k = ±8.</p>"
                       "<p>Tekshiruv: x² + 8x + 16 = (x + 4)², bitta ildiz "
                       "x = −4 ✓</p>",
    },
    {
        "text": "<p>For what value of <i>k</i> does 2<i>x</i><sup>2</sup> + 8<i>x</i> "
                "+ <i>k</i> = 0 have exactly one real solution?</p>",
        "choices": ["8", "4", "16", "2"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> D = 64 − 4(2)k = 64 − 8k = 0 → "
                       "k = 8.</p>"
                       "<p><strong>16</strong> — a = 2 ekani unutilgan: 64 − 4k = 0 "
                       "deb yechilgan.</p>",
    },
    {
        "text": "<p>A ball's height in metres is <i>h</i> = −5<i>t</i><sup>2</sup> + "
                "20<i>t</i>. Does the ball ever reach a height of 25 metres?</p>",
        "choices": ["No — the discriminant is negative",
                    "Yes — exactly once",
                    "Yes — twice",
                    "Yes — at t = 5 seconds"],
        "correct": "No — the discriminant is negative",
        "explanation": "<p><strong>Yoʻq.</strong> −5t² + 20t = 25 → t² − 4t + 5 = 0, "
                       "va D = 16 − 20 = −4 &lt; 0.</p>"
                       "<p>Diskriminant «yeta oladimi» degan savolga hisoblamasdan "
                       "javob beradi.</p>",
    },
    {
        "text": "<p>For the same ball, <i>h</i> = −5<i>t</i><sup>2</sup> + 20<i>t</i>. "
                "How many times does it reach a height of exactly 20 metres?</p>",
        "choices": ["Once", "Twice", "Never", "Three times"],
        "correct": "Once",
        "explanation": "<p><strong>Bir marta.</strong> t² − 4t + 4 = 0, D = 0 → "
                       "t = 2.</p>"
                       "<p>Demak 20 metr — toʻpning eng yuqori nuqtasi: unga faqat "
                       "bir lahza yetadi.</p>",
    },
]


# =====================================================================
# SAT-35 — vertex form
# =====================================================================

Q_SAT35 = [
    {
        "text": "<p>What is the vertex of <i>y</i> = (<i>x</i> − 2)<sup>2</sup> + 3?</p>",
        "choices": ["(2, 3)", "(−2, 3)", "(2, −3)", "(3, 2)"],
        "correct": "(2, 3)",
        "explanation": "<p><strong>(2, 3).</strong> y = a(x − h)² + k da h = 2, "
                       "k = 3.</p>"
                       "<p><strong>(3, 2)</strong> — koordinatalar oʻrin almashgan; "
                       "avval x, keyin y.</p>",
    },
    {
        "text": "<p>What is the vertex of <i>y</i> = (<i>x</i> + 1)<sup>2</sup> − 4?</p>",
        "choices": ["(−1, −4)", "(1, −4)", "(−1, 4)", "(1, 4)"],
        "correct": "(−1, −4)",
        "explanation": "<p><strong>(−1, −4).</strong> (x + 1)² = (x − (−1))², demak "
                       "h = −1.</p>"
                       "<p><strong>(1, −4)</strong> — qavsdagi son shundoq "
                       "koʻchirilgan; h ning ishorasi har doim almashadi.</p>",
    },
    {
        "text": "<p>What is the vertex of <i>y</i> = (<i>x</i> − 6)<sup>2</sup>?</p>",
        "choices": ["(6, 0)", "(0, 6)", "(−6, 0)", "(6, 6)"],
        "correct": "(6, 0)",
        "explanation": "<p><strong>(6, 0).</strong> k yozilmagan, demak k = 0.</p>"
                       "<p>Bu parabola x oʻqiga x = 6 nuqtasida urinadi — "
                       "diskriminanti nol (SAT-34).</p>",
    },
    {
        "text": "<p>What is the vertex of <i>y</i> = 2(<i>x</i> + 3)<sup>2</sup> + 1?</p>",
        "choices": ["(−3, 1)", "(3, 1)", "(−3, 2)", "(2, 1)"],
        "correct": "(−3, 1)",
        "explanation": "<p><strong>(−3, 1).</strong> a = 2 parabolani torroq qiladi, "
                       "lekin uchning oʻrnini <b>oʻzgartirmaydi</b>.</p>"
                       "<p><strong>(−3, 2)</strong> — a ni k oʻrniga olgan javob.</p>",
    },
    {
        "text": "<p>What is the minimum value of <i>y</i> = (<i>x</i> − 4)<sup>2</sup> "
                "+ 7?</p>",
        "choices": ["7", "4", "−7", "11"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Kvadrat hech qachon manfiy boʻlmaydi, "
                       "demak eng kichik qiymat (x − 4)² = 0 boʻlganda.</p>"
                       "<p><strong>4</strong> — bu minimum <b>qayerda</b> boʻlishi, "
                       "yaʼni x. Savol qiymatni soʻragan.</p>",
    },
    {
        "text": "<p>What is the maximum value of <i>y</i> = −(<i>x</i> − 2)<sup>2</sup> "
                "+ 9?</p>",
        "choices": ["9", "2", "−9", "7"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> a manfiy, demak parabola pastga "
                       "ochiladi va uch — eng yuqori nuqta.</p>"
                       "<p><strong>2</strong> — bu x koordinatasi.</p>",
    },
    {
        "text": "<p>What is the axis of symmetry of <i>y</i> = (<i>x</i> − 5)<sup>2</sup> "
                "+ 2?</p>",
        "choices": ["x = 5", "x = −5", "y = 2", "x = 2"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> Simmetriya oʻqi uchdan oʻtadigan "
                       "vertikal chiziq, yaʼni x = h.</p>"
                       "<p><strong>y = 2</strong> — bu gorizontal chiziq; simmetriya "
                       "oʻqi vertikal.</p>",
    },
    {
        "text": "<p>What is the <i>x</i>-coordinate of the vertex of <i>y</i> = "
                "<i>x</i><sup>2</sup> − 4<i>x</i> + 3?</p>",
        "choices": ["2", "−2", "4", "3"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> x = −b ÷ (2a) = −(−4) ÷ 2 = 2.</p>"
                       "<p><strong>−2</strong> — b ning minusi ikki marta "
                       "qoʻllangan.</p>",
    },
    {
        "text": "<p>What is the vertex of <i>y</i> = <i>x</i><sup>2</sup> − 4<i>x</i> "
                "+ 3?</p>",
        "choices": ["(2, −1)", "(2, 3)", "(−2, −1)", "(2, 1)"],
        "correct": "(2, −1)",
        "explanation": "<p><strong>(2, −1).</strong> x = 2, keyin "
                       "y = 4 − 8 + 3 = −1.</p>"
                       "<p><strong>(2, 3)</strong> — x = 0 dagi qiymat olingan, ya'ni "
                       "y oʻqidagi nuqta.</p>",
    },
    {
        "text": "<p>What is the vertex of <i>y</i> = <i>x</i><sup>2</sup> + 6<i>x</i> "
                "+ 5?</p>",
        "choices": ["(−3, −4)", "(3, −4)", "(−3, 4)", "(−6, 5)"],
        "correct": "(−3, −4)",
        "explanation": "<p><strong>(−3, −4).</strong> x = −6 ÷ 2 = −3, keyin "
                       "y = 9 − 18 + 5 = −4.</p>"
                       "<p>Yaʼni y = (x + 3)² − 4 ✓</p>",
    },
    {
        "text": "<p>What is the vertex of <i>y</i> = 2<i>x</i><sup>2</sup> − 8<i>x</i> "
                "+ 5?</p>",
        "choices": ["(2, −3)", "(4, −3)", "(2, 5)", "(−2, −3)"],
        "correct": "(2, −3)",
        "explanation": "<p><strong>(2, −3).</strong> x = 8 ÷ 4 = 2 — maxrajda "
                       "<b>2a</b> turadi, 2 emas.</p>"
                       "<p>Keyin y = 8 − 16 + 5 = −3.</p>",
    },
    {
        "text": "<p>Which form of a quadratic shows the coordinates of the vertex as "
                "constants?</p>",
        "choices": ["y = a(x − h)² + k", "y = ax² + bx + c", "y = a(x − p)(x − q)",
                    "y = mx + b"],
        "correct": "y = a(x − h)² + k",
        "explanation": "<p><strong>Uchi shakli.</strong> Undan uch (h, k) toʻgʻridan-"
                       "toʻgʻri oʻqiladi.</p>"
                       "<p><strong>y = a(x − p)(x − q)</strong> — bu ajratilgan "
                       "koʻrinish; u <b>nollarni</b> koʻrsatadi.</p>",
    },
    {
        "text": "<p>What is the minimum value of <i>y</i> = <i>x</i><sup>2</sup> − "
                "2<i>x</i> − 3?</p>",
        "choices": ["−4", "1", "−3", "4"],
        "correct": "−4",
        "explanation": "<p><strong>−4.</strong> x = 2 ÷ 2 = 1, keyin "
                       "y = 1 − 2 − 3 = −4.</p>"
                       "<p><strong>1</strong> — bu x, minimum qayerda boʻlishi. "
                       "<strong>−3</strong> — y oʻqidagi qiymat.</p>",
    },
    {
        "text": "<p>What is the maximum value of <i>y</i> = −<i>x</i><sup>2</sup> + "
                "4<i>x</i> + 1?</p>",
        "choices": ["5", "2", "1", "−5"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> x = −4 ÷ (−2) = 2, keyin "
                       "y = −4 + 8 + 1 = 5.</p>"
                       "<p>a manfiy, demak bu maksimum — bunday funksiyaning minimal "
                       "qiymati yoʻq.</p>",
    },
    {
        "text": "<p>A student says the vertex of <i>y</i> = (<i>x</i> + 3)<sup>2</sup> "
                "− 2 is (3, −2). What is the correct vertex?</p>",
        "choices": ["(−3, −2)", "(3, 2)", "(−3, 2)", "The student is right"],
        "correct": "(−3, −2)",
        "explanation": "<p><strong>(−3, −2).</strong> Formulada (x − h) turadi, demak "
                       "qavsdagi +3 h = −3 degani.</p>"
                       "<p>k = −2 esa qavsdan tashqarida — uning ishorasi "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>A student says the minimum value of <i>y</i> = "
                "<i>x</i><sup>2</sup> − 6<i>x</i> + 5 is 3. What is the correct "
                "minimum value?</p>",
        "choices": ["−4", "3", "5", "−3"],
        "correct": "−4",
        "explanation": "<p><strong>−4.</strong> Oʻquvchi x = 3 ni topib toʻxtab qolgan; "
                       "uni tenglamaga qaytarib qoʻyish kerak: 9 − 18 + 5 = −4.</p>"
                       "<p>«Value» — funksiyaning qiymati, yaʼni y.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = (<i>x</i> − 3)<sup>2</sup> − 16 crosses the "
                "<i>x</i>-axis at which two points?</p>",
        "choices": ["x = −1 and x = 7", "x = 3 and x = 16", "x = −3 and x = 16",
                    "x = 1 and x = −7"],
        "correct": "x = −1 and x = 7",
        "explanation": "<p><strong>x = −1 va x = 7.</strong> (x − 3)² = 16 → "
                       "x − 3 = ±4.</p>"
                       "<p>Eʼtibor bering: ikkala nol ham uchdan (x = 3) bir xil "
                       "masofada — parabola simmetrik.</p>",
    },
    {
        "text": "<p>The function <i>y</i> = <i>x</i><sup>2</sup> − 6<i>x</i> + "
                "<i>k</i> has a minimum value of 0. What is the value of <i>k</i>?</p>",
        "choices": ["9", "6", "0", "3"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> Uch x = 3 da, va y = 9 − 18 + k = "
                       "k − 9. Bu nolga teng boʻlsa k = 9.</p>"
                       "<p>Natija (x − 3)² — x oʻqiga urinadigan parabola.</p>",
    },
    {
        "text": "<p>A water jet's height is <i>h</i> = −5(<i>t</i> − 3)<sup>2</sup> + "
                "45 metres, where <i>t</i> is in seconds. What is its greatest "
                "height?</p>",
        "choices": ["45 metres", "3 metres", "5 metres", "40 metres"],
        "correct": "45 metres",
        "explanation": "<p><strong>45 metr.</strong> a = −5 manfiy, demak uch "
                       "maksimum, va k = 45.</p>"
                       "<p><strong>3</strong> — bu <b>qachon</b>, yaʼni 3 soniyada. "
                       "Savol balandlikni soʻragan.</p>",
    },
    {
        "text": "<p>A shop's daily profit is <i>P</i> = −2(<i>x</i> − 15)<sup>2</sup> "
                "+ 180, where <i>x</i> is the price in dollars. What price gives the "
                "greatest profit?</p>",
        "choices": ["15 dollars", "180 dollars", "2 dollars", "30 dollars"],
        "correct": "15 dollars",
        "explanation": "<p><strong>15 dollar.</strong> Uch (15, 180) da; x — narx, "
                       "demak javob 15.</p>"
                       "<p><strong>180</strong> — bu eng katta foyda, narx emas. "
                       "SAT bu ikkisini doim aralashtiradi.</p>",
    },
]


# =====================================================================
# Testlar
# =====================================================================

PRACTICES = [
    {
        "title":       "SAT-31 Practice: Factoring Standard Quadratics (x² + bx + c)",
        "description": "20 ta SAT uslubidagi savol — koʻpaytmasi c va yigʻindisi b "
                       "boʻlgan juftlik, ishoralar va koʻpaytma nol qoidasi.",
        "tutorial":    "SAT-31:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT31,
    },
    {
        "title":       "SAT-32 Practice: Factoring Advanced Quadratics (ax² + bx + c)",
        "description": "20 ta SAT uslubidagi savol — AC usuli, guruhlash va javobni "
                       "ochib tekshirish.",
        "tutorial":    "SAT-32:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT32,
    },
    {
        "title":       "SAT-33 Practice: The Quadratic Formula and the Discriminant",
        "description": "20 ta SAT uslubidagi savol — formula, ishoralar, ildizni "
                       "soddalashtirish va kontekstli tenglamalar.",
        "tutorial":    "SAT-33:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT33,
    },
    {
        "title":       "SAT-34 Practice: Determining Number and Type of Roots using the Discriminant",
        "description": "20 ta SAT uslubidagi savol — uchta holat, grafik bilan "
                       "bogʻlanish va «exactly one solution» turidagi k savollari.",
        "tutorial":    "SAT-34:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT34,
    },
    {
        "title":       "SAT-35 Practice: Vertex Form of a Quadratic",
        "description": "20 ta SAT uslubidagi savol — uch (h, k), h ning ishorasi, "
                       "x = −b ÷ (2a) va maksimum/minimum qiymatlar.",
        "tutorial":    "SAT-35:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT35,
    },
]
