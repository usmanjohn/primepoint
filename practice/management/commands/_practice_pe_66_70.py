# -*- coding: utf-8 -*-
"""Prime English practices — PE-66 … PE-70.

The causative closes Block E; PE-67 opens Block F, where the level becomes `hard`.
Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_66_70.py --master=prime --expect-questions=20
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
# PE-66 — The Causative
# =====================================================================

Q_PE66 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda ___ her hair cut at the hairdresser's yesterday.</strong></p>",
        "choices": ["had", "has", "did", "made"],
        "correct": "had",
        "explanation": "<p><strong>had</strong> is correct — the causative is "
                       "<em>have + object + V3</em>: somebody else did it for her.<br><br>"
                       "<em>(<strong>had</strong> toʻgʻri — kauzativ qolip <em>have + toʻldiruvchi + "
                       "V3</em>: buni uning oʻrniga boshqa kishi bajargan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “I cut my hair yesterday” mean to an English speaker?</strong></p>",
        "choices": ["I cut it myself, with my own scissors.",
                    "A barber cut it for me.",
                    "My hair was long.",
                    "I wanted a haircut."],
        "correct": "I cut it myself, with my own scissors.",
        "explanation": "<p><strong>I cut it myself, with my own scissors.</strong> is correct — that is "
                       "exactly why the causative exists: <em>I had my hair cut</em> is what you "
                       "mean.<br><br>"
                       "<em>(<strong>Oʻzim, oʻz qaychim bilan kesdim.</strong> toʻgʻri — kauzativ aynan "
                       "shuning uchun kerak: <em>I had my hair cut</em> demoqchisiz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct word order.</p>",
        "choices": ["Behruz had his bicycle repaired.", "Behruz had repaired his bicycle.",
                    "Behruz had his bicycle repair.", "Behruz repaired had his bicycle."],
        "correct": "Behruz had his bicycle repaired.",
        "explanation": "<p><strong>Behruz had his bicycle repaired.</strong> is correct — the object "
                       "comes <em>before</em> the V3. <em>Had repaired his bicycle</em> is just the past "
                       "perfect, meaning he did it himself.<br><br>"
                       "<em>(<strong>Behruz had his bicycle repaired.</strong> toʻgʻri — toʻldiruvchi V3 "
                       "dan <em>oldin</em> keladi. <em>Had repaired his bicycle</em> esa oddiy past "
                       "perfect boʻlib, u oʻzi tuzatgan degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos is going to ___ her photo taken for the documents.</strong></p>",
        "choices": ["get", "make", "let", "do"],
        "correct": "get",
        "explanation": "<p><strong>get</strong> is correct — <em>get + object + V3</em> means the same as "
                       "<em>have</em>, but sounds more informal.<br><br>"
                       "<em>(<strong>get</strong> toʻgʻri — <em>get + toʻldiruvchi + V3</em> "
                       "<em>have</em> bilan bir xil maʼnoda, lekin norasmiyroq eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar's family had their house ___ last summer.</strong></p>",
        "choices": ["painted", "paint", "painting", "to paint"],
        "correct": "painted",
        "explanation": "<p><strong>painted</strong> is correct — the third form always follows the "
                       "object.<br><br>"
                       "<em>(<strong>painted</strong> toʻgʻri — toʻldiruvchidan keyin doim uchinchi shakl "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek ___ his phone stolen at the bazaar.</strong></p>",
        "choices": ["had", "did", "made", "let"],
        "correct": "had",
        "explanation": "<p><strong>had</strong> is correct — the second meaning of the causative: "
                       "something bad happened to him. He certainly did not arrange it.<br><br>"
                       "<em>(<strong>had</strong> toʻgʻri — kauzativning ikkinchi maʼnosi: unga yomon "
                       "voqea yuz bergan. Buni u albatta uyushtirmagan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “Firdavs had his wallet stolen” mean?</strong></p>",
        "choices": ["Somebody stole it from him.",
                    "He asked somebody to steal it.",
                    "He stole a wallet.",
                    "He lost his wallet on purpose."],
        "correct": "Somebody stole it from him.",
        "explanation": "<p><strong>Somebody stole it from him.</strong> is correct — with unpleasant "
                       "events, <em>have something done</em> means it happened <em>to</em> you.<br><br>"
                       "<em>(<strong>Kimdir undan oʻgʻirlagan.</strong> toʻgʻri — yoqimsiz voqealarda "
                       "<em>have something done</em> bu sizning boshingizga tushgan degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher had us ___ the exercise twice.</strong></p>",
        "choices": ["do", "to do", "done", "doing"],
        "correct": "do",
        "explanation": "<p><strong>do</strong> is correct — <em>have + person + base verb</em> means "
                       "making or getting somebody to act.<br><br>"
                       "<em>(<strong>do</strong> toʻgʻri — <em>have + shaxs + asosiy feʼl</em> kimnidir "
                       "biror ish qilishga undash degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir got his brother ___ him with the project.</strong></p>",
        "choices": ["to help", "help", "helped", "helping"],
        "correct": "to help",
        "explanation": "<p><strong>to help</strong> is correct — <em>get + person + to + verb</em> keeps "
                       "its <em>to</em>, while <em>have + person + verb</em> does not.<br><br>"
                       "<em>(<strong>to help</strong> toʻgʻri — <em>get + shaxs + to + feʼl</em> "
                       "<em>to</em> ni saqlaydi, <em>have + shaxs + feʼl</em> esa saqlamaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina needs to ___ her eyes tested.</strong></p>",
        "choices": ["have", "make", "let", "do"],
        "correct": "have",
        "explanation": "<p><strong>have</strong> is correct — a professional will do it for her.<br><br>"
                       "<em>(<strong>have</strong> toʻgʻri — buni uning uchun mutaxassis bajaradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence means somebody else did the work?</strong></p>",
        "choices": ["Shaxzoda had her dress made.", "Shaxzoda made her dress.",
                    "Shaxzoda has made her dress.", "Shaxzoda had made her dress."],
        "correct": "Shaxzoda had her dress made.",
        "explanation": "<p><strong>Shaxzoda had her dress made.</strong> is correct — object before V3. "
                       "The last option is the past perfect and means she made it herself.<br><br>"
                       "<em>(<strong>Shaxzoda had her dress made.</strong> toʻgʻri — toʻldiruvchi V3 dan "
                       "oldin. Oxirgi variant past perfect boʻlib, u oʻzi tikkan degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh ___ his composition checked by Rozimurod teacher.</strong></p>",
        "choices": ["had", "was", "did", "made"],
        "correct": "had",
        "explanation": "<p><strong>had</strong> is correct — and <em>by</em> can name the person, exactly "
                       "as in the passive.<br><br>"
                       "<em>(<strong>had</strong> toʻgʻri — <em>by</em> esa xuddi passivdagidek shaxsni "
                       "koʻrsatishi mumkin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin is having a new window ___ in his room.</strong></p>",
        "choices": ["fitted", "fit", "fitting", "to fit"],
        "correct": "fitted",
        "explanation": "<p><strong>fitted</strong> is correct — the causative works in any tense, because "
                       "only <em>have</em> changes.<br><br>"
                       "<em>(<strong>fitted</strong> toʻgʻri — kauzativ har qanday zamonda ishlaydi, "
                       "chunki faqat <em>have</em> oʻzgaradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona will ___ her computer repaired tomorrow.</strong></p>",
        "choices": ["have", "has", "had", "having"],
        "correct": "have",
        "explanation": "<p><strong>have</strong> is correct — after <em>will</em> the base form is "
                       "required.<br><br>"
                       "<em>(<strong>have</strong> toʻgʻri — <em>will</em> dan keyin asosiy shakl talab "
                       "qilinadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which Uzbek idea matches the causative?</strong></p>",
        "choices": ["-tirdim (sochimni oldirdim)", "-yapman", "-gan edi", "-moqchiman"],
        "correct": "-tirdim (sochimni oldirdim)",
        "explanation": "<p><strong>-tirdim</strong> is correct — Uzbek does exactly the same job with this "
                       "suffix, which is why the idea is already familiar to you.<br><br>"
                       "<em>(<strong>-tirdim</strong> toʻgʻri — oʻzbek tili bu vazifani aynan shu "
                       "qoʻshimcha bilan bajaradi, shuning uchun gʻoya sizga allaqachon tanish.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Davron ___ his hair cut and then ___ his photo taken.</strong></p>",
        "choices": ["had … had", "had … has", "did … had", "made … got to"],
        "correct": "had … had",
        "explanation": "<p><strong>had … had</strong> is correct — two services, both arranged by "
                       "him.<br><br>"
                       "<em>(<strong>had … had</strong> toʻgʻri — ikki xizmat, ikkalasini ham u "
                       "uyushtirgan.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Afsona had cut her hair at the hairdresser's.",
                    "Afsona had her hair cut at the hairdresser's.",
                    "Afsona got her hair cut at the hairdresser's.",
                    "Afsona is having her hair cut at the hairdresser's."],
        "correct": "Afsona had cut her hair at the hairdresser's.",
        "explanation": "<p><strong>Afsona had cut her hair at the hairdresser's.</strong> is the mistake "
                       "in this context — that word order is the past perfect and says she cut it "
                       "herself.<br><br>"
                       "<em>(<strong>Afsona had cut her hair at the hairdresser's.</strong> bu kontekstda "
                       "xato — bunday tartib past perfect boʻlib, u sochini oʻzi kesgan degan maʼno "
                       "beradi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["We had the roof repaired last week.", "We had repaired the roof by a builder.",
                    "We had the roof repair last week.", "We were had the roof repaired last week."],
        "correct": "We had the roof repaired last week.",
        "explanation": "<p><strong>We had the roof repaired last week.</strong> is correct — "
                       "<em>have + object + V3</em>.<br><br>"
                       "<em>(<strong>We had the roof repaired last week.</strong> toʻgʻri — "
                       "<em>have + toʻldiruvchi + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Your handwriting looks different today, "
                "Jasur.</p>"
                "<p><strong>Jasur:</strong> ___</p>",
        "choices": ["I had my glasses changed last week.",
                    "I had changed my glasses last week by the optician.",
                    "I had my glasses change last week.",
                    "I have changed my glasses by the optician last week."],
        "correct": "I had my glasses changed last week.",
        "explanation": "<p><strong>I had my glasses changed last week.</strong> is correct — the optician "
                       "did it for him.<br><br>"
                       "<em>(<strong>I had my glasses changed last week.</strong> toʻgʻri — buni uning "
                       "uchun optik bajargan.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Behruz had his bike repaired, got his brother to pump the tyres, "
                    "and then had his photo taken with it.",
                    "Behruz had repaired his bike, got his brother pump the tyres, "
                    "and then had taken his photo with it.",
                    "Behruz had his bike repair, got his brother to pumping the tyres, "
                    "and then had his photo take with it.",
                    "Behruz got his bike repair, had his brother to pump the tyres, "
                    "and then had taken his photo with it."],
        "correct": "Behruz had his bike repaired, got his brother to pump the tyres, "
                   "and then had his photo taken with it.",
        "explanation": "<p><strong>had his bike repaired … got his brother to pump … had his photo "
                       "taken</strong> is correct — a service, a person persuaded with <em>to</em>, and "
                       "another service.<br><br>"
                       "<em>(<strong>had his bike repaired … got his brother to pump … had his photo "
                       "taken</strong> toʻgʻri — xizmat, <em>to</em> bilan koʻndirilgan shaxs va yana "
                       "bitta xizmat.)</em></p>",
    },
]


# =====================================================================
# PE-67 — Comparatives and Superlatives
# =====================================================================

Q_PE67 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz is ___ than his brother.</strong></p>",
        "choices": ["taller", "more tall", "tallest", "the taller"],
        "correct": "taller",
        "explanation": "<p><strong>taller</strong> is correct — one-syllable adjectives take "
                       "<em>-er</em>.<br><br>"
                       "<em>(<strong>taller</strong> toʻgʻri — bir boʻgʻinli sifatlar <em>-er</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>This exercise is ___ than the last one.</strong></p>",
        "choices": ["more difficult", "difficulter", "most difficult", "more difficulter"],
        "correct": "more difficult",
        "explanation": "<p><strong>more difficult</strong> is correct — adjectives of two or more "
                       "syllables take <em>more</em>.<br><br>"
                       "<em>(<strong>more difficult</strong> toʻgʻri — ikki va undan koʻp boʻgʻinli "
                       "sifatlar <em>more</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct spelling.</p>"
                "<p><strong>big → ___</strong></p>",
        "choices": ["bigger", "biger", "more big", "bigest"],
        "correct": "bigger",
        "explanation": "<p><strong>bigger</strong> is correct — one short vowel + one consonant doubles "
                       "the consonant.<br><br>"
                       "<em>(<strong>bigger</strong> toʻgʻri — bitta qisqa unli + bitta undosh undoshni "
                       "ikkilaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct spelling.</p>"
                "<p><strong>easy → ___</strong></p>",
        "choices": ["easier", "easyer", "more easy", "easiest than"],
        "correct": "easier",
        "explanation": "<p><strong>easier</strong> is correct — two syllables ending in <em>-y</em> take "
                       "<em>-ier</em>.<br><br>"
                       "<em>(<strong>easier</strong> toʻgʻri — <em>-y</em> bilan tugagan ikki boʻgʻinli "
                       "sifatlar <em>-ier</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda is ___ pupil in our class.</strong></p>",
        "choices": ["the cleverest", "cleverest", "the most clever than", "more clever"],
        "correct": "the cleverest",
        "explanation": "<p><strong>the cleverest</strong> is correct — a superlative always takes "
                       "<em>the</em>.<br><br>"
                       "<em>(<strong>the cleverest</strong> toʻgʻri — superlativ doim <em>the</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos is ___ girl in the school.</strong></p>",
        "choices": ["the most hard-working", "the hard-workingest",
                    "most hard-working", "more hard-working"],
        "correct": "the most hard-working",
        "explanation": "<p><strong>the most hard-working</strong> is correct — long adjectives take "
                       "<em>the most</em>.<br><br>"
                       "<em>(<strong>the most hard-working</strong> toʻgʻri — uzun sifatlar <em>the "
                       "most</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar's mark was ___ than mine.</strong></p>",
        "choices": ["better", "gooder", "more good", "the best"],
        "correct": "better",
        "explanation": "<p><strong>better</strong> is correct — <em>good → better → the best</em> is "
                       "irregular.<br><br>"
                       "<em>(<strong>better</strong> toʻgʻri — <em>good → better → the best</em> "
                       "notoʻgʻri shakl.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The weather today is ___ than yesterday.</strong></p>",
        "choices": ["worse", "badder", "more bad", "the worst"],
        "correct": "worse",
        "explanation": "<p><strong>worse</strong> is correct — <em>bad → worse → the worst</em>.<br><br>"
                       "<em>(<strong>worse</strong> toʻgʻri — <em>bad → worse → the worst</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek lives ___ from school than Firdavs.</strong></p>",
        "choices": ["further", "farer", "more far", "the furthest"],
        "correct": "further",
        "explanation": "<p><strong>further</strong> is correct — <em>far → further / farther → the "
                       "furthest</em>.<br><br>"
                       "<em>(<strong>further</strong> toʻgʻri — <em>far → further / farther → the "
                       "furthest</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir is ___ taller than his sister.</strong></p>",
        "choices": ["much", "very", "so", "too"],
        "correct": "much",
        "explanation": "<p><strong>much</strong> is correct — comparatives are strengthened with "
                       "<em>much, far, a lot</em>, never with <em>very</em>.<br><br>"
                       "<em>(<strong>much</strong> toʻgʻri — komparativ <em>much, far, a lot</em> bilan "
                       "kuchaytiriladi, <em>very</em> bilan emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina is ___ a bit younger than Shaxzoda.</strong></p>",
        "choices": ["quite", "very", "much more", "the most"],
        "correct": "quite",
        "explanation": "<p><strong>quite</strong> is correct — <em>quite a bit / a little / slightly</em> "
                       "soften a comparative.<br><br>"
                       "<em>(<strong>quite</strong> toʻgʻri — <em>quite a bit / a little / slightly</em> "
                       "komparativni yumshatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence contains the “more better” trap?</strong></p>",
        "choices": ["This book is more better than that one.",
                    "This book is better than that one.",
                    "This book is much better than that one.",
                    "This is the best book of all."],
        "correct": "This book is more better than that one.",
        "explanation": "<p><strong>This book is more better than that one.</strong> is the mistake — "
                       "never use <em>more</em> with an <em>-er</em> form.<br><br>"
                       "<em>(<strong>This book is more better than that one.</strong> xato — "
                       "<em>-er</em> shakli bilan <em>more</em> hech qachon ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh is the ___ boy in the team.</strong></p>",
        "choices": ["fastest", "most fast", "faster", "more fast"],
        "correct": "fastest",
        "explanation": "<p><strong>fastest</strong> is correct — one syllable, so <em>-est</em>.<br><br>"
                       "<em>(<strong>fastest</strong> toʻgʻri — bir boʻgʻin, shuning uchun "
                       "<em>-est</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin is the best pupil ___ the class.</strong></p>",
        "choices": ["in", "of", "from", "at"],
        "correct": "in",
        "explanation": "<p><strong>in</strong> is correct — <em>in</em> for a place or group; <em>of</em> "
                       "for a number or period: <em>the best of the three</em>.<br><br>"
                       "<em>(<strong>in</strong> toʻgʻri — joy yoki guruh uchun <em>in</em>; son yoki "
                       "davr uchun <em>of</em>: <em>the best of the three</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The ___ you practise, the ___ you become.</strong></p>",
        "choices": ["more … better", "most … best", "more … more good", "much … better"],
        "correct": "more … better",
        "explanation": "<p><strong>more … better</strong> is correct — the double comparative pattern "
                       "<em>the … the …</em> shows two things changing together.<br><br>"
                       "<em>(<strong>more … better</strong> toʻgʻri — <em>the … the …</em> qolipi ikki "
                       "narsaning birga oʻzgarishini koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona sings ___ than her sister.</strong></p>",
        "choices": ["better", "more good", "gooder", "more well"],
        "correct": "better",
        "explanation": "<p><strong>better</strong> is correct — this compares <em>how</em> she sings, and "
                       "the comparative of <em>well</em> is also <em>better</em>.<br><br>"
                       "<em>(<strong>better</strong> toʻgʻri — bu <em>qanday</em> kuylashini "
                       "solishtiradi, <em>well</em> ning komparativi ham <em>better</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Davron is more taller than me.", "Davron is much taller than me.",
                    "Davron is taller than me.", "Davron is the tallest in our class."],
        "correct": "Davron is more taller than me.",
        "explanation": "<p><strong>Davron is more taller than me.</strong> is the mistake — one "
                       "comparative marker is enough.<br><br>"
                       "<em>(<strong>Davron is more taller than me.</strong> xato — bitta komparativ "
                       "belgisi yetarli.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Afsona is the most careful pupil in the class.",
                    "Afsona is most careful pupil in the class.",
                    "Afsona is the carefulest pupil in the class.",
                    "Afsona is more careful pupil in the class."],
        "correct": "Afsona is the most careful pupil in the class.",
        "explanation": "<p><strong>Afsona is the most careful pupil in the class.</strong> is correct — "
                       "<em>the most</em> for a long adjective, with <em>the</em> kept.<br><br>"
                       "<em>(<strong>Afsona is the most careful pupil in the class.</strong> toʻgʻri — "
                       "uzun sifat uchun <em>the most</em>, <em>the</em> esa saqlanadi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> How was the second test compared with the "
                "first?</p>"
                "<p><strong>Jasur:</strong> ___</p>",
        "choices": ["It was much easier than the first one.",
                    "It was much more easier than the first one.",
                    "It was very easier than the first one.",
                    "It was the easiest than the first one."],
        "correct": "It was much easier than the first one.",
        "explanation": "<p><strong>It was much easier than the first one.</strong> is correct — "
                       "<em>much</em> strengthens a comparative, <em>very</em> never does.<br><br>"
                       "<em>(<strong>It was much easier than the first one.</strong> toʻgʻri — "
                       "komparativni <em>much</em> kuchaytiradi, <em>very</em> esa hech qachon.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Behruz is taller than Elbek, but Firdavs is the tallest and much stronger too.",
                    "Behruz is more taller than Elbek, but Firdavs is most tallest and very stronger too.",
                    "Behruz is tallest than Elbek, but Firdavs is the most tall and much more strong too.",
                    "Behruz is more tall than Elbek, but Firdavs is the tallest and very much stronger too."],
        "correct": "Behruz is taller than Elbek, but Firdavs is the tallest and much stronger too.",
        "explanation": "<p><strong>taller … the tallest … much stronger</strong> is correct — a "
                       "comparative, a superlative with <em>the</em>, and <em>much</em> as the "
                       "intensifier.<br><br>"
                       "<em>(<strong>taller … the tallest … much stronger</strong> toʻgʻri — komparativ, "
                       "<em>the</em> bilan superlativ va kuchaytiruvchi sifatida <em>much</em>.)</em></p>",
    },
]


# =====================================================================
# PE-68 — as ... as, too, enough
# =====================================================================

Q_PE68 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Jasur is as ___ as his brother.</strong></p>",
        "choices": ["tall", "taller", "tallest", "more tall"],
        "correct": "tall",
        "explanation": "<p><strong>tall</strong> is correct — the adjective between <em>as … as</em> "
                       "never changes.<br><br>"
                       "<em>(<strong>tall</strong> toʻgʻri — <em>as … as</em> orasidagi sifat hech qachon "
                       "oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Today isn't ___ cold as yesterday.</strong></p>",
        "choices": ["as", "so much", "more", "than"],
        "correct": "as",
        "explanation": "<p><strong>as</strong> is correct — <em>not as … as</em> means less. So today is "
                       "warmer.<br><br>"
                       "<em>(<strong>as</strong> toʻgʻri — <em>not as … as</em> kamroq degani. Yaʼni "
                       "bugun issiqroq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>This tea is ___ hot to drink.</strong></p>",
        "choices": ["too", "enough", "very much", "as"],
        "correct": "too",
        "explanation": "<p><strong>too</strong> is correct — <em>too</em> means more than you want, and "
                       "it always carries a problem with it.<br><br>"
                       "<em>(<strong>too</strong> toʻgʻri — <em>too</em> “kerakdan ortiq” degani va doim "
                       "muammoni bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda isn't old ___ to drive.</strong></p>",
        "choices": ["enough", "too", "as", "so"],
        "correct": "enough",
        "explanation": "<p><strong>enough</strong> is correct — after an adjective, <em>enough</em> comes "
                       "<em>after</em> it: <em>old enough</em>.<br><br>"
                       "<em>(<strong>enough</strong> toʻgʻri — sifatdan keyin <em>enough</em> uning "
                       "<em>orqasidan</em> keladi: <em>old enough</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Where does <em>enough</em> go with a noun?</strong></p>",
        "choices": ["before the noun — enough time", "after the noun — time enough",
                    "at the end of the sentence", "before the verb"],
        "correct": "before the noun — enough time",
        "explanation": "<p><strong>before the noun — enough time</strong> is correct — that is the "
                       "position trap: after adjectives, before nouns.<br><br>"
                       "<em>(<strong>otdan oldin — enough time</strong> toʻgʻri — oʻrin tuzogʻi shu: "
                       "sifatdan keyin, otdan oldin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos doesn't have ___ to finish the project.</strong></p>",
        "choices": ["enough time", "time enough", "too time", "as time"],
        "correct": "enough time",
        "explanation": "<p><strong>enough time</strong> is correct — a noun follows, so <em>enough</em> "
                       "goes first.<br><br>"
                       "<em>(<strong>enough time</strong> toʻgʻri — keyin ot keladi, shuning uchun "
                       "<em>enough</em> oldin turadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The box was ___ heavy for Samandar to lift.</strong></p>",
        "choices": ["too", "enough", "as", "so much"],
        "correct": "too",
        "explanation": "<p><strong>too</strong> is correct — the pattern <em>too + adjective + to + "
                       "verb</em>.<br><br>"
                       "<em>(<strong>too</strong> toʻgʻri — <em>too + sifat + to + feʼl</em> "
                       "qolipi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek is strong ___ to carry both bags.</strong></p>",
        "choices": ["enough", "too", "as", "so"],
        "correct": "enough",
        "explanation": "<p><strong>enough</strong> is correct — the pattern <em>adjective + enough + to "
                       "+ verb</em>.<br><br>"
                       "<em>(<strong>enough</strong> toʻgʻri — <em>sifat + enough + to + feʼl</em> "
                       "qolipi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference between <em>too</em> and <em>very</em>?</strong></p>",
        "choices": ["too = a problem · very = just a strong degree",
                    "too = a strong degree · very = a problem",
                    "They mean exactly the same.",
                    "too is formal, very is informal."],
        "correct": "too = a problem · very = just a strong degree",
        "explanation": "<p><strong>too = a problem · very = just a strong degree</strong> is correct — "
                       "<em>The tea is very hot</em> (nice!) vs <em>too hot</em> (I can't drink "
                       "it).<br><br>"
                       "<em>(<strong>too = muammo · very = shunchaki kuchli daraja</strong> toʻgʻri — "
                       "<em>The tea is very hot</em> (yaxshi!) va <em>too hot</em> (icha "
                       "olmayman).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs runs as ___ as Javohir.</strong></p>",
        "choices": ["fast", "faster", "fastest", "more fast"],
        "correct": "fast",
        "explanation": "<p><strong>fast</strong> is correct — the base form sits between <em>as … "
                       "as</em>, whether it describes a thing or an action.<br><br>"
                       "<em>(<strong>fast</strong> toʻgʻri — <em>as … as</em> orasida asosiy shakl "
                       "turadi, narsani ham, harakatni ham taʼriflaganda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina has ___ money to buy the book.</strong></p>",
        "choices": ["enough", "too", "as", "very"],
        "correct": "enough",
        "explanation": "<p><strong>enough</strong> is correct — before an uncountable noun, meaning “as "
                       "much as she needs”.<br><br>"
                       "<em>(<strong>enough</strong> toʻgʻri — sanalmaydigan otdan oldin, “kerakli "
                       "miqdorda” maʼnosida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Shaxzoda was ___ tired to finish her homework.</strong></p>",
        "choices": ["too", "enough", "very", "as"],
        "correct": "too",
        "explanation": "<p><strong>too</strong> is correct — the tiredness stopped her, which is exactly "
                       "what <em>too</em> signals.<br><br>"
                       "<em>(<strong>too</strong> toʻgʻri — charchoq unga toʻsqinlik qildi, <em>too</em> "
                       "aynan shuni bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence means Abdulloh <em>can</em> reach the shelf?</strong></p>",
        "choices": ["Abdulloh is tall enough to reach the shelf.",
                    "Abdulloh is too short to reach the shelf.",
                    "Abdulloh isn't tall enough to reach the shelf.",
                    "Abdulloh is too tall to reach the shelf."],
        "correct": "Abdulloh is tall enough to reach the shelf.",
        "explanation": "<p><strong>Abdulloh is tall enough to reach the shelf.</strong> is correct — "
                       "<em>enough</em> says the amount is sufficient.<br><br>"
                       "<em>(<strong>Abdulloh is tall enough to reach the shelf.</strong> toʻgʻri — "
                       "<em>enough</em> miqdor yetarli ekanini aytadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>This film isn't as interesting ___ the book.</strong></p>",
        "choices": ["as", "than", "that", "so"],
        "correct": "as",
        "explanation": "<p><strong>as</strong> is correct — the pair is always <em>as … as</em>, never "
                       "<em>as … than</em>.<br><br>"
                       "<em>(<strong>as</strong> toʻgʻri — juftlik doim <em>as … as</em>, <em>as … "
                       "than</em> emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Sirojiddin's answer was ___ good as Marjona's.</strong></p>",
        "choices": ["as", "so", "too", "enough"],
        "correct": "as",
        "explanation": "<p><strong>as</strong> is correct — equality in a positive sentence takes "
                       "<em>as … as</em>.<br><br>"
                       "<em>(<strong>as</strong> toʻgʻri — tasdiq gapdagi tenglik <em>as … as</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>The soup was ___ salty to eat, and there wasn't ___ bread "
                "either.</strong></p>",
        "choices": ["too … enough", "enough … too", "very … enough", "too … too"],
        "correct": "too … enough",
        "explanation": "<p><strong>too … enough</strong> is correct — <em>too</em> before an adjective, "
                       "<em>enough</em> before a noun.<br><br>"
                       "<em>(<strong>too … enough</strong> toʻgʻri — sifat oldidan <em>too</em>, ot "
                       "oldidan esa <em>enough</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Davron is enough old to vote.", "Davron is old enough to vote.",
                    "Davron isn't old enough to vote.", "Davron is too young to vote."],
        "correct": "Davron is enough old to vote.",
        "explanation": "<p><strong>Davron is enough old to vote.</strong> is the mistake — after an "
                       "adjective, <em>enough</em> must follow it.<br><br>"
                       "<em>(<strong>Davron is enough old to vote.</strong> xato — sifatdan keyin "
                       "<em>enough</em> uning orqasidan kelishi kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Afsona is as clever as her sister.", "Afsona is as clever than her sister.",
                    "Afsona is so clever as her sister is.", "Afsona is as cleverer as her sister."],
        "correct": "Afsona is as clever as her sister.",
        "explanation": "<p><strong>Afsona is as clever as her sister.</strong> is correct — "
                       "<em>as + base adjective + as</em>.<br><br>"
                       "<em>(<strong>Afsona is as clever as her sister.</strong> toʻgʻri — "
                       "<em>as + asosiy sifat + as</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Why didn't you finish the test, Behruz?</p>"
                "<p><strong>Behruz:</strong> ___</p>",
        "choices": ["There wasn't enough time.", "There wasn't time enough.",
                    "There was too time.", "There wasn't as time."],
        "correct": "There wasn't enough time.",
        "explanation": "<p><strong>There wasn't enough time.</strong> is correct — <em>enough</em> before "
                       "the noun <em>time</em>.<br><br>"
                       "<em>(<strong>There wasn't enough time.</strong> toʻgʻri — <em>enough</em> "
                       "<em>time</em> otidan oldin.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["The bag was too heavy for Iroda, so Elbek — who is strong enough — "
                    "carried it as easily as an empty box.",
                    "The bag was very heavy for Iroda, so Elbek — who is enough strong — "
                    "carried it as easy than an empty box.",
                    "The bag was too much heavy for Iroda, so Elbek — who is strong enough — "
                    "carried it so easily as an empty box.",
                    "The bag was enough heavy for Iroda, so Elbek — who is too strong — "
                    "carried it as easier as an empty box."],
        "correct": "The bag was too heavy for Iroda, so Elbek — who is strong enough — "
                   "carried it as easily as an empty box.",
        "explanation": "<p><strong>too heavy … strong enough … as easily as</strong> is correct — a "
                       "problem, a sufficiency, and an equality, each in its own pattern.<br><br>"
                       "<em>(<strong>too heavy … strong enough … as easily as</strong> toʻgʻri — muammo, "
                       "yetarlilik va tenglik, har biri oʻz qolipida.)</em></p>",
    },
]


# =====================================================================
# PE-69 — Quantifiers
# =====================================================================

Q_PE69 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There's ___ milk in the fridge.</strong></p>",
        "choices": ["some", "any", "many", "a few"],
        "correct": "some",
        "explanation": "<p><strong>some</strong> is correct — <em>some</em> belongs to positive "
                       "sentences.<br><br>"
                       "<em>(<strong>some</strong> toʻgʻri — <em>some</em> tasdiq gaplarga "
                       "tegishli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There isn't ___ bread left.</strong></p>",
        "choices": ["any", "some", "many", "a few"],
        "correct": "any",
        "explanation": "<p><strong>any</strong> is correct — <em>any</em> belongs to negatives and "
                       "questions.<br><br>"
                       "<em>(<strong>any</strong> toʻgʻri — <em>any</em> inkor va savollarga "
                       "tegishli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Did Behruz buy ___ apples at the bazaar?</strong></p>",
        "choices": ["any", "some", "much", "a little"],
        "correct": "any",
        "explanation": "<p><strong>any</strong> is correct — an ordinary question takes <em>any</em>."
                       "<br><br><em>(<strong>any</strong> toʻgʻri — oddiy savol <em>any</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Would you like ___ tea, Iroda?</strong></p>",
        "choices": ["some", "any", "many", "few"],
        "correct": "some",
        "explanation": "<p><strong>some</strong> is correct — this is the exception: offers and requests "
                       "take <em>some</em> even though they are questions.<br><br>"
                       "<em>(<strong>some</strong> toʻgʻri — bu istisno: taklif va iltimoslar savol "
                       "boʻlsa ham <em>some</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Could I have ___ water, please?</strong></p>",
        "choices": ["some", "any", "many", "a few"],
        "correct": "some",
        "explanation": "<p><strong>some</strong> is correct — a request, so the same exception "
                       "applies.<br><br>"
                       "<em>(<strong>some</strong> toʻgʻri — bu iltimos, shuning uchun oʻsha istisno "
                       "amal qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How ___ pupils are there in Rozimurod teacher's class?</strong></p>",
        "choices": ["many", "much", "a little", "any"],
        "correct": "many",
        "explanation": "<p><strong>many</strong> is correct — countable plural.<br><br>"
                       "<em>(<strong>many</strong> toʻgʻri — sanaladigan otning koʻpligi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How ___ sugar do you take in your tea?</strong></p>",
        "choices": ["much", "many", "a few", "some"],
        "correct": "much",
        "explanation": "<p><strong>much</strong> is correct — uncountable.<br><br>"
                       "<em>(<strong>much</strong> toʻgʻri — sanalmaydigan ot.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos has ___ friends in her new school.</strong></p>",
        "choices": ["a lot of", "much", "a little", "any"],
        "correct": "a lot of",
        "explanation": "<p><strong>a lot of</strong> is correct — it works with both countable and "
                       "uncountable nouns, which makes it the safe option.<br><br>"
                       "<em>(<strong>a lot of</strong> toʻgʻri — u sanaladigan va sanalmaydigan otlar "
                       "bilan ham ishlaydi, shuning uchun eng xavfsiz variant.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Where do <em>much</em> and <em>many</em> really belong?</strong></p>",
        "choices": ["mostly in negatives and questions",
                    "mostly in positive sentences",
                    "only in questions",
                    "only with uncountable nouns"],
        "correct": "mostly in negatives and questions",
        "explanation": "<p><strong>mostly in negatives and questions</strong> is correct — in positive "
                       "sentences English prefers <em>a lot of</em>: <em>I have a lot of "
                       "homework</em>.<br><br>"
                       "<em>(<strong>asosan inkor va savollarda</strong> toʻgʻri — tasdiq gaplarda "
                       "ingliz tili <em>a lot of</em> ni afzal koʻradi: <em>I have a lot of "
                       "homework</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar doesn't have ___ free time this week.</strong></p>",
        "choices": ["much", "many", "a lot", "a few"],
        "correct": "much",
        "explanation": "<p><strong>much</strong> is correct — a negative sentence with an uncountable "
                       "noun: its natural home.<br><br>"
                       "<em>(<strong>much</strong> toʻgʻri — sanalmaydigan ot bilan inkor gap: uning "
                       "tabiiy oʻrni.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek has ___ of books about space.</strong></p>",
        "choices": ["lots", "much", "many of", "a little"],
        "correct": "lots",
        "explanation": "<p><strong>lots</strong> is correct — <em>lots of</em> and <em>plenty of</em> are "
                       "the friendly informal options.<br><br>"
                       "<em>(<strong>lots</strong> toʻgʻri — <em>lots of</em> va <em>plenty of</em> — "
                       "qulay, norasmiy variantlar.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There is ___ time — don't hurry.</strong></p>",
        "choices": ["plenty of", "many", "a few", "any"],
        "correct": "plenty of",
        "explanation": "<p><strong>plenty of</strong> is correct — more than enough, and it works with "
                       "uncountables.<br><br>"
                       "<em>(<strong>plenty of</strong> toʻgʻri — yetarlidan ham koʻp va sanalmaydigan "
                       "otlar bilan ishlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs has ___ money — he can't buy the ticket.</strong></p>",
        "choices": ["no", "any", "not any of", "much"],
        "correct": "no",
        "explanation": "<p><strong>no</strong> is correct — <em>no + noun</em> equals <em>not any</em>, "
                       "but is stronger and needs a positive verb.<br><br>"
                       "<em>(<strong>no</strong> toʻgʻri — <em>no + ot</em> <em>not any</em> ga teng, "
                       "lekin kuchliroq va tasdiq feʼl talab qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which is correct?</strong></p>",
        "choices": ["Javohir has no brothers.", "Javohir hasn't no brothers.",
                    "Javohir doesn't have no brothers.", "Javohir has not any brother."],
        "correct": "Javohir has no brothers.",
        "explanation": "<p><strong>Javohir has no brothers.</strong> is correct — <em>no</em> already "
                       "carries the negative, so the verb stays positive.<br><br>"
                       "<em>(<strong>Javohir has no brothers.</strong> toʻgʻri — <em>no</em> inkorni "
                       "oʻzi tashiydi, shuning uchun feʼl tasdiqda qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina bought ___ new pens yesterday.</strong></p>",
        "choices": ["some", "any", "much", "a little"],
        "correct": "some",
        "explanation": "<p><strong>some</strong> is correct — a positive statement with a countable "
                       "plural.<br><br>"
                       "<em>(<strong>some</strong> toʻgʻri — sanaladigan koʻplik bilan tasdiq "
                       "gap.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>There isn't ___ juice, but there are ___ apples.</strong></p>",
        "choices": ["any … some", "some … any", "much … much", "any … any"],
        "correct": "any … some",
        "explanation": "<p><strong>any … some</strong> is correct — negative half takes <em>any</em>, "
                       "positive half takes <em>some</em>.<br><br>"
                       "<em>(<strong>any … some</strong> toʻgʻri — inkor qismi <em>any</em>, tasdiq qismi "
                       "esa <em>some</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Shaxzoda has much friends at school.",
                    "Shaxzoda has a lot of friends at school.",
                    "Shaxzoda doesn't have many friends at school.",
                    "Shaxzoda has lots of friends at school."],
        "correct": "Shaxzoda has much friends at school.",
        "explanation": "<p><strong>Shaxzoda has much friends at school.</strong> is the mistake — "
                       "<em>friends</em> is countable, and <em>much</em> avoids positive sentences "
                       "anyway.<br><br>"
                       "<em>(<strong>Shaxzoda has much friends at school.</strong> xato — "
                       "<em>friends</em> sanaladi, <em>much</em> esa tasdiq gaplarda "
                       "ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Would you like some help with your bag?",
                    "Would you like any help with your bag?",
                    "Would you like much help with your bag?",
                    "Would you like a few help with your bag?"],
        "correct": "Would you like some help with your bag?",
        "explanation": "<p><strong>Would you like some help with your bag?</strong> is correct — an offer "
                       "breaks the question rule and takes <em>some</em>.<br><br>"
                       "<em>(<strong>Would you like some help with your bag?</strong> toʻgʻri — taklif "
                       "savol qoidasini buzadi va <em>some</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Abdulloh:</strong> Have we got everything for the picnic?</p>"
                "<p><strong>Sirojiddin:</strong> ___</p>",
        "choices": ["We have plenty of bread, but we haven't got any water.",
                    "We have plenty of bread, but we haven't got some water.",
                    "We have much bread, but we haven't got no water.",
                    "We have many bread, but we haven't got any waters."],
        "correct": "We have plenty of bread, but we haven't got any water.",
        "explanation": "<p><strong>plenty of bread … haven't got any water</strong> is correct — a "
                       "positive with <em>plenty of</em>, a negative with <em>any</em>.<br><br>"
                       "<em>(<strong>plenty of bread … haven't got any water</strong> toʻgʻri — tasdiqda "
                       "<em>plenty of</em>, inkorda esa <em>any</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> quantifier is correct.</p>",
        "choices": ["There are a lot of pupils, but there isn't much space, "
                    "so we don't have many chairs.",
                    "There are much pupils, but there isn't many space, "
                    "so we don't have much chairs.",
                    "There are a lot of pupils, but there isn't many space, "
                    "so we don't have any of chairs.",
                    "There are many of pupils, but there isn't much of space, "
                    "so we haven't no chairs."],
        "correct": "There are a lot of pupils, but there isn't much space, "
                   "so we don't have many chairs.",
        "explanation": "<p><strong>a lot of … much … many</strong> is correct — the safe option in the "
                       "positive, <em>much</em> with an uncountable negative, <em>many</em> with a "
                       "countable one.<br><br>"
                       "<em>(<strong>a lot of … much … many</strong> toʻgʻri — tasdiqda xavfsiz variant, "
                       "sanalmaydigan inkorda <em>much</em>, sanaladiganida esa <em>many</em>.)</em></p>",
    },
]


# =====================================================================
# PE-70 — few vs a few, little vs a little
# =====================================================================

Q_PE70 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda has ___ friends here — she's very happy at her new "
                "school.</strong></p>",
        "choices": ["a few", "few", "a little", "little"],
        "correct": "a few",
        "explanation": "<p><strong>a few</strong> is correct — <em>a few</em> is positive: “some, and "
                       "that's enough”.<br><br>"
                       "<em>(<strong>a few</strong> toʻgʻri — <em>a few</em> ijobiy: “bir nechta, va bu "
                       "yetarli”.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz has ___ friends here — he feels lonely.</strong></p>",
        "choices": ["few", "a few", "little", "a little"],
        "correct": "few",
        "explanation": "<p><strong>few</strong> is correct — without <em>a</em> the meaning turns "
                       "negative: “almost none, unfortunately”.<br><br>"
                       "<em>(<strong>few</strong> toʻgʻri — <em>a</em> siz maʼno salbiy boʻladi: "
                       "“deyarli yoʻq, afsuski”.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which pair goes with <em>countable</em> nouns?</strong></p>",
        "choices": ["few / a few", "little / a little", "much / a much", "less / a less"],
        "correct": "few / a few",
        "explanation": "<p><strong>few / a few</strong> is correct — countable; <em>little / a "
                       "little</em> is uncountable.<br><br>"
                       "<em>(<strong>few / a few</strong> toʻgʻri — sanaladigan otlar bilan; "
                       "<em>little / a little</em> esa sanalmaydiganlar bilan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There's ___ milk left — enough for tea.</strong></p>",
        "choices": ["a little", "little", "a few", "few"],
        "correct": "a little",
        "explanation": "<p><strong>a little</strong> is correct — uncountable and positive.<br><br>"
                       "<em>(<strong>a little</strong> toʻgʻri — sanalmaydigan va ijobiy.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>There's ___ milk left — we'll have to buy some.</strong></p>",
        "choices": ["little", "a little", "few", "a few"],
        "correct": "little",
        "explanation": "<p><strong>little</strong> is correct — uncountable and negative: hardly any."
                       "<br><br><em>(<strong>little</strong> toʻgʻri — sanalmaydigan va salbiy: deyarli "
                       "yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos has ___ time before the lesson — she can help you.</strong></p>",
        "choices": ["a little", "little", "a few", "few"],
        "correct": "a little",
        "explanation": "<p><strong>a little</strong> is correct — the second half shows the mood is "
                       "positive.<br><br>"
                       "<em>(<strong>a little</strong> toʻgʻri — gapning ikkinchi qismi kayfiyat ijobiy "
                       "ekanini koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar had ___ time, so he didn't finish the last question.</strong></p>",
        "choices": ["little", "a little", "few", "a few"],
        "correct": "little",
        "explanation": "<p><strong>little</strong> is correct — the consequence tells you the meaning is "
                       "negative.<br><br>"
                       "<em>(<strong>little</strong> toʻgʻri — oqibat maʼno salbiy ekanini "
                       "koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Only ___ pupils came to the extra lesson — Rozimurod teacher was "
                "disappointed.</strong></p>",
        "choices": ["a few", "few", "a little", "little"],
        "correct": "a few",
        "explanation": "<p><strong>a few</strong> is correct — after <em>only</em>, <em>a few</em> "
                       "already sounds negative, which is why the teacher was disappointed.<br><br>"
                       "<em>(<strong>a few</strong> toʻgʻri — <em>only</em> dan keyin <em>a few</em> "
                       "allaqachon salbiy eshitiladi, shuning uchun oʻqituvchi xafa boʻlgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek made ___ mistakes — well done!</strong></p>",
        "choices": ["few", "a few", "little", "a little"],
        "correct": "few",
        "explanation": "<p><strong>few</strong> is correct — “hardly any mistakes”, which with mistakes "
                       "is good news.<br><br>"
                       "<em>(<strong>few</strong> toʻgʻri — “deyarli xato yoʻq”, xatolar haqida gap "
                       "ketganda bu yaxshi xabar.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs speaks ___ Korean — enough to order food.</strong></p>",
        "choices": ["a little", "little", "a few", "few"],
        "correct": "a little",
        "explanation": "<p><strong>a little</strong> is correct — a language is uncountable, and the mood "
                       "is positive.<br><br>"
                       "<em>(<strong>a little</strong> toʻgʻri — til sanalmaydi va kayfiyat "
                       "ijobiy.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ people know this story — it isn't in the textbook.</strong></p>",
        "choices": ["Few", "A few", "Little", "A little"],
        "correct": "Few",
        "explanation": "<p><strong>Few</strong> is correct — countable and negative: almost nobody."
                       "<br><br><em>(<strong>Few</strong> toʻgʻri — sanaladigan va salbiy: deyarli hech "
                       "kim.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir has ___ interest in football, so don't invite him.</strong></p>",
        "choices": ["little", "a little", "few", "a few"],
        "correct": "little",
        "explanation": "<p><strong>little</strong> is correct — <em>interest</em> is uncountable here, and "
                       "the meaning is negative.<br><br>"
                       "<em>(<strong>little</strong> toʻgʻri — bu yerda <em>interest</em> sanalmaydi va "
                       "maʼno salbiy.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does <em>quite a few</em> mean?</strong></p>",
        "choices": ["quite a lot", "almost none", "exactly four", "not enough"],
        "correct": "quite a lot",
        "explanation": "<p><strong>quite a lot</strong> is correct — the surprise of this lesson: "
                       "<em>quite a few</em> means many, not few.<br><br>"
                       "<em>(<strong>ancha koʻp</strong> toʻgʻri — bu darsning ajablanarli tomoni: "
                       "<em>quite a few</em> “koʻp” degani, “kam” emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Quite a few pupils ___ the olympiad this year.</strong></p>",
        "choices": ["entered", "enters", "was entering", "enter it"],
        "correct": "entered",
        "explanation": "<p><strong>entered</strong> is correct — <em>quite a few pupils</em> is a plural "
                       "subject, and quite a lot of them took part.<br><br>"
                       "<em>(<strong>entered</strong> toʻgʻri — <em>quite a few pupils</em> koʻplikdagi "
                       "subject va ularning ancha qismi qatnashgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina needs ___ more minutes to finish.</strong></p>",
        "choices": ["a few", "a little", "few", "little"],
        "correct": "a few",
        "explanation": "<p><strong>a few</strong> is correct — <em>minutes</em> is countable, and the "
                       "meaning is positive.<br><br>"
                       "<em>(<strong>a few</strong> toʻgʻri — <em>minutes</em> sanaladi va maʼno "
                       "ijobiy.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>Shaxzoda has ___ books but ___ time to read them.</strong></p>",
        "choices": ["a few … little", "a little … few", "few … a little", "little … a few"],
        "correct": "a few … little",
        "explanation": "<p><strong>a few … little</strong> is correct — countable and positive, then "
                       "uncountable and negative.<br><br>"
                       "<em>(<strong>a few … little</strong> toʻgʻri — sanaladigan va ijobiy, keyin "
                       "sanalmaydigan va salbiy.)</em></p>",
    },
    {
        "text": "<p>Which sentence sounds <em>lonely</em>?</p>",
        "choices": ["Abdulloh has few friends in this city.",
                    "Abdulloh has a few friends in this city.",
                    "Abdulloh has quite a few friends in this city.",
                    "Abdulloh has a lot of friends in this city."],
        "correct": "Abdulloh has few friends in this city.",
        "explanation": "<p><strong>Abdulloh has few friends in this city.</strong> is correct — dropping "
                       "<em>a</em> flips the whole mood of the sentence.<br><br>"
                       "<em>(<strong>Abdulloh has few friends in this city.</strong> toʻgʻri — "
                       "<em>a</em> ni tushirib qoldirish gapning butun kayfiyatini oʻzgartiradi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Sirojiddin has a few money.", "Sirojiddin has a little money.",
                    "Sirojiddin has a few coins.", "Sirojiddin has little money."],
        "correct": "Sirojiddin has a few money.",
        "explanation": "<p><strong>Sirojiddin has a few money.</strong> is the mistake — <em>money</em> "
                       "is uncountable, so it needs <em>a little</em>.<br><br>"
                       "<em>(<strong>Sirojiddin has a few money.</strong> xato — <em>money</em> "
                       "sanalmaydi, shuning uchun <em>a little</em> kerak.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Do you need help with the exercise, "
                "Marjona?</p>"
                "<p><strong>Marjona:</strong> ___</p>",
        "choices": ["Just a little, thank you — I've nearly finished.",
                    "Just little, thank you — I've nearly finished.",
                    "Just a few, thank you — I've nearly finished.",
                    "Just few, thank you — I've nearly finished."],
        "correct": "Just a little, thank you — I've nearly finished.",
        "explanation": "<p><strong>Just a little, thank you.</strong> is correct — <em>help</em> is "
                       "uncountable, and the tone is positive.<br><br>"
                       "<em>(<strong>Just a little, thank you.</strong> toʻgʻri — <em>help</em> "
                       "sanalmaydi va ohang ijobiy.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> word is correct.</p>",
        "choices": ["Davron made few mistakes and had a little time left, "
                    "so quite a few pupils asked him for help.",
                    "Davron made a few mistakes and had few time left, "
                    "so quite a little pupils asked him for help.",
                    "Davron made little mistakes and had a few time left, "
                    "so quite few pupils asked him for help.",
                    "Davron made a little mistakes and had little times left, "
                    "so a quite few pupils asked him for help."],
        "correct": "Davron made few mistakes and had a little time left, "
                   "so quite a few pupils asked him for help.",
        "explanation": "<p><strong>few mistakes … a little time … quite a few pupils</strong> is "
                       "correct — hardly any mistakes (good), some time left (good), and quite a lot of "
                       "pupils.<br><br>"
                       "<em>(<strong>few mistakes … a little time … quite a few pupils</strong> "
                       "toʻgʻri — deyarli xatosiz (yaxshi), biroz vaqt qolgan (yaxshi) va ancha koʻp "
                       "oʻquvchi.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-66 Practice: The Causative: have / get something done",
        "tutorial":    "PE-66:",
        "level":       "medium",
        "description": "PE-66 darsiga 20 savol: have / get + toʻldiruvchi + V3, soʻz tartibining "
                       "ahamiyati, boshga tushgan yoqimsiz voqea maʼnosi hamda have somebody do va "
                       "get somebody to do. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE66,
    },
    {
        "title":       "PE-67 Practice: Comparatives and Superlatives",
        "tutorial":    "PE-67:",
        "description": "PE-67 darsiga 20 savol: -er/-est va more/most chegarasi, imlo qoidalari, "
                       "good/bad/far notoʻgʻri shakllari, much bilan kuchaytirish va “more better” "
                       "tuzogʻi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE67,
    },
    {
        "title":       "PE-68 Practice: as ... as, too, enough",
        "tutorial":    "PE-68:",
        "description": "PE-68 darsiga 20 savol: as … as va not as … as, too (kerakdan ortiq) va "
                       "enough (yetarli), enough ning oʻrni hamda too … to / enough … to qoliplari. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE68,
    },
    {
        "title":       "PE-69 Practice: Quantifiers: some, any, much, many, a lot of",
        "tutorial":    "PE-69:",
        "description": "PE-69 darsiga 20 savol: some va any (hamda taklifdagi istisno), much/many "
                       "ning haqiqiy oʻrni, a lot of / lots of / plenty of va no bilan not any farqi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE69,
    },
    {
        "title":       "PE-70 Practice: few vs a few, little vs a little",
        "tutorial":    "PE-70:",
        "description": "PE-70 darsiga 20 savol: a few / a little (ijobiy) va few / little (salbiy), "
                       "sanaladigan va sanalmaydigan otlar bilan mosligi hamda quite a few "
                       "kutilmaganligi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE70,
    },
]
