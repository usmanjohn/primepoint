# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-16 … PM-18 (kasrlar bilan amallar).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ `text` |safe bilan chiqadi (HTML mumkin), `choices` esa ekranlanadi —
   u yerda HTML teg yoʻq, kasrlar oddiy chiziqcha bilan yoziladi: 3/4.
⚠️ Kumulyativ: notoʻgʻri kasr va aralash son PM-19 da, oʻnlik kasr PM-20 da —
   bu uch testda har bir javob toʻgʻri kasr yoki butun son.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_16_18.py --master=prime \\
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
# PM-16 — qisqartirish va taqqoslash
# =====================================================================

Q_PM16 = [
    # 1–5 tanish
    {
        "text": "<p>Qisqartiring.</p><p><strong>2/6 = ?</strong></p>",
        "choices": ["1/3", "1/4", "1/6", "2/3"],
        "correct": "1/3",
        "explanation": "<p><strong>1/3.</strong> Surat va maxrajni 2 ga boʻldik: "
                       "2 ÷ 2 = 1, 6 ÷ 2 = 3.</p>",
    },
    {
        "text": "<p>Qisqartiring.</p><p><strong>4/10 = ?</strong></p>",
        "choices": ["1/5", "2/5", "2/10", "4/5"],
        "correct": "2/5",
        "explanation": "<p><strong>2/5.</strong> Ikkalasini 2 ga boʻldik. "
                       "2/10 javobi faqat suratni boʻlganda chiqadi.</p>",
    },
    {
        "text": "<p>Qisqartiring.</p><p><strong>9/12 = ?</strong></p>",
        "choices": ["1/3", "3/4", "3/12", "9/4"],
        "correct": "3/4",
        "explanation": "<p><strong>3/4.</strong> EKUB(9, 12) = 3: 9 ÷ 3 = 3, "
                       "12 ÷ 3 = 4.</p>",
    },
    {
        "text": "<p>Qisqartiring.</p><p><strong>5/20 = ?</strong></p>",
        "choices": ["1/4", "1/5", "5/4", "2/5"],
        "correct": "1/4",
        "explanation": "<p><strong>1/4.</strong> EKUB(5, 20) = 5: 5 ÷ 5 = 1, "
                       "20 ÷ 5 = 4.</p>",
    },
    {
        "text": "<p>Qisqartiring.</p><p><strong>8/10 = ?</strong></p>",
        "choices": ["2/5", "4/5", "8/5", "1/2"],
        "correct": "4/5",
        "explanation": "<p><strong>4/5.</strong> Ikkalasini 2 ga boʻldik.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>EKUB dan foydalanib, bir qadamda qisqartiring.</p>"
                "<p><strong>12/18 = ?</strong></p>",
        "choices": ["2/3", "3/4", "6/9", "4/6"],
        "correct": "2/3",
        "explanation": "<p><strong>2/3.</strong> EKUB(12, 18) = 6: 12 ÷ 6 = 2, "
                       "18 ÷ 6 = 3. 6/9 va 4/6 — toʻgʻri, lekin oxirigacha "
                       "qisqartirilmagan.</p>",
    },
    {
        "text": "<p>Qisqartiring.</p><p><strong>15/25 = ?</strong></p>",
        "choices": ["1/5", "3/5", "5/3", "3/10"],
        "correct": "3/5",
        "explanation": "<p><strong>3/5.</strong> EKUB(15, 25) = 5.</p>",
    },
    {
        "text": "<p>Qisqartiring.</p><p><strong>24/36 = ?</strong></p>",
        "choices": ["1/2", "2/3", "3/4", "12/18"],
        "correct": "2/3",
        "explanation": "<p><strong>2/3.</strong> EKUB(24, 36) = 12: 24 ÷ 12 = 2, "
                       "36 ÷ 12 = 3. 12/18 hali qisqaradi.</p>",
    },
    {
        "text": "<p>2/3 kasrini maxraji 15 boʻlgan teng kasr koʻrinishida yozing.</p>",
        "choices": ["5/15", "8/15", "10/15", "12/15"],
        "correct": "10/15",
        "explanation": "<p><strong>10/15.</strong> 15 ÷ 3 = 5, demak surat ham 5 ga "
                       "koʻpaytiriladi: 2 × 5 = 10. Faqat maxrajni oʻzgartirish "
                       "kasrni buzadi.</p>",
    },
    {
        "text": "<p>Taqqoslang.</p><p><strong>3/8 va 5/8</strong></p>",
        "choices": ["3/8 katta", "5/8 katta", "Ular teng", "Taqqoslab boʻlmaydi"],
        "correct": "5/8 katta",
        "explanation": "<p><strong>5/8.</strong> Maxrajlar bir xil — boʻlaklar bir xil "
                       "kattalikda, demak nechtasi koʻp boʻlsa oʻsha katta.</p>",
    },
    {
        "text": "<p>Taqqoslang.</p><p><strong>2/5 va 2/7</strong></p>",
        "choices": ["2/5 katta", "2/7 katta", "Ular teng", "Taqqoslab boʻlmaydi"],
        "correct": "2/5 katta",
        "explanation": "<p><strong>2/5.</strong> Suratlar bir xil, demak maxraji "
                       "kichigi kattaroq: beshga boʻlingan boʻlak yettiga "
                       "boʻlingandan katta.</p>",
    },
    {
        "text": "<p>Taqqoslang.</p><p><strong>1/2 va 2/5</strong></p>",
        "choices": ["1/2 katta", "2/5 katta", "Ular teng", "Taqqoslab boʻlmaydi"],
        "correct": "1/2 katta",
        "explanation": "<p><strong>1/2.</strong> Umumiy maxraj 10: 1/2 = 5/10, "
                       "2/5 = 4/10. 5 &gt; 4.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Quyidagilardan qaysi biri "
                "1/2 ga TENG EMAS?</strong></p>",
        "choices": ["3/6", "4/9", "5/10", "7/14"],
        "correct": "4/9",
        "explanation": "<p><strong>4/9.</strong> Qolganlarida maxraj suratning "
                       "roppa-rosa ikki barobari: 3/6, 5/10, 7/14 — hammasi 1/2. "
                       "4/9 da esa 9 soni 8 emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi kasr qisqarmas — "
                "yaʼni undan boshqa qisqartirish mumkin emas?</strong></p>",
        "choices": ["4/6", "6/9", "7/9", "10/15"],
        "correct": "7/9",
        "explanation": "<p><strong>7/9.</strong> 7 va 9 ning 1 dan boshqa umumiy "
                       "boʻluvchisi yoʻq. Qolganlari: 4/6 = 2/3, 6/9 = 2/3, "
                       "10/15 = 2/3.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Quyidagilardan qaysi biri "
                "eng katta?</strong></p>",
        "choices": ["1/2", "2/3", "3/5", "5/8"],
        "correct": "2/3",
        "explanation": "<p><strong>2/3.</strong> Toʻrtalasining umumiy maxraji 120: "
                       "1/2 = 60/120, <strong>2/3 = 80/120</strong>, 3/5 = 72/120, "
                       "5/8 = 75/120. Suratlar solishtirilsa, eng kattasi 80 — "
                       "yaʼni 2/3.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>5-A sinfda 20 oʻquvchidan 12 tasi, "
                "5-B sinfda 25 oʻquvchidan 15 tasi kutubxonaga yozilgan.</p>"
                "<p><strong>Qaysi sinfda yozilganlarning ulushi katta?</strong></p>",
        "choices": [
            "5-A da, chunki 20 kichikroq sinf",
            # literal ">" — choices are autoescaped, &gt; would show as text
            "5-B da, chunki 15 > 12",
            "Ulushlar teng — ikkalasi ham 3/5",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Ulushlar teng — ikkalasi ham 3/5",
        "explanation": "<p>12/20 = 3/5 (ikkalasini 4 ga boʻldik), 15/25 = 3/5 "
                       "(ikkalasini 5 ga boʻldik). Sonlar har xil, ulush bir xil.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Bekzod shunday yozdi: <strong>6/9 = 2/9</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Hech qanday xato yoʻq",
            "U faqat suratni boʻlgan; ikkalasini ham 3 ga boʻlib, 2/3 chiqadi",
            "Javob 3/9 boʻlishi kerak edi",
            "Javob 6/3 boʻlishi kerak edi",
        ],
        "correct": "U faqat suratni boʻlgan; ikkalasini ham 3 ga boʻlib, 2/3 chiqadi",
        "explanation": "<p><strong>6/9 = 2/3.</strong> Kasrning asosiy xossasi surat "
                       "va maxrajni <i>birga</i> oʻzgartirishni talab qiladi. Faqat "
                       "suratni boʻlsangiz, miqdor kichrayib ketadi.</p>",
    },
    {
        "text": "<p>Dilnoza shunday dedi: <strong>«5/7 = 3/5, chunki ikkalasidan 2 ni "
                "ayirdim»</strong>.</p><p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Kasrning asosiy xossasida ayirish yoʻq — faqat koʻpaytirish va boʻlish bor",
            "Hech qanday xato yoʻq",
            "Toʻgʻrisi 3/7 boʻlishi kerak edi",
            "Toʻgʻrisi 7/5 boʻlishi kerak edi",
        ],
        "correct": "Kasrning asosiy xossasida ayirish yoʻq — faqat koʻpaytirish va "
                   "boʻlish bor",
        "explanation": "<p>5/7 — qisqarmas kasr, u oʻzgarmaydi. Umumiy maxraj 35 da "
                       "tekshirsak: 5/7 = 25/35, 3/5 = 21/35 — teng emas.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Bogʻda <strong>30 ta</strong> daraxt bor, ulardan "
                "<strong>18 tasi</strong> olma.</p>"
                "<p><strong>Olmalarning ulushi qisqarmas kasr bilan qanday "
                "yoziladi?</strong></p>",
        "choices": ["3/5", "6/10", "9/15", "18/30"],
        "correct": "3/5",
        "explanation": "<p><strong>3/5.</strong> 18/30, EKUB(18, 30) = 6: 18 ÷ 6 = 3, "
                       "30 ÷ 6 = 5. Qolgan uch variant ham shu miqdorni bildiradi, "
                       "lekin ular oxirigacha qisqartirilmagan.</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Afsona 40 ta masaladan <strong>24 tasini</strong>, Jasur esa 35 ta "
                "masaladan <strong>20 tasini</strong> yechdi.</p>"
                "<p><strong>Kim oʻz masalalarining kattaroq ulushini "
                "yechgan?</strong></p>",
        "choices": [
            "Afsona — uning ulushi 3/5, Jasurniki esa 4/7",
            "Jasur — u koʻproq masala yechgan",
            "Ikkalasi teng ulush yechgan",
            "Jasur — uning ulushi 4/7, bu 3/5 dan katta",
        ],
        "correct": "Afsona — uning ulushi 3/5, Jasurniki esa 4/7",
        "explanation": "<p>24/40 = 3/5 va 20/35 = 4/7. Umumiy maxraj 35: 3/5 = 21/35, "
                       "4/7 = 20/35. 21 &gt; 20, demak Afsonaning ulushi katta — "
                       "garchi u atigi 4 taga koʻp masala yechgan boʻlsa ham.</p>",
    },
]


# =====================================================================
# PM-17 — qoʻshish va ayirish
# =====================================================================

Q_PM17 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>1/5 + 2/5 = ?</strong></p>",
        "choices": ["3/5", "3/10", "2/5", "2/10"],
        "correct": "3/5",
        "explanation": "<p><strong>3/5.</strong> Maxrajlar bir xil — faqat suratlarni "
                       "qoʻshamiz. 3/10 javobi maxrajlarni ham qoʻshganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3/7 + 2/7 = ?</strong></p>",
        "choices": ["5/7", "5/14", "6/7", "1/7"],
        "correct": "5/7",
        "explanation": "<p><strong>5/7.</strong> Yettidan boʻlaklar sanaldi: uchta "
                       "va ikkita — beshta.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>5/8 − 2/8 = ?</strong></p>",
        "choices": ["3/8", "3/16", "7/8", "1/4"],
        "correct": "3/8",
        "explanation": "<p><strong>3/8.</strong> Ayirishda ham maxraj oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang va javobni qisqartiring.</p>"
                "<p><strong>1/4 + 1/4 = ?</strong></p>",
        "choices": ["1/2", "2/8", "1/8", "1/4"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> 1/4 + 1/4 = 2/4, qisqartirsak 1/2. "
                       "2/8 javobi maxrajlarni ham qoʻshganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang va javobni qisqartiring.</p>"
                "<p><strong>7/9 − 4/9 = ?</strong></p>",
        "choices": ["1/3", "3/9", "1/9", "11/9"],
        "correct": "1/3",
        "explanation": "<p><strong>1/3.</strong> 7/9 − 4/9 = 3/9, EKUB(3, 9) = 3, "
                       "demak 1/3. 3/9 ham toʻgʻri son, lekin qisqartirilmagan.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>1/2 + 1/3 = ?</strong></p>",
        "choices": ["2/5", "5/6", "1/6", "2/6"],
        "correct": "5/6",
        "explanation": "<p><strong>5/6.</strong> EKUK(2, 3) = 6: 3/6 + 2/6 = 5/6. "
                       "2/5 javobi suratlarni ham, maxrajlarni ham qoʻshganda "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1/2 + 1/4 = ?</strong></p>",
        "choices": ["2/6", "1/6", "3/4", "1/3"],
        "correct": "3/4",
        "explanation": "<p><strong>3/4.</strong> 4 soni 2 ga boʻlinadi, demak umumiy "
                       "maxraj 4: 2/4 + 1/4 = 3/4.</p>",
    },
    {
        "text": "<p>Hisoblang va javobni qisqartiring.</p>"
                "<p><strong>2/3 − 1/6 = ?</strong></p>",
        "choices": ["1/2", "1/3", "1/6", "3/6"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> Umumiy maxraj 6: 4/6 − 1/6 = 3/6, "
                       "qisqartirsak 1/2.</p>",
    },
    {
        "text": "<p>Hisoblang va javobni qisqartiring.</p>"
                "<p><strong>1/3 + 1/6 = ?</strong></p>",
        "choices": ["2/9", "1/2", "2/6", "1/9"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> 2/6 + 1/6 = 3/6 = 1/2. 2/9 javobi "
                       "suratlarni ham, maxrajlarni ham qoʻshganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3/4 − 1/2 = ?</strong></p>",
        "choices": ["1/4", "2/2", "1/2", "2/4"],
        "correct": "1/4",
        "explanation": "<p><strong>1/4.</strong> Umumiy maxraj 4: 3/4 − 2/4 = 1/4.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2/5 + 3/10 = ?</strong></p>",
        "choices": ["5/15", "7/10", "1/2", "5/10"],
        "correct": "7/10",
        "explanation": "<p><strong>7/10.</strong> EKUK(5, 10) = 10: 4/10 + 3/10 = "
                       "7/10. Faqat birinchi kasr kengaydi.</p>",
    },
    {
        "text": "<p>Hisoblang va javobni qisqartiring.</p>"
                "<p><strong>5/6 − 1/3 = ?</strong></p>",
        "choices": ["1/2", "4/3", "1/3", "3/6"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> Umumiy maxraj 6: 5/6 − 2/6 = 3/6 = "
                       "1/2.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>4 va 6 maxrajlar uchun eng "
                "kichik umumiy maxraj qaysi?</strong></p>",
        "choices": ["10", "12", "24", "2"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Bu EKUK(4, 6). 24 ham umumiy maxraj "
                       "boʻla oladi (4 × 6), lekin u eng kichigi emas — kattaroq "
                       "sonlar bilan ishlash esa qiyinroq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Kasrlarni qoʻshganda maxraj "
                "nega qoʻshilmaydi?</strong></p>",
        "choices": [
            "Chunki maxraj har doim katta son boʻladi",
            "Chunki maxraj boʻlakning nomi — u nechtaligini emas, qanchaligini aytadi",
            "Chunki maxrajlar har doim teng boʻladi",
            "Chunki maxrajni faqat koʻpaytirish mumkin",
        ],
        "correct": "Chunki maxraj boʻlakning nomi — u nechtaligini emas, qanchaligini "
                   "aytadi",
        "explanation": "<p>«Uchta olma + ikkita olma = beshta olma» deymiz, «olmaolma» "
                       "demaymiz. Maxraj — boʻlakning nomi, shuning uchun "
                       "1/8 + 3/8 = 4/8, hech qachon 4/16 emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Quyidagi yigʻindilardan "
                "qaysi biri eng katta?</strong></p>",
        "choices": ["1/4 + 1/4", "1/3 + 1/6", "1/2 + 1/4", "1/5 + 1/5"],
        "correct": "1/2 + 1/4",
        "explanation": "<p><strong>1/2 + 1/4 = 3/4.</strong> Qolganlari: "
                       "1/4 + 1/4 = 1/2, 1/3 + 1/6 = 1/2, 1/5 + 1/5 = 2/5. "
                       "3/4 — eng kattasi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Butun tortning 5/8 qismi "
                "yeyildi.</p><p><strong>Qanchasi qoldi?</strong></p>",
        "choices": ["3/8", "5/8", "3/16", "8/5"],
        "correct": "3/8",
        "explanation": "<p><strong>3/8.</strong> Butun tort — 8/8. "
                       "8/8 − 5/8 = 3/8. Butunni har doim maxraj/maxraj koʻrinishida "
                       "yozing.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Bekzod shunday yozdi: <strong>1/2 + 1/3 = 2/5</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Javob 2/6 boʻlishi kerak edi",
            "Hech qanday xato yoʻq",
            "U maxrajlarni ham qoʻshgan; umumiy maxrajga keltirilsa javob 5/6",
            "Javob 1/5 boʻlishi kerak edi",
        ],
        "correct": "U maxrajlarni ham qoʻshgan; umumiy maxrajga keltirilsa javob 5/6",
        "explanation": "<p><strong>1/2 + 1/3 = 3/6 + 2/6 = 5/6.</strong> Tez "
                       "tekshiruv: qoʻshishda javob ikkala qoʻshiluvchidan ham katta "
                       "boʻlishi kerak, 2/5 esa 1/2 dan kichik — demak allaqachon "
                       "xato.</p>",
    },
    {
        "text": "<p>Sherbek shunday yozdi: <strong>3/8 + 1/8 = 4/16</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Maxrajlar allaqachon bir xil edi — javob 4/8, yaʼni 1/2",
            "Hech qanday xato yoʻq",
            "Javob 3/16 boʻlishi kerak edi",
            "Javob 4/64 boʻlishi kerak edi",
        ],
        "correct": "Maxrajlar allaqachon bir xil edi — javob 4/8, yaʼni 1/2",
        "explanation": "<p><strong>3/8 + 1/8 = 4/8 = 1/2.</strong> Sherbek "
                       "maxrajlarni ham qoʻshgan. Aslida 4/16 = 1/4 — bu javobdan "
                       "ikki barobar kichik son.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Bekzod devorning <strong>1/3</strong> qismini birinchi kuni, "
                "<strong>1/4</strong> qismini ikkinchi kuni boʻyadi.</p>"
                "<p><strong>Devorning qanchasi boʻyalmay qoldi?</strong></p>",
        "choices": ["2/7", "5/12", "7/12", "1/12"],
        "correct": "5/12",
        "explanation": "<p><strong>5/12.</strong> EKUK(3, 4) = 12: 4/12 + 3/12 = "
                       "7/12 boʻyaldi. Qolgani 12/12 − 7/12 = 5/12. 7/12 javobi "
                       "boʻyalgan qismni, 2/7 esa maxrajlarni qoʻshib yuborgan "
                       "xatoni bildiradi.</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Afsona kitobning <strong>1/4</strong> qismini dushanba, "
                "<strong>2/5</strong> qismini seshanba kuni oʻqidi.</p>"
                "<p><strong>Kitobning qanchasi qolgan?</strong></p>",
        "choices": ["3/9", "7/20", "13/20", "1/2"],
        "correct": "7/20",
        "explanation": "<p><strong>7/20.</strong> EKUK(4, 5) = 20: 5/20 + 8/20 = "
                       "13/20 oʻqildi. Qolgani 20/20 − 13/20 = 7/20. Tekshiruv: "
                       "13/20 + 7/20 = 20/20 = 1 ✓</p>",
    },
]


# =====================================================================
# PM-18 — koʻpaytirish va boʻlish
# =====================================================================

Q_PM18 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>3 × 1/8 = ?</strong></p>",
        "choices": ["3/8", "1/24", "3/24", "1/8"],
        "correct": "3/8",
        "explanation": "<p><strong>3/8.</strong> Uchta sakkizdan bir boʻlak. Butun "
                       "son faqat suratga koʻpaytiriladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1/2 × 1/3 = ?</strong></p>",
        "choices": ["1/6", "2/6", "2/5", "3/2"],
        "correct": "1/6",
        "explanation": "<p><strong>1/6.</strong> Suratlar: 1 × 1 = 1. Maxrajlar: "
                       "2 × 3 = 6. «Yarmining uchdan biri» — yarimdan kichik "
                       "boʻlishi tabiiy.</p>",
    },
    {
        "text": "<p>Hisoblang va javobni qisqartiring.</p>"
                "<p><strong>2/3 × 1/2 = ?</strong></p>",
        "choices": ["1/3", "2/6", "1/6", "3/4"],
        "correct": "1/3",
        "explanation": "<p><strong>1/3.</strong> (2 × 1)/(3 × 2) = 2/6 = 1/3. "
                       "«Uchdan ikkining yarmi — uchdan bir».</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1/4 × 1/5 = ?</strong></p>",
        "choices": ["1/20", "2/9", "1/9", "5/4"],
        "correct": "1/20",
        "explanation": "<p><strong>1/20.</strong> Maxrajlar koʻpaytiriladi: "
                       "4 × 5 = 20.</p>",
    },
    {
        "text": "<p>Hisoblang va javobni qisqartiring.</p>"
                "<p><strong>5 × 1/10 = ?</strong></p>",
        "choices": ["1/2", "5/10", "1/50", "1/5"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> 5 × 1/10 = 5/10, qisqartirsak 1/2. "
                       "5/10 ham toʻgʻri son, lekin qisqartirilmagan.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang va javobni qisqartiring.</p>"
                "<p><strong>3/4 × 2/3 = ?</strong></p>",
        "choices": ["1/2", "6/12", "5/7", "9/8"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> (3 × 2)/(4 × 3) = 6/12 = 1/2.</p>",
    },
    {
        "text": "<p>Hisoblang va javobni qisqartiring.</p>"
                "<p><strong>2/5 × 5/6 = ?</strong></p>",
        "choices": ["1/3", "10/30", "7/11", "1/6"],
        "correct": "1/3",
        "explanation": "<p><strong>1/3.</strong> (2 × 5)/(5 × 6) = 10/30, "
                       "EKUB(10, 30) = 10, demak 1/3.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1/2 ÷ 3 = ?</strong></p>",
        "choices": ["1/6", "3/2", "1/5", "2/3"],
        "correct": "1/6",
        "explanation": "<p><strong>1/6.</strong> Yarim nonni uch bolaga boʻlsak, "
                       "butun oltiga boʻlingan boʻladi. Boʻlish ulushni "
                       "kichraytiradi — 3/2 javobi undan katta chiqib ketardi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3/4 ÷ 3 = ?</strong></p>",
        "choices": ["1/4", "3/12", "9/4", "1/12"],
        "correct": "1/4",
        "explanation": "<p><strong>1/4.</strong> Surat 3 ga boʻlinadi: 1/4. Yoki "
                       "3/12 deb yozib, keyin qisqartirish mumkin — natija bir xil.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1/2 ÷ 1/6 = ?</strong></p>",
        "choices": ["3", "1/12", "1/3", "6"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Savol: yarimga nechta 1/6 sigʻadi? "
                       "1/2 = 3/6, demak uchta. Qoida bilan: ÷ 1/6 = × 6, "
                       "1/2 × 6 = 3.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3/4 ÷ 1/4 = ?</strong></p>",
        "choices": ["3", "4", "3/16", "1/3"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> 3/4 kilogramm unda nechta 1/4 "
                       "kilogrammlik paket bor? Uchta. Qoida bilan: "
                       "3/4 × 4 = 12/4 = 3.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2/3 ÷ 2 = ?</strong></p>",
        "choices": ["1/3", "4/3", "2/6", "1/6"],
        "correct": "1/3",
        "explanation": "<p><strong>1/3.</strong> Surat 2 ga boʻlinadi: 1/3. "
                       "Uchdan ikkini ikkiga boʻlsak, uchdan bir qoladi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Hisoblamasdan aniqlang.</p><p><strong>1/2 × 1/3 ning natijasi "
                "1/2 dan katta boʻladimi yoki kichikmi?</strong></p>",
        "choices": [
            "Katta, chunki koʻpaytirish sonni oshiradi",
            "Kichik, chunki 1 dan kichik songa koʻpaytirish boʻlak olish demak",
            "Teng boʻladi",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Kichik, chunki 1 dan kichik songa koʻpaytirish boʻlak olish demak",
        "explanation": "<p>«Yarmining uchdan biri» yarimdan katta boʻlishi mumkin "
                       "emas. Natija 1/6 — yarimdan uch barobar kichik.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«3/4 kilogrammning yarmi» "
                "qaysi amal bilan topiladi?</strong></p>",
        "choices": ["3/4 + 1/2", "3/4 − 1/2", "1/2 × 3/4", "3/4 ÷ 1/2"],
        "correct": "1/2 × 3/4",
        "explanation": "<p><strong>1/2 × 3/4 = 3/8.</strong> Matndagi «…ning …qismi» "
                       "har doim koʻpaytirish degani.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>1/6 ning teskarisi "
                "qaysi son?</strong></p>",
        "choices": ["6", "1/6", "6/6", "1"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Bitta butunda oltita 1/6 bor. Shuning "
                       "uchun 1/6 ga boʻlish 6 ga koʻpaytirish bilan bir xil.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Yarim litr sut bor, har bir chashka "
                "1/8 litr sigʻdiradi.</p><p><strong>Nechta chashka toʻldiriladi?</strong></p>",
        "choices": ["2 ta", "4 ta", "8 ta", "16 ta"],
        "correct": "4 ta",
        "explanation": "<p><strong>4 ta.</strong> 1/2 = 4/8, demak yarimga toʻrtta "
                       "sakkizdan bir sigʻadi. Qoida bilan: 1/2 ÷ 1/8 = "
                       "1/2 × 8 = 4.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Dilnoza shunday yozdi: <strong>1/2 × 1/3 = 2/6</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Javob 3/6 boʻlishi kerak edi",
            "Hech qanday xato yoʻq",
            "Javob 5/6 boʻlishi kerak edi",
            "U suratlarni qoʻshib yuborgan; koʻpaytirilsa 1 × 1 = 1, javob 1/6",
        ],
        "correct": "U suratlarni qoʻshib yuborgan; koʻpaytirilsa 1 × 1 = 1, javob 1/6",
        "explanation": "<p><strong>1/2 × 1/3 = 1/6.</strong> Maxraj toʻgʻri "
                       "hisoblangan (2 × 3 = 6), surat esa qoʻshib yuborilgan. "
                       "2/6 = 1/3 — bu javobdan ikki barobar katta.</p>",
    },
    {
        "text": "<p>Jasur shunday yozdi: <strong>1/2 ÷ 3 = 3/2</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Hech qanday xato yoʻq",
            "U boʻlish oʻrniga koʻpaytirgan; boʻlish ulushni kichraytiradi, javob 1/6",
            "Javob 2/3 boʻlishi kerak edi",
            "Javob 1/5 boʻlishi kerak edi",
        ],
        "correct": "U boʻlish oʻrniga koʻpaytirgan; boʻlish ulushni kichraytiradi, "
                   "javob 1/6",
        "explanation": "<p><strong>1/2 ÷ 3 = 1/6.</strong> Yarim nonni uch bolaga "
                       "boʻlsangiz, har kimga yarimdan <i>kam</i> tegishi kerak. "
                       "3/2 esa butundan ham katta son.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Retsept 6 kishiga moʻljallangan va unda <strong>1/2 stakan "
                "yogʻ</strong> bor. Nodira opa 2 kishiga osh damlamoqchi — yaʼni "
                "retseptning <strong>1/3</strong> qismi kerak.</p>"
                "<p><strong>Qancha yogʻ olishi kerak?</strong></p>",
        "choices": ["1/6 stakan", "1/5 stakan", "1/3 stakan", "3/2 stakan"],
        "correct": "1/6 stakan",
        "explanation": "<p><strong>1/6 stakan.</strong> 1/3 × 1/2 = 1/6. Tekshiruv: "
                       "3 × 1/6 = 3/6 = 1/2 stakan — retseptga qaytdi ✓</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Bir bogʻ yerning <strong>3/4</strong> qismi ekilgan. Ekilgan "
                "qismning <strong>1/3</strong> i — pomidor.</p>"
                "<p><strong>Pomidor butun yerning qaysi qismini egallaydi?</strong></p>",
        "choices": ["1/4", "1/3", "3/7", "1/12"],
        "correct": "1/4",
        "explanation": "<p><strong>1/4.</strong> 1/3 × 3/4 = 3/12 = 1/4. Diqqat: "
                       "1/3 butun yerdan emas, faqat <i>ekilgan qismdan</i> "
                       "olinadi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-16 Mashq: Kasrlarni qisqartirish va taqqoslash",
        "description": "20 savol — teng kasrlar, kasrning asosiy xossasi, EKUB bilan "
                       "qisqartirish va umumiy maxraj orqali taqqoslash.",
        "tutorial":    "PM-16:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM16,
    },
    {
        "title":       "PM-17 Mashq: Kasrlarni qoʻshish va ayirish",
        "description": "20 savol — bir xil va har xil maxrajli kasrlar, EKUK bilan "
                       "umumiy maxraj, javobni qisqartirish.",
        "tutorial":    "PM-17:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM17,
    },
    {
        "title":       "PM-18 Mashq: Kasrlarni koʻpaytirish va boʻlish",
        "description": "20 savol — kasrni butun songa va kasrga koʻpaytirish, "
                       "«…ning …qismi», birlik kasrga boʻlish.",
        "tutorial":    "PM-18:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM18,
    },
]
