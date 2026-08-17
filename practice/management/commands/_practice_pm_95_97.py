# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-95, PM-96, PM-97 (mantiqiy jadval;
juftlik; Dirixle prinsipi). Blok H ning boshlanishi.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: uchalasi ham `hard`.

⚠️ BLOK H — hisoblash emas, MULOHAZA. Shuning uchun bu yerdagi
   «matnli masala» ham hisob emas, xulosa chiqarish boʻladi.
⚠️ `choices` EKRANLANADI — HTML teg yoʻq.
⚠️ Kumulyativ:
   • PM-95 — 3×3 va 4×4 mantiqiy jadval. Hamma mantiqiy masalaning
     yechimi YAGONA ekani verify skriptda tekshirilgan;
   • PM-96 — juft-toq, invariant, doskani boʻyash, qoʻl berish
     lemmasi;
   • PM-97 — Dirixle prinsipi, eng yomon hol, k × (m − 1) + 1.
⚠️ Distraktorlar — haqiqiy xatolar: «X bilan Y birga keldi» ni ✓ deb
   oʻqish, toq + toq = toq, ±2 juftlikni oʻzgartiradi deb oʻylash,
   qoʻl berishlar yigʻindisini ikkiga boʻlmaslik, eng yomon holni
   sanamaslik, n ÷ k ni pastga yaxlitlash, Dirixledan «kimligi»ni
   soʻrash.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_95_97.py --master=prime \\
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


# =====================================================================
# PM-95 — mantiqiy masalalar va jadval usuli
# =====================================================================

Q_PM95 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Mantiqiy "
                "jadvalda har bir qatorda nechta ✓ boʻladi?</strong></p>",
        "choices": ["Bittasi", "Ikkitasi", "Uchtasi", "Har xil"],
        "correct": "Bittasi",
        "explanation": "<p><strong>Bittasi.</strong> Har bir odamda bitta "
                       "kasb, har bir kasb bitta odamda. Shuning uchun "
                       "har qatorda ham, har ustunda ham roppa-rosa "
                       "bitta ✓ boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Katakka ✓ qoʻyildi.</p>"
                "<p><strong>Keyin nima qilinadi?</strong></p>",
        "choices": [
            "Hech narsa, keyingi shartga oʻtiladi",
            "Oʻsha qator va ustunning qolganiga ✗ qoʻyiladi",
            "Faqat oʻsha qatorga ✗ qoʻyiladi",
            "Jadval qaytadan chiziladi",
        ],
        "correct": "Oʻsha qator va ustunning qolganiga ✗ qoʻyiladi",
        "explanation": "<p><strong>Qator va ustunning qolganiga ✗.</strong> "
                       "Oʻchirmasangiz keyingi qadam koʻrinmaydi. "
                       "Faqat qatorni oʻchirish esa yarim ish — "
                       "ustundagi maʼlumot yoʻqoladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Shifokor Bekzod bilan "
                "birga keldi».</p><p><strong>Bu jadvalga qanday "
                "tushadi?</strong></p>",
        "choices": [
            "Bekzod shifokor ✓",
            "Bekzod shifokor emas ✗",
            "Bekzod shifokorning doʻsti ✓",
            "Hech qanday belgi bermaydi",
        ],
        "correct": "Bekzod shifokor emas ✗",
        "explanation": "<p><strong>Bekzod shifokor emas ✗.</strong> Gap "
                       "ikki har xil odam haqida: Bekzod va shifokor "
                       "birga kelgan, demak ular bir odam emas. Bunday "
                       "gaplar har doim ✗ beradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Uch odam va uch kasb "
                "boʻlsa, jami nechta joylashtirish mumkin?</strong></p>",
        "choices": ["3 ta", "6 ta", "9 ta", "27 ta"],
        "correct": "6 ta",
        "explanation": "<p><strong>6 ta.</strong> 3 × 2 × 1 = 6 "
                       "(PM-82). <strong>9</strong> — 3 × 3 qilinganda "
                       "chiqadi, lekin bir kasbni ikki odamga berib "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Jadvalning bir "
                "qatorida uchta katakdan ikkitasi ✗.</p><p><strong>Uchinchi "
                "katak haqida nima deyish mumkin?</strong></p>",
        "choices": [
            "U ✓ boʻladi",
            "U ham ✗ boʻlishi mumkin",
            "Buni aniqlab boʻlmaydi",
            "Jadval notoʻgʻri tuzilgan",
        ],
        "correct": "U ✓ boʻladi",
        "explanation": "<p><strong>U ✓ boʻladi.</strong> Har qatorda "
                       "roppa-rosa bitta ✓ boʻlishi shart. Ikkitasi "
                       "oʻchgan ekan, qolgan yagona katak javob "
                       "boʻladi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Afsona, Bekzod va Dilnoza — "
                "qizil, koʻk va yashil koʻylakda. Afsona na qizil, na "
                "koʻk kiygan. Dilnoza koʻk kiymagan.</p><p><strong>Bekzod "
                "qanday rangda?</strong></p>",
        "choices": ["Qizil", "Koʻk", "Yashil", "Aniqlab boʻlmaydi"],
        "correct": "Koʻk",
        "explanation": "<p><strong>Koʻk.</strong> Afsona faqat yashil "
                       "kiyishi mumkin ✓ Yashil ustuni yopildi. Dilnoza "
                       "koʻk emas, demak Dilnoza qizil. Bekzodga koʻk "
                       "qoladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Jasur, Nodira va Sherbek — "
                "5, 6 va 7-sinfda. Jasur 6-sinfda. Sherbek Nodiradan "
                "katta sinfda.</p><p><strong>Nodira qaysi "
                "sinfda?</strong></p>",
        "choices": ["5-sinfda", "6-sinfda", "7-sinfda",
                    "Aniqlab boʻlmaydi"],
        "correct": "5-sinfda",
        "explanation": "<p><strong>5-sinfda.</strong> Jasur 6-sinfda ekan, "
                       "Nodira va Sherbekka 5 va 7 qoladi. Sherbek "
                       "Nodiradan katta boʻlgani uchun Sherbek — 7, "
                       "Nodira — 5.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Uch bola — Bekzod, Jasur, "
                "Sherbek — futbol, shaxmat va suzish bilan "
                "shugʻullanadi. Bekzod shaxmat oʻynamaydi. Shaxmatchi "
                "Jasurning doʻsti. Bekzod suzmaydi.</p><p><strong>Kim "
                "shaxmat oʻynaydi?</strong></p>",
        "choices": ["Bekzod", "Jasur", "Sherbek", "Aniqlab boʻlmaydi"],
        "correct": "Sherbek",
        "explanation": "<p><strong>Sherbek.</strong> «Shaxmatchi "
                       "Jasurning doʻsti» → Jasur shaxmatchi emas. "
                       "Bekzod ham emas, demak Sherbek ✓ Shaxmat ustuni "
                       "yopilgach: Bekzod suzmaydi → Bekzod futbol, "
                       "Jasurga suzish qoladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Toʻrt bola toʻrt xil meva "
                "oldi: olma, nok, uzum, anor. Afsona anor oldi. Bekzod na "
                "olma, na nok oldi. Dilnoza nok olmadi.</p>"
                "<p><strong>Sherbek qaysi mevani olgan?</strong></p>",
        "choices": ["Olma", "Nok", "Uzum", "Anor"],
        "correct": "Nok",
        "explanation": "<p><strong>Nok.</strong> Afsona anor ✓ — ustun "
                       "yopildi. Bekzod olma ✗, nok ✗, anor ✗ → uzum ✓ "
                       "Dilnoza nok emas, uzum va anor band → olma ✓ "
                       "Sherbekka nok qoladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Uch qoʻshni — Karim, Nodira, "
                "Bekzod — 1, 2 va 3-qavatda yashaydi. Nodira Karimdan "
                "pastda, Bekzod esa Karimdan yuqorida yashaydi.</p>"
                "<p><strong>Kim 3-qavatda?</strong></p>",
        "choices": ["Karim", "Nodira", "Bekzod", "Aniqlab boʻlmaydi"],
        "correct": "Bekzod",
        "explanation": "<p><strong>Bekzod.</strong> Nodira &lt; Karim &lt; Bekzod "
                       "degan zanjir uchala oʻrinni bir yoʻla "
                       "aniqlaydi: Nodira — 1, Karim — 2, Bekzod — 3. "
                       "Taqqoslash shartlari shuning uchun eng "
                       "foydali: bittasi bir necha katakni "
                       "oʻchiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Jadvalni toʻldirib "
                "boʻlgach, ikkita boʻsh katak qoldi va ikkalasi ham "
                "mumkin.</p><p><strong>Bu nimani bildiradi?</strong></p>",
        "choices": [
            "Yechim yoʻq",
            "Shartlardan biri ishlatilmagan yoki yetishmayapti",
            "Jadval notoʻgʻri chizilgan",
            "Ikkala javob ham toʻgʻri",
        ],
        "correct": "Shartlardan biri ishlatilmagan yoki yetishmayapti",
        "explanation": "<p><strong>Shartlardan biri ishlatilmagan yoki "
                       "yetishmayapti.</strong> Avval hamma shartni "
                       "qaytadan oʻqing. Agar hammasi ishlatilgan "
                       "boʻlsa, demak maʼlumot yetarli emas "
                       "(PM-94).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Jasur shifokordan "
                "yosh».</p><p><strong>Bu shartdan nechta belgi "
                "chiqadi?</strong></p>",
        "choices": [
            "Bitta: Jasur shifokor emas",
            "Ikkita: Jasur shifokor emas va shifokor eng yosh emas",
            "Hech qanday belgi chiqmaydi",
            "Uchta belgi",
        ],
        "correct": "Ikkita: Jasur shifokor emas va shifokor eng yosh emas",
        "explanation": "<p><strong>Ikkita.</strong> Odam oʻzidan yosh "
                       "boʻlolmaydi → Jasur shifokor emas. Va kimdir "
                       "undan yosh ekan → shifokor eng yosh emas. "
                       "Taqqoslash shartlari eng foydali "
                       "shartlardir.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Mantiqiy "
                "masalada nima qilinadi?</strong></p>",
        "choices": [
            "Hisoblash",
            "Imkonsiz variantlarni chiqarib tashlash",
            "Taxmin qilish",
            "Formulaga qoʻyish",
        ],
        "correct": "Imkonsiz variantlarni chiqarib tashlash",
        "explanation": "<p><strong>Imkonsiz variantlarni chiqarib "
                       "tashlash.</strong> Bu yerda qoʻshiladigan yoki "
                       "koʻpaytiriladigan hech narsa yoʻq. Har bir "
                       "shart bir nechta variantni oʻchiradi, oxirida "
                       "bittasi qoladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi biri "
                "xulosa, qaysi biri taxmin?</strong></p>",
        "choices": [
            "«Karim shifokor emas» — taxmin",
            "«Karim muhandis boʻlsa kerak» — xulosa",
            "«Karim shifokor emas» — xulosa, «boʻlsa kerak» — taxmin",
            "Ikkalasi ham xulosa",
        ],
        "correct": "«Karim shifokor emas» — xulosa, «boʻlsa kerak» — taxmin",
        "explanation": "<p><strong>Birinchisi xulosa, ikkinchisi "
                       "taxmin.</strong> Xulosa shartdan kelib chiqadi "
                       "va isbotlangan. «Boʻlsa kerak» esa hali "
                       "isbotlanmagan. Jadvalda faqat xulosalar "
                       "yoziladi — har birining yoniga qaysi shartdan "
                       "chiqqanini belgilab qoʻying.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Jadvalda bir ustunda "
                "ikkita ✓ paydo boʻldi.</p><p><strong>Nima "
                "boʻlgan?</strong></p>",
        "choices": [
            "Xato qilingan",
            "Bu normal holat",
            "Masala ikkita yechimga ega",
            "Bitta shart ortiqcha",
        ],
        "correct": "Xato qilingan",
        "explanation": "<p><strong>Xato qilingan.</strong> Har bir kasb "
                       "faqat bitta odamga tegishli. Ikkita ✓ — "
                       "ziddiyat; orqaga qaytib tekshirish kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Javobni "
                "topgandan keyin nima qilish kerak?</strong></p>",
        "choices": [
            "Faqat oxirgi shartni tekshirish",
            "Hech narsa, javob tayyor",
            "Hamma shart boʻyicha tekshirish",
            "Jadvalni oʻchirib tashlash",
        ],
        "correct": "Hamma shart boʻyicha tekshirish",
        "explanation": "<p><strong>Hamma shart boʻyicha.</strong> "
                       "Yechimni har bir shartga qaytarib qoʻying. "
                       "Bitta shart bajarilmasa, yoʻlning bir joyida "
                       "xato bor.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>«Oʻqituvchi Dilnozaning "
                "qoʻshnisi» degan shartni oʻqib, oʻquvchi jadvalga "
                "«Dilnoza — oʻqituvchi ✓» deb yozdi.</p><p><strong>Nima "
                "notoʻgʻri?</strong></p>",
        "choices": [
            "Shart aksini bildiradi: Dilnoza oʻqituvchi emas",
            "✓ oʻrniga ✗ qoʻyish kerak edi, lekin maʼnosi oʻsha",
            "Shart hech qanday maʼlumot bermaydi",
            "Xato yoʻq",
        ],
        "correct": "Shart aksini bildiradi: Dilnoza oʻqituvchi emas",
        "explanation": "<p><strong>Shart aksini bildiradi.</strong> "
                       "Oʻqituvchi Dilnozaning qoʻshnisi ekan, demak "
                       "u Dilnozaning oʻzi emas — ular ikki har xil "
                       "odam. Bu xato butun yechimni buzadi.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Uch bola: A "
                "shifokor emas, B oʻqituvchi emas, C na shifokor, na "
                "muhandis. Kim shifokor?</strong></p>",
        "choices": [
            "A — chunki u birinchi",
            "B — chunki A va C shifokor emas",
            "C — chunki u oxirgi qoldi",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "B — chunki A va C shifokor emas",
        "explanation": "<p><strong>B.</strong> A shifokor emas (shart), "
                       "C ham shifokor emas (shart). Uch boladan "
                       "ikkitasi oʻchgan ekan, shifokor — B. Bu "
                       "ustun boʻyicha chiqarib tashlash: bir ustunda "
                       "ham bitta ✓ boʻladi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Toʻrt doʻst toʻrt xil "
                "shaharga bordi: Buxoro, Xiva, Samarqand, Namangan. "
                "Jasur Xivaga bordi. Afsona na Buxoro, na Samarqandga "
                "bordi. Bekzod Samarqandga bormadi.</p><p><strong>Bekzod "
                "qayerga borgan?</strong></p>",
        "choices": ["Buxoroga", "Xivaga", "Samarqandga", "Namanganga"],
        "correct": "Buxoroga",
        "explanation": "<p><strong>Buxoroga.</strong> Jasur — Xiva ✓, "
                       "ustun yopildi. Afsona Buxoro ✗, Samarqand ✗, "
                       "Xiva band → Afsona Namangan ✓ Bekzod Samarqand "
                       "✗, Xiva va Namangan band → Bekzod Buxoro ✓ "
                       "Toʻrtinchisiga Samarqand qoladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Uch qiz uch xil gul oldi: "
                "atirgul, lola, chinnigul. Chinnigul olgan qiz Afsona "
                "bilan birga keldi. Afsona atirgul olmadi. Dilnoza "
                "chinnigul olmadi.</p><p><strong>Nodira qaysi gulni "
                "olgan?</strong></p>",
        "choices": ["Atirgulni", "Lolani", "Chinnigulni",
                    "Aniqlab boʻlmaydi"],
        "correct": "Chinnigulni",
        "explanation": "<p><strong>Chinnigulni.</strong> «Chinnigul olgan "
                       "qiz Afsona bilan birga keldi» → Afsona "
                       "chinnigul olmagan. Afsona atirgul ham olmagan, "
                       "demak Afsona — lola ✓ Dilnoza chinnigul "
                       "olmagan va lola band, demak Dilnoza — "
                       "atirgul ✓ Nodiraga chinnigul qoladi.</p>",
    },
]


# =====================================================================
# PM-96 — juftlik (juft-toq) gʻoyasi
# =====================================================================

Q_PM96 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikkita toq "
                "sonning yigʻindisi qanday boʻladi?</strong></p>",
        "choices": ["Toq", "Juft", "Baʼzan toq, baʼzan juft",
                    "Har doim nol"],
        "correct": "Juft",
        "explanation": "<p><strong>Juft.</strong> (2a + 1) + (2b + 1) = "
                       "2(a + b + 1). Misol: 3 + 5 = 8, 7 + 9 = 16. Har "
                       "bir toq sondagi «ortiqcha bir» ikkitasi "
                       "qoʻshilganda juftlashadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Juft son "
                "bilan toq sonning yigʻindisi qanday?</strong></p>",
        "choices": ["Juft", "Toq", "Aniqlab boʻlmaydi", "Har doim 1"],
        "correct": "Toq",
        "explanation": "<p><strong>Toq.</strong> 2a + (2b + 1) = "
                       "2(a + b) + 1. Misol: 4 + 7 = 11.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Invariant "
                "nima?</strong></p>",
        "choices": [
            "Har bir harakatda oʻzgaradigan son",
            "Hech qanday harakatda oʻzgarmaydigan xossa",
            "Masalaning javobi",
            "Eng katta son",
        ],
        "correct": "Hech qanday harakatda oʻzgarmaydigan xossa",
        "explanation": "<p><strong>Hech qanday harakatda oʻzgarmaydigan "
                       "xossa.</strong> Boshlangʻich holat bilan "
                       "maqsadning invarianti farq qilsa, maqsadga "
                       "yetib boʻlmaydi — bu imkonsizlikning "
                       "isboti.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Stakanlardan roppa-rosa "
                "ikkitasi agʻdariladi.</p><p><strong>Agʻdarilganlar soni "
                "qanday oʻzgaradi?</strong></p>",
        "choices": ["−2, 0 yoki +2 ga", "Faqat +2 ga", "−1 yoki +1 ga",
                    "Umuman oʻzgarmaydi"],
        "correct": "−2, 0 yoki +2 ga",
        "explanation": "<p><strong>−2, 0 yoki +2 ga.</strong> Ikkalasi "
                       "agʻdarilgan boʻlsa −2; ikkalasi toʻgʻri boʻlsa "
                       "+2; aralash boʻlsa 0. Uchalasi ham juft son, "
                       "shuning uchun juft-toqlik saqlanadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1 + 2 + 3 + … + 10 "
                "yigʻindisi qanday son?</strong></p>",
        "choices": ["Juft — 55", "Toq — 55", "Juft — 50", "Toq — 45"],
        "correct": "Toq — 55",
        "explanation": "<p><strong>Toq — 55.</strong> Yigʻindi 55 ga teng "
                       "va u toq son. Shuning uchun belgilarni "
                       "almashtirib 0 chiqarib boʻlmaydi: 0 juft.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Stolda 7 ta stakan "
                "agʻdarilgan. Har safar roppa-rosa 2 tasi "
                "agʻdariladi.</p><p><strong>Hammasini toʻgʻrilash "
                "mumkinmi?</strong></p>",
        "choices": [
            "Ha, 4 ta harakatda",
            "Ha, lekin koʻp harakat kerak",
            "Yoʻq — 7 toq, harakatlar esa juft son bilan oʻzgartiradi",
            "Yoʻq — stakanlar juda kam",
        ],
        "correct": "Yoʻq — 7 toq, harakatlar esa juft son bilan oʻzgartiradi",
        "explanation": "<p><strong>Yoʻq.</strong> 7 — toq son. Har bir "
                       "harakat sonni −2, 0 yoki +2 ga oʻzgartiradi, "
                       "demak toqlik hech qachon buzilmaydi. Maqsad "
                       "esa 0 — juft son.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Stolda 10 ta stakan "
                "agʻdarilgan. Har safar 2 tasi agʻdariladi.</p>"
                "<p><strong>Hammasini toʻgʻrilash mumkinmi?</strong></p>",
        "choices": [
            "Ha — 5 ta harakat yetadi",
            "Yoʻq — invariant toʻsqinlik qiladi",
            "Ha, lekin 10 ta harakat kerak",
            "Faqat 3 tadan agʻdarilsa mumkin",
        ],
        "correct": "Ha — 5 ta harakat yetadi",
        "explanation": "<p><strong>Ha.</strong> 10 juft, maqsad 0 ham "
                       "juft — invariant toʻsqinlik qilmaydi. Har safar "
                       "boshqa ikkitasini agʻdarib, 5 ta harakatda "
                       "bitiriladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>1 dan 9 gacha sonlar oldiga "
                "«+» va «−» belgilari qoʻyiladi.</p><p><strong>Natijani "
                "0 ga tenglash mumkinmi?</strong></p>",
        "choices": [
            "Ha",
            "Yoʻq — yigʻindi 45, toq son",
            "Yoʻq — sonlar juda kam",
            "Faqat 1 ni tashlab yuborsa",
        ],
        "correct": "Yoʻq — yigʻindi 45, toq son",
        "explanation": "<p><strong>Yoʻq.</strong> 1 + 2 + … + 9 = 45 — "
                       "toq. Bitta «+» ni «−» ga almashtirish "
                       "yigʻindini 2k ga, yaʼni juft songa "
                       "oʻzgartiradi. Demak toqlik saqlanadi va 0 "
                       "(juft) ga yetib boʻlmaydi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sinfda 15 oʻquvchi bor.</p>"
                "<p><strong>Har biri roppa-rosa 5 kishi bilan qoʻl "
                "berishi mumkinmi?</strong></p>",
        "choices": [
            "Ha — 37 ta qoʻl berish boʻladi",
            "Ha — 75 ta qoʻl berish boʻladi",
            "Yoʻq — 15 × 5 = 75 toq son",
            "Yoʻq — 5 juda koʻp",
        ],
        "correct": "Yoʻq — 15 × 5 = 75 toq son",
        "explanation": "<p><strong>Yoʻq.</strong> Yigʻindi 15 × 5 = 75, "
                       "lekin u qoʻl berishlar sonining ikki barobari "
                       "boʻlishi — yaʼni juft boʻlishi kerak. Toq son "
                       "juft boʻlolmaydi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sinfda 12 oʻquvchi bor va har "
                "biri roppa-rosa 3 kishi bilan qoʻl berdi.</p>"
                "<p><strong>Nechta qoʻl berish boʻlgan?</strong></p>",
        "choices": ["12 ta", "18 ta", "36 ta", "72 ta"],
        "correct": "18 ta",
        "explanation": "<p><strong>18 ta.</strong> Yigʻindi 12 × 3 = 36 — "
                       "juft, demak toʻsiq yoʻq. Har bir qoʻl berish "
                       "ikki marta sanalgani uchun 36 ÷ 2 = 18. "
                       "<strong>36</strong> — ikki marta sanalgan "
                       "son.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>4 × 4 doskadan ikkita "
                "qarama-qarshi burchak olib tashlandi.</p><p><strong>Qolgan "
                "qismni 2 × 1 domino bilan qoplash mumkinmi?</strong></p>",
        "choices": [
            "Ha — 14 katak va 7 domino, sonlar mos",
            "Yoʻq — 6 ta sariq va 8 ta koʻk katak qoldi",
            "Ha — lekin faqat maxsus tartibda",
            "Yoʻq — kataklar soni toq",
        ],
        "correct": "Yoʻq — 6 ta sariq va 8 ta koʻk katak qoldi",
        "explanation": "<p><strong>Yoʻq.</strong> Har bir domino roppa-rosa "
                       "1 sariq va 1 koʻk katakni qoplaydi, demak ranglar "
                       "teng boʻlishi kerak. Kesilgan ikkala burchak "
                       "ham sariq edi: 6 ≠ 8. Kataklar soni mos "
                       "kelishi (14 = 7 × 2) yetarli emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Stolda 9 ta stakan "
                "agʻdarilgan. Endi har safar roppa-rosa 3 tasi "
                "agʻdariladi.</p><p><strong>Hammasini toʻgʻrilash "
                "mumkinmi?</strong></p>",
        "choices": [
            "Yoʻq — 9 toq son",
            "Yoʻq — invariant oʻzgarmaydi",
            "Ha — 3 ta harakat yetadi",
            "Ha — 9 ta harakat kerak",
        ],
        "correct": "Ha — 3 ta harakat yetadi",
        "explanation": "<p><strong>Ha.</strong> Uchtadan agʻdarilganda "
                       "juftlik har safar almashadi, demak toʻsiq "
                       "yoʻqoladi. 9 ÷ 3 = 3: har safar boshqa "
                       "uchtasini agʻdarsa, hamma stakan bir martadan "
                       "agʻdarilib toʻgʻri turadi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Men koʻp urindim, "
                "boʻlmadi».</p><p><strong>Bu isbotmi?</strong></p>",
        "choices": [
            "Ha, agar juda koʻp urinilgan boʻlsa",
            "Yoʻq — balki yoʻl bor, topilmagan",
            "Ha, chunki tajriba ishonchli",
            "Faqat sonlar katta boʻlganda",
        ],
        "correct": "Yoʻq — balki yoʻl bor, topilmagan",
        "explanation": "<p><strong>Yoʻq.</strong> Urinishlar isbot emas. "
                       "Invariant esa hamma yoʻlni bir yoʻla yopadi — "
                       "shuning uchun u isbot boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Masalada juftlik "
                "toʻsqinlik qilmadi (ikkalasi ham juft chiqdi).</p>"
                "<p><strong>Bu nimani bildiradi?</strong></p>",
        "choices": [
            "Maqsadga albatta yetiladi",
            "Toʻsiq yoʻq, lekin yoʻlni koʻrsatish kerak",
            "Masala yechilmaydi",
            "Yana bitta invariant qidirish shart",
        ],
        "correct": "Toʻsiq yoʻq, lekin yoʻlni koʻrsatish kerak",
        "explanation": "<p><strong>Toʻsiq yoʻq, lekin yoʻlni koʻrsatish "
                       "kerak.</strong> Juftlik faqat "
                       "<strong>imkonsizlikni</strong> isbotlaydi. "
                       "Mumkinligini isbotlash uchun aniq ketma-ketlik "
                       "keltirish kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Doskani "
                "boʻyash usuli nimaning koʻrinishi?</strong></p>",
        "choices": [
            "Koʻpaytirish prinsipining",
            "Juftlik gʻoyasining",
            "Dirixle prinsipining",
            "Oʻrtacha arifmetikning",
        ],
        "correct": "Juftlik gʻoyasining",
        "explanation": "<p><strong>Juftlik gʻoyasining.</strong> Ranglar "
                       "soni — invariant: har bir domino ikkalasidan "
                       "bittadan oladi. Bu — juft-toqlikning geometrik "
                       "koʻrinishi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Guruhda «har "
                "kim necha kishi bilan qoʻl berdi» sonlarining "
                "yigʻindisi qanday boʻladi?</strong></p>",
        "choices": [
            "Har doim juft",
            "Har doim toq",
            "Odamlar soniga teng",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Har doim juft",
        "explanation": "<p><strong>Har doim juft.</strong> Chunki bu "
                       "yigʻindi qoʻl berishlar sonining roppa-rosa "
                       "ikki barobari — har bir qoʻl berishda ikki "
                       "kishi qatnashadi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>Oʻquvchi yozdi: «Sinfda "
                "25 kishi, har biri 3 martadan qoʻl berdi, demak "
                "25 × 3 = 75 ta qoʻl berish boʻlgan».</p>"
                "<p><strong>Nima notoʻgʻri?</strong></p>",
        "choices": [
            "Koʻpaytirish notoʻgʻri hisoblangan",
            "Har bir qoʻl berish ikki marta sanalgan",
            "25 ni 3 ga boʻlish kerak edi",
            "Xato yoʻq",
        ],
        "correct": "Har bir qoʻl berish ikki marta sanalgan",
        "explanation": "<p><strong>Har bir qoʻl berish ikki marta "
                       "sanalgan.</strong> 75 — yigʻindi, qoʻl "
                       "berishlar soni emas; uni 2 ga boʻlish kerak. "
                       "75 ÷ 2 = 37,5 butun chiqmadi — demak bunday "
                       "holat umuman mumkin emas.</p>",
    },
    {
        "text": "<p>Qaysi mulohaza toʻgʻri?</p><p><strong>11 ta stakan "
                "agʻdarilgan, har safar 2 tasi agʻdariladi. Hammasini "
                "toʻgʻrilash mumkinmi?</strong></p>",
        "choices": [
            "Mumkin — 11 ta harakat kerak",
            "Mumkin emas — 11 toq, oʻzgarish esa har doim juft",
            "Mumkin emas — 11 tub son",
            "Mumkin — chunki 11 > 2",
        ],
        "correct": "Mumkin emas — 11 toq, oʻzgarish esa har doim juft",
        "explanation": "<p><strong>Mumkin emas.</strong> Sabab tub sonlikda "
                       "emas, <strong>toqlikda</strong>: har bir "
                       "harakat sonni juft miqdorga oʻzgartiradi, "
                       "demak toq son toq boʻlib qoladi va 0 ga "
                       "yetmaydi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Xonada 9 ta chiroq bor va "
                "hammasi oʻchiq. Bitta tugma bosilganda roppa-rosa "
                "2 ta chiroqning holati almashadi.</p><p><strong>Hamma "
                "chiroqni yoqish mumkinmi?</strong></p>",
        "choices": [
            "Ha — 4 marta bosish kerak",
            "Ha — 9 marta bosish kerak",
            "Yoʻq — oʻchiq chiroqlar soni har doim toq qoladi",
            "Yoʻq — chiroqlar juda koʻp",
        ],
        "correct": "Yoʻq — oʻchiq chiroqlar soni har doim toq qoladi",
        "explanation": "<p><strong>Yoʻq.</strong> Bu — stakanlar "
                       "masalasining oʻzi. Oʻchiq chiroqlar soni "
                       "boshida 9 (toq); har bosishda u −2, 0 yoki "
                       "+2 ga oʻzgaradi, demak toq boʻlib qoladi. "
                       "Maqsad esa 0 — juft.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Doirada 7 kishi oʻtiribdi. "
                "Har biri oʻzining ikkala qoʻshnisi bilan qoʻl "
                "berdi.</p><p><strong>Nechta qoʻl berish "
                "boʻlgan?</strong></p>",
        "choices": ["7 ta", "12 ta", "14 ta", "49 ta"],
        "correct": "7 ta",
        "explanation": "<p><strong>7 ta.</strong> Har kim 2 martadan qoʻl "
                       "berdi, yigʻindi 7 × 2 = 14 — juft ✓ Qoʻl "
                       "berishlar soni esa 14 ÷ 2 = 7. Buni doiradagi "
                       "qoʻshni juftliklar sonidan ham koʻrish "
                       "mumkin: 7 kishi — 7 ta qoʻshnilik.</p>",
    },
]


# =====================================================================
# PM-97 — Dirixle prinsipi
# =====================================================================

Q_PM97 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>5 ta kaptar 4 ta "
                "uyaga joylashdi.</p><p><strong>Nima deyish "
                "mumkin?</strong></p>",
        "choices": [
            "Kamida bitta uyada 2 ta kaptar bor",
            "Har bir uyada bittadan kaptar bor",
            "Bitta uya boʻsh qoladi",
            "Hech narsa deyish mumkin emas",
        ],
        "correct": "Kamida bitta uyada 2 ta kaptar bor",
        "explanation": "<p><strong>Kamida bitta uyada 2 ta.</strong> Agar "
                       "har uyada koʻpi bilan bitta boʻlsa, jami 4 ta "
                       "kaptar boʻlardi. Bizda esa 5 ta — "
                       "ziddiyat.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sinfda 13 oʻquvchi "
                "bor.</p><p><strong>Nima deyish mumkin?</strong></p>",
        "choices": [
            "Kamida ikkitasi bir oyda tugʻilgan",
            "Ikkitasi bir oyda tugʻilgan boʻlishi mumkin",
            "Hammasi har xil oyda tugʻilgan",
            "Buni faqat roʻyxatni koʻrib aytish mumkin",
        ],
        "correct": "Kamida ikkitasi bir oyda tugʻilgan",
        "explanation": "<p><strong>Kamida ikkitasi bir oyda.</strong> 13 ta "
                       "kaptar, 12 ta uya. Bu ehtimol emas — "
                       "<strong>kafolat</strong>: hech qanday "
                       "istisnosiz ishlaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Dirixle "
                "prinsipi nimani isbotlaydi?</strong></p>",
        "choices": [
            "Obyekt borligini",
            "Obyekt kimligini",
            "Obyekt qayerdaligini",
            "Obyekt nechtaligini aniq",
        ],
        "correct": "Obyekt borligini",
        "explanation": "<p><strong>Obyekt borligini.</strong> Bu — "
                       "mavjudlik isboti. Prinsip bunday obyekt "
                       "borligini kafolatlaydi, lekin uni topib "
                       "bermaydi va kimligini aytmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Qutida 3 xil rangdagi qalam "
                "bor.</p><p><strong>Kamida nechta olsa, ikkitasi bir xil "
                "rangda boʻlishi kafolatlanadi?</strong></p>",
        "choices": ["2 ta", "3 ta", "4 ta", "6 ta"],
        "correct": "4 ta",
        "explanation": "<p><strong>4 ta.</strong> Eng yomon hol — har "
                       "rangdan bittadan, yaʼni 3 ta. Toʻrtinchisi "
                       "albatta takrorlanadi. Formula: "
                       "3 × (2 − 1) + 1 = 4.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Savolda «kafolatlansin» "
                "deyilgan.</p><p><strong>Bu nimani talab qiladi?</strong>"
                "</p>",
        "choices": [
            "Eng omadli holni hisoblashni",
            "Eng yomon holni hisoblashni",
            "Oʻrtacha holni hisoblashni",
            "Ehtimolni hisoblashni",
        ],
        "correct": "Eng yomon holni hisoblashni",
        "explanation": "<p><strong>Eng yomon holni.</strong> Javob "
                       "<strong>har qanday</strong> holda ishlashi "
                       "kerak, omadga tayanmasligi shart. Shuning uchun "
                       "eng omadsiz taqsimot hisoblanadi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>Qutida 4 xil rangdagi shar bor.</p>"
                "<p><strong>Kamida nechta olsa, bir xil rangdagi 2 ta "
                "shar kafolatlanadi?</strong></p>",
        "choices": ["4 ta", "5 ta", "8 ta", "9 ta"],
        "correct": "5 ta",
        "explanation": "<p><strong>5 ta.</strong> 4 × (2 − 1) + 1 = 5. Eng "
                       "yomon hol — har rangdan bittadan (4 ta); "
                       "beshinchisi albatta takrorlaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Qutida 3 xil rangdagi shar bor.</p>"
                "<p><strong>Kamida nechta olsa, bir xil rangdagi 4 ta "
                "shar kafolatlanadi?</strong></p>",
        "choices": ["7 ta", "9 ta", "10 ta", "12 ta"],
        "correct": "10 ta",
        "explanation": "<p><strong>10 ta.</strong> 3 × (4 − 1) + 1 = 10. "
                       "Eng yomon hol — har rangdan 3 tadan (9 ta); "
                       "oʻninchisi biror rangni 4 taga yetkazadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Maktabda 30 oʻquvchi bor, yilda "
                "12 oy.</p><p><strong>Kamida nechtasi bir oyda "
                "tugʻilgan?</strong></p>",
        "choices": ["2 tasi", "3 tasi", "4 tasi", "12 tasi"],
        "correct": "3 tasi",
        "explanation": "<p><strong>3 tasi.</strong> 30 ÷ 12 = 2,5 → "
                       "yuqoriga yaxlitlab 3. Tekshirish: har oyda "
                       "koʻpi bilan 2 ta boʻlsa, jami 24 ta boʻlardi — "
                       "30 ta emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>50 ta son 7 ga boʻlinmoqda.</p>"
                "<p><strong>Kamida nechtasi bir xil qoldiq "
                "beradi?</strong></p>",
        "choices": ["6 tasi", "7 tasi", "8 tasi", "9 tasi"],
        "correct": "8 tasi",
        "explanation": "<p><strong>8 tasi.</strong> 7 ga boʻlganda qoldiq "
                       "0 dan 6 gacha — 7 xil (uyalar). "
                       "50 ÷ 7 ≈ 7,14 → yuqoriga yaxlitlab 8. "
                       "Tekshirish: har qoldiqdan koʻpi bilan 7 ta "
                       "boʻlsa, jami 49 ta boʻlardi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Qorongʻi xonada 10 qora va 10 oq "
                "paypoq bor.</p><p><strong>Kamida nechta olsa, bir xil "
                "rangdagi juft kafolatlanadi?</strong></p>",
        "choices": ["2 ta", "3 ta", "10 ta", "11 ta"],
        "correct": "3 ta",
        "explanation": "<p><strong>3 ta.</strong> Eng yomon hol — bittasi "
                       "qora, bittasi oq. Uchinchisi ikkala rangdan "
                       "biriga tushadi va juft hosil qiladi. "
                       "<strong>2 ta</strong> — omadga tayangan "
                       "javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Bir maktabda 400 oʻquvchi bor, yilda "
                "365 kun.</p><p><strong>Nima deyish mumkin?</strong></p>",
        "choices": [
            "Kamida 2 tasining tugʻilgan kuni bir xil",
            "Hammasining tugʻilgan kuni har xil",
            "Kamida 35 tasining tugʻilgan kuni bir xil",
            "Buni aytish mumkin emas",
        ],
        "correct": "Kamida 2 tasining tugʻilgan kuni bir xil",
        "explanation": "<p><strong>Kamida 2 tasining.</strong> 400 ta "
                       "kaptar, 365 ta uya. <strong>35</strong> — "
                       "400 − 365 dan chiqadi, lekin bu prinsipning "
                       "xulosasi emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Qutida 6 xil rangdagi shar bor.</p>"
                "<p><strong>Kamida nechta olsa, bir xil rangdagi 3 ta "
                "shar kafolatlanadi?</strong></p>",
        "choices": ["12 ta", "13 ta", "18 ta", "19 ta"],
        "correct": "13 ta",
        "explanation": "<p><strong>13 ta.</strong> 6 × (3 − 1) + 1 = 13. "
                       "Eng yomon hol — har rangdan 2 tadan (12 ta); "
                       "oʻn uchinchisi biror rangni 3 taga "
                       "yetkazadi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Dirixle "
                "prinsipining xulosasi ehtimolmi yoki kafolatmi?</strong>"
                "</p>",
        "choices": [
            "Ehtimol — koʻpincha shunday boʻladi",
            "Kafolat — hech qanday istisnosiz",
            "Ehtimol, lekin juda yuqori",
            "Sonlar katta boʻlganda kafolat",
        ],
        "correct": "Kafolat — hech qanday istisnosiz",
        "explanation": "<p><strong>Kafolat.</strong> Prinsip ehtimolga "
                       "umuman aloqador emas. U sanoq mulohazasiga "
                       "asoslangan va har doim, har qanday holda "
                       "ishlaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>25 oʻquvchi, 12 oy. "
                "Oʻquvchi 25 ÷ 12 = 2,08 deb hisobladi.</p>"
                "<p><strong>Javob nima?</strong></p>",
        "choices": [
            "Kamida 2 tasi bir oyda",
            "Kamida 3 tasi bir oyda",
            "Roppa-rosa 2 tasi bir oyda",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Kamida 3 tasi bir oyda",
        "explanation": "<p><strong>Kamida 3 tasi.</strong> Yuqoriga "
                       "yaxlitlanadi (PM-14). Agar har oyda koʻpi "
                       "bilan 2 ta boʻlsa, jami 24 ta boʻlardi — 25 ta "
                       "emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>PM-96 dagi "
                "juftlik bilan PM-97 dagi Dirixle nimasi bilan farq "
                "qiladi?</strong></p>",
        "choices": [
            "Juftlik imkonsizlikni, Dirixle mavjudlikni isbotlaydi",
            "Juftlik mavjudlikni, Dirixle imkonsizlikni isbotlaydi",
            "Ikkalasi ham bir xil narsani isbotlaydi",
            "Ikkalasi ham ehtimolni hisoblaydi",
        ],
        "correct": "Juftlik imkonsizlikni, Dirixle mavjudlikni isbotlaydi",
        "explanation": "<p><strong>Juftlik imkonsizlikni, Dirixle "
                       "mavjudlikni.</strong> Invariant «bunga yetib "
                       "boʻlmaydi» deydi; Dirixle esa «bunday narsa "
                       "bor» deydi. Isbotlashning ikki turi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sinfda 13 oʻquvchi "
                "bor.</p><p><strong>Dirixle prinsipi yordamida "
                "«Bekzod bilan Afsona bir oyda tugʻilgan» deyish "
                "mumkinmi?</strong></p>",
        "choices": [
            "Ha, hisobdan shu chiqadi",
            "Yoʻq — prinsip kimligini aytmaydi",
            "Ha, agar ular bir sinfda boʻlsa",
            "Yoʻq, chunki 13 juda kam",
        ],
        "correct": "Yoʻq — prinsip kimligini aytmaydi",
        "explanation": "<p><strong>Yoʻq.</strong> Prinsip faqat bunday "
                       "ikki kishi <strong>borligini</strong> "
                       "isbotlaydi. Aniq odamlarni bilish uchun "
                       "tugʻilgan kunlar roʻyxatini koʻrish "
                       "kerak.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>«Qutida 5 xil rangdagi "
                "shar bor. Bir xil rangdagi 2 ta shar kafolatlanishi "
                "uchun 2 ta olish yetadi» deb yozildi.</p>"
                "<p><strong>Nima notoʻgʻri?</strong></p>",
        "choices": [
            "Eng yomon hol hisobga olinmagan",
            "5 ni 2 ga koʻpaytirish kerak edi",
            "Javob 5 ta boʻlishi kerak",
            "Xato yoʻq",
        ],
        "correct": "Eng yomon hol hisobga olinmagan",
        "explanation": "<p><strong>Eng yomon hol hisobga "
                       "olinmagan.</strong> Ikkita olganda ikkalasi "
                       "har xil rang boʻlishi mumkin. Eng yomon holda "
                       "har rangdan bittadan (5 ta) olinadi, oltinchisi "
                       "takrorlaydi: 5 × (2 − 1) + 1 = 6 ta.</p>",
    },
    {
        "text": "<p>Qaysi mulohaza toʻgʻri?</p><p><strong>100 ta son "
                "9 ga boʻlinmoqda. Kamida nechtasi bir xil qoldiq "
                "beradi?</strong></p>",
        "choices": [
            "100 ÷ 9 ≈ 11,1 → kamida 11 tasi",
            "100 ÷ 9 ≈ 11,1 → kamida 12 tasi",
            "100 ÷ 10 = 10 → kamida 10 tasi",
            "9 ta — qoldiqlar soniga teng",
        ],
        "correct": "100 ÷ 9 ≈ 11,1 → kamida 12 tasi",
        "explanation": "<p><strong>Kamida 12 tasi.</strong> Qoldiqlar "
                       "0 dan 8 gacha — 9 xil. 100 ÷ 9 ≈ 11,1 va u "
                       "<strong>yuqoriga</strong> yaxlitlanadi. "
                       "Tekshirish: har qoldiqdan koʻpi bilan 11 ta "
                       "boʻlsa, jami 99 ta boʻlardi — 100 ta "
                       "emas.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Kutubxonada 5 xil janrdagi "
                "kitoblar bor. Bekzod koʻzini yumib kitob olmoqda.</p>"
                "<p><strong>Kamida nechta olsa, bir janrdan 3 ta kitob "
                "kafolatlanadi?</strong></p>",
        "choices": ["8 ta", "10 ta", "11 ta", "15 ta"],
        "correct": "11 ta",
        "explanation": "<p><strong>11 ta.</strong> Eng yomon hol — har "
                       "janrdan 2 tadan, yaʼni 5 × 2 = 10 ta; hali "
                       "uchtalik yoʻq. Oʻn birinchisi qaysi janr "
                       "boʻlmasin, oʻsha janrni 3 taga yetkazadi. "
                       "Formula: 5 × (3 − 1) + 1 = 11.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir shaharda 900 000 kishi "
                "yashaydi. Odam boshidagi soch tolalari soni koʻpi bilan "
                "200 000 ta.</p><p><strong>Sochlari soni bir xil boʻlgan "
                "kamida nechta kishi bor?</strong></p>",
        "choices": ["2 kishi", "4 kishi", "5 kishi", "200 kishi"],
        "correct": "5 kishi",
        "explanation": "<p><strong>5 kishi.</strong> Sochlar soni 0 dan "
                       "200 000 gacha — 200 001 xil (uyalar). "
                       "900 000 ÷ 200 001 ≈ 4,5 → yuqoriga yaxlitlab 5. "
                       "Tekshirish: har sondan koʻpi bilan 4 kishi "
                       "boʻlsa, jami 800 004 kishi boʻlardi — "
                       "900 000 emas. <strong>2 kishi</strong> ham "
                       "rost, lekin bu eng zaif xulosa.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-95 Mashq: Mantiqiy masalalar va jadval usuli",
        "tutorial":    "PM-95:",
        "description": (
            "Mantiqiy jadval, shartni «bu emas» ga oʻgirish, chiqarib "
            "tashlash va yechimning yagonaligi. 20 savol."
        ),
        "questions":   Q_PM95,
        **DEFAULTS,
    },
    {
        "title":       "PM-96 Mashq: Juftlik (juft-toq) gʻoyasi",
        "tutorial":    "PM-96:",
        "description": (
            "Juft-toq qoidalari, invariant, imkonsizlik isboti, doskani "
            "boʻyash va qoʻl berish lemmasi. 20 savol."
        ),
        "questions":   Q_PM96,
        **DEFAULTS,
    },
    {
        "title":       "PM-97 Mashq: Dirixle prinsipi",
        "tutorial":    "PM-97:",
        "description": (
            "Kaptarxona qoidasi, eng yomon hol, k × (m − 1) + 1 va "
            "mavjudlik isboti. 20 savol."
        ),
        "questions":   Q_PM97,
        **DEFAULTS,
    },
]
