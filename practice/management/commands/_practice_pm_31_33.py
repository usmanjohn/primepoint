# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-31 … PM-33 (qiymat, oʻxshash hadlar, qavs ochish).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ `choices` EKRANLANADI — u yerda HTML teg boʻlmasligi kerak. Shuning uchun
   daraja «a·a» yoki «a kvadrat» deb yoziladi, savol matnida esa <sup> mumkin.
⚠️ Kumulyativ: PM-31 da ixchamlash yoʻq, PM-32 da qavs ochilmaydi; umumiy
   koʻpaytuvchini qavsdan chiqarish (PM-34) va tenglama (PM-36) uch testda ham
   yoʻq.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_31_33.py --master=prime \\
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
# PM-31 — ifodaning qiymatini hisoblash
# =====================================================================

Q_PM31 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>3a, a = 4</strong></p>",
        "choices": ["7", "12", "34", "43"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 3a — bu 3 × a, demak 3 × 4 = 12. "
                       "<strong>34</strong> — harf oʻrniga sonni yonma-yon "
                       "yozishdan chiqadigan xato; <strong>7</strong> esa "
                       "koʻpaytirish oʻrniga qoʻshishdan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>a + 7, a = 5</strong></p>",
        "choices": ["2", "12", "35", "57"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 5 + 7 = 12. Bu yerda koʻpaytirish "
                       "yoʻq — qoʻshish belgisi yozilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2a + 1, a = 3</strong></p>",
        "choices": ["5", "7", "8", "21"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Avval koʻpaytirish: 2 × 3 = 6, keyin "
                       "6 + 1 = 7. <strong>8</strong> — avval qoʻshib "
                       "(3 + 1 = 4), keyin ikkiga koʻpaytirishdan chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>a<sup>2</sup>, a = 6</strong></p>",
        "choices": ["12", "26", "36", "62"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> Kvadrat — a ni oʻziga koʻpaytirish: "
                       "6 × 6 = 36. <strong>12</strong> — darajani ikkiga "
                       "koʻpaytirish deb oʻqishdan chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>10 − a, a = 4</strong></p>",
        "choices": ["4", "6", "14", "40"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 10 − 4 = 6. Ayirishda tartib muhim: "
                       "a birinchi emas, ikkinchi turibdi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>3a + 5, a = 4</strong></p>",
        "choices": ["12", "17", "27", "32"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> 3 × 4 = 12, keyin 12 + 5 = 17. "
                       "<strong>27</strong> — avval 4 + 5 = 9 qilib, keyin uchga "
                       "koʻpaytirishdan chiqadi: amallar tartibi buzilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2a + 3b, a = 4, b = 5</strong></p>",
        "choices": ["14", "23", "35", "60"],
        "correct": "23",
        "explanation": "<p><strong>23.</strong> 2 × 4 = 8 va 3 × 5 = 15; "
                       "8 + 15 = 23. Har harfning oʻz soni qoʻyiladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>5(a + 2), a = 3</strong></p>",
        "choices": ["17", "21", "25", "30"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Qavs avval: 3 + 2 = 5, keyin "
                       "5 × 5 = 25. <strong>17</strong> — qavsni eʼtiborsiz "
                       "qoldirib 5 × 3 + 2 qilishdan chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>a<sup>2</sup> − 1, a = 6</strong></p>",
        "choices": ["11", "25", "35", "36"],
        "correct": "35",
        "explanation": "<p><strong>35.</strong> Avval daraja: 6 × 6 = 36, keyin "
                       "36 − 1 = 35. Daraja qoʻshish va ayirishdan oldin "
                       "bajariladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(a + b)/2, a = 7, b = 9</strong></p>",
        "choices": ["8", "11", "16", "23"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Kasr chizigʻi qavs vazifasini "
                       "bajaradi: avval 7 + 9 = 16, keyin 16 ÷ 2 = 8. "
                       "<strong>11</strong> — faqat b ni ikkiga boʻlishdan "
                       "chiqadi (7 + 4,5 emas, 7 + 4).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>100 − 4n, n = 12</strong></p>",
        "choices": ["48", "52", "88", "1152"],
        "correct": "52",
        "explanation": "<p><strong>52.</strong> 4 × 12 = 48, keyin "
                       "100 − 48 = 52. <strong>48</strong> — ayirishni unutgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>ab, a = 6, b = 7</strong></p>",
        "choices": ["13", "42", "67", "76"],
        "correct": "42",
        "explanation": "<p><strong>42.</strong> Yonma-yon turgan harflar "
                       "koʻpaytiriladi: 6 × 7 = 42. <strong>67</strong> — "
                       "sonlarni yonma-yon yozishdan chiqadi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Hisoblang.</p><p>a = 5.</p><p><strong>a<sup>2</sup> va 2a "
                "qiymatlari qanday?</strong></p>",
        "choices": ["10 va 25", "25 va 10", "Ikkalasi ham 10", "Ikkalasi ham 25"],
        "correct": "25 va 10",
        "explanation": "<p><strong>25 va 10.</strong> Kvadrat — koʻpaytirish "
                       "(5 × 5), 2a esa qoʻshish natijasi (5 + 5). Ular faqat "
                       "a = 2 boʻlgandagina teng boʻladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>a = 2.</p><p><strong>3a<sup>2</sup> nechaga "
                "teng?</strong></p>",
        "choices": ["12", "18", "36", "64"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Daraja faqat a ga tegishli: "
                       "3 × (2 × 2) = 3 × 4 = 12. <strong>36</strong> — butun "
                       "koʻpaytmani kvadratga koʻtarishdan chiqadi, lekin bu "
                       "(3a)<sup>2</sup> boʻlar edi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−a, a = −5</strong></p>",
        "choices": ["−10", "−5", "0", "5"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> −a — «a ning qarama-qarshisi». a "
                       "manfiy boʻlsa, uning qarama-qarshisi musbat: "
                       "−(−5) = 5 (PM-9).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>a = 4.</p><p><strong>2(a + 3) va 2a + 3 "
                "qiymatlari qanday?</strong></p>",
        "choices": ["11 va 14", "14 va 11", "Ikkalasi ham 14", "Ikkalasi ham 11"],
        "correct": "14 va 11",
        "explanation": "<p><strong>14 va 11.</strong> Qavs avval bajariladi: "
                       "2 × 7 = 14. Qavssiz esa avval koʻpaytirish: 8 + 3 = 11.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>3a<sup>2</sup>, a = 2: "
                "3 × 2 = 6, keyin 6 × 6 = 36</strong></p>",
        "choices": [
            "Daraja faqat a ga tegishli: 3 × 4 = 12 boʻlishi kerak",
            "Koʻpaytirish oʻrniga qoʻshish kerak edi",
            "Avval 3 ni kvadratga koʻtarish kerak edi",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Daraja faqat a ga tegishli: 3 × 4 = 12 boʻlishi kerak",
        "explanation": "<p><strong>Daraja faqat a ga tegishli.</strong> Avval "
                       "2 × 2 = 4, keyin 3 × 4 = 12. Butun koʻpaytmani kvadratga "
                       "koʻtarish uchun qavs kerak edi: (3a)<sup>2</sup>.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>a<sup>2</sup>, a = −3</strong></p>",
        "choices": [
            "−3 × 3 = −9",
            "(−3) × (−3) = 9",
            "−(3 × 3) = −9",
            "3 × 3 = 9 va oldiga minus qoʻyiladi",
        ],
        "correct": "(−3) × (−3) = 9",
        "explanation": "<p><strong>9.</strong> Manfiy sonni qavsga olamiz va uni "
                       "oʻziga koʻpaytiramiz. Ikki manfiyning koʻpaytmasi musbat "
                       "(PM-11), shuning uchun javob 9 — minus yoʻqoladi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Elektr toʻlovi: abonent haqi 15 000 soʻm, ustiga har bir "
                "kilovatt-soat uchun 450 soʻm. Toʻlov ifodasi 15 000 + 450k.</p>"
                "<p><strong>120 kilovatt-soat sarflansa, toʻlov qancha?</strong></p>",
        "choices": ["54 000 soʻm", "69 000 soʻm", "87 000 soʻm", "1 800 000 soʻm"],
        "correct": "69 000 soʻm",
        "explanation": "<p><strong>69 000 soʻm.</strong> 450 × 120 = 54 000, keyin "
                       "15 000 + 54 000 = 69 000. <strong>54 000</strong> — "
                       "abonent haqi qoʻshilmagan javob.</p>",
    },
    {
        "text": "<p>Sinf ekskursiyaga chiqmoqchi. Avtobus 400 000 soʻm, har bir "
                "oʻquvchining chiptasi 25 000 soʻm. Xarajat ifodasi "
                "400 000 + 25 000n.</p><p><strong>24 oʻquvchi borsa, jami xarajat "
                "qancha?</strong></p>",
        "choices": ["600 000 soʻm", "1 000 000 soʻm", "10 200 000 soʻm",
                    "425 000 soʻm"],
        "correct": "1 000 000 soʻm",
        "explanation": "<p><strong>1 000 000 soʻm.</strong> 25 000 × 24 = 600 000, "
                       "keyin 400 000 + 600 000 = 1 000 000. "
                       "<strong>10 200 000</strong> — avtobus narxini ham n ga "
                       "koʻpaytirishdan chiqadi, lekin avtobus barcha uchun "
                       "bitta.</p>",
    },
]


# =====================================================================
# PM-32 — oʻxshash hadlarni ixchamlash
# =====================================================================

Q_PM32 = [
    # 1–5 tanish
    {
        "text": "<p>Ixchamlang.</p><p><strong>3a + 5a = ?</strong></p>",
        "choices": ["8a", "15a", "8", "8aa"],
        "correct": "8a",
        "explanation": "<p><strong>8a.</strong> Koeffitsientlar qoʻshiladi "
                       "(3 + 5 = 8), harf qismi oʻzgarmaydi. "
                       "<strong>15a</strong> — qoʻshish oʻrniga koʻpaytirishdan "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>7x − 3x = ?</strong></p>",
        "choices": ["4", "4x", "10x", "21x"],
        "correct": "4x",
        "explanation": "<p><strong>4x.</strong> 7 − 3 = 4, harf qismi x boʻlib "
                       "qoladi. <strong>4</strong> — x ni yoʻqotib yuborgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>2b + b = ?</strong></p>",
        "choices": ["2b", "3b", "2bb", "3"],
        "correct": "3b",
        "explanation": "<p><strong>3b.</strong> Yolgʻiz b — bu 1b, demak "
                       "2 + 1 = 3. Koʻrinmayotgan koeffitsient har doim 1.</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>5m − m = ?</strong></p>",
        "choices": ["4m", "5m", "5", "4"],
        "correct": "4m",
        "explanation": "<p><strong>4m.</strong> 5 − 1 = 4. m butunlay yoʻqolmaydi "
                       "— undan bittasi ayirildi, xolos.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi juftlik oʻxshash "
                "hadlar?</strong></p>",
        "choices": ["3a va 5b", "4x va 9x", "2m va 2n", "a va b"],
        "correct": "4x va 9x",
        "explanation": "<p><strong>4x va 9x.</strong> Oʻxshash hadlarda harf qismi "
                       "bir xil boʻlishi kerak; koeffitsient har xil boʻlsa "
                       "mayli. Qolgan juftliklarda harflar boshqa-boshqa.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Ixchamlang.</p><p><strong>4a + 3b − a + 2b = ?</strong></p>",
        "choices": ["3a + 5b", "5a + 5b", "3a + b", "8ab"],
        "correct": "3a + 5b",
        "explanation": "<p><strong>3a + 5b.</strong> a li hadlar: 4 − 1 = 3; b li "
                       "hadlar: 3 + 2 = 5. Tekshirish a = 2, b = 3 da: "
                       "8 + 9 − 2 + 6 = 21 va 6 + 15 = 21 ✓</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>5x + 3 − 2x + 7 = ?</strong></p>",
        "choices": ["3x + 10", "7x + 10", "3x + 4", "13x"],
        "correct": "3x + 10",
        "explanation": "<p><strong>3x + 10.</strong> x li hadlar: 5 − 2 = 3; ozod "
                       "hadlar: 3 + 7 = 10. Harfli va harfsiz hadlar alohida "
                       "guruhlarda qoʻshiladi.</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>6y − 2y + 3y = ?</strong></p>",
        "choices": ["5y", "7y", "11y", "y"],
        "correct": "7y",
        "explanation": "<p><strong>7y.</strong> Koeffitsientlar ketma-ket: "
                       "6 − 2 + 3 = 7. Ishorani har doim oʻz hadi bilan birga "
                       "oling.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3a + 4b ifodasini "
                "ixchamlash mumkinmi?</strong></p>",
        "choices": [
            "Ha, 7ab boʻladi",
            "Ha, 7 boʻladi",
            "Yoʻq — harf qismlari har xil",
            "Ha, 12ab boʻladi",
        ],
        "correct": "Yoʻq — harf qismlari har xil",
        "explanation": "<p><strong>Ixchamlanmaydi.</strong> a va b har xil narsani "
                       "bildiradi, ularni qoʻshib bitta had qilib boʻlmaydi. "
                       "3a + 4b — bu toʻliq javob, tugallanmagan emas.</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>10x − 4x − x = ?</strong></p>",
        "choices": ["5x", "6x", "7x", "5"],
        "correct": "5x",
        "explanation": "<p><strong>5x.</strong> 10 − 4 − 1 = 5. Oxirgi hadning "
                       "koeffitsienti 1 — uni unutish eng koʻp uchraydigan "
                       "xato.</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>2a + 3 + 4a + 5 = ?</strong></p>",
        "choices": ["6a + 8", "14a", "6a + 15", "9a + 5"],
        "correct": "6a + 8",
        "explanation": "<p><strong>6a + 8.</strong> Harfli hadlar 2 + 4 = 6; ozod "
                       "hadlar 3 + 5 = 8. <strong>14a</strong> — hamma sonni "
                       "aralashtirib qoʻshishdan chiqadi.</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>7m − m + 2m = ?</strong></p>",
        "choices": ["6m", "8m", "9m", "10m"],
        "correct": "8m",
        "explanation": "<p><strong>8m.</strong> 7 − 1 + 2 = 8.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Hisoblang.</p><p>a = 3.</p><p><strong>a + a va a·a qiymatlari "
                "qanday?</strong></p>",
        "choices": ["6 va 9", "9 va 6", "Ikkalasi ham 6", "Ikkalasi ham 9"],
        "correct": "6 va 9",
        "explanation": "<p><strong>6 va 9.</strong> a + a = 2a — qoʻshish; a·a = "
                       "a kvadrat — koʻpaytirish. Ixchamlashda qoʻshish harf "
                       "qismini oʻzgartirmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi juftlik oʻxshash "
                "hadlar EMAS?</strong></p>",
        "choices": ["5a va a", "2x va 7x", "a·a va a", "3m va −m"],
        "correct": "a·a va a",
        "explanation": "<p><strong>a·a va a.</strong> Darajalari har xil: biri a "
                       "kvadrat, ikkinchisi oddiy a. Oʻxshash hadlarda harf qismi "
                       "toʻliq bir xil boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>4a + 4b = ?</strong></p>",
        "choices": ["8ab", "8a", "4ab", "4a + 4b — ixchamlanmaydi"],
        "correct": "4a + 4b — ixchamlanmaydi",
        "explanation": "<p><strong>Ixchamlanmaydi.</strong> Koeffitsientlar bir xil "
                       "boʻlgani bilan harf qismlari boshqa. Bunday ifodani "
                       "keyinroq qavsdan umumiy koʻpaytuvchi chiqarib yozish "
                       "mumkin, lekin qoʻshib bitta had qilib boʻlmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>5x − 3y + 2x ifodasida "
                "nechta had qoladi?</strong></p>",
        "choices": ["1 ta", "2 ta", "3 ta", "4 ta"],
        "correct": "2 ta",
        "explanation": "<p><strong>2 ta:</strong> 7x va −3y. x li hadlar qoʻshildi "
                       "(5 + 2 = 7), y li had esa yolgʻiz qoldi — unga juft "
                       "topilmadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>3a + 5b = 8ab</strong></p>",
        "choices": [
            "Har xil harf qismli hadlar qoʻshilmaydi",
            "Koeffitsientlar koʻpaytirilishi kerak edi",
            "Javob 8 boʻlishi kerak",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Har xil harf qismli hadlar qoʻshilmaydi",
        "explanation": "<p><strong>Ixchamlanmaydi.</strong> Tekshirish: a = 2, "
                       "b = 1 boʻlsa chapda 6 + 5 = 11, oʻngda esa 8 × 2 = 16 — "
                       "teng emas. Demak bu ikki ifoda bir xil emas.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>6x − x</strong></p>",
        "choices": ["6", "5x", "6x", "5"],
        "correct": "5x",
        "explanation": "<p><strong>5x.</strong> x — bu 1x, demak 6 − 1 = 5. "
                       "<strong>6</strong> — x ni butunlay yoʻqotib yuborgan "
                       "javob. Tekshirish x = 2 da: 12 − 2 = 10 va 5 × 2 = 10 ✓</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Omborga ertalab 5 quti va 3 qop un keldi. Kun davomida 2 quti va "
                "1 qop sotildi, kechqurun yana 4 quti keltirildi. Bitta quti a kg, "
                "bitta qop b kg.</p><p><strong>Ombordagi un qanday "
                "ixchamlanadi?</strong></p>",
        "choices": ["7a + 2b", "11a + 4b", "7a + 4b", "9a + 2b"],
        "correct": "7a + 2b",
        "explanation": "<p><strong>7a + 2b.</strong> Qutilar: 5 − 2 + 4 = 7; "
                       "qoplar: 3 − 1 = 2. Sotilgan mahsulot minus ishorasi bilan "
                       "yoziladi.</p>",
    },
    {
        "text": "<p>Bitta daftar a soʻm, bitta ruchka b soʻm. Afsona 4 daftar va 2 "
                "ruchka oldi, keyin yana 3 daftar oldi, lekin bitta ruchkani "
                "qaytardi.</p><p><strong>a = 6000, b = 4000 boʻlsa, Afsona qancha "
                "pul sarfladi?</strong></p>",
        "choices": ["42 000 soʻm", "46 000 soʻm", "50 000 soʻm", "54 000 soʻm"],
        "correct": "46 000 soʻm",
        "explanation": "<p><strong>46 000 soʻm.</strong> Ixchamlaymiz: daftarlar "
                       "4 + 3 = 7 ta, ruchkalar 2 − 1 = 1 ta, yaʼni 7a + b. Keyin "
                       "7 × 6000 + 4000 = 46 000. <strong>42 000</strong> — "
                       "ruchka hisobga olinmagan javob.</p>",
    },
]


# =====================================================================
# PM-33 — qavslarni ochish
# =====================================================================

Q_PM33 = [
    # 1–5 tanish
    {
        "text": "<p>Qavsni oching.</p><p><strong>3(x + 4) = ?</strong></p>",
        "choices": ["3x + 4", "3x + 12", "x + 12", "3x + 7"],
        "correct": "3x + 12",
        "explanation": "<p><strong>3x + 12.</strong> Koʻpaytuvchi har ikkala hadga "
                       "ham tarqaladi: 3 × x va 3 × 4. <strong>3x + 4</strong> — "
                       "ikkinchi hadni unutgan javob.</p>",
    },
    {
        "text": "<p>Qavsni oching.</p><p><strong>2(a − 5) = ?</strong></p>",
        "choices": ["2a − 5", "2a − 10", "2a + 10", "a − 10"],
        "correct": "2a − 10",
        "explanation": "<p><strong>2a − 10.</strong> 2 × a = 2a va 2 × (−5) = −10. "
                       "Ichkaridagi ishora oʻz joyida qoladi.</p>",
    },
    {
        "text": "<p>Qavsni oching.</p><p><strong>−(x + 3) = ?</strong></p>",
        "choices": ["−x + 3", "−x − 3", "x − 3", "x + 3"],
        "correct": "−x − 3",
        "explanation": "<p><strong>−x − 3.</strong> Qavs oldidagi minus — bu −1 ga "
                       "koʻpaytirish, demak ikkala hadning ham ishorasi "
                       "almashadi.</p>",
    },
    {
        "text": "<p>Soddalashtiring.</p><p><strong>5 − (x − 2) = ?</strong></p>",
        "choices": ["3 − x", "7 − x", "5 − x − 2", "x − 7"],
        "correct": "7 − x",
        "explanation": "<p><strong>7 − x.</strong> Minus ikkala ishorani "
                       "almashtiradi: 5 − x + 2, keyin ozod hadlar qoʻshiladi. "
                       "<strong>3 − x</strong> — faqat birinchi ishorani "
                       "almashtirgan javob.</p>",
    },
    {
        "text": "<p>Qavsni oching.</p><p><strong>2(3x + 1) = ?</strong></p>",
        "choices": ["6x + 1", "6x + 2", "5x + 2", "3x + 2"],
        "correct": "6x + 2",
        "explanation": "<p><strong>6x + 2.</strong> 2 × 3x = 6x va 2 × 1 = 2.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Qavsni oching.</p><p><strong>−3(a − 2) = ?</strong></p>",
        "choices": ["−3a − 6", "−3a + 6", "3a − 6", "−3a + 2"],
        "correct": "−3a + 6",
        "explanation": "<p><strong>−3a + 6.</strong> (−3) × (−2) = +6 — ikki "
                       "manfiyning koʻpaytmasi musbat (PM-11). "
                       "<strong>−3a − 6</strong> — ishoralar qoidasini unutgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Soddalashtiring.</p><p><strong>2(x + 3) + 3(x − 1) = ?</strong></p>",
        "choices": ["5x + 3", "5x + 9", "5x + 5", "6x + 3"],
        "correct": "5x + 3",
        "explanation": "<p><strong>5x + 3.</strong> Ochamiz: 2x + 6 + 3x − 3; "
                       "keyin ixchamlaymiz: 5x va 6 − 3 = 3. Tekshirish x = 2 da: "
                       "2 × 5 + 3 × 1 = 13 va 5 × 2 + 3 = 13 ✓</p>",
    },
    {
        "text": "<p>Soddalashtiring.</p><p><strong>4(2a + 1) − 3(a − 2) = ?</strong></p>",
        "choices": ["5a − 2", "5a + 10", "11a + 10", "5a − 10"],
        "correct": "5a + 10",
        "explanation": "<p><strong>5a + 10.</strong> 8a + 4 − 3a + 6; keyin "
                       "8a − 3a = 5a va 4 + 6 = 10. Ikkinchi qavs oldida minus "
                       "boʻlgani uchun −2 → +6 boʻldi.</p>",
    },
    {
        "text": "<p>Soddalashtiring.</p><p><strong>6 − 2(x + 1) = ?</strong></p>",
        "choices": ["4 − 2x", "4x", "8 − 2x", "6 − 2x + 1"],
        "correct": "4 − 2x",
        "explanation": "<p><strong>4 − 2x.</strong> Avval qavs: −2 × x = −2x va "
                       "−2 × 1 = −2, demak 6 − 2x − 2, keyin 6 − 2 = 4.</p>",
    },
    {
        "text": "<p>Soddalashtiring.</p><p><strong>3(a + 2) + 2 = ?</strong></p>",
        "choices": ["3a + 4", "3a + 8", "5a + 4", "3a + 6"],
        "correct": "3a + 8",
        "explanation": "<p><strong>3a + 8.</strong> Qavs ochiladi: 3a + 6, keyin "
                       "ozod hadlar: 6 + 2 = 8.</p>",
    },
    {
        "text": "<p>Qavsni oching.</p><p><strong>−(2x − 5) = ?</strong></p>",
        "choices": ["−2x − 5", "−2x + 5", "2x − 5", "2x + 5"],
        "correct": "−2x + 5",
        "explanation": "<p><strong>−2x + 5.</strong> Ikkala ishora ham almashadi: "
                       "+2x manfiy boʻldi, −5 esa musbat.</p>",
    },
    {
        "text": "<p>Soddalashtiring.</p><p><strong>5(x − 1) − 2x = ?</strong></p>",
        "choices": ["3x − 5", "3x − 1", "7x − 5", "3x + 5"],
        "correct": "3x − 5",
        "explanation": "<p><strong>3x − 5.</strong> 5x − 5 − 2x; keyin "
                       "5x − 2x = 3x. Ozod had oʻzgarmaydi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Hisoblang.</p><p>x = 4.</p><p><strong>5 − (x − 3) va 5 − x − 3 "
                "qiymatlari qanday?</strong></p>",
        "choices": ["4 va −2", "−2 va 4", "Ikkalasi ham 4", "Ikkalasi ham −2"],
        "correct": "4 va −2",
        "explanation": "<p><strong>4 va −2.</strong> Birinchisi: 5 − 1 = 4. "
                       "Ikkinchisi: 5 − 4 − 3 = −2. Qavs oldidagi minus ikkinchi "
                       "ishorani ham almashtirishi kerak edi — mana shu farq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2(x + 3) va 2x + 3 bir xil "
                "ifodami?</strong></p>",
        "choices": [
            "Ha, ikkalasi ham bir xil",
            "Yoʻq: 2(x + 3) = 2x + 6",
            "Yoʻq: 2(x + 3) = 2x + 5",
            "Faqat x = 0 boʻlganda bir xil",
        ],
        "correct": "Yoʻq: 2(x + 3) = 2x + 6",
        "explanation": "<p><strong>Bir xil emas.</strong> Qavs ochilganda 3 ham "
                       "ikkiga koʻpaytiriladi. Tekshirish x = 1 da: 2 × 4 = 8, "
                       "lekin 2 + 3 = 5.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi ifoda 4n + 12 ga "
                "teng?</strong></p>",
        "choices": ["4(n + 12)", "4(n + 3)", "4n + 3", "n + 12"],
        "correct": "4(n + 3)",
        "explanation": "<p><strong>4(n + 3).</strong> Ochib koʻramiz: 4 × n = 4n "
                       "va 4 × 3 = 12 ✓ <strong>4(n + 12)</strong> ochilganda "
                       "4n + 48 beradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>a = 5.</p><p><strong>−2(a − 3) nechaga "
                "teng?</strong></p>",
        "choices": ["−16", "−4", "4", "16"],
        "correct": "−4",
        "explanation": "<p><strong>−4.</strong> Ochamiz: −2a + 6 = −10 + 6 = −4. "
                       "Yoki qavsni avval hisoblab: −2 × (5 − 3) = −2 × 2 = −4. "
                       "<strong>−16</strong> — ishoralar qoidasi buzilganda "
                       "chiqadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>10 − (a − 4) = "
                "10 − a − 4 = 6 − a</strong></p>",
        "choices": [
            "Minus ikkala ishorani almashtiradi: 10 − a + 4 = 14 − a",
            "Qavsni umuman ochib boʻlmaydi",
            "Ozod hadlar notoʻgʻri qoʻshilgan",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Minus ikkala ishorani almashtiradi: 10 − a + 4 = 14 − a",
        "explanation": "<p><strong>14 − a boʻlishi kerak.</strong> Tekshirish "
                       "a = 6 da: asl ifoda 10 − 2 = 8; toʻgʻri javob "
                       "14 − 6 = 8 ✓; notoʻgʻri javob esa 6 − 6 = 0 beradi.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>3(x + 5)</strong></p>",
        "choices": ["3x + 5", "3x + 8", "3x + 15", "x + 15"],
        "correct": "3x + 15",
        "explanation": "<p><strong>3x + 15.</strong> Uchlik ikkala hadga ham "
                       "tarqaladi. <strong>3x + 8</strong> — koʻpaytirish oʻrniga "
                       "qoʻshishdan (3 + 5) chiqadi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Kutubxonaga toʻrtta bir xil paket keldi. Har paketda n ta kitob "
                "va 3 ta daftar bor.</p><p><strong>n = 12 boʻlsa, jami nechta narsa "
                "keldi?</strong></p>",
        "choices": ["48 ta", "51 ta", "60 ta", "63 ta"],
        "correct": "60 ta",
        "explanation": "<p><strong>60 ta.</strong> Ifoda 4(n + 3) = 4n + 12; "
                       "n = 12 boʻlsa 48 + 12 = 60. Tekshirish: har paketda "
                       "12 + 3 = 15 ta, toʻrt paket — 60 ta ✓ "
                       "<strong>51</strong> — qavsni ochmasdan 4n + 3 qilishdan "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Uchta bir xil sovgʻa xalta tayyorlandi. Har xaltada a soʻmlik "
                "shirinlik va 5000 soʻmlik oʻyinchoq bor.</p><p><strong>a = 20 000 "
                "boʻlsa, jami xarajat qancha?</strong></p>",
        "choices": ["60 000 soʻm", "65 000 soʻm", "75 000 soʻm", "80 000 soʻm"],
        "correct": "75 000 soʻm",
        "explanation": "<p><strong>75 000 soʻm.</strong> Ifoda 3(a + 5000) = "
                       "3a + 15 000; a = 20 000 boʻlsa 60 000 + 15 000 = 75 000. "
                       "<strong>65 000</strong> — oʻyinchoqni faqat bitta xaltaga "
                       "hisoblashdan chiqadi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-31 Mashq: Ifodaning qiymatini hisoblash",
        "description": "20 savol — harf oʻrniga son qoʻyish, amallar tartibi, "
                       "manfiy son va daraja bilan ishlash.",
        "tutorial":    "PM-31:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM31,
    },
    {
        "title":       "PM-32 Mashq: Oʻxshash hadlarni ixchamlash",
        "description": "20 savol — hadlarni ajratish, oʻxshash hadlarni tanish va "
                       "koeffitsientlarni qoʻshib ifodani qisqartirish.",
        "tutorial":    "PM-32:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM32,
    },
    {
        "title":       "PM-33 Mashq: Qavslarni ochish",
        "description": "20 savol — taqsimot qonuni, qavs oldidagi minus va "
                       "ochilgandan keyin ixchamlash.",
        "tutorial":    "PM-33:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM33,
    },
]
