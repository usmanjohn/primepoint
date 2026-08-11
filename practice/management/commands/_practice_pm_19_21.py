# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-19 … PM-21 (aralash sonlar, oʻnlik kasrlar).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ `text` |safe bilan chiqadi (HTML mumkin), `choices` esa ekranlanadi —
   u yerda HTML teg yoʻq; kasrlar «3/4», aralash sonlar «2 1/4», oʻnlik
   kasrlar vergul bilan «0,45» koʻrinishida yoziladi.
⚠️ Kumulyativ: PM-19 da hali vergulli son yoʻq (oʻnlik kasr PM-20 da);
   foiz esa PM-22 dan boshlanadi — uch testda ham foiz yoʻq.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_19_21.py --master=prime \\
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
# PM-19 — aralash sonlar va notoʻgʻri kasrlar
# =====================================================================

Q_PM19 = [
    # 1–5 tanish
    {
        "text": "<p>Aralash son koʻrinishida yozing.</p><p><strong>7/3 = ?</strong></p>",
        "choices": ["2 1/3", "3 1/2", "1 4/3", "2 3/1"],
        "correct": "2 1/3",
        "explanation": "<p><strong>2 1/3.</strong> 7 ÷ 3 = 2 (qoldiq 1). Boʻlinma — "
                       "butun qism, qoldiq — yangi surat, maxraj oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Aralash son koʻrinishida yozing.</p><p><strong>9/4 = ?</strong></p>",
        "choices": ["2 1/4", "4 1/9", "1 5/4", "2 4/1"],
        "correct": "2 1/4",
        "explanation": "<p><strong>2 1/4.</strong> 9 ÷ 4 = 2 (qoldiq 1).</p>",
    },
    {
        "text": "<p>Notoʻgʻri kasr koʻrinishida yozing.</p>"
                "<p><strong>2 1/2 = ?</strong></p>",
        "choices": ["5/2", "3/2", "2/2", "4/2"],
        "correct": "5/2",
        "explanation": "<p><strong>5/2.</strong> 2 × 2 + 1 = 5, maxraj oʻzgarmaydi. "
                       "Ikki yarim — bu beshta yarim.</p>",
    },
    {
        "text": "<p>Notoʻgʻri kasr koʻrinishida yozing.</p>"
                "<p><strong>3 2/5 = ?</strong></p>",
        "choices": ["10/5", "15/5", "17/5", "32/5"],
        "correct": "17/5",
        "explanation": "<p><strong>17/5.</strong> 3 × 5 + 2 = 17.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi kasr notoʻgʻri "
                "kasr?</strong></p>",
        "choices": ["3/4", "5/8", "9/5", "2/9"],
        "correct": "9/5",
        "explanation": "<p><strong>9/5.</strong> Notoʻgʻri kasrda surat maxrajdan "
                       "katta yoki unga teng. «Notoʻgʻri» degani xato degani emas — "
                       "bu shunchaki butundan katta kasr.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Aralash son koʻrinishida yozing.</p><p><strong>11/4 = ?</strong></p>",
        "choices": ["2 3/4", "3 1/4", "4 3/11", "2 1/4"],
        "correct": "2 3/4",
        "explanation": "<p><strong>2 3/4.</strong> 11 ÷ 4 = 2 (qoldiq 3). 4 3/11 "
                       "javobi maxraj bilan boʻlinmani almashtirib yuborganda "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Notoʻgʻri kasr koʻrinishida yozing.</p>"
                "<p><strong>1 5/6 = ?</strong></p>",
        "choices": ["6/6", "11/6", "15/6", "56/6"],
        "correct": "11/6",
        "explanation": "<p><strong>11/6.</strong> 1 × 6 + 5 = 11.</p>",
    },
    {
        "text": "<p>Notoʻgʻri kasr koʻrinishida yozing.</p>"
                "<p><strong>4 1/3 = ?</strong></p>",
        "choices": ["7/3", "12/3", "13/3", "41/3"],
        "correct": "13/3",
        "explanation": "<p><strong>13/3.</strong> 4 × 3 + 1 = 13.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1 1/4 + 2 1/2 = ?</strong></p>",
        "choices": ["3 2/6", "3 3/4", "3 1/4", "4 1/4"],
        "correct": "3 3/4",
        "explanation": "<p><strong>3 3/4.</strong> Butunlar: 1 + 2 = 3. Kasrlar: "
                       "1/4 + 2/4 = 3/4.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2 3/4 + 1 1/2 = ?</strong></p>",
        "choices": ["3 5/4", "3 1/4", "4 1/4", "4 3/4"],
        "correct": "4 1/4",
        "explanation": "<p><strong>4 1/4.</strong> Butunlar 3, kasrlar "
                       "3/4 + 2/4 = 5/4. Kasr qism butundan oshdi: 5/4 = 1 1/4, "
                       "uni butunlarga qoʻshamiz. Javob aralash sonda yoziladi, "
                       "shuning uchun «3 5/4» tugallanmagan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3 1/2 − 1 1/4 = ?</strong></p>",
        "choices": ["2 1/4", "2 1/2", "1 1/4", "2 3/4"],
        "correct": "2 1/4",
        "explanation": "<p><strong>2 1/4.</strong> Butunlar: 3 − 1 = 2. Kasrlar: "
                       "2/4 − 1/4 = 1/4.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3 1/4 − 1 3/4 = ?</strong></p>",
        "choices": ["1 1/2", "2 2/4", "2 1/2", "1 1/4"],
        "correct": "1 1/2",
        "explanation": "<p><strong>1 1/2.</strong> Notoʻgʻri kasrga oʻtamiz: "
                       "13/4 − 7/4 = 6/4 = 3/2 = 1 1/2. «2 2/4» javobi kasrlarni "
                       "«kattadan kichigini» deb ayirganda chiqadi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>8/3 son oʻqida qaysi ikki "
                "butun son orasida turadi?</strong></p>",
        "choices": ["1 va 2", "2 va 3", "3 va 4", "8 va 3"],
        "correct": "2 va 3",
        "explanation": "<p><strong>2 va 3 orasida.</strong> 8 ÷ 3 = 2 (qoldiq 2), "
                       "demak 8/3 = 2 2/3 — uchga yaqinroq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Quyidagilardan qaysi biri "
                "eng katta?</strong></p>",
        "choices": ["2", "2 1/4", "9/4", "5/2"],
        "correct": "5/2",
        "explanation": "<p><strong>5/2.</strong> Hammasini toʻrtdan boʻlakka "
                       "keltiramiz: 2 = 8/4, 2 1/4 = 9/4, 9/4 = 9/4, 5/2 = 10/4. "
                       "Eng kattasi 10/4. Diqqat: 2 1/4 va 9/4 — bir xil son.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3 2/3 qaysi kasrga "
                "teng?</strong></p>",
        "choices": ["6/3", "9/3", "11/3", "32/3"],
        "correct": "11/3",
        "explanation": "<p><strong>11/3.</strong> 3 × 3 + 2 = 11.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>6/6 nimaga teng?</strong></p>",
        "choices": ["0", "1", "6", "1/6"],
        "correct": "1",
        "explanation": "<p><strong>1 ga.</strong> Surat maxrajga teng boʻlsa, kasr "
                       "butunga teng. Bu ham notoʻgʻri kasr hisoblanadi — surat "
                       "maxrajdan kichik emas.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Jasur shunday yozdi: <strong>2 1/3 = 2/3</strong>, chunki 2 ni "
                "1/3 ga koʻpaytirdim.</p><p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Hech qanday xato yoʻq",
            "Aralash sonda qoʻshish yashiringan: 2 + 1/3 = 7/3",
            "Toʻgʻrisi 3/2 boʻlishi kerak edi",
            "Toʻgʻrisi 21/3 boʻlishi kerak edi",
        ],
        "correct": "Aralash sonda qoʻshish yashiringan: 2 + 1/3 = 7/3",
        "explanation": "<p><strong>2 1/3 = 7/3.</strong> Tez tekshiruv: javob 2 dan "
                       "katta boʻlishi kerak edi, 2/3 esa 1 dan ham kichik.</p>",
    },
    {
        "text": "<p>Dilnoza shunday yozdi: <strong>11/4 = 4 3/11</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Toʻgʻrisi 2 3/4: surat maxrajga boʻlinadi, teskarisi emas",
            "Hech qanday xato yoʻq",
            "Toʻgʻrisi 3 2/4 boʻlishi kerak edi",
            "Toʻgʻrisi 1 7/4 boʻlishi kerak edi",
        ],
        "correct": "Toʻgʻrisi 2 3/4: surat maxrajga boʻlinadi, teskarisi emas",
        "explanation": "<p><strong>11 ÷ 4 = 2 (qoldiq 3)</strong>, demak 2 3/4. "
                       "Dilnoza 4 ni 11 ga boʻlib yuborgan va maxrajni ham "
                       "almashtirgan.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Usta ikkita taxtani ulab qoʻydi: biri <strong>1 3/4 m</strong>, "
                "ikkinchisi <strong>2 1/2 m</strong>. Soʻng undan "
                "<strong>3 1/4 m</strong>lik boʻlak kesib oldi.</p>"
                "<p><strong>Necha metr taxta qoldi?</strong></p>",
        "choices": ["1 m", "1 1/4 m", "1 1/2 m", "4 1/4 m"],
        "correct": "1 m",
        "explanation": "<p><strong>1 metr.</strong> Jami: 1 3/4 + 2 1/2 = "
                       "3 + 5/4 = 4 1/4 m. Keyin 4 1/4 − 3 1/4 = 1 m. 4 1/4 javobi "
                       "kesishni unutganda chiqadi.</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Buvijon ertalab <strong>2 1/4 kg</strong>, kechqurun "
                "<strong>1 1/2 kg</strong> un ishlatdi.</p>"
                "<p><strong>Jami qancha un ketdi?</strong></p>",
        "choices": ["3 2/6 kg", "3 3/4 kg", "3 1/4 kg", "4 1/4 kg"],
        "correct": "3 3/4 kg",
        "explanation": "<p><strong>3 3/4 kg.</strong> Butunlar: 2 + 1 = 3. Kasrlar: "
                       "1/4 + 2/4 = 3/4. «3 2/6» javobi suratlarni ham, maxrajlarni "
                       "ham qoʻshganda chiqadi.</p>",
    },
]


# =====================================================================
# PM-20 — oʻnlik kasrlar
# =====================================================================

Q_PM20 = [
    # 1–5 tanish
    {
        "text": "<p>Oddiy kasr koʻrinishida yozing.</p><p><strong>0,7 = ?</strong></p>",
        "choices": ["7/10", "7/100", "1/7", "10/7"],
        "correct": "7/10",
        "explanation": "<p><strong>7/10.</strong> Vergul ortida bitta raqam — "
                       "maxrajda bitta nol.</p>",
    },
    {
        "text": "<p>Oʻnlik kasr koʻrinishida yozing.</p><p><strong>3/10 = ?</strong></p>",
        "choices": ["0,3", "0,03", "3,0", "0,13"],
        "correct": "0,3",
        "explanation": "<p><strong>0,3.</strong> Maxrajda bitta nol — vergul ortida "
                       "bitta raqam.</p>",
    },
    {
        "text": "<p>Oʻnlik kasr koʻrinishida yozing.</p><p><strong>1/2 = ?</strong></p>",
        "choices": ["0,2", "0,12", "0,5", "1,2"],
        "correct": "0,5",
        "explanation": "<p><strong>0,5.</strong> 1/2 = 5/10 (surat va maxrajni 5 ga "
                       "koʻpaytirdik), demak 0,5. 0,2 javobi maxrajni vergul ortiga "
                       "koʻchirganda chiqadi.</p>",
    },
    {
        "text": "<p>Oʻnlik kasr koʻrinishida yozing.</p><p><strong>7/100 = ?</strong></p>",
        "choices": ["0,7", "0,07", "0,007", "7,100"],
        "correct": "0,07",
        "explanation": "<p><strong>0,07.</strong> Maxrajda ikkita nol — vergul ortida "
                       "ikkita raqam kerak, shuning uchun 7 dan oldin nol turadi. "
                       "0,7 esa 70/100 boʻlib qolardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>0,9 va 0,45 dan qaysi biri "
                "katta?</strong></p>",
        "choices": ["0,9", "0,45", "Ular teng", "Taqqoslab boʻlmaydi"],
        "correct": "0,9",
        "explanation": "<p><strong>0,9.</strong> Oxiriga nol qoʻshamiz: 0,9 = 0,90. "
                       "Endi 90 va 45 solishtiriladi. Uzunroq son katta degani "
                       "emas.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>0,5 va 0,50 dan qaysi biri "
                "katta?</strong></p>",
        "choices": ["0,5", "0,50", "Ular teng", "Taqqoslab boʻlmaydi"],
        "correct": "Ular teng",
        "explanation": "<p>Oxirgi nol sonni oʻzgartirmaydi: 5/10 = 50/100. Bu "
                       "PM-16 dagi kasrning asosiy xossasi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>1,2 va 1,15 dan qaysi biri "
                "katta?</strong></p>",
        "choices": ["1,2", "1,15", "Ular teng", "Taqqoslab boʻlmaydi"],
        "correct": "1,2",
        "explanation": "<p><strong>1,2.</strong> Butunlar teng. 1,2 = 1,20 va "
                       "20 &gt; 15.</p>",
    },
    {
        "text": "<p>Oddiy kasr koʻrinishida yozing (qisqartirmasdan).</p>"
                "<p><strong>0,08 = ?</strong></p>",
        "choices": ["8/10", "8/100", "8/1000", "80/100"],
        "correct": "8/100",
        "explanation": "<p><strong>8/100.</strong> Vergul ortida ikkita raqam — "
                       "maxrajda ikkita nol.</p>",
    },
    {
        "text": "<p>Oʻnlik kasr koʻrinishida yozing.</p>"
                "<p><strong>2 4/10 = ?</strong></p>",
        "choices": ["2,4", "0,24", "24,0", "2,04"],
        "correct": "2,4",
        "explanation": "<p><strong>2,4.</strong> Butun qism vergulgacha, kasr qism "
                       "vergul ortiga yoziladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3,45 sonida 4 raqami qaysi "
                "razryadda turibdi?</strong></p>",
        "choices": ["Birlik", "Oʻndan bir", "Yuzdan bir", "Mingdan bir"],
        "correct": "Oʻndan bir",
        "explanation": "<p>Verguldan keyingi birinchi oʻrin — oʻndan bir. Ikkinchisi "
                       "(5 raqami) — yuzdan bir.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>12,05 sonida 5 raqami qaysi "
                "razryadda turibdi?</strong></p>",
        "choices": ["Oʻnlik", "Birlik", "Oʻndan bir", "Yuzdan bir"],
        "correct": "Yuzdan bir",
        "explanation": "<p>Verguldan keyin avval oʻndan bir keladi — u yerda 0 "
                       "turibdi. 5 raqami esa ikkinchi oʻrinda, yaʼni yuzdan bir "
                       "razryadida.</p>",
    },
    {
        "text": "<p>Oʻnlik kasr koʻrinishida yozing.</p><p><strong>3/4 = ?</strong></p>",
        "choices": ["0,34", "0,75", "0,43", "3,4"],
        "correct": "0,75",
        "explanation": "<p><strong>0,75.</strong> Surat va maxrajni 25 ga "
                       "koʻpaytiramiz: 3/4 = 75/100 = 0,75.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Quyidagilardan qaysi biri "
                "1/4 ga TENG EMAS?</strong></p>",
        "choices": ["0,25", "25/100", "0,4", "0,250"],
        "correct": "0,4",
        "explanation": "<p><strong>0,4.</strong> 0,4 = 4/10 = 2/5, bu 1/4 emas. "
                       "Qolganlari: 0,25 = 25/100 = 0,250 = 1/4.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Uchta son berilgan: 0,3 · 0,30 · "
                "0,03.</p><p><strong>Qaysi biri boshqalaridan farq qiladi?</strong></p>",
        "choices": ["0,3", "0,30", "0,03", "Uchalasi ham teng"],
        "correct": "0,03",
        "explanation": "<p><strong>0,03.</strong> 0,3 = 0,30 = 3/10, 0,03 esa "
                       "3/100 — oʻn barobar kichik. Nolni oxiriga qoʻshish mumkin, "
                       "boshiga esa yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Quyidagilardan qaysi biri "
                "eng katta?</strong></p>",
        "choices": ["0,7", "0,68", "0,695", "0,7001"],
        "correct": "0,7001",
        "explanation": "<p><strong>0,7001.</strong> Toʻrtinchi razryadgacha "
                       "tenglashtiramiz: 0,7000 · 0,6800 · 0,6950 · 0,7001. "
                       "Eng kattasi 7001.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Sonlar oʻsish tartibida "
                "qaysi qatorda toʻgʻri joylashgan?</strong></p>",
        "choices": [
            "2,405 · 2,45 · 2,5",
            "2,45 · 2,405 · 2,5",
            "2,5 · 2,45 · 2,405",
            "2,405 · 2,5 · 2,45",
        ],
        "correct": "2,405 · 2,45 · 2,5",
        "explanation": "<p>Mingdan birgacha tenglashtiramiz: 2,405 · 2,450 · 2,500. "
                       "Endi 405 &lt; 450 &lt; 500 — oʻsish tartibi shu.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Bekzod shunday dedi: <strong>«0,45 soni 0,9 dan katta, chunki 45 "
                "soni 9 dan katta»</strong>.</p><p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Hech qanday xato yoʻq",
            "Ular teng",
            "Razryadlarni tenglashtirish kerak: 0,9 = 0,90, va 90 katta",
            "0,45 ni 0,450 deb yozish kerak edi",
        ],
        "correct": "Razryadlarni tenglashtirish kerak: 0,9 = 0,90, va 90 katta",
        "explanation": "<p>Butun sonlardagi «uzunroq — kattaroq» qoidasi oʻnlik "
                       "kasrlarda ishlamaydi. 0,9 — deyarli bir butun, 0,45 esa "
                       "yarimdan ham kam.</p>",
    },
    {
        "text": "<p>Afsona shunday yozdi: <strong>0,5 = 1/5</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Vergul ortidagi raqam surat boʻladi: 0,5 = 5/10 = 1/2",
            "Hech qanday xato yoʻq",
            "Toʻgʻrisi 5/100 boʻlishi kerak edi",
            "Toʻgʻrisi 1/50 boʻlishi kerak edi",
        ],
        "correct": "Vergul ortidagi raqam surat boʻladi: 0,5 = 5/10 = 1/2",
        "explanation": "<p>Maxrajni nollar soni belgilaydi, vergul ortidagi raqam "
                       "emas. 1/5 esa 0,2 ga teng — butunlay boshqa son.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Bir doʻkonda goʻsht <strong>1,250 kg</strong>, boshqasida "
                "<strong>1,25 kg</strong> tortildi.</p>"
                "<p><strong>Qaysi tarozida koʻproq goʻsht bor?</strong></p>",
        "choices": [
            "Birinchisida — 1,250 uzunroq son",
            "Ikkinchisida — 1,25 soddaroq son",
            "Ikkalasida ham bir xil miqdor",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Ikkalasida ham bir xil miqdor",
        "explanation": "<p>Oxirgi nol sonni oʻzgartirmaydi: 250/1000 = 25/100. "
                       "Ikkalasi ham 1 kg 250 gramm.</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Uch xaltaning ogʻirligi: <strong>2,5 kg</strong>, "
                "<strong>2,45 kg</strong> va <strong>2,405 kg</strong>.</p>"
                "<p><strong>Eng ogʻiri bilan eng yengili orasidagi farq "
                "qancha?</strong></p>",
        "choices": ["0,05 kg", "0,095 kg", "0,45 kg", "0,95 kg"],
        "correct": "0,095 kg",
        "explanation": "<p><strong>0,095 kg</strong>, yaʼni 95 gramm. Eng ogʻiri "
                       "2,500 kg, eng yengili 2,405 kg: 2 500 g − 2 405 g = 95 g. "
                       "Grammga oʻtkazish bunday masalada eng ishonchli yoʻl.</p>",
    },
]


# =====================================================================
# PM-21 — oʻnlik kasrlar bilan toʻrt amal
# =====================================================================

Q_PM21 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>0,3 + 0,4 = ?</strong></p>",
        "choices": ["0,7", "0,07", "7", "0,12"],
        "correct": "0,7",
        "explanation": "<p><strong>0,7.</strong> Oʻndan birlar qoʻshiladi: "
                       "3 + 4 = 7.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1,5 + 2,3 = ?</strong></p>",
        "choices": ["3,8", "3,08", "38", "4,8"],
        "correct": "3,8",
        "explanation": "<p><strong>3,8.</strong> Butunlar 1 + 2 = 3, oʻndan birlar "
                       "5 + 3 = 8.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>5,7 − 2,4 = ?</strong></p>",
        "choices": ["3,3", "3,03", "2,3", "33"],
        "correct": "3,3",
        "explanation": "<p><strong>3,3.</strong> 57 − 24 = 33, bitta oʻnlik xona.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>0,2 × 3 = ?</strong></p>",
        "choices": ["0,6", "0,06", "6", "0,23"],
        "correct": "0,6",
        "explanation": "<p><strong>0,6.</strong> 2 × 3 = 6, bitta xona — 0,6.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>4,8 ÷ 2 = ?</strong></p>",
        "choices": ["2,4", "0,24", "24", "2,04"],
        "correct": "2,4",
        "explanation": "<p><strong>2,4.</strong> 48 ÷ 2 = 24, bitta xona qoladi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>2,45 + 1,3 = ?</strong></p>",
        "choices": ["2,58", "3,75", "3,48", "2,75"],
        "correct": "3,75",
        "explanation": "<p><strong>3,75.</strong> 1,3 ni 1,30 deb yozamiz va vergulni "
                       "vergul ostiga qoʻyamiz: 2,45 + 1,30 = 3,75. 2,58 javobi "
                       "sonlarni oʻng chetidan tekislaganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>6 − 1,4 = ?</strong></p>",
        "choices": ["4,6", "5,4", "4,4", "5,6"],
        "correct": "4,6",
        "explanation": "<p><strong>4,6.</strong> 6 ni 6,0 deb yozamiz: "
                       "6,0 − 1,4 = 4,6.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>0,2 × 0,3 = ?</strong></p>",
        "choices": ["0,6", "0,06", "0,006", "6"],
        "correct": "0,06",
        "explanation": "<p><strong>0,06.</strong> 2 × 3 = 6; xonalar qoʻshiladi: "
                       "1 + 1 = 2, demak oʻng chetdan ikkita raqam sanaymiz. Mantiq "
                       "ham shuni aytadi: 0,3 birdan kichik, natija 0,2 dan kichik "
                       "boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1,2 × 5 = ?</strong></p>",
        "choices": ["6", "0,6", "60", "6,5"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 12 × 5 = 60, bitta xona: 6,0 — yaʼni "
                       "6.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>7,5 ÷ 5 = ?</strong></p>",
        "choices": ["1,5", "0,15", "15", "1,05"],
        "correct": "1,5",
        "explanation": "<p><strong>1,5.</strong> 75 ÷ 5 = 15, bitta xona.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3,6 ÷ 0,4 = ?</strong></p>",
        "choices": ["0,9", "9", "90", "1,44"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> Ikkala sonning vergulini birga "
                       "suramiz: 36 ÷ 4 = 9. Faqat bittasini surish 0,9 degan xato "
                       "javobni beradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2,5 × 4 = ?</strong></p>",
        "choices": ["10", "1", "100", "8,5"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 25 × 4 = 100, bitta xona: 10,0 — "
                       "yaʼni 10.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Hisoblang.</p><p><strong>4,7 × 10 = ?</strong></p>",
        "choices": ["0,47", "4,7", "47", "470"],
        "correct": "47",
        "explanation": "<p><strong>47.</strong> 10 ga koʻpaytirilganda vergul bir "
                       "oʻrin oʻngga suriladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>23,5 ÷ 10 = ?</strong></p>",
        "choices": ["235", "23,5", "2,35", "0,235"],
        "correct": "2,35",
        "explanation": "<p><strong>2,35.</strong> 10 ga boʻlinganda vergul bir oʻrin "
                       "chapga suriladi. 100 ga boʻlinsa, ikki oʻrin: 0,235.</p>",
    },
    {
        "text": "<p>Hisoblamasdan aniqlang.</p><p><strong>0,8 × 0,5 ning natijasi "
                "qanday boʻladi?</strong></p>",
        "choices": [
            "0,8 dan katta, chunki koʻpaytiryapmiz",
            "0,8 dan kichik, chunki 0,5 birdan kichik",
            "Aynan 0,8 ga teng",
            "Butun son chiqadi",
        ],
        "correct": "0,8 dan kichik, chunki 0,5 birdan kichik",
        "explanation": "<p>Birdan kichik songa koʻpaytirish natijani kichraytiradi "
                       "(PM-18). Javob 0,4 — bu 0,8 ning yarmi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi hisob "
                "toʻgʻri?</strong></p>",
        "choices": [
            "0,5 × 0,2 = 1",
            "0,5 × 0,2 = 0,1",
            "0,5 × 0,2 = 0,10",
            "0,5 × 0,2 = 10",
        ],
        "correct": "0,5 × 0,2 = 0,1",
        "explanation": "<p>5 × 2 = 10, xonalar 1 + 1 = 2, demak 0,10 — oxirgi nol "
                       "tashlab yuboriladi va javob <strong>0,1</strong> deb "
                       "yoziladi. Son sifatida 0,10 ham shu, lekin tugallangan "
                       "yozuv 0,1.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Afsona ustunda shunday yozdi va <strong>2,5 + 1,25 = 1,50</strong> "
                "deb topdi.</p><p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "U sonlarni oʻng chetidan tekislagan; vergul vergul ostida turishi kerak, "
            "javob 3,75",
            "Hech qanday xato yoʻq",
            "Javob 3,30 boʻlishi kerak edi",
            "Javob 2,75 boʻlishi kerak edi",
        ],
        "correct": "U sonlarni oʻng chetidan tekislagan; vergul vergul ostida turishi "
                   "kerak, javob 3,75",
        "explanation": "<p><strong>2,50 + 1,25 = 3,75.</strong> Tez tekshiruv: "
                       "yigʻindi 2,5 dan katta boʻlishi shart edi, 1,50 esa undan "
                       "kichik — demak allaqachon xato.</p>",
    },
    {
        "text": "<p>Sherbek shunday yozdi: <strong>0,2 × 0,3 = 0,6</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Hech qanday xato yoʻq",
            "Javob 6 boʻlishi kerak edi",
            "Xonalar qoʻshiladi: 1 + 1 = 2, demak javob 0,06",
            "Javob 0,5 boʻlishi kerak edi",
        ],
        "correct": "Xonalar qoʻshiladi: 1 + 1 = 2, demak javob 0,06",
        "explanation": "<p>Sherbek faqat bitta xonani hisobga olgan. Mantiqan ham "
                       "tekshirish mumkin: 0,3 birdan kichik, demak natija 0,2 dan "
                       "kichik boʻlishi kerak — 0,6 esa undan katta.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Samarqandgacha <strong>300 km</strong>. Mashina har 100 km da "
                "<strong>9,5 litr</strong> benzin sarflaydi, benzinning litri "
                "<strong>8 400 soʻm</strong>.</p>"
                "<p><strong>Yoʻlga qancha pul ketadi?</strong></p>",
        "choices": ["79 800 soʻm", "239 400 soʻm", "285 000 soʻm", "478 800 soʻm"],
        "correct": "239 400 soʻm",
        "explanation": "<p><strong>239 400 soʻm.</strong> 300 ÷ 100 = 3, "
                       "3 × 9,5 = 28,5 litr, 28,5 × 8 400 = 239 400. Tekshiruv: "
                       "28 × 8 400 = 235 200 va 0,5 × 8 400 = 4 200; jami 239 400 ✓ "
                       "478 800 javobi borib-kelish uchun chiqadi.</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Sherbek bozordan <strong>2,4 kg</strong> olma oldi. Bir "
                "kilogrammi <strong>15 000 soʻm</strong>.</p>"
                "<p><strong>U qancha toʻladi?</strong></p>",
        "choices": ["3 600 soʻm", "36 000 soʻm", "360 000 soʻm", "17 400 soʻm"],
        "correct": "36 000 soʻm",
        "explanation": "<p><strong>36 000 soʻm.</strong> 24 × 15 = 360, bitta xona "
                       "hisobga olinsa 36,0 ming — yaʼni 36 000 soʻm. Taxmin: "
                       "2,4 taxminan 2,5, 2,5 × 15 000 = 37 500 — javob shu "
                       "atrofda.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-19 Mashq: Aralash sonlar va notoʻgʻri kasrlar",
        "description": "20 savol — notoʻgʻri kasr va aralash son orasidagi oʻtish, "
                       "son oʻqi, aralash sonlarni qoʻshish va ayirish.",
        "tutorial":    "PM-19:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM19,
    },
    {
        "title":       "PM-20 Mashq: Oʻnlik kasrlar",
        "description": "20 savol — vergul va razryadlar, oʻnlik ↔ oddiy kasr, oxirgi "
                       "nollar va oʻnlik kasrlarni taqqoslash.",
        "tutorial":    "PM-20:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM20,
    },
    {
        "title":       "PM-21 Mashq: Oʻnlik kasrlar bilan toʻrt amal",
        "description": "20 savol — ustunda qoʻshish va ayirish, koʻpaytirishda xona "
                       "sanash, vergulni surib boʻlish, 10 va 100 ga amallar.",
        "tutorial":    "PM-21:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM21,
    },
]
