# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-28 … PM-30 (proporsiya/masshtab, harf, ifoda tuzish).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ `text` |safe bilan chiqadi (HTML mumkin), `choices` esa ekranlanadi —
   u yerda HTML teg yoʻq. Shuning uchun darajalar «a2» emas, «a·a» yoki
   soʻz bilan beriladi; kasrlar «a/2», nisbatlar «1 : 3» koʻrinishida.
⚠️ Kumulyativ: PM-28 da harf yoʻq (nomaʼlum «?»); oʻxshash hadlarni
   ixchamlash (PM-32), qavs ochish (PM-33) va tenglama yechish (PM-36) bu
   uch testda yoʻq — PM-30 da qavs faqat yoziladi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_28_30.py --master=prime \\
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
# PM-28 — proporsiya, masshtab, toʻgʻri va teskari proporsionallik
# =====================================================================

Q_PM28 = [
    # 1–5 tanish
    {
        "text": "<p>Masalani yeching.</p><p>5 kg olma 60 000 soʻm turadi.</p>"
                "<p><strong>1 kg olma qancha?</strong></p>",
        "choices": ["10 000 soʻm", "12 000 soʻm", "15 000 soʻm", "30 000 soʻm"],
        "correct": "12 000 soʻm",
        "explanation": "<p><strong>12 000 soʻm.</strong> 60 000 ÷ 5 = 12 000. Bu — "
                       "«bir birlik» usulining birinchi qadami, undan keyin istalgan "
                       "ogʻirlikni hisoblash oson.</p>",
    },
    {
        "text": "<p>Nomaʼlum hadni toping.</p><p><strong>3/4 = ?/20</strong></p>",
        "choices": ["12", "15", "16", "17"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> Maxraj 5 marta oshdi (4 → 20), demak "
                       "surat ham: 3 × 5 = 15. Tekshirish: 3 × 20 = 60 va "
                       "4 × 15 = 60 ✓</p>",
    },
    {
        "text": "<p>Nomaʼlum hadni toping.</p><p><strong>2/5 = 6/?</strong></p>",
        "choices": ["10", "12", "15", "30"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> Surat 3 marta oshdi (2 → 6), maxraj "
                       "ham shuncha: 5 × 3 = 15. <strong>30</strong> — 5 ni 6 ga "
                       "koʻpaytirishdan chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Masshtab 1 : 100 000.</p>"
                "<p><strong>Xaritadagi 1 sm yerda qancha?</strong></p>",
        "choices": ["1 metr", "100 metr", "1 kilometr", "100 kilometr"],
        "correct": "1 kilometr",
        "explanation": "<p><strong>1 kilometr.</strong> 1 sm = 100 000 sm; "
                       "100 000 sm = 1000 m = 1 km. <strong>100 kilometr</strong> — "
                       "masshtabdagi sonni kilometr deb oʻqishdan chiqadigan xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Toʻgʻri proporsionallikda "
                "bir miqdor 2 marta oshsa, ikkinchisi qanday oʻzgaradi?</strong></p>",
        "choices": [
            "2 marta oshadi",
            "2 marta kamayadi",
            "2 taga oshadi",
            "Oʻzgarmaydi",
        ],
        "correct": "2 marta oshadi",
        "explanation": "<p><strong>2 marta oshadi.</strong> Toʻgʻri proporsionallikda "
                       "miqdorlar birga oʻsadi va ularning boʻlinmasi oʻzgarmaydi. "
                       "<strong>2 marta kamayadi</strong> — bu teskari "
                       "proporsionallik.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Masalani yeching.</p><p>5 kg olma 60 000 soʻm.</p>"
                "<p><strong>8 kg qancha turadi?</strong></p>",
        "choices": ["84 000 soʻm", "96 000 soʻm", "120 000 soʻm", "480 000 soʻm"],
        "correct": "96 000 soʻm",
        "explanation": "<p><strong>96 000 soʻm.</strong> Bir kilogramm "
                       "60 000 ÷ 5 = 12 000; 12 000 × 8 = 96 000. "
                       "<strong>480 000</strong> — bir birlikning narxini topmasdan "
                       "60 000 ni 8 ga koʻpaytirishdan chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>4 kishi uchun 600 gramm guruch "
                "kerak.</p><p><strong>6 kishiga qancha kerak?</strong></p>",
        "choices": ["750 gramm", "900 gramm", "1000 gramm", "3600 gramm"],
        "correct": "900 gramm",
        "explanation": "<p><strong>900 gramm.</strong> Bir kishiga 600 ÷ 4 = 150 g; "
                       "150 × 6 = 900 g. Odam koʻpaydi — guruch ham koʻpaydi, demak "
                       "bogʻlanish toʻgʻri.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Masshtab 1 : 500 000.</p>"
                "<p><strong>Xaritadagi 2 sm yerda necha kilometr?</strong></p>",
        "choices": ["1 km", "5 km", "10 km", "100 km"],
        "correct": "10 km",
        "explanation": "<p><strong>10 km.</strong> 1 sm = 500 000 sm = 5 km; "
                       "5 × 2 = 10 km. <strong>5 km</strong> — bitta santimetrning "
                       "javobi, ikkitasiniki emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Masshtab 1 : 25 000.</p>"
                "<p><strong>Xaritadagi 4 sm yerda necha metr?</strong></p>",
        "choices": ["250 metr", "500 metr", "1000 metr", "2500 metr"],
        "correct": "1000 metr",
        "explanation": "<p><strong>1000 metr.</strong> 1 sm = 25 000 sm = 250 m; "
                       "250 × 4 = 1000 m, yaʼni 1 km.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>4 ishchi ishni 12 kunda "
                "bajaradi.</p><p><strong>6 ishchi shu ishni necha kunda "
                "bajaradi?</strong></p>",
        "choices": ["6 kun", "8 kun", "10 kun", "18 kun"],
        "correct": "8 kun",
        "explanation": "<p><strong>8 kun.</strong> Ish hajmi 4 × 12 = 48 ishchi-kun; "
                       "48 ÷ 6 = 8. <strong>18 kun</strong> — teskari bogʻlanishga "
                       "proporsiya qoʻllashdan chiqadi, lekin ishchi koʻpaysa ish "
                       "tezroq tugaydi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Mashina 60 km/soat tezlikda 4 soat "
                "yurdi.</p><p><strong>Shu yoʻlni 80 km/soat tezlikda necha soatda "
                "bosib oʻtadi?</strong></p>",
        "choices": ["2 soat", "3 soat", "3,5 soat", "5 soat"],
        "correct": "3 soat",
        "explanation": "<p><strong>3 soat.</strong> Yoʻl 60 × 4 = 240 km; "
                       "240 ÷ 80 = 3. Tezlik oshdi — vaqt kamaydi. Tekshirish: "
                       "80 × 3 = 240 ✓</p>",
    },
    {
        "text": "<p>Nomaʼlum hadni toping.</p><p><strong>9/12 = ?/8</strong></p>",
        "choices": ["3", "6", "9", "11"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Asosiy xossa bilan: 9 × 8 = 72, demak "
                       "? × 12 = 72 va ? = 6. Yoki 9/12 ni qisqartiramiz: 3/4 = 6/8.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi juftlik TESKARI "
                "proporsional?</strong></p>",
        "choices": [
            "Olma ogʻirligi va uning narxi",
            "Tezlik va yoʻlga ketgan vaqt",
            "Ishlagan soat va olingan haq",
            "Kishilar soni va kerakli non",
        ],
        "correct": "Tezlik va yoʻlga ketgan vaqt",
        "explanation": "<p><strong>Tezlik va vaqt.</strong> Tezlik oshsa vaqt "
                       "kamayadi, ularning koʻpaytmasi (yaʼni yoʻl) oʻzgarmaydi. "
                       "Qolgan uchtasida miqdorlar birga oshadi — ular toʻgʻri "
                       "proporsional.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi tenglik proporsiya "
                "EMAS?</strong></p>",
        "choices": ["2/3 = 8/12", "3/5 = 9/15", "4/6 = 6/9", "5/8 = 10/15"],
        "correct": "5/8 = 10/15",
        "explanation": "<p><strong>5/8 = 10/15</strong> proporsiya emas: "
                       "5 × 15 = 75, lekin 8 × 10 = 80 — teng emas. Toʻgʻrisi 10/16 "
                       "boʻlar edi. Qolgan uchtasida kesishma koʻpaytmalar teng.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>3 usta hovlini 8 kunda "
                "gʻishtlaydi.</p><p><strong>Ishni 6 kunda tugatish uchun nechta usta "
                "kerak?</strong></p>",
        "choices": ["2 usta", "4 usta", "6 usta", "16 usta"],
        "correct": "4 usta",
        "explanation": "<p><strong>4 usta.</strong> Ish hajmi 3 × 8 = 24 usta-kun; "
                       "24 ÷ 6 = 4. Kun kamaydi — usta koʻpayishi kerak. "
                       "<strong>2 usta</strong> — bogʻlanishni teskari tomonga "
                       "oʻqishdan chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki xarita bir xil yerni "
                "koʻrsatadi.</p><p><strong>Qaysi masshtabda yer yiriroq "
                "koʻrinadi?</strong></p>",
        "choices": ["1 : 10 000", "1 : 100 000", "1 : 500 000", "Ikkalasi bir xil"],
        "correct": "1 : 10 000",
        "explanation": "<p><strong>1 : 10 000.</strong> Boʻluvchi qancha kichik "
                       "boʻlsa, tasvir shuncha yirik: bu xaritada 1 sm atigi 100 "
                       "metrni bildiradi, 1 : 500 000 da esa 5 kilometrni.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>Masshtab 1 : 100 000, "
                "xaritada 3 sm. Yechim: 3 × 100 000 = 300 000 km</strong></p>",
        "choices": [
            "Birlik almashtirilmagan: 300 000 sm = 3 km",
            "Koʻpaytirish oʻrniga boʻlish kerak edi",
            "Masshtab teskari oʻqilgan",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Birlik almashtirilmagan: 300 000 sm = 3 km",
        "explanation": "<p><strong>Birlik almashtirilmagan.</strong> Masshtabdagi son "
                       "santimetrni bildiradi: 3 × 100 000 = 300 000 sm, uni "
                       "100 000 ga boʻlsak 3 km chiqadi. 300 000 km — Yerdan Oygacha "
                       "boʻlgan masofaga yaqin.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>6 ishchi ishni 10 kunda "
                "bajaradi. 5 ishchi necha kunda bajaradi?</strong></p>",
        "choices": [
            "6 × 10 = 60; 60 ÷ 5 = 12 kun",
            "10 ÷ 5 = 2; 2 × 6 = 12 kun boʻlmaydi, javob 2 kun",
            "6/10 = 5/? → ? ≈ 8,3 kun",
            "10 − 1 = 9 kun",
        ],
        "correct": "6 × 10 = 60; 60 ÷ 5 = 12 kun",
        "explanation": "<p><strong>12 kun</strong> toʻgʻri: ish hajmi 60 ishchi-kun, "
                       "uni 5 ishchiga boʻlamiz. Ishchi kamaydi — kun koʻpaydi. "
                       "Proporsiya tuzish (uchinchi variant) bu yerda ishlamaydi, "
                       "chunki bogʻlanish teskari.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Bekzod xaritada Toshkent bilan Samarqand orasini oʻlchadi — 28 "
                "santimetr chiqdi. Xarita masshtabi 1 : 1 000 000.</p>"
                "<p><strong>Ikki shahar orasi necha kilometr?</strong></p>",
        "choices": ["28 km", "180 km", "280 km", "2800 km"],
        "correct": "280 km",
        "explanation": "<p><strong>280 km.</strong> 1 : 1 000 000 masshtabda 1 sm = "
                       "1 000 000 sm = 10 km; 28 × 10 = 280 km. Tekshirish: bu "
                       "haqiqiy yoʻlga ham yaqin.</p>",
    },
    {
        "text": "<p>Mashina 280 kilometrlik yoʻlni 80 km/soat tezlik bilan bosib "
                "oʻtmoqchi edi, lekin tezlikni 70 km/soatga tushirdi.</p>"
                "<p><strong>Yoʻl endi necha soat davom etadi?</strong></p>",
        "choices": ["3 soat", "3,5 soat", "4 soat", "4,5 soat"],
        "correct": "4 soat",
        "explanation": "<p><strong>4 soat.</strong> 280 ÷ 70 = 4. "
                       "<strong>3,5 soat</strong> — 80 km/soat tezlikdagi javob "
                       "(280 ÷ 80). Tezlik kamaydi, demak vaqt ortishi kerak edi — "
                       "bu teskari proporsionallik.</p>",
    },
]


# =====================================================================
# PM-29 — harf: nomaʼlum va oʻzgaruvchi
# =====================================================================

Q_PM29 = [
    # 1–5 tanish
    {
        "text": "<p>Qisqa yozing.</p><p><strong>3 × a = ?</strong></p>",
        "choices": ["3a", "a3", "a + 3", "3/a"],
        "correct": "3a",
        "explanation": "<p><strong>3a.</strong> Koʻpaytirish belgisi tushiriladi va "
                       "son doim harfdan oldin yoziladi. <strong>a3</strong> — "
                       "qoidaga zid yozuv.</p>",
    },
    {
        "text": "<p>Qisqa yozing.</p><p><strong>a × a = ?</strong></p>",
        "choices": ["2a", "a kvadrat", "a + a", "aa qoʻshuv"],
        "correct": "a kvadrat",
        "explanation": "<p><strong>a kvadrat</strong>, yaʼni a ning ikkinchi darajasi. "
                       "Bir xil koʻpaytuvchi ikki marta — daraja (PM-12). "
                       "<strong>2a</strong> esa a + a ga teng, bu boshqa narsa.</p>",
    },
    {
        "text": "<p>Qisqa yozing.</p><p><strong>x ni 2 ga boʻlish</strong></p>",
        "choices": ["2x", "x/2", "2/x", "x − 2"],
        "correct": "x/2",
        "explanation": "<p><strong>x/2.</strong> Boʻlish kasr chizigʻi bilan "
                       "yoziladi, boʻlinuvchi tepada turadi. <strong>2/x</strong> — "
                       "aksincha, 2 ni x ga boʻlish.</p>",
    },
    {
        "text": "<p>Qisqa yozing.</p><p><strong>1 × y = ?</strong></p>",
        "choices": ["y", "1y", "y1", "y + 1"],
        "correct": "y",
        "explanation": "<p><strong>y.</strong> Koeffitsient 1 boʻlsa yozilmaydi — "
                       "1y va y bir xil son.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qiymati oʻzgarib turadigan "
                "miqdor nima deyiladi?</strong></p>",
        "choices": ["Oʻzgaruvchi", "Koeffitsient", "Daraja", "Yigʻindi"],
        "correct": "Oʻzgaruvchi",
        "explanation": "<p><strong>Oʻzgaruvchi.</strong> Qiymati bitta, lekin bizga "
                       "maʼlum boʻlmagan miqdor esa <em>nomaʼlum</em> deyiladi. "
                       "<strong>Koeffitsient</strong> — harf oldidagi son.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Qisqa yozing.</p><p><strong>b × 5 = ?</strong></p>",
        "choices": ["5b", "b5", "b + 5", "b/5"],
        "correct": "5b",
        "explanation": "<p><strong>5b.</strong> Koʻpaytirishda tartib ahamiyatsiz, "
                       "lekin yozuvda son har doim oldinda turadi.</p>",
    },
    {
        "text": "<p>Qisqa yozing.</p><p><strong>a + a + a = ?</strong></p>",
        "choices": ["3a", "a kub", "a + 3", "3 + a"],
        "correct": "3a",
        "explanation": "<p><strong>3a.</strong> Bir xil qoʻshiluvchi uch marta — bu "
                       "koʻpaytirish (PM-3). <strong>a kub</strong> esa a × a × a, "
                       "yaʼni butunlay boshqa narsa.</p>",
    },
    {
        "text": "<p>Qisqa yozing.</p><p><strong>2 × a × b = ?</strong></p>",
        "choices": ["2ab", "2a + b", "ab2", "2(a + b)"],
        "correct": "2ab",
        "explanation": "<p><strong>2ab.</strong> Son oldinda, harflar alifbo tartibida "
                       "va belgilarsiz yoziladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir qutida 12 ta qalam bor, qutilar soni "
                "n ta.</p><p><strong>Jami qalamlar soni qanday yoziladi?</strong></p>",
        "choices": ["12 + n", "12n", "12/n", "n − 12"],
        "correct": "12n",
        "explanation": "<p><strong>12n.</strong> Har qutida 12 tadan, qutilar n ta — "
                       "koʻpaytirish. n = 7 boʻlsa, 12 × 7 = 84 ta qalam.</p>",
    },
    {
        "text": "<p>Qisqa yozing.</p><p><strong>m ta olmaning yarmi</strong></p>",
        "choices": ["2m", "m/2", "m − 2", "m + 2"],
        "correct": "m/2",
        "explanation": "<p><strong>m/2.</strong> Yarim — ikkiga boʻlish. "
                       "<strong>2m</strong> aksincha, miqdorni ikki baravar "
                       "koʻpaytiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>5n ifodasida 5 nima "
                "deyiladi?</strong></p>",
        "choices": ["Koeffitsient", "Daraja", "Oʻzgaruvchi", "Maxraj"],
        "correct": "Koeffitsient",
        "explanation": "<p><strong>Koeffitsient</strong> — harf oldidagi son. n esa "
                       "oʻzgaruvchi. Koeffitsient nechta harf borligini "
                       "koʻrsatadi: 5n — beshta n.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>t — bir kunda oʻqilgan bet "
                "soni.</p><p><strong>Bir haftada oʻqilgan betlar soni qanday "
                "yoziladi?</strong></p>",
        "choices": ["t + 7", "7t", "t/7", "t − 7"],
        "correct": "7t",
        "explanation": "<p><strong>7t.</strong> Haftada 7 kun, har kuni t betdan — "
                       "koʻpaytirish. <strong>t + 7</strong> «yetti bet koʻp» degani "
                       "boʻlar edi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>a = 5.</p>"
                "<p><strong>2a va a·a qiymatlari qanday?</strong></p>",
        "choices": [
            "2a = 10, a·a = 25",
            "2a = 25, a·a = 10",
            "Ikkalasi ham 10",
            "Ikkalasi ham 25",
        ],
        "correct": "2a = 10, a·a = 25",
        "explanation": "<p><strong>2a = 10, a·a = 25.</strong> 2a — a ni ikki marta "
                       "qoʻshish (5 + 5), a·a esa a ning kvadrati (5 × 5). Ular "
                       "faqat a = 2 boʻlgandagina teng boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>a = 4.</p>"
                "<p><strong>3a va a + 3 qiymatlari qanday?</strong></p>",
        "choices": [
            "3a = 12, a + 3 = 7",
            "3a = 7, a + 3 = 12",
            "Ikkalasi ham 12",
            "Ikkalasi ham 7",
        ],
        "correct": "3a = 12, a + 3 = 7",
        "explanation": "<p><strong>3a = 12, a + 3 = 7.</strong> 3a — koʻpaytirish "
                       "(3 × 4), a + 3 — qoʻshish. Yozuvdagi kichik farq javobni "
                       "butunlay oʻzgartiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi yozuv tenglama, ifoda "
                "emas?</strong></p>",
        "choices": ["3a + 5", "12n", "2x = 14", "a/2 − 1"],
        "correct": "2x = 14",
        "explanation": "<p><strong>2x = 14.</strong> Tenglik belgisi bor — demak bu "
                       "tenglama. Qolganlari ifoda: ularni hisoblab boʻlmaydi, chunki "
                       "harfning qiymati berilmagan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Afsona bir necha daftar oldi, "
                "nechtaligini bilmaymiz.»</p><p><strong>Daftarlar soni bu yerda "
                "nima?</strong></p>",
        "choices": [
            "Nomaʼlum — qiymati bitta, lekin bizga aytilmagan",
            "Oʻzgaruvchi — qiymati har safar boshqacha",
            "Koeffitsient",
            "Daraja",
        ],
        "correct": "Nomaʼlum — qiymati bitta, lekin bizga aytilmagan",
        "explanation": "<p><strong>Nomaʼlum.</strong> Afsona aniq bir sondagi daftar "
                       "olgan — u oʻzgarmaydi, faqat biz bilmaymiz. Taksidagi "
                       "kilometr esa har safar boshqacha boʻladi — u oʻzgaruvchi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>a + a = a kvadrat</strong></p>",
        "choices": [
            "Qoʻshish koʻpaytirish bilan adashtirilgan: a + a = 2a",
            "Yigʻindi notoʻgʻri: a + a = a",
            "Daraja notoʻgʻri: a + a = a kub",
            "Hech qayerda — yozuv toʻgʻri",
        ],
        "correct": "Qoʻshish koʻpaytirish bilan adashtirilgan: a + a = 2a",
        "explanation": "<p><strong>a + a = 2a.</strong> Kvadrat — a ni a ga "
                       "koʻpaytirish. Tekshirish: a = 3 boʻlsa, 3 + 3 = 6, kvadrati "
                       "esa 9 — teng emas.</p>",
    },
    {
        "text": "<p>Qaysi yozuv toʻgʻri?</p><p><strong>«k ning uch barobari»</strong></p>",
        "choices": ["k3", "3k", "k + 3", "k/3"],
        "correct": "3k",
        "explanation": "<p><strong>3k.</strong> Barobar — koʻpaytirish, son esa "
                       "harfdan oldin yoziladi. <strong>k/3</strong> «uch marta kam» "
                       "degani boʻlar edi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Sinfdagi har bir oʻquvchi bayramga 5000 soʻmdan qoʻshdi, sinf "
                "rahbari esa yana 20 000 soʻm qoʻshdi. Oʻquvchilar soni n ta.</p>"
                "<p><strong>Yigʻilgan pul qanday yoziladi?</strong></p>",
        "choices": ["5000 + 20 000n", "5000n + 20 000", "25 000n", "5000n − 20 000"],
        "correct": "5000n + 20 000",
        "explanation": "<p><strong>5000n + 20 000.</strong> Oʻquvchilar pulining "
                       "miqdori ularning soniga bogʻliq (5000n), rahbarning ulushi "
                       "esa oʻzgarmaydi. <strong>25 000n</strong> — ikkala summani "
                       "ham n ga koʻpaytirishdan chiqadigan xato.</p>",
    },
    {
        "text": "<p>Bir quti sharbat 9000 soʻm. Jasur k quti sharbat va yana 15 000 "
                "soʻmlik non oldi.</p><p><strong>k = 4 boʻlsa, Jasur qancha "
                "pul sarfladi?</strong></p>",
        "choices": ["36 000 soʻm", "51 000 soʻm", "60 000 soʻm", "96 000 soʻm"],
        "correct": "51 000 soʻm",
        "explanation": "<p><strong>51 000 soʻm.</strong> Xarajat 9000k + 15 000; "
                       "k = 4 boʻlsa 9000 × 4 = 36 000, ustiga non 15 000 — jami "
                       "51 000. <strong>36 000</strong> — faqat sharbatlarning "
                       "puli.</p>",
    },
]


# =====================================================================
# PM-30 — matndan ifoda tuzish
# =====================================================================

Q_PM30 = [
    # 1–5 tanish
    {
        "text": "<p>Ifoda tuzing.</p><p><strong>«a dan 5 ta koʻp»</strong></p>",
        "choices": ["a + 5", "a − 5", "5a", "a/5"],
        "correct": "a + 5",
        "explanation": "<p><strong>a + 5.</strong> Gapda «marta» soʻzi yoʻq, demak "
                       "qoʻshish. <strong>5a</strong> «besh marta koʻp» degani boʻlar "
                       "edi.</p>",
    },
    {
        "text": "<p>Ifoda tuzing.</p><p><strong>«a dan 5 ta kam»</strong></p>",
        "choices": ["a + 5", "a − 5", "5 − a", "a/5"],
        "correct": "a − 5",
        "explanation": "<p><strong>a − 5.</strong> «…dan» qoʻshimchasi kamayuvchini "
                       "koʻrsatadi: ayirish a dan boshlanadi. <strong>5 − a</strong> "
                       "boshqa son.</p>",
    },
    {
        "text": "<p>Ifoda tuzing.</p><p><strong>«a dan 3 marta koʻp»</strong></p>",
        "choices": ["a + 3", "a − 3", "3a", "a/3"],
        "correct": "3a",
        "explanation": "<p><strong>3a.</strong> «Marta» soʻzi koʻpaytirishni "
                       "bildiradi. Tekshirish: a = 10 boʻlsa, «uch marta koʻp» 30 "
                       "boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Ifoda tuzing.</p><p><strong>«a ning yarmi»</strong></p>",
        "choices": ["2a", "a/2", "a − 2", "a + 2"],
        "correct": "a/2",
        "explanation": "<p><strong>a/2.</strong> Yarim — ikkiga boʻlish.</p>",
    },
    {
        "text": "<p>Ifoda tuzing.</p><p><strong>«a va b sonlarining "
                "yigʻindisi»</strong></p>",
        "choices": ["a + b", "ab", "a − b", "a/b"],
        "correct": "a + b",
        "explanation": "<p><strong>a + b.</strong> Yigʻindi — qoʻshish natijasi. "
                       "<strong>ab</strong> esa koʻpaytma boʻlar edi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Ifoda tuzing.</p><p><strong>«a va b yigʻindisining 3 "
                "barobari»</strong></p>",
        "choices": ["3a + b", "3(a + b)", "a + 3b", "3ab"],
        "correct": "3(a + b)",
        "explanation": "<p><strong>3(a + b).</strong> Uch barobar butun yigʻindiga "
                       "tegishli, shuning uchun qavs kerak. Tekshirish: a = 1, b = 2 "
                       "boʻlsa toʻgʻri javob 9, <strong>3a + b</strong> esa 5 "
                       "beradi.</p>",
    },
    {
        "text": "<p>Ifoda tuzing.</p><p><strong>«a ning 3 barobariga 5 "
                "qoʻshildi»</strong></p>",
        "choices": ["3(a + 5)", "3a + 5", "a + 15", "5(a + 3)"],
        "correct": "3a + 5",
        "explanation": "<p><strong>3a + 5.</strong> Bu yerda avval koʻpaytirish, keyin "
                       "qoʻshish — qavs kerak emas. <strong>3(a + 5)</strong> "
                       "«a bilan 5 ning yigʻindisi uch barobar» degani boʻlar edi.</p>",
    },
    {
        "text": "<p>Ifoda tuzing.</p><p><strong>«5 dan a ni ayirish»</strong></p>",
        "choices": ["a − 5", "5 − a", "5a", "a/5"],
        "correct": "5 − a",
        "explanation": "<p><strong>5 − a.</strong> Ayirish beshdan boshlanadi, demak "
                       "5 birinchi turadi. a = 8 boʻlsa javob −3 chiqadi — bu ham "
                       "toʻgʻri son (PM-9).</p>",
    },
    {
        "text": "<p>Ifoda tuzing.</p><p><strong>«a ning uchdan biri»</strong></p>",
        "choices": ["3a", "a/3", "a − 3", "a + 1/3"],
        "correct": "a/3",
        "explanation": "<p><strong>a/3.</strong> Uchdan bir — uchga boʻlish, xuddi "
                       "«uch marta kam» kabi.</p>",
    },
    {
        "text": "<p>Ifoda tuzing.</p><p>Taksi: oʻtirish uchun 8000 soʻm, har kilometr "
                "uchun 3000 soʻm. Bosib oʻtilgan yoʻl k kilometr.</p>"
                "<p><strong>Yoʻl narxi qanday yoziladi?</strong></p>",
        "choices": ["8000k + 3000", "8000 + 3000k", "11 000k", "3000(k + 8000)"],
        "correct": "8000 + 3000k",
        "explanation": "<p><strong>8000 + 3000k.</strong> 8000 bir marta olinadi va "
                       "kilometrga bogʻliq emas; 3000 esa har kilometr uchun. "
                       "<strong>11 000k</strong> — ikki sonni qoʻshib yuborishdan "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Ifoda tuzing.</p><p>Har biri a soʻmdan 4 ta daftar va 2000 "
                "soʻmlik ruchka olindi.</p><p><strong>Jami xarajat qanday "
                "yoziladi?</strong></p>",
        "choices": ["4a + 2000", "4(a + 2000)", "a + 2000", "2000a + 4"],
        "correct": "4a + 2000",
        "explanation": "<p><strong>4a + 2000.</strong> Toʻrtta daftar — 4a, ruchka "
                       "esa bitta va uning narxi aniq. <strong>4(a + 2000)</strong> "
                       "toʻrtta ruchka olingandek boʻlar edi.</p>",
    },
    {
        "text": "<p>Ifoda tuzing.</p><p><strong>«b ning kvadratidan 1 ni "
                "ayirish»</strong></p>",
        "choices": ["b·b − 1", "(b − 1)·(b − 1)", "b − 1", "2b − 1"],
        "correct": "b·b − 1",
        "explanation": "<p><strong>b·b − 1</strong>, yaʼni b kvadrat minus bir. Avval "
                       "daraja, keyin ayirish — amallar tartibi (PM-5). "
                       "<strong>2b − 1</strong> — kvadratni ikkiga koʻpaytirish deb "
                       "oʻqishdan chiqadi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>a = 10.</p>"
                "<p><strong>«a dan 5 ta koʻp» va «a dan 5 marta koʻp» qanday "
                "farq qiladi?</strong></p>",
        "choices": ["15 va 50", "50 va 15", "15 va 15", "50 va 50"],
        "correct": "15 va 50",
        "explanation": "<p><strong>15 va 50.</strong> «5 ta koʻp» — a + 5 = 15; "
                       "«5 marta koʻp» — 5a = 50. Bitta soʻz javobni 35 taga "
                       "oʻzgartirdi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>a = 3.</p>"
                "<p><strong>a − 7 va 7 − a qiymatlari qanday?</strong></p>",
        "choices": ["−4 va 4", "4 va −4", "Ikkalasi ham 4", "Ikkalasi ham −4"],
        "correct": "−4 va 4",
        "explanation": "<p><strong>−4 va 4.</strong> a − 7 = 3 − 7 = −4; "
                       "7 − a = 7 − 3 = 4. Ayirishda tartib almashsa, ishora ham "
                       "almashadi (PM-10).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>a = 4.</p>"
                "<p><strong>3(a + 2) va 3a + 2 qiymatlari qanday?</strong></p>",
        "choices": ["18 va 14", "14 va 18", "Ikkalasi ham 18", "Ikkalasi ham 14"],
        "correct": "18 va 14",
        "explanation": "<p><strong>18 va 14.</strong> Qavs avval bajariladi: "
                       "3 × 6 = 18. Qavssiz esa avval koʻpaytirish: 12 + 2 = 14. "
                       "Qavs — «avval shuni bajar» degan buyruq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«a va b yigʻindisining "
                "yarmi» qaysi ifoda?</strong></p>",
        "choices": ["a + b/2", "(a + b)/2", "a/2 + b", "2(a + b)"],
        "correct": "(a + b)/2",
        "explanation": "<p><strong>(a + b)/2.</strong> Yarim butun yigʻindiga "
                       "tegishli, shuning uchun yigʻindi qavsga olinadi. "
                       "<strong>a + b/2</strong> — faqat b ning yarmi olinadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>«x dan 4 marta koʻp» → "
                "x + 4</strong></p>",
        "choices": [
            "«Marta» koʻpaytirishni bildiradi: 4x boʻlishi kerak",
            "Ayirish kerak edi: x − 4",
            "Boʻlish kerak edi: x/4",
            "Hech qayerda — ifoda toʻgʻri",
        ],
        "correct": "«Marta» koʻpaytirishni bildiradi: 4x boʻlishi kerak",
        "explanation": "<p><strong>4x boʻlishi kerak.</strong> «Marta», «barobar», "
                       "«baravar» soʻzlari koʻpaytirishni bildiradi. Tekshirish: "
                       "x = 10 boʻlsa, javob 40 boʻlishi kerak, 14 emas.</p>",
    },
    {
        "text": "<p>Qaysi ifoda toʻgʻri?</p><p><strong>«a va 3 ning yigʻindisi 5 "
                "barobar orttirildi»</strong></p>",
        "choices": ["5a + 3", "a + 15", "5(a + 3)", "5a + 15a"],
        "correct": "5(a + 3)",
        "explanation": "<p><strong>5(a + 3).</strong> Orttirilayotgani — butun "
                       "yigʻindi, shuning uchun u qavsga olinadi. Tekshirish: a = 2 "
                       "boʻlsa toʻgʻri javob 25, <strong>5a + 3</strong> esa 13 "
                       "beradi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Taksi: oʻtirganingiz uchun 8000 soʻm, keyin har kilometr uchun "
                "3000 soʻm.</p><p><strong>6 kilometrlik yoʻl qancha turadi?</strong></p>",
        "choices": ["18 000 soʻm", "24 000 soʻm", "26 000 soʻm", "66 000 soʻm"],
        "correct": "26 000 soʻm",
        "explanation": "<p><strong>26 000 soʻm.</strong> Narx 8000 + 3000k; k = 6 "
                       "boʻlsa 8000 + 18 000 = 26 000. <strong>18 000</strong> — "
                       "oʻtirish haqi unutilgan javob; <strong>66 000</strong> — "
                       "8000 ni ham 6 ga koʻpaytirishdan chiqadi.</p>",
    },
    {
        "text": "<p>Telefon tarifi: oyiga 25 000 soʻm abonent toʻlovi va har bir "
                "gigabayt uchun 5000 soʻm.</p><p><strong>8 gigabayt ishlatilsa, "
                "oylik toʻlov qancha?</strong></p>",
        "choices": ["40 000 soʻm", "60 000 soʻm", "65 000 soʻm", "240 000 soʻm"],
        "correct": "65 000 soʻm",
        "explanation": "<p><strong>65 000 soʻm.</strong> Toʻlov 25 000 + 5000g; "
                       "g = 8 boʻlsa 25 000 + 40 000 = 65 000. "
                       "<strong>40 000</strong> — abonent toʻlovi hisobga "
                       "olinmagan.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-28 Mashq: Proporsiya va masshtab",
        "description": "20 savol — proporsiyaning asosiy xossasi, «bir birlik» "
                       "usuli, masshtabni kilometrga aylantirish va teskari "
                       "proporsionallik.",
        "tutorial":    "PM-28:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM28,
    },
    {
        "title":       "PM-29 Mashq: Nomaʼlum va oʻzgaruvchi",
        "description": "20 savol — algebraik yozuv qoidalari (3a, ab, a/2), "
                       "nomaʼlum bilan oʻzgaruvchining farqi va sodda ifodalar.",
        "tutorial":    "PM-29:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM29,
    },
    {
        "title":       "PM-30 Mashq: Matndan ifoda tuzish",
        "description": "20 savol — soʻzni belgiga aylantirish, «marta» va «ta» "
                       "farqi, ayirishdagi tartib va qavs qachon kerakligi.",
        "tutorial":    "PM-30:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM30,
    },
]
