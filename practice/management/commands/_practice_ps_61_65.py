# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-61 … SAT-65 (Blok C ning yakuni).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

⚠️ SAT-61 va SAT-62 da hisoblash deyarli yoʻq — faqat xulosaning oʻrinliligi.
⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_61_65.py --master=prime \\
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
# SAT-61 — selection bias
# =====================================================================

Q_SAT61 = [
    {
        "text": "<p>A survey is completed only by people who saw a poster in the school "
                "canteen. What type of bias is this?</p>",
        "choices": ["Self-selection", "Undercoverage", "Non-response", "No bias"],
        "correct": "Self-selection",
        "explanation": "<p><strong>Self-selection.</strong> Odamlar qatnashishni "
                       "oʻzlari tanlagan.</p>",
    },
    {
        "text": "<p>A town survey uses only the landline telephone directory. What type "
                "of bias is this?</p>",
        "choices": ["Undercoverage", "Self-selection", "Non-response", "No bias"],
        "correct": "Undercoverage",
        "explanation": "<p><strong>Undercoverage.</strong> Telefoni yoʻqlar "
                       "roʻyxatga umuman tushmagan.</p>",
    },
    {
        "text": "<p>A researcher interviews the first 25 people who walk past. What type "
                "of bias is this?</p>",
        "choices": ["Convenience", "Non-response", "Undercoverage", "No bias"],
        "correct": "Convenience",
        "explanation": "<p><strong>Convenience.</strong> Qulay boʻlgani uchun "
                       "tanlangan.</p>"
                       "<p>Oʻsha joyda, oʻsha vaqtda boʻlgan odamlar butun "
                       "guruhning vakili emas.</p>",
    },
    {
        "text": "<p>Questionnaires are sent to 2,000 people and 90 reply. What type of "
                "bias is the main concern?</p>",
        "choices": ["Non-response", "Undercoverage", "Convenience", "No bias"],
        "correct": "Non-response",
        "explanation": "<p><strong>Non-response.</strong> Javob berganlar — "
                       "javob berishni tanlaganlar.</p>"
                       "<p>Ular odatda mavzuga koʻproq qiziqadi.</p>",
    },
    {
        "text": "<p>Does increasing a biased sample from 1,000 to 20,000 reduce the "
                "bias?</p>",
        "choices": ["No — bias comes from how people were chosen",
                    "Yes, larger samples are less biased",
                    "Yes, if the increase is random",
                    "Only for surveys about opinions"],
        "correct": "No — bias comes from how people were chosen",
        "explanation": "<p><strong>Yoʻq.</strong> Ogʻish tanlash usulida, hajmda "
                       "emas.</p>"
                       "<p>Katta ogʻishgan tanlanma faqat ishonarliroq "
                       "koʻrinadi.</p>",
    },
    {
        "text": "<p>A random sample of one company's employees is surveyed. To whom do "
                "the results apply?</p>",
        "choices": ["That company's employees", "All employees in the industry",
                    "All working adults", "Only the people surveyed"],
        "correct": "That company's employees",
        "explanation": "<p><strong>Oʻsha kompaniya xodimlari.</strong> Tanlanma "
                       "shu guruhdan olingan.</p>"
                       "<p><strong>Only the people surveyed</strong> — juda "
                       "tor: tasodifiy tanlanma butun guruh haqida gapiradi.</p>",
    },
    {
        "text": "<p>A library asks visitors 'how often do you read?' and reports a very "
                "high figure. In which direction is the result biased?</p>",
        "choices": ["Too high, because library visitors read more than average",
                    "Too low", "Not biased", "It cannot be determined"],
        "correct": "Too high, because library visitors read more than average",
        "explanation": "<p><strong>Yuqoriga ogʻishgan.</strong> Kutubxonadagilar "
                       "allaqachon oʻqishni tanlagan odamlar.</p>",
    },
    {
        "text": "<p>A survey about public transport is conducted only among car owners. "
                "In which direction is support likely biased?</p>",
        "choices": ["Too low", "Too high", "Not biased", "It depends on the city"],
        "correct": "Too low",
        "explanation": "<p><strong>Pastga.</strong> Mashinasi borlar jamoat "
                       "transportiga kamroq muhtoj.</p>"
                       "<p>Ogʻishning <b>yoʻnalishini</b> aytish SAT'da "
                       "alohida savol turi.</p>",
    },
    {
        "text": "<p>Which change would most improve a survey with a low response "
                "rate?</p>",
        "choices": ["Follow up with those who did not reply",
                    "Send the questionnaire to more people",
                    "Shorten the questionnaire only",
                    "Report the results with a smaller margin of error"],
        "correct": "Follow up with those who did not reply",
        "explanation": "<p><strong>Javob bermaganlarni qayta soʻrash.</strong> "
                       "Bu ogʻishning oʻzagiga tegadi.</p>"
                       "<p>Koʻproq yuborish faqat koʻproq shunday odamni "
                       "keltiradi.</p>",
    },
    {
        "text": "<p>Which question is most likely to bias the answers?</p>",
        "choices": ["'Do you support the excellent new plan?'",
                    "'Do you support the new plan?'",
                    "'What is your view of the new plan?'",
                    "'Have you read about the new plan?'"],
        "correct": "'Do you support the excellent new plan?'",
        "explanation": "<p><strong>Birinchisi.</strong> «Excellent» soʻzi javobni "
                       "yoʻnaltiradi.</p>"
                       "<p>Bu «leading question» deyiladi.</p>",
    },
    {
        "text": "<p>A random sample of 500 is drawn from a list that omits everyone "
                "without an address. What is the problem?</p>",
        "choices": ["The list itself excludes part of the population",
                    "500 is too small",
                    "The selection was not random",
                    "There is no problem"],
        "correct": "The list itself excludes part of the population",
        "explanation": "<p><strong>Roʻyxatning oʻzi toʻliq emas.</strong> "
                       "Tanlash tasodifiy, lekin roʻyxat qamramagan.</p>"
                       "<p>Bu undercoverage — eng yashirin ogʻish turi.</p>",
    },
    {
        "text": "<p>What is the difference between bias and random error?</p>",
        "choices": ["Bias goes in one direction; random error goes both ways",
                    "Bias is smaller",
                    "Random error can be removed by a larger sample; bias cannot",
                    "Both A and C"],
        "correct": "Both A and C",
        "explanation": "<p><strong>Ikkalasi ham toʻgʻri.</strong> Ogʻish bir "
                       "yoʻnalishda va hajm bilan kamaymaydi.</p>"
                       "<p>Tasodifiy xato ikki tomonga ketadi va katta "
                       "tanlanmada kamayadi.</p>",
    },
    {
        "text": "<p>A study of a city's residents samples randomly from every "
                "neighbourhood. Why is this better than sampling from one "
                "neighbourhood?</p>",
        "choices": ["It covers the whole population, not one part of it",
                    "It is faster", "It gives a larger sample",
                    "It removes the margin of error"],
        "correct": "It covers the whole population, not one part of it",
        "explanation": "<p><strong>Butun aholi qamraladi.</strong> Bitta "
                       "mahalla shaharning vakili emas.</p>",
    },
    {
        "text": "<p>An online poll on a news website reports 78% agreement. What can be "
                "concluded?</p>",
        "choices": ["Only that 78% of those who chose to vote agreed",
                    "78% of the country agrees",
                    "78% of the website's readers agree",
                    "Nothing at all can be said"],
        "correct": "Only that 78% of those who chose to vote agreed",
        "explanation": "<p><strong>Faqat ovoz berganlar haqida.</strong> Ular "
                       "oʻzlarini tanlagan.</p>"
                       "<p>Hatto saytning barcha oʻquvchilari haqida ham "
                       "gapirib boʻlmaydi.</p>",
    },
    {
        "text": "<p>A student says a survey with 40,000 replies must be accurate. What "
                "is the flaw in this reasoning?</p>",
        "choices": ["Accuracy depends on how the sample was chosen, not its size",
                    "40,000 is not enough",
                    "Surveys are never accurate",
                    "There is no flaw"],
        "correct": "Accuracy depends on how the sample was chosen, not its size",
        "explanation": "<p><strong>Avval usul, keyin hajm.</strong></p>"
                       "<p>Bu SAT'ning eng koʻp takrorlanadigan Blok C "
                       "gʻoyasi.</p>",
    },
    {
        "text": "<p>A student says a random sample of one university means the results "
                "apply to all students nationally. What is the flaw?</p>",
        "choices": ["The sample came from one university only",
                    "The sample was random",
                    "Universities cannot be surveyed",
                    "There is no flaw"],
        "correct": "The sample came from one university only",
        "explanation": "<p><strong>Bitta universitetdan.</strong> Xulosa shu "
                       "universitet bilan chegaralanadi.</p>",
    },
    {
        "text": "<p>Researchers want to study exercise habits of a city. Which sampling "
                "plan is best?</p>",
        "choices": ["A random sample from the city's residence register",
                    "A survey at a running club",
                    "A survey outside a supermarket on Saturday",
                    "An advertisement asking for volunteers"],
        "correct": "A random sample from the city's residence register",
        "explanation": "<p><strong>Roʻyxatdan tasodifiy tanlanma.</strong> "
                       "Har bir aholi teng imkoniyatga ega.</p>"
                       "<p>Qolgan uchtasi maʼlum guruhga ogʻishgan.</p>",
    },
    {
        "text": "<p>A hospital surveys patients about waiting times, but only those who "
                "stayed until the end of their visit. In which direction is the result "
                "likely biased?</p>",
        "choices": ["Too positive, because those who left early are missing",
                    "Too negative", "Not biased", "It cannot be determined"],
        "correct": "Too positive, because those who left early are missing",
        "explanation": "<p><strong>Juda ijobiy tomonga.</strong> Eng koʻp "
                       "norozi boʻlganlar — ketib qolganlar.</p>"
                       "<p>Ular soʻrovga umuman tushmagan.</p>",
    },
    {
        "text": "<p>A shop wants to know why customers stopped coming. Surveying current "
                "customers has which problem?</p>",
        "choices": ["The people who left are exactly the ones missing",
                    "Current customers are too few",
                    "The question is too hard",
                    "There is no problem"],
        "correct": "The people who left are exactly the ones missing",
        "explanation": "<p><strong>Ketganlar tanlanmada yoʻq.</strong> Va "
                       "savolning butun mazmuni aynan ular haqida.</p>"
                       "<p>Bu survivorship deb ataladigan ogʻishning "
                       "koʻrinishi.</p>",
    },
    {
        "text": "<p>A government wants unemployment figures. Why is surveying only "
                "people at job centres a poor plan?</p>",
        "choices": ["It misses unemployed people who do not attend, and all employed people",
                    "Job centres are closed at weekends",
                    "The sample would be too large",
                    "Unemployment cannot be measured"],
        "correct": "It misses unemployed people who do not attend, and all employed people",
        "explanation": "<p><strong>Ikki tomondan ham qamramaydi.</strong> "
                       "Ishsizlarning bir qismi ham, ishlaydiganlar ham "
                       "tushmaydi.</p>"
                       "<p>Ishsizlik darajasini hisoblash uchun ikkala "
                       "guruh ham kerak.</p>",
    },
]


# =====================================================================
# SAT-62 — experimental design
# =====================================================================

Q_SAT62 = [
    {
        "text": "<p>Which type of randomisation allows a conclusion about cause and "
                "effect?</p>",
        "choices": ["Random assignment", "Random selection", "Both equally", "Neither"],
        "correct": "Random assignment",
        "explanation": "<p><strong>Tasodifiy taqsimlash.</strong> U guruhlarni "
                       "boshidanoq tenglashtiradi.</p>",
    },
    {
        "text": "<p>Which type of randomisation allows generalizing to a wider "
                "group?</p>",
        "choices": ["Random selection", "Random assignment", "Both equally", "Neither"],
        "correct": "Random selection",
        "explanation": "<p><strong>Tasodifiy tanlash.</strong> U tanlanmani "
                       "vakillik qiluvchi qiladi.</p>"
                       "<p>Ikki huquq alohida keladi.</p>",
    },
    {
        "text": "<p>Volunteers are randomly assigned to two groups in an experiment. "
                "What can be concluded?</p>",
        "choices": ["Cause, but only for people like these volunteers",
                    "Cause, for everyone",
                    "Association only",
                    "Nothing at all"],
        "correct": "Cause, but only for people like these volunteers",
        "explanation": "<p><strong>Sabab, lekin faqat shunday "
                       "koʻngillilar uchun.</strong></p>"
                       "<p>Taqsimlash bor, tanlash yoʻq.</p>",
    },
    {
        "text": "<p>A study compares people who already do yoga with people who do not. "
                "What kind of study is this?</p>",
        "choices": ["Observational", "An experiment", "A census", "A random trial"],
        "correct": "Observational",
        "explanation": "<p><strong>Kuzatuv tadqiqoti.</strong> Hech kim guruhga "
                       "taqsimlanmagan.</p>"
                       "<p>Shuning uchun sabab haqida xulosa "
                       "chiqarilmaydi.</p>",
    },
    {
        "text": "<p>A random sample of a city's residents is randomly assigned to two "
                "groups. What can be concluded?</p>",
        "choices": ["Cause, and for the whole city",
                    "Cause, but only for participants",
                    "Association, for the whole city",
                    "Nothing"],
        "correct": "Cause, and for the whole city",
        "explanation": "<p><strong>Ikkala huquq ham bor.</strong> Tasodifiy "
                       "tanlash va tasodifiy taqsimlash birga.</p>"
                       "<p>Bu eng kuchli tadqiqot turi.</p>",
    },
    {
        "text": "<p>Why is a control group used?</p>",
        "choices": ["To give something to compare the treatment group with",
                    "To increase the sample size",
                    "To make the study random",
                    "To reduce the margin of error"],
        "correct": "To give something to compare the treatment group with",
        "explanation": "<p><strong>Taqqoslash uchun.</strong> Usiz "
                       "«yaxshilandi» nimaga nisbatan ekani nomaʼlum.</p>",
    },
    {
        "text": "<p>Which word in a question tells you that cause may be "
                "concluded?</p>",
        "choices": ["'assigned'", "'chose'", "'observed'", "'reported'"],
        "correct": "'assigned'",
        "explanation": "<p><strong>«Assigned».</strong> Taqsimlash tadqiqotchi "
                       "tomonidan qilingan.</p>"
                       "<p>Qolgan uchtasi qatnashchining oʻz qarorini "
                       "bildiradi.</p>",
    },
    {
        "text": "<p>In an experiment, why should participants not know which group they "
                "are in?</p>",
        "choices": ["So their expectations do not affect the result",
                    "To keep the study secret",
                    "To make the sample larger",
                    "It does not matter"],
        "correct": "So their expectations do not affect the result",
        "explanation": "<p><strong>Kutish natijaga taʼsir qilmasligi "
                       "uchun.</strong></p>"
                       "<p>Odam «davolanyapman» deb bilsa, oʻzini yaxshi his "
                       "qilishi mumkin.</p>",
    },
    {
        "text": "<p>A study finds that students who attend extra classes score higher. "
                "The students chose whether to attend. What can be concluded?</p>",
        "choices": ["Attendance is associated with higher scores",
                    "Extra classes cause higher scores",
                    "Higher scores cause attendance",
                    "Nothing at all"],
        "correct": "Attendance is associated with higher scores",
        "explanation": "<p><strong>Faqat bogʻliqlik.</strong> Qatnashishni "
                       "tanlagan oʻquvchilar allaqachon boshqacha boʻlishi "
                       "mumkin.</p>",
    },
    {
        "text": "<p>Which is a confounding variable in a study of coffee drinking and "
                "heart disease?</p>",
        "choices": ["Smoking, if coffee drinkers smoke more",
                    "The number of participants",
                    "The brand of coffee",
                    "The length of the study"],
        "correct": "Smoking, if coffee drinkers smoke more",
        "explanation": "<p><strong>Chekish.</strong> U ikkala oʻzgaruvchiga ham "
                       "bogʻliq boʻlishi mumkin.</p>"
                       "<p>Chalkashtiruvchi omil — sababni yashiradigan "
                       "uchinchi narsa.</p>",
    },
    {
        "text": "<p>Which change would most improve a study in which participants chose "
                "their own group?</p>",
        "choices": ["Assign participants to groups at random",
                    "Increase the number of participants",
                    "Ask better questions",
                    "Run the study for longer"],
        "correct": "Assign participants to groups at random",
        "explanation": "<p><strong>Tasodifiy taqsimlash.</strong> Bu sababga "
                       "yoʻl ochadigan yagona oʻzgarish.</p>",
    },
    {
        "text": "<p>Can an experiment always be used instead of an observational "
                "study?</p>",
        "choices": ["No — some treatments cannot ethically be assigned",
                    "Yes, always",
                    "Yes, if the sample is large enough",
                    "No, because experiments are too expensive"],
        "correct": "No — some treatments cannot ethically be assigned",
        "explanation": "<p><strong>Yoʻq.</strong> Zararli narsani odamlarga "
                       "tasodifiy tayinlab boʻlmaydi.</p>"
                       "<p>Bunday hollarda faqat kuzatuv qoladi.</p>",
    },
    {
        "text": "<p>A study of a random sample of employees observes their sleep and "
                "productivity. What can be concluded?</p>",
        "choices": ["Association, and it applies to all the employees",
                    "Cause, for all employees",
                    "Cause, for participants only",
                    "Nothing"],
        "correct": "Association, and it applies to all the employees",
        "explanation": "<p><strong>Bogʻliqlik, butun guruhga.</strong> "
                       "Tanlash tasodifiy, taqsimlash yoʻq.</p>"
                       "<p>Bu jadvalning uchinchi qatori.</p>",
    },
    {
        "text": "<p>Two groups in an experiment each have 6 participants and show a "
                "difference. What is a reasonable concern?</p>",
        "choices": ["The groups are so small that chance could explain the difference",
                    "The study is invalid",
                    "The groups must be biased",
                    "There is no concern"],
        "correct": "The groups are so small that chance could explain the difference",
        "explanation": "<p><strong>Guruhlar juda kichik.</strong> Tasodif "
                       "farqni tushuntirishi mumkin.</p>"
                       "<p>Taqsimlash toʻgʻri boʻlsa ham, hajm yetarli "
                       "boʻlishi kerak.</p>",
    },
    {
        "text": "<p>A student concludes 'the treatment caused improvement' from a study "
                "where participants chose their group. What is wrong?</p>",
        "choices": ["Without random assignment, cause cannot be claimed",
                    "The sample was too small",
                    "The treatment was ineffective",
                    "Nothing is wrong"],
        "correct": "Without random assignment, cause cannot be claimed",
        "explanation": "<p><strong>Taqsimlash yoʻq.</strong> Guruhlar boshidanoq "
                       "farq qilgan boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>A student says a randomised experiment on volunteers proves the "
                "effect for everyone. What is wrong?</p>",
        "choices": ["The volunteers were not randomly selected from a wider group",
                    "Random assignment was missing",
                    "Volunteers cannot be studied",
                    "Nothing is wrong"],
        "correct": "The volunteers were not randomly selected from a wider group",
        "explanation": "<p><strong>Tasodifiy tanlash yoʻq.</strong> Sabab "
                       "haqida gapirish mumkin, umumlashtirish haqida "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>In a well-designed experiment, what should be the only systematic "
                "difference between the groups?</p>",
        "choices": ["The treatment being tested",
                    "The number of participants",
                    "The age of participants",
                    "The location of the study"],
        "correct": "The treatment being tested",
        "explanation": "<p><strong>Sinovdan oʻtayotgan taʼsir.</strong> "
                       "Qolgan hamma narsa oʻrtacha teng taqsimlangan "
                       "boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Why does random assignment tend to balance age, health and habits "
                "between groups?</p>",
        "choices": ["Because chance spreads all characteristics roughly evenly",
                    "Because researchers check each person",
                    "Because groups are matched by hand",
                    "It does not balance them"],
        "correct": "Because chance spreads all characteristics roughly evenly",
        "explanation": "<p><strong>Tasodif hamma xususiyatni taxminan teng "
                       "taqsimlaydi.</strong></p>"
                       "<p>Va bu tadqiqotchi bilmagan xususiyatlarga ham "
                       "tegishli — bu usulning eng kuchli tomoni.</p>",
    },
    {
        "text": "<p>A farm randomly assigns fields to two fertilisers and measures "
                "yield. The fields were all on one farm. What can be concluded?</p>",
        "choices": ["The fertiliser affected yield on those fields",
                    "The fertiliser affects yield on all farms",
                    "Only an association exists",
                    "Nothing"],
        "correct": "The fertiliser affected yield on those fields",
        "explanation": "<p><strong>Oʻsha dalalarda sabab.</strong> Taqsimlash "
                       "tasodifiy, lekin dalalar bitta fermadan.</p>"
                       "<p>Boshqa tuproq va iqlimga umumlashtirib "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p>A clinic randomly assigns a new exercise programme to half of a "
                "random sample of its patients. Six months later that group is "
                "healthier. What is the strongest appropriate conclusion?</p>",
        "choices": ["The programme improved health among this clinic's patients",
                    "The programme improves health for everyone",
                    "Healthier people joined the programme",
                    "Only an association can be claimed"],
        "correct": "The programme improved health among this clinic's patients",
        "explanation": "<p><strong>Shu shifoxona bemorlari uchun sabab.</strong> "
                       "Ikkala tasodifiylik ham bor, lekin tanlanma "
                       "shifoxonadan.</p>"
                       "<p>Bu jadvalning birinchi qatori — eng kuchli "
                       "xulosa, oʻz guruhi doirasida.</p>",
    },
]


# =====================================================================
# SAT-63 — margin of error
# =====================================================================

Q_SAT63 = [
    {
        "text": "<p>A poll reports 55% with a margin of error of 3%. What is the "
                "plausible range?</p>",
        "choices": ["52% to 58%", "55% to 58%", "52% to 55%", "49% to 61%"],
        "correct": "52% to 58%",
        "explanation": "<p><strong>52% dan 58% gacha.</strong> Ikkala tomonga "
                       "ham 3 dan.</p>",
    },
    {
        "text": "<p>A poll reports 27% with a margin of error of 1.5%. What is the "
                "plausible range?</p>",
        "choices": ["25.5% to 28.5%", "27% to 28.5%", "25.5% to 27%", "26% to 28%"],
        "correct": "25.5% to 28.5%",
        "explanation": "<p><strong>25.5% dan 28.5% gacha.</strong></p>"
                       "<p>Oraliqning kengligi 3 — chegaraning ikki "
                       "barobari.</p>",
    },
    {
        "text": "<p>An interval runs from 38% to 46%. What was the reported estimate?</p>",
        "choices": ["42%", "38%", "46%", "8%"],
        "correct": "42%",
        "explanation": "<p><strong>42%.</strong> Oraliqning oʻrtasi: "
                       "(38 + 46) ÷ 2.</p>",
    },
    {
        "text": "<p>An interval runs from 38% to 46%. What was the margin of error?</p>",
        "choices": ["4%", "8%", "42%", "2%"],
        "correct": "4%",
        "explanation": "<p><strong>4%.</strong> Kenglikning yarmi: 8 ÷ 2.</p>",
    },
    {
        "text": "<p>Which change is most likely to reduce the margin of error?</p>",
        "choices": ["Increasing the sample size", "Increasing the confidence level",
                    "Rewording the questions", "Repeating the study"],
        "correct": "Increasing the sample size",
        "explanation": "<p><strong>Tanlanma hajmini oshirish.</strong></p>"
                       "<p>Ishonch darajasini oshirish esa oraliqni "
                       "<b>kengaytiradi</b>.</p>",
    },
    {
        "text": "<p>Raising the confidence level from 95% to 99% does what to the "
                "interval?</p>",
        "choices": ["Widens it", "Narrows it", "Leaves it unchanged", "Removes it"],
        "correct": "Widens it",
        "explanation": "<p><strong>Kengaytiradi.</strong> Koʻproq ishonch uchun "
                       "koʻproq qiymatni qamrash kerak.</p>",
    },
    {
        "text": "<p>Two results are 41% ± 3 and 46% ± 3. Can a real difference be "
                "claimed?</p>",
        "choices": ["No, the intervals overlap", "Yes, 46 is greater than 41",
                    "Yes, the margins are equal", "It cannot be determined"],
        "correct": "No, the intervals overlap",
        "explanation": "<p><strong>Yoʻq.</strong> 38–44 va 43–49 kesishadi.</p>"
                       "<p>43 dan 44 gacha ikkalasiga ham tegishli.</p>",
    },
    {
        "text": "<p>Two results are 41% ± 2 and 48% ± 2. Can a real difference be "
                "claimed?</p>",
        "choices": ["Yes, the intervals do not overlap", "No, they overlap",
                    "Only if the samples are equal", "It cannot be determined"],
        "correct": "Yes, the intervals do not overlap",
        "explanation": "<p><strong>Ha.</strong> 39–43 va 46–50 kesishmaydi.</p>"
                       "<p>Ikki oraliq orasida boʻshliq bor — farq "
                       "haqiqiy.</p>",
    },
    {
        "text": "<p>A poll reports 51% support with a margin of error of 3%. Can a "
                "majority be claimed?</p>",
        "choices": ["No, the interval includes values below 50%",
                    "Yes, 51 is above 50",
                    "Yes, because the sample was random",
                    "Only at 99% confidence"],
        "correct": "No, the interval includes values below 50%",
        "explanation": "<p><strong>Yoʻq.</strong> Oraliq 48% dan 54% gacha.</p>"
                       "<p>Haqiqiy qiymat 50 dan past boʻlishi ham "
                       "mumkin.</p>",
    },
    {
        "text": "<p>Does a small margin of error mean the sample was well chosen?</p>",
        "choices": ["No, it only measures random variation",
                    "Yes, always", "Yes, if the sample was large",
                    "Only for surveys about opinions"],
        "correct": "No, it only measures random variation",
        "explanation": "<p><strong>Yoʻq.</strong> Chegara ogʻishni umuman "
                       "qamramaydi.</p>"
                       "<p>Ogʻishgan tanlanmada tor oraliq — xavf "
                       "belgisi.</p>",
    },
    {
        "text": "<p>A study reports a mean waiting time of 42 minutes with a margin of "
                "error of 5 minutes. What is the interval?</p>",
        "choices": ["37 to 47 minutes", "42 to 47 minutes", "37 to 42 minutes",
                    "40 to 44 minutes"],
        "correct": "37 to 47 minutes",
        "explanation": "<p><strong>37 dan 47 daqiqagacha.</strong></p>"
                       "<p>Chegara faqat foizda emas, har qanday birlikda "
                       "boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>What does '52% with a margin of error of 3%' mean about the 3?</p>",
        "choices": ["It is 3 percentage points, not 3% of 52",
                    "It is 3% of 52, which is about 1.56",
                    "It is 3 people",
                    "It is the confidence level"],
        "correct": "It is 3 percentage points, not 3% of 52",
        "explanation": "<p><strong>3 foiz punkti.</strong> Yaʼni 49 dan "
                       "55 gacha.</p>"
                       "<p>52 ning 3 foizi 1.56 boʻlardi — bu boshqa "
                       "narsa.</p>",
    },
    {
        "text": "<p>A student says the interval means the true value is definitely "
                "inside it. What is correct?</p>",
        "choices": ["It means the true value is likely inside it",
                    "The student is right",
                    "The true value is never inside it",
                    "The interval has no meaning"],
        "correct": "It means the true value is likely inside it",
        "explanation": "<p><strong>Ehtimoli katta.</strong> «Definitely» degan "
                       "soʻz SAT javoblarida deyarli har doim "
                       "notoʻgʻri.</p>",
    },
    {
        "text": "<p>A student adds the margin only to the upper end: 60% ± 4 becomes 60% "
                "to 64%. What is correct?</p>",
        "choices": ["56% to 64%", "60% to 64%", "56% to 60%", "58% to 62%"],
        "correct": "56% to 64%",
        "explanation": "<p><strong>56% dan 64% gacha.</strong> Chegara ikkala "
                       "tomonga ham qoʻllanadi.</p>",
    },
    {
        "text": "<p>Two polls of the same population report 35% ± 2 and 44% ± 2. What "
                "can be concluded?</p>",
        "choices": ["The difference is real, since 33–37 and 42–46 do not overlap",
                    "The difference is not real",
                    "One poll must be wrong",
                    "Nothing can be said"],
        "correct": "The difference is real, since 33–37 and 42–46 do not overlap",
        "explanation": "<p><strong>Farq haqiqiy.</strong> Oraliqlar "
                       "kesishmaydi.</p>"
                       "<p>Sabab boshqa boʻlishi mumkin — vaqt, savol "
                       "shakli — lekin farqning oʻzi bor.</p>",
    },
    {
        "text": "<p>Which sample size would give the smallest margin of error, all else "
                "equal?</p>",
        "choices": ["4,000", "400", "40", "It does not depend on sample size"],
        "correct": "4,000",
        "explanation": "<p><strong>4,000.</strong> Kattaroq tanlanma — kichikroq "
                       "chegara.</p>",
    },
    {
        "text": "<p>A margin of error is reported as 0%. What is most likely?</p>",
        "choices": ["Every member of the population was surveyed",
                    "The sample was very small",
                    "The poll is wrong",
                    "The confidence level was 100%"],
        "correct": "Every member of the population was surveyed",
        "explanation": "<p><strong>Butun aholi soʻralgan.</strong> Bu tanlanma "
                       "emas, toʻliq roʻyxat — census.</p>",
    },
    {
        "text": "<p>A pollster halves the margin of error. What roughly happened to the "
                "sample size?</p>",
        "choices": ["It grew several times larger", "It doubled",
                    "It halved", "It stayed the same"],
        "correct": "It grew several times larger",
        "explanation": "<p><strong>Bir necha barobar oshdi.</strong> Chegarani "
                       "ikki barobar kamaytirish uchun hajmni ikki "
                       "barobar oshirish yetmaydi.</p>"
                       "<p>SAT aniq nisbatni soʻramaydi, faqat "
                       "yoʻnalishni.</p>",
    },
    {
        "text": "<p>An election poll gives candidate A 49% ± 3 and candidate B 44% ± 3. "
                "A newspaper writes 'A leads'. Is that supported?</p>",
        "choices": ["No, the intervals 46–52 and 41–47 overlap",
                    "Yes, 49 is greater than 44",
                    "Yes, because A is above 45",
                    "It cannot be determined"],
        "correct": "No, the intervals 46–52 and 41–47 overlap",
        "explanation": "<p><strong>Asoslanmagan.</strong> 46 dan 47 gacha "
                       "ikkalasiga ham tegishli.</p>"
                       "<p>Gazetalar bu xatoni tez-tez qiladi.</p>",
    },
    {
        "text": "<p>A council reports that 62% of residents support a plan, margin of "
                "error 5%, based on a survey of volunteers who came to a meeting. What "
                "is the main problem?</p>",
        "choices": ["The margin of error does not cover the bias in who attended",
                    "The margin of error is too large",
                    "62% is too low to act on",
                    "There is no problem"],
        "correct": "The margin of error does not cover the bias in who attended",
        "explanation": "<p><strong>Chegara ogʻishni qamramaydi.</strong> "
                       "Yigʻilishga kelganlar oʻzlarini tanlagan.</p>"
                       "<p>Oraliq tor boʻlsa ham, u notoʻgʻri joyda "
                       "boʻlishi mumkin.</p>",
    },
]


# =====================================================================
# SAT-64 — boxplots and histograms
# =====================================================================
# Maʼlumot: 2, 4, 5, 7, 8, 10, 12, 15, 18, 30
# min 2 · Q1 5 · median 9 · Q3 15 · max 30 · IQR 10 · range 28

Q_SAT64 = [
    {
        "text": "<p>A boxplot has minimum 2, lower quartile 5, median 9, upper quartile "
                "15 and maximum 30. What is the interquartile range?</p>",
        "choices": ["10", "28", "9", "13"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 15 − 5.</p>"
                       "<p><strong>28</strong> — bu butun oraliq (30 − 2).</p>",
    },
    {
        "text": "<p>For that same boxplot, what is the range?</p>",
        "choices": ["28", "10", "30", "9"],
        "correct": "28",
        "explanation": "<p><strong>28.</strong> 30 − 2.</p>"
                       "<p>Oraliq moʻylovning chetidan chetigacha.</p>",
    },
    {
        "text": "<p>What fraction of the data lies inside the box of a boxplot?</p>",
        "choices": ["One half", "One quarter", "Three quarters", "All of it"],
        "correct": "One half",
        "explanation": "<p><strong>Yarmi.</strong> Quti pastki chorakdan yuqori "
                       "chorakgacha — oʻrtadagi 50 foiz.</p>",
    },
    {
        "text": "<p>What fraction of the data lies in each whisker?</p>",
        "choices": ["One quarter", "One half", "One eighth", "It varies"],
        "correct": "One quarter",
        "explanation": "<p><strong>Chorak qism.</strong> Toʻrtta qism bor va har "
                       "birida chorakdan.</p>",
    },
    {
        "text": "<p>One whisker of a boxplot is much longer than the other. What does "
                "this show?</p>",
        "choices": ["The values in that quarter are more spread out",
                    "There is more data in that quarter",
                    "The median is wrong",
                    "The box should be redrawn"],
        "correct": "The values in that quarter are more spread out",
        "explanation": "<p><strong>Oʻsha chorakda qiymatlar kengroq "
                       "tarqalgan.</strong></p>"
                       "<p>Miqdor har bir qismda bir xil — chorakdan.</p>",
    },
    {
        "text": "<p>A histogram has a long tail to the right. Which is greater?</p>",
        "choices": ["The mean", "The median", "They are equal",
                    "Neither can be found"],
        "correct": "The mean",
        "explanation": "<p><strong>Oʻrta arifmetik.</strong> U dum tomonga "
                       "tortiladi.</p>",
    },
    {
        "text": "<p>A histogram has a long tail to the left. Which is greater?</p>",
        "choices": ["The median", "The mean", "They are equal",
                    "Neither can be found"],
        "correct": "The median",
        "explanation": "<p><strong>Mediana.</strong> Oʻrtacha chapdagi dum "
                       "tomonga tortilgan.</p>",
    },
    {
        "text": "<p>A histogram is symmetric. What is true of the mean and median?</p>",
        "choices": ["They are approximately equal", "The mean is larger",
                    "The median is larger", "They cannot be compared"],
        "correct": "They are approximately equal",
        "explanation": "<p><strong>Taxminan teng.</strong> Hech qaysi tomonga "
                       "dum yoʻq.</p>",
    },
    {
        "text": "<p>Two boxplots look identical. Must the two data sets have the same "
                "number of values?</p>",
        "choices": ["No, a boxplot does not show how many values there are",
                    "Yes, always",
                    "Yes, if the medians match",
                    "Only if the ranges match"],
        "correct": "No, a boxplot does not show how many values there are",
        "explanation": "<p><strong>Yoʻq.</strong> Quti diagramma beshta sonni "
                       "koʻrsatadi, miqdorni emas.</p>",
    },
    {
        "text": "<p>Data set P has IQR 4 and data set Q has IQR 19. What does this "
                "tell you?</p>",
        "choices": ["Q's middle half is much more spread out",
                    "Q has more values",
                    "Q has a higher median",
                    "P has more outliers"],
        "correct": "Q's middle half is much more spread out",
        "explanation": "<p><strong>Q ning oʻrtadagi yarmi kengroq "
                       "tarqalgan.</strong></p>"
                       "<p>IQR markaz haqida ham, miqdor haqida ham hech "
                       "narsa aytmaydi.</p>",
    },
    {
        "text": "<p>Why is the IQR often preferred to the range?</p>",
        "choices": ["It is resistant to outliers",
                    "It is easier to compute",
                    "It uses every value",
                    "It is always larger"],
        "correct": "It is resistant to outliers",
        "explanation": "<p><strong>Chetdagi qiymatlarga chidamli.</strong> "
                       "U faqat oʻrtadagi yarimga qaraydi.</p>"
                       "<p>Oraliq esa butunlay ikki chekka qiymatdan "
                       "tuzilgan.</p>",
    },
    {
        "text": "<p>In a histogram, a bar labelled '20 to 30' has height 14. What does "
                "14 mean?</p>",
        "choices": ["14 values fall in that interval", "The value is 14",
                    "14 is the average", "14 intervals were used"],
        "correct": "14 values fall in that interval",
        "explanation": "<p><strong>Oʻsha oraliqqa 14 ta qiymat tushgan.</strong></p>"
                       "<p>Gistogramma oraliqlarni sanaydi, alohida "
                       "qiymatlarni emas.</p>",
    },
    {
        "text": "<p>For the data 3, 5, 6, 8, 9, 11, 14, 20, what is the median?</p>",
        "choices": ["8.5", "8", "9", "9.5"],
        "correct": "8.5",
        "explanation": "<p><strong>8.5.</strong> Sakkizta qiymat — oʻrtadagi "
                       "ikkitasi 8 va 9.</p>",
    },
    {
        "text": "<p>For that same data, what is the lower quartile?</p>",
        "choices": ["5.5", "5", "6", "8"],
        "correct": "5.5",
        "explanation": "<p><strong>5.5.</strong> Pastki toʻrttasi 3, 5, 6, 8 — "
                       "ularning medianasi (5 + 6) ÷ 2.</p>",
    },
    {
        "text": "<p>A student says the IQR of a boxplot with minimum 4 and maximum 40 is "
                "36. What is wrong?</p>",
        "choices": ["That is the range; the IQR uses the quartiles",
                    "The IQR is 40",
                    "The IQR cannot be found from a boxplot",
                    "Nothing is wrong"],
        "correct": "That is the range; the IQR uses the quartiles",
        "explanation": "<p><strong>Bu oraliq.</strong> IQR faqat qutining "
                       "kengligi.</p>",
    },
    {
        "text": "<p>A student says a long right whisker means most of the data is on the "
                "right. What is correct?</p>",
        "choices": ["Each whisker holds a quarter of the data, however long it is",
                    "The student is right",
                    "The whisker holds half the data",
                    "Whiskers hold no data"],
        "correct": "Each whisker holds a quarter of the data, however long it is",
        "explanation": "<p><strong>Har bir moʻylovda chorak qism.</strong> "
                       "Uzunlik tarqoqlikni bildiradi.</p>",
    },
    {
        "text": "<p>Two boxplots have the same median but one box is much wider. What "
                "differs?</p>",
        "choices": ["The spread of the middle half", "The centre",
                    "The number of values", "The maximum only"],
        "correct": "The spread of the middle half",
        "explanation": "<p><strong>Oʻrtadagi yarimning tarqalishi.</strong> "
                       "Markaz bir xil, IQR boshqa.</p>",
    },
    {
        "text": "<p>Salaries at a company are strongly skewed right. Which measure "
                "better describes a typical salary?</p>",
        "choices": ["The median", "The mean", "The range", "The maximum"],
        "correct": "The median",
        "explanation": "<p><strong>Mediana.</strong> Oʻngdagi dum oʻrta "
                       "arifmetikni yuqoriga tortadi.</p>"
                       "<p>Bu SAT-55 ning bevosita davomi.</p>",
    },
    {
        "text": "<p>Two classes take the same test. Class A's boxplot sits entirely to "
                "the right of class B's. What can be concluded?</p>",
        "choices": ["Every value in A is greater than every value in B",
                    "A's mean is greater but some B scores may be higher",
                    "The classes are the same size",
                    "Nothing can be concluded"],
        "correct": "Every value in A is greater than every value in B",
        "explanation": "<p><strong>A ning har bir qiymati B nikidan "
                       "katta.</strong> «Entirely to the right» — hatto A "
                       "ning eng kichigi ham B ning eng kattasidan "
                       "katta.</p>"
                       "<p>Bu juda kuchli shart, va u kamdan-kam "
                       "uchraydi.</p>",
    },
    {
        "text": "<p>A boxplot of delivery times has median 30 minutes, quartiles 25 and "
                "50, and maximum 180. What does the shape suggest?</p>",
        "choices": ["Most deliveries are quick, but a few are very slow",
                    "Most deliveries are slow",
                    "All deliveries take about 30 minutes",
                    "The data must be wrong"],
        "correct": "Most deliveries are quick, but a few are very slow",
        "explanation": "<p><strong>Koʻpchiligi tez, bir nechtasi juda "
                       "sekin.</strong> Quti tor (25 dan 50 gacha), oʻng "
                       "moʻylov esa 180 gacha choʻzilgan.</p>"
                       "<p>Bu oʻngga qiyshaygan maʼlumot.</p>",
    },
]


# =====================================================================
# SAT-65 — choosing a model from data
# =====================================================================

Q_SAT65 = [
    {
        "text": "<p>Values are 7, 11, 15, 19. Which model best fits?</p>",
        "choices": ["Linear, adding 4 each time", "Exponential, ratio 4",
                    "Exponential, ratio about 1.5", "Neither"],
        "correct": "Linear, adding 4 each time",
        "explanation": "<p><strong>Chiziqli.</strong> Ayirmalar 4, 4, 4.</p>",
    },
    {
        "text": "<p>Values are 3, 12, 48, 192. Which model best fits?</p>",
        "choices": ["Exponential, ratio 4", "Linear, adding 9 each time",
                    "Linear, adding 36 each time", "Neither"],
        "correct": "Exponential, ratio 4",
        "explanation": "<p><strong>Koʻrsatkichli, nisbat 4.</strong></p>"
                       "<p>Ayirmalar 9, 36, 144 — teng emas.</p>",
    },
    {
        "text": "<p>Values are 800, 720, 648, 583.2. Which model best fits?</p>",
        "choices": ["Exponential, ratio 0.9", "Linear, subtracting 80 each time",
                    "Exponential, ratio 0.1", "Neither"],
        "correct": "Exponential, ratio 0.9",
        "explanation": "<p><strong>Koʻrsatkichli, nisbat 0.9.</strong> Har "
                       "safar 10 foizdan tushadi.</p>"
                       "<p>Ayirmalar 80, 72, 64.8 — kichrayib boradi.</p>",
    },
    {
        "text": "<p>In real data, successive ratios are 1.97, 2.02 and 1.99. What does "
                "this suggest?</p>",
        "choices": ["An exponential model with a ratio of about 2",
                    "A linear model",
                    "No model fits",
                    "The data is wrong"],
        "correct": "An exponential model with a ratio of about 2",
        "explanation": "<p><strong>Koʻrsatkichli, nisbat taxminan 2.</strong></p>"
                       "<p>Haqiqiy maʼlumotda nisbatlar aynan teng "
                       "boʻlmaydi — yaqin boʻlishi yetarli.</p>",
    },
    {
        "text": "<p>Which is the correct order of checks when choosing a model from a "
                "table?</p>",
        "choices": ["Differences first, then ratios", "Ratios first, then differences",
                    "Only ratios", "Only differences"],
        "correct": "Differences first, then ratios",
        "explanation": "<p><strong>Avval ayirmalar, keyin nisbatlar.</strong></p>"
                       "<p>Ayirmalar teng boʻlsa javob tayyor — nisbatlarni "
                       "hisoblash shart emas.</p>",
    },
    {
        "text": "<p>A graph rises and becomes steeper and steeper. Which model is "
                "this?</p>",
        "choices": ["Exponential growth", "Linear growth",
                    "Exponential decay", "Linear decay"],
        "correct": "Exponential growth",
        "explanation": "<p><strong>Koʻrsatkichli oʻsish.</strong> Tiklik "
                       "ortib boradi.</p>"
                       "<p>Chiziqli grafik esa doim bir xil tiklikda.</p>",
    },
    {
        "text": "<p>A graph falls, gets flatter, and approaches but never reaches zero. "
                "Which model is this?</p>",
        "choices": ["Exponential decay", "Linear decay",
                    "Exponential growth", "Neither"],
        "correct": "Exponential decay",
        "explanation": "<p><strong>Koʻrsatkichli kamayish.</strong></p>"
                       "<p>Chiziqli kamayish nolni kesib oʻtib, manfiy "
                       "tomonga ketardi.</p>",
    },
    {
        "text": "<p>A model built from 8 hours of data is used to predict 3 months "
                "ahead. What is the concern?</p>",
        "choices": ["The prediction is far outside the range of the data",
                    "The model is a formula and cannot be used",
                    "The units are wrong",
                    "There is no concern"],
        "correct": "The prediction is far outside the range of the data",
        "explanation": "<p><strong>Maʼlumot oraliqidan juda uzoq.</strong> "
                       "Model u yerda tekshirilmagan.</p>",
    },
    {
        "text": "<p>A savings account pays a fixed percentage each year. Which model "
                "describes the balance?</p>",
        "choices": ["Exponential", "Linear", "Neither", "Both equally"],
        "correct": "Exponential",
        "explanation": "<p><strong>Koʻrsatkichli.</strong> Foiz — "
                       "koʻpaytirish.</p>",
    },
    {
        "text": "<p>A worker is paid a fixed amount per hour. Which model describes "
                "total pay?</p>",
        "choices": ["Linear", "Exponential", "Neither", "It depends on the hours"],
        "correct": "Linear",
        "explanation": "<p><strong>Chiziqli.</strong> Har soatga bir xil "
                       "miqdor qoʻshiladi.</p>",
    },
    {
        "text": "<p>Values at times 0, 1, 2, 3 are 50, 65, 84.5 and 109.85. What is the "
                "growth rate per period?</p>",
        "choices": ["30%", "15%", "65%", "It is linear"],
        "correct": "30%",
        "explanation": "<p><strong>30%.</strong> 65 ÷ 50 = 1.3 va "
                       "84.5 ÷ 65 = 1.3.</p>"
                       "<p><strong>15</strong> — birinchi ayirma, oʻsish "
                       "sur'ati emas.</p>",
    },
    {
        "text": "<p>A population model gives 5,000 at time zero and grows 4% a year. "
                "Which describes the yearly increase?</p>",
        "choices": ["It grows larger each year",
                    "It is 200 every year",
                    "It shrinks each year",
                    "It stays at 4 each year"],
        "correct": "It grows larger each year",
        "explanation": "<p><strong>Har yili kattalashadi.</strong> Birinchi yil "
                       "200, ikkinchi yil 208.</p>"
                       "<p>Foiz kattaroq summadan olinadi.</p>",
    },
    {
        "text": "<p>A linear model is fitted to data, and the residuals are positive at "
                "both ends and negative in the middle. What does this suggest?</p>",
        "choices": ["The data is curved, so a linear model is a poor choice",
                    "The model fits well",
                    "The data has an outlier",
                    "The residuals were computed wrongly"],
        "correct": "The data is curved, so a linear model is a poor choice",
        "explanation": "<p><strong>Maʼlumot egri.</strong> Qoldiqlarning "
                       "naqshi modelning notoʻgʻriligini koʻrsatadi.</p>"
                       "<p>Yaxshi moslashgan modelda qoldiqlar tasodifiy "
                       "tarqalgan boʻladi.</p>",
    },
    {
        "text": "<p>A quantity halves every 6 hours. After 24 hours, what fraction "
                "remains?</p>",
        "choices": ["1/16", "1/4", "1/8", "1/24"],
        "correct": "1/16",
        "explanation": "<p><strong>1/16.</strong> 24 ÷ 6 = 4 marta yarimlanadi.</p>"
                       "<p>1/2 toʻrt marta koʻpaytiriladi.</p>",
    },
    {
        "text": "<p>A student sees differences of 12, 12, 13 and calls the data "
                "exponential. What is correct?</p>",
        "choices": ["Linear — the differences are nearly constant",
                    "Exponential — the differences change",
                    "Neither model fits",
                    "More data is needed"],
        "correct": "Linear — the differences are nearly constant",
        "explanation": "<p><strong>Chiziqli.</strong> 12, 12, 13 — deyarli "
                       "teng.</p>"
                       "<p>Haqiqiy maʼlumotda kichik tebranish "
                       "normal.</p>",
    },
    {
        "text": "<p>A student says a model must work for all values because it is a "
                "formula. What is the flaw?</p>",
        "choices": ["A model is only supported over the range of its data",
                    "Formulas are unreliable",
                    "The formula must be wrong",
                    "There is no flaw"],
        "correct": "A model is only supported over the range of its data",
        "explanation": "<p><strong>Model faqat oʻz oraliqida "
                       "asoslangan.</strong></p>"
                       "<p>Formulaga istalgan sonni qoʻyish mumkin — javob "
                       "maʼnoli boʻlishi boshqa masala.</p>",
    },
    {
        "text": "<p>Values are 100, 150, 200, 250. A student says this is exponential "
                "because the values grow. What is correct?</p>",
        "choices": ["Linear — the differences are all 50",
                    "Exponential, ratio 1.5",
                    "Exponential, ratio 1.25",
                    "Neither"],
        "correct": "Linear — the differences are all 50",
        "explanation": "<p><strong>Chiziqli.</strong> Nisbatlar 1.5, 1.33, "
                       "1.25 — teng emas.</p>"
                       "<p>Oʻsish oʻz-oʻzidan koʻrsatkichlilikni "
                       "anglatmaydi.</p>",
    },
    {
        "text": "<p>A town's population is 12,000 and falls 3% a year. Which expression "
                "gives the population after <i>t</i> years?</p>",
        "choices": ["12,000(0.97)^t", "12,000(1.03)^t", "12,000 − 360t",
                    "12,000(0.03)^t"],
        "correct": "12,000(0.97)^t",
        "explanation": "<p><strong>12,000(0.97)^t.</strong> Har yili "
                       "97 foizi qoladi.</p>"
                       "<p><strong>12,000 − 360t</strong> chiziqli model "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>A phone's battery drops from 100% to 50% in one hour and to 25% in "
                "the next. Which model describes the charge?</p>",
        "choices": ["Exponential decay, halving each hour",
                    "Linear decay, losing 50 points each hour",
                    "Linear decay, losing 25 points each hour",
                    "Neither"],
        "correct": "Exponential decay, halving each hour",
        "explanation": "<p><strong>Koʻrsatkichli, har soatda yarimlanadi.</strong></p>"
                       "<p>Chiziqli boʻlganda ikkinchi soatda nolga "
                       "yetardi.</p>",
    },
    {
        "text": "<p>A shop's sales are 400, 480, 576 and 691 in four months. Which "
                "statement is best supported?</p>",
        "choices": ["Sales are growing by about 20% a month",
                    "Sales are growing by 80 a month",
                    "Sales are growing by 96 a month",
                    "Sales are falling"],
        "correct": "Sales are growing by about 20% a month",
        "explanation": "<p><strong>Oyiga taxminan 20 foiz.</strong> "
                       "480 ÷ 400 = 1.2 va 576 ÷ 480 = 1.2.</p>"
                       "<p>Ayirmalar 80, 96, 115 — oʻsib bormoqda, demak "
                       "chiziqli emas.</p>",
    },
]


# =====================================================================
# Testlar
# =====================================================================

PRACTICES = [
    {
        "title":       "SAT-61 Practice: Selection Bias and Generalizing Results",
        "description": "20 ta SAT uslubidagi savol — ogʻishning toʻrt turi, uning "
                       "yoʻnalishi va xulosaning chegarasi.",
        "tutorial":    "SAT-61:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT61,
    },
    {
        "title":       "SAT-62 Practice: Experimental Design — Random Assignment and Cause-and-Effect",
        "description": "20 ta SAT uslubidagi savol — tasodifiy taqsimlash va tanlash "
                       "ikki boshqa huquq beradi; nazorat guruhi va koʻr sinov.",
        "tutorial":    "SAT-62:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT62,
    },
    {
        "title":       "SAT-63 Practice: Margin of Error and Confidence Intervals",
        "description": "20 ta SAT uslubidagi savol — oraliqni ikki tomondan yozish, "
                       "kesishuv va chegara nimani qamramasligi.",
        "tutorial":    "SAT-63:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT63,
    },
    {
        "title":       "SAT-64 Practice: Comparing Data Sets — Boxplots and Histograms",
        "description": "20 ta SAT uslubidagi savol — beshta son, IQR va oraliq farqi, "
                       "qiyshiqlik va oʻrtacha-mediana bogʻliqligi.",
        "tutorial":    "SAT-64:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT64,
    },
    {
        "title":       "SAT-65 Practice: Linear vs. Exponential Data Modeling",
        "description": "20 ta SAT uslubidagi savol — avval ayirmalar keyin nisbatlar, "
                       "taxminiy maʼlumot va modelning chegarasi.",
        "tutorial":    "SAT-65:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT65,
    },
]
