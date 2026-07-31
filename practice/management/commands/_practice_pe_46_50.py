# -*- coding: utf-8 -*-
"""Prime English practices — PE-46 … PE-50 (the rest of Block D, modal verbs).

Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_46_50.py --master=prime --expect-questions=20
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
# PE-46 — should, ought to, had better: Advice
# =====================================================================

Q_PE46 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>You look tired. You ___ rest.</strong></p>",
        "choices": ["should", "should to", "shoulds", "are should"],
        "correct": "should",
        "explanation": "<p><strong>should</strong> is correct — the everyday advice modal, followed by "
                       "the base verb with no <em>to</em>.<br><br>"
                       "<em>(<strong>should</strong> toʻgʻri — kundalik maslahat modali, undan keyin "
                       "<em>to</em> siz asosiy feʼl keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Behruz ___ stay up so late before an exam.</strong></p>",
        "choices": ["shouldn't", "doesn't should", "not should", "shouldn't to"],
        "correct": "shouldn't",
        "explanation": "<p><strong>shouldn't</strong> is correct — modals take <em>not</em> directly, "
                       "with no <em>do</em>.<br><br>"
                       "<em>(<strong>shouldn't</strong> toʻgʻri — modallar <em>not</em> ni toʻgʻridan "
                       "toʻgʻri oladi, <em>do</em> kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What ___ I do, Rozimurod teacher?</strong></p>",
        "choices": ["should", "do should", "am should", "should to"],
        "correct": "should",
        "explanation": "<p><strong>should</strong> is correct — this is how you ask for advice, and it is "
                       "one of the most useful questions in real conversation.<br><br>"
                       "<em>(<strong>should</strong> toʻgʻri — maslahat shunday soʻraladi va bu haqiqiy "
                       "suhbatdagi eng foydali savollardan biri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda ___ drink more water — she has a headache.</strong></p>",
        "choices": ["should", "shoulds", "should to", "is should"],
        "correct": "should",
        "explanation": "<p><strong>should</strong> is correct — no <em>-s</em> for <em>she</em>, like "
                       "every modal.<br><br>"
                       "<em>(<strong>should</strong> toʻgʻri — har qanday modal kabi <em>she</em> uchun "
                       "<em>-s</em> qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which modal keeps its <em>to</em>?</strong></p>",
        "choices": ["ought to", "should", "must", "can"],
        "correct": "ought to",
        "explanation": "<p><strong>ought to</strong> is correct — it is the one modal that carries "
                       "<em>to</em> with it: <em>You ought to apologise</em>.<br><br>"
                       "<em>(<strong>ought to</strong> toʻgʻri — bu <em>to</em> ni oʻzi bilan olib "
                       "yuradigan yagona modal: <em>You ought to apologise</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ apologise — she was rude to her sister.</strong></p>",
        "choices": ["ought to", "ought", "oughts to", "ought to to"],
        "correct": "ought to",
        "explanation": "<p><strong>ought to</strong> is correct — it means much the same as "
                       "<em>should</em>, but sounds a little more formal.<br><br>"
                       "<em>(<strong>ought to</strong> toʻgʻri — maʼnosi <em>should</em> ga juda yaqin, "
                       "lekin biroz rasmiyroq eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>You ___ hurry — the bus leaves in five minutes!</strong></p>",
        "choices": ["had better", "have better", "had better to", "has better"],
        "correct": "had better",
        "explanation": "<p><strong>had better</strong> is correct — advice with a warning: something bad "
                       "will happen if you don't.<br><br>"
                       "<em>(<strong>had better</strong> toʻgʻri — ogohlantirish bilan berilgan "
                       "maslahat: aks holda yomon narsa boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ take an umbrella — it looks like rain.</strong></p>",
        "choices": ["had better", "had better to", "have better", "would better"],
        "correct": "had better",
        "explanation": "<p><strong>had better</strong> is correct — the form never changes for the "
                       "person, and the base verb follows with no <em>to</em>.<br><br>"
                       "<em>(<strong>had better</strong> toʻgʻri — shakl shaxsga qarab oʻzgarmaydi, undan "
                       "keyin esa <em>to</em> siz asosiy feʼl keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>You ___ tell anybody — it's a secret.</strong></p>",
        "choices": ["had better not", "hadn't better", "had not better to", "didn't have better"],
        "correct": "had better not",
        "explanation": "<p><strong>had better not</strong> is correct — the <em>not</em> comes after "
                       "<em>better</em>, which surprises many learners.<br><br>"
                       "<em>(<strong>had better not</strong> toʻgʻri — <em>not</em> <em>better</em> dan "
                       "keyin keladi, bu koʻp oʻrganuvchilarni hayron qoldiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which is the strongest advice?</strong></p>",
        "choices": ["You'd better see a doctor.", "You should see a doctor.",
                    "You ought to see a doctor.", "You could see a doctor."],
        "correct": "You'd better see a doctor.",
        "explanation": "<p><strong>You'd better see a doctor.</strong> is correct — <em>had better</em> "
                       "carries an unspoken “or something bad will happen”.<br><br>"
                       "<em>(<strong>You'd better see a doctor.</strong> toʻgʻri — <em>had better</em> "
                       "ichida “aks holda yomon boʻladi” degan ogohlantirish yashiringan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The parcel ___ arrive tomorrow — they posted it on Monday.</strong></p>",
        "choices": ["should", "had better", "ought", "shoulds"],
        "correct": "should",
        "explanation": "<p><strong>should</strong> is correct — the quieter job of <em>should</em>: what "
                       "you expect to happen, not advice.<br><br>"
                       "<em>(<strong>should</strong> toʻgʻri — <em>should</em> ning ikkinchi vazifasi: "
                       "maslahat emas, kutilayotgan natija.)</em></p>",
    },
    {
        "text": "<p>Choose the correct question form.</p>"
                "<p><strong>___ I tell Marjona the truth?</strong></p>",
        "choices": ["Should", "Do I should", "Am I should", "Should to"],
        "correct": "Should",
        "explanation": "<p><strong>Should</strong> is correct — questions by inversion, no <em>do</em>."
                       "<br><br><em>(<strong>Should</strong> toʻgʻri — savol inversiya bilan yasaladi, "
                       "<em>do</em> kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ study harder if he wants to enter university.</strong></p>",
        "choices": ["should", "shoulds", "should to", "had better to"],
        "correct": "should",
        "explanation": "<p><strong>should</strong> is correct — advice tied to a goal.<br><br>"
                       "<em>(<strong>should</strong> toʻgʻri — maqsad bilan bogʻliq maslahat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the short form of <em>had better</em>?</strong></p>",
        "choices": ["'d better", "'ll better", "'ve better", "'s better"],
        "correct": "'d better",
        "explanation": "<p><strong>'d better</strong> is correct — <em>You'd better go</em>. Careful: "
                       "<em>'d</em> can also be <em>would</em>, so look at what follows.<br><br>"
                       "<em>(<strong>'d better</strong> toʻgʻri — <em>You'd better go</em>. Ehtiyot "
                       "boʻling: <em>'d</em> <em>would</em> ham boʻlishi mumkin, shuning uchun keyingi "
                       "soʻzga qarang.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir ___ have told me earlier — now it's too late.</strong></p>",
        "choices": ["should", "should to", "shoulds", "had better"],
        "correct": "should",
        "explanation": "<p><strong>should</strong> is correct — <em>should have + V3</em> looks back at "
                       "the past with regret. You meet it fully in PE-48.<br><br>"
                       "<em>(<strong>should</strong> toʻgʻri — <em>should have + V3</em> oʻtmishga afsus "
                       "bilan qaraydi. Buni PE-48 da toʻliq koʻrasiz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>You ___ revise tonight, and you ___ forget your calculator "
                "tomorrow.</strong></p>",
        "choices": ["should … had better not", "had better not … should",
                    "should … should to", "ought … had better"],
        "correct": "should … had better not",
        "explanation": "<p><strong>should … had better not</strong> is correct — ordinary advice, then a "
                       "warning about a specific consequence.<br><br>"
                       "<em>(<strong>should … had better not</strong> toʻgʻri — oddiy maslahat, keyin "
                       "aniq oqibat haqida ogohlantirish.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Shaxzoda should to see a doctor.", "Shaxzoda should see a doctor.",
                    "Shaxzoda ought to see a doctor.", "Shaxzoda had better see a doctor."],
        "correct": "Shaxzoda should to see a doctor.",
        "explanation": "<p><strong>Shaxzoda should to see a doctor.</strong> is the mistake — only "
                       "<em>ought</em> keeps <em>to</em>.<br><br>"
                       "<em>(<strong>Shaxzoda should to see a doctor.</strong> xato — <em>to</em> ni "
                       "faqat <em>ought</em> saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["You'd better not be late again.", "You'd not better be late again.",
                    "You hadn't better be late again.", "You'd better don't be late again."],
        "correct": "You'd better not be late again.",
        "explanation": "<p><strong>You'd better not be late again.</strong> is correct — <em>not</em> "
                       "sits after <em>better</em>, and no <em>don't</em> appears.<br><br>"
                       "<em>(<strong>You'd better not be late again.</strong> toʻgʻri — <em>not</em> "
                       "<em>better</em> dan keyin turadi, <em>don't</em> esa ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Abdulloh:</strong> I've got a terrible headache.</p>"
                "<p><strong>Madina:</strong> ___</p>",
        "choices": ["You should go home and rest.", "You should to go home and rest.",
                    "You had better to go home and rest.", "You shoulds go home and rest."],
        "correct": "You should go home and rest.",
        "explanation": "<p><strong>You should go home and rest.</strong> is correct — friendly, ordinary "
                       "advice.<br><br>"
                       "<em>(<strong>You should go home and rest.</strong> toʻgʻri — doʻstona, oddiy "
                       "maslahat.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["You should revise tonight, you ought to sleep early, "
                    "and you'd better not forget your pen.",
                    "You should to revise tonight, you ought sleep early, "
                    "and you'd better not to forget your pen.",
                    "You shoulds revise tonight, you ought to sleep early, "
                    "and you hadn't better forget your pen.",
                    "You should revise tonight, you ought to sleeping early, "
                    "and you had better don't forget your pen."],
        "correct": "You should revise tonight, you ought to sleep early, "
                   "and you'd better not forget your pen.",
        "explanation": "<p><strong>should … ought to … 'd better not …</strong> is correct — no <em>to</em> "
                       "after <em>should</em>, <em>to</em> kept after <em>ought</em>, and <em>not</em> "
                       "after <em>better</em>.<br><br>"
                       "<em>(<strong>should … ought to … 'd better not …</strong> toʻgʻri — "
                       "<em>should</em> dan keyin <em>to</em> yoʻq, <em>ought</em> dan keyin bor, "
                       "<em>not</em> esa <em>better</em> dan keyin.)</em></p>",
    },
]


# =====================================================================
# PE-47 — Modals of Deduction
# =====================================================================

Q_PE47 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz worked all night. He ___ be tired.</strong></p>",
        "choices": ["must", "can't", "mustn't", "shouldn't"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — <em>must be</em> = I am almost certain it "
                       "is true (about 95%).<br><br>"
                       "<em>(<strong>must</strong> toʻgʻri — <em>must be</em> = deyarli aminman, shunday "
                       "(taxminan 95%).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>That ___ be Iroda — she is in Tashkent today.</strong></p>",
        "choices": ["can't", "mustn't", "shouldn't", "wouldn't"],
        "correct": "can't",
        "explanation": "<p><strong>can't</strong> is correct — <em>can't be</em> = I am almost certain it "
                       "is false. This is the opposite of <em>must be</em>.<br><br>"
                       "<em>(<strong>can't</strong> toʻgʻri — <em>can't be</em> = deyarli aminman, bunday "
                       "emas. Bu <em>must be</em> ning aksi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the opposite of <em>must be</em>?</strong></p>",
        "choices": ["can't be", "mustn't be", "shouldn't be", "won't be"],
        "correct": "can't be",
        "explanation": "<p><strong>can't be</strong> is correct — and this is the key point of the "
                       "lesson: <em>mustn't be</em> means “it is forbidden”, not “it is impossible”."
                       "<br><br><em>(<strong>can't be</strong> toʻgʻri — darsning eng muhim nuqtasi shu: "
                       "<em>mustn't be</em> “taqiqlangan” degani, “boʻlishi mumkin emas” "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ be in the library — she sometimes studies there.</strong></p>",
        "choices": ["might", "must", "can't", "shouldn't"],
        "correct": "might",
        "explanation": "<p><strong>might</strong> is correct — around 50%: possible, but not "
                       "certain.<br><br>"
                       "<em>(<strong>might</strong> toʻgʻri — taxminan 50%: mumkin, lekin aniq "
                       "emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar has won the olympiad. He ___ very clever.</strong></p>",
        "choices": ["must be", "can't be", "mustn't be", "must to be"],
        "correct": "must be",
        "explanation": "<p><strong>must be</strong> is correct — the evidence makes the conclusion almost "
                       "certain.<br><br>"
                       "<em>(<strong>must be</strong> toʻgʻri — dalil xulosani deyarli aniq "
                       "qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The lights are off. Elbek's family ___ out.</strong></p>",
        "choices": ["must be", "can't be", "shouldn't be", "mustn't be"],
        "correct": "must be",
        "explanation": "<p><strong>must be</strong> is correct — the dark windows are the evidence for "
                       "the guess.<br><br>"
                       "<em>(<strong>must be</strong> toʻgʻri — qorongʻi derazalar — taxmin uchun "
                       "dalil.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>They ___ be asleep — it's midday!</strong></p>",
        "choices": ["can't", "must", "might not be", "shouldn't"],
        "correct": "can't",
        "explanation": "<p><strong>can't</strong> is correct — midday makes sleeping almost "
                       "impossible.<br><br>"
                       "<em>(<strong>can't</strong> toʻgʻri — tush payti uxlashni deyarli imkonsiz "
                       "qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs isn't answering. He ___ be in a lesson.</strong></p>",
        "choices": ["may", "can't", "mustn't", "shouldn't"],
        "correct": "may",
        "explanation": "<p><strong>may</strong> is correct — a possible explanation among several."
                       "<br><br><em>(<strong>may</strong> toʻgʻri — bir necha mumkin boʻlgan "
                       "izohlardan biri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ know the answer — he teaches this subject.</strong></p>",
        "choices": ["must", "can't", "mustn't", "may not"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — deduction works with any verb, not only "
                       "<em>be</em>: <em>must know, must have, must live</em>.<br><br>"
                       "<em>(<strong>must</strong> toʻgʻri — xulosa faqat <em>be</em> bilan emas, har "
                       "qanday feʼl bilan ishlaydi: <em>must know, must have, must live</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence shows about 5% certainty?</strong></p>",
        "choices": ["That can't be true.", "That must be true.",
                    "That might be true.", "That may be true."],
        "correct": "That can't be true.",
        "explanation": "<p><strong>That can't be true.</strong> is correct — the bottom of the scale: "
                       "almost certainly false.<br><br>"
                       "<em>(<strong>That can't be true.</strong> toʻgʻri — shkalaning eng pasti: "
                       "deyarli aniq notoʻgʻri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir's bag is here, so he ___ be somewhere in the school.</strong></p>",
        "choices": ["must", "can't", "mustn't", "wouldn't"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — the bag is the clue that leads to the "
                       "conclusion.<br><br>"
                       "<em>(<strong>must</strong> toʻgʻri — sumka — xulosaga olib boradigan "
                       "dalil.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina ___ be hungry — she has just had lunch.</strong></p>",
        "choices": ["can't", "must", "might", "may well"],
        "correct": "can't",
        "explanation": "<p><strong>can't</strong> is correct — having just eaten makes hunger almost "
                       "impossible.<br><br>"
                       "<em>(<strong>can't</strong> toʻgʻri — hozirgina ovqatlangani ochlikni deyarli "
                       "imkonsiz qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Somebody is knocking. It ___ be Sirojiddin — he said he would "
                "come.</strong></p>",
        "choices": ["could", "can't", "mustn't", "shouldn't"],
        "correct": "could",
        "explanation": "<p><strong>could</strong> is correct — <em>could be</em> sits with <em>might "
                       "be</em> and <em>may be</em> in the middle of the scale.<br><br>"
                       "<em>(<strong>could</strong> toʻgʻri — <em>could be</em> shkalaning oʻrtasida "
                       "<em>might be</em> va <em>may be</em> bilan birga turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “Shaxzoda mustn't be at home” mean?</strong></p>",
        "choices": ["She is forbidden to be at home.",
                    "I'm sure she isn't at home.",
                    "She might not be at home.",
                    "She probably is at home."],
        "correct": "She is forbidden to be at home.",
        "explanation": "<p><strong>She is forbidden to be at home.</strong> is correct — and that is why "
                       "you must say <em>can't be</em> when you mean “I'm sure she isn't”.<br><br>"
                       "<em>(<strong>Unga uyda boʻlish taqiqlangan.</strong> toʻgʻri — shuning uchun "
                       "“aminman, u uyda emas” demoqchi boʻlsangiz, <em>can't be</em> deyish "
                       "kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>He ___ be Abdulloh's brother — they look identical. It ___ be "
                "a coincidence.</strong></p>",
        "choices": ["must … can't", "can't … must", "might … mustn't", "must … mustn't"],
        "correct": "must … can't",
        "explanation": "<p><strong>must … can't</strong> is correct — a confident positive guess and a "
                       "confident negative one.<br><br>"
                       "<em>(<strong>must … can't</strong> toʻgʻri — ishonchli tasdiq taxmini va "
                       "ishonchli inkor taxmini.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona ___ be studying — her light is on.</strong></p>",
        "choices": ["must", "can't", "mustn't", "shouldn't"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — deduction can also use a continuous form: "
                       "<em>must be studying</em> = I'm sure she is studying now.<br><br>"
                       "<em>(<strong>must</strong> toʻgʻri — xulosa continuous shakl bilan ham keladi: "
                       "<em>must be studying</em> = aminman, u hozir oʻqiyapti.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["That mustn't be Davron — he's in Bukhara.",
                    "That can't be Davron — he's in Bukhara.",
                    "That must be Davron — I recognise his coat.",
                    "That might be Davron — I'm not sure."],
        "correct": "That mustn't be Davron — he's in Bukhara.",
        "explanation": "<p><strong>That mustn't be Davron …</strong> is the mistake — <em>mustn't</em> "
                       "forbids, it does not deny. The right word is <em>can't</em>.<br><br>"
                       "<em>(<strong>That mustn't be Davron …</strong> xato — <em>mustn't</em> taqiqlaydi, "
                       "inkor qilmaydi. Toʻgʻri soʻz — <em>can't</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Ilgʻor must be at the stadium now.", "Ilgʻor must to be at the stadium now.",
                    "Ilgʻor musts be at the stadium now.", "Ilgʻor is must be at the stadium now."],
        "correct": "Ilgʻor must be at the stadium now.",
        "explanation": "<p><strong>Ilgʻor must be at the stadium now.</strong> is correct — modal + base "
                       "verb, unchanged.<br><br>"
                       "<em>(<strong>Ilgʻor must be at the stadium now.</strong> toʻgʻri — modal + "
                       "oʻzgarmagan asosiy feʼl.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Iroda:</strong> There's a light on in the classroom at ten at night.</p>"
                "<p><strong>Charos:</strong> ___</p>",
        "choices": ["It must be Rozimurod teacher — he often marks tests late.",
                    "It mustn't be Rozimurod teacher — he often marks tests late.",
                    "It can't be Rozimurod teacher — he often marks tests late.",
                    "It must to be Rozimurod teacher — he often marks tests late."],
        "correct": "It must be Rozimurod teacher — he often marks tests late.",
        "explanation": "<p><strong>It must be Rozimurod teacher …</strong> is correct — the second half "
                       "gives the evidence, so the guess is confident and positive.<br><br>"
                       "<em>(<strong>It must be Rozimurod teacher …</strong> toʻgʻri — gapning ikkinchi "
                       "qismi dalil beradi, shuning uchun taxmin ishonchli va tasdiq.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> deduction is correct.</p>",
        "choices": ["He must be tired, he can't be hungry, and he might be at home.",
                    "He must be tired, he mustn't be hungry, and he can be at home.",
                    "He can't be tired, he must to be hungry, and he mights be at home.",
                    "He musts be tired, he can't to be hungry, and he might to be at home."],
        "correct": "He must be tired, he can't be hungry, and he might be at home.",
        "explanation": "<p><strong>must be … can't be … might be</strong> is correct — the three points "
                       "of the scale, each with a bare verb after the modal.<br><br>"
                       "<em>(<strong>must be … can't be … might be</strong> toʻgʻri — shkalaning uchta "
                       "nuqtasi, har birida modaldan keyin oʻzgarmagan feʼl.)</em></p>",
    },
]


# =====================================================================
# PE-48 — Modals in the Past
# =====================================================================

Q_PE48 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the formula for modals in the past?</strong></p>",
        "choices": ["modal + have + V3", "modal + had + V3",
                    "modal + has + V2", "modal + have + V2"],
        "correct": "modal + have + V3",
        "explanation": "<p><strong>modal + have + V3</strong> is correct — <em>have</em> never becomes "
                       "<em>has</em> or <em>had</em>, and the verb is always the third form.<br><br>"
                       "<em>(<strong>modal + have + V3</strong> toʻgʻri — <em>have</em> hech qachon "
                       "<em>has</em> yoki <em>had</em> ga aylanmaydi, feʼl esa doim uchinchi "
                       "shaklda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona ___ forgotten — she never misses a lesson.</strong></p>",
        "choices": ["must have", "must has", "must had", "musts have"],
        "correct": "must have",
        "explanation": "<p><strong>must have</strong> is correct — a confident guess about the "
                       "past.<br><br>"
                       "<em>(<strong>must have</strong> toʻgʻri — oʻtmish haqidagi ishonchli "
                       "taxmin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ seen the film — he was at football all evening.</strong></p>",
        "choices": ["can't have", "mustn't have", "shouldn't have", "wouldn't have"],
        "correct": "can't have",
        "explanation": "<p><strong>can't have</strong> is correct — the past version of <em>can't "
                       "be</em>: almost certainly it did not happen.<br><br>"
                       "<em>(<strong>can't have</strong> toʻgʻri — <em>can't be</em> ning oʻtmishdagi "
                       "shakli: deyarli aniq, bu boʻlmagan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda ___ told me earlier — now it's too late to help.</strong></p>",
        "choices": ["should have", "should has", "must have", "can't have"],
        "correct": "should have",
        "explanation": "<p><strong>should have</strong> is correct — regret or gentle criticism: the "
                       "right thing did not happen.<br><br>"
                       "<em>(<strong>should have</strong> toʻgʻri — afsus yoki yumshoq tanqid: kerakli "
                       "ish bajarilmagan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ studied harder — she failed the test.</strong></p>",
        "choices": ["should have", "must have", "can't have", "might have"],
        "correct": "should have",
        "explanation": "<p><strong>should have</strong> is correct — looking back at what would have been "
                       "better.<br><br>"
                       "<em>(<strong>should have</strong> toʻgʻri — nima qilish kerak edi, deb orqaga "
                       "qarash.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ have taken the wrong bus — he is very late.</strong></p>",
        "choices": ["might", "should", "can't", "mustn't"],
        "correct": "might",
        "explanation": "<p><strong>might</strong> is correct — a possible explanation for the past, "
                       "around 50%.<br><br>"
                       "<em>(<strong>might</strong> toʻgʻri — oʻtmish uchun mumkin boʻlgan izoh, taxminan "
                       "50%.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek ___ won the race, but he fell at the last moment.</strong></p>",
        "choices": ["could have", "must have", "should has", "can't have"],
        "correct": "could have",
        "explanation": "<p><strong>could have</strong> is correct — it was possible, but it did not "
                       "happen.<br><br>"
                       "<em>(<strong>could have</strong> toʻgʻri — bu mumkin edi, lekin sodir "
                       "boʻlmadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>You ___ have told me! I waited two hours.</strong></p>",
        "choices": ["should", "must", "can't", "might not"],
        "correct": "should",
        "explanation": "<p><strong>should</strong> is correct — criticism of something that was not "
                       "done.<br><br>"
                       "<em>(<strong>should</strong> toʻgʻri — bajarilmagan ish uchun tanqid.)</em></p>",
    },
    {
        "text": "<p>Choose the correct negative.</p>"
                "<p><strong>Firdavs ___ have eaten so much cake — he feels ill now.</strong></p>",
        "choices": ["shouldn't", "mustn't", "can't", "couldn't"],
        "correct": "shouldn't",
        "explanation": "<p><strong>shouldn't</strong> is correct — regret about something that was "
                       "done.<br><br>"
                       "<em>(<strong>shouldn't</strong> toʻgʻri — bajarilgan ish uchun "
                       "afsus.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir isn't here. He ___ have gone home already.</strong></p>",
        "choices": ["must", "should", "can't", "shouldn't"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — the empty seat is the evidence for the "
                       "conclusion.<br><br>"
                       "<em>(<strong>must</strong> toʻgʻri — boʻsh joy — xulosa uchun dalil.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which V3 is correct?</strong></p>"
                "<p><strong>Madina must have ___ the bus.</strong></p>",
        "choices": ["missed", "miss", "missing", "misses"],
        "correct": "missed",
        "explanation": "<p><strong>missed</strong> is correct — after <em>have</em> the third form is "
                       "required.<br><br>"
                       "<em>(<strong>missed</strong> toʻgʻri — <em>have</em> dan keyin uchinchi shakl "
                       "talab qilinadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda can't have ___ that — she is always polite.</strong></p>",
        "choices": ["said", "say", "says", "saying"],
        "correct": "said",
        "explanation": "<p><strong>said</strong> is correct — <em>say → said → said</em>, and the third "
                       "form follows <em>have</em>.<br><br>"
                       "<em>(<strong>said</strong> toʻgʻri — <em>say → said → said</em>, <em>have</em> "
                       "dan keyin uchinchi shakl keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher ___ have marked our tests — he looked very "
                "tired.</strong></p>",
        "choices": ["may", "should", "can't", "mustn't"],
        "correct": "may",
        "explanation": "<p><strong>may</strong> is correct — a possible past explanation for how he "
                       "looked.<br><br>"
                       "<em>(<strong>may</strong> toʻgʻri — uning koʻrinishi uchun mumkin boʻlgan "
                       "oʻtmishdagi izoh.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “Abdulloh could have helped us” mean?</strong></p>",
        "choices": ["He was able to help, but he didn't.",
                    "He helped us successfully.",
                    "He will help us tomorrow.",
                    "He was not able to help at all."],
        "correct": "He was able to help, but he didn't.",
        "explanation": "<p><strong>He was able to help, but he didn't.</strong> is correct — "
                       "<em>could have</em> describes an unused possibility, often with "
                       "disappointment.<br><br>"
                       "<em>(<strong>U yordam bera olardi, lekin bermadi.</strong> toʻgʻri — <em>could "
                       "have</em> ishlatilmagan imkoniyatni, koʻpincha xafagarchilik bilan "
                       "bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Sirojiddin ___ have missed the train, so he ___ have arrived by "
                "now.</strong></p>",
        "choices": ["must … can't", "can't … must", "should … might", "might … shouldn't"],
        "correct": "must … can't",
        "explanation": "<p><strong>must … can't</strong> is correct — a confident past guess, then a "
                       "confident past denial.<br><br>"
                       "<em>(<strong>must … can't</strong> toʻgʻri — oʻtmish haqida ishonchli taxmin, "
                       "keyin ishonchli inkor.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Davron ___ have known about the test — nobody told him.</strong></p>",
        "choices": ["can't", "must", "should", "mustn't"],
        "correct": "can't",
        "explanation": "<p><strong>can't</strong> is correct — with nobody telling him, knowing was "
                       "almost impossible.<br><br>"
                       "<em>(<strong>can't</strong> toʻgʻri — hech kim aytmagan boʻlsa, bilishi deyarli "
                       "imkonsiz edi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Afsona must has forgotten the meeting.",
                    "Afsona must have forgotten the meeting.",
                    "Afsona might have forgotten the meeting.",
                    "Afsona can't have forgotten the meeting."],
        "correct": "Afsona must has forgotten the meeting.",
        "explanation": "<p><strong>Afsona must has forgotten the meeting.</strong> is the mistake — after "
                       "a modal the word is always <em>have</em>, never <em>has</em>.<br><br>"
                       "<em>(<strong>Afsona must has forgotten the meeting.</strong> xato — modaldan "
                       "keyin doim <em>have</em> keladi, <em>has</em> emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["I should have listened to Rozimurod teacher.",
                    "I should have listen to Rozimurod teacher.",
                    "I should had listened to Rozimurod teacher.",
                    "I should have listening to Rozimurod teacher."],
        "correct": "I should have listened to Rozimurod teacher.",
        "explanation": "<p><strong>I should have listened to Rozimurod teacher.</strong> is correct — "
                       "<em>should + have + V3</em>.<br><br>"
                       "<em>(<strong>I should have listened to Rozimurod teacher.</strong> toʻgʻri — "
                       "<em>should + have + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Behruz didn't come to the olympiad.</p>"
                "<p><strong>Marjona:</strong> ___</p>",
        "choices": ["He must have forgotten the date.", "He must has forgotten the date.",
                    "He mustn't have forgotten the date.", "He must have forget the date."],
        "correct": "He must have forgotten the date.",
        "explanation": "<p><strong>He must have forgotten the date.</strong> is correct — the most likely "
                       "past explanation, in the standard formula.<br><br>"
                       "<em>(<strong>He must have forgotten the date.</strong> toʻgʻri — eng ehtimolli "
                       "oʻtmishdagi izoh, standart qolipda.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Ilgʻor should have revised, he could have passed easily, "
                    "and he can't have read the last chapter.",
                    "Ilgʻor should have revise, he could has passed easily, "
                    "and he can't had read the last chapter.",
                    "Ilgʻor should had revised, he could have pass easily, "
                    "and he mustn't have read the last chapter.",
                    "Ilgʻor should have revised, he could have passing easily, "
                    "and he can't have readed the last chapter."],
        "correct": "Ilgʻor should have revised, he could have passed easily, "
                   "and he can't have read the last chapter.",
        "explanation": "<p><strong>should have revised … could have passed … can't have read</strong> is "
                       "correct — regret, an unused possibility and a confident denial, all with "
                       "<em>have + V3</em>.<br><br>"
                       "<em>(<strong>should have revised … could have passed … can't have read</strong> "
                       "toʻgʻri — afsus, ishlatilmagan imkoniyat va ishonchli inkor, hammasi "
                       "<em>have + V3</em> bilan.)</em></p>",
    },
]


# =====================================================================
# PE-49 — Polite Requests, Offers and Permission
# =====================================================================

Q_PE49 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which request is the <em>most</em> polite?</strong></p>",
        "choices": ["Would you mind waiting a moment?", "Can you wait a moment?",
                    "Wait a moment.", "Could you wait a moment?"],
        "correct": "Would you mind waiting a moment?",
        "explanation": "<p><strong>Would you mind waiting a moment?</strong> is correct — the top of the "
                       "ladder: <em>Can you</em> → <em>Could you</em> → <em>Would you</em> → <em>Would "
                       "you mind</em>.<br><br>"
                       "<em>(<strong>Would you mind waiting a moment?</strong> toʻgʻri — narvonning eng "
                       "tepasi: <em>Can you</em> → <em>Could you</em> → <em>Would you</em> → <em>Would "
                       "you mind</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you pass me the salt, Behruz?</strong> (talking to a friend)</p>",
        "choices": ["Can", "Would you mind to", "May", "Shall"],
        "correct": "Can",
        "explanation": "<p><strong>Can</strong> is correct — with family and friends the simplest form is "
                       "perfectly polite.<br><br>"
                       "<em>(<strong>Can</strong> toʻgʻri — oila va doʻstlar bilan eng oddiy shakl "
                       "mutlaqo odobli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you tell me the way to the station, please?</strong></p>",
        "choices": ["Could", "Shall", "Must", "Should"],
        "correct": "Could",
        "explanation": "<p><strong>Could</strong> is correct — <em>Could you + please</em> is the safest "
                       "combination with anybody.<br><br>"
                       "<em>(<strong>Could</strong> toʻgʻri — <em>Could you + please</em> har kim bilan "
                       "ishlatish mumkin boʻlgan eng xavfsiz shakl.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ I ask you something, Rozimurod teacher?</strong></p>",
        "choices": ["May", "Shall", "Would", "Must"],
        "correct": "May",
        "explanation": "<p><strong>May</strong> is correct — the most formal way to ask permission, "
                       "perfect for a teacher.<br><br>"
                       "<em>(<strong>May</strong> toʻgʻri — ruxsat soʻrashning eng rasmiy shakli, "
                       "oʻqituvchiga juda mos.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ I help you with those books?</strong></p>",
        "choices": ["Shall", "Do", "May you", "Would you mind"],
        "correct": "Shall",
        "explanation": "<p><strong>Shall</strong> is correct — <em>Shall I …?</em> offers help.<br><br>"
                       "<em>(<strong>Shall</strong> toʻgʻri — <em>Shall I …?</em> yordam taklif "
                       "qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ we start the lesson now?</strong></p>",
        "choices": ["Shall", "Will we can", "May we to", "Do"],
        "correct": "Shall",
        "explanation": "<p><strong>Shall</strong> is correct — <em>Shall we …?</em> suggests doing "
                       "something together.<br><br>"
                       "<em>(<strong>Shall</strong> toʻgʻri — <em>Shall we …?</em> birgalikda biror ish "
                       "qilishni taklif qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Would you mind ___ the window?</strong></p>",
        "choices": ["closing", "to close", "close", "closed"],
        "correct": "closing",
        "explanation": "<p><strong>closing</strong> is correct — <em>Would you mind</em> is always "
                       "followed by <em>-ing</em>, never by an infinitive.<br><br>"
                       "<em>(<strong>closing</strong> toʻgʻri — <em>Would you mind</em> dan keyin doim "
                       "<em>-ing</em> keladi, infinitiv emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct answer.</p>"
                "<p><strong>Would you mind waiting outside? — ___</strong> (you agree)</p>",
        "choices": ["Not at all.", "Yes, of course.", "Yes, I would.", "Yes, certainly."],
        "correct": "Not at all.",
        "explanation": "<p><strong>Not at all.</strong> is correct — this is the trap: <em>mind</em> "
                       "means “object to”, so “no” is the friendly answer. <em>Yes, I would</em> means "
                       "you refuse.<br><br>"
                       "<em>(<strong>Not at all.</strong> toʻgʻri — bu tuzoq: <em>mind</em> “eʼtiroz "
                       "qilmoq” degani, shuning uchun “yoʻq” — bu rozilik javobi. <em>Yes, I "
                       "would</em> esa rad etish degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you like some tea, Iroda?</strong></p>",
        "choices": ["Would", "Do", "Are", "Shall"],
        "correct": "Would",
        "explanation": "<p><strong>Would</strong> is correct — <em>Would you like …?</em> is the polite "
                       "way to offer something.<br><br>"
                       "<em>(<strong>Would</strong> toʻgʻri — <em>Would you like …?</em> biror narsani "
                       "taklif qilishning odobli shakli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Would you like ___ to our house on Sunday?</strong></p>",
        "choices": ["to come", "coming", "come", "came"],
        "correct": "to come",
        "explanation": "<p><strong>to come</strong> is correct — <em>would like</em> takes the infinitive "
                       "with <em>to</em>, unlike <em>would you mind</em>.<br><br>"
                       "<em>(<strong>to come</strong> toʻgʻri — <em>would like</em> <em>to</em> li "
                       "infinitiv oladi, <em>would you mind</em> dan farqli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ I borrow your dictionary, Charos?</strong></p>",
        "choices": ["Could", "Should", "Must", "Shall"],
        "correct": "Could",
        "explanation": "<p><strong>Could</strong> is correct — <em>Could I …?</em> asks permission "
                       "politely, a step above <em>Can I …?</em><br><br>"
                       "<em>(<strong>Could</strong> toʻgʻri — <em>Could I …?</em> ruxsatni odob bilan "
                       "soʻraydi, <em>Can I …?</em> dan bir pogʻona yuqori.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is a <em>request</em>, not a permission "
                "question?</strong></p>",
        "choices": ["Could you open the window?", "Could I open the window?",
                    "May I open the window?", "Can I open the window?"],
        "correct": "Could you open the window?",
        "explanation": "<p><strong>Could you open the window?</strong> is correct — <em>you</em> asks "
                       "somebody else to act; <em>I</em> asks for permission to act yourself.<br><br>"
                       "<em>(<strong>Could you open the window?</strong> toʻgʻri — <em>you</em> boshqadan "
                       "ish soʻraydi; <em>I</em> esa oʻzi uchun ruxsat soʻraydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar, ___ you mind helping me with this box?</strong></p>",
        "choices": ["would", "will", "do you", "should"],
        "correct": "would",
        "explanation": "<p><strong>would</strong> is correct — <em>Would you mind …?</em> is the fixed "
                       "phrase.<br><br>"
                       "<em>(<strong>would</strong> toʻgʻri — <em>Would you mind …?</em> qatʼiy "
                       "ibora.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which reply <em>refuses</em> politely?</strong></p>",
        "choices": ["I'm afraid I can't — I'm busy right now.",
                    "Of course, no problem.",
                    "Certainly, here you are.",
                    "Not at all, go ahead."],
        "correct": "I'm afraid I can't — I'm busy right now.",
        "explanation": "<p><strong>I'm afraid I can't — I'm busy right now.</strong> is correct — "
                       "<em>I'm afraid</em> softens a refusal, and a reason makes it kinder.<br><br>"
                       "<em>(<strong>I'm afraid I can't — I'm busy right now.</strong> toʻgʻri — "
                       "<em>I'm afraid</em> rad javobini yumshatadi, sabab esa uni yanada "
                       "muloyim qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek, ___ you like me to carry that for you?</strong></p>",
        "choices": ["would", "do", "are", "shall"],
        "correct": "would",
        "explanation": "<p><strong>would</strong> is correct — <em>Would you like me to …?</em> is a very "
                       "polite offer.<br><br>"
                       "<em>(<strong>would</strong> toʻgʻri — <em>Would you like me to …?</em> juda "
                       "odobli taklif.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which is <em>too direct</em> for a stranger?</strong></p>",
        "choices": ["Give me your pen.", "Could you lend me your pen, please?",
                    "Would you mind lending me your pen?", "May I borrow your pen?"],
        "correct": "Give me your pen.",
        "explanation": "<p><strong>Give me your pen.</strong> is correct — the grammar is perfect, the "
                       "manners are not. English wraps requests in modals.<br><br>"
                       "<em>(<strong>Give me your pen.</strong> toʻgʻri — grammatikasi mukammal, odobi "
                       "esa yoʻq. Ingliz tili iltimosni modallarga oʻrab beradi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Would you mind to close the door?", "Would you mind closing the door?",
                    "Could you close the door, please?", "Would you close the door, please?"],
        "correct": "Would you mind to close the door?",
        "explanation": "<p><strong>Would you mind to close the door?</strong> is the mistake — "
                       "<em>mind</em> is followed by <em>-ing</em>.<br><br>"
                       "<em>(<strong>Would you mind to close the door?</strong> xato — <em>mind</em> dan "
                       "keyin <em>-ing</em> keladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Shall I open the window for you?", "Shall you open the window for me?",
                    "Shall he open the window for you?", "Shall I to open the window for you?"],
        "correct": "Shall I open the window for you?",
        "explanation": "<p><strong>Shall I open the window for you?</strong> is correct — modern "
                       "<em>shall</em> lives only with <em>I</em> and <em>we</em>, in questions.<br><br>"
                       "<em>(<strong>Shall I open the window for you?</strong> toʻgʻri — zamonaviy "
                       "<em>shall</em> faqat <em>I</em> va <em>we</em> bilan, savollarda "
                       "ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Madina:</strong> Would you mind if I opened the window?</p>"
                "<p><strong>Javohir:</strong> ___</p>",
        "choices": ["Of course not — please do.", "Yes, of course — please do.",
                    "Yes, I would — please do.", "Certainly I mind — please do."],
        "correct": "Of course not — please do.",
        "explanation": "<p><strong>Of course not — please do.</strong> is correct — you are saying “I "
                       "don't object”, which is why the sentence begins with a negative.<br><br>"
                       "<em>(<strong>Of course not — please do.</strong> toʻgʻri — siz “eʼtirozim yoʻq” "
                       "deyapsiz, shuning uchun javob inkor bilan boshlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Could you help me, please? And would you mind waiting while I find my keys?",
                    "Could you to help me, please? And would you mind to wait while I find my keys?",
                    "Shall you help me, please? And would you mind waited while I find my keys?",
                    "May you help me, please? And would you mind that you wait while I find my keys?"],
        "correct": "Could you help me, please? And would you mind waiting while I find my keys?",
        "explanation": "<p><strong>Could you help … would you mind waiting …</strong> is correct — a bare "
                       "verb after <em>could</em>, an <em>-ing</em> form after <em>mind</em>.<br><br>"
                       "<em>(<strong>Could you help … would you mind waiting …</strong> toʻgʻri — "
                       "<em>could</em> dan keyin oʻzgarmagan feʼl, <em>mind</em> dan keyin esa "
                       "<em>-ing</em> shakli.)</em></p>",
    },
]


# =====================================================================
# PE-50 — shall, will, would: Willingness and Habit
# =====================================================================

Q_PE50 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ I close the window? It's cold in here.</strong></p>",
        "choices": ["Shall", "Will", "Would", "Do"],
        "correct": "Shall",
        "explanation": "<p><strong>Shall</strong> is correct — <em>Shall I …?</em> offers to do something "
                       "for somebody.<br><br>"
                       "<em>(<strong>Shall</strong> toʻgʻri — <em>Shall I …?</em> kimgadir biror ish "
                       "qilishni taklif qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>With which subjects does modern <em>shall</em> live?</strong></p>",
        "choices": ["I and we", "he and she", "you and they", "all subjects equally"],
        "correct": "I and we",
        "explanation": "<p><strong>I and we</strong> is correct — and almost only in questions: "
                       "<em>Shall I …? Shall we …?</em><br><br>"
                       "<em>(<strong>I va we</strong> toʻgʻri — va deyarli faqat savollarda: <em>Shall I "
                       "…? Shall we …?</em>)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ we go to the cinema this evening?</strong></p>",
        "choices": ["Shall", "Will", "Do", "Would"],
        "correct": "Shall",
        "explanation": "<p><strong>Shall</strong> is correct — <em>Shall we …?</em> suggests doing "
                       "something together.<br><br>"
                       "<em>(<strong>Shall</strong> toʻgʻri — <em>Shall we …?</em> birga biror ish "
                       "qilishni taklif qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The door ___ open — it's stuck.</strong></p>",
        "choices": ["won't", "doesn't will", "wouldn't be", "shan't"],
        "correct": "won't",
        "explanation": "<p><strong>won't</strong> is correct — English lets even objects “refuse”: "
                       "<em>the door won't open, the car won't start</em>.<br><br>"
                       "<em>(<strong>won't</strong> toʻgʻri — ingliz tilida hatto narsalar ham “rad "
                       "etadi”: <em>the door won't open, the car won't start</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ help us — he says he is too busy.</strong></p>",
        "choices": ["won't", "shan't", "wouldn't be", "doesn't will"],
        "correct": "won't",
        "explanation": "<p><strong>won't</strong> is correct — a refusal in the present: he is not "
                       "willing.<br><br>"
                       "<em>(<strong>won't</strong> toʻgʻri — hozirgi zamondagi rad javobi: u "
                       "xohlamayapti.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My old bicycle ___ start yesterday, so I walked.</strong></p>",
        "choices": ["wouldn't", "won't", "shan't", "shouldn't"],
        "correct": "wouldn't",
        "explanation": "<p><strong>wouldn't</strong> is correct — <em>wouldn't</em> is the past of this "
                       "“refusing” <em>won't</em>.<br><br>"
                       "<em>(<strong>wouldn't</strong> toʻgʻri — <em>wouldn't</em> — “rad etadigan” "
                       "<em>won't</em> ning oʻtgan zamon shakli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda ___ like a glass of tea.</strong></p>",
        "choices": ["would", "will", "shall", "does"],
        "correct": "would",
        "explanation": "<p><strong>would</strong> is correct — <em>would like</em> = want, politely."
                       "<br><br><em>(<strong>would</strong> toʻgʻri — <em>would like</em> = odob bilan "
                       "“xohlayman”.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which is more polite?</strong></p>",
        "choices": ["I would like some water.", "I want some water.",
                    "Give me some water.", "I will water."],
        "correct": "I would like some water.",
        "explanation": "<p><strong>I would like some water.</strong> is correct — <em>I want</em> is "
                       "grammatical but sounds blunt to English ears.<br><br>"
                       "<em>(<strong>I would like some water.</strong> toʻgʻri — <em>I want</em> "
                       "grammatik jihatdan toʻgʻri, lekin inglizlarga qoʻpol eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>When we were children, my grandfather ___ tell us long stories every "
                "evening.</strong></p>",
        "choices": ["would", "will", "shall", "should"],
        "correct": "would",
        "explanation": "<p><strong>would</strong> is correct — <em>would</em> for repeated past actions, "
                       "just like <em>used to</em> in PE-25.<br><br>"
                       "<em>(<strong>would</strong> toʻgʻri — takrorlangan oʻtmish harakatlari uchun "
                       "<em>would</em>, xuddi PE-25 dagi <em>used to</em> kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is <em>wrong</em> with <em>would</em>?</strong></p>",
        "choices": ["We would have a big house when I was small.",
                    "We would visit our grandmother every summer.",
                    "My father would read to us at bedtime.",
                    "We would walk to school together."],
        "correct": "We would have a big house when I was small.",
        "explanation": "<p><strong>We would have a big house when I was small.</strong> is wrong — "
                       "<em>have</em> here is a state, and <em>would</em> only covers repeated actions. "
                       "Use <em>used to have</em>.<br><br>"
                       "<em>(<strong>We would have a big house when I was small.</strong> xato — bu "
                       "yerda <em>have</em> holat, <em>would</em> esa faqat takrorlanadigan "
                       "harakatlarni qamraydi. <em>Used to have</em> ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you help me with this box, Charos?</strong></p>",
        "choices": ["Would", "Shall", "Should", "Do"],
        "correct": "Would",
        "explanation": "<p><strong>Would</strong> is correct — a polite request, one step above "
                       "<em>could</em>.<br><br>"
                       "<em>(<strong>Would</strong> toʻgʻri — odobli iltimos, <em>could</em> dan bir "
                       "pogʻona yuqori.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In “Samandar'd like some help”, what does <em>'d</em> mean?</strong></p>",
        "choices": ["would", "had", "did", "should"],
        "correct": "would",
        "explanation": "<p><strong>would</strong> is correct — before <em>like</em> the <em>'d</em> is "
                       "always <em>would</em>. Before a V3 it would be <em>had</em>.<br><br>"
                       "<em>(<strong>would</strong> toʻgʻri — <em>like</em> dan oldin <em>'d</em> doim "
                       "<em>would</em> boʻladi. V3 dan oldin esa <em>had</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In “Elbek'd already left”, what does <em>'d</em> mean?</strong></p>",
        "choices": ["had", "would", "did", "could"],
        "correct": "had",
        "explanation": "<p><strong>had</strong> is correct — <em>left</em> is a third form, so this is "
                       "the Past Perfect.<br><br>"
                       "<em>(<strong>had</strong> toʻgʻri — <em>left</em> uchinchi shakl, yaʼni bu Past "
                       "Perfect.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ rather stay at home tonight.</strong></p>",
        "choices": ["would", "will", "shall", "should"],
        "correct": "would",
        "explanation": "<p><strong>would</strong> is correct — <em>would rather + base verb</em> = "
                       "prefer.<br><br>"
                       "<em>(<strong>would</strong> toʻgʻri — <em>would rather + asosiy feʼl</em> = "
                       "afzal koʻrmoq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir would rather ___ football than watch it.</strong></p>",
        "choices": ["play", "to play", "playing", "played"],
        "correct": "play",
        "explanation": "<p><strong>play</strong> is correct — the base verb follows <em>would "
                       "rather</em>, with no <em>to</em>.<br><br>"
                       "<em>(<strong>play</strong> toʻgʻri — <em>would rather</em> dan keyin <em>to</em> "
                       "siz asosiy feʼl keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The computer ___ save my file, so I lost the whole essay.</strong></p>",
        "choices": ["wouldn't", "won't", "shouldn't", "mustn't"],
        "correct": "wouldn't",
        "explanation": "<p><strong>wouldn't</strong> is correct — an object refusing to work, in the "
                       "past.<br><br>"
                       "<em>(<strong>wouldn't</strong> toʻgʻri — oʻtmishda ishlashdan “bosh tortgan” "
                       "narsa.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Shall he help you with your bag?", "Shall I help you with your bag?",
                    "Shall we help you with your bag?", "Would you like some help with your bag?"],
        "correct": "Shall he help you with your bag?",
        "explanation": "<p><strong>Shall he help you with your bag?</strong> is the mistake — modern "
                       "<em>shall</em> works only with <em>I</em> and <em>we</em>.<br><br>"
                       "<em>(<strong>Shall he help you with your bag?</strong> xato — zamonaviy "
                       "<em>shall</em> faqat <em>I</em> va <em>we</em> bilan ishlaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Shaxzoda would like to join us.", "Shaxzoda would like join us.",
                    "Shaxzoda will like to join us tonight, she'd rather.",
                    "Shaxzoda would likes to join us."],
        "correct": "Shaxzoda would like to join us.",
        "explanation": "<p><strong>Shaxzoda would like to join us.</strong> is correct — "
                       "<em>would like + to + verb</em>, and modals never take <em>-s</em>.<br><br>"
                       "<em>(<strong>Shaxzoda would like to join us.</strong> toʻgʻri — "
                       "<em>would like + to + feʼl</em>, modallar esa hech qachon <em>-s</em> "
                       "olmaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> The board is dirty.</p>"
                "<p><strong>Abdulloh:</strong> ___</p>",
        "choices": ["Shall I clean it?", "Will I clean it?",
                    "Would I clean it?", "Shall I to clean it?"],
        "correct": "Shall I clean it?",
        "explanation": "<p><strong>Shall I clean it?</strong> is correct — offering help. <em>Will I "
                       "…?</em> would sound like a question about his own future.<br><br>"
                       "<em>(<strong>Shall I clean it?</strong> toʻgʻri — yordam taklifi. <em>Will I "
                       "…?</em> esa oʻz kelajagi haqidagi savoldek eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Shall we start? I'd like some tea first, and my brother would always "
                    "make it for me when we were small.",
                    "Shall we start? I'd like some tea first, and my brother will always "
                    "make it for me when we were small.",
                    "Will we start? I'd like some tea first, and my brother would always "
                    "made it for me when we were small.",
                    "Shall we start? I would like some tea first, and my brother would always "
                    "have a teapot when we were small."],
        "correct": "Shall we start? I'd like some tea first, and my brother would always "
                   "make it for me when we were small.",
        "explanation": "<p><strong>Shall we … I'd like … would always make …</strong> is correct — a "
                       "suggestion, a polite want, and a repeated past action.<br><br>"
                       "<em>(<strong>Shall we … I'd like … would always make …</strong> toʻgʻri — "
                       "taklif, odobli xohish va takrorlangan oʻtmish harakati.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-46 Practice: should, ought to, had better: Advice",
        "tutorial":    "PE-46:",
        "description": "PE-46 darsiga 20 savol: should bilan maslahat va kutilma, to ni saqlaydigan "
                       "ought to, hamda ogohlantirishli had better (va had better not). Javoblar "
                       "ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE46,
    },
    {
        "title":       "PE-47 Practice: Modals of Deduction: must be, can't be, might be",
        "tutorial":    "PE-47:",
        "description": "PE-47 darsiga 20 savol: must be (95%), might/may/could be (50%), can't be "
                       "(5%) va eng muhimi — must be ning aksi mustn't be emas, can't be ekani. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE47,
    },
    {
        "title":       "PE-48 Practice: Modals in the Past: must have, should have, could have",
        "tutorial":    "PE-48:",
        "description": "PE-48 darsiga 20 savol: modal + have + V3 qolipi, oʻtmish haqida xulosa, "
                       "should have bilan afsus va could have bilan ishlatilmagan imkoniyat. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE48,
    },
    {
        "title":       "PE-49 Practice: Polite Requests, Offers and Permission",
        "tutorial":    "PE-49:",
        "description": "PE-49 darsiga 20 savol: odob narvoni (Can you → Could you → Would you → "
                       "Would you mind), ruxsat soʻrash, taklif qilish va Would you mind…? "
                       "tuzogʻi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE49,
    },
    {
        "title":       "PE-50 Practice: shall, will, would: Willingness and Habit",
        "tutorial":    "PE-50:",
        "description": "PE-50 darsiga 20 savol: Shall I / Shall we bilan taklif, won't va wouldn't "
                       "bilan rad javobi, would like / would rather hamda 'd = would yoki had "
                       "tuzogʻi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE50,
    },
]
