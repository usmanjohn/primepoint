# -*- coding: utf-8 -*-
"""Prime English practices — PE-26 … PE-30 (the futures).

Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_26_30.py --master=prime
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
# PE-26 — Future with "will"
# =====================================================================

Q_PE26 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Don't worry, I ___ help you with your homework.</strong></p>",
        "choices": ["will", "will to", "am will", "wills"],
        "correct": "will",
        "explanation": "<p><strong>will</strong> is correct — <em>will + base verb</em>, with no "
                       "<em>to</em> and no <em>-s</em>.<br><br>"
                       "<em>(<strong>will</strong> toʻgʻri — <em>will + asosiy feʼl</em>, <em>to</em> "
                       "ham, <em>-s</em> ham qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ be fifteen next month.</strong></p>",
        "choices": ["will", "wills", "will to", "is will"],
        "correct": "will",
        "explanation": "<p><strong>will</strong> is correct — the form never changes, not even for "
                       "<em>he / she / it</em>.<br><br>"
                       "<em>(<strong>will</strong> toʻgʻri — bu shakl hech qachon oʻzgarmaydi, hatto "
                       "<em>he / she / it</em> uchun ham.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The phone is ringing. — ___ get it!</strong></p>",
        "choices": ["I'll", "I'm going to", "I get", "I am getting"],
        "correct": "I'll",
        "explanation": "<p><strong>I'll</strong> is correct — an instant decision, made at the moment of "
                       "speaking. This is the heart of <em>will</em>.<br><br>"
                       "<em>(<strong>I'll</strong> toʻgʻri — gapirayotgan paytda qabul qilingan bir "
                       "zumlik qaror. <em>Will</em> ning asosiy maʼnosi shu.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>I promise I ___ forget your birthday.</strong></p>",
        "choices": ["won't", "willn't", "don't will", "will not to"],
        "correct": "won't",
        "explanation": "<p><strong>won't</strong> is correct — <em>will not</em> shortens to "
                       "<em>won't</em>, which is irregular but the only correct form.<br><br>"
                       "<em>(<strong>won't</strong> toʻgʻri — <em>will not</em> <em>won't</em> ga "
                       "qisqaradi; gʻalati, lekin yagona toʻgʻri shakl.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ you help me carry these books, Behruz?</strong></p>",
        "choices": ["Will", "Do", "Are", "Does"],
        "correct": "Will",
        "explanation": "<p><strong>Will</strong> is correct — <em>will</em> jumps in front of the subject "
                       "to make a question or a polite request.<br><br>"
                       "<em>(<strong>Will</strong> toʻgʻri — savol yoki xushmuomala iltimos uchun "
                       "<em>will</em> subject oldiga chiqadi.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Will you come to my birthday party? — Yes, ___ .</strong></p>",
        "choices": ["I will", "I'll", "I do", "I am"],
        "correct": "I will",
        "explanation": "<p><strong>I will</strong> is correct — a positive short answer is never "
                       "shortened to <em>I'll</em>.<br><br>"
                       "<em>(<strong>I will</strong> toʻgʻri — qisqa tasdiq javob hech qachon "
                       "<em>I'll</em> ga qisqartirilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I think Iroda ___ pass the exam easily.</strong></p>",
        "choices": ["will", "is going to be", "will to", "goes to"],
        "correct": "will",
        "explanation": "<p><strong>will</strong> is correct — an opinion or prediction, especially after "
                       "<em>I think, I'm sure, maybe, probably</em>.<br><br>"
                       "<em>(<strong>will</strong> toʻgʻri — fikr yoki taxmin, ayniqsa <em>I think, I'm "
                       "sure, maybe, probably</em> dan keyin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>That bag looks heavy. ___ I carry it for you?</strong></p>",
        "choices": ["Shall", "Do", "Am", "Will I to"],
        "correct": "Shall",
        "explanation": "<p><strong>Shall</strong> is correct — <em>Shall I …?</em> is the natural way to "
                       "offer help. <em>Will I …?</em> sounds like you are asking about your own "
                       "future.<br><br>"
                       "<em>(<strong>Shall</strong> toʻgʻri — <em>Shall I …?</em> yordam taklif qilishning "
                       "tabiiy shakli. <em>Will I …?</em> esa oʻz kelajagi haqida soʻrayotgandek "
                       "eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin ___ eighteen in 2030.</strong></p>",
        "choices": ["will be", "will is", "is will be", "will being"],
        "correct": "will be",
        "explanation": "<p><strong>will be</strong> is correct — a future fact that nobody can change. "
                       "After <em>will</em> the verb <em>be</em> stays in its base form.<br><br>"
                       "<em>(<strong>will be</strong> toʻgʻri — hech kim oʻzgartira olmaydigan kelasi "
                       "zamon fakti. <em>Will</em> dan keyin <em>be</em> asosiy shaklda qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher says the test ___ easy if we revise.</strong></p>",
        "choices": ["will be", "will", "is going", "will been"],
        "correct": "will be",
        "explanation": "<p><strong>will be</strong> is correct — <em>will</em> always needs a verb after "
                       "it, and here that verb is <em>be</em>.<br><br>"
                       "<em>(<strong>will be</strong> toʻgʻri — <em>will</em> dan keyin doim feʼl kerak, "
                       "bu yerda esa u <em>be</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is a <em>promise</em>?</strong></p>",
        "choices": ["I'll never tell anybody your secret.",
                    "I'm meeting Charos at four.",
                    "I'm going to study medicine.",
                    "The train leaves at six."],
        "correct": "I'll never tell anybody your secret.",
        "explanation": "<p><strong>I'll never tell anybody your secret.</strong> is correct — promises "
                       "belong to <em>will</em>.<br><br>"
                       "<em>(<strong>I'll never tell anybody your secret.</strong> toʻgʻri — vaʼdalar "
                       "<em>will</em> ga tegishli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ my grandmother tomorrow if I have time.</strong></p>",
        "choices": ["will visit", "will visiting", "am will visit", "will to visit"],
        "correct": "will visit",
        "explanation": "<p><strong>will visit</strong> is correct — base verb after <em>will</em>."
                       "<br><br><em>(<strong>will visit</strong> toʻgʻri — <em>will</em> dan keyin asosiy "
                       "feʼl.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I'll call you when I ___ home.</strong></p>",
        "choices": ["get", "will get", "am getting", "will be getting"],
        "correct": "get",
        "explanation": "<p><strong>get</strong> is correct — this is the one place <em>will</em> is "
                       "forbidden: after <em>when, if, before, after, until, as soon as</em> English uses "
                       "the present, even about the future.<br><br>"
                       "<em>(<strong>get</strong> toʻgʻri — <em>will</em> ishlatilmaydigan yagona joy: "
                       "<em>when, if, before, after, until, as soon as</em> dan keyin ingliz tili kelasi "
                       "zamon haqida gapirsa ham hozirgi zamonni ishlatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If it ___ tomorrow, we will stay at home.</strong></p>",
        "choices": ["rains", "will rain", "is raining", "will be raining"],
        "correct": "rains",
        "explanation": "<p><strong>rains</strong> is correct — after <em>if</em> the present is used, and "
                       "<em>will</em> stays in the other half of the sentence.<br><br>"
                       "<em>(<strong>rains</strong> toʻgʻri — <em>if</em> dan keyin hozirgi zamon "
                       "ishlatiladi, <em>will</em> esa gapning ikkinchi qismida qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir is tired. He ___ go to bed early tonight.</strong></p>",
        "choices": ["will probably", "probably will not", "will probably not", "probably won't be"],
        "correct": "will probably",
        "explanation": "<p><strong>will probably</strong> is correct — the adverb sits between "
                       "<em>will</em> and the verb: <em>will probably go</em>.<br><br>"
                       "<em>(<strong>will probably</strong> toʻgʻri — ravish <em>will</em> va feʼl orasida "
                       "turadi: <em>will probably go</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which short form is correct?</strong></p>",
        "choices": ["they'll", "they'will", "theyl'l", "they'ill"],
        "correct": "they'll",
        "explanation": "<p><strong>they'll</strong> is correct — the apostrophe replaces <em>wi</em>: "
                       "<em>I'll, you'll, he'll, we'll, they'll</em>.<br><br>"
                       "<em>(<strong>they'll</strong> toʻgʻri — apostrof <em>wi</em> ni almashtiradi: "
                       "<em>I'll, you'll, he'll, we'll, they'll</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Elbek will helps us tomorrow.", "Elbek will help us tomorrow.",
                    "Elbek won't help us tomorrow.", "Will Elbek help us tomorrow?"],
        "correct": "Elbek will helps us tomorrow.",
        "explanation": "<p><strong>Elbek will helps us tomorrow.</strong> is the mistake — after "
                       "<em>will</em> the verb never takes <em>-s</em>.<br><br>"
                       "<em>(<strong>Elbek will helps us tomorrow.</strong> xato — <em>will</em> dan "
                       "keyin feʼl hech qachon <em>-s</em> olmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["I'll phone you as soon as I arrive.",
                    "I'll phone you as soon as I will arrive.",
                    "I phone you as soon as I will arrive.",
                    "I'll phone you as soon as I am arriving."],
        "correct": "I'll phone you as soon as I arrive.",
        "explanation": "<p><strong>I'll phone you as soon as I arrive.</strong> is correct — "
                       "<em>will</em> in the main half, the present after <em>as soon as</em>.<br><br>"
                       "<em>(<strong>I'll phone you as soon as I arrive.</strong> toʻgʻri — asosiy qismda "
                       "<em>will</em>, <em>as soon as</em> dan keyin esa hozirgi zamon.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Shaxzoda:</strong> This box is too heavy for me.</p>"
                "<p><strong>Davron:</strong> ___</p>",
        "choices": ["Don't worry, I'll carry it.", "Don't worry, I carry it.",
                    "Don't worry, I am carrying it now.", "Don't worry, I will carrying it."],
        "correct": "Don't worry, I'll carry it.",
        "explanation": "<p><strong>Don't worry, I'll carry it.</strong> is correct — an offer decided at "
                       "this second.<br><br>"
                       "<em>(<strong>Don't worry, I'll carry it.</strong> toʻgʻri — shu daqiqada qabul "
                       "qilingan taklif.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["I think Firdavs will win, but he won't be happy until he sees the results.",
                    "I think Firdavs will wins, but he willn't be happy until he will see the results.",
                    "I think Firdavs will win, but he won't be happy until he will see the results.",
                    "I think Firdavs wills win, but he won't to be happy until he sees the results."],
        "correct": "I think Firdavs will win, but he won't be happy until he sees the results.",
        "explanation": "<p><strong>will win … won't be … until he sees …</strong> is correct — base verb "
                       "after <em>will</em>, <em>won't</em> for the negative, and the present after "
                       "<em>until</em>.<br><br>"
                       "<em>(<strong>will win … won't be … until he sees …</strong> toʻgʻri — "
                       "<em>will</em> dan keyin asosiy feʼl, inkor uchun <em>won't</em>, <em>until</em> "
                       "dan keyin esa hozirgi zamon.)</em></p>",
    },
]


# =====================================================================
# PE-27 — Future with "be going to"
# =====================================================================

Q_PE27 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ visit our grandparents this weekend. We bought the tickets "
                "last week.</strong></p>",
        "choices": ["are going to", "will", "go to", "are going"],
        "correct": "are going to",
        "explanation": "<p><strong>are going to</strong> is correct — the decision was made before "
                       "speaking, and the tickets prove it.<br><br>"
                       "<em>(<strong>are going to</strong> toʻgʻri — qaror gapirishdan oldin qabul "
                       "qilingan, chiptalar buni tasdiqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ study medicine. She decided last year.</strong></p>",
        "choices": ["is going to", "will", "goes to", "is going"],
        "correct": "is going to",
        "explanation": "<p><strong>is going to</strong> is correct — one person, and the plan already "
                       "exists.<br><br>"
                       "<em>(<strong>is going to</strong> toʻgʻri — bitta shaxs va reja allaqachon "
                       "bor.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Look at those black clouds! It ___ rain.</strong></p>",
        "choices": ["is going to", "will", "goes to", "is raining"],
        "correct": "is going to",
        "explanation": "<p><strong>is going to</strong> is correct — a prediction based on evidence you "
                       "can see right now.<br><br>"
                       "<em>(<strong>is going to</strong> toʻgʻri — hozir koʻrinib turgan dalilga "
                       "asoslangan taxmin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ going to buy a new phone next month.</strong></p>",
        "choices": ["am", "is", "are", "will"],
        "correct": "am",
        "explanation": "<p><strong>am</strong> is correct — the structure starts with "
                       "<em>am / is / are</em>, and <em>I</em> takes <em>am</em>.<br><br>"
                       "<em>(<strong>am</strong> toʻgʻri — qurilish <em>am / is / are</em> bilan "
                       "boshlanadi, <em>I</em> esa <em>am</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Behruz ___ going to come — he has to work.</strong></p>",
        "choices": ["isn't", "doesn't", "won't", "not"],
        "correct": "isn't",
        "explanation": "<p><strong>isn't</strong> is correct — the negative sits on "
                       "<em>am / is / are</em>, exactly as in PE-6.<br><br>"
                       "<em>(<strong>isn't</strong> toʻgʻri — inkor <em>am / is / are</em> ga qoʻyiladi, "
                       "xuddi PE-6 dagidek.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ you going to watch the match tonight?</strong></p>",
        "choices": ["Are", "Do", "Will", "Does"],
        "correct": "Are",
        "explanation": "<p><strong>Are</strong> is correct — the <em>to be</em> part moves to the front."
                       "<br><br><em>(<strong>Are</strong> toʻgʻri — <em>to be</em> qismi gap boshiga "
                       "chiqadi.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Is Ilgʻor going to join us? — No, ___ .</strong></p>",
        "choices": ["he isn't", "he doesn't", "he won't be", "he not"],
        "correct": "he isn't",
        "explanation": "<p><strong>he isn't</strong> is correct — the short answer repeats "
                       "<em>am / is / are</em>.<br><br>"
                       "<em>(<strong>he isn't</strong> toʻgʻri — qisqa javobda <em>am / is / are</em> "
                       "takrorlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Careful! You ___ drop those plates!</strong></p>",
        "choices": ["are going to", "will", "go to", "are dropping"],
        "correct": "are going to",
        "explanation": "<p><strong>are going to</strong> is correct — the evidence is in front of your "
                       "eyes: the plates are already slipping.<br><br>"
                       "<em>(<strong>are going to</strong> toʻgʻri — dalil koʻz oldingizda: likopchalar "
                       "allaqachon sirgʻalib ketmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona and Madina ___ open a small shop together.</strong></p>",
        "choices": ["are going to", "is going to", "am going to", "goes to"],
        "correct": "are going to",
        "explanation": "<p><strong>are going to</strong> is correct — two people make a plural "
                       "subject.<br><br>"
                       "<em>(<strong>are going to</strong> toʻgʻri — ikki kishi koʻplikdagi subject hosil "
                       "qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What ___ you going to do after school today?</strong></p>",
        "choices": ["are", "do", "will", "is"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct — <em>Wh- + am/is/are + subject + going "
                       "to</em>.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri — <em>Wh- + am/is/are + subject + going "
                       "to</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>After the exams Samandar ___ to Tashkent for a week.</strong></p>",
        "choices": ["is going", "is going to go", "will going", "goes to go"],
        "correct": "is going",
        "explanation": "<p><strong>is going</strong> is correct. <em>Going to go</em> is grammatically "
                       "fine but sounds heavy, so English simply says <em>is going</em>.<br><br>"
                       "<em>(<strong>is going</strong> toʻgʻri. <em>Going to go</em> grammatik jihatdan "
                       "xato emas, lekin ogʻir eshitiladi, shuning uchun oddiy <em>is going</em> "
                       "deyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence shows a plan made <em>before</em> speaking?</strong></p>",
        "choices": ["I'm going to learn Korean next year.",
                    "I'll answer the phone.",
                    "I'll help you with that bag.",
                    "I think I'll have tea."],
        "correct": "I'm going to learn Korean next year.",
        "explanation": "<p><strong>I'm going to learn Korean next year.</strong> is correct — the others "
                       "are all decisions made at the moment of speaking.<br><br>"
                       "<em>(<strong>I'm going to learn Korean next year.</strong> toʻgʻri — qolganlari "
                       "gapirayotgan paytda qabul qilingan qarorlar.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ give us a test on Friday. He told us "
                "yesterday.</strong></p>",
        "choices": ["is going to", "will", "goes to", "is going"],
        "correct": "is going to",
        "explanation": "<p><strong>is going to</strong> is correct — the decision was announced "
                       "yesterday, so it already existed.<br><br>"
                       "<em>(<strong>is going to</strong> toʻgʻri — qaror kecha aytilgan, yaʼni "
                       "allaqachon mavjud edi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I'm going ___ my room this evening.</strong></p>",
        "choices": ["to clean", "clean", "cleaning", "to cleaning"],
        "correct": "to clean",
        "explanation": "<p><strong>to clean</strong> is correct — the base verb follows "
                       "<em>going to</em>.<br><br>"
                       "<em>(<strong>to clean</strong> toʻgʻri — <em>going to</em> dan keyin asosiy feʼl "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sherbek ___ not going to play in the match. He hurt his leg.</strong></p>",
        "choices": ["is", "does", "will", "are"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — <em>is not going to</em>, with the negative on "
                       "the <em>to be</em> part.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — <em>is not going to</em>, inkor <em>to be</em> "
                       "qismiga qoʻyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh ___ his room tomorrow — his mother asked him "
                "yesterday.</strong></p>",
        "choices": ["is going to paint", "will paint", "paints", "painted"],
        "correct": "is going to paint",
        "explanation": "<p><strong>is going to paint</strong> is correct — the plan came from yesterday's "
                       "conversation.<br><br>"
                       "<em>(<strong>is going to paint</strong> toʻgʻri — reja kechagi suhbatdan "
                       "kelib chiqqan.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Iroda going to buy a new bag.", "Iroda is going to buy a new bag.",
                    "Iroda isn't going to buy a new bag.", "Is Iroda going to buy a new bag?"],
        "correct": "Iroda going to buy a new bag.",
        "explanation": "<p><strong>Iroda going to buy a new bag.</strong> is the mistake — <em>is</em> is "
                       "missing. The structure always needs its <em>am / is / are</em>.<br><br>"
                       "<em>(<strong>Iroda going to buy a new bag.</strong> xato — <em>is</em> yoʻq. Bu "
                       "qurilishga doim <em>am / is / are</em> kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Are you going to help me?", "Do you going to help me?",
                    "Are you going to helping me?", "You are going help me?"],
        "correct": "Are you going to help me?",
        "explanation": "<p><strong>Are you going to help me?</strong> is correct — <em>Are + subject + "
                       "going to + base verb</em>.<br><br>"
                       "<em>(<strong>Are you going to help me?</strong> toʻgʻri — <em>Are + subject + "
                       "going to + asosiy feʼl</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> What are you going to be in the future, "
                "Javohir?</p>"
                "<p><strong>Javohir:</strong> ___</p>",
        "choices": ["I'm going to be a programmer.", "I going to be a programmer.",
                    "I'm going to being a programmer.", "I will going to be a programmer."],
        "correct": "I'm going to be a programmer.",
        "explanation": "<p><strong>I'm going to be a programmer.</strong> is correct — an existing plan, "
                       "with the base verb <em>be</em>.<br><br>"
                       "<em>(<strong>I'm going to be a programmer.</strong> toʻgʻri — mavjud reja, asosiy "
                       "feʼl <em>be</em> bilan.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Firdavs is going to take the exam in June, but he isn't going to study abroad.",
                    "Firdavs going to take the exam in June, but he doesn't going to study abroad.",
                    "Firdavs is going to taking the exam in June, but he isn't go to study abroad.",
                    "Firdavs will going to take the exam in June, but he won't going to study abroad."],
        "correct": "Firdavs is going to take the exam in June, but he isn't going to study abroad.",
        "explanation": "<p><strong>is going to take … isn't going to study …</strong> is correct — the "
                       "<em>to be</em> part carries the negative, and both verbs stay bare.<br><br>"
                       "<em>(<strong>is going to take … isn't going to study …</strong> toʻgʻri — inkorni "
                       "<em>to be</em> qismi oladi, ikki feʼl esa oʻzgarmaydi.)</em></p>",
    },
]


# =====================================================================
# PE-28 — Present Continuous for Future Arrangements
# =====================================================================

Q_PE28 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ the dentist at three o'clock tomorrow.</strong></p>",
        "choices": ["am seeing", "see", "will seeing", "am see"],
        "correct": "am seeing",
        "explanation": "<p><strong>am seeing</strong> is correct — an appointment written in a diary is a "
                       "fixed arrangement, so English uses the Present Continuous.<br><br>"
                       "<em>(<strong>am seeing</strong> toʻgʻri — kundalikka yozilgan uchrashuv qatʼiy "
                       "kelishuv, shuning uchun ingliz tilida Present Continuous "
                       "ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What makes something an <em>arrangement</em>?</strong></p>",
        "choices": ["The time and place are already agreed with somebody.",
                    "You have only just thought of it.",
                    "You hope it will happen.",
                    "It is a general fact about the future."],
        "correct": "The time and place are already agreed with somebody.",
        "explanation": "<p><strong>The time and place are already agreed with somebody.</strong> is "
                       "correct — somebody is expecting you.<br><br>"
                       "<em>(<strong>Vaqt va joy allaqachon kimsa bilan kelishilgan.</strong> toʻgʻri — "
                       "kimdir sizni kutmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ a party on Saturday. Sherbek is coming too.</strong></p>",
        "choices": ["are having", "have", "will having", "are have"],
        "correct": "are having",
        "explanation": "<p><strong>are having</strong> is correct — the party is organised and the guests "
                       "are invited.<br><br>"
                       "<em>(<strong>are having</strong> toʻgʻri — bazm uyushtirilgan va mehmonlar taklif "
                       "qilingan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ to Bukhara on Friday. She has already bought her "
                "ticket.</strong></p>",
        "choices": ["is travelling", "travels", "will travelling", "is travel"],
        "correct": "is travelling",
        "explanation": "<p><strong>is travelling</strong> is correct — the ticket is the proof that it is "
                       "arranged.<br><br>"
                       "<em>(<strong>is travelling</strong> toʻgʻri — chipta bu ishning kelishilganini "
                       "tasdiqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which words tell you “I'm meeting Iroda” is about the "
                "<em>future</em>?</strong></p>",
        "choices": ["a future time expression like “at four tomorrow”",
                    "the word “meeting” itself",
                    "the subject “I”",
                    "nothing — it is always about now"],
        "correct": "a future time expression like “at four tomorrow”",
        "explanation": "<p><strong>a future time expression like “at four tomorrow”</strong> is correct — "
                       "the tense is the same as PE-12; only the time word tells you which meaning is "
                       "intended.<br><br>"
                       "<em>(<strong>“at four tomorrow” kabi kelasi zamon ifodasi</strong> toʻgʻri — "
                       "zamon PE-12 dagi bilan bir xil; qaysi maʼno koʻzda tutilganini faqat vaqt soʻzi "
                       "koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ his cousin at the airport tonight.</strong></p>",
        "choices": ["is meeting", "meets", "will meeting", "meeting"],
        "correct": "is meeting",
        "explanation": "<p><strong>is meeting</strong> is correct — <em>meet</em> is one of the verbs that "
                       "appear in this structure most often, along with <em>come, go, see, play, "
                       "have</em>.<br><br>"
                       "<em>(<strong>is meeting</strong> toʻgʻri — <em>meet</em> bu qurilishda eng koʻp "
                       "uchraydigan feʼllardan biri, <em>come, go, see, play, have</em> bilan "
                       "birga.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The train ___ at 6:40 tomorrow morning.</strong></p>",
        "choices": ["leaves", "is leaving her", "leave", "will leaving"],
        "correct": "leaves",
        "explanation": "<p><strong>leaves</strong> is correct — a timetable is not a personal "
                       "arrangement, so it takes the Present Simple (PE-9).<br><br>"
                       "<em>(<strong>leaves</strong> toʻgʻri — jadval shaxsiy kelishuv emas, shuning uchun "
                       "Present Simple oladi (PE-9).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Our lessons ___ at nine every day, but tomorrow we ___ the museum "
                "at ten.</strong></p>",
        "choices": ["start … are visiting", "are starting … visit",
                    "start … visit", "are starting … are visiting"],
        "correct": "start … are visiting",
        "explanation": "<p><strong>start … are visiting</strong> is correct — a timetable in the first "
                       "half, a special arrangement in the second.<br><br>"
                       "<em>(<strong>start … are visiting</strong> toʻgʻri — birinchi qismda jadval, "
                       "ikkinchi qismda maxsus kelishuv.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ you doing anything on Sunday?</strong></p>",
        "choices": ["Are", "Do", "Will", "Does"],
        "correct": "Are",
        "explanation": "<p><strong>Are</strong> is correct — this is the normal English way to ask about "
                       "somebody's plans.<br><br>"
                       "<em>(<strong>Are</strong> toʻgʻri — birovning rejalarini soʻrashning oddiy ingliz "
                       "usuli shu.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ tennis with Marjona after school today.</strong></p>",
        "choices": ["is playing", "plays", "play", "will playing"],
        "correct": "is playing",
        "explanation": "<p><strong>is playing</strong> is correct — the two girls have agreed it, so it is "
                       "an arrangement.<br><br>"
                       "<em>(<strong>is playing</strong> toʻgʻri — ikki qiz kelishib olgan, yaʼni bu "
                       "kelishuv.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Elbek ___ coming to the picnic — he has to help his father.</strong></p>",
        "choices": ["isn't", "doesn't", "won't", "not"],
        "correct": "isn't",
        "explanation": "<p><strong>isn't</strong> is correct — the negative goes on <em>is</em>."
                       "<br><br><em>(<strong>isn't</strong> toʻgʻri — inkor <em>is</em> ga "
                       "qoʻyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is about <em>right now</em>, not the future?</strong></p>",
        "choices": ["Look — Davron is running in the yard.",
                    "Davron is running in the school race on Saturday.",
                    "Davron is meeting his coach at five tomorrow.",
                    "Davron is flying to Tashkent next week."],
        "correct": "Look — Davron is running in the yard.",
        "explanation": "<p><strong>Look — Davron is running in the yard.</strong> is correct — "
                       "<em>Look</em> points at this moment; the others all carry a future time.<br><br>"
                       "<em>(<strong>Look — Davron is running in the yard.</strong> toʻgʻri — "
                       "<em>Look</em> shu daqiqaga ishora qiladi; qolganlarida kelasi zamon vaqti "
                       "bor.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ the parents on Thursday evening.</strong></p>",
        "choices": ["is meeting", "meets", "will meeting", "is meet"],
        "correct": "is meeting",
        "explanation": "<p><strong>is meeting</strong> is correct — a fixed appointment with other "
                       "people.<br><br>"
                       "<em>(<strong>is meeting</strong> toʻgʻri — boshqa odamlar bilan belgilangan "
                       "uchrashuv.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ his exam next Monday. The date is on the "
                "noticeboard.</strong></p>",
        "choices": ["is taking", "takes", "take", "will taking"],
        "correct": "is taking",
        "explanation": "<p><strong>is taking</strong> is correct — the date is settled, so it is "
                       "arranged.<br><br>"
                       "<em>(<strong>is taking</strong> toʻgʻri — sana belgilangan, yaʼni bu "
                       "kelishilgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which verb does <em>not</em> work in this structure?</strong></p>",
        "choices": ["know", "come", "have", "play"],
        "correct": "know",
        "explanation": "<p><strong>know</strong> is correct — stative verbs never take <em>-ing</em>, in "
                       "any tense.<br><br>"
                       "<em>(<strong>know</strong> toʻgʻri — holat feʼllari hech qanday zamonda "
                       "<em>-ing</em> olmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda and Afsona ___ to the theatre on Friday. Their tickets are "
                "in row five.</strong></p>",
        "choices": ["are going", "go", "goes", "will going"],
        "correct": "are going",
        "explanation": "<p><strong>are going</strong> is correct — plural subject, and the seats are "
                       "already booked.<br><br>"
                       "<em>(<strong>are going</strong> toʻgʻri — koʻplikdagi subject, oʻrindiqlar esa "
                       "allaqachon band qilingan.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I meeting Sirojiddin at six tomorrow.",
                    "I'm meeting Sirojiddin at six tomorrow.",
                    "I'm not meeting Sirojiddin tomorrow.",
                    "Am I meeting Sirojiddin tomorrow?"],
        "correct": "I meeting Sirojiddin at six tomorrow.",
        "explanation": "<p><strong>I meeting Sirojiddin at six tomorrow.</strong> is the mistake — "
                       "<em>am</em> is missing.<br><br>"
                       "<em>(<strong>I meeting Sirojiddin at six tomorrow.</strong> xato — <em>am</em> "
                       "yoʻq.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Ilgʻor is coming to our house on Sunday.",
                    "Ilgʻor is come to our house on Sunday.",
                    "Ilgʻor coming to our house on Sunday.",
                    "Ilgʻor will coming to our house on Sunday."],
        "correct": "Ilgʻor is coming to our house on Sunday.",
        "explanation": "<p><strong>Ilgʻor is coming to our house on Sunday.</strong> is correct — "
                       "<em>is + coming</em>, both pieces present.<br><br>"
                       "<em>(<strong>Ilgʻor is coming to our house on Sunday.</strong> toʻgʻri — "
                       "<em>is + coming</em>, ikki boʻlak ham oʻz oʻrnida.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Abdulloh:</strong> Are you free on Saturday?</p>"
                "<p><strong>Iroda:</strong> Sorry, ___</p>",
        "choices": ["I'm visiting my grandmother in the village.",
                    "I visit my grandmother in the village.",
                    "I will visiting my grandmother in the village.",
                    "I visiting my grandmother in the village."],
        "correct": "I'm visiting my grandmother in the village.",
        "explanation": "<p><strong>I'm visiting my grandmother in the village.</strong> is correct — the "
                       "visit is already arranged, which is exactly why she cannot come.<br><br>"
                       "<em>(<strong>I'm visiting my grandmother in the village.</strong> toʻgʻri — "
                       "tashrif allaqachon kelishilgan, shuning uchun u kela olmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>both</strong> tenses are used correctly.</p>",
        "choices": ["The film starts at seven, so we're meeting at half past six.",
                    "The film is starting at seven, so we meet at half past six.",
                    "The film start at seven, so we are meet at half past six.",
                    "The film starts at seven, so we meeting at half past six."],
        "correct": "The film starts at seven, so we're meeting at half past six.",
        "explanation": "<p><strong>starts … we're meeting …</strong> is correct — the cinema's timetable "
                       "in Present Simple, our own arrangement in Present Continuous.<br><br>"
                       "<em>(<strong>starts … we're meeting …</strong> toʻgʻri — kinoteatr jadvali "
                       "Present Simple da, bizning kelishuvimiz esa Present Continuous da.)</em></p>",
    },
]


# =====================================================================
# PE-29 — will vs going to vs Present Continuous
# =====================================================================

Q_PE29 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which form is the <em>most fixed</em> future?</strong></p>",
        "choices": ["Present Continuous — I'm meeting him at five.",
                    "be going to — I'm going to meet him.",
                    "will — I'll meet him.",
                    "Present Simple — I meet him."],
        "correct": "Present Continuous — I'm meeting him at five.",
        "explanation": "<p><strong>Present Continuous</strong> is correct — arranged with somebody, time "
                       "and place agreed. The scale runs: arranged → decided → just decided now."
                       "<br><br><em>(<strong>Present Continuous</strong> toʻgʻri — kimsa bilan "
                       "kelishilgan, vaqt va joy belgilangan. Shkala: kelishilgan → qaror qilingan → "
                       "hozir qaror qilindi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The waiter is here. — I ___ have the beef, please.</strong></p>",
        "choices": ["will", "am going to", "am having", "have"],
        "correct": "will",
        "explanation": "<p><strong>will</strong> is correct — the restaurant test: you decide as you "
                       "look at the menu, at the moment of speaking.<br><br>"
                       "<em>(<strong>will</strong> toʻgʻri — restoran sinovi: menyuga qarab, gapirayotgan "
                       "paytda qaror qilasiz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Before we came, I decided what to order. I ___ have the fish.</strong></p>",
        "choices": ["am going to", "will", "have", "had"],
        "correct": "am going to",
        "explanation": "<p><strong>am going to</strong> is correct — the decision was made before "
                       "speaking, so <em>going to</em> is the natural choice.<br><br>"
                       "<em>(<strong>am going to</strong> toʻgʻri — qaror gapirishdan oldin qabul "
                       "qilingan, shuning uchun <em>going to</em> tabiiy tanlov.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ Charos at the library at four — we agreed yesterday.</strong></p>",
        "choices": ["am meeting", "will meet", "meet", "am going to meeting"],
        "correct": "am meeting",
        "explanation": "<p><strong>am meeting</strong> is correct — agreed with another person, so it is "
                       "an arrangement.<br><br>"
                       "<em>(<strong>am meeting</strong> toʻgʻri — boshqa odam bilan kelishilgan, yaʼni "
                       "bu kelishuv.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Look out! You ___ hit that wall!</strong></p>",
        "choices": ["are going to", "will", "are hitting", "hit"],
        "correct": "are going to",
        "explanation": "<p><strong>are going to</strong> is correct — a prediction from evidence right in "
                       "front of you.<br><br>"
                       "<em>(<strong>are going to</strong> toʻgʻri — koʻz oldingizdagi dalilga asoslangan "
                       "taxmin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I think Uzbekistan ___ win the match tonight.</strong></p>",
        "choices": ["will", "is going to be", "is winning", "wins"],
        "correct": "will",
        "explanation": "<p><strong>will</strong> is correct — an opinion with no evidence, and "
                       "<em>I think</em> is its classic partner.<br><br>"
                       "<em>(<strong>will</strong> toʻgʻri — dalilsiz fikr, <em>I think</em> esa uning "
                       "klassik hamrohi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz has bought paint and brushes. He ___ his room.</strong></p>",
        "choices": ["is going to paint", "will paint", "paints", "painted"],
        "correct": "is going to paint",
        "explanation": "<p><strong>is going to paint</strong> is correct — the paint is the evidence of a "
                       "plan already made.<br><br>"
                       "<em>(<strong>is going to paint</strong> toʻgʻri — boʻyoq allaqachon qabul "
                       "qilingan rejaning dalili.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>This bag is heavy. — ___ carry it for you.</strong></p>",
        "choices": ["I'll", "I'm going to", "I'm carrying", "I carry"],
        "correct": "I'll",
        "explanation": "<p><strong>I'll</strong> is correct — an offer decided at this second.<br><br>"
                       "<em>(<strong>I'll</strong> toʻgʻri — shu daqiqada qabul qilingan taklif.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ to Seoul on Tuesday. Her flight is at nine.</strong></p>",
        "choices": ["is flying", "will fly", "flies", "is going to flying"],
        "correct": "is flying",
        "explanation": "<p><strong>is flying</strong> is correct — a booked ticket is as fixed as a future "
                       "gets.<br><br>"
                       "<em>(<strong>is flying</strong> toʻgʻri — band qilingan chipta kelajakning eng "
                       "qatʼiy koʻrinishi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ look for a job in Tashkent. He has decided, but nothing "
                "is arranged.</strong></p>",
        "choices": ["is going to", "is looking to", "will be", "looks to"],
        "correct": "is going to",
        "explanation": "<p><strong>is going to</strong> is correct — decided but not yet arranged: the "
                       "middle step of the scale.<br><br>"
                       "<em>(<strong>is going to</strong> toʻgʻri — qaror qilingan, lekin hali "
                       "kelishilmagan: shkalaning oʻrta pogʻonasi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Perhaps Iroda ___ come with us.</strong></p>",
        "choices": ["will", "is coming", "is going to be", "comes"],
        "correct": "will",
        "explanation": "<p><strong>will</strong> is correct — <em>perhaps, maybe, probably, I'm sure</em> "
                       "all belong to <em>will</em>.<br><br>"
                       "<em>(<strong>will</strong> toʻgʻri — <em>perhaps, maybe, probably, I'm sure</em> "
                       "hammasi <em>will</em> ga tegishli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I'll tell Sherbek the news when I ___ him tomorrow.</strong></p>",
        "choices": ["see", "will see", "am seeing", "am going to see"],
        "correct": "see",
        "explanation": "<p><strong>see</strong> is correct — the time-clause rule applies to all three "
                       "futures: after <em>when, if, before, after, until, as soon as</em>, use the "
                       "present.<br><br>"
                       "<em>(<strong>see</strong> toʻgʻri — vaqt ergash gap qoidasi uchala kelasi zamonga "
                       "ham tegishli: <em>when, if, before, after, until, as soon as</em> dan keyin "
                       "hozirgi zamon ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ the results tomorrow — it is on the "
                "timetable.</strong></p>",
        "choices": ["is announcing", "will announcing", "announce", "is going to announcing"],
        "correct": "is announcing",
        "explanation": "<p><strong>is announcing</strong> is correct — fixed and on the schedule."
                       "<br><br><em>(<strong>is announcing</strong> toʻgʻri — belgilangan va jadvalda "
                       "bor.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>A:</strong> We have no bread. — <strong>B:</strong> Really? ___ to the "
                "shop then.</p>",
        "choices": ["I'll go", "I'm going", "I'm going to go", "I go"],
        "correct": "I'll go",
        "explanation": "<p><strong>I'll go</strong> is correct — B has only just heard the news, so the "
                       "decision is instant.<br><br>"
                       "<em>(<strong>I'll go</strong> toʻgʻri — B xabarni hozir eshitdi, shuning uchun "
                       "qaror bir zumda qabul qilindi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence sounds wrong to a native speaker?</strong></p>",
        "choices": ["I'll meet Marjona at four — we arranged it last week.",
                    "I'm meeting Marjona at four — we arranged it last week.",
                    "I'm going to meet Marjona — I decided yesterday.",
                    "I'll help you now."],
        "correct": "I'll meet Marjona at four — we arranged it last week.",
        "explanation": "<p><strong>I'll meet Marjona at four — we arranged it last week.</strong> is "
                       "wrong — <em>will</em> means the decision is new, but the second half says it was "
                       "arranged a week ago.<br><br>"
                       "<em>(<strong>I'll meet Marjona at four — we arranged it last week.</strong> "
                       "xato — <em>will</em> qaror yangi ekanini bildiradi, ikkinchi qism esa bir hafta "
                       "oldin kelishilganini aytadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ a doctor. He has already started medical school.</strong></p>",
        "choices": ["is going to be", "will be probably", "is being", "be"],
        "correct": "is going to be",
        "explanation": "<p><strong>is going to be</strong> is correct — the plan is under way, with "
                       "evidence behind it.<br><br>"
                       "<em>(<strong>is going to be</strong> toʻgʻri — reja allaqachon boshlangan va "
                       "dalili bor.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Don't phone at eight — we ___ dinner then.</strong></p>",
        "choices": ["are having", "will have had", "have", "are going to having"],
        "correct": "are having",
        "explanation": "<p><strong>are having</strong> is correct — a family routine already fixed for "
                       "that time.<br><br>"
                       "<em>(<strong>are having</strong> toʻgʻri — oʻsha vaqtga allaqachon belgilangan "
                       "oilaviy tartib.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I'll call you when I will arrive.", "I'll call you when I arrive.",
                    "I'm calling you at six tonight.", "I'm going to call you tonight."],
        "correct": "I'll call you when I will arrive.",
        "explanation": "<p><strong>I'll call you when I will arrive.</strong> is the mistake — "
                       "<em>will</em> is forbidden after <em>when</em>.<br><br>"
                       "<em>(<strong>I'll call you when I will arrive.</strong> xato — <em>when</em> dan "
                       "keyin <em>will</em> ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Javohir:</strong> Have you got any plans for the summer?</p>"
                "<p><strong>Elbek:</strong> Yes, ___ , and I'm starting on 1 June.</p>",
        "choices": ["I'm going to work at my uncle's shop",
                    "I'll work at my uncle's shop",
                    "I work at my uncle's shop",
                    "I will working at my uncle's shop"],
        "correct": "I'm going to work at my uncle's shop",
        "explanation": "<p><strong>I'm going to work at my uncle's shop</strong> is correct — an existing "
                       "plan, and the start date shows how fixed it is.<br><br>"
                       "<em>(<strong>I'm going to work at my uncle's shop</strong> toʻgʻri — mavjud "
                       "reja, boshlanish sanasi esa uning qanchalik qatʼiy ekanini koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>all three</strong> futures are used "
                "correctly.</p>",
        "choices": ["I'm seeing the doctor at five, then I'm going to rest at home, "
                    "and I think I'll feel better tomorrow.",
                    "I see the doctor at five, then I will to rest at home, "
                    "and I think I'm feeling better tomorrow.",
                    "I'll see the doctor at five, then I'm resting at home, "
                    "and I'm going to feel better tomorrow probably.",
                    "I'm going to see the doctor at five o'clock arranged, then I rest at home, "
                    "and I will feeling better tomorrow."],
        "correct": "I'm seeing the doctor at five, then I'm going to rest at home, "
                   "and I think I'll feel better tomorrow.",
        "explanation": "<p><strong>I'm seeing … I'm going to rest … I think I'll feel …</strong> is "
                       "correct — arranged, decided, and just an opinion: the whole scale in one "
                       "sentence.<br><br>"
                       "<em>(<strong>I'm seeing … I'm going to rest … I think I'll feel …</strong> "
                       "toʻgʻri — kelishilgan, qaror qilingan va shunchaki fikr: bitta gapda butun "
                       "shkala.)</em></p>",
    },
]


# =====================================================================
# PE-30 — Future Continuous
# =====================================================================

Q_PE30 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>At eight o'clock tonight I ___ my homework.</strong></p>",
        "choices": ["will be doing", "will do", "will did", "am doing"],
        "correct": "will be doing",
        "explanation": "<p><strong>will be doing</strong> is correct — <em>will be + verb-ing</em> puts "
                       "you inside the future moment, in the middle of the action.<br><br>"
                       "<em>(<strong>will be doing</strong> toʻgʻri — <em>will be + feʼl-ing</em> sizni "
                       "kelasi daqiqaning ichiga, harakat oʻrtasiga olib kiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>This time tomorrow Madina ___ to Seoul.</strong></p>",
        "choices": ["will be flying", "will fly", "flies", "is fly"],
        "correct": "will be flying",
        "explanation": "<p><strong>will be flying</strong> is correct — the plane will be in the air at "
                       "that exact moment. <em>Will fly</em> would state only the bare fact.<br><br>"
                       "<em>(<strong>will be flying</strong> toʻgʻri — oʻsha aniq daqiqada samolyot "
                       "havoda boʻladi. <em>Will fly</em> esa faqat quruq faktni aytadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the form of the Future Continuous?</strong></p>",
        "choices": ["will be + verb-ing", "will + verb-ing", "will be + verb-ed", "am going to be"],
        "correct": "will be + verb-ing",
        "explanation": "<p><strong>will be + verb-ing</strong> is correct — three pieces, and none of "
                       "them changes for the person.<br><br>"
                       "<em>(<strong>will be + feʼl-ing</strong> toʻgʻri — uch boʻlak, va ularning hech "
                       "biri shaxsga qarab oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Don't call at nine — we ___ dinner then.</strong></p>",
        "choices": ["will be having", "will have", "have", "are have"],
        "correct": "will be having",
        "explanation": "<p><strong>will be having</strong> is correct — the meal will be in progress at "
                       "nine.<br><br>"
                       "<em>(<strong>will be having</strong> toʻgʻri — soat toʻqqizda ovqat davom "
                       "etayotgan boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Next week Behruz ___ his exams. He has five of them.</strong></p>",
        "choices": ["will be taking", "will took", "takes", "will be take"],
        "correct": "will be taking",
        "explanation": "<p><strong>will be taking</strong> is correct — an activity spread across a "
                       "future period.<br><br>"
                       "<em>(<strong>will be taking</strong> toʻgʻri — kelasi davr boʻyi choʻzilgan "
                       "faoliyat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Iroda ___ be waiting for us — she went home early.</strong></p>",
        "choices": ["won't", "willn't", "isn't", "doesn't"],
        "correct": "won't",
        "explanation": "<p><strong>won't</strong> is correct — <em>won't be + -ing</em>.<br><br>"
                       "<em>(<strong>won't</strong> toʻgʻri — <em>won't be + -ing</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ you be using the car tomorrow?</strong></p>",
        "choices": ["Will", "Do", "Are", "Would"],
        "correct": "Will",
        "explanation": "<p><strong>Will</strong> is correct — and this question is more polite than "
                       "<em>Will you use the car?</em>, because it asks about your plans instead of asking "
                       "you to change them.<br><br>"
                       "<em>(<strong>Will</strong> toʻgʻri — bu savol <em>Will you use the car?</em> dan "
                       "xushmuomalaroq, chunki u rejangizni oʻzgartirishni emas, shunchaki rejangizni "
                       "soʻraydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is more polite?</strong></p>",
        "choices": ["Will you be going to the shop later?", "Will you go to the shop later?",
                    "Do you go to the shop later?", "Go to the shop later?"],
        "correct": "Will you be going to the shop later?",
        "explanation": "<p><strong>Will you be going to the shop later?</strong> is correct — it simply "
                       "asks about an existing plan, so it puts no pressure on the listener.<br><br>"
                       "<em>(<strong>Will you be going to the shop later?</strong> toʻgʻri — u shunchaki "
                       "mavjud reja haqida soʻraydi, shuning uchun tinglovchiga bosim "
                       "oʻtkazmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>At this time next year Charos ___ at university.</strong></p>",
        "choices": ["will be studying", "will study", "studies", "will be study"],
        "correct": "will be studying",
        "explanation": "<p><strong>will be studying</strong> is correct — a long situation surrounding "
                       "that future moment.<br><br>"
                       "<em>(<strong>will be studying</strong> toʻgʻri — oʻsha kelasi daqiqani "
                       "oʻrab turgan uzoq holat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Don't worry about your bags — Davron ___ at the station.</strong></p>",
        "choices": ["will be waiting", "waits", "will waiting", "is wait"],
        "correct": "will be waiting",
        "explanation": "<p><strong>will be waiting</strong> is correct — he will already be there, in the "
                       "middle of waiting, when you arrive.<br><br>"
                       "<em>(<strong>will be waiting</strong> toʻgʻri — siz kelganingizda u allaqachon "
                       "kutib turgan boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ the answer by tomorrow — I'm sure of it.</strong></p>",
        "choices": ["will know", "will be knowing", "will be know", "am knowing"],
        "correct": "will know",
        "explanation": "<p><strong>will know</strong> is correct — <em>know</em> is a stative verb, so it "
                       "refuses <em>-ing</em> in the future too.<br><br>"
                       "<em>(<strong>will know</strong> toʻgʻri — <em>know</em> holat feʼli, shuning uchun "
                       "kelasi zamonda ham <em>-ing</em> ni qabul qilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which verb cannot take <em>will be + -ing</em>?</strong></p>",
        "choices": ["believe", "wait", "travel", "work"],
        "correct": "believe",
        "explanation": "<p><strong>believe</strong> is correct — a state of mind, like <em>know, "
                       "understand, like, want</em>.<br><br>"
                       "<em>(<strong>believe</strong> toʻgʻri — ong holati, xuddi <em>know, understand, "
                       "like, want</em> kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>At six o'clock tomorrow Samandar ___ football and Marjona ___ the "
                "piano.</strong></p>",
        "choices": ["will be playing … will be practising", "will play … will practise",
                    "will be playing … will practise", "plays … practises"],
        "correct": "will be playing … will be practising",
        "explanation": "<p><strong>will be playing … will be practising</strong> is correct — two actions "
                       "in progress at the same future moment.<br><br>"
                       "<em>(<strong>will be playing … will be practising</strong> toʻgʻri — kelasi bir "
                       "daqiqada davom etayotgan ikki harakat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ our tests all evening, so he can't come.</strong></p>",
        "choices": ["will be marking", "will mark it", "marks", "will be mark"],
        "correct": "will be marking",
        "explanation": "<p><strong>will be marking</strong> is correct — <em>all evening</em> stresses the "
                       "length of the activity.<br><br>"
                       "<em>(<strong>will be marking</strong> toʻgʻri — <em>all evening</em> faoliyatning "
                       "davomiyligini taʼkidlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Ilgʻor ___ at the airport at nine, so we can meet him there.</strong></p>",
        "choices": ["will be arriving", "will be arrive", "arrives to", "will arriving"],
        "correct": "will be arriving",
        "explanation": "<p><strong>will be arriving</strong> is correct — an expected event, part of the "
                       "normal course of things.<br><br>"
                       "<em>(<strong>will be arriving</strong> toʻgʻri — tabiiy kutilgan voqea.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Compare: “I'll write the letter” and “I'll be writing the letter”. Which "
                "one puts you <em>inside</em> the action?</strong></p>",
        "choices": ["I'll be writing the letter.", "I'll write the letter.",
                    "Both are the same.", "Neither of them."],
        "correct": "I'll be writing the letter.",
        "explanation": "<p><strong>I'll be writing the letter.</strong> is correct — the Continuous shows "
                       "the action in progress; the simple form states only that it will happen.<br><br>"
                       "<em>(<strong>I'll be writing the letter.</strong> toʻgʻri — Continuous harakatni "
                       "davom etayotgan holda koʻrsatadi; oddiy shakl esa faqat sodir boʻlishini "
                       "aytadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda and Afsona ___ in the school concert on Friday "
                "evening.</strong></p>",
        "choices": ["will be singing", "will be sing", "will singing", "sings"],
        "correct": "will be singing",
        "explanation": "<p><strong>will be singing</strong> is correct — the form is identical for a "
                       "plural subject.<br><br>"
                       "<em>(<strong>will be singing</strong> toʻgʻri — koʻplikdagi subject uchun ham "
                       "shakl aynan bir xil.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["At ten tomorrow Sirojiddin will be write his test.",
                    "At ten tomorrow Sirojiddin will be writing his test.",
                    "At ten tomorrow Sirojiddin won't be writing his test.",
                    "Will Sirojiddin be writing his test at ten tomorrow?"],
        "correct": "At ten tomorrow Sirojiddin will be write his test.",
        "explanation": "<p><strong>At ten tomorrow Sirojiddin will be write his test.</strong> is the "
                       "mistake — after <em>will be</em> the verb must take <em>-ing</em>.<br><br>"
                       "<em>(<strong>At ten tomorrow Sirojiddin will be write his test.</strong> xato — "
                       "<em>will be</em> dan keyin feʼl <em>-ing</em> olishi kerak.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Abdulloh:</strong> Can I visit you at seven tomorrow?</p>"
                "<p><strong>Elbek:</strong> Sorry, ___ Come at eight.</p>",
        "choices": ["I'll be having supper then.", "I'll have supper then, sorry.",
                    "I will be have supper then.", "I am having supper then yesterday."],
        "correct": "I'll be having supper then.",
        "explanation": "<p><strong>I'll be having supper then.</strong> is correct — at seven the meal "
                       "will be in progress, which is exactly why seven is not convenient.<br><br>"
                       "<em>(<strong>I'll be having supper then.</strong> toʻgʻri — soat yettida ovqat "
                       "davom etayotgan boʻladi, shuning uchun yetti qulay emas.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["This time next week Javohir will be sitting his exam, "
                    "but he won't be worrying — he will know the material.",
                    "This time next week Javohir will be sit his exam, "
                    "but he won't worrying — he will be knowing the material.",
                    "This time next week Javohir will sitting his exam, "
                    "but he willn't be worrying — he will be know the material.",
                    "This time next week Javohir will be sitting his exam, "
                    "but he won't be worrying — he will be knowing the material."],
        "correct": "This time next week Javohir will be sitting his exam, "
                   "but he won't be worrying — he will know the material.",
        "explanation": "<p><strong>will be sitting … won't be worrying … will know …</strong> is correct — "
                       "two actions in progress, and the stative <em>know</em> staying simple.<br><br>"
                       "<em>(<strong>will be sitting … won't be worrying … will know …</strong> toʻgʻri — "
                       "davom etayotgan ikki harakat va Simple da qolgan holat feʼli "
                       "<em>know</em>.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-26 Practice: Future with \"will\": Decisions, Promises, Predictions",
        "tutorial":    "PE-26:",
        "description": "PE-26 darsiga 20 savol: will + asosiy feʼl, won't va 'll, bir zumlik qarorlar, "
                       "vaʼda va taxminlar, hamda when/if dan keyin will ishlatilmasligi. Javoblar "
                       "ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE26,
    },
    {
        "title":       "PE-27 Practice: Future with \"be going to\": Plans and Evidence",
        "tutorial":    "PE-27:",
        "description": "PE-27 darsiga 20 savol: am/is/are + going to, avvaldan qabul qilingan rejalar "
                       "va koʻrinib turgan dalilga asoslangan taxminlar. Javoblar ingliz va oʻzbek "
                       "tilida izohlangan.",
        "questions":   Q_PE27,
    },
    {
        "title":       "PE-28 Practice: Present Continuous for Future Arrangements",
        "tutorial":    "PE-28:",
        "description": "PE-28 darsiga 20 savol: kelishilgan rejalar uchun Present Continuous, "
                       "“hozir” va “kelasi” maʼnolarini ajratish, jadval (Present Simple) bilan farqi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE28,
    },
    {
        "title":       "PE-29 Practice: will vs going to vs Present Continuous",
        "tutorial":    "PE-29:",
        "description": "PE-29 darsiga 20 savol: “qanchalik qatʼiy?” shkalasi, restoran sinovi, "
                       "uchta kelasi zamon oʻrtasidagi tanlov va vaqt ergash gap qoidasi. Javoblar "
                       "ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE29,
    },
    {
        "title":       "PE-30 Practice: Future Continuous: What You Will Be Doing",
        "tutorial":    "PE-30:",
        "description": "PE-30 darsiga 20 savol: will be + -ing, kelasi daqiqadagi harakat, kutilgan "
                       "voqea, xushmuomala savollar va -ing olmaydigan feʼllar. Javoblar ingliz va "
                       "oʻzbek tilida izohlangan.",
        "questions":   Q_PE30,
    },
]
