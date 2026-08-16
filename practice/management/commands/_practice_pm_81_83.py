# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-81, PM-82, PM-83 (aldamchi diagrammalar,
koʻpaytirish prinsipi, ehtimollik gʻoyasi).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: uchalasi ham `hard`.

⚠️ `choices` EKRANLANADI — HTML teg yoʻq.
⚠️ Kumulyativ:
   • PM-81 — aldamchi diagrammalar; foiz oʻzgarishi (PM-25) va yuza k²
     (PM-72) faol ishlatiladi;
   • PM-82 — faqat SANASH. ⛔ EHTIMOLLIK soʻzi yoʻq;
   • PM-83 — ehtimollik gʻoyasi va P = qulay ÷ jami. ⛔ Teskari hodisa
     QOIDA sifatida va tajriba (chastota → ehtimollik) PM-84 da.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_81_83.py --master=prime \\
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
# PM-81 — aldamchi diagrammalar
# =====================================================================

Q_PM81 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ustunli "
                "diagrammaning sonlar oʻqi qayerdan boshlanishi "
                "kerak?</strong></p>",
        "choices": [
            "Noldan",
            "Eng kichik qiymatdan",
            "Eng katta qiymatning yarmidan",
            "Istalgan qulay sondan",
        ],
        "correct": "Noldan",
        "explanation": "<p><strong>Noldan.</strong> Faqat shunda ustunlarning "
                       "uzunligi sonlarning nisbatini toʻgʻri koʻrsatadi. "
                       "Boshqa joydan boshlangan oʻq kichik farqni katta "
                       "qilib koʻrsatadi — bu eng keng tarqalgan hiyla.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Diagrammaning oʻqi 40 dan "
                "boshlangan. Ikkita ustun: 44 va 48.</p><p><strong>Ustunlar "
                "necha marta farq qilib koʻrinadi?</strong></p>",
        "choices": ["1,1 marta", "2 marta", "4 marta", "8 marta"],
        "correct": "2 marta",
        "explanation": "<p><strong>2 marta.</strong> Oʻqdan yuqorisi: "
                       "44 − 40 = 4 va 48 − 40 = 8, demak 8 ÷ 4 = 2. "
                       "<strong>1,1 marta</strong> — sonlarning haqiqiy "
                       "nisbati (48 ÷ 44), koʻzga koʻringani emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Reklamadagi rasmning "
                "tomoni 3 marta kattalashtirildi. Yuzasi necha marta "
                "oshadi?</strong></p>",
        "choices": ["3 marta", "6 marta", "9 marta", "27 marta"],
        "correct": "9 marta",
        "explanation": "<p><strong>9 marta.</strong> 3<sup>2</sup> = 9 "
                       "(PM-72). Koʻz uzunlikni emas, yuzani baholaydi — "
                       "shuning uchun «3 barobar» degan rasm toʻqqiz barobar "
                       "taassurot qoldiradi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Savdo 200 mln dan "
                "210 mln soʻmga oshdi. Bu necha foizga oshish?</strong></p>",
        "choices": ["5%", "10%", "21%", "105%"],
        "correct": "5%",
        "explanation": "<p><strong>5%.</strong> (210 − 200) ÷ 200 × 100 = 5% "
                       "(PM-25). Asos — <em>eski</em> son. Oʻsish bor, lekin "
                       "u kichik: «oʻsish!» degan yozuv buni yashiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Aldamchi "
                "diagrammadagi eng koʻp uchraydigan hiyla qaysi?</strong></p>",
        "choices": [
            "Oʻqning noldan boshlanmagani",
            "Ustunlarning rangi",
            "Sarlavhaning uzunligi",
            "Ustunlarning soni",
        ],
        "correct": "Oʻqning noldan boshlanmagani",
        "explanation": "<p><strong>Oʻqning noldan boshlanmagani.</strong> "
                       "Odam ustunning uzunligiga qaraydi, oʻqdagi mayda "
                       "raqamlarga emas — shuning uchun bu hiyla deyarli "
                       "har doim ishlaydi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Reklamada ikkita ustun: 92 va 96. "
                "Diagrammaning oʻqi 90 dan boshlangan.</p><p><strong>Ustunlar "
                "necha marta farq qilib koʻrinadi?</strong></p>",
        "choices": ["1,04 marta", "2 marta", "3 marta", "4 marta"],
        "correct": "3 marta",
        "explanation": "<p><strong>3 marta.</strong> Oʻqdan yuqorisi: "
                       "92 − 90 = 2 va 96 − 90 = 6, demak 6 ÷ 2 = 3. "
                       "Reklamadagi «3 barobar» — aynan shu ustunlarning "
                       "nisbati.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Oʻsha reklamadagi sonlar: 92 va "
                "96 mg.</p><p><strong>Haqiqiy farq necha foiz?</strong></p>",
        "choices": ["4,3%", "8,3%", "50%", "300%"],
        "correct": "4,3%",
        "explanation": "<p><strong>4,3%.</strong> Farq: 96 − 92 = 4. Asos — "
                       "raqibning 92 tasi: 4 ÷ 92 × 100 = 4,34…% ≈ 4,3%. "
                       "Ustunlar 3 barobar farq qilib koʻrinsa ham, haqiqiy "
                       "farq besh foizga ham yetmaydi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Diagrammaning oʻqi 46 dan "
                "boshlangan. Ustunlar: 48 va 52.</p><p><strong>Ular necha "
                "marta farq qilib koʻrinadi?</strong></p>",
        "choices": ["1,08 marta", "2 marta", "3 marta", "6 marta"],
        "correct": "3 marta",
        "explanation": "<p><strong>3 marta.</strong> 48 − 46 = 2 va "
                       "52 − 46 = 6, demak 6 ÷ 2 = 3. "
                       "<strong>1,08 marta</strong> — sonlarning haqiqiy "
                       "nisbati (52 ÷ 48).</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>48 dan 52 ga oʻsish necha "
                "foiz?</strong></p>",
        "choices": ["4%", "7,7%", "8,3%", "108%"],
        "correct": "8,3%",
        "explanation": "<p><strong>8,3%.</strong> (52 − 48) ÷ 48 × 100 = "
                       "8,33…%. <strong>7,7%</strong> — asos qilib 52 "
                       "olingan (4 ÷ 52); oshishda asos har doim "
                       "<em>eski</em> son (PM-25).</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Belgining tomoni 2 marta "
                "kattalashtirildi. Uning yuzasi necha marta oshadi?</strong></p>",
        "choices": ["2 marta", "4 marta", "6 marta", "8 marta"],
        "correct": "4 marta",
        "explanation": "<p><strong>4 marta.</strong> 2<sup>2</sup> = 4. "
                       "Katta kvadratga kichigidan roppa-rosa toʻrttasi "
                       "sigʻadi. <strong>8 marta</strong> — bu hajmning "
                       "qoidasi (2<sup>3</sup>), yassi rasmniki emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Doʻkonning savdosi olti oyda "
                "100 mln dan 88 mln soʻmga tushdi.</p><p><strong>Bu necha "
                "foizga kamayish?</strong></p>",
        "choices": ["8,8%", "12%", "13,6%", "88%"],
        "correct": "12%",
        "explanation": "<p><strong>12%.</strong> (100 − 88) ÷ 100 × 100 = 12%. "
                       "<strong>13,6%</strong> — asos qilib yangi son (88) "
                       "olingan; kamayishda ham asos eski son boʻladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Reklamada faqat uchta oy "
                "koʻrsatilgan: 90, 92 va 95 mln soʻm.</p><p><strong>Shu uch "
                "oyda savdo necha foizga oshgan?</strong></p>",
        "choices": ["5%", "5,6%", "12%", "95%"],
        "correct": "5,6%",
        "explanation": "<p><strong>5,6%.</strong> (95 − 90) ÷ 90 × 100 = "
                       "5,55…%. Bu rost, lekin bu faqat tanlangan uch oy — "
                       "butun olti oyda savdo aslida 12 foizga tushgan "
                       "boʻlishi mumkin.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nima uchun ustunli "
                "diagrammada oʻq noldan boshlanishi kerak?</strong></p>",
        "choices": [
            "Chunki aks holda ustunlarning nisbati sonlarning nisbatiga "
            "toʻgʻri kelmaydi",
            "Chunki nol chiroyli koʻrinadi",
            "Chunki manfiy sonlar boʻlishi mumkin",
            "Chunki shunday qilish osonroq",
        ],
        "correct": ("Chunki aks holda ustunlarning nisbati sonlarning "
                    "nisbatiga toʻgʻri kelmaydi"),
        "explanation": "<p><strong>Chunki nisbat buziladi.</strong> Oʻq 46 dan "
                       "boshlanganda 48 ning ustunidan 46 tasi kesib "
                       "tashlanadi — koʻzga koʻringan uzunlik endi sonni "
                       "emas, faqat oʻqdan yuqoridagi qoldiqni koʻrsatadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Reklamada «50 foizga koʻp!» "
                "deb yozilgan.</p><p><strong>Bu qanday holatda ham toʻgʻri "
                "boʻlishi mumkin?</strong></p>",
        "choices": [
            "2 tadan 3 taga oshganda",
            "Faqat juda katta sonlarda",
            "Faqat 50 dan 100 ga oshganda",
            "Hech qachon — bu har doim yolgʻon",
        ],
        "correct": "2 tadan 3 taga oshganda",
        "explanation": "<p><strong>2 tadan 3 taga.</strong> (3 − 2) ÷ 2 × 100 "
                       "= 50%. Foiz har doim <em>asos</em> bilan birga "
                       "aytilishi kerak: «nimadan 50 foiz?» degan savolsiz bu "
                       "yozuv hech nima demaydi (PM-23).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Diagrammada faqat mart, "
                "aprel va may koʻrsatilgan va savdo oʻsgan.</p><p><strong>Bundan "
                "yil davomida oʻsgan degan xulosa chiqarish "
                "mumkinmi?</strong></p>",
        "choices": [
            "Yoʻq — qolgan oylar boshqacha manzara koʻrsatishi mumkin",
            "Ha — uch oy yetarli",
            "Ha, agar oʻsish 5 foizdan koʻp boʻlsa",
            "Faqat diagramma ustunli boʻlsa",
        ],
        "correct": "Yoʻq — qolgan oylar boshqacha manzara koʻrsatishi mumkin",
        "explanation": "<p><strong>Yoʻq.</strong> Uch oyda 5,6% oʻsish olti "
                       "oylik 12% pasayish ichida boʻlishi mumkin. Agar "
                       "diagramma gʻalati davrni koʻrsatsa, buning sababi "
                       "bor — toʻliq maʼlumotni soʻrang.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Korxona «oʻrtacha maoshimiz "
                "yuqori» deb eʼlon berdi.</p><p><strong>Qachon bu son "
                "chalgʻitadi?</strong></p>",
        "choices": [
            "Bir-ikkita juda katta maosh oʻrtachani koʻtarib turganda",
            "Xodimlar soni koʻp boʻlganda",
            "Maoshlar bir-biriga yaqin boʻlganda",
            "Oʻrtacha butun son boʻlmaganda",
        ],
        "correct": "Bir-ikkita juda katta maosh oʻrtachani koʻtarib turganda",
        "explanation": "<p><strong>Chetki son boʻlganda.</strong> Bu "
                       "PM-79 dagi holat: oʻrtacha rost boʻlsa ham, "
                       "koʻpchilik undan kam olayotgan boʻlishi mumkin. "
                       "Bunday paytda mediana halolroq son.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>Diagrammaning oʻqi 46 dan "
                "boshlangan, ustunlar 48 va 52.<br>Xulosa: <strong>«C doʻkoni "
                "A dan uch barobar koʻp sotgan»</strong></p>",
        "choices": [
            "Oʻq noldan boshlanmagan; haqiqiy farq atigi 8,3%",
            "Ustunlar notoʻgʻri chizilgan",
            "Sonlar notoʻgʻri; toʻgʻrisi 46 va 52",
            "Xato yoʻq, xulosa toʻgʻri",
        ],
        "correct": "Oʻq noldan boshlanmagan; haqiqiy farq atigi 8,3%",
        "explanation": "<p><strong>Oʻq noldan boshlanmagan.</strong> Uch "
                       "barobar farq qiladigan narsa — ustunlarning oʻqdan "
                       "yuqoridagi qismi (2 va 6), doʻkonlarning savdosi "
                       "emas: (52 − 48) ÷ 48 × 100 = 8,3%.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Diagrammada qop rasmi ishlatilgan: "
                "ikkinchi qopning tomoni birinchisinikidan 2 marta "
                "katta.<br>Xulosa: <strong>«Demak hosil 2 barobar "
                "koʻp»</strong></p>",
        "choices": [
            "Rasmning yuzasi 4 marta katta — koʻz shuni koʻradi",
            "Rasm 2 marta emas, 3 marta katta",
            "Qop rasmini ishlatib boʻlmaydi",
            "Xato yoʻq, xulosa toʻgʻri",
        ],
        "correct": "Rasmning yuzasi 4 marta katta — koʻz shuni koʻradi",
        "explanation": "<p><strong>Yuzasi 4 marta katta.</strong> Tomonlar "
                       "2 marta oshsa, yuza 2<sup>2</sup> = 4 marta oshadi "
                       "(PM-72). Rasm «2 barobar» degan sonni koʻrsatmoqchi, "
                       "lekin koʻzga toʻrt barobar boʻlib koʻrinadi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Doʻkon reklamasida «Bizda ikki "
                "barobar arzon!» deb yozilgan. Diagrammada raqibning narxi "
                "5000, oʻzlariniki 4500 soʻm; oʻq esa 4000 dan "
                "boshlangan.</p><p><strong>Narxlar orasidagi haqiqiy farq "
                "necha foiz?</strong></p>",
        "choices": ["5%", "10%", "50%", "200%"],
        "correct": "10%",
        "explanation": "<p><strong>10%.</strong> Farq: 5000 − 4500 = 500. "
                       "Asos — raqibning 5000 tasi: 500 ÷ 5000 × 100 = 10%. "
                       "Ustunlar esa 1000 va 500 boʻlib koʻrinadi, yaʼni "
                       "2 marta — «ikki barobar» oʻsha yerdan olingan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki maktabning natijasi: A da "
                "oʻrtacha 78 ball, B da 76 ball. Diagrammaning oʻqi 75 dan "
                "boshlangan.</p><p><strong>Ustunlar necha marta farq qilib "
                "koʻrinadi?</strong></p>",
        "choices": ["1,03 marta", "2 marta", "3 marta", "26 marta"],
        "correct": "3 marta",
        "explanation": "<p><strong>3 marta.</strong> Oʻqdan yuqorisi: "
                       "78 − 75 = 3 va 76 − 75 = 1, demak 3 ÷ 1 = 3. Haqiqiy "
                       "farq esa (78 − 76) ÷ 76 × 100 = 2,6% — deyarli "
                       "sezilmaydigan farq uch barobarga aylantirilgan.</p>",
    },
]


# =====================================================================
# PM-82 — koʻpaytirish prinsipi
# =====================================================================

Q_PM82 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>4 xil muzqaymoq va 5 xil "
                "qoʻshimcha bor. Necha xil kombinatsiya boʻladi?</strong></p>",
        "choices": ["9", "20", "45", "54"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> 4 × 5 = 20. <strong>9</strong> "
                       "— qoʻshilgan (4 + 5); qoʻshish «yo muzqaymoq, yo "
                       "qoʻshimcha tanlayman» degan boshqa savolga javob "
                       "berardi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3 xil non va 3 xil pishloq bor. "
                "Necha xil buterbrod tayyorlash mumkin?</strong></p>",
        "choices": ["3", "6", "9", "27"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> 3 × 3 = 9. Har bir non har bir "
                       "pishloq bilan keladi. <strong>6</strong> — "
                       "qoʻshilgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Koʻpaytirish "
                "prinsipi nima deydi?</strong></p>",
        "choices": [
            "Bosqichlarning imkoniyatlari koʻpaytiriladi",
            "Bosqichlarning imkoniyatlari qoʻshiladi",
            "Eng katta imkoniyat olinadi",
            "Bosqichlar soni koʻpaytiriladi",
        ],
        "correct": "Bosqichlarning imkoniyatlari koʻpaytiriladi",
        "explanation": "<p><strong>Koʻpaytiriladi.</strong> Birinchi tanlovni "
                       "m xil, ikkinchisini n xil qilish mumkin boʻlsa, "
                       "ikkalasini birga m × n xil qilish mumkin. "
                       "<em>Bosqichlar soni</em> emas, ularning "
                       "imkoniyatlari koʻpaytiriladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2 xil non, 3 xil pishloq va "
                "4 xil sabzavot bor. Necha xil buterbrod?</strong></p>",
        "choices": ["9", "14", "24", "36"],
        "correct": "24",
        "explanation": "<p><strong>24.</strong> 2 × 3 × 4 = 24. Har bir yangi "
                       "bosqich yangi koʻpaytiruvchi qoʻshadi. "
                       "<strong>14</strong> — 2 × 3 + 4 hisoblangan; amallar "
                       "tartibi ham javobni buzadi (PM-5).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Ikkita zar tashlandi. Nechta "
                "natija boʻlishi mumkin?</strong></p>",
        "choices": ["12", "21", "36", "66"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> Har bir zarda 6 tadan natija: "
                       "6 × 6 = 36. <strong>12</strong> — qoʻshilgan "
                       "(6 + 6).</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>5 ta koʻylak va 3 ta shim bor. "
                "Necha xil kiyinish mumkin?</strong></p>",
        "choices": ["8", "15", "35", "53"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> 5 × 3 = 15. Daraxt chizsangiz, "
                       "beshta shoxning har biridan uchtadan tarmoq "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Qulfda uchta gʻildirak bor, har "
                "birida 0 dan 9 gacha raqam.</p><p><strong>Nechta kod boʻlishi "
                "mumkin?</strong></p>",
        "choices": ["30", "100", "720", "1000"],
        "correct": "1000",
        "explanation": "<p><strong>1000.</strong> 10 × 10 × 10 = 1000 — "
                       "000 dan 999 gacha. <strong>30</strong> — 10 × 3 "
                       "hisoblangan; bosqichlar soni koʻpaytiruvchi emas, "
                       "koʻpaytiruvchilar soni.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Tanga uch marta tashlandi. Nechta "
                "natija boʻlishi mumkin?</strong></p>",
        "choices": ["3", "6", "8", "9"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Har tashlashda 2 ta natija: "
                       "2 × 2 × 2 = 8. <strong>6</strong> — 2 × 3 "
                       "hisoblangan, <strong>9</strong> — 3<sup>2</sup>.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Uch xonali kod tuziladi, har "
                "xonaga 4 ta harfdan biri qoʻyiladi. Nechta kod boʻlishi "
                "mumkin?</strong></p>",
        "choices": ["12", "24", "64", "81"],
        "correct": "64",
        "explanation": "<p><strong>64.</strong> 4 × 4 × 4 = 64. Harflar "
                       "takrorlanishi mumkin, shuning uchun har xonada "
                       "baribir 4 ta imkoniyat qoladi. <strong>12</strong> — "
                       "4 × 3 hisoblangan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>6 ta koʻylak va 4 ta shim bor. "
                "Necha xil kiyinish mumkin?</strong></p>",
        "choices": ["10", "18", "24", "64"],
        "correct": "24",
        "explanation": "<p><strong>24.</strong> 6 × 4 = 24. Jadval bilan ham "
                       "tekshirsa boʻladi: 6 qator va 4 ustun, katakchalar "
                       "soni 24.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Daraxt diagrammasida ildizdan "
                "3 ta shox chiqadi, har bir shoxdan yana 2 tadan."
                "</p><p><strong>Nechta variant hosil boʻladi?</strong></p>",
        "choices": ["5", "6", "9", "11"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 3 × 2 = 6 — daraxtning oxirgi "
                       "nuqtalari soni. <strong>11</strong> — hamma nuqta "
                       "sanalgan (1 + 3 + 6); variant esa toʻliq bir yoʻl, "
                       "yaʼni faqat oxirgi uchlar.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Bufetda 2 xil salat, 5 xil taom "
                "va 3 xil ichimlik bor. Necha xil tushlik boʻladi?</strong></p>",
        "choices": ["10", "15", "30", "45"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> 2 × 5 × 3 = 30. Bosqichlarni "
                       "qaysi tartibda koʻpaytirsangiz ham javob bir xil "
                       "chiqadi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>3 ta koʻylak va 4 ta shim bor. "
                "Sherbek <em>faqat bitta</em> narsa sotib olmoqchi — yo "
                "koʻylak, yo shim.</p><p><strong>Necha xil tanlov "
                "bor?</strong></p>",
        "choices": ["7", "12", "24", "34"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Bu yerda «yoki» bor, demak "
                       "<em>qoʻshiladi</em>: 3 + 4 = 7. Agar «koʻylak "
                       "<em>va</em> shim» boʻlganida, 3 × 4 = 12 boʻlardi. "
                       "«Va» — koʻpaytirish, «yoki» — qoʻshish.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nega 3 ta koʻylak "
                "va 4 ta shim uchun 3 + 4 emas, 3 × 4 hisoblanadi?</strong></p>",
        "choices": [
            "Chunki har bir koʻylak har bir shim bilan kiyiladi",
            "Chunki koʻpaytirish qoʻshishdan katta javob beradi",
            "Chunki shimlar koʻproq",
            "Chunki koʻylak va shim har xil narsa",
        ],
        "correct": "Chunki har bir koʻylak har bir shim bilan kiyiladi",
        "explanation": "<p><strong>Har bir koʻylak har bir shim bilan.</strong> "
                       "Uchta koʻylakning har biriga toʻrttadan shim mos "
                       "keladi: 4 + 4 + 4, yaʼni 3 × 4. Daraxt diagrammasi "
                       "buni bir qarashda koʻrsatadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Toʻrt xonali kod tuziladi, "
                "har xonada 10 ta raqam.</p><p><strong>Qaysi hisob "
                "toʻgʻri?</strong></p>",
        "choices": [
            "10 × 10 × 10 × 10",
            "10 × 4",
            "10 + 10 + 10 + 10",
            "4 × 4 × 4 × 4",
        ],
        "correct": "10 × 10 × 10 × 10",
        "explanation": "<p><strong>10 × 10 × 10 × 10 = 10 000.</strong> Har "
                       "bir xona — alohida bosqich va har birida 10 ta "
                       "imkoniyat bor. <strong>10 × 4</strong> — bosqichlar "
                       "sonini koʻpaytiruvchi deb olish, klassik xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Daraxt "
                "diagrammasida variantlar sonini qanday topamiz?</strong></p>",
        "choices": [
            "Oxirgi nuqtalarni sanaymiz",
            "Hamma nuqtani sanaymiz",
            "Shoxlar sonini qoʻshamiz",
            "Ildizdan chiqqan shoxlarni sanaymiz",
        ],
        "correct": "Oxirgi nuqtalarni sanaymiz",
        "explanation": "<p><strong>Oxirgi nuqtalarni.</strong> Variant — bu "
                       "ildizdan oxirgi uchgacha boʻlgan <em>toʻliq</em> "
                       "yoʻl. Oraliq tugunlar tugallanmagan tanlovlar, "
                       "shuning uchun ular sanalmaydi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>3 ta koʻylak va 4 ta shim bilan "
                "necha xil kiyinish mumkin?<br>Yechim: <strong>3 + 4 = "
                "7</strong></p>",
        "choices": [
            "Qoʻshilgan; toʻgʻrisi 3 × 4 = 12",
            "Kam olingan; toʻgʻrisi 3 + 4 + 3 = 10",
            "Koʻylaklar ikki marta sanalishi kerak edi",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Qoʻshilgan; toʻgʻrisi 3 × 4 = 12",
        "explanation": "<p><strong>Qoʻshilgan.</strong> Koʻylak <em>va</em> "
                       "shim birga kiyiladi, shuning uchun koʻpaytiriladi: "
                       "3 × 4 = 12. Qoʻshish faqat «yo u, yo bu» degan "
                       "savolda toʻgʻri boʻlardi.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Uch xonali kod, har xonada "
                "10 raqam.<br>Yechim: <strong>10 × 3 = 30</strong></p>",
        "choices": [
            "Bosqichlar soniga koʻpaytirilgan; toʻgʻrisi 10 × 10 × 10 = 1000",
            "Qoʻshish kerak edi; toʻgʻrisi 30",
            "Har xonada 9 ta raqam bor; toʻgʻrisi 729",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": ("Bosqichlar soniga koʻpaytirilgan; toʻgʻrisi "
                    "10 × 10 × 10 = 1000"),
        "explanation": "<p><strong>Bosqichlar soniga koʻpaytirilgan.</strong> "
                       "Uchta bosqich — uchta <em>oʻnlik</em> koʻpaytiriladi, "
                       "10 ni 3 ga emas. Tekshirish oson: 000 dan 999 gacha "
                       "roppa-rosa 1000 ta kod bor.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Maktab bufetida 3 xil birinchi "
                "taom, 4 xil ikkinchi taom va 2 xil ichimlik bor. Tushlik — "
                "har biridan bittadan.</p><p><strong>Necha xil tushlik boʻlishi "
                "mumkin?</strong></p>",
        "choices": ["9 xil", "14 xil", "24 xil", "36 xil"],
        "correct": "24 xil",
        "explanation": "<p><strong>24 xil.</strong> 3 × 4 × 2 = 24. "
                       "Bosqichma-bosqich: 3 × 4 = 12 (taomlar), keyin "
                       "12 × 2 = 24 (ichimlik ham). Bu 20 ta oʻquv kunidan "
                       "koʻp — bir oy davomida har kuni boshqacha tushlik "
                       "qilish mumkin.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Afsonaning 5 ta koʻylagi, 3 ta "
                "yubkasi va 2 ta sharfi bor. U har kuni boshqacha kiyinmoqchi "
                "va har safar uchalasini ham kiyadi.</p><p><strong>Necha kunga "
                "yetadi?</strong></p>",
        "choices": ["10 kunga", "16 kunga", "30 kunga", "60 kunga"],
        "correct": "30 kunga",
        "explanation": "<p><strong>30 kunga.</strong> 5 × 3 × 2 = 30 ta "
                       "variant, demak 30 kun. <strong>10 kunga</strong> — "
                       "qoʻshilgan (5 + 3 + 2). Ikki oy taxminan 60 kun, "
                       "shuning uchun bu yarmigagina yetadi.</p>",
    },
]


# =====================================================================
# PM-83 — ehtimollik gʻoyasi
# =====================================================================

Q_PM83 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>Tanga tashlandi. Gerb tushish "
                "ehtimolligi qancha?</strong></p>",
        "choices": ["0,25", "0,5", "1", "2"],
        "correct": "0,5",
        "explanation": "<p><strong>0,5.</strong> Ikkita teng imkoniyatli "
                       "natijadan bittasi qulay: 1 ÷ 2 = 0,5 = 50%. "
                       "<strong>2</strong> — natijalar soni, ehtimollik "
                       "emas; ehtimollik 1 dan katta boʻlmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Zar tashlandi. 3 tushish "
                "ehtimolligi qancha?</strong></p>",
        "choices": ["0,17", "0,3", "0,5", "3"],
        "correct": "0,17",
        "explanation": "<p><strong>0,17 (yaʼni 1 ÷ 6 ≈ 0,1666…).</strong> "
                       "Oltita yoqdan bittasi qulay. <strong>3</strong> — "
                       "yoqning raqami, ehtimollik emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ehtimollik qanday "
                "chegaralar orasida boʻladi?</strong></p>",
        "choices": [
            "0 bilan 1 orasida",
            "0 bilan 100 orasida",
            "1 bilan 6 orasida",
            "Har qanday son boʻlishi mumkin",
        ],
        "correct": "0 bilan 1 orasida",
        "explanation": "<p><strong>0 bilan 1 orasida.</strong> Qulay hollar "
                       "jami hollardan koʻp boʻlolmaydi, shuning uchun "
                       "boʻlinma 1 dan oshmaydi. Foizda yozilganda esa "
                       "0% dan 100% gacha boʻladi — bu oʻsha narsa.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Zarda juft son tushish "
                "ehtimolligi qancha?</strong></p>",
        "choices": ["0,17", "0,33", "0,5", "3"],
        "correct": "0,5",
        "explanation": "<p><strong>0,5.</strong> Juft sonlar 2, 4 va 6 — "
                       "uchta qulay hol: 3 ÷ 6 = 0,5. <strong>0,33</strong> "
                       "— ikkita qulay hol boʻlganda chiqardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Imkonsiz hodisaning "
                "ehtimolligi qancha?</strong></p>",
        "choices": ["−1", "0", "0,5", "1"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Imkonsiz hodisa hech qachon "
                       "roʻy bermaydi, demak qulay hollar soni nol: "
                       "0 ÷ 6 = 0. Masalan oddiy zarda 7 tushishi. "
                       "Ehtimollik manfiy boʻlmaydi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>Zarda 4 dan katta son tushish "
                "ehtimolligi qancha?</strong></p>",
        "choices": ["0,17", "0,33", "0,5", "0,67"],
        "correct": "0,33",
        "explanation": "<p><strong>0,33 (2 ÷ 6 = <sup>1</sup>/<sub>3</sub>)."
                       "</strong> Qulay hollar 5 va 6 — ikkitasi. "
                       "<strong>0,67</strong> — «4 dan kichik yoki teng» "
                       "boʻlganda chiqardi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Qopchada 4 ta qizil va 6 ta koʻk "
                "shar bor.</p><p><strong>Koʻk shar chiqish ehtimolligi "
                "qancha?</strong></p>",
        "choices": ["0,4", "0,6", "1,5", "6"],
        "correct": "0,6",
        "explanation": "<p><strong>0,6.</strong> Jami sharlar: 4 + 6 = 10. "
                       "Qulay hollar 6 ta: 6 ÷ 10 = 0,6 = 60%. "
                       "<strong>1,5</strong> — 6 ÷ 4 hisoblangan; maxrajda "
                       "<em>hamma</em> sharlar turadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Lotereyada 20 ta bilet bor, "
                "5 tasi yutuqli. Bitta bilet olindi.</p><p><strong>Yutish "
                "ehtimolligi necha foiz?</strong></p>",
        "choices": ["5%", "20%", "25%", "75%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> 5 ÷ 20 = 0,25 = 25%. "
                       "<strong>75%</strong> — yutmaslik ehtimolligi. "
                       "<strong>5%</strong> — yutuqli biletlar sonining "
                       "oʻzi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Oʻsha lotereyada 20 ta biletdan "
                "5 tasi yutuqli.</p><p><strong>Yutmaslik ehtimolligi "
                "qancha?</strong></p>",
        "choices": ["0,25", "0,5", "0,75", "15"],
        "correct": "0,75",
        "explanation": "<p><strong>0,75.</strong> Yutuqsiz biletlar: "
                       "20 − 5 = 15 ta, demak 15 ÷ 20 = 0,75 = 75%. "
                       "Diqqat: 0,25 + 0,75 = 1 — bu tasodif emas, ikkala "
                       "hodisa birgalikda hamma hollarni qamrab oladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Zarda 5 dan kichik son tushish "
                "ehtimolligi qancha?</strong></p>",
        "choices": ["0,33", "0,5", "0,67", "0,83"],
        "correct": "0,67",
        "explanation": "<p><strong>0,67 (4 ÷ 6 = <sup>2</sup>/<sub>3</sub>)."
                       "</strong> Qulay hollar 1, 2, 3 va 4 — toʻrttasi. "
                       "<strong>0,83</strong> — beshta qulay hol boʻlganda "
                       "(5 ÷ 6), yaʼni «6 dan kichik» boʻlganda.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Qopchada 3 ta qizil va 7 ta koʻk "
                "shar bor.</p><p><strong>Qizil shar chiqish ehtimolligi "
                "qancha?</strong></p>",
        "choices": ["0,3", "0,43", "0,7", "3"],
        "correct": "0,3",
        "explanation": "<p><strong>0,3.</strong> Jami 3 + 7 = 10 ta shar, "
                       "qulay hollar 3 ta: 3 ÷ 10 = 0,3 = 30%. "
                       "<strong>0,43</strong> — 3 ÷ 7 hisoblangan, yaʼni "
                       "maxrajga faqat koʻk sharlar olingan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>0,5 ehtimollik "
                "boshqa qanday yoziladi?</strong></p>",
        "choices": [
            "1/2 yoki 50%",
            "5% yoki 1/5",
            "1/5 yoki 20%",
            "2/1 yoki 200%",
        ],
        "correct": "1/2 yoki 50%",
        "explanation": "<p><strong>1/2 yoki 50%.</strong> Ehtimollikni kasr, "
                       "oʻnlik kasr yoki foiz bilan yozish mumkin — bu "
                       "PM-22 dagi bitta sonning uch xil libosi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻquvchi hisoblab, "
                "ehtimollik 1,2 chiqdi.</p><p><strong>Bu nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Hisobda xato bor — ehtimollik 1 dan katta boʻlmaydi",
            "Hodisa juda ehtimolli",
            "Hodisa aniq roʻy beradi",
            "Javobni 100 ga boʻlish kerak",
        ],
        "correct": "Hisobda xato bor — ehtimollik 1 dan katta boʻlmaydi",
        "explanation": "<p><strong>Hisobda xato bor.</strong> Qulay hollar "
                       "jami hollardan koʻp boʻlishi mumkin emas. Koʻpincha "
                       "sabab: boʻlish teskari qilingan yoki qulay hollar "
                       "notoʻgʻri sanalgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi biri "
                "ehtimolliroq: zarda juft son tushishimi yoki 5 dan kichik "
                "son tushishimi?</strong></p>",
        "choices": [
            "5 dan kichik son (0,67)",
            "Juft son (0,5)",
            "Ikkalasi teng",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "5 dan kichik son (0,67)",
        "explanation": "<p><strong>5 dan kichik son.</strong> Juft: 2, 4, 6 → "
                       "3 ÷ 6 = 0,5. Beshdan kichik: 1, 2, 3, 4 → "
                       "4 ÷ 6 ≈ 0,67. Solishtirish uchun ikkalasini bir xil "
                       "koʻrinishga keltiring.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Ertaga yo yomgʻir yogʻadi, "
                "yo yogʻmaydi — ikkita natija bor, demak ehtimollik 0,5.»"
                "</p><p><strong>Bu fikr toʻgʻrimi?</strong></p>",
        "choices": [
            "Yoʻq — formula faqat teng imkoniyatli hollarda ishlaydi",
            "Ha — ikkita natija bor",
            "Ha, agar yozda boʻlsa",
            "Yoʻq — ehtimollik 1 boʻlishi kerak",
        ],
        "correct": "Yoʻq — formula faqat teng imkoniyatli hollarda ishlaydi",
        "explanation": "<p><strong>Yoʻq.</strong> Yomgʻir yogʻishi va "
                       "yogʻmasligi teng imkoniyatli emas — tanga yoki zardan "
                       "farqli oʻlaroq. Bunday ehtimollikni oʻlchash uchun "
                       "koʻp yillik kuzatuv maʼlumoti kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>P = qulay ÷ jami "
                "formulasida maxrajda nima turadi?</strong></p>",
        "choices": [
            "Hamma mumkin boʻlgan natijalar",
            "Faqat qulay boʻlmagan natijalar",
            "Qulay natijalar",
            "Tajribalar soni",
        ],
        "correct": "Hamma mumkin boʻlgan natijalar",
        "explanation": "<p><strong>Hamma natijalar.</strong> 3 qizil va "
                       "7 koʻk shar boʻlsa, maxrajda 10 turadi — 7 emas. "
                       "Maxrajga faqat «boshqalarni» qoʻyish eng koʻp "
                       "uchraydigan xato.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>Zarda juft son tushish ehtimolligi "
                "topilmoqda.<br>Yechim: <strong>6 ÷ 3 = 2</strong></p>",
        "choices": [
            "Boʻlish teskari; toʻgʻrisi 3 ÷ 6 = 0,5",
            "Qulay hollar 2 ta; toʻgʻrisi 2 ÷ 6",
            "Jami hollar 3 ta; toʻgʻrisi 1",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Boʻlish teskari; toʻgʻrisi 3 ÷ 6 = 0,5",
        "explanation": "<p><strong>Boʻlish teskari.</strong> Yuqorida qulay "
                       "hollar (3 ta juft son), pastda jami hollar (6 ta yoq) "
                       "turadi. Javob 2 chiqishi darrov xato ekanini "
                       "koʻrsatadi — ehtimollik 1 dan katta boʻlmaydi.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Qopchada 3 qizil va 7 koʻk shar "
                "bor.<br>Yechim: <strong>P(qizil) = 3 ÷ 7 ≈ 0,43</strong></p>",
        "choices": [
            "Maxrajda hamma sharlar turishi kerak; toʻgʻrisi 3 ÷ 10 = 0,3",
            "Qulay hollar 7 ta; toʻgʻrisi 7 ÷ 10",
            "Sharlar qoʻshilishi kerak edi; toʻgʻrisi 10",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": ("Maxrajda hamma sharlar turishi kerak; toʻgʻrisi "
                    "3 ÷ 10 = 0,3"),
        "explanation": "<p><strong>Maxrajda hamma sharlar.</strong> Jami "
                       "3 + 7 = 10 ta shar bor, shuning uchun P = 3 ÷ 10 = "
                       "0,3. Maxrajga faqat koʻk sharlarni qoʻyish "
                       "ehtimollikni oshirib yuboradi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Qopchada 3 ta qizil va 7 ta koʻk "
                "shar bor. Dilnoza qizil shar chiqish ehtimolligini 0,5 ga "
                "yetkazmoqchi va faqat qizil shar qoʻshadi.</p><p><strong>Nechta "
                "qizil shar qoʻshishi kerak?</strong></p>",
        "choices": ["2 ta", "4 ta", "5 ta", "7 ta"],
        "correct": "4 ta",
        "explanation": "<p><strong>4 ta.</strong> Ehtimollik 0,5 boʻlishi "
                       "uchun qizil va koʻk sharlar teng boʻlishi kerak. Koʻk "
                       "sharlar 7 ta va ular oʻzgarmaydi, demak qizil ham "
                       "7 ta boʻlishi kerak: 7 − 3 = 4 ta qoʻshiladi. "
                       "Tekshirish: 7 ÷ 14 = 0,5 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sinfda 25 oʻquvchi bor, ulardan "
                "10 tasi qiz. Oʻqituvchi tasodifan bitta oʻquvchini "
                "chaqiradi.</p><p><strong>Chaqirilgan oʻquvchi qiz boʻlish "
                "ehtimolligi necha foiz?</strong></p>",
        "choices": ["10%", "25%", "40%", "60%"],
        "correct": "40%",
        "explanation": "<p><strong>40%.</strong> 10 ÷ 25 = 0,4 = 40%. "
                       "<strong>60%</strong> — oʻgʻil boʻlish ehtimolligi "
                       "(15 ÷ 25). <strong>10%</strong> — qizlar sonining "
                       "oʻzi foiz deb olingan.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-81 Mashq: Aldamchi diagrammalar",
        "tutorial":    "PM-81:",
        "description": (
            "Kesilgan oʻq, belgi yuzasi, tanlangan davr va asossiz foiz — "
            "diagramma qanday aldashini fosh qilish. 20 savol."
        ),
        "questions":   Q_PM81,
        **DEFAULTS,
    },
    {
        "title":       "PM-82 Mashq: Sanash: koʻpaytirish prinsipi",
        "tutorial":    "PM-82:",
        "description": (
            "Variantlarni sanash, daraxt diagrammasi, koʻp bosqichli tanlov "
            "va kodlar soni. 20 savol."
        ),
        "questions":   Q_PM82,
        **DEFAULTS,
    },
    {
        "title":       "PM-83 Mashq: Ehtimollik gʻoyasi",
        "tutorial":    "PM-83:",
        "description": (
            "0 dan 1 gacha shkala, P = qulay ÷ jami, imkonsiz va aniq "
            "hodisalar, kasr–oʻnlik–foiz. 20 savol."
        ),
        "questions":   Q_PM83,
        **DEFAULTS,
    },
]
