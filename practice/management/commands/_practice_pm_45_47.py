# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-45, PM-46, PM-47 (koordinata, masofa, funksiya).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan. BLOK D BOSHI.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: `medium` — toc boʻyicha Blok D (45–56) shu darajadan boshlanadi.

⚠️ `choices` EKRANLANADI — HTML teg yoʻq. Darajalar «x^2» koʻrinishida
   yoziladi, savol matnida esa <sup> ishlatiladi.
⚠️ Kumulyativ: QIYA kesmaning uzunligi soʻralmaydi (Pifagor — PM-64);
   grafik chizish ham yoʻq (PM-48 dan boshlanadi).

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_45_47.py --master=prime \\
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
# PM-45 — koordinata tekisligi
# =====================================================================

Q_PM45 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>A(3; 2) nuqtasiga borish "
                "uchun koordinata boshidan qanday yurish kerak?</strong></p>",
        "choices": [
            "3 katak oʻngga, keyin 2 katak yuqoriga",
            "2 katak oʻngga, keyin 3 katak yuqoriga",
            "3 katak yuqoriga, keyin 2 katak oʻngga",
            "3 katak chapga, keyin 2 katak pastga",
        ],
        "correct": "3 katak oʻngga, keyin 2 katak yuqoriga",
        "explanation": "<p><strong>3 katak oʻngga, keyin 2 katak yuqoriga.</strong> "
                       "Birinchi son doim abssissa — chapga-oʻngga; ikkinchisi "
                       "ordinata — yuqoriga-pastga. <strong>2 katak oʻngga, keyin "
                       "3 katak yuqoriga</strong> — bu A(2; 3) nuqtasi, boshqa "
                       "nuqta.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Koordinata boshining "
                "koordinatalari qanday?</strong></p>",
        "choices": ["(0; 0)", "(0; 1)", "(1; 0)", "(1; 1)"],
        "correct": "(0; 0)",
        "explanation": "<p><strong>(0; 0).</strong> Koordinata boshi — ikki oʻq "
                       "kesishgan nuqta. Undan hech qaysi tomonga yurilmagan, "
                       "shuning uchun ikkala koordinata ham nol.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>(5; −2) nuqtasi qaysi "
                "chorakda?</strong></p>",
        "choices": ["I", "II", "III", "IV"],
        "correct": "IV",
        "explanation": "<p><strong>IV.</strong> Abssissa musbat — nuqta oʻngda; "
                       "ordinata manfiy — pastda. Oʻng past burchak IV chorak "
                       "boʻladi. <strong>I</strong> — ordinataning minusi "
                       "eʼtiborsiz qolgan javob.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nuqtaning birinchi "
                "koordinatasi qanday ataladi?</strong></p>",
        "choices": ["Abssissa", "Ordinata", "Chorak", "Koordinata boshi"],
        "correct": "Abssissa",
        "explanation": "<p><strong>Abssissa.</strong> Bu — x, gorizontal "
                       "yoʻnalishdagi qadam. Ikkinchi koordinata ordinata (y) "
                       "deyiladi va u vertikal yoʻnalishni koʻrsatadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>(−1; −4) nuqtasi qaysi "
                "chorakda?</strong></p>",
        "choices": ["I", "II", "III", "IV"],
        "correct": "III",
        "explanation": "<p><strong>III.</strong> Ikkala koordinata ham manfiy — "
                       "nuqta ham chapda, ham pastda. (−; −) faqat III chorakda "
                       "boʻladi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>(0; 7) nuqtasi qayerda "
                "yotadi?</strong></p>",
        "choices": [
            "Oy oʻqida",
            "Ox oʻqida",
            "I chorakda",
            "II chorakda",
        ],
        "correct": "Oy oʻqida",
        "explanation": "<p><strong>Oy oʻqida.</strong> Abssissasi nol — demak "
                       "chapga ham, oʻngga ham yurilmagan, nuqta vertikal oʻqda "
                       "qolgan. Oʻqda yotgan nuqta hech qaysi chorakka "
                       "tegishli emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>(−6; 0) nuqtasi qayerda "
                "yotadi?</strong></p>",
        "choices": [
            "Ox oʻqida, koordinata boshidan 6 katak chapda",
            "Oy oʻqida, koordinata boshidan 6 katak pastda",
            "II chorakda",
            "III chorakda",
        ],
        "correct": "Ox oʻqida, koordinata boshidan 6 katak chapda",
        "explanation": "<p><strong>Ox oʻqida, 6 katak chapda.</strong> Ordinatasi "
                       "nol boʻlgani uchun nuqta yuqoriga ham, pastga ham "
                       "koʻtarilmagan — u gorizontal oʻqning ustida.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nuqta II chorakda "
                "yotsa, uning koordinatalari qanday ishorada boʻladi?</strong></p>",
        "choices": [
            "x manfiy, y musbat",
            "x musbat, y musbat",
            "x manfiy, y manfiy",
            "x musbat, y manfiy",
        ],
        "correct": "x manfiy, y musbat",
        "explanation": "<p><strong>x manfiy, y musbat.</strong> II chorak — chap "
                       "yuqori burchak: chapda boʻlgani uchun abssissa manfiy, "
                       "yuqorida boʻlgani uchun ordinata musbat.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>A(−5; 3) nuqtasiga "
                "borish uchun qanday yurish kerak?</strong></p>",
        "choices": [
            "5 katak chapga, 3 katak yuqoriga",
            "5 katak oʻngga, 3 katak yuqoriga",
            "5 katak chapga, 3 katak pastga",
            "3 katak chapga, 5 katak yuqoriga",
        ],
        "correct": "5 katak chapga, 3 katak yuqoriga",
        "explanation": "<p><strong>5 katak chapga, 3 katak yuqoriga.</strong> "
                       "Abssissa manfiy — chapga; ordinata musbat — yuqoriga. "
                       "<strong>3 katak chapga, 5 katak yuqoriga</strong> — "
                       "koordinatalar oʻrni almashtirib yuborilgan javob.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Abssissasi 2, ordinatasi "
                "−4 boʻlgan nuqta qanday yoziladi?</strong></p>",
        "choices": ["(2; −4)", "(−4; 2)", "(2; 4)", "(−2; −4)"],
        "correct": "(2; −4)",
        "explanation": "<p><strong>(2; −4).</strong> Avval abssissa, keyin "
                       "ordinata. <strong>(−4; 2)</strong> — tartib buzilgan "
                       "javob; u butunlay boshqa nuqta (II chorakda).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nuqta Ox oʻqida yotadi "
                "va koordinata boshidan 3 katak chapda. Uning koordinatalari "
                "qanday?</strong></p>",
        "choices": ["(−3; 0)", "(0; −3)", "(3; 0)", "(−3; −3)"],
        "correct": "(−3; 0)",
        "explanation": "<p><strong>(−3; 0).</strong> Ox oʻqida yotgani uchun "
                       "ordinata nol; chapda boʻlgani uchun abssissa manfiy. "
                       "<strong>(0; −3)</strong> — Oy oʻqidagi nuqta, "
                       "chalkashtirmang.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Toʻgʻri toʻrtburchakning uchta "
                "burchagi: (1; 1), (6; 1), (6; 4).</p><p><strong>Toʻrtinchi burchak "
                "qayerda?</strong></p>",
        "choices": ["(1; 4)", "(1; 6)", "(4; 1)", "(6; 6)"],
        "correct": "(1; 4)",
        "explanation": "<p><strong>(1; 4).</strong> Toʻrtinchi burchak (1; 1) "
                       "ning ustida (abssissasi 1) va (6; 4) ning yonida "
                       "(ordinatasi 4) boʻlishi kerak. <strong>(4; 1)</strong> — "
                       "koordinatalar oʻrni almashgan javob.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>(4; −7) va (−7; 4) "
                "nuqtalari haqida nima deyish mumkin?</strong></p>",
        "choices": [
            "Birinchisi IV, ikkinchisi II chorakda",
            "Ikkalasi ham IV chorakda",
            "Ikkalasi bitta nuqta",
            "Birinchisi II, ikkinchisi IV chorakda",
        ],
        "correct": "Birinchisi IV, ikkinchisi II chorakda",
        "explanation": "<p><strong>Birinchisi IV, ikkinchisi II chorakda.</strong> "
                       "(4; −7): oʻngda va pastda — IV chorak. (−7; 4): chapda va "
                       "yuqorida — II chorak. Sonlar bir xil, lekin tartib har xil "
                       "boʻlgani uchun nuqtalar butunlay boshqa joyda.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi nuqta hech qaysi "
                "chorakka tegishli emas?</strong></p>",
        "choices": ["(0; −9)", "(3; 1)", "(4; −1)", "(−2; −5)"],
        "correct": "(0; −9)",
        "explanation": "<p><strong>(0; −9).</strong> Koordinatalaridan biri nol "
                       "boʻlgan nuqta oʻqning ustida yotadi, chorak esa oʻqlar "
                       "orasidagi soha. Bu nuqta Oy oʻqida, koordinata boshidan "
                       "9 katak pastda.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi nuqta Ox oʻqidan "
                "eng uzoqda joylashgan?</strong></p>",
        "choices": ["(2; −6)", "(−1; 5)", "(0; 3)", "(7; 1)"],
        "correct": "(2; −6)",
        "explanation": "<p><strong>(2; −6).</strong> Ox oʻqidan uzoqlikni "
                       "<strong>ordinata</strong> aytadi, abssissa emas. "
                       "Uzoqliklar: 6, 5, 3 va 1 katak. <strong>(7; 1)</strong> — "
                       "eng katta birinchi songa qarab tanlangan javob, lekin "
                       "7 gorizontal yoʻnalishni bildiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>A(−3; 5) va B(3; 5) "
                "nuqtalari qanday joylashgan?</strong></p>",
        "choices": [
            "Bir xil balandlikda: A chapda, B oʻngda",
            "Bir vertikal chiziqda: A pastda, B yuqorida",
            "Ikkalasi ham II chorakda",
            "Ikkalasi Ox oʻqida",
        ],
        "correct": "Bir xil balandlikda: A chapda, B oʻngda",
        "explanation": "<p><strong>Bir xil balandlikda: A chapda, B oʻngda.</strong> "
                       "Ordinatalari teng (5) — demak ular bir gorizontal chiziqda. "
                       "Abssissalari qarama-qarshi ishorada boʻlgani uchun biri "
                       "Oy oʻqining chap, ikkinchisi oʻng tomonida.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Afsona: «(−2; 6) nuqtasi IV chorakda, "
                "chunki unda bitta minus bor.»</p><p><strong>Toʻgʻri javob "
                "qaysi?</strong></p>",
        "choices": [
            "Nuqta II chorakda: (−; +) shuni bildiradi",
            "Nuqta IV chorakda — Afsona haq",
            "Nuqta III chorakda",
            "Nuqta Oy oʻqida yotadi",
        ],
        "correct": "Nuqta II chorakda: (−; +) shuni bildiradi",
        "explanation": "<p><strong>Nuqta II chorakda.</strong> Chorakni minuslar "
                       "soni emas, ularning <strong>oʻrni</strong> aniqlaydi. "
                       "Abssissa manfiy — chapda; ordinata musbat — yuqorida. "
                       "Chap yuqori burchak II chorak boʻladi. IV chorakda esa "
                       "aksincha, (+; −).</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Jasur B(0; 5) nuqtasini Ox oʻqiga "
                "qoʻydi.</p><p><strong>Toʻgʻri javob qaysi?</strong></p>",
        "choices": [
            "B Oy oʻqida yotadi, chunki abssissasi nol",
            "B Ox oʻqida yotadi — Jasur haq",
            "B I chorakda yotadi",
            "B koordinata boshida yotadi",
        ],
        "correct": "B Oy oʻqida yotadi, chunki abssissasi nol",
        "explanation": "<p><strong>B Oy oʻqida yotadi.</strong> Nol qaysi "
                       "yoʻnalishda umuman yurilmaganini koʻrsatadi. Bu yerda "
                       "abssissa nol — chapga ham, oʻngga ham yurilmagan, demak "
                       "nuqta vertikal oʻqda, koordinata boshidan 5 katak "
                       "yuqorida.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Katakli xaritada Bekzodning uyi (−3; 2), maktab esa (4; 2) "
                "nuqtada. Har bir katakning tomoni 100 metr.</p><p><strong>Bekzod "
                "maktabgacha necha metr yuradi?</strong></p>",
        "choices": ["100 metr", "300 metr", "700 metr", "900 metr"],
        "correct": "700 metr",
        "explanation": "<p><strong>700 metr.</strong> Ikkala nuqtaning ordinatasi "
                       "bir xil (2), demak yoʻl gorizontal. −3 dan 4 gacha 7 katak: "
                       "−3 dan 0 gacha uchta, 0 dan 4 gacha toʻrtta. "
                       "7 × 100 = 700 metr. <strong>100 metr</strong> — "
                       "4 − 3 = 1 deb, minusni eʼtibordan chiqargan javob.</p>",
    },
    {
        "text": "<p>Sherbek bogʻning chizmasini katakli daftarga tushirdi; har "
                "katak 1 metr. Toʻgʻri toʻrtburchak shaklidagi bogʻning uchta "
                "burchagi: (−1; −2), (5; −2), (5; 3).</p><p><strong>Bogʻning yuzasi "
                "necha m² boʻladi?</strong></p>",
        "choices": ["11 m²", "22 m²", "30 m²", "36 m²"],
        "correct": "30 m²",
        "explanation": "<p><strong>30 m².</strong> Gorizontal tomon: −1 dan 5 gacha "
                       "6 metr. Vertikal tomon: −2 dan 3 gacha 5 metr. "
                       "S = 6 × 5 = 30 m². <strong>22 m²</strong> — yuza oʻrniga "
                       "perimetr hisoblangan javob: 2 × (6 + 5) = 22.</p>",
    },
]


# =====================================================================
# PM-46 — masofa va kesmaning oʻrtasi
# =====================================================================

Q_PM46 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>A(2; 5) va B(9; 5) nuqtalari "
                "orasidagi masofa qancha?</strong></p>",
        "choices": ["4", "5", "7", "11"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Ordinatalar teng, demak kesma "
                       "gorizontal: |9 − 2| = 7 birlik. <strong>11</strong> — "
                       "ayirish oʻrniga qoʻshilgan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>C(3; −1) va D(3; 4) nuqtalari "
                "orasidagi masofa qancha?</strong></p>",
        "choices": ["3", "5", "7", "8"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Abssissalar teng — kesma vertikal: "
                       "|4 − (−1)| = |4 + 1| = 5. <strong>3</strong> — javob "
                       "sifatida ayirmasi emas, bir xil boʻlgan koordinata "
                       "olingan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>A(0; 0) va B(6; 0) kesmasining "
                "oʻrtasi qayerda?</strong></p>",
        "choices": ["(2; 0)", "(3; 0)", "(6; 0)", "(0; 3)"],
        "correct": "(3; 0)",
        "explanation": "<p><strong>(3; 0).</strong> x: (0 + 6) ÷ 2 = 3; "
                       "y: (0 + 0) ÷ 2 = 0. <strong>(0; 3)</strong> — "
                       "koordinatalar oʻrni almashgan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>A(2; 4) va B(8; 4) kesmasining "
                "oʻrtasi qayerda?</strong></p>",
        "choices": ["(3; 4)", "(5; 4)", "(5; 8)", "(6; 4)"],
        "correct": "(5; 4)",
        "explanation": "<p><strong>(5; 4).</strong> x: (2 + 8) ÷ 2 = 5; y oʻzgarmadi, "
                       "chunki ikkala ordinata ham 4. <strong>(3; 4)</strong> — "
                       "yigʻindi oʻrniga ayirma olingan javob: (8 − 2) ÷ 2 = 3.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Son oʻqida −2 va 6 orasidagi masofa "
                "qancha?</strong></p>",
        "choices": ["3", "4", "8", "12"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> |6 − (−2)| = |6 + 2| = 8. "
                       "<strong>4</strong> — minus tushirib qoldirilgan javob "
                       "(6 − 2). Masofa hech qachon manfiy boʻlmaydi, shuning "
                       "uchun modul olinadi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>A(−5; 3) va B(4; 3) nuqtalari "
                "orasidagi masofa qancha?</strong></p>",
        "choices": ["1", "3", "9", "15"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> |4 − (−5)| = |4 + 5| = 9. "
                       "<strong>1</strong> — 5 − 4 deb hisoblangan, minus "
                       "eʼtibordan chiqqan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>C(−2; −7) va D(−2; −1) nuqtalari "
                "orasidagi masofa qancha?</strong></p>",
        "choices": ["2", "6", "8", "9"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Abssissalar teng — kesma vertikal: "
                       "|−1 − (−7)| = |−1 + 7| = 6. <strong>8</strong> — ikkala "
                       "manfiy son qoʻshib yuborilgan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>A(2; 3) va B(8; 11) kesmasining "
                "oʻrtasi qayerda?</strong></p>",
        "choices": ["(3; 4)", "(5; 7)", "(6; 8)", "(10; 14)"],
        "correct": "(5; 7)",
        "explanation": "<p><strong>(5; 7).</strong> x: (2 + 8) ÷ 2 = 5; "
                       "y: (3 + 11) ÷ 2 = 7. <strong>(3; 4)</strong> — ayirmalarning "
                       "yarmi, yaʼni kesmaning yarim eni va yarim balandligi; bu "
                       "oʻrta nuqtaning manzili emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>A(−4; 1) va B(6; −3) kesmasining "
                "oʻrtasi qayerda?</strong></p>",
        "choices": ["(1; −1)", "(1; 2)", "(2; −1)", "(5; −2)"],
        "correct": "(1; −1)",
        "explanation": "<p><strong>(1; −1).</strong> x: (−4 + 6) ÷ 2 = 2 ÷ 2 = 1; "
                       "y: (1 + (−3)) ÷ 2 = (−2) ÷ 2 = −1. Manfiy sonlar ham "
                       "xuddi shunday qoʻshiladi (PM-10).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>A(−7; 2) va B(−1; 2) nuqtalari "
                "orasidagi masofa qancha?</strong></p>",
        "choices": ["4", "6", "8", "14"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> |−1 − (−7)| = |−1 + 7| = 6. "
                       "<strong>8</strong> — ikkala sonning moduli qoʻshib "
                       "yuborilgan javob (7 + 1); bu ikkalasi ham manfiy "
                       "boʻlganda notoʻgʻri.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>AB kesmasining oʻrtasi M(−1; 2), "
                "bitta uchi esa A(−6; 2).</p><p><strong>Ikkinchi uch B qayerda?"
                "</strong></p>",
        "choices": ["(−11; 2)", "(1; 2)", "(4; 2)", "(5; 2)"],
        "correct": "(4; 2)",
        "explanation": "<p><strong>(4; 2).</strong> A dan M gacha 5 katak oʻngga "
                       "yurildi, oʻrtadan ikkinchi uchgacha ham xuddi shuncha: "
                       "−1 + 5 = 4. Tekshirish: (−6 + 4) ÷ 2 = −1 ✓ "
                       "<strong>(−11; 2)</strong> — teskari tomonga yurilgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>CD kesmasining oʻrtasi M(3; 5), "
                "bitta uchi esa C(3; 1).</p><p><strong>Ikkinchi uch D qayerda?"
                "</strong></p>",
        "choices": ["(3; 4)", "(3; 6)", "(3; 9)", "(3; 10)"],
        "correct": "(3; 9)",
        "explanation": "<p><strong>(3; 9).</strong> Abssissa oʻzgarmaydi (kesma "
                       "vertikal). C dan M gacha 4 katak yuqoriga, demak M dan D "
                       "gacha yana 4: 5 + 4 = 9. Tekshirish: (1 + 9) ÷ 2 = 5 ✓</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>A(1; 5) va B(7; 5) "
                "orasidagi masofa qaysi koordinatalar bilan topiladi?</strong></p>",
        "choices": [
            "Abssissalar bilan: |7 − 1| = 6",
            "Ordinatalar bilan: |5 − 5| = 0",
            "Toʻrtala son qoʻshiladi: 1 + 5 + 7 + 5 = 18",
            "Abssissalar qoʻshiladi: 1 + 7 = 8",
        ],
        "correct": "Abssissalar bilan: |7 − 1| = 6",
        "explanation": "<p><strong>Abssissalar bilan: |7 − 1| = 6.</strong> "
                       "Masofani <strong>oʻzgargan</strong> koordinata beradi. "
                       "Bu yerda ordinatalar bir xil — ular faqat kesma qaysi "
                       "balandlikda turganini aytadi, uzunligini emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>A(2; 3) va B(8; 11) uchun "
                "|8 − 2| = 6 hisoblandi.</p><p><strong>Bu 6 nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Faqat gorizontal farqni, kesmaning uzunligini emas",
            "AB kesmasining uzunligini",
            "Kesmaning oʻrtasining abssissasini",
            "Kesmaning vertikal farqini",
        ],
        "correct": "Faqat gorizontal farqni, kesmaning uzunligini emas",
        "explanation": "<p><strong>Faqat gorizontal farqni.</strong> Bu kesma qiya: "
                       "gorizontal boʻyicha 6, vertikal boʻyicha |11 − 3| = 8 "
                       "birlik. Qiya kesmaning uzunligi ikkalasidan hisoblanadi, "
                       "lekin buning formulasi Pifagor teoremasiga tayanadi — "
                       "u PM-64 darsida.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>A(−4; 0) va B(6; 0) "
                "berilgan.</p><p><strong>Masofa va oʻrta nuqta qaysi javobda "
                "toʻgʻri?</strong></p>",
        "choices": [
            "Masofa 2, oʻrtasi (5; 0)",
            "Masofa 10, oʻrtasi (1; 0)",
            "Masofa 10, oʻrtasi (5; 0)",
            "Masofa 24, oʻrtasi (1; 0)",
        ],
        "correct": "Masofa 10, oʻrtasi (1; 0)",
        "explanation": "<p><strong>Masofa 10, oʻrtasi (1; 0).</strong> "
                       "Masofa: |6 − (−4)| = 10. Oʻrta: (−4 + 6) ÷ 2 = 1. "
                       "Masofada <strong>ayirma</strong>, oʻrtada esa "
                       "<strong>yigʻindi</strong> ishlatiladi — ikki amal "
                       "adashtirilmasin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi ikki nuqta "
                "orasidagi masofa 5 ga teng?</strong></p>",
        "choices": [
            "(0; 3) va (0; 7)",
            "(1; 2) va (6; 2)",
            "(5; −1) va (5; 2)",
            "(−2; 1) va (4; 1)",
        ],
        "correct": "(1; 2) va (6; 2)",
        "explanation": "<p><strong>(1; 2) va (6; 2).</strong> |6 − 1| = 5. "
                       "Qolganlari: |7 − 3| = 4; |2 − (−1)| = 3; |4 − (−2)| = 6. "
                       "Har safar oʻzgargan koordinata olinadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Dilnoza A(−3; 2) va B(5; 2) orasidagi "
                "masofani 5 − 3 = 2 deb hisobladi.</p><p><strong>Toʻgʻri javob "
                "qaysi?</strong></p>",
        "choices": [
            "|5 − (−3)| = 8",
            "5 − 3 = 2 — Dilnoza haq",
            "|5 + 3| ÷ 2 = 4",
            "|2 − 2| = 0",
        ],
        "correct": "|5 − (−3)| = 8",
        "explanation": "<p><strong>|5 − (−3)| = 8.</strong> Dilnoza minus "
                       "ishorasini tushirib qoldirgan. Manfiy sonni ayirish — uni "
                       "qoʻshish demakdir (PM-10): 5 + 3 = 8. Chizmaga qarasangiz "
                       "ham koʻrinadi: −3 dan 0 gacha 3 katak, 0 dan 5 gacha "
                       "5 katak.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Jasur A(1; 2) va B(7; 6) kesmasining "
                "oʻrtasini ((7 − 1) ÷ 2; (6 − 2) ÷ 2) = (3; 2) deb topdi.</p>"
                "<p><strong>Toʻgʻri javob qaysi?</strong></p>",
        "choices": [
            "(3; 2) — Jasur haq",
            "(4; 4), chunki ayirma emas, yigʻindi olinadi",
            "(6; 4), chunki koordinatalar qoʻshiladi",
            "(8; 8), chunki koordinatalar ikkilanadi",
        ],
        "correct": "(4; 4), chunki ayirma emas, yigʻindi olinadi",
        "explanation": "<p><strong>(4; 4).</strong> x: (1 + 7) ÷ 2 = 4; "
                       "y: (2 + 6) ÷ 2 = 4. Jasur topgan (3; 2) — bu kesmaning "
                       "yarim eni va yarim balandligi, oʻrta nuqtaning manzili "
                       "emas. Tekshirish: 4 − 1 = 3 va 7 − 4 = 3 ✓</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Shahar koʻchalari katak boʻlib joylashgan. Afsonaning uyi "
                "(−3; 4), Dilnozaning uyi (5; 4) nuqtada; bitta katak 150 metr. "
                "Ular teng masofa yurib, yoʻlning oʻrtasida uchrashishdi.</p>"
                "<p><strong>Har biri necha metr yurdi?</strong></p>",
        "choices": ["300 metr", "450 metr", "600 metr", "1200 metr"],
        "correct": "600 metr",
        "explanation": "<p><strong>600 metr.</strong> Uylar orasi: "
                       "|5 − (−3)| = 8 katak, yaʼni 8 × 150 = 1200 metr. "
                       "Uchrashuv joyi oʻrtada, demak har biri yarim yoʻlni "
                       "bosdi: 1200 ÷ 2 = 600 metr. <strong>1200 metr</strong> — "
                       "butun masofa, bitta odamning yoʻli emas.</p>",
    },
    {
        "text": "<p>Dalaga sugʻorish trubasi tortildi: u xaritada (2; −3) "
                "nuqtadan (2; 9) nuqtagacha boradi. Har bir katak 5 metr. "
                "Trubaning roppa-rosa oʻrtasiga nasos oʻrnatiladi.</p>"
                "<p><strong>Truba necha metr va nasos qaysi nuqtada?</strong></p>",
        "choices": [
            "30 metr, nasos (2; 3) da",
            "60 metr, nasos (2; 3) da",
            "60 metr, nasos (2; 6) da",
            "72 metr, nasos (2; 6) da",
        ],
        "correct": "60 metr, nasos (2; 3) da",
        "explanation": "<p><strong>60 metr, nasos (2; 3) da.</strong> Uzunlik: "
                       "|9 − (−3)| = 12 katak, 12 × 5 = 60 metr. Oʻrtasi: abssissa "
                       "oʻzgarmaydi (2), ordinata (−3 + 9) ÷ 2 = 3. "
                       "<strong>(2; 6)</strong> — manfiy uchni hisobga olmay, "
                       "12 ning yarmini 9 dan emas, 0 dan sanagan javob.</p>",
    },
]


# =====================================================================
# PM-47 — funksiya gʻoyasi
# =====================================================================

Q_PM47 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>y = 2x + 3 boʻlsa, x = 4 da y nechaga "
                "teng?</strong></p>",
        "choices": ["9", "11", "14", "24"],
        "correct": "11",
        "explanation": "<p><strong>11.</strong> Avval koʻpaytirish: 2 × 4 = 8, "
                       "keyin 8 + 3 = 11. <strong>14</strong> — qavs qoʻshib "
                       "yuborilgan javob: 2 × (4 + 3); formulada qavs yoʻq.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = 3x − 1 boʻlsa, x = 5 da y nechaga "
                "teng?</strong></p>",
        "choices": ["12", "14", "15", "16"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> 3 × 5 = 15, keyin 15 − 1 = 14. "
                       "<strong>12</strong> — avval 5 − 1 = 4 qilib, keyin 3 ga "
                       "koʻpaytirgan javob; amallar tartibi buzilgan (PM-5).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>f(x) = x + 7 boʻlsa, f(0) nechaga "
                "teng?</strong></p>",
        "choices": ["0", "1", "7", "8"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Nol kiritildi: 0 + 7 = 7. "
                       "<strong>0</strong> — «nol kirsa nol chiqadi» degan "
                       "notoʻgʻri fikr; qoʻshuvchi 7 hech qayerga "
                       "yoʻqolmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = 5x boʻlsa, x = 6 da y nechaga "
                "teng?</strong></p>",
        "choices": ["11", "25", "30", "56"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> 5x — bu 5 × x, demak 5 × 6 = 30. "
                       "<strong>11</strong> — koʻpaytirish oʻrniga qoʻshilgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>f(x) = 10 − x boʻlsa, f(4) nechaga "
                "teng?</strong></p>",
        "choices": ["4", "6", "14", "40"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 10 − 4 = 6. <strong>40</strong> — "
                       "f(4) ni «f ni 4 ga koʻpaytirish» deb tushungan javob; "
                       "qavs bu yerda koʻpaytirishni emas, kiritishni "
                       "bildiradi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>y = 2x + 3 boʻlsa, x = 0 da y nechaga "
                "teng?</strong></p>",
        "choices": ["0", "2", "3", "5"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> 2 × 0 = 0, keyin 0 + 3 = 3. Nol "
                       "kiritilganda faqat oʻzgarmas had qoladi — bu har qanday "
                       "funksiyada shunday.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>f(x) = x<sup>2</sup> + 1 boʻlsa, "
                "f(−3) nechaga teng?</strong></p>",
        "choices": ["−8", "−5", "7", "10"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> (−3)<sup>2</sup> = 9, chunki ikkita "
                       "manfiyning koʻpaytmasi musbat (PM-11); keyin 9 + 1 = 10. "
                       "<strong>−8</strong> — kvadratni −9 deb hisoblagan "
                       "javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = 10 − 2x boʻlsa, x = 3 da y nechaga "
                "teng?</strong></p>",
        "choices": ["4", "8", "16", "24"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Avval koʻpaytirish: 2 × 3 = 6, keyin "
                       "10 − 6 = 4. <strong>24</strong> — avval 10 − 2 = 8 qilib, "
                       "keyin 3 ga koʻpaytirgan javob (amallar tartibi buzilgan); "
                       "<strong>16</strong> — ayirish oʻrniga qoʻshilgan "
                       "javob (10 + 6).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 4x + 2 boʻlsa, "
                "y = 30 boʻlishi uchun x qanday boʻlishi kerak?</strong></p>",
        "choices": ["7", "8", "28", "122"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Teskari savol — tenglama yechiladi: "
                       "4x + 2 = 30 → 4x = 28 → x = 7. Tekshirish: 4 × 7 + 2 = 30 ✓ "
                       "<strong>122</strong> — formulani qayta qoʻllagan javob: "
                       "4 × 30 + 2.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>y = 2x + 3 boʻlsa, "
                "y = 23 boʻlishi uchun x qanday boʻlishi kerak?</strong></p>",
        "choices": ["10", "13", "20", "49"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 2x + 3 = 23 → 2x = 20 → x = 10. "
                       "Tekshirish: 2 × 10 + 3 = 23 ✓ <strong>20</strong> — "
                       "faqat 3 ni ayirib, ikkiga boʻlishni unutgan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>f(x) = 3x − 4 boʻlsa, f(−2) nechaga "
                "teng?</strong></p>",
        "choices": ["−10", "−2", "2", "10"],
        "correct": "−10",
        "explanation": "<p><strong>−10.</strong> 3 × (−2) = −6, keyin "
                       "−6 − 4 = −10. <strong>−2</strong> — −6 − 4 ni −2 deb "
                       "hisoblagan javob; ikkala son ham manfiy boʻlgani uchun "
                       "ular qoʻshiladi va natija yanada kichrayadi (PM-10).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>y = x ÷ 2 + 5 boʻlsa, x = 8 da y "
                "nechaga teng?</strong></p>",
        "choices": ["6,5", "9", "13", "18"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> Avval boʻlish: 8 ÷ 2 = 4, keyin "
                       "4 + 5 = 9. <strong>6,5</strong> — avval 8 + 5 = 13 qilib, "
                       "keyin ikkiga boʻlgan javob; amallar tartibi buzilgan.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p>y = 2x + 3 formulasida x = 4 "
                "boʻlsin.</p><p><strong>Toʻgʻri hisobni tanlang.</strong></p>",
        "choices": [
            "2 × 4 + 3 = 11",
            "2 × (4 + 3) = 14",
            "2 + 4 × 3 = 14",
            "(2 + 3) × 4 = 20",
        ],
        "correct": "2 × 4 + 3 = 11",
        "explanation": "<p><strong>2 × 4 + 3 = 11.</strong> Formulada qavs yoʻq, "
                       "demak amallar tartibi boʻyicha avval koʻpaytirish "
                       "bajariladi (PM-5). Qolgan uchtasi — boshqa qoidalar, "
                       "yaʼni boshqa funksiyalar.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>f(4) = 11 yozuvi nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "f funksiyasiga 4 kiritilsa, 11 chiqadi",
            "f ni 4 ga koʻpaytirsa, 11 chiqadi",
            "f funksiyasiga 11 kiritilsa, 4 chiqadi",
            "f oʻzgaruvchisi 4 va 11 ga teng",
        ],
        "correct": "f funksiyasiga 4 kiritilsa, 11 chiqadi",
        "explanation": "<p><strong>f funksiyasiga 4 kiritilsa, 11 chiqadi.</strong> "
                       "f — mashinaning nomi, koʻpaytuvchi emas. Qavs ichidagi son "
                       "kirish (argument), tenglikdan keyingisi esa chiqish "
                       "(funksiyaning qiymati).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Jadval: x = 1 da y = 4; x = 2 da "
                "y = 7; x = 3 da y = 10.</p><p><strong>Qoida qaysi "
                "formulada?</strong></p>",
        "choices": ["y = x + 3", "y = 3x + 1", "y = 4x", "y = 3x + 4"],
        "correct": "y = 3x + 1",
        "explanation": "<p><strong>y = 3x + 1.</strong> Tekshiramiz: 3 × 1 + 1 = 4 ✓, "
                       "3 × 2 + 1 = 7 ✓, 3 × 3 + 1 = 10 ✓. x bir birlikka oʻsganda "
                       "y uch birlikka oʻsayapti — demak koʻpaytuvchi 3. "
                       "<strong>y = 4x</strong> faqat birinchi ustunga toʻgʻri "
                       "keladi, ikkinchisiga esa yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Quyidagi qoidalardan "
                "qaysi biri funksiya EMAS?</strong></p>",
        "choices": [
            "Har bir songa undan kichik son mos qoʻyiladi",
            "Har bir songa uning kvadrati mos qoʻyiladi",
            "Har bir oʻquvchiga uning tugʻilgan sanasi mos qoʻyiladi",
            "Har bir kunga oʻsha kundagi eng yuqori harorat mos qoʻyiladi",
        ],
        "correct": "Har bir songa undan kichik son mos qoʻyiladi",
        "explanation": "<p><strong>Har bir songa undan kichik son.</strong> "
                       "Funksiyada har bir kirishga <strong>faqat bitta</strong> "
                       "chiqish toʻgʻri kelishi kerak. 10 dan kichik sonlar esa "
                       "cheksiz koʻp — mashina har safar boshqa javob berardi, "
                       "yaʼni ishonchsiz boʻlardi. Qolgan uchtasida javob "
                       "yagona.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Sherbek y = 2x + 3 formulasida x = 4 "
                "uchun 2 × (4 + 3) = 14 deb yozdi.</p><p><strong>Toʻgʻri javob "
                "qaysi?</strong></p>",
        "choices": [
            "11 — formulada qavs yoʻq, avval koʻpaytiriladi",
            "14 — Sherbek haq",
            "20 — avval 2 va 3 qoʻshiladi",
            "24 — hamma sonlar koʻpaytiriladi",
        ],
        "correct": "11 — formulada qavs yoʻq, avval koʻpaytiriladi",
        "explanation": "<p><strong>11.</strong> Sherbek oʻzi qavs qoʻshib yuborgan, "
                       "qavs esa hisob tartibini oʻzgartiradi. 2x + 3 da avval "
                       "2 × 4 = 8 bajariladi, keyin 8 + 3 = 11 (PM-5).</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>y = 2x + 3 da y = 25 boʻlsin. Afsona "
                "x = 2 × 25 + 3 = 53 deb javob berdi.</p><p><strong>Toʻgʻri javob "
                "qaysi?</strong></p>",
        "choices": [
            "x = 11, chunki tenglama yechiladi",
            "x = 53 — Afsona haq",
            "x = 14, chunki 25 dan 11 ayiriladi",
            "x = 28, chunki 25 ga 3 qoʻshiladi",
        ],
        "correct": "x = 11, chunki tenglama yechiladi",
        "explanation": "<p><strong>x = 11.</strong> Chiqish maʼlum boʻlganda qoida "
                       "qayta qoʻllanmaydi — tenglama tuziladi (PM-36): "
                       "2x + 3 = 25 → 2x = 22 → x = 11. Tekshirish: "
                       "2 × 11 + 3 = 25 ✓</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Bosmaxona har bir buyurtma uchun 15 000 soʻm tayyorgarlik haqi "
                "oladi, ustiga har bir nusxa uchun 500 soʻm qoʻshadi.</p>"
                "<p><strong>60 nusxa necha soʻm turadi?</strong></p>",
        "choices": ["30 000 soʻm", "45 000 soʻm", "75 000 soʻm", "930 000 soʻm"],
        "correct": "45 000 soʻm",
        "explanation": "<p><strong>45 000 soʻm.</strong> Qoida: "
                       "N(x) = 15 000 + 500x. N(60) = 15 000 + 500 × 60 = "
                       "15 000 + 30 000 = 45 000. <strong>30 000 soʻm</strong> — "
                       "oʻzgarmas tayyorgarlik haqi qoʻshilmagan javob.</p>",
    },
    {
        "text": "<p>Suv yetkazish xizmati har bir chaqiruv uchun 8 000 soʻm, har "
                "bir ballon uchun esa 12 000 soʻm oladi. Karim aka jami 56 000 soʻm "
                "toʻladi.</p><p><strong>U nechta ballon buyurtma qilgan?</strong></p>",
        "choices": ["3 ta", "4 ta", "5 ta", "7 ta"],
        "correct": "4 ta",
        "explanation": "<p><strong>4 ta.</strong> Qoida: T(x) = 8 000 + 12 000x. "
                       "Teskari savol — tenglama: 8 000 + 12 000x = 56 000 → "
                       "12 000x = 48 000 → x = 4. Tekshirish: "
                       "8 000 + 48 000 = 56 000 ✓ <strong>7 ta</strong> — "
                       "chaqiruv haqini ayirmay, 56 000 ni toʻgʻridan-toʻgʻri "
                       "boʻlishga urinilgan javob.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-45 Mashq: Koordinata tekisligi",
        "description": "20 savol — abssissa va ordinata, koordinata boshi, toʻrt "
                       "chorak va oʻqlar ustidagi nuqtalar.",
        "tutorial":    "PM-45:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM45,
    },
    {
        "title":       "PM-46 Mashq: Masofa va kesmaning oʻrtasi",
        "description": "20 savol — gorizontal va vertikal masofa moduli hamda "
                       "kesmaning oʻrtasi.",
        "tutorial":    "PM-46:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM46,
    },
    {
        "title":       "PM-47 Mashq: Funksiya gʻoyasi",
        "description": "20 savol — kirish, qoida va chiqish; f(x) belgisi, jadval "
                       "va teskari savol.",
        "tutorial":    "PM-47:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM47,
    },
]
