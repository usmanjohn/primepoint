# -*- coding: utf-8 -*-
"""Prime English practices — PE-41 … PE-45.

The tense map, then the start of Block D (modal verbs).
Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_41_45.py --master=prime --expect-questions=20
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
# PE-41 — The 12 Tenses: The Complete Map
# =====================================================================

Q_PE41 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How is the English tense system built?</strong></p>",
        "choices": ["3 times × 4 aspects = 12 tenses", "12 separate unrelated tenses",
                    "4 times × 2 aspects = 8 tenses", "2 times × 6 aspects = 12 tenses"],
        "correct": "3 times × 4 aspects = 12 tenses",
        "explanation": "<p><strong>3 times × 4 aspects = 12 tenses</strong> is correct — past, present, "
                       "future, each in Simple, Continuous, Perfect and Perfect Continuous.<br><br>"
                       "<em>(<strong>3 zamon × 4 aspekt = 12 shakl</strong> toʻgʻri — oʻtgan, hozirgi va "
                       "kelasi zamon, har biri Simple, Continuous, Perfect va Perfect Continuous "
                       "koʻrinishida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does the <em>Continuous</em> aspect show?</strong></p>",
        "choices": ["The action is in progress at that time.",
                    "The action is finished with a result.",
                    "The action is a plain fact.",
                    "The action never happened."],
        "correct": "The action is in progress at that time.",
        "explanation": "<p><strong>The action is in progress at that time.</strong> is correct — the "
                       "Continuous puts you in the middle of the action.<br><br>"
                       "<em>(<strong>Harakat oʻsha paytda davom etayotgan boʻladi.</strong> toʻgʻri — "
                       "Continuous sizni harakatning oʻrtasiga olib kiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does the <em>Perfect</em> aspect show?</strong></p>",
        "choices": ["Finished earlier, and it matters at that point.",
                    "Happening right now.",
                    "A repeated habit.",
                    "Something that will never happen."],
        "correct": "Finished earlier, and it matters at that point.",
        "explanation": "<p><strong>Finished earlier, and it matters at that point.</strong> is correct — "
                       "the Perfect always looks back from a chosen moment.<br><br>"
                       "<em>(<strong>Oldinroq tugagan va oʻsha nuqtada muhim.</strong> toʻgʻri — Perfect "
                       "doim tanlangan daqiqadan orqaga qaraydi.)</em></p>",
    },
    {
        "text": "<p>Name the tense.</p>"
                "<p><strong>Iroda is writing a letter.</strong></p>",
        "choices": ["Present Continuous", "Present Simple", "Present Perfect", "Past Continuous"],
        "correct": "Present Continuous",
        "explanation": "<p><strong>Present Continuous</strong> is correct — <em>am / is / are + "
                       "-ing</em>.<br><br>"
                       "<em>(<strong>Present Continuous</strong> toʻgʻri — <em>am / is / are + "
                       "-ing</em>.)</em></p>",
    },
    {
        "text": "<p>Name the tense.</p>"
                "<p><strong>Behruz had finished his homework.</strong></p>",
        "choices": ["Past Perfect", "Present Perfect", "Past Simple", "Future Perfect"],
        "correct": "Past Perfect",
        "explanation": "<p><strong>Past Perfect</strong> is correct — <em>had + V3</em>.<br><br>"
                       "<em>(<strong>Past Perfect</strong> toʻgʻri — <em>had + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Name the tense.</p>"
                "<p><strong>Charos will have been studying for three hours.</strong></p>",
        "choices": ["Future Perfect Continuous", "Future Continuous",
                    "Future Perfect", "Present Perfect Continuous"],
        "correct": "Future Perfect Continuous",
        "explanation": "<p><strong>Future Perfect Continuous</strong> is correct — "
                       "<em>will have been + -ing</em>, the longest form in the system.<br><br>"
                       "<em>(<strong>Future Perfect Continuous</strong> toʻgʻri — <em>will have been + "
                       "-ing</em>, tizimdagi eng uzun shakl.)</em></p>",
    },
    {
        "text": "<p>Choose the correct form.</p>"
                "<p><strong>Present Perfect of <em>work</em>, for “she”:</strong></p>",
        "choices": ["she has worked", "she have worked", "she has been work", "she worked"],
        "correct": "she has worked",
        "explanation": "<p><strong>she has worked</strong> is correct — <em>has + V3</em>.<br><br>"
                       "<em>(<strong>she has worked</strong> toʻgʻri — <em>has + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct form.</p>"
                "<p><strong>Past Continuous of <em>work</em>, for “they”:</strong></p>",
        "choices": ["they were working", "they was working", "they had working", "they work"],
        "correct": "they were working",
        "explanation": "<p><strong>they were working</strong> is correct — <em>was / were + -ing</em>, "
                       "and a plural subject takes <em>were</em>.<br><br>"
                       "<em>(<strong>they were working</strong> toʻgʻri — <em>was / were + -ing</em>, "
                       "koʻplikdagi subject esa <em>were</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ this school since 2021.</strong></p>",
        "choices": ["has attended", "attends", "attended", "is attending"],
        "correct": "has attended",
        "explanation": "<p><strong>has attended</strong> is correct — started in the past, still true, so "
                       "the Present Perfect.<br><br>"
                       "<em>(<strong>has attended</strong> toʻgʻri — oʻtmishda boshlanib hali davom "
                       "etmoqda, shuning uchun Present Perfect.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>At eight o'clock last night Elbek ___ his bicycle.</strong></p>",
        "choices": ["was repairing", "repaired", "has repaired", "repairs"],
        "correct": "was repairing",
        "explanation": "<p><strong>was repairing</strong> is correct — a past moment with the action in "
                       "the middle of happening.<br><br>"
                       "<em>(<strong>was repairing</strong> toʻgʻri — oʻtmishdagi daqiqa va oʻsha paytda "
                       "davom etayotgan harakat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which five tenses do most of the work in real speech?</strong></p>",
        "choices": ["Present Simple, Present Continuous, Past Simple, Present Perfect, will",
                    "The four Perfect Continuous forms and the Past Simple",
                    "Only the three Simple tenses",
                    "Future Perfect Continuous and Past Perfect Continuous"],
        "correct": "Present Simple, Present Continuous, Past Simple, Present Perfect, will",
        "explanation": "<p><strong>Present Simple, Present Continuous, Past Simple, Present Perfect, "
                       "will</strong> is correct — these five carry about 90% of everyday English."
                       "<br><br><em>(<strong>Present Simple, Present Continuous, Past Simple, Present "
                       "Perfect, will</strong> toʻgʻri — kundalik ingliz tilining taxminan 90% shu "
                       "beshtasiga toʻgʻri keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ football every Saturday.</strong></p>",
        "choices": ["plays", "is playing", "has played", "was playing"],
        "correct": "plays",
        "explanation": "<p><strong>plays</strong> is correct — a repeated habit, so the Present "
                       "Simple.<br><br>"
                       "<em>(<strong>plays</strong> toʻgʻri — takrorlanadigan odat, shuning uchun Present "
                       "Simple.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>By this time next year Javohir ___ school.</strong></p>",
        "choices": ["will have left", "will leave", "leaves", "has left"],
        "correct": "will have left",
        "explanation": "<p><strong>will have left</strong> is correct — finished before a future point, "
                       "so the Future Perfect.<br><br>"
                       "<em>(<strong>will have left</strong> toʻgʻri — kelasi nuqtadan oldin tugagan "
                       "boʻladi, shuning uchun Future Perfect.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which pair shows the same aspect in two different times?</strong></p>",
        "choices": ["I am working — I was working", "I work — I am working",
                    "I have worked — I work", "I will work — I have worked"],
        "correct": "I am working — I was working",
        "explanation": "<p><strong>I am working — I was working</strong> is correct — both are "
                       "Continuous, one present and one past. That is the map in action.<br><br>"
                       "<em>(<strong>I am working — I was working</strong> toʻgʻri — ikkisi ham "
                       "Continuous, biri hozirgi, biri oʻtgan zamonda. Xarita aynan shunday "
                       "ishlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda ___ her project when the lights went out.</strong> "
                "Which tense fits the long action?</p>",
        "choices": ["Past Continuous — was finishing", "Past Simple — finished",
                    "Present Perfect — has finished", "Future Simple — will finish"],
        "correct": "Past Continuous — was finishing",
        "explanation": "<p><strong>Past Continuous — was finishing</strong> is correct — the long "
                       "background action, cut by a short Past Simple event.<br><br>"
                       "<em>(<strong>Past Continuous — was finishing</strong> toʻgʻri — uzoq fon "
                       "harakati, uni qisqa Past Simple voqeasi kesib oʻtadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which tense is “Madina has been reading”?</strong></p>",
        "choices": ["Present Perfect Continuous", "Present Perfect",
                    "Past Perfect Continuous", "Present Continuous"],
        "correct": "Present Perfect Continuous",
        "explanation": "<p><strong>Present Perfect Continuous</strong> is correct — "
                       "<em>have / has + been + -ing</em>.<br><br>"
                       "<em>(<strong>Present Perfect Continuous</strong> toʻgʻri — "
                       "<em>have / has + been + -ing</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Abdulloh has finished his homework yesterday.",
                    "Abdulloh finished his homework yesterday.",
                    "Abdulloh has finished his homework.",
                    "Abdulloh had finished his homework before dinner."],
        "correct": "Abdulloh has finished his homework yesterday.",
        "explanation": "<p><strong>Abdulloh has finished his homework yesterday.</strong> is the mistake "
                       "— a dated past time forces the Past Simple.<br><br>"
                       "<em>(<strong>Abdulloh has finished his homework yesterday.</strong> xato — sanasi "
                       "aniq oʻtgan vaqt Past Simple ni talab qiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Sirojiddin will be waiting for you at six.",
                    "Sirojiddin will be wait for you at six.",
                    "Sirojiddin will been waiting for you at six.",
                    "Sirojiddin will waiting for you at six."],
        "correct": "Sirojiddin will be waiting for you at six.",
        "explanation": "<p><strong>Sirojiddin will be waiting for you at six.</strong> is correct — "
                       "Future Continuous: <em>will be + -ing</em>.<br><br>"
                       "<em>(<strong>Sirojiddin will be waiting for you at six.</strong> toʻgʻri — "
                       "Future Continuous: <em>will be + -ing</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> What have you been doing all morning, "
                "Marjona?</p>"
                "<p><strong>Marjona:</strong> ___</p>",
        "choices": ["I've been revising the tenses, and I've finished Block C.",
                    "I revise the tenses, and I have finish Block C.",
                    "I've been revised the tenses, and I finish Block C.",
                    "I am revising the tenses since morning, and I finished Block C."],
        "correct": "I've been revising the tenses, and I've finished Block C.",
        "explanation": "<p><strong>I've been revising … I've finished …</strong> is correct — the "
                       "activity in the Continuous, the completed result in the Simple.<br><br>"
                       "<em>(<strong>I've been revising … I've finished …</strong> toʻgʻri — faoliyat "
                       "Continuous da, tugallangan natija esa Simple da.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> tense is correct.</p>",
        "choices": ["Davron studies here now, he studied in Andijan before, "
                    "and by June he will have studied English for six years.",
                    "Davron is studying here now, he has studied in Andijan before, "
                    "and by June he will study English for six years.",
                    "Davron study here now, he was studying in Andijan before, "
                    "and by June he will have study English for six years.",
                    "Davron has been studying here now, he studies in Andijan before, "
                    "and by June he studies English for six years."],
        "correct": "Davron studies here now, he studied in Andijan before, "
                   "and by June he will have studied English for six years.",
        "explanation": "<p><strong>studies … studied … will have studied</strong> is correct — a present "
                       "fact, a closed past, and a future looking back: three times, one sentence."
                       "<br><br><em>(<strong>studies … studied … will have studied</strong> toʻgʻri — "
                       "hozirgi fakt, yopilgan oʻtmish va kelajakdan orqaga qarash: bitta gapda uch "
                       "zamon.)</em></p>",
    },
]


# =====================================================================
# PE-42 — can, could, be able to: Ability
# =====================================================================

Q_PE42 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Afsona ___ speak three languages.</strong></p>",
        "choices": ["can", "cans", "can to", "is can"],
        "correct": "can",
        "explanation": "<p><strong>can</strong> is correct — modal verbs never take <em>-s</em>, even for "
                       "<em>he / she / it</em>.<br><br>"
                       "<em>(<strong>can</strong> toʻgʻri — modal feʼllar hech qachon <em>-s</em> "
                       "olmaydi, hatto <em>he / she / it</em> uchun ham.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz can ___ very fast.</strong></p>",
        "choices": ["run", "to run", "runs", "running"],
        "correct": "run",
        "explanation": "<p><strong>run</strong> is correct — no <em>to</em> after a modal, and no ending "
                       "on the verb.<br><br>"
                       "<em>(<strong>run</strong> toʻgʻri — modaldan keyin <em>to</em> qoʻyilmaydi, "
                       "feʼlga qoʻshimcha ham qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ you swim, Iroda?</strong></p>",
        "choices": ["Can", "Do", "Are", "Does"],
        "correct": "Can",
        "explanation": "<p><strong>Can</strong> is correct — modals make questions by moving in front of "
                       "the subject, with no <em>do</em>.<br><br>"
                       "<em>(<strong>Can</strong> toʻgʻri — modallar savolni subject oldiga chiqib "
                       "yasaydi, <em>do</em> kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Sherbek ___ drive — he is only fifteen.</strong></p>",
        "choices": ["can't", "doesn't can", "don't can", "not can"],
        "correct": "can't",
        "explanation": "<p><strong>can't</strong> is correct — <em>cannot → can't</em>, with no "
                       "<em>don't</em>.<br><br>"
                       "<em>(<strong>can't</strong> toʻgʻri — <em>cannot → can't</em>, <em>don't</em> "
                       "ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>When Charos was six, she ___ already read.</strong></p>",
        "choices": ["could", "can", "cans", "could to"],
        "correct": "could",
        "explanation": "<p><strong>could</strong> is correct — <em>could</em> is the past of <em>can</em> "
                       "for a general ability.<br><br>"
                       "<em>(<strong>could</strong> toʻgʻri — umumiy qobiliyat uchun <em>could</em> "
                       "<em>can</em> ning oʻtgan zamon shakli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ I open the window, please?</strong></p>",
        "choices": ["Can", "Do", "Am", "Will I can"],
        "correct": "Can",
        "explanation": "<p><strong>Can</strong> is correct — <em>can</em> also asks for permission, not "
                       "only about ability.<br><br>"
                       "<em>(<strong>Can</strong> toʻgʻri — <em>can</em> faqat qobiliyatni emas, ruxsat "
                       "ham soʻraydi.)</em></p>",
    },
    {
        "text": "<p>Choose the more polite option.</p>"
                "<p><strong>___ you help me with this exercise, Rozimurod teacher?</strong></p>",
        "choices": ["Could", "Can", "Do", "Are"],
        "correct": "Could",
        "explanation": "<p><strong>Could</strong> is correct — <em>could</em> makes a request softer and "
                       "more respectful than <em>can</em>.<br><br>"
                       "<em>(<strong>Could</strong> toʻgʻri — <em>could</em> iltimosni <em>can</em> ga "
                       "qaraganda yumshoqroq va hurmatliroq qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ finish the race yesterday, although his leg "
                "hurt.</strong></p>",
        "choices": ["was able to", "can", "could to", "is able"],
        "correct": "was able to",
        "explanation": "<p><strong>was able to</strong> is correct — for one successful action on one "
                       "occasion in the past, English prefers <em>was able to</em> over "
                       "<em>could</em>.<br><br>"
                       "<em>(<strong>was able to</strong> toʻgʻri — oʻtmishda bir marta muvaffaqiyatli "
                       "bajarilgan ish uchun ingliz tili <em>could</em> emas, <em>was able to</em> ni "
                       "afzal koʻradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Next year Elbek ___ drive a car.</strong></p>",
        "choices": ["will be able to", "will can", "can will", "will could"],
        "correct": "will be able to",
        "explanation": "<p><strong>will be able to</strong> is correct — two modals can never stand "
                       "together, so <em>can</em> borrows <em>be able to</em> for the future.<br><br>"
                       "<em>(<strong>will be able to</strong> toʻgʻri — ikki modal yonma-yon kelmaydi, "
                       "shuning uchun kelasi zamonda <em>can</em> <em>be able to</em> dan "
                       "foydalanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs would like ___ swim better.</strong></p>",
        "choices": ["to be able to", "to can", "can", "be able"],
        "correct": "to be able to",
        "explanation": "<p><strong>to be able to</strong> is correct — <em>can</em> has no infinitive, so "
                       "<em>be able to</em> fills the gap.<br><br>"
                       "<em>(<strong>to be able to</strong> toʻgʻri — <em>can</em> ning infinitiv shakli "
                       "yoʻq, shuning uchun uning oʻrnini <em>be able to</em> toʻldiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir has ___ to solve difficult problems since he was ten.</strong></p>",
        "choices": ["been able", "could", "can", "be able"],
        "correct": "been able",
        "explanation": "<p><strong>been able</strong> is correct — after <em>has</em> we need a third "
                       "form, and <em>can</em> does not have one.<br><br>"
                       "<em>(<strong>been able</strong> toʻgʻri — <em>has</em> dan keyin uchinchi shakl "
                       "kerak, <em>can</em> da esa u yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ play the piano when she was five, and she still "
                "plays.</strong></p>",
        "choices": ["could", "can", "was able", "will can"],
        "correct": "could",
        "explanation": "<p><strong>could</strong> is correct — a general ability that lasted over a "
                       "period of the past.<br><br>"
                       "<em>(<strong>could</strong> toʻgʻri — oʻtmishda uzoq davom etgan umumiy "
                       "qobiliyat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is about a <em>single successful moment</em>?</strong></p>",
        "choices": ["Ilgʻor was able to answer the last question in the test.",
                    "Ilgʻor could speak English as a child.",
                    "Ilgʻor can swim well.",
                    "Ilgʻor will be able to drive next year."],
        "correct": "Ilgʻor was able to answer the last question in the test.",
        "explanation": "<p><strong>Ilgʻor was able to answer the last question in the test.</strong> is "
                       "correct — one occasion, and he managed it.<br><br>"
                       "<em>(<strong>Ilgʻor was able to answer the last question in the test.</strong> "
                       "toʻgʻri — bir marta boʻlgan holat va u uddaladi.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Can Shaxzoda cook plov? — Yes, ___ .</strong></p>",
        "choices": ["she can", "she cans", "she does", "she is"],
        "correct": "she can",
        "explanation": "<p><strong>she can</strong> is correct — the short answer repeats the modal, "
                       "unchanged.<br><br>"
                       "<em>(<strong>she can</strong> toʻgʻri — qisqa javobda modal oʻzgarishsiz "
                       "takrorlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh ___ hear the teacher — the classroom was too noisy.</strong></p>",
        "choices": ["couldn't", "can't", "didn't could", "wasn't able"],
        "correct": "couldn't",
        "explanation": "<p><strong>couldn't</strong> is correct — for a past failure both "
                       "<em>couldn't</em> and <em>wasn't able to</em> work, but <em>wasn't able</em> "
                       "without <em>to</em> is wrong.<br><br>"
                       "<em>(<strong>couldn't</strong> toʻgʻri — oʻtmishdagi muvaffaqiyatsizlik uchun "
                       "<em>couldn't</em> ham, <em>wasn't able to</em> ham boʻladi, lekin <em>to</em> siz "
                       "<em>wasn't able</em> xato.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which rule is <em>false</em> for modal verbs?</strong></p>",
        "choices": ["They take -s for he / she / it.",
                    "They are followed by the base verb with no 'to'.",
                    "They make questions by inversion.",
                    "They make negatives with 'not'."],
        "correct": "They take -s for he / she / it.",
        "explanation": "<p><strong>They take -s for he / she / it.</strong> is false — modals never "
                       "change: <em>she can</em>, never <em>she cans</em>.<br><br>"
                       "<em>(<strong>Ular he / she / it uchun -s oladi.</strong> — bu notoʻgʻri. Modallar "
                       "hech qachon oʻzgarmaydi: <em>she can</em>, <em>she cans</em> emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Sirojiddin can to play the guitar.", "Sirojiddin can play the guitar.",
                    "Sirojiddin can't play the guitar.", "Can Sirojiddin play the guitar?"],
        "correct": "Sirojiddin can to play the guitar.",
        "explanation": "<p><strong>Sirojiddin can to play the guitar.</strong> is the mistake — no "
                       "<em>to</em> after a modal.<br><br>"
                       "<em>(<strong>Sirojiddin can to play the guitar.</strong> xato — modaldan keyin "
                       "<em>to</em> qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Marjona will be able to join us tomorrow.",
                    "Marjona will can join us tomorrow.",
                    "Marjona will be able join us tomorrow.",
                    "Marjona can will join us tomorrow."],
        "correct": "Marjona will be able to join us tomorrow.",
        "explanation": "<p><strong>Marjona will be able to join us tomorrow.</strong> is correct — one "
                       "modal only, and <em>be able to</em> keeps its <em>to</em>.<br><br>"
                       "<em>(<strong>Marjona will be able to join us tomorrow.</strong> toʻgʻri — faqat "
                       "bitta modal, <em>be able to</em> esa <em>to</em> ni saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Did you manage to translate the whole "
                "text, Davron?</p>"
                "<p><strong>Davron:</strong> ___</p>",
        "choices": ["Yes, I was able to finish it in an hour.",
                    "Yes, I could to finish it in an hour.",
                    "Yes, I can finished it in an hour.",
                    "Yes, I was able finish it in an hour."],
        "correct": "Yes, I was able to finish it in an hour.",
        "explanation": "<p><strong>Yes, I was able to finish it in an hour.</strong> is correct — one "
                       "successful past occasion, with the full <em>was able to</em>.<br><br>"
                       "<em>(<strong>Yes, I was able to finish it in an hour.</strong> toʻgʻri — "
                       "oʻtmishda bir marta muvaffaqiyatli bajarilgan ish, toʻliq <em>was able to</em> "
                       "bilan.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Behruz can swim now, he couldn't swim two years ago, "
                    "and next summer he will be able to swim across the river.",
                    "Behruz cans swim now, he couldn't to swim two years ago, "
                    "and next summer he will can swim across the river.",
                    "Behruz can to swim now, he can't swim two years ago, "
                    "and next summer he will be able swim across the river.",
                    "Behruz can swim now, he didn't could swim two years ago, "
                    "and next summer he can will swim across the river."],
        "correct": "Behruz can swim now, he couldn't swim two years ago, "
                   "and next summer he will be able to swim across the river.",
        "explanation": "<p><strong>can … couldn't … will be able to …</strong> is correct — present, "
                       "past and future ability, each in its proper form.<br><br>"
                       "<em>(<strong>can … couldn't … will be able to …</strong> toʻgʻri — hozirgi, "
                       "oʻtgan va kelasi zamondagi qobiliyat, har biri oʻz shaklida.)</em></p>",
    },
]


# =====================================================================
# PE-43 — may, might, could: Possibility
# =====================================================================

Q_PE43 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sherbek ___ come to the party — he hasn't decided yet.</strong></p>",
        "choices": ["may", "will", "won't", "mays"],
        "correct": "may",
        "explanation": "<p><strong>may</strong> is correct — about 50% certainty: perhaps yes, perhaps "
                       "no.<br><br>"
                       "<em>(<strong>may</strong> toʻgʻri — taxminan 50% ishonch: balki ha, balki "
                       "yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Look at those clouds — it ___ rain this evening.</strong></p>",
        "choices": ["might", "must", "can", "will certainly not"],
        "correct": "might",
        "explanation": "<p><strong>might</strong> is correct — an honest maybe, weaker than "
                       "<em>will</em>.<br><br>"
                       "<em>(<strong>might</strong> toʻgʻri — samimiy “balki”, <em>will</em> dan "
                       "kuchsizroq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which modal shows 100% certainty about the future?</strong></p>",
        "choices": ["will", "might", "may", "could"],
        "correct": "will",
        "explanation": "<p><strong>will</strong> is correct — the top of the scale: "
                       "<em>will</em> 100% → <em>should</em> 70% → <em>may / might / could</em> 50% → "
                       "<em>won't</em> 0%.<br><br>"
                       "<em>(<strong>will</strong> toʻgʻri — shkalaning eng tepasi: <em>will</em> 100% → "
                       "<em>should</em> 70% → <em>may / might / could</em> 50% → <em>won't</em> "
                       "0%.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda ___ be at home — I saw her leave ten minutes ago.</strong></p>",
        "choices": ["might not", "might", "may", "could"],
        "correct": "might not",
        "explanation": "<p><strong>might not</strong> is correct — the evidence makes it unlikely, but "
                       "not impossible.<br><br>"
                       "<em>(<strong>might not</strong> toʻgʻri — dalil buni ehtimoldan yiroq qiladi, "
                       "lekin butunlay inkor etmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ know the answer — she read the whole chapter.</strong></p>",
        "choices": ["may", "mays", "may to", "is may"],
        "correct": "may",
        "explanation": "<p><strong>may</strong> is correct — like every modal it never changes and takes "
                       "the base verb.<br><br>"
                       "<em>(<strong>may</strong> toʻgʻri — har qanday modal kabi u ham oʻzgarmaydi va "
                       "asosiy feʼl oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ be in the library — he sometimes studies there.</strong></p>",
        "choices": ["could", "can", "could to", "cans"],
        "correct": "could",
        "explanation": "<p><strong>could</strong> is correct — here <em>could</em> means possibility, not "
                       "past ability. <em>Can</em> would not fit: <em>He can be in the library</em> means "
                       "something different.<br><br>"
                       "<em>(<strong>could</strong> toʻgʻri — bu yerda <em>could</em> ehtimolni "
                       "bildiradi, oʻtmish qobiliyatini emas. <em>Can</em> mos kelmaydi: <em>He can be in "
                       "the library</em> boshqa maʼno beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Elbek ___ come tomorrow — his mother is ill.</strong></p>",
        "choices": ["might not", "mightn't to", "don't might", "doesn't might"],
        "correct": "might not",
        "explanation": "<p><strong>might not</strong> is correct — modals take <em>not</em> directly, with "
                       "no helper.<br><br>"
                       "<em>(<strong>might not</strong> toʻgʻri — modallar <em>not</em> ni toʻgʻridan "
                       "toʻgʻri oladi, yordamchi kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference between <em>might not</em> and "
                "<em>couldn't</em>?</strong></p>",
        "choices": ["might not = perhaps not · couldn't = impossible",
                    "might not = impossible · couldn't = perhaps not",
                    "They mean exactly the same.",
                    "Both mean 100% certain."],
        "correct": "might not = perhaps not · couldn't = impossible",
        "explanation": "<p><strong>might not = perhaps not · couldn't = impossible</strong> is correct — "
                       "<em>couldn't</em> is much stronger: <em>That couldn't be Firdavs — he's in "
                       "Tashkent</em>.<br><br>"
                       "<em>(<strong>might not = balki yoʻq · couldn't = mumkin emas</strong> toʻgʻri — "
                       "<em>couldn't</em> ancha kuchli: <em>That couldn't be Firdavs — he's in "
                       "Tashkent</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ Javohir will pass the exam.</strong></p>",
        "choices": ["Maybe", "May be", "May", "Might"],
        "correct": "Maybe",
        "explanation": "<p><strong>Maybe</strong> is correct — one word, an adverb, usually at the start "
                       "of the sentence. <em>May be</em> (two words) is a verb: <em>He may be "
                       "late</em>.<br><br>"
                       "<em>(<strong>Maybe</strong> toʻgʻri — bitta soʻz, ravish, odatda gap boshida "
                       "keladi. <em>May be</em> (ikki soʻz) esa feʼl: <em>He may be late</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ late — the traffic is terrible today.</strong></p>",
        "choices": ["may be", "maybe", "may being", "maybe be"],
        "correct": "may be",
        "explanation": "<p><strong>may be</strong> is correct — modal + <em>be</em>, two separate words."
                       "<br><br><em>(<strong>may be</strong> toʻgʻri — modal + <em>be</em>, ikkita "
                       "alohida soʻz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The parcel ___ arrive today — the shop promised Tuesday.</strong></p>",
        "choices": ["should", "must", "might not", "won't"],
        "correct": "should",
        "explanation": "<p><strong>should</strong> is correct — around 70%: you expect it, based on what "
                       "you were told.<br><br>"
                       "<em>(<strong>should</strong> toʻgʻri — taxminan 70%: sizga aytilganiga asoslanib "
                       "buni kutasiz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is the <em>least</em> certain?</strong></p>",
        "choices": ["Shaxzoda might come.", "Shaxzoda will come.",
                    "Shaxzoda should come.", "Shaxzoda is coming."],
        "correct": "Shaxzoda might come.",
        "explanation": "<p><strong>Shaxzoda might come.</strong> is correct — <em>might</em> sits at "
                       "about 50%, below <em>should</em> and far below <em>will</em>.<br><br>"
                       "<em>(<strong>Shaxzoda might come.</strong> toʻgʻri — <em>might</em> taxminan 50% "
                       "da, <em>should</em> dan past va <em>will</em> dan ancha past.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh ___ be at the stadium — I'm not sure.</strong></p>",
        "choices": ["might", "will certainly", "must", "can"],
        "correct": "might",
        "explanation": "<p><strong>might</strong> is correct — <em>I'm not sure</em> puts the sentence "
                       "firmly in the middle of the scale.<br><br>"
                       "<em>(<strong>might</strong> toʻgʻri — <em>I'm not sure</em> gapni shkalaning "
                       "aynan oʻrtasiga joylashtiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ I ask you a question, Rozimurod teacher?</strong></p>",
        "choices": ["May", "Might to", "Could to", "May to"],
        "correct": "May",
        "explanation": "<p><strong>May</strong> is correct — <em>May I …?</em> is the most formal and "
                       "polite way to ask permission.<br><br>"
                       "<em>(<strong>May</strong> toʻgʻri — <em>May I …?</em> ruxsat soʻrashning eng "
                       "rasmiy va xushmuomala shakli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin ___ be tired — he has been working since morning.</strong></p>",
        "choices": ["may well", "may to", "mays", "is may"],
        "correct": "may well",
        "explanation": "<p><strong>may well</strong> is correct — <em>may well</em> raises the "
                       "probability: “it is quite likely”.<br><br>"
                       "<em>(<strong>may well</strong> toʻgʻri — <em>may well</em> ehtimolni oshiradi: "
                       "“ancha ehtimol”.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Marjona ___ be in the yard, or she ___ have gone home.</strong></p>",
        "choices": ["might … might", "might … must", "will … might", "can … may not"],
        "correct": "might … might",
        "explanation": "<p><strong>might … might</strong> is correct — two equally possible options, so "
                       "the same modal fits both.<br><br>"
                       "<em>(<strong>might … might</strong> toʻgʻri — bir xil ehtimoldagi ikki variant, "
                       "shuning uchun ikkalasiga ham bitta modal mos keladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Ilgʻor might to be at home.", "Ilgʻor might be at home.",
                    "Ilgʻor may be at home.", "Ilgʻor could be at home."],
        "correct": "Ilgʻor might to be at home.",
        "explanation": "<p><strong>Ilgʻor might to be at home.</strong> is the mistake — no <em>to</em> "
                       "after a modal.<br><br>"
                       "<em>(<strong>Ilgʻor might to be at home.</strong> xato — modaldan keyin "
                       "<em>to</em> qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["It may not be true, but I heard it from Behruz.",
                    "It doesn't may be true, but I heard it from Behruz.",
                    "It may not to be true, but I heard it from Behruz.",
                    "It not may be true, but I heard it from Behruz."],
        "correct": "It may not be true, but I heard it from Behruz.",
        "explanation": "<p><strong>It may not be true …</strong> is correct — <em>not</em> goes straight "
                       "after the modal.<br><br>"
                       "<em>(<strong>It may not be true …</strong> toʻgʻri — <em>not</em> modaldan keyin "
                       "darhol keladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Davron:</strong> Will Charos come to the match?</p>"
                "<p><strong>Iroda:</strong> ___</p>",
        "choices": ["She might — she hasn't decided yet.",
                    "She might to — she hasn't decided yet.",
                    "Maybe she will comes — she hasn't decided yet.",
                    "She may to come — she hasn't decided yet."],
        "correct": "She might — she hasn't decided yet.",
        "explanation": "<p><strong>She might — she hasn't decided yet.</strong> is correct — a modal can "
                       "stand alone at the end of a short answer, with the verb understood.<br><br>"
                       "<em>(<strong>She might — she hasn't decided yet.</strong> toʻgʻri — qisqa javob "
                       "oxirida modal yolgʻiz turishi mumkin, feʼl esa tushunib olinadi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Maybe Afsona is ill; she may be at home, but she might not answer the phone.",
                    "May be Afsona is ill; she maybe at home, but she might not to answer the phone.",
                    "Maybe Afsona is ill; she maybe at home, but she doesn't might answer the phone.",
                    "May be Afsona is ill; she may be at home, but she mightn't to answer the phone."],
        "correct": "Maybe Afsona is ill; she may be at home, but she might not answer the phone.",
        "explanation": "<p><strong>Maybe … may be … might not …</strong> is correct — the adverb as one "
                       "word, the modal + <em>be</em> as two, and <em>not</em> straight after the "
                       "modal.<br><br>"
                       "<em>(<strong>Maybe … may be … might not …</strong> toʻgʻri — ravish bitta soʻz, "
                       "modal + <em>be</em> ikkita, <em>not</em> esa modaldan keyin darhol "
                       "keladi.)</em></p>",
    },
]


# =====================================================================
# PE-44 — must, have to, need to: Obligation
# =====================================================================

Q_PE44 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ call my grandmother today — I promised her.</strong></p>",
        "choices": ["must", "have to be", "musts", "must to"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — the necessity comes from inside the "
                       "speaker: his own promise.<br><br>"
                       "<em>(<strong>must</strong> toʻgʻri — zarurat gapiruvchining oʻzidan kelib "
                       "chiqadi: oʻz vaʼdasidan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ wear a uniform — it is the school rule.</strong></p>",
        "choices": ["has to", "must to", "have to", "musts"],
        "correct": "has to",
        "explanation": "<p><strong>has to</strong> is correct — the obligation comes from outside, and "
                       "<em>have to</em> changes for <em>he / she / it</em>.<br><br>"
                       "<em>(<strong>has to</strong> toʻgʻri — majburiyat tashqaridan keladi, "
                       "<em>have to</em> esa <em>he / she / it</em> uchun oʻzgaradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference between <em>must</em> and <em>have to</em>?</strong></p>",
        "choices": ["must = I decide · have to = somebody else decides",
                    "must = somebody else decides · have to = I decide",
                    "They are always identical.",
                    "must is past, have to is present."],
        "correct": "must = I decide · have to = somebody else decides",
        "explanation": "<p><strong>must = I decide · have to = somebody else decides</strong> is correct "
                       "— the difference is where the pressure comes from.<br><br>"
                       "<em>(<strong>must = men qaror qilaman · have to = boshqa kimdir qaror "
                       "qiladi</strong> toʻgʻri — farq bosim qayerdan kelishida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Passengers ___ wear a seatbelt.</strong> (a written rule)</p>",
        "choices": ["must", "have to be", "musts", "are must"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — written rules and notices use <em>must</em>, "
                       "because the writer is the authority.<br><br>"
                       "<em>(<strong>must</strong> toʻgʻri — yozma qoida va eʼlonlarda <em>must</em> "
                       "ishlatiladi, chunki yozgan odam — hokimiyat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Yesterday Iroda ___ stay at school until five.</strong></p>",
        "choices": ["had to", "must", "musted", "must have"],
        "correct": "had to",
        "explanation": "<p><strong>had to</strong> is correct — <em>must</em> has no past of its own, so "
                       "it borrows <em>had to</em>.<br><br>"
                       "<em>(<strong>had to</strong> toʻgʻri — <em>must</em> ning oʻz oʻtgan zamon shakli "
                       "yoʻq, shuning uchun u <em>had to</em> dan foydalanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Next week Charos ___ take three exams.</strong></p>",
        "choices": ["will have to", "will must", "must will", "musts"],
        "correct": "will have to",
        "explanation": "<p><strong>will have to</strong> is correct — <em>must</em> has no future either, "
                       "and two modals never stand together.<br><br>"
                       "<em>(<strong>will have to</strong> toʻgʻri — <em>must</em> ning kelasi zamon "
                       "shakli ham yoʻq, ikki modal esa yonma-yon kelmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ Samandar have to work on Saturdays?</strong></p>",
        "choices": ["Does", "Do", "Must", "Is"],
        "correct": "Does",
        "explanation": "<p><strong>Does</strong> is correct — <em>have to</em> is an ordinary verb, so it "
                       "needs <em>do / does</em>, unlike the modals.<br><br>"
                       "<em>(<strong>Does</strong> toʻgʻri — <em>have to</em> oddiy feʼl, shuning uchun "
                       "modallardan farqli oʻlaroq <em>do / does</em> talab qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek ___ finish this exercise before the bell.</strong></p>",
        "choices": ["needs to", "need to", "needs", "need"],
        "correct": "needs to",
        "explanation": "<p><strong>needs to</strong> is correct — used as an ordinary verb, <em>need "
                       "to</em> takes <em>-s</em> for one person.<br><br>"
                       "<em>(<strong>needs to</strong> toʻgʻri — oddiy feʼl sifatida <em>need to</em> "
                       "bitta shaxs uchun <em>-s</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ buy a new notebook — his old one is full.</strong></p>",
        "choices": ["has to", "must to", "have to", "is have to"],
        "correct": "has to",
        "explanation": "<p><strong>has to</strong> is correct — the circumstances, not his own wish, "
                       "create the necessity.<br><br>"
                       "<em>(<strong>has to</strong> toʻgʻri — zaruratni uning xohishi emas, vaziyat "
                       "yaratmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence shows the speaker's <em>own</em> decision?</strong></p>",
        "choices": ["I must start getting up earlier.",
                    "I have to wear a uniform at school.",
                    "We have to pay for the tickets.",
                    "Javohir has to take the bus."],
        "correct": "I must start getting up earlier.",
        "explanation": "<p><strong>I must start getting up earlier.</strong> is correct — nobody is "
                       "forcing him; it is his own resolution.<br><br>"
                       "<em>(<strong>I must start getting up earlier.</strong> toʻgʻri — uni hech kim "
                       "majburlamayapti; bu — uning oʻz qarori.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher says we ___ hand in the essays on Monday.</strong></p>",
        "choices": ["must", "must to", "musts", "are must"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — the teacher is the authority giving the "
                       "instruction.<br><br>"
                       "<em>(<strong>must</strong> toʻgʻri — koʻrsatma berayotgan hokimiyat — "
                       "oʻqituvchi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ get up at six because her bus leaves at seven.</strong></p>",
        "choices": ["has to", "must to", "have to", "musts"],
        "correct": "has to",
        "explanation": "<p><strong>has to</strong> is correct — the timetable decides, not Madina."
                       "<br><br><em>(<strong>has to</strong> toʻgʻri — Madina emas, jadval qaror "
                       "qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda ___ study last night because of the test.</strong></p>",
        "choices": ["had to", "must", "have to", "has to"],
        "correct": "had to",
        "explanation": "<p><strong>had to</strong> is correct — the one past form serves both <em>must</em> "
                       "and <em>have to</em>.<br><br>"
                       "<em>(<strong>had to</strong> toʻgʻri — bitta oʻtgan zamon shakli ham "
                       "<em>must</em>, ham <em>have to</em> uchun xizmat qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ we bring our dictionaries tomorrow?</strong></p>",
        "choices": ["Do we have to", "Have we to must", "Must we to", "Does we must"],
        "correct": "Do we have to",
        "explanation": "<p><strong>Do we have to</strong> is correct — the natural everyday question. "
                       "<em>Must we …?</em> is possible but sounds formal and rather strong.<br><br>"
                       "<em>(<strong>Do we have to</strong> toʻgʻri — kundalik nutqdagi tabiiy savol. "
                       "<em>Must we …?</em> ham mumkin, lekin rasmiy va qatʼiy eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh ___ take a taxi — there were no buses.</strong></p>",
        "choices": ["had to", "must", "has to", "needs to"],
        "correct": "had to",
        "explanation": "<p><strong>had to</strong> is correct — a past necessity created by the "
                       "circumstances.<br><br>"
                       "<em>(<strong>had to</strong> toʻgʻri — vaziyat yaratgan oʻtmishdagi "
                       "zarurat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Sirojiddin ___ wear a tie at school, and next year he ___ wear one at "
                "college too.</strong></p>",
        "choices": ["has to … will have to", "must to … will must",
                    "have to … will have to", "has to … will must"],
        "correct": "has to … will have to",
        "explanation": "<p><strong>has to … will have to</strong> is correct — an outside rule now and an "
                       "outside rule later, and <em>must</em> cannot follow <em>will</em>.<br><br>"
                       "<em>(<strong>has to … will have to</strong> toʻgʻri — hozir ham, keyin ham "
                       "tashqi qoida, <em>must</em> esa <em>will</em> dan keyin kela olmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Marjona must to finish her project.", "Marjona must finish her project.",
                    "Marjona has to finish her project.", "Marjona needs to finish her project."],
        "correct": "Marjona must to finish her project.",
        "explanation": "<p><strong>Marjona must to finish her project.</strong> is the mistake — "
                       "<em>must</em> is a modal, so no <em>to</em>. But <em>have to</em> and <em>need "
                       "to</em> keep their <em>to</em>.<br><br>"
                       "<em>(<strong>Marjona must to finish her project.</strong> xato — <em>must</em> "
                       "modal, shuning uchun <em>to</em> qoʻyilmaydi. <em>Have to</em> va <em>need "
                       "to</em> esa <em>to</em> ni saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Davron had to leave early yesterday.", "Davron musted leave early yesterday.",
                    "Davron must left early yesterday.", "Davron has to leave early yesterday."],
        "correct": "Davron had to leave early yesterday.",
        "explanation": "<p><strong>Davron had to leave early yesterday.</strong> is correct — the past of "
                       "obligation is always <em>had to</em>.<br><br>"
                       "<em>(<strong>Davron had to leave early yesterday.</strong> toʻgʻri — "
                       "majburiyatning oʻtgan zamoni doim <em>had to</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Why were you absent yesterday, Ilgʻor?</p>"
                "<p><strong>Ilgʻor:</strong> ___</p>",
        "choices": ["I had to take my little sister to the doctor.",
                    "I must take my little sister to the doctor.",
                    "I have to took my little sister to the doctor.",
                    "I musted take my little sister to the doctor."],
        "correct": "I had to take my little sister to the doctor.",
        "explanation": "<p><strong>I had to take my little sister to the doctor.</strong> is correct — a "
                       "past obligation coming from the circumstances.<br><br>"
                       "<em>(<strong>I had to take my little sister to the doctor.</strong> toʻgʻri — "
                       "vaziyatdan kelib chiqqan oʻtmishdagi majburiyat.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["I must revise tonight, we have to hand in the essay tomorrow, "
                    "and last week we had to write two of them.",
                    "I must to revise tonight, we must hand in the essay tomorrow, "
                    "and last week we musted write two of them.",
                    "I have to revise tonight, we must to hand in the essay tomorrow, "
                    "and last week we have to write two of them.",
                    "I must revise tonight, we has to hand in the essay tomorrow, "
                    "and last week we must have write two of them."],
        "correct": "I must revise tonight, we have to hand in the essay tomorrow, "
                   "and last week we had to write two of them.",
        "explanation": "<p><strong>must … have to … had to …</strong> is correct — my own decision, an "
                       "outside rule, and the past that serves them both.<br><br>"
                       "<em>(<strong>must … have to … had to …</strong> toʻgʻri — oʻz qarorim, tashqi "
                       "qoida va ikkisiga ham xizmat qiladigan oʻtgan zamon.)</em></p>",
    },
]


# =====================================================================
# PE-45 — mustn't vs don't have to
# =====================================================================

Q_PE45 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>You ___ use your phone in the exam — it is forbidden.</strong></p>",
        "choices": ["mustn't", "don't have to", "needn't", "haven't to"],
        "correct": "mustn't",
        "explanation": "<p><strong>mustn't</strong> is correct — <em>mustn't</em> means it is "
                       "prohibited.<br><br>"
                       "<em>(<strong>mustn't</strong> toʻgʻri — <em>mustn't</em> taqiqlanganini "
                       "bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>You ___ come if you're tired — it's up to you.</strong></p>",
        "choices": ["don't have to", "mustn't", "can't", "may not"],
        "correct": "don't have to",
        "explanation": "<p><strong>don't have to</strong> is correct — there is no obligation; the choice "
                       "is yours.<br><br>"
                       "<em>(<strong>don't have to</strong> toʻgʻri — majburiyat yoʻq; tanlov "
                       "sizniki.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does <em>mustn't</em> mean?</strong></p>",
        "choices": ["It is forbidden.", "It is optional.",
                    "It is not necessary.", "It is certain."],
        "correct": "It is forbidden.",
        "explanation": "<p><strong>It is forbidden.</strong> is correct — and that is the opposite of "
                       "<em>don't have to</em>, which means it is optional.<br><br>"
                       "<em>(<strong>Taqiqlangan.</strong> toʻgʻri — bu <em>don't have to</em> ning "
                       "aksi, u esa “ixtiyoriy” degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Children ___ play with matches.</strong></p>",
        "choices": ["mustn't", "don't have to", "needn't", "may"],
        "correct": "mustn't",
        "explanation": "<p><strong>mustn't</strong> is correct — a firm prohibition, for safety.<br><br>"
                       "<em>(<strong>mustn't</strong> toʻgʻri — xavfsizlik uchun qatʼiy "
                       "taqiq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ wear a uniform on Fridays — we can wear what we like.</strong></p>",
        "choices": ["don't have to", "mustn't", "can't", "aren't allowed to"],
        "correct": "don't have to",
        "explanation": "<p><strong>don't have to</strong> is correct — the second half explains that it "
                       "is a free choice.<br><br>"
                       "<em>(<strong>don't have to</strong> toʻgʻri — gapning ikkinchi qismi buning erkin "
                       "tanlov ekanini tushuntiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda ___ pay for the ticket — the concert is free.</strong></p>",
        "choices": ["doesn't have to", "mustn't", "can't", "isn't allowed to"],
        "correct": "doesn't have to",
        "explanation": "<p><strong>doesn't have to</strong> is correct — no obligation. <em>Mustn't "
                       "pay</em> would strangely mean paying is forbidden.<br><br>"
                       "<em>(<strong>doesn't have to</strong> toʻgʻri — majburiyat yoʻq. <em>Mustn't "
                       "pay</em> desa, toʻlash taqiqlangan degan gʻalati maʼno chiqadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>You ___ take photos in the museum — look at the sign.</strong></p>",
        "choices": ["mustn't", "don't have to", "needn't", "don't need"],
        "correct": "mustn't",
        "explanation": "<p><strong>mustn't</strong> is correct — the sign forbids it.<br><br>"
                       "<em>(<strong>mustn't</strong> toʻgʻri — belgi buni taqiqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ come to the extra lesson, but he wants to.</strong></p>",
        "choices": ["doesn't have to", "mustn't", "can't", "may not"],
        "correct": "doesn't have to",
        "explanation": "<p><strong>doesn't have to</strong> is correct — nothing obliges him; he comes by "
                       "choice.<br><br>"
                       "<em>(<strong>doesn't have to</strong> toʻgʻri — uni hech narsa majburlamaydi; u "
                       "oʻz xohishi bilan keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How do you say <em>mustn't</em> in the past?</strong></p>",
        "choices": ["wasn't allowed to", "mustn't have", "didn't must", "hadn't to"],
        "correct": "wasn't allowed to",
        "explanation": "<p><strong>wasn't allowed to</strong> is correct — <em>mustn't</em> has no past "
                       "form, so English uses <em>wasn't / weren't allowed to</em> or <em>couldn't</em>."
                       "<br><br><em>(<strong>wasn't allowed to</strong> toʻgʻri — <em>mustn't</em> ning "
                       "oʻtgan zamon shakli yoʻq, shuning uchun <em>wasn't / weren't allowed to</em> yoki "
                       "<em>couldn't</em> ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ work yesterday — it was a holiday.</strong></p>",
        "choices": ["didn't have to", "mustn't", "wasn't allowed to", "hadn't to"],
        "correct": "didn't have to",
        "explanation": "<p><strong>didn't have to</strong> is correct — the past of “no obligation”."
                       "<br><br><em>(<strong>didn't have to</strong> toʻgʻri — “majburiyat yoʻq” ning "
                       "oʻtgan zamoni.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence means the same as “You mustn't smoke here”?</strong></p>",
        "choices": ["You are not allowed to smoke here.",
                    "You don't need to smoke here.",
                    "You don't have to smoke here.",
                    "You needn't smoke here."],
        "correct": "You are not allowed to smoke here.",
        "explanation": "<p><strong>You are not allowed to smoke here.</strong> is correct — English also "
                       "forbids things with <em>can't</em>, <em>may not</em> and <em>not allowed "
                       "to</em>.<br><br>"
                       "<em>(<strong>You are not allowed to smoke here.</strong> toʻgʻri — ingliz tili "
                       "taqiqni <em>can't</em>, <em>may not</em> va <em>not allowed to</em> bilan ham "
                       "ifodalaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ hurry — there is plenty of time.</strong></p>",
        "choices": ["doesn't have to", "mustn't", "isn't allowed to", "can't"],
        "correct": "doesn't have to",
        "explanation": "<p><strong>doesn't have to</strong> is correct — plenty of time means hurrying is "
                       "unnecessary, not forbidden.<br><br>"
                       "<em>(<strong>doesn't have to</strong> toʻgʻri — vaqt koʻp, yaʼni shoshilish "
                       "shart emas, taqiqlangan emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek ___ be late again — Rozimurod teacher warned him twice.</strong></p>",
        "choices": ["mustn't", "doesn't have to", "needn't", "doesn't need to"],
        "correct": "mustn't",
        "explanation": "<p><strong>mustn't</strong> is correct — after two warnings it is now "
                       "forbidden.<br><br>"
                       "<em>(<strong>mustn't</strong> toʻgʻri — ikki marta ogohlantirilgandan keyin bu "
                       "endi taqiq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which one means “it is not necessary”?</strong></p>",
        "choices": ["needn't", "mustn't", "may not", "can't"],
        "correct": "needn't",
        "explanation": "<p><strong>needn't</strong> is correct — <em>needn't</em> = <em>don't have "
                       "to</em>. The other three all forbid.<br><br>"
                       "<em>(<strong>needn't</strong> toʻgʻri — <em>needn't</em> = <em>don't have "
                       "to</em>. Qolgan uchtasi taqiqni bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>You ___ touch that wire, but you ___ wear gloves if you don't want "
                "to.</strong></p>",
        "choices": ["mustn't … don't have to", "don't have to … mustn't",
                    "mustn't … mustn't", "don't have to … don't have to"],
        "correct": "mustn't … don't have to",
        "explanation": "<p><strong>mustn't … don't have to</strong> is correct — danger forbids the "
                       "first, choice governs the second.<br><br>"
                       "<em>(<strong>mustn't … don't have to</strong> toʻgʻri — birinchisini xavf "
                       "taqiqlaydi, ikkinchisi esa tanlovga bogʻliq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ answer that question — it isn't in the exam.</strong></p>",
        "choices": ["doesn't have to", "mustn't", "isn't allowed to", "may not"],
        "correct": "doesn't have to",
        "explanation": "<p><strong>doesn't have to</strong> is correct — the question is simply not "
                       "required.<br><br>"
                       "<em>(<strong>doesn't have to</strong> toʻgʻri — bu savol shunchaki talab "
                       "qilinmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake in meaning</strong>?</p>",
        "choices": ["The library is free, so you mustn't pay.",
                    "The library is free, so you don't have to pay.",
                    "You mustn't shout in the library.",
                    "You don't have to whisper, but please be quiet."],
        "correct": "The library is free, so you mustn't pay.",
        "explanation": "<p><strong>The library is free, so you mustn't pay.</strong> is the mistake — it "
                       "says paying is forbidden. The meaning needed is <em>don't have to</em>.<br><br>"
                       "<em>(<strong>The library is free, so you mustn't pay.</strong> xato — bu toʻlash "
                       "taqiqlangan degani. Kerakli maʼno esa <em>don't have to</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Javohir didn't have to bring his dictionary yesterday.",
                    "Javohir mustn't bring his dictionary yesterday.",
                    "Javohir didn't must bring his dictionary yesterday.",
                    "Javohir hadn't to bring his dictionary yesterday."],
        "correct": "Javohir didn't have to bring his dictionary yesterday.",
        "explanation": "<p><strong>Javohir didn't have to bring his dictionary yesterday.</strong> is "
                       "correct — <em>have to</em> uses <em>didn't</em> in the past like any ordinary "
                       "verb.<br><br>"
                       "<em>(<strong>Javohir didn't have to bring his dictionary yesterday.</strong> "
                       "toʻgʻri — <em>have to</em> oʻtgan zamonda har qanday oddiy feʼl kabi "
                       "<em>didn't</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Madina:</strong> Do I need to write the date on every page?</p>"
                "<p><strong>Rozimurod teacher:</strong> ___</p>",
        "choices": ["No, you don't have to — only on the first one.",
                    "No, you mustn't — only on the first one.",
                    "No, you aren't allowed to — only on the first one.",
                    "No, you can't — only on the first one."],
        "correct": "No, you don't have to — only on the first one.",
        "explanation": "<p><strong>No, you don't have to — only on the first one.</strong> is correct — "
                       "it is unnecessary, not forbidden. <em>Mustn't</em> would tell her writing the "
                       "date is against the rules.<br><br>"
                       "<em>(<strong>No, you don't have to — only on the first one.</strong> toʻgʻri — "
                       "bu shart emas, taqiqlangan emas. <em>Mustn't</em> desa, sana yozish qoidaga zid "
                       "degan maʼno chiqadi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>both</strong> meanings are correct.</p>",
        "choices": ["You mustn't cheat in the test, but you don't have to answer in order.",
                    "You don't have to cheat in the test, but you mustn't answer in order.",
                    "You mustn't cheat in the test, but you mustn't answer in order.",
                    "You don't have to cheat in the test, but you aren't allowed to answer "
                    "in order."],
        "correct": "You mustn't cheat in the test, but you don't have to answer in order.",
        "explanation": "<p><strong>mustn't cheat … don't have to answer in order</strong> is correct — "
                       "cheating is forbidden, the order of answers is free.<br><br>"
                       "<em>(<strong>mustn't cheat … don't have to answer in order</strong> toʻgʻri — "
                       "koʻchirish taqiqlangan, javoblar tartibi esa erkin.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-41 Practice: The 12 Tenses: The Complete Map",
        "tutorial":    "PE-41:",
        "description": "PE-41 darsiga 20 savol: 3 zamon × 4 aspekt tizimi, har bir aspektning "
                       "maʼnosi, zamonlarni nomlash va bir gapda bir necha zamonni toʻgʻri "
                       "ishlatish. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE41,
    },
    {
        "title":       "PE-42 Practice: can, could, be able to: Ability",
        "tutorial":    "PE-42:",
        "description": "PE-42 darsiga 20 savol: modal feʼllarning toʻrt qoidasi, can va could, "
                       "hamda will be able to / was able to kabi majburiy shakllar. Javoblar ingliz "
                       "va oʻzbek tilida izohlangan.",
        "questions":   Q_PE42,
    },
    {
        "title":       "PE-43 Practice: may, might, could: Possibility",
        "tutorial":    "PE-43:",
        "description": "PE-43 darsiga 20 savol: ishonch shkalasi (will → should → may/might/could → "
                       "won't), inkor shakllari va maybe / may be tuzogʻi. Javoblar ingliz va oʻzbek "
                       "tilida izohlangan.",
        "questions":   Q_PE43,
    },
    {
        "title":       "PE-44 Practice: must, have to, need to: Obligation",
        "tutorial":    "PE-44:",
        "description": "PE-44 darsiga 20 savol: ichkaridan kelgan must va tashqaridan kelgan have "
                       "to, must ning oʻtgan va kelasi zamoni (had to, will have to) hamda savol "
                       "shakllari. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE44,
    },
    {
        "title":       "PE-45 Practice: mustn't vs don't have to: The Dangerous Pair",
        "tutorial":    "PE-45:",
        "description": "PE-45 darsiga 20 savol: mustn't (taqiq) va don't have to (ixtiyoriy) "
                       "farqi, ularning oʻtgan zamon shakllari va taqiqning boshqa yoʻllari. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE45,
    },
]
