# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-40 … PM-42 (tengsizlik, modul, daraja qonunlari).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq. Shuning uchun darajalar «2^7»
   koʻrinishida yoziladi, savol matnida esa <sup> ishlatiladi.
⚠️ Kumulyativ: modulli tengsizlik yoʻq; ildiz qonunlari yoʻq; koʻphadlar
   (PM-43) va qisqa koʻpaytirish formulalari (PM-44) keyingi darslarda.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_40_42.py --master=prime \\
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
# PM-40 — tengsizlik
# =====================================================================

Q_PM40 = [
    # 1–5 tanish
    {
        "text": "<p>Tengsizlikni yeching.</p><p><strong>x + 5 &gt; 12</strong></p>",
        "choices": ["x > 7", "x > 17", "x < 7", "x < 17"],
        "correct": "x > 7",
        "explanation": "<p><strong>x &gt; 7.</strong> Ikki tomondan 5 ni ayiramiz. "
                       "Qoʻshish va ayirishda ishora oʻzgarmaydi. Tekshirish: "
                       "x = 8 → 13 &gt; 12 ✓</p>",
    },
    {
        "text": "<p>Tengsizlikni yeching.</p><p><strong>3x ≤ 21</strong></p>",
        "choices": ["x ≤ 7", "x ≥ 7", "x ≤ 18", "x ≤ 63"],
        "correct": "x ≤ 7",
        "explanation": "<p><strong>x ≤ 7.</strong> Ikki tomonni 3 ga boʻldik; 3 "
                       "musbat, shuning uchun ishora oʻzgarmadi. x = 7 ham javob "
                       "ichida.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Kamida 60 ball» qanday "
                "yoziladi?</strong></p>",
        "choices": ["ball < 60", "ball ≤ 60", "ball > 60", "ball ≥ 60"],
        "correct": "ball ≥ 60",
        "explanation": "<p><strong>ball ≥ 60.</strong> «Kamida» degani 60 ning oʻzi "
                       "ham mumkin. <strong>&gt; 60</strong> boʻlsa, roppa-rosa 60 "
                       "ball olgan oʻquvchi oʻtmay qolardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Koʻpi bilan 20 kg» qanday "
                "yoziladi?</strong></p>",
        "choices": ["m ≤ 20", "m < 20", "m ≥ 20", "m > 20"],
        "correct": "m ≤ 20",
        "explanation": "<p><strong>m ≤ 20.</strong> «Koʻpi bilan» — shu qiymat yoki "
                       "undan kam. Roppa-rosa 20 kilogramm ham mumkin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Son oʻqida 6 nuqtasida ichi boʻsh "
                "doiracha turibdi va oʻng tomon boʻyalgan.</p><p><strong>Bu qaysi "
                "tengsizlik?</strong></p>",
        "choices": ["x > 6", "x ≥ 6", "x < 6", "x ≤ 6"],
        "correct": "x > 6",
        "explanation": "<p><strong>x &gt; 6.</strong> Ichi boʻsh doiracha chegara "
                       "javobga <em>kirmasligi</em>ni bildiradi; boʻyalgan oʻng "
                       "tomon esa oltidan katta sonlarni.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Tengsizlikni yeching.</p><p><strong>2x + 3 &lt; 15</strong></p>",
        "choices": ["x < 6", "x < 9", "x > 6", "x < 12"],
        "correct": "x < 6",
        "explanation": "<p><strong>x &lt; 6.</strong> 2x &lt; 12, keyin 2 ga "
                       "boʻlamiz. <strong>x &lt; 9</strong> — faqat 3 ni ayirib, "
                       "boʻlishni unutishdan chiqadi.</p>",
    },
    {
        "text": "<p>Tengsizlikni yeching.</p><p><strong>5x − 4 ≥ 26</strong></p>",
        "choices": ["x ≥ 6", "x ≥ 30", "x ≤ 6", "x ≥ 4,4"],
        "correct": "x ≥ 6",
        "explanation": "<p><strong>x ≥ 6.</strong> Ikki tomonga 4 qoʻshamiz: "
                       "5x ≥ 30; keyin 5 ga boʻlamiz. Tekshirish: x = 6 → "
                       "26 ≥ 26 ✓</p>",
    },
    {
        "text": "<p>Tengsizlikni yeching.</p><p><strong>−2x &lt; 6</strong></p>",
        "choices": ["x > −3", "x < −3", "x > 3", "x < 3"],
        "correct": "x > −3",
        "explanation": "<p><strong>x &gt; −3.</strong> Manfiy songa boʻlinganda "
                       "ishora teskari boʻladi. Tekshirish: x = 0 → 0 &lt; 6 ✓ "
                       "demak 0 javob ichida.</p>",
    },
    {
        "text": "<p>Tengsizlikni yeching.</p><p><strong>−4x ≥ 20</strong></p>",
        "choices": ["x ≤ −5", "x ≥ −5", "x ≤ 5", "x ≥ 5"],
        "correct": "x ≤ −5",
        "explanation": "<p><strong>x ≤ −5.</strong> −4 ga boʻlganda ishora aylanadi. "
                       "Tekshirish: x = −6 → 24 ≥ 20 ✓; x = 0 → 0 ≥ 20 ✗</p>",
    },
    {
        "text": "<p>Tengsizlikni yeching.</p><p><strong>4x + 1 &gt; 2x + 9</strong></p>",
        "choices": ["x > 4", "x > 5", "x < 4", "x > 2"],
        "correct": "x > 4",
        "explanation": "<p><strong>x &gt; 4.</strong> Ikki tomondan 2x ni ayiramiz: "
                       "2x + 1 &gt; 9 → 2x &gt; 8. Tengsizlikda ham harfli hadlarni "
                       "bir tomonga yigʻamiz (PM-37).</p>",
    },
    {
        "text": "<p>Tengsizlikni yeching.</p><p><strong>x/3 ≤ 4</strong></p>",
        "choices": ["x ≤ 12", "x ≤ 4/3", "x ≥ 12", "x ≤ 7"],
        "correct": "x ≤ 12",
        "explanation": "<p><strong>x ≤ 12.</strong> Ikki tomonni 3 ga koʻpaytiramiz; "
                       "3 musbat, ishora oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Tengsizlikni yeching.</p><p><strong>10 − x &gt; 4</strong></p>",
        "choices": ["x < 6", "x > 6", "x < 14", "x > 14"],
        "correct": "x < 6",
        "explanation": "<p><strong>x &lt; 6.</strong> 10 − x &gt; 4 → −x &gt; −6; "
                       "ikki tomonni −1 ga boʻlganda ishora aylanadi. Tekshirish: "
                       "x = 5 → 5 &gt; 4 ✓; x = 7 → 3 &gt; 4 ✗</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi holatda tengsizlik "
                "ishorasi teskari boʻladi?</strong></p>",
        "choices": [
            "Ikki tomonga manfiy son qoʻshilganda",
            "Ikki tomon manfiy songa koʻpaytirilganda yoki boʻlinganda",
            "Ikki tomondan son ayirilganda",
            "Ikki tomon musbat songa boʻlinganda",
        ],
        "correct": "Ikki tomon manfiy songa koʻpaytirilganda yoki boʻlinganda",
        "explanation": "<p><strong>Faqat manfiy songa koʻpaytirish yoki "
                       "boʻlishda.</strong> Qoʻshish va ayirish tartibni "
                       "buzmaydi: 3 &lt; 5 dan 3 − 10 &lt; 5 − 10 chiqadi va bu "
                       "rost.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>x ≥ 4 va x &gt; 4 "
                "orasidagi farq nima?</strong></p>",
        "choices": [
            "Farqi yoʻq",
            "Birinchisida 4 ham yechim, ikkinchisida yoʻq",
            "Ikkinchisida 4 ham yechim, birinchisida yoʻq",
            "Birinchisi faqat butun sonlarni bildiradi",
        ],
        "correct": "Birinchisida 4 ham yechim, ikkinchisida yoʻq",
        "explanation": "<p><strong>Chegaraning oʻzi.</strong> ≥ da chegara kiradi "
                       "(son oʻqida toʻla doiracha), &gt; da kirmaydi (ichi boʻsh "
                       "doiracha).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son x &lt; −2 "
                "tengsizligining yechimi?</strong></p>",
        "choices": ["−5", "−2", "0", "2"],
        "correct": "−5",
        "explanation": "<p><strong>−5.</strong> Manfiy sonlarda −5 son oʻqida −2 dan "
                       "chapda turadi, demak undan kichik. <strong>−2</strong> "
                       "chegaraning oʻzi va qatʼiy tengsizlikka kirmaydi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Liftga koʻpi bilan 400 kg yuk sigʻadi. "
                "Unda allaqachon 250 kg yuk bor.</p><p><strong>Yana qancha yuk "
                "solish mumkin?</strong></p>",
        "choices": ["m ≤ 150 kg", "m < 150 kg", "m ≥ 150 kg", "m ≤ 650 kg"],
        "correct": "m ≤ 150 kg",
        "explanation": "<p><strong>m ≤ 150 kg.</strong> 250 + m ≤ 400 → m ≤ 150. "
                       "Roppa-rosa 150 kilogramm ham mumkin, chunki jami 400 boʻladi "
                       "va u chegaraga teng.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>−3x &lt; 12 → x &lt; −4"
                "</strong></p>",
        "choices": [
            "Manfiy songa boʻlinganda ishora teskari boʻladi: x > −4",
            "Ikki tomonga 3 qoʻshish kerak edi",
            "Javob x < 4 boʻlishi kerak",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Manfiy songa boʻlinganda ishora teskari boʻladi: x > −4",
        "explanation": "<p><strong>x &gt; −4.</strong> Tekshirish: x = 0 olsak "
                       "0 &lt; 12 rost, demak nol javob ichida boʻlishi kerak. "
                       "x &lt; −4 esa nolni tashqarida qoldiradi.</p>",
    },
    {
        "text": "<p>Qaysi yozuv toʻgʻri?</p><p><strong>«Sinfda kamida 15 oʻquvchi "
                "bor»</strong></p>",
        "choices": ["n < 15", "n ≤ 15", "n > 15", "n ≥ 15"],
        "correct": "n ≥ 15",
        "explanation": "<p><strong>n ≥ 15.</strong> «Kamida» — shu son yoki undan "
                       "koʻp. Roppa-rosa 15 oʻquvchi boʻlsa ham shart "
                       "bajariladi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Sherbekda 200 000 soʻm bor. Borish-kelish yoʻl kirasi 45 000 "
                "soʻm, har bir kunga esa 20 000 soʻm ketadi.</p><p><strong>Koʻpi "
                "bilan necha kun qola oladi?</strong></p>",
        "choices": ["6 kun", "7 kun", "8 kun", "10 kun"],
        "correct": "7 kun",
        "explanation": "<p><strong>7 kun.</strong> 45 000 + 20 000k ≤ 200 000 → "
                       "20 000k ≤ 155 000 → k ≤ 7,75. Kun butun boʻlgani uchun 7. "
                       "Tekshirish: 8 kun boʻlsa 205 000 soʻm — pul yetmaydi.</p>",
    },
    {
        "text": "<p>Bir daftar 6000 soʻm. Afsonada 50 000 soʻm bor va u 10 000 "
                "soʻmlik ruchka ham olmoqchi.</p><p><strong>Koʻpi bilan nechta "
                "daftar ola oladi?</strong></p>",
        "choices": ["5 ta", "6 ta", "7 ta", "8 ta"],
        "correct": "6 ta",
        "explanation": "<p><strong>6 ta.</strong> 10 000 + 6000d ≤ 50 000 → "
                       "6000d ≤ 40 000 → d ≤ 6,66… Daftar butun boʻlgani uchun 6 ta. "
                       "Tekshirish: 46 000 ≤ 50 000 ✓; 7 ta boʻlsa 52 000 — "
                       "yetmaydi.</p>",
    },
]


# =====================================================================
# PM-41 — modul
# =====================================================================

Q_PM41 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>|7| = ?</strong></p>",
        "choices": ["−7", "0", "7", "14"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Musbat sonning moduli oʻzi: u noldan "
                       "yetti qadam narida.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>|−12| = ?</strong></p>",
        "choices": ["−12", "0", "12", "24"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Modul — noldan masofa, u manfiy "
                       "boʻlmaydi. −12 ham noldan oʻn ikki qadam narida.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>|0| = ?</strong></p>",
        "choices": ["0", "1", "−1", "aniqlanmagan"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Nol nolning oʻzida turibdi — masofa "
                       "nolga teng.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Modul nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Sonning noldan masofasini",
            "Sonning qarama-qarshisini",
            "Sonning kvadratini",
            "Sonning yarmini",
        ],
        "correct": "Sonning noldan masofasini",
        "explanation": "<p><strong>Noldan masofa.</strong> Yoʻnalish hisobga "
                       "olinmaydi, shuning uchun |5| va |−5| bir xil javob "
                       "beradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Modul manfiy boʻlishi "
                "mumkinmi?</strong></p>",
        "choices": [
            "Ha, agar son manfiy boʻlsa",
            "Yoʻq — masofa manfiy boʻlmaydi",
            "Ha, agar ichida ayirish boʻlsa",
            "Faqat nolda mumkin",
        ],
        "correct": "Yoʻq — masofa manfiy boʻlmaydi",
        "explanation": "<p><strong>Hech qachon.</strong> «Minus uch qadam "
                       "uzoqlikda» degan gap maʼnosiz. Modul doim noldan katta yoki "
                       "unga teng.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>|4 − 9| = ?</strong></p>",
        "choices": ["−5", "5", "13", "36"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Avval ichidagi: 4 − 9 = −5; keyin "
                       "modul: |−5| = 5. Modul chizigʻi qavs vazifasini "
                       "bajaradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>|3| − |8| = ?</strong></p>",
        "choices": ["−5", "5", "11", "−11"],
        "correct": "−5",
        "explanation": "<p><strong>−5.</strong> Bu safar modullar ALOHIDA olinadi: "
                       "3 − 8 = −5. Diqqat: |3 − 8| esa 5 ga teng — belgilarning "
                       "oʻrni javobni oʻzgartiradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>|−6| + |−4| = ?</strong></p>",
        "choices": ["−10", "2", "10", "24"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> Har bir modul alohida: 6 + 4 = 10.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Ikki son: 8 va −5.</p><p><strong>Ular "
                "orasidagi masofa qancha?</strong></p>",
        "choices": ["3", "13", "40", "−13"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> |8 − (−5)| = |13| = 13. Nolning ikki "
                       "tomonidagi sonlar boʻlgani uchun modullar qoʻshiladi: "
                       "8 + 5.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>|x| = 9 tenglamaning yechimi "
                "nima?</strong></p>",
        "choices": ["x = 9", "x = −9", "x = 9 yoki x = −9", "Yechimi yoʻq"],
        "correct": "x = 9 yoki x = −9",
        "explanation": "<p><strong>Ikkita yechim.</strong> Noldan toʻqqiz qadam "
                       "narida ikkita nuqta bor: biri oʻngda, biri chapda. Faqat "
                       "bittasini yozish — yarim javob.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>|x| = 0 tenglamaning nechta "
                "yechimi bor?</strong></p>",
        "choices": ["Bitta", "Ikkita", "Uchta", "Cheksiz koʻp"],
        "correct": "Bitta",
        "explanation": "<p><strong>Bitta:</strong> x = 0. Noldan nol qadam "
                       "uzoqlikdagi yagona son — nolning oʻzi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>|−3| · |−4| = ?</strong></p>",
        "choices": ["−12", "−7", "7", "12"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Avval modullar: 3 va 4; keyin "
                       "koʻpaytiramiz: 3 × 4 = 12. Modullar musbat boʻlgani uchun "
                       "javob ham musbat.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>|3 − 8| va |3| − |8| "
                "qiymatlari qanday?</strong></p>",
        "choices": ["5 va −5", "−5 va 5", "Ikkalasi ham 5", "Ikkalasi ham −5"],
        "correct": "5 va −5",
        "explanation": "<p><strong>5 va −5.</strong> Birinchisida modul chizigʻi "
                       "butun ayirmani qamrab oladi, ikkinchisida esa har son "
                       "alohida modulga olinadi. Belgining oʻrni muhim.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>|x| = −3 tenglamaning "
                "yechimi bormi?</strong></p>",
        "choices": [
            "Yoʻq — modul manfiy boʻlolmaydi",
            "Ha, x = −3",
            "Ha, x = 3 yoki x = −3",
            "Ha, x = 3",
        ],
        "correct": "Yoʻq — modul manfiy boʻlolmaydi",
        "explanation": "<p><strong>Yechimi yoʻq.</strong> Masofa manfiy boʻla "
                       "olmaydi, shuning uchun hech qanday son bu tenglamani rost "
                       "qilmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi tenglik "
                "notoʻgʻri?</strong></p>",
        "choices": ["|−8| = 8", "|8| = |−8|", "|−8| = −8", "|0| = 0"],
        "correct": "|−8| = −8",
        "explanation": "<p><strong>|−8| = −8</strong> notoʻgʻri: modul manfiy "
                       "boʻlmaydi, toʻgʻrisi 8. Qolgan uchtasi rost.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Muzxonada −18 gradus, xonada +22 "
                "gradus.</p><p><strong>Ular orasidagi farq necha gradus?</strong></p>",
        "choices": ["4 gradus", "22 gradus", "40 gradus", "−40 gradus"],
        "correct": "40 gradus",
        "explanation": "<p><strong>40 gradus.</strong> |22 − (−18)| = |40| = 40. "
                       "<strong>4 gradus</strong> — manfiyni ayirish qoidasini "
                       "unutib, 22 − 18 qilishdan chiqadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>|5 − 12| = |5| − |12| = "
                "−7</strong></p>",
        "choices": [
            "Avval ichidagi hisoblanadi: |−7| = 7",
            "Modul ichida ayirish mumkin emas",
            "Javob −17 boʻlishi kerak",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Avval ichidagi hisoblanadi: |−7| = 7",
        "explanation": "<p><strong>7.</strong> Modul chizigʻi qavs kabi ishlaydi: "
                       "5 − 12 = −7, keyin modul olinadi. Va javob manfiy chiqishi "
                       "allaqachon xato ekanini koʻrsatib turibdi.</p>",
    },
    {
        "text": "<p>Qaysi javob toʻliq?</p><p><strong>|x| = 7</strong></p>",
        "choices": ["x = 7", "x = −7", "x = 7 yoki x = −7", "x = 0"],
        "correct": "x = 7 yoki x = −7",
        "explanation": "<p><strong>Ikkita yechim.</strong> Faqat musbatini yozish — "
                       "eng koʻp uchraydigan tushib qolish. Son oʻqida chegara "
                       "nuqtalari ikkita.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Bir kuni kunduzi harorat +8 gradus, kechasi −5 gradus boʻldi. "
                "Ertasi kuni kunduzi +3, kechasi −1 gradus.</p><p><strong>Birinchi "
                "kunning farqi ikkinchisinikidan qanchaga katta?</strong></p>",
        "choices": ["4 gradusga", "9 gradusga", "13 gradusga", "17 gradusga"],
        "correct": "9 gradusga",
        "explanation": "<p><strong>9 gradusga.</strong> 1-kun: |8 − (−5)| = 13; "
                       "2-kun: |3 − (−1)| = 4. Farqi 13 − 4 = 9 gradus.</p>",
    },
    {
        "text": "<p>Zavodda detal uzunligi 50 mm boʻlishi kerak. Chetlanish koʻpi "
                "bilan 2 mm boʻlsa, detal yaroqli.</p><p><strong>Qaysi detal "
                "yaroqsiz?</strong></p>",
        "choices": ["48 mm", "49 mm", "51 mm", "53 mm"],
        "correct": "53 mm",
        "explanation": "<p><strong>53 mm.</strong> Chetlanish |uzunlik − 50| bilan "
                       "oʻlchanadi: |53 − 50| = 3, bu 2 dan katta. Qolganlarida "
                       "chetlanish 2, 1 va 1 mm — hammasi yaroqli.</p>",
    },
]


# =====================================================================
# PM-42 — daraja qonunlari
# =====================================================================

Q_PM42 = [
    # 1–5 tanish
    {
        "text": "<p>Daraja koʻrinishida yozing.</p><p><strong>2<sup>3</sup> · "
                "2<sup>4</sup> = ?</strong></p>",
        "choices": ["2^7", "2^12", "4^7", "2^1"],
        "correct": "2^7",
        "explanation": "<p><strong>2^7.</strong> Asoslar bir xil — koʻrsatkichlar "
                       "qoʻshiladi: 3 + 4 = 7. Tekshirish: 8 × 16 = 128 va "
                       "2^7 = 128 ✓</p>",
    },
    {
        "text": "<p>Daraja koʻrinishida yozing.</p><p><strong>3<sup>5</sup> ÷ "
                "3<sup>2</sup> = ?</strong></p>",
        "choices": ["3^3", "3^7", "3^10", "1^3"],
        "correct": "3^3",
        "explanation": "<p><strong>3^3 = 27.</strong> Boʻlishda koʻrsatkichlar "
                       "ayiriladi: 5 − 2 = 3. Tekshirish: 243 ÷ 9 = 27 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(2<sup>3</sup>)<sup>2</sup> = ?</strong></p>",
        "choices": ["2^5", "2^6", "2^9", "4^3"],
        "correct": "2^6",
        "explanation": "<p><strong>2^6 = 64.</strong> Darajani darajaga "
                       "koʻtarganda koʻrsatkichlar koʻpaytiriladi: 3 × 2 = 6. "
                       "Tekshirish: 8 kvadrat = 64 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>5<sup>0</sup> = ?</strong></p>",
        "choices": ["0", "1", "5", "aniqlanmagan"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> Har qanday sonning nolinchi darajasi "
                       "bir. Sababi: 5^2 ÷ 5^2 = 25 ÷ 25 = 1, qonun boʻyicha esa "
                       "5^0.</p>",
    },
    {
        "text": "<p>Standart koʻrinishda yozing.</p><p><strong>7 000 000 = ?</strong></p>",
        "choices": ["7 × 10^5", "7 × 10^6", "7 × 10^7", "70 × 10^5"],
        "correct": "7 × 10^6",
        "explanation": "<p><strong>7 × 10^6.</strong> Yettidan keyin oltita nol bor. "
                       "<strong>70 × 10^5</strong> ham shu songa teng, lekin "
                       "standart koʻrinishda birinchi son 1 dan 10 gacha boʻlishi "
                       "kerak.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>3<sup>2</sup> · 3<sup>4</sup> = ?</strong></p>",
        "choices": ["81", "243", "729", "6561"],
        "correct": "729",
        "explanation": "<p><strong>729.</strong> 3^(2+4) = 3^6 = 729. Tekshirish: "
                       "9 × 81 = 729 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>5<sup>7</sup> ÷ 5<sup>5</sup> = ?</strong></p>",
        "choices": ["5", "25", "125", "3125"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> 5^(7−5) = 5^2 = 25.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(10<sup>2</sup>)<sup>3</sup> = ?</strong></p>",
        "choices": ["100 000", "1 000 000", "10 000 000", "1000"],
        "correct": "1 000 000",
        "explanation": "<p><strong>1 000 000.</strong> 10^(2×3) = 10^6, yaʼni oltita "
                       "nol.</p>",
    },
    {
        "text": "<p>Daraja koʻrinishida yozing.</p><p><strong>a<sup>5</sup> · a "
                "= ?</strong></p>",
        "choices": ["a^5", "a^6", "a^25", "2a^5"],
        "correct": "a^6",
        "explanation": "<p><strong>a^6.</strong> Yolgʻiz a — bu a^1, demak "
                       "5 + 1 = 6. Koʻrinmayotgan koʻrsatkich har doim 1.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2<sup>−3</sup> = ?</strong></p>",
        "choices": ["−8", "−6", "1/8", "8"],
        "correct": "1/8",
        "explanation": "<p><strong>1/8.</strong> Manfiy koʻrsatkich maxrajga "
                       "tushishni bildiradi: 2^2 ÷ 2^5 = 4 ÷ 32 = 1/8, qonun bilan "
                       "esa 2^(−3). Javob manfiy emas, kasr.</p>",
    },
    {
        "text": "<p>Standart koʻrinishda yozing.</p><p><strong>150 000 000 = ?</strong></p>",
        "choices": ["1,5 × 10^7", "1,5 × 10^8", "15 × 10^7", "1,5 × 10^9"],
        "correct": "1,5 × 10^8",
        "explanation": "<p><strong>1,5 × 10^8.</strong> Vergulni birinchi raqamdan "
                       "keyin qoʻyamiz va uni sakkiz xona surganimizni sanaymiz. Bu "
                       "— Yerdan Quyoshgacha boʻlgan masofa (km).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(2 × 5)<sup>3</sup> = ?</strong></p>",
        "choices": ["30", "125", "1000", "10 000"],
        "correct": "1000",
        "explanation": "<p><strong>1000.</strong> Avval qavs: 10^3 = 1000. Yoki "
                       "qonun bilan: 2^3 × 5^3 = 8 × 125 = 1000 ✓ Ikki yoʻl bir xil "
                       "javob beradi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Hisoblang.</p><p><strong>2<sup>3</sup> + 2<sup>4</sup> va "
                "2<sup>3</sup> · 2<sup>4</sup> qiymatlari qanday?</strong></p>",
        "choices": ["24 va 128", "128 va 24", "Ikkalasi ham 128", "Ikkalasi ham 24"],
        "correct": "24 va 128",
        "explanation": "<p><strong>24 va 128.</strong> Qoʻshishda qonun yoʻq — "
                       "shunchaki hisoblaymiz: 8 + 16 = 24. Koʻrsatkichlar faqat "
                       "KOʻPAYTIRISHDA qoʻshiladi: 2^7 = 128.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2<sup>3</sup> · "
                "3<sup>4</sup> ni bitta daraja qilib yozish mumkinmi?</strong></p>",
        "choices": [
            "Yoʻq — asoslar har xil",
            "Ha, 6^7 boʻladi",
            "Ha, 6^12 boʻladi",
            "Ha, 5^7 boʻladi",
        ],
        "correct": "Yoʻq — asoslar har xil",
        "explanation": "<p><strong>Mumkin emas.</strong> Koʻrsatkichlarni qoʻshish "
                       "qoidasi faqat asoslar bir xil boʻlganda ishlaydi. Bu yerda "
                       "javob shunchaki 8 × 81 = 648.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3<sup>2</sup> · "
                "4<sup>2</sup> nechaga teng?</strong></p>",
        "choices": ["12^2", "12^4", "7^2", "7^4"],
        "correct": "12^2",
        "explanation": "<p><strong>12^2 = 144.</strong> Koʻrsatkichlar bir xil "
                       "boʻlsa, asoslar koʻpaytiriladi, koʻrsatkich oʻzgarmaydi. "
                       "Tekshirish: 9 × 16 = 144 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son eng "
                "katta?</strong></p>",
        "choices": ["2^5", "3^3", "5^2", "10^1"],
        "correct": "2^5",
        "explanation": "<p><strong>2^5 = 32.</strong> Har birini hisoblaymiz: "
                       "2^5 = 32, 3^3 = 27, 5^2 = 25, 10^1 = 10. Eʼtibor bering — "
                       "asos eng kichigi (2) eng katta natijani berdi, chunki "
                       "koʻrsatkich kattaroq. Darajada koʻrsatkich asosdan "
                       "kuchliroq taʼsir qiladi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>2<sup>3</sup> · "
                "2<sup>4</sup> = 2<sup>12</sup></strong></p>",
        "choices": [
            "Koʻpaytirishda koʻrsatkichlar qoʻshiladi: 2^7",
            "Asoslarni ham koʻpaytirish kerak edi: 4^7",
            "Javob 2^1 boʻlishi kerak",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Koʻpaytirishda koʻrsatkichlar qoʻshiladi: 2^7",
        "explanation": "<p><strong>2^7 = 128.</strong> Koʻrsatkichlar qoʻshiladi, "
                       "koʻpaytmaydi. Tekshirish: 8 × 16 = 128, 2^12 esa 4096.</p>",
    },
    {
        "text": "<p>Qaysi tenglik toʻgʻri?</p><p><strong>Nolinchi daraja</strong></p>",
        "choices": ["7^0 = 0", "7^0 = 1", "7^0 = 7", "0^0 = 7"],
        "correct": "7^0 = 1",
        "explanation": "<p><strong>7^0 = 1.</strong> Sababi boʻlish qonunida: "
                       "7^3 ÷ 7^3 = 1 va u 7^(3−3) = 7^0 ga teng. Demak nolinchi "
                       "daraja bir boʻlishi shart.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Yorugʻlik sekundiga 3 × 10<sup>5</sup> km yuradi. Yerdan "
                "Quyoshgacha 1,5 × 10<sup>8</sup> km.</p><p><strong>Quyosh nuri "
                "Yerga necha sekundda yetib keladi?</strong></p>",
        "choices": ["50 sekund", "500 sekund", "5000 sekund", "50 000 sekund"],
        "correct": "500 sekund",
        "explanation": "<p><strong>500 sekund.</strong> t = S ÷ v = "
                       "(1,5 ÷ 3) × 10^(8−5) = 0,5 × 10^3 = 500. Bu taxminan "
                       "8 daqiqa 20 sekund — haqiqiy qiymat.</p>",
    },
    {
        "text": "<p>Bir bakteriya har soatda ikkiga boʻlinadi. Boshida bitta "
                "bakteriya bor edi.</p><p><strong>10 soatdan keyin nechta "
                "boʻladi?</strong></p>",
        "choices": ["20 ta", "100 ta", "512 ta", "1024 ta"],
        "correct": "1024 ta",
        "explanation": "<p><strong>1024 ta.</strong> Har soat ikki barobar: "
                       "2^10 = 1024. <strong>20</strong> — qoʻshish deb "
                       "oʻylashdan, <strong>512</strong> esa 2^9 dan (bir soat kam "
                       "sanashdan) chiqadi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-40 Mashq: Tengsizlik",
        "description": "20 savol — belgilarni oʻqish, «kamida» va «koʻpi bilan», "
                       "tengsizlikni yechish va manfiy songa boʻlishda ishora.",
        "tutorial":    "PM-40:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM40,
    },
    {
        "title":       "PM-41 Mashq: Modul",
        "description": "20 savol — modul masofa sifatida, ikki son orasidagi masofa "
                       "va |x| = a koʻrinishidagi tenglamalar.",
        "tutorial":    "PM-41:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM41,
    },
    {
        "title":       "PM-42 Mashq: Daraja qonunlari",
        "description": "20 savol — koʻrsatkichlarni qoʻshish va ayirish, darajani "
                       "darajaga koʻtarish, nolinchi daraja va standart koʻrinish.",
        "tutorial":    "PM-42:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM42,
    },
]
