# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-54, PM-55, PM-56 (qoʻshish usuli, sistemali matnli
masala, parabola).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: `medium` (Blok D).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq. Savol matnida <strong>, <sup> mumkin.
⚠️ Kumulyativ: kvadrat tenglamani yechish YOʻQ (keyingi bloklar), perimetr/yuza
   formulalari (PM-67, PM-68) YOʻQ, Pifagor (PM-64) YOʻQ.
   PM-54 da sistema QOʻSHISH usuli bilan, PM-55 da qulay usul tanlanadi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_54_56.py --master=prime \\
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
# PM-54 — sistemani qoʻshish usuli bilan yechish
# =====================================================================

Q_PM54 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qoʻshish usulining "
                "maqsadi nima?</strong></p>",
        "choices": [
            "Nomaʼlumlardan birini butunlay yoʻqotish",
            "Ikkala tenglamani soddalashtirish",
            "Grafikni chizmasdan kesishgan nuqtani chamalash",
            "Koeffitsientlarni kasrga aylantirish",
        ],
        "correct": "Nomaʼlumlardan birini butunlay yoʻqotish",
        "explanation": "<p><strong>Nomaʼlumlardan birini butunlay yoʻqotish.</strong> "
                       "Ikki tenglamani qoʻshganda (yoki ayirganda) bir nomaʼlum "
                       "bekor boʻladi va ikki nomaʼlumli sistemadan bitta oddiy "
                       "tenglama qoladi. Qolgan variantlar chiroyli eshitiladi, "
                       "lekin usulning maqsadi emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>x + y = 9 va x − y = 1 "
                "tenglamalarini qoʻshsak nima chiqadi?</strong></p>",
        "choices": ["2x = 8", "2x = 10", "2y = 10", "x = 10"],
        "correct": "2x = 10",
        "explanation": "<p><strong>2x = 10.</strong> Chap tomonlar qoʻshiladi: "
                       "(x + y) + (x − y) = 2x, chunki +y va −y bir-birini yoʻq "
                       "qiladi. Oʻng tomonlar ham qoʻshiladi: 9 + 1 = 10. "
                       "<strong>2x = 8</strong> — oʻng tomonda qoʻshish oʻrniga "
                       "ayirish qilingan.</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>x + y = 7, x − y = 3</strong></p>",
        "choices": ["(2; 5)", "(4; 3)", "(5; 2)", "(7; 3)"],
        "correct": "(5; 2)",
        "explanation": "<p><strong>(5; 2).</strong> Qoʻshamiz: 2x = 10, demak "
                       "x = 5. Keyin 5 + y = 7, y = 2. Tekshirish: 5 − 2 = 3 ✓ "
                       "<strong>(2; 5)</strong> — x bilan y oʻrni almashtirilgan "
                       "javob; juftlikda avval x yoziladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2x + y = 9 va 3x − y = 11 "
                "qoʻshilsa nima chiqadi?</strong></p>",
        "choices": ["5x = 2", "5x = 20", "x + 2y = 20", "6x = 20"],
        "correct": "5x = 20",
        "explanation": "<p><strong>5x = 20.</strong> 2x + 3x = 5x, +y va −y "
                       "yoʻqoladi, 9 + 11 = 20. Demak x = 4. "
                       "<strong>6x = 20</strong> — koeffitsientlar qoʻshilmay, "
                       "koʻpaytirilgan (2 × 3).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki tenglamada nomaʼlum "
                "oldidagi koeffitsientlar bir xil boʻlsa nima qilinadi?</strong></p>",
        "choices": [
            "Tenglamalar ayiriladi",
            "Tenglamalar qoʻshiladi",
            "Ikkalasi 2 ga koʻpaytiriladi",
            "Sistema yechilmaydi",
        ],
        "correct": "Tenglamalar ayiriladi",
        "explanation": "<p><strong>Tenglamalar ayiriladi.</strong> Bir xil narsani "
                       "yoʻqotish uchun uni ayirish kerak: 2y − 2y = 0. Qoʻshsak "
                       "aksincha 4y chiqadi va hech narsa yoʻqolmaydi. Qoida qisqa: "
                       "<strong>bir xil — ayiramiz, qarama-qarshi — "
                       "qoʻshamiz</strong>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Sistemani yeching.</p><p><strong>2x + y = 13, 3x − y = 12</strong></p>",
        "choices": ["(3; 7)", "(5; 3)", "(5; 5)", "(6; 1)"],
        "correct": "(5; 3)",
        "explanation": "<p><strong>(5; 3).</strong> y oldida +1 va −1 — "
                       "qarama-qarshi, demak qoʻshamiz: 5x = 25, x = 5. Keyin "
                       "2 × 5 + y = 13, y = 3. Tekshirish: 3 × 5 − 3 = 12 ✓</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>4x + 3y = 23, 4x − y = 3</strong></p>",
        "choices": ["(2; 5)", "(3; 4)", "(5; 1)", "(5; 2)"],
        "correct": "(2; 5)",
        "explanation": "<p><strong>(2; 5).</strong> x oldida ikkalasida ham 4 — "
                       "ayiramiz: 3y − (−y) = 4y va 23 − 3 = 20, demak 4y = 20, "
                       "y = 5. Keyin 4x − 5 = 3, 4x = 8, x = 2. Tekshirish: "
                       "4 × 2 + 3 × 5 = 8 + 15 = 23 ✓</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>3x + y = 14, 2x − 3y = 2</strong></p>",
        "choices": ["(2; 8)", "(4; 2)", "(4; 3)", "(5; −1)"],
        "correct": "(4; 2)",
        "explanation": "<p><strong>(4; 2).</strong> Birinchi tenglamani 3 ga "
                       "koʻpaytiramiz: 9x + 3y = 42 (oʻng tomon ham koʻpaydi!). "
                       "Ikkinchisi bilan qoʻshamiz: 11x = 44, x = 4. Keyin "
                       "3 × 4 + y = 14, y = 2. Tekshirish: 2 × 4 − 3 × 2 = 2 ✓</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>2x + 3y = 16, 5x − 2y = 2</strong></p>",
        "choices": ["(2; 4)", "(3; 3)", "(4; 2)", "(5; 2)"],
        "correct": "(2; 4)",
        "explanation": "<p><strong>(2; 4).</strong> y ning koeffitsientlari 3 va 2, "
                       "EKUK i 6: birinchisini 2 ga, ikkinchisini 3 ga "
                       "koʻpaytiramiz — 4x + 6y = 32 va 15x − 6y = 6. Qoʻshamiz: "
                       "19x = 38, x = 2. Keyin 2 × 2 + 3y = 16, 3y = 12, y = 4. "
                       "Tekshirish: 5 × 2 − 2 × 4 = 2 ✓</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>5x − 2y = 11, 3x + 2y = 13</strong></p>",
        "choices": ["(2; 3)", "(3; 2)", "(3; 4)", "(4; 1)"],
        "correct": "(3; 2)",
        "explanation": "<p><strong>(3; 2).</strong> y oldida −2 va +2 — "
                       "qarama-qarshi, qoʻshamiz: 8x = 24, x = 3. Keyin "
                       "3 × 3 + 2y = 13, 2y = 4, y = 2. Tekshirish: "
                       "5 × 3 − 2 × 2 = 15 − 4 = 11 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>4x − y = 22 tenglamasi "
                "3 ga koʻpaytirilsa nima chiqadi?</strong></p>",
        "choices": [
            "4x − 3y = 22",
            "12x − 3y = 22",
            "12x − 3y = 66",
            "12x − y = 66",
        ],
        "correct": "12x − 3y = 66",
        "explanation": "<p><strong>12x − 3y = 66.</strong> Tenglamani songa "
                       "koʻpaytirganda <strong>har bir had</strong> koʻpayadi, oʻng "
                       "tomon ham: 4x × 3 = 12x, −y × 3 = −3y, 22 × 3 = 66. "
                       "<strong>12x − 3y = 22</strong> — eng koʻp uchraydigan xato: "
                       "oʻng tomon unutilgan. Tarozining bitta tovoqchasini "
                       "ogʻirlashtirib boʻlmaydi.</p>",
    },
    {
        "text": "<p>Sistemani yeching.</p><p><strong>x + 2y = 11, 3x − 2y = 9</strong></p>",
        "choices": ["(3; 4)", "(4; 3)", "(5; 3)", "(5; 4)"],
        "correct": "(5; 3)",
        "explanation": "<p><strong>(5; 3).</strong> y oldida +2 va −2 — qoʻshamiz: "
                       "4x = 20, x = 5. Keyin 5 + 2y = 11, 2y = 6, y = 3. "
                       "Tekshirish: 3 × 5 − 2 × 3 = 15 − 6 = 9 ✓</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3x + 2y = 31 va "
                "x + 2y = 17. Nomaʼlumni yoʻqotish uchun nima qilinadi?</strong></p>",
        "choices": [
            "Tenglamalar ayiriladi",
            "Tenglamalar qoʻshiladi",
            "Birinchisi 2 ga koʻpaytiriladi",
            "Ikkinchisi 3 ga koʻpaytiriladi",
        ],
        "correct": "Tenglamalar ayiriladi",
        "explanation": "<p><strong>Tenglamalar ayiriladi.</strong> y oldida "
                       "ikkalasida ham +2 turibdi — bir xil koeffitsient ayirish "
                       "bilan yoʻqoladi: 2x = 14, x = 7. Agar qoʻshsak "
                       "4x + 4y = 48 chiqadi — ikkala nomaʼlum ham qolib ketadi, "
                       "yaʼni ish oldinga siljimaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi sistemada hech "
                "narsani koʻpaytirmasdan, darrov qoʻshish mumkin?</strong></p>",
        "choices": [
            "5x + 4y = 18 va 2x − 4y = 6",
            "3x + 2y = 7 va 5x + 3y = 9",
            "x + 2y = 8 va 3x + 5y = 1",
            "2x + y = 5 va 4x + 3y = 11",
        ],
        "correct": "5x + 4y = 18 va 2x − 4y = 6",
        "explanation": "<p><strong>5x + 4y = 18 va 2x − 4y = 6.</strong> y oldida "
                       "+4 va −4 — qarama-qarshi sonlar, qoʻshsak darrov yoʻqoladi: "
                       "7x = 24. Qolgan uchtasida hech bir juft koeffitsient na "
                       "teng, na qarama-qarshi, shuning uchun avval koʻpaytirish "
                       "kerak boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>x + y = 5 va x + y = 8 "
                "ayirilganda 0 = 3 chiqdi. Bu nimani bildiradi?</strong></p>",
        "choices": [
            "Sistemaning yechimi yoʻq",
            "Sistemaning cheksiz koʻp yechimi bor",
            "Yechim (0; 3)",
            "Hisobda xato bor, qaytadan yechish kerak",
        ],
        "correct": "Sistemaning yechimi yoʻq",
        "explanation": "<p><strong>Sistemaning yechimi yoʻq.</strong> 0 = 3 — "
                       "yolgʻon tenglik, uni hech qanday x va y bajara olmaydi. "
                       "Grafikda bu ikki <strong>parallel</strong> chiziq: bir xil "
                       "qiyalik, har xil joy — ular hech qachon kesishmaydi "
                       "(PM-52).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2x + 2y = 10 va "
                "x + y = 5 sistemasining yechimlari qanday?</strong></p>",
        "choices": [
            "Bitta yechim: (5; 0)",
            "Bitta yechim: (2,5; 2,5)",
            "Cheksiz koʻp yechim",
            "Yechim yoʻq",
        ],
        "correct": "Cheksiz koʻp yechim",
        "explanation": "<p><strong>Cheksiz koʻp yechim.</strong> Birinchi tenglama "
                       "ikkinchisining 2 ga koʻpaytirilgani — bu bitta chiziqning "
                       "ikki xil yozuvi. Ayirsak 0 = 0 chiqadi, yaʼni har doim "
                       "toʻgʻri. x + y = 5 ni bajaradigan har bir juftlik — (5; 0), "
                       "(2,5; 2,5), (1; 4) — yechim boʻladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>4x − y = 22 | × 3 → "
                "12x − 3y = 22</strong></p>",
        "choices": [
            "Oʻng tomon koʻpaytirilmagan, 66 boʻlishi kerak",
            "4x 3 ga koʻpaytirilmasligi kerak edi",
            "−y ning ishorasi notoʻgʻri",
            "Xato yoʻq, yozuv toʻgʻri",
        ],
        "correct": "Oʻng tomon koʻpaytirilmagan, 66 boʻlishi kerak",
        "explanation": "<p><strong>Oʻng tomon koʻpaytirilmagan.</strong> Toʻgʻrisi "
                       "12x − 3y = <strong>66</strong>, chunki 22 × 3 = 66. "
                       "Tenglama — muvozanatdagi tarozi: chap tomonni 3 barobar "
                       "ogʻirlashtirsangiz, oʻng tomonni ham shuncha "
                       "ogʻirlashtirasiz.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>(3x + 2y) − (x + 2y) "
                "= ?</strong></p>",
        "choices": ["2x", "2x + 4y", "4x + 4y", "2x − 4y"],
        "correct": "2x",
        "explanation": "<p><strong>2x.</strong> Qavsni ayirganda ichidagi har bir "
                       "hadning ishorasi almashadi (PM-33): 3x + 2y − x − 2y. "
                       "Endi 3x − x = 2x va 2y − 2y = 0. "
                       "<strong>2x + 4y</strong> — faqat birinchi hadning ishorasi "
                       "oʻzgartirilgan, +2y esa oʻz holicha qoldirilgan; bu eng "
                       "koʻp uchraydigan xato.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Choyxonada 3 ta somsa va 2 ta choy 35 000 soʻm turadi. "
                "3 ta somsa va 5 ta choy esa 47 000 soʻm.</p>"
                "<p><strong>Bitta somsa va bitta choy necha soʻm?</strong></p>",
        "choices": [
            "Somsa 7 000, choy 5 000",
            "Somsa 8 000, choy 4 500",
            "Somsa 9 000, choy 4 000",
            "Somsa 10 000, choy 3 500",
        ],
        "correct": "Somsa 9 000, choy 4 000",
        "explanation": "<p><strong>Somsa 9 000, choy 4 000 soʻm.</strong> "
                       "3s + 2c = 35 000 va 3s + 5c = 47 000. Ikkala hisobda ham "
                       "3 ta somsa bor — demak ayiramiz: 3c = 12 000, c = 4 000. "
                       "Keyin 3s + 8 000 = 35 000, 3s = 27 000, s = 9 000. "
                       "Tekshirish: 3 × 9 000 + 5 × 4 000 = 27 000 + 20 000 "
                       "= 47 000 ✓</p>",
    },
    {
        "text": "<p>Ustaxonada usta 2 soat va shogird 3 soat ishlaganda ish haqi "
                "46 000 soʻm boʻladi. Usta 4 soat va shogird 1 soat ishlaganda esa "
                "42 000 soʻm.</p><p><strong>Ustaning bir soatlik ish haqi "
                "qancha?</strong></p>",
        "choices": ["6 000 soʻm", "8 000 soʻm", "10 000 soʻm", "12 000 soʻm"],
        "correct": "8 000 soʻm",
        "explanation": "<p><strong>8 000 soʻm.</strong> 2u + 3sh = 46 000 va "
                       "4u + sh = 42 000. Ikkinchisini 3 ga koʻpaytiramiz: "
                       "12u + 3sh = 126 000. Birinchisidan ayiramiz: 10u = 80 000, "
                       "u = 8 000. Shogirdniki: sh = 42 000 − 32 000 = 10 000. "
                       "Tekshirish: 2 × 8 000 + 3 × 10 000 = 16 000 + 30 000 "
                       "= 46 000 ✓</p>",
    },
]


# =====================================================================
# PM-55 — sistema bilan yechiladigan matnli masalalar
# =====================================================================

Q_PM55 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri tenglamani tanlang.</p><p><strong>«Qutida jami 20 ta "
                "qalam va ruchka bor.»</strong></p>",
        "choices": ["q + r = 20", "q − r = 20", "q × r = 20", "q = 20r"],
        "correct": "q + r = 20",
        "explanation": "<p><strong>q + r = 20.</strong> «Jami» — qoʻshish: "
                       "qalamlar soni va ruchkalar soni birga 20 ta. Bu — "
                       "<strong>soni</strong> haqidagi tenglama; narx haqidagisi "
                       "boshqa tenglama boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri tenglamani tanlang.</p><p><strong>«Qizlar oʻgʻillardan "
                "6 ta koʻp.»</strong></p>",
        "choices": ["q = oʻ + 6", "q = 6oʻ", "q + oʻ = 6", "oʻ = q + 6"],
        "correct": "q = oʻ + 6",
        "explanation": "<p><strong>q = oʻ + 6.</strong> «6 <strong>ta</strong> "
                       "koʻp» — qoʻshish. <strong>q = 6oʻ</strong> «6 "
                       "<strong>marta</strong> koʻp» degani boʻlardi — bu butunlay "
                       "boshqa maʼno va imtihonda eng koʻp ochko yoʻqotadigan "
                       "oʻqish xatosi.</p>",
    },
    {
        "text": "<p>Toʻgʻri tenglamani tanlang.</p><p><strong>«Otasi oʻgʻlidan "
                "5 marta katta.»</strong></p>",
        "choices": ["o = 5b", "o = b + 5", "o + b = 5", "b = 5o"],
        "correct": "o = 5b",
        "explanation": "<p><strong>o = 5b.</strong> «5 <strong>marta</strong> "
                       "katta» — koʻpaytirish. <strong>o = b + 5</strong> «5 "
                       "<strong>yosh</strong> katta» degani boʻlardi. Jumlani ovoz "
                       "chiqarib oʻqing: «ta» — qoʻshish, «marta» — "
                       "koʻpaytirish.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Ikki sonning yigʻindisi 40, "
                "farqi 8. Bu sonlar qaysilar?</strong></p>",
        "choices": ["16 va 24", "18 va 22", "20 va 20", "24 va 32"],
        "correct": "16 va 24",
        "explanation": "<p><strong>16 va 24.</strong> x + y = 40 va x − y = 8. "
                       "Qoʻshamiz: 2x = 48, x = 24, keyin y = 16. Tekshirish: "
                       "24 + 16 = 40 ✓ va 24 − 16 = 8 ✓ <strong>18 va 22</strong> "
                       "— yigʻindisi toʻgʻri, lekin farqi 4, 8 emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Masalada ikkita nomaʼlum "
                "boʻlsa, nechta tenglama kerak boʻladi?</strong></p>",
        "choices": [
            "Ikkita — har biri matnning boshqa jumlasidan",
            "Bitta yetadi",
            "Uchta, tekshirish uchun bittasi qoʻshimcha",
            "Nomaʼlumlar soniga bogʻliq emas",
        ],
        "correct": "Ikkita — har biri matnning boshqa jumlasidan",
        "explanation": "<p><strong>Ikkita, va ular turli jumlalardan chiqishi "
                       "shart.</strong> Bitta tenglama ikki nomaʼlumni aniqlay "
                       "olmaydi. Agar ikkala tenglama bitta jumlaning ikki xil "
                       "yozuvi boʻlsa, sistema cheksiz koʻp yechim beradi va masala "
                       "yechilmaydi (PM-52).</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Masalani yeching.</p><p>Sinfda 30 oʻquvchi bor. Qizlar "
                "oʻgʻillardan 6 ta koʻp.</p><p><strong>Nechta qiz bor?</strong></p>",
        "choices": ["12 ta", "15 ta", "18 ta", "24 ta"],
        "correct": "18 ta",
        "explanation": "<p><strong>18 ta qiz.</strong> q + oʻ = 30 va q − oʻ = 6. "
                       "Qoʻshamiz: 2q = 36, q = 18, demak oʻgʻillar 12 ta. "
                       "Tekshirish: 18 + 12 = 30 ✓ va 18 − 12 = 6 ✓ "
                       "<strong>12 ta</strong> — bu oʻgʻillar soni, savol esa "
                       "qizlar haqida.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sherbek 10 ta narsa oldi: daftar "
                "3 000 soʻmdan, ruchka 2 000 soʻmdan. Hammasiga 26 000 soʻm "
                "toʻladi.</p><p><strong>Nechta daftar olgan?</strong></p>",
        "choices": ["4 ta", "5 ta", "6 ta", "7 ta"],
        "correct": "6 ta",
        "explanation": "<p><strong>6 ta daftar.</strong> d + r = 10 va "
                       "3 000d + 2 000r = 26 000. r = 10 − d ni qoʻysak: "
                       "3 000d + 20 000 − 2 000d = 26 000, 1 000d = 6 000, d = 6. "
                       "Ruchka 4 ta. Tekshirish: 6 × 3 000 + 4 × 2 000 = 18 000 + "
                       "8 000 = 26 000 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ota va oʻgʻilning yoshi birgalikda 50. "
                "Otasi oʻgʻlidan 26 yosh katta.</p><p><strong>Oʻgʻil necha "
                "yoshda?</strong></p>",
        "choices": ["10 yoshda", "12 yoshda", "14 yoshda", "24 yoshda"],
        "correct": "12 yoshda",
        "explanation": "<p><strong>12 yoshda.</strong> o + b = 50 va o − b = 26. "
                       "Qoʻshamiz: 2o = 76, o = 38, demak b = 50 − 38 = 12. "
                       "Tekshirish: 38 − 12 = 26 ✓ <strong>24 yoshda</strong> — "
                       "farqning yarmi olingan, bu esa yosh emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki shahar orasi 360 km. Ikki mashina "
                "bir-biriga qarab yoʻlga chiqdi va 3 soatdan keyin uchrashdi. "
                "Birining tezligi ikkinchisinikidan 20 km/soat "
                "ortiq.</p><p><strong>Tezroq mashinaning tezligi qancha?</strong></p>",
        "choices": ["50 km/soat", "60 km/soat", "70 km/soat", "80 km/soat"],
        "correct": "70 km/soat",
        "explanation": "<p><strong>70 km/soat.</strong> Bir-biriga qarab "
                       "yurganda tezliklar qoʻshiladi: 360 ÷ 3 = 120, demak "
                       "v₁ + v₂ = 120 va v₁ − v₂ = 20. Qoʻshamiz: 2v₁ = 140, "
                       "v₁ = 70, v₂ = 50. Tekshirish: (70 + 50) × 3 = 360 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Muzeyga 15 ta chipta olindi. Katta odam "
                "chiptasi 12 000 soʻm, bola chiptasi 5 000 soʻm. Hammasiga 138 000 "
                "soʻm toʻlandi.</p><p><strong>Nechta katta odam chiptasi "
                "olingan?</strong></p>",
        "choices": ["6 ta", "8 ta", "9 ta", "10 ta"],
        "correct": "9 ta",
        "explanation": "<p><strong>9 ta.</strong> k + b = 15 va 12 000k + 5 000b "
                       "= 138 000. b = 15 − k ni qoʻysak: 12 000k + 75 000 − "
                       "5 000k = 138 000, 7 000k = 63 000, k = 9. Bola chiptasi "
                       "6 ta. Tekshirish: 9 × 12 000 + 6 × 5 000 = 108 000 + "
                       "30 000 = 138 000 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Ikki sonning yigʻindisi 72, "
                "biri ikkinchisidan 3 marta katta. Katta son qaysi?</strong></p>",
        "choices": ["18", "24", "36", "54"],
        "correct": "54",
        "explanation": "<p><strong>54.</strong> x + y = 72 va x = 3y. "
                       "3y + y = 72, 4y = 72, y = 18, demak x = 54. Tekshirish: "
                       "54 + 18 = 72 ✓ va 54 ÷ 18 = 3 ✓ <strong>24</strong> — "
                       "72 ni 3 ga boʻlganda chiqadi, lekin yigʻindi 3 ta emas, "
                       "<strong>4 ta</strong> ulushga boʻlinadi (3 ulush katta "
                       "songa, 1 ulush kichigiga).</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Afsona bilan Dilnozada birgalikda "
                "90 000 soʻm bor. Afsonada Dilnozanikidan 14 000 soʻm "
                "koʻp.</p><p><strong>Afsonada qancha pul bor?</strong></p>",
        "choices": ["38 000 soʻm", "45 000 soʻm", "52 000 soʻm", "62 000 soʻm"],
        "correct": "52 000 soʻm",
        "explanation": "<p><strong>52 000 soʻm.</strong> a + d = 90 000 va "
                       "a − d = 14 000. Qoʻshamiz: 2a = 104 000, a = 52 000, demak "
                       "d = 38 000. Tekshirish: 52 000 − 38 000 = 14 000 ✓ "
                       "<strong>38 000</strong> — bu Dilnozaning puli.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri tenglamani tanlang.</p><p><strong>«Sherbekda Bekzodnikidan "
                "3 marta koʻp pul bor.»</strong></p>",
        "choices": ["s = 3b", "s = b + 3", "s + b = 3", "3s = b"],
        "correct": "s = 3b",
        "explanation": "<p><strong>s = 3b.</strong> «marta» — koʻpaytirish. "
                       "<strong>s = b + 3</strong> «3 soʻm koʻp» degani boʻlardi — "
                       "3 soʻm bilan uch barobar orasidagi farq juda katta. "
                       "<strong>3s = b</strong> esa aksincha: Bekzodda koʻp "
                       "boʻlib qoladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>12 ta chipta olindi va hammasiga "
                "100 000 soʻm toʻlandi.</p><p><strong>Qaysi tenglama "
                "notoʻgʻri?</strong></p>",
        "choices": [
            "k + b = 100 000",
            "k + b = 12",
            "8 000k + 6 000b = 100 000",
            "b = 12 − k",
        ],
        "correct": "k + b = 100 000",
        "explanation": "<p><strong>k + b = 100 000 notoʻgʻri.</strong> Chap tomonda "
                       "chiptalar <strong>soni</strong>, oʻng tomonda esa "
                       "<strong>soʻm</strong> turibdi — bir-biriga teng "
                       "boʻlolmaydi. 12 ta chipta 100 000 soʻmga teng emas, 100 000 "
                       "soʻm <strong>turadi</strong>. Soni alohida tenglama, puli "
                       "alohida tenglama.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻquvchi «jami 30 ta» va "
                "«ikkalasining soni birga 30 ta» degan ikki jumladan ikki tenglama "
                "tuzdi.</p><p><strong>Nega bu sistema masalani "
                "yechmaydi?</strong></p>",
        "choices": [
            "Ikkala tenglama bir xil maʼlumot beradi",
            "Tenglamalar qarama-qarshi, yechim yoʻq",
            "Nomaʼlumlar notoʻgʻri belgilangan",
            "Tenglamalarni faqat qoʻshish bilan yechib boʻlmaydi",
        ],
        "correct": "Ikkala tenglama bir xil maʼlumot beradi",
        "explanation": "<p><strong>Ikkala tenglama bir xil maʼlumot beradi.</strong> "
                       "Ikkalasi ham x + y = 30 ga aylanadi — bu bitta jumlaning "
                       "ikki xil aytilishi. Ayirsak 0 = 0 chiqadi, yaʼni cheksiz "
                       "koʻp yechim (PM-52). Ikkinchi tenglama matnning "
                       "<strong>boshqa</strong> jumlasidan olinishi kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki velosipedchi bir-biriga "
                "qarab yurib, 4 soatda uchrashdi. Ular orasidagi masofa 320 km edi."
                "</p><p><strong>Tezliklarining yigʻindisi qancha?</strong></p>",
        "choices": ["40 km/soat", "80 km/soat", "160 km/soat", "320 km/soat"],
        "correct": "80 km/soat",
        "explanation": "<p><strong>80 km/soat.</strong> Bir-biriga qarab yurganda "
                       "ular birgalikda butun masofani bosadi: har soatda "
                       "320 ÷ 4 = 80 km yaqinlashadi — bu ikki tezlikning "
                       "yigʻindisi. <strong>40 km/soat</strong> — yigʻindini yana "
                       "ikkiga boʻlish kerak deb oʻylaganda chiqadi; ikkiga boʻlish "
                       "faqat tezliklar teng boʻlganda bitta tezlikni beradi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Masala: qizlar oʻgʻillardan 4 ta koʻp, "
                "jami 28 oʻquvchi.</p><p><strong>Yechim: q = 4oʻ va q + oʻ = 28, "
                "demak 5oʻ = 28.</strong></p>",
        "choices": [
            "Birinchi tenglama notoʻgʻri: q = oʻ + 4 boʻlishi kerak",
            "Ikkinchi tenglama notoʻgʻri: q − oʻ = 28 boʻlishi kerak",
            "Oʻrniga qoʻyish notoʻgʻri bajarilgan",
            "Xato yoʻq, yechim davom ettirilishi kerak",
        ],
        "correct": "Birinchi tenglama notoʻgʻri: q = oʻ + 4 boʻlishi kerak",
        "explanation": "<p><strong>Birinchi tenglama notoʻgʻri.</strong> «4 "
                       "<strong>ta</strong> koʻp» — qoʻshish: q = oʻ + 4, "
                       "koʻpaytirish emas. Toʻgʻri yechim: (oʻ + 4) + oʻ = 28, "
                       "2oʻ = 24, oʻ = 12 va q = 16. Tekshirish: 16 + 12 = 28 ✓ "
                       "va 16 − 12 = 4 ✓</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Masala: 12 ta chipta olindi, katta "
                "15 000 soʻmdan, bola 7 000 soʻmdan, jami 140 000 soʻm.</p>"
                "<p><strong>Yechim: 15 000k + 7 000b = 12 va k + b = 140 000."
                "</strong></p>",
        "choices": [
            "Ikki tenglamaning oʻng tomonlari almashib ketgan",
            "Narxlar notoʻgʻri yozilgan",
            "Nomaʼlumlar soni yetarli emas",
            "Xato yoʻq, faqat yechish qoldi",
        ],
        "correct": "Ikki tenglamaning oʻng tomonlari almashib ketgan",
        "explanation": "<p><strong>Oʻng tomonlar almashib ketgan.</strong> "
                       "Toʻgʻrisi: k + b = <strong>12</strong> (soni) va "
                       "15 000k + 7 000b = <strong>140 000</strong> (puli). "
                       "Yozilgani boʻyicha 12 ta chipta 140 000 soʻmga teng boʻlib "
                       "qolyapti. Har bir tenglamada ikkala tomonning birligi bir "
                       "xil boʻlishi shart.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Kassada 5 000 soʻmlik va 10 000 soʻmlik banknotlar bor. "
                "Jami 24 ta banknot va ularning umumiy qiymati 175 000 soʻm.</p>"
                "<p><strong>Nechta 5 000 soʻmlik banknot bor?</strong></p>",
        "choices": ["9 ta", "11 ta", "13 ta", "15 ta"],
        "correct": "13 ta",
        "explanation": "<p><strong>13 ta.</strong> b + o = 24 va 5 000b + 10 000o "
                       "= 175 000. o = 24 − b ni qoʻysak: 5 000b + 240 000 − "
                       "10 000b = 175 000, demak 5 000b = 65 000 va b = 13. "
                       "10 000 soʻmliklar 11 ta. Tekshirish: 13 × 5 000 + "
                       "11 × 10 000 = 65 000 + 110 000 = 175 000 ✓</p>",
    },
    {
        "text": "<p>Ikki velosipedchi orasidagi masofa 45 km edi. Ular bir-biriga "
                "qarab yoʻlga chiqdi va 1,5 soatdan keyin uchrashdi. Birining "
                "tezligi ikkinchisinikidan 4 km/soat ortiq.</p>"
                "<p><strong>Sekinroq velosipedchining tezligi qancha?</strong></p>",
        "choices": ["11 km/soat", "13 km/soat", "15 km/soat", "17 km/soat"],
        "correct": "13 km/soat",
        "explanation": "<p><strong>13 km/soat.</strong> Har soatda ular birgalikda "
                       "45 ÷ 1,5 = 30 km yaqinlashadi, demak v₁ + v₂ = 30 va "
                       "v₁ − v₂ = 4. Qoʻshamiz: 2v₁ = 34, v₁ = 17, keyin "
                       "v₂ = 30 − 17 = 13. Tekshirish: (17 + 13) × 1,5 = 45 ✓ "
                       "<strong>17 km/soat</strong> — bu tezrogʻining tezligi.</p>",
    },
]


# =====================================================================
# PM-56 — parabola bilan tanishuv: y = x²
# =====================================================================

Q_PM56 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>y = x<sup>2</sup> boʻlsa, x = 4 da y "
                "qancha?</strong></p>",
        "choices": ["8", "16", "24", "42"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> 4<sup>2</sup> = 4 × 4 = 16. "
                       "<strong>8</strong> — kvadrat oʻrniga 2 ga koʻpaytirilgan "
                       "(4 × 2); daraja koʻpaytirishning qisqa yozuvi, lekin "
                       "asosga koʻpaytirish emas (PM-12).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = x<sup>2</sup> boʻlsa, x = −6 da y "
                "qancha?</strong></p>",
        "choices": ["−36", "−12", "12", "36"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> (−6)<sup>2</sup> = (−6) × (−6) "
                       "= 36. Manfiy son manfiyga koʻpaysa musbat chiqadi (PM-11). "
                       "<strong>−36</strong> — minus kvadratdan tashqarida "
                       "qoldirilganda chiqadi, yaʼni −6<sup>2</sup>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x<sup>2</sup> "
                "funksiyasining grafigi qanday ataladi?</strong></p>",
        "choices": ["Parabola", "Toʻgʻri chiziq", "Aylana", "Giperbola"],
        "correct": "Parabola",
        "explanation": "<p><strong>Parabola.</strong> Bu — kursdagi birinchi "
                       "toʻgʻri chiziq boʻlmagan grafik. Toʻgʻri chiziq faqat "
                       "y = kx + b da chiqadi (PM-49), chunki u yerda oʻsish har "
                       "doim bir xil; y = x<sup>2</sup> da esa oʻsish ham oʻsib "
                       "boradi, shuning uchun chiziq egiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x<sup>2</sup> "
                "parabolasining uchi qaysi nuqtada?</strong></p>",
        "choices": ["(0; 0)", "(0; 1)", "(1; 1)", "(1; 0)"],
        "correct": "(0; 0)",
        "explanation": "<p><strong>(0; 0).</strong> x = 0 da y = 0<sup>2</sup> = 0 "
                       "— bu parabolaning eng past nuqtasi, egri chiziq shu yerda "
                       "burilib yana koʻtariladi. Uchi bir vaqtda simmetriya "
                       "oʻqining ham ustida turadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x<sup>2</sup> "
                "grafigida y hech qachon qanday boʻlmaydi?</strong></p>",
        "choices": ["Manfiy", "Nolga teng", "Butun son", "1 dan katta"],
        "correct": "Manfiy",
        "explanation": "<p><strong>Manfiy boʻlmaydi.</strong> Har qanday sonning "
                       "kvadrati musbat yoki nol: 3<sup>2</sup> = 9, "
                       "(−3)<sup>2</sup> = 9, 0<sup>2</sup> = 0. Shuning uchun "
                       "grafik x oʻqidan pastga hech qachon tushmaydi — u faqat "
                       "(0; 0) da unga tegadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>(−7)<sup>2</sup> = ?</strong></p>",
        "choices": ["−49", "−14", "14", "49"],
        "correct": "49",
        "explanation": "<p><strong>49.</strong> (−7) × (−7) = 49: ikki manfiy "
                       "koʻpaytuvchi musbat beradi. Qavs muhim — (−7)<sup>2</sup> "
                       "bilan −7<sup>2</sup> ikki xil narsa, ikkinchisi −49 ga "
                       "teng.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = x<sup>2</sup> + 5 boʻlsa, x = 3 da "
                "y qancha?</strong></p>",
        "choices": ["11", "14", "16", "64"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> Avval kvadrat: 3<sup>2</sup> = 9, "
                       "keyin qoʻshish: 9 + 5 = 14 (amallar tartibi, PM-5). "
                       "<strong>64</strong> — avval 3 + 5 = 8 qilinib, keyin "
                       "kvadratga koʻtarilganda chiqadi; bu amallar tartibining "
                       "buzilishi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = −x<sup>2</sup> boʻlsa, x = 4 da y "
                "qancha?</strong></p>",
        "choices": ["−16", "−8", "8", "16"],
        "correct": "−16",
        "explanation": "<p><strong>−16.</strong> Avval 4<sup>2</sup> = 16 "
                       "hisoblanadi, keyin minus qoʻyiladi: −16. y = −x<sup>2</sup> "
                       "grafigining tarmoqlari pastga qaraydi va bitta ham musbat y "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x<sup>2</sup> "
                "grafigida y = 64 boʻlgan nuqtalar qaysilar?</strong></p>",
        "choices": [
            "Faqat (8; 64)",
            "(8; 64) va (−8; 64)",
            "Faqat (32; 64)",
            "(64; 8) va (64; −8)",
        ],
        "correct": "(8; 64) va (−8; 64)",
        "explanation": "<p><strong>(8; 64) va (−8; 64).</strong> 8<sup>2</sup> = 64 "
                       "va (−8)<sup>2</sup> = 64. Parabola simmetrik boʻlgani uchun "
                       "har bir musbat y ga <strong>ikkita</strong> x toʻgʻri "
                       "keladi. Faqat uchida — y = 0 da — bitta x boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x<sup>2</sup> − 2 "
                "parabolasining uchi qayerda?</strong></p>",
        "choices": ["(0; −2)", "(0; 2)", "(−2; 0)", "(2; 0)"],
        "correct": "(0; −2)",
        "explanation": "<p><strong>(0; −2).</strong> Har bir y dan 2 ayrildi, demak "
                       "butun grafik 2 birlik <strong>pastga</strong> koʻchdi. "
                       "Shakli oʻzgarmaydi, faqat oʻrni oʻzgaradi — bu PM-50 dagi "
                       "b ning aynan oʻzi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = x<sup>2</sup> da x = 3 dan x = 4 "
                "ga oʻtganda y qanchaga oʻsadi?</strong></p>",
        "choices": ["1 ga", "5 ga", "7 ga", "12 ga"],
        "correct": "7 ga",
        "explanation": "<p><strong>7 ga.</strong> 3<sup>2</sup> = 9 va "
                       "4<sup>2</sup> = 16, farqi 16 − 9 = 7. Toʻgʻri chiziqda bu "
                       "oʻsish har doim bir xil boʻlardi; parabolada esa oʻsishlar "
                       "1, 3, 5, 7 — tobora kattalashadi, shuning uchun chiziq "
                       "tikroq boʻlib boradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = 2x<sup>2</sup> boʻlsa, x = 3 da y "
                "qancha?</strong></p>",
        "choices": ["12", "18", "36", "81"],
        "correct": "18",
        "explanation": "<p><strong>18.</strong> Avval kvadrat, keyin koʻpaytirish: "
                       "3<sup>2</sup> = 9, keyin 2 × 9 = 18. <strong>36</strong> — "
                       "avval 2 × 3 = 6 qilinib, keyin kvadratga koʻtarilganda "
                       "chiqadi (6<sup>2</sup> = 36); amallar tartibi buzilgan.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>x = 5 da y = 2x va "
                "y = x<sup>2</sup> dan qaysi biri katta qiymat beradi?</strong></p>",
        "choices": [
            "y = x² katta: 25 > 10",
            "y = 2x katta: 10 > 25",
            "Ikkalasi teng: 10 = 10",
            "Taqqoslab boʻlmaydi",
        ],
        "correct": "y = x² katta: 25 > 10",
        "explanation": "<p><strong>y = x<sup>2</sup> katta.</strong> 5<sup>2</sup> "
                       "= 25, 2 × 5 = 10. Kichik x larda chiziq oldinda boradi "
                       "(x = 1 da 2 > 1), lekin parabola tezroq oʻsib, uni albatta "
                       "quvib oʻtadi. Kvadrat oʻsish har doim chiziqli oʻsishdan "
                       "ustun keladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x<sup>2</sup> va "
                "y = −x<sup>2</sup> grafiklari nimasi bilan farq qiladi?</strong></p>",
        "choices": [
            "Tarmoqlari qarama-qarshi tomonga qaraydi",
            "Uchlari har xil nuqtada boʻladi",
            "Biri parabola, ikkinchisi toʻgʻri chiziq",
            "Biri simmetrik, ikkinchisi emas",
        ],
        "correct": "Tarmoqlari qarama-qarshi tomonga qaraydi",
        "explanation": "<p><strong>Tarmoqlari qarama-qarshi tomonga qaraydi.</strong> "
                       "y = x<sup>2</sup> da yuqoriga, y = −x<sup>2</sup> da "
                       "pastga. Uchi ikkalasida ham (0; 0) da qoladi va ikkalasi "
                       "ham y oʻqiga nisbatan simmetrik — faqat biri x oʻqi boʻylab "
                       "agʻdarilgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>(−5)<sup>2</sup> va "
                "−5<sup>2</sup> qanday qiymatlarga teng?</strong></p>",
        "choices": [
            "25 va −25",
            "25 va 25",
            "−25 va −25",
            "−25 va 25",
        ],
        "correct": "25 va −25",
        "explanation": "<p><strong>25 va −25.</strong> Qavs bor boʻlsa butun "
                       "(−5) kvadratga koʻtariladi: (−5) × (−5) = 25. Qavs boʻlmasa "
                       "avval 5<sup>2</sup> = 25 hisoblanadi va minus keyin "
                       "qoʻyiladi: −25. Bitta qavs javobning ishorasini "
                       "oʻzgartiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x<sup>2</sup> + 3 "
                "grafigi y = x<sup>2</sup> grafigidan qanday farq qiladi?</strong></p>",
        "choices": [
            "3 birlik yuqoriga koʻchgan",
            "3 birlik pastga koʻchgan",
            "3 marta tor boʻlgan",
            "Tarmoqlari pastga qaragan",
        ],
        "correct": "3 birlik yuqoriga koʻchgan",
        "explanation": "<p><strong>3 birlik yuqoriga koʻchgan.</strong> Har bir y "
                       "ga 3 qoʻshildi, demak har bir nuqta 3 birlik tepaga siljidi "
                       "va uchi (0; 3) ga koʻchdi. Shakli oʻzgarmaydi: qoʻshimcha "
                       "son grafikni <strong>koʻtaradi</strong>, torlashtirmaydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>Oʻquvchi (−3)<sup>2</sup> = −9 "
                "deb yozdi.</strong></p>",
        "choices": [
            "Manfiy son kvadratga koʻtarilganda musbat boʻladi: javob 9",
            "Kvadrat oʻrniga 2 ga koʻpaytirish kerak edi: javob −6",
            "Xato yoʻq, javob toʻgʻri",
            "Qavsni ochish kerak edi: javob −6",
        ],
        "correct": "Manfiy son kvadratga koʻtarilganda musbat boʻladi: javob 9",
        "explanation": "<p><strong>Javob 9.</strong> (−3)<sup>2</sup> = (−3) × "
                       "(−3) = 9 — ikki manfiy koʻpaytuvchi musbat beradi (PM-11). "
                       "Aynan shuning uchun y = x<sup>2</sup> grafigi x oʻqidan "
                       "pastga tushmaydi. −9 javobi faqat qavssiz −3<sup>2</sup> "
                       "yozuvida toʻgʻri boʻlardi.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>Oʻquvchi y = x<sup>2</sup> "
                "grafigini chizish uchun (1; 1) va (2; 4) nuqtalarini qoʻydi va "
                "ularni chizgʻich bilan tutashtirdi.</strong></p>",
        "choices": [
            "y = x² grafigi egri chiziq — kamida 5 nuqta kerak",
            "Nuqtalar notoʻgʻri hisoblangan",
            "Chizishdan oldin uchini topish shart edi",
            "Xato yoʻq, ikki nuqta yetarli",
        ],
        "correct": "y = x² grafigi egri chiziq — kamida 5 nuqta kerak",
        "explanation": "<p><strong>y = x<sup>2</sup> grafigi egri chiziq.</strong> "
                       "Nuqtalar toʻgʻri hisoblangan (1<sup>2</sup> = 1, "
                       "2<sup>2</sup> = 4), lekin ikki nuqta faqat toʻgʻri chiziq "
                       "uchun yetarli (PM-49). Parabola uchun uchidan ikki tomonga "
                       "kamida beshta nuqta qoʻyib, ularni silliq tutashtirish "
                       "kerak.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Haydovchilik qoidalarida taxminiy qoida bor: mashinaning tormoz "
                "yoʻli metrda s = (v ÷ 10)<sup>2</sup> ga teng, bunda v — "
                "km/soatdagi tezlik.</p><p><strong>60 km/soat tezlikda tormoz yoʻli "
                "qancha boʻladi?</strong></p>",
        "choices": ["6 metr", "12 metr", "36 metr", "60 metr"],
        "correct": "36 metr",
        "explanation": "<p><strong>36 metr.</strong> Avval 60 ÷ 10 = 6, keyin "
                       "6<sup>2</sup> = 36. <strong>6 metr</strong> — kvadratga "
                       "koʻtarish unutilgan; <strong>12 metr</strong> — kvadrat "
                       "oʻrniga 2 ga koʻpaytirilgan. Tekshirish: 40 km/soatda "
                       "4<sup>2</sup> = 16 m, demak 60 da undan koʻproq "
                       "chiqishi kerak ✓</p>",
    },
    {
        "text": "<p>Kvadrat shaklidagi hovlining tomoni 8 metr edi. Egasi hovlini "
                "kengaytirib, tomonini 16 metr qildi.</p><p><strong>Hovlining "
                "yuzasi necha marta ortdi?</strong></p>",
        "choices": ["2 marta", "4 marta", "8 marta", "16 marta"],
        "correct": "4 marta",
        "explanation": "<p><strong>4 marta.</strong> Kvadratning yuzasi tomonining "
                       "kvadratiga teng: 8<sup>2</sup> = 64 va 16<sup>2</sup> "
                       "= 256, demak 256 ÷ 64 = 4. <strong>2 marta</strong> — eng "
                       "koʻp uchraydigan xato: tomon 2 marta ortgani yuza ham "
                       "2 marta ortadi degani emas. Tomon 2 marta ortsa, yuza "
                       "2 × 2 = 4 marta ortadi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-54 Mashq: Sistema: qoʻshish usuli",
        "description": "20 savol — qoʻshish va ayirish, tenglamani koʻpaytirish, "
                       "ikki maxsus hol va ikki chekli matnli masalalar.",
        "tutorial":    "PM-54:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM54,
    },
    {
        "title":       "PM-55 Mashq: Sistemali matnli masalalar",
        "description": "20 savol — jumlani tenglamaga aylantirish, soni va puli, "
                       "yosh, qarama-qarshi harakat va javobni matnga qaytarish.",
        "tutorial":    "PM-55:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM55,
    },
    {
        "title":       "PM-56 Mashq: Parabola bilan tanishuv",
        "description": "20 savol — y = x² jadvali, uchi va simmetriya, "
                       "y = x² + c va y = −x², kvadrat oʻsishning tezligi.",
        "tutorial":    "PM-56:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM56,
    },
]
