# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-69, PM-70, PM-71 (yuza 2, doira va π,
aylana uzunligi va doira yuzasi).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: PM-69 va PM-70 `medium`, PM-71 dan boshlab `hard` (STYLE_GUIDE 1-boʻlim).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq: variantlarda x<sup>2</sup> emas,
   Unicode ² yoziladi (m², sm²).
⚠️ Kumulyativ:
   • PM-69 mashqida DOIRA ham, π ham YOʻQ — faqat toʻgʻri chiziqli shakllar;
   • PM-70 mashqida faqat doiraning QISMLARI va π = L ÷ d munosabati.
     ⛔ DOIRA YUZASI bu testda umuman yoʻq;
   • PM-71 mashqida ikkala formula ham va aynan ularni farqlash sinaladi.
   • Oʻxshashlik (PM-72) va hajm (PM-74) hech qayerda yoʻq.
⚠️ Hamma joyda π ≈ 3,14.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_69_71.py --master=prime \\
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
# PM-69 — yuza 2: parallelogramm, trapetsiya, murakkab shakllar
# =====================================================================

Q_PM69 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>Parallelogrammning asosi 7 sm, "
                "balandligi 4 sm. Yuzasi qancha?</strong></p>",
        "choices": ["11 sm²", "14 sm²", "22 sm²", "28 sm²"],
        "correct": "28 sm²",
        "explanation": "<p><strong>28 sm².</strong> S = a × h = 7 × 4 = 28. "
                       "<strong>14 sm²</strong> — uchburchak formulasi bilan "
                       "ikkiga boʻlingan; parallelogrammda boʻlish yoʻq. "
                       "<strong>22 sm²</strong> — bu perimetr: 2 × (7 + 4). "
                       "<strong>11 sm²</strong> — tomonlar shunchaki "
                       "qoʻshilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Trapetsiyaning asoslari 10 sm va "
                "6 sm, balandligi 5 sm. Yuzasi qancha?</strong></p>",
        "choices": ["21 sm²", "40 sm²", "50 sm²", "80 sm²"],
        "correct": "40 sm²",
        "explanation": "<p><strong>40 sm².</strong> S = (a + b) ÷ 2 × h = "
                       "(10 + 6) ÷ 2 × 5 = 8 × 5 = 40. <strong>80 sm²</strong> — "
                       "ikkiga boʻlish qadami tushib qolgan, shuning uchun javob "
                       "aynan ikki barobar katta. <strong>50 sm²</strong> — faqat "
                       "katta asos ishlatilgan (10 × 5); trapetsiyada ikkala asos "
                       "ham kerak.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Rombning diagonallari 12 sm va "
                "5 sm. Yuzasi qancha?</strong></p>",
        "choices": ["17 sm²", "30 sm²", "34 sm²", "60 sm²"],
        "correct": "30 sm²",
        "explanation": "<p><strong>30 sm².</strong> S = d₁ × d₂ ÷ 2 = "
                       "12 × 5 ÷ 2 = 60 ÷ 2 = 30. <strong>60 sm²</strong> — "
                       "ikkiga boʻlish unutilgan; 60 — rombni oʻrab turgan "
                       "toʻgʻri toʻrtburchakning yuzasi, romb esa uning "
                       "yarmini egallaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Parallelogrammning asosi 15 sm, "
                "balandligi 6 sm. Yuzasi qancha?</strong></p>",
        "choices": ["21 sm²", "42 sm²", "45 sm²", "90 sm²"],
        "correct": "90 sm²",
        "explanation": "<p><strong>90 sm².</strong> S = 15 × 6 = 90. "
                       "<strong>45 sm²</strong> — ikkiga boʻlingan (bu uchburchak "
                       "formulasi). <strong>42 sm²</strong> — perimetr: "
                       "2 × (15 + 6).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Trapetsiyaning asoslari 8 sm va "
                "4 sm, balandligi 3 sm. Yuzasi qancha?</strong></p>",
        "choices": ["15 sm²", "18 sm²", "24 sm²", "36 sm²"],
        "correct": "18 sm²",
        "explanation": "<p><strong>18 sm².</strong> (8 + 4) ÷ 2 × 3 = 6 × 3 = 18. "
                       "<strong>36 sm²</strong> — ikkiga boʻlinmagan. "
                       "<strong>24 sm²</strong> — faqat katta asos: 8 × 3. "
                       "<strong>15 sm²</strong> — uchta son shunchaki "
                       "qoʻshilgan.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p><strong>Parallelogrammning yuzasi "
                "72 sm², balandligi 8 sm. Asosi qancha?</strong></p>",
        "choices": ["4,5 sm", "9 sm", "64 sm", "576 sm"],
        "correct": "9 sm",
        "explanation": "<p><strong>9 sm.</strong> a × 8 = 72, demak "
                       "a = 72 ÷ 8 = 9. Tekshirish: 9 × 8 = 72 ✓ "
                       "<strong>576 sm</strong> — boʻlish oʻrniga koʻpaytirilgan. "
                       "<strong>64 sm</strong> — ayirilgan. "
                       "<strong>4,5 sm</strong> — yana ikkiga boʻlingan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Trapetsiyaning yuzasi "
                "60 sm², asoslari 8 sm va 4 sm. Balandligi qancha?</strong></p>",
        "choices": ["5 sm", "7,5 sm", "10 sm", "15 sm"],
        "correct": "10 sm",
        "explanation": "<p><strong>10 sm.</strong> (8 + 4) ÷ 2 = 6, demak "
                       "6 × h = 60 va h = 60 ÷ 6 = 10. Tekshirish: "
                       "6 × 10 = 60 ✓ <strong>5 sm</strong> — ikkiga boʻlish "
                       "unutilib, 12 × h = 60 deb yechilgan. "
                       "<strong>7,5 sm</strong> — faqat katta asos "
                       "(60 ÷ 8).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Parallelogrammning asosi 9 sm, "
                "yon tomoni 7 sm, balandligi 5 sm. Yuzasi qancha?</strong></p>",
        "choices": ["32 sm²", "35 sm²", "45 sm²", "63 sm²"],
        "correct": "45 sm²",
        "explanation": "<p><strong>45 sm².</strong> S = asos × balandlik = "
                       "9 × 5 = 45. <strong>63 sm²</strong> — asos yon tomonga "
                       "koʻpaytirilgan (9 × 7); yon tomon qiya turadi va "
                       "balandlikdan uzun, shuning uchun javob katta chiqadi. "
                       "Formulaga faqat perpendikulyar balandlik qoʻyiladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Trapetsiyaning asoslari 14 sm va "
                "6 sm, balandligi 4 sm. Yuzasi qancha?</strong></p>",
        "choices": ["24 sm²", "40 sm²", "56 sm²", "80 sm²"],
        "correct": "40 sm²",
        "explanation": "<p><strong>40 sm².</strong> (14 + 6) ÷ 2 × 4 = "
                       "10 × 4 = 40. <strong>80 sm²</strong> — ikkiga "
                       "boʻlinmagan. <strong>56 sm²</strong> — faqat katta asos "
                       "(14 × 4), <strong>24 sm²</strong> — faqat kichigi "
                       "(6 × 4). Toʻgʻri javob aynan shu ikkisining "
                       "oʻrtasida.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Shakl pastdan 6 m × 4 m toʻgʻri "
                "toʻrtburchak, uning ustida esa asoslari 6 m va 2 m, balandligi "
                "3 m boʻlgan trapetsiya turibdi.</p><p><strong>Butun shaklning "
                "yuzasi qancha?</strong></p>",
        "choices": ["24 m²", "30 m²", "36 m²", "48 m²"],
        "correct": "36 m²",
        "explanation": "<p><strong>36 m².</strong> Pastki qism: 6 × 4 = 24 m². "
                       "Yuqori qism: (6 + 2) ÷ 2 × 3 = 4 × 3 = 12 m². Jami: "
                       "24 + 12 = 36 m². <strong>48 m²</strong> — trapetsiyada "
                       "ikkiga boʻlish unutilgan (24 + 24). "
                       "<strong>24 m²</strong> — yuqori qism umuman "
                       "hisoblanmagan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Rombning diagonallari 16 sm va "
                "9 sm. Yuzasi qancha?</strong></p>",
        "choices": ["25 sm²", "50 sm²", "72 sm²", "144 sm²"],
        "correct": "72 sm²",
        "explanation": "<p><strong>72 sm².</strong> 16 × 9 ÷ 2 = 144 ÷ 2 = 72. "
                       "<strong>144 sm²</strong> — ikkiga boʻlinmagan. "
                       "<strong>25 sm²</strong> — diagonallar qoʻshilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Parallelogrammning asosi "
                "1,2 m, balandligi 80 sm. Yuzasi necha kvadrat metr?</strong></p>",
        "choices": ["0,96 m²", "9,6 m²", "96 m²", "960 m²"],
        "correct": "0,96 m²",
        "explanation": "<p><strong>0,96 m².</strong> Avval birliklarni "
                       "tenglashtiramiz: 80 sm = 0,8 m. Keyin S = 1,2 × 0,8 = "
                       "0,96 m². <strong>96 m²</strong> — birlik almashtirilmay "
                       "1,2 × 80 hisoblangan; javob yuz barobar katta chiqqan. "
                       "Bir xonaning yuzasi 96 m² boʻlishi mumkin emasligini "
                       "taxmin ham koʻrsatib turibdi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p><strong>Parallelogrammning tomonlari "
                "8 sm va 5 sm, balandligi 4 sm. Uning PERIMETRI "
                "qancha?</strong></p>",
        "choices": ["26 sm", "32 sm", "40 sm", "52 sm"],
        "correct": "26 sm",
        "explanation": "<p><strong>26 sm.</strong> Perimetr — chegara uzunligi: "
                       "P = 2 × (8 + 5) = 26 sm (PM-67). Balandlik bu yerda "
                       "umuman kerak emas — u faqat yuza uchun. "
                       "<strong>32 sm</strong> — bu yuza: 8 × 4 = 32 sm². "
                       "Birlikka qarang: perimetr sm da, yuza sm² da.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi formula "
                "trapetsiyaning yuzasini beradi?</strong></p>",
        "choices": [
            "(a + b) ÷ 2 × h",
            "a × h",
            "a × b",
            "d₁ × d₂ ÷ 2",
        ],
        "correct": "(a + b) ÷ 2 × h",
        "explanation": "<p><strong>(a + b) ÷ 2 × h.</strong> Ikkala asosni "
                       "qoʻshamiz, ikkiga boʻlamiz, balandlikka koʻpaytiramiz. "
                       "<strong>a × h</strong> — parallelogrammniki, "
                       "<strong>d₁ × d₂ ÷ 2</strong> — rombniki, "
                       "<strong>a × b</strong> — toʻgʻri toʻrtburchakniki.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Parallelogrammning "
                "yuzasini topish uchun qanday oʻlchovlar kerak?</strong></p>",
        "choices": [
            "Asos va unga perpendikulyar balandlik",
            "Asos va qiya yon tomon",
            "Faqat toʻrtta tomonning uzunligi",
            "Faqat ikkita burchagi",
        ],
        "correct": "Asos va unga perpendikulyar balandlik",
        "explanation": "<p><strong>Asos va unga perpendikulyar balandlik.</strong> "
                       "Yon tomon berilsa ham u formulaga tushmaydi: u qiya "
                       "turadi va balandlikdan uzun. Faqat tomonlarning "
                       "uzunligini bilish yetarli emas — bir xil tomonli "
                       "parallelogrammlar har xil «yassilikda» boʻlib, "
                       "yuzalari har xil boʻladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Birinchi shakl — asosi 10 sm, "
                "balandligi 4 sm boʻlgan parallelogramm. Ikkinchi shakl — "
                "asoslari 10 sm va 6 sm, balandligi 5 sm boʻlgan "
                "trapetsiya.</p><p><strong>Qaysi birining yuzasi "
                "katta?</strong></p>",
        "choices": [
            "Parallelogrammniki katta",
            "Trapetsiyaniki katta",
            "Ikkalasining yuzasi teng",
            "Berilganlar yetarli emas",
        ],
        "correct": "Ikkalasining yuzasi teng",
        "explanation": "<p><strong>Ikkalasining yuzasi teng.</strong> "
                       "Parallelogramm: 10 × 4 = 40 sm². Trapetsiya: "
                       "(10 + 6) ÷ 2 × 5 = 8 × 5 = 40 sm². Shakllar butunlay "
                       "boshqacha koʻrinadi, lekin egallagan joyi bir xil — "
                       "yuza shaklga emas, oʻlchovlarga bogʻliq.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>Parallelogrammning asosi 10 sm, "
                "yon tomoni 8 sm, balandligi 6 sm.<br>Yechim: "
                "<strong>S = 10 × 8 = 80 sm²</strong></p>",
        "choices": [
            "Balandlik oʻrniga yon tomon olingan; toʻgʻrisi 60 sm²",
            "Yuzani yana ikkiga boʻlish kerak edi; toʻgʻrisi 40 sm²",
            "Asos notoʻgʻri tanlangan; toʻgʻrisi 48 sm²",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Balandlik oʻrniga yon tomon olingan; toʻgʻrisi 60 sm²",
        "explanation": "<p><strong>Balandlik oʻrniga yon tomon olingan.</strong> "
                       "Formulada asosga perpendikulyar balandlik turadi: "
                       "S = 10 × 6 = 60 sm². Yon tomon (8 sm) qiya, shuning "
                       "uchun u balandlikdan (6 sm) uzun va javobni "
                       "kattalashtirib yuboradi. Masalada ortiqcha son "
                       "berilishi — odatiy tuzoq.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Trapetsiyaning asoslari 9 m va 5 m, "
                "balandligi 4 m.<br>Yechim: <strong>S = (9 + 5) ÷ 2 × 4 = "
                "14 ÷ 2 × 4 = 7 × 4 = 28 m²</strong></p>",
        "choices": [
            "Xato yoʻq, yechim toʻgʻri",
            "Ikkiga boʻlish ortiqcha; toʻgʻrisi 56 m²",
            "Asoslarni qoʻshish emas, koʻpaytirish kerak edi",
            "Balandlik ishlatilmasligi kerak edi",
        ],
        "correct": "Xato yoʻq, yechim toʻgʻri",
        "explanation": "<p><strong>Xato yoʻq.</strong> Har bir qadam joyida: "
                       "asoslar qoʻshildi (9 + 5 = 14), ikkiga boʻlindi (7), "
                       "balandlikka koʻpaytirildi (7 × 4 = 28 m²). "
                       "Har doim xato qidirmang — yechimni qadam-baqadam "
                       "tekshirish ham javobning bir turi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Sherbekning tomorqasi trapetsiya "
                "shaklida: parallel tomonlari 22 m va 14 m, ular orasidagi "
                "masofa 10 m. Har bir kvadrat metrdan 3 kg sabzavot "
                "olinadi.</p><p><strong>Tomorqadan necha kilogramm sabzavot "
                "olinadi?</strong></p>",
        "choices": ["180 kg", "420 kg", "540 kg", "660 kg"],
        "correct": "540 kg",
        "explanation": "<p><strong>540 kg.</strong> Avval yuza: (22 + 14) ÷ 2 × 10 "
                       "= 18 × 10 = 180 m². Keyin hosil: 180 × 3 = 540 kg. "
                       "<strong>180 kg</strong> — yuza javob deb yozib "
                       "yuborilgan, hosilga oʻtilmagan. <strong>660 kg</strong> — "
                       "yuza 22 × 10 = 220 m² deb olingan (faqat katta asos).</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bekzodning otasi tomni qoplamoqchi. "
                "Tomning har bir yon tomoni trapetsiya: asoslari 12 m va 8 m, "
                "balandligi 5 m. Bunday tomon ikkita. Bir kvadrat metr material "
                "30 000 soʻm turadi.</p><p><strong>Material necha soʻm "
                "boʻladi?</strong></p>",
        "choices": ["1 500 000 soʻm", "1 800 000 soʻm", "3 000 000 soʻm",
                    "6 000 000 soʻm"],
        "correct": "3 000 000 soʻm",
        "explanation": "<p><strong>3 000 000 soʻm.</strong> Bitta tomon: "
                       "(12 + 8) ÷ 2 × 5 = 10 × 5 = 50 m². Ikkitasi: "
                       "50 × 2 = 100 m². Narx: 100 × 30 000 = 3 000 000 soʻm. "
                       "<strong>1 500 000 soʻm</strong> — ikkinchi tomon "
                       "unutilgan. <strong>6 000 000 soʻm</strong> — "
                       "trapetsiyada ikkiga boʻlish tushib qolgan.</p>",
    },
]


# =====================================================================
# PM-70 — doira va aylana; π
# =====================================================================

Q_PM70 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>Doiraning radiusi 6 sm. Diametri "
                "qancha?</strong></p>",
        "choices": ["3 sm", "6 sm", "12 sm", "36 sm"],
        "correct": "12 sm",
        "explanation": "<p><strong>12 sm.</strong> d = 2 × r = 2 × 6 = 12. "
                       "<strong>3 sm</strong> — koʻpaytirish oʻrniga boʻlingan; "
                       "diametr radiusdan katta boʻlishi kerak. "
                       "<strong>36 sm</strong> — kvadratga koʻtarilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Doiraning diametri 18 m. Radiusi "
                "qancha?</strong></p>",
        "choices": ["4,5 m", "9 m", "18 m", "36 m"],
        "correct": "9 m",
        "explanation": "<p><strong>9 m.</strong> r = d ÷ 2 = 18 ÷ 2 = 9. "
                       "<strong>36 m</strong> — boʻlish oʻrniga koʻpaytirilgan; "
                       "radius diametrdan kichik boʻlishi kerak. "
                       "<strong>4,5 m</strong> — ikki marta boʻlingan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Aylana "
                "nima?</strong></p>",
        "choices": [
            "Markazdan bir xil uzoqlikdagi nuqtalardan tuzilgan chiziq",
            "Chiziq va uning ichidagi hamma joy",
            "Markazdan oʻtuvchi eng uzun kesma",
            "Aylananing ikki nuqtasini tutashtiruvchi kesma",
        ],
        "correct": "Markazdan bir xil uzoqlikdagi nuqtalardan tuzilgan chiziq",
        "explanation": "<p><strong>Markazdan bir xil uzoqlikdagi nuqtalardan "
                       "tuzilgan chiziq.</strong> «Chiziq va uning ichi» — bu "
                       "doira. «Markazdan oʻtuvchi eng uzun kesma» — diametr. "
                       "«Ikki nuqtani tutashtiruvchi kesma» — vatar.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>π taxminan nechaga "
                "teng?</strong></p>",
        "choices": ["2,14", "3,14", "3,41", "4,13"],
        "correct": "3,14",
        "explanation": "<p><strong>3,14.</strong> π = 3,14159265… — uning oʻnlik "
                       "yozuvi cheksiz, shuning uchun hisobda 3,14 gacha "
                       "yaxlitlanadi. Uni eslab qolishning oson yoʻli: har "
                       "qanday dumaloq narsaning atrofi enidan uch marta "
                       "va biroz koʻproq uzun.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Aylananing ikki "
                "nuqtasini tutashtiruvchi kesma qanday ataladi?</strong></p>",
        "choices": ["Vatar", "Radius", "Yoy", "Markaz"],
        "correct": "Vatar",
        "explanation": "<p><strong>Vatar.</strong> Radius markazdan aylanagacha "
                       "boradi, yoy — aylananing bir boʻlagi (chiziq, kesma "
                       "emas), markaz esa nuqta. Diametr ham vatar — eng uzuni, "
                       "chunki u markazdan oʻtadi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>Aylananing uzunligi 157 sm, diametri "
                "50 sm.</p><p><strong>L ni d ga boʻlsangiz nima "
                "chiqadi?</strong></p>",
        "choices": ["0,32", "3,14", "3,41", "6,28"],
        "correct": "3,14",
        "explanation": "<p><strong>3,14 — yaʼni π.</strong> 157 ÷ 50 = 3,14. "
                       "Qanday aylana olsangiz ham natija oʻsha boʻladi — "
                       "aynan shuning uchun bu son alohida nom olgan. "
                       "<strong>0,32</strong> — boʻlish teskari qilingan "
                       "(50 ÷ 157). <strong>6,28</strong> — diametr oʻrniga "
                       "radiusga boʻlingan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Aylananing uzunligi 314 sm. "
                "Uning diametri qancha? (π ≈ 3,14)</strong></p>",
        "choices": ["50 sm", "100 sm", "157 sm", "986 sm"],
        "correct": "100 sm",
        "explanation": "<p><strong>100 sm.</strong> π = L ÷ d munosabatidan "
                       "d = L ÷ π = 314 ÷ 3,14 = 100. Tekshirish: "
                       "100 × 3,14 = 314 ✓ <strong>986 sm</strong> — boʻlish "
                       "oʻrniga koʻpaytirilgan; diametr aylananing uzunligidan "
                       "katta boʻlishi mumkin emas. <strong>50 sm</strong> — bu "
                       "radius.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Aylananing uzunligi "
                "62,8 sm. Uning radiusi qancha?</strong></p>",
        "choices": ["10 sm", "20 sm", "31,4 sm", "40 sm"],
        "correct": "10 sm",
        "explanation": "<p><strong>10 sm.</strong> Ikki qadam kerak: avval "
                       "diametr — 62,8 ÷ 3,14 = 20 sm, keyin radius — "
                       "20 ÷ 2 = 10 sm. <strong>20 sm</strong> — ikkinchi qadam "
                       "tushib qolgan, bu diametr. <strong>31,4 sm</strong> — "
                       "shunchaki ikkiga boʻlingan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Diametri 7 sm boʻlgan aylananing "
                "uzunligi qancha? (π ≈ 3,14)</strong></p>",
        "choices": ["10,99 sm", "21,98 sm", "43,96 sm", "49 sm"],
        "correct": "21,98 sm",
        "explanation": "<p><strong>21,98 sm.</strong> π = L ÷ d, demak "
                       "L = π × d = 3,14 × 7 = 21,98. <strong>10,99 sm</strong> — "
                       "diametr oʻrniga radius (3,5 sm) ishlatilgan. "
                       "<strong>49 sm</strong> — π umuman ishlatilmagan, "
                       "7 kvadratga koʻtarilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Gʻildirakning radiusi "
                "25 sm. Uning diametri necha metr?</strong></p>",
        "choices": ["0,25 m", "0,5 m", "5 m", "50 m"],
        "correct": "0,5 m",
        "explanation": "<p><strong>0,5 m.</strong> d = 2 × 25 = 50 sm, va "
                       "50 sm = 0,5 m (100 sm = 1 m). <strong>50 m</strong> — "
                       "birlik almashtirilmagan; 50 metrlik gʻildirak "
                       "boʻlmaydi. <strong>0,25 m</strong> — radiusning oʻzi "
                       "metrga oʻgirilgan, diametrga oʻtilmagan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Radiusi 12 sm boʻlgan "
                "doirada eng uzun vatar necha santimetr?</strong></p>",
        "choices": ["6 sm", "12 sm", "24 sm", "144 sm"],
        "correct": "24 sm",
        "explanation": "<p><strong>24 sm.</strong> Eng uzun vatar — markazdan "
                       "oʻtadigani, yaʼni diametr: d = 2 × 12 = 24 sm. Markazdan "
                       "oʻtmagan har qanday vatar undan qisqaroq boʻladi. "
                       "<strong>12 sm</strong> — radiusning oʻzi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>π haqida qaysi "
                "jumla toʻgʻri?</strong></p>",
        "choices": [
            "π ≈ 3,14; aniq qiymati cheksiz va takrorlanmaydi",
            "π aynan 3,14 ga teng",
            "π har bir aylanada boshqacha chiqadi",
            "π faqat katta doiralarda 3,14 ga yaqin boʻladi",
        ],
        "correct": "π ≈ 3,14; aniq qiymati cheksiz va takrorlanmaydi",
        "explanation": "<p><strong>π ≈ 3,14; aniq qiymati cheksiz va "
                       "takrorlanmaydi.</strong> 3,14 — bu faqat yaxlitlangan "
                       "qiymat (PM-14). Va u doiraning kattaligiga bogʻliq "
                       "emas: stakanda ham, gʻildirakda ham L ÷ d bir xil "
                       "son beradi — π ni buyuk qiladigan narsa aynan shu.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Doiraviy hovlining atrofiga "
                "panjara qoʻyiladi.</p><p><strong>Panjaraning uzunligi qaysi "
                "kattalikka teng?</strong></p>",
        "choices": [
            "Aylananing uzunligiga",
            "Doiraning ichidagi joyga",
            "Vatarning uzunligiga",
            "Radiusning uzunligiga",
        ],
        "correct": "Aylananing uzunligiga",
        "explanation": "<p><strong>Aylananing uzunligiga.</strong> Panjara "
                       "chegara boʻylab ketadi, chegara esa — aylana, yaʼni "
                       "chiziq. Doiraning ichi — bu hovlining oʻzi, u metrlab "
                       "emas, kvadrat metrlab oʻlchanadi. Panjara — perimetrning "
                       "dumaloq shakldagi koʻrinishi (PM-67).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Diametri 10 sm "
                "boʻlgan doira bilan radiusi 10 sm boʻlgan doiradan qaysi biri "
                "katta?</strong></p>",
        "choices": [
            "Diametri 10 sm boʻlgani",
            "Radiusi 10 sm boʻlgani",
            "Ikkalasi teng",
            "Berilganlar yetarli emas",
        ],
        "correct": "Radiusi 10 sm boʻlgani",
        "explanation": "<p><strong>Radiusi 10 sm boʻlgani.</strong> Uning "
                       "diametri 2 × 10 = 20 sm, yaʼni birinchisidan ikki "
                       "barobar keng. Bir xil son berilgan boʻlsa ham, u qaysi "
                       "kattalik ekaniga qarash shart — bu doiradagi eng koʻp "
                       "uchraydigan chalkashlik.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Aylana va doira "
                "haqida qaysi jumla toʻgʻri?</strong></p>",
        "choices": [
            "Aylana — chiziq, doira — chiziq va uning ichi",
            "Doira — chiziq, aylana — uning ichi",
            "Aylana va doira — bir xil narsaning ikki nomi",
            "Doira — aylananing yarmi",
        ],
        "correct": "Aylana — chiziq, doira — chiziq va uning ichi",
        "explanation": "<p><strong>Aylana — chiziq, doira — chiziq va uning "
                       "ichi.</strong> Farqi xuddi panjara bilan hovlining "
                       "farqi kabi: panjara — aylana, hovlining oʻzi — doira. "
                       "Shuning uchun «aylananing uzunligi» va «doiraning "
                       "yuzasi» deyiladi, teskarisi emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Har qanday diametr "
                "— vatar». Bu jumla toʻgʻrimi?</strong></p>",
        "choices": [
            "Toʻgʻri — diametr eng uzun vatar",
            "Notoʻgʻri — vatar markazdan oʻtmasligi shart",
            "Notoʻgʻri — diametr kesma emas",
            "Faqat kichik doiralarda toʻgʻri",
        ],
        "correct": "Toʻgʻri — diametr eng uzun vatar",
        "explanation": "<p><strong>Toʻgʻri.</strong> Vatar — aylananing ikki "
                       "nuqtasini tutashtiruvchi kesma; diametr ham aynan "
                       "shunday kesma, faqat u markazdan oʻtadi va shu bois "
                       "hammasidan uzun. Teskarisi esa notoʻgʻri: har qanday "
                       "vatar diametr emas.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>Doiraning diametri 14 sm. "
                "Sherbekning yechimi: <strong>r = 2 × 14 = 28 sm</strong></p>",
        "choices": [
            "Koʻpaytirilgan; toʻgʻrisi r = 14 ÷ 2 = 7 sm",
            "π ga koʻpaytirish kerak edi",
            "Radius diametrga teng boʻlishi kerak edi",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Koʻpaytirilgan; toʻgʻrisi r = 14 ÷ 2 = 7 sm",
        "explanation": "<p><strong>Koʻpaytirilgan.</strong> d = 2r formulasi "
                       "diametr uchun, radius uchun emas: r = d ÷ 2 = 7 sm. "
                       "Javobni tekshirishning oson yoʻli — radius har doim "
                       "diametrdan <em>kichik</em>. 28 sm 14 sm dan katta, "
                       "demak yechim boshidanoq notoʻgʻri.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Aylananing uzunligi 94,2 sm, "
                "diametri 30 sm. Afsona π ni topmoqchi:<br><strong>π = "
                "30 ÷ 94,2 = 0,32</strong></p>",
        "choices": [
            "Boʻlish teskari qilingan; π = 94,2 ÷ 30 = 3,14",
            "Radius oʻrniga diametr ishlatilgan",
            "Natijani ikkiga boʻlish kerak edi",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Boʻlish teskari qilingan; π = 94,2 ÷ 30 = 3,14",
        "explanation": "<p><strong>Boʻlish teskari qilingan.</strong> "
                       "π = L ÷ d, yaʼni uzunlik diametrga boʻlinadi: "
                       "94,2 ÷ 30 = 3,14 ✓ π har doim 1 dan katta, chunki "
                       "aylana oʻz diametridan uzun. 0,32 kabi javob "
                       "chiqsa — boʻlish teskari boʻlgan.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Dilnoza bogʻdagi dumaloq hovuzning "
                "chetidan ip oʻrab chiqdi. Ipni yozib oʻlchaganda 47,1 metr "
                "chiqdi.</p><p><strong>Hovuzning diametri qancha?</strong></p>",
        "choices": ["7,5 m", "15 m", "23,55 m", "147,9 m"],
        "correct": "15 m",
        "explanation": "<p><strong>15 m.</strong> Ip — aylananing uzunligi, "
                       "demak d = L ÷ π = 47,1 ÷ 3,14 = 15 m. Tekshirish: "
                       "15 × 3,14 = 47,1 ✓ <strong>7,5 m</strong> — bu radius. "
                       "<strong>147,9 m</strong> — boʻlish oʻrniga "
                       "koʻpaytirilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Karim aka dumaloq stolga dasturxon "
                "tikmoqchi. Stolning atrofini oʻlchadi: 251,2 sm. Dasturxon "
                "stolning chetidan har tomonga 15 sm osilib turishi "
                "kerak.</p><p><strong>Dasturxonning diametri qancha boʻlishi "
                "kerak?</strong></p>",
        "choices": ["55 sm", "95 sm", "110 sm", "281,2 sm"],
        "correct": "110 sm",
        "explanation": "<p><strong>110 sm.</strong> Avval stolning diametri: "
                       "251,2 ÷ 3,14 = 80 sm. Dasturxon <em>ikkala</em> "
                       "tomondan osiladi, demak: 80 + 15 + 15 = 110 sm. "
                       "<strong>95 sm</strong> — 15 sm faqat bir marta "
                       "qoʻshilgan. <strong>281,2 sm</strong> — 30 sm "
                       "diametrga emas, aylananing uzunligiga qoʻshilgan.</p>",
    },
]


# =====================================================================
# PM-71 — aylana uzunligi va doira yuzasi
# =====================================================================

Q_PM71 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang. (π ≈ 3,14)</p><p><strong>Radiusi 2 sm boʻlgan "
                "aylananing uzunligi qancha?</strong></p>",
        "choices": ["4 sm", "6,28 sm", "12,56 sm", "25,12 sm"],
        "correct": "12,56 sm",
        "explanation": "<p><strong>12,56 sm.</strong> L = 2 × π × r = "
                       "2 × 3,14 × 2 = 12,56. <strong>6,28 sm</strong> — 2 ga "
                       "koʻpaytirish tushib qolgan (π × r). <strong>4 sm</strong> "
                       "— π umuman ishlatilmagan, faqat 2r olingan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Diametri 6 m boʻlgan aylananing "
                "uzunligi qancha?</strong></p>",
        "choices": ["9,42 m", "18,84 m", "37,68 m", "113,04 m"],
        "correct": "18,84 m",
        "explanation": "<p><strong>18,84 m.</strong> Diametr berilganda "
                       "L = π × d = 3,14 × 6 = 18,84 — radiusga oʻtish shart "
                       "emas. <strong>37,68 m</strong> — diametr yana 2 ga "
                       "koʻpaytirilgan (2πd). <strong>113,04 m</strong> — bu "
                       "yuza formulasi bilan hisoblangan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Radiusi 3 sm boʻlgan doiraning "
                "yuzasi qancha?</strong></p>",
        "choices": ["9,42 sm²", "18,84 sm²", "28,26 sm²", "113,04 sm²"],
        "correct": "28,26 sm²",
        "explanation": "<p><strong>28,26 sm².</strong> S = π × r² = 3,14 × 9 = "
                       "28,26. <strong>18,84 sm²</strong> — bu aylananing "
                       "uzunligi (2πr), yuza emas; birlikka qarang. "
                       "<strong>113,04 sm²</strong> — radius oʻrniga diametr "
                       "(6 sm) qoʻyilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Radiusi 10 sm boʻlgan doiraning "
                "yuzasi qancha?</strong></p>",
        "choices": ["31,4 sm²", "62,8 sm²", "314 sm²", "1256 sm²"],
        "correct": "314 sm²",
        "explanation": "<p><strong>314 sm².</strong> S = 3,14 × 10² = "
                       "3,14 × 100 = 314. <strong>62,8 sm²</strong> — bu "
                       "aylananing uzunligi. <strong>1256 sm²</strong> — "
                       "radius oʻrniga diametr (20 sm) kvadratga "
                       "koʻtarilgan; javob aynan 4 barobar katta chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Doiraning yuzasi "
                "qaysi formula bilan topiladi?</strong></p>",
        "choices": ["π × r × r", "2 × π × r", "π × d × d", "π × r ÷ 2"],
        "correct": "π × r × r",
        "explanation": "<p><strong>π × r × r</strong>, yaʼni π × r². "
                       "<strong>2 × π × r</strong> — bu aylananing uzunligi. "
                       "<strong>π × d × d</strong> — diametr qoʻyilgan, javob "
                       "toʻrt barobar katta chiqadi. Yodda tuting: yuzada "
                       "har doim <em>radius</em> ishlaydi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p><strong>Diametri 20 sm boʻlgan "
                "doiraning yuzasi qancha?</strong></p>",
        "choices": ["62,8 sm²", "78,5 sm²", "314 sm²", "1256 sm²"],
        "correct": "314 sm²",
        "explanation": "<p><strong>314 sm².</strong> Avval radius: "
                       "r = 20 ÷ 2 = 10 sm. Keyin S = 3,14 × 100 = 314 sm². "
                       "<strong>1256 sm²</strong> — diametr toʻgʻridan-toʻgʻri "
                       "formulaga qoʻyilgan. <strong>62,8 sm²</strong> — bu "
                       "aylananing uzunligi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Radiusi 7 m boʻlgan doiraning "
                "yuzasi qancha?</strong></p>",
        "choices": ["43,96 m²", "153,86 m²", "307,72 m²", "615,44 m²"],
        "correct": "153,86 m²",
        "explanation": "<p><strong>153,86 m².</strong> S = 3,14 × 7² = "
                       "3,14 × 49 = 153,86 (3 × 49 = 147 va 0,14 × 49 = 6,86). "
                       "<strong>43,96 m²</strong> — bu aylananing uzunligi. "
                       "<strong>615,44 m²</strong> — diametr (14 m) kvadratga "
                       "koʻtarilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Aylananing uzunligi "
                "25,12 m. Uning radiusi qancha?</strong></p>",
        "choices": ["4 m", "8 m", "12,56 m", "78,88 m"],
        "correct": "4 m",
        "explanation": "<p><strong>4 m.</strong> Avval diametr: "
                       "25,12 ÷ 3,14 = 8 m, keyin radius: 8 ÷ 2 = 4 m. "
                       "Tekshirish: 2 × 3,14 × 4 = 25,12 ✓ "
                       "<strong>8 m</strong> — ikkinchi qadam tushib qolgan. "
                       "<strong>78,88 m</strong> — boʻlish oʻrniga "
                       "koʻpaytirilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Aylananing uzunligi "
                "18,84 sm. Shu doiraning yuzasi qancha?</strong></p>",
        "choices": ["9,42 sm²", "28,26 sm²", "56,52 sm²", "113,04 sm²"],
        "correct": "28,26 sm²",
        "explanation": "<p><strong>28,26 sm².</strong> Uch qadam: "
                       "d = 18,84 ÷ 3,14 = 6 sm → r = 3 sm → "
                       "S = 3,14 × 9 = 28,26 sm². <strong>113,04 sm²</strong> — "
                       "radiusga oʻtilmay, 6 kvadratga koʻtarilgan. "
                       "Uzunlikdan yuzaga oʻtishda har doim radiusdan "
                       "oʻting.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Halqaning tashqi radiusi 6 m, "
                "ichki radiusi 4 m.</p><p><strong>Halqaning yuzasi "
                "qancha?</strong></p>",
        "choices": ["12,56 m²", "50,24 m²", "62,8 m²", "113,04 m²"],
        "correct": "62,8 m²",
        "explanation": "<p><strong>62,8 m².</strong> Katta doira: "
                       "3,14 × 36 = 113,04 m². Kichik doira: 3,14 × 16 = "
                       "50,24 m². Ayiramiz: 113,04 − 50,24 = 62,8 m². "
                       "<strong>12,56 m²</strong> — radiuslar ayirilib "
                       "(6 − 4 = 2), keyin yuza hisoblangan; ayirish "
                       "<em>yuzalar</em> ustida bajariladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Diametri 10 sm boʻlgan "
                "yarim doiraning yuzasi qancha?</strong></p>",
        "choices": ["15,7 sm²", "39,25 sm²", "78,5 sm²", "157 sm²"],
        "correct": "39,25 sm²",
        "explanation": "<p><strong>39,25 sm².</strong> Butun doira: r = 5 sm, "
                       "S = 3,14 × 25 = 78,5 sm². Yarmi: 78,5 ÷ 2 = 39,25 sm². "
                       "<strong>78,5 sm²</strong> — ikkiga boʻlish unutilgan. "
                       "<strong>15,7 sm²</strong> — yarim aylananing "
                       "uzunligi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Radiusi 50 sm boʻlgan "
                "doiraning yuzasi necha kvadrat metr?</strong></p>",
        "choices": ["0,785 m²", "7,85 m²", "78,5 m²", "7850 m²"],
        "correct": "0,785 m²",
        "explanation": "<p><strong>0,785 m².</strong> Avval birlik: "
                       "50 sm = 0,5 m. Keyin S = 3,14 × 0,5² = 3,14 × 0,25 = "
                       "0,785 m². <strong>7850 m²</strong> — santimetrda "
                       "hisoblanib (3,14 × 2500 = 7850 sm²), birligi metrga "
                       "almashtirib yuborilgan. 1 m² = 10 000 sm², shuning "
                       "uchun 7850 sm² = 0,785 m².</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Doiraviy hovuzning radiusi 5 m. "
                "Uning atrofiga panjara qoʻyiladi.</p><p><strong>Panjara necha "
                "metr kerak?</strong></p>",
        "choices": ["15,7 m", "31,4 m", "78,5 m", "157 m"],
        "correct": "31,4 m",
        "explanation": "<p><strong>31,4 m.</strong> Panjara chegara boʻylab "
                       "ketadi, demak aylana uzunligi: L = 2 × 3,14 × 5 = "
                       "31,4 m. <strong>78,5 m</strong> — bu hovuzning yuzasi "
                       "(78,5 m²), panjaraga aloqasi yoʻq. Birlikka qarang: "
                       "panjara metrda, yuza kvadrat metrda.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Oʻsha hovuzning radiusi yana "
                "5 m.</p><p><strong>Hovuzdagi suvning yuzasi "
                "qancha?</strong></p>",
        "choices": ["15,7 m²", "31,4 m²", "78,5 m²", "157 m²"],
        "correct": "78,5 m²",
        "explanation": "<p><strong>78,5 m².</strong> Suv doiraning ichini "
                       "egallaydi, demak S = 3,14 × 25 = 78,5 m². "
                       "<strong>31,4 m²</strong> — bu panjaraning uzunligi "
                       "(oldingi savol), yuza emas. Bitta doira, ikkita "
                       "butunlay boshqa savol: chegara uchun L, ichi uchun S.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Doiraning radiusi "
                "3 marta oshsa, yuzasi necha marta oshadi?</strong></p>",
        "choices": ["3 marta", "6 marta", "9 marta", "27 marta"],
        "correct": "9 marta",
        "explanation": "<p><strong>9 marta.</strong> Formulada radius kvadratga "
                       "koʻtariladi, demak 3 marta oshgan radius 3² = 9 marta "
                       "koʻp yuza beradi. Tekshiring: r = 2 → 3,14 × 4 = "
                       "12,56; r = 6 → 3,14 × 36 = 113,04; va 113,04 ÷ 12,56 = "
                       "9 ✓ <strong>3 marta</strong> — aylananing uzunligi "
                       "shunday oshadi, yuza esa yoʻq.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Birinchi shakl — diametri 10 sm "
                "boʻlgan doira. Ikkinchi shakl — tomoni 9 sm boʻlgan "
                "kvadrat.</p><p><strong>Qaysi birining yuzasi "
                "katta?</strong></p>",
        "choices": [
            "Doiraning yuzasi katta",
            "Kvadratning yuzasi katta",
            "Ikkalasi teng",
            "Berilganlar yetarli emas",
        ],
        "correct": "Kvadratning yuzasi katta",
        "explanation": "<p><strong>Kvadratning yuzasi katta.</strong> Doira: "
                       "r = 5 sm, S = 3,14 × 25 = 78,5 sm². Kvadrat: "
                       "9² = 81 sm². 81 &gt; 78,5, farqi atigi 2,5 sm². "
                       "Koʻz bilan qaraganda doira kattaroqdek koʻrinadi — "
                       "shuning uchun taxmin emas, hisob kerak.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>Doiraning diametri 8 sm.<br>Yechim: "
                "<strong>S = 3,14 × 8² = 3,14 × 64 = 200,96 sm²</strong></p>",
        "choices": [
            "Radius oʻrniga diametr qoʻyilgan; toʻgʻrisi 50,24 sm²",
            "π ni ham kvadratga koʻtarish kerak edi",
            "Natijani ikkiga boʻlish kerak edi; toʻgʻrisi 100,48 sm²",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Radius oʻrniga diametr qoʻyilgan; toʻgʻrisi 50,24 sm²",
        "explanation": "<p><strong>Radius oʻrniga diametr qoʻyilgan.</strong> "
                       "Avval r = 8 ÷ 2 = 4 sm, keyin S = 3,14 × 16 = "
                       "50,24 sm². Diametrni qoʻyish javobni har doim aynan "
                       "4 barobar kattalashtiradi, chunki (2r)² = 4r².</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Radiusi 5 m boʻlgan gulzorning "
                "atrofiga panjara kerak.<br>Yechim: <strong>L = 3,14 × 5 = "
                "15,7 m</strong></p>",
        "choices": [
            "2 ga koʻpaytirish tushib qolgan; toʻgʻrisi 31,4 m",
            "Yuza formulasi ishlatilishi kerak edi; toʻgʻrisi 78,5 m",
            "Radiusni kvadratga koʻtarish kerak edi",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "2 ga koʻpaytirish tushib qolgan; toʻgʻrisi 31,4 m",
        "explanation": "<p><strong>2 ga koʻpaytirish tushib qolgan.</strong> "
                       "π × d formulasiga diametr, 2 × π × r formulasiga esa "
                       "radius qoʻyiladi. Bu yerda radius berilgan, demak "
                       "L = 2 × 3,14 × 5 = 31,4 m. Yozilgan 15,7 m — bu "
                       "aylananing roppa-rosa yarmi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Sherbekning velosipedi gʻildiragining "
                "diametri 50 sm.</p><p><strong>Gʻildirak bir marta toʻliq "
                "aylanganda velosiped necha metr yuradi?</strong></p>",
        "choices": ["0,785 m", "1,57 m", "3,14 m", "157 m"],
        "correct": "1,57 m",
        "explanation": "<p><strong>1,57 m.</strong> Bir aylanishda gʻildirak "
                       "oʻz aylanasining uzunligicha yoʻl bosadi: 50 sm = 0,5 m, "
                       "L = 3,14 × 0,5 = 1,57 m. <strong>157 m</strong> — "
                       "santimetrda hisoblanib (157 sm), birligi metr deb "
                       "yozilgan. <strong>0,785 m</strong> — radius "
                       "ishlatilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Jasurning hovlisidagi doiraviy "
                "gulzorning radiusi 5 m. Gulzorga goʻng solinadi: har kvadrat "
                "metriga 4 kg.</p><p><strong>Necha kilogramm goʻng "
                "kerak?</strong></p>",
        "choices": ["125,6 kg", "157 kg", "314 kg", "1256 kg"],
        "correct": "314 kg",
        "explanation": "<p><strong>314 kg.</strong> Avval yuza: S = 3,14 × 25 = "
                       "78,5 m². Keyin goʻng: 78,5 × 4 = 314 kg. "
                       "<strong>125,6 kg</strong> — yuza oʻrniga aylananing "
                       "uzunligi olingan (31,4 × 4). <strong>1256 kg</strong> — "
                       "radius oʻrniga diametr (10 m) qoʻyilgan: "
                       "3,14 × 100 = 314 m², bu esa haqiqiy yuzadan 4 barobar "
                       "katta.</p>",
    },
]


PRACTICES = [
    {
        "title":       ("PM-69 Mashq: Yuza 2: parallelogramm, trapetsiya va "
                        "murakkab shakllar"),
        "tutorial":    "PM-69:",
        "description": (
            "Parallelogramm, romb va trapetsiya yuzasi, murakkab shaklni "
            "boʻlaklarga ajratish, teskari masalalar. 20 savol."
        ),
        "questions":   Q_PM69,
        **DEFAULTS,
    },
    {
        "title":       "PM-70 Mashq: Doira va aylana; π",
        "tutorial":    "PM-70:",
        "description": (
            "Aylana va doiraning farqi, markaz, radius, diametr, vatar va yoy, "
            "d = 2r hamda π = L ÷ d munosabati. 20 savol."
        ),
        "questions":   Q_PM70,
        **DEFAULTS,
    },
    {
        "title":       "PM-71 Mashq: Aylana uzunligi va doira yuzasi",
        "tutorial":    "PM-71:",
        "description": (
            "L = 2πr va S = πr², teskari masalalar, halqa, yarim doira va "
            "ikkala formulani farqlash. 20 savol."
        ),
        "questions":   Q_PM71,
        **DEFAULTS,
        "level":       "hard",
    },
]
