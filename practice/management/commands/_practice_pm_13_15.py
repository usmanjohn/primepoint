# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-13 … PM-15 (kvadrat ildiz, yaxlitlash, kasr).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ `text` maydoni |safe bilan chiqadi — HTML yozish mumkin (<sup>, <strong>).
   `choices` esa avtomatik ekranlanadi — u yerda HTML teg ISHLAMAYDI: kasrlar
   oddiy chiziqcha bilan (3/4), darajalar Yunikod belgisi bilan (², ³) yoziladi.
⚠️ Oʻnlik kasr PM-20 da — bu uch testda vergulli son yoʻq.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_13_15.py --master=prime \\
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
# PM-13 — kvadrat ildiz va aniq kvadratlar
# =====================================================================

Q_PM13 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>√49 = ?</strong></p>",
        "choices": ["7", "9", "24", "98"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 7 × 7 = 49. Ildiz — yarmini olish emas: "
                       "24 javobi 49 ni ikkiga boʻlganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>√25 = ?</strong></p>",
        "choices": ["5", "6", "12", "50"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 5 × 5 = 25.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>√81 = ?</strong></p>",
        "choices": ["8", "9", "18", "40"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> 9 × 9 = 81. 8 javobi jadvaldagi qoʻshni "
                       "qatordan (8<sup>2</sup> = 64) keladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>√1 = ?</strong></p>",
        "choices": ["0", "1", "2", "10"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> 1 × 1 = 1 — birning ildizi yana bir.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>√100 = ?</strong></p>",
        "choices": ["10", "20", "50", "1 000"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 10 × 10 = 100. Ildiz nollarni "
                       "ikkitadan bittaga qisqartiradi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>√144 = ?</strong></p>",
        "choices": ["12", "14", "22", "72"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 12 × 12 = 144 — kvadratlar jadvalining "
                       "oʻn ikkinchi qatori.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>√400 = ?</strong></p>",
        "choices": ["20", "40", "200", "1 600"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> 20 × 20 = 400. 200 javobi nollarni "
                       "qisqartirmaganda chiqadi: 200 × 200 = 40 000.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>√169 = ?</strong></p>",
        "choices": ["11", "13", "17", "84"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> 13 × 13 = 169.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>√(36 × 4) = ?</strong></p>",
        "choices": ["6", "10", "12", "144"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Ildiz qavs kabi ishlaydi: avval "
                       "36 × 4 = 144, keyin √144 = 12. 10 javobi √36 + √4 = 6 + 2 "
                       "dan chiqadi — bu notoʻgʻri yoʻl.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>√64 + √16 = ?</strong></p>",
        "choices": ["10", "12", "40", "80"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Bu yerda ikkita alohida ildiz bor: "
                       "√64 = 8, √16 = 4, yigʻindisi 12. Diqqat: √(64 + 16) = √80 "
                       "boʻlardi, u esa butun son emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>√900 = ?</strong></p>",
        "choices": ["30", "90", "300", "450"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> 30 × 30 = 900: 9 → 3 va bitta nol.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>√225 = ?</strong></p>",
        "choices": ["15", "25", "45", "112"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> 15 × 15 = 225.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son aniq kvadrat "
                "EMAS?</strong></p>",
        "choices": ["16", "25", "30", "36"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> 16 = 4<sup>2</sup>, 25 = 5<sup>2</sup>, "
                       "36 = 6<sup>2</sup>. 30 esa 25 bilan 36 orasida — uning ildizi "
                       "butun son emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>√50 qaysi ikki butun son "
                "orasida turadi?</strong></p>",
        "choices": ["5 va 6", "6 va 7", "7 va 8", "24 va 25"],
        "correct": "7 va 8",
        "explanation": "<p><strong>7 va 8 orasida.</strong> 49 &lt; 50 &lt; 64, demak "
                       "√49 &lt; √50 &lt; √64. 50 soni 49 ga juda yaqin, shuning uchun "
                       "javob 7 ga yaqinroq.</p>",
    },
    {
        "text": "<p>Hisoblamasdan aniqlang.</p><p><strong>Qaysi son aniq kvadrat "
                "boʻlishi mumkin emas — oxirgi raqamiga qarab?</strong></p>",
        "choices": ["121", "196", "289", "347"],
        "correct": "347",
        "explanation": "<p><strong>347.</strong> Aniq kvadratning oxirgi raqami hech "
                       "qachon 2, 3, 7 yoki 8 boʻlmaydi. Qolganlari: 121 = 11<sup>2</sup>, "
                       "196 = 14<sup>2</sup>, 289 = 17<sup>2</sup>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>√(9 + 16) nimaga "
                "teng?</strong></p>",
        "choices": ["5", "7", "12", "25"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Ildiz belgisi qavs vazifasini bajaradi: "
                       "avval 9 + 16 = 25, keyin √25 = 5. 7 javobi — eng mashhur xato: "
                       "√9 + √16 = 3 + 4.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Bekzod shunday yozdi: <strong>√36 = 18</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Hech qanday xato yoʻq, javob toʻgʻri",
            "Javob 9 boʻlishi kerak edi",
            "Bekzod sonni ikkiga boʻlgan; ildiz esa 6, chunki 6 × 6 = 36",
            "Javob 72 boʻlishi kerak edi",
        ],
        "correct": "Bekzod sonni ikkiga boʻlgan; ildiz esa 6, chunki 6 × 6 = 36",
        "explanation": "<p><strong>√36 = 6.</strong> Ildiz chiqarish — yarmini olish "
                       "emas. Tekshiruv: 18 × 18 = 324, 36 emas.</p>",
    },
    {
        "text": "<p>Dilnoza shunday yozdi: <strong>√10 000 = 1 000</strong>.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Nollar ikkitadan bittaga qisqaradi: javob 100",
            "Hech qanday xato yoʻq, javob toʻgʻri",
            "Javob 10 boʻlishi kerak edi",
            "Javob 5 000 boʻlishi kerak edi",
        ],
        "correct": "Nollar ikkitadan bittaga qisqaradi: javob 100",
        "explanation": "<p><strong>√10 000 = 100.</strong> Tekshiruv: 100 × 100 = "
                       "10 000 ✓ Dilnozaning javobi 1 000 × 1 000 = 1 000 000 "
                       "boʻlardi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Kvadrat shaklidagi xonaning yuzasi <strong>64 m<sup>2</sup></strong>.</p>"
                "<p><strong>Xonaning perimetri necha metr?</strong></p>",
        "choices": ["8 m", "16 m", "32 m", "256 m"],
        "correct": "32 m",
        "explanation": "<p><strong>32 m.</strong> Avval tomon: √64 = 8 m. Keyin "
                       "perimetr: 4 × 8 = 32 m. 8 javobi faqat tomonni, 16 javobi esa "
                       "ikkita tomonni bergan boʻlardi.</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Bogʻbon <strong>196 ta</strong> koʻchatni kvadrat shaklida — "
                "qatorlar soni bir qatordagi koʻchatlar soniga teng qilib — "
                "ekdi.</p><p><strong>Bir qatorda nechta koʻchat bor?</strong></p>",
        "choices": ["14 ta", "16 ta", "49 ta", "98 ta"],
        "correct": "14 ta",
        "explanation": "<p><strong>14 ta.</strong> Qatorlar soni × bir qatordagi soni = "
                       "196, ikkalasi teng, demak √196 = 14. Tekshiruv: "
                       "14 × 14 = 196 ✓</p>",
    },
]


# =====================================================================
# PM-14 — yaxlitlash va taqribiy hisob
# =====================================================================

Q_PM14 = [
    # 1–5 tanish
    {
        "text": "<p><strong>47</strong> ni oʻnliklarga yaxlitlang.</p>",
        "choices": ["40", "45", "50", "70"],
        "correct": "50",
        "explanation": "<p><strong>50.</strong> Birliklar raqami 7 — beshdan katta, "
                       "demak yuqoriga.</p>",
    },
    {
        "text": "<p><strong>43</strong> ni oʻnliklarga yaxlitlang.</p>",
        "choices": ["30", "40", "45", "50"],
        "correct": "40",
        "explanation": "<p><strong>40.</strong> Birliklar raqami 3 — beshdan kichik, "
                       "demak pastga.</p>",
    },
    {
        "text": "<p><strong>285</strong> ni yuzliklarga yaxlitlang.</p>",
        "choices": ["200", "280", "290", "300"],
        "correct": "300",
        "explanation": "<p><strong>300.</strong> Yuzliklarga yaxlitlaganda oʻnliklar "
                       "raqamiga (8 ga) qaraymiz — yuqoriga. 290 javobi oʻnliklarga "
                       "yaxlitlaganda chiqardi.</p>",
    },
    {
        "text": "<p><strong>1 240</strong> ni mingliklarga yaxlitlang.</p>",
        "choices": ["1 000", "1 200", "1 300", "2 000"],
        "correct": "1 000",
        "explanation": "<p><strong>1 000.</strong> Mingliklarga yaxlitlaganda "
                       "yuzliklar raqamiga (2 ga) qaraymiz — pastga.</p>",
    },
    {
        "text": "<p><strong>6 500</strong> ni mingliklarga yaxlitlang.</p>",
        "choices": ["6 000", "6 500", "7 000", "10 000"],
        "correct": "7 000",
        "explanation": "<p><strong>7 000.</strong> 5 raqami har doim yuqoriga "
                       "koʻtariladi — «oʻrtada turibdi» degan istisno yoʻq.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p><strong>3 472</strong> ni yuzliklarga yaxlitlang.</p>",
        "choices": ["3 000", "3 400", "3 470", "3 500"],
        "correct": "3 500",
        "explanation": "<p><strong>3 500.</strong> Oʻnliklar raqami 7 — yuqoriga. "
                       "3 470 javobi oʻnliklarga yaxlitlaganda, 3 000 esa "
                       "mingliklarga yaxlitlaganda chiqadi.</p>",
    },
    {
        "text": "<p><strong>2 449</strong> ni yuzliklarga yaxlitlang.</p>",
        "choices": ["2 000", "2 400", "2 450", "2 500"],
        "correct": "2 400",
        "explanation": "<p><strong>2 400.</strong> Faqat oʻnliklar raqamiga (4 ga) "
                       "qaraladi — pastga. 2 500 javobi ketma-ket yaxlitlashdan "
                       "(2 449 → 2 450 → 2 500) chiqadi, bu esa xato yoʻl.</p>",
    },
    {
        "text": "<p><strong>19 800</strong> ni mingliklarga yaxlitlang.</p>",
        "choices": ["19 000", "19 800", "20 000", "100 000"],
        "correct": "20 000",
        "explanation": "<p><strong>20 000.</strong> Yuzliklar raqami 8 — yuqoriga, va "
                       "koʻtarilish razryaddan oshib, 19 ming 20 mingga aylanadi.</p>",
    },
    {
        "text": "<p><strong>155</strong> ni oʻnliklarga yaxlitlang.</p>",
        "choices": ["100", "150", "160", "200"],
        "correct": "160",
        "explanation": "<p><strong>160.</strong> Birliklar raqami 5 — yuqoriga.</p>",
    },
    {
        "text": "<p>Ogʻzaki baholang.</p><p><strong>198 × 4 ≈ ?</strong></p>",
        "choices": ["600", "800", "1 000", "8 000"],
        "correct": "800",
        "explanation": "<p><strong>≈ 800.</strong> 198 ≈ 200, 200 × 4 = 800. Aniq "
                       "javob 792 — taxmin 8 taga katta, chunki har bir 198 ni 2 taga "
                       "oshirgandik.</p>",
    },
    {
        "text": "<p>Ogʻzaki baholang.</p><p><strong>1 234 ÷ 6 ≈ ?</strong></p>",
        "choices": ["20", "200", "600", "2 000"],
        "correct": "200",
        "explanation": "<p><strong>≈ 200.</strong> 1 234 ≈ 1 200, u esa oltiga butun "
                       "boʻlinadi: 1 200 ÷ 6 = 200.</p>",
    },
    {
        "text": "<p>Ogʻzaki baholang.</p><p><strong>497 × 6 ≈ ?</strong></p>",
        "choices": ["300", "2 400", "3 000", "30 000"],
        "correct": "3 000",
        "explanation": "<p><strong>≈ 3 000.</strong> 497 ≈ 500, 500 × 6 = 3 000. Aniq "
                       "javob 2 982.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bir xil son — <strong>4 850</strong> "
                "— uch xil razryadga yaxlitlandi.</p>"
                "<p><strong>Qaysi qator toʻliq toʻgʻri?</strong></p>",
        "choices": [
            "oʻnliklarga 4 850 · yuzliklarga 4 900 · mingliklarga 5 000",
            "oʻnliklarga 4 900 · yuzliklarga 5 000 · mingliklarga 5 000",
            "oʻnliklarga 4 850 · yuzliklarga 4 800 · mingliklarga 4 000",
            "oʻnliklarga 4 860 · yuzliklarga 4 900 · mingliklarga 5 000",
        ],
        "correct": "oʻnliklarga 4 850 · yuzliklarga 4 900 · mingliklarga 5 000",
        "explanation": "<p>Oʻnliklarga: birliklar raqami 0, son oʻzgarmaydi — 4 850. "
                       "Yuzliklarga: oʻnliklar raqami 5 — yuqoriga, 4 900. "
                       "Mingliklarga: yuzliklar raqami 8 — yuqoriga, 5 000.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi taxmin 3 900 ga eng "
                "yaqin natija beradi?</strong></p>",
        "choices": ["39 × 10", "390 × 100", "39 × 100", "3 × 900"],
        "correct": "39 × 100",
        "explanation": "<p><strong>39 × 100 = 3 900.</strong> Qolganlari: 39 × 10 = 390, "
                       "390 × 100 = 39 000, 3 × 900 = 2 700. Razryadni sanash "
                       "oʻrganilsa, bunday savol bir soniyada yechiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi javob mantiqan "
                "notoʻgʻri?</strong></p>",
        "choices": [
            "Sinfda 28 oʻquvchi bor",
            "Piyoda odam soatiga 5 km yuradi",
            "Bir kilogramm non 45 000 000 soʻm turadi",
            "Maktabgacha 20 daqiqa yurish kerak",
        ],
        "correct": "Bir kilogramm non 45 000 000 soʻm turadi",
        "explanation": "<p>Bu razryad xatosi: nollar ortiqcha yozilgan. Har javobdan "
                       "keyin «mantiqiymi?» deb soʻrash odati aynan shunday "
                       "xatolarni ushlaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nima uchun taxminiy javob "
                "= belgisi bilan emas, ≈ belgisi bilan yoziladi?</strong></p>",
        "choices": [
            "Chunki ≈ belgisini yozish qisqaroq",
            "Chunki taxmin aniq javob emas, unga faqat yaqin",
            "Chunki taxmin har doim aniq javobdan katta boʻladi",
            "Chunki yaxlitlangan sonlarda nol koʻp",
        ],
        "correct": "Chunki taxmin aniq javob emas, unga faqat yaqin",
        "explanation": "<p>198 × 4 <strong>≈</strong> 800, aniq javob esa 792. "
                       "Tenglik belgisi qoʻyilsa, notoʻgʻri tasdiq yozilgan boʻladi. "
                       "Taxmin aniq javobdan katta ham, kichik ham boʻlishi mumkin.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Jasur <strong>2 449</strong> ni yuzliklarga yaxlitladi va "
                "<strong>2 500</strong> deb yozdi.</p><p><strong>Xato "
                "qayerda?</strong></p>",
        "choices": [
            "Javob 2 000 boʻlishi kerak edi",
            "U ketma-ket yaxlitlagan; faqat oʻnliklar raqamiga qaralib, javob 2 400 "
            "boʻladi",
            "Hech qanday xato yoʻq, javob toʻgʻri",
            "Javob 2 450 boʻlishi kerak edi",
        ],
        "correct": "U ketma-ket yaxlitlagan; faqat oʻnliklar raqamiga qaralib, javob "
                   "2 400 boʻladi",
        "explanation": "<p><strong>2 400.</strong> Jasur avval 2 449 ni 2 450 ga, "
                       "keyin 2 450 ni 2 500 ga yaxlitlagan. Yaxlitlashda faqat "
                       "<i>bitta</i> raqamga — yaxlitlanayotgan razryaddan "
                       "keyingisiga — qaraladi.</p>",
    },
    {
        "text": "<p>Afsona <strong>198 × 4</strong> ni hisoblab, daftariga "
                "<strong>198 × 4 = 800</strong> deb yozdi.</p><p><strong>Xato "
                "qayerda?</strong></p>",
        "choices": [
            "Taxmin 800, aniq javob esa 792; tenglik belgisi qoʻyib boʻlmaydi",
            "Hech qanday xato yoʻq, javob toʻgʻri",
            "Taxmin 700 boʻlishi kerak edi",
            "198 ni 190 ga yaxlitlash kerak edi",
        ],
        "correct": "Taxmin 800, aniq javob esa 792; tenglik belgisi qoʻyib boʻlmaydi",
        "explanation": "<p>Taxmin — tekshiruv vositasi, natija emas. Toʻgʻri yozuv: "
                       "198 × 4 ≈ 800, aniq javob 792.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Buvijon bozorda <strong>3 800</strong>, <strong>2 100</strong> va "
                "<strong>1 450</strong> soʻmlik uch narsa oldi. Hamyonida "
                "<strong>8 000 soʻm</strong> bor.</p>"
                "<p><strong>Xariddan keyin qancha pul qoladi?</strong></p>",
        "choices": ["650 soʻm", "1 000 soʻm", "1 350 soʻm", "7 350 soʻm"],
        "correct": "650 soʻm",
        "explanation": "<p><strong>650 soʻm.</strong> Taxmin: 4 000 + 2 000 + 1 000 "
                       "≈ 7 000 — pul yetadi. Aniq hisob: 3 800 + 2 100 + 1 450 = "
                       "7 350; 8 000 − 7 350 = 650. 1 000 javobi taxminni aniq javob "
                       "deb olganda chiqadi.</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Doʻkonda daftar <strong>2 800 soʻm</strong>. Sherbek "
                "<strong>12 ta</strong> daftar olmoqchi, choʻntagida "
                "<strong>30 000 soʻm</strong> bor.</p>"
                "<p><strong>Toʻgʻri xulosa qaysi?</strong></p>",
        "choices": [
            "Puli yetadi, 3 600 soʻm ortadi",
            "Puli yetadi, roppa-rosa yetadi",
            "Puli yetmaydi, yana 3 600 soʻm kerak",
            "Puli yetmaydi, yana 6 000 soʻm kerak",
        ],
        "correct": "Puli yetmaydi, yana 3 600 soʻm kerak",
        "explanation": "<p>Taxmin: 2 800 ≈ 3 000, 3 000 × 12 = 36 000 — 30 000 dan "
                       "koʻp, demak yetmasligi ehtimoli katta. Aniq hisob: "
                       "2 800 × 12 = 33 600 soʻm. 33 600 − 30 000 = 3 600 soʻm "
                       "yetishmaydi.</p>",
    },
]


# =====================================================================
# PM-15 — kasr nima
# =====================================================================

Q_PM15 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3/8 kasrida maxraj qaysi "
                "son?</strong></p>",
        "choices": ["3", "5", "8", "11"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Maxraj — pastdagi son. U butun nechta "
                       "teng boʻlakka boʻlinganini bildiradi. 3 esa surat.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Surat nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Butun nechta teng boʻlakka boʻlinganini",
            "Nechta boʻlak olinganini",
            "Boʻlaklarning ogʻirligini",
            "Kasrning kattaligini",
        ],
        "correct": "Nechta boʻlak olinganini",
        "explanation": "<p>Surat — yuqoridagi son, olingan boʻlaklar soni. Nechta "
                       "boʻlakka boʻlinganini esa maxraj aytadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Beshdan ikki» qanday "
                "yoziladi?</strong></p>",
        "choices": ["2/5", "5/2", "2/7", "25"],
        "correct": "2/5",
        "explanation": "<p><strong>2/5.</strong> Oʻqilishda maxraj oldin aytiladi "
                       "(«beshdan»), yozuvda esa u pastda turadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bitta nonni <strong>6 kishi</strong> "
                "teng boʻlishdi.</p><p><strong>Har kimga nonning qanchasi "
                "tegadi?</strong></p>",
        "choices": ["1/6", "6/1", "1/3", "6"],
        "correct": "1/6",
        "explanation": "<p><strong>1/6.</strong> Non oltita teng boʻlakka boʻlindi "
                       "(maxraj 6), har kimga bittadan tegdi (surat 1).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>8/8 nimaga teng?</strong></p>",
        "choices": ["0", "1/8", "1", "8"],
        "correct": "1",
        "explanation": "<p><strong>1 ga.</strong> Sakkizta boʻlakning hammasi "
                       "yigʻilsa, butun qaytadi. Surat maxrajga teng boʻlsa, kasr "
                       "butunga teng.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>1/3 va 1/5 dan qaysi biri "
                "katta?</strong></p>",
        "choices": ["1/3", "1/5", "Ular teng", "Aniqlab boʻlmaydi"],
        "correct": "1/3",
        "explanation": "<p><strong>1/3.</strong> Nonni uchga boʻlsangiz, boʻlak beshga "
                       "boʻlgandan katta chiqadi. Maxraj katta — boʻlak kichik.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3/7 va 5/7 dan qaysi biri "
                "katta?</strong></p>",
        "choices": ["3/7", "5/7", "Ular teng", "Aniqlab boʻlmaydi"],
        "correct": "5/7",
        "explanation": "<p><strong>5/7.</strong> Maxrajlar bir xil — boʻlaklar bir xil "
                       "kattalikda. Demak nechtasi koʻp boʻlsa, oʻsha katta.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>24 ning 1/4 qismi qancha?</strong></p>",
        "choices": ["4", "6", "8", "20"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 24 ÷ 4 = 6. Tekshiruv: 6 × 4 = 24 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>30 ning 2/5 qismi qancha?</strong></p>",
        "choices": ["6", "10", "12", "15"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Ikki qadam: 30 ÷ 5 = 6 (beshdan bir "
                       "qism), keyin 6 × 2 = 12. 6 javobi ikkinchi qadamni "
                       "tashlab ketganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>20 ning 3/4 qismi qancha?</strong></p>",
        "choices": ["5", "12", "15", "16"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> 20 ÷ 4 = 5, keyin 5 × 3 = 15. Javob "
                       "20 dan kichik — toʻgʻri, chunki 3/4 butundan kam.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>45 ning 2/9 qismi qancha?</strong></p>",
        "choices": ["5", "9", "10", "18"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 45 ÷ 9 = 5, keyin 5 × 2 = 10.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Tort <strong>10 ta teng "
                "boʻlak</strong>ka boʻlindi va <strong>3 tasi</strong> yeyildi.</p>"
                "<p><strong>Tortning qanchasi qoldi?</strong></p>",
        "choices": ["3/10", "7/10", "7/3", "10/7"],
        "correct": "7/10",
        "explanation": "<p><strong>7/10.</strong> Boʻlaklar soni oʻzgarmaydi — maxraj "
                       "baribir 10. Qolgan boʻlaklar: 10 − 3 = 7 ta.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Quyidagilardan qaysi biri "
                "eng kichik?</strong></p>",
        "choices": ["1/2", "1/3", "1/4", "1/8"],
        "correct": "1/8",
        "explanation": "<p><strong>1/8.</strong> Suratlar bir xil boʻlganda, maxraji "
                       "eng katta kasr eng kichik boʻladi: 1/8 &lt; 1/4 &lt; 1/3 "
                       "&lt; 1/2. Tortni sakkiz kishiga boʻlsangiz, ulush eng "
                       "kichkina chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bir non koʻz bilan chamalab, "
                "<strong>oltita har xil</strong> boʻlakka boʻlindi.</p>"
                "<p><strong>Bitta boʻlakni 1/6 deb atash mumkinmi?</strong></p>",
        "choices": [
            "Ha, chunki boʻlaklar soni oltita",
            "Ha, chunki non bitta edi",
            "Yoʻq, chunki kasr uchun boʻlaklar teng boʻlishi shart",
            "Yoʻq, chunki non kasr bilan oʻlchanmaydi",
        ],
        "correct": "Yoʻq, chunki kasr uchun boʻlaklar teng boʻlishi shart",
        "explanation": "<p>Kasrning butun mantigʻi teng boʻlishga tayanadi. Boʻlaklar "
                       "har xil boʻlsa, ularning hech biri «oltidan bir» emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Son oʻqida 3/4 qayerda "
                "turadi?</strong></p>",
        "choices": [
            "0 dan chapda",
            "0 ga 1 dan koʻra yaqinroq",
            "1 ga 0 dan koʻra yaqinroq",
            "1 dan oʻngda",
        ],
        "correct": "1 ga 0 dan koʻra yaqinroq",
        "explanation": "<p>0 bilan 1 orasi toʻrtta teng boʻlakka boʻlinsa, 3/4 "
                       "uchinchi belgida turadi — butunga bitta boʻlak qolgan "
                       "joyda.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Afsona 40 ta shirinlikning 1/5 "
                "qismini, Jasur esa 40 ta shirinlikning 1/4 qismini oldi.</p>"
                "<p><strong>Kim koʻproq oldi?</strong></p>",
        "choices": [
            # literal ">" — choices are autoescaped, so &gt; would show as text
            "Afsona, chunki 5 > 4",
            "Jasur, chunki maxraj kichik — boʻlak katta",
            "Ikkalasi teng oldi",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Jasur, chunki maxraj kichik — boʻlak katta",
        "explanation": "<p>Afsona: 40 ÷ 5 = 8 ta. Jasur: 40 ÷ 4 = 10 ta. Katta maxraj "
                       "kichik boʻlak degani — bu kasrdagi eng kutilmagan qoida.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Sherbek shunday dedi: <strong>«1/8 kasri 1/6 dan katta, chunki "
                "8 &gt; 6»</strong>.</p><p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Hech qanday xato yoʻq",
            "Ular teng, chunki suratlari bir xil",
            "Maxraj boʻlakning kattaligini belgilaydi: 1/8 aslida 1/6 dan kichik",
            "Kasrlarni umuman taqqoslab boʻlmaydi",
        ],
        "correct": "Maxraj boʻlakning kattaligini belgilaydi: 1/8 aslida 1/6 dan kichik",
        "explanation": "<p>Butun sakkizga boʻlinsa, boʻlak oltiga boʻlingandan "
                       "kichikroq chiqadi. Suratlar teng boʻlganda maxraj katta — "
                       "kasr kichik.</p>",
    },
    {
        "text": "<p>Dilnoza «uchdan ikki» ni <strong>3/2</strong> deb yozdi.</p>"
                "<p><strong>Xato qayerda?</strong></p>",
        "choices": [
            "Toʻgʻri yozuv 2/3: oʻqishda maxraj oldin aytiladi, yozuvda esa pastda "
            "turadi",
            "Hech qanday xato yoʻq",
            "Toʻgʻri yozuv 3/5 boʻlishi kerak edi",
            "Toʻgʻri yozuv 23 boʻlishi kerak edi",
        ],
        "correct": "Toʻgʻri yozuv 2/3: oʻqishda maxraj oldin aytiladi, yozuvda esa "
                   "pastda turadi",
        "explanation": "<p>«Uchdan ikki» — butun uchga boʻlingan, ikkitasi olingan: "
                       "<strong>2/3</strong>. Dilnozaning yozuvi 3/2 esa butundan "
                       "kattaroq son boʻlib qoladi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Sinfda <strong>28 oʻquvchi</strong> bor, ularning "
                "<strong>1/4</strong> qismi shaxmat toʻgaragiga qatnaydi.</p>"
                "<p><strong>Nechta oʻquvchi shaxmat toʻgaragiga qatnamaydi?</strong></p>",
        "choices": ["4 ta", "7 ta", "14 ta", "21 ta"],
        "correct": "21 ta",
        "explanation": "<p><strong>21 ta.</strong> Qatnaydiganlar: 28 ÷ 4 = 7 ta. "
                       "Qatnamaydiganlar: 28 − 7 = 21 ta. 7 javobi savolni notoʻgʻri "
                       "oʻqiganda tanlanadi — soʻralgani qatnamaydiganlar.</p>",
    },
    {
        "text": "<p><strong>Matnli masala.</strong></p>"
                "<p>Buvijon <strong>36 ta somsa</strong> pishirdi. <strong>1/4</strong> "
                "qismini qoʻshnilarga berdi, <strong>1/3</strong> qismini nabiralari "
                "yedi.</p><p><strong>Nechta somsa qoldi?</strong></p>",
        "choices": ["9 ta", "12 ta", "15 ta", "21 ta"],
        "correct": "15 ta",
        "explanation": "<p><strong>15 ta.</strong> Qoʻshnilarga: 36 ÷ 4 = 9 ta. "
                       "Nabiralarga: 36 ÷ 3 = 12 ta. Ketgani 9 + 12 = 21 ta, qolgani "
                       "36 − 21 = 15 ta. 21 javobi ketganlar sonini bergan "
                       "boʻlardi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-13 Mashq: Kvadrat ildiz va aniq kvadratlar",
        "description": "20 savol — √ belgisi, aniq kvadratlar, nollar qoidasi, "
                       "ildizni baholash va yuza-perimetr masalalari.",
        "tutorial":    "PM-13:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM13,
    },
    {
        "title":       "PM-14 Mashq: Yaxlitlash va taqribiy hisob",
        "description": "20 savol — razryadga yaxlitlash, ogʻzaki taxmin, ≈ belgisi va "
                       "«javob mantiqiymi?» tekshiruvi.",
        "tutorial":    "PM-14:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM14,
    },
    {
        "title":       "PM-15 Mashq: Kasr nima",
        "description": "20 savol — surat va maxraj, teng boʻlaklar, kasrlarni "
                       "taqqoslash va sonning kasr qismini topish.",
        "tutorial":    "PM-15:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM15,
    },
]
