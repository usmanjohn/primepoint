# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-36 … SAT-40.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context & interpretation ·
      15–16 trap-spotting · 17–18 Module 2 level · 19–20 word problems.

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_36_40.py --master=prime \\
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
# SAT-36 — maximum and minimum values
# =====================================================================

Q_SAT36 = [
    {
        "text": "<p>What is the maximum value of <i>y</i> = −(<i>x</i> − 3)<sup>2</sup> + 8?</p>",
        "choices": ["8", "3", "−8", "5"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> a manfiy, demak uch maksimum, va k = 8.</p>"
                       "<p><strong>3</strong> — bu maksimum <b>qayerda</b> boʻlishi.</p>",
    },
    {
        "text": "<p>What is the minimum value of <i>y</i> = <i>x</i><sup>2</sup> − "
                "6<i>x</i> + 11?</p>",
        "choices": ["2", "3", "11", "−2"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> x = 6 ÷ 2 = 3, keyin y = 9 − 18 + 11 = 2.</p>"
                       "<p><strong>3</strong> — bu x koordinatasi, qiymat emas.</p>",
    },
    {
        "text": "<p>A ball's height is <i>h</i> = −5<i>t</i><sup>2</sup> + 40<i>t</i> "
                "metres. After how many seconds does it reach its greatest height?</p>",
        "choices": ["4", "8", "80", "20"],
        "correct": "4",
        "explanation": "<p><strong>4 soniya.</strong> t = −40 ÷ (−10) = 4.</p>"
                       "<p><strong>8</strong> — bu yerga tushish vaqti, eng yuqori "
                       "nuqta emas.</p>",
    },
    {
        "text": "<p>For the same ball, <i>h</i> = −5<i>t</i><sup>2</sup> + 40<i>t</i>. "
                "What is its greatest height?</p>",
        "choices": ["80 metres", "40 metres", "4 metres", "160 metres"],
        "correct": "80 metres",
        "explanation": "<p><strong>80 metr.</strong> t = 4 da: −80 + 160 = 80.</p>"
                       "<p><strong>40</strong> — koeffitsient shundoq olingan; uni "
                       "modelga qoʻyish kerak edi.</p>",
    },
    {
        "text": "<p>Two numbers have a sum of 20. What is their greatest possible "
                "product?</p>",
        "choices": ["100", "20", "40", "400"],
        "correct": "100",
        "explanation": "<p><strong>100.</strong> P = x(20 − x), uch x = 10 da → "
                       "10 × 10.</p>"
                       "<p>Yigʻindisi qatʼiy boʻlganda koʻpaytma sonlar teng "
                       "boʻlganda eng katta boʻladi.</p>",
    },
    {
        "text": "<p>A rectangle has a perimeter of 24 metres. What is its greatest "
                "possible area?</p>",
        "choices": ["36 square metres", "24 square metres", "144 square metres",
                    "72 square metres"],
        "correct": "36 square metres",
        "explanation": "<p><strong>36 m².</strong> Yarim perimetr 12, demak "
                       "A = w(12 − w), uch w = 6 da → 6 × 6.</p>"
                       "<p>Toʻrtala tomon toʻrlanganda javob har doim kvadrat.</p>",
    },
    {
        "text": "<p>A farmer has 60 metres of fencing for a rectangular pen against a "
                "wall, needing fencing on only three sides. What is the greatest "
                "possible area?</p>",
        "choices": ["450 square metres", "225 square metres", "900 square metres",
                    "300 square metres"],
        "correct": "450 square metres",
        "explanation": "<p><strong>450 m².</strong> A = w(60 − 2w), uch w = 15 da → "
                       "15 × 30 = 450.</p>"
                       "<p><strong>225</strong> — 15 × 15 kvadrat deb hisoblangan; "
                       "devor bu qoidani buzadi.</p>",
    },
    {
        "text": "<p>A shop sells a lamp for 30 dollars and sells 200 each month. Each "
                "1 dollar increase loses 5 sales. What price gives the greatest "
                "revenue?</p>",
        "choices": ["35 dollars", "5 dollars", "175 dollars", "30 dollars"],
        "correct": "35 dollars",
        "explanation": "<p><strong>35 dollar.</strong> R = (30 + x)(200 − 5x), uch "
                       "x = 5 da → narx 30 + 5.</p>"
                       "<p><strong>5</strong> — bu oshirish miqdori, narx emas.</p>",
    },
    {
        "text": "<p>For that shop, what is the greatest monthly revenue?</p>",
        "choices": ["6,125 dollars", "6,000 dollars", "5,250 dollars", "7,000 dollars"],
        "correct": "6,125 dollars",
        "explanation": "<p><strong>6,125 dollar.</strong> 35 × 175 = 6,125.</p>"
                       "<p><strong>6,000</strong> — bu boshlangʻich holat "
                       "(30 × 200), maksimum emas.</p>",
    },
    {
        "text": "<p>The profit of a business is <i>P</i> = −3(<i>x</i> − 20)<sup>2</sup> "
                "+ 240. What is the greatest profit?</p>",
        "choices": ["240", "20", "−3", "220"],
        "correct": "240",
        "explanation": "<p><strong>240.</strong> Uchi shakli: k = 240, va a manfiy "
                       "boʻlgani uchun bu maksimum.</p>"
                       "<p><strong>20</strong> — maksimum qaysi x da boʻlishi.</p>",
    },
    {
        "text": "<p>In the model <i>R</i> = (20 + <i>x</i>)(300 − 10<i>x</i>) for "
                "revenue, what does <i>x</i> represent?</p>",
        "choices": ["The increase in price, in dollars", "The price itself",
                    "The number of items sold", "The revenue"],
        "correct": "The increase in price, in dollars",
        "explanation": "<p><strong>Narxning oshishi.</strong> Narx 20 + x, soni "
                       "300 − 10x — demak x oʻzgarish miqdori.</p>"
                       "<p>Bu farqni yozib qoʻymaslik matnli masaladagi eng koʻp "
                       "uchraydigan yoʻqotish.</p>",
    },
    {
        "text": "<p>A quadratic model of revenue has <i>a</i> &lt; 0. What does this "
                "tell you?</p>",
        "choices": ["The revenue has a maximum but no minimum",
                    "The revenue has a minimum but no maximum",
                    "The revenue grows forever",
                    "The revenue is always negative"],
        "correct": "The revenue has a maximum but no minimum",
        "explanation": "<p><strong>Maksimum bor, minimum yoʻq.</strong> a manfiy "
                       "boʻlsa parabola pastga ochiladi.</p>"
                       "<p>Bu mantiqan ham toʻgʻri: narx juda oshsa hech kim "
                       "sotib olmaydi.</p>",
    },
    {
        "text": "<p>A ball's height is <i>h</i> = −5<i>t</i><sup>2</sup> + 20<i>t</i> "
                "+ 25. What was its height at the moment it was thrown?</p>",
        "choices": ["25 metres", "45 metres", "20 metres", "0 metres"],
        "correct": "25 metres",
        "explanation": "<p><strong>25 metr.</strong> t = 0 qoʻying — erkin had "
                       "boshlangʻich balandlikni beradi.</p>"
                       "<p><strong>45</strong> — bu eng yuqori nuqta (t = 2 da), "
                       "boshlangʻich holat emas.</p>",
    },
    {
        "text": "<p>For that same ball, what is its greatest height?</p>",
        "choices": ["45 metres", "25 metres", "20 metres", "2 metres"],
        "correct": "45 metres",
        "explanation": "<p><strong>45 metr.</strong> t = −20 ÷ (−10) = 2, keyin "
                       "−20 + 40 + 25 = 45.</p>"
                       "<p><strong>2</strong> — bu soniya, metr emas: oʻlchov "
                       "birligiga qarang.</p>",
    },
    {
        "text": "<p>A student solves a revenue problem, finds the vertex at "
                "<i>x</i> = 4, and answers '4 dollars' for the best price. The "
                "original price was 15 dollars and <i>x</i> is the increase. What is "
                "the correct answer?</p>",
        "choices": ["19 dollars", "4 dollars", "11 dollars", "60 dollars"],
        "correct": "19 dollars",
        "explanation": "<p><strong>19 dollar.</strong> Narx = 15 + 4.</p>"
                       "<p>Oʻquvchi x ni javob deb belgilagan — modelni tuzganda "
                       "x nimani anglatishini yozib qoʻyish kerak edi.</p>",
    },
    {
        "text": "<p>A student says that 40 metres of fencing on three sides gives the "
                "greatest area as a 10-by-10 square. What is the correct greatest "
                "area?</p>",
        "choices": ["200 square metres", "100 square metres", "400 square metres",
                    "160 square metres"],
        "correct": "200 square metres",
        "explanation": "<p><strong>200 m².</strong> Uch tomonda 2w + L = 40, uch "
                       "w = 10 da → 10 × 20.</p>"
                       "<p>«Eng katta maydon — kvadrat» qoidasi faqat toʻrt tomon "
                       "toʻrlanganda ishlaydi.</p>",
    },
    {
        "text": "<p>A cinema charges 8 dollars and sells 500 tickets. Each 1 dollar "
                "rise loses 25 tickets. What ticket price gives the greatest "
                "revenue?</p>",
        "choices": ["14 dollars", "6 dollars", "10 dollars", "20 dollars"],
        "correct": "14 dollars",
        "explanation": "<p><strong>14 dollar.</strong> R = (8 + x)(500 − 25x), uch "
                       "x = 6 da → 8 + 6 = 14.</p>"
                       "<p>Tekshiruv: 14 × 350 = 4,900, va 13 × 375 = 4,875 ✓</p>",
    },
    {
        "text": "<p>A rectangular field is divided into two equal pens by a fence "
                "parallel to one side. With 60 metres of fencing in total (all four "
                "sides plus the divider), what is the greatest total area?</p>",
        "choices": ["150 square metres", "225 square metres", "200 square metres",
                    "300 square metres"],
        "correct": "150 square metres",
        "explanation": "<p><strong>150 m².</strong> Uchta parallel tomon: 3w + 2L = 60, "
                       "demak A = w(60 − 3w) ÷ 2, uch w = 10 da → 10 × 15 = 150.</p>"
                       "<p>Boʻluvchi devor toʻrni uchinchi marta oʻsha yoʻnalishda "
                       "ishlatadi — shuning uchun 3w.</p>",
    },
    {
        "text": "<p>A gardener has 32 metres of edging for a rectangular bed. What "
                "dimensions give the greatest area?</p>",
        "choices": ["8 m by 8 m", "10 m by 6 m", "12 m by 4 m", "16 m by 16 m"],
        "correct": "8 m by 8 m",
        "explanation": "<p><strong>8 m × 8 m.</strong> Yarim perimetr 16, uch w = 8 "
                       "da → maydon 64 m².</p>"
                       "<p><strong>10 × 6</strong> perimetri toʻgʻri, lekin maydoni "
                       "60 — kamroq.</p>",
    },
    {
        "text": "<p>A bus company charges 5 dollars and carries 400 passengers a day. "
                "Each 1 dollar rise loses 40 passengers. What is the greatest daily "
                "income?</p>",
        "choices": ["2,250 dollars", "2,000 dollars", "1,800 dollars", "2,400 dollars"],
        "correct": "2,250 dollars",
        "explanation": "<p><strong>2,250 dollar.</strong> I = (5 + x)(400 − 40x), uch "
                       "x = 2.5 da → 7.50 × 300 = 2,250.</p>"
                       "<p><strong>2,000</strong> — boshlangʻich holat "
                       "(5 × 400).</p>",
    },
]


# =====================================================================
# SAT-37 — graphing parabolas
# =====================================================================

Q_SAT37 = [
    {
        "text": "<p>What is the <i>y</i>-intercept of <i>y</i> = <i>x</i><sup>2</sup> "
                "− 5<i>x</i> + 6?</p>",
        "choices": ["(0, 6)", "(6, 0)", "(0, −5)", "(0, 0)"],
        "correct": "(0, 6)",
        "explanation": "<p><strong>(0, 6).</strong> x = 0 qoʻying — erkin had.</p>"
                       "<p><strong>(6, 0)</strong> — koordinatalar oʻrin almashgan.</p>",
    },
    {
        "text": "<p>What are the <i>x</i>-intercepts of <i>y</i> = (<i>x</i> − 2)"
                "(<i>x</i> + 5)?</p>",
        "choices": ["x = 2 and x = −5", "x = −2 and x = 5", "x = 2 and x = 5",
                    "x = −2 and x = −5"],
        "correct": "x = 2 and x = −5",
        "explanation": "<p><strong>x = 2 va x = −5.</strong> Har bir qavsni nolga "
                       "tenglashtiring.</p>"
                       "<p>Ildizlar qavsdagi sonlarning qarama-qarshisi.</p>",
    },
    {
        "text": "<p>A parabola has zeros at <i>x</i> = 2 and <i>x</i> = 8. What is the "
                "equation of its axis of symmetry?</p>",
        "choices": ["x = 5", "x = 3", "x = 6", "y = 5"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> Nollarning oʻrtasi: "
                       "(2 + 8) ÷ 2.</p>"
                       "<p><strong>x = 3</strong> — ayirmaning yarmi hisoblangan.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = −2<i>x</i><sup>2</sup> + 4<i>x</i> + 1 "
                "opens in which direction?</p>",
        "choices": ["Downward", "Upward", "To the right", "To the left"],
        "correct": "Downward",
        "explanation": "<p><strong>Pastga.</strong> a = −2 manfiy.</p>"
                       "<p>Parabola faqat yuqoriga yoki pastga ochiladi — yon "
                       "tomonga emas.</p>",
    },
    {
        "text": "<p>How many times does the graph of <i>y</i> = <i>x</i><sup>2</sup> "
                "+ 3<i>x</i> + 7 cross the <i>x</i>-axis?</p>",
        "choices": ["It does not cross it", "Once", "Twice", "Three times"],
        "correct": "It does not cross it",
        "explanation": "<p><strong>Kesmaydi.</strong> D = 9 − 28 = −19 &lt; 0 "
                       "(SAT-34).</p>"
                       "<p>Parabola x oʻqidan butunlay yuqorida turadi.</p>",
    },
    {
        "text": "<p>What is the vertex of <i>y</i> = <i>x</i><sup>2</sup> − "
                "10<i>x</i> + 21?</p>",
        "choices": ["(5, −4)", "(5, 21)", "(−5, −4)", "(10, 21)"],
        "correct": "(5, −4)",
        "explanation": "<p><strong>(5, −4).</strong> x = 10 ÷ 2 = 5, keyin "
                       "25 − 50 + 21 = −4.</p>"
                       "<p>Nollari 3 va 7, va ularning oʻrtasi ham 5 ✓</p>",
    },
    {
        "text": "<p>Which equation displays the zeros of the parabola as "
                "constants?</p>",
        "choices": ["y = (x − 3)(x + 5)", "y = x² + 2x − 15", "y = (x + 1)² − 16",
                    "y = 2x + 3"],
        "correct": "y = (x − 3)(x + 5)",
        "explanation": "<p><strong>Ajratilgan koʻrinish.</strong> Nollar 3 va −5 "
                       "toʻgʻridan-toʻgʻri koʻrinadi.</p>"
                       "<p>Uchinchi variant <b>uchni</b> koʻrsatadi, nollarni "
                       "emas — uchalasi ham bir xil parabola.</p>",
    },
    {
        "text": "<p>Which equation displays the vertex of the parabola as "
                "constants?</p>",
        "choices": ["y = (x + 1)² − 16", "y = (x − 3)(x + 5)", "y = x² + 2x − 15",
                    "y = x + 1"],
        "correct": "y = (x + 1)² − 16",
        "explanation": "<p><strong>Uchi shakli.</strong> Uch (−1, −16) darrov "
                       "oʻqiladi.</p>"
                       "<p>Uchala kvadrat variant ham bir xil grafikni chizadi — "
                       "farq faqat nima koʻrinishida.</p>",
    },
    {
        "text": "<p>The point (0, 7) lies on the graph of <i>y</i> = "
                "<i>x</i><sup>2</sup> − 6<i>x</i> + 7. Which other point has the same "
                "<i>y</i>-value?</p>",
        "choices": ["(6, 7)", "(3, 7)", "(−6, 7)", "(7, 7)"],
        "correct": "(6, 7)",
        "explanation": "<p><strong>(6, 7).</strong> Uch x = 3 da; 0 va 6 undan bir "
                       "xil masofada.</p>"
                       "<p>Tekshiruv: 36 − 36 + 7 = 7 ✓</p>",
    },
    {
        "text": "<p>A parabola opens upward and its vertex is at (2, 5). How many "
                "<i>x</i>-intercepts does it have?</p>",
        "choices": ["None", "One", "Two", "It cannot be determined"],
        "correct": "None",
        "explanation": "<p><strong>Bittasi ham yoʻq.</strong> Eng past nuqtasi "
                       "y = 5 da, yaʼni x oʻqidan yuqorida.</p>"
                       "<p>Yuqoriga ochilgan parabola uchidan pastga "
                       "tushmaydi.</p>",
    },
    {
        "text": "<p>A table shows that a quadratic has the same value at <i>x</i> = 1 "
                "and <i>x</i> = 9. What is the <i>x</i>-coordinate of its vertex?</p>",
        "choices": ["5", "4", "8", "10"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Bir xil y qiymatli ikki nuqta uchdan "
                       "bir xil masofada — oʻrtasi (1 + 9) ÷ 2.</p>"
                       "<p>Bu jadval berilgan savollardagi eng tez yoʻl.</p>",
    },
    {
        "text": "<p>The graph of a quadratic has its vertex at (4, −9) and passes "
                "through (0, 7). Does it cross the <i>x</i>-axis?</p>",
        "choices": ["Yes, twice", "No", "Yes, once", "It cannot be determined"],
        "correct": "Yes, twice",
        "explanation": "<p><strong>Ha, ikki marta.</strong> Uch x oʻqidan pastda "
                       "(−9), (0, 7) esa yuqorida — demak grafik oʻqni ikki "
                       "tomondan kesib oʻtadi.</p>"
                       "<p>Uch pastda va biror nuqta yuqorida boʻlsa, kesishish "
                       "muqarrar.</p>",
    },
    {
        "text": "<p>Which feature of <i>y</i> = <i>ax</i><sup>2</sup> + <i>bx</i> + "
                "<i>c</i> does the constant <i>c</i> give you directly?</p>",
        "choices": ["The y-intercept", "The vertex", "The zeros",
                    "The axis of symmetry"],
        "correct": "The y-intercept",
        "explanation": "<p><strong>y oʻqidagi nuqta.</strong> x = 0 qoʻyilganda "
                       "faqat c qoladi.</p>"
                       "<p>Nollar uchun ajratish, uch uchun −b ÷ (2a) kerak.</p>",
    },
    {
        "text": "<p>A parabola passes through (−2, 0) and (6, 0). Where is its axis of "
                "symmetry?</p>",
        "choices": ["x = 2", "x = 4", "x = −2", "x = 8"],
        "correct": "x = 2",
        "explanation": "<p><strong>x = 2.</strong> (−2 + 6) ÷ 2 = 2.</p>"
                       "<p><strong>x = 4</strong> — ayirmaning yarmi "
                       "(8 ÷ 2), oʻrtasi emas.</p>",
    },
    {
        "text": "<p>A student says the <i>y</i>-intercept of <i>y</i> = "
                "<i>x</i><sup>2</sup> − 4<i>x</i> + 9 is (9, 0). What is the correct "
                "answer?</p>",
        "choices": ["(0, 9)", "(9, 0)", "(0, −4)", "(2, 5)"],
        "correct": "(0, 9)",
        "explanation": "<p><strong>(0, 9).</strong> y oʻqida turgan nuqtaning x "
                       "koordinatasi nolga teng.</p>"
                       "<p><strong>(2, 5)</strong> — bu uch, boshqa savolning "
                       "javobi.</p>",
    },
    {
        "text": "<p>A student says a parabola with zeros at −4 and 10 has its axis of "
                "symmetry at <i>x</i> = 7. What is the correct answer?</p>",
        "choices": ["x = 3", "x = 7", "x = −7", "x = 6"],
        "correct": "x = 3",
        "explanation": "<p><strong>x = 3.</strong> (−4 + 10) ÷ 2 = 3.</p>"
                       "<p>Oʻquvchi ayirmaning yarmini olgan (14 ÷ 2 = 7) — bu "
                       "uchdan nolgacha boʻlgan masofa, oʻrta emas.</p>",
    },
    {
        "text": "<p>The graph of <i>y</i> = <i>a</i>(<i>x</i> − 3)<sup>2</sup> + 4 "
                "passes through (1, 12). What is the value of <i>a</i>?</p>",
        "choices": ["2", "4", "8", "−2"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> 12 = a(1 − 3)² + 4 → 12 = 4a + 4 → "
                       "a = 2.</p>"
                       "<p><strong>8</strong> — 4 ni ayirish unutilgan.</p>",
    },
    {
        "text": "<p>A parabola has zeros at <i>x</i> = 1 and <i>x</i> = 5 and passes "
                "through (3, −8). What is its vertex?</p>",
        "choices": ["(3, −8)", "(3, 0)", "(2, −8)", "(4, −8)"],
        "correct": "(3, −8)",
        "explanation": "<p><strong>(3, −8).</strong> Uch nollarning oʻrtasida, "
                       "x = 3 — va berilgan nuqta ham aynan x = 3 da.</p>"
                       "<p>Demak bu nuqtaning oʻzi uch.</p>",
    },
    {
        "text": "<p>A bridge arch follows a parabola. Its base meets the ground at "
                "<i>x</i> = 0 and <i>x</i> = 40 metres. How far from the left base is "
                "its highest point?</p>",
        "choices": ["20 metres", "40 metres", "10 metres", "80 metres"],
        "correct": "20 metres",
        "explanation": "<p><strong>20 metr.</strong> Uch ikki nolning oʻrtasida: "
                       "(0 + 40) ÷ 2.</p>"
                       "<p>Balandligini bilish shart emas — simmetriya "
                       "yetadi.</p>",
    },
    {
        "text": "<p>A ball's height follows <i>h</i> = −5<i>t</i><sup>2</sup> + "
                "30<i>t</i>. At what two times is the ball at ground level?</p>",
        "choices": ["t = 0 and t = 6", "t = 0 and t = 30", "t = 3 and t = 6",
                    "t = 6 only"],
        "correct": "t = 0 and t = 6",
        "explanation": "<p><strong>t = 0 va t = 6.</strong> −5t(t − 6) = 0.</p>"
                       "<p>Uch ularning oʻrtasida, t = 3 — eng yuqori nuqtaning "
                       "vaqti.</p>",
    },
]


# =====================================================================
# SAT-38 — linear-quadratic systems
# =====================================================================

Q_SAT38 = [
    {
        "text": "<p>Which ordered pair is a solution to <i>y</i> = <i>x</i><sup>2</sup> "
                "and <i>y</i> = 3<i>x</i> − 2?</p>",
        "choices": ["(2, 4)", "(2, 2)", "(4, 2)", "(3, 9)"],
        "correct": "(2, 4)",
        "explanation": "<p><strong>(2, 4).</strong> x² = 3x − 2 → x² − 3x + 2 = 0 → "
                       "x = 1 yoki 2; x = 2 da y = 4.</p>"
                       "<p>Tekshiruv: 4 = 2² ✓ va 4 = 6 − 2 ✓</p>",
    },
    {
        "text": "<p>Solve the system <i>y</i> = <i>x</i><sup>2</sup> − 1 and "
                "<i>y</i> = 3. What are the <i>x</i>-values?</p>",
        "choices": ["x = 2 and x = −2", "x = 2 only", "x = 4 and x = −4",
                    "x = 3 and x = −3"],
        "correct": "x = 2 and x = −2",
        "explanation": "<p><strong>x = ±2.</strong> x² − 1 = 3 → x² = 4.</p>"
                       "<p><strong>x = 2 only</strong> — manfiy ildiz unutilgan; "
                       "x² = 4 ning ikkita yechimi bor.</p>",
    },
    {
        "text": "<p>How many points of intersection do <i>y</i> = <i>x</i><sup>2</sup> "
                "and <i>y</i> = −5 have?</p>",
        "choices": ["Zero", "One", "Two", "Infinitely many"],
        "correct": "Zero",
        "explanation": "<p><strong>Zero.</strong> x² = −5 ning haqiqiy yechimi "
                       "yoʻq.</p>"
                       "<p>y = x² parabolasi hech qachon x oʻqidan pastga "
                       "tushmaydi.</p>",
    },
    {
        "text": "<p>Solve the system <i>y</i> = <i>x</i><sup>2</sup> + 4<i>x</i> and "
                "<i>y</i> = <i>x</i> + 4.</p>",
        "choices": ["(1, 5) and (−4, 0)", "(1, 5) and (4, 8)", "(−1, 3) and (4, 8)",
                    "(1, 1) and (−4, −4)"],
        "correct": "(1, 5) and (−4, 0)",
        "explanation": "<p><strong>(1, 5) va (−4, 0).</strong> x² + 3x − 4 = 0 → "
                       "(x + 4)(x − 1) = 0.</p>"
                       "<p>y ni chiziqli tenglamadan oldik: 1 + 4 = 5 va "
                       "−4 + 4 = 0.</p>",
    },
    {
        "text": "<p>How many points of intersection do <i>y</i> = <i>x</i><sup>2</sup> "
                "+ 3 and <i>y</i> = <i>x</i> have?</p>",
        "choices": ["Zero", "One", "Two", "Three"],
        "correct": "Zero",
        "explanation": "<p><strong>Zero.</strong> x² − x + 3 = 0, D = 1 − 12 = −11 "
                       "&lt; 0.</p>"
                       "<p>Diskriminant sistemani yechmasdan javob beradi.</p>",
    },
    {
        "text": "<p>How many points of intersection do <i>y</i> = <i>x</i><sup>2</sup> "
                "and <i>y</i> = 2<i>x</i> − 1 have?</p>",
        "choices": ["One", "Two", "Zero", "Infinitely many"],
        "correct": "One",
        "explanation": "<p><strong>One.</strong> x² − 2x + 1 = 0 → (x − 1)², D = 0.</p>"
                       "<p>Chiziq parabolaga (1, 1) nuqtada <b>urinadi</b> — "
                       "tangent.</p>",
    },
    {
        "text": "<p>The line <i>y</i> = <i>c</i> is tangent to <i>y</i> = "
                "<i>x</i><sup>2</sup> − 6<i>x</i> + 11. What is the value of "
                "<i>c</i>?</p>",
        "choices": ["2", "3", "11", "−2"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Gorizontal chiziq parabolaga faqat "
                       "uchida urinadi; uch (3, 2).</p>"
                       "<p><strong>3</strong> — bu uchning x koordinatasi.</p>",
    },
    {
        "text": "<p>Solve the system <i>y</i> = <i>x</i><sup>2</sup> − 4 and "
                "<i>y</i> = 3<i>x</i>.</p>",
        "choices": ["(4, 12) and (−1, −3)", "(4, 12) and (1, 3)",
                    "(−4, −12) and (1, 3)", "(2, 6) and (−2, −6)"],
        "correct": "(4, 12) and (−1, −3)",
        "explanation": "<p><strong>(4, 12) va (−1, −3).</strong> x² − 3x − 4 = 0 → "
                       "(x − 4)(x + 1) = 0.</p>"
                       "<p>Tekshiruv: 12 = 16 − 4 ✓ va −3 = 1 − 4 ✓</p>",
    },
    {
        "text": "<p>If 2<i>x</i> + <i>y</i> = 7 and <i>y</i> = <i>x</i><sup>2</sup>, "
                "what is one possible value of <i>x</i>?</p>",
        "choices": ["−1 + 2√2", "7", "−2", "3"],
        "correct": "−1 + 2√2",
        "explanation": "<p><strong>−1 + 2√2.</strong> Avval y = 7 − 2x deb yozing, "
                       "keyin x² + 2x − 7 = 0; D = 4 + 28 = 32.</p>"
                       "<p>x = (−2 ± 4√2) ÷ 2 = −1 ± 2√2, taxminan 1.83 va "
                       "−3.83.</p>",
    },
    {
        "text": "<p>The graphs of <i>y</i> = <i>x</i><sup>2</sup> and <i>y</i> = "
                "<i>x</i> + <i>k</i> intersect at exactly one point. What is the value "
                "of <i>k</i>?</p>",
        "choices": ["−0.25", "0.25", "0", "1"],
        "correct": "−0.25",
        "explanation": "<p><strong>−0.25.</strong> x² − x − k = 0 va D = 1 + 4k = 0 "
                       "→ k = −0.25.</p>"
                       "<p>Ishoraga eʼtibor bering: −k ning diskriminantdagi "
                       "hissasi +4k.</p>",
    },
    {
        "text": "<p>What does it mean for a line to be tangent to a parabola?</p>",
        "choices": ["They meet at exactly one point",
                    "They meet at two points",
                    "They never meet",
                    "The line passes through the vertex"],
        "correct": "They meet at exactly one point",
        "explanation": "<p><strong>Aynan bitta nuqtada uchrashadi.</strong> Bu "
                       "D = 0 ning inglizchasi.</p>"
                       "<p>Uchdan oʻtish shart emas — faqat gorizontal tangent "
                       "chiziq uchdan oʻtadi.</p>",
    },
    {
        "text": "<p>Can the graphs of a line and a parabola intersect at three "
                "points?</p>",
        "choices": ["No — the resulting equation is quadratic, so at most two",
                    "Yes, if the parabola is wide enough",
                    "Yes, if the line is horizontal",
                    "Only if they are the same curve"],
        "correct": "No — the resulting equation is quadratic, so at most two",
        "explanation": "<p><strong>Yoʻq.</strong> Tenglashtirilganda kvadrat tenglama "
                       "hosil boʻladi, uning esa koʻpi bilan ikkita ildizi bor.</p>"
                       "<p>Shuning uchun «uchta kesishish» varianti har doim "
                       "notoʻgʻri.</p>",
    },
    {
        "text": "<p>Two graphs intersect at (3, 5). What must be true?</p>",
        "choices": ["The point satisfies both equations",
                    "The point satisfies at least one equation",
                    "x = 3 solves only the linear equation",
                    "The graphs are identical"],
        "correct": "The point satisfies both equations",
        "explanation": "<p><strong>Ikkala tenglamani ham qanoatlantiradi.</strong> "
                       "Kesishish nuqtasi ikkala grafikda ham yotadi.</p>"
                       "<p>Javobni tekshirishning eng ishonchli yoʻli ham shu.</p>",
    },
    {
        "text": "<p>The system <i>y</i> = <i>x</i><sup>2</sup> + 2 and <i>y</i> = "
                "<i>mx</i> has no real solution. What must be true about the "
                "discriminant of the resulting equation?</p>",
        "choices": ["It is negative", "It is zero", "It is positive", "It equals m"],
        "correct": "It is negative",
        "explanation": "<p><strong>Manfiy.</strong> Yechim yoʻqligi D &lt; 0 "
                       "degani.</p>"
                       "<p>Bu yerda x² − mx + 2 = 0, demak m² − 8 &lt; 0.</p>",
    },
    {
        "text": "<p>A student solves <i>y</i> = <i>x</i><sup>2</sup> and <i>y</i> = "
                "<i>x</i> + 6, finds <i>x</i> = 3, and answers '3'. What is the full "
                "solution?</p>",
        "choices": ["(3, 9) and (−2, 4)", "(3, 9) only", "(3, 3) and (−2, −2)",
                    "(9, 3) and (4, −2)"],
        "correct": "(3, 9) and (−2, 4)",
        "explanation": "<p><strong>(3, 9) va (−2, 4).</strong> x² − x − 6 = 0 → "
                       "x = 3 yoki −2, va har biriga y kerak.</p>"
                       "<p>Oʻquvchi ikkinchi ildizni ham, y larni ham "
                       "tashlab ketgan.</p>",
    },
    {
        "text": "<p>A student says <i>y</i> = <i>x</i><sup>2</sup> + 1 and <i>y</i> = "
                "<i>x</i> − 1 must intersect twice because a line always crosses a "
                "parabola. How many intersections are there really?</p>",
        "choices": ["Zero", "One", "Two", "Three"],
        "correct": "Zero",
        "explanation": "<p><strong>Zero.</strong> x² − x + 2 = 0, D = 1 − 8 = −7.</p>"
                       "<p>Chiziq parabolaning butunlay pastida qolishi mumkin — "
                       "diskriminantni tekshiring.</p>",
    },
    {
        "text": "<p>Solve the system <i>y</i> = 2<i>x</i><sup>2</sup> − 3<i>x</i> and "
                "<i>y</i> = <i>x</i> + 6.</p>",
        "choices": ["(3, 9) and (−1, 5)", "(3, 9) and (1, 7)", "(−3, 3) and (1, 7)",
                    "(2, 8) and (−1.5, 4.5)"],
        "correct": "(3, 9) and (−1, 5)",
        "explanation": "<p><strong>(3, 9) va (−1, 5).</strong> 2x² − 4x − 6 = 0 → "
                       "x² − 2x − 3 = 0 → (x − 3)(x + 1) = 0.</p>"
                       "<p>Tekshiruv: 2(9) − 9 = 9 ✓ va 3 + 6 = 9 ✓</p>",
    },
    {
        "text": "<p>For what value of <i>k</i> is the line <i>y</i> = <i>k</i> tangent "
                "to <i>y</i> = 2<i>x</i><sup>2</sup> − 8<i>x</i> + 5?</p>",
        "choices": ["−3", "2", "5", "3"],
        "correct": "−3",
        "explanation": "<p><strong>−3.</strong> Uch x = 8 ÷ 4 = 2 da, va "
                       "y = 8 − 16 + 5 = −3.</p>"
                       "<p><strong>2</strong> — uchning x koordinatasi; gorizontal "
                       "chiziq y qiymatida turadi.</p>",
    },
    {
        "text": "<p>A ball's height is <i>y</i> = −<i>x</i><sup>2</sup> + 8<i>x</i> "
                "and a drone flies along the line <i>y</i> = 3<i>x</i>. At what "
                "positive horizontal distance do their paths cross?</p>",
        "choices": ["x = 5", "x = 3", "x = 8", "x = 0"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> −x² + 8x = 3x → x² − 5x = 0 → "
                       "x(x − 5) = 0.</p>"
                       "<p>x = 0 ham yechim, lekin savol <b>musbat</b> masofani "
                       "soʻragan.</p>",
    },
    {
        "text": "<p>A stone's path is <i>y</i> = −<i>x</i><sup>2</sup> + 6<i>x</i> and "
                "a wall runs along <i>y</i> = 8. At which two distances does the stone "
                "reach the wall's height?</p>",
        "choices": ["x = 2 and x = 4", "x = 2 and x = 6", "x = 4 and x = 8",
                    "x = 3 and x = 8"],
        "correct": "x = 2 and x = 4",
        "explanation": "<p><strong>x = 2 va x = 4.</strong> −x² + 6x = 8 → "
                       "x² − 6x + 8 = 0 → (x − 2)(x − 4) = 0.</p>"
                       "<p>Ikkalasi ham uchdan (x = 3) bir xil masofada — "
                       "simmetriya ✓</p>",
    },
]


# =====================================================================
# SAT-39 — radical equations and extraneous solutions
# =====================================================================

Q_SAT39 = [
    {
        "text": "<p>What is the solution to √(<i>x</i> + 12) = <i>x</i>?</p>",
        "choices": ["x = 4", "x = 4 and x = −3", "x = −3", "There is no solution"],
        "correct": "x = 4",
        "explanation": "<p><strong>x = 4.</strong> x + 12 = x² → x² − x − 12 = 0 → "
                       "x = 4 yoki −3.</p>"
                       "<p>x = −3: √9 = 3, lekin oʻng tomon −3 ✗ — begona ildiz.</p>",
    },
    {
        "text": "<p>What is the solution to √(4<i>x</i> + 5) = <i>x</i>?</p>",
        "choices": ["x = 5", "x = 5 and x = −1", "x = −1", "There is no solution"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> 4x + 5 = x² → x² − 4x − 5 = 0 → "
                       "x = 5 yoki −1.</p>"
                       "<p>Tekshiruv: √25 = 5 ✓; x = −1 da √1 = 1 ≠ −1 ✗</p>",
    },
    {
        "text": "<p>How many solutions does √<i>x</i> = −2 have?</p>",
        "choices": ["Zero", "One", "Two", "Infinitely many"],
        "correct": "Zero",
        "explanation": "<p><strong>Zero.</strong> √ belgisi manfiy boʻlmagan sonni "
                       "bildiradi.</p>"
                       "<p>Kvadratga koʻtarsangiz x = 4 chiqadi, lekin √4 = 2, −2 "
                       "emas — bu toza begona ildiz.</p>",
    },
    {
        "text": "<p>What is the solution to √(<i>x</i> − 1) = 3?</p>",
        "choices": ["x = 10", "x = 9", "x = 4", "x = 8"],
        "correct": "x = 10",
        "explanation": "<p><strong>x = 10.</strong> x − 1 = 9 → x = 10.</p>"
                       "<p>Tekshiruv: √9 = 3 ✓. Oʻng tomon musbat boʻlgani uchun "
                       "begona ildiz xavfi yoʻq.</p>",
    },
    {
        "text": "<p>What is the solution to √(<i>x</i> + 3) = <i>x</i> − 3?</p>",
        "choices": ["x = 6", "x = 6 and x = 1", "x = 1", "There is no solution"],
        "correct": "x = 6",
        "explanation": "<p><strong>x = 6.</strong> x + 3 = x² − 6x + 9 → "
                       "x² − 7x + 6 = 0 → x = 6 yoki 1.</p>"
                       "<p>x = 1: √4 = 2, lekin 1 − 3 = −2 ✗</p>",
    },
    {
        "text": "<p>Which value is an extraneous solution of √(2<i>x</i> + 8) = "
                "<i>x</i>?</p>",
        "choices": ["x = −2", "x = 4", "x = 2", "x = −4"],
        "correct": "x = −2",
        "explanation": "<p><strong>x = −2.</strong> 2x + 8 = x² → x² − 2x − 8 = 0 → "
                       "x = 4 yoki −2.</p>"
                       "<p>x = −2 da √4 = 2 ≠ −2 ✗, x = 4 da √16 = 4 ✓</p>",
    },
    {
        "text": "<p>What is the solution to √(<i>x</i> + 4) + 2 = <i>x</i>?</p>",
        "choices": ["x = 5", "x = 5 and x = 0", "x = 0", "There is no solution"],
        "correct": "x = 5",
        "explanation": "<p><strong>x = 5.</strong> Avval ildizni yolgʻiz qoldiring: "
                       "√(x + 4) = x − 2, keyin x + 4 = x² − 4x + 4.</p>"
                       "<p>x² − 5x = 0 → x = 5 yoki 0; x = 0 da √4 = 2 ≠ −2 ✗</p>",
    },
    {
        "text": "<p>How many solutions does √(<i>x</i> + 7) = <i>x</i> + 1 have?</p>",
        "choices": ["One", "Two", "Zero", "Three"],
        "correct": "One",
        "explanation": "<p><strong>One.</strong> x + 7 = x² + 2x + 1 → "
                       "x² + x − 6 = 0 → x = 2 yoki −3.</p>"
                       "<p>x = 2 ✓ (√9 = 3 = 2 + 1); x = −3 ✗ (√4 = 2, −3 + 1 = −2)</p>",
    },
    {
        "text": "<p>What is the first step in solving √(<i>x</i> − 2) + 5 = 9?</p>",
        "choices": ["Subtract 5 from both sides to isolate the radical",
                    "Square both sides immediately",
                    "Add 2 to both sides",
                    "Divide both sides by 5"],
        "correct": "Subtract 5 from both sides to isolate the radical",
        "explanation": "<p><strong>Ildizni yolgʻiz qoldiring.</strong> "
                       "√(x − 2) = 4, keyingina kvadratga koʻtaring.</p>"
                       "<p>Darrov kvadratga koʻtarish (√(x−2) + 5)² ni "
                       "hisoblashni talab qiladi — ancha murakkab.</p>",
    },
    {
        "text": "<p>What is the solution to √(<i>x</i> − 2) + 5 = 9?</p>",
        "choices": ["x = 18", "x = 6", "x = 83", "x = 11"],
        "correct": "x = 18",
        "explanation": "<p><strong>x = 18.</strong> √(x − 2) = 4 → x − 2 = 16.</p>"
                       "<p>Tekshiruv: √16 + 5 = 9 ✓</p>",
    },
    {
        "text": "<p>Why can squaring both sides create a solution that does not "
                "belong to the original equation?</p>",
        "choices": ["Because squaring loses the sign: 2 and −2 have the same square",
                    "Because squaring changes the value of x",
                    "Because the equation becomes harder",
                    "Because square roots are always irrational"],
        "correct": "Because squaring loses the sign: 2 and −2 have the same square",
        "explanation": "<p><strong>Ishora yoʻqoladi.</strong> Kvadratga koʻtarganda "
                       "−2 va 2 farqlanmay qoladi.</p>"
                       "<p>Shuning uchun tekshirish yechimning bir qismi, "
                       "qoʻshimcha emas.</p>",
    },
    {
        "text": "<p>In solving a radical equation, into which equation should each "
                "candidate be substituted?</p>",
        "choices": ["The original equation, before squaring",
                    "The squared equation",
                    "The simplified quadratic",
                    "Either one — they are equivalent"],
        "correct": "The original equation, before squaring",
        "explanation": "<p><strong>Asl tenglamaga.</strong> Kvadratlangan tenglama "
                       "begona ildizni ham qabul qiladi.</p>"
                       "<p><strong>Either one</strong> — aynan shu xato: ular teng "
                       "kuchli EMAS.</p>",
    },
    {
        "text": "<p>Without solving, which value cannot be a solution of "
                "√(<i>x</i> + 1) = <i>x</i> − 4?</p>",
        "choices": ["x = 3", "x = 5", "x = 8", "x = 15"],
        "correct": "x = 3",
        "explanation": "<p><strong>x = 3.</strong> Oʻng tomon 3 − 4 = −1, manfiy — "
                       "ildiz esa manfiy boʻlmaydi.</p>"
                       "<p>Bu tez tekshiruv: oʻng tomoni manfiy chiqadigan har "
                       "qanday nomzod darrov oʻchadi.</p>",
    },
    {
        "text": "<p>For √(<i>x</i> − 5) to be a real number, what must be true?</p>",
        "choices": ["x is at least 5", "x is at most 5", "x is positive",
                    "x is not zero"],
        "correct": "x is at least 5",
        "explanation": "<p><strong>x ≥ 5.</strong> Ildiz ostidagi ifoda manfiy "
                       "boʻlmasligi kerak: x − 5 ≥ 0.</p>"
                       "<p>Bu ham nomzodlarni oldindan oʻchirishga yordam "
                       "beradi.</p>",
    },
    {
        "text": "<p>A student solves √(<i>x</i> + 6) = <i>x</i> and answers "
                "'<i>x</i> = 3 and <i>x</i> = −2'. What is the correct answer?</p>",
        "choices": ["x = 3", "x = −2", "x = 3 and x = −2", "There is no solution"],
        "correct": "x = 3",
        "explanation": "<p><strong>x = 3.</strong> Oʻquvchi tekshirishni "
                       "tashlab ketgan.</p>"
                       "<p>x = −2 da chap tomon √4 = 2, oʻng tomon −2 — teng "
                       "emas.</p>",
    },
    {
        "text": "<p>A student writes √(<i>x</i> + 5) = <i>x</i> + 1, then "
                "<i>x</i> + 5 = <i>x</i><sup>2</sup> + 1. What is the correct second "
                "line?</p>",
        "choices": ["x + 5 = x² + 2x + 1", "x + 5 = x² + 1", "x + 5 = x² − 2x + 1",
                    "x + 5 = 2x + 1"],
        "correct": "x + 5 = x² + 2x + 1",
        "explanation": "<p><strong>x + 5 = x² + 2x + 1.</strong> "
                       "(x + 1)² = x² + 2x + 1 — oʻrtadagi had tushib qolgan "
                       "(SAT-30).</p>"
                       "<p>Bu bu mavzudagi eng koʻp uchraydigan hisob xatosi.</p>",
    },
    {
        "text": "<p>What is the solution to √(<i>x</i> + 9) = <i>x</i> − 3?</p>",
        "choices": ["x = 7", "x = 7 and x = 0", "x = 0", "There is no solution"],
        "correct": "x = 7",
        "explanation": "<p><strong>x = 7.</strong> x + 9 = x² − 6x + 9 → "
                       "x² − 7x = 0 → x = 7 yoki 0.</p>"
                       "<p>x = 0: √9 = 3, lekin 0 − 3 = −3 ✗</p>",
    },
    {
        "text": "<p>What is the sum of all real solutions of √(3<i>x</i> + 1) = "
                "<i>x</i> − 1?</p>",
        "choices": ["5", "6", "1", "0"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 3x + 1 = x² − 2x + 1 → x² − 5x = 0 → "
                       "x = 5 yoki 0; x = 0 da √1 = 1 ≠ −1 ✗</p>"
                       "<p>Faqat bitta yechim qolgani uchun yigʻindi 5. "
                       "<strong>6</strong> — begona ildiz ham qoʻshilgan (5 + 1).</p>",
    },
    {
        "text": "<p>The time in seconds for an object to fall <i>d</i> metres is "
                "<i>t</i> = √(<i>d</i> ÷ 5). If the fall takes 4 seconds, what is the "
                "distance?</p>",
        "choices": ["80 metres", "20 metres", "16 metres", "3.2 metres"],
        "correct": "80 metres",
        "explanation": "<p><strong>80 metr.</strong> 4 = √(d ÷ 5) → 16 = d ÷ 5 → "
                       "d = 80.</p>"
                       "<p><strong>20</strong> — kvadratga koʻtarish unutilgan "
                       "(4 × 5).</p>",
    },
    {
        "text": "<p>A rope of length √(<i>x</i> + 40) metres is stretched, and its "
                "length equals <i>x</i> − 2 metres. What is <i>x</i>?</p>",
        "choices": ["9", "9 and −4", "−4", "There is no solution"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> x + 40 = x² − 4x + 4 → "
                       "x² − 5x − 36 = 0 → x = 9 yoki −4.</p>"
                       "<p>x = −4: √36 = 6, lekin −4 − 2 = −6 ✗ — bundan tashqari "
                       "uzunlik manfiy boʻlmaydi.</p>",
    },
]


# =====================================================================
# SAT-40 — rational equations and domain restrictions
# =====================================================================

Q_SAT40 = [
    {
        "text": "<p>For what value of <i>x</i> is 1 ÷ (<i>x</i> − 4) undefined?</p>",
        "choices": ["x = 4", "x = −4", "x = 0", "x = 1"],
        "correct": "x = 4",
        "explanation": "<p><strong>x = 4.</strong> Maxraj nolga aylanadi.</p>"
                       "<p>Nolga boʻlish aniqlanmagan — shuning uchun bu qiymat "
                       "taqiqlangan.</p>",
    },
    {
        "text": "<p>For what values of <i>x</i> is 3 ÷ (<i>x</i><sup>2</sup> − 25) "
                "undefined?</p>",
        "choices": ["x = 5 and x = −5", "x = 25", "x = 5 only", "x = 0"],
        "correct": "x = 5 and x = −5",
        "explanation": "<p><strong>x = ±5.</strong> x² − 25 = (x − 5)(x + 5) — "
                       "ikkita taqiq.</p>"
                       "<p><strong>x = 5 only</strong> — manfiy variant unutilgan; "
                       "maxrajni ajratib yozing.</p>",
    },
    {
        "text": "<p>For what values of <i>x</i> is <i>x</i> ÷ ((<i>x</i> − 1)"
                "(<i>x</i> + 6)) undefined?</p>",
        "choices": ["x = 1 and x = −6", "x = −1 and x = 6", "x = 0",
                    "x = 1 and x = 6"],
        "correct": "x = 1 and x = −6",
        "explanation": "<p><strong>x = 1 va x = −6.</strong> Har bir qavsni nolga "
                       "tenglashtiring.</p>"
                       "<p>Surat nolga aylanishi muammo emas — faqat maxraj "
                       "muhim.</p>",
    },
    {
        "text": "<p>What is the domain of 2 ÷ (<i>x</i> + 3)?</p>",
        "choices": ["All real numbers except −3", "All real numbers except 3",
                    "All positive numbers", "All real numbers"],
        "correct": "All real numbers except −3",
        "explanation": "<p><strong>−3 dan tashqari barcha sonlar.</strong> "
                       "x + 3 = 0 → x = −3.</p>"
                       "<p>Ishoraga eʼtibor bering: qavsdagi +3 taqiqni −3 "
                       "qiladi.</p>",
    },
    {
        "text": "<p>What is the solution to 1 ÷ (<i>x</i> − 2) = 3 ÷ (<i>x</i> + 2)?</p>",
        "choices": ["x = 4", "x = 2", "x = −2", "There is no solution"],
        "correct": "x = 4",
        "explanation": "<p><strong>x = 4.</strong> Krest koʻpaytirish: x + 2 = "
                       "3(x − 2) → x + 2 = 3x − 6 → x = 4.</p>"
                       "<p>Tekshiruv: 1/2 = 3/6 ✓ va 4 taqiqlanmagan ✓</p>",
    },
    {
        "text": "<p>What is the solution to 2 ÷ (<i>x</i> + 1) = 4 ÷ (<i>x</i> + 5)?</p>",
        "choices": ["x = 3", "x = −1", "x = 1", "There is no solution"],
        "correct": "x = 3",
        "explanation": "<p><strong>x = 3.</strong> 2(x + 5) = 4(x + 1) → "
                       "2x + 10 = 4x + 4 → x = 3.</p>"
                       "<p>Tekshiruv: 2/4 = 4/8 ✓</p>",
    },
    {
        "text": "<p>What is the solution to <i>x</i> ÷ (<i>x</i> − 4) = 4 ÷ "
                "(<i>x</i> − 4)?</p>",
        "choices": ["There is no solution", "x = 4", "x = 0", "x = 8"],
        "correct": "There is no solution",
        "explanation": "<p><strong>Yechim yoʻq.</strong> Algebra x = 4 beradi, lekin "
                       "x = 4 da maxraj nolga aylanadi.</p>"
                       "<p>Aynan shu sabab taqiqlarni yechishdan <b>oldin</b> yozib "
                       "qoʻyish kerak.</p>",
    },
    {
        "text": "<p>What is the solution to 1 ÷ <i>x</i> + 1 ÷ (2<i>x</i>) = 3?</p>",
        "choices": ["x = 0.5", "x = 1", "x = 2", "x = 1.5"],
        "correct": "x = 0.5",
        "explanation": "<p><strong>x = 0.5.</strong> Umumiy maxraj 2x: "
                       "(2 + 1) ÷ (2x) = 3 → 3 = 6x → x = 0.5.</p>"
                       "<p>Tekshiruv: 2 + 1 = 3 ✓ va 0.5 taqiqlanmagan (x ≠ 0)</p>",
    },
    {
        "text": "<p>What is the solution to (<i>x</i> + 6) ÷ (<i>x</i> − 2) = 4?</p>",
        "choices": ["x = 14/3", "x = 2", "x = 14", "There is no solution"],
        "correct": "x = 14/3",
        "explanation": "<p><strong>x = 14/3.</strong> x + 6 = 4(x − 2) → "
                       "x + 6 = 4x − 8 → 3x = 14.</p>"
                       "<p>Taxminan 4.67, va u 2 ga teng emas ✓</p>",
    },
    {
        "text": "<p>What is the solution to 5 ÷ (<i>x</i> − 3) = 1?</p>",
        "choices": ["x = 8", "x = 3", "x = 5", "x = 2"],
        "correct": "x = 8",
        "explanation": "<p><strong>x = 8.</strong> 5 = x − 3 → x = 8.</p>"
                       "<p>Tekshiruv: 5 ÷ 5 = 1 ✓</p>",
    },
    {
        "text": "<p>Is (<i>x</i><sup>2</sup> − 9) ÷ (<i>x</i> − 3) the same expression "
                "as <i>x</i> + 3?</p>",
        "choices": ["Almost — they agree everywhere except at x = 3",
                    "Yes, they are identical",
                    "No, they are never equal",
                    "They agree only for positive x"],
        "correct": "Almost — they agree everywhere except at x = 3",
        "explanation": "<p><strong>x = 3 dan tashqari hamma joyda teng.</strong> "
                       "Asl ifoda x = 3 da aniqlanmagan, x + 3 esa 6 beradi.</p>"
                       "<p>Qisqartirish taqiqni oʻchirmaydi.</p>",
    },
    {
        "text": "<p>Why must you list excluded values before solving a rational "
                "equation?</p>",
        "choices": ["Because the algebra can produce an answer that is excluded",
                    "Because it makes the arithmetic easier",
                    "Because the denominators disappear",
                    "Because the equation may have two solutions"],
        "correct": "Because the algebra can produce an answer that is excluded",
        "explanation": "<p><strong>Javob taqiqlangan qiymat chiqishi mumkin.</strong> "
                       "U holda toʻgʻri javob «no solution».</p>"
                       "<p>Taqiqni oldindan yozmasangiz, buni sezmay qolasiz.</p>",
    },
    {
        "text": "<p>A rate problem gives <i>t</i> = 120 ÷ <i>v</i>, where <i>v</i> is "
                "speed. What value of <i>v</i> is not allowed?</p>",
        "choices": ["v = 0", "v = 120", "v = 1", "None — all values are allowed"],
        "correct": "v = 0",
        "explanation": "<p><strong>v = 0.</strong> Maxraj nolga aylanadi — va "
                       "maʼnosi ham bor: harakatsiz jism manzilga hech qachon "
                       "yetmaydi.</p>"
                       "<p>Bu yerda matematik taqiq va hayotdagi maʼno mos "
                       "keladi.</p>",
    },
    {
        "text": "<p>For which values is (<i>x</i> + 1) ÷ (<i>x</i><sup>2</sup> − "
                "<i>x</i>) undefined?</p>",
        "choices": ["x = 0 and x = 1", "x = −1", "x = 1 only", "x = 0 only"],
        "correct": "x = 0 and x = 1",
        "explanation": "<p><strong>x = 0 va x = 1.</strong> x² − x = x(x − 1) — "
                       "umumiy koʻpaytuvchini chiqaring (SAT-29).</p>"
                       "<p>Maxrajni ajratmasangiz bitta taqiqni oson boy "
                       "berasiz.</p>",
    },
    {
        "text": "<p>A student solves <i>x</i> ÷ (<i>x</i> − 6) = 6 ÷ (<i>x</i> − 6) and "
                "answers <i>x</i> = 6. What is the correct answer?</p>",
        "choices": ["There is no solution", "x = 6", "x = 0", "x = 12"],
        "correct": "There is no solution",
        "explanation": "<p><strong>Yechim yoʻq.</strong> x = 6 taqiqlangan qiymat.</p>"
                       "<p>Oʻquvchining algebrasi toʻgʻri — faqat oxirgi tekshiruv "
                       "qilinmagan.</p>",
    },
    {
        "text": "<p>A student says 4 ÷ (<i>x</i><sup>2</sup> − 36) is undefined at "
                "<i>x</i> = 36. What is the correct answer?</p>",
        "choices": ["x = 6 and x = −6", "x = 36", "x = 6 only", "x = 18"],
        "correct": "x = 6 and x = −6",
        "explanation": "<p><strong>x = ±6.</strong> Maxraj nolga aylanadigan qiymat "
                       "kerak, maxrajning oʻzi emas.</p>"
                       "<p>x = 36 da maxraj 1,296 − 36 — noldan juda uzoq.</p>",
    },
    {
        "text": "<p>What is the solution to 1 ÷ (<i>x</i> − 1) + 2 ÷ (<i>x</i> − 1) "
                "= 3?</p>",
        "choices": ["x = 2", "x = 1", "x = 3", "There is no solution"],
        "correct": "x = 2",
        "explanation": "<p><strong>x = 2.</strong> Maxrajlar bir xil: "
                       "3 ÷ (x − 1) = 3 → x − 1 = 1.</p>"
                       "<p>2 taqiqlanmagan (x ≠ 1) ✓</p>",
    },
    {
        "text": "<p>What is the solution to (2<i>x</i> + 1) ÷ (<i>x</i> − 3) = 2?</p>",
        "choices": ["There is no solution", "x = 3", "x = 7", "x = −7"],
        "correct": "There is no solution",
        "explanation": "<p><strong>Yechim yoʻq.</strong> 2x + 1 = 2(x − 3) → "
                       "2x + 1 = 2x − 6 → 1 = −6, yolgʻon tenglik.</p>"
                       "<p>x butunlay yoʻqoldi — demak hech qanday x tenglamani "
                       "qanoatlantirmaydi.</p>",
    },
    {
        "text": "<p>Two workers paint a wall. Together their rate is 1 ÷ <i>x</i> + "
                "1 ÷ (<i>x</i> + 5) walls per hour. Which values of <i>x</i> are not "
                "allowed?</p>",
        "choices": ["x = 0 and x = −5", "x = 5 only", "x = 0 only", "x = −5 only"],
        "correct": "x = 0 and x = −5",
        "explanation": "<p><strong>x = 0 va x = −5.</strong> Ikkala maxraj ham "
                       "tekshiriladi.</p>"
                       "<p>Kontekstda x manfiy ham boʻlmaydi (vaqt), lekin savol "
                       "matematik taqiqni soʻragan.</p>",
    },
    {
        "text": "<p>A car travels 150 kilometres at speed <i>v</i>, and the trip takes "
                "150 ÷ <i>v</i> hours. If the trip takes 2.5 hours, what is "
                "<i>v</i>?</p>",
        "choices": ["60 km/h", "375 km/h", "6 km/h", "75 km/h"],
        "correct": "60 km/h",
        "explanation": "<p><strong>60 km/soat.</strong> 150 ÷ v = 2.5 → "
                       "v = 150 ÷ 2.5 = 60.</p>"
                       "<p><strong>375</strong> — boʻlish oʻrniga koʻpaytirilgan "
                       "(150 × 2.5).</p>",
    },
]


# =====================================================================
# Testlar
# =====================================================================

PRACTICES = [
    {
        "title":       "SAT-36 Practice: Finding Maximum and Minimum Values of a Quadratic",
        "description": "20 ta SAT uslubidagi savol — matndan model tuzish, uchni topish "
                       "va savol x ni yoki y ni soʻrayotganini ajratish.",
        "tutorial":    "SAT-36:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT36,
    },
    {
        "title":       "SAT-37 Practice: Graphing Parabolas — Intercepts, Vertex, and Symmetry",
        "description": "20 ta SAT uslubidagi savol — y oʻqidagi nuqta, nollar, uch va "
                       "simmetriya; qaysi koʻrinish nimani koʻrsatadi.",
        "tutorial":    "SAT-37:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT37,
    },
    {
        "title":       "SAT-38 Practice: Systems of Non-Linear Equations (Linear–Quadratic)",
        "description": "20 ta SAT uslubidagi savol — oʻrniga qoʻyish, javob nuqta "
                       "ekani va kesishishlar sonini diskriminant bilan aytish.",
        "tutorial":    "SAT-38:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT38,
    },
    {
        "title":       "SAT-39 Practice: Radical Equations and Extraneous Solutions",
        "description": "20 ta SAT uslubidagi savol — ildizni yolgʻiz qoldirish, "
                       "kvadratga koʻtarish va har bir ildizni asl tenglamada tekshirish.",
        "tutorial":    "SAT-39:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT39,
    },
    {
        "title":       "SAT-40 Practice: Rational Equations and Domain Restrictions",
        "description": "20 ta SAT uslubidagi savol — taqiqlangan qiymatlar, krest "
                       "koʻpaytirish va «no solution» qachon toʻgʻri javob ekani.",
        "tutorial":    "SAT-40:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT40,
    },
]
