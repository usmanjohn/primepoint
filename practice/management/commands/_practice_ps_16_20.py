# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-16 … SAT-20 (tenglamalar sistemasi).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context & interpretation ·
      15–16 trap-spotting · 17–18 Module 2 level · 19–20 word problems.

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA. Son: 3.5 va 1,200.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_16_20.py --master=prime \\
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
# SAT-16 — substitution
# =====================================================================

Q_SAT16 = [
    {
        "text": "<p><i>y</i> = <i>x</i> + 3</p><p><i>x</i> + <i>y</i> = 9</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["3", "6", "9", "12"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> y ning oʻrniga x + 3 ni qoʻyamiz: "
                       "x + (x + 3) = 9 → 2x = 6 → x = 3.</p>"
                       "<p><strong>6</strong> — bu <i>y</i> ning qiymati. Sistemada ikki "
                       "javob bor, savol qaysi birini soʻraganiga qarang.</p>",
    },
    {
        "text": "<p><i>y</i> = 2<i>x</i></p><p><i>x</i> + <i>y</i> = 12</p>"
                "<p>What is the value of <i>y</i>?</p>",
        "choices": ["4", "6", "8", "12"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> x + 2x = 12 → 3x = 12 → x = 4, demak "
                       "y = 2(4) = 8.</p>"
                       "<p><strong>4</strong> — bu <i>x</i>; <strong>6</strong> — "
                       "12 ni ikkiga boʻlgan javob, lekin ikki son teng emas.</p>",
    },
    {
        "text": "<p><i>x</i> = <i>y</i> + 5</p><p><i>x</i> + <i>y</i> = 11</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["3", "5", "8", "11"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> (y + 5) + y = 11 → 2y = 6 → y = 3, "
                       "demak x = 8.</p>"
                       "<p><strong>3</strong> — bu <i>y</i>; <strong>5</strong> — ikki "
                       "son orasidagi farq.</p>",
    },
    {
        "text": "<p>Which ordered pair is the solution to <i>y</i> = <i>x</i> − 1 and "
                "<i>x</i> + <i>y</i> = 7?</p>",
        "choices": ["(3, 4)", "(4, 3)", "(5, 2)", "(7, 6)"],
        "correct": "(4, 3)",
        "explanation": "<p><strong>(4, 3).</strong> x + (x − 1) = 7 → 2x = 8 → x = 4, "
                       "y = 3.</p>"
                       "<p><strong>(3, 4)</strong> — koordinatalar almashtirilgan: "
                       "tartib har doim (x, y).</p>",
    },
    {
        "text": "<p><i>y</i> = 3<i>x</i> + 1</p><p>2<i>x</i> + <i>y</i> = 11</p>"
                "<p>What is the value of <i>x</i> + <i>y</i>?</p>",
        "choices": ["2", "7", "9", "11"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> 2x + (3x + 1) = 11 → 5x = 10 → x = 2, "
                       "y = 7, va x + y = 9.</p>"
                       "<p><strong>2</strong> va <strong>7</strong> — alohida "
                       "javoblar; savol ularning <b>yigʻindisini</b> soʻradi.</p>",
    },
    {
        "text": "<p><i>x</i> = 4<i>y</i></p><p>2<i>x</i> + <i>y</i> = 27</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["3", "9", "12", "27"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 2(4y) + y = 27 → 9y = 27 → y = 3, "
                       "demak x = 4(3) = 12.</p>"
                       "<p><strong>3</strong> — bu <i>y</i>: oxirgi qadamni "
                       "(orqaga qoʻyishni) qilish shart.</p>",
    },
    {
        "text": "<p><i>y</i> = 5 − 2<i>x</i></p><p>3<i>x</i> + <i>y</i> = 8</p>"
                "<p>What is the value of <i>y</i>?</p>",
        "choices": ["−1", "1", "3", "5"],
        "correct": "−1",
        "explanation": "<p><strong>−1.</strong> 3x + (5 − 2x) = 8 → x + 5 = 8 → x = 3, "
                       "demak y = 5 − 6 = −1.</p>"
                       "<p><strong>3</strong> — bu <i>x</i>. Manfiy javobdan "
                       "qoʻrqmang: sistemaning yechimi manfiy boʻlishi mutlaqo "
                       "normal.</p>",
    },
    {
        "text": "<p>2<i>x</i> + <i>y</i> = 10</p><p><i>y</i> = <i>x</i> + 1</p>"
                "<p>What is the value of <i>y</i>?</p>",
        "choices": ["3", "4", "7", "10"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 2x + (x + 1) = 10 → 3x = 9 → x = 3, "
                       "demak y = 4.</p>"
                       "<p><strong>3</strong> — bu <i>x</i>. Har safar orqaga "
                       "qoʻyganingizdan keyin «qaysi harf soʻralgan edi?» deb "
                       "soʻrang.</p>",
    },
    {
        "text": "<p><i>x</i> + 3<i>y</i> = 14</p><p><i>x</i> = 2<i>y</i> − 1</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["3", "5", "8", "14"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> (2y − 1) + 3y = 14 → 5y = 15 → y = 3, "
                       "demak x = 2(3) − 1 = 5.</p>"
                       "<p><strong>3</strong> — bu <i>y</i>; <strong>8</strong> — "
                       "x + y ning qiymati.</p>",
    },
    {
        "text": "<p>Which point satisfies both <i>y</i> = 2<i>x</i> − 1 and "
                "<i>x</i> + <i>y</i> = 5?</p>",
        "choices": ["(1, 1)", "(2, 3)", "(3, 2)", "(4, 7)"],
        "correct": "(2, 3)",
        "explanation": "<p><strong>(2, 3).</strong> 2(2) − 1 = 3 ✓ va 2 + 3 = 5 ✓ — "
                       "ikkala tenglama ham rost.</p>"
                       "<p><strong>(3, 2)</strong> ikkinchi tenglamani "
                       "qanoatlantiradi (3 + 2 = 5), lekin birinchisini emas: "
                       "2(3) − 1 = 5, 2 emas.</p>",
    },
    {
        "text": "<p>A number <i>y</i> is 4 more than a number <i>x</i>, and their sum is "
                "20. What is the larger number?</p>",
        "choices": ["4", "8", "12", "20"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> y = x + 4 va x + y = 20 → x + x + 4 = 20 "
                       "→ x = 8, y = 12.</p>"
                       "<p><strong>8</strong> — kichigi. «Larger» soʻzi qaysi javobni "
                       "belgilashni aytadi.</p>",
    },
    {
        "text": "<p>What does the solution to a system of two linear equations represent "
                "on a graph?</p>",
        "choices": ["The point where the two lines cross",
                    "The slope of the first line",
                    "The y-intercept of the second line",
                    "The distance between the two lines"],
        "correct": "The point where the two lines cross",
        "explanation": "<p><strong>Ikki chiziqning kesishgan nuqtasi.</strong> Yechim "
                       "ikkala tenglamani ham rost qiladi, demak u ikkala chiziqda "
                       "ham yotadi.</p>"
                       "<p>Shuning uchun yechim son emas, <b>nuqta</b>: (x, y).</p>",
    },
    {
        "text": "<p>A 24-metre rope is cut into two pieces, one of which is 6 metres "
                "longer than the other. How long is the shorter piece?</p>",
        "choices": ["9", "12", "15", "18"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> x + y = 24 va y = x + 6 → x + x + 6 = 24 "
                       "→ 2x = 18 → x = 9 (uzunrogʻi 15).</p>"
                       "<p><strong>15</strong> — uzun boʻlagi; <strong>12</strong> — "
                       "arqonni teng ikkiga boʻlgan javob, lekin boʻlaklar teng "
                       "emas.</p>",
    },
    {
        "text": "<p><i>y</i> = 3<i>x</i></p><p><i>x</i> + <i>y</i> = 16</p>"
                "<p>What is the value of <i>y</i> − <i>x</i>?</p>",
        "choices": ["4", "8", "12", "16"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> x + 3x = 16 → x = 4, y = 12, demak "
                       "y − x = 8.</p>"
                       "<p><strong>12</strong> — bu <i>y</i>; <strong>4</strong> — "
                       "bu <i>x</i>. Savol <b>ayirmani</b> soʻradi.</p>",
    },
    {
        "text": "<p><i>y</i> = <i>x</i> + 2</p><p>3<i>x</i> + <i>y</i> = 14</p>"
                "<p>What is the value of 2<i>y</i>?</p>",
        "choices": ["3", "5", "8", "10"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 3x + x + 2 = 14 → 4x = 12 → x = 3, "
                       "y = 5, demak 2y = 10.</p>"
                       "<p><strong>5</strong> — bu <i>y</i> ning oʻzi. SAT oxirgi "
                       "qadamni qoʻshib qoʻyadi va koʻp oʻquvchi uni oʻqimaydi.</p>",
    },
    {
        "text": "<p><i>x</i> = 3<i>y</i></p><p><i>x</i> + <i>y</i> = 16</p>"
                "<p>If (<i>a</i>, <i>b</i>) is the solution to the system, what is the "
                "value of <i>b</i>?</p>",
        "choices": ["4", "8", "12", "16"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 3y + y = 16 → y = 4, x = 12. "
                       "(a, b) = (x, y), demak b = <b>4</b>.</p>"
                       "<p><strong>12</strong> — bu <i>a</i>. Harflar oʻzgarganda ham "
                       "tartib oʻsha: birinchisi x, ikkinchisi y.</p>",
    },
    {
        "text": "<p>3<i>x</i> − <i>y</i> = 7</p><p><i>y</i> = 2<i>x</i> − 3</p>"
                "<p>What is the value of <i>x</i> + <i>y</i>?</p>",
        "choices": ["4", "5", "9", "12"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> 3x − (2x − 3) = 7 → x + 3 = 7 → x = 4, "
                       "y = 5, va x + y = 9.</p>"
                       "<p>Qavsga eʼtibor bering: −(2x − 3) = −2x <b>+</b> 3. Qavssiz "
                       "qoʻyish javobni butunlay oʻzgartiradi.</p>",
    },
    {
        "text": "<p><i>x</i> + 2<i>y</i> = 11</p><p><i>x</i> = 3<i>y</i> + 1</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["2", "5", "7", "11"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> (3y + 1) + 2y = 11 → 5y = 10 → y = 2, "
                       "demak x = 3(2) + 1 = 7.</p>"
                       "<p><strong>2</strong> — bu <i>y</i>. Tekshiruv: 7 + 2(2) = 11 "
                       "✓</p>",
    },
    {
        "text": "<p>Two numbers have a sum of 30, and one number is twice the other. "
                "What is the larger number?</p>",
        "choices": ["10", "15", "20", "30"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> x + 2x = 30 → x = 10, ikkinchisi 20.</p>"
                       "<p><strong>15</strong> — 30 ni teng ikkiga boʻlgan javob, lekin "
                       "sonlar teng emas; <strong>10</strong> — kichigi.</p>",
    },
    {
        "text": "<p>A father is three times as old as his son. Together their ages total "
                "48 years. How old is the son?</p>",
        "choices": ["12", "16", "24", "36"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> s + 3s = 48 → 4s = 48 → s = 12 "
                       "(otasi 36 yoshda).</p>"
                       "<p><strong>36</strong> — otasining yoshi; <strong>16</strong> — "
                       "48 ni uchga boʻlgan javob, lekin nisbat 1 : 3, yaʼni jami "
                       "<b>toʻrt</b> ulush.</p>",
    },
]


# =====================================================================
# SAT-17 — elimination
# =====================================================================

Q_SAT17 = [
    {
        "text": "<p><i>x</i> + <i>y</i> = 8</p><p><i>x</i> − <i>y</i> = 2</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["3", "5", "6", "8"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Qoʻshamiz: 2x = 10 → x = 5 (va y = 3).</p>"
                       "<p><strong>3</strong> — bu <i>y</i>; <strong>10</strong> "
                       "boʻlmagani yaxshi, chunki 2x = 10 da toʻxtash ham xato "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>2<i>x</i> + <i>y</i> = 9</p><p><i>x</i> − <i>y</i> = 3</p>"
                "<p>What is the value of <i>y</i>?</p>",
        "choices": ["1", "3", "4", "9"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> Qoʻshamiz: 3x = 12 → x = 4, keyin "
                       "4 − y = 3 → y = 1.</p>"
                       "<p><strong>4</strong> — bu <i>x</i>. Qoʻshish x ni beradi, "
                       "y esa orqaga qoʻyishdan chiqadi.</p>",
    },
    {
        "text": "<p>3<i>x</i> + 2<i>y</i> = 13</p><p>3<i>x</i> − 2<i>y</i> = 5</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["2", "3", "5", "6"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> +2y va −2y qarama-qarshi: qoʻshsak "
                       "6x = 18 → x = 3 (va y = 2).</p>"
                       "<p><strong>6</strong> — 6x dagi koeffitsient; oxirgi boʻlishni "
                       "unutmang.</p>",
    },
    {
        "text": "<p>To eliminate <i>y</i> from <i>x</i> + <i>y</i> = 7 and "
                "<i>x</i> − <i>y</i> = 1, what should you do?</p>",
        "choices": ["Add the two equations", "Subtract the two equations",
                    "Multiply the first equation by 2", "Divide the second equation by 2"],
        "correct": "Add the two equations",
        "explanation": "<p><strong>Qoʻshish.</strong> y ning koeffitsientlari +1 va −1 — "
                       "qarama-qarshi, demak qoʻshganda yoʻqoladi.</p>"
                       "<p>Ayirish bu yerda 2y beradi, yaʼni y yoʻqolmaydi.</p>",
    },
    {
        "text": "<p>5<i>x</i> + 2<i>y</i> = 16</p><p>3<i>x</i> − 2<i>y</i> = 0</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["2", "3", "8", "16"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Qoʻshamiz: 8x = 16 → x = 2 (va y = 3).</p>"
                       "<p><strong>3</strong> — bu <i>y</i>; <strong>16</strong> — "
                       "boʻlishdan oldingi son.</p>",
    },
    {
        "text": "<p>4<i>x</i> + <i>y</i> = 14</p><p>2<i>x</i> + <i>y</i> = 8</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["2", "3", "6", "11"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Koeffitsientlar <b>bir xil</b> (+y va +y), "
                       "shuning uchun ayiramiz: 2x = 6 → x = 3 (va y = 2).</p>"
                       "<p><strong>2</strong> — bu <i>y</i>. Bir xil koeffitsientda "
                       "qoʻshish emas, ayirish kerak.</p>",
    },
    {
        "text": "<p><i>x</i> + 3<i>y</i> = 10</p><p><i>x</i> + <i>y</i> = 6</p>"
                "<p>What is the value of <i>y</i>?</p>",
        "choices": ["2", "4", "6", "10"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Ayiramiz: 2y = 4 → y = 2 (va x = 4).</p>"
                       "<p><strong>4</strong> — bu <i>x</i>, yoki ayirishdan keyingi "
                       "oʻng tomon. Har ikki holatda ham oxirgi qadam qolgan.</p>",
    },
    {
        "text": "<p>2<i>x</i> + <i>y</i> = 8</p><p>3<i>x</i> + 2<i>y</i> = 14</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["2", "4", "6", "14"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Birinchisini 2 ga koʻpaytiramiz: "
                       "4x + 2y = 16, keyin ikkinchisini ayiramiz: x = 2 (va y = 4).</p>"
                       "<p><strong>4</strong> — bu <i>y</i>. Koʻpaytirganda oʻng tomon "
                       "ham koʻpayadi: 8 × 2 = 16.</p>",
    },
    {
        "text": "<p><i>x</i> + 4<i>y</i> = 18</p><p>3<i>x</i> − 2<i>y</i> = 12</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["3", "6", "7", "18"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Ikkinchisini 2 ga koʻpaytiramiz: "
                       "6x − 4y = 24, keyin qoʻshamiz: 7x = 42 → x = 6 (va y = 3).</p>"
                       "<p><strong>3</strong> — bu <i>y</i>. Bu yerda koʻpaytirish "
                       "<b>ikkinchi</b> tenglamaga qilindi, chunki 4y va 2y ni "
                       "moslashtirish osonroq edi.</p>",
    },
    {
        "text": "<p>4<i>x</i> + 3<i>y</i> = 17</p><p>3<i>x</i> + 4<i>y</i> = 11</p>"
                "<p>What is the value of <i>x</i> + <i>y</i>?</p>",
        "choices": ["4", "7", "14", "28"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Qoʻshamiz: 7x + 7y = 28, keyin 7 ga "
                       "boʻlamiz: x + y = 4. Alohida yechish shart emas.</p>"
                       "<p><strong>28</strong> — boʻlishdan oldingi son. Simmetrik "
                       "koeffitsientlar (4, 3 va 3, 4) shu qisqa yoʻlning belgisi.</p>",
    },
    {
        "text": "<p>Adding two equations of a system gives 5<i>x</i> + 5<i>y</i> = 35. "
                "What is the value of <i>x</i> + <i>y</i>?</p>",
        "choices": ["5", "7", "30", "35"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Hamma hadni 5 ga boʻlamiz: "
                       "x + y = 7.</p>"
                       "<p><strong>35</strong> — boʻlishdan oldingi son. SAT bu qadamni "
                       "qilmaganlar uchun uni albatta variantlar orasiga qoʻyadi.</p>",
    },
    {
        "text": "<p>Why is one equation sometimes multiplied before the equations are "
                "added?</p>",
        "choices": ["To make one variable's coefficients match",
                    "To make the numbers smaller",
                    "To change the solution of the system",
                    "To turn the system into a single equation with two unknowns"],
        "correct": "To make one variable's coefficients match",
        "explanation": "<p><strong>Koeffitsientlarni moslashtirish uchun.</strong> "
                       "Faqat mos (bir xil yoki qarama-qarshi) koeffitsientlargina "
                       "qoʻshish yoki ayirishda yoʻqoladi.</p>"
                       "<p>Koʻpaytirish yechimni <b>oʻzgartirmaydi</b> — u tenglamaning "
                       "faqat koʻrinishini oʻzgartiradi.</p>",
    },
    {
        "text": "<p>6<i>x</i> + 5<i>y</i> = 40</p><p>6<i>x</i> − 5<i>y</i> = 20</p>"
                "<p>What is the value of <i>y</i>?</p>",
        "choices": ["2", "5", "10", "20"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Qoʻshamiz: 12x = 60 → x = 5, keyin "
                       "30 + 5y = 40 → y = 2.</p>"
                       "<p><strong>5</strong> — bu <i>x</i>. Yoki ayirish bilan: "
                       "10y = 20 → y = 2 — bir xil javob, qisqaroq yoʻl.</p>",
    },
    {
        "text": "<p>The sum of two numbers is 25 and their difference is 9. What is the "
                "larger number?</p>",
        "choices": ["8", "9", "16", "17"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> x + y = 25 va x − y = 9 → qoʻshamiz: "
                       "2x = 34 → x = 17 (va y = 8).</p>"
                       "<p><strong>8</strong> — kichigi; <strong>16</strong> — 25 − 9, "
                       "yaʼni ayirishni notoʻgʻri qoʻllagan javob.</p>",
    },
    {
        "text": "<p>3<i>x</i> + 2<i>y</i> = 19</p><p>3<i>x</i> − 2<i>y</i> = 5</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["3.5", "4", "12", "24"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Qoʻshamiz: 6x = 24 → x = 4 "
                       "(va y = 3.5).</p>"
                       "<p><strong>24</strong> — boʻlishdan oldingi son; "
                       "<strong>3.5</strong> — bu <i>y</i>, x emas. Kasr javob "
                       "sistemada mutlaqo normal.</p>",
    },
    {
        "text": "<p>2<i>x</i> + 5<i>y</i> = 21</p><p>2<i>x</i> + 3<i>y</i> = 15</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["3", "4.5", "6", "18"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Ayiramiz: 2y = 6 → y = 3, keyin "
                       "2x + 9 = 15 → x = 3.</p>"
                       "<p>Bu yerda <i>x</i> va <i>y</i> tasodifan teng chiqdi — "
                       "shuning uchun javobni <b>ikkala</b> tenglamada tekshirish "
                       "kerak: 2(3) + 5(3) = 21 ✓</p>",
    },
    {
        "text": "<p>3<i>x</i> + 4<i>y</i> = 10</p><p>2<i>x</i> + <i>y</i> = 5</p>"
                "<p>What is the value of <i>x</i>?</p>",
        "choices": ["1", "2", "5", "20"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Ikkinchisini 4 ga koʻpaytiramiz: "
                       "8x + 4y = 20, keyin birinchisini ayiramiz: 5x = 10 → x = 2 "
                       "(va y = 1).</p>"
                       "<p><strong>1</strong> — bu <i>y</i>; <strong>20</strong> — "
                       "koʻpaytirilgan tenglamaning oʻng tomoni.</p>",
    },
    {
        "text": "<p>5<i>x</i> + 4<i>y</i> = 20</p><p>4<i>x</i> + 5<i>y</i> = 16</p>"
                "<p>What is the value of <i>x</i> + <i>y</i>?</p>",
        "choices": ["4", "9", "18", "36"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Qoʻshamiz: 9x + 9y = 36, keyin 9 ga "
                       "boʻlamiz: x + y = 4.</p>"
                       "<p><strong>36</strong> — boʻlishdan oldin; <strong>9</strong> — "
                       "koeffitsient. Simmetrik sistemada qoʻshish deyarli har doim "
                       "eng tez yoʻl.</p>",
    },
    {
        "text": "<p>Two adults and three children pay $31 to enter a park. One adult and "
                "two children pay $18. What is the price of one adult ticket?</p>",
        "choices": ["$5", "$8", "$13", "$18"],
        "correct": "$8",
        "explanation": "<p><strong>$8.</strong> 2a + 3c = 31 va a + 2c = 18. Ikkinchisini "
                       "2 ga koʻpaytiramiz: 2a + 4c = 36, keyin birinchisini ayiramiz: "
                       "c = 5, demak a = 18 − 10 = 8.</p>"
                       "<p><strong>$5</strong> — bola chiptasi. Savol kattalarnikini "
                       "soʻradi.</p>",
    },
    {
        "text": "<p>Two pens and three books cost $31. Two pens and five books cost $45. "
                "What is the price of one book?</p>",
        "choices": ["$5", "$7", "$14", "$21"],
        "correct": "$7",
        "explanation": "<p><strong>$7.</strong> Ruchkalar soni ikkalasida ham bir xil, "
                       "shuning uchun ayiramiz: 2b = 14 → b = 7 (va ruchka $5).</p>"
                       "<p><strong>$14</strong> — boʻlishdan oldingi son; "
                       "<strong>$5</strong> — ruchkaning narxi.</p>",
    },
]


# =====================================================================
# SAT-18 — word problems with systems
# =====================================================================

Q_SAT18 = [
    {
        "text": "<p>Adult tickets cost $8 and child tickets cost $5. A group bought "
                "20 tickets for $136. Which system represents this situation?</p>",
        "choices": ["<i>a</i> + <i>c</i> = 20 and 8<i>a</i> + 5<i>c</i> = 136",
                    "<i>a</i> + <i>c</i> = 136 and 8<i>a</i> + 5<i>c</i> = 20",
                    "8<i>a</i> + 5<i>c</i> = 20 and <i>a</i> + <i>c</i> = 136",
                    "13<i>a</i> + <i>c</i> = 156 and <i>a</i> = <i>c</i>"],
        "correct": "<i>a</i> + <i>c</i> = 20 and 8<i>a</i> + 5<i>c</i> = 136",
        "explanation": "<p><strong>a + c = 20 va 8a + 5c = 136.</strong> Birinchi "
                       "tenglama <b>nechta</b> chipta, ikkinchisi <b>qancha pul</b>.</p>"
                       "<p>Ikkinchi variantda ikki son oʻrin almashgan: 20 — chiptalar "
                       "soni, 136 esa dollar. Birlikni yozib qoʻysangiz adashmaysiz.</p>",
    },
    {
        "text": "<p>Using that system — 20 tickets for $136, adults $8 and children $5 — "
                "how many adult tickets were bought?</p>",
        "choices": ["8", "12", "17", "20"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> c = 20 − a ni qoʻyamiz: "
                       "8a + 100 − 5a = 136 → 3a = 36 → a = 12.</p>"
                       "<p><strong>8</strong> — bolalar chiptasi soni; "
                       "<strong>17</strong> — 136 ÷ 8, yaʼni hamma chiptani "
                       "kattalarniki deb hisoblagan javob.</p>",
    },
    {
        "text": "<p>The sum of two numbers is 54 and their difference is 8. What is the "
                "larger number?</p>",
        "choices": ["23", "27", "31", "46"],
        "correct": "31",
        "explanation": "<p><strong>31.</strong> Qoʻshamiz: 2x = 62 → x = 31 "
                       "(va y = 23).</p>"
                       "<p><strong>23</strong> — kichigi; <strong>27</strong> — 54 ni "
                       "teng ikkiga boʻlgan javob, lekin sonlar teng emas.</p>",
    },
    {
        "text": "<p>Notebooks cost $3 each and pens cost $2 each. A customer bought "
                "15 items for $37. How many notebooks were bought?</p>",
        "choices": ["7", "8", "12", "15"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> n + p = 15 va 3n + 2p = 37 → "
                       "3n + 30 − 2n = 37 → n = 7 (va 8 ta ruchka).</p>"
                       "<p><strong>8</strong> — ruchkalar soni. Tez usul: 15 dona × $2 "
                       "= $30, farq $7, va har bir daftar $1 qimmat — demak 7 ta.</p>",
    },
    {
        "text": "<p>A rectangle has a perimeter of 34 and its length is 5 more than its "
                "width. What is the width?</p>",
        "choices": ["6", "8", "11", "17"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> l = w + 5 va 2(l + w) = 34 → "
                       "2(2w + 5) = 34 → 4w = 24 → w = 6 (uzunligi 11).</p>"
                       "<p><strong>11</strong> — uzunligi; <strong>17</strong> — "
                       "perimetrning yarmi, yaʼni l + w.</p>",
    },
    {
        "text": "<p>A jar holds 30 coins, some worth 5 and some worth 10, with a total "
                "value of 220. How many 5-coins are in the jar?</p>",
        "choices": ["14", "16", "20", "22"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> x + y = 30 va 5x + 10y = 220 → "
                       "5x + 300 − 10x = 220 → −5x = −80 → x = 16 (va 14 ta 10-lik).</p>"
                       "<p><strong>14</strong> — 10-liklar soni. Har doim qaysi harf "
                       "nimani bildirganini boshida yozing.</p>",
    },
    {
        "text": "<p>A cafe sells tea for $2 and coffee for $3. One morning it sold "
                "40 drinks for $104. How many coffees were sold?</p>",
        "choices": ["16", "20", "24", "34"],
        "correct": "24",
        "explanation": "<p><strong>24.</strong> t + c = 40 va 2t + 3c = 104 → "
                       "80 − 2c + 3c = 104 → c = 24 (va 16 ta choy).</p>"
                       "<p><strong>16</strong> — choylar soni; <strong>34</strong> — "
                       "104 − 40 + ... hech qanday maʼnoli amal bermaydi, lekin "
                       "shoshgan oʻquvchi shunday ayirishi mumkin.</p>",
    },
    {
        "text": "<p>A rectangle's length is 3 more than twice its width, and its "
                "perimeter is 36. Which system represents this?</p>",
        "choices": ["<i>l</i> = 2<i>w</i> + 3 and 2(<i>l</i> + <i>w</i>) = 36",
                    "<i>l</i> = 2<i>w</i> + 3 and <i>l</i> + <i>w</i> = 36",
                    "<i>l</i> = 2(<i>w</i> + 3) and 2(<i>l</i> + <i>w</i>) = 36",
                    "<i>w</i> = 2<i>l</i> + 3 and 2(<i>l</i> + <i>w</i>) = 36"],
        "correct": "<i>l</i> = 2<i>w</i> + 3 and 2(<i>l</i> + <i>w</i>) = 36",
        "explanation": "<p><strong>l = 2w + 3 va 2(l + w) = 36.</strong> «Twice its "
                       "width» = 2w, «3 more» = +3; perimetr esa toʻrt tomonning "
                       "yigʻindisi.</p>"
                       "<p><strong>l + w = 36</strong> — perimetrni yarmi bilan "
                       "adashtirgan javob.</p>",
    },
    {
        "text": "<p>Using that system, what is the width of the rectangle?</p>",
        "choices": ["5", "6", "13", "18"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 2(2w + 3 + w) = 36 → 6w + 6 = 36 → "
                       "w = 5 (uzunligi 13).</p>"
                       "<p><strong>13</strong> — uzunligi; <strong>18</strong> — "
                       "perimetrning yarmi.</p>",
    },
    {
        "text": "<p>Two numbers have a sum of 40, and one is four times the other. What "
                "is the smaller number?</p>",
        "choices": ["8", "10", "20", "32"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> x + 4x = 40 → 5x = 40 → x = 8 "
                       "(kattasi 32).</p>"
                       "<p><strong>10</strong> — 40 ni toʻrtga boʻlgan javob, lekin "
                       "nisbat 1 : 4, yaʼni jami <b>besh</b> ulush.</p>",
    },
    {
        "text": "<p>In the system <i>a</i> + <i>c</i> = 20 and 8<i>a</i> + 5<i>c</i> = "
                "136, what does the 20 represent?</p>",
        "choices": ["The total number of tickets bought",
                    "The total amount of money spent",
                    "The price of an adult ticket",
                    "The number of adult tickets"],
        "correct": "The total number of tickets bought",
        "explanation": "<p><strong>Sotib olingan chiptalarning umumiy soni.</strong> "
                       "Birinchi tenglamada narxlar yoʻq — faqat sonlar qoʻshiladi.</p>"
                       "<p>Pul esa ikkinchi tenglamada: u yerda har bir son narxga "
                       "koʻpaytirilgan.</p>",
    },
    {
        "text": "<p>In the same system, what does the 8 represent?</p>",
        "choices": ["The price of one adult ticket",
                    "The number of adult tickets",
                    "The total number of tickets",
                    "The difference between the two prices"],
        "correct": "The price of one adult ticket",
        "explanation": "<p><strong>Bitta kattalar chiptasining narxi.</strong> 8 soni "
                       "<i>a</i> ga koʻpaytirilgan — demak u «har bir chipta uchun» "
                       "degan son (SAT-10 dagi qiyalik gʻoyasi).</p>"
                       "<p>Chiptalar soni — bu <i>a</i> ning oʻzi.</p>",
    },
    {
        "text": "<p>A group bought 20 tickets for $136 (adults $8, children $5). How many "
                "<b>more</b> adult tickets than child tickets did they buy?</p>",
        "choices": ["4", "8", "12", "20"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> a = 12 va c = 8, demak farq 12 − 8 = 4.</p>"
                       "<p><strong>12</strong> va <strong>8</strong> — alohida sonlar. "
                       "<em>How many more … than</em> har doim <b>ayirmani</b> "
                       "soʻraydi.</p>",
    },
    {
        "text": "<p>A shop sells small bags for $4 and large bags for $7. It sold 12 bags "
                "for $66. How many large bags were sold?</p>",
        "choices": ["5", "6", "7", "9"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> s + l = 12 va 4s + 7l = 66 → "
                       "48 − 4l + 7l = 66 → 3l = 18 → l = 6 (va 6 ta kichik).</p>"
                       "<p>Bu safar ikkala son teng chiqdi — shuning uchun tekshiruv "
                       "muhim: 4(6) + 7(6) = 66 ✓</p>",
    },
    {
        "text": "<p>A test has 30 questions. Easy questions are worth 4 points and hard "
                "ones 6 points, and the whole test is worth 148 points. How many hard "
                "questions are there?</p>",
        "choices": ["14", "16", "18", "24"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> e + h = 30 va 4e + 6h = 148 → "
                       "120 − 4h + 6h = 148 → 2h = 28 → h = 14 (va 16 ta oson).</p>"
                       "<p><strong>16</strong> — oson savollar soni. Savolning oxirgi "
                       "soʻzi qaysi birini soʻraganini aytadi.</p>",
    },
    {
        "text": "<p>Using the same test — 30 questions, 148 points, easy 4 and hard 6 — "
                "how many <b>easy</b> questions are there?</p>",
        "choices": ["12", "14", "16", "20"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> h = 14, demak e = 30 − 14 = 16.</p>"
                       "<p><strong>14</strong> — qiyin savollar soni, oldingi "
                       "savolning javobi. SAT bitta vaziyat ustiga ikki savol "
                       "qoʻyganda, javoblar almashib ketishi juda oson.</p>",
    },
    {
        "text": "<p>Three apples and two pears cost $13. Two apples and three pears cost "
                "$12. What is the price of one apple?</p>",
        "choices": ["$2", "$3", "$5", "$6"],
        "correct": "$3",
        "explanation": "<p><strong>$3.</strong> Qoʻshamiz: 5a + 5p = 25 → a + p = 5; "
                       "ayiramiz: a − p = 1. Demak a = 3, p = 2.</p>"
                       "<p><strong>$2</strong> — nokning narxi; <strong>$5</strong> — "
                       "ikkalasining yigʻindisi.</p>",
    },
    {
        "text": "<p>A vending machine holds 25 items: chocolate bars at $2 and packets of "
                "crisps at $1.50. The full machine is worth $44. How many chocolate bars "
                "are there?</p>",
        "choices": ["12", "13", "15", "22"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> c + k = 25 va 2c + 1.5k = 44 → "
                       "2c + 37.5 − 1.5c = 44 → 0.5c = 6.5 → c = 13 (va 12 ta "
                       "chips).</p>"
                       "<p><strong>12</strong> — chipslar soni; <strong>22</strong> — "
                       "44 ÷ 2, yaʼni hammasini shokolad deb hisoblagan javob.</p>",
    },
    {
        "text": "<p>A farmyard holds chickens and cows — 20 animals with 56 legs in "
                "total. How many chickens are there?</p>",
        "choices": ["8", "10", "12", "14"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> c + w = 20 va 2c + 4w = 56 → "
                       "2c + 80 − 4c = 56 → −2c = −24 → c = 12 (va 8 ta sigir).</p>"
                       "<p><strong>8</strong> — sigirlar soni. Tez usul: hammasi tovuq "
                       "boʻlsa 40 ta oyoq boʻlardi; ortiqcha 16 ta oyoq, va har bir "
                       "sigir 2 ta qoʻshadi — demak 8 ta sigir.</p>",
    },
    {
        "text": "<p>A boat trip costs $12 for an adult and $7 for a child. A family of "
                "6 people paid $52. How many children were in the family?</p>",
        "choices": ["2", "3", "4", "5"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> a + c = 6 va 12a + 7c = 52 → "
                       "72 − 12c + 7c = 52 → −5c = −20 → c = 4 (va 2 ta katta).</p>"
                       "<p><strong>2</strong> — kattalar soni. Tekshiruv: "
                       "12(2) + 7(4) = 24 + 28 = 52 ✓</p>",
    },
]


# =====================================================================
# SAT-19 — infinitely many solutions
# =====================================================================

Q_SAT19 = [
    {
        "text": "<p>3<i>x</i> + 5<i>y</i> = 9</p><p>6<i>x</i> + 10<i>y</i> = <i>k</i></p>"
                "<p>If the system has infinitely many solutions, what is <i>k</i>?</p>",
        "choices": ["9", "12", "15", "18"],
        "correct": "18",
        "explanation": "<p><strong>18.</strong> Chap tomon 2 ga koʻpaytirilgan "
                       "(6 ÷ 3 = 2, 10 ÷ 5 = 2), demak oʻng tomon ham: 9 × 2 = 18.</p>"
                       "<p><strong>9</strong> — koʻpaytirmasdan koʻchirilgan javob. "
                       "Uchala qism ham bir xil koʻpaytuvchi bilan oʻzgaradi.</p>",
    },
    {
        "text": "<p>10<i>x</i> + 4<i>y</i> = 22</p><p>5<i>x</i> + 2<i>y</i> = <i>c</i></p>"
                "<p>If the system has infinitely many solutions, what is <i>c</i>?</p>",
        "choices": ["5", "11", "22", "44"],
        "correct": "11",
        "explanation": "<p><strong>11.</strong> Ikkinchi tenglama birinchisining "
                       "<b>yarmi</b>, demak c = 22 ÷ 2 = 11.</p>"
                       "<p><strong>44</strong> — koʻpaytuvchini teskari yoʻnalishda "
                       "qoʻllagan javob. Qaysi tenglama kattaroq ekaniga qarang.</p>",
    },
    {
        "text": "<p>How many solutions does the system <i>y</i> = 2<i>x</i> + 1 and "
                "2<i>y</i> = 4<i>x</i> + 2 have?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "Infinitely many",
        "explanation": "<p><strong>Cheksiz koʻp.</strong> Ikkinchi tenglamani 2 ga "
                       "boʻlsak, aynan birinchisi chiqadi — bu bitta chiziq.</p>"
                       "<p>Grafikda ular ustma-ust tushadi: ikkinchi chiziq "
                       "koʻrinmaydi.</p>",
    },
    {
        "text": "<p><i>kx</i> + 6<i>y</i> = 15</p><p>2<i>x</i> + 4<i>y</i> = 10</p>"
                "<p>If the system has infinitely many solutions, what is <i>k</i>?</p>",
        "choices": ["2", "3", "4", "6"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Koʻpaytuvchi: 6 ÷ 4 = 1.5 va "
                       "15 ÷ 10 = 1.5 ✓. Demak k = 1.5 × 2 = 3.</p>"
                       "<p><strong>2</strong> — ikkinchi tenglamadan koʻchirilgan "
                       "koeffitsient; proporsional boʻlishi kerak, teng emas.</p>",
    },
    {
        "text": "<p>4<i>x</i> + <i>ky</i> = 20</p><p>2<i>x</i> + 3<i>y</i> = 10</p>"
                "<p>If the system has infinitely many solutions, what is <i>k</i>?</p>",
        "choices": ["3", "6", "10", "12"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 4 ÷ 2 = 2 va 20 ÷ 10 = 2, demak "
                       "k = 2 × 3 = 6.</p>"
                       "<p><strong>3</strong> — koʻchirilgan koeffitsient; "
                       "<strong>12</strong> — koʻpaytuvchini 4 deb olgan javob.</p>",
    },
    {
        "text": "<p>Which system has infinitely many solutions?</p>",
        "choices": ["<i>x</i> + <i>y</i> = 4 and 2<i>x</i> + 2<i>y</i> = 9",
                    "<i>x</i> + <i>y</i> = 4 and 3<i>x</i> + 3<i>y</i> = 12",
                    "<i>x</i> + <i>y</i> = 4 and <i>x</i> − <i>y</i> = 4",
                    "<i>x</i> + <i>y</i> = 4 and 2<i>x</i> + 3<i>y</i> = 8"],
        "correct": "<i>x</i> + <i>y</i> = 4 and 3<i>x</i> + 3<i>y</i> = 12",
        "explanation": "<p><strong>x + y = 4 va 3x + 3y = 12.</strong> Ikkinchisini "
                       "3 ga boʻlsak birinchisi chiqadi.</p>"
                       "<p>Birinchi variantda chap tomon ikkilangan, oʻng tomon esa "
                       "8 emas 9 — u <b>yechimsiz</b> sistema.</p>",
    },
    {
        "text": "<p>How many solutions does 2<i>x</i> + 3<i>y</i> = 8 and "
                "4<i>x</i> + 6<i>y</i> = 16 have?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "Infinitely many",
        "explanation": "<p><strong>Cheksiz koʻp.</strong> 4 ÷ 2 = 6 ÷ 3 = 16 ÷ 8 = 2 — "
                       "uchala nisbat ham teng.</p>"
                       "<p>Agar oʻng tomon 16 emas, 9 boʻlganda javob <b>None</b> "
                       "boʻlardi. Farq faqat shu sonda.</p>",
    },
    {
        "text": "<p>5<i>x</i> − 2<i>y</i> = 7</p><p>10<i>x</i> − 4<i>y</i> = <i>k</i></p>"
                "<p>If the system has infinitely many solutions, what is <i>k</i>?</p>",
        "choices": ["7", "10", "14", "28"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> Koʻpaytuvchi 2, demak oʻng tomon ham "
                       "ikkilanadi: 7 × 2 = 14.</p>"
                       "<p><strong>28</strong> — toʻrtga koʻpaytirgan javob; "
                       "koʻpaytuvchini <b>ikkita</b> maʼlum nisbatdan tekshiring.</p>",
    },
    {
        "text": "<p><i>x</i> − 3<i>y</i> = 6</p><p><i>kx</i> − 12<i>y</i> = 24</p>"
                "<p>If the system has infinitely many solutions, what is <i>k</i>?</p>",
        "choices": ["3", "4", "6", "12"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 12 ÷ 3 = 4 va 24 ÷ 6 = 4, demak "
                       "k = 4 × 1 = 4.</p>"
                       "<p><strong>12</strong> — y ning koeffitsienti koʻchirilgan; "
                       "<i>x</i> ning koeffitsienti 1 edi, shuning uchun k = 4.</p>",
    },
    {
        "text": "<p>If a system of two linear equations has infinitely many solutions, "
                "what do the two graphs look like?</p>",
        "choices": ["Two parallel lines", "Two lines crossing at one point",
                    "The same line drawn twice", "Two lines crossing at two points"],
        "correct": "The same line drawn twice",
        "explanation": "<p><strong>Bitta chiziq ikki marta chizilgan.</strong> Ular "
                       "ustma-ust tushadi, shuning uchun har bir nuqta umumiy.</p>"
                       "<p><strong>Parallel</strong> chiziqlar esa <b>yechimsiz</b> "
                       "sistemani beradi (SAT-20).</p>",
    },
    {
        "text": "<p>How many points do the two graphs of such a system have in "
                "common?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "Infinitely many",
        "explanation": "<p><strong>Cheksiz koʻp.</strong> Chiziq ustidagi har bir nuqta "
                       "ikkala tenglamani ham qanoatlantiradi.</p>"
                       "<p>Diqqat: bu «har qanday nuqta» degani emas — chiziqdan "
                       "tashqaridagi nuqta yechim emas.</p>",
    },
    {
        "text": "<p>Which equation is equivalent to 6<i>x</i> + 9<i>y</i> = 24?</p>",
        "choices": ["2<i>x</i> + 3<i>y</i> = 8", "2<i>x</i> + 3<i>y</i> = 24",
                    "3<i>x</i> + 6<i>y</i> = 8", "6<i>x</i> + 9<i>y</i> = 8"],
        "correct": "2<i>x</i> + 3<i>y</i> = 8",
        "explanation": "<p><strong>2x + 3y = 8.</strong> Hamma hadni 3 ga boʻldik — "
                       "oʻng tomonni ham.</p>"
                       "<p><strong>2x + 3y = 24</strong> — oʻng tomon boʻlinmagan; "
                       "bu <b>boshqa</b> chiziq va u bilan sistema yechimsiz "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Two shops advertise the same deal in different words: «3 kilograms "
                "for 24 som» and «6 kilograms for 48 som». Written as equations, what "
                "kind of system is this?</p>",
        "choices": ["A system with no solution",
                    "A system with exactly one solution",
                    "A system with infinitely many solutions",
                    "Not a system at all"],
        "correct": "A system with infinitely many solutions",
        "explanation": "<p><strong>Cheksiz koʻp yechimli sistema.</strong> Ikkinchi "
                       "eʼlon birinchisining aynan ikki barobari — bir xil narx, "
                       "boshqacha yozilgan.</p>"
                       "<p>Har ikkala doʻkonda ham kilogrammi 8 som: bu bitta "
                       "chiziqning ikki xil yozuvi.</p>",
    },
    {
        "text": "<p>For a system to have infinitely many solutions, what must be true of "
                "the coefficients?</p>",
        "choices": ["They must be equal",
                    "They must be proportional, including the constant terms",
                    "Only the x-coefficients must match",
                    "The constant terms must be different"],
        "correct": "They must be proportional, including the constant terms",
        "explanation": "<p><strong>Proporsional — oʻzgarmas hadlar bilan birga.</strong> "
                       "A, B va C uchalasi bir xil koʻpaytuvchi bilan bogʻlangan "
                       "boʻlishi kerak.</p>"
                       "<p><strong>«Teng»</strong> notoʻgʻri: 3x + 3y = 12 va "
                       "x + y = 4 koeffitsientlari teng emas, lekin proporsional.</p>",
    },
    {
        "text": "<p>Is the following true: «If two equations have the same coefficients "
                "for x and y, the system has infinitely many solutions»?</p>",
        "choices": ["Yes, always",
                    "No — the constant terms must match too",
                    "Yes, but only if the constants are different",
                    "No — the coefficients must be different"],
        "correct": "No — the constant terms must match too",
        "explanation": "<p><strong>Yoʻq — oʻzgarmas hadlar ham mos boʻlishi kerak.</strong> "
                       "2x + 3y = 8 va 2x + 3y = 9 bir xil koeffitsientlarga ega, "
                       "lekin yechimi <b>yoʻq</b>.</p>"
                       "<p>Bitta ifoda ikki xil songa teng boʻla olmaydi.</p>",
    },
    {
        "text": "<p>How many solutions does 2<i>x</i> + 3<i>y</i> = 8 and "
                "4<i>x</i> + 6<i>y</i> = 9 have?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "None",
        "explanation": "<p><strong>Bittasi ham yoʻq.</strong> Chap tomon ikkilangan, "
                       "lekin oʻng tomon 16 boʻlishi kerak edi, 9 emas.</p>"
                       "<p>Bu savol oldingilarining <b>juftligi</b>: bitta son "
                       "oʻzgarganda javob «cheksiz koʻp»dan «yoʻq»ga aylanadi.</p>",
    },
    {
        "text": "<p><i>kx</i> + 8<i>y</i> = 12</p><p>3<i>x</i> + 4<i>y</i> = 6</p>"
                "<p>If the system has infinitely many solutions, what is <i>k</i>?</p>",
        "choices": ["2", "3", "6", "8"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 8 ÷ 4 = 2 va 12 ÷ 6 = 2, demak "
                       "k = 2 × 3 = 6.</p>"
                       "<p>Tekshiruv: 6x + 8y = 12 aynan 3x + 4y = 6 ning ikki "
                       "barobari ✓</p>",
    },
    {
        "text": "<p>4<i>x</i> − 6<i>y</i> = 10</p><p>2<i>x</i> − 3<i>y</i> = <i>c</i></p>"
                "<p>If the system has infinitely many solutions, what is <i>c</i>?</p>",
        "choices": ["2", "5", "10", "20"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Ikkinchi tenglama birinchisining yarmi, "
                       "demak c = 10 ÷ 2 = 5.</p>"
                       "<p><strong>20</strong> — koʻpaytuvchini teskari qoʻllagan "
                       "javob; kichikroq tenglama kichikroq oʻng tomon oladi.</p>",
    },
    {
        "text": "<p>A recipe uses 2 cups of flour and 3 eggs. A second recipe uses 6 cups "
                "of flour and 9 eggs. What is true of the two recipes?</p>",
        "choices": ["They are the same recipe, tripled",
                    "The second uses proportionally more flour",
                    "The second uses proportionally more eggs",
                    "They cannot be compared"],
        "correct": "They are the same recipe, tripled",
        "explanation": "<p><strong>Bir xil retsept, uch barobar.</strong> 6 ÷ 2 = 3 va "
                       "9 ÷ 3 = 3 — ikkala nisbat ham teng.</p>"
                       "<p>Tenglamalar tilida bu «cheksiz koʻp yechim» holati: bitta "
                       "munosabat, ikki xil yozuv.</p>",
    },
    {
        "text": "<p>A shop lists «4 notebooks and 2 pens for 60 som». A second sign says "
                "«2 notebooks and 1 pen for 30 som». How many solutions does this system "
                "have?</p>",
        "choices": ["None", "Exactly one", "Infinitely many",
                    "It depends on the price of a pen"],
        "correct": "Infinitely many",
        "explanation": "<p><strong>Cheksiz koʻp.</strong> Ikkinchi eʼlon birinchisining "
                       "aynan yarmi: 4 ÷ 2 = 2 ÷ 1 = 60 ÷ 30 = 2.</p>"
                       "<p>Amaliy maʼnosi: ikki eʼlon <b>bir xil</b> maʼlumot beradi, "
                       "shuning uchun ular alohida narxlarni aniqlab bermaydi.</p>",
    },
]


# =====================================================================
# SAT-20 — no solution
# =====================================================================

Q_SAT20 = [
    {
        "text": "<p><i>y</i> = 4<i>x</i> + 1</p><p><i>y</i> = <i>kx</i> − 6</p>"
                "<p>If the system has no solution, what is <i>k</i>?</p>",
        "choices": ["−6", "1", "4", "6"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Yechim boʻlmasligi uchun chiziqlar "
                       "parallel boʻlishi kerak — qiyaliklar teng.</p>"
                       "<p>b lar (1 va −6) allaqachon har xil, shuning uchun ular "
                       "ustma-ust tushmaydi ✓</p>",
    },
    {
        "text": "<p>How many solutions does <i>x</i> + <i>y</i> = 5 and "
                "2<i>x</i> + 2<i>y</i> = 7 have?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "None",
        "explanation": "<p><strong>Bittasi ham yoʻq.</strong> Chap tomon ikkilangan, "
                       "oʻng tomon esa 10 boʻlishi kerak edi.</p>"
                       "<p>Boshqacha koʻrsak: 2x + 2y = 7 ni 2 ga boʻlsak x + y = 3.5, "
                       "lekin birinchi tenglama x + y = 5 deydi. Bitta ifoda ikki xil "
                       "songa teng boʻlolmaydi.</p>",
    },
    {
        "text": "<p>How many solutions does <i>x</i> + <i>y</i> = 5 and "
                "<i>x</i> − <i>y</i> = 1 have?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "Exactly one",
        "explanation": "<p><strong>Roppa-rosa bittasi.</strong> Qiyaliklar har xil "
                       "(1 va −1... aniqrogʻi y = 5 − x va y = x − 1), demak chiziqlar "
                       "kesishadi: (3, 2).</p>"
                       "<p>Qiyaliklar har xil boʻlishi — bitta yechimning "
                       "kafolati.</p>",
    },
    {
        "text": "<p>5<i>x</i> + <i>ky</i> = 3</p><p>10<i>x</i> + 4<i>y</i> = 9</p>"
                "<p>If the system has no solution, what is <i>k</i>?</p>",
        "choices": ["2", "3", "4", "8"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> 5 ÷ 10 = 1/2, demak k ÷ 4 = 1/2 va "
                       "k = 2.</p>"
                       "<p>Tekshiruv: 3 ÷ 9 = 1/3, bu 1/2 ga teng emas ✓ — demak "
                       "haqiqatan yechim yoʻq, cheksiz koʻp emas.</p>",
    },
    {
        "text": "<p>2<i>x</i> + 3<i>y</i> = 9</p><p>4<i>x</i> + <i>ky</i> = 7</p>"
                "<p>If the system has no solution, what is <i>k</i>?</p>",
        "choices": ["3", "6", "7", "18"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 4 ÷ 2 = 2, demak k = 2 × 3 = 6.</p>"
                       "<p><strong>18</strong> — cheksiz koʻp yechim beradigan oʻng "
                       "tomon (9 × 2), <i>k</i> ning javobi emas.</p>",
    },
    {
        "text": "<p>How many solutions does 3<i>x</i> − <i>y</i> = 5 and "
                "6<i>x</i> − 2<i>y</i> = 10 have?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "Infinitely many",
        "explanation": "<p><strong>Cheksiz koʻp.</strong> 6 ÷ 3 = 2, (−2) ÷ (−1) = 2 va "
                       "10 ÷ 5 = 2 — uchala nisbat ham bir xil.</p>"
                       "<p>Agar oʻng tomon 11 boʻlganda, javob <b>None</b> boʻlardi.</p>",
    },
    {
        "text": "<p>How many solutions does 2<i>x</i> + <i>y</i> = 4 and "
                "4<i>x</i> + 2<i>y</i> = 9 have?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "None",
        "explanation": "<p><strong>Bittasi ham yoʻq.</strong> Chap tomon ikkilangan, "
                       "oʻng tomon 8 boʻlishi kerak edi.</p>"
                       "<p>Chiziqlar parallel: bir xil qiyalik (−2), boshqa "
                       "y-intercept.</p>",
    },
    {
        "text": "<p>How many solutions does <i>y</i> = 3<i>x</i> + 2 and "
                "<i>y</i> = 3<i>x</i> + 5 have?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "None",
        "explanation": "<p><strong>Bittasi ham yoʻq.</strong> Qiyaliklar teng (3), "
                       "b lar har xil (2 va 5) — bu parallel chiziqlarning taʼrifi "
                       "(SAT-11).</p>"
                       "<p>Ular har doim 3 birlik masofada yonma-yon boradi.</p>",
    },
    {
        "text": "<p>How many solutions does <i>y</i> = 3<i>x</i> + 2 and "
                "2<i>y</i> = 6<i>x</i> + 4 have?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "Infinitely many",
        "explanation": "<p><strong>Cheksiz koʻp.</strong> Ikkinchisini 2 ga boʻlsak "
                       "aynan birinchisi chiqadi.</p>"
                       "<p>Oldingi savol bilan solishtiring: u yerda b lar har xil "
                       "edi, bu yerda esa bir xil — javob butunlay oʻzgardi.</p>",
    },
    {
        "text": "<p>How many solutions does <i>y</i> = 2<i>x</i> and <i>y</i> = "
                "−2<i>x</i> have?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "Exactly one",
        "explanation": "<p><strong>Roppa-rosa bittasi.</strong> Qiyaliklar har xil "
                       "(2 va −2), demak chiziqlar kesishadi — boshda, (0, 0) da.</p>"
                       "<p>Ishoraning qarama-qarshi boʻlishi «parallel» degani emas; "
                       "parallellik uchun qiyaliklar <b>teng</b> boʻlishi kerak.</p>",
    },
    {
        "text": "<p>If a system has no solution, what is true of the two graphs?</p>",
        "choices": ["They are parallel and never meet",
                    "They are the same line",
                    "They cross at exactly one point",
                    "They cross at the origin"],
        "correct": "They are parallel and never meet",
        "explanation": "<p><strong>Parallel va hech qachon uchrashmaydi.</strong> Umumiy "
                       "nuqta yoʻqligi — kesishmaslik degani.</p>"
                       "<p><strong>«The same line»</strong> esa aksincha: cheksiz koʻp "
                       "yechim (SAT-19).</p>",
    },
    {
        "text": "<p>Which description matches a system with no solution?</p>",
        "choices": ["Same slope, different y-intercepts",
                    "Same slope, same y-intercept",
                    "Different slopes, same y-intercept",
                    "Different slopes, different y-intercepts"],
        "correct": "Same slope, different y-intercepts",
        "explanation": "<p><strong>Bir xil qiyalik, har xil y-intercept.</strong> "
                       "Bu parallel chiziqlarning taʼrifi.</p>"
                       "<p>Bir xil qiyalik <b>va</b> bir xil b — bu bitta chiziq, "
                       "yaʼni cheksiz koʻp yechim.</p>",
    },
    {
        "text": "<p>Two phone plans cost <i>C</i> = 10<i>g</i> + 30 and <i>C</i> = "
                "10<i>g</i> + 55. Is there an amount of data at which the two plans cost "
                "the same?</p>",
        "choices": ["No — the difference is always $25",
                    "Yes — at 25 gigabytes",
                    "Yes — at 85 gigabytes",
                    "Yes, but only for large amounts of data"],
        "correct": "No — the difference is always $25",
        "explanation": "<p><strong>Yoʻq — farq har doim $25.</strong> Qiyaliklar teng "
                       "(har gigabayt $10), shuning uchun chiziqlar parallel.</p>"
                       "<p>Bu sistemaning <b>yechimi yoʻq</b>: hech qanday <i>g</i> "
                       "ikkala narxni tenglashtirmaydi.</p>",
    },
    {
        "text": "<p>A system of two linear equations is written, and after eliminating "
                "<i>x</i> the result is 0 = 7. What does this mean?</p>",
        "choices": ["The system has no solution",
                    "The system has infinitely many solutions",
                    "x = 7", "x = 0"],
        "correct": "The system has no solution",
        "explanation": "<p><strong>Yechim yoʻq.</strong> 0 = 7 — yolgʻon tenglik, demak "
                       "hech qanday (x, y) juftligi ikkala tenglamani rost qila "
                       "olmaydi.</p>"
                       "<p>Agar natija 0 = 0 boʻlganda (rost tenglik), javob "
                       "<b>cheksiz koʻp</b> boʻlardi — SAT-2 dagi qoida oʻsha.</p>",
    },
    {
        "text": "<p><i>y</i> = 5<i>x</i> + 3</p><p><i>y</i> = 5<i>x</i> + 3</p>"
                "<p>How many solutions does this system have?</p>",
        "choices": ["None", "Exactly one", "Exactly two", "Infinitely many"],
        "correct": "Infinitely many",
        "explanation": "<p><strong>Cheksiz koʻp.</strong> Ikki tenglama aynan bir xil — "
                       "bu bitta chiziq.</p>"
                       "<p>Bir xil qiyalikni koʻrib «yechim yoʻq» deyish tuzoq: "
                       "b lar ham teng, shuning uchun chiziqlar ustma-ust tushadi.</p>",
    },
    {
        "text": "<p>3<i>x</i> + <i>ky</i> = 4</p><p>6<i>x</i> + 8<i>y</i> = 9</p>"
                "<p>If the system has no solution, what is <i>k</i>?</p>",
        "choices": ["2", "4", "8", "12"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 3 ÷ 6 = 1/2, demak k ÷ 8 = 1/2 va "
                       "k = 4.</p>"
                       "<p>Tekshiruv: 4 ÷ 9 ≠ 1/2 ✓ — oʻng tomon mos emas, shuning "
                       "uchun javob «yechim yoʻq», «cheksiz koʻp» emas.</p>",
    },
    {
        "text": "<p>6<i>x</i> + <i>ky</i> = 5</p><p>9<i>x</i> + 6<i>y</i> = 8</p>"
                "<p>If the system has no solution, what is <i>k</i>?</p>",
        "choices": ["3", "4", "6", "9"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 6 ÷ 9 = 2/3, demak k ÷ 6 = 2/3 va "
                       "k = 4.</p>"
                       "<p>Tekshiruv: 5 ÷ 8 ≠ 2/3 ✓. Kasrli nisbatlardan "
                       "qoʻrqmang — usul aynan oʻsha.</p>",
    },
    {
        "text": "<p>For which situation does a linear system have <b>exactly one</b> "
                "solution?</p>",
        "choices": ["The slopes are different",
                    "The slopes are equal and the intercepts differ",
                    "The slopes and intercepts are both equal",
                    "The constant terms are equal"],
        "correct": "The slopes are different",
        "explanation": "<p><strong>Qiyaliklar har xil boʻlganda.</strong> Turli "
                       "qiyalikdagi ikki chiziq albatta kesishadi — va faqat bir "
                       "marta.</p>"
                       "<p>Qolgan ikkitasi parallel (yechim yoʻq) va ustma-ust "
                       "(cheksiz koʻp) holatlari.</p>",
    },
    {
        "text": "<p>A hall is being paid for in two ways. Plan A costs 40 som plus 6 som "
                "per guest; plan B costs 75 som plus 6 som per guest. For how many guests "
                "do the two plans cost the same?</p>",
        "choices": ["For no number of guests", "For 35 guests",
                    "For 115 guests", "For every number of guests"],
        "correct": "For no number of guests",
        "explanation": "<p><strong>Hech qanday mehmonlar sonida.</strong> Har bir "
                       "mehmon uchun narx bir xil (6 som), shuning uchun 35 somlik "
                       "farq hech qachon yopilmaydi.</p>"
                       "<p>Bu — «yechim yoʻq» holatining kundalik koʻrinishi: "
                       "parallel chiziqlar.</p>",
    },
    {
        "text": "<p>Two taxi firms charge 5,000 som plus 1,200 som per kilometre, and "
                "10,000 som plus 1,200 som per kilometre. Which statement is true?</p>",
        "choices": ["The second firm is always 5,000 som more expensive",
                    "The two firms cost the same after 5 kilometres",
                    "The first firm becomes more expensive on long trips",
                    "The costs cannot be compared without the distance"],
        "correct": "The second firm is always 5,000 som more expensive",
        "explanation": "<p><strong>Ikkinchi firma har doim 5,000 som qimmat.</strong> "
                       "Kilometr narxi bir xil, demak farq masofaga bogʻliq emas.</p>"
                       "<p>Grafikda bu ikki parallel chiziq: ular hech qachon "
                       "kesishmaydi va sistemaning yechimi yoʻq.</p>",
    },
]


PRACTICES = [
    {
        "title":       "SAT-16 Practice: Systems of Linear Equations: Solving by Substitution",
        "description": "20 ta SAT uslubidagi savol — oʻrniga qoʻyish, qavs qoidasi, "
                       "yechim nuqta ekani va «x emas, x + y» tuzogʻi.",
        "tutorial":    "SAT-16:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT16,
    },
    {
        "title":       "SAT-17 Practice: Systems of Linear Equations: Solving by Elimination",
        "description": "20 ta SAT uslubidagi savol — qoʻshish va ayirish, oldindan "
                       "koʻpaytirish va x + y ni bitta amalda topish.",
        "tutorial":    "SAT-17:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT17,
    },
    {
        "title":       "SAT-18 Practice: Word Problems Involving Systems of Linear Equations",
        "description": "20 ta SAT uslubidagi savol — soni va qiymati, yigʻindi va "
                       "ayirma, sistemani matndan tuzish va toʻgʻri javobni tanlash.",
        "tutorial":    "SAT-18:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT18,
    },
    {
        "title":       "SAT-19 Practice: Systems with Infinite Solutions (Identical Lines)",
        "description": "20 ta SAT uslubidagi savol — nisbat testi, nomaʼlum "
                       "koeffitsient va «proporsional, teng emas» qoidasi.",
        "tutorial":    "SAT-19:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT19,
    },
    {
        "title":       "SAT-20 Practice: Systems with No Solution (Parallel Lines)",
        "description": "20 ta SAT uslubidagi savol — parallel chiziqlar, uchala "
                       "holatni ajratish va 0 = 7 nimani anglatishi.",
        "tutorial":    "SAT-20:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT20,
    },
]
