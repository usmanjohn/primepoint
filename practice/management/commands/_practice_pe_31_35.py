# -*- coding: utf-8 -*-
"""Prime English practices — PE-31 … PE-35.

End of Block B (time expressions) and the start of Block C, the perfect tenses.
Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_31_35.py --master=prime --expect-questions=20
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
# PE-31 — Time Expressions: ago, for, since, by, until
# =====================================================================

Q_PE31 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Davron's family moved to this city three years ___ .</strong></p>",
        "choices": ["ago", "before", "since", "for"],
        "correct": "ago",
        "explanation": "<p><strong>ago</strong> is correct — it counts backwards from now and always "
                       "comes <em>after</em> the period of time.<br><br>"
                       "<em>(<strong>ago</strong> toʻgʻri — u hozirgi paytdan orqaga sanaydi va doim "
                       "vaqt ifodasidan <em>keyin</em> keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda has studied Korean ___ two years.</strong></p>",
        "choices": ["for", "since", "ago", "during"],
        "correct": "for",
        "explanation": "<p><strong>for</strong> is correct — it answers <em>How long?</em> with a length "
                       "of time.<br><br>"
                       "<em>(<strong>for</strong> toʻgʻri — u <em>How long?</em> savoliga vaqt "
                       "uzunligi bilan javob beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz has known Sherbek ___ 2019.</strong></p>",
        "choices": ["since", "for", "ago", "by"],
        "correct": "since",
        "explanation": "<p><strong>since</strong> is correct — it answers <em>Since when?</em> with the "
                       "point where it started.<br><br>"
                       "<em>(<strong>since</strong> toʻgʻri — u <em>Since when?</em> savoliga boshlangan "
                       "nuqta bilan javob beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher wants the projects ___ Friday.</strong></p>",
        "choices": ["by", "until", "for", "since"],
        "correct": "by",
        "explanation": "<p><strong>by</strong> is correct — a deadline: not later than Friday. "
                       "<em>Until Friday</em> would mean the work continues right up to Friday.<br><br>"
                       "<em>(<strong>by</strong> toʻgʻri — muddat: jumadan kechikmasdan. <em>Until "
                       "Friday</em> esa ish jumagacha davom etishini bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The library is open ___ eight o'clock every evening.</strong></p>",
        "choices": ["until", "by", "for", "since"],
        "correct": "until",
        "explanation": "<p><strong>until</strong> is correct — it covers the whole period up to that "
                       "moment, when the situation stops.<br><br>"
                       "<em>(<strong>until</strong> toʻgʻri — u oʻsha daqiqagacha boʻlgan butun davrni "
                       "qamrab oladi, keyin holat toʻxtaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona has been in this school ___ September.</strong></p>",
        "choices": ["since", "for", "ago", "until"],
        "correct": "since",
        "explanation": "<p><strong>since</strong> is correct — <em>September</em> is a starting point, "
                       "not a length.<br><br>"
                       "<em>(<strong>since</strong> toʻgʻri — <em>September</em> boshlanish nuqtasi, "
                       "uzunlik emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We waited at the bus stop ___ half an hour.</strong></p>",
        "choices": ["for", "since", "by", "ago"],
        "correct": "for",
        "explanation": "<p><strong>for</strong> is correct — <em>half an hour</em> is a length of "
                       "time.<br><br>"
                       "<em>(<strong>for</strong> toʻgʻri — <em>half an hour</em> vaqt "
                       "uzunligi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar phoned me a few minutes ___ .</strong></p>",
        "choices": ["ago", "since", "before", "for"],
        "correct": "ago",
        "explanation": "<p><strong>ago</strong> is correct — counting back from now, and it lives with "
                       "the Past Simple.<br><br>"
                       "<em>(<strong>ago</strong> toʻgʻri — hozirgi paytdan orqaga sanaydi va Past "
                       "Simple bilan yashaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ my last visit, the village has changed a lot.</strong></p>",
        "choices": ["Since", "For", "Ago", "By"],
        "correct": "Since",
        "explanation": "<p><strong>Since</strong> is correct — <em>my last visit</em> is a point in the "
                       "past where the change started.<br><br>"
                       "<em>(<strong>Since</strong> toʻgʻri — <em>my last visit</em> oʻzgarish boshlangan "
                       "oʻtmishdagi nuqta.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos fell asleep ___ the film.</strong></p>",
        "choices": ["during", "while", "for", "since"],
        "correct": "during",
        "explanation": "<p><strong>during</strong> is correct — <em>during</em> takes a noun "
                       "(<em>the film</em>), while <em>while</em> takes a whole clause with a verb "
                       "(<em>while we were watching the film</em>).<br><br>"
                       "<em>(<strong>during</strong> toʻgʻri — <em>during</em> ot oladi (<em>the "
                       "film</em>), <em>while</em> esa feʼli bor butun gap oladi (<em>while we were "
                       "watching the film</em>).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs broke his arm ___ he was playing football.</strong></p>",
        "choices": ["while", "during", "for", "by"],
        "correct": "while",
        "explanation": "<p><strong>while</strong> is correct — a clause with a subject and a verb "
                       "follows it.<br><br>"
                       "<em>(<strong>while</strong> toʻgʻri — undan keyin egasi va feʼli bor gap "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina will be back ___ two weeks.</strong></p>",
        "choices": ["in", "for", "since", "ago"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct — for the future, <em>in</em> means “after that "
                       "much time from now”. It is the mirror image of <em>ago</em>.<br><br>"
                       "<em>(<strong>in</strong> toʻgʻri — kelasi zamon uchun <em>in</em> “shuncha "
                       "vaqtdan keyin” degani. U <em>ago</em> ning oynadagi aksi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Javohir has played the dutar ___ he was seven — that is ___ nine "
                "years.</strong></p>",
        "choices": ["since … for", "for … since", "since … since", "for … for"],
        "correct": "since … for",
        "explanation": "<p><strong>since … for</strong> is correct — a starting point first, then the "
                       "length of the whole period.<br><br>"
                       "<em>(<strong>since … for</strong> toʻgʻri — avval boshlanish nuqtasi, keyin "
                       "butun davrning uzunligi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which question does <em>for</em> answer?</strong></p>",
        "choices": ["How long?", "Since when?", "When exactly?", "How often?"],
        "correct": "How long?",
        "explanation": "<p><strong>How long?</strong> is correct — that one test separates the pair: "
                       "<em>for</em> = how long, <em>since</em> = since when.<br><br>"
                       "<em>(<strong>How long?</strong> toʻgʻri — shu bitta sinov juftlikni ajratadi: "
                       "<em>for</em> = qancha vaqt, <em>since</em> = qachondan beri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda must finish the exercise ___ the end of the lesson.</strong></p>",
        "choices": ["by", "until", "for", "during"],
        "correct": "by",
        "explanation": "<p><strong>by</strong> is correct — a deadline again: at that point it has to be "
                       "ready.<br><br>"
                       "<em>(<strong>by</strong> toʻgʻri — yana muddat: oʻsha nuqtaga kelib tayyor "
                       "boʻlishi kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek stayed at his cousin's house ___ Sunday, then came home.</strong></p>",
        "choices": ["until", "by", "for", "since"],
        "correct": "until",
        "explanation": "<p><strong>until</strong> is correct — the staying continued all the way to "
                       "Sunday.<br><br>"
                       "<em>(<strong>until</strong> toʻgʻri — qolish yakshanbagacha davom etdi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I saw Abdulloh since two days.", "I saw Abdulloh two days ago.",
                    "I haven't seen Abdulloh for two days.",
                    "I haven't seen Abdulloh since Monday."],
        "correct": "I saw Abdulloh since two days.",
        "explanation": "<p><strong>I saw Abdulloh since two days.</strong> is the mistake — "
                       "<em>two days</em> is a length, so it needs <em>for</em>, and with the Past "
                       "Simple the natural word is <em>ago</em>.<br><br>"
                       "<em>(<strong>I saw Abdulloh since two days.</strong> xato — <em>two days</em> "
                       "uzunlik, shuning uchun <em>for</em> kerak; Past Simple bilan esa tabiiy soʻz "
                       "<em>ago</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Sirojiddin left five minutes ago.", "Sirojiddin left ago five minutes.",
                    "Sirojiddin left since five minutes.", "Sirojiddin left for five minutes ago."],
        "correct": "Sirojiddin left five minutes ago.",
        "explanation": "<p><strong>Sirojiddin left five minutes ago.</strong> is correct — the number "
                       "comes first and <em>ago</em> last, exactly as in Uzbek <em>besh daqiqa "
                       "oldin</em>.<br><br>"
                       "<em>(<strong>Sirojiddin left five minutes ago.</strong> toʻgʻri — avval son, "
                       "oxirida <em>ago</em>, xuddi oʻzbekchadagi <em>besh daqiqa oldin</em> "
                       "kabi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> How long have you been in this class, Iroda?</p>"
                "<p><strong>Iroda:</strong> ___</p>",
        "choices": ["For two years, since September 2024.",
                    "Since two years, for September 2024.",
                    "Two years ago, until September 2024.",
                    "For two years ago, since September 2024."],
        "correct": "For two years, since September 2024.",
        "explanation": "<p><strong>For two years, since September 2024.</strong> is correct — the length "
                       "with <em>for</em>, the starting point with <em>since</em>.<br><br>"
                       "<em>(<strong>For two years, since September 2024.</strong> toʻgʻri — uzunlik "
                       "<em>for</em> bilan, boshlanish nuqtasi esa <em>since</em> bilan.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> word is correct.</p>",
        "choices": ["Afsona started English three years ago and has studied it since then, "
                    "so by June she will have done six courses.",
                    "Afsona started English since three years and has studied it for then, "
                    "so until June she will have done six courses.",
                    "Afsona started English for three years ago and has studied it since then, "
                    "so until June she will have done six courses.",
                    "Afsona started English three years since and has studied it for then, "
                    "so by June she will have done six courses."],
        "correct": "Afsona started English three years ago and has studied it since then, "
                   "so by June she will have done six courses.",
        "explanation": "<p><strong>three years ago … since then … by June</strong> is correct — counting "
                       "back, a starting point, and a deadline: the three ideas of this lesson in one "
                       "sentence.<br><br>"
                       "<em>(<strong>three years ago … since then … by June</strong> toʻgʻri — orqaga "
                       "sanash, boshlanish nuqtasi va muddat: bitta gapda shu darsning uchala "
                       "gʻoyasi.)</em></p>",
    },
]


# =====================================================================
# PE-32 — Present Perfect: Form and the Idea of "It Matters Now"
# =====================================================================

Q_PE32 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ lost my keys — I can't open the door.</strong></p>",
        "choices": ["have", "has", "am", "did"],
        "correct": "have",
        "explanation": "<p><strong>have</strong> is correct — the Present Perfect is "
                       "<em>have / has + V3</em>, and <em>I</em> takes <em>have</em>.<br><br>"
                       "<em>(<strong>have</strong> toʻgʻri — Present Perfect <em>have / has + V3</em> "
                       "shaklida boʻlib, <em>I</em> <em>have</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona ___ finished her project.</strong></p>",
        "choices": ["has", "have", "is", "did"],
        "correct": "has",
        "explanation": "<p><strong>has</strong> is correct — <em>he / she / it</em> take <em>has</em>."
                       "<br><br><em>(<strong>has</strong> toʻgʻri — <em>he / she / it</em> <em>has</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct third form (V3).</p>"
                "<p><strong>Behruz has ___ his homework.</strong></p>",
        "choices": ["done", "did", "do", "doing"],
        "correct": "done",
        "explanation": "<p><strong>done</strong> is correct — <em>do → did → done</em>. The Present "
                       "Perfect always uses the third form, never the past form.<br><br>"
                       "<em>(<strong>done</strong> toʻgʻri — <em>do → did → done</em>. Present Perfect "
                       "doim uchinchi shaklni oladi, oʻtgan zamon shaklini emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct third form (V3).</p>"
                "<p><strong>Charos has ___ that book twice.</strong></p>",
        "choices": ["read", "readed", "reading", "reads"],
        "correct": "read",
        "explanation": "<p><strong>read</strong> is correct — the spelling never changes, only the sound "
                       "(<em>/red/</em> here).<br><br>"
                       "<em>(<strong>read</strong> toʻgʻri — yozilishi oʻzgarmaydi, faqat talaffuzi "
                       "(bu yerda <em>/red/</em>).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “I've lost my phone” tell us?</strong></p>",
        "choices": ["I don't have it now.", "I found it again.",
                    "I lost it and then bought a new one.", "I will lose it tomorrow."],
        "correct": "I don't have it now.",
        "explanation": "<p><strong>I don't have it now.</strong> is correct — the Present Perfect is a "
                       "past action with a result you can still feel today.<br><br>"
                       "<em>(<strong>Hozir u menda yoʻq.</strong> toʻgʻri — Present Perfect — natijasi "
                       "bugun ham sezilib turgan oʻtmish harakati.)</em></p>",
    },
    {
        "text": "<p>Choose the correct V3.</p>"
                "<p><strong>Ilgʻor has ___ to Samarkand three times.</strong></p>",
        "choices": ["been", "went", "gone to be", "being"],
        "correct": "been",
        "explanation": "<p><strong>been</strong> is correct — <em>has been to</em> means he went and came "
                       "back. <em>Has gone to</em> would mean he is still there.<br><br>"
                       "<em>(<strong>been</strong> toʻgʻri — <em>has been to</em> borib qaytganini "
                       "bildiradi. <em>Has gone to</em> esa u hali ham oʻsha yerda degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Davron isn't here — he ___ to the shop.</strong></p>",
        "choices": ["has gone", "has been", "have gone", "is gone"],
        "correct": "has gone",
        "explanation": "<p><strong>has gone</strong> is correct — he left and has not come back yet."
                       "<br><br><em>(<strong>has gone</strong> toʻgʻri — u ketdi va hali "
                       "qaytmadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Samandar ___ seen that film.</strong></p>",
        "choices": ["hasn't", "haven't", "didn't", "doesn't"],
        "correct": "hasn't",
        "explanation": "<p><strong>hasn't</strong> is correct — the negative goes on <em>have / has</em>, "
                       "and the V3 stays.<br><br>"
                       "<em>(<strong>hasn't</strong> toʻgʻri — inkor <em>have / has</em> ga qoʻyiladi, "
                       "V3 esa oʻz oʻrnida qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ you finished your homework?</strong></p>",
        "choices": ["Have", "Do", "Did", "Are"],
        "correct": "Have",
        "explanation": "<p><strong>Have</strong> is correct — <em>have / has</em> moves in front of the "
                       "subject, with no <em>do</em>.<br><br>"
                       "<em>(<strong>Have</strong> toʻgʻri — <em>have / has</em> subject oldiga chiqadi, "
                       "<em>do</em> kerak emas.)</em></p>",
    },
    {
        "text": "<p>Complete the short answer.</p>"
                "<p><strong>Has Javohir cleaned the board? — Yes, ___ .</strong></p>",
        "choices": ["he has", "he did", "he is", "he have"],
        "correct": "he has",
        "explanation": "<p><strong>he has</strong> is correct — the short answer repeats the same "
                       "helper.<br><br>"
                       "<em>(<strong>he has</strong> toʻgʻri — qisqa javobda oʻsha yordamchi "
                       "takrorlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ our tests, so we know our marks.</strong></p>",
        "choices": ["has checked", "checked yesterday", "is checking", "checks"],
        "correct": "has checked",
        "explanation": "<p><strong>has checked</strong> is correct — a finished action whose result "
                       "(knowing the marks) matters right now.<br><br>"
                       "<em>(<strong>has checked</strong> toʻgʻri — tugagan harakat, uning natijasi "
                       "(bahoni bilish) esa hozir muhim.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda ___ never been to the mountains.</strong></p>",
        "choices": ["has", "have", "did", "is"],
        "correct": "has",
        "explanation": "<p><strong>has</strong> is correct — life experience is one of the three jobs of "
                       "this tense, and <em>never</em> makes it negative by itself.<br><br>"
                       "<em>(<strong>has</strong> toʻgʻri — hayotiy tajriba — bu zamonning uchta "
                       "vazifasidan biri, <em>never</em> esa oʻzi inkorni bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ three tests this week, and the week isn't over.</strong></p>",
        "choices": ["have had", "had", "have", "are having"],
        "correct": "have had",
        "explanation": "<p><strong>have had</strong> is correct — <em>this week</em> is an unfinished "
                       "period, so more tests are still possible.<br><br>"
                       "<em>(<strong>have had</strong> toʻgʻri — <em>this week</em> tugamagan davr, "
                       "shuning uchun yana test boʻlishi mumkin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which word must <em>never</em> appear with the Present Perfect?</strong></p>",
        "choices": ["yesterday", "already", "just", "ever"],
        "correct": "yesterday",
        "explanation": "<p><strong>yesterday</strong> is correct — a finished, dated time closes the box, "
                       "so it forces the Past Simple: <em>I saw him yesterday</em>.<br><br>"
                       "<em>(<strong>yesterday</strong> toʻgʻri — tugagan, sanasi aniq vaqt “quti”ni "
                       "yopadi, shuning uchun Past Simple talab qilinadi: <em>I saw him "
                       "yesterday</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh ___ his bicycle, so he is walking to school now.</strong></p>",
        "choices": ["has broken", "broke it in", "is breaking", "breaks"],
        "correct": "has broken",
        "explanation": "<p><strong>has broken</strong> is correct — the walking is the present result of "
                       "the past action.<br><br>"
                       "<em>(<strong>has broken</strong> toʻgʻri — piyoda yurish — oʻtmishdagi "
                       "harakatning hozirgi natijasi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Elbek and Firdavs ___ their room, so it ___ clean now.</strong></p>",
        "choices": ["have tidied … is", "has tidied … is", "have tidied … has", "tidied … has been"],
        "correct": "have tidied … is",
        "explanation": "<p><strong>have tidied … is</strong> is correct — a plural subject takes "
                       "<em>have</em>, and the result is described in the present.<br><br>"
                       "<em>(<strong>have tidied … is</strong> toʻgʻri — koʻplikdagi subject "
                       "<em>have</em> oladi, natija esa hozirgi zamonda taʼriflanadi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Madina has went to the library.", "Madina has gone to the library.",
                    "Madina went to the library.", "Madina has been to the library."],
        "correct": "Madina has went to the library.",
        "explanation": "<p><strong>Madina has went to the library.</strong> is the mistake — after "
                       "<em>has</em> the verb must be the third form (<em>gone</em>), not the past form "
                       "(<em>went</em>).<br><br>"
                       "<em>(<strong>Madina has went to the library.</strong> xato — <em>has</em> dan "
                       "keyin feʼl uchinchi shaklda boʻlishi kerak (<em>gone</em>), oʻtgan zamon shakli "
                       "(<em>went</em>) emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Sirojiddin has written three letters this month.",
                    "Sirojiddin has wrote three letters this month.",
                    "Sirojiddin have written three letters this month.",
                    "Sirojiddin has written three letters yesterday."],
        "correct": "Sirojiddin has written three letters this month.",
        "explanation": "<p><strong>Sirojiddin has written three letters this month.</strong> is correct "
                       "— <em>has + written</em>, and <em>this month</em> is an unfinished period. The "
                       "last option fails because <em>yesterday</em> is finished.<br><br>"
                       "<em>(<strong>Sirojiddin has written three letters this month.</strong> toʻgʻri — "
                       "<em>has + written</em>, <em>this month</em> esa tugamagan davr. Oxirgi variant "
                       "xato, chunki <em>yesterday</em> tugagan.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Iroda:</strong> Why are you so happy?</p>"
                "<p><strong>Charos:</strong> ___</p>",
        "choices": ["I've passed my exam!", "I pass my exam!",
                    "I have passed my exam yesterday!", "I am passed my exam!"],
        "correct": "I've passed my exam!",
        "explanation": "<p><strong>I've passed my exam!</strong> is correct — announcing news whose "
                       "result (her happiness) is here right now.<br><br>"
                       "<em>(<strong>I've passed my exam!</strong> toʻgʻri — natijasi (xursandligi) "
                       "hozir sezilib turgan yangilikni eʼlon qilish.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Jasur has finished his homework, but he hasn't checked it yet.",
                    "Jasur has finish his homework, but he hasn't checked it yesterday.",
                    "Jasur have finished his homework, but he doesn't checked it yet.",
                    "Jasur has finished his homework, but he hasn't check it yet."],
        "correct": "Jasur has finished his homework, but he hasn't checked it yet.",
        "explanation": "<p><strong>has finished … hasn't checked …</strong> is correct — the V3 stays in "
                       "both halves, and the negative sits on <em>has</em>.<br><br>"
                       "<em>(<strong>has finished … hasn't checked …</strong> toʻgʻri — ikki qismda ham "
                       "V3 saqlanadi, inkor esa <em>has</em> ga qoʻyiladi.)</em></p>",
    },
]


# =====================================================================
# PE-33 — Present Perfect with for and since
# =====================================================================

Q_PE33 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz's family ___ in this house for ten years.</strong></p>",
        "choices": ["have lived", "live", "lived", "are living"],
        "correct": "have lived",
        "explanation": "<p><strong>have lived</strong> is correct — they moved in ten years ago and are "
                       "still here, so the band reaches now.<br><br>"
                       "<em>(<strong>have lived</strong> toʻgʻri — ular oʻn yil oldin koʻchib kelgan va "
                       "hali ham shu yerda, yaʼni davr hozirgacha yetadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ Korean since 2023.</strong></p>",
        "choices": ["has studied", "studies", "studied", "is studying since"],
        "correct": "has studied",
        "explanation": "<p><strong>has studied</strong> is correct — started in 2023, still going."
                       "<br><br><em>(<strong>has studied</strong> toʻgʻri — 2023 yilda boshlangan va "
                       "hali davom etmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which English sentence matches “Men bu yerda oʻn yildan beri "
                "yashayman”?</strong></p>",
        "choices": ["I have lived here for ten years.", "I live here for ten years.",
                    "I am living here for ten years.", "I lived here for ten years."],
        "correct": "I have lived here for ten years.",
        "explanation": "<p><strong>I have lived here for ten years.</strong> is correct. This is the "
                       "biggest trap in the course: Uzbek uses the present tense here, English uses the "
                       "Present Perfect. Translating word for word gives the wrong sentence.<br><br>"
                       "<em>(<strong>I have lived here for ten years.</strong> toʻgʻri. Bu — kursdagi "
                       "eng katta tuzoq: oʻzbekcha bu yerda hozirgi zamonni ishlatadi, ingliz tili esa "
                       "Present Perfect ni. Soʻzma-soʻz tarjima notoʻgʻri gap beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ at our school since 2015.</strong></p>",
        "choices": ["has worked", "works", "worked", "is working"],
        "correct": "has worked",
        "explanation": "<p><strong>has worked</strong> is correct — he started in 2015 and is still "
                       "teaching us.<br><br>"
                       "<em>(<strong>has worked</strong> toʻgʻri — u 2015 yilda boshlagan va hali ham "
                       "bizga dars beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How long ___ you known Shaxzoda?</strong></p>",
        "choices": ["have", "do", "did", "are"],
        "correct": "have",
        "explanation": "<p><strong>have</strong> is correct — <em>How long …?</em> about something still "
                       "true always takes the Present Perfect.<br><br>"
                       "<em>(<strong>have</strong> toʻgʻri — hali davom etayotgan narsa haqidagi "
                       "<em>How long …?</em> savoli doim Present Perfect oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar has had that bicycle ___ his last birthday.</strong></p>",
        "choices": ["since", "for", "ago", "during"],
        "correct": "since",
        "explanation": "<p><strong>since</strong> is correct — a birthday is a point in time.<br><br>"
                       "<em>(<strong>since</strong> toʻgʻri — tugʻilgan kun — vaqtdagi nuqta.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos has been in the library ___ two hours.</strong></p>",
        "choices": ["for", "since", "ago", "by"],
        "correct": "for",
        "explanation": "<p><strong>for</strong> is correct — <em>two hours</em> is a length of time."
                       "<br><br><em>(<strong>for</strong> toʻgʻri — <em>two hours</em> vaqt "
                       "uzunligi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek ___ his cousin since he moved to Nukus.</strong></p>",
        "choices": ["hasn't seen", "didn't see", "doesn't see", "isn't seeing"],
        "correct": "hasn't seen",
        "explanation": "<p><strong>hasn't seen</strong> is correct — the not-seeing started then and "
                       "continues today.<br><br>"
                       "<em>(<strong>hasn't seen</strong> toʻgʻri — koʻrishmaslik oʻshanda boshlangan va "
                       "bugungacha davom etmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Ilgʻor ___ ill since Monday, so he is still at home.</strong></p>",
        "choices": ["has been", "is", "was", "has being"],
        "correct": "has been",
        "explanation": "<p><strong>has been</strong> is correct — the V3 of <em>be</em> is <em>been</em>, "
                       "and the illness continues.<br><br>"
                       "<em>(<strong>has been</strong> toʻgʻri — <em>be</em> ning V3 shakli "
                       "<em>been</em>, kasallik esa davom etmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona and Iroda ___ friends since primary school.</strong></p>",
        "choices": ["have been", "has been", "are", "were"],
        "correct": "have been",
        "explanation": "<p><strong>have been</strong> is correct — a plural subject, and the friendship "
                       "is still alive.<br><br>"
                       "<em>(<strong>have been</strong> toʻgʻri — koʻplikdagi subject, doʻstlik esa hali "
                       "davom etmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference between “I lived in Andijan” and “I have lived "
                "in Andijan for six years”?</strong></p>",
        "choices": ["The first is finished; the second is still true.",
                    "The first is still true; the second is finished.",
                    "There is no difference.",
                    "The second one is about the future."],
        "correct": "The first is finished; the second is still true.",
        "explanation": "<p><strong>The first is finished; the second is still true.</strong> is correct — "
                       "the Past Simple closes the period, the Present Perfect keeps it open.<br><br>"
                       "<em>(<strong>Birinchisi tugagan; ikkinchisi hali davom etmoqda.</strong> "
                       "toʻgʻri — Past Simple davrni yopadi, Present Perfect esa ochiq "
                       "qoldiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ that jacket for three winters and it still looks new.</strong></p>",
        "choices": ["has worn", "wore", "wears", "is wearing"],
        "correct": "has worn",
        "explanation": "<p><strong>has worn</strong> is correct — three winters up to now, and the jacket "
                       "is still in use.<br><br>"
                       "<em>(<strong>has worn</strong> toʻgʻri — hozirgacha uch qish, kurtka esa hali "
                       "ishlatilmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Javohir ___ the dutar since he was seven, but last year he also "
                "___ the guitar.</strong></p>",
        "choices": ["has played … learnt", "played … has learnt",
                    "has played … has learnt", "plays … learnt"],
        "correct": "has played … learnt",
        "explanation": "<p><strong>has played … learnt</strong> is correct — the first half is still "
                       "true, the second half is closed by <em>last year</em>.<br><br>"
                       "<em>(<strong>has played … learnt</strong> toʻgʻri — birinchi qism hali davom "
                       "etmoqda, ikkinchi qismni esa <em>last year</em> yopib qoʻygan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh lived in Tashkent for two years.</strong> What does this "
                "mean?</p>",
        "choices": ["He does not live there now.", "He still lives there.",
                    "He will live there.", "He has never lived there."],
        "correct": "He does not live there now.",
        "explanation": "<p><strong>He does not live there now.</strong> is correct — the Past Simple "
                       "closes the period, so the two years are over.<br><br>"
                       "<em>(<strong>U hozir u yerda yashamaydi.</strong> toʻgʻri — Past Simple davrni "
                       "yopadi, yaʼni ikki yil tugagan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin ___ me since the beginning of the lesson.</strong></p>",
        "choices": ["hasn't spoken to", "didn't speak to", "doesn't speak to", "wasn't speaking to"],
        "correct": "hasn't spoken to",
        "explanation": "<p><strong>hasn't spoken to</strong> is correct — the lesson is not over, so the "
                       "period is unfinished.<br><br>"
                       "<em>(<strong>hasn't spoken to</strong> toʻgʻri — dars tugamagan, yaʼni davr "
                       "hali ochiq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How long has Davron had that phone? — ___</strong></p>",
        "choices": ["For about a year.", "Since about a year.",
                    "About a year ago he has.", "During about a year."],
        "correct": "For about a year.",
        "explanation": "<p><strong>For about a year.</strong> is correct — a length of time answers "
                       "<em>How long?</em><br><br>"
                       "<em>(<strong>For about a year.</strong> toʻgʻri — <em>How long?</em> savoliga "
                       "vaqt uzunligi javob beradi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Afsona is learning English for five years.",
                    "Afsona has learnt English for five years.",
                    "Afsona learnt English for five years, then stopped.",
                    "Afsona has learnt English since 2021."],
        "correct": "Afsona is learning English for five years.",
        "explanation": "<p><strong>Afsona is learning English for five years.</strong> is the mistake — "
                       "this is the word-for-word translation from Uzbek. Something that started in the "
                       "past and continues needs the Present Perfect.<br><br>"
                       "<em>(<strong>Afsona is learning English for five years.</strong> xato — bu "
                       "oʻzbekchadan soʻzma-soʻz tarjima. Oʻtmishda boshlanib davom etayotgan ish Present "
                       "Perfect talab qiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["We have known Rozimurod teacher since our first year.",
                    "We know Rozimurod teacher since our first year.",
                    "We have known Rozimurod teacher for our first year.",
                    "We knew Rozimurod teacher since our first year."],
        "correct": "We have known Rozimurod teacher since our first year.",
        "explanation": "<p><strong>We have known Rozimurod teacher since our first year.</strong> is "
                       "correct — Present Perfect with a starting point.<br><br>"
                       "<em>(<strong>We have known Rozimurod teacher since our first year.</strong> "
                       "toʻgʻri — boshlanish nuqtasi bilan Present Perfect.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> How long have you played volleyball, "
                "Shaxzoda?</p>"
                "<p><strong>Shaxzoda:</strong> ___</p>",
        "choices": ["I've played since I was ten — that's five years.",
                    "I play since I was ten — that's five years.",
                    "I played since I was ten — that's five years.",
                    "I am playing for I was ten — that's five years."],
        "correct": "I've played since I was ten — that's five years.",
        "explanation": "<p><strong>I've played since I was ten — that's five years.</strong> is correct — "
                       "still playing, so Present Perfect, with <em>since</em> for the starting "
                       "point.<br><br>"
                       "<em>(<strong>I've played since I was ten — that's five years.</strong> toʻgʻri — "
                       "hali oʻynaydi, shuning uchun Present Perfect, boshlanish nuqtasi esa "
                       "<em>since</em> bilan.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Behruz has been in this class for two years and has known Elbek since 2023.",
                    "Behruz is in this class for two years and knows Elbek since 2023.",
                    "Behruz has been in this class since two years and has known Elbek for 2023.",
                    "Behruz was in this class for two years and has known Elbek since 2023."],
        "correct": "Behruz has been in this class for two years and has known Elbek since 2023.",
        "explanation": "<p><strong>has been … for two years … has known … since 2023</strong> is correct "
                       "— both situations are still true, with <em>for</em> on the length and "
                       "<em>since</em> on the point.<br><br>"
                       "<em>(<strong>has been … for two years … has known … since 2023</strong> "
                       "toʻgʻri — ikki holat ham davom etmoqda, uzunlikka <em>for</em>, nuqtaga esa "
                       "<em>since</em>.)</em></p>",
    },
]


# =====================================================================
# PE-34 — Present Perfect with already, yet, just, still, ever, never
# =====================================================================

Q_PE34 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I've ___ eaten, thank you — I'm not hungry.</strong></p>",
        "choices": ["already", "yet", "still", "ever"],
        "correct": "already",
        "explanation": "<p><strong>already</strong> is correct — it means sooner than expected, and it "
                       "belongs to positive sentences.<br><br>"
                       "<em>(<strong>already</strong> toʻgʻri — u kutilganidan erta degani va tasdiq "
                       "gaplarda ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Have you finished your project ___ , Javohir?</strong></p>",
        "choices": ["yet", "already", "just", "never"],
        "correct": "yet",
        "explanation": "<p><strong>yet</strong> is correct — it lives in questions and negatives, and it "
                       "stands at the very end.<br><br>"
                       "<em>(<strong>yet</strong> toʻgʻri — u savol va inkorlarda ishlatiladi va gap "
                       "oxirida turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona has ___ left — you can still catch her at the gate.</strong></p>",
        "choices": ["just", "yet", "still", "ever"],
        "correct": "just",
        "explanation": "<p><strong>just</strong> is correct — a moment ago.<br><br>"
                       "<em>(<strong>just</strong> toʻgʻri — hozirgina.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Have you ___ been to Khiva?</strong></p>",
        "choices": ["ever", "already", "yet", "still"],
        "correct": "ever",
        "explanation": "<p><strong>ever</strong> is correct — it asks about a whole life: “at any time up "
                       "to now?”<br><br>"
                       "<em>(<strong>ever</strong> toʻgʻri — u butun hayot haqida soʻraydi: “hozirgacha "
                       "biror marta?”)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda has ___ seen snow in the mountains.</strong></p>",
        "choices": ["never", "yet", "already not", "ever not"],
        "correct": "never",
        "explanation": "<p><strong>never</strong> is correct — it is negative all by itself, so no second "
                       "negative may join it.<br><br>"
                       "<em>(<strong>never</strong> toʻgʻri — u oʻzi inkor, shuning uchun yoniga ikkinchi "
                       "inkor qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ hasn't answered my message.</strong></p>",
        "choices": ["still", "yet", "already", "ever"],
        "correct": "still",
        "explanation": "<p><strong>still</strong> is correct — it shows we expected it to happen and are "
                       "surprised that it hasn't. It stands <em>before</em> <em>hasn't</em>.<br><br>"
                       "<em>(<strong>still</strong> toʻgʻri — biz buni kutgan edik va hali "
                       "boʻlmagani ajablantiradi. U <em>hasn't</em> dan <em>oldin</em> turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct position.</p>"
                "<p><strong>Where does <em>already</em> stand?</strong></p>",
        "choices": ["between have/has and the V3", "at the very end of the sentence",
                    "before the subject", "after the object"],
        "correct": "between have/has and the V3",
        "explanation": "<p><strong>between have/has and the V3</strong> is correct: <em>I have already "
                       "eaten</em>. <em>Already, just, ever, never</em> all sit there.<br><br>"
                       "<em>(<strong>have/has bilan V3 orasida</strong> toʻgʻri: <em>I have already "
                       "eaten</em>. <em>Already, just, ever, never</em> — hammasi shu yerda "
                       "turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher hasn't given us the results ___ .</strong></p>",
        "choices": ["yet", "already", "just", "ever"],
        "correct": "yet",
        "explanation": "<p><strong>yet</strong> is correct — a negative sentence, and <em>yet</em> goes "
                       "at the end.<br><br>"
                       "<em>(<strong>yet</strong> toʻgʻri — inkor gap, <em>yet</em> esa oxirida "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda has just ___ from the shop.</strong></p>",
        "choices": ["come back", "came back", "coming back", "come backed"],
        "correct": "come back",
        "explanation": "<p><strong>come back</strong> is correct — after the companion word the verb is "
                       "still the V3 (<em>come</em>), not the past form.<br><br>"
                       "<em>(<strong>come back</strong> toʻgʻri — hamroh soʻzdan keyin ham feʼl V3 "
                       "shaklida qoladi (<em>come</em>), oʻtgan zamon shakli emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Have you ___ tried Korean food, Samandar?</strong> — No, ___ .</p>",
        "choices": ["ever … never", "never … ever", "yet … already", "already … yet"],
        "correct": "ever … never",
        "explanation": "<p><strong>ever … never</strong> is correct — <em>ever</em> asks about life "
                       "experience, <em>never</em> answers it.<br><br>"
                       "<em>(<strong>ever … never</strong> toʻgʻri — <em>ever</em> hayotiy tajriba haqida "
                       "soʻraydi, <em>never</em> esa javob beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos has ___ finished all her exercises, and the lesson has only just "
                "started.</strong></p>",
        "choices": ["already", "yet", "still", "never"],
        "correct": "already",
        "explanation": "<p><strong>already</strong> is correct — faster than expected, which is exactly "
                       "the surprise this word carries.<br><br>"
                       "<em>(<strong>already</strong> toʻgʻri — kutilganidan tezroq, bu soʻz aynan shu "
                       "hayratni bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh ___ hasn't decided which university to choose.</strong></p>",
        "choices": ["still", "yet", "already", "just"],
        "correct": "still",
        "explanation": "<p><strong>still</strong> is correct — the decision was expected long ago."
                       "<br><br><em>(<strong>still</strong> toʻgʻri — qaror ancha oldin kutilgan "
                       "edi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference between <em>yet</em> and <em>already</em>?</strong></p>",
        "choices": ["yet = questions and negatives; already = positive sentences",
                    "yet = positive sentences; already = negatives",
                    "They are exactly the same.",
                    "yet is about the future; already is about the past."],
        "correct": "yet = questions and negatives; already = positive sentences",
        "explanation": "<p><strong>yet = questions and negatives; already = positive sentences</strong> "
                       "is correct — and <em>yet</em> also sits at the end while <em>already</em> sits in "
                       "the middle.<br><br>"
                       "<em>(<strong>yet = savol va inkor; already = tasdiq gaplar</strong> toʻgʻri — "
                       "hamda <em>yet</em> gap oxirida, <em>already</em> esa oʻrtada turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek has ___ washed the dishes, so you can rest.</strong></p>",
        "choices": ["already", "yet", "still", "ever"],
        "correct": "already",
        "explanation": "<p><strong>already</strong> is correct — the job is done sooner than you "
                       "thought.<br><br>"
                       "<em>(<strong>already</strong> toʻgʻri — ish siz oʻylagandan erta "
                       "bajarilgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence uses <em>still</em> correctly?</strong></p>",
        "choices": ["Sirojiddin still hasn't come.", "Sirojiddin hasn't still come.",
                    "Sirojiddin hasn't come still.", "Still Sirojiddin hasn't come yet already."],
        "correct": "Sirojiddin still hasn't come.",
        "explanation": "<p><strong>Sirojiddin still hasn't come.</strong> is correct — <em>still</em> "
                       "comes <em>before</em> the negative helper, unlike the others.<br><br>"
                       "<em>(<strong>Sirojiddin still hasn't come.</strong> toʻgʻri — <em>still</em> "
                       "inkor yordamchidan <em>oldin</em> keladi, boshqalaridan farqli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Ilgʻor has ___ been abroad, but he wants to go one day.</strong></p>",
        "choices": ["never", "ever", "yet", "already"],
        "correct": "never",
        "explanation": "<p><strong>never</strong> is correct — no experience at all, so far.<br><br>"
                       "<em>(<strong>never</strong> toʻgʻri — hozirgacha umuman tajriba yoʻq.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Madina hasn't never seen the sea.", "Madina has never seen the sea.",
                    "Madina hasn't seen the sea yet.", "Has Madina ever seen the sea?"],
        "correct": "Madina hasn't never seen the sea.",
        "explanation": "<p><strong>Madina hasn't never seen the sea.</strong> is the mistake — a double "
                       "negative. <em>Never</em> already carries the “not”.<br><br>"
                       "<em>(<strong>Madina hasn't never seen the sea.</strong> xato — ikki karra inkor. "
                       "<em>Never</em> allaqachon “yoʻq” maʼnosini tashiydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Have you spoken to Rozimurod teacher yet?",
                    "Have you yet spoken to Rozimurod teacher?",
                    "Have you spoken yet to Rozimurod teacher?",
                    "Yet have you spoken to Rozimurod teacher?"],
        "correct": "Have you spoken to Rozimurod teacher yet?",
        "explanation": "<p><strong>Have you spoken to Rozimurod teacher yet?</strong> is correct — "
                       "<em>yet</em> belongs at the very end of the question.<br><br>"
                       "<em>(<strong>Have you spoken to Rozimurod teacher yet?</strong> toʻgʻri — "
                       "<em>yet</em> savolning eng oxirida turadi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Davron:</strong> Shall we start the game?</p>"
                "<p><strong>Behruz:</strong> Wait — ___</p>",
        "choices": ["Firdavs hasn't arrived yet.", "Firdavs hasn't arrived already.",
                    "Firdavs has arrived yet.", "Firdavs hasn't yet arrive."],
        "correct": "Firdavs hasn't arrived yet.",
        "explanation": "<p><strong>Firdavs hasn't arrived yet.</strong> is correct — a negative with "
                       "<em>yet</em> at the end, and the V3 <em>arrived</em>.<br><br>"
                       "<em>(<strong>Firdavs hasn't arrived yet.</strong> toʻgʻri — oxirida <em>yet</em> "
                       "bilan inkor va V3 shakli <em>arrived</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> word is in the right place.</p>",
        "choices": ["I've just come home, I've already done my homework, "
                    "but I still haven't eaten and I haven't rested yet.",
                    "I've come just home, I've done already my homework, "
                    "but I haven't still eaten and I haven't yet rested.",
                    "I just have come home, I already have done my homework, "
                    "but I still haven't eaten and I haven't rested already.",
                    "I've just come home, I've yet done my homework, "
                    "but I haven't never eaten and I still haven't rested yet."],
        "correct": "I've just come home, I've already done my homework, "
                   "but I still haven't eaten and I haven't rested yet.",
        "explanation": "<p><strong>just … already … still … yet</strong> is correct — the first two sit "
                       "in the middle, <em>still</em> comes before the negative helper, and <em>yet</em> "
                       "closes the sentence.<br><br>"
                       "<em>(<strong>just … already … still … yet</strong> toʻgʻri — birinchi ikkitasi "
                       "oʻrtada, <em>still</em> inkor yordamchidan oldin, <em>yet</em> esa gapni yopib "
                       "keladi.)</em></p>",
    },
]


# =====================================================================
# PE-35 — Present Perfect vs Past Simple
# =====================================================================

Q_PE35 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda ___ her arm last year.</strong></p>",
        "choices": ["broke", "has broken", "breaks", "is breaking"],
        "correct": "broke",
        "explanation": "<p><strong>broke</strong> is correct — <em>last year</em> is a finished, dated "
                       "time, so the box is closed.<br><br>"
                       "<em>(<strong>broke</strong> toʻgʻri — <em>last year</em> tugagan, sanasi aniq "
                       "vaqt, yaʼni “quti” yopilgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda ___ her arm — look at the plaster!</strong></p>",
        "choices": ["has broken", "broke", "breaks", "was breaking"],
        "correct": "has broken",
        "explanation": "<p><strong>has broken</strong> is correct — no time is named, and the result is "
                       "visible right now.<br><br>"
                       "<em>(<strong>has broken</strong> toʻgʻri — vaqt aytilmagan, natija esa hozir "
                       "koʻrinib turibdi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which test decides between the two tenses?</strong></p>",
        "choices": ["Is the time finished, or does it matter now?",
                    "Is the sentence long or short?",
                    "Is the verb regular or irregular?",
                    "Is the subject singular or plural?"],
        "correct": "Is the time finished, or does it matter now?",
        "explanation": "<p><strong>Is the time finished, or does it matter now?</strong> is correct — "
                       "finished time → Past Simple; result now → Present Perfect.<br><br>"
                       "<em>(<strong>Vaqt tugaganmi yoki hozir muhimmi?</strong> toʻgʻri — tugagan "
                       "vaqt → Past Simple; hozirgi natija → Present Perfect.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ Rozimurod teacher yesterday.</strong></p>",
        "choices": ["saw", "have seen", "see", "has seen"],
        "correct": "saw",
        "explanation": "<p><strong>saw</strong> is correct — <em>yesterday</em> is the clearest Past "
                       "Simple signal there is.<br><br>"
                       "<em>(<strong>saw</strong> toʻgʻri — <em>yesterday</em> — Past Simple ning eng "
                       "aniq signali.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>We ___ Elbek this week — where is he?</strong></p>",
        "choices": ["haven't seen", "didn't see", "don't see", "weren't seeing"],
        "correct": "haven't seen",
        "explanation": "<p><strong>haven't seen</strong> is correct — <em>this week</em> is not over, so "
                       "the period is still open.<br><br>"
                       "<em>(<strong>haven't seen</strong> toʻgʻri — <em>this week</em> tugamagan, yaʼni "
                       "davr hali ochiq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which signal word belongs to the Present Perfect?</strong></p>",
        "choices": ["never", "in 2019", "two days ago", "last night"],
        "correct": "never",
        "explanation": "<p><strong>never</strong> is correct — the Present Perfect family is "
                       "<em>ever, never, just, already, yet, so far, this week, for, since</em>.<br><br>"
                       "<em>(<strong>never</strong> toʻgʻri — Present Perfect oilasi: <em>ever, never, "
                       "just, already, yet, so far, this week, for, since</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which signal word belongs to the Past Simple?</strong></p>",
        "choices": ["in 2020", "yet", "so far", "just"],
        "correct": "in 2020",
        "explanation": "<p><strong>in 2020</strong> is correct — a dated year closes the time.<br><br>"
                       "<em>(<strong>in 2020</strong> toʻgʻri — aniq yil vaqtni yopadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ in Nukus from 2015 to 2019.</strong></p>",
        "choices": ["lived", "has lived", "lives", "has been living"],
        "correct": "lived",
        "explanation": "<p><strong>lived</strong> is correct — the period has both a start and an end, so "
                       "it is completely closed.<br><br>"
                       "<em>(<strong>lived</strong> toʻgʻri — davrning boshi ham, oxiri ham bor, yaʼni "
                       "u toʻliq yopilgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ in Nukus for four years and still loves it there.</strong></p>",
        "choices": ["has lived", "lived", "was living", "lives"],
        "correct": "has lived",
        "explanation": "<p><strong>has lived</strong> is correct — the second half tells us she is still "
                       "there, so the band reaches now.<br><br>"
                       "<em>(<strong>has lived</strong> toʻgʻri — gapning ikkinchi qismi u hali ham oʻsha "
                       "yerda ekanini aytadi, yaʼni davr hozirgacha yetadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ his phone. He is looking for it now.</strong></p>",
        "choices": ["has lost", "lost it last", "loses", "was losing"],
        "correct": "has lost",
        "explanation": "<p><strong>has lost</strong> is correct — the searching is the present "
                       "consequence.<br><br>"
                       "<em>(<strong>has lost</strong> toʻgʻri — qidirayotgani — hozirgi natija.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Behruz ___ his leg! He ___ off his bicycle this morning.</strong></p>",
        "choices": ["has hurt … fell", "hurt … has fallen", "has hurt … has fallen", "hurt … fell"],
        "correct": "has hurt … fell",
        "explanation": "<p><strong>has hurt … fell</strong> is correct — this is the news pattern: "
                       "announce with the Present Perfect, then explain the details with the Past "
                       "Simple.<br><br>"
                       "<em>(<strong>has hurt … fell</strong> toʻgʻri — bu yangilik qolipi: Present "
                       "Perfect bilan eʼlon qilinadi, tafsilotlar esa Past Simple bilan "
                       "aytiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher has arrived. He ___ ten minutes ago.</strong></p>",
        "choices": ["came", "has come", "comes", "was coming"],
        "correct": "came",
        "explanation": "<p><strong>came</strong> is correct — as soon as a time is named "
                       "(<em>ten minutes ago</em>), English switches to the Past Simple.<br><br>"
                       "<em>(<strong>came</strong> toʻgʻri — vaqt aytilishi bilan (<em>ten minutes "
                       "ago</em>) ingliz tili Past Simple ga oʻtadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you ever ___ to Bukhara?</strong></p>",
        "choices": ["Have … been", "Did … be", "Have … was", "Did … been"],
        "correct": "Have … been",
        "explanation": "<p><strong>Have … been</strong> is correct — <em>ever</em> asks about a whole "
                       "life, so the time is unfinished.<br><br>"
                       "<em>(<strong>Have … been</strong> toʻgʻri — <em>ever</em> butun hayot haqida "
                       "soʻraydi, yaʼni vaqt tugamagan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>When ___ Marjona ___ that jacket?</strong></p>",
        "choices": ["did … buy", "has … bought", "did … bought", "have … buy"],
        "correct": "did … buy",
        "explanation": "<p><strong>did … buy</strong> is correct — <em>when</em> asks for a specific "
                       "finished moment, so the Present Perfect is impossible here.<br><br>"
                       "<em>(<strong>did … buy</strong> toʻgʻri — <em>when</em> aniq, tugagan daqiqani "
                       "soʻraydi, shuning uchun bu yerda Present Perfect boʻlmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Madina ___ three books this month, but last month she ___ only "
                "one.</strong></p>",
        "choices": ["has read … read", "read … has read", "has read … has read", "read … read"],
        "correct": "has read … read",
        "explanation": "<p><strong>has read … read</strong> is correct — <em>this month</em> is open, "
                       "<em>last month</em> is closed. One sentence, both tenses.<br><br>"
                       "<em>(<strong>has read … read</strong> toʻgʻri — <em>this month</em> ochiq, "
                       "<em>last month</em> yopiq. Bitta gapda ikki zamon.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Ilgʻor ___ his homework, so he can play football now.</strong></p>",
        "choices": ["has finished", "finished it in", "finishes", "was finishing"],
        "correct": "has finished",
        "explanation": "<p><strong>has finished</strong> is correct — permission to play is the present "
                       "result.<br><br>"
                       "<em>(<strong>has finished</strong> toʻgʻri — futbol oʻynash imkoni — hozirgi "
                       "natija.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I have seen Abdulloh yesterday.", "I saw Abdulloh yesterday.",
                    "I have seen Abdulloh today.", "I have just seen Abdulloh."],
        "correct": "I have seen Abdulloh yesterday.",
        "explanation": "<p><strong>I have seen Abdulloh yesterday.</strong> is the mistake — "
                       "<em>yesterday</em> is finished time and can never sit in the Present "
                       "Perfect.<br><br>"
                       "<em>(<strong>I have seen Abdulloh yesterday.</strong> xato — <em>yesterday</em> "
                       "tugagan vaqt va hech qachon Present Perfect bilan kelmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Sirojiddin has never eaten sushi, but he tried kimchi last year.",
                    "Sirojiddin never ate sushi, but he has tried kimchi last year.",
                    "Sirojiddin has never eaten sushi, but he has tried kimchi last year.",
                    "Sirojiddin never has eaten sushi, but he tried kimchi last year."],
        "correct": "Sirojiddin has never eaten sushi, but he tried kimchi last year.",
        "explanation": "<p><strong>has never eaten … tried … last year</strong> is correct — life "
                       "experience in the Present Perfect, a dated event in the Past Simple.<br><br>"
                       "<em>(<strong>has never eaten … tried … last year</strong> toʻgʻri — hayotiy "
                       "tajriba Present Perfect da, sanasi aniq voqea esa Past Simple da.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Where is your project, Javohir?</p>"
                "<p><strong>Javohir:</strong> ___</p>",
        "choices": ["I've left it at home. I finished it late last night.",
                    "I left it at home. I have finished it late last night.",
                    "I've left it at home. I've finished it late last night.",
                    "I leave it at home. I have finish it late last night."],
        "correct": "I've left it at home. I finished it late last night.",
        "explanation": "<p><strong>I've left it at home. I finished it late last night.</strong> is "
                       "correct — the news first (that is why it is missing now), then the dated "
                       "detail.<br><br>"
                       "<em>(<strong>I've left it at home. I finished it late last night.</strong> "
                       "toʻgʻri — avval yangilik (shuning uchun u hozir yoʻq), keyin sanasi aniq "
                       "tafsilot.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>both</strong> tenses are used correctly.</p>",
        "choices": ["Afsona has won the competition! She practised every day for six months.",
                    "Afsona won the competition! She has practised every day for six months ago.",
                    "Afsona has won the competition yesterday! She has practised every day.",
                    "Afsona has win the competition! She has practise every day for six months."],
        "correct": "Afsona has won the competition! She practised every day for six months.",
        "explanation": "<p><strong>has won … practised …</strong> is correct — the news in the Present "
                       "Perfect, the finished background in the Past Simple.<br><br>"
                       "<em>(<strong>has won … practised …</strong> toʻgʻri — yangilik Present Perfect "
                       "da, tugagan tayyorgarlik esa Past Simple da.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-31 Practice: Time Expressions: ago, for, since, by, until",
        "tutorial":    "PE-31:",
        "level":       "easy",
        "description": "PE-31 darsiga 20 savol: ago bilan orqaga sanash, for va since farqi, "
                       "by (muddat) va until (butun davr), during/while va kelasi zamondagi in. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE31,
    },
    {
        "title":       "PE-32 Practice: Present Perfect: Form and the Idea of \"It Matters Now\"",
        "tutorial":    "PE-32:",
        "description": "PE-32 darsiga 20 savol: have/has + V3, uchinchi shakl, hozirgi natija, "
                       "hayotiy tajriba, been va gone farqi hamda yesterday bilan ishlatib "
                       "boʻlmasligi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE32,
    },
    {
        "title":       "PE-33 Practice: Present Perfect with for and since",
        "tutorial":    "PE-33:",
        "description": "PE-33 darsiga 20 savol: oʻtmishda boshlanib hozir ham davom etayotgan ish, "
                       "for va since, How long …? savoli va oʻzbekchadan soʻzma-soʻz tarjima "
                       "tuzogʻi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE33,
    },
    {
        "title":       "PE-34 Practice: Present Perfect with already, yet, just, still, ever, never",
        "tutorial":    "PE-34:",
        "description": "PE-34 darsiga 20 savol: oltita hamroh soʻz, ularning aniq oʻrni "
                       "(oʻrtada yoki gap oxirida) va never bilan ikki karra inkor xatosi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE34,
    },
    {
        "title":       "PE-35 Practice: Present Perfect vs Past Simple — The Big Decision",
        "tutorial":    "PE-35:",
        "description": "PE-35 darsiga 20 savol: vaqt tugaganmi yoki hozir muhimmi degan sinov, "
                       "har bir zamonning signal soʻzlari va yangilikni eʼlon qilib, keyin "
                       "tafsilotini aytish qolipi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE35,
    },
]
