# -*- coding: utf-8 -*-
"""Prime English practices — PE-6 … PE-10.

Written with STYLE_GUIDE_PE_PRACTICE.md · lesson list in toc_pe_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_06_10.py --master=prime
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
# PE-6 — The Verb "to be": am / is / are
# =====================================================================

Q_PE6 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ a pupil at school number 12.</strong></p>",
        "choices": ["am", "is", "are", "be"],
        "correct": "am",
        "explanation": "<p><strong>am</strong> is correct. Only <em>I</em> takes <em>am</em>.<br><br>"
                       "<em>(<strong>am</strong> toʻgʻri. <em>Am</em> faqat <em>I</em> bilan "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek ___ fifteen years old.</strong></p>",
        "choices": ["is", "am", "are", "be"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct. <em>He / she / it</em> and any single person "
                       "or thing take <em>is</em>. Note that English uses <em>to be</em> for age, "
                       "not <em>have</em>.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri. <em>He / she / it</em> va har qanday bitta "
                       "shaxs yoki narsa <em>is</em> oladi. Eʼtibor bering: yoshni aytishda ingliz "
                       "tilida <em>to be</em> ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sherbek and I ___ in the same class this year.</strong></p>",
        "choices": ["are", "am", "is", "be"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct. <em>Sherbek and I</em> = <em>we</em>, and "
                       "<em>we</em> takes <em>are</em>.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri. <em>Sherbek and I</em> = <em>we</em>, "
                       "<em>we</em> esa <em>are</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct short form.</p>"
                "<p><strong>I am from Andijan. → ___ from Andijan.</strong></p>",
        "choices": ["I'm", "Im", "I's", "Iam"],
        "correct": "I'm",
        "explanation": "<p><strong>I'm</strong> is correct. The apostrophe stands for the missing "
                       "<em>a</em> of <em>am</em>.<br><br>"
                       "<em>(<strong>I'm</strong> toʻgʻri. Apostrof <em>am</em> dagi tushib qolgan "
                       "<em>a</em> harfi oʻrniga qoʻyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>You ___ my best friend.</strong></p>",
        "choices": ["are", "am", "is", "be"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct. <em>You</em> always takes <em>are</em> — "
                       "for one person and for many.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri. <em>You</em> doim <em>are</em> oladi — "
                       "bir kishiga ham, koʻpchilikka ham.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ at home now — she is at school.</strong></p>",
        "choices": ["isn't", "aren't", "amn't", "doesn't"],
        "correct": "isn't",
        "explanation": "<p><strong>isn't</strong> is correct. <em>To be</em> makes its own negative with "
                       "<em>not</em> — it needs no helper like <em>do</em>.<br><br>"
                       "<em>(<strong>isn't</strong> toʻgʻri. <em>To be</em> inkorni oʻzi "
                       "<em>not</em> bilan yasaydi — <em>do</em> kabi yordamchi kerak "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ very tired after the match.</strong></p>",
        "choices": ["are", "am", "is", "be"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct. Feelings are one of the main jobs of "
                       "<em>to be</em>: <em>we are tired, I am happy</em>.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri. Hissiyotlarni ifodalash — <em>to be</em> "
                       "ning asosiy vazifalaridan biri: <em>we are tired, I am happy</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you ready for the test?</strong></p>",
        "choices": ["Are", "Do", "Is", "Am"],
        "correct": "Are",
        "explanation": "<p><strong>Are</strong> is correct. To ask a question, <em>to be</em> simply "
                       "jumps in front of the subject — no <em>do</em>.<br><br>"
                       "<em>(<strong>Are</strong> toʻgʻri. Savol berish uchun <em>to be</em> shunchaki "
                       "subject oldiga oʻtadi — <em>do</em> ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ your parents at work now?</strong></p>",
        "choices": ["Are", "Is", "Am", "Does"],
        "correct": "Are",
        "explanation": "<p><strong>Are</strong> is correct — <em>your parents</em> is plural.<br><br>"
                       "<em>(<strong>Are</strong> toʻgʻri — <em>your parents</em> koʻplikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ very hot in Tashkent in July.</strong></p>",
        "choices": ["It is", "Is", "There is", "He is"],
        "correct": "It is",
        "explanation": "<p><strong>It is</strong> is correct. Weather sentences need the empty subject "
                       "<em>it</em> plus <em>to be</em>.<br><br>"
                       "<em>(<strong>It is</strong> toʻgʻri. Ob-havo gaplarida boʻsh subject "
                       "<em>it</em> va <em>to be</em> kerak boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The books ___ on the small table near the window.</strong></p>",
        "choices": ["are", "is", "am", "be"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct — <em>the books</em> is plural, so the verb "
                       "is plural too.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri — <em>the books</em> koʻplikda, shuning uchun "
                       "feʼl ham koʻplikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative form.</p>"
                "<p><strong>They ___ from Bukhara; they are from Khiva.</strong></p>",
        "choices": ["aren't", "isn't", "not", "don't"],
        "correct": "aren't",
        "explanation": "<p><strong>aren't</strong> is correct. <em>They</em> takes <em>are</em>, so the "
                       "negative is <em>are not = aren't</em>.<br><br>"
                       "<em>(<strong>aren't</strong> toʻgʻri. <em>They</em> <em>are</em> oladi, shuning "
                       "uchun inkori <em>are not = aren't</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “He's a doctor” mean?</strong></p>",
        "choices": ["He is a doctor.", "He has a doctor.",
                    "He was a doctor.", "He does a doctor."],
        "correct": "He is a doctor.",
        "explanation": "<p><strong>He is a doctor.</strong> is correct. In this sentence <em>'s</em> is "
                       "the short form of <em>is</em>.<br><br>"
                       "<em>(<strong>He is a doctor.</strong> toʻgʻri. Bu gapda <em>'s</em> — "
                       "<em>is</em> ning qisqa shakli.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Are you hungry? — Yes, ___ .</strong></p>",
        "choices": ["I am", "I'm", "I do", "am I"],
        "correct": "I am",
        "explanation": "<p><strong>I am</strong> is correct. In a positive short answer the verb is "
                       "never shortened — <em>Yes, I'm</em> is wrong.<br><br>"
                       "<em>(<strong>I am</strong> toʻgʻri. Qisqa tasdiq javobda feʼl qisqartirilmaydi — "
                       "<em>Yes, I'm</em> xato boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda and Charos ___ in the same university.</strong></p>",
        "choices": ["are", "is", "am", "be"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct. Two people joined by <em>and</em> make a "
                       "plural subject.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri. <em>And</em> bilan bogʻlangan ikki shaxs "
                       "koʻplikdagi subject hosil qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ Jasur your neighbour?</strong></p>",
        "choices": ["Is", "Are", "Does", "Am"],
        "correct": "Is",
        "explanation": "<p><strong>Is</strong> is correct — one person, so <em>is</em>, moved in front "
                       "of the subject to make the question.<br><br>"
                       "<em>(<strong>Is</strong> toʻgʻri — bir kishi, shuning uchun <em>is</em>, va u "
                       "savol yasash uchun subject oldiga chiqadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I student at school 12.", "I am a student at school 12.",
                    "She is a student at school 12.", "We are students at school 12."],
        "correct": "I student at school 12.",
        "explanation": "<p><strong>I student at school 12.</strong> is the mistake — the verb "
                       "<em>am</em> is missing. Uzbek hides the verb inside the word "
                       "(<em>oʻquvchiman</em>), English never does.<br><br>"
                       "<em>(<strong>I student at school 12.</strong> xato — <em>am</em> feʼli yoʻq. "
                       "Oʻzbekcha feʼlni soʻz ichiga yashiradi (<em>oʻquvchiman</em>), ingliz tili esa "
                       "hech qachon.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["My parents aren't at home.", "My parents isn't at home.",
                    "My parents not at home.", "My parents doesn't at home."],
        "correct": "My parents aren't at home.",
        "explanation": "<p><strong>My parents aren't at home.</strong> is correct: plural subject → "
                       "<em>are</em> → negative <em>aren't</em>, with no <em>do</em>.<br><br>"
                       "<em>(<strong>My parents aren't at home.</strong> toʻgʻri: koʻplikdagi subject → "
                       "<em>are</em> → inkori <em>aren't</em>, <em>do</em> ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> How old is your little brother?</p>"
                "<p><strong>Behruz:</strong> ___</p>",
        "choices": ["He's twelve.", "He has twelve.", "He twelve.", "He's twelve years."],
        "correct": "He's twelve.",
        "explanation": "<p><strong>He's twelve.</strong> is correct. English says <em>be + number</em> "
                       "for age; <em>have</em> is a direct translation from other languages and sounds "
                       "wrong.<br><br>"
                       "<em>(<strong>He's twelve.</strong> toʻgʻri. Yosh ingliz tilida <em>be + son</em> "
                       "bilan aytiladi; <em>have</em> boshqa tillardan soʻzma-soʻz tarjima boʻlib, xato "
                       "eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> form of “to be” is correct.</p>",
        "choices": ["I am from Namangan, my parents are teachers and my sister is a student.",
                    "I is from Namangan, my parents is teachers and my sister are a student.",
                    "I am from Namangan, my parents is teachers and my sister am a student.",
                    "I are from Namangan, my parents are teachers and my sister are a student."],
        "correct": "I am from Namangan, my parents are teachers and my sister is a student.",
        "explanation": "<p><strong>I am … my parents are … my sister is …</strong> is correct — "
                       "<em>I → am</em>, plural → <em>are</em>, one person → <em>is</em>.<br><br>"
                       "<em>(<strong>I am … my parents are … my sister is …</strong> toʻgʻri — "
                       "<em>I → am</em>, koʻplik → <em>are</em>, bitta shaxs → <em>is</em>.)</em></p>",
    },
]


# =====================================================================
# PE-7 — There is / There are
# =====================================================================

Q_PE7 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ a big park near our school.</strong></p>",
        "choices": ["is", "are", "have", "be"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct. The verb agrees with the noun that follows, "
                       "and <em>a big park</em> is singular.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri. Feʼl oʻzidan keyingi otga qarab keladi, "
                       "<em>a big park</em> esa birlikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ thirty pupils in Rozimurod teacher's class.</strong></p>",
        "choices": ["are", "is", "have", "has"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct — <em>thirty pupils</em> is plural.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri — <em>thirty pupils</em> koʻplikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ some water in the bottle.</strong></p>",
        "choices": ["is", "are", "aren't", "have"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct. Uncountable nouns (PE-2) always take "
                       "<em>is</em>, never <em>are</em>.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri. Sanalmaydigan otlar (PE-2) doim <em>is</em> "
                       "oladi, <em>are</em> emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ a lot of traffic in the city this morning.</strong></p>",
        "choices": ["is", "are", "were", "have"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct. <em>A lot of</em> looks plural, but "
                       "<em>traffic</em> is uncountable, so the verb stays singular.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri. <em>A lot of</em> koʻplikka oʻxshaydi, lekin "
                       "<em>traffic</em> sanalmaydi, shuning uchun feʼl birlikda qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ there any milk in the fridge?</strong></p>",
        "choices": ["Is", "Are", "Do", "Has"],
        "correct": "Is",
        "explanation": "<p><strong>Is</strong> is correct — <em>milk</em> is uncountable. To ask, the "
                       "verb simply moves in front of <em>there</em>.<br><br>"
                       "<em>(<strong>Is</strong> toʻgʻri — <em>milk</em> sanalmaydi. Savolda feʼl "
                       "shunchaki <em>there</em> oldiga chiqadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ any chairs in this room.</strong></p>",
        "choices": ["aren't", "isn't", "not", "don't"],
        "correct": "aren't",
        "explanation": "<p><strong>aren't</strong> is correct — plural noun after the verb. "
                       "<em>There aren't</em> is the English for <em>yoʻq</em> with plural things."
                       "<br><br><em>(<strong>aren't</strong> toʻgʻri — feʼldan keyin koʻplikdagi ot. "
                       "<em>There aren't</em> — koʻplikdagi narsalar uchun <em>yoʻq</em> "
                       "degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ a table and four chairs in the kitchen.</strong></p>",
        "choices": ["is", "are", "be", "has"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — the list rule: the verb agrees only with the "
                       "<em>first</em> item, and <em>a table</em> is singular.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — roʻyxat qoidasi: feʼl faqat "
                       "<em>birinchi</em> narsaga qarab keladi, <em>a table</em> esa birlikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ four chairs and a table in the kitchen.</strong></p>",
        "choices": ["are", "is", "be", "has"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct. Same room, same furniture — but now the "
                       "plural noun comes first, so the verb is plural.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri. Xona ham, mebel ham oʻsha, lekin endi "
                       "koʻplikdagi ot oldin keldi, shuning uchun feʼl ham koʻplikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How many pupils ___ there in your class?</strong></p>",
        "choices": ["are", "is", "do", "have"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct — <em>how many</em> always asks about plural "
                       "countable things.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri — <em>how many</em> doim koʻplikdagi "
                       "sanaladigan narsalar haqida soʻraydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How much sugar ___ there in this tea?</strong></p>",
        "choices": ["is", "are", "do", "have"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — <em>how much</em> goes with uncountable "
                       "nouns, and they take <em>is</em>.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — <em>how much</em> sanalmaydigan otlar bilan "
                       "keladi, ular esa <em>is</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ a problem with my phone — it doesn't charge.</strong></p>",
        "choices": ["There is", "It is", "There are", "He is"],
        "correct": "There is",
        "explanation": "<p><strong>There is</strong> is correct. We use <em>there is</em> to say that "
                       "something <em>exists</em> for the first time; <em>it is</em> describes something "
                       "we already know.<br><br>"
                       "<em>(<strong>There is</strong> toʻgʻri. <em>There is</em> biror narsaning "
                       "<em>borligini</em> birinchi marta bildiradi; <em>it is</em> esa biz bilgan "
                       "narsani taʼriflaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Look at that bike near the gate. ___ Javohir's.</strong></p>",
        "choices": ["It's", "There's", "There are", "Is"],
        "correct": "It's",
        "explanation": "<p><strong>It's</strong> is correct. The bike has already been introduced, so we "
                       "describe it with <em>it is</em>, not <em>there is</em>.<br><br>"
                       "<em>(<strong>It's</strong> toʻgʻri. Velosiped allaqachon tilga olingan, shuning "
                       "uchun uni <em>it is</em> bilan taʼriflaymiz, <em>there is</em> bilan "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ a lot of homework today, so Behruz can't play football.</strong></p>",
        "choices": ["is", "are", "aren't", "have"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — <em>homework</em> is uncountable.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — <em>homework</em> sanalmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There ___ some interesting books on Charos's desk.</strong></p>",
        "choices": ["are", "is", "was", "has"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct. <em>Some</em> works with both types, so look "
                       "at the noun: <em>books</em> is plural.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri. <em>Some</em> ikki turdagi ot bilan ham "
                       "keladi, shuning uchun otga qarang: <em>books</em> koʻplikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ there a bank near here?</strong></p>",
        "choices": ["Is", "Are", "Does", "Have"],
        "correct": "Is",
        "explanation": "<p><strong>Is</strong> is correct — <em>a bank</em> is one thing.<br><br>"
                       "<em>(<strong>Is</strong> toʻgʻri — <em>a bank</em> bitta narsa.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Are there any apples in the bag? — No, there ___ .</strong></p>",
        "choices": ["aren't", "isn't", "not are", "don't"],
        "correct": "aren't",
        "explanation": "<p><strong>aren't</strong> is correct. The short answer repeats "
                       "<em>there + the same verb</em>.<br><br>"
                       "<em>(<strong>aren't</strong> toʻgʻri. Qisqa javobda <em>there + oʻsha feʼl</em> "
                       "takrorlanadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["In my room a table is.", "There is a table in my room.",
                    "There is a big table in my room.", "There isn't a table in my room."],
        "correct": "In my room a table is.",
        "explanation": "<p><strong>In my room a table is.</strong> is the mistake — it is Uzbek word "
                       "order translated word by word. English opens with <em>There is …</em>.<br><br>"
                       "<em>(<strong>In my room a table is.</strong> xato — bu oʻzbekcha soʻz tartibining "
                       "soʻzma-soʻz tarjimasi. Ingliz tilida gap <em>There is …</em> bilan "
                       "boshlanadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["There are two windows in my room.", "There is two windows in my room.",
                    "There have two windows in my room.", "Two windows there are in my room."],
        "correct": "There are two windows in my room.",
        "explanation": "<p><strong>There are two windows in my room.</strong> is correct: plural noun → "
                       "<em>are</em>, and the place goes at the end.<br><br>"
                       "<em>(<strong>There are two windows in my room.</strong> toʻgʻri: koʻplikdagi ot "
                       "→ <em>are</em>, joy esa gap oxirida keladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Iroda:</strong> What's in your school bag?</p>"
                "<p><strong>Firdavs:</strong> ___</p>",
        "choices": ["There are two books and a pen.", "There is two books and a pen.",
                    "It is two books and a pen.", "Have two books and a pen."],
        "correct": "There are two books and a pen.",
        "explanation": "<p><strong>There are two books and a pen.</strong> is correct — the first item "
                       "in the list (<em>two books</em>) is plural, so <em>are</em>.<br><br>"
                       "<em>(<strong>There are two books and a pen.</strong> toʻgʻri — roʻyxatdagi "
                       "birinchi narsa (<em>two books</em>) koʻplikda, shuning uchun "
                       "<em>are</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["There is a mosque, two shops and a school in our street.",
                    "There are a mosque, two shops and a school in our street.",
                    "There is a mosque, two shops and a school in our street?",
                    "In our street there have a mosque, two shops and a school."],
        "correct": "There is a mosque, two shops and a school in our street.",
        "explanation": "<p><strong>There is a mosque, two shops and a school in our street.</strong> is "
                       "correct. The list rule again: only the first item counts, and <em>a mosque</em> "
                       "is singular.<br><br>"
                       "<em>(<strong>There is a mosque, two shops and a school in our street.</strong> "
                       "toʻgʻri. Yana roʻyxat qoidasi: faqat birinchi narsa hisobga olinadi, "
                       "<em>a mosque</em> esa birlikda.)</em></p>",
    },
]


# =====================================================================
# PE-8 — This, That, These, Those
# =====================================================================

Q_PE8 = [
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>___ pen in my hand is new.</strong></p>",
        "choices": ["This", "That", "These", "Those"],
        "correct": "This",
        "explanation": "<p><strong>This</strong> is correct — one thing, near me.<br><br>"
                       "<em>(<strong>This</strong> toʻgʻri — bitta narsa, menga yaqin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>___ buildings on the other side of the river are new.</strong></p>",
        "choices": ["Those", "These", "This", "That"],
        "correct": "Those",
        "explanation": "<p><strong>Those</strong> is correct — many things, far from me.<br><br>"
                       "<em>(<strong>Those</strong> toʻgʻri — koʻp narsa, mendan uzoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>___ books here on my desk are mine.</strong></p>",
        "choices": ["These", "This", "Those", "That"],
        "correct": "These",
        "explanation": "<p><strong>These</strong> is correct — many things, near me. Hear the long "
                       "“ee” sound: <em>this → these</em>.<br><br>"
                       "<em>(<strong>These</strong> toʻgʻri — koʻp narsa, menga yaqin. Uzun “ee” "
                       "tovushini eshiting: <em>this → these</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>Look at ___ mountain in the distance!</strong></p>",
        "choices": ["that", "this", "these", "those"],
        "correct": "that",
        "explanation": "<p><strong>that</strong> is correct — one thing, far away.<br><br>"
                       "<em>(<strong>that</strong> toʻgʻri — bitta narsa, uzoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>___ shoes on my feet are too small.</strong></p>",
        "choices": ["These", "This", "That", "Those"],
        "correct": "These",
        "explanation": "<p><strong>These</strong> is correct. <em>Shoes</em> is plural and they are on my "
                       "feet — near and many.<br><br>"
                       "<em>(<strong>These</strong> toʻgʻri. <em>Shoes</em> koʻplikda va oyogʻimda — "
                       "yaqin va koʻp.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>Are ___ your keys, Sirojiddin? I found them here on the floor.</strong></p>",
        "choices": ["these", "this", "that", "those"],
        "correct": "these",
        "explanation": "<p><strong>these</strong> is correct — plural (<em>keys</em>) and here in my "
                       "hand.<br><br>"
                       "<em>(<strong>these</strong> toʻgʻri — koʻplik (<em>keys</em>) va shu yerda, "
                       "qoʻlimda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>Hello, ___ is Afsona. Can I speak to Jasur, please?</strong></p>",
        "choices": ["this", "that", "these", "it"],
        "correct": "this",
        "explanation": "<p><strong>this</strong> is correct. On the phone English speakers introduce "
                       "themselves with <em>This is …</em>, not <em>I am …</em>.<br><br>"
                       "<em>(<strong>this</strong> toʻgʻri. Telefonda inglizlar oʻzini <em>This is …</em> "
                       "deb tanishtiradi, <em>I am …</em> deb emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>Who is ___ man over there, next to Rozimurod teacher?</strong></p>",
        "choices": ["that", "this", "these", "those"],
        "correct": "that",
        "explanation": "<p><strong>that</strong> is correct — one person, at a distance.<br><br>"
                       "<em>(<strong>that</strong> toʻgʻri — bitta shaxs, masofada.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ my favourite song. Listen!</strong></p>",
        "choices": ["This is", "These is", "This are", "These are"],
        "correct": "This is",
        "explanation": "<p><strong>This is</strong> is correct. Singular on both sides: "
                       "<em>this + is</em>.<br><br>"
                       "<em>(<strong>This is</strong> toʻgʻri. Ikki tomonda ham birlik: "
                       "<em>this + is</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ my parents, and this is my little sister.</strong></p>",
        "choices": ["These are", "This is", "These is", "Those is"],
        "correct": "These are",
        "explanation": "<p><strong>These are</strong> is correct. The number must match on both sides: "
                       "<em>these + are</em>.<br><br>"
                       "<em>(<strong>These are</strong> toʻgʻri. Son ikki tomonda ham mos boʻlishi "
                       "kerak: <em>these + are</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>___ morning I woke up at five and studied for the exam.</strong></p>",
        "choices": ["This", "That", "These", "Those"],
        "correct": "This",
        "explanation": "<p><strong>This</strong> is correct. <em>This</em> also means “near in time” — "
                       "today, now: <em>this morning, this week, this year</em>.<br><br>"
                       "<em>(<strong>This</strong> toʻgʻri. <em>This</em> vaqt jihatidan ham "
                       "“yaqin” degani — bugun, hozir: <em>this morning, this week, this "
                       "year</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>In ___ days there were no mobile phones.</strong></p>",
        "choices": ["those", "these", "this", "that"],
        "correct": "those",
        "explanation": "<p><strong>those</strong> is correct — far away in time, and <em>days</em> is "
                       "plural.<br><br>"
                       "<em>(<strong>those</strong> toʻgʻri — vaqt jihatidan uzoq, <em>days</em> esa "
                       "koʻplikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence uses “this” <em>with a noun</em>?</strong></p>",
        "choices": ["This shirt is expensive.", "This is expensive.",
                    "This is Davron.", "This is Afsona speaking."],
        "correct": "This shirt is expensive.",
        "explanation": "<p><strong>This shirt is expensive.</strong> is correct — here <em>this</em> "
                       "stands in front of a noun, like <em>my</em> or <em>the</em>. In the others it "
                       "replaces the noun and stands alone.<br><br>"
                       "<em>(<strong>This shirt is expensive.</strong> toʻgʻri — bu yerda <em>this</em> "
                       "otdan oldin turadi, xuddi <em>my</em> yoki <em>the</em> kabi. Qolganlarida u "
                       "otni almashtirib, yolgʻiz turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>I don't like ___ kind of film — it's too frightening.</strong></p>",
        "choices": ["this", "these", "those", "them"],
        "correct": "this",
        "explanation": "<p><strong>this</strong> is correct — <em>kind</em> is singular, so the "
                       "singular word is needed.<br><br>"
                       "<em>(<strong>this</strong> toʻgʻri — <em>kind</em> birlikda, shuning uchun "
                       "birlikdagi soʻz kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ over there my house.</strong> — how do we finish it "
                "correctly?</p>",
        "choices": ["That house over there is my house.", "That over there is my house.",
                    "Those over there is my house.", "That over there are my house."],
        "correct": "That house over there is my house.",
        "explanation": "<p><strong>That house over there is my house.</strong> is the natural, complete "
                       "sentence: <em>that + noun</em>, then the verb <em>is</em>.<br><br>"
                       "<em>(<strong>That house over there is my house.</strong> — tabiiy va toʻliq "
                       "gap: <em>that + ot</em>, keyin <em>is</em> feʼli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>___ books here are new, but ___ books over there are old.</strong></p>",
        "choices": ["These … those", "This … that", "These … that", "Those … these"],
        "correct": "These … those",
        "explanation": "<p><strong>These … those</strong> is correct — both nouns are plural, one group "
                       "near and one group far.<br><br>"
                       "<em>(<strong>These … those</strong> toʻgʻri — ikki ot ham koʻplikda, bir guruh "
                       "yaqin, ikkinchisi uzoq.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["This shoes are new.", "These shoes are new.",
                    "This shoe is new.", "Those shoes are new."],
        "correct": "This shoes are new.",
        "explanation": "<p><strong>This shoes are new.</strong> is the mistake — <em>shoes</em> is "
                       "plural, so it needs <em>these</em>. The number must match.<br><br>"
                       "<em>(<strong>This shoes are new.</strong> xato — <em>shoes</em> koʻplikda, "
                       "shuning uchun <em>these</em> kerak. Son mos boʻlishi shart.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Those flowers smell very nice.", "Those flower smell very nice.",
                    "That flowers smell very nice.", "These flower smells very nice."],
        "correct": "Those flowers smell very nice.",
        "explanation": "<p><strong>Those flowers smell very nice.</strong> is correct — plural word, "
                       "plural noun, plural verb, all agreeing.<br><br>"
                       "<em>(<strong>Those flowers smell very nice.</strong> toʻgʻri — koʻplikdagi soʻz, "
                       "koʻplikdagi ot va koʻplikdagi feʼl — hammasi mos.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Madina:</strong> (on the phone) Hello, who is this?</p>"
                "<p><strong>Sherbek:</strong> ___</p>",
        "choices": ["This is Sherbek.", "That is Sherbek.", "It is me Sherbek.", "I am this Sherbek."],
        "correct": "This is Sherbek.",
        "explanation": "<p><strong>This is Sherbek.</strong> is correct — the fixed English phone "
                       "phrase.<br><br>"
                       "<em>(<strong>This is Sherbek.</strong> toʻgʻri — telefondagi qatʼiy ingliz "
                       "iborasi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> word is correct.</p>",
        "choices": ["This is my desk, these are my books and that is Rozimurod teacher's table.",
                    "This is my desk, this are my books and those is Rozimurod teacher's table.",
                    "These is my desk, these are my books and that are Rozimurod teacher's table.",
                    "That is my desk, those are my book and this are Rozimurod teacher's table."],
        "correct": "This is my desk, these are my books and that is Rozimurod teacher's table.",
        "explanation": "<p><strong>This is my desk, these are my books and that is the teacher's "
                       "table.</strong> is correct — near + one, near + many, far + one, each with the "
                       "matching verb.<br><br>"
                       "<em>(<strong>This is my desk, these are my books and that is the teacher's "
                       "table.</strong> toʻgʻri — yaqin + bitta, yaqin + koʻp, uzoq + bitta, har biri "
                       "mos feʼl bilan.)</em></p>",
    },
]


# =====================================================================
# PE-9 — Present Simple: Habits, Facts and Timetables
# =====================================================================

Q_PE9 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Ilgʻor ___ football every Sunday morning.</strong></p>",
        "choices": ["plays", "play", "playing", "is play"],
        "correct": "plays",
        "explanation": "<p><strong>plays</strong> is correct. In the Present Simple we add "
                       "<strong>-s</strong> after <em>he / she / it</em>.<br><br>"
                       "<em>(<strong>plays</strong> toʻgʻri. Present Simple da <em>he / she / it</em> "
                       "dan keyin feʼlga <strong>-s</strong> qoʻshiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ in Samarkand with her grandparents.</strong></p>",
        "choices": ["lives", "live", "is live", "living"],
        "correct": "lives",
        "explanation": "<p><strong>lives</strong> is correct — a permanent situation, and the subject is "
                       "one person.<br><br>"
                       "<em>(<strong>lives</strong> toʻgʻri — doimiy holat, subject esa bitta "
                       "shaxs.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Water ___ at 100 degrees.</strong></p>",
        "choices": ["boils", "boil", "is boiling", "boiled"],
        "correct": "boils",
        "explanation": "<p><strong>boils</strong> is correct. General truths — things that are always "
                       "true — go in the Present Simple.<br><br>"
                       "<em>(<strong>boils</strong> toʻgʻri. Umumiy haqiqatlar — doim toʻgʻri boʻlgan "
                       "narsalar — Present Simple da keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Hurry up! The train ___ at 6:40 tomorrow morning.</strong></p>",
        "choices": ["leaves", "leave", "is leaving now", "left"],
        "correct": "leaves",
        "explanation": "<p><strong>leaves</strong> is correct. Timetables use the Present Simple even "
                       "for the future — the timetable itself does not change.<br><br>"
                       "<em>(<strong>leaves</strong> toʻgʻri. Jadvallar kelasi zamon uchun ham Present "
                       "Simple da ishlatiladi — jadvalning oʻzi oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ up at seven o'clock every morning.</strong></p>",
        "choices": ["get", "gets", "getting", "am get"],
        "correct": "get",
        "explanation": "<p><strong>get</strong> is correct. <em>I, you, we, they</em> use the bare verb "
                       "— no <em>-s</em>.<br><br>"
                       "<em>(<strong>get</strong> toʻgʻri. <em>I, you, we, they</em> feʼlni oʻzgarishsiz "
                       "oladi — <em>-s</em> qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda ___ the dishes after dinner.</strong></p>",
        "choices": ["washes", "washs", "wash", "washies"],
        "correct": "washes",
        "explanation": "<p><strong>washes</strong> is correct. After a hissing sound "
                       "(<em>-sh, -ch, -ss, -x, -o</em>) the third-person ending is "
                       "<strong>-es</strong>.<br><br>"
                       "<em>(<strong>washes</strong> toʻgʻri. Hushtakli tovushdan keyin "
                       "(<em>-sh, -ch, -ss, -x, -o</em>) uchinchi shaxs qoʻshimchasi "
                       "<strong>-es</strong> boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Jasur ___ Korean at a language centre.</strong></p>",
        "choices": ["studies", "studys", "study", "studyes"],
        "correct": "studies",
        "explanation": "<p><strong>studies</strong> is correct. Consonant + <em>y</em> → "
                       "<strong>-ies</strong>, exactly as with plural nouns in PE-3.<br><br>"
                       "<em>(<strong>studies</strong> toʻgʻri. Undosh + <em>y</em> → "
                       "<strong>-ies</strong>, xuddi PE-3 dagi koʻplikdagi otlar kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz's father ___ to the mosque on Fridays.</strong></p>",
        "choices": ["goes", "gos", "go", "goies"],
        "correct": "goes",
        "explanation": "<p><strong>goes</strong> is correct — <em>go → goes</em>, like "
                       "<em>do → does</em>.<br><br>"
                       "<em>(<strong>goes</strong> toʻgʻri — <em>go → goes</em>, xuddi "
                       "<em>do → does</em> kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs's uncle ___ two cars and a small shop.</strong></p>",
        "choices": ["has", "have", "haves", "having"],
        "correct": "has",
        "explanation": "<p><strong>has</strong> is correct. <em>Have</em> is irregular in the third "
                       "person: <em>he / she / it has</em>.<br><br>"
                       "<em>(<strong>has</strong> toʻgʻri. <em>Have</em> uchinchi shaxsda notoʻgʻri "
                       "shakl oladi: <em>he / she / it has</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ English three times a week.</strong></p>",
        "choices": ["have", "has", "haves", "having"],
        "correct": "have",
        "explanation": "<p><strong>have</strong> is correct — <em>we</em> keeps the base form.<br><br>"
                       "<em>(<strong>have</strong> toʻgʻri — <em>we</em> feʼlning asosiy shaklini "
                       "saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina's parents ___ in a hospital in the city centre.</strong></p>",
        "choices": ["work", "works", "working", "is working"],
        "correct": "work",
        "explanation": "<p><strong>work</strong> is correct. <em>Madina's parents</em> = <em>they</em>, so no "
                       "<em>-s</em>. The <em>-s</em> belongs to one person only.<br><br>"
                       "<em>(<strong>work</strong> toʻgʻri. <em>Madina's parents</em> = <em>they</em>, shuning "
                       "uchun <em>-s</em> qoʻshilmaydi. <em>-s</em> faqat bitta shaxs uchun.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Jasur and Sherbek ___ chess after school.</strong></p>",
        "choices": ["play", "plays", "playing", "is playing"],
        "correct": "play",
        "explanation": "<p><strong>play</strong> is correct — two people make a plural subject, so the "
                       "verb has no <em>-s</em>.<br><br>"
                       "<em>(<strong>play</strong> toʻgʻri — ikki kishi koʻplikdagi subject hosil "
                       "qiladi, shuning uchun feʼl <em>-s</em> olmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The sun ___ in the east and ___ in the west.</strong></p>",
        "choices": ["rises … sets", "rise … set", "rises … set", "rise … sets"],
        "correct": "rises … sets",
        "explanation": "<p><strong>rises … sets</strong> is correct. One subject (<em>the sun</em>) with "
                       "two verbs — both take the <em>-s</em>.<br><br>"
                       "<em>(<strong>rises … sets</strong> toʻgʻri. Bitta subject (<em>the sun</em>) va "
                       "ikki feʼl — ikkisi ham <em>-s</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which time expression fits the Present Simple best?</strong></p>",
        "choices": ["every day", "right now", "at the moment", "yesterday"],
        "correct": "every day",
        "explanation": "<p><strong>every day</strong> is correct. The Present Simple lives with "
                       "<em>every day, usually, often, on Mondays</em> — not with <em>now</em> or "
                       "<em>at the moment</em>.<br><br>"
                       "<em>(<strong>every day</strong> toʻgʻri. Present Simple <em>every day, usually, "
                       "often, on Mondays</em> bilan yashaydi — <em>now</em> yoki <em>at the "
                       "moment</em> bilan emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Our first lesson ___ at nine o'clock every day.</strong></p>",
        "choices": ["starts", "start", "is starting", "started"],
        "correct": "starts",
        "explanation": "<p><strong>starts</strong> is correct — a timetable, and <em>lesson</em> is "
                       "singular.<br><br>"
                       "<em>(<strong>starts</strong> toʻgʻri — jadval, <em>lesson</em> esa "
                       "birlikda.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["She watches TV in the evening.", "She watch TV in the evening.",
                    "She watchs TV in the evening.", "She is watch TV in the evening."],
        "correct": "She watches TV in the evening.",
        "explanation": "<p><strong>She watches TV in the evening.</strong> is correct — <em>-ch</em> "
                       "ending → <strong>-es</strong>.<br><br>"
                       "<em>(<strong>She watches TV in the evening.</strong> toʻgʻri — <em>-ch</em> "
                       "bilan tugaydi → <strong>-es</strong>.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["My sister go to school by bus.", "My sister goes to school by bus.",
                    "My sisters go to school by bus.", "I go to school by bus."],
        "correct": "My sister go to school by bus.",
        "explanation": "<p><strong>My sister go to school by bus.</strong> is the mistake — one sister, "
                       "so <em>goes</em>. This missing <em>-s</em> is the most common Present Simple "
                       "error.<br><br>"
                       "<em>(<strong>My sister go to school by bus.</strong> xato — bitta singil, "
                       "shuning uchun <em>goes</em>. Tushib qolgan <em>-s</em> — Present Simple dagi eng "
                       "koʻp uchraydigan xato.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["He teaches mathematics at our school.",
                    "He teach mathematics at our school.",
                    "He teachs mathematics at our school.",
                    "He is teach mathematics at our school."],
        "correct": "He teaches mathematics at our school.",
        "explanation": "<p><strong>He teaches mathematics at our school.</strong> is correct: "
                       "<em>teach + es</em> because of the <em>-ch</em> ending.<br><br>"
                       "<em>(<strong>He teaches mathematics at our school.</strong> toʻgʻri: "
                       "<em>-ch</em> bilan tugagani uchun <em>teach + es</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> What does your father do?</p>"
                "<p><strong>Javohir:</strong> ___</p>",
        "choices": ["He works in a bank.", "He work in a bank.",
                    "He is work in a bank.", "He working in a bank."],
        "correct": "He works in a bank.",
        "explanation": "<p><strong>He works in a bank.</strong> is correct. <em>What do you do?</em> "
                       "asks about a permanent job, so the answer is Present Simple with the "
                       "<em>-s</em>.<br><br>"
                       "<em>(<strong>He works in a bank.</strong> toʻgʻri. <em>What do you do?</em> "
                       "doimiy kasb haqida soʻraydi, shuning uchun javob <em>-s</em> bilan Present "
                       "Simple da boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> verb is correct.</p>",
        "choices": ["Afsona gets up at six, has breakfast and goes to school.",
                    "Afsona get up at six, have breakfast and go to school.",
                    "Afsona gets up at six, have breakfast and goes to school.",
                    "Afsona getes up at six, has breakfast and goies to school."],
        "correct": "Afsona gets up at six, has breakfast and goes to school.",
        "explanation": "<p><strong>Afsona gets up at six, has breakfast and goes to school.</strong> is "
                       "correct. One subject, three verbs — every one of them carries the "
                       "<em>-s</em>.<br><br>"
                       "<em>(<strong>Afsona gets up at six, has breakfast and goes to school.</strong> "
                       "toʻgʻri. Bitta subject, uchta feʼl — har biri <em>-s</em> oladi.)</em></p>",
    },
]


# =====================================================================
# PE-10 — Present Simple: Negatives and Questions
# =====================================================================

Q_PE10 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ like coffee. She always drinks tea.</strong></p>",
        "choices": ["doesn't", "don't", "isn't", "not"],
        "correct": "doesn't",
        "explanation": "<p><strong>doesn't</strong> is correct. For <em>he / she / it</em> the negative "
                       "is <em>doesn't + verb</em>, and the main verb stays bare.<br><br>"
                       "<em>(<strong>doesn't</strong> toʻgʻri. <em>He / she / it</em> uchun inkor "
                       "<em>doesn't + feʼl</em> boʻladi, asosiy feʼl esa oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ live in Tashkent — I live in Fergana.</strong></p>",
        "choices": ["don't", "doesn't", "am not", "not"],
        "correct": "don't",
        "explanation": "<p><strong>don't</strong> is correct. <em>I, you, we, they</em> take "
                       "<em>don't</em>.<br><br>"
                       "<em>(<strong>don't</strong> toʻgʻri. <em>I, you, we, they</em> <em>don't</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you speak English at home, Javohir?</strong></p>",
        "choices": ["Do", "Does", "Are", "Is"],
        "correct": "Do",
        "explanation": "<p><strong>Do</strong> is correct. Every verb except <em>to be</em> needs the "
                       "helper <em>do / does</em> to make a question.<br><br>"
                       "<em>(<strong>Do</strong> toʻgʻri. <em>To be</em> dan boshqa har qanday feʼl "
                       "savol yasash uchun <em>do / does</em> yordamchisini talab qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ Marjona play the piano?</strong></p>",
        "choices": ["Does", "Do", "Is", "Are"],
        "correct": "Does",
        "explanation": "<p><strong>Does</strong> is correct — <em>Marjona</em> = <em>she</em>."
                       "<br><br><em>(<strong>Does</strong> toʻgʻri — <em>your sister</em> = "
                       "<em>she</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin doesn't ___ meat.</strong></p>",
        "choices": ["eat", "eats", "eating", "ate"],
        "correct": "eat",
        "explanation": "<p><strong>eat</strong> is correct — the golden rule: once <em>does</em> has "
                       "taken the <em>-s</em>, the main verb gives it up.<br><br>"
                       "<em>(<strong>eat</strong> toʻgʻri — oltin qoida: <em>does</em> <em>-s</em> ni "
                       "olgach, asosiy feʼl undan voz kechadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Does your father ___ in this factory?</strong></p>",
        "choices": ["work", "works", "working", "worked"],
        "correct": "work",
        "explanation": "<p><strong>work</strong> is correct. In a question the helper <em>does</em> "
                       "carries the ending, so the main verb is bare.<br><br>"
                       "<em>(<strong>work</strong> toʻgʻri. Savolda qoʻshimchani yordamchi "
                       "<em>does</em> oladi, asosiy feʼl esa yalangʻoch qoladi.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Do you like ice cream? — Yes, ___ .</strong></p>",
        "choices": ["I do", "I like", "I am", "I doing"],
        "correct": "I do",
        "explanation": "<p><strong>I do</strong> is correct. The short answer repeats the helper, not "
                       "the main verb.<br><br>"
                       "<em>(<strong>I do</strong> toʻgʻri. Qisqa javobda asosiy feʼl emas, yordamchi "
                       "takrorlanadi.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Does Afsona study Korean? — No, ___ .</strong></p>",
        "choices": ["she doesn't", "she don't", "she isn't", "she not study"],
        "correct": "she doesn't",
        "explanation": "<p><strong>she doesn't</strong> is correct — the same helper comes back in the "
                       "answer.<br><br>"
                       "<em>(<strong>she doesn't</strong> toʻgʻri — javobda oʻsha yordamchi qaytib "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Where ___ your grandparents live?</strong></p>",
        "choices": ["do", "does", "are", "is"],
        "correct": "do",
        "explanation": "<p><strong>do</strong> is correct. In a wh- question the order is "
                       "<em>question word + do/does + subject + verb</em>, and "
                       "<em>grandparents</em> is plural.<br><br>"
                       "<em>(<strong>do</strong> toʻgʻri. Wh- savolda tartib: <em>soʻroq soʻzi + "
                       "do/does + subject + feʼl</em>, <em>grandparents</em> esa koʻplikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What time ___ the film start?</strong></p>",
        "choices": ["does", "do", "is", "are"],
        "correct": "does",
        "explanation": "<p><strong>does</strong> is correct — <em>the film</em> is one thing, so "
                       "<em>does</em>, and <em>start</em> stays bare.<br><br>"
                       "<em>(<strong>does</strong> toʻgʻri — <em>the film</em> bitta narsa, shuning "
                       "uchun <em>does</em>, <em>start</em> esa oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Who ___ in this house?</strong></p>",
        "choices": ["lives", "does live", "do live", "living"],
        "correct": "lives",
        "explanation": "<p><strong>lives</strong> is correct. When <em>who</em> is the subject of the "
                       "question, the helper disappears and the verb keeps its <em>-s</em>.<br><br>"
                       "<em>(<strong>lives</strong> toʻgʻri. <em>Who</em> savolning subjecti boʻlsa, "
                       "yordamchi tushib qoladi va feʼl <em>-s</em> ni saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Why ___ he want to go to the party?</strong></p>",
        "choices": ["doesn't", "don't", "isn't", "not"],
        "correct": "doesn't",
        "explanation": "<p><strong>doesn't</strong> is correct — a negative wh- question about "
                       "<em>he</em>.<br><br>"
                       "<em>(<strong>doesn't</strong> toʻgʻri — <em>he</em> haqidagi inkor wh- "
                       "savol.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you a pupil in Rozimurod teacher's class?</strong></p>",
        "choices": ["Are", "Do", "Does", "Have"],
        "correct": "Are",
        "explanation": "<p><strong>Are</strong> is correct. There is no action verb here — only "
                       "<em>to be</em>, which asks questions by itself, with no <em>do</em>.<br><br>"
                       "<em>(<strong>Are</strong> toʻgʻri. Bu yerda harakat feʼli yoʻq — faqat "
                       "<em>to be</em>, u esa savolni <em>do</em> siz, oʻzi beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you know my elder brother?</strong></p>",
        "choices": ["Do", "Are", "Is", "Does"],
        "correct": "Do",
        "explanation": "<p><strong>Do</strong> is correct. <em>Know</em> is an ordinary verb, so it "
                       "needs the helper — compare with <em>Are you …?</em><br><br>"
                       "<em>(<strong>Do</strong> toʻgʻri. <em>Know</em> — oddiy feʼl, shuning uchun "
                       "yordamchi kerak — <em>Are you …?</em> bilan solishtiring.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda's parents ___ speak English, but they understand a little.</strong></p>",
        "choices": ["don't", "doesn't", "aren't", "not"],
        "correct": "don't",
        "explanation": "<p><strong>don't</strong> is correct — <em>Iroda's parents</em> = <em>they</em>."
                       "<br><br><em>(<strong>don't</strong> toʻgʻri — <em>my parents</em> = "
                       "<em>they</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How often ___ you go to the cinema?</strong></p>",
        "choices": ["do", "does", "are", "is"],
        "correct": "do",
        "explanation": "<p><strong>do</strong> is correct — <em>you</em> always takes <em>do</em>."
                       "<br><br><em>(<strong>do</strong> toʻgʻri — <em>you</em> doim <em>do</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["She doesn't likes fish.", "She doesn't like fish.",
                    "She likes fish.", "Does she like fish?"],
        "correct": "She doesn't likes fish.",
        "explanation": "<p><strong>She doesn't likes fish.</strong> is the mistake — two verbs are "
                       "holding the <em>-s</em> at the same time. Only one player can hold the ball."
                       "<br><br><em>(<strong>She doesn't likes fish.</strong> xato — <em>-s</em> ni bir "
                       "vaqtda ikki feʼl ushlab turibdi. Toʻpni faqat bitta oʻyinchi ushlaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Does your brother work here?", "Does your brother works here?",
                    "Do your brother work here?", "Is your brother work here?"],
        "correct": "Does your brother work here?",
        "explanation": "<p><strong>Does your brother work here?</strong> is correct: "
                       "<em>Does + subject + bare verb</em>.<br><br>"
                       "<em>(<strong>Does your brother work here?</strong> toʻgʻri: "
                       "<em>Does + subject + oʻzgarmagan feʼl</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Charos:</strong> ___</p>"
                "<p><strong>Samandar:</strong> No, she doesn't. She works in a school.</p>",
        "choices": ["Does your mother work in a hospital?",
                    "Do your mother work in a hospital?",
                    "Is your mother work in a hospital?",
                    "Does your mother works in a hospital?"],
        "correct": "Does your mother work in a hospital?",
        "explanation": "<p><strong>Does your mother work in a hospital?</strong> is correct — the answer "
                       "<em>she doesn't</em> tells us the question used <em>does</em>.<br><br>"
                       "<em>(<strong>Does your mother work in a hospital?</strong> toʻgʻri — "
                       "<em>she doesn't</em> javobi savolda <em>does</em> ishlatilganini "
                       "koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Sherbek doesn't play chess, but he plays football. Does he play well?",
                    "Sherbek don't play chess, but he play football. Do he plays well?",
                    "Sherbek doesn't plays chess, but he play football. Does he plays well?",
                    "Sherbek isn't play chess, but he plays football. Is he play well?"],
        "correct": "Sherbek doesn't play chess, but he plays football. Does he play well?",
        "explanation": "<p><strong>Sherbek doesn't play chess, but he plays football. Does he play "
                       "well?</strong> is correct. Follow the <em>-s</em>: the helper holds it in the "
                       "negative and the question, the main verb holds it in the positive.<br><br>"
                       "<em>(<strong>Sherbek doesn't play chess, but he plays football. Does he play "
                       "well?</strong> toʻgʻri. <em>-s</em> ni kuzatib boring: inkor va savolda uni "
                       "yordamchi ushlaydi, tasdiqda esa asosiy feʼl.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-6 Practice: The Verb \"to be\": am / is / are",
        "tutorial":    "PE-6:",
        "description": "PE-6 darsiga 20 savol: am / is / are, qisqa shakllar, inkor va savol, "
                       "tushib qoladigan feʼl muammosi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE6,
    },
    {
        "title":       "PE-7 Practice: There is / There are",
        "tutorial":    "PE-7:",
        "description": "PE-7 darsiga 20 savol: there is / there are, roʻyxat qoidasi, "
                       "there is va it is farqi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE7,
    },
    {
        "title":       "PE-8 Practice: This, That, These, Those",
        "tutorial":    "PE-8:",
        "description": "PE-8 darsiga 20 savol: yaqin/uzoq va bitta/koʻp tizimi, ot bilan yoki "
                       "yolgʻiz ishlatilishi, telefondagi iboralar. Javoblar ingliz va oʻzbek tilida "
                       "izohlangan.",
        "questions":   Q_PE8,
    },
    {
        "title":       "PE-9 Practice: Present Simple: Habits, Facts and Timetables",
        "tutorial":    "PE-9:",
        "description": "PE-9 darsiga 20 savol: uchinchi shaxs -s qoʻshimchasi va imlo qoidalari, "
                       "odat, haqiqat va jadval maʼnolari. Javoblar ingliz va oʻzbek tilida "
                       "izohlangan.",
        "questions":   Q_PE9,
    },
    {
        "title":       "PE-10 Practice: Present Simple: Negatives and Questions",
        "tutorial":    "PE-10:",
        "description": "PE-10 darsiga 20 savol: don't / doesn't, Do / Does bilan savollar, qisqa "
                       "javoblar va oltin qoida (bitta -s). Javoblar ingliz va oʻzbek tilida "
                       "izohlangan.",
        "questions":   Q_PE10,
    },
]
