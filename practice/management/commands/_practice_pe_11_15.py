# -*- coding: utf-8 -*-
"""Prime English practices — PE-11 … PE-15.

Written with STYLE_GUIDE_PE_PRACTICE.md · lesson list in toc_pe_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_11_15.py --master=prime
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
# PE-11 — Adverbs of Frequency: always, usually, never
# =====================================================================

Q_PE11 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which adverb means 100% — every single time?</strong></p>",
        "choices": ["always", "usually", "sometimes", "never"],
        "correct": "always",
        "explanation": "<p><strong>always</strong> is correct — the top of the scale "
                       "(<em>doim</em>).<br><br>"
                       "<em>(<strong>always</strong> toʻgʻri — shkalaning eng yuqorisi "
                       "(<em>doim</em>).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which adverb means 0% — not even once?</strong></p>",
        "choices": ["never", "rarely", "sometimes", "often"],
        "correct": "never",
        "explanation": "<p><strong>never</strong> is correct (<em>hech qachon</em>). <em>Rarely</em> is "
                       "about 20% — very little, but not zero.<br><br>"
                       "<em>(<strong>never</strong> toʻgʻri (<em>hech qachon</em>). <em>Rarely</em> "
                       "taxminan 20% — juda kam, lekin nol emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct position for the adverb.</p>"
                "<p><strong>I ___ brush my teeth before bed.</strong></p>",
        "choices": ["always", "am always", "always am", "do always"],
        "correct": "always",
        "explanation": "<p><strong>always</strong> is correct. With an ordinary verb the adverb sits "
                       "<em>before</em> the verb: <em>I always brush</em>.<br><br>"
                       "<em>(<strong>always</strong> toʻgʻri. Oddiy feʼl bilan ravish feʼldan "
                       "<em>oldin</em> turadi: <em>I always brush</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>She ___ walks to school.</strong></p>",
        "choices": ["usually", "usual", "usualy", "is usually"],
        "correct": "usually",
        "explanation": "<p><strong>usually</strong> is correct — the adverb form, before the ordinary "
                       "verb <em>walks</em>.<br><br>"
                       "<em>(<strong>usually</strong> toʻgʻri — ravish shakli, oddiy feʼl "
                       "<em>walks</em> dan oldin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ play chess in the evening.</strong></p>",
        "choices": ["often", "are often", "often are", "do often"],
        "correct": "often",
        "explanation": "<p><strong>often</strong> is correct — ordinary verb, so the adverb goes in front "
                       "of it.<br><br>"
                       "<em>(<strong>often</strong> toʻgʻri — oddiy feʼl, shuning uchun ravish uning "
                       "oldiga qoʻyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Jasur ___ late for the lesson.</strong></p>",
        "choices": ["is never", "never is", "never", "does never"],
        "correct": "is never",
        "explanation": "<p><strong>is never</strong> is correct. The other half of the position rule: "
                       "with <em>am / is / are</em> the adverb comes <em>after</em> the verb.<br><br>"
                       "<em>(<strong>is never</strong> toʻgʻri. Qoidaning ikkinchi yarmi: "
                       "<em>am / is / are</em> bilan ravish feʼldan <em>keyin</em> keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My little brother ___ tired after school.</strong></p>",
        "choices": ["is always", "always is", "always", "is always be"],
        "correct": "is always",
        "explanation": "<p><strong>is always</strong> is correct — <em>to be</em> first, adverb second."
                       "<br><br><em>(<strong>is always</strong> toʻgʻri — avval <em>to be</em>, keyin "
                       "ravish.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>They ___ watch TV — they prefer reading.</strong></p>",
        "choices": ["rarely", "are rarely", "rarely are", "don't rarely"],
        "correct": "rarely",
        "explanation": "<p><strong>rarely</strong> is correct — ordinary verb <em>watch</em>, so the "
                       "adverb goes before it.<br><br>"
                       "<em>(<strong>rarely</strong> toʻgʻri — oddiy feʼl <em>watch</em>, shuning uchun "
                       "ravish undan oldin keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ finishes her homework at school.</strong></p>",
        "choices": ["sometimes", "sometime", "some times", "is sometimes"],
        "correct": "sometimes",
        "explanation": "<p><strong>sometimes</strong> is correct — one word, with the <em>-s</em>. "
                       "<em>Sometime</em> (no <em>-s</em>) means “at some unknown time”.<br><br>"
                       "<em>(<strong>sometimes</strong> toʻgʻri — bitta soʻz, <em>-s</em> bilan. "
                       "<em>Sometime</em> (<em>-s</em> siz) “qachondir” degan maʼnoni "
                       "beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ drink coffee. I don't like the taste.</strong></p>",
        "choices": ["never", "don't never", "not never", "never don't"],
        "correct": "never",
        "explanation": "<p><strong>never</strong> is correct. <em>Never</em> already contains the "
                       "negative — adding <em>don't</em> makes a double negative.<br><br>"
                       "<em>(<strong>never</strong> toʻgʻri. <em>Never</em> oʻzida inkorni saqlaydi — "
                       "<em>don't</em> qoʻshilsa, ikki karra inkor boʻlib qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question.</p>"
                "<p><strong>___ do you go to the cinema? — About once a month.</strong></p>",
        "choices": ["How often", "How many", "How much", "How long"],
        "correct": "How often",
        "explanation": "<p><strong>How often</strong> is correct — the question that asks about "
                       "frequency.<br><br>"
                       "<em>(<strong>How often</strong> toʻgʻri — bu takrorlanish (chastota) haqidagi "
                       "savol.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How often do you play football? — ___</strong></p>",
        "choices": ["Twice a week.", "Two times in week.",
                    "Every two week.", "In two week once."],
        "correct": "Twice a week.",
        "explanation": "<p><strong>Twice a week.</strong> is correct. English says <em>once / twice / "
                       "three times a week</em>, with <em>a</em> meaning “each”.<br><br>"
                       "<em>(<strong>Twice a week.</strong> toʻgʻri. Ingliz tilida <em>once / twice / "
                       "three times a week</em> deyiladi, <em>a</em> esa “har” maʼnosini "
                       "beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ my father takes us to the mountains.</strong></p>",
        "choices": ["Sometimes", "Always", "Never", "Rarely"],
        "correct": "Sometimes",
        "explanation": "<p><strong>Sometimes</strong> is correct. A few adverbs — <em>sometimes, "
                       "usually, often</em> — may also start the sentence for emphasis, but "
                       "<em>always</em> and <em>never</em> cannot.<br><br>"
                       "<em>(<strong>Sometimes</strong> toʻgʻri. Baʼzi ravishlar — <em>sometimes, "
                       "usually, often</em> — urgʻu uchun gap boshida ham kelishi mumkin, "
                       "<em>always</em> va <em>never</em> esa kelmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct order.</p>"
                "<p><strong>Which sentence puts the adverb correctly with “to be”?</strong></p>",
        "choices": ["My teacher is usually very patient.",
                    "My teacher usually is very patient.",
                    "My teacher is very patient usually.",
                    "Usually is my teacher very patient."],
        "correct": "My teacher is usually very patient.",
        "explanation": "<p><strong>My teacher is usually very patient.</strong> is correct — the adverb "
                       "goes straight after <em>is</em>.<br><br>"
                       "<em>(<strong>My teacher is usually very patient.</strong> toʻgʻri — ravish "
                       "<em>is</em> dan keyin darhol keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct order.</p>"
                "<p><strong>Which sentence puts the adverb correctly with an ordinary verb?</strong></p>",
        "choices": ["She always helps her mother.", "She helps always her mother.",
                    "Always she helps her mother.", "She helps her mother always."],
        "correct": "She always helps her mother.",
        "explanation": "<p><strong>She always helps her mother.</strong> is correct — the adverb slips "
                       "in between the subject and the verb.<br><br>"
                       "<em>(<strong>She always helps her mother.</strong> toʻgʻri — ravish subject va "
                       "feʼl orasiga kiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ eat meat, but I sometimes eat fish.</strong></p>",
        "choices": ["hardly ever", "hardly never", "not ever hardly", "never ever not"],
        "correct": "hardly ever",
        "explanation": "<p><strong>hardly ever</strong> is correct — it means “almost never” and is "
                       "already negative in meaning.<br><br>"
                       "<em>(<strong>hardly ever</strong> toʻgʻri — “deyarli hech qachon” degani va "
                       "maʼnosi allaqachon inkor.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I don't never drink cola.", "I never drink cola.",
                    "I don't drink cola.", "I rarely drink cola."],
        "correct": "I don't never drink cola.",
        "explanation": "<p><strong>I don't never drink cola.</strong> is the mistake — a double "
                       "negative. Choose one: <em>I never drink</em> or <em>I don't drink</em>."
                       "<br><br><em>(<strong>I don't never drink cola.</strong> xato — ikki karra inkor. "
                       "Bittasini tanlang: <em>I never drink</em> yoki <em>I don't drink</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["My sister is often late.", "My sister often is late.",
                    "My sister is late often always.", "Often my sister is being late."],
        "correct": "My sister is often late.",
        "explanation": "<p><strong>My sister is often late.</strong> is correct — after <em>is</em>."
                       "<br><br><em>(<strong>My sister is often late.</strong> toʻgʻri — <em>is</em> dan "
                       "keyin.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> How often does Sherbek go to the swimming pool?</p>"
                "<p><strong>B:</strong> ___</p>",
        "choices": ["He usually goes on Saturdays.", "He goes usually on Saturdays.",
                    "He is usually go on Saturdays.", "Usually he is going on Saturdays."],
        "correct": "He usually goes on Saturdays.",
        "explanation": "<p><strong>He usually goes on Saturdays.</strong> is correct — subject + adverb "
                       "+ verb, with the Present Simple <em>-s</em>.<br><br>"
                       "<em>(<strong>He usually goes on Saturdays.</strong> toʻgʻri — subject + ravish + "
                       "feʼl, Present Simple <em>-s</em> qoʻshimchasi bilan.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> adverb is in the right place.</p>",
        "choices": ["Afsona is always busy, so she rarely watches TV and never plays computer games.",
                    "Afsona always is busy, so she watches rarely TV and plays never computer games.",
                    "Afsona is always busy, so she doesn't never watch TV and never plays computer games.",
                    "Always Afsona is busy, so rarely she watches TV and she plays never computer games."],
        "correct": "Afsona is always busy, so she rarely watches TV and never plays computer games.",
        "explanation": "<p><strong>Afsona is always busy, so she rarely watches TV and never plays "
                       "computer games.</strong> is correct — after <em>is</em>, but before the ordinary "
                       "verbs, and no double negative.<br><br>"
                       "<em>(<strong>Afsona is always busy, so she rarely watches TV and never plays "
                       "computer games.</strong> toʻgʻri — <em>is</em> dan keyin, oddiy feʼllardan esa "
                       "oldin, ikki karra inkor ham yoʻq.)</em></p>",
    },
]


# =====================================================================
# PE-12 — Present Continuous: Happening Right Now
# =====================================================================

Q_PE12 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Be quiet! The baby ___ .</strong></p>",
        "choices": ["is sleeping", "sleeps", "sleep", "is sleep"],
        "correct": "is sleeping",
        "explanation": "<p><strong>is sleeping</strong> is correct. The Present Continuous is "
                       "<em>am / is / are + verb-ing</em>, for an action in progress right now.<br><br>"
                       "<em>(<strong>is sleeping</strong> toʻgʻri. Present Continuous "
                       "<em>am / is / are + feʼl-ing</em> shaklida boʻlib, hozir davom etayotgan "
                       "harakat uchun ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ this exercise at the moment.</strong></p>",
        "choices": ["am doing", "do", "doing", "am do"],
        "correct": "am doing",
        "explanation": "<p><strong>am doing</strong> is correct — <em>I</em> takes <em>am</em>, and the "
                       "verb takes <em>-ing</em>. Both pieces are needed.<br><br>"
                       "<em>(<strong>am doing</strong> toʻgʻri — <em>I</em> <em>am</em> oladi, feʼl esa "
                       "<em>-ing</em>. Ikki boʻlak ham kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Look! The children ___ in the garden.</strong></p>",
        "choices": ["are playing", "is playing", "play", "playing"],
        "correct": "are playing",
        "explanation": "<p><strong>are playing</strong> is correct — plural subject → <em>are</em>. "
                       "<em>Look!</em> is a classic signal for this tense.<br><br>"
                       "<em>(<strong>are playing</strong> toʻgʻri — koʻplikdagi subject → <em>are</em>. "
                       "<em>Look!</em> — bu zamonning klassik signali.)</em></p>",
    },
    {
        "text": "<p>Choose the correct -ing form.</p>"
                "<p><strong>make → ___</strong></p>",
        "choices": ["making", "makeing", "makking", "makein"],
        "correct": "making",
        "explanation": "<p><strong>making</strong> is correct. A silent <em>-e</em> at the end drops "
                       "before <em>-ing</em>: <em>write → writing, come → coming</em>.<br><br>"
                       "<em>(<strong>making</strong> toʻgʻri. Oxiridagi oʻqilmaydigan <em>-e</em> "
                       "<em>-ing</em> dan oldin tushib qoladi: <em>write → writing, come → "
                       "coming</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct -ing form.</p>"
                "<p><strong>sit → ___</strong></p>",
        "choices": ["sitting", "siting", "sitteing", "sitin"],
        "correct": "sitting",
        "explanation": "<p><strong>sitting</strong> is correct. One short vowel + one consonant → double "
                       "the consonant: <em>run → running, swim → swimming</em>.<br><br>"
                       "<em>(<strong>sitting</strong> toʻgʻri. Bitta qisqa unli + bitta undosh → undosh "
                       "ikkilanadi: <em>run → running, swim → swimming</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My mother ___ dinner in the kitchen now.</strong></p>",
        "choices": ["is cooking", "cooks", "are cooking", "cooking"],
        "correct": "is cooking",
        "explanation": "<p><strong>is cooking</strong> is correct — one person + <em>now</em>.<br><br>"
                       "<em>(<strong>is cooking</strong> toʻgʻri — bitta shaxs + <em>now</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Jasur ___ TV — he is doing his homework.</strong></p>",
        "choices": ["isn't watching", "doesn't watching", "not watching", "isn't watch"],
        "correct": "isn't watching",
        "explanation": "<p><strong>isn't watching</strong> is correct. Because the first word is "
                       "<em>to be</em>, the negative needs no <em>do</em> — just add <em>not</em>."
                       "<br><br><em>(<strong>isn't watching</strong> toʻgʻri. Birinchi soʻz "
                       "<em>to be</em> boʻlgani uchun inkorga <em>do</em> kerak emas — shunchaki "
                       "<em>not</em> qoʻshiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question.</p>"
                "<p><strong>___ you listening to me?</strong></p>",
        "choices": ["Are", "Do", "Is", "Does"],
        "correct": "Are",
        "explanation": "<p><strong>Are</strong> is correct — the <em>to be</em> part jumps to the front, "
                       "exactly as in PE-6.<br><br>"
                       "<em>(<strong>Are</strong> toʻgʻri — <em>to be</em> qismi gap boshiga chiqadi, "
                       "xuddi PE-6 dagidek.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What ___ you ___ now?</strong></p>",
        "choices": ["are … doing", "do … doing", "are … do", "do … do"],
        "correct": "are … doing",
        "explanation": "<p><strong>are … doing</strong> is correct: "
                       "<em>question word + am/is/are + subject + verb-ing</em>.<br><br>"
                       "<em>(<strong>are … doing</strong> toʻgʻri: <em>soʻroq soʻzi + am/is/are + "
                       "subject + feʼl-ing</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My father ___ in Kazakhstan this month, but he usually works "
                "here.</strong></p>",
        "choices": ["is working", "works", "work", "is work"],
        "correct": "is working",
        "explanation": "<p><strong>is working</strong> is correct. The Continuous also covers temporary "
                       "situations — true now, but not forever.<br><br>"
                       "<em>(<strong>is working</strong> toʻgʻri. Continuous vaqtinchalik holatlarni ham "
                       "qamrab oladi — hozir toʻgʻri, lekin doimiy emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which time expression belongs to the Present Continuous?</strong></p>",
        "choices": ["at the moment", "every Monday", "usually", "twice a week"],
        "correct": "at the moment",
        "explanation": "<p><strong>at the moment</strong> is correct. Signals for this tense: "
                       "<em>now, at the moment, today, this week, Look!, Listen!</em><br><br>"
                       "<em>(<strong>at the moment</strong> toʻgʻri. Bu zamon signallari: "
                       "<em>now, at the moment, today, this week, Look!, Listen!</em>)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ for the bus. It's late again.</strong></p>",
        "choices": ["are waiting", "wait", "waiting", "are wait"],
        "correct": "are waiting",
        "explanation": "<p><strong>are waiting</strong> is correct — the action is in progress at this "
                       "moment.<br><br>"
                       "<em>(<strong>are waiting</strong> toʻgʻri — harakat hozir davom "
                       "etmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Afsona usually ___ tea, but today she ___ coffee.</strong></p>",
        "choices": ["drinks … is drinking", "is drinking … drinks",
                    "drinks … drinks", "is drinking … is drinking"],
        "correct": "drinks … is drinking",
        "explanation": "<p><strong>drinks … is drinking</strong> is correct. <em>Usually</em> → Present "
                       "Simple; <em>today</em> → Present Continuous.<br><br>"
                       "<em>(<strong>drinks … is drinking</strong> toʻgʻri. <em>Usually</em> → Present "
                       "Simple; <em>today</em> → Present Continuous.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Listen! Somebody ___ the door.</strong></p>",
        "choices": ["is knocking at", "knocks at", "knocking at", "is knock at"],
        "correct": "is knocking at",
        "explanation": "<p><strong>is knocking at</strong> is correct — <em>Listen!</em> tells you the "
                       "action is happening this second.<br><br>"
                       "<em>(<strong>is knocking at</strong> toʻgʻri — <em>Listen!</em> harakat shu "
                       "daqiqada boʻlayotganini bildiradi.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Is your brother studying now? — No, ___ .</strong></p>",
        "choices": ["he isn't", "he doesn't", "he not", "he isn't studying not"],
        "correct": "he isn't",
        "explanation": "<p><strong>he isn't</strong> is correct — the short answer repeats "
                       "<em>am / is / are</em>, never <em>do</em>.<br><br>"
                       "<em>(<strong>he isn't</strong> toʻgʻri — qisqa javobda <em>am / is / are</em> "
                       "takrorlanadi, <em>do</em> emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence describes a picture you are looking at?</strong></p>",
        "choices": ["A boy is riding a bike and a woman is selling flowers.",
                    "A boy rides a bike and a woman sells flowers.",
                    "A boy ride a bike and a woman sell flowers.",
                    "A boy is ride a bike and a woman is sell flowers."],
        "correct": "A boy is riding a bike and a woman is selling flowers.",
        "explanation": "<p><strong>A boy is riding a bike and a woman is selling flowers.</strong> is "
                       "correct. Describing what is happening in a picture is a classic job of this "
                       "tense.<br><br>"
                       "<em>(<strong>A boy is riding a bike and a woman is selling flowers.</strong> "
                       "toʻgʻri. Rasmda nima boʻlayotganini taʼriflash — bu zamonning klassik "
                       "vazifasi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I reading a very interesting book.", "I am reading a very interesting book.",
                    "I'm reading a very interesting book.", "I am not reading now."],
        "correct": "I reading a very interesting book.",
        "explanation": "<p><strong>I reading a very interesting book.</strong> is the mistake — "
                       "<em>am</em> is missing. Uzbek needs one word (<em>oʻqiyapman</em>), English needs "
                       "two pieces.<br><br>"
                       "<em>(<strong>I reading a very interesting book.</strong> xato — <em>am</em> "
                       "yoʻq. Oʻzbekchada bitta soʻz yetarli (<em>oʻqiyapman</em>), ingliz tilida esa "
                       "ikki boʻlak kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["They are swimming in the river.", "They are swiming in the river.",
                    "They is swimming in the river.", "They swimming in the river."],
        "correct": "They are swimming in the river.",
        "explanation": "<p><strong>They are swimming in the river.</strong> is correct — plural "
                       "<em>are</em>, and <em>swim</em> doubles its <em>m</em>.<br><br>"
                       "<em>(<strong>They are swimming in the river.</strong> toʻgʻri — koʻplik uchun "
                       "<em>are</em>, <em>swim</em> esa <em>m</em> ni ikkilaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> Where's Sherbek?</p>"
                "<p><strong>B:</strong> ___</p>",
        "choices": ["He's having a shower.", "He has a shower now.",
                    "He is have a shower.", "He having a shower."],
        "correct": "He's having a shower.",
        "explanation": "<p><strong>He's having a shower.</strong> is correct — an action in progress "
                       "right now, so Continuous.<br><br>"
                       "<em>(<strong>He's having a shower.</strong> toʻgʻri — hozir davom etayotgan "
                       "harakat, shuning uchun Continuous.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> verb is correct.</p>",
        "choices": ["I'm writing a letter, my sister is making tea and the cat is sitting on the sofa.",
                    "I'm writeing a letter, my sister is makeing tea and the cat is siting on the sofa.",
                    "I writing a letter, my sister making tea and the cat sitting on the sofa.",
                    "I'm writing a letter, my sister are making tea and the cat are sitting on the sofa."],
        "correct": "I'm writing a letter, my sister is making tea and the cat is sitting on the sofa.",
        "explanation": "<p><strong>I'm writing … is making … is sitting …</strong> is correct — the "
                       "silent <em>-e</em> drops, the short vowel doubles the consonant, and every "
                       "subject has its own <em>am / is</em>.<br><br>"
                       "<em>(<strong>I'm writing … is making … is sitting …</strong> toʻgʻri — "
                       "oʻqilmaydigan <em>-e</em> tushadi, qisqa unlidan keyin undosh ikkilanadi, har bir "
                       "subject esa oʻz <em>am / is</em> ini oladi.)</em></p>",
    },
]


# =====================================================================
# PE-13 — Present Simple vs Present Continuous
# =====================================================================

Q_PE13 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sherbek ___ football every Sunday.</strong></p>",
        "choices": ["plays", "is playing", "play", "playing"],
        "correct": "plays",
        "explanation": "<p><strong>plays</strong> is correct. <em>Every Sunday</em> = a repeated habit → "
                       "Present Simple.<br><br>"
                       "<em>(<strong>plays</strong> toʻgʻri. <em>Every Sunday</em> = takrorlanadigan "
                       "odat → Present Simple.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sherbek ___ football right now.</strong></p>",
        "choices": ["is playing", "plays", "play", "is play"],
        "correct": "is playing",
        "explanation": "<p><strong>is playing</strong> is correct. <em>Right now</em> → the action is in "
                       "progress → Present Continuous.<br><br>"
                       "<em>(<strong>is playing</strong> toʻgʻri. <em>Right now</em> → harakat davom "
                       "etmoqda → Present Continuous.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Water ___ at 100 degrees.</strong></p>",
        "choices": ["boils", "is boiling", "boil", "are boiling"],
        "correct": "boils",
        "explanation": "<p><strong>boils</strong> is correct — a general truth, always true.<br><br>"
                       "<em>(<strong>boils</strong> toʻgʻri — umumiy haqiqat, doim "
                       "toʻgʻri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The water ___ — turn off the gas!</strong></p>",
        "choices": ["is boiling", "boils", "boil", "is boil"],
        "correct": "is boiling",
        "explanation": "<p><strong>is boiling</strong> is correct — this particular water, at this "
                       "moment.<br><br>"
                       "<em>(<strong>is boiling</strong> toʻgʻri — aynan shu suv, aynan shu "
                       "daqiqada.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which question decides between the two tenses?</strong></p>",
        "choices": ["Always / in general, or now / temporarily?",
                    "Past or future?",
                    "Positive or negative?",
                    "Countable or uncountable?"],
        "correct": "Always / in general, or now / temporarily?",
        "explanation": "<p><strong>Always / in general, or now / temporarily?</strong> is correct — that "
                       "one question is the whole decision.<br><br>"
                       "<em>(<strong>Always / in general, or now / temporarily?</strong> toʻgʻri — "
                       "butun tanlov aynan shu savolga bogʻliq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ in Fergana with her family.</strong></p>",
        "choices": ["lives", "is living", "live", "living"],
        "correct": "lives",
        "explanation": "<p><strong>lives</strong> is correct — a permanent situation, with no hint that "
                       "it is temporary.<br><br>"
                       "<em>(<strong>lives</strong> toʻgʻri — doimiy holat, vaqtinchalik ekaniga ishora "
                       "yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>She ___ with her aunt this month while her parents are abroad.</strong></p>",
        "choices": ["is living", "lives", "live", "is live"],
        "correct": "is living",
        "explanation": "<p><strong>is living</strong> is correct — <em>this month</em> marks it as "
                       "temporary.<br><br>"
                       "<em>(<strong>is living</strong> toʻgʻri — <em>this month</em> uning "
                       "vaqtinchalik ekanini koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ what you mean.</strong></p>",
        "choices": ["understand", "am understanding", "understanding", "am understand"],
        "correct": "understand",
        "explanation": "<p><strong>understand</strong> is correct. Stative verbs — <em>understand, know, "
                       "like, want, need, believe</em> — describe states, not actions, so they take no "
                       "<em>-ing</em>.<br><br>"
                       "<em>(<strong>understand</strong> toʻgʻri. Holat feʼllari — <em>understand, know, "
                       "like, want, need, believe</em> — harakatni emas, holatni bildiradi, shuning uchun "
                       "<em>-ing</em> olmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ this song very much.</strong></p>",
        "choices": ["likes", "is liking", "like", "is like"],
        "correct": "likes",
        "explanation": "<p><strong>likes</strong> is correct — <em>like</em> is a stative verb, so it "
                       "stays simple even when we mean “right now”.<br><br>"
                       "<em>(<strong>likes</strong> toʻgʻri — <em>like</em> holat feʼli, shuning uchun "
                       "“hozir” maʼnosida ham Simple da qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which verb is a stative verb (no -ing)?</strong></p>",
        "choices": ["know", "run", "write", "eat"],
        "correct": "know",
        "explanation": "<p><strong>know</strong> is correct — you cannot say <em>I am knowing</em>. The "
                       "others are all real, visible actions.<br><br>"
                       "<em>(<strong>know</strong> toʻgʻri — <em>I am knowing</em> deb boʻlmaydi. "
                       "Qolganlari esa haqiqiy, koʻrinadigan harakatlar.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My mother ___ in a school, but this week she ___ from home.</strong></p>",
        "choices": ["works … is working", "is working … works",
                    "works … works", "is working … is working"],
        "correct": "works … is working",
        "explanation": "<p><strong>works … is working</strong> is correct — the permanent fact first, "
                       "the temporary exception second.<br><br>"
                       "<em>(<strong>works … is working</strong> toʻgʻri — avval doimiy fakt, keyin "
                       "vaqtinchalik istisno.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Look! It ___ .</strong></p>",
        "choices": ["is raining", "rains", "rain", "is rain"],
        "correct": "is raining",
        "explanation": "<p><strong>is raining</strong> is correct — <em>Look!</em> points at this "
                       "moment.<br><br>"
                       "<em>(<strong>is raining</strong> toʻgʻri — <em>Look!</em> shu daqiqaga ishora "
                       "qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It often ___ in Tashkent in March.</strong></p>",
        "choices": ["rains", "is raining", "rain", "raining"],
        "correct": "rains",
        "explanation": "<p><strong>rains</strong> is correct — <em>often</em> makes it a general "
                       "pattern.<br><br>"
                       "<em>(<strong>rains</strong> toʻgʻri — <em>often</em> uni umumiy holatga "
                       "aylantiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What ___ your father usually ___ after work?</strong></p>",
        "choices": ["does … do", "is … doing", "does … doing", "is … do"],
        "correct": "does … do",
        "explanation": "<p><strong>does … do</strong> is correct — <em>usually</em> means a habit, so we "
                       "need the Present Simple question with <em>does</em>.<br><br>"
                       "<em>(<strong>does … do</strong> toʻgʻri — <em>usually</em> odatni bildiradi, "
                       "shuning uchun <em>does</em> bilan Present Simple savoli kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ of buying a new phone. What do you think?</strong></p>",
        "choices": ["am thinking", "think", "am think", "thinking"],
        "correct": "am thinking",
        "explanation": "<p><strong>am thinking</strong> is correct. <em>Think of / about</em> = a mental "
                       "activity in progress, so the Continuous works. But <em>I think it's "
                       "true</em> (= my opinion) stays simple.<br><br>"
                       "<em>(<strong>am thinking</strong> toʻgʻri. <em>Think of / about</em> = davom "
                       "etayotgan fikrlash jarayoni, shuning uchun Continuous. Lekin <em>I think it's "
                       "true</em> (= mening fikrim) Simple da qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>She ___ a shower at the moment.</strong></p>",
        "choices": ["is having", "has", "is have", "having"],
        "correct": "is having",
        "explanation": "<p><strong>is having</strong> is correct. <em>Have</em> = possess is stative "
                       "(<em>she has a car</em>), but <em>have a shower / have lunch</em> is an action, "
                       "so it can take <em>-ing</em>.<br><br>"
                       "<em>(<strong>is having</strong> toʻgʻri. <em>Have</em> = egalik holat feʼli "
                       "(<em>she has a car</em>), lekin <em>have a shower / have lunch</em> — harakat, "
                       "shuning uchun <em>-ing</em> olishi mumkin.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I am wanting a cold drink.", "I want a cold drink.",
                    "I am drinking cold water.", "I usually drink water."],
        "correct": "I am wanting a cold drink.",
        "explanation": "<p><strong>I am wanting a cold drink.</strong> is the mistake — <em>want</em> is "
                       "stative and never takes <em>-ing</em>.<br><br>"
                       "<em>(<strong>I am wanting a cold drink.</strong> xato — <em>want</em> holat feʼli "
                       "va hech qachon <em>-ing</em> olmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["My brother is watching TV at the moment.",
                    "My brother watches TV at the moment.",
                    "My brother watch TV at the moment.",
                    "My brother is watch TV at the moment."],
        "correct": "My brother is watching TV at the moment.",
        "explanation": "<p><strong>My brother is watching TV at the moment.</strong> is correct — "
                       "<em>at the moment</em> demands the Continuous.<br><br>"
                       "<em>(<strong>My brother is watching TV at the moment.</strong> toʻgʻri — "
                       "<em>at the moment</em> Continuous ni talab qiladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> Can you help me with this exercise?</p>"
                "<p><strong>B:</strong> Sorry, ___ my own homework.</p>",
        "choices": ["I'm doing", "I do", "I am do", "I doing"],
        "correct": "I'm doing",
        "explanation": "<p><strong>I'm doing</strong> is correct — an action in progress that explains "
                       "why I can't help now.<br><br>"
                       "<em>(<strong>I'm doing</strong> toʻgʻri — hozir davom etayotgan harakat, shuning "
                       "uchun yordam bera olmayman.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>both</strong> tenses are used correctly.</p>",
        "choices": ["Jasur usually studies in the library, but today he is studying at home.",
                    "Jasur usually is studying in the library, but today he studies at home.",
                    "Jasur usually studying in the library, but today he study at home.",
                    "Jasur usually is study in the library, but today he is studies at home."],
        "correct": "Jasur usually studies in the library, but today he is studying at home.",
        "explanation": "<p><strong>Jasur usually studies in the library, but today he is studying at "
                       "home.</strong> is correct — <em>usually</em> → Simple, <em>today</em> → "
                       "Continuous.<br><br>"
                       "<em>(<strong>Jasur usually studies in the library, but today he is studying at "
                       "home.</strong> toʻgʻri — <em>usually</em> → Simple, <em>today</em> → "
                       "Continuous.)</em></p>",
    },
]


# =====================================================================
# PE-14 — have / have got: Talking About Possession
# =====================================================================

Q_PE14 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ two sisters and one brother.</strong></p>",
        "choices": ["have", "has", "am have", "having"],
        "correct": "have",
        "explanation": "<p><strong>have</strong> is correct — <em>I, you, we, they</em> take "
                       "<em>have</em>.<br><br>"
                       "<em>(<strong>have</strong> toʻgʻri — <em>I, you, we, they</em> <em>have</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My uncle ___ a small shop in the bazaar.</strong></p>",
        "choices": ["has", "have", "haves", "is have"],
        "correct": "has",
        "explanation": "<p><strong>has</strong> is correct — <em>he / she / it</em> takes "
                       "<em>has</em>.<br><br>"
                       "<em>(<strong>has</strong> toʻgʻri — <em>he / she / it</em> <em>has</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ got a new bicycle.</strong></p>",
        "choices": ["has", "have", "is", "does"],
        "correct": "has",
        "explanation": "<p><strong>has</strong> is correct — in <em>have got</em> only the first part "
                       "changes: <em>he / she / it has got</em>.<br><br>"
                       "<em>(<strong>has</strong> toʻgʻri — <em>have got</em> da faqat birinchi qism "
                       "oʻzgaradi: <em>he / she / it has got</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct short form.</p>"
                "<p><strong>I have got a new phone. → ___ a new phone.</strong></p>",
        "choices": ["I've got", "I'm got", "I got", "I has got"],
        "correct": "I've got",
        "explanation": "<p><strong>I've got</strong> is correct. In speech <em>have got</em> is almost "
                       "always shortened: <em>I've got, he's got, we've got</em>.<br><br>"
                       "<em>(<strong>I've got</strong> toʻgʻri. Nutqda <em>have got</em> deyarli doim "
                       "qisqartiriladi: <em>I've got, he's got, we've got</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you got any brothers?</strong></p>",
        "choices": ["Have", "Do", "Are", "Does"],
        "correct": "Have",
        "explanation": "<p><strong>Have</strong> is correct. <em>Have got</em> asks questions by itself, "
                       "like <em>to be</em> — no <em>do</em>.<br><br>"
                       "<em>(<strong>Have</strong> toʻgʻri. <em>Have got</em> savolni oʻzi beradi, xuddi "
                       "<em>to be</em> kabi — <em>do</em> kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you have a driving licence?</strong></p>",
        "choices": ["Do", "Have", "Are", "Has"],
        "correct": "Do",
        "explanation": "<p><strong>Do</strong> is correct. Plain <em>have</em> (without <em>got</em>) "
                       "behaves like an ordinary verb and needs <em>do / does</em>.<br><br>"
                       "<em>(<strong>Do</strong> toʻgʻri. <em>Got</em> siz oddiy <em>have</em> boshqa "
                       "feʼllar kabi ishlaydi va <em>do / does</em> talab qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sherbek ___ got a car — he goes to work by bus.</strong></p>",
        "choices": ["hasn't", "haven't", "doesn't", "isn't"],
        "correct": "hasn't",
        "explanation": "<p><strong>hasn't</strong> is correct — the <em>have got</em> negative is "
                       "<em>hasn't got / haven't got</em>, with no helper.<br><br>"
                       "<em>(<strong>hasn't</strong> toʻgʻri — <em>have got</em> inkori "
                       "<em>hasn't got / haven't got</em> boʻlib, yordamchi kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My grandparents ___ have a computer.</strong></p>",
        "choices": ["don't", "haven't", "aren't", "doesn't"],
        "correct": "don't",
        "explanation": "<p><strong>don't</strong> is correct — with plain <em>have</em> the negative "
                       "needs <em>don't / doesn't</em>.<br><br>"
                       "<em>(<strong>don't</strong> toʻgʻri — oddiy <em>have</em> bilan inkorga "
                       "<em>don't / doesn't</em> kerak.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Has your sister got a bike? — Yes, ___ .</strong></p>",
        "choices": ["she has", "she does", "she is", "she got"],
        "correct": "she has",
        "explanation": "<p><strong>she has</strong> is correct — the answer repeats the same word that "
                       "started the question.<br><br>"
                       "<em>(<strong>she has</strong> toʻgʻri — javobda savolni boshlagan soʻz "
                       "takrorlanadi.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Do you have a pet? — No, ___ .</strong></p>",
        "choices": ["I don't", "I haven't", "I'm not", "I not have"],
        "correct": "I don't",
        "explanation": "<p><strong>I don't</strong> is correct — the question used <em>do</em>, so the "
                       "answer does too.<br><br>"
                       "<em>(<strong>I don't</strong> toʻgʻri — savolda <em>do</em> ishlatilgan, javobda "
                       "ham shunday.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We usually ___ breakfast at seven.</strong></p>",
        "choices": ["have", "have got", "has", "are having got"],
        "correct": "have",
        "explanation": "<p><strong>have</strong> is correct. This is the “other” <em>have</em> — an "
                       "action, not possession: <em>have breakfast, have a shower, have a good "
                       "time</em>. You can never add <em>got</em> to it.<br><br>"
                       "<em>(<strong>have</strong> toʻgʻri. Bu — “boshqa” <em>have</em>: egalik emas, "
                       "harakat: <em>have breakfast, have a shower, have a good time</em>. Unga "
                       "<em>got</em> qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is about an <em>action</em>, not possession?</strong></p>",
        "choices": ["I'm having lunch with my cousin.", "I have a new bag.",
                    "I've got two sisters.", "She has a red bike."],
        "correct": "I'm having lunch with my cousin.",
        "explanation": "<p><strong>I'm having lunch with my cousin.</strong> is correct — <em>have "
                       "lunch</em> is an activity, so it can be Continuous. Possession never can.<br><br>"
                       "<em>(<strong>I'm having lunch with my cousin.</strong> toʻgʻri — <em>have "
                       "lunch</em> faoliyat, shuning uchun Continuous boʻlishi mumkin. Egalik esa hech "
                       "qachon.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In “He's got a headache”, what does <em>'s</em> mean?</strong></p>",
        "choices": ["has", "is", "does", "was"],
        "correct": "has",
        "explanation": "<p><strong>has</strong> is correct. Before <em>got</em>, <em>'s</em> is always "
                       "<em>has</em>. Compare <em>He's a doctor</em> = <em>he is</em>.<br><br>"
                       "<em>(<strong>has</strong> toʻgʻri. <em>Got</em> dan oldin <em>'s</em> doim "
                       "<em>has</em> boʻladi. <em>He's a doctor</em> = <em>he is</em> bilan "
                       "solishtiring.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which form is better in a formal exam essay?</strong></p>",
        "choices": ["Many families have two cars.", "Many families have got two cars.",
                    "Many families has got two cars.", "Many families got two cars."],
        "correct": "Many families have two cars.",
        "explanation": "<p><strong>Many families have two cars.</strong> is correct. <em>Have got</em> is "
                       "friendly spoken British English; plain <em>have</em> is the safer choice in "
                       "writing.<br><br>"
                       "<em>(<strong>Many families have two cars.</strong> toʻgʻri. <em>Have got</em> — "
                       "ogʻzaki britancha uslub; yozma ishda oddiy <em>have</em> xavfsizroq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How many cousins ___ you got?</strong></p>",
        "choices": ["have", "do", "are", "has"],
        "correct": "have",
        "explanation": "<p><strong>have</strong> is correct — the <em>got</em> at the end tells you which "
                       "system this question uses.<br><br>"
                       "<em>(<strong>have</strong> toʻgʻri — oxiridagi <em>got</em> qaysi tizim "
                       "ishlatilganini koʻrsatib turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Did you ___ a good time at the wedding?</strong></p>",
        "choices": ["have", "have got", "has", "having"],
        "correct": "have",
        "explanation": "<p><strong>have</strong> is correct — <em>have a good time</em> is a fixed "
                       "expression, and after <em>did</em> the verb is bare.<br><br>"
                       "<em>(<strong>have</strong> toʻgʻri — <em>have a good time</em> qatʼiy ibora, "
                       "<em>did</em> dan keyin esa feʼl oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Do you have got a pen?", "Do you have a pen?",
                    "Have you got a pen?", "Have you a pen?"],
        "correct": "Do you have got a pen?",
        "explanation": "<p><strong>Do you have got a pen?</strong> is the mistake — it mixes the two "
                       "systems. Choose one: <em>Do you have …?</em> or <em>Have you got …?</em><br><br>"
                       "<em>(<strong>Do you have got a pen?</strong> xato — ikki tizim aralashib ketgan. "
                       "Bittasini tanlang: <em>Do you have …?</em> yoki <em>Have you got "
                       "…?</em>)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["My friend hasn't got any brothers.", "My friend haven't got any brothers.",
                    "My friend doesn't got any brothers.", "My friend not has got any brothers."],
        "correct": "My friend hasn't got any brothers.",
        "explanation": "<p><strong>My friend hasn't got any brothers.</strong> is correct — one person → "
                       "<em>hasn't got</em>.<br><br>"
                       "<em>(<strong>My friend hasn't got any brothers.</strong> toʻgʻri — bitta shaxs → "
                       "<em>hasn't got</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> Have you got any homework today?</p>"
                "<p><strong>B:</strong> ___</p>",
        "choices": ["Yes, I've got a lot.", "Yes, I do got a lot.",
                    "Yes, I am got a lot.", "Yes, I have got a lots."],
        "correct": "Yes, I've got a lot.",
        "explanation": "<p><strong>Yes, I've got a lot.</strong> is correct — the same system as the "
                       "question, shortened as in real speech.<br><br>"
                       "<em>(<strong>Yes, I've got a lot.</strong> toʻgʻri — savol bilan bir xil tizim, "
                       "haqiqiy nutqdagidek qisqartirilgan.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["My sister has got a laptop, but she doesn't have a printer.",
                    "My sister have got a laptop, but she hasn't a printer's.",
                    "My sister has got a laptop, but she doesn't has a printer.",
                    "My sister does have got a laptop, but she not have a printer."],
        "correct": "My sister has got a laptop, but she doesn't have a printer.",
        "explanation": "<p><strong>My sister has got a laptop, but she doesn't have a printer.</strong> "
                       "is correct — each half stays inside its own system: <em>has got</em> "
                       "and <em>doesn't have</em>.<br><br>"
                       "<em>(<strong>My sister has got a laptop, but she doesn't have a printer.</strong> "
                       "toʻgʻri — har bir yarmi oʻz tizimida qoladi: <em>has got</em> va "
                       "<em>doesn't have</em>.)</em></p>",
    },
]


# =====================================================================
# PE-15 — Adjectives: Meaning, Position and Order
# =====================================================================

Q_PE15 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>This is a ___ question.</strong></p>",
        "choices": ["difficult", "difficulty", "difficultly", "difficults"],
        "correct": "difficult",
        "explanation": "<p><strong>difficult</strong> is correct — the adjective form, right in front of "
                       "the noun.<br><br>"
                       "<em>(<strong>difficult</strong> toʻgʻri — sifat shakli, otdan oldin "
                       "turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I have two ___ brothers.</strong></p>",
        "choices": ["tall", "talls", "talles", "tallies"],
        "correct": "tall",
        "explanation": "<p><strong>tall</strong> is correct. English adjectives never take <em>-s</em>, "
                       "even before a plural noun.<br><br>"
                       "<em>(<strong>tall</strong> toʻgʻri. Ingliz tilida sifatlar hech qachon "
                       "<em>-s</em> olmaydi, hatto koʻplikdagi otdan oldin ham.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word order.</p>",
        "choices": ["a red car", "a car red", "red a car", "car a red"],
        "correct": "a red car",
        "explanation": "<p><strong>a red car</strong> is correct. English puts the adjective in front of "
                       "the noun — never after it, the way many languages allow.<br><br>"
                       "<em>(<strong>a red car</strong> toʻgʻri. Ingliz tilida sifat otdan oldin "
                       "keladi — koʻp tillarda mumkin boʻlgan “ot + sifat” tartibi bu yerda "
                       "ishlamaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>This question ___ difficult.</strong></p>",
        "choices": ["is", "does", "has", "are"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct. The second home of an adjective is after a "
                       "linking verb: <em>be, seem, look, feel, sound, taste</em>.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri. Sifatning ikkinchi joyi — bogʻlovchi feʼldan "
                       "keyin: <em>be, seem, look, feel, sound, taste</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Your idea ___ very interesting.</strong></p>",
        "choices": ["sounds", "sounds like interesting", "is sound", "sound"],
        "correct": "sounds",
        "explanation": "<p><strong>sounds</strong> is correct — a linking verb takes the adjective "
                       "directly, with no <em>like</em>.<br><br>"
                       "<em>(<strong>sounds</strong> toʻgʻri — bogʻlovchi feʼl sifatni toʻgʻridan "
                       "toʻgʻri oladi, <em>like</em> qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct order.</p>",
        "choices": ["a beautiful old carpet", "an old beautiful carpet",
                    "a carpet beautiful old", "an old carpet beautiful"],
        "correct": "a beautiful old carpet",
        "explanation": "<p><strong>a beautiful old carpet</strong> is correct. Opinion comes before "
                       "fact: <em>opinion → size → age → shape → colour → origin → "
                       "material</em>.<br><br>"
                       "<em>(<strong>a beautiful old carpet</strong> toʻgʻri. Fikr faktdan oldin "
                       "keladi: <em>opinion → size → age → shape → colour → origin → "
                       "material</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct order.</p>",
        "choices": ["a big round table", "a round big table",
                    "a table big round", "big a round table"],
        "correct": "a big round table",
        "explanation": "<p><strong>a big round table</strong> is correct — size before shape.<br><br>"
                       "<em>(<strong>a big round table</strong> toʻgʻri — oʻlcham shakldan oldin "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct order.</p>",
        "choices": ["a new black leather jacket", "a leather black new jacket",
                    "a black new leather jacket", "a leather new black jacket"],
        "correct": "a new black leather jacket",
        "explanation": "<p><strong>a new black leather jacket</strong> is correct — age → colour → "
                       "material. Material always sits closest to the noun.<br><br>"
                       "<em>(<strong>a new black leather jacket</strong> toʻgʻri — yosh → rang → "
                       "material. Material doim otga eng yaqin turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct order.</p>",
        "choices": ["a small Uzbek village", "an Uzbek small village",
                    "a village small Uzbek", "small an Uzbek village"],
        "correct": "a small Uzbek village",
        "explanation": "<p><strong>a small Uzbek village</strong> is correct — size before origin."
                       "<br><br><em>(<strong>a small Uzbek village</strong> toʻgʻri — oʻlcham kelib "
                       "chiqishdan oldin keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The lesson was ___ , so I nearly fell asleep.</strong></p>",
        "choices": ["boring", "bored", "bore", "boredom"],
        "correct": "boring",
        "explanation": "<p><strong>boring</strong> is correct. <em>-ing</em> describes the thing that "
                       "causes the feeling; <em>-ed</em> describes the person who feels it.<br><br>"
                       "<em>(<strong>boring</strong> toʻgʻri. <em>-ing</em> hissiyotni keltirib "
                       "chiqaradigan narsani, <em>-ed</em> esa uni his qilayotgan odamni "
                       "taʼriflaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I was very ___ during that lesson.</strong></p>",
        "choices": ["bored", "boring", "bore", "boredly"],
        "correct": "bored",
        "explanation": "<p><strong>bored</strong> is correct — I am the person feeling it. Saying "
                       "<em>I am boring</em> means other people find <em>you</em> dull!<br><br>"
                       "<em>(<strong>bored</strong> toʻgʻri — his qilayotgan odam menman. <em>I am "
                       "boring</em> desangiz, “men zerikarli odamman” degan maʼno chiqadi!)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The film was really ___ . I want to see it again.</strong></p>",
        "choices": ["exciting", "excited", "excite", "excitingly"],
        "correct": "exciting",
        "explanation": "<p><strong>exciting</strong> is correct — the film causes the feeling.<br><br>"
                       "<em>(<strong>exciting</strong> toʻgʻri — hissiyotni film keltirib "
                       "chiqaradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The children were ___ about the trip to the mountains.</strong></p>",
        "choices": ["excited", "exciting", "excite", "excitement"],
        "correct": "excited",
        "explanation": "<p><strong>excited</strong> is correct — the children feel it.<br><br>"
                       "<em>(<strong>excited</strong> toʻgʻri — buni bolalar his qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Where does the adjective go in “The soup tastes ___”?</strong></p>",
        "choices": ["delicious — after the linking verb",
                    "deliciously — after the linking verb",
                    "delicious — before the noun only",
                    "the soup delicious tastes"],
        "correct": "delicious — after the linking verb",
        "explanation": "<p><strong>delicious — after the linking verb</strong> is correct. "
                       "<em>Taste</em> is a linking verb, so it takes an adjective, not an adverb."
                       "<br><br><em>(<strong>delicious — after the linking verb</strong> toʻgʻri. "
                       "<em>Taste</em> — bogʻlovchi feʼl, shuning uchun ravish emas, sifat "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct order.</p>",
        "choices": ["two nice young Uzbek girls", "two Uzbek young nice girls",
                    "two young nice Uzbek girls", "two Uzbek nice young girls"],
        "correct": "two nice young Uzbek girls",
        "explanation": "<p><strong>two nice young Uzbek girls</strong> is correct — opinion "
                       "(<em>nice</em>) → age (<em>young</em>) → origin (<em>Uzbek</em>).<br><br>"
                       "<em>(<strong>two nice young Uzbek girls</strong> toʻgʻri — fikr "
                       "(<em>nice</em>) → yosh (<em>young</em>) → kelib chiqish "
                       "(<em>Uzbek</em>).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>She has ___ hair.</strong></p>",
        "choices": ["long black", "black long", "long blacks", "blacks long"],
        "correct": "long black",
        "explanation": "<p><strong>long black</strong> is correct — size/length before colour, and no "
                       "<em>-s</em> on adjectives.<br><br>"
                       "<em>(<strong>long black</strong> toʻgʻri — oʻlcham rangdan oldin keladi, "
                       "sifatlarga esa <em>-s</em> qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I have two talls brothers.", "I have two tall brothers.",
                    "My brothers are tall.", "He is a tall boy."],
        "correct": "I have two talls brothers.",
        "explanation": "<p><strong>I have two talls brothers.</strong> is the mistake — adjectives never "
                       "take a plural <em>-s</em> in English.<br><br>"
                       "<em>(<strong>I have two talls brothers.</strong> xato — ingliz tilida sifatlar "
                       "koʻplik <em>-s</em> ini olmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["We stayed in a beautiful little hotel.",
                    "We stayed in a little beautiful hotel.",
                    "We stayed in a hotel beautiful little.",
                    "We stayed in a beautiful hotel little."],
        "correct": "We stayed in a beautiful little hotel.",
        "explanation": "<p><strong>We stayed in a beautiful little hotel.</strong> is correct — opinion "
                       "before size.<br><br>"
                       "<em>(<strong>We stayed in a beautiful little hotel.</strong> toʻgʻri — fikr "
                       "oʻlchamdan oldin keladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>A:</strong> What was the concert like?</p>"
                "<p><strong>B:</strong> ___</p>",
        "choices": ["It was amazing! We were all really surprised.",
                    "It was amazed! We were all really surprising.",
                    "It was amazing! We were all really surprising.",
                    "It was amazed! We were all really surprised."],
        "correct": "It was amazing! We were all really surprised.",
        "explanation": "<p><strong>It was amazing! We were all really surprised.</strong> is correct — "
                       "the concert causes the feeling (<em>-ing</em>), the people feel it "
                       "(<em>-ed</em>).<br><br>"
                       "<em>(<strong>It was amazing! We were all really surprised.</strong> toʻgʻri — "
                       "hissiyotni konsert keltirib chiqaradi (<em>-ing</em>), odamlar esa uni his "
                       "qiladi (<em>-ed</em>).)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["My grandfather has an old wooden chair, and it is very comfortable.",
                    "My grandfather has a wooden old chair, and it is very comfortables.",
                    "My grandfather has an old chair wooden, and it is very comfortable.",
                    "My grandfather has olds wooden chair, and it very comfortable."],
        "correct": "My grandfather has an old wooden chair, and it is very comfortable.",
        "explanation": "<p><strong>My grandfather has an old wooden chair, and it is very "
                       "comfortable.</strong> is correct — age before material, adjectives in front of "
                       "the noun, no <em>-s</em>, and the linking verb <em>is</em> present.<br><br>"
                       "<em>(<strong>My grandfather has an old wooden chair, and it is very "
                       "comfortable.</strong> toʻgʻri — yosh materialdan oldin, sifatlar otdan oldin, "
                       "<em>-s</em> yoʻq, <em>is</em> bogʻlovchi feʼli esa oʻz oʻrnida.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-11 Practice: Adverbs of Frequency: always, usually, never",
        "tutorial":    "PE-11:",
        "description": "PE-11 darsiga 20 savol: chastota shkalasi, ravishning oʻrni (feʼldan oldin, "
                       "am/is/are dan keyin), ikki karra inkor xatosi, How often …? "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE11,
    },
    {
        "title":       "PE-12 Practice: Present Continuous: Happening Right Now",
        "tutorial":    "PE-12:",
        "description": "PE-12 darsiga 20 savol: am/is/are + -ing, imlo qoidalari (make → making, "
                       "sit → sitting), inkor, savol va qisqa javoblar. Javoblar ingliz va oʻzbek "
                       "tilida izohlangan.",
        "questions":   Q_PE12,
    },
    {
        "title":       "PE-13 Practice: Present Simple vs Present Continuous",
        "tutorial":    "PE-13:",
        "description": "PE-13 darsiga 20 savol: doimiy va hozirgi harakat oʻrtasidagi tanlov, "
                       "signal soʻzlar, -ing olmaydigan holat feʼllari. Javoblar ingliz va oʻzbek "
                       "tilida izohlangan.",
        "questions":   Q_PE13,
    },
    {
        "title":       "PE-14 Practice: have / have got: Talking About Possession",
        "tutorial":    "PE-14:",
        "description": "PE-14 darsiga 20 savol: have va have got, ularning inkor va savol shakllari, "
                       "have breakfast turidagi iboralar, he's = has yoki is. Javoblar ingliz va "
                       "oʻzbek tilida izohlangan.",
        "questions":   Q_PE14,
    },
    {
        "title":       "PE-15 Practice: Adjectives: Meaning, Position and Order",
        "tutorial":    "PE-15:",
        "description": "PE-15 darsiga 20 savol: sifatning oʻrni, -s olmasligi, tabiiy tartib "
                       "(opinion → size → age → colour → origin → material) va bored/boring farqi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE15,
    },
]
