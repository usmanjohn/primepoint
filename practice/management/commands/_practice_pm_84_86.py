# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-84, PM-85, PM-86 (ehtimollik hisobi;
masalani oʻqishning toʻrt qadami; nomaʼlumni tanlash va jadval).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: uchalasi ham `hard`.

⚠️ `choices` EKRANLANADI — HTML teg yoʻq.
⚠️ Kumulyativ:
   • PM-84 — sanab hisoblash (PM-82), teskari hodisa 1 − P, nisbiy
     chastota. ⛔ Shartli ehtimollik YOʻQ;
   • PM-85 — toʻrt qadam. Yangi formula yoʻq: hamma savol matnni
     ifodaga aylantirish va soʻralganni ushlab qolish haqida.
     ⛔ Chizma usuli (PM-87) va ortiqcha maʼlumot (PM-94) YOʻQ;
   • PM-86 — nomaʼlumni tanlash va jadval. ⛔ Harakat/ish/aralashma
     masalalari (PM-88…91) YOʻQ.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_84_86.py --master=prime \\
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
# PM-84 — ehtimollikni hisoblash va tajriba bilan tekshirish
# =====================================================================

Q_PM84 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikkita zar "
                "tashlanganda jami nechta hol boʻladi?</strong></p>",
        "choices": ["6", "12", "30", "36"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> Koʻpaytirish prinsipiga "
                       "koʻra (PM-82) birinchi zarning 6 ta natijasi "
                       "ikkinchisining 6 ta natijasi bilan qoʻshiladi: "
                       "6 × 6 = 36. <strong>12</strong> — 6 + 6 qilib "
                       "qoʻshilganda chiqadi; sanashda bosqichlar "
                       "koʻpaytiriladi, qoʻshilmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Bir hodisaning ehtimolligi 0,4.</p>"
                "<p><strong>Uning roʻy bermaslik ehtimolligi "
                "qancha?</strong></p>",
        "choices": ["0,4", "0,6", "1,4", "2,5"],
        "correct": "0,6",
        "explanation": "<p><strong>0,6.</strong> Teskari hodisa qoidasi: "
                       "1 − 0,4 = 0,6. <strong>2,5</strong> — 1 ÷ 0,4 "
                       "qilinganda chiqadi; teskari hodisada ayiriladi, "
                       "boʻlinmaydi. <strong>1,4</strong> — qoʻshib "
                       "yuborilgan, lekin ehtimollik 1 dan katta "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Zar tashlandi. 3 dan katta son "
                "tushish ehtimolligi qancha?</strong></p>",
        "choices": ["0,17", "0,33", "0,5", "0,67"],
        "correct": "0,5",
        "explanation": "<p><strong>0,5.</strong> Uchdan katta sonlar — 4, 5 "
                       "va 6, ya'ni 3 ta qulay hol: 3 ÷ 6 = 0,5. "
                       "<strong>0,67</strong> — «3 dan kichik boʻlmagan» "
                       "deb oʻqilganda (3, 4, 5, 6 → 4 ÷ 6) chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Tanga 100 marta tashlandi va gerb "
                "58 marta tushdi.</p><p><strong>Nisbiy chastota "
                "qancha?</strong></p>",
        "choices": ["0,42", "0,50", "0,58", "1,72"],
        "correct": "0,58",
        "explanation": "<p><strong>0,58.</strong> Nisbiy chastota = roʻy "
                       "bergan marta ÷ jami tajriba = 58 ÷ 100 = 0,58. "
                       "<strong>0,50</strong> — nazariy ehtimollik, "
                       "tajriba natijasi emas. <strong>0,42</strong> — "
                       "raqam tomonining chastotasi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son "
                "ehtimollik boʻla olmaydi?</strong></p>",
        "choices": ["0", "0,45", "1", "1,2"],
        "correct": "1,2",
        "explanation": "<p><strong>1,2.</strong> Ehtimollik har doim 0 bilan "
                       "1 orasida boʻladi, chunki qulay hollar jami "
                       "hollardan koʻp boʻlishi mumkin emas. "
                       "<strong>0</strong> — imkonsiz hodisa, "
                       "<strong>1</strong> — aniq hodisa; ikkalasi ham "
                       "haqiqiy ehtimollik.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>Ikkita zar tashlandi. "
                "Yigʻindisi 4 boʻladigan nechta hol bor?</strong></p>",
        "choices": ["2", "3", "4", "6"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Bular (1; 3), (2; 2) va "
                       "(3; 1). <strong>2</strong> — (2; 2) bitta marta "
                       "sanalgan, lekin (1; 3) va (3; 1) har xil hol "
                       "deb hisoblanmagan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Ikkita zar tashlandi. "
                "Yigʻindisi 10 boʻlish ehtimolligi qancha?</strong></p>",
        "choices": ["0,06", "0,08", "0,11", "0,17"],
        "correct": "0,08",
        "explanation": "<p><strong>0,08.</strong> Qulay hollar: (4; 6), "
                       "(5; 5), (6; 4) — 3 ta. Demak 3 ÷ 36 = 0,083 ≈ "
                       "0,08. <strong>0,17</strong> — 6 ÷ 36, ya'ni "
                       "yigʻindisi 7 boʻlgan hol.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Ikkita zar tashlandi. Kamida "
                "bitta 5 tushish ehtimolligi qancha?</strong></p>",
        "choices": ["0,17", "0,28", "0,31", "0,33"],
        "correct": "0,31",
        "explanation": "<p><strong>0,31.</strong> «Kamida bitta» — teskari "
                       "hodisadan yuriladi. 5 siz hollar: 5 × 5 = 25, "
                       "demak 1 − 25 ÷ 36 = 11 ÷ 36 ≈ 0,31. "
                       "<strong>0,33</strong> — ikkita <sup>1</sup>/"
                       "<sub>6</sub> qoʻshilganda chiqadi; bunda ikkala "
                       "zarda ham 5 tushgan hol ikki marta "
                       "sanaladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Ikkita tanga tashlandi. "
                "Ikkalasida ham gerb tushish ehtimolligi qancha?</strong>"
                "</p>",
        "choices": ["0,25", "0,33", "0,5", "0,75"],
        "correct": "0,25",
        "explanation": "<p><strong>0,25.</strong> Jami hollar 2 × 2 = 4: "
                       "GG, GR, RG, RR. Qulay hol bitta — GG. Demak "
                       "1 ÷ 4 = 0,25. <strong>0,33</strong> — hollar "
                       "«ikki gerb, bir gerb, gerbsiz» deb 3 ta deb "
                       "olinganda chiqadi, lekin ular teng imkoniyatli "
                       "emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Qopchada 6 ta qizil, 9 ta koʻk va 5 ta "
                "yashil shar bor. Bitta shar olindi.</p><p><strong>Qizil "
                "chiqmaslik ehtimolligi qancha?</strong></p>",
        "choices": ["0,3", "0,45", "0,7", "0,75"],
        "correct": "0,7",
        "explanation": "<p><strong>0,7.</strong> Jami sharlar 6 + 9 + 5 = "
                       "20. P(qizil) = 6 ÷ 20 = 0,3, demak teskari "
                       "hodisa 1 − 0,3 = 0,7. Toʻgʻridan-toʻgʻri ham "
                       "boʻladi: (9 + 5) ÷ 20 = 0,7. <strong>0,3</strong> "
                       "— qizil chiqish ehtimolligi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Knopka 400 marta tashlandi va 152 marta "
                "uchi bilan yuqoriga tushdi.</p><p><strong>Nisbiy chastota "
                "necha foiz?</strong></p>",
        "choices": ["26%", "38%", "62%", "152%"],
        "correct": "38%",
        "explanation": "<p><strong>38%.</strong> 152 ÷ 400 = 0,38 = 38%. "
                       "<strong>62%</strong> — teskari holning "
                       "chastotasi. Knopkani sanab hisoblab boʻlmaydi — "
                       "uning yoqlari teng emas, shuning uchun faqat "
                       "tajriba yordam beradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Bir hodisaning ehtimolligi 25% ga "
                "teng.</p><p><strong>200 ta sinovda u taxminan necha marta "
                "roʻy beradi?</strong></p>",
        "choices": ["25", "50", "75", "175"],
        "correct": "50",
        "explanation": "<p><strong>50.</strong> 200 × 0,25 = 50 marta. "
                       "<strong>25</strong> — foiz sonining oʻzi javob "
                       "deb olingan. <strong>150</strong> emas, "
                       "<strong>175</strong> ham emas: 175 — "
                       "200 − 25 dan chiqadi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi holda "
                "ehtimollikni sanab hisoblab boʻlmaydi va faqat tajriba "
                "yordam beradi?</strong></p>",
        "choices": [
            "Zar tashlash",
            "Tanga tashlash",
            "Qopchadan shar olish",
            "Knopka tashlash",
        ],
        "correct": "Knopka tashlash",
        "explanation": "<p><strong>Knopka tashlash.</strong> P = qulay ÷ "
                       "jami formulasi natijalar <strong>teng "
                       "imkoniyatli</strong> boʻlgandagina ishlaydi. "
                       "Zarning oltita yogʻi, tanganing ikki tomoni va "
                       "qopchadagi sharlar teng huquqli; knopkaning "
                       "yoqlari esa teng emas, shuning uchun uni faqat "
                       "koʻp marta tashlab oʻlchash mumkin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki zarning yigʻindisi "
                "2 dan 12 gacha — oʻn bir xil son.</p><p><strong>Nega "
                "P(yigʻindi 7) <sup>1</sup>/<sub>11</sub> ga teng "
                "emas?</strong></p>",
        "choices": [
            "Chunki yigʻindilar teng imkoniyatli emas",
            "Chunki 7 toq son",
            "Chunki zarlar bir xil rangda emas",
            "Chunki 11 tub son",
        ],
        "correct": "Chunki yigʻindilar teng imkoniyatli emas",
        "explanation": "<p><strong>Chunki yigʻindilar teng imkoniyatli "
                       "emas.</strong> Yigʻindi 2 faqat bitta yoʻl bilan "
                       "chiqadi — (1; 1). Yigʻindi 7 esa oltita yoʻl "
                       "bilan. Maxrajda teng imkoniyatli hollar turishi "
                       "kerak, ular esa 36 ta juftlik: P(7) = 6 ÷ 36 = "
                       "<sup>1</sup>/<sub>6</sub>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Tanga ketma-ket 6 marta "
                "gerb tomoni bilan tushdi.</p><p><strong>Yettinchi "
                "tashlashda raqam tushish ehtimolligi qancha?</strong></p>",
        "choices": ["0,5", "0,6", "0,86", "1"],
        "correct": "0,5",
        "explanation": "<p><strong>0,5.</strong> Tangada xotira yoʻq: "
                       "oldingi natijalar keyingisiga umuman taʼsir "
                       "qilmaydi. <strong>0,86</strong> va "
                       "<strong>1</strong> — tanga «qarzini qaytaradi» "
                       "degan notoʻgʻri fikrdan chiqadi. Chastota 0,5 ga "
                       "yaqinlashishi kelgusi natijalar tuzatgani uchun "
                       "emas, tashlashlar soni koʻpayib eski oltitasining "
                       "ulushi kichrayib ketgani uchun.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bir tajribada 20 ta "
                "tashlashda chastota 0,65, boshqasida 500 ta tashlashda "
                "0,508 chiqdi.</p><p><strong>Qaysi biri ehtimollikka "
                "yaqinroq baho beradi?</strong></p>",
        "choices": [
            "20 talik tajriba, chunki soni kichik",
            "500 talik tajriba, chunki soni katta",
            "Ikkalasi bir xil ishonchli",
            "Hech qaysisi — tajriba baho bermaydi",
        ],
        "correct": "500 talik tajriba, chunki soni katta",
        "explanation": "<p><strong>500 talik tajriba.</strong> Tajriba soni "
                       "ortgani sari nisbiy chastota ehtimollikka "
                       "yaqinlashadi. 20 ta tashlashda 0,65 chiqishi "
                       "butunlay tabiiy va u hech narsani isbotlamaydi; "
                       "500 ta tashlashda esa 0,5 dan uzoqlashish "
                       "deyarli imkonsiz.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Ikkita zar "
                "tashlandi. Kamida bitta 6 tushish ehtimolligini "
                "toping.</strong></p>",
        "choices": [
            "6 ÷ 36 = 0,17",
            "11 ÷ 36 ≈ 0,31",
            "12 ÷ 36 ≈ 0,33",
            "25 ÷ 36 ≈ 0,69",
        ],
        "correct": "11 ÷ 36 ≈ 0,31",
        "explanation": "<p><strong>11 ÷ 36 ≈ 0,31.</strong> Teskari hodisa: "
                       "6 siz hollar 5 × 5 = 25 ta, demak kamida bitta "
                       "6 bor hollar 36 − 25 = 11 ta. "
                       "<strong>12 ÷ 36</strong> — ikkita "
                       "<sup>1</sup>/<sub>6</sub> qoʻshilgan va (6; 6) "
                       "ikki marta sanalgan. <strong>25 ÷ 36</strong> — "
                       "teskari hodisaning oʻzi, undan 1 ayirilmagan.</p>",
    },
    {
        "text": "<p>Qayerda xato qilingan?</p><p>Lotereyada yutish "
                "ehtimolligi 0,2. Oʻquvchi yozdi: «P(yutmaslik) = "
                "1 ÷ 0,2 = 5».</p><p><strong>Xato qaysi qatorda?</strong>"
                "</p>",
        "choices": [
            "Boshlangʻich 0,2 notoʻgʻri olingan",
            "Teskari hodisada boʻlish oʻrniga ayirish kerak edi",
            "Javobni foizga oʻgirish unutilgan",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Teskari hodisada boʻlish oʻrniga ayirish kerak edi",
        "explanation": "<p><strong>Teskari hodisada boʻlish oʻrniga ayirish "
                       "kerak edi.</strong> Toʻgʻrisi: 1 − 0,2 = 0,8, "
                       "ya'ni 80%. Javob 5 chiqqani xatoni darrov "
                       "koʻrsatib turibdi — ehtimollik hech qachon 1 dan "
                       "katta boʻlmaydi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Bayram lotereyasida 500 ta bilet "
                "sotildi, ulardan 25 tasi yutuqli. Sherbek bitta bilet "
                "oldi.</p><p><strong>Uning hech narsa yutmaslik ehtimolligi "
                "necha foiz?</strong></p>",
        "choices": ["5%", "20%", "95%", "475%"],
        "correct": "95%",
        "explanation": "<p><strong>95%.</strong> P(yutish) = 25 ÷ 500 = "
                       "0,05 = 5%. Teskari hodisa qoidasi bilan "
                       "P(yutmaslik) = 1 − 0,05 = 0,95 = 95%. "
                       "<strong>5%</strong> — yutish ehtimolligi, "
                       "<strong>475%</strong> esa yutuqsiz biletlar "
                       "sonini (475 ta) foiz deb oʻqiganda chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Dilnoza qutidan 120 marta shar "
                "olib, rangini yozdi va qaytarib soldi. Sariq shar 90 marta "
                "chiqdi. Qutida jami 8 ta shar bor.</p><p><strong>Taxminan "
                "nechtasi sariq?</strong></p>",
        "choices": ["2 ta", "4 ta", "6 ta", "7 ta"],
        "correct": "6 ta",
        "explanation": "<p><strong>6 ta.</strong> Nisbiy chastota = 90 ÷ "
                       "120 = 0,75. Demak P(sariq) ≈ 0,75 va sariq "
                       "sharlar 8 × 0,75 = 6 ta. Tekshirish: 6 ÷ 8 = "
                       "0,75 ✓ <strong>2 ta</strong> — sariq "
                       "boʻlmaganlar soni. Javobda «taxminan» deyiladi, "
                       "chunki tajriba aniq emas, baho beradi.</p>",
    },
]


# =====================================================================
# PM-85 — masalani oʻqishning toʻrt qadami
# =====================================================================

Q_PM85 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>Jasur x ta kitob "
                "oʻqidi. Sherbek Jasurdan 8 ta koʻp oʻqidi.</p>"
                "<p><strong>Sherbek ___ ta kitob oʻqidi.</strong></p>",
        "choices": ["8x", "x + 8", "x − 8", "x ÷ 8"],
        "correct": "x + 8",
        "explanation": "<p><strong>x + 8.</strong> «8 ta koʻp» — ayirma, "
                       "demak qoʻshiladi. <strong>8x</strong> — «8 marta "
                       "koʻp» deb oʻqilganda chiqadi; «ta» va «marta» "
                       "butun masalani oʻzgartiradi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>Jasur x ta kitob "
                "oʻqidi. Sherbek Jasurdan 8 marta koʻp oʻqidi.</p>"
                "<p><strong>Sherbek ___ ta kitob oʻqidi.</strong></p>",
        "choices": ["x − 8", "x + 8", "8x", "x ÷ 8"],
        "correct": "8x",
        "explanation": "<p><strong>8x.</strong> «marta» soʻzi nisbatni "
                       "bildiradi — koʻpaytiriladi. Oldingi savol bilan "
                       "solishtiring: bitta soʻz «x + 8» ni «8x» ga "
                       "aylantirdi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>x sonining "
                "yarmi — bu ___</strong></p>",
        "choices": ["2x", "x ÷ 2", "x − 2", "x + 2"],
        "correct": "x ÷ 2",
        "explanation": "<p><strong>x ÷ 2.</strong> «Yarmi» — ikkiga boʻlish. "
                       "<strong>2x</strong> — «ikki marta koʻp» degani, "
                       "ya'ni teskarisi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Masalani "
                "yechishning toʻrt qadami qanday tartibda "
                "boradi?</strong></p>",
        "choices": [
            "Oʻqi → reja tuz → yech → tekshir",
            "Yech → oʻqi → tekshir → reja tuz",
            "Reja tuz → oʻqi → yech → tekshir",
            "Oʻqi → yech → reja tuz → tekshir",
        ],
        "correct": "Oʻqi → reja tuz → yech → tekshir",
        "explanation": "<p><strong>Oʻqi → reja tuz → yech → tekshir.</strong> "
                       "Birinchi qadam eng uzun boʻlishi kerak: berilgan "
                       "va soʻralgan ajratiladi. Uchinchi qadam eng "
                       "qisqasi — birinchi ikkitasi bajarilgan boʻlsa, "
                       "faqat texnika qoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>«Sinfda kamida 15 ta "
                "oʻquvchi bor».</p><p><strong>Bu shart ___ koʻrinishida "
                "yoziladi.</strong></p>",
        "choices": ["x < 15", "x ≤ 15", "x ≥ 15", "x > 15"],
        "correct": "x ≥ 15",
        "explanation": "<p><strong>x ≥ 15.</strong> «Kamida 15» degani 15 "
                       "ham boʻlishi mumkin, undan koʻp ham. "
                       "<strong>x &gt; 15</strong> 15 ni chiqarib "
                       "tashlaydi — bu «15 dan koʻp» degani.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Ikki sonning yigʻindisi 48 ga "
                "teng. Biri ikkinchisidan 6 taga katta.</p><p><strong>Kichik "
                "son qanday?</strong></p>",
        "choices": ["18", "21", "24", "27"],
        "correct": "21",
        "explanation": "<p><strong>21.</strong> x — kichik son, kattasi "
                       "x + 6. x + (x + 6) = 48 → 2x = 42 → x = 21. "
                       "Kattasi 27. Tekshirish: 21 + 27 = 48 ✓ va "
                       "27 − 21 = 6 ✓ <strong>24</strong> — 48 ni teng "
                       "ikkiga boʻlganda chiqadi va 6 talik farqni "
                       "yoʻqotadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir son va uning uchdan bir "
                "qismi yigʻindisi 64 ga teng.</p><p><strong>Bu son "
                "qanday?</strong></p>",
        "choices": ["16", "48", "64", "80"],
        "correct": "48",
        "explanation": "<p><strong>48.</strong> x + x ÷ 3 = 64. Chap tomon "
                       "sonning <sup>4</sup>/<sub>3</sub> qismi, demak "
                       "x = 64 × 3 ÷ 4 = 48. Tekshirish: 48 + 16 = 64 ✓ "
                       "<strong>16</strong> — sonning uchdan bir qismi, "
                       "sonning oʻzi emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Afsona 36 000 soʻmga ruchka "
                "oldi. Bu uning pulining toʻrtdan bir qismi edi.</p>"
                "<p><strong>Afsonada qancha pul bor edi?</strong></p>",
        "choices": ["9 000 soʻm", "40 000 soʻm", "144 000 soʻm",
                    "180 000 soʻm"],
        "correct": "144 000 soʻm",
        "explanation": "<p><strong>144 000 soʻm.</strong> x ÷ 4 = 36 000 → "
                       "x = 36 000 × 4 = 144 000. Tekshirish: "
                       "144 000 ÷ 4 = 36 000 ✓ <strong>9 000</strong> — "
                       "koʻpaytirish oʻrniga boʻlingan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Dilnoza kitobning beshdan bir "
                "qismini oʻqidi va 96 bet qoldi.</p><p><strong>Kitobda "
                "nechta bet bor?</strong></p>",
        "choices": ["100", "115", "120", "480"],
        "correct": "120",
        "explanation": "<p><strong>120.</strong> Beshdan biri oʻqilgan "
                       "boʻlsa, <sup>4</sup>/<sub>5</sub> qismi qolgan: "
                       "x × <sup>4</sup>/<sub>5</sub> = 96 → x = 96 × 5 "
                       "÷ 4 = 120. Tekshirish: 120 ÷ 5 = 24 oʻqildi, "
                       "120 − 24 = 96 ✓ <strong>480</strong> — 96 ni "
                       "shunchaki 5 ga koʻpaytirganda chiqadi, ya'ni 96 "
                       "oʻqilgan deb oʻqilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sinfda 30 oʻquvchi bor. "
                "Oʻgʻillar qizlardan 4 taga koʻp.</p><p><strong>Nechta qiz "
                "bor?</strong></p>",
        "choices": ["13", "15", "17", "26"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> x — qizlar, oʻgʻillar "
                       "x + 4. x + (x + 4) = 30 → 2x = 26 → x = 13, "
                       "oʻgʻillar 17. Tekshirish: 13 + 17 = 30 ✓ va "
                       "17 − 13 = 4 ✓ <strong>17</strong> — oʻgʻillar "
                       "soni, <strong>15</strong> esa 30 ni teng ikkiga "
                       "boʻlganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2 soat 45 minut — bu necha "
                "minut?</strong></p>",
        "choices": ["47", "105", "165", "245"],
        "correct": "165",
        "explanation": "<p><strong>165.</strong> 2 × 60 + 45 = 120 + 45 = "
                       "165 minut. <strong>47</strong> — har xil "
                       "birlikdagi sonlar shunchaki qoʻshilganda "
                       "(2 + 45) chiqadi; qoʻshishdan oldin bitta "
                       "birlikka keltiriladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sherbek 3 kg olma va 2 kg nok "
                "olib, 88 000 soʻm toʻladi. Olmaning bir kilosi nokning bir "
                "kilosidan 4 000 soʻm arzon.</p><p><strong>Nokning bir "
                "kilosi necha soʻm?</strong></p>",
        "choices": ["16 000 soʻm", "18 000 soʻm", "20 000 soʻm",
                    "24 000 soʻm"],
        "correct": "20 000 soʻm",
        "explanation": "<p><strong>20 000 soʻm.</strong> x — nokning kilosi, "
                       "olma x − 4 000. 3(x − 4 000) + 2x = 88 000 → "
                       "3x − 12 000 + 2x = 88 000 → 5x = 100 000 → "
                       "x = 20 000. Tekshirish: olma 16 000, "
                       "3 × 16 000 = 48 000 va 2 × 20 000 = 40 000, jami "
                       "88 000 ✓ <strong>16 000</strong> — olmaning "
                       "narxi, savol nokni soʻragan.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi gap "
                "koʻpaytirishni bildiradi?</strong></p>",
        "choices": [
            "Olma daraxti nokdan 12 ta koʻp",
            "Olma daraxti nokdan 12 marta koʻp",
            "Olma daraxti nokdan 12 taga kam",
            "Olma daraxti va nok jami 12 ta",
        ],
        "correct": "Olma daraxti nokdan 12 marta koʻp",
        "explanation": "<p><strong>«12 marta koʻp».</strong> «marta» — "
                       "nisbat, demak koʻpaytirish: 12x. «12 ta koʻp» esa "
                       "ayirma: x + 12. Bu ikkisi matematika xatosi emas, "
                       "til xatosi — shuning uchun masalada bu soʻzlarni "
                       "har doim ajratib belgilang.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki sonning yigʻindisi 60. Biri "
                "ikkinchisidan 3 marta katta.</p><p><strong>Katta son "
                "qanday?</strong></p>",
        "choices": ["15", "20", "45", "60"],
        "correct": "45",
        "explanation": "<p><strong>45.</strong> x + 3x = 60 → 4x = 60 → "
                       "x = 15, lekin x — <strong>kichik</strong> son. "
                       "Savol kattasini soʻragan: 3 × 15 = 45. "
                       "Tekshirish: 15 + 45 = 60 ✓ va 45 ÷ 15 = 3 ✓ "
                       "<strong>15</strong> — eng koʻp uchraydigan xato: "
                       "x topilgach toʻxtab qolish.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nima uchun javob "
                "bitta son emas, gap bilan yoziladi?</strong></p>",
        "choices": [
            "Yozuv chiroyli koʻrinishi uchun",
            "Oʻqituvchi shuni talab qilgani uchun",
            "Soʻralgan narsaga javob berilgani darrov koʻrinishi uchun",
            "Hisob-kitobni qayta tekshirish shart boʻlmasligi uchun",
        ],
        "correct": "Soʻralgan narsaga javob berilgani darrov koʻrinishi "
                   "uchun",
        "explanation": "<p><strong>Soʻralgan narsaga javob berilgani darrov "
                       "koʻrinishi uchun.</strong> «45» degan son oʻzicha "
                       "hech narsa demaydi. «Katta son 45 ga teng» degan "
                       "gap esa savol bilan yonma-yon qoʻyilganda "
                       "mos-nomosligini oshkor qiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki sonning yigʻindisi "
                "84, farqi 12.</p><p><strong>Qaysi juftlik ikkala shartni "
                "ham qanoatlantiradi?</strong></p>",
        "choices": ["30 va 54", "36 va 48", "40 va 44", "42 va 42"],
        "correct": "36 va 48",
        "explanation": "<p><strong>36 va 48.</strong> 36 + 48 = 84 ✓ va "
                       "48 − 36 = 12 ✓ Qolgan uch juftlikning "
                       "yigʻindisi ham 84, lekin farqi mos emas: 24, 4 "
                       "va 0. Shuning uchun tekshirishda masalaning "
                       "<strong>hamma</strong> shartlari koʻriladi, "
                       "bittasi emas.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>«Dilnoza 1 soat 20 minut "
                "yugurdi, Bekzod 95 minut yugurdi. Kim koʻp yugurdi?» — "
                "Oʻquvchi yozdi: «Dilnoza 1 + 20 = 21, Bekzod 95. Demak "
                "Bekzod koʻp».</p><p><strong>Yechimda nima "
                "notoʻgʻri?</strong></p>",
        "choices": [
            "Xulosa notoʻgʻri — aslida Dilnoza koʻp yugurgan",
            "Birliklar keltirilmagan, garchi xulosa toʻgʻri chiqqan boʻlsa ham",
            "Bekzodning vaqti soatga oʻgirilmagan",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Birliklar keltirilmagan, garchi xulosa toʻgʻri chiqqan "
                   "boʻlsa ham",
        "explanation": "<p><strong>Birliklar keltirilmagan.</strong> "
                       "1 + 20 = 21 degan qator maʼnosiz: soat bilan "
                       "minut qoʻshilgan. Toʻgʻrisi 1 × 60 + 20 = 80 "
                       "minut. Xulosa tasodifan toʻgʻri chiqdi (80 &lt; "
                       "95), lekin yoʻl notoʻgʻri — boshqa sonlarda "
                       "javob ham xato boʻlardi.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Bir son va uning "
                "yarmi yigʻindisi 90 ga teng. Bu son qanday?</strong></p>",
        "choices": [
            "x ÷ 2 = 90 → x = 45",
            "2x = 90 → x = 45",
            "1,5x = 90 → x = 60",
            "x + 2 = 90 → x = 88",
        ],
        "correct": "1,5x = 90 → x = 60",
        "explanation": "<p><strong>1,5x = 90 → x = 60.</strong> Sonning oʻzi "
                       "x, yarmi x ÷ 2, yigʻindisi x + x ÷ 2 = 1,5x. "
                       "Tekshirish: 60 + 30 = 90 ✓ <strong>x + 2 = "
                       "90</strong> — «yarmi» qoʻshish deb oʻqilgan; "
                       "«yarmi» boʻlishni bildiradi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Maktab kutubxonasida 340 ta "
                "kitob bor edi. Yangi 85 ta kitob keldi, 60 tasi esa qoʻshni "
                "maktabga berib yuborildi.</p><p><strong>Hozir kutubxonada "
                "nechta kitob bor?</strong></p>",
        "choices": ["195", "365", "425", "485"],
        "correct": "365",
        "explanation": "<p><strong>365.</strong> 340 + 85 = 425, keyin "
                       "425 − 60 = 365. <strong>485</strong> — ikkala "
                       "sonni ham qoʻshib yuborganda chiqadi; berib "
                       "yuborilgan kitoblar ayiriladi. "
                       "<strong>195</strong> — ikkalasi ham "
                       "ayirilganda.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bekzod va Dilnoza birgalikda "
                "84 ta shokolad sotishdi. Bekzod Dilnozadan 3 marta koʻp "
                "sotdi.</p><p><strong>Bekzod Dilnozadan nechtaga koʻp "
                "sotgan?</strong></p>",
        "choices": ["21 ta", "42 ta", "63 ta", "84 ta"],
        "correct": "42 ta",
        "explanation": "<p><strong>42 ta.</strong> x — Dilnoza sotgani. "
                       "x + 3x = 84 → 4x = 84 → x = 21, Bekzod "
                       "3 × 21 = 63. Savol <strong>farqni</strong> "
                       "soʻragan: 63 − 21 = 42. Tekshirish: 21 + 63 = "
                       "84 ✓ va 63 ÷ 21 = 3 ✓ <strong>21</strong> va "
                       "<strong>63</strong> — toʻgʻri hisoblangan, lekin "
                       "soʻralgan savolga javob emas.</p>",
    },
]


# =====================================================================
# PM-86 — nomaʼlumni tanlash va jadval tuzish
# =====================================================================

Q_PM86 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Kitob daftardan 5 marta "
                "qimmat».</p><p><strong>Qaysi narsaning narxini x deb olish "
                "qulay?</strong></p>",
        "choices": [
            "Daftarning narxini",
            "Kitobning narxini",
            "Ikkalasining yigʻindisini",
            "Ikkalasining farqini",
        ],
        "correct": "Daftarning narxini",
        "explanation": "<p><strong>Daftarning narxini.</strong> Kitob "
                       "daftarga qarab taʼriflangan, demak daftar = x va "
                       "kitob = 5x — faqat butun ifodalar. Kitobni x "
                       "desak, daftar x ÷ 5 boʻlib, kasr paydo "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>Muzeyga jami 40 kishi "
                "kirdi, ulardan k tasi katta odam.</p><p><strong>Bolalar "
                "soni — ___</strong></p>",
        "choices": ["40 ÷ k", "40 − k", "40k", "k − 40"],
        "correct": "40 − k",
        "explanation": "<p><strong>40 − k.</strong> Jamidan bir qismi "
                       "ayiriladi. <strong>k − 40</strong> — ayirish "
                       "tartibi teskari va u manfiy son berardi, odamlar "
                       "soni esa manfiy boʻlmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>Bekzodda Afsonadan "
                "3 marta koʻp marka bor. Afsonaning markalari x ta.</p>"
                "<p><strong>Bekzodda ___ ta marka bor.</strong></p>",
        "choices": ["x ÷ 3", "x − 3", "x + 3", "3x"],
        "correct": "3x",
        "explanation": "<p><strong>3x.</strong> Koʻpaytiruvchi koʻp boʻlgan "
                       "tomonga qoʻyiladi. Yozgandan keyin ovoz chiqarib "
                       "oʻqib koʻring: «Bekzodda 3x, Afsonada x — ha, "
                       "Bekzodda koʻproq».</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Afsonada Jasurdan "
                "2 marta koʻp pul bor».</p><p><strong>Kimning pulini x deb "
                "olish qulay?</strong></p>",
        "choices": [
            "Afsonaning pulini",
            "Jasurning pulini",
            "Ikkalasining jamini",
            "Farqi boʻlgan summani",
        ],
        "correct": "Jasurning pulini",
        "explanation": "<p><strong>Jasurning pulini.</strong> Afsonaning "
                       "puli Jasurga qarab taʼriflangan, demak Jasur = x "
                       "va Afsona = 2x. Afsonani x desak, Jasur x ÷ 2 "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nima uchun hamma "
                "miqdorni bitta harf orqali yozish afzal?</strong></p>",
        "choices": [
            "Yozish qisqaroq boʻlgani uchun",
            "Har bir yangi harf yana bitta tenglama talab qilgani uchun",
            "Ikkita harf bilan yechib boʻlmagani uchun",
            "x harfi boshqalaridan qulayroq boʻlgani uchun",
        ],
        "correct": "Har bir yangi harf yana bitta tenglama talab qilgani "
                   "uchun",
        "explanation": "<p><strong>Har bir yangi harf yana bitta tenglama "
                       "talab qilgani uchun.</strong> Uch harf uchun uch "
                       "tenglama kerak. Masalada bogʻlanishlar berilgan "
                       "ekan, ularni ishlatib hammasini bitta harf bilan "
                       "yozish mumkin.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Uch doʻst 120 000 soʻmni "
                "boʻlishdi. Ikkinchisi birinchisidan 2 marta koʻp, uchinchisi "
                "birinchisidan 3 marta koʻp oldi.</p><p><strong>Birinchisi "
                "qancha oldi?</strong></p>",
        "choices": ["20 000 soʻm", "24 000 soʻm", "40 000 soʻm",
                    "60 000 soʻm"],
        "correct": "20 000 soʻm",
        "explanation": "<p><strong>20 000 soʻm.</strong> Hammasi birinchisiga "
                       "qarab aytilgan, demak x — birinchisining ulushi. "
                       "x + 2x + 3x = 120 000 → 6x = 120 000 → "
                       "x = 20 000. Tekshirish: 20 000 + 40 000 + "
                       "60 000 = 120 000 ✓ <strong>40 000</strong> — "
                       "120 000 ni 3 ga boʻlganda chiqadi, ya'ni "
                       "ulushlar teng deb olinganda.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Uch sonning yigʻindisi 101. "
                "Ikkinchisi birinchisidan 4 marta katta, uchinchisi "
                "birinchisidan 5 taga katta.</p><p><strong>Birinchi son "
                "qanday?</strong></p>",
        "choices": ["15", "16", "18", "20"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> x + 4x + (x + 5) = 101 → "
                       "6x + 5 = 101 → 6x = 96 → x = 16. Sonlar: 16, "
                       "64 va 21. Tekshirish: 16 + 64 + 21 = 101 ✓ "
                       "Diqqat: «4 marta» koʻpaytirish, «5 taga» esa "
                       "qoʻshish.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bekzodda Dilnozadan 3 marta koʻp "
                "marka bor. Bekzod Dilnozaga 8 ta marka bersa, ularniki teng "
                "boʻladi.</p><p><strong>Dilnozada nechta marka "
                "bor?</strong></p>",
        "choices": ["4 ta", "8 ta", "12 ta", "16 ta"],
        "correct": "8 ta",
        "explanation": "<p><strong>8 ta.</strong> Jadval tuzamiz. Dilnoza: "
                       "x → x + 8. Bekzod: 3x → 3x − 8. Teng boʻlgani "
                       "uchun 3x − 8 = x + 8 → 2x = 16 → x = 8. "
                       "Tekshirish: Bekzodda 24 ta edi, 24 − 8 = 16 va "
                       "8 + 8 = 16 ✓ <strong>16</strong> — teng "
                       "boʻlgandan keyingi soni.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Muzeyga 25 kishi bordi. Katta "
                "odam chiptasi 12 000 soʻm, bola chiptasi 5 000 soʻm. Jami "
                "174 000 soʻm toʻlandi.</p><p><strong>Nechta katta odam "
                "bor edi?</strong></p>",
        "choices": ["5 ta", "7 ta", "9 ta", "18 ta"],
        "correct": "7 ta",
        "explanation": "<p><strong>7 ta.</strong> x — kattalar, bolalar "
                       "25 − x. 12 000x + 5 000(25 − x) = 174 000 → "
                       "12 000x + 125 000 − 5 000x = 174 000 → "
                       "7 000x = 49 000 → x = 7. Tekshirish: "
                       "7 × 12 000 = 84 000 va 18 × 5 000 = 90 000, jami "
                       "174 000 ✓ <strong>18</strong> — bolalar "
                       "soni.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Qutida 1 000 soʻmlik va "
                "5 000 soʻmlik banknotlar bor. Jami 20 ta banknot, umumiy "
                "summa 76 000 soʻm.</p><p><strong>Nechta besh minglik "
                "bor?</strong></p>",
        "choices": ["6 ta", "10 ta", "14 ta", "16 ta"],
        "correct": "14 ta",
        "explanation": "<p><strong>14 ta.</strong> x — mingliklar soni, besh "
                       "mingliklar 20 − x. 1 000x + 5 000(20 − x) = "
                       "76 000 → 1 000x + 100 000 − 5 000x = 76 000 → "
                       "4 000x = 24 000 → x = 6. Demak besh mingliklar "
                       "20 − 6 = 14 ta. Tekshirish: 6 000 + 70 000 = "
                       "76 000 ✓ <strong>6</strong> — mingliklar "
                       "soni.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki qutida jami 90 ta olma bor. "
                "Birinchi qutida ikkinchisidan 2 marta koʻp.</p>"
                "<p><strong>Birinchi qutida nechta olma bor?</strong></p>",
        "choices": ["30 ta", "45 ta", "60 ta", "70 ta"],
        "correct": "60 ta",
        "explanation": "<p><strong>60 ta.</strong> x — ikkinchi qutidagi "
                       "olmalar (kichigi), birinchisi 2x. x + 2x = 90 → "
                       "3x = 90 → x = 30, birinchisi 60. Tekshirish: "
                       "30 + 60 = 90 ✓ va 60 ÷ 30 = 2 ✓ "
                       "<strong>30</strong> — ikkinchi quti; x topilgach "
                       "toʻxtab qolish eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Afsonada Bekzoddan 4 marta koʻp "
                "pul bor. Afsona Bekzodga 30 000 soʻm bersa, pullari teng "
                "boʻladi.</p><p><strong>Afsonada boshida qancha pul bor "
                "edi?</strong></p>",
        "choices": ["20 000 soʻm", "40 000 soʻm", "60 000 soʻm",
                    "80 000 soʻm"],
        "correct": "80 000 soʻm",
        "explanation": "<p><strong>80 000 soʻm.</strong> Jadval: Bekzod "
                       "x → x + 30 000; Afsona 4x → 4x − 30 000. Teng: "
                       "4x − 30 000 = x + 30 000 → 3x = 60 000 → "
                       "x = 20 000, Afsona 4 × 20 000 = 80 000. "
                       "Tekshirish: 80 000 − 30 000 = 50 000 va "
                       "20 000 + 30 000 = 50 000 ✓ "
                       "<strong>20 000</strong> — Bekzodning puli.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Jasur Afsonadan 2 marta "
                "koʻp yigʻdi».</p><p><strong>Qaysi yozuv "
                "toʻgʻri?</strong></p>",
        "choices": [
            "Afsona = x, Jasur = 2x",
            "Jasur = x, Afsona = 2x",
            "Afsona = 2x, Jasur = 2x",
            "Afsona = x + 2, Jasur = x",
        ],
        "correct": "Afsona = x, Jasur = 2x",
        "explanation": "<p><strong>Afsona = x, Jasur = 2x.</strong> "
                       "Koʻpaytiruvchi koʻp boʻlgan tomonga qoʻyiladi. "
                       "<strong>Jasur = x, Afsona = 2x</strong> — "
                       "bogʻlanish teskari yozilgan va bu yechimni "
                       "boshidanoq buzadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sinfda 28 oʻquvchi bor, "
                "qizlar q ta.</p><p><strong>Oʻgʻillar soni qanday "
                "yoziladi?</strong></p>",
        "choices": ["q − 28", "28 − q", "28q", "q + 28"],
        "correct": "28 − q",
        "explanation": "<p><strong>28 − q.</strong> Jamidan bir qismi "
                       "ayiriladi. <strong>q − 28</strong> manfiy son "
                       "berardi — bu yozuvni tekshirishning eng tez "
                       "yoʻli: q oʻrniga har qanday haqiqiy son "
                       "qoʻying va natijaning mantiqiyligiga "
                       "qarang.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Masalani x = eng "
                "katta miqdor deb yechsak nima boʻladi?</strong></p>",
        "choices": [
            "Javob notoʻgʻri chiqadi",
            "Masala umuman yechilmaydi",
            "Javob oʻsha boʻladi, lekin yoʻlda kasrlar paydo boʻladi",
            "Tenglama tuzib boʻlmaydi",
        ],
        "correct": "Javob oʻsha boʻladi, lekin yoʻlda kasrlar paydo boʻladi",
        "explanation": "<p><strong>Javob oʻsha boʻladi, lekin yoʻlda kasrlar "
                       "paydo boʻladi.</strong> Masala bitta, shuning "
                       "uchun javob ham bitta. Farq faqat mehnatda: "
                       "x ÷ 2 va x ÷ 3 kabi ifodalar bilan ishlash "
                       "xatoga koʻproq imkon beradi. Shuning uchun "
                       "kichigini x deb olish odat qilinadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qachon jadval "
                "tuzish eng foydali boʻladi?</strong></p>",
        "choices": [
            "Masalada faqat bitta son boʻlganda",
            "Masalada ikki holat yoki ikki turdagi narsa boʻlganda",
            "Javob butun son chiqmaganda",
            "Masala geometrik boʻlganda",
        ],
        "correct": "Masalada ikki holat yoki ikki turdagi narsa boʻlganda",
        "explanation": "<p><strong>Ikki holat yoki ikki turdagi narsa "
                       "boʻlganda.</strong> «Boshida — keyin» yoki «katta "
                       "chipta — bola chiptasi» kabi masalalarda "
                       "ustunlar holatlarni, qatorlar qatnashchilarni "
                       "koʻrsatadi. Jadval toʻlgach, tenglama oxirgi "
                       "ustundan oʻzi chiqadi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>«Uch doʻst 180 000 soʻmni "
                "boʻlishdi…» masalasiga oʻquvchi shunday boshladi: «Afsona = "
                "x, Jasur = y, Sherbek = z».</p><p><strong>Nima "
                "notoʻgʻri?</strong></p>",
        "choices": [
            "Harflar notoʻgʻri tanlangan — faqat x ishlatiladi",
            "Bogʻlanishlar berilgan ekan, hammasini bitta harf bilan yozish kerak",
            "Nomaʼlumlar umuman belgilanmasligi kerak edi",
            "Xato yoʻq, yechim toʻgʻri boshlangan",
        ],
        "correct": "Bogʻlanishlar berilgan ekan, hammasini bitta harf bilan "
                   "yozish kerak",
        "explanation": "<p><strong>Hammasini bitta harf bilan yozish "
                       "kerak.</strong> Uch harf uch tenglama talab "
                       "qiladi, masalada esa bitta yigʻindi berilgan. "
                       "Toʻgʻrisi: Afsona = x, Jasur = 2x, Sherbek = "
                       "x + 20 000. Harfning nomi (x, a, n) ahamiyatsiz "
                       "— <strong>soni</strong> muhim.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Uch sonning "
                "yigʻindisi 90. Ikkinchisi birinchisidan 2 marta katta, "
                "uchinchisi birinchisidan 10 taga katta. Birinchi son "
                "qanday?</strong></p>",
        "choices": [
            "3x + 10 = 90 → x ≈ 26,7",
            "4x + 10 = 90 → x = 20",
            "4x = 90 → x = 22,5",
            "x + 2 + 10 = 90 → x = 78",
        ],
        "correct": "4x + 10 = 90 → x = 20",
        "explanation": "<p><strong>4x + 10 = 90 → x = 20.</strong> "
                       "x + 2x + (x + 10) = 90, ya'ni 4x + 10 = 90 → "
                       "4x = 80 → x = 20. Sonlar 20, 40 va 30; "
                       "tekshirish: 20 + 40 + 30 = 90 ✓ "
                       "<strong>4x = 90</strong> — 10 unutilgan, "
                       "<strong>3x + 10</strong> — ikkinchi son x + 2 "
                       "deb olingan, 2x emas.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Kinoteatrga 50 kishi kirdi. "
                "Katta odam chiptasi 25 000 soʻm, bola chiptasi 10 000 soʻm. "
                "Chiptalarga jami 800 000 soʻm toʻlandi.</p><p><strong>Nechta "
                "bola bor edi?</strong></p>",
        "choices": ["15 ta", "20 ta", "30 ta", "35 ta"],
        "correct": "30 ta",
        "explanation": "<p><strong>30 ta.</strong> x — kattalar soni, bolalar "
                       "50 − x. 25 000x + 10 000(50 − x) = 800 000 → "
                       "25 000x + 500 000 − 10 000x = 800 000 → "
                       "15 000x = 300 000 → x = 20 kattalar, demak "
                       "bolalar 50 − 20 = 30. Tekshirish: 20 × 25 000 = "
                       "500 000 va 30 × 10 000 = 300 000, jami "
                       "800 000 ✓ <strong>20</strong> — kattalar soni, "
                       "savol bolalarni soʻragan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Uch aka-uka bogʻda ishlab, "
                "300 000 soʻmni boʻlishdi. Oʻrtanchasi kichigidan 2 marta "
                "koʻp, kattasi esa kichigidan 40 000 soʻm koʻp oldi.</p>"
                "<p><strong>Kattasi qancha oldi?</strong></p>",
        "choices": ["65 000 soʻm", "105 000 soʻm", "130 000 soʻm",
                    "195 000 soʻm"],
        "correct": "105 000 soʻm",
        "explanation": "<p><strong>105 000 soʻm.</strong> Hammasi kichigiga "
                       "qarab aytilgan, demak x — kichigining ulushi. "
                       "x + 2x + (x + 40 000) = 300 000 → "
                       "4x + 40 000 = 300 000 → 4x = 260 000 → "
                       "x = 65 000. Kattasi 65 000 + 40 000 = 105 000. "
                       "Tekshirish: 65 000 + 130 000 + 105 000 = "
                       "300 000 ✓ <strong>65 000</strong> — kichigining "
                       "ulushi, <strong>130 000</strong> — "
                       "oʻrtanchasiniki.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-84 Mashq: Ehtimollikni hisoblash",
        "tutorial":    "PM-84:",
        "description": (
            "Hollarni sanab hisoblash, teskari hodisa qoidasi (1 − P), "
            "nisbiy chastota va tajriba bilan baholash. 20 savol."
        ),
        "questions":   Q_PM84,
        **DEFAULTS,
    },
    {
        "title":       "PM-85 Mashq: Masalani oʻqishning toʻrt qadami",
        "tutorial":    "PM-85:",
        "description": (
            "Soʻzni belgiga aylantirish, berilgan va soʻralganni ajratish, "
            "birliklar va javobni tekshirish. 20 savol."
        ),
        "questions":   Q_PM85,
        **DEFAULTS,
    },
    {
        "title":       "PM-86 Mashq: Nomaʼlumni tanlash va jadval tuzish",
        "tutorial":    "PM-86:",
        "description": (
            "Qaysi miqdorni x deb olish kerak, hammasini bitta harf bilan "
            "yozish va «boshida — keyin» jadvali. 20 savol."
        ),
        "questions":   Q_PM86,
        **DEFAULTS,
    },
]
