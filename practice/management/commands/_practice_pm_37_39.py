# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-37 … PM-39 (ikki tomonli tenglama, matnli masala 1-2).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ PM-38 va PM-39 butunlay matnli masalalarga bagʻishlangan darslar, shuning
   uchun ularda «matnli masala» ulushi 19–20 dan koʻp — bu ataylab shunday.
⚠️ `choices` EKRANLANADI — HTML teg yoʻq.
⚠️ Kumulyativ: tengsizlik (PM-40) va modul (PM-41) yoʻq; ikki nomaʼlumli
   sistemalar ham yoʻq — hamma masala bitta harf bilan yechiladi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_37_39.py --master=prime \\
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
# PM-37 — ikki tomonida ham nomaʼlumi bor tenglamalar
# =====================================================================

Q_PM37 = [
    # 1–5 tanish
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>5x = 2x + 12</strong></p>",
        "choices": ["x = 3", "x = 4", "x = 7", "x = 12"],
        "correct": "x = 4",
        "explanation": "<p><strong>x = 4.</strong> Ikki tomondan 2x ni ayiramiz: "
                       "3x = 12. Tekshirish: 5 × 4 = 20 va 2 × 4 + 12 = 20 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>4x = x + 9</strong></p>",
        "choices": ["x = 3", "x = 5", "x = 9", "x = 12"],
        "correct": "x = 3",
        "explanation": "<p><strong>x = 3.</strong> 4x − x = 3x, demak 3x = 9. "
                       "Tekshirish: 12 = 3 + 9 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>3x + 2 = 2x + 7</strong></p>",
        "choices": ["x = 2", "x = 5", "x = 7", "x = 9"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> Ikki tomondan 2x ni ayiramiz: "
                       "x + 2 = 7. Tekshirish: 17 = 17 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>6x − 4 = 4x + 6</strong></p>",
        "choices": ["x = 1", "x = 5", "x = 10", "x = 20"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> 2x − 4 = 6 → 2x = 10. "
                       "Tekshirish: 26 = 26 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>7x = 3x + 20 tenglamasi "
                "berilgan.</p><p><strong>Birinchi qadam qanday boʻladi?</strong></p>",
        "choices": [
            "Ikki tomondan 3x ni ayirish",
            "Ikki tomonga 3x ni qoʻshish",
            "Ikki tomonni 7 ga boʻlish",
            "Ikki tomondan 20 ni ayirish",
        ],
        "correct": "Ikki tomondan 3x ni ayirish",
        "explanation": "<p><strong>3x ni ayirish.</strong> Shunda harfli hadlar bir "
                       "tomonga yigʻiladi: 4x = 20 va x = 5. Qoʻshish 3x ni "
                       "yoʻqotmaydi, faqat koʻpaytiradi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>4x + 3 = 2x + 11</strong></p>",
        "choices": ["x = 2", "x = 4", "x = 7", "x = 14"],
        "correct": "x = 4",
        "explanation": "<p><strong>x = 4.</strong> 2x + 3 = 11 → 2x = 8. "
                       "Tekshirish: 19 = 19 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>7x − 5 = 3x + 7</strong></p>",
        "choices": ["x = 2", "x = 3", "x = 4", "x = 12"],
        "correct": "x = 3",
        "explanation": "<p><strong>x = 3.</strong> 4x − 5 = 7 → 4x = 12. "
                       "Tekshirish: 21 − 5 = 16 va 9 + 7 = 16 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>5x + 1 = 2x + 16</strong></p>",
        "choices": ["x = 3", "x = 5", "x = 15", "x = 17"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> 3x + 1 = 16 → 3x = 15. "
                       "Tekshirish: 26 = 26 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>8x − 3 = 5x + 9</strong></p>",
        "choices": ["x = 2", "x = 4", "x = 6", "x = 12"],
        "correct": "x = 4",
        "explanation": "<p><strong>x = 4.</strong> 3x − 3 = 9 → 3x = 12. "
                       "Tekshirish: 32 − 3 = 29 va 20 + 9 = 29 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>2x + 9 = 5x</strong></p>",
        "choices": ["x = 3", "x = 4,5", "x = 9", "x = 11"],
        "correct": "x = 3",
        "explanation": "<p><strong>x = 3.</strong> Nomaʼlum oʻng tomonda koʻproq: "
                       "ikki tomondan 2x ni ayiramiz va 9 = 3x chiqadi. "
                       "Tekshirish: 6 + 9 = 15 va 5 × 3 = 15 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>3(x + 2) = x + 10</strong></p>",
        "choices": ["x = 2", "x = 4", "x = 6", "x = 8"],
        "correct": "x = 2",
        "explanation": "<p><strong>x = 2.</strong> Avval qavsni ochamiz: "
                       "3x + 6 = x + 10; keyin 2x = 4. Tekshirish: "
                       "3 × 4 = 12 va 2 + 10 = 12 ✓</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>4(x − 1) = 2x + 6</strong></p>",
        "choices": ["x = 2", "x = 3", "x = 5", "x = 10"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> 4x − 4 = 2x + 6 → 2x = 10. "
                       "Tekshirish: 4 × 4 = 16 va 10 + 6 = 16 ✓</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2x + 5 = 2x + 9 "
                "tenglamasining yechimi nechta?</strong></p>",
        "choices": [
            "Yechimi yoʻq",
            "Bitta yechim: x = 2",
            "Bitta yechim: x = 4",
            "Har qanday son yechim",
        ],
        "correct": "Yechimi yoʻq",
        "explanation": "<p><strong>Yechimi yoʻq.</strong> Ikki tomondan 2x ni "
                       "ayirsak, 5 = 9 degan yolgʻon tenglik qoladi. Hech qanday "
                       "son bu tenglamani rost qilmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3x + 6 = 3(x + 2) "
                "tenglamasi haqida nima deyish mumkin?</strong></p>",
        "choices": [
            "Yechimi yoʻq",
            "Faqat x = 0 yechim",
            "Har qanday son yechim — bu ayniyat",
            "Faqat x = 2 yechim",
        ],
        "correct": "Har qanday son yechim — bu ayniyat",
        "explanation": "<p><strong>Ayniyat.</strong> Qavsni ochsak, ikkala tomon "
                       "ham 3x + 6 boʻlib chiqadi: 6 = 6 — har doim rost. Istalgan "
                       "x toʻgʻri keladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>x + 12 = 5x va 5x = x + 12 "
                "tenglamalari qanday?</strong></p>",
        "choices": [
            "Bir xil — ikkalasining yechimi x = 3",
            "Har xil — birinchisining yechimi 3, ikkinchisiniki 4",
            "Birinchisining yechimi yoʻq",
            "Ikkalasining ham yechimi 12",
        ],
        "correct": "Bir xil — ikkalasining yechimi x = 3",
        "explanation": "<p><strong>Bir xil.</strong> Tenglikning ikki tomonini "
                       "almashtirish uni oʻzgartirmaydi: 4x = 12 va x = 3. "
                       "Nomaʼlum qaysi tomonda turishi ahamiyatsiz.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi tenglamaning yechimi "
                "x = 6?</strong></p>",
        "choices": ["3x = 2x + 5", "4x − 2 = 2x + 10", "5x = 3x + 6", "x + 6 = 2x + 3"],
        "correct": "4x − 2 = 2x + 10",
        "explanation": "<p><strong>4x − 2 = 2x + 10.</strong> 2x = 12 → x = 6. "
                       "Tekshirish: 22 = 22 ✓ Qolganlarining yechimlari 5, 3 va 3.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>5x = 2x + 12 → "
                "5x + 2x = 12 → 7x = 12</strong></p>",
        "choices": [
            "2x ni yoʻqotish uchun uni ayirish kerak: 3x = 12",
            "Ikki tomonni 5 ga boʻlish kerak edi",
            "12 ni chap tomonga oʻtkazish kerak edi",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "2x ni yoʻqotish uchun uni ayirish kerak: 3x = 12",
        "explanation": "<p><strong>3x = 12, x = 4.</strong> Qoʻshish 2x ni "
                       "yoʻqotmaydi. Tekshirish: 7x = 12 dan chiqqan javob "
                       "tenglamani rost qilmaydi.</p>",
    },
    {
        "text": "<p>Qaysi qadam toʻgʻri?</p><p><strong>3(x + 2) = x + 10</strong></p>",
        "choices": [
            "3x + 2 = x + 10",
            "3x + 6 = x + 10",
            "3x + 2 = 3x + 30",
            "x + 2 = x + 10",
        ],
        "correct": "3x + 6 = x + 10",
        "explanation": "<p><strong>3x + 6 = x + 10.</strong> Qavs ochilganda "
                       "koʻpaytuvchi ikkala hadga ham tarqaladi (PM-33): "
                       "3 × 2 = 6, 2 emas.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>«Olimp» klubi 100 000 soʻm abonent va har mashgʻulot uchun 15 000 "
                "soʻm oladi. «Chempion» klubida abonent 40 000 soʻm, har mashgʻulot "
                "esa 20 000 soʻm.</p><p><strong>Necha marta borganda toʻlovlar "
                "tenglashadi?</strong></p>",
        "choices": ["8 marta", "10 marta", "12 marta", "15 marta"],
        "correct": "12 marta",
        "explanation": "<p><strong>12 marta.</strong> 100 000 + 15 000n = "
                       "40 000 + 20 000n → 60 000 = 5000n → n = 12. Tekshirish: "
                       "ikkala klubda ham 280 000 soʻm ✓</p>",
    },
    {
        "text": "<p>Bir taksi 10 000 soʻm oʻtirish haqi va har kilometr uchun 4000 "
                "soʻm oladi. Ikkinchisi 25 000 soʻm oʻtirish haqi va har kilometr "
                "uchun 1000 soʻm.</p><p><strong>Necha kilometrda narxlar "
                "tenglashadi?</strong></p>",
        "choices": ["3 km", "5 km", "7 km", "15 km"],
        "correct": "5 km",
        "explanation": "<p><strong>5 km.</strong> 10 000 + 4000k = 25 000 + 1000k → "
                       "3000k = 15 000 → k = 5. Ikkalasida ham 30 000 soʻm. Undan "
                       "qisqa yoʻlda birinchisi, uzunroqda ikkinchisi arzon.</p>",
    },
]


# =====================================================================
# PM-38 — matnli masalani tenglama bilan yechish 1
# =====================================================================

Q_PM38 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Afsona x ta olma yigʻdi, Jasur "
                "undan 12 ta koʻp yigʻdi.</p><p><strong>Jasur yigʻgani qanday "
                "yoziladi?</strong></p>",
        "choices": ["x + 12", "12x", "x − 12", "12 − x"],
        "correct": "x + 12",
        "explanation": "<p><strong>x + 12.</strong> «12 ta koʻp» — qoʻshish. "
                       "<strong>12x</strong> «12 marta koʻp» degani boʻlar edi "
                       "(PM-30).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Afsona x ta yigʻdi, Jasur undan "
                "3 marta koʻp yigʻdi.</p><p><strong>Jasur yigʻgani qanday "
                "yoziladi?</strong></p>",
        "choices": ["x + 3", "3x", "x/3", "x − 3"],
        "correct": "3x",
        "explanation": "<p><strong>3x.</strong> «Marta» soʻzi koʻpaytirishni "
                       "bildiradi.</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p>Afsona x ta, Jasur x + 12 ta yigʻdi.</p>"
                "<p><strong>Ikkalasi jami qancha yigʻdi?</strong></p>",
        "choices": ["2x + 12", "x + 12", "12x", "2x"],
        "correct": "2x + 12",
        "explanation": "<p><strong>2x + 12.</strong> x + (x + 12) = 2x + 12 — "
                       "oʻxshash hadlar qoʻshildi (PM-32).</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>x + (x + 12) = 60</strong></p>",
        "choices": ["x = 12", "x = 24", "x = 36", "x = 48"],
        "correct": "x = 24",
        "explanation": "<p><strong>x = 24.</strong> 2x + 12 = 60 → 2x = 48. "
                       "Bu — Afsonaning soni.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Afsona 24 ta yigʻdi, Jasur undan 12 ta "
                "koʻp.</p><p><strong>Jasur nechta yigʻdi?</strong></p>",
        "choices": ["12 ta", "24 ta", "36 ta", "60 ta"],
        "correct": "36 ta",
        "explanation": "<p><strong>36 ta.</strong> 24 + 12 = 36. Bu — matnli "
                       "masalaning oxirgi qadami: x ni topgach, savolda "
                       "soʻralgan miqdorga qaytish.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Masalani yeching.</p><p>Ikki sonning yigʻindisi 50, biri "
                "ikkinchisidan 8 taga katta.</p><p><strong>Kichik son "
                "nechchi?</strong></p>",
        "choices": ["17", "21", "25", "29"],
        "correct": "21",
        "explanation": "<p><strong>21.</strong> x + (x + 8) = 50 → 2x = 42 → "
                       "x = 21. Kattasi 29. Tekshirish: 21 + 29 = 50 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sherbek Bekzoddan 2 marta koʻp kitob "
                "oʻqidi, ikkalasi birga 27 ta oʻqidi.</p><p><strong>Sherbek nechta "
                "oʻqigan?</strong></p>",
        "choices": ["9 ta", "13 ta", "18 ta", "27 ta"],
        "correct": "18 ta",
        "explanation": "<p><strong>18 ta.</strong> Bekzod x, Sherbek 2x: "
                       "3x = 27 → x = 9. Sherbek 2 × 9 = 18. <strong>9</strong> — "
                       "Bekzodniki; savol Sherbek haqida edi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sinfda qizlar oʻgʻillardan 4 taga koʻp, "
                "jami 28 oʻquvchi bor.</p><p><strong>Nechta oʻgʻil bola "
                "bor?</strong></p>",
        "choices": ["10 ta", "12 ta", "14 ta", "16 ta"],
        "correct": "12 ta",
        "explanation": "<p><strong>12 ta.</strong> 2x + 4 = 28 → 2x = 24 → x = 12. "
                       "Qizlar 16 ta. Tekshirish: 12 + 16 = 28 va farq 4 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Daftar qalamdan 3000 soʻm qimmat, "
                "ikkalasi birga 17 000 soʻm.</p><p><strong>Daftar necha "
                "soʻm?</strong></p>",
        "choices": ["7000 soʻm", "8500 soʻm", "10 000 soʻm", "14 000 soʻm"],
        "correct": "10 000 soʻm",
        "explanation": "<p><strong>10 000 soʻm.</strong> Qalam x: "
                       "2x + 3000 = 17 000 → x = 7000; daftar 7000 + 3000 = "
                       "10 000. <strong>7000</strong> — qalamning narxi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Kitobda 120 bet bor. Oʻqilmagan qismi "
                "oʻqilganidan 3 marta koʻp.</p><p><strong>Necha bet "
                "oʻqilgan?</strong></p>",
        "choices": ["30 bet", "40 bet", "60 bet", "90 bet"],
        "correct": "30 bet",
        "explanation": "<p><strong>30 bet.</strong> Oʻqilgani x, qolgani 3x: "
                       "4x = 120 → x = 30. Qolgani 90 bet. Tekshirish: "
                       "30 + 90 = 120 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki sonning yigʻindisi 84, biri "
                "ikkinchisidan 6 marta katta.</p><p><strong>Katta son "
                "nechchi?</strong></p>",
        "choices": ["12", "14", "70", "72"],
        "correct": "72",
        "explanation": "<p><strong>72.</strong> Kichigi x, kattasi 6x: 7x = 84 → "
                       "x = 12; kattasi 6 × 12 = 72. Tekshirish: 12 + 72 = 84 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki qutida jami 45 ta qalam bor, "
                "birinchisida ikkinchisidan 9 taga koʻp.</p><p><strong>Birinchi "
                "qutida nechta?</strong></p>",
        "choices": ["18 ta", "22 ta", "27 ta", "36 ta"],
        "correct": "27 ta",
        "explanation": "<p><strong>27 ta.</strong> Ikkinchisi x: 2x + 9 = 45 → "
                       "x = 18; birinchisi 18 + 9 = 27. Tekshirish: "
                       "27 + 18 = 45 ✓</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Jasur Afsonadan 12 ta koʻp "
                "yigʻdi, jami 60 ta».</p><p><strong>Qaysi tenglama "
                "toʻgʻri?</strong></p>",
        "choices": [
            "x + 12x = 60",
            "x + (x + 12) = 60",
            "x − (x + 12) = 60",
            "12(x + x) = 60",
        ],
        "correct": "x + (x + 12) = 60",
        "explanation": "<p><strong>x + (x + 12) = 60.</strong> «12 ta koʻp» — "
                       "qoʻshish, «12 marta koʻp» esa koʻpaytirish boʻlardi. "
                       "Bitta soʻz tenglamani butunlay oʻzgartiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Matnli masalada nima "
                "uchun ikkinchi harf (y) kiritilmaydi?</strong></p>",
        "choices": [
            "Ikki harfli tenglamani bitta shart bilan yechib boʻlmaydi",
            "Ikkinchi harf yozish taqiqlangan",
            "y harfi faqat geometriyada ishlatiladi",
            "Ikki harf javobni ikki barobar qiladi",
        ],
        "correct": "Ikki harfli tenglamani bitta shart bilan yechib boʻlmaydi",
        "explanation": "<p><strong>Bitta shart — bitta harf.</strong> Ikkinchi "
                       "miqdorni birinchisi orqali yozsangiz (x + 12 kabi), "
                       "tenglama yechiladigan boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Masalada x — Afsonaning soni deb "
                "olindi va x = 24 chiqdi. Savol esa Jasur haqida "
                "edi.</p><p><strong>Javob nima?</strong></p>",
        "choices": ["24", "36", "60", "12"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> x ni topish — yechimning oʻrtasi. "
                       "Jasur Afsonadan 12 ta koʻp yigʻgan: 24 + 12 = 36. Savolga "
                       "qaytmaslik — eng koʻp ball yoʻqotiladigan xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Ikki sonning yigʻindisi 40, biri "
                "ikkinchisidan 4 marta katta».</p><p><strong>Qaysi tenglama "
                "toʻgʻri?</strong></p>",
        "choices": ["x + 4 = 40", "x + 4x = 40", "4(x + x) = 40", "x − 4x = 40"],
        "correct": "x + 4x = 40",
        "explanation": "<p><strong>x + 4x = 40.</strong> Kichigi x, kattasi 4x; "
                       "5x = 40 → x = 8, kattasi 32. Tekshirish: 8 + 32 = 40 ✓</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p>«Qizlar oʻgʻillardan 4 taga koʻp, "
                "jami 28».</p><p><strong>Yechim: x + 4x = 28 → 5x = 28</strong></p>",
        "choices": [
            "«4 taga koʻp» qoʻshish: x + (x + 4) = 28",
            "Jami 28 emas, 32 boʻlishi kerak",
            "Ikki harf kiritish kerak edi",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "«4 taga koʻp» qoʻshish: x + (x + 4) = 28",
        "explanation": "<p><strong>x + (x + 4) = 28.</strong> «Taga koʻp» — "
                       "qoʻshish. Notoʻgʻri tenglamadan x = 5,6 chiqadi — oʻquvchi "
                       "soni kasr boʻlolmasligi ham xatoni koʻrsatib turadi.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p>«Bir son ikkinchisidan 3 marta katta, "
                "yigʻindisi 48».</p>",
        "choices": [
            "x + 3 = 48 → x = 45",
            "x + 3x = 48 → x = 12, sonlar 12 va 36",
            "3x = 48 → x = 16, sonlar 16 va 48",
            "x − 3x = 48 → x = −24",
        ],
        "correct": "x + 3x = 48 → x = 12, sonlar 12 va 36",
        "explanation": "<p><strong>12 va 36.</strong> Kichigi x, kattasi 3x, "
                       "yigʻindisi 4x = 48. Tekshirish: 12 + 36 = 48 va "
                       "36 = 3 × 12 ✓</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Ikki sonning yigʻindisi 90 ga teng. Birinchi son ikkinchisidan "
                "14 taga katta.</p><p><strong>Katta son nechchi?</strong></p>",
        "choices": ["38", "45", "52", "76"],
        "correct": "52",
        "explanation": "<p><strong>52.</strong> Kichigi x: x + (x + 14) = 90 → "
                       "2x = 76 → x = 38; kattasi 38 + 14 = 52. Tekshirish: "
                       "38 + 52 = 90 va 52 − 38 = 14 ✓</p>",
    },
    {
        "text": "<p>Bogʻda olma daraxti nokdan 2 marta koʻp. Jami 54 ta daraxt "
                "bor.</p><p><strong>Nechta olma daraxti bor?</strong></p>",
        "choices": ["18 ta", "27 ta", "36 ta", "45 ta"],
        "correct": "36 ta",
        "explanation": "<p><strong>36 ta.</strong> Nok x, olma 2x: 3x = 54 → "
                       "x = 18; olma 2 × 18 = 36. Tekshirish: 18 + 36 = 54 ✓ "
                       "<strong>18</strong> — nok daraxtlarining soni.</p>",
    },
]


# =====================================================================
# PM-39 — matnli masalani tenglama bilan yechish 2
# =====================================================================

Q_PM39 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Birinchi bogʻcha x ta koʻchat "
                "oldi, ikkinchisi 2 marta koʻp, uchinchisi 15 taga "
                "koʻp.</p><p><strong>Uchinchi bogʻcha qanday yoziladi?</strong></p>",
        "choices": ["15x", "x + 15", "2x + 15", "x/15"],
        "correct": "x + 15",
        "explanation": "<p><strong>x + 15.</strong> «Taga koʻp» — qoʻshish va u "
                       "birinchi bogʻchaga nisbatan aytilgan.</p>",
    },
    {
        "text": "<p>Ixchamlang.</p><p><strong>x + 2x + (x + 15) = ?</strong></p>",
        "choices": ["3x + 15", "4x + 15", "4x + 15x", "3x + 15x"],
        "correct": "4x + 15",
        "explanation": "<p><strong>4x + 15.</strong> Harfli hadlar: "
                       "1 + 2 + 1 = 4; ozod had 15 yolgʻiz qoladi.</p>",
    },
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>4x + 15 = 115</strong></p>",
        "choices": ["x = 20", "x = 25", "x = 30", "x = 32,5"],
        "correct": "x = 25",
        "explanation": "<p><strong>x = 25.</strong> 4x = 100 → x = 25.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki chelakdan biridan "
                "ikkinchisiga 5 litr quyilsa, ular teng boʻladi.</p>"
                "<p><strong>Boshlangʻich farq necha litr edi?</strong></p>",
        "choices": ["2,5 litr", "5 litr", "10 litr", "15 litr"],
        "correct": "10 litr",
        "explanation": "<p><strong>10 litr.</strong> Quyilgan suv bir tomondan "
                       "kamayib, ikkinchisiga qoʻshiladi — demak farq quyilganning "
                       "IKKI barobariga qisqaradi. <strong>5 litr</strong> — bu "
                       "turdagi masaladagi eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Toʻgʻri toʻrtburchakning eni x, "
                "boʻyi undan 5 sm uzun.</p><p><strong>Perimetri qanday "
                "yoziladi?</strong></p>",
        "choices": ["x + (x + 5)", "2(x + x + 5)", "x(x + 5)", "2x + 5"],
        "correct": "2(x + x + 5)",
        "explanation": "<p><strong>2(x + x + 5).</strong> Perimetr — "
                       "P = 2(en + boʻy) (PM-35). <strong>x + (x + 5)</strong> "
                       "faqat yarim perimetrni beradi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Masalani yeching.</p><p>Uch bogʻcha jami 115 ta koʻchat oldi. "
                "Ikkinchisi birinchisidan 2 marta koʻp, uchinchisi birinchisidan "
                "15 taga koʻp.</p><p><strong>Ikkinchi bogʻcha nechta "
                "oldi?</strong></p>",
        "choices": ["25 ta", "40 ta", "50 ta", "75 ta"],
        "correct": "50 ta",
        "explanation": "<p><strong>50 ta.</strong> 4x + 15 = 115 → x = 25; "
                       "ikkinchisi 2 × 25 = 50. Tekshirish: 25 + 50 + 40 = 115 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki chelakda jami 30 litr suv bor. "
                "Birinchisidan ikkinchisiga 5 litr quyilsa, ular teng "
                "boʻladi.</p><p><strong>Birinchi chelakda necha litr "
                "bor?</strong></p>",
        "choices": ["10 litr", "15 litr", "20 litr", "25 litr"],
        "correct": "20 litr",
        "explanation": "<p><strong>20 litr.</strong> Farq 10 litr: "
                       "x + (x + 10) = 30 → x = 10; kattasi 20. Tekshirish: "
                       "20 − 5 = 15 va 10 + 5 = 15 — teng ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Toʻgʻri toʻrtburchakning boʻyi enidan "
                "5 sm uzun, perimetri 46 sm.</p><p><strong>Eni necha "
                "santimetr?</strong></p>",
        "choices": ["9 sm", "11 sm", "14 sm", "18 sm"],
        "correct": "9 sm",
        "explanation": "<p><strong>9 sm.</strong> 2(x + x + 5) = 46 → 2x + 5 = 23 "
                       "→ x = 9; boʻyi 14 sm. Tekshirish: 2(9 + 14) = 46 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Otasi oʻgʻlidan 28 yosh katta, "
                "ikkalasining yoshi yigʻindisi 46.</p><p><strong>Oʻgʻil necha "
                "yoshda?</strong></p>",
        "choices": ["9 yoshda", "18 yoshda", "23 yoshda", "37 yoshda"],
        "correct": "9 yoshda",
        "explanation": "<p><strong>9 yoshda.</strong> x + (x + 28) = 46 → 2x = 18 "
                       "→ x = 9; otasi 37 yoshda. Tekshirish: 9 + 37 = 46 va "
                       "37 − 9 = 28 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki savatda jami 40 ta non bor. "
                "Birinchisidan ikkinchisiga 4 ta olib qoʻyilsa, teng "
                "boʻladi.</p><p><strong>Birinchi savatda nechta non "
                "bor?</strong></p>",
        "choices": ["16 ta", "20 ta", "24 ta", "28 ta"],
        "correct": "24 ta",
        "explanation": "<p><strong>24 ta.</strong> Farq 8 ta: x + (x + 8) = 40 → "
                       "x = 16; kattasi 24. Tekshirish: 24 − 4 = 20 va "
                       "16 + 4 = 20 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Uch doʻst 150 000 soʻm topdi. Jasur "
                "Afsonadan 2 marta koʻp, Sherbek Afsonadan 20 000 soʻm koʻp "
                "oldi.</p><p><strong>Jasur qancha oldi?</strong></p>",
        "choices": ["32 500 soʻm", "52 500 soʻm", "65 000 soʻm", "75 000 soʻm"],
        "correct": "65 000 soʻm",
        "explanation": "<p><strong>65 000 soʻm.</strong> "
                       "x + 2x + (x + 20 000) = 150 000 → 4x = 130 000 → "
                       "x = 32 500; Jasur 2 × 32 500 = 65 000. Tekshirish: "
                       "32 500 + 65 000 + 52 500 = 150 000 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Toʻgʻri toʻrtburchakning boʻyi enidan "
                "3 sm uzun, perimetri 26 sm.</p><p><strong>Boʻyi necha "
                "santimetr?</strong></p>",
        "choices": ["5 sm", "8 sm", "10 sm", "13 sm"],
        "correct": "8 sm",
        "explanation": "<p><strong>8 sm.</strong> 2(x + x + 3) = 26 → 2x + 3 = 13 "
                       "→ x = 5 (eni); boʻyi 5 + 3 = 8 sm. Tekshirish: "
                       "2(5 + 8) = 26 ✓</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki qutidan biridan ikkinchisiga "
                "3 ta olma olib qoʻyilsa, ular teng boʻladi.</p>"
                "<p><strong>Boshlangʻich farq nechta edi?</strong></p>",
        "choices": ["3 ta", "6 ta", "9 ta", "12 ta"],
        "correct": "6 ta",
        "explanation": "<p><strong>6 ta.</strong> Bir tomondan 3 ta kamayadi, "
                       "ikkinchisiga 3 ta qoʻshiladi — farq 6 taga qisqaradi. "
                       "Teng boʻlgani uchun boshlangʻich farq 6 ta boʻlgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Perimetri 46 sm boʻlgan "
                "toʻgʻri toʻrtburchak uchun qaysi tenglama toʻgʻri?</strong></p>",
        "choices": [
            "x + (x + 5) = 46",
            "2(x + x + 5) = 46",
            "x(x + 5) = 46",
            "4x + 5 = 46",
        ],
        "correct": "2(x + x + 5) = 46",
        "explanation": "<p><strong>2(x + x + 5) = 46.</strong> Toʻrtta tomon bor: "
                       "en va boʻy ikkitadan. <strong>x(x + 5)</strong> — bu yuza "
                       "formulasi, perimetr emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Masala yechilib, oʻquvchilar soni "
                "x = 12,5 chiqdi.</p><p><strong>Bu nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Javob toʻgʻri, uni yaxlitlash kerak",
            "Masalada yoki yechimda xato bor — odam soni butun boʻlishi kerak",
            "Javobni ikkiga koʻpaytirish kerak",
            "Masalaning ikkita yechimi bor",
        ],
        "correct": "Masalada yoki yechimda xato bor — odam soni butun boʻlishi kerak",
        "explanation": "<p><strong>Xato bor.</strong> Odam, olma, kitob soni kasr "
                       "boʻlolmaydi. Bunday javob chiqsa, tenglamani va shartni "
                       "qayta oʻqing — bu hayotiylik nazorati.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Uch son: x, 2x va x + 10. "
                "Yigʻindisi 90.</p><p><strong>Qaysi tenglama toʻgʻri?</strong></p>",
        "choices": ["3x + 10 = 90", "4x + 10 = 90", "4x = 90", "3x + 10x = 90"],
        "correct": "4x + 10 = 90",
        "explanation": "<p><strong>4x + 10 = 90.</strong> Harfli hadlar "
                       "1 + 2 + 1 = 4, ozod had 10. Yechimi x = 20, sonlar 20, "
                       "40 va 30. Tekshirish: 20 + 40 + 30 = 90 ✓</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p>«Ikki chelakda 30 litr, 5 litr "
                "quyilsa teng boʻladi».</p><p><strong>Yechim: farq 5 litr, "
                "x + (x + 5) = 30 → 12,5 va 17,5</strong></p>",
        "choices": [
            "Farq 10 litr boʻlishi kerak — quyilganning ikki barobari",
            "Jami 30 emas, 35 litr boʻlishi kerak",
            "Chelaklar teng boʻlishi mumkin emas",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Farq 10 litr boʻlishi kerak — quyilganning ikki barobari",
        "explanation": "<p><strong>Farq 10 litr.</strong> Tekshirib koʻring: "
                       "17,5 − 5 = 12,5 va 12,5 + 5 = 17,5 — teng emas. Toʻgʻri "
                       "javob 20 va 10: 20 − 5 = 15 va 10 + 5 = 15 ✓</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p>«Boʻyi enidan 4 sm uzun, perimetri "
                "36 sm».</p>",
        "choices": [
            "x + (x + 4) = 36 → eni 16 sm",
            "2(x + x + 4) = 36 → eni 7 sm, boʻyi 11 sm",
            "4x + 4 = 36 → eni 8 sm",
            "x(x + 4) = 36 → eni 4 sm",
        ],
        "correct": "2(x + x + 4) = 36 → eni 7 sm, boʻyi 11 sm",
        "explanation": "<p><strong>7 sm va 11 sm.</strong> 2x + 4 = 18 → 2x = 14 "
                       "→ x = 7. Tekshirish: 2(7 + 11) = 36 ✓ va 11 − 7 = 4 ✓</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Onasi qizidan 24 yosh katta, ikkalasining yoshi yigʻindisi "
                "50.</p><p><strong>Onasi necha yoshda?</strong></p>",
        "choices": ["13 yoshda", "24 yoshda", "26 yoshda", "37 yoshda"],
        "correct": "37 yoshda",
        "explanation": "<p><strong>37 yoshda.</strong> Qiz x: x + (x + 24) = 50 → "
                       "2x = 26 → x = 13; onasi 13 + 24 = 37. Tekshirish: "
                       "13 + 37 = 50 ✓ <strong>13</strong> — qizning yoshi.</p>",
    },
    {
        "text": "<p>Uch qutida jami 102 ta olma bor. Ikkinchisida birinchisidan "
                "2 marta koʻp, uchinchisida birinchisidan 6 taga "
                "koʻp.</p><p><strong>Uchinchi qutida nechta olma bor?</strong></p>",
        "choices": ["24 ta", "30 ta", "48 ta", "54 ta"],
        "correct": "30 ta",
        "explanation": "<p><strong>30 ta.</strong> x + 2x + (x + 6) = 102 → "
                       "4x = 96 → x = 24; uchinchisi 24 + 6 = 30. Tekshirish: "
                       "24 + 48 + 30 = 102 ✓</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-37 Mashq: Ikki tomonida nomaʼlumi bor tenglamalar",
        "description": "20 savol — harfli hadlarni bir tomonga yigʻish, qavsli "
                       "tenglamalar, ayniyat va yechimi yoʻq holatlar.",
        "tutorial":    "PM-37:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM37,
    },
    {
        "title":       "PM-38 Mashq: Matnli masalani tenglama bilan yechish 1",
        "description": "20 savol — nomaʼlumni tanlash, ikki miqdorni bitta harf "
                       "bilan yozish, tenglama tuzish va savolga qaytish.",
        "tutorial":    "PM-38:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM38,
    },
    {
        "title":       "PM-39 Mashq: Matnli masalani tenglama bilan yechish 2",
        "description": "20 savol — uch qismli taqsimot, «quyib teng qilish» va "
                       "perimetr masalalari.",
        "tutorial":    "PM-39:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM39,
    },
]
