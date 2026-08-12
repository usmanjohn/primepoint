# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-60, PM-61, PM-62 (parallel chiziqlar, uchburchak,
uchburchak tengsizligi).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: `medium` (Blok E, 70 gacha).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq. Savol matnida <strong>, <sup> mumkin.
⚠️ Kumulyativ: teng yonli uchburchak xossalari (PM-63) YOʻQ, Pifagor (PM-64)
   YOʻQ, perimetr (PM-67) va yuza (PM-68) YOʻQ, π (PM-70) YOʻQ.
   PM-61 da «ikki burchagi teng» faqat SHART sifatida beriladi, xossa
   sifatida emas.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_60_62.py --master=prime \\
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
# PM-60 — parallel chiziqlar va kesuvchi
# =====================================================================

Q_PM60 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>a ∥ b yozuvi nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "a va b parallel chiziqlar",
            "a va b kesishadi",
            "a va b perpendikulyar",
            "a va b teng uzunlikda",
        ],
        "correct": "a va b parallel chiziqlar",
        "explanation": "<p><strong>a va b parallel.</strong> ∥ belgisi "
                       "«hech qachon kesishmaydi» degani; ikki chiziq orasidagi "
                       "masofa hamma joyda bir xil boʻladi. Perpendikulyarlik "
                       "boshqa narsa — u 90° ostida kesishishni bildiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>a ∥ b va ularni kesuvchi "
                "kesib oʻtdi.</p><p><strong>Mos burchaklar haqida nima deyish "
                "mumkin?</strong></p>",
        "choices": [
            "Ular teng",
            "Ularning yigʻindisi 180°",
            "Ularning yigʻindisi 90°",
            "Ular har doim toʻgʻri burchak",
        ],
        "correct": "Ular teng",
        "explanation": "<p><strong>Ular teng.</strong> Bu F qoidasi: ikkala "
                       "kesishishda bir xil oʻrinda turgan burchaklar parallel "
                       "chiziqlarda teng boʻladi. 180° beradiganlari — bir "
                       "tomonli ichki burchaklar (U qoidasi).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Bir tomonli ichki "
                "burchaklarning yigʻindisi qancha?</strong></p>",
        "choices": ["90°", "180°", "270°", "360°"],
        "correct": "180°",
        "explanation": "<p><strong>180°.</strong> Bu U qoidasi. Chizmada bu "
                       "juftlik «U» harfini hosil qiladi va xuddi qoʻshni "
                       "burchaklardek 180° beradi — teng emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Kesuvchi deb "
                "nimaga aytiladi?</strong></p>",
        "choices": [
            "Ikkala chiziqni ham kesib oʻtuvchi uchinchi chiziq",
            "Ikki parallel chiziqning oʻrtasidagi chiziq",
            "Burchakni teng ikkiga boʻluvchi nur",
            "Eng uzun chiziq",
        ],
        "correct": "Ikkala chiziqni ham kesib oʻtuvchi uchinchi chiziq",
        "explanation": "<p><strong>Ikkala chiziqni ham kesib oʻtuvchi uchinchi "
                       "chiziq.</strong> U ikkita kesishish nuqtasi va sakkizta "
                       "burchak hosil qiladi. Burchakni teng ikkiga boʻluvchi "
                       "nur esa bissektrisa deyiladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>a ∥ b va mos burchaklardan biri 55°.</p>"
                "<p><strong>Ikkinchisi qancha?</strong></p>",
        "choices": ["35°", "55°", "125°", "145°"],
        "correct": "55°",
        "explanation": "<p><strong>55°.</strong> Mos burchaklar teng (F "
                       "qoidasi). <strong>125°</strong> — bu uning qoʻshnisi "
                       "(180 − 55), <strong>35°</strong> esa toʻldiruvchisi "
                       "(90 − 55).</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p>a ∥ b. Kesuvchi hosil qilgan burchaklardan "
                "biri 130°.</p><p><strong>Unga qoʻshni burchak qancha?</strong></p>",
        "choices": ["40°", "50°", "130°", "230°"],
        "correct": "50°",
        "explanation": "<p><strong>50°.</strong> Qoʻshni burchaklar yoyiq "
                       "burchakni toʻldiradi: 180 − 130 = 50 (PM-59). "
                       "Parallel chiziqlarda faqat shu ikki qiymat "
                       "uchraydi: 130° va 50°.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>a ∥ b va bir tomonli ichki burchaklardan "
                "biri 105°.</p><p><strong>Ikkinchisi qancha?</strong></p>",
        "choices": ["15°", "75°", "105°", "255°"],
        "correct": "75°",
        "explanation": "<p><strong>75°.</strong> U qoidasi: yigʻindisi 180°, "
                       "demak 180 − 105 = 75. Tekshirish: 105 + 75 = 180 ✓ "
                       "<strong>105°</strong> — bu juftlik teng deb "
                       "oʻylanganda chiqadi, lekin U juftligi teng emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>a ∥ b, ∠2 = 130°. ∠3 — ∠2 ga qoʻshni, "
                "∠6 esa ∠3 ga almashinuvchi ichki burchak.</p><p><strong>∠6 "
                "qancha?</strong></p>",
        "choices": ["50°", "60°", "130°", "150°"],
        "correct": "50°",
        "explanation": "<p><strong>50°.</strong> Ikki qadam: ∠3 = 180 − 130 = "
                       "50 (qoʻshni), keyin ∠6 = ∠3 = 50 (almashinuvchi ichki, "
                       "Z qoidasi — teng). <strong>130°</strong> — faqat "
                       "birinchi qadam qilinmaganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>a ∥ b va almashinuvchi ichki burchaklardan "
                "biri 48°.</p><p><strong>Ikkinchisi qancha?</strong></p>",
        "choices": ["42°", "48°", "132°", "138°"],
        "correct": "48°",
        "explanation": "<p><strong>48°.</strong> Z qoidasi: almashinuvchi ichki "
                       "burchaklar parallel chiziqlarda teng. "
                       "<strong>132°</strong> — bu uning qoʻshnisi, yaʼni "
                       "bir tomonli ichki burchak.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>a ∥ b. Bir tomonli ichki "
                "burchaklardan biri x, ikkinchisi x + 40.</p><p><strong>Kichik "
                "burchak necha gradus?</strong></p>",
        "choices": ["50°", "70°", "90°", "110°"],
        "correct": "70°",
        "explanation": "<p><strong>70°.</strong> U qoidasi: x + (x + 40) = 180, "
                       "demak 2x = 140 va x = 70. Kattasi 110°. Tekshirish: "
                       "70 + 110 = 180 ✓ <strong>50°</strong> — 180 ni "
                       "notoʻgʻri boʻlganda chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>a ∥ b va mos burchaklar 3x va "
                "x + 50 bilan ifodalangan.</p><p><strong>Bu burchaklar necha "
                "gradus?</strong></p>",
        "choices": ["25°", "50°", "75°", "125°"],
        "correct": "75°",
        "explanation": "<p><strong>75°.</strong> Mos burchaklar teng, demak "
                       "3x = x + 50, 2x = 50, x = 25. Burchak esa "
                       "3 × 25 = 75° (tekshirish: 25 + 50 = 75 ✓). "
                       "<strong>25°</strong> — bu x ning qiymati, burchakning "
                       "oʻzi emas; savolni oxirigacha oʻqish kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki parallel chiziqni "
                "kesuvchi kesib oʻtdi.</p><p><strong>Hosil boʻlgan sakkizta "
                "burchakda nechta har xil qiymat boʻladi?</strong></p>",
        "choices": ["Bitta", "Ikkita", "Toʻrtta", "Sakkizta"],
        "correct": "Ikkita",
        "explanation": "<p><strong>Ikkita.</strong> Masalan 70° va 110°, va "
                       "ularning yigʻindisi 180°. Chiziqlar perpendikulyar "
                       "boʻlgandagina bitta qiymat (90°) qoladi. Shuning uchun "
                       "bitta oʻlchov butun chizmani beradi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Mos va almashinuvchi "
                "ichki burchaklarning farqi nimada?</strong></p>",
        "choices": [
            "Mos burchaklar kesuvchining bir tomonida, almashinuvchilar har xil tomonida",
            "Mos burchaklar teng, almashinuvchilar 180° beradi",
            "Almashinuvchilar teng, mos burchaklar 180° beradi",
            "Hech qanday farq yoʻq",
        ],
        "correct": "Mos burchaklar kesuvchining bir tomonida, almashinuvchilar har xil tomonida",
        "explanation": "<p><strong>Farq oʻrinda.</strong> Ikkala juftlik ham "
                       "parallel chiziqlarda <strong>teng</strong> — farqi "
                       "joylashuvida: mos burchaklar (F) kesuvchining bir "
                       "tomonida va bir xil oʻrinda, almashinuvchilar (Z) esa "
                       "orada, qarama-qarshi tomonlarda.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi juftlik "
                "parallel chiziqlarda teng EMAS?</strong></p>",
        "choices": [
            "Bir tomonli ichki burchaklar",
            "Mos burchaklar",
            "Almashinuvchi ichki burchaklar",
            "Vertikal burchaklar",
        ],
        "correct": "Bir tomonli ichki burchaklar",
        "explanation": "<p><strong>Bir tomonli ichki burchaklar.</strong> Ular "
                       "180° beradi, teng emas — faqat ikkalasi 90° boʻlgan "
                       "holda tasodifan teng chiqadi. Qolgan uch juftlik "
                       "har doim teng.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Kesuvchi ikki chiziqni kesib "
                "oʻtdi va mos burchaklar 68° hamda 74° chiqdi.</p>"
                "<p><strong>Bundan nima kelib chiqadi?</strong></p>",
        "choices": [
            "Chiziqlar parallel emas",
            "Chiziqlar parallel",
            "Chiziqlar perpendikulyar",
            "Bunday chizma mumkin emas",
        ],
        "correct": "Chiziqlar parallel emas",
        "explanation": "<p><strong>Parallel emas.</strong> Parallel boʻlganida "
                       "mos burchaklar teng chiqishi shart edi. 68 ≠ 74, demak "
                       "chiziqlar qayerdadir kesishadi — faqat chizmadan "
                       "tashqarida. Bu qoidaning teskari tomonga "
                       "oʻqilishi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki chiziq parallel "
                "EMAS.</p><p><strong>Mos burchaklar haqida nima deyish "
                "mumkin?</strong></p>",
        "choices": [
            "Ular teng emas",
            "Ular baribir teng",
            "Ularning yigʻindisi 180°",
            "Ularning yigʻindisi 90°",
        ],
        "correct": "Ular teng emas",
        "explanation": "<p><strong>Ular teng emas.</strong> «Mos burchaklar "
                       "teng» qoidasining <strong>sharti</strong> — "
                       "parallellik. Shart bajarilmasa, xulosa ham "
                       "bajarilmaydi: sakkizta burchakning qiymatlari har xil "
                       "boʻlib ketadi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>a ∥ b va bir tomonli ichki "
                "burchaklardan biri 110°.</p><p><strong>Yechim: ikkinchisi ham "
                "110°, chunki ular teng.</strong></p>",
        "choices": [
            "Bir tomonli ichki burchaklar teng emas: 180 − 110 = 70°",
            "Ikkinchisi 90° boʻlishi kerak",
            "Bunday burchak juftligi umuman yoʻq",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Bir tomonli ichki burchaklar teng emas: 180 − 110 = 70°",
        "explanation": "<p><strong>Ular teng emas.</strong> Teng boʻladiganlari "
                       "— mos (F) va almashinuvchi (Z) juftliklari. Bir tomonli "
                       "ichki burchaklar (U) esa yigʻindisi 180° beradi: "
                       "180 − 110 = 70°.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Yuqoridagi kesishishda burchaklar "
                "1–4, pastdagida 5–8 deb belgilangan.</p><p><strong>«∠3 va ∠5 — "
                "almashinuvchi ichki burchaklar».</strong></p>",
        "choices": [
            "∠3 ning almashinuvchisi ∠6, chunki u kesuvchining boshqa tomonida",
            "∠3 ning almashinuvchisi ∠7",
            "∠3 va ∠5 mos burchaklar",
            "Xato yoʻq, jumla toʻgʻri",
        ],
        "correct": "∠3 ning almashinuvchisi ∠6, chunki u kesuvchining boshqa tomonida",
        "explanation": "<p><strong>∠3 ning almashinuvchisi — ∠6.</strong> "
                       "Almashinuvchi juftlik ikki sharti bor: ikkalasi ham "
                       "parallel chiziqlar <strong>orasida</strong> va "
                       "kesuvchining <strong>har xil</strong> tomonlarida "
                       "boʻlishi kerak. ∠3 bilan ∠5 esa bitta tomonda.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Duradgor taxtani qiya kesdi. Taxtaning ikki cheti parallel. "
                "Kesim chizigʻi yuqorigi chet bilan 62° burchak hosil qildi.</p>"
                "<p><strong>Kesim pastki chet bilan qanday burchaklar hosil "
                "qiladi?</strong></p>",
        "choices": [
            "31° va 149°",
            "62° va 118°",
            "62° va 62°",
            "118° va 118°",
        ],
        "correct": "62° va 118°",
        "explanation": "<p><strong>62° va 118°.</strong> Taxtaning chetlari "
                       "parallel, kesim esa kesuvchi. Mos burchak teng: 62°. "
                       "Uning qoʻshnisi 180 − 62 = 118°. Parallel chiziqlarda "
                       "kesuvchi ikkala chiziq bilan ham bir xil burchaklarni "
                       "hosil qiladi.</p>",
    },
    {
        "text": "<p>Yoʻlda ikki parallel piyodalar yoʻlagi chizilgan. Ularni "
                "bitta qiya soʻqmoq kesib oʻtadi. Soʻqmoq bilan yuqorigi yoʻlak "
                "orasidagi ichki burchak 115°.</p><p><strong>Soʻqmoq bilan "
                "pastki yoʻlak orasidagi, xuddi shu tomondagi ichki burchak "
                "qancha?</strong></p>",
        "choices": ["55°", "65°", "115°", "125°"],
        "correct": "65°",
        "explanation": "<p><strong>65°.</strong> Ikkala burchak ham chiziqlar "
                       "orasida va soʻqmoqning bitta tomonida — demak bular "
                       "bir tomonli ichki burchaklar (U qoidasi): "
                       "180 − 115 = 65°. <strong>115°</strong> — bu juftlik "
                       "teng deb oʻylanganda chiqadi.</p>",
    },
]


# =====================================================================
# PM-61 — uchburchak turlari va burchaklar yigʻindisi
# =====================================================================

Q_PM61 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Uchburchak "
                "burchaklarining yigʻindisi qancha?</strong></p>",
        "choices": ["90°", "180°", "270°", "360°"],
        "correct": "180°",
        "explanation": "<p><strong>180°.</strong> Bu har qanday uchburchak "
                       "uchun toʻgʻri — kichik boʻladimi, katta boʻladimi, "
                       "farqi yoʻq. <strong>360°</strong> — bu nuqta "
                       "atrofidagi toʻla burchak.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Uchburchakning ikki burchagi 50° "
                "va 60°. Uchinchisi qancha?</strong></p>",
        "choices": ["60°", "70°", "80°", "110°"],
        "correct": "70°",
        "explanation": "<p><strong>70°.</strong> 180 − 50 − 60 = 70. "
                       "Tekshirish: 50 + 60 + 70 = 180 ✓ "
                       "<strong>110°</strong> — faqat ikki burchak qoʻshilib, "
                       "180 dan ayirilmaganda chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Teng tomonli "
                "uchburchakning har bir burchagi necha gradus?</strong></p>",
        "choices": ["45°", "60°", "90°", "120°"],
        "correct": "60°",
        "explanation": "<p><strong>60°.</strong> Uchala tomoni teng boʻlsa, "
                       "uchala burchagi ham teng: 180 ÷ 3 = 60. "
                       "<strong>90°</strong> boʻlganida yigʻindi 270° chiqib "
                       "ketardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Toʻgʻri burchakli "
                "uchburchak deb qanday uchburchakka aytiladi?</strong></p>",
        "choices": [
            "Bitta burchagi aniq 90° boʻlgan uchburchak",
            "Hamma burchagi 90° boʻlgan uchburchak",
            "Hamma tomoni teng boʻlgan uchburchak",
            "Ikki burchagi 90° boʻlgan uchburchak",
        ],
        "correct": "Bitta burchagi aniq 90° boʻlgan uchburchak",
        "explanation": "<p><strong>Bitta burchagi 90°.</strong> Ikkitasi 90° "
                       "boʻlishi mumkin emas — 90 + 90 = 180 boʻlib, uchinchi "
                       "burchakka hech narsa qolmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Bitta uchburchakda "
                "ikkita oʻtmas burchak boʻlishi mumkinmi?</strong></p>",
        "choices": [
            "Yoʻq — yigʻindi 180° dan oshib ketadi",
            "Ha, agar uchinchisi juda kichik boʻlsa",
            "Ha, teng yonli uchburchakda",
            "Faqat katta uchburchaklarda",
        ],
        "correct": "Yoʻq — yigʻindi 180° dan oshib ketadi",
        "explanation": "<p><strong>Yoʻq.</strong> Har bir oʻtmas burchak 90° "
                       "dan katta, demak ikkitasi birga 180° dan oshadi va "
                       "uchinchi burchakka joy qolmaydi. Har bir uchburchakda "
                       "kamida ikkita oʻtkir burchak bor.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>Uchburchakning ikki burchagi 47° "
                "va 65°. Uchinchisi qancha?</strong></p>",
        "choices": ["58°", "62°", "68°", "112°"],
        "correct": "68°",
        "explanation": "<p><strong>68°.</strong> 180 − 47 − 65 = 68. "
                       "Tekshirish: 47 + 65 + 68 = 180 ✓ "
                       "<strong>112°</strong> — 47 + 65 ning oʻzi, ayirish "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Toʻgʻri burchakli uchburchakning oʻtkir "
                "burchaklaridan biri 28°.</p><p><strong>Ikkinchi oʻtkir burchak "
                "qancha?</strong></p>",
        "choices": ["52°", "62°", "72°", "152°"],
        "correct": "62°",
        "explanation": "<p><strong>62°.</strong> Toʻgʻri burchak 90° ni oladi, "
                       "qolgan ikkitasiga 180 − 90 = 90° qoladi, demak "
                       "90 − 28 = 62. Tekshirish: 90 + 28 + 62 = 180 ✓ "
                       "<strong>152°</strong> — 180 dan ayirilganda chiqadi, "
                       "lekin toʻgʻri burchak hisobga olinmagan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Uchburchakda 100° li burchak "
                "bor.</p><p><strong>Bu qanday uchburchak?</strong></p>",
        "choices": [
            "Oʻtmas burchakli",
            "Oʻtkir burchakli",
            "Toʻgʻri burchakli",
            "Teng tomonli",
        ],
        "correct": "Oʻtmas burchakli",
        "explanation": "<p><strong>Oʻtmas burchakli.</strong> 100° &gt; 90°, "
                       "demak bu oʻtmas burchak. Qolgan ikkitasiga "
                       "180 − 100 = 80° qoladi, shuning uchun ikkalasi ham "
                       "albatta oʻtkir.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Uchburchakning burchaklari "
                "3 : 4 : 5 nisbatda. Eng katta burchak qancha?</strong></p>",
        "choices": ["45°", "60°", "75°", "90°"],
        "correct": "75°",
        "explanation": "<p><strong>75°.</strong> 3x + 4x + 5x = 180, demak "
                       "12x = 180 va x = 15. Burchaklar: 45°, 60°, 75°. "
                       "Tekshirish: 45 + 60 + 75 = 180 ✓ Eng kattasi 75°, u "
                       "90 dan kichik — demak uchburchak oʻtkir burchakli.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Uchburchakning burchaklari "
                "4 : 5 : 9 nisbatda. Burchaklarni toping.</strong></p>",
        "choices": [
            "20°, 25°, 45°",
            "40°, 50°, 90°",
            "45°, 60°, 75°",
            "50°, 60°, 70°",
        ],
        "correct": "40°, 50°, 90°",
        "explanation": "<p><strong>40°, 50°, 90°.</strong> 4x + 5x + 9x = 180, "
                       "18x = 180, x = 10. Tekshirish: 40 + 50 + 90 = 180 ✓ "
                       "<strong>20°, 25°, 45°</strong> — yigʻindisi 90 boʻlib "
                       "qoladi, yaʼni x notoʻgʻri topilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Uchburchakning ikki burchagi "
                "teng, uchinchisi esa 40°.</p><p><strong>Teng burchaklarning "
                "har biri qancha?</strong></p>",
        "choices": ["40°", "50°", "70°", "140°"],
        "correct": "70°",
        "explanation": "<p><strong>70°.</strong> Teng burchaklarni x deb "
                       "olamiz: x + x + 40 = 180, demak 2x = 140 va x = 70. "
                       "Tekshirish: 70 + 70 + 40 = 180 ✓ "
                       "<strong>140°</strong> — bu ikkalasining yigʻindisi, "
                       "bittasi emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Uchburchakning ikki burchagi teng "
                "va har biri 25°.</p><p><strong>Uchinchi burchak qancha va "
                "uchburchak qanday turga kiradi?</strong></p>",
        "choices": [
            "130°, oʻtmas burchakli",
            "130°, oʻtkir burchakli",
            "50°, oʻtkir burchakli",
            "155°, oʻtmas burchakli",
        ],
        "correct": "130°, oʻtmas burchakli",
        "explanation": "<p><strong>130°, oʻtmas burchakli.</strong> "
                       "180 − 25 − 25 = 130. Tekshirish: 25 + 25 + 130 = "
                       "180 ✓ 130° &gt; 90°, demak uchburchak oʻtmas "
                       "burchakli.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Burchaklari 90°, 60° "
                "va 40° boʻlgan uchburchak mavjudmi?</strong></p>",
        "choices": [
            "Yoʻq — yigʻindi 190°, 180° emas",
            "Ha, bu toʻgʻri burchakli uchburchak",
            "Ha, bu oʻtmas burchakli uchburchak",
            "Faqat katta oʻlchamda mavjud",
        ],
        "correct": "Yoʻq — yigʻindi 190°, 180° emas",
        "explanation": "<p><strong>Mavjud emas.</strong> 90 + 60 + 40 = 190 ≠ "
                       "180. Har qanday javobni qoʻshib tekshiring — bu eng "
                       "tez ishlaydigan nazorat.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bitta uchburchak "
                "ikkinchisidan ancha katta chizilgan.</p><p><strong>Ularning "
                "burchaklari yigʻindisi qanday taqqoslanadi?</strong></p>",
        "choices": [
            "Ikkalasida ham 180°",
            "Kattasida koʻproq",
            "Kichigida koʻproq",
            "Oʻlchamiga qarab har xil",
        ],
        "correct": "Ikkalasida ham 180°",
        "explanation": "<p><strong>Ikkalasida ham 180°.</strong> Burchak "
                       "uzunlikni emas, <strong>burilish</strong>ni oʻlchaydi "
                       "(PM-58). Tomonlarni choʻzish burchakni "
                       "oʻzgartirmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Teng tomonli va "
                "teng yonli uchburchakning farqi nimada?</strong></p>",
        "choices": [
            "Teng tomonlida uchala tomon teng, teng yonlida ikkitasi",
            "Teng tomonlida ikki tomon teng, teng yonlida uchtasi",
            "Teng tomonli har doim toʻgʻri burchakli",
            "Hech qanday farq yoʻq",
        ],
        "correct": "Teng tomonlida uchala tomon teng, teng yonlida ikkitasi",
        "explanation": "<p><strong>Uchtasi va ikkitasi.</strong> Teng tomonli "
                       "uchburchakning burchaklari ham har doim 60° dan "
                       "boʻladi; teng yonlinikida esa burchaklar har xil "
                       "boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Bitta uchburchakda "
                "eng koʻpi bilan nechta oʻtkir burchak boʻlishi mumkin?</strong></p>",
        "choices": ["Uchta", "Bitta", "Ikkita", "Toʻrtta"],
        "correct": "Uchta",
        "explanation": "<p><strong>Uchta.</strong> Masalan 60°, 60°, 60° — "
                       "hammasi 90° dan kichik. Bunday uchburchak oʻtkir "
                       "burchakli deyiladi. Aksincha, oʻtmas yoki toʻgʻri "
                       "burchak esa faqat <strong>bitta</strong> boʻlishi "
                       "mumkin.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Masala: burchaklar 2 : 3 : 4 "
                "nisbatda.</p><p><strong>Yechim: burchaklar 2°, 3° va "
                "4°.</strong></p>",
        "choices": [
            "Nisbat ulushni bildiradi: 2x + 3x + 4x = 180",
            "Nisbatni teskari oʻqish kerak edi",
            "Yigʻindi 360° boʻlishi kerak",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Nisbat ulushni bildiradi: 2x + 3x + 4x = 180",
        "explanation": "<p><strong>Nisbat ulushni bildiradi.</strong> "
                       "2 + 3 + 4 = 9, bu esa 180° emas. Toʻgʻri yechim: "
                       "9x = 180, x = 20, demak burchaklar 40°, 60° va 80° "
                       "(PM-27).</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Masala: toʻgʻri burchakli "
                "uchburchakning bir oʻtkir burchagi 35°.</p><p><strong>Yechim: "
                "ikkinchisi 180 − 35 = 145°.</strong></p>",
        "choices": [
            "Toʻgʻri burchak hisobga olinmagan: 90 − 35 = 55°",
            "180 oʻrniga 360 dan ayirish kerak edi",
            "35° ni ikkiga koʻpaytirish kerak edi",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Toʻgʻri burchak hisobga olinmagan: 90 − 35 = 55°",
        "explanation": "<p><strong>Toʻgʻri burchak unutilgan.</strong> Uchta "
                       "burchak bor: 90°, 35° va nomaʼlumi. "
                       "180 − 90 − 35 = 55°. Tekshirish: 90 + 35 + 55 = "
                       "180 ✓ 145° li burchak oʻtmas boʻlib, toʻgʻri burchak "
                       "bilan bir uchburchakda tura olmaydi.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Mahalladagi bogʻ uchburchak shaklida. Loyihachining "
                "chizmasida burchaklar 2 : 3 : 4 nisbatda koʻrsatilgan.</p>"
                "<p><strong>Bogʻning eng katta burchagi qancha?</strong></p>",
        "choices": ["40°", "60°", "80°", "90°"],
        "correct": "80°",
        "explanation": "<p><strong>80°.</strong> 2x + 3x + 4x = 180, 9x = 180, "
                       "x = 20. Burchaklar: 40°, 60°, 80°. Tekshirish: "
                       "40 + 60 + 80 = 180 ✓ Eng kattasi 80° va u 90 dan "
                       "kichik, demak bogʻ oʻtkir burchakli uchburchak.</p>",
    },
    {
        "text": "<p>Usta tom uchun uchburchak shaklidagi ferma yasadi. Fermaning "
                "pastki ikki burchagi teng va har biri 35°.</p>"
                "<p><strong>Yuqoridagi burchak qancha?</strong></p>",
        "choices": ["70°", "100°", "110°", "145°"],
        "correct": "110°",
        "explanation": "<p><strong>110°.</strong> Pastki ikkitasi birga "
                       "35 + 35 = 70°, demak yuqoridagisi 180 − 70 = 110°. "
                       "Tekshirish: 35 + 35 + 110 = 180 ✓ "
                       "<strong>70°</strong> — bu pastki ikkitasining "
                       "yigʻindisi, yuqoridagi burchak emas.</p>",
    },
]


# =====================================================================
# PM-62 — uchburchak tengsizligi
# =====================================================================

Q_PM62 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>7, 10 va 15 "
                "uzunlikdagi tayoqlardan uchburchak chiqadimi?</strong></p>",
        "choices": [
            "Ha, chunki 7 + 10 = 17 > 15",
            "Yoʻq, chunki 7 + 10 = 17 > 15",
            "Ha, chunki 15 − 10 = 5 < 7",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Ha, chunki 7 + 10 = 17 > 15",
        "explanation": "<p><strong>Ha.</strong> Eng qisqa ikki tomonni "
                       "qoʻshamiz: 7 + 10 = 17, bu eng uzuni 15 dan katta ✓ "
                       "Demak tayoqlar yetadi va uchburchak yopiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2, 3 va 6 "
                "uzunlikdagi tayoqlardan uchburchak chiqadimi?</strong></p>",
        "choices": [
            "Yoʻq, chunki 2 + 3 = 5 < 6",
            "Ha, chunki 3 + 6 = 9 > 2",
            "Ha, chunki uchala son ham musbat",
            "Yoʻq, chunki sonlar juda kichik",
        ],
        "correct": "Yoʻq, chunki 2 + 3 = 5 < 6",
        "explanation": "<p><strong>Chiqmaydi.</strong> Ikki qisqa tayoq birga "
                       "5 birlik, uzuni esa 6 — ular uning ikki uchini "
                       "tutashtira olmaydi. <strong>3 + 6 = 9 &gt; 2</strong> "
                       "toʻgʻri, lekin bitta shart yetarli emas: uchalasi ham "
                       "bajarilishi kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Uchburchak "
                "tengsizligi nimani talab qiladi?</strong></p>",
        "choices": [
            "Har ikki tomonning yigʻindisi uchinchisidan katta boʻlishini",
            "Uchala tomonning teng boʻlishini",
            "Burchaklar yigʻindisi 180° boʻlishini",
            "Eng uzun tomon 10 dan kichik boʻlishini",
        ],
        "correct": "Har ikki tomonning yigʻindisi uchinchisidan katta boʻlishini",
        "explanation": "<p><strong>Har ikki tomon yigʻindisi uchinchisidan "
                       "katta.</strong> Uchala shart ham bajarilishi kerak, "
                       "lekin amalda eng qisqa ikkitasini tekshirish "
                       "yetarli — qolgani avtomatik bajariladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Uchburchakda eng "
                "katta burchak qayerda turadi?</strong></p>",
        "choices": [
            "Eng uzun tomonning qarshisida",
            "Eng uzun tomonning yonida",
            "Eng qisqa tomonning qarshisida",
            "Har doim oʻrtadagi tomon qarshisida",
        ],
        "correct": "Eng uzun tomonning qarshisida",
        "explanation": "<p><strong>Eng uzun tomonning qarshisida.</strong> "
                       "Burchak oʻzi turgan tomonga emas, roʻparasidagi tomonga "
                       "bogʻlangan. Eng qisqa tomon qarshisida esa eng kichik "
                       "burchak turadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>4, 6 va 10 "
                "uzunlikdagi tayoqlardan uchburchak chiqadimi?</strong></p>",
        "choices": [
            "Yoʻq — 4 + 6 = 10, bu 10 dan katta emas",
            "Ha — 4 + 6 = 10, bu yetarli",
            "Ha, lekin faqat toʻgʻri burchakli",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Yoʻq — 4 + 6 = 10, bu 10 dan katta emas",
        "explanation": "<p><strong>Chiqmaydi.</strong> Yigʻindi "
                       "<strong>qatʼiy katta</strong> boʻlishi kerak, teng "
                       "emas. Teng boʻlganda tayoqlar uzun tayoq ustiga yotib "
                       "qoladi va uchburchak yassilanadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p>Uchburchakning ikki tomoni 5 va 7.</p>"
                "<p><strong>Uchinchi tomon qaysi oraliqda boʻlishi "
                "mumkin?</strong></p>",
        "choices": [
            "2 < x < 12",
            "0 < x < 12",
            "2 < x < 35",
            "5 < x < 7",
        ],
        "correct": "2 < x < 12",
        "explanation": "<p><strong>2 &lt; x &lt; 12.</strong> Yuqori chegara — "
                       "yigʻindi: 5 + 7 = 12. Quyi chegara — farq: "
                       "7 − 5 = 2. Chegaralarning oʻzi kirmaydi: x = 2 yoki "
                       "x = 12 boʻlsa uchburchak yassilanadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Uchburchakning ikki tomoni 8 va 3.</p>"
                "<p><strong>Uchinchi tomon qaysi oraliqda boʻlishi "
                "mumkin?</strong></p>",
        "choices": [
            "3 < x < 8",
            "5 < x < 11",
            "0 < x < 11",
            "5 < x < 24",
        ],
        "correct": "5 < x < 11",
        "explanation": "<p><strong>5 &lt; x &lt; 11.</strong> Yigʻindi: "
                       "8 + 3 = 11. Farq: 8 − 3 = 5. Masalan 6, 7 yoki 10 "
                       "boʻlishi mumkin; 5 yoki 11 esa yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Uchburchakning tomonlari "
                "6, 9 va 11.</p><p><strong>Eng katta burchak qaysi tomonning "
                "qarshisida?</strong></p>",
        "choices": [
            "6 uzunlikdagi tomonning",
            "9 uzunlikdagi tomonning",
            "11 uzunlikdagi tomonning",
            "Uchalasida ham teng",
        ],
        "correct": "11 uzunlikdagi tomonning",
        "explanation": "<p><strong>11 ning qarshisida.</strong> Eng uzun tomon "
                       "qarshisida eng katta burchak turadi. Eng kichik burchak "
                       "esa 6 ning qarshisida — tomonlarni tartiblasangiz, "
                       "burchaklar ham oʻsha tartibda joylashadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Uchburchakning ikki tomoni 9 va 9, "
                "uchinchisi esa butun son.</p><p><strong>Uchinchi tomon eng "
                "koʻpi bilan qancha boʻlishi mumkin?</strong></p>",
        "choices": ["9", "17", "18", "19"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> Shart: x &lt; 9 + 9 = 18, "
                       "demak eng katta butun son 17. <strong>18</strong> "
                       "boʻlganda uchburchak yassilanib qolardi — yigʻindi "
                       "qatʼiy katta boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Uchburchakning ikki tomoni 12 va 9.</p>"
                "<p><strong>Uchinchi tomon qaysi oraliqda?</strong></p>",
        "choices": [
            "3 < x < 21",
            "9 < x < 12",
            "0 < x < 21",
            "3 < x < 108",
        ],
        "correct": "3 < x < 21",
        "explanation": "<p><strong>3 &lt; x &lt; 21.</strong> Yigʻindi: "
                       "12 + 9 = 21. Farq: 12 − 9 = 3. Masalan 15 boʻlishi "
                       "mumkin, 22 esa hech qachon.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>5, 12 va 13 "
                "uzunlikdagi tayoqlardan uchburchak chiqadimi?</strong></p>",
        "choices": [
            "Ha — 5 + 12 = 17 > 13",
            "Yoʻq — 5 + 12 = 17 < 13",
            "Yoʻq — 13 − 12 = 1 < 5",
            "Faqat 13 ni qisqartirsa chiqadi",
        ],
        "correct": "Ha — 5 + 12 = 17 > 13",
        "explanation": "<p><strong>Ha.</strong> Eng qisqa ikkitasi: "
                       "5 + 12 = 17 &gt; 13 ✓ Uchburchak chiqadi. Bu mashhur "
                       "uchlik — kelgusida yana uchraydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Uchburchakning tomonlari "
                "4, 7 va 8.</p><p><strong>Eng kichik burchak qaysi tomonning "
                "qarshisida?</strong></p>",
        "choices": [
            "4 uzunlikdagi tomonning",
            "7 uzunlikdagi tomonning",
            "8 uzunlikdagi tomonning",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "4 uzunlikdagi tomonning",
        "explanation": "<p><strong>4 ning qarshisida.</strong> Eng qisqa tomon "
                       "qarshisida eng kichik burchak turadi. Eng kattasi esa "
                       "8 ning qarshisida boʻladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki tomon "
                "yigʻindisi uchinchisiga aynan TENG boʻlsa nima "
                "boʻladi?</strong></p>",
        "choices": [
            "Uchburchak chiqmaydi — uchala uch bitta chiziqda yotadi",
            "Toʻgʻri burchakli uchburchak chiqadi",
            "Teng yonli uchburchak chiqadi",
            "Eng katta uchburchak chiqadi",
        ],
        "correct": "Uchburchak chiqmaydi — uchala uch bitta chiziqda yotadi",
        "explanation": "<p><strong>Chiqmaydi.</strong> Tayoqlar aynan "
                       "yopishadi va yassi chiziq hosil boʻladi — bunga "
                       "yassilangan uchburchak deyiladi. Shuning uchun "
                       "shartda &lt; emas, qatʼiy &gt; belgisi turadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Tomonlar 3, 4 va 8. "
                "Oʻquvchi 3 + 8 = 11 &gt; 4 deb tekshirdi.</p>"
                "<p><strong>Bu tekshiruv yetarlimi?</strong></p>",
        "choices": [
            "Yoʻq — eng qisqa ikkitasini tekshirish kerak: 3 + 4 = 7 < 8",
            "Ha — bitta shart bajarilsa yetadi",
            "Yoʻq — uchala tomonni koʻpaytirish kerak",
            "Ha, lekin faqat butun sonlar uchun",
        ],
        "correct": "Yoʻq — eng qisqa ikkitasini tekshirish kerak: 3 + 4 = 7 < 8",
        "explanation": "<p><strong>Yetarli emas.</strong> Uzun tomonga son "
                       "qoʻshilsa, yigʻindi albatta katta chiqadi — bunday "
                       "tekshiruv hech narsani aniqlamaydi. Haqiqiy sinov — "
                       "eng qisqa ikkitasi: 3 + 4 = 7 &lt; 8, demak uchburchak "
                       "chiqmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Uchburchakning ikki tomoni "
                "6 va 10.</p><p><strong>Qaysi qiymat uchinchi tomon BOʻLA "
                "OLMAYDI?</strong></p>",
        "choices": ["4", "5", "9", "15"],
        "correct": "4",
        "explanation": "<p><strong>4 boʻla olmaydi.</strong> Oraliq: "
                       "10 − 6 = 4 &lt; x &lt; 16. Chegaraning oʻzi "
                       "kirmaydi, demak x = 4 da uchburchak yassilanadi. "
                       "5, 9 va 15 esa oraliq ichida.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Toʻgʻri yoʻl eng "
                "qisqa» degan gap qaysi qoidadan kelib chiqadi?</strong></p>",
        "choices": [
            "Uchburchak tengsizligidan",
            "Burchaklar yigʻindisi qoidasidan",
            "Vertikal burchaklar tengligidan",
            "Parallel chiziqlar qoidasidan",
        ],
        "correct": "Uchburchak tengsizligidan",
        "explanation": "<p><strong>Uchburchak tengsizligidan.</strong> "
                       "a + b &gt; c degani: uchinchi nuqtaga burilib borish "
                       "(a + b) toʻgʻri yoʻldan (c) har doim uzun. Geometriya "
                       "shu tarzda kundalik tajribani isbotlaydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Masala: tomonlari 5 va 9 boʻlgan "
                "uchburchakning uchinchi tomoni.</p><p><strong>Yechim: "
                "4 ≤ x ≤ 14.</strong></p>",
        "choices": [
            "Chegaralar kirmaydi: 4 < x < 14",
            "Oraliq notoʻgʻri: 5 < x < 9",
            "Yuqori chegara 45 boʻlishi kerak",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Chegaralar kirmaydi: 4 < x < 14",
        "explanation": "<p><strong>Chegaralar kirmaydi.</strong> Sonlar "
                       "toʻgʻri (9 − 5 = 4 va 9 + 5 = 14), lekin belgi "
                       "notoʻgʻri. x = 4 yoki x = 14 boʻlsa uchburchak "
                       "yassilanib qoladi, shuning uchun qatʼiy &lt; "
                       "ishlatiladi.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Uchburchakning tomonlari 5, 8 va "
                "10.</p><p><strong>Yechim: eng katta burchak 5 uzunlikdagi "
                "tomonning qarshisida.</strong></p>",
        "choices": [
            "Eng katta burchak eng uzun tomon (10) qarshisida boʻladi",
            "Eng katta burchak 8 ning qarshisida boʻladi",
            "Burchaklar tomonlarga bogʻliq emas",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Eng katta burchak eng uzun tomon (10) qarshisida boʻladi",
        "explanation": "<p><strong>Eng uzun tomon qarshisida.</strong> Bogʻliqlik "
                       "toʻgʻri yoʻnalishda ishlaydi: katta tomon — katta "
                       "burchak. 5 ning qarshisida esa eng "
                       "<strong>kichik</strong> burchak turadi.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Sherbekning uyidan maktabgacha toʻgʻri yoʻl bilan 700 metr. "
                "Bekat orqali yursa, uydan bekatgacha 600 metr, bekatdan "
                "maktabgacha esa 350 metr.</p><p><strong>Toʻgʻri yoʻl necha "
                "metrga qisqa?</strong></p>",
        "choices": ["100 metr", "250 metr", "350 metr", "950 metr"],
        "correct": "250 metr",
        "explanation": "<p><strong>250 metr.</strong> Bekat orqali: "
                       "600 + 350 = 950 m. Toʻgʻri yoʻl: 700 m. Farq: "
                       "950 − 700 = 250 m. Tekshirish — bunday uch nuqta "
                       "mavjudmi: 600 + 350 = 950 &gt; 700 ✓, "
                       "700 + 350 = 1050 &gt; 600 ✓, 700 + 600 = 1300 &gt; "
                       "350 ✓</p>",
    },
    {
        "text": "<p>Uch qishloq uchburchak hosil qiladi. A dan B gacha 12 km, "
                "B dan C gacha 9 km. Dilnoza A dan C ga toʻgʻri yoʻl bilan "
                "bordi.</p><p><strong>Uning yoʻli quyidagilardan qaysi biri "
                "BOʻLA OLMAYDI?</strong></p>",
        "choices": ["4 km", "15 km", "20 km", "22 km"],
        "correct": "22 km",
        "explanation": "<p><strong>22 km boʻla olmaydi.</strong> Oraliq: "
                       "12 − 9 = 3 &lt; AC &lt; 12 + 9 = 21. 22 km bu "
                       "oraliqdan tashqarida — aks holda A dan B va C orqali "
                       "borish (21 km) toʻgʻri yoʻldan qisqa chiqib qolardi, "
                       "bu esa mumkin emas. 4, 15 va 20 km esa oraliq "
                       "ichida.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-60 Mashq: Parallel chiziqlar va kesuvchi",
        "description": "20 savol — mos (F), almashinuvchi (Z) va bir tomonli (U) "
                       "burchaklar, bitta burchakdan sakkiztasi, teskari xulosa.",
        "tutorial":    "PM-60:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM60,
    },
    {
        "title":       "PM-61 Mashq: Uchburchak turlari va burchaklar yigʻindisi",
        "description": "20 savol — burchagi va tomoni boʻyicha turlari, 180° "
                       "qoidasi, nisbat bilan berilgan burchaklar.",
        "tutorial":    "PM-61:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM61,
    },
    {
        "title":       "PM-62 Mashq: Uchburchak tengsizligi",
        "description": "20 savol — uchburchak chiqadimi, uchinchi tomon oraligʻi "
                       "va katta burchak–katta tomon bogʻliqligi.",
        "tutorial":    "PM-62:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM62,
    },
]
