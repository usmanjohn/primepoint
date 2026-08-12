# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-63, PM-64, PM-65 (teng yonli uchburchak,
Pifagor teoremasi, Pifagorning qoʻllanishi).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: `medium` (Blok E, 70 gacha).

⚠️ `choices` EKRANLANADI — HTML teg yoʻq, shuning uchun variantlarda
   x<sup>2</sup> emas, Unicode ² yoziladi.
⚠️ Kumulyativ: toʻrtburchaklar oilasi (PM-66), perimetr (PM-67), yuza
   (PM-68/69) va π (PM-70) YOʻQ. Toʻgʻri toʻrtburchakning burchagi toʻgʻri
   ekani KUZATUV sifatida ishlatiladi (PM-58/61), xossalari oʻrgatilmaydi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_63_65.py --master=prime \\
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
# PM-63 — teng yonli va teng tomonli uchburchak
# =====================================================================

Q_PM63 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qanday uchburchak "
                "teng yonli deyiladi?</strong></p>",
        "choices": [
            "Ikki tomoni teng boʻlgan uchburchak",
            "Uchala tomoni teng boʻlgan uchburchak",
            "Bitta burchagi toʻgʻri boʻlgan uchburchak",
            "Uchala burchagi oʻtkir boʻlgan uchburchak",
        ],
        "correct": "Ikki tomoni teng boʻlgan uchburchak",
        "explanation": "<p><strong>Ikki tomoni teng boʻlgan uchburchak</strong> "
                       "teng yonli deyiladi. Teng boʻlgan ikkitasi — yon "
                       "tomonlar, uchinchisi — asos. <strong>Uchala tomoni "
                       "teng</strong> boʻlsa, u teng tomonli deyiladi: bu "
                       "teng yonlining alohida holati, boshqa nom bilan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Teng yonli uchburchakning "
                "uchidagi burchagi 40°. Asosdagi burchaklar necha gradus?"
                "</strong></p>",
        "choices": ["35°", "70°", "100°", "140°"],
        "correct": "70°",
        "explanation": "<p><strong>70°.</strong> Asosdagi ikki burchak teng, "
                       "ularga 180 − 40 = 140° qoladi, demak har biriga "
                       "140 ÷ 2 = 70°. <strong>140°</strong> — ikkalasining "
                       "yigʻindisi, bitta burchak emas. <strong>35°</strong> "
                       "esa 70 ning yarmi — ikki marta boʻlingan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Teng yonli "
                "uchburchakning asosdagi bitta burchagi 50°. Asosdagi "
                "ikkinchi burchak qancha?</strong></p>",
        "choices": ["40°", "50°", "80°", "130°"],
        "correct": "50°",
        "explanation": "<p><strong>50°.</strong> Asosdagi burchaklar teng — "
                       "bu teng yonli uchburchakning asosiy qoidasi, "
                       "shuning uchun hech narsa hisoblash kerak emas. "
                       "<strong>80°</strong> — uchidagi burchak "
                       "(180 − 50 − 50), asosdagi ikkinchisi emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Teng tomonli "
                "uchburchakning har bir burchagi necha gradus?</strong></p>",
        "choices": ["45°", "60°", "90°", "180°"],
        "correct": "60°",
        "explanation": "<p><strong>60°.</strong> Uchala tomon teng boʻlgani "
                       "uchun uchala burchak ham teng, yigʻindisi esa 180°: "
                       "180 ÷ 3 = 60. <strong>45°</strong> — 180 ÷ 4, "
                       "yaʼni uchburchakda emas, toʻrtburchakda boʻladigan "
                       "hisob.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Teng yonli "
                "uchburchakning teng boʻlmagan uchinchi tomoni ___ "
                "deyiladi.</strong></p>",
        "choices": ["asos", "yon tomon", "gipotenuza", "bissektrisa"],
        "correct": "asos",
        "explanation": "<p><strong>Asos.</strong> Teng boʻlgan ikkitasi — yon "
                       "tomonlar, ularning orasidagi burchak — uchidagi "
                       "burchak, uchinchi tomon esa asos. "
                       "<strong>Bissektrisa</strong> tomon emas — u "
                       "burchakni teng ikkiga boʻluvchi nur (PM-58).</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>Teng yonli uchburchakning "
                "uchidagi burchagi 96°. Asosdagi burchaklar qancha?"
                "</strong></p>",
        "choices": ["42°", "48°", "84°", "132°"],
        "correct": "42°",
        "explanation": "<p><strong>42°.</strong> (180 − 96) ÷ 2 = 84 ÷ 2 = 42. "
                       "Tekshirish: 96 + 42 + 42 = 180 ✓ "
                       "<strong>84°</strong> — ikkalasining yigʻindisi, "
                       "<strong>48°</strong> esa 96 ni ikkiga boʻlish — "
                       "notoʻgʻri burchakdan boshlangan yoʻl.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Teng yonli uchburchakning "
                "uchidagi burchagi toʻgʻri burchak. Asosdagi burchaklar "
                "qancha?</strong></p>",
        "choices": ["30°", "45°", "60°", "90°"],
        "correct": "45°",
        "explanation": "<p><strong>45°.</strong> Toʻgʻri burchak — 90° "
                       "(PM-58), demak (180 − 90) ÷ 2 = 45. Bu uchburchak "
                       "ayni paytda ham teng yonli, ham toʻgʻri burchakli. "
                       "<strong>60°</strong> — teng tomonli uchburchakning "
                       "burchagi, bu yerda toʻgʻri kelmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Teng yonli uchburchakning "
                "asosdagi burchagi 72°. Uchidagi burchak qancha?</strong></p>",
        "choices": ["18°", "36°", "54°", "108°"],
        "correct": "36°",
        "explanation": "<p><strong>36°.</strong> Asosdagi ikkinchi burchak ham "
                       "72°, ikkalasi 144° beradi: 180 − 144 = 36. "
                       "<strong>108°</strong> — 180 − 72, yaʼni faqat bitta "
                       "asos burchagi ayrilgan; ikkinchisi unutilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Teng yonli uchburchakning "
                "asosdagi burchagi 55°. Uchidagi burchak qancha?</strong></p>",
        "choices": ["55°", "70°", "110°", "125°"],
        "correct": "70°",
        "explanation": "<p><strong>70°.</strong> 55 + 55 = 110, keyin "
                       "180 − 110 = 70. <strong>110°</strong> — asosdagi "
                       "ikki burchakning yigʻindisi, <strong>125°</strong> "
                       "esa 180 − 55: ikkinchi asos burchagi hisobga "
                       "olinmagan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Teng yonli uchburchakning "
                "uchidagi burchagi 30°. Asosdagi burchaklar qancha?"
                "</strong></p>",
        "choices": ["15°", "60°", "75°", "150°"],
        "correct": "75°",
        "explanation": "<p><strong>75°.</strong> (180 − 30) ÷ 2 = 150 ÷ 2 = 75. "
                       "Tekshirish: 30 + 75 + 75 = 180 ✓ "
                       "<strong>150°</strong> — boʻlish qadamisiz qolgan "
                       "javob, <strong>15°</strong> esa 30 ning yarmi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Uchburchakning "
                "ikki burchagi 64° va 52°. Bu uchburchak teng yonlimi?"
                "</strong></p>",
        "choices": [
            "Ha — uchinchi burchak ham 64°, demak ikkita burchak teng",
            "Ha — chunki ikkala burchak ham oʻtkir",
            "Yoʻq — 64° va 52° teng emas",
            "Aniqlab boʻlmaydi, tomonlari berilmagan",
        ],
        "correct": "Ha — uchinchi burchak ham 64°, demak ikkita burchak teng",
        "explanation": "<p><strong>Ha.</strong> Uchinchi burchak: "
                       "180 − 64 − 52 = 64°. Endi ikkita burchak 64° ga "
                       "teng, teskari qoidaga koʻra ularning qarshisidagi "
                       "tomonlar ham teng — uchburchak teng yonli. "
                       "«Tomonlari berilmagan» degan javob shuning uchun "
                       "notoʻgʻri: burchaklar tomonlar haqida gapirib "
                       "beradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Teng yonli uchburchakning bitta "
                "burchagi 100°. Qolgan ikkitasi qancha?</strong></p>",
        "choices": ["40° va 40°", "50° va 30°", "80° va 0°", "100° va 20°"],
        "correct": "40° va 40°",
        "explanation": "<p><strong>40° va 40°.</strong> 100° faqat uchidagi "
                       "burchak boʻla oladi: agar u asosdagi boʻlganda, "
                       "ikkitasi 200° boʻlib ketardi — bu 180 dan katta. "
                       "Demak (180 − 100) ÷ 2 = 40. <strong>100° va 20°"
                       "</strong> varianti ikkita 100° ni nazarda tutadi, "
                       "bu esa mumkin emas.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Qaysi gap toʻgʻri?</p><p><strong>Teng yonli va teng "
                "tomonli uchburchak haqida.</strong></p>",
        "choices": [
            "Har bir teng tomonli uchburchak teng yonli hamdir",
            "Har bir teng yonli uchburchak teng tomonli hamdir",
            "Ular butunlay boshqa-boshqa, umumiy joyi yoʻq",
            "Ikkalasining ham burchaklari 60° dan iborat",
        ],
        "correct": "Har bir teng tomonli uchburchak teng yonli hamdir",
        "explanation": "<p><strong>Har bir teng tomonli uchburchak teng yonli "
                       "hamdir.</strong> Uchala tomoni teng boʻlsa, «ikki "
                       "tomoni teng» sharti ham bajarilgan boʻladi. "
                       "Teskarisi esa notoʻgʻri: asosi yon tomonidan "
                       "farq qiladigan teng yonli uchburchak teng tomonli "
                       "emas, va uning burchaklari 60° boʻlishi shart "
                       "emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Teng yonli "
                "uchburchakning bitta burchagi 40°» deyilgan. Qolgan "
                "burchaklar haqida nima deyish mumkin?</strong></p>",
        "choices": [
            "Ikki xil javob bor: 70° va 70° yoki 40° va 100°",
            "Faqat bitta javob bor: 70° va 70°",
            "Faqat bitta javob bor: 40° va 100°",
            "Hech qanday javob topib boʻlmaydi",
        ],
        "correct": "Ikki xil javob bor: 70° va 70° yoki 40° va 100°",
        "explanation": "<p><strong>Ikki xil javob bor.</strong> 40° uchidagi "
                       "burchak boʻlsa, asosdagilar (180 − 40) ÷ 2 = 70° "
                       "boʻladi. 40° asosdagi burchak boʻlsa, ikkinchisi "
                       "ham 40°, uchidagisi esa 180 − 80 = 100°. Masalada "
                       "«uchidagi» yoki «asosdagi» soʻzi boʻlmasa, ikkala "
                       "holatni ham yozish kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Teng yonli "
                "uchburchakning asosdagi burchagi 95° boʻla oladimi?"
                "</strong></p>",
        "choices": [
            "Yoʻq — ikkitasi 190° boʻlib, 180° dan oshib ketadi",
            "Ha — uchidagi burchak kichik boʻlsa boʻladi",
            "Ha — bunda uchidagi burchak −10° boʻladi",
            "Faqat teng tomonli uchburchakda boʻladi",
        ],
        "correct": "Yoʻq — ikkitasi 190° boʻlib, 180° dan oshib ketadi",
        "explanation": "<p><strong>Yoʻq.</strong> Asosdagi burchaklar teng, "
                       "demak 95 + 95 = 190° va bu allaqachon 180° dan "
                       "katta — uchidagi burchakka joy qolmaydi. Shuning "
                       "uchun asosdagi burchak har doim 90° dan kichik. "
                       "Burchak manfiy chiqishi (−10°) javob emas, "
                       "shartning notoʻgʻri ekanini bildiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Teng yonli "
                "uchburchakning uchidagi burchagi 60°. Bu uchburchak "
                "qanday?</strong></p>",
        "choices": [
            "Teng tomonli — uchala burchagi ham 60°",
            "Toʻgʻri burchakli",
            "Oʻtmas burchakli",
            "Faqat teng yonli, boshqa nomi yoʻq",
        ],
        "correct": "Teng tomonli — uchala burchagi ham 60°",
        "explanation": "<p><strong>Teng tomonli.</strong> Asosdagi burchaklar: "
                       "(180 − 60) ÷ 2 = 60°. Demak uchala burchak ham 60° "
                       "va uchala tomon teng boʻlib chiqadi. Bu teng "
                       "yonlilikning eng maxsus holati — uchidagi burchak "
                       "aynan 60° boʻlgan payt.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Uchidagi burchak 40°, "
                "asosdagilarni toping.</strong></p>",
        "choices": [
            "(180 − 40) ÷ 2 = 70°",
            "180 − 40 ÷ 2 = 160°",
            "(180 + 40) ÷ 2 = 110°",
            "180 ÷ 2 − 40 = 50°",
        ],
        "correct": "(180 − 40) ÷ 2 = 70°",
        "explanation": "<p><strong>(180 − 40) ÷ 2 = 70°</strong> toʻgʻri: avval "
                       "uchidagi burchakni ayiramiz, qolganini ikki teng "
                       "burchakka boʻlamiz. <strong>180 − 40 ÷ 2 = 160°"
                       "</strong> — qavs tushib qolgan, amallar tartibiga "
                       "koʻra avval boʻlish bajarilgan (PM-5). 160° bitta "
                       "burchak uchun juda katta: uchtasi 180° dan oshib "
                       "ketadi.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>«Teng yonli uchburchakning "
                "asosdagi burchagi 65°. (1) Ikkinchi asos burchagi ham 65°. "
                "(2) Ularning yigʻindisi 130°. (3) Uchidagi burchak "
                "180 + 130 = 310°.»</strong></p>",
        "choices": [
            "3-qatorda — qoʻshish emas, ayirish kerak: 180 − 130 = 50°",
            "1-qatorda — ikkinchi burchak boshqa boʻlishi kerak",
            "2-qatorda — yigʻindi 130° emas",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "3-qatorda — qoʻshish emas, ayirish kerak: 180 − 130 = 50°",
        "explanation": "<p><strong>3-qatorda xato.</strong> Uchala burchakning "
                       "yigʻindisi 180° boʻlgani uchun uchidagi burchak "
                       "180 dan ayiriladi: 180 − 130 = 50°. Birinchi ikki "
                       "qator toʻgʻri. 310° javobi bitta burchak uchun "
                       "yoyiq burchakdan (180°) ham katta — bu darhol "
                       "koʻrinib turgan belgi.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Dilnoza sayohatda chodir tikdi. Chodirning ikki yon tomoni "
                "teng uzunlikda, ular uchida tutashib 44° burchak hosil "
                "qiladi.</p><p><strong>Chodirning yon tomoni yer bilan qanday "
                "burchak hosil qiladi?</strong></p>",
        "choices": ["34°", "44°", "68°", "136°"],
        "correct": "68°",
        "explanation": "<p><strong>68°.</strong> Yer — chodirning asosi, yon "
                       "tomonlar teng, demak uchburchak teng yonli: "
                       "(180 − 44) ÷ 2 = 136 ÷ 2 = 68°. Tekshirish: "
                       "68 + 68 + 44 = 180 ✓ <strong>136°</strong> — "
                       "ikkalasining yigʻindisi, bitta burchak emas.</p>",
    },
    {
        "text": "<p>Karim aka tom yasayapti. Tomning ikki yon yogʻochi teng "
                "uzunlikda va ularning har biri gorizontal devor bilan 28° "
                "burchak hosil qiladi.</p><p><strong>Yogʻochlar tomning "
                "uchida qanday burchak hosil qiladi?</strong></p>",
        "choices": ["56°", "76°", "124°", "152°"],
        "correct": "124°",
        "explanation": "<p><strong>124°.</strong> Yon yogʻochlar teng, demak "
                       "asosdagi ikki burchak ham 28° dan: 28 + 28 = 56, "
                       "keyin 180 − 56 = 124°. <strong>152°</strong> — "
                       "180 − 28, yaʼni ikkinchi asos burchagi unutilgan. "
                       "<strong>56°</strong> esa asosdagi ikki burchakning "
                       "yigʻindisi.</p>",
    },
]


# =====================================================================
# PM-64 — Pifagor teoremasi
# =====================================================================

Q_PM64 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Toʻgʻri burchakli "
                "uchburchakda gipotenuza qaysi tomon?</strong></p>",
        "choices": [
            "Toʻgʻri burchak qarshisidagi tomon",
            "Toʻgʻri burchakni hosil qiluvchi tomonlardan biri",
            "Eng qisqa tomon",
            "Asosdagi tomon",
        ],
        "correct": "Toʻgʻri burchak qarshisidagi tomon",
        "explanation": "<p><strong>Toʻgʻri burchak qarshisidagi tomon.</strong> "
                       "Toʻgʻri burchakni hosil qilgan ikkita tomon — "
                       "katetlar. Gipotenuza esa har doim eng <em>uzun</em> "
                       "tomon, chunki eng katta burchak (90°) qarshisida "
                       "turadi (PM-62).</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Katetlari 3 va 4 boʻlgan toʻgʻri "
                "burchakli uchburchakning gipotenuzasi qancha?</strong></p>",
        "choices": ["5", "7", "12", "25"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> c² = 3² + 4² = 9 + 16 = 25, "
                       "c = √25 = 5. <strong>7</strong> — katetlarning "
                       "oʻzini qoʻshish (3 + 4), <strong>25</strong> esa "
                       "ildiz chiqarish qadami tushib qolgan javob.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>a² + b² = c² "
                "formulasi ___ uchburchakda ishlaydi.</strong></p>",
        "choices": [
            "faqat toʻgʻri burchakli",
            "har qanday",
            "faqat teng yonli",
            "faqat teng tomonli",
        ],
        "correct": "faqat toʻgʻri burchakli",
        "explanation": "<p><strong>Faqat toʻgʻri burchakli</strong> "
                       "uchburchakda. Boshqa uchburchakka qoʻllash — eng "
                       "jimgina yashiringan xato: masalan 5, 6, 7 "
                       "tomonlarda 25 + 36 = 61, 7² esa 49 — tenglik "
                       "bajarilmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Katetlari 6 va 8 boʻlgan "
                "uchburchakning gipotenuzasi qancha?</strong></p>",
        "choices": ["10", "14", "28", "100"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> c² = 36 + 64 = 100, "
                       "c = √100 = 10. Bu 3-4-5 uchligining ikki barobari. "
                       "<strong>14</strong> — katetlarni qoʻshish (6 + 8), "
                       "<strong>100</strong> — ildiz chiqarilmagan "
                       "javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Agar c² = 100 boʻlsa, c "
                "qancha?</strong></p>",
        "choices": ["10", "20", "50", "10 000"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> Kvadratning teskari amali — "
                       "kvadrat ildiz (PM-13): √100 = 10, chunki "
                       "10 × 10 = 100. <strong>50</strong> — ildiz "
                       "chiqarish oʻrniga ikkiga boʻlish; tekshirib "
                       "koʻring: 50 × 50 = 2500, 100 emas.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Hisoblang.</p><p><strong>Katetlari 9 va 12. Gipotenuza "
                "qancha?</strong></p>",
        "choices": ["15", "21", "108", "225"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> c² = 81 + 144 = 225, "
                       "c = √225 = 15. Bu 3-4-5 uchligining uch barobari "
                       "(9, 12, 15). <strong>21</strong> — 9 + 12, "
                       "<strong>225</strong> — ildizsiz qolgan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Katetlari 5 va 12. Gipotenuza "
                "qancha?</strong></p>",
        "choices": ["13", "17", "60", "169"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> c² = 25 + 144 = 169, "
                       "c = √169 = 13. Bu 5-12-13 uchligi — yod olishga "
                       "arziydi. <strong>17</strong> — katetlarning "
                       "yigʻindisi, <strong>60</strong> esa ularning "
                       "koʻpaytmasi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Gipotenuzasi 13, bitta kateti 5. "
                "Ikkinchi katet qancha?</strong></p>",
        "choices": ["8", "12", "14", "18"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Katet izlanayotgani uchun "
                       "ayiramiz: b² = 169 − 25 = 144, b = √144 = 12. "
                       "<strong>8</strong> — 13 − 5, yaʼni kvadratsiz "
                       "ayirish. <strong>14</strong> esa "
                       "√(169 + 25) ≈ 13,9 — qoʻshish tomoni notoʻgʻri "
                       "tanlangan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Gipotenuzasi 25, bitta kateti 7. "
                "Ikkinchi katet qancha?</strong></p>",
        "choices": ["18", "24", "26", "32"],
        "correct": "24",
        "explanation": "<p><strong>24.</strong> b² = 625 − 49 = 576, "
                       "b = √576 = 24. Tekshirish: 49 + 576 = 625 ✓ "
                       "<strong>18</strong> — 25 − 7 (kvadratsiz ayirish), "
                       "<strong>26</strong> esa gipotenuzadan uzun — katet "
                       "hech qachon gipotenuzadan uzun boʻlmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Katetlari 8 va 15. Gipotenuza "
                "qancha?</strong></p>",
        "choices": ["17", "23", "120", "289"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> c² = 64 + 225 = 289, "
                       "c = √289 = 17. Bu 8-15-17 uchligi. "
                       "<strong>23</strong> — 8 + 15, <strong>289</strong> "
                       "— ildiz chiqarilmagan javob.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Gipotenuzasi 10, bitta kateti 6. "
                "Ikkinchi katet qancha?</strong></p>",
        "choices": ["4", "8", "11", "16"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> b² = 100 − 36 = 64, "
                       "b = √64 = 8. Bu yana 6-8-10 uchligi. "
                       "<strong>4</strong> — 10 − 6, kvadratlarsiz "
                       "ayirilgan. <strong>11</strong> esa taxminan "
                       "√(100 + 36) — ayirish oʻrniga qoʻshilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Katetlari 20 va 21. Gipotenuza "
                "qancha?</strong></p>",
        "choices": ["29", "41", "420", "841"],
        "correct": "29",
        "explanation": "<p><strong>29.</strong> c² = 400 + 441 = 841, "
                       "c = √841 = 29 (29 × 29 = 841). "
                       "<strong>41</strong> — katetlarning yigʻindisi; u "
                       "uchburchak tengsizligiga ham zid boʻlardi, chunki "
                       "20 + 21 = 41 da uchburchak yassilanib qoladi "
                       "(PM-62).</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Tomonlari 5, 6 va 7 "
                "boʻlgan uchburchak toʻgʻri burchaklimi?</strong></p>",
        "choices": [
            "Yoʻq — 25 + 36 = 61, 7² esa 49",
            "Ha — 5 + 6 > 7 boʻlgani uchun",
            "Ha — uchala tomoni ham har xil boʻlgani uchun",
            "Aniqlab boʻlmaydi, burchaklari berilmagan",
        ],
        "correct": "Yoʻq — 25 + 36 = 61, 7² esa 49",
        "explanation": "<p><strong>Yoʻq.</strong> Teskari teoremani tekshiramiz: "
                       "eng katta tomon 7, demak 5² + 6² = 7² boʻlishi "
                       "kerak edi. 25 + 36 = 61, 49 esa emas — tenglik "
                       "bajarilmaydi. <strong>5 + 6 &gt; 7</strong> "
                       "sharti faqat uchburchak umuman mavjudligini "
                       "bildiradi (PM-62), burchak haqida hech narsa "
                       "aytmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Tomonlari 8, 15 va "
                "17 boʻlgan uchburchak toʻgʻri burchaklimi?</strong></p>",
        "choices": [
            "Ha — 64 + 225 = 289 = 17²",
            "Yoʻq — 8 + 15 = 23, bu 17 dan katta",
            "Ha — chunki 17 toq son",
            "Yoʻq — uchala tomoni har xil",
        ],
        "correct": "Ha — 64 + 225 = 289 = 17²",
        "explanation": "<p><strong>Ha.</strong> Eng katta tomon 17 ni "
                       "gipotenuza deb olamiz: 8² + 15² = 64 + 225 = 289 "
                       "va 17² = 289 — tenglik bajarildi, demak burchak "
                       "toʻgʻri. 8 + 15 = 23 &gt; 17 boʻlishi esa faqat "
                       "uchburchak mavjudligini koʻrsatadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Hisobda "
                "c² = 144 chiqdi. Endi nima qilinadi?</strong></p>",
        "choices": [
            "Ildiz chiqariladi: c = 12",
            "Javob yoziladi: c = 144",
            "Ikkiga boʻlinadi: c = 72",
            "Ikkiga koʻpaytiriladi: c = 288",
        ],
        "correct": "Ildiz chiqariladi: c = 12",
        "explanation": "<p><strong>Ildiz chiqariladi: c = √144 = 12.</strong> "
                       "c² — tomonning kvadrati, tomonning oʻzi emas. "
                       "<strong>72</strong> — ikkiga boʻlish; tekshiring: "
                       "72 × 72 = 5184, 144 emas. Bu qadamni unutish — "
                       "mavzudagi eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qachon qoʻshamiz, "
                "qachon ayiramiz?</strong></p>",
        "choices": [
            "Gipotenuza nomaʼlum — qoʻshamiz; katet nomaʼlum — ayiramiz",
            "Har doim qoʻshamiz",
            "Gipotenuza nomaʼlum — ayiramiz; katet nomaʼlum — qoʻshamiz",
            "Uchburchak katta boʻlsa qoʻshamiz, kichik boʻlsa ayiramiz",
        ],
        "correct": "Gipotenuza nomaʼlum — qoʻshamiz; katet nomaʼlum — ayiramiz",
        "explanation": "<p><strong>Gipotenuza nomaʼlum — qoʻshamiz; katet "
                       "nomaʼlum — ayiramiz.</strong> Formulada "
                       "a² + b² = c², yaʼni c² yolgʻiz tomonda turadi. "
                       "Adashsangiz javobni taqqoslang: gipotenuza har "
                       "ikkala katetdan ham uzun chiqishi shart.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Gipotenuzasi 13, bitta "
                "kateti 5. Ikkinchi katetni toping.</strong></p>",
        "choices": [
            "b² = 169 − 25 = 144, b = 12",
            "b² = 169 + 25 = 194, b ≈ 13,9",
            "b = 13 − 5 = 8",
            "b = 13 + 5 = 18",
        ],
        "correct": "b² = 169 − 25 = 144, b = 12",
        "explanation": "<p><strong>b² = 169 − 25 = 144, b = 12</strong> toʻgʻri. "
                       "Gipotenuza — eng katta son, u yigʻindi tomonda "
                       "turadi, shuning uchun katet izlanganda ayiriladi. "
                       "<strong>194</strong> varianti gipotenuzani katet "
                       "deb hisoblaydi va javob 13,9 — gipotenuzadan uzun "
                       "katet chiqib qoladi, bu mumkin emas.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>«Katetlari 6 va 8. "
                "(1) c² = 6² + 8². (2) c² = 36 + 64 = 100. (3) c = 100.»"
                "</strong></p>",
        "choices": [
            "3-qatorda — ildiz chiqarilmagan: c = √100 = 10",
            "1-qatorda — formula notoʻgʻri yozilgan",
            "2-qatorda — 36 + 64 = 100 emas",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "3-qatorda — ildiz chiqarilmagan: c = √100 = 10",
        "explanation": "<p><strong>3-qatorda xato.</strong> 100 — bu "
                       "gipotenuzaning <em>kvadrati</em>, gipotenuzaning "
                       "oʻzi emas: c = √100 = 10. Birinchi ikki qator "
                       "toʻgʻri. Javobni tekshirish oson: 100 uzunlik "
                       "katetlardan (6 va 8) oʻn barobar katta boʻlib "
                       "qoladi — bu mumkin emas.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Afsonaning bogʻi toʻgʻri toʻrtburchak shaklida: bir tomoni "
                "9 metr, ikkinchisi 12 metr. U bogʻ boʻylab bir burchakdan "
                "qarama-qarshi burchakka toʻgʻri yoʻlak yotqizmoqchi.</p>"
                "<p><strong>Yoʻlak necha metr boʻladi?</strong></p>",
        "choices": ["15 m", "21 m", "108 m", "225 m"],
        "correct": "15 m",
        "explanation": "<p><strong>15 m.</strong> Toʻgʻri toʻrtburchakning "
                       "burchagi toʻgʻri burchak, demak yoʻlak — "
                       "gipotenuza: 9² + 12² = 81 + 144 = 225, "
                       "√225 = 15. <strong>21 m</strong> — chetlab "
                       "yurgandagi yoʻl (9 + 12), toʻgʻri yoʻlak esa undan "
                       "qisqa boʻlishi kerak (PM-62).</p>",
    },
    {
        "text": "<p>Maktab hovlisi toʻgʻri toʻrtburchak: eni 15 metr, uzunligi "
                "20 metr. Jasur bir burchakdan qarama-qarshi burchakka "
                "boradi. U yo ikki tomon boʻylab chetlab boradi, yo hovlini "
                "kesib oʻtadi.</p><p><strong>Kesib oʻtsa, necha metr "
                "tejaydi?</strong></p>",
        "choices": ["5 m", "10 m", "25 m", "35 m"],
        "correct": "10 m",
        "explanation": "<p><strong>10 m.</strong> Chetlab: 15 + 20 = 35 m. "
                       "Kesib: d² = 225 + 400 = 625, d = √625 = 25 m "
                       "(bu 3-4-5 uchligining besh barobari). Tejaladi: "
                       "35 − 25 = 10 m. <strong>25 m</strong> — "
                       "diagonalning oʻzi, tejalgan masofa emas; savolni "
                       "oxirigacha oʻqish kerak.</p>",
    },
]


# =====================================================================
# PM-65 — Pifagorning qoʻllanishi
# =====================================================================

Q_PM65 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Narvon devorga "
                "suyalgan. Bu uchburchakda gipotenuza qaysi?</strong></p>",
        "choices": [
            "Narvonning oʻzi",
            "Devorning balandligi",
            "Narvon oyogʻidan devorgacha boʻlgan masofa",
            "Uchalasi ham teng",
        ],
        "correct": "Narvonning oʻzi",
        "explanation": "<p><strong>Narvonning oʻzi.</strong> Toʻgʻri burchakni "
                       "devor bilan yer hosil qiladi — demak ular "
                       "katetlar. Narvon qiya turibdi va toʻgʻri burchakka "
                       "tegmaydi, shuning uchun u gipotenuza va uchtasining "
                       "eng uzuni.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Narvonning uzunligi 5 m, "
                "oyogʻi devordan 3 m narida. Narvonning uchi qanday "
                "balandlikka yetadi?</strong></p>",
        "choices": ["2 m", "4 m", "5,8 m", "8 m"],
        "correct": "4 m",
        "explanation": "<p><strong>4 m.</strong> Narvon — gipotenuza, demak "
                       "ayiramiz: a² = 25 − 9 = 16, a = 4. "
                       "<strong>5,8 m</strong> — √(25 + 9) = √34, yaʼni "
                       "qoʻshish tomoni notoʻgʻri tanlangan; u narvonning "
                       "oʻzidan ham uzun chiqadi, bu esa mumkin emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Narvonning uzunligi 10 m, "
                "oyogʻi devordan 6 m narida. Narvonning uchi qanday "
                "balandlikka yetadi?</strong></p>",
        "choices": ["4 m", "8 m", "11,7 m", "16 m"],
        "correct": "8 m",
        "explanation": "<p><strong>8 m.</strong> a² = 100 − 36 = 64, a = 8. "
                       "Bu 6-8-10 uchligi. <strong>4 m</strong> — 10 − 6, "
                       "kvadratlarsiz ayirish; <strong>16 m</strong> esa "
                       "ildiz chiqarilmagan javob.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Teng yonli tomning "
                "balandligini topishda katet sifatida asosning ___ "
                "olinadi.</strong></p>",
        "choices": ["yarmi", "oʻzi", "ikki barobari", "kvadrati"],
        "correct": "yarmi",
        "explanation": "<p><strong>Yarmi.</strong> Uchdan asosga tushirilgan "
                       "perpendikulyar teng yonli uchburchakni ikkita bir "
                       "xil toʻgʻri burchakli uchburchakka boʻladi, "
                       "shuning uchun katet — asosning yarmi. Butun asos "
                       "olinsa, kvadrat manfiy chiqib qoladi — bu darhol "
                       "xatoni koʻrsatadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>A(0; 0) va B(3; 4) nuqtalar "
                "orasidagi masofa qancha?</strong></p>",
        "choices": ["5 birlik", "7 birlik", "12 birlik", "25 birlik"],
        "correct": "5 birlik",
        "explanation": "<p><strong>5 birlik.</strong> Gorizontal qadam 3, "
                       "vertikal qadam 4, ular perpendikulyar: "
                       "d² = 9 + 16 = 25, d = 5. <strong>7</strong> — "
                       "qadamlarni qoʻshish (3 + 4); bu katakchalar "
                       "boʻylab yurgandagi yoʻl, toʻgʻri masofa emas.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Masalani yeching.</p><p><strong>Narvonning uzunligi 13 m, "
                "oyogʻi devordan 5 m narida. Narvonning uchi qanday "
                "balandlikka yetadi?</strong></p>",
        "choices": ["8 m", "12 m", "13,9 m", "18 m"],
        "correct": "12 m",
        "explanation": "<p><strong>12 m.</strong> a² = 169 − 25 = 144, "
                       "a = 12. Bu 5-12-13 uchligi. <strong>8 m</strong> "
                       "— 13 − 5, kvadratlarsiz ayirish. "
                       "<strong>13,9 m</strong> esa √194 — qoʻshib "
                       "yuborilgan javob, u narvondan uzun.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Teng yonli tomning asosi "
                "16 m, yon yogʻochlari 17 m dan. Tomning balandligi "
                "qancha?</strong></p>",
        "choices": ["1 m", "8 m", "15 m", "23 m"],
        "correct": "15 m",
        "explanation": "<p><strong>15 m.</strong> Asosning yarmi: "
                       "16 ÷ 2 = 8. h² = 289 − 64 = 225, h = 15 "
                       "(8-15-17 uchligi). <strong>1 m</strong> — "
                       "17 − 16, yaʼni umuman Pifagorsiz ayirish; "
                       "<strong>8 m</strong> — asosning yarmi, balandlik "
                       "emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Teng yonli tomning asosi "
                "24 m, yon yogʻochlari 13 m dan. Tomning balandligi "
                "qancha?</strong></p>",
        "choices": ["5 m", "11 m", "12 m", "25 m"],
        "correct": "5 m",
        "explanation": "<p><strong>5 m.</strong> Asosning yarmi: "
                       "24 ÷ 2 = 12. h² = 169 − 144 = 25, h = 5. Tom past "
                       "va keng — asos yon tomondan ancha uzun. "
                       "<strong>11 m</strong> — 24 − 13, "
                       "<strong>12 m</strong> esa asosning yarmi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>A(2; 1) va B(10; 7) nuqtalar "
                "orasidagi masofa qancha?</strong></p>",
        "choices": ["10 birlik", "14 birlik", "20 birlik", "100 birlik"],
        "correct": "10 birlik",
        "explanation": "<p><strong>10 birlik.</strong> Gorizontal qadam "
                       "|10 − 2| = 8, vertikal qadam |7 − 1| = 6. "
                       "d² = 64 + 36 = 100, d = 10. <strong>14</strong> — "
                       "qadamlarni qoʻshish (8 + 6), <strong>100</strong> "
                       "— ildiz chiqarilmagan javob.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Ustunning balandligi 9 m. "
                "Uning uchidan yerga arqon tortilgan; arqonning yerdagi uchi "
                "ustun tagidan 12 m narida. Arqon necha metr?</strong></p>",
        "choices": ["3 m", "15 m", "21 m", "225 m"],
        "correct": "15 m",
        "explanation": "<p><strong>15 m.</strong> Arqon — gipotenuza: "
                       "c² = 81 + 144 = 225, c = 15. Bu safar arqon "
                       "ustundan ham, yerdagi masofadan ham uzun — "
                       "gipotenuza har doim shunday. <strong>21 m</strong> "
                       "— 9 + 12, <strong>3 m</strong> esa 12 − 9.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Narvonning uzunligi 6 m, "
                "oyogʻi devordan 2 m narida. Narvonning uchi taxminan qanday "
                "balandlikka yetadi?</strong></p>",
        "choices": ["4 m", "5,7 m", "6,3 m", "8 m"],
        "correct": "5,7 m",
        "explanation": "<p><strong>Taxminan 5,7 m.</strong> a² = 36 − 4 = 32. "
                       "32 aniq kvadrat emas: 25 &lt; 32 &lt; 36, demak "
                       "javob 5 va 6 orasida. 5,7² = 32,49 — 32 ga eng "
                       "yaqini. <strong>4 m</strong> — 6 − 2, "
                       "<strong>6,3 m</strong> esa narvondan uzun, bu "
                       "mumkin emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Bekzod uydan 300 m "
                "sharqqa, soʻng 400 m shimolga yurdi. Uydan hozirgi joyigacha "
                "toʻgʻri masofa qancha?</strong></p>",
        "choices": ["100 m", "500 m", "700 m", "1200 m"],
        "correct": "500 m",
        "explanation": "<p><strong>500 m.</strong> Sharq va shimol "
                       "perpendikulyar yoʻnalishlar: d² = 90 000 + "
                       "160 000 = 250 000, d = 500. Bu 3-4-5 uchligining "
                       "yuz barobari. <strong>700 m</strong> — bosib "
                       "oʻtgan yoʻli (300 + 400), toʻgʻri masofa "
                       "emas.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>A(1; 2) va B(5; 5) "
                "nuqtalar orasida: qaysi son toʻgʻri masofani beradi?"
                "</strong></p>",
        "choices": [
            "5 — chunki 4² + 3² = 25 va √25 = 5",
            "7 — chunki 4 + 3 = 7",
            "12 — chunki 4 × 3 = 12",
            "25 — chunki 16 + 9 = 25",
        ],
        "correct": "5 — chunki 4² + 3² = 25 va √25 = 5",
        "explanation": "<p><strong>5.</strong> Qadamlarning oʻzi emas, "
                       "kvadratlari qoʻshiladi, keyin ildiz chiqariladi. "
                       "<strong>7</strong> — katakchalar boʻylab yurgandagi "
                       "yoʻl (avval oʻngga, keyin yuqoriga), u toʻgʻri "
                       "masofadan har doim uzunroq (PM-62). "
                       "<strong>25</strong> — masofaning kvadrati.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Kvadrat shaklidagi "
                "maydonning tomoni 10 m. Uning diagonali qaysi ikki butun son "
                "orasida?</strong></p>",
        "choices": [
            "14 va 15 orasida",
            "10 va 11 orasida",
            "19 va 20 orasida",
            "Aniq 20 ga teng",
        ],
        "correct": "14 va 15 orasida",
        "explanation": "<p><strong>14 va 15 orasida.</strong> "
                       "d² = 100 + 100 = 200. 14² = 196 va 15² = 225, "
                       "demak 196 &lt; 200 &lt; 225 va 14 &lt; d &lt; 15 "
                       "(PM-13). <strong>20</strong> — tomonlarni qoʻshish "
                       "(10 + 10), bu diagonal emas. Javob butun "
                       "chiqmasligi normal.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Katetlari 60 sm va "
                "0,8 m. Gipotenuza qancha?</strong></p>",
        "choices": ["1 m", "1,4 m", "60,8 m", "Hisoblab boʻlmaydi"],
        "correct": "1 m",
        "explanation": "<p><strong>1 m.</strong> Avval birliklarni "
                       "tenglashtiramiz: 60 sm = 0,6 m. Keyin "
                       "c² = 0,36 + 0,64 = 1, c = 1 m. "
                       "<strong>1,4 m</strong> — 0,6 + 0,8, yaʼni "
                       "tomonlarni qoʻshish. Har xil birlikdagi sonlarni "
                       "toʻgʻridan-toʻgʻri qoʻshib boʻlmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Tom masalasida asos "
                "12 m, yon yogʻoch 10 m. Kimdir h² = 100 − 144 deb yozdi. Bu "
                "nimani bildiradi?</strong></p>",
        "choices": [
            "Asosning yarmi emas, butuni olingan — 100 − 36 boʻlishi kerak",
            "Yon yogʻoch katet deb olingan",
            "Hisob toʻgʻri, javob manfiy son",
            "Tom bunday oʻlchamda boʻlishi mumkin emas",
        ],
        "correct": "Asosning yarmi emas, butuni olingan — 100 − 36 boʻlishi kerak",
        "explanation": "<p><strong>Asosning yarmi emas, butuni olingan.</strong> "
                       "Perpendikulyar asosni ikkiga boʻladi, demak katet "
                       "12 emas, 6: h² = 100 − 36 = 64, h = 8 m. Kvadrat "
                       "manfiy chiqishi mumkin emas — bu har doim "
                       "boshlangʻich sonda xato borligini bildiradi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Narvon 5 m, oyogʻi "
                "devordan 3 m narida. Balandlikni toping.</strong></p>",
        "choices": [
            "a² = 25 − 9 = 16, a = 4 m",
            "a² = 25 + 9 = 34, a ≈ 5,8 m",
            "a = 5 − 3 = 2 m",
            "a = 5 + 3 = 8 m",
        ],
        "correct": "a² = 25 − 9 = 16, a = 4 m",
        "explanation": "<p><strong>a² = 25 − 9 = 16, a = 4 m</strong> toʻgʻri. "
                       "Narvon gipotenuza boʻlgani uchun uning kvadratidan "
                       "ayiriladi. <strong>5,8 m</strong> javobi narvonning "
                       "oʻzidan (5 m) uzun — bu darhol koʻrinadigan "
                       "belgi: katet gipotenuzadan uzun boʻlmaydi.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p><strong>«A(2; 3) va B(6; 6). "
                "(1) Gorizontal qadam 4. (2) Vertikal qadam 3. "
                "(3) Masofa 4 + 3 = 7.»</strong></p>",
        "choices": [
            "3-qatorda — kvadratlari qoʻshiladi: √(16 + 9) = 5",
            "1-qatorda — gorizontal qadam 4 emas",
            "2-qatorda — vertikal qadam 3 emas",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "3-qatorda — kvadratlari qoʻshiladi: √(16 + 9) = 5",
        "explanation": "<p><strong>3-qatorda xato.</strong> Qadamlarning oʻzi "
                       "emas, kvadratlari qoʻshiladi: d² = 16 + 9 = 25, "
                       "d = 5. Birinchi ikki qator toʻgʻri: |6 − 2| = 4 va "
                       "|6 − 3| = 3. 7 soni — katakchalar boʻylab "
                       "yurgandagi yoʻl.</p>",
    },

    # 19–20 matnli masala
    {
        "text": "<p>Karim aka hovliga 8 metrli ustun tikladi. Ustunning "
                "uchidan yerga arqon tortadi; arqonning yerdagi uchi ustun "
                "tagidan 6 metr narida qoqiladi. Shunday arqondan 4 ta kerak, "
                "arqonning bir metri 7000 soʻm turadi.</p><p><strong>Arqonlar "
                "uchun jami qancha pul kerak?</strong></p>",
        "choices": ["70 000 soʻm", "196 000 soʻm", "280 000 soʻm", "392 000 soʻm"],
        "correct": "280 000 soʻm",
        "explanation": "<p><strong>280 000 soʻm.</strong> Bitta arqon — "
                       "gipotenuza: c² = 64 + 36 = 100, c = 10 m. Toʻrtta "
                       "arqon: 10 × 4 = 40 m. Narxi: 40 × 7000 = 280 000 "
                       "soʻm. <strong>70 000</strong> — faqat bitta "
                       "arqonning narxi (10 × 7000); savol jamisini "
                       "soʻrayapti.</p>",
    },
    {
        "text": "<p>Dilnoza yangi shkaf oldi. Uni uyga kiritish uchun eshikdan "
                "yotqizib oʻtkazish kerak. Eshikning balandligi 2 m, eni "
                "1,5 m. Shkafning uzunligi 2,4 m.</p><p><strong>Shkaf "
                "eshikdan diagonal boʻylab oʻtadimi?</strong></p>",
        "choices": [
            "Ha — eshik diagonali 2,5 m, shkaf esa 2,4 m",
            "Yoʻq — eshik diagonali 1,3 m, shkaf undan uzun",
            "Ha — eshik diagonali 3,5 m",
            "Aniqlab boʻlmaydi, shkafning eni berilmagan",
        ],
        "correct": "Ha — eshik diagonali 2,5 m, shkaf esa 2,4 m",
        "explanation": "<p><strong>Ha, oʻtadi.</strong> Eshikning diagonali — "
                       "gipotenuza: d² = 2² + 1,5² = 4 + 2,25 = 6,25, "
                       "d = √6,25 = 2,5 m. Shkaf 2,4 m — diagonaldan "
                       "qisqa, demak sigʻadi. <strong>3,5 m</strong> — "
                       "tomonlarni qoʻshish (2 + 1,5), diagonal esa har "
                       "doim yigʻindidan kichik (PM-62).</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-63 Mashq: Teng yonli va teng tomonli uchburchak",
        "tutorial":    "PM-63:",
        "description": (
            "Teng yonli uchburchakning qismlari, asosdagi burchaklar "
            "tengligi va uning teskarisi, teng tomonli uchburchakning 60° "
            "burchaklari. 20 savol."
        ),
        "questions":   Q_PM63,
        **DEFAULTS,
    },
    {
        "title":       "PM-64 Mashq: Pifagor teoremasi",
        "tutorial":    "PM-64:",
        "description": (
            "Katet va gipotenuza, a² + b² = c², gipotenuzani va nomaʼlum "
            "katetni topish, Pifagor uchliklari va teskari teorema. "
            "20 savol."
        ),
        "questions":   Q_PM64,
        **DEFAULTS,
    },
    {
        "title":       "PM-65 Mashq: Pifagorning qoʻllanishi",
        "tutorial":    "PM-65:",
        "description": (
            "Narvon, tom balandligi, arqon va koordinatadagi qiya masofa — "
            "hayotdagi vaziyatdan toʻgʻri burchakli uchburchakni ajratish. "
            "20 savol."
        ),
        "questions":   Q_PM65,
        **DEFAULTS,
    },
]
