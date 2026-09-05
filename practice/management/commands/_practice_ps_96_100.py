# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-96 … SAT-100. OXIRGI BATCH. Kurs tugaydi.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.
⚠️ Javob har doim "correct" da va choices ning BIRINCHISIDA turadi.
⚠️ SAT-97 da jadval har bir savolda qayta aytiladi (savollar mustaqil).

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_96_100.py --master=prime \\
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

# The survey used throughout SAT-97, restated in each question that needs it.
SURVEY = ("<p><i>A survey of 80 students: in Grade 9, 18 chose Korean and 22 chose "
          "Russian; in Grade 10, 12 chose Korean and 28 chose Russian.</i></p>")


# =====================================================================
# SAT-96 — domain and range
# =====================================================================

Q_SAT96 = [
    {
        "text": "<p>Which value of <i>x</i> is NOT in the domain of "
                "1 ÷ (<i>x</i> − 3)?</p>",
        "choices": ["3", "0", "−3", "1"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Maxraj nolga aylanadi.</p>"
                       "<p><strong>−3</strong> — ifodadagi 3 ning manfiysi "
                       "tanlangan; u mutlaqo mumkin.</p>",
    },
    {
        "text": "<p>Which value of <i>x</i> is NOT in the domain of "
                "1 ÷ (<i>x</i> + 5)?</p>",
        "choices": ["−5", "5", "0", "1"],
        "correct": "−5",
        "explanation": "<p><strong>−5.</strong> x + 5 = 0 boʻlgan joy.</p>",
    },
    {
        "text": "<p>What is the domain of √(<i>x</i> − 2)?</p>",
        "choices": ["<i>x</i> ≥ 2", "<i>x</i> ≤ 2", "<i>x</i> ≥ 0",
                    "all real numbers"],
        "correct": "<i>x</i> ≥ 2",
        "explanation": "<p><strong>x ≥ 2.</strong> Ildiz ostidagi ifoda manfiy "
                       "boʻlmasligi kerak.</p>",
    },
    {
        "text": "<p>What is the domain of √<i>x</i>?</p>",
        "choices": ["<i>x</i> ≥ 0", "<i>x</i> &gt; 0", "all real numbers",
                    "<i>x</i> ≤ 0"],
        "correct": "<i>x</i> ≥ 0",
        "explanation": "<p><strong>x ≥ 0.</strong> Nolning ildizi bor — u "
                       "nolga teng.</p>",
    },
    {
        "text": "<p>What is the range of <i>y</i> = <i>x</i>² − 4?</p>",
        "choices": ["<i>y</i> ≥ −4", "<i>y</i> ≥ 0", "<i>y</i> ≥ 4",
                    "all real numbers"],
        "correct": "<i>y</i> ≥ −4",
        "explanation": "<p><strong>y ≥ −4.</strong> x² eng kichigi 0.</p>"
                       "<p><strong>all real numbers</strong> — bu domainning "
                       "javobi.</p>",
    },
    {
        "text": "<p>What is the range of <i>y</i> = <i>x</i>² + 7?</p>",
        "choices": ["<i>y</i> ≥ 7", "<i>y</i> ≥ 0", "<i>y</i> ≤ 7",
                    "all real numbers"],
        "correct": "<i>y</i> ≥ 7",
        "explanation": "<p><strong>y ≥ 7.</strong> Eng past nuqta (0, 7).</p>",
    },
    {
        "text": "<p>What is the range of <i>y</i> = 3<i>x</i> + 1?</p>",
        "choices": ["all real numbers", "<i>y</i> ≥ 1", "<i>y</i> ≥ 0",
                    "<i>y</i> ≥ 3"],
        "correct": "all real numbers",
        "explanation": "<p><strong>Barcha haqiqiy sonlar.</strong> Chiziqli "
                       "funksiya har qanday qiymatga yetadi.</p>",
    },
    {
        "text": "<p>What is the domain of <i>y</i> = 3<i>x</i> + 1?</p>",
        "choices": ["all real numbers", "<i>x</i> ≥ 0", "<i>x</i> ≥ 1",
                    "<i>x</i> ≠ 3"],
        "correct": "all real numbers",
        "explanation": "<p><strong>Barcha haqiqiy sonlar.</strong> Maxraj ham, "
                       "ildiz ham yoʻq — taqiq yoʻq.</p>",
    },
    {
        "text": "<p>A function gives the cost of <i>n</i> tickets. Which value of "
                "<i>n</i> would NOT make sense?</p>",
        "choices": ["3.5", "0", "4", "12"],
        "correct": "3.5",
        "explanation": "<p><strong>3.5.</strong> Chipta kasr boʻlmaydi. Nol "
                       "esa mumkin — hech narsa sotib olinmagan.</p>",
    },
    {
        "text": "<p>What does the domain of a function mean?</p>",
        "choices": ["The values that may be put in",
                    "The values that may come out",
                    "The highest value of the function",
                    "The values where the graph crosses the axes"],
        "correct": "The values that may be put in",
        "explanation": "<p><strong>Kirish qiymatlari.</strong> Domain — eshik, "
                       "range — natija.</p>",
    },
    {
        "text": "<p>What does the range of a function mean?</p>",
        "choices": ["The values that may come out",
                    "The values that may be put in",
                    "The width of the graph",
                    "The distance between the roots"],
        "correct": "The values that may come out",
        "explanation": "<p><strong>Chiqish qiymatlari.</strong></p>",
    },
    {
        "text": "<p>Which value is NOT in the domain of 1 ÷ <i>x</i>?</p>",
        "choices": ["0", "1", "−1", "100"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Nolga boʻlish mumkin emas.</p>",
    },
    {
        "text": "<p>What is the range of <i>y</i> = −<i>x</i>² + 5?</p>",
        "choices": ["<i>y</i> ≤ 5", "<i>y</i> ≥ 5", "<i>y</i> ≥ −5",
                    "all real numbers"],
        "correct": "<i>y</i> ≤ 5",
        "explanation": "<p><strong>y ≤ 5.</strong> Parabola pastga qaragan, "
                       "demak chegara yuqoridan.</p>"
                       "<p><strong>y ≥ 5</strong> — ishoraga qaralmagan.</p>",
    },
    {
        "text": "<p>A function gives the number of people in a room. Which value "
                "cannot occur?</p>",
        "choices": ["−2", "0", "1", "40"],
        "correct": "−2",
        "explanation": "<p><strong>−2.</strong> Odamlar soni manfiy "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p>What is the domain of √(<i>x</i> + 3)?</p>",
        "choices": ["<i>x</i> ≥ −3", "<i>x</i> ≥ 3", "<i>x</i> ≤ −3",
                    "all real numbers"],
        "correct": "<i>x</i> ≥ −3",
        "explanation": "<p><strong>x ≥ −3.</strong> x + 3 ≥ 0.</p>",
    },
    {
        "text": "<p>What is the range of <i>y</i> = <i>x</i>²?</p>",
        "choices": ["<i>y</i> ≥ 0", "<i>y</i> &gt; 0", "all real numbers",
                    "<i>y</i> ≤ 0"],
        "correct": "<i>y</i> ≥ 0",
        "explanation": "<p><strong>y ≥ 0.</strong> Nol ham kiradi (x = 0 da).</p>",
    },
    {
        "text": "<p>Which of these does NOT restrict a domain?</p>",
        "choices": ["Adding a constant", "Division by zero",
                    "An even root of a negative number",
                    "A real-world meaning such as a count of people"],
        "correct": "Adding a constant",
        "explanation": "<p><strong>Doimiy qoʻshish.</strong> Faqat uch narsa "
                       "taqiqlaydi, va qoʻshish ular orasida yoʻq.</p>",
    },
    {
        "text": "<p>Which value is NOT in the domain of 1 ÷ (2<i>x</i> − 6)?</p>",
        "choices": ["3", "6", "−3", "0"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> 2x − 6 = 0 → x = 3.</p>"
                       "<p><strong>6</strong> — ifodadagi son koʻchirilgan; "
                       "avval tenglamani yeching.</p>",
    },
    {
        "text": "<p>What is the range of <i>y</i> = (<i>x</i> − 2)² + 1?</p>",
        "choices": ["<i>y</i> ≥ 1", "<i>y</i> ≥ 2", "<i>y</i> ≥ 0",
                    "<i>y</i> ≥ 3"],
        "correct": "<i>y</i> ≥ 1",
        "explanation": "<p><strong>y ≥ 1.</strong> Uch (2, 1) da; chegara "
                       "uchning y qiymatidan boshlanadi.</p>"
                       "<p><strong>y ≥ 2</strong> — uchning x koordinatasi "
                       "olingan.</p>",
    },
    {
        "text": "<p>A shop's takings are given by a function of <i>n</i>, the number "
                "of items sold. Which value of <i>n</i> is impossible?</p>",
        "choices": ["−4", "0", "5", "20"],
        "correct": "−4",
        "explanation": "<p><strong>−4.</strong> Sotilgan buyumlar soni manfiy "
                       "boʻlmaydi — bu hayotiy domain.</p>",
    },
]


# =====================================================================
# SAT-97 — data tables
# =====================================================================

Q_SAT97 = [
    {
        "text": SURVEY + "<p>What fraction of all the students chose Korean?</p>",
        "choices": ["3/8", "3/5", "9/20", "5/8"],
        "correct": "3/8",
        "explanation": "<p><strong>3/8.</strong> 30 ÷ 80 — maxraj umumiy "
                       "jami.</p>",
    },
    {
        "text": SURVEY + "<p>Of the students who chose Korean, what fraction are in "
                         "Grade 9?</p>",
        "choices": ["3/5", "9/20", "3/8", "9/40"],
        "correct": "3/5",
        "explanation": "<p><strong>3/5.</strong> 18 ÷ 30 — maxraj koreys "
                       "tilini tanlaganlar.</p>"
                       "<p><strong>9/20</strong> — maxrajga 9-sinf jami "
                       "olingan.</p>",
    },
    {
        "text": SURVEY + "<p>What fraction of the Grade 9 students chose Korean?</p>",
        "choices": ["9/20", "3/5", "3/8", "1/2"],
        "correct": "9/20",
        "explanation": "<p><strong>9/20.</strong> 18 ÷ 40 — endi maxraj "
                       "9-sinf jami. Surat oʻsha-oʻsha 18.</p>",
    },
    {
        "text": SURVEY + "<p>What percent of the Grade 10 students chose "
                         "Russian?</p>",
        "choices": ["70%", "56%", "35%", "28%"],
        "correct": "70%",
        "explanation": "<p><strong>70%.</strong> 28 ÷ 40.</p>"
                       "<p><strong>56%</strong> — maxrajga rus tilini "
                       "tanlaganlarning jami (50) olingan.</p>",
    },
    {
        "text": SURVEY + "<p>What fraction of all the students chose Russian?</p>",
        "choices": ["5/8", "14/25", "11/20", "7/10"],
        "correct": "5/8",
        "explanation": "<p><strong>5/8.</strong> 50 ÷ 80.</p>",
    },
    {
        "text": SURVEY + "<p>Of the students who chose Russian, what fraction are in "
                         "Grade 10?</p>",
        "choices": ["14/25", "7/10", "5/8", "7/20"],
        "correct": "14/25",
        "explanation": "<p><strong>14/25.</strong> 28 ÷ 50.</p>"
                       "<p><strong>7/10</strong> — maxrajga 10-sinf jami "
                       "olingan.</p>",
    },
    {
        "text": SURVEY + "<p>What percent of the Grade 9 students chose Korean?</p>",
        "choices": ["45%", "60%", "22.5%", "40%"],
        "correct": "45%",
        "explanation": "<p><strong>45%.</strong> 18 ÷ 40 = 0.45.</p>"
                       "<p><strong>60%</strong> — 18 ÷ 30, boshqa "
                       "maxraj.</p>",
    },
    {
        "text": SURVEY + "<p>How many students chose Korean in total?</p>",
        "choices": ["30", "18", "50", "40"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> 18 + 12 — ustun jami.</p>",
    },
    {
        "text": SURVEY + "<p>How many students are in Grade 10?</p>",
        "choices": ["40", "28", "80", "12"],
        "correct": "40",
        "explanation": "<p><strong>40.</strong> 12 + 28 — qator jami.</p>",
    },
    {
        "text": "<p>In a two-way table, Grade 9 has 40 students in total and 22 of "
                "them chose Russian. How many chose Korean?</p>",
        "choices": ["18", "22", "62", "40"],
        "correct": "18",
        "explanation": "<p><strong>18.</strong> Qator jamidan ayiring: "
                       "40 − 22.</p>",
    },
    {
        "text": "<p>Which phrase in a question tells you what the denominator "
                "should be?</p>",
        "choices": ["\"Of the students who…\"", "\"In total…\"",
                    "\"How many…\"", "\"What percent…\""],
        "correct": "\"Of the students who…\"",
        "explanation": "<p><strong>«Of the …».</strong> Undan keyingi guruh "
                       "maxrajni belgilaydi.</p>",
    },
    {
        "text": "<p>A table's heading says \"in thousands\" and a cell reads 24. "
                "What value does that cell represent?</p>",
        "choices": ["24,000", "24", "240", "2,400"],
        "correct": "24,000",
        "explanation": "<p><strong>24,000.</strong> Birlik jadvalning ustida, "
                       "kichkina harflarda yozilgan.</p>",
    },
    {
        "text": "<p>What should you read first when a table appears?</p>",
        "choices": ["The row and column headings", "The largest number",
                    "The answer choices", "The final row"],
        "correct": "The row and column headings",
        "explanation": "<p><strong>Sarlavhalar.</strong> Qatorlar nima, "
                       "ustunlar nima, birlik nima.</p>",
    },
    {
        "text": SURVEY + "<p>Of the students who chose Korean, what percent are in "
                         "Grade 10?</p>",
        "choices": ["40%", "30%", "15%", "24%"],
        "correct": "40%",
        "explanation": "<p><strong>40%.</strong> 12 ÷ 30.</p>"
                       "<p><strong>30%</strong> — 12 ÷ 40, boshqa "
                       "maxraj.</p>",
    },
    {
        "text": SURVEY + "<p>How many students took part in the survey "
                         "altogether?</p>",
        "choices": ["80", "40", "50", "30"],
        "correct": "80",
        "explanation": "<p><strong>80.</strong> 40 + 40, yoki 30 + 50 — "
                       "ikkala yoʻl ham bir xil javob berishi kerak.</p>",
    },
    {
        "text": "<p>On a scatterplot, what should you use to predict a value that "
                "is not among the plotted points?</p>",
        "choices": ["The line of best fit", "The highest point",
                    "The nearest point", "The average of the points"],
        "correct": "The line of best fit",
        "explanation": "<p><strong>Moslashtirilgan chiziq.</strong> Alohida "
                       "nuqtalar undan chetga chiqishi mumkin.</p>",
    },
    {
        "text": "<p>What does \"which statement is supported by the data\" ask "
                "for?</p>",
        "choices": ["A statement that follows directly from the figures",
                    "A statement that is true in general",
                    "An explanation of why the pattern happens",
                    "The largest figure in the table"],
        "correct": "A statement that follows directly from the figures",
        "explanation": "<p><strong>Bevosita kelib chiqadigan jumla.</strong> "
                       "Rost, lekin maʼlumotda koʻrinmaydigan jumla — "
                       "notoʻgʻri javob.</p>",
    },
    {
        "text": "<p>In a two-way table, 30 students chose Korean in total and 12 of "
                "them are in Grade 10. How many are in Grade 9?</p>",
        "choices": ["18", "12", "42", "30"],
        "correct": "18",
        "explanation": "<p><strong>18.</strong> Bu safar <b>ustun</b> jamidan "
                       "ayirildi — javob oʻsha, yoʻl boshqa.</p>",
    },
    {
        "text": SURVEY + "<p>What fraction of all the students are in Grade 9?</p>",
        "choices": ["1/2", "3/8", "5/8", "9/20"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> 40 ÷ 80.</p>",
    },
    {
        "text": SURVEY + "<p>Of the 50 students who chose Russian, how many are in "
                         "Grade 9?</p>",
        "choices": ["22", "28", "18", "40"],
        "correct": "22",
        "explanation": "<p><strong>22.</strong> Bu jadvaldagi katakning oʻzi — "
                       "hisoblash kerak emas, oʻqish kerak.</p>",
    },
]


# =====================================================================
# SAT-98 — the reference sheet
# =====================================================================

Q_SAT98 = [
    {
        "text": "<p>A cone has radius 3 and height 4. What is its volume?</p>",
        "choices": ["12π", "36π", "4π", "48π"],
        "correct": "12π",
        "explanation": "<p><strong>12π.</strong> (1/3)π(9)(4).</p>"
                       "<p><strong>36π</strong> — uchdan bir tushib qolgan; "
                       "bu silindrning hajmi.</p>",
    },
    {
        "text": "<p>A cone has radius 6 and height 5. What is its volume?</p>",
        "choices": ["60π", "180π", "30π", "20π"],
        "correct": "60π",
        "explanation": "<p><strong>60π.</strong> (1/3)π(36)(5).</p>",
    },
    {
        "text": "<p>A cylinder has radius 2 and height 7. What is its volume?</p>",
        "choices": ["28π", "14π", "84π", "9.33π"],
        "correct": "28π",
        "explanation": "<p><strong>28π.</strong> π(4)(7) — bu yerda uchdan "
                       "bir YOʻQ.</p>",
    },
    {
        "text": "<p>A sphere has radius 3. What is its volume?</p>",
        "choices": ["36π", "12π", "27π", "108π"],
        "correct": "36π",
        "explanation": "<p><strong>36π.</strong> (4/3)π(27).</p>",
    },
    {
        "text": "<p>Which of the following is NOT provided on the reference "
                "sheet?</p>",
        "choices": ["The slope formula", "The area of a circle",
                    "The Pythagorean theorem", "The volume of a sphere"],
        "correct": "The slope formula",
        "explanation": "<p><strong>Qiyalik formulasi.</strong> Qolgan uchtasi "
                       "varaqda bor.</p>",
    },
    {
        "text": "<p>Is the quadratic formula provided on the reference sheet?</p>",
        "choices": ["No", "Yes", "Only in the second module",
                    "Only for grid-in questions"],
        "correct": "No",
        "explanation": "<p><strong>Yoʻq.</strong> Kvadrat tenglama formulasi "
                       "varaqda berilmagan.</p>",
    },
    {
        "text": "<p>Is the area of a circle provided on the reference sheet?</p>",
        "choices": ["Yes", "No", "Only the circumference is",
                    "Only for geometry questions"],
        "correct": "Yes",
        "explanation": "<p><strong>Ha.</strong> Yuza ham, aylana uzunligi ham "
                       "varaqda.</p>",
    },
    {
        "text": "<p>Which two solids have a one-third in their volume formula?</p>",
        "choices": ["The cone and the pyramid", "The cylinder and the cone",
                    "The sphere and the cone", "The box and the pyramid"],
        "correct": "The cone and the pyramid",
        "explanation": "<p><strong>Konus va piramida.</strong> Uchi teppa "
                       "boʻlgan jismlar.</p>",
    },
    {
        "text": "<p>Which three formulas should you memorise because they are NOT on "
                "the sheet?</p>",
        "choices": ["Slope, SOH-CAH-TOA and the circle equation",
                    "Circle area, circumference and the triangle area",
                    "The five volume formulas",
                    "The two special right triangles"],
        "correct": "Slope, SOH-CAH-TOA and the circle equation",
        "explanation": "<p><strong>Qiyalik, SOH-CAH-TOA, aylana "
                       "tenglamasi.</strong> Qolganlari varaqda bor.</p>",
    },
    {
        "text": "<p>A cone has volume 12π and radius 3. What is its height?</p>",
        "choices": ["4", "12", "36", "1.33"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> (1/3)π(9)h = 12π → 3h = 12. "
                       "π ikkala tomonda qisqaradi.</p>",
    },
    {
        "text": "<p>Is SOH-CAH-TOA provided on the reference sheet?</p>",
        "choices": ["No", "Yes", "Only the sine rule is",
                    "Only in degrees mode"],
        "correct": "No",
        "explanation": "<p><strong>Yoʻq.</strong> Bu Blok D dagi yagona "
                       "majburiy yodlash.</p>",
    },
    {
        "text": "<p>Is the Pythagorean theorem provided on the reference sheet?</p>",
        "choices": ["Yes", "No", "Only for right triangles with whole sides",
                    "Only in the first module"],
        "correct": "Yes",
        "explanation": "<p><strong>Ha.</strong> Ikkita maxsus uchburchak "
                       "bilan birga.</p>",
    },
    {
        "text": "<p>A sphere has radius 6. What is its volume?</p>",
        "choices": ["288π", "144π", "216π", "72π"],
        "correct": "288π",
        "explanation": "<p><strong>288π.</strong> (4/3)π(216).</p>"
                       "<p><strong>216π</strong> — kubga koʻtarilgan, lekin "
                       "4/3 ga koʻpaytirilmagan.</p>",
    },
    {
        "text": "<p>A pyramid has a rectangular base 3 by 4 and a height of 5. What "
                "is its volume?</p>",
        "choices": ["20", "60", "12", "15"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> (1/3)(3)(4)(5).</p>"
                       "<p><strong>60</strong> — uchdan bir tushib "
                       "qolgan.</p>",
    },
    {
        "text": "<p>A cylinder has radius 5 and height 2. What is its volume?</p>",
        "choices": ["50π", "20π", "100π", "16.67π"],
        "correct": "50π",
        "explanation": "<p><strong>50π.</strong> π(25)(2).</p>",
    },
    {
        "text": "<p>Are the two special right triangles provided on the reference "
                "sheet?</p>",
        "choices": ["Yes, with diagrams", "No",
                    "Only the 45-45-90 one", "Only their angle measures"],
        "correct": "Yes, with diagrams",
        "explanation": "<p><strong>Ha, chizma bilan.</strong> Demak qaysi "
                       "tomon qaysi burchakka qarshi ekani ham "
                       "koʻrinadi.</p>",
    },
    {
        "text": "<p>Is the equation of a circle provided on the reference sheet?</p>",
        "choices": ["No", "Yes", "Only the area of a circle is provided as well",
                    "Only for questions about the xy-plane"],
        "correct": "No",
        "explanation": "<p><strong>Yoʻq.</strong> Aylana yuzasi bor, "
                       "tenglamasi yoʻq — bu ikkalasi chalkashtiriladi.</p>",
    },
    {
        "text": "<p>A cone has radius 3 and height 8. What is its volume?</p>",
        "choices": ["24π", "72π", "8π", "12π"],
        "correct": "24π",
        "explanation": "<p><strong>24π.</strong> (1/3)π(9)(8).</p>",
    },
    {
        "text": "<p>What is the real skill in using the reference sheet?</p>",
        "choices": ["Knowing what is NOT on it",
                    "Memorising everything on it",
                    "Opening it on every question",
                    "Copying it onto the scratch paper"],
        "correct": "Knowing what is NOT on it",
        "explanation": "<p><strong>Unda nima yoʻqligini bilish.</strong> "
                       "Undagilar bir bosish naridagi joyda turibdi.</p>",
    },
    {
        "text": "<p>A paper cup is shaped like a cone with radius 4 and height 9. "
                "What is its volume?</p>",
        "choices": ["48π", "144π", "36π", "12π"],
        "correct": "48π",
        "explanation": "<p><strong>48π.</strong> (1/3)π(16)(9).</p>"
                       "<p><strong>144π</strong> — uchdan bir tushib "
                       "qolgan.</p>",
    },
]


# =====================================================================
# SAT-99 — the adaptive second module
# =====================================================================

Q_SAT99 = [
    {
        "text": "<p>What determines which second math module a student receives?</p>",
        "choices": ["Their performance on the first module",
                    "The order in which they answered",
                    "The test date",
                    "Nothing — it is the same for everyone"],
        "correct": "Their performance on the first module",
        "explanation": "<p><strong>Birinchi moduldagi natija.</strong></p>"
                       "<p><strong>Nothing</strong> — bu <b>birinchi</b> "
                       "modul haqida rost.</p>",
    },
    {
        "text": "<p>How many questions are in one math module?</p>",
        "choices": ["22", "20", "35", "44"],
        "correct": "22",
        "explanation": "<p><strong>22.</strong> Ikkita modul, jami 44.</p>",
    },
    {
        "text": "<p>How many minutes are given for one math module?</p>",
        "choices": ["35", "22", "70", "45"],
        "correct": "35",
        "explanation": "<p><strong>35.</strong> Jami 70 daqiqa.</p>",
    },
    {
        "text": "<p>A student answers all 22 questions in 30 minutes. About how many "
                "seconds per question is that?</p>",
        "choices": ["82", "95", "65", "110"],
        "correct": "82",
        "explanation": "<p><strong>82.</strong> 1,800 ÷ 22.</p>"
                       "<p><strong>95</strong> — bu toʻliq 35 daqiqa uchun "
                       "oʻrtacha.</p>",
    },
    {
        "text": "<p>A student answers all 22 questions in 33 minutes. How many "
                "seconds per question?</p>",
        "choices": ["90", "95", "82", "100"],
        "correct": "90",
        "explanation": "<p><strong>90.</strong> 1,980 ÷ 22.</p>",
    },
    {
        "text": "<p>During the second module, may a student return to the first?</p>",
        "choices": ["No, a closed module cannot be reopened",
                    "Yes, at any time",
                    "Yes, but only for flagged questions",
                    "Yes, in the last two minutes"],
        "correct": "No, a closed module cannot be reopened",
        "explanation": "<p><strong>Yoʻq.</strong> Har bir modulni alohida "
                       "imtihon deb qarang.</p>",
    },
    {
        "text": "<p>Does the second module count towards the score?</p>",
        "choices": ["Yes, both modules count", "No, only the first counts",
                    "Only if it is the harder version",
                    "Only the first half of it"],
        "correct": "Yes, both modules count",
        "explanation": "<p><strong>Ha, ikkalasi ham.</strong></p>",
    },
    {
        "text": "<p>The second module feels much harder than the first. What does "
                "that most likely mean?</p>",
        "choices": ["The student did well on the first module",
                    "The student did badly on the first module",
                    "The test is faulty",
                    "The student will not finish"],
        "correct": "The student did well on the first module",
        "explanation": "<p><strong>Birinchi modul yaxshi yozilgan.</strong> "
                       "Qiyin modul — yaxshi xabar.</p>",
    },
    {
        "text": "<p>The second module feels easy. What should the student do?</p>",
        "choices": ["Keep exactly the same care",
                    "Speed up and finish early",
                    "Assume the score will be low",
                    "Skip the checks"],
        "correct": "Keep exactly the same care",
        "explanation": "<p><strong>Eʼtiborni pasaytirmang.</strong> Oson "
                       "savolni yoʻqotish qiyinini yoʻqotishdan "
                       "achinarliroq.</p>",
    },
    {
        "text": "<p>How many math questions are there in total?</p>",
        "choices": ["44", "22", "35", "70"],
        "correct": "44",
        "explanation": "<p><strong>44.</strong> 22 + 22.</p>",
    },
    {
        "text": "<p>How many minutes in total are given to the math section?</p>",
        "choices": ["70", "35", "44", "95"],
        "correct": "70",
        "explanation": "<p><strong>70.</strong> 35 + 35.</p>",
    },
    {
        "text": "<p>Should a student ever leave a question blank in module one?</p>",
        "choices": ["Never — there is no penalty and it also lowers the next module",
                    "Yes, if the question is very hard",
                    "Yes, to save time for module two",
                    "Only on grid-in questions"],
        "correct": "Never — there is no penalty and it also lowers the next module",
        "explanation": "<p><strong>Hech qachon.</strong> Bu yerda boʻsh javob "
                       "ikki barobar qimmat.</p>",
    },
    {
        "text": "<p>A student uses the whole 35 minutes for 22 questions. How many "
                "seconds per question is that?</p>",
        "choices": ["95", "82", "90", "105"],
        "correct": "95",
        "explanation": "<p><strong>95.</strong> 2,100 ÷ 22.</p>",
    },
    {
        "text": "<p>What carries over from the first module to the second?</p>",
        "choices": ["Nothing", "The flagged questions",
                    "The crossed-out choices", "The scratch work on screen"],
        "correct": "Nothing",
        "explanation": "<p><strong>Hech narsa.</strong> Belgilangan savollar "
                       "ham, oʻchirilgan variantlar ham qoladi.</p>",
    },
    {
        "text": "<p>Where should a student put the single check on the clock during "
                "a module?</p>",
        "choices": ["Around question 11", "After every question",
                    "At question 3", "Only at the very end"],
        "correct": "Around question 11",
        "explanation": "<p><strong>11-savol atrofida.</strong> Bitta nazorat "
                       "nuqtasi yetarli — har qarash eʼtiborni uzadi.</p>",
    },
    {
        "text": "<p>In the last three minutes of a module, what comes first?</p>",
        "choices": ["Filling in every blank answer",
                    "Rechecking the first questions",
                    "Solving the hardest flagged question",
                    "Reading the reference sheet"],
        "correct": "Filling in every blank answer",
        "explanation": "<p><strong>Boʻshlarni toʻldirish.</strong> Boʻsh "
                       "javobning qiymati aniq nol.</p>",
    },
    {
        "text": "<p>Should a student change answers in the final minutes?</p>",
        "choices": ["Only if a new reason has been found",
                    "Yes, first instincts are usually wrong",
                    "Yes, change any answer that feels uncertain",
                    "Never, under any circumstances"],
        "correct": "Only if a new reason has been found",
        "explanation": "<p><strong>Faqat yangi sabab topilsa.</strong> "
                       "Shoshib almashtirilgan javob koʻpincha toʻgʻrisi "
                       "edi.</p>",
    },
    {
        "text": "<p>Why is the first module especially important?</p>",
        "choices": ["It counts and it also selects the second module",
                    "It is worth double points",
                    "It is the only one that is scored",
                    "It is longer than the second"],
        "correct": "It counts and it also selects the second module",
        "explanation": "<p><strong>Ikki ish qiladi.</strong> Ballga qoʻshiladi "
                       "va keyingi modulni tanlaydi.</p>",
    },
    {
        "text": "<p>A student answers questions 1 to 11 in 15 minutes. About how many "
                "seconds per question is that?</p>",
        "choices": ["82", "95", "68", "110"],
        "correct": "82",
        "explanation": "<p><strong>82.</strong> 900 ÷ 11 ≈ 81.8 — bu yaxshi "
                       "surʼat.</p>",
    },
    {
        "text": "<p>A student has finished 16 questions after 26 minutes of a "
                "35-minute module. How many seconds are left for each of the 6 "
                "remaining questions?</p>",
        "choices": ["90", "95", "75", "120"],
        "correct": "90",
        "explanation": "<p><strong>90.</strong> 9 daqiqa qoldi — 540 soniya, "
                       "va 540 ÷ 6 = 90.</p>",
    },
]


# =====================================================================
# SAT-100 — the final review protocol
# =====================================================================

Q_SAT100 = [
    {
        "text": "<p>What are the four final checks, in order?</p>",
        "choices": ["The question, the unit, the size, the form",
                    "The unit, the question, the form, the size",
                    "The size, the form, the question, the unit",
                    "The form, the size, the unit, the question"],
        "correct": "The question, the unit, the size, the form",
        "explanation": "<p><strong>Savol · birlik · kattalik · shakl.</strong> "
                       "Tartib muhim: birinchisi eng koʻp xatoni tutadi.</p>",
    },
    {
        "text": "<p>A jacket costs $80 and is reduced by 25 percent. A student "
                "answers 20. What should the final check have caught?</p>",
        "choices": ["20 is the discount, not the sale price",
                    "The units are wrong",
                    "The answer should be negative",
                    "The percent was applied twice"],
        "correct": "20 is the discount, not the sale price",
        "explanation": "<p><strong>Birinchi nazorat.</strong> Yangi narx 60.</p>",
    },
    {
        "text": "<p>A grid-in answer is two and a half and the student types 2 1/2. "
                "Which check catches it?</p>",
        "choices": ["The form of the answer", "The question that was asked",
                    "The unit", "The size of the answer"],
        "correct": "The form of the answer",
        "explanation": "<p><strong>Shakl.</strong> Qutida 2 1/2 → 21/2 boʻlib "
                       "oʻqiladi.</p>",
    },
    {
        "text": "<p>A train's speed comes out as 1.67 kilometres per hour. Which "
                "check catches that?</p>",
        "choices": ["The size of the answer", "The form of the answer",
                    "The question that was asked", "None of them"],
        "correct": "The size of the answer",
        "explanation": "<p><strong>Kattalik.</strong> Poyezd soatiga 1.67 km "
                       "yurmaydi — birlik oʻgirilmagan.</p>",
    },
    {
        "text": "<p>A student solves for <i>x</i> but the question asked for "
                "<i>x</i> + <i>y</i>. Which check catches it?</p>",
        "choices": ["The first — the question that was asked",
                    "The second — the unit",
                    "The third — the size", "The fourth — the form"],
        "correct": "The first — the question that was asked",
        "explanation": "<p><strong>Birinchi.</strong> Oxirgi jumlani qayta "
                       "oʻqish.</p>",
    },
    {
        "text": "<p>Which block of the course covers ratios, percentages and "
                "tables?</p>",
        "choices": ["Block C, lessons 49–65", "Block A, lessons 1–22",
                    "Block D, lessons 66–80", "Block E, lessons 81–100"],
        "correct": "Block C, lessons 49–65",
        "explanation": "<p><strong>Blok C.</strong> Problem-Solving and Data "
                       "Analysis.</p>",
    },
    {
        "text": "<p>Which block covers triangles, circles and trigonometry?</p>",
        "choices": ["Block D, lessons 66–80", "Block B, lessons 23–48",
                    "Block C, lessons 49–65", "Block A, lessons 1–22"],
        "correct": "Block D, lessons 66–80",
        "explanation": "<p><strong>Blok D.</strong> Geometry and "
                       "Trigonometry.</p>",
    },
    {
        "text": "<p>Which block covers plugging in, backsolving and Desmos?</p>",
        "choices": ["Block E, lessons 81–100", "Block D, lessons 66–80",
                    "Block A, lessons 1–22", "Block B, lessons 23–48"],
        "correct": "Block E, lessons 81–100",
        "explanation": "<p><strong>Blok E.</strong> Tactics and Desmos.</p>",
    },
    {
        "text": "<p>Which block covers linear equations, lines and systems?</p>",
        "choices": ["Block A, lessons 1–22", "Block B, lessons 23–48",
                    "Block C, lessons 49–65", "Block E, lessons 81–100"],
        "correct": "Block A, lessons 1–22",
        "explanation": "<p><strong>Blok A.</strong> The Heart of Algebra.</p>",
    },
    {
        "text": "<p>Which block covers exponents, polynomials and quadratics?</p>",
        "choices": ["Block B, lessons 23–48", "Block A, lessons 1–22",
                    "Block D, lessons 66–80", "Block C, lessons 49–65"],
        "correct": "Block B, lessons 23–48",
        "explanation": "<p><strong>Blok B.</strong> Advanced Math.</p>",
    },
    {
        "text": "<p>Which three formulas must you carry in your memory?</p>",
        "choices": ["Slope, SOH-CAH-TOA and the circle equation",
                    "The five volume formulas",
                    "Circle area, circumference and triangle area",
                    "The two special right triangles"],
        "correct": "Slope, SOH-CAH-TOA and the circle equation",
        "explanation": "<p><strong>Uchtasi ham varaqda yoʻq.</strong></p>",
    },
    {
        "text": "<p>Which of the seven traps can no checking protocol catch?</p>",
        "choices": ["A wrong operation in the middle of the working",
                    "Answering a different question",
                    "A unit that was not converted",
                    "Stopping halfway"],
        "correct": "A wrong operation in the middle of the working",
        "explanation": "<p><strong>Notoʻgʻri amal.</strong> Uni faqat bilim "
                       "tutadi — shuning uchun matematika saksonta dars, "
                       "taktika yigirmata.</p>",
    },
    {
        "text": "<p>Two minutes are left and one question is blank. What do you "
                "do?</p>",
        "choices": ["Mark an answer on the blank question",
                    "Run the four checks on your last answer",
                    "Reread the first question",
                    "Leave it and stop"],
        "correct": "Mark an answer on the blank question",
        "explanation": "<p><strong>Boʻshni toʻldiring.</strong> Uning qiymati "
                       "aniq nol; tekshirish esa kutishi mumkin.</p>",
    },
    {
        "text": "<p>Is the four-check protocol worth running on a one-step "
                "question?</p>",
        "choices": ["No — it is for multi-step questions",
                    "Yes, on every question without exception",
                    "Only on geometry questions",
                    "Only in the second module"],
        "correct": "No — it is for multi-step questions",
        "explanation": "<p><strong>Yoʻq.</strong> «What is 10 percent of 50?» "
                       "uchun toʻrtta savol ortiqcha.</p>",
    },
    {
        "text": "<p>After a practice test, what is the most useful thing to do with "
                "your mistakes?</p>",
        "choices": ["Sort them by block and by trap type",
                    "Reread the whole course",
                    "Count how many you got wrong",
                    "Retake the same test immediately"],
        "correct": "Sort them by block and by trap type",
        "explanation": "<p><strong>Blok va tuzoq turiga ajrating.</strong> "
                       "Ikkita roʻyxat qaysi darsga qaytish kerakligini "
                       "aytadi.</p>",
    },
    {
        "text": "<p>A jacket costs $80 and is reduced by 25 percent. What is the sale "
                "price?</p>",
        "choices": ["$60", "$20", "$100", "$55"],
        "correct": "$60",
        "explanation": "<p><strong>$60.</strong> Toʻrtdan uchi qoladi.</p>",
    },
    {
        "text": "<p>A probability comes out as 1.4. Which check catches it?</p>",
        "choices": ["The size of the answer", "The unit",
                    "The form of the answer", "The question that was asked"],
        "correct": "The size of the answer",
        "explanation": "<p><strong>Kattalik.</strong> Ehtimollik 0 bilan 1 "
                       "orasida boʻladi.</p>",
    },
    {
        "text": "<p>The answer is given in minutes but the question asked for hours. "
                "Which check catches it?</p>",
        "choices": ["The unit", "The size", "The form",
                    "The question that was asked"],
        "correct": "The unit",
        "explanation": "<p><strong>Birlik.</strong> Ikkinchi nazorat.</p>",
    },
    {
        "text": "<p>What is the single sentence to ask yourself before marking any "
                "answer?</p>",
        "choices": ["\"What did it ask for?\"", "\"Is this the easy answer?\"",
                    "\"How long did that take?\"", "\"Should I guess instead?\""],
        "correct": "\"What did it ask for?\"",
        "explanation": "<p><strong>«U nimani soʻragan edi?»</strong> Yuz "
                       "darsning oxirgi jumlasi.</p>",
    },
    {
        "text": "<p>A group of 15 people includes 8 adults. The question asks how "
                "many children there are, and the student marks 8. Which check would "
                "have caught it?</p>",
        "choices": ["The first — the question that was asked",
                    "The second — the unit",
                    "The third — the size", "The fourth — the form"],
        "correct": "The first — the question that was asked",
        "explanation": "<p><strong>Birinchi.</strong> Bolalar soni 7 — "
                       "hisob toʻgʻri, javob notoʻgʻri odamlar guruhi "
                       "uchun.</p>",
    },
]


PRACTICES = [
    {
        "title":       'SAT-96 Practice: The "Testing the Boundaries" Tactic (Domain and Range)',
        "description": "20 ta SAT uslubidagi savol — domain va range, taqiqlaydigan "
                       "uch narsa, parabolaning chegarasi, hayotiy maʼno.",
        "tutorial":    "SAT-96:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT96,
    },
    {
        "title":       "SAT-97 Practice: Data Table Extraction",
        "description": "20 ta SAT uslubidagi savol — qaysi jamini maxraj qilish, "
                       "«of the …» iborasi, yetishmayotgan katak, birlik.",
        "tutorial":    "SAT-97:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT97,
    },
    {
        "title":       "SAT-98 Practice: The Formula Sheet Hack",
        "description": "20 ta SAT uslubidagi savol — varaqda nima bor va nima yoʻq, "
                       "beshta hajm formulasi, konus va piramidadagi uchdan bir.",
        "tutorial":    "SAT-98:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT98,
    },
    {
        "title":       "SAT-99 Practice: Pacing for Module 2 (The Adaptive Test)",
        "description": "20 ta SAT uslubidagi savol — testning raqamlari, vaqt banki, "
                       "moslashuv, va nima uchun boʻsh qoldirilmaydi.",
        "tutorial":    "SAT-99:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT99,
    },
    {
        "title":       "SAT-100 Practice: The Final Review Protocol (30-Second Double-Check)",
        "description": "20 ta SAT uslubidagi savol — toʻrtta nazorat, yuz darsning "
                       "xaritasi, yodlanadigan uchta formula. Kursning oxirgi mashqi.",
        "tutorial":    "SAT-100:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT100,
    },
]
