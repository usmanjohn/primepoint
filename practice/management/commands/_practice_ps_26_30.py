# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-26 … SAT-30.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context & interpretation ·
      15–16 trap-spotting · 17–18 Module 2 level · 19–20 word problems.

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_26_30.py --master=prime \\
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
# SAT-26 — rationalizing denominators
# =====================================================================

Q_SAT26 = [
    {
        "text": "<p>Which expression is equivalent to 1 ÷ √2?</p>",
        "choices": ["√2", "√2 ÷ 2", "2√2", "2 ÷ √2"],
        "correct": "√2 ÷ 2",
        "explanation": "<p><strong>√2 ÷ 2.</strong> Surat va maxrajni √2 ga "
                       "koʻpaytiramiz; maxrajda √2 × √2 = 2 qoladi.</p>"
                       "<p><strong>√2</strong> — maxrajga boʻlish unutilgan: "
                       "1 ÷ 1.414 ≈ 0.71, √2 esa ≈ 1.41.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 3 ÷ √5?</p>",
        "choices": ["3√5", "3√5 ÷ 5", "√5 ÷ 3", "√15 ÷ 5"],
        "correct": "3√5 ÷ 5",
        "explanation": "<p><strong>3√5 ÷ 5.</strong> √5 ga koʻpaytiramiz: surat 3√5, "
                       "maxraj 5. 3 va 5 ning umumiy boʻluvchisi yoʻq, demak "
                       "qisqarmaydi.</p>"
                       "<p>Tekshiruv: 3 ÷ 2.236 ≈ 1.342 va 3(2.236) ÷ 5 ≈ 1.342 ✓</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 6 ÷ √3?</p>",
        "choices": ["2√3", "3√3", "6√3", "6√3 ÷ 9"],
        "correct": "2√3",
        "explanation": "<p><strong>2√3.</strong> 6√3 ÷ 3 = 2√3 — oxirgi qisqartirishni "
                       "unutmang.</p>"
                       "<p><strong>6√3</strong> — maxrajga boʻlinmagan javob; u haqiqiy "
                       "qiymatdan uch barobar katta.</p>",
    },
    {
        "text": "<p>What is the conjugate of 5 + √7?</p>",
        "choices": ["−5 + √7", "5 − √7", "5 + √7", "√7 − 5"],
        "correct": "5 − √7",
        "explanation": "<p><strong>5 − √7.</strong> Faqat <b>oʻrtadagi</b> ishora "
                       "almashadi.</p>"
                       "<p><strong>−5 + √7</strong> — birinchi hadning ishorasi "
                       "almashtirilgan, bu qoʻshma ifoda emas.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 8 ÷ √2?</p>",
        "choices": ["4√2", "8√2", "2√2", "8√2 ÷ 4"],
        "correct": "4√2",
        "explanation": "<p><strong>4√2.</strong> 8√2 ÷ 2 = 4√2.</p>"
                       "<p>Tekshiruv: 8 ÷ 1.414 ≈ 5.66 va 4 × 1.414 ≈ 5.66 ✓</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 10 ÷ √5?</p>",
        "choices": ["2", "2√5", "5√2", "10√5"],
        "correct": "2√5",
        "explanation": "<p><strong>2√5.</strong> 10√5 ÷ 5 = 2√5.</p>"
                       "<p><strong>2</strong> — ildiz butunlay yoʻqotilgan; asl qiymat "
                       "≈ 4.47, 2 emas.</p>",
    },
    {
        "text": "<p>What is the conjugate of √3 − 2?</p>",
        "choices": ["√3 + 2", "−√3 − 2", "2 − √3", "√3 − 2"],
        "correct": "√3 + 2",
        "explanation": "<p><strong>√3 + 2.</strong> Ikki hadning orasidagi ishora "
                       "almashadi, hadlar oʻz oʻrnida qoladi.</p>"
                       "<p><strong>2 − √3</strong> — hadlar oʻrin almashgan; bu boshqa "
                       "ifoda.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 1 ÷ (2 + √3)?</p>",
        "choices": ["2 − √3", "2 + √3", "(2 − √3) ÷ 7", "(2 + √3) ÷ 7"],
        "correct": "2 − √3",
        "explanation": "<p><strong>2 − √3.</strong> Qoʻshma ifoda 2 − √3; maxraj "
                       "4 − 3 = 1, shuning uchun boʻlish kerak emas.</p>"
                       "<p>Tekshiruv: 1 ÷ 3.732 ≈ 0.268 va 2 − 1.732 ≈ 0.268 ✓</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 1 ÷ (3 − √2)?</p>",
        "choices": ["(3 − √2) ÷ 7", "(3 + √2) ÷ 7", "(3 + √2) ÷ 11", "3 + √2"],
        "correct": "(3 + √2) ÷ 7",
        "explanation": "<p><strong>(3 + √2) ÷ 7.</strong> Maxraj: (3 − √2)(3 + √2) = "
                       "9 − 2 = 7.</p>"
                       "<p><strong>(3 + √2) ÷ 11</strong> — maxrajda 9 + 2 hisoblangan; "
                       "kvadratlar <b>ayirmasi</b> boʻladi.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 4 ÷ (√5 − 1)?</p>",
        "choices": ["√5 − 1", "√5 + 1", "(√5 + 1) ÷ 4", "4√5 + 4"],
        "correct": "√5 + 1",
        "explanation": "<p><strong>√5 + 1.</strong> Qoʻshma ifoda (√5 + 1); maxraj "
                       "5 − 1 = 4, va 4 ÷ 4 = 1.</p>"
                       "<p>Tekshiruv: 4 ÷ 1.236 ≈ 3.24 va 2.236 + 1 ≈ 3.24 ✓</p>",
    },
    {
        "text": "<p>Why did mathematicians before calculators prefer to move the radical "
                "out of the denominator?</p>",
        "choices": ["Because dividing by a whole number by hand is far easier than dividing by a decimal",
                    "Because the answer changes when the radical moves",
                    "Because radicals are not allowed in fractions",
                    "Because it makes the number smaller"],
        "correct": "Because dividing by a whole number by hand is far easier than dividing by a decimal",
        "explanation": "<p><strong>Chunki butun songa boʻlish qoʻlda ancha oson.</strong> "
                       "1.41421 ni 2 ga boʻlish — bir necha soniya; 1 ni 1.41421 ga "
                       "boʻlish esa uzun boʻlish.</p>"
                       "<p>Javob esa oʻzgarmaydi — faqat yozilish shakli.</p>",
    },
    {
        "text": "<p>Which of these expressions still needs to be rationalized?</p>",
        "choices": ["√3 ÷ 3", "2√5", "5 ÷ √7", "(1 + √2) ÷ 4"],
        "correct": "5 ÷ √7",
        "explanation": "<p><strong>5 ÷ √7.</strong> Faqat unda ildiz <b>maxrajda</b> "
                       "turibdi.</p>"
                       "<p>Qolganlarida ildiz suratda yoki umuman kasr yoʻq — ular "
                       "allaqachon qabul qilingan koʻrinishda.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 12 ÷ √6?</p>",
        "choices": ["2√6", "6√2", "12√6", "12√6 ÷ 36"],
        "correct": "2√6",
        "explanation": "<p><strong>2√6.</strong> 12√6 ÷ 6 = 2√6.</p>"
                       "<p>Tekshiruv: 12 ÷ 2.449 ≈ 4.90 va 2 × 2.449 ≈ 4.90 ✓</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 2 ÷ √8?</p>",
        "choices": ["√2 ÷ 2", "2√8", "√8 ÷ 4", "4√2"],
        "correct": "√2 ÷ 2",
        "explanation": "<p><strong>√2 ÷ 2.</strong> Avval soddalashtiramiz: √8 = 2√2, "
                       "demak 2 ÷ (2√2) = 1 ÷ √2 = √2 ÷ 2.</p>"
                       "<p>Ildizni <b>oldin</b> soddalashtirish (SAT-25) hisobni ancha "
                       "yengillashtiradi.</p>",
    },
    {
        "text": "<p>A student writes 1 ÷ √2 = √2. What is the mistake?</p>",
        "choices": ["The denominator was left out after multiplying",
                    "The conjugate should have been used",
                    "√2 × √2 is not 2",
                    "There is no mistake"],
        "correct": "The denominator was left out after multiplying",
        "explanation": "<p><strong>Koʻpaytirgandan keyin maxraj tashlab ketilgan.</strong> "
                       "Toʻgʻrisi √2 ÷ 2.</p>"
                       "<p>Tekshiruv: 1 ÷ 1.414 ≈ 0.71, √2 ≈ 1.41 — javob ikki barobar "
                       "katta.</p>",
    },
    {
        "text": "<p>A student says the conjugate of 2 + √3 is −2 + √3. What is the "
                "mistake?</p>",
        "choices": ["Only the sign between the two terms should change",
                    "The order of the terms should change",
                    "The radical should be removed",
                    "There is no mistake"],
        "correct": "Only the sign between the two terms should change",
        "explanation": "<p><strong>Faqat oʻrtadagi ishora almashadi:</strong> "
                       "2 − √3.</p>"
                       "<p>Birinchi hadning ishorasini almashtirsangiz, koʻpaytirganda "
                       "kvadratlar ayirmasi hosil boʻlmaydi va ildiz yoʻqolmaydi.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 6 ÷ (√7 + 1)?</p>",
        "choices": ["√7 − 1", "√7 + 1", "(√7 − 1) ÷ 6", "6√7 − 6"],
        "correct": "√7 − 1",
        "explanation": "<p><strong>√7 − 1.</strong> Qoʻshma ifoda (√7 − 1); maxraj "
                       "7 − 1 = 6, va 6 ÷ 6 = 1.</p>"
                       "<p>Tekshiruv: 6 ÷ 3.646 ≈ 1.646 va 2.646 − 1 ≈ 1.646 ✓</p>",
    },
    {
        "text": "<p>Which expression is equivalent to √3 ÷ √12?</p>",
        "choices": ["1 ÷ 2", "√3 ÷ 12", "2", "√36"],
        "correct": "1 ÷ 2",
        "explanation": "<p><strong>1 ÷ 2.</strong> √12 = 2√3, demak √3 ÷ (2√3) = "
                       "1 ÷ 2 — ildizlar qisqaradi.</p>"
                       "<p>Yoki: √(3 ÷ 12) = √(1/4) = 1/2 — ikkala yoʻl ham bir xil "
                       "javob beradi.</p>",
    },
    {
        "text": "<p>A square has an area of 50 square metres. A path runs along one side. "
                "What is 100 divided by the side length, in simplest form?</p>",
        "choices": ["10√2", "20 ÷ √2", "2√50", "100√50 ÷ 50"],
        "correct": "10√2",
        "explanation": "<p><strong>10√2.</strong> Tomoni √50 = 5√2, va 100 ÷ (5√2) = "
                       "20 ÷ √2 = 10√2.</p>"
                       "<p>Tekshiruv: 100 ÷ 7.071 ≈ 14.14 va 10 × 1.414 ≈ 14.14 ✓ "
                       "<strong>20 ÷ √2</strong> toʻgʻri qiymat, lekin hali "
                       "ratsionallashtirilmagan.</p>",
    },
    {
        "text": "<p>On A-series paper the short side divided by the long side is 1 ÷ √2. "
                "Written without a radical in the denominator, what is that ratio?</p>",
        "choices": ["√2 ÷ 2", "2 ÷ √2", "√2", "2√2"],
        "correct": "√2 ÷ 2",
        "explanation": "<p><strong>√2 ÷ 2</strong> — taxminan 0.707, yaʼni qisqa tomon "
                       "uzun tomonning taxminan 71 foizi.</p>"
                       "<p>Bu SAT-24 dagi A4 qogʻoz nisbatining teskarisi: uzun tomon "
                       "qisqasidan √2 marta katta.</p>",
    },
]


# =====================================================================
# SAT-27 — polynomials: adding and subtracting
# =====================================================================

Q_SAT27 = [
    {
        "text": "<p>Simplify: (2<i>x</i><sup>2</sup> + 3<i>x</i>) + "
                "(<i>x</i><sup>2</sup> − <i>x</i>)</p>",
        "choices": ["3<i>x</i><sup>2</sup> + 2<i>x</i>", "3<i>x</i><sup>2</sup> + 4<i>x</i>",
                    "2<i>x</i><sup>2</sup> + 2<i>x</i>", "3<i>x</i><sup>4</sup> + 2<i>x</i>"],
        "correct": "3<i>x</i><sup>2</sup> + 2<i>x</i>",
        "explanation": "<p><strong>3x<sup>2</sup> + 2x.</strong> 2 + 1 = 3 va "
                       "3 − 1 = 2.</p>"
                       "<p><strong>3x<sup>4</sup></strong> — qoʻshganda daraja "
                       "oʻzgarmaydi; koʻrsatkichlar qoʻshilmaydi.</p>",
    },
    {
        "text": "<p>Simplify: (5<i>x</i> − 4) − (2<i>x</i> − 9)</p>",
        "choices": ["3<i>x</i> − 13", "3<i>x</i> + 5", "7<i>x</i> − 13",
                    "3<i>x</i> − 5"],
        "correct": "3<i>x</i> + 5",
        "explanation": "<p><strong>3x + 5.</strong> Ikkinchi qavs ishoralarini "
                       "almashtiradi: −2x va <b>+9</b>. Keyin −4 + 9 = 5.</p>"
                       "<p><strong>3x − 13</strong> — −9 ning ishorasi "
                       "almashtirilmagan.</p>",
    },
    {
        "text": "<p>What is the degree of the polynomial 7<i>x</i><sup>4</sup> − "
                "3<i>x</i><sup>2</sup> + 1?</p>",
        "choices": ["1", "3", "4", "7"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Daraja — eng katta koʻrsatkich.</p>"
                       "<p><strong>3</strong> — hadlar soni; <strong>7</strong> — bosh "
                       "koeffitsient. Uchalasi uch xil narsa.</p>",
    },
    {
        "text": "<p>What is the leading coefficient of 5 − 2<i>x</i><sup>3</sup> + "
                "<i>x</i>?</p>",
        "choices": ["−2", "1", "3", "5"],
        "correct": "−2",
        "explanation": "<p><strong>−2.</strong> Standart koʻrinishda: "
                       "−2x<sup>3</sup> + x + 5. Eng katta darajali had −2x<sup>3</sup>, "
                       "koeffitsienti ishorasi bilan −2.</p>"
                       "<p><strong>5</strong> — birinchi yozilgan son, lekin hadlarning "
                       "tartibi ahamiyatsiz.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to (3<i>x</i><sup>2</sup> + 5<i>x</i> "
                "− 2) + (<i>x</i><sup>2</sup> − 4<i>x</i> + 7)?</p>",
        "choices": ["4<i>x</i><sup>2</sup> + <i>x</i> + 5",
                    "4<i>x</i><sup>2</sup> + 9<i>x</i> + 5",
                    "4<i>x</i><sup>2</sup> + <i>x</i> − 9",
                    "2<i>x</i><sup>2</sup> + 9<i>x</i> − 9"],
        "correct": "4<i>x</i><sup>2</sup> + <i>x</i> + 5",
        "explanation": "<p><strong>4x<sup>2</sup> + x + 5.</strong> 3 + 1 = 4, "
                       "5 − 4 = 1, −2 + 7 = 5.</p>"
                       "<p><strong>2x<sup>2</sup> + 9x − 9</strong> — qoʻshish oʻrniga "
                       "ayirilgan javob.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to (3<i>x</i><sup>2</sup> + 5<i>x</i> "
                "− 2) − (<i>x</i><sup>2</sup> − 4<i>x</i> + 7)?</p>",
        "choices": ["2<i>x</i><sup>2</sup> + <i>x</i> + 5",
                    "2<i>x</i><sup>2</sup> + 9<i>x</i> − 9",
                    "2<i>x</i><sup>2</sup> + 9<i>x</i> + 5",
                    "2<i>x</i><sup>2</sup> + <i>x</i> − 9"],
        "correct": "2<i>x</i><sup>2</sup> + 9<i>x</i> − 9",
        "explanation": "<p><strong>2x<sup>2</sup> + 9x − 9.</strong> Ikkinchi qavsning "
                       "uchala hadi ham ishorasini almashtiradi: −x<sup>2</sup>, +4x, "
                       "−7.</p>"
                       "<p>Keyin 5x + 4x = 9x va −2 − 7 = −9.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to (4<i>x</i><sup>2</sup> − 3<i>x</i> "
                "+ 1) − (2<i>x</i><sup>2</sup> + 5<i>x</i> − 6)?</p>",
        "choices": ["2<i>x</i><sup>2</sup> − 8<i>x</i> + 7",
                    "2<i>x</i><sup>2</sup> − 8<i>x</i> − 5",
                    "2<i>x</i><sup>2</sup> + 2<i>x</i> − 5",
                    "6<i>x</i><sup>2</sup> + 2<i>x</i> − 5"],
        "correct": "2<i>x</i><sup>2</sup> − 8<i>x</i> + 7",
        "explanation": "<p><strong>2x<sup>2</sup> − 8x + 7.</strong> 4 − 2 = 2, "
                       "−3 − 5 = −8, 1 + 6 = 7.</p>"
                       "<p><strong>2x<sup>2</sup> − 8x − 5</strong> — oxirgi hadning "
                       "ishorasi almashtirilmagan.</p>",
    },
    {
        "text": "<p>Simplify: (<i>x</i><sup>3</sup> + 2<i>x</i>) + "
                "(3<i>x</i><sup>3</sup> − <i>x</i> + 5)</p>",
        "choices": ["4<i>x</i><sup>3</sup> + <i>x</i> + 5",
                    "4<i>x</i><sup>3</sup> + 3<i>x</i> + 5",
                    "3<i>x</i><sup>3</sup> + <i>x</i> + 5",
                    "4<i>x</i><sup>6</sup> + <i>x</i> + 5"],
        "correct": "4<i>x</i><sup>3</sup> + <i>x</i> + 5",
        "explanation": "<p><strong>4x<sup>3</sup> + x + 5.</strong> 1 + 3 = 4, "
                       "2x − x = x, va 5 yolgʻiz qoladi.</p>"
                       "<p><strong>4x<sup>6</sup></strong> — koʻrsatkichlar qoʻshilgan; "
                       "qoʻshishda daraja oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Simplify: (6<i>x</i><sup>2</sup> − <i>x</i>) − "
                "(6<i>x</i><sup>2</sup> + 3<i>x</i>)</p>",
        "choices": ["−4<i>x</i>", "2<i>x</i>", "12<i>x</i><sup>2</sup> + 2<i>x</i>",
                    "−2<i>x</i>"],
        "correct": "−4<i>x</i>",
        "explanation": "<p><strong>−4x.</strong> 6x<sup>2</sup> lar qisqaradi, va "
                       "−x − 3x = −4x.</p>"
                       "<p>Eʼtibor bering: natijaning darajasi 1 ga tushdi — ayirishda "
                       "bosh hadlar qisqarsa, daraja kamayishi mumkin.</p>",
    },
    {
        "text": "<p>Which of the following is <b>NOT</b> a polynomial?</p>",
        "choices": ["3<i>x</i><sup>2</sup> − 5", "<i>x</i><sup>3</sup> + <i>x</i>",
                    "3<i>x</i><sup>−2</sup> + 1", "7"],
        "correct": "3<i>x</i><sup>−2</sup> + 1",
        "explanation": "<p><strong>3x<sup>−2</sup> + 1.</strong> Koʻphadda koʻrsatkich "
                       "<b>butun va manfiy boʻlmagan</b> boʻlishi shart.</p>"
                       "<p><strong>7</strong> ham koʻphad — nol darajali "
                       "(oʻzgarmas).</p>",
    },
    {
        "text": "<p>A rectangle has length (3<i>x</i> + 2) and width (<i>x</i> + 5). "
                "Which expression gives its perimeter?</p>",
        "choices": ["4<i>x</i> + 7", "8<i>x</i> + 14", "3<i>x</i><sup>2</sup> + 17<i>x</i> + 10",
                    "8<i>x</i> + 7"],
        "correct": "8<i>x</i> + 14",
        "explanation": "<p><strong>8x + 14.</strong> Perimetr = 2(uzunlik + eni) = "
                       "2(4x + 7).</p>"
                       "<p><strong>4x + 7</strong> — ikkiga koʻpaytirish unutilgan; "
                       "<strong>3x<sup>2</sup> + …</strong> — bu yuza, perimetr "
                       "emas.</p>",
    },
    {
        "text": "<p>In the polynomial −2<i>x</i><sup>3</sup> + <i>x</i> + 5, what is the "
                "constant term?</p>",
        "choices": ["−2", "1", "3", "5"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Oʻzgarmas had — harfsiz had.</p>"
                       "<p><strong>−2</strong> — bosh koeffitsient; <strong>3</strong> — "
                       "daraja. SAT uchalasini bitta savolda soʻrashi mumkin.</p>",
    },
    {
        "text": "<p>A company's income is (5<i>x</i> + 200) and its costs are "
                "(2<i>x</i> + 50), where <i>x</i> is the number of items sold. Which "
                "expression gives the profit?</p>",
        "choices": ["3<i>x</i> + 150", "3<i>x</i> + 250", "7<i>x</i> + 250",
                    "3<i>x</i> − 150"],
        "correct": "3<i>x</i> + 150",
        "explanation": "<p><strong>3x + 150.</strong> Foyda = daromad − xarajat: "
                       "5x − 2x = 3x va 200 − 50 = 150.</p>"
                       "<p><strong>3x + 250</strong> — 50 ning ishorasi "
                       "almashtirilmagan (200 + 50).</p>",
    },
    {
        "text": "<p>Using income (5<i>x</i> + 200) and costs (2<i>x</i> + 50), what is "
                "the profit when 40 items are sold?</p>",
        "choices": ["$150", "$270", "$400", "$530"],
        "correct": "$270",
        "explanation": "<p><strong>$270.</strong> Foyda 3x + 150, va 3(40) + 150 = "
                       "120 + 150 = 270.</p>"
                       "<p><strong>$400</strong> — daromad (5 × 40 + 200) minus emas, "
                       "yaʼni xarajat ayirilmagan javob.</p>",
    },
    {
        "text": "<p>A student writes (5<i>x</i> − 4) − (2<i>x</i> − 9) = 3<i>x</i> − 13. "
                "What is the mistake?</p>",
        "choices": ["Only the first term of the second bracket changed sign",
                    "The x terms were subtracted incorrectly",
                    "The brackets should have been multiplied",
                    "There is no mistake"],
        "correct": "Only the first term of the second bracket changed sign",
        "explanation": "<p><strong>Faqat birinchi hadning ishorasi almashtirilgan.</strong> "
                       "−(−9) = <b>+9</b>, demak −4 + 9 = 5.</p>"
                       "<p>Tekshiruv: x = 1 da asl ifoda 1 − (−7) = 8, va 3 + 5 = 8 ✓</p>",
    },
    {
        "text": "<p>Is 3<i>x</i><sup>2</sup> + 2<i>x</i> equal to 5<i>x</i><sup>3</sup>?</p>",
        "choices": ["Yes", "No — the terms are not alike and cannot be combined",
                    "Yes, but only when x = 1", "No — it equals 5x<sup>2</sup>"],
        "correct": "No — the terms are not alike and cannot be combined",
        "explanation": "<p><strong>Yoʻq — ular oʻxshash hadlar emas.</strong> Faqat "
                       "bir xil darajali hadlar birlashadi.</p>"
                       "<p>Tekshiruv: x = 2 da 12 + 4 = 16, 5(8) = 40 — teng emas.</p>",
    },
    {
        "text": "<p>Simplify: (<i>x</i><sup>2</sup> + 3<i>x</i> − 1) + "
                "(2<i>x</i><sup>2</sup> − 5) − (<i>x</i><sup>2</sup> + <i>x</i>)</p>",
        "choices": ["2<i>x</i><sup>2</sup> + 2<i>x</i> − 6",
                    "2<i>x</i><sup>2</sup> + 4<i>x</i> − 6",
                    "4<i>x</i><sup>2</sup> + 2<i>x</i> − 6",
                    "2<i>x</i><sup>2</sup> + 2<i>x</i> + 4"],
        "correct": "2<i>x</i><sup>2</sup> + 2<i>x</i> − 6",
        "explanation": "<p><strong>2x<sup>2</sup> + 2x − 6.</strong> "
                       "x<sup>2</sup>: 1 + 2 − 1 = 2. x: 3 − 1 = 2. Sonlar: "
                       "−1 − 5 = −6.</p>"
                       "<p>Uchta qavs boʻlsa ham qoida oʻsha: faqat oxirgisining "
                       "oldida minus turibdi.</p>",
    },
    {
        "text": "<p>If (<i>ax</i><sup>2</sup> + 3<i>x</i>) + (2<i>x</i><sup>2</sup> − "
                "<i>x</i>) = 7<i>x</i><sup>2</sup> + 2<i>x</i>, what is the value of "
                "<i>a</i>?</p>",
        "choices": ["2", "5", "7", "9"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> x<sup>2</sup> hadlari: a + 2 = 7, demak "
                       "a = 5.</p>"
                       "<p><strong>7</strong> — natijaning koeffitsienti koʻchirilgan; "
                       "unda 2 ni ayirish kerak edi.</p>",
    },
    {
        "text": "<p>A triangle has sides of (2<i>x</i> + 1), (3<i>x</i> − 2) and "
                "(<i>x</i> + 6). What is its perimeter?</p>",
        "choices": ["5<i>x</i> + 5", "6<i>x</i> + 5", "6<i>x</i> + 9",
                    "6<i>x</i><sup>3</sup> + 5"],
        "correct": "6<i>x</i> + 5",
        "explanation": "<p><strong>6x + 5.</strong> 2x + 3x + x = 6x va "
                       "1 − 2 + 6 = 5.</p>"
                       "<p><strong>6x + 9</strong> — −2 ning ishorasi eʼtiborsiz "
                       "qolgan (1 + 2 + 6).</p>",
    },
    {
        "text": "<p>A builder's plan shows two rooms with floor areas (3<i>x</i> + 12) "
                "and (5<i>x</i> + 5) square metres, and a corridor of (2<i>x</i> + 3) "
                "square metres is taken out of the total. What is the remaining area?</p>",
        "choices": ["6<i>x</i> + 14", "6<i>x</i> + 20", "10<i>x</i> + 20",
                    "8<i>x</i> + 17"],
        "correct": "6<i>x</i> + 14",
        "explanation": "<p><strong>6x + 14.</strong> Yigʻindi 8x + 17, undan "
                       "(2x + 3) ayiriladi: 8x − 2x = 6x va 17 − 3 = 14.</p>"
                       "<p><strong>8x + 17</strong> — koridor ayirilmagan; "
                       "<strong>10x + 20</strong> — ayirish oʻrniga qoʻshilgan.</p>",
    },
]


# =====================================================================
# SAT-28 — multiplying polynomials
# =====================================================================

Q_SAT28 = [
    {
        "text": "<p>Expand: (<i>x</i> + 2)(<i>x</i> + 7)</p>",
        "choices": ["<i>x</i><sup>2</sup> + 9<i>x</i> + 14", "<i>x</i><sup>2</sup> + 14",
                    "<i>x</i><sup>2</sup> + 5<i>x</i> + 14", "2<i>x</i> + 9"],
        "correct": "<i>x</i><sup>2</sup> + 9<i>x</i> + 14",
        "explanation": "<p><strong>x<sup>2</sup> + 9x + 14.</strong> Oʻrtada "
                       "7x + 2x = 9x.</p>"
                       "<p><strong>x<sup>2</sup> + 14</strong> — oʻrtadagi ikki "
                       "koʻpaytma tashlab ketilgan.</p>",
    },
    {
        "text": "<p>Expand: (<i>x</i> − 4)(<i>x</i> + 4)</p>",
        "choices": ["<i>x</i><sup>2</sup> − 16", "<i>x</i><sup>2</sup> + 16",
                    "<i>x</i><sup>2</sup> − 8<i>x</i> − 16", "<i>x</i><sup>2</sup> + 8<i>x</i> − 16"],
        "correct": "<i>x</i><sup>2</sup> − 16",
        "explanation": "<p><strong>x<sup>2</sup> − 16.</strong> Oʻrtadagi hadlar "
                       "(+4x va −4x) bir-birini yoʻqotadi.</p>"
                       "<p>Bu SAT-30 dagi kvadratlar ayirmasi — teskari "
                       "yoʻnalishda.</p>",
    },
    {
        "text": "<p>Expand: (2<i>x</i> + 1)(3<i>x</i> − 2)</p>",
        "choices": ["6<i>x</i><sup>2</sup> − <i>x</i> − 2", "6<i>x</i><sup>2</sup> + <i>x</i> − 2",
                    "6<i>x</i><sup>2</sup> − 2", "5<i>x</i><sup>2</sup> − <i>x</i> − 2"],
        "correct": "6<i>x</i><sup>2</sup> − <i>x</i> − 2",
        "explanation": "<p><strong>6x<sup>2</sup> − x − 2.</strong> Oʻrtada "
                       "−4x + 3x = −x.</p>"
                       "<p><strong>+x</strong> — ishora xatosi: kattaroq koʻpaytma "
                       "(−4x) manfiy edi.</p>",
    },
    {
        "text": "<p>Expand: (<i>x</i> + 5)<sup>2</sup></p>",
        "choices": ["<i>x</i><sup>2</sup> + 25", "<i>x</i><sup>2</sup> + 10<i>x</i> + 25",
                    "<i>x</i><sup>2</sup> + 5<i>x</i> + 25", "2<i>x</i> + 10"],
        "correct": "<i>x</i><sup>2</sup> + 10<i>x</i> + 25",
        "explanation": "<p><strong>x<sup>2</sup> + 10x + 25.</strong> Kvadrat — bu "
                       "(x + 5)(x + 5), demak oʻrtada 5x + 5x = 10x.</p>"
                       "<p><strong>x<sup>2</sup> + 25</strong> — SAT'dagi eng qadimiy "
                       "xato. Tekshiruv: x = 1 da 36, va 1 + 25 = 26.</p>",
    },
    {
        "text": "<p>Expand: (2<i>x</i> + 3)(<i>x</i> − 5)</p>",
        "choices": ["2<i>x</i><sup>2</sup> − 7<i>x</i> − 15", "2<i>x</i><sup>2</sup> + 7<i>x</i> − 15",
                    "2<i>x</i><sup>2</sup> − 13<i>x</i> − 15", "2<i>x</i><sup>2</sup> − 15"],
        "correct": "2<i>x</i><sup>2</sup> − 7<i>x</i> − 15",
        "explanation": "<p><strong>2x<sup>2</sup> − 7x − 15.</strong> Oʻrtada "
                       "−10x + 3x = −7x.</p>"
                       "<p><strong>−13x</strong> — ikki hadni qoʻshib yuborgan javob "
                       "(−10 − 3).</p>",
    },
    {
        "text": "<p>Expand: (3<i>x</i> − 1)(<i>x</i> + 2)</p>",
        "choices": ["3<i>x</i><sup>2</sup> + 5<i>x</i> − 2", "3<i>x</i><sup>2</sup> − 5<i>x</i> − 2",
                    "3<i>x</i><sup>2</sup> + 7<i>x</i> − 2", "3<i>x</i><sup>2</sup> − 2"],
        "correct": "3<i>x</i><sup>2</sup> + 5<i>x</i> − 2",
        "explanation": "<p><strong>3x<sup>2</sup> + 5x − 2.</strong> Oʻrtada "
                       "6x − x = 5x.</p>"
                       "<p><strong>−5x</strong> — ishoralar almashtirilgan: kattaroq "
                       "koʻpaytma (+6x) musbat edi.</p>",
    },
    {
        "text": "<p>Expand: (<i>x</i> − 3)(<i>x</i> − 4)</p>",
        "choices": ["<i>x</i><sup>2</sup> − 7<i>x</i> + 12", "<i>x</i><sup>2</sup> + 7<i>x</i> + 12",
                    "<i>x</i><sup>2</sup> − 7<i>x</i> − 12", "<i>x</i><sup>2</sup> − 12"],
        "correct": "<i>x</i><sup>2</sup> − 7<i>x</i> + 12",
        "explanation": "<p><strong>x<sup>2</sup> − 7x + 12.</strong> Ikki manfiy son "
                       "koʻpaytirilganda oxirgi had <b>musbat</b> boʻladi: "
                       "(−3)(−4) = +12.</p>"
                       "<p>Oʻrtada esa −4x − 3x = −7x.</p>",
    },
    {
        "text": "<p>In the product (3<i>x</i> − 2)(<i>x</i> + 4), what is the "
                "coefficient of <i>x</i>?</p>",
        "choices": ["−8", "3", "10", "12"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> Faqat ikkita koʻpaytma x beradi: "
                       "3x · 4 = 12x va (−2) · x = −2x. Demak 12 − 2 = 10.</p>"
                       "<p><strong>−8</strong> — oʻzgarmas had (−2 × 4).</p>",
    },
    {
        "text": "<p>In the product (2<i>x</i> + 5)(<i>x</i> − 3), what is the constant "
                "term?</p>",
        "choices": ["−15", "−1", "2", "15"],
        "correct": "−15",
        "explanation": "<p><strong>−15.</strong> Oʻzgarmas had — ikki oxirgi hadning "
                       "koʻpaytmasi: 5 × (−3).</p>"
                       "<p><strong>−1</strong> — x ning koeffitsienti (−6 + 5). "
                       "Savol qaysi hadni soʻraganiga qarang.</p>",
    },
    {
        "text": "<p>Expand: (<i>x</i> + 3)(<i>x</i><sup>2</sup> − 2<i>x</i> + 1)</p>",
        "choices": ["<i>x</i><sup>3</sup> + <i>x</i><sup>2</sup> − 5<i>x</i> + 3",
                    "<i>x</i><sup>3</sup> − 2<i>x</i><sup>2</sup> + 3",
                    "<i>x</i><sup>3</sup> + 5<i>x</i><sup>2</sup> + <i>x</i> + 3",
                    "<i>x</i><sup>3</sup> + <i>x</i><sup>2</sup> + 5<i>x</i> + 3"],
        "correct": "<i>x</i><sup>3</sup> + <i>x</i><sup>2</sup> − 5<i>x</i> + 3",
        "explanation": "<p><strong>x<sup>3</sup> + x<sup>2</sup> − 5x + 3.</strong> "
                       "Oltita koʻpaytma: x·(x²−2x+1) va 3·(x²−2x+1).</p>"
                       "<p>−2x<sup>2</sup> + 3x<sup>2</sup> = x<sup>2</sup> va "
                       "x − 6x = −5x.</p>",
    },
    {
        "text": "<p>A rectangular garden is (<i>x</i> + 3) metres by (<i>x</i> + 5) "
                "metres. Which expression gives its area?</p>",
        "choices": ["2<i>x</i> + 8", "4<i>x</i> + 16",
                    "<i>x</i><sup>2</sup> + 8<i>x</i> + 15", "<i>x</i><sup>2</sup> + 15"],
        "correct": "<i>x</i><sup>2</sup> + 8<i>x</i> + 15",
        "explanation": "<p><strong>x<sup>2</sup> + 8x + 15.</strong> Yuza = uzunlik × "
                       "eni.</p>"
                       "<p><strong>4x + 16</strong> — bu perimetr; <strong>2x + 8</strong> "
                       "— perimetrning yarmi.</p>",
    },
    {
        "text": "<p>How many separate products are formed when a two-term bracket is "
                "multiplied by a three-term bracket?</p>",
        "choices": ["Five", "Six", "Eight", "Nine"],
        "correct": "Six",
        "explanation": "<p><strong>Oltita.</strong> Har bir had har bir hadga "
                       "koʻpaytiriladi: 2 × 3 = 6.</p>"
                       "<p>Bu eng tez tekshiruv: beshta yozgan boʻlsangiz, bittasini "
                       "tashlab ketgansiz.</p>",
    },
    {
        "text": "<p>A garden is (<i>x</i> + 3) by (<i>x</i> + 5) metres. If <i>x</i> = 10, "
                "what is the area in square metres?</p>",
        "choices": ["130", "160", "195", "215"],
        "correct": "195",
        "explanation": "<p><strong>195.</strong> 13 × 15 = 195. Formula bilan ham: "
                       "100 + 80 + 15 = 195 ✓</p>"
                       "<p>Ikki yoʻl bir xil javob berishi — ifodaning toʻgʻri "
                       "ekanining isboti.</p>",
    },
    {
        "text": "<p>Expand: (<i>x</i> − 2)<sup>2</sup></p>",
        "choices": ["<i>x</i><sup>2</sup> − 4", "<i>x</i><sup>2</sup> + 4",
                    "<i>x</i><sup>2</sup> − 4<i>x</i> + 4", "<i>x</i><sup>2</sup> − 4<i>x</i> − 4"],
        "correct": "<i>x</i><sup>2</sup> − 4<i>x</i> + 4",
        "explanation": "<p><strong>x<sup>2</sup> − 4x + 4.</strong> Oʻrtada "
                       "−2x − 2x = −4x; oxirgi had (−2)(−2) = +4.</p>"
                       "<p><strong>x<sup>2</sup> − 4</strong> — bu (x − 2)(x + 2) ning "
                       "javobi, butunlay boshqa ifoda.</p>",
    },
    {
        "text": "<p>A student writes (<i>x</i> + 5)<sup>2</sup> = <i>x</i><sup>2</sup> + "
                "25. What is the mistake?</p>",
        "choices": ["The middle term 10x is missing",
                    "The 25 should be 10", "The square should be a cube",
                    "There is no mistake"],
        "correct": "The middle term 10x is missing",
        "explanation": "<p><strong>Oʻrtadagi 10x had yoʻq.</strong> Kvadrat — ikkita "
                       "qavsning koʻpaytmasi, demak toʻrtta koʻpaytma boʻladi.</p>"
                       "<p>Tekshiruv: x = 1 da (6)<sup>2</sup> = 36, lekin 1 + 25 = "
                       "26.</p>",
    },
    {
        "text": "<p>A student writes (<i>x</i> + 3)(<i>x</i> + 5) = <i>x</i><sup>2</sup> "
                "+ 15. Which two products were left out?</p>",
        "choices": ["3x and 5x", "3 and 5", "x and 15", "x<sup>2</sup> and 15"],
        "correct": "3x and 5x",
        "explanation": "<p><strong>3x va 5x.</strong> Ular qoʻshilib oʻrtadagi 8x "
                       "hadni beradi.</p>"
                       "<p>FOIL toʻrtta koʻpaytmani nazarda tutadi; faqat First va "
                       "Last hisoblangan.</p>",
    },
    {
        "text": "<p>Expand: (2<i>x</i> − 3)<sup>2</sup></p>",
        "choices": ["4<i>x</i><sup>2</sup> − 9", "4<i>x</i><sup>2</sup> + 9",
                    "4<i>x</i><sup>2</sup> − 12<i>x</i> + 9", "4<i>x</i><sup>2</sup> − 6<i>x</i> + 9"],
        "correct": "4<i>x</i><sup>2</sup> − 12<i>x</i> + 9",
        "explanation": "<p><strong>4x<sup>2</sup> − 12x + 9.</strong> Oʻrtada "
                       "−6x − 6x = −12x.</p>"
                       "<p><strong>−6x</strong> — faqat bitta oʻrta koʻpaytma "
                       "hisoblangan; ular ikkita.</p>",
    },
    {
        "text": "<p>In the product (<i>x</i> + <i>a</i>)(<i>x</i> + 3) the coefficient "
                "of <i>x</i> is 7. What is the value of <i>a</i>?</p>",
        "choices": ["3", "4", "7", "10"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Oʻrtadagi had (a + 3)x, demak "
                       "a + 3 = 7 va a = 4.</p>"
                       "<p><strong>7</strong> — koeffitsientning oʻzi koʻchirilgan; "
                       "undan 3 ni ayirish kerak edi.</p>",
    },
    {
        "text": "<p>A square plot has sides of (<i>x</i> + 4) metres. Which expression "
                "gives its area?</p>",
        "choices": ["<i>x</i><sup>2</sup> + 16", "<i>x</i><sup>2</sup> + 8<i>x</i> + 16",
                    "4<i>x</i> + 16", "2<i>x</i> + 8"],
        "correct": "<i>x</i><sup>2</sup> + 8<i>x</i> + 16",
        "explanation": "<p><strong>x<sup>2</sup> + 8x + 16.</strong> Kvadratning "
                       "yuzasi tomon × tomon = (x + 4)<sup>2</sup>.</p>"
                       "<p><strong>4x + 16</strong> — perimetr; <strong>x<sup>2</sup> "
                       "+ 16</strong> — oʻrta had unutilgan.</p>",
    },
    {
        "text": "<p>A rectangle is (2<i>x</i> + 1) metres by (<i>x</i> + 6) metres. What "
                "is its area when <i>x</i> = 4?</p>",
        "choices": ["50", "60", "90", "130"],
        "correct": "90",
        "explanation": "<p><strong>90.</strong> Tomonlari 9 va 10, demak yuza 90.</p>"
                       "<p>Ifoda bilan ham: 2x<sup>2</sup> + 13x + 6 = 32 + 52 + 6 = "
                       "90 ✓ — ikki yoʻl bir xil javob beradi.</p>",
    },
]


# =====================================================================
# SAT-29 — factoring: GCF and grouping
# =====================================================================

Q_SAT29 = [
    {
        "text": "<p>Factor: 6<i>x</i> + 9</p>",
        "choices": ["3(2<i>x</i> + 3)", "3(2<i>x</i> + 9)", "6(<i>x</i> + 3)",
                    "9(<i>x</i> + 1)"],
        "correct": "3(2<i>x</i> + 3)",
        "explanation": "<p><strong>3(2x + 3).</strong> 6 va 9 ning EKUBi 3.</p>"
                       "<p>Tekshiruv: 3 · 2x = 6x ✓ va 3 · 3 = 9 ✓</p>",
    },
    {
        "text": "<p>Factor: 5<i>x</i><sup>2</sup> − 15<i>x</i></p>",
        "choices": ["5(<i>x</i><sup>2</sup> − 3<i>x</i>)", "5<i>x</i>(<i>x</i> − 3)",
                    "5<i>x</i>(<i>x</i> − 15)", "<i>x</i>(5<i>x</i> − 15)"],
        "correct": "5<i>x</i>(<i>x</i> − 3)",
        "explanation": "<p><strong>5x(x − 3).</strong> Son 5, harf x — ikkalasi ham "
                       "umumiy.</p>"
                       "<p><strong>5(x<sup>2</sup> − 3x)</strong> toʻliq emas: qavs "
                       "ichida hali x bor.</p>",
    },
    {
        "text": "<p>Factor: 12<i>x</i><sup>2</sup><i>y</i> − 18<i>xy</i><sup>2</sup></p>",
        "choices": ["6<i>xy</i>(2<i>x</i> − 3<i>y</i>)", "6<i>x</i>(2<i>xy</i> − 3<i>y</i><sup>2</sup>)",
                    "3<i>xy</i>(4<i>x</i> − 6<i>y</i>)", "6<i>xy</i>(2<i>x</i> − 3)"],
        "correct": "6<i>xy</i>(2<i>x</i> − 3<i>y</i>)",
        "explanation": "<p><strong>6xy(2x − 3y).</strong> 12 va 18 ning EKUBi 6; har "
                       "ikki harfdan bittadan.</p>"
                       "<p><strong>3xy(4x − 6y)</strong> — toʻliq emas: qavs ichida "
                       "hali 2 umumiy koʻpaytuvchi bor.</p>",
    },
    {
        "text": "<p>Factor completely: 8<i>x</i><sup>3</sup> + 12<i>x</i><sup>2</sup></p>",
        "choices": ["2<i>x</i><sup>2</sup>(4<i>x</i> + 6)", "4<i>x</i>(2<i>x</i><sup>2</sup> + 3<i>x</i>)",
                    "4<i>x</i><sup>2</sup>(2<i>x</i> + 3)", "4<i>x</i><sup>2</sup>(2<i>x</i> + 12)"],
        "correct": "4<i>x</i><sup>2</sup>(2<i>x</i> + 3)",
        "explanation": "<p><strong>4x<sup>2</sup>(2x + 3).</strong> Sonlar 8 va 12 → 4; "
                       "harflar x<sup>3</sup> va x<sup>2</sup> → x<sup>2</sup>.</p>"
                       "<p>Birinchi ikki variant toʻgʻri koʻpaytma beradi, lekin "
                       "<b>toʻliq ajratilmagan</b>.</p>",
    },
    {
        "text": "<p>Factor: 4<i>x</i><sup>2</sup> + 6<i>x</i></p>",
        "choices": ["2(2<i>x</i><sup>2</sup> + 3<i>x</i>)", "2<i>x</i>(2<i>x</i> + 3)",
                    "<i>x</i>(4<i>x</i> + 6)", "4<i>x</i>(<i>x</i> + 2)"],
        "correct": "2<i>x</i>(2<i>x</i> + 3)",
        "explanation": "<p><strong>2x(2x + 3).</strong> EKUB 2, harf x.</p>"
                       "<p><strong>4x(x + 2)</strong> — qavsni ochsangiz "
                       "4x<sup>2</sup> + 8x chiqadi, asl ifoda emas.</p>",
    },
    {
        "text": "<p>Factor: 9<i>x</i><sup>3</sup> − 6<i>x</i><sup>2</sup></p>",
        "choices": ["3<i>x</i><sup>2</sup>(3<i>x</i> − 2)", "3<i>x</i>(3<i>x</i><sup>2</sup> − 2<i>x</i>)",
                    "3<i>x</i><sup>3</sup>(3 − 2)", "<i>x</i><sup>2</sup>(9<i>x</i> − 6)"],
        "correct": "3<i>x</i><sup>2</sup>(3<i>x</i> − 2)",
        "explanation": "<p><strong>3x<sup>2</sup>(3x − 2).</strong> EKUB 3, harfning "
                       "eng kichik darajasi x<sup>2</sup>.</p>"
                       "<p><strong>3x<sup>3</sup>(3 − 2)</strong> — eng katta daraja "
                       "chiqarilgan va ikkinchi hadda x qolmagan.</p>",
    },
    {
        "text": "<p>Factor by grouping: <i>x</i><sup>3</sup> + 3<i>x</i><sup>2</sup> + "
                "2<i>x</i> + 6</p>",
        "choices": ["(<i>x</i> − 3)(<i>x</i><sup>2</sup> + 2)", "(<i>x</i> + 2)(<i>x</i><sup>2</sup> + 3)",
                    "(<i>x</i> + 3)(<i>x</i><sup>2</sup> − 2)", "(<i>x</i> + 3)(<i>x</i><sup>2</sup> + 2)"],
        "correct": "(<i>x</i> + 3)(<i>x</i><sup>2</sup> + 2)",
        "explanation": "<p><strong>(x + 3)(x<sup>2</sup> + 2).</strong> "
                       "x<sup>2</sup>(x + 3) + 2(x + 3).</p>"
                       "<p>Tekshiruv: x = 1 da asl ifoda 12, va (4)(3) = 12 ✓</p>",
    },
    {
        "text": "<p>Factor by grouping: <i>x</i><sup>3</sup> + 4<i>x</i><sup>2</sup> + "
                "3<i>x</i> + 12</p>",
        "choices": ["(<i>x</i> + 3)(<i>x</i><sup>2</sup> + 4)", "(<i>x</i> + 4)(<i>x</i><sup>2</sup> + 3)",
                    "(<i>x</i> − 4)(<i>x</i><sup>2</sup> + 3)", "(<i>x</i> + 4)(<i>x</i><sup>2</sup> − 3)"],
        "correct": "(<i>x</i> + 4)(<i>x</i><sup>2</sup> + 3)",
        "explanation": "<p><strong>(x + 4)(x<sup>2</sup> + 3).</strong> "
                       "x<sup>2</sup>(x + 4) + 3(x + 4).</p>"
                       "<p>Qavs ichidagilar bir xil chiqishi — guruhlash toʻgʻri "
                       "boʻlganining belgisi.</p>",
    },
    {
        "text": "<p>Factor by grouping: 2<i>x</i><sup>3</sup> − 6<i>x</i><sup>2</sup> + "
                "5<i>x</i> − 15</p>",
        "choices": ["(<i>x</i> − 3)(2<i>x</i><sup>2</sup> + 5)", "(<i>x</i> + 3)(2<i>x</i><sup>2</sup> + 5)",
                    "(<i>x</i> − 3)(2<i>x</i><sup>2</sup> − 5)", "(2<i>x</i> − 3)(<i>x</i><sup>2</sup> + 5)"],
        "correct": "(<i>x</i> − 3)(2<i>x</i><sup>2</sup> + 5)",
        "explanation": "<p><strong>(x − 3)(2x<sup>2</sup> + 5).</strong> "
                       "2x<sup>2</sup>(x − 3) + 5(x − 3).</p>"
                       "<p>Tekshiruv: x = 1 da 2 − 6 + 5 − 15 = −14, va (−2)(7) = "
                       "−14 ✓</p>",
    },
    {
        "text": "<p>Which expression is factored <b>completely</b>?</p>",
        "choices": ["2<i>x</i>(3<i>x</i> + 6)", "3(2<i>x</i><sup>2</sup> + 4<i>x</i>)",
                    "6<i>x</i>(<i>x</i> + 2)", "6(<i>x</i><sup>2</sup> + 2<i>x</i>)"],
        "correct": "6<i>x</i>(<i>x</i> + 2)",
        "explanation": "<p><strong>6x(x + 2).</strong> Qavs ichida umumiy koʻpaytuvchi "
                       "qolmagan.</p>"
                       "<p>Qolgan uchtasida qavs ichida hali 2, 2x yoki x bor — "
                       "hammasi bir xil ifodaning yarim ajratilgan koʻrinishi.</p>",
    },
    {
        "text": "<p>What is the greatest common factor of 12 and 18?</p>",
        "choices": ["2", "3", "6", "36"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 12 = 6 × 2 va 18 = 6 × 3.</p>"
                       "<p><strong>36</strong> — eng kichik umumiy karrali (EKUK), "
                       "boshqa tushuncha.</p>",
    },
    {
        "text": "<p>What is the greatest common factor of <i>x</i><sup>3</sup> and "
                "<i>x</i><sup>2</sup>?</p>",
        "choices": ["<i>x</i>", "<i>x</i><sup>2</sup>", "<i>x</i><sup>3</sup>",
                    "<i>x</i><sup>5</sup>"],
        "correct": "<i>x</i><sup>2</sup>",
        "explanation": "<p><strong>x<sup>2</sup>.</strong> Harf uchun <b>eng kichik</b> "
                       "daraja olinadi.</p>"
                       "<p><strong>x<sup>5</sup></strong> — koʻrsatkichlar qoʻshilgan; "
                       "bu koʻpaytmaning javobi boʻlardi.</p>",
    },
    {
        "text": "<p>A rectangle has an area of 2<i>x</i><sup>2</sup> + 6<i>x</i>. Which "
                "pair could be its dimensions?</p>",
        "choices": ["2<i>x</i> and <i>x</i> + 3", "2<i>x</i> and <i>x</i> + 6",
                    "<i>x</i> and 2<i>x</i> + 6<i>x</i>", "2 and <i>x</i><sup>2</sup> + 3<i>x</i>"],
        "correct": "2<i>x</i> and <i>x</i> + 3",
        "explanation": "<p><strong>2x va (x + 3).</strong> Koʻpaytirsak "
                       "2x<sup>2</sup> + 6x ✓</p>"
                       "<p>Ajratish geometriyada «yuzadan tomonlarni topish» "
                       "degani.</p>",
    },
    {
        "text": "<p>What is the quickest way to check a factorisation?</p>",
        "choices": ["Expand the brackets and compare with the original",
                    "Substitute x = 0", "Count the terms", "Divide by the GCF again"],
        "correct": "Expand the brackets and compare with the original",
        "explanation": "<p><strong>Qavsni ochib, asl ifoda bilan solishtirish.</strong> "
                       "Ajratish — koʻpaytirishning teskarisi.</p>"
                       "<p><strong>x = 0</strong> qoʻyish yetarli emas: u koʻpincha "
                       "ikkala tomonni ham 0 qiladi va farqni koʻrsatmaydi.</p>",
    },
    {
        "text": "<p>A student factors 6<i>x</i><sup>3</sup> + 9<i>x</i><sup>2</sup> as "
                "3<i>x</i><sup>3</sup>(2 + 3). What is the mistake?</p>",
        "choices": ["The highest power of x was taken out instead of the lowest",
                    "The GCF of 6 and 9 is not 3",
                    "The signs are wrong",
                    "There is no mistake"],
        "correct": "The highest power of x was taken out instead of the lowest",
        "explanation": "<p><strong>Eng katta daraja chiqarilgan.</strong> "
                       "x<sup>3</sup> ni chiqarsangiz, ikkinchi hadda x qolmaydi.</p>"
                       "<p>Toʻgʻrisi: 3x<sup>2</sup>(2x + 3).</p>",
    },
    {
        "text": "<p>A student factors 5<i>x</i><sup>2</sup> − 15<i>x</i> as "
                "5<i>x</i>(<i>x</i> − 15). What is the mistake?</p>",
        "choices": ["The second term was not divided by the GCF",
                    "The GCF should be 15x", "The sign should be positive",
                    "There is no mistake"],
        "correct": "The second term was not divided by the GCF",
        "explanation": "<p><strong>Ikkinchi had GCF ga boʻlinmagan.</strong> "
                       "15x ÷ 5x = 3, 15 emas.</p>"
                       "<p>Toʻgʻrisi: 5x(x − 3). Qavsni ochib tekshirish bu xatoni "
                       "darhol koʻrsatadi.</p>",
    },
    {
        "text": "<p>Factor completely: 3<i>x</i><sup>3</sup> + 9<i>x</i><sup>2</sup> − "
                "6<i>x</i></p>",
        "choices": ["3(<i>x</i><sup>3</sup> + 3<i>x</i><sup>2</sup> − 2<i>x</i>)",
                    "3<i>x</i>(<i>x</i><sup>2</sup> + 3<i>x</i> − 2)",
                    "<i>x</i>(3<i>x</i><sup>2</sup> + 9<i>x</i> − 6)",
                    "3<i>x</i>(<i>x</i><sup>2</sup> + 3<i>x</i> − 6)"],
        "correct": "3<i>x</i>(<i>x</i><sup>2</sup> + 3<i>x</i> − 2)",
        "explanation": "<p><strong>3x(x<sup>2</sup> + 3x − 2).</strong> EKUB 3, harf "
                       "x.</p>"
                       "<p><strong>3x(x<sup>2</sup> + 3x − 6)</strong> — oxirgi had "
                       "notoʻgʻri boʻlingan: 6x ÷ 3x = 2.</p>",
    },
    {
        "text": "<p>Factor completely: 15<i>x</i><sup>4</sup> − 10<i>x</i><sup>3</sup> + "
                "5<i>x</i><sup>2</sup></p>",
        "choices": ["5<i>x</i><sup>2</sup>(3<i>x</i><sup>2</sup> − 2<i>x</i> + 1)",
                    "5<i>x</i><sup>2</sup>(3<i>x</i><sup>2</sup> − 2<i>x</i>)",
                    "5<i>x</i>(3<i>x</i><sup>3</sup> − 2<i>x</i><sup>2</sup> + <i>x</i>)",
                    "<i>x</i><sup>2</sup>(15<i>x</i><sup>2</sup> − 10<i>x</i> + 5)"],
        "correct": "5<i>x</i><sup>2</sup>(3<i>x</i><sup>2</sup> − 2<i>x</i> + 1)",
        "explanation": "<p><strong>5x<sup>2</sup>(3x<sup>2</sup> − 2x + 1).</strong> "
                       "EKUB 5, eng kichik daraja x<sup>2</sup>.</p>"
                       "<p><strong>5x<sup>2</sup>(3x<sup>2</sup> − 2x)</strong> — "
                       "uchinchi had tushib qolgan: 5x<sup>2</sup> ÷ 5x<sup>2</sup> = "
                       "1, 0 emas.</p>",
    },
    {
        "text": "<p>A rectangular room has an area of 4<i>x</i><sup>2</sup> + 12<i>x</i> "
                "square metres. If its width is 4<i>x</i> metres, what is its length?</p>",
        "choices": ["<i>x</i> + 3", "<i>x</i> + 12", "4<i>x</i> + 3", "<i>x</i><sup>2</sup> + 3"],
        "correct": "<i>x</i> + 3",
        "explanation": "<p><strong>x + 3.</strong> 4x<sup>2</sup> + 12x = 4x(x + 3), "
                       "demak ikkinchi tomon (x + 3).</p>"
                       "<p>Tekshiruv: 4x · (x + 3) = 4x<sup>2</sup> + 12x ✓</p>",
    },
    {
        "text": "<p>A school has 48 boys and 36 girls and wants to line them up in equal "
                "rows, with each row containing only boys or only girls. What is the "
                "largest possible row size?</p>",
        "choices": ["4", "6", "12", "24"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 48 va 36 ning eng katta umumiy "
                       "boʻluvchisi 12 — bu sonlardagi GCF.</p>"
                       "<p>Natijada 4 qator oʻgʻil va 3 qator qiz, jami 7 qator. "
                       "<strong>24</strong> — 36 ni boʻlmaydi.</p>",
    },
]


# =====================================================================
# SAT-30 — difference of squares & perfect square trinomials
# =====================================================================

Q_SAT30 = [
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> − 36</p>",
        "choices": ["(<i>x</i> − 6)(<i>x</i> + 6)", "(<i>x</i> − 6)<sup>2</sup>",
                    "(<i>x</i> − 36)(<i>x</i> + 1)", "(<i>x</i> − 18)(<i>x</i> + 18)"],
        "correct": "(<i>x</i> − 6)(<i>x</i> + 6)",
        "explanation": "<p><strong>(x − 6)(x + 6).</strong> Kvadratlar ayirmasi: "
                       "ildizlari x va 6.</p>"
                       "<p><strong>(x − 6)<sup>2</sup></strong> ochilganda "
                       "x<sup>2</sup> − 12x + 36 beradi — oʻrtada had paydo "
                       "boʻladi.</p>",
    },
    {
        "text": "<p>Factor: 4<i>x</i><sup>2</sup> − 9</p>",
        "choices": ["(2<i>x</i> − 3)(2<i>x</i> + 3)", "(2<i>x</i> − 3)<sup>2</sup>",
                    "(4<i>x</i> − 3)(<i>x</i> + 3)", "(2<i>x</i> − 9)(2<i>x</i> + 1)"],
        "correct": "(2<i>x</i> − 3)(2<i>x</i> + 3)",
        "explanation": "<p><strong>(2x − 3)(2x + 3).</strong> √(4x<sup>2</sup>) = 2x "
                       "va √9 = 3.</p>"
                       "<p>Tekshiruv: qavslarni oching — oʻrtadagi hadlar "
                       "(+6x va −6x) qisqaradi ✓</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> + 8<i>x</i> + 16</p>",
        "choices": ["(<i>x</i> + 4)<sup>2</sup>", "(<i>x</i> − 4)<sup>2</sup>",
                    "(<i>x</i> + 4)(<i>x</i> − 4)", "(<i>x</i> + 8)(<i>x</i> + 2)"],
        "correct": "(<i>x</i> + 4)<sup>2</sup>",
        "explanation": "<p><strong>(x + 4)<sup>2</sup>.</strong> Chetlari x va 4; "
                       "oʻrtasi 2 × 4 = 8 ✓, ishorasi musbat.</p>"
                       "<p><strong>(x + 8)(x + 2)</strong> ochilganda "
                       "x<sup>2</sup> + 10x + 16 beradi — oʻrta had mos "
                       "kelmaydi.</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> − 20<i>x</i> + 100</p>",
        "choices": ["(<i>x</i> − 10)<sup>2</sup>", "(<i>x</i> + 10)<sup>2</sup>",
                    "(<i>x</i> − 10)(<i>x</i> + 10)", "(<i>x</i> − 20)(<i>x</i> + 5)"],
        "correct": "(<i>x</i> − 10)<sup>2</sup>",
        "explanation": "<p><strong>(x − 10)<sup>2</sup>.</strong> Oʻrtasi 2 × 10 = 20 "
                       "✓, ishorasi manfiy.</p>"
                       "<p><strong>(x + 10)<sup>2</sup></strong> — ishora eʼtiborsiz "
                       "qolgan; u +20x berardi.</p>",
    },
    {
        "text": "<p>Factor: 49<i>x</i><sup>2</sup> − 4</p>",
        "choices": ["(7<i>x</i> − 2)(7<i>x</i> + 2)", "(7<i>x</i> − 2)<sup>2</sup>",
                    "(49<i>x</i> − 4)(<i>x</i> + 1)", "(7<i>x</i> − 4)(7<i>x</i> + 1)"],
        "correct": "(7<i>x</i> − 2)(7<i>x</i> + 2)",
        "explanation": "<p><strong>(7x − 2)(7x + 2).</strong> √(49x<sup>2</sup>) = 7x "
                       "va √4 = 2.</p>"
                       "<p><strong>(7x − 2)<sup>2</sup></strong> — ikki shakl "
                       "adashtirilgan: ayirmada qavslar har xil ishorali.</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> − 14<i>x</i> + 49</p>",
        "choices": ["(<i>x</i> − 7)<sup>2</sup>", "(<i>x</i> + 7)<sup>2</sup>",
                    "(<i>x</i> − 7)(<i>x</i> + 7)", "(<i>x</i> − 14)(<i>x</i> + 49)"],
        "correct": "(<i>x</i> − 7)<sup>2</sup>",
        "explanation": "<p><strong>(x − 7)<sup>2</sup>.</strong> Chetlari x va 7; "
                       "oʻrtasi 2 × 7 = 14 ✓, manfiy.</p>"
                       "<p><strong>(x − 7)(x + 7)</strong> ochilganda "
                       "x<sup>2</sup> − 49 beradi: oʻrtadagi had yoʻqoladi.</p>",
    },
    {
        "text": "<p>Factor: 9<i>x</i><sup>2</sup> − 16</p>",
        "choices": ["(3<i>x</i> − 4)(3<i>x</i> + 4)", "(3<i>x</i> − 16)(3<i>x</i> + 16)",
                    "(3<i>x</i> − 4)<sup>2</sup>", "(9<i>x</i> − 4)(<i>x</i> + 4)"],
        "correct": "(3<i>x</i> − 4)(3<i>x</i> + 4)",
        "explanation": "<p><strong>(3x − 4)(3x + 4).</strong> Qavsga sonning oʻzi "
                       "emas, <b>ildizi</b> yoziladi: √16 = 4.</p>"
                       "<p><strong>(3x − 16)(3x + 16)</strong> ochilganda "
                       "9x<sup>2</sup> − 256 beradi.</p>",
    },
    {
        "text": "<p>Which of the following <b>cannot</b> be factored using integers?</p>",
        "choices": ["<i>x</i><sup>2</sup> − 25", "<i>x</i><sup>2</sup> + 25",
                    "<i>x</i><sup>2</sup> − 10<i>x</i> + 25", "<i>x</i><sup>2</sup> + 10<i>x</i> + 25"],
        "correct": "<i>x</i><sup>2</sup> + 25",
        "explanation": "<p><strong>x<sup>2</sup> + 25.</strong> Kvadratlar "
                       "<b>yigʻindisi</b> butun sonlar bilan ajratilmaydi.</p>"
                       "<p>(x + 5)(x + 5) ochilganda x<sup>2</sup> + 10x + 25 beradi — "
                       "bu boshqa ifoda.</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> − 100</p>",
        "choices": ["(<i>x</i> − 10)(<i>x</i> + 10)", "(<i>x</i> − 10)<sup>2</sup>",
                    "(<i>x</i> − 50)(<i>x</i> + 50)", "(<i>x</i> − 100)(<i>x</i> + 1)"],
        "correct": "(<i>x</i> − 10)(<i>x</i> + 10)",
        "explanation": "<p><strong>(x − 10)(x + 10).</strong> √100 = 10.</p>"
                       "<p><strong>(x − 50)(x + 50)</strong> — 100 ni ikkiga boʻlgan "
                       "javob; kerak boʻlgani ildiz.</p>",
    },
    {
        "text": "<p>Factor: 25<i>x</i><sup>2</sup> − 1</p>",
        "choices": ["(5<i>x</i> − 1)(5<i>x</i> + 1)", "(5<i>x</i> − 1)<sup>2</sup>",
                    "(25<i>x</i> − 1)(<i>x</i> + 1)", "5<i>x</i>(5<i>x</i> − 1)"],
        "correct": "(5<i>x</i> − 1)(5<i>x</i> + 1)",
        "explanation": "<p><strong>(5x − 1)(5x + 1).</strong> √(25x<sup>2</sup>) = 5x "
                       "va √1 = 1.</p>"
                       "<p>1 ham toʻliq kvadrat — buni unutish bu savolning asosiy "
                       "tuzogʻi.</p>",
    },
    {
        "text": "<p>Without a calculator, what is 51<sup>2</sup> − 49<sup>2</sup>?</p>",
        "choices": ["2", "100", "200", "2,000"],
        "correct": "200",
        "explanation": "<p><strong>200.</strong> (51 − 49)(51 + 49) = 2 × 100.</p>"
                       "<p>Ikkala kvadratni hisoblash shart emas — tekshirsangiz: "
                       "2,601 − 2,401 = 200 ✓</p>",
    },
    {
        "text": "<p>Without a calculator, what is 103<sup>2</sup> − 97<sup>2</sup>?</p>",
        "choices": ["6", "600", "1,200", "2,400"],
        "correct": "1,200",
        "explanation": "<p><strong>1,200.</strong> (103 − 97)(103 + 97) = 6 × 200.</p>"
                       "<p><strong>600</strong> — koʻpaytmani yarim hisoblagan javob; "
                       "yigʻindi 200, ayirma 6.</p>",
    },
    {
        "text": "<p>Why can <i>x</i><sup>2</sup> + 25 not be factored with integers?</p>",
        "choices": ["Because the sum of two squares has no integer factorisation",
                    "Because 25 is not a perfect square",
                    "Because the middle term is missing",
                    "Because x<sup>2</sup> is already factored"],
        "correct": "Because the sum of two squares has no integer factorisation",
        "explanation": "<p><strong>Kvadratlar yigʻindisi butun sonlar bilan "
                       "ajratilmaydi.</strong> Faqat <b>ayirma</b> ajraladi.</p>"
                       "<p>25 toʻliq kvadrat, va oʻrta hadning yoʻqligi ayirmada "
                       "muammo emas — masalan x<sup>2</sup> − 25 bemalol "
                       "ajraladi.</p>",
    },
    {
        "text": "<p>Factor completely: 2<i>x</i><sup>2</sup> − 18</p>",
        "choices": ["2(<i>x</i> − 3)(<i>x</i> + 3)", "(2<i>x</i> − 3)(<i>x</i> + 6)",
                    "2(<i>x</i><sup>2</sup> − 9)", "(<i>x</i> − 3)(<i>x</i> + 3)"],
        "correct": "2(<i>x</i> − 3)(<i>x</i> + 3)",
        "explanation": "<p><strong>2(x − 3)(x + 3).</strong> Avval GCF (SAT-29): "
                       "2(x<sup>2</sup> − 9), keyin kvadratlar ayirmasi.</p>"
                       "<p><strong>2(x<sup>2</sup> − 9)</strong> — toʻgʻri, lekin "
                       "<b>toʻliq emas</b>: qavs ichi hali ajraladi.</p>",
    },
    {
        "text": "<p>A student factors 49<i>x</i><sup>2</sup> − 4 as "
                "(7<i>x</i> − 2)<sup>2</sup>. What is the mistake?</p>",
        "choices": ["A difference of squares gives two brackets with opposite signs",
                    "The square root of 49 is not 7",
                    "The expression cannot be factored",
                    "There is no mistake"],
        "correct": "A difference of squares gives two brackets with opposite signs",
        "explanation": "<p><strong>Kvadratlar ayirmasida qavslar har xil "
                       "ishorali.</strong> (7x − 2)<sup>2</sup> ochilganda "
                       "49x<sup>2</sup> − 28x + 4 beradi.</p>"
                       "<p>Toʻgʻrisi: (7x − 2)(7x + 2), oʻrtada had yoʻq.</p>",
    },
    {
        "text": "<p>A student factors <i>x</i><sup>2</sup> − 14<i>x</i> + 49 as "
                "(<i>x</i> + 7)<sup>2</sup>. What is the mistake?</p>",
        "choices": ["The sign inside the bracket should match the middle term",
                    "49 is not a perfect square",
                    "The answer should be a difference of squares",
                    "There is no mistake"],
        "correct": "The sign inside the bracket should match the middle term",
        "explanation": "<p><strong>Qavs ichidagi ishora oʻrtadagi hadga mos "
                       "boʻlishi kerak.</strong> Oʻrtada −14x turibdi, demak "
                       "(x − 7)<sup>2</sup>.</p>"
                       "<p>(x + 7)<sup>2</sup> ochilganda +14x berardi.</p>",
    },
    {
        "text": "<p>Factor: <i>x</i><sup>2</sup> + 12<i>x</i> + 36</p>",
        "choices": ["(<i>x</i> + 6)<sup>2</sup>", "(<i>x</i> − 6)<sup>2</sup>",
                    "(<i>x</i> + 6)(<i>x</i> − 6)", "(<i>x</i> + 12)(<i>x</i> + 3)"],
        "correct": "(<i>x</i> + 6)<sup>2</sup>",
        "explanation": "<p><strong>(x + 6)<sup>2</sup>.</strong> Chetlari x va 6; "
                       "oʻrtasi 2 × 6 = 12 ✓</p>"
                       "<p><strong>(x + 12)(x + 3)</strong> ochilganda "
                       "x<sup>2</sup> + 15x + 36 beradi — oʻrta had mos kelmaydi.</p>",
    },
    {
        "text": "<p>Which of the following is a factor of <i>x</i><sup>2</sup> − 49?</p>",
        "choices": ["<i>x</i> − 7", "<i>x</i> − 49", "<i>x</i><sup>2</sup> + 7",
                    "7<i>x</i>"],
        "correct": "<i>x</i> − 7",
        "explanation": "<p><strong>x − 7.</strong> x<sup>2</sup> − 49 = "
                       "(x − 7)(x + 7), demak ikkala qavs ham koʻpaytuvchi.</p>"
                       "<p><strong>x − 49</strong> — 49 ning oʻzi emas, ildizi "
                       "kerak.</p>",
    },
    {
        "text": "<p>Without a calculator, what is 25<sup>2</sup> − 24<sup>2</sup>?</p>",
        "choices": ["1", "49", "50", "625"],
        "correct": "49",
        "explanation": "<p><strong>49.</strong> (25 − 24)(25 + 24) = 1 × 49.</p>"
                       "<p>Ketma-ket ikki sonning kvadratlari ayirmasi har doim "
                       "ularning yigʻindisiga teng — chiroyli qoida.</p>",
    },
    {
        "text": "<p>A square garden of side 30 metres is replaced by a square of side "
                "28 metres. By how many square metres does the area decrease?</p>",
        "choices": ["2", "58", "116", "236"],
        "correct": "116",
        "explanation": "<p><strong>116.</strong> 30<sup>2</sup> − 28<sup>2</sup> = "
                       "(30 − 28)(30 + 28) = 2 × 58 = 116.</p>"
                       "<p><strong>58</strong> — faqat yigʻindi, ayirmaga "
                       "koʻpaytirilmagan; <strong>2</strong> — faqat tomonlar "
                       "ayirmasi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "SAT-26 Practice: Rationalizing Denominators",
        "description": "20 ta SAT uslubidagi savol — maxrajdagi ildizdan qutulish, "
                       "qoʻshma ifoda va natijani soddalashtirish.",
        "tutorial":    "SAT-26:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT26,
    },
    {
        "title":       "SAT-27 Practice: Introduction to Polynomials: Adding and Subtracting",
        "description": "20 ta SAT uslubidagi savol — daraja va bosh koeffitsient, "
                       "qoʻshish, va ayirishda qavs oldidagi minus.",
        "tutorial":    "SAT-27:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT27,
    },
    {
        "title":       "SAT-28 Practice: Multiplying Polynomials (FOIL and beyond)",
        "description": "20 ta SAT uslubidagi savol — FOIL, oʻrtadagi had, kvadratning "
                       "yoyilmasi va bitta koeffitsientni topish.",
        "tutorial":    "SAT-28:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT28,
    },
    {
        "title":       "SAT-29 Practice: Factoring: Greatest Common Factor (GCF) and Grouping",
        "description": "20 ta SAT uslubidagi savol — umumiy koʻpaytuvchi, eng kichik "
                       "daraja, guruhlash va «toʻliq ajratilgan» talabi.",
        "tutorial":    "SAT-29:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT29,
    },
    {
        "title":       "SAT-30 Practice: Factoring: Difference of Squares and Perfect Square Trinomials",
        "description": "20 ta SAT uslubidagi savol — kvadratlar ayirmasi, toʻliq "
                       "kvadrat uchhadi va ogʻzaki hisobdagi qoʻllanishi.",
        "tutorial":    "SAT-30:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT30,
    },
]
