# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-6 … SAT-10 (chiziqning hamma koʻrinishi).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context & interpretation ·
      15–16 trap-spotting · 17–18 Module 2 level · 19–20 word problems (har doim ikkita).

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA. Son: 3.5 va 1,200.
⚠️ Subject `Math` — Telegram uni "Matematika (SAT)" deb koʻrsatadi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_06_10.py --master=prime \\
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
# SAT-6 — slope from two points
# =====================================================================

Q_SAT6 = [
    {
        "text": "<p>What is the slope of the line that passes through (0, 0) and (2, 8)?</p>",
        "choices": ["1/4", "4", "8", "16"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> rise = 8 − 0 = 8, run = 2 − 0 = 2, "
                       "m = 8 ÷ 2 = 4.</p>"
                       "<p><strong>8</strong> — faqat rise, run ga boʻlinmagan; "
                       "<strong>1/4</strong> — nisbat teskari olingan.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (1, 2) and (4, 11)?</p>",
        "choices": ["1/3", "3", "9", "13"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> rise = 11 − 2 = 9, run = 4 − 1 = 3, "
                       "m = 9 ÷ 3 = 3.</p>"
                       "<p><strong>9</strong> — koʻtarilishning oʻzi; "
                       "<strong>13</strong> — ikki y ni qoʻshib yuborgan javob "
                       "(11 + 2). Formulada <b>ayirma</b> turadi.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (2, 7) and (5, 7)?</p>",
        "choices": ["0", "3", "7", "Undefined"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Ikkala y bir xil: rise = 7 − 7 = 0, "
                       "va 0 ÷ 3 = 0. Chiziq gorizontal.</p>"
                       "<p><strong>Undefined</strong> — bu vertikal chiziqniki. Nol "
                       "<b>ustida</b> boʻlsa javob 0; pastida boʻlsa aniqlanmagan.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (3, 1) and (3, 6)?</p>",
        "choices": ["0", "1", "5", "Undefined"],
        "correct": "Undefined",
        "explanation": "<p><strong>Undefined.</strong> run = 3 − 3 = 0, nolga boʻlish "
                       "aniqlanmagan. Chiziq vertikal.</p>"
                       "<p><strong>5</strong> — rise (6 − 1), lekin uni 0 ga boʻlib "
                       "boʻlmaydi. Oldingi savol bilan solishtiring: u yerda y lar, "
                       "bu yerda x lar bir xil edi.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (−2, 3) and (4, 15)?</p>",
        "choices": ["1/2", "2", "6", "12"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> rise = 15 − 3 = 12, "
                       "run = 4 − (−2) = 6, m = 12 ÷ 6 = 2.</p>"
                       "<p><strong>6</strong> — run ni javob deb olgan; "
                       "<strong>12</strong> — rise. Manfiy sondan ayirganda "
                       "qoʻshiladi: 4 − (−2) = 6, 2 emas.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (5, −2) and (9, −10)?</p>",
        "choices": ["−2", "−1/2", "1/2", "2"],
        "correct": "−2",
        "explanation": "<p><strong>−2.</strong> rise = −10 − (−2) = −8, run = 9 − 5 = 4, "
                       "m = −8 ÷ 4 = −2.</p>"
                       "<p><strong>2</strong> — ishora yoʻqolgan. y qiymati −2 dan −10 "
                       "ga <b>tushdi</b>, demak javob manfiy boʻlishi kerak edi.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (−4, −1) and (0, 7)?</p>",
        "choices": ["1/2", "2", "4", "8"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> rise = 7 − (−1) = 8, run = 0 − (−4) = 4, "
                       "m = 8 ÷ 4 = 2.</p>"
                       "<p><strong>8</strong> — faqat rise. Ikkala ayirmada ham manfiy "
                       "sondan ayirdik, shuning uchun ikkalasi ham qoʻshildi.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (6, 3) and (2, 11)?</p>",
        "choices": ["−2", "−1/2", "1/2", "2"],
        "correct": "−2",
        "explanation": "<p><strong>−2.</strong> rise = 11 − 3 = 8, run = 2 − 6 = −4, "
                       "m = 8 ÷ (−4) = −2.</p>"
                       "<p><strong>2</strong> — pastdagi ayirmaning ishorasi tashlab "
                       "ketilgan. Ikkala ayirma ham <b>bir xil nuqtadan</b> boshlanishi "
                       "shart.</p>",
    },
    {
        "text": "<p>A linear relationship is shown in a table: when <i>x</i> is 1, 3 and 5, "
                "<i>y</i> is 4, 10 and 16. What is the slope?</p>",
        "choices": ["2", "3", "6", "12"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> x har safar 2 ga ortganda y 6 ga ortadi: "
                       "6 ÷ 2 = 3.</p>"
                       "<p><strong>6</strong> — y ning oʻzgarishi, uni x ning "
                       "oʻzgarishiga boʻlish kerak; <strong>12</strong> — chekka "
                       "qiymatlar ayirmasi (16 − 4), lekin unda run 4 boʻladi.</p>",
    },
    {
        "text": "<p>The line through which pair of points has a slope of 5?</p>",
        "choices": ["(0, 0) and (5, 1)", "(1, 2) and (2, 7)",
                    "(1, 5) and (2, 5)", "(2, 10) and (3, 14)"],
        "correct": "(1, 2) and (2, 7)",
        "explanation": "<p><strong>(1, 2) va (2, 7).</strong> rise = 5, run = 1, "
                       "m = 5.</p>"
                       "<p><strong>(0, 0) va (5, 1)</strong> — qiyaligi 1/5, teskari "
                       "olingan javob; <strong>(1, 5) va (2, 5)</strong> — qiyaligi 0, "
                       "chunki y oʻzgarmagan.</p>",
    },
    {
        "text": "<p>A line passes through (0, 12) and (4, 0). What is its slope?</p>",
        "choices": ["−3", "−1/3", "1/3", "3"],
        "correct": "−3",
        "explanation": "<p><strong>−3.</strong> rise = 0 − 12 = −12, run = 4 − 0 = 4, "
                       "m = −12 ÷ 4 = −3.</p>"
                       "<p><strong>3</strong> — ishorasiz javob. Chiziq y oʻqidagi 12 "
                       "dan x oʻqidagi 4 ga <b>tushmoqda</b>.</p>",
    },
    {
        "text": "<p>A plant's height is recorded twice: 14 centimetres in week 2 and "
                "30 centimetres in week 6. If the growth is at a constant rate, how many "
                "centimetres does the plant grow each week?</p>",
        "choices": ["2", "4", "8", "16"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> (30 − 14) ÷ (6 − 2) = 16 ÷ 4 = 4 sm "
                       "har haftada.</p>"
                       "<p><strong>16</strong> — toʻrt haftadagi butun oʻsish, bir "
                       "haftaniki emas. «Each week» soʻzi boʻlishni buyuradi.</p>",
    },
    {
        "text": "<p>A taxi fare is $9 for a 3-mile ride and $19 for an 8-mile ride. "
                "The fare changes at a constant rate. How much does each additional mile "
                "cost?</p>",
        "choices": ["$2", "$3", "$10", "$28"],
        "correct": "$2",
        "explanation": "<p><strong>$2.</strong> (19 − 9) ÷ (8 − 3) = 10 ÷ 5 = 2 dollar "
                       "har bir mil uchun.</p>"
                       "<p><strong>$3</strong> — 9 ÷ 3, yaʼni butun narxni masofaga "
                       "boʻlgan javob; lekin narx ichida boshlangʻich toʻlov ham bor, "
                       "shuning uchun <b>ikki nuqtaning ayirmasi</b> olinadi.</p>",
    },
    {
        "text": "<p>A company's yearly revenue, in thousands of dollars, was 40 in 2016 "
                "and 72 in 2020. What was the average increase per year?</p>",
        "choices": ["$8,000", "$16,000", "$32,000", "$72,000"],
        "correct": "$8,000",
        "explanation": "<p><strong>$8,000.</strong> (72 − 40) ÷ (2020 − 2016) = 32 ÷ 4 = 8 "
                       "ming dollar har yili.</p>"
                       "<p><strong>$32,000</strong> — toʻrt yildagi butun oʻsish. "
                       "«Per year» — yillar soniga boʻlish degani.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (−1, 5) and (3, −3)?</p>",
        "choices": ["−2", "−1/2", "1/2", "2"],
        "correct": "−2",
        "explanation": "<p><strong>−2.</strong> rise = −3 − 5 = −8, run = 3 − (−1) = 4, "
                       "m = −8 ÷ 4 = −2.</p>"
                       "<p><strong>−1/2</strong> — nisbat teskari (4 ÷ −8); "
                       "<strong>2</strong> — ishora yoʻqolgan. Bu ikkitasi shu mavzudagi "
                       "doimiy tuzoq juftligi.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (4, 9) and (4, 1)?</p>",
        "choices": ["−2", "0", "2", "Undefined"],
        "correct": "Undefined",
        "explanation": "<p><strong>Undefined.</strong> Ikkala nuqtaning x koordinatasi "
                       "bir xil, demak run = 0 va chiziq vertikal.</p>"
                       "<p><strong>0</strong> — gorizontal chiziqning qiyaligi. "
                       "Qaysi koordinata takrorlanayotganiga qarang: x lar bir xil → "
                       "vertikal.</p>",
    },
    {
        "text": "<p>A line passes through (2, 5) and (<i>k</i>, 17), and its slope is 4. "
                "What is the value of <i>k</i>?</p>",
        "choices": ["3", "5", "14", "50"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> rise = 17 − 5 = 12. Qiyalik 4 boʻlsa, "
                       "run = 12 ÷ 4 = 3, demak k = 2 + 3 = 5.</p>"
                       "<p><strong>3</strong> — run ning oʻzi, boshlangʻich 2 ga "
                       "qoʻshilmagan; <strong>50</strong> — formula teskari qoʻllangan "
                       "(k − 2 = 4 × 12).</p>",
    },
    {
        "text": "<p>A line passes through (−3, 7) and (5, <i>k</i>), and its slope is "
                "−1/2. What is the value of <i>k</i>?</p>",
        "choices": ["−4", "3", "11", "15"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> run = 5 − (−3) = 8, rise = −1/2 × 8 = −4, "
                       "demak k = 7 + (−4) = 3.</p>"
                       "<p><strong>−4</strong> — koʻtarilishning oʻzi, boshlangʻich 7 ga "
                       "qoʻshilmagan; <strong>11</strong> — manfiy qiyalikni musbat deb "
                       "olgan javob (7 + 4).</p>",
    },
    {
        "text": "<p>A hiking trail rises from 320 metres above sea level at the 2-kilometre "
                "mark to 470 metres at the 8-kilometre mark. What is the average rise, in "
                "metres, per kilometre of trail?</p>",
        "choices": ["25", "75", "150", "235"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> (470 − 320) ÷ (8 − 2) = 150 ÷ 6 = 25 metr "
                       "har bir kilometrga.</p>"
                       "<p><strong>150</strong> — butun koʻtarilish, masofaga "
                       "boʻlinmagan; <strong>235</strong> — 470 ni 2 ga boʻlgan javob, "
                       "lekin 2 — bu masofa emas, boshlanish nuqtasi.</p>",
    },
    {
        "text": "<p>A shop had 480 notebooks in stock on day 3 and 300 notebooks on "
                "day 12. If notebooks sell at a constant rate, how many are sold each "
                "day?</p>",
        "choices": ["15", "20", "60", "180"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> Kamayish 480 − 300 = 180 ta, oʻtgan vaqt "
                       "12 − 3 = 9 kun: 180 ÷ 9 = 20 ta kuniga.</p>"
                       "<p><strong>15</strong> — 180 ni 12 ga boʻlgan javob, lekin sanoq "
                       "3-kundan boshlangan; <strong>180</strong> — butun kamayish.</p>",
    },
]


# =====================================================================
# SAT-7 — slope-intercept form
# =====================================================================

Q_SAT7 = [
    {
        "text": "<p>What is the slope of the line <i>y</i> = 7<i>x</i> − 2?</p>",
        "choices": ["−2", "2", "7", "9"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> y = mx + b da qiyalik — x oldidagi son.</p>"
                       "<p><strong>−2</strong> — bu b, chiziqning y oʻqini kesish "
                       "nuqtasi. Ikkalasi ham javoblar orasida turadi.</p>",
    },
    {
        "text": "<p>What is the <i>y</i>-intercept of the line <i>y</i> = −3<i>x</i> + 8?</p>",
        "choices": ["−3", "3", "5", "8"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Yolgʻiz turgan son — b, yaʼni "
                       "y-intercept.</p>"
                       "<p><strong>−3</strong> — qiyalik; <strong>5</strong> — ikki sonni "
                       "qoʻshib yuborgan javob (−3 + 8).</p>",
    },
    {
        "text": "<p>What is the slope of the line <i>y</i> = 5 − 2<i>x</i>?</p>",
        "choices": ["−2", "2", "5", "7"],
        "correct": "−2",
        "explanation": "<p><strong>−2.</strong> Hadlar oʻrin almashgan boʻlsa ham, x "
                       "oldidagi son — qiyalik, ishorasi bilan.</p>"
                       "<p><strong>5</strong> — bu b. Shakl «notoʻgʻri tartibda» "
                       "yozilganda birinchi sonni qiyalik deb olish — eng koʻp "
                       "uchraydigan xato.</p>",
    },
    {
        "text": "<p>Which equation represents a line with a slope of 1/2 and a "
                "<i>y</i>-intercept of −4?</p>",
        "choices": ["<i>y</i> = (1/2)<i>x</i> − 4", "<i>y</i> = (1/2)<i>x</i> + 4",
                    "<i>y</i> = 2<i>x</i> − 4", "<i>y</i> = −4<i>x</i> + 1/2"],
        "correct": "<i>y</i> = (1/2)<i>x</i> − 4",
        "explanation": "<p><strong>y = (1/2)x − 4.</strong> m x oldiga, b oxiriga "
                       "yoziladi, ishorasi bilan.</p>"
                       "<p><strong>y = −4x + 1/2</strong> — m va b oʻrin almashgan "
                       "javob.</p>",
    },
    {
        "text": "<p>A line has a slope of 3 and passes through (0, −5). Which equation "
                "represents this line?</p>",
        "choices": ["<i>y</i> = −5<i>x</i> + 3", "<i>y</i> = 3<i>x</i> − 5",
                    "<i>y</i> = 3<i>x</i> + 5", "<i>y</i> = 5<i>x</i> − 3"],
        "correct": "<i>y</i> = 3<i>x</i> − 5",
        "explanation": "<p><strong>y = 3x − 5.</strong> Nuqtaning x koordinatasi 0, "
                       "demak u nuqtaning oʻzi y-intercept: b = −5.</p>"
                       "<p><strong>y = 3x + 5</strong> — ishora tashlab ketilgan; "
                       "nuqta y oʻqining <b>pastida</b> turibdi.</p>",
    },
    {
        "text": "<p>A line has a slope of −1 and passes through (0, 6). Which equation "
                "represents this line?</p>",
        "choices": ["<i>y</i> = −<i>x</i> + 6", "<i>y</i> = −<i>x</i> − 6",
                    "<i>y</i> = <i>x</i> + 6", "<i>y</i> = 6<i>x</i> − 1"],
        "correct": "<i>y</i> = −<i>x</i> + 6",
        "explanation": "<p><strong>y = −x + 6.</strong> Qiyaligi −1 boʻlgan hadni "
                       "«−1x» emas, shunchaki «−x» deb yozamiz.</p>"
                       "<p><strong>y = 6x − 1</strong> — m va b almashgan javob.</p>",
    },
    {
        "text": "<p>What is the slope of the line 2<i>y</i> = 8<i>x</i> + 10?</p>",
        "choices": ["2", "4", "5", "8"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Shakl hali tayyor emas: ikkala tomonni "
                       "2 ga boʻlamiz → y = 4x + 5, demak qiyalik 4.</p>"
                       "<p><strong>8</strong> — boʻlishdan oldin oʻqilgan javob. Chap "
                       "tomonda <b>yolgʻiz y</b> turmaguncha m ni oʻqib boʻlmaydi.</p>",
    },
    {
        "text": "<p>What is the slope of the line 3<i>x</i> + <i>y</i> = 9?</p>",
        "choices": ["−3", "−1/3", "3", "9"],
        "correct": "−3",
        "explanation": "<p><strong>−3.</strong> y ga yechamiz: y = −3x + 9.</p>"
                       "<p><strong>3</strong> — 3x ni oʻtkazganda ishorasi "
                       "almashishini unutgan javob.</p>",
    },
    {
        "text": "<p>A line with a slope of 2 passes through (1, 7). What is the value of "
                "<i>b</i> in <i>y</i> = <i>mx</i> + <i>b</i>?</p>",
        "choices": ["2", "5", "7", "9"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 7 = 2(1) + b → 7 = 2 + b → b = 5.</p>"
                       "<p><strong>9</strong> — ayirish oʻrniga qoʻshgan javob (7 + 2); "
                       "<strong>7</strong> — nuqtaning y koordinatasi, b emas.</p>",
    },
    {
        "text": "<p>Which equation represents the line through the origin with a slope "
                "of −4?</p>",
        "choices": ["<i>y</i> = −4<i>x</i>", "<i>y</i> = −4<i>x</i> + 4",
                    "<i>y</i> = <i>x</i> − 4", "<i>y</i> = 4<i>x</i>"],
        "correct": "<i>y</i> = −4<i>x</i>",
        "explanation": "<p><strong>y = −4x.</strong> «Origin» — koordinata boshi (0, 0), "
                       "demak b = 0 va u umuman yozilmaydi.</p>"
                       "<p><strong>y = x − 4</strong> — −4 ni b deb olgan javob: u "
                       "qiyalik.</p>",
    },
    {
        "text": "<p>A summer pool pass costs $40, and each visit costs $3 more. The total "
                "cost is <i>y</i> = 3<i>x</i> + 40 for <i>x</i> visits. What is the total "
                "cost of 12 visits?</p>",
        "choices": ["$43", "$76", "$120", "$480"],
        "correct": "$76",
        "explanation": "<p><strong>$76.</strong> 3(12) + 40 = 36 + 40 = 76.</p>"
                       "<p><strong>$120</strong> — 3 × 40 hisoblangan; "
                       "<strong>$480</strong> — $40 ni har safar hisoblagan javob, "
                       "lekin u bir marta toʻlanadi.</p>",
    },
    {
        "text": "<p>In the model <i>y</i> = 3<i>x</i> + 40 above, which of the following "
                "is the best interpretation of 40?</p>",
        "choices": ["The cost of each visit is $40.",
                    "The one-time cost of the pass is $40.",
                    "A total of 40 visits are allowed.",
                    "The total cost of 3 visits is $40."],
        "correct": "The one-time cost of the pass is $40.",
        "explanation": "<p><strong>Bir martalik $40.</strong> 40 yolgʻiz turibdi — demak "
                       "u tashriflar soniga bogʻliq emas.</p>"
                       "<p>Harf bilan turgan son «har bir … uchun», yolgʻiz turgani "
                       "«bir marta» degani.</p>",
    },
    {
        "text": "<p>In the same model <i>y</i> = 3<i>x</i> + 40, which of the following "
                "is the best interpretation of 3?</p>",
        "choices": ["Each visit adds $3 to the total cost.",
                    "The pass costs $3.",
                    "Three visits are included in the pass.",
                    "The total cost is three times the number of visits."],
        "correct": "Each visit adds $3 to the total cost.",
        "explanation": "<p><strong>Har bir tashrif $3 qoʻshadi.</strong> 3 soni x bilan "
                       "turibdi — bu qiyalik.</p>"
                       "<p><strong>«The total cost is three times…»</strong> notoʻgʻri: "
                       "unda $40 hisobga olinmaydi.</p>",
    },
    {
        "text": "<p>A gym charges a $25 joining fee plus $12 each month, so the total "
                "cost is <i>C</i> = 12<i>m</i> + 25. What is the total cost after "
                "6 months?</p>",
        "choices": ["$37", "$72", "$97", "$150"],
        "correct": "$97",
        "explanation": "<p><strong>$97.</strong> 12(6) + 25 = 72 + 25 = 97.</p>"
                       "<p><strong>$72</strong> — bir martalik $25 qoʻshilmagan; "
                       "<strong>$150</strong> — $25 ni olti marta hisoblagan javob.</p>",
    },
    {
        "text": "<p>What is the slope of the line <i>y</i> = 4 − 7<i>x</i>?</p>",
        "choices": ["−7", "4", "7", "11"],
        "correct": "−7",
        "explanation": "<p><strong>−7.</strong> x oldidagi son ishorasi bilan olinadi, "
                       "hadlarning tartibi ahamiyatsiz.</p>"
                       "<p><strong>4</strong> — birinchi turgani uchun qiyalik deb "
                       "olingan, aslida u b. Har doim <b>x qayerda</b> — shunga qarang.</p>",
    },
    {
        "text": "<p>A line has a slope of 5 and passes through the point (2, 3). What is "
                "its <i>y</i>-intercept?</p>",
        "choices": ["−7", "−2", "3", "13"],
        "correct": "−7",
        "explanation": "<p><strong>−7.</strong> 3 = 5(2) + b → 3 = 10 + b → b = −7.</p>"
                       "<p><strong>13</strong> — ayirish oʻrniga qoʻshgan javob "
                       "(3 + 10). Nuqtadan y oʻqiga <b>chapga</b> yurilganda musbat "
                       "qiyalikda qiymat kamayadi.</p>",
    },
    {
        "text": "<p>What is the <i>y</i>-intercept of the line 4<i>x</i> − 2<i>y</i> = 14?</p>",
        "choices": ["−7", "−3.5", "3.5", "7"],
        "correct": "−7",
        "explanation": "<p><strong>−7.</strong> y ga yechamiz: −2y = −4x + 14 → "
                       "y = 2x − 7.</p>"
                       "<p><strong>7</strong> — manfiy songa boʻlishda ishora "
                       "almashishini unutgan javob; <strong>3.5</strong> — 14 ni 4 ga "
                       "boʻlgan javob.</p>",
    },
    {
        "text": "<p>A line passes through (−2, 9) and (2, 1). Which equation represents "
                "this line?</p>",
        "choices": ["<i>y</i> = −2<i>x</i> + 1", "<i>y</i> = −2<i>x</i> + 5",
                    "<i>y</i> = −(1/2)<i>x</i> + 5", "<i>y</i> = 2<i>x</i> + 5"],
        "correct": "<i>y</i> = −2<i>x</i> + 5",
        "explanation": "<p><strong>y = −2x + 5.</strong> m = (1 − 9) ÷ (2 − (−2)) = "
                       "−8 ÷ 4 = −2. Keyin 1 = −2(2) + b → b = 5.</p>"
                       "<p><strong>y = −2x + 1</strong> — nuqtaning y qiymatini b deb "
                       "olgan javob, lekin u nuqta y oʻqida emas (x = 2).</p>",
    },
    {
        "text": "<p>A candle is 24 centimetres tall and burns down 3 centimetres each "
                "hour. What is its height after 5 hours?</p>",
        "choices": ["9", "15", "21", "39"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> Model: y = 24 − 3x. 24 − 3(5) = "
                       "24 − 15 = 9 sm.</p>"
                       "<p><strong>39</strong> — ayirish oʻrniga qoʻshgan javob; "
                       "<strong>21</strong> — faqat bir soatdan keyingi balandlik.</p>",
    },
    {
        "text": "<p>A printing service charges $18 plus $2.50 for each poster. What is "
                "the total cost of 14 posters?</p>",
        "choices": ["$35", "$45", "$53", "$287"],
        "correct": "$53",
        "explanation": "<p><strong>$53.</strong> 2.50(14) + 18 = 35 + 18 = 53.</p>"
                       "<p><strong>$35</strong> — bir martalik $18 qoʻshilmagan; "
                       "<strong>$287</strong> — $18 ni har bir plakat uchun hisoblagan "
                       "javob (14 × 20.50).</p>",
    },
]


# =====================================================================
# SAT-8 — point-slope and standard form
# =====================================================================

Q_SAT8 = [
    {
        "text": "<p>Which equation represents, in point-slope form, the line through "
                "(3, 5) with a slope of 2?</p>",
        "choices": ["<i>y</i> − 3 = 2(<i>x</i> − 5)", "<i>y</i> − 5 = 2(<i>x</i> − 3)",
                    "<i>y</i> + 5 = 2(<i>x</i> + 3)", "<i>y</i> = 2(<i>x</i> − 3) + 5"],
        "correct": "<i>y</i> − 5 = 2(<i>x</i> − 3)",
        "explanation": "<p><strong>y − 5 = 2(x − 3).</strong> Formulada y ning yoniga "
                       "nuqtaning <b>y</b> koordinatasi, qavs ichiga <b>x</b> "
                       "koordinatasi yoziladi.</p>"
                       "<p><strong>y − 3 = 2(x − 5)</strong> — koordinatalar oʻrin "
                       "almashgan javob.</p>",
    },
    {
        "text": "<p>Which equation represents, in point-slope form, the line through "
                "(−1, 4) with a slope of −3?</p>",
        "choices": ["<i>y</i> − 4 = −3(<i>x</i> − 1)", "<i>y</i> − 4 = −3(<i>x</i> + 1)",
                    "<i>y</i> + 4 = −3(<i>x</i> − 1)", "<i>y</i> + 1 = −3(<i>x</i> − 4)"],
        "correct": "<i>y</i> − 4 = −3(<i>x</i> + 1)",
        "explanation": "<p><strong>y − 4 = −3(x + 1).</strong> x koordinatasi −1 boʻlgani "
                       "uchun x − (−1) = x <b>+</b> 1.</p>"
                       "<p><strong>y − 4 = −3(x − 1)</strong> — manfiy koordinatani "
                       "eʼtiborsiz qoldirgan javob.</p>",
    },
    {
        "text": "<p>What is the <i>x</i>-intercept of the graph of 2<i>x</i> + "
                "5<i>y</i> = 20?</p>",
        "choices": ["4", "5", "10", "20"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> x-intercept uchun y = 0: 2x = 20 → "
                       "x = 10.</p>"
                       "<p><strong>4</strong> — bu y-intercept (20 ÷ 5). Nomiga qarab "
                       "nol qoʻyiladigan harf <b>qarama-qarshi</b>: x-intercept uchun "
                       "y = 0.</p>",
    },
    {
        "text": "<p>What is the <i>y</i>-intercept of the graph of 2<i>x</i> + "
                "5<i>y</i> = 20?</p>",
        "choices": ["2", "4", "10", "20"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> y-intercept uchun x = 0: 5y = 20 → "
                       "y = 4.</p>"
                       "<p><strong>10</strong> — bu x-intercept. Bitta tenglama ikki "
                       "xil javob beradi — savol qaysi kesishmani soʻraganini oʻqing.</p>",
    },
    {
        "text": "<p>What is the slope of the line 5<i>x</i> + 2<i>y</i> = 12?</p>",
        "choices": ["−5/2", "−2/5", "2/5", "5/2"],
        "correct": "−5/2",
        "explanation": "<p><strong>−5/2.</strong> Qoida: qiyalik = −A ÷ B = −5 ÷ 2. "
                       "Tekshiruv: 2y = −5x + 12 → y = −(5/2)x + 6 ✓</p>"
                       "<p><strong>5/2</strong> — minus tushib qolgan javob. Ikkala "
                       "koeffitsient musbat boʻlsa, chiziq albatta pasayadi.</p>",
    },
    {
        "text": "<p>What is the slope of the line 3<i>x</i> − 4<i>y</i> = 8?</p>",
        "choices": ["−4/3", "−3/4", "3/4", "4/3"],
        "correct": "3/4",
        "explanation": "<p><strong>3/4.</strong> −A ÷ B = −3 ÷ (−4) = 3/4 — ikki minus "
                       "musbat beradi.</p>"
                       "<p><strong>−3/4</strong> — B ning manfiy ekanini hisobga "
                       "olmagan javob.</p>",
    },
    {
        "text": "<p>Which equation is equivalent to <i>y</i> = 4<i>x</i> − 3, written in "
                "standard form?</p>",
        "choices": ["4<i>x</i> − <i>y</i> = 3", "4<i>x</i> − <i>y</i> = −3",
                    "4<i>x</i> + <i>y</i> = 3", "<i>x</i> − 4<i>y</i> = 3"],
        "correct": "4<i>x</i> − <i>y</i> = 3",
        "explanation": "<p><strong>4x − y = 3.</strong> Ikkala tomondan y ni ayiramiz va "
                       "3 ni qoʻshamiz: 4x − y = 3.</p>"
                       "<p><strong>4x − y = −3</strong> — oʻng tomonning ishorasi "
                       "almashtirilmagan javob. Tekshirish uchun x = 1 qoʻying: "
                       "y = 1, va 4 − 1 = 3 ✓</p>",
    },
    {
        "text": "<p>Which point lies on the line <i>y</i> − 2 = 5(<i>x</i> − 1)?</p>",
        "choices": ["(−1, 2)", "(1, −2)", "(1, 2)", "(2, 1)"],
        "correct": "(1, 2)",
        "explanation": "<p><strong>(1, 2).</strong> Nuqta-qiyalik shakli oʻzi ishlatilgan "
                       "nuqtani koʻrsatib turadi: qavs ichidagi son x, y yonidagi son y.</p>"
                       "<p>Tekshiruv: x = 1 da oʻng tomon 0, demak y − 2 = 0 va y = 2 ✓ "
                       "<strong>(2, 1)</strong> — koordinatalar almashtirilgan javob.</p>",
    },
    {
        "text": "<p>Which equation is equivalent to <i>y</i> + 3 = 2(<i>x</i> − 4)?</p>",
        "choices": ["<i>y</i> = 2<i>x</i> − 11", "<i>y</i> = 2<i>x</i> − 5",
                    "<i>y</i> = 2<i>x</i> − 1", "<i>y</i> = 2<i>x</i> + 11"],
        "correct": "<i>y</i> = 2<i>x</i> − 11",
        "explanation": "<p><strong>y = 2x − 11.</strong> Qavsni ochamiz: y + 3 = 2x − 8, "
                       "keyin 3 ni ayiramiz: y = 2x − 11.</p>"
                       "<p><strong>y = 2x − 5</strong> — 3 ni ayirish oʻrniga qoʻshgan "
                       "javob (−8 + 3).</p>",
    },
    {
        "text": "<p>What is the <i>x</i>-intercept of the graph of 7<i>x</i> − "
                "3<i>y</i> = 21?</p>",
        "choices": ["−7", "3", "7", "21"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> y = 0 qoʻyamiz: 7x = 21 → x = 3.</p>"
                       "<p><strong>−7</strong> — bu y-intercept (−3y = 21 → y = −7); "
                       "<strong>7</strong> — 21 ni 3 ga boʻlgan javob, lekin 3 — bu "
                       "y ning koeffitsienti.</p>",
    },
    {
        "text": "<p>A 60-minute radio show is made up of songs lasting 2 minutes each and "
                "interviews lasting 5 minutes each, so 2<i>s</i> + 5<i>i</i> = 60. "
                "If the show has 4 interviews, how many songs does it have?</p>",
        "choices": ["8", "20", "28", "30"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> 2s + 5(4) = 60 → 2s + 20 = 60 → "
                       "2s = 40 → s = 20.</p>"
                       "<p><strong>28</strong> — suhbatlar sonini daqiqa deb olgan javob "
                       "(60 − 4) ÷ 2; <strong>30</strong> — suhbatlarni umuman hisobga "
                       "olmagan javob.</p>",
    },
    {
        "text": "<p>In the equation 2<i>s</i> + 5<i>i</i> = 60 above, which of the "
                "following is the best interpretation of 60?</p>",
        "choices": ["The number of songs in the show.",
                    "The total length of the show, in minutes.",
                    "The length of each interview, in minutes.",
                    "The number of items in the show."],
        "correct": "The total length of the show, in minutes.",
        "explanation": "<p><strong>Koʻrsatuvning umumiy uzunligi.</strong> Standart "
                       "shaklda oʻng tomondagi son — jami, yaʼni ikki qismning "
                       "yigʻindisi.</p>"
                       "<p>Chap tomondagi koeffitsientlar (2 va 5) esa <b>har bir "
                       "birlik</b> qancha vaqt olishini bildiradi.</p>",
    },
    {
        "text": "<p>In the same equation 2<i>s</i> + 5<i>i</i> = 60, which of the "
                "following is the best interpretation of 5?</p>",
        "choices": ["There are 5 interviews in the show.",
                    "Each interview lasts 5 minutes.",
                    "The show has 5 parts.",
                    "Each song lasts 5 minutes."],
        "correct": "Each interview lasts 5 minutes.",
        "explanation": "<p><strong>Har bir suhbat 5 daqiqa.</strong> 5 soni <i>i</i> "
                       "bilan turibdi, demak u har bir suhbatga tegishli.</p>"
                       "<p><strong>«Each song lasts 5 minutes»</strong> — koeffitsientlar "
                       "almashtirilgan: qoʻshiqniki 2.</p>",
    },
    {
        "text": "<p>A school sells adult tickets for $3 and child tickets for $2, and "
                "collects $60 in total, so 3<i>a</i> + 2<i>c</i> = 60. If 15 child "
                "tickets were sold, how many adult tickets were sold?</p>",
        "choices": ["10", "15", "20", "30"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 3a + 2(15) = 60 → 3a + 30 = 60 → "
                       "3a = 30 → a = 10.</p>"
                       "<p><strong>20</strong> — bolalar chiptasini umuman hisobga "
                       "olmagan javob (60 ÷ 3); <strong>30</strong> — bolalarga "
                       "ketgan pul, chiptalar soni emas.</p>",
    },
    {
        "text": "<p>Which equation represents, in point-slope form, the line through "
                "(5, −2) with a slope of −1?</p>",
        "choices": ["<i>y</i> − 2 = −(<i>x</i> − 5)", "<i>y</i> + 2 = −(<i>x</i> − 5)",
                    "<i>y</i> + 2 = −(<i>x</i> + 5)", "<i>y</i> + 5 = −(<i>x</i> − 2)"],
        "correct": "<i>y</i> + 2 = −(<i>x</i> − 5)",
        "explanation": "<p><strong>y + 2 = −(x − 5).</strong> y koordinatasi −2 boʻlgani "
                       "uchun y − (−2) = y <b>+</b> 2; x koordinatasi 5 musbat, shuning "
                       "uchun qavsda minus qoladi.</p>"
                       "<p><strong>y − 2 = −(x − 5)</strong> — manfiy y ni eʼtiborsiz "
                       "qoldirgan javob.</p>",
    },
    {
        "text": "<p>What is the <i>x</i>-intercept of the graph of 4<i>x</i> + "
                "9<i>y</i> = 36?</p>",
        "choices": ["4", "9", "13", "36"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> y = 0 qoʻyamiz: 4x = 36 → x = 9.</p>"
                       "<p><strong>4</strong> — bu y-intercept (9y = 36 → y = 4). "
                       "Ikkala son ham javoblar orasida turibdi, shuning uchun savolning "
                       "birinchi harfiga qarang.</p>",
    },
    {
        "text": "<p>The graph of 6<i>x</i> + <i>ky</i> = 24 has a <i>y</i>-intercept of 3, "
                "where <i>k</i> is a constant. What is the value of <i>k</i>?</p>",
        "choices": ["3", "4", "6", "8"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> y-intercept uchun x = 0: ky = 24, va "
                       "y = 3 boʻlgani uchun 3k = 24 → k = 8.</p>"
                       "<p><strong>4</strong> — 24 ni 6 ga boʻlgan javob, lekin 6 — bu "
                       "<i>x</i> ning koeffitsienti va u x = 0 da yoʻqoladi.</p>",
    },
    {
        "text": "<p>Which equation is equivalent to 5<i>x</i> − 2<i>y</i> = 30?</p>",
        "choices": ["<i>y</i> = −(5/2)<i>x</i> − 15", "<i>y</i> = (2/5)<i>x</i> − 15",
                    "<i>y</i> = (5/2)<i>x</i> − 15", "<i>y</i> = (5/2)<i>x</i> + 15"],
        "correct": "<i>y</i> = (5/2)<i>x</i> − 15",
        "explanation": "<p><strong>y = (5/2)x − 15.</strong> −2y = −5x + 30, keyin "
                       "ikkala tomonni −2 ga boʻlamiz: ikkala had ham ishorasini "
                       "almashtiradi.</p>"
                       "<p><strong>y = (5/2)x + 15</strong> — 30 ni −2 ga boʻlishda "
                       "ishorani unutgan javob.</p>",
    },
    {
        "text": "<p>A caterer spends exactly $96 on sandwiches costing $4 each and salads "
                "costing $6 each. If she buys 12 sandwiches, how many salads does "
                "she buy?</p>",
        "choices": ["8", "12", "16", "24"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Model: 4s + 6l = 96. 4(12) = 48, demak "
                       "6l = 48 va l = 8.</p>"
                       "<p><strong>16</strong> — butun pulni salatga sarflagan javob "
                       "(96 ÷ 6); <strong>24</strong> — 96 ÷ 4, yaʼni sendvichlar "
                       "narxiga boʻlingan javob.</p>",
    },
    {
        "text": "<p>A tank is filled by two pipes. Pipe A delivers 8 litres a minute and "
                "pipe B delivers 5 litres a minute, and together they must deliver "
                "120 litres. If pipe A runs for 10 minutes, for how many minutes must "
                "pipe B run?</p>",
        "choices": ["8", "10", "15", "24"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Model: 8a + 5b = 120. 8(10) = 80, demak "
                       "5b = 40 va b = 8 daqiqa.</p>"
                       "<p><strong>24</strong> — A quvurini umuman hisobga olmagan javob "
                       "(120 ÷ 5); <strong>15</strong> — 120 ni 8 ga boʻlgan javob.</p>",
    },
]


# =====================================================================
# SAT-9 — graphing linear equations quickly
# =====================================================================

Q_SAT9 = [
    {
        "text": "<p>At which point does the line <i>y</i> = 2<i>x</i> − 6 cross the "
                "<i>y</i>-axis?</p>",
        "choices": ["(−6, 0)", "(0, −6)", "(0, 6)", "(3, 0)"],
        "correct": "(0, −6)",
        "explanation": "<p><strong>(0, −6).</strong> y oʻqida x = 0, demak y = −6.</p>"
                       "<p><strong>(3, 0)</strong> — bu x oʻqidagi nuqta; "
                       "<strong>(−6, 0)</strong> — koordinatalar almashtirilgan javob.</p>",
    },
    {
        "text": "<p>At which point does the line <i>y</i> = 2<i>x</i> − 6 cross the "
                "<i>x</i>-axis?</p>",
        "choices": ["(0, −6)", "(0, 3)", "(3, 0)", "(6, 0)"],
        "correct": "(3, 0)",
        "explanation": "<p><strong>(3, 0).</strong> x oʻqida y = 0: 0 = 2x − 6 → "
                       "2x = 6 → x = 3.</p>"
                       "<p><strong>(6, 0)</strong> — 6 ni toʻgʻridan-toʻgʻri javob deb "
                       "olgan variant; uni avval 2 ga boʻlish kerak edi.</p>",
    },
    {
        "text": "<p>Which of the following lines has the steepest graph?</p>",
        "choices": ["<i>y</i> = 0.2<i>x</i>", "<i>y</i> = <i>x</i> + 9",
                    "<i>y</i> = 3<i>x</i> − 1", "<i>y</i> = −4<i>x</i>"],
        "correct": "<i>y</i> = −4<i>x</i>",
        "explanation": "<p><strong>y = −4x.</strong> Tiklikni qiyalikning <b>kattaligi</b> "
                       "hal qiladi, ishorasi emas: 4 &gt; 3 &gt; 1 &gt; 0.2.</p>"
                       "<p><strong>y = x + 9</strong> — 9 kattaligi uchun tanlanadi, "
                       "lekin 9 chiziqni faqat yuqoriroqqa koʻchiradi, tikroq "
                       "qilmaydi.</p>",
    },
    {
        "text": "<p>A line falls from left to right in the <i>xy</i>-plane. What must be "
                "true about its slope?</p>",
        "choices": ["It is negative.", "It is positive.", "It is zero.",
                    "It is undefined."],
        "correct": "It is negative.",
        "explanation": "<p><strong>Manfiy.</strong> Oʻngga yurganda pastga tushish — "
                       "manfiy qiyalik.</p>"
                       "<p><strong>Zero</strong> gorizontal chiziqniki, "
                       "<strong>undefined</strong> vertikalniki — ikkalasi ham na "
                       "koʻtariladi, na tushadi.</p>",
    },
    {
        "text": "<p>What are the two intercepts of the graph of 2<i>x</i> + "
                "3<i>y</i> = 12?</p>",
        "choices": ["(4, 0) and (0, 6)", "(6, 0) and (0, 4)", "(2, 0) and (0, 3)",
                    "(12, 0) and (0, 12)"],
        "correct": "(6, 0) and (0, 4)",
        "explanation": "<p><strong>(6, 0) va (0, 4).</strong> y = 0 → 2x = 12 → x = 6; "
                       "x = 0 → 3y = 12 → y = 4.</p>"
                       "<p><strong>(4, 0) va (0, 6)</strong> — ikkala kesishma oʻrin "
                       "almashgan: har bir kesishmada <b>qarama-qarshi</b> harfga nol "
                       "qoʻyiladi.</p>",
    },
    {
        "text": "<p>Which point lies on the graph of <i>y</i> = −3<i>x</i> + 5?</p>",
        "choices": ["(0, −5)", "(1, 8)", "(2, −1)", "(2, 1)"],
        "correct": "(2, −1)",
        "explanation": "<p><strong>(2, −1).</strong> x = 2 qoʻyamiz: −3(2) + 5 = "
                       "−6 + 5 = −1 ✓</p>"
                       "<p><strong>(2, 1)</strong> — ishorada adashgan javob; "
                       "<strong>(0, −5)</strong> — b ning ishorasini almashtirgan "
                       "javob (aslida (0, 5)).</p>",
    },
    {
        "text": "<p>A line has a positive slope and a negative <i>y</i>-intercept. "
                "Through which quadrant does the line <b>NOT</b> pass?</p>",
        "choices": ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"],
        "correct": "Quadrant II",
        "explanation": "<p><strong>Quadrant II.</strong> II chorakda x manfiy, y musbat. "
                       "Musbat qiyalikda x manfiy boʻlsa <i>mx</i> ham manfiy, ustiga "
                       "manfiy b qoʻshiladi — y hech qachon musbat boʻlmaydi.</p>"
                       "<p>Bitta son qoʻyib tekshiring: y = 2x − 5 da x = −1 boʻlsa "
                       "y = −7.</p>",
    },
    {
        "text": "<p>A line has a negative slope and a positive <i>y</i>-intercept. "
                "Through which quadrant does the line <b>NOT</b> pass?</p>",
        "choices": ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"],
        "correct": "Quadrant III",
        "explanation": "<p><strong>Quadrant III.</strong> III chorakda ikkala koordinata "
                       "ham manfiy. Manfiy qiyalikda x manfiy boʻlsa <i>mx</i> "
                       "<b>musbat</b> boʻladi va ustiga musbat b qoʻshiladi — y manfiy "
                       "boʻla olmaydi.</p>"
                       "<p>Tekshiring: y = −2x + 5 da x = −1 boʻlsa y = 7.</p>",
    },
    {
        "text": "<p>What does the graph of <i>y</i> = 4 look like in the "
                "<i>xy</i>-plane?</p>",
        "choices": ["A horizontal line through (0, 4)", "A vertical line through (4, 0)",
                    "A line through the origin with slope 4",
                    "A single point at (0, 4)"],
        "correct": "A horizontal line through (0, 4)",
        "explanation": "<p><strong>Gorizontal chiziq.</strong> y har doim 4 ga teng, "
                       "x esa istalgan qiymatni oladi — qiyaligi 0.</p>"
                       "<p><strong>«A single point»</strong> notoʻgʻri: tenglama "
                       "cheksiz koʻp nuqtani qanoatlantiradi.</p>",
    },
    {
        "text": "<p>What does the graph of <i>x</i> = −2 look like in the "
                "<i>xy</i>-plane?</p>",
        "choices": ["A horizontal line through (0, −2)",
                    "A vertical line through (−2, 0)",
                    "A line with slope −2", "A single point at (−2, 0)"],
        "correct": "A vertical line through (−2, 0)",
        "explanation": "<p><strong>Vertikal chiziq.</strong> x har doim −2, y esa erkin — "
                       "qiyaligi <b>undefined</b>.</p>"
                       "<p>Qoidani yodda tuting: «x = son» → vertikal, «y = son» → "
                       "gorizontal.</p>",
    },
    {
        "text": "<p>A cyclist rides 20 kilometres in week 0 and adds 6 kilometres each "
                "week, so her weekly distance is <i>y</i> = 6<i>x</i> + 20. Which point "
                "lies on the graph at week 5?</p>",
        "choices": ["(5, 26)", "(5, 30)", "(5, 50)", "(5, 120)"],
        "correct": "(5, 50)",
        "explanation": "<p><strong>(5, 50).</strong> 6(5) + 20 = 30 + 20 = 50.</p>"
                       "<p><strong>(5, 30)</strong> — boshlangʻich 20 ni qoʻshmagan; "
                       "<strong>(5, 26)</strong> — faqat bir haftadan keyingi masofa.</p>",
    },
    {
        "text": "<p>On the graph of <i>y</i> = 6<i>x</i> + 20 above, which of the "
                "following is the best interpretation of the <i>y</i>-intercept?</p>",
        "choices": ["She rode 20 kilometres in week 0.",
                    "She adds 20 kilometres each week.",
                    "She rode for 20 weeks.",
                    "Her longest ride was 20 kilometres."],
        "correct": "She rode 20 kilometres in week 0.",
        "explanation": "<p><strong>0-haftada 20 km.</strong> y-intercept — x = 0 "
                       "boʻlgandagi qiymat, yaʼni boshlangʻich masofa.</p>"
                       "<p><strong>«Adds 20 each week»</strong> — bu qiyalikning "
                       "taʼrifi, lekin qiyalik 6 ga teng.</p>",
    },
    {
        "text": "<p>A straight-line graph of cost rises from (0, 25) to (10, 75). "
                "What is its slope?</p>",
        "choices": ["2.5", "5", "7.5", "50"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> (75 − 25) ÷ (10 − 0) = 50 ÷ 10 = 5.</p>"
                       "<p><strong>50</strong> — faqat koʻtarilish; <strong>7.5</strong> "
                       "— 75 ni 10 ga boʻlgan javob, lekin boshlangʻich 25 hisobga "
                       "olinmagan.</p>",
    },
    {
        "text": "<p>The graph of a line passes through the origin. Which of the following "
                "must be true?</p>",
        "choices": ["Its slope is 0.", "Its slope is 1.",
                    "Its <i>y</i>-intercept is 0.", "Its <i>y</i>-intercept is 1."],
        "correct": "Its <i>y</i>-intercept is 0.",
        "explanation": "<p><strong>y-intercept 0.</strong> Boshdan oʻtgan chiziq (0, 0) "
                       "nuqtadan oʻtadi, demak b = 0.</p>"
                       "<p><strong>«Slope is 0»</strong> notoʻgʻri: boshdan oʻtgan "
                       "chiziqning qiyaligi istalgan son boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>What is the <i>x</i>-intercept of the graph of <i>y</i> = "
                "−2<i>x</i> + 8?</p>",
        "choices": ["−4", "2", "4", "8"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> y = 0: 0 = −2x + 8 → 2x = 8 → x = 4.</p>"
                       "<p><strong>8</strong> — bu b, yaʼni <i>y</i>-intercept; "
                       "<strong>−4</strong> — 8 ni −2 ga boʻlishda ishorani "
                       "tekshirmagan javob.</p>",
    },
    {
        "text": "<p>Which of the following lines is <b>NOT</b> steeper than "
                "<i>y</i> = 2<i>x</i>?</p>",
        "choices": ["<i>y</i> = 3<i>x</i>", "<i>y</i> = −4<i>x</i>",
                    "<i>y</i> = −5<i>x</i> + 1", "<i>y</i> = 0.5<i>x</i> + 9"],
        "correct": "<i>y</i> = 0.5<i>x</i> + 9",
        "explanation": "<p><strong>y = 0.5x + 9.</strong> Uning qiyaligi 0.5, kattaligi "
                       "2 dan kichik — demak yotiqroq.</p>"
                       "<p><strong>y = −5x + 1</strong> tikroq: tiklikda ishora emas, "
                       "<b>kattalik</b> hisobga olinadi. +9 esa tiklikka umuman "
                       "taʼsir qilmaydi.</p>",
    },
    {
        "text": "<p>A line passes through (0, −3) and (6, 0). Which equation represents "
                "this line?</p>",
        "choices": ["<i>y</i> = −(1/2)<i>x</i> − 3", "<i>y</i> = (1/2)<i>x</i> − 3",
                    "<i>y</i> = (1/2)<i>x</i> + 3", "<i>y</i> = 2<i>x</i> − 3"],
        "correct": "<i>y</i> = (1/2)<i>x</i> − 3",
        "explanation": "<p><strong>y = (1/2)x − 3.</strong> m = (0 − (−3)) ÷ (6 − 0) = "
                       "3 ÷ 6 = 1/2, va (0, −3) nuqtasi darhol b = −3 ni beradi.</p>"
                       "<p><strong>y = 2x − 3</strong> — qiyalik teskari olingan "
                       "(6 ÷ 3).</p>",
    },
    {
        "text": "<p>The graph of 3<i>x</i> + <i>ky</i> = 12 has an <i>x</i>-intercept of 4 "
                "and a <i>y</i>-intercept of 6, where <i>k</i> is a constant. What is the "
                "value of <i>k</i>?</p>",
        "choices": ["2", "3", "4", "6"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> y-intercept uchun x = 0: ky = 12, va "
                       "y = 6 boʻlgani uchun 6k = 12 → k = 2.</p>"
                       "<p><strong>3</strong> — <i>x</i> ning koeffitsienti, u x = 0 da "
                       "yoʻqoladi. (x-intercept 4 esa berilgan maʼlumotni tasdiqlaydi: "
                       "3 × 4 = 12 ✓)</p>",
    },
    {
        "text": "<p>A phone's battery starts at 80 percent and loses 4 percent each hour. "
                "Which point lies on the graph of battery level against hours at hour 9?</p>",
        "choices": ["(9, 36)", "(9, 44)", "(9, 71)", "(9, 76)"],
        "correct": "(9, 44)",
        "explanation": "<p><strong>(9, 44).</strong> Model: y = 80 − 4x. "
                       "80 − 4(9) = 80 − 36 = 44.</p>"
                       "<p><strong>(9, 36)</strong> — faqat yoʻqotilgan foiz; "
                       "<strong>(9, 71)</strong> — soatiga 1 foiz kamaytirgan javob.</p>",
    },
    {
        "text": "<p>A tree is 150 centimetres tall and grows 20 centimetres each year. "
                "After how many years will it be 350 centimetres tall?</p>",
        "choices": ["10", "17.5", "20", "25"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 150 + 20y = 350 → 20y = 200 → "
                       "y = 10.</p>"
                       "<p><strong>17.5</strong> — boshlangʻich balandlikni ayirmagan "
                       "javob (350 ÷ 20); <strong>25</strong> — ayirish oʻrniga "
                       "qoʻshgan javob (500 ÷ 20).</p>",
    },
]


# =====================================================================
# SAT-10 — interpreting slope and intercept in context
# =====================================================================

Q_SAT10 = [
    {
        "text": "<p>A worker's pay, in dollars, for <i>h</i> hours is <i>P</i> = "
                "15<i>h</i> + 50. Which of the following is the best interpretation "
                "of 15?</p>",
        "choices": ["The pay increases by $15 for each additional hour.",
                    "The worker is paid $15 in total.",
                    "The worker works 15 hours.",
                    "The fixed fee is $15."],
        "correct": "The pay increases by $15 for each additional hour.",
        "explanation": "<p><strong>Har bir qoʻshimcha soat $15 qoʻshadi.</strong> "
                       "15 soni <i>h</i> bilan turibdi — demak u qiyalik.</p>"
                       "<p><strong>«The fixed fee is $15»</strong> — bu 50 ning "
                       "taʼrifi. Yolgʻiz turgan son doimiy toʻlov.</p>",
    },
    {
        "text": "<p>In the same model <i>P</i> = 15<i>h</i> + 50, which of the following "
                "is the best interpretation of 50?</p>",
        "choices": ["The worker earns $50 each hour.",
                    "The worker is paid $50 even if no hours are worked.",
                    "The worker works at most 50 hours.",
                    "The total pay is always $50."],
        "correct": "The worker is paid $50 even if no hours are worked.",
        "explanation": "<p><strong>Hech soat ishlanmasa ham $50.</strong> b — bu "
                       "<i>h</i> = 0 boʻlgandagi qiymat.</p>"
                       "<p><strong>«At most 50 hours»</strong> — tengsizlik tili; "
                       "chiziqli model hech qanday chegara belgilamaydi.</p>",
    },
    {
        "text": "<p>The number of litres in a tank after <i>t</i> minutes is "
                "<i>L</i> = 200 − 4<i>t</i>. Which of the following is the best "
                "interpretation of −4?</p>",
        "choices": ["The tank loses 4 litres each minute.",
                    "The tank holds −4 litres.",
                    "The tank is empty after 4 minutes.",
                    "The tank starts with 4 litres."],
        "correct": "The tank loses 4 litres each minute.",
        "explanation": "<p><strong>Har daqiqada 4 litr kamayadi.</strong> Minus "
                       "«kamayadi» degani, «manfiy suv» degani emas.</p>"
                       "<p>Ishorani tushuntirishga har doim <b>soʻz bilan</b> "
                       "qoʻshing: yoʻqotadi, kamayadi, tushadi.</p>",
    },
    {
        "text": "<p>In the same model <i>L</i> = 200 − 4<i>t</i>, which of the following "
                "is the best interpretation of 200?</p>",
        "choices": ["The tank loses 200 litres each minute.",
                    "The tank contained 200 litres at the start.",
                    "The tank is empty after 200 minutes.",
                    "The tank can hold at most 200 litres."],
        "correct": "The tank contained 200 litres at the start.",
        "explanation": "<p><strong>Boshida 200 litr bor edi.</strong> 200 yolgʻiz "
                       "turibdi — t = 0 boʻlgandagi qiymat.</p>"
                       "<p><strong>«Can hold at most»</strong> — bakning sigʻimi haqida "
                       "model hech narsa demaydi; u faqat boshlangʻich miqdorni "
                       "beradi.</p>",
    },
    {
        "text": "<p>The cost, in dollars, of renting a car and driving <i>m</i> miles is "
                "<i>C</i> = 0.62<i>m</i> + 45. Which of the following is the best "
                "interpretation of 0.62?</p>",
        "choices": ["The total rental cost is $0.62.",
                    "The cost increases by $0.62 for each mile driven.",
                    "The car can be driven 0.62 miles.",
                    "The fixed rental fee is $0.62."],
        "correct": "The cost increases by $0.62 for each mile driven.",
        "explanation": "<p><strong>Har bir mil $0.62 qoʻshadi.</strong> 0.62 soni "
                       "<i>m</i> bilan turibdi.</p>"
                       "<p>Birligi bilan oʻqing: «dollar, har bir milga» — mos keladi. "
                       "Bu tekshiruvning oʻzi javobni tasdiqlaydi.</p>",
    },
    {
        "text": "<p>The total cost of <i>n</i> tickets is <i>T</i> = 9<i>n</i>. Which of "
                "the following is the best interpretation of 9?</p>",
        "choices": ["Each ticket costs $9.",
                    "There is a $9 booking fee.",
                    "Nine tickets were bought.",
                    "The total cost is $9."],
        "correct": "Each ticket costs $9.",
        "explanation": "<p><strong>Har bir chipta $9.</strong> Bu yerda doimiy toʻlov "
                       "yoʻq (b = 0), shuning uchun bitta chiptaning <b>jami</b> narxi "
                       "ham aynan $9 ga teng.</p>"
                       "<p>Diqqat: b = 0 boʻlgandagina «bittaga jami» va qiyalik "
                       "bir xil boʻladi.</p>",
    },
    {
        "text": "<p>A student's savings, in dollars, after <i>w</i> weeks is "
                "<i>S</i> = 25<i>w</i> + 120. Which of the following is the best "
                "interpretation of 120?</p>",
        "choices": ["She saves $120 each week.",
                    "She had $120 before she started saving weekly.",
                    "She will save for 120 weeks.",
                    "Her goal is $120."],
        "correct": "She had $120 before she started saving weekly.",
        "explanation": "<p><strong>Boshida $120 bor edi.</strong> w = 0 boʻlganda "
                       "S = 120.</p>"
                       "<p><strong>«Saves $120 each week»</strong> — qiyalikning "
                       "taʼrifi, lekin qiyalik 25.</p>",
    },
    {
        "text": "<p>In the same model <i>S</i> = 25<i>w</i> + 120, which of the following "
                "is the best interpretation of 25?</p>",
        "choices": ["She saves $25 each week.",
                    "She started with $25.",
                    "She saves for 25 weeks.",
                    "Her savings are 25 times her weeks."],
        "correct": "She saves $25 each week.",
        "explanation": "<p><strong>Har hafta $25 jamgʻaradi.</strong> 25 soni <i>w</i> "
                       "bilan turibdi.</p>"
                       "<p><strong>«25 times her weeks»</strong> — bu $120 ni "
                       "unutgan javob.</p>",
    },
    {
        "text": "<p>A model for a young tree's height, in metres, is <i>H</i> = "
                "0.4<i>y</i> + 1.2, where <i>y</i> is years since planting. Which of the "
                "following is the best interpretation of 1.2?</p>",
        "choices": ["The tree grows 1.2 metres each year.",
                    "The tree was 1.2 metres tall when it was planted.",
                    "The tree will reach 1.2 metres.",
                    "The tree is 1.2 years old."],
        "correct": "The tree was 1.2 metres tall when it was planted.",
        "explanation": "<p><strong>Ekilgan paytda 1.2 metr edi.</strong> y = 0 — "
                       "ekilgan yil.</p>"
                       "<p>Bu yerda b maʼnoli chiqdi. SAT ba'zan b maʼnosiz boʻladigan "
                       "modelni ham beradi — oʻshanda «does not make sense» toʻgʻri "
                       "javob boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>In the model <i>C</i> = 0.62<i>m</i> + 45, <i>C</i> is in dollars and "
                "<i>m</i> is in miles. What are the units of the slope?</p>",
        "choices": ["Dollars", "Miles", "Dollars per mile", "Miles per dollar"],
        "correct": "Dollars per mile",
        "explanation": "<p><strong>Dollar har bir milga.</strong> Qiyalikning birligi "
                       "har doim «y ning birligi ÷ x ning birligi».</p>"
                       "<p><strong>Miles per dollar</strong> — teskari olingan. Birlikni "
                       "ovoz chiqarib aytish notoʻgʻri sonni darhol fosh qiladi.</p>",
    },
    {
        "text": "<p>Using <i>P</i> = 15<i>h</i> + 50, what is the pay for 4 hours of "
                "work?</p>",
        "choices": ["$60", "$65", "$110", "$200"],
        "correct": "$110",
        "explanation": "<p><strong>$110.</strong> 15(4) + 50 = 60 + 50 = 110.</p>"
                       "<p><strong>$60</strong> — doimiy $50 qoʻshilmagan; "
                       "<strong>$200</strong> — $50 ni har soat uchun hisoblagan "
                       "javob.</p>",
    },
    {
        "text": "<p>Using <i>P</i> = 15<i>h</i> + 50, how much more is the pay for "
                "5 hours than for 4 hours?</p>",
        "choices": ["$15", "$50", "$65", "$125"],
        "correct": "$15",
        "explanation": "<p><strong>$15.</strong> 125 − 110 = 15 — bu aynan qiyalikning "
                       "oʻzi. Har bir qoʻshimcha soat toʻlovni shuncha oshiradi.</p>"
                       "<p><strong>$125</strong> — besh soatlik <b>jami</b> toʻlov, "
                       "farqi emas. Savol «how much more» deb soʻradi.</p>",
    },
    {
        "text": "<p>Using <i>L</i> = 200 − 4<i>t</i>, after how many minutes is the tank "
                "empty?</p>",
        "choices": ["40", "50", "196", "800"],
        "correct": "50",
        "explanation": "<p><strong>50.</strong> Boʻsh boʻlishi L = 0 degani: "
                       "200 − 4t = 0 → 4t = 200 → t = 50.</p>"
                       "<p><strong>196</strong> — bir daqiqadan keyingi hajm "
                       "(200 − 4); <strong>800</strong> — boʻlish oʻrniga "
                       "koʻpaytirgan javob.</p>",
    },
    {
        "text": "<p>Using <i>S</i> = 25<i>w</i> + 120, after how many weeks will the "
                "student have $370?</p>",
        "choices": ["10", "14.8", "19.6", "25"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 25w + 120 = 370 → 25w = 250 → "
                       "w = 10.</p>"
                       "<p><strong>14.8</strong> — boshlangʻich $120 ni ayirmagan javob "
                       "(370 ÷ 25); <strong>19.6</strong> — ayirish oʻrniga qoʻshgan "
                       "javob (490 ÷ 25).</p>",
    },
    {
        "text": "<p>A tailor's total charge, in dollars, for <i>m</i> metres is "
                "12<i>m</i> + 25. What is the total charge for one metre?</p>",
        "choices": ["$12", "$25", "$37", "$49"],
        "correct": "$37",
        "explanation": "<p><strong>$37.</strong> 12(1) + 25 = 37 — bir metrning "
                       "<b>jami</b> narxi.</p>"
                       "<p><strong>$12</strong> — bu faqat qiyalik, yaʼni har bir "
                       "qoʻshimcha metrning narxi. Qiyalik jamini emas, oʻzgarishni "
                       "bildiradi.</p>",
    },
    {
        "text": "<p>In the same model 12<i>m</i> + 25, which of the following is the best "
                "interpretation of 12?</p>",
        "choices": ["The total charge for one metre is $12.",
                    "Each additional metre adds $12 to the charge.",
                    "The fixed fee is $12.",
                    "The tailor sews at most 12 metres."],
        "correct": "Each additional metre adds $12 to the charge.",
        "explanation": "<p><strong>Har bir qoʻshimcha metr $12 qoʻshadi.</strong></p>"
                       "<p><strong>«The total charge for one metre is $12»</strong> — "
                       "eng koʻp tanlanadigan notoʻgʻri javob: bir metrning jami narxi "
                       "$37, chunki $25 baribir qoʻshiladi.</p>",
    },
    {
        "text": "<p>Plan A costs <i>C</i> = 5<i>x</i> + 60 and plan B costs "
                "<i>C</i> = 9<i>x</i> + 20, where <i>x</i> is the number of units. "
                "At 5 units, which plan costs more, and by how much?</p>",
        "choices": ["Plan A, by $20", "Plan A, by $40", "Plan B, by $20",
                    "Plan B, by $4"],
        "correct": "Plan A, by $20",
        "explanation": "<p><strong>A rejasi, $20 ga qimmat.</strong> A: 5(5) + 60 = 85. "
                       "B: 9(5) + 20 = 65. Farqi 85 − 65 = 20.</p>"
                       "<p>Diqqat: B ning qiyaligi kattaroq, lekin kichik <i>x</i> da "
                       "boshlangʻich toʻlov hal qiladi. Qiyalik faqat <b>oʻzgarish</b> "
                       "haqida gapiradi.</p>",
    },
    {
        "text": "<p>A model for a small business is <i>P</i> = 8<i>n</i> − 240, where "
                "<i>P</i> is profit in dollars and <i>n</i> is the number of items sold. "
                "Which of the following is the best interpretation of −240?</p>",
        "choices": ["The business loses $240 for each item sold.",
                    "The business has a loss of $240 when nothing is sold.",
                    "The business must sell 240 items.",
                    "Each item costs $240 to make."],
        "correct": "The business has a loss of $240 when nothing is sold.",
        "explanation": "<p><strong>Hech narsa sotilmaganda $240 zarar.</strong> n = 0 "
                       "boʻlganda P = −240 — bu doimiy xarajat.</p>"
                       "<p><strong>«For each item sold»</strong> — qiyalikning tili, "
                       "lekin qiyalik +8. Manfiy b maʼnoli boʻlishi mumkin: u "
                       "boshlangʻich xarajat.</p>",
    },
    {
        "text": "<p>A caterer charges $250 plus $18 for each guest. What is the total "
                "charge for 30 guests?</p>",
        "choices": ["$268", "$540", "$790", "$8,040"],
        "correct": "$790",
        "explanation": "<p><strong>$790.</strong> 18(30) + 250 = 540 + 250 = 790.</p>"
                       "<p><strong>$8,040</strong> — bir mehmonning narxini (268) "
                       "oʻttizga koʻpaytirgan javob; unda $250 oʻttiz marta "
                       "hisoblanadi. <strong>$540</strong> — $250 qoʻshilmagan.</p>",
    },
    {
        "text": "<p>A courier charges a base fee plus a fee for each kilometre. A 5-kilometre "
                "delivery costs $17 and a 12-kilometre delivery costs $31. How much does "
                "the courier charge per kilometre?</p>",
        "choices": ["$2", "$2.58", "$3.40", "$14"],
        "correct": "$2",
        "explanation": "<p><strong>$2.</strong> (31 − 17) ÷ (12 − 5) = 14 ÷ 7 = 2 — bu "
                       "qiyalik, yaʼni har bir kilometrning narxi.</p>"
                       "<p><strong>$3.40</strong> — 17 ni 5 ga boʻlgan javob, lekin "
                       "narx ichida boshlangʻich toʻlov ham bor. Shuning uchun har doim "
                       "<b>ikki nuqtaning ayirmasi</b> olinadi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "SAT-6 Practice: Calculating Slope from Two Points",
        "description": "20 ta SAT uslubidagi savol — qiyalik formulasi, manfiy "
                       "koordinatalar, nol va aniqlanmagan qiyalik, nomaʼlum koordinata.",
        "tutorial":    "SAT-6:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT6,
    },
    {
        "title":       "SAT-7 Practice: Slope-Intercept Form (y = mx + b) in Depth",
        "description": "20 ta SAT uslubidagi savol — m va b ni oʻqish, tenglama tuzish, "
                       "«y ga yechish» va kontekstdagi maʼnosi.",
        "tutorial":    "SAT-7:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT7,
    },
    {
        "title":       "SAT-8 Practice: Point-Slope Form and Standard Form",
        "description": "20 ta SAT uslubidagi savol — nuqta-qiyalik shakli, standart "
                       "shakl, kesishmalar va −A ÷ B qoidasi.",
        "tutorial":    "SAT-8:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT8,
    },
    {
        "title":       "SAT-9 Practice: Graphing Linear Equations Quickly",
        "description": "20 ta SAT uslubidagi savol — kesishmalar bilan chizish, tiklik, "
                       "choraklar va tenglamani grafikka moslash.",
        "tutorial":    "SAT-9:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT9,
    },
    {
        "title":       "SAT-10 Practice: Interpreting the Meaning of Slopes and Intercepts in Real-World Contexts",
        "description": "20 ta SAT uslubidagi savol — qiyalik «har bir birlik uchun», "
                       "kesishma «boshida», birliklar va «bittaga jami» tuzogʻi.",
        "tutorial":    "SAT-10:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT10,
    },
]
