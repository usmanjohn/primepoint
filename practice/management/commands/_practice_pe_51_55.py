# -*- coding: utf-8 -*-
"""Prime English practices — PE-51 … PE-55.

End of Block D (the modal scale) and the start of Block E: conjunctions and the
first three conditionals.
Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_51_55.py --master=prime --expect-questions=20
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
# PE-51 — Modal Verbs: The Full Strength Scale
# =====================================================================

Q_PE51 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which modal is the <em>strongest</em> obligation?</strong></p>",
        "choices": ["must", "should", "could", "might"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — 100% on the obligation scale, followed by "
                       "<em>had better</em> (80%), <em>should</em> (70%) and <em>could</em> (30%)."
                       "<br><br><em>(<strong>must</strong> toʻgʻri — majburiyat shkalasida 100%, keyin "
                       "<em>had better</em> (80%), <em>should</em> (70%) va <em>could</em> "
                       "(30%).)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which one is only a gentle suggestion?</strong></p>",
        "choices": ["could", "must", "had better", "have to"],
        "correct": "could",
        "explanation": "<p><strong>could</strong> is correct — <em>You could ask Rozimurod teacher</em> "
                       "leaves the decision completely free.<br><br>"
                       "<em>(<strong>could</strong> toʻgʻri — <em>You could ask Rozimurod teacher</em> "
                       "qarorni butunlay erkin qoldiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which two rows on the obligation scale must never be confused?</strong></p>",
        "choices": ["don't have to and mustn't", "must and have to",
                    "should and ought to", "could and might"],
        "correct": "don't have to and mustn't",
        "explanation": "<p><strong>don't have to and mustn't</strong> is correct — one frees you, the "
                       "other forbids you. Everything else on the scale is a matter of degree.<br><br>"
                       "<em>(<strong>don't have to va mustn't</strong> toʻgʻri — biri ozod qiladi, "
                       "ikkinchisi taqiqlaydi. Shkaladagi qolgan hamma narsa faqat daraja "
                       "masalasi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Behruz ___ wear a helmet on his bike — it's the law.</strong></p>",
        "choices": ["must", "could", "might", "doesn't have to"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — a law sits at the top of the scale."
                       "<br><br><em>(<strong>must</strong> toʻgʻri — qonun shkalaning eng "
                       "tepasida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda ___ come tomorrow — it's optional.</strong></p>",
        "choices": ["doesn't have to", "mustn't", "can't", "shouldn't"],
        "correct": "doesn't have to",
        "explanation": "<p><strong>doesn't have to</strong> is correct — zero obligation, free "
                       "choice.<br><br>"
                       "<em>(<strong>doesn't have to</strong> toʻgʻri — majburiyat nol, tanlov "
                       "erkin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>On the certainty scale, which is about 95% sure?</strong></p>",
        "choices": ["must be", "might be", "can't be", "could be"],
        "correct": "must be",
        "explanation": "<p><strong>must be</strong> is correct — <em>must be</em> 95% → "
                       "<em>may / might / could be</em> 50% → <em>can't be</em> 5%.<br><br>"
                       "<em>(<strong>must be</strong> toʻgʻri — <em>must be</em> 95% → "
                       "<em>may / might / could be</em> 50% → <em>can't be</em> 5%.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Charos ___ be at the library — I'm almost sure.</strong></p>",
        "choices": ["must", "might", "can't", "shouldn't"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — <em>almost sure</em> puts it at the top of "
                       "the certainty scale.<br><br>"
                       "<em>(<strong>must</strong> toʻgʻri — <em>almost sure</em> uni ishonch "
                       "shkalasining tepasiga qoʻyadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which modal family does <em>be able to</em> belong to?</strong></p>",
        "choices": ["ability", "obligation", "certainty", "permission"],
        "correct": "ability",
        "explanation": "<p><strong>ability</strong> is correct — the third family: <em>can</em>, "
                       "<em>could</em>, <em>be able to</em>.<br><br>"
                       "<em>(<strong>qobiliyat</strong> toʻgʻri — uchinchi oila: <em>can</em>, "
                       "<em>could</em>, <em>be able to</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How does <em>must</em> (obligation) move into the past?</strong></p>",
        "choices": ["had to", "must have", "musted", "would must"],
        "correct": "had to",
        "explanation": "<p><strong>had to</strong> is correct — <em>must have + V3</em> exists too, but "
                       "it means deduction about the past, not obligation.<br><br>"
                       "<em>(<strong>had to</strong> toʻgʻri — <em>must have + V3</em> ham bor, lekin u "
                       "majburiyat emas, oʻtmish haqidagi xulosani bildiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How does <em>can</em> move into the future?</strong></p>",
        "choices": ["will be able to", "will can", "could will", "shall can"],
        "correct": "will be able to",
        "explanation": "<p><strong>will be able to</strong> is correct — two modals never stand "
                       "together.<br><br>"
                       "<em>(<strong>will be able to</strong> toʻgʻri — ikki modal yonma-yon "
                       "kelmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ hurry — the train leaves in ten minutes.</strong></p>",
        "choices": ["had better", "could", "doesn't have to", "might"],
        "correct": "had better",
        "explanation": "<p><strong>had better</strong> is correct — 80%: advice with a real consequence "
                       "behind it.<br><br>"
                       "<em>(<strong>had better</strong> toʻgʻri — 80%: ortida haqiqiy oqibati bor "
                       "maslahat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which of the four rules is true for every modal?</strong></p>",
        "choices": ["No -s, no to, questions by inversion, negative with not.",
                    "They take -s and to, and use do in questions.",
                    "They change form in every tense.",
                    "They can follow another modal."],
        "correct": "No -s, no to, questions by inversion, negative with not.",
        "explanation": "<p><strong>No -s, no to, questions by inversion, negative with not.</strong> is "
                       "correct — the only exception is <em>ought</em>, which keeps <em>to</em>.<br><br>"
                       "<em>(<strong>-s yoʻq, to yoʻq, savol inversiya bilan, inkor not bilan.</strong> "
                       "toʻgʻri — yagona istisno <em>ought</em>, u <em>to</em> ni saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek ___ be tired — he slept all afternoon.</strong></p>",
        "choices": ["can't", "must", "should", "had better"],
        "correct": "can't",
        "explanation": "<p><strong>can't</strong> is correct — the evidence makes tiredness almost "
                       "impossible: 5% on the scale.<br><br>"
                       "<em>(<strong>can't</strong> toʻgʻri — dalil charchoqni deyarli imkonsiz qiladi: "
                       "shkalada 5%.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ ask Rozimurod teacher — it's just an idea.</strong></p>",
        "choices": ["could", "must", "has to", "mustn't"],
        "correct": "could",
        "explanation": "<p><strong>could</strong> is correct — 30%: a suggestion with no pressure at "
                       "all.<br><br>"
                       "<em>(<strong>could</strong> toʻgʻri — 30%: hech qanday bosimsiz "
                       "taklif.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence puts the least pressure on the listener?</strong></p>",
        "choices": ["You could try again.", "You must try again.",
                    "You have to try again.", "You'd better try again."],
        "correct": "You could try again.",
        "explanation": "<p><strong>You could try again.</strong> is correct — the softest step on the "
                       "obligation scale.<br><br>"
                       "<em>(<strong>You could try again.</strong> toʻgʻri — majburiyat shkalasidagi eng "
                       "yumshoq pogʻona.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir ___ have finished — I saw him leave an hour ago.</strong></p>",
        "choices": ["must", "should", "had better", "can"],
        "correct": "must",
        "explanation": "<p><strong>must</strong> is correct — deduction about the past, using "
                       "<em>modal + have + V3</em> from PE-48.<br><br>"
                       "<em>(<strong>must</strong> toʻgʻri — oʻtmish haqidagi xulosa, PE-48 dagi "
                       "<em>modal + have + V3</em> qolipida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>You ___ wear a uniform (it's the rule), but you ___ wear a tie "
                "(it's optional).</strong></p>",
        "choices": ["have to … don't have to", "don't have to … have to",
                    "mustn't … must", "must … mustn't"],
        "correct": "have to … don't have to",
        "explanation": "<p><strong>have to … don't have to</strong> is correct — the top and the bottom "
                       "of the obligation scale in one sentence.<br><br>"
                       "<em>(<strong>have to … don't have to</strong> toʻgʻri — bitta gapda majburiyat "
                       "shkalasining eng tepasi va eng pasti.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Madina will can drive next year.",
                    "Madina will be able to drive next year.",
                    "Madina can drive now.",
                    "Madina could drive when she was eighteen."],
        "correct": "Madina will can drive next year.",
        "explanation": "<p><strong>Madina will can drive next year.</strong> is the mistake — two modals "
                       "cannot stand together.<br><br>"
                       "<em>(<strong>Madina will can drive next year.</strong> xato — ikki modal "
                       "yonma-yon kela olmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Shaxzoda ought to apologise.", "Shaxzoda ought apologise.",
                    "Shaxzoda oughts to apologise.", "Shaxzoda ought to apologising."],
        "correct": "Shaxzoda ought to apologise.",
        "explanation": "<p><strong>Shaxzoda ought to apologise.</strong> is correct — <em>ought</em> is "
                       "the one modal that keeps <em>to</em>, and modals never take <em>-s</em>.<br><br>"
                       "<em>(<strong>Shaxzoda ought to apologise.</strong> toʻgʻri — <em>ought</em> "
                       "<em>to</em> ni saqlaydigan yagona modal, modallar esa <em>-s</em> "
                       "olmaydi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Abdulloh:</strong> Do we have to write the whole essay tonight?</p>"
                "<p><strong>Rozimurod teacher:</strong> ___</p>",
        "choices": ["No, you don't have to, but you'd better start it.",
                    "No, you mustn't, but you'd better start it.",
                    "No, you can't, but you must start it.",
                    "No, you don't must, but you had better to start it."],
        "correct": "No, you don't have to, but you'd better start it.",
        "explanation": "<p><strong>No, you don't have to, but you'd better start it.</strong> is correct "
                       "— no obligation tonight, but a clear warning attached.<br><br>"
                       "<em>(<strong>No, you don't have to, but you'd better start it.</strong> "
                       "toʻgʻri — bugun majburiyat yoʻq, lekin ochiq ogohlantirish bor.)</em></p>",
    },
]


# =====================================================================
# PE-52 — Conjunctions
# =====================================================================

Q_PE52 = [
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>It was late, ___ Behruz went home.</strong></p>",
        "choices": ["so", "because", "but", "although"],
        "correct": "so",
        "explanation": "<p><strong>so</strong> is correct — <em>so</em> introduces the <em>result</em>."
                       "<br><br><em>(<strong>so</strong> toʻgʻri — <em>so</em> <em>natijani</em> "
                       "kiritadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>Behruz went home ___ it was late.</strong></p>",
        "choices": ["because", "so", "but", "or"],
        "correct": "because",
        "explanation": "<p><strong>because</strong> is correct — <em>because</em> introduces the "
                       "<em>reason</em>. <em>So</em> and <em>because</em> point in opposite "
                       "directions.<br><br>"
                       "<em>(<strong>because</strong> toʻgʻri — <em>because</em> <em>sababni</em> "
                       "kiritadi. <em>So</em> va <em>because</em> qarama-qarshi tomonga "
                       "ishora qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>The jacket is cheap ___ warm.</strong></p>",
        "choices": ["but", "so", "because", "or"],
        "correct": "but",
        "explanation": "<p><strong>but</strong> is correct — a contrast between two ideas.<br><br>"
                       "<em>(<strong>but</strong> toʻgʻri — ikki fikr oʻrtasidagi qarama-qarshilik.)</em></p>",
    },
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>Would you like tea ___ coffee, Iroda?</strong></p>",
        "choices": ["or", "and", "so", "but"],
        "correct": "or",
        "explanation": "<p><strong>or</strong> is correct — a choice between two options.<br><br>"
                       "<em>(<strong>or</strong> toʻgʻri — ikki variant orasidagi tanlov.)</em></p>",
    },
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>Charos bought bread ___ milk at the shop.</strong></p>",
        "choices": ["and", "but", "so", "because"],
        "correct": "and",
        "explanation": "<p><strong>and</strong> is correct — simply adding one thing to another."
                       "<br><br><em>(<strong>and</strong> toʻgʻri — shunchaki bir narsani ikkinchisiga "
                       "qoʻshish.)</em></p>",
    },
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>___ it rained, we went to the mountains.</strong></p>",
        "choices": ["Although", "Because", "So", "And"],
        "correct": "Although",
        "explanation": "<p><strong>Although</strong> is correct — a contrast: the rain did not stop "
                       "us.<br><br>"
                       "<em>(<strong>Although</strong> toʻgʻri — qarama-qarshilik: yomgʻir bizni "
                       "toʻxtata olmadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Although Samandar was tired, ___ .</strong></p>",
        "choices": ["he finished his homework", "but he finished his homework",
                    "so he finished his homework", "and but he finished his homework"],
        "correct": "he finished his homework",
        "explanation": "<p><strong>he finished his homework</strong> is correct — English uses "
                       "<em>although</em> <strong>or</strong> <em>but</em>, never both in one "
                       "sentence.<br><br>"
                       "<em>(<strong>he finished his homework</strong> toʻgʻri — ingliz tilida "
                       "<em>although</em> <strong>yoki</strong> <em>but</em> ishlatiladi, bitta gapda "
                       "ikkalasi birga emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>Elbek studies hard, ___ he always gets good marks.</strong></p>",
        "choices": ["so", "because", "although", "or"],
        "correct": "so",
        "explanation": "<p><strong>so</strong> is correct — hard study is the cause, good marks are the "
                       "result.<br><br>"
                       "<em>(<strong>so</strong> toʻgʻri — qattiq oʻqish — sabab, yaxshi baholar — "
                       "natija.)</em></p>",
    },
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>Firdavs was late ___ the bus didn't come.</strong></p>",
        "choices": ["because", "so", "although", "and"],
        "correct": "because",
        "explanation": "<p><strong>because</strong> is correct — the missing bus is the reason.<br><br>"
                       "<em>(<strong>because</strong> toʻgʻri — avtobus kelmagani — sabab.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Where does the comma go?</strong></p>",
        "choices": ["Although it was cold, we walked home.",
                    "Although, it was cold we walked home.",
                    "Although it was cold we, walked home.",
                    "Although it was cold we walked, home."],
        "correct": "Although it was cold, we walked home.",
        "explanation": "<p><strong>Although it was cold, we walked home.</strong> is correct — when the "
                       "<em>although</em> half comes first, a comma separates the two halves.<br><br>"
                       "<em>(<strong>Although it was cold, we walked home.</strong> toʻgʻri — "
                       "<em>although</em> qismi oldin kelsa, ikki qism vergul bilan ajratiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>Hurry up, ___ we'll miss the bus.</strong></p>",
        "choices": ["or", "and", "so", "because"],
        "correct": "or",
        "explanation": "<p><strong>or</strong> is correct — here <em>or</em> warns about the consequence "
                       "of not acting.<br><br>"
                       "<em>(<strong>or</strong> toʻgʻri — bu yerda <em>or</em> harakat qilmaslikning "
                       "oqibati haqida ogohlantiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>Javohir plays football ___ his brother prefers chess.</strong></p>",
        "choices": ["but", "so", "because", "or"],
        "correct": "but",
        "explanation": "<p><strong>but</strong> is correct — two different preferences, set against each "
                       "other.<br><br>"
                       "<em>(<strong>but</strong> toʻgʻri — bir-biriga qarama-qarshi qoʻyilgan ikki xil "
                       "did.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence gives the <em>reason</em>?</strong></p>",
        "choices": ["Madina stayed at home because she was ill.",
                    "Madina was ill, so she stayed at home.",
                    "Madina was ill but she came to school.",
                    "Madina was ill and tired."],
        "correct": "Madina stayed at home because she was ill.",
        "explanation": "<p><strong>Madina stayed at home because she was ill.</strong> is correct — "
                       "<em>because</em> points back to the cause; <em>so</em> points forward to the "
                       "result.<br><br>"
                       "<em>(<strong>Madina stayed at home because she was ill.</strong> toʻgʻri — "
                       "<em>because</em> sababga, <em>so</em> esa natijaga ishora qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>Shaxzoda can sing ___ dance very well.</strong></p>",
        "choices": ["and", "but", "or", "so"],
        "correct": "and",
        "explanation": "<p><strong>and</strong> is correct — two abilities added together.<br><br>"
                       "<em>(<strong>and</strong> toʻgʻri — birga qoʻshilgan ikki qobiliyat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence sounds most like real English?</strong></p>",
        "choices": ["I was tired, so I went home and slept.",
                    "I was tired. I went home. I slept.",
                    "I was tired so because I went home and slept.",
                    "I was tired, but so I went home, and slept."],
        "correct": "I was tired, so I went home and slept.",
        "explanation": "<p><strong>I was tired, so I went home and slept.</strong> is correct — joining "
                       "ideas is what makes writing sound grown-up.<br><br>"
                       "<em>(<strong>I was tired, so I went home and slept.</strong> toʻgʻri — fikrlarni "
                       "bogʻlash yozuvni yetuk qilib koʻrsatadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct conjunction.</p>"
                "<p><strong>Sirojiddin didn't answer, ___ he didn't know the rule.</strong></p>",
        "choices": ["because", "so", "although", "or"],
        "correct": "because",
        "explanation": "<p><strong>because</strong> is correct — not knowing the rule caused the "
                       "silence.<br><br>"
                       "<em>(<strong>because</strong> toʻgʻri — qoidani bilmagani sukutga sabab "
                       "boʻlgan.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["Although Davron was ill, but he came to school.",
                    "Although Davron was ill, he came to school.",
                    "Davron was ill, but he came to school.",
                    "Davron came to school although he was ill."],
        "correct": "Although Davron was ill, but he came to school.",
        "explanation": "<p><strong>Although Davron was ill, but he came to school.</strong> is the "
                       "mistake — <em>although</em> and <em>but</em> do the same job, so one of them must "
                       "go.<br><br>"
                       "<em>(<strong>Although Davron was ill, but he came to school.</strong> xato — "
                       "<em>although</em> va <em>but</em> bir xil vazifani bajaradi, shuning uchun "
                       "bittasi ortiqcha.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Because it was raining, we stayed at home.",
                    "Because it was raining, so we stayed at home.",
                    "It was raining, because we stayed at home.",
                    "Because of it was raining, we stayed at home."],
        "correct": "Because it was raining, we stayed at home.",
        "explanation": "<p><strong>Because it was raining, we stayed at home.</strong> is correct — one "
                       "joiner is enough, and <em>because of</em> would need a noun, not a "
                       "sentence.<br><br>"
                       "<em>(<strong>Because it was raining, we stayed at home.</strong> toʻgʻri — bitta "
                       "bogʻlovchi yetarli, <em>because of</em> esa gap emas, ot talab qiladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Why didn't you finish the exercise, "
                "Marjona?</p>"
                "<p><strong>Marjona:</strong> ___</p>",
        "choices": ["Because I didn't understand the last question.",
                    "So I didn't understand the last question.",
                    "Although I didn't understand the last question.",
                    "But because I didn't understand the last question."],
        "correct": "Because I didn't understand the last question.",
        "explanation": "<p><strong>Because I didn't understand the last question.</strong> is correct — "
                       "a <em>why</em> question is answered with the reason.<br><br>"
                       "<em>(<strong>Because I didn't understand the last question.</strong> toʻgʻri — "
                       "<em>why</em> savoliga sabab bilan javob beriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>every</strong> joiner is correct.</p>",
        "choices": ["Afsona was tired, so she went home, but she still finished her homework, "
                    "because the test is tomorrow.",
                    "Afsona was tired, because she went home, so she still finished her homework, "
                    "but the test is tomorrow.",
                    "Although Afsona was tired, but she went home and so she finished her homework "
                    "because of the test is tomorrow.",
                    "Afsona was tired so because she went home, and but she still finished her "
                    "homework, although the test is tomorrow."],
        "correct": "Afsona was tired, so she went home, but she still finished her homework, "
                   "because the test is tomorrow.",
        "explanation": "<p><strong>so … but … because …</strong> is correct — result, contrast and "
                       "reason, each in its right place and never doubled.<br><br>"
                       "<em>(<strong>so … but … because …</strong> toʻgʻri — natija, qarama-qarshilik va "
                       "sabab, har biri oʻz oʻrnida va hech biri takrorlanmagan.)</em></p>",
    },
]


# =====================================================================
# PE-53 — Zero and First Conditional
# =====================================================================

Q_PE53 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If you heat water to 100°, it ___ .</strong></p>",
        "choices": ["boils", "will boil", "boiled", "would boil"],
        "correct": "boils",
        "explanation": "<p><strong>boils</strong> is correct — the zero conditional: both halves in the "
                       "Present Simple, for something always true.<br><br>"
                       "<em>(<strong>boils</strong> toʻgʻri — nol shart gap: doim toʻgʻri boʻlgan narsa "
                       "uchun ikki qism ham Present Simple da.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If it rains tomorrow, we ___ at home.</strong></p>",
        "choices": ["will stay", "stay", "stayed", "would stay"],
        "correct": "will stay",
        "explanation": "<p><strong>will stay</strong> is correct — the first conditional: a real future "
                       "possibility takes <em>will</em> in the result half.<br><br>"
                       "<em>(<strong>will stay</strong> toʻgʻri — birinchi shart gap: haqiqiy kelasi "
                       "imkoniyat natija qismida <em>will</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Behruz ___ hard, he will pass the exam.</strong></p>",
        "choices": ["studies", "will study", "studied", "would study"],
        "correct": "studies",
        "explanation": "<p><strong>studies</strong> is correct — the golden rule: never <em>will</em> "
                       "after <em>if</em>.<br><br>"
                       "<em>(<strong>studies</strong> toʻgʻri — oltin qoida: <em>if</em> dan keyin "
                       "hech qachon <em>will</em> qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the rule about <em>will</em> after <em>if</em>?</strong></p>",
        "choices": ["Never use it — use the present.",
                    "Always use it.",
                    "Use it only in the zero conditional.",
                    "Use it only with he / she / it."],
        "correct": "Never use it — use the present.",
        "explanation": "<p><strong>Never use it — use the present.</strong> is correct — the same rule "
                       "you met with <em>when</em>, <em>before</em> and <em>as soon as</em> in "
                       "PE-26.<br><br>"
                       "<em>(<strong>Hech qachon ishlatilmaydi — hozirgi zamon qoʻyiladi.</strong> "
                       "toʻgʻri — PE-26 dagi <em>when</em>, <em>before</em>, <em>as soon as</em> bilan "
                       "bir xil qoida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If I drink coffee at night, I ___ .</strong></p>",
        "choices": ["don't sleep", "won't sleep well tomorrow", "didn't sleep", "wouldn't sleep"],
        "correct": "don't sleep",
        "explanation": "<p><strong>don't sleep</strong> is correct — a personal law of nature, always "
                       "true, so the zero conditional.<br><br>"
                       "<em>(<strong>don't sleep</strong> toʻgʻri — shaxsiy “tabiat qonuni”, doim "
                       "toʻgʻri, shuning uchun nol shart gap.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In the zero conditional, <em>if</em> means almost the same as ___ "
                ".</strong></p>",
        "choices": ["when", "although", "because", "unless"],
        "correct": "when",
        "explanation": "<p><strong>when</strong> is correct — <em>If you heat ice, it melts</em> = "
                       "<em>When you heat ice, it melts</em>.<br><br>"
                       "<em>(<strong>when</strong> toʻgʻri — <em>If you heat ice, it melts</em> = "
                       "<em>When you heat ice, it melts</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda will call you if she ___ time.</strong></p>",
        "choices": ["has", "will have", "had", "would have"],
        "correct": "has",
        "explanation": "<p><strong>has</strong> is correct — present after <em>if</em>, even when the "
                       "meaning is future.<br><br>"
                       "<em>(<strong>has</strong> toʻgʻri — maʼnosi kelasi zamon boʻlsa ham, <em>if</em> "
                       "dan keyin hozirgi zamon keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ you hurry, you will miss the bus.</strong></p>",
        "choices": ["Unless", "If", "Although", "So"],
        "correct": "Unless",
        "explanation": "<p><strong>Unless</strong> is correct — <em>unless</em> = <em>if … not</em>, so "
                       "it already contains the negative.<br><br>"
                       "<em>(<strong>Unless</strong> toʻgʻri — <em>unless</em> = <em>if … not</em>, "
                       "yaʼni u oʻzida inkorni saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which means the same as “If Charos doesn't hurry, she'll be "
                "late”?</strong></p>",
        "choices": ["Unless Charos hurries, she'll be late.",
                    "Unless Charos doesn't hurry, she'll be late.",
                    "If Charos hurries, she'll be late.",
                    "Although Charos hurries, she'll be late."],
        "correct": "Unless Charos hurries, she'll be late.",
        "explanation": "<p><strong>Unless Charos hurries, she'll be late.</strong> is correct — never add "
                       "a second negative after <em>unless</em>.<br><br>"
                       "<em>(<strong>Unless Charos hurries, she'll be late.</strong> toʻgʻri — "
                       "<em>unless</em> dan keyin ikkinchi inkor qoʻshilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar will help us as soon as he ___ .</strong></p>",
        "choices": ["arrives", "will arrive", "arrived", "would arrive"],
        "correct": "arrives",
        "explanation": "<p><strong>arrives</strong> is correct — <em>as soon as, when, before, after, "
                       "until</em> follow the same no-<em>will</em> rule as <em>if</em>.<br><br>"
                       "<em>(<strong>arrives</strong> toʻgʻri — <em>as soon as, when, before, after, "
                       "until</em> ham <em>if</em> kabi <em>will</em> ni qabul qilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Elbek ___ me tomorrow, I'll explain everything.</strong></p>",
        "choices": ["asks", "will ask", "asked", "would ask"],
        "correct": "asks",
        "explanation": "<p><strong>asks</strong> is correct — a real possibility for tomorrow, with the "
                       "present after <em>if</em>.<br><br>"
                       "<em>(<strong>asks</strong> toʻgʻri — ertaga uchun haqiqiy imkoniyat, <em>if</em> "
                       "dan keyin hozirgi zamon.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If you ___ the red button, the machine stops.</strong></p>",
        "choices": ["press", "will press", "pressed", "would press"],
        "correct": "press",
        "explanation": "<p><strong>press</strong> is correct — a machine always behaves the same way, so "
                       "the zero conditional.<br><br>"
                       "<em>(<strong>press</strong> toʻgʻri — mashina doim bir xil ishlaydi, shuning "
                       "uchun nol shart gap.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the difference between the zero and the first "
                "conditional?</strong></p>",
        "choices": ["Zero = always true · First = one real future possibility",
                    "Zero = future · First = always true",
                    "Zero = imaginary · First = real",
                    "There is no difference."],
        "correct": "Zero = always true · First = one real future possibility",
        "explanation": "<p><strong>Zero = always true · First = one real future possibility</strong> is "
                       "correct — that is why the zero uses the present in both halves.<br><br>"
                       "<em>(<strong>Nol = doim toʻgʻri · Birinchi = bitta haqiqiy kelasi "
                       "imkoniyat</strong> toʻgʻri — shuning uchun nol shart gapda ikki qism ham hozirgi "
                       "zamonda.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Firdavs finishes early, he ___ football with us.</strong></p>",
        "choices": ["will play", "plays", "played", "would play"],
        "correct": "will play",
        "explanation": "<p><strong>will play</strong> is correct — the result of a real future "
                       "condition.<br><br>"
                       "<em>(<strong>will play</strong> toʻgʻri — haqiqiy kelasi shartning "
                       "natijasi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Javohir ___ tomorrow, tell him Rozimurod teacher is in the "
                "staff room.</strong></p>",
        "choices": ["comes", "will come", "came", "would come"],
        "correct": "comes",
        "explanation": "<p><strong>comes</strong> is correct — the result half can also be an "
                       "instruction, but <em>if</em> still takes the present.<br><br>"
                       "<em>(<strong>comes</strong> toʻgʻri — natija qismi buyruq ham boʻlishi mumkin, "
                       "lekin <em>if</em> baribir hozirgi zamon oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct punctuation.</p>",
        "choices": ["If it snows, we won't go.", "If it snows we, won't go.",
                    "If, it snows we won't go.", "If it snows we won't, go."],
        "correct": "If it snows, we won't go.",
        "explanation": "<p><strong>If it snows, we won't go.</strong> is correct — when the <em>if</em> "
                       "half comes first, put a comma between the halves.<br><br>"
                       "<em>(<strong>If it snows, we won't go.</strong> toʻgʻri — <em>if</em> qismi "
                       "oldin kelsa, ikki qism orasiga vergul qoʻyiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["If Madina will come, we will start.",
                    "If Madina comes, we will start.",
                    "We will start if Madina comes.",
                    "If Madina comes, we start at once."],
        "correct": "If Madina will come, we will start.",
        "explanation": "<p><strong>If Madina will come, we will start.</strong> is the mistake — "
                       "<em>will</em> can never follow <em>if</em>.<br><br>"
                       "<em>(<strong>If Madina will come, we will start.</strong> xato — <em>will</em> "
                       "hech qachon <em>if</em> dan keyin kelmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["Unless Shaxzoda studies, she won't pass.",
                    "Unless Shaxzoda doesn't study, she won't pass.",
                    "Unless Shaxzoda will study, she won't pass.",
                    "Unless Shaxzoda studies, she doesn't will pass."],
        "correct": "Unless Shaxzoda studies, she won't pass.",
        "explanation": "<p><strong>Unless Shaxzoda studies, she won't pass.</strong> is correct — "
                       "<em>unless</em> carries the negative by itself, and takes the present.<br><br>"
                       "<em>(<strong>Unless Shaxzoda studies, she won't pass.</strong> toʻgʻri — "
                       "<em>unless</em> inkorni oʻzi tashiydi va hozirgi zamon oladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Abdulloh:</strong> What will you do if it rains on Saturday?</p>"
                "<p><strong>Sirojiddin:</strong> ___</p>",
        "choices": ["If it rains, we'll play indoors.", "If it will rain, we'll play indoors.",
                    "If it rains, we play indoors tomorrow certainly.",
                    "If it rained, we'll play indoors."],
        "correct": "If it rains, we'll play indoors.",
        "explanation": "<p><strong>If it rains, we'll play indoors.</strong> is correct — present after "
                       "<em>if</em>, <em>will</em> in the result.<br><br>"
                       "<em>(<strong>If it rains, we'll play indoors.</strong> toʻgʻri — <em>if</em> dan "
                       "keyin hozirgi zamon, natijada esa <em>will</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>both</strong> conditionals are correct.</p>",
        "choices": ["If you mix blue and yellow, you get green; and if we have paint tomorrow, "
                    "we'll try it.",
                    "If you will mix blue and yellow, you get green; and if we will have paint "
                    "tomorrow, we'll try it.",
                    "If you mix blue and yellow, you will get green always; and if we have paint "
                    "tomorrow, we try it.",
                    "If you mixed blue and yellow, you would get green; and if we had paint "
                    "tomorrow, we'll try it."],
        "correct": "If you mix blue and yellow, you get green; and if we have paint tomorrow, "
                   "we'll try it.",
        "explanation": "<p><strong>you get green … we'll try it</strong> is correct — an always-true fact "
                       "in the zero conditional, a real plan in the first.<br><br>"
                       "<em>(<strong>you get green … we'll try it</strong> toʻgʻri — doim toʻgʻri fakt "
                       "nol shart gapda, haqiqiy reja esa birinchisida.)</em></p>",
    },
]


# =====================================================================
# PE-54 — Second Conditional
# =====================================================================

Q_PE54 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If I ___ a million dollars, I would travel the world.</strong></p>",
        "choices": ["had", "have", "will have", "would have"],
        "correct": "had",
        "explanation": "<p><strong>had</strong> is correct — the second conditional is "
                       "<em>If + past simple, would + base verb</em>.<br><br>"
                       "<em>(<strong>had</strong> toʻgʻri — ikkinchi shart gap "
                       "<em>If + past simple, would + asosiy feʼl</em> shaklida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Behruz knew her number, he ___ her.</strong></p>",
        "choices": ["would call", "will call", "calls", "called"],
        "correct": "would call",
        "explanation": "<p><strong>would call</strong> is correct — the result half of an imaginary "
                       "present.<br><br>"
                       "<em>(<strong>would call</strong> toʻgʻri — xayoliy hozirgi zamonning natija "
                       "qismi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Why does the second conditional use a past form?</strong></p>",
        "choices": ["The past form is a signal that it is not real.",
                    "Because the action happened yesterday.",
                    "Because English has no present tense here.",
                    "Because it is about the future."],
        "correct": "The past form is a signal that it is not real.",
        "explanation": "<p><strong>The past form is a signal that it is not real.</strong> is correct — "
                       "the time is now, but the verb steps back to show it is imaginary.<br><br>"
                       "<em>(<strong>Oʻtgan zamon shakli — bu haqiqiy emasligining belgisi.</strong> "
                       "toʻgʻri — vaqt hozirgi, lekin feʼl xayoliy ekanini koʻrsatish uchun orqaga "
                       "chekinadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If I ___ you, I would apologise to Rozimurod teacher.</strong></p>",
        "choices": ["were", "am", "will be", "would be"],
        "correct": "were",
        "explanation": "<p><strong>were</strong> is correct — <em>If I were you</em> is the fixed advice "
                       "phrase, and it uses <em>were</em> for every person.<br><br>"
                       "<em>(<strong>were</strong> toʻgʻri — <em>If I were you</em> qatʼiy maslahat "
                       "iborasi va u har bir shaxs uchun <em>were</em> oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “If I had time, I would help you” tell us?</strong></p>",
        "choices": ["I don't have time, so I can't help.",
                    "I have time and I will help.",
                    "I had time yesterday.",
                    "I will have time tomorrow."],
        "correct": "I don't have time, so I can't help.",
        "explanation": "<p><strong>I don't have time, so I can't help.</strong> is correct — every second "
                       "conditional states the opposite of reality.<br><br>"
                       "<em>(<strong>Vaqtim yoʻq, shuning uchun yordam bera olmayman.</strong> toʻgʻri — "
                       "har bir ikkinchi shart gap haqiqatning aksini aytadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Iroda ___ in Seoul, she would speak Korean every day.</strong></p>",
        "choices": ["lived", "lives", "will live", "would live"],
        "correct": "lived",
        "explanation": "<p><strong>lived</strong> is correct — she does not live there; this is "
                       "imagination.<br><br>"
                       "<em>(<strong>lived</strong> toʻgʻri — u u yerda yashamaydi; bu "
                       "xayol.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What would you do if you ___ a wallet in the street?</strong></p>",
        "choices": ["found", "find", "will find", "would find"],
        "correct": "found",
        "explanation": "<p><strong>found</strong> is correct — an imaginary situation, so the past form "
                       "after <em>if</em>.<br><br>"
                       "<em>(<strong>found</strong> toʻgʻri — xayoliy vaziyat, shuning uchun <em>if</em> "
                       "dan keyin oʻtgan zamon shakli.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Charos ___ harder, she would get better marks.</strong></p>",
        "choices": ["studied", "studies", "will study", "would study"],
        "correct": "studied",
        "explanation": "<p><strong>studied</strong> is correct — never put <em>would</em> in the "
                       "<em>if</em> half.<br><br>"
                       "<em>(<strong>studied</strong> toʻgʻri — <em>if</em> qismiga hech qachon "
                       "<em>would</em> qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Compare: “If it rains, I'll stay home” and “If it rained, I'd stay "
                "home.” What is the difference?</strong></p>",
        "choices": ["The first is likely; the second is unlikely or imaginary.",
                    "The first is imaginary; the second is likely.",
                    "The first is past; the second is future.",
                    "There is no difference."],
        "correct": "The first is likely; the second is unlikely or imaginary.",
        "explanation": "<p><strong>The first is likely; the second is unlikely or imaginary.</strong> is "
                       "correct — the past form moves the sentence away from reality.<br><br>"
                       "<em>(<strong>Birinchisi ehtimolli; ikkinchisi ehtimoldan yiroq yoki "
                       "xayoliy.</strong> toʻgʻri — oʻtgan zamon shakli gapni haqiqatdan "
                       "uzoqlashtiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Samandar ___ a car, he wouldn't take the bus.</strong></p>",
        "choices": ["had", "has", "will have", "would have"],
        "correct": "had",
        "explanation": "<p><strong>had</strong> is correct — he has no car, so the whole sentence is "
                       "imaginary.<br><br>"
                       "<em>(<strong>had</strong> toʻgʻri — uning mashinasi yoʻq, shuning uchun butun gap "
                       "xayoliy.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If I were Elbek, I ___ the truth.</strong></p>",
        "choices": ["would tell", "will tell", "told", "tell"],
        "correct": "would tell",
        "explanation": "<p><strong>would tell</strong> is correct — advice given through an imaginary "
                       "situation.<br><br>"
                       "<em>(<strong>would tell</strong> toʻgʻri — xayoliy vaziyat orqali berilgan "
                       "maslahat.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs ___ buy that bicycle if it were cheaper.</strong></p>",
        "choices": ["would", "will", "did", "does"],
        "correct": "would",
        "explanation": "<p><strong>would</strong> is correct — the result half, whichever order the two "
                       "halves come in.<br><br>"
                       "<em>(<strong>would</strong> toʻgʻri — ikki qism qanday tartibda kelishidan qatʼi "
                       "nazar, bu natija qismi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence gives advice?</strong></p>",
        "choices": ["If I were you, I'd start revising now.",
                    "If I am you, I will start revising now.",
                    "If I would be you, I start revising now.",
                    "If I were you, I will start revising now."],
        "correct": "If I were you, I'd start revising now.",
        "explanation": "<p><strong>If I were you, I'd start revising now.</strong> is correct — the most "
                       "useful advice phrase in English, and <em>will</em> never appears in it.<br><br>"
                       "<em>(<strong>If I were you, I'd start revising now.</strong> toʻgʻri — ingliz "
                       "tilidagi eng foydali maslahat iborasi, unda <em>will</em> hech qachon "
                       "kelmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Javohir ___ more free time, he would learn the piano.</strong></p>",
        "choices": ["had", "would have", "will have", "has"],
        "correct": "had",
        "explanation": "<p><strong>had</strong> is correct — past form after <em>if</em>, <em>would</em> "
                       "in the other half.<br><br>"
                       "<em>(<strong>had</strong> toʻgʻri — <em>if</em> dan keyin oʻtgan zamon shakli, "
                       "boshqa qismda esa <em>would</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Madina wouldn't be so tired if she ___ earlier.</strong></p>",
        "choices": ["went to bed", "goes to bed", "will go to bed", "would go to bed"],
        "correct": "went to bed",
        "explanation": "<p><strong>went to bed</strong> is correct — the <em>if</em> half keeps the past "
                       "form even when it comes second.<br><br>"
                       "<em>(<strong>went to bed</strong> toʻgʻri — <em>if</em> qismi ikkinchi oʻrinda "
                       "kelsa ham oʻtgan zamon shaklini saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the short form of <em>would</em> in “I would go”?</strong></p>",
        "choices": ["I'd go", "I'll go", "I've go", "I's go"],
        "correct": "I'd go",
        "explanation": "<p><strong>I'd go</strong> is correct — and remember from PE-50 that <em>'d</em> "
                       "before a base verb is <em>would</em>, not <em>had</em>.<br><br>"
                       "<em>(<strong>I'd go</strong> toʻgʻri — PE-50 dan eslang: asosiy feʼl oldidagi "
                       "<em>'d</em> — <em>would</em>, <em>had</em> emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["If Sirojiddin would have a bike, he would cycle to school.",
                    "If Sirojiddin had a bike, he would cycle to school.",
                    "Sirojiddin would cycle to school if he had a bike.",
                    "If Sirojiddin had a bike, he'd cycle to school."],
        "correct": "If Sirojiddin would have a bike, he would cycle to school.",
        "explanation": "<p><strong>If Sirojiddin would have a bike …</strong> is the mistake — "
                       "<em>would</em> belongs only in the result half, never after <em>if</em>.<br><br>"
                       "<em>(<strong>If Sirojiddin would have a bike …</strong> xato — <em>would</em> "
                       "faqat natija qismida boʻladi, <em>if</em> dan keyin hech qachon.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["If I were rich, I would build a school.",
                    "If I was rich, I will build a school.",
                    "If I am rich, I would build a school.",
                    "If I would be rich, I built a school."],
        "correct": "If I were rich, I would build a school.",
        "explanation": "<p><strong>If I were rich, I would build a school.</strong> is correct — "
                       "<em>were</em> for every person in this pattern, and <em>would</em> in the "
                       "result.<br><br>"
                       "<em>(<strong>If I were rich, I would build a school.</strong> toʻgʻri — bu "
                       "qolipda har bir shaxs uchun <em>were</em>, natijada esa <em>would</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Marjona:</strong> I don't know what to do about the competition.</p>"
                "<p><strong>Rozimurod teacher:</strong> ___</p>",
        "choices": ["If I were you, I would enter it.", "If I was you, I will enter it.",
                    "If I would be you, I enter it.", "If I am you, I would enter it."],
        "correct": "If I were you, I would enter it.",
        "explanation": "<p><strong>If I were you, I would enter it.</strong> is correct — imagining "
                       "yourself in the other person's place is how English gives careful advice."
                       "<br><br><em>(<strong>If I were you, I would enter it.</strong> toʻgʻri — oʻzini "
                       "boshqaning oʻrniga qoʻyib tasavvur qilish — ingliz tilida ehtiyotkor maslahat "
                       "berish usuli.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>everything</strong> is correct.</p>",
        "choices": ["If Afsona had more time, she'd read more, and if she read more, "
                    "she'd write better essays.",
                    "If Afsona would have more time, she'd read more, and if she would read more, "
                    "she'd write better essays.",
                    "If Afsona has more time, she'd read more, and if she reads more, "
                    "she will write better essays.",
                    "If Afsona had more time, she will read more, and if she read more, "
                    "she wrote better essays."],
        "correct": "If Afsona had more time, she'd read more, and if she read more, "
                   "she'd write better essays.",
        "explanation": "<p><strong>had … she'd read … read … she'd write</strong> is correct — two "
                       "chained second conditionals, with <em>would</em> only ever in the result "
                       "halves.<br><br>"
                       "<em>(<strong>had … she'd read … read … she'd write</strong> toʻgʻri — zanjir "
                       "boʻlib kelgan ikki ikkinchi shart gap, <em>would</em> esa faqat natija "
                       "qismlarida.)</em></p>",
    },
]


# =====================================================================
# PE-55 — Third Conditional
# =====================================================================

Q_PE55 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If I ___ harder, I would have passed.</strong></p>",
        "choices": ["had studied", "studied", "would study", "have studied"],
        "correct": "had studied",
        "explanation": "<p><strong>had studied</strong> is correct — the third conditional is "
                       "<em>If + had + V3, would have + V3</em>.<br><br>"
                       "<em>(<strong>had studied</strong> toʻgʻri — uchinchi shart gap "
                       "<em>If + had + V3, would have + V3</em> shaklida.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Behruz had left earlier, he ___ the bus.</strong></p>",
        "choices": ["would have caught", "would catch", "will catch", "had caught"],
        "correct": "would have caught",
        "explanation": "<p><strong>would have caught</strong> is correct — the result half of an "
                       "imaginary past.<br><br>"
                       "<em>(<strong>would have caught</strong> toʻgʻri — xayoliy oʻtmishning natija "
                       "qismi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What does “If I had left earlier, I would have caught the bus” tell us "
                "about reality?</strong></p>",
        "choices": ["I didn't leave early, and I didn't catch the bus.",
                    "I left early and caught the bus.",
                    "I left early but missed the bus.",
                    "I will leave early tomorrow."],
        "correct": "I didn't leave early, and I didn't catch the bus.",
        "explanation": "<p><strong>I didn't leave early, and I didn't catch the bus.</strong> is correct "
                       "— every third conditional states the opposite of what really happened, in "
                       "both halves.<br><br>"
                       "<em>(<strong>Erta chiqmadim va avtobusga ulgurmadim.</strong> toʻgʻri — har bir "
                       "uchinchi shart gap ikki qismida ham haqiqatning aksini aytadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Iroda ___ me, I wouldn't have finished the project.</strong></p>",
        "choices": ["hadn't helped", "didn't help", "wouldn't help", "hasn't helped"],
        "correct": "hadn't helped",
        "explanation": "<p><strong>hadn't helped</strong> is correct — and the real meaning is the "
                       "opposite: she did help, and he did finish.<br><br>"
                       "<em>(<strong>hadn't helped</strong> toʻgʻri — haqiqiy maʼnosi esa aksincha: u "
                       "yordam berdi va u tugatdi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which time does the third conditional talk about?</strong></p>",
        "choices": ["An imaginary past that cannot be changed.",
                    "A real future possibility.",
                    "Something always true.",
                    "An imaginary present."],
        "correct": "An imaginary past that cannot be changed.",
        "explanation": "<p><strong>An imaginary past that cannot be changed.</strong> is correct — it is "
                       "the language of regret and relief.<br><br>"
                       "<em>(<strong>Oʻzgartirib boʻlmaydigan xayoliy oʻtmish.</strong> toʻgʻri — bu "
                       "afsus va yengil nafas tilidir.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Charos had known about the test, she ___ .</strong></p>",
        "choices": ["would have revised", "would revise", "will revise", "had revised"],
        "correct": "would have revised",
        "explanation": "<p><strong>would have revised</strong> is correct — <em>would have + V3</em> in "
                       "the result.<br><br>"
                       "<em>(<strong>would have revised</strong> toʻgʻri — natijada "
                       "<em>would have + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Samandar ___ won if he hadn't fallen.</strong></p>",
        "choices": ["would have", "would", "will have", "had"],
        "correct": "would have",
        "explanation": "<p><strong>would have</strong> is correct — the result half keeps its form "
                       "whichever order the halves come in.<br><br>"
                       "<em>(<strong>would have</strong> toʻgʻri — qismlar qanday tartibda kelishidan "
                       "qatʼi nazar, natija qismi oʻz shaklini saqlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Elbek had asked, we ___ him.</strong></p>",
        "choices": ["could have helped", "can help", "could help", "had helped"],
        "correct": "could have helped",
        "explanation": "<p><strong>could have helped</strong> is correct — <em>could have</em> and "
                       "<em>might have</em> can replace <em>would have</em> in the result, to soften "
                       "it.<br><br>"
                       "<em>(<strong>could have helped</strong> toʻgʻri — natijada <em>would have</em> "
                       "oʻrniga uni yumshatish uchun <em>could have</em> yoki <em>might have</em> kelishi "
                       "mumkin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Firdavs had taken the earlier train, he ___ arrived on time.</strong></p>",
        "choices": ["might have", "might", "may", "will have"],
        "correct": "might have",
        "explanation": "<p><strong>might have</strong> is correct — a less certain imaginary "
                       "result.<br><br>"
                       "<em>(<strong>might have</strong> toʻgʻri — ishonchi kamroq boʻlgan xayoliy "
                       "natija.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Javohir wouldn't have been late if he ___ his alarm.</strong></p>",
        "choices": ["had set", "set", "would set", "has set"],
        "correct": "had set",
        "explanation": "<p><strong>had set</strong> is correct — <em>had + V3</em> in the <em>if</em> "
                       "half, always.<br><br>"
                       "<em>(<strong>had set</strong> toʻgʻri — <em>if</em> qismida doim "
                       "<em>had + V3</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Which sentence expresses <em>relief</em>?</strong></p>",
        "choices": ["If Madina hadn't warned me, I would have made a terrible mistake.",
                    "If Madina had warned me, I wouldn't have made a mistake.",
                    "If Madina warns me, I won't make a mistake.",
                    "If Madina warned me, I wouldn't make a mistake."],
        "correct": "If Madina hadn't warned me, I would have made a terrible mistake.",
        "explanation": "<p><strong>If Madina hadn't warned me …</strong> is correct — the real facts are "
                       "happy ones: she did warn me, and I did not make the mistake.<br><br>"
                       "<em>(<strong>If Madina hadn't warned me …</strong> toʻgʻri — haqiqiy faktlar "
                       "quvonchli: u ogohlantirdi va men xato qilmadim.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Shaxzoda hadn't missed the lesson, she ___ the rule.</strong></p>",
        "choices": ["would have understood", "would understand", "understood", "will understand"],
        "correct": "would have understood",
        "explanation": "<p><strong>would have understood</strong> is correct — a past that did not "
                       "happen.<br><br>"
                       "<em>(<strong>would have understood</strong> toʻgʻri — sodir boʻlmagan "
                       "oʻtmish.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>How do the three conditionals line up?</strong></p>",
        "choices": ["First = real future · Second = imaginary present · Third = imaginary past",
                    "First = imaginary past · Second = real future · Third = imaginary present",
                    "All three are about the future.",
                    "First = past · Second = present · Third = future"],
        "correct": "First = real future · Second = imaginary present · Third = imaginary past",
        "explanation": "<p><strong>First = real future · Second = imaginary present · Third = imaginary "
                       "past</strong> is correct — each step back in the verb form takes you one step "
                       "further from reality.<br><br>"
                       "<em>(<strong>Birinchi = haqiqiy kelajak · Ikkinchi = xayoliy hozir · Uchinchi = "
                       "xayoliy oʻtmish</strong> toʻgʻri — feʼl shaklidagi har bir orqaga qadam sizni "
                       "haqiqatdan bir pogʻona uzoqlashtiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>If Abdulloh ___ the answer, he would have raised his hand.</strong></p>",
        "choices": ["had known", "knew", "would know", "has known"],
        "correct": "had known",
        "explanation": "<p><strong>had known</strong> is correct — he did not know, so his hand stayed "
                       "down.<br><br>"
                       "<em>(<strong>had known</strong> toʻgʻri — u bilmagan, shuning uchun qoʻlini "
                       "koʻtarmagan.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>What is the short form of “I would have gone”?</strong></p>",
        "choices": ["I'd have gone", "I'll have gone", "I've gone", "I'd gone"],
        "correct": "I'd have gone",
        "explanation": "<p><strong>I'd have gone</strong> is correct — <em>'d</em> here is <em>would</em>, "
                       "and <em>have</em> stays. In speech it often sounds like <em>I'd've "
                       "gone</em>.<br><br>"
                       "<em>(<strong>I'd have gone</strong> toʻgʻri — bu yerda <em>'d</em> — "
                       "<em>would</em>, <em>have</em> esa saqlanadi. Nutqda koʻpincha <em>I'd've "
                       "gone</em> deb eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>If Sirojiddin ___ the map, we ___ lost.</strong></p>",
        "choices": ["had brought … wouldn't have got", "brought … wouldn't get",
                    "had brought … wouldn't get", "would bring … hadn't got"],
        "correct": "had brought … wouldn't have got",
        "explanation": "<p><strong>had brought … wouldn't have got</strong> is correct — both halves stay "
                       "inside the third conditional.<br><br>"
                       "<em>(<strong>had brought … wouldn't have got</strong> toʻgʻri — ikki qism ham "
                       "uchinchi shart gap ichida qoladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence <strong>has a mistake</strong>?</p>",
        "choices": ["If Davron would have studied, he would have passed.",
                    "If Davron had studied, he would have passed.",
                    "Davron would have passed if he had studied.",
                    "If Davron had studied, he'd have passed."],
        "correct": "If Davron would have studied, he would have passed.",
        "explanation": "<p><strong>If Davron would have studied …</strong> is the mistake — "
                       "<em>would</em> never appears after <em>if</em>, in any conditional.<br><br>"
                       "<em>(<strong>If Davron would have studied …</strong> xato — hech bir shart gapda "
                       "<em>would</em> <em>if</em> dan keyin kelmaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is <strong>correct</strong>?</p>",
        "choices": ["If Marjona hadn't been ill, she would have come.",
                    "If Marjona wasn't ill, she would have came.",
                    "If Marjona hadn't been ill, she would have came.",
                    "If Marjona hadn't be ill, she would has come."],
        "correct": "If Marjona hadn't been ill, she would have come.",
        "explanation": "<p><strong>If Marjona hadn't been ill, she would have come.</strong> is correct — "
                       "third forms on both sides: <em>been</em> and <em>come</em>.<br><br>"
                       "<em>(<strong>If Marjona hadn't been ill, she would have come.</strong> toʻgʻri — "
                       "ikki tomonda ham uchinchi shakl: <em>been</em> va <em>come</em>.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> You did well, but you lost two marks on "
                "question ten.</p>"
                "<p><strong>Afsona:</strong> ___</p>",
        "choices": ["If I'd read the question more carefully, I wouldn't have made that mistake.",
                    "If I would read the question more carefully, I wouldn't make that mistake.",
                    "If I read the question more carefully, I wouldn't have made that mistake.",
                    "If I'd read the question more carefully, I wouldn't made that mistake."],
        "correct": "If I'd read the question more carefully, I wouldn't have made that mistake.",
        "explanation": "<p><strong>If I'd read … I wouldn't have made …</strong> is correct — regret "
                       "about a past that cannot be changed.<br><br>"
                       "<em>(<strong>If I'd read … I wouldn't have made …</strong> toʻgʻri — "
                       "oʻzgartirib boʻlmaydigan oʻtmish haqidagi afsus.)</em></p>",
    },
    {
        "text": "<p>Choose the option where <strong>all three</strong> conditionals are correct.</p>",
        "choices": ["If it rains, we'll stay in; if I had a car, I'd drive you; "
                    "and if I had known, I would have told you.",
                    "If it will rain, we'll stay in; if I would have a car, I'd drive you; "
                    "and if I knew, I would have told you.",
                    "If it rains, we stay in always; if I have a car, I would drive you; "
                    "and if I had known, I would tell you.",
                    "If it rained, we'll stay in; if I had a car, I will drive you; "
                    "and if I would have known, I'd told you."],
        "correct": "If it rains, we'll stay in; if I had a car, I'd drive you; "
                   "and if I had known, I would have told you.",
        "explanation": "<p><strong>rains → 'll stay · had → 'd drive · had known → would have told</strong> "
                       "is correct — the whole system in one line, with <em>will</em> and <em>would</em> "
                       "always kept out of the <em>if</em> half.<br><br>"
                       "<em>(<strong>rains → 'll stay · had → 'd drive · had known → would have "
                       "told</strong> toʻgʻri — bitta qatorda butun tizim, <em>will</em> va "
                       "<em>would</em> esa doim <em>if</em> qismidan tashqarida.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-51 Practice: Modal Verbs: The Full Strength Scale",
        "tutorial":    "PE-51:",
        "description": "PE-51 darsiga 20 savol: majburiyat, ishonch va qobiliyat shkalalari, har bir "
                       "modalning kuchi, ularning oʻtgan va kelasi zamondagi shakllari hamda toʻrt "
                       "umumiy qoida. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE51,
    },
    {
        "title":       "PE-52 Practice: Conjunctions: and, but, or, so, because",
        "tutorial":    "PE-52:",
        "description": "PE-52 darsiga 20 savol: and, but, or, so, because va although, so bilan "
                       "because ning qarama-qarshi yoʻnalishi, although dan keyin but "
                       "qoʻyilmasligi va vergul oʻrni. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE52,
    },
    {
        "title":       "PE-53 Practice: Zero and First Conditional",
        "tutorial":    "PE-53:",
        "description": "PE-53 darsiga 20 savol: doim toʻgʻri boʻlgan nol shart gap, haqiqiy kelasi "
                       "imkoniyat uchun birinchi shart gap, if dan keyin will ishlatilmasligi va "
                       "unless. Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE53,
    },
    {
        "title":       "PE-54 Practice: Second Conditional: The Imaginary Present",
        "tutorial":    "PE-54:",
        "description": "PE-54 darsiga 20 savol: If + past simple, would + asosiy feʼl, oʻtgan zamon "
                       "shakli nega xayoliylik belgisi ekani va If I were you iborasi. Javoblar "
                       "ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE54,
    },
    {
        "title":       "PE-55 Practice: Third Conditional: Regretting the Past",
        "tutorial":    "PE-55:",
        "description": "PE-55 darsiga 20 savol: If + had + V3, would have + V3, har bir gap ortidagi "
                       "haqiqiy maʼno, could have / might have hamda uchala shart gapning tizimi. "
                       "Javoblar ingliz va oʻzbek tilida izohlangan.",
        "questions":   Q_PE55,
    },
]
