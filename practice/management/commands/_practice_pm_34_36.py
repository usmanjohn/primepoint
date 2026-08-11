# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-34 … PM-36 (qavsdan chiqarish, formula, tenglama).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq. Daraja «b·b» koʻrinishida yoziladi.
⚠️ Kumulyativ: PM-36 da nomaʼlum faqat BIR tomonda (ikki tomonli tenglamalar
   PM-37 da); matnli masalani tenglama bilan yechishning toʻliq usuli PM-38 da.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_34_36.py --master=prime \\
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
# PM-34 — umumiy koʻpaytuvchini qavsdan chiqarish
# =====================================================================

Q_PM34 = [
    # 1–5 tanish
    {
        "text": "<p>Umumiy koʻpaytuvchini qavsdan chiqaring.</p>"
                "<p><strong>2x + 6 = ?</strong></p>",
        "choices": ["2(x + 3)", "2(x + 6)", "2(x + 4)", "6(x + 2)"],
        "correct": "2(x + 3)",
        "explanation": "<p><strong>2(x + 3).</strong> Ikkala had ham 2 ga "
                       "boʻlinadi: 2x ÷ 2 = x va 6 ÷ 2 = 3. Tekshirish: qavsni "
                       "ochsak 2x + 6 qaytadi ✓</p>",
    },
    {
        "text": "<p>Umumiy koʻpaytuvchini qavsdan chiqaring.</p>"
                "<p><strong>3a + 9 = ?</strong></p>",
        "choices": ["3(a + 3)", "3(a + 9)", "9(a + 1)", "3(a + 6)"],
        "correct": "3(a + 3)",
        "explanation": "<p><strong>3(a + 3).</strong> 9 ÷ 3 = 3. "
                       "<strong>3(a + 9)</strong> ochilsa 3a + 27 chiqadi — "
                       "boshlangʻich ifoda emas.</p>",
    },
    {
        "text": "<p>Umumiy koʻpaytuvchini qavsdan chiqaring.</p>"
                "<p><strong>5m − 10 = ?</strong></p>",
        "choices": ["5(m − 2)", "5(m − 10)", "5(m − 5)", "10(m − 5)"],
        "correct": "5(m − 2)",
        "explanation": "<p><strong>5(m − 2).</strong> 10 ÷ 5 = 2, ishora "
                       "saqlanadi.</p>",
    },
    {
        "text": "<p>Umumiy koʻpaytuvchini qavsdan chiqaring.</p>"
                "<p><strong>4x + 4 = ?</strong></p>",
        "choices": ["4(x + 1)", "4x", "4(x + 4)", "8x"],
        "correct": "4(x + 1)",
        "explanation": "<p><strong>4(x + 1).</strong> 4 ÷ 4 = 1 — qavs ichida 1 "
                       "qoladi, u yoʻqolmaydi. <strong>4x</strong> ikkinchi hadni "
                       "butunlay tashlab yuborgan javob.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>6x + 9 ifodasining umumiy "
                "koʻpaytuvchisi qaysi?</strong></p>",
        "choices": ["2", "3", "6", "9"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> 6 va 9 ning eng katta umumiy "
                       "boʻluvchisi — EKUB(6, 9) = 3 (PM-8). "
                       "<strong>6</strong> ga 9 boʻlinmaydi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Umumiy koʻpaytuvchini qavsdan chiqaring.</p>"
                "<p><strong>6x + 9 = ?</strong></p>",
        "choices": ["3(2x + 3)", "3(2x + 9)", "6(x + 3)", "9(x + 1)"],
        "correct": "3(2x + 3)",
        "explanation": "<p><strong>3(2x + 3).</strong> 6 ÷ 3 = 2 va 9 ÷ 3 = 3. "
                       "Tekshirish: 3 × 2x = 6x va 3 × 3 = 9 ✓</p>",
    },
    {
        "text": "<p>Umumiy koʻpaytuvchini qavsdan chiqaring.</p>"
                "<p><strong>10a − 15 = ?</strong></p>",
        "choices": ["5(2a − 3)", "5(2a − 15)", "5(a − 3)", "10(a − 5)"],
        "correct": "5(2a − 3)",
        "explanation": "<p><strong>5(2a − 3).</strong> EKUB(10, 15) = 5; "
                       "10 ÷ 5 = 2 va 15 ÷ 5 = 3.</p>",
    },
    {
        "text": "<p>Umumiy koʻpaytuvchini qavsdan chiqaring.</p>"
                "<p><strong>8m + 12n = ?</strong></p>",
        "choices": ["2(4m + 6n)", "4(2m + 3n)", "4(2m + 12n)", "8(m + 4n)"],
        "correct": "4(2m + 3n)",
        "explanation": "<p><strong>4(2m + 3n).</strong> EKUB(8, 12) = 4. "
                       "<strong>2(4m + 6n)</strong> ham teng, lekin ish yarim "
                       "qolgan: qavs ichidagi 4 va 6 hali 2 ga boʻlinadi.</p>",
    },
    {
        "text": "<p>Umumiy koʻpaytuvchini qavsdan chiqaring.</p>"
                "<p><strong>2a + ab = ?</strong></p>",
        "choices": ["a(2 + b)", "2(a + b)", "ab(2 + 1)", "a(2 + ab)"],
        "correct": "a(2 + b)",
        "explanation": "<p><strong>a(2 + b).</strong> Umumiy koʻpaytuvchi son emas, "
                       "harf: ikkala hadda ham a bor. Tekshirish: a × 2 = 2a va "
                       "a × b = ab ✓</p>",
    },
    {
        "text": "<p>Umumiy koʻpaytuvchini qavsdan chiqaring.</p>"
                "<p><strong>14x − 21 = ?</strong></p>",
        "choices": ["7(2x − 3)", "7(2x − 21)", "3(4x − 7)", "7(x − 3)"],
        "correct": "7(2x − 3)",
        "explanation": "<p><strong>7(2x − 3).</strong> EKUB(14, 21) = 7; "
                       "14 ÷ 7 = 2 va 21 ÷ 7 = 3.</p>",
    },
    {
        "text": "<p>Umumiy koʻpaytuvchini qavsdan chiqaring.</p>"
                "<p><strong>12 + 18y = ?</strong></p>",
        "choices": ["3(4 + 6y)", "6(2 + 3y)", "6(2 + 18y)", "2(6 + 9y)"],
        "correct": "6(2 + 3y)",
        "explanation": "<p><strong>6(2 + 3y).</strong> EKUB(12, 18) = 6. Qolgan "
                       "variantlar ham teng, lekin toʻliq chiqarilmagan — qavs "
                       "ichida umumiy boʻluvchi qolib ketgan.</p>",
    },
    {
        "text": "<p>Umumiy koʻpaytuvchini qavsdan chiqaring.</p>"
                "<p><strong>5x + x·x = ?</strong></p>",
        "choices": ["x(5 + x)", "5x(1 + x)", "x(5 + 1)", "5(x + x)"],
        "correct": "x(5 + x)",
        "explanation": "<p><strong>x(5 + x).</strong> x·x — bu x ning kvadrati, "
                       "demak unda ham bitta x bor. Tekshirish: x × 5 = 5x va "
                       "x × x ✓</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi ifoda 4x + 12 ga "
                "TENG?</strong></p>",
        "choices": ["4(x + 12)", "4(x + 3)", "12(x + 4)", "4x(1 + 3)"],
        "correct": "4(x + 3)",
        "explanation": "<p><strong>4(x + 3).</strong> Har bir variantni ochib "
                       "koʻring: 4(x + 12) = 4x + 48, 12(x + 4) = 12x + 48. Faqat "
                       "bittasi boshlangʻich ifodani qaytaradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi javobda umumiy "
                "koʻpaytuvchi TOʻLIQ chiqarilgan?</strong></p>",
        "choices": ["2(3x + 6)", "3(2x + 4)", "6(x + 2)", "2(3x + 12)"],
        "correct": "6(x + 2)",
        "explanation": "<p><strong>6(x + 2).</strong> Uchala ifoda ham 6x + 12 ga "
                       "teng, lekin faqat oxirgisida qavs ichida umumiy boʻluvchi "
                       "qolmagan: 1 va 2 ning umumiy boʻluvchisi yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qavsdan chiqarish qaysi "
                "amalning teskarisi?</strong></p>",
        "choices": [
            "Qavs ochishning",
            "Oʻxshash hadlarni ixchamlashning",
            "Oʻrniga qoʻyishning",
            "Qisqartirishning",
        ],
        "correct": "Qavs ochishning",
        "explanation": "<p><strong>Qavs ochishning.</strong> a(b + c) = ab + ac "
                       "ochish edi; ab + ac = a(b + c) esa uning teskarisi. "
                       "Shuning uchun chiqarishni tekshirish uchun qavsni ochamiz.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>8 × 47 + 8 × 53 = ?</strong></p>",
        "choices": ["100", "376", "800", "8000"],
        "correct": "800",
        "explanation": "<p><strong>800.</strong> Umumiy koʻpaytuvchini chiqaramiz: "
                       "8(47 + 53) = 8 × 100 = 800. Qavs ichi yumaloq songa "
                       "aylandi — kalkulyator kerak boʻlmadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>5x + 10 = 5(x + 10)</strong></p>",
        "choices": [
            "Ikkinchi had ham 5 ga boʻlinishi kerak: 5(x + 2)",
            "Umumiy koʻpaytuvchi 10 boʻlishi kerak",
            "Bu ifodadan koʻpaytuvchi chiqarib boʻlmaydi",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Ikkinchi had ham 5 ga boʻlinishi kerak: 5(x + 2)",
        "explanation": "<p><strong>5(x + 2).</strong> 10 ÷ 5 = 2. Tekshirish: "
                       "5(x + 10) ochilsa 5x + 50 chiqadi — boshlangʻich ifodadan "
                       "boshqa.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻliq?</p><p><strong>9a + 6b</strong></p>",
        "choices": ["3(3a + 2b)", "3(9a + 6b)", "9(a + 6b)", "3(3a + 6b)"],
        "correct": "3(3a + 2b)",
        "explanation": "<p><strong>3(3a + 2b).</strong> EKUB(9, 6) = 3; 9 ÷ 3 = 3 "
                       "va 6 ÷ 3 = 2. Tekshirish: 3 × 3a = 9a va 3 × 2b = 6b ✓</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>25 nafar oʻquvchi sovgʻa uchun pul yigʻdi: har biri gulga 12 000 "
                "soʻmdan va kitobga 8000 soʻmdan qoʻshdi.</p>"
                "<p><strong>Jami qancha pul yigʻildi?</strong></p>",
        "choices": ["200 000 soʻm", "300 000 soʻm", "500 000 soʻm", "800 000 soʻm"],
        "correct": "500 000 soʻm",
        "explanation": "<p><strong>500 000 soʻm.</strong> 25a + 25b = 25(a + b); "
                       "a + b = 20 000, demak 25 × 20 000 = 500 000. Uzun yoʻl ham "
                       "shu javobni beradi: 300 000 + 200 000.</p>",
    },
    {
        "text": "<p>Bir kishilik chipta 45 000 soʻm. Ertalab 6 ta, kechqurun 4 ta "
                "chipta sotildi.</p><p><strong>Kunlik tushum qancha?</strong></p>",
        "choices": ["270 000 soʻm", "180 000 soʻm", "450 000 soʻm", "900 000 soʻm"],
        "correct": "450 000 soʻm",
        "explanation": "<p><strong>450 000 soʻm.</strong> 45 000 × 6 + 45 000 × 4 = "
                       "45 000(6 + 4) = 45 000 × 10 = 450 000. Umumiy "
                       "koʻpaytuvchini chiqarish hisobni bir zumda tugatdi.</p>",
    },
]


# =====================================================================
# PM-35 — formula bilan ishlash
# =====================================================================

Q_PM35 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>S = v · t; v = 60 km/soat, "
                "t = 2 soat</strong></p>",
        "choices": ["30 km", "62 km", "120 km", "3600 km"],
        "correct": "120 km",
        "explanation": "<p><strong>120 km.</strong> S = 60 × 2 = 120. Har soatda "
                       "60 kilometrdan ikki soat.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>S = 240 km, t = 3 soat. Tezlik "
                "qancha?</strong></p>",
        "choices": ["80 km/soat", "120 km/soat", "243 km/soat", "720 km/soat"],
        "correct": "80 km/soat",
        "explanation": "<p><strong>80 km/soat.</strong> v = S ÷ t = 240 ÷ 3 = 80. "
                       "<strong>720</strong> — koʻpaytirishdan chiqadi, lekin "
                       "tezlik butun yoʻldan katta boʻlolmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>S = 400 km, v = 80 km/soat. Vaqt "
                "qancha?</strong></p>",
        "choices": ["4 soat", "5 soat", "320 soat", "480 soat"],
        "correct": "5 soat",
        "explanation": "<p><strong>5 soat.</strong> t = S ÷ v = 400 ÷ 80 = 5. "
                       "Tekshirish: 80 × 5 = 400 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>P = 2(a + b); a = 8 sm, b = 5 sm</strong></p>",
        "choices": ["13 sm", "26 sm", "40 sm", "80 sm"],
        "correct": "26 sm",
        "explanation": "<p><strong>26 sm.</strong> P = 2(8 + 5) = 2 × 13 = 26. "
                       "<strong>40</strong> — bu yuza (8 × 5), perimetr emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>S = a · b; a = 8 sm, b = 5 sm</strong></p>",
        "choices": ["13 sm", "26 sm", "40 sm kvadrat", "80 sm kvadrat"],
        "correct": "40 sm kvadrat",
        "explanation": "<p><strong>40 sm kvadrat.</strong> Yuza — tomonlarning "
                       "koʻpaytmasi: 8 × 5 = 40. Birligi kvadrat santimetr, chunki "
                       "ikkita uzunlik koʻpaytirildi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>v = 90 km/soat, t = 4 soat. Yoʻl "
                "qancha?</strong></p>",
        "choices": ["22,5 km", "94 km", "270 km", "360 km"],
        "correct": "360 km",
        "explanation": "<p><strong>360 km.</strong> S = 90 × 4 = 360.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>S = 270 km, t = 3 soat. Tezlik "
                "qancha?</strong></p>",
        "choices": ["60 km/soat", "90 km/soat", "267 km/soat", "810 km/soat"],
        "correct": "90 km/soat",
        "explanation": "<p><strong>90 km/soat.</strong> 270 ÷ 3 = 90. Tekshirish: "
                       "90 × 3 = 270 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>S = 150 km, v = 50 km/soat. Vaqt "
                "qancha?</strong></p>",
        "choices": ["3 soat", "5 soat", "100 soat", "7500 soat"],
        "correct": "3 soat",
        "explanation": "<p><strong>3 soat.</strong> t = 150 ÷ 50 = 3.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Toʻgʻri toʻrtburchakning tomonlari 12 sm va "
                "7 sm.</p><p><strong>Perimetri qancha?</strong></p>",
        "choices": ["19 sm", "38 sm", "84 sm", "168 sm"],
        "correct": "38 sm",
        "explanation": "<p><strong>38 sm.</strong> P = 2(12 + 7) = 2 × 19 = 38. "
                       "<strong>19</strong> — qavsni ikkiga koʻpaytirishni unutgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Toʻgʻri toʻrtburchakning tomonlari 12 sm va "
                "7 sm.</p><p><strong>Yuzasi qancha?</strong></p>",
        "choices": ["19 sm kvadrat", "38 sm kvadrat", "84 sm kvadrat",
                    "144 sm kvadrat"],
        "correct": "84 sm kvadrat",
        "explanation": "<p><strong>84 sm kvadrat.</strong> S = 12 × 7 = 84.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Usta bir soat ish uchun 25 000 soʻm "
                "oladi.</p><p><strong>6 soat ishlasa, haqi qancha?</strong></p>",
        "choices": ["31 000 soʻm", "125 000 soʻm", "150 000 soʻm", "180 000 soʻm"],
        "correct": "150 000 soʻm",
        "explanation": "<p><strong>150 000 soʻm.</strong> haq = s × r = "
                       "6 × 25 000 = 150 000.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>v = 60 km/soat, t = 90 daqiqa. Yoʻl "
                "qancha?</strong></p>",
        "choices": ["90 km", "150 km", "540 km", "5400 km"],
        "correct": "90 km",
        "explanation": "<p><strong>90 km.</strong> Avval birlikni moslashtiramiz: "
                       "90 daqiqa = 1,5 soat. Keyin S = 60 × 1,5 = 90 km. "
                       "<strong>5400</strong> — daqiqani soatga aylantirmaslikdan "
                       "chiqadi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Tomonlari 6 sm va 4 sm "
                "boʻlgan toʻgʻri toʻrtburchakning perimetri va yuzasi "
                "qanday?</strong></p>",
        "choices": [
            "P = 20 sm, S = 24 sm kvadrat",
            "P = 24 sm, S = 20 sm kvadrat",
            "P = 10 sm, S = 24 sm kvadrat",
            "P = 24 sm, S = 24 sm kvadrat",
        ],
        "correct": "P = 20 sm, S = 24 sm kvadrat",
        "explanation": "<p><strong>P = 20, S = 24.</strong> P = 2(6 + 4) = 20 — "
                       "atrofi; S = 6 × 4 = 24 — ichi. Ikkisini almashtirib "
                       "yuborish eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>S = v · t formulasida vaqt "
                "nomaʼlum boʻlsa, qaysi hisob kerak?</strong></p>",
        "choices": ["t = S · v", "t = S ÷ v", "t = v ÷ S", "t = S − v"],
        "correct": "t = S ÷ v",
        "explanation": "<p><strong>t = S ÷ v.</strong> Koʻpaytirishning teskarisi — "
                       "boʻlish, va boʻlinuvchi doim yoʻl (S) boʻladi. "
                       "<strong>v ÷ S</strong> teskari boʻlish — bu eng koʻp "
                       "uchraydigan chalkashlik.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi juftlik "
                "moslashtirilishi shart?</strong></p>",
        "choices": [
            "Yoʻl km da, tezlik km/soat da",
            "Tezlik km/soat da, vaqt daqiqada",
            "Yuza sm kvadratda, tomonlar sm da",
            "Ish haqi soʻmda, soat sonida",
        ],
        "correct": "Tezlik km/soat da, vaqt daqiqada",
        "explanation": "<p><strong>Tezlik km/soat, vaqt daqiqa.</strong> Bu juftlik "
                       "mos emas: vaqtni avval soatga aylantirish kerak. Qolgan "
                       "juftliklarda birliklar allaqachon mos.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>v = 15 km/soat, t = 40 daqiqa. Yoʻl "
                "qancha?</strong></p>",
        "choices": ["6 km", "10 km", "22,5 km", "600 km"],
        "correct": "10 km",
        "explanation": "<p><strong>10 km.</strong> 40 daqiqa = 40/60 = 2/3 soat; "
                       "15 × 2/3 = 10 km. <strong>600</strong> — birlikni "
                       "moslashtirmaslikdan chiqadigan mantiqsiz javob.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>S = 240 km, t = 3 soat; "
                "v = 240 × 3 = 720 km/soat</strong></p>",
        "choices": [
            "Tezlikni topish uchun boʻlish kerak: 240 ÷ 3 = 80",
            "Vaqtni avval daqiqaga aylantirish kerak edi",
            "Yoʻlni ikkiga koʻpaytirish kerak edi",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Tezlikni topish uchun boʻlish kerak: 240 ÷ 3 = 80",
        "explanation": "<p><strong>240 ÷ 3 = 80 km/soat.</strong> Nomaʼlum tezlik "
                       "boʻlsa teskari amal — boʻlish. Nazorat: soatiga 720 "
                       "kilometr — bu samolyot tezligi, poyezdniki emas.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>v = 60 km/soat, "
                "t = 30 daqiqa</strong></p>",
        "choices": [
            "S = 60 × 30 = 1800 km",
            "S = 60 ÷ 30 = 2 km",
            "S = 60 × 0,5 = 30 km",
            "S = 60 + 30 = 90 km",
        ],
        "correct": "S = 60 × 0,5 = 30 km",
        "explanation": "<p><strong>30 km.</strong> 30 daqiqa — yarim soat, yaʼni "
                       "0,5. Yarim soatda 1800 kilometr yurib boʻlmaydi — javobning "
                       "oʻzi xatoni koʻrsatib turadi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Poyezd 240 kilometrlik yoʻlni 3 soatda bosib "
                "oʻtdi.</p><p><strong>Shu tezlikda 400 kilometrni necha soatda "
                "bosib oʻtadi?</strong></p>",
        "choices": ["4 soat", "5 soat", "6 soat", "8 soat"],
        "correct": "5 soat",
        "explanation": "<p><strong>5 soat.</strong> Avval tezlik: 240 ÷ 3 = 80 "
                       "km/soat. Keyin vaqt: 400 ÷ 80 = 5 soat. Tekshirish: "
                       "80 × 5 = 400 ✓</p>",
    },
    {
        "text": "<p>Bogʻning tomonlari 25 metr va 16 metr. Uni panjara bilan "
                "oʻrab chiqmoqchi.</p><p><strong>Necha metr panjara "
                "kerak?</strong></p>",
        "choices": ["41 metr", "82 metr", "400 metr", "800 metr"],
        "correct": "82 metr",
        "explanation": "<p><strong>82 metr.</strong> Panjara atrofga oʻraladi, "
                       "demak perimetr kerak: P = 2(25 + 16) = 2 × 41 = 82 m. "
                       "<strong>400</strong> — yuza (25 × 16), u yerni oʻt bilan "
                       "qoplashda kerak boʻlardi.</p>",
    },
]


# =====================================================================
# PM-36 — bir nomaʼlumli tenglama
# =====================================================================

Q_PM36 = [
    # 1–5 tanish
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>x + 5 = 12</strong></p>",
        "choices": ["x = 5", "x = 7", "x = 12", "x = 17"],
        "correct": "x = 7",
        "explanation": "<p><strong>x = 7.</strong> Ikki tomondan 5 ni ayiramiz: "
                       "x = 12 − 5. <strong>x = 17</strong> — teskari amal "
                       "oʻrniga qoʻshishdan chiqadi; tekshirish darrov tutadi: "
                       "17 + 5 = 22 ≠ 12.</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>x − 3 = 10</strong></p>",
        "choices": ["x = 7", "x = 10", "x = 13", "x = 30"],
        "correct": "x = 13",
        "explanation": "<p><strong>x = 13.</strong> Ikki tomonga 3 ni qoʻshamiz. "
                       "Tekshirish: 13 − 3 = 10 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>3x = 21</strong></p>",
        "choices": ["x = 7", "x = 18", "x = 24", "x = 63"],
        "correct": "x = 7",
        "explanation": "<p><strong>x = 7.</strong> 3x — bu 3 × x, demak teskari "
                       "amal boʻlish: 21 ÷ 3 = 7. <strong>x = 18</strong> — "
                       "boʻlish oʻrniga ayirishdan chiqadi.</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>x/4 = 3</strong></p>",
        "choices": ["x = 0,75", "x = 7", "x = 12", "x = 34"],
        "correct": "x = 12",
        "explanation": "<p><strong>x = 12.</strong> Boʻlishning teskarisi — "
                       "koʻpaytirish: ikki tomonni 4 ga koʻpaytiramiz. Tekshirish: "
                       "12 ÷ 4 = 3 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Muvozanat qoidasi nimani "
                "aytadi?</strong></p>",
        "choices": [
            "Chap tomonga qilingan amal oʻng tomonga ham qilinadi",
            "Nomaʼlum har doim chap tomonda turishi kerak",
            "Ikki tomonni ham nolga tenglashtirish kerak",
            "Faqat qoʻshish va ayirish ishlatiladi",
        ],
        "correct": "Chap tomonga qilingan amal oʻng tomonga ham qilinadi",
        "explanation": "<p><strong>Ikki tomonga bir xil amal.</strong> Tenglama — "
                       "tarozi: bir pallaga nima qilsangiz, ikkinchisiga ham "
                       "shuni qiling, aks holda muvozanat buziladi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>3x + 5 = 20</strong></p>",
        "choices": ["x = 5", "x = 15", "x = 25", "x = 45"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> Avval ikki tomondan 5 ni "
                       "ayiramiz: 3x = 15; keyin 3 ga boʻlamiz. Tekshirish: "
                       "3 × 5 + 5 = 20 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>2x − 7 = 9</strong></p>",
        "choices": ["x = 1", "x = 8", "x = 16", "x = 32"],
        "correct": "x = 8",
        "explanation": "<p><strong>x = 8.</strong> Ikki tomonga 7 qoʻshamiz: "
                       "2x = 16; keyin 2 ga boʻlamiz. Tekshirish: "
                       "2 × 8 − 7 = 9 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>5x + 4 = 24</strong></p>",
        "choices": ["x = 4", "x = 5", "x = 20", "x = 28"],
        "correct": "x = 4",
        "explanation": "<p><strong>x = 4.</strong> 5x = 20, keyin x = 4. "
                       "Tekshirish: 5 × 4 + 4 = 24 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>x/3 + 2 = 6</strong></p>",
        "choices": ["x = 4", "x = 12", "x = 18", "x = 24"],
        "correct": "x = 12",
        "explanation": "<p><strong>x = 12.</strong> Avval 2 ni ayiramiz: x/3 = 4; "
                       "keyin ikki tomonni 3 ga koʻpaytiramiz. Tekshirish: "
                       "12 ÷ 3 + 2 = 6 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>7 = x + 2</strong></p>",
        "choices": ["x = 5", "x = 7", "x = 9", "x = 14"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> Nomaʼlum oʻng tomonda turgani "
                       "hech nimani oʻzgartirmaydi: ikki tomondan 2 ni ayiramiz. "
                       "Tekshirish: 5 + 2 = 7 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>2(x + 3) = 16</strong></p>",
        "choices": ["x = 5", "x = 8", "x = 10", "x = 11"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> Ikki tomonni 2 ga boʻlamiz: "
                       "x + 3 = 8, demak x = 5. Yoki qavsni ochib: 2x + 6 = 16 → "
                       "2x = 10. Ikki yoʻl bir xil javob beradi.</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>4x − 6 = 18</strong></p>",
        "choices": ["x = 3", "x = 6", "x = 12", "x = 24"],
        "correct": "x = 6",
        "explanation": "<p><strong>x = 6.</strong> 4x = 24, keyin x = 6. "
                       "Tekshirish: 4 × 6 − 6 = 18 ✓</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>x + 6 = 18 va 6x = 18 "
                "tenglamalarining yechimlari qanday?</strong></p>",
        "choices": ["12 va 3", "3 va 12", "Ikkalasi ham 12", "Ikkalasi ham 3"],
        "correct": "12 va 3",
        "explanation": "<p><strong>12 va 3.</strong> Birinchisida qoʻshish bor — "
                       "teskarisi ayirish (18 − 6). Ikkinchisida koʻpaytirish — "
                       "teskarisi boʻlish (18 ÷ 6). Yozuvdagi kichik farq amalni "
                       "butunlay oʻzgartiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>5x = 40 tenglamasini "
                "yechish uchun ikki tomonga nima qilinadi?</strong></p>",
        "choices": [
            "5 ayiriladi",
            "5 ga boʻlinadi",
            "5 qoʻshiladi",
            "5 ga koʻpaytiriladi",
        ],
        "correct": "5 ga boʻlinadi",
        "explanation": "<p><strong>5 ga boʻlinadi.</strong> 5x — koʻpaytma, uning "
                       "teskarisi boʻlish: x = 8. <strong>5 ayirilsa</strong> "
                       "5x − 5 chiqadi va nomaʼlum yolgʻiz qolmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son 3x − 4 = 11 "
                "tenglamasining yechimi?</strong></p>",
        "choices": ["x = 3", "x = 5", "x = 7", "x = 15"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> Har birini qoʻyib tekshirish "
                       "mumkin: 3 × 5 − 4 = 11 ✓ Yechim — tenglamani toʻgʻri "
                       "qiladigan yagona son.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi yozuv tenglama, "
                "ifoda emas?</strong></p>",
        "choices": ["4a + 7", "2(x − 1)", "5n = 45", "12 − y"],
        "correct": "5n = 45",
        "explanation": "<p><strong>5n = 45.</strong> Tenglik belgisi bor va "
                       "nomaʼlumni topish mumkin (n = 9). Qolganlari — ifodalar, "
                       "ularni faqat hisoblash mumkin.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>3x = 21 → x = 21 − 3 = 18"
                "</strong></p>",
        "choices": [
            "Koʻpaytirishning teskarisi boʻlish: x = 21 ÷ 3 = 7",
            "Ikki tomonga 3 qoʻshish kerak edi",
            "Tenglamani yechib boʻlmaydi",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Koʻpaytirishning teskarisi boʻlish: x = 21 ÷ 3 = 7",
        "explanation": "<p><strong>x = 7.</strong> 3x — bu 3 × x, qoʻshish emas. "
                       "Tekshirish xatoni darrov koʻrsatadi: 3 × 18 = 54 ≠ 21.</p>",
    },
    {
        "text": "<p>Qaysi qadam toʻgʻri?</p><p><strong>2x + 6 = 14</strong></p>",
        "choices": [
            "2x + 6 − 6 = 14 → 2x = 14",
            "2x + 6 − 6 = 14 − 6 → 2x = 8",
            "2x = 14 + 6 → 2x = 20",
            "x + 6 = 7 → x = 1",
        ],
        "correct": "2x + 6 − 6 = 14 − 6 → 2x = 8",
        "explanation": "<p><strong>2x = 8, demak x = 4.</strong> Amal ikkala tomonga "
                       "ham qilinishi shart. Birinchi variantda faqat chap tomondan "
                       "ayirilgan — tarozi ogʻib ketadi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Afsona 3 ta bir xil daftar oldi va 24 000 soʻm toʻladi. Bitta "
                "daftar narxi x boʻlsin.</p><p><strong>Bitta daftar necha soʻm "
                "turadi?</strong></p>",
        "choices": ["6000 soʻm", "8000 soʻm", "12 000 soʻm", "72 000 soʻm"],
        "correct": "8000 soʻm",
        "explanation": "<p><strong>8000 soʻm.</strong> Tenglama: 3x = 24 000; ikki "
                       "tomonni 3 ga boʻlamiz. Tekshirish: 3 × 8000 = 24 000 ✓ "
                       "<strong>72 000</strong> — boʻlish oʻrniga koʻpaytirishdan "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Sinfda har bir oʻquvchi 5000 soʻmdan, sinf rahbari esa 20 000 "
                "soʻm qoʻshdi. Kassada 140 000 soʻm bor. Oʻquvchilar soni "
                "n.</p><p><strong>Sinfda nechta oʻquvchi bor?</strong></p>",
        "choices": ["20 ta", "24 ta", "28 ta", "32 ta"],
        "correct": "24 ta",
        "explanation": "<p><strong>24 ta.</strong> Tenglama: 5000n + 20 000 = "
                       "140 000. Ikki tomondan 20 000 ni ayiramiz: 5000n = 120 000; "
                       "keyin 5000 ga boʻlamiz. Tekshirish: "
                       "5000 × 24 + 20 000 = 140 000 ✓</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-34 Mashq: Umumiy koʻpaytuvchini qavsdan chiqarish",
        "description": "20 savol — umumiy koʻpaytuvchini EKUB orqali topish, "
                       "qavsdan chiqarish va javobni ochib tekshirish.",
        "tutorial":    "PM-34:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM34,
    },
    {
        "title":       "PM-35 Mashq: Formula bilan ishlash",
        "description": "20 savol — S = v·t oilasi, perimetr va yuza formulalari "
                       "hamda birliklarni moslashtirish.",
        "tutorial":    "PM-35:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM35,
    },
    {
        "title":       "PM-36 Mashq: Bir nomaʼlumli tenglama",
        "description": "20 savol — muvozanat qoidasi, bir va ikki qadamli "
                       "tenglamalar, qavsli tenglama va javobni tekshirish.",
        "tutorial":    "PM-36:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM36,
    },
]
