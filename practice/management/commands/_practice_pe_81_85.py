# -*- coding: utf-8 -*-
"""Prime English practices — PE-81 … PE-85 (end of Block F + start of Block G).

Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_81_85.py --master=prime --expect-questions=20
"""

SUBJECT = {
    "name":        "English",
    "description": "English grammar and vocabulary practice",
    "icon":        "bi-translate",
    "color":       "#6366f1",
}

DEFAULTS = {
    "level":                "hard",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PE-81 — Punctuation: Comma, Apostrophe, Colon, Semicolon
# =====================================================================
Q_PE81 = [
    {
        "text": "<p>Which sentence uses the commas correctly?</p>",
        "choices": [
            "Madina bought bread milk, and eggs.",
            "Madina bought bread, milk and eggs.",
            "Madina bought, bread milk and eggs.",
            "Madina bought bread milk and, eggs.",
        ],
        "correct": "Madina bought bread, milk and eggs.",
        "explanation": "<p><strong>Madina bought bread, milk and eggs.</strong> is correct. In a list "
                       "the comma separates the items, and British English usually puts no comma "
                       "before the final <em>and</em>.<br><br>"
                       "<em>(Roʻyxatda vergul narsalarni ajratadi. Britaniya ingliz tilida oxirgi "
                       "<em>and</em> dan oldin odatda vergul qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which punctuation mark belongs in the gap?</p>"
                "<p><strong>After the lesson ___ Charos went to the library.</strong></p>",
        "choices": ["comma", "colon", "semicolon", "full stop"],
        "correct": "comma",
        "explanation": "<p><strong>comma</strong> is correct. An introductory phrase or clause at the "
                       "start of a sentence is followed by a comma: <em>After the lesson, …</em><br><br>"
                       "<em>(Gap boshidagi kirish iborasidan keyin <strong>vergul</strong> qoʻyiladi: "
                       "<em>After the lesson, …</em>)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>That is ___ notebook.</strong> (the notebook belongs to Jasur)</p>",
        "choices": ["Jasurs", "Jasurs'", "Jasur's", "Jasur'"],
        "correct": "Jasur's",
        "explanation": "<p><strong>Jasur's</strong> is correct. One owner takes apostrophe + s "
                       "(PE-75).<br><br>"
                       "<em>(<strong>Jasur's</strong> toʻgʻri. Bitta egaga apostrof + s qoʻshiladi.)</em></p>",
    },
    {
        "text": "<p>Which punctuation mark belongs in the gap?</p>"
                "<p><strong>Rozimurod teacher needs three things ___ chalk, a marker and the register.</strong></p>",
        "choices": ["comma", "semicolon", "full stop", "colon"],
        "correct": "colon",
        "explanation": "<p><strong>colon</strong> is correct. The colon says \"here it comes\" — it "
                       "introduces a list or an explanation.<br><br>"
                       "<em>(<strong>Ikki nuqta</strong> toʻgʻri. Ikki nuqta roʻyxat yoki izohni "
                       "boshlab beradi — \"mana keladi\" degani.)</em></p>",
    },
    {
        "text": "<p>Which punctuation mark belongs in the gap?</p>"
                "<p><strong>Thank you ___ Iroda.</strong></p>",
        "choices": ["colon", "comma", "semicolon", "full stop"],
        "correct": "comma",
        "explanation": "<p><strong>comma</strong> is correct. When you speak <em>to</em> somebody, "
                       "their name is separated by a comma: <em>Thank you, Iroda. · Sherbek, come "
                       "here.</em><br><br>"
                       "<em>(Kimgadir murojaat qilganda, uning ismi <strong>vergul</strong> bilan "
                       "ajratiladi.)</em></p>",
    },
    {
        "text": "<p>The sentence below has a comma splice. Which correction is right?</p>"
                "<p><strong>It was raining, Samandar stayed at home.</strong></p>",
        "choices": [
            "It was raining, Samandar stayed at home.",
            "It was raining Samandar stayed at home.",
            "It was raining, so Samandar stayed at home.",
            "It was raining, and, Samandar stayed at home.",
        ],
        "correct": "It was raining, so Samandar stayed at home.",
        "explanation": "<p><strong>It was raining, so Samandar stayed at home.</strong> is correct. "
                       "A comma alone cannot join two complete sentences — you need a joining word "
                       "(<em>so, and, but</em>), a full stop or a semicolon.<br><br>"
                       "<em>(Ikki toʻliq gapni faqat vergul bilan bogʻlab boʻlmaydi. Yo bogʻlovchi "
                       "(<em>so, and, but</em>), yo nuqta, yo nuqtali vergul kerak. Bu — inshoda eng "
                       "koʻp uchraydigan xato.)</em></p>",
    },
    {
        "text": "<p>Which sentence is punctuated correctly?</p>",
        "choices": [
            "However, the weather was bad.",
            "However the weather was bad.",
            "However; the weather was bad.",
            "However: the weather was bad.",
        ],
        "correct": "However, the weather was bad.",
        "explanation": "<p><strong>However, the weather was bad.</strong> is correct. A linking word at "
                       "the start of a sentence always takes a comma after it: <em>However, · "
                       "Therefore, · In my opinion,</em><br><br>"
                       "<em>(Gap boshidagi bogʻlovchi soʻzdan keyin doim vergul qoʻyiladi — "
                       "oʻzbekchada ham \"Biroq,\", \"Shuning uchun,\" deb yozamiz.)</em></p>",
    },
    {
        "text": "<p>Which punctuation marks belong in the gaps?</p>"
                "<p><strong>Afsona ___ who lives next door ___ is a nurse.</strong></p>",
        "choices": ["colons", "semicolons", "full stops", "commas"],
        "correct": "commas",
        "explanation": "<p><strong>commas</strong> is correct. Extra, non-essential information is "
                       "wrapped in a pair of commas (PE-59) — take it out and the sentence still "
                       "works.<br><br>"
                       "<em>(Qoʻshimcha maʼlumot ikki tomondan <strong>vergul</strong> bilan oʻraladi. "
                       "Uni olib tashlasangiz ham gap toʻliq qoladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is punctuated correctly?</p>",
        "choices": [
            "Sherbek studied hard, he passed easily.",
            "Sherbek studied hard; he passed easily.",
            "Sherbek studied hard he passed easily.",
            "Sherbek studied hard, and, he passed easily.",
        ],
        "correct": "Sherbek studied hard; he passed easily.",
        "explanation": "<p><strong>Sherbek studied hard; he passed easily.</strong> is correct. The "
                       "semicolon is a strong comma: it joins two closely related complete sentences. "
                       "A plain comma there is the comma splice.<br><br>"
                       "<em>(Nuqtali vergul — kuchli vergul: bir-biriga bogʻliq ikki toʻliq gapni "
                       "birlashtiradi. U yerda oddiy vergul — bu comma splice xatosi.)</em></p>",
    },
    {
        "text": "<p>Which punctuation mark belongs in the gap?</p>"
                "<p><strong>Behruz gave one excuse ___ he had overslept.</strong></p>",
        "choices": ["comma", "semicolon", "colon", "full stop"],
        "correct": "colon",
        "explanation": "<p><strong>colon</strong> is correct. The second part explains the first, and "
                       "the colon points forward to that explanation.<br><br>"
                       "<em>(Ikkinchi qism birinchisini izohlayapti — <strong>ikki nuqta</strong> aynan "
                       "shu izohga ishora qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The ___ are waiting in the staff room.</strong></p>",
        "choices": ["teachers", "teacher's", "teachers'", "teachers's"],
        "correct": "teachers",
        "explanation": "<p><strong>teachers</strong> is correct. An apostrophe never makes a plural. "
                       "<em>Teacher's</em> would mean \"belonging to the teacher\".<br><br>"
                       "<em>(Apostrof hech qachon koʻplik yasamaydi. <em>Teacher's</em> — bu "
                       "\"oʻqituvchining\" degani, koʻplik emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is punctuated correctly?</p>",
        "choices": [
            "The dog wagged it's tail because its happy.",
            "The dog wagged its' tail because it's happy.",
            "The dog wagged it's tail because it's happy.",
            "The dog wagged its tail because it's happy.",
        ],
        "correct": "The dog wagged its tail because it's happy.",
        "explanation": "<p><strong>The dog wagged its tail because it's happy.</strong> is correct. "
                       "<em>its</em> = belonging to it; <em>it's</em> = <em>it is</em>. The apostrophe "
                       "here marks the missing letter, not possession.<br><br>"
                       "<em>(<em>its</em> — egalik (\"uning\"), <em>it's</em> — <em>it is</em> ning "
                       "qisqargani. Bu yerda apostrof tushib qolgan harfni bildiradi, egalikni "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is punctuated correctly?</p>",
        "choices": [
            "It rained: however, we went.",
            "It rained; however, we went.",
            "It rained, however, we went.",
            "It rained however; we went.",
        ],
        "correct": "It rained; however, we went.",
        "explanation": "<p><strong>It rained; however, we went.</strong> is correct. Use a semicolon "
                       "<em>before</em> <em>however</em> and a comma <em>after</em> it. The third "
                       "option is a comma splice.<br><br>"
                       "<em>(<em>however</em> dan <strong>oldin</strong> nuqtali vergul, "
                       "<strong>keyin</strong> vergul qoʻyiladi. Uchinchi variant — comma "
                       "splice xatosi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is punctuated correctly?</p>",
        "choices": [
            "After the lesson we went to the library, and borrowed three books.",
            "After, the lesson we went to the library and borrowed three books.",
            "After the lesson, we went to the library and borrowed three books.",
            "After the lesson, we went to the library, and borrowed three books.",
        ],
        "correct": "After the lesson, we went to the library and borrowed three books.",
        "explanation": "<p><strong>After the lesson, we went to the library and borrowed three "
                       "books.</strong> is correct. Comma after the introductory phrase — but no comma "
                       "before <em>and</em> here, because it joins two verbs, not two full "
                       "sentences.<br><br>"
                       "<em>(Kirish iborasidan keyin vergul bor, lekin <em>and</em> dan oldin vergul "
                       "yoʻq: u ikki toʻliq gapni emas, ikki feʼlni bogʻlayapti.)</em></p>",
    },
    {
        "text": "<p>Which sentence is punctuated correctly?</p>",
        "choices": [
            "Marjona's brothers are doctors.",
            "Marjonas brother's are doctors.",
            "Marjona's brother's are doctors.",
            "Marjonas' brothers are doctors.",
        ],
        "correct": "Marjona's brothers are doctors.",
        "explanation": "<p><strong>Marjona's brothers are doctors.</strong> is correct. "
                       "<em>Marjona's</em> = possession (apostrophe), <em>brothers</em> = plural "
                       "(no apostrophe). The two jobs must not be mixed.<br><br>"
                       "<em>(<em>Marjona's</em> — egalik, apostrof bilan; <em>brothers</em> — koʻplik, "
                       "apostrofsiz. Bu ikki vazifani aralashtirmang.)</em></p>",
    },
    {
        "text": "<p>Which sentence is punctuated correctly?</p>",
        "choices": [
            "Shaxzoda said \"I'll be late\".",
            "Shaxzoda said, \"I'll be late\".",
            "Shaxzoda said \"I'll be late.\"",
            "Shaxzoda said, \"I'll be late.\"",
        ],
        "correct": "Shaxzoda said, \"I'll be late.\"",
        "explanation": "<p><strong>Shaxzoda said, \"I'll be late.\"</strong> is correct. In direct "
                       "speech the comma comes <em>before</em> the quotation marks open, and the final "
                       "punctuation goes <em>inside</em> them.<br><br>"
                       "<em>(Koʻchirma gapda vergul qoʻshtirnoq <strong>ochilishidan oldin</strong> "
                       "keladi, oxirgi tinish belgisi esa qoʻshtirnoq <strong>ichida</strong> "
                       "qoladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a punctuation mistake?</p>",
        "choices": [
            "I like tea. He likes coffee.",
            "I like tea, he likes coffee.",
            "I like tea, but he likes coffee.",
            "I like tea; he likes coffee.",
        ],
        "correct": "I like tea, he likes coffee.",
        "explanation": "<p><strong>I like tea, he likes coffee.</strong> is the mistake — a comma "
                       "splice. The other three fix it with a full stop, a joining word and a "
                       "semicolon.<br><br>"
                       "<em>(Bu — comma splice xatosi. Qolgan uchtasi uni nuqta, bogʻlovchi va nuqtali "
                       "vergul bilan toʻgʻrilagan.)</em></p>",
    },
    {
        "text": "<p>Which sentence is punctuated correctly?</p>",
        "choices": [
            "My mother who is a doctor, works here.",
            "My mother, who is a doctor works here.",
            "My mother, who is a doctor, works here.",
            "My mother who is a doctor works here.",
        ],
        "correct": "My mother, who is a doctor, works here.",
        "explanation": "<p><strong>My mother, who is a doctor, works here.</strong> is correct. Extra "
                       "information needs commas on <em>both</em> sides — one comma alone leaves the "
                       "sentence half-open.<br><br>"
                       "<em>(Qoʻshimcha maʼlumotga <strong>ikki tomondan</strong> vergul kerak. Bitta "
                       "vergul yetarli emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is punctuated correctly?</p>",
        "choices": [
            "Rozimurod teacher said, \"Bring three things: a pen, a ruler and your notebook.\"",
            "Rozimurod teacher said \"Bring three things, a pen, a ruler and your notebook\".",
            "Rozimurod teacher said: \"Bring three things; a pen, a ruler and your notebook.\"",
            "Rozimurod teacher said, \"Bring three things a pen, a ruler and your notebook.\"",
        ],
        "correct": "Rozimurod teacher said, \"Bring three things: a pen, a ruler and your notebook.\"",
        "explanation": "<p>The first option is correct: comma before the quotation opens, a colon to "
                       "introduce the list, commas inside the list, and the full stop inside the "
                       "quotation marks.<br><br>"
                       "<em>(Qoʻshtirnoq ochilishidan oldin vergul, roʻyxatni boshlash uchun ikki "
                       "nuqta, roʻyxat ichida verguller va nuqta qoʻshtirnoq ichida.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Elbek:</strong> Whose bag is this?</p>"
                "<p><strong>Behruz:</strong> ___</p>",
        "choices": [
            "Its Madinas bag.",
            "Its Madina's bag.",
            "It's Madinas bag.",
            "It's Madina's bag.",
        ],
        "correct": "It's Madina's bag.",
        "explanation": "<p><strong>It's Madina's bag.</strong> is correct. Both apostrophes are doing a "
                       "job: <em>It's</em> = <em>It is</em> (missing letter), <em>Madina's</em> = "
                       "possession.<br><br>"
                       "<em>(Ikkala apostrof ham ish bajarayapti: <em>It's</em> — <em>It is</em> ning "
                       "qisqargani, <em>Madina's</em> — egalik.)</em></p>",
    },
]


# =====================================================================
# PE-82 — Capital Letters and Spelling Rules
# =====================================================================
Q_PE82 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>On Monday ___ have an English lesson.</strong></p>",
        "choices": ["i", "Me", "I", "me"],
        "correct": "I",
        "explanation": "<p><strong>I</strong> is correct. The pronoun <em>I</em> always takes a capital "
                       "letter, anywhere in the sentence.<br><br>"
                       "<em>(<strong>I</strong> olmoshi har doim, hatto gap oʻrtasida ham, bosh harf "
                       "bilan yoziladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda speaks ___ and Russian.</strong></p>",
        "choices": ["Uzbek", "uzbek", "the Uzbek", "an uzbek"],
        "correct": "Uzbek",
        "explanation": "<p><strong>Uzbek</strong> is correct. Languages and nationalities take a capital "
                       "letter in English — unlike Uzbek, where we write <em>ingliz tili</em> with a "
                       "small letter.<br><br>"
                       "<em>(Ingliz tilida til va millat nomlari bosh harf bilan yoziladi — oʻzbekchada "
                       "esa <em>ingliz tili</em> kichik harf bilan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We have a test on ___.</strong></p>",
        "choices": ["monday", "the monday", "a Monday", "Monday"],
        "correct": "Monday",
        "explanation": "<p><strong>Monday</strong> is correct. Days of the week and months take a "
                       "capital letter: <em>Monday, September</em>.<br><br>"
                       "<em>(Hafta kunlari va oylar bosh harf bilan: <em>Monday, September</em>. "
                       "Oʻzbekchada esa <em>dushanba</em>, <em>sentabr</em> — kichik harf bilan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In March we celebrate ___.</strong></p>",
        "choices": ["navruz", "Navruz", "the navruz", "a navruz"],
        "correct": "Navruz",
        "explanation": "<p><strong>Navruz</strong> is correct. Holidays are names, so they take a "
                       "capital letter: <em>Navruz, New Year</em>.<br><br>"
                       "<em>(Bayramlar — atoqli otlar, shuning uchun bosh harf bilan yoziladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ Karimov teaches history at our school.</strong></p>",
        "choices": ["mr", "the Mr", "a mr", "Mr"],
        "correct": "Mr",
        "explanation": "<p><strong>Mr</strong> is correct. A title in front of a name takes a capital: "
                       "<em>Mr Karimov, Dr Ahmedova</em>.<br><br>"
                       "<em>(Ism oldidan keladigan murojaat shakli bosh harf bilan yoziladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is written correctly?</p>",
        "choices": [
            "In Summer we go to the village.",
            "In summer we go to the Village.",
            "In summer we go to the village.",
            "In Summer we go to the Village.",
        ],
        "correct": "In summer we go to the village.",
        "explanation": "<p><strong>In summer we go to the village.</strong> is correct. Seasons stay "
                       "lower case in English — <em>summer, winter</em> — and <em>village</em> is an "
                       "ordinary noun.<br><br>"
                       "<em>(Fasllar ingliz tilida kichik harf bilan yoziladi, <em>village</em> esa "
                       "oddiy ot.)</em></p>",
    },
    {
        "text": "<p>Which sentence is written correctly?</p>",
        "choices": [
            "Firdavs studies maths and English.",
            "Firdavs studies Maths and English.",
            "Firdavs studies maths and english.",
            "Firdavs studies Maths and english.",
        ],
        "correct": "Firdavs studies maths and English.",
        "explanation": "<p><strong>Firdavs studies maths and English.</strong> is correct. School "
                       "subjects are lower case (<em>maths, history, biology</em>) — but "
                       "<em>English</em> is a language, so it keeps its capital.<br><br>"
                       "<em>(Maktab fanlari kichik harf bilan, lekin <em>English</em> — til boʻlgani "
                       "uchun bosh harf bilan.)</em></p>",
    },
    {
        "text": "<p>Which sentence is written correctly?</p>",
        "choices": [
            "My Mother teaches History.",
            "My mother teaches history.",
            "My mother teaches History.",
            "My Mother teaches history.",
        ],
        "correct": "My mother teaches history.",
        "explanation": "<p><strong>My mother teaches history.</strong> is correct. Family words used "
                       "with <em>my / his</em> stay lower case, and so do school subjects. (You would "
                       "write <em>Thanks, Mum!</em> only when the word replaces a name.)<br><br>"
                       "<em>(<em>my / his</em> bilan kelgan qarindoshlik soʻzlari va fan nomlari kichik "
                       "harf bilan. Faqat ism oʻrnida ishlatilganda — <em>Thanks, Mum!</em> — bosh "
                       "harf.)</em></p>",
    },
    {
        "text": "<p>Choose the correct spelling.</p>"
                "<p><strong>Sirojiddin is ___ his summer holiday.</strong> (plan + -ing)</p>",
        "choices": ["planing", "planeing", "plannning", "planning"],
        "correct": "planning",
        "explanation": "<p><strong>planning</strong> is correct. A short verb ending in one vowel + one "
                       "consonant doubles that consonant: <em>plan → planning, stop → stopped, sit → "
                       "sitting</em>.<br><br>"
                       "<em>(Qisqa feʼl bitta unli + bitta undosh bilan tugasa, undosh ikkilanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct spelling.</p>"
                "<p><strong>Charos ___ for two hours every evening.</strong> (study + -ed)</p>",
        "choices": ["studied", "studyed", "studed", "studying"],
        "correct": "studied",
        "explanation": "<p><strong>studied</strong> is correct. Consonant + <em>y</em> changes to "
                       "<em>i</em>: <em>study → studied, happy → happier, easy → easily</em>. Vowel + "
                       "<em>y</em> keeps it: <em>play → played</em>.<br><br>"
                       "<em>(Undosh + <em>y</em> boʻlsa, <em>y</em> → <em>i</em>. Unli + <em>y</em> "
                       "boʻlsa, <em>y</em> saqlanadi: <em>play → played</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct spelling.</p>"
                "<p><strong>Javohir is ___ a letter to his cousin.</strong> (write + -ing)</p>",
        "choices": ["writting", "writeing", "writing", "writes"],
        "correct": "writing",
        "explanation": "<p><strong>writing</strong> is correct. Drop the silent <em>e</em> before a "
                       "vowel ending: <em>write → writing, make → making, use → using</em>. The "
                       "<em>t</em> does not double here.<br><br>"
                       "<em>(Unli bilan boshlanadigan qoʻshimchadan oldin oxirgi jimjit <em>e</em> "
                       "tushadi, <em>t</em> esa ikkilanmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct spelling.</p>"
                "<p><strong>Marjona listened ___ to Rozimurod teacher.</strong> (care + -fully)</p>",
        "choices": ["carefuly", "carefully", "carefull", "carefullly"],
        "correct": "carefully",
        "explanation": "<p><strong>carefully</strong> is correct. The adjective has one <em>l</em> "
                       "(<em>careful</em>), the adverb has two (<em>carefully</em>).<br><br>"
                       "<em>(Sifatda bitta <em>l</em> — <em>careful</em>, ravishda ikkita — "
                       "<em>carefully</em>.)</em></p>",
    },
    {
        "text": "<p>Which pair is spelled correctly?</p>",
        "choices": [
            "believe / receive",
            "beleive / recieve",
            "believe / recieve",
            "beleive / receive",
        ],
        "correct": "believe / receive",
        "explanation": "<p><strong>believe / receive</strong> is correct. The rule is <em>i</em> before "
                       "<em>e</em> — <em>believe, friend, piece</em> — but <em>e</em> before <em>i</em> "
                       "after <em>c</em>: <em>receive, ceiling</em>.<br><br>"
                       "<em>(Qoida: <em>i</em> oldin <em>e</em> keyin — <em>believe</em>; lekin "
                       "<em>c</em> dan keyin teskari — <em>receive</em>.)</em></p>",
    },
    {
        "text": "<p>Which pair is spelled correctly?</p>",
        "choices": [
            "writting / siting",
            "writing / siting",
            "writting / sitting",
            "writing / sitting",
        ],
        "correct": "writing / sitting",
        "explanation": "<p><strong>writing / sitting</strong> is correct. These two rules look opposite, "
                       "so learn them side by side: <em>write</em> has a long vowel and a silent "
                       "<em>e</em>, so the <em>e</em> drops; <em>sit</em> has a short vowel, so the "
                       "<em>t</em> doubles.<br><br>"
                       "<em>(Ikki qoida qarama-qarshi tuyuladi: <em>write</em> da <em>e</em> tushadi, "
                       "<em>sit</em> da esa qisqa unli borligi uchun <em>t</em> ikkilanadi.)</em></p>",
    },
    {
        "text": "<p>Which pair is British English?</p>",
        "choices": [
            "color, center",
            "colour, centre",
            "colour, center",
            "color, centre",
        ],
        "correct": "colour, centre",
        "explanation": "<p><strong>colour, centre</strong> is British English; <em>color, center</em> is "
                       "American. Both are correct — but be consistent, and schools in Uzbekistan "
                       "usually teach the British forms.<br><br>"
                       "<em>(Ikkalasi ham toʻgʻri, faqat izchil boʻling. Oʻzbekistonda odatda Britaniya "
                       "varianti oʻrgatiladi, shuning uchun <em>colour, centre, organise</em> ni "
                       "tanlang.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Ilgʻor has ___ of homework this week.</strong></p>",
        "choices": ["alot", "allot", "a lot", "a lott"],
        "correct": "a lot",
        "explanation": "<p><strong>a lot</strong> is correct — always two words. <em>Alot</em> is not an "
                       "English word at all.<br><br>"
                       "<em>(<strong>a lot</strong> doim ikki soʻz boʻlib yoziladi. <em>Alot</em> degan "
                       "soʻz ingliz tilida umuman yoʻq.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "She is Uzbek and speaks Uzbek and Russian.",
            "She is Uzbek and speaks uzbek and Russian.",
            "On Monday Ilgʻor studies English.",
            "In winter we study maths.",
        ],
        "correct": "She is Uzbek and speaks uzbek and Russian.",
        "explanation": "<p><strong>She is Uzbek and speaks uzbek and Russian.</strong> is the mistake — "
                       "the language <em>Uzbek</em> needs a capital letter, exactly like "
                       "<em>Russian</em>.<br><br>"
                       "<em>(Til nomi <em>Uzbek</em> ham xuddi <em>Russian</em> kabi bosh harf bilan "
                       "yozilishi kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is written correctly?</p>",
        "choices": [
            "next Tuesday i have a Maths test and an english test.",
            "Next tuesday I have a maths test and an English test.",
            "Next Tuesday i have a Maths test and an English test.",
            "Next Tuesday I have a maths test and an English test.",
        ],
        "correct": "Next Tuesday I have a maths test and an English test.",
        "explanation": "<p>The last option is correct: capital for the day (<em>Tuesday</em>), for the "
                       "pronoun (<em>I</em>) and for the language (<em>English</em>) — but "
                       "<em>maths</em> stays lower case.<br><br>"
                       "<em>(Hafta kuni, <em>I</em> olmoshi va til nomi bosh harf bilan; "
                       "<em>maths</em> esa kichik harf bilan qoladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is written correctly?</p>",
        "choices": [
            "My mother speaks three languages and loves history.",
            "My Mother speaks three Languages and loves History.",
            "My mother speaks three Languages and loves History.",
            "My Mother speaks three languages and loves history.",
        ],
        "correct": "My mother speaks three languages and loves history.",
        "explanation": "<p>The first option is correct. Only the first word of the sentence takes a "
                       "capital — <em>mother</em>, <em>languages</em> and <em>history</em> are all "
                       "ordinary nouns.<br><br>"
                       "<em>(Faqat gapning birinchi soʻzi bosh harf bilan. <em>mother</em>, "
                       "<em>languages</em>, <em>history</em> — oddiy otlar.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> What are you doing on Saturday, Abdulloh?</p>"
                "<p><strong>Abdulloh:</strong> ___</p>",
        "choices": [
            "I'm writting an essay in english.",
            "i'm writing an essay in English.",
            "I'm writing an essay in English.",
            "I'm writeing an Essay in English.",
        ],
        "correct": "I'm writing an essay in English.",
        "explanation": "<p><strong>I'm writing an essay in English.</strong> is correct: the <em>e</em> "
                       "of <em>write</em> drops before <em>-ing</em>, <em>I</em> takes a capital, "
                       "<em>English</em> takes a capital and <em>essay</em> does not.<br><br>"
                       "<em>(<em>write</em> dagi <em>e</em> tushadi, <em>I</em> va <em>English</em> bosh "
                       "harf bilan, <em>essay</em> esa kichik harf bilan.)</em></p>",
    },
]


# =====================================================================
# PE-83 — Emphasis with do, does, did
# =====================================================================
Q_PE83 = [
    {
        "text": "<p>Complete the reply.</p>"
                "<p><strong>Iroda:</strong> You didn't tell me about the test!</p>"
                "<p><strong>Jasur:</strong> I ___ tell you!</p>",
        "choices": ["do", "did", "does", "was"],
        "correct": "did",
        "explanation": "<p><strong>did</strong> is correct. To contradict somebody about the past we put "
                       "the stressed helper <em>did</em> into a positive sentence.<br><br>"
                       "<em>(Oʻtgan zamonda kimningdir gapini rad etish uchun ijobiy gapga urgʻuli "
                       "<em>did</em> yordamchi feʼli qoʻshiladi — \"aytdim-ku!\")</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ speak Korean very well, doesn't she!</strong></p>",
        "choices": ["do", "did", "is", "does"],
        "correct": "does",
        "explanation": "<p><strong>does</strong> is correct. The subject is <em>she</em>, so the present "
                       "helper is <em>does</em> — and it carries the surprise.<br><br>"
                       "<em>(Ega — <em>she</em>, shuning uchun hozirgi zamon yordamchisi <em>does</em>. "
                       "U hayratni ifodalaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ come in! You are very welcome.</strong></p>",
        "choices": ["Do", "Does", "Did", "Are"],
        "correct": "Do",
        "explanation": "<p><strong>Do</strong> is correct. <em>Do</em> in front of an imperative makes "
                       "it warm and hospitable, not stronger.<br><br>"
                       "<em>(Buyruq gap oldidan <em>Do</em> qoʻyilsa, u iliq taklifga aylanadi: "
                       "\"marhamat, kiring!\")</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sherbek did ___ the letter — I saw him at the post office.</strong></p>",
        "choices": ["sent", "sends", "send", "sending"],
        "correct": "send",
        "explanation": "<p><strong>send</strong> is correct. <em>did</em> already carries the past, so "
                       "the main verb stays bare — the \"one marker\" rule from PE-22.<br><br>"
                       "<em>(Oʻtganlikni <em>did</em> koʻrsatgani uchun asosiy feʼl asl shaklda "
                       "qoladi — \"bitta belgi\" qoidasi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ like your idea — we just need more time.</strong></p>",
        "choices": ["does", "do", "did", "are"],
        "correct": "do",
        "explanation": "<p><strong>do</strong> is correct. With <em>we</em> the present helper is "
                       "<em>do</em>. Here it insists on one thing while admitting another.<br><br>"
                       "<em>(<em>we</em> bilan yordamchi feʼl <em>do</em> boʻladi. Bu yerda u bir "
                       "narsani tan olib, boshqasini taʼkidlayapti.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ warn us about the deadline, but we forgot.</strong></p>",
        "choices": ["does", "do", "was", "did"],
        "correct": "did",
        "explanation": "<p><strong>did</strong> is correct. The sentence is about the past "
                       "(<em>we forgot</em>), so the emphatic helper is <em>did</em> + bare "
                       "<em>warn</em>.<br><br>"
                       "<em>(Gap oʻtgan zamon haqida, shuning uchun taʼkid yordamchisi <em>did</em> va "
                       "undan keyin asl <em>warn</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ like the film — she just doesn't like the ending.</strong></p>",
        "choices": ["do", "did", "does", "is"],
        "correct": "does",
        "explanation": "<p><strong>does</strong> is correct. This is situation 2 — insisting. The "
                       "present tense and <em>she</em> give <em>does</em>.<br><br>"
                       "<em>(Bu — qatʼiy turish holati. Hozirgi zamon va <em>she</em> ega boʻlgani "
                       "uchun <em>does</em>.)</em></p>",
    },
    {
        "text": "<p>What does <strong>do</strong> add in \"Do come in! Do sit down.\"?</p>",
        "choices": [
            "warmth — it is a friendly invitation",
            "force — it makes the order stronger and ruder",
            "a question — it asks for permission",
            "a negative — it refuses politely",
        ],
        "correct": "warmth — it is a friendly invitation",
        "explanation": "<p><strong>warmth</strong> is correct. A bare imperative can sound blunt; "
                       "<em>Do come in!</em> is hospitable — very close to \"qani, kiravering\".<br><br>"
                       "<em>(Yalangʻoch buyruq quruq eshitilishi mumkin; <em>Do come in!</em> esa iliq "
                       "taklif — oʻzbek mehmondoʻstligidagi \"qani-qani, oʻtiring\" ohangi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It was ___ cold that Behruz stayed inside all day.</strong></p>",
        "choices": ["such", "so", "such a", "too"],
        "correct": "so",
        "explanation": "<p><strong>so</strong> is correct. <em>so</em> goes with an adjective alone: "
                       "<em>so cold, so tired</em>. <em>such a</em> needs a noun after it.<br><br>"
                       "<em>(<em>so</em> yolgʻiz sifat bilan keladi; <em>such a</em> dan keyin esa ot "
                       "kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It was ___ good film that Elbek watched it twice.</strong></p>",
        "choices": ["so", "so a", "such", "such a"],
        "correct": "such a",
        "explanation": "<p><strong>such a</strong> is correct. Here the adjective is followed by a noun "
                       "(<em>film</em>), so we need <em>such a</em>, not <em>so</em>.<br><br>"
                       "<em>(Bu yerda sifatdan keyin ot (<em>film</em>) bor, shuning uchun "
                       "<em>such a</em> kerak, <em>so</em> emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar didn't like the soup ___.</strong></p>",
        "choices": ["at all", "at any", "in all", "of all"],
        "correct": "at all",
        "explanation": "<p><strong>at all</strong> is correct. <em>at all</em> strengthens a negative — "
                       "\"umuman yoqmadi\".<br><br>"
                       "<em>(<em>at all</em> inkorni kuchaytiradi: <em>I don't like it at all</em> — "
                       "\"umuman yoqmaydi\".)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ apologised! I couldn't believe it.</strong></p>",
        "choices": ["actual", "in actual", "actually", "actuality"],
        "correct": "actually",
        "explanation": "<p><strong>actually</strong> is correct. It is an adverb of emphasis, like "
                       "<em>really</em>, and means \"aslida / haqiqatan ham\".<br><br>"
                       "<em>(<em>actually</em> — taʼkid ravishi, <em>really</em> ga oʻxshaydi va "
                       "\"haqiqatan ham\" degan maʼnoni beradi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is a statement with emphasis, not a question?</p>",
        "choices": [
            "Did Iroda finish her homework?",
            "Does Iroda like plov?",
            "Do you help at home?",
            "Iroda did finish her homework.",
        ],
        "correct": "Iroda did finish her homework.",
        "explanation": "<p><strong>Iroda did finish her homework.</strong> is the statement. The helper "
                       "is the same, but in a question it comes <em>before</em> the subject; in emphasis "
                       "it comes <em>after</em> it — and there is no question mark.<br><br>"
                       "<em>(Yordamchi feʼl bir xil, lekin savolda u egadan <strong>oldin</strong>, "
                       "taʼkidda esa egadan <strong>keyin</strong> keladi va soʻroq belgisi "
                       "qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I do have finished my homework.",
            "I have finished my homework.",
            "I did have finished my homework.",
            "I do finished my homework.",
        ],
        "correct": "I have finished my homework.",
        "explanation": "<p><strong>I have finished my homework.</strong> is correct. Never add emphatic "
                       "<em>do</em> to a sentence that already has another auxiliary — say <em>I have "
                       "finished</em>, or stress it with <em>really</em>.<br><br>"
                       "<em>(Gapda boshqa yordamchi feʼl bor boʻlsa, taʼkid uchun <em>do</em> "
                       "qoʻshilmaydi. Uning oʻrniga <em>really</em> ishlating.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Davron does plays the guitar very well.",
            "Davron do play the guitar very well.",
            "Davron does play the guitar very well.",
            "Davron did plays the guitar very well.",
        ],
        "correct": "Davron does play the guitar very well.",
        "explanation": "<p><strong>Davron does play the guitar very well.</strong> is correct. "
                       "<em>does</em> already carries the <em>-s</em>, so the main verb goes bare: "
                       "<em>does play</em>, never <em>does plays</em>.<br><br>"
                       "<em>(<em>-s</em> ni <em>does</em> koʻtargani uchun asosiy feʼl asl shaklda "
                       "qoladi: <em>does play</em>, <em>does plays</em> emas.)</em></p>",
    },
    {
        "text": "<p>Somebody says: \"You never help at home.\" Which reply contradicts it correctly?</p>",
        "choices": [
            "I do help at home!",
            "I am help at home!",
            "I does help at home!",
            "I helping at home!",
        ],
        "correct": "I do help at home!",
        "explanation": "<p><strong>I do help at home!</strong> is correct. The helper matches the "
                       "subject <em>I</em> (<em>do</em>), and it takes the stress in speech: \"I DO "
                       "help at home.\"<br><br>"
                       "<em>(Yordamchi feʼl <em>I</em> egasiga mos keladi va nutqda unga urgʻu "
                       "tushadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "She does like him.",
            "She does likes him.",
            "I did tell you.",
            "Do come in!",
        ],
        "correct": "She does likes him.",
        "explanation": "<p><strong>She does likes him.</strong> is the mistake. The <em>-s</em> appears "
                       "once only — it is already on <em>does</em>, so the main verb is "
                       "<em>like</em>.<br><br>"
                       "<em>(<em>-s</em> faqat bir marta ishlatiladi: u allaqachon <em>does</em> da bor, "
                       "shuning uchun asosiy feʼl <em>like</em> boʻladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I did went there yesterday.",
            "I do went there yesterday.",
            "I did going there yesterday.",
            "I did go there yesterday.",
        ],
        "correct": "I did go there yesterday.",
        "explanation": "<p><strong>I did go there yesterday.</strong> is correct. The past appears once, "
                       "on <em>did</em>; the main verb returns to its base form.<br><br>"
                       "<em>(Oʻtganlik belgisi faqat <em>did</em> da boʻladi, asosiy feʼl esa asl "
                       "shakliga qaytadi.)</em></p>",
    },
    {
        "text": "<p>You are surprised. Which is the correct emphatic version of "
                "<em>Afsona speaks Korean well</em>?</p>",
        "choices": [
            "Afsona do speak Korean well!",
            "Afsona does speaks Korean well!",
            "Afsona does speak Korean well!",
            "Afsona did speaks Korean well!",
        ],
        "correct": "Afsona does speak Korean well!",
        "explanation": "<p><strong>Afsona does speak Korean well!</strong> is correct — present tense, "
                       "third person <em>does</em>, and a bare main verb after it.<br><br>"
                       "<em>(Hozirgi zamon, uchinchi shaxs uchun <em>does</em>, undan keyin esa asosiy "
                       "feʼl asl shaklda.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Why didn't you study for the test, Samandar?</p>"
                "<p><strong>Samandar:</strong> ___</p>",
        "choices": [
            "I did study! I studied for three hours.",
            "I did studied! I studied for three hours.",
            "I do studied! I studied for three hours.",
            "I am study! I studied for three hours.",
        ],
        "correct": "I did study! I studied for three hours.",
        "explanation": "<p><strong>I did study! I studied for three hours.</strong> is correct. "
                       "Samandar is contradicting the teacher, so the stressed <em>did</em> + bare "
                       "<em>study</em> is exactly right.<br><br>"
                       "<em>(Samandar oʻqituvchining gapini rad etyapti, shuning uchun urgʻuli "
                       "<em>did</em> va asl <em>study</em> — \"oʻqidim-ku!\")</em></p>",
    },
]


# =====================================================================
# PE-84 — Inversion: Never have I seen ...
# =====================================================================
Q_PE84 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Never ___ I seen such a beautiful city.</strong></p>",
        "choices": ["has", "had", "did", "have"],
        "correct": "have",
        "explanation": "<p><strong>have</strong> is correct. The subject is <em>I</em>, so the helper is "
                       "<em>have</em> — and after a negative adverb it jumps in front of the "
                       "subject.<br><br>"
                       "<em>(Ega — <em>I</em>, shuning uchun yordamchi feʼl <em>have</em>. Inkor soʻzdan "
                       "keyin u egadan oldin keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Never have I ___ so happy.</strong></p>",
        "choices": ["be", "been", "being", "was"],
        "correct": "been",
        "explanation": "<p><strong>been</strong> is correct. The word order changes, but the tense does "
                       "not: <em>have been</em> is still the Present Perfect.<br><br>"
                       "<em>(Soʻz tartibi oʻzgaradi, lekin zamon oʻzgarmaydi: <em>have been</em> — "
                       "hamon Present Perfect.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rarely ___ Marjona speak in class.</strong></p>",
        "choices": ["do", "did", "does", "is"],
        "correct": "does",
        "explanation": "<p><strong>does</strong> is correct. The plain sentence <em>Marjona rarely speaks</em> "
                       "has no helper, so <em>does</em> appears — exactly as it would in a question — "
                       "and the verb goes bare.<br><br>"
                       "<em>(Oddiy gapda yordamchi feʼl yoʻq edi, shuning uchun savoldagidek "
                       "<em>does</em> paydo boʻladi va feʼl asl shaklda qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Little ___ I know what would happen next.</strong></p>",
        "choices": ["did", "do", "does", "had"],
        "correct": "did",
        "explanation": "<p><strong>did</strong> is correct. <em>Little did I know…</em> is a fixed "
                       "storytelling phrase meaning \"bilmagan ekanman\".<br><br>"
                       "<em>(<em>Little did I know…</em> — hikoyalarda ishlatiladigan tayyor ibora: "
                       "\"bilmagan ekanman\".)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ had we arrived than it started raining.</strong></p>",
        "choices": ["Hardly", "Never", "Seldom", "No sooner"],
        "correct": "No sooner",
        "explanation": "<p><strong>No sooner</strong> is correct, because the sentence continues with "
                       "<em>than</em>. Remember the pairs: <em>no sooner … than</em>, <em>hardly … "
                       "when</em>.<br><br>"
                       "<em>(Gap <em>than</em> bilan davom etgani uchun <em>No sooner</em> kerak. "
                       "Juftliklarni yodda tuting: <em>no sooner … than</em>, <em>hardly … "
                       "when</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Not only ___ Afsona pass the exam, but she also came first.</strong></p>",
        "choices": ["does", "did", "do", "had"],
        "correct": "did",
        "explanation": "<p><strong>did</strong> is correct. <em>Not only</em> at the front triggers "
                       "question word order, and the sentence is in the past.<br><br>"
                       "<em>(Gap boshidagi <em>Not only</em> savol tartibini talab qiladi, gap esa "
                       "oʻtgan zamonda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>No sooner had Davron sat down ___ the film started.</strong></p>",
        "choices": ["than", "when", "then", "that"],
        "correct": "than",
        "explanation": "<p><strong>than</strong> is correct. <em>No sooner</em> always pairs with "
                       "<em>than</em> — never with <em>when</em>. Exams test exactly this.<br><br>"
                       "<em>(<em>No sooner</em> doim <em>than</em> bilan juftlashadi, <em>when</em> "
                       "bilan emas. Imtihonlarda aynan shu tekshiriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Hardly had Behruz sat down ___ the phone rang.</strong></p>",
        "choices": ["than", "then", "when", "that"],
        "correct": "when",
        "explanation": "<p><strong>when</strong> is correct. <em>Hardly</em> pairs with <em>when</em>, "
                       "while <em>no sooner</em> pairs with <em>than</em>.<br><br>"
                       "<em>(<em>Hardly</em> — <em>when</em> bilan, <em>no sooner</em> esa <em>than</em> "
                       "bilan keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher was clear: under no circumstances ___ open this door.</strong></p>",
        "choices": ["should you", "you should", "do you should", "you do should"],
        "correct": "should you",
        "explanation": "<p><strong>should you</strong> is correct. After the negative phrase the helper "
                       "comes before the subject, exactly as in a question.<br><br>"
                       "<em>(Inkor iboradan keyin yordamchi feʼl egadan oldin keladi — xuddi "
                       "savoldagidek.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ I known, I would have come earlier.</strong></p>",
        "choices": ["If had", "Have", "Did", "Had"],
        "correct": "Had",
        "explanation": "<p><strong>Had</strong> is correct. This is conditional inversion: "
                       "<em>If I had known…</em> becomes <em>Had I known…</em> — and the <em>if</em> "
                       "disappears completely.<br><br>"
                       "<em>(Bu — shart gapdagi inversiya: <em>If I had known…</em> → <em>Had I "
                       "known…</em>. <em>if</em> butunlay tushib qoladi — <em>If had I…</em> "
                       "notoʻgʻri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you need any help, please call me.</strong></p>",
        "choices": ["Would", "Will", "Should", "Shall"],
        "correct": "Should",
        "explanation": "<p><strong>Should</strong> is correct. <em>Should you need help</em> = <em>If you "
                       "should need help</em> — a formal, polite opening for letters and emails.<br><br>"
                       "<em>(<em>Should you need help</em> — <em>If you should need help</em> ning "
                       "rasmiy shakli. Rasmiy xatlarda juda chiroyli eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ I you, I'd wait until tomorrow.</strong></p>",
        "choices": ["Were", "Was", "Am", "Be"],
        "correct": "Were",
        "explanation": "<p><strong>Were</strong> is correct. Only three verbs can start an inverted "
                       "conditional: <em>had</em>, <em>should</em> and <em>were</em>.<br><br>"
                       "<em>(Inversiyali shart gapni faqat uchta feʼl boshlay oladi: <em>had</em>, "
                       "<em>should</em>, <em>were</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Seldom Charos asks for help.",
            "Seldom does Charos asks for help.",
            "Seldom Charos does ask for help.",
            "Seldom does Charos ask for help.",
        ],
        "correct": "Seldom does Charos ask for help.",
        "explanation": "<p><strong>Seldom does Charos ask for help.</strong> is correct. The negative adverb "
                       "comes first, then helper + subject + <strong>bare</strong> verb.<br><br>"
                       "<em>(Avval inkor ravish, keyin yordamchi feʼl + ega + <strong>asl "
                       "shakldagi</strong> feʼl.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "If had I left earlier, I wouldn't have missed the bus.",
            "Had I left earlier, I wouldn't have missed the bus.",
            "Had if I left earlier, I wouldn't have missed the bus.",
            "Have I left earlier, I wouldn't have missed the bus.",
        ],
        "correct": "Had I left earlier, I wouldn't have missed the bus.",
        "explanation": "<p><strong>Had I left earlier, I wouldn't have missed the bus.</strong> is "
                       "correct. You use either <em>if</em> or the inversion — never both.<br><br>"
                       "<em>(Yo <em>if</em>, yo inversiya ishlatiladi — ikkalasi birga hech "
                       "qachon.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Here it comes!",
            "Here comes it!",
            "Here it come!",
            "Here is it coming!",
        ],
        "correct": "Here it comes!",
        "explanation": "<p><strong>Here it comes!</strong> is correct. We say <em>Here comes the "
                       "bus!</em> with a noun, but with a <strong>pronoun</strong> there is no "
                       "inversion.<br><br>"
                       "<em>(Ot bilan <em>Here comes the bus!</em> deymiz, lekin "
                       "<strong>olmosh</strong> bilan soʻz tartibi oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>You are chatting with your friend Elbek about plov. Which sentence sounds natural?</p>",
        "choices": [
            "Never have I eaten such good plov.",
            "Never I have eaten such good plov.",
            "I've never eaten such good plov.",
            "Never did I ate such good plov.",
        ],
        "correct": "I've never eaten such good plov.",
        "explanation": "<p><strong>I've never eaten such good plov.</strong> is the natural one. The "
                       "first option is grammatically correct but literary — said to a friend it sounds "
                       "theatrical. Inversion belongs in essays and formal writing.<br><br>"
                       "<em>(Birinchi variant grammatik toʻgʻri, lekin adabiy: doʻstingizga aytsangiz "
                       "teatrdagidek gʻalati eshitiladi. Inversiya — insho va rasmiy yozuv "
                       "uchun.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "Not only did Shaxzoda sing, but she also danced.",
            "Never have I seen such a thing.",
            "Rarely does Ilgʻor complain.",
            "Not only Shaxzoda sang, but she also danced.",
        ],
        "correct": "Not only Shaxzoda sang, but she also danced.",
        "explanation": "<p><strong>Not only Shaxzoda sang, but she also danced.</strong> is the mistake. "
                       "<em>Not only</em> at the front needs question word order: <em>Not only did Shaxzoda "
                       "sing…</em><br><br>"
                       "<em>(Gap boshidagi <em>Not only</em> savol tartibini talab qiladi: <em>Not only "
                       "did Shaxzoda sing…</em>)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "No sooner had we arrived than it started raining.",
            "No sooner we arrived when it started raining.",
            "No sooner did we arrived than it started raining.",
            "No sooner we had arrived than it started raining.",
        ],
        "correct": "No sooner had we arrived than it started raining.",
        "explanation": "<p><strong>No sooner had we arrived than it started raining.</strong> is "
                       "correct: <em>had</em> jumps in front of the subject, and <em>no sooner</em> "
                       "takes <em>than</em>.<br><br>"
                       "<em>(<em>had</em> egadan oldin chiqadi va <em>no sooner</em> <em>than</em> bilan "
                       "juftlashadi.)</em></p>",
    },
    {
        "text": "<p>Which is the correct inverted version of <em>I have never heard such nonsense</em>?</p>",
        "choices": [
            "Never I have heard such nonsense.",
            "Never have I heard such nonsense.",
            "Never did I heard such nonsense.",
            "Never have heard I such nonsense.",
        ],
        "correct": "Never have I heard such nonsense.",
        "explanation": "<p><strong>Never have I heard such nonsense.</strong> is correct. Move "
                       "<em>never</em> to the front, then swap the helper and the subject — nothing "
                       "else changes.<br><br>"
                       "<em>(<em>never</em> ni oldinga chiqaring, keyin yordamchi feʼl bilan egani "
                       "almashtiring — boshqa hech narsa oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Firdavs:</strong> Why didn't you come to the party?</p>"
                "<p><strong>Javohir:</strong> ___</p>",
        "choices": [
            "If had I known about it, I would have come.",
            "Had I know about it, I would have come.",
            "Had I known about it, I would have come.",
            "Have I known about it, I would have come.",
        ],
        "correct": "Had I known about it, I would have come.",
        "explanation": "<p><strong>Had I known about it, I would have come.</strong> is correct — the "
                       "third conditional with <em>if</em> removed and <em>had</em> moved to the "
                       "front.<br><br>"
                       "<em>(Bu — uchinchi shart gap: <em>if</em> olib tashlangan va <em>had</em> gap "
                       "boshiga chiqqan.)</em></p>",
    },
]


# =====================================================================
# PE-85 — Cleft Sentences: It was ... / What I need is ...
# =====================================================================
Q_PE85 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It was Afsona ___ won the prize.</strong></p>",
        "choices": ["who", "which", "what", "whose"],
        "correct": "who",
        "explanation": "<p><strong>who</strong> is correct. In an it-cleft we use <em>who</em> for "
                       "people and <em>that</em> for things.<br><br>"
                       "<em>(It-cleft qurilmasida odamlar uchun <em>who</em>, narsalar uchun "
                       "<em>that</em> ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It was the prize ___ Afsona won, not the medal.</strong></p>",
        "choices": ["who", "what", "that", "whom"],
        "correct": "that",
        "explanation": "<p><strong>that</strong> is correct. The spotlight is now on the thing "
                       "(<em>the prize</em>), so the sentence continues with <em>that</em>.<br><br>"
                       "<em>(Endi diqqat markazida narsa (<em>the prize</em>) turibdi, shuning uchun gap "
                       "<em>that</em> bilan davom etadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ Iroda needs is a holiday.</strong></p>",
        "choices": ["That", "What", "All what", "Which"],
        "correct": "What",
        "explanation": "<p><strong>What</strong> is correct. A what-cleft begins with <em>What</em> and "
                       "finishes with <em>is</em> or <em>was</em>: <em>What I need is…</em><br><br>"
                       "<em>(What-cleft <em>What</em> bilan boshlanib, <em>is</em> yoki <em>was</em> "
                       "bilan tugaydi: \"Menga kerak boʻlgan narsa — bu ...\")</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>All ___ want is a cup of tea.</strong></p>",
        "choices": ["what I", "that what I", "which I", "I"],
        "correct": "I",
        "explanation": "<p><strong>I</strong> is correct. After <em>All</em> there is no <em>what</em>: "
                       "<em>All I want is…</em> ✓ / <em>All what I want</em> ✗<br><br>"
                       "<em>(<em>All</em> dan keyin <em>what</em> qoʻyilmaydi. Oʻzbekchada \"men "
                       "xohlagan hamma <strong>narsa</strong>\" deymiz, shuning uchun bu xatoga yoʻl "
                       "qoʻyish oson.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Yesterday it ___ Jasur who broke the window.</strong></p>",
        "choices": ["was", "were", "did", "has"],
        "correct": "was",
        "explanation": "<p><strong>was</strong> is correct. The cleft opens with <em>It is</em> or "
                       "<em>It was</em>, and here the event is in the past.<br><br>"
                       "<em>(Cleft gap <em>It is</em> yoki <em>It was</em> bilan boshlanadi; bu yerda "
                       "voqea oʻtgan zamonda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What Behruz needs ___ two more days.</strong></p>",
        "choices": ["are", "were", "is", "have"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct. In a what-cleft the verb is singular, because "
                       "the whole clause <em>What Behruz needs</em> counts as one idea — even when the answer "
                       "is plural.<br><br>"
                       "<em>(What-cleft da feʼl birlikda boʻladi, chunki butun <em>What Behruz needs</em> "
                       "qismi bitta fikr hisoblanadi — javob koʻplikda boʻlsa ham.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It was in Bukhara ___ we first met.</strong></p>",
        "choices": ["who", "what", "whose", "that"],
        "correct": "that",
        "explanation": "<p><strong>that</strong> is correct. The spotlight can fall on a place or a "
                       "time as well as on a person, and then the cleft uses <em>that</em>.<br><br>"
                       "<em>(Diqqat markazi joy yoki vaqtga ham tushishi mumkin — bunda "
                       "<em>that</em> ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The reason why Charos is late is ___ the traffic was bad.</strong></p>",
        "choices": ["because", "that", "because of", "for"],
        "correct": "that",
        "explanation": "<p><strong>that</strong> is correct. <em>The reason why … is that …</em> — the "
                       "reason is already in the word <em>reason</em>, so <em>because</em> would say it "
                       "twice.<br><br>"
                       "<em>(Sabab allaqachon <em>reason</em> soʻzida bor, shuning uchun "
                       "<em>because</em> qoʻshilsa, bir narsa ikki marta aytilgan boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What Shaxzoda did ___ call the police immediately.</strong></p>",
        "choices": ["was", "did", "were", "has been"],
        "correct": "was",
        "explanation": "<p><strong>was</strong> is correct. The what-clause is finished by <em>is</em> or "
                       "<em>was</em>; here the action is in the past.<br><br>"
                       "<em>(What bilan boshlangan qism <em>is</em> yoki <em>was</em> bilan tugaydi; bu "
                       "yerda harakat oʻtgan zamonda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It wasn't me ___ told Rozimurod teacher.</strong></p>",
        "choices": ["which", "what", "who", "whom"],
        "correct": "who",
        "explanation": "<p><strong>who</strong> is correct — the spotlight is on a person. A cleft like "
                       "this lets you deny something politely instead of arguing.<br><br>"
                       "<em>(Diqqat markazida odam turibdi. Bunday cleft janjallashmasdan, xushmuomala "
                       "tarzda rad etish imkonini beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The person ___ helped me was Rozimurod teacher.</strong></p>",
        "choices": ["which", "what", "whose", "who"],
        "correct": "who",
        "explanation": "<p><strong>who</strong> is correct. <em>The person who…</em> is another useful "
                       "opener, built the same way as <em>The reason why…</em><br><br>"
                       "<em>(<em>The person who…</em> — yana bir foydali boshlanish, <em>The reason "
                       "why…</em> kabi tuziladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The place ___ we met was the school library.</strong></p>",
        "choices": ["which", "where", "what", "when"],
        "correct": "where",
        "explanation": "<p><strong>where</strong> is correct — the opener spotlights a place, so it takes "
                       "<em>where</em>, just as <em>The reason</em> takes <em>why</em>.<br><br>"
                       "<em>(Bu boshlanish joyni taʼkidlayapti, shuning uchun <em>where</em> kerak — "
                       "xuddi <em>The reason</em> bilan <em>why</em> kelgani kabi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "It was Jasur which broke the window.",
            "It was Jasur what broke the window.",
            "It was Jasur who broke the window.",
            "It was Jasur whose broke the window.",
        ],
        "correct": "It was Jasur who broke the window.",
        "explanation": "<p><strong>It was Jasur who broke the window.</strong> is correct. "
                       "<em>which</em> is for things, and <em>what</em> is never used to join a cleft "
                       "like this.<br><br>"
                       "<em>(<em>which</em> narsalar uchun, <em>what</em> esa bunday cleft gapni "
                       "bogʻlash uchun umuman ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "All I want is a quiet evening.",
            "All what I want is a quiet evening.",
            "All that what I want is a quiet evening.",
            "What all I want is a quiet evening.",
        ],
        "correct": "All I want is a quiet evening.",
        "explanation": "<p><strong>All I want is a quiet evening.</strong> is correct. <em>What</em> "
                       "appears only at the beginning (<em>What I want is…</em>) — never after "
                       "<em>All</em>.<br><br>"
                       "<em>(<em>What</em> faqat gap boshida keladi — <em>All</em> dan keyin hech "
                       "qachon.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "What we need are more chairs.",
            "What we need were more chairs.",
            "What we need have more chairs.",
            "What we need is more chairs.",
        ],
        "correct": "What we need is more chairs.",
        "explanation": "<p><strong>What we need is more chairs.</strong> is correct. The subject is the "
                       "whole clause <em>What we need</em>, which is one singular idea — so the verb "
                       "is <em>is</em>, even though <em>chairs</em> is plural.<br><br>"
                       "<em>(Ega — butun <em>What we need</em> qismi, u bitta birlik fikr. Shuning uchun "
                       "feʼl <em>is</em> boʻladi, garchi <em>chairs</em> koʻplikda boʻlsa ham.)</em></p>",
    },
    {
        "text": "<p>Fact: <strong>Madina bought the bicycle.</strong> "
                "Which sentence puts the spotlight on <em>the bicycle</em>?</p>",
        "choices": [
            "It was Madina who bought the bicycle.",
            "It was the bicycle that Madina bought.",
            "Madina bought the bicycle.",
            "It was Madina that the bicycle bought.",
        ],
        "correct": "It was the bicycle that Madina bought.",
        "explanation": "<p><strong>It was the bicycle that Madina bought.</strong> is correct. Whatever "
                       "you put straight after <em>It was</em> is the thing under the spotlight — here, "
                       "the bicycle rather than Madina.<br><br>"
                       "<em>(<em>It was</em> dan keyin nima qoʻysangiz, oʻsha narsa diqqat markaziga "
                       "tushadi — bu yerda Madina emas, velosiped.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "All I want is to sleep.",
            "What I want is to sleep.",
            "All what I want is to sleep.",
            "It is sleep that I want.",
        ],
        "correct": "All what I want is to sleep.",
        "explanation": "<p><strong>All what I want is to sleep.</strong> is the mistake — after "
                       "<em>All</em> there is no <em>what</em>. The other three are all correct ways of "
                       "saying the same thing.<br><br>"
                       "<em>(<em>All</em> dan keyin <em>what</em> boʻlmaydi. Qolgan uchtasi — bir "
                       "fikrni aytishning toʻgʻri usullari.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "It was Afsona who called you.",
            "Was Afsona who called you.",
            "It was Afsona which called you.",
            "It Afsona was who called you.",
        ],
        "correct": "It was Afsona who called you.",
        "explanation": "<p><strong>It was Afsona who called you.</strong> is correct. The cleft must "
                       "start with <em>It</em> — you cannot drop it, and the word order after it is "
                       "fixed.<br><br>"
                       "<em>(Cleft gap albatta <em>It</em> bilan boshlanadi — uni tashlab ketib "
                       "boʻlmaydi, undan keyingi soʻz tartibi ham qatʼiy.)</em></p>",
    },
    {
        "text": "<p>Rewrite with the spotlight on <em>Sherbek</em>: "
                "<strong>Sherbek found the keys.</strong></p>",
        "choices": [
            "It was Sherbek which found the keys.",
            "Was Sherbek who found the keys.",
            "It Sherbek was who found the keys.",
            "It was Sherbek who found the keys.",
        ],
        "correct": "It was Sherbek who found the keys.",
        "explanation": "<p><strong>It was Sherbek who found the keys.</strong> is correct: "
                       "<em>It was</em> + the spotlight + <em>who</em> + the rest of the "
                       "sentence.<br><br>"
                       "<em>(<em>It was</em> + taʼkidlanayotgan soʻz + <em>who</em> + gapning qolgan "
                       "qismi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Shaxzoda:</strong> You told the teacher about us!</p>"
                "<p><strong>Sirojiddin:</strong> ___</p>",
        "choices": [
            "It wasn't me which told the teacher — it was my brother.",
            "It wasn't me who told the teacher — it was my brother.",
            "Wasn't me who told the teacher — it was my brother.",
            "It wasn't me who told the teacher — was my brother.",
        ],
        "correct": "It wasn't me who told the teacher — it was my brother.",
        "explanation": "<p><strong>It wasn't me who told the teacher — it was my brother.</strong> is "
                       "correct. This is what clefts are best at: denying and correcting in the same "
                       "breath, without sounding aggressive.<br><br>"
                       "<em>(Cleft gaplar aynan shu narsada kuchli: bir vaqtning oʻzida rad etish va "
                       "toʻgʻrilash — qoʻpol eshitilmasdan.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-81 Practice: Punctuation: Comma, Apostrophe, Colon, Semicolon",
        "tutorial":    "PE-81:",
        "description": "PE-81 darsiga 20 savol: vergulning besh vazifasi, comma splice xatosi, "
                       "ikki nuqta va nuqtali vergul, apostrof qoidalari va koʻchirma gap. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE81,
    },
    {
        "title":       "PE-82 Practice: Capital Letters and Spelling Rules",
        "tutorial":    "PE-82:",
        "description": "PE-82 darsiga 20 savol: bosh harf qoidalari (til, millat, kun, oy, bayram), "
                       "imlo qoidalari va koʻp xato yoziladigan soʻzlar, Britaniya va Amerika imlosi. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE82,
    },
    {
        "title":       "PE-83 Practice: Emphasis with do, does, did",
        "tutorial":    "PE-83:",
        "description": "PE-83 darsiga 20 savol: ijobiy gapda taʼkid uchun do / does / did, "
                       "\"bitta belgi\" qoidasi, iliq taklif (Do come in!) va so / such a / at all. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE83,
    },
    {
        "title":       "PE-84 Practice: Inversion: Never have I seen ...",
        "tutorial":    "PE-84:",
        "description": "PE-84 darsiga 20 savol: never, seldom, hardly, not only, no sooner bilan "
                       "soʻz tartibi, if siz shart gaplar (Had I known…) va inversiya qachon "
                       "ishlatilmasligi. Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE84,
    },
    {
        "title":       "PE-85 Practice: Cleft Sentences: It was ... / What I need is ...",
        "tutorial":    "PE-85:",
        "description": "PE-85 darsiga 20 savol: It was ... who / that ..., What I need is ..., "
                       "All I want is ..., The reason why ... va xushmuomala tarzda toʻgʻrilash. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE85,
    },
]
