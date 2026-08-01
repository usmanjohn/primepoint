# -*- coding: utf-8 -*-
"""Prime English practices — PE-96 … PE-100 (Block H: grammar at work — the final batch).

PE-100 is the capstone: one question from every major area of the whole course.
Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_96_100.py --master=prime --expect-questions=20
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
# PE-96 — Describing People, Places and Things
# =====================================================================
Q_PE96 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ long dark hair.</strong></p>",
        "choices": ["is", "has got", "is got", "have got"],
        "correct": "has got",
        "explanation": "<p><strong>has got</strong> is correct. The rule is mechanical: <em>be</em> takes "
                       "an adjective, <em>have got</em> takes a noun — and <em>hair</em> is a "
                       "noun.<br><br>"
                       "<em>(Qoida oddiy: <em>be</em> sifat bilan, <em>have got</em> ot bilan keladi. "
                       "<em>hair</em> — ot.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sherbek ___ quite tall.</strong></p>",
        "choices": ["has got", "have got", "has", "is"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — <em>tall</em> is an adjective, so it takes "
                       "<em>be</em>. In Uzbek both ideas use one structure, which is why they get "
                       "mixed up.<br><br>"
                       "<em>(<em>tall</em> — sifat, shuning uchun <em>be</em> bilan keladi. Oʻzbekchada "
                       "ikkala fikr bitta qurilma bilan aytilgani uchun ular aralashib "
                       "ketadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question word.</p>"
                "<p><strong>___ does Iroda look like? — She's tall with dark hair.</strong></p>",
        "choices": ["What", "How", "Which", "Who"],
        "correct": "What",
        "explanation": "<p><strong>What</strong> is correct. <em>What does she look like?</em> asks about "
                       "appearance — the answer describes her face and body.<br><br>"
                       "<em>(<em>What does she look like?</em> tashqi koʻrinish haqida soʻraydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is Davron ___? — He's very generous and patient.</strong></p>",
        "choices": ["look like", "liking", "like", "looks like"],
        "correct": "like",
        "explanation": "<p><strong>like</strong> is correct. <em>What is he like?</em> asks about "
                       "character. Compare the trio: <em>look like</em> = appearance, <em>be like</em> = "
                       "personality, <em>like</em> = what he enjoys.<br><br>"
                       "<em>(Uchlikni solishtiring: <em>look like</em> — tashqi koʻrinish, <em>be "
                       "like</em> — xarakter, <em>like</em> — nima yoqishi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ a small river next to our house.</strong></p>",
        "choices": ["It is", "Have", "There is", "There has"],
        "correct": "There is",
        "explanation": "<p><strong>There is</strong> is correct — this is the structure for saying what "
                       "exists somewhere (PE-7).<br><br>"
                       "<em>(<em>There is / There are</em> — biror joyda nima borligini aytish "
                       "qurilmasi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ his father — they have exactly the same eyes.</strong></p>",
        "choices": ["looks like", "is like", "likes", "is looking like"],
        "correct": "looks like",
        "explanation": "<p><strong>looks like</strong> is correct — the sentence is about appearance. "
                       "Note there is no continuous form here: <em>look</em> in this meaning is stative "
                       "(PE-13).<br><br>"
                       "<em>(Gap tashqi koʻrinish haqida. Bu maʼnodagi <em>look</em> — holat feʼli, "
                       "shuning uchun davomli shakli yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ green eyes and a very friendly face.</strong></p>",
        "choices": ["is", "is got", "have got", "has got"],
        "correct": "has got",
        "explanation": "<p><strong>has got</strong> is correct — <em>eyes</em> and <em>face</em> are "
                       "nouns, and the subject is third person singular.<br><br>"
                       "<em>(<em>eyes</em> va <em>face</em> — otlar, ega esa uchinchi shaxs "
                       "birlikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ apricot trees everywhere in my village.</strong></p>",
        "choices": ["There is", "There are", "It is", "They is"],
        "correct": "There are",
        "explanation": "<p><strong>There are</strong> is correct — <em>trees</em> is plural, so the verb "
                       "is plural too.<br><br>"
                       "<em>(<em>trees</em> koʻplikda, shuning uchun feʼl ham koʻplikda "
                       "boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Rozimurod teacher's brother is ___ his twenties.</strong></p>",
        "choices": ["on", "at", "by", "in"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct — <em>in his twenties / in her thirties</em> is "
                       "the fixed way to give somebody's approximate age.<br><br>"
                       "<em>(<em>in his twenties</em> — yoshni taxminan aytishning qatʼiy "
                       "shakli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It's the sort of place ___ nothing ever hurries.</strong></p>",
        "choices": ["which", "where", "what", "when"],
        "correct": "where",
        "explanation": "<p><strong>where</strong> is correct — the relative word points at a place "
                       "(PE-58). <em>It's the sort of place where…</em> is a ready-made phrase that "
                       "lifts any description.<br><br>"
                       "<em>(Bogʻlovchi soʻz joyga ishora qilyapti. <em>It's the sort of place "
                       "where…</em> — har qanday tavsifni koʻtaradigan tayyor ibora.)</em></p>",
    },
    {
        "text": "<p>Choose the correct adjective order.</p>"
                "<p><strong>It's a ___ box that my grandfather made.</strong></p>",
        "choices": [
            "wooden old beautiful",
            "old beautiful wooden",
            "beautiful old wooden",
            "beautiful wooden old",
        ],
        "correct": "beautiful old wooden",
        "explanation": "<p><strong>beautiful old wooden</strong> is correct. The order from PE-15 is "
                       "opinion → size → age → colour → origin → material.<br><br>"
                       "<em>(Tartib: fikr → oʻlcham → yosh → rang → kelib chiqishi → material.)</em></p>",
    },
    {
        "text": "<p>Choose the correct adjective order.</p>"
                "<p><strong>Charos was wearing a ___ scarf.</strong> (silk · beautiful · Uzbek)</p>",
        "choices": [
            "beautiful Uzbek silk",
            "silk Uzbek beautiful",
            "Uzbek beautiful silk",
            "beautiful silk Uzbek",
        ],
        "correct": "beautiful Uzbek silk",
        "explanation": "<p><strong>beautiful Uzbek silk</strong> is correct — opinion, then origin, then "
                       "material. English speakers do not learn this order; they simply feel it, so it "
                       "is worth practising until you do too.<br><br>"
                       "<em>(Fikr, keyin kelib chiqishi, keyin material. Ingliz tilida soʻzlashuvchilar "
                       "bu tartibni yodlamaydi — his qiladi. Siz ham shunday his qilguningizcha mashq "
                       "qiling.)</em></p>",
    },
    {
        "text": "<p>Which question asks about somebody's <strong>character</strong>?</p>",
        "choices": [
            "What is he like?",
            "What does he look like?",
            "What does he like?",
            "What is he doing?",
        ],
        "correct": "What is he like?",
        "explanation": "<p><strong>What is he like?</strong> asks about personality. This trio is a "
                       "classic exam trap — one small word changes the whole question.<br><br>"
                       "<em>(Bu uchlik — klassik imtihon tuzogʻi: bitta kichik soʻz butun savol maʼnosini "
                       "oʻzgartiradi.)</em></p>",
    },
    {
        "text": "<p>Which question asks about somebody's <strong>appearance</strong>?</p>",
        "choices": [
            "What is she like?",
            "What does she like?",
            "What does she look like?",
            "What is she?",
        ],
        "correct": "What does she look like?",
        "explanation": "<p><strong>What does she look like?</strong> is correct. <em>What is she "
                       "like?</em> would ask about character, and <em>What does she like?</em> about her "
                       "preferences.<br><br>"
                       "<em>(<em>What is she like?</em> xarakter haqida, <em>What does she like?</em> esa "
                       "nima yoqishi haqida soʻragan boʻlardi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Marjona is long hair.",
            "Marjona has got long hair.",
            "Marjona is got long hair.",
            "Marjona have got long hair.",
        ],
        "correct": "Marjona has got long hair.",
        "explanation": "<p><strong>Marjona has got long hair.</strong> is correct. <em>She is long "
                       "hair</em> is the classic error — before you build the sentence, ask yourself: is "
                       "this word an adjective or a noun?<br><br>"
                       "<em>(<em>She is long hair</em> — klassik xato. Gapni tuzishdan oldin oʻzingizga "
                       "savol bering: bu soʻz sifatmi yoki otmi?)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "In my village is a river.",
            "In my village there has a river.",
            "My village is a river.",
            "There is a river in my village.",
        ],
        "correct": "There is a river in my village.",
        "explanation": "<p><strong>There is a river in my village.</strong> is correct. Uzbek can start "
                       "with the place and leave out the subject; English needs <em>There is</em> to hold "
                       "the sentence up.<br><br>"
                       "<em>(Oʻzbekchada joydan boshlab, egani tushirib qoldirish mumkin. Ingliz tilida "
                       "esa gapni ushlab turish uchun <em>There is</em> kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "Firdavs looks like his father.",
            "Firdavs is looking like his father.",
            "Firdavs is like his mother — calm and patient.",
            "Firdavs has got brown eyes.",
        ],
        "correct": "Firdavs is looking like his father.",
        "explanation": "<p><strong>Firdavs is looking like his father.</strong> is the mistake. "
                       "<em>Look</em> in the sense of \"resemble\" is a stative verb, so it has no "
                       "continuous form (PE-13).<br><br>"
                       "<em>(\"Oʻxshamoq\" maʼnosidagi <em>look</em> — holat feʼli, shuning uchun davomli "
                       "shakli yoʻq.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "It's a box wooden old beautiful.",
            "It's a wooden beautiful old box.",
            "It's an old beautiful wooden box.",
            "It's a beautiful old wooden box.",
        ],
        "correct": "It's a beautiful old wooden box.",
        "explanation": "<p><strong>It's a beautiful old wooden box.</strong> is correct. In Uzbek the "
                       "order is freer, which is why adjective order has to be practised rather than "
                       "reasoned out.<br><br>"
                       "<em>(Oʻzbekchada tartib erkinroq — shuning uchun sifatlar tartibini mulohaza "
                       "bilan emas, mashq bilan oʻzlashtirish kerak.)</em></p>",
    },
    {
        "text": "<p>Which description would score best in an exam?</p>",
        "choices": [
            "He's the kind of person who always notices when you're upset. Last week, for example, "
            "he stayed late to help me with my homework.",
            "He is kind. He is helpful. He is good.",
            "He is kind and helpful and nice and good.",
            "He kind and helpful person.",
        ],
        "correct": "He's the kind of person who always notices when you're upset. Last week, for example, "
                   "he stayed late to help me with my homework.",
        "explanation": "<p>The first one wins. A list of adjectives is dull; a reason or an example "
                       "brings a description alive. That is the golden rule of describing: after every "
                       "fact, add <em>why?</em> or <em>for example?</em><br><br>"
                       "<em>(Sifatlar roʻyxati zerikarli; sabab yoki misol tavsifni jonlantiradi. "
                       "Tavsiflashning oltin qoidasi: har bir faktdan keyin \"nega?\" yoki \"masalan?\" "
                       "qoʻshing.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Tell us about your grandmother, Shaxzoda.</p>"
                "<p><strong>Shaxzoda:</strong> ___</p>",
        "choices": [
            "My grandmother is small and she is very kind eyes.",
            "My grandmother small and has very kind eyes.",
            "My grandmother is small and she has got very kind eyes. She's the kind of person who "
            "never complains.",
            "My grandmother is small and she has got very kind eyes. She's the kind of person which "
            "never complains.",
        ],
        "correct": "My grandmother is small and she has got very kind eyes. She's the kind of person who "
                   "never complains.",
        "explanation": "<p>The third reply is correct and complete: <em>is</em> + adjective, <em>has "
                       "got</em> + noun, then a sentence of character with <em>who</em> for a person. "
                       "That is a whole description in two lines.<br><br>"
                       "<em>(<em>is</em> + sifat, <em>has got</em> + ot, keyin odam uchun <em>who</em> "
                       "bilan xarakter haqida jumla — ikki qatorda toʻliq tavsif.)</em></p>",
    },
]


# =====================================================================
# PE-97 — Describing Charts, Trends and Numbers
# =====================================================================
Q_PE97 = [
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>In Sherbek's project, sales ___ from 20 to 50 between January and June.</strong></p>",
        "choices": ["fell", "dropped", "rose", "declined"],
        "correct": "rose",
        "explanation": "<p><strong>rose</strong> is correct — the numbers went up. The family is "
                       "<em>increase, rise, grow, go up, climb</em>.<br><br>"
                       "<em>(Raqamlar oshgan. Oila: <em>increase, rise, grow, go up, climb</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>The number of tourists ___ at four million in 2019.</strong></p>",
        "choices": ["peaked", "rose", "grew", "climbed"],
        "correct": "peaked",
        "explanation": "<p><strong>peaked</strong> is correct — it names the highest point of the whole "
                       "graph. And note the fixed preposition: <em>peak at a number</em>.<br><br>"
                       "<em>(<em>peak</em> — butun grafikning eng yuqori nuqtasi. Predlog qatʼiy: "
                       "<em>peak at</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Prices ___ sharply after the summer.</strong> (they went down)</p>",
        "choices": ["rose", "climbed", "grew", "fell"],
        "correct": "fell",
        "explanation": "<p><strong>fell</strong> is correct. The downward family is <em>decrease, fall, "
                       "drop, decline, go down</em>.<br><br>"
                       "<em>(Pastga tushish oilasi: <em>decrease, fall, drop, decline, go "
                       "down</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Between 2015 and 2020 the figure ___ stable at around 30%.</strong></p>",
        "choices": ["kept", "remained", "held", "stood"],
        "correct": "remained",
        "explanation": "<p><strong>remained</strong> is correct — <em>remain stable</em>, <em>stay the "
                       "same</em> and <em>level off</em> all describe a flat line.<br><br>"
                       "<em>(<em>remain stable</em>, <em>stay the same</em>, <em>level off</em> — "
                       "hammasi tekis chiziqni tasvirlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>Iroda's line went up and down all year — the graph shows a ___.</strong></p>",
        "choices": ["fluctuation", "peak", "low", "decline"],
        "correct": "fluctuation",
        "explanation": "<p><strong>fluctuation</strong> is correct — the verb is <em>fluctuate</em>, and "
                       "it is the word for a line that keeps changing direction.<br><br>"
                       "<em>(Feʼli — <em>fluctuate</em>. Bu soʻz yoʻnalishini doim oʻzgartirib turadigan "
                       "chiziq uchun ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct prepositions.</p>"
                "<p><strong>Madina wrote: sales rose ___ 20 ___ 50.</strong></p>",
        "choices": ["by / to", "from / until", "of / to", "from / to"],
        "correct": "from / to",
        "explanation": "<p><strong>from / to</strong> is correct — these two mark the end points. "
                       "<em>Until</em> is for time, never for numbers.<br><br>"
                       "<em>(Bu ikkalasi boshlangʻich va oxirgi nuqtani belgilaydi. <em>Until</em> vaqt "
                       "uchun, raqamlar uchun emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Production increased ___ 20% last year.</strong></p>",
        "choices": ["with", "by", "of", "to"],
        "correct": "by",
        "explanation": "<p><strong>by</strong> is correct — <em>by</em> gives the <strong>size</strong> "
                       "of the change. <em>Increased with 20%</em> is a direct translation and is "
                       "wrong.<br><br>"
                       "<em>(<em>by</em> oʻzgarishning <strong>hajmini</strong> bildiradi. "
                       "<em>increased with</em> — soʻzma-soʻz tarjima va notoʻgʻri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>On Behruz's chart the figure went from 100 to 150 — an increase ___ 50%.</strong></p>",
        "choices": ["by", "with", "of", "in"],
        "correct": "of",
        "explanation": "<p><strong>of</strong> is correct. The rule in one line: <em>from … to</em> = end "
                       "points · <em>by</em> = size of change · <em>of</em> = after a noun.<br><br>"
                       "<em>(Qoida bir qatorda: <em>from … to</em> — chegaralar, <em>by</em> — "
                       "oʻzgarish hajmi, <em>of</em> — otdan keyin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct adverb.</p>"
                "<p><strong>Prices rose ___ — they doubled in a single month.</strong></p>",
        "choices": ["slightly", "sharply", "gradually", "marginally"],
        "correct": "sharply",
        "explanation": "<p><strong>sharply</strong> is correct — for a big, fast change. Its family: "
                       "<em>dramatically, significantly, considerably, steeply</em>.<br><br>"
                       "<em>(Katta va tez oʻzgarish uchun. Oilasi: <em>dramatically, significantly, "
                       "considerably, steeply</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct adverb.</p>"
                "<p><strong>Charos noted that the figure fell ___ , by just one per cent.</strong></p>",
        "choices": ["dramatically", "sharply", "slightly", "steeply"],
        "correct": "slightly",
        "explanation": "<p><strong>slightly</strong> is correct — for a small change, alongside "
                       "<em>marginally</em>. For a slow one use <em>gradually</em> or "
                       "<em>steadily</em>.<br><br>"
                       "<em>(Kichik oʻzgarish uchun — <em>marginally</em> bilan bir qatorda. Sekin "
                       "oʻzgarish uchun <em>gradually</em> yoki <em>steadily</em>.)</em></p>",
    },
    {
        "text": "<p>Rewrite with a noun: <strong>Prices rose sharply.</strong></p>"
                "<p><strong>There was a ___ in prices.</strong></p>",
        "choices": ["sharp rise", "sharply rise", "sharp rose", "sharply increase"],
        "correct": "sharp rise",
        "explanation": "<p><strong>sharp rise</strong> is correct. Adverb becomes adjective, verb becomes "
                       "noun. Alternating between the two versions keeps your writing from "
                       "repeating itself.<br><br>"
                       "<em>(Ravish sifatga, feʼl otga aylanadi. Inshoda ikki variantni navbatlashtirsangiz, "
                       "matn takrorlanmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>The ___ of students at the school increased last year.</strong></p>",
        "choices": ["amount", "quantity", "much", "number"],
        "correct": "number",
        "explanation": "<p><strong>number</strong> is correct — <em>students</em> is countable. Use "
                       "<em>the amount of</em> only with uncountable nouns: <em>the amount of water</em> "
                       "(PE-2).<br><br>"
                       "<em>(<em>students</em> — sanaladigan ot. <em>the amount of</em> ni faqat "
                       "sanalmaydigan otlar bilan ishlating.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>The government ___ taxes, so prices ___ .</strong></p>",
        "choices": ["rose / raised", "raised / raised", "rose / rose", "raised / rose"],
        "correct": "raised / rose",
        "explanation": "<p><strong>raised / rose</strong> is correct. <em>Raise</em> needs an object — "
                       "somebody lifts something; <em>rise</em> happens by itself.<br><br>"
                       "<em>(<em>Raise</em> ga toʻldiruvchi kerak — kimdir biror narsani koʻtaradi; "
                       "<em>rise</em> esa oʻz-oʻzidan sodir boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>The ___ of water used by the factory fell in 2020.</strong></p>",
        "choices": ["number", "amount", "figure", "total"],
        "correct": "amount",
        "explanation": "<p><strong>amount</strong> is correct — <em>water</em> is uncountable. This pair "
                       "comes up constantly in chart writing, because almost every sentence starts with "
                       "\"the number of…\" or \"the amount of…\"<br><br>"
                       "<em>(<em>water</em> — sanalmaydigan ot. Bu juftlik grafik tavsifida doim kerak "
                       "boʻladi, chunki deyarli har bir jumla shu ikkisidan biri bilan "
                       "boshlanadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "The number of students was increased.",
            "There was a sharply increase.",
            "The number of students increased.",
            "The number of students were increased.",
        ],
        "correct": "The number of students increased.",
        "explanation": "<p><strong>The number of students increased.</strong> is correct. "
                       "<em>Increase</em> is not passive here — the number went up by itself. And note "
                       "<em>the number … increased</em>, singular (PE-74).<br><br>"
                       "<em>(Bu yerda <em>increase</em> majhul emas — son oʻz-oʻzidan oshgan. "
                       "<em>the number</em> — birlik.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Prices rose sharply.",
            "Prices raised sharply.",
            "Prices were risen sharply.",
            "Prices rose sharp.",
        ],
        "correct": "Prices rose sharply.",
        "explanation": "<p><strong>Prices rose sharply.</strong> is correct: <em>rise</em> takes no "
                       "object and no passive, and the word describing the verb must be an adverb "
                       "(<em>sharply</em>, not <em>sharp</em>).<br><br>"
                       "<em>(<em>rise</em> toʻldiruvchi ham, majhul shakl ham olmaydi, feʼlni "
                       "tasvirlaydigan soʻz esa ravish boʻlishi kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "Sales increased by 20%.",
            "It rose from 20 to 50.",
            "The amount of tourists grew.",
            "There was a slight fall in sales.",
        ],
        "correct": "The amount of tourists grew.",
        "explanation": "<p><strong>The amount of tourists grew.</strong> is the mistake — tourists are "
                       "countable, so it must be <em>the number of tourists</em>.<br><br>"
                       "<em>(Turistlar sanaladi, shuning uchun <em>the number of tourists</em> boʻlishi "
                       "kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "It peaked at four million.",
            "It peaked on four million.",
            "It peaked in four million.",
            "It peaked to four million.",
        ],
        "correct": "It peaked at four million.",
        "explanation": "<p><strong>It peaked at four million.</strong> is correct — <em>peak at</em> is "
                       "fixed, and examiners notice it.<br><br>"
                       "<em>(<em>peak at</em> — qatʼiy birikma, imtihonchilar buni sezadi.)</em></p>",
    },
    {
        "text": "<p>Javohir is writing about a population chart. Which sentence is a good "
                "<strong>overview</strong>?</p>",
        "choices": [
            "In my opinion, this is a very good trend for the country.",
            "Tashkent had 2.5 million and Samarkand had 0.5 million.",
            "I think the population will grow even more next year.",
            "Overall, the population increased in all three cities, with the sharpest growth in Tashkent.",
        ],
        "correct": "Overall, the population increased in all three cities, with the sharpest growth in Tashkent.",
        "explanation": "<p>The last one is the overview: the biggest pattern, in one sentence, with no "
                       "detailed numbers yet. The first and third give opinions, and a chart description "
                       "reports rather than argues.<br><br>"
                       "<em>(Umumiy manzara — eng katta tendensiya, bitta jumlada, hali raqamlarsiz. "
                       "Birinchi va uchinchisi fikr bildiryapti, grafik tavsifi esa bahslashmaydi, "
                       "faktlarni bayon qiladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> What must you never put in a chart "
                "description, Samandar?</p>"
                "<p><strong>Samandar:</strong> ___</p>",
        "choices": [
            "The overview.",
            "Your own opinion.",
            "The numbers.",
            "The time period.",
        ],
        "correct": "Your own opinion.",
        "explanation": "<p><strong>Your own opinion.</strong> is correct. \"I think this is a good "
                       "trend\" earns no marks — the task is to report the facts. The structure is: what "
                       "the chart shows → the overview → the details.<br><br>"
                       "<em>(\"Menimcha, bu yaxshi tendensiya\" degan jumla ball qoʻshmaydi — vazifa "
                       "faktlarni bayon qilish. Tuzilma: nima koʻrsatilgan → umumiy manzara → "
                       "tafsilot.)</em></p>",
    },
]


# =====================================================================
# PE-98 — Making Excuses, Apologising and Explaining
# =====================================================================
Q_PE98 = [
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>Sorry ___ being late, Rozimurod teacher.</strong></p>",
        "choices": ["to", "for", "about", "of"],
        "correct": "for",
        "explanation": "<p><strong>for</strong> is correct. <em>Sorry for + -ing</em> is used for "
                       "something <strong>you did</strong>.<br><br>"
                       "<em>(<em>Sorry for + -ing</em> — <strong>siz qilgan</strong> ish uchun "
                       "ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>Sorry ___ the noise — my little brother is playing.</strong></p>",
        "choices": ["for", "to", "of", "about"],
        "correct": "about",
        "explanation": "<p><strong>about</strong> is correct. <em>Sorry about + noun</em> is used for a "
                       "thing or a situation.<br><br>"
                       "<em>(<em>Sorry about + ot</em> — narsa yoki vaziyat uchun.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>Sorry ___ hear that. I hope she gets better soon.</strong></p>",
        "choices": ["to", "for", "about", "with"],
        "correct": "to",
        "explanation": "<p><strong>to</strong> is correct. <em>Sorry to + verb</em> is used when you are "
                       "<strong>reacting to news</strong> or interrupting — you are not apologising for "
                       "anything you did.<br><br>"
                       "<em>(<em>Sorry to + feʼl</em> — <strong>xabarga javob</strong> berayotganda yoki "
                       "gapini boʻlayotganda. Bu yerda siz oʻz ishingiz uchun uzr "
                       "soʻramayapsiz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>Sorry ___ forgetting your book, Iroda.</strong></p>",
        "choices": ["to", "about", "for", "of"],
        "correct": "for",
        "explanation": "<p><strong>for</strong> is correct — a verb follows, so it takes <em>for + "
                       "-ing</em>. Choose by looking at the next word: verb → <em>for</em>, noun → "
                       "<em>about</em>, reaction → <em>to</em>.<br><br>"
                       "<em>(Keyin feʼl kelyapti, shuning uchun <em>for + -ing</em>. Keyingi soʻzga "
                       "qarab tanlang: feʼl → <em>for</em>, ot → <em>about</em>, javob → "
                       "<em>to</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>Marjona:</strong> Sorry ___ bother you, but could I ask a question?</p>",
        "choices": ["for", "about", "to", "of"],
        "correct": "to",
        "explanation": "<p><strong>to</strong> is correct — <em>Sorry to bother you</em> and <em>Sorry to "
                       "interrupt</em> are fixed polite openers.<br><br>"
                       "<em>(<em>Sorry to bother you</em> va <em>Sorry to interrupt</em> — muloyim "
                       "murojaatning tayyor shakllari.)</em></p>",
    },
    {
        "text": "<p>Choose the formal option.</p>"
                "<p><strong>Shaxzoda:</strong> I ___ for the delay in sending the report.</p>",
        "choices": ["apologise", "sorry", "excuse", "regret to"],
        "correct": "apologise",
        "explanation": "<p><strong>apologise</strong> is correct — the written, formal end of the scale. "
                       "And note it takes <em>for</em>, never <em>about</em>.<br><br>"
                       "<em>(Yozma, rasmiy shakl. Eʼtibor bering — u <em>for</em> oladi, "
                       "<em>about</em> emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Please accept my ___ for any inconvenience caused.</strong></p>",
        "choices": ["apologise", "sorry", "excuse", "apologies"],
        "correct": "apologies",
        "explanation": "<p><strong>apologies</strong> is correct — the noun, and in the plural. This is "
                       "the most formal apology in the lesson; learn it as one block.<br><br>"
                       "<em>(Bu — ot shakli, koʻplikda. Darsdagi eng rasmiy uzr; uni butunligicha "
                       "yodlang.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs:</strong> I couldn't finish the homework ___ the electricity went off.</p>",
        "choices": ["because of", "because", "due to", "owing to"],
        "correct": "because",
        "explanation": "<p><strong>because</strong> is correct — a full clause (subject + verb) follows. "
                       "<em>Because of</em>, <em>due to</em> and <em>owing to</em> all need a noun "
                       "(PE-88).<br><br>"
                       "<em>(Keyin toʻliq gap (ega + kesim) kelyapti. <em>Because of</em>, <em>due "
                       "to</em>, <em>owing to</em> ga esa ot kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The lesson was cancelled ___ the weather.</strong></p>",
        "choices": ["because", "although", "so", "due to"],
        "correct": "due to",
        "explanation": "<p><strong>due to</strong> is correct — only a noun follows. <em>Due to</em> and "
                       "<em>owing to</em> sound better than <em>because of</em> in formal "
                       "writing.<br><br>"
                       "<em>(Keyin faqat ot kelyapti. Rasmiy yozuvda <em>due to</em> va <em>owing to</em> "
                       "<em>because of</em> dan chiroyliroq eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ told you earlier. I'm really sorry.</strong></p>",
        "choices": ["should tell", "should have told", "must have told", "would tell"],
        "correct": "should have told",
        "explanation": "<p><strong>should have told</strong> is correct — <em>should have + V3</em> is "
                       "how English admits a mistake about the past (PE-48).<br><br>"
                       "<em>(<em>should have + V3</em> — ingliz tilida oʻtgan ish uchun aybni tan olish "
                       "shakli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar:</strong> It ___ happen again, I promise.</p>",
        "choices": ["doesn't", "isn't", "won't", "didn't"],
        "correct": "won't",
        "explanation": "<p><strong>won't</strong> is correct — the promise is about the future. "
                       "<em>It won't happen again</em> is the standard closing of an apology.<br><br>"
                       "<em>(Vaʼda kelasi zamon haqida. <em>It won't happen again</em> — uzrning "
                       "standart yakuni.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tense.</p>"
                "<p><strong>Sirojiddin:</strong> I'm sorry I'm late. I ___ for the bus for half an hour.</p>",
        "choices": ["was waiting", "wait", "have waited", "am waiting"],
        "correct": "was waiting",
        "explanation": "<p><strong>was waiting</strong> is correct. A believable excuse usually needs the "
                       "Past Continuous — what you were in the middle of — or the Past Perfect, for what "
                       "had already gone wrong.<br><br>"
                       "<em>(Ishonarli bahonaga odatda Past Continuous kerak — nima qilib turgan "
                       "edingiz; yoki Past Perfect — nima allaqachon buzilgan edi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Sorry for being late.",
            "Sorry for be late.",
            "Sorry to being late.",
            "Sorry of being late.",
        ],
        "correct": "Sorry for being late.",
        "explanation": "<p><strong>Sorry for being late.</strong> is correct. The three structures never "
                       "mix: it is <em>for + -ing</em>, not <em>for + base verb</em> and not <em>to + "
                       "-ing</em>.<br><br>"
                       "<em>(Uchta qurilma hech qachon aralashmaydi: <em>for + -ing</em>, "
                       "<em>for + asl feʼl</em> ham, <em>to + -ing</em> ham emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Sorry for hear about your problem.",
            "Sorry about hear your problem.",
            "Sorry to hear about your problem.",
            "Sorry of hearing about your problem.",
        ],
        "correct": "Sorry to hear about your problem.",
        "explanation": "<p><strong>Sorry to hear about your problem.</strong> is correct — you are "
                       "reacting to news, so it takes <em>to + verb</em>. You did not cause the problem, "
                       "so <em>for</em> would be wrong.<br><br>"
                       "<em>(Siz xabarga javob berayapsiz, shuning uchun <em>to + feʼl</em>. Muammoni "
                       "siz keltirib chiqarmagansiz, demak <em>for</em> notoʻgʻri boʻlardi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I apologise about the delay.",
            "I apologise for the delay.",
            "I apologise of the delay.",
            "I apologise to the delay.",
        ],
        "correct": "I apologise for the delay.",
        "explanation": "<p><strong>I apologise for the delay.</strong> is correct. Note the difference "
                       "from <em>sorry</em>: <em>sorry</em> can take <em>about</em>, but "
                       "<em>apologise</em> only takes <em>for</em>.<br><br>"
                       "<em>(<em>sorry</em> dan farqiga eʼtibor bering: <em>sorry</em> <em>about</em> "
                       "olishi mumkin, <em>apologise</em> esa faqat <em>for</em> oladi.)</em></p>",
    },
    {
        "text": "<p>What are the three parts of a good apology, in order?</p>",
        "choices": [
            "explain → apologise → offer to fix it",
            "apologise → offer to fix it → explain",
            "explain → offer to fix it → apologise",
            "apologise → explain briefly → offer to fix it",
        ],
        "correct": "apologise → explain briefly → offer to fix it",
        "explanation": "<p><strong>apologise → explain briefly → offer to fix it</strong> is correct. A "
                       "long explanation with no apology sounds like an excuse; an apology with no "
                       "explanation sounds careless.<br><br>"
                       "<em>(Uzrsiz uzun tushuntirish bahonaga oʻxshaydi; tushuntirishsiz uzr esa "
                       "eʼtiborsizlikdek eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "I'm sorry for the mistake I made.",
            "Excuse me for the mistake I did.",
            "Sorry about the mess.",
            "I'm sorry to interrupt you.",
        ],
        "correct": "Excuse me for the mistake I did.",
        "explanation": "<p><strong>Excuse me for the mistake I did.</strong> is the mistake — you "
                       "<em>make</em> a mistake, never <em>do</em> one (PE-90).<br><br>"
                       "<em>(Xato <em>make</em> qilinadi, <em>do</em> emas — bu PE-90 dagi juftlik "
                       "qoidasi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "It was because of the traffic was bad.",
            "It was because of the traffic was heavy.",
            "It was because the heavy traffic.",
            "It was because the traffic was bad.",
        ],
        "correct": "It was because the traffic was bad.",
        "explanation": "<p><strong>It was because the traffic was bad.</strong> is correct. You may also "
                       "say <em>because of the heavy traffic</em> — but never mix the two into "
                       "<em>because of … was …</em><br><br>"
                       "<em>(<em>because of the heavy traffic</em> deyish ham mumkin — lekin ikkalasini "
                       "aralashtirib yubormang.)</em></p>",
    },
    {
        "text": "<p>Javohir missed his friend's birthday party. Which is a complete apology?</p>",
        "choices": [
            "I'm so sorry for missing your party. My little sister was ill and I had to stay at home. "
            "Let me take you out at the weekend to make up for it.",
            "Sorry. I couldn't come.",
            "I didn't come because my sister was ill. That's all.",
            "My sister was ill. It was not my fault.",
        ],
        "correct": "I'm so sorry for missing your party. My little sister was ill and I had to stay at home. "
                   "Let me take you out at the weekend to make up for it.",
        "explanation": "<p>The first one has all three parts: it apologises, it explains briefly, and it "
                       "offers to fix things. The others are missing at least one — and the last is not "
                       "an apology at all.<br><br>"
                       "<em>(Birinchisida uchala qism ham bor: uzr, qisqa izoh va oʻrnini qoplash "
                       "taklifi. Qolganlarida kamida bittasi yetishmaydi, oxirgisi esa umuman uzr "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Elbek:</strong> I'm really sorry — I forgot to bring your book.</p>"
                "<p><strong>Madina:</strong> ___</p>",
        "choices": [
            "(Madina says nothing.)",
            "You should be sorry.",
            "That's all right, don't worry about it.",
            "Yes, you forgot it.",
        ],
        "correct": "That's all right, don't worry about it.",
        "explanation": "<p><strong>That's all right, don't worry about it.</strong> is correct. In "
                       "English you must accept an apology <em>out loud</em> — silence comes across as "
                       "cold. <em>No problem</em>, <em>Never mind</em> and <em>These things happen</em> "
                       "all work too.<br><br>"
                       "<em>(Ingliz tilida uzrni <strong>ovoz chiqarib</strong> qabul qilish kerak — jim "
                       "turish sovuqlikdek tuyuladi. <em>No problem</em>, <em>Never mind</em>, "
                       "<em>These things happen</em> ham mos keladi.)</em></p>",
    },
]


# =====================================================================
# PE-99 — Small Talk and Everyday Conversation Grammar
# =====================================================================
Q_PE99 = [
    {
        "text": "<p>Complete the exchange.</p>"
                "<p><strong>Charos:</strong> How are you?</p>"
                "<p><strong>Behruz:</strong> ___</p>",
        "choices": [
            "I am not very well because my head hurts and my back hurts and…",
            "I am fine and you are fine.",
            "Fine, thanks. And you?",
            "Yes, I am.",
        ],
        "correct": "Fine, thanks. And you?",
        "explanation": "<p><strong>Fine, thanks. And you?</strong> is correct. <em>How are you?</em> is "
                       "part of the greeting, not a real question about your health — reply short and "
                       "ask back.<br><br>"
                       "<em>(<em>How are you?</em> — salomlashishning bir qismi, sogʻliq haqidagi "
                       "haqiqiy savol emas. Qisqa javob bering va savolni qaytaring — oʻzbekchadagi "
                       "\"Yaxshi, rahmat. Oʻzingiz-chi?\" kabi.)</em></p>",
    },
    {
        "text": "<p>Complete the reply.</p>"
                "<p><strong>Jasur:</strong> I like plov.</p>"
                "<p><strong>Sherbek:</strong> ___</p>",
        "choices": ["So do I.", "So I do.", "So am I.", "Also I."],
        "correct": "So do I.",
        "explanation": "<p><strong>So do I.</strong> is correct. Use the same auxiliary as the speaker "
                       "(<em>like</em> → <em>do</em>) and invert it (PE-84) — <em>So I do</em> has the "
                       "word order the wrong way round.<br><br>"
                       "<em>(Gapiruvchi ishlatgan yordamchi feʼlni oling va soʻz tartibini almashtiring. "
                       "<em>So I do</em> da tartib teskari.)</em></p>",
    },
    {
        "text": "<p>Complete the reply.</p>"
                "<p><strong>Firdavs:</strong> I don't smoke.</p>"
                "<p><strong>Davron:</strong> ___</p>",
        "choices": ["Neither don't I.", "So do I.", "Neither I do.", "Neither do I."],
        "correct": "Neither do I.",
        "explanation": "<p><strong>Neither do I.</strong> is correct. <em>Neither</em> already carries "
                       "the negative, so <em>don't</em> would be a double negative (PE-11).<br><br>"
                       "<em>(<em>Neither</em> ning oʻzi inkorni koʻtaryapti, shuning uchun <em>don't</em> "
                       "qoʻsh inkor boʻlib qolardi.)</em></p>",
    },
    {
        "text": "<p>Complete the reply.</p>"
                "<p><strong>Shaxzoda:</strong> I'm really tired.</p>"
                "<p><strong>Marjona:</strong> ___</p>",
        "choices": ["So do I.", "So am I.", "Neither am I.", "So I am."],
        "correct": "So am I.",
        "explanation": "<p><strong>So am I.</strong> is correct — the speaker used <em>am</em>, so the "
                       "reply uses <em>am</em>. Match the auxiliary, every time.<br><br>"
                       "<em>(Gapiruvchi <em>am</em> ishlatdi, javob ham <em>am</em> bilan. Yordamchi "
                       "feʼl doim mos kelishi kerak.)</em></p>",
    },
    {
        "text": "<p>Complete the reply.</p>"
                "<p><strong>Abdulloh:</strong> I've never been abroad.</p>"
                "<p><strong>Iroda:</strong> ___</p>",
        "choices": ["Neither have I.", "Neither did I.", "So have I.", "Neither I have."],
        "correct": "Neither have I.",
        "explanation": "<p><strong>Neither have I.</strong> is correct — negative sentence, auxiliary "
                       "<em>have</em>, so the reply is <em>Neither have I</em>.<br><br>"
                       "<em>(Inkor gap, yordamchi feʼl <em>have</em> — demak javob <em>Neither have "
                       "I</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the echo question.</p>"
                "<p><strong>Samandar:</strong> I went to Samarkand last week.</p>"
                "<p><strong>Madina:</strong> Oh, ___?</p>",
        "choices": ["do you", "are you", "have you", "did you"],
        "correct": "did you",
        "explanation": "<p><strong>did you</strong> is correct. An echo question repeats the speaker's "
                       "own auxiliary — the sentence is past simple, so it takes <em>did</em>.<br><br>"
                       "<em>(Takroriy savol gapiruvchining yordamchi feʼlini takrorlaydi. Gap past "
                       "simple da, shuning uchun <em>did</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the echo question.</p>"
                "<p><strong>Ilgʻor:</strong> I'm learning Korean.</p>"
                "<p><strong>Afsona:</strong> ___? That's interesting!</p>",
        "choices": ["Do you", "Are you", "Did you", "Have you"],
        "correct": "Are you",
        "explanation": "<p><strong>Are you</strong> is correct — the speaker said <em>I'm</em>, so the "
                       "echo is <em>Are you?</em> These little questions mean \"really? tell me "
                       "more\".<br><br>"
                       "<em>(Gapiruvchi <em>I'm</em> dedi, demak javob <em>Are you?</em>. Bu kichik "
                       "savollar \"rostdanmi? davom et\" degan maʼnoni beradi.)</em></p>",
    },
    {
        "text": "<p>Complete the echo question.</p>"
                "<p><strong>Sirojiddin:</strong> I've never eaten sushi.</p>"
                "<p><strong>Charos:</strong> ___?</p>",
        "choices": ["Didn't you", "Don't you", "Haven't you", "Weren't you"],
        "correct": "Haven't you",
        "explanation": "<p><strong>Haven't you</strong> is correct — a negative sentence with "
                       "<em>have</em> echoes back as <em>Haven't you?</em><br><br>"
                       "<em>(<em>have</em> bilan tuzilgan inkor gap <em>Haven't you?</em> boʻlib "
                       "qaytadi.)</em></p>",
    },
    {
        "text": "<p>Complete the exchange.</p>"
                "<p><strong>Elbek:</strong> How's it going?</p>"
                "<p><strong>Javohir:</strong> ___</p>",
        "choices": [
            "It is going by bus.",
            "Not bad, thanks. You?",
            "Yes, it goes.",
            "I go to school every day.",
        ],
        "correct": "Not bad, thanks. You?",
        "explanation": "<p><strong>Not bad, thanks. You?</strong> is correct. <em>How's it going?</em> is "
                       "another greeting, not a question about movement — the expected reply is short and "
                       "comes with a question back.<br><br>"
                       "<em>(<em>How's it going?</em> — yana bir salomlashish shakli. Kutilgan javob "
                       "qisqa va savol bilan qaytariladi.)</em></p>",
    },
    {
        "text": "<p>Complete the exchange.</p>"
                "<p><strong>Rozimurod teacher:</strong> What have you been up to, Behruz?</p>"
                "<p><strong>Behruz:</strong> ___</p>",
        "choices": [
            "I am up.",
            "Yes, I have been.",
            "Not much, really. Just studying.",
            "I was up at seven o'clock.",
        ],
        "correct": "Not much, really. Just studying.",
        "explanation": "<p><strong>Not much, really. Just studying.</strong> is correct. <em>What have "
                       "you been up to?</em> means \"what have you been doing lately?\" — the Present "
                       "Perfect Continuous is the natural tense here (PE-36).<br><br>"
                       "<em>(<em>What have you been up to?</em> — \"soʻnggi paytda nima qilyapsan?\" "
                       "degani. Bu yerda Present Perfect Continuous eng tabiiy zamon.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word.</p>"
                "<p><strong>___ , I'd better go — I've got a lesson at two.</strong></p>",
        "choices": ["Anyway", "However", "Therefore", "Although"],
        "correct": "Anyway",
        "explanation": "<p><strong>Anyway</strong> is correct — it is the standard signal that you are "
                       "about to leave, and <em>I'd better go</em> (PE-46) softens it.<br><br>"
                       "<em>(<em>Anyway</em> — ketmoqchi ekaningizni bildiruvchi standart signal, "
                       "<em>I'd better go</em> esa uni yumshatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the natural filler.</p>"
                "<p><strong>— How long have you been learning? — ___ , only about a month.</strong></p>",
        "choices": ["Yes", "Please", "Sorry", "Well"],
        "correct": "Well",
        "explanation": "<p><strong>Well</strong> is correct. Fillers — <em>Well…, Actually…, You know…, "
                       "I mean…</em> — buy you thinking time. They are not mistakes; they sound far more "
                       "natural than silence.<br><br>"
                       "<em>(Toʻldiruvchi soʻzlar oʻylash uchun vaqt beradi — oʻzbekchadagi \"xoʻsh\", "
                       "\"aslida\" kabi. Ular xato emas: jim qolishdan koʻra ancha tabiiy "
                       "eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Which reply is correct?</p>",
        "choices": [
            "— I like tea. — So I do.",
            "— I like tea. — So am I.",
            "— I like tea. — Also do I.",
            "— I like tea. — So do I.",
        ],
        "correct": "— I like tea. — So do I.",
        "explanation": "<p><strong>So do I.</strong> is correct. Two things must be right at once: the "
                       "auxiliary must match the speaker's verb, and the order must be inverted.<br><br>"
                       "<em>(Bir vaqtda ikki narsa toʻgʻri boʻlishi kerak: yordamchi feʼl gapiruvchining "
                       "feʼliga mos kelsin va soʻz tartibi teskari boʻlsin.)</em></p>",
    },
    {
        "text": "<p>Which reply is correct?</p>",
        "choices": [
            "— I don't like coffee. — Neither don't I.",
            "— I don't like coffee. — Neither do I.",
            "— I don't like coffee. — So don't I.",
            "— I don't like coffee. — Neither I don't.",
        ],
        "correct": "— I don't like coffee. — Neither do I.",
        "explanation": "<p><strong>Neither do I.</strong> is correct. Positive sentences take <em>So + "
                       "aux + I</em>; negative ones take <em>Neither + aux + I</em> — and never a second "
                       "negative.<br><br>"
                       "<em>(Ijobiy gapga <em>So + yordamchi + I</em>, inkor gapga <em>Neither + "
                       "yordamchi + I</em>. Ikkinchi inkor hech qachon qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which echo question matches the tense?</p>",
        "choices": [
            "— I went to London. — Oh, do you?",
            "— I went to London. — Oh, have you?",
            "— I went to London. — Oh, did you?",
            "— I went to London. — Oh, are you?",
        ],
        "correct": "— I went to London. — Oh, did you?",
        "explanation": "<p><strong>Oh, did you?</strong> is correct — the speaker used the past simple, "
                       "so the echo must be past too. Matching the tense is the whole trick.<br><br>"
                       "<em>(Gapiruvchi past simple ishlatdi, demak javob ham oʻtgan zamonda boʻlishi "
                       "kerak. Butun sir — zamonni moslashtirishda.)</em></p>",
    },
    {
        "text": "<p>In English culture, what is <strong>How are you?</strong>?</p>",
        "choices": [
            "Part of the greeting — reply short and ask back.",
            "A real question about your health — answer in detail.",
            "A rude question you should not answer.",
            "A question only doctors ask.",
        ],
        "correct": "Part of the greeting — reply short and ask back.",
        "explanation": "<p><strong>Part of the greeting — reply short and ask back.</strong> A long "
                       "answer about how you really feel is not expected. Save the details for a real "
                       "question, later in the conversation.<br><br>"
                       "<em>(Haqiqiy ahvolingiz haqidagi uzun javob kutilmaydi. Tafsilotlarni "
                       "suhbatning keyingi, haqiqiy savoliga saqlang.)</em></p>",
    },
    {
        "text": "<p>Which exchange has a mistake?</p>",
        "choices": [
            "Anyway, I'd better go — it was nice talking to you.",
            "— It was lovely to see you! — You too!",
            "— I passed my driving test! — Oh, do you?",
            "— I'm hungry. — So am I.",
        ],
        "correct": "— I passed my driving test! — Oh, do you?",
        "explanation": "<p><strong>— I passed my driving test! — Oh, do you?</strong> is the mistake — "
                       "the speaker used the past simple, so the echo must be <em>Did you? "
                       "Congratulations!</em><br><br>"
                       "<em>(Gapiruvchi past simple ishlatgan, shuning uchun javob <em>Did you?</em> "
                       "boʻlishi kerak.)</em></p>",
    },
    {
        "text": "<p>Which reply is correct?</p>",
        "choices": [
            "— I can't drive. — Neither can I.",
            "— I can't drive. — Neither can't I.",
            "— I can't drive. — So can I.",
            "— I can't drive. — Neither I can.",
        ],
        "correct": "— I can't drive. — Neither can I.",
        "explanation": "<p><strong>Neither can I.</strong> is correct — the pattern works with every "
                       "auxiliary: <em>So can I, Neither have I, So am I, Neither did I</em>.<br><br>"
                       "<em>(Qolip barcha yordamchi feʼllar bilan ishlaydi: <em>So can I, Neither have "
                       "I, So am I, Neither did I</em>.)</em></p>",
    },
    {
        "text": "<p>Which is the best way to end a conversation politely?</p>",
        "choices": [
            "Goodbye. Finish.",
            "I go now.",
            "Stop, I must go.",
            "Anyway, I'd better get going — I'm meeting my sister at five. It was lovely to see you!",
        ],
        "correct": "Anyway, I'd better get going — I'm meeting my sister at five. It was lovely to see you!",
        "explanation": "<p>The last one is correct: the signal (<em>Anyway</em>), a soft reason "
                       "(<em>I'd better…</em>) and something warm at the end. Leaving without the warm "
                       "line sounds abrupt in English.<br><br>"
                       "<em>(Signal (<em>Anyway</em>), yumshoq sabab (<em>I'd better…</em>) va oxirida "
                       "iliq jumla. Iliq jumlasiz ketish ingliz tilida qoʻpol eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Jasur:</strong> Hi Charos! How's it going?</p>"
                "<p><strong>Charos:</strong> Not bad, thanks. What about you?</p>"
                "<p><strong>Jasur:</strong> Fine. I've been revising all weekend.</p>"
                "<p><strong>Charos:</strong> ___</p>",
        "choices": [
            "Have you? So I have.",
            "Have you? So have I.",
            "Did you? So have I.",
            "Are you? So am I.",
        ],
        "correct": "Have you? So have I.",
        "explanation": "<p><strong>Have you? So have I.</strong> is correct — the echo question and the "
                       "agreement both take <em>have</em>, because Jasur said <em>I've been</em>. Two "
                       "small structures, and the conversation sounds completely natural.<br><br>"
                       "<em>(Takroriy savol ham, rozilik ham <em>have</em> oladi, chunki Jasur <em>I've "
                       "been</em> dedi. Ikkita kichik qurilma — va suhbat butunlay tabiiy "
                       "eshitiladi.)</em></p>",
    },
]


# =====================================================================
# PE-100 — Your Grammar Toolkit: The One-Page Review of Everything
# The capstone: one question from every major area of the course.
# =====================================================================
Q_PE100 = [
    {
        "text": "<p>Choose the correct tense.</p>"
                "<p><strong>Afsona ___ in this village for ten years, and she still loves "
                "it.</strong></p>",
        "choices": ["lives", "has lived", "is living", "lived"],
        "correct": "has lived",
        "explanation": "<p><strong>has lived</strong> is correct. It started in the past and is still "
                       "true, which is exactly what the Present Perfect is for (PE-33). Uzbek uses the "
                       "present here, and that is why <em>I live here for ten years</em> is such a common "
                       "error.<br><br>"
                       "<em>(Oʻtmishda boshlangan va hamon davom etyapti — Present Perfect aynan shuning "
                       "uchun. Oʻzbekchada hozirgi zamon ishlatilgani uchun bu xato juda koʻp "
                       "uchraydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tense.</p>"
                "<p><strong>By this time next year, Sherbek ___ his first English novel.</strong></p>",
        "choices": ["will finish", "is finishing", "finishes", "will have finished"],
        "correct": "will have finished",
        "explanation": "<p><strong>will have finished</strong> is correct — the Future Perfect, for "
                       "something completed <em>before</em> a point in the future (PE-40). "
                       "<em>By this time next year</em> is the classic signal.<br><br>"
                       "<em>(Future Perfect — kelajakdagi bir nuqtaga <strong>qadar</strong> tugaydigan "
                       "ish uchun. <em>By this time next year</em> — uning klassik "
                       "belgisi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct modal.</p>"
                "<p><strong>All the lights are off. They ___ be at home.</strong></p>",
        "choices": ["can't", "mustn't", "shouldn't", "don't have to"],
        "correct": "can't",
        "explanation": "<p><strong>can't</strong> is correct. On the certainty scale <em>can't be</em> is "
                       "the 5% end — \"it is impossible\" (PE-44). <em>Mustn't</em> belongs to the "
                       "obligation scale and means \"it is forbidden\" — a completely different "
                       "job.<br><br>"
                       "<em>(Ishonch shkalasida <em>can't be</em> — 5% chekkasi, yaʼni \"boʻlishi mumkin "
                       "emas\". <em>Mustn't</em> esa majburiyat shkalasida va \"taqiqlanadi\" degani — "
                       "butunlay boshqa vazifa.)</em></p>",
    },
    {
        "text": "<p>Choose the correct form.</p>"
                "<p><strong>I ___ you earlier — I'm sorry you found out from somebody else.</strong></p>",
        "choices": ["should tell", "must tell", "should have told", "would tell"],
        "correct": "should have told",
        "explanation": "<p><strong>should have told</strong> is correct — <em>modal + have + V3</em> is "
                       "how English talks about the past, and <em>should have</em> is regret for what you "
                       "did not do (PE-48).<br><br>"
                       "<em>(<em>modal + have + V3</em> — ingliz tilida oʻtgan zamon haqida gapirish "
                       "shakli. <em>should have</em> — qilinmagan ish uchun afsus.)</em></p>",
    },
    {
        "text": "<p>Choose the correct form.</p>"
                "<p><strong>If I ___ his number, I would call him.</strong> (I don't know it)</p>",
        "choices": ["know", "will know", "knew", "would know"],
        "correct": "knew",
        "explanation": "<p><strong>knew</strong> is correct — the second conditional, for an imaginary "
                       "present (PE-54). Each step into imagination moves the verb one step back, and "
                       "there is never a <em>will</em> or <em>would</em> after <em>if</em>.<br><br>"
                       "<em>(Ikkinchi turdagi shart gap — xayoliy hozirgi zamon uchun. Xayolga har bir "
                       "qadam feʼlni bir zamon orqaga suradi, <em>if</em> dan keyin esa hech qachon "
                       "<em>will</em> yoki <em>would</em> qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct form.</p>"
                "<p><strong>If Davron ___ enough this year, he will definitely buy a bicycle.</strong></p>",
        "choices": ["saves", "will save", "saved", "would save"],
        "correct": "saves",
        "explanation": "<p><strong>saves</strong> is correct — the first conditional, for a real future "
                       "(PE-53). The <em>if</em>-half stays in the present even though the meaning is "
                       "future.<br><br>"
                       "<em>(Birinchi turdagi shart gap — haqiqiy kelajak uchun. <em>if</em> qismi "
                       "hozirgi zamonda qoladi, garchi maʼno kelasi zamon boʻlsa ham.)</em></p>",
    },
    {
        "text": "<p>Choose the correct form.</p>"
                "<p><strong>If Marjona ___ harder, she would have passed the exam.</strong></p>",
        "choices": ["studied", "studies", "would study", "had studied"],
        "correct": "had studied",
        "explanation": "<p><strong>had studied</strong> is correct — the third conditional, for an "
                       "imaginary past (PE-56). One more step into imagination, one more step back for "
                       "the verb.<br><br>"
                       "<em>(Uchinchi turdagi shart gap — xayoliy oʻtmish uchun. Xayolga yana bir qadam — "
                       "feʼl uchun yana bir qadam orqaga.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ school, Iroda wants to study medicine.</strong></p>",
        "choices": ["When she will finish", "When she finishes", "When she is finishing", "When will she finish"],
        "correct": "When she finishes",
        "explanation": "<p><strong>When she finishes</strong> is correct. There is no <em>will</em> after "
                       "<em>when, if, as soon as, until, by the time</em> — one of the ten golden rules "
                       "(PE-26).<br><br>"
                       "<em>(<em>when, if, as soon as, until, by the time</em> dan keyin <em>will</em> "
                       "qoʻyilmaydi — bu oʻnta oltin qoidadan biri.)</em></p>",
    },
    {
        "text": "<p>Make it passive: <strong>Somebody stole Behruz's bike.</strong></p>",
        "choices": [
            "Behruz's bike stole.",
            "Behruz's bike is stolen yesterday.",
            "Somebody was stolen Behruz's bike.",
            "Behruz's bike was stolen.",
        ],
        "correct": "Behruz's bike was stolen.",
        "explanation": "<p><strong>Behruz's bike was stolen.</strong> is correct — <em>be</em> + V3, and "
                       "we drop <em>somebody</em> because we do not know who it was. That is exactly when "
                       "the passive is useful (PE-60).<br><br>"
                       "<em>(<em>be</em> + V3, va <em>somebody</em> tushirib qoldiriladi, chunki kim "
                       "ekanini bilmaymiz. Majhul nisbat aynan shunda foydali.)</em></p>",
    },
    {
        "text": "<p>Report this: <strong>\"My bike was stolen,\" Behruz said.</strong></p>",
        "choices": [
            "Behruz said his bike is stolen.",
            "Behruz said that his bike had been stolen.",
            "Behruz said that his bike has stolen.",
            "Behruz said that his bike was stole.",
        ],
        "correct": "Behruz said that his bike had been stolen.",
        "explanation": "<p><strong>Behruz said that his bike had been stolen.</strong> is correct. In "
                       "reported speech every tense steps one back (PE-62): <em>was stolen</em> becomes "
                       "<em>had been stolen</em>, and <em>my</em> becomes <em>his</em>.<br><br>"
                       "<em>(Koʻchirma gapda har bir zamon bir qadam orqaga suriladi va <em>my</em> "
                       "<em>his</em> ga aylanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct relative pronoun.</p>"
                "<p><strong>The teacher ___ told me to do it is Rozimurod.</strong></p>",
        "choices": ["which", "what", "who", "whose"],
        "correct": "who",
        "explanation": "<p><strong>who</strong> is correct — the relative pronoun for people (PE-58). "
                       "<em>Which</em> is for things, and <em>what</em> never joins a relative "
                       "clause.<br><br>"
                       "<em>(Odamlar uchun <em>who</em>. <em>Which</em> narsalar uchun, <em>what</em> esa "
                       "aniqlovchi ergash gapni umuman bogʻlamaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ the answer to that question.</strong></p>",
        "choices": ["know", "am knowing", "knows", "am know"],
        "correct": "know",
        "explanation": "<p><strong>know</strong> is correct. Stative verbs — <em>know, want, like, need, "
                       "understand, have</em> (own) — describe a state, not an action, so they take no "
                       "<em>-ing</em> (PE-13).<br><br>"
                       "<em>(Holat feʼllari harakatni emas, holatni bildiradi, shuning uchun ular "
                       "<em>-ing</em> olmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Did Samandar ___ to the meeting yesterday?</strong></p>",
        "choices": ["go", "went", "gone", "going"],
        "correct": "go",
        "explanation": "<p><strong>go</strong> is correct — one tense marker per verb phrase. "
                       "<em>Did</em> already carries the past, so the main verb goes bare "
                       "(PE-22).<br><br>"
                       "<em>(Bitta feʼl birikmasida bitta zamon belgisi. <em>Did</em> oʻtganlikni "
                       "koʻtargani uchun asosiy feʼl asl shaklda qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct version.</p>"
                "<p><strong>Charos ___ every day and she is very good ___ maths.</strong></p>",
        "choices": [
            "go to the school / in",
            "goes to the school / in",
            "goes to school / at",
            "go to school / at",
        ],
        "correct": "goes to school / at",
        "explanation": "<p><strong>goes to school / at</strong> is correct — three rules at once: the "
                       "third-person <em>-s</em> (PE-9), no <em>the</em> before <em>school</em> when you "
                       "mean the activity (PE-4), and the fixed partner <em>good at</em> "
                       "(PE-76).<br><br>"
                       "<em>(Bir vaqtda uchta qoida: uchinchi shaxs <em>-s</em>, faoliyat maʼnosidagi "
                       "<em>school</em> oldida <em>the</em> yoʻq, va qatʼiy juftlik "
                       "<em>good at</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs is very good at ___.</strong></p>",
        "choices": ["swim", "swimming", "to swim", "swims"],
        "correct": "swimming",
        "explanation": "<p><strong>swimming</strong> is correct — after a preposition, a verb always "
                       "takes <em>-ing</em> (PE-64). The same rule explains <em>look forward to "
                       "hearing</em> and <em>interested in learning</em>.<br><br>"
                       "<em>(Predlogdan keyin feʼl doim <em>-ing</em> oladi. Shu qoida <em>look forward "
                       "to hearing</em> va <em>interested in learning</em> ni ham tushuntiradi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I don't never smoke.",
            "Although I was tired, but I never stopped.",
            "I never don't smoke.",
            "Although I was tired, I never stopped.",
        ],
        "correct": "Although I was tired, I never stopped.",
        "explanation": "<p><strong>Although I was tired, I never stopped.</strong> is correct — one "
                       "negative per sentence, and one contrast word per sentence. Both errors come from "
                       "the same source: Uzbek needs two markers where English needs one (PE-11, "
                       "PE-52).<br><br>"
                       "<em>(Bitta gapda bitta inkor va bitta qarama-qarshilik soʻzi. Ikkala xatoning "
                       "sababi bitta: oʻzbekchada ikkita belgi kerak, ingliz tilida esa "
                       "bitta.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "I have been living here since 2018.",
            "I am living here since 2018.",
            "I've studied English for five years.",
            "I moved here in 2018.",
        ],
        "correct": "I am living here since 2018.",
        "explanation": "<p><strong>I am living here since 2018.</strong> is the mistake. <em>Since</em> "
                       "and <em>for</em> need a perfect tense — the present simple or continuous cannot "
                       "reach back into the past (PE-33).<br><br>"
                       "<em>(<em>Since</em> va <em>for</em> ga perfect zamon kerak. Hozirgi zamon "
                       "oʻtmishga qoʻl uzata olmaydi.)</em></p>",
    },
    {
        "text": "<p>Find the correct version of: <strong>She go to the school every day and she is "
                "very good in maths.</strong></p>",
        "choices": [
            "She goes to the school every day and she is very good in maths.",
            "She go to school every day and she is very good at maths.",
            "She goes to school every day and she is very good in maths.",
            "She goes to school every day and she is very good at maths.",
        ],
        "correct": "She goes to school every day and she is very good at maths.",
        "explanation": "<p>The last option fixes all three errors together. Each of the others still "
                       "leaves one in — which is exactly why the self-check works best as <strong>one "
                       "pass per problem</strong> rather than one general re-read (PE-92).<br><br>"
                       "<em>(Oxirgi variant uchala xatoni ham tuzatadi, qolganlarida bittasi qolgan. "
                       "Aynan shuning uchun oʻz-oʻzini tekshirish <strong>har bir xato uchun alohida "
                       "oʻqish</strong> bilan yaxshi ishlaydi.)</em></p>",
    },
    {
        "text": "<p>A beginner writes: <strong>Yesterday I go school. Teacher say me homework.</strong> "
                "Which is the version you can write now?</p>",
        "choices": [
            "Yesterday, while I was walking to school, I realised that I had forgotten the homework "
            "my teacher had told me to do.",
            "Yesterday I went school and teacher said me homework.",
            "Yesterday I was go to school and teacher was say me the homework.",
            "Yesterday I go to school and my teacher say me homework.",
        ],
        "correct": "Yesterday, while I was walking to school, I realised that I had forgotten the homework "
                   "my teacher had told me to do.",
        "explanation": "<p>The first version is the one. Look at what is working inside it: Past "
                       "Continuous for the background (PE-23), Past Perfect for what came earlier "
                       "(PE-38), a reported command (PE-63) and a relative clause with the pronoun left "
                       "out (PE-58). Same idea as the beginner's sentence — a hundred lessons of "
                       "difference.<br><br>"
                       "<em>(Uning ichida nima ishlayotganiga qarang: fon uchun Past Continuous, oldingi "
                       "ish uchun Past Perfect, koʻchirma buyruq va aniqlovchi ergash gap. Fikr oʻsha, "
                       "farq — yuzta dars.)</em></p>",
    },
    {
        "text": "<p>The last question of the course.</p>"
                "<p><strong>Rozimurod teacher:</strong> Well done — you have finished all one hundred "
                "lessons. So what comes next?</p>"
                "<p><strong>The class:</strong> ___</p>",
        "choices": [
            "Now we memorise all the rules again from lesson one.",
            "Now we stop speaking until our English is perfect.",
            "Now we read, write and speak every day — fluency comes from using English, not from "
            "waiting until it is perfect.",
            "Now grammar is finished, so English is finished.",
        ],
        "correct": "Now we read, write and speak every day — fluency comes from using English, not from "
                   "waiting until it is perfect.",
        "explanation": "<p>That is the right answer, and the last thing this course has to say. Grammar "
                       "is now the part of English you know best — from here, progress comes from "
                       "<strong>use</strong>, not study. Read fifteen minutes a day and copy whole "
                       "phrases, not single words. Write something every week and check it against the "
                       "ten golden rules. Speak imperfectly. Keep your own top three errors on the first "
                       "page of your notebook.<br><br>"
                       "<em>(Grammatika endi ingliz tilingizning eng kuchli qismi — bundan keyingi oʻsish "
                       "oʻrganishdan emas, <strong>ishlatishdan</strong> keladi. Har kuni oʻn besh daqiqa "
                       "oʻqing va yolgʻiz soʻzlarni emas, butun iboralarni koʻchirib oling. Har hafta "
                       "biror narsa yozing va uni oʻnta oltin qoida boʻyicha tekshiring. Xato bilan "
                       "boʻlsa ham gapiring — xato qilgan odam oʻrganadi, jim turgan odam esa yoʻq. "
                       "Omad, va oʻrganishni davom ettiring!)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-96 Practice: Describing People, Places and Things",
        "tutorial":    "PE-96:",
        "description": "PE-96 darsiga 20 savol: be + sifat va have got + ot, look like / be like / like "
                       "farqi, joyni There is / There are bilan tasvirlash va sifatlar tartibi. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE96,
    },
    {
        "title":       "PE-97 Practice: Describing Charts, Trends and Numbers",
        "tutorial":    "PE-97:",
        "description": "PE-97 darsiga 20 savol: rise / fall / peak / remain stable feʼllari, sharply va "
                       "slightly ravishlari, from … to / by / of predloglari, number va amount farqi. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE97,
    },
    {
        "title":       "PE-98 Practice: Making Excuses, Apologising and Explaining",
        "tutorial":    "PE-98:",
        "description": "PE-98 darsiga 20 savol: sorry for + -ing, sorry about + ot, sorry to + feʼl, "
                       "rasmiy uzr shakllari, bahonaning zamonlari va kechirimni qabul qilish. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE98,
    },
    {
        "title":       "PE-99 Practice: Small Talk and Everyday Conversation Grammar",
        "tutorial":    "PE-99:",
        "description": "PE-99 darsiga 20 savol: salomlashuv va kutilgan javoblar, takroriy savollar "
                       "(Oh, did you?), So do I / Neither do I, fillerlar va suhbatni chiroyli yakunlash. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE99,
    },
    {
        "title":       "PE-100 Practice: Your Grammar Toolkit: The One-Page Review of Everything",
        "tutorial":    "PE-100:",
        "description": "Kursning yakuniy testi: 20 savol butun Prime English boʻyicha — 12 zamon, modal "
                       "feʼllar, toʻrtta shart gap, majhul nisbat, koʻchirma gap, aniqlovchi ergash gap "
                       "va oʻnta oltin qoida. Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE100,
    },
]
