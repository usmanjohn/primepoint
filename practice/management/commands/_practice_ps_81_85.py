# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-81 … SAT-85 (Blok E: taktika va Desmos).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.
⚠️ Javob har doim "correct" da va choices ning BIRINCHISIDA turadi.
⚠️ Blok E matematika oʻrgatmaydi — savollardagi matematika ILGARIGI
   darslardan olinadi, sinaladigan narsa esa USUL.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_81_85.py --master=prime \\
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
# SAT-81 — plugging in numbers
# =====================================================================

Q_SAT81 = [
    {
        "text": "<p>A price of <i>p</i> dollars is reduced by 10 percent. Which "
                "expression gives the new price?</p>",
        "choices": ["0.9<i>p</i>", "<i>p</i> − 0.1", "1.1<i>p</i>", "0.1<i>p</i>"],
        "correct": "0.9<i>p</i>",
        "explanation": "<p><strong>0.9p.</strong> p = 100 qoʻying: 10 foiz — 10 dollar, "
                       "yangi narx 90. Faqat 0.9p 90 beradi.</p>"
                       "<p><strong>p − 0.1</strong> — foizni oddiy son deb "
                       "olgan: 99.90.</p>",
    },
    {
        "text": "<p>A price of <i>p</i> dollars is increased by 25 percent. Which "
                "expression gives the new price?</p>",
        "choices": ["1.25<i>p</i>", "<i>p</i> + 0.25", "0.25<i>p</i>", "0.75<i>p</i>"],
        "correct": "1.25<i>p</i>",
        "explanation": "<p><strong>1.25p.</strong> p = 100 → 125.</p>"
                       "<p><strong>0.25p</strong> — bu qoʻshilgan qism, butun "
                       "narx emas.</p>",
    },
    {
        "text": "<p>Which number is the worst choice to plug in when the answer "
                "choices contain exponents?</p>",
        "choices": ["1", "4", "5", "7"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> 1 ning har qanday darajasi 1 — "
                       "darajasi farq qiladigan variantlar bir xil chiqadi.</p>",
    },
    {
        "text": "<p>The sum of three consecutive integers is <i>n</i>. In terms of "
                "<i>n</i>, what is the smallest of the three?</p>",
        "choices": ["(<i>n</i> − 3)/3", "<i>n</i>/3", "(<i>n</i> + 3)/3",
                    "<i>n</i>/3 − 3"],
        "correct": "(<i>n</i> − 3)/3",
        "explanation": "<p><strong>(n − 3)/3.</strong> 4, 5, 6 ni oling: n = 15, eng "
                       "kichigi 4, va (15 − 3)/3 = 4 ✓</p>"
                       "<p><strong>n/3</strong> — bu oʻrtadagi son (5).</p>",
    },
    {
        "text": "<p>The sum of three consecutive integers is <i>n</i>. In terms of "
                "<i>n</i>, what is the largest of the three?</p>",
        "choices": ["(<i>n</i> + 3)/3", "<i>n</i>/3", "(<i>n</i> − 3)/3",
                    "3<i>n</i> + 3"],
        "correct": "(<i>n</i> + 3)/3",
        "explanation": "<p><strong>(n + 3)/3.</strong> 4, 5, 6 → n = 15, eng "
                       "kattasi 6, va (15 + 3)/3 = 6 ✓</p>",
    },
    {
        "text": "<p>If <i>x</i> is 3 more than <i>y</i>, which expression gives "
                "<i>y</i> in terms of <i>x</i>?</p>",
        "choices": ["<i>x</i> − 3", "<i>x</i> + 3", "3 − <i>x</i>", "3<i>x</i>"],
        "correct": "<i>x</i> − 3",
        "explanation": "<p><strong>x − 3.</strong> y = 10 boʻlsa x = 13; 13 − 3 = 10 ✓</p>"
                       "<p><strong>x + 3</strong> — yoʻnalish teskari olingan.</p>",
    },
    {
        "text": "<p>A rectangle has width <i>w</i> and length 2<i>w</i>. Which "
                "expression gives its perimeter?</p>",
        "choices": ["6<i>w</i>", "3<i>w</i>", "2<i>w</i>²", "4<i>w</i>"],
        "correct": "6<i>w</i>",
        "explanation": "<p><strong>6w.</strong> w = 5 qoʻying: tomonlar 5 va 10, "
                       "perimetr 30 = 6 × 5 ✓</p>"
                       "<p><strong>3w</strong> — faqat bitta uzunlik va bitta "
                       "en qoʻshilgan.</p>",
    },
    {
        "text": "<p>A rectangle has width <i>w</i> and length 2<i>w</i>. Which "
                "expression gives its area?</p>",
        "choices": ["2<i>w</i>²", "6<i>w</i>", "<i>w</i>²", "4<i>w</i>²"],
        "correct": "2<i>w</i>²",
        "explanation": "<p><strong>2w².</strong> w = 5 → 5 × 10 = 50 = 2 × 25 ✓</p>",
    },
    {
        "text": "<p>Which number is usually best to plug in for a question about "
                "percentages?</p>",
        "choices": ["100", "1", "0", "10"],
        "correct": "100",
        "explanation": "<p><strong>100.</strong> Har qanday foiz darrov butun "
                       "son beradi va kasr chiqmaydi.</p>",
    },
    {
        "text": "<p>Which expression represents half of a number <i>n</i>, "
                "decreased by 4?</p>",
        "choices": ["<i>n</i>/2 − 4", "(<i>n</i> − 4)/2", "2<i>n</i> − 4",
                    "<i>n</i>/2 + 4"],
        "correct": "<i>n</i>/2 − 4",
        "explanation": "<p><strong>n/2 − 4.</strong> n = 10 → yarmi 5, keyin 4 kam: 1.</p>"
                       "<p><strong>(n − 4)/2</strong> — avval ayirib, keyin "
                       "boʻlgan: 3.</p>",
    },
    {
        "text": "<p>If <i>a</i> = 2<i>b</i> and <i>b</i> = 3<i>c</i>, which "
                "expression gives <i>a</i> in terms of <i>c</i>?</p>",
        "choices": ["6<i>c</i>", "5<i>c</i>", "<i>c</i>/6", "2<i>c</i>/3"],
        "correct": "6<i>c</i>",
        "explanation": "<p><strong>6c.</strong> c = 2 qoʻying: b = 6, a = 12 = 6 × 2 ✓</p>"
                       "<p><strong>5c</strong> — koeffitsiyentlar qoʻshilgan, "
                       "koʻpaytirilmagan.</p>",
    },
    {
        "text": "<p>A shop sells <i>n</i> items at <i>d</i> dollars each and takes "
                "$5 off the total. Which expression gives the amount paid?</p>",
        "choices": ["<i>nd</i> − 5", "<i>n</i>(<i>d</i> − 5)", "<i>nd</i> + 5",
                    "(<i>n</i> − 5)<i>d</i>"],
        "correct": "<i>nd</i> − 5",
        "explanation": "<p><strong>nd − 5.</strong> n = 3, d = 10 → 30 dan 5 kam: 25.</p>"
                       "<p><strong>n(d − 5)</strong> — chegirma har bir "
                       "narsadan olingan: 15.</p>",
    },
    {
        "text": "<p>When should you NOT use the plugging-in tactic?</p>",
        "choices": ["When the answer choices are numbers",
                    "When the answer choices contain letters",
                    "When the question mentions percentages",
                    "When the question is about geometry"],
        "correct": "When the answer choices are numbers",
        "explanation": "<p><strong>Javoblar son boʻlganda.</strong> U holda "
                       "backsolving kerak (SAT-82).</p>",
    },
    {
        "text": "<p>Which expression represents twice the sum of <i>x</i> and 5?</p>",
        "choices": ["2<i>x</i> + 10", "2<i>x</i> + 5", "<i>x</i> + 10",
                    "2<i>x</i> − 10"],
        "correct": "2<i>x</i> + 10",
        "explanation": "<p><strong>2x + 10.</strong> x = 3 → yigʻindi 8, ikki "
                       "barobari 16 = 2(3) + 10 ✓</p>"
                       "<p><strong>2x + 5</strong> — faqat x ikkilangan.</p>",
    },
    {
        "text": "<p>Every answer choice contains the letter <i>k</i>. Which tactic "
                "fits?</p>",
        "choices": ["Plugging in a number for <i>k</i>",
                    "Backsolving from the choices",
                    "Grid-in estimation",
                    "Eyeballing the diagram"],
        "correct": "Plugging in a number for <i>k</i>",
        "explanation": "<p><strong>Son qoʻyish.</strong> Harfli javoblar — bu "
                       "taktikaning yagona belgisi.</p>",
    },
    {
        "text": "<p><i>n</i> is an even integer. Which expression is always odd?</p>",
        "choices": ["<i>n</i> + 1", "<i>n</i> + 2", "2<i>n</i>", "<i>n</i>/2"],
        "correct": "<i>n</i> + 1",
        "explanation": "<p><strong>n + 1.</strong> n = 4, 6, 10 — hammasida "
                       "toq chiqadi.</p>"
                       "<p><strong>n/2</strong> — n = 4 da 2 (juft), n = 6 da "
                       "3 (toq): har doim emas.</p>",
    },
    {
        "text": "<p>A car travels at 60 kilometres per hour for <i>t</i> hours. "
                "Which expression gives the distance in kilometres?</p>",
        "choices": ["60<i>t</i>", "60/<i>t</i>", "<i>t</i>/60", "60 + <i>t</i>"],
        "correct": "60<i>t</i>",
        "explanation": "<p><strong>60t.</strong> t = 2 → 120 km ✓</p>",
    },
    {
        "text": "<p>The average of <i>x</i>, <i>y</i> and <i>z</i> is <i>m</i>. "
                "Which expression gives <i>x</i> + <i>y</i> + <i>z</i>?</p>",
        "choices": ["3<i>m</i>", "<i>m</i>/3", "<i>m</i> + 3", "<i>m</i>"],
        "correct": "3<i>m</i>",
        "explanation": "<p><strong>3m.</strong> 2, 4, 6 ni oling: oʻrtacha 4, "
                       "yigʻindi 12 = 3 × 4 ✓</p>",
    },
    {
        "text": "<p>A number is increased by 20 percent and then the result is "
                "decreased by 20 percent. Which expression gives the final value?</p>",
        "choices": ["0.96<i>n</i>", "<i>n</i>", "1.04<i>n</i>", "0.8<i>n</i>"],
        "correct": "0.96<i>n</i>",
        "explanation": "<p><strong>0.96n.</strong> n = 100 qoʻying: 120, keyin "
                       "120 ning 20 foizi 24, demak 96.</p>"
                       "<p><strong>n</strong> — «koʻtardik va tushirdik, demak "
                       "joyida» degan tuzoq. Ikkinchi foiz kattaroq sondan "
                       "olinadi.</p>",
    },
    {
        "text": "<p>A taxi charges $3 plus $2 for each kilometre travelled. Which "
                "expression gives the cost of a trip of <i>k</i> kilometres?</p>",
        "choices": ["3 + 2<i>k</i>", "2 + 3<i>k</i>", "5<i>k</i>", "6<i>k</i>"],
        "correct": "3 + 2<i>k</i>",
        "explanation": "<p><strong>3 + 2k.</strong> k = 4 qoʻying: 3 + 8 = 11.</p>"
                       "<p><strong>5k</strong> — ikkala sonni qoʻshib, hammasini "
                       "kilometrga koʻpaytirgan: 20.</p>",
    },
]


# =====================================================================
# SAT-82 — backsolving
# =====================================================================

Q_SAT82 = [
    {
        "text": "<p>If 2(<i>x</i> + 5) + 3<i>x</i> = 35, what is the value of "
                "<i>x</i>?</p>",
        "choices": ["5", "6", "7", "9"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 2(10) + 15 = 35 ✓</p>"
                       "<p><strong>6</strong> — qavsda 5 ni 2 ga koʻpaytirmagan: "
                       "2x + 5 + 3x = 35 → x = 6. Sinab koʻrsangiz 40 chiqadi.</p>",
    },
    {
        "text": "<p>If 3(<i>x</i> − 4) + 2<i>x</i> = 23, what is the value of "
                "<i>x</i>?</p>",
        "choices": ["7", "5", "9", "11"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 3(3) + 14 = 23 ✓</p>",
    },
    {
        "text": "<p>If 2(<i>x</i> + 3) = 20, what is the value of <i>x</i>?</p>",
        "choices": ["7", "4", "10", "13"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 2(10) = 20 ✓</p>"
                       "<p><strong>10</strong> — 20 ni 2 ga boʻlgan, lekin 3 ni "
                       "ayirmagan.</p>",
    },
    {
        "text": "<p>Backsolving is fastest when you begin with which choice?</p>",
        "choices": ["The middle one", "The first one", "The last one",
                    "The largest one"],
        "correct": "The middle one",
        "explanation": "<p><strong>Oʻrtadagi.</strong> Katta yoki kichik "
                       "chiqishiga qarab yarmini bir urinishda kesasiz.</p>",
    },
    {
        "text": "<p>Tickets cost $12 for an adult and $7 for a child. A group of 15 "
                "people paid $145 in total. How many adults were in the group?</p>",
        "choices": ["8", "7", "9", "10"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> 8 × 12 + 7 × 7 = 96 + 49 = 145 ✓</p>"
                       "<p><strong>7</strong> — bu bolalar soni; savol "
                       "kattalarni soʻragan.</p>",
    },
    {
        "text": "<p>Tickets cost $12 for an adult and $7 for a child. A group of 20 "
                "people paid $190 in total. How many adults were in the group?</p>",
        "choices": ["10", "8", "12", "9"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 10 × 12 + 10 × 7 = 190 ✓</p>"
                       "<p><strong>8</strong> berardi 96 + 84 = 180 — kam.</p>",
    },
    {
        "text": "<p>If 5<i>x</i> − 3 = 2<i>x</i> + 12, what is the value of "
                "<i>x</i>?</p>",
        "choices": ["5", "3", "7", "9"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 25 − 3 = 22 va 10 + 12 = 22 ✓</p>",
    },
    {
        "text": "<p>If <i>x</i>/3 + 4 = 10, what is the value of <i>x</i>?</p>",
        "choices": ["18", "6", "12", "24"],
        "correct": "18",
        "explanation": "<p><strong>18.</strong> 6 + 4 = 10 ✓</p>"
                       "<p><strong>6</strong> — 10 − 4 topilgan, lekin 3 ga "
                       "koʻpaytirilmagan.</p>",
    },
    {
        "text": "<p>You test the middle choice and the result is too large. What do "
                "you do next?</p>",
        "choices": ["Eliminate it and every larger choice",
                    "Eliminate it and every smaller choice",
                    "Start again from the first choice",
                    "Choose the largest remaining choice"],
        "correct": "Eliminate it and every larger choice",
        "explanation": "<p><strong>Uni va undan kattalarini oʻchiring.</strong> "
                       "Bitta urinish yarmini kesadi.</p>",
    },
    {
        "text": "<p>Which type of question cannot be backsolved?</p>",
        "choices": ["A grid-in question", "A word problem",
                    "A linear equation", "A question about percentages"],
        "correct": "A grid-in question",
        "explanation": "<p><strong>Grid-in.</strong> Sinab koʻriladigan variant "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>A number plus twice that number equals 27. What is the number?</p>",
        "choices": ["9", "8", "12", "27"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> 9 + 18 = 27 ✓</p>",
    },
    {
        "text": "<p>If (<i>x</i> − 2)² = 25 and <i>x</i> &gt; 0, what is the value "
                "of <i>x</i>?</p>",
        "choices": ["7", "3", "5", "23"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> (7 − 2)² = 25 ✓</p>"
                       "<p><strong>5</strong> — ildizni toʻgʻridan-toʻgʻri "
                       "javob deb olgan; (5 − 2)² = 9.</p>",
    },
    {
        "text": "<p>If 4<i>x</i> − 7 = 2<i>x</i> + 9, what is the value of "
                "<i>x</i>?</p>",
        "choices": ["8", "6", "10", "4"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> 32 − 7 = 25 va 16 + 9 = 25 ✓</p>",
    },
    {
        "text": "<p>A rectangle's length is 3 more than its width, and its perimeter "
                "is 26. What is the width?</p>",
        "choices": ["5", "4", "6", "8"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> En 5, uzunlik 8, perimetr "
                       "2(5 + 8) = 26 ✓</p>"
                       "<p><strong>8</strong> — bu uzunlik; savol enni "
                       "soʻragan.</p>",
    },
    {
        "text": "<p>Pens cost $3 each and notebooks cost $5 each. A student bought "
                "12 items in total for $50. How many pens did she buy?</p>",
        "choices": ["5", "6", "7", "4"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 5 × 3 + 7 × 5 = 15 + 35 = 50 ✓</p>"
                       "<p><strong>7</strong> — bu daftarlar soni.</p>",
    },
    {
        "text": "<p>Four choices are listed in increasing order. You test the "
                "second one and it is too small. How many choices remain "
                "possible?</p>",
        "choices": ["2", "1", "3", "4"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Ikkinchisi va undan kichigi "
                       "chiqib ketadi; uchinchi va toʻrtinchi qoladi.</p>",
    },
    {
        "text": "<p>Which of the following is a solution to 3<i>x</i> − 5 &gt; 7?</p>",
        "choices": ["6", "4", "3", "2"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 18 − 5 = 13 &gt; 7 ✓</p>"
                       "<p><strong>4</strong> — 7 chiqadi, va 7 &gt; 7 "
                       "notoʻgʻri: chegara kirmaydi.</p>",
    },
    {
        "text": "<p>If <i>x</i>² − <i>x</i> = 12 and <i>x</i> &gt; 0, what is the "
                "value of <i>x</i>?</p>",
        "choices": ["4", "3", "6", "12"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 16 − 4 = 12 ✓</p>",
    },
    {
        "text": "<p>Why is testing a choice usually safer than solving the "
                "equation?</p>",
        "choices": ["Testing uses only arithmetic, with no rearranging",
                    "Testing is always faster",
                    "The first choice is usually correct",
                    "Equations cannot be solved without a calculator"],
        "correct": "Testing uses only arithmetic, with no rearranging",
        "explanation": "<p><strong>Faqat arifmetika.</strong> Had koʻchirish va "
                       "ishora almashtirish yoʻq — demak xato qiladigan joy "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>A group bought 14 tickets, some at $8 and the rest at $6, "
                "paying $96 in total. How many $8 tickets did they buy?</p>",
        "choices": ["6", "8", "7", "5"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 6 × 8 + 8 × 6 = 48 + 48 = 96 ✓</p>"
                       "<p><strong>8</strong> — bu $6 lik chiptalar soni.</p>",
    },
]


# =====================================================================
# SAT-83 — Desmos I
# =====================================================================

Q_SAT83 = [
    {
        "text": "<p>You graph <i>y</i> = 3<i>x</i> + 5 and <i>y</i> = <i>x</i> + 11. "
                "At what value of <i>x</i> do they intersect?</p>",
        "choices": ["3", "14", "5", "11"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Kesishish (3, 14) da: 14 = 14 ✓</p>"
                       "<p><strong>14</strong> — bu y koordinatasi.</p>",
    },
    {
        "text": "<p>The graphs of <i>y</i> = 3<i>x</i> + 5 and <i>y</i> = <i>x</i> + 11 "
                "meet at one point. What is its <i>y</i>-coordinate?</p>",
        "choices": ["14", "3", "8", "16"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> 3(3) + 5 = 14.</p>",
    },
    {
        "text": "<p>What are the zeros of <i>y</i> = <i>x</i>² − 5<i>x</i> + 6?</p>",
        "choices": ["2 and 3", "−2 and −3", "5 and 6", "1 and 6"],
        "correct": "2 and 3",
        "explanation": "<p><strong>2 va 3.</strong> Grafik x oʻqini shu ikki "
                       "nuqtada kesadi.</p>",
    },
    {
        "text": "<p>The system <i>y</i> = 2<i>x</i> − 1 and <i>y</i> = −<i>x</i> + 5 "
                "has solution (<i>x</i>, <i>y</i>). What is <i>x</i> + <i>y</i>?</p>",
        "choices": ["5", "2", "3", "−1"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Kesishish (2, 3), demak 2 + 3 = 5.</p>"
                       "<p><strong>2</strong> — faqat x. Desmos nuqtani beradi, "
                       "savolni oʻzingiz oʻqiysiz.</p>",
    },
    {
        "text": "<p>What is the positive solution to <i>x</i>² − 4 = 3<i>x</i>?</p>",
        "choices": ["4", "−1", "3", "1"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 16 − 4 = 12 va 3 × 4 = 12 ✓</p>"
                       "<p><strong>−1</strong> — u ham yechim, lekin manfiy.</p>",
    },
    {
        "text": "<p>To solve an equation with Desmos, what should you do first?</p>",
        "choices": ["Graph each side as its own function",
                    "Type the whole equation on one line and press enter",
                    "Add a slider",
                    "Switch to degrees mode"],
        "correct": "Graph each side as its own function",
        "explanation": "<p><strong>Har bir tomonni alohida grafik qiling.</strong> "
                       "Yechim ular kesishgan joyda.</p>",
    },
    {
        "text": "<p>Desmos shows nothing on the screen. What should you try "
                "first?</p>",
        "choices": ["Zoom out", "Restart the app",
                    "Switch to radians", "Add a slider"],
        "correct": "Zoom out",
        "explanation": "<p><strong>Uzoqlashtirish.</strong> Yechim ekrandan "
                       "tashqarida boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>You type sin(30) into Desmos and get about −0.988. Why?</p>",
        "choices": ["Desmos is working in radians",
                    "The sine of 30 degrees really is negative",
                    "You must type sin(30x)",
                    "Desmos rounds to three decimal places"],
        "correct": "Desmos is working in radians",
        "explanation": "<p><strong>Radianda.</strong> 30 radianning sinusi "
                       "hisoblangan, 30 daraja emas.</p>",
    },
    {
        "text": "<p>What are the zeros of <i>y</i> = <i>x</i>² − 7<i>x</i> + 12?</p>",
        "choices": ["3 and 4", "−3 and −4", "7 and 12", "2 and 6"],
        "correct": "3 and 4",
        "explanation": "<p><strong>3 va 4.</strong> Koʻpaytmasi 12, yigʻindisi 7.</p>",
    },
    {
        "text": "<p>Solve 5<i>x</i> − 2 = 2<i>x</i> + 7 by graphing.</p>",
        "choices": ["<i>x</i> = 3", "<i>x</i> = 9", "<i>x</i> = 13",
                    "<i>x</i> = 5"],
        "correct": "<i>x</i> = 3",
        "explanation": "<p><strong>3.</strong> Ikkala tomon x = 3 da 13 ga teng.</p>",
    },
    {
        "text": "<p>Which point lies on the graph of <i>y</i> = 2<i>x</i> + 1?</p>",
        "choices": ["(3, 7)", "(3, 6)", "(2, 6)", "(1, 4)"],
        "correct": "(3, 7)",
        "explanation": "<p><strong>(3, 7).</strong> 2(3) + 1 = 7 ✓ Desmosda "
                       "nuqtani kiritsangiz, u chiziq ustida turadi.</p>",
    },
    {
        "text": "<p>A system's graphs meet at (4, −2). What is <i>y</i> − "
                "<i>x</i>?</p>",
        "choices": ["−6", "6", "2", "−2"],
        "correct": "−6",
        "explanation": "<p><strong>−6.</strong> −2 − 4 = −6.</p>"
                       "<p><strong>6</strong> — tartib almashtirilgan.</p>",
    },
    {
        "text": "<p>Where does the graph of <i>y</i> = <i>x</i>² − 4 cross the "
                "<i>x</i>-axis?</p>",
        "choices": ["−2 and 2", "0 and 4", "−4 and 4", "It does not cross"],
        "correct": "−2 and 2",
        "explanation": "<p><strong>−2 va 2.</strong> Ikkalasining kvadrati 4.</p>",
    },
    {
        "text": "<p>A question shows a graph and asks which of four equations it "
                "could be. What is the fastest use of Desmos?</p>",
        "choices": ["Enter all four and toggle them on and off",
                    "Enter only the first one",
                    "Add a slider to each",
                    "Zoom in as far as possible"],
        "correct": "Enter all four and toggle them on and off",
        "explanation": "<p><strong>Toʻrttasini ham kiriting.</strong> Chap "
                       "tomondagi doirachani bosib yoqib-oʻchirasiz.</p>",
    },
    {
        "text": "<p>What are the solutions to <i>x</i>² = 9?</p>",
        "choices": ["−3 and 3", "3 only", "9 only", "−9 and 9"],
        "correct": "−3 and 3",
        "explanation": "<p><strong>−3 va 3.</strong> Grafikda ikkita kesishish "
                       "koʻrinadi — manfiysini unutmang.</p>",
    },
    {
        "text": "<p>At how many points does the graph of <i>y</i> = <i>x</i>² + 1 "
                "cross the <i>x</i>-axis?</p>",
        "choices": ["0", "1", "2", "3"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Parabolaning eng past nuqtasi "
                       "y = 1 da, demak u x oʻqiga yetmaydi.</p>",
    },
    {
        "text": "<p>At what value of <i>x</i> do <i>y</i> = <i>x</i> and "
                "<i>y</i> = −<i>x</i> intersect?</p>",
        "choices": ["0", "1", "−1", "They never intersect"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Faqat boshlangʻich nuqtada, "
                       "(0, 0).</p>",
    },
    {
        "text": "<p>Solve 2<i>x</i> + 6 = 0 by graphing.</p>",
        "choices": ["<i>x</i> = −3", "<i>x</i> = 3", "<i>x</i> = 6",
                    "<i>x</i> = −6"],
        "correct": "<i>x</i> = −3",
        "explanation": "<p><strong>−3.</strong> Chiziq x oʻqini −3 da kesadi.</p>",
    },
    {
        "text": "<p>For which question is Desmos clearly faster than working by "
                "hand?</p>",
        "choices": ["A system of two equations", "Solving 3<i>x</i> = 12",
                    "Adding 15 and 27", "Finding 10 percent of 80"],
        "correct": "A system of two equations",
        "explanation": "<p><strong>Sistema.</strong> Oddiy savolda kiritishning "
                       "oʻzi qoʻlda yechishdan uzoqroq davom etadi.</p>",
    },
    {
        "text": "<p>A workshop's costs are 200 + 4<i>n</i> dollars and its revenue "
                "is 12<i>n</i> dollars, where <i>n</i> is the number of items sold. "
                "At what value of <i>n</i> are they equal?</p>",
        "choices": ["25", "20", "50", "16"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Ikki chiziqni chizing: kesishish "
                       "n = 25 da, ikkalasi ham 300 dollar.</p>"
                       "<p><strong>50</strong> — 200 ni 4 ga boʻlgan.</p>",
    },
]


# =====================================================================
# SAT-84 — sliders
# =====================================================================

Q_SAT84 = [
    {
        "text": "<p>The graph of <i>y</i> = <i>a</i><i>x</i>² passes through "
                "(2, 12). What is the value of <i>a</i>?</p>",
        "choices": ["3", "6", "12", "1/3"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> 12 = a × 4.</p>"
                       "<p><strong>6</strong> — 12 ni 2 ga boʻlgan; x avval "
                       "kvadratga koʻtariladi.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = <i>a</i><i>x</i>² passes through "
                "(3, 18). What is the value of <i>a</i>?</p>",
        "choices": ["2", "6", "18", "3"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> 18 = a × 9.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = <i>a</i><i>x</i>² passes through "
                "(2, −8). What is the value of <i>a</i>?</p>",
        "choices": ["−2", "2", "−4", "−8"],
        "correct": "−2",
        "explanation": "<p><strong>−2.</strong> −8 = a × 4. Manfiy a parabolani "
                       "pastga qaratadi.</p>",
    },
    {
        "text": "<p>For what value of <i>k</i> does the line <i>y</i> = <i>k</i> "
                "intersect <i>y</i> = <i>x</i>² − 4<i>x</i> + 3 at exactly one "
                "point?</p>",
        "choices": ["−1", "3", "2", "1"],
        "correct": "−1",
        "explanation": "<p><strong>−1.</strong> Uchning balandligi: x = 2 da "
                       "y = 4 − 8 + 3 = −1.</p>"
                       "<p><strong>2</strong> — bu uchning x koordinatasi.</p>",
    },
    {
        "text": "<p>For what value of <i>k</i> does the line <i>y</i> = <i>k</i> "
                "touch <i>y</i> = <i>x</i>² − 6<i>x</i> + 5 at exactly one "
                "point?</p>",
        "choices": ["−4", "3", "5", "−6"],
        "correct": "−4",
        "explanation": "<p><strong>−4.</strong> Uch x = 3 da: 9 − 18 + 5 = −4.</p>",
    },
    {
        "text": "<p>Desmos offers to add a slider when you type which of the "
                "following?</p>",
        "choices": ["A letter other than <i>x</i> or <i>y</i>",
                    "Any equation at all", "A pair of coordinates",
                    "An inequality"],
        "correct": "A letter other than <i>x</i> or <i>y</i>",
        "explanation": "<p><strong>x va y dan boshqa harf.</strong> Ular "
                       "oʻzgaruvchi, doimiy emas.</p>",
    },
    {
        "text": "<p>Your slider reads 0.25. Which fraction is that?</p>",
        "choices": ["1/4", "1/2", "2/5", "1/5"],
        "correct": "1/4",
        "explanation": "<p><strong>1/4.</strong> Javob variantlari kasr "
                       "boʻlgani uchun oʻnlini qaytarish kerak.</p>",
    },
    {
        "text": "<p>Your slider reads 0.75. Which fraction is that?</p>",
        "choices": ["3/4", "7/5", "1/3", "2/3"],
        "correct": "3/4",
        "explanation": "<p><strong>3/4.</strong></p>",
    },
    {
        "text": "<p>For the graph of <i>y</i> = <i>x</i>² − 4<i>x</i> + 3, the line "
                "<i>y</i> = <i>k</i> has NO intersection when</p>",
        "choices": ["<i>k</i> &lt; −1", "<i>k</i> &gt; −1", "<i>k</i> = −1",
                    "<i>k</i> &gt; 3"],
        "correct": "<i>k</i> &lt; −1",
        "explanation": "<p><strong>k &lt; −1.</strong> Chiziq parabolaning "
                       "uchidan pastda qolsa, ular uchrashmaydi.</p>",
    },
    {
        "text": "<p>For the same graph, the line <i>y</i> = <i>k</i> crosses it "
                "TWICE when</p>",
        "choices": ["<i>k</i> &gt; −1", "<i>k</i> &lt; −1", "<i>k</i> = −1",
                    "<i>k</i> = 0 only"],
        "correct": "<i>k</i> &gt; −1",
        "explanation": "<p><strong>k &gt; −1.</strong> Uchdan yuqoridagi har "
                       "qanday gorizontal chiziq ikki marta kesadi.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = <i>a</i><i>x</i> + 3 passes through "
                "(2, 11). What is <i>a</i>?</p>",
        "choices": ["4", "8", "11", "5.5"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 2a + 3 = 11, demak 2a = 8.</p>"
                       "<p><strong>8</strong> — 3 ni ayirgan, lekin 2 ga "
                       "boʻlmagan.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = <i>a</i><i>x</i>² passes through "
                "(1, 5). What is <i>a</i>?</p>",
        "choices": ["5", "1", "1/5", "25"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 5 = a × 1.</p>",
    },
    {
        "text": "<p>Two answer choices are 0.33 and 0.35, and your slider sits "
                "between them. What should you do?</p>",
        "choices": ["Confirm the value by hand",
                    "Choose the larger one", "Choose the smaller one",
                    "Drag the slider faster"],
        "correct": "Confirm the value by hand",
        "explanation": "<p><strong>Qoʻlda tasdiqlang.</strong> Surgich taxmin "
                       "beradi, isbot emas.</p>",
    },
    {
        "text": "<p>What is the vertex of <i>y</i> = <i>x</i>² − 4<i>x</i> + 3?</p>",
        "choices": ["(2, −1)", "(−2, 1)", "(2, 3)", "(1, 3)"],
        "correct": "(2, −1)",
        "explanation": "<p><strong>(2, −1).</strong> Bu SAT-84 dagi «bitta "
                       "yechim» savolining javobi turgan joy.</p>",
    },
    {
        "text": "<p>What is the vertex of <i>y</i> = <i>x</i>² − 6<i>x</i> + 5?</p>",
        "choices": ["(3, −4)", "(−3, 4)", "(3, 5)", "(6, 5)"],
        "correct": "(3, −4)",
        "explanation": "<p><strong>(3, −4).</strong> x = 3 da 9 − 18 + 5 = −4.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = <i>x</i>² + <i>k</i> passes through "
                "(2, 7). What is <i>k</i>?</p>",
        "choices": ["3", "7", "4", "−3"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> 4 + k = 7.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = <i>a</i>(<i>x</i> − 1)² passes through "
                "(3, 12). What is <i>a</i>?</p>",
        "choices": ["3", "4", "6", "12"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> (3 − 1)² = 4, demak 4a = 12.</p>"
                       "<p><strong>4</strong> — qavs ichidagi kvadratning "
                       "oʻzi.</p>",
    },
    {
        "text": "<p>A question has two unknown constants and two conditions. How "
                "should you use the two sliders?</p>",
        "choices": ["Satisfy one condition first, then the other",
                    "Drag both at the same time",
                    "Set both to zero and read the graph",
                    "Use only the first slider"],
        "correct": "Satisfy one condition first, then the other",
        "explanation": "<p><strong>Birma-bir.</strong> Ikkalasini birga "
                       "surganda ilgari topilgan shart buziladi.</p>",
    },
    {
        "text": "<p>For what value of <i>k</i> does <i>y</i> = <i>k</i> meet "
                "<i>y</i> = <i>x</i>² at exactly one point?</p>",
        "choices": ["0", "1", "−1", "2"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Parabolaning uchi (0, 0) da.</p>"
                       "<p><strong>−1</strong> — bu chiziq parabolaning "
                       "pastida qoladi va umuman kesmaydi.</p>",
    },
    {
        "text": "<p>A ball's height in metres is modelled by <i>h</i> = "
                "−5<i>t</i>² + <i>kt</i>, where <i>t</i> is in seconds. The ball "
                "returns to the ground at <i>t</i> = 4. What is <i>k</i>?</p>",
        "choices": ["20", "5", "16", "80"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> t = 4 da balandlik nol: "
                       "−5(16) + 4k = 0, demak 4k = 80.</p>"
                       "<p><strong>80</strong> — oxirgi boʻlish "
                       "bajarilmagan.</p>",
    },
]


# =====================================================================
# SAT-85 — inequalities and regions
# =====================================================================

Q_SAT85 = [
    {
        "text": "<p>Which point is a solution to the system <i>y</i> ≥ 2<i>x</i> − 3 "
                "and <i>y</i> &lt; −<i>x</i> + 6?</p>",
        "choices": ["(1, 2)", "(4, 1)", "(0, 7)", "(3, 3)"],
        "correct": "(1, 2)",
        "explanation": "<p><strong>(1, 2).</strong> 2 ≥ −1 ✓ va 2 &lt; 5 ✓</p>"
                       "<p><strong>(3, 3)</strong> — aynan ikkinchi chegarada: "
                       "3 &lt; 3 notoʻgʻri.</p>",
    },
    {
        "text": "<p>Is (2, 5) a solution to <i>y</i> &gt; 2<i>x</i>?</p>",
        "choices": ["Yes, because 5 is greater than 4",
                    "No, because 5 is greater than 4",
                    "Yes, because 2 is less than 5",
                    "No, because the point is on the line"],
        "correct": "Yes, because 5 is greater than 4",
        "explanation": "<p><strong>Ha.</strong> 2x = 4, va 5 &gt; 4.</p>",
    },
    {
        "text": "<p>Is (2, 4) a solution to <i>y</i> &gt; 2<i>x</i>?</p>",
        "choices": ["No, it lies on the boundary line",
                    "Yes, it lies inside the region",
                    "No, it lies below the line",
                    "Yes, because 4 equals 4"],
        "correct": "No, it lies on the boundary line",
        "explanation": "<p><strong>Yoʻq.</strong> 4 &gt; 4 notoʻgʻri — qattiq "
                       "tengsizlik oʻz chizigʻini olmaydi.</p>",
    },
    {
        "text": "<p>Is (2, 4) a solution to <i>y</i> ≥ 2<i>x</i>?</p>",
        "choices": ["Yes, because ≥ includes the line",
                    "No, because it is on the line",
                    "Yes, because 4 is greater than 4",
                    "No, because 2 is less than 4"],
        "correct": "Yes, because ≥ includes the line",
        "explanation": "<p><strong>Ha.</strong> Bitta belgi javobni "
                       "oʻzgartiradi: ≥ tenglikni oladi.</p>",
    },
    {
        "text": "<p>Translate \"at most 30 hours\" into a symbol.</p>",
        "choices": ["≤ 30", "≥ 30", "&lt; 30", "= 30"],
        "correct": "≤ 30",
        "explanation": "<p><strong>≤ 30.</strong> «At most» — 30 ham mumkin.</p>",
    },
    {
        "text": "<p>Translate \"at least 12 students\" into a symbol.</p>",
        "choices": ["≥ 12", "≤ 12", "&gt; 12", "&lt; 12"],
        "correct": "≥ 12",
        "explanation": "<p><strong>≥ 12.</strong> «At least» — 12 ham mumkin.</p>",
    },
    {
        "text": "<p>Translate \"no more than 50 kilograms\" into a symbol.</p>",
        "choices": ["≤ 50", "≥ 50", "&lt; 50", "&gt; 50"],
        "correct": "≤ 50",
        "explanation": "<p><strong>≤ 50.</strong> «No more than» — «at most» "
                       "bilan bir xil.</p>",
    },
    {
        "text": "<p>On a graph, a strict inequality such as &lt; is drawn with</p>",
        "choices": ["A dashed boundary line", "A solid boundary line",
                    "No boundary line", "Two boundary lines"],
        "correct": "A dashed boundary line",
        "explanation": "<p><strong>Uzuq chiziq.</strong> Chiziqning oʻzi "
                       "yechimga kirmaydi.</p>",
    },
    {
        "text": "<p>On a graph, ≥ is drawn with</p>",
        "choices": ["A solid boundary line", "A dashed boundary line",
                    "A dotted region", "No shading"],
        "correct": "A solid boundary line",
        "explanation": "<p><strong>Toʻliq chiziq.</strong> Chegara yechimga "
                       "kiradi.</p>",
    },
    {
        "text": "<p>A student buys notebooks at $4 each and pens at $2 each. She has "
                "at most $60 and needs at least 8 notebooks. Which combination is "
                "possible?</p>",
        "choices": ["10 notebooks and 10 pens", "5 notebooks and 20 pens",
                    "12 notebooks and 8 pens", "8 notebooks and 15 pens"],
        "correct": "10 notebooks and 10 pens",
        "explanation": "<p><strong>10 va 10.</strong> 40 + 20 = 60 ≤ 60 ✓ va "
                       "10 ≥ 8 ✓</p>"
                       "<p><strong>8 va 15</strong> — daftar sharti bajarilgan, "
                       "lekin 62 dollar: budjetdan ortiq.</p>",
    },
    {
        "text": "<p>With the same constraints, is 14 notebooks and 2 pens "
                "possible?</p>",
        "choices": ["Yes, it costs exactly $60", "No, it costs $64",
                    "No, there are too few notebooks", "Yes, it costs $56"],
        "correct": "Yes, it costs exactly $60",
        "explanation": "<p><strong>Ha.</strong> 56 + 4 = 60, va «at most $60» "
                       "60 ni ham oladi.</p>",
    },
    {
        "text": "<p>In a system of two inequalities, the solution set is</p>",
        "choices": ["The overlap of the two shaded regions",
                    "Either shaded region", "The area between the two lines only",
                    "The point where the lines cross"],
        "correct": "The overlap of the two shaded regions",
        "explanation": "<p><strong>Ustma-ust tushgan joy.</strong> Yechim "
                       "ikkala shartga birdan tegishli boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Which point satisfies <i>y</i> &lt; <i>x</i> + 2?</p>",
        "choices": ["(0, 1)", "(0, 2)", "(0, 5)", "(3, 6)"],
        "correct": "(0, 1)",
        "explanation": "<p><strong>(0, 1).</strong> 1 &lt; 2 ✓</p>"
                       "<p><strong>(0, 2)</strong> — aynan chegarada: 2 &lt; 2 "
                       "notoʻgʻri.</p>",
    },
    {
        "text": "<p>Which point satisfies both <i>x</i> ≥ 0 and <i>y</i> ≥ 0?</p>",
        "choices": ["(2, 3)", "(−1, 4)", "(3, −2)", "(−2, −3)"],
        "correct": "(2, 3)",
        "explanation": "<p><strong>(2, 3).</strong> Ikkala koordinata ham "
                       "manfiy emas — birinchi chorak.</p>",
    },
    {
        "text": "<p>In a real-world problem about numbers of objects, which hidden "
                "constraints always apply?</p>",
        "choices": ["Both quantities are at least zero",
                    "Both quantities are at most 100",
                    "The quantities must be equal",
                    "One quantity must be negative"],
        "correct": "Both quantities are at least zero",
        "explanation": "<p><strong>Ikkalasi ham nol yoki undan katta.</strong> "
                       "Manfiy daftar sotib bo'lmaydi.</p>",
    },
    {
        "text": "<p>Is (3, 3) a solution to <i>y</i> &lt; −<i>x</i> + 6?</p>",
        "choices": ["No, it lies exactly on the boundary",
                    "Yes, because 3 is less than 6",
                    "Yes, it lies below the line",
                    "No, it lies above the line"],
        "correct": "No, it lies exactly on the boundary",
        "explanation": "<p><strong>Yoʻq.</strong> −3 + 6 = 3, va 3 &lt; 3 "
                       "notoʻgʻri.</p>",
    },
    {
        "text": "<p>A student has at most $40 for tickets costing $6 each. What is "
                "the greatest whole number of tickets she can buy?</p>",
        "choices": ["6", "7", "5", "4"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 6 × 6 = 36 ≤ 40, lekin "
                       "7 × 6 = 42 &gt; 40.</p>"
                       "<p><strong>7</strong> — butun songa yaxlitlash "
                       "yuqoriga qilingan; cheklov yuqoridan turibdi.</p>",
    },
    {
        "text": "<p>Solve 3<i>x</i> + 2 ≤ 14.</p>",
        "choices": ["<i>x</i> ≤ 4", "<i>x</i> ≥ 4", "<i>x</i> ≤ 12",
                    "<i>x</i> ≤ 16/3"],
        "correct": "<i>x</i> ≤ 4",
        "explanation": "<p><strong>x ≤ 4.</strong> 12 ni 3 ga boʻling; belgi "
                       "musbatga boʻlinganda oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>For <i>y</i> &gt; 2<i>x</i>, is the line <i>y</i> = 2<i>x</i> "
                "part of the solution?</p>",
        "choices": ["No, strict inequalities exclude their boundary",
                    "Yes, boundaries are always included",
                    "Only where <i>x</i> is positive",
                    "Only at the origin"],
        "correct": "No, strict inequalities exclude their boundary",
        "explanation": "<p><strong>Yoʻq.</strong> Shuning uchun u uzuq chiziq "
                       "bilan chiziladi.</p>",
    },
    {
        "text": "<p>A truck may carry at most 1,200 kilograms and already has 300 "
                "kilograms on board. Boxes weigh 25 kilograms each. What is the "
                "greatest number of boxes it can take?</p>",
        "choices": ["36", "48", "40", "32"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> Qolgan sigʻim 900 kg, va "
                       "900 ÷ 25 = 36.</p>"
                       "<p><strong>48</strong> — 1,200 ni 25 ga boʻlgan, "
                       "yukdagi 300 kg hisobga olinmagan.</p>",
    },
]


PRACTICES = [
    {
        "title":       'SAT-81 Practice: The "Plugging In Numbers" Tactic',
        "description": "20 ta SAT uslubidagi savol — harfli javoblarga son qoʻyish, "
                       "yaxshi va yomon son tanlash, oʻz algebrangizni tekshirish.",
        "tutorial":    "SAT-81:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT81,
    },
    {
        "title":       "SAT-82 Practice: Backsolving (Working from the Options)",
        "description": "20 ta SAT uslubidagi savol — variantni sinash, oʻrtadan "
                       "boshlash va matnli masalada javobni matnga qaytarish.",
        "tutorial":    "SAT-82:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT82,
    },
    {
        "title":       "SAT-83 Practice: Mastering Desmos I — Graphing and Intersections",
        "description": "20 ta SAT uslubidagi savol — tenglamani ikki grafikka "
                       "ajratish, kesishish, nollar va Desmosning ikki tuzogʻi.",
        "tutorial":    "SAT-83:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT83,
    },
    {
        "title":       "SAT-84 Practice: Mastering Desmos II — Sliders for Unknown Constants",
        "description": "20 ta SAT uslubidagi savol — nomaʼlum doimiyni surgich bilan "
                       "topish, «nechta yechim» oilasi va oʻnlini kasrga qaytarish.",
        "tutorial":    "SAT-84:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT84,
    },
    {
        "title":       "SAT-85 Practice: Mastering Desmos III — Inequalities and Bounded Regions",
        "description": "20 ta SAT uslubidagi savol — at most / at least, uzuq va "
                       "toʻliq chegara, ikki shartning kesishgan sohasi.",
        "tutorial":    "SAT-85:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT85,
    },
]
