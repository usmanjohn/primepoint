# -*- coding: utf-8 -*-
"""Prime English practices — PE-71 … PE-75 (Block F: precision).

Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_71_75.py --master=prime --expect-questions=20
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
# PE-71 — Determiners
# =====================================================================

Q_PE71 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Every pupil ___ a textbook.</strong></p>",
        "choices": ["has", "have", "are having", "having"],
        "correct": "has",
        "explanation": "<p><strong>has</strong> is correct — <em>every</em> takes a singular noun and a "
                       "singular verb, even though it means the whole group.<br><br>"
                       "<em>(<strong>has</strong> toʻgʻri — <em>every</em> butun guruhni bildirsa ham, "
                       "birlikdagi ot va birlikdagi feʼl oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference between <em>every</em> and <em>each</em>?</strong></p>",
        "choices": ["every = the whole group · each = one by one",
                    "every = one by one · each = the whole group",
                    "They are always identical.",
                    "every is for two things, each for many."],
        "correct": "every = the whole group · each = one by one",
        "explanation": "<p><strong>every = the whole group · each = one by one</strong> is correct — and "
                       "<em>each</em> can be used for just two, <em>every</em> needs three or more."
                       "<br><br><em>(<strong>every = butun guruh · each = bittalab</strong> toʻgʻri — "
                       "<em>each</em> ikkitasi uchun ham ishlatiladi, <em>every</em> esa uch va undan "
                       "koʻp uchun.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher gave ___ pupil a different exercise.</strong></p>",
        "choices": ["each", "all", "both", "every ones"],
        "correct": "each",
        "explanation": "<p><strong>each</strong> is correct — the attention is on the individuals, one at "
                       "a time.<br><br>"
                       "<em>(<strong>each</strong> toʻgʻri — eʼtibor bittalab, har bir shaxsga "
                       "qaratilgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Everybody ___ ready for the test.</strong></p>",
        "choices": ["is", "are", "were", "have"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — <em>everybody, everyone, everything</em> all "
                       "take a singular verb. This surprises most learners.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — <em>everybody, everyone, everything</em> "
                       "hammasi birlikdagi feʼl oladi. Bu koʻpchilikni hayron qoldiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ Iroda and Charos passed the olympiad.</strong></p>",
        "choices": ["Both", "Every", "Each of", "Either"],
        "correct": "Both",
        "explanation": "<p><strong>Both</strong> is correct — <em>both</em> means the two of them "
                       "together, and it takes a plural verb.<br><br>"
                       "<em>(<strong>Both</strong> toʻgʻri — <em>both</em> ikkalasi birga degani va "
                       "koʻplikdagi feʼl oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Both pupils ___ the answer.</strong></p>",
        "choices": ["know", "knows", "is knowing", "has known"],
        "correct": "know",
        "explanation": "<p><strong>know</strong> is correct — <em>both</em> is the one word in this "
                       "family that is genuinely plural.<br><br>"
                       "<em>(<strong>know</strong> toʻgʻri — <em>both</em> bu guruhdagi haqiqatan ham "
                       "koʻplikdagi yagona soʻz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>You can take ___ book — they're both good.</strong></p>",
        "choices": ["either", "both", "neither", "every"],
        "correct": "either",
        "explanation": "<p><strong>either</strong> is correct — <em>either</em> = one of the two, it "
                       "doesn't matter which.<br><br>"
                       "<em>(<strong>either</strong> toʻgʻri — <em>either</em> = ikkisidan biri, qaysi "
                       "biri boʻlishi muhim emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ of the answers is correct — try again.</strong></p>",
        "choices": ["Neither", "Both", "Either", "Every"],
        "correct": "Neither",
        "explanation": "<p><strong>Neither</strong> is correct — <em>neither</em> = not one and not the "
                       "other, and it takes a singular verb.<br><br>"
                       "<em>(<strong>Neither</strong> toʻgʻri — <em>neither</em> = na u, na bu, va u "
                       "birlikdagi feʼl oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which words are only for <em>exactly two</em>?</strong></p>",
        "choices": ["both, either, neither", "every, all, each",
                    "some, any, no", "much, many, a lot of"],
        "correct": "both, either, neither",
        "explanation": "<p><strong>both, either, neither</strong> is correct — for three or more you need "
                       "<em>all, any, none</em>.<br><br>"
                       "<em>(<strong>both, either, neither</strong> toʻgʻri — uch va undan koʻp uchun "
                       "<em>all, any, none</em> kerak boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ the pupils in our class study English.</strong></p>",
        "choices": ["All", "Every", "Each", "Both"],
        "correct": "All",
        "explanation": "<p><strong>All</strong> is correct — <em>all + plural noun + plural verb</em>, "
                       "unlike <em>every</em>.<br><br>"
                       "<em>(<strong>All</strong> toʻgʻri — <em>every</em> dan farqli oʻlaroq, "
                       "<em>all + koʻplikdagi ot + koʻplikdagi feʼl</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ of Samandar's brothers lives in Tashkent.</strong></p>",
        "choices": ["Neither", "Both", "All", "Every"],
        "correct": "Neither",
        "explanation": "<p><strong>Neither</strong> is correct — the singular verb <em>lives</em> tells "
                       "you the answer.<br><br>"
                       "<em>(<strong>Neither</strong> toʻgʻri — birlikdagi feʼl <em>lives</em> javobni "
                       "koʻrsatib turibdi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ of the pupils came — the classroom was empty.</strong></p>",
        "choices": ["None", "Neither", "No", "All"],
        "correct": "None",
        "explanation": "<p><strong>None</strong> is correct — <em>none</em> is for three or more; "
                       "<em>neither</em> is only for two.<br><br>"
                       "<em>(<strong>None</strong> toʻgʻri — <em>none</em> uch va undan koʻp uchun; "
                       "<em>neither</em> esa faqat ikkitasi uchun.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek goes to the gym ___ day.</strong></p>",
        "choices": ["every", "all", "each of", "both"],
        "correct": "every",
        "explanation": "<p><strong>every</strong> is correct — <em>every day, every week, every "
                       "morning</em> are the fixed time expressions.<br><br>"
                       "<em>(<strong>every</strong> toʻgʻri — <em>every day, every week, every "
                       "morning</em> — qatʼiy vaqt iboralari.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs and Javohir both ___ chess very well.</strong></p>",
        "choices": ["play", "plays", "is playing", "has played"],
        "correct": "play",
        "explanation": "<p><strong>play</strong> is correct — two people joined by <em>and</em>, and "
                       "<em>both</em> confirms the plural.<br><br>"
                       "<em>(<strong>play</strong> toʻgʻri — <em>and</em> bilan bogʻlangan ikki kishi, "
                       "<em>both</em> esa koʻplikni tasdiqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Neither Madina ___ Shaxzoda was late.</strong></p>",
        "choices": ["nor", "or", "and", "either"],
        "correct": "nor",
        "explanation": "<p><strong>nor</strong> is correct — the fixed pairs are <em>neither … nor</em> "
                       "and <em>either … or</em>.<br><br>"
                       "<em>(<strong>nor</strong> toʻgʻri — qatʼiy juftliklar: <em>neither … nor</em> va "
                       "<em>either … or</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Either Abdulloh ___ Sirojiddin will bring the ball.</strong></p>",
        "choices": ["or", "nor", "and", "neither"],
        "correct": "or",
        "explanation": "<p><strong>or</strong> is correct — <em>either … or</em>, one of the two will do "
                       "it.<br><br>"
                       "<em>(<strong>or</strong> toʻgʻri — <em>either … or</em>, ikkisidan biri buni "
                       "bajaradi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Every pupils have a notebook.", "Every pupil has a notebook.",
                    "All the pupils have notebooks.", "Each pupil has a notebook."],
        "correct": "Every pupils have a notebook.",
        "explanation": "<p><strong>Every pupils have a notebook.</strong> is the mistake — <em>every</em> "
                       "needs a singular noun and a singular verb.<br><br>"
                       "<em>(<strong>Every pupils have a notebook.</strong> xato — <em>every</em> "
                       "birlikdagi ot va birlikdagi feʼl talab qiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Everybody was happy with the results.",
                    "Everybody were happy with the results.",
                    "Everybody are happy with the results.",
                    "All body was happy with the results."],
        "correct": "Everybody was happy with the results.",
        "explanation": "<p><strong>Everybody was happy with the results.</strong> is correct — singular "
                       "verb, however many people are meant.<br><br>"
                       "<em>(<strong>Everybody was happy with the results.</strong> toʻgʻri — nechta odam "
                       "nazarda tutilishidan qatʼi nazar, feʼl birlikda.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Did Behruz or Davron win the chess match?</p>"
                "<p><strong>Marjona:</strong> ___</p>",
        "choices": ["Neither of them — it was a draw.", "None of them — it was a draw.",
                    "Both of them didn't — it was a draw.", "Either of them — it was a draw."],
        "correct": "Neither of them — it was a draw.",
        "explanation": "<p><strong>Neither of them — it was a draw.</strong> is correct — exactly two "
                       "players, so <em>neither</em>, not <em>none</em>.<br><br>"
                       "<em>(<strong>Neither of them — it was a draw.</strong> toʻgʻri — aynan ikki "
                       "oʻyinchi, shuning uchun <em>none</em> emas, <em>neither</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> determiner is correct.</p>",
        "choices": ["Every pupil has a book, both girls have finished, "
                    "and neither boy is late.",
                    "Every pupils have a book, both girl has finished, "
                    "and neither boys are late.",
                    "Each pupils has a book, both girls has finished, "
                    "and neither boy are late.",
                    "Every pupil have a book, both girls has finished, "
                    "and none boy is late."],
        "correct": "Every pupil has a book, both girls have finished, "
                   "and neither boy is late.",
        "explanation": "<p><strong>every … has · both … have · neither … is</strong> is correct — two "
                       "singulars around one genuine plural.<br><br>"
                       "<em>(<strong>every … has · both … have · neither … is</strong> toʻgʻri — bitta "
                       "haqiqiy koʻplik atrofida ikkita birlik.)</em></p>",
    },
]


# =====================================================================
# PE-72 — Word Order: SVOMPT
# =====================================================================

Q_PE72 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does SVOMPT stand for?</strong></p>",
        "choices": ["Subject–Verb–Object–Manner–Place–Time",
                    "Subject–Verb–Object–Place–Manner–Time",
                    "Subject–Verb–Time–Place–Object–Manner",
                    "Subject–Object–Verb–Manner–Time–Place"],
        "correct": "Subject–Verb–Object–Manner–Place–Time",
        "explanation": "<p><strong>Subject–Verb–Object–Manner–Place–Time</strong> is correct — who, did, "
                       "what, how, where, when.<br><br>"
                       "<em>(<strong>Subject–Verb–Object–Manner–Place–Time</strong> toʻgʻri — kim, "
                       "qildi, nimani, qanday, qayerda, qachon.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word order.</p>",
        "choices": ["Afsona sang a song beautifully at the concert last night.",
                    "Afsona sang beautifully a song at the concert last night.",
                    "Afsona sang a song at the concert beautifully last night.",
                    "Afsona last night sang beautifully a song at the concert."],
        "correct": "Afsona sang a song beautifully at the concert last night.",
        "explanation": "<p><strong>Afsona sang a song beautifully at the concert last night.</strong> is "
                       "correct — all six links in order.<br><br>"
                       "<em>(<strong>Afsona sang a song beautifully at the concert last night.</strong> "
                       "toʻgʻri — oltala boʻgʻin oʻz tartibida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What must never be separated?</strong></p>",
        "choices": ["the verb and its object", "the subject and the verb",
                    "the place and the time", "the manner and the place"],
        "correct": "the verb and its object",
        "explanation": "<p><strong>the verb and its object</strong> is correct — nothing may stand "
                       "between them: <em>I like very much English</em> ✗.<br><br>"
                       "<em>(<strong>feʼl va uning toʻldiruvchisi</strong> toʻgʻri — ular orasiga hech "
                       "narsa qoʻyilmaydi: <em>I like very much English</em> ✗.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz plays ___ .</strong></p>",
        "choices": ["football very well", "very well football",
                    "football well very", "well very football"],
        "correct": "football very well",
        "explanation": "<p><strong>football very well</strong> is correct — the object comes first, then "
                       "the manner.<br><br>"
                       "<em>(<strong>football very well</strong> toʻgʻri — avval toʻldiruvchi, keyin "
                       "tarz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word order.</p>",
        "choices": ["Iroda studies English at home every evening.",
                    "Iroda studies at home English every evening.",
                    "Iroda studies every evening English at home.",
                    "Iroda every evening studies English at home."],
        "correct": "Iroda studies English at home every evening.",
        "explanation": "<p><strong>Iroda studies English at home every evening.</strong> is correct — "
                       "object, place, time.<br><br>"
                       "<em>(<strong>Iroda studies English at home every evening.</strong> toʻgʻri — "
                       "toʻldiruvchi, joy, vaqt.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which comes first — place or time?</strong></p>",
        "choices": ["place", "time", "either order is fine", "it depends on the verb"],
        "correct": "place",
        "explanation": "<p><strong>place</strong> is correct — <em>at the concert last night</em>, never "
                       "the other way round. Uzbek does the opposite, which is why this needs "
                       "practice.<br><br>"
                       "<em>(<strong>joy</strong> toʻgʻri — <em>at the concert last night</em>, aksincha "
                       "emas. Oʻzbekcha teskarisini qiladi, shuning uchun mashq kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word order.</p>",
        "choices": ["Charos went to Samarkand by train last summer.",
                    "Charos went last summer by train to Samarkand.",
                    "Charos went by train last summer to Samarkand.",
                    "Charos last summer went to Samarkand by train."],
        "correct": "Charos went to Samarkand by train last summer.",
        "explanation": "<p><strong>Charos went to Samarkand by train last summer.</strong> is correct — "
                       "the manner (<em>by train</em>) and the place can swap when the place belongs to "
                       "the verb of movement, but the time still comes last.<br><br>"
                       "<em>(<strong>Charos went to Samarkand by train last summer.</strong> toʻgʻri — "
                       "harakat feʼli bilan joy va tarz oʻrin almashishi mumkin, lekin vaqt baribir "
                       "oxirida qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Where can a time expression also stand?</strong></p>",
        "choices": ["at the beginning of the sentence", "between the verb and the object",
                    "between the subject and the verb", "nowhere else"],
        "correct": "at the beginning of the sentence",
        "explanation": "<p><strong>at the beginning of the sentence</strong> is correct — <em>Last night "
                       "Afsona sang at the concert</em> is fine, for emphasis.<br><br>"
                       "<em>(<strong>gap boshida</strong> toʻgʻri — urgʻu uchun <em>Last night Afsona "
                       "sang at the concert</em> deyish mumkin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ his homework.</strong></p>",
        "choices": ["always does", "does always", "always is doing", "do always"],
        "correct": "always does",
        "explanation": "<p><strong>always does</strong> is correct — adverbs of frequency sit before an "
                       "ordinary verb, as you learned in PE-11.<br><br>"
                       "<em>(<strong>always does</strong> toʻgʻri — chastota ravishlari oddiy feʼldan "
                       "oldin turadi, PE-11 dagidek.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word order.</p>",
        "choices": ["Elbek gave Firdavs his notes.", "Elbek gave his notes Firdavs.",
                    "Elbek gave to Firdavs his notes.", "Elbek Firdavs gave his notes."],
        "correct": "Elbek gave Firdavs his notes.",
        "explanation": "<p><strong>Elbek gave Firdavs his notes.</strong> is correct — pattern one: "
                       "<em>give + person + thing</em>, with no <em>to</em>.<br><br>"
                       "<em>(<strong>Elbek gave Firdavs his notes.</strong> toʻgʻri — birinchi qolip: "
                       "<em>give + shaxs + narsa</em>, <em>to</em> siz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word order.</p>",
        "choices": ["Elbek gave his notes to Firdavs.", "Elbek gave to Firdavs his notes.",
                    "Elbek gave his notes Firdavs to.", "Elbek to Firdavs gave his notes."],
        "correct": "Elbek gave his notes to Firdavs.",
        "explanation": "<p><strong>Elbek gave his notes to Firdavs.</strong> is correct — pattern two: "
                       "<em>give + thing + to + person</em>. Both patterns are right; mixing them is "
                       "not.<br><br>"
                       "<em>(<strong>Elbek gave his notes to Firdavs.</strong> toʻgʻri — ikkinchi qolip: "
                       "<em>give + narsa + to + shaxs</em>. Ikki qolip ham toʻgʻri, ularni aralashtirish "
                       "esa xato.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word order.</p>",
        "choices": ["Javohir reads books quickly in the library after school.",
                    "Javohir reads quickly books in the library after school.",
                    "Javohir reads books in the library quickly after school.",
                    "Javohir reads books after school quickly in the library."],
        "correct": "Javohir reads books quickly in the library after school.",
        "explanation": "<p><strong>Javohir reads books quickly in the library after school.</strong> is "
                       "correct — object, manner, place, time.<br><br>"
                       "<em>(<strong>Javohir reads books quickly in the library after school.</strong> "
                       "toʻgʻri — toʻldiruvchi, tarz, joy, vaqt.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina speaks ___ .</strong></p>",
        "choices": ["Korean fluently", "fluently Korean",
                    "Korean fluent", "fluent Korean very"],
        "correct": "Korean fluently",
        "explanation": "<p><strong>Korean fluently</strong> is correct — the object cannot be pushed "
                       "behind the adverb.<br><br>"
                       "<em>(<strong>Korean fluently</strong> toʻgʻri — toʻldiruvchini ravishdan keyinga "
                       "surib boʻlmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word order.</p>",
        "choices": ["Shaxzoda met her friend at the bus stop this morning.",
                    "Shaxzoda met at the bus stop her friend this morning.",
                    "Shaxzoda met her friend this morning at the bus stop quickly.",
                    "Shaxzoda this morning met at the bus stop her friend."],
        "correct": "Shaxzoda met her friend at the bus stop this morning.",
        "explanation": "<p><strong>Shaxzoda met her friend at the bus stop this morning.</strong> is "
                       "correct — the object stays next to the verb, then place, then time.<br><br>"
                       "<em>(<strong>Shaxzoda met her friend at the bus stop this morning.</strong> "
                       "toʻgʻri — toʻldiruvchi feʼl yonida qoladi, keyin joy, keyin vaqt.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh finished the test ___ .</strong></p>",
        "choices": ["quickly yesterday", "yesterday quickly",
                    "quick yesterday", "yesterday quick"],
        "correct": "quickly yesterday",
        "explanation": "<p><strong>quickly yesterday</strong> is correct — manner before time, and the "
                       "adverb keeps its <em>-ly</em>.<br><br>"
                       "<em>(<strong>quickly yesterday</strong> toʻgʻri — tarz vaqtdan oldin, ravish esa "
                       "<em>-ly</em> ni saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word order.</p>",
        "choices": ["Rozimurod teacher explained the rule clearly to us today.",
                    "Rozimurod teacher explained clearly the rule to us today.",
                    "Rozimurod teacher today explained clearly to us the rule.",
                    "Rozimurod teacher explained to us today the rule clearly."],
        "correct": "Rozimurod teacher explained the rule clearly to us today.",
        "explanation": "<p><strong>Rozimurod teacher explained the rule clearly to us today.</strong> is "
                       "correct — object, manner, then the rest.<br><br>"
                       "<em>(<strong>Rozimurod teacher explained the rule clearly to us today.</strong> "
                       "toʻgʻri — toʻldiruvchi, tarz, keyin qolgani.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Sirojiddin likes very much football.",
                    "Sirojiddin likes football very much.",
                    "Sirojiddin really likes football.",
                    "Sirojiddin likes football a lot."],
        "correct": "Sirojiddin likes very much football.",
        "explanation": "<p><strong>Sirojiddin likes very much football.</strong> is the mistake — nothing "
                       "may stand between the verb and its object.<br><br>"
                       "<em>(<strong>Sirojiddin likes very much football.</strong> xato — feʼl bilan "
                       "toʻldiruvchi orasiga hech narsa qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Marjona sang at the concert last night.",
                    "Marjona sang last night at the concert beautiful.",
                    "Marjona at the concert sang last night.",
                    "Marjona sang last night at the concert quick."],
        "correct": "Marjona sang at the concert last night.",
        "explanation": "<p><strong>Marjona sang at the concert last night.</strong> is correct — place "
                       "before time.<br><br>"
                       "<em>(<strong>Marjona sang at the concert last night.</strong> toʻgʻri — joy "
                       "vaqtdan oldin.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Davron:</strong> What did you do at the weekend?</p>"
                "<p><strong>Iroda:</strong> ___</p>",
        "choices": ["I read a book quietly at home on Sunday.",
                    "I read quietly a book at home on Sunday.",
                    "I read a book on Sunday quietly at home.",
                    "I on Sunday read a book quietly at home."],
        "correct": "I read a book quietly at home on Sunday.",
        "explanation": "<p><strong>I read a book quietly at home on Sunday.</strong> is correct — the "
                       "whole chain, in order.<br><br>"
                       "<em>(<strong>I read a book quietly at home on Sunday.</strong> toʻgʻri — butun "
                       "zanjir oʻz tartibida.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is in the right place.</p>",
        "choices": ["Behruz always plays football well at the stadium on Saturdays.",
                    "Behruz plays always well football at the stadium on Saturdays.",
                    "Behruz always plays well football on Saturdays at the stadium.",
                    "Behruz plays football always well on Saturdays at the stadium."],
        "correct": "Behruz always plays football well at the stadium on Saturdays.",
        "explanation": "<p><strong>always plays … football well … at the stadium … on Saturdays</strong> "
                       "is correct — frequency before the verb, then object, manner, place, time."
                       "<br><br><em>(<strong>always plays … football well … at the stadium … on "
                       "Saturdays</strong> toʻgʻri — chastota feʼldan oldin, keyin toʻldiruvchi, tarz, "
                       "joy va vaqt.)</em></p>",
    },
]


# =====================================================================
# PE-73 — Question Tags
# =====================================================================

Q_PE73 = [
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>You are tired, ___ ?</strong></p>",
        "choices": ["aren't you", "are you", "isn't it", "don't you"],
        "correct": "aren't you",
        "explanation": "<p><strong>aren't you</strong> is correct — a positive sentence takes a negative "
                       "tag, repeating the same helper.<br><br>"
                       "<em>(<strong>aren't you</strong> toʻgʻri — tasdiq gap inkor tag oladi va oʻsha "
                       "yordamchi takrorlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Charos hasn't finished, ___ ?</strong></p>",
        "choices": ["has she", "hasn't she", "did she", "is she"],
        "correct": "has she",
        "explanation": "<p><strong>has she</strong> is correct — a negative sentence takes a positive "
                       "tag.<br><br>"
                       "<em>(<strong>has she</strong> toʻgʻri — inkor gap tasdiq tag oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Behruz can swim, ___ ?</strong></p>",
        "choices": ["can't he", "can he", "doesn't he", "isn't he"],
        "correct": "can't he",
        "explanation": "<p><strong>can't he</strong> is correct — the modal is repeated, with the sign "
                       "flipped.<br><br>"
                       "<em>(<strong>can't he</strong> toʻgʻri — modal takrorlanadi, belgisi esa "
                       "almashadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Iroda studies Korean, ___ ?</strong></p>",
        "choices": ["doesn't she", "isn't she", "hasn't she", "don't she"],
        "correct": "doesn't she",
        "explanation": "<p><strong>doesn't she</strong> is correct — when there is no helper in the "
                       "sentence, <em>do / does / did</em> steps in.<br><br>"
                       "<em>(<strong>doesn't she</strong> toʻgʻri — gapda yordamchi boʻlmasa, "
                       "<em>do / does / did</em> paydo boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Samandar went home early, ___ ?</strong></p>",
        "choices": ["didn't he", "doesn't he", "wasn't he", "hasn't he"],
        "correct": "didn't he",
        "explanation": "<p><strong>didn't he</strong> is correct — a past simple sentence takes "
                       "<em>did</em> in the tag.<br><br>"
                       "<em>(<strong>didn't he</strong> toʻgʻri — past simple gap tagda <em>did</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>I am late, ___ ?</strong></p>",
        "choices": ["aren't I", "amn't I", "am not I", "isn't I"],
        "correct": "aren't I",
        "explanation": "<p><strong>aren't I</strong> is correct — English has no <em>amn't</em>, so this "
                       "irregular tag fills the gap.<br><br>"
                       "<em>(<strong>aren't I</strong> toʻgʻri — ingliz tilida <em>amn't</em> yoʻq, "
                       "shuning uchun bu notoʻgʻri shakl oʻrnini bosadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Let's start the game, ___ ?</strong></p>",
        "choices": ["shall we", "will we", "don't we", "shan't we"],
        "correct": "shall we",
        "explanation": "<p><strong>shall we</strong> is correct — <em>Let's …</em> always takes "
                       "<em>shall we</em>.<br><br>"
                       "<em>(<strong>shall we</strong> toʻgʻri — <em>Let's …</em> doim <em>shall we</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Close the window, ___ ?</strong></p>",
        "choices": ["will you", "shall we", "don't you", "won't we"],
        "correct": "will you",
        "explanation": "<p><strong>will you</strong> is correct — an imperative takes <em>will you</em>, "
                       "which also makes it politer.<br><br>"
                       "<em>(<strong>will you</strong> toʻgʻri — buyruq gap <em>will you</em> oladi va "
                       "bu uni odobliroq qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>There is a test tomorrow, ___ ?</strong></p>",
        "choices": ["isn't there", "isn't it", "aren't there", "doesn't it"],
        "correct": "isn't there",
        "explanation": "<p><strong>isn't there</strong> is correct — with <em>there is / there are</em> "
                       "the word <em>there</em> is repeated as if it were the subject.<br><br>"
                       "<em>(<strong>isn't there</strong> toʻgʻri — <em>there is / there are</em> bilan "
                       "<em>there</em> soʻzi xuddi subject kabi takrorlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Elbek never eats meat, ___ ?</strong></p>",
        "choices": ["does he", "doesn't he", "did he", "is he"],
        "correct": "does he",
        "explanation": "<p><strong>does he</strong> is correct — <em>never</em> makes the sentence "
                       "negative in meaning, so the tag turns positive.<br><br>"
                       "<em>(<strong>does he</strong> toʻgʻri — <em>never</em> gapni maʼno jihatidan "
                       "inkor qiladi, shuning uchun tag tasdiq boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Everybody was there, ___ ?</strong></p>",
        "choices": ["weren't they", "wasn't he", "wasn't everybody", "weren't there"],
        "correct": "weren't they",
        "explanation": "<p><strong>weren't they</strong> is correct — <em>everybody</em> takes a singular "
                       "verb but is answered by the pronoun <em>they</em>.<br><br>"
                       "<em>(<strong>weren't they</strong> toʻgʻri — <em>everybody</em> birlikdagi feʼl "
                       "oladi, lekin olmoshi <em>they</em> boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Nobody phoned, ___ ?</strong></p>",
        "choices": ["did they", "didn't they", "did he", "didn't nobody"],
        "correct": "did they",
        "explanation": "<p><strong>did they</strong> is correct — <em>nobody</em> is negative, so the tag "
                       "is positive, and the pronoun is <em>they</em>.<br><br>"
                       "<em>(<strong>did they</strong> toʻgʻri — <em>nobody</em> inkor, shuning uchun tag "
                       "tasdiq, olmosh esa <em>they</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Firdavs will help us, ___ ?</strong></p>",
        "choices": ["won't he", "will he", "doesn't he", "shan't he"],
        "correct": "won't he",
        "explanation": "<p><strong>won't he</strong> is correct — <em>will</em> flips to "
                       "<em>won't</em>.<br><br>"
                       "<em>(<strong>won't he</strong> toʻgʻri — <em>will</em> <em>won't</em> ga "
                       "aylanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Javohir has been to Bukhara, ___ ?</strong></p>",
        "choices": ["hasn't he", "isn't he", "didn't he", "doesn't he"],
        "correct": "hasn't he",
        "explanation": "<p><strong>hasn't he</strong> is correct — the first helper "
                       "(<em>has</em>) is the one repeated.<br><br>"
                       "<em>(<strong>hasn't he</strong> toʻgʻri — birinchi yordamchi (<em>has</em>) "
                       "takrorlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Madina and Shaxzoda are sisters, ___ ?</strong></p>",
        "choices": ["aren't they", "isn't she", "aren't we", "don't they"],
        "correct": "aren't they",
        "explanation": "<p><strong>aren't they</strong> is correct — the tag always uses a pronoun, never "
                       "the names.<br><br>"
                       "<em>(<strong>aren't they</strong> toʻgʻri — tagda doim olmosh ishlatiladi, ismlar "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does a <em>falling</em> intonation on the tag mean?</strong></p>",
        "choices": ["I'm sure — just confirm it.",
                    "I really don't know — please tell me.",
                    "I am angry.",
                    "It changes nothing."],
        "correct": "I'm sure — just confirm it.",
        "explanation": "<p><strong>I'm sure — just confirm it.</strong> is correct — rising intonation "
                       "would be a genuine question.<br><br>"
                       "<em>(<strong>Ishonchim komil — shunchaki tasdiqlang.</strong> toʻgʻri — "
                       "koʻtariluvchi ohang esa haqiqiy savol boʻlardi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct tag.</p>"
                "<p><strong>Abdulloh doesn't like coffee, ___ ?</strong></p>",
        "choices": ["does he", "doesn't he", "is he", "did he"],
        "correct": "does he",
        "explanation": "<p><strong>does he</strong> is correct — negative sentence, positive tag, same "
                       "helper.<br><br>"
                       "<em>(<strong>does he</strong> toʻgʻri — inkor gap, tasdiq tag, oʻsha "
                       "yordamchi.)</em></p>",
    },
    {
        "text": "<p>Which tag <strong>has a mistake</strong>?</p>",
        "choices": ["Sirojiddin plays chess, doesn't Sirojiddin?",
                    "Sirojiddin plays chess, doesn't he?",
                    "Sirojiddin doesn't play chess, does he?",
                    "Sirojiddin played chess, didn't he?"],
        "correct": "Sirojiddin plays chess, doesn't Sirojiddin?",
        "explanation": "<p><strong>Sirojiddin plays chess, doesn't Sirojiddin?</strong> is the mistake — "
                       "a tag always uses a pronoun.<br><br>"
                       "<em>(<strong>Sirojiddin plays chess, doesn't Sirojiddin?</strong> xato — tagda "
                       "doim olmosh ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Marjona:</strong> ___</p>"
                "<p><strong>Rozimurod teacher:</strong> Yes, on Friday. Don't forget your pens.</p>",
        "choices": ["We have a test this week, don't we?",
                    "We have a test this week, haven't we got?",
                    "We have a test this week, isn't it?",
                    "We have a test this week, do we?"],
        "correct": "We have a test this week, don't we?",
        "explanation": "<p><strong>We have a test this week, don't we?</strong> is correct — <em>have</em> "
                       "as an ordinary verb needs <em>do</em> in the tag.<br><br>"
                       "<em>(<strong>We have a test this week, don't we?</strong> toʻgʻri — oddiy feʼl "
                       "sifatidagi <em>have</em> tagda <em>do</em> talab qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> tag is correct.</p>",
        "choices": ["You're ready, aren't you? Let's begin, shall we? "
                    "And nobody is missing, are they?",
                    "You're ready, are you? Let's begin, will we? "
                    "And nobody is missing, aren't they?",
                    "You're ready, isn't it? Let's begin, don't we? "
                    "And nobody is missing, is he?",
                    "You're ready, aren't you? Let's begin, do we? "
                    "And nobody is missing, isn't they?"],
        "correct": "You're ready, aren't you? Let's begin, shall we? "
                   "And nobody is missing, are they?",
        "explanation": "<p><strong>aren't you … shall we … are they</strong> is correct — a normal flip, "
                       "the <em>Let's</em> special case, and a negative word answered positively."
                       "<br><br><em>(<strong>aren't you … shall we … are they</strong> toʻgʻri — oddiy "
                       "almashinish, <em>Let's</em> istisnosi va inkor soʻzga tasdiq javob.)</em></p>",
    },
]


# =====================================================================
# PE-74 — Subject–Verb Agreement
# =====================================================================

Q_PE74 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The box of old books ___ heavy.</strong></p>",
        "choices": ["is", "are", "were", "have"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — the head noun is <em>box</em>; <em>of old "
                       "books</em> is only decoration.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — asosiy ot <em>box</em>; <em>of old books</em> "
                       "esa faqat qoʻshimcha.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The book on the shelf near the windows ___ mine.</strong></p>",
        "choices": ["is", "are", "were", "have been"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — cross out everything between the head noun "
                       "and the verb, and the answer is obvious.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — asosiy ot bilan feʼl orasidagi hamma narsani "
                       "oʻchirsangiz, javob koʻrinib qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz and Elbek ___ in the same class.</strong></p>",
        "choices": ["are", "is", "was", "has been"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct — <em>and</em> genuinely creates a plural "
                       "subject.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri — <em>and</em> haqiqatan ham koʻplikdagi "
                       "subject hosil qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda, together with her sisters, ___ coming to the concert.</strong></p>",
        "choices": ["is", "are", "were", "have"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — <em>together with, as well as, along "
                       "with</em> do <em>not</em> make the subject plural.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — <em>together with, as well as, along "
                       "with</em> subjectni koʻplikka <em>aylantirmaydi</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos as well as her friends ___ studying Korean.</strong></p>",
        "choices": ["is", "are", "were", "have been"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — only <em>and</em> creates a plural; the other "
                       "phrases are just extra information.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — faqat <em>and</em> koʻplik hosil qiladi; "
                       "qolgan iboralar shunchaki qoʻshimcha maʼlumot.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The news ___ very good today.</strong></p>",
        "choices": ["is", "are", "were", "have been"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — <em>news</em> ends in <em>-s</em> but is "
                       "singular, like <em>mathematics</em> and <em>physics</em>.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — <em>news</em> <em>-s</em> bilan tugasa ham "
                       "birlikda, xuddi <em>mathematics</em> va <em>physics</em> kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Mathematics ___ Samandar's favourite subject.</strong></p>",
        "choices": ["is", "are", "were", "have been"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — school subjects ending in <em>-ics</em> are "
                       "singular.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — <em>-ics</em> bilan tugagan fan nomlari "
                       "birlikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>These trousers ___ too long for Firdavs.</strong></p>",
        "choices": ["are", "is", "was", "has been"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct — <em>trousers, scissors, glasses, jeans</em> "
                       "are always plural.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri — <em>trousers, scissors, glasses, jeans</em> "
                       "doim koʻplikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The people in this photo ___ my classmates.</strong></p>",
        "choices": ["are", "is", "was", "has been"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct — <em>people</em> is already plural, with no "
                       "<em>-s</em>.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri — <em>people</em> <em>-s</em> siz allaqachon "
                       "koʻplikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Twenty thousand soum ___ enough for the ticket.</strong></p>",
        "choices": ["is", "are", "were", "have been"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — an amount of money is treated as one single "
                       "quantity.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — pul miqdori bitta yaxlit miqdor sifatida "
                       "qaraladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Three hours ___ a long time to wait.</strong></p>",
        "choices": ["is", "are", "were", "have been"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — time, money and distance amounts take a "
                       "singular verb.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — vaqt, pul va masofa miqdorlari birlikdagi feʼl "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Everyone in the two classes ___ taken the test.</strong></p>",
        "choices": ["has", "have", "were", "are"],
        "correct": "has",
        "explanation": "<p><strong>has</strong> is correct — <em>everyone</em> is singular however large "
                       "the group is.<br><br>"
                       "<em>(<strong>has</strong> toʻgʻri — guruh qanchalik katta boʻlmasin, "
                       "<em>everyone</em> birlikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Neither Javohir nor his brothers ___ at home.</strong></p>",
        "choices": ["are", "is", "was", "has been"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct — with <em>neither … nor</em> the verb agrees "
                       "with the <em>nearest</em> subject, and <em>brothers</em> is plural.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri — <em>neither … nor</em> bilan feʼl "
                       "<em>eng yaqin</em> subjectga mos keladi, <em>brothers</em> esa koʻplikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Either the pupils or Madina ___ going to answer.</strong></p>",
        "choices": ["is", "are", "were", "have been"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — the same nearest-subject rule, and "
                       "<em>Madina</em> is singular.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — xuddi shu eng yaqin subject qoidasi, "
                       "<em>Madina</em> esa birlikda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The number of pupils in our school ___ growing.</strong></p>",
        "choices": ["is", "are", "were", "have been"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — <em>the number of</em> is singular; <em>a "
                       "number of</em> would be plural.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — <em>the number of</em> birlikda; <em>a number "
                       "of</em> esa koʻplikda boʻlardi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>A number of pupils ___ absent today.</strong></p>",
        "choices": ["are", "is", "was", "has been"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct — <em>a number of</em> simply means “several”, "
                       "so it is plural.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri — <em>a number of</em> shunchaki “bir necha” "
                       "degani, yaʼni koʻplik.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["The list of names are on the desk.", "The list of names is on the desk.",
                    "The names are on the list.", "The lists of names are on the desk."],
        "correct": "The list of names are on the desk.",
        "explanation": "<p><strong>The list of names are on the desk.</strong> is the mistake — the head "
                       "noun is <em>list</em>, and the ear was fooled by <em>names</em>.<br><br>"
                       "<em>(<strong>The list of names are on the desk.</strong> xato — asosiy ot "
                       "<em>list</em>, quloq esa <em>names</em> ga aldangan.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Physics is difficult but interesting.",
                    "Physics are difficult but interesting.",
                    "Physic is difficult but interesting.",
                    "The physics are difficult but interesting."],
        "correct": "Physics is difficult but interesting.",
        "explanation": "<p><strong>Physics is difficult but interesting.</strong> is correct — an "
                       "<em>-ics</em> subject with a singular verb.<br><br>"
                       "<em>(<strong>Physics is difficult but interesting.</strong> toʻgʻri — "
                       "<em>-ics</em> bilan tugagan fan va birlikdagi feʼl.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Where are the exercise books?</p>"
                "<p><strong>Sirojiddin:</strong> ___</p>",
        "choices": ["The pile of books is on your desk.", "The pile of books are on your desk.",
                    "The pile of book are on your desk.", "The piles of books is on your desk."],
        "correct": "The pile of books is on your desk.",
        "explanation": "<p><strong>The pile of books is on your desk.</strong> is correct — one pile, so "
                       "one verb.<br><br>"
                       "<em>(<strong>The pile of books is on your desk.</strong> toʻgʻri — bitta uyum, "
                       "shuning uchun birlikdagi feʼl.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> verb agrees.</p>",
        "choices": ["The news is good, mathematics is hard, and these scissors are new.",
                    "The news are good, mathematics are hard, and these scissors is new.",
                    "The news is good, mathematics are hard, and this scissors are new.",
                    "The news are good, mathematics is hard, and these scissors is new."],
        "correct": "The news is good, mathematics is hard, and these scissors are new.",
        "explanation": "<p><strong>news is … mathematics is … scissors are</strong> is correct — two "
                       "words that look plural but aren't, and one that really is.<br><br>"
                       "<em>(<strong>news is … mathematics is … scissors are</strong> toʻgʻri — "
                       "koʻplikka oʻxshab koʻringan ikki soʻz va haqiqatan koʻplikdagi bittasi.)</em></p>",
    },
]


# =====================================================================
# PE-75 — Possession
# =====================================================================

Q_PE75 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>This is ___ book. (one boy)</strong></p>",
        "choices": ["the boy's", "the boys'", "the boys", "the boy"],
        "correct": "the boy's",
        "explanation": "<p><strong>the boy's</strong> is correct — a singular owner takes "
                       "<em>'s</em>.<br><br>"
                       "<em>(<strong>the boy's</strong> toʻgʻri — birlikdagi ega <em>'s</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>These are ___ books. (several boys)</strong></p>",
        "choices": ["the boys'", "the boy's", "the boys's", "the boys"],
        "correct": "the boys'",
        "explanation": "<p><strong>the boys'</strong> is correct — a plural already ending in <em>-s</em> "
                       "takes only the apostrophe.<br><br>"
                       "<em>(<strong>the boys'</strong> toʻgʻri — <em>-s</em> bilan tugagan koʻplik faqat "
                       "apostrof oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The ___ toys are in the box.</strong></p>",
        "choices": ["children's", "childrens'", "childrens", "children"],
        "correct": "children's",
        "explanation": "<p><strong>children's</strong> is correct — an irregular plural does not end in "
                       "<em>-s</em>, so it takes the full <em>'s</em>.<br><br>"
                       "<em>(<strong>children's</strong> toʻgʻri — notoʻgʻri koʻplik <em>-s</em> bilan "
                       "tugamaydi, shuning uchun toʻliq <em>'s</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference between “my sister's room” and “my sisters' "
                "rooms”?</strong></p>",
        "choices": ["one sister vs several sisters", "one room vs several rooms",
                    "there is no difference", "present vs past"],
        "correct": "one sister vs several sisters",
        "explanation": "<p><strong>one sister vs several sisters</strong> is correct — the apostrophe's "
                       "position tells you how many owners there are.<br><br>"
                       "<em>(<strong>bitta opa va bir nechta opa</strong> toʻgʻri — apostrofning oʻrni "
                       "nechta ega borligini bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda and Charos ___ house is near the school. (they share it)</strong></p>",
        "choices": ["'s", "s'", "'s ... 's", "of"],
        "correct": "'s",
        "explanation": "<p><strong>'s</strong> is correct — when two people own something together, only "
                       "the last name takes the <em>'s</em>.<br><br>"
                       "<em>(<strong>'s</strong> toʻgʻri — ikki kishi bir narsaga birga egalik qilsa, "
                       "faqat oxirgi ism <em>'s</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which is better English?</strong></p>",
        "choices": ["the leg of the table", "the table's leg",
                    "the table leg's", "the legs' table"],
        "correct": "the leg of the table",
        "explanation": "<p><strong>the leg of the table</strong> is correct — <em>of</em> is preferred "
                       "for things, <em>'s</em> for people and animals.<br><br>"
                       "<em>(<strong>the leg of the table</strong> toʻgʻri — narsalar uchun <em>of</em>, "
                       "odam va hayvonlar uchun esa <em>'s</em> afzal.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz is at ___ — he has toothache.</strong></p>",
        "choices": ["the dentist's", "the dentist", "the dentists'", "the dentist of"],
        "correct": "the dentist's",
        "explanation": "<p><strong>the dentist's</strong> is correct — the shop-and-home shortcut: "
                       "<em>the dentist's (surgery)</em>, <em>the baker's (shop)</em>.<br><br>"
                       "<em>(<strong>the dentist's</strong> toʻgʻri — “doʻkon va uy” qisqartmasi: "
                       "<em>the dentist's (surgery)</em>, <em>the baker's (shop)</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We had dinner at ___ last night.</strong></p>",
        "choices": ["Samandar's", "Samandar", "Samandars'", "the Samandar's of"],
        "correct": "Samandar's",
        "explanation": "<p><strong>Samandar's</strong> is correct — <em>at somebody's</em> means at their "
                       "house.<br><br>"
                       "<em>(<strong>Samandar's</strong> toʻgʻri — <em>at somebody's</em> ularning uyida "
                       "degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which is correct for a name ending in -s?</strong></p>",
        "choices": ["Both James's car and James' car", "Only Jameses car",
                    "Only James car", "Only James's cars"],
        "correct": "Both James's car and James' car",
        "explanation": "<p><strong>Both James's car and James' car</strong> is correct — English accepts "
                       "either form.<br><br>"
                       "<em>(<strong>James's car ham, James' car ham</strong> toʻgʻri — ingliz tili ikki "
                       "shaklni ham qabul qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek borrowed ___ notes.</strong></p>",
        "choices": ["Firdavs's", "Firdavs", "Firdavs of", "Firdavs'es"],
        "correct": "Firdavs's",
        "explanation": "<p><strong>Firdavs's</strong> is correct — one owner, so <em>'s</em>. "
                       "<em>Firdavs'</em> would also be acceptable.<br><br>"
                       "<em>(<strong>Firdavs's</strong> toʻgʻri — bitta ega, shuning uchun <em>'s</em>. "
                       "<em>Firdavs'</em> ham qabul qilinadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the biggest apostrophe trap?</strong></p>",
        "choices": ["Using an apostrophe to make a plural.",
                    "Using 's for people.",
                    "Using of for things.",
                    "Writing children's."],
        "correct": "Using an apostrophe to make a plural.",
        "explanation": "<p><strong>Using an apostrophe to make a plural.</strong> is correct — "
                       "<em>photo's</em> for several photos is wrong, and even native speakers do "
                       "it.<br><br>"
                       "<em>(<strong>Koʻplik yasash uchun apostrof ishlatish.</strong> toʻgʻri — bir "
                       "necha rasm uchun <em>photo's</em> xato, buni hatto ingliz tili egalari ham "
                       "qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir took twenty ___ at the wedding.</strong></p>",
        "choices": ["photos", "photo's", "photos'", "photoes"],
        "correct": "photos",
        "explanation": "<p><strong>photos</strong> is correct — a plain plural never takes an "
                       "apostrophe.<br><br>"
                       "<em>(<strong>photos</strong> toʻgʻri — oddiy koʻplik hech qachon apostrof "
                       "olmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina is ___ best friend.</strong></p>",
        "choices": ["Shaxzoda's", "Shaxzodas", "Shaxzodas'", "of Shaxzoda"],
        "correct": "Shaxzoda's",
        "explanation": "<p><strong>Shaxzoda's</strong> is correct — a person, so <em>'s</em>, not "
                       "<em>of</em>.<br><br>"
                       "<em>(<strong>Shaxzoda's</strong> toʻgʻri — shaxs, shuning uchun <em>of</em> emas, "
                       "<em>'s</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh cleaned the ___ windows.</strong></p>",
        "choices": ["classroom", "classroom's", "classrooms'", "classrooms"],
        "correct": "classroom",
        "explanation": "<p><strong>classroom</strong> is correct — English often just puts one noun in "
                       "front of another: <em>classroom windows, car keys, school bag</em>.<br><br>"
                       "<em>(<strong>classroom</strong> toʻgʻri — ingliz tili koʻpincha bir otni "
                       "ikkinchisining oldiga qoʻyadi: <em>classroom windows, car keys, school "
                       "bag</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin is a friend ___ .</strong></p>",
        "choices": ["of mine", "of me", "of my", "of I"],
        "correct": "of mine",
        "explanation": "<p><strong>of mine</strong> is correct — the double possessive uses a possessive "
                       "pronoun: <em>a friend of mine, a cousin of hers</em>.<br><br>"
                       "<em>(<strong>of mine</strong> toʻgʻri — qoʻsh egalik possessive pronoun oladi: "
                       "<em>a friend of mine, a cousin of hers</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Today is Rozimurod ___ birthday.</strong></p>",
        "choices": ["teacher's", "teachers'", "teachers", "teacher"],
        "correct": "teacher's",
        "explanation": "<p><strong>teacher's</strong> is correct — one person, so the apostrophe goes "
                       "before the <em>s</em>.<br><br>"
                       "<em>(<strong>teacher's</strong> toʻgʻri — bitta shaxs, shuning uchun apostrof "
                       "<em>s</em> dan oldin qoʻyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>___ room is small, but ___ rooms are both big.</strong></p>",
        "choices": ["My sister's … my sisters'", "My sisters' … my sister's",
                    "My sisters … my sister's", "My sister's … my sisters"],
        "correct": "My sister's … my sisters'",
        "explanation": "<p><strong>My sister's … my sisters'</strong> is correct — one sister first, "
                       "several after.<br><br>"
                       "<em>(<strong>My sister's … my sisters'</strong> toʻgʻri — avval bitta opa, keyin "
                       "bir nechtasi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["The girl's are waiting outside.", "The girls are waiting outside.",
                    "The girl's bag is on the desk.", "The girls' bags are on the desk."],
        "correct": "The girl's are waiting outside.",
        "explanation": "<p><strong>The girl's are waiting outside.</strong> is the mistake — the plural "
                       "of <em>girl</em> is simply <em>girls</em>, with no apostrophe.<br><br>"
                       "<em>(<strong>The girl's are waiting outside.</strong> xato — <em>girl</em> ning "
                       "koʻpligi apostrofsiz shunchaki <em>girls</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Marjona is going to the baker's.", "Marjona is going to the bakers.",
                    "Marjona is going to the bakers's.", "Marjona is going to baker of."],
        "correct": "Marjona is going to the baker's.",
        "explanation": "<p><strong>Marjona is going to the baker's.</strong> is correct — the shop "
                       "shortcut, with the word <em>shop</em> understood.<br><br>"
                       "<em>(<strong>Marjona is going to the baker's.</strong> toʻgʻri — doʻkon "
                       "qisqartmasi, <em>shop</em> soʻzi tushunib olinadi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> apostrophe is correct.</p>",
        "choices": ["The children's books are on my sister's desk, "
                    "and the teachers' room is upstairs.",
                    "The childrens' books are on my sisters desk, "
                    "and the teacher's room's are upstairs.",
                    "The children's book's are on my sisters' desk, "
                    "and the teachers room is upstairs.",
                    "The childrens books are on my sister's desk, "
                    "and the teachers's room is upstairs."],
        "correct": "The children's books are on my sister's desk, "
                   "and the teachers' room is upstairs.",
        "explanation": "<p><strong>children's … sister's … teachers'</strong> is correct — an irregular "
                       "plural, a singular owner, and a plural already ending in <em>-s</em>.<br><br>"
                       "<em>(<strong>children's … sister's … teachers'</strong> toʻgʻri — notoʻgʻri "
                       "koʻplik, birlikdagi ega va <em>-s</em> bilan tugagan koʻplik.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-71 Practice: Determiners: each, every, both, either, neither, all",
        "tutorial":    "PE-71:",
        "description": "PE-71 darsiga 20 savol: every va each farqi, aynan ikkitasi uchun both / "
                       "either / neither, all va none, hamda qaysilari birlikdagi feʼl olishi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE71,
    },
    {
        "title":       "PE-72 Practice: Word Order in English: SVOMPT",
        "tutorial":    "PE-72:",
        "description": "PE-72 darsiga 20 savol: Subject–Verb–Object–Manner–Place–Time zanjiri, feʼl "
                       "bilan toʻldiruvchi orasiga hech narsa qoʻyilmasligi va give somebody "
                       "something ning ikki qolipi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE72,
    },
    {
        "title":       "PE-73 Practice: Question Tags",
        "tutorial":    "PE-73:",
        "description": "PE-73 darsiga 20 savol: belgini almashtirish va yordamchini takrorlash "
                       "qoidasi, yordamchi boʻlmagan holatlar, I am / Let's / buyruq / there is "
                       "istisnolari va ohangning maʼnosi. Javoblar ingliz va oʻzbek tilida "
                       "izohlangan.",
        "questions":   Q_PE73,
    },
    {
        "title":       "PE-74 Practice: Subject–Verb Agreement",
        "tutorial":    "PE-74:",
        "description": "PE-74 darsiga 20 savol: uzun gapda asosiy otni topish, and / with / as well "
                       "as farqi, koʻplikka oʻxshagan birlik otlar va pul, vaqt, masofa miqdorlari. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE74,
    },
    {
        "title":       "PE-75 Practice: Possession: 's, s' and of",
        "tutorial":    "PE-75:",
        "description": "PE-75 darsiga 20 savol: apostrof qayerga qoʻyilishi ('s yoki s'), of qachon "
                       "ishlatilishi, at the doctor's qisqartmasi va koʻplik yasashda apostrof "
                       "qoʻyish tuzogʻi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE75,
    },
]
