# -*- coding: utf-8 -*-
"""Prime English practices — PE-86 … PE-90 (Block G: advanced and stylish English).

Written with STYLE_GUIDE_PE_PRACTICE.md (section 7: the pupils' names + Rozimurod teacher).
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pe_86_90.py --master=prime --expect-questions=20
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
# PE-86 — Participle Clauses
# =====================================================================
Q_PE86 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ home, Madina met Rozimurod teacher.</strong> "
                "(= While she was walking home)</p>",
        "choices": ["Walking", "Walked", "Walk", "To walk"],
        "correct": "Walking",
        "explanation": "<p><strong>Walking</strong> is correct. When both halves are about the same "
                       "person and that person is doing the action, drop the conjunction and the "
                       "subject and use the <em>-ing</em> form.<br><br>"
                       "<em>(Ikkala qism ham bir odam haqida boʻlsa va u harakatni bajarayotgan boʻlsa, "
                       "bogʻlovchi va ega tushiriladi, feʼl esa <em>-ing</em> shaklga oʻtadi — "
                       "oʻzbekchadagi <em>-ib / -ayotib</em> kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ tired, Behruz went to bed early.</strong> (= Because he was tired)</p>",
        "choices": ["Been", "Being", "Be", "To be"],
        "correct": "Being",
        "explanation": "<p><strong>Being</strong> is correct. An <em>-ing</em> clause can carry the "
                       "meaning \"because\": <em>Being ill, he stayed at home.</em><br><br>"
                       "<em>(<em>-ing</em> oborot \"chunki\" maʼnosini ham bera oladi: <em>Being ill, he "
                       "stayed at home</em> — \"Kasal boʻlgani uchun uyda qoldi\".)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ in 1890, the house is still beautiful.</strong> (build)</p>",
        "choices": ["Building", "Build", "Built", "Builds"],
        "correct": "Built",
        "explanation": "<p><strong>Built</strong> is correct. The house does not build — it "
                       "<em>receives</em> the action, so we need the passive form, the V3.<br><br>"
                       "<em>(Uy qurmaydi — u harakatni <strong>qabul qiladi</strong>, shuning uchun "
                       "majhul shakl, yaʼni V3 kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ finished her homework, Charos watched TV.</strong></p>",
        "choices": ["Have", "Has", "Had", "Having"],
        "correct": "Having",
        "explanation": "<p><strong>Having</strong> is correct. <em>Having + V3</em> shows that the first "
                       "action finished before the second — it replaces the Past Perfect (PE-38) in this "
                       "compact style.<br><br>"
                       "<em>(<em>Having + V3</em> birinchi ish ikkinchisidan oldin tugaganini "
                       "koʻrsatadi — bu qisqa uslubda Past Perfect oʻrnini bosadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ the alarm, Jasur jumped out of bed.</strong> (hear)</p>",
        "choices": ["Hearing", "Heard", "Hear", "To hear"],
        "correct": "Hearing",
        "explanation": "<p><strong>Hearing</strong> is correct. Jasur is the one who hears, so the "
                       "active <em>-ing</em> form is needed.<br><br>"
                       "<em>(Eshitayotgan — Jasurning oʻzi, shuning uchun aniq nisbatdagi "
                       "<em>-ing</em> shakli kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ in Bukhara, the carpet is very valuable.</strong> (make)</p>",
        "choices": ["Making", "Make", "Made", "Makes"],
        "correct": "Made",
        "explanation": "<p><strong>Made</strong> is correct. The carpet does not make anything — "
                       "somebody made it, so the V3 (passive) form is right.<br><br>"
                       "<em>(Gilam hech narsa yasamaydi — uni kimdir yasagan, shuning uchun V3 "
                       "(majhul) shakl toʻgʻri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Having ___ breakfast, Sherbek left the house.</strong> (eat)</p>",
        "choices": ["ate", "eat", "eating", "eaten"],
        "correct": "eaten",
        "explanation": "<p><strong>eaten</strong> is correct. <em>Having</em> is always followed by the "
                       "V3, never by the past simple: <em>Having eaten</em>, not <em>Having "
                       "ate</em>.<br><br>"
                       "<em>(<em>Having</em> dan keyin doim V3 keladi, past simple emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ in simple English, the book is easy to read.</strong> (write)</p>",
        "choices": ["Written", "Writing", "Wrote", "Write"],
        "correct": "Written",
        "explanation": "<p><strong>Written</strong> is correct. The book was written by somebody — it "
                       "receives the action, so we use the V3.<br><br>"
                       "<em>(Kitobni kimdir yozgan — u harakatni qabul qilyapti, shuning uchun V3 "
                       "ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Firdavs fell, ___ his arm.</strong> (break)</p>",
        "choices": ["broke", "breaking", "broken", "break"],
        "correct": "breaking",
        "explanation": "<p><strong>breaking</strong> is correct. Here the <em>-ing</em> clause shows the "
                       "<strong>result</strong> of the first action — he fell, and the fall broke his "
                       "arm.<br><br>"
                       "<em>(Bu yerda <em>-ing</em> oborot birinchi harakatning "
                       "<strong>natijasini</strong> koʻrsatyapti.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>After ___ our work, we went out.</strong> (finish)</p>",
        "choices": ["finish", "finished", "finishing", "to finish"],
        "correct": "finishing",
        "explanation": "<p><strong>finishing</strong> is correct. After a preposition such as "
                       "<em>after, before, on</em>, the verb always takes the <em>-ing</em> "
                       "form.<br><br>"
                       "<em>(<em>after, before, on</em> kabi predloglardan keyin feʼl doim "
                       "<em>-ing</em> shaklda keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ lived in Nukus for ten years, Afsona knows the city well.</strong></p>",
        "choices": ["Have", "Having", "Has", "Had"],
        "correct": "Having",
        "explanation": "<p><strong>Having</strong> is correct — the ten years came first, and the "
                       "knowledge is the result. <em>Having lived…</em> = \"Oʻn yil yashagani "
                       "uchun…\"<br><br>"
                       "<em>(Oʻn yillik hayot oldin boʻlgan, bilim esa uning natijasi — shuning uchun "
                       "<em>Having lived…</em>)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ to the party, Iroda bought a present.</strong> (invite)</p>",
        "choices": ["Inviting", "Invite", "Invited", "To invite"],
        "correct": "Invited",
        "explanation": "<p><strong>Invited</strong> is correct. Iroda did not invite anybody — she "
                       "<em>was invited</em>, so the passive V3 form is needed.<br><br>"
                       "<em>(Iroda hech kimni taklif qilmadi — uni taklif qilishdi, shuning uchun majhul "
                       "V3 shakli kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Opening the door, Davron went in.",
            "Opened the door, Davron went in.",
            "Open the door, Davron went in.",
            "Been opening the door, Davron went in.",
        ],
        "correct": "Opening the door, Davron went in.",
        "explanation": "<p><strong>Opening the door, Davron went in.</strong> is correct. Davron opens "
                       "the door himself, so the active <em>-ing</em> form is right; <em>Opened</em> "
                       "would mean somebody opened Davron.<br><br>"
                       "<em>(Eshikni Davronning oʻzi ochyapti, shuning uchun aniq nisbatdagi "
                       "<em>-ing</em> kerak. <em>Opened</em> boʻlsa, Davronni kimdir \"ochgan\" boʻlib "
                       "chiqadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ by the news, Shaxzoda said nothing.</strong> (surprise)</p>",
        "choices": ["Surprising", "Surprise", "To surprise", "Surprised"],
        "correct": "Surprised",
        "explanation": "<p><strong>Surprised</strong> is correct. Shaxzoda receives the surprise, so the "
                       "V3 is used. <em>Surprising</em> would describe the news, not her.<br><br>"
                       "<em>(Hayratni Shaxzoda qabul qilyapti, shuning uchun V3. <em>Surprising</em> "
                       "boʻlsa, u yangilikni tasvirlagan boʻlardi, qizni emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is absurd (a \"dangling participle\")?</p>",
        "choices": [
            "Walking down the street, I saw that the shop was closed.",
            "Walking down the street, the shop was closed.",
            "Feeling tired, Charos sat down.",
            "Hearing a noise, Sherbek opened the window.",
        ],
        "correct": "Walking down the street, the shop was closed.",
        "explanation": "<p><strong>Walking down the street, the shop was closed.</strong> is absurd — it "
                       "says the shop was walking. The participle must belong to the subject of the main "
                       "clause.<br><br>"
                       "<em>(Bu gap \"doʻkon koʻcha boʻylab ketyapti\" degan maʼnoni beradi. Ravishdosh "
                       "asosiy gapning egasiga tegishli boʻlishi shart — \"buni kim qilyapti?\" deb "
                       "tekshiring.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Being tired, my mother made me tea.",
            "Running to school, my bag fell open.",
            "Because I was tired, my mother made me tea.",
            "Invited to the party, my new shoes were dirty.",
        ],
        "correct": "Because I was tired, my mother made me tea.",
        "explanation": "<p><strong>Because I was tired, my mother made me tea.</strong> is correct. In "
                       "the other three the participle belongs to the wrong person or thing — the mother "
                       "was not tired, the bag was not running, the shoes were not invited. When the "
                       "subjects differ, use the ordinary version with <em>because</em> or "
                       "<em>while</em>.<br><br>"
                       "<em>(Qolgan uchtasida ravishdosh notoʻgʻri egaga tegishli. Egalar har xil "
                       "boʻlsa, <em>because</em> yoki <em>while</em> bilan oddiy shaklda "
                       "yozing.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "Having finished my work, I went out.",
            "Having finish my work, I went out.",
            "Built in 1890, the house is old.",
            "Waiting for the bus, Marjona read the news.",
        ],
        "correct": "Having finish my work, I went out.",
        "explanation": "<p><strong>Having finish my work, I went out.</strong> is the mistake — "
                       "<em>Having</em> must be followed by the V3: <em>Having "
                       "finished</em>.<br><br>"
                       "<em>(<em>Having</em> dan keyin albatta V3 kelishi kerak: <em>Having "
                       "finished</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Build in 1890, the house is old.",
            "Building in 1890, the house is old.",
            "Been built in 1890, the house is old.",
            "Built in 1890, the house is old.",
        ],
        "correct": "Built in 1890, the house is old.",
        "explanation": "<p><strong>Built in 1890, the house is old.</strong> is correct. The passive "
                       "participle clause uses the V3 alone — no <em>been</em>, and not the base "
                       "form.<br><br>"
                       "<em>(Majhul ravishdosh oborotda faqat V3 ishlatiladi — <em>been</em> ham, asl "
                       "shakl ham kerak emas.)</em></p>",
    },
    {
        "text": "<p>Combine into one sentence: <strong>Jasur heard the alarm. He jumped out of "
                "bed.</strong></p>",
        "choices": [
            "Hearing the alarm, Jasur jumped out of bed.",
            "Heard the alarm, Jasur jumped out of bed.",
            "Hearing the alarm, the bed jumped out of Jasur.",
            "Having hear the alarm, Jasur jumped out of bed.",
        ],
        "correct": "Hearing the alarm, Jasur jumped out of bed.",
        "explanation": "<p><strong>Hearing the alarm, Jasur jumped out of bed.</strong> is correct — "
                       "same subject in both halves, active meaning, so the <em>-ing</em> clause joins "
                       "them with no conjunction at all.<br><br>"
                       "<em>(Ikkala qismning egasi bir xil va maʼno aniq nisbatda, shuning uchun "
                       "<em>-ing</em> oborot ularni bogʻlovchisiz birlashtiradi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue. Which reply sounds more natural in ordinary "
                "conversation?</p>"
                "<p><strong>Marjona:</strong> Why did you go to bed so early?</p>"
                "<p><strong>Firdavs:</strong> ___</p>",
        "choices": [
            "Being tired, I went to bed early.",
            "Tired being, I went to bed early.",
            "Having tired, I went to bed early.",
            "I went to bed early because I was tired.",
        ],
        "correct": "I went to bed early because I was tired.",
        "explanation": "<p><strong>I went to bed early because I was tired.</strong> is the natural "
                       "reply. <em>Being tired…</em> is grammatically correct but it belongs to "
                       "<strong>writing</strong> — in a conversation the version with <em>because</em> "
                       "is far more normal.<br><br>"
                       "<em>(<em>Being tired…</em> grammatik toʻgʻri, lekin u <strong>yozma "
                       "nutq</strong> uchun. Suhbatda <em>because</em> bilan aytish ancha "
                       "tabiiy.)</em></p>",
    },
]


# =====================================================================
# PE-87 — The Unreal Past: It's time, would rather, as if
# =====================================================================
Q_PE87 = [
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It's time you ___ home, Samandar. It's nearly midnight.</strong></p>",
        "choices": ["go", "went", "going", "to go"],
        "correct": "went",
        "explanation": "<p><strong>went</strong> is correct. After <em>It's time + subject</em> we use a "
                       "past form, even though the meaning is <em>now</em>.<br><br>"
                       "<em>(<em>It's time + ega</em> dan keyin oʻtgan zamon shakli qoʻyiladi, gap "
                       "esa <strong>hozir</strong> haqida — \"endi ketsang boʻladi\".)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It's time ___ go — the bus leaves in five minutes.</strong></p>",
        "choices": ["to", "for", "that", "you"],
        "correct": "to",
        "explanation": "<p><strong>to</strong> is correct. <em>It's time to go</em> is the neutral "
                       "version — it simply states that the moment has arrived, with no criticism in "
                       "it.<br><br>"
                       "<em>(<em>It's time to go</em> — betaraf shakl: shunchaki \"ketish vaqti "
                       "boʻldi\", hech qanday taʼnasiz.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I'd rather ___ at home tonight.</strong></p>",
        "choices": ["to stay", "staying", "stay", "stayed"],
        "correct": "stay",
        "explanation": "<p><strong>stay</strong> is correct. When <strong>I</strong> am the one acting, "
                       "<em>would rather</em> is followed by the base verb — and never by "
                       "<em>to</em>.<br><br>"
                       "<em>(Harakatni <strong>men</strong> bajarsam, <em>would rather</em> dan keyin "
                       "feʼlning asl shakli keladi, <em>to</em> esa hech qachon "
                       "qoʻyilmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I'd rather you ___ at home tonight — the roads are icy.</strong></p>",
        "choices": ["stay", "to stay", "staying", "stayed"],
        "correct": "stayed",
        "explanation": "<p><strong>stayed</strong> is correct. When <strong>somebody else</strong> does "
                       "the action, <em>would rather</em> takes a past tense — the same unreal-past "
                       "pattern.<br><br>"
                       "<em>(Harakatni <strong>boshqa odam</strong> bajarsa, <em>would rather</em> dan "
                       "keyin oʻtgan zamon keladi — xuddi shu \"noreal oʻtgan zamon\" "
                       "qoidasi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek talks as if he ___ everything.</strong> (he doesn't)</p>",
        "choices": ["knows", "know", "knowing", "knew"],
        "correct": "knew",
        "explanation": "<p><strong>knew</strong> is correct. The comparison is not true, so the verb "
                       "steps one tense backwards.<br><br>"
                       "<em>(Taqqoslash haqiqat emas, shuning uchun feʼl bir zamon orqaga qadam "
                       "tashlaydi — \"bilgandek gapiradi\".)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It's high time Sirojiddin ___ a job.</strong></p>",
        "choices": ["find", "finds", "found", "finding"],
        "correct": "found",
        "explanation": "<p><strong>found</strong> is correct. <em>It's high time</em> takes the same past "
                       "form and makes the criticism even stronger — \"allaqachon vaqti boʻldi\".<br><br>"
                       "<em>(<em>It's high time</em> ham oʻtgan zamon shaklini oladi va taʼnani yanada "
                       "kuchaytiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I'd rather ___ talk about it, if you don't mind.</strong></p>",
        "choices": ["not", "don't", "not to", "no"],
        "correct": "not",
        "explanation": "<p><strong>not</strong> is correct. When I am the one acting, the negative is "
                       "<em>would rather not + base verb</em>: <em>I'd rather not talk about "
                       "it.</em><br><br>"
                       "<em>(Harakatni men bajarsam, inkor shakli — <em>would rather not + asl "
                       "feʼl</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I'd rather you ___ smoke here.</strong></p>",
        "choices": ["don't", "didn't", "not", "won't"],
        "correct": "didn't",
        "explanation": "<p><strong>didn't</strong> is correct. For somebody else, the negative is "
                       "<em>would rather + didn't</em>. Remember <em>I'd rather you didn't</em> as a "
                       "whole phrase — it is one of the politest refusals in English.<br><br>"
                       "<em>(Boshqa odam uchun inkor shakli — <em>would rather + didn't</em>. "
                       "<em>I'd rather you didn't</em> ni butun ibora sifatida yodlang: bu ingliz "
                       "tilidagi eng muloyim rad javoblaridan biri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>I'd rather walk ___ take a taxi.</strong></p>",
        "choices": ["that", "then", "than", "as"],
        "correct": "than",
        "explanation": "<p><strong>than</strong> is correct — the comparison after <em>would rather</em> "
                       "always uses <em>than</em>, matching the Uzbek \"...gandan <strong>koʻra</strong> "
                       "...ganim maʼqul\".<br><br>"
                       "<em>(<em>would rather</em> dan keyingi taqqoslash doim <em>than</em> bilan "
                       "boʻladi — oʻzbekchadagi \"koʻra\" soʻziga toʻgʻri keladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Iroda looks as though she ___ a ghost.</strong> (she hasn't)</p>",
        "choices": ["had seen", "has seen", "sees", "seeing"],
        "correct": "had seen",
        "explanation": "<p><strong>had seen</strong> is correct. The comparison is unreal, so the verb "
                       "steps back one further — from the present perfect to the past "
                       "perfect.<br><br>"
                       "<em>(Taqqoslash noreal, shuning uchun feʼl yana bir qadam orqaga qadam tashlaydi — "
                       "\"arvoh koʻrgandek\".)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Look at those clouds — it looks as if it ___ to rain.</strong></p>",
        "choices": ["went", "were going", "is going", "had gone"],
        "correct": "is going",
        "explanation": "<p><strong>is going</strong> is correct. Here the comparison <em>might well be "
                       "true</em>, so an ordinary present tense is used — no step backwards.<br><br>"
                       "<em>(Bu yerda taqqoslash <strong>haqiqat boʻlishi mumkin</strong>, shuning uchun "
                       "oddiy hozirgi zamon ishlatiladi — orqaga qadam yoʻq.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Abdulloh behaves as if he ___ the boss.</strong> (he isn't)</p>",
        "choices": ["were", "is", "was being", "be"],
        "correct": "were",
        "explanation": "<p><strong>were</strong> is correct. In unreal comparisons <em>were</em> is used "
                       "for all persons — <em>as if he were</em>, not <em>as if he was</em>.<br><br>"
                       "<em>(Noreal taqqoslashda barcha shaxslar uchun <em>were</em> ishlatiladi — "
                       "<em>as if he were</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence contains a note of criticism?</p>",
        "choices": [
            "It's time to leave.",
            "It's time for us to leave.",
            "It's time to go home.",
            "It's time you left.",
        ],
        "correct": "It's time you left.",
        "explanation": "<p><strong>It's time you left.</strong> carries the criticism — it means you have "
                       "stayed too long already. The other three, with <em>to + verb</em>, are "
                       "neutral.<br><br>"
                       "<em>(<em>It's time you left</em> da ozgina taʼna bor — \"allaqachon ketishing "
                       "kerak edi\". <em>to + feʼl</em> bilan tuzilgan qolganlari betaraf.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I'd rather to stay here.",
            "I'd rather staying here.",
            "I'd rather stayed here.",
            "I'd rather stay here.",
        ],
        "correct": "I'd rather stay here.",
        "explanation": "<p><strong>I'd rather stay here.</strong> is correct. <em>would rather</em> never "
                       "takes <em>to</em> or <em>-ing</em>, and the past form is only used when somebody "
                       "<em>else</em> acts.<br><br>"
                       "<em>(<em>would rather</em> dan keyin <em>to</em> ham, <em>-ing</em> ham "
                       "qoʻyilmaydi. Oʻtgan zamon esa faqat harakatni boshqa odam bajarganda "
                       "ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence tells us that he is <strong>not</strong> a professor?</p>",
        "choices": [
            "He speaks as if he is a professor.",
            "He speaks as if he were a professor.",
            "He speaks like a professor speaks.",
            "He speaks as if he will be a professor.",
        ],
        "correct": "He speaks as if he were a professor.",
        "explanation": "<p><strong>He speaks as if he were a professor.</strong> is the one. The past "
                       "form <em>were</em> is the signal that the comparison is imaginary; a present "
                       "tense would suggest it might really be true.<br><br>"
                       "<em>(Oʻtgan zamondagi <em>were</em> — taqqoslash xayoliy ekanining belgisi. "
                       "Hozirgi zamon qoʻyilsa, bu haqiqat boʻlishi mumkindek eshitiladi.)</em></p>",
    },
    {
        "text": "<p>Marjona wants to borrow your new phone and you do not want to lend it. "
                "What is the politest reply?</p>",
        "choices": [
            "Don't take it.",
            "No, you can't.",
            "I'd rather you didn't, if you don't mind.",
            "I'd rather you don't, if you don't mind.",
        ],
        "correct": "I'd rather you didn't, if you don't mind.",
        "explanation": "<p><strong>I'd rather you didn't, if you don't mind.</strong> is the politest. It "
                       "is far gentler than <em>No</em> or <em>Don't</em> — and note the past form "
                       "<em>didn't</em>, not <em>don't</em>.<br><br>"
                       "<em>(Bu <em>No</em> yoki <em>Don't</em> dan ancha muloyim. Eʼtibor bering — "
                       "oʻtgan zamondagi <em>didn't</em>, <em>don't</em> emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "It's time you went home.",
            "It's time you go home.",
            "It's time to go home.",
            "It's high time she found a job.",
        ],
        "correct": "It's time you go home.",
        "explanation": "<p><strong>It's time you go home.</strong> is the mistake. After <em>It's time + "
                       "subject</em> the verb must be in the past: <em>It's time you went home.</em><br><br>"
                       "<em>(<em>It's time + ega</em> dan keyin feʼl oʻtgan zamonda boʻlishi shart.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "I'd rather walk that take the bus.",
            "I'd rather you don't come late.",
            "I'd rather to walk than take the bus.",
            "I'd rather you didn't come late.",
        ],
        "correct": "I'd rather you didn't come late.",
        "explanation": "<p><strong>I'd rather you didn't come late.</strong> is correct. The others show "
                       "the three classic errors: <em>that</em> instead of <em>than</em>, <em>don't</em> "
                       "instead of <em>didn't</em>, and an extra <em>to</em>.<br><br>"
                       "<em>(Qolganlarida uchta klassik xato bor: <em>than</em> oʻrniga <em>that</em>, "
                       "<em>didn't</em> oʻrniga <em>don't</em> va ortiqcha <em>to</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Rozimurod teacher:</strong> ___ you started your project, Javohir — "
                "it must be finished on Friday.</p>",
        "choices": ["It's time", "It's the time", "There is time", "It has time"],
        "correct": "It's time",
        "explanation": "<p><strong>It's time</strong> is correct. The structure is fixed: <em>It's time + "
                       "subject + past verb</em>, with a note of \"you should have started "
                       "already\".<br><br>"
                       "<em>(Qurilma qatʼiy: <em>It's time + ega + oʻtgan zamondagi feʼl</em>, "
                       "\"allaqachon boshlagan boʻlishing kerak edi\" ohangi bilan.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Charos:</strong> Shall I tell everybody about your marks?</p>"
                "<p><strong>Madina:</strong> ___</p>",
        "choices": [
            "I'd rather you don't.",
            "I'd rather you didn't, please.",
            "I'd rather you not.",
            "I'd rather not you.",
        ],
        "correct": "I'd rather you didn't, please.",
        "explanation": "<p><strong>I'd rather you didn't, please.</strong> is correct. Madina is asking "
                       "somebody <em>else</em> not to do something, so the past form <em>didn't</em> is "
                       "required — and the phrase softens the refusal.<br><br>"
                       "<em>(Madina <strong>boshqa odamdan</strong> biror ishni qilmaslikni soʻrayapti, "
                       "shuning uchun oʻtgan zamondagi <em>didn't</em> kerak — bu ibora rad javobini "
                       "yumshatadi.)</em></p>",
    },
]


# =====================================================================
# PE-88 — Linking Words for Writing: however, therefore, although
# =====================================================================
Q_PE88 = [
    {
        "text": "<p>Choose the correct linking word.</p>"
                "<p><strong>Learning English opens many doors. ___, it improves your memory.</strong></p>",
        "choices": ["However", "In addition", "Therefore", "For example"],
        "correct": "In addition",
        "explanation": "<p><strong>In addition</strong> is correct — the second sentence <em>adds</em> "
                       "another advantage. <em>Moreover</em> and <em>Furthermore</em> would work "
                       "too.<br><br>"
                       "<em>(Ikkinchi gap yana bir foydani <strong>qoʻshyapti</strong>. "
                       "<em>Moreover</em>, <em>Furthermore</em> ham mos kelardi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct linking word.</p>"
                "<p><strong>Learning a language takes time. ___, you need patience.</strong></p>",
        "choices": ["Therefore", "However", "For example", "In addition"],
        "correct": "Therefore",
        "explanation": "<p><strong>Therefore</strong> is correct — the second sentence is the "
                       "<em>result</em> of the first. <em>As a result</em> and <em>Consequently</em> do "
                       "the same job.<br><br>"
                       "<em>(Ikkinchi gap birinchisining <strong>natijasi</strong>. <em>As a result</em>, "
                       "<em>Consequently</em> ham xuddi shu vazifani bajaradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct linking word.</p>"
                "<p><strong>Iroda says studying online is convenient. ___, it can be lonely.</strong></p>",
        "choices": ["Moreover", "Therefore", "However", "For instance"],
        "correct": "However",
        "explanation": "<p><strong>However</strong> is correct — the second sentence <em>contrasts</em> "
                       "with the first. <em>On the other hand</em> and <em>Nevertheless</em> belong to "
                       "the same family.<br><br>"
                       "<em>(Ikkinchi gap birinchisiga <strong>qarama-qarshi</strong>. <em>On the other "
                       "hand</em>, <em>Nevertheless</em> ham shu oilaga kiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct linking word.</p>"
                "<p><strong>Many sports are popular in Jasur's class, ___ football and volleyball.</strong></p>",
        "choices": ["therefore", "however", "moreover", "such as"],
        "correct": "such as",
        "explanation": "<p><strong>such as</strong> is correct — it introduces examples inside the "
                       "sentence, where <em>For example</em> would start a new one.<br><br>"
                       "<em>(<em>such as</em> misollarni gap ichida keltiradi; <em>For example</em> esa "
                       "yangi gap boshlagan boʻlardi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct linking word.</p>"
                "<p><strong>___, the effort is definitely worth it.</strong> (the last sentence of an "
                "essay)</p>",
        "choices": ["In addition", "In conclusion", "However", "For example"],
        "correct": "In conclusion",
        "explanation": "<p><strong>In conclusion</strong> is correct. <em>To sum up</em>, <em>Overall</em> "
                       "and <em>All in all</em> also close an essay.<br><br>"
                       "<em>(<em>To sum up</em>, <em>Overall</em>, <em>All in all</em> ham inshoni "
                       "yakunlaydi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is punctuated correctly?</p>",
        "choices": [
            "The plan, however, failed.",
            "The plan however failed.",
            "The plan, however failed.",
            "The plan however, failed.",
        ],
        "correct": "The plan, however, failed.",
        "explanation": "<p><strong>The plan, however, failed.</strong> is correct. In the middle of a "
                       "sentence a linking word takes commas on <em>both</em> sides; at the start it "
                       "takes one comma after it.<br><br>"
                       "<em>(Gap oʻrtasida bogʻlovchi soʻz <strong>ikki tomondan</strong> vergul oladi; "
                       "gap boshida esa faqat oʻzidan keyin.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ it rained all morning, we went out.</strong></p>",
        "choices": ["Despite", "In spite of", "Although", "However"],
        "correct": "Although",
        "explanation": "<p><strong>Although</strong> is correct, because a full clause "
                       "(<em>it rained</em> = subject + verb) follows. <em>Despite</em> and <em>in spite "
                       "of</em> need a noun, and <em>however</em> needs a new sentence.<br><br>"
                       "<em>(Keyin toʻliq gap (ega + kesim) kelgani uchun <em>Although</em> kerak. "
                       "<em>Despite</em> ga ot, <em>however</em> ga esa yangi gap kerak.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___ the rain, we went out.</strong></p>",
        "choices": ["Although", "Despite", "Though", "However"],
        "correct": "Despite",
        "explanation": "<p><strong>Despite</strong> is correct, because only a noun (<em>the rain</em>) "
                       "follows. <em>Despite</em> and <em>in spite of</em> take a noun or an "
                       "<em>-ing</em> form, never a clause.<br><br>"
                       "<em>(Keyin faqat ot (<em>the rain</em>) kelgani uchun <em>Despite</em> kerak. "
                       "<em>Despite / in spite of</em> dan keyin ot yoki <em>-ing</em> keladi, toʻliq "
                       "gap emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>It rained all morning. ___, we went out.</strong></p>",
        "choices": ["Although", "Despite", "However", "In spite of"],
        "correct": "However",
        "explanation": "<p><strong>However</strong> is correct — it opens a <em>new sentence</em> after a "
                       "full stop, which is exactly what the punctuation here requires.<br><br>"
                       "<em>(<em>However</em> nuqtadan keyin <strong>yangi gap</strong> boshlaydi — bu "
                       "yerdagi tinish belgilari aynan shuni talab qilyapti.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>In spite of ___, Behruz walked to school.</strong></p>",
        "choices": ["the rain was heavy", "it rained", "although it rained", "the heavy rain"],
        "correct": "the heavy rain",
        "explanation": "<p><strong>the heavy rain</strong> is correct. <em>In spite of</em> must be "
                       "followed by a noun phrase, so the clause <em>the rain was heavy</em> has to "
                       "become the noun phrase <em>the heavy rain</em>.<br><br>"
                       "<em>(<em>In spite of</em> dan keyin ot birikmasi kelishi shart, shuning uchun "
                       "<em>the rain was heavy</em> gapi <em>the heavy rain</em> ot birikmasiga "
                       "aylanadi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct linking word.</p>"
                "<p><strong>___, Madina would like to explain the problem. Secondly, she will "
                "suggest a solution.</strong></p>",
        "choices": ["Finally", "However", "Therefore", "Firstly"],
        "correct": "Firstly",
        "explanation": "<p><strong>Firstly</strong> is correct. <em>Firstly / Secondly / Finally</em> put "
                       "your points in order and give an essay a clear shape.<br><br>"
                       "<em>(<em>Firstly / Secondly / Finally</em> fikrlarni tartibga soladi va inshoga "
                       "aniq tuzilish beradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct linking word.</p>"
                "<p><strong>Sirojiddin never opens the book and never asks questions. ___, he is not "
                "interested.</strong></p>",
        "choices": ["In other words", "For example", "However", "Nevertheless"],
        "correct": "In other words",
        "explanation": "<p><strong>In other words</strong> is correct — the second sentence says the same "
                       "thing again, more directly. <em>That is to say</em> does the same job.<br><br>"
                       "<em>(Ikkinchi gap oʻsha fikrni boshqacha, toʻgʻridan-toʻgʻri aytyapti. "
                       "<em>That is to say</em> ham shu vazifada.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "However the weather was bad, we went.",
            "Despite the weather was bad, we went.",
            "In spite the weather was bad, we went.",
            "Although the weather was bad, we went.",
        ],
        "correct": "Although the weather was bad, we went.",
        "explanation": "<p><strong>Although the weather was bad, we went.</strong> is correct. Only "
                       "<em>although</em> can be followed by a full clause here.<br><br>"
                       "<em>(Bu yerda toʻliq gap kelgani uchun faqat <em>although</em> mos "
                       "keladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Despite it rained, we went out.",
            "Despite of the rain, we went out.",
            "Despite the rain, we went out.",
            "Despite that it rained, we went out.",
        ],
        "correct": "Despite the rain, we went out.",
        "explanation": "<p><strong>Despite the rain, we went out.</strong> is correct. Note there is no "
                       "<em>of</em> after <em>despite</em> — that belongs to <em>in spite "
                       "of</em>.<br><br>"
                       "<em>(<em>despite</em> dan keyin <em>of</em> qoʻyilmaydi — <em>of</em> faqat "
                       "<em>in spite of</em> iborasida boʻladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "Although Firdavs studied hard, but he failed.",
            "Although Firdavs studied hard, he failed.",
            "Although Firdavs studied hard, however he failed.",
            "Firdavs studied hard, although but he failed.",
        ],
        "correct": "Although Firdavs studied hard, he failed.",
        "explanation": "<p><strong>Although Firdavs studied hard, he failed.</strong> is correct. English uses "
                       "<strong>one</strong> contrast marker per sentence — the <em>garchi … lekin</em> "
                       "habit from Uzbek produces <em>although … but</em>, which is wrong (PE-52).<br><br>"
                       "<em>(Ingliz tilida bitta gapda <strong>bitta</strong> qarama-qarshilik soʻzi "
                       "boʻladi. Oʻzbekchadagi \"garchi … lekin\" odati <em>although … but</em> "
                       "xatosini keltirib chiqaradi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is punctuated correctly?</p>",
        "choices": [
            "I like tea, however I don't like coffee.",
            "I like tea however, I don't like coffee.",
            "I like tea. However, I don't like coffee.",
            "I like tea, however, I don't like coffee.",
        ],
        "correct": "I like tea. However, I don't like coffee.",
        "explanation": "<p><strong>I like tea. However, I don't like coffee.</strong> is correct. "
                       "<em>However</em> cannot join two sentences with a comma — you need a full stop or "
                       "a semicolon before it (PE-81).<br><br>"
                       "<em>(<em>However</em> ikki gapni vergul bilan bogʻlay olmaydi — undan oldin "
                       "nuqta yoki nuqtali vergul kerak.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "Therefore we must act now.",
            "Therefore, we must act now.",
            "In conclusion, the plan is a good one.",
            "For example, Sherbek reads a page every day.",
        ],
        "correct": "Therefore we must act now.",
        "explanation": "<p><strong>Therefore we must act now.</strong> is the mistake — a linking word at "
                       "the start of a sentence always takes a comma after it.<br><br>"
                       "<em>(Gap boshidagi bogʻlovchi soʻzdan keyin doim vergul qoʻyiladi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "In spite of the rain was heavy, we walked.",
            "Despite of the heavy rain, we walked.",
            "Although the rain, we walked.",
            "In spite of the heavy rain, we walked.",
        ],
        "correct": "In spite of the heavy rain, we walked.",
        "explanation": "<p><strong>In spite of the heavy rain, we walked.</strong> is correct. Each of "
                       "the others breaks one rule: a clause after <em>in spite of</em>, an extra "
                       "<em>of</em> after <em>despite</em>, and a bare noun after "
                       "<em>although</em>.<br><br>"
                       "<em>(Qolgan uchtasi bittadan qoidani buzgan: <em>in spite of</em> dan keyin "
                       "toʻliq gap, <em>despite</em> dan keyin ortiqcha <em>of</em>, "
                       "<em>although</em> dan keyin esa yolgʻiz ot.)</em></p>",
    },
    {
        "text": "<p>Choose the correct linking word.</p>"
                "<p><strong>Elbek thinks studying abroad is expensive. ___, it gives you experience you cannot get "
                "at home.</strong></p>",
        "choices": ["Therefore", "However", "For example", "In addition"],
        "correct": "However",
        "explanation": "<p><strong>However</strong> is correct — the second sentence gives the other side "
                       "of the argument, so a contrast word is needed, not an adding one.<br><br>"
                       "<em>(Ikkinchi gap masalaning ikkinchi tomonini koʻrsatyapti, shuning uchun "
                       "qarama-qarshilik soʻzi kerak, qoʻshimcha soʻz emas.)</em></p>",
    },
    {
        "text": "<p>Rozimurod teacher asks for a two-sentence argument. Which version is written "
                "correctly?</p>",
        "choices": [
            "Reading improves your vocabulary. For example, one novel can teach you hundreds of words.",
            "Reading improves your vocabulary. For example one novel can teach you hundreds of words.",
            "Reading improves your vocabulary, for example, one novel can teach you hundreds of words.",
            "Reading improves your vocabulary, however, one novel can teach you hundreds of words.",
        ],
        "correct": "Reading improves your vocabulary. For example, one novel can teach you hundreds of words.",
        "explanation": "<p>The first version is correct: a full stop between the two sentences, "
                       "<em>For example</em> at the start of the second, and a comma after it. The third "
                       "is a comma splice and the fourth uses a contrast word where an example is "
                       "needed.<br><br>"
                       "<em>(Ikki gap orasida nuqta, ikkinchi gap boshida <em>For example</em> va undan "
                       "keyin vergul. Uchinchisi — comma splice, toʻrtinchisida esa misol oʻrniga "
                       "qarama-qarshilik soʻzi ishlatilgan.)</em></p>",
    },
]


# =====================================================================
# PE-89 — Word Formation: Prefixes and Suffixes
# =====================================================================
Q_PE89 = [
    {
        "text": "<p>Choose the opposite.</p>"
                "<p><strong>possible → ___</strong></p>",
        "choices": ["unpossible", "impossible", "inpossible", "dispossible"],
        "correct": "impossible",
        "explanation": "<p><strong>impossible</strong> is correct. Before <em>m</em> and <em>p</em> the "
                       "prefix becomes <em>im-</em> — the prefix copies the first letter of the "
                       "word.<br><br>"
                       "<em>(<em>m</em> va <em>p</em> harflaridan oldin prefiks <em>im-</em> boʻladi — "
                       "prefiks soʻzning birinchi harfini takrorlaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the opposite.</p>"
                "<p><strong>legal → ___</strong></p>",
        "choices": ["unlegal", "inlegal", "illegal", "dislegal"],
        "correct": "illegal",
        "explanation": "<p><strong>illegal</strong> is correct — before <em>l</em> the prefix becomes "
                       "<em>il-</em>, just as in <em>illogical</em>.<br><br>"
                       "<em>(<em>l</em> harfidan oldin prefiks <em>il-</em> boʻladi — <em>illogical</em> "
                       "dagi kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the opposite.</p>"
                "<p><strong>regular → ___</strong></p>",
        "choices": ["irregular", "unregular", "inregular", "disregular"],
        "correct": "irregular",
        "explanation": "<p><strong>irregular</strong> is correct — before <em>r</em> the prefix becomes "
                       "<em>ir-</em>: <em>irregular, irresponsible</em>.<br><br>"
                       "<em>(<em>r</em> harfidan oldin prefiks <em>ir-</em> boʻladi: <em>irregular, "
                       "irresponsible</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the opposite.</p>"
                "<p><strong>honest → ___</strong></p>",
        "choices": ["unhonest", "inhonest", "imhonest", "dishonest"],
        "correct": "dishonest",
        "explanation": "<p><strong>dishonest</strong> is correct. <em>dis-</em> reverses the idea: "
                       "<em>disagree, dishonest, disappear</em>. Which prefix a word takes has to be "
                       "learned with the word itself.<br><br>"
                       "<em>(<em>dis-</em> maʼnoni teskari qiladi. Qaysi prefiks mos kelishini soʻzning "
                       "oʻzi belgilaydi, shuning uchun soʻzni prefiksi bilan birga yodlang.)</em></p>",
    },
    {
        "text": "<p>Choose the opposite.</p>"
                "<p><strong>usual → ___</strong></p>",
        "choices": ["inusual", "unusual", "disusual", "imusual"],
        "correct": "unusual",
        "explanation": "<p><strong>unusual</strong> is correct. <em>un-</em> is the commonest negative "
                       "prefix of all: <em>unhappy, unfair, unable</em>.<br><br>"
                       "<em>(<em>un-</em> — eng koʻp uchraydigan inkor prefiksi: <em>unhappy, unfair, "
                       "unable</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct form.</p>"
                "<p><strong>Shaxzoda won the competition. It was a great ___.</strong> (succeed)</p>",
        "choices": ["succeed", "successful", "success", "successfully"],
        "correct": "success",
        "explanation": "<p><strong>success</strong> is correct. After <em>a great</em> we need a noun — "
                       "the slot decides the form.<br><br>"
                       "<em>(<em>a great</em> dan keyin ot kerak — soʻz qaysi oʻrinda turgani uning "
                       "shaklini belgilaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct form.</p>"
                "<p><strong>Javohir explained the problem very ___.</strong> (clear)</p>",
        "choices": ["clear", "clearness", "clarity", "clearly"],
        "correct": "clearly",
        "explanation": "<p><strong>clearly</strong> is correct. The word describes <em>how</em> he "
                       "explained, so an adverb is needed — and adverbs usually add "
                       "<em>-ly</em>.<br><br>"
                       "<em>(Soʻz <strong>qanday</strong> tushuntirganini bildiryapti, shuning uchun "
                       "ravish kerak — ravishlar odatda <em>-ly</em> qoʻshimchasini oladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct form.</p>"
                "<p><strong>He is a very ___ businessman.</strong> (success)</p>",
        "choices": ["success", "succeed", "successful", "successfully"],
        "correct": "successful",
        "explanation": "<p><strong>successful</strong> is correct. Before a noun "
                       "(<em>businessman</em>) we need an adjective, not a noun.<br><br>"
                       "<em>(Otdan (<em>businessman</em>) oldin sifat kerak, ot emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct form.</p>"
                "<p><strong>I'm afraid I disagree with your ___.</strong> (decide)</p>",
        "choices": ["decision", "decide", "decisive", "decisively"],
        "correct": "decision",
        "explanation": "<p><strong>decision</strong> is correct. After <em>your</em> a noun is needed; "
                       "the suffix <em>-sion / -tion</em> turns a verb into a noun.<br><br>"
                       "<em>(<em>your</em> dan keyin ot kerak; <em>-sion / -tion</em> qoʻshimchasi feʼlni "
                       "otga aylantiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Ilgʻor misunderstood the question, so he had to ___ his answer.</strong></p>",
        "choices": ["rewrite", "miswrite", "overwrite", "prewrite"],
        "correct": "rewrite",
        "explanation": "<p><strong>rewrite</strong> is correct. <em>re-</em> means \"again\": "
                       "<em>rewrite, rebuild, return, repeat</em>.<br><br>"
                       "<em>(<em>re-</em> \"qaytadan\" degani: <em>rewrite, rebuild, return, "
                       "repeat</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Be careful not to ___ this word, Samandar — it has two s's.</strong></p>",
        "choices": ["respell", "misspell", "overspell", "unspell"],
        "correct": "misspell",
        "explanation": "<p><strong>misspell</strong> is correct. <em>mis-</em> means \"wrongly\": "
                       "<em>misspell, misunderstand, misread</em>.<br><br>"
                       "<em>(<em>mis-</em> \"notoʻgʻri\" degani: <em>misspell, misunderstand, "
                       "misread</em>.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Elbek ___ and missed the first lesson.</strong></p>",
        "choices": ["underslept", "preslept", "overslept", "reslept"],
        "correct": "overslept",
        "explanation": "<p><strong>overslept</strong> is correct. <em>over-</em> means \"too much\": "
                       "<em>oversleep, overcook</em>. Its opposite, <em>under-</em>, means \"too "
                       "little\".<br><br>"
                       "<em>(<em>over-</em> \"haddan ziyod\" degani: <em>oversleep, overcook</em>. "
                       "Uning teskarisi <em>under-</em> — \"yetarli emas\".)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>Marjona speaks English very ___.</strong></p>",
        "choices": ["well", "good", "goodly", "better"],
        "correct": "well",
        "explanation": "<p><strong>well</strong> is correct. <em>good</em> is an adjective; its adverb is "
                       "the irregular <em>well</em>, not <em>goodly</em>.<br><br>"
                       "<em>(<em>good</em> — sifat; uning ravishi notoʻgʻri shakldagi <em>well</em>, "
                       "<em>goodly</em> emas.)</em></p>",
    },
    {
        "text": "<p>Which sentence is a compliment?</p>",
        "choices": [
            "He hardly works.",
            "He works hardly.",
            "He works hard.",
            "He hard works.",
        ],
        "correct": "He works hard.",
        "explanation": "<p><strong>He works hard.</strong> is the compliment — it means he puts in a lot "
                       "of effort. <em>Hardly</em> means \"almost not\", so <em>He hardly works</em> is "
                       "criticism. One <em>-ly</em> reverses the whole meaning.<br><br>"
                       "<em>(<em>hard</em> = \"qattiq, tirishib\" — maqtov. <em>hardly</em> = \"deyarli "
                       "emas\" — tanqid. Bitta <em>-ly</em> butun maʼnoni oʻzgartiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct option.</p>"
                "<p><strong>___, Firdavs has been feeling very tired.</strong> (= recently)</p>",
        "choices": ["Late", "Later", "Latest", "Lately"],
        "correct": "Lately",
        "explanation": "<p><strong>Lately</strong> is correct — it means \"recently\". <em>Late</em> "
                       "means \"not on time\", so this is another pair where the <em>-ly</em> changes "
                       "the meaning completely.<br><br>"
                       "<em>(<em>Lately</em> — \"soʻnggi paytda\", <em>late</em> — \"kech\". Bu ham "
                       "<em>-ly</em> maʼnoni butunlay oʻzgartiradigan juftlik.)</em></p>",
    },
    {
        "text": "<p>Choose the correct form.</p>"
                "<p><strong>The ___ between the two answers is big.</strong> (differ)</p>",
        "choices": ["different", "differently", "differ", "difference"],
        "correct": "difference",
        "explanation": "<p><strong>difference</strong> is correct. After <em>The</em> a noun is needed; "
                       "<em>different</em> is the adjective.<br><br>"
                       "<em>(<em>The</em> dan keyin ot kerak; <em>different</em> esa "
                       "sifat.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "It's impossible to finish today.",
            "It's unpossible to finish today.",
            "Iroda is a careful driver.",
            "Iroda drives carefully.",
        ],
        "correct": "It's unpossible to finish today.",
        "explanation": "<p><strong>It's unpossible to finish today.</strong> is the mistake — the correct "
                       "prefix is <em>im-</em>: <em>impossible</em>.<br><br>"
                       "<em>(Toʻgʻri prefiks — <em>im-</em>: <em>impossible</em>. <em>unpossible</em> "
                       "degan soʻz yoʻq.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "She speaks English very good.",
            "The different between them is big.",
            "I disagree with your decide.",
            "He is a very successful businessman.",
        ],
        "correct": "He is a very successful businessman.",
        "explanation": "<p><strong>He is a very successful businessman.</strong> is correct. The others "
                       "put the wrong word class in the slot: an adjective where an adverb belongs, and "
                       "adjectives and verbs where nouns belong.<br><br>"
                       "<em>(Qolganlarida soʻz turkumi notoʻgʻri tanlangan: ravish oʻrniga sifat, ot "
                       "oʻrniga sifat va feʼl qoʻyilgan.)</em></p>",
    },
    {
        "text": "<p>Which row is the correct word family for <strong>to decide</strong>?</p>",
        "choices": [
            "decide — decision — decisive — decisively",
            "decide — deciding — decided — decidely",
            "decide — decidement — decisional — decisely",
            "decide — decider — decideful — decidly",
        ],
        "correct": "decide — decision — decisive — decisively",
        "explanation": "<p>The first row is correct: verb, noun, adjective, adverb. Learning every new "
                       "word with its whole family is the fastest way to grow your vocabulary — and "
                       "exams ask for exactly this.<br><br>"
                       "<em>(Feʼl, ot, sifat, ravish. Har bir yangi soʻzni butun oilasi bilan oʻrganish "
                       "— lugʻatni oshirishning eng tez yoʻli, va imtihonlarda aynan shu "
                       "soʻraladi.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> How was Charos's presentation?</p>"
                "<p><strong>Abdulloh:</strong> ___</p>",
        "choices": [
            "It was absolutely success and she spoke very good.",
            "It was a great success and she spoke very well.",
            "It was a great successful and she spoke very good.",
            "It was a great succeed and she spoke very well.",
        ],
        "correct": "It was a great success and she spoke very well.",
        "explanation": "<p><strong>It was a great success and she spoke very well.</strong> is correct — "
                       "a noun after <em>a great</em>, and the adverb <em>well</em> after the verb "
                       "<em>spoke</em>.<br><br>"
                       "<em>(<em>a great</em> dan keyin ot, <em>spoke</em> feʼlidan keyin esa ravish "
                       "<em>well</em>.)</em></p>",
    },
]


# =====================================================================
# PE-90 — Collocations: Words That Live Together
# =====================================================================
Q_PE90 = [
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Afsona ___ her homework every evening.</strong></p>",
        "choices": ["makes", "does", "takes", "gives"],
        "correct": "does",
        "explanation": "<p><strong>does</strong> is correct. Homework is an activity or duty, and "
                       "<em>do</em> is the verb for activities: <em>do homework, do the shopping, do "
                       "exercise</em>.<br><br>"
                       "<em>(Uy vazifasi — mashgʻulot yoki vazifa, mashgʻulotlar uchun esa <em>do</em> "
                       "ishlatiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Sorry, I ___ a mistake in the last question.</strong></p>",
        "choices": ["made", "did", "took", "had"],
        "correct": "made",
        "explanation": "<p><strong>made</strong> is correct. <em>make a mistake</em> is the fixed "
                       "partnership. <em>Do a mistake</em> is understandable but no English speaker "
                       "says it.<br><br>"
                       "<em>(<em>make a mistake</em> — qatʼiy juftlik. Oʻzbekchada \"xato "
                       "<strong>qilmoq</strong>\" deymiz, shuning uchun <em>do</em> deb tarjima qilish "
                       "oson — lekin bu notoʻgʻri.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Can you ___ a photo of us, please?</strong></p>",
        "choices": ["make", "do", "take", "give"],
        "correct": "take",
        "explanation": "<p><strong>take</strong> is correct — <em>take a photo</em> is fixed, like "
                       "<em>take a taxi, take an exam, take a break</em>.<br><br>"
                       "<em>(<em>take a photo</em> — qatʼiy juftlik, <em>take a taxi, take an exam, take "
                       "a break</em> kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Please ___ attention to the board, everybody.</strong></p>",
        "choices": ["make", "do", "give", "pay"],
        "correct": "pay",
        "explanation": "<p><strong>pay</strong> is correct. <em>pay attention</em> is a fixed "
                       "partnership, along with <em>pay a visit</em> and <em>pay a "
                       "compliment</em>.<br><br>"
                       "<em>(<em>pay attention</em> — qatʼiy juftlik, <em>pay a visit</em>, <em>pay a "
                       "compliment</em> kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>We must ___ a decision before Friday.</strong></p>",
        "choices": ["do", "make", "take", "get"],
        "correct": "make",
        "explanation": "<p><strong>make</strong> is correct. A decision is something you produce, so it "
                       "goes with <em>make</em> — British English strongly prefers <em>make a "
                       "decision</em> to <em>take a decision</em>.<br><br>"
                       "<em>(Qaror — siz yaratadigan narsa, shuning uchun <em>make</em> bilan keladi. "
                       "Britaniya ingliz tilida <em>make a decision</em> afzal koʻriladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Behruz wants to ___ some exercise before dinner.</strong></p>",
        "choices": ["do", "make", "take", "pay"],
        "correct": "do",
        "explanation": "<p><strong>do</strong> is correct — exercise is an activity, so it belongs to the "
                       "<em>do</em> family: <em>do exercise, do the washing-up, do "
                       "research</em>.<br><br>"
                       "<em>(Mashq — faoliyat, shuning uchun u <em>do</em> oilasiga kiradi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Iroda is ___ good progress in English this year.</strong></p>",
        "choices": ["doing", "taking", "making", "getting"],
        "correct": "making",
        "explanation": "<p><strong>making</strong> is correct. <em>make progress</em> belongs with "
                       "<em>make an effort</em> and <em>make a plan</em> — things you produce.<br><br>"
                       "<em>(<em>make progress</em> — <em>make an effort</em>, <em>make a plan</em> bilan "
                       "bir oilada: bular siz yaratadigan narsalar.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Let's ___ a break for ten minutes.</strong></p>",
        "choices": ["make", "do", "give", "take"],
        "correct": "take",
        "explanation": "<p><strong>take</strong> is correct — <em>take a break</em>, like <em>take "
                       "care</em> and <em>take medicine</em>.<br><br>"
                       "<em>(<em>take a break</em> — <em>take care</em>, <em>take medicine</em> "
                       "kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Could you ___ Shaxzoda some advice about the exam?</strong></p>",
        "choices": ["give", "do", "make", "take"],
        "correct": "give",
        "explanation": "<p><strong>give</strong> is correct — <em>give advice</em>, like <em>give a "
                       "lift</em>, <em>give a speech</em> and <em>give an example</em>. Note "
                       "<em>advice</em> is uncountable, so <em>some advice</em> and never <em>an "
                       "advice</em> (PE-2).<br><br>"
                       "<em>(<em>give advice</em> — <em>give a lift</em>, <em>give a speech</em> kabi. "
                       "<em>advice</em> sanalmaydigan ot, shuning uchun <em>some advice</em> deyiladi, "
                       "<em>an advice</em> emas.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Sherbek hopes to ___ a job in Tashkent after university.</strong></p>",
        "choices": ["make", "get", "do", "pay"],
        "correct": "get",
        "explanation": "<p><strong>get</strong> is correct — <em>get a job</em>, like <em>get married, "
                       "get dressed, get lost, get better</em>.<br><br>"
                       "<em>(<em>get a job</em> — <em>get married, get dressed, get lost, get better</em> "
                       "kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Please ___ in touch when you arrive in Nukus.</strong></p>",
        "choices": ["make", "do", "keep", "take"],
        "correct": "keep",
        "explanation": "<p><strong>keep</strong> is correct — <em>keep in touch</em>, like <em>keep a "
                       "secret, keep calm, keep a promise</em>.<br><br>"
                       "<em>(<em>keep in touch</em> — <em>keep a secret, keep calm, keep a promise</em> "
                       "kabi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct verb.</p>"
                "<p><strong>Charos and Davron ___ an important exam tomorrow morning.</strong></p>",
        "choices": ["make", "do", "give", "take"],
        "correct": "take",
        "explanation": "<p><strong>take</strong> is correct — the student <em>takes</em> an exam, while "
                       "the teacher <em>gives</em> or <em>sets</em> one.<br><br>"
                       "<em>(Oʻquvchi imtihonni <em>take</em> qiladi, oʻqituvchi esa uni <em>give</em> "
                       "qiladi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct pair.</p>"
                "<p><strong>There was ___ rain and ___ traffic yesterday, so Javohir was late.</strong></p>",
        "choices": ["strong / big", "big / strong", "heavy / heavy", "high / heavy"],
        "correct": "heavy / heavy",
        "explanation": "<p><strong>heavy / heavy</strong> is correct. English says <em>heavy rain</em> "
                       "and <em>heavy traffic</em> — <em>strong rain</em> and <em>big traffic</em> are "
                       "grammatically fine but nobody says them.<br><br>"
                       "<em>(Ingliz tilida <em>heavy rain</em> va <em>heavy traffic</em> deyiladi. "
                       "<em>strong rain</em> grammatik jihatdan toʻgʻri, lekin hech kim "
                       "aytmaydi.)</em></p>",
    },
    {
        "text": "<p>Choose the correct adjective.</p>"
                "<p><strong>Rozimurod teacher likes ___ coffee in the morning.</strong></p>",
        "choices": ["heavy", "big", "strong", "high"],
        "correct": "strong",
        "explanation": "<p><strong>strong</strong> is correct — <em>strong coffee</em> and <em>a strong "
                       "accent</em>, but <em>heavy rain</em> and <em>heavy traffic</em>. Each adjective "
                       "has its favourite nouns.<br><br>"
                       "<em>(<em>strong coffee</em>, <em>a strong accent</em>, lekin <em>heavy rain</em>, "
                       "<em>heavy traffic</em>. Har bir sifatning oʻz sevimli otlari bor.)</em></p>",
    },
    {
        "text": "<p>Choose the correct adverb.</p>"
                "<p><strong>Madina's answer was ___ perfect.</strong></p>",
        "choices": ["absolutely", "very", "highly", "deeply"],
        "correct": "absolutely",
        "explanation": "<p><strong>absolutely</strong> is correct. <em>Very</em> does not work with "
                       "absolute adjectives — something cannot be \"very perfect\". Compare "
                       "<em>completely different, highly recommended, deeply sorry</em>.<br><br>"
                       "<em>(<em>Very</em> mutlaq sifatlar bilan ishlamaydi — \"very perfect\" boʻlmaydi. "
                       "Taqqoslang: <em>completely different, highly recommended, deeply "
                       "sorry</em>.)</em></p>",
    },
    {
        "text": "<p>Which pair is correct?</p>",
        "choices": [
            "make your homework / do a decision",
            "make your homework / make a decision",
            "do your homework / do a decision",
            "do your homework / make a decision",
        ],
        "correct": "do your homework / make a decision",
        "explanation": "<p><strong>do your homework / make a decision</strong> is correct. This is the "
                       "core of the lesson: <em>do</em> for activities and duties, <em>make</em> for "
                       "things you produce.<br><br>"
                       "<em>(Darsning asosiy gʻoyasi: faoliyat va vazifalar uchun <em>do</em>, siz "
                       "yaratadigan narsalar uchun <em>make</em>.)</em></p>",
    },
    {
        "text": "<p>Which sentence has a mistake?</p>",
        "choices": [
            "I must do my homework.",
            "I must make my homework.",
            "Marjona made a big mistake.",
            "We had heavy rain yesterday.",
        ],
        "correct": "I must make my homework.",
        "explanation": "<p><strong>I must make my homework.</strong> is the mistake — homework goes with "
                       "<em>do</em>. This is the commonest collocation error of all for Uzbek "
                       "speakers.<br><br>"
                       "<em>(Uy vazifasi <em>do</em> bilan keladi. Bu — oʻzbek tilida "
                       "soʻzlashuvchilarning eng koʻp uchraydigan juftlik xatosi.)</em></p>",
    },
    {
        "text": "<p>Which sentence is correct?</p>",
        "choices": [
            "He gave me a good advice.",
            "Please make attention to the board.",
            "We had a strong rain yesterday.",
            "He gave me some good advice.",
        ],
        "correct": "He gave me some good advice.",
        "explanation": "<p><strong>He gave me some good advice.</strong> is correct. The others break "
                       "three different partnerships: <em>an advice</em> (uncountable), <em>make "
                       "attention</em> (it is <em>pay</em>) and <em>strong rain</em> (it is "
                       "<em>heavy</em>).<br><br>"
                       "<em>(Qolganlarida uchta juftlik buzilgan: <em>an advice</em> (sanalmaydigan ot), "
                       "<em>make attention</em> (toʻgʻrisi <em>pay</em>) va <em>strong rain</em> "
                       "(toʻgʻrisi <em>heavy</em>).)</em></p>",
    },
    {
        "text": "<p>Correct this sentence: <strong>I want to make some exercise and take a decision "
                "about my future.</strong></p>",
        "choices": [
            "I want to do some exercise and make a decision about my future.",
            "I want to make some exercise and make a decision about my future.",
            "I want to do some exercise and take a decision about my future.",
            "I want to take some exercise and do a decision about my future.",
        ],
        "correct": "I want to do some exercise and make a decision about my future.",
        "explanation": "<p>The first version is correct: <em>do exercise</em> (an activity) and "
                       "<em>make a decision</em> (something you produce).<br><br>"
                       "<em>(<em>do exercise</em> — faoliyat, <em>make a decision</em> — siz yaratadigan "
                       "narsa.)</em></p>",
    },
    {
        "text": "<p>Complete the dialogue.</p>"
                "<p><strong>Rozimurod teacher:</strong> Why were you late this morning, Elbek?</p>"
                "<p><strong>Elbek:</strong> ___</p>",
        "choices": [
            "Sorry, I did a mistake with the bus times — I'll make my best tomorrow.",
            "Sorry, I made a mistake with the bus times — I'll do my best tomorrow.",
            "Sorry, I made a mistake with the bus times — I'll make my best tomorrow.",
            "Sorry, I did a mistake with the bus times — I'll do my best tomorrow.",
        ],
        "correct": "Sorry, I made a mistake with the bus times — I'll do my best tomorrow.",
        "explanation": "<p><strong>Sorry, I made a mistake with the bus times — I'll do my best "
                       "tomorrow.</strong> is correct. Two fixed partnerships in one sentence: "
                       "<em>make a mistake</em> and <em>do your best</em>.<br><br>"
                       "<em>(Bitta gapda ikkita qatʼiy juftlik: <em>make a mistake</em> va <em>do your "
                       "best</em>.)</em></p>",
    },
]


PRACTICES = [
    {
        "title":       "PE-86 Practice: Participle Clauses",
        "tutorial":    "PE-86:",
        "description": "PE-86 darsiga 20 savol: -ing (aniq) va -ed / V3 (majhul) oborotlar, "
                       "Having + V3, egasiz ravishdosh xatosi va bu qurilma qayerda ishlatilishi. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE86,
    },
    {
        "title":       "PE-87 Practice: The Unreal Past: It's time, would rather, as if",
        "tutorial":    "PE-87:",
        "description": "PE-87 darsiga 20 savol: It's time + oʻtgan zamon, would rather ning ikki "
                       "qurilmasi, as if / as though va \"I'd rather you didn't\" muloyim rad javobi. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE87,
    },
    {
        "title":       "PE-88 Practice: Linking Words for Writing: however, therefore, although",
        "tutorial":    "PE-88:",
        "description": "PE-88 darsiga 20 savol: bogʻlovchi soʻzlarning besh oilasi, ularning tinish "
                       "belgilari va although / despite / however orasidagi grammatik farq. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE88,
    },
    {
        "title":       "PE-89 Practice: Word Formation: Prefixes and Suffixes",
        "tutorial":    "PE-89:",
        "description": "PE-89 darsiga 20 savol: un- / im- / ir- / il- / dis- prefikslari, soʻz "
                       "turkumini oʻzgartiruvchi suffikslar, soʻz oilalari va hard / hardly kabi "
                       "tuzoqlar. Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE89,
    },
    {
        "title":       "PE-90 Practice: Collocations: Words That Live Together",
        "tutorial":    "PE-90:",
        "description": "PE-90 darsiga 20 savol: make yoki do, have / take / get / give / pay "
                       "juftliklari, heavy rain va strong coffee kabi sifat + ot birikmalari. "
                       "Har bir javob ingliz va oʻzbek tilida izohlanadi.",
        "questions":   Q_PE90,
    },
]
