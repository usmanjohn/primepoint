# -*- coding: utf-8 -*-
"""Prime English practices — PE-61 … PE-65.

The full passive, reported speech, and the gerund/infinitive choice.
Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_61_65.py --master=prime --expect-questions=20
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
# PE-61 — Passive Voice in All Tenses
# =====================================================================

Q_PE61 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In the passive, which word carries the tense?</strong></p>",
        "choices": ["be", "the V3", "the subject", "by"],
        "correct": "be",
        "explanation": "<p><strong>be</strong> is correct — put <em>be</em> into any tense and the "
                       "passive follows automatically. The V3 never changes.<br><br>"
                       "<em>(<strong>be</strong> toʻgʻri — <em>be</em> ni istalgan zamonga qoʻysangiz, "
                       "passiv oʻzi shakllanadi. V3 esa hech qachon oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The classroom ___ at the moment — come back in ten minutes.</strong></p>",
        "choices": ["is being cleaned", "is cleaned", "was cleaned", "is cleaning"],
        "correct": "is being cleaned",
        "explanation": "<p><strong>is being cleaned</strong> is correct — present continuous passive: "
                       "<em>is being + V3</em>.<br><br>"
                       "<em>(<strong>is being cleaned</strong> toʻgʻri — hozirgi davomli zamon passivi: "
                       "<em>is being + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The tests ___ already ___ by Rozimurod teacher.</strong></p>",
        "choices": ["have … been marked", "have … marked", "has … been marked", "are … been marked"],
        "correct": "have … been marked",
        "explanation": "<p><strong>have … been marked</strong> is correct — present perfect passive: "
                       "<em>have / has been + V3</em>.<br><br>"
                       "<em>(<strong>have … been marked</strong> toʻgʻri — present perfect passivi: "
                       "<em>have / has been + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>When we arrived, the hall ___ .</strong></p>",
        "choices": ["was being decorated", "was decorated by", "is decorated", "were decorating"],
        "correct": "was being decorated",
        "explanation": "<p><strong>was being decorated</strong> is correct — past continuous passive, for "
                       "work in progress at that past moment.<br><br>"
                       "<em>(<strong>was being decorated</strong> toʻgʻri — oʻtgan davomli zamon "
                       "passivi, oʻsha daqiqada davom etayotgan ish uchun.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The letter ___ before we arrived.</strong></p>",
        "choices": ["had been sent", "had sent", "has been sent", "was send"],
        "correct": "had been sent",
        "explanation": "<p><strong>had been sent</strong> is correct — past perfect passive: <em>had been "
                       "+ V3</em>.<br><br>"
                       "<em>(<strong>had been sent</strong> toʻgʻri — past perfect passivi: <em>had been "
                       "+ V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The new school ___ next year.</strong></p>",
        "choices": ["will be opened", "will open by", "is opened", "will been opened"],
        "correct": "will be opened",
        "explanation": "<p><strong>will be opened</strong> is correct — future passive: <em>will be + "
                       "V3</em>.<br><br>"
                       "<em>(<strong>will be opened</strong> toʻgʻri — kelasi zamon passivi: <em>will be "
                       "+ V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>By June the building ___ .</strong></p>",
        "choices": ["will have been finished", "will be finish", "has been finished", "will finished"],
        "correct": "will have been finished",
        "explanation": "<p><strong>will have been finished</strong> is correct — future perfect passive: "
                       "<em>will have been + V3</em>.<br><br>"
                       "<em>(<strong>will have been finished</strong> toʻgʻri — future perfect passivi: "
                       "<em>will have been + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>This exercise ___ in five minutes.</strong></p>",
        "choices": ["can be done", "can do", "can be do", "can been done"],
        "correct": "can be done",
        "explanation": "<p><strong>can be done</strong> is correct — with a modal the pattern is "
                       "<em>modal + be + V3</em>.<br><br>"
                       "<em>(<strong>can be done</strong> toʻgʻri — modal bilan qolip <em>modal + be + "
                       "V3</em> boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The homework ___ before Friday.</strong></p>",
        "choices": ["must be handed in", "must hand in", "must be hand in", "must been handed in"],
        "correct": "must be handed in",
        "explanation": "<p><strong>must be handed in</strong> is correct — the same "
                       "<em>modal + be + V3</em> pattern, with a phrasal verb kept together.<br><br>"
                       "<em>(<strong>must be handed in</strong> toʻgʻri — xuddi shu <em>modal + be + "
                       "V3</em> qolipi, frazali feʼl esa buzilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>That mistake ___ — you should have checked your work.</strong></p>",
        "choices": ["could have been avoided", "could be avoided yesterday",
                    "could have avoided", "could been avoided"],
        "correct": "could have been avoided",
        "explanation": "<p><strong>could have been avoided</strong> is correct — a past modal passive: "
                       "<em>modal + have been + V3</em>.<br><br>"
                       "<em>(<strong>could have been avoided</strong> toʻgʻri — oʻtmishdagi modal "
                       "passivi: <em>modal + have been + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda ___ a prize at the olympiad.</strong></p>",
        "choices": ["was given", "was gave", "gave to", "is give"],
        "correct": "was given",
        "explanation": "<p><strong>was given</strong> is correct — with two objects, English usually "
                       "makes the <em>person</em> the passive subject.<br><br>"
                       "<em>(<strong>was given</strong> toʻgʻri — ikki toʻldiruvchi boʻlganda ingliz "
                       "tili odatda <em>shaxsni</em> passiv subject qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ the news this morning.</strong></p>",
        "choices": ["was told", "was telled", "told to", "is telling"],
        "correct": "was told",
        "explanation": "<p><strong>was told</strong> is correct — <em>tell → told → told</em>, with the "
                       "person as the subject.<br><br>"
                       "<em>(<strong>was told</strong> toʻgʻri — <em>tell → told → told</em>, shaxs esa "
                       "subject.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The cake ___ butter and sugar.</strong></p>",
        "choices": ["was made with", "was made by", "was made from by", "made with"],
        "correct": "was made with",
        "explanation": "<p><strong>was made with</strong> is correct — <em>by</em> introduces the doer; "
                       "<em>with</em> introduces the tool or ingredient.<br><br>"
                       "<em>(<strong>was made with</strong> toʻgʻri — <em>by</em> bajaruvchini, "
                       "<em>with</em> esa vosita yoki masalliqni kiritadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The window was broken ___ a stone.</strong></p>",
        "choices": ["with", "by", "from", "of"],
        "correct": "with",
        "explanation": "<p><strong>with</strong> is correct — the stone is the instrument. <em>Broken by "
                       "Elbek</em> would name the person.<br><br>"
                       "<em>(<strong>with</strong> toʻgʻri — tosh — vosita. <em>Broken by Elbek</em> esa "
                       "shaxsni koʻrsatgan boʻlardi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence keeps <em>by</em> for a good reason?</strong></p>",
        "choices": ["This poem was written by Alisher Navoiy.",
                    "My bag was stolen by somebody.",
                    "The letters are delivered by someone every day.",
                    "The room was cleaned by a person."],
        "correct": "This poem was written by Alisher Navoiy.",
        "explanation": "<p><strong>This poem was written by Alisher Navoiy.</strong> is correct — keep "
                       "<em>by</em> only when the doer adds real information.<br><br>"
                       "<em>(<strong>This poem was written by Alisher Navoiy.</strong> toʻgʻri — "
                       "<em>by</em> faqat bajaruvchi haqiqiy maʼlumot qoʻshganda saqlanadi.)</em></p>",
    },
    {
        "text": "<p>Make this passive.</p>"
                "<p><strong>They are repairing the road.</strong></p>",
        "choices": ["The road is being repaired.", "The road is repaired.",
                    "The road was being repaired.", "The road is repairing."],
        "correct": "The road is being repaired.",
        "explanation": "<p><strong>The road is being repaired.</strong> is correct — the active continuous "
                       "becomes <em>is being + V3</em>.<br><br>"
                       "<em>(<strong>The road is being repaired.</strong> toʻgʻri — aktiv davomli zamon "
                       "<em>is being + V3</em> ga aylanadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["The work has been did by Charos.", "The work has been done by Charos.",
                    "The work was done by Charos.", "Charos has done the work."],
        "correct": "The work has been did by Charos.",
        "explanation": "<p><strong>The work has been did by Charos.</strong> is the mistake — the passive "
                       "needs the third form <em>done</em>, never the past form <em>did</em>.<br><br>"
                       "<em>(<strong>The work has been did by Charos.</strong> xato — passivga uchinchi "
                       "shakl <em>done</em> kerak, <em>did</em> emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["The results will be announced tomorrow.",
                    "The results will announced tomorrow.",
                    "The results will be announce tomorrow.",
                    "The results will been announced tomorrow."],
        "correct": "The results will be announced tomorrow.",
        "explanation": "<p><strong>The results will be announced tomorrow.</strong> is correct — "
                       "<em>will be + V3</em>.<br><br>"
                       "<em>(<strong>The results will be announced tomorrow.</strong> toʻgʻri — "
                       "<em>will be + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Samandar:</strong> Why can't we use the gym today?</p>"
                "<p><strong>Madina:</strong> ___</p>",
        "choices": ["It's being painted this week.", "It's painted this week.",
                    "It's being paint this week.", "It has being painted this week."],
        "correct": "It's being painted this week.",
        "explanation": "<p><strong>It's being painted this week.</strong> is correct — work in progress "
                       "right now, so the present continuous passive.<br><br>"
                       "<em>(<strong>It's being painted this week.</strong> toʻgʻri — hozir davom "
                       "etayotgan ish, shuning uchun hozirgi davomli zamon passivi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> passive is correct.</p>",
        "choices": ["The hall has been cleaned, the chairs are being arranged, "
                    "and the prizes will be given out at six.",
                    "The hall has been clean, the chairs are being arrange, "
                    "and the prizes will given out at six.",
                    "The hall has cleaned, the chairs are arranging, "
                    "and the prizes will be gave out at six.",
                    "The hall has been cleaned, the chairs are been arranged, "
                    "and the prizes will be give out at six."],
        "correct": "The hall has been cleaned, the chairs are being arranged, "
                   "and the prizes will be given out at six.",
        "explanation": "<p><strong>has been cleaned … are being arranged … will be given out</strong> is "
                       "correct — three tenses, one formula, and the V3 never moves.<br><br>"
                       "<em>(<strong>has been cleaned … are being arranged … will be given out</strong> "
                       "toʻgʻri — uch zamon, bitta qolip, V3 esa oʻzgarmaydi.)</em></p>",
    },
]


# =====================================================================
# PE-62 — Reported Speech: Statements and Backshift
# =====================================================================

Q_PE62 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona: “I am tired.” → She ___ she was tired.</strong></p>",
        "choices": ["said", "told", "said to", "spoke"],
        "correct": "said",
        "explanation": "<p><strong>said</strong> is correct — <em>say</em> takes no person straight after "
                       "it.<br><br>"
                       "<em>(<strong>said</strong> toʻgʻri — <em>say</em> dan keyin darhol shaxs "
                       "kelmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>He ___ me he was busy.</strong></p>",
        "choices": ["told", "said", "said to me that", "spoke"],
        "correct": "told",
        "explanation": "<p><strong>told</strong> is correct — <em>tell</em> needs a person straight "
                       "after it. <em>He said me</em> is always wrong.<br><br>"
                       "<em>(<strong>told</strong> toʻgʻri — <em>tell</em> dan keyin darhol shaxs kerak. "
                       "<em>He said me</em> hech qachon toʻgʻri emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is <em>backshift</em>?</strong></p>",
        "choices": ["Every tense moves one step into the past.",
                    "Every tense moves one step into the future.",
                    "The word order changes.",
                    "The verb disappears."],
        "correct": "Every tense moves one step into the past.",
        "explanation": "<p><strong>Every tense moves one step into the past.</strong> is correct — "
                       "present → past, past → past perfect, <em>will</em> → <em>would</em>.<br><br>"
                       "<em>(<strong>Har bir zamon bir pogʻona orqaga suriladi.</strong> toʻgʻri — "
                       "hozirgi → oʻtgan, oʻtgan → past perfect, <em>will</em> → <em>would</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz: “I work in the library.” → He said he ___ in the "
                "library.</strong></p>",
        "choices": ["worked", "works", "had worked", "would work"],
        "correct": "worked",
        "explanation": "<p><strong>worked</strong> is correct — present simple steps back to past "
                       "simple.<br><br>"
                       "<em>(<strong>worked</strong> toʻgʻri — present simple past simple ga "
                       "suriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda: “I have finished.” → She said she ___ .</strong></p>",
        "choices": ["had finished", "has finished", "finished", "would finish"],
        "correct": "had finished",
        "explanation": "<p><strong>had finished</strong> is correct — present perfect steps back to past "
                       "perfect.<br><br>"
                       "<em>(<strong>had finished</strong> toʻgʻri — present perfect past perfect ga "
                       "suriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos: “I will call you.” → She said she ___ me.</strong></p>",
        "choices": ["would call", "will call", "called", "had called"],
        "correct": "would call",
        "explanation": "<p><strong>would call</strong> is correct — <em>will</em> becomes "
                       "<em>would</em>.<br><br>"
                       "<em>(<strong>would call</strong> toʻgʻri — <em>will</em> <em>would</em> ga "
                       "aylanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar: “I am reading.” → He said he ___ .</strong></p>",
        "choices": ["was reading", "is reading", "had read", "would read"],
        "correct": "was reading",
        "explanation": "<p><strong>was reading</strong> is correct — present continuous steps back to "
                       "past continuous.<br><br>"
                       "<em>(<strong>was reading</strong> toʻgʻri — present continuous past continuous "
                       "ga suriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek: “I saw the film.” → He said he ___ the film.</strong></p>",
        "choices": ["had seen", "saw", "has seen", "would see"],
        "correct": "had seen",
        "explanation": "<p><strong>had seen</strong> is correct — past simple steps back to past "
                       "perfect.<br><br>"
                       "<em>(<strong>had seen</strong> toʻgʻri — past simple past perfect ga "
                       "suriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs: “I can swim.” → He said he ___ swim.</strong></p>",
        "choices": ["could", "can", "will can", "had could"],
        "correct": "could",
        "explanation": "<p><strong>could</strong> is correct — <em>can</em> becomes <em>could</em>, "
                       "<em>may</em> becomes <em>might</em>.<br><br>"
                       "<em>(<strong>could</strong> toʻgʻri — <em>can</em> <em>could</em> ga, <em>may</em> "
                       "esa <em>might</em> ga aylanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir: “I am busy <em>today</em>.” → He said he was busy ___ "
                ".</strong></p>",
        "choices": ["that day", "today", "yesterday", "tomorrow"],
        "correct": "that day",
        "explanation": "<p><strong>that day</strong> is correct — time words shift too: "
                       "<em>today → that day, tomorrow → the next day, yesterday → the day "
                       "before</em>.<br><br>"
                       "<em>(<strong>that day</strong> toʻgʻri — vaqt soʻzlari ham suriladi: "
                       "<em>today → that day, tomorrow → the next day, yesterday → the day "
                       "before</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina: “I'll see you <em>tomorrow</em>.” → She said she would see me "
                "___ .</strong></p>",
        "choices": ["the next day", "tomorrow", "that day", "the day before"],
        "correct": "the next day",
        "explanation": "<p><strong>the next day</strong> is correct — the reporting happens later, so "
                       "<em>tomorrow</em> no longer means the same day.<br><br>"
                       "<em>(<strong>the next day</strong> toʻgʻri — yetkazish keyinroq boʻladi, shuning "
                       "uchun <em>tomorrow</em> endi oʻsha kunni bildirmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda: “I like <em>my</em> new school.” → She said she liked ___ new "
                "school.</strong></p>",
        "choices": ["her", "my", "your", "their"],
        "correct": "her",
        "explanation": "<p><strong>her</strong> is correct — pronouns shift to match the new "
                       "speaker.<br><br>"
                       "<em>(<strong>her</strong> toʻgʻri — olmoshlar yangi gapiruvchiga moslashib "
                       "oʻzgaradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>When do you <em>not</em> need to backshift?</strong></p>",
        "choices": ["When the statement is still true now.",
                    "When the sentence is long.",
                    "When the speaker is a teacher.",
                    "Backshift is always required."],
        "correct": "When the statement is still true now.",
        "explanation": "<p><strong>When the statement is still true now.</strong> is correct — "
                       "<em>Rozimurod teacher said that water boils at 100°</em> stays in the "
                       "present.<br><br>"
                       "<em>(<strong>Gap hozir ham toʻgʻri boʻlsa.</strong> toʻgʻri — <em>Rozimurod "
                       "teacher said that water boils at 100°</em> hozirgi zamonda qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher: “The test is on Friday.” (it is still Wednesday) → "
                "He said the test ___ on Friday.</strong></p>",
        "choices": ["is", "was being", "had been", "would have been"],
        "correct": "is",
        "explanation": "<p><strong>is</strong> is correct — the test has not happened yet, so keeping the "
                       "present is natural.<br><br>"
                       "<em>(<strong>is</strong> toʻgʻri — test hali boʻlmagan, shuning uchun hozirgi "
                       "zamonni saqlash tabiiy.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin: “I don't understand.” → He said he ___ .</strong></p>",
        "choices": ["didn't understand", "doesn't understand",
                    "hadn't understood", "wouldn't understand"],
        "correct": "didn't understand",
        "explanation": "<p><strong>didn't understand</strong> is correct — the negative shifts back "
                       "too.<br><br>"
                       "<em>(<strong>didn't understand</strong> toʻgʻri — inkor ham orqaga "
                       "suriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which word can always be left out?</strong></p>",
        "choices": ["that", "said", "told", "he"],
        "correct": "that",
        "explanation": "<p><strong>that</strong> is correct — <em>He said (that) he was tired</em>; both "
                       "versions are perfectly good English.<br><br>"
                       "<em>(<strong>that</strong> toʻgʻri — <em>He said (that) he was tired</em>; ikki "
                       "variant ham mutlaqo toʻgʻri.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Abdulloh said me he was late.", "Abdulloh told me he was late.",
                    "Abdulloh said he was late.", "Abdulloh said to me that he was late."],
        "correct": "Abdulloh said me he was late.",
        "explanation": "<p><strong>Abdulloh said me he was late.</strong> is the mistake — <em>say</em> "
                       "never takes a person directly; use <em>told me</em> or <em>said to me</em>."
                       "<br><br><em>(<strong>Abdulloh said me he was late.</strong> xato — <em>say</em> "
                       "dan keyin toʻgʻridan toʻgʻri shaxs kelmaydi; <em>told me</em> yoki <em>said to "
                       "me</em> deyiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Marjona said she had already eaten.",
                    "Marjona said she has already eaten yesterday.",
                    "Marjona told she had already eaten.",
                    "Marjona said she already eat."],
        "correct": "Marjona said she had already eaten.",
        "explanation": "<p><strong>Marjona said she had already eaten.</strong> is correct — present "
                       "perfect backshifted, and <em>said</em> with no person after it.<br><br>"
                       "<em>(<strong>Marjona said she had already eaten.</strong> toʻgʻri — present "
                       "perfect orqaga surilgan, <em>said</em> dan keyin esa shaxs yoʻq.)</em></p>",
    },
    {
        "text": "<p>Complete the report.</p>"
                "<p><strong>Davron:</strong> “I am going to Tashkent next week.”</p>"
                "<p><strong>Report:</strong> ___</p>",
        "choices": ["Davron said he was going to Tashkent the following week.",
                    "Davron said he is going to Tashkent next week ago.",
                    "Davron told he was going to Tashkent the following week.",
                    "Davron said me he was going to Tashkent next week."],
        "correct": "Davron said he was going to Tashkent the following week.",
        "explanation": "<p><strong>Davron said he was going to Tashkent the following week.</strong> is "
                       "correct — the verb, the pronoun and the time word all shift together.<br><br>"
                       "<em>(<strong>Davron said he was going to Tashkent the following week.</strong> "
                       "toʻgʻri — feʼl, olmosh va vaqt soʻzi birgalikda suriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Jasur told me he had finished his project and would bring it the next day.",
                    "Jasur said me he has finished his project and will bring it tomorrow.",
                    "Jasur told me he has finished his project and would bring it the next day.",
                    "Jasur said me that he had finished his project and will bring it next day."],
        "correct": "Jasur told me he had finished his project and would bring it the next day.",
        "explanation": "<p><strong>told me … had finished … would bring … the next day</strong> is "
                       "correct — <em>tell</em> with a person, both verbs backshifted, and the time word "
                       "moved.<br><br>"
                       "<em>(<strong>told me … had finished … would bring … the next day</strong> "
                       "toʻgʻri — shaxs bilan <em>tell</em>, ikki feʼl ham orqaga surilgan, vaqt soʻzi "
                       "esa oʻzgargan.)</em></p>",
    },
]


# =====================================================================
# PE-63 — Reported Questions, Commands and Reporting Verbs
# =====================================================================

Q_PE63 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>“Are you tired?” → He asked ___ I was tired.</strong></p>",
        "choices": ["if", "that", "what", "do"],
        "correct": "if",
        "explanation": "<p><strong>if</strong> is correct — a yes/no question is reported with <em>if</em> "
                       "or <em>whether</em>.<br><br>"
                       "<em>(<strong>if</strong> toʻgʻri — ha/yoʻq savoli <em>if</em> yoki "
                       "<em>whether</em> bilan yetkaziladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What happens to the word order in a reported question?</strong></p>",
        "choices": ["It becomes normal statement order.",
                    "It keeps the question order.",
                    "The subject disappears.",
                    "The verb goes first."],
        "correct": "It becomes normal statement order.",
        "explanation": "<p><strong>It becomes normal statement order.</strong> is correct — no inversion, "
                       "no <em>do/does</em>, and no question mark.<br><br>"
                       "<em>(<strong>Oddiy darak gap tartibiga oʻtadi.</strong> toʻgʻri — inversiya ham, "
                       "<em>do/does</em> ham, soʻroq belgisi ham qolmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>“Do you like plov?” → She asked if I ___ plov.</strong></p>",
        "choices": ["liked", "did like", "do like", "was liking"],
        "correct": "liked",
        "explanation": "<p><strong>liked</strong> is correct — <em>do</em> disappears completely; it only "
                       "existed to build the question.<br><br>"
                       "<em>(<strong>liked</strong> toʻgʻri — <em>do</em> butunlay yoʻqoladi; u faqat "
                       "savol yasash uchun kerak edi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>“Where do you live?” → He asked where I ___ .</strong></p>",
        "choices": ["lived", "did live", "do I live", "was living there"],
        "correct": "lived",
        "explanation": "<p><strong>lived</strong> is correct — the wh- word stays, then normal statement "
                       "order follows.<br><br>"
                       "<em>(<strong>lived</strong> toʻgʻri — wh- soʻzi qoladi, keyin esa oddiy darak gap "
                       "tartibi keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher asked me ___ I had finished my project.</strong></p>",
        "choices": ["whether", "that", "what", "did"],
        "correct": "whether",
        "explanation": "<p><strong>whether</strong> is correct — it means the same as <em>if</em> here, "
                       "and sounds slightly more formal.<br><br>"
                       "<em>(<strong>whether</strong> toʻgʻri — bu yerda <em>if</em> bilan bir xil "
                       "maʼnoda va biroz rasmiyroq eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>“Sit down.” → The teacher told us ___ down.</strong></p>",
        "choices": ["to sit", "sit", "that sit", "sitting"],
        "correct": "to sit",
        "explanation": "<p><strong>to sit</strong> is correct — orders are reported with <em>tell + "
                       "person + to + verb</em>.<br><br>"
                       "<em>(<strong>to sit</strong> toʻgʻri — buyruqlar <em>tell + shaxs + to + "
                       "feʼl</em> orqali yetkaziladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>“Don't be late.” → He told me ___ late.</strong></p>",
        "choices": ["not to be", "to not be", "don't be", "that not be"],
        "correct": "not to be",
        "explanation": "<p><strong>not to be</strong> is correct — the negative goes <em>before</em> "
                       "<em>to</em>.<br><br>"
                       "<em>(<strong>not to be</strong> toʻgʻri — inkor <em>to</em> dan <em>oldin</em> "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>“Please help me.” → Iroda asked me ___ her.</strong></p>",
        "choices": ["to help", "help", "helping", "that help"],
        "correct": "to help",
        "explanation": "<p><strong>to help</strong> is correct — requests use <em>ask + person + to + "
                       "verb</em>.<br><br>"
                       "<em>(<strong>to help</strong> toʻgʻri — iltimoslar <em>ask + shaxs + to + "
                       "feʼl</em> orqali yetkaziladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference between <em>tell</em> and <em>ask</em> "
                "here?</strong></p>",
        "choices": ["tell = an order · ask = a request",
                    "tell = a request · ask = an order",
                    "They are the same.",
                    "tell is polite, ask is rude."],
        "correct": "tell = an order · ask = a request",
        "explanation": "<p><strong>tell = an order · ask = a request</strong> is correct — the "
                       "grammar is identical, the politeness is not.<br><br>"
                       "<em>(<strong>tell = buyruq · ask = iltimos</strong> toʻgʻri — grammatikasi bir "
                       "xil, odob darajasi esa boshqacha.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ to help us with the boxes.</strong></p>",
        "choices": ["offered", "suggested", "insisted", "apologised"],
        "correct": "offered",
        "explanation": "<p><strong>offered</strong> is correct — <em>offer + to + verb</em>.<br><br>"
                       "<em>(<strong>offered</strong> toʻgʻri — <em>offer + to + feʼl</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ going to the museum together.</strong></p>",
        "choices": ["suggested", "offered", "promised", "refused"],
        "correct": "suggested",
        "explanation": "<p><strong>suggested</strong> is correct — <em>suggest</em> takes <em>-ing</em>, "
                       "never <em>to</em>.<br><br>"
                       "<em>(<strong>suggested</strong> toʻgʻri — <em>suggest</em> <em>-ing</em> oladi, "
                       "<em>to</em> emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ to lend anybody his notes.</strong></p>",
        "choices": ["refused", "suggested", "admitted", "denied"],
        "correct": "refused",
        "explanation": "<p><strong>refused</strong> is correct — <em>refuse + to + verb</em>.<br><br>"
                       "<em>(<strong>refused</strong> toʻgʻri — <em>refuse + to + feʼl</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek ___ breaking the window.</strong></p>",
        "choices": ["admitted", "promised", "offered", "refused"],
        "correct": "admitted",
        "explanation": "<p><strong>admitted</strong> is correct — <em>admit</em> and <em>deny</em> both "
                       "take <em>-ing</em>.<br><br>"
                       "<em>(<strong>admitted</strong> toʻgʻri — <em>admit</em> va <em>deny</em> ikkisi "
                       "ham <em>-ing</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ to bring the ball tomorrow.</strong></p>",
        "choices": ["promised", "admitted", "denied", "suggested"],
        "correct": "promised",
        "explanation": "<p><strong>promised</strong> is correct — <em>promise + to + verb</em>.<br><br>"
                       "<em>(<strong>promised</strong> toʻgʻri — <em>promise + to + feʼl</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>“What time does the film start?” → She asked what time the film "
                "___ .</strong></p>",
        "choices": ["started", "does start", "did start", "starts it"],
        "correct": "started",
        "explanation": "<p><strong>started</strong> is correct — backshift plus statement order, with "
                       "<em>does</em> gone.<br><br>"
                       "<em>(<strong>started</strong> toʻgʻri — orqaga surish va darak gap tartibi, "
                       "<em>does</em> esa yoʻqolgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>“Have you seen Javohir?” → He asked ___ .</strong></p>",
        "choices": ["if I had seen Javohir", "if had I seen Javohir",
                    "have I seen Javohir", "if I have seen Javohir?"],
        "correct": "if I had seen Javohir",
        "explanation": "<p><strong>if I had seen Javohir</strong> is correct — no inversion, no question "
                       "mark, and the present perfect steps back.<br><br>"
                       "<em>(<strong>if I had seen Javohir</strong> toʻgʻri — inversiya ham, soʻroq "
                       "belgisi ham yoʻq, present perfect esa orqaga suriladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["She asked me where did I live.", "She asked me where I lived.",
                    "She asked where I lived.", "She asked me if I lived there."],
        "correct": "She asked me where did I live.",
        "explanation": "<p><strong>She asked me where did I live.</strong> is the mistake — a reported "
                       "question keeps statement order, so <em>did</em> must go.<br><br>"
                       "<em>(<strong>She asked me where did I live.</strong> xato — yetkazilgan savol "
                       "darak gap tartibini saqlaydi, shuning uchun <em>did</em> tushib "
                       "qolishi kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Rozimurod teacher told us not to talk during the test.",
                    "Rozimurod teacher told us don't talk during the test.",
                    "Rozimurod teacher said us not to talk during the test.",
                    "Rozimurod teacher told to us not talk during the test."],
        "correct": "Rozimurod teacher told us not to talk during the test.",
        "explanation": "<p><strong>Rozimurod teacher told us not to talk during the test.</strong> is "
                       "correct — <em>tell + person + not to + verb</em>.<br><br>"
                       "<em>(<strong>Rozimurod teacher told us not to talk during the test.</strong> "
                       "toʻgʻri — <em>tell + shaxs + not to + feʼl</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the report.</p>"
                "<p><strong>Madina:</strong> “Can you help me with this exercise, Shaxzoda?”</p>"
                "<p><strong>Report:</strong> ___</p>",
        "choices": ["Madina asked Shaxzoda to help her with the exercise.",
                    "Madina asked Shaxzoda can she help her with the exercise.",
                    "Madina told Shaxzoda to helping her with the exercise.",
                    "Madina said Shaxzoda to help her with the exercise."],
        "correct": "Madina asked Shaxzoda to help her with the exercise.",
        "explanation": "<p><strong>Madina asked Shaxzoda to help her with the exercise.</strong> is "
                       "correct — <em>Can you …?</em> is a request, so it is reported with <em>ask + "
                       "person + to</em>.<br><br>"
                       "<em>(<strong>Madina asked Shaxzoda to help her with the exercise.</strong> "
                       "toʻgʻri — <em>Can you …?</em> — iltimos, shuning uchun <em>ask + shaxs + to</em> "
                       "orqali yetkaziladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Sirojiddin asked if I was free, told me to come at six, "
                    "and promised to bring the tickets.",
                    "Sirojiddin asked was I free, told me come at six, "
                    "and promised bringing the tickets.",
                    "Sirojiddin asked if was I free, said me to come at six, "
                    "and promised to bringing the tickets.",
                    "Sirojiddin asked me did I free, told to me come at six, "
                    "and promised he brings the tickets."],
        "correct": "Sirojiddin asked if I was free, told me to come at six, "
                   "and promised to bring the tickets.",
        "explanation": "<p><strong>asked if I was … told me to come … promised to bring</strong> is "
                       "correct — a reported question, an order and a promise, each in its own "
                       "pattern.<br><br>"
                       "<em>(<strong>asked if I was … told me to come … promised to bring</strong> "
                       "toʻgʻri — yetkazilgan savol, buyruq va vaʼda, har biri oʻz qolipida.)</em></p>",
    },
]


# =====================================================================
# PE-64 — Gerunds and Infinitives: The Basics
# =====================================================================

Q_PE64 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda enjoys ___ books in the evening.</strong></p>",
        "choices": ["reading", "to read", "read", "reads"],
        "correct": "reading",
        "explanation": "<p><strong>reading</strong> is correct — <em>enjoy</em> always takes the gerund "
                       "(<em>-ing</em>).<br><br>"
                       "<em>(<strong>reading</strong> toʻgʻri — <em>enjoy</em> doim gerundiy "
                       "(<em>-ing</em>) oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz wants ___ a doctor.</strong></p>",
        "choices": ["to be", "being", "be", "is"],
        "correct": "to be",
        "explanation": "<p><strong>to be</strong> is correct — <em>want</em> always takes the "
                       "infinitive.<br><br>"
                       "<em>(<strong>to be</strong> toʻgʻri — <em>want</em> doim infinitiv "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which rule never fails?</strong></p>",
        "choices": ["After a preposition, always use -ing.",
                    "After a preposition, always use to + verb.",
                    "After a verb, always use -ing.",
                    "After a noun, always use to + verb."],
        "correct": "After a preposition, always use -ing.",
        "explanation": "<p><strong>After a preposition, always use -ing.</strong> is correct — "
                       "<em>afraid of swimming, good at drawing, instead of going</em>.<br><br>"
                       "<em>(<strong>Predlogdan keyin doim -ing.</strong> toʻgʻri — <em>afraid of "
                       "swimming, good at drawing, instead of going</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos is good at ___ pictures.</strong></p>",
        "choices": ["drawing", "to draw", "draw", "draws"],
        "correct": "drawing",
        "explanation": "<p><strong>drawing</strong> is correct — <em>at</em> is a preposition, so the "
                       "<em>-ing</em> form must follow.<br><br>"
                       "<em>(<strong>drawing</strong> toʻgʻri — <em>at</em> predlog, shuning uchun undan "
                       "keyin <em>-ing</em> shakli keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar is afraid of ___ in deep water.</strong></p>",
        "choices": ["swimming", "to swim", "swim", "swims"],
        "correct": "swimming",
        "explanation": "<p><strong>swimming</strong> is correct — again after a preposition.<br><br>"
                       "<em>(<strong>swimming</strong> toʻgʻri — yana predlogdan keyin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ is good for your health.</strong></p>",
        "choices": ["Swimming", "To swimming", "Swim", "Swims"],
        "correct": "Swimming",
        "explanation": "<p><strong>Swimming</strong> is correct — a gerund can be the subject of a "
                       "sentence, exactly like a noun.<br><br>"
                       "<em>(<strong>Swimming</strong> toʻgʻri — gerundiy xuddi ot kabi gapning subjecti "
                       "boʻla oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek decided ___ Korean next year.</strong></p>",
        "choices": ["to study", "studying", "study", "studies"],
        "correct": "to study",
        "explanation": "<p><strong>to study</strong> is correct — <em>decide, hope, plan, promise, "
                       "agree</em> all take the infinitive.<br><br>"
                       "<em>(<strong>to study</strong> toʻgʻri — <em>decide, hope, plan, promise, "
                       "agree</em> — hammasi infinitiv oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs finished ___ his homework at nine.</strong></p>",
        "choices": ["doing", "to do", "do", "did"],
        "correct": "doing",
        "explanation": "<p><strong>doing</strong> is correct — <em>finish, avoid, mind, suggest, "
                       "practise</em> take the gerund.<br><br>"
                       "<em>(<strong>doing</strong> toʻgʻri — <em>finish, avoid, mind, suggest, "
                       "practise</em> gerundiy oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher told Javohir ___ his answer again.</strong></p>",
        "choices": ["to check", "checking", "check", "checks"],
        "correct": "to check",
        "explanation": "<p><strong>to check</strong> is correct — the pattern <em>verb + person + to + "
                       "verb</em>: <em>tell, ask, want, allow, teach</em>.<br><br>"
                       "<em>(<strong>to check</strong> toʻgʻri — <em>feʼl + shaxs + to + feʼl</em> "
                       "qolipi: <em>tell, ask, want, allow, teach</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina's parents want her ___ at university.</strong></p>",
        "choices": ["to study", "studying", "study", "studies"],
        "correct": "to study",
        "explanation": "<p><strong>to study</strong> is correct — <em>want + person + to + verb</em>, and "
                       "the person takes the object form (<em>her</em>).<br><br>"
                       "<em>(<strong>to study</strong> toʻgʻri — <em>want + shaxs + to + feʼl</em>, shaxs "
                       "esa object shaklida (<em>her</em>).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda avoids ___ late to school.</strong></p>",
        "choices": ["being", "to be", "be", "is"],
        "correct": "being",
        "explanation": "<p><strong>being</strong> is correct — <em>avoid</em> takes the gerund.<br><br>"
                       "<em>(<strong>being</strong> toʻgʻri — <em>avoid</em> gerundiy oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh hopes ___ the olympiad this year.</strong></p>",
        "choices": ["to win", "winning", "win", "wins"],
        "correct": "to win",
        "explanation": "<p><strong>to win</strong> is correct — <em>hope</em> takes the infinitive."
                       "<br><br><em>(<strong>to win</strong> toʻgʻri — <em>hope</em> infinitiv "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin is thinking about ___ a new bicycle.</strong></p>",
        "choices": ["buying", "to buy", "buy", "buys"],
        "correct": "buying",
        "explanation": "<p><strong>buying</strong> is correct — <em>about</em> is a preposition, and the "
                       "rule never fails.<br><br>"
                       "<em>(<strong>buying</strong> toʻgʻri — <em>about</em> predlog, qoida esa hech "
                       "qachon buzilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona doesn't mind ___ early.</strong></p>",
        "choices": ["getting up", "to get up", "get up", "gets up"],
        "correct": "getting up",
        "explanation": "<p><strong>getting up</strong> is correct — <em>mind</em> takes the gerund, as "
                       "you saw with <em>Would you mind …?</em> in PE-49.<br><br>"
                       "<em>(<strong>getting up</strong> toʻgʻri — <em>mind</em> gerundiy oladi, xuddi "
                       "PE-49 dagi <em>Would you mind …?</em> kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Davron went to the shop ___ some bread.</strong></p>",
        "choices": ["to buy", "for buying", "buying", "buy"],
        "correct": "to buy",
        "explanation": "<p><strong>to buy</strong> is correct — the infinitive of purpose answers "
                       "<em>why?</em><br><br>"
                       "<em>(<strong>to buy</strong> toʻgʻri — maqsad infinitivi <em>nima uchun?</em> "
                       "savoliga javob beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Afsona enjoys ___ but she wants ___ a doctor.</strong></p>",
        "choices": ["singing … to be", "to sing … being", "singing … being", "to sing … to be"],
        "correct": "singing … to be",
        "explanation": "<p><strong>singing … to be</strong> is correct — <em>enjoy</em> takes the gerund, "
                       "<em>want</em> takes the infinitive.<br><br>"
                       "<em>(<strong>singing … to be</strong> toʻgʻri — <em>enjoy</em> gerundiy, "
                       "<em>want</em> esa infinitiv oladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Jasur is interested in to learn Korean.",
                    "Jasur is interested in learning Korean.",
                    "Jasur wants to learn Korean.",
                    "Jasur enjoys learning Korean."],
        "correct": "Jasur is interested in to learn Korean.",
        "explanation": "<p><strong>Jasur is interested in to learn Korean.</strong> is the mistake — "
                       "<em>in</em> is a preposition, so it must be <em>learning</em>.<br><br>"
                       "<em>(<strong>Jasur is interested in to learn Korean.</strong> xato — <em>in</em> "
                       "predlog, shuning uchun <em>learning</em> boʻlishi kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Behruz suggested going to the cinema.",
                    "Behruz suggested to go to the cinema.",
                    "Behruz suggested me to go to the cinema.",
                    "Behruz suggested that go to the cinema."],
        "correct": "Behruz suggested going to the cinema.",
        "explanation": "<p><strong>Behruz suggested going to the cinema.</strong> is correct — "
                       "<em>suggest</em> takes the gerund and never <em>suggest somebody to do</em>."
                       "<br><br><em>(<strong>Behruz suggested going to the cinema.</strong> toʻgʻri — "
                       "<em>suggest</em> gerundiy oladi va hech qachon <em>suggest somebody to do</em> "
                       "boʻlmaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Why did you come early today, Charos?</p>"
                "<p><strong>Charos:</strong> ___</p>",
        "choices": ["To ask you about the project.", "For ask you about the project.",
                    "For asking you about the project.", "Asking you about the project."],
        "correct": "To ask you about the project.",
        "explanation": "<p><strong>To ask you about the project.</strong> is correct — purpose takes "
                       "<em>to + verb</em>, not <em>for + -ing</em>.<br><br>"
                       "<em>(<strong>To ask you about the project.</strong> toʻgʻri — maqsad <em>to + "
                       "feʼl</em> bilan ifodalanadi, <em>for + -ing</em> bilan emas.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Iroda decided to study harder, practised speaking every day, "
                    "and succeeded in passing the exam.",
                    "Iroda decided studying harder, practised to speak every day, "
                    "and succeeded to pass the exam.",
                    "Iroda decided to study harder, practised to speaking every day, "
                    "and succeeded in to pass the exam.",
                    "Iroda decided study harder, practised speaking every day, "
                    "and succeeded pass the exam."],
        "correct": "Iroda decided to study harder, practised speaking every day, "
                   "and succeeded in passing the exam.",
        "explanation": "<p><strong>decided to … practised speaking … succeeded in passing</strong> is "
                       "correct — an infinitive verb, a gerund verb, and a preposition forcing "
                       "<em>-ing</em>.<br><br>"
                       "<em>(<strong>decided to … practised speaking … succeeded in passing</strong> "
                       "toʻgʻri — infinitiv oladigan feʼl, gerundiy oladigan feʼl va <em>-ing</em> ni "
                       "talab qiladigan predlog.)</em></p>",
    },
]


# =====================================================================
# PE-65 — Verbs That Change Meaning
# =====================================================================

Q_PE65 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz's uncle stopped ___ last year — he hasn't touched a cigarette "
                "since.</strong></p>",
        "choices": ["smoking", "to smoke", "smoke", "smoked"],
        "correct": "smoking",
        "explanation": "<p><strong>smoking</strong> is correct — <em>stop + -ing</em> means giving the "
                       "activity up.<br><br>"
                       "<em>(<strong>smoking</strong> toʻgʻri — <em>stop + -ing</em> faoliyatni tashlash "
                       "degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We drove for hours, then we stopped ___ lunch.</strong></p>",
        "choices": ["to have", "having", "have", "had"],
        "correct": "to have",
        "explanation": "<p><strong>to have</strong> is correct — <em>stop + to</em> means pausing "
                       "<em>in order to</em> do something else.<br><br>"
                       "<em>(<strong>to have</strong> toʻgʻri — <em>stop + to</em> boshqa ish qilish "
                       "<em>uchun</em> toʻxtash degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the underlying logic?</strong></p>",
        "choices": ["-ing = the activity itself or earlier · to = the purpose or later",
                    "-ing = the future · to = the past",
                    "-ing = formal · to = informal",
                    "There is no logic; you memorise everything."],
        "correct": "-ing = the activity itself or earlier · to = the purpose or later",
        "explanation": "<p><strong>-ing = the activity itself or earlier · to = the purpose or "
                       "later</strong> is correct — that one idea explains every verb in this "
                       "lesson.<br><br>"
                       "<em>(<strong>-ing = faoliyatning oʻzi yoki avvalgi · to = maqsad yoki "
                       "keyingi</strong> toʻgʻri — shu bitta gʻoya bu darsdagi hamma feʼlni "
                       "tushuntiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda remembered ___ the door — she can picture herself doing "
                "it.</strong></p>",
        "choices": ["locking", "to lock", "lock", "locked"],
        "correct": "locking",
        "explanation": "<p><strong>locking</strong> is correct — <em>remember + -ing</em> = the action "
                       "happened first, the memory came after.<br><br>"
                       "<em>(<strong>locking</strong> toʻgʻri — <em>remember + -ing</em> = avval ish "
                       "bajarilgan, keyin esa esga olingan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Remember ___ your homework tomorrow!</strong></p>",
        "choices": ["to bring", "bringing", "bring", "brought"],
        "correct": "to bring",
        "explanation": "<p><strong>to bring</strong> is correct — <em>remember + to</em> = the memory "
                       "comes first, the action later.<br><br>"
                       "<em>(<strong>to bring</strong> toʻgʻri — <em>remember + to</em> = avval esga "
                       "olinadi, ish esa keyin bajariladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos will never forget ___ the sea for the first time.</strong></p>",
        "choices": ["seeing", "to see", "see", "saw"],
        "correct": "seeing",
        "explanation": "<p><strong>seeing</strong> is correct — <em>forget + -ing</em> is about a memory "
                       "you keep, usually a strong one.<br><br>"
                       "<em>(<strong>seeing</strong> toʻgʻri — <em>forget + -ing</em> saqlanib qolgan, "
                       "odatda kuchli xotira haqida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar forgot ___ his dictionary, so he had to share.</strong></p>",
        "choices": ["to bring", "bringing", "bring", "brought"],
        "correct": "to bring",
        "explanation": "<p><strong>to bring</strong> is correct — <em>forget + to</em> = he did not do "
                       "it.<br><br>"
                       "<em>(<strong>to bring</strong> toʻgʻri — <em>forget + to</em> = u buni "
                       "bajarmagan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The window won't open. Try ___ it with warm water.</strong></p>",
        "choices": ["washing", "to wash", "wash", "washed"],
        "correct": "washing",
        "explanation": "<p><strong>washing</strong> is correct — <em>try + -ing</em> means experimenting "
                       "with a method to see if it helps.<br><br>"
                       "<em>(<strong>washing</strong> toʻgʻri — <em>try + -ing</em> foyda beradimi deb "
                       "biror usulni sinab koʻrish degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek tried ___ the heavy box, but he couldn't.</strong></p>",
        "choices": ["to lift", "lifting", "lift", "lifted"],
        "correct": "to lift",
        "explanation": "<p><strong>to lift</strong> is correct — <em>try + to</em> means making an effort "
                       "at something difficult.<br><br>"
                       "<em>(<strong>to lift</strong> toʻgʻri — <em>try + to</em> qiyin ishga urinib "
                       "koʻrish degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>After a short break, Rozimurod teacher went on ___ the next "
                "topic.</strong></p>",
        "choices": ["to explain", "explaining", "explain", "explained"],
        "correct": "to explain",
        "explanation": "<p><strong>to explain</strong> is correct — <em>go on + to</em> = move to "
                       "something new.<br><br>"
                       "<em>(<strong>to explain</strong> toʻgʻri — <em>go on + to</em> = yangi narsaga "
                       "oʻtish.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs went on ___ for another hour without a break.</strong></p>",
        "choices": ["working", "to work", "work", "worked"],
        "correct": "working",
        "explanation": "<p><strong>working</strong> is correct — <em>go on + -ing</em> = continue the "
                       "same activity.<br><br>"
                       "<em>(<strong>working</strong> toʻgʻri — <em>go on + -ing</em> = oʻsha faoliyatni "
                       "davom ettirish.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir likes ___ football at the weekend.</strong></p>",
        "choices": ["playing", "to playing", "play", "played"],
        "correct": "playing",
        "explanation": "<p><strong>playing</strong> is correct — <em>like + -ing</em> means enjoying "
                       "it.<br><br>"
                       "<em>(<strong>playing</strong> toʻgʻri — <em>like + -ing</em> undan zavq olish "
                       "degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina likes ___ her homework before dinner — it's the sensible "
                "thing.</strong></p>",
        "choices": ["to do", "doing it always", "do", "did"],
        "correct": "to do",
        "explanation": "<p><strong>to do</strong> is correct — <em>like + to</em> often means “I think it "
                       "is a good idea”, not “I enjoy it”.<br><br>"
                       "<em>(<strong>to do</strong> toʻgʻri — <em>like + to</em> koʻpincha “zavq "
                       "olaman” emas, “buni toʻgʻri deb bilaman” maʼnosini beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>These shoes are dirty — they need ___ .</strong></p>",
        "choices": ["cleaning", "to clean", "clean", "cleaned"],
        "correct": "cleaning",
        "explanation": "<p><strong>cleaning</strong> is correct — <em>need + -ing</em> has a passive "
                       "meaning: they need <em>to be cleaned</em>.<br><br>"
                       "<em>(<strong>cleaning</strong> toʻgʻri — <em>need + -ing</em> passiv maʼno "
                       "beradi: ularni tozalash kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda needs ___ harder for the olympiad.</strong></p>",
        "choices": ["to work", "working", "work", "worked"],
        "correct": "to work",
        "explanation": "<p><strong>to work</strong> is correct — with a person as the subject, "
                       "<em>need</em> takes the ordinary infinitive.<br><br>"
                       "<em>(<strong>to work</strong> toʻgʻri — subject shaxs boʻlsa, <em>need</em> oddiy "
                       "infinitiv oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Abdulloh stopped ___ computer games and started ___ more.</strong></p>",
        "choices": ["playing … reading", "to play … to read", "playing … to read", "to play … reading"],
        "correct": "playing … reading",
        "explanation": "<p><strong>playing … reading</strong> is correct — he gave up one activity and "
                       "took up another; <em>start</em> accepts both forms but <em>-ing</em> is natural "
                       "here.<br><br>"
                       "<em>(<strong>playing … reading</strong> toʻgʻri — u bir faoliyatni tashlab, "
                       "boshqasini boshladi; <em>start</em> ikki shaklni ham oladi, lekin bu yerda "
                       "<em>-ing</em> tabiiyroq.)</em></p>",
    },
    {
        "text": "<p>Which sentence means “he gave up football”?</p>",
        "choices": ["Sirojiddin stopped playing football.",
                    "Sirojiddin stopped to play football.",
                    "Sirojiddin stopped to watch football.",
                    "Sirojiddin went on to play football."],
        "correct": "Sirojiddin stopped playing football.",
        "explanation": "<p><strong>Sirojiddin stopped playing football.</strong> is correct — "
                       "<em>stopped to play</em> would mean he paused something else in order to "
                       "play.<br><br>"
                       "<em>(<strong>Sirojiddin stopped playing football.</strong> toʻgʻri — "
                       "<em>stopped to play</em> desa, oʻynash uchun boshqa ishni toʻxtatgani "
                       "chiqadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake in meaning</strong>?</p>",
        "choices": ["I remembered to lock the door yesterday — luckily, because I forgot.",
                    "I remembered locking the door, so I wasn't worried.",
                    "Remember to lock the door tonight.",
                    "I'll never forget seeing the mountains for the first time."],
        "correct": "I remembered to lock the door yesterday — luckily, because I forgot.",
        "explanation": "<p><strong>I remembered to lock the door yesterday — luckily, because I "
                       "forgot.</strong> contradicts itself: <em>remembered to lock</em> means he did "
                       "lock it.<br><br>"
                       "<em>(<strong>I remembered to lock the door yesterday — luckily, because I "
                       "forgot.</strong> oʻz-oʻziga zid: <em>remembered to lock</em> u qulflagan "
                       "degani.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Marjona:</strong> My computer keeps freezing.</p>"
                "<p><strong>Davron:</strong> ___</p>",
        "choices": ["Try restarting it — that usually helps.",
                    "Try to restart it — that usually helps.",
                    "Try restart it — that usually helps.",
                    "Try for restarting it — that usually helps."],
        "correct": "Try restarting it — that usually helps.",
        "explanation": "<p><strong>Try restarting it — that usually helps.</strong> is correct — a method "
                       "worth experimenting with, so <em>-ing</em>.<br><br>"
                       "<em>(<strong>Try restarting it — that usually helps.</strong> toʻgʻri — sinab "
                       "koʻrishga arziydigan usul, shuning uchun <em>-ing</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> form is correct.</p>",
        "choices": ["Afsona stopped watching TV, remembered to phone her mother, "
                    "and went on studying until midnight.",
                    "Afsona stopped to watch TV, remembered phoning her mother tomorrow, "
                    "and went on to study until midnight.",
                    "Afsona stopped watching TV, remembered phoning her mother tomorrow, "
                    "and went on study until midnight.",
                    "Afsona stopped watch TV, remembered to phoning her mother, "
                    "and went on studied until midnight."],
        "correct": "Afsona stopped watching TV, remembered to phone her mother, "
                   "and went on studying until midnight.",
        "explanation": "<p><strong>stopped watching … remembered to phone … went on studying</strong> is "
                       "correct — an activity given up, a duty carried out, and one activity "
                       "continued.<br><br>"
                       "<em>(<strong>stopped watching … remembered to phone … went on studying</strong> "
                       "toʻgʻri — tashlangan faoliyat, bajarilgan vazifa va davom ettirilgan bir "
                       "ish.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-61 Practice: Passive Voice in All Tenses, and the by-agent",
        "tutorial":    "PE-61:",
        "description": "PE-61 darsiga 20 savol: barcha zamonlarda passiv (faqat be oʻzgaradi), "
                       "modallar bilan passiv, ikki toʻldiruvchili feʼllar hamda by va with farqi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE61,
    },
    {
        "title":       "PE-62 Practice: Reported Speech: Statements and Backshift",
        "tutorial":    "PE-62:",
        "description": "PE-62 darsiga 20 savol: say va tell farqi, backshift jadvali, olmosh va vaqt "
                       "soʻzlarining oʻzgarishi hamda backshift shart boʻlmagan holatlar. Javoblar "
                       "ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE62,
    },
    {
        "title":       "PE-63 Practice: Reported Speech: Questions, Commands and Reporting Verbs",
        "tutorial":    "PE-63:",
        "description": "PE-63 darsiga 20 savol: if / whether bilan savollar, wh- savollarda darak gap "
                       "tartibi, tell / ask + to bilan buyruq va iltimoslar, hamda asosiy yetkazish "
                       "feʼllari. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE63,
    },
    {
        "title":       "PE-64 Practice: Gerunds and Infinitives: The Basics",
        "tutorial":    "PE-64:",
        "description": "PE-64 darsiga 20 savol: gerundiy va infinitiv, predlogdan keyin doim -ing "
                       "qoidasi, qaysi feʼl qaysi shaklni olishi va feʼl + shaxs + to qolipi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE64,
    },
    {
        "title":       "PE-65 Practice: Verbs That Change Meaning: stop doing vs stop to do",
        "tutorial":    "PE-65:",
        "description": "PE-65 darsiga 20 savol: stop, remember, forget, try, go on feʼllarining "
                       "maʼno oʻzgarishi, -ing va to ortidagi mantiq hamda need washing "
                       "qolipi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE65,
    },
]
