# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-91 … SAT-95 (Blok E, uchinchi qismi).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.
⚠️ Javob har doim "correct" da va choices ning BIRINCHISIDA turadi.
⚠️ Ismlar — foydalanuvchining oʻz oʻquvchilari (memory: pupil-names).

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_91_95.py --master=prime \\
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
# SAT-91 — translating English into math
# =====================================================================

Q_SAT91 = [
    {
        "text": "<p>Three less than twice a number is 11. What is the number?</p>",
        "choices": ["7", "−4", "4", "28"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 2n − 3 = 11.</p>"
                       "<p><strong>−4</strong> — «three less than» ni 3 − 2n deb "
                       "yozgan: teskari ibora tuzogʻi.</p>",
    },
    {
        "text": "<p>Which expression means \"5 less than <i>x</i>\"?</p>",
        "choices": ["<i>x</i> − 5", "5 − <i>x</i>", "5<i>x</i>", "<i>x</i> + 5"],
        "correct": "<i>x</i> − 5",
        "explanation": "<p><strong>x − 5.</strong> «than» dan keyingi narsa "
                       "oldinga chiqadi.</p>",
    },
    {
        "text": "<p>Which expression means \"<i>x</i> subtracted from 5\"?</p>",
        "choices": ["5 − <i>x</i>", "<i>x</i> − 5", "5<i>x</i>", "<i>x</i> ÷ 5"],
        "correct": "5 − <i>x</i>",
        "explanation": "<p><strong>5 − x.</strong> «Subtracted from» dan keyingi "
                       "son boshida turadi — bu oldingi savolning aksi.</p>",
    },
    {
        "text": "<p>12 is 25 percent of what number?</p>",
        "choices": ["48", "3", "37", "300"],
        "correct": "48",
        "explanation": "<p><strong>48.</strong> Nomaʼlum «of» dan keyin, demak "
                       "butun soʻralgan: 12 × 4.</p>"
                       "<p><strong>3</strong> — savol «25% of 12» deb "
                       "oʻqilgan.</p>",
    },
    {
        "text": "<p>What is 25 percent of 80?</p>",
        "choices": ["20", "320", "55", "105"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> Toʻrtga boʻling.</p>",
    },
    {
        "text": "<p>9 is what percent of 36?</p>",
        "choices": ["25", "400", "27", "45"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> 9 ÷ 36 = 0.25.</p>"
                       "<p><strong>400</strong> — kasr agʻdarilgan.</p>",
    },
    {
        "text": "<p>The sum of a number and 4 is 19. What is the number?</p>",
        "choices": ["15", "23", "76", "4.75"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> n + 4 = 19.</p>",
    },
    {
        "text": "<p>Four more than three times a number is 25. What is the "
                "number?</p>",
        "choices": ["7", "9.67", "87", "21"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 3n + 4 = 25 → 3n = 21.</p>"
                       "<p><strong>21</strong> — oxirgi boʻlish "
                       "bajarilmagan.</p>",
    },
    {
        "text": "<p>Twice a number, decreased by 6, is 10. What is the number?</p>",
        "choices": ["8", "2", "32", "5"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> 2n − 6 = 10 → 2n = 16.</p>",
    },
    {
        "text": "<p>What is 40 percent of 65?</p>",
        "choices": ["26", "162.5", "39", "104"],
        "correct": "26",
        "explanation": "<p><strong>26.</strong> 65 ning oʻndan biri 6.5, "
                       "toʻrt barobari 26.</p>",
    },
    {
        "text": "<p>Which English word most often means the equals sign?</p>",
        "choices": ["is", "of", "per", "and"],
        "correct": "is",
        "explanation": "<p><strong>is.</strong> «is», «are», «equals», «the "
                       "result is» — hammasi tenglik.</p>",
    },
    {
        "text": "<p>Which symbol matches \"at most 40\"?</p>",
        "choices": ["≤ 40", "≥ 40", "&lt; 40", "= 40"],
        "correct": "≤ 40",
        "explanation": "<p><strong>≤ 40.</strong> 40 ning oʻzi ham mumkin.</p>",
    },
    {
        "text": "<p>Which symbol matches \"at least 8\"?</p>",
        "choices": ["≥ 8", "≤ 8", "&gt; 8", "= 8"],
        "correct": "≥ 8",
        "explanation": "<p><strong>≥ 8.</strong> 8 ning oʻzi ham mumkin.</p>",
    },
    {
        "text": "<p>What is the quotient of 20 and 4?</p>",
        "choices": ["5", "80", "24", "16"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> «Quotient» — boʻlinma.</p>"
                       "<p><strong>80</strong> — «product» ning javobi.</p>",
    },
    {
        "text": "<p>The product of 7 and a number is 42. What is the number?</p>",
        "choices": ["6", "35", "49", "294"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> «Product» — koʻpaytma.</p>",
    },
    {
        "text": "<p>Three consecutive integers begin with <i>n</i>. Which expression "
                "gives their sum?</p>",
        "choices": ["3<i>n</i> + 3", "3<i>n</i>", "<i>n</i> + 3", "3<i>n</i> + 6"],
        "correct": "3<i>n</i> + 3",
        "explanation": "<p><strong>3n + 3.</strong> n + (n+1) + (n+2).</p>"
                       "<p><strong>3n</strong> — qoʻshimchalar "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>Seven less than a number is 12. What is the number?</p>",
        "choices": ["19", "5", "−5", "84"],
        "correct": "19",
        "explanation": "<p><strong>19.</strong> n − 7 = 12.</p>"
                       "<p><strong>−5</strong> — 7 − n = 12 deb yozilgan.</p>",
    },
    {
        "text": "<p>Half of a number, increased by 3, is 11. What is the number?</p>",
        "choices": ["16", "8", "28", "22"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> n ÷ 2 + 3 = 11 → n ÷ 2 = 8.</p>"
                       "<p><strong>8</strong> — yarmi topilgan, sonning oʻzi "
                       "emas.</p>",
    },
    {
        "text": "<p>The difference of 15 and a number is 4. What is the number?</p>",
        "choices": ["11", "19", "60", "3.75"],
        "correct": "11",
        "explanation": "<p><strong>11.</strong> 15 − n = 4 — bu yerda tartib "
                       "gapda berilgan.</p>",
    },
    {
        "text": "<p>A number decreased by 8 equals twice the number. What is the "
                "number?</p>",
        "choices": ["−8", "8", "4", "16"],
        "correct": "−8",
        "explanation": "<p><strong>−8.</strong> n − 8 = 2n → −8 = n.</p>"
                       "<p>Tekshiruv: −8 − 8 = −16, va 2 × (−8) = −16 ✓ "
                       "Javob manfiy boʻlishi mumkin.</p>",
    },
]


# =====================================================================
# SAT-92 — structure
# =====================================================================

Q_SAT92 = [
    {
        "text": "<p>If <i>a</i> + <i>b</i> = 9, what is the value of "
                "4<i>a</i> + 4<i>b</i>?</p>",
        "choices": ["36", "13", "9", "It cannot be determined"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> 4(a + b) = 4 × 9.</p>"
                       "<p><strong>It cannot be determined</strong> — a va b "
                       "topilmagani uchun tanlanadigan eng koʻp tuzoq.</p>",
    },
    {
        "text": "<p>If <i>x</i> + <i>y</i> = 5, what is 2<i>x</i> + 2<i>y</i>?</p>",
        "choices": ["10", "7", "5", "25"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 2(x + y).</p>",
    },
    {
        "text": "<p>If 3(<i>m</i> + <i>n</i>) = 21, what is <i>m</i> + <i>n</i>?</p>",
        "choices": ["7", "18", "63", "24"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Uchga boʻling.</p>"
                       "<p><strong>18</strong> — 21 − 3 hisoblangan.</p>",
    },
    {
        "text": "<p>If 5(<i>p</i> + <i>q</i>) = 40, what is <i>p</i> + <i>q</i>?</p>",
        "choices": ["8", "35", "200", "45"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Beshga boʻling.</p>",
    },
    {
        "text": "<p>If <i>x</i>² + <i>y</i>² = 20 and <i>xy</i> = 8, what is "
                "(<i>x</i> + <i>y</i>)²?</p>",
        "choices": ["36", "28", "160", "12"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> 20 + 2(8).</p>"
                       "<p><strong>28</strong> — oʻrtadagi had "
                       "ikkilanmagan.</p>",
    },
    {
        "text": "<p>If <i>x</i>² + <i>y</i>² = 13 and <i>xy</i> = 6, what is "
                "(<i>x</i> + <i>y</i>)²?</p>",
        "choices": ["25", "19", "78", "7"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> 13 + 12.</p>",
    },
    {
        "text": "<p>If <i>a</i> − <i>b</i> = 4 and <i>a</i> + <i>b</i> = 10, what is "
                "<i>a</i>² − <i>b</i>²?</p>",
        "choices": ["40", "14", "6", "100"],
        "correct": "40",
        "explanation": "<p><strong>40.</strong> a² − b² = (a − b)(a + b).</p>"
                       "<p><strong>14</strong> — ikkalasi qoʻshilgan.</p>",
    },
    {
        "text": "<p>If <i>a</i> − <i>b</i> = 3 and <i>a</i> + <i>b</i> = 7, what is "
                "<i>a</i>² − <i>b</i>²?</p>",
        "choices": ["21", "10", "4", "49"],
        "correct": "21",
        "explanation": "<p><strong>21.</strong> 3 × 7. a va b ning oʻzi "
                       "(5 va 2) kerak boʻlmadi.</p>",
    },
    {
        "text": "<p>If 2(<i>m</i> + 3) = 14, what is <i>m</i> + 3?</p>",
        "choices": ["7", "4", "11", "28"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> m ni topish shart emas.</p>"
                       "<p><strong>4</strong> — bu m ning oʻzi; savol "
                       "m + 3 ni soʻragan.</p>",
    },
    {
        "text": "<p>If 2<sup><i>x</i></sup> = 5, what is 2<sup><i>x</i>+1</sup>?</p>",
        "choices": ["10", "6", "25", "7"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 2<sup>x+1</sup> = "
                       "2<sup>x</sup> × 2.</p>"
                       "<p><strong>6</strong> — darajaga 1 qoʻshib, natijaga "
                       "1 qoʻshgan.</p>",
    },
    {
        "text": "<p>If 3<sup><i>x</i></sup> = 4, what is 3<sup>2<i>x</i></sup>?</p>",
        "choices": ["16", "8", "12", "64"],
        "correct": "16",
        "explanation": "<p><strong>16.</strong> 3<sup>2x</sup> = "
                       "(3<sup>x</sup>)².</p>"
                       "<p><strong>8</strong> — 4 ikkilangan, kvadratga "
                       "koʻtarilmagan.</p>",
    },
    {
        "text": "<p>If <i>a</i> ÷ <i>b</i> = 3, what is <i>b</i> ÷ <i>a</i>?</p>",
        "choices": ["1/3", "3", "−3", "9"],
        "correct": "1/3",
        "explanation": "<p><strong>1/3.</strong> Nisbat agʻdariladi; a va b "
                       "ning oʻzi kerak emas.</p>",
    },
    {
        "text": "<p>Which expression equals (<i>x</i> + <i>y</i>)²?</p>",
        "choices": ["<i>x</i>² + 2<i>xy</i> + <i>y</i>²",
                    "<i>x</i>² + <i>y</i>²",
                    "<i>x</i>² + <i>xy</i> + <i>y</i>²",
                    "<i>x</i>² − 2<i>xy</i> + <i>y</i>²"],
        "correct": "<i>x</i>² + 2<i>xy</i> + <i>y</i>²",
        "explanation": "<p><strong>x² + 2xy + y².</strong> Oʻrtadagi had "
                       "ikkilanadi.</p>",
    },
    {
        "text": "<p>If <i>x</i> + <i>y</i> = 12, what is (<i>x</i> + <i>y</i>) ÷ 3?</p>",
        "choices": ["4", "36", "9", "15"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Boʻlak bitta son sifatida "
                       "boʻlinadi.</p>",
    },
    {
        "text": "<p>When is the choice \"It cannot be determined\" most often a "
                "trap?</p>",
        "choices": ["When the question asks for a combination, not the variables",
                    "When the question has a figure",
                    "When the numbers are large",
                    "When there are two equations"],
        "correct": "When the question asks for a combination, not the variables",
        "explanation": "<p><strong>Birikma soʻralganda.</strong> Nomaʼlumlarni "
                       "topib boʻlmasa ham, boʻlak aniq boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>If <i>x</i> − <i>y</i> = 5 and <i>x</i> + <i>y</i> = 6, what is "
                "<i>x</i>² − <i>y</i>²?</p>",
        "choices": ["30", "11", "1", "36"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> 5 × 6.</p>",
    },
    {
        "text": "<p>If 4(<i>a</i> + <i>b</i>) = 20, what is <i>a</i> + <i>b</i>?</p>",
        "choices": ["5", "16", "80", "24"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Toʻrtga boʻling.</p>",
    },
    {
        "text": "<p>If 2<sup><i>x</i></sup> = 7, what is 2<sup><i>x</i>+2</sup>?</p>",
        "choices": ["28", "9", "49", "14"],
        "correct": "28",
        "explanation": "<p><strong>28.</strong> 7 × 2 × 2.</p>"
                       "<p><strong>14</strong> — faqat bir marta "
                       "ikkilangan.</p>",
    },
    {
        "text": "<p>If <i>x</i> + <i>y</i> = 10 and <i>xy</i> = 21, what is "
                "<i>x</i>² + <i>y</i>²?</p>",
        "choices": ["58", "100", "142", "79"],
        "correct": "58",
        "explanation": "<p><strong>58.</strong> (x + y)² = 100, va undan "
                       "2xy = 42 ni ayiring.</p>"
                       "<p><strong>79</strong> — faqat bitta xy "
                       "ayirilgan.</p>",
    },
    {
        "text": "<p>A rectangle has perimeter 30, so 2(<i>l</i> + <i>w</i>) = 30. "
                "What is <i>l</i> + <i>w</i>?</p>",
        "choices": ["15", "28", "60", "7.5"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> Uzunlik va enni alohida topish "
                       "shart emas — ular topilmaydi ham.</p>",
    },
]


# =====================================================================
# SAT-93 — extreme values
# =====================================================================

Q_SAT93 = [
    {
        "text": "<p>If <i>x</i> &gt; <i>y</i>, which of the following must be "
                "true?</p>",
        "choices": ["<i>x</i> − <i>y</i> &gt; 0", "<i>x</i>² &gt; <i>y</i>²",
                    "<i>x</i> ÷ <i>y</i> &gt; 1", "<i>xy</i> &gt; 0"],
        "correct": "<i>x</i> − <i>y</i> &gt; 0",
        "explanation": "<p><strong>x − y &gt; 0.</strong> Bu tengsizlikning "
                       "taʼrifi.</p>"
                       "<p><strong>x² &gt; y²</strong> — x = 1, y = −2 da "
                       "yiqiladi: 1 &lt; 4.</p>",
    },
    {
        "text": "<p>If <i>n</i> is an integer, which must be even?</p>",
        "choices": ["2<i>n</i>", "<i>n</i> + 2", "<i>n</i>²", "3<i>n</i>"],
        "correct": "2<i>n</i>",
        "explanation": "<p><strong>2n.</strong> n = 1 ni qoʻying: qolgan "
                       "uchtasi ham toq chiqadi.</p>",
    },
    {
        "text": "<p>Is <i>x</i>² ≥ <i>x</i> true for every number?</p>",
        "choices": ["No, it fails for a fraction such as one half",
                    "Yes, squaring always increases a number",
                    "No, it fails only for negative numbers",
                    "Yes, for every real number"],
        "correct": "No, it fails for a fraction such as one half",
        "explanation": "<p><strong>Yoʻq.</strong> (1/2)² = 1/4, va u 1/2 dan "
                       "kichik.</p>",
    },
    {
        "text": "<p>Is <i>x</i>² &gt; 0 true for every number?</p>",
        "choices": ["No, it fails at zero", "Yes, squares are always positive",
                    "No, it fails for negatives", "Yes, except for fractions"],
        "correct": "No, it fails at zero",
        "explanation": "<p><strong>Nolda yiqiladi.</strong> 0 &gt; 0 "
                       "notoʻgʻri.</p>",
    },
    {
        "text": "<p>Which value breaks the claim \"1 ÷ <i>x</i> is less than "
                "<i>x</i>\"?</p>",
        "choices": ["1/2", "2", "5", "10"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> 1 ÷ (1/2) = 2, va 2 &gt; 1/2.</p>",
    },
    {
        "text": "<p>If <i>a</i> &lt; <i>b</i>, must <i>a</i> − <i>b</i> be "
                "negative?</p>",
        "choices": ["Yes, always", "No, not if both are negative",
                    "No, not if <i>a</i> is zero", "Only for integers"],
        "correct": "Yes, always",
        "explanation": "<p><strong>Ha.</strong> a &lt; b degani aynan a − b "
                       "manfiy degani.</p>",
    },
    {
        "text": "<p>The phrase \"must be true\" tells you to look for what?</p>",
        "choices": ["A counterexample that breaks a choice",
                    "One example that works",
                    "The largest possible value",
                    "A figure drawn to scale"],
        "correct": "A counterexample that breaks a choice",
        "explanation": "<p><strong>Qarshi misol.</strong> Bitta buzuvchi son "
                       "variantni oʻldiradi.</p>",
    },
    {
        "text": "<p>The phrase \"could be true\" needs what?</p>",
        "choices": ["One example that works", "A counterexample",
                    "Every value to work", "A negative value"],
        "correct": "One example that works",
        "explanation": "<p><strong>Bitta mos misol.</strong> Yoʻnalish "
                       "teskari.</p>",
    },
    {
        "text": "<p>If <i>n</i> is an integer, must 3<i>n</i> be odd?</p>",
        "choices": ["No, <i>n</i> = 2 gives 6", "Yes, always",
                    "Yes, unless <i>n</i> is zero", "Only for negative <i>n</i>"],
        "correct": "No, <i>n</i> = 2 gives 6",
        "explanation": "<p><strong>Yoʻq.</strong> Bitta juft n yetarli.</p>",
    },
    {
        "text": "<p>In a \"must be true\" question, which value should you almost "
                "always try?</p>",
        "choices": ["Zero", "One hundred", "Seven", "Twelve"],
        "correct": "Zero",
        "explanation": "<p><strong>Nol.</strong> U koʻpaytmani nolga "
                       "aylantiradi va boʻlishni buzadi.</p>",
    },
    {
        "text": "<p>If <i>x</i> &gt; 0, must 1 ÷ <i>x</i> be less than 1?</p>",
        "choices": ["No, <i>x</i> = 1/2 gives 2", "Yes, always",
                    "Yes, for integers only", "No, only when <i>x</i> is negative"],
        "correct": "No, <i>x</i> = 1/2 gives 2",
        "explanation": "<p><strong>Yoʻq.</strong> Birdan kichik kasrning "
                       "teskarisi birdan katta.</p>",
    },
    {
        "text": "<p>If <i>x</i> &gt; <i>y</i>, must <i>xy</i> be positive?</p>",
        "choices": ["No, one of them may be negative", "Yes, always",
                    "Yes, if both are integers", "Only if <i>y</i> is zero"],
        "correct": "No, one of them may be negative",
        "explanation": "<p><strong>Yoʻq.</strong> x = 1, y = −2 da xy = −2.</p>",
    },
    {
        "text": "<p>If <i>n</i> is an integer, which must be odd?</p>",
        "choices": ["2<i>n</i> + 1", "<i>n</i> + 1", "<i>n</i>²", "2<i>n</i>"],
        "correct": "2<i>n</i> + 1",
        "explanation": "<p><strong>2n + 1.</strong> Juft songa bir qoʻshilsa, "
                       "har doim toq.</p>",
    },
    {
        "text": "<p>A question says \"<i>n</i> is a positive integer.\" May you test "
                "<i>n</i> = −1?</p>",
        "choices": ["No, the condition forbids it", "Yes, extremes always help",
                    "Yes, if no other value works", "Only for \"could be true\""],
        "correct": "No, the condition forbids it",
        "explanation": "<p><strong>Yoʻq.</strong> Chekka qiymatlarni sinashdan "
                       "oldin savolning chegarasini oʻqing.</p>",
    },
    {
        "text": "<p>If <i>x</i> is a fraction between 0 and 1, then <i>x</i>² is</p>",
        "choices": ["smaller than <i>x</i>", "larger than <i>x</i>",
                    "equal to <i>x</i>", "negative"],
        "correct": "smaller than <i>x</i>",
        "explanation": "<p><strong>Kichikroq.</strong> Bu darsdagi tuzoqlarning "
                       "yarmi shu faktdan chiqadi.</p>",
    },
    {
        "text": "<p>Which value breaks the claim \"<i>x</i>³ is greater than "
                "<i>x</i>\"?</p>",
        "choices": ["1/2", "2", "3", "10"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> Kubi 1/8, va u kichikroq. "
                       "Nol ham buzadi.</p>",
    },
    {
        "text": "<p>If <i>x</i> &gt; <i>y</i>, must <i>x</i> ÷ <i>y</i> be greater "
                "than 1?</p>",
        "choices": ["No, <i>x</i> = 1 and <i>y</i> = −2 gives −0.5",
                    "Yes, always", "Yes, for positive numbers only",
                    "Only when <i>y</i> is 1"],
        "correct": "No, <i>x</i> = 1 and <i>y</i> = −2 gives −0.5",
        "explanation": "<p><strong>Yoʻq.</strong> Manfiy maxraj nisbatni "
                       "manfiy qiladi.</p>",
    },
    {
        "text": "<p>For every integer <i>n</i>, which must be true?</p>",
        "choices": ["<i>n</i>² ≥ 0", "<i>n</i>² &gt; 0", "<i>n</i>² &gt; <i>n</i>",
                    "<i>n</i>² is even"],
        "correct": "<i>n</i>² ≥ 0",
        "explanation": "<p><strong>n² ≥ 0.</strong> Nolda tenglik boʻladi, "
                       "shuning uchun ikkinchi variant yiqiladi.</p>",
    },
    {
        "text": "<p>If <i>a</i> and <i>b</i> are both negative, their product is</p>",
        "choices": ["positive", "negative", "zero", "impossible to determine"],
        "correct": "positive",
        "explanation": "<p><strong>Musbat.</strong> Ikki manfiy koʻpaytmasi "
                       "musbat.</p>",
    },
    {
        "text": "<p>A student tests only 2, 3 and 5 and concludes that a statement "
                "is always true. What is wrong with that?</p>",
        "choices": ["Positive integers alone cannot test the claim",
                    "Three values are too few, but ten would be enough",
                    "The values should have been larger",
                    "Nothing — three examples prove a statement"],
        "correct": "Positive integers alone cannot test the claim",
        "explanation": "<p><strong>Musbat butun sonlar yetarli emas.</strong> "
                       "Tuzoqlar aynan 0, 1, manfiy va kasrda yashiringan.</p>",
    },
]


# =====================================================================
# SAT-94 — direct translation of word problems
# =====================================================================

Q_SAT94 = [
    {
        "text": "<p>A gym charges a joining fee of $40 plus $15 for each month. After "
                "how many months has a member paid a total of $175?</p>",
        "choices": ["9", "12", "11", "135"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> 40 + 15m = 175.</p>"
                       "<p><strong>12</strong> — kirish toʻlovi "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>A club charges $25 to join and $8 for each visit. How many visits "
                "cost a total of $105?</p>",
        "choices": ["10", "13", "12", "80"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> (105 − 25) ÷ 8.</p>",
    },
    {
        "text": "<p>Afsona has 3 more than twice as many books as Jasur. Together "
                "they have 27 books. How many does Jasur have?</p>",
        "choices": ["8", "19", "12", "9"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> j + (2j + 3) = 27.</p>"
                       "<p><strong>19</strong> — bu Afsonaniki.</p>",
    },
    {
        "text": "<p>Using the same information, how many books does Afsona have?</p>",
        "choices": ["19", "8", "16", "24"],
        "correct": "19",
        "explanation": "<p><strong>19.</strong> 2(8) + 3. Endi savol boshqa "
                       "odamni soʻrayapti.</p>",
    },
    {
        "text": "<p>Sherbek has 5 more than three times as many pens as Iroda. "
                "Together they have 29. How many does Iroda have?</p>",
        "choices": ["6", "23", "8", "7"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> i + (3i + 5) = 29 → 4i = 24.</p>",
    },
    {
        "text": "<p>Using the same information, how many pens does Sherbek have?</p>",
        "choices": ["23", "6", "18", "24"],
        "correct": "23",
        "explanation": "<p><strong>23.</strong> 3(6) + 5.</p>",
    },
    {
        "text": "<p>\"Davron has twice as many marbles as Charos\" means which "
                "equation?</p>",
        "choices": ["Davron = 2 × Charos", "Charos = 2 × Davron",
                    "Davron + Charos = 2", "Davron = Charos + 2"],
        "correct": "Davron = 2 × Charos",
        "explanation": "<p><strong>Davron = 2 × Charos.</strong> Gapda oldin "
                       "turgan ism kattaroq tomonda.</p>",
    },
    {
        "text": "<p>What is the first step of the direct translation method?</p>",
        "choices": ["Name the unknown in a short sentence",
                    "Write the equation", "Check the answer choices",
                    "Draw a diagram"],
        "correct": "Name the unknown in a short sentence",
        "explanation": "<p><strong>Nomaʼlumni soʻz bilan nomlash.</strong> "
                       "«n = 8» emas, «Jasurda 8 ta kitob».</p>",
    },
    {
        "text": "<p>Why write the unit beside every number?</p>",
        "choices": ["A unit error becomes visible in the answer",
                    "It is required by the test",
                    "It makes the arithmetic faster",
                    "It replaces the equation"],
        "correct": "A unit error becomes visible in the answer",
        "explanation": "<p><strong>Xato koʻzga tashlanadi.</strong> "
                       "«km/daqiqa» chiqsa, savol km/soat soʻragani darrov "
                       "seziladi.</p>",
    },
    {
        "text": "<p>A phone plan costs $20 a month plus 10 cents a minute. A bill is "
                "$32. How many minutes were used?</p>",
        "choices": ["120", "320", "12", "52"],
        "correct": "120",
        "explanation": "<p><strong>120.</strong> Qoʻshimcha 12 dollar, va har "
                       "daqiqa 0.10 dollar: 12 ÷ 0.10.</p>",
    },
    {
        "text": "<p>A taxi charges $3 plus $2 for each kilometre. A trip costs $19. "
                "How many kilometres was it?</p>",
        "choices": ["8", "9.5", "11", "6"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> (19 − 3) ÷ 2.</p>"
                       "<p><strong>9.5</strong> — boshlangʻich 3 dollar "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>Two numbers add to 30 and one is 4 more than the other. What is "
                "the smaller number?</p>",
        "choices": ["13", "17", "15", "26"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> n + (n + 4) = 30 → 2n = 26.</p>",
    },
    {
        "text": "<p>Using the same information, what is the larger number?</p>",
        "choices": ["17", "13", "15", "34"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> 13 + 4. Tekshiruv: "
                       "13 + 17 = 30 ✓</p>",
    },
    {
        "text": "<p>The gym charges $40 to join and $15 a month. What is the total "
                "cost after 6 months?</p>",
        "choices": ["$130", "$90", "$55", "$240"],
        "correct": "$130",
        "explanation": "<p><strong>$130.</strong> 40 + 6(15).</p>"
                       "<p><strong>$90</strong> — kirish toʻlovi "
                       "qoʻshilmagan.</p>",
    },
    {
        "text": "<p>Three consecutive integers add to 42. What is the smallest?</p>",
        "choices": ["13", "14", "15", "12"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> 13 + 14 + 15 = 42.</p>"
                       "<p><strong>14</strong> — bu oʻrtadagi son.</p>",
    },
    {
        "text": "<p>Davron has 5 fewer than twice as many books as Marjona. Together "
                "they have 25. How many does Marjona have?</p>",
        "choices": ["10", "15", "12", "8"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> m + (2m − 5) = 25 → 3m = 30.</p>",
    },
    {
        "text": "<p>Using the same information, how many books does Davron have?</p>",
        "choices": ["15", "10", "20", "5"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> 2(10) − 5. Tekshiruv: "
                       "10 + 15 = 25 ✓</p>",
    },
    {
        "text": "<p>A service charges a one-time fee of $50 and $12 a week. After how "
                "many weeks is the total $158?</p>",
        "choices": ["9", "13", "8", "12"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> (158 − 50) ÷ 12.</p>"
                       "<p><strong>13</strong> — bir martalik toʻlov "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>Why name the unknown with a sentence rather than a letter?</p>",
        "choices": ["The answer then checks itself when read aloud",
                    "Letters are not allowed on the scratchpad",
                    "It makes the equation shorter",
                    "The test requires it"],
        "correct": "The answer then checks itself when read aloud",
        "explanation": "<p><strong>Javob oʻzini tekshiradi.</strong> «Jasurda "
                       "8 ta kitob» — toʻgʻriligi ovoz chiqarganda "
                       "sezilib qoladi.</p>",
    },
    {
        "text": "<p>Samandar buys 3 notebooks and 2 pens for $23. A notebook costs "
                "$5. What does one pen cost?</p>",
        "choices": ["$4", "$8", "$3", "$6.50"],
        "correct": "$4",
        "explanation": "<p><strong>$4.</strong> 15 + 2p = 23 → 2p = 8.</p>"
                       "<p><strong>$8</strong> — ikkala ruchkaning "
                       "narxi.</p>",
    },
]


# =====================================================================
# SAT-95 — the scratchpad
# =====================================================================

Q_SAT95 = [
    {
        "text": "<p>What goes on the first line of the four-line scratchpad "
                "layout?</p>",
        "choices": ["The target — what the question asks for",
                    "The given numbers", "The equation", "The final answer"],
        "correct": "The target — what the question asks for",
        "explanation": "<p><strong>Maqsad.</strong> Uch-toʻrt soʻz, va u "
                       "birinchi tur tuzoqni butunlay yopadi.</p>",
    },
    {
        "text": "<p>A printer produces 24 pages a minute. A 900-page job starts at "
                "10:00. At what time does it finish, to the nearest minute?</p>",
        "choices": ["10:38", "10:24", "11:15", "10:15"],
        "correct": "10:38",
        "explanation": "<p><strong>10:38.</strong> 900 ÷ 24 = 37.5 → 38 "
                       "daqiqa.</p>"
                       "<p><strong>10:24</strong> — berilgan tezlik javob "
                       "sifatida qaytarilgan.</p>",
    },
    {
        "text": "<p>How many minutes does a 900-page job take at 24 pages a "
                "minute?</p>",
        "choices": ["37.5", "38", "21,600", "24"],
        "correct": "37.5",
        "explanation": "<p><strong>37.5.</strong> Yaxlitlash keyingi qadam — "
                       "qogʻozga ikkalasini ham yozing.</p>",
    },
    {
        "text": "<p>A printer produces 30 pages a minute. How long does a 450-page "
                "job take?</p>",
        "choices": ["15 minutes", "13,500 minutes", "20 minutes", "45 minutes"],
        "correct": "15 minutes",
        "explanation": "<p><strong>15 daqiqa.</strong> 450 ÷ 30.</p>",
    },
    {
        "text": "<p>A recipe for 4 people needs 300 grams of rice. How much is needed "
                "for 10 people?</p>",
        "choices": ["750 grams", "600 grams", "1,200 grams", "120 grams"],
        "correct": "750 grams",
        "explanation": "<p><strong>750.</strong> Bir kishiga 75 g.</p>"
                       "<p><strong>600</strong> — 4 dan 10 ga oʻtish «ikki "
                       "barobar» deb olingan; aslida 2.5 barobar.</p>",
    },
    {
        "text": "<p>The same recipe: how much rice is needed for 6 people?</p>",
        "choices": ["450 grams", "500 grams", "400 grams", "600 grams"],
        "correct": "450 grams",
        "explanation": "<p><strong>450.</strong> 6 × 75.</p>",
    },
    {
        "text": "<p>Should you copy the question onto the scratch paper?</p>",
        "choices": ["No, it is already on the screen",
                    "Yes, always", "Yes, for word problems only",
                    "Yes, but only the numbers"],
        "correct": "No, it is already on the screen",
        "explanation": "<p><strong>Yoʻq.</strong> Koʻchirish 30 soniya oladi "
                       "va hech narsa qoʻshmaydi.</p>",
    },
    {
        "text": "<p>Why draw a line between one question's work and the next?</p>",
        "choices": ["So the work can be found again on the second pass",
                    "To use less paper", "Because the rules require it",
                    "To make the writing neater"],
        "correct": "So the work can be found again on the second pass",
        "explanation": "<p><strong>Ikkinchi oʻtishda topish uchun.</strong> "
                       "Belgilangan savolga qaytganda ish tayyor turadi.</p>",
    },
    {
        "text": "<p>What belongs on the ANSWER line?</p>",
        "choices": ["The number together with its unit",
                    "The number alone", "The equation", "The question number"],
        "correct": "The number together with its unit",
        "explanation": "<p><strong>Son va birlik.</strong> Birliksiz son "
                       "savolga javob bermaydi.</p>",
    },
    {
        "text": "<p>A geometry figure is marked \"not drawn to scale.\" What should "
                "you do on paper?</p>",
        "choices": ["Redraw it honestly with the labels",
                    "Copy it exactly as shown",
                    "Measure it with the paper's edge",
                    "Ignore the figure completely"],
        "correct": "Redraw it honestly with the labels",
        "explanation": "<p><strong>Qayta chizing.</strong> Yorliqlarni oʻz "
                       "chizmangizga koʻchiring (SAT-86).</p>",
    },
    {
        "text": "<p>Ten people is how many times as many as four people?</p>",
        "choices": ["2.5", "2", "6", "3"],
        "correct": "2.5",
        "explanation": "<p><strong>2.5.</strong> 10 ÷ 4 — bu retsept "
                       "savolidagi tuzoqning kaliti.</p>",
    },
    {
        "text": "<p>A recipe for 4 people needs 300 grams. How much is that per "
                "person?</p>",
        "choices": ["75 grams", "60 grams", "80 grams", "120 grams"],
        "correct": "75 grams",
        "explanation": "<p><strong>75.</strong> 300 ÷ 4.</p>",
    },
    {
        "text": "<p>A 38-minute run at 24 pages a minute produces how many pages?</p>",
        "choices": ["912", "900", "62", "1,000"],
        "correct": "912",
        "explanation": "<p><strong>912.</strong> Bu NAZORAT qatori: 900 dan "
                       "sal koʻp, demak yaxlitlash toʻgʻri qilingan.</p>",
    },
    {
        "text": "<p>What does the test's answer-eliminator tool let you do?</p>",
        "choices": ["Cross out answer choices on the screen",
                    "Delete a question", "Add a slider to a graph",
                    "Change the time limit"],
        "correct": "Cross out answer choices on the screen",
        "explanation": "<p><strong>Variantlarni chizib tashlash.</strong> "
                       "Belgilangan savolga qaytganda ular saqlanib "
                       "turadi.</p>",
    },
    {
        "text": "<p>When is the four-line layout not worth writing?</p>",
        "choices": ["On a one-step question",
                    "On a word problem", "On a geometry question",
                    "On a grid-in question"],
        "correct": "On a one-step question",
        "explanation": "<p><strong>Bir qadamli savolda.</strong> Yozish "
                       "qilishdan uzoqroq davom etadi.</p>",
    },
    {
        "text": "<p>A printer runs for 20 minutes at 24 pages a minute. How many "
                "pages does it produce?</p>",
        "choices": ["480", "440", "1.2", "44"],
        "correct": "480",
        "explanation": "<p><strong>480.</strong> 20 × 24.</p>",
    },
    {
        "text": "<p>How long does a 600-page job take at 24 pages a minute?</p>",
        "choices": ["25 minutes", "24 minutes", "30 minutes", "14,400 minutes"],
        "correct": "25 minutes",
        "explanation": "<p><strong>25.</strong> 600 ÷ 24.</p>",
    },
    {
        "text": "<p>A job takes 37.5 minutes. What does \"to the nearest minute\" "
                "require?</p>",
        "choices": ["Rounding to 38", "Rounding to 37",
                    "Leaving it as 37.5", "Rounding to 40"],
        "correct": "Rounding to 38",
        "explanation": "<p><strong>38.</strong> Yarim daqiqa yuqoriga "
                       "yaxlitlanadi.</p>",
    },
    {
        "text": "<p>Desmos will solve the question for you. What still belongs on the "
                "paper?</p>",
        "choices": ["The target line", "Nothing at all",
                    "The full working", "A copy of the graph"],
        "correct": "The target line",
        "explanation": "<p><strong>Maqsad qatori.</strong> Desmos nuqtani "
                       "beradi, savolni oʻzingiz oʻqiysiz.</p>",
    },
    {
        "text": "<p>A tap fills 6 litres a minute. A 90-litre tank starts empty at "
                "08:00. At what time is it full?</p>",
        "choices": ["08:15", "08:06", "08:90", "09:30"],
        "correct": "08:15",
        "explanation": "<p><strong>08:15.</strong> 90 ÷ 6 = 15 daqiqa.</p>"
                       "<p><strong>08:06</strong> — berilgan tezlik javob "
                       "sifatida qaytarilgan.</p>",
    },
]


PRACTICES = [
    {
        "title":       "SAT-91 Practice: Translating English into Math (Key Terms Dictionary)",
        "description": "20 ta SAT uslubidagi savol — «less than» va «subtracted from» "
                       "teskari iboralari, «is» va «of», foizning uch turi.",
        "tutorial":    "SAT-91:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT91,
    },
    {
        "title":       "SAT-92 Practice: Recognizing Structure (Treating a Group as One Variable)",
        "description": "20 ta SAT uslubidagi savol — boʻlakni bitta son deb olish, "
                       "(x+y)² va a²−b² koʻpriklari, daraja tuzilmasi.",
        "tutorial":    "SAT-92:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT92,
    },
    {
        "title":       "SAT-93 Practice: The Extreme Plug-In Technique (0, 1, Negatives)",
        "description": "20 ta SAT uslubidagi savol — «must be true» savolida qarshi "
                       "misol qidirish; 0, 1, manfiy va kasrning kuchi.",
        "tutorial":    "SAT-93:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT93,
    },
    {
        "title":       "SAT-94 Practice: The Direct Translation Method for Word Problems",
        "description": "20 ta SAT uslubidagi savol — nomaʼlumni nomlash, jumlama-jumla "
                       "oʻgirish, bir martalik va takrorlanadigan toʻlov.",
        "tutorial":    "SAT-94:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT94,
    },
    {
        "title":       "SAT-95 Practice: Using the Scratchpad Effectively",
        "description": "20 ta SAT uslubidagi savol — MAQSAD/BERILGAN/ISH/JAVOB qolipi, "
                       "birlik yozish, qayta chizish va nazorat qatori.",
        "tutorial":    "SAT-95:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT95,
    },
]
