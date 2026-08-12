# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-66, PM-67, PM-68 (toʻrtburchaklar oilasi,
perimetr, yuza 1).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: `medium` (Blok E, 70 gacha).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq: variantlarda x<sup>2</sup> emas,
   Unicode ² yoziladi (m², sm²).
⚠️ Kumulyativ, bu blokda juda muhim:
   • PM-66 mashqida PERIMETR ham, YUZA ham YOʻQ — faqat burchak va taʼrif;
   • PM-67 mashqida YUZA YOʻQ — faqat perimetr;
   • PM-68 mashqida ikkalasi ham bor va aynan ularni farqlash sinaladi.
   • π (PM-70) va oʻxshashlik (PM-72) hech qayerda yoʻq.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_66_68.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Matematika",
    "description": "Matematika — Prime Math darslarining mashqlari",
    "icon":        "bi-calculator",
    "color":       "#f59e0b",
}

DEFAULTS = {
    "level":                "medium",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PM-66 — toʻrtburchaklar oilasi
# =====================================================================

Q_PM66 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Har qanday "
                "toʻrtburchakning burchaklari yigʻindisi qancha?</strong></p>",
        "choices": ["180°", "270°", "360°", "540°"],
        "correct": "360°",
        "explanation": "<p><strong>360°.</strong> Bitta diagonal toʻrtburchakni "
                       "ikkita uchburchakka boʻladi, har birida esa 180°: "
                       "180 + 180 = 360. <strong>180°</strong> — "
                       "uchburchakniki (PM-61), toʻrtburchakniki emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qanday toʻrtburchak "
                "parallelogramm deyiladi?</strong></p>",
        "choices": [
            "Qarama-qarshi tomonlari juft-juft parallel boʻlgani",
            "Faqat bitta juft tomoni parallel boʻlgani",
            "Toʻrtala tomoni teng boʻlgani",
            "Toʻrtala burchagi 90° boʻlgani",
        ],
        "correct": "Qarama-qarshi tomonlari juft-juft parallel boʻlgani",
        "explanation": "<p><strong>Qarama-qarshi tomonlari juft-juft parallel "
                       "boʻlgani.</strong> <strong>Faqat bitta juft</strong> "
                       "parallel boʻlsa — bu trapetsiya. Toʻrtala tomoni "
                       "teng boʻlishi rombning, burchaklari 90° boʻlishi "
                       "esa toʻgʻri toʻrtburchakning qoʻshimcha sharti.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Toʻrtburchakning uch burchagi "
                "80°, 95° va 100°. Toʻrtinchisi qancha?</strong></p>",
        "choices": ["75°", "85°", "95°", "105°"],
        "correct": "85°",
        "explanation": "<p><strong>85°.</strong> 80 + 95 + 100 = 275, keyin "
                       "360 − 275 = 85. Agar 180 dan ayirilsa manfiy son "
                       "chiqadi — bu darhol notoʻgʻri yoʻlni "
                       "koʻrsatadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Tomonlari teng "
                "boʻlgan parallelogramm ___ deyiladi.</strong></p>",
        "choices": ["romb", "trapetsiya", "kvadrat", "toʻgʻri toʻrtburchak"],
        "correct": "romb",
        "explanation": "<p><strong>Romb.</strong> Rombning burchaklari 90° "
                       "boʻlishi shart emas — gilamdagi qiyshiq naqshlar "
                       "ham romb. <strong>Kvadrat</strong> esa rombning "
                       "maxsus holati: unda burchaklar ham 90°.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Trapetsiyada "
                "nechta juft parallel tomon bor?</strong></p>",
        "choices": ["Bitta juft", "Ikkita juft", "Uchta juft", "Birorta ham yoʻq"],
        "correct": "Bitta juft",
        "explanation": "<p><strong>Bitta juft.</strong> Aynan shu bilan "
                       "trapetsiya parallelogrammdan farq qiladi — unda "
                       "ikkala juft ham parallel. Trapetsiyaning parallel "
                       "tomonlari asoslar deyiladi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>Parallelogrammning bitta burchagi "
                "48°. Unga qoʻshni burchak qancha?</strong></p>",
        "choices": ["42°", "48°", "132°", "312°"],
        "correct": "132°",
        "explanation": "<p><strong>132°.</strong> Qoʻshni burchaklar yigʻindisi "
                       "180°: 180 − 48 = 132. <strong>48°</strong> — "
                       "qarama-qarshi burchak, qoʻshni emas; "
                       "<strong>42°</strong> esa 90 − 48, bu yerda hech "
                       "qanday aloqasi yoʻq.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Parallelogrammning bitta burchagi "
                "65°. Unga qarama-qarshi burchak qancha?</strong></p>",
        "choices": ["25°", "65°", "115°", "295°"],
        "correct": "65°",
        "explanation": "<p><strong>65°.</strong> Qarama-qarshi burchaklar teng "
                       "— hisoblash kerak emas. <strong>115°</strong> — "
                       "qoʻshni burchak (180 − 65). Teng boʻlganlari "
                       "roʻparama-roʻpara turadi, yonma-yon emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Toʻrtburchakning burchaklari 90°, "
                "90° va 110°. Toʻrtinchisi qancha?</strong></p>",
        "choices": ["70°", "80°", "90°", "110°"],
        "correct": "70°",
        "explanation": "<p><strong>70°.</strong> 90 + 90 + 110 = 290, va "
                       "360 − 290 = 70. Bunday shakl trapetsiya boʻlishi "
                       "mumkin: ikkita 90° li burchagi bor, lekin "
                       "parallelogramm emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Rombning bitta burchagi 60°. Unga "
                "qoʻshni burchak qancha?</strong></p>",
        "choices": ["30°", "60°", "120°", "300°"],
        "correct": "120°",
        "explanation": "<p><strong>120°.</strong> Romb ham parallelogramm, "
                       "demak unga ham oʻsha qoida ishlaydi: "
                       "180 − 60 = 120. Rombning burchaklari 60°, 120°, "
                       "60°, 120° — yigʻindisi 360 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Parallelogrammning "
                "bitta burchagi 90°. Qolgan uchtasi qanday?</strong></p>",
        "choices": [
            "Uchalasi ham 90° — bu toʻgʻri toʻrtburchak",
            "Ikkitasi 90°, bittasi 180°",
            "Qolganlari 60° dan",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Uchalasi ham 90° — bu toʻgʻri toʻrtburchak",
        "explanation": "<p><strong>Uchalasi ham 90°.</strong> Qoʻshnisi "
                       "180 − 90 = 90, qarama-qarshisi ham 90. Shuning "
                       "uchun usta xonaning faqat <em>bitta</em> burchagini "
                       "tekshiradi — qolgani oʻzidan chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Teng yonli trapetsiyaning katta "
                "asosidagi burchaklari 75° dan. Kichik asosdagi burchaklar "
                "qancha?</strong></p>",
        "choices": ["15°", "75°", "105°", "150°"],
        "correct": "105°",
        "explanation": "<p><strong>105°.</strong> Yon tomon ikki parallel "
                       "asosni kesib oʻtadi, demak yuqori va quyi "
                       "burchaklar bir tomonli ichki burchaklar (PM-60): "
                       "180 − 75 = 105. Tekshirish: "
                       "75 + 75 + 105 + 105 = 360 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Toʻrtburchakning burchaklari "
                "3 : 3 : 2 : 2 nisbatda. Eng katta burchagi qancha?</strong></p>",
        "choices": ["36°", "72°", "108°", "144°"],
        "correct": "108°",
        "explanation": "<p><strong>108°.</strong> Jami ulush: "
                       "3 + 3 + 2 + 2 = 10 ta (PM-27). Bitta ulush: "
                       "360 ÷ 10 = 36°. Eng kattasi 3 ulush: "
                       "3 × 36 = 108°. Burchaklar 108°, 108°, 72°, 72° — "
                       "yigʻindisi 360 ✓ <strong>36°</strong> — bitta "
                       "ulushning oʻzi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Qaysi gap toʻgʻri?</p><p><strong>Kvadrat va romb "
                "haqida.</strong></p>",
        "choices": [
            "Har bir kvadrat — romb",
            "Har bir romb — kvadrat",
            "Kvadrat ham, romb ham parallelogramm emas",
            "Rombning burchaklari har doim 90°",
        ],
        "correct": "Har bir kvadrat — romb",
        "explanation": "<p><strong>Har bir kvadrat — romb.</strong> Kvadratning "
                       "toʻrtala tomoni teng, demak u rombning shartini "
                       "bajaradi. Teskarisi notoʻgʻri: burchagi 60° va "
                       "120° boʻlgan romb kvadrat emas. Ikkalasi ham "
                       "parallelogramm oilasiga kiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Trapetsiya "
                "parallelogrammning bir turimi?</strong></p>",
        "choices": [
            "Yoʻq — unda faqat bitta juft tomon parallel",
            "Ha — har qanday trapetsiya parallelogramm",
            "Ha, agar yon tomonlari teng boʻlsa",
            "Ha, agar burchaklari 90° boʻlsa",
        ],
        "correct": "Yoʻq — unda faqat bitta juft tomon parallel",
        "explanation": "<p><strong>Yoʻq.</strong> Parallelogrammda "
                       "<em>ikkala</em> juft tomon parallel, trapetsiyada "
                       "esa faqat bittasi. Yon tomonlari teng boʻlsa u "
                       "teng yonli trapetsiya boʻladi — baribir "
                       "parallelogramm emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Parallelogrammda "
                "qaysi burchaklar teng?</strong></p>",
        "choices": [
            "Qarama-qarshi turganlari",
            "Qoʻshni turganlari",
            "Hammasi teng",
            "Faqat asosdagilari",
        ],
        "correct": "Qarama-qarshi turganlari",
        "explanation": "<p><strong>Qarama-qarshi turganlari</strong> teng, "
                       "qoʻshnilari esa 180° ni beradi. Hammasi teng "
                       "boʻlishi faqat toʻgʻri toʻrtburchak va kvadratda "
                       "sodir boʻladi — u yerda toʻrttasi ham 90°.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Shaklning toʻrtala "
                "tomoni 12 sm, burchaklaridan biri esa 90°. Bu qanday "
                "shakl?</strong></p>",
        "choices": ["Kvadrat", "Faqat romb", "Trapetsiya", "Aniqlab boʻlmaydi"],
        "correct": "Kvadrat",
        "explanation": "<p><strong>Kvadrat.</strong> Toʻrtala tomoni teng — "
                       "demak romb, yaʼni parallelogramm. Parallelogrammda "
                       "bitta burchak 90° boʻlsa, qolgan uchtasi ham 90° "
                       "boʻladi. Tomonlari teng + burchaklari 90° = "
                       "kvadrat.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Parallelogrammning "
                "bitta burchagi 65°. Unga qoʻshni burchakni toping.</strong></p>",
        "choices": [
            "180 − 65 = 115°",
            "65° — qoʻshni burchaklar teng",
            "360 − 65 = 295°",
            "90 − 65 = 25°",
        ],
        "correct": "180 − 65 = 115°",
        "explanation": "<p><strong>180 − 65 = 115°.</strong> Qoʻshni burchaklar "
                       "bir tomonli ichki burchaklar boʻlgani uchun 180° "
                       "ni beradi (PM-60). <strong>65°</strong> javobi eng "
                       "koʻp uchraydigan xato: teng boʻlganlari "
                       "qarama-qarshi turganlar, qoʻshnilar emas.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>«Toʻrtburchakning uch "
                "burchagi 100°, 80° va 90°. (1) Ularning yigʻindisi 270°. "
                "(2) Toʻrtburchakda burchaklar yigʻindisi 180°. "
                "(3) Toʻrtinchi burchak 180 − 270 = −90°.»</strong></p>",
        "choices": [
            "2-qatorda — toʻrtburchakda yigʻindi 360°, demak javob 90°",
            "1-qatorda — yigʻindi 270° emas",
            "3-qatorda — ayirish tartibi notoʻgʻri",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "2-qatorda — toʻrtburchakda yigʻindi 360°, demak javob 90°",
        "explanation": "<p><strong>2-qatorda xato.</strong> 180° — uchburchakniki. "
                       "Toʻrtburchakda 360°, demak toʻrtinchi burchak "
                       "360 − 270 = 90°. Birinchi qator toʻgʻri edi: "
                       "100 + 80 + 90 = 270. Burchak manfiy chiqishi har "
                       "doim qoida notoʻgʻri olinganini bildiradi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Karim aka darvozaga naqshli panel yasayapti. Panel "
                "parallelogramm shaklida va uning bitta burchagi 72°.</p>"
                "<p><strong>Panelning eng katta burchagi necha "
                "gradus?</strong></p>",
        "choices": ["72°", "108°", "144°", "288°"],
        "correct": "108°",
        "explanation": "<p><strong>108°.</strong> Parallelogrammning burchaklari "
                       "72°, 108°, 72°, 108°: qarama-qarshisi 72°, "
                       "qoʻshnisi 180 − 72 = 108°. Eng kattasi — 108°. "
                       "Tekshirish: 72 + 108 + 72 + 108 = 360 ✓</p>",
    },
    {
        "text": "<p>Dilnoza gilamdagi naqshni oʻlchadi. Naqshning toʻrtala "
                "tomoni ham teng, eng katta burchagi esa 110°.</p>"
                "<p><strong>Naqshning eng kichik burchagi necha "
                "gradus?</strong></p>",
        "choices": ["55°", "70°", "90°", "110°"],
        "correct": "70°",
        "explanation": "<p><strong>70°.</strong> Toʻrtala tomoni teng — demak "
                       "romb, yaʼni parallelogramm. Qoʻshni burchak: "
                       "180 − 110 = 70°. Burchaklar 110°, 70°, 110°, 70° — "
                       "yigʻindisi 360 ✓ <strong>55°</strong> — 110 ning "
                       "yarmi, bu yerda hech qanday asosi yoʻq.</p>",
    },
]


# =====================================================================
# PM-67 — perimetr
# =====================================================================

Q_PM67 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Perimetr nima?"
                "</strong></p>",
        "choices": [
            "Shaklni oʻrab turgan chiziqning uzunligi",
            "Shakl ichiga sigʻadigan kataklar soni",
            "Eng uzun tomonning uzunligi",
            "Ikki qarama-qarshi tomonning yigʻindisi",
        ],
        "correct": "Shaklni oʻrab turgan chiziqning uzunligi",
        "explanation": "<p><strong>Shaklni oʻrab turgan chiziqning "
                       "uzunligi.</strong> Perimetr — chegara boʻylab bir "
                       "marta aylanib chiqqanda bosib oʻtilgan yoʻl, "
                       "yaʼni hamma tomonlarning yigʻindisi. Metr yoki "
                       "santimetrda oʻlchanadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Toʻgʻri toʻrtburchakning tomonlari "
                "14 sm va 6 sm. Perimetri qancha?</strong></p>",
        "choices": ["20 sm", "26 sm", "40 sm", "84 sm"],
        "correct": "40 sm",
        "explanation": "<p><strong>40 sm.</strong> P = 2 × (14 + 6) = 2 × 20 = "
                       "40. <strong>20 sm</strong> — faqat ikkita tomon "
                       "(14 + 6); ikkilantirish unutilgan. Toʻrtburchakda "
                       "toʻrtta tomon bor.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Kvadratning tomoni 9 m. Perimetri "
                "qancha?</strong></p>",
        "choices": ["18 m", "27 m", "36 m", "81 m"],
        "correct": "36 m",
        "explanation": "<p><strong>36 m.</strong> Toʻrtala tomon teng: "
                       "P = 4 × 9 = 36. <strong>81 m</strong> — tomonni "
                       "oʻziga koʻpaytirish; bu perimetr bermaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Uchburchakning tomonlari 6, 8 va "
                "10 sm. Perimetri qancha?</strong></p>",
        "choices": ["18 sm", "24 sm", "28 sm", "48 sm"],
        "correct": "24 sm",
        "explanation": "<p><strong>24 sm.</strong> 6 + 8 + 10 = 24. "
                       "Uchburchakda formula shart emas — hamma tomonni "
                       "qoʻshsangiz boʻldi. Bu yerda ikkilantirish "
                       "<em>kerak emas</em>: har bir tomon bitta.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Bogʻning tomonlari 15 m va 9 m. "
                "Uni oʻrab turgan chiziq necha metr?</strong></p>",
        "choices": ["24 m", "33 m", "48 m", "135 m"],
        "correct": "48 m",
        "explanation": "<p><strong>48 m.</strong> P = 2 × (15 + 9) = 2 × 24 = "
                       "48. <strong>24 m</strong> — ikkita tomonning "
                       "yigʻindisi, butun chegara emas.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>Kvadratning perimetri 52 sm. "
                "Tomoni qancha?</strong></p>",
        "choices": ["13 sm", "26 sm", "48 sm", "208 sm"],
        "correct": "13 sm",
        "explanation": "<p><strong>13 sm.</strong> Toʻrtala tomon teng, demak "
                       "52 ÷ 4 = 13. Tekshirish: 4 × 13 = 52 ✓ "
                       "<strong>26 sm</strong> — ikkiga boʻlingan javob; "
                       "kvadratda toʻrtga boʻlinadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Toʻgʻri toʻrtburchakning perimetri "
                "30 m, eni 4 m. Uzunligi qancha?</strong></p>",
        "choices": ["7 m", "11 m", "13 m", "26 m"],
        "correct": "11 m",
        "explanation": "<p><strong>11 m.</strong> 2 × (a + 4) = 30 → "
                       "a + 4 = 15 → a = 11. Tekshirish: "
                       "2 × (11 + 4) = 30 ✓ <strong>26 m</strong> — "
                       "30 − 4, yaʼni avval 2 ga boʻlish qadami tushib "
                       "qolgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Toʻgʻri toʻrtburchakning perimetri "
                "36 sm, uzunligi 12 sm. Eni qancha?</strong></p>",
        "choices": ["6 sm", "12 sm", "18 sm", "24 sm"],
        "correct": "6 sm",
        "explanation": "<p><strong>6 sm.</strong> 2 × (12 + b) = 36 → "
                       "12 + b = 18 → b = 6. Tekshirish: "
                       "2 × (12 + 6) = 36 ✓ <strong>24 sm</strong> — "
                       "36 − 12, bu esa perimetrni bitta tomonlar juftligi "
                       "deb hisoblaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>L shaklidagi maydonning tomonlari "
                "12 m, 3 m, 7 m, 5 m, 5 m va 8 m. Perimetri qancha?</strong></p>",
        "choices": ["30 m", "35 m", "40 m", "96 m"],
        "correct": "40 m",
        "explanation": "<p><strong>40 m.</strong> Hamma tomonni chegara boʻylab "
                       "qoʻshamiz: 12 + 3 + 7 + 5 + 5 + 8 = 40. Tez "
                       "tekshiruv: uni oʻrab turgan toʻrtburchak 12 × 8, "
                       "va 2 × (12 + 8) = 40 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>L shaklidagi maydonni oʻrab turgan "
                "eng kichik toʻgʻri toʻrtburchak 9 m × 7 m. L shaklning "
                "perimetri qancha?</strong></p>",
        "choices": ["16 m", "23 m", "32 m", "63 m"],
        "correct": "32 m",
        "explanation": "<p><strong>32 m.</strong> «Zinapoyali» shaklda "
                       "gorizontal tomonlar yigʻindisi eng uzun "
                       "gorizontalga, vertikallariniki eng uzun "
                       "vertikalga teng — demak perimetr oʻrovchi "
                       "toʻrtburchaknikiga teng: 2 × (9 + 7) = 32. "
                       "Oʻyiqning qayerdaligi javobni oʻzgartirmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Kvadratning tomoni 2,5 m. "
                "Perimetri qancha?</strong></p>",
        "choices": ["6,25 m", "7,5 m", "10 m", "12,5 m"],
        "correct": "10 m",
        "explanation": "<p><strong>10 m.</strong> P = 4 × 2,5 = 10. "
                       "<strong>6,25 m</strong> — 2,5 × 2,5, yaʼni tomonni "
                       "oʻziga koʻpaytirish; <strong>7,5 m</strong> esa "
                       "faqat uchta tomon.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Toʻgʻri toʻrtburchakning tomonlari "
                "80 sm va 1,2 m. Perimetri necha metr?</strong></p>",
        "choices": ["2 m", "4 m", "81,2 m", "162,4 m"],
        "correct": "4 m",
        "explanation": "<p><strong>4 m.</strong> Avval birliklarni "
                       "tenglashtiramiz: 80 sm = 0,8 m. Keyin "
                       "P = 2 × (0,8 + 1,2) = 2 × 2 = 4 m. "
                       "<strong>162,4 m</strong> — birliklarni "
                       "almashtirmasdan qoʻshish natijasi; bunday javob "
                       "hech qanday maʼnoga ega emas.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Toʻgʻri "
                "toʻrtburchakning perimetri qaysi formula bilan "
                "topiladi?</strong></p>",
        "choices": [
            "P = 2 × (a + b)",
            "P = a + b",
            "P = a × b",
            "P = 4 × a",
        ],
        "correct": "P = 2 × (a + b)",
        "explanation": "<p><strong>P = 2 × (a + b).</strong> "
                       "<strong>a + b</strong> — faqat ikkita tomon; "
                       "<strong>4 × a</strong> — kvadratniki, chunki u "
                       "yerda toʻrtala tomon teng. Qarama-qarshi tomonlar "
                       "teng boʻlgani uchun har bir son ikki marta "
                       "qoʻshiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Kvadratning tomoni "
                "7 sm. Quyidagilardan qaysi biri uning perimetri?</strong></p>",
        "choices": ["14 sm", "28 sm", "49 sm", "56 sm"],
        "correct": "28 sm",
        "explanation": "<p><strong>28 sm.</strong> P = 4 × 7 = 28. "
                       "<strong>49 sm</strong> — 7 × 7, yaʼni tomonni "
                       "oʻziga koʻpaytirish: bu perimetr emas. "
                       "<strong>14 sm</strong> — faqat ikkita tomon.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki shaklning "
                "perimetri bir xil boʻlishi mumkinmi?</strong></p>",
        "choices": [
            "Ha — masalan 5 × 5 kvadrat va 8 × 2 toʻrtburchak, ikkalasi ham 20",
            "Yoʻq — har bir shaklning perimetri boshqacha",
            "Faqat ikkala shakl ham kvadrat boʻlsa",
            "Faqat tomonlari teng boʻlsa",
        ],
        "correct": "Ha — masalan 5 × 5 kvadrat va 8 × 2 toʻrtburchak, ikkalasi ham 20",
        "explanation": "<p><strong>Ha.</strong> 4 × 5 = 20 va "
                       "2 × (8 + 2) = 20 — tomonlari butunlay boshqacha, "
                       "chegaralari esa bir xil uzunlikda. Perimetr "
                       "shaklning shaklini emas, faqat chegarasining "
                       "uzunligini oʻlchaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Tomonlari 50 sm va "
                "0,5 m boʻlgan shakl haqida nima deyish mumkin?</strong></p>",
        "choices": [
            "Bu kvadrat — chunki 50 sm = 0,5 m",
            "Bu toʻgʻri toʻrtburchak, tomonlari har xil",
            "Bunday shakl boʻlishi mumkin emas",
            "Perimetrini hisoblab boʻlmaydi",
        ],
        "correct": "Bu kvadrat — chunki 50 sm = 0,5 m",
        "explanation": "<p><strong>Bu kvadrat.</strong> 50 sm va 0,5 m — bitta "
                       "uzunlikning ikki xil yozuvi, demak tomonlar teng. "
                       "Perimetri: 4 × 0,5 = 2 m. Birliklarni "
                       "tenglashtirmasdan turib shaklni ham, javobni ham "
                       "notoʻgʻri aniqlab qoʻyish oson.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Tomonlari 15 m va 9 m "
                "boʻlgan bogʻning perimetrini toping.</strong></p>",
        "choices": [
            "2 × (15 + 9) = 48 m",
            "15 + 9 = 24 m",
            "15 × 9 = 135 m",
            "2 × 15 + 9 = 39 m",
        ],
        "correct": "2 × (15 + 9) = 48 m",
        "explanation": "<p><strong>2 × (15 + 9) = 48 m.</strong> "
                       "<strong>24 m</strong> — ikkilantirish unutilgan "
                       "(eng koʻp uchraydigan xato). <strong>39 m</strong> "
                       "— faqat bitta tomon ikkilantirilgan. "
                       "<strong>135 m</strong> — tomonlarni koʻpaytirish, "
                       "bu perimetr bermaydi.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>«Perimetri 36 sm, uzunligi "
                "12 sm. (1) 2 × (12 + b) = 36. (2) 12 + b = 18. "
                "(3) b = 18 + 12 = 30 sm.»</strong></p>",
        "choices": [
            "3-qatorda — qoʻshish emas, ayirish: b = 18 − 12 = 6 sm",
            "1-qatorda — formula notoʻgʻri",
            "2-qatorda — 36 ni 2 ga boʻlish notoʻgʻri",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "3-qatorda — qoʻshish emas, ayirish: b = 18 − 12 = 6 sm",
        "explanation": "<p><strong>3-qatorda xato.</strong> 12 + b = 18 "
                       "tenglamasida b ni topish uchun 12 <em>ayiriladi</em> "
                       "(PM-36): b = 6. Birinchi ikki qator toʻgʻri. "
                       "Tekshirish javobni darrov rad etadi: "
                       "2 × (12 + 30) = 84, 36 emas.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Sherbekning oilasi toʻgʻri toʻrtburchak shaklidagi bogʻni "
                "panjara bilan oʻramoqchi. Bogʻning uzunligi 20 m, eni 12 m. "
                "Bir joyda 4 metrlik darvoza qoldiriladi. Panjaraning bir "
                "metri 30 000 soʻm.</p><p><strong>Panjara uchun jami qancha "
                "pul kerak?</strong></p>",
        "choices": ["1 680 000 soʻm", "1 800 000 soʻm", "1 920 000 soʻm", "7 200 000 soʻm"],
        "correct": "1 800 000 soʻm",
        "explanation": "<p><strong>1 800 000 soʻm.</strong> Perimetr: "
                       "2 × (20 + 12) = 64 m. Darvozani ayiramiz: "
                       "64 − 4 = 60 m. Narxi: 60 × 30 000 = 1 800 000. "
                       "<strong>1 920 000</strong> — darvoza ayirilmagan "
                       "javob (64 × 30 000).</p>",
    },
    {
        "text": "<p>Afsona 25 sm × 35 sm oʻlchamdagi rasmning chetiga bezak "
                "lenta yopishtirmoqchi. Lentaning bir metri 15 000 soʻm "
                "turadi.</p><p><strong>Lenta necha soʻm turadi?</strong></p>",
        "choices": ["9000 soʻm", "18 000 soʻm", "180 000 soʻm", "1 800 000 soʻm"],
        "correct": "18 000 soʻm",
        "explanation": "<p><strong>18 000 soʻm.</strong> Perimetr: "
                       "2 × (25 + 35) = 120 sm. Birlikni keltiramiz: "
                       "120 sm = 1,2 m. Narxi: 1,2 × 15 000 = 18 000. "
                       "<strong>1 800 000</strong> — santimetrni metrga "
                       "aylantirmasdan hisoblangan javob, yaʼni yuz "
                       "barobar katta.</p>",
    },
]


# =====================================================================
# PM-68 — yuza 1
# =====================================================================

Q_PM68 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Yuza nima?</strong></p>",
        "choices": [
            "Shakl ichiga sigʻadigan birlik kvadratlar soni",
            "Shaklni oʻrab turgan chiziqning uzunligi",
            "Eng uzun tomonning uzunligi",
            "Tomonlar sonining oʻzi",
        ],
        "correct": "Shakl ichiga sigʻadigan birlik kvadratlar soni",
        "explanation": "<p><strong>Shakl ichiga sigʻadigan birlik kvadratlar "
                       "soni.</strong> Chegara uzunligi — bu perimetr "
                       "(PM-67). Yuza shaklning <em>ichini</em> oʻlchaydi "
                       "va sm² yoki m² da yoziladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Toʻgʻri toʻrtburchakning tomonlari "
                "9 sm va 7 sm. Yuzasi qancha?</strong></p>",
        "choices": ["16 sm²", "32 sm²", "63 sm²", "126 sm²"],
        "correct": "63 sm²",
        "explanation": "<p><strong>63 sm².</strong> S = 9 × 7 = 63. "
                       "<strong>32 sm²</strong> — bu aslida perimetr "
                       "(2 × (9 + 7)), yuza emas — birligiga ham "
                       "eʼtibor bering.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Kvadratning tomoni 12 m. Yuzasi "
                "qancha?</strong></p>",
        "choices": ["24 m²", "48 m²", "144 m²", "1440 m²"],
        "correct": "144 m²",
        "explanation": "<p><strong>144 m².</strong> S = 12 × 12 = 12² = 144. "
                       "<strong>48 m²</strong> — bu perimetr (4 × 12). "
                       "«Kvadrat» soʻzi bejiz emas: tomonni oʻziga "
                       "koʻpaytirish aynan kvadrat yuzasidan chiqqan "
                       "(PM-12).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Uchburchakning asosi 14 sm, "
                "balandligi 6 sm. Yuzasi qancha?</strong></p>",
        "choices": ["20 sm²", "42 sm²", "84 sm²", "168 sm²"],
        "correct": "42 sm²",
        "explanation": "<p><strong>42 sm².</strong> (14 × 6) ÷ 2 = 84 ÷ 2 = 42. "
                       "<strong>84 sm²</strong> — ikkiga boʻlish qadami "
                       "tushib qolgan; u uchburchakni oʻrab turgan "
                       "toʻrtburchakning yuzasi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>1 m² = ___ sm²"
                "</strong></p>",
        "choices": ["100", "1000", "10 000", "1 000 000"],
        "correct": "10 000",
        "explanation": "<p><strong>10 000.</strong> 1 m = 100 sm, lekin yuza "
                       "ikkala tomonga oʻsadi: 100 × 100 = 10 000. "
                       "<strong>100</strong> — uzunlik uchun toʻgʻri, yuza "
                       "uchun emas. Bu mavzudagi eng qimmat xato.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>Xona 5 m × 4 m. Polining yuzasi "
                "qancha?</strong></p>",
        "choices": ["9 m²", "18 m²", "20 m²", "40 m²"],
        "correct": "20 m²",
        "explanation": "<p><strong>20 m².</strong> S = 5 × 4 = 20. "
                       "<strong>18 m²</strong> — 2 × (5 + 4), yaʼni "
                       "perimetr formulasi. Yuza uchun tomonlar "
                       "koʻpaytiriladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Uchburchakning asosi 10 sm, "
                "balandligi 6 sm. Yuzasi qancha?</strong></p>",
        "choices": ["16 sm²", "30 sm²", "32 sm²", "60 sm²"],
        "correct": "30 sm²",
        "explanation": "<p><strong>30 sm².</strong> (10 × 6) ÷ 2 = 30. "
                       "<strong>60 sm²</strong> — oʻrab turgan "
                       "toʻrtburchakning yuzasi; uchburchak uning aynan "
                       "yarmi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Toʻgʻri toʻrtburchakning yuzasi "
                "72 sm², eni 8 sm. Uzunligi qancha?</strong></p>",
        "choices": ["9 sm", "28 sm", "64 sm", "576 sm"],
        "correct": "9 sm",
        "explanation": "<p><strong>9 sm.</strong> S = a × b, demak "
                       "a = 72 ÷ 8 = 9. Tekshirish: 9 × 8 = 72 ✓ "
                       "<strong>64 sm</strong> — 72 − 8, yaʼni "
                       "koʻpaytirishning teskarisi ayirish deb "
                       "olingan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Kvadratning yuzasi 49 m². Tomoni "
                "qancha?</strong></p>",
        "choices": ["7 m", "12,25 m", "24,5 m", "196 m"],
        "correct": "7 m",
        "explanation": "<p><strong>7 m.</strong> Tomoni oʻziga koʻpaytirilganda "
                       "49 chiqadi, demak √49 = 7 (PM-13). "
                       "<strong>24,5 m</strong> — 49 ni ikkiga boʻlish; "
                       "kvadratning teskarisi ildiz, boʻlish emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>L shaklidagi maydon ikkita "
                "toʻrtburchakka boʻlinadi: 12 m × 3 m va 5 m × 5 m. Umumiy "
                "yuzasi qancha?</strong></p>",
        "choices": ["40 m²", "61 m²", "96 m²", "131 m²"],
        "correct": "61 m²",
        "explanation": "<p><strong>61 m².</strong> 12 × 3 = 36 va 5 × 5 = 25, "
                       "yigʻindisi 36 + 25 = 61. Boshqa yoʻl bilan "
                       "tekshirish: oʻrovchi toʻrtburchak 12 × 8 = 96, "
                       "oʻyiq 7 × 5 = 35, va 96 − 35 = 61 ✓ "
                       "<strong>40 m²</strong> — bu shu shaklning "
                       "perimetri, yuzasi emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Hovli 20 m × 15 m. Uning bir "
                "burchagida 6 m × 5 m gulzor bor. Gulzordan tashqari yuza "
                "qancha?</strong></p>",
        "choices": ["30 m²", "240 m²", "270 m²", "300 m²"],
        "correct": "270 m²",
        "explanation": "<p><strong>270 m².</strong> Butun hovli: "
                       "20 × 15 = 300 m². Gulzor: 6 × 5 = 30 m². "
                       "Ayiramiz: 300 − 30 = 270. Murakkab shaklda "
                       "«ortiqchasini ayirish» ham, «boʻlaklarni qoʻshish» "
                       "ham ishlaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Uchburchakning asosi 20 sm, "
                "balandligi 9 sm. Yuzasi qancha?</strong></p>",
        "choices": ["29 sm²", "58 sm²", "90 sm²", "180 sm²"],
        "correct": "90 sm²",
        "explanation": "<p><strong>90 sm².</strong> (20 × 9) ÷ 2 = 180 ÷ 2 = 90. "
                       "<strong>180 sm²</strong> — ikkiga boʻlinmagan "
                       "javob; <strong>58 sm²</strong> esa "
                       "2 × (20 + 9), yaʼni perimetr formulasi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Tomonlari 9 sm va "
                "7 sm boʻlgan toʻgʻri toʻrtburchakning perimetri va yuzasi "
                "qanday?</strong></p>",
        "choices": [
            "Perimetri 32 sm, yuzasi 63 sm²",
            "Perimetri 63 sm, yuzasi 32 sm²",
            "Ikkalasi ham 63",
            "Ikkalasi ham 32",
        ],
        "correct": "Perimetri 32 sm, yuzasi 63 sm²",
        "explanation": "<p><strong>Perimetri 32 sm, yuzasi 63 sm².</strong> "
                       "Perimetr — chegara: 2 × (9 + 7) = 32 sm. Yuza — "
                       "ichi: 9 × 7 = 63 sm². Birligiga qarab qaysi biri "
                       "ekanini darrov bilasiz: perimetr sm da, yuza "
                       "sm² da.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Xonaning poli "
                "3 m × 2 m. Bu necha sm²?</strong></p>",
        "choices": ["6 sm²", "600 sm²", "6000 sm²", "60 000 sm²"],
        "correct": "60 000 sm²",
        "explanation": "<p><strong>60 000 sm².</strong> Yuzasi 3 × 2 = 6 m², va "
                       "1 m² = 10 000 sm², demak 6 × 10 000 = 60 000. "
                       "<strong>600 sm²</strong> — 100 ga koʻpaytirish, "
                       "yaʼni uzunlik qoidasini yuzaga qoʻllash.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Uchburchakning "
                "asosi 10 sm, yon tomoni 8 sm, balandligi 6 sm. Yuzasini "
                "topish uchun qaysi sonlar kerak?</strong></p>",
        "choices": [
            "Asos va balandlik: (10 × 6) ÷ 2 = 30 sm²",
            "Asos va yon tomon: (10 × 8) ÷ 2 = 40 sm²",
            "Yon tomon va balandlik: (8 × 6) ÷ 2 = 24 sm²",
            "Uchala tomon: 10 + 8 + 6 = 24 sm²",
        ],
        "correct": "Asos va balandlik: (10 × 6) ÷ 2 = 30 sm²",
        "explanation": "<p><strong>Asos va balandlik.</strong> Formulada faqat "
                       "asosga <em>perpendikulyar</em> boʻlgan balandlik "
                       "ishlaydi. Yon tomon qiya turadi va balandlikdan "
                       "uzun — u gipotenuza (PM-64). Chizmadagi 90° "
                       "belgisini qidiring.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki shaklning "
                "perimetri bir xil — 20 sm. Yuzalari ham bir xilmi?</strong></p>",
        "choices": [
            "Shart emas: 5 × 5 kvadratda 25 sm², 8 × 2 toʻrtburchakda 16 sm²",
            "Ha — perimetri teng shakllarning yuzasi ham teng",
            "Yoʻq — yuzalari hech qachon teng boʻlmaydi",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Shart emas: 5 × 5 kvadratda 25 sm², 8 × 2 toʻrtburchakda 16 sm²",
        "explanation": "<p><strong>Shart emas.</strong> Ikkalasining ham "
                       "perimetri 20 sm, lekin yuzalari 25 sm² va 16 sm². "
                       "Perimetr chegarani, yuza esa ichini oʻlchaydi — "
                       "biri ikkinchisini belgilamaydi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Xona 5 m × 4 m. "
                "Polining yuzasini toping.</strong></p>",
        "choices": [
            "S = 5 × 4 = 20 m²",
            "S = 2 × (5 + 4) = 18 m²",
            "S = 5 + 4 = 9 m²",
            "S = (5 × 4) ÷ 2 = 10 m²",
        ],
        "correct": "S = 5 × 4 = 20 m²",
        "explanation": "<p><strong>S = 5 × 4 = 20 m².</strong> "
                       "<strong>18 m²</strong> — perimetr formulasi "
                       "(PM-67). <strong>10 m²</strong> — uchburchak "
                       "formulasi; toʻgʻri toʻrtburchakda ikkiga boʻlish "
                       "kerak emas.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>«Uchburchakning asosi "
                "12 sm, balandligi 5 sm. (1) Oʻrab turgan toʻrtburchak: "
                "12 × 5 = 60. (2) Uchburchak uning yarmi. "
                "(3) Javob: 60 sm².»</strong></p>",
        "choices": [
            "3-qatorda — ikkiga boʻlish bajarilmagan: 60 ÷ 2 = 30 sm²",
            "1-qatorda — 12 × 5 = 60 emas",
            "2-qatorda — uchburchak yarmi emas",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "3-qatorda — ikkiga boʻlish bajarilmagan: 60 ÷ 2 = 30 sm²",
        "explanation": "<p><strong>3-qatorda xato.</strong> Ikkinchi qatorning "
                       "oʻzi toʻgʻri javobni aytib turibdi — «yarmi» — "
                       "lekin hisobda bajarilmagan: 60 ÷ 2 = 30 sm². "
                       "Formulani yozib qoʻyib, oxirgi qadamni unutish "
                       "eng koʻp uchraydigan xato.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Sinf xonasining uzunligi 9 metr, eni 5 metr. Polga tomoni "
                "50 santimetr boʻlgan kvadrat plitka yotqiziladi. Usta "
                "sindirib qoʻyish uchun hisobdan 10 foiz koʻp olishni "
                "maslahat berdi.</p><p><strong>Jami nechta plitka sotib olish "
                "kerak?</strong></p>",
        "choices": ["99 ta", "180 ta", "198 ta", "450 ta"],
        "correct": "198 ta",
        "explanation": "<p><strong>198 ta.</strong> Xona yuzasi: "
                       "9 × 5 = 45 m². Plitka: 50 sm = 0,5 m, demak "
                       "0,5 × 0,5 = 0,25 m². Kerak: 45 ÷ 0,25 = 180 ta. "
                       "10 foiz zaxira: 180 ÷ 100 × 10 = 18, va "
                       "180 + 18 = 198. <strong>180 ta</strong> — "
                       "zaxirasiz javob.</p>",
    },
    {
        "text": "<p>Bekzod xonasining bitta devorini boʻyamoqchi. Devorning "
                "uzunligi 6 metr, balandligi 3 metr. Bir banka boʻyoq 8 "
                "kvadrat metr yuzaga yetadi.</p><p><strong>Necha banka boʻyoq "
                "sotib olish kerak?</strong></p>",
        "choices": ["2 banka", "3 banka", "4 banka", "18 banka"],
        "correct": "3 banka",
        "explanation": "<p><strong>3 banka.</strong> Devorning yuzasi: "
                       "6 × 3 = 18 m². Bankalar soni: 18 ÷ 8 = 2,25. "
                       "Bankani boʻlib sotib boʻlmaydi, shuning uchun "
                       "javob <em>yuqoriga</em> yaxlitlanadi: 3 banka "
                       "(PM-14). <strong>2 banka</strong> bilan "
                       "16 m² boʻyaladi — devorga yetmaydi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-66 Mashq: Toʻrtburchaklar oilasi",
        "tutorial":    "PM-66:",
        "description": (
            "Toʻrtburchakda 360°, parallelogrammning xossalari, kvadrat, "
            "romb va trapetsiyaning farqi. 20 savol."
        ),
        "questions":   Q_PM66,
        **DEFAULTS,
    },
    {
        "title":       "PM-67 Mashq: Perimetr",
        "tutorial":    "PM-67:",
        "description": (
            "Chegara uzunligi: toʻgʻri toʻrtburchak va kvadrat formulalari, "
            "murakkab shakl, teskari masala va birliklar. 20 savol."
        ),
        "questions":   Q_PM67,
        **DEFAULTS,
    },
    {
        "title":       "PM-68 Mashq: Yuza 1: toʻgʻri toʻrtburchak va uchburchak",
        "tutorial":    "PM-68:",
        "description": (
            "Yuza birlik kvadratlar orqali, S = a × b, uchburchak yuzasi "
            "va perimetr bilan farqi. 20 savol."
        ),
        "questions":   Q_PM68,
        **DEFAULTS,
    },
]
