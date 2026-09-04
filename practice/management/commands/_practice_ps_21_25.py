# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-21 … SAT-25.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context & interpretation ·
      15–16 trap-spotting · 17–18 Module 2 level · 19–20 word problems.

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA. Son: 3.5 va 1,200.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_21_25.py --master=prime \\
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
# SAT-21 — systems of linear inequalities
# =====================================================================

Q_SAT21 = [
    {
        "text": "<p>Is (0, 0) a solution to the system <i>y</i> ≥ <i>x</i> − 1 and "
                "<i>y</i> &lt; 4?</p>",
        "choices": ["Yes — both are true", "No — the first fails",
                    "No — the second fails", "No — both fail"],
        "correct": "Yes — both are true",
        "explanation": "<p><strong>Ha.</strong> 0 ≥ 0 − 1 rost ✓ va 0 &lt; 4 rost ✓.</p>"
                       "<p>Sistemada nuqta <b>ikkala</b> shartni ham qanoatlantirishi "
                       "kerak — bittasi yetmaydi.</p>",
    },
    {
        "text": "<p>Is (5, 3) a solution to the system <i>x</i> + <i>y</i> ≤ 6 and "
                "<i>y</i> ≥ 2?</p>",
        "choices": ["Yes — both are true", "No — the first fails",
                    "No — the second fails", "No — both fail"],
        "correct": "No — the first fails",
        "explanation": "<p><strong>Yoʻq — birinchisi buziladi.</strong> 5 + 3 = 8, va "
                       "8 ≤ 6 yolgʻon. Ikkinchisi esa rost (3 ≥ 2).</p>"
                       "<p>Bitta yolgʻon yetarli: nuqta darhol yechim boʻlmay "
                       "qoladi.</p>",
    },
    {
        "text": "<p>On a graph, what does the solution to a system of two inequalities "
                "look like?</p>",
        "choices": ["The region where the two shaded areas overlap",
                    "The two boundary lines only",
                    "Everything that is shaded by either inequality",
                    "The point where the two lines cross"],
        "correct": "The region where the two shaded areas overlap",
        "explanation": "<p><strong>Ikki shtrixlangan sohaning umumiy qismi.</strong> "
                       "Faqat u yerdagi nuqtalar ikkala shartni ham qanoatlantiradi.</p>"
                       "<p><strong>«Either»</strong> — bu «yoki» degani; sistema esa "
                       "«va» bilan bogʻlanadi.</p>",
    },
    {
        "text": "<p>Is (1, 3) a solution to the system <i>x</i> + <i>y</i> ≤ 6 and "
                "<i>y</i> ≥ 2?</p>",
        "choices": ["Yes — both are true", "No — the first fails",
                    "No — the second fails", "It lies on the boundary of both"],
        "correct": "Yes — both are true",
        "explanation": "<p><strong>Ha.</strong> 1 + 3 = 4 ≤ 6 ✓ va 3 ≥ 2 ✓.</p>"
                       "<p>Oldingi savol bilan solishtiring: oʻsha sistema, boshqa "
                       "nuqta — va javob butunlay boshqa.</p>",
    },
    {
        "text": "<p>Which point is a solution to the system <i>y</i> &gt; <i>x</i> − 2 "
                "and <i>y</i> &lt; 3?</p>",
        "choices": ["(−4, −7)", "(0, 0)", "(2, 4)", "(5, 1)"],
        "correct": "(0, 0)",
        "explanation": "<p><strong>(0, 0).</strong> 0 &gt; −2 ✓ va 0 &lt; 3 ✓.</p>"
                       "<p>Qolganlari: (5, 1) → 1 &gt; 3 ✗; (2, 4) → 4 &lt; 3 ✗; "
                       "(−4, −7) → −7 &gt; −6 ✗.</p>",
    },
    {
        "text": "<p>Which point is a solution to the system <i>y</i> ≤ 2<i>x</i> and "
                "<i>y</i> ≥ <i>x</i> − 1?</p>",
        "choices": ["(0, −2)", "(1, 3)", "(2, −1)", "(3, 4)"],
        "correct": "(3, 4)",
        "explanation": "<p><strong>(3, 4).</strong> 4 ≤ 6 ✓ va 4 ≥ 2 ✓.</p>"
                       "<p>(1, 3) → 3 ≤ 2 ✗; (0, −2) → −2 ≥ −1 ✗; (2, −1) → "
                       "−1 ≥ 1 ✗.</p>",
    },
    {
        "text": "<p>A team can spend at most $60 on shirts costing $4 each and caps "
                "costing $6 each, and must buy at least 10 items. Which system represents "
                "this?</p>",
        "choices": ["4<i>s</i> + 6<i>c</i> ≤ 60 and <i>s</i> + <i>c</i> ≥ 10",
                    "4<i>s</i> + 6<i>c</i> ≥ 60 and <i>s</i> + <i>c</i> ≤ 10",
                    "<i>s</i> + <i>c</i> ≤ 60 and 4<i>s</i> + 6<i>c</i> ≥ 10",
                    "4<i>s</i> + 6<i>c</i> ≤ 60 and <i>s</i> + <i>c</i> ≤ 10"],
        "correct": "4<i>s</i> + 6<i>c</i> ≤ 60 and <i>s</i> + <i>c</i> ≥ 10",
        "explanation": "<p><strong>4s + 6c ≤ 60 va s + c ≥ 10.</strong> «At most» pul "
                       "uchun ≤, «at least» soni uchun ≥.</p>"
                       "<p>Oxirgi variantda ikkala belgi ham ≤ — u kamida 10 ta olish "
                       "shartini butunlay yoʻqotadi.</p>",
    },
    {
        "text": "<p>Using that system, is buying 8 shirts and 3 caps possible?</p>",
        "choices": ["Yes", "No — it costs too much",
                    "No — there are too few items", "No — both conditions fail"],
        "correct": "Yes",
        "explanation": "<p><strong>Ha.</strong> Narxi 32 + 18 = $50 ≤ 60 ✓ va soni "
                       "11 ≥ 10 ✓.</p>"
                       "<p>Ikkala shart ham bajarildi, demak bu juftlik shtrixlangan "
                       "sohada yotadi.</p>",
    },
    {
        "text": "<p>Using the same system, is buying 10 shirts and 4 caps possible?</p>",
        "choices": ["Yes", "No — it costs too much",
                    "No — there are too few items", "No — both conditions fail"],
        "correct": "No — it costs too much",
        "explanation": "<p><strong>Yoʻq — juda qimmat.</strong> 40 + 24 = $64, bu "
                       "$60 dan oshadi.</p>"
                       "<p>Miqdor sharti bajarilgan (14 ≥ 10), lekin bitta shart "
                       "buzilsa yetarli.</p>",
    },
    {
        "text": "<p>Which point is <b>NOT</b> a solution to the system <i>x</i> ≥ 0 and "
                "<i>y</i> ≥ 0?</p>",
        "choices": ["(0, 0)", "(0, 5)", "(3, 2)", "(−1, 2)"],
        "correct": "(−1, 2)",
        "explanation": "<p><strong>(−1, 2).</strong> x = −1 manfiy, demak x ≥ 0 sharti "
                       "buziladi.</p>"
                       "<p>(0, 0) va (0, 5) chegarada yotadi, lekin belgi ≥ boʻlgani "
                       "uchun ular <b>yechim</b>.</p>",
    },
    {
        "text": "<p>In the model 4<i>s</i> + 6<i>c</i> ≤ 60, what does the 60 "
                "represent?</p>",
        "choices": ["The greatest amount of money that can be spent",
                    "The number of items that must be bought",
                    "The price of one shirt and one cap together",
                    "The least amount of money that must be spent"],
        "correct": "The greatest amount of money that can be spent",
        "explanation": "<p><strong>Sarflash mumkin boʻlgan eng koʻp pul.</strong> "
                       "≤ belgisi yuqori chegarani belgilaydi.</p>"
                       "<p><strong>«The least amount»</strong> — bu ≥ ning maʼnosi "
                       "boʻlardi; belgiga qarang.</p>",
    },
    {
        "text": "<p>Why do real-world systems of this kind usually also include the "
                "hidden conditions <i>s</i> ≥ 0 and <i>c</i> ≥ 0?</p>",
        "choices": ["Because you cannot buy a negative number of items",
                    "Because the budget must be positive",
                    "Because the graph must be bounded",
                    "Because the prices are whole numbers"],
        "correct": "Because you cannot buy a negative number of items",
        "explanation": "<p><strong>Manfiy sonda narsa sotib boʻlmaydi.</strong> "
                       "Matematik jihatdan sistema manfiy yechimlarni ham beradi, lekin "
                       "vaziyat ularni rad etadi.</p>"
                       "<p>Shuning uchun amaliy masalalarda javob har doim butun va "
                       "manfiy emas.</p>",
    },
    {
        "text": "<p>A club may spend at most $50 on tickets at $6 each and programmes at "
                "$4 each, and must buy at least 8 items. Is 5 tickets and 4 programmes "
                "possible?</p>",
        "choices": ["Yes", "No — it costs too much",
                    "No — there are too few items", "No — both conditions fail"],
        "correct": "Yes",
        "explanation": "<p><strong>Ha.</strong> Narxi 30 + 16 = $46 ≤ 50 ✓ va soni "
                       "9 ≥ 8 ✓.</p>"
                       "<p>Ikkala shartni ham alohida hisoblash — bu savol turining "
                       "yagona yechish usuli.</p>",
    },
    {
        "text": "<p>Using the same club system, is 3 tickets and 4 programmes "
                "possible?</p>",
        "choices": ["Yes", "No — it costs too much",
                    "No — there are too few items", "No — both conditions fail"],
        "correct": "No — there are too few items",
        "explanation": "<p><strong>Yoʻq — narsalar kam.</strong> Soni 3 + 4 = 7, va "
                       "kamida 8 ta kerak edi.</p>"
                       "<p>Narxi esa mos: 18 + 16 = $34 ≤ 50. Lekin bitta buzilgan "
                       "shart yetarli.</p>",
    },
    {
        "text": "<p>A point satisfies the first inequality of a system but not the "
                "second. Is it a solution to the system?</p>",
        "choices": ["Yes, partly", "Yes, if it lies on a boundary line",
                    "No", "It cannot be decided without a graph"],
        "correct": "No",
        "explanation": "<p><strong>Yoʻq.</strong> Sistemaning yechimi <b>ikkala</b> "
                       "shartni ham qanoatlantirishi kerak.</p>"
                       "<p>«Qisman yechim» degan narsa yoʻq — shuning uchun tekshirishda "
                       "birinchi yolgʻonda toʻxtash mumkin.</p>",
    },
    {
        "text": "<p>Which inequality correctly translates «the club must buy at least "
                "12 items»?</p>",
        "choices": ["<i>s</i> + <i>c</i> ≥ 12", "<i>s</i> + <i>c</i> ≤ 12",
                    "<i>s</i> + <i>c</i> &gt; 12", "<i>s</i> + <i>c</i> = 12"],
        "correct": "<i>s</i> + <i>c</i> ≥ 12",
        "explanation": "<p><strong>s + c ≥ 12.</strong> «At least» — kamida, va 12 ning "
                       "oʻzi ham mumkin.</p>"
                       "<p><strong>&gt; 12</strong> roppa-rosa 12 tani chiqarib "
                       "tashlaydi; <strong>≤ 12</strong> esa shartni butunlay "
                       "teskari qiladi.</p>",
    },
    {
        "text": "<p>How many points satisfy both <i>y</i> ≥ <i>x</i> and "
                "<i>y</i> ≤ <i>x</i>?</p>",
        "choices": ["None", "Exactly one",
                    "All the points on the line <i>y</i> = <i>x</i>", "All points"],
        "correct": "All the points on the line <i>y</i> = <i>x</i>",
        "explanation": "<p><strong>y = x chizigʻidagi barcha nuqtalar.</strong> "
                       "y ≥ x va y ≤ x bir vaqtda faqat y = x boʻlganda bajariladi.</p>"
                       "<p>Ikki yarim tekislikning kesishmasi bu safar sohaga emas, "
                       "<b>chiziqqa</b> qisqargan.</p>",
    },
    {
        "text": "<p>Which point is a solution to the system 2<i>x</i> + <i>y</i> ≤ 10 "
                "and <i>y</i> ≥ 2<i>x</i>?</p>",
        "choices": ["(0, −1)", "(1, 3)", "(4, 2)", "(5, 1)"],
        "correct": "(1, 3)",
        "explanation": "<p><strong>(1, 3).</strong> 2(1) + 3 = 5 ≤ 10 ✓ va "
                       "3 ≥ 2(1) = 2 ✓.</p>"
                       "<p>(4, 2) → 2 ≥ 8 ✗; (5, 1) → 11 ≤ 10 ✗; (0, −1) → "
                       "−1 ≥ 0 ✗.</p>",
    },
    {
        "text": "<p>A baker has at most 30 eggs and needs to make at least 6 cakes. Each "
                "cake takes 4 eggs and each loaf takes 2 eggs. If she makes 6 cakes, what "
                "is the greatest number of loaves she can also make?</p>",
        "choices": ["2", "3", "6", "15"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Olti tort 24 ta tuxum oladi, qolgani "
                       "30 − 24 = 6 ta. Har bir non 2 ta tuxum: 6 ÷ 2 = 3.</p>"
                       "<p><strong>15</strong> — tortlarni umuman hisobga olmagan javob "
                       "(30 ÷ 2).</p>",
    },
    {
        "text": "<p>A farmer has 20 hectares and wants to plant at least 8 hectares of "
                "wheat. Cotton needs 2 workers per hectare and wheat needs 1, and only "
                "30 workers are available. If he plants 8 hectares of wheat, what is the "
                "greatest number of hectares of cotton he can plant?</p>",
        "choices": ["8", "11", "12", "15"],
        "correct": "11",
        "explanation": "<p><strong>11.</strong> Bugʻdoy 8 ta ishchi oladi, qolgan "
                       "30 − 8 = 22 ta ishchi. Paxta gektariga 2 ta: 22 ÷ 2 = 11.</p>"
                       "<p><strong>12</strong> — yer boʻyicha chegara (20 − 8), lekin "
                       "ishchilar yetmaydi; ikkala shartni ham tekshirish kerak.</p>",
    },
]


# =====================================================================
# SAT-22 — absolute value inequalities
# =====================================================================

Q_SAT22 = [
    {
        "text": "<p>Solve: |<i>x</i>| &lt; 5</p>",
        "choices": ["−5 &lt; <i>x</i> &lt; 5", "<i>x</i> &lt; −5 or <i>x</i> &gt; 5",
                    "<i>x</i> &lt; 5", "<i>x</i> &gt; −5"],
        "correct": "−5 &lt; <i>x</i> &lt; 5",
        "explanation": "<p><strong>−5 &lt; x &lt; 5.</strong> «Kichik» — noldan yaqin, "
                       "demak bitta oraliq.</p>"
                       "<p>Yodlash: <b>less → between</b>. Ikki tomonli javob "
                       "«katta»ning shakli.</p>",
    },
    {
        "text": "<p>Solve: |<i>x</i>| ≥ 3</p>",
        "choices": ["−3 ≤ <i>x</i> ≤ 3", "<i>x</i> ≤ −3 or <i>x</i> ≥ 3",
                    "<i>x</i> ≥ 3", "<i>x</i> ≥ −3"],
        "correct": "<i>x</i> ≤ −3 or <i>x</i> ≥ 3",
        "explanation": "<p><strong>x ≤ −3 yoki x ≥ 3.</strong> «Katta» — noldan uzoq, "
                       "demak ikki tomon.</p>"
                       "<p><strong>x ≥ 3</strong> — yarim javob: manfiy tomon "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>Solve: |<i>x</i> − 3| &lt; 5</p>",
        "choices": ["−2 &lt; <i>x</i> &lt; 8", "−5 &lt; <i>x</i> &lt; 5",
                    "<i>x</i> &lt; −2 or <i>x</i> &gt; 8", "2 &lt; <i>x</i> &lt; 8"],
        "correct": "−2 &lt; <i>x</i> &lt; 8",
        "explanation": "<p><strong>−2 &lt; x &lt; 8.</strong> −5 &lt; x − 3 &lt; 5, "
                       "uchala qismga 3 ni qoʻshamiz.</p>"
                       "<p><strong>−5 &lt; x &lt; 5</strong> — 3 ni qoʻshish "
                       "unutilgan; markaz 0 emas, <b>3</b>.</p>",
    },
    {
        "text": "<p>Solve: |<i>x</i> + 2| &lt; 6</p>",
        "choices": ["−8 &lt; <i>x</i> &lt; 4", "−6 &lt; <i>x</i> &lt; 6",
                    "−4 &lt; <i>x</i> &lt; 8", "<i>x</i> &lt; −8 or <i>x</i> &gt; 4"],
        "correct": "−8 &lt; <i>x</i> &lt; 4",
        "explanation": "<p><strong>−8 &lt; x &lt; 4.</strong> −6 &lt; x + 2 &lt; 6, "
                       "uchala qismdan 2 ni ayiramiz.</p>"
                       "<p><strong>−4 &lt; x &lt; 8</strong> — ayirish oʻrniga qoʻshgan "
                       "javob. Markaz −2, chunki x + 2 nolga aylanadigan son shu.</p>",
    },
    {
        "text": "<p>Solve: |<i>x</i> − 4| ≤ 6</p>",
        "choices": ["−10 ≤ <i>x</i> ≤ 10", "−2 ≤ <i>x</i> ≤ 10",
                    "<i>x</i> ≤ −2 or <i>x</i> ≥ 10", "2 ≤ <i>x</i> ≤ 6"],
        "correct": "−2 ≤ <i>x</i> ≤ 10",
        "explanation": "<p><strong>−2 ≤ x ≤ 10.</strong> Markaz 4, ruxsat etilgan "
                       "uzoqlik 6 — chegaralar 4 − 6 va 4 + 6.</p>"
                       "<p>Tekshiruv: x = 0 → |−4| = 4 ≤ 6 ✓, va 0 haqiqatan "
                       "oraliqda.</p>",
    },
    {
        "text": "<p>Solve: |2<i>x</i> + 1| ≥ 7</p>",
        "choices": ["−4 ≤ <i>x</i> ≤ 3", "<i>x</i> ≤ −4 or <i>x</i> ≥ 3",
                    "<i>x</i> ≤ −3 or <i>x</i> ≥ 4", "<i>x</i> ≥ 3"],
        "correct": "<i>x</i> ≤ −4 or <i>x</i> ≥ 3",
        "explanation": "<p><strong>x ≤ −4 yoki x ≥ 3.</strong> 2x + 1 ≥ 7 → x ≥ 3; "
                       "2x + 1 ≤ −7 → 2x ≤ −8 → x ≤ −4.</p>"
                       "<p>Ikkinchi holda belgi ham agʻdariladi — bu qadam koʻpincha "
                       "tushib qoladi.</p>",
    },
    {
        "text": "<p>Solve: |2<i>x</i> − 5| &gt; 3</p>",
        "choices": ["1 &lt; <i>x</i> &lt; 4", "<i>x</i> &lt; 1 or <i>x</i> &gt; 4",
                    "<i>x</i> &lt; −4 or <i>x</i> &gt; 1", "<i>x</i> &gt; 4"],
        "correct": "<i>x</i> &lt; 1 or <i>x</i> &gt; 4",
        "explanation": "<p><strong>x &lt; 1 yoki x &gt; 4.</strong> 2x − 5 &gt; 3 → "
                       "x &gt; 4; 2x − 5 &lt; −3 → x &lt; 1.</p>"
                       "<p><strong>x &gt; 4</strong> — faqat bitta tomon. «Katta» "
                       "modul har doim ikkita qismdan iborat.</p>",
    },
    {
        "text": "<p>Solve: 3|<i>x</i>| + 2 &lt; 14</p>",
        "choices": ["−4 &lt; <i>x</i> &lt; 4", "−12 &lt; <i>x</i> &lt; 12",
                    "<i>x</i> &lt; −4 or <i>x</i> &gt; 4", "<i>x</i> &lt; 4"],
        "correct": "−4 &lt; <i>x</i> &lt; 4",
        "explanation": "<p><strong>−4 &lt; x &lt; 4.</strong> Avval izolyatsiya: "
                       "3|x| &lt; 12 → |x| &lt; 4, keyin «kichik» qoidasi.</p>"
                       "<p><strong>−12 &lt; x &lt; 12</strong> — 3 ga boʻlish "
                       "unutilgan javob.</p>",
    },
    {
        "text": "<p>Solve: 2|<i>x</i>| − 1 &gt; 9</p>",
        "choices": ["−5 &lt; <i>x</i> &lt; 5", "<i>x</i> &lt; −5 or <i>x</i> &gt; 5",
                    "<i>x</i> &gt; 5", "<i>x</i> &lt; −4 or <i>x</i> &gt; 4"],
        "correct": "<i>x</i> &lt; −5 or <i>x</i> &gt; 5",
        "explanation": "<p><strong>x &lt; −5 yoki x &gt; 5.</strong> 2|x| &gt; 10 → "
                       "|x| &gt; 5, keyin «katta» qoidasi.</p>"
                       "<p><strong>x &lt; −4 or x &gt; 4</strong> — 1 ni qoʻshish "
                       "oʻrniga ayirgan javob.</p>",
    },
    {
        "text": "<p>How many solutions does |<i>x</i>| &lt; −2 have?</p>",
        "choices": ["None", "One", "Two", "Infinitely many"],
        "correct": "None",
        "explanation": "<p><strong>Bittasi ham yoʻq.</strong> Modul — uzoqlik, u "
                       "hech qachon manfiy sondan kichik boʻlolmaydi.</p>"
                       "<p>Bu savolda hech narsa hisoblash kerak emas: oʻng "
                       "tomonning ishorasiga qarash yetadi.</p>",
    },
    {
        "text": "<p>A bottle is accepted if its volume differs from 500 millilitres by no "
                "more than 8 millilitres. Which inequality describes the accepted "
                "volumes <i>v</i>?</p>",
        "choices": ["|<i>v</i> − 500| ≤ 8", "|<i>v</i> − 8| ≤ 500",
                    "|<i>v</i> − 500| &gt; 8", "|<i>v</i> + 500| ≤ 8"],
        "correct": "|<i>v</i> − 500| ≤ 8",
        "explanation": "<p><strong>|v − 500| ≤ 8.</strong> Modul ichida <b>markaz</b> "
                       "ayriladi (500), oʻng tomonda esa ruxsat etilgan uzoqlik (8).</p>"
                       "<p><strong>&gt; 8</strong> — rad etiladigan shishalarni "
                       "tasvirlaydi, qabul qilinadiganlarini emas.</p>",
    },
    {
        "text": "<p>Using |<i>v</i> − 500| ≤ 8, what is the range of accepted "
                "volumes?</p>",
        "choices": ["492 ≤ <i>v</i> ≤ 508", "500 ≤ <i>v</i> ≤ 508",
                    "<i>v</i> ≤ 492 or <i>v</i> ≥ 508", "8 ≤ <i>v</i> ≤ 500"],
        "correct": "492 ≤ <i>v</i> ≤ 508",
        "explanation": "<p><strong>492 ≤ v ≤ 508.</strong> Markaz 500, ikki tomonga "
                       "8 dan.</p>"
                       "<p><strong>v ≤ 492 or v ≥ 508</strong> — aynan rad etiladigan "
                       "shishalar; belgi teskari oʻqilgan.</p>",
    },
    {
        "text": "<p>A thermostat keeps a room «within 2 degrees of 21 degrees». Which "
                "inequality says this?</p>",
        "choices": ["|<i>T</i> − 21| ≤ 2", "|<i>T</i> − 2| ≤ 21",
                    "|<i>T</i> + 21| ≤ 2", "|<i>T</i> − 21| ≥ 2"],
        "correct": "|<i>T</i> − 21| ≤ 2",
        "explanation": "<p><strong>|T − 21| ≤ 2.</strong> «Within 2 of 21» — 21 dan "
                       "ikki darajadan uzoq emas.</p>"
                       "<p>Ruxsat etilgan harorat: 19 dan 23 gacha.</p>",
    },
    {
        "text": "<p>What does |<i>x</i> − 7| &gt; 4 mean in words?</p>",
        "choices": ["x is more than 4 away from 7", "x is less than 4 away from 7",
                    "x is more than 7 away from 4", "x is exactly 4 away from 7"],
        "correct": "x is more than 4 away from 7",
        "explanation": "<p><strong>x soni 7 dan 4 dan koʻproq uzoqda.</strong> Modul "
                       "ichidagi son — markaz, oʻng tomondagi — uzoqlik.</p>"
                       "<p>Yechim: x &lt; 3 yoki x &gt; 11 — ikki tomon.</p>",
    },
    {
        "text": "<p>A student writes the solution of |<i>x</i>| &gt; 6 as "
                "6 &lt; <i>x</i> &lt; −6. What is wrong?</p>",
        "choices": ["Nothing — it is correct",
                    "No number is both greater than 6 and less than −6",
                    "The signs should be ≤ and ≥",
                    "The 6 should be −6 on both sides"],
        "correct": "No number is both greater than 6 and less than −6",
        "explanation": "<p><strong>Hech bir son bir vaqtda 6 dan katta va −6 dan "
                       "kichik boʻlolmaydi.</strong> «Katta» javobi zanjir shaklida "
                       "yozilmaydi.</p>"
                       "<p>Toʻgʻrisi: x &lt; −6 <b>yoki</b> x &gt; 6 — ikki alohida "
                       "qism.</p>",
    },
    {
        "text": "<p>Which is the solution of |<i>x</i> + 1| ≤ 0?</p>",
        "choices": ["No solution", "<i>x</i> = −1", "−1 ≤ <i>x</i> ≤ 1",
                    "All real numbers"],
        "correct": "<i>x</i> = −1",
        "explanation": "<p><strong>x = −1.</strong> Modul hech qachon manfiy emas, "
                       "shuning uchun «≤ 0» faqat <b>aynan 0</b> boʻlgandagina "
                       "bajariladi.</p>"
                       "<p>x + 1 = 0 → x = −1. Bu SAT'ning sevimli «bitta yechim» "
                       "tuzogʻi.</p>",
    },
    {
        "text": "<p>Solve: |3<i>x</i> − 6| &lt; 9</p>",
        "choices": ["−1 &lt; <i>x</i> &lt; 5", "−3 &lt; <i>x</i> &lt; 3",
                    "<i>x</i> &lt; −1 or <i>x</i> &gt; 5", "1 &lt; <i>x</i> &lt; 5"],
        "correct": "−1 &lt; <i>x</i> &lt; 5",
        "explanation": "<p><strong>−1 &lt; x &lt; 5.</strong> −9 &lt; 3x − 6 &lt; 9 → "
                       "−3 &lt; 3x &lt; 15 → −1 &lt; x &lt; 5.</p>"
                       "<p>Uchala qismga bir vaqtda amal qoʻllanadi: avval 6 ni "
                       "qoʻshdik, keyin 3 ga boʻldik.</p>",
    },
    {
        "text": "<p>Solve: |4 − <i>x</i>| ≥ 5</p>",
        "choices": ["−1 ≤ <i>x</i> ≤ 9", "<i>x</i> ≤ −1 or <i>x</i> ≥ 9",
                    "<i>x</i> ≤ 1 or <i>x</i> ≥ 9", "<i>x</i> ≥ 9"],
        "correct": "<i>x</i> ≤ −1 or <i>x</i> ≥ 9",
        "explanation": "<p><strong>x ≤ −1 yoki x ≥ 9.</strong> 4 − x ≥ 5 → −x ≥ 1 → "
                       "x ≤ −1 (belgi agʻdarildi); 4 − x ≤ −5 → −x ≤ −9 → x ≥ 9.</p>"
                       "<p>Bu yerda ikki agʻdarish bor: modulniki va manfiy "
                       "koeffitsientniki.</p>",
    },
    {
        "text": "<p>A machine cuts rods to 60 centimetres and rejects any rod that "
                "differs from that by more than 0.5 centimetres. A rod measures "
                "60.4 centimetres. Is it accepted?</p>",
        "choices": ["Yes — the difference is 0.4, which is not more than 0.5",
                    "No — it is longer than 60",
                    "No — the difference is more than 0.5",
                    "It is exactly on the limit"],
        "correct": "Yes — the difference is 0.4, which is not more than 0.5",
        "explanation": "<p><strong>Ha.</strong> |60.4 − 60| = 0.4, va 0.4 &gt; 0.5 "
                       "yolgʻon — demak sterjen rad etilmaydi.</p>"
                       "<p>Uzunroq boʻlishi oʻzi ayb emas: qoida <b>uzoqlikni</b> "
                       "oʻlchaydi, tomonni emas.</p>",
    },
    {
        "text": "<p>A runner's time must be within 3 seconds of the team average of "
                "52 seconds to qualify. Which times qualify?</p>",
        "choices": ["49 to 55 seconds", "52 to 55 seconds",
                    "Under 49 or over 55 seconds", "3 to 52 seconds"],
        "correct": "49 to 55 seconds",
        "explanation": "<p><strong>49 dan 55 gacha.</strong> |t − 52| ≤ 3, demak "
                       "52 − 3 = 49 va 52 + 3 = 55.</p>"
                       "<p><strong>«Under 49 or over 55»</strong> — aynan "
                       "<b>saralanmaydigan</b> vaqtlar; «within» oraliqni "
                       "bildiradi.</p>",
    },
]


# =====================================================================
# SAT-23 — laws of exponents
# =====================================================================

Q_SAT23 = [
    {
        "text": "<p>Simplify: <i>x</i><sup>4</sup> · <i>x</i><sup>6</sup></p>",
        "choices": ["<i>x</i><sup>2</sup>", "<i>x</i><sup>10</sup>",
                    "<i>x</i><sup>24</sup>", "2<i>x</i><sup>10</sup>"],
        "correct": "<i>x</i><sup>10</sup>",
        "explanation": "<p><strong>x<sup>10</sup>.</strong> Bir xil asos "
                       "koʻpaytirilganda koʻrsatkichlar qoʻshiladi: 4 + 6.</p>"
                       "<p><strong>x<sup>24</sup></strong> — koʻrsatkichlar "
                       "koʻpaytirilgan; bu faqat qavs boʻlganda toʻgʻri.</p>",
    },
    {
        "text": "<p>Simplify: <i>y</i><sup>9</sup> ÷ <i>y</i><sup>4</sup></p>",
        "choices": ["<i>y</i><sup>2</sup>", "<i>y</i><sup>5</sup>",
                    "<i>y</i><sup>13</sup>", "<i>y</i><sup>36</sup>"],
        "correct": "<i>y</i><sup>5</sup>",
        "explanation": "<p><strong>y<sup>5</sup>.</strong> Boʻlganda koʻrsatkichlar "
                       "ayriladi: 9 − 4.</p>"
                       "<p><strong>y<sup>13</sup></strong> — qoʻshgan javob; "
                       "boʻlish har doim ayirish.</p>",
    },
    {
        "text": "<p>Simplify: (<i>x</i><sup>4</sup>)<sup>3</sup></p>",
        "choices": ["<i>x</i><sup>7</sup>", "<i>x</i><sup>12</sup>",
                    "<i>x</i><sup>64</sup>", "3<i>x</i><sup>4</sup>"],
        "correct": "<i>x</i><sup>12</sup>",
        "explanation": "<p><strong>x<sup>12</sup>.</strong> Qavs bor — demak "
                       "koʻrsatkichlar koʻpaytiriladi: 4 × 3.</p>"
                       "<p><strong>x<sup>7</sup></strong> — qoʻshgan javob. Qavs "
                       "boʻlsa koʻpaytiring, boʻlmasa qoʻshing.</p>",
    },
    {
        "text": "<p>What is the value of 3<sup>2</sup> · 3<sup>3</sup>?</p>",
        "choices": ["36", "81", "243", "729"],
        "correct": "243",
        "explanation": "<p><strong>243.</strong> 3<sup>2+3</sup> = 3<sup>5</sup> = "
                       "243.</p>"
                       "<p><strong>729</strong> — 3<sup>6</sup>, yaʼni "
                       "koʻrsatkichlarni koʻpaytirgan javob; <strong>81</strong> — "
                       "3<sup>4</sup>.</p>",
    },
    {
        "text": "<p>Simplify: (2<i>x</i><sup>2</sup>)<sup>3</sup></p>",
        "choices": ["2<i>x</i><sup>5</sup>", "2<i>x</i><sup>6</sup>",
                    "6<i>x</i><sup>6</sup>", "8<i>x</i><sup>6</sup>"],
        "correct": "8<i>x</i><sup>6</sup>",
        "explanation": "<p><strong>8x<sup>6</sup>.</strong> Qavs ichidagi <b>ikkala</b> "
                       "koʻpaytuvchi ham kubga koʻtariladi: 2<sup>3</sup> = 8 va "
                       "x<sup>6</sup>.</p>"
                       "<p><strong>2x<sup>6</sup></strong> — koeffitsient tegilmagan; "
                       "<strong>6x<sup>6</sup></strong> — 2 × 3 hisoblangan.</p>",
    },
    {
        "text": "<p>Simplify: (3<i>x</i><sup>2</sup><i>y</i>)<sup>2</sup></p>",
        "choices": ["3<i>x</i><sup>4</sup><i>y</i><sup>2</sup>",
                    "6<i>x</i><sup>4</sup><i>y</i><sup>2</sup>",
                    "9<i>x</i><sup>4</sup><i>y</i><sup>2</sup>",
                    "9<i>x</i><sup>4</sup><i>y</i>"],
        "correct": "9<i>x</i><sup>4</sup><i>y</i><sup>2</sup>",
        "explanation": "<p><strong>9x<sup>4</sup>y<sup>2</sup>.</strong> Uchala "
                       "koʻpaytuvchi ham kvadratga koʻtariladi.</p>"
                       "<p><strong>9x<sup>4</sup>y</strong> — <i>y</i> unutilgan: "
                       "koʻrsatkichi koʻrinmasa u yerda 1 turadi, va 1 × 2 = 2.</p>",
    },
    {
        "text": "<p>Simplify: (2<i>x</i><sup>3</sup>)<sup>4</sup></p>",
        "choices": ["8<i>x</i><sup>7</sup>", "8<i>x</i><sup>12</sup>",
                    "16<i>x</i><sup>7</sup>", "16<i>x</i><sup>12</sup>"],
        "correct": "16<i>x</i><sup>12</sup>",
        "explanation": "<p><strong>16x<sup>12</sup>.</strong> 2<sup>4</sup> = 16 va "
                       "3 × 4 = 12.</p>"
                       "<p><strong>8x<sup>12</sup></strong> — 2<sup>3</sup> "
                       "hisoblangan; <strong>16x<sup>7</sup></strong> — "
                       "koʻrsatkichlar qoʻshilgan.</p>",
    },
    {
        "text": "<p>For <i>x</i> &gt; 0, simplify: (<i>x</i><sup>5</sup> · "
                "<i>x</i><sup>3</sup>) ÷ <i>x</i><sup>2</sup></p>",
        "choices": ["<i>x</i><sup>6</sup>", "<i>x</i><sup>10</sup>",
                    "<i>x</i><sup>13</sup>", "<i>x</i><sup>15</sup>"],
        "correct": "<i>x</i><sup>6</sup>",
        "explanation": "<p><strong>x<sup>6</sup>.</strong> Avval 5 + 3 = 8, keyin "
                       "8 − 2 = 6.</p>"
                       "<p><strong>x<sup>10</sup></strong> — boʻlishda qoʻshgan; "
                       "<strong>x<sup>15</sup></strong> — 5 × 3 qilgan javob.</p>",
    },
    {
        "text": "<p>For <i>x</i> &gt; 0, simplify: (<i>x</i><sup>6</sup>)<sup>2</sup> ÷ "
                "<i>x</i><sup>4</sup></p>",
        "choices": ["<i>x</i><sup>3</sup>", "<i>x</i><sup>8</sup>",
                    "<i>x</i><sup>12</sup>", "<i>x</i><sup>16</sup>"],
        "correct": "<i>x</i><sup>8</sup>",
        "explanation": "<p><strong>x<sup>8</sup>.</strong> Avval qavs: 6 × 2 = 12, "
                       "keyin boʻlish: 12 − 4 = 8.</p>"
                       "<p><strong>x<sup>16</sup></strong> — boʻlishda qoʻshgan "
                       "javob; amallar tartibiga eʼtibor bering.</p>",
    },
    {
        "text": "<p>What is the value of 5<sup>3</sup> · 5<sup>2</sup> ÷ "
                "5<sup>4</sup>?</p>",
        "choices": ["1", "5", "25", "125"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Koʻrsatkichlar: 3 + 2 − 4 = 1, demak "
                       "5<sup>1</sup> = 5.</p>"
                       "<p><strong>25</strong> — 5<sup>2</sup>, koʻrsatkichni "
                       "notoʻgʻri hisoblagan javob.</p>",
    },
    {
        "text": "<p>A single bacterium doubles every hour. How many bacteria are there "
                "after 10 hours?</p>",
        "choices": ["20", "100", "512", "1,024"],
        "correct": "1,024",
        "explanation": "<p><strong>1,024.</strong> Har soat ikkiga koʻpayadi: "
                       "2<sup>10</sup> = 1,024.</p>"
                       "<p><strong>512</strong> — 2<sup>9</sup>, yaʼni bir soat kam; "
                       "<strong>20</strong> — 2 × 10, koʻpaytirish emas, "
                       "<b>takroriy</b> koʻpaytirish boʻlishi kerak edi.</p>",
    },
    {
        "text": "<p>In the expression 3<i>x</i><sup>2</sup>, what is squared?</p>",
        "choices": ["Only the x", "Only the 3", "Both the 3 and the x",
                    "The whole expression"],
        "correct": "Only the x",
        "explanation": "<p><strong>Faqat x.</strong> Koʻrsatkich oʻzi turgan belgiga "
                       "tegishli, qoʻshnisiga emas.</p>"
                       "<p>(3x)<sup>2</sup> boʻlganda esa qavs ikkalasini ham qamrab "
                       "olardi va 9x<sup>2</sup> chiqardi.</p>",
    },
    {
        "text": "<p>What is the value of (10<sup>3</sup>)<sup>2</sup>?</p>",
        "choices": ["10<sup>5</sup>", "10<sup>6</sup>", "10<sup>9</sup>",
                    "20<sup>3</sup>"],
        "correct": "10<sup>6</sup>",
        "explanation": "<p><strong>10<sup>6</sup></strong> (bir million). Qavs bor — "
                       "koʻrsatkichlar koʻpaytiriladi: 3 × 2.</p>"
                       "<p><strong>10<sup>5</sup></strong> — qoʻshgan javob. Bu farq "
                       "bir million bilan yuz mingni ajratadi.</p>",
    },
    {
        "text": "<p>A square has sides of length 3<i>x</i><sup>2</sup>. What is its "
                "area?</p>",
        "choices": ["3<i>x</i><sup>4</sup>", "6<i>x</i><sup>2</sup>",
                    "9<i>x</i><sup>2</sup>", "9<i>x</i><sup>4</sup>"],
        "correct": "9<i>x</i><sup>4</sup>",
        "explanation": "<p><strong>9x<sup>4</sup>.</strong> Yuza = tomon × tomon = "
                       "(3x<sup>2</sup>)<sup>2</sup>, demak 3<sup>2</sup> = 9 va "
                       "x<sup>4</sup>.</p>"
                       "<p><strong>6x<sup>2</sup></strong> — tomonni ikkiga "
                       "koʻpaytirgan javob; bu perimetrga ham toʻgʻri kelmaydi.</p>",
    },
    {
        "text": "<p>Which of the following is equal to <i>x</i><sup>3</sup> · "
                "<i>x</i><sup>5</sup>?</p>",
        "choices": ["<i>x</i><sup>8</sup>", "<i>x</i><sup>15</sup>",
                    "2<i>x</i><sup>8</sup>", "<i>x</i><sup>2</sup>"],
        "correct": "<i>x</i><sup>8</sup>",
        "explanation": "<p><strong>x<sup>8</sup>.</strong> Uchta x va beshta x — jami "
                       "sakkizta.</p>"
                       "<p><strong>x<sup>15</sup></strong> — eng koʻp uchraydigan "
                       "tuzoq: koʻrsatkichlar faqat <b>qavs</b> boʻlganda "
                       "koʻpaytiriladi.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to (3<i>x</i>)<sup>2</sup>?</p>",
        "choices": ["3<i>x</i><sup>2</sup>", "6<i>x</i><sup>2</sup>",
                    "9<i>x</i><sup>2</sup>", "9<i>x</i>"],
        "correct": "9<i>x</i><sup>2</sup>",
        "explanation": "<p><strong>9x<sup>2</sup>.</strong> Qavs 3 ni ham qamrab "
                       "oladi: 3<sup>2</sup> = 9.</p>"
                       "<p><strong>3x<sup>2</sup></strong> — qavssiz yozuvning "
                       "javobi. Bu ikkisi butunlay boshqa ifoda: x = 2 da 36 va 12.</p>",
    },
    {
        "text": "<p>For <i>x</i> &gt; 0 and <i>y</i> &gt; 0, simplify: "
                "(4<i>x</i><sup>3</sup><i>y</i><sup>2</sup>)<sup>2</sup> ÷ "
                "(2<i>xy</i>)</p>",
        "choices": ["4<i>x</i><sup>5</sup><i>y</i><sup>3</sup>",
                    "8<i>x</i><sup>5</sup><i>y</i><sup>3</sup>",
                    "8<i>x</i><sup>6</sup><i>y</i><sup>4</sup>",
                    "16<i>x</i><sup>5</sup><i>y</i><sup>3</sup>"],
        "correct": "8<i>x</i><sup>5</sup><i>y</i><sup>3</sup>",
        "explanation": "<p><strong>8x<sup>5</sup>y<sup>3</sup>.</strong> Avval qavs: "
                       "16x<sup>6</sup>y<sup>4</sup>. Keyin boʻlish: 16 ÷ 2 = 8, "
                       "6 − 1 = 5, 4 − 1 = 3.</p>"
                       "<p><strong>16x<sup>5</sup>y<sup>3</sup></strong> — "
                       "koeffitsient boʻlinmagan javob.</p>",
    },
    {
        "text": "<p>If (<i>x</i><sup><i>a</i></sup>)<sup>3</sup> = "
                "<i>x</i><sup>12</sup>, what is the value of <i>a</i>?</p>",
        "choices": ["3", "4", "9", "36"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Qavs koʻrsatkichlarni koʻpaytiradi: "
                       "3a = 12, demak a = 4.</p>"
                       "<p><strong>9</strong> — ayirgan javob (12 − 3); qavs har doim "
                       "koʻpaytiradi.</p>",
    },
    {
        "text": "<p>The side of a square is doubled. What happens to its area?</p>",
        "choices": ["It doubles", "It triples", "It is multiplied by four",
                    "It stays the same"],
        "correct": "It is multiplied by four",
        "explanation": "<p><strong>Toʻrt barobar ortadi.</strong> Yangi yuza "
                       "(2s)<sup>2</sup> = 4s<sup>2</sup>.</p>"
                       "<p>Sabab — qavs: koeffitsient 2 ham kvadratga koʻtariladi. "
                       "SAT bu gʻoyani geometriyada ham soʻraydi.</p>",
    },
    {
        "text": "<p>A sheet of paper is folded in half 8 times. How many layers of paper "
                "are there?</p>",
        "choices": ["16", "64", "128", "256"],
        "correct": "256",
        "explanation": "<p><strong>256.</strong> Har bukish qatlamlar sonini ikkiga "
                       "koʻpaytiradi: 2<sup>8</sup> = 256.</p>"
                       "<p><strong>16</strong> — 8 × 2, yaʼni takroriy koʻpaytirish "
                       "oʻrniga oddiy koʻpaytirish qilgan javob.</p>",
    },
]


# =====================================================================
# SAT-24 — negative and fractional exponents
# =====================================================================

Q_SAT24 = [
    {
        "text": "<p>What is the value of 3<sup>−2</sup>?</p>",
        "choices": ["−9", "−6", "1/9", "9"],
        "correct": "1/9",
        "explanation": "<p><strong>1/9.</strong> Manfiy koʻrsatkich sonni maxrajga "
                       "tushiradi: 1 ÷ 3<sup>2</sup>.</p>"
                       "<p><strong>−9</strong> — eng koʻp uchraydigan tuzoq: minus "
                       "ishorani emas, <b>oʻrinni</b> oʻzgartiradi.</p>",
    },
    {
        "text": "<p>What is the value of 5<sup>0</sup>?</p>",
        "choices": ["0", "1", "5", "It is undefined"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> Har qanday son (0 dan tashqari) nol "
                       "darajada 1 ga teng.</p>"
                       "<p>Sabab: 5<sup>3</sup> ÷ 5<sup>3</sup> = 1, va qonun "
                       "boʻyicha u 5<sup>0</sup>.</p>",
    },
    {
        "text": "<p>What is the value of 25<sup>1/2</sup>?</p>",
        "choices": ["5", "12.5", "50", "625"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 1/2 koʻrsatkichi kvadrat ildizni "
                       "bildiradi: √25 = 5.</p>"
                       "<p><strong>12.5</strong> — 25 ni ikkiga boʻlgan javob; kasr "
                       "koʻrsatkich boʻlish emas, <b>ildiz</b>.</p>",
    },
    {
        "text": "<p>What is the value of 27<sup>1/3</sup>?</p>",
        "choices": ["3", "9", "13.5", "81"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Kub ildiz: 3 × 3 × 3 = 27.</p>"
                       "<p><strong>9</strong> — 27 ni uchga boʻlgan javob; maxraj "
                       "ildizning <b>darajasini</b> bildiradi.</p>",
    },
    {
        "text": "<p>What is the value of 8<sup>2/3</sup>?</p>",
        "choices": ["2", "4", "16", "512"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Avval kub ildiz: ∛8 = 2, keyin "
                       "kvadrat: 2<sup>2</sup> = 4.</p>"
                       "<p><strong>2</strong> — faqat ildiz olingan; "
                       "<strong>512</strong> — 8<sup>3</sup>, kasr butunlay teskari "
                       "oʻqilgan.</p>",
    },
    {
        "text": "<p>What is the value of 16<sup>3/4</sup>?</p>",
        "choices": ["8", "12", "48", "64"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Toʻrtinchi darajali ildiz: "
                       "<sup>4</sup>√16 = 2, keyin 2<sup>3</sup> = 8.</p>"
                       "<p><strong>64</strong> — kvadrat ildiz olib (4), keyin kubga "
                       "koʻtargan javob; maxraj 4 edi, 2 emas.</p>",
    },
    {
        "text": "<p>What is the value of 9<sup>−1/2</sup>?</p>",
        "choices": ["−3", "−1/3", "1/3", "3"],
        "correct": "1/3",
        "explanation": "<p><strong>1/3.</strong> Avval ildiz: √9 = 3, keyin minus uni "
                       "maxrajga tushiradi.</p>"
                       "<p><strong>−3</strong> — minusni ishora deb oʻqigan javob. "
                       "Natija musbat va birdan kichik.</p>",
    },
    {
        "text": "<p>What is the value of 32<sup>1/5</sup>?</p>",
        "choices": ["2", "5", "6.4", "16"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Beshinchi darajali ildiz: "
                       "2<sup>5</sup> = 32.</p>"
                       "<p><strong>6.4</strong> — 32 ni beshga boʻlgan javob; kasr "
                       "koʻrsatkich hech qachon boʻlish emas.</p>",
    },
    {
        "text": "<p>What is the value of (1/2)<sup>−2</sup>?</p>",
        "choices": ["−4", "1/4", "2", "4"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Manfiy koʻrsatkich kasrni agʻdaradi: "
                       "(2/1)<sup>2</sup> = 4.</p>"
                       "<p><strong>1/4</strong> — minusni eʼtiborsiz qoldirgan "
                       "javob. Bu qoida SAT'da tez-tez chiqadi.</p>",
    },
    {
        "text": "<p>What is the value of 27<sup>−2/3</sup>?</p>",
        "choices": ["−9", "1/9", "1/3", "9"],
        "correct": "1/9",
        "explanation": "<p><strong>1/9.</strong> ∛27 = 3, keyin 3<sup>2</sup> = 9, "
                       "va minus uni maxrajga tushiradi.</p>"
                       "<p>Tartib muhim: <b>ildiz → daraja → minus</b>. Minusni "
                       "oxirida qoʻllang.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to √<i>x</i>?</p>",
        "choices": ["<i>x</i><sup>1/2</sup>", "<i>x</i><sup>2</sup>",
                    "<i>x</i><sup>−2</sup>", "2<i>x</i>"],
        "correct": "<i>x</i><sup>1/2</sup>",
        "explanation": "<p><strong>x<sup>1/2</sup>.</strong> Kvadrat ildiz — 1/2 "
                       "koʻrsatkichining boshqa yozuvi.</p>"
                       "<p>Bu ikki yozuv butunlay teng kuchli; SAT ikkalasini ham "
                       "ishlatadi va javoblarni bir shakldan ikkinchisiga "
                       "oʻtkazishni talab qiladi.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 1 ÷ <i>x</i><sup>3</sup>?</p>",
        "choices": ["<i>x</i><sup>−3</sup>", "<i>x</i><sup>3</sup>",
                    "<i>x</i><sup>1/3</sup>", "−<i>x</i><sup>3</sup>"],
        "correct": "<i>x</i><sup>−3</sup>",
        "explanation": "<p><strong>x<sup>−3</sup>.</strong> Maxrajdagi ifoda manfiy "
                       "koʻrsatkich bilan yuqoriga koʻtariladi.</p>"
                       "<p><strong>x<sup>1/3</sup></strong> — bu kub ildiz, butunlay "
                       "boshqa narsa: maxraj ildizni, minus esa oʻrinni bildiradi.</p>",
    },
    {
        "text": "<p>In the exponent <i>m</i>/<i>n</i>, what does the denominator "
                "<i>n</i> tell you?</p>",
        "choices": ["Which root to take", "Which power to raise to",
                    "How many times to divide", "Whether the answer is negative"],
        "correct": "Which root to take",
        "explanation": "<p><strong>Qaysi ildizni olish kerakligini.</strong> Maxraj — "
                       "ildizning darajasi, surat esa daraja.</p>"
                       "<p>8<sup>2/3</sup> da 3 kub ildizni, 2 esa kvadratga "
                       "koʻtarishni bildiradi.</p>",
    },
    {
        "text": "<p>Which is larger: 64<sup>1/2</sup> or 64<sup>1/3</sup>?</p>",
        "choices": ["64<sup>1/2</sup>, which is 8", "64<sup>1/3</sup>, which is 4",
                    "They are equal", "64<sup>1/3</sup>, which is 8"],
        "correct": "64<sup>1/2</sup>, which is 8",
        "explanation": "<p><strong>64<sup>1/2</sup> = 8.</strong> Kvadrat ildiz 8, kub "
                       "ildiz esa 4.</p>"
                       "<p>Qoida: ildizning darajasi <b>kattalashsa</b>, natija "
                       "kichrayadi (1 dan katta sonlar uchun).</p>",
    },
    {
        "text": "<p>A student writes 2<sup>−3</sup> = −8. What is the mistake?</p>",
        "choices": ["The minus makes the number negative instead of moving it to the denominator",
                    "The exponent should have been added",
                    "2<sup>3</sup> is not 8",
                    "There is no mistake"],
        "correct": "The minus makes the number negative instead of moving it to the denominator",
        "explanation": "<p><strong>Minus ishorani emas, oʻrinni oʻzgartiradi.</strong> "
                       "Toʻgʻrisi: 2<sup>−3</sup> = 1/8.</p>"
                       "<p>Manfiy koʻrsatkichli musbat asos har doim <b>musbat</b> "
                       "javob beradi.</p>",
    },
    {
        "text": "<p>A student writes <i>x</i><sup>0</sup> = 0. What is the correct "
                "value, for <i>x</i> ≠ 0?</p>",
        "choices": ["0", "1", "<i>x</i>", "It is undefined"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> Nol daraja har doim 1 beradi.</p>"
                       "<p>Sabab boʻlish qonunida: x<sup>n</sup> ÷ x<sup>n</sup> "
                       "ham 1 ga, ham x<sup>0</sup> ga teng.</p>",
    },
    {
        "text": "<p>For <i>x</i> &gt; 0, simplify: (<i>x</i><sup>1/2</sup>)<sup>6</sup></p>",
        "choices": ["<i>x</i><sup>1/3</sup>", "<i>x</i><sup>3</sup>",
                    "<i>x</i><sup>6</sup>", "<i>x</i><sup>12</sup>"],
        "correct": "<i>x</i><sup>3</sup>",
        "explanation": "<p><strong>x<sup>3</sup>.</strong> Qavs koʻrsatkichlarni "
                       "koʻpaytiradi: (1/2) × 6 = 3.</p>"
                       "<p>Kasr koʻrsatkich ham xuddi butun koʻrsatkich kabi "
                       "qonunlarga boʻysunadi — bu butun mavzuning maʼnosi.</p>",
    },
    {
        "text": "<p>What is the value of 4<sup>3/2</sup>?</p>",
        "choices": ["6", "8", "12", "64"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> √4 = 2, keyin 2<sup>3</sup> = 8.</p>"
                       "<p><strong>6</strong> — 4 × 3/2 hisoblangan javob; "
                       "<strong>64</strong> — 4<sup>3</sup>, maxraj eʼtiborsiz "
                       "qolgan.</p>",
    },
    {
        "text": "<p>A photo is scaled so that each side is multiplied by 4<sup>1/2</sup>. "
                "By what number is each side multiplied?</p>",
        "choices": ["2", "4", "8", "16"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> 4<sup>1/2</sup> = √4 = 2 — har bir "
                       "tomon ikki barobar ortadi.</p>"
                       "<p><strong>4</strong> — koʻrsatkichni eʼtiborsiz qoldirgan "
                       "javob. (Yuzasi esa toʻrt barobar ortadi.)</p>",
    },
    {
        "text": "<p>A quantity is multiplied by 10<sup>−3</sup>. What happens to it?</p>",
        "choices": ["It becomes 1,000 times smaller", "It becomes 1,000 times larger",
                    "It becomes negative", "It becomes 3 times smaller"],
        "correct": "It becomes 1,000 times smaller",
        "explanation": "<p><strong>Ming marta kichrayadi.</strong> 10<sup>−3</sup> = "
                       "1/1,000.</p>"
                       "<p><strong>«Negative»</strong> — manfiy koʻrsatkichning eng "
                       "koʻp uchraydigan notoʻgʻri oʻqilishi; u faqat kichraytiradi.</p>",
    },
]


# =====================================================================
# SAT-25 — simplifying radicals
# =====================================================================

Q_SAT25 = [
    {
        "text": "<p>Simplify: √50</p>",
        "choices": ["2√5", "5√2", "10√5", "25√2"],
        "correct": "5√2",
        "explanation": "<p><strong>5√2.</strong> 50 = 25 × 2, va √25 = 5.</p>"
                       "<p><strong>25√2</strong> — toʻliq kvadrat ildizsiz "
                       "chiqarilgan: tashqariga 25 emas, uning ildizi 5 chiqadi.</p>",
    },
    {
        "text": "<p>Simplify: √48</p>",
        "choices": ["3√4", "4√3", "6√2", "16√3"],
        "correct": "4√3",
        "explanation": "<p><strong>4√3.</strong> 48 = 16 × 3, va √16 = 4.</p>"
                       "<p><strong>3√4</strong> — koʻpaytuvchilar oʻrin almashgan; "
                       "tashqariga <b>toʻliq kvadratning ildizi</b> chiqadi.</p>",
    },
    {
        "text": "<p>Simplify: √32</p>",
        "choices": ["2√8", "4√2", "8√2", "16√2"],
        "correct": "4√2",
        "explanation": "<p><strong>4√2.</strong> 32 = 16 × 2.</p>"
                       "<p><strong>2√8</strong> — 4 ni ajratgan javob; u toʻgʻri, "
                       "lekin <b>soddalashtirilmagan</b>: √8 hali ham ochiladi. "
                       "Eng katta toʻliq kvadratni qidiring.</p>",
    },
    {
        "text": "<p>Simplify: √75</p>",
        "choices": ["3√5", "5√3", "15", "25√3"],
        "correct": "5√3",
        "explanation": "<p><strong>5√3.</strong> 75 = 25 × 3.</p>"
                       "<p>Tekshiruv: 5 × 1.73 ≈ 8.66, va √75 ≈ 8.66 ✓ — "
                       "kalkulyatorda 10 soniyada tasdiqlanadi.</p>",
    },
    {
        "text": "<p>Simplify: √72</p>",
        "choices": ["2√18", "6√2", "8√3", "36√2"],
        "correct": "6√2",
        "explanation": "<p><strong>6√2.</strong> 72 = 36 × 2, va √36 = 6.</p>"
                       "<p><strong>2√18</strong> — 4 ni ajratgan javob va u hali "
                       "soddalashtirilmagan (√18 = 3√2).</p>",
    },
    {
        "text": "<p>Simplify: 3√2 + 5√2</p>",
        "choices": ["8√2", "8√4", "15√2", "√2"],
        "correct": "8√2",
        "explanation": "<p><strong>8√2.</strong> Ildiz ostidagi son bir xil, demak "
                       "koeffitsientlar qoʻshiladi — xuddi 3x + 5x kabi.</p>"
                       "<p><strong>8√4</strong> — ildiz ostidagi sonni ham qoʻshgan "
                       "javob; u oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Simplify: 2√5 + 7√5</p>",
        "choices": ["9√5", "9√10", "14√5", "√5"],
        "correct": "9√5",
        "explanation": "<p><strong>9√5.</strong> 2 + 7 = 9, ildiz oʻzgarmaydi.</p>"
                       "<p><strong>14√5</strong> — koeffitsientlarni koʻpaytirgan "
                       "javob; bu qoʻshish, koʻpaytirish emas.</p>",
    },
    {
        "text": "<p>Simplify: √2 · √8</p>",
        "choices": ["4", "√10", "2√8", "16"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> √2 · √8 = √16 = 4 — ildiz butunlay "
                       "yoʻqoldi.</p>"
                       "<p><strong>√10</strong> — ildiz ostidagi sonlarni qoʻshgan "
                       "javob; koʻpaytirishda ular <b>koʻpaytiriladi</b>.</p>",
    },
    {
        "text": "<p>Simplify: √3 · √12</p>",
        "choices": ["6", "√15", "3√12", "36"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 3 × 12 = 36, va √36 = 6.</p>"
                       "<p><strong>36</strong> — ildiz olishni unutgan javob. Ikki "
                       "irratsional son koʻpaytirilib butun son berishi mumkin.</p>",
    },
    {
        "text": "<p>Simplify: 2√18 + √8</p>",
        "choices": ["6√2", "8√2", "10√2", "√80"],
        "correct": "8√2",
        "explanation": "<p><strong>8√2.</strong> 2√18 = 6√2 va √8 = 2√2, demak "
                       "yigʻindi 8√2.</p>"
                       "<p><strong>√80</strong> — ildiz ostidagi sonlarni qoʻshgan "
                       "javob (72 + 8). Ildiz qoʻshishga taqsimlanmaydi.</p>",
    },
    {
        "text": "<p>Simplify: √200</p>",
        "choices": ["2√100", "10√2", "20√5", "100√2"],
        "correct": "10√2",
        "explanation": "<p><strong>10√2.</strong> 200 = 100 × 2, va √100 = 10.</p>"
                       "<p><strong>2√100</strong> — teskari ajratilgan: √100 ning "
                       "oʻzi butun son, shuning uchun uni tashqariga chiqarish "
                       "kerak.</p>",
    },
    {
        "text": "<p>Why is √9 + √16 not equal to √25?</p>",
        "choices": ["Because the square root does not distribute over addition",
                    "Because 9 and 16 are not perfect squares",
                    "Because 9 + 16 is not 25",
                    "Because square roots cannot be added at all"],
        "correct": "Because the square root does not distribute over addition",
        "explanation": "<p><strong>Ildiz qoʻshishga taqsimlanmaydi.</strong> "
                       "√9 + √16 = 3 + 4 = 7, √25 esa 5.</p>"
                       "<p>Qoida faqat <b>koʻpaytirish</b> uchun: √(a · b) = "
                       "√a · √b.</p>",
    },
    {
        "text": "<p>A square field has an area of 200 square metres. What is the length "
                "of one side, in simplest radical form?</p>",
        "choices": ["10√2 metres", "20√5 metres", "100 metres", "50 metres"],
        "correct": "10√2 metres",
        "explanation": "<p><strong>10√2 metr.</strong> Tomoni √200, va "
                       "200 = 100 × 2.</p>"
                       "<p>Taxminan 14.1 metr — javobni chamalash uchun "
                       "√2 ≈ 1.41 ni bilish yetarli.</p>",
    },
    {
        "text": "<p>Between which two whole numbers does √75 lie?</p>",
        "choices": ["7 and 8", "8 and 9", "9 and 10", "37 and 38"],
        "correct": "8 and 9",
        "explanation": "<p><strong>8 va 9 orasida.</strong> 8<sup>2</sup> = 64 va "
                       "9<sup>2</sup> = 81, va 75 ular orasida.</p>"
                       "<p><strong>37 va 38</strong> — 75 ni ikkiga boʻlgan javob; "
                       "ildiz olish boʻlish emas.</p>",
    },
    {
        "text": "<p>Is √2 + √3 equal to √5?</p>",
        "choices": ["Yes", "No — the two radicals are not alike and cannot be combined",
                    "Yes, but only approximately", "No — it equals √6"],
        "correct": "No — the two radicals are not alike and cannot be combined",
        "explanation": "<p><strong>Yoʻq.</strong> 1.41 + 1.73 = 3.14, √5 esa 2.24 — "
                       "ular teng emas.</p>"
                       "<p>√2 va √3 — oʻxshash hadlar emas, xuddi x va y kabi: "
                       "ularni qoʻshib bitta ifodaga aylantirib boʻlmaydi.</p>",
    },
    {
        "text": "<p>A student simplifies √75 as 25√3. What is the mistake?</p>",
        "choices": ["The perfect square was taken out without taking its root",
                    "75 has no perfect square factor",
                    "The answer should keep the radical over 75",
                    "There is no mistake"],
        "correct": "The perfect square was taken out without taking its root",
        "explanation": "<p><strong>Toʻliq kvadrat ildizsiz chiqarilgan.</strong> "
                       "Tashqariga 25 emas, √25 = 5 chiqadi.</p>"
                       "<p>Tekshiruv: 25√3 ≈ 43.3, √75 esa ≈ 8.66 — javob oʻn barobar "
                       "katta.</p>",
    },
    {
        "text": "<p>Simplify: √98</p>",
        "choices": ["7√2", "2√49", "14√2", "49√2"],
        "correct": "7√2",
        "explanation": "<p><strong>7√2.</strong> 98 = 49 × 2, va √49 = 7.</p>"
                       "<p><strong>2√49</strong> — ajratish teskari qilingan; "
                       "√49 = 7 butun son, demak u tashqariga chiqishi kerak.</p>",
    },
    {
        "text": "<p>Simplify: 3√12 − √27</p>",
        "choices": ["2√3", "3√3", "5√3", "3√15"],
        "correct": "3√3",
        "explanation": "<p><strong>3√3.</strong> √12 = 2√3, demak 3√12 = 6√3; "
                       "√27 = 3√3. Ayirma: 6√3 − 3√3 = 3√3.</p>"
                       "<p>Avval <b>ikkalasini ham soddalashtiring</b> — shundagina "
                       "ular oʻxshash hadlarga aylanadi.</p>",
    },
    {
        "text": "<p>A square garden has an area of 72 square metres. What is the length "
                "of one side, in simplest radical form?</p>",
        "choices": ["6√2 metres", "8√3 metres", "36√2 metres", "12 metres"],
        "correct": "6√2 metres",
        "explanation": "<p><strong>6√2 metr.</strong> √72 = √36 · √2 = 6√2 "
                       "(taxminan 8.5 metr).</p>"
                       "<p><strong>12 metr</strong> — 72 ni oltiga boʻlgan javob; "
                       "kvadratning tomoni yuzaning <b>ildizi</b>.</p>",
    },
    {
        "text": "<p>A square tile has sides of 5 centimetres. What is the length of its "
                "diagonal, in simplest radical form?</p>",
        "choices": ["5√2 centimetres", "10 centimetres", "25√2 centimetres",
                    "√10 centimetres"],
        "correct": "5√2 centimetres",
        "explanation": "<p><strong>5√2 santimetr.</strong> Diagonal "
                       "√(25 + 25) = √50 = 5√2 (taxminan 7.1 sm).</p>"
                       "<p><strong>10 sm</strong> — ikki tomonni qoʻshgan javob; "
                       "diagonal ikki tomonning yigʻindisidan har doim "
                       "<b>qisqaroq</b>.</p>",
    },
]


PRACTICES = [
    {
        "title":       "SAT-21 Practice: Systems of Linear Inequalities and Bounded Regions",
        "description": "20 ta SAT uslubidagi savol — ikki sohaning kesishmasi, nuqtani "
                       "ikkala shartga qoʻyish va byudjet + minimal talab modeli.",
        "tutorial":    "SAT-21:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT21,
    },
    {
        "title":       "SAT-22 Practice: Absolute Value Inequalities on the Number Line",
        "description": "20 ta SAT uslubidagi savol — «kichik» oraliq, «katta» ikki "
                       "tomon, izolyatsiya va meʼyor–chetlanish masalalari.",
        "tutorial":    "SAT-22:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT22,
    },
    {
        "title":       "SAT-23 Practice: Laws of Exponents: Multiplication, Division, and Power-to-Power",
        "description": "20 ta SAT uslubidagi savol — qoʻshish/ayirish/koʻpaytirish "
                       "qonunlari va qavs ichidagi koeffitsient.",
        "tutorial":    "SAT-23:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT23,
    },
    {
        "title":       "SAT-24 Practice: Negative and Fractional Exponents",
        "description": "20 ta SAT uslubidagi savol — nol daraja, manfiy koʻrsatkich va "
                       "«maxraj — ildiz, surat — daraja» qoidasi.",
        "tutorial":    "SAT-24:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT24,
    },
    {
        "title":       "SAT-25 Practice: Simplifying Radical Expressions",
        "description": "20 ta SAT uslubidagi savol — toʻliq kvadratni chiqarish, "
                       "oʻxshash ildizlarni qoʻshish va ildizlarni koʻpaytirish.",
        "tutorial":    "SAT-25:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT25,
    },
]
