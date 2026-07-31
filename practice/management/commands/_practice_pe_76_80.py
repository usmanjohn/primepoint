# -*- coding: utf-8 -*-
"""Prime English practices — PE-76 … PE-80 (Block F continued).

Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_76_80.py --master=prime --expect-questions=20
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
# PE-76 — Dependent Prepositions
# =====================================================================

Q_PE76 = [
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Iroda is very good ___ mathematics.</strong></p>",
        "choices": ["at", "in", "on", "for"],
        "correct": "at",
        "explanation": "<p><strong>at</strong> is correct — <em>good / bad / brilliant / terrible at</em> "
                       "is a fixed pair.<br><br>"
                       "<em>(<strong>at</strong> toʻgʻri — <em>good / bad / brilliant / terrible at</em> "
                       "qatʼiy juftlik.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Behruz is interested ___ history.</strong></p>",
        "choices": ["in", "at", "for", "about"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct — <em>interested in</em>, even though "
                       "<em>good at</em>. There is no logic; learn the pair.<br><br>"
                       "<em>(<strong>in</strong> toʻgʻri — <em>good at</em> boʻlsa ham, <em>interested "
                       "in</em>. Mantiq yoʻq; juftlikni yodlang.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Charos is afraid ___ dogs.</strong></p>",
        "choices": ["of", "from", "at", "with"],
        "correct": "of",
        "explanation": "<p><strong>of</strong> is correct — <em>afraid / proud / full / tired / aware "
                       "of</em>.<br><br>"
                       "<em>(<strong>of</strong> toʻgʻri — <em>afraid / proud / full / tired / aware "
                       "of</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Samandar is worried ___ the exam.</strong></p>",
        "choices": ["about", "for", "of", "on"],
        "correct": "about",
        "explanation": "<p><strong>about</strong> is correct — <em>worried / excited / sorry / angry "
                       "about</em>.<br><br>"
                       "<em>(<strong>about</strong> toʻgʻri — <em>worried / excited / sorry / angry "
                       "about</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Bukhara is famous ___ its old buildings.</strong></p>",
        "choices": ["for", "of", "with", "about"],
        "correct": "for",
        "explanation": "<p><strong>for</strong> is correct — <em>famous / late / ready / sorry "
                       "for</em>.<br><br>"
                       "<em>(<strong>for</strong> toʻgʻri — <em>famous / late / ready / sorry "
                       "for</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Elbek's grandmother is very proud ___ him.</strong></p>",
        "choices": ["of", "for", "about", "with"],
        "correct": "of",
        "explanation": "<p><strong>of</strong> is correct — <em>proud of</em> somebody or something."
                       "<br><br><em>(<strong>of</strong> toʻgʻri — kimdir yoki nimadir bilan "
                       "<em>proud of</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Everything depends ___ the weather.</strong></p>",
        "choices": ["on", "of", "from", "in"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct — <em>depend on</em>, never <em>depend "
                       "from</em>.<br><br>"
                       "<em>(<strong>on</strong> toʻgʻri — <em>depend on</em>, <em>depend from</em> "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Firdavs is listening ___ music.</strong></p>",
        "choices": ["to", "—", "at", "of"],
        "correct": "to",
        "explanation": "<p><strong>to</strong> is correct — <em>listen to</em> always keeps its "
                       "<em>to</em>, unlike <em>hear</em>.<br><br>"
                       "<em>(<strong>to</strong> toʻgʻri — <em>hear</em> dan farqli oʻlaroq, <em>listen "
                       "to</em> doim <em>to</em> ni saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We discussed ___ the problem for an hour.</strong></p>",
        "choices": ["— (no preposition)", "about", "on", "of"],
        "correct": "— (no preposition)",
        "explanation": "<p><strong>— (no preposition)</strong> is correct — <em>discuss</em> takes a "
                       "direct object. <em>Discuss about</em> is a classic Uzbek-speaker mistake."
                       "<br><br><em>(<strong>Predlogsiz</strong> toʻgʻri — <em>discuss</em> "
                       "toʻgʻridan toʻgʻri toʻldiruvchi oladi. <em>Discuss about</em> — oʻzbek tilida "
                       "soʻzlashuvchilarning klassik xatosi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir ___ his little brother every evening.</strong></p>",
        "choices": ["helps", "helps to", "helps for", "helps at"],
        "correct": "helps",
        "explanation": "<p><strong>helps</strong> is correct — <em>help somebody</em> needs no "
                       "preposition either.<br><br>"
                       "<em>(<strong>helps</strong> toʻgʻri — <em>help somebody</em> ga ham predlog kerak "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Madina is waiting ___ the bus.</strong></p>",
        "choices": ["for", "to", "on", "at"],
        "correct": "for",
        "explanation": "<p><strong>for</strong> is correct — <em>wait for</em>, always.<br><br>"
                       "<em>(<strong>for</strong> toʻgʻri — doim <em>wait for</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Shaxzoda apologised ___ being late.</strong></p>",
        "choices": ["for", "of", "about to", "from"],
        "correct": "for",
        "explanation": "<p><strong>for</strong> is correct — <em>apologise for</em>, and note that "
                       "<em>-ing</em> follows the preposition.<br><br>"
                       "<em>(<strong>for</strong> toʻgʻri — <em>apologise for</em>, va predlogdan keyin "
                       "<em>-ing</em> kelishiga eʼtibor bering.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh is thinking about ___ a new dictionary.</strong></p>",
        "choices": ["buying", "to buy", "buy", "buys"],
        "correct": "buying",
        "explanation": "<p><strong>buying</strong> is correct — after any preposition the verb must take "
                       "<em>-ing</em>, the rule from PE-64 that never fails.<br><br>"
                       "<em>(<strong>buying</strong> toʻgʻri — har qanday predlogdan keyin feʼl "
                       "<em>-ing</em> oladi — PE-64 dagi hech qachon buzilmaydigan qoida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Sirojiddin is looking ___ his keys — he can't find them.</strong></p>",
        "choices": ["for", "at", "after", "to"],
        "correct": "for",
        "explanation": "<p><strong>for</strong> is correct — <em>look for</em> = search. <em>Look "
                       "after</em> = take care of, <em>look at</em> = direct your eyes.<br><br>"
                       "<em>(<strong>for</strong> toʻgʻri — <em>look for</em> = qidirmoq. <em>Look "
                       "after</em> = qaramoq, <em>look at</em> = koʻz tikmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Rozimurod teacher explained the rule ___ us.</strong></p>",
        "choices": ["to", "for", "—", "at"],
        "correct": "to",
        "explanation": "<p><strong>to</strong> is correct — <em>explain something to somebody</em>, never "
                       "<em>explain us</em>.<br><br>"
                       "<em>(<strong>to</strong> toʻgʻri — <em>explain something to somebody</em>, "
                       "<em>explain us</em> emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which verb takes <em>no</em> preposition?</strong></p>",
        "choices": ["enter", "listen", "wait", "depend"],
        "correct": "enter",
        "explanation": "<p><strong>enter</strong> is correct — <em>enter the room</em>, not <em>enter "
                       "into the room</em>. Same for <em>marry, phone, answer</em>.<br><br>"
                       "<em>(<strong>enter</strong> toʻgʻri — <em>enter into the room</em> emas, "
                       "<em>enter the room</em>. <em>Marry, phone, answer</em> ham shunday.)</em></p>",
    },
    {
        "text": "<p>Choose the correct preposition.</p>"
                "<p><strong>Marjona is married ___ a doctor.</strong></p>",
        "choices": ["to", "with", "on", "for"],
        "correct": "to",
        "explanation": "<p><strong>to</strong> is correct — the adjective <em>married to</em> keeps a "
                       "preposition, even though the verb <em>marry somebody</em> does not.<br><br>"
                       "<em>(<strong>to</strong> toʻgʻri — <em>marry somebody</em> feʼli predlog olmasa "
                       "ham, <em>married to</em> sifati uni saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["We discussed about the plan yesterday.",
                    "We discussed the plan yesterday.",
                    "We talked about the plan yesterday.",
                    "We spoke about the plan yesterday."],
        "correct": "We discussed about the plan yesterday.",
        "explanation": "<p><strong>We discussed about the plan yesterday.</strong> is the mistake — "
                       "<em>discuss</em> takes no preposition, though <em>talk about</em> and <em>speak "
                       "about</em> do.<br><br>"
                       "<em>(<strong>We discussed about the plan yesterday.</strong> xato — "
                       "<em>discuss</em> predlog olmaydi, <em>talk about</em> va <em>speak about</em> esa "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Davron is good at drawing and interested in art.",
                    "Davron is good in drawing and interested at art.",
                    "Davron is good at draw and interested in to draw.",
                    "Davron is good on drawing and interested for art."],
        "correct": "Davron is good at drawing and interested in art.",
        "explanation": "<p><strong>good at drawing … interested in art</strong> is correct — the right "
                       "pairs, and <em>-ing</em> after the preposition.<br><br>"
                       "<em>(<strong>good at drawing … interested in art</strong> toʻgʻri — toʻgʻri "
                       "juftliklar va predlogdan keyin <em>-ing</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Why are you so quiet today, Afsona?</p>"
                "<p><strong>Afsona:</strong> ___</p>",
        "choices": ["I'm worried about tomorrow's test.", "I'm worried for tomorrow's test.",
                    "I'm worried of tomorrow's test.", "I'm worried at tomorrow's test."],
        "correct": "I'm worried about tomorrow's test.",
        "explanation": "<p><strong>I'm worried about tomorrow's test.</strong> is correct — "
                       "<em>worried about</em> is the fixed pair.<br><br>"
                       "<em>(<strong>I'm worried about tomorrow's test.</strong> toʻgʻri — "
                       "<em>worried about</em> qatʼiy juftlik.)</em></p>",
    },
]


# =====================================================================
# PE-77 — Phrasal Verbs: How They Work
# =====================================================================

Q_PE77 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is a phrasal verb?</strong></p>",
        "choices": ["a verb + a particle, with a new meaning",
                    "a very long verb",
                    "a verb in the past tense",
                    "two verbs together"],
        "correct": "a verb + a particle, with a new meaning",
        "explanation": "<p><strong>a verb + a particle, with a new meaning</strong> is correct — "
                       "<em>get</em> + <em>up / on / over</em> gives three different verbs.<br><br>"
                       "<em>(<strong>feʼl + zarracha, yangi maʼno bilan</strong> toʻgʻri — <em>get</em> + "
                       "<em>up / on / over</em> uchta boshqa feʼl beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct meaning.</p>"
                "<p><strong>Iroda looked up the word in the dictionary.</strong></p>",
        "choices": ["She searched for it.", "She raised her eyes.",
                    "She wrote it down.", "She forgot it."],
        "correct": "She searched for it.",
        "explanation": "<p><strong>She searched for it.</strong> is correct — the idiomatic meaning. "
                       "<em>She looked up at the sky</em> would be the literal one.<br><br>"
                       "<em>(<strong>U uni qidirdi.</strong> toʻgʻri — bu idiomatik maʼno. <em>She looked "
                       "up at the sky</em> esa soʻzma-soʻz maʼno boʻlardi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct particle.</p>"
                "<p><strong>Behruz gets ___ at six every morning.</strong></p>",
        "choices": ["up", "on", "over", "off"],
        "correct": "up",
        "explanation": "<p><strong>up</strong> is correct — <em>get up</em> = leave your bed.<br><br>"
                       "<em>(<strong>up</strong> toʻgʻri — <em>get up</em> = oʻrindan turmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct particle.</p>"
                "<p><strong>Charos got ___ the bus at the last stop.</strong></p>",
        "choices": ["on", "up", "over", "in"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct — <em>get on</em> a bus, train or plane; "
                       "<em>get in</em> a car.<br><br>"
                       "<em>(<strong>on</strong> toʻgʻri — avtobus, poyezd va samolyotga <em>get on</em>; "
                       "mashinaga esa <em>get in</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct meaning.</p>"
                "<p><strong>Samandar has got over his illness.</strong></p>",
        "choices": ["He has recovered.", "He has caught it.",
                    "He has climbed something.", "He has forgotten it."],
        "correct": "He has recovered.",
        "explanation": "<p><strong>He has recovered.</strong> is correct — <em>get over</em> = recover "
                       "from.<br><br>"
                       "<em>(<strong>U tuzalib ketdi.</strong> toʻgʻri — <em>get over</em> = "
                       "tuzalmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is correct with a pronoun object?</strong></p>",
        "choices": ["Turn it off.", "Turn off it.", "Turn off's it.", "It turn off."],
        "correct": "Turn it off.",
        "explanation": "<p><strong>Turn it off.</strong> is correct — the pronoun rule: a pronoun object "
                       "must go <em>between</em> the verb and the particle.<br><br>"
                       "<em>(<strong>Turn it off.</strong> toʻgʻri — olmosh qoidasi: olmosh toʻldiruvchi "
                       "feʼl bilan zarracha <em>orasiga</em> qoʻyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek took ___ his coat because the room was warm.</strong></p>",
        "choices": ["off", "up", "on", "over"],
        "correct": "off",
        "explanation": "<p><strong>off</strong> is correct — <em>take off</em> = remove, the opposite of "
                       "<em>put on</em>.<br><br>"
                       "<em>(<strong>off</strong> toʻgʻri — <em>take off</em> = yechmoq, <em>put on</em> "
                       "ning aksi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which of these can be separated?</strong></p>",
        "choices": ["turn on the light → turn the light on",
                    "look after the baby → look the baby after",
                    "get on the bus → get the bus on",
                    "look for the keys → look the keys for"],
        "correct": "turn on the light → turn the light on",
        "explanation": "<p><strong>turn on the light → turn the light on</strong> is correct — some "
                       "phrasal verbs split, others never do.<br><br>"
                       "<em>(<strong>turn on the light → turn the light on</strong> toʻgʻri — baʼzi "
                       "frazali feʼllar ajraladi, baʼzilari esa hech qachon.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs is looking after ___ while their parents are away.</strong></p>",
        "choices": ["his little sister", "her little sister after",
                    "after his little sister", "his little sister after"],
        "correct": "his little sister",
        "explanation": "<p><strong>his little sister</strong> is correct — <em>look after</em> can never "
                       "be split, not even by a pronoun.<br><br>"
                       "<em>(<strong>his little sister</strong> toʻgʻri — <em>look after</em> hech qachon, "
                       "hatto olmosh bilan ham ajralmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct meaning.</p>"
                "<p><strong>Javohir gets on well with his classmates.</strong></p>",
        "choices": ["He has a good relationship with them.",
                    "He boards a bus with them.",
                    "He is faster than them.",
                    "He argues with them."],
        "correct": "He has a good relationship with them.",
        "explanation": "<p><strong>He has a good relationship with them.</strong> is correct — <em>get on "
                       "with</em> takes three words and is never split.<br><br>"
                       "<em>(<strong>U ular bilan yaxshi til topishadi.</strong> toʻgʻri — <em>get on "
                       "with</em> uch soʻzdan iborat va hech qachon ajralmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct particle.</p>"
                "<p><strong>Madina gave ___ smoking two years ago.</strong></p>",
        "choices": ["up", "in", "off", "away"],
        "correct": "up",
        "explanation": "<p><strong>up</strong> is correct — <em>give up</em> = stop doing something, and "
                       "an <em>-ing</em> form follows.<br><br>"
                       "<em>(<strong>up</strong> toʻgʻri — <em>give up</em> = tashlamoq, undan keyin esa "
                       "<em>-ing</em> shakli keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda tried ___ the dress before buying it.</strong></p>",
        "choices": ["on", "up", "over", "in"],
        "correct": "on",
        "explanation": "<p><strong>on</strong> is correct — <em>try on</em> clothes. It splits too: "
                       "<em>try it on</em>.<br><br>"
                       "<em>(<strong>on</strong> toʻgʻri — kiyimni <em>try on</em> qilinadi. U "
                       "ajraladi ham: <em>try it on</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher told us to write ___ the new words.</strong></p>",
        "choices": ["down", "up", "off", "in"],
        "correct": "down",
        "explanation": "<p><strong>down</strong> is correct — <em>write down</em> = record on paper. "
                       "<em>Write them down</em> with a pronoun.<br><br>"
                       "<em>(<strong>down</strong> toʻgʻri — <em>write down</em> = qogʻozga yozib olmoq. "
                       "Olmosh bilan: <em>write them down</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh, please turn ___ ! I can't hear the news.</strong></p>",
        "choices": ["it up", "up it", "it on up", "up it on"],
        "correct": "it up",
        "explanation": "<p><strong>it up</strong> is correct — the pronoun goes in the middle, "
                       "always.<br><br>"
                       "<em>(<strong>it up</strong> toʻgʻri — olmosh doim oʻrtaga qoʻyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the best way to learn phrasal verbs?</strong></p>",
        "choices": ["in groups by particle or topic", "in alphabetical order",
                    "one hundred at a time", "by translating each word separately"],
        "correct": "in groups by particle or topic",
        "explanation": "<p><strong>in groups by particle or topic</strong> is correct — the particle "
                       "often carries a shared idea: <em>up</em> = completely, <em>off</em> = away."
                       "<br><br><em>(<strong>zarracha yoki mavzu boʻyicha guruhlab</strong> toʻgʻri — "
                       "zarracha koʻpincha umumiy gʻoyani tashiydi: <em>up</em> = butunlay, <em>off</em> "
                       "= uzoqlashish.)</em></p>",
    },
    {
        "text": "<p>Choose the correct particle.</p>"
                "<p><strong>Sirojiddin ran ___ of money before the end of the trip.</strong></p>",
        "choices": ["out", "off", "away", "over"],
        "correct": "out",
        "explanation": "<p><strong>out</strong> is correct — <em>run out of</em> = have none left."
                       "<br><br><em>(<strong>out</strong> toʻgʻri — <em>run out of</em> = tugab "
                       "qolmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The plane took ___ exactly on time.</strong></p>",
        "choices": ["off", "up", "on", "out"],
        "correct": "off",
        "explanation": "<p><strong>off</strong> is correct — <em>take off</em> also means to leave the "
                       "ground. Same words, another meaning.<br><br>"
                       "<em>(<strong>off</strong> toʻgʻri — <em>take off</em> “uchib ketmoq” maʼnosini "
                       "ham beradi. Oʻsha soʻzlar, boshqa maʼno.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Turn off it, please.", "Turn it off, please.",
                    "Turn off the light, please.", "Turn the light off, please."],
        "correct": "Turn off it, please.",
        "explanation": "<p><strong>Turn off it, please.</strong> is the mistake — a pronoun can never "
                       "follow the particle.<br><br>"
                       "<em>(<strong>Turn off it, please.</strong> xato — olmosh hech qachon zarrachadan "
                       "keyin kelmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Marjona looks after her grandmother every weekend.",
                    "Marjona looks her grandmother after every weekend.",
                    "Marjona looks after she every weekend.",
                    "Marjona after looks her grandmother every weekend."],
        "correct": "Marjona looks after her grandmother every weekend.",
        "explanation": "<p><strong>Marjona looks after her grandmother every weekend.</strong> is correct "
                       "— <em>look after</em> stays together, and the object follows it.<br><br>"
                       "<em>(<strong>Marjona looks after her grandmother every weekend.</strong> "
                       "toʻgʻri — <em>look after</em> birga qoladi, toʻldiruvchi esa undan keyin "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Davron:</strong> I don't know this word.</p>"
                "<p><strong>Iroda:</strong> ___</p>",
        "choices": ["Look it up in the dictionary.", "Look up it in the dictionary.",
                    "Look after it in the dictionary.", "Look for up it in the dictionary."],
        "correct": "Look it up in the dictionary.",
        "explanation": "<p><strong>Look it up in the dictionary.</strong> is correct — the pronoun rule "
                       "in action.<br><br>"
                       "<em>(<strong>Look it up in the dictionary.</strong> toʻgʻri — olmosh qoidasi "
                       "amalda.)</em></p>",
    },
]


# =====================================================================
# PE-78 — 40 Everyday Phrasal Verbs
# =====================================================================

Q_PE78 = [
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Behruz ___ at six every morning, then gets up slowly.</strong></p>",
        "choices": ["wakes up", "takes off", "gives up", "puts on"],
        "correct": "wakes up",
        "explanation": "<p><strong>wakes up</strong> is correct — <em>wake up</em> = stop sleeping; "
                       "<em>get up</em> = leave the bed.<br><br>"
                       "<em>(<strong>wakes up</strong> toʻgʻri — <em>wake up</em> = uygʻonmoq; <em>get "
                       "up</em> = oʻrindan turmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>It's cold outside — ___ your coat.</strong></p>",
        "choices": ["put on", "take off", "look up", "give up"],
        "correct": "put on",
        "explanation": "<p><strong>put on</strong> is correct — <em>put on</em> clothes, <em>take "
                       "off</em> to remove them.<br><br>"
                       "<em>(<strong>put on</strong> toʻgʻri — kiyimni <em>put on</em> qilinadi, yechish "
                       "esa <em>take off</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Rozimurod teacher asked us to ___ our rooms before the "
                "inspection.</strong></p>",
        "choices": ["tidy up", "look after", "get over", "hand in"],
        "correct": "tidy up",
        "explanation": "<p><strong>tidy up</strong> is correct — <em>tidy up</em> = put in order."
                       "<br><br><em>(<strong>tidy up</strong> toʻgʻri — <em>tidy up</em> = tartibga "
                       "solmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Please ___ your projects on Friday.</strong></p>",
        "choices": ["hand in", "hand out", "take up", "put off"],
        "correct": "hand in",
        "explanation": "<p><strong>hand in</strong> is correct — <em>hand in</em> = give to the teacher; "
                       "<em>hand out</em> = distribute to everybody.<br><br>"
                       "<em>(<strong>hand in</strong> toʻgʻri — <em>hand in</em> = oʻqituvchiga topshirmoq; "
                       "<em>hand out</em> = hammaga tarqatmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Charos wants to ___ the new words before the test.</strong></p>",
        "choices": ["go over", "get on", "put on", "take off"],
        "correct": "go over",
        "explanation": "<p><strong>go over</strong> is correct — <em>go over</em> = review, check "
                       "again.<br><br>"
                       "<em>(<strong>go over</strong> toʻgʻri — <em>go over</em> = qaytadan koʻrib "
                       "chiqmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Samandar ___ maths quickly — he's very clever.</strong></p>",
        "choices": ["picks up", "takes off", "gives in", "runs out"],
        "correct": "picks up",
        "explanation": "<p><strong>picks up</strong> is correct — <em>pick up</em> = learn something "
                       "easily, often without formal study.<br><br>"
                       "<em>(<strong>picks up</strong> toʻgʻri — <em>pick up</em> = biror narsani oson, "
                       "koʻpincha maxsus oʻqimasdan oʻrganmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Elbek ___ well with everybody in the class.</strong></p>",
        "choices": ["gets on", "gets up", "gets off", "gets over"],
        "correct": "gets on",
        "explanation": "<p><strong>gets on</strong> is correct — <em>get on with somebody</em> = have a "
                       "good relationship.<br><br>"
                       "<em>(<strong>gets on</strong> toʻgʻri — <em>get on with somebody</em> = yaxshi "
                       "til topishmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Firdavs and his cousin ___ over a game, but they're friends "
                "again.</strong></p>",
        "choices": ["fell out", "fell over", "took off", "put up"],
        "correct": "fell out",
        "explanation": "<p><strong>fell out</strong> is correct — <em>fall out</em> = quarrel. "
                       "<em>Fall over</em> means to trip and land on the ground.<br><br>"
                       "<em>(<strong>fell out</strong> toʻgʻri — <em>fall out</em> = janjallashmoq. "
                       "<em>Fall over</em> esa qoqilib yiqilmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Javohir ___ his father — they look exactly the same.</strong></p>",
        "choices": ["takes after", "takes off", "takes up", "takes in"],
        "correct": "takes after",
        "explanation": "<p><strong>takes after</strong> is correct — <em>take after</em> = resemble a "
                       "family member.<br><br>"
                       "<em>(<strong>takes after</strong> toʻgʻri — <em>take after</em> = oila aʼzosiga "
                       "oʻxshamoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>We had to ___ at five in the morning to catch the train.</strong></p>",
        "choices": ["set off", "set up", "put off", "take in"],
        "correct": "set off",
        "explanation": "<p><strong>set off</strong> is correct — <em>set off</em> = begin a journey."
                       "<br><br><em>(<strong>set off</strong> toʻgʻri — <em>set off</em> = safarga "
                       "chiqmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Madina ___ at the last stop and walked home.</strong></p>",
        "choices": ["got off", "got on", "got up", "got over"],
        "correct": "got off",
        "explanation": "<p><strong>got off</strong> is correct — <em>get off</em> a bus or train; the "
                       "opposite of <em>get on</em>.<br><br>"
                       "<em>(<strong>got off</strong> toʻgʻri — avtobus yoki poyezddan <em>get off</em>; "
                       "<em>get on</em> ning aksi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>The concert was ___ until next month because of the weather.</strong></p>",
        "choices": ["put off", "put on", "put up", "put down"],
        "correct": "put off",
        "explanation": "<p><strong>put off</strong> is correct — <em>put off</em> = postpone.<br><br>"
                       "<em>(<strong>put off</strong> toʻgʻri — <em>put off</em> = keyinga "
                       "qoldirmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Shaxzoda never ___ — she always finishes what she starts.</strong></p>",
        "choices": ["gives up", "gives out", "takes up", "puts on"],
        "correct": "gives up",
        "explanation": "<p><strong>gives up</strong> is correct — <em>give up</em> = stop trying."
                       "<br><br><em>(<strong>gives up</strong> toʻgʻri — <em>give up</em> = taslim "
                       "boʻlmoq, tashlab qoʻymoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Abdulloh ___ the problem after thinking for an hour.</strong></p>",
        "choices": ["worked out", "worked on out", "took out", "ran out"],
        "correct": "worked out",
        "explanation": "<p><strong>worked out</strong> is correct — <em>work out</em> = solve or "
                       "calculate.<br><br>"
                       "<em>(<strong>worked out</strong> toʻgʻri — <em>work out</em> = yechmoq yoki "
                       "hisoblab chiqmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Sirojiddin's phone rang, so he ___ .</strong></p>",
        "choices": ["picked it up", "picked up it", "took it after", "put it off"],
        "correct": "picked it up",
        "explanation": "<p><strong>picked it up</strong> is correct — <em>pick up</em> the phone, with "
                       "the pronoun in the middle.<br><br>"
                       "<em>(<strong>picked it up</strong> toʻgʻri — telefonni <em>pick up</em> qilinadi, "
                       "olmosh esa oʻrtada turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Sorry, the line is bad — I'll ___ later.</strong></p>",
        "choices": ["call you back", "call back you", "call you again back", "back call you"],
        "correct": "call you back",
        "explanation": "<p><strong>call you back</strong> is correct — the pronoun goes between the verb "
                       "and the particle.<br><br>"
                       "<em>(<strong>call you back</strong> toʻgʻri — olmosh feʼl bilan zarracha orasiga "
                       "qoʻyiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct phrasal verb.</p>"
                "<p><strong>Marjona ___ her little brother while her mother is at work.</strong></p>",
        "choices": ["looks after", "looks for", "looks up", "looks at"],
        "correct": "looks after",
        "explanation": "<p><strong>looks after</strong> is correct — <em>look after</em> = take care "
                       "of.<br><br>"
                       "<em>(<strong>looks after</strong> toʻgʻri — <em>look after</em> = "
                       "qaramoq.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Please hand in it tomorrow.", "Please hand it in tomorrow.",
                    "Please hand in your project tomorrow.",
                    "Please hand your project in tomorrow."],
        "correct": "Please hand in it tomorrow.",
        "explanation": "<p><strong>Please hand in it tomorrow.</strong> is the mistake — the pronoun "
                       "<em>it</em> must sit between the two parts.<br><br>"
                       "<em>(<strong>Please hand in it tomorrow.</strong> xato — <em>it</em> olmoshi ikki "
                       "qism orasida turishi kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Davron takes after his grandfather.", "Davron takes his grandfather after.",
                    "Davron takes off his grandfather.", "Davron takes after of his grandfather."],
        "correct": "Davron takes after his grandfather.",
        "explanation": "<p><strong>Davron takes after his grandfather.</strong> is correct — <em>take "
                       "after</em> never splits and needs no extra preposition.<br><br>"
                       "<em>(<strong>Davron takes after his grandfather.</strong> toʻgʻri — <em>take "
                       "after</em> ajralmaydi va qoʻshimcha predlog talab qilmaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> You've missed three lessons, Afsona.</p>"
                "<p><strong>Afsona:</strong> ___</p>",
        "choices": ["I know — I'll catch up at the weekend.",
                    "I know — I'll catch up on at the weekend it.",
                    "I know — I'll catch at the weekend up.",
                    "I know — I'll up catch at the weekend."],
        "correct": "I know — I'll catch up at the weekend.",
        "explanation": "<p><strong>I know — I'll catch up at the weekend.</strong> is correct — "
                       "<em>catch up</em> = reach the level of the others.<br><br>"
                       "<em>(<strong>I know — I'll catch up at the weekend.</strong> toʻgʻri — "
                       "<em>catch up</em> = boshqalarga yetib olmoq.)</em></p>",
    },
]


# =====================================================================
# PE-79 — Expressions of Quantity
# =====================================================================

Q_PE79 = [
    {
        "text": "<p>Choose the correct expression.</p>"
                "<p><strong>Behruz's mother bought two ___ of bread.</strong></p>",
        "choices": ["loaves", "slices'", "pieces of", "breads"],
        "correct": "loaves",
        "explanation": "<p><strong>loaves</strong> is correct — <em>a loaf of bread</em> is the whole "
                       "one; you count the container, not the uncountable noun.<br><br>"
                       "<em>(<strong>loaves</strong> toʻgʻri — <em>a loaf of bread</em> butun non; "
                       "sanalmaydigan otni emas, oʻlchovni sanaysiz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct expression.</p>"
                "<p><strong>Iroda ate a ___ of cake after dinner.</strong></p>",
        "choices": ["piece", "loaf", "bar", "sheet"],
        "correct": "piece",
        "explanation": "<p><strong>piece</strong> is correct — <em>a piece of cake / fruit / meat</em>."
                       "<br><br><em>(<strong>piece</strong> toʻgʻri — <em>a piece of cake / fruit / "
                       "meat</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct expression.</p>"
                "<p><strong>Charos cut a thin ___ of bread for her tea.</strong></p>",
        "choices": ["slice", "bar", "bottle", "packet"],
        "correct": "slice",
        "explanation": "<p><strong>slice</strong> is correct — a slice is a flat, cut piece: bread, "
                       "cheese, meat.<br><br>"
                       "<em>(<strong>slice</strong> toʻgʻri — tilim — kesilgan yassi boʻlak: non, "
                       "pishloq, goʻsht.)</em></p>",
    },
    {
        "text": "<p>Choose the correct expression.</p>"
                "<p><strong>Samandar drank two ___ of water after the match.</strong></p>",
        "choices": ["bottles", "loaves", "bars", "slices"],
        "correct": "bottles",
        "explanation": "<p><strong>bottles</strong> is correct — liquids are counted by their "
                       "container.<br><br>"
                       "<em>(<strong>bottles</strong> toʻgʻri — suyuqliklar idishi bilan "
                       "sanaladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct expression.</p>"
                "<p><strong>Elbek bought a ___ of chocolate at the shop.</strong></p>",
        "choices": ["bar", "slice", "loaf", "glass"],
        "correct": "bar",
        "explanation": "<p><strong>bar</strong> is correct — <em>a bar of chocolate / soap</em>."
                       "<br><br><em>(<strong>bar</strong> toʻgʻri — <em>a bar of chocolate / "
                       "soap</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct expression.</p>"
                "<p><strong>Rozimurod teacher gave each pupil a ___ of paper.</strong></p>",
        "choices": ["sheet", "bar", "loaf", "bottle"],
        "correct": "sheet",
        "explanation": "<p><strong>sheet</strong> is correct — <em>a sheet of paper</em>, or <em>a piece "
                       "of paper</em>.<br><br>"
                       "<em>(<strong>sheet</strong> toʻgʻri — <em>a sheet of paper</em> yoki <em>a piece "
                       "of paper</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct expression.</p>"
                "<p><strong>Firdavs needs a new ___ of trousers.</strong></p>",
        "choices": ["pair", "piece", "slice", "bar"],
        "correct": "pair",
        "explanation": "<p><strong>pair</strong> is correct — always-plural nouns are counted with <em>a "
                       "pair of</em>: trousers, scissors, glasses, shoes.<br><br>"
                       "<em>(<strong>pair</strong> toʻgʻri — doim koʻplikdagi otlar <em>a pair of</em> "
                       "bilan sanaladi: shim, qaychi, koʻzoynak, poyabzal.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>A pair of scissors ___ on the desk.</strong></p>",
        "choices": ["is", "are", "were", "have been"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — the head noun is <em>pair</em>, which is "
                       "singular. Compare <em>the scissors are</em>.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — asosiy ot <em>pair</em>, u esa birlikda. "
                       "<em>The scissors are</em> bilan solishtiring.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Two glasses of milk ___ on the table.</strong></p>",
        "choices": ["are", "is", "was", "has been"],
        "correct": "are",
        "explanation": "<p><strong>are</strong> is correct — <em>two glasses</em> is the plural head "
                       "noun.<br><br>"
                       "<em>(<strong>are</strong> toʻgʻri — <em>two glasses</em> koʻplikdagi asosiy "
                       "ot.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir gave me a useful ___ of advice.</strong></p>",
        "choices": ["piece", "slice", "pair", "bar"],
        "correct": "piece",
        "explanation": "<p><strong>piece</strong> is correct — abstract uncountables use <em>a piece "
                       "of</em>: advice, information, news, furniture.<br><br>"
                       "<em>(<strong>piece</strong> toʻgʻri — mavhum sanalmaydigan otlar <em>a piece "
                       "of</em> oladi: advice, information, news, furniture.)</em></p>",
    },
    {
        "text": "<p>Choose the correct meaning.</p>"
                "<p><strong>Madina has three <em>papers</em> to write this term.</strong></p>",
        "choices": ["three written works", "three sheets of paper",
                    "three newspapers only", "three pieces of card"],
        "correct": "three written works",
        "explanation": "<p><strong>three written works</strong> is correct — <em>paper</em> is "
                       "uncountable as a material, countable as an essay or a newspaper.<br><br>"
                       "<em>(<strong>uchta yozma ish</strong> toʻgʻri — <em>paper</em> material sifatida "
                       "sanalmaydi, insho yoki gazeta maʼnosida esa sanaladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct meaning.</p>"
                "<p><strong>Shaxzoda would like two <em>coffees</em>, please.</strong></p>",
        "choices": ["two cups of coffee", "two kilos of coffee",
                    "two coffee plants", "two coffee shops"],
        "correct": "two cups of coffee",
        "explanation": "<p><strong>two cups of coffee</strong> is correct — in a café, drinks become "
                       "countable and mean servings.<br><br>"
                       "<em>(<strong>ikki piyola qahva</strong> toʻgʻri — kafeda ichimliklar sanaladigan "
                       "boʻlib, porsiyani bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh doesn't have much ___ .</strong></p>",
        "choices": ["experience", "experiences of job", "an experience", "experience's"],
        "correct": "experience",
        "explanation": "<p><strong>experience</strong> is correct — uncountable when it means knowledge. "
                       "<em>An experience</em> would be one single event.<br><br>"
                       "<em>(<strong>experience</strong> toʻgʻri — bilim maʼnosida sanalmaydi. <em>An "
                       "experience</em> esa bitta voqeani bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct expression.</p>"
                "<p><strong>Sirojiddin bought a ___ of biscuits for the trip.</strong></p>",
        "choices": ["packet", "slice", "sheet", "pair"],
        "correct": "packet",
        "explanation": "<p><strong>packet</strong> is correct — <em>a packet of biscuits / crisps / "
                       "tea</em>.<br><br>"
                       "<em>(<strong>packet</strong> toʻgʻri — <em>a packet of biscuits / crisps / "
                       "tea</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct expression.</p>"
                "<p><strong>Marjona picked a ___ of flowers for her mother.</strong></p>",
        "choices": ["bunch", "bar", "loaf", "sheet"],
        "correct": "bunch",
        "explanation": "<p><strong>bunch</strong> is correct — <em>a bunch of flowers / grapes / "
                       "keys</em>.<br><br>"
                       "<em>(<strong>bunch</strong> toʻgʻri — <em>a bunch of flowers / grapes / "
                       "keys</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Davron needs a ___ of milk from the shop.</strong></p>",
        "choices": ["carton", "slice", "pair", "bar"],
        "correct": "carton",
        "explanation": "<p><strong>carton</strong> is correct — <em>a carton of milk / juice</em>."
                       "<br><br><em>(<strong>carton</strong> toʻgʻri — <em>a carton of milk / "
                       "juice</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Afsona bought two breads and three milks.",
                    "Afsona bought two loaves of bread and three bottles of milk.",
                    "Afsona bought some bread and some milk.",
                    "Afsona bought a loaf of bread and a carton of milk."],
        "correct": "Afsona bought two breads and three milks.",
        "explanation": "<p><strong>Afsona bought two breads and three milks.</strong> is the mistake — "
                       "count the container, not the uncountable noun itself.<br><br>"
                       "<em>(<strong>Afsona bought two breads and three milks.</strong> xato — "
                       "sanalmaydigan otning oʻzini emas, idishini sanang.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["I need a pair of scissors and two sheets of paper.",
                    "I need a scissors and two papers sheets.",
                    "I need two scissors and a sheet papers.",
                    "I need a pair of scissor and two sheet of papers."],
        "correct": "I need a pair of scissors and two sheets of paper.",
        "explanation": "<p><strong>I need a pair of scissors and two sheets of paper.</strong> is "
                       "correct — <em>a pair of</em> for the always-plural noun, <em>sheets of</em> for "
                       "the material.<br><br>"
                       "<em>(<strong>I need a pair of scissors and two sheets of paper.</strong> "
                       "toʻgʻri — doim koʻplikdagi ot uchun <em>a pair of</em>, material uchun esa "
                       "<em>sheets of</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Behruz:</strong> What shall I buy for the picnic?</p>"
                "<p><strong>Elbek:</strong> ___</p>",
        "choices": ["Two loaves of bread and a packet of biscuits.",
                    "Two breads and a biscuits packet.",
                    "Two loaf of breads and a packet of biscuit.",
                    "Two pieces of breads and a bar of biscuits."],
        "correct": "Two loaves of bread and a packet of biscuits.",
        "explanation": "<p><strong>Two loaves of bread and a packet of biscuits.</strong> is correct — "
                       "the plural goes on the container word, not on the uncountable noun.<br><br>"
                       "<em>(<strong>Two loaves of bread and a packet of biscuits.</strong> toʻgʻri — "
                       "koʻplik qoʻshimchasi sanalmaydigan otga emas, idish soʻziga qoʻshiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["A pair of glasses is on the desk, and two bottles of water are in the bag.",
                    "A pair of glasses are on the desk, and two bottles of water is in the bag.",
                    "A pair of glass is on the desk, and two bottle of waters are in the bag.",
                    "A glasses pair are on the desk, and two waters bottles is in the bag."],
        "correct": "A pair of glasses is on the desk, and two bottles of water are in the bag.",
        "explanation": "<p><strong>A pair … is · two bottles … are</strong> is correct — the verb agrees "
                       "with the container word, not with what is inside it.<br><br>"
                       "<em>(<strong>A pair … is · two bottles … are</strong> toʻgʻri — feʼl ichidagi "
                       "narsaga emas, idish soʻziga mos keladi.)</em></p>",
    },
]


# =====================================================================
# PE-80 — Articles: The Advanced Cases
# =====================================================================

Q_PE80 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz's family swam in ___ Amu Darya last summer.</strong></p>",
        "choices": ["the", "a", "an", "— (no article)"],
        "correct": "the",
        "explanation": "<p><strong>the</strong> is correct — rivers, seas and oceans take <em>the</em>."
                       "<br><br><em>(<strong>the</strong> toʻgʻri — daryolar, dengizlar va okeanlar "
                       "<em>the</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda has never been to ___ Uzbekistan's neighbour Kazakhstan.</strong></p>",
        "choices": ["— (no article)", "the", "a", "an"],
        "correct": "— (no article)",
        "explanation": "<p><strong>— (no article)</strong> is correct — single country names take no "
                       "article; only plural or group names do.<br><br>"
                       "<em>(<strong>Artiklsiz</strong> toʻgʻri — yakka davlat nomlari artikl olmaydi; "
                       "faqat koʻplik yoki guruh nomlari oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos wants to study in ___ USA.</strong></p>",
        "choices": ["the", "a", "an", "— (no article)"],
        "correct": "the",
        "explanation": "<p><strong>the</strong> is correct — plural or group country names take "
                       "<em>the</em>: <em>the USA, the Netherlands, the UAE</em>.<br><br>"
                       "<em>(<strong>the</strong> toʻgʻri — koʻplik yoki guruh davlat nomlari <em>the</em> "
                       "oladi: <em>the USA, the Netherlands, the UAE</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar's uncle has climbed in ___ Tian Shan.</strong></p>",
        "choices": ["the", "a", "an", "— (no article)"],
        "correct": "the",
        "explanation": "<p><strong>the</strong> is correct — mountain <em>ranges</em> take <em>the</em>, "
                       "but a single mountain does not.<br><br>"
                       "<em>(<strong>the</strong> toʻgʻri — togʻ <em>tizmalari</em> <em>the</em> oladi, "
                       "yakka togʻ esa olmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek would like to see ___ Mount Everest one day.</strong></p>",
        "choices": ["— (no article)", "the", "a", "an"],
        "correct": "— (no article)",
        "explanation": "<p><strong>— (no article)</strong> is correct — a single mountain takes no "
                       "article. Compare <em>the Alps</em>.<br><br>"
                       "<em>(<strong>Artiklsiz</strong> toʻgʻri — yakka togʻ artikl olmaydi. <em>The "
                       "Alps</em> bilan solishtiring.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs's family crossed ___ Kyzylkum by car.</strong></p>",
        "choices": ["the", "a", "an", "— (no article)"],
        "correct": "the",
        "explanation": "<p><strong>the</strong> is correct — deserts take <em>the</em>.<br><br>"
                       "<em>(<strong>the</strong> toʻgʻri — choʻllar <em>the</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir swam in ___ Lake Aydar.</strong></p>",
        "choices": ["— (no article)", "the", "a", "an"],
        "correct": "— (no article)",
        "explanation": "<p><strong>— (no article)</strong> is correct — lakes with <em>Lake</em> in the "
                       "name take no article, unlike rivers.<br><br>"
                       "<em>(<strong>Artiklsiz</strong> toʻgʻri — nomida <em>Lake</em> boʻlgan koʻllar, "
                       "daryolardan farqli oʻlaroq, artikl olmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ rich should help ___ poor.</strong></p>",
        "choices": ["The … the", "A … a", "— … —", "The … a"],
        "correct": "The … the",
        "explanation": "<p><strong>The … the</strong> is correct — <em>the + adjective</em> means a whole "
                       "group of people: <em>the rich, the poor, the young</em>.<br><br>"
                       "<em>(<strong>The … the</strong> toʻgʻri — <em>the + sifat</em> butun bir guruh "
                       "odamni bildiradi: <em>the rich, the poor, the young</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina plays ___ piano beautifully.</strong></p>",
        "choices": ["the", "a", "an", "— (no article)"],
        "correct": "the",
        "explanation": "<p><strong>the</strong> is correct — musical instruments take <em>the</em>, but "
                       "sports take nothing.<br><br>"
                       "<em>(<strong>the</strong> toʻgʻri — musiqa asboblari <em>the</em> oladi, sport "
                       "turlari esa olmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda's grandfather was born in ___ 1960s.</strong></p>",
        "choices": ["the", "a", "an", "— (no article)"],
        "correct": "the",
        "explanation": "<p><strong>the</strong> is correct — decades take <em>the</em>: <em>the 1990s, "
                       "the sixties</em>.<br><br>"
                       "<em>(<strong>the</strong> toʻgʻri — oʻn yilliklar <em>the</em> oladi: <em>the "
                       "1990s, the sixties</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh heard the news on ___ radio.</strong></p>",
        "choices": ["the", "a", "an", "— (no article)"],
        "correct": "the",
        "explanation": "<p><strong>the</strong> is correct — <em>the radio, the internet, the cinema</em> "
                       "— but <em>television</em> usually takes nothing: <em>watch TV</em>.<br><br>"
                       "<em>(<strong>the</strong> toʻgʻri — <em>the radio, the internet, the cinema</em> "
                       "— lekin <em>television</em> odatda artiklsiz: <em>watch TV</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin's father is ___ engineer.</strong></p>",
        "choices": ["an", "a", "the", "— (no article)"],
        "correct": "an",
        "explanation": "<p><strong>an</strong> is correct — jobs in the singular take <em>a/an</em>, "
                       "chosen by sound.<br><br>"
                       "<em>(<strong>an</strong> toʻgʻri — birlikdagi kasblar <em>a/an</em> oladi, tanlov "
                       "esa tovushga qarab.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ books are cheaper than they used to be.</strong> (books in "
                "general)</p>",
        "choices": ["— (no article)", "The", "A", "An"],
        "correct": "— (no article)",
        "explanation": "<p><strong>— (no article)</strong> is correct — a plural noun with no article is "
                       "the commonest way to make a general statement.<br><br>"
                       "<em>(<strong>Artiklsiz</strong> toʻgʻri — artiklsiz koʻplikdagi ot — umumiy fikr "
                       "bildirishning eng keng tarqalgan usuli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ tiger is a dangerous animal.</strong> (tigers in general, formal "
                "style)</p>",
        "choices": ["The", "A tiger's", "Some", "An"],
        "correct": "The",
        "explanation": "<p><strong>The</strong> is correct — <em>the + singular noun</em> can describe a "
                       "whole species in formal or scientific writing.<br><br>"
                       "<em>(<strong>The</strong> toʻgʻri — <em>the + birlikdagi ot</em> rasmiy yoki "
                       "ilmiy uslubda butun turni taʼriflashi mumkin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona goes to ___ university in Tashkent.</strong> (she is a "
                "student there)</p>",
        "choices": ["— (no article)", "the", "an", "a the"],
        "correct": "— (no article)",
        "explanation": "<p><strong>— (no article)</strong> is correct — like <em>school</em> and "
                       "<em>hospital</em>, it takes no article when you are there for its purpose."
                       "<br><br><em>(<strong>Artiklsiz</strong> toʻgʻri — <em>school</em> va "
                       "<em>hospital</em> kabi, oʻz vazifasi uchun borilganda artikl olmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Davron crossed ___ Black Sea and then visited ___ Turkey.</strong></p>",
        "choices": ["the … —", "— … the", "the … the", "a … the"],
        "correct": "the … —",
        "explanation": "<p><strong>the … —</strong> is correct — a sea takes <em>the</em>, a single "
                       "country takes nothing.<br><br>"
                       "<em>(<strong>the … —</strong> toʻgʻri — dengiz <em>the</em> oladi, yakka davlat "
                       "esa artiklsiz.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Afsona lives in the Uzbekistan.", "Afsona lives in Uzbekistan.",
                    "Afsona lives in the UK.", "Afsona lives in the Netherlands."],
        "correct": "Afsona lives in the Uzbekistan.",
        "explanation": "<p><strong>Afsona lives in the Uzbekistan.</strong> is the mistake — a single "
                       "country name takes no article.<br><br>"
                       "<em>(<strong>Afsona lives in the Uzbekistan.</strong> xato — yakka davlat nomi "
                       "artikl olmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Jasur plays the guitar and football.",
                    "Jasur plays guitar and the football.",
                    "Jasur plays the guitar and the football.",
                    "Jasur plays a guitar and a football."],
        "correct": "Jasur plays the guitar and football.",
        "explanation": "<p><strong>Jasur plays the guitar and football.</strong> is correct — instrument "
                       "with <em>the</em>, sport with nothing.<br><br>"
                       "<em>(<strong>Jasur plays the guitar and football.</strong> toʻgʻri — asbob "
                       "<em>the</em> bilan, sport esa artiklsiz.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Where would you like to travel, Charos?</p>"
                "<p><strong>Charos:</strong> ___</p>",
        "choices": ["To the Netherlands, and then along the Rhine.",
                    "To Netherlands, and then along Rhine.",
                    "To the Netherlands, and then along Rhine.",
                    "To Netherlands, and then along the Rhine river the."],
        "correct": "To the Netherlands, and then along the Rhine.",
        "explanation": "<p><strong>To the Netherlands, and then along the Rhine.</strong> is correct — a "
                       "plural country name and a river, both with <em>the</em>.<br><br>"
                       "<em>(<strong>To the Netherlands, and then along the Rhine.</strong> toʻgʻri — "
                       "koʻplikdagi davlat nomi va daryo, ikkisi ham <em>the</em> bilan.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> article is correct.</p>",
        "choices": ["The Amu Darya flows through Uzbekistan, past the Kyzylkum, "
                    "and the young often swim in it.",
                    "Amu Darya flows through the Uzbekistan, past Kyzylkum, "
                    "and young often swim in it.",
                    "The Amu Darya flows through the Uzbekistan, past the Kyzylkum, "
                    "and a young often swim in it.",
                    "Amu Darya flows through Uzbekistan, past the Kyzylkum, "
                    "and the youngs often swim in it."],
        "correct": "The Amu Darya flows through Uzbekistan, past the Kyzylkum, "
                   "and the young often swim in it.",
        "explanation": "<p><strong>the Amu Darya … Uzbekistan … the Kyzylkum … the young</strong> is "
                       "correct — a river and a desert take <em>the</em>, a single country takes nothing, "
                       "and <em>the + adjective</em> names a group.<br><br>"
                       "<em>(<strong>the Amu Darya … Uzbekistan … the Kyzylkum … the young</strong> "
                       "toʻgʻri — daryo va choʻl <em>the</em> oladi, yakka davlat artiklsiz, <em>the + "
                       "sifat</em> esa guruhni bildiradi.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-76 Practice: Adjective + Preposition, Verb + Preposition (Dependent Prepositions)",
        "tutorial":    "PE-76:",
        "description": "PE-76 darsiga 20 savol: good at, interested in, afraid of kabi qatʼiy "
                       "juftliklar, depend on va listen to, predlog olmaydigan feʼllar (discuss, "
                       "enter) va predlogdan keyingi -ing. Javoblar ingliz va oʻzbek tilida "
                       "izohlangan.",
        "questions":   Q_PE76,
    },
    {
        "title":       "PE-77 Practice: Phrasal Verbs: How They Actually Work",
        "tutorial":    "PE-77:",
        "description": "PE-77 darsiga 20 savol: feʼl + zarracha maʼnosi, ajraladigan va "
                       "ajralmaydigan turlari, olmosh qoidasi (turn it off) va ularni guruhlab "
                       "oʻrganish. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE77,
    },
    {
        "title":       "PE-78 Practice: 40 Everyday Phrasal Verbs by Topic",
        "tutorial":    "PE-78:",
        "description": "PE-78 darsiga 20 savol: kundalik hayot, oʻqish, odamlar, safar, muammo va "
                       "telefon mavzularidagi eng koʻp ishlatiladigan frazali feʼllar. Javoblar "
                       "ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE78,
    },
    {
        "title":       "PE-79 Practice: Countable and Uncountable Revisited: Expressions of Quantity",
        "tutorial":    "PE-79:",
        "description": "PE-79 darsiga 20 savol: a loaf / slice / piece / bottle kabi oʻlchov soʻzlari, "
                       "doim koʻplikdagi otlar uchun a pair of, ikki tomonlama otlar va feʼlning "
                       "mosligi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE79,
    },
    {
        "title":       "PE-80 Practice: Articles: The Advanced Cases",
        "tutorial":    "PE-80:",
        "description": "PE-80 darsiga 20 savol: geografik nomlarda the qoidasi, the + sifat = butun "
                       "guruh, musiqa asboblari, oʻn yilliklar va umumiy fikr bildirishning uch "
                       "yoʻli. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE80,
    },
]
