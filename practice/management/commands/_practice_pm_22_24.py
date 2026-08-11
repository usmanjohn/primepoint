# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-22 … PM-24 (foizning uch qiyofasi va ikki teskari savol).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ `text` |safe bilan chiqadi (HTML mumkin), `choices` esa ekranlanadi —
   u yerda HTML teg yoʻq; kasrlar «3/4», oʻnlik kasrlar vergul bilan «0,45»,
   foiz «25%» koʻrinishida yoziladi.
⚠️ Kumulyativ: foiz OʻZGARISHI (oshdi/kamaydi, PM-25) va chegirmadan keyingi
   yangi narxni topish qoidasi (PM-26) bu uch testda YOʻQ. PM-24 dagi chegirma
   faqat «narxning p foizi» darajasida.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_22_24.py --master=prime \\
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
# PM-22 — kasr ↔ oʻnlik ↔ foiz
# =====================================================================

Q_PM22 = [
    # 1–5 tanish
    {
        "text": "<p>Foizda yozing.</p><p><strong>0,25 = ?</strong></p>",
        "choices": ["0,25%", "2,5%", "25%", "250%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> Oʻnlikdan foizga oʻtish uchun 100 ga "
                       "koʻpaytiramiz, yaʼni vergulni ikki xona oʻngga suramiz: "
                       "0,25 → 25. <strong>2,5%</strong> — vergulni bitta xonaga "
                       "surganda chiqadigan xato.</p>",
    },
    {
        "text": "<p>Foizda yozing.</p><p><strong>1/2 = ?</strong></p>",
        "choices": ["2%", "12%", "50%", "100%"],
        "correct": "50%",
        "explanation": "<p><strong>50%.</strong> 1 ÷ 2 = 0,5; 0,5 × 100 = 50. Yarim — "
                       "yuzta katakning ellikkasi. <strong>100%</strong> — butunning "
                       "oʻzi, yarmi emas.</p>",
    },
    {
        "text": "<p>Oʻnlik kasrda yozing.</p><p><strong>40% = ?</strong></p>",
        "choices": ["0,04", "0,4", "4,0", "40,0"],
        "correct": "0,4",
        "explanation": "<p><strong>0,4.</strong> Foizdan oʻnlikka oʻtish — 100 ga "
                       "boʻlish, yaʼni vergul ikki xona chapga: 40 → 0,40 = 0,4. "
                       "<strong>0,04</strong> — vergul uch xona surilganda chiqadi.</p>",
    },
    {
        "text": "<p>Oʻnlik kasrda yozing.</p><p><strong>7% = ?</strong></p>",
        "choices": ["0,007", "0,07", "0,7", "7,0"],
        "correct": "0,07",
        "explanation": "<p><strong>0,07.</strong> 7 ÷ 100 = 0,07. Yuzta katakdan "
                       "yettitasi — juda kichik ulush. <strong>0,7</strong> esa 70% "
                       "boʻlar edi, yaʼni butunning katta qismi.</p>",
    },
    {
        "text": "<p>Foizda yozing.</p><p><strong>3/4 = ?</strong></p>",
        "choices": ["34%", "43%", "75%", "80%"],
        "correct": "75%",
        "explanation": "<p><strong>75%.</strong> 3 ÷ 4 = 0,75; 0,75 × 100 = 75. Uch "
                       "chorak — soatning 45 daqiqasi. <strong>34%</strong> — surat "
                       "va maxrajni shunchaki yonma-yon yozib yuborishdan chiqadi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Oʻnlik kasrda yozing.</p><p><strong>3/8 = ?</strong></p>",
        "choices": ["0,038", "0,375", "0,38", "3,8"],
        "correct": "0,375",
        "explanation": "<p><strong>0,375.</strong> 3 ÷ 8: 30 ÷ 8 = 3 (qoldiq 6), "
                       "60 ÷ 8 = 7 (qoldiq 4), 40 ÷ 8 = 5. Qoldiq nolga aylandi — "
                       "boʻlish tugadi. <strong>0,38</strong> — yaxlitlangan qiymat, "
                       "aniq javob emas.</p>",
    },
    {
        "text": "<p>Foizda yozing.</p><p><strong>5/8 = ?</strong></p>",
        "choices": ["58%", "62,5%", "80%", "85%"],
        "correct": "62,5%",
        "explanation": "<p><strong>62,5%.</strong> 5 ÷ 8 = 0,625; vergulni ikki xona "
                       "oʻngga surdik. Foiz butun son boʻlishi shart emas. "
                       "<strong>58%</strong> — surat va maxrajni yonma-yon yozishdan "
                       "chiqadigan xato.</p>",
    },
    {
        "text": "<p>Foizda yozing.</p><p><strong>0,06 = ?</strong></p>",
        "choices": ["0,6%", "6%", "60%", "600%"],
        "correct": "6%",
        "explanation": "<p><strong>6%.</strong> 0,06 × 100 = 6. Yuzdan olti boʻlak. "
                       "<strong>60%</strong> — 0,6 ning foizi; noldan keyingi nolni "
                       "eʼtiborsiz qoldirish shu xatoga olib keladi.</p>",
    },
    {
        "text": "<p>Qisqartirilgan oddiy kasr koʻrinishida yozing.</p>"
                "<p><strong>12% = ?</strong></p>",
        "choices": ["1/12", "3/25", "6/50", "12/10"],
        "correct": "3/25",
        "explanation": "<p><strong>3/25.</strong> 12% = 12/100; surat va maxrajni 4 ga "
                       "boʻldik. <strong>6/50</strong> ham 12% ga teng, lekin toʻliq "
                       "qisqartirilmagan — 6 va 50 hali ham 2 ga boʻlinadi.</p>",
    },
    {
        "text": "<p>Foizda yozing.</p><p><strong>1,25 = ?</strong></p>",
        "choices": ["1,25%", "12,5%", "125%", "1250%"],
        "correct": "125%",
        "explanation": "<p><strong>125%.</strong> 1,25 × 100 = 125. Butundan katta son "
                       "100 foizdan katta foiz beradi — bu xato emas: 1,25 bir butun "
                       "va chorak.</p>",
    },
    {
        "text": "<p>Foizda yozing.</p><p><strong>2/5 = ?</strong></p>",
        "choices": ["2,5%", "25%", "40%", "52%"],
        "correct": "40%",
        "explanation": "<p><strong>40%.</strong> Eng qisqa yoʻl — maxrajni 100 ga "
                       "keltirish: 2/5 = 40/100 = 40%. <strong>25%</strong> — 2/5 ni "
                       "1/4 bilan chalkashtirishdan chiqadi.</p>",
    },
    {
        "text": "<p>Qisqartirilgan oddiy kasr koʻrinishida yozing.</p>"
                "<p><strong>0,8 = ?</strong></p>",
        "choices": ["1/8", "4/5", "8/10", "8/100"],
        "correct": "4/5",
        "explanation": "<p><strong>4/5.</strong> 0,8 = 8/10, surat va maxrajni 2 ga "
                       "boʻldik. <strong>8/100</strong> — 0,08 ga teng, chunki maxraj "
                       "vergul ortidagi xonalar soniga qarab tanlanadi: bitta xona — "
                       "10, ikkita xona — 100.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi biri katta: 3/5 yoki "
                "58%?</strong></p>",
        "choices": ["3/5 katta", "58% katta", "Ular teng", "Taqqoslab boʻlmaydi"],
        "correct": "3/5 katta",
        "explanation": "<p><strong>3/5 katta.</strong> Taqqoslash uchun bitta qiyofaga "
                       "keltiramiz: 3/5 = 6/10 = 0,6 = 60%. 60% &gt; 58%. Har xil "
                       "koʻrinishdagi sonlarni «taqqoslab boʻlmaydi» degan javob "
                       "notoʻgʻri — aynan shuning uchun aylantirishni oʻrganamiz.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi juftlik teng "
                "EMAS?</strong></p>",
        "choices": ["1/4 va 25%", "1/5 va 15%", "0,2 va 20%", "0,75 va 75%"],
        "correct": "1/5 va 15%",
        "explanation": "<p><strong>1/5 va 15%</strong> teng emas: 1 ÷ 5 = 0,2, yaʼni "
                       "1/5 = 20%. 15% deb yozish — surat va maxrajni yonma-yon "
                       "qoʻyishdan kelib chiqadigan xato. Qolgan uch juftlik toʻgʻri.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi biri eng "
                "kichik?</strong></p>",
        "choices": ["1/4", "27%", "3/10", "0,35"],
        "correct": "1/4",
        "explanation": "<p><strong>1/4</strong> eng kichik. Hammasini foizga "
                       "aylantiramiz: 1/4 = 25%, 27% = 27%, 3/10 = 30%, 0,35 = 35%. "
                       "Eng kichigi 25%. Koʻrinishi har xil sonlarni koʻz bilan "
                       "taqqoslash mumkin emas — avval bitta qiyofaga keltiring.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>100% qaysi songa "
                "teng?</strong></p>",
        "choices": ["0,01", "0,1", "1", "100"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> 100% = 100 ÷ 100 = 1, yaʼni butunning "
                       "oʻzi. <strong>100</strong> — foiz belgisini tushirib "
                       "qoldirishdan chiqadi; <strong>0,01</strong> esa 1% ga teng.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>1/5 = 1 ÷ 5 = 0,15 = 15%"
                "</strong></p>",
        "choices": [
            "Boʻlishda: 1 ÷ 5 = 0,2 boʻlishi kerak",
            "Foizga oʻtishda: 0,15 = 1,5% boʻlishi kerak",
            "Kasr chizigʻini boʻlish deb olishda",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Boʻlishda: 1 ÷ 5 = 0,2 boʻlishi kerak",
        "explanation": "<p><strong>Boʻlishda xato.</strong> 1 ÷ 5 = 0,2, demak "
                       "1/5 = 20%. Surat va maxrajni yonma-yon yozib «0,15» qilish — "
                       "eng koʻp uchraydigan xato. Tekshirish oson: 1/5 beshdan bir, "
                       "1/4 esa 25% — beshdan bir chorakdan sal kichik boʻlishi "
                       "kerak, 15% esa juda uzoq.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>0,07 ni foizga "
                "aylantirish</strong></p>",
        "choices": ["0,07 = 0,7%", "0,07 = 7%", "0,07 = 70%", "0,07 = 700%"],
        "correct": "0,07 = 7%",
        "explanation": "<p><strong>0,07 = 7%.</strong> Vergul ikki xona oʻngga "
                       "suriladi: 0,07 → 7. <strong>0,7%</strong> — bitta xona, "
                       "<strong>700%</strong> — uchta xona surilganda chiqadi. "
                       "Nazorat: 0,07 juda kichik son, demak foizi ham kichik "
                       "boʻlishi kerak.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Uch doʻkon bir xil kurtkani bir xil narxda sotmoqda. «Bahor» "
                "narxning 1/4 qismini chegirma qilyapti, «Chorsu» 0,2 qismini, "
                "«Yangi bozor» esa 30 foizini.</p>"
                "<p><strong>Qaysi doʻkonda chegirma eng katta?</strong></p>",
        "choices": ["«Bahor»", "«Chorsu»", "«Yangi bozor»", "Uchalasida bir xil"],
        "correct": "«Yangi bozor»",
        "explanation": "<p><strong>«Yangi bozor».</strong> Narx hamma joyda bir xil, "
                       "shuning uchun faqat ulushlarni taqqoslash yetarli: "
                       "1/4 = 25%, 0,2 = 20%, 30% = 30%. Eng kattasi 30%. "
                       "Tekshirish: narx 200 000 soʻm boʻlsa, chegirmalar 50 000, "
                       "40 000 va 60 000 soʻm boʻladi.</p>",
    },
    {
        "text": "<p>Bekzod kitobning 0,35 qismini oʻqidi. Dilnoza xuddi shu kitobning "
                "2/5 qismini oʻqidi.</p>"
                "<p><strong>Kim koʻproq oʻqigan?</strong></p>",
        "choices": ["Bekzod", "Dilnoza", "Ikkalasi teng", "Aniqlab boʻlmaydi"],
        "correct": "Dilnoza",
        "explanation": "<p><strong>Dilnoza.</strong> Kitob bitta va bir xil, demak "
                       "ulushlarni taqqoslaymiz: 0,35 = 35%, 2/5 = 0,4 = 40%. "
                       "40% &gt; 35%. Bet soni berilmagan boʻlsa ham javob topiladi — "
                       "ulush butunning oʻlchamiga bogʻliq emas.</p>",
    },
]


# =====================================================================
# PM-23 — sonning foizini topish
# =====================================================================

Q_PM23 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>100 ning 30% i = ?</strong></p>",
        "choices": ["3", "30", "300", "3000"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> 100 × 0,3 = 30. Butun aynan 100 "
                       "boʻlganda foiz va qism bir xil son boʻladi — foiz «yuzdan "
                       "boʻlak» degani shu.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>200 ning 10% i = ?</strong></p>",
        "choices": ["2", "20", "100", "2000"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> 10% — oʻndan bir: 200 ÷ 10 = 20. Bu "
                       "eng oson foiz, uni doim boʻlish bilan toping.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>80 ning 50% i = ?</strong></p>",
        "choices": ["8", "16", "40", "160"],
        "correct": "40",
        "explanation": "<p><strong>40.</strong> 50% — yarim: 80 ÷ 2 = 40. "
                       "<strong>160</strong> — koʻpaytirib yuborishdan chiqadi, lekin "
                       "yarim butundan katta boʻlishi mumkin emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>60 ning 25% i = ?</strong></p>",
        "choices": ["6", "15", "24", "150"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> 25% — chorak: 60 ÷ 4 = 15. Yoki "
                       "60 × 0,25 = 15.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>500 ning 1% i = ?</strong></p>",
        "choices": ["0,5", "5", "50", "500"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 1% — yuzdan bir: 500 ÷ 100 = 5. Bir "
                       "foizni topish barcha foiz hisoblarining kalitidir.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>240 ning 30% i = ?</strong></p>",
        "choices": ["8", "72", "80", "720"],
        "correct": "72",
        "explanation": "<p><strong>72.</strong> 240 × 0,3 = 72 (24 × 3 = 72). "
                       "<strong>8</strong> — 240 ni 30 ga boʻlishdan chiqadi: foizga "
                       "boʻlish mumkin emas, faqat 100 ga.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>4500 ning 20% i = ?</strong></p>",
        "choices": ["225", "450", "900", "9000"],
        "correct": "900",
        "explanation": "<p><strong>900.</strong> 20% — beshdan bir: 4500 ÷ 5 = 900. "
                       "Yoki 1% = 45, 45 × 20 = 900. <strong>450</strong> — 10% i, "
                       "yaʼni yarmi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>350 ning 8% i = ?</strong></p>",
        "choices": ["2,8", "28", "280", "2800"],
        "correct": "28",
        "explanation": "<p><strong>28.</strong> 1% = 350 ÷ 100 = 3,5; 3,5 × 8 = 28. "
                       "Yoki 350 × 0,08 = 28.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>60 000 ning 15% i = ?</strong></p>",
        "choices": ["900", "6000", "9000", "90 000"],
        "correct": "9000",
        "explanation": "<p><strong>9000.</strong> Eng qulay yoʻl — 15% ni boʻlaklarga "
                       "ajratish: 10% = 6000, 5% = 3000 (oʻndan birning yarmi), "
                       "jami 9000. Tekshirish: 60 000 × 0,15 = 9000.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1200 ning 45% i = ?</strong></p>",
        "choices": ["54", "480", "540", "5400"],
        "correct": "540",
        "explanation": "<p><strong>540.</strong> 1% = 12; 12 × 45 = 540. Yoki "
                       "1200 × 0,45 = 540. Yana bir yoʻl: 50% = 600, undan 5% = 60 ni "
                       "ayiramiz — 540.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>90 ning 120% i = ?</strong></p>",
        "choices": ["75", "90", "108", "1080"],
        "correct": "108",
        "explanation": "<p><strong>108.</strong> 120% = 1,2, demak 90 × 1,2 = 108. "
                       "Javob butundan katta chiqishi kerak edi, chunki foiz 100 dan "
                       "katta — bu nazoratni har doim qiling.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2500 ning 6% i = ?</strong></p>",
        "choices": ["15", "150", "250", "1500"],
        "correct": "150",
        "explanation": "<p><strong>150.</strong> 1% = 25; 25 × 6 = 150. Yoki "
                       "2500 × 0,06 = 150.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi biri katta: 400 ning "
                "25% i yoki 300 ning 40% i?</strong></p>",
        "choices": [
            "400 ning 25% i",
            "300 ning 40% i",
            "Ular teng",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "300 ning 40% i",
        "explanation": "<p><strong>300 ning 40% i katta.</strong> 400 × 0,25 = 100, "
                       "300 × 0,4 = 120. 120 &gt; 100. Katta foiz kichik sondan "
                       "olinsa ham koʻproq chiqishi mumkin — foizni butunsiz "
                       "taqqoslab boʻlmaydi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Mahsulot 40 000 soʻm turadi, unga 25% "
                "chegirma eʼlon qilindi.</p><p><strong>CHEGIRMA necha soʻm?</strong></p>",
        "choices": ["4000 soʻm", "10 000 soʻm", "25 000 soʻm", "30 000 soʻm"],
        "correct": "10 000 soʻm",
        "explanation": "<p><strong>10 000 soʻm.</strong> Chegirma — narxning 25 foizi: "
                       "40 000 ÷ 4 = 10 000. <strong>30 000</strong> — toʻlanadigan "
                       "pul, chegirmaning oʻzi emas. Savol nimani soʻrayotganini "
                       "diqqat bilan oʻqing.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>600 ning 10% i bilan 6% i orasidagi farq "
                "qancha?</strong></p>",
        "choices": ["4", "24", "36", "60"],
        "correct": "24",
        "explanation": "<p><strong>24.</strong> 10% = 60, 6% = 36; farqi 60 − 36 = 24. "
                       "<strong>4</strong> — foizlarning farqini (10 − 6) javob deb "
                       "olishdan chiqadi, lekin 4% ning oʻzi 24 ga teng.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi hisob 150 ning 20% ini "
                "beradi?</strong></p>",
        "choices": ["150 ÷ 20", "150 × 0,2", "150 × 20", "150 + 0,2"],
        "correct": "150 × 0,2",
        "explanation": "<p><strong>150 × 0,2 = 30.</strong> Foizni avval oʻnlik kasrga "
                       "aylantirib, songa koʻpaytiramiz. <strong>150 × 20</strong> "
                       "yuz baravar katta javob beradi, <strong>150 ÷ 20</strong> esa "
                       "foizga boʻlish — bunday amal yoʻq.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>700 ning 15% i: "
                "700 × 15 = 10 500</strong></p>",
        "choices": [
            "Foiz oʻnlik kasrga aylantirilmagan: 700 × 0,15 = 105",
            "Koʻpaytirish oʻrniga boʻlish kerak edi: 700 ÷ 15",
            "700 ni avval 15 ga qoʻshish kerak edi",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Foiz oʻnlik kasrga aylantirilmagan: 700 × 0,15 = 105",
        "explanation": "<p><strong>Foiz belgisi tushirib qoldirilgan.</strong> 15% = "
                       "0,15, demak 700 × 0,15 = 105. Javob 10 500 butunning oʻzidan "
                       "15 baravar katta — foiz 100 dan kichik boʻlsa, qism butundan "
                       "katta boʻlolmaydi.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>900 ning 3% i</strong></p>",
        "choices": [
            "900 ÷ 3 = 300",
            "900 ÷ 100 = 9; 9 × 3 = 27",
            "900 × 3 = 2700",
            "900 ÷ 100 = 9; 9 ÷ 3 = 3",
        ],
        "correct": "900 ÷ 100 = 9; 9 × 3 = 27",
        "explanation": "<p><strong>27</strong> toʻgʻri. Avval 1% ni topamiz "
                       "(900 ÷ 100 = 9), keyin uni 3 ga koʻpaytiramiz. "
                       "<strong>900 ÷ 3</strong> — foizga boʻlish xatosi; "
                       "<strong>900 × 3</strong> — foiz belgisini unutish.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Afsonaning 240 000 soʻmi bor edi. U pulining 30 foiziga kitob "
                "oldi.</p><p><strong>Kitob necha soʻm turdi?</strong></p>",
        "choices": ["8000 soʻm", "72 000 soʻm", "168 000 soʻm", "720 000 soʻm"],
        "correct": "72 000 soʻm",
        "explanation": "<p><strong>72 000 soʻm.</strong> «Pulining 30 foizi» — "
                       "koʻpaytirish: 240 000 × 0,3 = 72 000. <strong>168 000</strong> "
                       "— kitobdan keyin qolgan pul (240 000 − 72 000), savol esa "
                       "kitobning narxini soʻragan. <strong>8000</strong> — 240 000 ni "
                       "30 ga boʻlishdan chiqadi.</p>",
    },
    {
        "text": "<p>Maktabda 750 oʻquvchi bor. Ulardan 12 foizi sport toʻgaragiga "
                "qatnaydi.</p><p><strong>Nechta oʻquvchi sport toʻgaragiga "
                "qatnaydi?</strong></p>",
        "choices": ["62 ta", "75 ta", "90 ta", "120 ta"],
        "correct": "90 ta",
        "explanation": "<p><strong>90 ta.</strong> 1% = 750 ÷ 100 = 7,5; "
                       "7,5 × 12 = 90. Yoki 750 × 0,12 = 90. <strong>75</strong> — "
                       "10% i, yaʼni foizni yaxlitlab yuborishdan chiqadi. Taxmin: "
                       "12% oʻndan birdan sal koʻp, demak javob 75 dan biroz katta "
                       "boʻlishi kerak.</p>",
    },
]


# =====================================================================
# PM-24 — foizdan butunni topish va «necha foiz?»
# =====================================================================

Q_PM24 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>10 — 20 ning necha foizi?</strong></p>",
        "choices": ["10%", "20%", "50%", "200%"],
        "correct": "50%",
        "explanation": "<p><strong>50%.</strong> Qismni butunga boʻlamiz: "
                       "10 ÷ 20 = 0,5; 0,5 × 100 = 50. Yarmi — 50 foiz.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>10 — 40 ning necha foizi?</strong></p>",
        "choices": ["4%", "10%", "25%", "40%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> 10 ÷ 40 = 0,25 = 25%. 10 — 40 ning "
                       "choragi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>20 — 200 ning necha foizi?</strong></p>",
        "choices": ["2%", "10%", "20%", "100%"],
        "correct": "10%",
        "explanation": "<p><strong>10%.</strong> 20 ÷ 200 = 0,1 = 10%. "
                       "<strong>20%</strong> — qismning oʻzini foiz deb olishdan "
                       "chiqadi; qism va foiz faqat butun 100 boʻlgandagina bir xil "
                       "son boʻladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>5 — 25 ning necha foizi?</strong></p>",
        "choices": ["5%", "20%", "25%", "500%"],
        "correct": "20%",
        "explanation": "<p><strong>20%.</strong> 5 ÷ 25 = 0,2 = 20%. Yoki maxrajni "
                       "100 ga keltiramiz: 5/25 = 20/100 = 20%.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Sonning 50% i 30. Son "
                "qancha?</strong></p>",
        "choices": ["15", "30", "60", "150"],
        "correct": "60",
        "explanation": "<p><strong>60.</strong> 50% — yarim, demak son ikki baravar "
                       "katta: 30 × 2 = 60. <strong>15</strong> — 30 ning yarmi, "
                       "yaʼni koʻpaytirish oʻrniga boʻlishdan chiqadi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>45 — 60 ning necha foizi?</strong></p>",
        "choices": ["45%", "60%", "75%", "133%"],
        "correct": "75%",
        "explanation": "<p><strong>75%.</strong> 45/60 = 3/4 = 0,75 = 75%. "
                       "<strong>133%</strong> — boʻlishni teskari qilishdan "
                       "(60 ÷ 45) chiqadi; qism butundan kichik boʻlsa, javob 100% "
                       "dan kichik boʻlishi shart.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>34 — 40 ning necha foizi?</strong></p>",
        "choices": ["34%", "76%", "85%", "118%"],
        "correct": "85%",
        "explanation": "<p><strong>85%.</strong> 34 ÷ 40 = 0,85 = 85%. Qisqartirib ham "
                       "boʻladi: 34/40 = 17/20 = 85/100.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>7 — 20 ning necha foizi?</strong></p>",
        "choices": ["7%", "14%", "35%", "70%"],
        "correct": "35%",
        "explanation": "<p><strong>35%.</strong> Maxrajni 100 ga keltiramiz: "
                       "7/20 = 35/100 = 35%. Yoki 7 ÷ 20 = 0,35.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Sonning 12% i 9000. Son "
                "qancha?</strong></p>",
        "choices": ["1080", "10 800", "75 000", "108 000"],
        "correct": "75 000",
        "explanation": "<p><strong>75 000.</strong> 1% = 9000 ÷ 12 = 750; "
                       "100% = 750 × 100 = 75 000. Yoki 9000 ÷ 0,12 = 75 000. "
                       "<strong>1080</strong> — koʻpaytirishdan chiqadi, lekin butun "
                       "oʻz boʻlagidan kichik boʻlolmaydi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Sonning 30% i 60. Son "
                "qancha?</strong></p>",
        "choices": ["18", "90", "180", "200"],
        "correct": "200",
        "explanation": "<p><strong>200.</strong> 1% = 60 ÷ 30 = 2; 100% = 200. Yoki "
                       "60 ÷ 0,3 = 200. Tekshirish: 200 × 0,3 = 60 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Sonning 5% i 15. Son "
                "qancha?</strong></p>",
        "choices": ["0,75", "20", "75", "300"],
        "correct": "300",
        "explanation": "<p><strong>300.</strong> 1% = 15 ÷ 5 = 3; 100% = 300. Kichik "
                       "foiz katta butunni anglatadi: 5% atigi yigirmadan bir.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Sonning 40% i 24 000. Son "
                "qancha?</strong></p>",
        "choices": ["9600", "48 000", "60 000", "600 000"],
        "correct": "60 000",
        "explanation": "<p><strong>60 000.</strong> 1% = 24 000 ÷ 40 = 600; "
                       "100% = 60 000. Tekshirish: 60 000 × 0,4 = 24 000 ✓ "
                       "<strong>48 000</strong> — 40% ni yarim deb olishdan chiqadi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Hisoblang.</p><p><strong>80 — 200 ning necha foizi?</strong></p>",
        "choices": ["8%", "40%", "80%", "250%"],
        "correct": "40%",
        "explanation": "<p><strong>40%.</strong> 80 ÷ 200 = 0,4 = 40%. "
                       "<strong>250%</strong> — boʻlishni teskari qilishdan "
                       "(200 ÷ 80) chiqadi. Doim qismni butunga boʻling: «ning» "
                       "soʻzidan oldingi son — butun.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Sonning 20% i 40. Son "
                "qancha?</strong></p>",
        "choices": ["8", "20", "80", "200"],
        "correct": "200",
        "explanation": "<p><strong>200.</strong> Bu «butunni topish» savoli, demak "
                       "boʻlamiz: 40 ÷ 0,2 = 200. <strong>8</strong> — 40 ning 20% i, "
                       "yaʼni savolni teskari oʻqishdan chiqadi: bu yerda 40 — qism, "
                       "butun emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Necha foiz?» savoliga "
                "qaysi hisob javob beradi?</strong></p>",
        "choices": [
            "butun ÷ qism × 100",
            "butun − qism",
            "qism × butun ÷ 100",
            "qism ÷ butun × 100",
        ],
        "correct": "qism ÷ butun × 100",
        "explanation": "<p><strong>qism ÷ butun × 100.</strong> Foiz — ulush, ulush "
                       "esa qism/butun degan kasr; uni foizga aylantirish uchun 100 ga "
                       "koʻpaytiramiz. <strong>butun ÷ qism</strong> — eng koʻp "
                       "uchraydigan teskari boʻlish xatosi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi holatda «necha "
                "foiz?» savolining javobi 100% dan katta boʻladi?</strong></p>",
        "choices": [
            "Qism butundan katta boʻlsa",
            "Qism butundan kichik boʻlsa",
            "Qism nolga teng boʻlsa",
            "Hech qachon boʻlmaydi",
        ],
        "correct": "Qism butundan katta boʻlsa",
        "explanation": "<p><strong>Qism butundan katta boʻlsa.</strong> Masalan "
                       "30 — 20 ning 150 foizi, chunki 30 ÷ 20 = 1,5. Bunday holat "
                       "hayotda ham uchraydi: bu yilgi hosil oʻtgan yilgining 120 "
                       "foizi. 100% — butunning oʻzi, undan kattasi butundan "
                       "oshganini bildiradi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>18 — 30 ning necha foizi? "
                "30 ÷ 18 × 100 ≈ 167%</strong></p>",
        "choices": [
            "Boʻlish teskari: 18 ÷ 30 × 100 = 60% boʻlishi kerak",
            "100 ga koʻpaytirish ortiqcha",
            "Boʻlish oʻrniga ayirish kerak edi",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Boʻlish teskari: 18 ÷ 30 × 100 = 60% boʻlishi kerak",
        "explanation": "<p><strong>Boʻlish teskari qilingan.</strong> Qismni butunga "
                       "boʻlamiz: 18 ÷ 30 = 0,6 = 60%. Nazorat: 18 — 30 dan kichik, "
                       "demak javob 100% dan kichik boʻlishi shart edi; 167% esa "
                       "darrov xato ekanini koʻrsatib turibdi.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Sonning 8% i 24. Son "
                "qancha?</strong></p>",
        "choices": [
            "24 × 0,08 = 1,92",
            "24 ÷ 8 = 3; 3 × 100 = 300",
            "24 × 8 = 192",
            "24 ÷ 100 × 8 = 1,92",
        ],
        "correct": "24 ÷ 8 = 3; 3 × 100 = 300",
        "explanation": "<p><strong>300</strong> toʻgʻri: avval 1% ni topamiz "
                       "(24 ÷ 8 = 3), keyin 100 ga koʻpaytiramiz. Tekshirish: "
                       "300 × 0,08 = 24 ✓ Qolgan uch yoʻl ham koʻpaytirishga tayanadi, "
                       "lekin butunni topish — boʻlish amali.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Jasur imtihonda 40 ta savoldan 34 tasini toʻgʻri ishladi. Maktab "
                "natijani foizda eʼlon qiladi.</p>"
                "<p><strong>Jasurning natijasi necha foiz?</strong></p>",
        "choices": ["34%", "60%", "85%", "118%"],
        "correct": "85%",
        "explanation": "<p><strong>85%.</strong> Qism — 34, butun — 40: "
                       "34 ÷ 40 = 0,85 = 85%. Tekshirish teskari amal bilan: "
                       "40 × 0,85 = 34 ✓ <strong>34%</strong> — toʻgʻri javoblar "
                       "sonini foiz deb olishdan chiqadi.</p>",
    },
    {
        "text": "<p>Sherbek lugʻat buyurtma qildi va narxning 40 foizini oldindan "
                "toʻladi. Oldindan toʻlov 24 000 soʻm boʻldi.</p>"
                "<p><strong>Lugʻat necha soʻm turadi?</strong></p>",
        "choices": ["9600 soʻm", "36 000 soʻm", "60 000 soʻm", "96 000 soʻm"],
        "correct": "60 000 soʻm",
        "explanation": "<p><strong>60 000 soʻm.</strong> 40% = 24 000, demak "
                       "1% = 24 000 ÷ 40 = 600 va 100% = 60 000. "
                       "<strong>36 000</strong> — qolgan toʻlov (60 000 − 24 000), "
                       "narxning oʻzi emas; <strong>9600</strong> — 24 000 ni 0,4 ga "
                       "koʻpaytirishdan chiqadi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-22 Mashq: Kasr ↔ oʻnlik ↔ foiz",
        "description": "20 savol — kasrni oʻnlikka, oʻnlikni foizga aylantirish, "
                       "foizdan qisqartirilgan kasrga qaytish va taqqoslash.",
        "tutorial":    "PM-22:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM22,
    },
    {
        "title":       "PM-23 Mashq: Sonning foizini topish",
        "description": "20 savol — foizni oʻnlik kasrga aylantirib koʻpaytirish, "
                       "1% orqali hisoblash va oson foizlarning yoʻllari.",
        "tutorial":    "PM-23:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM23,
    },
    {
        "title":       "PM-24 Mashq: Foizdan butunni topish",
        "description": "20 savol — «necha foiz?» savoli, foizi maʼlum boʻlganda "
                       "butunni tiklash va uch turdagi foiz savolini ajratish.",
        "tutorial":    "PM-24:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM24,
    },
]
