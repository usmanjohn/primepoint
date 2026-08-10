# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-4 … PM-6 (boʻlish, amallar tartibi, boʻlinish alomatlari).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_04_06.py --master=prime \\
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
# PM-4 — boʻlish, qoldiqli boʻlish va tekshirish
# =====================================================================

Q_PM4 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>24 ÷ 4 = ?</strong></p>",
        "choices": ["4", "6", "8", "12"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Boʻlish — koʻpaytirishning teskarisi: "
                       "4 ni nechaga koʻpaytirsak 24 chiqadi? 4 × 6 = 24 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>56 ÷ 7 = ?</strong></p>",
        "choices": ["6", "7", "8", "9"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> 7 × 8 = 56, demak 56 ÷ 7 = 8. Bitta "
                       "koʻpaytirishdan ikkita boʻlish chiqadi: 56 ÷ 8 = 7 ham "
                       "toʻgʻri.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Boʻlish natijasi qanday "
                "ataladi?</strong></p>",
        "choices": ["Ayirma", "Boʻlinma", "Koʻpaytma", "Qoldiq"],
        "correct": "Boʻlinma",
        "explanation": "<p><strong>Boʻlinma.</strong> Boʻlinuvchi ÷ boʻluvchi = "
                       "boʻlinma. Qoldiq — boʻlinmay ortib qolgan qism.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>0 ÷ 7 = ?</strong></p>",
        "choices": ["0", "7", "1", "Bunday amal yoʻq"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Hech narsani yetti kishiga boʻlsak, har "
                       "biriga hech narsa tegadi. Diqqat: <strong>7 ÷ 0</strong> esa "
                       "boshqa masala — bunday amalning maʼnosi yoʻq.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>13 ÷ 1 = ?</strong></p>",
        "choices": ["1", "0", "13", "31"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> Bittadan guruhlarga ajratsak, guruhlar "
                       "soni sonning oʻzi boʻladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>37 ÷ 6 = ?</strong></p>",
        "choices": ["5 (qoldiq 7)", "6 (qoldiq 1)", "6 (qoldiq 5)", "7 (qoldiq 1)"],
        "correct": "6 (qoldiq 1)",
        "explanation": "<p><strong>6 (qoldiq 1).</strong> 6 × 6 = 36, 37 − 36 = 1. "
                       "<strong>5 (qoldiq 7)</strong> notoʻgʻri, chunki qoldiq "
                       "boʻluvchidan kichik boʻlishi shart. Tekshirish: "
                       "6 × 6 + 1 = 37 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>96 ÷ 4 = ?</strong></p>",
        "choices": ["18", "22", "24", "26"],
        "correct": "24",
        "explanation": "<p><strong>24.</strong> Razryadlab: 8 oʻnlik ÷ 4 = 2 oʻnlik, "
                       "qolgan 16 ÷ 4 = 4. Tekshirish: 24 × 4 = 96 ✓</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>852 ÷ 4 = ?</strong></p>",
        "choices": ["203", "212", "213", "231"],
        "correct": "213",
        "explanation": "<p><strong>213.</strong> Chapdan: 8 ÷ 4 = 2; 5 ÷ 4 = 1, qoldiq "
                       "1; tushgan 12 ÷ 4 = 3. Tekshirish: 213 × 4 = 852 ✓ Taxmin: "
                       "852 ÷ 4 ≈ 800 ÷ 4 = 200.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>100 ÷ 8 = ?</strong></p>",
        "choices": ["11 (qoldiq 12)", "12 (qoldiq 4)", "12 (qoldiq 8)", "13 (qoldiq 4)"],
        "correct": "12 (qoldiq 4)",
        "explanation": "<p><strong>12 (qoldiq 4).</strong> 8 × 12 = 96, 100 − 96 = 4. "
                       "Qoldiq 4 boʻluvchi 8 dan kichik ✓ Tekshirish: "
                       "12 × 8 + 4 = 100 ✓</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Boʻlinma 7 ga, boʻluvchi 9 ga, "
                "qoldiq 5 ga teng. Boʻlinuvchi qancha?</strong></p>",
        "choices": ["21", "63", "68", "72"],
        "correct": "68",
        "explanation": "<p><strong>68.</strong> Boʻlinma × boʻluvchi + qoldiq = "
                       "7 × 9 + 5 = 63 + 5 = 68. <strong>63</strong> — qoldiqni "
                       "qoʻshishni unutgan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>145 ÷ 5 = ?</strong></p>",
        "choices": ["27", "29", "31", "35"],
        "correct": "29",
        "explanation": "<p><strong>29.</strong> 5 × 29 = 145. Tez usul: 150 ÷ 5 = 30, "
                       "bittasi ortiqcha edi (5 ta), demak 30 − 1 = 29.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Bir sonni 5 ga boʻlganda "
                "qoldiq eng koʻpi bilan qancha boʻlishi mumkin?</strong></p>",
        "choices": ["3", "4", "5", "6"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Qoldiq boʻluvchidan kichik boʻlishi shart. "
                       "Qoldiq 5 chiqsa, u yana bitta toʻliq beshlikni beradi va boʻlinma "
                       "bittaga oshadi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>24 ta konfet 4 tadan qilib paketlanadi.</p><p><strong>24 ÷ 4 = 6 "
                "javobidagi 6 — nima?</strong></p>",
        "choices": ["Paketlar soni", "Bir paketdagi konfetlar soni",
                    "Ortib qolgan konfetlar", "Bolalar soni"],
        "correct": "Paketlar soni",
        "explanation": "<p><strong>Paketlar soni.</strong> Bu boʻlishning ikkinchi "
                       "maʼnosi: “nechta guruh chiqadi?”. Agar masala “24 ta konfetni "
                       "4 bolaga teng boʻling” deganda edi, oʻsha 6 — bir bolaga "
                       "tegadigan konfetlar boʻlardi. Hisob bir xil, javobning nomi "
                       "boshqa.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi tenglik "
                "notoʻgʻri?</strong></p>",
        "choices": ["0 ÷ 9 = 0", "9 ÷ 9 = 1", "9 ÷ 1 = 9", "9 ÷ 0 = 0"],
        "correct": "9 ÷ 0 = 0",
        "explanation": "<p><strong>9 ÷ 0 = 0</strong> notoʻgʻri: nolga boʻlish mumkin "
                       "emas. “0 ni nechaga koʻpaytirsak 9 chiqadi?” — hech qanday "
                       "songa. Qolgan uchtasi toʻgʻri.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>50 ÷ 8 = 6 (qoldiq 2). "
                "“Oxirgi avtobusda nechta bola boʻladi?” degan savolga qaysi son javob "
                "beradi?</strong></p>",
        "choices": ["6", "2", "7", "8"],
        "correct": "2",
        "explanation": "<p><strong>2</strong> — bu qoldiq. <strong>6</strong> toʻla "
                       "avtobuslar soni, <strong>7</strong> esa kerakli avtobuslar "
                       "soni. Bitta boʻlishdan uch xil javob chiqadi — savolni "
                       "oʻqing.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi holatda qoldiqli boʻlish "
                "toʻgʻri yozilgan?</strong></p>",
        "choices": ["29 ÷ 4 = 7 (qoldiq 1)", "29 ÷ 4 = 6 (qoldiq 5)",
                    "29 ÷ 4 = 8 (qoldiq 3)", "29 ÷ 4 = 7 (qoldiq 2)"],
        "correct": "29 ÷ 4 = 7 (qoldiq 1)",
        "explanation": "<p><strong>29 ÷ 4 = 7 (qoldiq 1).</strong> 4 × 7 = 28, "
                       "29 − 28 = 1. Ikkinchi variantda qoldiq (5) boʻluvchidan katta; "
                       "uchinchisida 4 × 8 = 32 — 29 dan oshib ketgan; toʻrtinchisida "
                       "tekshiruv 7 × 4 + 2 = 30 ≠ 29.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Oʻquvchi shunday yozdi: <strong>43 ÷ 8 = 4 (qoldiq 11)</strong>.</p>"
                "<p><strong>Qayerda xato?</strong></p>",
        "choices": ["Qoldiq boʻluvchidan katta — yana bitta guruh chiqadi",
                    "Boʻlinma juda katta olingan",
                    "Boʻlish oʻrniga koʻpaytirish qilingan",
                    "Xato yoʻq"],
        "correct": "Qoldiq boʻluvchidan katta — yana bitta guruh chiqadi",
        "explanation": "<p><strong>Qoldiq boʻluvchidan katta.</strong> 11 &gt; 8, demak "
                       "yana bitta sakkizlik ajratish mumkin edi. Toʻgʻri javob: "
                       "43 ÷ 8 = <strong>5 (qoldiq 3)</strong>, chunki 8 × 5 = 40 va "
                       "43 − 40 = 3.</p>",
    },
    {
        "text": "<p>Masala: “37 bola, har stolga 6 kishi. Kamida nechta stol kerak?” "
                "Oʻquvchi <strong>6 ta</strong> deb javob berdi.</p><p><strong>Nima "
                "unutilgan?</strong></p>",
        "choices": ["Qoldiqdagi bitta bolaga ham stol kerak",
                    "Boʻlish notoʻgʻri bajarilgan",
                    "Stollar soni koʻpaytirilishi kerak edi",
                    "Javob toʻgʻri"],
        "correct": "Qoldiqdagi bitta bolaga ham stol kerak",
        "explanation": "<p><strong>Qoldiqdagi bola.</strong> 37 ÷ 6 = 6 (qoldiq 1): "
                       "oltita stol toʻladi, bitta bola joysiz qoladi. Javob — "
                       "<strong>7 ta stol</strong>. “Kamida nechta kerak?” degan savol "
                       "qoldiqni doim yuqoriga yaxlitlashni talab qiladi.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Kutubxonaga 92 ta yangi kitob keldi. Har bir javonga 7 tadan kitob "
                "sigʻadi.</p><p><strong>Hamma kitob joylashishi uchun kamida nechta "
                "javon kerak?</strong></p>",
        "choices": ["13 ta", "14 ta", "12 ta", "15 ta"],
        "correct": "14 ta",
        "explanation": "<p><strong>14 ta.</strong> 92 ÷ 7 = 13 (qoldiq 1), chunki "
                       "7 × 13 = 91. Oʻn uchta javon toʻladi, bitta kitob ortadi — unga "
                       "ham javon kerak: 13 + 1 = 14. <strong>13</strong> — qoldiqni "
                       "tashlab yuborgan javob.</p>",
    },
    {
        "text": "<p>Bogʻbon 75 ta koʻchatni 8 tadan qilib qatorlarga ekdi.</p>"
                "<p><strong>Nechta toʻla qator chiqdi va nechta koʻchat ortib "
                "qoldi?</strong></p>",
        "choices": ["9 qator, 3 koʻchat", "8 qator, 11 koʻchat",
                    "9 qator, 5 koʻchat", "10 qator, 5 koʻchat"],
        "correct": "9 qator, 3 koʻchat",
        "explanation": "<p><strong>9 qator, 3 koʻchat.</strong> 8 × 9 = 72, "
                       "75 − 72 = 3. Tekshirish: 9 × 8 + 3 = 75 ✓ Bu safar savol "
                       "“toʻla qator” deb soʻragani uchun qoldiq javobga "
                       "qoʻshilmaydi.</p>",
    },
]


# =====================================================================
# PM-5 — amallar tartibi va qavslar
# =====================================================================

Q_PM5 = [
    # 1–5 tanish
    {
        "text": "<p>Hisoblang.</p><p><strong>2 + 3 × 4 = ?</strong></p>",
        "choices": ["14", "20", "24", "9"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> Amallar tartibiga koʻra avval "
                       "koʻpaytirish: 3 × 4 = 12, keyin 2 + 12 = 14. "
                       "<strong>20</strong> — chapdan oʻngga hisoblaganda chiqadi; bu "
                       "eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>(2 + 3) × 4 = ?</strong></p>",
        "choices": ["14", "20", "24", "11"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> Qavs “avval buni hisobla” degani: "
                       "2 + 3 = 5, keyin 5 × 4 = 20. Bitta qavs javobni 14 dan 20 ga "
                       "oʻzgartirdi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ifodada birinchi navbatda nima "
                "bajariladi?</strong></p>",
        "choices": ["Qavs ichidagi amal", "Koʻpaytirish", "Qoʻshish",
                    "Eng chapdagi amal"],
        "correct": "Qavs ichidagi amal",
        "explanation": "<p><strong>Qavs ichidagi amal.</strong> Tartib: qavslar → × va ÷ "
                       "→ + va −. Teng darajadagilar chapdan oʻngga bajariladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>10 − 2 × 3 = ?</strong></p>",
        "choices": ["4", "24", "6", "8"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Avval 2 × 3 = 6, keyin 10 − 6 = 4. "
                       "<strong>24</strong> — avval ayirib, keyin koʻpaytirganda "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>12 ÷ 3 + 5 = ?</strong></p>",
        "choices": ["9", "1", "4", "17"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> Boʻlish qoʻshishdan oldin: 12 ÷ 3 = 4, "
                       "keyin 4 + 5 = 9. <strong>1</strong> — 12 ÷ (3 + 5) deb "
                       "hisoblaganda chiqadi, lekin qavs yoʻq.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>5 + 2 × 6 = ?</strong></p>",
        "choices": ["17", "42", "13", "22"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> 2 × 6 = 12, keyin 5 + 12 = 17. "
                       "<strong>42</strong> — (5 + 2) × 6 ning javobi, lekin savolda "
                       "qavs yoʻq.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>30 − 10 ÷ 5 = ?</strong></p>",
        "choices": ["28", "4", "26", "25"],
        "correct": "28",
        "explanation": "<p><strong>28.</strong> Avval 10 ÷ 5 = 2, keyin 30 − 2 = 28. "
                       "<strong>4</strong> — (30 − 10) ÷ 5 ning javobi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>48 ÷ (2 × 3) = ?</strong></p>",
        "choices": ["8", "72", "24", "9"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Qavs ichi birinchi: 2 × 3 = 6, keyin "
                       "48 ÷ 6 = 8. Qavssiz 48 ÷ 2 × 3 boʻlsa, chapdan oʻngga "
                       "24 × 3 = <strong>72</strong> chiqadi — qavs shuning uchun "
                       "kerak.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>20 − 8 + 3 = ?</strong></p>",
        "choices": ["15", "9", "11", "31"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> Qoʻshish va ayirish teng darajada, "
                       "shuning uchun chapdan oʻngga: 20 − 8 = 12, 12 + 3 = 15. "
                       "<strong>9</strong> — avval 8 + 3 qoʻshib yuborganda "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>24 ÷ 4 × 2 = ?</strong></p>",
        "choices": ["12", "3", "48", "6"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Koʻpaytirish va boʻlish teng darajada — "
                       "chapdagisi birinchi: 24 ÷ 4 = 6, keyin 6 × 2 = 12. "
                       "<strong>3</strong> — avval 4 × 2 = 8 deb koʻpaytirganda "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>100 − (20 + 5) × 3 = ?</strong></p>",
        "choices": ["25", "225", "75", "45"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Qavs: 20 + 5 = 25; koʻpaytirish: "
                       "25 × 3 = 75; ayirish: 100 − 75 = 25. Qavsdagi natija (25) hali "
                       "javob emas — u koʻpaytirishga kiradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>6 × (12 − 4) ÷ 3 = ?</strong></p>",
        "choices": ["16", "22", "48", "8"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> Qavs: 12 − 4 = 8. Keyin chapdan oʻngga: "
                       "6 × 8 = 48, 48 ÷ 3 = 16.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi ifodaning qiymati "
                "boshqalaridan farq qiladi?</strong></p>",
        "choices": ["2 + 3 × 4", "(2 + 3) × 4", "4 × 5", "10 + 10"],
        "correct": "2 + 3 × 4",
        "explanation": "<p><strong>2 + 3 × 4 = 14</strong>, qolgan uchtasi esa 20 ga "
                       "teng: (2 + 3) × 4 = 20, 4 × 5 = 20, 10 + 10 = 20. Qavs shu "
                       "farqni yaratadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi ifodada qavs javobni "
                "umuman oʻzgartirmaydi?</strong></p>",
        "choices": ["8 + (2 × 5)", "(8 + 2) × 5", "(8 − 2) − 5", "8 ÷ (2 × 2)"],
        "correct": "8 + (2 × 5)",
        "explanation": "<p><strong>8 + (2 × 5).</strong> Koʻpaytirish qavssiz ham "
                       "birinchi bajarilar edi: ikkalasi ham 18. Qolganlarida qavs "
                       "tartibni haqiqatdan oʻzgartiradi. Keraksiz qavs qoʻyish xato "
                       "emas, lekin ifodani ogʻirlashtiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>“Avval qoʻshish, keyin "
                "koʻpaytirish” boʻlishi uchun 3 + 5 × 2 ifodasini qanday "
                "yozish kerak?</strong></p>",
        "choices": ["(3 + 5) × 2", "3 + (5 × 2)", "3 × (5 + 2)", "(3 × 5) + 2"],
        "correct": "(3 + 5) × 2",
        "explanation": "<p><strong>(3 + 5) × 2 = 16.</strong> Qavs qoʻshishni birinchi "
                       "oʻringa chiqaradi. 3 + (5 × 2) esa asl ifodaning oʻzi, "
                       "qiymati 13.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>15 − 3 × 2 va (15 − 3) × 2 "
                "ifodalarining qiymatlari qanday?</strong></p>",
        "choices": ["9 va 24", "24 va 9", "9 va 9", "24 va 24"],
        "correct": "9 va 24",
        "explanation": "<p><strong>9 va 24.</strong> Birinchisida 3 × 2 = 6, "
                       "15 − 6 = 9. Ikkinchisida 15 − 3 = 12, 12 × 2 = 24. Bir xil "
                       "sonlar, bir xil amallar — javoblar esa butunlay boshqa.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Oʻquvchi shunday yozdi: <strong>7 + 3 × 2 = 20</strong>.</p>"
                "<p><strong>Qayerda xato?</strong></p>",
        "choices": ["Avval qoʻshish bajarilgan, koʻpaytirish esa birinchi boʻlishi kerak",
                    "Koʻpaytirish notoʻgʻri hisoblangan",
                    "Qavs qoʻyilmagan, shuning uchun ifoda notoʻgʻri",
                    "Xato yoʻq"],
        "correct": "Avval qoʻshish bajarilgan, koʻpaytirish esa birinchi boʻlishi kerak",
        "explanation": "<p><strong>Avval qoʻshish bajarilgan.</strong> "
                       "(7 + 3) × 2 = 20 boʻladi, lekin qavs yoʻq. Toʻgʻri yechim: "
                       "3 × 2 = 6, 7 + 6 = <strong>13</strong>.</p>",
    },
    {
        "text": "<p>Oʻquvchi <strong>36 ÷ 6 × 3 = 2</strong> deb topdi.</p>"
                "<p><strong>Xatoning sababi nima?</strong></p>",
        "choices": ["Koʻpaytirish boʻlishdan oldin bajarilgan",
                    "Boʻlish notoʻgʻri hisoblangan",
                    "Qavs ochilmagan",
                    "Javob toʻgʻri"],
        "correct": "Koʻpaytirish boʻlishdan oldin bajarilgan",
        "explanation": "<p><strong>Koʻpaytirish oldin bajarilgan:</strong> 6 × 3 = 18, "
                       "36 ÷ 18 = 2. Lekin × va ÷ teng darajada, chapdagisi birinchi: "
                       "36 ÷ 6 = 6, 6 × 3 = <strong>18</strong>.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Karim aka 3 kg olma oldi, har kilosi 12 000 soʻmdan. Yana 2 kg uzum "
                "oldi, har kilosi 15 000 soʻmdan. Sotuvchiga 100 000 soʻm berdi.</p>"
                "<p><strong>Qancha qaytim oldi?</strong></p>",
        "choices": ["34 000 soʻm", "66 000 soʻm", "40 000 soʻm", "24 000 soʻm"],
        "correct": "34 000 soʻm",
        "explanation": "<p><strong>34 000 soʻm.</strong> Butun masala bitta ifodada: "
                       "100 000 − (3 × 12 000 + 2 × 15 000) = 100 000 − (36 000 + "
                       "30 000) = 100 000 − 66 000 = 34 000. <strong>66 000</strong> — "
                       "bu xarajat, qaytim emas.</p>",
    },
    {
        "text": "<p>Kinoga 4 ta chipta olindi, har biri 25 000 soʻmdan, va 2 ta popkorn, "
                "har biri 15 000 soʻmdan.</p><p><strong>Jami qancha "
                "toʻlangan?</strong></p>",
        "choices": ["130 000 soʻm", "160 000 soʻm", "100 000 soʻm", "115 000 soʻm"],
        "correct": "130 000 soʻm",
        "explanation": "<p><strong>130 000 soʻm.</strong> "
                       "4 × 25 000 + 2 × 15 000 = 100 000 + 30 000 = 130 000. Bu yerda "
                       "qavs kerak emas — koʻpaytirishlar oʻzi birinchi bajariladi.</p>",
    },
]


# =====================================================================
# PM-6 — boʻlinish alomatlari
# =====================================================================

Q_PM6 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son 2 ga "
                "boʻlinadi?</strong></p>",
        "choices": ["47", "84", "135", "251"],
        "correct": "84",
        "explanation": "<p><strong>84.</strong> Oxirgi raqami 4 — juft. 2 ga boʻlinish "
                       "uchun oxirgi raqam 0, 2, 4, 6 yoki 8 boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son 5 ga "
                "boʻlinadi?</strong></p>",
        "choices": ["1 350", "84", "126", "232"],
        "correct": "1 350",
        "explanation": "<p><strong>1 350.</strong> Oxirgi raqami 0. 5 ga boʻlinish "
                       "alomati: oxirgi raqam 0 yoki 5.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>10 ga boʻlinish alomati "
                "qanday?</strong></p>",
        "choices": ["Oxirgi raqam 0", "Oxirgi raqam juft",
                    "Raqamlar yigʻindisi 10 ga boʻlinadi", "Son besh xonali"],
        "correct": "Oxirgi raqam 0",
        "explanation": "<p><strong>Oxirgi raqam 0.</strong> Chunki 10 ga boʻlish — bu "
                       "razryadlarni bittaga oʻngga surish; buning uchun birliklar "
                       "razryadi boʻsh boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3 ga boʻlinishni bilish uchun "
                "nimaga qaraladi?</strong></p>",
        "choices": ["Raqamlar yigʻindisiga", "Oxirgi raqamga",
                    "Oxirgi ikki raqamga", "Birinchi raqamga"],
        "correct": "Raqamlar yigʻindisiga",
        "explanation": "<p><strong>Raqamlar yigʻindisiga.</strong> Masalan 84: "
                       "8 + 4 = 12, u 3 ga boʻlinadi, demak 84 ham boʻlinadi. Oxirgi "
                       "raqamga qarash faqat 2, 5 va 10 uchun ishlaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>81 soni 2 ga "
                "boʻlinadimi?</strong></p>",
        "choices": ["Ha", "Yoʻq, u toq son", "Faqat qoldiq bilan 2 ga",
                    "Aniqlash uchun boʻlish kerak"],
        "correct": "Yoʻq, u toq son",
        "explanation": "<p><strong>Yoʻq.</strong> Oxirgi raqami 1 — toq. 81 uchga va "
                       "toʻqqizga boʻlinadi (8 + 1 = 9), lekin ikkiga emas.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>5 274 soni 3 ga "
                "boʻlinadimi?</strong></p>",
        "choices": ["Ha, chunki raqamlar yigʻindisi 18", "Yoʻq, chunki oxirgi raqami 4",
                    "Ha, chunki son juft", "Yoʻq, chunki u 3 ga karrali emas"],
        "correct": "Ha, chunki raqamlar yigʻindisi 18",
        "explanation": "<p><strong>Ha.</strong> 5 + 2 + 7 + 4 = 18, 18 uchga boʻlinadi. "
                       "Yigʻindi 9 ga ham boʻlingani uchun 5 274 toʻqqizga ham "
                       "boʻlinadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>3 116 soni 4 ga "
                "boʻlinadimi?</strong></p>",
        "choices": ["Ha, oxirgi ikki raqamdan tuzilgan 16 toʻrtga boʻlinadi",
                    "Yoʻq, chunki 3 116 juda katta",
                    "Ha, chunki oxirgi raqami 6",
                    "Yoʻq, chunki raqamlar yigʻindisi 11"],
        "correct": "Ha, oxirgi ikki raqamdan tuzilgan 16 toʻrtga boʻlinadi",
        "explanation": "<p><strong>Ha.</strong> 4 ga boʻlinish alomati — oxirgi "
                       "<em>ikki</em> raqam: 16 ÷ 4 = 4 ✓ Faqat oxirgi raqamga qarash "
                       "bu yerda ishlamaydi: 3 126 da ham oxirgi raqam 6, lekin 26 "
                       "toʻrtga boʻlinmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>1 350 soni qaysi "
                "sonlarga boʻlinadi?</strong></p>",
        "choices": ["2, 3, 5, 6, 9 va 10 ga", "Faqat 5 va 10 ga",
                    "2, 4 va 5 ga", "Faqat 2 va 3 ga"],
        "correct": "2, 3, 5, 6, 9 va 10 ga",
        "explanation": "<p><strong>2, 3, 5, 6, 9 va 10 ga.</strong> Oxiri 0 → 10 ✓, "
                       "5 ✓, 2 ✓. Raqamlar yigʻindisi 1 + 3 + 5 + 0 = 9 → 3 ✓ va 9 ✓; "
                       "juft va uchga karrali boʻlgani uchun 6 ✓. Oxirgi ikki raqam 50 "
                       "toʻrtga boʻlinmaydi → 4 ✗</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son 9 ga "
                "boʻlinadi?</strong></p>",
        "choices": ["4 725", "84", "1 234", "512"],
        "correct": "4 725",
        "explanation": "<p><strong>4 725.</strong> 4 + 7 + 2 + 5 = 18, u 9 ga boʻlinadi. "
                       "84 da yigʻindi 12 — uchga boʻlinadi, toʻqqizga emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son 6 ga "
                "boʻlinadi?</strong></p>",
        "choices": ["132", "82", "81", "125"],
        "correct": "132",
        "explanation": "<p><strong>132.</strong> Juft ✓ va 1 + 3 + 2 = 6 uchga boʻlinadi "
                       "✓ — ikkala shart bajarildi. 82 juft, lekin 8 + 2 = 10 uchga "
                       "boʻlinmaydi; 81 uchga boʻlinadi, lekin toq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>4 ★ 5 sonining 9 ga "
                "boʻlinishi uchun ★ oʻrniga qaysi raqamni qoʻyish mumkin?</strong></p>",
        "choices": ["0 yoki 9", "3 yoki 6", "faqat 5", "1 yoki 8"],
        "correct": "0 yoki 9",
        "explanation": "<p><strong>0 yoki 9.</strong> Yigʻindi 4 + ★ + 5 = 9 + ★ "
                       "boʻlishi va 9 ga boʻlinishi kerak: ★ = 0 → 9 ✓, ★ = 9 → 18 ✓. "
                       "Demak 405 va 495.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Eng kichik uch xonali va "
                "5 ga boʻlinadigan son qaysi?</strong></p>",
        "choices": ["100", "105", "110", "150"],
        "correct": "100",
        "explanation": "<p><strong>100.</strong> Uch xonali sonlar 100 dan boshlanadi, "
                       "100 ning oxirgi raqami 0 — demak u allaqachon 5 ga (va 10 ga) "
                       "boʻlinadi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Bir son 2 ga ham, 3 ga ham "
                "boʻlinadi. U yana qaysi songa albatta boʻlinadi?</strong></p>",
        "choices": ["6 ga", "5 ga", "9 ga", "4 ga"],
        "correct": "6 ga",
        "explanation": "<p><strong>6 ga.</strong> Bu 6 ning alomatining oʻzi. 4 yoki 9 "
                       "ga boʻlinishi shart emas: 6 ning oʻzi na 4 ga, na 9 ga "
                       "boʻlinadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Bir son 9 ga boʻlinadi. "
                "U 3 ga boʻlinadimi?</strong></p>",
        "choices": ["Ha, doim", "Yoʻq, hech qachon", "Faqat juft boʻlsa",
                    "Faqat uch xonali boʻlsa"],
        "correct": "Ha, doim",
        "explanation": "<p><strong>Ha, doim.</strong> 9 ning oʻzi 3 ga boʻlinadi, "
                       "shuning uchun toʻqqizlardan tuzilgan har qanday son uchlarga "
                       "ham ajraladi. Teskarisi esa notoʻgʻri: 12 uchga boʻlinadi, "
                       "toʻqqizga emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi son 3 ga boʻlinadi, "
                "lekin 9 ga boʻlinmaydi?</strong></p>",
        "choices": ["84", "81", "45", "999"],
        "correct": "84",
        "explanation": "<p><strong>84.</strong> 8 + 4 = 12: uchga boʻlinadi, toʻqqizga "
                       "emas. Qolganlarida yigʻindi 9 ga karrali: 81 → 9, 45 → 9, "
                       "999 → 27.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Boʻlinish alomati qaysi "
                "savolga javob beradi?</strong></p>",
        "choices": ["“Boʻlinadimi yoki yoʻqmi?”", "“Nechta chiqadi?”",
                    "“Qoldiq qancha?”", "“Qaysi son katta?”"],
        "correct": "“Boʻlinadimi yoki yoʻqmi?”",
        "explanation": "<p><strong>“Boʻlinadimi yoki yoʻqmi?”</strong> 84 ning uchga "
                       "boʻlinishini bir soniyada aytasiz, lekin 28 chiqishini bilish "
                       "uchun baribir boʻlish kerak.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Oʻquvchi: “123 uchga boʻlinadi, chunki <strong>oxirgi raqami "
                "3</strong>”, dedi.</p><p><strong>Fikr toʻgʻrimi?</strong></p>",
        "choices": ["Javob toʻgʻri, lekin sabab notoʻgʻri",
                    "Javob ham, sabab ham toʻgʻri",
                    "Javob notoʻgʻri",
                    "123 umuman boʻlinmaydi"],
        "correct": "Javob toʻgʻri, lekin sabab notoʻgʻri",
        "explanation": "<p><strong>Javob toʻgʻri, sabab notoʻgʻri.</strong> 123 uchga "
                       "boʻlinadi, chunki 1 + 2 + 3 = 6. Oxirgi raqamga qarash usuli "
                       "ishlaganda edi, 13 ham uchga boʻlinishi kerak boʻlardi — "
                       "boʻlinmaydi.</p>",
    },
    {
        "text": "<p>Oʻquvchi: “82 juft, demak u <strong>6 ga boʻlinadi</strong>”, "
                "dedi.</p><p><strong>Nima unutilgan?</strong></p>",
        "choices": ["6 uchun 3 ga boʻlinish sharti ham kerak",
                    "6 uchun son toq boʻlishi kerak",
                    "6 uchun oxirgi ikki raqamga qaraladi",
                    "Hech narsa, javob toʻgʻri"],
        "correct": "6 uchun 3 ga boʻlinish sharti ham kerak",
        "explanation": "<p><strong>3 ga boʻlinish sharti.</strong> 8 + 2 = 10, u uchga "
                       "boʻlinmaydi — demak 82 oltiga ham boʻlinmaydi "
                       "(82 ÷ 6 = 13, qoldiq 4). 6 uchun <em>ikkala</em> shart kerak.</p>",
    },
    # 19–20 matnli masala
    {
        "text": "<p>Sinfda 84 ta daftar bor va ularni oʻquvchilarga qoldiqsiz teng "
                "ulashish kerak.</p><p><strong>5, 6 yoki 9 ta oʻquvchi boʻlsa, qaysi "
                "holatda teng ulashish mumkin?</strong></p>",
        "choices": ["Faqat 6 ta oʻquvchi boʻlganda", "Faqat 5 ta oʻquvchi boʻlganda",
                    "6 va 9 ta oʻquvchi boʻlganda", "Uchala holatda ham"],
        "correct": "Faqat 6 ta oʻquvchi boʻlganda",
        "explanation": "<p><strong>Faqat 6 ta.</strong> 84 ning oxirgi raqami 4 → 5 ga "
                       "boʻlinmaydi. Raqamlar yigʻindisi 12 → 9 ga boʻlinmaydi. Lekin "
                       "84 juft va 12 uchga boʻlinadi → 6 ga boʻlinadi: har biriga "
                       "84 ÷ 6 = 14 tadan.</p>",
    },
    {
        "text": "<p>Mashgʻulotda 96 ta bola bor. Ularni teng jamoalarga ajratmoqchimiz: "
                "har jamoada 4, 5 yoki 8 tadan bola boʻlsin.</p><p><strong>Qaysi "
                "holatlarda hech kim ortib qolmaydi?</strong></p>",
        "choices": ["4 va 8 tadan boʻlganda", "Faqat 4 tadan boʻlganda",
                    "5 va 8 tadan boʻlganda", "Uchala holatda ham"],
        "correct": "4 va 8 tadan boʻlganda",
        "explanation": "<p><strong>4 va 8 tadan.</strong> Oxirgi ikki raqam 96 toʻrtga "
                       "boʻlinadi → 96 ÷ 4 = 24 jamoa. 96 ÷ 8 = 12 jamoa. 5 uchun esa "
                       "oxirgi raqam 0 yoki 5 boʻlishi kerak edi — 96 ÷ 5 = 19, "
                       "qoldiq 1, yaʼni bitta bola jamoasiz qoladi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-4 Mashq: Boʻlish, qoldiqli boʻlish va tekshirish",
        "description": "20 savol — boʻlishning ikki maʼnosi, qoldiq qoidasi, ustunda "
                       "boʻlish, tekshirish va qoldiqli matnli masalalar.",
        "tutorial":    "PM-4:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM4,
    },
    {
        "title":       "PM-5 Mashq: Amallar tartibi va qavslar",
        "description": "20 savol — amallar tartibi, qavslar, chapdan oʻngga qoidasi va "
                       "xarid hisobidagi matnli masalalar.",
        "tutorial":    "PM-5:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM5,
    },
    {
        "title":       "PM-6 Mashq: Boʻlinish alomatlari",
        "description": "20 savol — 2, 3, 4, 5, 6, 9 va 10 ga boʻlinish alomatlari, "
                       "ularni birga qoʻllash va teng boʻlish masalalari.",
        "tutorial":    "PM-6:",
        "subject":     "Matematika",
        "level":       "easy",
        "questions":   Q_PM6,
    },
]
