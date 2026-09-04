# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-56 … SAT-60.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

⚠️ Blok C: SAT-57 butunlay taqqoslash — hech bir savolda standart ogʻish
   hisoblanmaydi. SAT-60 da hisoblash umuman yoʻq.
⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_56_60.py --master=prime \\
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
# SAT-56 — mode, range, outliers
# =====================================================================

Q_SAT56 = [
    {
        "text": "<p>What is the mode of 3, 7, 7, 9, 12?</p>",
        "choices": ["7", "9", "7.6", "9.5"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> U ikki marta uchraydi.</p>"
                       "<p><strong>7.6</strong> — oʻrta arifmetik.</p>",
    },
    {
        "text": "<p>What is the range of 3, 7, 7, 9, 12?</p>",
        "choices": ["9", "12", "From 3 to 12", "7"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> 12 − 3.</p>"
                       "<p><strong>From 3 to 12</strong> — SAT'da «range» bitta "
                       "son, oraliq emas.</p>",
    },
    {
        "text": "<p>What is the mode of 2, 4, 6, 8, 10?</p>",
        "choices": ["There is no mode", "2", "6", "10"],
        "correct": "There is no mode",
        "explanation": "<p><strong>Moda yoʻq.</strong> Hamma qiymat bir "
                       "martadan.</p>"
                       "<p><strong>6</strong> — mediana va oʻrta arifmetik, moda "
                       "emas.</p>",
    },
    {
        "text": "<p>How many modes does the data set 4, 4, 7, 9, 9 have?</p>",
        "choices": ["Two", "One", "None", "Five"],
        "correct": "Two",
        "explanation": "<p><strong>Ikkita.</strong> 4 va 9 — ikkalasi ham ikki "
                       "martadan.</p>"
                       "<p>Bunday maʼlumot «bimodal» deyiladi.</p>",
    },
    {
        "text": "<p>A data set has a range of 0. What must be true?</p>",
        "choices": ["All the values are equal", "There is only one value",
                    "The mean is 0", "The mode is 0"],
        "correct": "All the values are equal",
        "explanation": "<p><strong>Barcha qiymatlar teng.</strong> Eng katta va "
                       "eng kichik bir xil.</p>"
                       "<p>Qiymatlar 100 boʻlsa ham oraliq nol boʻladi.</p>",
    },
    {
        "text": "<p>The value 200 is added to 5, 6, 7, 8. Which measure changes the "
                "most?</p>",
        "choices": ["The range", "The median", "The mode", "Nothing changes"],
        "correct": "The range",
        "explanation": "<p><strong>Oraliq.</strong> 3 dan 195 ga.</p>"
                       "<p>Mediana 6.5 dan 7 ga oʻzgaradi — juda kam.</p>",
    },
    {
        "text": "<p>Which measure is completely unaffected by adding one very large "
                "value to a data set?</p>",
        "choices": ["The mode", "The mean", "The range", "All of them change"],
        "correct": "The mode",
        "explanation": "<p><strong>Moda.</strong> Yangi qiymat bir marta "
                       "uchraydi, demak u moda boʻla olmaydi.</p>"
                       "<p>Mediana bir pogʻona surilishi mumkin, moda esa "
                       "qolaveradi.</p>",
    },
    {
        "text": "<p>A shop records shoe sizes sold: 38, 40, 40, 41, 42. Which measure "
                "is most useful for deciding what to restock?</p>",
        "choices": ["The mode", "The mean", "The range", "The sum"],
        "correct": "The mode",
        "explanation": "<p><strong>Moda.</strong> Eng koʻp sotilgani — 40.</p>"
                       "<p>Oʻrtacha 40.2 — bunday oʻlchamdagi tufli mavjud "
                       "emas.</p>",
    },
    {
        "text": "<p>The range of a data set is 15 and its smallest value is 8. What is "
                "the largest value?</p>",
        "choices": ["23", "15", "7", "120"],
        "correct": "23",
        "explanation": "<p><strong>23.</strong> 8 + 15.</p>"
                       "<p>Oraliq ayirma boʻlgani uchun eng kattasini topish "
                       "uchun qoʻshamiz.</p>",
    },
    {
        "text": "<p>Which data set has the larger range: A = 1, 2, 3, 100 or B = 40, "
                "45, 50, 55?</p>",
        "choices": ["A, with a range of 99", "B, with a range of 15",
                    "They are equal", "B, because its values are larger"],
        "correct": "A, with a range of 99",
        "explanation": "<p><strong>A, oraliqi 99.</strong> B ning oraliqi 15.</p>"
                       "<p>Qiymatlarning kattaligi emas, chekkalar orasidagi "
                       "masofa muhim.</p>",
    },
    {
        "text": "<p>In a survey of favourite colours, blue was chosen most often. Which "
                "measure is this?</p>",
        "choices": ["The mode", "The mean", "The median", "The range"],
        "correct": "The mode",
        "explanation": "<p><strong>Moda.</strong> U yagona oʻlchov boʻlib, son "
                       "boʻlmagan maʼlumotda ham ishlaydi.</p>"
                       "<p>Ranglarning oʻrtachasini hisoblab boʻlmaydi.</p>",
    },
    {
        "text": "<p>A teacher removes an outlier from a data set. Which pair is most "
                "likely to change a lot?</p>",
        "choices": ["The mean and the range", "The median and the mode",
                    "The mode and the range", "Nothing changes"],
        "correct": "The mean and the range",
        "explanation": "<p><strong>Oʻrta arifmetik va oraliq.</strong> Ikkalasi "
                       "ham qiymatlarning kattaligiga sezgir.</p>"
                       "<p>Mediana va moda faqat tartib va takrorlanishga "
                       "qaraydi.</p>",
    },
    {
        "text": "<p>A data set of test scores has a range of 60. What does this tell "
                "you about the middle of the data?</p>",
        "choices": ["Nothing at all", "The median is 30",
                    "The mean is 30", "Half the scores are above 30"],
        "correct": "Nothing at all",
        "explanation": "<p><strong>Hech narsa.</strong> Oraliq faqat ikki "
                       "chekkadan tuzilgan.</p>"
                       "<p>Oʻrtadagi barcha qiymatlar bir joyga toʻplangan ham "
                       "boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Which statement about an outlier is most accurate?</p>",
        "choices": ["It may be an error or a genuine unusual value",
                    "It is always a mistake and should be deleted",
                    "It is always the largest value",
                    "It has no effect on any measure"],
        "correct": "It may be an error or a genuine unusual value",
        "explanation": "<p><strong>Xato ham, haqiqiy hodisa ham boʻlishi "
                       "mumkin.</strong></p>"
                       "<p>Tashlab yuborishdan oldin sababini soʻrash "
                       "kerak.</p>",
    },
    {
        "text": "<p>A student says the range of 5, 9, 9, 14 is 'from 5 to 14'. What is "
                "the correct answer?</p>",
        "choices": ["9", "From 5 to 14", "14", "5"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> 14 − 5.</p>"
                       "<p>Tasodifan bu javob modaga ham teng — lekin usul "
                       "boshqa.</p>",
    },
    {
        "text": "<p>A student says 1, 2, 3, 4 has a mode of 1 because 1 comes first. "
                "What is correct?</p>",
        "choices": ["There is no mode", "The mode is 1", "The mode is 4",
                    "The mode is 2.5"],
        "correct": "There is no mode",
        "explanation": "<p><strong>Moda yoʻq.</strong> Moda — eng koʻp "
                       "<b>uchragan</b> qiymat, birinchisi emas.</p>",
    },
    {
        "text": "<p>Two data sets have the same range. What else must be true?</p>",
        "choices": ["Nothing else", "They have the same mean",
                    "They have the same number of values",
                    "They have the same median"],
        "correct": "Nothing else",
        "explanation": "<p><strong>Boshqa hech narsa.</strong> 1, 2, 10 va "
                       "50, 58, 59 — ikkalasining oraliqi 9.</p>"
                       "<p>Oraliq markaz haqida hech narsa aytmaydi.</p>",
    },
    {
        "text": "<p>Five numbers have a range of 20 and a smallest value of 3. If the "
                "largest value increases by 5, what is the new range?</p>",
        "choices": ["25", "20", "28", "5"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Eng kattasi 23 dan 28 ga chiqdi, "
                       "eng kichigi 3 boʻlib qoldi.</p>",
    },
    {
        "text": "<p>A factory records defects per day for a week: 2, 3, 2, 4, 2, 3, 40. "
                "Which measure best describes a typical day?</p>",
        "choices": ["The mode, 2", "The mean, about 8", "The range, 38",
                    "The largest value, 40"],
        "correct": "The mode, 2",
        "explanation": "<p><strong>Moda, 2.</strong> Odatiy kunda ikkita nuqson "
                       "boʻlgan.</p>"
                       "<p>Oʻrtacha taxminan 8 — 40 li kun tufayli, va u hech "
                       "bir kunga oʻxshamaydi.</p>",
    },
    {
        "text": "<p>For that same week, what should the factory do about the day with "
                "40 defects?</p>",
        "choices": ["Investigate why it happened before deciding anything",
                    "Delete it from the records",
                    "Assume it is a typing error",
                    "Recalculate the mean without it and report that"],
        "correct": "Investigate why it happened before deciding anything",
        "explanation": "<p><strong>Sababini tekshirish kerak.</strong> Bu kun "
                       "eng qimmatli maʼlumot boʻlishi mumkin.</p>"
                       "<p>Chetdagi qiymatni oʻchirish — maʼlumotni emas, "
                       "muammoni yashirish.</p>",
    },
]


# =====================================================================
# SAT-57 — standard deviation (taqqoslash, hisoblash emas)
# =====================================================================

Q_SAT57 = [
    {
        "text": "<p>Which data set has the greater standard deviation: A = 6, 7, 8, 9, "
                "10 or B = 2, 5, 8, 11, 14?</p>",
        "choices": ["B", "A", "They are equal", "It cannot be determined"],
        "correct": "B",
        "explanation": "<p><strong>B.</strong> Ikkalasining oʻrtachasi 8, lekin B "
                       "ning qiymatlari ancha uzoq tarqalgan.</p>"
                       "<p>Hisoblash shart emas — koʻz bilan koʻrinadi.</p>",
    },
    {
        "text": "<p>What is the standard deviation of 7, 7, 7, 7?</p>",
        "choices": ["0", "7", "1", "28"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Hamma qiymat teng — oʻrtachadan "
                       "chetlanish yoʻq.</p>",
    },
    {
        "text": "<p>Data set C is 5, 10, 15. Data set D is 105, 110, 115. Compare their "
                "standard deviations.</p>",
        "choices": ["They are equal", "D is greater", "C is greater",
                    "D is 21 times greater"],
        "correct": "They are equal",
        "explanation": "<p><strong>Teng.</strong> D — C ga 100 qoʻshilgani; "
                       "sonlar orasidagi masofalar oʻzgarmagan.</p>"
                       "<p>Faqat markaz siljidi.</p>",
    },
    {
        "text": "<p>Can a standard deviation be negative?</p>",
        "choices": ["No, it measures distance", "Yes, if the data is negative",
                    "Yes, if the mean is negative", "Only for small data sets"],
        "correct": "No, it measures distance",
        "explanation": "<p><strong>Yoʻq.</strong> U masofa oʻlchaydi, masofa esa "
                       "manfiy boʻlmaydi.</p>"
                       "<p>Maʼlumot manfiy boʻlsa ham ogʻish musbat qoladi.</p>",
    },
    {
        "text": "<p>Two histograms have the same mean. One is tall and narrow, the "
                "other short and wide. Which has the greater standard "
                "deviation?</p>",
        "choices": ["The short, wide one", "The tall, narrow one",
                    "They are equal", "It depends on the mean"],
        "correct": "The short, wide one",
        "explanation": "<p><strong>Keng va past boʻlgani.</strong> Maʼlumot "
                       "kengroq tarqalgan.</p>"
                       "<p>Tor va baland shakl — zich toʻplangan maʼlumot.</p>",
    },
    {
        "text": "<p>Data set E has values between 40 and 60. Data set F has values "
                "between 10 and 90. Both have a mean of 50. Which has the greater "
                "standard deviation?</p>",
        "choices": ["F", "E", "They are equal", "It cannot be determined"],
        "correct": "F",
        "explanation": "<p><strong>F.</strong> Uning qiymatlari oʻrtachadan "
                       "40 birlikkacha uzoq, E niki esa 10 birlikkacha.</p>",
    },
    {
        "text": "<p>Every value in a data set is multiplied by 2. What happens to the "
                "standard deviation?</p>",
        "choices": ["It doubles", "It stays the same", "It halves", "It becomes 0"],
        "correct": "It doubles",
        "explanation": "<p><strong>Ikki barobar oshadi.</strong> Barcha masofalar "
                       "ikki barobar kattalashdi.</p>"
                       "<p>Qoʻshish ogʻishni oʻzgartirmaydi, koʻpaytirish esa "
                       "oʻzgartiradi.</p>",
    },
    {
        "text": "<p>A class's scores are all between 78 and 82. What can you say about "
                "the standard deviation?</p>",
        "choices": ["It is small", "It is large", "It is zero", "It is negative"],
        "correct": "It is small",
        "explanation": "<p><strong>Kichik.</strong> Qiymatlar juda zich "
                       "toʻplangan.</p>"
                       "<p>Nol emas, chunki ular aynan teng emas.</p>",
    },
    {
        "text": "<p>Which statement is true about the mean and the standard "
                "deviation?</p>",
        "choices": ["Two data sets can share a mean and have different spreads",
                    "The same mean means the same spread",
                    "A larger mean always means a larger spread",
                    "The standard deviation equals the mean"],
        "correct": "Two data sets can share a mean and have different spreads",
        "explanation": "<p><strong>Ha, boʻlishi mumkin.</strong> Markaz va "
                       "tarqalish bir-biriga bogʻliq emas.</p>"
                       "<p>6, 6, 6 va 1, 6, 11 — bir xil oʻrtacha, boshqa "
                       "ogʻish.</p>",
    },
    {
        "text": "<p>Two machines fill bottles to a mean of 500 ml. Machine X has a "
                "standard deviation of 2 ml; machine Y, 15 ml. Which is more "
                "consistent?</p>",
        "choices": ["Machine X", "Machine Y", "They are equally consistent",
                    "It cannot be determined"],
        "correct": "Machine X",
        "explanation": "<p><strong>X mashinasi.</strong> Kichikroq ogʻish — "
                       "natijalar oʻrtachaga yaqinroq.</p>"
                       "<p>Ishlab chiqarishda kichik ogʻish sifat "
                       "belgisi.</p>",
    },
    {
        "text": "<p>A data set of salaries has a large standard deviation. What does "
                "this mean in context?</p>",
        "choices": ["Salaries vary widely across the group",
                    "Salaries are all high",
                    "Salaries are all low",
                    "The mean salary is large"],
        "correct": "Salaries vary widely across the group",
        "explanation": "<p><strong>Maoshlar keng tarqalgan.</strong> Ogʻish "
                       "farqni oʻlchaydi, darajani emas.</p>",
    },
    {
        "text": "<p>Ten students all score exactly 75 on a test. What is the standard "
                "deviation of the scores?</p>",
        "choices": ["0", "75", "7.5", "10"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Barcha qiymatlar bir xil.</p>"
                       "<p>Nol ogʻish faqat shu holatda boʻladi.</p>",
    },
    {
        "text": "<p>Set G is 1, 2, 3 and set H is 1, 2, 3, 100. Which has the greater "
                "standard deviation?</p>",
        "choices": ["H", "G", "They are equal", "Neither has one"],
        "correct": "H",
        "explanation": "<p><strong>H.</strong> 100 oʻrtachadan juda uzoq va "
                       "tarqalishni keskin oshiradi.</p>"
                       "<p>Chetdagi qiymat ogʻishga ham kuchli taʼsir "
                       "qiladi.</p>",
    },
    {
        "text": "<p>Two towns have the same mean temperature. Town P ranges from 15 to "
                "25 degrees; town Q from 0 to 40. Which has the greater standard "
                "deviation?</p>",
        "choices": ["Town Q", "Town P", "They are equal", "It depends on the season"],
        "correct": "Town Q",
        "explanation": "<p><strong>Q shahri.</strong> Haroratlar ancha keng "
                       "tarqalgan.</p>"
                       "<p>Bir xil oʻrtacha butunlay boshqa iqlimni "
                       "yashirishi mumkin.</p>",
    },
    {
        "text": "<p>A student says set D (105, 110, 115) has a greater standard "
                "deviation than set C (5, 10, 15) because its numbers are bigger. What "
                "is correct?</p>",
        "choices": ["They are equal", "D is greater", "C is greater",
                    "Neither can be compared"],
        "correct": "They are equal",
        "explanation": "<p><strong>Teng.</strong> Kattalik va tarqoqlik — ikki "
                       "boshqa narsa.</p>"
                       "<p>Har bir qiymatga bir xil son qoʻshish ogʻishni "
                       "oʻzgartirmaydi.</p>",
    },
    {
        "text": "<p>A student says two sets with the same mean must have the same "
                "standard deviation. What is a counterexample?</p>",
        "choices": ["4, 4, 4 and 1, 4, 7", "1, 2, 3 and 4, 5, 6",
                    "2, 4, 6 and 3, 5, 7", "There is no counterexample"],
        "correct": "4, 4, 4 and 1, 4, 7",
        "explanation": "<p><strong>4, 4, 4 va 1, 4, 7.</strong> Ikkalasining "
                       "oʻrtachasi 4, lekin birinchisining ogʻishi nol.</p>"
                       "<p>Qolgan variantlarda oʻrtachalar teng emas.</p>",
    },
    {
        "text": "<p>A quality inspector wants bottles as close to 500 ml as possible. "
                "Which target should be set?</p>",
        "choices": ["A small standard deviation", "A large standard deviation",
                    "A large mean", "A small mean"],
        "correct": "A small standard deviation",
        "explanation": "<p><strong>Kichik ogʻish.</strong> Bu barcha shishalar "
                       "500 ga yaqin degani.</p>",
    },
    {
        "text": "<p>Set J is 20, 30, 40. Every value is decreased by 10. What is the "
                "new standard deviation compared with the old?</p>",
        "choices": ["The same", "10 less", "Smaller but not by 10", "Zero"],
        "correct": "The same",
        "explanation": "<p><strong>Oʻsha-oʻsha.</strong> Bir xil son ayirilsa "
                       "ham masofalar oʻzgarmaydi.</p>"
                       "<p>Faqat oʻrtacha 30 dan 20 ga tushdi.</p>",
    },
    {
        "text": "<p>Two exam classes have mean 70. Class A's standard deviation is 4, "
                "class B's is 18. Which conclusion is best supported?</p>",
        "choices": ["Class B's results are far more varied",
                    "Class B scored higher on average",
                    "Class A had more students",
                    "Class A's best score was higher"],
        "correct": "Class B's results are far more varied",
        "explanation": "<p><strong>B sinfda natijalar ancha xilma-xil.</strong></p>"
                       "<p>Ogʻish oʻrtachani ham, sinf hajmini ham "
                       "koʻrsatmaydi.</p>",
    },
    {
        "text": "<p>A bus company reports mean waiting time 10 minutes with a standard "
                "deviation of 9 minutes. What does this suggest to a passenger?</p>",
        "choices": ["Waiting times are unpredictable",
                    "Every wait is about 10 minutes",
                    "The buses are always late",
                    "The mean must be wrong"],
        "correct": "Waiting times are unpredictable",
        "explanation": "<p><strong>Kutish vaqti oldindan aytib "
                       "boʻlmaydi.</strong> Ogʻish oʻrtachaga deyarli teng.</p>"
                       "<p>Baʼzida bir daqiqa, baʼzida yigirma — oʻrtacha esa "
                       "oʻn.</p>",
    },
]


# =====================================================================
# SAT-58 — probability
# =====================================================================

Q_SAT58 = [
    {
        "text": "<p>A fair die is rolled. What is the probability of rolling a 3?</p>",
        "choices": ["1/6", "1/3", "5/6", "1/2"],
        "correct": "1/6",
        "explanation": "<p><strong>1/6.</strong> Bitta qulay hol, olti hol.</p>",
    },
    {
        "text": "<p>A bag holds 4 red and 6 blue balls. What is the probability of "
                "drawing a red ball?</p>",
        "choices": ["2/5", "4/6", "1/4", "6/10"],
        "correct": "2/5",
        "explanation": "<p><strong>2/5.</strong> 4 ÷ 10, qisqartirilgan.</p>"
                       "<p><strong>4/6</strong> — maxrajga koʻklar soni "
                       "qoʻyilgan; jami 10 ta.</p>",
    },
    {
        "text": "<p>A bag holds 4 red and 6 blue balls. What is the probability of "
                "<i>not</i> drawing a red ball?</p>",
        "choices": ["3/5", "2/5", "1/6", "4/6"],
        "correct": "3/5",
        "explanation": "<p><strong>3/5.</strong> 1 − 2/5, yoki 6 ÷ 10.</p>",
    },
    {
        "text": "<p>A fair coin is flipped twice. What is the probability of two "
                "tails?</p>",
        "choices": ["1/4", "1/2", "1", "3/4"],
        "correct": "1/4",
        "explanation": "<p><strong>1/4.</strong> 1/2 × 1/2.</p>"
                       "<p>Toʻrt teng hol bor va faqat bittasi ikkita "
                       "raqam.</p>",
    },
    {
        "text": "<p>A spinner has 8 equal sections numbered 1 to 8. What is the "
                "probability of landing on a number greater than 5?</p>",
        "choices": ["3/8", "5/8", "1/8", "1/2"],
        "correct": "3/8",
        "explanation": "<p><strong>3/8.</strong> 6, 7 va 8 — uchta hol.</p>"
                       "<p>«Greater than 5» 5 ni oʻz ichiga olmaydi.</p>",
    },
    {
        "text": "<p>Two fair dice are rolled. What is the probability that both show "
                "an even number?</p>",
        "choices": ["1/4", "1/2", "1/6", "1/36"],
        "correct": "1/4",
        "explanation": "<p><strong>1/4.</strong> Har birida juft son ehtimoli "
                       "1/2, va 1/2 × 1/2.</p>",
    },
    {
        "text": "<p>A class has 12 girls and 18 boys. One student is chosen at random. "
                "What is the probability of choosing a girl?</p>",
        "choices": ["2/5", "12/18", "1/2", "3/5"],
        "correct": "2/5",
        "explanation": "<p><strong>2/5.</strong> 12 ÷ 30.</p>"
                       "<p><strong>12/18</strong> — qizlar oʻgʻillarga "
                       "boʻlingan, jamiga emas.</p>",
    },
    {
        "text": "<p>A bag has 5 white and 5 black balls. Two are drawn without "
                "replacement. What is the probability that both are white?</p>",
        "choices": ["2/9", "1/4", "1/2", "5/9"],
        "correct": "2/9",
        "explanation": "<p><strong>2/9.</strong> 5/10 × 4/9.</p>"
                       "<p><strong>1/4</strong> — qaytarish boʻlganda "
                       "toʻgʻri boʻlardi.</p>",
    },
    {
        "text": "<p>The same bag, but the first ball is replaced before the second "
                "draw. What is the probability that both are white?</p>",
        "choices": ["1/4", "2/9", "1/2", "1/5"],
        "correct": "1/4",
        "explanation": "<p><strong>1/4.</strong> 5/10 × 5/10 — maxraj "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>A coin is flipped three times. What is the probability of getting "
                "at least one head?</p>",
        "choices": ["7/8", "1/8", "3/8", "1/2"],
        "correct": "7/8",
        "explanation": "<p><strong>7/8.</strong> Teskarisi: bittasi ham gerb "
                       "emas — 1/8. Demak 1 − 1/8.</p>"
                       "<p>«At least one» savolida teskari yoʻl har doim "
                       "tezroq.</p>",
    },
    {
        "text": "<p>A coin has landed heads four times in a row. What is the "
                "probability of heads on the fifth flip?</p>",
        "choices": ["1/2", "1/32", "1/16", "Less than 1/2"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> Tangada xotira yoʻq — har bir "
                       "tashlash bogʻliqsiz.</p>"
                       "<p><strong>1/32</strong> — beshta gerb ketma-ket "
                       "kelishining ehtimoli, boshqa savol.</p>",
    },
    {
        "text": "<p>A probability is reported as 1.4. What must be true?</p>",
        "choices": ["A mistake has been made", "The event is very likely",
                    "The event is certain", "The event happens 1.4 times"],
        "correct": "A mistake has been made",
        "explanation": "<p><strong>Xato bor.</strong> Ehtimollik 0 va 1 "
                       "orasida boʻlishi shart.</p>"
                       "<p>Koʻpincha qoʻshish oʻrniga koʻpaytirish yoki "
                       "notoʻgʻri maxraj sabab boʻladi.</p>",
    },
    {
        "text": "<p>A box holds 3 pens and 7 pencils. What is the probability of "
                "drawing a pen or a pencil?</p>",
        "choices": ["1", "3/10", "7/10", "21/100"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> Qutida boshqa hech narsa yoʻq — "
                       "hodisa aniq.</p>"
                       "<p>3/10 + 7/10 = 1.</p>",
    },
    {
        "text": "<p>A weather forecast says 30% chance of rain on Saturday and 30% on "
                "Sunday, and the days are independent. What is the probability of rain "
                "on both days?</p>",
        "choices": ["9%", "60%", "30%", "3%"],
        "correct": "9%",
        "explanation": "<p><strong>9%.</strong> 0.3 × 0.3 = 0.09.</p>"
                       "<p><strong>60%</strong> — ehtimollar qoʻshilgan; «va» "
                       "koʻpaytirishni bildiradi.</p>",
    },
    {
        "text": "<p>A student computes the probability of two sixes on two dice as "
                "1/6 + 1/6. What is the correct answer?</p>",
        "choices": ["1/36", "1/3", "1/6", "1/12"],
        "correct": "1/36",
        "explanation": "<p><strong>1/36.</strong> «Va» — koʻpaytirish.</p>"
                       "<p>Qoʻshish natijasi 1/3 boʻlardi, va u birdan "
                       "koʻra katta ehtimolni bildiradi — mantiqan "
                       "notoʻgʻri.</p>",
    },
    {
        "text": "<p>A student says drawing two red balls without replacement from 5 red "
                "and 5 blue is 1/4. What is the correct answer?</p>",
        "choices": ["2/9", "1/4", "1/5", "4/9"],
        "correct": "2/9",
        "explanation": "<p><strong>2/9.</strong> Ikkinchi tortishda 4 qizil "
                       "va jami 9 ta qoladi.</p>"
                       "<p>Oʻquvchi qaytarish bordek hisoblagan.</p>",
    },
    {
        "text": "<p>A bag has 6 red, 4 green and 10 yellow sweets. What is the "
                "probability of drawing a sweet that is not yellow?</p>",
        "choices": ["1/2", "1/5", "3/10", "2/5"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> Sariq boʻlmaganlar 10 ta, jami "
                       "20 ta.</p>"
                       "<p>Yoki 1 − 10/20.</p>",
    },
    {
        "text": "<p>Two independent events each have probability 1/3. What is the "
                "probability that neither happens?</p>",
        "choices": ["4/9", "2/3", "1/9", "5/9"],
        "correct": "4/9",
        "explanation": "<p><strong>4/9.</strong> Har biri sodir boʻlmasligi "
                       "2/3, va 2/3 × 2/3.</p>"
                       "<p>«Hech biri» — ikkala teskari hodisa birga.</p>",
    },
    {
        "text": "<p>A lottery sells 500 tickets and a person buys 4. What is the "
                "probability of holding the single winning ticket?</p>",
        "choices": ["1/125", "4/500 rounded", "1/500", "4/125"],
        "correct": "1/125",
        "explanation": "<p><strong>1/125.</strong> 4 ÷ 500, qisqartirilgan.</p>"
                       "<p>Qisqartirmasdan qoldirish notoʻgʻri emas, lekin "
                       "SAT javoblari odatda sodda koʻrinishda.</p>",
    },
    {
        "text": "<p>A machine produces parts, and 2% are faulty. Two parts are chosen "
                "independently. What is the probability that both are faulty?</p>",
        "choices": ["0.04%", "4%", "2%", "0.4%"],
        "correct": "0.04%",
        "explanation": "<p><strong>0.04%.</strong> 0.02 × 0.02 = 0.0004.</p>"
                       "<p><strong>4%</strong> — foizlar koʻpaytirilib, "
                       "foizga qaytarish unutilgan.</p>",
    },
]


# =====================================================================
# SAT-59 — conditional probability
# =====================================================================
# Jadval: Men tea 30, coffee 45 (75) · Women tea 50, coffee 25 (75)
#         Tea 80 · Coffee 70 · Total 150

Q_SAT59 = [
    {
        "text": "<p>A survey of 150 people gives: men — 30 prefer tea, 45 coffee; "
                "women — 50 tea, 25 coffee. How many people prefer tea?</p>",
        "choices": ["80", "75", "70", "30"],
        "correct": "80",
        "explanation": "<p><strong>80.</strong> 30 + 50.</p>"
                       "<p>Chekka yigʻindilarni darrov yozib qoʻying.</p>",
    },
    {
        "text": "<p>Using that table, what is the probability that a randomly chosen "
                "person prefers coffee?</p>",
        "choices": ["70/150", "45/75", "25/75", "70/80"],
        "correct": "70/150",
        "explanation": "<p><strong>70/150.</strong> Shart yoʻq — maxraj jami "
                       "150.</p>",
    },
    {
        "text": "<p>Using that table, given that a person is a man, what is the "
                "probability he prefers tea?</p>",
        "choices": ["30/75", "30/80", "30/150", "75/150"],
        "correct": "30/75",
        "explanation": "<p><strong>30/75.</strong> «Given that a man» — maxraj "
                       "erkaklar soni.</p>"
                       "<p>Bu 0.4 ga teng.</p>",
    },
    {
        "text": "<p>Using that table, given that a person prefers tea, what is the "
                "probability the person is a man?</p>",
        "choices": ["30/80", "30/75", "30/150", "80/150"],
        "correct": "30/80",
        "explanation": "<p><strong>30/80.</strong> Shart choy tanlaganlarni "
                       "belgilaydi.</p>"
                       "<p>Bu 0.375 — oldingi savolning javobidan farq "
                       "qiladi.</p>",
    },
    {
        "text": "<p>Using that table, what is the probability that a randomly chosen "
                "person is a woman who prefers coffee?</p>",
        "choices": ["25/150", "25/75", "25/70", "70/150"],
        "correct": "25/150",
        "explanation": "<p><strong>25/150.</strong> Shart soʻzi yoʻq — maxraj "
                       "butun guruh.</p>"
                       "<p>Qisqartirilsa 1/6.</p>",
    },
    {
        "text": "<p>Using that table, among the women, what is the probability of "
                "preferring tea?</p>",
        "choices": ["50/75", "50/80", "50/150", "75/150"],
        "correct": "50/75",
        "explanation": "<p><strong>50/75, yaʼni 2/3.</strong> «Among the women» "
                       "maxrajni belgiladi.</p>",
    },
    {
        "text": "<p>Using that table, of those who prefer coffee, what percent are "
                "men?</p>",
        "choices": ["About 64%", "60%", "About 36%", "30%"],
        "correct": "About 64%",
        "explanation": "<p><strong>Taxminan 64%.</strong> 45 ÷ 70 ≈ 0.643.</p>"
                       "<p><strong>60%</strong> — 45 ÷ 75, yaʼni erkaklar "
                       "maxrajga olingan.</p>",
    },
    {
        "text": "<p>Using that table, what percent of the men prefer coffee?</p>",
        "choices": ["60%", "About 64%", "30%", "45%"],
        "correct": "60%",
        "explanation": "<p><strong>60%.</strong> 45 ÷ 75.</p>"
                       "<p>Bu oldingi savolning teskarisi — bir xil katak, "
                       "boshqa maxraj.</p>",
    },
    {
        "text": "<p>Using that table, what is the sum of the probability of tea given a "
                "man and coffee given a man?</p>",
        "choices": ["1", "0.75", "150", "0.5"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> 30/75 + 45/75 = 75/75.</p>"
                       "<p>Bitta shart ostidagi barcha ehtimollar birga "
                       "teng — foydali tekshiruv.</p>",
    },
    {
        "text": "<p>In a two-way table, which phrase tells you the denominator?</p>",
        "choices": ["'given that' or 'of those who'",
                    "'and'", "'at random'", "'the probability that'"],
        "correct": "'given that' or 'of those who'",
        "explanation": "<p><strong>«Given that» yoki «of those who».</strong> "
                       "Ulardan keyingi guruh maxraj boʻladi.</p>"
                       "<p>«And» esa ikkala shartni suratga qoʻyadi.</p>",
    },
    {
        "text": "<p>A student answers 'given that a person prefers tea, the probability "
                "of a man' with 30/75. What is correct?</p>",
        "choices": ["30/80", "30/75", "30/150", "75/80"],
        "correct": "30/80",
        "explanation": "<p><strong>30/80.</strong> Oʻquvchi shartni teskari "
                       "olgan.</p>"
                       "<p>Uning javobi «given that a man, tea» ning "
                       "javobidir.</p>",
    },
    {
        "text": "<p>A student computes 'a man who prefers tea' from all 150 people as "
                "30/75. What is correct?</p>",
        "choices": ["30/150", "30/75", "30/80", "75/150"],
        "correct": "30/150",
        "explanation": "<p><strong>30/150.</strong> Shart soʻzi yoʻq, demak "
                       "maxraj butun guruh.</p>",
    },
    {
        "text": "<p>In a different table, 60 students take art and 90 take music, with "
                "150 students in total and no overlap. Given that a student takes art, "
                "what is the probability they take music?</p>",
        "choices": ["0", "90/150", "60/150", "90/60"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Kesishma yoʻq — sanʼat oluvchi "
                       "musiqa olmaydi.</p>"
                       "<p>Shartli ehtimollik nol boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Using the tea and coffee table, is a randomly chosen tea drinker "
                "more likely to be a man or a woman?</p>",
        "choices": ["A woman, because 50 of the 80 tea drinkers are women",
                    "A man, because 30 is a large number",
                    "Equally likely",
                    "It cannot be determined"],
        "correct": "A woman, because 50 of the 80 tea drinkers are women",
        "explanation": "<p><strong>Ayol.</strong> 50/80 va 30/80 — birinchisi "
                       "kattaroq.</p>"
                       "<p>Ikkala ehtimol ham bir xil maxrajga ega, shuning "
                       "uchun suratlarni solishtirish yetadi.</p>",
    },
    {
        "text": "<p>Using that table, what is the probability that a randomly chosen "
                "person is a man or prefers tea?</p>",
        "choices": ["125/150", "155/150", "105/150", "80/150"],
        "correct": "125/150",
        "explanation": "<p><strong>125/150.</strong> Erkaklar 75, choy 80, "
                       "lekin 30 kishi ikkalasida ham: 75 + 80 − 30.</p>"
                       "<p><strong>155/150</strong> — kesishma ikki marta "
                       "sanalgan, va javob birdan katta chiqqan.</p>",
    },
    {
        "text": "<p>A hospital table shows: of 200 patients, 40 have symptom X and a "
                "positive test; 10 have symptom X and a negative test. Given symptom X, "
                "what is the probability of a positive test?</p>",
        "choices": ["40/50", "40/200", "40/210", "50/200"],
        "correct": "40/50",
        "explanation": "<p><strong>40/50, yaʼni 4/5.</strong> Belgi X bor "
                       "bemorlar 50 ta.</p>"
                       "<p>Maxraj shartni qanoatlantiradigan barcha "
                       "holatlar.</p>",
    },
    {
        "text": "<p>Using the tea and coffee table, which two probabilities are "
                "equal?</p>",
        "choices": ["The probability a person is a man, and the probability a person is a woman",
                    "Tea given a man, and a man given tea",
                    "Coffee given a woman, and a woman given coffee",
                    "None of them are equal"],
        "correct": "The probability a person is a man, and the probability a person is a woman",
        "explanation": "<p><strong>Erkak va ayol ehtimollari.</strong> "
                       "Ikkalasi ham 75/150.</p>"
                       "<p>Shartli juftliklar esa teng emas — bu darsning "
                       "asosiy gʻoyasi.</p>",
    },
    {
        "text": "<p>A club table shows 24 members under 18 and 36 over 18; of the under "
                "18s, 18 play chess. Given a member is under 18, what is the probability "
                "they play chess?</p>",
        "choices": ["3/4", "18/60", "18/36", "24/60"],
        "correct": "3/4",
        "explanation": "<p><strong>3/4.</strong> 18 ÷ 24.</p>"
                       "<p><strong>18/60</strong> — butun klub maxrajga "
                       "olingan, lekin shart bor edi.</p>",
    },
    {
        "text": "<p>A school reports that 70% of pupils who cycle live within 2 km. "
                "Which question does this answer?</p>",
        "choices": ["Given that a pupil cycles, do they live within 2 km?",
                    "Given that a pupil lives within 2 km, do they cycle?",
                    "What percent of all pupils cycle?",
                    "What percent of all pupils live within 2 km?"],
        "correct": "Given that a pupil cycles, do they live within 2 km?",
        "explanation": "<p><strong>Velosipedchilar orasida.</strong> "
                       "«Pupils who cycle» maxrajni belgilaydi.</p>"
                       "<p>Teskari savolning javobi butunlay boshqa "
                       "boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Of 100 shoppers, 60 bought bread and 30 of those also bought milk. "
                "What is the probability that a randomly chosen shopper bought both?</p>",
        "choices": ["30/100", "30/60", "60/100", "90/100"],
        "correct": "30/100",
        "explanation": "<p><strong>30/100.</strong> Tanlov barcha xaridorlardan, "
                       "demak maxraj 100.</p>"
                       "<p><strong>30/60</strong> — «non olganlar orasida sut "
                       "olish» ehtimoli, boshqa savol.</p>",
    },
]


# =====================================================================
# SAT-60 — sample surveys  (hisoblash yoʻq, faqat xulosa)
# =====================================================================

Q_SAT60 = [
    {
        "text": "<p>A random sample of 150 students is selected from the 900 students at "
                "one school. To which group can the results be generalized?</p>",
        "choices": ["The 900 students at that school", "All students in the country",
                    "Only the 150 students sampled", "All young people"],
        "correct": "The 900 students at that school",
        "explanation": "<p><strong>Oʻsha maktabning 900 oʻquvchisiga.</strong> "
                       "Tanlanma shu guruhdan olingan.</p>"
                       "<p>Undan kengroq guruhga umumlashtirib boʻlmaydi.</p>",
    },
    {
        "text": "<p>Why is random selection important in a survey?</p>",
        "choices": ["It makes the sample representative of the group it was drawn from",
                    "It makes the sample larger",
                    "It proves cause and effect",
                    "It removes the margin of error"],
        "correct": "It makes the sample representative of the group it was drawn from",
        "explanation": "<p><strong>Vakillik qilishini taʼminlaydi.</strong></p>"
                       "<p>Sabab uchun tasodifiy <b>taqsimlash</b> kerak, "
                       "tanlash emas.</p>",
    },
    {
        "text": "<p>A survey is conducted only among people leaving a gym. What is the "
                "main problem?</p>",
        "choices": ["The sample is not random and over-represents active people",
                    "The sample is too small",
                    "The questions are unclear",
                    "There is no problem"],
        "correct": "The sample is not random and over-represents active people",
        "explanation": "<p><strong>Tanlanma tasodifiy emas.</strong> Sport bilan "
                       "shugʻullanadiganlar ortiqcha vakillik qiladi.</p>",
    },
    {
        "text": "<p>A poll reports 46% support with a margin of error of 3%. What is the "
                "plausible range?</p>",
        "choices": ["43% to 49%", "46% to 49%", "43% to 46%", "Exactly 46%"],
        "correct": "43% to 49%",
        "explanation": "<p><strong>43% dan 49% gacha.</strong> Ikkala tomonga "
                       "3 foizdan.</p>",
    },
    {
        "text": "<p>Increasing a random sample from 100 to 1,000 people will generally</p>",
        "choices": ["reduce the margin of error", "remove all bias",
                    "prove causation", "change the population"],
        "correct": "reduce the margin of error",
        "explanation": "<p><strong>Xatolik chegarasini kamaytiradi.</strong></p>"
                       "<p>Ogʻishni esa u tuzatmaydi — u faqat aniqlikni "
                       "oshiradi.</p>",
    },
    {
        "text": "<p>Increasing a <i>non-random</i> sample from 100 to 10,000 people "
                "will</p>",
        "choices": ["not fix the bias", "make the results reliable",
                    "remove the margin of error", "prove the conclusion"],
        "correct": "not fix the bias",
        "explanation": "<p><strong>Ogʻishni tuzatmaydi.</strong> Katta hajm "
                       "notoʻgʻri javobni faqat aniqroq qiladi.</p>"
                       "<p>Avval <b>qanday</b> tanlangani muhim.</p>",
    },
    {
        "text": "<p>Two candidates poll at 44% and 48%, each with a margin of error of "
                "5%. What can be concluded?</p>",
        "choices": ["No lead can be claimed, because the ranges overlap",
                    "The second candidate leads",
                    "The first candidate leads",
                    "The poll is invalid"],
        "correct": "No lead can be claimed, because the ranges overlap",
        "explanation": "<p><strong>Yetakchini aytib boʻlmaydi.</strong> "
                       "39–49 va 43–53 oraliqlari kesishadi.</p>",
    },
    {
        "text": "<p>A researcher surveys shoppers on a Tuesday morning in one shopping "
                "centre. Which group do the results describe?</p>",
        "choices": ["Only shoppers there at that time",
                    "All shoppers in the city",
                    "All people in the country",
                    "All people who shop on Tuesdays"],
        "correct": "Only shoppers there at that time",
        "explanation": "<p><strong>Faqat oʻsha vaqtdagi xaridorlar.</strong></p>"
                       "<p>Seshanba ertalab xarid qiladiganlar butun aholining "
                       "vakili emas.</p>",
    },
    {
        "text": "<p>Which sample is most likely to represent all the residents of a "
                "town?</p>",
        "choices": ["A random sample drawn from the town's residence register",
                    "People who answer a phone poll on a weekday morning",
                    "People who reply to a newspaper advertisement",
                    "People at a town football match"],
        "correct": "A random sample drawn from the town's residence register",
        "explanation": "<p><strong>Roʻyxatdan tasodifiy tanlanma.</strong> "
                       "Har bir aholi teng imkoniyatga ega.</p>"
                       "<p>Qolgan uchtasida odamlar oʻzlarini tanlaydi "
                       "yoki maʼlum guruh ustunlik qiladi.</p>",
    },
    {
        "text": "<p>A study finds that people who take a certain vitamin have fewer "
                "colds. The participants chose whether to take it. What can be "
                "concluded?</p>",
        "choices": ["Taking the vitamin is associated with fewer colds",
                    "The vitamin prevents colds",
                    "Colds prevent people from taking vitamins",
                    "Nothing at all can be learned"],
        "correct": "Taking the vitamin is associated with fewer colds",
        "explanation": "<p><strong>Bogʻliqlik bor.</strong> Qatnashchilar "
                       "oʻzlari tanlagani uchun sabab isbotlanmaydi.</p>"
                       "<p>Sabab uchun tasodifiy taqsimlash kerak edi.</p>",
    },
    {
        "text": "<p>A survey of a random sample of 400 farmers in one region finds 65% "
                "grow wheat. Which statement is most appropriate?</p>",
        "choices": ["About 65% of farmers in that region grow wheat",
                    "Exactly 65% of farmers in that region grow wheat",
                    "About 65% of farmers everywhere grow wheat",
                    "65% of all people grow wheat"],
        "correct": "About 65% of farmers in that region grow wheat",
        "explanation": "<p><strong>Taxminan 65% — oʻsha viloyat "
                       "fermerlari.</strong></p>"
                       "<p>«Exactly» — tanlanma hech qachon aniq songa "
                       "kafolat bermaydi.</p>",
    },
    {
        "text": "<p>What does a margin of error describe?</p>",
        "choices": ["How far the true value is likely to be from the reported one",
                    "How many people refused to answer",
                    "How many questions were wrong",
                    "The percentage who said yes"],
        "correct": "How far the true value is likely to be from the reported one",
        "explanation": "<p><strong>Haqiqiy qiymat qanchalik uzoq boʻlishi "
                       "mumkinligi.</strong></p>"
                       "<p>U natijani bitta son emas, oraliq qiladi.</p>",
    },
    {
        "text": "<p>A school surveys every pupil in the school. What is the margin of "
                "error for the whole school?</p>",
        "choices": ["There is none — this is a census, not a sample",
                    "It is very large", "It is 5%", "It cannot be determined"],
        "correct": "There is none — this is a census, not a sample",
        "explanation": "<p><strong>Yoʻq — bu tanlanma emas, toʻliq "
                       "roʻyxat.</strong></p>"
                       "<p>Xatolik chegarasi faqat tanlanmada paydo "
                       "boʻladi.</p>",
    },
    {
        "text": "<p>Which phrase in an answer choice should make you suspicious in a "
                "survey question?</p>",
        "choices": ["'proves that'", "'is associated with'",
                    "'about'", "'in this sample'"],
        "correct": "'proves that'",
        "explanation": "<p><strong>«Proves that».</strong> Soʻrovnoma hech "
                       "narsani isbotlamaydi.</p>"
                       "<p>Qolgan uchtasi ehtiyotkor iboralar.</p>",
    },
    {
        "text": "<p>A student says a survey of 2,000 self-selected internet users "
                "represents the whole country because the sample is large. What is "
                "wrong?</p>",
        "choices": ["Self-selected samples are biased regardless of size",
                    "2,000 is too small",
                    "Internet users cannot be surveyed",
                    "Nothing is wrong"],
        "correct": "Self-selected samples are biased regardless of size",
        "explanation": "<p><strong>Oʻzini tanlagan tanlanma ogʻishgan.</strong> "
                       "Hajm bunga taʼsir qilmaydi.</p>",
    },
    {
        "text": "<p>A student concludes from a random sample of one school that the "
                "result applies to all schools in the country. What is wrong?</p>",
        "choices": ["The sample came from only one school",
                    "The sample was random",
                    "The sample was too large",
                    "Nothing is wrong"],
        "correct": "The sample came from only one school",
        "explanation": "<p><strong>Tanlanma bitta maktabdan.</strong> Xulosa "
                       "shu maktab bilan chegaralanadi.</p>",
    },
    {
        "text": "<p>A council wants to know how residents feel about a new park. Which "
                "method gives the most trustworthy result?</p>",
        "choices": ["Post questionnaires to a random sample of households",
                    "Ask people already visiting the park",
                    "Put a form on the council website",
                    "Ask councillors' neighbours"],
        "correct": "Post questionnaires to a random sample of households",
        "explanation": "<p><strong>Uy xoʻjaliklaridan tasodifiy "
                       "tanlanma.</strong></p>"
                       "<p>Parkdagilarni soʻrash — parkni yoqtiradiganlarni "
                       "soʻrash demakdir.</p>",
    },
    {
        "text": "<p>A poll of a random sample reports 51% support with a margin of error "
                "of 4%. Can the pollster say a majority supports the plan?</p>",
        "choices": ["No, because the range includes values below 50%",
                    "Yes, because 51% is above 50%",
                    "Yes, because the sample was random",
                    "No, because polls are never reliable"],
        "correct": "No, because the range includes values below 50%",
        "explanation": "<p><strong>Yoʻq.</strong> Oraliq 47% dan 55% gacha — "
                       "u 50 dan pastni ham qamraydi.</p>"
                       "<p>Xatolik chegarasi eʼtiborga olinmasa, xulosa "
                       "asossiz.</p>",
    },
    {
        "text": "<p>A factory tests every hundredth item coming off a line, choosing the "
                "starting item at random. Is this a reasonable sample?</p>",
        "choices": ["Yes, it gives every item a fair chance of being tested",
                    "No, because it is not exactly random",
                    "No, because the sample is too small",
                    "Yes, but only for the first hour"],
        "correct": "Yes, it gives every item a fair chance of being tested",
        "explanation": "<p><strong>Ha, oʻrinli.</strong> Boshlanish tasodifiy "
                       "boʻlgani uchun har bir buyum teng imkoniyatga "
                       "ega.</p>"
                       "<p>Bu «tizimli tanlanma» deyiladi va amalda keng "
                       "qoʻllaniladi.</p>",
    },
    {
        "text": "<p>Two polls of the same population report 40% and 46%, each with a "
                "margin of error of 2%. What can be concluded?</p>",
        "choices": ["The results genuinely differ, since the ranges do not overlap",
                    "The results agree",
                    "One poll must be wrong",
                    "Nothing can be concluded from two polls"],
        "correct": "The results genuinely differ, since the ranges do not overlap",
        "explanation": "<p><strong>Natijalar haqiqatan farq qiladi.</strong> "
                       "38–42 va 44–48 kesishmaydi.</p>"
                       "<p>Sabab boshqa boʻlishi mumkin — vaqt, savolning "
                       "shakli — lekin farqning oʻzi haqiqiy.</p>",
    },
]


# =====================================================================
# Testlar
# =====================================================================

PRACTICES = [
    {
        "title":       "SAT-56 Practice: Mode, Range, and Outliers",
        "description": "20 ta SAT uslubidagi savol — moda va oraliq, chetdagi qiymat "
                       "qaysi oʻlchovni buzishi va qaysinisiga tegmasligi.",
        "tutorial":    "SAT-56:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT56,
    },
    {
        "title":       "SAT-57 Practice: Standard Deviation — Measuring Data Spread",
        "description": "20 ta SAT uslubidagi savol — hisoblashsiz taqqoslash, siljish "
                       "va koʻpaytirishning taʼsiri, kontekstdagi maʼnosi.",
        "tutorial":    "SAT-57:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT57,
    },
    {
        "title":       "SAT-58 Practice: Probability — Simple and Independent Events",
        "description": "20 ta SAT uslubidagi savol — qulay ÷ jami, «yoki» va «va», "
                       "qaytarishli va qaytarishsiz tanlash.",
        "tutorial":    "SAT-58:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT58,
    },
    {
        "title":       "SAT-59 Practice: Conditional Probability from Two-Way Tables",
        "description": "20 ta SAT uslubidagi savol — «given that» maxrajni belgilaydi; "
                       "A|B va B|A farqi.",
        "tutorial":    "SAT-59:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT59,
    },
    {
        "title":       "SAT-60 Practice: Sample Surveys and Random Sampling",
        "description": "20 ta SAT uslubidagi savol — xulosa kimga tegishli, "
                       "tasodifiylik va hajm, xatolik chegarasi.",
        "tutorial":    "SAT-60:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT60,
    },
]
