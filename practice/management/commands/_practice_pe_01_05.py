# -*- coding: utf-8 -*-
"""Prime English practices — PE-1 … PE-5.

One 20-question test per tutorial, linked to the tutorial itself.
Written with STYLE_GUIDE_PE_PRACTICE.md · lesson list in toc_pe_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_01_05.py --master=prime
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
# PE-1 — What Is a Sentence? Subject + Verb
# =====================================================================

Q_PE1 = [
    {
        "text": "<p>Which word is the <strong>subject</strong>?</p>"
                "<p><strong>Afsona reads a book every evening.</strong></p>",
        "choices": ["Afsona", "reads", "a book", "every evening"],
        "correct": "Afsona",
        "explanation": "<p><strong>Afsona</strong> is correct. Ask the verb <em>Who reads?</em> "
                       "— the answer is the subject.<br><br>"
                       "<em>(<strong>Afsona</strong> toʻgʻri. Feʼldan <em>kim oʻqiydi?</em> deb "
                       "soʻralsa, javob subject boʻladi.)</em></p>",
    },
    {
        "text": "<p>Which word is the <strong>verb</strong>?</p>"
                "<p><strong>My brother plays football on Sundays.</strong></p>",
        "choices": ["My brother", "plays", "football", "Sundays"],
        "correct": "plays",
        "explanation": "<p><strong>plays</strong> is correct. The verb is the action — the engine "
                       "of the sentence.<br><br>"
                       "<em>(<strong>plays</strong> toʻgʻri. Verb — harakat, gapning motori.)</em></p>",
    },
    {
        "text": "<p>Which words are the <strong>object</strong>?</p>"
                "<p><strong>Jasur opened the window.</strong></p>",
        "choices": ["Jasur", "opened", "the window", "Jasur opened"],
        "correct": "the window",
        "explanation": "<p><strong>the window</strong> is correct. Ask the verb <em>opened what?</em> "
                       "— the answer receives the action, so it is the object.<br><br>"
                       "<em>(<strong>the window</strong> toʻgʻri. <em>Nimani ochdi?</em> degan savolga "
                       "javob — object, yaʼni harakatni qabul qiluvchi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Every English sentence needs at least …</strong></p>",
        "choices": ["a subject and a verb", "a verb and an object",
                    "a subject and an adjective", "a verb only"],
        "correct": "a subject and a verb",
        "explanation": "<p><strong>a subject and a verb</strong> is correct. Without one of them "
                       "you have a fragment, not a sentence.<br><br>"
                       "<em>(<strong>a subject and a verb</strong> toʻgʻri. Ulardan biri yoʻq boʻlsa, "
                       "bu gap emas — fragment (chala gap).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The normal English word order is …</strong></p>",
        "choices": ["Subject + Verb + Object", "Subject + Object + Verb",
                    "Verb + Subject + Object", "Object + Subject + Verb"],
        "correct": "Subject + Verb + Object",
        "explanation": "<p><strong>Subject + Verb + Object</strong> is correct. English puts the verb "
                       "in the middle; Uzbek puts it at the end.<br><br>"
                       "<em>(<strong>Subject + Verb + Object</strong> toʻgʻri. Ingliz tilida feʼl "
                       "oʻrtada turadi, oʻzbek tilida esa gap oxirida.)</em></p>",
    },
    {
        "text": "<p>Which one is a <strong>complete sentence</strong>?</p>",
        "choices": ["The children are sleeping.", "Because he was tired.",
                    "In the garden behind our house.", "Running very fast."],
        "correct": "The children are sleeping.",
        "explanation": "<p><strong>The children are sleeping.</strong> is correct — it has a subject "
                       "(<em>the children</em>) and a verb (<em>are sleeping</em>). The others have no "
                       "subject–verb pair.<br><br>"
                       "<em>(<strong>The children are sleeping.</strong> toʻgʻri — unda subject "
                       "(<em>the children</em>) ham, verb (<em>are sleeping</em>) ham bor. "
                       "Qolganlarida subject–verb jufti yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ is raining. Take your umbrella.</strong></p>",
        "choices": ["It", "Is", "This", "— (nothing)"],
        "correct": "It",
        "explanation": "<p><strong>It</strong> is correct. English always needs a subject, so weather "
                       "sentences borrow <em>it</em> even though it means nothing.<br><br>"
                       "<em>(<strong>It</strong> toʻgʻri. Ingliz tilida subject har doim kerak, shuning "
                       "uchun ob-havo gaplarida maʼnosi boʻlmasa ham <em>it</em> qoʻyiladi. Oʻzbekchada "
                       "esa shunchaki “yomgʻir yogʻyapti” deyiladi.)</em></p>",
    },
    {
        "text": "<p>Which words are the <strong>subject</strong>?</p>"
                "<p><strong>My little sister sings beautifully.</strong></p>",
        "choices": ["My little sister", "sister", "sings", "beautifully"],
        "correct": "My little sister",
        "explanation": "<p><strong>My little sister</strong> is correct. A subject can be several words "
                       "working as one group, not just a single word.<br><br>"
                       "<em>(<strong>My little sister</strong> toʻgʻri. Subject bitta soʻz emas, bir "
                       "necha soʻzdan iborat guruh ham boʻlishi mumkin.)</em></p>",
    },
    {
        "text": "<p>Which word is the <strong>verb</strong>?</p>"
                "<p><strong>Afsona knows the answer.</strong></p>",
        "choices": ["knows", "Afsona", "the answer", "answer"],
        "correct": "knows",
        "explanation": "<p><strong>knows</strong> is correct. <em>Know</em> is a state, not a visible "
                       "action, but grammatically it is still the verb.<br><br>"
                       "<em>(<strong>knows</strong> toʻgʻri. <em>Know</em> — koʻrinadigan harakat emas, "
                       "holat; lekin grammatik jihatdan u ham verb.)</em></p>",
    },
    {
        "text": "<p>Choose the sentence with the <strong>correct word order</strong>.</p>",
        "choices": ["Afsona speaks English very well.", "Afsona English speaks very well.",
                    "Speaks Afsona English very well.", "English Afsona very well speaks."],
        "correct": "Afsona speaks English very well.",
        "explanation": "<p><strong>Afsona speaks English very well.</strong> is correct: "
                       "subject → verb → object. The other options use Uzbek order, with the verb "
                       "pushed away from its subject.<br><br>"
                       "<em>(<strong>Afsona speaks English very well.</strong> toʻgʻri: "
                       "subject → verb → object. Boshqalari oʻzbekcha tartibda, feʼl subjectdan "
                       "uzoqlashib qolgan.)</em></p>",
    },
    {
        "text": "<p>Which words are the <strong>subject</strong>?</p>"
                "<p><strong>Every morning my father drinks green tea.</strong></p>",
        "choices": ["my father", "Every morning", "drinks", "green tea"],
        "correct": "my father",
        "explanation": "<p><strong>my father</strong> is correct. <em>Every morning</em> is a time "
                       "expression — it can stand at the front, but it never does the action.<br><br>"
                       "<em>(<strong>my father</strong> toʻgʻri. <em>Every morning</em> — vaqt "
                       "ifodasi; gap boshida turishi mumkin, lekin harakatni bajarmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is missing in this fragment: “Goes to school by bus.”</strong></p>",
        "choices": ["the subject", "the verb", "the object", "nothing is missing"],
        "correct": "the subject",
        "explanation": "<p><strong>the subject</strong> is correct. There is a verb (<em>goes</em>) but "
                       "nobody to do it: <em>Sherbek goes to school by bus.</em><br><br>"
                       "<em>(<strong>the subject</strong> toʻgʻri. Verb bor (<em>goes</em>), lekin uni "
                       "bajaruvchi yoʻq: <em>Sherbek goes to school by bus.</em>)</em></p>",
    },
    {
        "text": "<p>Which sentence has <strong>no verb</strong>?</p>",
        "choices": ["My friend Sherbek very clever.", "My friend Sherbek studies hard.",
                    "Sherbek helps his mother.", "Sherbek is in my class."],
        "correct": "My friend Sherbek very clever.",
        "explanation": "<p><strong>My friend Sherbek very clever.</strong> is correct — it needs the "
                       "verb <em>is</em>: <em>My friend Sherbek is very clever.</em> Uzbek can leave "
                       "the verb out; English cannot.<br><br>"
                       "<em>(<strong>My friend Sherbek very clever.</strong> toʻgʻri — unga <em>is</em> "
                       "feʼli kerak. Oʻzbekchada “juda aqlli” desa boʻladi, ingliz tilida "
                       "esa feʼl tushib qolmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In “The teacher asked Jasur”, who receives the action?</strong></p>",
        "choices": ["Jasur", "The teacher", "asked", "nobody"],
        "correct": "Jasur",
        "explanation": "<p><strong>Jasur</strong> is correct. <em>The teacher</em> does the asking "
                       "(subject); <em>Jasur</em> receives it (object).<br><br>"
                       "<em>(<strong>Jasur</strong> toʻgʻri. <em>The teacher</em> soʻraydi (subject), "
                       "<em>Jasur</em> esa harakatni qabul qiladi (object).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ study English every day.</strong></p>",
        "choices": ["They", "Them", "Their", "Theirs"],
        "correct": "They",
        "explanation": "<p><strong>They</strong> is correct. The subject seat — right before the verb — "
                       "takes <em>I, you, he, she, it, we, they</em>.<br><br>"
                       "<em>(<strong>They</strong> toʻgʻri. Subject oʻrni — feʼl oldidan — "
                       "<em>I, you, he, she, it, we, they</em> ni oladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence keeps the <strong>English</strong> order and not the Uzbek one?</p>",
        "choices": ["Jasur writes a letter to his friend.", "Jasur his friend to a letter writes.",
                    "A letter Jasur writes to his friend.", "Writes Jasur a letter to his friend."],
        "correct": "Jasur writes a letter to his friend.",
        "explanation": "<p><strong>Jasur writes a letter to his friend.</strong> is correct. English "
                       "keeps subject and verb together at the front; the extra information follows."
                       "<br><br><em>(<strong>Jasur writes a letter to his friend.</strong> toʻgʻri. "
                       "Ingliz tilida subject va verb gap boshida yonma-yon turadi, qoʻshimcha "
                       "maʼlumot esa keyin keladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["It is very cold today.", "Is very cold today.",
                    "Very cold today is.", "Today very cold."],
        "correct": "It is very cold today.",
        "explanation": "<p><strong>It is very cold today.</strong> is correct. Every English sentence "
                       "needs a subject, so weather takes <em>it</em>.<br><br>"
                       "<em>(<strong>It is very cold today.</strong> toʻgʻri. Har bir ingliz gapi "
                       "subject talab qiladi, ob-havo uchun esa <em>it</em> ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Reads a book every evening.", "Afsona reads a book every evening.",
                    "She reads a book every evening.", "My sister reads a book every evening."],
        "correct": "Reads a book every evening.",
        "explanation": "<p><strong>Reads a book every evening.</strong> is the mistake — the subject is "
                       "missing. English never drops the subject, even when it is obvious.<br><br>"
                       "<em>(<strong>Reads a book every evening.</strong> xato — subject yoʻq. Ingliz "
                       "tilida subject, aniq boʻlsa ham, tashlab ketilmaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> What does your sister do after school?</p>"
                "<p><strong>B:</strong> ___</p>",
        "choices": ["She helps my mother.", "Helps my mother.",
                    "My mother helps.", "Is helps my mother."],
        "correct": "She helps my mother.",
        "explanation": "<p><strong>She helps my mother.</strong> is correct: subject (<em>she</em>) + "
                       "verb (<em>helps</em>) + object (<em>my mother</em>). <em>My mother helps.</em> "
                       "is a sentence too, but it changes the meaning — then the mother does the "
                       "helping.<br><br>"
                       "<em>(<strong>She helps my mother.</strong> toʻgʻri: subject (<em>she</em>) + "
                       "verb (<em>helps</em>) + object (<em>my mother</em>). <em>My mother helps.</em> "
                       "ham gap, lekin maʼnosi oʻzgaradi — unda onasi yordam beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the sentence with the correct order of <strong>place</strong> and "
                "<strong>time</strong>.</p>",
        "choices": ["Afsona plays tennis in the park every Saturday.",
                    "Afsona plays every Saturday tennis in the park.",
                    "Afsona plays tennis every Saturday in the park.",
                    "Every Saturday plays Afsona tennis in the park."],
        "correct": "Afsona plays tennis in the park every Saturday.",
        "explanation": "<p><strong>Afsona plays tennis in the park every Saturday.</strong> is correct. "
                       "After subject + verb + object, English puts <em>place</em> before "
                       "<em>time</em>.<br><br>"
                       "<em>(<strong>Afsona plays tennis in the park every Saturday.</strong> toʻgʻri. "
                       "Subject + verb + object dan keyin ingliz tilida avval <em>joy</em>, keyin "
                       "<em>vaqt</em> keladi.)</em></p>",
    },
]


# =====================================================================
# PE-2 — Nouns: Countable and Uncountable
# =====================================================================

Q_PE2 = [
    {
        "text": "<p>Which noun is <strong>uncountable</strong>?</p>",
        "choices": ["water", "book", "chair", "pen"],
        "correct": "water",
        "explanation": "<p><strong>water</strong> is correct. You cannot count water one by one — you "
                       "measure it. So no <em>a/an</em> and no <em>-s</em>.<br><br>"
                       "<em>(<strong>water</strong> toʻgʻri. Suvni donalab sanab boʻlmaydi, faqat "
                       "oʻlchanadi. Shuning uchun <em>a/an</em> ham, <em>-s</em> ham "
                       "qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which noun is <strong>countable</strong>?</p>",
        "choices": ["apple", "information", "advice", "rice"],
        "correct": "apple",
        "explanation": "<p><strong>apple</strong> is correct: <em>one apple, two apples</em>. "
                       "<em>Information</em>, <em>advice</em> and <em>rice</em> have no plural form."
                       "<br><br><em>(<strong>apple</strong> toʻgʻri: <em>one apple, two apples</em>. "
                       "<em>Information</em>, <em>advice</em> va <em>rice</em> ning koʻpligi "
                       "yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I need ___ about the university entrance exam.</strong></p>",
        "choices": ["some information", "some informations",
                    "an information", "many informations"],
        "correct": "some information",
        "explanation": "<p><strong>some information</strong> is correct. <em>Information</em> is "
                       "uncountable: never <em>informations</em>, never <em>an information</em>."
                       "<br><br><em>(<strong>some information</strong> toʻgʻri. <em>Information</em> "
                       "sanalmaydi: <em>informations</em> ham, <em>an information</em> ham "
                       "boʻlmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona gave me a very useful ___ about learning words.</strong></p>",
        "choices": ["piece of advice", "advice", "advices", "an advice"],
        "correct": "piece of advice",
        "explanation": "<p><strong>piece of advice</strong> is correct. <em>Advice</em> is uncountable, "
                       "so to talk about one single item we say <em>a piece of advice</em>.<br><br>"
                       "<em>(<strong>piece of advice</strong> toʻgʻri. <em>Advice</em> sanalmaydi, "
                       "shuning uchun bitta maslahat haqida gapirganda <em>a piece of advice</em> "
                       "deyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How ___ money do you need?</strong></p>",
        "choices": ["much", "many", "a few", "number of"],
        "correct": "much",
        "explanation": "<p><strong>much</strong> is correct. <em>Money</em> is uncountable, and "
                       "uncountable nouns take <em>much</em>.<br><br>"
                       "<em>(<strong>much</strong> toʻgʻri. <em>Money</em> sanalmaydi, sanalmaydigan "
                       "otlar bilan esa <em>much</em> ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How ___ books did you read last summer?</strong></p>",
        "choices": ["many", "much", "a little", "amount of"],
        "correct": "many",
        "explanation": "<p><strong>many</strong> is correct. Countable plurals take <em>many</em>; "
                       "uncountables take <em>much</em>.<br><br>"
                       "<em>(<strong>many</strong> toʻgʻri. Sanaladigan otlarning koʻpligi bilan "
                       "<em>many</em>, sanalmaydiganlar bilan <em>much</em> keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We have too ___ homework this week.</strong></p>",
        "choices": ["much", "many", "a few", "several"],
        "correct": "much",
        "explanation": "<p><strong>much</strong> is correct. <em>Homework</em> is one of the famous "
                       "uncountables — never <em>homeworks</em>.<br><br>"
                       "<em>(<strong>much</strong> toʻgʻri. <em>Homework</em> — mashhur sanalmaydigan "
                       "otlardan biri, <em>homeworks</em> deb boʻlmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Can I have two ___ of tea, please?</strong></p>",
        "choices": ["cups", "teas", "cup", "pieces"],
        "correct": "cups",
        "explanation": "<p><strong>cups</strong> is correct. To count an uncountable noun we count its "
                       "container or measure: <em>two cups of tea, three bottles of water</em>.<br><br>"
                       "<em>(<strong>cups</strong> toʻgʻri. Sanalmaydigan otni sanash uchun uning idishi "
                       "yoki oʻlchovi sanaladi: <em>two cups of tea, three bottles of "
                       "water</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The news ___ very good today.</strong></p>",
        "choices": ["is", "are", "were", "have"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct. <em>News</em> ends in <em>-s</em> but it is "
                       "uncountable and singular.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri. <em>News</em> <em>-s</em> bilan tugasa ham "
                       "sanalmaydigan va birlikdagi ot.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The furniture in this shop ___ very expensive.</strong></p>",
        "choices": ["is", "are", "many", "have"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct. <em>Furniture</em> is a collection seen as "
                       "one mass, so the verb is singular.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri. <em>Furniture</em> — yigʻma tushuncha, bir "
                       "butun sifatida koʻriladi, shuning uchun feʼl birlikda boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There isn't ___ milk in the fridge.</strong></p>",
        "choices": ["much", "many", "a few", "few"],
        "correct": "much",
        "explanation": "<p><strong>much</strong> is correct — <em>milk</em> is uncountable, and "
                       "<em>much</em> is very natural in negative sentences.<br><br>"
                       "<em>(<strong>much</strong> toʻgʻri — <em>milk</em> sanalmaydi, <em>much</em> esa "
                       "inkor gaplarda juda tabiiy eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There are ___ chairs in the classroom, so everybody can sit.</strong></p>",
        "choices": ["enough", "much", "a little", "a piece of"],
        "correct": "enough",
        "explanation": "<p><strong>enough</strong> is correct. <em>Enough</em> works with both types; "
                       "<em>much</em> and <em>a little</em> only go with uncountables.<br><br>"
                       "<em>(<strong>enough</strong> toʻgʻri. <em>Enough</em> ikki turdagi ot bilan ham "
                       "keladi, <em>much</em> va <em>a little</em> esa faqat sanalmaydiganlar "
                       "bilan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My mother bought ___ bread on the way home.</strong></p>",
        "choices": ["some", "a", "two", "many"],
        "correct": "some",
        "explanation": "<p><strong>some</strong> is correct. <em>Bread</em> is uncountable, so no "
                       "<em>a</em> and no number in front — <em>some bread</em> or <em>two loaves of "
                       "bread</em>.<br><br>"
                       "<em>(<strong>some</strong> toʻgʻri. <em>Bread</em> sanalmaydi, shuning uchun "
                       "oldiga <em>a</em> ham, son ham qoʻyilmaydi — <em>some bread</em> yoki <em>two "
                       "loaves of bread</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There is ___ traffic in Tashkent in the morning.</strong></p>",
        "choices": ["a lot of", "many", "a few", "several"],
        "correct": "a lot of",
        "explanation": "<p><strong>a lot of</strong> is correct. <em>Traffic</em> is uncountable, and "
                       "<em>a lot of</em> is the friendly option that works with both types.<br><br>"
                       "<em>(<strong>a lot of</strong> toʻgʻri. <em>Traffic</em> sanalmaydi, "
                       "<em>a lot of</em> esa ikki turdagi ot bilan ham ishlatiladigan qulay "
                       "variant.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How ___ luggage are you taking with you?</strong></p>",
        "choices": ["much", "many", "much of", "many of"],
        "correct": "much",
        "explanation": "<p><strong>much</strong> is correct. <em>Luggage</em> is uncountable, like "
                       "<em>furniture</em> and <em>equipment</em>.<br><br>"
                       "<em>(<strong>much</strong> toʻgʻri. <em>Luggage</em> — <em>furniture</em> va "
                       "<em>equipment</em> kabi sanalmaydigan ot.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I have ___ questions about the homework.</strong></p>",
        "choices": ["a few", "a little", "much", "a piece of"],
        "correct": "a few",
        "explanation": "<p><strong>a few</strong> is correct. <em>Questions</em> is a countable plural, "
                       "so it takes <em>a few</em>; <em>a little</em> belongs to uncountables.<br><br>"
                       "<em>(<strong>a few</strong> toʻgʻri. <em>Questions</em> — sanaladigan otning "
                       "koʻpligi, shuning uchun <em>a few</em>; <em>a little</em> esa sanalmaydiganlar "
                       "uchun.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["She gave me two advices.", "She gave me some advice.",
                    "She gave me a piece of advice.", "She gave me a lot of advice."],
        "correct": "She gave me two advices.",
        "explanation": "<p><strong>She gave me two advices.</strong> is the mistake. <em>Advice</em> "
                       "never takes <em>-s</em> — say <em>two pieces of advice</em>.<br><br>"
                       "<em>(<strong>She gave me two advices.</strong> xato. <em>Advice</em> hech qachon "
                       "<em>-s</em> olmaydi — <em>two pieces of advice</em> deyiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["I need a piece of paper.", "I need a papers.",
                    "I need two papers for drawing.", "I need many paper."],
        "correct": "I need a piece of paper.",
        "explanation": "<p><strong>I need a piece of paper.</strong> is correct. As a material "
                       "<em>paper</em> is uncountable, so we count sheets or pieces of it.<br><br>"
                       "<em>(<strong>I need a piece of paper.</strong> toʻgʻri. Material sifatida "
                       "<em>paper</em> sanalmaydi, shuning uchun uning varagʻi yoki boʻlagi "
                       "sanaladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> Would you like some sugar in your tea?</p>"
                "<p><strong>B:</strong> Yes, please — just ___ .</p>",
        "choices": ["a little", "a few", "many", "a number of"],
        "correct": "a little",
        "explanation": "<p><strong>a little</strong> is correct — a small amount of an uncountable "
                       "noun. <em>A few</em> would need countable things (<em>a few sweets</em>)."
                       "<br><br><em>(<strong>a little</strong> toʻgʻri — sanalmaydigan otning ozgina "
                       "miqdori. <em>A few</em> esa sanaladigan narsalar bilan keladi (<em>a few "
                       "sweets</em>).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Our teacher gave us ___ homework, but only ___ exercises were "
                "difficult.</strong></p>",
        "choices": ["a lot of … a few", "many … a little",
                    "a few … much", "much … a little"],
        "correct": "a lot of … a few",
        "explanation": "<p><strong>a lot of … a few</strong> is correct. <em>Homework</em> is "
                       "uncountable (<em>a lot of</em>), <em>exercises</em> is a countable plural "
                       "(<em>a few</em>).<br><br>"
                       "<em>(<strong>a lot of … a few</strong> toʻgʻri. <em>Homework</em> sanalmaydi "
                       "(<em>a lot of</em>), <em>exercises</em> esa sanaladigan otning koʻpligi "
                       "(<em>a few</em>).)</em></p>",
    },
]


# =====================================================================
# PE-3 — Plural Nouns: Regular and Irregular
# =====================================================================

Q_PE3 = [
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>There are three ___ on my desk.</strong></p>",
        "choices": ["books", "bookes", "bookies", "book"],
        "correct": "books",
        "explanation": "<p><strong>books</strong> is correct. Nine nouns out of ten just add "
                       "<strong>-s</strong>.<br><br>"
                       "<em>(<strong>books</strong> toʻgʻri. Oʻntadan toʻqqiz ot shunchaki "
                       "<strong>-s</strong> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>Two ___ stopped in front of the school.</strong></p>",
        "choices": ["buses", "bus", "buss", "busses'"],
        "correct": "buses",
        "explanation": "<p><strong>buses</strong> is correct. After a hissing sound "
                       "(<em>-s, -ss, -sh, -ch, -x, -z</em>) we add <strong>-es</strong> so the ending "
                       "can be heard.<br><br>"
                       "<em>(<strong>buses</strong> toʻgʻri. Hushtakli tovushdan keyin "
                       "(<em>-s, -ss, -sh, -ch, -x, -z</em>) <strong>-es</strong> qoʻshiladi, aks holda "
                       "qoʻshimcha eshitilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>My father repairs ___ .</strong></p>",
        "choices": ["watches", "watchs", "watch", "watchies"],
        "correct": "watches",
        "explanation": "<p><strong>watches</strong> is correct — <em>-ch</em> is a hissing ending, so "
                       "it takes <strong>-es</strong>.<br><br>"
                       "<em>(<strong>watches</strong> toʻgʻri — <em>-ch</em> hushtakli tugash, shuning "
                       "uchun <strong>-es</strong> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>Uzbekistan has many beautiful ___ .</strong></p>",
        "choices": ["cities", "citys", "cityes", "cities'"],
        "correct": "cities",
        "explanation": "<p><strong>cities</strong> is correct. Consonant + <em>y</em> → "
                       "<strong>-ies</strong>.<br><br>"
                       "<em>(<strong>cities</strong> toʻgʻri. Undosh + <em>y</em> → "
                       "<strong>-ies</strong>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>We were on holiday for ten ___ .</strong></p>",
        "choices": ["days", "dais", "dayes", "daies"],
        "correct": "days",
        "explanation": "<p><strong>days</strong> is correct. Look at the letter before the <em>y</em>: "
                       "<em>a</em> is a vowel, so just add <strong>-s</strong>.<br><br>"
                       "<em>(<strong>days</strong> toʻgʻri. <em>y</em> dan oldingi harfga qarang: "
                       "<em>a</em> unli, shuning uchun oddiy <strong>-s</strong>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>There are two ___ on the kitchen table.</strong></p>",
        "choices": ["knives", "knifes", "knifs", "knive"],
        "correct": "knives",
        "explanation": "<p><strong>knives</strong> is correct. Many nouns in <em>-f / -fe</em> change "
                       "to <strong>-ves</strong>: <em>knife → knives, wife → wives, leaf → leaves</em>."
                       "<br><br><em>(<strong>knives</strong> toʻgʻri. <em>-f / -fe</em> bilan tugagan "
                       "koʻp otlar <strong>-ves</strong> ga aylanadi: <em>knife → knives, wife → wives, "
                       "leaf → leaves</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>My mother bought a kilo of ___ .</strong></p>",
        "choices": ["tomatoes", "tomatos", "tomatoies", "tomato"],
        "correct": "tomatoes",
        "explanation": "<p><strong>tomatoes</strong> is correct. Most nouns ending in <em>-o</em> take "
                       "<strong>-es</strong>: <em>potatoes, heroes</em> — but short modern words keep "
                       "plain <em>-s</em>: <em>photos, videos</em>.<br><br>"
                       "<em>(<strong>tomatoes</strong> toʻgʻri. <em>-o</em> bilan tugagan koʻp otlar "
                       "<strong>-es</strong> oladi: <em>potatoes, heroes</em> — lekin qisqargan zamonaviy "
                       "soʻzlar oddiy <em>-s</em> ni saqlaydi: <em>photos, videos</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>I took a lot of ___ at my sister's wedding.</strong></p>",
        "choices": ["photos", "photoes", "photoies", "photo's"],
        "correct": "photos",
        "explanation": "<p><strong>photos</strong> is correct. <em>Photo</em> is a shortened modern "
                       "word, so it keeps plain <strong>-s</strong>.<br><br>"
                       "<em>(<strong>photos</strong> toʻgʻri. <em>Photo</em> — qisqargan zamonaviy soʻz, "
                       "shuning uchun oddiy <strong>-s</strong> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>Five ___ are playing in the yard.</strong></p>",
        "choices": ["children", "childs", "childrens", "childes"],
        "correct": "children",
        "explanation": "<p><strong>children</strong> is correct — an irregular plural you simply learn. "
                       "It is already plural, so never <em>childrens</em>.<br><br>"
                       "<em>(<strong>children</strong> toʻgʻri — yod olinadigan notoʻgʻri koʻplik. U "
                       "allaqachon koʻplikda, shuning uchun <em>childrens</em> boʻlmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>My new shoes hurt my ___ .</strong></p>",
        "choices": ["feet", "foots", "feets", "foot"],
        "correct": "feet",
        "explanation": "<p><strong>feet</strong> is correct. <em>Foot → feet</em>, like "
                       "<em>tooth → teeth</em> and <em>goose → geese</em> — the vowel changes."
                       "<br><br><em>(<strong>feet</strong> toʻgʻri. <em>Foot → feet</em>, xuddi "
                       "<em>tooth → teeth</em> va <em>goose → geese</em> kabi — unli tovush "
                       "oʻzgaradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>The dentist says I must clean my ___ twice a day.</strong></p>",
        "choices": ["teeth", "tooths", "teeths", "tooth"],
        "correct": "teeth",
        "explanation": "<p><strong>teeth</strong> is correct — <em>tooth → teeth</em>.<br><br>"
                       "<em>(<strong>teeth</strong> toʻgʻri — <em>tooth → teeth</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct plural form.</p>"
                "<p><strong>Three ___ were waiting at the gate.</strong></p>",
        "choices": ["men", "mans", "mens", "man"],
        "correct": "men",
        "explanation": "<p><strong>men</strong> is correct: <em>man → men</em>, "
                       "<em>woman → women</em>.<br><br>"
                       "<em>(<strong>men</strong> toʻgʻri: <em>man → men</em>, "
                       "<em>woman → women</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My uncle keeps twenty ___ on his farm.</strong></p>",
        "choices": ["sheep", "sheeps", "sheepes", "sheepies"],
        "correct": "sheep",
        "explanation": "<p><strong>sheep</strong> is correct. A few nouns do not change at all: "
                       "<em>sheep, fish, deer</em> — the number in front shows the plural.<br><br>"
                       "<em>(<strong>sheep</strong> toʻgʻri. Bir necha ot umuman oʻzgarmaydi: "
                       "<em>sheep, fish, deer</em> — koʻplikni oldidagi son koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The ___ in this photo are my classmates.</strong></p>",
        "choices": ["people", "peoples", "persons", "peoplees"],
        "correct": "people",
        "explanation": "<p><strong>people</strong> is correct — it is the normal plural of "
                       "<em>person</em> and already plural, so the verb is <em>are</em>.<br><br>"
                       "<em>(<strong>people</strong> toʻgʻri — <em>person</em> ning oddiy koʻpligi, "
                       "oʻzi koʻplikda, shuning uchun feʼl <em>are</em>.)</em></p>",
    },
    {
        "text": "<p>Which pair is <strong>both correct</strong>?</p>",
        "choices": ["boxes – classes", "boxs – classies", "boxies – classes", "boxes – classs"],
        "correct": "boxes – classes",
        "explanation": "<p><strong>boxes – classes</strong> is correct. Both end in a hissing sound "
                       "(<em>-x</em>, <em>-ss</em>), so both take <strong>-es</strong>.<br><br>"
                       "<em>(<strong>boxes – classes</strong> toʻgʻri. Ikkisi ham hushtakli tovush bilan "
                       "tugaydi (<em>-x</em>, <em>-ss</em>), shuning uchun ikkisi ham "
                       "<strong>-es</strong> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which noun has an irregular plural?</strong></p>",
        "choices": ["mouse", "house", "flower", "window"],
        "correct": "mouse",
        "explanation": "<p><strong>mouse</strong> is correct: <em>mouse → mice</em>. <em>House</em> "
                       "looks similar but is regular: <em>houses</em>.<br><br>"
                       "<em>(<strong>mouse</strong> toʻgʻri: <em>mouse → mice</em>. <em>House</em> "
                       "oʻxshab koʻrinsa ham qoidaga boʻysunadi: <em>houses</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I have two childrens.", "I have two children.",
                    "I have two cousins.", "I have two brothers."],
        "correct": "I have two childrens.",
        "explanation": "<p><strong>I have two childrens.</strong> is the mistake. <em>Children</em> is "
                       "already plural — you cannot add a second <em>-s</em>.<br><br>"
                       "<em>(<strong>I have two childrens.</strong> xato. <em>Children</em> allaqachon "
                       "koʻplikda — ikkinchi <em>-s</em> qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["There are five women in the office.",
                    "There are five womens in the office.",
                    "There are five womans in the office.",
                    "There are five woman in the office."],
        "correct": "There are five women in the office.",
        "explanation": "<p><strong>There are five women in the office.</strong> is correct: "
                       "<em>woman → women</em> (the spelling barely changes, the sound changes a "
                       "lot).<br><br>"
                       "<em>(<strong>There are five women in the office.</strong> toʻgʻri: "
                       "<em>woman → women</em> (yozilishi deyarli oʻzgarmaydi, talaffuzi esa juda "
                       "oʻzgaradi).)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> What did you buy at the bazaar?</p>"
                "<p><strong>B:</strong> ___</p>",
        "choices": ["Some potatoes and two loaves of bread.",
                    "Some potatos and two breads.",
                    "Some potatoes and two breads.",
                    "Some potatos and two loafs of bread."],
        "correct": "Some potatoes and two loaves of bread.",
        "explanation": "<p><strong>Some potatoes and two loaves of bread.</strong> is correct: "
                       "<em>potato → potatoes</em>, <em>loaf → loaves</em>, and <em>bread</em> is "
                       "uncountable so we count loaves.<br><br>"
                       "<em>(<strong>Some potatoes and two loaves of bread.</strong> toʻgʻri: "
                       "<em>potato → potatoes</em>, <em>loaf → loaves</em>, <em>bread</em> esa "
                       "sanalmaydi, shuning uchun nonning boʻlagi sanaladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> plural is correct.</p>",
        "choices": ["families, leaves, mice, keys",
                    "familys, leafs, mouses, keies",
                    "families, leafs, mice, keies",
                    "familyes, leaves, mouses, keys"],
        "correct": "families, leaves, mice, keys",
        "explanation": "<p><strong>families, leaves, mice, keys</strong> is correct — consonant + y → "
                       "<em>-ies</em>, <em>-f</em> → <em>-ves</em>, an irregular plural, and vowel + y → "
                       "plain <em>-s</em>.<br><br>"
                       "<em>(<strong>families, leaves, mice, keys</strong> toʻgʻri — undosh + y → "
                       "<em>-ies</em>, <em>-f</em> → <em>-ves</em>, notoʻgʻri koʻplik va unli + y → "
                       "oddiy <em>-s</em>.)</em></p>",
    },
]


# =====================================================================
# PE-4 — Articles: a, an, the and the Zero Article
# =====================================================================

Q_PE4 = [
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>My father is ___ engineer.</strong></p>",
        "choices": ["an", "a", "the", "— (no article)"],
        "correct": "an",
        "explanation": "<p><strong>an</strong> is correct. <em>Engineer</em> begins with a vowel "
                       "sound.<br><br>"
                       "<em>(<strong>an</strong> toʻgʻri. <em>Engineer</em> unli tovush bilan "
                       "boshlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>My cousin studies at ___ university in Tashkent.</strong></p>",
        "choices": ["a", "an", "the", "— (no article)"],
        "correct": "a",
        "explanation": "<p><strong>a</strong> is correct. Listen, don't look: <em>university</em> is "
                       "pronounced <em>yu-niversity</em>, a consonant sound.<br><br>"
                       "<em>(<strong>a</strong> toʻgʻri. Harfga emas, tovushga qarang: "
                       "<em>university</em> “yuniversity” deb oʻqiladi, yaʼni undosh "
                       "tovush.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>We waited for ___ hour at the bus stop.</strong></p>",
        "choices": ["an", "a", "the", "— (no article)"],
        "correct": "an",
        "explanation": "<p><strong>an</strong> is correct. The <em>h</em> in <em>hour</em> is silent — "
                       "it sounds like <em>auer</em>, a vowel sound.<br><br>"
                       "<em>(<strong>an</strong> toʻgʻri. <em>Hour</em> dagi <em>h</em> oʻqilmaydi — "
                       "“auer” deb talaffuz qilinadi, yaʼni unli tovush.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>Yesterday I bought a book and a pen. ___ book was expensive.</strong></p>",
        "choices": ["The", "A", "An", "— (no article)"],
        "correct": "The",
        "explanation": "<p><strong>The</strong> is correct. First mention → <em>a</em>; after that we "
                       "both know which one → <em>the</em>.<br><br>"
                       "<em>(<strong>The</strong> toʻgʻri. Birinchi eslatishda <em>a</em>, keyin esa "
                       "ikkalamiz ham qaysi biri ekanini bilamiz → <em>the</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>Afsona goes to ___ school by bus every morning.</strong></p>",
        "choices": ["— (no article)", "a", "an", "the"],
        "correct": "— (no article)",
        "explanation": "<p><strong>— (no article)</strong> is correct. When we talk about a place doing "
                       "its normal job we use no article: <em>go to school, go to bed, go to "
                       "work</em>.<br><br>"
                       "<em>(<strong>Artiklsiz</strong> toʻgʻri. Joy oʻzining asosiy vazifasini "
                       "bajarayotgani haqida gapirilsa, artikl qoʻyilmaydi: <em>go to school, go to bed, "
                       "go to work</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>___ sun rises in the east.</strong></p>",
        "choices": ["The", "A", "An", "— (no article)"],
        "correct": "The",
        "explanation": "<p><strong>The</strong> is correct. There is only one sun, so the listener "
                       "always knows which one — unique things take <em>the</em>.<br><br>"
                       "<em>(<strong>The</strong> toʻgʻri. Quyosh bitta, tinglovchi qaysi biri ekanini "
                       "har doim biladi — yakka-yagona narsalar <em>the</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>I like ___ music very much.</strong></p>",
        "choices": ["— (no article)", "a", "an", "the"],
        "correct": "— (no article)",
        "explanation": "<p><strong>— (no article)</strong> is correct. Talking about something in "
                       "general — <em>music, water, dogs, children</em> — takes no article.<br><br>"
                       "<em>(<strong>Artiklsiz</strong> toʻgʻri. Umumiy maʼnoda gapirilganda — "
                       "<em>music, water, dogs, children</em> — artikl qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>Can you close ___ door, please? It's cold.</strong></p>",
        "choices": ["the", "a", "an", "— (no article)"],
        "correct": "the",
        "explanation": "<p><strong>the</strong> is correct. We are both in the room, so there is only "
                       "one obvious door — the listener knows which one.<br><br>"
                       "<em>(<strong>the</strong> toʻgʻri. Ikkalamiz bir xonadamiz, shuning uchun qaysi "
                       "eshik ekani aniq — tinglovchi biladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>Sherbek plays ___ guitar every evening.</strong></p>",
        "choices": ["the", "a", "an", "— (no article)"],
        "correct": "the",
        "explanation": "<p><strong>the</strong> is correct. Musical instruments take <em>the</em>: "
                       "<em>play the guitar, play the piano</em> — but sports take nothing: "
                       "<em>play football</em>.<br><br>"
                       "<em>(<strong>the</strong> toʻgʻri. Musiqa asboblari <em>the</em> oladi: "
                       "<em>play the guitar, play the piano</em> — sport turlari esa artikl olmaydi: "
                       "<em>play football</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>My brother plays ___ football after school.</strong></p>",
        "choices": ["— (no article)", "a", "the", "an"],
        "correct": "— (no article)",
        "explanation": "<p><strong>— (no article)</strong> is correct. Games and sports take no "
                       "article. Compare with <em>play the guitar</em>.<br><br>"
                       "<em>(<strong>Artiklsiz</strong> toʻgʻri. Oʻyin va sport turlari artikl olmaydi. "
                       "<em>Play the guitar</em> bilan solishtiring.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>She is ___ honest girl — everybody trusts her.</strong></p>",
        "choices": ["an", "a", "the", "— (no article)"],
        "correct": "an",
        "explanation": "<p><strong>an</strong> is correct. The <em>h</em> in <em>honest</em> is silent, "
                       "so the word starts with a vowel sound.<br><br>"
                       "<em>(<strong>an</strong> toʻgʻri. <em>Honest</em> dagi <em>h</em> oʻqilmaydi, "
                       "yaʼni soʻz unli tovush bilan boshlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>We had dinner in ___ small restaurant near the station.</strong></p>",
        "choices": ["a", "an", "the", "— (no article)"],
        "correct": "a",
        "explanation": "<p><strong>a</strong> is correct — first mention, and the listener does not yet "
                       "know which restaurant.<br><br>"
                       "<em>(<strong>a</strong> toʻgʻri — birinchi eslatish, tinglovchi hali qaysi "
                       "restoran ekanini bilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair of articles.</p>"
                "<p><strong>I saw ___ cat in our yard. ___ cat was black and very thin.</strong></p>",
        "choices": ["a … The", "the … A", "a … A", "the … The"],
        "correct": "a … The",
        "explanation": "<p><strong>a … The</strong> is correct — this is the first-mention / "
                       "second-mention rule, the heart of the article system.<br><br>"
                       "<em>(<strong>a … The</strong> toʻgʻri — bu birinchi eslatish / ikkinchi eslatish "
                       "qoidasi, artikl tizimining yuragi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>My mother is ___ best cook in our family.</strong></p>",
        "choices": ["the", "a", "an", "— (no article)"],
        "correct": "the",
        "explanation": "<p><strong>the</strong> is correct. A superlative points at one single winner, "
                       "so it always takes <em>the</em>.<br><br>"
                       "<em>(<strong>the</strong> toʻgʻri. Superlative bitta yakka gʻolibni koʻrsatadi, "
                       "shuning uchun doim <em>the</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct article.</p>"
                "<p><strong>Jasur is in ___ hospital — he broke his leg yesterday.</strong></p>",
        "choices": ["— (no article)", "a", "an", "the"],
        "correct": "— (no article)",
        "explanation": "<p><strong>— (no article)</strong> is correct in British English: he is there as "
                       "a patient, which is the building's normal job. <em>The hospital</em> would mean "
                       "one particular building.<br><br>"
                       "<em>(<strong>Artiklsiz</strong> toʻgʻri: u bemor sifatida yotgan, yaʼni bino "
                       "oʻz vazifasini bajarmoqda. <em>The hospital</em> desa, aniq bitta bino "
                       "tushuniladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ books are cheaper than ___ books in that new shop.</strong></p>",
        "choices": ["— … the", "The … —", "A … the", "The … a"],
        "correct": "— … the",
        "explanation": "<p><strong>— … the</strong> is correct. The first <em>books</em> means books in "
                       "general (no article); the second means the particular ones in that shop "
                       "(<em>the</em>).<br><br>"
                       "<em>(<strong>— … the</strong> toʻgʻri. Birinchi <em>books</em> umuman kitoblarni "
                       "bildiradi (artiklsiz), ikkinchisi esa oʻsha doʻkondagi aniq kitoblarni "
                       "(<em>the</em>).)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I am student at school 12.", "I am a student at school 12.",
                    "She is a doctor.", "He is an artist."],
        "correct": "I am student at school 12.",
        "explanation": "<p><strong>I am student at school 12.</strong> is the mistake. Jobs and roles in "
                       "the singular always need <em>a/an</em>: <em>I am a student.</em> Uzbek needs "
                       "nothing there, which is why this mistake is so common.<br><br>"
                       "<em>(<strong>I am student at school 12.</strong> xato. Kasb va rollar birlikda "
                       "har doim <em>a/an</em> talab qiladi: <em>I am a student.</em> Oʻzbekchada hech "
                       "narsa kerak emas — shuning uchun bu xato juda koʻp uchraydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["The Moon goes round the Earth.", "Moon goes round Earth.",
                    "A Moon goes round a Earth.", "The Moon goes round a Earth."],
        "correct": "The Moon goes round the Earth.",
        "explanation": "<p><strong>The Moon goes round the Earth.</strong> is correct — both are unique "
                       "objects, so both take <em>the</em>.<br><br>"
                       "<em>(<strong>The Moon goes round the Earth.</strong> toʻgʻri — ikkisi ham "
                       "yakka-yagona narsa, shuning uchun ikkisi ham <em>the</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> Where is your brother?</p>"
                "<p><strong>B:</strong> He's at ___ , he finishes at six.</p>",
        "choices": ["work", "a work", "the work", "works"],
        "correct": "work",
        "explanation": "<p><strong>work</strong> is correct. <em>Work</em> in this meaning takes no "
                       "article, like <em>school</em> and <em>bed</em>.<br><br>"
                       "<em>(<strong>work</strong> toʻgʻri. Bu maʼnodagi <em>work</em> artikl olmaydi, "
                       "xuddi <em>school</em> va <em>bed</em> kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>all three</strong> articles are correct.</p>",
        "choices": ["I have an idea. The idea is simple: we need a plan.",
                    "I have a idea. The idea is simple: we need an plan.",
                    "I have the idea. A idea is simple: we need the plan.",
                    "I have an idea. A idea is simple: we need the plan."],
        "correct": "I have an idea. The idea is simple: we need a plan.",
        "explanation": "<p><strong>I have an idea. The idea is simple: we need a plan.</strong> is "
                       "correct — <em>an</em> before a vowel sound, <em>the</em> for the second "
                       "mention, <em>a</em> for something new.<br><br>"
                       "<em>(<strong>I have an idea. The idea is simple: we need a plan.</strong> "
                       "toʻgʻri — unli tovush oldidan <em>an</em>, ikkinchi eslatishda <em>the</em>, "
                       "yangi narsa uchun <em>a</em>.)</em></p>",
    },
]


# =====================================================================
# PE-5 — Pronouns: Subject, Object and Possessive
# =====================================================================

Q_PE5 = [
    {
        "text": "<p>Choose the correct pronoun.</p>"
                "<p><strong>___ speaks three languages.</strong></p>",
        "choices": ["She", "Her", "Hers", "Herself"],
        "correct": "She",
        "explanation": "<p><strong>She</strong> is correct. Before the verb we need a subject "
                       "pronoun.<br><br>"
                       "<em>(<strong>She</strong> toʻgʻri. Feʼl oldida subject pronoun kerak "
                       "boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pronoun.</p>"
                "<p><strong>Jasur called ___ yesterday evening.</strong></p>",
        "choices": ["me", "I", "my", "mine"],
        "correct": "me",
        "explanation": "<p><strong>me</strong> is correct. After the verb we need an object "
                       "pronoun.<br><br>"
                       "<em>(<strong>me</strong> toʻgʻri. Feʼldan keyin object pronoun kerak "
                       "boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pronoun.</p>"
                "<p><strong>This is ___ notebook. Please don't take it.</strong></p>",
        "choices": ["my", "me", "mine", "I"],
        "correct": "my",
        "explanation": "<p><strong>my</strong> is correct. A possessive adjective stands in front of a "
                       "noun: <em>my notebook</em>.<br><br>"
                       "<em>(<strong>my</strong> toʻgʻri. Possessive adjective otdan oldin turadi: "
                       "<em>my notebook</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pronoun.</p>"
                "<p><strong>That notebook isn't yours — it's ___ .</strong></p>",
        "choices": ["mine", "my", "me", "myself"],
        "correct": "mine",
        "explanation": "<p><strong>mine</strong> is correct. A possessive pronoun stands alone, with no "
                       "noun after it: <em>my notebook = mine</em>.<br><br>"
                       "<em>(<strong>mine</strong> toʻgʻri. Possessive pronoun yolgʻiz turadi, undan "
                       "keyin ot kelmaydi: <em>my notebook = mine</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pronoun.</p>"
                "<p><strong>Afsona and Sherbek are late. ___ bus didn't come.</strong></p>",
        "choices": ["Their", "They", "Theirs", "Them"],
        "correct": "Their",
        "explanation": "<p><strong>Their</strong> is correct — a noun follows (<em>bus</em>), so we need "
                       "the possessive adjective.<br><br>"
                       "<em>(<strong>Their</strong> toʻgʻri — keyin ot keladi (<em>bus</em>), shuning "
                       "uchun possessive adjective kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pronoun.</p>"
                "<p><strong>Can you help ___ with this exercise, please?</strong></p>",
        "choices": ["us", "we", "our", "ours"],
        "correct": "us",
        "explanation": "<p><strong>us</strong> is correct — after the verb <em>help</em> we need the "
                       "object form.<br><br>"
                       "<em>(<strong>us</strong> toʻgʻri — <em>help</em> feʼlidan keyin object shakli "
                       "kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pronoun.</p>"
                "<p><strong>My little brother is waiting for ___ at the gate.</strong></p>",
        "choices": ["them", "they", "their", "theirs"],
        "correct": "them",
        "explanation": "<p><strong>them</strong> is correct. After a preposition (<em>for, to, with, "
                       "about</em>) we always use the object form.<br><br>"
                       "<em>(<strong>them</strong> toʻgʻri. Predlogdan keyin (<em>for, to, with, "
                       "about</em>) doim object shakli ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pronoun.</p>"
                "<p><strong>The cat is licking ___ paw.</strong></p>",
        "choices": ["its", "it's", "it", "his'"],
        "correct": "its",
        "explanation": "<p><strong>its</strong> is correct — the possessive of <em>it</em>, with no "
                       "apostrophe. <em>It's</em> means <em>it is</em>.<br><br>"
                       "<em>(<strong>its</strong> toʻgʻri — <em>it</em> ning egalik shakli, apostrof "
                       "qoʻyilmaydi. <em>It's</em> esa <em>it is</em> degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ very cold outside today.</strong></p>",
        "choices": ["It's", "Its", "Its'", "It"],
        "correct": "It's",
        "explanation": "<p><strong>It's</strong> is correct — here it means <em>it is</em>. If you can "
                       "say <em>it is</em>, you need the apostrophe.<br><br>"
                       "<em>(<strong>It's</strong> toʻgʻri — bu yerda <em>it is</em> maʼnosida. Agar "
                       "<em>it is</em> deb aytish mumkin boʻlsa, apostrof kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pronoun.</p>"
                "<p><strong>Sherbek made this cake ___ .</strong></p>",
        "choices": ["himself", "him", "his", "he"],
        "correct": "himself",
        "explanation": "<p><strong>himself</strong> is correct. A reflexive pronoun means the person "
                       "did it alone, with nobody's help.<br><br>"
                       "<em>(<strong>himself</strong> toʻgʻri. Reflexive pronoun ish hech kimning "
                       "yordamisiz, oʻzi bajarilganini bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pronoun.</p>"
                "<p><strong>Look at that dog — ___ is following us!</strong></p>",
        "choices": ["it", "he", "its", "him"],
        "correct": "it",
        "explanation": "<p><strong>it</strong> is correct: animals and things take <em>it</em> in the "
                       "subject seat. In Uzbek <em>u</em> covers people, animals and things alike."
                       "<br><br><em>(<strong>it</strong> toʻgʻri: hayvon va narsalar subject oʻrnida "
                       "<em>it</em> boʻladi. Oʻzbekchada esa <em>u</em> odam, hayvon va narsa uchun "
                       "birdek ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>___ gave ___ a beautiful present.</strong></p>",
        "choices": ["They … her", "Them … she", "Their … her", "They … she"],
        "correct": "They … her",
        "explanation": "<p><strong>They … her</strong> is correct: subject form before the verb, object "
                       "form after it.<br><br>"
                       "<em>(<strong>They … her</strong> toʻgʻri: feʼl oldida subject shakli, feʼldan "
                       "keyin object shakli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona and ___ walk to school together.</strong></p>",
        "choices": ["I", "me", "my", "mine"],
        "correct": "I",
        "explanation": "<p><strong>I</strong> is correct. <em>Afsona and I</em> is the subject of "
                       "<em>walk</em>. Test it by removing the other person: <em>I walk</em>, not "
                       "<em>me walk</em>.<br><br>"
                       "<em>(<strong>I</strong> toʻgʻri. <em>Afsona and I</em> — <em>walk</em> feʼlining "
                       "subjecti. Sinash uchun ikkinchi odamni olib tashlang: <em>I walk</em>, "
                       "<em>me walk</em> emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The teacher thanked Jasur and ___ .</strong></p>",
        "choices": ["me", "I", "my", "mine"],
        "correct": "me",
        "explanation": "<p><strong>me</strong> is correct. Here the pair comes after the verb, so the "
                       "object form is needed: <em>thanked me</em>.<br><br>"
                       "<em>(<strong>me</strong> toʻgʻri. Bu yerda juftlik feʼldan keyin turadi, shuning "
                       "uchun object shakli kerak: <em>thanked me</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Is this ___ pen? No, ___ is on the table.</strong></p>",
        "choices": ["your … mine", "yours … my", "your … my", "yours … mine"],
        "correct": "your … mine",
        "explanation": "<p><strong>your … mine</strong> is correct. A noun follows the first gap "
                       "(<em>pen</em>) → possessive adjective; the second gap stands alone → possessive "
                       "pronoun.<br><br>"
                       "<em>(<strong>your … mine</strong> toʻgʻri. Birinchi boʻshliqdan keyin ot keladi "
                       "(<em>pen</em>) → possessive adjective; ikkinchisi yolgʻiz turadi → possessive "
                       "pronoun.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We washed the car ___ , so we didn't pay anything.</strong></p>",
        "choices": ["ourselves", "us", "our", "ours"],
        "correct": "ourselves",
        "explanation": "<p><strong>ourselves</strong> is correct — the reflexive form for <em>we</em>."
                       "<br><br><em>(<strong>ourselves</strong> toʻgʻri — <em>we</em> uchun reflexive "
                       "shakl.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Me and Jasur play chess every evening.",
                    "Jasur and I play chess every evening.",
                    "He plays chess with me every evening.",
                    "We play chess every evening."],
        "correct": "Me and Jasur play chess every evening.",
        "explanation": "<p><strong>Me and Jasur play chess every evening.</strong> is the mistake — the "
                       "subject seat needs <em>I</em>, and politeness puts the other person first: "
                       "<em>Jasur and I</em>.<br><br>"
                       "<em>(<strong>Me and Jasur play chess every evening.</strong> xato — subject "
                       "oʻrnida <em>I</em> kerak, odob yuzasidan esa ikkinchi odam oldin qoʻyiladi: "
                       "<em>Jasur and I</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["The dog wagged its tail.", "The dog wagged it's tail.",
                    "The dog wagged its' tail.", "The dog wagged his' tail."],
        "correct": "The dog wagged its tail.",
        "explanation": "<p><strong>The dog wagged its tail.</strong> is correct. <em>Its</em> = "
                       "belonging to it; <em>it's</em> = <em>it is</em>. Even native speakers mix these "
                       "up.<br><br>"
                       "<em>(<strong>The dog wagged its tail.</strong> toʻgʻri. <em>Its</em> = uning "
                       "(egalik); <em>it's</em> = <em>it is</em>. Bu ikkisini hatto ingliz tili egalari "
                       "ham adashtiradi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> Whose jacket is this?</p>"
                "<p><strong>B:</strong> ___</p>",
        "choices": ["It's hers.", "It's her.", "Its hers.", "It's her's."],
        "correct": "It's hers.",
        "explanation": "<p><strong>It's hers.</strong> is correct: <em>it's</em> = <em>it is</em>, and "
                       "<em>hers</em> is the possessive pronoun standing alone — never with an "
                       "apostrophe.<br><br>"
                       "<em>(<strong>It's hers.</strong> toʻgʻri: <em>it's</em> = <em>it is</em>, "
                       "<em>hers</em> esa yolgʻiz turgan possessive pronoun — apostrof bilan hech qachon "
                       "yozilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> pronoun is correct.</p>",
        "choices": ["She showed us her photos, and we showed her ours.",
                    "She showed we her photos, and us showed her our.",
                    "Her showed us hers photos, and we showed she ours.",
                    "She showed us hers photos, and we showed her our."],
        "correct": "She showed us her photos, and we showed her ours.",
        "explanation": "<p><strong>She showed us her photos, and we showed her ours.</strong> is "
                       "correct — subject <em>she/we</em>, object <em>us/her</em>, possessive adjective "
                       "<em>her + photos</em>, possessive pronoun <em>ours</em> alone.<br><br>"
                       "<em>(<strong>She showed us her photos, and we showed her ours.</strong> "
                       "toʻgʻri — subject <em>she/we</em>, object <em>us/her</em>, possessive adjective "
                       "<em>her + photos</em>, yolgʻiz turgan possessive pronoun <em>ours</em>.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-1 Practice: What Is a Sentence? Subject + Verb",
        "tutorial":    "PE-1:",
        "description": "PE-1 darsiga 20 savol: subject va verb, S–V–O tartibi, chala gaplarni "
                       "tuzatish. Har bir javob ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE1,
    },
    {
        "title":       "PE-2 Practice: Nouns: Countable and Uncountable",
        "tutorial":    "PE-2:",
        "description": "PE-2 darsiga 20 savol: sanaladigan va sanalmaydigan otlar, much/many, "
                       "advice va information kabi tuzoqlar. Javoblar ingliz va oʻzbek tilida "
                       "izohlangan.",
        "questions":   Q_PE2,
    },
    {
        "title":       "PE-3 Practice: Plural Nouns: Regular and Irregular",
        "tutorial":    "PE-3:",
        "description": "PE-3 darsiga 20 savol: -s va -es, city → cities, knife → knives va "
                       "children, feet, mice kabi notoʻgʻri koʻpliklar. Javoblar ingliz va oʻzbek "
                       "tilida izohlangan.",
        "questions":   Q_PE3,
    },
    {
        "title":       "PE-4 Practice: Articles: a, an, the and the Zero Article",
        "tutorial":    "PE-4:",
        "description": "PE-4 darsiga 20 savol: a yoki an (tovushga qarab), birinchi va ikkinchi "
                       "eslatish, artikl qoʻyilmaydigan holatlar. Javoblar ingliz va oʻzbek tilida "
                       "izohlangan.",
        "questions":   Q_PE4,
    },
    {
        "title":       "PE-5 Practice: Pronouns: Subject, Object and Possessive",
        "tutorial":    "PE-5:",
        "description": "PE-5 darsiga 20 savol: I/me, my/mine, its va it's, reflexive olmoshlar. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE5,
    },
]
