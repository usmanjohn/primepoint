# -*- coding: utf-8 -*-
"""Prime English practices — PE-36 … PE-40 (the rest of the perfect tenses).

Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_36_40.py --master=prime --expect-questions=20
"""

SUBJECT = {
    "name":        "English",
    "description": "English grammar and vocabulary practice",
    "icon":        "bi-translate",
    "color":       "#6366f1",
}

DEFAULTS = {
    "level":                "medium",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PE-36 — Present Perfect Continuous
# =====================================================================

Q_PE36 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ for two hours! Where were you?</strong></p>",
        "choices": ["have been waiting", "have waited for", "am waiting", "was waiting"],
        "correct": "have been waiting",
        "explanation": "<p><strong>have been waiting</strong> is correct — the form is "
                       "<em>have / has + been + verb-ing</em>, and it puts the spotlight on how long the "
                       "activity lasted.<br><br>"
                       "<em>(<strong>have been waiting</strong> toʻgʻri — shakli "
                       "<em>have / has + been + feʼl-ing</em> boʻlib, faoliyat qancha davom etganiga "
                       "urgʻu beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona ___ studying all night — look at her tired eyes.</strong></p>",
        "choices": ["has been", "have been", "is been", "has being"],
        "correct": "has been",
        "explanation": "<p><strong>has been</strong> is correct — one person takes <em>has</em>, and "
                       "<em>been</em> never changes.<br><br>"
                       "<em>(<strong>has been</strong> toʻgʻri — bitta shaxs <em>has</em> oladi, "
                       "<em>been</em> esa hech qachon oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz and Elbek ___ football since four o'clock.</strong></p>",
        "choices": ["have been playing", "has been playing", "have been played", "are playing since"],
        "correct": "have been playing",
        "explanation": "<p><strong>have been playing</strong> is correct — a plural subject takes "
                       "<em>have</em>, and the activity is still going on.<br><br>"
                       "<em>(<strong>have been playing</strong> toʻgʻri — koʻplikdagi subject "
                       "<em>have</em> oladi, faoliyat esa hali davom etmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The ground is wet. It ___ .</strong></p>",
        "choices": ["has been raining", "has rained it", "is raining", "rains"],
        "correct": "has been raining",
        "explanation": "<p><strong>has been raining</strong> is correct — the activity has just stopped "
                       "but its traces are still visible. That is the second job of this tense.<br><br>"
                       "<em>(<strong>has been raining</strong> toʻgʻri — faoliyat hozirgina toʻxtadi, "
                       "lekin izlari koʻrinib turibdi. Bu — bu zamonning ikkinchi vazifasi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How long ___ Iroda been learning Korean?</strong></p>",
        "choices": ["has", "have", "did", "is"],
        "correct": "has",
        "explanation": "<p><strong>has</strong> is correct — questions start with "
                       "<em>have / has + subject + been + -ing</em>.<br><br>"
                       "<em>(<strong>has</strong> toʻgʻri — savol <em>have / has + subject + been + "
                       "-ing</em> shaklida boshlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos has been reading that book ___ Monday.</strong></p>",
        "choices": ["since", "for", "ago", "during"],
        "correct": "since",
        "explanation": "<p><strong>since</strong> is correct — <em>Monday</em> is the point where the "
                       "activity started.<br><br>"
                       "<em>(<strong>since</strong> toʻgʻri — <em>Monday</em> faoliyat boshlangan "
                       "nuqta.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar has been working in the garden ___ three hours.</strong></p>",
        "choices": ["for", "since", "ago", "by"],
        "correct": "for",
        "explanation": "<p><strong>for</strong> is correct — <em>three hours</em> is a length of "
                       "time.<br><br>"
                       "<em>(<strong>for</strong> toʻgʻri — <em>three hours</em> vaqt "
                       "uzunligi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Firdavs ___ been feeling well lately.</strong></p>",
        "choices": ["hasn't", "haven't", "didn't", "isn't"],
        "correct": "hasn't",
        "explanation": "<p><strong>hasn't</strong> is correct — the negative sits on <em>has</em>, and "
                       "<em>been + -ing</em> follows unchanged.<br><br>"
                       "<em>(<strong>hasn't</strong> toʻgʻri — inkor <em>has</em> ga qoʻyiladi, "
                       "<em>been + -ing</em> esa oʻzgarishsiz keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ at our school for twelve years.</strong></p>",
        "choices": ["has been teaching", "is teaching", "teaches since", "has been taught"],
        "correct": "has been teaching",
        "explanation": "<p><strong>has been teaching</strong> is correct — a long activity that started "
                       "in the past and still continues.<br><br>"
                       "<em>(<strong>has been teaching</strong> toʻgʻri — oʻtmishda boshlanib hali davom "
                       "etayotgan uzoq faoliyat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which verb can <em>never</em> be used in this tense?</strong></p>",
        "choices": ["know", "wait", "study", "work"],
        "correct": "know",
        "explanation": "<p><strong>know</strong> is correct — stative verbs (<em>know, like, want, "
                       "believe, understand</em>) refuse <em>-ing</em> in every tense. Say <em>I have "
                       "known him for years</em>.<br><br>"
                       "<em>(<strong>know</strong> toʻgʻri — holat feʼllari (<em>know, like, want, "
                       "believe, understand</em>) barcha zamonlarda <em>-ing</em> ni rad etadi. "
                       "<em>I have known him for years</em> deyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir ___ Sherbek since primary school.</strong></p>",
        "choices": ["has known", "has been knowing", "is knowing", "has been known"],
        "correct": "has known",
        "explanation": "<p><strong>has known</strong> is correct — a stative verb, so only the Simple "
                       "form is possible.<br><br>"
                       "<em>(<strong>has known</strong> toʻgʻri — holat feʼli, shuning uchun faqat Simple "
                       "shakli mumkin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Why are your hands dirty? — I ___ my bicycle.</strong></p>",
        "choices": ["have been repairing", "have repaired", "repair", "am repaired"],
        "correct": "have been repairing",
        "explanation": "<p><strong>have been repairing</strong> is correct — the dirty hands are the "
                       "trace the activity left on me.<br><br>"
                       "<em>(<strong>have been repairing</strong> toʻgʻri — kir qoʻllar — faoliyat "
                       "qoldirgan iz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda ___ for the exam since early morning, and she is still at "
                "her desk.</strong></p>",
        "choices": ["has been preparing", "prepared", "prepares", "is prepared"],
        "correct": "has been preparing",
        "explanation": "<p><strong>has been preparing</strong> is correct — the activity started earlier "
                       "and has not stopped.<br><br>"
                       "<em>(<strong>has been preparing</strong> toʻgʻri — faoliyat oldin boshlangan va "
                       "toʻxtamagan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence stresses <em>how long</em> the activity lasted?</strong></p>",
        "choices": ["Abdulloh has been writing letters all evening.",
                    "Abdulloh has written three letters.",
                    "Abdulloh writes letters.",
                    "Abdulloh wrote a letter yesterday."],
        "correct": "Abdulloh has been writing letters all evening.",
        "explanation": "<p><strong>Abdulloh has been writing letters all evening.</strong> is correct — "
                       "the Continuous shows the line of activity; the Simple would count the "
                       "results.<br><br>"
                       "<em>(<strong>Abdulloh has been writing letters all evening.</strong> toʻgʻri — "
                       "Continuous faoliyat chizigʻini koʻrsatadi, Simple esa natijani "
                       "sanaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Has Ilgʻor been helping you? — Yes, ___ .</strong></p>",
        "choices": ["he has", "he is", "he did", "he have"],
        "correct": "he has",
        "explanation": "<p><strong>he has</strong> is correct — the short answer repeats only the first "
                       "helper.<br><br>"
                       "<em>(<strong>he has</strong> toʻgʻri — qisqa javobda faqat birinchi yordamchi "
                       "takrorlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct -ing form.</p>"
                "<p><strong>Madina has been ___ her room since morning. (tidy)</strong></p>",
        "choices": ["tidying", "tidieing", "tidyying", "tided"],
        "correct": "tidying",
        "explanation": "<p><strong>tidying</strong> is correct — a verb ending in <em>-y</em> simply adds "
                       "<em>-ing</em>; the <em>y</em> never changes before <em>-ing</em>.<br><br>"
                       "<em>(<strong>tidying</strong> toʻgʻri — <em>-y</em> bilan tugagan feʼl shunchaki "
                       "<em>-ing</em> oladi; <em>-ing</em> oldidan <em>y</em> hech qachon "
                       "oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Sirojiddin has been knowing Davron for years.",
                    "Sirojiddin has known Davron for years.",
                    "Sirojiddin has been playing chess for years.",
                    "Sirojiddin has been waiting for an hour."],
        "correct": "Sirojiddin has been knowing Davron for years.",
        "explanation": "<p><strong>Sirojiddin has been knowing Davron for years.</strong> is the mistake "
                       "— <em>know</em> is stative and cannot take <em>-ing</em>.<br><br>"
                       "<em>(<strong>Sirojiddin has been knowing Davron for years.</strong> xato — "
                       "<em>know</em> holat feʼli va <em>-ing</em> ola olmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["We have been living here since 2020.",
                    "We have been live here since 2020.",
                    "We has been living here since 2020.",
                    "We have being living here since 2020."],
        "correct": "We have been living here since 2020.",
        "explanation": "<p><strong>We have been living here since 2020.</strong> is correct — all three "
                       "pieces are in place: <em>have + been + living</em>.<br><br>"
                       "<em>(<strong>We have been living here since 2020.</strong> toʻgʻri — uchala "
                       "boʻlak ham oʻz oʻrnida: <em>have + been + living</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> You look exhausted, Behruz.</p>"
                "<p><strong>Behruz:</strong> ___</p>",
        "choices": ["I've been revising for the test since six o'clock.",
                    "I've revised for the test since six o'clock ago.",
                    "I am revising for the test since six o'clock.",
                    "I have been revise for the test since six o'clock."],
        "correct": "I've been revising for the test since six o'clock.",
        "explanation": "<p><strong>I've been revising for the test since six o'clock.</strong> is correct "
                       "— the long activity explains why he looks exhausted now.<br><br>"
                       "<em>(<strong>I've been revising for the test since six o'clock.</strong> "
                       "toʻgʻri — uzoq faoliyat uning hozir charchagan koʻrinishini "
                       "tushuntiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Afsona has been studying since morning, but she has known this rule for years.",
                    "Afsona has been studying since morning, but she has been knowing this rule "
                    "for years.",
                    "Afsona is studying since morning, but she knows this rule for years.",
                    "Afsona has studied since morning ago, but she has been knowing this rule "
                    "since years."],
        "correct": "Afsona has been studying since morning, but she has known this rule for years.",
        "explanation": "<p><strong>has been studying … has known …</strong> is correct — an activity in "
                       "the Continuous, a stative verb forced into the Simple.<br><br>"
                       "<em>(<strong>has been studying … has known …</strong> toʻgʻri — faoliyat "
                       "Continuous da, holat feʼli esa Simple da.)</em></p>",
    },
]


# =====================================================================
# PE-37 — Present Perfect Simple vs Continuous
# =====================================================================

Q_PE37 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ the kitchen — come and look how clean it is!</strong></p>",
        "choices": ["have painted", "have been painting", "am painting", "paint"],
        "correct": "have painted",
        "explanation": "<p><strong>have painted</strong> is correct — the invitation to look means the "
                       "job is finished, so we point at the result.<br><br>"
                       "<em>(<strong>have painted</strong> toʻgʻri — “kelib qarang” degani ish tugagan "
                       "degani, yaʼni natijaga ishora qilinmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ the kitchen — that's why there is paint in my hair.</strong></p>",
        "choices": ["have been painting", "have painted", "painted", "paint"],
        "correct": "have been painting",
        "explanation": "<p><strong>have been painting</strong> is correct — the paint in the hair is a "
                       "trace of the activity, not a finished result.<br><br>"
                       "<em>(<strong>have been painting</strong> toʻgʻri — sochdagi boʻyoq — faoliyatning "
                       "izi, tugagan natija emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which question goes with the Simple form?</strong></p>",
        "choices": ["How many?", "How long?", "Since when?", "For how long exactly?"],
        "correct": "How many?",
        "explanation": "<p><strong>How many?</strong> is correct — counting finished results needs the "
                       "Simple; <em>How long?</em> asks about the activity and takes the "
                       "Continuous.<br><br>"
                       "<em>(<strong>How many?</strong> toʻgʻri — tugagan natijalarni sanash Simple ni "
                       "talab qiladi; <em>How long?</em> esa faoliyat haqida soʻraydi va Continuous "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ three emails this morning.</strong></p>",
        "choices": ["has written", "has been writing", "is writing", "writes"],
        "correct": "has written",
        "explanation": "<p><strong>has written</strong> is correct — a number of finished items, so the "
                       "Simple.<br><br>"
                       "<em>(<strong>has written</strong> toʻgʻri — tugagan ishlarning soni aytilgan, "
                       "shuning uchun Simple.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ emails all morning — she hasn't stopped once.</strong></p>",
        "choices": ["has been writing", "has written", "wrote", "writes"],
        "correct": "has been writing",
        "explanation": "<p><strong>has been writing</strong> is correct — no number, just a long stretch "
                       "of activity.<br><br>"
                       "<em>(<strong>has been writing</strong> toʻgʻri — son yoʻq, faqat uzoq davom "
                       "etgan faoliyat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Jasur ___ that book, so he can tell you the ending.</strong></p>",
        "choices": ["has read", "has been reading", "reads", "is reading"],
        "correct": "has read",
        "explanation": "<p><strong>has read</strong> is correct — he finished it, which is why he knows "
                       "the ending.<br><br>"
                       "<em>(<strong>has read</strong> toʻgʻri — u kitobni oʻqib tugatgan, shuning uchun "
                       "oxirini biladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Jasur ___ that book — he is on page ninety.</strong></p>",
        "choices": ["has been reading", "has read", "read", "reads"],
        "correct": "has been reading",
        "explanation": "<p><strong>has been reading</strong> is correct — he is in the middle of it, so "
                       "the activity is unfinished.<br><br>"
                       "<em>(<strong>has been reading</strong> toʻgʻri — u hali oʻrtasida, yaʼni faoliyat "
                       "tugamagan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ all her exercises. There is nothing left.</strong></p>",
        "choices": ["has done", "has been doing", "does", "is doing"],
        "correct": "has done",
        "explanation": "<p><strong>has done</strong> is correct — <em>all</em> and <em>nothing left</em> "
                       "point at a complete result.<br><br>"
                       "<em>(<strong>has done</strong> toʻgʻri — <em>all</em> va <em>nothing left</em> "
                       "toʻliq natijani koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek ___ chess for three hours and the game is still not "
                "over.</strong></p>",
        "choices": ["has been playing", "has played", "played", "plays"],
        "correct": "has been playing",
        "explanation": "<p><strong>has been playing</strong> is correct — the activity is still "
                       "running.<br><br>"
                       "<em>(<strong>has been playing</strong> toʻgʻri — faoliyat hali davom "
                       "etmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ twenty tests, and ten are still on his "
                "desk.</strong></p>",
        "choices": ["has marked", "has been marking twenty", "marks", "is marked"],
        "correct": "has marked",
        "explanation": "<p><strong>has marked</strong> is correct — a counted quantity of finished work "
                       "takes the Simple.<br><br>"
                       "<em>(<strong>has marked</strong> toʻgʻri — bajarilgan ishning sanalgan miqdori "
                       "Simple ni oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ English for six years.</strong> Which is also "
                "correct here?</p>",
        "choices": ["Both 'has studied' and 'has been studying'.",
                    "Only 'has studied'.",
                    "Only 'has been studying'.",
                    "Neither of them."],
        "correct": "Both 'has studied' and 'has been studying'.",
        "explanation": "<p><strong>Both are correct.</strong> With <em>live, work, study, teach</em> plus "
                       "<em>for / since</em>, the difference almost disappears and English speakers use "
                       "either form.<br><br>"
                       "<em>(<strong>Ikkisi ham toʻgʻri.</strong> <em>Live, work, study, teach</em> "
                       "feʼllari <em>for / since</em> bilan kelganda farq deyarli yoʻqoladi va ikki "
                       "shakl ham ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda ___ this classroom for years — she remembers every "
                "desk.</strong></p>",
        "choices": ["has known", "has been knowing", "knows since", "is knowing"],
        "correct": "has known",
        "explanation": "<p><strong>has known</strong> is correct — stative verbs allow only the Simple, "
                       "whatever the meaning.<br><br>"
                       "<em>(<strong>has known</strong> toʻgʻri — holat feʼllari, maʼnosidan qatʼi nazar, "
                       "faqat Simple ga ruxsat beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Behruz ___ five pages, and he ___ since morning.</strong></p>",
        "choices": ["has translated … has been working", "has been translating … has worked",
                    "has translated … has worked", "has been translating … has been working"],
        "correct": "has translated … has been working",
        "explanation": "<p><strong>has translated … has been working</strong> is correct — a number takes "
                       "the Simple, a stretch of time takes the Continuous.<br><br>"
                       "<em>(<strong>has translated … has been working</strong> toʻgʻri — son Simple ni, "
                       "vaqt davomiyligi esa Continuous ni oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence explains <em>why somebody is tired</em>?</strong></p>",
        "choices": ["Firdavs has been carrying boxes all afternoon.",
                    "Firdavs has carried ten boxes.",
                    "Firdavs carries boxes.",
                    "Firdavs carried a box yesterday."],
        "correct": "Firdavs has been carrying boxes all afternoon.",
        "explanation": "<p><strong>Firdavs has been carrying boxes all afternoon.</strong> is correct — "
                       "the Continuous explains a present state by the activity behind it.<br><br>"
                       "<em>(<strong>Firdavs has been carrying boxes all afternoon.</strong> toʻgʻri — "
                       "Continuous hozirgi holatni orqasidagi faoliyat bilan tushuntiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda ___ her tea — the cup is empty.</strong></p>",
        "choices": ["has drunk", "has been drinking", "drinks", "is drinking"],
        "correct": "has drunk",
        "explanation": "<p><strong>has drunk</strong> is correct — the empty cup is a completed "
                       "result.<br><br>"
                       "<em>(<strong>has drunk</strong> toʻgʻri — boʻsh piyola — tugallangan "
                       "natija.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Somebody ___ my tea — the cup is half empty!</strong></p>",
        "choices": ["has been drinking", "has drunk it all", "drinks", "drank all"],
        "correct": "has been drinking",
        "explanation": "<p><strong>has been drinking</strong> is correct — half empty means the activity "
                       "happened but was not completed.<br><br>"
                       "<em>(<strong>has been drinking</strong> toʻgʻri — yarim boʻsh degani faoliyat "
                       "boʻlgan, lekin tugallanmagan.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Sirojiddin has been finishing his homework.",
                    "Sirojiddin has finished his homework.",
                    "Sirojiddin has been doing his homework.",
                    "Sirojiddin has done his homework."],
        "correct": "Sirojiddin has been finishing his homework.",
        "explanation": "<p><strong>Sirojiddin has been finishing his homework.</strong> is the mistake — "
                       "<em>finish</em> names a single completed moment, so it does not stretch into an "
                       "activity.<br><br>"
                       "<em>(<strong>Sirojiddin has been finishing his homework.</strong> xato — "
                       "<em>finish</em> bitta tugallangan daqiqani bildiradi, shuning uchun choʻzilgan "
                       "faoliyatga aylanmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["How many books have you read this year?",
                    "How many books have you been reading this year?",
                    "How long have you read this year?",
                    "How many books you have been read this year?"],
        "correct": "How many books have you read this year?",
        "explanation": "<p><strong>How many books have you read this year?</strong> is correct — "
                       "<em>How many</em> counts results, so the Simple is needed.<br><br>"
                       "<em>(<strong>How many books have you read this year?</strong> toʻgʻri — "
                       "<em>How many</em> natijalarni sanaydi, shuning uchun Simple kerak.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Davron:</strong> Your hands are covered in flour!</p>"
                "<p><strong>Marjona:</strong> ___</p>",
        "choices": ["I've been making bread with my mother.",
                    "I've made bread with my mother, that's why.",
                    "I make bread with my mother since morning.",
                    "I have been make bread with my mother."],
        "correct": "I've been making bread with my mother.",
        "explanation": "<p><strong>I've been making bread with my mother.</strong> is correct — the flour "
                       "is the visible trace of the activity, not a finished product.<br><br>"
                       "<em>(<strong>I've been making bread with my mother.</strong> toʻgʻri — un — "
                       "faoliyatning koʻrinib turgan izi, tayyor mahsulot emas.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>both</strong> forms are used correctly.</p>",
        "choices": ["Abdulloh has been learning to drive for a year, and he has already passed "
                    "two tests.",
                    "Abdulloh has learnt to drive for a year, and he has already been passing "
                    "two tests.",
                    "Abdulloh has been learning to drive for a year, and he has already been "
                    "passing two tests.",
                    "Abdulloh has learn to drive for a year, and he has already pass two tests."],
        "correct": "Abdulloh has been learning to drive for a year, and he has already passed "
                   "two tests.",
        "explanation": "<p><strong>has been learning … has already passed …</strong> is correct — a long "
                       "activity in the Continuous, two counted results in the Simple.<br><br>"
                       "<em>(<strong>has been learning … has already passed …</strong> toʻgʻri — uzoq "
                       "faoliyat Continuous da, sanalgan ikki natija esa Simple da.)</em></p>",
    },
]


# =====================================================================
# PE-38 — Past Perfect
# =====================================================================

Q_PE38 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>When Behruz arrived at the station, the train ___ .</strong></p>",
        "choices": ["had left", "left", "has left", "was leaving"],
        "correct": "had left",
        "explanation": "<p><strong>had left</strong> is correct — the train went first, so the earlier "
                       "action takes <em>had + V3</em>.<br><br>"
                       "<em>(<strong>had left</strong> toʻgʻri — poyezd oldin joʻnadi, shuning uchun "
                       "avvalroq boʻlgan harakat <em>had + V3</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the form of the Past Perfect?</strong></p>",
        "choices": ["had + V3, for every person", "have + V3", "was + V3", "had + V2"],
        "correct": "had + V3, for every person",
        "explanation": "<p><strong>had + V3, for every person</strong> is correct — <em>I had, she had, "
                       "they had</em>; nothing changes.<br><br>"
                       "<em>(<strong>had + V3, har bir shaxs uchun</strong> toʻgʻri — <em>I had, she "
                       "had, they had</em>; hech narsa oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda couldn't get in because she ___ her keys at home.</strong></p>",
        "choices": ["had left", "left", "has left", "leaves"],
        "correct": "had left",
        "explanation": "<p><strong>had left</strong> is correct — leaving the keys happened before the "
                       "moment she stood at the door.<br><br>"
                       "<em>(<strong>had left</strong> toʻgʻri — kalitni qoldirish u eshik oldida turgan "
                       "daqiqadan oldin sodir boʻlgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>By the time Rozimurod teacher came in, the pupils ___ their "
                "books.</strong></p>",
        "choices": ["had opened", "opened", "have opened", "were opening"],
        "correct": "had opened",
        "explanation": "<p><strong>had opened</strong> is correct — <em>by the time</em> is one of this "
                       "tense's favourite partners.<br><br>"
                       "<em>(<strong>had opened</strong> toʻgʻri — <em>by the time</em> bu zamonning eng "
                       "sevimli hamrohlaridan biri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “When I arrived, the train had left” mean?</strong></p>",
        "choices": ["The train left before I arrived.",
                    "The train left after I arrived.",
                    "We arrived at exactly the same time.",
                    "The train never left."],
        "correct": "The train left before I arrived.",
        "explanation": "<p><strong>The train left before I arrived.</strong> is correct — compare "
                       "<em>When I arrived, the train left</em>, which would mean it left afterwards."
                       "<br><br><em>(<strong>Poyezd men yetib borishimdan oldin joʻnab ketgan.</strong> "
                       "toʻgʻri — <em>When I arrived, the train left</em> bilan solishtiring: u keyin "
                       "joʻnagan boʻlardi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>After Charos ___ her homework, she went out.</strong></p>",
        "choices": ["had finished", "has finished", "finish", "was finishing"],
        "correct": "had finished",
        "explanation": "<p><strong>had finished</strong> is correct — the finishing came first, then the "
                       "going out.<br><br>"
                       "<em>(<strong>had finished</strong> toʻgʻri — avval tugatdi, keyin "
                       "chiqdi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ never ___ the sea before that trip.</strong></p>",
        "choices": ["had … seen", "has … seen", "did … see", "had … saw"],
        "correct": "had … seen",
        "explanation": "<p><strong>had … seen</strong> is correct — experience up to a point in the past "
                       "takes the Past Perfect.<br><br>"
                       "<em>(<strong>had … seen</strong> toʻgʻri — oʻtmishdagi bir nuqtaga qadar boʻlgan "
                       "tajriba Past Perfect oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Elbek ___ done his homework, so the teacher was angry.</strong></p>",
        "choices": ["hadn't", "hasn't", "didn't", "wasn't"],
        "correct": "hadn't",
        "explanation": "<p><strong>hadn't</strong> is correct — the not-doing came before the "
                       "anger.<br><br>"
                       "<em>(<strong>hadn't</strong> toʻgʻri — bajarmaslik jahl chiqishidan oldin sodir "
                       "boʻlgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ Madina already left when you called?</strong></p>",
        "choices": ["Had", "Did", "Has", "Was"],
        "correct": "Had",
        "explanation": "<p><strong>Had</strong> is correct — <em>had</em> moves in front of the subject "
                       "to make the question.<br><br>"
                       "<em>(<strong>Had</strong> toʻgʻri — savol yasash uchun <em>had</em> subject "
                       "oldiga chiqadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs was hungry because he ___ breakfast.</strong></p>",
        "choices": ["hadn't eaten", "didn't eat", "hasn't eaten", "wasn't eating"],
        "correct": "hadn't eaten",
        "explanation": "<p><strong>hadn't eaten</strong> is correct — the reason lies further back than "
                       "the hunger itself.<br><br>"
                       "<em>(<strong>hadn't eaten</strong> toʻgʻri — sabab ochlikdan ham "
                       "avvalroqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>When Javohir ___ home, his brother ___ already ___ the "
                "dishes.</strong></p>",
        "choices": ["got … had … washed", "had got … has … washed",
                    "got … has … washed", "had got … had … washed"],
        "correct": "got … had … washed",
        "explanation": "<p><strong>got … had … washed</strong> is correct — the later event is a normal "
                       "Past Simple, the earlier one is <em>had + V3</em>.<br><br>"
                       "<em>(<strong>got … had … washed</strong> toʻgʻri — keyingi voqea oddiy Past "
                       "Simple, avvalgisi esa <em>had + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda got up, washed her face and ___ breakfast.</strong></p>",
        "choices": ["had", "had had", "has had", "was having"],
        "correct": "had",
        "explanation": "<p><strong>had</strong> is correct. When actions are told in the order they "
                       "happened, the Past Simple is enough — the Past Perfect is only needed to break "
                       "that order.<br><br>"
                       "<em>(<strong>had</strong> toʻgʻri. Harakatlar sodir boʻlgan tartibda aytilsa, "
                       "Past Simple yetarli — Past Perfect faqat tartib buzilganda kerak "
                       "boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence does <em>not</em> need the Past Perfect?</strong></p>",
        "choices": ["Abdulloh came in, sat down and opened his book.",
                    "Abdulloh was late because the bus ___ already gone.",
                    "By the time we arrived, the film ___ started.",
                    "She couldn't pay because she ___ lost her purse."],
        "correct": "Abdulloh came in, sat down and opened his book.",
        "explanation": "<p><strong>Abdulloh came in, sat down and opened his book.</strong> is correct — "
                       "three actions in their natural order, so no extra tense is needed.<br><br>"
                       "<em>(<strong>Abdulloh came in, sat down and opened his book.</strong> toʻgʻri — "
                       "uchta harakat tabiiy tartibda, shuning uchun qoʻshimcha zamon kerak "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Ilgʻor told me he ___ the film twice already.</strong></p>",
        "choices": ["had seen", "has seen", "sees", "did see"],
        "correct": "had seen",
        "explanation": "<p><strong>had seen</strong> is correct — reporting a past statement pushes the "
                       "verb one step further back (you will meet this again in PE-62).<br><br>"
                       "<em>(<strong>had seen</strong> toʻgʻri — oʻtmishdagi gapni yetkazishda feʼl bir "
                       "pogʻona orqaga suriladi (buni PE-62 da yana koʻrasiz).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The house was quiet — everybody ___ to bed.</strong></p>",
        "choices": ["had gone", "went", "has gone", "was going"],
        "correct": "had gone",
        "explanation": "<p><strong>had gone</strong> is correct — the going to bed explains the earlier "
                       "quietness.<br><br>"
                       "<em>(<strong>had gone</strong> toʻgʻri — uxlashga yotish oldingi sukunatni "
                       "tushuntiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin didn't come to the party because nobody ___ him.</strong></p>",
        "choices": ["had invited", "invited", "has invited", "invites"],
        "correct": "had invited",
        "explanation": "<p><strong>had invited</strong> is correct — the missing invitation came before "
                       "the party.<br><br>"
                       "<em>(<strong>had invited</strong> toʻgʻri — taklif qilinmagani bazmdan oldin "
                       "sodir boʻlgan.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["When we arrived, the concert had already began.",
                    "When we arrived, the concert had already begun.",
                    "When we arrived, the concert began.",
                    "The concert had already begun when we arrived."],
        "correct": "When we arrived, the concert had already began.",
        "explanation": "<p><strong>… had already began.</strong> is the mistake — after <em>had</em> the "
                       "verb must be the third form: <em>begin → began → begun</em>.<br><br>"
                       "<em>(<strong>… had already began.</strong> xato — <em>had</em> dan keyin feʼl "
                       "uchinchi shaklda boʻlishi kerak: <em>begin → began → begun</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Marjona had finished her project before the deadline.",
                    "Marjona has finished her project before the deadline last week.",
                    "Marjona had finish her project before the deadline.",
                    "Marjona did had finished her project before the deadline."],
        "correct": "Marjona had finished her project before the deadline.",
        "explanation": "<p><strong>Marjona had finished her project before the deadline.</strong> is "
                       "correct — <em>had + V3</em>, with <em>before</em> marking the order.<br><br>"
                       "<em>(<strong>Marjona had finished her project before the deadline.</strong> "
                       "toʻgʻri — <em>had + V3</em>, tartibni esa <em>before</em> koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Why didn't you answer in the lesson, Davron?</p>"
                "<p><strong>Davron:</strong> ___</p>",
        "choices": ["I hadn't read that chapter, sorry.", "I haven't read that chapter, sorry.",
                    "I didn't have read that chapter, sorry.", "I hadn't readed that chapter, sorry."],
        "correct": "I hadn't read that chapter, sorry.",
        "explanation": "<p><strong>I hadn't read that chapter, sorry.</strong> is correct — the not "
                       "reading came before the lesson.<br><br>"
                       "<em>(<strong>I hadn't read that chapter, sorry.</strong> toʻgʻri — oʻqimagani "
                       "darsdan oldin sodir boʻlgan.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>both</strong> tenses are correct.</p>",
        "choices": ["When Afsona got to the hall, the competition had already started, "
                    "so she waited outside.",
                    "When Afsona had got to the hall, the competition already started, "
                    "so she had waited outside.",
                    "When Afsona got to the hall, the competition has already started, "
                    "so she had waited outside.",
                    "When Afsona had got to the hall, the competition had already started, "
                    "so she had waited outside."],
        "correct": "When Afsona got to the hall, the competition had already started, "
                   "so she waited outside.",
        "explanation": "<p><strong>got … had already started … waited</strong> is correct — only the "
                       "out-of-order event needs <em>had</em>; the rest of the story stays in the Past "
                       "Simple.<br><br>"
                       "<em>(<strong>got … had already started … waited</strong> toʻgʻri — faqat "
                       "tartibdan chiqqan voqeaga <em>had</em> kerak; hikoyaning qolgani Past Simple da "
                       "qoladi.)</em></p>",
    },
]


# =====================================================================
# PE-39 — Past Perfect Continuous
# =====================================================================

Q_PE39 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ for an hour when the bus finally came.</strong></p>",
        "choices": ["had been waiting", "have been waiting", "were waiting for", "waited"],
        "correct": "had been waiting",
        "explanation": "<p><strong>had been waiting</strong> is correct — the form is "
                       "<em>had been + verb-ing</em>, and it measures the activity up to a past "
                       "moment.<br><br>"
                       "<em>(<strong>had been waiting</strong> toʻgʻri — shakli <em>had been + "
                       "feʼl-ing</em> boʻlib, oʻtmishdagi bir daqiqagacha boʻlgan faoliyatni "
                       "oʻlchaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz's eyes were red because he ___ .</strong></p>",
        "choices": ["had been crying", "has been crying", "cried", "was crying"],
        "correct": "had been crying",
        "explanation": "<p><strong>had been crying</strong> is correct — the second job of this tense: "
                       "explaining the cause of a past situation.<br><br>"
                       "<em>(<strong>had been crying</strong> toʻgʻri — bu zamonning ikkinchi vazifasi: "
                       "oʻtmishdagi holatning sababini tushuntirish.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the form?</strong></p>",
        "choices": ["had been + verb-ing", "had + verb-ing", "has been + verb-ing", "was been + verb-ing"],
        "correct": "had been + verb-ing",
        "explanation": "<p><strong>had been + verb-ing</strong> is correct — three pieces, identical for "
                       "every person.<br><br>"
                       "<em>(<strong>had been + feʼl-ing</strong> toʻgʻri — uch boʻlak, har bir shaxs "
                       "uchun bir xil.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda was tired because she ___ all morning.</strong></p>",
        "choices": ["had been studying", "has been studying", "studied", "had studied"],
        "correct": "had been studying",
        "explanation": "<p><strong>had been studying</strong> is correct — a long activity that led to "
                       "the tiredness.<br><br>"
                       "<em>(<strong>had been studying</strong> toʻgʻri — charchoqqa olib kelgan uzoq "
                       "faoliyat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The ground was wet because it ___ all night.</strong></p>",
        "choices": ["had been raining", "has been raining", "was raining", "rained"],
        "correct": "had been raining",
        "explanation": "<p><strong>had been raining</strong> is correct — the rain came before the moment "
                       "we are describing.<br><br>"
                       "<em>(<strong>had been raining</strong> toʻgʻri — yomgʻir biz taʼriflayotgan "
                       "daqiqadan oldin yoqqan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ Korean for two years before she went to Seoul.</strong></p>",
        "choices": ["had been learning", "has been learning", "was learning", "learns"],
        "correct": "had been learning",
        "explanation": "<p><strong>had been learning</strong> is correct — the duration is measured up to "
                       "the trip.<br><br>"
                       "<em>(<strong>had been learning</strong> toʻgʻri — davomiylik safarga qadar "
                       "oʻlchanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ football for an hour when it started to snow.</strong></p>",
        "choices": ["had been playing", "has been playing", "played", "had played"],
        "correct": "had been playing",
        "explanation": "<p><strong>had been playing</strong> is correct — the hour is the activity that "
                       "was already running when the snow began.<br><br>"
                       "<em>(<strong>had been playing</strong> toʻgʻri — qor boshlanganda bu faoliyat "
                       "allaqachon bir soatdan beri davom etayotgan edi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference from the Past Continuous?</strong></p>",
        "choices": ["This one says how long the activity had lasted before that moment.",
                    "This one is about the future.",
                    "There is no difference at all.",
                    "This one is only for stative verbs."],
        "correct": "This one says how long the activity had lasted before that moment.",
        "explanation": "<p><strong>It says how long the activity had lasted.</strong> <em>He was "
                       "waiting</em> tells you what he was doing; <em>He had been waiting for an "
                       "hour</em> tells you how long.<br><br>"
                       "<em>(<strong>U faoliyat qancha davom etganini aytadi.</strong> <em>He was "
                       "waiting</em> nima qilayotganini, <em>He had been waiting for an hour</em> esa "
                       "qancha vaqtdan beri ekanini bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek ___ in that factory since 2018 when it closed.</strong></p>",
        "choices": ["had been working", "has been working", "was working", "worked"],
        "correct": "had been working",
        "explanation": "<p><strong>had been working</strong> is correct — <em>since</em> works with this "
                       "tense exactly as it does with the present perfect.<br><br>"
                       "<em>(<strong>had been working</strong> toʻgʻri — <em>since</em> bu zamon bilan "
                       "ham xuddi present perfect dagidek ishlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Firdavs ___ been sleeping well before the exams.</strong></p>",
        "choices": ["hadn't", "hasn't", "didn't", "wasn't"],
        "correct": "hadn't",
        "explanation": "<p><strong>hadn't</strong> is correct — the negative goes on <em>had</em>."
                       "<br><br><em>(<strong>hadn't</strong> toʻgʻri — inkor <em>had</em> ga "
                       "qoʻyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>How long ___ Javohir been waiting when you arrived?</strong></p>",
        "choices": ["had", "has", "did", "was"],
        "correct": "had",
        "explanation": "<p><strong>had</strong> is correct — <em>How long had + subject + been + "
                       "-ing</em>.<br><br>"
                       "<em>(<strong>had</strong> toʻgʻri — <em>How long had + subject + been + "
                       "-ing</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ our tests for three hours when the lights went "
                "out.</strong></p>",
        "choices": ["had been marking", "has been marking", "marked", "had marked"],
        "correct": "had been marking",
        "explanation": "<p><strong>had been marking</strong> is correct — the activity was running when "
                       "the interruption came.<br><br>"
                       "<em>(<strong>had been marking</strong> toʻgʻri — uzilish sodir boʻlganda faoliyat "
                       "davom etayotgan edi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda ___ that dictionary for years before she lost it.</strong></p>",
        "choices": ["had had", "had been having", "has had", "was having"],
        "correct": "had had",
        "explanation": "<p><strong>had had</strong> is correct — <em>have</em> meaning possession is "
                       "stative, so it takes the Simple even here.<br><br>"
                       "<em>(<strong>had had</strong> toʻgʻri — egalik maʼnosidagi <em>have</em> holat "
                       "feʼli, shuning uchun bu yerda ham Simple oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Madina ___ tired because she ___ all day.</strong></p>",
        "choices": ["was … had been travelling", "had been … was travelling",
                    "was … has been travelling", "had been … had travelled"],
        "correct": "was … had been travelling",
        "explanation": "<p><strong>was … had been travelling</strong> is correct — the past state first, "
                       "then the earlier activity that caused it.<br><br>"
                       "<em>(<strong>was … had been travelling</strong> toʻgʻri — avval oʻtmishdagi "
                       "holat, keyin unga sabab boʻlgan avvalgi faoliyat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh's clothes were covered in dust — he ___ in the garden.</strong></p>",
        "choices": ["had been working", "had worked", "has been working", "worked"],
        "correct": "had been working",
        "explanation": "<p><strong>had been working</strong> is correct — the dust is the trace of the "
                       "activity, exactly as in PE-36 but shifted into the past.<br><br>"
                       "<em>(<strong>had been working</strong> toʻgʻri — chang — faoliyatning izi, xuddi "
                       "PE-36 dagidek, faqat oʻtmishga surilgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence measures the <em>duration</em>?</strong></p>",
        "choices": ["Sirojiddin had been reading for two hours.",
                    "Sirojiddin had read two books.",
                    "Sirojiddin read a book.",
                    "Sirojiddin has read that book."],
        "correct": "Sirojiddin had been reading for two hours.",
        "explanation": "<p><strong>Sirojiddin had been reading for two hours.</strong> is correct — the "
                       "Continuous counts time, the Simple counts finished items.<br><br>"
                       "<em>(<strong>Sirojiddin had been reading for two hours.</strong> toʻgʻri — "
                       "Continuous vaqtni, Simple esa tugagan ishlarni sanaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Davron had been knowing her for years.",
                    "Davron had known her for years.",
                    "Davron had been waiting for hours.",
                    "Davron had waited patiently."],
        "correct": "Davron had been knowing her for years.",
        "explanation": "<p><strong>Davron had been knowing her for years.</strong> is the mistake — "
                       "<em>know</em> is stative in every tense.<br><br>"
                       "<em>(<strong>Davron had been knowing her for years.</strong> xato — <em>know</em> "
                       "barcha zamonlarda holat feʼli.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["They had been living there for ten years before they moved.",
                    "They had been live there for ten years before they moved.",
                    "They has been living there for ten years before they moved.",
                    "They had been living there since ten years before they moved."],
        "correct": "They had been living there for ten years before they moved.",
        "explanation": "<p><strong>They had been living there for ten years before they moved.</strong> "
                       "is correct — <em>had been + living</em>, and <em>for</em> with a length.<br><br>"
                       "<em>(<strong>They had been living there for ten years before they moved.</strong> "
                       "toʻgʻri — <em>had been + living</em>, uzunlik bilan esa <em>for</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Marjona:</strong> Why was Ilgʻor so happy yesterday?</p>"
                "<p><strong>Charos:</strong> ___</p>",
        "choices": ["He'd been preparing for that competition for months, and he won.",
                    "He's been preparing for that competition for months, and he won.",
                    "He had been prepare for that competition for months, and he won.",
                    "He was been preparing for that competition for months, and he won."],
        "correct": "He'd been preparing for that competition for months, and he won.",
        "explanation": "<p><strong>He'd been preparing … and he won.</strong> is correct — the months of "
                       "activity came before the victory. <em>He'd</em> = <em>he had</em>.<br><br>"
                       "<em>(<strong>He'd been preparing … and he won.</strong> toʻgʻri — oylab davom "
                       "etgan tayyorgarlik gʻalabadan oldin boʻlgan. <em>He'd</em> = <em>he "
                       "had</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Behruz had been running for twenty minutes when he stopped, "
                    "because he had hurt his knee.",
                    "Behruz has been running for twenty minutes when he stopped, "
                    "because he has hurt his knee.",
                    "Behruz had been run for twenty minutes when he had stopped, "
                    "because he had hurted his knee.",
                    "Behruz was been running for twenty minutes when he stopped, "
                    "because he had been hurting his knee."],
        "correct": "Behruz had been running for twenty minutes when he stopped, "
                   "because he had hurt his knee.",
        "explanation": "<p><strong>had been running … stopped … had hurt …</strong> is correct — a "
                       "measured activity, the moment that ended it, and an earlier single event."
                       "<br><br><em>(<strong>had been running … stopped … had hurt …</strong> toʻgʻri — "
                       "oʻlchangan faoliyat, uni tugatgan daqiqa va undan ham avvalgi bitta "
                       "voqea.)</em></p>",
    },
]


# =====================================================================
# PE-40 — Future Perfect and Future Perfect Continuous
# =====================================================================

Q_PE40 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>By next June Marjona ___ school.</strong></p>",
        "choices": ["will have finished", "will finish", "has finished", "will be finishing"],
        "correct": "will have finished",
        "explanation": "<p><strong>will have finished</strong> is correct — the form is "
                       "<em>will have + V3</em>: finished before a future moment.<br><br>"
                       "<em>(<strong>will have finished</strong> toʻgʻri — shakli <em>will have + V3</em>: "
                       "kelasi bir daqiqadan oldin tugagan boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which word is the classic signal for this tense?</strong></p>",
        "choices": ["by", "since", "ago", "while"],
        "correct": "by",
        "explanation": "<p><strong>by</strong> is correct — <em>by June, by five o'clock, by the time you "
                       "arrive</em>: a deadline to look back from.<br><br>"
                       "<em>(<strong>by</strong> toʻgʻri — <em>by June, by five o'clock, by the time you "
                       "arrive</em>: orqaga qarash uchun muddat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ his project by Friday.</strong></p>",
        "choices": ["will have completed", "will completed", "has completed", "completes"],
        "correct": "will have completed",
        "explanation": "<p><strong>will have completed</strong> is correct — after <em>will have</em> the "
                       "verb takes its third form.<br><br>"
                       "<em>(<strong>will have completed</strong> toʻgʻri — <em>will have</em> dan keyin "
                       "feʼl uchinchi shaklini oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>By the time Rozimurod teacher ___ , we will have finished the "
                "exercise.</strong></p>",
        "choices": ["arrives", "will arrive", "will have arrived", "arrived"],
        "correct": "arrives",
        "explanation": "<p><strong>arrives</strong> is correct — the <em>by the time</em> rule: after it "
                       "we use the present, never <em>will</em>, exactly as in PE-26.<br><br>"
                       "<em>(<strong>arrives</strong> toʻgʻri — <em>by the time</em> qoidasi: undan keyin "
                       "hozirgi zamon ishlatiladi, <em>will</em> emas, xuddi PE-26 dagidek.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>By 2030 Iroda ___ at that hospital for ten years.</strong></p>",
        "choices": ["will have been working", "will have worked out",
                    "will be working since", "has been working"],
        "correct": "will have been working",
        "explanation": "<p><strong>will have been working</strong> is correct — "
                       "<em>will have been + verb-ing</em> measures how long, up to a future "
                       "moment.<br><br>"
                       "<em>(<strong>will have been working</strong> toʻgʻri — <em>will have been + "
                       "feʼl-ing</em> kelasi daqiqagacha qancha vaqt oʻtganini oʻlchaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference between the two forms?</strong></p>",
        "choices": ["will have + V3 = finished · will have been + -ing = how long",
                    "will have + V3 = how long · will have been + -ing = finished",
                    "They mean exactly the same.",
                    "One is past, the other is present."],
        "correct": "will have + V3 = finished · will have been + -ing = how long",
        "explanation": "<p><strong>will have + V3 = finished · will have been + -ing = how long</strong> "
                       "is correct — the same result/activity split as PE-37, moved into the "
                       "future.<br><br>"
                       "<em>(<strong>will have + V3 = tugagan · will have been + -ing = qancha "
                       "vaqt</strong> toʻgʻri — PE-37 dagi natija/faoliyat boʻlinishi, kelasi zamonga "
                       "koʻchirilgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Don't call at eight — Charos ___ home by then.</strong></p>",
        "choices": ["will have gone", "will go", "goes", "has gone"],
        "correct": "will have gone",
        "explanation": "<p><strong>will have gone</strong> is correct — by eight the leaving will already "
                       "be complete.<br><br>"
                       "<em>(<strong>will have gone</strong> toʻgʻri — soat sakkizga kelib ketish "
                       "allaqachon tugagan boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>By the end of this month Samandar ___ fifty books this year.</strong></p>",
        "choices": ["will have read", "will read", "will have been reading", "reads"],
        "correct": "will have read",
        "explanation": "<p><strong>will have read</strong> is correct — a counted number of finished "
                       "books takes the Simple form.<br><br>"
                       "<em>(<strong>will have read</strong> toʻgʻri — oʻqib tugatilgan kitoblarning "
                       "sanalgan soni Simple shaklini oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>By six o'clock Elbek ___ for four hours without a break.</strong></p>",
        "choices": ["will have been studying", "will have studied four",
                    "will be studied", "studies"],
        "correct": "will have been studying",
        "explanation": "<p><strong>will have been studying</strong> is correct — <em>four hours</em> is a "
                       "duration, not a quantity of finished work.<br><br>"
                       "<em>(<strong>will have been studying</strong> toʻgʻri — <em>four hours</em> — "
                       "davomiylik, bajarilgan ishning miqdori emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Firdavs ___ have finished by tomorrow — the work is too big.</strong></p>",
        "choices": ["won't", "willn't", "doesn't", "hasn't"],
        "correct": "won't",
        "explanation": "<p><strong>won't</strong> is correct — <em>won't have + V3</em>.<br><br>"
                       "<em>(<strong>won't</strong> toʻgʻri — <em>won't have + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ you have finished the exercise by the bell?</strong></p>",
        "choices": ["Will", "Do", "Have", "Are"],
        "correct": "Will",
        "explanation": "<p><strong>Will</strong> is correct — <em>Will + subject + have + V3</em>."
                       "<br><br><em>(<strong>Will</strong> toʻgʻri — <em>Will + subject + have + "
                       "V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>By next spring Javohir ___ the guitar for three years.</strong></p>",
        "choices": ["will have been playing", "will have played three",
                    "is playing", "will play"],
        "correct": "will have been playing",
        "explanation": "<p><strong>will have been playing</strong> is correct — three years of activity "
                       "counted up to a future point.<br><br>"
                       "<em>(<strong>will have been playing</strong> toʻgʻri — kelasi nuqtaga qadar "
                       "sanalgan uch yillik faoliyat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which verb cannot take <em>will have been + -ing</em>?</strong></p>",
        "choices": ["know", "wait", "live", "work"],
        "correct": "know",
        "explanation": "<p><strong>know</strong> is correct — stative verbs stay simple: <em>By June I "
                       "will have known him for ten years</em>.<br><br>"
                       "<em>(<strong>know</strong> toʻgʻri — holat feʼllari Simple da qoladi: <em>By June "
                       "I will have known him for ten years</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>By the time we ___ , the film ___ .</strong></p>",
        "choices": ["arrive … will have started", "will arrive … will have started",
                    "arrive … has started", "will arrive … started"],
        "correct": "arrive … will have started",
        "explanation": "<p><strong>arrive … will have started</strong> is correct — present after "
                       "<em>by the time</em>, Future Perfect in the main half.<br><br>"
                       "<em>(<strong>arrive … will have started</strong> toʻgʻri — <em>by the time</em> "
                       "dan keyin hozirgi zamon, asosiy qismda esa Future Perfect.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda ___ her homework by nine, so she can watch the "
                "match.</strong></p>",
        "choices": ["will have done", "will have been doing", "has done", "does"],
        "correct": "will have done",
        "explanation": "<p><strong>will have done</strong> is correct — completion is the point, not "
                       "duration.<br><br>"
                       "<em>(<strong>will have done</strong> toʻgʻri — bu yerda muhimi tugallanish, "
                       "davomiylik emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In August Abdulloh and Ilgʻor ___ in this school for six "
                "years.</strong></p>",
        "choices": ["will have been studying", "will have studied six",
                    "have been studying", "study"],
        "correct": "will have been studying",
        "explanation": "<p><strong>will have been studying</strong> is correct — the duration reaches a "
                       "future moment.<br><br>"
                       "<em>(<strong>will have been studying</strong> toʻgʻri — davomiylik kelasi bir "
                       "daqiqagacha yetadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["By ten o'clock we will have arrive.", "By ten o'clock we will have arrived.",
                    "By ten o'clock we won't have arrived.", "Will we have arrived by ten o'clock?"],
        "correct": "By ten o'clock we will have arrive.",
        "explanation": "<p><strong>By ten o'clock we will have arrive.</strong> is the mistake — after "
                       "<em>will have</em> the third form is required: <em>arrived</em>.<br><br>"
                       "<em>(<strong>By ten o'clock we will have arrive.</strong> xato — <em>will "
                       "have</em> dan keyin uchinchi shakl talab qilinadi: <em>arrived</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["By the time you read this, Madina will have left.",
                    "By the time you will read this, Madina will have left.",
                    "By the time you read this, Madina will left.",
                    "By the time you will read this, Madina has left."],
        "correct": "By the time you read this, Madina will have left.",
        "explanation": "<p><strong>By the time you read this, Madina will have left.</strong> is correct "
                       "— the present after <em>by the time</em>, and <em>will have + V3</em> in the "
                       "main half.<br><br>"
                       "<em>(<strong>By the time you read this, Madina will have left.</strong> "
                       "toʻgʻri — <em>by the time</em> dan keyin hozirgi zamon, asosiy qismda esa "
                       "<em>will have + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Can you hand in the essay on Monday, "
                "Sirojiddin?</p>"
                "<p><strong>Sirojiddin:</strong> Yes — ___</p>",
        "choices": ["I'll have written it by Sunday evening.",
                    "I'll write it by Sunday evening already.",
                    "I have written it by Sunday evening.",
                    "I'll have been writing it by Sunday evening."],
        "correct": "I'll have written it by Sunday evening.",
        "explanation": "<p><strong>I'll have written it by Sunday evening.</strong> is correct — the "
                       "essay will be complete before that deadline.<br><br>"
                       "<em>(<strong>I'll have written it by Sunday evening.</strong> toʻgʻri — insho "
                       "oʻsha muddatdan oldin tayyor boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>both</strong> forms are correct.</p>",
        "choices": ["By December Afsona will have passed two exams and will have been studying "
                    "here for a year.",
                    "By December Afsona will have pass two exams and will have been study here "
                    "for a year.",
                    "By December Afsona will have been passing two exams and will have studied "
                    "here for a year ago.",
                    "By December Afsona will pass two exams and will be studying here since a year."],
        "correct": "By December Afsona will have passed two exams and will have been studying "
                   "here for a year.",
        "explanation": "<p><strong>will have passed … will have been studying …</strong> is correct — "
                       "counted results in the Simple, duration in the Continuous.<br><br>"
                       "<em>(<strong>will have passed … will have been studying …</strong> toʻgʻri — "
                       "sanalgan natijalar Simple da, davomiylik esa Continuous da.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-36 Practice: Present Perfect Continuous",
        "tutorial":    "PE-36:",
        "description": "PE-36 darsiga 20 savol: have/has + been + -ing, hali davom etayotgan yoki "
                       "endigina toʻxtagan faoliyat, for va since, hamda -ing olmaydigan feʼllar. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE36,
    },
    {
        "title":       "PE-37 Practice: Present Perfect Simple vs Continuous",
        "tutorial":    "PE-37:",
        "description": "PE-37 darsiga 20 savol: natija yoki faoliyat, How many va How long, ikki "
                       "shakl ham toʻgʻri boʻladigan holatlar va faqat Simple oladigan feʼllar. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE37,
    },
    {
        "title":       "PE-38 Practice: Past Perfect: The Past Before the Past",
        "tutorial":    "PE-38:",
        "description": "PE-38 darsiga 20 savol: had + V3, ikki oʻtgan voqeaning tartibi, "
                       "when/after/before/by the time bilan ishlatilishi va qachon kerak "
                       "emasligi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE38,
    },
    {
        "title":       "PE-39 Practice: Past Perfect Continuous",
        "tutorial":    "PE-39:",
        "description": "PE-39 darsiga 20 savol: had been + -ing, oʻtgan daqiqagacha boʻlgan "
                       "davomiylik, oʻtmishdagi holatning sababi va Past Continuous dan farqi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE39,
    },
    {
        "title":       "PE-40 Practice: Future Perfect and Future Perfect Continuous",
        "tutorial":    "PE-40:",
        "description": "PE-40 darsiga 20 savol: will have + V3 va will have been + -ing, by signal "
                       "soʻzi hamda by the time dan keyin hozirgi zamon qoidasi. Javoblar ingliz va "
                       "oʻzbek tilida izohlangan.",
        "questions":   Q_PE40,
    },
]
