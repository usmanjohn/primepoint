# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-57, PM-58, PM-59 (geometriya alifbosi, burchak,
burchak juftliklari).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: `medium` (Blok E, 70 gacha).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq. Savol matnida <strong>, <sup> mumkin.
⚠️ Kumulyativ: parallel chiziq va kesuvchi (PM-60) YOʻQ, uchburchak burchaklari
   yigʻindisi (PM-61) YOʻQ, Pifagor (PM-64) YOʻQ, perimetr (PM-67) va yuza
   (PM-68) YOʻQ, aylana uzunligi/π (PM-70, PM-71) YOʻQ.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_57_59.py --master=prime \\
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
# PM-57 — nuqta, chiziq, kesma, nur
# =====================================================================

Q_PM57 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi shaklning "
                "uzunligini oʻlchash mumkin?</strong></p>",
        "choices": ["Kesma", "Nuqta", "Nur", "Toʻgʻri chiziq"],
        "correct": "Kesma",
        "explanation": "<p><strong>Kesma.</strong> Faqat uning ikkala uchi ham "
                       "bor, demak boshi bilan oxiri orasidagi masofani oʻlchash "
                       "mumkin. Nuqtaning oʻlchami yoʻq; nur bir tomonga, "
                       "toʻgʻri chiziq esa ikki tomonga cheksiz davom etadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nur AB ning boshi "
                "qaysi nuqtada?</strong></p>",
        "choices": ["A nuqtasida", "B nuqtasida", "Oʻrtasida", "Boshi yoʻq"],
        "correct": "A nuqtasida",
        "explanation": "<p><strong>A nuqtasida.</strong> Nurni belgilashda "
                       "birinchi harf har doim boshini bildiradi, ikkinchisi esa "
                       "yoʻnalishini koʻrsatadi. Shuning uchun nur AB bilan nur "
                       "BA — ikki xil nur, kesma AB bilan kesma BA esa bir "
                       "xil.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki nuqta orqali "
                "nechta toʻgʻri chiziq oʻtkazish mumkin?</strong></p>",
        "choices": ["Faqat bitta", "Ikkita", "Uchta", "Cheksiz koʻp"],
        "correct": "Faqat bitta",
        "explanation": "<p><strong>Faqat bitta.</strong> Bitta nuqta orqali "
                       "cheksiz koʻp chiziq oʻtadi — qalamni aylantiraverasiz. "
                       "Ikkinchi nuqta uni qotiradi. Usta taxtani devorga "
                       "ikkita mix bilan qoqishining sababi ham shu.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>M nuqtasi AB kesmasining oʻrtasi. "
                "AB = 20 sm boʻlsa, AM qancha?</strong></p>",
        "choices": ["5 sm", "10 sm", "20 sm", "40 sm"],
        "correct": "10 sm",
        "explanation": "<p><strong>10 sm.</strong> Oʻrta nuqta kesmani teng "
                       "ikkiga boʻladi: 20 ÷ 2 = 10. Tekshirish: 10 + 10 = 20 ✓ "
                       "<strong>40 sm</strong> — boʻlish oʻrniga koʻpaytirilgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Geometriyada nuqta "
                "qanday belgilanadi?</strong></p>",
        "choices": [
            "Bosh harf bilan: A, B, O",
            "Kichik harf bilan: a, b, o",
            "Son bilan: 1, 2, 3",
            "Ikki harf bilan: AB",
        ],
        "correct": "Bosh harf bilan: A, B, O",
        "explanation": "<p><strong>Bosh harf bilan.</strong> Nuqtalar A, B, C, O "
                       "kabi bosh harflar bilan belgilanadi. Ikki harf (AB) esa "
                       "kesma, nur yoki toʻgʻri chiziqni bildiradi — qaysi biri "
                       "ekanini yonidagi soʻz aytadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p>A, B va C nuqtalari shu tartibda bitta "
                "toʻgʻri chiziqda yotadi.</p><p><strong>AB = 15 sm, BC = 8 sm "
                "boʻlsa, AC qancha?</strong></p>",
        "choices": ["7 sm", "15 sm", "23 sm", "30 sm"],
        "correct": "23 sm",
        "explanation": "<p><strong>23 sm.</strong> B nuqtasi A bilan C orasida "
                       "yotgani uchun kesmalar qoʻshiladi: AB + BC = AC, "
                       "15 + 8 = 23. <strong>7 sm</strong> — qoʻshish oʻrniga "
                       "ayirilganda chiqadi, bu esa C nuqtasi orada yotgan "
                       "boshqa holga tegishli.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>C nuqtasi A bilan B orasida yotadi.</p>"
                "<p><strong>AB = 30 sm, AC = 12 sm boʻlsa, CB qancha?</strong></p>",
        "choices": ["12 sm", "18 sm", "30 sm", "42 sm"],
        "correct": "18 sm",
        "explanation": "<p><strong>18 sm.</strong> AC + CB = AB, demak "
                       "CB = 30 − 12 = 18. Tekshirish: 12 + 18 = 30 ✓ "
                       "<strong>42 sm</strong> — ayirish oʻrniga qoʻshilganda "
                       "chiqadi, lekin qism butundan katta boʻlolmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>M nuqtasi AB kesmasining oʻrtasi va "
                "AM = 7,5 sm. AB qancha?</strong></p>",
        "choices": ["3,75 sm", "7,5 sm", "15 sm", "22,5 sm"],
        "correct": "15 sm",
        "explanation": "<p><strong>15 sm.</strong> Oʻrta nuqta ikkita teng "
                       "boʻlak beradi, demak AB = 2 × 7,5 = 15. "
                       "<strong>3,75 sm</strong> — koʻpaytirish oʻrniga yana "
                       "ikkiga boʻlinganda chiqadi; butun kesma oʻz yarmidan "
                       "kichik boʻlolmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki toʻgʻri chiziq "
                "eng koʻpi bilan nechta nuqtada kesishishi mumkin?</strong></p>",
        "choices": ["Bitta nuqtada", "Ikkita nuqtada", "Uchta nuqtada",
                    "Cheksiz koʻp nuqtada"],
        "correct": "Bitta nuqtada",
        "explanation": "<p><strong>Bitta nuqtada.</strong> Agar ikkita umumiy "
                       "nuqtasi boʻlganida, oʻsha ikki nuqta orqali ikkita "
                       "toʻgʻri chiziq oʻtgan boʻlardi — bu esa mumkin emas. "
                       "Demak ular yo bitta nuqtada kesishadi, yo umuman "
                       "kesishmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Tekislikda 5 ta nuqta bor va ularning hech "
                "qaysi uchtasi bitta toʻgʻri chiziqda yotmaydi.</p><p><strong>Ular "
                "orqali nechta toʻgʻri chiziq oʻtkazish mumkin?</strong></p>",
        "choices": ["5 ta", "10 ta", "15 ta", "20 ta"],
        "correct": "10 ta",
        "explanation": "<p><strong>10 ta.</strong> Har bir juft nuqta bitta "
                       "chiziq beradi. Birinchi nuqtani 5 xil, ikkinchisini "
                       "4 xil tanlaymiz: 5 × 4 = 20, lekin AB bilan BA bir xil "
                       "chiziq, shuning uchun 20 ÷ 2 = 10. "
                       "<strong>20 ta</strong> — aynan shu ikkiga boʻlish "
                       "unutilgan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Xonaning rejasi 1 : 200 masshtabda "
                "chizilgan.</p><p><strong>Rejadagi 6 sm lik kesma haqiqatda necha "
                "metr?</strong></p>",
        "choices": ["6 metr", "12 metr", "20 metr", "120 metr"],
        "correct": "12 metr",
        "explanation": "<p><strong>12 metr.</strong> 1 : 200 degani rejadagi "
                       "1 sm haqiqatda 200 sm (PM-28). 6 × 200 = 1 200 sm = "
                       "12 m. <strong>120 metr</strong> — santimetrni metrga "
                       "aylantirish unutilganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>AB = 24 sm. M — AB ning oʻrtasi, N esa AM "
                "ning oʻrtasi.</p><p><strong>AN qancha?</strong></p>",
        "choices": ["3 sm", "6 sm", "8 sm", "12 sm"],
        "correct": "6 sm",
        "explanation": "<p><strong>6 sm.</strong> Avval AM = 24 ÷ 2 = 12, keyin "
                       "AN = 12 ÷ 2 = 6. <strong>12 sm</strong> — faqat "
                       "birinchi qadam bajarilganda chiqadi, yaʼni AM ning "
                       "oʻzi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Kesma AB bilan "
                "toʻgʻri chiziq AB orasidagi farq nimada?</strong></p>",
        "choices": [
            "Kesma A va B da tugaydi, toʻgʻri chiziq esa davom etadi",
            "Kesma egri, toʻgʻri chiziq tekis",
            "Kesma faqat gorizontal boʻladi",
            "Hech qanday farq yoʻq, ikkalasi bir xil",
        ],
        "correct": "Kesma A va B da tugaydi, toʻgʻri chiziq esa davom etadi",
        "explanation": "<p><strong>Kesma A va B da tugaydi.</strong> Ikkalasi "
                       "ham «AB» deb yoziladi, farqni yonidagi soʻz aytadi. "
                       "Aynan shuning uchun «AB = 12 sm» degan yozuv faqat kesma "
                       "haqida maʼnoga ega.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi juftlikda "
                "harflarning tartibi maʼnoni oʻzgartiradi?</strong></p>",
        "choices": [
            "Nur AB va nur BA",
            "Kesma AB va kesma BA",
            "Toʻgʻri chiziq AB va toʻgʻri chiziq BA",
            "Hech qaysisida",
        ],
        "correct": "Nur AB va nur BA",
        "explanation": "<p><strong>Nur AB va nur BA.</strong> Nurda birinchi "
                       "harf boshini bildiradi, demak bular qarama-qarshi "
                       "yoʻnalishdagi ikki xil nur. Kesmada ham, toʻgʻri "
                       "chiziqda ham tartib hech narsani oʻzgartirmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>AB = 12 sm va BC = 5 sm, "
                "lekin nuqtalarning tartibi aytilmagan.</p><p><strong>AC qanday "
                "boʻlishi mumkin?</strong></p>",
        "choices": [
            "7 sm yoki 17 sm",
            "Faqat 17 sm",
            "Faqat 7 sm",
            "Faqat 12 sm",
        ],
        "correct": "7 sm yoki 17 sm",
        "explanation": "<p><strong>7 sm yoki 17 sm.</strong> Agar B nuqtasi "
                       "A bilan C orasida boʻlsa, AC = 12 + 5 = 17. Agar "
                       "C nuqtasi A bilan B orasida boʻlsa, AC = 12 − 5 = 7. "
                       "Tartib aytilmagan ekan, ikkala javob ham mumkin — avval "
                       "chizing, keyin hisoblang.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi shaklning eni "
                "ham, boʻyi ham yoʻq?</strong></p>",
        "choices": ["Nuqta", "Kesma", "Nur", "Tekislik"],
        "correct": "Nuqta",
        "explanation": "<p><strong>Nuqta.</strong> U faqat oʻrinni koʻrsatadi. "
                       "Qogʻozdagi qora nuqtacha — uning tasviri, oʻzi emas. "
                       "Tekislik esa aksincha, ikki tomonga ham cheksiz "
                       "yoyilgan.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>«AB toʻgʻri chizigʻining "
                "uzunligi 9 sm».</strong></p>",
        "choices": [
            "Toʻgʻri chiziqning uzunligi boʻlmaydi — bu kesma boʻlishi kerak",
            "Uzunlik metrda oʻlchanishi kerak edi",
            "Toʻgʻri chiziq bir harf bilan belgilanadi",
            "Xato yoʻq, yozuv toʻgʻri",
        ],
        "correct": "Toʻgʻri chiziqning uzunligi boʻlmaydi — bu kesma boʻlishi kerak",
        "explanation": "<p><strong>Toʻgʻri chiziqning uzunligi boʻlmaydi.</strong> "
                       "U ikki tomonga cheksiz davom etadi, demak oʻlchab "
                       "boʻlmaydi. Oʻlchanadigan yagona shakl — kesma, shuning "
                       "uchun toʻgʻrisi «AB <strong>kesmasining</strong> uzunligi "
                       "9 sm».</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Masala: AB = 10 sm, BC = 4 sm, "
                "nuqtalar bitta chiziqda.</p><p><strong>Yechim: AC = 10 + 4 = "
                "14 sm.</strong></p>",
        "choices": [
            "Nuqtalarning tartibi aytilmagan — 6 sm ham mumkin",
            "Qoʻshish oʻrniga koʻpaytirish kerak edi",
            "Birliklar notoʻgʻri",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Nuqtalarning tartibi aytilmagan — 6 sm ham mumkin",
        "explanation": "<p><strong>Tartib aytilmagan.</strong> 14 sm faqat "
                       "B nuqtasi orada yotganda toʻgʻri. Agar C nuqtasi A bilan "
                       "B orasida boʻlsa, AC = 10 − 4 = 6 sm. «Bitta chiziqda "
                       "yotadi» degani hali «shu tartibda yotadi» degani "
                       "emas.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Sherbekning uyi, kutubxona va maktab bitta toʻgʻri koʻchada "
                "shu tartibda joylashgan. Uydan maktabgacha 1 200 metr. "
                "Kutubxona uy bilan maktabning aynan oʻrtasida.</p>"
                "<p><strong>Kutubxonadan maktabgacha necha metr?</strong></p>",
        "choices": ["400 metr", "600 metr", "800 metr", "1 200 metr"],
        "correct": "600 metr",
        "explanation": "<p><strong>600 metr.</strong> Kutubxona — kesmaning "
                       "oʻrta nuqtasi, demak u yoʻlni ikkita teng boʻlakka "
                       "boʻladi: 1 200 ÷ 2 = 600. Tekshirish: 600 + 600 = "
                       "1 200 ✓</p>",
    },
    {
        "text": "<p>Nodira opa xonasining rejasini 1 : 150 masshtabda chizdi. "
                "Rejada uzun devor 9 sm lik kesma boʻlib chiqdi.</p>"
                "<p><strong>Devor haqiqatda necha metr?</strong></p>",
        "choices": ["9 metr", "13,5 metr", "15 metr", "135 metr"],
        "correct": "13,5 metr",
        "explanation": "<p><strong>13,5 metr.</strong> 1 : 150 degani rejadagi "
                       "1 sm haqiqatda 150 sm. 9 × 150 = 1 350 sm, keyin "
                       "1 350 ÷ 100 = 13,5 m. <strong>135 metr</strong> — "
                       "santimetrni metrga aylantirish unutilganda chiqadi; "
                       "13,5 metrlik devor real, 135 metrlik esa emas.</p>",
    },
]


# =====================================================================
# PM-58 — burchak va uni oʻlchash
# =====================================================================

Q_PM58 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>∠XYZ burchagining "
                "uchi qaysi nuqtada?</strong></p>",
        "choices": ["X nuqtasida", "Y nuqtasida", "Z nuqtasida",
                    "Uch nuqtaning oʻrtasida"],
        "correct": "Y nuqtasida",
        "explanation": "<p><strong>Y nuqtasida.</strong> Burchak yozuvida "
                       "oʻrtadagi harf har doim uchni bildiradi; chetdagi ikki "
                       "harf esa tomonlaridagi nuqtalar. Shuning uchun ∠XYZ "
                       "bilan ∠ZYX bir xil, ∠YXZ esa butunlay boshqa "
                       "burchak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>45° li burchak qaysi "
                "turga kiradi?</strong></p>",
        "choices": ["Oʻtkir", "Toʻgʻri", "Oʻtmas", "Yoyiq"],
        "correct": "Oʻtkir",
        "explanation": "<p><strong>Oʻtkir.</strong> 90° dan kichik burchaklar "
                       "oʻtkir deyiladi. Toʻgʻri burchak aniq 90°, oʻtmas "
                       "burchak 90 bilan 180 orasida, yoyiq esa aniq 180°.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Toʻla burchak necha "
                "gradus?</strong></p>",
        "choices": ["90°", "180°", "270°", "360°"],
        "correct": "360°",
        "explanation": "<p><strong>360°.</strong> Bu toʻliq bir aylanish. "
                       "Yarmi — yoyiq burchak, 180°; choragi — toʻgʻri burchak, "
                       "90°. 360 soni tanlangani bejiz emas: u juda koʻp songa "
                       "qoldiqsiz boʻlinadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Chizmada toʻgʻri "
                "burchak qanday belgilanadi?</strong></p>",
        "choices": [
            "Uchida kichik kvadratcha bilan",
            "Ikkita yoy bilan",
            "Qalin nuqta bilan",
            "Uzuq chiziq bilan",
        ],
        "correct": "Uchida kichik kvadratcha bilan",
        "explanation": "<p><strong>Kichik kvadratcha bilan.</strong> Bu — "
                       "xalqaro odat: 90° li burchak yoy bilan emas, kvadratcha "
                       "bilan koʻrsatiladi. Shuning uchun chizmada kvadratchani "
                       "koʻrsangiz, oʻsha burchak aniq 90° degani.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Yoyiq burchak necha "
                "gradus?</strong></p>",
        "choices": ["45°", "90°", "180°", "360°"],
        "correct": "180°",
        "explanation": "<p><strong>180°.</strong> Uning tomonlari qarama-qarshi "
                       "nurlar boʻlgani uchun yoyiq burchak toʻgʻri chiziqqa "
                       "oʻxshab koʻrinadi — lekin u baribir burchak va "
                       "oʻlchanadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>Doira 6 ta teng boʻlakka boʻlindi. "
                "Bitta boʻlakning markazdagi burchagi qancha?</strong></p>",
        "choices": ["30°", "45°", "60°", "72°"],
        "correct": "60°",
        "explanation": "<p><strong>60°.</strong> Toʻla burchak 6 ga boʻlinadi: "
                       "360 ÷ 6 = 60. Tekshirish: 6 × 60 = 360 ✓ — boʻlaklar "
                       "toʻliq aylanani toʻldiradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>OB nuri ∠AOC burchagining ichida yotadi.</p>"
                "<p><strong>∠AOB = 32° va ∠BOC = 41° boʻlsa, ∠AOC "
                "qancha?</strong></p>",
        "choices": ["9°", "41°", "73°", "90°"],
        "correct": "73°",
        "explanation": "<p><strong>73°.</strong> Ichkaridagi nur burchakni "
                       "ikkiga boʻladi, demak boʻlaklar qoʻshiladi: "
                       "32 + 41 = 73. <strong>9°</strong> — qoʻshish oʻrniga "
                       "ayirilgan javob. 73° hali ham 90 dan kichik, demak ∠AOC "
                       "oʻtkir burchak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>137° li burchak qaysi "
                "turga kiradi?</strong></p>",
        "choices": ["Oʻtkir", "Toʻgʻri", "Oʻtmas", "Toʻla"],
        "correct": "Oʻtmas",
        "explanation": "<p><strong>Oʻtmas.</strong> 137 soni 90 dan katta va "
                       "180 dan kichik. Oʻtkir boʻlishi uchun 90 dan kichik "
                       "boʻlishi kerak edi; yoyiq boʻlishi uchun esa aniq 180 "
                       "boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Tort teng boʻlaklarga kesildi va har bir "
                "boʻlakning burchagi 40° chiqdi.</p><p><strong>Nechta boʻlak "
                "kesilgan?</strong></p>",
        "choices": ["6 ta", "8 ta", "9 ta", "12 ta"],
        "correct": "9 ta",
        "explanation": "<p><strong>9 ta.</strong> 360 ÷ 40 = 9. Tekshirish: "
                       "9 × 40 = 360 ✓ Boʻlaklar soni har doim toʻla burchakni "
                       "bitta boʻlak burchagiga boʻlish bilan topiladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Soat siferblatidagi ikki qoʻshni son "
                "orasidagi burchak 30°.</p><p><strong>Soat aynan 2:00 boʻlganda "
                "millar orasidagi burchak qancha?</strong></p>",
        "choices": ["30°", "60°", "90°", "120°"],
        "correct": "60°",
        "explanation": "<p><strong>60°.</strong> Soat 2:00 da daqiqa mili 12 da, "
                       "soat mili esa 2 da turadi — orada 2 ta boʻlim bor: "
                       "2 × 30 = 60°. <strong>30°</strong> — boʻlimlar soni "
                       "notoʻgʻri sanalganda chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bekzod shimolga qarab "
                "turibdi va oʻng tomonga 180° buriladi.</p><p><strong>Endi qaysi "
                "tomonga qarab turibdi?</strong></p>",
        "choices": ["Sharqqa", "Gʻarbga", "Janubga", "Yana shimolga"],
        "correct": "Janubga",
        "explanation": "<p><strong>Janubga.</strong> 180° — yarim aylanish, "
                       "yaʼni aynan teskari tomon. <strong>Sharqqa</strong> "
                       "boʻlishi uchun 90° burilishi kerak edi, "
                       "<strong>yana shimolga</strong> qarashi uchun esa toʻla "
                       "360°.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Toʻla burchakdan 250° li burchak "
                "olinsa, qolgani qancha boʻladi?</strong></p>",
        "choices": ["70°", "110°", "130°", "250°"],
        "correct": "110°",
        "explanation": "<p><strong>110°.</strong> Toʻla burchak 360°, demak "
                       "360 − 250 = 110. Tekshirish: 250 + 110 = 360 ✓ "
                       "<strong>70°</strong> — 180 dan ayirilganda chiqadi, "
                       "lekin bu yerda gap toʻla aylana haqida.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Aniq 90° li burchak "
                "qaysi turga kiradi?</strong></p>",
        "choices": [
            "Toʻgʻri burchak — na oʻtkir, na oʻtmas",
            "Oʻtkir burchak",
            "Oʻtmas burchak",
            "Ham oʻtkir, ham oʻtmas",
        ],
        "correct": "Toʻgʻri burchak — na oʻtkir, na oʻtmas",
        "explanation": "<p><strong>Toʻgʻri burchak.</strong> Oʻtkir "
                       "<strong>90 dan kichik</strong>, oʻtmas esa "
                       "<strong>90 dan katta</strong> boʻlishi shart. 90 ning "
                       "oʻzi ikkalasiga ham kirmaydi — u alohida turga ega va "
                       "kvadratcha bilan belgilanadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>∠ABC va ∠BAC "
                "burchaklari haqida nima deyish mumkin?</strong></p>",
        "choices": [
            "Bular ikki xil burchak: uchlari har xil",
            "Bular bir xil burchak",
            "Ular har doim teng boʻladi",
            "Ularning yigʻindisi 180°",
        ],
        "correct": "Bular ikki xil burchak: uchlari har xil",
        "explanation": "<p><strong>Ikki xil burchak.</strong> ∠ABC ning uchi B, "
                       "∠BAC ning uchi esa A — oʻrtadagi harf uchni bildiradi. "
                       "Bitta harfni surib yuborish butun burchakni "
                       "almashtiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Burchak tomonlari "
                "ikki barobar uzun chizilsa, burchak qanday oʻzgaradi?</strong></p>",
        "choices": [
            "Oʻzgarmaydi",
            "Ikki barobar kattalashadi",
            "Ikki barobar kichrayadi",
            "Toʻgʻri burchakka aylanadi",
        ],
        "correct": "Oʻzgarmaydi",
        "explanation": "<p><strong>Oʻzgarmaydi.</strong> Burchak uzunlikni emas, "
                       "<strong>burilish</strong>ni oʻlchaydi. Tomonlar nur "
                       "boʻlgani uchun ular allaqachon cheksiz — ularni "
                       "«uzaytirish» chizmaning koʻrinishini oʻzgartiradi, "
                       "burchakni emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Transportirda burchakning "
                "nuri 60 va 120 sonlari orasidan oʻtdi, burchak esa koʻzga "
                "oʻtmas koʻrinadi.</p><p><strong>Javob qaysi?</strong></p>",
        "choices": ["120°", "60°", "180°", "90°"],
        "correct": "120°",
        "explanation": "<p><strong>120°.</strong> Transportirda ikki shkala bor, "
                       "shuning uchun bitta nur ikkita son koʻrsatadi. Tanlash "
                       "qoidasi: burchakning ikkinchi tomoni qaysi shkaladagi 0 "
                       "da yotgan boʻlsa, javob ham oʻsha shkaladan olinadi. "
                       "Tekshiruvi esa yanada oson — oʻtmas burchak 90 dan "
                       "<strong>katta</strong> boʻlishi shart.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p>Oʻquvchi koʻzga oʻtkir koʻringan "
                "burchakni transportir bilan oʻlchadi.</p><p><strong>Yozdi: "
                "«burchak 145°».</strong></p>",
        "choices": [
            "Notoʻgʻri shkala oʻqilgan — oʻtkir burchak 90 dan kichik",
            "Transportirning markazi notoʻgʻri qoʻyilgan",
            "Burchak oʻtmas, demak javob toʻgʻri",
            "145° umuman mavjud emas",
        ],
        "correct": "Notoʻgʻri shkala oʻqilgan — oʻtkir burchak 90 dan kichik",
        "explanation": "<p><strong>Notoʻgʻri shkala oʻqilgan.</strong> Oʻtkir "
                       "burchak taʼrifiga koʻra 90° dan kichik, demak 145° "
                       "boʻlishi mumkin emas. Toʻgʻri qiymat ikkinchi shkalada "
                       "turibdi: 180 − 145 = 35°.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>«Uchi M boʻlgan burchak: "
                "∠KMN emas, ∠MKN deb yozildi».</strong></p>",
        "choices": [
            "Uchning harfi oʻrtada turishi kerak: ∠KMN",
            "Burchak faqat ikki harf bilan yoziladi",
            "Harflar alifbo tartibida yozilishi kerak",
            "Xato yoʻq, ikkala yozuv ham toʻgʻri",
        ],
        "correct": "Uchning harfi oʻrtada turishi kerak: ∠KMN",
        "explanation": "<p><strong>Uchning harfi oʻrtada turishi kerak.</strong> "
                       "∠MKN yozuvining uchi K boʻlib qoladi — bu boshqa "
                       "burchak. Yozishdan oldin oʻzingizga bitta savol bering: "
                       "«uchi qayerda?» — oʻsha harf oʻrtaga tushadi.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Bogʻdagi doira shaklidagi gulzor markazdan chiqqan "
                "yoʻlchalar bilan 5 ta teng boʻlakka boʻlingan. Dilnoza ulardan "
                "2 tasiga atirgul ekdi.</p><p><strong>Atirgul ekilgan qismning "
                "markazdagi burchagi qancha?</strong></p>",
        "choices": ["72°", "108°", "144°", "180°"],
        "correct": "144°",
        "explanation": "<p><strong>144°.</strong> Avval bitta boʻlak: "
                       "360 ÷ 5 = 72°. Keyin ikkita boʻlak qoʻshiladi: "
                       "2 × 72 = 144°. Tekshirish: 5 × 72 = 360 ✓ "
                       "<strong>72°</strong> — faqat bitta boʻlak hisoblangan "
                       "javob. 144° oʻtmas burchak, chizmada ham shunday "
                       "koʻrinadi.</p>",
    },
    {
        "text": "<p>Oʻyinchoq robot shimolga qarab turibdi. U ketma-ket uch "
                "marta oʻng tomonga 90° dan buriladi.</p><p><strong>Robot qaysi "
                "tomonga qarab qoladi va jami necha gradus buriladi?</strong></p>",
        "choices": [
            "Sharqqa, 180°",
            "Janubga, 180°",
            "Gʻarbga, 270°",
            "Shimolga, 360°",
        ],
        "correct": "Gʻarbga, 270°",
        "explanation": "<p><strong>Gʻarbga, 270°.</strong> Shimoldan oʻngga: "
                       "birinchi burilish — sharq, ikkinchisi — janub, "
                       "uchinchisi — gʻarb. Burilishlar qoʻshiladi: "
                       "3 × 90 = 270°. Tekshirish: yana bir 90° qoʻshsak "
                       "360° boʻlib, robot shimolga qaytadi ✓</p>",
    },
]


# =====================================================================
# PM-59 — burchak juftliklari
# =====================================================================

Q_PM59 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qoʻshni burchaklarning "
                "yigʻindisi qancha?</strong></p>",
        "choices": ["90°", "180°", "270°", "360°"],
        "correct": "180°",
        "explanation": "<p><strong>180°.</strong> Ular birgalikda yoyiq "
                       "burchakni, yaʼni toʻgʻri chiziqni toʻldiradi. "
                       "<strong>90°</strong> — bu toʻldiruvchi burchaklar "
                       "haqida; ikkalasini adashtirmaslik uchun chizmaga qarang: "
                       "toʻgʻri chiziq hosil boʻlsa — 180.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>50° li burchakning qoʻshnisi "
                "qancha?</strong></p>",
        "choices": ["40°", "50°", "130°", "310°"],
        "correct": "130°",
        "explanation": "<p><strong>130°.</strong> 180 − 50 = 130. Tekshirish: "
                       "50 + 130 = 180 ✓ <strong>40°</strong> — bu qoʻshnisi "
                       "emas, <strong>toʻldiruvchisi</strong> (90 − 50).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Vertikal burchaklar "
                "haqida nima deyish mumkin?</strong></p>",
        "choices": [
            "Ular har doim teng",
            "Ularning yigʻindisi 180°",
            "Ularning yigʻindisi 90°",
            "Ular har doim toʻgʻri burchak",
        ],
        "correct": "Ular har doim teng",
        "explanation": "<p><strong>Ular har doim teng.</strong> Vertikal "
                       "burchaklar — kesishgan chiziqlarda qarama-qarshi "
                       "yotganlari. 180° beradiganlari esa yonma-yon yotgan "
                       "qoʻshni burchaklar.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>30° li burchakning toʻldiruvchisi "
                "qancha?</strong></p>",
        "choices": ["30°", "60°", "90°", "150°"],
        "correct": "60°",
        "explanation": "<p><strong>60°.</strong> Toʻldiruvchi burchaklar "
                       "birgalikda toʻgʻri burchakni beradi: 90 − 30 = 60. "
                       "<strong>150°</strong> — 180 dan ayirilgan javob, bu esa "
                       "qoʻshni burchak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Toʻldiruvchi "
                "burchaklarning yigʻindisi qancha?</strong></p>",
        "choices": ["45°", "90°", "180°", "360°"],
        "correct": "90°",
        "explanation": "<p><strong>90°.</strong> Nomi ham shundan: ular toʻgʻri "
                       "burchakni <strong>toʻldiradi</strong>. Shuning uchun "
                       "90° dan katta burchakning toʻldiruvchisi umuman "
                       "boʻlmaydi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p>Ikki toʻgʻri chiziq kesishdi va "
                "burchaklardan biri 43°.</p><p><strong>Unga qarama-qarshi yotgan "
                "burchak qancha?</strong></p>",
        "choices": ["43°", "47°", "137°", "180°"],
        "correct": "43°",
        "explanation": "<p><strong>43°.</strong> Qarama-qarshi yotgan burchaklar "
                       "vertikal, demak teng. <strong>137°</strong> — bu "
                       "yonma-yon yotgan qoʻshni burchak (180 − 43), "
                       "<strong>47°</strong> esa toʻldiruvchisi (90 − 43).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>68° li burchakning qoʻshnisi "
                "qancha?</strong></p>",
        "choices": ["22°", "68°", "112°", "292°"],
        "correct": "112°",
        "explanation": "<p><strong>112°.</strong> 180 − 68 = 112. Tekshirish: "
                       "68 + 112 = 180 ✓ Oʻtkir burchakning qoʻshnisi har doim "
                       "oʻtmas boʻladi — 112 shu talabga javob beradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>68° li burchakning toʻldiruvchisi "
                "qancha?</strong></p>",
        "choices": ["12°", "22°", "32°", "112°"],
        "correct": "22°",
        "explanation": "<p><strong>22°.</strong> 90 − 68 = 22. Tekshirish: "
                       "68 + 22 = 90 ✓ <strong>112°</strong> — 180 dan "
                       "ayirilgan javob, yaʼni qoʻshnisi. Bitta burchakning "
                       "toʻldiruvchisi ham, qoʻshnisi ham bor — savolni "
                       "diqqat bilan oʻqing.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Qoʻshni burchaklardan biri "
                "ikkinchisidan 5 marta katta. Kichigi qancha?</strong></p>",
        "choices": ["30°", "36°", "45°", "150°"],
        "correct": "30°",
        "explanation": "<p><strong>30°.</strong> x + 5x = 180, demak 6x = 180 va "
                       "x = 30. Kattasi esa 5 × 30 = 150. Tekshirish: "
                       "30 + 150 = 180 ✓ <strong>36°</strong> — 180 ni 5 ga "
                       "boʻlganda chiqadi, lekin ulushlar soni 5 ta emas, "
                       "6 ta.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Burchak oʻzining "
                "toʻldiruvchisidan 30° katta. Katta burchak qancha?</strong></p>",
        "choices": ["30°", "45°", "60°", "75°"],
        "correct": "60°",
        "explanation": "<p><strong>60°.</strong> x + y = 90 va x − y = 30. "
                       "Qoʻshamiz (PM-54): 2x = 120, x = 60, keyin y = 30. "
                       "Tekshirish: 60 + 30 = 90 ✓ va 60 − 30 = 30 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Ikki toʻgʻri chiziq kesishganda "
                "hosil boʻlgan toʻrtta burchakning yigʻindisi qancha?</strong></p>",
        "choices": ["180°", "270°", "360°", "540°"],
        "correct": "360°",
        "explanation": "<p><strong>360°.</strong> Toʻrtala burchak kesishish "
                       "nuqtasi atrofini toʻliq aylanib chiqadi, demak toʻla "
                       "burchakni beradi. Buni tekshiruv sifatida ishlating: "
                       "masalan 43 + 137 + 43 + 137 = 360 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Ikki chiziq kesishdi va burchaklardan biri "
                "aniq 90°.</p><p><strong>Qolgan uchtasi qancha?</strong></p>",
        "choices": [
            "Uchalasi ham 90°",
            "Ikkitasi 90°, bittasi 180°",
            "Uchalasi ham 45°",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Uchalasi ham 90°",
        "explanation": "<p><strong>Uchalasi ham 90°.</strong> Qoʻshnisi "
                       "180 − 90 = 90, vertikallari ham 90. Bunday chiziqlar "
                       "<strong>perpendikulyar</strong> deyiladi. Tekshirish: "
                       "4 × 90 = 360 ✓</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Toʻldiruvchi bilan "
                "qoʻshni burchaklarning farqi nimada?</strong></p>",
        "choices": [
            "Toʻldiruvchilar 90° ni, qoʻshnilar 180° ni beradi",
            "Toʻldiruvchilar 180° ni, qoʻshnilar 90° ni beradi",
            "Toʻldiruvchilar teng, qoʻshnilar har xil",
            "Hech qanday farq yoʻq",
        ],
        "correct": "Toʻldiruvchilar 90° ni, qoʻshnilar 180° ni beradi",
        "explanation": "<p><strong>Toʻldiruvchilar 90°, qoʻshnilar 180°.</strong> "
                       "Chizmadan bilib olish oson: agar ikki burchak birga "
                       "<strong>toʻgʻri chiziq</strong> hosil qilsa — 180; agar "
                       "<strong>toʻgʻri burchak</strong> hosil qilsa — 90.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>130° li burchakning "
                "toʻldiruvchisi qancha?</strong></p>",
        "choices": [
            "Toʻldiruvchisi yoʻq",
            "40°",
            "50°",
            "230°",
        ],
        "correct": "Toʻldiruvchisi yoʻq",
        "explanation": "<p><strong>Toʻldiruvchisi yoʻq.</strong> "
                       "90 − 130 = −40 chiqadi, manfiy burchak esa mavjud emas. "
                       "Toʻldiruvchisi boʻlishi uchun burchak 90° dan kichik "
                       "boʻlishi shart. <strong>50°</strong> — bu uning "
                       "qoʻshnisi (180 − 130).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki chiziq kesishdi va "
                "burchaklar soat yoʻnalishi boʻyicha ∠1, ∠2, ∠3, ∠4 deb "
                "belgilandi.</p><p><strong>Qaysi tenglik har doim "
                "toʻgʻri?</strong></p>",
        "choices": [
            "∠1 = ∠3",
            "∠1 = ∠2",
            "∠1 + ∠3 = 180°",
            "∠2 = ∠3",
        ],
        "correct": "∠1 = ∠3",
        "explanation": "<p><strong>∠1 = ∠3.</strong> Ular qarama-qarshi "
                       "yotgan vertikal burchaklar, demak teng. ∠1 bilan ∠2 esa "
                       "yonma-yon — ularning <strong>yigʻindisi</strong> 180°, "
                       "oʻzlari esa faqat ikkalasi 90° boʻlgandagina teng "
                       "boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Chizmada ikki burchak "
                "teng koʻrinib turibdi. Bu ularning tengligiga yetarli "
                "dalilmi?</strong></p>",
        "choices": [
            "Yoʻq — qoida yoki oʻlchov kerak",
            "Ha, chizma har doim aniq",
            "Ha, agar chizma chizgʻich bilan chizilgan boʻlsa",
            "Faqat oʻtkir burchaklar uchun yetarli",
        ],
        "correct": "Yoʻq — qoida yoki oʻlchov kerak",
        "explanation": "<p><strong>Yoʻq.</strong> Geometriyada «koʻzga shunday "
                       "koʻrindi» dalil emas — chizma qoʻlda chizilgani uchun "
                       "aldashi mumkin. Vertikal burchaklar tengligini biz "
                       "koʻrib emas, <strong>isbotlab</strong> bildik.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>«Vertikal burchaklarning "
                "yigʻindisi 180° ga teng».</strong></p>",
        "choices": [
            "Vertikal burchaklar teng; 180° beradiganlari qoʻshnilari",
            "Vertikal burchaklarning yigʻindisi 90°",
            "Vertikal burchaklarning yigʻindisi 360°",
            "Xato yoʻq, jumla toʻgʻri",
        ],
        "correct": "Vertikal burchaklar teng; 180° beradiganlari qoʻshnilari",
        "explanation": "<p><strong>Vertikal burchaklar teng.</strong> Ular "
                       "faqat ikkalasi ham 90° boʻlgandagina 180° beradi — "
                       "boshqa hollarda yoʻq. Masalan 43° va 43° vertikal "
                       "juftlik, yigʻindisi esa 86°.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Masala: 40° li burchakning "
                "toʻldiruvchisini toping.</p><p><strong>Yechim: "
                "180 − 40 = 140°.</strong></p>",
        "choices": [
            "Toʻldiruvchi 90 dan ayiriladi: 90 − 40 = 50°",
            "Toʻldiruvchi 360 dan ayiriladi: 360 − 40 = 320°",
            "Toʻldiruvchi qoʻshish bilan topiladi: 180 + 40 = 220°",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Toʻldiruvchi 90 dan ayiriladi: 90 − 40 = 50°",
        "explanation": "<p><strong>90 − 40 = 50°.</strong> Toʻldiruvchi burchak "
                       "toʻgʻri burchakni toʻldiradi, yoyiq burchakni emas. "
                       "140° — bu 40° ning <strong>qoʻshnisi</strong>. Ikkala "
                       "son ham «toʻgʻri javob»ga oʻxshaydi, farqni savoldagi "
                       "soʻz belgilaydi.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Bogʻdagi ikki toʻgʻri yoʻlcha bir-birini kesib "
                "oʻtadi. Bogʻbon chorrahaning burchaklarini gul ekish "
                "uchun belgilamoqchi va ulardan bittasini transportir "
                "bilan oʻlchab, 55° ekanini aniqladi.</p>"
                "<p><strong>Qolgan uchta burchak qancha?</strong></p>",
        "choices": [
            "35°, 55° va 35°",
            "55°, 55° va 55°",
            "125°, 55° va 125°",
            "125°, 125° va 125°",
        ],
        "correct": "125°, 55° va 125°",
        "explanation": "<p><strong>125°, 55° va 125°.</strong> Qoʻshnisi "
                       "180 − 55 = 125°; qarama-qarshi yotgani vertikal, demak "
                       "55°; toʻrtinchisi esa 125° ga vertikal, yaʼni 125°. "
                       "Tekshirish: 55 + 125 + 55 + 125 = 360 ✓ Bitta oʻlchov "
                       "butun chorrahani beradi.</p>",
    },
    {
        "text": "<p>Shahar markazidagi ikki koʻcha kesishadi. Yoʻl "
                "belgisini oʻrnatuvchi usta chorrahaning burchaklarini "
                "bilishi kerak. Unga faqat bitta maʼlumot berilgan: "
                "burchaklardan biri oʻz qoʻshnisidan 50° kichik.</p>"
                "<p><strong>Kichik burchak necha gradus?</strong></p>",
        "choices": ["50°", "65°", "75°", "115°"],
        "correct": "65°",
        "explanation": "<p><strong>65°.</strong> x + y = 180 va y − x = 50. "
                       "Qoʻshni burchaklar 180° beradi, demak x + (x + 50) = 180, "
                       "2x = 130, x = 65. Kattasi 115°. Tekshirish: "
                       "65 + 115 = 180 ✓ va 115 − 65 = 50 ✓ Chorrahaning "
                       "toʻrtta burchagi: 65°, 115°, 65°, 115°.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-57 Mashq: Nuqta, chiziq, kesma, nur",
        "description": "20 savol — toʻrt shaklning farqi, belgilash tartibi, "
                       "kesmalarni qoʻshish, oʻrta nuqta va masshtab.",
        "tutorial":    "PM-57:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM57,
    },
    {
        "title":       "PM-58 Mashq: Burchak va uni oʻlchash",
        "description": "20 savol — ∠ABC yozuvi, burchak turlari, transportirning "
                       "ikki shkalasi, burchaklarni qoʻshish va burilishlar.",
        "tutorial":    "PM-58:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM58,
    },
    {
        "title":       "PM-59 Mashq: Burchak juftliklari",
        "description": "20 savol — qoʻshni, toʻldiruvchi va vertikal burchaklar, "
                       "bitta burchakdan toʻrttasi va burchakli tenglamalar.",
        "tutorial":    "PM-59:",
        "subject":     "Matematika",
        "level":       "medium",
        "questions":   Q_PM59,
    },
]
