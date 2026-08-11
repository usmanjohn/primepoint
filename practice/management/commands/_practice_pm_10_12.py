# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-10 … PM-12 (manfiy sonlar bilan amallar, daraja).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ `text` maydoni |safe bilan chiqadi — HTML yozish mumkin (<sup>, <strong>).
   `choices` esa avtomatik ekranlanadi — u yerda HTML teg ISHLAMAYDI, shuning
   uchun darajalar Yunikod belgilari bilan yoziladi: ², ³, ⁴, ⁵.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_10_12.py --master=prime \\
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
# PM-10 — manfiy sonlarni qoʻshish va ayirish
# =====================================================================

Q_PM10 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>−6 + 2 = ?</strong></p>",
        "choices": ["−8", "−4", "4", "8"],
        "correct": "−4",
        "explanation": "<p><strong>−4.</strong> Ishoralar har xil, demak sonlar "
                       "bir-biriga qarshi yuradi: 6 − 2 = 4. Nol dan uzoqrogʻi (6) "
                       "manfiy — javob ham manfiy.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−3 + (−7) = ?</strong></p>",
        "choices": ["−10", "−4", "4", "10"],
        "correct": "−10",
        "explanation": "<p><strong>−10.</strong> Ikkala son ham manfiy — ikkala qadam "
                       "ham chapga: 3 + 7 = 10 qadam chapga.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>5 − 9 = ?</strong></p>",
        "choices": ["−14", "−4", "4", "14"],
        "correct": "−4",
        "explanation": "<p><strong>−4.</strong> 5 + (−9) ga aylantiramiz: 9 − 5 = 4, "
                       "uzoqrogʻi manfiy.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−8 + 8 = ?</strong></p>",
        "choices": ["−16", "−8", "0", "16"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> −8 va 8 — qarama-qarshi sonlar. Chapga "
                       "8 qadam, keyin oʻngga 8 qadam: aynan nolga qaytamiz.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>7 + (−2) = ?</strong></p>",
        "choices": ["−9", "−5", "5", "9"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Manfiy son qoʻshilishi — chapga qadam: "
                       "7 dan 2 qadam chapga borsak, 5 boʻladi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>−12 + 5 = ?</strong></p>",
        "choices": ["−17", "−7", "7", "17"],
        "correct": "−7",
        "explanation": "<p><strong>−7.</strong> Ishoralar har xil: 12 − 5 = 7. Uzoqrogʻi "
                       "manfiy 12 — javob manfiy. −17 javobi ikkala sonni chapga "
                       "yurgizib yuborganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−4 − 9 = ?</strong></p>",
        "choices": ["−13", "−5", "5", "13"],
        "correct": "−13",
        "explanation": "<p><strong>−13.</strong> −4 + (−9): ikkala harakat ham chapga, "
                       "shuning uchun qoʻshiladi. 5 javobi ishoralarni «bir-birini "
                       "yeydi» deb oʻylaganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>10 − (−3) = ?</strong></p>",
        "choices": ["−13", "−7", "7", "13"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> Manfiy sonni ayirish — uni qoʻshish: "
                       "10 + 3 = 13. Ikki minus yonma-yon kelib plus berdi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−15 + 20 = ?</strong></p>",
        "choices": ["−35", "−5", "5", "35"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 20 − 15 = 5, uzoqrogʻi musbat 20 — javob "
                       "musbat.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−7 − (−2) = ?</strong></p>",
        "choices": ["−9", "−5", "5", "9"],
        "correct": "−5",
        "explanation": "<p><strong>−5.</strong> −7 + 2 ga aylanadi: 7 − 2 = 5, uzoqrogʻi "
                       "manfiy. −9 javobi qavsni ochmasdan qoʻshib yuborganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−8 + 15 − 4 = ?</strong></p>",
        "choices": ["−27", "−3", "3", "27"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Chapdan oʻngga: −8 + 15 = 7, keyin "
                       "7 − 4 = 3.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>0 − 14 = ?</strong></p>",
        "choices": ["−14", "0", "1", "14"],
        "correct": "−14",
        "explanation": "<p><strong>−14.</strong> Noldan 14 qadam chapga — bu −14. "
                       "Noldan ayirish har doim qarama-qarshi sonni beradi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Hisoblamasdan, faqat ishoraga qarab aniqlang.</p>"
                "<p><strong>Qaysi ifodaning qiymati musbat?</strong></p>",
        "choices": ["−8 + 3", "−5 − 2", "4 − 9", "−3 + 10"],
        "correct": "−3 + 10",
        "explanation": "<p><strong>−3 + 10 = 7.</strong> Bu yerda musbat son nol dan "
                       "uzoqroq. Qolganlari: −8 + 3 = −5, −5 − 2 = −7, 4 − 9 = −5 — "
                       "hammasi manfiy.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>−5 − 3 ifodasi qaysi "
                "ifodaga teng?</strong></p>",
        "choices": ["−(5 − 3)", "−5 + (−3)", "−5 + 3", "5 − 3"],
        "correct": "−5 + (−3)",
        "explanation": "<p><strong>−5 + (−3).</strong> Ayirish — qarama-qarshi sonni "
                       "qoʻshish: a − b = a + (−b). Ikkalasi ham −8 beradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi ifodaning qiymati "
                "eng kichik?</strong></p>",
        "choices": ["−4 − 4", "−9 + 2", "−3 − 3", "1 − 8"],
        "correct": "−4 − 4",
        "explanation": "<p><strong>−4 − 4 = −8.</strong> Qolganlari: −9 + 2 = −7, "
                       "−3 − 3 = −6, 1 − 8 = −7. Son oʻqida eng chapda turgani — "
                       "eng kichigi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>6 − (−4) ifodasi qaysi "
                "amalga teng?</strong></p>",
        "choices": ["−6 − 4", "−6 + 4", "6 − 4", "6 + 4"],
        "correct": "6 + 4",
        "explanation": "<p><strong>6 + 4 = 10.</strong> Manfiy sonni ayirsak, uni "
                       "qoʻshgan boʻlamiz. 6 − 4 = 2 javobi qavsdagi minusni "
                       "unutganda chiqadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Afsona shunday yozdi: <strong>−9 + 4 = −13</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Ishoralar har xil boʻlgani uchun sonlar ayirilishi kerak edi: javob −5",
            "Hech qanday xato yoʻq, javob toʻgʻri",
            "Javob musbat boʻlishi kerak edi: 13",
            "Javob nol boʻlishi kerak edi",
        ],
        "correct": "Ishoralar har xil boʻlgani uchun sonlar ayirilishi kerak edi: javob −5",
        "explanation": "<p><strong>−9 + 4 = −5.</strong> Afsona ikkala sonni ham chapga "
                       "yurgizib, 9 + 4 = 13 deb qoʻshib yuborgan. Aslida musbat 4 "
                       "bizni oʻngga qaytaradi: 9 − 4 = 5, ishora manfiy.</p>",
    },
    {
        "text": "<p>Jasur shunday yozdi: <strong>7 − (−5) = 2</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Javob −12 boʻlishi kerak edi",
            "Javob −2 boʻlishi kerak edi",
            "Hech qanday xato yoʻq, javob toʻgʻri",
            "Manfiy sonni ayirish — uni qoʻshish demak: 7 + 5 = 12",
        ],
        "correct": "Manfiy sonni ayirish — uni qoʻshish demak: 7 + 5 = 12",
        "explanation": "<p><strong>7 − (−5) = 12.</strong> Jasur qavsdagi minusni "
                       "koʻrmay, 7 − 5 deb hisoblagan. Ikki minus yonma-yon kelsa, "
                       "plus boʻladi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Nukusda ertalab harorat <strong>−11 °C</strong> edi. Kunduzi havo "
                "<strong>14 daraja isidi</strong>, kechasi esa yana <strong>9 daraja "
                "sovidi</strong>.</p>"
                "<p><strong>Kechasi harorat necha daraja boʻldi?</strong></p>",
        "choices": ["−34 °C", "−6 °C", "3 °C", "12 °C"],
        "correct": "−6 °C",
        "explanation": "<p><strong>−6 °C.</strong> Isish — qoʻshish: −11 + 14 = 3. "
                       "Sovish — ayirish: 3 − 9 = −6. Kechasi havo yana noldan pastga "
                       "tushdi.</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Bekzodning telefon hisobida <strong>5 000 soʻm</strong> bor edi. U "
                "<strong>12 000 soʻmlik</strong> paketni qarzga oldi, ertasi kuni esa "
                "hisobiga <strong>20 000 soʻm</strong> tashladi.</p>"
                "<p><strong>Hozir uning hisobida qancha pul bor?</strong></p>",
        "choices": ["3 000 soʻm", "8 000 soʻm", "13 000 soʻm", "37 000 soʻm"],
        "correct": "13 000 soʻm",
        "explanation": "<p><strong>13 000 soʻm.</strong> 5 000 − 12 000 = −7 000 "
                       "(qarzga tushdi), keyin −7 000 + 20 000 = 13 000. Tekshiruv: "
                       "jami kiritilgan 5 000 + 20 000 = 25 000, sarflangan 12 000, "
                       "25 000 − 12 000 = 13 000 ✓</p>",
    },
]


# =====================================================================
# PM-11 — manfiy sonlarni koʻpaytirish va boʻlish
# =====================================================================

Q_PM11 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>(−3) × 5 = ?</strong></p>",
        "choices": ["−15", "−8", "8", "15"],
        "correct": "−15",
        "explanation": "<p><strong>−15.</strong> 3 × 5 = 15, ishoralar har xil — javob "
                       "manfiy.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(−4) × (−6) = ?</strong></p>",
        "choices": ["−24", "−10", "10", "24"],
        "correct": "24",
        "explanation": "<p><strong>24.</strong> Ishoralar bir xil — javob musbat. "
                       "4 × 6 = 24.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−20 ÷ 5 = ?</strong></p>",
        "choices": ["−25", "−4", "4", "25"],
        "correct": "−4",
        "explanation": "<p><strong>−4.</strong> 20 ÷ 5 = 4, ishoralar har xil — manfiy. "
                       "Tekshiruv: (−4) × 5 = −20 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−18 ÷ (−3) = ?</strong></p>",
        "choices": ["−21", "−6", "6", "21"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Ishoralar bir xil — javob musbat. "
                       "Tekshiruv: 6 × (−3) = −18 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>0 × (−7) = ?</strong></p>",
        "choices": ["−7", "0", "7", "70"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Nolga koʻpaytirilgan har qanday son nol "
                       "beradi — ishora bu yerda hech narsani oʻzgartirmaydi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>(−7) × 8 = ?</strong></p>",
        "choices": ["−56", "−15", "15", "56"],
        "correct": "−56",
        "explanation": "<p><strong>−56.</strong> 7 × 8 = 56, ishoralar har xil — manfiy. "
                       "−15 javobi koʻpaytirish oʻrniga qoʻshib yuborganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(−9) × (−9) = ?</strong></p>",
        "choices": ["−81", "−18", "18", "81"],
        "correct": "81",
        "explanation": "<p><strong>81.</strong> Ikkita minus — juft, javob musbat. "
                       "9 × 9 = 81.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>48 ÷ (−6) = ?</strong></p>",
        "choices": ["−42", "−8", "8", "42"],
        "correct": "−8",
        "explanation": "<p><strong>−8.</strong> 48 ÷ 6 = 8, ishoralar har xil — manfiy. "
                       "Tekshiruv: (−8) × (−6) = 48 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(−2) × (−3) × (−5) = ?</strong></p>",
        "choices": ["−30", "−10", "10", "30"],
        "correct": "−30",
        "explanation": "<p><strong>−30.</strong> Uchta minus — toq son, javob manfiy. "
                       "Sonlar: 2 × 3 × 5 = 30.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(−1) × (−1) × (−1) × (−1) = ?</strong></p>",
        "choices": ["−4", "−1", "1", "4"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> Toʻrtta minus — juft son, javob musbat. "
                       "Sonlar: 1 × 1 × 1 × 1 = 1. −4 javobi koʻpaytirish oʻrniga "
                       "qoʻshganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−56 ÷ (−7) = ?</strong></p>",
        "choices": ["−63", "−8", "8", "63"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Ishoralar bir xil — musbat. 56 ÷ 7 = 8.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(−12) × 3 = ?</strong></p>",
        "choices": ["−36", "−9", "9", "36"],
        "correct": "−36",
        "explanation": "<p><strong>−36.</strong> 12 × 3 = 36, ishoralar har xil — "
                       "manfiy.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Hisoblamasdan aniqlang.</p><p><strong>Qaysi koʻpaytmaning qiymati "
                "musbat?</strong></p>",
        "choices": ["6 × (−1)", "(−2) × 3", "(−2) × (−3) × (−4)", "(−5) × (−4)"],
        "correct": "(−5) × (−4)",
        "explanation": "<p><strong>(−5) × (−4) = 20.</strong> Ikkita minus — juft. "
                       "Qolganlari: 6 × (−1) = −6, (−2) × 3 = −6, "
                       "(−2) × (−3) × (−4) = −24 (uchta minus, toq).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Toʻrtta manfiy sonning "
                "koʻpaytmasi qanday boʻladi?</strong></p>",
        "choices": [
            "Har doim musbat",
            "Har doim manfiy",
            "Har doim nol",
            "Sonlarning kattaligiga bogʻliq",
        ],
        "correct": "Har doim musbat",
        "explanation": "<p><strong>Har doim musbat.</strong> Minuslar soni juft (4 ta), "
                       "ular juft-juft boʻlib bir-birini yoʻq qiladi. Sonlarning "
                       "kattaligi ishoraga taʼsir qilmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi qator toʻliq "
                "toʻgʻri?</strong></p>",
        "choices": [
            "−2 − 3 = −5 va (−2) × (−3) = −6",
            "−2 − 3 = −5 va (−2) × (−3) = 6",
            "−2 − 3 = 5 va (−2) × (−3) = 6",
            "−2 − 3 = 5 va (−2) × (−3) = −6",
        ],
        "correct": "−2 − 3 = −5 va (−2) × (−3) = 6",
        "explanation": "<p>Ishoralar qoidasi <strong>faqat koʻpaytirish va boʻlishga</strong> "
                       "tegishli. Qoʻshish-ayirishda ikkala qadam ham chapga: "
                       "−2 − 3 = −5. Koʻpaytirishda esa ikkita minus plus beradi: "
                       "(−2) × (−3) = 6.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Uchta sonning koʻpaytmasi manfiy "
                "chiqdi.</p><p><strong>Ular orasida nechta manfiy son boʻlishi "
                "mumkin?</strong></p>",
        "choices": ["Faqat 2 ta", "Faqat 3 ta", "1 ta yoki 3 ta", "Hech qanaqasi"],
        "correct": "1 ta yoki 3 ta",
        "explanation": "<p><strong>1 ta yoki 3 ta.</strong> Javob manfiy boʻlishi uchun "
                       "minuslar soni toq boʻlishi kerak. Uchta sondan toq son — 1 yoki "
                       "3. Agar 2 ta boʻlsa, koʻpaytma musbat chiqardi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Dilnoza shunday yozdi: <strong>(−6) × (−7) = −42</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Javob −13 boʻlishi kerak edi",
            "Hech qanday xato yoʻq, javob toʻgʻri",
            "Ikki manfiy sonning koʻpaytmasi musbat: javob 42",
            "Javob 13 boʻlishi kerak edi",
        ],
        "correct": "Ikki manfiy sonning koʻpaytmasi musbat: javob 42",
        "explanation": "<p><strong>(−6) × (−7) = 42.</strong> Dilnoza «ikkita manfiy — "
                       "demak juda manfiy» deb oʻylagan. Aslida ishoralar bir xil "
                       "boʻlsa, javob musbat chiqadi.</p>",
    },
    {
        "text": "<p>Sherbek shunday yozdi: <strong>−4 − 4 = 16</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Ishoralar qoidasi faqat × va ÷ uchun; −4 − 4 = −8",
            "Javob −16 boʻlishi kerak edi",
            "Hech qanday xato yoʻq, javob toʻgʻri",
            "Javob 8 boʻlishi kerak edi",
        ],
        "correct": "Ishoralar qoidasi faqat × va ÷ uchun; −4 − 4 = −8",
        "explanation": "<p><strong>−4 − 4 = −8.</strong> Sherbek ayirishni koʻpaytirish "
                       "bilan chalkashtirib, «ikki minus plus beradi» qoidasini "
                       "notoʻgʻri joyga qoʻllagan. (−4) × (−4) boʻlganda 16 toʻgʻri "
                       "boʻlardi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Suvga shoʻngʻuvchi har daqiqada <strong>3 metr</strong> pastga "
                "tushadi. Suv sathini nol deb olamiz.</p>"
                "<p><strong>7 daqiqadan keyin u qaysi chuqurlikda boʻladi?</strong></p>",
        "choices": ["−21 m", "−10 m", "10 m", "21 m"],
        "correct": "−21 m",
        "explanation": "<p><strong>−21 m.</strong> Har daqiqa −3 m: 7 × (−3) = −21. "
                       "Manfiy ishora «suv sathidan pastda» degani. 10 javobi "
                       "koʻpaytirish oʻrniga qoʻshganda chiqadi.</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Beshta doʻst doʻkonda birgalikda <strong>45 000 soʻm</strong> "
                "qarzdor boʻlib qolishdi va qarzni oʻzaro <strong>teng</strong> "
                "boʻlishdi.</p>"
                "<p><strong>Har biriga qancha qarz tushdi?</strong></p>",
        "choices": ["−9 000 soʻm", "−5 000 soʻm", "9 000 soʻm", "225 000 soʻm"],
        "correct": "−9 000 soʻm",
        "explanation": "<p><strong>−9 000 soʻm.</strong> −45 000 ÷ 5 = −9 000. "
                       "Ishoralar har xil — javob manfiy, chunki bu qarz. Tekshiruv: "
                       "5 × 9 000 = 45 000 ✓</p>",
    },
]


# =====================================================================
# PM-12 — daraja
# =====================================================================

Q_PM12 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>2<sup>4</sup> = ?</strong></p>",
        "choices": ["6", "8", "16", "24"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> 2 × 2 × 2 × 2 = 16. 8 javobi uchta "
                       "ikkini, 6 javobi esa 2 × 4 ni bergan boʻlardi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>5<sup>2</sup> = ?</strong></p>",
        "choices": ["7", "10", "25", "52"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> «Besh kvadrat» — 5 × 5. 10 javobi "
                       "5 × 2 dan chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3<sup>3</sup> = ?</strong></p>",
        "choices": ["6", "9", "27", "33"],
        "correct": "27",
        "explanation": "<p><strong>27.</strong> «Uch kub» — 3 × 3 × 3. 9 javobi faqat "
                       "ikkita uchni koʻpaytirganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>10<sup>4</sup> = ?</strong></p>",
        "choices": ["40", "1 000", "10 000", "100 000"],
        "correct": "10 000",
        "explanation": "<p><strong>10 000.</strong> Nollar soni koʻrsatkichga teng — "
                       "toʻrtta nol.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>7<sup>1</sup> = ?</strong></p>",
        "choices": ["0", "1", "7", "49"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Birinchi daraja — sonning oʻzi: bitta "
                       "yettini koʻpaytirishga hojat yoʻq.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>2<sup>6</sup> = ?</strong></p>",
        "choices": ["12", "36", "64", "128"],
        "correct": "64",
        "explanation": "<p><strong>64.</strong> 2, 4, 8, 16, 32, 64 — oltinchi qadam. "
                       "128 javobi bitta ortiqcha ikkiga koʻpaytirganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>6<sup>2</sup> = ?</strong></p>",
        "choices": ["8", "12", "36", "62"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> 6 × 6 = 36. 12 javobi 6 × 2 dan "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(−3)<sup>2</sup> = ?</strong></p>",
        "choices": ["−9", "−6", "6", "9"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> (−3) × (−3): ikkita minus — juft, javob "
                       "musbat.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(−2)<sup>3</sup> = ?</strong></p>",
        "choices": ["−8", "−6", "6", "8"],
        "correct": "−8",
        "explanation": "<p><strong>−8.</strong> (−2) × (−2) × (−2): uchta minus — toq, "
                       "javob manfiy. Sonlar: 2 × 2 × 2 = 8.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>10<sup>6</sup> = ?</strong></p>",
        "choices": ["60", "100 000", "1 000 000", "10 000 000"],
        "correct": "1 000 000",
        "explanation": "<p><strong>1 000 000.</strong> Bir million — bir va oltita nol. "
                       "100 000 da beshta nol bor, u 10<sup>5</sup>.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>9<sup>2</sup> = ?</strong></p>",
        "choices": ["11", "18", "81", "92"],
        "correct": "81",
        "explanation": "<p><strong>81.</strong> 9 × 9 = 81 — kvadratlar jadvalidagi "
                       "toʻqqizinchi son.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2 + 3 × 4<sup>2</sup> = ?</strong></p>",
        "choices": ["50", "80", "144", "400"],
        "correct": "50",
        "explanation": "<p><strong>50.</strong> Avval daraja: 4<sup>2</sup> = 16. Keyin "
                       "koʻpaytirish: 3 × 16 = 48. Oxirida qoʻshish: 2 + 48 = 50. "
                       "80 javobi qavs boʻlganda chiqardi: (2 + 3) × 16.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2<sup>5</sup> va "
                "5<sup>2</sup> dan qaysi biri katta?</strong></p>",
        "choices": [
            "Ular teng",
            "5² katta, chunki asosi katta",
            "2⁵ katta: 32 > 25",
            "Solishtirib boʻlmaydi",
        ],
        "correct": "2⁵ katta: 32 > 25",
        "explanation": "<p><strong>2<sup>5</sup> = 32</strong>, "
                       "<strong>5<sup>2</sup> = 25</strong>. Asos bilan koʻrsatkichning "
                       "oʻrnini almashtirish javobni oʻzgartiradi — ular teng emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3<sup>4</sup> qaysi "
                "koʻpaytmaga teng?</strong></p>",
        "choices": ["3 × 4", "3 + 3 + 3 + 3", "4 × 4 × 4", "3 × 3 × 3 × 3"],
        "correct": "3 × 3 × 3 × 3",
        "explanation": "<p><strong>3 × 3 × 3 × 3 = 81.</strong> Asos — 3 (nimani "
                       "koʻpaytiramiz), koʻrsatkich — 4 (necha marta).</p>",
    },
    {
        "text": "<p>Hisoblamasdan, faqat ishoraga qarab aniqlang.</p>"
                "<p><strong>Qaysi ifodaning qiymati musbat?</strong></p>",
        "choices": ["(−2)³", "(−2)⁵", "−2⁴", "(−2)⁴"],
        "correct": "(−2)⁴",
        "explanation": "<p><strong>(−2)<sup>4</sup> = 16.</strong> Toʻrtta minus — juft, "
                       "javob musbat. (−2)<sup>3</sup> = −8 va (−2)<sup>5</sup> = −32 "
                       "(toq), −2<sup>4</sup> = −16 esa qavssiz — minus darajaga "
                       "kirmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>−4<sup>2</sup> va "
                "(−4)<sup>2</sup> orasidagi farq nimada?</strong></p>",
        "choices": [
            "Farqi yoʻq, ikkalasi ham 16",
            "−4² = −16, (−4)² = 16",
            "−4² = 16, (−4)² = −16",
            "Farqi yoʻq, ikkalasi ham −16",
        ],
        "correct": "−4² = −16, (−4)² = 16",
        "explanation": "<p>Qavs bor boʻlsa, minus ham darajaga koʻtariladi: "
                       "(−4) × (−4) = 16. Qavs boʻlmasa, avval 4<sup>2</sup> = 16 "
                       "hisoblanadi, minus esa tashqarida qoladi: −16.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Afsona shunday yozdi: <strong>3<sup>4</sup> = 12</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Hech qanday xato yoʻq, javob toʻgʻri",
            "Javob 7 boʻlishi kerak edi",
            "Javob 64 boʻlishi kerak edi",
            "Koʻrsatkich koʻpaytuvchi emas: 3 × 3 × 3 × 3 = 81",
        ],
        "correct": "Koʻrsatkich koʻpaytuvchi emas: 3 × 3 × 3 × 3 = 81",
        "explanation": "<p><strong>3<sup>4</sup> = 81.</strong> Afsona asos bilan "
                       "koʻrsatkichni koʻpaytirib yuborgan (3 × 4 = 12). Koʻrsatkich "
                       "faqat <i>necha marta</i> ekanini aytadi.</p>",
    },
    {
        "text": "<p>Jasur shunday yozdi: <strong>10<sup>5</sup> = 10 000</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Nollar soni koʻrsatkichga teng: 100 000",
            "Javob 50 boʻlishi kerak edi",
            "Hech qanday xato yoʻq, javob toʻgʻri",
            "Javob 1 000 boʻlishi kerak edi",
        ],
        "correct": "Nollar soni koʻrsatkichga teng: 100 000",
        "explanation": "<p><strong>10<sup>5</sup> = 100 000.</strong> Jasur toʻrtta nol "
                       "yozgan, yaʼni 10<sup>4</sup> ni. Koʻrsatkich 5 boʻlsa, beshta "
                       "nol boʻladi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Laboratoriyada bakteriyalar soni har soatda <strong>ikki "
                "baravar</strong> ortadi. Boshida idishda <strong>4 ta</strong> "
                "bakteriya bor edi.</p>"
                "<p><strong>5 soatdan keyin nechta bakteriya boʻladi?</strong></p>",
        "choices": ["20 ta", "32 ta", "128 ta", "1 024 ta"],
        "correct": "128 ta",
        "explanation": "<p><strong>128 ta.</strong> 4 × 2<sup>5</sup> = 4 × 32 = 128. "
                       "Soat-soat: 4 → 8 → 16 → 32 → 64 → 128 ✓ 20 javobi 4 × 5 dan, "
                       "32 javobi esa boshlangʻich 4 ni unutganda chiqadi.</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Omborda <strong>4 ta javon</strong> bor. Har javonda "
                "<strong>4 ta quti</strong>, har qutida <strong>4 ta paket</strong>, "
                "har paketda <strong>4 ta daftar</strong>.</p>"
                "<p><strong>Omborda jami nechta daftar bor?</strong></p>",
        "choices": ["16 ta", "64 ta", "256 ta", "1 024 ta"],
        "correct": "256 ta",
        "explanation": "<p><strong>256 ta.</strong> 4 × 4 × 4 × 4 = 4<sup>4</sup> = 256. "
                       "Bosqichma-bosqich: 4 javon → 16 quti → 64 paket → 256 daftar. "
                       "64 javobi bitta bosqichni tashlab ketganda chiqadi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-10 Mashq: Manfiy sonlarni qoʻshish va ayirish",
        "description": "20 savol — son oʻqida yurish, ishoralar bilan qoʻshish, "
                       "ayirishni qoʻshishga aylantirish va harorat masalalari.",
        "tutorial":    "PM-10:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM10,
    },
    {
        "title":       "PM-11 Mashq: Manfiy sonlarni koʻpaytirish va boʻlish",
        "description": "20 savol — ishoralar qoidasi, minuslarni sanash, boʻlish va "
                       "qarz masalalari.",
        "tutorial":    "PM-11:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM11,
    },
    {
        "title":       "PM-12 Mashq: Daraja",
        "description": "20 savol — asos va koʻrsatkich, kvadrat va kub, oʻnning "
                       "darajalari, manfiy asos va amallar tartibi.",
        "tutorial":    "PM-12:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM12,
    },
]
