# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-87, PM-88, PM-89 (chizma va sxema;
harakat 1: tezlik/vaqt/masofa; harakat 2: uchrashuv va quvish).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: uchalasi ham `hard`.

⚠️ `choices` EKRANLANADI — HTML teg yoʻq.
⚠️ Kumulyativ:
   • PM-87 — tasma model, kesma chizma, oʻq sxemasi. ⛔ Tezlik YOʻQ;
   • PM-88 — S = v·t uchligi, birliklar, oʻrtacha tezlik.
     ⛔ Ikki harakatlanuvchi YOʻQ;
   • PM-89 — uchrashuv (v₁ + v₂) va quvish (v₁ − v₂).
     ⛔ Oqim boʻylab harakat kursda umuman yoʻq.
⚠️ Distraktorlar — haqiqiy xatolar: minutni soatga oʻgirmaslik,
   tezliklarning oddiy oʻrtachasi, quvishda qoʻshib yuborish,
   uchrashuvni yoʻlning oʻrtasi deb olish, «qolgani» ni notoʻgʻri
   oʻqish, farqni yoʻqotib teng boʻlish.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_87_89.py --master=prime \\
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
# PM-87 — chizma va sxema
# =====================================================================

Q_PM87 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Masalada butun va uning "
                "boʻlaklari haqida gap ketyapti.</p><p><strong>Qaysi chizma "
                "mos keladi?</strong></p>",
        "choices": [
            "Tasma model",
            "Kesma chizma",
            "Oʻq sxemasi",
            "Doiraviy diagramma",
        ],
        "correct": "Tasma model",
        "explanation": "<p><strong>Tasma model.</strong> Butun va boʻlaklar "
                       "— tasmalar uchun. Kesma chizma yoʻl va uzunlik "
                       "uchun, oʻq sxemasi esa bosqichma-bosqich "
                       "oʻzgarish uchun ishlatiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Chizmadagi "
                "uzunliklar haqida qaysi gap toʻgʻri?</strong></p>",
        "choices": [
            "Uzunlik nisbatga mos boʻlishi shart",
            "Uzunlik ahamiyatsiz, faqat yozuv muhim",
            "Hamma tasmalar teng chizilishi kerak",
            "Uzunlik har doim santimetrda oʻlchanadi",
        ],
        "correct": "Uzunlik nisbatga mos boʻlishi shart",
        "explanation": "<p><strong>Uzunlik nisbatga mos boʻlishi "
                       "shart.</strong> 2x deb belgilangan tasma x dan "
                       "roppa-rosa ikki barobar uzun boʻlsin. Nisbatsiz "
                       "chizma xato javobni ham toʻgʻridek "
                       "koʻrsatadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>Yoʻlning "
                "<strong>1/4</strong> qismi asfalt.</p><p><strong>Qolgani "
                "— yoʻlning ___ qismi.</strong></p>",
        "choices": ["1/4", "1/2", "2/3", "3/4"],
        "correct": "3/4",
        "explanation": "<p><strong>3/4.</strong> Butun 1 ga teng: "
                       "1 − 1/4 = 3/4. Chizmada toʻrtta boʻlakdan "
                       "uchtasi qolgani darrov koʻrinadi. «1/4» — eng "
                       "koʻp uchraydigan xato: «qolgani» soʻzi "
                       "butundan ayirishni talab qiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Masalada «avval yarmi "
                "olindi, keyin yana 5 tasi olindi» deyilgan.</p>"
                "<p><strong>Qaysi chizma mos keladi?</strong></p>",
        "choices": [
            "Tasma model",
            "Kesma chizma",
            "Oʻq sxemasi",
            "Koordinata tekisligi",
        ],
        "correct": "Oʻq sxemasi",
        "explanation": "<p><strong>Oʻq sxemasi.</strong> Bu yerda "
                       "bosqichma-bosqich oʻzgarish bor: x → yarmi "
                       "olindi → 5 tasi olindi → qoldi. Voqealar "
                       "ketma-ketligini oʻqlar bilan yozish "
                       "qulay.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Ikki sonning yigʻindisi 50, farqi "
                "10.</p><p><strong>Kichik son qanday?</strong></p>",
        "choices": ["15", "20", "25", "30"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> Ortiqchani qirqamiz: "
                       "(50 − 10) ÷ 2 = 20. Kattasi 20 + 10 = 30. "
                       "Tekshirish: 20 + 30 = 50 ✓ va 30 − 20 = 10 ✓ "
                       "<strong>25</strong> — 50 ni teng ikkiga "
                       "boʻlganda chiqadi va farqni yoʻqotadi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Ikki doʻst 76 000 soʻmni "
                "boʻlishdi. Biri ikkinchisidan 8 000 soʻm koʻp oldi.</p>"
                "<p><strong>Kattasi qancha oldi?</strong></p>",
        "choices": ["34 000 soʻm", "38 000 soʻm", "42 000 soʻm",
                    "46 000 soʻm"],
        "correct": "42 000 soʻm",
        "explanation": "<p><strong>42 000 soʻm.</strong> Ortiqchani "
                       "qirqamiz: (76 000 − 8 000) ÷ 2 = 34 000 — "
                       "kichigi. Kattasi 34 000 + 8 000 = 42 000. "
                       "Tekshirish: 34 000 + 42 000 = 76 000 ✓ "
                       "<strong>34 000</strong> — kichik ulush, savol "
                       "kattasini soʻragan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki qutida jami 60 ta ruchka "
                "bor. Birinchi qutida ikkinchisidan 4 marta koʻp.</p>"
                "<p><strong>Birinchi qutida nechta ruchka bor?</strong></p>",
        "choices": ["12 ta", "15 ta", "45 ta", "48 ta"],
        "correct": "48 ta",
        "explanation": "<p><strong>48 ta.</strong> Chizmada jami beshta "
                       "teng boʻlak (1 + 4): 60 ÷ 5 = 12 — ikkinchi "
                       "quti. Birinchisi 4 × 12 = 48. Tekshirish: "
                       "12 + 48 = 60 ✓ <strong>12</strong> — ikkinchi "
                       "quti, <strong>15</strong> esa 60 ni 4 ga "
                       "boʻlganda chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Yoʻlning uchdan bir qismi "
                "koʻtarilish, qolgani tekislik. Tekislik koʻtarilishdan "
                "8 km uzun.</p><p><strong>Jami yoʻl necha "
                "kilometr?</strong></p>",
        "choices": ["12 km", "16 km", "24 km", "32 km"],
        "correct": "24 km",
        "explanation": "<p><strong>24 km.</strong> Koʻtarilish — 1 boʻlak, "
                       "tekislik — 2 boʻlak, farqi 1 boʻlak. Demak "
                       "1 boʻlak = 8 km va jami 3 × 8 = 24 km. "
                       "Tekshirish: 8 va 16, farq 8 ✓ "
                       "<strong>16</strong> — faqat tekislik qismi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir sonni 4 ga koʻpaytirib, "
                "7 ni ayirsak, 45 chiqadi.</p><p><strong>Bu son "
                "qanday?</strong></p>",
        "choices": ["9", "13", "17", "23"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> Sxema: x → ×4 → 4x → −7 → "
                       "45. Demak 4x − 7 = 45 → 4x = 52 → x = 13. "
                       "Tekshirish sxema boʻylab: 13 × 4 = 52, "
                       "52 − 7 = 45 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Qutida olmalar bor edi. Avval "
                "yarmi olindi, keyin yana 3 tasi olindi va 12 ta "
                "qoldi.</p><p><strong>Boshida nechta olma bor "
                "edi?</strong></p>",
        "choices": ["24 ta", "27 ta", "30 ta", "36 ta"],
        "correct": "30 ta",
        "explanation": "<p><strong>30 ta.</strong> Sxema: x → yarmi olindi "
                       "→ x ÷ 2 → 3 tasi olindi → 12. Demak "
                       "x ÷ 2 − 3 = 12 → x ÷ 2 = 15 → x = 30. "
                       "Tekshirish oldinga: 30 → 15 → 12 ✓ "
                       "<strong>24</strong> — 12 ni ikkilantirib, "
                       "3 ni notoʻgʻri qoʻshganda chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Uch sinf birgalikda 240 ta "
                "koʻchat ekdi. B sinfi A dan 2 marta koʻp, V sinfi A dan "
                "40 ta koʻp ekdi.</p><p><strong>A sinfi nechta koʻchat "
                "ekdi?</strong></p>",
        "choices": ["40 ta", "50 ta", "60 ta", "80 ta"],
        "correct": "50 ta",
        "explanation": "<p><strong>50 ta.</strong> Hamma narsa A ga qarab "
                       "aytilgan: x + 2x + (x + 40) = 240 → "
                       "4x + 40 = 240 → 4x = 200 → x = 50. B — 100, "
                       "V — 90. Tekshirish: 50 + 100 + 90 = 240 ✓ "
                       "<strong>60</strong> — 240 ni 4 ga boʻlib, "
                       "40 ni unutganda chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Kitobning beshdan bir qismi "
                "oʻqildi. Oʻqilmagan qism oʻqilganidan 90 bet koʻp.</p>"
                "<p><strong>Kitobda nechta bet bor?</strong></p>",
        "choices": ["120", "150", "180", "450"],
        "correct": "150",
        "explanation": "<p><strong>150.</strong> Oʻqilgan — 1 boʻlak, "
                       "oʻqilmagan — 4 boʻlak, farqi 3 boʻlak. Demak "
                       "3 boʻlak = 90 bet, 1 boʻlak = 30 bet, jami "
                       "5 × 30 = 150. Tekshirish: 30 oʻqilgan, "
                       "120 qolgan, farq 90 ✓ <strong>450</strong> — "
                       "90 ni 5 ga koʻpaytirganda chiqadi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki son berilgan: "
                "yigʻindisi 90, farqi 20.</p><p><strong>Qaysi yoʻl "
                "toʻgʻri?</strong></p>",
        "choices": [
            "90 ÷ 2 = 45, demak sonlar 45 va 45",
            "(90 − 20) ÷ 2 = 35, demak sonlar 35 va 55",
            "(90 + 20) ÷ 2 = 55, demak sonlar 55 va 75",
            "90 − 20 = 70, demak sonlar 20 va 70",
        ],
        "correct": "(90 − 20) ÷ 2 = 35, demak sonlar 35 va 55",
        "explanation": "<p><strong>(90 − 20) ÷ 2 = 35.</strong> Ortiqchani "
                       "qirqib, qolganini teng boʻlamiz. Tekshirish: "
                       "35 + 55 = 90 ✓ va 55 − 35 = 20 ✓ Birinchi "
                       "variant farqni yoʻqotadi, oxirgisi esa ikkala "
                       "shartni ham buzadi (20 + 70 = 90, lekin farq "
                       "50).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Chizma nima "
                "qiladi?</strong></p>",
        "choices": [
            "Tenglamaning oʻrnini bosadi",
            "Tenglamani topib beradi",
            "Javobni oʻzi hisoblab beradi",
            "Tekshirish zaruratini yoʻqotadi",
        ],
        "correct": "Tenglamani topib beradi",
        "explanation": "<p><strong>Tenglamani topib beradi.</strong> Chizma "
                       "bogʻlanishlarni uzunlikka aylantiradi va "
                       "tenglama shundan koʻrinadi. Lekin hisoblashni "
                       "ham, tekshirishni ham baribir oʻzingiz "
                       "qilasiz.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bogʻning ikkidan bir "
                "qismiga olma, qolganiga oʻrik ekilgan.</p><p><strong>Olma "
                "va oʻrik qismlari qanday nisbatda?</strong></p>",
        "choices": [
            "Olma 2 marta koʻp",
            "Oʻrik 2 marta koʻp",
            "Ular teng",
            "Oʻrik 3 marta koʻp",
        ],
        "correct": "Ular teng",
        "explanation": "<p><strong>Ular teng.</strong> Yarmi olma boʻlsa, "
                       "qolgani ham yarmi: 1 − 1/2 = 1/2. Bu — "
                       "«qolgani» qoidasining eng oddiy holi va uni "
                       "chizmada bir qarashda koʻrish mumkin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻq sxemasi bilan "
                "yechilgan masalada javob topildi.</p><p><strong>Uni qanday "
                "tekshirish eng qulay?</strong></p>",
        "choices": [
            "Javobni sxema boshiga qoʻyib, oʻqlar boʻylab yurish",
            "Tenglamani qaytadan yechish",
            "Javobni ikkiga boʻlib koʻrish",
            "Chizmani qaytadan chizish",
        ],
        "correct": "Javobni sxema boshiga qoʻyib, oʻqlar boʻylab yurish",
        "explanation": "<p><strong>Javobni sxema boshiga qoʻyib, oʻqlar "
                       "boʻylab yurish.</strong> Oxirida masaladagi son "
                       "chiqsa, javob toʻgʻri. Tenglamani qayta yechish "
                       "xuddi oʻsha xatoni takrorlash xavfini "
                       "tugʻdiradi — tekshirish boshqa yoʻldan borishi "
                       "kerak.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>«Yoʻlning uchdan bir qismi "
                "avtobusda bosildi» — oʻquvchi chizmani ikkita teng "
                "boʻlakka boʻlib, biriga «avtobus», ikkinchisiga «qolgani» "
                "deb yozdi.</p><p><strong>Nima notoʻgʻri?</strong></p>",
        "choices": [
            "Chizma uchta teng boʻlakka boʻlinishi kerak edi",
            "Chizma umuman kerak emas edi",
            "Boʻlaklar nomlanmagan",
            "Xato yoʻq, chizma toʻgʻri",
        ],
        "correct": "Chizma uchta teng boʻlakka boʻlinishi kerak edi",
        "explanation": "<p><strong>Uchta teng boʻlakka.</strong> «Uchdan "
                       "bir qism» degani butun uchga boʻlinadi: bittasi "
                       "avtobus, <strong>ikkitasi</strong> qolgani. "
                       "Ikkiga boʻlish qolgan qismni ham 1/3 qilib "
                       "koʻrsatadi va bu xato javobga olib "
                       "keladi.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Ikki qutida jami "
                "72 ta olma. Birinchisida ikkinchisidan 2 marta koʻp. Har "
                "birida nechtadan?</strong></p>",
        "choices": [
            "72 ÷ 2 = 36, demak 36 va 36",
            "72 ÷ 3 = 24, demak 24 va 48",
            "72 ÷ 2 = 36, demak 36 va 72",
            "72 − 2 = 70, demak 2 va 70",
        ],
        "correct": "72 ÷ 3 = 24, demak 24 va 48",
        "explanation": "<p><strong>72 ÷ 3 = 24.</strong> Chizmada jami "
                       "uchta teng boʻlak (1 + 2). Bitta boʻlak 24, "
                       "demak ikkinchi quti 24, birinchisi 48. "
                       "Tekshirish: 24 + 48 = 72 ✓ va 48 ÷ 24 = 2 ✓ "
                       "«36 va 72» varianti yigʻindini 108 qilib "
                       "yuboradi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Afsona va Dilnoza birgalikda "
                "108 ta gul terishdi. Afsona Dilnozadan 12 ta koʻp "
                "terdi.</p><p><strong>Dilnoza nechta gul terdi?</strong>"
                "</p>",
        "choices": ["42 ta", "48 ta", "54 ta", "60 ta"],
        "correct": "48 ta",
        "explanation": "<p><strong>48 ta.</strong> Ortiqchani qirqamiz: "
                       "(108 − 12) ÷ 2 = 48 — Dilnoza. Afsona "
                       "48 + 12 = 60. Tekshirish: 48 + 60 = 108 ✓ va "
                       "60 − 48 = 12 ✓ <strong>54</strong> — 108 ni "
                       "teng ikkiga boʻlganda chiqadi va 12 talik "
                       "farqni yoʻqotadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bekzodda bir necha marka bor "
                "edi. U ularning yarmini doʻstiga berdi, keyin 7 tasini "
                "yoʻqotdi va 18 tasi qoldi.</p><p><strong>Boshida nechta "
                "marka bor edi?</strong></p>",
        "choices": ["36 ta", "44 ta", "50 ta", "56 ta"],
        "correct": "50 ta",
        "explanation": "<p><strong>50 ta.</strong> Sxema: x → yarmi berildi "
                       "→ x ÷ 2 → 7 tasi yoʻqoldi → 18. Demak "
                       "x ÷ 2 − 7 = 18 → x ÷ 2 = 25 → x = 50. "
                       "Tekshirish oldinga: 50 → 25 → 18 ✓ "
                       "<strong>36</strong> — 18 ni ikkilantirganda "
                       "chiqadi, yaʼni 7 tani hisobga olmaganda.</p>",
    },
]


# =====================================================================
# PM-88 — harakat masalalari 1
# =====================================================================

Q_PM88 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>Mashina 80 km/soat bilan "
                "3 soat yurdi. Qancha yoʻl bosdi?</strong></p>",
        "choices": ["24 km", "83 km", "240 km", "480 km"],
        "correct": "240 km",
        "explanation": "<p><strong>240 km.</strong> S = v × t = 80 × 3 = "
                       "240. <strong>83</strong> — tezlik bilan vaqt "
                       "qoʻshib yuborilganda chiqadi; bu ikki har xil "
                       "miqdor, ular qoʻshilmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Piyoda 15 km yoʻlni 3 soatda "
                "bosdi. Tezligi qancha?</strong></p>",
        "choices": ["3 km/soat", "5 km/soat", "12 km/soat", "45 km/soat"],
        "correct": "5 km/soat",
        "explanation": "<p><strong>5 km/soat.</strong> v = S ÷ t = "
                       "15 ÷ 3 = 5. <strong>45</strong> — boʻlish "
                       "oʻrniga koʻpaytirilganda chiqadi. Birlikning "
                       "oʻzi formulani aytib turadi: km/soat — kilometr "
                       "boʻlingan soat.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>120 km yoʻlni 60 km/soat "
                "bilan bosishga qancha vaqt ketadi?</strong></p>",
        "choices": ["0,5 soat", "2 soat", "60 soat", "180 soat"],
        "correct": "2 soat",
        "explanation": "<p><strong>2 soat.</strong> t = S ÷ v = "
                       "120 ÷ 60 = 2. <strong>0,5</strong> — boʻlish "
                       "teskari qilinganda (60 ÷ 120) chiqadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>30 minut — bu "
                "___ soat.</strong></p>",
        "choices": ["0,3", "0,5", "0,30", "3"],
        "correct": "0,5",
        "explanation": "<p><strong>0,5.</strong> 30 ÷ 60 = 0,5. "
                       "<strong>0,3</strong> va <strong>0,30</strong> — "
                       "vaqtni oʻnlik sanoq deb oʻylaganda chiqadi, "
                       "lekin soatda 100 emas, 60 minut bor.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>1 soat "
                "30 minut — bu ___ soat.</strong></p>",
        "choices": ["1,3", "1,5", "1,30", "90"],
        "correct": "1,5",
        "explanation": "<p><strong>1,5.</strong> 60 + 30 = 90 minut, "
                       "90 ÷ 60 = 1,5 soat. <strong>1,3</strong> — eng "
                       "koʻp uchraydigan xato; <strong>90</strong> esa "
                       "toʻgʻri son, lekin soatda emas, minutda.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>Velosipedchi 16 km/soat bilan "
                "45 minut yurdi. Qancha yoʻl bosdi?</strong></p>",
        "choices": ["7,2 km", "12 km", "36 km", "720 km"],
        "correct": "12 km",
        "explanation": "<p><strong>12 km.</strong> 45 minut = 45 ÷ 60 = "
                       "0,75 soat. S = 16 × 0,75 = 12 km. "
                       "<strong>720</strong> — 16 × 45 qilinganda "
                       "chiqadi, yaʼni birlik moslanmaganda; bunday "
                       "javob darrov mantiqsizligi bilan koʻzga "
                       "tashlanadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Afsona 2 km yoʻlni "
                "30 minutda piyoda bosdi. Tezligi necha km/soat?</strong>"
                "</p>",
        "choices": ["1 km/soat", "4 km/soat", "15 km/soat", "60 km/soat"],
        "correct": "4 km/soat",
        "explanation": "<p><strong>4 km/soat.</strong> 30 minut = 0,5 soat, "
                       "v = 2 ÷ 0,5 = 4 km/soat. <strong>1</strong> — "
                       "2 ÷ 2 qilinganda; <strong>15</strong> — 30 ÷ 2 "
                       "qilinganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>72 km/soat necha m/s ga "
                "teng?</strong></p>",
        "choices": ["12 m/s", "20 m/s", "72 m/s", "259 m/s"],
        "correct": "20 m/s",
        "explanation": "<p><strong>20 m/s.</strong> km/soatdan m/s ga "
                       "oʻtish uchun 3,6 ga boʻlinadi: 72 ÷ 3,6 = 20. "
                       "Tekshirish: 20 m/s × 3600 s = 72 000 m = "
                       "72 km ✓ <strong>259</strong> — 3,6 ga "
                       "koʻpaytirilganda, yaʼni teskari yoʻnalishda "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Poyezd 12 km yoʻlni "
                "10 minutda bosdi. Tezligi necha km/soat?</strong></p>",
        "choices": ["1,2 km/soat", "22 km/soat", "72 km/soat",
                    "120 km/soat"],
        "correct": "72 km/soat",
        "explanation": "<p><strong>72 km/soat.</strong> 10 minut = "
                       "10 ÷ 60 = 1/6 soat. v = 12 ÷ (1/6) = 12 × 6 = "
                       "72 km/soat. <strong>1,2</strong> — 12 ni 10 ga "
                       "boʻlganda, yaʼni minutni soatga "
                       "oʻgirmaganda.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Mashina 2 soat 90 km/soat bilan, keyin "
                "3 soat 70 km/soat bilan yurdi.</p><p><strong>Jami qancha "
                "yoʻl bosdi?</strong></p>",
        "choices": ["160 km", "320 km", "390 km", "400 km"],
        "correct": "390 km",
        "explanation": "<p><strong>390 km.</strong> Boʻlaklar boʻyicha: "
                       "90 × 2 = 180 km va 70 × 3 = 210 km, jami "
                       "180 + 210 = 390. <strong>160</strong> — "
                       "tezliklar qoʻshib yuborilganda (90 + 70) "
                       "chiqadi; tezliklar qoʻshilmaydi, masofalar "
                       "qoʻshiladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Poyezd 3 soat 100 km/soat bilan, keyin "
                "2 soat 75 km/soat bilan yurdi.</p><p><strong>Oʻrtacha "
                "tezligi qancha?</strong></p>",
        "choices": ["80 km/soat", "87,5 km/soat", "90 km/soat",
                    "175 km/soat"],
        "correct": "90 km/soat",
        "explanation": "<p><strong>90 km/soat.</strong> Masofa: 300 + 150 = "
                       "450 km. Vaqt: 5 soat. 450 ÷ 5 = 90. "
                       "<strong>87,5</strong> — ikki tezlikning oddiy "
                       "oʻrtachasi (100 + 75) ÷ 2; u faqat vaqtlar teng "
                       "boʻlganda toʻgʻri boʻlardi, bu yerda esa "
                       "3 soat va 2 soat.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Sherbek 9 km yoʻlni "
                "36 minutda velosipedda bosdi. Tezligi necha "
                "km/soat?</strong></p>",
        "choices": ["0,25 km/soat", "4 km/soat", "15 km/soat",
                    "324 km/soat"],
        "correct": "15 km/soat",
        "explanation": "<p><strong>15 km/soat.</strong> 36 minut = "
                       "36 ÷ 60 = 0,6 soat. v = 9 ÷ 0,6 = 15 km/soat. "
                       "Tekshirish: 15 × 0,6 = 9 ✓ <strong>0,25</strong> "
                       "— 9 ni 36 ga boʻlganda chiqadi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Mashina borishda "
                "80 km/soat, qaytishda oʻsha yoʻldan 20 km/soat bilan "
                "yurdi.</p><p><strong>Butun safar davomidagi oʻrtacha "
                "tezlik haqida nima deyish mumkin?</strong></p>",
        "choices": [
            "U roppa-rosa 50 km/soat",
            "U 50 dan kichik",
            "U 50 dan katta",
            "Uni hisoblab boʻlmaydi",
        ],
        "correct": "U 50 dan kichik",
        "explanation": "<p><strong>U 50 dan kichik.</strong> Sekin "
                       "boʻlakda koʻproq vaqt oʻtadi, shuning uchun "
                       "oʻrtacha tezlik har doim sekin tomonga "
                       "tortiladi. Aniq hisob: 100 km lik yoʻl uchun "
                       "1,25 + 5 = 6,25 soat, 200 ÷ 6,25 = 32 km/soat "
                       "— 50 dan ancha kichik.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi holda "
                "oʻrtacha tezlik ikki tezlikning oddiy oʻrtachasiga teng "
                "boʻladi?</strong></p>",
        "choices": [
            "Masofalar teng boʻlganda",
            "Vaqtlar teng boʻlganda",
            "Har doim",
            "Hech qachon",
        ],
        "correct": "Vaqtlar teng boʻlganda",
        "explanation": "<p><strong>Vaqtlar teng boʻlganda.</strong> Shunda "
                       "ikkala tezlik oʻrtachaga bir xil «ogʻirlik» "
                       "bilan taʼsir qiladi. Masofalar teng boʻlganda "
                       "esa sekin boʻlakda koʻproq vaqt ketadi va "
                       "oʻrtacha sekin tomonga siljiydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Yoʻl ikki boʻlakdan "
                "iborat: 60 km/soat va 40 km/soat.</p><p><strong>Qaysi "
                "amal maʼnoga ega?</strong></p>",
        "choices": [
            "Tezliklarni qoʻshish: 100 km/soat",
            "Masofalarni qoʻshish",
            "Vaqtlarni koʻpaytirish",
            "Tezliklarni koʻpaytirish",
        ],
        "correct": "Masofalarni qoʻshish",
        "explanation": "<p><strong>Masofalarni qoʻshish.</strong> Har bir "
                       "boʻlakning masofasi alohida hisoblanadi va "
                       "qoʻshiladi. <strong>100 km/soat</strong> degan "
                       "tezlik bu safarda hech qachon boʻlmagan — "
                       "tezliklar qoʻshilmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Masalada «butun safar "
                "davomida oʻrtacha tezlik» soʻralgan va yoʻlda 40 minutlik "
                "dam olish boʻlgan.</p><p><strong>Dam olish vaqti bilan "
                "nima qilinadi?</strong></p>",
        "choices": [
            "Jami vaqtga qoʻshiladi",
            "Hisobga olinmaydi",
            "Jami vaqtdan ayiriladi",
            "Masofaga qoʻshiladi",
        ],
        "correct": "Jami vaqtga qoʻshiladi",
        "explanation": "<p><strong>Jami vaqtga qoʻshiladi.</strong> «Butun "
                       "safar» degani toʻxtash bilan birga. Dam olish "
                       "masofaga hech narsa qoʻshmaydi, lekin vaqtni "
                       "uzaytiradi va shu bilan oʻrtacha tezlikni "
                       "pasaytiradi. «Harakat davomida» deyilsa edi, "
                       "u hisobga olinmasdi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>«Velosipedchi 14 km/soat "
                "bilan 30 minut yurdi» — oʻquvchi yozdi: "
                "«S = 14 × 30 = 420 km».</p><p><strong>Nima "
                "notoʻgʻri?</strong></p>",
        "choices": [
            "Formula notoʻgʻri tanlangan",
            "Vaqt soatga oʻgirilmagan",
            "Tezlik m/s ga oʻgirilmagan",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Vaqt soatga oʻgirilmagan",
        "explanation": "<p><strong>Vaqt soatga oʻgirilmagan.</strong> "
                       "Toʻgʻrisi: 30 minut = 0,5 soat, "
                       "S = 14 × 0,5 = 7 km. Formula toʻgʻri edi. "
                       "420 km — velosipedda yarim soatda bosib "
                       "boʻlmaydigan masofa; javobning mantiqiyligini "
                       "tekshirish shuni darrov koʻrsatadi.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Mashina 60 km ni "
                "60 km/soat bilan bordi va oʻsha 60 km ni 20 km/soat bilan "
                "qaytdi. Oʻrtacha tezligi qancha?</strong></p>",
        "choices": [
            "(60 + 20) ÷ 2 = 40 km/soat",
            "120 ÷ 4 = 30 km/soat",
            "120 ÷ 2 = 60 km/soat",
            "60 − 20 = 40 km/soat",
        ],
        "correct": "120 ÷ 4 = 30 km/soat",
        "explanation": "<p><strong>120 ÷ 4 = 30 km/soat.</strong> Borish "
                       "1 soat, qaytish 60 ÷ 20 = 3 soat, jami 4 soat "
                       "va 120 km. <strong>40</strong> — tezliklarning "
                       "oddiy oʻrtachasi; u sekin boʻlakda uch barobar "
                       "koʻp vaqt oʻtganini hisobga olmaydi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Dilnoza maktabgacha 1,5 km "
                "yoʻlni 18 minutda piyoda bosadi.</p><p><strong>Uning "
                "tezligi necha km/soat?</strong></p>",
        "choices": ["0,08 km/soat", "3 km/soat", "5 km/soat",
                    "27 km/soat"],
        "correct": "5 km/soat",
        "explanation": "<p><strong>5 km/soat.</strong> 18 minut = 18 ÷ 60 = "
                       "0,3 soat. v = 1,5 ÷ 0,3 = 5 km/soat. "
                       "Tekshirish: 5 × 0,3 = 1,5 ✓ "
                       "<strong>0,08</strong> — 1,5 ni 18 ga "
                       "boʻlganda chiqadi, yaʼni birlik "
                       "moslanmaganda.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bekzod 10 km/soat bilan 1 soat "
                "velosiped uchdi, keyin 30 minut dam oldi, soʻng "
                "6 km/soat bilan yana 30 minut yurdi.</p><p><strong>Butun "
                "safar davomida oʻrtacha tezligi qancha?</strong></p>",
        "choices": ["6,5 km/soat", "8 km/soat", "8,7 km/soat",
                    "13 km/soat"],
        "correct": "6,5 km/soat",
        "explanation": "<p><strong>6,5 km/soat.</strong> Masofa: "
                       "10 × 1 = 10 km va 6 × 0,5 = 3 km, jami 13 km. "
                       "Vaqt: 1 + 0,5 + 0,5 = 2 soat (dam olish ham "
                       "kiradi). 13 ÷ 2 = 6,5. <strong>8,7</strong> — "
                       "dam olish hisobga olinmaganda (13 ÷ 1,5); "
                       "<strong>8</strong> esa ikki tezlikning oddiy "
                       "oʻrtachasi.</p>",
    },
]


# =====================================================================
# PM-89 — harakat masalalari 2
# =====================================================================

Q_PM89 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>Ikki mashina bir-biriga qarab "
                "kelmoqda: 50 va 70 km/soat.</p><p><strong>Yaqinlashish "
                "tezligi qancha?</strong></p>",
        "choices": ["20 km/soat", "60 km/soat", "120 km/soat",
                    "3500 km/soat"],
        "correct": "120 km/soat",
        "explanation": "<p><strong>120 km/soat.</strong> Qarama-qarshi "
                       "harakatda tezliklar qoʻshiladi: 50 + 70 = 120. "
                       "Har soatda ora shuncha kamayadi. "
                       "<strong>20</strong> — ayirilganda chiqadi, "
                       "bu esa quvish holiga tegishli.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Bir yoʻnalishda ketayotgan ikki "
                "mashina: 90 va 60 km/soat.</p><p><strong>Farq tezligi "
                "qancha?</strong></p>",
        "choices": ["30 km/soat", "75 km/soat", "150 km/soat",
                    "5400 km/soat"],
        "correct": "30 km/soat",
        "explanation": "<p><strong>30 km/soat.</strong> Bir yoʻnalishda "
                       "tezliklar ayiriladi: 90 − 60 = 30. Orqadagi "
                       "mashina har soatda 30 km yaqinlashadi. "
                       "<strong>150</strong> — qoʻshilganda chiqadi va "
                       "u qarama-qarshi harakatga tegishli.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Ikki shahar orasi 240 km. Ikki poyezd "
                "qarshi chiqdi, yaqinlashish tezligi 120 km/soat.</p>"
                "<p><strong>Necha soatdan keyin uchrashadi?</strong></p>",
        "choices": ["1 soat", "2 soat", "3 soat", "4 soat"],
        "correct": "2 soat",
        "explanation": "<p><strong>2 soat.</strong> t = ora ÷ yaqinlashish "
                       "tezligi = 240 ÷ 120 = 2 soat.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki mashina bir "
                "vaqtda qarshi chiqdi, biri tezroq.</p><p><strong>Ular "
                "qayerda uchrashadi?</strong></p>",
        "choices": [
            "Yoʻlning roppa-rosa oʻrtasida",
            "Tez mashina chiqqan shaharga yaqinroq",
            "Sekin mashina chiqqan shaharga yaqinroq",
            "Buni aniqlab boʻlmaydi",
        ],
        "correct": "Sekin mashina chiqqan shaharga yaqinroq",
        "explanation": "<p><strong>Sekin mashina chiqqan shaharga "
                       "yaqinroq.</strong> Vaqt ikkalasi uchun bir xil, "
                       "shuning uchun tez mashina koʻproq yoʻl bosadi "
                       "va uchrashuv nuqtasi undan uzoqroqda — yaʼni "
                       "sekin mashinaning shahriga yaqin boʻladi. "
                       "Oʻrtada uchrashish faqat tezliklar teng "
                       "boʻlganda.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Harakat "
                "masalasida qaysi savolni birinchi berish kerak?</strong>"
                "</p>",
        "choices": [
            "Ora har soatda qanchaga oʻzgaradi?",
            "Kim tezroq ketyapti?",
            "Yoʻlning oʻrtasi qayerda?",
            "Kim oldin chiqqan?",
        ],
        "correct": "Ora har soatda qanchaga oʻzgaradi?",
        "explanation": "<p><strong>Ora har soatda qanchaga "
                       "oʻzgaradi?</strong> Bu savol formulani oʻzi "
                       "beradi: qarshi yursa qoʻshiladi, birga ketsa "
                       "ayiriladi. Keyin masofa shu songa "
                       "boʻlinadi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Ikki qishloq orasi 36 km. Ikki "
                "piyoda bir vaqtda bir-biriga qarab chiqdi: 5 va "
                "4 km/soat.</p><p><strong>Necha soatdan keyin "
                "uchrashadi?</strong></p>",
        "choices": ["2 soat", "4 soat", "6 soat", "9 soat"],
        "correct": "4 soat",
        "explanation": "<p><strong>4 soat.</strong> Yaqinlashish tezligi "
                       "5 + 4 = 9 km/soat. t = 36 ÷ 9 = 4. Tekshirish: "
                       "20 + 16 = 36 ✓ <strong>9</strong> — 36 ni "
                       "faqat 4 ga boʻlganda chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki shahar orasi 420 km. Ikki "
                "avtobus qarshi chiqib 3 soatda uchrashdi. Biri "
                "80 km/soat bilan yurgan.</p><p><strong>Ikkinchisining "
                "tezligi qancha?</strong></p>",
        "choices": ["50 km/soat", "60 km/soat", "70 km/soat",
                    "140 km/soat"],
        "correct": "60 km/soat",
        "explanation": "<p><strong>60 km/soat.</strong> Yaqinlashish tezligi "
                       "420 ÷ 3 = 140 km/soat. Demak 140 − 80 = 60. "
                       "Tekshirish: 240 + 180 = 420 ✓ "
                       "<strong>140</strong> — ikkalasining yigʻindisi, "
                       "bitta mashinaning tezligi emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Mashina 50 km/soat bilan "
                "ketmoqda. Uning ortidan 30 km naridan 80 km/soat bilan "
                "ikkinchi mashina chiqdi.</p><p><strong>Qachon quvib "
                "yetadi?</strong></p>",
        "choices": ["0,23 soat", "0,6 soat", "1 soat", "1,6 soat"],
        "correct": "1 soat",
        "explanation": "<p><strong>1 soat.</strong> Farq tezligi "
                       "80 − 50 = 30 km/soat. t = 30 ÷ 30 = 1 soat. "
                       "Tekshirish: birinchisi 50, ikkinchisi 80 km "
                       "yurdi; 30 + 50 = 80 ✓ <strong>0,23</strong> — "
                       "tezliklar qoʻshilganda (30 ÷ 130) chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki shahar orasi 300 km. Ikki "
                "poyezd qarshi chiqdi: 70 va 80 km/soat.</p>"
                "<p><strong>Uchrashguncha tez poyezd qancha yoʻl "
                "bosadi?</strong></p>",
        "choices": ["140 km", "150 km", "160 km", "180 km"],
        "correct": "160 km",
        "explanation": "<p><strong>160 km.</strong> Yaqinlashish tezligi "
                       "70 + 80 = 150, t = 300 ÷ 150 = 2 soat. Tez "
                       "poyezd 80 × 2 = 160 km bosadi. Tekshirish: "
                       "140 + 160 = 300 ✓ <strong>150</strong> — "
                       "yoʻlning oʻrtasi, lekin uchrashuv oʻrtada "
                       "emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sherbek 6 km/soat bilan piyoda "
                "chiqdi. 1 soatdan keyin Jasur oʻsha yoʻldan 15 km/soat "
                "bilan velosipedda ortidan chiqdi.</p><p><strong>Jasur "
                "necha soatdan keyin quvib yetadi?</strong></p>",
        "choices": ["0,29 soat", "0,4 soat", "0,67 soat", "1,5 soat"],
        "correct": "0,67 soat",
        "explanation": "<p><strong>0,67 soat</strong> (taxminan 40 minut). "
                       "Sherbekning ustunligi 6 × 1 = 6 km. Farq "
                       "tezligi 15 − 6 = 9 km/soat. t = 6 ÷ 9 = "
                       "2/3 ≈ 0,67 soat. Tekshirish: Sherbek "
                       "5/3 soatda 10 km, Jasur 2/3 soatda 10 km ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki velosipedchi bir joydan "
                "bir vaqtda qarama-qarshi tomonga chiqdi: 12 va "
                "18 km/soat.</p><p><strong>3 soatdan keyin oralari qancha "
                "boʻladi?</strong></p>",
        "choices": ["18 km", "36 km", "54 km", "90 km"],
        "correct": "90 km",
        "explanation": "<p><strong>90 km.</strong> Bu safar ora ortadi. "
                       "Uzoqlashish tezligi 12 + 18 = 30 km/soat, "
                       "demak 30 × 3 = 90 km. Qoʻshish qoidasi "
                       "uzoqlashishda ham ishlaydi. <strong>18</strong> "
                       "— farq tezligi bilan hisoblanganda "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki shahar orasi 350 km. "
                "Birinchisidan 60 km/soat bilan mashina chiqdi. Ayni "
                "paytda ikkinchisidan 80 km/soat bilan qarshi mashina "
                "chiqdi.</p><p><strong>Uchrashuv joyi birinchi shahardan "
                "qancha narida?</strong></p>",
        "choices": ["120 km", "150 km", "175 km", "200 km"],
        "correct": "150 km",
        "explanation": "<p><strong>150 km.</strong> Yaqinlashish tezligi "
                       "60 + 80 = 140, t = 350 ÷ 140 = 2,5 soat. "
                       "Birinchi mashina 60 × 2,5 = 150 km bosadi. "
                       "Tekshirish: 150 + 200 = 350 ✓ "
                       "<strong>175</strong> — yoʻlning oʻrtasi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qachon "
                "tezliklar ayiriladi?</strong></p>",
        "choices": [
            "Ikki jism bir-biriga qarab yurganda",
            "Ikki jism bir yoʻnalishda yurganda",
            "Ikki jism qarama-qarshi tomonga uzoqlashganda",
            "Har doim",
        ],
        "correct": "Ikki jism bir yoʻnalishda yurganda",
        "explanation": "<p><strong>Bir yoʻnalishda yurganda.</strong> "
                       "Qochuvchi ham oldinga siljib boradi, shuning "
                       "uchun ora faqat tezliklar farqi qadar "
                       "kamayadi. Qarama-qarshi harakatda ham, "
                       "uzoqlashishda ham tezliklar qoʻshiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Quvish masalasida farq "
                "tezligi manfiy chiqdi.</p><p><strong>Bu nimani "
                "bildiradi?</strong></p>",
        "choices": [
            "Hisobda xato bor",
            "Quvuvchi sekinroq — u hech qachon yetib ololmaydi",
            "Ular allaqachon uchrashgan",
            "Masofani ikkiga boʻlish kerak",
        ],
        "correct": "Quvuvchi sekinroq — u hech qachon yetib ololmaydi",
        "explanation": "<p><strong>Quvuvchi sekinroq.</strong> Ayirish "
                       "tartibi toʻgʻri boʻlsa (quvuvchi − qochuvchi) "
                       "va natija manfiy chiqsa, ora ortib boradi. "
                       "Manfiy javob shuni aytadi — bu xato emas, "
                       "maʼlumot.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki poyezd bir vaqtda "
                "qarshi chiqib uchrashdi.</p><p><strong>Ular haqida qaysi "
                "gap har doim toʻgʻri?</strong></p>",
        "choices": [
            "Bosgan masofalari teng",
            "Yoʻlda boʻlgan vaqtlari teng",
            "Tezliklari teng",
            "Uchrashuv oʻrtada boʻlgan",
        ],
        "correct": "Yoʻlda boʻlgan vaqtlari teng",
        "explanation": "<p><strong>Yoʻlda boʻlgan vaqtlari teng.</strong> "
                       "Bir vaqtda chiqib bir vaqtda uchrashgan — "
                       "demak vaqt bir xil. Masofa esa tezlikka qarab "
                       "har xil boʻladi; qolgan uch gap faqat "
                       "tezliklar teng boʻlgandagina toʻgʻri.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Poyezdlar bir vaqtda "
                "emas, bir soat farq bilan chiqdi.</p><p><strong>Yechishni "
                "nimadan boshlash kerak?</strong></p>",
        "choices": [
            "Oradan birinchisi bosgan yoʻlni ayirishdan",
            "Ikki tezlikning oʻrtachasini olishdan",
            "Butun orani yaqinlashish tezligiga boʻlishdan",
            "Yoʻlning oʻrtasini topishdan",
        ],
        "correct": "Oradan birinchisi bosgan yoʻlni ayirishdan",
        "explanation": "<p><strong>Oradan birinchisi bosgan yoʻlni "
                       "ayirishdan.</strong> Ikkinchisi chiqqan paytga "
                       "oʻtiladi va shundan keyin masala oddiy "
                       "uchrashuvga aylanadi. Javobni esa oʻsha paytga "
                       "qoʻshib yozish kerak.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>«Ikki shahar orasi 240 km, "
                "mashinalar qarshi chiqdi: 60 va 60 km/soat» — oʻquvchi "
                "yozdi: «t = 240 ÷ 60 = 4 soat».</p><p><strong>Nima "
                "notoʻgʻri?</strong></p>",
        "choices": [
            "Faqat bitta tezlik olingan",
            "Masofa notoʻgʻri",
            "Boʻlish oʻrniga koʻpaytirish kerak edi",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Faqat bitta tezlik olingan",
        "explanation": "<p><strong>Faqat bitta tezlik olingan.</strong> "
                       "Ora ikkala mashina hisobiga kamayadi: "
                       "60 + 60 = 120 km/soat, demak "
                       "t = 240 ÷ 120 = 2 soat. Tekshirish: har biri "
                       "120 km bosadi, 120 + 120 = 240 ✓</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Piyoda 4 km/soat "
                "bilan ketdi. 2 soatdan keyin velosipedchi 12 km/soat "
                "bilan ortidan chiqdi. Qachon quvib yetadi?</strong></p>",
        "choices": [
            "8 ÷ 16 = 0,5 soat",
            "8 ÷ 8 = 1 soat",
            "8 ÷ 12 = 0,67 soat",
            "8 ÷ 4 = 2 soat",
        ],
        "correct": "8 ÷ 8 = 1 soat",
        "explanation": "<p><strong>8 ÷ 8 = 1 soat.</strong> Ustunlik "
                       "4 × 2 = 8 km, farq tezligi 12 − 4 = 8 km/soat. "
                       "Tekshirish: piyoda 3 soatda 12 km, velosipedchi "
                       "1 soatda 12 km ✓ <strong>8 ÷ 16</strong> — "
                       "tezliklar qoʻshib yuborilgan; bu qarama-qarshi "
                       "harakatning qoidasi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>A va B shaharlari orasi 320 km. "
                "Soat 07:00 da A dan 60 km/soat bilan avtobus chiqdi. Soat "
                "08:00 da B dan 70 km/soat bilan qarshi avtobus "
                "chiqdi.</p><p><strong>Ular soat nechada "
                "uchrashadi?</strong></p>",
        "choices": ["09:00 da", "10:00 da", "11:00 da", "12:00 da"],
        "correct": "10:00 da",
        "explanation": "<p><strong>10:00 da.</strong> 08:00 gacha birinchi "
                       "avtobus 60 × 1 = 60 km yurdi, demak ora "
                       "320 − 60 = 260 km. Yaqinlashish tezligi "
                       "60 + 70 = 130 km/soat, t = 260 ÷ 130 = 2 soat "
                       "— 08:00 dan boshlab, yaʼni 10:00. Tekshirish: "
                       "birinchisi 3 soatda 180 km, ikkinchisi 2 soatda "
                       "140 km; 180 + 140 = 320 ✓ <strong>09:00</strong> "
                       "— boshlangʻich ustunlik oradan "
                       "ayirilmaganda.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Dilnoza uydan 5 km/soat bilan "
                "piyoda chiqdi. 30 minutdan keyin akasi 10 km/soat bilan "
                "velosipedda ortidan chiqdi.</p><p><strong>Akasi uydan "
                "qancha narida quvib yetadi?</strong></p>",
        "choices": ["2,5 km", "5 km", "7,5 km", "10 km"],
        "correct": "5 km",
        "explanation": "<p><strong>5 km.</strong> Dilnozaning ustunligi "
                       "5 × 0,5 = 2,5 km. Farq tezligi 10 − 5 = "
                       "5 km/soat, demak t = 2,5 ÷ 5 = 0,5 soat. Akasi "
                       "shu vaqtda 10 × 0,5 = 5 km yuradi. Tekshirish: "
                       "Dilnoza jami 1 soat yurgan, 5 × 1 = 5 km ✓ "
                       "<strong>2,5</strong> — faqat boshlangʻich "
                       "ustunlik, quvib yetish joyi emas.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-87 Mashq: Chizma va sxema",
        "tutorial":    "PM-87:",
        "description": (
            "Tasma model, kesma chizma va oʻq sxemasi: ortiqchani qirqish, "
            "«qolgani» qoidasi va bosqichli oʻzgarish. 20 savol."
        ),
        "questions":   Q_PM87,
        **DEFAULTS,
    },
    {
        "title":       "PM-88 Mashq: Harakat masalalari 1",
        "tutorial":    "PM-88:",
        "description": (
            "S = v·t uchligi, minutni soatga oʻgirish, km/soat va m/s, "
            "koʻp boʻlakli yoʻl va oʻrtacha tezlik. 20 savol."
        ),
        "questions":   Q_PM88,
        **DEFAULTS,
    },
    {
        "title":       "PM-89 Mashq: Harakat masalalari 2",
        "tutorial":    "PM-89:",
        "description": (
            "Uchrashuv va quvish: yaqinlashish tezligi, farq tezligi, "
            "boshlangʻich ustunlik va uchrashuv joyi. 20 savol."
        ),
        "questions":   Q_PM89,
        **DEFAULTS,
    },
]
