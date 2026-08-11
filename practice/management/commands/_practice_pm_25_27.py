# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-25 … PM-27 (foiz oʻzgarishi, bozor matematikasi, nisbat).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

⚠️ `text` |safe bilan chiqadi (HTML mumkin), `choices` esa ekranlanadi —
   u yerda HTML teg yoʻq; oʻnlik kasrlar vergul bilan «0,85», nisbatlar
   «3 : 4» koʻrinishida yoziladi.
⚠️ Kumulyativ: proporsiya va masshtab (PM-28) hali yoʻq; nisbat masalalari
   «bir qism» usuli bilan yechiladi, tenglama (PM-36) bilan emas.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_25_27.py --master=prime \\
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
# PM-25 — foiz oʻzgarishi
# =====================================================================

Q_PM25 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>100 dan 120 ga oshdi. Necha "
                "foizga?</strong></p>",
        "choices": ["12%", "20%", "25%", "120%"],
        "correct": "20%",
        "explanation": "<p><strong>20%.</strong> Oʻzgarish 20; uni ESKI qiymatga "
                       "boʻlamiz: 20 ÷ 100 = 0,2 = 20%. Butun aynan 100 boʻlganda "
                       "oʻzgarish va foiz bir xil son chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>50 dan 40 ga tushdi. Necha "
                "foizga?</strong></p>",
        "choices": ["10%", "20%", "25%", "40%"],
        "correct": "20%",
        "explanation": "<p><strong>20%.</strong> Oʻzgarish 10; asos — eski qiymat 50: "
                       "10 ÷ 50 = 0,2. <strong>25%</strong> — yangi qiymatga "
                       "(10 ÷ 40) boʻlishdan chiqadigan eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>200 ni 10 foizga oshiring.</strong></p>",
        "choices": ["20", "180", "210", "220"],
        "correct": "220",
        "explanation": "<p><strong>220.</strong> 200 × 1,1 = 220. <strong>20</strong> — "
                       "faqat qoʻshimchaning oʻzi, yangi qiymat emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>300 ni 10 foizga kamaytiring.</strong></p>",
        "choices": ["30", "270", "290", "330"],
        "correct": "270",
        "explanation": "<p><strong>270.</strong> 300 × 0,9 = 270. Yoki 300 − 30. "
                       "<strong>330</strong> — kamaytirish oʻrniga oshirishdan "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>20 foizga oshirish qaysi "
                "koʻpaytuvchiga teng?</strong></p>",
        "choices": ["0,2", "0,8", "1,2", "20"],
        "correct": "1,2",
        "explanation": "<p><strong>1,2.</strong> Eski qiymat — 100%, unga 20% "
                       "qoʻshilsa 120% boʻladi, yaʼni 1,2. <strong>0,8</strong> — "
                       "aksincha, 20 foizga kamaytirish koʻpaytuvchisi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p>Non 4000 soʻm edi, 5000 soʻm boʻldi.</p>"
                "<p><strong>Narx necha foizga oshdi?</strong></p>",
        "choices": ["10%", "20%", "25%", "50%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> Oʻzgarish 1000 soʻm; asos — eski narx "
                       "4000: 1000 ÷ 4000 = 0,25. <strong>20%</strong> — yangi narxga "
                       "(1000 ÷ 5000) boʻlishdan chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Telefon 3 000 000 soʻmdan 2 400 000 soʻmga "
                "tushdi.</p><p><strong>Necha foizga arzonlashdi?</strong></p>",
        "choices": ["6%", "20%", "25%", "60%"],
        "correct": "20%",
        "explanation": "<p><strong>20%.</strong> Oʻzgarish 600 000; "
                       "600 000 ÷ 3 000 000 = 0,2. <strong>25%</strong> — yangi narxga "
                       "boʻlganda chiqadi (600 000 ÷ 2 400 000).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>800 000 ni 15 foizga oshiring.</strong></p>",
        "choices": ["120 000", "680 000", "815 000", "920 000"],
        "correct": "920 000",
        "explanation": "<p><strong>920 000.</strong> 800 000 × 1,15 = 920 000. Yoki "
                       "800 000 + 120 000. <strong>120 000</strong> — qoʻshimchaning "
                       "oʻzi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>60 000 ni 20 foizga "
                "kamaytiring.</strong></p>",
        "choices": ["12 000", "40 000", "48 000", "72 000"],
        "correct": "48 000",
        "explanation": "<p><strong>48 000.</strong> 60 000 × 0,8 = 48 000. "
                       "<strong>12 000</strong> — kamayishning oʻzi, qolgan qiymat "
                       "emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Oylik 2 000 000 soʻmdan 2 300 000 soʻmga "
                "koʻtarildi.</p><p><strong>Necha foizga oshdi?</strong></p>",
        "choices": ["3%", "13%", "15%", "30%"],
        "correct": "15%",
        "explanation": "<p><strong>15%.</strong> Oʻzgarish 300 000; "
                       "300 000 ÷ 2 000 000 = 0,15. Tekshirish: "
                       "2 000 000 × 1,15 = 2 300 000.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>25 foizga kamaytirish qaysi "
                "koʻpaytuvchiga teng?</strong></p>",
        "choices": ["0,25", "0,75", "1,25", "4"],
        "correct": "0,75",
        "explanation": "<p><strong>0,75.</strong> Qolgan qism 100 − 25 = 75%, yaʼni "
                       "0,75. <strong>0,25</strong> — kamayishning oʻzini beradi, "
                       "qolgan qiymatni emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>150 ni 8 foizga oshiring.</strong></p>",
        "choices": ["12", "138", "158", "162"],
        "correct": "162",
        "explanation": "<p><strong>162.</strong> 150 × 1,08 = 162. Yoki 1% = 1,5, "
                       "8% = 12, keyin 150 + 12.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Hisoblang.</p><p>Narx 100 000 soʻm edi. Avval 20 foizga oshdi, "
                "keyin 20 foizga tushdi.</p><p><strong>Hozir narx qancha?</strong></p>",
        "choices": ["96 000 soʻm", "100 000 soʻm", "104 000 soʻm", "120 000 soʻm"],
        "correct": "96 000 soʻm",
        "explanation": "<p><strong>96 000 soʻm.</strong> 100 000 × 1,2 = 120 000, "
                       "keyin 120 000 × 0,8 = 96 000. Ikkinchi 20% kattaroq sondan "
                       "olindi, shuning uchun eski narx qaytmaydi. Koʻpaytuvchilar "
                       "bilan: 1,2 × 0,8 = 0,96.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Narx 30 foizga oshdi, keyin 30 "
                "foizga tushdi.</p><p><strong>Yakuniy narx eski narxga nisbatan "
                "qanday?</strong></p>",
        "choices": [
            "9 foizga arzon",
            "9 foizga qimmat",
            "Aynan eski narxga teng",
            "30 foizga arzon",
        ],
        "correct": "9 foizga arzon",
        "explanation": "<p><strong>9 foizga arzon.</strong> 1,3 × 0,7 = 0,91, yaʼni "
                       "yakuniy narx eskining 91 foizi. Foizlarni qoʻshib yoki ayirib "
                       "boʻlmaydi — koʻpaytuvchilar koʻpaytiriladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Bank stavkasi 10 foizdan 12 foizga "
                "koʻtarildi.</p><p><strong>Stavkaning oʻzi necha foizga "
                "oshdi?</strong></p>",
        "choices": ["2%", "12%", "20%", "22%"],
        "correct": "20%",
        "explanation": "<p><strong>20%.</strong> Oʻzgarish 2 punkt; uni eski stavkaga "
                       "boʻlamiz: 2 ÷ 10 = 0,2 = 20%. <strong>2%</strong> — bu foiz "
                       "<em>punkti</em>, foiz oʻzgarishi emas: ikkalasi bir xil "
                       "narsa emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>40 000 dan 50 000 ga oshdi. Necha "
                "foizga?</strong></p>",
        "choices": ["10%", "20%", "25%", "80%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> 10 000 ÷ 40 000 = 0,25. "
                       "<strong>20%</strong> — yangi narxni asos qilib olishdan "
                       "chiqadi (10 000 ÷ 50 000). Asos har doim ESKI qiymat.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>80 dan 100 ga oshdi: "
                "20 ÷ 100 = 20% oshgan</strong></p>",
        "choices": [
            "Asos notoʻgʻri: 20 ÷ 80 = 25% boʻlishi kerak",
            "Oʻzgarish notoʻgʻri: 100 − 80 = 30",
            "100 ga koʻpaytirish ortiqcha",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Asos notoʻgʻri: 20 ÷ 80 = 25% boʻlishi kerak",
        "explanation": "<p><strong>Asos notoʻgʻri tanlangan.</strong> Oʻsish 80 dan "
                       "boshlandi, demak boʻluvchi ham 80: 20 ÷ 80 = 0,25 = 25%. "
                       "Tekshirish: 80 × 1,25 = 100 ✓</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>500 ni 30 foizga "
                "kamaytirish</strong></p>",
        "choices": [
            "500 × 0,3 = 150",
            "500 × 0,7 = 350",
            "500 × 1,3 = 650",
            "500 ÷ 0,3 ≈ 1667",
        ],
        "correct": "500 × 0,7 = 350",
        "explanation": "<p><strong>350</strong> toʻgʻri: qolgan qism 70%, yaʼni 0,7. "
                       "<strong>150</strong> — kamayishning oʻzi (uni 500 dan ayirish "
                       "kerak edi), <strong>650</strong> esa kamaytirish oʻrniga "
                       "oshirish.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Bir yil oldin non 4000 soʻm edi. Bugun uning narxi 5000 "
                "soʻm.</p><p><strong>Non necha foizga qimmatlashdi?</strong></p>",
        "choices": ["20 foizga", "25 foizga", "50 foizga", "125 foizga"],
        "correct": "25 foizga",
        "explanation": "<p><strong>25 foizga.</strong> Oʻzgarish 1000 soʻm, asos esa "
                       "eski narx 4000 soʻm: 1000 ÷ 4000 = 0,25. Tekshirish: "
                       "4000 × 1,25 = 5000 ✓ <strong>20 foiz</strong> — yangi narxni "
                       "asos qilib olgan javob.</p>",
    },
    {
        "text": "<p>Afsonaning oyligi 1 500 000 soʻm edi. Yangi yildan boshlab oylik "
                "12 foizga oshirildi.</p><p><strong>Afsona endi qancha "
                "oladi?</strong></p>",
        "choices": ["180 000 soʻm", "1 320 000 soʻm", "1 512 000 soʻm",
                    "1 680 000 soʻm"],
        "correct": "1 680 000 soʻm",
        "explanation": "<p><strong>1 680 000 soʻm.</strong> 1 500 000 × 1,12 = "
                       "1 680 000. Yoki 1% = 15 000, 12% = 180 000, keyin "
                       "1 500 000 + 180 000. <strong>180 000</strong> — faqat "
                       "qoʻshimchaning oʻzi.</p>",
    },
]


# =====================================================================
# PM-26 — chegirma, ustama va soliq
# =====================================================================

Q_PM26 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p>100 000 soʻmlik mahsulotga 10 foiz "
                "chegirma.</p><p><strong>Qancha toʻlanadi?</strong></p>",
        "choices": ["10 000 soʻm", "90 000 soʻm", "99 000 soʻm", "110 000 soʻm"],
        "correct": "90 000 soʻm",
        "explanation": "<p><strong>90 000 soʻm.</strong> 100 000 × 0,9 = 90 000. "
                       "<strong>10 000</strong> — chegirmaning oʻzi, toʻlov emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>200 000 soʻmlik mahsulotga 25 foiz "
                "chegirma.</p><p><strong>Qancha toʻlanadi?</strong></p>",
        "choices": ["50 000 soʻm", "150 000 soʻm", "175 000 soʻm", "250 000 soʻm"],
        "correct": "150 000 soʻm",
        "explanation": "<p><strong>150 000 soʻm.</strong> 200 000 × 0,75 = 150 000. "
                       "Chegirma 50 000 soʻm boʻldi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>50 000 soʻmlik xizmatga 12 foiz QQS "
                "qoʻshiladi.</p><p><strong>Chek qancha boʻladi?</strong></p>",
        "choices": ["6000 soʻm", "44 000 soʻm", "50 120 soʻm", "56 000 soʻm"],
        "correct": "56 000 soʻm",
        "explanation": "<p><strong>56 000 soʻm.</strong> 50 000 × 1,12 = 56 000. "
                       "Soliq narxning ustiga qoʻshiladi, undan ayirilmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Tannarx 40 000 soʻm, ustama 50 "
                "foiz.</p><p><strong>Sotuv narxi qancha?</strong></p>",
        "choices": ["20 000 soʻm", "45 000 soʻm", "60 000 soʻm", "80 000 soʻm"],
        "correct": "60 000 soʻm",
        "explanation": "<p><strong>60 000 soʻm.</strong> 40 000 × 1,5 = 60 000. "
                       "<strong>20 000</strong> — ustamaning oʻzi; sotuv narxi "
                       "tannarx plyus ustama.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>20 foiz chegirma qaysi "
                "koʻpaytuvchiga teng?</strong></p>",
        "choices": ["0,2", "0,8", "1,2", "1,8"],
        "correct": "0,8",
        "explanation": "<p><strong>0,8.</strong> Chegirmadan keyin narxning 80 foizi "
                       "toʻlanadi. <strong>0,2</strong> chegirmaning oʻzini beradi, "
                       "toʻlovni emas.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p>320 000 soʻmlik kurtkaga 15 foiz "
                "chegirma.</p><p><strong>Qancha toʻlanadi?</strong></p>",
        "choices": ["48 000 soʻm", "272 000 soʻm", "305 000 soʻm", "368 000 soʻm"],
        "correct": "272 000 soʻm",
        "explanation": "<p><strong>272 000 soʻm.</strong> 320 000 × 0,85 = 272 000. "
                       "Chegirma 48 000 soʻm — u javob emas, savol toʻlovni "
                       "soʻragan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>250 000 soʻmlik mahsulotga 12 foiz QQS "
                "qoʻshiladi.</p><p><strong>Chek qancha boʻladi?</strong></p>",
        "choices": ["30 000 soʻm", "220 000 soʻm", "262 000 soʻm", "280 000 soʻm"],
        "correct": "280 000 soʻm",
        "explanation": "<p><strong>280 000 soʻm.</strong> 250 000 × 1,12 = 280 000. "
                       "Soliqning oʻzi 30 000 soʻm.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Tannarx 60 000 soʻm, ustama 30 "
                "foiz.</p><p><strong>Sotuv narxi qancha?</strong></p>",
        "choices": ["18 000 soʻm", "42 000 soʻm", "63 000 soʻm", "78 000 soʻm"],
        "correct": "78 000 soʻm",
        "explanation": "<p><strong>78 000 soʻm.</strong> 60 000 × 1,3 = 78 000. "
                       "<strong>42 000</strong> — ustama oʻrniga chegirma "
                       "qilinganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>80 000 soʻmlik mahsulot 25 foiz chegirma bilan "
                "sotildi.</p><p><strong>Xaridor qancha toʻladi?</strong></p>",
        "choices": ["20 000 soʻm", "55 000 soʻm", "60 000 soʻm", "75 000 soʻm"],
        "correct": "60 000 soʻm",
        "explanation": "<p><strong>60 000 soʻm.</strong> 80 000 × 0,75 = 60 000. "
                       "Chegirma 20 000 soʻm boʻldi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>45 000 soʻmlik mahsulotga 10 foiz "
                "chegirma.</p><p><strong>Sotuvchi qancha pul oldi?</strong></p>",
        "choices": ["4500 soʻm", "40 500 soʻm", "44 000 soʻm", "49 500 soʻm"],
        "correct": "40 500 soʻm",
        "explanation": "<p><strong>40 500 soʻm.</strong> 45 000 × 0,9 = 40 500. "
                       "<strong>49 500</strong> — chegirma oʻrniga ustama "
                       "qoʻshilganda chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Xaridor 10 foiz chegirma bilan 36 000 soʻm "
                "toʻladi.</p><p><strong>Chegirmasiz narx qancha edi?</strong></p>",
        "choices": ["32 400 soʻm", "39 600 soʻm", "40 000 soʻm", "46 000 soʻm"],
        "correct": "40 000 soʻm",
        "explanation": "<p><strong>40 000 soʻm.</strong> Toʻlangan pul — eski narxning "
                       "90 foizi, demak 36 000 ÷ 0,9 = 40 000. Tekshirish: "
                       "40 000 × 0,9 = 36 000 ✓ <strong>39 600</strong> — 36 000 ga "
                       "10 foiz qoʻshishdan chiqadi, lekin chegirma kichikroq sondan "
                       "hisoblanmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>1 200 000 soʻmlik mebelga 5 foiz "
                "chegirma.</p><p><strong>Qancha toʻlanadi?</strong></p>",
        "choices": ["60 000 soʻm", "1 140 000 soʻm", "1 195 000 soʻm",
                    "1 260 000 soʻm"],
        "correct": "1 140 000 soʻm",
        "explanation": "<p><strong>1 140 000 soʻm.</strong> 1 200 000 × 0,95 = "
                       "1 140 000. Chegirma 60 000 soʻm.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Hisoblang.</p><p>Doʻkon avval 20 foiz, kassada yana 10 foiz "
                "chegirma beryapti.</p><p><strong>Jami necha foiz chegirma "
                "boʻladi?</strong></p>",
        "choices": ["18%", "28%", "30%", "72%"],
        "correct": "28%",
        "explanation": "<p><strong>28%.</strong> 0,8 × 0,9 = 0,72, yaʼni narxning 72 "
                       "foizi toʻlanadi; chegirma 100 − 72 = 28%. "
                       "<strong>30%</strong> — foizlarni qoʻshib yuborishdan "
                       "chiqadigan eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>90 000 soʻmlik mahsulotga 20 foiz "
                "chegirma.</p><p><strong>CHEGIRMA necha soʻm?</strong></p>",
        "choices": ["9000 soʻm", "18 000 soʻm", "72 000 soʻm", "108 000 soʻm"],
        "correct": "18 000 soʻm",
        "explanation": "<p><strong>18 000 soʻm.</strong> 90 000 × 0,2 = 18 000. "
                       "<strong>72 000</strong> — toʻlanadigan pul; savol "
                       "chegirmaning oʻzini soʻragan. Ikki savolni ajratib "
                       "oʻqing.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Tannarxi 100 000 soʻm boʻlgan mahsulotga 20 foiz "
                "ustama qoʻyildi, keyin 20 foiz chegirma qilindi.</p>"
                "<p><strong>Yakuniy narx qancha?</strong></p>",
        "choices": ["80 000 soʻm", "96 000 soʻm", "100 000 soʻm", "120 000 soʻm"],
        "correct": "96 000 soʻm",
        "explanation": "<p><strong>96 000 soʻm.</strong> 100 000 × 1,2 = 120 000, "
                       "keyin 120 000 × 0,8 = 96 000. Chegirma kattalashgan narxdan "
                       "olingani uchun natija tannarxdan ham past tushdi — sotuvchi "
                       "zarar koʻrdi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ustama va chegirma qaysi "
                "narxdan hisoblanadi?</strong></p>",
        "choices": [
            "Ustama tannarxdan, chegirma sotuv narxidan",
            "Ustama sotuv narxidan, chegirma tannarxdan",
            "Ikkalasi ham tannarxdan",
            "Ikkalasi ham sotuv narxidan",
        ],
        "correct": "Ustama tannarxdan, chegirma sotuv narxidan",
        "explanation": "<p><strong>Ustama tannarxdan, chegirma sotuv narxidan.</strong> "
                       "Sotuvchi tannarx ustiga foyda qoʻshadi va shu bilan sotuv "
                       "narxini belgilaydi; chegirma esa oʻsha eʼlon qilingan narxdan "
                       "tushiriladi. Asosni adashtirish butun hisobni buzadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>50 000 soʻmga 20 foiz "
                "chegirma: 50 000 × 0,2 = 10 000, demak narx 10 000 soʻm</strong></p>",
        "choices": [
            "10 000 — chegirmaning oʻzi; narx 50 000 − 10 000 = 40 000",
            "Koʻpaytirish oʻrniga boʻlish kerak edi",
            "Chegirma 0,8 ga koʻpaytirib topiladi, demak chegirma 40 000",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "10 000 — chegirmaning oʻzi; narx 50 000 − 10 000 = 40 000",
        "explanation": "<p><strong>Chegirma javob deb olingan.</strong> "
                       "50 000 × 0,2 = 10 000 — bu tushirilgan pul. Toʻlanadigan narx "
                       "esa 40 000 soʻm, yaʼni 50 000 × 0,8. Nazorat: chegirmadan "
                       "keyingi narx eskisidan biroz kichik boʻlishi kerak, besh "
                       "baravar emas.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Tannarxi 80 000 soʻm boʻlgan "
                "mahsulotga 20 foiz ustama</strong></p>",
        "choices": [
            "80 000 × 0,2 = 16 000",
            "80 000 × 0,8 = 64 000",
            "80 000 × 1,2 = 96 000",
            "80 000 ÷ 1,2 ≈ 66 700",
        ],
        "correct": "80 000 × 1,2 = 96 000",
        "explanation": "<p><strong>96 000</strong> toʻgʻri: sotuv narxi tannarxning "
                       "120 foizi. <strong>16 000</strong> — ustamaning oʻzi, "
                       "<strong>64 000</strong> esa ustama oʻrniga chegirma "
                       "qilingan javob. Sotuv narxi tannarxdan kichik boʻlolmaydi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Sherbek 180 000 soʻmlik shimni koʻrdi. Doʻkonda «hamma shimga 25 "
                "foiz chegirma» eʼloni osilgan.</p><p><strong>Sherbek kassada qancha "
                "toʻlaydi?</strong></p>",
        "choices": ["45 000 soʻm", "135 000 soʻm", "155 000 soʻm", "225 000 soʻm"],
        "correct": "135 000 soʻm",
        "explanation": "<p><strong>135 000 soʻm.</strong> Chegirmadan keyin narxning "
                       "75 foizi qoladi: 180 000 × 0,75 = 135 000. "
                       "<strong>45 000</strong> — chegirmaning oʻzi.</p>",
    },
    {
        "text": "<p>Karim aka kurtkani 40 000 soʻmga oladi va ustiga 25 foiz ustama "
                "qoʻyib sotadi. Mavsum oxirida esa oʻsha narxdan 10 foiz chegirma "
                "eʼlon qildi.</p><p><strong>Xaridor necha soʻm toʻlaydi?</strong></p>",
        "choices": ["40 000 soʻm", "45 000 soʻm", "46 000 soʻm", "50 000 soʻm"],
        "correct": "45 000 soʻm",
        "explanation": "<p><strong>45 000 soʻm.</strong> Avval ustama tannarxdan: "
                       "40 000 × 1,25 = 50 000. Keyin chegirma sotuv narxidan: "
                       "50 000 × 0,9 = 45 000. Karim akaning foydasi 5000 soʻm. "
                       "<strong>46 000</strong> — 25 va 10 foizni «15 foiz ustama» "
                       "deb qoʻshib yuborishga oʻxshash xatolardan chiqadi.</p>",
    },
]


# =====================================================================
# PM-27 — nisbat
# =====================================================================

Q_PM27 = [
    # 1–5 tanish
    {
        "text": "<p>Qisqartiring.</p><p><strong>12 : 18 = ?</strong></p>",
        "choices": ["1 : 2", "2 : 3", "3 : 4", "6 : 9"],
        "correct": "2 : 3",
        "explanation": "<p><strong>2 : 3.</strong> Ikkala sonni EKUB 6 ga boʻldik. "
                       "<strong>6 : 9</strong> ham teng nisbat, lekin toʻliq "
                       "qisqartirilmagan — 3 ga yana boʻlinadi.</p>",
    },
    {
        "text": "<p>Qisqartiring.</p><p><strong>15 : 20 = ?</strong></p>",
        "choices": ["2 : 3", "3 : 4", "4 : 5", "5 : 6"],
        "correct": "3 : 4",
        "explanation": "<p><strong>3 : 4.</strong> Ikkalasini 5 ga boʻldik.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>60 ni 1:3 nisbatda "
                "boʻling.</strong></p>",
        "choices": ["10 va 50", "15 va 45", "20 va 40", "30 va 30"],
        "correct": "15 va 45",
        "explanation": "<p><strong>15 va 45.</strong> Qismlar soni 1 + 3 = 4; bir qism "
                       "60 ÷ 4 = 15; ikkinchisi 15 × 3 = 45. Tekshirish: "
                       "15 + 45 = 60 ✓ <strong>20 va 40</strong> — miqdorni 3 ga "
                       "boʻlishdan chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2:3 nisbatda birinchi qism "
                "butunning qanchasi?</strong></p>",
        "choices": ["2/3 qismi", "2/5 qismi", "3/5 qismi", "1/2 qismi"],
        "correct": "2/5 qismi",
        "explanation": "<p><strong>2/5 qismi.</strong> Butun 2 + 3 = 5 ta qismdan "
                       "iborat, birinchisiga ulardan 2 tasi tegadi. "
                       "<strong>2/3</strong> — nisbatni kasr deb oʻqishdan chiqadigan "
                       "eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Qisqartiring.</p><p><strong>10 : 5 = ?</strong></p>",
        "choices": ["1 : 2", "2 : 1", "5 : 1", "10 : 5"],
        "correct": "2 : 1",
        "explanation": "<p><strong>2 : 1.</strong> Ikkalasini 5 ga boʻldik. Tartib "
                       "muhim: <strong>1 : 2</strong> boshqa nisbat — unda birinchi "
                       "miqdor kichik boʻlar edi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Masalani yeching.</p><p><strong>120 ni 2:3 nisbatda "
                "boʻling.</strong></p>",
        "choices": ["24 va 96", "40 va 80", "48 va 72", "60 va 60"],
        "correct": "48 va 72",
        "explanation": "<p><strong>48 va 72.</strong> Qismlar 2 + 3 = 5; bir qism "
                       "120 ÷ 5 = 24; 24 × 2 = 48 va 24 × 3 = 72. Tekshirish: "
                       "48 + 72 = 120 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>84 ni 3:4 nisbatda "
                "boʻling.</strong></p>",
        "choices": ["28 va 56", "36 va 48", "40 va 44", "42 va 42"],
        "correct": "36 va 48",
        "explanation": "<p><strong>36 va 48.</strong> Qismlar 3 + 4 = 7; bir qism "
                       "84 ÷ 7 = 12; 12 × 3 = 36 va 12 × 4 = 48.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sement va qum 1:3 nisbatda "
                "aralashtiriladi.</p><p><strong>24 kg aralashmada necha kg sement "
                "bor?</strong></p>",
        "choices": ["6 kg", "8 kg", "12 kg", "18 kg"],
        "correct": "6 kg",
        "explanation": "<p><strong>6 kg.</strong> Aralashma 1 + 3 = 4 qismdan iborat; "
                       "bir qism 24 ÷ 4 = 6 kg. Sement bir qism — 6 kg, qum uch qism "
                       "— 18 kg. <strong>8 kg</strong> — sementni aralashmaning "
                       "uchdan biri deb olishdan chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>96 ni 3:4:5 nisbatda "
                "boʻling.</strong></p>",
        "choices": ["16, 32, 48", "24, 32, 40", "24, 36, 36", "32, 32, 32"],
        "correct": "24, 32, 40",
        "explanation": "<p><strong>24, 32, 40.</strong> Qismlar 3 + 4 + 5 = 12; bir "
                       "qism 96 ÷ 12 = 8; keyin 8 × 3, 8 × 4 va 8 × 5. Tekshirish: "
                       "24 + 32 + 40 = 96 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Nisbat 5:2 va kichik qism 8 "
                "ta.</p><p><strong>Katta qism nechta?</strong></p>",
        "choices": ["10 ta", "16 ta", "20 ta", "40 ta"],
        "correct": "20 ta",
        "explanation": "<p><strong>20 ta.</strong> Kichik qism 2 ulushga toʻgʻri "
                       "keladi: 8 ÷ 2 = 4 — bitta ulush. Katta qism 5 ulush: "
                       "4 × 5 = 20. <strong>40</strong> — 8 ni toʻgʻridan-toʻgʻri 5 "
                       "ga koʻpaytirishdan chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>350 000 soʻmni 3:4 nisbatda "
                "boʻling.</strong></p>",
        "choices": ["100 000 va 250 000", "150 000 va 200 000",
                    "170 000 va 180 000", "175 000 va 175 000"],
        "correct": "150 000 va 200 000",
        "explanation": "<p><strong>150 000 va 200 000.</strong> Qismlar 3 + 4 = 7; bir "
                       "qism 350 000 ÷ 7 = 50 000; keyin 50 000 × 3 va 50 000 × 4. "
                       "Tekshirish: 150 000 + 200 000 = 350 000 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sinfda oʻgʻillar va qizlar soni 4:5 "
                "nisbatda, jami 27 oʻquvchi bor.</p><p><strong>Nechta oʻgʻil "
                "bola?</strong></p>",
        "choices": ["9 ta", "12 ta", "13 ta", "15 ta"],
        "correct": "12 ta",
        "explanation": "<p><strong>12 ta.</strong> Qismlar 4 + 5 = 9; bir qism "
                       "27 ÷ 9 = 3; oʻgʻillar 3 × 4 = 12, qizlar 3 × 5 = 15. "
                       "Tekshirish: 12 + 15 = 27 ✓</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2:3 nisbatda ikkinchi qism "
                "butunning qanchasi?</strong></p>",
        "choices": ["3/2 qismi", "2/5 qismi", "3/5 qismi", "2/3 qismi"],
        "correct": "3/5 qismi",
        "explanation": "<p><strong>3/5 qismi.</strong> Jami 5 ta qism, ikkinchisiga "
                       "3 tasi tegadi — foizda 60%. Nisbatdagi sonlar bir-biri bilan, "
                       "kasrdagi sonlar esa butun bilan taqqoslanadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Savatda olma va nok 2:3 nisbatda. Olma 20 "
                "ta.</p><p><strong>Nok nechta?</strong></p>",
        "choices": ["10 ta", "13 ta", "30 ta", "50 ta"],
        "correct": "30 ta",
        "explanation": "<p><strong>30 ta.</strong> Olma 2 ulush — 20 ta, demak bir "
                       "ulush 10 ta. Nok 3 ulush: 10 × 3 = 30. <strong>50</strong> — "
                       "20 ni jami qismlar soniga (5) koʻpaytirishdan chiqadi, lekin "
                       "50 — bu butun emas, nok ham emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sement va qum 1:3 "
                "nisbatda.</p><p><strong>Sement aralashmaning necha foizi?</strong></p>",
        "choices": ["25%", "30%", "33%", "75%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> Aralashma 4 qismdan iborat, sement "
                       "bittasi: 1/4 = 0,25 = 25%. <strong>33%</strong> — sementni "
                       "1/3 deb olishdan chiqadi; 1:3 «uchdan bir» degani emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi nisbat 3:2 ga "
                "teng?</strong></p>",
        "choices": ["2 : 3", "5 : 4", "6 : 4", "9 : 4"],
        "correct": "6 : 4",
        "explanation": "<p><strong>6 : 4.</strong> Ikkala sonni 2 ga boʻlsak, 3 : 2 "
                       "chiqadi. <strong>9 : 4</strong> — faqat birinchi sonni "
                       "koʻpaytirishdan chiqadi; teng nisbat uchun ikkala son ham bir "
                       "xil songa koʻpaytiriladi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato qilingan?</p><p><strong>40 ni 3:5 nisbatda boʻlish: "
                "40 ÷ 3 ≈ 13,3 va 40 ÷ 5 = 8</strong></p>",
        "choices": [
            "Avval qismlar soni topilmagan: 3 + 5 = 8, bir qism 5 → 15 va 25",
            "Nisbatni avval qisqartirish kerak edi",
            "Boʻlish oʻrniga koʻpaytirish kerak edi: 40 × 3 va 40 × 5",
            "Hech qayerda — yechim toʻgʻri",
        ],
        "correct": "Avval qismlar soni topilmagan: 3 + 5 = 8, bir qism 5 → 15 va 25",
        "explanation": "<p><strong>Qismlar soni topilmagan.</strong> Miqdor "
                       "nisbatdagi sonlarga alohida boʻlinmaydi. Toʻgʻri yoʻl: "
                       "3 + 5 = 8, 40 ÷ 8 = 5, keyin 5 × 3 = 15 va 5 × 5 = 25. "
                       "Nazorat: 13,3 + 8 = 40 boʻlmaydi, 15 + 25 = 40 esa ✓</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>45 ni 4:5 nisbatda "
                "boʻlish</strong></p>",
        "choices": [
            "45 ÷ 4 va 45 ÷ 5 → 11,25 va 9",
            "45 ÷ 9 = 5 → 20 va 25",
            "45 × 4 va 45 × 5 → 180 va 225",
            "45 ÷ 2 → 22,5 va 22,5",
        ],
        "correct": "45 ÷ 9 = 5 → 20 va 25",
        "explanation": "<p><strong>20 va 25</strong> toʻgʻri: qismlar 4 + 5 = 9, bir "
                       "qism 45 ÷ 9 = 5, keyin 5 × 4 va 5 × 5. Tekshirish: "
                       "20 + 25 = 45 ✓ va 20 : 25 = 4 : 5 ✓</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Afsona 3 soat, Jasur 4 soat, Sherbek 5 soat olma terishdi. Olmani "
                "sotib, jami 96 000 soʻm olishdi va pulni ishlagan vaqtlariga qarab "
                "boʻlishdi.</p><p><strong>Sherbek necha soʻm oldi?</strong></p>",
        "choices": ["24 000 soʻm", "32 000 soʻm", "40 000 soʻm", "48 000 soʻm"],
        "correct": "40 000 soʻm",
        "explanation": "<p><strong>40 000 soʻm.</strong> Vaqtlar nisbati 3:4:5; "
                       "qismlar 3 + 4 + 5 = 12; bir qism 96 000 ÷ 12 = 8000. "
                       "Sherbek 5 qism: 8000 × 5 = 40 000. Afsona 24 000, Jasur "
                       "32 000 oldi; jami 96 000 ✓</p>",
    },
    {
        "text": "<p>Buvijon xamirni un va suvdan 5:2 nisbatda qoradi. Unga jami 700 "
                "gramm aralashma kerak.</p><p><strong>Necha gramm un "
                "olishi kerak?</strong></p>",
        "choices": ["200 gramm", "350 gramm", "500 gramm", "560 gramm"],
        "correct": "500 gramm",
        "explanation": "<p><strong>500 gramm.</strong> Qismlar 5 + 2 = 7; bir qism "
                       "700 ÷ 7 = 100 g; un 5 qism — 500 g, suv 2 qism — 200 g. "
                       "Tekshirish: 500 + 200 = 700 ✓ <strong>200</strong> — suvning "
                       "miqdori.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-25 Mashq: Foiz oʻzgarishi",
        "description": "20 savol — oʻzgarish foizini topish, koʻpaytuvchi bilan "
                       "oshirish-kamaytirish va ketma-ket ikki oʻzgarish.",
        "tutorial":    "PM-25:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM25,
    },
    {
        "title":       "PM-26 Mashq: Chegirma, ustama va soliq",
        "description": "20 savol — chegirmadan keyingi narx, tannarxga ustama, QQS "
                       "va ketma-ket chegirmalar.",
        "tutorial":    "PM-26:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM26,
    },
    {
        "title":       "PM-27 Mashq: Nisbat",
        "description": "20 savol — nisbatni qisqartirish, miqdorni nisbatda boʻlish "
                       "va nisbat bilan kasrni ajratish.",
        "tutorial":    "PM-27:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM27,
    },
]
