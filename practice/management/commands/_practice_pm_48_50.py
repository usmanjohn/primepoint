# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-48, PM-49, PM-50 (grafik, y = kx + b, k va b).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: `medium` (Blok D).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq. Darajalar «x^2» koʻrinishida
   yoziladi, savol matnida esa <sup> ishlatiladi.
⚠️ Kumulyativ: ikki chiziqning kesishishini ALGEBRA bilan yechish yoʻq
   (PM-52); parabola yoʻq (PM-56). Taqqoslash faqat konkret x larda,
   jadval orqali.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_48_50.py --master=prime \\
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
# PM-48 — jadvaldan grafikka
# =====================================================================

Q_PM48 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x + 2 boʻlsa, "
                "x = 3 ga qaysi nuqta mos keladi?</strong></p>",
        "choices": ["(3; 5)", "(5; 3)", "(3; 6)", "(2; 3)"],
        "correct": "(3; 5)",
        "explanation": "<p><strong>(3; 5).</strong> y = 3 + 2 = 5, nuqta esa "
                       "(kirish; chiqish) tartibida yoziladi. "
                       "<strong>(5; 3)</strong> — koordinatalar oʻrni almashgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Jadval: x = 0 da y = 1; x = 1 da "
                "y = 3; x = 2 da y = 5.</p><p><strong>Bu qaysi nuqtalarni "
                "beradi?</strong></p>",
        "choices": [
            "(0; 1), (1; 3), (2; 5)",
            "(1; 0), (3; 1), (5; 2)",
            "(0; 1), (3; 1), (5; 2)",
            "(1; 3), (3; 5), (5; 7)",
        ],
        "correct": "(0; 1), (1; 3), (2; 5)",
        "explanation": "<p><strong>(0; 1), (1; 3), (2; 5).</strong> Jadvalning "
                       "yuqori qatori — abssissalar, pastki qatori — ordinatalar. "
                       "Har bir ustun bitta nuqta beradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Funksiyaning grafigi "
                "nima?</strong></p>",
        "choices": [
            "Uning barcha (x; y) juftliklaridan hosil boʻlgan shakl",
            "Faqat jadvalga yozilgan nuqtalar",
            "Koordinata oʻqlarining oʻzi",
            "Funksiyaning formulasi",
        ],
        "correct": "Uning barcha (x; y) juftliklaridan hosil boʻlgan shakl",
        "explanation": "<p><strong>Barcha (x; y) juftliklaridan hosil boʻlgan "
                       "shakl.</strong> Jadvalga bir nechta nuqta tushadi, grafik "
                       "esa ular orasidagi va ulardan naridagi nuqtalarni ham "
                       "oʻz ichiga oladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 2x boʻlsa, x = 4 ga "
                "qaysi nuqta mos keladi?</strong></p>",
        "choices": ["(4; 6)", "(4; 8)", "(8; 4)", "(2; 8)"],
        "correct": "(4; 8)",
        "explanation": "<p><strong>(4; 8).</strong> y = 2 × 4 = 8. "
                       "<strong>(4; 6)</strong> — koʻpaytirish oʻrniga qoʻshilgan "
                       "javob (4 + 2).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>(2; 7) nuqtasi "
                "y = 3x + 1 grafigida yotadimi?</strong></p>",
        "choices": [
            "Ha, chunki 3 × 2 + 1 = 7",
            "Yoʻq, chunki 3 × 2 + 1 = 6",
            "Yoʻq, chunki 3 + 2 + 1 = 6",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Ha, chunki 3 × 2 + 1 = 7",
        "explanation": "<p><strong>Ha.</strong> Nuqta grafikda yotishini tekshirish "
                       "— uning koordinatalarini formulaga qoʻyish demakdir. "
                       "x = 2 qoʻysak, 3 × 2 + 1 = 7 chiqadi va bu nuqtaning "
                       "ordinatasiga teng.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x − 3 funksiyasining "
                "x = 0, 1, 2, 3 dagi qiymatlari qanday?</strong></p>",
        "choices": [
            "−3, −2, −1, 0",
            "3, 2, 1, 0",
            "−3, −4, −5, −6",
            "0, 1, 2, 3",
        ],
        "correct": "−3, −2, −1, 0",
        "explanation": "<p><strong>−3, −2, −1, 0.</strong> Har safar x dan 3 "
                       "ayriladi. <strong>3, 2, 1, 0</strong> — 3 dan x ayrilgan "
                       "javob, yaʼni y = 3 − x funksiyasi; bu boshqa "
                       "funksiya.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi nuqta y = 2x + 1 "
                "grafigida yotadi?</strong></p>",
        "choices": ["(0; 2)", "(1; 3)", "(2; 4)", "(3; 6)"],
        "correct": "(1; 3)",
        "explanation": "<p><strong>(1; 3).</strong> 2 × 1 + 1 = 3 ✓ "
                       "Qolganlari: x = 0 da 1 (2 emas), x = 2 da 5 (4 emas), "
                       "x = 3 da 7 (6 emas).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = 5 − x boʻlsa, x = −2 da y nechaga "
                "teng?</strong></p>",
        "choices": ["3", "5", "7", "10"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 5 − (−2) = 5 + 2 = 7. Manfiy sonni "
                       "ayirish — uni qoʻshish demakdir (PM-10). "
                       "<strong>3</strong> — minus eʼtibordan chiqib, 5 − 2 "
                       "hisoblangan javob.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 4x + 3 grafigi Oy "
                "oʻqini qaysi nuqtada kesadi?</strong></p>",
        "choices": ["(0; 3)", "(0; 4)", "(3; 0)", "(4; 0)"],
        "correct": "(0; 3)",
        "explanation": "<p><strong>(0; 3).</strong> Oy oʻqida abssissa nol "
                       "(PM-45), demak x = 0 qoʻyamiz: y = 0 + 3 = 3. "
                       "<strong>(3; 0)</strong> — koordinatalar oʻrni almashgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x − 4 grafigi Ox "
                "oʻqini qaysi nuqtada kesadi?</strong></p>",
        "choices": ["(−4; 0)", "(0; −4)", "(4; 0)", "(0; 4)"],
        "correct": "(4; 0)",
        "explanation": "<p><strong>(4; 0).</strong> Ox oʻqida ordinata nol, demak "
                       "y = 0 qoʻyamiz: x − 4 = 0 → x = 4. "
                       "<strong>(0; −4)</strong> — bu Oy oʻqini kesish "
                       "nuqtasi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Grafikda bitta katak 5 birlikni "
                "bildiradi.</p><p><strong>Nuqta Ox oʻqidan 3 katak yuqorida boʻlsa, "
                "uning ordinatasi nechaga teng?</strong></p>",
        "choices": ["3", "5", "8", "15"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> 3 × 5 = 15. <strong>3</strong> — "
                       "shkalani oʻqimay, har katakni 1 birlik deb olgan javob; "
                       "bu grafik oʻqishdagi eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = −x + 1 boʻlsa, x = 3 da y nechaga "
                "teng?</strong></p>",
        "choices": ["−4", "−2", "2", "4"],
        "correct": "−2",
        "explanation": "<p><strong>−2.</strong> −3 + 1 = −2. <strong>4</strong> — "
                       "minus eʼtibordan chiqib, 3 + 1 hisoblangan javob.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi maʼlumotning "
                "nuqtalarini chiziq bilan bogʻlash mumkin EMAS?</strong></p>",
        "choices": [
            "Sotilgan chiptalar soni",
            "Kun davomidagi harorat",
            "Bosib oʻtilgan masofa",
            "Bakdagi suv miqdori",
        ],
        "correct": "Sotilgan chiptalar soni",
        "explanation": "<p><strong>Sotilgan chiptalar soni.</strong> Chipta faqat "
                       "butun sonda sanaladi — 2,5 ta chipta yoʻq, demak "
                       "nuqtalar orasida hech narsa yoʻq. Harorat, masofa va suv "
                       "esa uzluksiz oʻzgaradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x + 2 grafigida "
                "(3; 5) va (5; 3) nuqtalaridan qaysi biri yotadi?</strong></p>",
        "choices": [
            "Faqat (3; 5)",
            "Faqat (5; 3)",
            "Ikkalasi ham",
            "Hech qaysisi",
        ],
        "correct": "Faqat (3; 5)",
        "explanation": "<p><strong>Faqat (3; 5).</strong> 3 + 2 = 5 ✓, lekin "
                       "5 + 2 = 7 ≠ 3. Nuqtadagi sonlar bir xil boʻlsa ham, "
                       "tartib har xil — demak nuqtalar har xil.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Grafikdan x = 4 dagi y "
                "ni oʻqish uchun nima qilinadi?</strong></p>",
        "choices": [
            "x oʻqida 4 ni topib, chiziqqa qadar tik yuriladi, keyin y oʻqiga "
            "burilinadi",
            "y oʻqida 4 ni topib, chiziqqa qadar oʻngga yuriladi",
            "Koordinata boshidan 4 katak sanaladi",
            "Chiziqning eng yuqori nuqtasi olinadi",
        ],
        "correct": "x oʻqida 4 ni topib, chiziqqa qadar tik yuriladi, keyin "
                   "y oʻqiga burilinadi",
        "explanation": "<p><strong>x oʻqidan boshlanadi.</strong> Kirish gorizontal "
                       "oʻqda, chiqish esa vertikalda. Ikkinchi variant — teskari "
                       "savolning yoʻli: y maʼlum boʻlganda x ni topish.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki jadval: A da y qiymatlari "
                "2, 4, 6, 8; B da y qiymatlari 1, 4, 9, 16 (x = 1, 2, 3, 4).</p>"
                "<p><strong>Qaysi biri toʻgʻri chiziq beradi?</strong></p>",
        "choices": ["A", "B", "Ikkalasi ham", "Hech qaysisi"],
        "correct": "A",
        "explanation": "<p><strong>A.</strong> A da har qadamda y aynan 2 ga "
                       "oʻsadi — bir xil qadam toʻgʻri chiziq beradi. B da esa "
                       "qadamlar 3, 5, 7 — oʻzgarib boradi, shuning uchun grafik "
                       "egri chiziq boʻladi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Jadvalda x = 2, y = 5 edi. Afsona "
                "nuqtani 5 katak oʻngga va 2 katak yuqoriga qoʻydi.</p>"
                "<p><strong>Toʻgʻri javob qaysi?</strong></p>",
        "choices": [
            "2 katak oʻngga, 5 katak yuqoriga — nuqta (2; 5)",
            "5 katak oʻngga, 2 katak yuqoriga — Afsona haq",
            "5 katak yuqoriga, 2 katak oʻngga",
            "2 katak chapga, 5 katak yuqoriga",
        ],
        "correct": "2 katak oʻngga, 5 katak yuqoriga — nuqta (2; 5)",
        "explanation": "<p><strong>2 katak oʻngga, 5 katak yuqoriga.</strong> "
                       "Grafikda gorizontal yoʻnalish har doim kirish (x), "
                       "vertikal esa chiqish (y). Afsona jadvalning ikki qatorini "
                       "almashtirib yuborgan.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Bekzod «nechta daftar — qancha pul» "
                "maʼlumotining nuqtalarini toʻgʻri chiziq bilan tutashtirdi.</p>"
                "<p><strong>Toʻgʻri javob qaysi?</strong></p>",
        "choices": [
            "Nuqtalar bogʻlanmaydi, chunki 2,5 ta daftar boʻlmaydi",
            "Nuqtalar bogʻlanadi — Bekzod haq",
            "Nuqtalarni egri chiziq bilan bogʻlash kerak",
            "Bunday maʼlumotni umuman chizib boʻlmaydi",
        ],
        "correct": "Nuqtalar bogʻlanmaydi, chunki 2,5 ta daftar boʻlmaydi",
        "explanation": "<p><strong>Nuqtalar bogʻlanmaydi.</strong> Chiziq «orada "
                       "ham qiymat bor» deganini bildiradi. Daftar diskret "
                       "miqdor — faqat butun sonda sanaladi, shuning uchun "
                       "nuqtalar shundayligicha qoldiriladi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Bakda boshida 5 litr suv bor edi. Jomrat ochildi va bak har "
                "daqiqada 3 litrdan toʻla boshladi.</p><p><strong>6 daqiqadan "
                "keyin bakda qancha suv boʻladi?</strong></p>",
        "choices": ["18 litr", "21 litr", "23 litr", "30 litr"],
        "correct": "23 litr",
        "explanation": "<p><strong>23 litr.</strong> Qoida: y = 3x + 5. "
                       "3 × 6 + 5 = 18 + 5 = 23. <strong>18 litr</strong> — "
                       "boshidagi 5 litrni qoʻshishni unutgan javob.</p>",
    },
    {
        "text": "<p>Bir haftalik harorat: dushanba 3°, seshanba 5°, chorshanba 8°, "
                "payshanba 6°, juma 2°, shanba −1°, yakshanba −4°.</p>"
                "<p><strong>Eng yuqori va eng past harorat orasidagi farq "
                "qancha?</strong></p>",
        "choices": ["4 daraja", "8 daraja", "12 daraja", "14 daraja"],
        "correct": "12 daraja",
        "explanation": "<p><strong>12 daraja.</strong> Eng yuqori 8° (chorshanba), "
                       "eng past −4° (yakshanba). Farq: |8 − (−4)| = 8 + 4 = 12 "
                       "(PM-41, PM-46). <strong>4 daraja</strong> — minus "
                       "eʼtibordan chiqib, 8 − 4 hisoblangan javob.</p>",
    },
]


# =====================================================================
# PM-49 — chiziqli funksiya y = kx + b
# =====================================================================

Q_PM49 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 3x + 5 da k va b "
                "nechaga teng?</strong></p>",
        "choices": [
            "k = 3, b = 5",
            "k = 5, b = 3",
            "k = 3, b = 3",
            "k = 8, b = 0",
        ],
        "correct": "k = 3, b = 5",
        "explanation": "<p><strong>k = 3, b = 5.</strong> Qolip y = kx + b: x "
                       "oldidagi son — k, yolgʻiz turgan son — b.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 2x + 7 grafigi Oy "
                "oʻqini qaysi nuqtada kesadi?</strong></p>",
        "choices": ["(0; 2)", "(0; 7)", "(2; 0)", "(7; 0)"],
        "correct": "(0; 7)",
        "explanation": "<p><strong>(0; 7).</strong> Oy oʻqini kesish nuqtasini b "
                       "beradi, k emas. <strong>(0; 2)</strong> — k ni b deb "
                       "olgan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = 4x − 1 boʻlsa, x = 2 da y nechaga "
                "teng?</strong></p>",
        "choices": ["4", "7", "8", "9"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 4 × 2 = 8, keyin 8 − 1 = 7. "
                       "<strong>4</strong> — 4 × (2 − 1) deb, qavs qoʻshib "
                       "yuborilgan javob.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>k manfiy boʻlsa, chiziq "
                "qanday joylashadi?</strong></p>",
        "choices": [
            "Oʻngga qarab tushadi",
            "Oʻngga qarab koʻtariladi",
            "Gorizontal boʻladi",
            "Vertikal boʻladi",
        ],
        "correct": "Oʻngga qarab tushadi",
        "explanation": "<p><strong>Oʻngga qarab tushadi.</strong> k — x bir "
                       "birlikka oshganda y ning oʻzgarishi. U manfiy boʻlsa, y "
                       "kamayadi, demak grafik pastga qarab yuradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = x + 6 da k nechaga "
                "teng?</strong></p>",
        "choices": ["0", "1", "6", "7"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> x oldida son koʻrinmasa, u yerda 1 "
                       "turadi: y = 1x + 6. <strong>6</strong> — b ni k deb olgan "
                       "javob.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>y = −3x + 2 boʻlsa, x = 4 da y nechaga "
                "teng?</strong></p>",
        "choices": ["−14", "−10", "10", "14"],
        "correct": "−10",
        "explanation": "<p><strong>−10.</strong> −3 × 4 = −12, keyin "
                       "−12 + 2 = −10. <strong>−14</strong> — qoʻshish oʻrniga "
                       "ayirilgan javob (−12 − 2).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Chiziq Oy oʻqini (0; −5) da "
                "kesadi va k = 2.</p><p><strong>Uning formulasi qaysi?</strong></p>",
        "choices": ["y = 2x − 5", "y = 2x + 5", "y = −5x + 2", "y = 5x − 2"],
        "correct": "y = 2x − 5",
        "explanation": "<p><strong>y = 2x − 5.</strong> k — x oldida, b — yolgʻiz "
                       "son va u ishorasi bilan olinadi: b = −5. "
                       "<strong>y = −5x + 2</strong> — k va b oʻrni almashgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Funksiyaning boshlangʻich "
                "qiymati 3, x bir birlikka oshganda y esa 4 birlikka oshadi.</p>"
                "<p><strong>Formulasi qaysi?</strong></p>",
        "choices": ["y = 3x + 4", "y = 4x + 3", "y = 4x − 3", "y = 7x"],
        "correct": "y = 4x + 3",
        "explanation": "<p><strong>y = 4x + 3.</strong> Qadam — k = 4, "
                       "boshlangʻich qiymat — b = 3. <strong>y = 3x + 4</strong> "
                       "— ikkisi almashtirilgan javob; tekshirish uchun x = 1 "
                       "qoʻying: toʻgʻri javobda 7, notoʻgʻrisida ham 7 chiqadi, "
                       "lekin x = 2 da 11 va 10 — allaqachon har xil.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 5x da b nechaga "
                "teng?</strong></p>",
        "choices": ["0", "1", "5", "Aniqlab boʻlmaydi"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Qoʻshiluvchi koʻrinmasa, u nolga "
                       "teng: y = 5x + 0. Demak grafik koordinata boshidan "
                       "oʻtadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 7 funksiyasining "
                "grafigi qanday?</strong></p>",
        "choices": [
            "Gorizontal chiziq",
            "Vertikal chiziq",
            "Koʻtariluvchi chiziq",
            "Bitta nuqta",
        ],
        "correct": "Gorizontal chiziq",
        "explanation": "<p><strong>Gorizontal chiziq.</strong> Bu yerda "
                       "y = 0x + 7, yaʼni k = 0: x qanday boʻlishidan qatʼi nazar "
                       "y hamisha 7 ga teng. Chiziq Ox oʻqiga parallel boʻlib, "
                       "(0; 7) dan oʻtadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 2x + 6 grafigi Ox "
                "oʻqini qaysi nuqtada kesadi?</strong></p>",
        "choices": ["(−3; 0)", "(0; 6)", "(3; 0)", "(6; 0)"],
        "correct": "(−3; 0)",
        "explanation": "<p><strong>(−3; 0).</strong> Ox oʻqida y = 0, demak "
                       "2x + 6 = 0 → 2x = −6 → x = −3. <strong>(3; 0)</strong> — "
                       "manfiy ishorani tushirib qoldirgan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Taksi oʻtirish uchun 8 000 soʻm, har kilometr "
                "uchun 3 000 soʻm oladi.</p><p><strong>12 km yoʻl qancha "
                "turadi?</strong></p>",
        "choices": ["36 000 soʻm", "44 000 soʻm", "56 000 soʻm", "132 000 soʻm"],
        "correct": "44 000 soʻm",
        "explanation": "<p><strong>44 000 soʻm.</strong> y = 3 000x + 8 000; "
                       "3 000 × 12 + 8 000 = 36 000 + 8 000 = 44 000. "
                       "<strong>36 000</strong> — oʻtirish haqi qoʻshilmagan "
                       "javob.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 2x + 5 va y = 5x + 2 "
                "orasidagi farq nima?</strong></p>",
        "choices": [
            "Birinchisining qadami 2 va boshlanishi 5; ikkinchisida aksincha",
            "Ular bir xil chiziq",
            "Ikkalasining ham qadami 5",
            "Ikkalasi ham (0; 2) dan oʻtadi",
        ],
        "correct": "Birinchisining qadami 2 va boshlanishi 5; ikkinchisida "
                   "aksincha",
        "explanation": "<p><strong>Qadam va boshlanish oʻrni almashgan.</strong> "
                       "x = 1 da ikkalasi ham 7 beradi, shuning uchun ular bir xil "
                       "koʻrinishi mumkin. Lekin x = 2 da 9 va 12 — chiziqlar "
                       "butunlay boshqa.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi chiziq "
                "tikroq?</strong></p>",
        "choices": [
            "y = 3x + 1",
            "y = x + 3",
            "Ikkalasi bir xil",
            "y = x + 3, chunki 3 kattaroq",
        ],
        "correct": "y = 3x + 1",
        "explanation": "<p><strong>y = 3x + 1.</strong> Tiklikni k belgilaydi, b "
                       "emas: birinchisida har qadamda y 3 birlikka, "
                       "ikkinchisida esa 1 birlikka oʻsadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi funksiya chiziqli "
                "EMAS?</strong></p>",
        "choices": [
            "y = x^2 + 1",
            "y = 2x",
            "y = 5 − x",
            "y = 0,5x + 4",
        ],
        "correct": "y = x^2 + 1",
        "explanation": "<p><strong>y = x^2 + 1.</strong> Chiziqli funksiyada x "
                       "faqat birinchi darajada boʻladi (y = kx + b). Daraja "
                       "paydo boʻlishi bilan grafik toʻgʻri chiziq boʻlmay "
                       "qoladi: qiymatlar 2, 5, 10, 17 — qadam oʻzgarib "
                       "boradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = −x + 4 grafigi "
                "haqida nima deyish mumkin?</strong></p>",
        "choices": [
            "(0; 4) dan oʻtadi va oʻngga qarab tushadi",
            "(0; 4) dan oʻtadi va oʻngga qarab koʻtariladi",
            "(0; −1) dan oʻtadi va tushadi",
            "(4; 0) dan oʻtadi va gorizontal boʻladi",
        ],
        "correct": "(0; 4) dan oʻtadi va oʻngga qarab tushadi",
        "explanation": "<p><strong>(0; 4) dan oʻtadi va tushadi.</strong> b = 4 — "
                       "boshlanish nuqtasi; k = −1 — manfiy, demak har qadamda y "
                       "bir birlikka kamayadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Sherbek y = 4x − 6 funksiyasida "
                "b = 6 deb yozdi.</p><p><strong>Toʻgʻri javob qaysi?</strong></p>",
        "choices": [
            "b = −6, chunki qolip y = kx + b",
            "b = 6 — Sherbek haq",
            "b = 4, chunki x oldidagi son olinadi",
            "b = −4",
        ],
        "correct": "b = −6, chunki qolip y = kx + b",
        "explanation": "<p><strong>b = −6.</strong> Qolipda qoʻshuv turibdi, demak "
                       "ayirish koʻrsangiz minusni b ning oʻziga qoʻshib olasiz: "
                       "4x + (−6). Tekshirish: x = 0 da y = −6, yaʼni chiziq "
                       "(0; −6) dan oʻtadi.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Dilnoza y = 2x + 3 grafigini chizishda "
                "(0; 2) nuqtadan boshladi.</p><p><strong>Toʻgʻri javob "
                "qaysi?</strong></p>",
        "choices": [
            "(0; 3) dan boshlanadi, chunki b = 3",
            "(0; 2) dan boshlanadi — Dilnoza haq",
            "(2; 0) dan boshlanadi",
            "(3; 0) dan boshlanadi",
        ],
        "correct": "(0; 3) dan boshlanadi, chunki b = 3",
        "explanation": "<p><strong>(0; 3).</strong> Oy oʻqini kesish nuqtasini b "
                       "beradi. Dilnoza k ni (yaʼni qiyalikni) boshlanish deb "
                       "olgan. Tekshirish: x = 0 da y = 2 × 0 + 3 = 3.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Taksi oʻtirish uchun 8 000 soʻm, har kilometr uchun 3 000 soʻm "
                "oladi. Bekzod jami 29 000 soʻm toʻladi.</p><p><strong>U necha "
                "kilometr yurgan?</strong></p>",
        "choices": ["5 km", "7 km", "9 km", "12 km"],
        "correct": "7 km",
        "explanation": "<p><strong>7 km.</strong> 3 000x + 8 000 = 29 000 → "
                       "3 000x = 21 000 → x = 7. Tekshirish: "
                       "21 000 + 8 000 = 29 000 ✓ <strong>9 km</strong> — oʻtirish "
                       "haqini ayirmay, 29 000 ni 3 000 ga boʻlishga urinilgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Sport zali obunasi oyiga 90 000 soʻm, ustiga har bir mashgʻulot "
                "uchun 6 000 soʻm.</p><p><strong>15 marta borgan Afsona qancha "
                "toʻlaydi?</strong></p>",
        "choices": ["90 000 soʻm", "96 000 soʻm", "180 000 soʻm", "1 440 000 soʻm"],
        "correct": "180 000 soʻm",
        "explanation": "<p><strong>180 000 soʻm.</strong> y = 6 000x + 90 000; "
                       "6 000 × 15 = 90 000, ustiga obuna 90 000: jami 180 000. "
                       "<strong>90 000</strong> — obunani qoʻshishni unutgan "
                       "javob; <strong>1 440 000</strong> — obuna bilan "
                       "mashgʻulot narxini qoʻshib, keyin hammasini 15 ga "
                       "koʻpaytirgan javob.</p>",
    },
]


# =====================================================================
# PM-50 — k va b ning maʼnosi
# =====================================================================

Q_PM50 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>y = 2 000x + 5 000 formulasida "
                "x — ishlangan soatlar soni.</p><p><strong>5 000 nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Ish boshlanmasdan turib ham toʻlanadigan oʻzgarmas haq",
            "Bir soatlik ish haqi",
            "Besh soatlik ish haqi",
            "Jami ish haqi",
        ],
        "correct": "Ish boshlanmasdan turib ham toʻlanadigan oʻzgarmas haq",
        "explanation": "<p><strong>Oʻzgarmas haq.</strong> b — x = 0 dagi qiymat: "
                       "hech narsa qilinmaganda ham qoladigan miqdor. Bir soatlik "
                       "haq esa k = 2 000.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Xuddi shu formulada "
                "2 000 nimani bildiradi?</strong></p>",
        "choices": [
            "Har bir soat uchun qoʻshiladigan pul",
            "Boshlangʻich haq",
            "Ikki ming soatlik ish",
            "Jami toʻlov",
        ],
        "correct": "Har bir soat uchun qoʻshiladigan pul",
        "explanation": "<p><strong>Har bir soat uchun qoʻshiladigan pul.</strong> "
                       "k — x bir birlikka oshganda y ning oʻzgarishi. Grafikda "
                       "bu chiziqning qiyaligi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>k manfiy boʻlsa, real "
                "vaziyatda nima roʻy beradi?</strong></p>",
        "choices": [
            "Miqdor vaqt oʻtishi bilan kamayadi",
            "Miqdor vaqt oʻtishi bilan oʻsadi",
            "Miqdor oʻzgarmaydi",
            "Miqdor manfiy boʻlib qoladi",
        ],
        "correct": "Miqdor vaqt oʻtishi bilan kamayadi",
        "explanation": "<p><strong>Kamayadi.</strong> Masalan bakdan suv "
                       "sarflanishi, shamning yonishi, qarzning toʻlanishi. "
                       "Grafik oʻngga qarab tushadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 200 − 25x da b "
                "nechaga teng?</strong></p>",
        "choices": ["−25", "25", "175", "200"],
        "correct": "200",
        "explanation": "<p><strong>200.</strong> b — x = 0 dagi qiymat, yaʼni "
                       "boshidagi miqdor. <strong>25</strong> va "
                       "<strong>−25</strong> — bu k, har soatdagi oʻzgarish.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 200 − 25x formulasi "
                "boʻyicha har soatda nima roʻy beradi?</strong></p>",
        "choices": [
            "25 birlik kamayadi",
            "25 birlik oʻsadi",
            "200 birlik kamayadi",
            "Hech narsa oʻzgarmaydi",
        ],
        "correct": "25 birlik kamayadi",
        "explanation": "<p><strong>25 birlik kamayadi.</strong> k = −25: minus "
                       "kamayishni, 25 esa qancha kamayishini bildiradi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p>Bakda 200 litr suv bor, har soatda 25 litr "
                "sarflanadi.</p><p><strong>6 soatdan keyin qancha suv "
                "qoladi?</strong></p>",
        "choices": ["25 litr", "50 litr", "75 litr", "150 litr"],
        "correct": "50 litr",
        "explanation": "<p><strong>50 litr.</strong> y = 200 − 25x; "
                       "200 − 25 × 6 = 200 − 150 = 50. <strong>150 litr</strong> "
                       "— sarflangan miqdor, qolgani emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Bakda 200 litr suv bor, har soatda 25 litr "
                "sarflanadi.</p><p><strong>Bak necha soatda boʻshaydi?</strong></p>",
        "choices": ["6 soat", "8 soat", "10 soat", "25 soat"],
        "correct": "8 soat",
        "explanation": "<p><strong>8 soat.</strong> 200 − 25x = 0 → 25x = 200 → "
                       "x = 8. Tekshirish: 200 − 25 × 8 = 0 ✓ Grafik (8; 0) da Ox "
                       "oʻqiga tegadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki chiziqning k si bir "
                "xil, b si har xil boʻlsa, ular qanday joylashadi?</strong></p>",
        "choices": [
            "Parallel — hech qachon kesishmaydi",
            "Bitta nuqtada kesishadi",
            "Ustma-ust tushadi",
            "Perpendikulyar boʻladi",
        ],
        "correct": "Parallel — hech qachon kesishmaydi",
        "explanation": "<p><strong>Parallel.</strong> Bir xil k — bir xil tiklik "
                       "degani, demak chiziqlar bir xil yoʻnalishda yuradi va "
                       "orasidagi masofa oʻzgarmaydi. Har xil b esa biri "
                       "ikkinchisidan doim yuqorida turishini bildiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki chiziqning b si bir "
                "xil, k si har xil boʻlsa, ular haqida nima deyish "
                "mumkin?</strong></p>",
        "choices": [
            "Ikkalasi ham (0; b) nuqtadan oʻtadi",
            "Ular parallel boʻladi",
            "Ular hech qachon uchrashmaydi",
            "Ikkalasi ham gorizontal boʻladi",
        ],
        "correct": "Ikkalasi ham (0; b) nuqtadan oʻtadi",
        "explanation": "<p><strong>Ikkalasi ham (0; b) dan oʻtadi.</strong> "
                       "Boshlanish nuqtasi bir xil, keyin esa har biri oʻz "
                       "qiyaligi bilan ajralib ketadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>A tarif: abonent haqi 20 000 soʻm, daqiqasi "
                "200 soʻm.</p><p><strong>250 daqiqa gaplashish qancha "
                "turadi?</strong></p>",
        "choices": ["20 000 soʻm", "50 000 soʻm", "70 000 soʻm", "220 000 soʻm"],
        "correct": "70 000 soʻm",
        "explanation": "<p><strong>70 000 soʻm.</strong> y = 200x + 20 000; "
                       "200 × 250 = 50 000, ustiga abonent haqi 20 000: jami "
                       "70 000. <strong>50 000</strong> — abonent haqi "
                       "qoʻshilmagan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>B tarif: abonent haqi 50 000 soʻm, daqiqasi "
                "100 soʻm.</p><p><strong>250 daqiqa gaplashish qancha "
                "turadi?</strong></p>",
        "choices": ["25 000 soʻm", "50 000 soʻm", "75 000 soʻm", "150 000 soʻm"],
        "correct": "75 000 soʻm",
        "explanation": "<p><strong>75 000 soʻm.</strong> y = 100x + 50 000; "
                       "100 × 250 = 25 000, ustiga 50 000: jami 75 000. Demak "
                       "250 daqiqada A tarif (70 000) arzonroq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>A tarif: 200x + 20 000. "
                "B tarif: 100x + 50 000.</p><p><strong>400 daqiqada qaysi tarif "
                "arzon?</strong></p>",
        "choices": [
            "A tarif, 10 000 soʻmga arzon",
            "B tarif, 10 000 soʻmga arzon",
            "B tarif, 30 000 soʻmga arzon",
            "Ikkalasi ham teng",
        ],
        "correct": "B tarif, 10 000 soʻmga arzon",
        "explanation": "<p><strong>B tarif, 10 000 soʻmga arzon.</strong> "
                       "A: 200 × 400 + 20 000 = 100 000. "
                       "B: 100 × 400 + 50 000 = 90 000. Farq: 10 000 soʻm. Koʻp "
                       "gaplashadiganga kichik k li tarif foydali.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 100x + 3 000 va "
                "y = 3 000x + 100 dan qaysi biri tezroq oʻsadi?</strong></p>",
        "choices": [
            "y = 3 000x + 100",
            "y = 100x + 3 000",
            "Ikkalasi bir xil tezlikda",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "y = 3 000x + 100",
        "explanation": "<p><strong>y = 3 000x + 100.</strong> Oʻsish tezligini k "
                       "belgilaydi: har qadamda 3 000 va 100. Boshlanishi past "
                       "boʻlsa ham, u tez orada ikkinchisidan oʻzib ketadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Grafik oʻngga qarab "
                "pastga tushmoqda. Nima deyish mumkin?</strong></p>",
        "choices": [
            "k manfiy",
            "k musbat",
            "k nolga teng",
            "b manfiy",
        ],
        "correct": "k manfiy",
        "explanation": "<p><strong>k manfiy.</strong> Tushish yoki koʻtarilishni "
                       "faqat k belgilaydi. b esa chiziqning qayerdan "
                       "boshlanishini koʻrsatadi va u musbat ham boʻlishi "
                       "mumkin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Karim aka: kelish haqi 50 000, "
                "soatiga 20 000. Anvar aka: kelish haqi 20 000, soatiga 50 000.</p>"
                "<p><strong>1 soatlik ish uchun kim arzon?</strong></p>",
        "choices": [
            "Ikkalasi ham teng — 70 000 soʻmdan",
            "Karim aka arzon",
            "Anvar aka arzon",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Ikkalasi ham teng — 70 000 soʻmdan",
        "explanation": "<p><strong>Teng.</strong> Karim aka: "
                       "50 000 + 20 000 = 70 000. Anvar aka: "
                       "20 000 + 50 000 = 70 000. Lekin 3 soatda Karim aka "
                       "110 000, Anvar aka esa 170 000 oladi — uzoq ishga kichik "
                       "k li usta afzal.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>b = 0 boʻlsa, bu real "
                "vaziyatda nimani bildiradi?</strong></p>",
        "choices": [
            "Boshlangʻich haq yoʻq — grafik koordinata boshidan oʻtadi",
            "Xizmat butunlay bepul",
            "Grafik gorizontal boʻladi",
            "Miqdor kamayadi",
        ],
        "correct": "Boshlangʻich haq yoʻq — grafik koordinata boshidan oʻtadi",
        "explanation": "<p><strong>Boshlangʻich haq yoʻq.</strong> Masalan "
                       "oʻtirish haqisiz taksi yoki noldan boshlangan harakat. "
                       "Xizmat bepul degani emas — har bir birlik uchun k "
                       "toʻlanadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Bekzod y = 200 − 25x formulasida "
                "k = 25 dedi.</p><p><strong>Toʻgʻri javob qaysi?</strong></p>",
        "choices": [
            "k = −25, chunki miqdor kamayadi",
            "k = 25 — Bekzod haq",
            "k = 200",
            "k = 175",
        ],
        "correct": "k = −25, chunki miqdor kamayadi",
        "explanation": "<p><strong>k = −25.</strong> Qolip y = kx + b, demak "
                       "formulani y = −25x + 200 koʻrinishida yozib olish kerak. "
                       "Minus «kamayadi» degan maʼnoni oʻz ichiga oladi — usiz "
                       "grafik teskari tomonga, yuqoriga ketardi.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Afsona: «k kattaroq boʻlgan tarif "
                "hamma vaqt qimmatroq».</p><p><strong>Toʻgʻri javob "
                "qaysi?</strong></p>",
        "choices": [
            "Notoʻgʻri: kichik x larda past b li tarif arzonroq boʻlishi mumkin",
            "Toʻgʻri: k qancha katta boʻlsa, narx shuncha yuqori",
            "Notoʻgʻri: k narxga umuman taʼsir qilmaydi",
            "Toʻgʻri, lekin faqat b = 0 boʻlganda",
        ],
        "correct": "Notoʻgʻri: kichik x larda past b li tarif arzonroq boʻlishi "
                   "mumkin",
        "explanation": "<p><strong>Notoʻgʻri.</strong> 100 daqiqada A tarif "
                       "(k = 200) 40 000, B tarif (k = 100) esa 60 000 soʻm. "
                       "k tiklikni, b esa boshlanishni belgilaydi — kim arzon "
                       "ekani qaysi x da qaraganingizga bogʻliq.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Sherbek doʻkonda ishlaydi: oyiga 1 200 000 soʻm doimiy maosh "
                "va har bir sotilgan mahsulot uchun 15 000 soʻm mukofot.</p>"
                "<p><strong>2 100 000 soʻm olish uchun nechta mahsulot sotishi "
                "kerak?</strong></p>",
        "choices": ["40 ta", "60 ta", "80 ta", "140 ta"],
        "correct": "60 ta",
        "explanation": "<p><strong>60 ta.</strong> 15 000x + 1 200 000 = "
                       "2 100 000 → 15 000x = 900 000 → x = 60. Tekshirish: "
                       "900 000 + 1 200 000 = 2 100 000 ✓ <strong>140 ta</strong> "
                       "— doimiy maoshni ayirmay, 2 100 000 ni 15 000 ga "
                       "boʻlishga urinilgan javob.</p>",
    },
    {
        "text": "<p>Shamning uzunligi boshida 20 sm edi va u har soatda 4 sm dan "
                "qisqaradi.</p><p><strong>Shamning formulasi va butunlay yonib "
                "bitish vaqti qaysi javobda toʻgʻri?</strong></p>",
        "choices": [
            "y = 20 − 4x, 4 soat",
            "y = 20 − 4x, 5 soat",
            "y = 4x + 20, 5 soat",
            "y = 4x − 20, 4 soat",
        ],
        "correct": "y = 20 − 4x, 5 soat",
        "explanation": "<p><strong>y = 20 − 4x, 5 soat.</strong> b = 20 — "
                       "boshidagi uzunlik, k = −4 — qisqarish. Yonib bitishi: "
                       "20 − 4x = 0 → x = 5. <strong>y = 4x + 20</strong> — "
                       "kamayish oʻrniga oʻsish yozilgan javob: unda sham uzayib "
                       "borardi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-48 Mashq: Jadvaldan grafikka",
        "description": "20 savol — qiymatlar jadvali, nuqtalarni qoʻyish, "
                       "grafikdan oʻqish va diskret maʼlumot.",
        "tutorial":    "PM-48:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM48,
    },
    {
        "title":       "PM-49 Mashq: Chiziqli funksiya y = kx + b",
        "description": "20 savol — k va b ni ajratish, oʻqlarni kesish nuqtalari "
                       "va chiziqning yoʻnalishi.",
        "tutorial":    "PM-49:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM49,
    },
    {
        "title":       "PM-50 Mashq: k va b ning maʼnosi",
        "description": "20 savol — k va b ni real vaziyatga tarjima qilish, "
                       "kamayuvchi jarayonlar va ikki tarifni taqqoslash.",
        "tutorial":    "PM-50:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM50,
    },
]
