# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-98, PM-99, PM-100. **KURSNING YAKUNI.**

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: uchalasi ham `hard`.

⚠️ PM-100 mashqi BOSHQACHA: u yangi mavzuni emas, BUTUN KURSNI
   tekshiradi. Savollar sakkizta blokning hammasidan olingan va har
   birining izohida qaysi darsdan ekani koʻrsatilgan — shunday qilib
   test bir vaqtning oʻzida takrorlash xaritasi ham boʻladi.
   Shuning uchun undagi ramp mavzu boʻyicha emas, BLOK boʻyicha
   boradi: A → H, oxirida ikkita matnli masala.

⚠️ `choices` EKRANLANADI — HTML teg yoʻq.
⚠️ Kumulyativ:
   • PM-98 — teskari amallar va teskari tartib;
   • PM-99 — namuna, n-had, 1..n yigʻindisi, toq sonlar va kvadratlar.
     ⛔ Induksiya YOʻQ;
   • PM-100 — hamma blok. Yangi hech narsa yoʻq.
⚠️ Distraktorlar — haqiqiy xatolar: orqaga yurganda amalni
   almashtirmaslik, tartibni almashtirmaslik, «yarmi olindi» ni ÷2
   deb olish, n-hadda toʻgʻrilashni unutish, 1..n da 2 ga
   boʻlmaslik.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_98_100.py --master=prime \\
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
# PM-98 — teskaridan yurish
# =====================================================================

Q_PM98 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>Bir songa 7 qoʻshilsa, 15 chiqadi.</p>"
                "<p><strong>Bu son qanday?</strong></p>",
        "choices": ["7", "8", "15", "22"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Orqaga qaytamiz: 15 − 7 = 8. "
                       "Tekshirish: 8 + 7 = 15 ✓ <strong>22</strong> — "
                       "ayirish oʻrniga qoʻshilganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Bir son 6 ga koʻpaytirilsa, 42 "
                "chiqadi.</p><p><strong>Bu son qanday?</strong></p>",
        "choices": ["6", "7", "36", "252"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Orqaga: 42 ÷ 6 = 7. "
                       "Tekshirish: 7 × 6 = 42 ✓ <strong>252</strong> — "
                       "boʻlish oʻrniga koʻpaytirilganda.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>«+ 9» "
                "amalining teskarisi — ___</strong></p>",
        "choices": ["+ 9", "− 9", "× 9", "÷ 9"],
        "correct": "− 9",
        "explanation": "<p><strong>− 9.</strong> Qoʻshishning teskarisi — "
                       "ayirish. Orqaga qaytganda bajarilgan amal "
                       "bekor qilinadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>Qutidagi buyumlarning "
                "yarmi olindi.</p><p><strong>Orqaga qaytish uchun qolgan "
                "songa ___ qilinadi.</strong></p>",
        "choices": ["÷ 2", "× 2", "+ 2", "− 2"],
        "correct": "× 2",
        "explanation": "<p><strong>× 2.</strong> Yarmi olinsa, qolgani ham "
                       "yarmi. Orqaga qaytganda son "
                       "<strong>kattalashadi</strong> — axir biz "
                       "kamayishni bekor qilyapmiz. "
                       "<strong>÷ 2</strong> — eng koʻp uchraydigan "
                       "xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oldinga: avval × 2, "
                "keyin + 5.</p><p><strong>Orqaga qaytishda tartib "
                "qanday boʻladi?</strong></p>",
        "choices": [
            "Avval ÷ 2, keyin − 5",
            "Avval − 5, keyin ÷ 2",
            "Avval × 2, keyin − 5",
            "Avval + 5, keyin ÷ 2",
        ],
        "correct": "Avval − 5, keyin ÷ 2",
        "explanation": "<p><strong>Avval − 5, keyin ÷ 2.</strong> Amallar "
                       "ham teskarisiga almashadi, <strong>tartib "
                       "ham</strong> teskari boʻladi: eng oxirgi "
                       "bajarilgan amal birinchi qaytariladi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Bir son 5 ga koʻpaytirildi, "
                "keyin 4 ayirildi va 31 chiqdi.</p><p><strong>Bu son "
                "qanday?</strong></p>",
        "choices": ["5", "7", "9", "35"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Orqaga: 31 + 4 = 35, keyin "
                       "35 ÷ 5 = 7. Tekshirish oldinga: 7 × 5 = 35, "
                       "35 − 4 = 31 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir songa 6 qoʻshildi, keyin "
                "natija 3 ga boʻlindi va 8 chiqdi.</p><p><strong>Bu son "
                "qanday?</strong></p>",
        "choices": ["18", "24", "30", "42"],
        "correct": "18",
        "explanation": "<p><strong>18.</strong> Orqaga: 8 × 3 = 24, keyin "
                       "24 − 6 = 18. Tekshirish: 18 + 6 = 24, "
                       "24 ÷ 3 = 8 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir son 4 ga boʻlindi, keyin "
                "7 qoʻshildi va 12 chiqdi.</p><p><strong>Bu son "
                "qanday?</strong></p>",
        "choices": ["5", "20", "48", "76"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> Orqaga: 12 − 7 = 5, keyin "
                       "5 × 4 = 20. Tekshirish: 20 ÷ 4 = 5, "
                       "5 + 7 = 12 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Qutidagi qalamlarning yarmi "
                "olindi va 14 tasi qoldi.</p><p><strong>Boshida nechta "
                "edi?</strong></p>",
        "choices": ["7 ta", "16 ta", "21 ta", "28 ta"],
        "correct": "28 ta",
        "explanation": "<p><strong>28 ta.</strong> 14 × 2 = 28. "
                       "<strong>7</strong> — 14 ni ikkiga boʻlganda "
                       "chiqadi, lekin orqaga qaytganda son "
                       "kattalashishi kerak.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Savatdagi mevaning yarmi va "
                "yana 3 tasi olindi, 9 tasi qoldi.</p><p><strong>Boshida "
                "nechta edi?</strong></p>",
        "choices": ["12 ta", "18 ta", "24 ta", "30 ta"],
        "correct": "24 ta",
        "explanation": "<p><strong>24 ta.</strong> Ikkita qadamni ajratamiz. "
                       "Orqaga: 9 + 3 = 12, keyin 12 × 2 = 24. "
                       "Tekshirish: 24 ning yarmi 12, yana 3 tasi — "
                       "jami 15 ta olindi; 24 − 15 = 9 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir son 3 ga koʻpaytirildi, "
                "keyin 4 qoʻshildi, soʻng 2 ga koʻpaytirildi va 32 "
                "chiqdi.</p><p><strong>Bu son qanday?</strong></p>",
        "choices": ["4", "6", "12", "16"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Uchta qadam orqaga: "
                       "32 ÷ 2 = 16, keyin 16 − 4 = 12, keyin "
                       "12 ÷ 3 = 4. Tekshirish oldinga: 4 × 3 = 12, "
                       "12 + 4 = 16, 16 × 2 = 32 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bogʻdagi olmalarning uchdan "
                "bir qismi terildi va 20 tasi qoldi.</p><p><strong>Boshida "
                "nechta edi?</strong></p>",
        "choices": ["24 ta", "27 ta", "30 ta", "60 ta"],
        "correct": "30 ta",
        "explanation": "<p><strong>30 ta.</strong> Uchdan biri terilsa, "
                       "qolgani uchdan ikki qism (PM-87). Demak "
                       "20 — bu 2/3 qism: 20 ÷ 2 × 3 = 30. Tekshirish: "
                       "30 ning uchdan biri 10, 30 − 10 = 20 ✓</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qachon "
                "teskaridan yurish eng qulay?</strong></p>",
        "choices": [
            "Boshlangʻich son maʼlum boʻlganda",
            "Oxirgi natija maʼlum, boshlanish nomaʼlum boʻlganda",
            "Masalada faqat qoʻshish boʻlganda",
            "Sonlar kichik boʻlganda",
        ],
        "correct": "Oxirgi natija maʼlum, boshlanish nomaʼlum boʻlganda",
        "explanation": "<p><strong>Oxirgi natija maʼlum boʻlganda.</strong> "
                       "«…va oxirida 5 ta qoldi», «…natijada 35 chiqdi» "
                       "degan gaplar shu usulni chaqiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Pulning yarmi "
                "sarflandi, 6 000 soʻm qoldi».</p><p><strong>Boshida "
                "qancha bor edi?</strong></p>",
        "choices": ["3 000 soʻm", "6 000 soʻm", "9 000 soʻm",
                    "12 000 soʻm"],
        "correct": "12 000 soʻm",
        "explanation": "<p><strong>12 000 soʻm.</strong> 6 000 × 2 = "
                       "12 000. <strong>3 000</strong> — ikkiga "
                       "boʻlinganda chiqadi; orqaga qaytganda esa "
                       "koʻpaytiriladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Orqaga qaytishda "
                "amallar teskarisiga almashtirildi.</p><p><strong>Tartib "
                "bilan nima qilinadi?</strong></p>",
        "choices": [
            "Tartib oʻzgarmaydi",
            "Tartib ham teskari boʻladi",
            "Tartib ahamiyatsiz",
            "Faqat koʻpaytirish oldinga surtiladi",
        ],
        "correct": "Tartib ham teskari boʻladi",
        "explanation": "<p><strong>Tartib ham teskari boʻladi.</strong> "
                       "Eng oxirgi bajarilgan amal birinchi "
                       "qaytariladi. Faqat amallarni almashtirib, "
                       "tartibni saqlash — yarim ish va xato "
                       "javob.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Teskaridan yurib javob "
                "topildi.</p><p><strong>Uni qanday tekshirish eng "
                "qulay?</strong></p>",
        "choices": [
            "Yana bir marta orqaga yurish",
            "Javobni ikkiga boʻlish",
            "Javobni boshiga qoʻyib, oldinga yurish",
            "Tenglama tuzish",
        ],
        "correct": "Javobni boshiga qoʻyib, oldinga yurish",
        "explanation": "<p><strong>Javobni boshiga qoʻyib, oldinga "
                       "yurish.</strong> Oxirida masaladagi son "
                       "chiqishi kerak. Yana bir marta orqaga yurish "
                       "esa oʻsha xatoni takrorlashi mumkin — "
                       "tekshirish boshqa yoʻldan borishi kerak.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>«Bir son 3 ga "
                "koʻpaytirildi, keyin 8 qoʻshildi va 35 chiqdi» — "
                "oʻquvchi yozdi: «35 ÷ 3 = 11,67, keyin "
                "11,67 − 8 = 3,67».</p><p><strong>Nima notoʻgʻri?</strong>"
                "</p>",
        "choices": [
            "Amallar teskarisiga almashtirilmagan",
            "Tartib teskari qilinmagan — avval 8 ni ayirish kerak edi",
            "Boʻlish oʻrniga koʻpaytirish kerak edi",
            "Xato yoʻq",
        ],
        "correct": "Tartib teskari qilinmagan — avval 8 ni ayirish kerak edi",
        "explanation": "<p><strong>Tartib teskari qilinmagan.</strong> "
                       "Amallar toʻgʻri almashtirilgan (× → ÷, "
                       "+ → −), lekin tartib saqlanib qolgan. "
                       "Toʻgʻrisi: 35 − 8 = 27, keyin 27 ÷ 3 = 9. "
                       "Butun son chiqmagani darrov "
                       "shubhalantirishi kerak edi.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Bir sondan 5 "
                "ayirildi, keyin 3 ga koʻpaytirildi va 21 chiqdi. Bu son "
                "qanday?</strong></p>",
        "choices": [
            "21 ÷ 3 = 7, keyin 7 + 5 = 12",
            "21 + 5 = 26, keyin 26 ÷ 3 ≈ 8,67",
            "21 × 3 = 63, keyin 63 − 5 = 58",
            "21 ÷ 3 = 7, keyin 7 − 5 = 2",
        ],
        "correct": "21 ÷ 3 = 7, keyin 7 + 5 = 12",
        "explanation": "<p><strong>21 ÷ 3 = 7, keyin 7 + 5 = 12.</strong> "
                       "Oxirgi amal «×3» edi — birinchi qaytariladi. "
                       "Keyin «−5» ning teskarisi «+5». Tekshirish: "
                       "12 − 5 = 7, 7 × 3 = 21 ✓ Oxirgi variantda "
                       "ayirish qaytarilmagan.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Dilnoza pulining yarmini "
                "kitobga sarfladi, keyin 8 000 soʻmga daftar oldi va "
                "12 000 soʻm qoldi.</p><p><strong>Boshida qancha puli "
                "bor edi?</strong></p>",
        "choices": ["20 000 soʻm", "28 000 soʻm", "40 000 soʻm",
                    "48 000 soʻm"],
        "correct": "40 000 soʻm",
        "explanation": "<p><strong>40 000 soʻm.</strong> Orqaga: "
                       "12 000 + 8 000 = 20 000 (kitobdan keyin "
                       "qolgani), keyin 20 000 × 2 = 40 000. "
                       "Tekshirish oldinga: 40 000 → yarmi → 20 000 → "
                       "−8 000 → 12 000 ✓ <strong>20 000</strong> — "
                       "oxirgi qadam unutilganda chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Savatda meva bor edi. "
                "Birinchi kuni yarmi yeyildi. Ikkinchi kuni qolganning "
                "yarmi yeyildi. Uchinchi kuni yana 3 tasi yeyildi va "
                "2 tasi qoldi.</p><p><strong>Boshida nechta meva bor "
                "edi?</strong></p>",
        "choices": ["10 ta", "14 ta", "20 ta", "24 ta"],
        "correct": "20 ta",
        "explanation": "<p><strong>20 ta.</strong> Uchta qadam orqaga: "
                       "2 + 3 = 5, keyin 5 × 2 = 10, keyin "
                       "10 × 2 = 20. Tekshirish oldinga: 20 → 10 → 5 → "
                       "5 − 3 = 2 ✓</p>",
    },
]


# =====================================================================
# PM-99 — namuna izlash va umumlashtirish
# =====================================================================

Q_PM99 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>1 + 2 + 3 + … + 10 = ?</strong>"
                "</p>",
        "choices": ["50", "55", "100", "110"],
        "correct": "55",
        "explanation": "<p><strong>55.</strong> 10 × 11 ÷ 2 = 55. "
                       "Juftlash bilan: 5 ta juftlik, har biri 11 ga "
                       "teng. <strong>110</strong> — 2 ga boʻlish "
                       "unutilganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1 + 3 + 5 + 7 = ?</strong></p>",
        "choices": ["12", "16", "20", "25"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> Bu birinchi 4 ta toq son, "
                       "demak 4² = 16. Bevosita qoʻshib ham tekshirish "
                       "mumkin: 1 + 3 = 4, + 5 = 9, + 7 = 16 ✓</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>2, 5, 8, 11, "
                "___</strong></p>",
        "choices": ["12", "13", "14", "16"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> Har qadamda +3. Bu "
                       "qatorning n-hadi 3n − 1: n = 5 uchun "
                       "3 × 5 − 1 = 14 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>n × (n + 1) ÷ 2 "
                "formulasi nimani beradi?</strong></p>",
        "choices": [
            "1 dan n gacha sonlar yigʻindisini",
            "Birinchi n ta toq son yigʻindisini",
            "n ning kvadratini",
            "n ta sonning oʻrtachasini",
        ],
        "correct": "1 dan n gacha sonlar yigʻindisini",
        "explanation": "<p><strong>1 dan n gacha yigʻindini.</strong> "
                       "Juftlash usulidan chiqadi: n ÷ 2 ta juftlik, "
                       "har biri n + 1 ga teng. Birinchi n ta toq "
                       "sonning yigʻindisi esa n².</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>1, 4, 9, 16, "
                "___</strong></p>",
        "choices": ["20", "24", "25", "32"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Bular aniq kvadratlar: "
                       "1², 2², 3², 4², demak keyingisi 5² = 25.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>1 + 2 + 3 + … + 30 = ?</strong>"
                "</p>",
        "choices": ["435", "465", "480", "930"],
        "correct": "465",
        "explanation": "<p><strong>465.</strong> 30 × 31 ÷ 2 = 465. "
                       "<strong>930</strong> — 2 ga boʻlmaganda "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Birinchi 8 ta toq sonning "
                "yigʻindisi qancha?</strong></p>",
        "choices": ["36", "56", "64", "72"],
        "correct": "64",
        "explanation": "<p><strong>64.</strong> Birinchi n ta toq sonning "
                       "yigʻindisi n²: 8² = 64. Yaʼni "
                       "1 + 3 + 5 + … + 15 = 64.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Qator: 5, 9, 13, 17, …</p>"
                "<p><strong>Uning 10-hadi qanday?</strong></p>",
        "choices": ["37", "41", "45", "50"],
        "correct": "41",
        "explanation": "<p><strong>41.</strong> Har qadamda +4 → 4n; "
                       "n = 1 da 4 chiqadi, kerak 5 → 4n + 1. Demak "
                       "4 × 10 + 1 = 41. Tekshirish: n = 3 → "
                       "13 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Gugurt choʻplaridan qatorga "
                "kvadratlar yasaladi: 1 tasi — 4 ta choʻp, 2 tasi — 7 ta, "
                "3 tasi — 10 ta.</p><p><strong>12 ta kvadrat uchun nechta "
                "choʻp kerak?</strong></p>",
        "choices": ["36 ta", "37 ta", "48 ta", "49 ta"],
        "correct": "37 ta",
        "explanation": "<p><strong>37 ta.</strong> Har qadamda +3 → 3n; "
                       "n = 1 da 3 chiqadi, kerak 4 → 3n + 1. Demak "
                       "3 × 12 + 1 = 37. <strong>36</strong> — "
                       "toʻgʻrilash «+1» unutilganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>1 dan 100 gacha sonlar ikki uchidan "
                "juftlanadi.</p><p><strong>Nechta juftlik hosil boʻladi "
                "va har biri qanchaga teng?</strong></p>",
        "choices": [
            "50 ta juftlik, har biri 101",
            "50 ta juftlik, har biri 100",
            "100 ta juftlik, har biri 101",
            "101 ta juftlik, har biri 50",
        ],
        "correct": "50 ta juftlik, har biri 101",
        "explanation": "<p><strong>50 ta juftlik, har biri 101.</strong> "
                       "1 + 100 = 101, 2 + 99 = 101 va hokazo. "
                       "Yuzta son ikkitadan juftlanadi: 100 ÷ 2 = 50. "
                       "Natija 50 × 101 = 5050.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>6 kishi bir-biri bilan bir "
                "martadan qoʻl berdi.</p><p><strong>Nechta qoʻl berish "
                "boʻlgan?</strong></p>",
        "choices": ["12 ta", "15 ta", "30 ta", "36 ta"],
        "correct": "15 ta",
        "explanation": "<p><strong>15 ta.</strong> Har biri qolgan 5 kishi "
                       "bilan: 6 × 5 = 30, lekin har bir qoʻl berish "
                       "ikki marta sanaldi (PM-96), demak "
                       "30 ÷ 2 = 15. Formula: n(n − 1) ÷ 2.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Kvadrat stollar qatorga "
                "qoʻyiladi: 1 ta stolga 4 kishi, 2 ta stolga 6 kishi, "
                "3 ta stolga 8 kishi oʻtiradi.</p><p><strong>15 ta stolga "
                "necha kishi oʻtiradi?</strong></p>",
        "choices": ["30 kishi", "32 kishi", "45 kishi", "60 kishi"],
        "correct": "32 kishi",
        "explanation": "<p><strong>32 kishi.</strong> Har qadamda +2 → 2n; "
                       "n = 1 da 2 chiqadi, kerak 4 → 2n + 2. Demak "
                       "2 × 15 + 2 = 32. Maʼnosi: har stol yuqoriga va "
                       "pastga bittadan joy beradi, ikki uchida esa "
                       "yana bittadan.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Beshta kichik holda "
                "formula toʻgʻri chiqdi.</p><p><strong>Bu formulaning "
                "isbotimi?</strong></p>",
        "choices": [
            "Ha, besh hol yetarli",
            "Yoʻq — namuna taxmin beradi, isbot emas",
            "Ha, agar hollar ketma-ket boʻlsa",
            "Faqat sonlar kichik boʻlganda",
        ],
        "correct": "Yoʻq — namuna taxmin beradi, isbot emas",
        "explanation": "<p><strong>Yoʻq.</strong> Aylanadagi boʻlaklar "
                       "qatori 1, 2, 4, 8, 16 deb boshlanadi, lekin "
                       "keyingisi 32 emas, <strong>31</strong>. Isbot "
                       "uchun <b>sabab</b> koʻrsatish kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qator: 2, 5, 8, 11, …</p>"
                "<p><strong>Uning n-hadi qanday?</strong></p>",
        "choices": ["3n", "3n − 1", "3n + 1", "n + 3"],
        "correct": "3n − 1",
        "explanation": "<p><strong>3n − 1.</strong> Qadam +3 boʻlgani uchun "
                       "3n, keyin toʻgʻrilash: n = 1 da 3 chiqadi, "
                       "kerak esa 2 — demak «− 1». <strong>3n</strong> "
                       "— toʻgʻrilash unutilgan eng koʻp uchraydigan "
                       "xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Topilgan "
                "formulani birinchi navbatda nima bilan tekshirish "
                "kerak?</strong></p>",
        "choices": [
            "Katta n qiymatlari bilan",
            "Kichik n qiymatlari bilan (n = 1, 2, 3)",
            "Kalkulyator bilan",
            "Boshqa formula bilan",
        ],
        "correct": "Kichik n qiymatlari bilan (n = 1, 2, 3)",
        "explanation": "<p><strong>Kichik n qiymatlari bilan.</strong> Bir "
                       "necha soniya vaqt oladi va notoʻgʻri formulani "
                       "darrov fosh qiladi — ayniqsa toʻgʻrilash "
                       "unutilgan boʻlsa.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nima uchun "
                "3n + 1 formulasi gugurt kvadratlariga mos "
                "keladi?</strong></p>",
        "choices": [
            "Chunki har bir kvadrat 3 ta yangi choʻp qoʻshadi, boshida esa 1 ta ortiqcha turadi",
            "Chunki kvadratning 4 ta tomoni bor",
            "Chunki 3 va 1 qoʻshilsa 4 boʻladi",
            "Bu shunchaki tasodif",
        ],
        "correct": "Chunki har bir kvadrat 3 ta yangi choʻp qoʻshadi, "
                   "boshida esa 1 ta ortiqcha turadi",
        "explanation": "<p><strong>Har bir kvadrat 3 ta choʻp qoʻshadi, "
                       "boshida 1 ta ortiqcha.</strong> Formulani "
                       "maʼnosi bilan tushunsangiz, uni hech qachon "
                       "unutmaysiz — va u nima uchun rost ekanini ham "
                       "bilasiz.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>Oʻquvchi yozdi: "
                "«1 + 2 + … + 100 = 100 × 101 = 10 100».</p>"
                "<p><strong>Nima notoʻgʻri?</strong></p>",
        "choices": [
            "101 emas, 100 ga koʻpaytirish kerak edi",
            "Natijani 2 ga boʻlish unutilgan",
            "Juftlash usuli bu yerda ishlamaydi",
            "Xato yoʻq",
        ],
        "correct": "Natijani 2 ga boʻlish unutilgan",
        "explanation": "<p><strong>2 ga boʻlish unutilgan.</strong> "
                       "Juftlaganda har bir son ikki marta sanaladi, "
                       "shuning uchun 100 × 101 ÷ 2 = 5050. Javobni "
                       "kichik holda tekshirish shuni darrov "
                       "koʻrsatardi: n = 4 uchun 4 × 5 = 20, "
                       "haqiqiy yigʻindi esa 10.</p>",
    },
    {
        "text": "<p>Qaysi n-had toʻgʻri?</p><p><strong>Qator: 7, 12, 17, "
                "22, …</strong></p>",
        "choices": ["5n", "5n + 2", "5n − 2", "7n"],
        "correct": "5n + 2",
        "explanation": "<p><strong>5n + 2.</strong> Qadam +5 → 5n; n = 1 da "
                       "5 chiqadi, kerak 7 → «+ 2». Tekshirish: n = 3 → "
                       "5 × 3 + 2 = 17 ✓ <strong>5n − 2</strong> "
                       "toʻgʻrilash ishorasi teskari olinganda "
                       "chiqadi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Teatr zalida birinchi qatorda "
                "12 ta oʻrindiq bor. Har bir keyingi qatorda 2 tadan "
                "koʻp.</p><p><strong>10-qatorda nechta oʻrindiq "
                "bor?</strong></p>",
        "choices": ["20 ta", "28 ta", "30 ta", "32 ta"],
        "correct": "30 ta",
        "explanation": "<p><strong>30 ta.</strong> Har qadamda +2 → 2n; "
                       "n = 1 da 2 chiqadi, kerak 12 → 2n + 10. Demak "
                       "2 × 10 + 10 = 30. Boshqacha: birinchi qatordan "
                       "9 qadam oʻtildi, 12 + 2 × 9 = 30 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Devor gʻishtdan terilgan: eng "
                "yuqori qatorda 1 ta gʻisht, undan pastdagisida 2 ta, "
                "keyingisida 3 ta va shu tartibda pastga qarab. Jami "
                "20 ta qator bor.</p><p><strong>Devorda nechta gʻisht "
                "bor?</strong></p>",
        "choices": ["190 ta", "200 ta", "210 ta", "400 ta"],
        "correct": "210 ta",
        "explanation": "<p><strong>210 ta.</strong> Bu 1 + 2 + … + 20 "
                       "yigʻindisi: 20 × 21 ÷ 2 = 210. Juftlash bilan "
                       "ham: 10 ta juftlik, har biri 21 ga teng. "
                       "<strong>400</strong> — 20 × 20 qilinganda "
                       "chiqadi.</p>",
    },
]


# =====================================================================
# PM-100 — YAKUNIY TAKROR: butun kurs boʻyicha
# Ramp mavzu emas, BLOK boʻyicha: A → H, oxirida ikki matnli masala.
# =====================================================================

Q_PM100 = [
    # ── Blok A: sonlar va amallar ─────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>2 + 3 × 4 = ?</strong></p>",
        "choices": ["9", "14", "20", "24"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> Amallar tartibi (PM-5): "
                       "avval koʻpaytirish, 3 × 4 = 12, keyin "
                       "2 + 12 = 14. <strong>20</strong> — chapdan "
                       "oʻngga hisoblaganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>12 va 18 sonlarining EKUB i "
                "qancha?</strong></p>",
        "choices": ["2", "3", "6", "36"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> (PM-8) 12 = 2² × 3, "
                       "18 = 2 × 3². Umumiylari: 2 × 3 = 6. "
                       "<strong>36</strong> — bu EKUK, eng kichik "
                       "umumiy karrali.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−7 + 3 = ?</strong></p>",
        "choices": ["−10", "−4", "4", "10"],
        "correct": "−4",
        "explanation": "<p><strong>−4.</strong> (PM-10) Son oʻqida −7 dan "
                       "oʻngga 3 qadam. <strong>−10</strong> — "
                       "qoʻshish oʻrniga ayirilganda chiqadi.</p>",
    },
    # ── Blok B: kasr, foiz ────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>240 ning 25 foizi "
                "qancha?</strong></p>",
        "choices": ["24", "60", "96", "6000"],
        "correct": "60",
        "explanation": "<p><strong>60.</strong> (PM-23) 240 × 0,25 = 60. "
                       "<strong>6000</strong> — foizni oʻnlik kasrga "
                       "oʻgirmay 240 × 25 qilinganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1/2 + 1/4 = ?</strong></p>",
        "choices": ["1/6", "2/6", "3/4", "1/8"],
        "correct": "3/4",
        "explanation": "<p><strong>3/4.</strong> (PM-17) Umumiy maxraj 4: "
                       "2/4 + 1/4 = 3/4. <strong>2/6</strong> — surat "
                       "va maxraj alohida qoʻshilganda chiqadigan "
                       "klassik xato.</p>",
    },
    # ── Blok C: algebra ───────────────────────────────────────────
    {
        "text": "<p>Tenglamani yeching.</p><p><strong>4x − 7 = 21</strong>"
                "</p>",
        "choices": ["x = 3,5", "x = 7", "x = 14", "x = 28"],
        "correct": "x = 7",
        "explanation": "<p><strong>x = 7.</strong> (PM-36) Ikki tomonga 7 "
                       "qoʻshamiz: 4x = 28, keyin 4 ga boʻlamiz: "
                       "x = 7. Tekshirish: 4 × 7 − 7 = 21 ✓</p>",
    },
    {
        "text": "<p>Qavsni oching.</p><p><strong>3(x + 2) = ?</strong></p>",
        "choices": ["3x + 2", "3x + 6", "x + 6", "3x + 5"],
        "correct": "3x + 6",
        "explanation": "<p><strong>3x + 6.</strong> (PM-33) Koʻpaytuvchi "
                       "qavs ichidagi <b>har bir</b> hadga tarqaladi. "
                       "<strong>3x + 2</strong> — ikkinchi hadga "
                       "tarqatish unutilgan.</p>",
    },
    # ── Blok D: funksiya va grafik ────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>Funksiya: y = 3x − 2.</p>"
                "<p><strong>x = 5 boʻlganda y qancha?</strong></p>",
        "choices": ["10", "13", "15", "17"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> (PM-49) Oʻrniga qoʻyamiz: "
                       "3 × 5 − 2 = 15 − 2 = 13.</p>",
    },
    # ── Blok E: geometriya ────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>Toʻgʻri toʻrtburchakning tomonlari "
                "9 sm va 6 sm.</p><p><strong>Uning yuzasi qancha?</strong>"
                "</p>",
        "choices": ["15 sm²", "30 sm²", "54 sm²", "108 sm²"],
        "correct": "54 sm²",
        "explanation": "<p><strong>54 sm².</strong> (PM-68) S = a × b = "
                       "9 × 6 = 54. <strong>30</strong> — bu perimetr "
                       "(2 × (9 + 6)); yuza bilan perimetrni "
                       "chalkashtirish eng koʻp uchraydigan "
                       "xato.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Toʻgʻri burchakli uchburchakning "
                "katetlari 5 sm va 12 sm.</p><p><strong>Gipotenuza "
                "qancha?</strong></p>",
        "choices": ["13 sm", "17 sm", "60 sm", "169 sm"],
        "correct": "13 sm",
        "explanation": "<p><strong>13 sm.</strong> (PM-64) Pifagor "
                       "teoremasi: 5² + 12² = 25 + 144 = 169, "
                       "√169 = 13. <strong>169</strong> — ildiz olish "
                       "unutilgan; <strong>17</strong> — katetlar "
                       "shunchaki qoʻshilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Aylananing radiusi 10 sm "
                "(π ≈ 3,14).</p><p><strong>Aylana uzunligi qancha?</strong>"
                "</p>",
        "choices": ["31,4 sm", "62,8 sm", "314 sm", "628 sm"],
        "correct": "62,8 sm",
        "explanation": "<p><strong>62,8 sm.</strong> (PM-71) "
                       "L = 2πR = 2 × 3,14 × 10 = 62,8. "
                       "<strong>31,4</strong> — πR qilinganda, yaʼni "
                       "2 ga koʻpaytirish unutilganda; "
                       "<strong>314</strong> — bu doira yuzasi "
                       "(πR²).</p>",
    },
    # ── Blok F: maʼlumot va ehtimollik ────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>Sonlar: 3, 5, 7, 9, 11.</p>"
                "<p><strong>Ularning medianasi qancha?</strong></p>",
        "choices": ["5", "7", "8", "35"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> (PM-79) Mediana — tartibga "
                       "solingan qatorning oʻrtasidagi son. Bu yerda u "
                       "oʻrtacha arifmetikka ham teng (35 ÷ 5 = 7), "
                       "lekin har doim ham unday boʻlmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Zar tashlandi. 5 dan katta "
                "son tushish ehtimolligi qancha?</strong></p>",
        "choices": ["0,17", "0,33", "0,5", "0,83"],
        "correct": "0,17",
        "explanation": "<p><strong>0,17.</strong> (PM-83) Beshdan katta "
                       "son faqat 6 — bitta qulay hol: "
                       "1 ÷ 6 ≈ 0,17. <strong>0,33</strong> — "
                       "«5 dan kichik boʻlmagan» deb oʻqilganda "
                       "(5 va 6) chiqadi.</p>",
    },
    # ── Blok G: matnli masalalar ──────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>Mashina 80 km/soat bilan "
                "1,5 soat yurdi. Qancha yoʻl bosdi?</strong></p>",
        "choices": ["53 km", "81,5 km", "120 km", "800 km"],
        "correct": "120 km",
        "explanation": "<p><strong>120 km.</strong> (PM-88) "
                       "S = v × t = 80 × 1,5 = 120. Diqqat: 1,5 soat — "
                       "bu 1 soat 30 minut.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir usta ishni 4 kunda, "
                "ikkinchisi 12 kunda bitiradi.</p><p><strong>Birga necha "
                "kunda bitirishadi?</strong></p>",
        "choices": ["3 kunda", "6 kunda", "8 kunda", "16 kunda"],
        "correct": "3 kunda",
        "explanation": "<p><strong>3 kunda.</strong> (PM-90) "
                       "1/4 + 1/12 = 3/12 + 1/12 = 4/12 = 1/3, demak "
                       "3 kun. Javob eng tez ishlovchining vaqtidan "
                       "(4 kun) kichik ✓ <strong>16</strong> — "
                       "vaqtlar qoʻshilganda.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>2,5 m² — bu "
                "___ sm².</strong></p>",
        "choices": ["250", "2500", "25 000", "250 000"],
        "correct": "25 000",
        "explanation": "<p><strong>25 000.</strong> (PM-94) "
                       "1 m² = 10 000 sm², demak 2,5 × 10 000 = "
                       "25 000. <strong>250</strong> — uzunlik "
                       "koeffitsiyenti (100) yuzaga qoʻllanganda "
                       "chiqadi; yuzada u kvadratga koʻtariladi.</p>",
    },
    # ── Blok H: mantiq ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Guruhda 10 kishi bor, "
                "hafta esa 7 kundan iborat.</p><p><strong>Nima deyish "
                "mumkin?</strong></p>",
        "choices": [
            "Kamida 2 kishi haftaning bir kunida tugʻilgan",
            "Hammasi har xil kunda tugʻilgan",
            "Kamida 3 kishi bir kunda tugʻilgan",
            "Hech narsa deyish mumkin emas",
        ],
        "correct": "Kamida 2 kishi haftaning bir kunida tugʻilgan",
        "explanation": "<p><strong>Kamida 2 kishi.</strong> (PM-97) "
                       "Dirixle prinsipi: 10 ta kaptar, 7 ta uya. "
                       "10 ÷ 7 ≈ 1,43 → yuqoriga yaxlitlab 2. Bu "
                       "ehtimol emas, kafolat.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Stolda 11 ta stakan "
                "agʻdarilgan. Har safar roppa-rosa 2 tasi "
                "agʻdariladi.</p><p><strong>Hammasini toʻgʻrilash "
                "mumkinmi?</strong></p>",
        "choices": [
            "Ha, 6 ta harakatda",
            "Ha, lekin koʻp harakat kerak",
            "Yoʻq — 11 toq, oʻzgarish esa har doim juft",
            "Yoʻq — 11 tub son",
        ],
        "correct": "Yoʻq — 11 toq, oʻzgarish esa har doim juft",
        "explanation": "<p><strong>Yoʻq.</strong> (PM-96) Har bir harakat "
                       "agʻdarilganlar sonini −2, 0 yoki +2 ga "
                       "oʻzgartiradi, demak toqlik saqlanadi va 0 "
                       "(juft) ga hech qachon yetib boʻlmaydi. Sabab "
                       "tub sonlikda emas.</p>",
    },
    # ── Ikkita matnli masala ──────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Afsona kilosi 12 000 soʻmdan "
                "3 kg olma oldi va sotuvchiga 50 000 soʻm berdi.</p>"
                "<p><strong>Qancha qaytim oldi?</strong></p>",
        "choices": ["14 000 soʻm", "24 000 soʻm", "36 000 soʻm",
                    "38 000 soʻm"],
        "correct": "14 000 soʻm",
        "explanation": "<p><strong>14 000 soʻm.</strong> (PM-92) Olma "
                       "12 000 × 3 = 36 000 soʻm. Qaytim: "
                       "50 000 − 36 000 = 14 000. "
                       "<strong>36 000</strong> — toʻlangan pul, "
                       "savol esa qaytimni soʻragan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki sonning yigʻindisi 84, "
                "farqi esa 12.</p><p><strong>Katta son qanday?</strong>"
                "</p>",
        "choices": ["36", "42", "48", "72"],
        "correct": "48",
        "explanation": "<p><strong>48.</strong> (PM-87) Ortiqchani "
                       "qirqamiz: (84 − 12) ÷ 2 = 36 — kichigi. "
                       "Kattasi 36 + 12 = 48. Tekshirish: "
                       "36 + 48 = 84 ✓ va 48 − 36 = 12 ✓ "
                       "<strong>42</strong> — 84 ni teng ikkiga "
                       "boʻlganda chiqadi va farqni yoʻqotadi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-98 Mashq: Teskaridan yurish",
        "tutorial":    "PM-98:",
        "description": (
            "Teskari amallar, teskari tartib, ulushlar bilan orqaga "
            "yurish va oldinga yurib tekshirish. 20 savol."
        ),
        "questions":   Q_PM98,
        **DEFAULTS,
    },
    {
        "title":       "PM-99 Mashq: Namuna izlash va umumlashtirish",
        "tutorial":    "PM-99:",
        "description": (
            "Namunadan n-hadga, 1 dan n gacha yigʻindi, toq sonlar va "
            "kvadratlar, shakldan formulaga. 20 savol."
        ),
        "questions":   Q_PM99,
        **DEFAULTS,
    },
    {
        "title":       "PM-100 Mashq: Yakuniy takror — 100 darsdan hammasi",
        "tutorial":    "PM-100:",
        "description": (
            "Butun kurs boʻyicha yakuniy test: sakkizta blokning "
            "hammasidan savollar. Har bir izohda qaysi darsdan ekani "
            "koʻrsatilgan. 20 savol."
        ),
        "questions":   Q_PM100,
        **DEFAULTS,
    },
]
