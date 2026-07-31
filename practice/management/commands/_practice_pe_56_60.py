# -*- coding: utf-8 -*-
"""Prime English practices — PE-56 … PE-60.

Mixed conditionals, wish, relative clauses and the passive.
Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_56_60.py --master=prime --expect-questions=20
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
# PE-56 — Mixed Conditionals
# =====================================================================

Q_PE56 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If I had studied medicine, I ___ a doctor now.</strong></p>",
        "choices": ["would be", "would have been", "will be", "am"],
        "correct": "would be",
        "explanation": "<p><strong>would be</strong> is correct — a past cause with a present result: the "
                       "third-conditional <em>if</em>-half joined to the second-conditional "
                       "result.<br><br>"
                       "<em>(<strong>would be</strong> toʻgʻri — oʻtmishdagi sabab, hozirgi natija: "
                       "uchinchi shart gapning <em>if</em> qismi ikkinchi shart gapning natijasi bilan "
                       "birlashgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is “Mix 1”?</strong></p>",
        "choices": ["Past cause → present result", "Present cause → past result",
                    "Future cause → past result", "Past cause → past result"],
        "correct": "Past cause → present result",
        "explanation": "<p><strong>Past cause → present result</strong> is correct — "
                       "<em>If + had + V3, would + base verb</em>. It is the commoner of the two "
                       "mixes.<br><br>"
                       "<em>(<strong>Oʻtmishdagi sabab → hozirgi natija</strong> toʻgʻri — "
                       "<em>If + had + V3, would + asosiy feʼl</em>. Bu — ikki aralash turdan koʻproq "
                       "uchraydigani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Behruz hadn't broken his leg, he ___ in the match today.</strong></p>",
        "choices": ["would be playing", "would have played", "will play", "played"],
        "correct": "would be playing",
        "explanation": "<p><strong>would be playing</strong> is correct — the accident is past, the match "
                       "is today.<br><br>"
                       "<em>(<strong>would be playing</strong> toʻgʻri — jarohat oʻtmishda, oʻyin esa "
                       "bugun.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Iroda ___ more careful, she wouldn't have lost her keys "
                "yesterday.</strong></p>",
        "choices": ["were", "had been", "is", "would be"],
        "correct": "were",
        "explanation": "<p><strong>were</strong> is correct — Mix 2: a permanent present quality causing "
                       "a past result.<br><br>"
                       "<em>(<strong>were</strong> toʻgʻri — 2-aralash tur: doimiy hozirgi xususiyat "
                       "oʻtmishdagi natijaga sabab boʻlgan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Charos spoke Korean, she ___ that letter last week.</strong></p>",
        "choices": ["would have understood", "would understand", "understood", "will understand"],
        "correct": "would have understood",
        "explanation": "<p><strong>would have understood</strong> is correct — present ability (she "
                       "doesn't speak Korean) explaining a past event.<br><br>"
                       "<em>(<strong>would have understood</strong> toʻgʻri — hozirgi qobiliyat (u "
                       "koreyscha bilmaydi) oʻtmishdagi voqeani tushuntiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Samandar had gone to bed earlier, he ___ so tired now.</strong></p>",
        "choices": ["wouldn't be", "wouldn't have been", "isn't", "won't be"],
        "correct": "wouldn't be",
        "explanation": "<p><strong>wouldn't be</strong> is correct — <em>now</em> tells you the result "
                       "belongs to the present.<br><br>"
                       "<em>(<strong>wouldn't be</strong> toʻgʻri — <em>now</em> natija hozirgi zamonga "
                       "tegishli ekanini koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which word tells you the result is in the present?</strong></p>",
        "choices": ["now", "yesterday", "last year", "in 2019"],
        "correct": "now",
        "explanation": "<p><strong>now</strong> is correct — <em>now, today, at the moment</em> pull the "
                       "result half into the present.<br><br>"
                       "<em>(<strong>now</strong> toʻgʻri — <em>now, today, at the moment</em> natija "
                       "qismini hozirgi zamonga tortadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Elbek had saved his money, he ___ a new bicycle today.</strong></p>",
        "choices": ["would have", "would have had", "has", "will have"],
        "correct": "would have",
        "explanation": "<p><strong>would have</strong> is correct — here <em>have</em> is the main verb "
                       "meaning “own”, and the result is present.<br><br>"
                       "<em>(<strong>would have</strong> toʻgʻri — bu yerda <em>have</em> “egalik "
                       "qilmoq” maʼnosidagi asosiy feʼl, natija esa hozirgi zamonda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Firdavs weren't afraid of water, he ___ swimming with us "
                "yesterday.</strong></p>",
        "choices": ["would have come", "would come", "came", "will come"],
        "correct": "would have come",
        "explanation": "<p><strong>would have come</strong> is correct — a lasting present fear, one "
                       "missed past occasion.<br><br>"
                       "<em>(<strong>would have come</strong> toʻgʻri — doimiy hozirgi qoʻrquv, "
                       "oʻtkazib yuborilgan bitta oʻtmish holati.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Javohir had taken that job, he ___ in Tashkent now.</strong></p>",
        "choices": ["would live", "would have lived", "lives", "lived"],
        "correct": "would live",
        "explanation": "<p><strong>would live</strong> is correct — a past decision shaping today's "
                       "life.<br><br>"
                       "<em>(<strong>would live</strong> toʻgʻri — oʻtmishdagi qaror bugungi hayotni "
                       "belgilaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is a mixed conditional?</strong></p>",
        "choices": ["If I had left earlier, I would be there by now.",
                    "If I had left earlier, I would have arrived on time.",
                    "If I leave earlier, I will arrive on time.",
                    "If I left earlier, I would arrive on time."],
        "correct": "If I had left earlier, I would be there by now.",
        "explanation": "<p><strong>If I had left earlier, I would be there by now.</strong> is correct — "
                       "the two halves sit in different times, which is what makes it mixed.<br><br>"
                       "<em>(<strong>If I had left earlier, I would be there by now.</strong> toʻgʻri — "
                       "ikki qism turli zamonda, aynan shu uni aralash qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Madina hadn't missed the bus, she ___ here already.</strong></p>",
        "choices": ["would be", "would have been", "is", "was"],
        "correct": "would be",
        "explanation": "<p><strong>would be</strong> is correct — <em>already</em> here points at the "
                       "present moment.<br><br>"
                       "<em>(<strong>would be</strong> toʻgʻri — bu yerda <em>already</em> hozirgi "
                       "daqiqaga ishora qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Shaxzoda didn't hate mathematics, she ___ that course last "
                "year.</strong></p>",
        "choices": ["would have chosen", "would choose", "chose", "will choose"],
        "correct": "would have chosen",
        "explanation": "<p><strong>would have chosen</strong> is correct — Mix 2 again: a present feeling "
                       "explaining a past choice.<br><br>"
                       "<em>(<strong>would have chosen</strong> toʻgʻri — yana 2-aralash tur: hozirgi "
                       "his oʻtmishdagi tanlovni tushuntiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Abdulloh had listened to Rozimurod teacher, he ___ the answer "
                "now.</strong></p>",
        "choices": ["would know", "would have known", "knows", "knew"],
        "correct": "would know",
        "explanation": "<p><strong>would know</strong> is correct — the listening was in the lesson, the "
                       "knowing would be now.<br><br>"
                       "<em>(<strong>would know</strong> toʻgʻri — tinglash darsda boʻlardi, bilish esa "
                       "hozir.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What are the real facts behind “If Sirojiddin had trained, he would be "
                "in the team now”?</strong></p>",
        "choices": ["He didn't train, and he isn't in the team.",
                    "He trained, and he is in the team.",
                    "He trained, but he isn't in the team.",
                    "He didn't train, but he is in the team."],
        "correct": "He didn't train, and he isn't in the team.",
        "explanation": "<p><strong>He didn't train, and he isn't in the team.</strong> is correct — as "
                       "always, both halves state the opposite of reality.<br><br>"
                       "<em>(<strong>U mashq qilmadi va jamoada emas.</strong> toʻgʻri — har doimgidek, "
                       "ikki qism ham haqiqatning aksini aytadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>If Marjona ___ the early train, she ___ with us now.</strong></p>",
        "choices": ["had taken … would be", "took … would be",
                    "had taken … would have been", "would take … had been"],
        "correct": "had taken … would be",
        "explanation": "<p><strong>had taken … would be</strong> is correct — past <em>if</em>-half, "
                       "present result.<br><br>"
                       "<em>(<strong>had taken … would be</strong> toʻgʻri — <em>if</em> qismi "
                       "oʻtmishda, natija esa hozirda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Davron were taller, he ___ that shot last night.</strong></p>",
        "choices": ["would have scored", "would score", "scored", "will score"],
        "correct": "would have scored",
        "explanation": "<p><strong>would have scored</strong> is correct — height is permanent, the shot "
                       "was one past moment.<br><br>"
                       "<em>(<strong>would have scored</strong> toʻgʻri — boʻy doimiy, zarba esa "
                       "oʻtmishdagi bitta daqiqa.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["If I would have studied harder, I would be at university now.",
                    "If I had studied harder, I would be at university now.",
                    "If I had studied harder, I would have entered university.",
                    "If I studied harder, I would get better marks."],
        "correct": "If I would have studied harder, I would be at university now.",
        "explanation": "<p><strong>If I would have studied harder …</strong> is the mistake — "
                       "<em>would</em> never appears after <em>if</em>, in any conditional, mixed or "
                       "not.<br><br>"
                       "<em>(<strong>If I would have studied harder …</strong> xato — aralash boʻladimi "
                       "yoki yoʻqmi, hech bir shart gapda <em>would</em> <em>if</em> dan keyin "
                       "kelmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["If Afsona hadn't helped me, I wouldn't be here today.",
                    "If Afsona didn't help me, I wouldn't be here today.",
                    "If Afsona hadn't helped me, I wouldn't been here today.",
                    "If Afsona wouldn't have helped me, I wouldn't be here today."],
        "correct": "If Afsona hadn't helped me, I wouldn't be here today.",
        "explanation": "<p><strong>If Afsona hadn't helped me, I wouldn't be here today.</strong> is "
                       "correct — past help, present situation.<br><br>"
                       "<em>(<strong>If Afsona hadn't helped me, I wouldn't be here today.</strong> "
                       "toʻgʻri — oʻtmishdagi yordam, hozirgi holat.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> You speak English so well, Jasur.</p>"
                "<p><strong>Jasur:</strong> ___</p>",
        "choices": ["If I hadn't started at seven, I wouldn't speak it so well now.",
                    "If I didn't start at seven, I wouldn't have spoken it so well now.",
                    "If I wouldn't have started at seven, I wouldn't speak it so well now.",
                    "If I hadn't started at seven, I wouldn't have spoken it so well now."],
        "correct": "If I hadn't started at seven, I wouldn't speak it so well now.",
        "explanation": "<p><strong>If I hadn't started at seven, I wouldn't speak it so well now.</strong> "
                       "is correct — the past beginning explains the present skill.<br><br>"
                       "<em>(<strong>If I hadn't started at seven, I wouldn't speak it so well "
                       "now.</strong> toʻgʻri — oʻtmishdagi boshlanish hozirgi mahoratni "
                       "tushuntiradi.)</em></p>",
    },
]


# =====================================================================
# PE-57 — wish and if only
# =====================================================================

Q_PE57 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I wish I ___ a car — I'm tired of taking the bus.</strong></p>",
        "choices": ["had", "have", "will have", "would have"],
        "correct": "had",
        "explanation": "<p><strong>had</strong> is correct — <em>wish + past simple</em> for a different "
                       "present. The real fact is: I don't have a car.<br><br>"
                       "<em>(<strong>had</strong> toʻgʻri — boshqacha hozirgi holat uchun <em>wish + past "
                       "simple</em>. Haqiqat esa: mashinam yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz wishes he ___ nearer to school.</strong></p>",
        "choices": ["lived", "lives", "will live", "would live"],
        "correct": "lived",
        "explanation": "<p><strong>lived</strong> is correct — a past form signalling that this present "
                       "is not real.<br><br>"
                       "<em>(<strong>lived</strong> toʻgʻri — oʻtgan zamon shakli bu hozirgi holat "
                       "haqiqiy emasligini bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I wish I ___ you — you look wonderful in that photo.</strong></p>",
        "choices": ["were", "am", "was being", "would be"],
        "correct": "were",
        "explanation": "<p><strong>were</strong> is correct — after <em>wish</em>, <em>were</em> is used "
                       "for every person, exactly as in the second conditional.<br><br>"
                       "<em>(<strong>were</strong> toʻgʻri — <em>wish</em> dan keyin har bir shaxs uchun "
                       "<em>were</em> ishlatiladi, xuddi ikkinchi shart gapdagidek.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda wishes she ___ harder for the exam last month.</strong></p>",
        "choices": ["had studied", "studied", "would study", "has studied"],
        "correct": "had studied",
        "explanation": "<p><strong>had studied</strong> is correct — <em>wish + past perfect</em> for "
                       "regret about a different past.<br><br>"
                       "<em>(<strong>had studied</strong> toʻgʻri — oʻtmish boshqacha boʻlishini "
                       "istash uchun <em>wish + past perfect</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “I wish I had told her” mean?</strong></p>",
        "choices": ["I didn't tell her, and I regret it.",
                    "I told her, and I'm glad.",
                    "I will tell her tomorrow.",
                    "I always tell her everything."],
        "correct": "I didn't tell her, and I regret it.",
        "explanation": "<p><strong>I didn't tell her, and I regret it.</strong> is correct — <em>wish</em> "
                       "always states the opposite of the truth.<br><br>"
                       "<em>(<strong>Men unga aytmadim va bunga afsuslanaman.</strong> toʻgʻri — "
                       "<em>wish</em> doim haqiqatning aksini aytadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I wish Charos ___ talking during the lesson — it's annoying.</strong></p>",
        "choices": ["would stop", "stopped", "stops", "had stopped"],
        "correct": "would stop",
        "explanation": "<p><strong>would stop</strong> is correct — <em>wish + would</em> complains about "
                       "somebody's behaviour that they could change.<br><br>"
                       "<em>(<strong>would stop</strong> toʻgʻri — <em>wish + would</em> odam oʻzgartira "
                       "oladigan xatti-harakatdan norozilik bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which one can you <em>not</em> say?</strong></p>",
        "choices": ["I wish I would be taller.", "I wish I were taller.",
                    "I wish he would drive more carefully.", "I wish I had a bicycle."],
        "correct": "I wish I would be taller.",
        "explanation": "<p><strong>I wish I would be taller.</strong> is wrong — <em>wish + would</em> is "
                       "for other people's behaviour, never for yourself or for things you cannot "
                       "change.<br><br>"
                       "<em>(<strong>I wish I would be taller.</strong> xato — <em>wish + would</em> "
                       "boshqalarning xatti-harakati uchun, oʻzingiz yoki oʻzgartirib boʻlmaydigan "
                       "narsalar uchun emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar wishes he ___ the answer.</strong></p>",
        "choices": ["knew", "knows", "would know", "has known"],
        "correct": "knew",
        "explanation": "<p><strong>knew</strong> is correct — a present wish, so the past simple."
                       "<br><br><em>(<strong>knew</strong> toʻgʻri — hozirgi istak, shuning uchun past "
                       "simple.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ I had listened to my parents!</strong></p>",
        "choices": ["If only", "If", "Although", "Unless"],
        "correct": "If only",
        "explanation": "<p><strong>If only</strong> is correct — it works exactly like <em>wish</em>, but "
                       "with stronger feeling.<br><br>"
                       "<em>(<strong>If only</strong> toʻgʻri — u aynan <em>wish</em> kabi ishlaydi, "
                       "lekin his-tuygʻusi kuchliroq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek wishes he ___ so much cake yesterday.</strong></p>",
        "choices": ["hadn't eaten", "didn't eat", "wouldn't eat", "hasn't eaten"],
        "correct": "hadn't eaten",
        "explanation": "<p><strong>hadn't eaten</strong> is correct — regret about something he did do."
                       "<br><br><em>(<strong>hadn't eaten</strong> toʻgʻri — u qilgan ish haqidagi "
                       "afsus.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference between <em>wish</em> and <em>hope</em>?</strong></p>",
        "choices": ["wish = it isn't true · hope = it is still possible",
                    "wish = it is possible · hope = it isn't true",
                    "They mean the same thing.",
                    "wish is future, hope is past."],
        "correct": "wish = it isn't true · hope = it is still possible",
        "explanation": "<p><strong>wish = it isn't true · hope = it is still possible</strong> is correct "
                       "— <em>I hope you pass</em> (real chance) vs <em>I wish I were taller</em> (not "
                       "real).<br><br>"
                       "<em>(<strong>wish = haqiqat emas · hope = hali mumkin</strong> toʻgʻri — <em>I "
                       "hope you pass</em> (haqiqiy imkoniyat) va <em>I wish I were taller</em> (haqiqiy "
                       "emas).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I ___ you pass your exam tomorrow!</strong></p>",
        "choices": ["hope", "wish", "wished", "would wish"],
        "correct": "hope",
        "explanation": "<p><strong>hope</strong> is correct — the exam is tomorrow and passing is "
                       "genuinely possible.<br><br>"
                       "<em>(<strong>hope</strong> toʻgʻri — imtihon ertaga va oʻtish haqiqatan ham "
                       "mumkin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs wishes his brother ___ his things without asking.</strong></p>",
        "choices": ["wouldn't take", "didn't take", "doesn't take", "hadn't taken"],
        "correct": "wouldn't take",
        "explanation": "<p><strong>wouldn't take</strong> is correct — an annoying habit that the other "
                       "person could change.<br><br>"
                       "<em>(<strong>wouldn't take</strong> toʻgʻri — boshqa odam oʻzgartira oladigan, "
                       "asabga tegadigan odat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir wishes he ___ Korean — then he could watch films without "
                "subtitles.</strong></p>",
        "choices": ["spoke", "speaks", "would speak", "had spoken"],
        "correct": "spoke",
        "explanation": "<p><strong>spoke</strong> is correct — a present wish about an ability he does "
                       "not have.<br><br>"
                       "<em>(<strong>spoke</strong> toʻgʻri — unda yoʻq boʻlgan qobiliyat haqidagi "
                       "hozirgi istak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If only Madina ___ me about the change of room!</strong></p>",
        "choices": ["had told", "told", "would tell", "tells"],
        "correct": "had told",
        "explanation": "<p><strong>had told</strong> is correct — regret about the past, so the past "
                       "perfect.<br><br>"
                       "<em>(<strong>had told</strong> toʻgʻri — oʻtmish haqidagi afsus, shuning uchun "
                       "past perfect.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>I wish I ___ more time now, and I wish I ___ this project "
                "earlier.</strong></p>",
        "choices": ["had … had started", "have … started", "had … started", "would have … had started"],
        "correct": "had … had started",
        "explanation": "<p><strong>had … had started</strong> is correct — a present wish and a past "
                       "regret in one sentence.<br><br>"
                       "<em>(<strong>had … had started</strong> toʻgʻri — bitta gapda hozirgi istak va "
                       "oʻtmishga afsus.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["I wish I would know the answer.", "I wish I knew the answer.",
                    "I wish I had known the answer.", "I wish he would tell me the answer."],
        "correct": "I wish I would know the answer.",
        "explanation": "<p><strong>I wish I would know the answer.</strong> is the mistake — "
                       "<em>wish + would</em> cannot be used about yourself.<br><br>"
                       "<em>(<strong>I wish I would know the answer.</strong> xato — <em>wish + "
                       "would</em> oʻzingiz haqingizda ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Shaxzoda wishes she were taller.", "Shaxzoda wishes she is taller.",
                    "Shaxzoda wishes she will be taller.", "Shaxzoda wishes she would be taller."],
        "correct": "Shaxzoda wishes she were taller.",
        "explanation": "<p><strong>Shaxzoda wishes she were taller.</strong> is correct — <em>were</em> "
                       "for every person after <em>wish</em>.<br><br>"
                       "<em>(<strong>Shaxzoda wishes she were taller.</strong> toʻgʻri — <em>wish</em> "
                       "dan keyin har bir shaxs uchun <em>were</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> You lost two marks for spelling, Sirojiddin.</p>"
                "<p><strong>Sirojiddin:</strong> ___</p>",
        "choices": ["I wish I had checked my work.", "I wish I checked my work.",
                    "I wish I would check my work.", "I hope I had checked my work."],
        "correct": "I wish I had checked my work.",
        "explanation": "<p><strong>I wish I had checked my work.</strong> is correct — the test is over, "
                       "so the regret belongs to the past.<br><br>"
                       "<em>(<strong>I wish I had checked my work.</strong> toʻgʻri — test tugagan, "
                       "shuning uchun afsus oʻtmishga tegishli.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["I wish I had a bike, I wish I had learnt to ride earlier, "
                    "and I wish my brother would lend me his.",
                    "I wish I have a bike, I wish I learnt to ride earlier, "
                    "and I wish my brother lends me his.",
                    "I wish I would have a bike, I wish I had learnt to ride earlier, "
                    "and I wish my brother lent me his.",
                    "I hope I had a bike, I wish I would learn to ride earlier, "
                    "and I wish my brother will lend me his."],
        "correct": "I wish I had a bike, I wish I had learnt to ride earlier, "
                   "and I wish my brother would lend me his.",
        "explanation": "<p><strong>had … had learnt … would lend</strong> is correct — the three uses in "
                       "one line: a different present, a different past, and somebody else's "
                       "behaviour.<br><br>"
                       "<em>(<strong>had … had learnt … would lend</strong> toʻgʻri — bitta qatorda "
                       "uchala qoʻllanish: boshqacha hozir, boshqacha oʻtmish va boshqa odamning "
                       "xatti-harakati.)</em></p>",
    },
]


# =====================================================================
# PE-58 — Relative Clauses
# =====================================================================

Q_PE58 = [
    {
        "text": "<p>Choose the correct relative pronoun.</p>"
                "<p><strong>I have a friend ___ lives in Khiva.</strong></p>",
        "choices": ["who", "which", "whose", "where"],
        "correct": "who",
        "explanation": "<p><strong>who</strong> is correct — <em>who</em> follows a person.<br><br>"
                       "<em>(<strong>who</strong> toʻgʻri — <em>who</em> shaxsdan keyin keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct relative pronoun.</p>"
                "<p><strong>This is the book ___ I bought yesterday.</strong></p>",
        "choices": ["which", "who", "whose", "when"],
        "correct": "which",
        "explanation": "<p><strong>which</strong> is correct — <em>which</em> follows a thing. "
                       "<em>That</em> would also work here.<br><br>"
                       "<em>(<strong>which</strong> toʻgʻri — <em>which</em> narsadan keyin keladi. Bu "
                       "yerda <em>that</em> ham boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Where does English put the description?</strong></p>",
        "choices": ["after the noun", "before the noun",
                    "at the start of the sentence", "at the end of the paragraph"],
        "correct": "after the noun",
        "explanation": "<p><strong>after the noun</strong> is correct — <em>the book that I read</em>. "
                       "Uzbek puts it before: <em>men oʻqigan kitob</em>. This one difference causes many "
                       "mistakes.<br><br>"
                       "<em>(<strong>otdan keyin</strong> toʻgʻri — <em>the book that I read</em>. "
                       "Oʻzbekcha esa oldin qoʻyadi: <em>men oʻqigan kitob</em>. Shu bitta farq koʻp "
                       "xatoga sabab boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct relative pronoun.</p>"
                "<p><strong>That's the girl ___ father is a doctor.</strong></p>",
        "choices": ["whose", "who's", "who", "which"],
        "correct": "whose",
        "explanation": "<p><strong>whose</strong> is correct — it shows possession. <em>Who's</em> means "
                       "<em>who is</em>.<br><br>"
                       "<em>(<strong>whose</strong> toʻgʻri — u egalikni bildiradi. <em>Who's</em> esa "
                       "<em>who is</em> degani.)</em></p>",
    },
    {
        "text": "<p>Choose the correct relative pronoun.</p>"
                "<p><strong>This is the school ___ Rozimurod teacher works.</strong></p>",
        "choices": ["where", "which", "who", "when"],
        "correct": "where",
        "explanation": "<p><strong>where</strong> is correct — <em>where</em> follows a place.<br><br>"
                       "<em>(<strong>where</strong> toʻgʻri — <em>where</em> joydan keyin "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct relative pronoun.</p>"
                "<p><strong>I remember the day ___ we won the competition.</strong></p>",
        "choices": ["when", "where", "which", "who"],
        "correct": "when",
        "explanation": "<p><strong>when</strong> is correct — <em>when</em> follows a time.<br><br>"
                       "<em>(<strong>when</strong> toʻgʻri — <em>when</em> vaqtdan keyin "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda is the pupil ___ won the olympiad.</strong></p>",
        "choices": ["who", "which", "whom", "where"],
        "correct": "who",
        "explanation": "<p><strong>who</strong> is correct — a person doing the action, so the subject "
                       "form.<br><br>"
                       "<em>(<strong>who</strong> toʻgʻri — harakatni bajarayotgan shaxs, yaʼni subject "
                       "shakli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In which sentence can you leave out the relative pronoun?</strong></p>",
        "choices": ["The book (that) Behruz bought is interesting.",
                    "The boy who bought the book is Behruz.",
                    "The school where he studies is new.",
                    "The girl whose bag was lost is crying."],
        "correct": "The book (that) Behruz bought is interesting.",
        "explanation": "<p><strong>The book (that) Behruz bought is interesting.</strong> is correct — "
                       "you may drop it when another subject follows (<em>Behruz</em>), never when the "
                       "pronoun is itself the subject.<br><br>"
                       "<em>(<strong>The book (that) Behruz bought is interesting.</strong> toʻgʻri — "
                       "keyin boshqa subject kelsa (<em>Behruz</em>) tushirib qoldirish mumkin, olmoshning "
                       "oʻzi subject boʻlsa esa hech qachon.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The film ___ we watched last night was excellent.</strong></p>",
        "choices": ["that", "who", "whose", "where"],
        "correct": "that",
        "explanation": "<p><strong>that</strong> is correct — for things, <em>that</em> and <em>which</em> "
                       "are both fine in this kind of clause.<br><br>"
                       "<em>(<strong>that</strong> toʻgʻri — narsalar uchun bu turdagi ergash gapda "
                       "<em>that</em> ham, <em>which</em> ham boʻladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos, ___ sits next to me, is from Nukus.</strong></p>",
        "choices": ["who", "which", "that", "whose"],
        "correct": "who",
        "explanation": "<p><strong>who</strong> is correct — with commas around a person's name, "
                       "<em>that</em> is not possible.<br><br>"
                       "<em>(<strong>who</strong> toʻgʻri — shaxs ismi vergul bilan ajratilganda "
                       "<em>that</em> ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence contains the “double object” mistake?</strong></p>",
        "choices": ["The book that I read it was long.",
                    "The book that I read was long.",
                    "The book I read was long.",
                    "The book which I read was long."],
        "correct": "The book that I read it was long.",
        "explanation": "<p><strong>The book that I read it was long.</strong> is the mistake — "
                       "<em>that</em> already stands for the book, so <em>it</em> is one object too "
                       "many.<br><br>"
                       "<em>(<strong>The book that I read it was long.</strong> xato — <em>that</em> "
                       "allaqachon kitobni bildiradi, shuning uchun <em>it</em> ortiqcha.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar has a brother ___ works in Tashkent.</strong></p>",
        "choices": ["who", "which", "where", "whose"],
        "correct": "who",
        "explanation": "<p><strong>who</strong> is correct — the brother is a person and he does the "
                       "working.<br><br>"
                       "<em>(<strong>who</strong> toʻgʻri — aka — shaxs va ishni u bajaradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>This is the house ___ roof was damaged in the storm.</strong></p>",
        "choices": ["whose", "which", "that", "where"],
        "correct": "whose",
        "explanation": "<p><strong>whose</strong> is correct — <em>whose</em> works for things as well as "
                       "people when something belongs to them.<br><br>"
                       "<em>(<strong>whose</strong> toʻgʻri — egalikni bildirganda <em>whose</em> "
                       "odamlarga ham, narsalarga ham ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence sounds like an adult speaking?</strong></p>",
        "choices": ["I have a friend who lives in Khiva and works as a doctor.",
                    "I have a friend. He lives in Khiva. He is a doctor.",
                    "I have a friend, he lives in Khiva, he is a doctor.",
                    "I have a friend which lives in Khiva he is a doctor."],
        "correct": "I have a friend who lives in Khiva and works as a doctor.",
        "explanation": "<p><strong>I have a friend who lives in Khiva and works as a doctor.</strong> is "
                       "correct — joining the facts into one clause is exactly what relative clauses are "
                       "for.<br><br>"
                       "<em>(<strong>I have a friend who lives in Khiva and works as a doctor.</strong> "
                       "toʻgʻri — faktlarni bitta ergash gapga birlashtirish — aynan shu ergash "
                       "gaplarning vazifasi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The shop ___ Elbek bought his bicycle is near the bazaar.</strong></p>",
        "choices": ["where", "which", "who", "when"],
        "correct": "where",
        "explanation": "<p><strong>where</strong> is correct — a place, and no other object follows to "
                       "make <em>which</em> possible.<br><br>"
                       "<em>(<strong>where</strong> toʻgʻri — joy, va <em>which</em> ni mumkin qiladigan "
                       "boshqa toʻldiruvchi yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs, ___ I met at the olympiad, is a very good "
                "mathematician.</strong></p>",
        "choices": ["whom", "which", "whose", "where"],
        "correct": "whom",
        "explanation": "<p><strong>whom</strong> is correct — the formal object form. In speech people "
                       "usually say <em>who</em>.<br><br>"
                       "<em>(<strong>whom</strong> toʻgʻri — rasmiy object shakli. Nutqda odatda "
                       "<em>who</em> deyiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["The girl which sits next to me is Madina.",
                    "The girl who sits next to me is Madina.",
                    "The girl that sits next to me is Madina.",
                    "The girl sitting next to me is Madina."],
        "correct": "The girl which sits next to me is Madina.",
        "explanation": "<p><strong>The girl which sits next to me is Madina.</strong> is the mistake — "
                       "<em>which</em> is for things, never for people.<br><br>"
                       "<em>(<strong>The girl which sits next to me is Madina.</strong> xato — "
                       "<em>which</em> narsalar uchun, odamlar uchun emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["The book that Javohir gave me is very useful.",
                    "The book that Javohir gave me it is very useful.",
                    "The book what Javohir gave me is very useful.",
                    "The book who Javohir gave me is very useful."],
        "correct": "The book that Javohir gave me is very useful.",
        "explanation": "<p><strong>The book that Javohir gave me is very useful.</strong> is correct — no "
                       "extra <em>it</em>, and <em>what</em> is never a relative pronoun here.<br><br>"
                       "<em>(<strong>The book that Javohir gave me is very useful.</strong> toʻgʻri — "
                       "ortiqcha <em>it</em> yoʻq, <em>what</em> esa bu yerda hech qachon nisbiy olmosh "
                       "boʻlmaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Which pupil helped you with the project?</p>"
                "<p><strong>Abdulloh:</strong> ___</p>",
        "choices": ["The boy who sits by the window — Sirojiddin.",
                    "The boy which sits by the window — Sirojiddin.",
                    "The boy what sits by the window — Sirojiddin.",
                    "The boy who he sits by the window — Sirojiddin."],
        "correct": "The boy who sits by the window — Sirojiddin.",
        "explanation": "<p><strong>The boy who sits by the window — Sirojiddin.</strong> is correct — "
                       "<em>who</em> for a person, and no extra <em>he</em>.<br><br>"
                       "<em>(<strong>The boy who sits by the window — Sirojiddin.</strong> toʻgʻri — "
                       "shaxs uchun <em>who</em>, ortiqcha <em>he</em> esa yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> pronoun is correct.</p>",
        "choices": ["Marjona, who won the prize, thanked the teacher whose lessons she loved, "
                    "in the hall where we all sat.",
                    "Marjona, which won the prize, thanked the teacher who's lessons she loved, "
                    "in the hall which we all sat.",
                    "Marjona, who won the prize, thanked the teacher which lessons she loved, "
                    "in the hall where we all sat there.",
                    "Marjona, that won the prize, thanked the teacher whose lessons she loved them, "
                    "in the hall when we all sat."],
        "correct": "Marjona, who won the prize, thanked the teacher whose lessons she loved, "
                   "in the hall where we all sat.",
        "explanation": "<p><strong>who … whose … where</strong> is correct — a person, a possession and a "
                       "place, with no doubled objects.<br><br>"
                       "<em>(<strong>who … whose … where</strong> toʻgʻri — shaxs, egalik va joy, "
                       "takrorlangan toʻldiruvchisiz.)</em></p>",
    },
]


# =====================================================================
# PE-59 — Defining vs Non-Defining
# =====================================================================

Q_PE59 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “My brother who lives in Tashkent is a doctor” "
                "suggest?</strong></p>",
        "choices": ["I have more than one brother.", "I have exactly one brother.",
                    "I have no brothers.", "My brother is not a doctor."],
        "correct": "I have more than one brother.",
        "explanation": "<p><strong>I have more than one brother.</strong> is correct — with no commas the "
                       "clause is essential: it tells you <em>which</em> brother.<br><br>"
                       "<em>(<strong>Mening bir nechta akam bor.</strong> toʻgʻri — vergulsiz ergash gap "
                       "zarur boʻlib, <em>qaysi</em> aka ekanini aytadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “My brother, who lives in Tashkent, is a doctor” "
                "suggest?</strong></p>",
        "choices": ["I have exactly one brother.", "I have several brothers.",
                    "My brother doesn't live in Tashkent.", "I don't know my brother."],
        "correct": "I have exactly one brother.",
        "explanation": "<p><strong>I have exactly one brother.</strong> is correct — the commas make the "
                       "clause extra information, not identification.<br><br>"
                       "<em>(<strong>Mening bitta akam bor.</strong> toʻgʻri — vergullar ergash gapni "
                       "qoʻshimcha maʼlumotga aylantiradi, aniqlovchiga emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>A defining clause ___ .</strong></p>",
        "choices": ["is essential and takes no commas",
                    "is extra and takes commas",
                    "always uses which",
                    "can always be removed"],
        "correct": "is essential and takes no commas",
        "explanation": "<p><strong>is essential and takes no commas</strong> is correct — remove it and "
                       "the sentence no longer identifies anybody.<br><br>"
                       "<em>(<strong>zarur va vergul olmaydi</strong> toʻgʻri — uni olib tashlasangiz, "
                       "gap kimni nazarda tutayotganini koʻrsatmay qoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz, ___ father is a driver, wants to be an engineer.</strong></p>",
        "choices": ["whose", "who's", "that", "which"],
        "correct": "whose",
        "explanation": "<p><strong>whose</strong> is correct — possession, inside a non-defining clause "
                       "marked by commas.<br><br>"
                       "<em>(<strong>whose</strong> toʻgʻri — egalik, vergul bilan ajratilgan "
                       "qoʻshimcha ergash gap ichida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which rule changes when you add commas?</strong></p>",
        "choices": ["that becomes impossible", "who becomes impossible",
                    "whose becomes impossible", "where becomes impossible"],
        "correct": "that becomes impossible",
        "explanation": "<p><strong>that becomes impossible</strong> is correct — non-defining clauses "
                       "take <em>who</em> or <em>which</em>, never <em>that</em>, and the pronoun can "
                       "never be dropped.<br><br>"
                       "<em>(<strong>that ishlatib boʻlmaydi</strong> toʻgʻri — qoʻshimcha ergash gaplar "
                       "<em>who</em> yoki <em>which</em> oladi, <em>that</em> emas, va olmosh hech qachon "
                       "tushirilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samarkand, ___ is famous for the Registan, is very old.</strong></p>",
        "choices": ["which", "that", "who", "where"],
        "correct": "which",
        "explanation": "<p><strong>which</strong> is correct — extra information about a unique place, so "
                       "commas and <em>which</em>.<br><br>"
                       "<em>(<strong>which</strong> toʻgʻri — yagona joy haqidagi qoʻshimcha maʼlumot, "
                       "shuning uchun vergul va <em>which</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The pupil ___ sits next to me is from Nukus.</strong></p>",
        "choices": ["who", ", who", ", which", ", that"],
        "correct": "who",
        "explanation": "<p><strong>who</strong> is correct — no commas, because the clause identifies "
                       "which pupil.<br><br>"
                       "<em>(<strong>who</strong> toʻgʻri — vergul yoʻq, chunki ergash gap qaysi oʻquvchi "
                       "ekanini aniqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda, ___ won the olympiad, is only fifteen.</strong></p>",
        "choices": ["who", "that", "which", "whom"],
        "correct": "who",
        "explanation": "<p><strong>who</strong> is correct — after a name the clause can only be extra, "
                       "so commas and <em>who</em>.<br><br>"
                       "<em>(<strong>who</strong> toʻgʻri — ismdan keyin ergash gap faqat qoʻshimcha "
                       "boʻladi, shuning uchun vergul va <em>who</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos passed all her exams, ___ made her parents very "
                "proud.</strong></p>",
        "choices": ["which", "that", "who", "what"],
        "correct": "which",
        "explanation": "<p><strong>which</strong> is correct — here <em>which</em> refers to the whole "
                       "idea in the first half, not to one noun.<br><br>"
                       "<em>(<strong>which</strong> toʻgʻri — bu yerda <em>which</em> bitta otga emas, "
                       "birinchi qismdagi butun fikrga ishora qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is punctuated correctly?</strong></p>",
        "choices": ["Rozimurod teacher, who teaches us English, is very patient.",
                    "Rozimurod teacher who teaches us English, is very patient.",
                    "Rozimurod teacher, who teaches us English is very patient.",
                    "Rozimurod teacher, that teaches us English, is very patient."],
        "correct": "Rozimurod teacher, who teaches us English, is very patient.",
        "explanation": "<p><strong>Rozimurod teacher, who teaches us English, is very patient.</strong> "
                       "is correct — a non-defining clause needs a comma at <em>both</em> ends.<br><br>"
                       "<em>(<strong>Rozimurod teacher, who teaches us English, is very patient.</strong> "
                       "toʻgʻri — qoʻshimcha ergash gap <em>ikki</em> tomonidan vergul talab "
                       "qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The car ___ Elbek's father bought is very fast.</strong></p>",
        "choices": ["that", ", which", ", that", ", who"],
        "correct": "that",
        "explanation": "<p><strong>that</strong> is correct — it identifies which car, so no commas."
                       "<br><br><em>(<strong>that</strong> toʻgʻri — u qaysi mashina ekanini aniqlaydi, "
                       "shuning uchun vergul qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In a non-defining clause, can you drop the pronoun?</strong></p>",
        "choices": ["No, never.", "Yes, always.",
                    "Only with people.", "Only with things."],
        "correct": "No, never.",
        "explanation": "<p><strong>No, never.</strong> is correct — dropping is only possible in defining "
                       "clauses where another subject follows.<br><br>"
                       "<em>(<strong>Yoʻq, hech qachon.</strong> toʻgʻri — tushirib qoldirish faqat "
                       "keyin boshqa subject keladigan zarur ergash gaplarda mumkin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs, ___ I have known since primary school, is my best "
                "friend.</strong></p>",
        "choices": ["who", "that", "which", "what"],
        "correct": "who",
        "explanation": "<p><strong>who</strong> is correct — a person in an extra clause. <em>Whom</em> "
                       "would be the formal alternative.<br><br>"
                       "<em>(<strong>who</strong> toʻgʻri — qoʻshimcha ergash gapdagi shaxs. Rasmiy "
                       "variant esa <em>whom</em> boʻlardi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence says the writer has only one sister?</strong></p>",
        "choices": ["My sister, who lives in Andijan, is a teacher.",
                    "My sister who lives in Andijan is a teacher.",
                    "My sister that lives in Andijan is a teacher.",
                    "The sister who lives in Andijan is a teacher."],
        "correct": "My sister, who lives in Andijan, is a teacher.",
        "explanation": "<p><strong>My sister, who lives in Andijan, is a teacher.</strong> is correct — "
                       "the commas turn the clause into a simple extra fact.<br><br>"
                       "<em>(<strong>My sister, who lives in Andijan, is a teacher.</strong> toʻgʻri — "
                       "vergullar ergash gapni oddiy qoʻshimcha faktga aylantiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir missed the bus, ___ meant he was late for the "
                "olympiad.</strong></p>",
        "choices": ["which", "that", "what", "who"],
        "correct": "which",
        "explanation": "<p><strong>which</strong> is correct — again referring back to the whole first "
                       "half.<br><br>"
                       "<em>(<strong>which</strong> toʻgʻri — yana butun birinchi qismga ishora "
                       "qilmoqda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The house ___ we visited last summer has been sold.</strong></p>",
        "choices": ["that", ", which", ", that", ", where"],
        "correct": "that",
        "explanation": "<p><strong>that</strong> is correct — it defines which house, so no commas."
                       "<br><br><em>(<strong>that</strong> toʻgʻri — u qaysi uy ekanini aniqlaydi, "
                       "shuning uchun vergulsiz.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Madina, that helped me yesterday, is very kind.",
                    "Madina, who helped me yesterday, is very kind.",
                    "The girl that helped me yesterday is very kind.",
                    "The girl who helped me yesterday is very kind."],
        "correct": "Madina, that helped me yesterday, is very kind.",
        "explanation": "<p><strong>Madina, that helped me yesterday, is very kind.</strong> is the "
                       "mistake — <em>that</em> cannot be used in a clause marked off by commas.<br><br>"
                       "<em>(<strong>Madina, that helped me yesterday, is very kind.</strong> xato — "
                       "vergul bilan ajratilgan ergash gapda <em>that</em> ishlatilmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Shaxzoda, whose brother is a pilot, wants to study in Seoul.",
                    "Shaxzoda whose brother is a pilot, wants to study in Seoul.",
                    "Shaxzoda, who's brother is a pilot, wants to study in Seoul.",
                    "Shaxzoda, that her brother is a pilot, wants to study in Seoul."],
        "correct": "Shaxzoda, whose brother is a pilot, wants to study in Seoul.",
        "explanation": "<p><strong>Shaxzoda, whose brother is a pilot, wants to study in Seoul.</strong> "
                       "is correct — commas on both sides, and <em>whose</em> for possession.<br><br>"
                       "<em>(<strong>Shaxzoda, whose brother is a pilot, wants to study in Seoul.</strong> "
                       "toʻgʻri — ikki tomonda vergul va egalik uchun <em>whose</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Sirojiddin:</strong> Do you know Davron?</p>"
                "<p><strong>Abdulloh:</strong> ___</p>",
        "choices": ["Yes — the boy who won the chess tournament, isn't he?",
                    "Yes — the boy, who won the chess tournament isn't he?",
                    "Yes — the boy which won the chess tournament, isn't he?",
                    "Yes — the boy, that won the chess tournament, isn't he?"],
        "correct": "Yes — the boy who won the chess tournament, isn't he?",
        "explanation": "<p><strong>Yes — the boy who won the chess tournament, isn't he?</strong> is "
                       "correct — the clause identifies which boy, so no commas and <em>who</em> for a "
                       "person.<br><br>"
                       "<em>(<strong>Yes — the boy who won the chess tournament, isn't he?</strong> "
                       "toʻgʻri — ergash gap qaysi bola ekanini aniqlaydi, shuning uchun vergulsiz va "
                       "shaxs uchun <em>who</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["Afsona, who sits behind me, lent me the book that I needed, "
                    "which was very kind of her.",
                    "Afsona who sits behind me, lent me the book, that I needed, "
                    "which was very kind of her.",
                    "Afsona, that sits behind me, lent me the book which I needed it, "
                    "what was very kind of her.",
                    "Afsona, who sits behind me lent me the book that I needed it, "
                    "which was very kind of her."],
        "correct": "Afsona, who sits behind me, lent me the book that I needed, "
                   "which was very kind of her.",
        "explanation": "<p><strong>who … that … which</strong> is correct — an extra clause with commas, "
                       "a defining clause without them, and <em>which</em> for the whole idea.<br><br>"
                       "<em>(<strong>who … that … which</strong> toʻgʻri — vergulli qoʻshimcha ergash "
                       "gap, vergulsiz zarur ergash gap va butun fikrga ishora qiluvchi "
                       "<em>which</em>.)</em></p>",
    },
]


# =====================================================================
# PE-60 — Passive Voice: Present and Past
# =====================================================================

Q_PE60 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>This house ___ in 1890.</strong></p>",
        "choices": ["was built", "built", "is built", "was build"],
        "correct": "was built",
        "explanation": "<p><strong>was built</strong> is correct — the passive is <em>be + V3</em>, and "
                       "the past needs <em>was</em>.<br><br>"
                       "<em>(<strong>was built</strong> toʻgʻri — passiv <em>be + V3</em> shaklida, "
                       "oʻtgan zamon esa <em>was</em> talab qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>English ___ by millions of people.</strong></p>",
        "choices": ["is spoken", "speaks", "is speaking", "was spoke"],
        "correct": "is spoken",
        "explanation": "<p><strong>is spoken</strong> is correct — present passive: <em>am / is / are + "
                       "V3</em>.<br><br>"
                       "<em>(<strong>is spoken</strong> toʻgʻri — hozirgi zamon passivi: "
                       "<em>am / is / are + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the formula for the passive?</strong></p>",
        "choices": ["be + V3", "have + V3", "be + V-ing", "do + V3"],
        "correct": "be + V3",
        "explanation": "<p><strong>be + V3</strong> is correct — only <em>be</em> changes for tense and "
                       "person; the third form never moves.<br><br>"
                       "<em>(<strong>be + V3</strong> toʻgʻri — zamon va shaxsga qarab faqat <em>be</em> "
                       "oʻzgaradi; uchinchi shakl esa oʻzgarmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>My bicycle ___ last week.</strong></p>",
        "choices": ["was stolen", "stole", "is stolen", "was stole"],
        "correct": "was stolen",
        "explanation": "<p><strong>was stolen</strong> is correct — we don't know who took it, and it "
                       "doesn't matter: that is exactly when English chooses the passive.<br><br>"
                       "<em>(<strong>was stolen</strong> toʻgʻri — kim olganini bilmaymiz va bu muhim "
                       "emas: ingliz tili aynan shunday paytda passivni tanlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The letters ___ every morning.</strong></p>",
        "choices": ["are delivered", "deliver", "is delivered", "are deliver"],
        "correct": "are delivered",
        "explanation": "<p><strong>are delivered</strong> is correct — a plural subject takes "
                       "<em>are</em>.<br><br>"
                       "<em>(<strong>are delivered</strong> toʻgʻri — koʻplikdagi subject <em>are</em> "
                       "oladi.)</em></p>",
    },
    {
        "text": "<p>Make this active sentence passive.</p>"
                "<p><strong>Amir Temur built this mosque.</strong></p>",
        "choices": ["This mosque was built by Amir Temur.",
                    "This mosque built by Amir Temur.",
                    "This mosque is built from Amir Temur.",
                    "This mosque was build by Amir Temur."],
        "correct": "This mosque was built by Amir Temur.",
        "explanation": "<p><strong>This mosque was built by Amir Temur.</strong> is correct — the "
                       "receiver becomes the subject, and the doer follows <em>by</em>.<br><br>"
                       "<em>(<strong>This mosque was built by Amir Temur.</strong> toʻgʻri — qabul "
                       "qiluvchi subject boʻladi, bajaruvchi esa <em>by</em> dan keyin keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>When should you leave out <em>by</em>?</strong></p>",
        "choices": ["When the doer is unknown or unimportant.",
                    "Always — by is never used.",
                    "When the doer is famous.",
                    "When the sentence is in the past."],
        "correct": "When the doer is unknown or unimportant.",
        "explanation": "<p><strong>When the doer is unknown or unimportant.</strong> is correct — "
                       "<em>My bike was stolen</em> needs no <em>by somebody</em>.<br><br>"
                       "<em>(<strong>Bajaruvchi nomaʼlum yoki muhim boʻlmaganda.</strong> toʻgʻri — "
                       "<em>My bike was stolen</em> gapiga <em>by somebody</em> kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Our classroom ___ every day.</strong></p>",
        "choices": ["is cleaned", "cleans", "is cleaning", "are cleaned"],
        "correct": "is cleaned",
        "explanation": "<p><strong>is cleaned</strong> is correct — a singular subject in the present "
                       "passive.<br><br>"
                       "<em>(<strong>is cleaned</strong> toʻgʻri — hozirgi zamon passivida birlikdagi "
                       "subject.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The tests ___ by Rozimurod teacher yesterday.</strong></p>",
        "choices": ["were marked", "was marked", "marked", "are marked"],
        "correct": "were marked",
        "explanation": "<p><strong>were marked</strong> is correct — plural subject, past time, and "
                       "<em>by</em> is kept because the person matters.<br><br>"
                       "<em>(<strong>were marked</strong> toʻgʻri — koʻplikdagi subject, oʻtgan zamon, "
                       "va bu yerda shaxs muhim boʻlgani uchun <em>by</em> saqlanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rice ___ in many countries of Asia.</strong></p>",
        "choices": ["is grown", "grows it", "is growing", "are grown"],
        "correct": "is grown",
        "explanation": "<p><strong>is grown</strong> is correct — uncountable subject, and the growers "
                       "are unimportant.<br><br>"
                       "<em>(<strong>is grown</strong> toʻgʻri — sanalmaydigan subject, yetishtiruvchilar "
                       "esa muhim emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence is passive?</strong></p>",
        "choices": ["The window was broken by Behruz.", "Behruz broke the window.",
                    "Behruz was breaking the window.", "Behruz has broken the window."],
        "correct": "The window was broken by Behruz.",
        "explanation": "<p><strong>The window was broken by Behruz.</strong> is correct — the receiver "
                       "sits in the subject seat, which is the mark of the passive.<br><br>"
                       "<em>(<strong>The window was broken by Behruz.</strong> toʻgʻri — qabul qiluvchi "
                       "subject oʻrnida turibdi, bu esa passivning belgisi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>These photos ___ by Iroda last summer.</strong></p>",
        "choices": ["were taken", "was taken", "are taken", "were took"],
        "correct": "were taken",
        "explanation": "<p><strong>were taken</strong> is correct — <em>take → took → taken</em>, and the "
                       "V3 is required.<br><br>"
                       "<em>(<strong>were taken</strong> toʻgʻri — <em>take → took → taken</em>, va V3 "
                       "talab qilinadi.)</em></p>",
    },
    {
        "text": "<p>Make this passive sentence active.</p>"
                "<p><strong>The homework was checked by Charos.</strong></p>",
        "choices": ["Charos checked the homework.", "Charos was checked the homework.",
                    "The homework checked Charos.", "Charos is checked the homework."],
        "correct": "Charos checked the homework.",
        "explanation": "<p><strong>Charos checked the homework.</strong> is correct — the doer moves to "
                       "the front and <em>by</em> disappears.<br><br>"
                       "<em>(<strong>Charos checked the homework.</strong> toʻgʻri — bajaruvchi gap "
                       "boshiga oʻtadi, <em>by</em> esa yoʻqoladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which is a reason to use the passive?</strong></p>",
        "choices": ["The receiver is more important than the doer.",
                    "The sentence is too short.",
                    "You want to use more words.",
                    "The verb is irregular."],
        "correct": "The receiver is more important than the doer.",
        "explanation": "<p><strong>The receiver is more important than the doer.</strong> is correct — "
                       "that is why news and science are full of passives.<br><br>"
                       "<em>(<strong>Qabul qiluvchi bajaruvchidan muhimroq.</strong> toʻgʻri — shuning "
                       "uchun yangiliklar va ilmiy matnlar passivga toʻla.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>The new library ___ last year.</strong></p>",
        "choices": ["was opened", "opened by", "is opened", "was open"],
        "correct": "was opened",
        "explanation": "<p><strong>was opened</strong> is correct — <em>was open</em> would describe a "
                       "state, not the event of opening.<br><br>"
                       "<em>(<strong>was opened</strong> toʻgʻri — <em>was open</em> ochilish voqeasini "
                       "emas, holatni bildirgan boʻlardi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar's phone ___ in the bazaar yesterday.</strong></p>",
        "choices": ["was found", "found", "is found", "were found"],
        "correct": "was found",
        "explanation": "<p><strong>was found</strong> is correct — singular subject, past passive, and "
                       "the finder is unknown.<br><br>"
                       "<em>(<strong>was found</strong> toʻgʻri — birlikdagi subject, oʻtgan zamon "
                       "passivi, topgan odam esa nomaʼlum.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["The window was broke by the wind.", "The window was broken by the wind.",
                    "The wind broke the window.", "The windows were broken by the wind."],
        "correct": "The window was broke by the wind.",
        "explanation": "<p><strong>The window was broke by the wind.</strong> is the mistake — the "
                       "passive needs the third form <em>broken</em>, not the past form "
                       "<em>broke</em>.<br><br>"
                       "<em>(<strong>The window was broke by the wind.</strong> xato — passivga uchinchi "
                       "shakl <em>broken</em> kerak, oʻtgan zamon shakli <em>broke</em> emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["These carpets are made in Samarkand.",
                    "These carpets are make in Samarkand.",
                    "These carpets is made in Samarkand.",
                    "These carpets are made from Samarkand."],
        "correct": "These carpets are made in Samarkand.",
        "explanation": "<p><strong>These carpets are made in Samarkand.</strong> is correct — plural "
                       "<em>are</em>, the V3 <em>made</em>, and <em>in</em> for the place.<br><br>"
                       "<em>(<strong>These carpets are made in Samarkand.</strong> toʻgʻri — koʻplik "
                       "uchun <em>are</em>, V3 shakli <em>made</em> va joy uchun <em>in</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Elbek:</strong> What happened to your bike?</p>"
                "<p><strong>Firdavs:</strong> ___</p>",
        "choices": ["It was stolen outside the shop.", "It stole outside the shop.",
                    "It was stole outside the shop.", "It is stolen outside the shop yesterday."],
        "correct": "It was stolen outside the shop.",
        "explanation": "<p><strong>It was stolen outside the shop.</strong> is correct — the thief is "
                       "unknown, so no <em>by</em> is needed.<br><br>"
                       "<em>(<strong>It was stolen outside the shop.</strong> toʻgʻri — oʻgʻri "
                       "nomaʼlum, shuning uchun <em>by</em> kerak emas.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["This mosque was built in the 15th century, and it is visited by thousands "
                    "of tourists every year.",
                    "This mosque was build in the 15th century, and it is visit by thousands "
                    "of tourists every year.",
                    "This mosque built in the 15th century, and it visits by thousands "
                    "of tourists every year.",
                    "This mosque was built in the 15th century, and it was visited by thousands "
                    "of tourists every year now."],
        "correct": "This mosque was built in the 15th century, and it is visited by thousands "
                   "of tourists every year.",
        "explanation": "<p><strong>was built … is visited …</strong> is correct — a past passive for the "
                       "building and a present passive for what happens every year.<br><br>"
                       "<em>(<strong>was built … is visited …</strong> toʻgʻri — qurilish uchun oʻtgan "
                       "zamon passivi, har yili takrorlanadigan ish uchun esa hozirgi zamon "
                       "passivi.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-56 Practice: Mixed Conditionals",
        "tutorial":    "PE-56:",
        "description": "PE-56 darsiga 20 savol: oʻtmishdagi sabab → hozirgi natija va hozirgi sabab "
                       "→ oʻtmishdagi natija, qaysi aralash tur kerakligini aniqlash va if dan "
                       "keyin would ishlatilmasligi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE56,
    },
    {
        "title":       "PE-57 Practice: wish and if only",
        "tutorial":    "PE-57:",
        "description": "PE-57 darsiga 20 savol: wish + past simple, wish + past perfect, wish + "
                       "would bilan norozilik, if only hamda wish va hope farqi. Javoblar ingliz va "
                       "oʻzbek tilida izohlangan.",
        "questions":   Q_PE57,
    },
    {
        "title":       "PE-58 Practice: Relative Clauses: who, which, that",
        "tutorial":    "PE-58:",
        "description": "PE-58 darsiga 20 savol: who, which, that, whose, where, when; taʼrifning "
                       "otdan keyin kelishi, olmoshni tushirib qoldirish va “ikki toʻldiruvchi” "
                       "xatosi. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE58,
    },
    {
        "title":       "PE-59 Practice: Defining vs Non-Defining Relative Clauses",
        "tutorial":    "PE-59:",
        "description": "PE-59 darsiga 20 savol: vergulsiz zarur ergash gap va vergulli qoʻshimcha "
                       "ergash gap, vergul bilan oʻzgaradigan qoidalar hamda butun fikrga ishora "
                       "qiluvchi which. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE59,
    },
    {
        "title":       "PE-60 Practice: Passive Voice: Present and Past",
        "tutorial":    "PE-60:",
        "description": "PE-60 darsiga 20 savol: be + V3 hozirgi va oʻtgan zamonda, aktivni passivga "
                       "aylantirish, passiv tanlanadigan holatlar va by qachon qoʻyilishi. Javoblar "
                       "ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE60,
    },
]
