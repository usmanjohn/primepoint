# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-43 va PM-44 (koʻphadlar, qisqa koʻpaytirish).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan. BLOK C YAKUNI.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq. Darajalar «x^2» koʻrinishida
   yoziladi, savol matnida esa <sup> ishlatiladi.
⚠️ Kumulyativ: kvadrat tenglama yechish yoʻq (Blok D); uchhadni umumiy
   usulda ajratish ham yoʻq — faqat toʻliq kvadrat va kvadratlar ayirmasi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_43_44.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Matematika",
    "description": "Matematika — Prime Math darslarining mashqlari",
    "icon":        "bi-calculator",
    "color":       "#f59e0b",
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
# PM-43 — koʻphadlar
# =====================================================================

Q_PM43 = [
    # 1–5 tanish
    {
        "text": "<p>Ixchamlang.</p><p><strong>(2x<sup>2</sup> + 3x) + "
                "(x<sup>2</sup> − x) = ?</strong></p>",
        "choices": ["3x^2 + 2x", "3x^2 + 4x", "2x^2 + 2x", "3x^3 + 2x"],
        "correct": "3x^2 + 2x",
        "explanation": "<p><strong>3x^2 + 2x.</strong> x^2 li hadlar: 2 + 1 = 3; "
                       "x li hadlar: 3 − 1 = 2. Daraja qoʻshishda "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3x<sup>2</sup> + 2x − 5 "
                "koʻphadining darajasi nechchi?</strong></p>",
        "choices": ["1", "2", "3", "5"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Daraja — eng katta koʻrsatkich. Bu "
                       "yerda u x^2 dagi ikkilik. <strong>3</strong> — hadlar "
                       "soni, daraja emas.</p>",
    },
    {
        "text": "<p>Qavsni oching.</p><p><strong>2x(3x + 4) = ?</strong></p>",
        "choices": ["6x^2 + 8x", "6x + 8x", "5x^2 + 8x", "6x^2 + 8"],
        "correct": "6x^2 + 8x",
        "explanation": "<p><strong>6x^2 + 8x.</strong> 2x · 3x = 6x^2 (sonlar "
                       "koʻpaytiriladi, koʻrsatkichlar qoʻshiladi) va "
                       "2x · 4 = 8x.</p>",
    },
    {
        "text": "<p>Koʻpaytiring.</p><p><strong>(x + 2)(x + 3) = ?</strong></p>",
        "choices": ["x^2 + 6", "x^2 + 5x + 6", "x^2 + 6x + 5", "2x + 5"],
        "correct": "x^2 + 5x + 6",
        "explanation": "<p><strong>x^2 + 5x + 6.</strong> Toʻrtta koʻpaytma: x^2, "
                       "3x, 2x, 6; oʻrtadagilar yigʻiladi. <strong>x^2 + 6</strong> "
                       "— oʻrtadagi ikki had tushib qolgan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3x · 2x = ?</strong></p>",
        "choices": ["5x", "6x", "5x^2", "6x^2"],
        "correct": "6x^2",
        "explanation": "<p><strong>6x^2.</strong> 3 × 2 = 6, x · x = x^2. "
                       "<strong>6x</strong> — darajani unutgan javob.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Ixchamlang.</p><p><strong>(3x<sup>2</sup> + 2x − 5) + "
                "(x<sup>2</sup> − 4x + 7) = ?</strong></p>",
        "choices": ["4x^2 − 2x + 2", "4x^2 + 6x + 2", "4x^2 − 2x + 12",
                    "2x^2 − 2x + 2"],
        "correct": "4x^2 − 2x + 2",
        "explanation": "<p><strong>4x^2 − 2x + 2.</strong> Har guruh alohida: "
                       "3 + 1 = 4; 2 − 4 = −2; −5 + 7 = 2. Tekshirish x = 2 da: "
                       "11 + 3 = 14 va 16 − 4 + 2 = 14 ✓</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>(5x<sup>2</sup> − 3x + 4) − "
                "(2x<sup>2</sup> + x − 6) = ?</strong></p>",
        "choices": ["3x^2 − 4x + 10", "3x^2 − 2x − 2", "3x^2 − 4x − 2",
                    "7x^2 − 2x − 2"],
        "correct": "3x^2 − 4x + 10",
        "explanation": "<p><strong>3x^2 − 4x + 10.</strong> Minus ikkinchi qavsdagi "
                       "UCHALA ishorani almashtiradi: −2x^2, −x, +6. Tekshirish "
                       "x = 2 da: 18 − 4 = 14 va 12 − 8 + 10 = 14 ✓</p>",
    },
    {
        "text": "<p>Qavsni oching.</p><p><strong>3x(2x − 5) = ?</strong></p>",
        "choices": ["6x^2 − 15x", "6x^2 − 5x", "6x − 15x", "5x^2 − 15x"],
        "correct": "6x^2 − 15x",
        "explanation": "<p><strong>6x^2 − 15x.</strong> 3x ikkala hadga ham "
                       "koʻpaytiriladi; ikkinchisining ishorasi saqlanadi.</p>",
    },
    {
        "text": "<p>Koʻpaytiring.</p><p><strong>(x + 4)(x + 2) = ?</strong></p>",
        "choices": ["x^2 + 8", "x^2 + 6x + 8", "x^2 + 8x + 6", "x^2 + 6x + 6"],
        "correct": "x^2 + 6x + 8",
        "explanation": "<p><strong>x^2 + 6x + 8.</strong> Oʻrta had 2x + 4x = 6x, "
                       "oxirgisi 4 × 2 = 8.</p>",
    },
    {
        "text": "<p>Koʻpaytiring.</p><p><strong>(2x − 1)(x + 4) = ?</strong></p>",
        "choices": ["2x^2 + 7x − 4", "2x^2 + 9x − 4", "2x^2 − 7x − 4",
                    "2x^2 + 7x + 4"],
        "correct": "2x^2 + 7x − 4",
        "explanation": "<p><strong>2x^2 + 7x − 4.</strong> 2x·x = 2x^2; "
                       "2x·4 = 8x; −1·x = −x; −1·4 = −4. Oʻrta had 8x − x = 7x. "
                       "Tekshirish x = 2 da: 3 × 6 = 18 va 8 + 14 − 4 = 18 ✓</p>",
    },
    {
        "text": "<p>Koʻpaytiring.</p><p><strong>(x − 3)(x + 6) = ?</strong></p>",
        "choices": ["x^2 + 3x − 18", "x^2 − 3x − 18", "x^2 + 9x − 18",
                    "x^2 + 3x + 18"],
        "correct": "x^2 + 3x − 18",
        "explanation": "<p><strong>x^2 + 3x − 18.</strong> Oʻrta had "
                       "6x − 3x = 3x; oxirgisi (−3) × 6 = −18.</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>(x<sup>2</sup> + 5) − "
                "(3x<sup>2</sup> − 2) = ?</strong></p>",
        "choices": ["−2x^2 + 7", "−2x^2 + 3", "4x^2 + 3", "−2x^2 − 7"],
        "correct": "−2x^2 + 7",
        "explanation": "<p><strong>−2x^2 + 7.</strong> 1 − 3 = −2; ozod hadlar: "
                       "5 − (−2) = 5 + 2 = 7. Ikkinchi qavsdagi minus musbatga "
                       "aylandi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>x = 1.</p><p><strong>(x + 2)"
                "(x + 3) va x<sup>2</sup> + 6 qiymatlari qanday?</strong></p>",
        "choices": ["12 va 7", "7 va 12", "Ikkalasi ham 12", "Ikkalasi ham 7"],
        "correct": "12 va 7",
        "explanation": "<p><strong>12 va 7.</strong> 3 × 4 = 12; 1 + 6 = 7. Demak "
                       "x^2 + 6 notoʻgʻri javob: oʻrtadagi 5x hadi tushib "
                       "qolgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>(3x<sup>2</sup> − x) − "
                "(x<sup>2</sup> − x) nechaga teng?</strong></p>",
        "choices": ["2x^2", "2x^2 − 2x", "4x^2", "2x^2 + 2x"],
        "correct": "2x^2",
        "explanation": "<p><strong>2x^2.</strong> x li hadlar: −x − (−x) = "
                       "−x + x = 0 — ular butunlay qisqarib ketdi. Qolgani "
                       "3x^2 − x^2 = 2x^2.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi ifoda ikki "
                "had?</strong></p>",
        "choices": ["5x", "x^2 + 3", "3x^2 + 2x − 5", "7"],
        "correct": "x^2 + 3",
        "explanation": "<p><strong>x^2 + 3.</strong> Ikkita had bor. 5x va 7 — bir "
                       "had, 3x^2 + 2x − 5 esa uch had.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>(x + 2)(x + 3) "
                "koʻpaytmasida nechta koʻpaytma hosil boʻladi?</strong></p>",
        "choices": ["Ikkita", "Uchta", "Toʻrtta", "Beshta"],
        "correct": "Toʻrtta",
        "explanation": "<p><strong>Toʻrtta:</strong> x·x, x·3, 2·x, 2·3. Ulardan "
                       "ikkitasi oʻxshash boʻlgani uchun javobda uchta had "
                       "qoladi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>(5x<sup>2</sup> − 3x) − "
                "(2x<sup>2</sup> + x) = 5x<sup>2</sup> − 3x − 2x<sup>2</sup> + x"
                "</strong></p>",
        "choices": [
            "Ikkinchi hadning ishorasi ham almashishi kerak: −x",
            "Birinchi qavsni ham ochish kerak edi",
            "x^2 lar qoʻshilishi kerak edi",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Ikkinchi hadning ishorasi ham almashishi kerak: −x",
        "explanation": "<p><strong>−x boʻlishi kerak.</strong> Qavs oldidagi minus "
                       "ichkaridagi HAMMA hadga tegishli. Tekshirish x = 1 da: "
                       "asl ifoda 2 − 3 = −1, notoʻgʻri yozuvda esa 1.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>(x + 5)(x + 1)</strong></p>",
        "choices": ["x^2 + 5", "x^2 + 5x + 1", "x^2 + 6x + 5", "x^2 + 6x + 6"],
        "correct": "x^2 + 6x + 5",
        "explanation": "<p><strong>x^2 + 6x + 5.</strong> Oʻrta had x + 5x = 6x; "
                       "oxirgisi 5 × 1 = 5. Tekshirish x = 1 da: 6 × 2 = 12 va "
                       "1 + 6 + 5 = 12 ✓</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Bogʻning eni x metr, boʻyi enidan 5 metr uzun. Eni tomonga yana "
                "3 metr qoʻshildi.</p><p><strong>Yangi yuza qanday "
                "yoziladi?</strong></p>",
        "choices": ["x^2 + 8x + 15", "x^2 + 15", "x^2 + 8x", "x^2 + 5x + 3"],
        "correct": "x^2 + 8x + 15",
        "explanation": "<p><strong>x^2 + 8x + 15.</strong> Yangi eni x + 3, boʻyi "
                       "x + 5: (x + 3)(x + 5) = x^2 + 5x + 3x + 15. x = 10 boʻlsa "
                       "195 m² — va 13 × 15 ham 195 ✓</p>",
    },
    {
        "text": "<p>Xonaning eni x metr, boʻyi undan 2 metr uzun. Gilam uchun har "
                "tomondan 1 metrdan boʻsh joy qoldirildi.</p><p><strong>x = 5 "
                "boʻlsa, gilamning yuzasi qancha?</strong></p>",
        "choices": ["9 m²", "15 m²", "21 m²", "35 m²"],
        "correct": "15 m²",
        "explanation": "<p><strong>15 m².</strong> Gilamning eni x − 2 = 3, boʻyi "
                       "(x + 2) − 2 = 5; yuza (x − 2)·x = x^2 − 2x = 15. "
                       "Tekshirish: 3 × 5 = 15 ✓ <strong>35</strong> — butun "
                       "xonaning yuzasi.</p>",
    },
]


# =====================================================================
# PM-44 — qisqa koʻpaytirish formulalari
# =====================================================================

Q_PM44 = [
    # 1–5 tanish
    {
        "text": "<p>Formula bilan yozing.</p><p><strong>(x + 2)<sup>2</sup> = ?"
                "</strong></p>",
        "choices": ["x^2 + 4", "x^2 + 2x + 4", "x^2 + 4x + 4", "x^2 + 4x + 2"],
        "correct": "x^2 + 4x + 4",
        "explanation": "<p><strong>x^2 + 4x + 4.</strong> Oʻrta had "
                       "2 × x × 2 = 4x. <strong>x^2 + 4</strong> — eng mashhur "
                       "xato: oʻrta had tushib qolgan.</p>",
    },
    {
        "text": "<p>Formula bilan yozing.</p><p><strong>(x − 6)<sup>2</sup> = ?"
                "</strong></p>",
        "choices": ["x^2 − 36", "x^2 − 12x + 36", "x^2 − 12x − 36",
                    "x^2 + 12x + 36"],
        "correct": "x^2 − 12x + 36",
        "explanation": "<p><strong>x^2 − 12x + 36.</strong> Oxirgi had MUSBAT: "
                       "(−6) × (−6) = +36. Minus faqat oʻrta hadda qoladi.</p>",
    },
    {
        "text": "<p>Formula bilan yozing.</p><p><strong>(x − 7)(x + 7) = ?</strong></p>",
        "choices": ["x^2 − 49", "x^2 + 49", "x^2 − 14x − 49", "x^2 − 14x + 49"],
        "correct": "x^2 − 49",
        "explanation": "<p><strong>x^2 − 49.</strong> Kvadratlar ayirmasi: oʻrta "
                       "hadlar (+7x va −7x) bir-birini yoʻq qiladi.</p>",
    },
    {
        "text": "<p>Koʻpaytuvchilarga ajrating.</p><p><strong>x<sup>2</sup> − 16 = ?"
                "</strong></p>",
        "choices": ["(x − 4)(x + 4)", "(x − 4)^2", "(x + 4)^2", "(x − 8)(x + 8)"],
        "correct": "(x − 4)(x + 4)",
        "explanation": "<p><strong>(x − 4)(x + 4).</strong> 16 = 4^2 va orada "
                       "minus — demak kvadratlar ayirmasi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>(a + b)<sup>2</sup> "
                "nechaga teng?</strong></p>",
        "choices": ["a^2 + b^2", "a^2 + ab + b^2", "a^2 + 2ab + b^2", "2a + 2b"],
        "correct": "a^2 + 2ab + b^2",
        "explanation": "<p><strong>a^2 + 2ab + b^2.</strong> Sonlar bilan "
                       "tekshiring: (3 + 4)^2 = 49, lekin 9 + 16 = 25. Farq 24 — "
                       "bu aynan 2 × 3 × 4.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Formula bilan yozing.</p><p><strong>(x + 3)<sup>2</sup> = ?"
                "</strong></p>",
        "choices": ["x^2 + 9", "x^2 + 3x + 9", "x^2 + 6x + 9", "x^2 + 6x + 3"],
        "correct": "x^2 + 6x + 9",
        "explanation": "<p><strong>x^2 + 6x + 9.</strong> Oʻrta had "
                       "2 × x × 3 = 6x.</p>",
    },
    {
        "text": "<p>Formula bilan yozing.</p><p><strong>(2x + 1)<sup>2</sup> = ?"
                "</strong></p>",
        "choices": ["4x^2 + 1", "4x^2 + 2x + 1", "4x^2 + 4x + 1", "2x^2 + 4x + 1"],
        "correct": "4x^2 + 4x + 1",
        "explanation": "<p><strong>4x^2 + 4x + 1.</strong> Birinchi had "
                       "(2x)^2 = 4x^2; oʻrta had 2 × 2x × 1 = 4x.</p>",
    },
    {
        "text": "<p>Koʻpaytuvchilarga ajrating.</p><p><strong>x<sup>2</sup> + 6x + 9 "
                "= ?</strong></p>",
        "choices": ["(x + 3)^2", "(x − 3)^2", "(x + 3)(x − 3)", "(x + 9)^2"],
        "correct": "(x + 3)^2",
        "explanation": "<p><strong>(x + 3)^2.</strong> Chetdagilar kvadrat "
                       "(x^2 va 9 = 3^2), oʻrta had esa 2 × x × 3 = 6x — toʻliq "
                       "kvadrat.</p>",
    },
    {
        "text": "<p>Koʻpaytuvchilarga ajrating.</p><p><strong>x<sup>2</sup> − 25 = ?"
                "</strong></p>",
        "choices": ["(x − 5)(x + 5)", "(x − 5)^2", "(x + 5)^2", "x(x − 25)"],
        "correct": "(x − 5)(x + 5)",
        "explanation": "<p><strong>(x − 5)(x + 5).</strong> 25 = 5^2, orada "
                       "minus.</p>",
    },
    {
        "text": "<p>Koʻpaytuvchilarga ajrating.</p><p><strong>4x<sup>2</sup> − 1 = ?"
                "</strong></p>",
        "choices": ["(2x − 1)(2x + 1)", "(4x − 1)(4x + 1)", "(2x − 1)^2",
                    "2x(2x − 1)"],
        "correct": "(2x − 1)(2x + 1)",
        "explanation": "<p><strong>(2x − 1)(2x + 1).</strong> 4x^2 = (2x)^2 va "
                       "1 = 1^2 — ikkalasi ham kvadrat, orada minus.</p>",
    },
    {
        "text": "<p>Ogʻzaki hisoblang.</p><p><strong>102<sup>2</sup> = ?</strong></p>",
        "choices": ["10 004", "10 204", "10 404", "10 440"],
        "correct": "10 404",
        "explanation": "<p><strong>10 404.</strong> (100 + 2)^2 = 10 000 + 400 + 4. "
                       "<strong>10 004</strong> — oʻrta hadni unutgan javob.</p>",
    },
    {
        "text": "<p>Ogʻzaki hisoblang.</p><p><strong>51 × 49 = ?</strong></p>",
        "choices": ["2401", "2499", "2500", "2501"],
        "correct": "2499",
        "explanation": "<p><strong>2499.</strong> (50 + 1)(50 − 1) = 2500 − 1. "
                       "Ikki son ellikdan teng uzoqlikda — kvadratlar ayirmasi "
                       "aynan shu holat uchun.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>a = 3, b = 4.</p>"
                "<p><strong>(a + b)<sup>2</sup> va a<sup>2</sup> + b<sup>2</sup> "
                "qiymatlari qanday?</strong></p>",
        "choices": ["25 va 49", "49 va 25", "Ikkalasi ham 49", "Ikkalasi ham 25"],
        "correct": "49 va 25",
        "explanation": "<p><strong>49 va 25.</strong> (3 + 4)^2 = 7^2 = 49; "
                       "9 + 16 = 25. Ular teng emas — farq 24, yaʼni 2ab. Shuning "
                       "uchun oʻrta hadni hech qachon unutmang.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi ifodani "
                "koʻpaytuvchilarga ajratib boʻlmaydi?</strong></p>",
        "choices": ["x^2 − 9", "x^2 + 9", "x^2 − 1", "4x^2 − 25"],
        "correct": "x^2 + 9",
        "explanation": "<p><strong>x^2 + 9.</strong> Kvadratlar AYIRMASI ajraladi, "
                       "yigʻindisi esa oddiy yoʻl bilan ajralmaydi. Qolgan uchtasida "
                       "minus bor.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>(x − 4)<sup>2</sup> ning "
                "oxirgi hadi qanday?</strong></p>",
        "choices": ["−16", "+16", "−8", "+8"],
        "correct": "+16",
        "explanation": "<p><strong>+16.</strong> (−4) × (−4) = +16 — ikki "
                       "manfiyning koʻpaytmasi musbat. Manfiy faqat oʻrta hadda "
                       "(−8x) qoladi.</p>",
    },
    {
        "text": "<p>Ogʻzaki hisoblang.</p><p><strong>98<sup>2</sup> = ?</strong></p>",
        "choices": ["9404", "9604", "9996", "10 004"],
        "correct": "9604",
        "explanation": "<p><strong>9604.</strong> (100 − 2)^2 = "
                       "10 000 − 400 + 4 = 9604. Oʻrta had manfiy, oxirgisi "
                       "musbat.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>(x + 5)<sup>2</sup> = "
                "x<sup>2</sup> + 25</strong></p>",
        "choices": [
            "Oʻrta had 10x tushib qolgan: x^2 + 10x + 25",
            "Oxirgi had −25 boʻlishi kerak",
            "Birinchi had 2x boʻlishi kerak",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Oʻrta had 10x tushib qolgan: x^2 + 10x + 25",
        "explanation": "<p><strong>x^2 + 10x + 25.</strong> Tekshirish x = 1 da: "
                       "chapda 36, notoʻgʻri javobda esa 26. Farq 10 — bu aynan "
                       "tushib qolgan oʻrta had.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>(x − 3)<sup>2</sup></strong></p>",
        "choices": ["x^2 − 9", "x^2 − 6x − 9", "x^2 − 6x + 9", "x^2 + 6x + 9"],
        "correct": "x^2 − 6x + 9",
        "explanation": "<p><strong>x^2 − 6x + 9.</strong> <strong>x^2 − 9</strong> "
                       "— bu (x − 3)(x + 3) ning javobi, kvadratniki emas. Ikki "
                       "formulani adashtirmang.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Tomoni a metr boʻlgan kvadrat maydon bir tomondan 3 metrga "
                "uzaytirilib, ikkinchi tomondan 3 metrga qisqartirildi.</p>"
                "<p><strong>Yangi yuza eskisidan qanday farq qiladi?</strong></p>",
        "choices": [
            "9 m² ga katta",
            "9 m² ga kichik",
            "Teng qoladi",
            "6 m² ga kichik",
        ],
        "correct": "9 m² ga kichik",
        "explanation": "<p><strong>9 m² ga kichik.</strong> Yangi yuza "
                       "(a + 3)(a − 3) = a^2 − 9. Yoʻqotish a ga bogʻliq emas: "
                       "a = 20 da 400 va 391; a = 50 da 2500 va 2491 — har doim "
                       "9 m².</p>",
    },
    {
        "text": "<p>Usta 103 ta gʻishtni 97 qatorga terdi.</p><p><strong>Jami "
                "nechta gʻisht boʻldi?</strong></p>",
        "choices": ["9991", "9997", "10 000", "10 009"],
        "correct": "9991",
        "explanation": "<p><strong>9991.</strong> (100 + 3)(100 − 3) = "
                       "10 000 − 9 = 9991. Ikki son yuzdan teng uzoqlikda "
                       "boʻlgani uchun kvadratlar ayirmasi ishlaydi — ustunda "
                       "koʻpaytirish shart emas.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-43 Mashq: Koʻphadlar",
        "description": "20 savol — koʻphadlarni qoʻshish va ayirish, bir hadga "
                       "koʻpaytirish va ikki qavsni koʻpaytirish.",
        "tutorial":    "PM-43:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM43,
    },
    {
        "title":       "PM-44 Mashq: Qisqa koʻpaytirish formulalari",
        "description": "20 savol — uchta formula, ular bilan ogʻzaki hisoblash va "
                       "koʻpaytuvchilarga ajratish.",
        "tutorial":    "PM-44:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM44,
    },
]
