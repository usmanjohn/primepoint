# -*- coding: utf-8 -*-
"""Prime English practices — PE-21 … PE-25.

Written with STYLE_GUIDE_PE_PRACTICE.md (see section 7: the pupils' own names —
Afsona, Jasur, Sherbek, Davron, Samandar, Iroda, Shaxzoda, Marjona, Madina, Charos,
Firdavs, Ilgʻor, Javohir, Sirojiddin, Behruz, Elbek, Abdulloh + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_21_25.py --master=prime
"""

SUBJECT = {
    "name":        "English",
    "description": "English grammar and vocabulary practice",
    "icon":        "bi-translate",
    "color":       "#6366f1",
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
# PE-21 — Past Simple: Irregular Verbs
# =====================================================================

Q_PE21 = [
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Yesterday Davron ___ to the bazaar with his father.</strong></p>",
        "choices": ["went", "goed", "gone", "goes"],
        "correct": "went",
        "explanation": "<p><strong>went</strong> is correct — <em>go</em> is irregular: "
                       "<em>go → went</em>, never <em>goed</em>.<br><br>"
                       "<em>(<strong>went</strong> toʻgʻri — <em>go</em> notoʻgʻri feʼl: "
                       "<em>go → went</em>, <em>goed</em> boʻlmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Marjona ___ a beautiful bird in the garden this morning.</strong></p>",
        "choices": ["saw", "seed", "seen", "sees"],
        "correct": "saw",
        "explanation": "<p><strong>saw</strong> is correct — <em>see → saw</em>. <em>Seen</em> is the "
                       "third form, which you will need later, not here.<br><br>"
                       "<em>(<strong>saw</strong> toʻgʻri — <em>see → saw</em>. <em>Seen</em> — uchinchi "
                       "shakl, u keyinroq kerak boʻladi, bu yerda emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Iroda ___ a new dictionary last week.</strong></p>",
        "choices": ["bought", "buyed", "buy", "boughted"],
        "correct": "bought",
        "explanation": "<p><strong>bought</strong> is correct — <em>buy → bought</em>, from the "
                       "<em>-ought / -aught</em> family: <em>bring → brought, think → thought, teach → "
                       "taught</em>.<br><br>"
                       "<em>(<strong>bought</strong> toʻgʻri — <em>buy → bought</em>, "
                       "<em>-ought / -aught</em> guruhidan: <em>bring → brought, think → thought, "
                       "teach → taught</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Rozimurod teacher ___ us a very difficult question.</strong></p>",
        "choices": ["asked", "asks", "asken", "did asked"],
        "correct": "asked",
        "explanation": "<p><strong>asked</strong> is correct — not every verb is irregular! "
                       "<em>Ask</em> is a normal regular verb, so it simply takes <em>-ed</em>.<br><br>"
                       "<em>(<strong>asked</strong> toʻgʻri — hamma feʼl notoʻgʻri emas! <em>Ask</em> "
                       "oddiy qoidali feʼl, shuning uchun shunchaki <em>-ed</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Behruz ___ his homework in twenty minutes.</strong></p>",
        "choices": ["did", "done", "doed", "does"],
        "correct": "did",
        "explanation": "<p><strong>did</strong> is correct — <em>do → did</em>. Here <em>did</em> is the "
                       "main verb, not a helper.<br><br>"
                       "<em>(<strong>did</strong> toʻgʻri — <em>do → did</em>. Bu yerda <em>did</em> "
                       "yordamchi emas, asosiy feʼl.)</em></p>",
    },
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Samandar ___ up at six o'clock and ___ breakfast.</strong></p>",
        "choices": ["got … had", "getted … haved", "got … has", "get … had"],
        "correct": "got … had",
        "explanation": "<p><strong>got … had</strong> is correct — <em>get → got</em>, "
                       "<em>have → had</em>. Both are irregular, and both are the same for every "
                       "person.<br><br>"
                       "<em>(<strong>got … had</strong> toʻgʻri — <em>get → got</em>, "
                       "<em>have → had</em>. Ikkisi ham notoʻgʻri feʼl va har bir shaxs uchun bir "
                       "xil.)</em></p>",
    },
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Charos ___ a long letter to her cousin in Nukus.</strong></p>",
        "choices": ["wrote", "writed", "written", "writes"],
        "correct": "wrote",
        "explanation": "<p><strong>wrote</strong> is correct — <em>write → wrote</em>, from the "
                       "<em>i → o</em> family: <em>drive → drove, ride → rode</em>.<br><br>"
                       "<em>(<strong>wrote</strong> toʻgʻri — <em>write → wrote</em>, <em>i → o</em> "
                       "guruhidan: <em>drive → drove, ride → rode</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Javohir ___ his lunch and ___ some tea.</strong></p>",
        "choices": ["ate … drank", "eated … drinked", "eaten … drunk", "eat … drank"],
        "correct": "ate … drank",
        "explanation": "<p><strong>ate … drank</strong> is correct — <em>eat → ate</em>, "
                       "<em>drink → drank</em>.<br><br>"
                       "<em>(<strong>ate … drank</strong> toʻgʻri — <em>eat → ate</em>, "
                       "<em>drink → drank</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Ilgʻor ___ me his new bicycle yesterday.</strong></p>",
        "choices": ["showed", "shew", "shown", "showd"],
        "correct": "showed",
        "explanation": "<p><strong>showed</strong> is correct. <em>Show</em> looks like it should be "
                       "irregular, but it is regular: <em>showed</em>.<br><br>"
                       "<em>(<strong>showed</strong> toʻgʻri. <em>Show</em> notoʻgʻriga oʻxshab "
                       "koʻrinadi, lekin qoidali feʼl: <em>showed</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Shaxzoda ___ her keys, so she waited outside.</strong></p>",
        "choices": ["lost", "losed", "lose", "loosed"],
        "correct": "lost",
        "explanation": "<p><strong>lost</strong> is correct — <em>lose → lost</em>, from the family that "
                       "ends in <em>-t</em>: <em>sleep → slept, keep → kept, feel → felt</em>.<br><br>"
                       "<em>(<strong>lost</strong> toʻgʻri — <em>lose → lost</em>, <em>-t</em> bilan "
                       "tugaydigan guruhdan: <em>sleep → slept, keep → kept, feel → felt</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Abdulloh ___ me about the test, so I studied all evening.</strong></p>",
        "choices": ["told", "telled", "said", "tolded"],
        "correct": "told",
        "explanation": "<p><strong>told</strong> is correct — <em>tell → told</em>. <em>Said</em> is also "
                       "a past form, but <em>say</em> does not take a person after it: <em>he told "
                       "me</em>, not <em>he said me</em>.<br><br>"
                       "<em>(<strong>told</strong> toʻgʻri — <em>tell → told</em>. <em>Said</em> ham "
                       "oʻtgan shakl, lekin <em>say</em> dan keyin shaxs kelmaydi: <em>he told me</em>, "
                       "<em>he said me</em> emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct past form.</p>"
                "<p><strong>Sirojiddin ___ very fast and won the race.</strong></p>",
        "choices": ["ran", "runned", "run", "runs"],
        "correct": "ran",
        "explanation": "<p><strong>ran</strong> is correct — <em>run → ran</em>, like "
                       "<em>swim → swam</em> and <em>begin → began</em>.<br><br>"
                       "<em>(<strong>ran</strong> toʻgʻri — <em>run → ran</em>, xuddi "
                       "<em>swim → swam</em> va <em>begin → began</em> kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which verb is <em>regular</em> (it takes -ed)?</strong></p>",
        "choices": ["visit", "come", "take", "give"],
        "correct": "visit",
        "explanation": "<p><strong>visit</strong> is correct — <em>visited</em>. The others change shape: "
                       "<em>came, took, gave</em>.<br><br>"
                       "<em>(<strong>visit</strong> toʻgʻri — <em>visited</em>. Qolganlari shaklini "
                       "oʻzgartiradi: <em>came, took, gave</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which verb does <em>not</em> change at all in the past?</strong></p>",
        "choices": ["cut", "sing", "sit", "speak"],
        "correct": "cut",
        "explanation": "<p><strong>cut</strong> is correct — <em>cut → cut</em>, like <em>put, let, "
                       "shut, cost</em>. Only the time words tell you it is the past.<br><br>"
                       "<em>(<strong>cut</strong> toʻgʻri — <em>cut → cut</em>, xuddi <em>put, let, "
                       "shut, cost</em> kabi. Oʻtgan zamon ekanini faqat vaqt soʻzlari "
                       "koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ that book last month. (read)</strong></p>",
        "choices": ["read", "readed", "red", "reads"],
        "correct": "read",
        "explanation": "<p><strong>read</strong> is correct — the spelling does not change, but the sound "
                       "does: present <em>/riːd/</em>, past <em>/red/</em>.<br><br>"
                       "<em>(<strong>read</strong> toʻgʻri — yozilishi oʻzgarmaydi, talaffuzi esa "
                       "oʻzgaradi: hozirgi zamon <em>/riːd/</em>, oʻtgan zamon <em>/red/</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Firdavs ___ the ball and Elbek ___ it.</strong></p>",
        "choices": ["threw … caught", "throwed … catched",
                    "thrown … caught", "threw … catched"],
        "correct": "threw … caught",
        "explanation": "<p><strong>threw … caught</strong> is correct — <em>throw → threw</em>, "
                       "<em>catch → caught</em>.<br><br>"
                       "<em>(<strong>threw … caught</strong> toʻgʻri — <em>throw → threw</em>, "
                       "<em>catch → caught</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Jasur goed to the stadium yesterday.",
                    "Jasur went to the stadium yesterday.",
                    "Jasur walked to the stadium yesterday.",
                    "Jasur was at the stadium yesterday."],
        "correct": "Jasur goed to the stadium yesterday.",
        "explanation": "<p><strong>Jasur goed to the stadium yesterday.</strong> is the mistake — "
                       "<em>go</em> is irregular, so no <em>-ed</em> may be added.<br><br>"
                       "<em>(<strong>Jasur goed to the stadium yesterday.</strong> xato — <em>go</em> "
                       "notoʻgʻri feʼl, shuning uchun unga <em>-ed</em> qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Afsona took her little brother to school.",
                    "Afsona taked her little brother to school.",
                    "Afsona taken her little brother to school.",
                    "Afsona did took her little brother to school."],
        "correct": "Afsona took her little brother to school.",
        "explanation": "<p><strong>Afsona took her little brother to school.</strong> is correct — "
                       "<em>take → took</em>, with no helper in a positive sentence.<br><br>"
                       "<em>(<strong>Afsona took her little brother to school.</strong> toʻgʻri — "
                       "<em>take → took</em>, tasdiq gapda yordamchi ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Where were you yesterday, Sherbek?</p>"
                "<p><strong>Sherbek:</strong> ___</p>",
        "choices": ["I went to Samarkand with my family.",
                    "I goed to Samarkand with my family.",
                    "I go to Samarkand with my family.",
                    "I was went to Samarkand with my family."],
        "correct": "I went to Samarkand with my family.",
        "explanation": "<p><strong>I went to Samarkand with my family.</strong> is correct — one past "
                       "form, no extra helper, no <em>was</em>.<br><br>"
                       "<em>(<strong>I went to Samarkand with my family.</strong> toʻgʻri — bitta oʻtgan "
                       "shakl, qoʻshimcha yordamchi ham, <em>was</em> ham kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> past form is correct.</p>",
        "choices": ["Iroda came home, made some tea and sat on the sofa.",
                    "Iroda comed home, maked some tea and sitted on the sofa.",
                    "Iroda came home, made some tea and sitted on the sofa.",
                    "Iroda come home, make some tea and sat on the sofa."],
        "correct": "Iroda came home, made some tea and sat on the sofa.",
        "explanation": "<p><strong>came … made … sat</strong> is correct — three irregular verbs, three "
                       "changed shapes, and no <em>-ed</em> anywhere.<br><br>"
                       "<em>(<strong>came … made … sat</strong> toʻgʻri — uchta notoʻgʻri feʼl, uchta "
                       "oʻzgargan shakl, hech qayerda <em>-ed</em> yoʻq.)</em></p>",
    },
]


# =====================================================================
# PE-22 — Past Simple: Negatives and Questions
# =====================================================================

Q_PE22 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona ___ come to school yesterday.</strong></p>",
        "choices": ["didn't", "doesn't", "wasn't", "don't"],
        "correct": "didn't",
        "explanation": "<p><strong>didn't</strong> is correct — the past has only one helper, "
                       "<em>did</em>, for every person.<br><br>"
                       "<em>(<strong>didn't</strong> toʻgʻri — oʻtgan zamonda har bir shaxs uchun bitta "
                       "yordamchi bor: <em>did</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you see Rozimurod teacher this morning?</strong></p>",
        "choices": ["Did", "Do", "Was", "Were"],
        "correct": "Did",
        "explanation": "<p><strong>Did</strong> is correct — questions about the past start with "
                       "<em>Did</em>, whatever the subject is.<br><br>"
                       "<em>(<strong>Did</strong> toʻgʻri — oʻtgan zamondagi savol, subject qanday "
                       "boʻlishidan qatʼi nazar, <em>Did</em> bilan boshlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Davron didn't ___ his homework last night.</strong></p>",
        "choices": ["do", "did", "does", "done"],
        "correct": "do",
        "explanation": "<p><strong>do</strong> is correct — <em>didn't</em> is already the past, so the "
                       "main verb goes back to its base form.<br><br>"
                       "<em>(<strong>do</strong> toʻgʻri — <em>didn't</em> allaqachon oʻtgan zamon, "
                       "shuning uchun asosiy feʼl asosiy shakliga qaytadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Did Charos ___ to the wedding?</strong></p>",
        "choices": ["go", "went", "goes", "gone"],
        "correct": "go",
        "explanation": "<p><strong>go</strong> is correct. This is the beautiful part: after <em>did</em> "
                       "even irregular verbs lose their special form.<br><br>"
                       "<em>(<strong>go</strong> toʻgʻri. Eng qulay tomoni shu: <em>did</em> dan keyin "
                       "hatto notoʻgʻri feʼllar ham maxsus shaklini yoʻqotadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ eat anything at breakfast.</strong></p>",
        "choices": ["didn't", "doesn't", "hadn't", "wasn't"],
        "correct": "didn't",
        "explanation": "<p><strong>didn't</strong> is correct — one past negative for everybody."
                       "<br><br><em>(<strong>didn't</strong> toʻgʻri — hamma uchun bitta oʻtgan zamon "
                       "inkori.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Did Behruz call you yesterday? — Yes, ___ .</strong></p>",
        "choices": ["he did", "he does", "he was", "he called"],
        "correct": "he did",
        "explanation": "<p><strong>he did</strong> is correct — the short answer repeats the helper, not "
                       "the main verb.<br><br>"
                       "<em>(<strong>he did</strong> toʻgʻri — qisqa javobda asosiy feʼl emas, yordamchi "
                       "takrorlanadi.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Did the girls finish the project? — No, ___ .</strong></p>",
        "choices": ["they didn't", "they don't", "they weren't", "they hadn't"],
        "correct": "they didn't",
        "explanation": "<p><strong>they didn't</strong> is correct — the same helper comes back in the "
                       "negative answer.<br><br>"
                       "<em>(<strong>they didn't</strong> toʻgʻri — inkor javobda oʻsha yordamchi qaytib "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Where ___ Shaxzoda buy that dress?</strong></p>",
        "choices": ["did", "does", "was", "do"],
        "correct": "did",
        "explanation": "<p><strong>did</strong> is correct — a wh- question in the past: "
                       "<em>Wh- + did + subject + base verb</em>.<br><br>"
                       "<em>(<strong>did</strong> toʻgʻri — oʻtgan zamondagi wh- savol: "
                       "<em>Wh- + did + subject + asosiy feʼl</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What time ___ the lesson finish yesterday?</strong></p>",
        "choices": ["did", "does", "was", "were"],
        "correct": "did",
        "explanation": "<p><strong>did</strong> is correct — <em>yesterday</em> makes it past, and "
                       "<em>finish</em> is an ordinary verb.<br><br>"
                       "<em>(<strong>did</strong> toʻgʻri — <em>yesterday</em> gapni oʻtgan zamonga "
                       "aylantiradi, <em>finish</em> esa oddiy feʼl.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ Iroda at home last night?</strong></p>",
        "choices": ["Was", "Did", "Does", "Had"],
        "correct": "Was",
        "explanation": "<p><strong>Was</strong> is correct — the first case where <em>did</em> must not "
                       "appear: with <em>to be</em>, the verb asks the question itself.<br><br>"
                       "<em>(<strong>Was</strong> toʻgʻri — <em>did</em> ishlatilmaydigan birinchi holat: "
                       "<em>to be</em> savolni oʻzi beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Who ___ the window? — Elbek did.</strong></p>",
        "choices": ["broke", "did break", "did broke", "was broke"],
        "correct": "broke",
        "explanation": "<p><strong>broke</strong> is correct — the second case where <em>did</em> "
                       "disappears: when <em>who</em> is the subject of the question.<br><br>"
                       "<em>(<strong>broke</strong> toʻgʻri — <em>did</em> tushib qoladigan ikkinchi "
                       "holat: <em>who</em> savolning subjecti boʻlganda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ his phone at home, so he couldn't call us.</strong></p>",
        "choices": ["left", "didn't left", "did left", "leaved"],
        "correct": "left",
        "explanation": "<p><strong>left</strong> is correct — this is a positive sentence, so the "
                       "irregular past form is used on its own, with no helper.<br><br>"
                       "<em>(<strong>left</strong> toʻgʻri — bu tasdiq gap, shuning uchun notoʻgʻri "
                       "feʼlning oʻtgan shakli yordamchisiz ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Javohir ___ the test, but he ___ the last question.</strong></p>",
        "choices": ["passed … didn't understand", "passed … didn't understood",
                    "did pass … not understood", "passed … don't understand"],
        "correct": "passed … didn't understand",
        "explanation": "<p><strong>passed … didn't understand</strong> is correct — <em>-ed</em> in the "
                       "positive half, base form after <em>didn't</em>.<br><br>"
                       "<em>(<strong>passed … didn't understand</strong> toʻgʻri — tasdiq qismida "
                       "<em>-ed</em>, <em>didn't</em> dan keyin esa asosiy shakl.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How many pupils ___ come to the club yesterday?</strong></p>",
        "choices": ["did", "does", "were", "was"],
        "correct": "did",
        "explanation": "<p><strong>did</strong> is correct — <em>come</em> is the main verb here, so the "
                       "helper is needed.<br><br>"
                       "<em>(<strong>did</strong> toʻgʻri — bu yerda asosiy feʼl <em>come</em>, shuning "
                       "uchun yordamchi kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Why ___ Sirojiddin leave so early?</strong></p>",
        "choices": ["did", "does", "was", "had"],
        "correct": "did",
        "explanation": "<p><strong>did</strong> is correct — a past wh- question with an ordinary "
                       "verb.<br><br>"
                       "<em>(<strong>did</strong> toʻgʻri — oddiy feʼl bilan oʻtgan zamon wh- "
                       "savoli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ her keys, but she found them later.</strong></p>",
        "choices": ["lost", "didn't lost", "did lost", "was lost"],
        "correct": "lost",
        "explanation": "<p><strong>lost</strong> is correct — positive sentence, so the irregular form "
                       "stands alone.<br><br>"
                       "<em>(<strong>lost</strong> toʻgʻri — tasdiq gap, shuning uchun notoʻgʻri shakl "
                       "yolgʻiz turadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Abdulloh didn't went to the lesson.", "Abdulloh didn't go to the lesson.",
                    "Abdulloh went to the lesson.", "Did Abdulloh go to the lesson?"],
        "correct": "Abdulloh didn't went to the lesson.",
        "explanation": "<p><strong>Abdulloh didn't went to the lesson.</strong> is the mistake — the past "
                       "is marked twice. <em>Didn't</em> already carries it, so say <em>didn't "
                       "go</em>.<br><br>"
                       "<em>(<strong>Abdulloh didn't went to the lesson.</strong> xato — oʻtgan zamon "
                       "ikki marta koʻrsatilgan. <em>Didn't</em> uni allaqachon bildiradi, shuning uchun "
                       "<em>didn't go</em> deyiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Did Ilgʻor finish his project?", "Did Ilgʻor finished his project?",
                    "Ilgʻor did finished his project?", "Was Ilgʻor finish his project?"],
        "correct": "Did Ilgʻor finish his project?",
        "explanation": "<p><strong>Did Ilgʻor finish his project?</strong> is correct — "
                       "<em>Did + subject + base verb</em>.<br><br>"
                       "<em>(<strong>Did Ilgʻor finish his project?</strong> toʻgʻri — "
                       "<em>Did + subject + asosiy feʼl</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> ___</p>"
                "<p><strong>Charos:</strong> No, I didn't. I forgot my notebook at home.</p>",
        "choices": ["Did you do the exercise, Charos?", "Do you did the exercise, Charos?",
                    "Did you did the exercise, Charos?", "Were you do the exercise, Charos?"],
        "correct": "Did you do the exercise, Charos?",
        "explanation": "<p><strong>Did you do the exercise, Charos?</strong> is correct — the answer "
                       "<em>No, I didn't</em> tells you the question began with <em>Did</em>.<br><br>"
                       "<em>(<strong>Did you do the exercise, Charos?</strong> toʻgʻri — <em>No, I "
                       "didn't</em> javobi savol <em>Did</em> bilan boshlanganini koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Jasur didn't come to school, so Rozimurod teacher asked me: "
                    "“Did he call you?”",
                    "Jasur didn't came to school, so Rozimurod teacher asked me: "
                    "“Did he called you?”",
                    "Jasur don't came to school, so Rozimurod teacher asked me: "
                    "“Was he call you?”",
                    "Jasur wasn't come to school, so Rozimurod teacher asked me: "
                    "“Did he calls you?”"],
        "correct": "Jasur didn't come to school, so Rozimurod teacher asked me: "
                   "“Did he call you?”",
        "explanation": "<p><strong>didn't come … Did he call …</strong> is correct — after "
                       "<em>didn't</em> and after <em>Did</em> the verb is always bare.<br><br>"
                       "<em>(<strong>didn't come … Did he call …</strong> toʻgʻri — <em>didn't</em> va "
                       "<em>Did</em> dan keyin feʼl doim oʻzgarmagan shaklda boʻladi.)</em></p>",
    },
]


# =====================================================================
# PE-23 — Past Continuous: The Interrupted Moment
# =====================================================================

Q_PE23 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>At nine o'clock last night I ___ my homework.</strong></p>",
        "choices": ["was doing", "did", "was do", "am doing"],
        "correct": "was doing",
        "explanation": "<p><strong>was doing</strong> is correct — the Past Continuous is "
                       "<em>was / were + verb-ing</em>, for an action in the middle of a past "
                       "moment.<br><br>"
                       "<em>(<strong>was doing</strong> toʻgʻri — Past Continuous "
                       "<em>was / were + feʼl-ing</em> shaklida boʻlib, oʻtgan bir daqiqada davom "
                       "etayotgan harakatni bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda and Madina ___ TV at eight o'clock.</strong></p>",
        "choices": ["were watching", "was watching", "watched", "were watch"],
        "correct": "were watching",
        "explanation": "<p><strong>were watching</strong> is correct — a plural subject takes "
                       "<em>were</em>.<br><br>"
                       "<em>(<strong>were watching</strong> toʻgʻri — koʻplikdagi subject <em>were</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What ___ you ___ at seven o'clock yesterday evening?</strong></p>",
        "choices": ["were … doing", "did … doing", "were … do", "was … doing"],
        "correct": "were … doing",
        "explanation": "<p><strong>were … doing</strong> is correct — this question asks what was "
                       "<em>in progress</em>, not what you did.<br><br>"
                       "<em>(<strong>were … doing</strong> toʻgʻri — bu savol nima "
                       "<em>davom etayotganini</em> soʻraydi, nima qilganingizni emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ football while his sister ___ the piano.</strong></p>",
        "choices": ["was playing … was practising", "played … practised",
                    "was playing … practised", "played … was practising"],
        "correct": "was playing … was practising",
        "explanation": "<p><strong>was playing … was practising</strong> is correct — two long actions "
                       "happening at the same time both take the Continuous.<br><br>"
                       "<em>(<strong>was playing … was practising</strong> toʻgʻri — bir vaqtda davom "
                       "etgan ikki uzoq harakat ikkisi ham Continuous da boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The sun ___ and the birds ___ when we left the house.</strong></p>",
        "choices": ["was shining … were singing", "shone … sang",
                    "was shining … sang", "shone … were singing"],
        "correct": "was shining … were singing",
        "explanation": "<p><strong>was shining … were singing</strong> is correct — this is the "
                       "background of a story, which is exactly what this tense paints.<br><br>"
                       "<em>(<strong>was shining … were singing</strong> toʻgʻri — bu hikoyaning fon "
                       "manzarasi, bu zamon aynan shuni chizadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Samandar ___ listening — he was looking out of the window.</strong></p>",
        "choices": ["wasn't", "didn't", "weren't", "isn't"],
        "correct": "wasn't",
        "explanation": "<p><strong>wasn't</strong> is correct — the first word is <em>to be</em>, so "
                       "<em>not</em> is simply added, with no <em>didn't</em>.<br><br>"
                       "<em>(<strong>wasn't</strong> toʻgʻri — birinchi soʻz <em>to be</em>, shuning "
                       "uchun shunchaki <em>not</em> qoʻshiladi, <em>didn't</em> kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ Marjona waiting for us at the gate?</strong></p>",
        "choices": ["Was", "Did", "Were", "Does"],
        "correct": "Was",
        "explanation": "<p><strong>Was</strong> is correct — one person, and <em>to be</em> moves to the "
                       "front by itself.<br><br>"
                       "<em>(<strong>Was</strong> toʻgʻri — bitta shaxs, <em>to be</em> esa oʻzi gap "
                       "boshiga chiqadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which time expression fits the Past Continuous best?</strong></p>",
        "choices": ["at five o'clock yesterday", "every day", "usually", "tomorrow morning"],
        "correct": "at five o'clock yesterday",
        "explanation": "<p><strong>at five o'clock yesterday</strong> is correct — this tense loves an "
                       "exact past moment: <em>at 5 o'clock, at that moment, all evening, "
                       "while …</em><br><br>"
                       "<em>(<strong>at five o'clock yesterday</strong> toʻgʻri — bu zamon aniq oʻtgan "
                       "daqiqani yaxshi koʻradi: <em>at 5 o'clock, at that moment, all evening, "
                       "while …</em>)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Ilgʻor ___ his bike when it started to rain.</strong></p>",
        "choices": ["was riding", "rode", "was ride", "rides"],
        "correct": "was riding",
        "explanation": "<p><strong>was riding</strong> is correct — the long action that the rain cut "
                       "into.<br><br>"
                       "<em>(<strong>was riding</strong> toʻgʻri — yomgʻir kesib oʻtgan uzoq "
                       "harakat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct -ing form.</p>"
                "<p><strong>Charos was ___ a letter to her cousin. (write)</strong></p>",
        "choices": ["writing", "writeing", "writting", "wrote"],
        "correct": "writing",
        "explanation": "<p><strong>writing</strong> is correct — the silent <em>-e</em> drops before "
                       "<em>-ing</em>.<br><br>"
                       "<em>(<strong>writing</strong> toʻgʻri — oʻqilmaydigan <em>-e</em> <em>-ing</em> "
                       "oldidan tushib qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs and Elbek ___ in the river all afternoon.</strong></p>",
        "choices": ["were swimming", "was swimming", "were swiming", "swam all"],
        "correct": "were swimming",
        "explanation": "<p><strong>were swimming</strong> is correct — plural <em>were</em>, and "
                       "<em>swim</em> doubles the <em>m</em>. <em>All afternoon</em> stresses the "
                       "length.<br><br>"
                       "<em>(<strong>were swimming</strong> toʻgʻri — koʻplik uchun <em>were</em>, "
                       "<em>swim</em> esa <em>m</em> ni ikkilaydi. <em>All afternoon</em> davomiylikni "
                       "taʼkidlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ the answer, so I put up my hand.</strong></p>",
        "choices": ["knew", "was knowing", "was know", "knowing"],
        "correct": "knew",
        "explanation": "<p><strong>knew</strong> is correct — <em>know</em> is a stative verb, so it "
                       "refuses <em>-ing</em> in the past too.<br><br>"
                       "<em>(<strong>knew</strong> toʻgʻri — <em>know</em> holat feʼli, shuning uchun "
                       "oʻtgan zamonda ham <em>-ing</em> ni qabul qilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin ___ the new bicycle very much.</strong></p>",
        "choices": ["liked", "was liking", "was like", "liking"],
        "correct": "liked",
        "explanation": "<p><strong>liked</strong> is correct — another stative verb: feelings and "
                       "opinions stay simple.<br><br>"
                       "<em>(<strong>liked</strong> toʻgʻri — yana bir holat feʼli: hissiyot va fikrlar "
                       "Simple da qoladi.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Were you sleeping when I called? — No, ___ .</strong></p>",
        "choices": ["I wasn't", "I didn't", "I weren't", "I am not"],
        "correct": "I wasn't",
        "explanation": "<p><strong>I wasn't</strong> is correct — the answer repeats <em>was / were</em>, "
                       "and <em>I</em> takes <em>was</em>.<br><br>"
                       "<em>(<strong>I wasn't</strong> toʻgʻri — javobda <em>was / were</em> "
                       "takrorlanadi, <em>I</em> esa <em>was</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>When Rozimurod teacher came in, the pupils ___ .</strong></p>",
        "choices": ["were talking loudly", "talked loudly", "was talking loudly", "talk loudly"],
        "correct": "were talking loudly",
        "explanation": "<p><strong>were talking loudly</strong> is correct — the talking was already in "
                       "progress before he came in.<br><br>"
                       "<em>(<strong>were talking loudly</strong> toʻgʻri — oʻqituvchi kirgunga qadar "
                       "suhbat allaqachon davom etayotgan edi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Shaxzoda ___ tired because she ___ all night.</strong></p>",
        "choices": ["was … had been studying", "was … was studying",
                    "were … was studying", "was … studied all"],
        "correct": "was … was studying",
        "explanation": "<p><strong>was … was studying</strong> is correct at this level — a state "
                       "(<em>was tired</em>) plus a long action across the night.<br><br>"
                       "<em>(<strong>was … was studying</strong> bu darajada toʻgʻri — holat "
                       "(<em>was tired</em>) va tun boʻyi davom etgan uzoq harakat.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Javohir didn't watching TV at that time.",
                    "Javohir wasn't watching TV at that time.",
                    "Javohir was watching TV at that time.",
                    "Was Javohir watching TV at that time?"],
        "correct": "Javohir didn't watching TV at that time.",
        "explanation": "<p><strong>Javohir didn't watching TV at that time.</strong> is the mistake — "
                       "<em>didn't</em> and <em>-ing</em> never work together. Use <em>wasn't "
                       "watching</em>.<br><br>"
                       "<em>(<strong>Javohir didn't watching TV at that time.</strong> xato — "
                       "<em>didn't</em> va <em>-ing</em> birga ishlamaydi. <em>Wasn't watching</em> "
                       "deyiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["The children were playing in the yard.", "The children was playing in the yard.",
                    "The children were play in the yard.", "The children playing in the yard."],
        "correct": "The children were playing in the yard.",
        "explanation": "<p><strong>The children were playing in the yard.</strong> is correct — "
                       "<em>children</em> is plural, so <em>were</em>, and both pieces are present."
                       "<br><br><em>(<strong>The children were playing in the yard.</strong> toʻgʻri — "
                       "<em>children</em> koʻplikda, shuning uchun <em>were</em>, va ikki boʻlak ham oʻz "
                       "oʻrnida.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Abdulloh:</strong> Why didn't you answer your phone?</p>"
                "<p><strong>Afsona:</strong> Sorry, ___</p>",
        "choices": ["I was helping my mother in the kitchen.",
                    "I helped my mother in the kitchen at that moment.",
                    "I was help my mother in the kitchen.",
                    "I did helping my mother in the kitchen."],
        "correct": "I was helping my mother in the kitchen.",
        "explanation": "<p><strong>I was helping my mother in the kitchen.</strong> is correct — an "
                       "action in progress at that moment, which is why she missed the call.<br><br>"
                       "<em>(<strong>I was helping my mother in the kitchen.</strong> toʻgʻri — oʻsha "
                       "daqiqada davom etayotgan harakat, shuning uchun qoʻngʻiroqni "
                       "oʻtkazib yubordi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> verb is correct.</p>",
        "choices": ["At six o'clock Madina was cooking, Davron was washing the car "
                    "and I was reading.",
                    "At six o'clock Madina cooked, Davron was wash the car and I reading.",
                    "At six o'clock Madina was cooking, Davron were washing the car "
                    "and I were reading.",
                    "At six o'clock Madina was cook, Davron was washing the car and I was read."],
        "correct": "At six o'clock Madina was cooking, Davron was washing the car "
                   "and I was reading.",
        "explanation": "<p><strong>was cooking … was washing … was reading</strong> is correct — three "
                       "parallel actions at one past moment, each with its own <em>was</em> and "
                       "<em>-ing</em>.<br><br>"
                       "<em>(<strong>was cooking … was washing … was reading</strong> toʻgʻri — oʻtgan "
                       "bir daqiqadagi uchta parallel harakat, har biri oʻz <em>was</em> va <em>-ing</em> "
                       "i bilan.)</em></p>",
    },
]


# =====================================================================
# PE-24 — Past Simple vs Past Continuous: when and while
# =====================================================================

Q_PE24 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ home when I met Rozimurod teacher.</strong></p>",
        "choices": ["was walking", "walked", "was walk", "walk"],
        "correct": "was walking",
        "explanation": "<p><strong>was walking</strong> is correct — walking home was the long "
                       "background action; meeting the teacher was the short event inside it.<br><br>"
                       "<em>(<strong>was walking</strong> toʻgʻri — uyga ketish — uzoq fon harakati, "
                       "oʻqituvchini uchratish esa uning ichidagi qisqa voqea.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda was cooking dinner when the lights ___ out.</strong></p>",
        "choices": ["went", "were going", "go", "was going"],
        "correct": "went",
        "explanation": "<p><strong>went</strong> is correct — the lights went out in one second: short "
                       "action → Past Simple.<br><br>"
                       "<em>(<strong>went</strong> toʻgʻri — chiroq bir soniyada oʻchdi: qisqa harakat → "
                       "Past Simple.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which tense marks the <em>long</em> action?</strong></p>",
        "choices": ["Past Continuous", "Past Simple", "Present Simple", "Present Continuous"],
        "correct": "Past Continuous",
        "explanation": "<p><strong>Past Continuous</strong> is correct — the band is the long background; "
                       "the Past Simple dot is the short interruption.<br><br>"
                       "<em>(<strong>Past Continuous</strong> toʻgʻri — “tasma” uzoq fon, Past Simple "
                       "“nuqtasi” esa qisqa uzilish.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>While Samandar ___ his homework, his little brother broke his "
                "pencil.</strong></p>",
        "choices": ["was doing", "did", "does", "was do"],
        "correct": "was doing",
        "explanation": "<p><strong>was doing</strong> is correct — <em>while</em> almost always "
                       "introduces the long action, so the Continuous follows it.<br><br>"
                       "<em>(<strong>was doing</strong> toʻgʻri — <em>while</em> deyarli doim uzoq "
                       "harakatni kiritadi, shuning uchun undan keyin Continuous keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>When the bell ___ , we were still writing.</strong></p>",
        "choices": ["rang", "was ringing", "rings", "ring"],
        "correct": "rang",
        "explanation": "<p><strong>rang</strong> is correct — <em>when</em> usually introduces the short "
                       "action, so the Past Simple follows it.<br><br>"
                       "<em>(<strong>rang</strong> toʻgʻri — <em>when</em> odatda qisqa harakatni "
                       "kiritadi, shuning uchun undan keyin Past Simple keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Marjona ___ her arm while she ___ volleyball.</strong></p>",
        "choices": ["hurt … was playing", "was hurting … played",
                    "hurt … played", "was hurting … was playing"],
        "correct": "hurt … was playing",
        "explanation": "<p><strong>hurt … was playing</strong> is correct — the injury happened in a "
                       "second, the game lasted a long time.<br><br>"
                       "<em>(<strong>hurt … was playing</strong> toʻgʻri — jarohat bir soniyada sodir "
                       "boʻldi, oʻyin esa uzoq davom etdi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>While I ___ the dishes, my phone ___ .</strong></p>",
        "choices": ["was washing … rang", "washed … was ringing",
                    "was washing … was ringing", "washed … rang"],
        "correct": "was washing … rang",
        "explanation": "<p><strong>was washing … rang</strong> is correct — long action after "
                       "<em>while</em>, short event as the interruption.<br><br>"
                       "<em>(<strong>was washing … rang</strong> toʻgʻri — <em>while</em> dan keyin uzoq "
                       "harakat, uzilish esa qisqa voqea.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ his bag, ___ goodbye and left the classroom.</strong></p>",
        "choices": ["took … said", "was taking … was saying",
                    "took … was saying", "was taking … said"],
        "correct": "took … said",
        "explanation": "<p><strong>took … said</strong> is correct. When several short actions happen one "
                       "after another, they are all Past Simple — no interruption here.<br><br>"
                       "<em>(<strong>took … said</strong> toʻgʻri. Bir necha qisqa harakat ketma-ket "
                       "sodir boʻlsa, hammasi Past Simple da boʻladi — bu yerda uzilish "
                       "yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “When Charos came in, Madina was reading” mean?</strong></p>",
        "choices": ["Madina started reading before Charos came in.",
                    "Madina started reading after Charos came in.",
                    "They started at exactly the same time.",
                    "Madina did not read at all."],
        "correct": "Madina started reading before Charos came in.",
        "explanation": "<p><strong>Madina started reading before Charos came in.</strong> is correct — "
                       "the Continuous action was already in progress. If we said <em>Madina read a "
                       "book</em>, the reading would start afterwards.<br><br>"
                       "<em>(<strong>Madina Charos kirishidan oldin oʻqishni boshlagan.</strong> "
                       "toʻgʻri — Continuous harakati allaqachon davom etayotgan edi. <em>Madina read a "
                       "book</em> desak, oʻqish keyin boshlangan boʻlardi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>While the girls ___ , the boys ___ football.</strong></p>",
        "choices": ["were talking … were playing", "talked … played",
                    "were talking … played", "talked … were playing"],
        "correct": "were talking … were playing",
        "explanation": "<p><strong>were talking … were playing</strong> is correct — two long actions "
                       "side by side, so both are Continuous.<br><br>"
                       "<em>(<strong>were talking … were playing</strong> toʻgʻri — yonma-yon davom "
                       "etgan ikki uzoq harakat, shuning uchun ikkisi ham Continuous.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ TV when his father ___ home.</strong></p>",
        "choices": ["was watching … came", "watched … was coming",
                    "was watching … was coming", "watched … came"],
        "correct": "was watching … came",
        "explanation": "<p><strong>was watching … came</strong> is correct — the long action is cut by "
                       "the short one.<br><br>"
                       "<em>(<strong>was watching … came</strong> toʻgʻri — uzoq harakatni qisqa harakat "
                       "kesib oʻtadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which word usually comes before the <em>long</em> action?</strong></p>",
        "choices": ["while", "when", "then", "after"],
        "correct": "while",
        "explanation": "<p><strong>while</strong> is correct — <em>while + was/were + -ing</em>. "
                       "<em>When</em> prefers the short action.<br><br>"
                       "<em>(<strong>while</strong> toʻgʻri — <em>while + was/were + -ing</em>. "
                       "<em>When</em> esa qisqa harakatni afzal koʻradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correctly punctuated sentence.</p>",
        "choices": ["While Elbek was sleeping, his phone rang.",
                    "While Elbek was sleeping his phone, rang.",
                    "While, Elbek was sleeping his phone rang.",
                    "While Elbek, was sleeping, his phone rang."],
        "correct": "While Elbek was sleeping, his phone rang.",
        "explanation": "<p><strong>While Elbek was sleeping, his phone rang.</strong> is correct. When "
                       "the <em>while</em>/<em>when</em> half comes first, a comma separates the two "
                       "halves; when it comes second, no comma is needed.<br><br>"
                       "<em>(<strong>While Elbek was sleeping, his phone rang.</strong> toʻgʻri. "
                       "<em>While</em>/<em>when</em> qismi oldin kelsa, ikki qism vergul bilan "
                       "ajratiladi; keyin kelsa, vergul qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Ilgʻor was crossing the road when a car ___ .</strong></p>",
        "choices": ["stopped", "was stopping", "stops", "stop"],
        "correct": "stopped",
        "explanation": "<p><strong>stopped</strong> is correct — a single short event inside the long "
                       "one.<br><br>"
                       "<em>(<strong>stopped</strong> toʻgʻri — uzoq harakat ichidagi bitta qisqa "
                       "voqea.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir ___ his keys while he ___ for the bus.</strong></p>",
        "choices": ["lost … was waiting", "was losing … waited",
                    "lost … waited", "was losing … was waiting"],
        "correct": "lost … was waiting",
        "explanation": "<p><strong>lost … was waiting</strong> is correct — losing the keys took a "
                       "second; waiting took a long time.<br><br>"
                       "<em>(<strong>lost … was waiting</strong> toʻgʻri — kalitni yoʻqotish bir soniya, "
                       "kutish esa uzoq davom etdi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda ___ the door and ___ the room quietly.</strong></p>",
        "choices": ["opened … entered", "was opening … was entering",
                    "opened … was entering", "was opening … entered"],
        "correct": "opened … entered",
        "explanation": "<p><strong>opened … entered</strong> is correct — two quick actions in sequence, "
                       "so both are Past Simple.<br><br>"
                       "<em>(<strong>opened … entered</strong> toʻgʻri — ketma-ket sodir boʻlgan ikki "
                       "tez harakat, shuning uchun ikkisi ham Past Simple.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["While I did my homework, the lights went out.",
                    "While I was doing my homework, the lights went out.",
                    "I was doing my homework when the lights went out.",
                    "When the lights went out, I was doing my homework."],
        "correct": "While I did my homework, the lights went out.",
        "explanation": "<p><strong>While I did my homework, the lights went out.</strong> is the mistake "
                       "— <em>while</em> needs the long Continuous action after it.<br><br>"
                       "<em>(<strong>While I did my homework, the lights went out.</strong> xato — "
                       "<em>while</em> dan keyin uzoq Continuous harakat kelishi kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Sirojiddin was riding his bike when he fell.",
                    "Sirojiddin rode his bike when he was falling.",
                    "Sirojiddin was riding his bike when he was falling.",
                    "Sirojiddin rode his bike when he fell down suddenly and was falling."],
        "correct": "Sirojiddin was riding his bike when he fell.",
        "explanation": "<p><strong>Sirojiddin was riding his bike when he fell.</strong> is correct — "
                       "long action interrupted by a one-second event.<br><br>"
                       "<em>(<strong>Sirojiddin was riding his bike when he fell.</strong> toʻgʻri — "
                       "uzoq harakatni bir soniyalik voqea uzib qoʻydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Why are you late, Abdulloh?</p>"
                "<p><strong>Abdulloh:</strong> ___</p>",
        "choices": ["I was waiting for the bus when it started to rain.",
                    "I waited for the bus when it was starting to rain.",
                    "I was waiting for the bus when it was starting to rain.",
                    "I waited for the bus when it started to raining."],
        "correct": "I was waiting for the bus when it started to rain.",
        "explanation": "<p><strong>I was waiting for the bus when it started to rain.</strong> is correct "
                       "— the waiting was the background, the rain was the event.<br><br>"
                       "<em>(<strong>I was waiting for the bus when it started to rain.</strong> "
                       "toʻgʻri — kutish fon boʻlgan, yomgʻir esa voqea.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>both</strong> tenses are used correctly.</p>",
        "choices": ["While Afsona was reading, Davron came in and switched on the light.",
                    "While Afsona read, Davron was coming in and was switching on the light.",
                    "While Afsona was reading, Davron was coming in and switched on the light.",
                    "While Afsona read, Davron came in and was switching on the light."],
        "correct": "While Afsona was reading, Davron came in and switched on the light.",
        "explanation": "<p><strong>While Afsona was reading, Davron came in and switched on the "
                       "light.</strong> is correct — one long background, then two short actions in "
                       "sequence.<br><br>"
                       "<em>(<strong>While Afsona was reading, Davron came in and switched on the "
                       "light.</strong> toʻgʻri — bitta uzoq fon, keyin ketma-ket ikki qisqa "
                       "harakat.)</em></p>",
    },
]


# =====================================================================
# PE-25 — used to and would: Past Habits
# =====================================================================

Q_PE25 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sherbek ___ play chess every day, but now he plays football.</strong></p>",
        "choices": ["used to", "use to", "is used to", "used"],
        "correct": "used to",
        "explanation": "<p><strong>used to</strong> is correct — a past habit that has stopped. The base "
                       "verb follows: <em>used to play</em>.<br><br>"
                       "<em>(<strong>used to</strong> toʻgʻri — toʻxtagan oʻtmish odati. Undan keyin "
                       "asosiy feʼl keladi: <em>used to play</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “Iroda used to have long hair” tell us?</strong></p>",
        "choices": ["She had long hair before, but not now.",
                    "She has long hair now.",
                    "She will have long hair.",
                    "She has always had long hair."],
        "correct": "She had long hair before, but not now.",
        "explanation": "<p><strong>She had long hair before, but not now.</strong> is correct — "
                       "<em>used to</em> always carries this second message: it is finished.<br><br>"
                       "<em>(<strong>Avval sochi uzun edi, hozir emas.</strong> toʻgʻri — <em>used "
                       "to</em> doim shu ikkinchi xabarni tashiydi: bu holat tugagan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ walk to school when we were small.</strong></p>",
        "choices": ["used to", "are used to", "use to", "used"],
        "correct": "used to",
        "explanation": "<p><strong>used to</strong> is correct — a repeated action in the childhood past."
                       "<br><br><em>(<strong>used to</strong> toʻgʻri — bolalikda takrorlangan "
                       "harakat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ like tomatoes, but now she eats them every day.</strong></p>",
        "choices": ["didn't use to", "didn't used to", "doesn't use to", "wasn't used to"],
        "correct": "didn't use to",
        "explanation": "<p><strong>didn't use to</strong> is correct — in the negative the <em>d</em> "
                       "disappears, because <em>didn't</em> already carries the past.<br><br>"
                       "<em>(<strong>didn't use to</strong> toʻgʻri — inkorda <em>d</em> tushib qoladi, "
                       "chunki oʻtgan zamonni <em>didn't</em> allaqachon bildirgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ you use to live in Namangan?</strong></p>",
        "choices": ["Did", "Do", "Were", "Have"],
        "correct": "Did",
        "explanation": "<p><strong>Did</strong> is correct — the question uses the ordinary past helper, "
                       "and again the <em>d</em> of <em>used</em> disappears.<br><br>"
                       "<em>(<strong>Did</strong> toʻgʻri — savolda oddiy oʻtgan zamon yordamchisi "
                       "ishlatiladi va <em>used</em> ning <em>d</em> si yana tushib qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ a cinema on this street, but they knocked it down.</strong></p>",
        "choices": ["used to be", "used to being", "was used to be", "uses to be"],
        "correct": "used to be",
        "explanation": "<p><strong>used to be</strong> is correct — <em>used to</em> works with states "
                       "too, not only actions.<br><br>"
                       "<em>(<strong>used to be</strong> toʻgʻri — <em>used to</em> harakat bilan ham, "
                       "holat bilan ham ishlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In summer my grandfather ___ tell us long stories every "
                "evening.</strong></p>",
        "choices": ["would", "will", "used", "is used to"],
        "correct": "would",
        "explanation": "<p><strong>would</strong> is correct — <em>would</em> can replace <em>used to</em> "
                       "for repeated <em>actions</em>, and it sounds warm and story-like.<br><br>"
                       "<em>(<strong>would</strong> toʻgʻri — takrorlangan <em>harakatlar</em> uchun "
                       "<em>would</em> <em>used to</em> ni almashtira oladi va hikoyaga xos, iliq "
                       "eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is <em>wrong</em> with “would”?</strong></p>",
        "choices": ["I would have a bicycle when I was ten.",
                    "I would ride my bicycle every evening.",
                    "We would visit our grandmother every summer.",
                    "He would help his father in the garden."],
        "correct": "I would have a bicycle when I was ten.",
        "explanation": "<p><strong>I would have a bicycle when I was ten.</strong> is wrong — "
                       "<em>have</em> here is a state, and <em>would</em> only works with repeated "
                       "actions. Say <em>I used to have a bicycle</em>.<br><br>"
                       "<em>(<strong>I would have a bicycle when I was ten.</strong> xato — bu yerda "
                       "<em>have</em> holatni bildiradi, <em>would</em> esa faqat takrorlanadigan "
                       "harakatlar bilan ishlaydi. <em>I used to have a bicycle</em> deyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ be afraid of dogs, but now she has one.</strong></p>",
        "choices": ["used to", "would", "is used to", "uses to"],
        "correct": "used to",
        "explanation": "<p><strong>used to</strong> is correct — <em>be afraid</em> is a state, so "
                       "<em>would</em> is not possible here.<br><br>"
                       "<em>(<strong>used to</strong> toʻgʻri — <em>be afraid</em> holat, shuning uchun "
                       "bu yerda <em>would</em> mumkin emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ getting up early — he has done it for years.</strong></p>",
        "choices": ["is used to", "used to", "did use to", "would"],
        "correct": "is used to",
        "explanation": "<p><strong>is used to</strong> is correct. <em>Be used to + -ing</em> means "
                       "“accustomed to”, and it is about <em>now</em>, not the past. Watch this "
                       "look-alike carefully.<br><br>"
                       "<em>(<strong>is used to</strong> toʻgʻri. <em>Be used to + -ing</em> “koʻnikkan” "
                       "degani va <em>hozir</em> haqida, oʻtmish haqida emas. Bu oʻxshash shakldan "
                       "ehtiyot boʻling.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What follows <em>be used to</em>?</strong></p>",
        "choices": ["a verb with -ing", "a base verb", "the past form", "the infinitive with to"],
        "correct": "a verb with -ing",
        "explanation": "<p><strong>a verb with -ing</strong> is correct: <em>I'm used to walking</em>. "
                       "Compare <em>I used to walk</em> — base verb, past habit.<br><br>"
                       "<em>(<strong>-ing</strong> li feʼl toʻgʻri: <em>I'm used to walking</em>. "
                       "<em>I used to walk</em> bilan solishtiring — asosiy feʼl, oʻtmish "
                       "odati.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar and Davron ___ play in this yard when they were "
                "children.</strong></p>",
        "choices": ["used to", "was used to", "uses to", "are used to"],
        "correct": "used to",
        "explanation": "<p><strong>used to</strong> is correct — the form never changes for person or "
                       "number.<br><br>"
                       "<em>(<strong>used to</strong> toʻgʻri — bu shakl shaxs va songa qarab "
                       "oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence talks about a habit that has <em>stopped</em>?</strong></p>",
        "choices": ["Marjona used to play the piano.", "Marjona plays the piano.",
                    "Marjona is playing the piano.", "Marjona is used to playing the piano."],
        "correct": "Marjona used to play the piano.",
        "explanation": "<p><strong>Marjona used to play the piano.</strong> is correct — the others are "
                       "all about the present.<br><br>"
                       "<em>(<strong>Marjona used to play the piano.</strong> toʻgʻri — qolganlari "
                       "hozirgi zamon haqida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek didn't ___ speak English well, but now he speaks it "
                "fluently.</strong></p>",
        "choices": ["use to", "used to", "uses to", "using to"],
        "correct": "use to",
        "explanation": "<p><strong>use to</strong> is correct — after <em>didn't</em> the <em>d</em> is "
                       "gone. This missing letter is the most common mistake with this "
                       "structure.<br><br>"
                       "<em>(<strong>use to</strong> toʻgʻri — <em>didn't</em> dan keyin <em>d</em> "
                       "yoʻqoladi. Aynan shu tushib qolgan harf — bu qurilishdagi eng koʻp uchraydigan "
                       "xato.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ to school by bus last Monday.</strong></p>",
        "choices": ["went", "used to go", "would go", "uses to go"],
        "correct": "went",
        "explanation": "<p><strong>went</strong> is correct — <em>last Monday</em> is one single "
                       "occasion, and <em>used to</em> is only for repeated habits.<br><br>"
                       "<em>(<strong>went</strong> toʻgʻri — <em>last Monday</em> bir marta boʻlgan "
                       "voqea, <em>used to</em> esa faqat takrorlanadigan odatlar uchun.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Ilgʻor ___ be very shy, but now he speaks in front of the whole "
                "class.</strong></p>",
        "choices": ["used to", "would", "was used to", "used"],
        "correct": "used to",
        "explanation": "<p><strong>used to</strong> is correct — <em>be shy</em> is a state, so "
                       "<em>would</em> cannot be used.<br><br>"
                       "<em>(<strong>used to</strong> toʻgʻri — <em>be shy</em> holat, shuning uchun "
                       "<em>would</em> ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Javohir didn't used to like maths.", "Javohir didn't use to like maths.",
                    "Javohir used to like maths.", "Did Javohir use to like maths?"],
        "correct": "Javohir didn't used to like maths.",
        "explanation": "<p><strong>Javohir didn't used to like maths.</strong> is the mistake — the "
                       "<em>d</em> must go after <em>didn't</em>.<br><br>"
                       "<em>(<strong>Javohir didn't used to like maths.</strong> xato — <em>didn't</em> "
                       "dan keyin <em>d</em> tushishi kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Shaxzoda is used to getting up at six.",
                    "Shaxzoda is used to get up at six.",
                    "Shaxzoda used to getting up at six.",
                    "Shaxzoda is use to getting up at six."],
        "correct": "Shaxzoda is used to getting up at six.",
        "explanation": "<p><strong>Shaxzoda is used to getting up at six.</strong> is correct — "
                       "<em>be used to + -ing</em>, meaning she is accustomed to it now.<br><br>"
                       "<em>(<strong>Shaxzoda is used to getting up at six.</strong> toʻgʻri — "
                       "<em>be used to + -ing</em>, yaʼni u hozir bunga koʻnikkan.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Did you use to play any sport, Sirojiddin?</p>"
                "<p><strong>Sirojiddin:</strong> ___</p>",
        "choices": ["Yes, I used to play volleyball, but I stopped last year.",
                    "Yes, I use to play volleyball, but I stopped last year.",
                    "Yes, I am used to play volleyball, but I stopped last year.",
                    "Yes, I used to playing volleyball, but I stopped last year."],
        "correct": "Yes, I used to play volleyball, but I stopped last year.",
        "explanation": "<p><strong>Yes, I used to play volleyball, but I stopped last year.</strong> is "
                       "correct — the positive form keeps the <em>d</em>, and the base verb follows."
                       "<br><br><em>(<strong>Yes, I used to play volleyball, but I stopped last "
                       "year.</strong> toʻgʻri — tasdiq shaklda <em>d</em> saqlanadi, undan keyin esa "
                       "asosiy feʼl keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Afsona used to be afraid of exams, but now she is used to writing tests "
                    "every week.",
                    "Afsona use to be afraid of exams, but now she used to write tests every week.",
                    "Afsona used to being afraid of exams, but now she is used to write tests "
                    "every week.",
                    "Afsona didn't used to be afraid of exams, but now she is used to write tests "
                    "every week."],
        "correct": "Afsona used to be afraid of exams, but now she is used to writing tests "
                   "every week.",
        "explanation": "<p><strong>used to be … is used to writing …</strong> is correct — the two "
                       "look-alikes in one sentence: past habit with the base verb, present "
                       "accustomedness with <em>-ing</em>.<br><br>"
                       "<em>(<strong>used to be … is used to writing …</strong> toʻgʻri — bir gapda "
                       "ikki oʻxshash shakl: asosiy feʼl bilan oʻtmish odati va <em>-ing</em> bilan "
                       "hozirgi koʻnikma.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-21 Practice: Past Simple: Irregular Verbs",
        "tutorial":    "PE-21:",
        "description": "PE-21 darsiga 20 savol: notoʻgʻri feʼllarning oʻtgan shakllari, tovush "
                       "guruhlari, oʻzgarmaydigan feʼllar (cut, put) va read → read tuzogʻi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE21,
    },
    {
        "title":       "PE-22 Practice: Past Simple: Negatives and Questions",
        "tutorial":    "PE-22:",
        "description": "PE-22 darsiga 20 savol: didn't va Did bilan inkor va savollar, feʼlning "
                       "asosiy shaklga qaytishi, qisqa javoblar va did ishlatilmaydigan ikki holat. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE22,
    },
    {
        "title":       "PE-23 Practice: Past Continuous: The Interrupted Moment",
        "tutorial":    "PE-23:",
        "description": "PE-23 darsiga 20 savol: was/were + -ing, oʻtgan daqiqadagi harakat, parallel "
                       "harakatlar, fon manzarasi va -ing olmaydigan holat feʼllari. Javoblar ingliz "
                       "va oʻzbek tilida izohlangan.",
        "questions":   Q_PE23,
    },
    {
        "title":       "PE-24 Practice: Past Simple vs Past Continuous: when and while",
        "tutorial":    "PE-24:",
        "description": "PE-24 darsiga 20 savol: uzoq va qisqa harakat qoidasi, when va while bilan "
                       "qaysi zamon kelishi, ketma-ket harakatlar va vergul qoʻyilishi. Javoblar "
                       "ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE24,
    },
    {
        "title":       "PE-25 Practice: used to and would: Past Habits",
        "tutorial":    "PE-25:",
        "description": "PE-25 darsiga 20 savol: used to + asosiy feʼl, didn't use to dagi tushib "
                       "qoladigan d, would qachon almashtira oladi va be used to + -ing farqi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE25,
    },
]
