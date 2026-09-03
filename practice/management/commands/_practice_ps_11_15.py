# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-11 … SAT-15 (parallel, perpendikulyar, tengsizliklar).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context & interpretation ·
      15–16 trap-spotting · 17–18 Module 2 level · 19–20 word problems.

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA. Son: 3.5 va 1,200.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_11_15.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Math",
    "description": "SAT Math — Prime SAT darslarining mashqlari",
    "icon":        "bi-calculator",
    "color":       "#4f46e5",
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
# SAT-11 — parallel lines
# =====================================================================

Q_SAT11 = [
    {
        "text": "<p>What is the slope of any line parallel to <i>y</i> = 5<i>x</i> − 2?</p>",
        "choices": ["−5", "−1/5", "1/5", "5"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Parallel chiziqlarning qiyaligi aynan bir "
                       "xil — hisoblash kerak emas, koʻchiriladi.</p>"
                       "<p><strong>−1/5</strong> — bu <b>perpendikulyar</b> chiziqning "
                       "qiyaligi (SAT-12). Ikki mavzu javoblar orasida doim yonma-yon "
                       "turadi.</p>",
    },
    {
        "text": "<p>Which line is parallel to <i>y</i> = 3<i>x</i> + 4?</p>",
        "choices": ["<i>y</i> = −3<i>x</i> + 4", "<i>y</i> = (1/3)<i>x</i> + 4",
                    "<i>y</i> = 3<i>x</i> − 1", "<i>y</i> = 4<i>x</i> + 3"],
        "correct": "<i>y</i> = 3<i>x</i> − 1",
        "explanation": "<p><strong>y = 3x − 1.</strong> Qiyalik 3 bilan bir xil, b esa "
                       "boshqa — ikkala shart ham bajarildi.</p>"
                       "<p><strong>y = 4x + 3</strong> — sonlar oʻrin almashgan javob; "
                       "<strong>y = −3x + 4</strong> bir xil b ga ega, lekin b ning "
                       "tengligi parallellikka aloqasi yoʻq.</p>",
    },
    {
        "text": "<p>Are the lines <i>y</i> = 2<i>x</i> + 5 and <i>y</i> = 2<i>x</i> + 5 "
                "parallel?</p>",
        "choices": ["No — they are the same line.", "No — their slopes are different.",
                    "Yes — their slopes are equal.", "Only where they cross the y-axis."],
        "correct": "No — they are the same line.",
        "explanation": "<p><strong>Yoʻq — bu bitta chiziq.</strong> Parallellik uchun "
                       "qiyaliklar teng, lekin b lar <b>har xil</b> boʻlishi shart.</p>"
                       "<p>Ustma-ust tushgan chiziqlarning cheksiz koʻp umumiy nuqtasi "
                       "bor; parallel chiziqlarniki esa bitta ham yoʻq.</p>",
    },
    {
        "text": "<p>What is the slope of a line parallel to 3<i>x</i> + <i>y</i> = 7?</p>",
        "choices": ["−3", "−1/3", "3", "7"],
        "correct": "−3",
        "explanation": "<p><strong>−3.</strong> Avval y ga yechamiz: y = −3x + 7, demak "
                       "qiyalik −3; parallel chiziqniki ham oʻsha.</p>"
                       "<p><strong>3</strong> — 3x ni oʻtkazganda ishora almashishini "
                       "unutgan javob.</p>",
    },
    {
        "text": "<p>Which equation represents the line parallel to <i>y</i> = "
                "−4<i>x</i> + 1 that passes through (0, 6)?</p>",
        "choices": ["<i>y</i> = −4<i>x</i> + 6", "<i>y</i> = −4<i>x</i> − 6",
                    "<i>y</i> = 4<i>x</i> + 6", "<i>y</i> = 6<i>x</i> − 4"],
        "correct": "<i>y</i> = −4<i>x</i> + 6",
        "explanation": "<p><strong>y = −4x + 6.</strong> Qiyalik koʻchiriladi (−4), va "
                       "nuqtaning x koordinatasi 0 boʻlgani uchun b darhol maʼlum: 6.</p>"
                       "<p><strong>y = 6x − 4</strong> — m va b oʻrin almashgan javob.</p>",
    },
    {
        "text": "<p>A line is parallel to <i>y</i> = (1/2)<i>x</i> − 3 and passes through "
                "(4, 5). What is its <i>y</i>-intercept?</p>",
        "choices": ["−3", "2", "3", "5"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> m = 1/2, keyin 5 = (1/2)(4) + b → "
                       "5 = 2 + b → b = 3.</p>"
                       "<p><strong>−3</strong> — berilgan chiziqning b si: parallel "
                       "chiziqda b <b>albatta boshqa</b> boʻladi.</p>",
    },
    {
        "text": "<p>Which equation represents the line parallel to 2<i>x</i> + "
                "3<i>y</i> = 12 that passes through (3, 1)?</p>",
        "choices": ["2<i>x</i> + 3<i>y</i> = 6", "2<i>x</i> + 3<i>y</i> = 9",
                    "2<i>x</i> + 3<i>y</i> = 12", "3<i>x</i> + 2<i>y</i> = 9"],
        "correct": "2<i>x</i> + 3<i>y</i> = 9",
        "explanation": "<p><strong>2x + 3y = 9.</strong> Standart shaklda parallel "
                       "chiziqning chap tomoni bir xil qoladi; nuqtani qoʻyamiz: "
                       "2(3) + 3(1) = 9.</p>"
                       "<p><strong>2x + 3y = 12</strong> — berilgan chiziqning oʻzi, "
                       "u (3, 1) dan oʻtmaydi (6 + 3 = 9 ≠ 12).</p>",
    },
    {
        "text": "<p>For what value of <i>k</i> are the lines <i>y</i> = <i>kx</i> + 2 and "
                "<i>y</i> = 6<i>x</i> − 1 parallel?</p>",
        "choices": ["−6", "−1/6", "1/6", "6"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Parallellik sharti — qiyaliklar teng, "
                       "demak k = 6. b lar (2 va −1) har xil, shart bajarildi.</p>"
                       "<p><strong>−1/6</strong> — perpendikulyarlik javobi; savolning "
                       "birinchi soʻziga qarang.</p>",
    },
    {
        "text": "<p>Which pair of lines is parallel?</p>",
        "choices": ["<i>y</i> = 2<i>x</i> and <i>y</i> = −2<i>x</i>",
                    "<i>y</i> = 2<i>x</i> + 1 and 2<i>y</i> = 4<i>x</i> + 10",
                    "<i>y</i> = 2<i>x</i> + 1 and <i>y</i> = (1/2)<i>x</i> + 1",
                    "<i>y</i> = 3<i>x</i> and <i>y</i> = 3<i>x</i>"],
        "correct": "<i>y</i> = 2<i>x</i> + 1 and 2<i>y</i> = 4<i>x</i> + 10",
        "explanation": "<p><strong>y = 2x + 1 va 2y = 4x + 10.</strong> Ikkinchisini "
                       "2 ga boʻlsak y = 2x + 5 — qiyaliklar teng (2), b lar har xil "
                       "(1 va 5).</p>"
                       "<p><strong>y = 3x va y = 3x</strong> — bitta chiziq, parallel "
                       "emas.</p>",
    },
    {
        "text": "<p>A system of two linear equations has no solution. Which of the "
                "following must be true?</p>",
        "choices": ["The lines are parallel and distinct.",
                    "The lines are the same line.",
                    "The lines are perpendicular.",
                    "The lines meet at the origin."],
        "correct": "The lines are parallel and distinct.",
        "explanation": "<p><strong>Chiziqlar parallel va har xil.</strong> Umumiy nuqta "
                       "boʻlmasligi — kesishmaslik degani.</p>"
                       "<p><strong>«The same line»</strong> — bu <b>cheksiz koʻp</b> "
                       "yechim beradi, nol emas (SAT-2).</p>",
    },
    {
        "text": "<p>Two straight roads on a plan are <i>y</i> = 0.4<i>x</i> + 1 and "
                "<i>y</i> = 0.4<i>x</i> + 5. Will they ever meet?</p>",
        "choices": ["No — they are parallel.", "Yes — at the origin.",
                    "Yes — where x = 4.", "Only if the plan is extended far enough."],
        "correct": "No — they are parallel.",
        "explanation": "<p><strong>Yoʻq — parallel.</strong> Qiyaliklari teng (0.4), "
                       "b lari har xil (1 va 5).</p>"
                       "<p><strong>«Far enough»</strong> — parallel chiziqlar "
                       "<b>hech qachon</b> uchrashmaydi; ular doim 4 birlik masofada "
                       "qoladi.</p>",
    },
    {
        "text": "<p>Two phone plans cost <i>C</i> = 10<i>g</i> + 30 and <i>C</i> = "
                "10<i>g</i> + 55, where <i>g</i> is gigabytes. Which statement is best "
                "supported by the models?</p>",
        "choices": ["The second plan always costs $25 more.",
                    "The second plan costs more only for large g.",
                    "The plans cost the same at g = 25.",
                    "The second plan charges more for each gigabyte."],
        "correct": "The second plan always costs $25 more.",
        "explanation": "<p><strong>Har doim $25 qimmat.</strong> Qiyaliklar teng, demak "
                       "farq oʻzgarmaydi: 55 − 30 = 25.</p>"
                       "<p><strong>«More for each gigabyte»</strong> notoʻgʻri: har "
                       "gigabayt narxi ikkalasida ham $10.</p>",
    },
    {
        "text": "<p>A canal on a survey map has a slope of 3/8. A service path is drawn "
                "parallel to it. What is the slope of the path?</p>",
        "choices": ["−8/3", "−3/8", "3/8", "8/3"],
        "correct": "3/8",
        "explanation": "<p><strong>3/8.</strong> Parallel — qiyalik oʻzgarmaydi.</p>"
                       "<p><strong>−8/3</strong> — perpendikulyar yoʻlniki boʻlardi. "
                       "«Parallel» va «at a right angle» iboralarini adashtirmang.</p>",
    },
    {
        "text": "<p>Using <i>C</i> = 10<i>g</i> + 30 and <i>C</i> = 10<i>g</i> + 55, how "
                "much more does the second plan cost for 6 gigabytes?</p>",
        "choices": ["$25", "$30", "$85", "$115"],
        "correct": "$25",
        "explanation": "<p><strong>$25.</strong> 115 − 90 = 25 — parallel modellarda "
                       "farq <i>g</i> ga umuman bogʻliq emas.</p>"
                       "<p><strong>$115</strong> — ikkinchi rejaning jami narxi, farqi "
                       "emas: savol «how much more» deb soʻradi.</p>",
    },
    {
        "text": "<p>Which of the following is parallel to <i>y</i> = 2<i>x</i> + 7?</p>",
        "choices": ["<i>y</i> = 2<i>x</i> + 7", "<i>y</i> = 2<i>x</i> − 7",
                    "<i>y</i> = −(1/2)<i>x</i> + 7", "<i>y</i> = 7<i>x</i> + 2"],
        "correct": "<i>y</i> = 2<i>x</i> − 7",
        "explanation": "<p><strong>y = 2x − 7.</strong> Bir xil qiyalik, boshqa b.</p>"
                       "<p><strong>y = 2x + 7</strong> — berilgan chiziqning aynan "
                       "oʻzi. Chiziq oʻz-oʻziga parallel deb hisoblanmaydi, va SAT bu "
                       "variantni ataylab qoʻyadi.</p>",
    },
    {
        "text": "<p>Are the lines <i>y</i> = 4<i>x</i> + 1 and 2<i>y</i> = 8<i>x</i> + 2 "
                "parallel?</p>",
        "choices": ["No — they are the same line.", "No — the slopes differ.",
                    "Yes — the slopes are 4 and 8.", "Yes — the intercepts differ."],
        "correct": "No — they are the same line.",
        "explanation": "<p><strong>Yoʻq — bitta chiziq.</strong> Ikkinchisini 2 ga "
                       "boʻlsak, aynan birinchisi chiqadi.</p>"
                       "<p><strong>«Slopes are 4 and 8»</strong> — 2y = 8x + 2 ni "
                       "yechmasdan oʻqigan javob: qiyalik 8 emas, 4.</p>",
    },
    {
        "text": "<p>For what value of <i>k</i> are the lines 2<i>x</i> + <i>ky</i> = 5 "
                "and <i>y</i> = 4<i>x</i> + 1 parallel?</p>",
        "choices": ["−2", "−1/2", "1/2", "2"],
        "correct": "−1/2",
        "explanation": "<p><strong>−1/2.</strong> Birinchi chiziqning qiyaligi "
                       "−A ÷ B = −2 ÷ k. U 4 ga teng boʻlishi kerak: −2 ÷ k = 4 → "
                       "k = −1/2.</p>"
                       "<p><strong>1/2</strong> — minusni tashlab ketgan javob; "
                       "standart shaklda qiyalik har doim <b>−</b>A ÷ B.</p>",
    },
    {
        "text": "<p>A line is parallel to 5<i>x</i> − 2<i>y</i> = 8 and passes through "
                "(2, −1). Which equation represents it?</p>",
        "choices": ["<i>y</i> = −(5/2)<i>x</i> + 4", "<i>y</i> = (2/5)<i>x</i> − 6",
                    "<i>y</i> = (5/2)<i>x</i> − 6", "<i>y</i> = (5/2)<i>x</i> + 4"],
        "correct": "<i>y</i> = (5/2)<i>x</i> − 6",
        "explanation": "<p><strong>y = (5/2)x − 6.</strong> Qiyalik −5 ÷ (−2) = 5/2; "
                       "keyin −1 = (5/2)(2) + b → −1 = 5 + b → b = −6.</p>"
                       "<p><strong>y = (5/2)x + 4</strong> — b ni topishda ayirish "
                       "oʻrniga qoʻshgan javob.</p>",
    },
    {
        "text": "<p>A roof rises 1 metre for every 12 metres of length. A wheelchair ramp "
                "beside it rises 2 metres for every 24 metres. Are the two surfaces "
                "parallel?</p>",
        "choices": ["Yes — both have a gradient of one in twelve.",
                    "No — the ramp is twice as steep.",
                    "No — the ramp is half as steep.",
                    "It cannot be decided from the numbers given."],
        "correct": "Yes — both have a gradient of one in twelve.",
        "explanation": "<p><strong>Ha.</strong> 2 ÷ 24 = 1 ÷ 12 — nisbat bir xil, demak "
                       "qiyalik ham bir xil.</p>"
                       "<p><strong>«Twice as steep»</strong> — sonlarning kattaligiga "
                       "qarab aytilgan javob, lekin tiklikni <b>nisbat</b> hal qiladi, "
                       "sonlarning oʻzi emas.</p>",
    },
    {
        "text": "<p>Two trains leave the same station on parallel tracks. The first "
                "travels 60 kilometres in the first hour and the second travels "
                "60 kilometres in the first hour, starting 20 kilometres further along "
                "the line. On a distance-time graph, what is true of the two lines?</p>",
        "choices": ["They have equal slopes and different intercepts.",
                    "They have equal slopes and equal intercepts.",
                    "They have different slopes and equal intercepts.",
                    "They meet after one hour."],
        "correct": "They have equal slopes and different intercepts.",
        "explanation": "<p><strong>Teng qiyalik, har xil boshlangʻich.</strong> Tezlik "
                       "bir xil (qiyalik), boshlangʻich masofa esa boshqa (b).</p>"
                       "<p>Shuning uchun grafiklar parallel: poyezdlar orasidagi 20 km "
                       "farq hech qachon oʻzgarmaydi va ular uchrashmaydi.</p>",
    },
]


# =====================================================================
# SAT-12 — perpendicular lines
# =====================================================================

Q_SAT12 = [
    {
        "text": "<p>What is the slope of a line perpendicular to <i>y</i> = 3<i>x</i>?</p>",
        "choices": ["−3", "−1/3", "1/3", "3"],
        "correct": "−1/3",
        "explanation": "<p><strong>−1/3.</strong> 3 ni agʻdaramiz (1/3) va ishorani "
                       "almashtiramiz. Tekshiruv: 3 × (−1/3) = −1 ✓</p>"
                       "<p><strong>−3</strong> — faqat ishora almashtirilgan, kasr "
                       "agʻdarilmagan.</p>",
    },
    {
        "text": "<p>What is the slope of a line perpendicular to <i>y</i> = "
                "−(1/2)<i>x</i> + 4?</p>",
        "choices": ["−2", "−1/2", "1/2", "2"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> −1/2 ni agʻdaramiz (−2/1) va ishorani "
                       "almashtiramiz (2). Tekshiruv: (−1/2) × 2 = −1 ✓</p>"
                       "<p><strong>−2</strong> — faqat agʻdarilgan, ishora "
                       "almashtirilmagan.</p>",
    },
    {
        "text": "<p>If two lines are perpendicular, what is the product of their "
                "slopes?</p>",
        "choices": ["−1", "0", "1", "It is always undefined."],
        "correct": "−1",
        "explanation": "<p><strong>−1.</strong> Bu perpendikulyarlikning taʼrifi.</p>"
                       "<p>Yagona istisno — gorizontal (0) va vertikal (undefined) "
                       "juftligi: ular perpendikulyar, lekin koʻpaytma qoidasi "
                       "ularga qoʻllanmaydi.</p>",
    },
    {
        "text": "<p>What is the slope of a line perpendicular to <i>y</i> = 6?</p>",
        "choices": ["0", "1/6", "6", "Undefined"],
        "correct": "Undefined",
        "explanation": "<p><strong>Undefined.</strong> y = 6 gorizontal chiziq, unga "
                       "perpendikulyari vertikal, vertikal chiziqning qiyaligi esa "
                       "aniqlanmagan.</p>"
                       "<p><strong>0</strong> — berilgan chiziqning oʻz qiyaligi. Bu "
                       "juftlikda formula ishlamaydi, rasm ishlaydi.</p>",
    },
    {
        "text": "<p>What is the slope of a line perpendicular to <i>y</i> = "
                "(2/3)<i>x</i> − 1?</p>",
        "choices": ["−3/2", "−2/3", "2/3", "3/2"],
        "correct": "−3/2",
        "explanation": "<p><strong>−3/2.</strong> Agʻdaramiz (3/2), ishorani "
                       "almashtiramiz. Tekshiruv: (2/3) × (−3/2) = −1 ✓</p>"
                       "<p><strong>3/2</strong> — faqat agʻdarilgan; <strong>−2/3</strong> "
                       "— faqat ishora almashtirilgan. Ikkala amal ham kerak.</p>",
    },
    {
        "text": "<p>Two lines have slopes 4 and −1/4. What is true of the lines?</p>",
        "choices": ["They are perpendicular.", "They are parallel.",
                    "They are the same line.", "They never intersect."],
        "correct": "They are perpendicular.",
        "explanation": "<p><strong>Perpendikulyar.</strong> 4 × (−1/4) = −1.</p>"
                       "<p><strong>«Never intersect»</strong> — bu parallel chiziqlar "
                       "haqida; perpendikulyar chiziqlar esa albatta kesishadi.</p>",
    },
    {
        "text": "<p>What is the slope of a line perpendicular to 3<i>x</i> + "
                "4<i>y</i> = 12?</p>",
        "choices": ["−4/3", "−3/4", "3/4", "4/3"],
        "correct": "4/3",
        "explanation": "<p><strong>4/3.</strong> Berilgan chiziqning qiyaligi "
                       "−A ÷ B = −3/4; uni agʻdarib ishorani almashtirsak 4/3.</p>"
                       "<p><strong>−4/3</strong> — ishorani almashtirishni unutgan "
                       "javob. Tekshiruv: (−3/4) × (4/3) = −1 ✓</p>",
    },
    {
        "text": "<p>A line is perpendicular to <i>y</i> = 2<i>x</i> + 9 and passes "
                "through (4, −1). Which equation represents it?</p>",
        "choices": ["<i>y</i> = −(1/2)<i>x</i> − 3", "<i>y</i> = −(1/2)<i>x</i> + 1",
                    "<i>y</i> = (1/2)<i>x</i> + 1", "<i>y</i> = 2<i>x</i> − 9"],
        "correct": "<i>y</i> = −(1/2)<i>x</i> + 1",
        "explanation": "<p><strong>y = −(1/2)x + 1.</strong> m = −1/2, keyin "
                       "−1 = −(1/2)(4) + b → −1 = −2 + b → b = 1.</p>"
                       "<p><strong>y = −(1/2)x − 3</strong> — b ni topishda ishorada "
                       "adashgan javob. Nuqtani qoʻyib tekshiring.</p>",
    },
    {
        "text": "<p>What is the slope of a line perpendicular to <i>x</i> = −2?</p>",
        "choices": ["−2", "0", "2", "Undefined"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> x = −2 vertikal chiziq; unga "
                       "perpendikulyari gorizontal, gorizontal chiziqning qiyaligi 0.</p>"
                       "<p><strong>Undefined</strong> — berilgan chiziqning oʻziniki. "
                       "Bu savol oldingi juftlikning teskarisi.</p>",
    },
    {
        "text": "<p>Which pair of slopes belongs to perpendicular lines?</p>",
        "choices": ["5 and −5", "5 and 1/5", "5 and −1/5", "5 and 5"],
        "correct": "5 and −1/5",
        "explanation": "<p><strong>5 va −1/5.</strong> Koʻpaytmasi 5 × (−1/5) = −1.</p>"
                       "<p><strong>5 va −5</strong> — koʻpaytmasi −25; "
                       "<strong>5 va 1/5</strong> — koʻpaytmasi 1. Faqat −1 toʻgʻri.</p>",
    },
    {
        "text": "<p>A straight road on a map has a slope of 5/12. A driveway meets it at "
                "a right angle. What is the slope of the driveway?</p>",
        "choices": ["−12/5", "−5/12", "5/12", "12/5"],
        "correct": "−12/5",
        "explanation": "<p><strong>−12/5.</strong> «At a right angle» — perpendikulyar: "
                       "agʻdaramiz (12/5) va ishorani almashtiramiz.</p>"
                       "<p><strong>5/12</strong> — parallel yoʻlniki boʻlardi. Savoldagi "
                       "«right angle» iborasi butun javobni hal qiladi.</p>",
    },
    {
        "text": "<p>Two perpendicular lines are graphed in the <i>xy</i>-plane. How many "
                "points do they have in common?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "Exactly one",
        "explanation": "<p><strong>Roppa-rosa bittasi.</strong> Perpendikulyar chiziqlar "
                       "toʻgʻri burchak ostida <b>kesishadi</b>, demak bitta umumiy "
                       "nuqta bor.</p>"
                       "<p><strong>None</strong> — parallel chiziqlar haqida; "
                       "<strong>infinitely many</strong> — ustma-ust tushgan chiziqlar "
                       "haqida (SAT-11).</p>",
    },
    {
        "text": "<p>A carpenter's shelf is perfectly horizontal. A support is fixed at a "
                "right angle to it. What is the slope of the support?</p>",
        "choices": ["0", "1", "−1", "Undefined"],
        "correct": "Undefined",
        "explanation": "<p><strong>Undefined.</strong> Gorizontalning perpendikulyari "
                       "vertikal — tayanch tik turadi.</p>"
                       "<p><strong>0</strong> — javoning oʻz qiyaligi. Amaliy "
                       "masalalarda ham istisno juftligi oʻsha-oʻsha.</p>",
    },
    {
        "text": "<p>A wall brace runs along a line of slope 3/4. A second brace is fixed "
                "perpendicular to it. What is the slope of the second brace?</p>",
        "choices": ["−4/3", "−3/4", "3/4", "4/3"],
        "correct": "−4/3",
        "explanation": "<p><strong>−4/3.</strong> Agʻdaramiz va ishorani almashtiramiz; "
                       "tekshiruv: (3/4) × (−4/3) = −1 ✓</p>"
                       "<p><strong>4/3</strong> — ishorasi almashtirilmagan javob. "
                       "Perpendikulyar qiyalikning ishorasi <b>har doim</b> "
                       "qarama-qarshi.</p>",
    },
    {
        "text": "<p>What is the slope of a line perpendicular to <i>y</i> = 6<i>x</i> − 5?</p>",
        "choices": ["−6", "−1/6", "1/6", "6"],
        "correct": "−1/6",
        "explanation": "<p><strong>−1/6.</strong> 6 = 6/1, agʻdarilsa 1/6, ishorasi "
                       "almashtirilsa −1/6.</p>"
                       "<p><strong>−6</strong> — butun sonni «agʻdarib boʻlmaydi» deb "
                       "oʻylagan javob. Har qanday butun son ham kasr: 6 = 6/1.</p>",
    },
    {
        "text": "<p>Which statement about the slopes of two perpendicular lines is "
                "true?</p>",
        "choices": ["Their product is −1.", "Their sum is −1.",
                    "They are equal.", "Their difference is 1."],
        "correct": "Their product is −1.",
        "explanation": "<p><strong>Koʻpaytmasi −1.</strong> Masalan 2 va −1/2.</p>"
                       "<p><strong>«Sum is −1»</strong> — 2 + (−1/2) = 1.5, −1 emas. "
                       "Qoida <b>koʻpaytirish</b> haqida; «equal» esa parallel "
                       "chiziqlar haqida.</p>",
    },
    {
        "text": "<p>A line is perpendicular to <i>y</i> = −(3/5)<i>x</i> + 2 and passes "
                "through (3, 4). What is its <i>y</i>-intercept?</p>",
        "choices": ["−1", "1", "4", "9"],
        "correct": "−1",
        "explanation": "<p><strong>−1.</strong> m = 5/3, keyin 4 = (5/3)(3) + b → "
                       "4 = 5 + b → b = −1.</p>"
                       "<p><strong>9</strong> — ayirish oʻrniga qoʻshgan javob; "
                       "<strong>4</strong> — nuqtaning y qiymati.</p>",
    },
    {
        "text": "<p>For what value of <i>k</i> are the lines <i>y</i> = <i>kx</i> + 1 and "
                "<i>y</i> = −(1/4)<i>x</i> perpendicular?</p>",
        "choices": ["−4", "−1/4", "1/4", "4"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Koʻpaytmasi −1 boʻlishi kerak: "
                       "k × (−1/4) = −1 → k = 4.</p>"
                       "<p><strong>−4</strong> — ishorani ikki marta almashtirgan "
                       "javob: (−4) × (−1/4) = +1, bu −1 emas.</p>",
    },
    {
        "text": "<p>A ladder leans against a vertical wall and the ground is horizontal. "
                "What is the slope of the wall?</p>",
        "choices": ["0", "1", "−1", "Undefined"],
        "correct": "Undefined",
        "explanation": "<p><strong>Undefined.</strong> Devor vertikal, demak «run» nolga "
                       "teng va nolga boʻlish aniqlanmagan.</p>"
                       "<p><strong>0</strong> — yerning qiyaligi. Devor va yer "
                       "bir-biriga perpendikulyar, lekin koʻpaytma qoidasi bu juftlikka "
                       "qoʻllanmaydi.</p>",
    },
    {
        "text": "<p>Two streets meet at a right angle. On the town plan, one street lies "
                "along a line of slope 7/2. What is the slope of the other street?</p>",
        "choices": ["−7/2", "−2/7", "2/7", "7/2"],
        "correct": "−2/7",
        "explanation": "<p><strong>−2/7.</strong> Agʻdaramiz (2/7) va ishorani "
                       "almashtiramiz; tekshiruv: (7/2) × (−2/7) = −1 ✓</p>"
                       "<p><strong>−7/2</strong> — faqat ishora almashtirilgan javob; "
                       "u koʻpaytmada −49/4 beradi.</p>",
    },
]


# =====================================================================
# SAT-13 — multi-step linear inequalities
# =====================================================================

Q_SAT13 = [
    {
        "text": "<p>Solve: <i>x</i> + 5 &gt; 12</p>",
        "choices": ["<i>x</i> &lt; 7", "<i>x</i> &gt; 7", "<i>x</i> &lt; 17",
                    "<i>x</i> &gt; 17"],
        "correct": "<i>x</i> &gt; 7",
        "explanation": "<p><strong>x &gt; 7.</strong> Ikkala tomondan 5 ni ayirdik. "
                       "Ayirish belgini <b>hech qachon</b> agʻdarmaydi.</p>"
                       "<p><strong>x &gt; 17</strong> — ayirish oʻrniga qoʻshgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Solve: 3<i>x</i> ≤ 21</p>",
        "choices": ["<i>x</i> ≤ 7", "<i>x</i> ≥ 7", "<i>x</i> ≤ 18", "<i>x</i> ≥ 63"],
        "correct": "<i>x</i> ≤ 7",
        "explanation": "<p><strong>x ≤ 7.</strong> 3 ga boʻldik; 3 musbat, demak belgi "
                       "oʻzgarmaydi.</p>"
                       "<p><strong>x ≤ 18</strong> — boʻlish oʻrniga 3 ni ayirgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Solve: −<i>x</i> &lt; 4</p>",
        "choices": ["<i>x</i> &lt; −4", "<i>x</i> &gt; −4", "<i>x</i> &lt; 4",
                    "<i>x</i> &gt; 4"],
        "correct": "<i>x</i> &gt; −4",
        "explanation": "<p><strong>x &gt; −4.</strong> Ikkala tomonni −1 ga boʻldik — "
                       "manfiy son, demak belgi agʻdarildi.</p>"
                       "<p>Tekshiruv: x = 0 olsak, −0 = 0 &lt; 4 rost, va 0 haqiqatan "
                       "−4 dan katta ✓</p>",
    },
    {
        "text": "<p>Solve: −5<i>x</i> ≥ 20</p>",
        "choices": ["<i>x</i> ≤ −4", "<i>x</i> ≥ −4", "<i>x</i> ≤ 4", "<i>x</i> ≥ 4"],
        "correct": "<i>x</i> ≤ −4",
        "explanation": "<p><strong>x ≤ −4.</strong> −5 ga boʻldik: son −4, belgi esa "
                       "≥ dan ≤ ga agʻdarildi.</p>"
                       "<p><strong>x ≥ −4</strong> — agʻdarish unutilgan. Bitta son "
                       "qoʻyib koʻring: x = 0 da −0 = 0 ≥ 20 yolgʻon, demak 0 "
                       "toʻplamga kirmaydi.</p>",
    },
    {
        "text": "<p>Solve: 2<i>x</i> + 9 &lt; 3</p>",
        "choices": ["<i>x</i> &lt; −3", "<i>x</i> &gt; −3", "<i>x</i> &lt; 3",
                    "<i>x</i> &lt; 6"],
        "correct": "<i>x</i> &lt; −3",
        "explanation": "<p><strong>x &lt; −3.</strong> 2x &lt; −6, keyin 2 ga boʻldik — "
                       "musbat, agʻdarish yoʻq.</p>"
                       "<p><strong>x &gt; −3</strong> — manfiy son koʻrilgani uchun "
                       "agʻdarilgan javob, lekin biz <b>2</b> ga boʻldik, −2 ga emas.</p>",
    },
    {
        "text": "<p>Solve: 7 − 2<i>x</i> ≥ 1</p>",
        "choices": ["<i>x</i> ≤ 3", "<i>x</i> ≥ 3", "<i>x</i> ≤ −3", "<i>x</i> ≥ −3"],
        "correct": "<i>x</i> ≤ 3",
        "explanation": "<p><strong>x ≤ 3.</strong> −2x ≥ −6, keyin −2 ga boʻlamiz va "
                       "belgi agʻdariladi: x ≤ 3.</p>"
                       "<p>Tekshiruv: x = 0 → 7 ≥ 1 rost ✓, x = 5 → −3 ≥ 1 yolgʻon ✓</p>",
    },
    {
        "text": "<p>Solve: 4(<i>x</i> + 1) &gt; 20</p>",
        "choices": ["<i>x</i> &gt; 4", "<i>x</i> &gt; 5", "<i>x</i> &gt; 16",
                    "<i>x</i> &gt; 19"],
        "correct": "<i>x</i> &gt; 4",
        "explanation": "<p><strong>x &gt; 4.</strong> Ikkala tomonni 4 ga boʻlamiz: "
                       "x + 1 &gt; 5, demak x &gt; 4.</p>"
                       "<p><strong>x &gt; 5</strong> — bir qadam yetmay toʻxtagan "
                       "javob (x + 1 &gt; 5 da toʻxtash).</p>",
    },
    {
        "text": "<p>Solve: 5<i>x</i> − 2 ≤ 3<i>x</i> + 8</p>",
        "choices": ["<i>x</i> ≤ 3", "<i>x</i> ≤ 5", "<i>x</i> ≥ 5", "<i>x</i> ≤ 10"],
        "correct": "<i>x</i> ≤ 5",
        "explanation": "<p><strong>x ≤ 5.</strong> 3x ni ayiramiz: 2x − 2 ≤ 8, keyin "
                       "2x ≤ 10 va x ≤ 5.</p>"
                       "<p><strong>x ≤ 10</strong> — oxirgi boʻlish qilinmagan "
                       "javob.</p>",
    },
    {
        "text": "<p>Solve: <i>x</i> ÷ 3 + 4 &gt; 6</p>",
        "choices": ["<i>x</i> &gt; 2/3", "<i>x</i> &gt; 2", "<i>x</i> &gt; 6",
                    "<i>x</i> &gt; 30"],
        "correct": "<i>x</i> &gt; 6",
        "explanation": "<p><strong>x &gt; 6.</strong> 4 ni ayiramiz (x ÷ 3 &gt; 2), "
                       "keyin 3 ga koʻpaytiramiz.</p>"
                       "<p><strong>x &gt; 2</strong> — oxirgi qadam qilinmagan; "
                       "<strong>x &gt; 30</strong> — 4 ni ayirmasdan 6 × 3 + ... "
                       "hisoblagan javob.</p>",
    },
    {
        "text": "<p>Solve: 6 − <i>x</i> &lt; 2<i>x</i> + 15</p>",
        "choices": ["<i>x</i> &lt; −3", "<i>x</i> &gt; −3", "<i>x</i> &lt; 3",
                    "<i>x</i> &gt; 7"],
        "correct": "<i>x</i> &gt; −3",
        "explanation": "<p><strong>x &gt; −3.</strong> x ni oʻngga oʻtkazamiz: "
                       "6 &lt; 3x + 15 → −9 &lt; 3x → −3 &lt; x.</p>"
                       "<p>Harfni <b>kattaroq</b> tomonga yigʻsangiz manfiy koeffitsient "
                       "paydo boʻlmaydi va agʻdarish kerak emas.</p>",
    },
    {
        "text": "<p>Which phrase means the same as «no more than 40»?</p>",
        "choices": ["at most 40", "at least 40", "more than 40", "exactly 40"],
        "correct": "at most 40",
        "explanation": "<p><strong>At most 40</strong> — ikkalasi ham <b>≤ 40</b> "
                       "degani: 40 ning oʻzi ham mumkin.</p>"
                       "<p><strong>At least 40</strong> esa aksincha, ≥ 40 — kamida "
                       "40.</p>",
    },
    {
        "text": "<p>Which phrase means the same as «a minimum of 5»?</p>",
        "choices": ["at least 5", "at most 5", "fewer than 5", "under 5"],
        "correct": "at least 5",
        "explanation": "<p><strong>At least 5</strong> — <b>≥ 5</b>, kamida beshta.</p>"
                       "<p>«Minimum» pastki chegarani belgilaydi, «maximum» esa "
                       "yuqorisini. Bu ikkisini adashtirish matnli masalada "
                       "toʻgʻridan-toʻgʻri notoʻgʻri javobga olib boradi.</p>",
    },
    {
        "text": "<p>A bus can carry at most 45 passengers. Which inequality represents "
                "the number of passengers <i>n</i>?</p>",
        "choices": ["<i>n</i> ≤ 45", "<i>n</i> ≥ 45", "<i>n</i> &lt; 45",
                    "<i>n</i> &gt; 45"],
        "correct": "<i>n</i> ≤ 45",
        "explanation": "<p><strong>n ≤ 45.</strong> «At most» — koʻpi bilan, va 45 ta "
                       "yoʻlovchi ham mumkin.</p>"
                       "<p><strong>n &lt; 45</strong> — 45 ning oʻzini chiqarib "
                       "tashlaydi, lekin toʻla avtobus ham ruxsat etilgan.</p>",
    },
    {
        "text": "<p>A student has 62 points and needs at least 90. Each task is worth "
                "4 points. How many tasks are needed?</p>",
        "choices": ["6", "7", "8", "28"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 62 + 4t ≥ 90 → 4t ≥ 28 → t ≥ 7.</p>"
                       "<p><strong>28</strong> — bir qadam yetmay toʻxtagan javob: "
                       "28 — bu kerakli <b>ochkolar</b>, topshiriqlar soni emas.</p>",
    },
    {
        "text": "<p>What is the greatest integer value of <i>x</i> for which "
                "<i>x</i> &lt; 9?</p>",
        "choices": ["8", "9", "9.5", "10"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Belgi qatʼiy (&lt;), demak 9 ning oʻzi "
                       "toʻplamga kirmaydi.</p>"
                       "<p><strong>9</strong> — chegarani javob deb olgan variant. "
                       "&lt; va ≤ farqi aynan shu yerda ochkoga aylanadi.</p>",
    },
    {
        "text": "<p>What is the least integer value of <i>x</i> for which "
                "<i>x</i> &gt; 4?</p>",
        "choices": ["3", "4", "4.5", "5"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 4 ning oʻzi kirmaydi (qatʼiy &gt;), "
                       "shuning uchun eng kichik butun son 5.</p>"
                       "<p><strong>4</strong> — chegaraning oʻzi. Butun son "
                       "soʻralganda javob har doim chegaradan bir qadam ichkarida.</p>",
    },
    {
        "text": "<p>Solve: −3(<i>x</i> − 2) &gt; 12</p>",
        "choices": ["<i>x</i> &lt; −2", "<i>x</i> &gt; −2", "<i>x</i> &lt; 2",
                    "<i>x</i> &gt; 6"],
        "correct": "<i>x</i> &lt; −2",
        "explanation": "<p><strong>x &lt; −2.</strong> Qavs: −3x + 6 &gt; 12 → "
                       "−3x &gt; 6, keyin −3 ga boʻlamiz va belgi agʻdariladi.</p>"
                       "<p><strong>x &gt; −2</strong> — agʻdarish unutilgan. Tekshiruv: "
                       "x = −3 → −3(−5) = 15 &gt; 12 ✓</p>",
    },
    {
        "text": "<p>What is the greatest integer value of <i>x</i> that satisfies "
                "4<i>x</i> + 5 ≤ 30?</p>",
        "choices": ["6", "6.25", "7", "25"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 4x ≤ 25 → x ≤ 6.25, va eng katta butun "
                       "son 6.</p>"
                       "<p><strong>6.25</strong> — butun son emas; <strong>7</strong> — "
                       "odatdagi yaxlitlash qoidasi bilan olingan javob, lekin 7 "
                       "chegaradan chiqib ketadi (33 &gt; 30).</p>",
    },
    {
        "text": "<p>A taxi charges $5 plus $3 for each kilometre. A passenger has at most "
                "$26 to spend. What is the greatest whole number of kilometres they can "
                "travel?</p>",
        "choices": ["6", "7", "8", "21"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 5 + 3n ≤ 26 → 3n ≤ 21 → n ≤ 7. Bu safar "
                       "chegara aniq chiqdi, demak 7 ning oʻzi mumkin.</p>"
                       "<p><strong>21</strong> — bir qadam yetmay toʻxtagan javob; "
                       "<strong>8</strong> — 8 km $29 turadi, pul yetmaydi.</p>",
    },
    {
        "text": "<p>Notebooks cost $8 each. With $100, what is the greatest number of "
                "notebooks that can be bought?</p>",
        "choices": ["11", "12", "12.5", "13"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 8n ≤ 100 → n ≤ 12.5, va daftar butun "
                       "sonda sotiladi.</p>"
                       "<p><strong>13</strong> — odatdagidek yuqoriga yaxlitlangan "
                       "javob, lekin 13 ta $104 turadi. Byudjet masalasida yaxlitlash "
                       "har doim <b>pastga</b>.</p>",
    },
]


# =====================================================================
# SAT-14 — graphing linear inequalities
# =====================================================================

Q_SAT14 = [
    {
        "text": "<p>Is the boundary line of <i>y</i> ≤ 3<i>x</i> + 2 solid or dashed?</p>",
        "choices": ["Solid", "Dashed", "It depends on the shading",
                    "There is no boundary line"],
        "correct": "Solid",
        "explanation": "<p><strong>Uzluksiz (solid).</strong> ≤ tenglikni ham qamrab "
                       "oladi, demak chiziqning oʻzidagi nuqtalar ham yechim.</p>"
                       "<p>Uzuq chiziq faqat qatʼiy belgilarda (&lt; va &gt;) "
                       "chiziladi.</p>",
    },
    {
        "text": "<p>Is the boundary line of <i>y</i> &gt; <i>x</i> − 1 solid or dashed?</p>",
        "choices": ["Solid", "Dashed", "Solid on one side only",
                    "It cannot be determined"],
        "correct": "Dashed",
        "explanation": "<p><strong>Uzuq (dashed).</strong> &gt; qatʼiy belgi — chegara "
                       "yechimga kirmaydi.</p>"
                       "<p>Qoidani soddalashtiring: belgida <b>tag chizigʻi</b> "
                       "boʻlsa (≤, ≥) chiziq ham uzluksiz.</p>",
    },
    {
        "text": "<p>Is (0, 0) a solution of <i>y</i> &gt; <i>x</i> + 1?</p>",
        "choices": ["Yes", "No", "Only if x is positive", "It is on the boundary"],
        "correct": "No",
        "explanation": "<p><strong>Yoʻq.</strong> 0 &gt; 0 + 1 yaʼni 0 &gt; 1 — "
                       "yolgʻon.</p>"
                       "<p>Demak shtrixlash boshning <b>boshqa</b> tomonida. Sinov "
                       "nuqtasi yolgʻon chiqsa, qarama-qarshi tomon tanlanadi.</p>",
    },
    {
        "text": "<p>Is (5, 2) a solution of 2<i>x</i> + <i>y</i> ≤ 12?</p>",
        "choices": ["Yes — it lies on the boundary line.",
                    "No — it is above the line.",
                    "No — it is outside the shaded region.",
                    "It cannot be checked without a graph."],
        "correct": "Yes — it lies on the boundary line.",
        "explanation": "<p><strong>Ha.</strong> 2(5) + 2 = 12, va 12 ≤ 12 rost.</p>"
                       "<p>Chegaradagi nuqta ham yechim, chunki belgi ≤. Agar &lt; "
                       "boʻlganda, bu nuqta yechim boʻlmasdi.</p>",
    },
    {
        "text": "<p>Which of the following describes the graph of <i>y</i> &lt; "
                "−<i>x</i> + 4?</p>",
        "choices": ["A dashed line with the region above it shaded",
                    "A dashed line with the region below it shaded",
                    "A solid line with the region above it shaded",
                    "A solid line with the region below it shaded"],
        "correct": "A dashed line with the region below it shaded",
        "explanation": "<p><strong>Uzuq chiziq, pastki tomon.</strong> &lt; qatʼiy "
                       "belgi (uzuq), va <i>y</i> yolgʻiz turgan holda «kichik» — "
                       "pastki tomon.</p>"
                       "<p>Tekshiruv: (0, 0) → 0 &lt; 4 rost, va bosh haqiqatan "
                       "chiziqdan pastda.</p>",
    },
    {
        "text": "<p>Which of the following describes the graph of <i>y</i> ≥ "
                "2<i>x</i> − 3?</p>",
        "choices": ["A dashed line with the region above it shaded",
                    "A dashed line with the region below it shaded",
                    "A solid line with the region above it shaded",
                    "A solid line with the region below it shaded"],
        "correct": "A solid line with the region above it shaded",
        "explanation": "<p><strong>Uzluksiz chiziq, ustki tomon.</strong> ≥ tenglikni "
                       "qamrab oladi (uzluksiz), va «katta» — yuqori tomon.</p>"
                       "<p>Tekshiruv: (0, 0) → 0 ≥ −3 rost ✓</p>",
    },
    {
        "text": "<p>Which point is a solution to <i>y</i> ≥ 2<i>x</i> − 6?</p>",
        "choices": ["(0, −7)", "(1, −5)", "(2, −3)", "(3, 1)"],
        "correct": "(3, 1)",
        "explanation": "<p><strong>(3, 1).</strong> 2(3) − 6 = 0, va 1 ≥ 0 rost.</p>"
                       "<p><strong>(2, −3)</strong>: 2(2) − 6 = −2, va −3 ≥ −2 "
                       "<b>yolgʻon</b> — manfiy tomonda −3 −2 dan kichik.</p>",
    },
    {
        "text": "<p>What does the graph of <i>y</i> &lt; 4 look like?</p>",
        "choices": ["A dashed horizontal line with the region below it shaded",
                    "A solid horizontal line with the region below it shaded",
                    "A dashed vertical line with the region left of it shaded",
                    "A solid vertical line with the region below it shaded"],
        "correct": "A dashed horizontal line with the region below it shaded",
        "explanation": "<p><strong>Uzuq gorizontal chiziq, pastki tomon.</strong> "
                       "«y = son» gorizontal chiziq beradi, &lt; esa uzuq va pastki "
                       "tomon.</p>"
                       "<p>Vertikal chiziq «x = son» dan chiqadi — harfga qarang.</p>",
    },
    {
        "text": "<p>What does the graph of <i>x</i> ≥ −2 look like?</p>",
        "choices": ["A solid vertical line with the region to its right shaded",
                    "A solid horizontal line with the region above it shaded",
                    "A dashed vertical line with the region to its right shaded",
                    "A solid vertical line with the region to its left shaded"],
        "correct": "A solid vertical line with the region to its right shaded",
        "explanation": "<p><strong>Uzluksiz vertikal chiziq, oʻng tomon.</strong> "
                       "«x = −2» vertikal chiziq; ≥ uzluksiz qiladi va «kattaroq x» "
                       "oʻng tomonni bildiradi.</p>"
                       "<p>Bu yerda «yuqori/quyi» emas, <b>oʻng/chap</b> ishlatiladi — "
                       "chunki tengsizlik x haqida.</p>",
    },
    {
        "text": "<p>For the inequality 2<i>x</i> + 3<i>y</i> &lt; 12, which region is "
                "shaded?</p>",
        "choices": ["The region containing the origin, with a dashed boundary",
                    "The region containing the origin, with a solid boundary",
                    "The region not containing the origin, with a dashed boundary",
                    "The region not containing the origin, with a solid boundary"],
        "correct": "The region containing the origin, with a dashed boundary",
        "explanation": "<p><strong>Boshni oʻz ichiga olgan tomon, uzuq chegara.</strong> "
                       "(0, 0) ni qoʻyamiz: 0 &lt; 12 rost, demak bosh shtrixlangan "
                       "sohada.</p>"
                       "<p>Belgi qatʼiy (&lt;), shuning uchun chegara uzuq.</p>",
    },
    {
        "text": "<p>A shop's delivery zone is described by <i>y</i> ≤ 8 − <i>x</i>, where "
                "<i>x</i> and <i>y</i> are kilometres east and north of the shop. Is a "
                "house at (3, 6) inside the zone?</p>",
        "choices": ["Yes", "No", "Only if the shop moves", "It is exactly on the edge"],
        "correct": "No",
        "explanation": "<p><strong>Yoʻq.</strong> 8 − 3 = 5, va 6 ≤ 5 yolgʻon.</p>"
                       "<p>Uy chegaradan tashqarida: shimolga bir kilometr ortiqcha "
                       "ketgan.</p>",
    },
    {
        "text": "<p>Using the same zone <i>y</i> ≤ 8 − <i>x</i>, is a house at (2, 5) "
                "inside the zone?</p>",
        "choices": ["Yes", "No", "Only for deliveries before noon",
                    "It is outside by 1 kilometre"],
        "correct": "Yes",
        "explanation": "<p><strong>Ha.</strong> 8 − 2 = 6, va 5 ≤ 6 rost.</p>"
                       "<p>Uy chegaradan bir kilometr ichkarida. Shtrixlangan sohaning "
                       "har bir nuqtasi — yetkazib beriladigan manzil.</p>",
    },
    {
        "text": "<p>In the graph of a linear inequality, what does the shaded region "
                "represent?</p>",
        "choices": ["All the points that make the inequality true",
                    "Only the points on the boundary line",
                    "The points where x and y are both positive",
                    "The single solution of the inequality"],
        "correct": "All the points that make the inequality true",
        "explanation": "<p><strong>Tengsizlikni rost qiladigan barcha nuqtalar.</strong> "
                       "Ular cheksiz koʻp — shuning uchun javob soha, chiziq emas.</p>"
                       "<p><strong>«The single solution»</strong> — tenglama haqida; "
                       "tengsizlikning yechimi bitta son emas, toʻplam.</p>",
    },
    {
        "text": "<p>Why is a boundary line sometimes drawn dashed?</p>",
        "choices": ["Because the points on it are not part of the solution",
                    "Because the line has a negative slope",
                    "Because the shading is below the line",
                    "Because the inequality has no solution"],
        "correct": "Because the points on it are not part of the solution",
        "explanation": "<p><strong>Chunki chiziqdagi nuqtalar yechim emas.</strong> "
                       "Bu qatʼiy belgilarda (&lt;, &gt;) boʻladi.</p>"
                       "<p>Uzuq chiziq «bu yergacha, lekin bu chiziqning oʻzi emas» "
                       "degan rasm.</p>",
    },
    {
        "text": "<p>What kind of boundary line does <i>y</i> &gt; 2<i>x</i> + 1 have?</p>",
        "choices": ["Dashed", "Solid", "Solid, because the slope is positive",
                    "Dashed, because the intercept is positive"],
        "correct": "Dashed",
        "explanation": "<p><strong>Uzuq.</strong> Belgi &gt; — qatʼiy.</p>"
                       "<p>Qiyalik va b chiziqning <b>turiga</b> umuman taʼsir "
                       "qilmaydi — faqat tengsizlik belgisi hal qiladi.</p>",
    },
    {
        "text": "<p>Which region is shaded for the inequality −2<i>y</i> &gt; 4?</p>",
        "choices": ["Below the line <i>y</i> = −2", "Above the line <i>y</i> = −2",
                    "Below the line <i>y</i> = 2", "Above the line <i>y</i> = 2"],
        "correct": "Below the line <i>y</i> = −2",
        "explanation": "<p><strong>y = −2 chizigʻining pastki tomoni.</strong> Avval "
                       "yechamiz: −2y &gt; 4 → y &lt; −2 (manfiy songa boʻldik, belgi "
                       "agʻdarildi).</p>"
                       "<p><strong>«Above y = −2»</strong> — agʻdarishni unutgan javob. "
                       "«Yuqori/quyi» qoidasi faqat y yolgʻiz qolgandan <b>keyin</b> "
                       "ishlaydi.</p>",
    },
    {
        "text": "<p>Which inequality is graphed with a solid line and the region below it "
                "shaded?</p>",
        "choices": ["<i>y</i> ≤ 3<i>x</i> + 1", "<i>y</i> &lt; 3<i>x</i> + 1",
                    "<i>y</i> ≥ 3<i>x</i> + 1", "<i>y</i> &gt; 3<i>x</i> + 1"],
        "correct": "<i>y</i> ≤ 3<i>x</i> + 1",
        "explanation": "<p><strong>y ≤ 3x + 1.</strong> Tag chizigʻi bor — uzluksiz "
                       "chiziq; «kichik yoki teng» — pastki tomon.</p>"
                       "<p><strong>y &lt; 3x + 1</strong> ham pastki tomon, lekin "
                       "chizigʻi <b>uzuq</b> boʻlardi.</p>",
    },
    {
        "text": "<p>Is the point (−1, 3) a solution of <i>y</i> &gt; −2<i>x</i> + 1?</p>",
        "choices": ["No — the point lies exactly on the boundary line.",
                    "Yes — the point lies above the line.",
                    "No — the point lies below the line.",
                    "Yes — the point lies on the boundary line."],
        "correct": "No — the point lies exactly on the boundary line.",
        "explanation": "<p><strong>Yoʻq — nuqta aynan chegarada.</strong> "
                       "−2(−1) + 1 = 3, va 3 &gt; 3 yolgʻon.</p>"
                       "<p>Belgi qatʼiy boʻlgani uchun chegaradagi nuqta yechim emas. "
                       "Agar ≥ boʻlganda, javob «ha» boʻlardi.</p>",
    },
    {
        "text": "<p>A farmer fences a field so that the usable area satisfies "
                "<i>y</i> ≤ 10 − 2<i>x</i>, where <i>x</i> and <i>y</i> are hundreds of "
                "metres. Is the point (2, 5) inside the usable area?</p>",
        "choices": ["Yes", "No", "Only if the fence is moved", "Exactly on the fence"],
        "correct": "Yes",
        "explanation": "<p><strong>Ha.</strong> 10 − 2(2) = 6, va 5 ≤ 6 rost — demak "
                       "nuqta shtrixlangan sohada, yaʼni foydalaniladigan yer "
                       "ichida.</p>"
                       "<p><strong>«Exactly on the fence»</strong> boʻlishi uchun "
                       "5 = 6 boʻlishi kerak edi. Har doim ikkala tomonni alohida "
                       "hisoblang, keyin belgini solishtiring.</p>",
    },
    {
        "text": "<p>A club's budget region is <i>y</i> ≤ 200 − 12<i>x</i>, where <i>x</i> "
                "is the number of shirts and <i>y</i> is dollars kept in reserve. If the "
                "club buys 10 shirts, what is the greatest reserve it can keep?</p>",
        "choices": ["$68", "$80", "$120", "$188"],
        "correct": "$80",
        "explanation": "<p><strong>$80.</strong> 200 − 12(10) = 200 − 120 = 80, va "
                       "belgi ≤ — demak eng koʻpi 80.</p>"
                       "<p><strong>$120</strong> — futbolkalarga ketgan pul, "
                       "qoldiq emas.</p>",
    },
]


# =====================================================================
# SAT-15 — modelling with inequalities
# =====================================================================

Q_SAT15 = [
    {
        "text": "<p>A lift holds no more than 40 people. Which inequality represents the "
                "number of people <i>n</i>?</p>",
        "choices": ["<i>n</i> ≤ 40", "<i>n</i> ≥ 40", "<i>n</i> &lt; 40",
                    "<i>n</i> &gt; 40"],
        "correct": "<i>n</i> ≤ 40",
        "explanation": "<p><strong>n ≤ 40.</strong> «No more than» — koʻpi bilan, va "
                       "40 kishi ham mumkin.</p>"
                       "<p><strong>n &lt; 40</strong> — 40 ning oʻzini chiqarib "
                       "tashlaydi, lekin toʻla lift ham ruxsat etilgan.</p>",
    },
    {
        "text": "<p>A team needs a minimum of 5 more points. Which inequality represents "
                "the points <i>p</i> they still need?</p>",
        "choices": ["<i>p</i> ≥ 5", "<i>p</i> ≤ 5", "<i>p</i> &gt; 5", "<i>p</i> &lt; 5"],
        "correct": "<i>p</i> ≥ 5",
        "explanation": "<p><strong>p ≥ 5.</strong> «A minimum of» — kamida, pastki "
                       "chegara.</p>"
                       "<p><strong>p &gt; 5</strong> — roppa-rosa 5 ochkoni chiqarib "
                       "tashlaydi, lekin 5 ta ham yetarli.</p>",
    },
    {
        "text": "<p>Pens cost $8 each. With $100, what is the greatest number of pens "
                "that can be bought?</p>",
        "choices": ["11", "12", "12.5", "13"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 8n ≤ 100 → n ≤ 12.5, va ruchka butun "
                       "sonda sotiladi.</p>"
                       "<p><strong>13</strong> — odatdagi yaxlitlash bilan olingan "
                       "javob, lekin 13 ta $104 turadi.</p>",
    },
    {
        "text": "<p>A worker earns $15 for showing up plus $6 per hour. How many hours "
                "must they work to earn at least $51?</p>",
        "choices": ["5", "6", "7", "36"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 15 + 6h ≥ 51 → 6h ≥ 36 → h ≥ 6. Aniq "
                       "chiqdi, yaxlitlash kerak emas.</p>"
                       "<p><strong>36</strong> — bir qadam yetmay toʻxtagan javob: "
                       "36 — bu <b>dollar</b>, soat emas.</p>",
    },
    {
        "text": "<p>A club has $200 for shirts. Each shirt costs $12 and the printer "
                "charges a one-time $25 setup fee. What is the greatest number of shirts "
                "the club can buy?</p>",
        "choices": ["14", "15", "16", "18"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> 12n + 25 ≤ 200 → 12n ≤ 175 → "
                       "n ≤ 14.58…, va byudjet masalasi <b>pastga</b> "
                       "yaxlitlanadi.</p>"
                       "<p><strong>15</strong> — 0.58 ni yuqoriga yaxlitlagan javob, "
                       "lekin 15 ta $205 turadi; <strong>16</strong> — $25 ni "
                       "ayirmagan javob.</p>",
    },
    {
        "text": "<p>A van can carry a load of at most 850 kilograms. The driver weighs "
                "80 kilograms and each box weighs 23 kilograms. What is the greatest "
                "number of boxes?</p>",
        "choices": ["33", "34", "36", "37"],
        "correct": "33",
        "explanation": "<p><strong>33.</strong> 80 + 23b ≤ 850 → 23b ≤ 770 → "
                       "b ≤ 33.47…</p>"
                       "<p>Tekshiruv: 33 ta → 759 + 80 = 839 ✓; 34 ta → 782 + 80 = 862 "
                       "✗. <strong>36</strong> — haydovchini hisobga olmagan javob.</p>",
    },
    {
        "text": "<p>A player has 18 points and needs at least 100. Each game is worth "
                "7 points. What is the least number of games needed?</p>",
        "choices": ["11", "11.7", "12", "15"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 18 + 7g ≥ 100 → 7g ≥ 82 → "
                       "g ≥ 11.71…</p>"
                       "<p>«Kamida» talabida <b>yuqoriga</b> yaxlitlanadi: 11 ta oʻyin "
                       "faqat 95 ochko beradi, 12 tasi esa 102.</p>",
    },
    {
        "text": "<p>A garage charges $4 to enter plus $2.50 per hour. With $20, what is "
                "the greatest whole number of hours a driver can park?</p>",
        "choices": ["5", "6", "6.4", "8"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 4 + 2.50h ≤ 20 → 2.50h ≤ 16 → "
                       "h ≤ 6.4, pastga yaxlitlanadi.</p>"
                       "<p>Tekshiruv: 6 soat $19 ✓, 7 soat $21.50 ✗. "
                       "<strong>8</strong> — kirish haqini hisobga olmagan javob.</p>",
    },
    {
        "text": "<p>Tickets cost $9 each and there is a one-time booking fee of $12. "
                "A buyer has $150. Which inequality represents the number of tickets "
                "<i>t</i>?</p>",
        "choices": ["9<i>t</i> + 12 ≤ 150", "9<i>t</i> + 12 ≥ 150",
                    "9<i>t</i> − 12 ≤ 150", "12<i>t</i> + 9 ≤ 150"],
        "correct": "9<i>t</i> + 12 ≤ 150",
        "explanation": "<p><strong>9t + 12 ≤ 150.</strong> Har bir chipta $9 — chiptalar "
                       "soniga koʻpayadi; $12 bir marta qoʻshiladi; pul yetishi kerak, "
                       "demak ≤.</p>"
                       "<p><strong>12t + 9 ≤ 150</strong> — ikki son oʻrin almashgan "
                       "javob.</p>",
    },
    {
        "text": "<p>Using 9<i>t</i> + 12 ≤ 150, what is the greatest number of tickets "
                "the buyer can afford?</p>",
        "choices": ["14", "15", "16", "18"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> 9t ≤ 138 → t ≤ 15.33…, pastga "
                       "yaxlitlaymiz.</p>"
                       "<p>Tekshiruv: 15 ta → 135 + 12 = 147 ✓; 16 ta → 144 + 12 = 156 "
                       "✗. <strong>16</strong> — $12 ni ayirmagan javob "
                       "(150 ÷ 9 = 16.67).</p>",
    },
    {
        "text": "<p>In a budget problem the answer comes out as <i>n</i> ≤ 14.58. How "
                "should it be rounded?</p>",
        "choices": ["Down to 14, because 15 exceeds the budget",
                    "Up to 15, because 0.58 is more than a half",
                    "To 14.6, because money uses one decimal place",
                    "It cannot be rounded"],
        "correct": "Down to 14, because 15 exceeds the budget",
        "explanation": "<p><strong>Pastga, 14 ga.</strong> Chegara masalasida yaxlitlash "
                       "matematik emas, <b>mantiqiy</b>: 15 ta olishga pul yetmaydi.</p>"
                       "<p>Odatdagi «0.5 dan katta boʻlsa yuqoriga» qoidasi bu yerda "
                       "ishlamaydi.</p>",
    },
    {
        "text": "<p>In a «minimum requirement» problem the answer comes out as "
                "<i>g</i> ≥ 11.7. How should it be rounded?</p>",
        "choices": ["Up to 12, because 11 is not enough",
                    "Down to 11, because you cannot have part of a game",
                    "To 11.7, because that is the exact answer",
                    "Down to 11, because 0.7 is small"],
        "correct": "Up to 12, because 11 is not enough",
        "explanation": "<p><strong>Yuqoriga, 12 ga.</strong> «Kamida» talabida 11 ta "
                       "talabni bajarmaydi.</p>"
                       "<p>Qoida: ≤ da pastga, ≥ da yuqoriga — kasrning kattaligiga "
                       "qaramasdan.</p>",
    },
    {
        "text": "<p>In the model 12<i>n</i> + 25 ≤ 200, which of the following is the "
                "best interpretation of 25?</p>",
        "choices": ["A one-time setup fee of $25",
                    "The cost of each shirt is $25",
                    "At most 25 shirts can be bought",
                    "The club has $25 left over"],
        "correct": "A one-time setup fee of $25",
        "explanation": "<p><strong>Bir martalik $25.</strong> 25 harfsiz turibdi — "
                       "demak nechta futbolka olinishidan qatʼi nazar bir marta "
                       "toʻlanadi.</p>"
                       "<p>Harf bilan turgan 12 esa «har bir futbolka uchun» degan "
                       "son (SAT-10).</p>",
    },
    {
        "text": "<p>Why must the answer to «what is the greatest number of shirts» be a "
                "whole number?</p>",
        "choices": ["Because shirts cannot be bought in parts",
                    "Because the inequality uses ≤ rather than &lt;",
                    "Because money is always a whole number",
                    "Because the setup fee is a whole number"],
        "correct": "Because shirts cannot be bought in parts",
        "explanation": "<p><strong>Chunki futbolka boʻlaklab sotilmaydi.</strong> "
                       "Yaxlitlash talabi <b>vaziyatdan</b> kelib chiqadi, "
                       "tengsizlikning oʻzidan emas.</p>"
                       "<p>Agar savol pul yoki vaqt soʻraganda, kasrli javob "
                       "mutlaqo normal boʻlardi.</p>",
    },
    {
        "text": "<p>A budget gives <i>n</i> ≤ 14.58. A student answers 15. What mistake "
                "has been made?</p>",
        "choices": ["The ordinary rounding rule was used instead of the budget limit",
                    "The inequality sign was flipped",
                    "The setup fee was subtracted twice",
                    "The division was done incorrectly"],
        "correct": "The ordinary rounding rule was used instead of the budget limit",
        "explanation": "<p><strong>Odatdagi yaxlitlash qoidasi qoʻllangan.</strong> "
                       "0.58 «yarimdan koʻp» boʻlgani uchun yuqoriga koʻtarilgan.</p>"
                       "<p>Lekin 15 ta chegaradan chiqib ketadi — byudjet masalasida "
                       "javob har doim pastga yaxlitlanadi.</p>",
    },
    {
        "text": "<p>A minimum requirement gives <i>g</i> ≥ 11.7. A student answers 11. "
                "What mistake has been made?</p>",
        "choices": ["The answer was rounded down when the requirement needs rounding up",
                    "The inequality sign was flipped",
                    "The starting points were not subtracted",
                    "The answer should have been left as a decimal"],
        "correct": "The answer was rounded down when the requirement needs rounding up",
        "explanation": "<p><strong>Pastga yaxlitlangan.</strong> 11 ta talabni "
                       "bajarmaydi, chunki 11 &lt; 11.7.</p>"
                       "<p>≥ bilan chiqqan javob har doim <b>yuqoriga</b> "
                       "yaxlitlanadi.</p>",
    },
    {
        "text": "<p>A phone plan costs $5 per month plus $1.75 per gigabyte. A customer "
                "wants the monthly bill to be at most $40. What is the greatest whole "
                "number of gigabytes?</p>",
        "choices": ["20", "22", "23", "35"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> 5 + 1.75g ≤ 40 → 1.75g ≤ 35 → g ≤ 20 "
                       "roppa-rosa.</p>"
                       "<p><strong>22</strong> — oylik $5 ni ayirmagan javob "
                       "(40 ÷ 1.75 = 22.85 → 22). <strong>35</strong> — bir qadam "
                       "yetmay toʻxtagan javob.</p>",
    },
    {
        "text": "<p>A student has 45 points and needs at least 150. Each project is worth "
                "8 points. What is the least number of projects needed?</p>",
        "choices": ["13", "13.125", "14", "19"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> 45 + 8w ≥ 150 → 8w ≥ 105 → "
                       "w ≥ 13.125, yuqoriga yaxlitlanadi.</p>"
                       "<p>Tekshiruv: 13 ta → 45 + 104 = 149, yetmaydi; 14 ta → "
                       "45 + 112 = 157 ✓. <strong>19</strong> — 45 ni ayirmagan "
                       "javob.</p>",
    },
    {
        "text": "<p>A coach's luggage hold takes at most 900 kilograms. Forty-eight "
                "pupils each bring 15 kilograms. Equipment boxes weigh 20 kilograms each. "
                "What is the greatest number of boxes that can also be carried?</p>",
        "choices": ["9", "12", "36", "45"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> Oʻquvchilar: 48 × 15 = 720 kg. Qolgan "
                       "joy: 900 − 720 = 180 kg. Qutilar: 180 ÷ 20 = 9.</p>"
                       "<p><strong>45</strong> — oʻquvchilarning yukini hisobga olmagan "
                       "javob (900 ÷ 20); <strong>36</strong> — 720 ni 20 ga boʻlgan "
                       "javob.</p>",
    },
    {
        "text": "<p>A print shop charges a $60 setup fee plus $1.20 for each copy. "
                "A school has a budget of $300. What is the greatest number of copies it "
                "can order?</p>",
        "choices": ["180", "200", "240", "250"],
        "correct": "200",
        "explanation": "<p><strong>200.</strong> 60 + 1.20c ≤ 300 → 1.20c ≤ 240 → "
                       "c ≤ 200 roppa-rosa.</p>"
                       "<p><strong>250</strong> — bir martalik $60 ni ayirmagan javob "
                       "(300 ÷ 1.20); <strong>240</strong> — bir qadam yetmay toʻxtagan "
                       "javob ($240 — bu pul, nusxa emas).</p>",
    },
]


PRACTICES = [
    {
        "title":       "SAT-11 Practice: Parallel Lines and Equal Slopes",
        "description": "20 ta SAT uslubidagi savol — teng qiyaliklar, «bitta chiziq» "
                       "tuzogʻi, standart shaklda parallellik va nomaʼlum k.",
        "tutorial":    "SAT-11:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT11,
    },
    {
        "title":       "SAT-12 Practice: Perpendicular Lines and Negative Reciprocal Slopes",
        "description": "20 ta SAT uslubidagi savol — agʻdar va ishorani almashtir, "
                       "koʻpaytmasi −1, gorizontal/vertikal istisnosi.",
        "tutorial":    "SAT-12:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT12,
    },
    {
        "title":       "SAT-13 Practice: Solving Multi-Step Linear Inequalities",
        "description": "20 ta SAT uslubidagi savol — belgini agʻdarish qoidasi, "
                       "koʻp qadamli yechim va «eng katta butun son» savoli.",
        "tutorial":    "SAT-13:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT13,
    },
    {
        "title":       "SAT-14 Practice: Graphing Linear Inequalities on the Coordinate Plane",
        "description": "20 ta SAT uslubidagi savol — uzuq/uzluksiz chegara, sinov "
                       "nuqtasi, shtrixlangan soha va nuqtani tekshirish.",
        "tutorial":    "SAT-14:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT14,
    },
    {
        "title":       "SAT-15 Practice: Modeling Real-World Scenarios with Inequalities",
        "description": "20 ta SAT uslubidagi savol — at least/at most, byudjet modeli "
                       "va yaxlitlash tomonini toʻgʻri tanlash.",
        "tutorial":    "SAT-15:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT15,
    },
]
