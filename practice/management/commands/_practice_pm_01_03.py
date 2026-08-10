# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-1 … PM-3 (sonlar va amallar).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_01_03.py --master=prime \\
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
# PM-1 — razryadlar va raqamning oʻrni
# =====================================================================

Q_PM1 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>6 083 sonida 8 raqami qaysi "
                "razryadda turibdi?</strong></p>",
        "choices": ["Birlik", "Oʻnlik", "Yuzlik", "Minglik"],
        "correct": "Oʻnlik",
        "explanation": "<p><strong>Oʻnlik.</strong> Razryadlarni oʻngdan sanaymiz: "
                       "3 — birlik, 8 — oʻnlik, 0 — yuzlik, 6 — minglik. Demak 8 ning "
                       "qiymati 80 ga teng.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>4 725 sonida 7 raqamining "
                "qiymati qancha?</strong></p>",
        "choices": ["7", "70", "700", "7 000"],
        "correct": "700",
        "explanation": "<p><strong>700.</strong> 7 yuzliklar razryadida turibdi, "
                       "yuzlikning vazni 100: 7 × 100 = 700. Yoyilma yozuvda bu shunday "
                       "koʻrinadi: 4 725 = 4 000 + <strong>700</strong> + 20 + 5.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Matematikada nechta raqam "
                "bor?</strong></p>",
        "choices": ["9 ta", "10 ta", "11 ta", "Cheksiz koʻp"],
        "correct": "10 ta",
        "explanation": "<p><strong>10 ta:</strong> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. "
                       "Raqam — belgi, son esa shu belgilardan yozilgan miqdor. Sonlar "
                       "cheksiz koʻp, lekin ular oʻn xil raqamdan tuziladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>5 042 — necha xonali "
                "son?</strong></p>",
        "choices": ["Uch xonali", "Toʻrt xonali", "Besh xonali", "Olti xonali"],
        "correct": "Toʻrt xonali",
        "explanation": "<p><strong>Toʻrt xonali.</strong> Sondagi raqamlar soni "
                       "sanaladi: 5, 0, 4, 2 — toʻrtta. Ichida nol boʻlishi xonalar "
                       "sonini kamaytirmaydi, chunki nol ham razryadni egallab "
                       "turibdi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>300 + 40 + 6 yoyilmasi qaysi "
                "songa teng?</strong></p>",
        "choices": ["346", "364", "3 406", "30 406"],
        "correct": "346",
        "explanation": "<p><strong>346.</strong> Yuzliklarda 3, oʻnliklarda 4, "
                       "birliklarda 6. Yoyilma yozuvdagi qoʻshiluvchilar tartibi aynan "
                       "razryadlar tartibi bilan bir xil.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Yoyilmasi 5 000 + 40 + 2 "
                "boʻlgan son qaysi?</strong></p>",
        "choices": ["542", "5 042", "5 402", "50 042"],
        "correct": "5 042",
        "explanation": "<p><strong>5 042.</strong> Mingliklarda 5, yuzliklar razryadi "
                       "boʻsh — shuning uchun u yerga <strong>0</strong> yoziladi, — "
                       "oʻnliklarda 4, birliklarda 2. Nolni tashlab yuborsak, 542 "
                       "chiqadi va bu butunlay boshqa son.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>90 300 soni qanday "
                "oʻqiladi?</strong></p>",
        "choices": ["Toʻqson ming uch yuz", "Toʻqqiz ming uch yuz",
                    "Toʻqson uch ming", "Toʻqqiz yuz ming uch yuz"],
        "correct": "Toʻqson ming uch yuz",
        "explanation": "<p><strong>Toʻqson ming uch yuz.</strong> Sonni oʻngdan "
                       "uchtalikka ajratamiz: 90 | 300. Minglar sinfida 90, birliklar "
                       "sinfida 300.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2 350 000 sonida 3 raqami "
                "qaysi razryadda turibdi?</strong></p>",
        "choices": ["Minglik", "Oʻn minglik", "Yuz minglik", "Million"],
        "correct": "Yuz minglik",
        "explanation": "<p><strong>Yuz minglik.</strong> Oʻngdan sanaymiz: uchta nol — "
                       "birlik, oʻnlik, yuzlik; keyin 0 — minglik, 5 — oʻn minglik, "
                       "3 — yuz minglik, 2 — million. Demak 3 ning qiymati "
                       "300 000.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Eng katta toʻrt xonali son "
                "qaysi?</strong></p>",
        "choices": ["9 999", "1 000", "9 000", "10 000"],
        "correct": "9 999",
        "explanation": "<p><strong>9 999.</strong> Toʻrt xonali sonlar 1 000 dan "
                       "9 999 gacha. 10 000 — besh xonali, chunki unda beshta raqam "
                       "bor.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>7 006 sonining yoyilma yozuvi "
                "qaysi?</strong></p>",
        "choices": ["7 000 + 6", "700 + 6", "7 000 + 60", "7 000 + 600"],
        "correct": "7 000 + 6",
        "explanation": "<p><strong>7 000 + 6.</strong> Yuzliklar va oʻnliklar razryadi "
                       "boʻsh, shuning uchun ular yoyilmada qatnashmaydi, yozuvda esa "
                       "ularning oʻrniga nol turadi.</p>",
    },
    {
        "text": "<p>Sonni raqamlar bilan yozing.</p><p><strong>Oʻn toʻrt ming besh "
                "yuz</strong></p>",
        "choices": ["14 500", "1 450", "14 050", "140 500"],
        "correct": "14 500",
        "explanation": "<p><strong>14 500.</strong> Minglar sinfida 14, birliklar "
                       "sinfida 500. Uchtalikka ajratib tekshiring: 14 | 500.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>360 soni 36 dan necha marta "
                "katta?</strong></p>",
        "choices": ["10 marta", "100 marta", "324 marta", "6 marta"],
        "correct": "10 marta",
        "explanation": "<p><strong>10 marta.</strong> Har bir raqam bitta razryad chapga "
                       "surildi, birliklar razryadi esa boʻshab qoldi va u yerga 0 "
                       "yozildi. Razryad chapga bir qadam — vazn 10 marta katta. "
                       "324 — bu 360 − 36, yaʼni <em>nechtaga</em> koʻpligi, "
                       "<em>necha marta</em> emas.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son katta: 7 099 yoki "
                "7 100?</strong></p>",
        "choices": ["7 100", "7 099", "Ular teng", "Taqqoslab boʻlmaydi"],
        "correct": "7 100",
        "explanation": "<p><strong>7 100.</strong> Xonalari teng, shuning uchun chapdan "
                       "solishtiramiz: mingliklar teng (7 = 7), yuzliklarda esa "
                       "1 &gt; 0. Oxiridagi 99 katta koʻrinadi, lekin u faqat oʻnlik "
                       "va birlik razryadlarida turibdi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>999 va 1 000 sonlarini "
                "taqqoslang.</strong></p>",
        # NB: choices render through {{ choice.text }} (autoescaped), so the
        # comparison signs are written literally here, not as HTML entities.
        "choices": ["999 < 1 000", "999 > 1 000", "999 = 1 000",
                    "Avval yaxlitlash kerak"],
        "correct": "999 < 1 000",
        "explanation": "<p><strong>999 &lt; 1 000.</strong> Birinchi qadam — xonalarni "
                       "sanash: 999 uch xonali, 1 000 toʻrt xonali. Koʻproq xonali son "
                       "har doim katta (agar u noldan boshlanmasa).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>305 sonidagi nolni nega "
                "tashlab yuborib boʻlmaydi?</strong></p>",
        "choices": ["Chunki u oʻnliklar razryadi boʻsh ekanini koʻrsatadi",
                    "Chunki nol ham son hisoblanadi",
                    "Chunki shunday qabul qilingan",
                    "Aslida tashlab yuborsa ham boʻladi"],
        "correct": "Chunki u oʻnliklar razryadi boʻsh ekanini koʻrsatadi",
        "explanation": "<p><strong>Chunki u oʻnliklar razryadi boʻsh ekanini "
                       "koʻrsatadi.</strong> Nolni tashlasak, 3 va 5 bir-biriga "
                       "yaqinlashadi va 35 hosil boʻladi — yaʼni 3 yuzliklardan "
                       "oʻnliklarga tushib qoladi. Nol — “bu razryad boʻsh” degan "
                       "belgi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi qatorda sonlar oʻsish "
                "tartibida yozilgan?</strong></p>",
        "choices": ["899 < 1 001 < 1 010", "1 001 < 899 < 1 010",
                    "899 < 1 010 < 1 001", "1 010 < 1 001 < 899"],
        "correct": "899 < 1 001 < 1 010",
        "explanation": "<p><strong>899 &lt; 1 001 &lt; 1 010.</strong> 899 — uch xonali, "
                       "shuning uchun eng kichigi. Qolgan ikkitasi toʻrt xonali: "
                       "mingliklar va yuzliklar teng, oʻnliklarda esa 0 &lt; 1, demak "
                       "1 001 &lt; 1 010.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi yoyilma toʻgʻri?</p><p><strong>4 725 = ?</strong></p>",
        "choices": ["4 000 + 700 + 20 + 5", "4 + 7 + 2 + 5",
                    "4 000 + 70 + 20 + 5", "400 + 70 + 2 + 5"],
        "correct": "4 000 + 700 + 20 + 5",
        "explanation": "<p><strong>4 000 + 700 + 20 + 5.</strong> Har bir raqam oʻz "
                       "razryadining vazniga koʻpaytiriladi. "
                       "<strong>4 + 7 + 2 + 5 = 18</strong> — bu raqamlar yigʻindisi, "
                       "sonning oʻzi emas; eng koʻp uchraydigan xato aynan shu.</p>",
    },
    {
        "text": "<p>Oʻquvchi “yigirma ming”ni <strong>200 00</strong> deb yozdi. "
                "Toʻgʻri yozuv qaysi?</p>",
        "choices": ["20 000", "2 000", "200 000", "200 00 — toʻgʻri yozilgan"],
        "correct": "20 000",
        "explanation": "<p><strong>20 000.</strong> “Yigirma ming” — bu 20 × 1 000, "
                       "yaʼni beshta raqamli son. Boʻshliq faqat oʻqishga yordam beradi "
                       "va u <em>oʻngdan uchtalik</em> qoʻyiladi: 20 | 000.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Sherbek chekka 2 400 000 soʻm deb yozishi kerak edi. Shoshib, bitta "
                "ortiqcha nol qoʻyib yubordi va 24 000 000 soʻm boʻlib qoldi.</p>"
                "<p><strong>Yozilgan summa keragidan necha marta koʻp?</strong></p>",
        "choices": ["10 marta", "100 marta", "2 marta", "1 000 marta"],
        "correct": "10 marta",
        "explanation": "<p><strong>10 marta.</strong> Ortiqcha nol har bir raqamni "
                       "bitta razryad chapga surdi, har bir razryad esa 10 marta "
                       "ogʻirroq. Tekshirish: 2 400 000 × 10 = 24 000 000 ✓. "
                       "Savol <em>necha marta</em> deb soʻralgani muhim — "
                       "<em>nechtaga</em> koʻp deganda ayirish kerak boʻlardi.</p>",
    },
    {
        "text": "<p>Bir qutida 100 ta qalam, bir yashikda esa 10 ta quti bor. Omborda "
                "4 ta yashik, 3 ta quti va yana 7 ta yakka qalam turibdi.</p>"
                "<p><strong>Omborda jami nechta qalam bor?</strong></p>",
        "choices": ["4 307 ta", "4 037 ta", "437 ta", "43 007 ta"],
        "correct": "4 307 ta",
        "explanation": "<p><strong>4 307 ta.</strong> Bir yashik = 10 × 100 = 1 000 "
                       "qalam, demak 4 yashik — 4 000 ta. 3 quti — 300 ta. Yakka "
                       "qalamlar — 7 ta. 4 000 + 300 + 7 = <strong>4 307</strong>. "
                       "Eʼtibor bering: oʻnliklar razryadi boʻsh, shuning uchun u yerda "
                       "0 turibdi.</p>",
    },
]


# =====================================================================
# PM-2 — qoʻshish va ayirish
# =====================================================================

Q_PM2 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>47 + 28 = ?</strong></p>",
        "choices": ["75", "65", "615", "70"],
        "correct": "75",
        "explanation": "<p><strong>75.</strong> Birliklar: 7 + 8 = 15 — 5 ni yozamiz, "
                       "1 oʻnlikni koʻtaramiz. Oʻnliklar: 4 + 2 + 1 = 7. "
                       "<strong>65</strong> — koʻtarilgan oʻnlik unutilganda chiqadigan "
                       "javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>362 + 185 = ?</strong></p>",
        "choices": ["547", "437", "537", "557"],
        "correct": "547",
        "explanation": "<p><strong>547.</strong> Razryadlab: (300 + 100) + (60 + 80) + "
                       "(2 + 5) = 400 + 140 + 7 = 547. Oʻnliklardagi 140 — bu 1 yuzlik "
                       "va 4 oʻnlik, shuning uchun yuzliklarga 1 qoʻshiladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>90 − 45 = ?</strong></p>",
        "choices": ["45", "55", "35", "40"],
        "correct": "45",
        "explanation": "<p><strong>45.</strong> Tekshirish: 45 + 45 = 90 ✓. Ayirishni "
                       "doim qoʻshish bilan tekshiring — bu ikki soniya vaqt oladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>120 + 80 = ?</strong></p>",
        "choices": ["200", "180", "220", "1 100"],
        "correct": "200",
        "explanation": "<p><strong>200.</strong> 20 + 80 = 100, demak 120 + 80 = "
                       "100 + 100 = 200. Oʻnliklar toʻlib, yangi yuzlik hosil "
                       "boʻldi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ayirish natijasi qanday "
                "ataladi?</strong></p>",
        "choices": ["Ayirma", "Yigʻindi", "Koʻpaytma", "Boʻlinma"],
        "correct": "Ayirma",
        "explanation": "<p><strong>Ayirma.</strong> Kamayuvchi − ayiriluvchi = ayirma. "
                       "Yigʻindi — qoʻshish natijasi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Ogʻzaki hisoblang.</p><p><strong>236 + 98 = ?</strong></p>",
        "choices": ["334", "324", "336", "434"],
        "correct": "334",
        "explanation": "<p><strong>334.</strong> 98 ni 100 deb yaxlitlaymiz: "
                       "236 + 100 = 336, keyin ortiqcha qoʻshilgan 2 ni qaytaramiz: "
                       "336 − 2 = 334. <strong>336</strong> — tuzatishni unutganda "
                       "chiqadigan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>500 − 236 = ?</strong></p>",
        "choices": ["264", "336", "274", "364"],
        "correct": "264",
        "explanation": "<p><strong>264.</strong> 500 = 4 yuzlik + 9 oʻnlik + 10 birlik. "
                       "10 − 6 = 4, 9 − 3 = 6, 4 − 2 = 2. <strong>336</strong> — har bir "
                       "ustunda kattadan kichigini ayirib yuborganda chiqadi. "
                       "Tekshirish: 264 + 236 = 500 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>704 − 268 = ?</strong></p>",
        "choices": ["436", "446", "536", "564"],
        "correct": "436",
        "explanation": "<p><strong>436.</strong> Oʻnliklar boʻsh, shuning uchun qarz "
                       "yuzlikdan olinadi: 704 = 6 yuzlik + 9 oʻnlik + 14 birlik. "
                       "14 − 8 = 6, 9 − 6 = 3, 6 − 2 = 4. Tekshirish: "
                       "436 + 268 = 704 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1 250 + 750 = ?</strong></p>",
        "choices": ["2 000", "1 900", "2 100", "1 000"],
        "correct": "2 000",
        "explanation": "<p><strong>2 000.</strong> 250 + 750 = 1 000, unga 1 000 "
                       "qoʻshiladi. Bunday “toʻldiruvchi” juftliklarni (250 va 750, "
                       "300 va 700) koʻrish ogʻzaki hisobni tezlashtiradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>12 400 − 9 850 = ?</strong></p>",
        "choices": ["2 550", "2 450", "2 650", "3 550"],
        "correct": "2 550",
        "explanation": "<p><strong>2 550.</strong> Sanab yetish usuli: 9 850 + 150 = "
                       "10 000, 10 000 + 2 400 = 12 400, demak 150 + 2 400 = 2 550. "
                       "Tekshirish: 9 850 + 2 550 = 12 400 ✓</p>",
    },
    {
        "text": "<p>Ogʻzaki hisoblang.</p><p><strong>199 + 199 = ?</strong></p>",
        "choices": ["398", "388", "400", "298"],
        "correct": "398",
        "explanation": "<p><strong>398.</strong> 200 + 200 = 400, keyin ortiqcha "
                       "qoʻshilgan 1 + 1 = 2 ni ayiramiz: 400 − 2 = 398.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>85 000 − 47 500 = ?</strong></p>",
        "choices": ["37 500", "38 500", "42 500", "47 500"],
        "correct": "37 500",
        "explanation": "<p><strong>37 500.</strong> 47 500 + 2 500 = 50 000, "
                       "50 000 + 35 000 = 85 000, demak ayirma 2 500 + 35 000 = "
                       "37 500. Tekshirish: 37 500 + 47 500 = 85 000 ✓</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ayirma 341 ga, ayiriluvchi "
                "159 ga teng. Kamayuvchi qancha?</strong></p>",
        "choices": ["500", "182", "482", "241"],
        "correct": "500",
        "explanation": "<p><strong>500.</strong> Kamayuvchi = ayirma + ayiriluvchi = "
                       "341 + 159 = 500. <strong>182</strong> — 341 dan 159 ni ayirib "
                       "yuborganda chiqadi, lekin bu yerda ayirish emas, qoʻshish "
                       "kerak.</p>",
    },
    {
        "text": "<p>Qaysi ifoda <strong>63 − 29</strong> ga teng?</p>",
        "choices": ["63 − 30 + 1", "63 − 30 − 1", "63 + 30 − 1", "60 − 30 + 1"],
        "correct": "63 − 30 + 1",
        "explanation": "<p><strong>63 − 30 + 1 = 34.</strong> 29 oʻrniga 30 ni ayirdik, "
                       "yaʼni bittani ortiqcha ayirdik — shuning uchun uni qaytarib "
                       "qoʻshamiz. <strong>63 − 30 − 1 = 32</strong> — tuzatish "
                       "notoʻgʻri tomonga qilingan, bu eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Qaysi yoʻl <strong>198 + 47</strong> ni ogʻzaki hisoblashning toʻgʻri "
                "usuli?</p>",
        "choices": ["200 + 47 − 2", "200 + 47 + 2", "200 + 50 − 2", "190 + 47 + 2"],
        "correct": "200 + 47 − 2",
        "explanation": "<p><strong>200 + 47 − 2 = 245.</strong> 198 ni 200 gacha "
                       "toʻldirish uchun 2 qoʻshdik, demak oxirida shu 2 ni qaytarib "
                       "olamiz. Qoʻshishda yaxlitlash boʻyicha qoida: <em>qoʻshdingmi — "
                       "ayir</em>.</p>",
    },
    {
        "text": "<p>Jasur 12 400 qadam, Dilnoza 9 850 qadam yurdi.</p><p><strong>“Jasur "
                "nechtaga koʻp yurdi?” degan savolga qaysi amal javob "
                "beradi?</strong></p>",
        "choices": ["Ayirish", "Qoʻshish", "Koʻpaytirish", "Boʻlish"],
        "correct": "Ayirish",
        "explanation": "<p><strong>Ayirish.</strong> “Nechtaga koʻp” — farqni soʻrayapti: "
                       "12 400 − 9 850 = 2 550 qadam. Agar savol “<em>necha marta</em> "
                       "koʻp” boʻlganida, boʻlish kerak boʻlardi — bu ikki savol bir xil "
                       "emas.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Oʻquvchi shunday yozdi: <strong>47 + 28 = 65</strong>.</p>"
                "<p><strong>Qayerda xato qilingan?</strong></p>",
        "choices": ["Birliklardagi 15 dan oʻnlik koʻtarilmagan",
                    "Sonlar notoʻgʻri tekislangan",
                    "Qoʻshish oʻrniga ayirish bajarilgan",
                    "Xato yoʻq, javob toʻgʻri"],
        "correct": "Birliklardagi 15 dan oʻnlik koʻtarilmagan",
        "explanation": "<p><strong>Birliklardagi 15 dan oʻnlik koʻtarilmagan.</strong> "
                       "7 + 8 = 15: 5 yoziladi, 1 oʻnlik esa oʻnliklar razryadiga "
                       "koʻtariladi. Oʻsha 1 tashlab ketilgani uchun javob roppa-rosa "
                       "10 taga kam chiqqan. Toʻgʻri javob — 75.</p>",
    },
    {
        "text": "<p>Oʻquvchi ustunda yozib, <strong>245 + 30 = 545</strong> deb "
                "topdi.</p><p><strong>Xatoning sababi nima?</strong></p>",
        "choices": ["30 soni oʻng chekkadan tekislanmagan",
                    "Koʻtarilgan birlik unutilgan",
                    "Qoʻshiluvchilar oʻrni almashtirilgan",
                    "Javob toʻgʻri hisoblangan"],
        "correct": "30 soni oʻng chekkadan tekislanmagan",
        "explanation": "<p><strong>30 soni oʻng chekkadan tekislanmagan.</strong> "
                       "3 raqami oʻnliklar emas, yuzliklar ustiga yozilgan, shuning "
                       "uchun 30 oʻrniga 300 qoʻshilib qolgan. Toʻgʻri javob — "
                       "<strong>275</strong>. Ustunda sonlar doim <em>oʻng "
                       "chekkasidan</em> tekislanadi.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Sinf kassasida 85 000 soʻm bor edi. Bayram uchun 47 500 soʻmga shar "
                "va shirinlik olindi. Ertasi kuni ota-onalar yana 30 000 soʻm "
                "qoʻshdi.</p><p><strong>Kassada qancha pul qoldi?</strong></p>",
        "choices": ["67 500 soʻm", "37 500 soʻm", "107 500 soʻm", "62 500 soʻm"],
        "correct": "67 500 soʻm",
        "explanation": "<p><strong>67 500 soʻm.</strong> Amallar hodisalar tartibida "
                       "bajariladi: 85 000 − 47 500 = 37 500, soʻng "
                       "37 500 + 30 000 = 67 500. <strong>37 500</strong> — ikkinchi "
                       "qadamni unutgan javob.</p>",
    },
    {
        "text": "<p>Karim aka bozorga 200 000 soʻm bilan bordi. 78 500 soʻmga goʻsht, "
                "24 000 soʻmga non va koʻkat oldi.</p><p><strong>Uning qoʻlida qancha "
                "pul qoldi?</strong></p>",
        "choices": ["97 500 soʻm", "102 500 soʻm", "121 500 soʻm", "96 500 soʻm"],
        "correct": "97 500 soʻm",
        "explanation": "<p><strong>97 500 soʻm.</strong> Avval xarajatni yigʻamiz: "
                       "78 500 + 24 000 = 102 500. Keyin ayiramiz: "
                       "200 000 − 102 500 = 97 500. <strong>102 500</strong> — "
                       "sarflangan pul, qolgani emas; savolni oxirigacha oʻqish shuning "
                       "uchun kerak.</p>",
    },
]


# =====================================================================
# PM-3 — koʻpaytirish
# =====================================================================

Q_PM3 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>8 × 7 = ?</strong></p>",
        "choices": ["56", "54", "63", "48"],
        "correct": "56",
        "explanation": "<p><strong>56.</strong> Esdan chiqsa boʻlaklang: "
                       "8 × 7 = 8 × 5 + 8 × 2 = 40 + 16 = 56.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>6 × 9 = ?</strong></p>",
        "choices": ["54", "56", "45", "63"],
        "correct": "54",
        "explanation": "<p><strong>54.</strong> 9 ga koʻpaytirish qoidasi bilan "
                       "tekshirish mumkin: natijaning raqamlari yigʻindisi doim 9 ga "
                       "teng — 5 + 4 = 9 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>4 × 6 nimani "
                "bildiradi?</strong></p>",
        "choices": ["6 + 6 + 6 + 6", "4 + 6", "4 + 4 + 4 + 4 + 4", "6 − 4"],
        "correct": "6 + 6 + 6 + 6",
        "explanation": "<p><strong>6 + 6 + 6 + 6 = 24.</strong> Koʻpaytirish — bir xil "
                       "sonni takror qoʻshishning qisqa yozuvi: 6 ni 4 marta oldik. "
                       "Toʻrtburchak modelida bu 4 qator, har qatorda 6 ta katak.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>12 × 0 = ?</strong></p>",
        "choices": ["0", "12", "1", "120"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> 12 ni nol marta oldik — hech narsa "
                       "yoʻq. Har qanday sonni 0 ga koʻpaytirsa, natija 0 boʻladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>25 × 1 = ?</strong></p>",
        "choices": ["25", "1", "26", "0"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Sonni 1 ga koʻpaytirsak, u oʻzgarmaydi: "
                       "25 ni bir marta oldik.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>24 × 6 = ?</strong></p>",
        "choices": ["144", "124", "126", "1 444"],
        "correct": "144",
        "explanation": "<p><strong>144.</strong> Birliklar: 4 × 6 = 24 — 4 ni yozamiz, "
                       "2 oʻnlikni koʻtaramiz. Oʻnliklar: 2 × 6 = 12, ustiga 2 → 14. "
                       "<strong>124</strong> — koʻtarilgan 2 unutilgan javob. Taxmin: "
                       "24 × 6 ≈ 25 × 6 = 150 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>45 × 3 = ?</strong></p>",
        "choices": ["135", "125", "1 215", "145"],
        "correct": "135",
        "explanation": "<p><strong>135.</strong> Boʻlaklab: 40 × 3 = 120, 5 × 3 = 15, "
                       "120 + 15 = 135. Taxmin: 45 × 3 ≈ 50 × 3 = 150 — javob shunga "
                       "yaqin.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>213 × 4 = ?</strong></p>",
        "choices": ["852", "842", "812", "8 052"],
        "correct": "852",
        "explanation": "<p><strong>852.</strong> Birliklar: 3 × 4 = 12 — 2 ni yozamiz, "
                       "1 ni koʻtaramiz. Oʻnliklar: 1 × 4 = 4, ustiga 1 → 5. "
                       "Yuzliklar: 2 × 4 = 8.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>36 × 10 = ?</strong></p>",
        "choices": ["360", "306", "3 600", "46"],
        "correct": "360",
        "explanation": "<p><strong>360.</strong> Har bir raqam bitta razryad chapga "
                       "suriladi, birliklar razryadi boʻshab qoladi va u yerga 0 "
                       "yoziladi. <strong>306</strong> — nol notoʻgʻri joyga "
                       "qoʻyilgan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>124 × 5 = ?</strong></p>",
        "choices": ["620", "610", "520", "6 200"],
        "correct": "620",
        "explanation": "<p><strong>620.</strong> Tez usul: 124 × 10 = 1 240, uning "
                       "yarmi 620. Ustunda ham shu chiqadi: 4 × 5 = 20 (0 yozamiz, 2 "
                       "koʻtariladi), 2 × 5 = 10 + 2 = 12, 1 × 5 = 5 + 1 = 6.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>7 × 12 = ?</strong></p>",
        "choices": ["84", "72", "74", "94"],
        "correct": "84",
        "explanation": "<p><strong>84.</strong> Boʻlaklab: 7 × 10 + 7 × 2 = 70 + 14 = "
                       "84. <strong>72</strong> — ikkinchi boʻlak (7 × 2) qoʻshilmay "
                       "qolgan javob.</p>",
    },
    {
        "text": "<p>Ogʻzaki hisoblang.</p><p><strong>6 × 25 = ?</strong></p>",
        "choices": ["150", "125", "160", "1 500"],
        "correct": "150",
        "explanation": "<p><strong>150.</strong> 4 × 25 = 100, qolgan 2 × 25 = 50, "
                       "jami 150. Yoki: 6 × 25 = 3 × 50 = 150.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>4 × 6 va 6 × 4 "
                "koʻpaytmalari haqida nima deyish mumkin?</strong></p>",
        "choices": ["Ular teng: ikkalasi ham 24",
                    "4 × 6 kattaroq", "6 × 4 kattaroq",
                    "Ularni taqqoslab boʻlmaydi"],
        "correct": "Ular teng: ikkalasi ham 24",
        "explanation": "<p><strong>Ular teng.</strong> Toʻrtburchakni qatorlab ham, "
                       "ustunlab ham sanash mumkin — kataklar soni oʻzgarmaydi. "
                       "Bu <em>oʻrin almashtirish</em> qoidasi, va u tufayli "
                       "koʻpaytirish jadvalining yarmini yodlash yetarli.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>8 × 5 + 8 × 2 ifodasi qaysi "
                "koʻpaytmaga teng?</strong></p>",
        "choices": ["8 × 7", "8 × 10", "8 × 3", "16 × 7"],
        "correct": "8 × 7",
        "explanation": "<p><strong>8 × 7 = 56.</strong> 8 ni avval 5 marta, keyin 2 "
                       "marta oldik — jami 7 marta. Bu boʻlaklab koʻpaytirish "
                       "qoidasining oʻzi, teskari tomondan oʻqilgani.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>36 × 100 = ?</strong></p>",
        "choices": ["3 600", "360", "36 000", "30 600"],
        "correct": "3 600",
        "explanation": "<p><strong>3 600.</strong> 100 ga koʻpaytirganda har bir raqam "
                       "<em>ikkita</em> razryad chapga suriladi, boʻshagan ikki "
                       "razryadga esa nol yoziladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>9 × 7 = 63. Bu javobni "
                "qanday qilib tez tekshirish mumkin?</strong></p>",
        "choices": ["Raqamlar yigʻindisi 9 ga teng: 6 + 3 = 9",
                    "Raqamlar yigʻindisi 7 ga teng",
                    "Javob juft son boʻlishi kerak",
                    "Javob 9 ga tugashi kerak"],
        "correct": "Raqamlar yigʻindisi 9 ga teng: 6 + 3 = 9",
        "explanation": "<p><strong>Raqamlar yigʻindisi 9 ga teng.</strong> 9 ga "
                       "koʻpaytirish jadvalining hamma natijalarida shunday: "
                       "18 (1+8), 27 (2+7), 36 (3+6), 63 (6+3), 81 (8+1).</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Oʻquvchi <strong>24 × 6 = 124</strong> deb yozdi.</p>"
                "<p><strong>Qayerda xato qilingan?</strong></p>",
        "choices": ["4 × 6 = 24 dagi koʻtarilgan 2 oʻnlik qoʻshilmagan",
                    "Koʻpaytirish oʻrniga qoʻshish bajarilgan",
                    "Sonlar notoʻgʻri tekislangan",
                    "Xato yoʻq"],
        "correct": "4 × 6 = 24 dagi koʻtarilgan 2 oʻnlik qoʻshilmagan",
        "explanation": "<p><strong>Koʻtarilgan 2 oʻnlik qoʻshilmagan.</strong> "
                       "Oʻnliklar hisobi 2 × 6 = 12 emas, 12 + 2 = 14 boʻlishi kerak "
                       "edi. Toʻgʻri javob — <strong>144</strong>, va u taxminga ham "
                       "mos: 24 × 6 ≈ 150.</p>",
    },
    {
        "text": "<p>Oʻquvchi <strong>7 × 12 = 72</strong> deb topdi.</p>"
                "<p><strong>Nima yetishmayapti?</strong></p>",
        "choices": ["7 × 2 boʻlagi qoʻshilmagan",
                    "7 × 10 boʻlagi qoʻshilmagan",
                    "Koʻtarilgan birlik unutilgan",
                    "Javob toʻgʻri"],
        "correct": "7 × 2 boʻlagi qoʻshilmagan",
        "explanation": "<p><strong>7 × 2 boʻlagi qoʻshilmagan.</strong> "
                       "7 × 12 = 7 × 10 + 7 × 2 = 70 + 14 = <strong>84</strong>. "
                       "Boʻlaklab koʻpaytirishda ikkala boʻlakni ham qoʻshish "
                       "kerak.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Omborda 6 ta yashik bor, har birida 24 tadan choynak. Yana 3 ta "
                "choynak yashiksiz, alohida turibdi.</p><p><strong>Omborda jami nechta "
                "choynak bor?</strong></p>",
        "choices": ["147 ta", "144 ta", "150 ta", "33 ta"],
        "correct": "147 ta",
        "explanation": "<p><strong>147 ta.</strong> “Har birida 24 tadan” — bu "
                       "koʻpaytirish: 6 × 24 = 144. Yakka choynaklarni qoʻshamiz: "
                       "144 + 3 = 147. <strong>144</strong> — oxirgi jumlani "
                       "oʻqimaganda chiqadigan javob.</p>",
    },
    {
        "text": "<p>Sinfda 4 qator parta bor. Har qatorda 7 tadan parta, har partada "
                "2 oʻquvchi oʻtiradi.</p><p><strong>Sinfda nechta oʻquvchi "
                "bor?</strong></p>",
        "choices": ["56 ta", "28 ta", "13 ta", "42 ta"],
        "correct": "56 ta",
        "explanation": "<p><strong>56 ta.</strong> Ikki bosqichli masala: avval partalar "
                       "soni 4 × 7 = 28, keyin oʻquvchilar soni 28 × 2 = 56. "
                       "<strong>28</strong> — bu partalar soni, oʻquvchilar emas; har "
                       "bosqichda “bu nima?” deb ayting.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-1 Mashq: Razryadlar va raqamning oʻrni",
        "description": "20 savol — razryad, yoyilma yozuv, nolning vazifasi, "
                       "katta sonlarni oʻqish va taqqoslash.",
        "tutorial":    "PM-1:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM1,
    },
    {
        "title":       "PM-2 Mashq: Qoʻshish va ayirish — ustunda va ogʻzaki",
        "description": "20 savol — ustun usuli, koʻtarish va qarz olish, ogʻzaki "
                       "hisob usullari, tekshirish va kassa masalalari.",
        "tutorial":    "PM-2:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM2,
    },
    {
        "title":       "PM-3 Mashq: Koʻpaytirish va jadval mantigʻi",
        "description": "20 savol — koʻpaytirishning maʼnosi, jadval qoidalari, "
                       "ustunda koʻpaytirish va matnli masalalar.",
        "tutorial":    "PM-3:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM3,
    },
]
