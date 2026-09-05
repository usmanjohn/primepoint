# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-86 … SAT-90 (Blok E, ikkinchi yarmi).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.
⚠️ Javob har doim "correct" da va choices ning BIRINCHISIDA turadi.
⚠️ Blok E matematika oʻrgatmaydi — matematika ILGARIGI darslardan.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_86_90.py --master=prime \\
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
# SAT-86 — eyeballing diagrams
# =====================================================================

Q_SAT86 = [
    {
        "text": "<p>In a right triangle, one acute angle measures 30°. What is the "
                "measure of the other acute angle?</p>",
        "choices": ["60°", "30°", "90°", "120°"],
        "correct": "60°",
        "explanation": "<p><strong>60°.</strong> 180 − 90 − 30 = 60.</p>"
                       "<p><strong>120°</strong> — chizmaga bir marta qarash buni "
                       "rad etadi: burchak toʻgʻri burchakdan kichik.</p>",
    },
    {
        "text": "<p>A figure carries the note \"Figure not drawn to scale.\" What "
                "does that allow you to do?</p>",
        "choices": ["Trust only the labels, not the picture",
                    "Measure the picture with a ruler",
                    "Ignore the question's numbers",
                    "Assume all angles are right angles"],
        "correct": "Trust only the labels, not the picture",
        "explanation": "<p><strong>Faqat yorliqlarga ishoning.</strong> Bunday "
                       "chizma dalil emas, bezak.</p>",
    },
    {
        "text": "<p>A geometry figure carries no note about scale. Are its lengths "
                "drawn in proportion?</p>",
        "choices": ["Yes, SAT figures are to scale unless stated otherwise",
                    "No, figures are never to scale",
                    "Only the angles are to scale",
                    "Only if the question says they are"],
        "correct": "Yes, SAT figures are to scale unless stated otherwise",
        "explanation": "<p><strong>Ha.</strong> Bu testning oʻz qoidasi — shuning "
                       "uchun koʻz bilan chamalash mumkin.</p>",
    },
    {
        "text": "<p>Point <i>B</i> lies on segment <i>AC</i>, <i>AB</i> = 2 and "
                "<i>BC</i> = 6. What is <i>AC</i>? (Figure not drawn to scale.)</p>",
        "choices": ["8", "4", "12", "3"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> 2 + 6.</p>"
                       "<p><strong>4</strong> — chizmaga ishonib B oʻrta nuqta deb "
                       "olingan.</p>",
    },
    {
        "text": "<p>Point <i>B</i> lies on segment <i>AC</i>, <i>AB</i> = 5 and "
                "<i>BC</i> = 9. What is <i>AC</i>?</p>",
        "choices": ["14", "4", "45", "9"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> 5 + 9.</p>",
    },
    {
        "text": "<p>In a figure drawn to scale, an angle looks a little smaller than "
                "a right angle. Which measure is most likely?</p>",
        "choices": ["88°", "95°", "130°", "45°"],
        "correct": "88°",
        "explanation": "<p><strong>88°.</strong> 95 va 130 — 90 dan katta; 45 esa "
                       "«bir oz kichik» emas, ancha kichik.</p>",
    },
    {
        "text": "<p>In a right triangle, one acute angle measures 55°. What is the "
                "other?</p>",
        "choices": ["35°", "45°", "125°", "55°"],
        "correct": "35°",
        "explanation": "<p><strong>35°.</strong> 90 − 55.</p>",
    },
    {
        "text": "<p>In a figure drawn to scale, a rectangle's width is labelled 6 "
                "and its height looks about half the width. Which is the best "
                "estimate of the height?</p>",
        "choices": ["3", "6", "12", "1"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Maʼlum tomon lineyka boʻlib "
                       "xizmat qiladi: yarmi — 3.</p>",
    },
    {
        "text": "<p>What should eyeballing a diagram be used for?</p>",
        "choices": ["Eliminating impossible choices",
                    "Choosing the final answer directly",
                    "Replacing the calculation entirely",
                    "Deciding between 58° and 60°"],
        "correct": "Eliminating impossible choices",
        "explanation": "<p><strong>Oʻchirish uchun.</strong> Chamalash tanlash "
                       "uchun emas.</p>",
    },
    {
        "text": "<p>Two angles of a triangle measure 40° and 75°. What is the "
                "third?</p>",
        "choices": ["65°", "115°", "45°", "80°"],
        "correct": "65°",
        "explanation": "<p><strong>65°.</strong> 180 − 40 − 75.</p>"
                       "<p><strong>115°</strong> — dastlabki ikkitasi qoʻshilgan.</p>",
    },
    {
        "text": "<p>Two answer choices are 58° and 60°. Can eyeballing decide "
                "between them?</p>",
        "choices": ["No, the difference is too small to see",
                    "Yes, 60° always looks larger",
                    "Yes, if the figure is to scale",
                    "Only with a protractor"],
        "correct": "No, the difference is too small to see",
        "explanation": "<p><strong>Yoʻq.</strong> Koʻz «yarmi», «ikki barobar» "
                       "va «deyarli teng» dan nozikroq farqni ajratmaydi.</p>",
    },
    {
        "text": "<p>In a figure drawn to scale, one side looks about twice as long "
                "as a side labelled 5. What is the best estimate?</p>",
        "choices": ["10", "7", "2.5", "25"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> Ikki barobar — koʻz ishonchli "
                       "aytadigan uch xulosadan biri.</p>",
    },
    {
        "text": "<p>What is the first thing to read under a geometry figure?</p>",
        "choices": ["Whether it says \"not drawn to scale\"",
                    "The largest labelled number",
                    "The answer choices",
                    "The units"],
        "correct": "Whether it says \"not drawn to scale\"",
        "explanation": "<p><strong>Oʻsha yozuv.</strong> U butun strategiyani "
                       "yoqadi yoki oʻchiradi.</p>",
    },
    {
        "text": "<p>A figure not drawn to scale shows <i>B</i> between <i>A</i> and "
                "<i>C</i>, with <i>AB</i> = 3 and <i>BC</i> = 3. Is <i>B</i> the "
                "midpoint of <i>AC</i>?</p>",
        "choices": ["Yes, because the labels are equal",
                    "No, because the figure is not to scale",
                    "There is not enough information",
                    "Only if the figure shows it that way"],
        "correct": "Yes, because the labels are equal",
        "explanation": "<p><strong>Ha.</strong> Yorliqlar hukmron — ular teng "
                       "boʻlsa, B oʻrta nuqta, chizma qanday koʻrinishidan qatʼi "
                       "nazar.</p>",
    },
    {
        "text": "<p>A triangle's angles are labelled 30°, 60° and <i>x</i>°. What is "
                "<i>x</i>?</p>",
        "choices": ["90", "60", "30", "180"],
        "correct": "90",
        "explanation": "<p><strong>90.</strong> 180 − 30 − 60.</p>",
    },
    {
        "text": "<p>A triangle has sides of 5 and 9. Which length is impossible for "
                "the third side?</p>",
        "choices": ["3", "6", "10", "13"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Uchinchi tomon 4 bilan 14 orasida "
                       "boʻlishi kerak (SAT-73), va 3 bu oraliqdan tashqarida.</p>",
    },
    {
        "text": "<p>A shape is drawn entirely inside a 10-by-10 square. What can you "
                "say about its area?</p>",
        "choices": ["It is less than 100", "It is exactly 100",
                    "It is more than 100", "Nothing at all"],
        "correct": "It is less than 100",
        "explanation": "<p><strong>100 dan kichik.</strong> Bu chamalashning "
                       "uchinchi asbobi — shaklni oʻrab turgan "
                       "toʻrtburchak.</p>",
    },
    {
        "text": "<p>In a figure to scale, an angle clearly looks obtuse. Which choice "
                "can you drop?</p>",
        "choices": ["80°", "100°", "120°", "150°"],
        "correct": "80°",
        "explanation": "<p><strong>80°.</strong> U oʻtkir; qolgan uchtasi "
                       "90 dan katta.</p>",
    },
    {
        "text": "<p>An isosceles triangle has an apex angle of 40°. What does each "
                "base angle measure?</p>",
        "choices": ["70°", "40°", "140°", "50°"],
        "correct": "70°",
        "explanation": "<p><strong>70°.</strong> (180 − 40) ÷ 2.</p>"
                       "<p><strong>140°</strong> — ikkiga boʻlish "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>A figure drawn to scale shows a ladder leaning against a wall. "
                "The wall is 8 metres high and the ladder clearly reaches above the "
                "top of it. Which could be the ladder's length?</p>",
        "choices": ["10 metres", "6 metres", "7 metres", "4 metres"],
        "correct": "10 metres",
        "explanation": "<p><strong>10.</strong> Narvon devordan uzun — demak "
                       "8 dan katta boʻlishi shart, va faqat bitta variant "
                       "shunday.</p>",
    },
]


# =====================================================================
# SAT-87 — estimation
# =====================================================================

Q_SAT87 = [
    {
        "text": "<p>What is 19 percent of 412?</p>",
        "choices": ["78.28", "41.2", "8.24", "782.8"],
        "correct": "78.28",
        "explanation": "<p><strong>78.28.</strong> Chamalash: 400 ning beshdan "
                       "biri 80.</p>"
                       "<p><strong>41.2</strong> — bu 10 foiz.</p>",
    },
    {
        "text": "<p>What is 21 percent of 396?</p>",
        "choices": ["83.16", "39.6", "8.32", "79.2"],
        "correct": "83.16",
        "explanation": "<p><strong>83.16.</strong> Chamalash 20 foizi 400 dan = 80, "
                       "va javob undan sal katta boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Estimate 20 percent of 400.</p>",
        "choices": ["80", "20", "800", "40"],
        "correct": "80",
        "explanation": "<p><strong>80.</strong> 20 foiz — beshdan bir.</p>",
    },
    {
        "text": "<p>A jacket priced at $84 is on sale for 25 percent off. What is the "
                "sale price?</p>",
        "choices": ["$63", "$21", "$105", "$59"],
        "correct": "$63",
        "explanation": "<p><strong>$63.</strong> Chorak chegirma — toʻrtdan uchi "
                       "qoladi.</p>"
                       "<p><strong>$21</strong> — bu chegirmaning oʻzi.</p>",
    },
    {
        "text": "<p>A coat priced at $60 is reduced by 30 percent. What is the new "
                "price?</p>",
        "choices": ["$42", "$18", "$78", "$30"],
        "correct": "$42",
        "explanation": "<p><strong>$42.</strong> Chegirma 18, va 60 − 18 = 42.</p>"
                       "<p><strong>$18</strong> — chegirmaning oʻzi.</p>",
    },
    {
        "text": "<p>Between which two whole numbers does √50 lie?</p>",
        "choices": ["7 and 8", "6 and 7", "8 and 9", "24 and 26"],
        "correct": "7 and 8",
        "explanation": "<p><strong>7 va 8.</strong> 49 &lt; 50 &lt; 64.</p>",
    },
    {
        "text": "<p>Between which two whole numbers does √30 lie?</p>",
        "choices": ["5 and 6", "4 and 5", "6 and 7", "14 and 16"],
        "correct": "5 and 6",
        "explanation": "<p><strong>5 va 6.</strong> 25 &lt; 30 &lt; 36.</p>",
    },
    {
        "text": "<p>What is the average of 12, 15 and 48?</p>",
        "choices": ["25", "75", "15", "30"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> 75 ÷ 3.</p>"
                       "<p><strong>75</strong> — yigʻindining oʻzi.</p>",
    },
    {
        "text": "<p>Could the average of 4, 9 and 20 be 25?</p>",
        "choices": ["No, an average lies between the smallest and largest value",
                    "Yes, if the numbers are weighted",
                    "Yes, averages can exceed every value",
                    "There is not enough information"],
        "correct": "No, an average lies between the smallest and largest value",
        "explanation": "<p><strong>Yoʻq.</strong> Oʻrtacha 4 bilan 20 orasida "
                       "boʻlishi shart; u 11.</p>",
    },
    {
        "text": "<p>Which is closest to 38 × 21?</p>",
        "choices": ["800", "80", "8,000", "600"],
        "correct": "800",
        "explanation": "<p><strong>800.</strong> 40 × 20 = 800; aniq qiymat 798.</p>",
    },
    {
        "text": "<p>Which is closest to 612 ÷ 29?</p>",
        "choices": ["20", "2", "200", "60"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> 600 ÷ 30; aniq qiymat 21.1.</p>",
    },
    {
        "text": "<p>What is 10 percent of 730?</p>",
        "choices": ["73", "7.3", "730", "37"],
        "correct": "73",
        "explanation": "<p><strong>73.</strong> Vergulni bir xona chapga.</p>",
    },
    {
        "text": "<p>What is 25 percent of 88?</p>",
        "choices": ["22", "44", "66", "11"],
        "correct": "22",
        "explanation": "<p><strong>22.</strong> Toʻrtga boʻling.</p>"
                       "<p><strong>66</strong> — qolgan qism (75 foiz).</p>",
    },
    {
        "text": "<p>Which is closest to 3√3?</p>",
        "choices": ["5.2", "9", "3.5", "1.7"],
        "correct": "5.2",
        "explanation": "<p><strong>5.2.</strong> √3 ≈ 1.7, va 3 × 1.7 = 5.1.</p>"
                       "<p><strong>9</strong> — 3 × 3 hisoblangan, ildiz "
                       "eʼtiborsiz qoldirilgan.</p>",
    },
    {
        "text": "<p>Two answer choices are 4.71 and 4.79. Should you estimate?</p>",
        "choices": ["No, they are too close — compute exactly",
                    "Yes, estimation always works",
                    "Yes, round both to 5",
                    "Only if the question says approximately"],
        "correct": "No, they are too close — compute exactly",
        "explanation": "<p><strong>Yoʻq.</strong> Variantlarning farqi "
                       "chamalashning aniqligidan kichik.</p>",
    },
    {
        "text": "<p>Which value is impossible for a probability?</p>",
        "choices": ["1.4", "0", "0.5", "1"],
        "correct": "1.4",
        "explanation": "<p><strong>1.4.</strong> Ehtimollik 0 bilan 1 orasida "
                       "boʻladi — bu imkonsizlik nazorati.</p>",
    },
    {
        "text": "<p>What is a 15 percent tip on a bill of $40?</p>",
        "choices": ["$6", "$4", "$15", "$8"],
        "correct": "$6",
        "explanation": "<p><strong>$6.</strong> 10 foizi 4, yarmi yana 2, "
                       "jami 6.</p>",
    },
    {
        "text": "<p>Which is a reasonable estimate for 4.8 × 5.2?</p>",
        "choices": ["25", "10", "50", "2.5"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Ikkalasi ham 5 atrofida; aniq "
                       "qiymat 24.96.</p>",
    },
    {
        "text": "<p>What does the word \"approximately\" in a question signal?</p>",
        "choices": ["An estimate is acceptable",
                    "The answer must be a whole number",
                    "A calculator is forbidden",
                    "The figure is not to scale"],
        "correct": "An estimate is acceptable",
        "explanation": "<p><strong>Chamalash mumkin.</strong> Bu soʻz javobning "
                       "aniq boʻlishi shart emasligini aytadi.</p>",
    },
    {
        "text": "<p>A shop marks down a $250 coat by 40 percent. What is the sale "
                "price?</p>",
        "choices": ["$150", "$100", "$210", "$350"],
        "correct": "$150",
        "explanation": "<p><strong>$150.</strong> 60 foizi qoladi: 250 ning "
                       "yarmi 125, ustiga oʻndan biri 25.</p>"
                       "<p><strong>$100</strong> — chegirmaning oʻzi.</p>",
    },
]


# =====================================================================
# SAT-88 — time and guessing
# =====================================================================

Q_SAT88 = [
    {
        "text": "<p>A math module has 22 questions and 35 minutes. About how many "
                "seconds is that per question?</p>",
        "choices": ["95", "60", "120", "150"],
        "correct": "95",
        "explanation": "<p><strong>95.</strong> 2,100 soniya ÷ 22.</p>",
    },
    {
        "text": "<p>A student has 12 minutes left and 9 questions unanswered. On "
                "average, how many seconds per question?</p>",
        "choices": ["80", "95", "60", "108"],
        "correct": "80",
        "explanation": "<p><strong>80.</strong> 720 ÷ 9.</p>"
                       "<p><strong>95</strong> — bu umumiy oʻrtacha, qolgan vaqt "
                       "uchun emas.</p>",
    },
    {
        "text": "<p>A student has 6 minutes left and 4 questions. How many seconds "
                "each?</p>",
        "choices": ["90", "60", "120", "75"],
        "correct": "90",
        "explanation": "<p><strong>90.</strong> 360 ÷ 4.</p>",
    },
    {
        "text": "<p>A student has 10 minutes left and 8 questions. How many seconds "
                "each?</p>",
        "choices": ["75", "80", "90", "60"],
        "correct": "75",
        "explanation": "<p><strong>75.</strong> 600 ÷ 8.</p>",
    },
    {
        "text": "<p>On a four-choice question, a student eliminates two choices and "
                "then guesses. What is the probability of being correct?</p>",
        "choices": ["1/2", "1/4", "1/3", "0"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> Ikkita variant qoldi.</p>"
                       "<p><strong>1/4</strong> — oʻchirish hisobga "
                       "olinmagan.</p>",
    },
    {
        "text": "<p>A student eliminates one of four choices and guesses. What is the "
                "probability of being correct?</p>",
        "choices": ["1/3", "1/4", "1/2", "3/4"],
        "correct": "1/3",
        "explanation": "<p><strong>1/3.</strong> Uchta variant qoldi.</p>",
    },
    {
        "text": "<p>A student guesses on a four-choice question without eliminating "
                "anything. What is the probability of being correct?</p>",
        "choices": ["1/4", "1/2", "1/3", "1"],
        "correct": "1/4",
        "explanation": "<p><strong>1/4.</strong> Toʻrtta teng imkoniyat.</p>",
    },
    {
        "text": "<p>Should a student ever leave a question blank on the SAT?</p>",
        "choices": ["No, there is no penalty for a wrong answer",
                    "Yes, wrong answers lose a quarter point",
                    "Yes, if the question is very hard",
                    "Only on grid-in questions"],
        "correct": "No, there is no penalty for a wrong answer",
        "explanation": "<p><strong>Hech qachon.</strong> Jarima yoʻq, demak "
                       "boʻsh javobning qiymati nol.</p>",
    },
    {
        "text": "<p>How many questions are in one digital SAT math module?</p>",
        "choices": ["22", "20", "35", "44"],
        "correct": "22",
        "explanation": "<p><strong>22.</strong> Ikkita modul, jami 44 savol.</p>",
    },
    {
        "text": "<p>How many minutes are given for one math module?</p>",
        "choices": ["35", "22", "70", "45"],
        "correct": "35",
        "explanation": "<p><strong>35.</strong> Ikki modul — jami 70 daqiqa.</p>",
    },
    {
        "text": "<p>During the second module, can a student return to the first?</p>",
        "choices": ["No, a closed module cannot be reopened",
                    "Yes, at any time", "Yes, but only in the last minute",
                    "Only for marked questions"],
        "correct": "No, a closed module cannot be reopened",
        "explanation": "<p><strong>Yoʻq.</strong> Shuning uchun belgilab "
                       "qoldirishdan oldin bitta javob tanlang.</p>",
    },
    {
        "text": "<p>What determines the difficulty of the second math module?</p>",
        "choices": ["The student's performance on the first module",
                    "The test date", "The order the student answers in",
                    "Nothing — it is the same for everyone"],
        "correct": "The student's performance on the first module",
        "explanation": "<p><strong>Birinchi moduldagi natija.</strong> Test "
                       "moslashuvchi.</p>",
    },
    {
        "text": "<p>A question has already taken three minutes and is not finished. "
                "What is the best move?</p>",
        "choices": ["Mark an answer, flag it and move on",
                    "Keep working until it is solved",
                    "Leave it blank and move on",
                    "Skip the next two questions to save time"],
        "correct": "Mark an answer, flag it and move on",
        "explanation": "<p><strong>Javob belgilab, belgilab qoʻying.</strong> "
                       "Bitta qiyin savol ikkita osonini yeydi.</p>",
    },
    {
        "text": "<p>About what fraction of the math questions ask you to type your "
                "own answer?</p>",
        "choices": ["About a quarter", "About a half",
                    "About three quarters", "None"],
        "correct": "About a quarter",
        "explanation": "<p><strong>Taxminan chorak.</strong> Qolganlari "
                       "variantli.</p>",
    },
    {
        "text": "<p>With one minute left in a module, what should a student do?</p>",
        "choices": ["Fill in every blank answer",
                    "Recheck the first three questions",
                    "Solve the hardest remaining question",
                    "Nothing, to avoid mistakes"],
        "correct": "Fill in every blank answer",
        "explanation": "<p><strong>Boʻshlarni toʻldirish.</strong> Toʻrtta boʻsh "
                       "savolda bu oʻrtacha bitta toʻgʻri javob.</p>",
    },
    {
        "text": "<p>How many math questions are there in total on the digital SAT?</p>",
        "choices": ["44", "22", "35", "70"],
        "correct": "44",
        "explanation": "<p><strong>44.</strong> Ikkita modul, har birida 22.</p>",
    },
    {
        "text": "<p>How many minutes in total are given to the math section?</p>",
        "choices": ["70", "35", "44", "90"],
        "correct": "70",
        "explanation": "<p><strong>70.</strong> 35 + 35.</p>",
    },
    {
        "text": "<p>Which three tools are the cheapest way to eliminate a choice?</p>",
        "choices": ["Estimation, the figure, and an impossibility check",
                    "The reference sheet, Desmos, and the clock",
                    "Rereading, rewriting, and recalculating",
                    "Guessing, flagging, and skipping"],
        "correct": "Estimation, the figure, and an impossibility check",
        "explanation": "<p><strong>Chamalash, chizma, imkonsizlik "
                       "nazorati.</strong> Uchtasi ham 10 soniya oladi.</p>",
    },
    {
        "text": "<p>The second module feels easy. What does that tell the student?</p>",
        "choices": ["Nothing certain — difficulty is already built into the score",
                    "That they did badly in the first module",
                    "That they will score above 700",
                    "That the test is broken"],
        "correct": "Nothing certain — difficulty is already built into the score",
        "explanation": "<p><strong>Hech narsa aniq emas.</strong> Qiyinlik "
                       "darajasi ballga allaqachon kiritilgan — ruhingizni "
                       "tushirmang.</p>",
    },
    {
        "text": "<p>A student answers 12 questions in the first 20 minutes of a "
                "35-minute module. How many seconds are available for each of the "
                "10 remaining questions?</p>",
        "choices": ["90", "95", "75", "120"],
        "correct": "90",
        "explanation": "<p><strong>90.</strong> 15 daqiqa qoldi — 900 soniya, "
                       "va 900 ÷ 10 = 90.</p>"
                       "<p><strong>95</strong> — umumiy oʻrtacha; hisobni "
                       "qaytadan qilish kerak edi.</p>",
    },
]


# =====================================================================
# SAT-89 — trap answers
# =====================================================================

Q_SAT89 = [
    {
        "text": "<p>A rectangle's length is 4 more than its width and its perimeter "
                "is 36. What is the length?</p>",
        "choices": ["11", "7", "18", "36"],
        "correct": "11",
        "explanation": "<p><strong>11.</strong> En 7, uzunlik 11, perimetr 36 ✓</p>"
                       "<p><strong>7</strong> — bu en: birinchi tur tuzoq.</p>",
    },
    {
        "text": "<p>The same rectangle: length 4 more than width, perimeter 36. What "
                "is the width?</p>",
        "choices": ["7", "11", "9", "4"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Endi savol enni soʻrayapti — "
                       "oxirgi jumlani oʻqish shuning uchun kerak.</p>",
    },
    {
        "text": "<p>A train travels 150 kilometres in 90 minutes. What is its speed "
                "in kilometres per hour?</p>",
        "choices": ["100", "1.67", "135", "60"],
        "correct": "100",
        "explanation": "<p><strong>100.</strong> 90 daqiqa = 1.5 soat.</p>"
                       "<p><strong>1.67</strong> — 150 ÷ 90: birlik "
                       "oʻgirilmagan.</p>",
    },
    {
        "text": "<p>A car travels 120 kilometres in 90 minutes. What is its speed in "
                "kilometres per hour?</p>",
        "choices": ["80", "1.33", "180", "60"],
        "correct": "80",
        "explanation": "<p><strong>80.</strong> 120 ÷ 1.5.</p>",
    },
    {
        "text": "<p>You solve correctly for <i>x</i>, but the question asks for "
                "2<i>x</i>. Which trap is that?</p>",
        "choices": ["Answering a different question",
                    "Stopping halfway", "A sign error", "A unit error"],
        "correct": "Answering a different question",
        "explanation": "<p><strong>Birinchi tur.</strong> Masala toʻgʻri "
                       "yechilgan, notoʻgʻri son belgilangan.</p>",
    },
    {
        "text": "<p>You find that <i>r</i>² = 49 and enter 49. Which trap is that?</p>",
        "choices": ["Stopping halfway", "A unit error",
                    "Answering a different question", "The other root"],
        "correct": "Stopping halfway",
        "explanation": "<p><strong>Ikkinchi tur.</strong> Javob 7 — oxirgi qadam "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>What is the center of the circle "
                "(<i>x</i> − 3)² + (<i>y</i> + 2)² = 25?</p>",
        "choices": ["(3, −2)", "(−3, 2)", "(3, 2)", "(−3, −2)"],
        "correct": "(3, −2)",
        "explanation": "<p><strong>(3, −2).</strong> Ishorani agʻdaring — "
                       "uchinchi tur tuzoq shu yerda.</p>",
    },
    {
        "text": "<p>What is the radius of that same circle?</p>",
        "choices": ["5", "25", "√5", "12.5"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Oʻng tomonda r² turadi — ikkinchi "
                       "tur tuzoq.</p>",
    },
    {
        "text": "<p>Which single habit removes four of the seven trap types?</p>",
        "choices": ["Rereading the question's last line before marking",
                    "Using Desmos on every question",
                    "Answering the easiest questions first",
                    "Checking the reference sheet"],
        "correct": "Rereading the question's last line before marking",
        "explanation": "<p><strong>Oxirgi jumlani qayta oʻqish.</strong> Ikki "
                       "soniya oladi va toʻrtta tuzoqni yoʻq qiladi.</p>",
    },
    {
        "text": "<p>What is a wrong answer choice on the SAT usually made from?</p>",
        "choices": ["A common, predictable mistake",
                    "A randomly chosen number",
                    "The answer to a different test question",
                    "A number that cannot occur at all"],
        "correct": "A common, predictable mistake",
        "explanation": "<p><strong>Koʻp uchraydigan xato.</strong> Shuning uchun "
                       "ularni oʻrganish mumkin.</p>",
    },
    {
        "text": "<p>A student computes 150 ÷ 90 = 1.67 for a speed in kilometres per "
                "hour. What went wrong?</p>",
        "choices": ["Minutes were not converted to hours",
                    "The division was done backwards",
                    "The distance was wrong",
                    "The answer should be negative"],
        "correct": "Minutes were not converted to hours",
        "explanation": "<p><strong>Birlik.</strong> Javob kilometr/daqiqada "
                       "chiqdi.</p>",
    },
    {
        "text": "<p>Tickets cost $12 for adults and $7 for children. A group of 15 "
                "paid $145. How many children were there?</p>",
        "choices": ["7", "8", "9", "6"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Kattalar 8, bolalar 7. Bu safar "
                       "savol bolalarni soʻrayapti.</p>",
    },
    {
        "text": "<p>An equation has solutions −1 and 4. The question asks for the "
                "positive solution. What is the answer?</p>",
        "choices": ["4", "−1", "3", "5"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Beshinchi tur tuzoq — ikkinchi "
                       "ildiz ham haqiqiy, lekin soʻralmagan.</p>",
    },
    {
        "text": "<p>You work out that there were 8 adults in a group of 15. The "
                "question asks for the total number of people. What is the answer?</p>",
        "choices": ["15", "8", "7", "23"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> Bu son savolda berilgan edi — "
                       "hisoblash ham kerak emas.</p>",
    },
    {
        "text": "<p>The phrase \"the positive solution\" warns you about which trap?</p>",
        "choices": ["Choosing the other root", "A unit error",
                    "Stopping halfway", "A sign error in a formula"],
        "correct": "Choosing the other root",
        "explanation": "<p><strong>Ikkinchi ildiz.</strong> Ikkala yechim ham "
                       "toʻgʻri, faqat bittasi soʻralgan.</p>",
    },
    {
        "text": "<p>In a right triangle, cos <i>A</i> = 5/13. What is sin <i>A</i>?</p>",
        "choices": ["12/13", "8/13", "5/13", "13/12"],
        "correct": "12/13",
        "explanation": "<p><strong>12/13.</strong> 5-12-13 uchligi.</p>"
                       "<p><strong>8/13</strong> — 13 − 5 hisoblangan: yettinchi "
                       "tur, bitta ishonchli notoʻgʻri amal.</p>",
    },
    {
        "text": "<p>A rectangle is 7 by 11. What is its perimeter?</p>",
        "choices": ["36", "77", "18", "40"],
        "correct": "36",
        "explanation": "<p><strong>36.</strong> 2(7 + 11).</p>"
                       "<p><strong>77</strong> — bu yuza.</p>",
    },
    {
        "text": "<p>How many hours are 45 minutes?</p>",
        "choices": ["0.75", "0.45", "4.5", "1.45"],
        "correct": "0.75",
        "explanation": "<p><strong>0.75.</strong> 45 ÷ 60 — toʻrtinchi tur "
                       "tuzoqning oldini oladi.</p>",
    },
    {
        "text": "<p>A question asks for an amount in cents and you computed dollars. "
                "Which trap is that?</p>",
        "choices": ["A unit error", "Stopping halfway",
                    "The other root", "A sign error"],
        "correct": "A unit error",
        "explanation": "<p><strong>Toʻrtinchi tur.</strong> Javob toʻgʻri, "
                       "birligi notoʻgʻri.</p>",
    },
    {
        "text": "<p>A jacket costs $80 and is reduced by 25 percent. A student "
                "answers $20. Which trap is that?</p>",
        "choices": ["Giving the discount instead of the new price",
                    "A unit error", "A sign error", "Stopping at the wrong root"],
        "correct": "Giving the discount instead of the new price",
        "explanation": "<p><strong>Birinchi tur.</strong> $20 — chegirma; yangi "
                       "narx $60.</p>",
    },
]


# =====================================================================
# SAT-90 — grid-ins
# =====================================================================

Q_SAT90 = [
    {
        "text": "<p>A grid-in answer is two and a half. Which entry is "
                "acceptable?</p>",
        "choices": ["2.5", "2 1/2", "2½", "two and a half"],
        "correct": "2.5",
        "explanation": "<p><strong>2.5.</strong> 5/2 ham toʻgʻri boʻlar edi.</p>"
                       "<p><strong>2 1/2</strong> — qutida 21/2 boʻlib "
                       "oʻqiladi.</p>",
    },
    {
        "text": "<p>Which entry would the machine misread?</p>",
        "choices": ["2 1/2", "5/2", "2.5", "2.50"],
        "correct": "2 1/2",
        "explanation": "<p><strong>2 1/2.</strong> Boʻsh joy yoʻq, shuning uchun "
                       "u 21/2, yaʼni 10.5 boʻlib oʻqiladi.</p>",
    },
    {
        "text": "<p>How would you enter three quarters?</p>",
        "choices": ["3/4", "3 4", "0.7", "75%"],
        "correct": "3/4",
        "explanation": "<p><strong>3/4.</strong> .75 ham toʻgʻri; foiz belgisi "
                       "esa qabul qilinmaydi.</p>",
    },
    {
        "text": "<p>What is the safest entry for one third?</p>",
        "choices": ["1/3", "0.33", "0.3", "33%"],
        "correct": "1/3",
        "explanation": "<p><strong>1/3.</strong> Kasr yaxlitlash talab qilmaydi; "
                       "0.33 esa yetarlicha aniq emas.</p>",
    },
    {
        "text": "<p>How would you enter one thousand two hundred?</p>",
        "choices": ["1200", "1,200", "$1200", "1200.00"],
        "correct": "1200",
        "explanation": "<p><strong>1200.</strong> Vergul va dollar belgisi "
                       "yozilmaydi; 1200.00 esa yetti belgi.</p>",
    },
    {
        "text": "<p>Is 1,050 an acceptable grid-in entry?</p>",
        "choices": ["No, commas are not accepted",
                    "Yes, commas are required over 999",
                    "Yes, but only in the math section",
                    "No, the number is too large"],
        "correct": "No, commas are not accepted",
        "explanation": "<p><strong>Yoʻq.</strong> 1050 deb yoziladi.</p>",
    },
    {
        "text": "<p>How many characters may a positive grid-in answer use?</p>",
        "choices": ["5", "4", "6", "7"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Manfiy javobda oltitagacha.</p>",
    },
    {
        "text": "<p>How many characters may a negative grid-in answer use?</p>",
        "choices": ["6", "5", "7", "4"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Minus belgisi ham "
                       "hisoblanadi.</p>",
    },
    {
        "text": "<p>The answer to a question is twelve dollars. Which entry is "
                "acceptable?</p>",
        "choices": ["12", "$12", "12 dollars", "12.00$"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Faqat son — belgi ham, soʻz ham "
                       "yozilmaydi.</p>",
    },
    {
        "text": "<p>The answer to a question is fifty percent. Which entry is "
                "acceptable?</p>",
        "choices": ["50", "50%", "%50", "fifty"],
        "correct": "50",
        "explanation": "<p><strong>50.</strong> Foiz belgisi qabul "
                       "qilinmaydi.</p>",
    },
    {
        "text": "<p>Which decimal entry is acceptable for two thirds?</p>",
        "choices": [".6666", ".66", "0.6", ".7"],
        "correct": ".6666",
        "explanation": "<p><strong>.6666.</strong> Davriy son qutini toʻldirishi "
                       "kerak; 0.667 ham toʻgʻri.</p>",
    },
    {
        "text": "<p>Why is 0.66 not accepted as two thirds?</p>",
        "choices": ["It does not fill the box, so it is not accurate enough",
                    "Decimals are never accepted",
                    "It has too many characters",
                    "It should start with a comma"],
        "correct": "It does not fill the box, so it is not accurate enough",
        "explanation": "<p><strong>Qutini toʻldirmagan.</strong> Davriy sonda "
                       "joy borligicha yoziladi.</p>",
    },
    {
        "text": "<p>A question says more than one answer is possible. What should you "
                "enter?</p>",
        "choices": ["Only one of them", "Both, separated by a comma",
                    "The larger one only", "Both, separated by a space"],
        "correct": "Only one of them",
        "explanation": "<p><strong>Faqat bittasini.</strong> Ikkalasini yozish "
                       "javobni buzadi.</p>",
    },
    {
        "text": "<p>Written as the decimal 3.1428, how many characters does 22/7 "
                "use?</p>",
        "choices": ["6", "5", "4", "7"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Musbat javob uchun bu koʻp — "
                       "22/7 deb yozgan maʼqul.</p>",
    },
    {
        "text": "<p>Which uses fewer characters: 5/16 or .3125?</p>",
        "choices": ["5/16, with four", ".3125, with four",
                    "They are equal", "5/16, with three"],
        "correct": "5/16, with four",
        "explanation": "<p><strong>5/16 — toʻrtta belgi.</strong> .3125 esa "
                       "beshta.</p>",
    },
    {
        "text": "<p>About what fraction of the math questions are grid-ins?</p>",
        "choices": ["About a quarter", "About a half",
                    "About a tenth", "About three quarters"],
        "correct": "About a quarter",
        "explanation": "<p><strong>Taxminan chorak.</strong> Ularda variant "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>How many characters does the entry −3/4 use?</p>",
        "choices": ["4", "3", "5", "6"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Minus, 3, kesma, 4 — va manfiy "
                       "javobda oltitagacha ruxsat.</p>",
    },
    {
        "text": "<p>Why is 1200.00 not an acceptable entry?</p>",
        "choices": ["It uses seven characters", "Decimals are not allowed",
                    "It needs a comma", "It is not a whole number"],
        "correct": "It uses seven characters",
        "explanation": "<p><strong>Yetti belgi.</strong> Chegara beshta.</p>",
    },
    {
        "text": "<p>What is the safest general habit for grid-in answers?</p>",
        "choices": ["Enter a fraction rather than a rounded decimal",
                    "Always round to two decimal places",
                    "Always write the decimal form",
                    "Add a zero before every decimal point"],
        "correct": "Enter a fraction rather than a rounded decimal",
        "explanation": "<p><strong>Kasr yozing.</strong> U qisqaroq va "
                       "yaxlitlash talab qilmaydi.</p>",
    },
    {
        "text": "<p>An answer works out to seven eighths. Which entry uses the fewest "
                "characters?</p>",
        "choices": ["7/8", ".875", "0.875", "87.5"],
        "correct": "7/8",
        "explanation": "<p><strong>7/8 — uchta belgi.</strong> .875 toʻrtta, "
                       "0.875 beshta.</p>"
                       "<p><strong>87.5</strong> — bu foiz, kasr emas.</p>",
    },
]


PRACTICES = [
    {
        "title":       'SAT-86 Practice: The "Eyeballing" Strategy for Geometry Diagrams',
        "description": "20 ta SAT uslubidagi savol — chizmaga qachon ishonish mumkin, "
                       "maʼlum tomonni lineyka qilish va imkonsizni oʻchirish.",
        "tutorial":    "SAT-86:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT86,
    },
    {
        "title":       "SAT-87 Practice: The Art of Estimation",
        "description": "20 ta SAT uslubidagi savol — yaxlitlash, foizni kasrga "
                       "aylantirish, ildizni ikki son orasiga qoʻyish, imkonsizlik.",
        "tutorial":    "SAT-87:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT87,
    },
    {
        "title":       "SAT-88 Practice: Strategic Guessing and Time Management",
        "description": "20 ta SAT uslubidagi savol — 95 soniya, ikki oʻtish, "
                       "oʻchirish ehtimolliklari va testning oʻz raqamlari.",
        "tutorial":    "SAT-88:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT88,
    },
    {
        "title":       'SAT-89 Practice: Avoiding the "Trap Answers"',
        "description": "20 ta SAT uslubidagi savol — yettita tuzoq turini nom bilan "
                       "tanish va oxirgi jumlani qayta oʻqish odati.",
        "tutorial":    "SAT-89:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT89,
    },
    {
        "title":       "SAT-90 Practice: The Grid-In Blueprint (Student-Produced Responses)",
        "description": "20 ta SAT uslubidagi savol — belgilar soni, aralash son, "
                       "davriy oʻnli son va yozilmaydigan belgilar.",
        "tutorial":    "SAT-90:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT90,
    },
]
