# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-75, PM-76, PM-77 (maʼlumot, diagramma turlari,
diagrammani oʻqish). Blok F ning boshi.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: uchalasi ham `hard`.

⚠️ Mashqda SVG yoʻq — diagramma maʼlumoti oddiy <table> bilan beriladi
   (STYLE_GUIDE_PM_PRACTICE 4-boʻlim: jadval faqat savol haqiqatan jadval
   boʻlganda). Uchala testda ham bitta maʼlumot ishlatiladi, shuning uchun
   oʻquvchi darsdagi diagrammani eslab qoladi.
⚠️ `choices` EKRANLANADI — HTML teg yoʻq.
⚠️ Kumulyativ:
   • PM-75 — faqat jadval va foiz; ⛔ DIAGRAMMA soʻzi ham yoʻq;
   • PM-76 — uchta tur va sektor burchagi; ⛔ chuqur oʻqish PM-77 da;
   • PM-77 — oʻqish, farq, jami, sakrash, foiz oʻzgarishi (PM-25).
     ⛔ Oʻrta arifmetik (PM-78), mediana (PM-79), tarqoqlik (PM-80) va
     aldamchi diagramma (PM-81) YOʻQ — «oʻrtacha» atama sifatida
     ishlatilmaydi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_75_77.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Matematika",
    "description": "Matematika — Prime Math darslarining mashqlari",
    "icon":        "bi-calculator",
    "color":       "#f59e0b",
}

DEFAULTS = {
    "level":                "hard",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}

# Uchala testda ham koʻrinadigan maʼlumot (darsdagi diagramma bilan bir xil)
KITOB_JADVAL = (
    "<table><tr><th>Oy</th><th>Sen</th><th>Okt</th><th>Noy</th>"
    "<th>Dek</th><th>Yan</th></tr>"
    "<tr><td>Kitob</td><td>40</td><td>55</td><td>35</td><td>60</td>"
    "<td>45</td></tr></table>"
)
NIHOL_JADVAL = (
    "<table><tr><th>Hafta</th><th>1</th><th>2</th><th>3</th><th>4</th>"
    "<th>5</th><th>6</th></tr>"
    "<tr><td>Boʻyi, sm</td><td>2</td><td>5</td><td>9</td><td>14</td>"
    "<td>16</td><td>17</td></tr></table>"
)


# =====================================================================
# PM-75 — maʼlumot yigʻish va jadval
# =====================================================================

Q_PM75 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>Chiziqchalarda uchta toʻliq guruh va yana "
                "ikkita chiziqcha bor.</p><p><strong>Bu nechta?</strong></p>",
        "choices": ["8", "15", "17", "32"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> Har bir toʻliq guruh — 5 ta: "
                       "5 + 5 + 5 = 15, va yana 2 ta: 15 + 2 = 17. "
                       "<strong>8</strong> — guruhlar soni bilan qoldiq "
                       "qoʻshilgan (3 + 5). <strong>15</strong> — oxirgi "
                       "ikkitasi unutilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>20 oʻquvchidan 5 tasi anorni "
                "tanladi. Bu necha foiz?</strong></p>",
        "choices": ["5%", "20%", "25%", "40%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> 5 ÷ 20 = 0,25, va "
                       "0,25 × 100 = 25%. <strong>5%</strong> — chastotaning "
                       "oʻzi foiz deb yozib yuborilgan; foiz har doim "
                       "<em>jamiga</em> nisbatan olinadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Chastota "
                "nima?</strong></p>",
        "choices": [
            "Bir javob necha marta uchragani",
            "Soʻralganlarning umumiy soni",
            "Eng koʻp uchragan javob",
            "Javoblarning foizi",
        ],
        "correct": "Bir javob necha marta uchragani",
        "explanation": "<p><strong>Bir javob necha marta uchragani.</strong> "
                       "Masalan «olma — 8» degani olmani 8 kishi tanlagan. "
                       "Soʻralganlarning umumiy soni — bu <em>jami</em>, "
                       "foiz esa chastotani jamiga boʻlib topiladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Chastota jadvalida uchta qator bor: "
                "7, 5 va 8.</p><p><strong>Jami nechta javob "
                "yigʻilgan?</strong></p>",
        "choices": ["15", "18", "20", "22"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> 7 + 5 + 8 = 20. Bu son "
                       "soʻralganlar soniga teng boʻlishi shart — bu "
                       "jadvalning birinchi tekshiruvi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Jadvalda toʻrtta ulush bor. Uchtasining "
                "foizi 50%, 20% va 20%.</p><p><strong>Toʻrtinchisi necha "
                "foiz?</strong></p>",
        "choices": ["5%", "10%", "20%", "30%"],
        "correct": "10%",
        "explanation": "<p><strong>10%.</strong> Foizlar yigʻindisi har doim "
                       "100 boʻladi: 100 − (50 + 20 + 20) = 100 − 90 = 10%. "
                       "Agar 100 chiqmasa, ulushlardan biri notoʻgʻri "
                       "hisoblangan.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>40 kishidan 16 tasi «ha» dedi. "
                "Bu necha foiz?</strong></p>",
        "choices": ["16%", "24%", "40%", "60%"],
        "correct": "40%",
        "explanation": "<p><strong>40%.</strong> 16 ÷ 40 = 0,4 → 40%. "
                       "<strong>24%</strong> — «yoʻq» deganlarning foizi "
                       "(40 − 16 = 24 kishi, yaʼni 60%) bilan chalkashtirilgan; "
                       "<strong>16%</strong> — chastotaning oʻzi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>50 oʻquvchining 30 foizi "
                "velosipedda keladi. Bu nechta oʻquvchi?</strong></p>",
        "choices": ["15", "20", "30", "35"],
        "correct": "15",
        "explanation": "<p><strong>15 ta.</strong> 50 ÷ 100 × 30 = 15 "
                       "(PM-24). <strong>30</strong> — foizning oʻzi javob "
                       "deb yozib yuborilgan; foiz odam soni emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Chastotalar: 12, 9, 6 va 3.</p>"
                "<p><strong>9 chastotasi necha foiz?</strong></p>",
        "choices": ["9%", "20%", "30%", "33%"],
        "correct": "30%",
        "explanation": "<p><strong>30%.</strong> Avval jami: "
                       "12 + 9 + 6 + 3 = 30. Keyin 9 ÷ 30 = 0,3 → 30%. "
                       "Bu yerda jami ham 30 ekani tasodif — chastotani "
                       "jamiga boʻlish qadamini baribir bajaring.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>25 oʻquvchidan soʻraldi: olma 10, non 8, "
                "choy 7.</p><p><strong>Choy tanlaganlar necha "
                "foiz?</strong></p>",
        "choices": ["7%", "25%", "28%", "32%"],
        "correct": "28%",
        "explanation": "<p><strong>28%.</strong> Tekshiramiz: "
                       "10 + 8 + 7 = 25 ✓ Keyin 7 ÷ 25 = 0,28 → 28%. "
                       "<strong>32%</strong> — nonning foizi (8 ÷ 25).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Birinchi qatorda ikkita toʻliq guruh va "
                "uchta chiziqcha, ikkinchi qatorda bitta toʻliq guruh va "
                "toʻrtta chiziqcha.</p><p><strong>Ikkalasida jami "
                "nechta?</strong></p>",
        "choices": ["13", "18", "22", "24"],
        "correct": "22",
        "explanation": "<p><strong>22.</strong> Birinchi qator: "
                       "5 + 5 + 3 = 13. Ikkinchi qator: 5 + 4 = 9. Jami: "
                       "13 + 9 = 22. <strong>13</strong> — faqat birinchi "
                       "qator.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>60 oʻquvchining 45 foizi "
                "avtobusda keladi. Bu nechta oʻquvchi?</strong></p>",
        "choices": ["15", "27", "33", "45"],
        "correct": "27",
        "explanation": "<p><strong>27 ta.</strong> 60 ÷ 100 × 45 = 27. "
                       "Tekshirish: qolgani 60 − 27 = 33 ta, yaʼni 55% ✓ "
                       "<strong>45</strong> — foizning oʻzi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Jami 200 ta javob yigʻildi, ulardan "
                "30 tasi bitta ulushga tegishli.</p><p><strong>Bu necha "
                "foiz?</strong></p>",
        "choices": ["3%", "6,7%", "15%", "30%"],
        "correct": "15%",
        "explanation": "<p><strong>15%.</strong> 30 ÷ 200 = 0,15 → 15%. "
                       "<strong>6,7%</strong> — boʻlish teskari qilingan "
                       "(200 ÷ 30). <strong>30%</strong> — chastota foiz deb "
                       "olingan.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi savol "
                "soʻrovnoma uchun yaxshi?</strong></p>",
        "choices": [
            "Haftada necha marta sport bilan shugʻullanasiz?",
            "Sport yaxshimi?",
            "Sizningcha, sport hamma uchun foydali emasmi?",
            "Nega sport bilan shugʻullanish kerak?",
        ],
        "correct": "Haftada necha marta sport bilan shugʻullanasiz?",
        "explanation": "<p><strong>Haftada necha marta sport bilan "
                       "shugʻullanasiz?</strong> Bu savolga <em>sanab "
                       "boʻladigan</em> javob keladi. «Sport yaxshimi?» ga "
                       "hamma «ha» deydi, uchinchisi esa javobni oʻzi aytib "
                       "turibdi — bunday savol maʼlumotni buzadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bekzod futbol toʻgaragida "
                "soʻrov oʻtkazdi va «maktabning 90 foizi futbolni yoqtiradi» "
                "deb yozdi.</p><p><strong>U haqmi?</strong></p>",
        "choices": [
            "Yoʻq — u faqat futbolchilardan soʻragan",
            "Ha — 90% juda katta son",
            "Ha, agar 20 kishidan koʻp soʻragan boʻlsa",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Yoʻq — u faqat futbolchilardan soʻragan",
        "explanation": "<p><strong>Yoʻq.</strong> Futbol toʻgaragidagilar "
                       "butun maktabni ifodalamaydi — javob boshidanoq "
                       "maʼlum edi. Kimdan soʻralgani natijaning bir qismi va "
                       "u har doim yozib qoʻyiladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Piyoda keladiganlar 18 ta, "
                "velosipedda keladiganlar 6 ta.</p><p><strong>Piyodalar necha "
                "MARTA koʻp?</strong></p>",
        "choices": ["3 marta", "6 marta", "12 marta", "24 marta"],
        "correct": "3 marta",
        "explanation": "<p><strong>3 marta.</strong> «Necha marta» — boʻlish: "
                       "18 ÷ 6 = 3. <strong>12 marta</strong> — bu ayirma "
                       "(18 − 6 = 12), yaʼni «nechtaga koʻp» degan boshqa "
                       "savolning javobi. Ikkalasini chalkashtirish eng koʻp "
                       "uchraydigan xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Jadvaldagi foizlar "
                "yigʻindisi 96% chiqdi.</p><p><strong>Bu nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Hisobda xato bor — yigʻindi 100% boʻlishi kerak",
            "4% javob bermaganlar",
            "Hammasi joyida, 96% ham boʻlaveradi",
            "Soʻralganlar soni notoʻgʻri",
        ],
        "correct": "Hisobda xato bor — yigʻindi 100% boʻlishi kerak",
        "explanation": "<p><strong>Hisobda xato bor.</strong> Butun 100% ga "
                       "boʻlinadi, shuning uchun ulushlarning foizi ham 100 "
                       "ni berishi shart. Javob bermaganlar boʻlsa, ular ham "
                       "alohida qator sifatida jadvalga kiritiladi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>20 oʻquvchidan soʻraldi. "
                "Jadval: 9, 7 va 5.</p>",
        "choices": [
            "Yigʻindi 21 — kimdir ikki marta sanalgan",
            "Yigʻindi 20 — hammasi joyida",
            "Uchta emas, toʻrtta qator boʻlishi kerak",
            "Foizlar yozilmagan",
        ],
        "correct": "Yigʻindi 21 — kimdir ikki marta sanalgan",
        "explanation": "<p><strong>Yigʻindi 21.</strong> 9 + 7 + 5 = 21, "
                       "lekin 20 kishi soʻralgan. Demak bittasi ikki marta "
                       "sanalgan yoki chiziqcha notoʻgʻri oʻqilgan. Jadvalni "
                       "yigʻindi tekshiruvidan oʻtkazmasdan xulosa "
                       "chiqarmang.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>20 oʻquvchidan 8 tasi olmani "
                "tanladi.<br>Yechim: <strong>bu 8%</strong></p>",
        "choices": [
            "Jamiga boʻlinmagan; toʻgʻrisi 40%",
            "100 ga koʻpaytirilmagan; toʻgʻrisi 0,4%",
            "Toʻgʻrisi 80%",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Jamiga boʻlinmagan; toʻgʻrisi 40%",
        "explanation": "<p><strong>Jamiga boʻlinmagan.</strong> Chastotani "
                       "shundoq foiz deb yozib boʻlmaydi: 8 ÷ 20 × 100 = 40%. "
                       "Tekshirish oson — 8 ta 20 tadan koʻp, deyarli "
                       "yarmi, demak javob 8% ga yaqin ham emas.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Dilnoza 80 oʻquvchidan qanday "
                "kelishini soʻradi: piyoda 32 ta, avtobusda 28 ta, mashinada "
                "20 ta.</p><p><strong>Piyoda keladiganlar necha "
                "foiz?</strong></p>",
        "choices": ["20%", "32%", "35%", "40%"],
        "correct": "40%",
        "explanation": "<p><strong>40%.</strong> Avval tekshiramiz: "
                       "32 + 28 + 20 = 80 ✓ Keyin 32 ÷ 80 = 0,4 → 40%. "
                       "<strong>32%</strong> — chastotaning oʻzi foiz deb "
                       "olingan; 80 kishidan soʻralganini unutmang.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bufet uchun 60 oʻquvchidan "
                "soʻraldi: somsa 24, patir 18, pirog 12, boshqasi 6. Bufetchi "
                "ertaga 150 dona pishiriq tayyorlaydi va soʻrov "
                "foizlariga amal qilmoqchi.</p><p><strong>Nechta somsa "
                "qilishi kerak?</strong></p>",
        "choices": ["24 ta", "45 ta", "60 ta", "75 ta"],
        "correct": "60 ta",
        "explanation": "<p><strong>60 ta.</strong> Tekshiruv: "
                       "24 + 18 + 12 + 6 = 60 ✓ Somsaning foizi: "
                       "24 ÷ 60 = 0,4 → 40%. Keyin 150 ÷ 100 × 40 = 60 ta. "
                       "<strong>24 ta</strong> — soʻrovdagi son, buyurtma "
                       "soni emas.</p>",
    },
]


# =====================================================================
# PM-76 — diagramma turlari
# =====================================================================

Q_PM76 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Doiraviy "
                "diagrammada sektor burchagi qanday topiladi?</strong></p>",
        "choices": [
            "ulush ÷ jami × 360",
            "ulush ÷ jami × 100",
            "ulush × 360",
            "jami ÷ ulush × 360",
        ],
        "correct": "ulush ÷ jami × 360",
        "explanation": "<p><strong>ulush ÷ jami × 360.</strong> Butun doira — "
                       "360°, shuning uchun har bir ulushga oʻz ulushicha "
                       "burchak tegadi. <strong>× 100</strong> foiz beradi, "
                       "burchak emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>40 kishidan 10 tasi bitta "
                "javobni tanladi. Bu sektorning burchagi qancha?</strong></p>",
        "choices": ["25°", "90°", "100°", "144°"],
        "correct": "90°",
        "explanation": "<p><strong>90°.</strong> 10 ÷ 40 × 360 = "
                       "0,25 × 360 = 90° — chorak doira. <strong>25°</strong> "
                       "— bu foiz (25%), 360 ga koʻpaytirish qadami tushib "
                       "qolgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Uch yil davomida "
                "maktabdagi oʻquvchilar soni qanday oʻzgarganini koʻrsatmoqchimiz."
                "</p><p><strong>Qaysi diagramma?</strong></p>",
        "choices": ["Chiziqli", "Ustunli", "Doiraviy", "Hech qaysisi"],
        "correct": "Chiziqli",
        "explanation": "<p><strong>Chiziqli.</strong> Maʼlumot vaqt boʻyicha "
                       "yigʻilgan va savol «qanday oʻzgardi» — bu chiziqli "
                       "diagrammaning ishi. Doiraviy bu yerda ishlamaydi: "
                       "yillar butunning boʻlaklari emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oilaning oyligi nimaga "
                "sarflanganini koʻrsatmoqchimiz.</p><p><strong>Qaysi "
                "diagramma?</strong></p>",
        "choices": ["Doiraviy", "Chiziqli", "Ustunli", "Hech qaysisi"],
        "correct": "Doiraviy",
        "explanation": "<p><strong>Doiraviy.</strong> Savol «butundan "
                       "qanchasi» — pul bitta butun boʻlib, u boʻlaklarga "
                       "boʻlinadi. Ustunli ham xato emas, lekin doiraviy "
                       "«hammasi birgalikda 100%» ekanini koʻrsatib "
                       "turadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Doiraviy "
                "diagrammadagi hamma sektorning burchaklari yigʻindisi "
                "qancha?</strong></p>",
        "choices": ["100°", "180°", "360°", "400°"],
        "correct": "360°",
        "explanation": "<p><strong>360°.</strong> Toʻliq doira 360 gradus "
                       "(PM-58), va doira boʻsh joy qoldirmaydi. "
                       "<strong>100°</strong> — foizlar bilan "
                       "chalkashtirilgan: foizlar 100 ni, burchaklar 360 ni "
                       "beradi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>24 kishidan 6 tasi. Sektorning "
                "burchagi qancha?</strong></p>",
        "choices": ["25°", "60°", "90°", "144°"],
        "correct": "90°",
        "explanation": "<p><strong>90°.</strong> 6 ÷ 24 = 0,25, va "
                       "0,25 × 360 = 90°. Chorak — har doim 90°, jami "
                       "qanday boʻlishidan qatʼi nazar.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Sektorning burchagi 108°. Bu "
                "butunning necha foizi?</strong></p>",
        "choices": ["10,8%", "30%", "36%", "108%"],
        "correct": "30%",
        "explanation": "<p><strong>30%.</strong> 108 ÷ 360 = 0,3 → 30%. Tez "
                       "yoʻl: burchakni 3,6 ga boʻling (108 ÷ 3,6 = 30). "
                       "<strong>10,8%</strong> — 10 ga boʻlingan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Bir ulush butunning 45 foizi. "
                "Uning sektor burchagi qancha?</strong></p>",
        "choices": ["45°", "90°", "162°", "180°"],
        "correct": "162°",
        "explanation": "<p><strong>162°.</strong> Foizdan burchakka oʻtish: "
                       "45 × 3,6 = 162°. Yoki 0,45 × 360 = 162. "
                       "<strong>45°</strong> — foiz shundoq gradus deb "
                       "yozilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Doiraviy diagrammada uchta sektor bor: "
                "90°, 120° va 60°.</p><p><strong>Toʻrtinchisi necha "
                "gradus?</strong></p>",
        "choices": ["60°", "90°", "110°", "150°"],
        "correct": "90°",
        "explanation": "<p><strong>90°.</strong> 360 − (90 + 120 + 60) = "
                       "360 − 270 = 90°. Doira toʻliq yopilishi kerak, "
                       "shuning uchun qolgan burchak har doim shu yoʻl bilan "
                       "topiladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>30 kishidan 12 tasi. Sektorning "
                "burchagi qancha?</strong></p>",
        "choices": ["40°", "120°", "144°", "200°"],
        "correct": "144°",
        "explanation": "<p><strong>144°.</strong> 12 ÷ 30 = 0,4, va "
                       "0,4 × 360 = 144°. <strong>40°</strong> — bu foiz "
                       "(40%), 3,6 ga koʻpaytirish qolib ketgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ustunli "
                "diagrammaning sonlar oʻqi qayerdan boshlanishi "
                "kerak?</strong></p>",
        "choices": [
            "Noldan",
            "Eng kichik qiymatdan",
            "Eng katta qiymatdan",
            "Istalgan sondan",
        ],
        "correct": "Noldan",
        "explanation": "<p><strong>Noldan.</strong> Aks holda ustunlarning "
                       "balandligi sonlarga mos kelmay qoladi va kichik farq "
                       "katta koʻrinadi. Bu — diagramma bilan aldashning eng "
                       "keng tarqalgan usuli.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Bir ulush butunning choragi. "
                "Uning burchagi qancha?</strong></p>",
        "choices": ["25°", "45°", "90°", "100°"],
        "correct": "90°",
        "explanation": "<p><strong>90°.</strong> Chorak doira: "
                       "360 ÷ 4 = 90°. <strong>25°</strong> — chorakning "
                       "foizi (25%) gradus deb yozilgan.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Besh xil fandan sinfning "
                "nechta «5» olganini solishtirmoqchimiz.</p><p><strong>Qaysi "
                "diagramma eng qulay?</strong></p>",
        "choices": ["Ustunli", "Chiziqli", "Doiraviy", "Hech qaysisi"],
        "correct": "Ustunli",
        "explanation": "<p><strong>Ustunli.</strong> Savol «qaysi biri koʻp» "
                       "— bu solishtirish. Fanlar vaqt emas, shuning uchun "
                       "chiziqli ishlamaydi; ular bir butunning boʻlagi ham "
                       "emas (bitta oʻquvchi bir nechta «5» olishi "
                       "mumkin).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Doʻkonning yanvardan "
                "dekabrgacha boʻlgan oylik savdosini koʻrsatmoqchimiz."
                "</p><p><strong>Qaysi diagramma?</strong></p>",
        "choices": ["Chiziqli", "Doiraviy", "Ustunli", "Hech qaysisi"],
        "correct": "Chiziqli",
        "explanation": "<p><strong>Chiziqli.</strong> Oylar ketma-ket keladi "
                       "va savol oʻzgarish haqida — chiziq koʻtarilish va "
                       "tushishni koʻrsatadi. Doiraviy bu yerda notoʻgʻri: "
                       "oylar butunning boʻlaklari emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nega bir haftalik "
                "haroratni doiraviy diagrammada koʻrsatib "
                "boʻlmaydi?</strong></p>",
        "choices": [
            "Chunki harorat butunning boʻlagi emas",
            "Chunki yetti sektor juda koʻp",
            "Chunki harorat manfiy boʻlishi mumkin",
            "Chunki gradus ikki xil maʼnoda ishlatiladi",
        ],
        "correct": "Chunki harorat butunning boʻlagi emas",
        "explanation": "<p><strong>Chunki harorat butunning boʻlagi "
                       "emas.</strong> Kunlik haroratlarni qoʻshishning hech "
                       "qanday maʼnosi yoʻq, doiraviy diagramma esa aynan "
                       "yigʻindini boʻlaklarga ajratadi. Bunday maʼlumot "
                       "uchun chiziqli diagramma kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikkita diagramma bir xil "
                "jadvaldan qurildi: biri ustunli, biri doiraviy."
                "</p><p><strong>Ular nima bilan farq qiladi?</strong></p>",
        "choices": [
            "Ustunli sonlarni solishtiradi, doiraviy ulushni koʻrsatadi",
            "Ustunli aniqroq, doiraviy noaniq",
            "Doiraviy faqat katta sonlar uchun",
            "Hech qanday farqi yoʻq",
        ],
        "correct": "Ustunli sonlarni solishtiradi, doiraviy ulushni koʻrsatadi",
        "explanation": "<p><strong>Ustunli sonlarni solishtiradi, doiraviy "
                       "ulushni koʻrsatadi.</strong> Bitta jadval, ikki xil "
                       "savol: «kim koʻp?» va «butundan qanchasi?». "
                       "Diagramma turini maʼlumot emas, <em>savol</em> "
                       "tanlaydi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>20 kishidan 8 tasi. Sektor "
                "burchagi topilmoqchi.<br>Yechim: <strong>8 ÷ 20 × 100 = "
                "40°</strong></p>",
        "choices": [
            "100 emas, 360 ga koʻpaytiriladi; toʻgʻrisi 144°",
            "Boʻlish teskari; toʻgʻrisi 250°",
            "Yana 2 ga koʻpaytirish kerak; toʻgʻrisi 80°",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "100 emas, 360 ga koʻpaytiriladi; toʻgʻrisi 144°",
        "explanation": "<p><strong>100 emas, 360 ga koʻpaytiriladi.</strong> "
                       "8 ÷ 20 × 360 = 144°. Chiqqan 40 — bu foiz, gradus "
                       "emas. Foizdan burchakka oʻtish uchun 3,6 ga "
                       "koʻpaytiring: 40 × 3,6 = 144 ✓</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Doiraviy diagrammaning "
                "sektorlari: 100°, 120°, 80° va 40°.</p>",
        "choices": [
            "Yigʻindi 340° — 20° yetishmayapti",
            "Yigʻindi 360° — hammasi joyida",
            "Sektorlar soni koʻp",
            "Burchaklar foizga aylantirilmagan",
        ],
        "correct": "Yigʻindi 340° — 20° yetishmayapti",
        "explanation": "<p><strong>Yigʻindi 340°.</strong> "
                       "100 + 120 + 80 + 40 = 340, lekin doira 360° boʻlishi "
                       "shart. Demak bitta ulush notoʻgʻri hisoblangan yoki "
                       "bir toifa tushib qolgan. Bu tekshiruvni har safar "
                       "bajaring.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Oilaning bir oylik xarajati "
                "800 000 soʻm: ovqatga 320 000, kommunalga 160 000, kiyimga "
                "120 000, boshqasiga 200 000 soʻm. Bu doiraviy diagrammada "
                "koʻrsatiladi.</p><p><strong>Ovqat sektorining burchagi "
                "qancha?</strong></p>",
        "choices": ["40°", "72°", "144°", "160°"],
        "correct": "144°",
        "explanation": "<p><strong>144°.</strong> Tekshiruv: "
                       "320 + 160 + 120 + 200 = 800 ming ✓ Burchak: "
                       "320 000 ÷ 800 000 = 0,4, va 0,4 × 360 = 144°. "
                       "<strong>40°</strong> — bu foiz (40%).</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>36 oʻquvchidan sevimli fanini "
                "soʻrashdi: matematika 12, ona tili 9, tarix 6, boshqa fanlar "
                "9.</p><p><strong>Matematika sektorining burchagi "
                "qancha?</strong></p>",
        "choices": ["30°", "90°", "120°", "150°"],
        "correct": "120°",
        "explanation": "<p><strong>120°.</strong> Tekshiruv: "
                       "12 + 9 + 6 + 9 = 36 ✓ Matematika uchdan bir ulush: "
                       "12 ÷ 36 = 1/3, va 360 ÷ 3 = 120°. "
                       "<strong>90°</strong> — chorak boʻlganda chiqardi, "
                       "lekin bu yerda ulush uchdan bir.</p>",
    },
]


# =====================================================================
# PM-77 — diagrammani oʻqish
# =====================================================================

Q_PM77 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Jadvalga qarang.</p>" + KITOB_JADVAL +
                "<p><strong>Qaysi oyda eng koʻp kitob olingan?</strong></p>",
        "choices": ["Sentabr", "Oktabr", "Noyabr", "Dekabr"],
        "correct": "Dekabr",
        "explanation": "<p><strong>Dekabr — 60 ta.</strong> Diagrammada bu "
                       "eng baland ustun. <strong>Oktabr</strong> (55) "
                       "ikkinchi oʻrinda; koʻz bilan qaraganda ular yaqin, "
                       "shuning uchun sonni oʻqish shart.</p>",
    },
    {
        "text": "<p>Jadvalga qarang.</p>" + KITOB_JADVAL +
                "<p><strong>Qaysi oyda eng kam kitob olingan?</strong></p>",
        "choices": ["Sentabr", "Noyabr", "Dekabr", "Yanvar"],
        "correct": "Noyabr",
        "explanation": "<p><strong>Noyabr — 35 ta.</strong> Bu eng past "
                       "ustun, lekin nol emas: past ustun «hech kim olmagan» "
                       "degani emas.</p>",
    },
    {
        "text": "<p>Jadvalga qarang.</p>" + KITOB_JADVAL +
                "<p><strong>Eng koʻp va eng kam olingan oylar orasidagi farq "
                "qancha?</strong></p>",
        "choices": ["15 ta", "20 ta", "25 ta", "35 ta"],
        "correct": "25 ta",
        "explanation": "<p><strong>25 ta.</strong> Dekabr 60, Noyabr 35: "
                       "60 − 35 = 25. <strong>20 ta</strong> — Oktabr va "
                       "Noyabrning farqi (55 − 35).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Diagrammani "
                "oʻqishda birinchi navbatda nima qilinadi?</strong></p>",
        "choices": [
            "Sarlavha oʻqiladi",
            "Eng baland ustun topiladi",
            "Xulosa yoziladi",
            "Qiymatlar qoʻshiladi",
        ],
        "correct": "Sarlavha oʻqiladi",
        "explanation": "<p><strong>Sarlavha oʻqiladi.</strong> Tartib shunday: "
                       "sarlavha → oʻq va birlik → qiymatlar → xulosa. "
                       "Sarlavhani oʻqimasdan sonlarga qarash — nimani "
                       "oʻqiyotganingizni bilmaslik degani.</p>",
    },
    {
        "text": "<p>Jadvalga qarang.</p>" + KITOB_JADVAL +
                "<p><strong>Besh oyda jami nechta kitob olingan?</strong></p>",
        "choices": ["195 ta", "215 ta", "235 ta", "260 ta"],
        "correct": "235 ta",
        "explanation": "<p><strong>235 ta.</strong> 40 + 55 = 95; "
                       "95 + 35 = 130; 130 + 60 = 190; 190 + 45 = 235. "
                       "Qoʻshishni bosqichma-bosqich yozib boring — beshta "
                       "sonni birdan qoʻshganda adashish oson.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Jadvalga qarang.</p>" + KITOB_JADVAL +
                "<p><strong>Sentabr va Oktabrda jami nechta kitob "
                "olingan?</strong></p>",
        "choices": ["85 ta", "95 ta", "105 ta", "130 ta"],
        "correct": "95 ta",
        "explanation": "<p><strong>95 ta.</strong> 40 + 55 = 95. "
                       "<strong>130 ta</strong> — Noyabr ham qoʻshib "
                       "yuborilgan (40 + 55 + 35).</p>",
    },
    {
        "text": "<p>Jadvalga qarang.</p>" + KITOB_JADVAL +
                "<p><strong>Oktabr va Noyabrning farqi qancha?</strong></p>",
        "choices": ["10 ta", "15 ta", "20 ta", "25 ta"],
        "correct": "20 ta",
        "explanation": "<p><strong>20 ta.</strong> 55 − 35 = 20. Bu — "
                       "diagrammadagi eng katta pasayish: Oktabrdan Noyabrga "
                       "chiziq keskin tushadi.</p>",
    },
    {
        "text": "<p>Jadvalga qarang.</p>" + NIHOL_JADVAL +
                "<p><strong>Nihol 1-haftadan 2-haftaga necha santimetr "
                "oʻsdi?</strong></p>",
        "choices": ["2 sm", "3 sm", "5 sm", "7 sm"],
        "correct": "3 sm",
        "explanation": "<p><strong>3 sm.</strong> 5 − 2 = 3. "
                       "<strong>5 sm</strong> — 2-haftadagi boʻyining oʻzi, "
                       "oʻsish emas. Oʻsish har doim qoʻshni ikki qiymatning "
                       "<em>farqi</em>.</p>",
    },
    {
        "text": "<p>Jadvalga qarang.</p>" + NIHOL_JADVAL +
                "<p><strong>Nihol qaysi haftada eng tez oʻsgan?</strong></p>",
        "choices": [
            "2-haftadan 3-haftaga",
            "3-haftadan 4-haftaga",
            "4-haftadan 5-haftaga",
            "5-haftadan 6-haftaga",
        ],
        "correct": "3-haftadan 4-haftaga",
        "explanation": "<p><strong>3-haftadan 4-haftaga — 5 sm.</strong> "
                       "Oʻsishlar: 3, 4, 5, 2, 1 sm. Diagrammada bu joyda "
                       "chiziq eng tik koʻtariladi. Eng baland nuqta esa "
                       "6-haftada — «eng baland» va «eng tez oʻsgan» ikki xil "
                       "savol.</p>",
    },
    {
        "text": "<p>Jadvalga qarang.</p>" + NIHOL_JADVAL +
                "<p><strong>Olti hafta davomida nihol jami necha santimetr "
                "oʻsdi?</strong></p>",
        "choices": ["15 sm", "17 sm", "19 sm", "63 sm"],
        "correct": "15 sm",
        "explanation": "<p><strong>15 sm.</strong> Oxirgi boʻyidan "
                       "birinchisini ayiramiz: 17 − 2 = 15 sm. "
                       "<strong>17 sm</strong> — oxirgi boʻyi, oʻsish emas: "
                       "nihol boshida ham 2 sm edi.</p>",
    },
    {
        "text": "<p>Jadvalga qarang.</p>" + KITOB_JADVAL +
                "<p><strong>Yanvarda Dekabrga nisbatan necha foizga kam kitob "
                "olingan?</strong></p>",
        "choices": ["15%", "25%", "33%", "45%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> Farq: 60 − 45 = 15. Asos — "
                       "<em>eski</em> son, yaʼni Dekabrning 60 tasi: "
                       "15 ÷ 60 × 100 = 25% (PM-25). <strong>33%</strong> — "
                       "yangi songa boʻlingan (15 ÷ 45), bu eng qimmat "
                       "xato.</p>",
    },
    {
        "text": "<p>Jadvalga qarang.</p>" + KITOB_JADVAL +
                "<p><strong>Oktabrda Sentabrga nisbatan necha foizga koʻp "
                "kitob olingan?</strong></p>",
        "choices": ["15%", "27,3%", "37,5%", "55%"],
        "correct": "37,5%",
        "explanation": "<p><strong>37,5%.</strong> Farq: 55 − 40 = 15. Asos — "
                       "Sentabrning 40 tasi: 15 ÷ 40 × 100 = 37,5%. "
                       "<strong>27,3%</strong> — asos qilib 55 olingan "
                       "(15 ÷ 55); oshishda asos har doim <em>eski</em> "
                       "son.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Jadvalga qarang.</p>" + KITOB_JADVAL +
                "<p><strong>Dekabrda Noyabrga nisbatan NECHTAGA koʻp kitob "
                "olingan?</strong></p>",
        "choices": ["1,7 taga", "15 taga", "25 taga", "95 taga"],
        "correct": "25 taga",
        "explanation": "<p><strong>25 taga.</strong> «Nechtaga» — ayirish: "
                       "60 − 35 = 25. <strong>1,7 taga</strong> — bu boʻlish "
                       "natijasi (60 ÷ 35 ≈ 1,7), yaʼni «necha marta» degan "
                       "boshqa savolning javobi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Faraz qilaylik, Noyabrda 30 ta "
                "kitob olingan boʻlsin. Dekabrda esa 60 ta.</p><p><strong>Dekabr "
                "Noyabrdan necha MARTA koʻp?</strong></p>",
        "choices": ["1,5 marta", "2 marta", "30 marta", "90 marta"],
        "correct": "2 marta",
        "explanation": "<p><strong>2 marta.</strong> «Necha marta» — boʻlish: "
                       "60 ÷ 30 = 2. <strong>1,5 marta</strong> — Noyabr oʻrniga "
                       "Sentabrning 40 tasi olingan (60 ÷ 40). "
                       "<strong>30 marta</strong> — bu ayirma "
                       "(60 − 30 = 30), «nechtaga koʻp» degan savolning "
                       "javobi. Ikki savolni ajratib oʻqing.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Diagramma nimani "
                "koʻrsatmaydi?</strong></p>",
        "choices": [
            "Nima uchun shunday boʻlganini",
            "Eng katta qiymatni",
            "Qiymatlar orasidagi farqni",
            "Qiymatlarning oʻzgarishini",
        ],
        "correct": "Nima uchun shunday boʻlganini",
        "explanation": "<p><strong>Nima uchun shunday boʻlganini.</strong> "
                       "Dekabrda kitob koʻp olingani koʻrinadi, lekin sababi "
                       "— taʼtilmi, yangi kitoblarmi, topshiriqmi — "
                       "koʻrinmaydi. Sababni aytish uchun qoʻshimcha maʼlumot "
                       "kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sherbek diagrammaga qarab "
                "«Noyabrda hech kim kitob olmagan» dedi.</p><p><strong>U "
                "haqmi?</strong></p>",
        "choices": [
            "Yoʻq — Noyabrda 35 ta olingan, bu eng kam, lekin nol emas",
            "Ha — Noyabr ustuni eng past",
            "Ha, chunki ustun oʻq chizigʻiga tegib turibdi",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Yoʻq — Noyabrda 35 ta olingan, bu eng kam, lekin nol emas",
        "explanation": "<p><strong>Yoʻq.</strong> «Eng kam» bilan «yoʻq» "
                       "butunlay boshqa narsa. Ustunning pastligi uning "
                       "boʻshligini anglatmaydi — oʻqdagi songa qarash "
                       "kerak.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>Dekabr 60 ta, Yanvar 45 ta. "
                "Kamayish foizi topilmoqchi.<br>Yechim: <strong>15 ÷ 45 × 100 "
                "≈ 33%</strong></p>",
        "choices": [
            "Asos notoʻgʻri; toʻgʻrisi 15 ÷ 60 × 100 = 25%",
            "Farq notoʻgʻri; toʻgʻrisi 105 ÷ 60 × 100",
            "100 ga koʻpaytirish ortiqcha",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Asos notoʻgʻri; toʻgʻrisi 15 ÷ 60 × 100 = 25%",
        "explanation": "<p><strong>Asos notoʻgʻri.</strong> Foiz "
                       "<em>nimadan</em> oʻzgarganiga nisbatan olinadi — bu "
                       "yerda Dekabrning 60 tasidan (PM-25). Yangi songa "
                       "boʻlish har doim kattaroq, notoʻgʻri javob "
                       "beradi.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p>" + NIHOL_JADVAL +
                "<p>«Nihol 6-haftada eng tez oʻsgan, chunki oʻshanda eng "
                "baland edi.»</p>",
        "choices": [
            "Eng baland boʻlish eng tez oʻsish emas; 6-haftada atigi 1 sm",
            "Nihol 6-haftada eng baland emas edi",
            "Oʻsish 5-haftada eng katta boʻlgan",
            "Xato yoʻq, xulosa toʻgʻri",
        ],
        "correct": "Eng baland boʻlish eng tez oʻsish emas; 6-haftada atigi 1 sm",
        "explanation": "<p><strong>Eng baland boʻlish eng tez oʻsish "
                       "emas.</strong> 6-haftada nihol haqiqatan eng baland "
                       "(17 sm), lekin oʻsha hafta atigi 17 − 16 = 1 sm "
                       "oʻsgan — eng sekin. Eng tez oʻsish 3-haftadan "
                       "4-haftaga, 5 sm.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p>" + KITOB_JADVAL +
                "<p>Kutubxonachi Fevral uchun ham hisob yuritdi: 45 ta kitob "
                "olingan.</p><p><strong>Olti oyda jami nechta kitob "
                "olingan?</strong></p>",
        "choices": ["235 ta", "260 ta", "280 ta", "325 ta"],
        "correct": "280 ta",
        "explanation": "<p><strong>280 ta.</strong> Besh oydagi jami 235 ta "
                       "edi (40 + 55 + 35 + 60 + 45). Fevralni qoʻshamiz: "
                       "235 + 45 = 280 ta. <strong>235 ta</strong> — Fevral "
                       "qoʻshilmagan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Kutubxonachi besh oyda olingan "
                "235 ta kitobning har 20 tasi uchun bitta yangi javon "
                "olmoqchi.</p><p><strong>Nechta javon kerak "
                "boʻladi?</strong></p>",
        "choices": ["11 ta", "12 ta", "13 ta", "24 ta"],
        "correct": "12 ta",
        "explanation": "<p><strong>12 ta.</strong> 235 ÷ 20 = 11,75. Javonni "
                       "boʻlib olib boʻlmaydi, qolgan kitoblarga ham joy "
                       "kerak — shuning uchun <em>yuqoriga</em> yaxlitlanadi "
                       "(PM-14): 12 ta. <strong>11 ta</strong> bilan "
                       "220 tagina kitob joylashadi, 15 tasi ochiqda "
                       "qoladi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-75 Mashq: Maʼlumot yigʻish va jadval",
        "tutorial":    "PM-75:",
        "description": (
            "Soʻrovnoma savoli, chiziqcha bilan sanash, chastota jadvali va "
            "ulushning foizi. 20 savol."
        ),
        "questions":   Q_PM75,
        **DEFAULTS,
    },
    {
        "title":       "PM-76 Mashq: Diagramma turlari",
        "tutorial":    "PM-76:",
        "description": (
            "Ustunli, chiziqli va doiraviy diagramma, sektor burchagi va "
            "toʻgʻri turini tanlash. 20 savol."
        ),
        "questions":   Q_PM76,
        **DEFAULTS,
    },
    {
        "title":       "PM-77 Mashq: Diagrammani oʻqish",
        "tutorial":    "PM-77:",
        "description": (
            "Diagrammadan eng katta, eng kichik, farq, jami va sakrashni "
            "topish hamda foiz oʻzgarishi. 20 savol."
        ),
        "questions":   Q_PM77,
        **DEFAULTS,
    },
]
