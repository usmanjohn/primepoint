# -*- coding: utf-8 -*-
"""Prime English Readings — PE-46 … PE-50 (batch 10). The rest of the modals.

PE-46 should / ought to / had better · PE-47 modals of deduction (must be / can't be /
might be) · PE-48 past modals (must have / should have / could have) · PE-49 polite
requests, offers, permission · PE-50 shall / will / would.

Shapes:
  46 — a life story: eleven pieces of advice on the back of a bus ticket, and the one
       that was underlined twice
  47 — a small mystery in a school yard: four pupils deduce who the stranger is, and
       the photograph in the corridor answers them
  48 — first-person regret that turns into luck: a dead phone, the wrong bus, and the
       one evening the narrator was glad he had not charged it
  49 — a trial day at a hotel desk: two candidates, one job, and one polite question
  50 — a Bukhara tea-house waiter who would not take a tip for thirty years, and the
       envelope he finally took

Cumulative rule: no conditionals (PE-53+), no `wish` (PE-57), no `which` / non-defining
relative clauses (PE-58/59), no passive (PE-60), no reported speech with backshift
(PE-62 — direct quotes only), no `as … as` / `too` / `enough` (PE-67/68).
PE-47 stays out of `must have + V3` on purpose — that is PE-48's whole lesson, and
PE-48 is built on it. PE-49 avoids `shall`, which belongs to PE-50.
Length: 250–290 words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_46_50.py --author=prime
"""

SUBJECT = {
    "name":    "English",
    "summary": "Ingliz tili: IELTS uslubidagi qiziqarli oʻqish matnlari — lugʻat va grammatika bilan.",
    "icon":    "bi-globe2",
    "color":   "#2563eb",
    "order":   2,
}

COLLECTION = {
    "title":       "Prime English Readings",
    "description": (
        "Prime English darslarining oʻqish matnlari — har bir matn oʻz darsining "
        "grammatikasini jonli holda koʻrsatadi. Lugʻat izohlari va audio bilan."
    ),
    "order":       6,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PE-46 — should / ought to / had better  (the underlined line)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Advice from the Older Cousin",
        "summary": (
            "PE-46 matni. Opasi avtobus chiptasining orqasiga oʻn bitta "
            "maslahat yozib berdi. Oʻntasi oddiy edi — bittasi ostiga "
            "ikki marta chizilgan edi. Noyabr kechasi aynan oʻsha kerak boʻldi."
        ),
        "order":   46,
        "grammar": [
            {
                "pattern":  "should / ought to — ordinary advice",
                "meaning":  "<b>should</b> — kundalik maslahat: "
                            "<i>You <b>should</b> keep your money in two "
                            "pockets</i>. <b>ought to</b> — xuddi shu "
                            "maʼno, biroz rasmiyroq. Ikkisidan keyin "
                            "ham <b>V1</b> keladi (<i>to</i> faqat "
                            "<i>ought</i> bilan).",
                "examples": ["You should eat something before you study.",
                             "You ought to learn the number of the last bus."],
            },
            {
                "pattern":  "had better — advice with a warning",
                "meaning":  "<b>had better</b> (+ V1) — “shunday qilsang "
                            "yaxshi boʻladi, aks holda yomon boʻladi”. "
                            "Ichida ogohlantirish bor, shuning uchun u "
                            "<i>should</i> dan kuchli. Nutqda deyarli "
                            "har doim <b>'d better</b>. Inkori — "
                            "<b>had better not</b>, <i>hadn't better</i> emas.",
                "examples": ["You had better learn the name of your own street.",
                             "You'd better not lose that ticket."],
            },
            {
                "pattern":  "The strength scale",
                "meaning":  "<i>You could ask her</i> (bir variant) → "
                            "<i>You <b>should</b> ask her</i> (maslahat) → "
                            "<i>You'<b>d better</b> ask her</i> "
                            "(ogohlantirish) → <i>You <b>must</b> ask her</i> "
                            "(majburiyat). Bir xil gap, toʻrt xil kuch — "
                            "shuning uchun <b>had better</b> ni har kuni "
                            "ishlatilmaydi, uni asrab qoʻyiladi.",
                "examples": ["You could take the bus.",
                             "You should take the bus.",
                             "You'd better take the bus — the taxi costs a week's food."],
            },
        ],
        "body": '''<p>When Sherbek left the village for Tashkent, his cousin Nigora met him at the bus station with a bag of bread and a list.</p>

<p>She had written it on the back of a bus <span class="cn-word" data-tr="chipta">ticket</span>, in small letters, on both sides. Eleven pieces of <span class="cn-word" data-tr="maslahat">advice</span>. Nigora is twenty-four and works nights at a hospital, so she knows the city at the hour when nobody else is awake.</p>

<p>"You <strong>should</strong> keep your money in two pockets, not one," she said. "You <strong>ought to</strong> learn the number of the last bus. You <strong>should</strong> eat something before you study, not after."</p>

<p>Ten of them were like that: <span class="cn-word" data-pos="adj" data-tr="aqlga muvofiq">sensible</span>, boring, easy to forget. The eleventh she had <span class="cn-word" data-pos="verb" data-tr="tagiga chizgan">underlined</span> twice, and she read it out loud at the gate of the station.</p>

<p><i>"You <strong>had better</strong> learn the name of your own street. The real name, and the old name too."</i></p>

<p>Sherbek laughed. He knew his street perfectly. The bakery, the blue <span class="cn-word" data-tr="darvoza">gate</span>, the tall tree, the third <span class="cn-word" data-tr="burilish">turning</span>.</p>

<p>In November his phone died at half past one in the morning. He had missed the last bus, every shop was <span class="cn-word" data-pos="adj" data-tr="yopiq">shut</span>, and a taxi driver stopped and asked him one question: which street?</p>

<p>The bakery. The blue gate. The tall tree. At night, from the back seat of a car, none of that is an <span class="cn-word" data-tr="manzil">address</span>. They drove for forty minutes through streets that all looked the same, and the <span class="cn-word" data-tr="taksometr">meter</span> counted every one of them. He walked the last part and found his gate at four.</p>

<p>That ticket is in his <span class="cn-word" data-tr="hamyon">wallet</span> now, <span class="cn-word" data-pos="adj" data-tr="toʻrt buklangan">folded in four</span>. Nine of the eleven he still <span class="cn-word" data-pos="verb" data-tr="eʼtiborsiz qoldiradi">ignores</span>.</p>

<p>But in March his own brother arrived at that station, and Sherbek was standing there with bread and a list of one line. "You <strong>had better</strong> learn the name of your street," he said, and he <span class="cn-word" data-pos="verb" data-tr="tagiga chizdi">underlined</span> it twice while the boy watched.</p>''',
        "questions": [
            {
                "text": "Why was the eleventh piece of advice different?",
                "choices": [
                    "It was the only one Nigora underlined, and the only one Sherbek needed that night",
                    "It was the only one about money",
                    "It was written on the front of the ticket",
                ],
                "answer": 0,
                "explanation": "Oʻn maslahat oddiy edi; oʻn birinchisining "
                               "tagiga ikki marta chizilgan, va noyabr "
                               "kechasi aynan oʻsha yetmadi.",
            },
            {
                "text": "\"You had better learn the name of your street\" is stronger than \"You should learn it\" because:",
                "choices": [
                    "it is more polite",
                    "there is a warning inside it — something bad will happen if you don't",
                    "it is about the past",
                ],
                "answer": 1,
                "explanation": "<b>had better</b> ichida ogohlantirish bor: "
                               "“aks holda yomon boʻladi”. <b>should</b> — "
                               "shunchaki maslahat, ogohlantirish emas.",
            },
            {
                "text": "Which sentence is correct English?",
                "choices": [
                    "You had better to take the bus.",
                    "You hadn't better take the bus.",
                    "You'd better not take that taxi.",
                ],
                "answer": 2,
                "explanation": "<b>had better</b> dan keyin <i>to</i> "
                               "qoʻyilmaydi, inkori esa <b>had better "
                               "not</b> — <i>hadn't better</i> degan shakl "
                               "yoʻq.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-47 — must be / can't be / might be  (the school-yard deduction)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "He Must Be the New Teacher",
        "summary": (
            "PE-47 matni. Sentyabrning birinchi kuni: hovlida notanish "
            "odam turadi va toʻrtta oʻquvchi uning kimligini "
            "dalillarga qarab topmoqchi. Javob koridordagi 1994-yilgi "
            "suratda yozilgan edi."
        ),
        "order":   47,
        "grammar": [
            {
                "pattern":  "must be / might be / can't be — how sure you are",
                "meaning":  "Bu modallar kelasi zamon emas, <b>ishonch "
                            "darajasi</b>ni bildiradi. <b>must be</b> — "
                            "“shu boʻlsa kerak” (dalil bor, 95%), "
                            "<b>might / may / could be</b> — “boʻlishi "
                            "mumkin” (50%), <b>can't be</b> — “boʻlishi "
                            "mumkin emas” (dalil qarshi, 0%).",
                "examples": ["He must be a teacher — he is holding a register.",
                             "He might be somebody's father.",
                             "He can't be an inspector — inspectors come in October."],
            },
            {
                "pattern":  "The trap: can't be, NOT mustn't be",
                "meaning":  "<b>must be</b> ning teskarisi — "
                            "<b>can't be</b>. <i>mustn't</i> esa "
                            "<b>taqiq</b> (PE-45), taxmin emas: "
                            "<i>He mustn't be a teacher</i> — “unga "
                            "oʻqituvchi boʻlish taqiqlanadi” degan "
                            "gʻalati maʼno chiqadi.",
                "examples": ["That can't be his car.",
                             "She can't be at home — the lights are off."],
            },
            {
                "pattern":  "Guessing about actions: must be + V-ing",
                "meaning":  "Harakat haqida taxmin qilinsa, "
                            "modal + <b>be + V-ing</b>: <i>He <b>must be "
                            "waiting</b> for somebody</i>, <i>She "
                            "<b>might be looking</b> for room 8-B</i>. "
                            "Holat uchun esa oddiy <b>be</b>: "
                            "<i>He must be new here</i>.",
                "examples": ["He must be waiting for the director.",
                             "They might be looking at the noticeboard."],
            },
        ],
        "body": '''<p>On the first morning of September a man in a grey jacket stood in the school yard, reading the <span class="cn-word" data-tr="eʼlonlar taxtasi">noticeboard</span>. Four of us watched him from the steps.</p>

<p>"He <strong>must be</strong> a teacher," Dilnoza said. "Look — he is holding a <span class="cn-word" data-tr="sinf jurnali">register</span>."</p>

<p>"He <strong>can't be</strong> a teacher," Bekzod said. "Teachers do not read the noticeboard. They write on it."</p>

<p>"He <strong>might be</strong> somebody's father," I said. "Or he <strong>could be</strong> an <span class="cn-word" data-tr="inspektor, tekshiruvchi">inspector</span>."</p>

<p>"Inspectors come in October," Bekzod said, and he was right about that. "He <strong>must be</strong> the new teacher. Ours left in June, and somebody has to teach 8-B on Monday."</p>

<p>The man walked past us into the building. He did not ask the way, which was strange. In our <span class="cn-word" data-tr="koridor">corridor</span> there is a long photograph from 1994 — a class of <span class="cn-word" data-tr="bitiruvchilar">graduates</span> in front of the same tree, and one boy in the middle holding a <span class="cn-word" data-tr="diplom, guvohnoma">certificate</span>. He stopped in front of it for a long time.</p>

<p>Then he went into 8-B, put down the register, and wrote his name on the board with a piece of <span class="cn-word" data-tr="boʻr">chalk</span>: <i>Karimov O.</i></p>

<p>Dilnoza was already <span class="cn-word" data-pos="verb" data-tr="shivirlab">whispering</span>. The name under the boy in the photograph is Karimov O.</p>

<p>"That desk by the window is mine," he said. "It was mine for two years. The <span class="cn-word" data-tr="oyna, shisha">glass</span> is still <span class="cn-word" data-pos="adj" data-tr="siniq">broken</span> in the same corner."</p>

<p>He had not come for a job at all. He had come to see whether the tree in the yard was still alive, and the director found him at the noticeboard and asked him one question.</p>

<p>So Bekzod was right: the man in the grey jacket <strong>must be</strong> the new teacher. He simply <strong>wasn't</strong> one yet when Bekzod said it.</p>''',
        "questions": [
            {
                "text": "Why had the man really come to the school?",
                "choices": [
                    "To apply for a job in 8-B",
                    "To see whether the tree in the yard was still alive",
                    "Because he was an inspector",
                ],
                "answer": 1,
                "explanation": "U ish uchun kelmagan edi — hovlidagi "
                               "daraxt tirikmi, yoʻqmi, koʻrgani kelgan. "
                               "Direktor uni eʼlonlar taxtasi oldida "
                               "koʻrib qoldi.",
            },
            {
                "text": "\"He can't be a teacher\" means the speaker thinks:",
                "choices": [
                    "it is impossible that he is a teacher",
                    "he is not allowed to be a teacher",
                    "maybe he is a teacher",
                ],
                "answer": 0,
                "explanation": "<b>can't be</b> — “boʻlishi mumkin emas”, "
                               "yaʼni ishonch bilan rad etish. Taqiq "
                               "boʻlsa <i>mustn't</i> boʻlar edi, lekin "
                               "bu yerda taxmin haqida gap ketmoqda.",
            },
            {
                "text": "Which sentence correctly guesses about an action happening now?",
                "choices": [
                    "He must waiting for the director.",
                    "He must be waiting for the director.",
                    "He mustn't be the director.",
                ],
                "answer": 1,
                "explanation": "Harakat uchun formula — modal + "
                               "<b>be + V-ing</b>: <i>must be waiting</i>. "
                               "Uchinchi variant taxmin emas, taqiq "
                               "maʼnosini beradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-48 — must have / should have / could have  (the dead phone)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "I Should Have Charged My Phone",
        "summary": (
            "PE-48 matni. Telefon oʻchdi, avtobus notoʻgʻri boʻldi, "
            "yomgʻir yogʻdi. “Telefonni quvvatlashim kerak edi” — deb "
            "oʻsha kecha yigirma marta aytdim. Va bu — hayotimda "
            "oʻsha gap notoʻgʻri boʻlgan yagona kecha."
        ),
        "order":   48,
        "grammar": [
            {
                "pattern":  "should have + V3 — regret and criticism",
                "meaning":  "Oʻtgan ish qilinmagan, lekin qilish kerak "
                            "edi: <i>I <b>should have charged</b> my "
                            "phone</i> — quvvatlamadim, afsusdaman. "
                            "Inkori <b>shouldn't have + V3</b> — "
                            "qildim, lekin qilmasligim kerak edi.",
                "examples": ["I should have charged my phone.",
                             "I shouldn't have left the charger at home."],
            },
            {
                "pattern":  "must have + V3 — deduction about the past",
                "meaning":  "Oʻtgan voqea haqida ishonchli taxmin: "
                            "<i>Somebody <b>must have taken</b> my "
                            "charger</i> — “olgan boʻlsa kerak”. "
                            "Teskarisi — <b>can't have + V3</b> "
                            "(<i>mustn't have</i> emas!).",
                "examples": ["Somebody must have taken the charger.",
                             "She can't have seen my message — my phone was dead."],
            },
            {
                "pattern":  "could have + V3 — the missed possibility",
                "meaning":  "Imkoni bor edi, lekin boʻlmadi: "
                            "<i>I <b>could have asked</b> the driver</i> "
                            "— soʻrashim mumkin edi, soʻramadim. "
                            "Uchtasi bir formulada: <b>modal + have + "
                            "V3</b>, va nutqda hammasi qisqaradi — "
                            "<i>should've</i>, <i>must've</i>, "
                            "<i>could've</i> (“shudov”, “mastov”, “kudov”).",
                "examples": ["I could have asked the driver.",
                             "He could have called from a shop."],
            },
        ],
        "body": '''<p>Ten <span class="cn-word" data-tr="foiz">per cent</span>. I saw the number at the bus stop, and I did nothing about it.</p>

<p>I was going to my aunt's flat on the other side of the city, and I had been there twice — but both times with the map open in my hand. The phone died between two stops, in the middle of a sentence.</p>

<p>Bus 44 is not bus 14. I know that now. I sat there for fifty minutes with the <span class="cn-word" data-tr="qora ekran">black screen</span> in my pocket, and I got off at the <span class="cn-word" data-tr="oxirgi bekat">last stop</span>, in a <span class="cn-word" data-tr="tuman, mahalla">district</span> whose name I had never even heard. Then it started to rain.</p>

<p>"I <strong>should have charged</strong> my phone," I said <span class="cn-word" data-tr="ovoz chiqarib">out loud</span>, to nobody. "I <strong>shouldn't have</strong> left the <span class="cn-word" data-tr="quvvatlagich">charger</span> on the table. Somebody <strong>must have moved</strong> it — I put it in the bag myself." (Nobody had moved it. It was on the table.)</p>

<p>I <strong>could have asked</strong> the driver. I did not want to look like a boy from a village on his third day in the city, so I walked instead, <span class="cn-word" data-pos="adj" data-tr="shilta boʻlgan">soaked</span> to the shoulders, past shut gates.</p>

<p>At the end of that street one window was still <span class="cn-word" data-pos="adj" data-tr="yoritilgan">lit</span>: a tiny bookshop, and an old woman carrying <span class="cn-word" data-tr="qutilar">boxes</span> out to a car in the rain, one box at a time. I carried the rest. It took eleven minutes.</p>

<p>She gave me tea in a plastic cup and asked whether I could read English. Her <span class="cn-word" data-tr="nabira">grandson</span> had an exam in April and nobody in the family could help him with it.</p>

<p>I have taught in the <span class="cn-word" data-tr="orqa xona">back room</span> of that bookshop two evenings a week for a year and a half. It pays for my own books.</p>

<p>So: I <strong>should have charged</strong> my phone. I have said that sentence a hundred times in my life, and that was the only night it was <span class="cn-word" data-pos="adj" data-tr="notoʻgʻri">wrong</span>.</p>''',
        "questions": [
            {
                "text": "Why does the narrator say that sentence was \"wrong\" that night?",
                "choices": [
                    "Because the phone was not really dead",
                    "Because the dead phone is the only reason he found the bookshop and the teaching work",
                    "Because he had charged it after all",
                ],
                "answer": 1,
                "explanation": "Telefon oʻchmasa, u 44-avtobusga chiqmas, "
                               "oʻsha koʻchaga bormas va kitob doʻkonini "
                               "topmas edi. Afsus baxtga aylandi.",
            },
            {
                "text": "\"Somebody must have moved it\" means:",
                "choices": [
                    "he is fairly sure somebody moved it",
                    "somebody was allowed to move it",
                    "somebody had to move it",
                ],
                "answer": 0,
                "explanation": "<b>must have + V3</b> — oʻtgan zamon "
                               "haqida ishonchli taxmin: “koʻchirgan "
                               "boʻlsa kerak”. Bu majburiyat emas.",
            },
            {
                "text": "Which sentence means \"he had the chance but did not do it\"?",
                "choices": [
                    "He must have asked the driver.",
                    "He should ask the driver.",
                    "He could have asked the driver.",
                ],
                "answer": 2,
                "explanation": "<b>could have + V3</b> — imkoniyat bor edi, "
                               "lekin amalga oshmadi. <i>must have</i> — "
                               "taxmin, <i>should ask</i> — hozirgi "
                               "maslahat.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-49 — polite requests, offers, permission  (the trial day)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Could You Say That Again, Please?",
        "summary": (
            "PE-49 matni. Samarqanddagi mehmonxonada bitta oʻrin, "
            "ikkita nomzod. Afsona mehmonning bir soʻzini ham "
            "tushunmadi va uch marta “yana bir marta aytolasizmi?” "
            "deb soʻradi. Ishga oʻsha uch savol uchun olindi."
        ),
        "order":   49,
        "grammar": [
            {
                "pattern":  "Asking somebody to do something",
                "meaning":  "Xushmuomalalik zinapoyasi: "
                            "<i><b>Can</b> you…?</i> (doʻstona) → "
                            "<i><b>Could</b> you…?</i> (odatdagi, "
                            "eng ishonchli) → <i><b>Would</b> you…?</i> "
                            "→ <i><b>Would you mind</b> + V-ing?</i> "
                            "(eng yumshoq). Har birining oxirida "
                            "<b>please</b> — bepul, lekin juda qimmatli.",
                "examples": ["Could you say that again, please?",
                             "Could you speak a little more slowly, please?",
                             "Would you mind writing it down?"],
            },
            {
                "pattern":  "Permission and offers",
                "meaning":  "Ruxsat soʻrash: <i><b>Can I</b>…?</i> — "
                            "<i><b>Could I</b>…?</i> — <i><b>May I</b>"
                            "…?</i> (eng rasmiy, mehmonxona va imtihon "
                            "tili). Taklif qilish: <i><b>Would you "
                            "like</b> some tea?</i> va <i><b>Would you "
                            "like me to</b> call a taxi?</i> — "
                            "<i>Do you want…?</i> dan ancha muloyim.",
                "examples": ["May I take your bag?",
                             "Would you like me to write the address down?"],
            },
            {
                "pattern":  "The Would you mind…? trap",
                "meaning":  "<b>Would you mind…?</b> — “malol "
                            "kelmaydimi?”. Shuning uchun <b>No, not at "
                            "all</b> = “mayli, qilaman”, "
                            "<i>Yes, I do mind</i> esa rad javobi. "
                            "Roziligni <b>No</b> bilan aytish — "
                            "inglizchaning eng gʻalati burilishi.",
                "examples": ['"Would you mind waiting five minutes?" — "No, not at all."',
                             "Would you mind if I opened the window?"],
            },
        ],
        "body": '''<p>One place, two <span class="cn-word" data-tr="nomzod">candidates</span>, one <span class="cn-word" data-tr="sinov kuni">trial day</span>. That is how the small hotel behind the Registan takes on people for the front <span class="cn-word" data-tr="qabul stoli">desk</span>: you stand there for six hours on a Saturday and the manager watches from the stairs.</p>

<p>Afsona was seventeen and her English came out of a school in Kattaqoʻrgʻon and forty-one Prime English lessons.</p>

<p>At eleven o'clock a French guest arrived with two <span class="cn-word" data-tr="jomadonlar">suitcases</span> and a train ticket in his hand, and he spoke very fast, in a long line, without gaps.</p>

<p>Afsona understood the word "train" and nothing else.</p>

<p>"I'm sorry — <strong>could you say that again</strong>, please?" she said.</p>

<p>He said it again, at the same <span class="cn-word" data-tr="tezlik">speed</span>.</p>

<p>"<strong>Could you speak</strong> a little more slowly, please? <strong>Would you mind</strong> writing the time down for me?" She turned her notebook round and put a pen on it.</p>

<p>The guest stopped. He looked at her, he smiled, and he wrote: <i>06:40, Tashkent.</i> Then he said, slowly, six words: he needed a taxi at five.</p>

<p>"<strong>May I take</strong> your bag to the room? And <strong>would you like</strong> some tea while I call the driver?"</p>

<p>She sat in the kitchen afterwards and was sure she had lost the job. Three times she had asked a guest to <span class="cn-word" data-pos="verb" data-tr="takrorlash">repeat</span> himself. The other candidate had not asked anybody anything all day.</p>

<p>The manager came in at seven with two <span class="cn-word" data-tr="anketalar">forms</span> in her hand and one pen.</p>

<p>"He said 'yes, of course' to every question," she said. "A German family is standing at the airport in Tashkent this evening, at the wrong <span class="cn-word" data-tr="terminal">terminal</span>, because of that. <span class="cn-word" data-tr="xushmuomalalik">Politeness</span> is not <span class="cn-word" data-tr="bezak">decoration</span>, Afsona. It is the only <span class="cn-word" data-tr="asbob, vosita">tool</span> you have when you do not understand."</p>

<p>Afsona works there on Saturdays and Sundays. Above her desk there is a card with one sentence on it, in her own <span class="cn-word" data-tr="qoʻl yozuvi">handwriting</span>: <i>Could you say that again, please?</i></p>''',
        "questions": [
            {
                "text": "Why did the other candidate lose the job?",
                "choices": [
                    "He arrived late on the trial day",
                    "He said \"yes, of course\" to everything instead of asking, and sent a family to the wrong terminal",
                    "He spoke no English at all",
                ],
                "answer": 1,
                "explanation": "U hech kimdan hech narsa soʻramadi — "
                               "tushunmasa ham “yes, of course” dedi, "
                               "va bir nemis oilasi notoʻgʻri "
                               "terminalda qoldi.",
            },
            {
                "text": "\"Would you mind writing it down?\" — how do you AGREE?",
                "choices": [
                    "\"Yes, I would.\"",
                    "\"No, not at all.\"",
                    "\"Yes, of course I mind.\"",
                ],
                "answer": 1,
                "explanation": "<b>Would you mind…?</b> — “malol "
                               "kelmaydimi?”. Rozilik shuning uchun "
                               "<b>No, not at all</b> — “yoʻq, malol "
                               "kelmaydi”. <i>Yes</i> deyish rad javobi "
                               "boʻlib qoladi.",
            },
            {
                "text": "Which is the most polite way to ask for a repeat?",
                "choices": [
                    "Say that again.",
                    "Repeat!",
                    "Could you say that again, please?",
                ],
                "answer": 2,
                "explanation": "Buyruq shakli (<i>Say that again</i>, "
                               "<i>Repeat!</i>) inglizchada qoʻpol "
                               "eshitiladi. <b>Could you … , please?</b> "
                               "— xavfsiz, hamma joyda toʻgʻri shakl.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-50 — shall / will / would  (the waiter who refused)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Waiter Who Would Not Take a Tip",
        "summary": (
            "PE-50 matni. Buxoro choyxonasida oʻttiz yil davomida "
            "bironta ham choychaqa olmagan keksa xizmatchi. "
            "2019-yilning kuzida esa bitta konvertni oldi — "
            "sababi 1994-yilda qolgan edi."
        ),
        "order":   50,
        "grammar": [
            {
                "pattern":  "would not = refused (a past refusal)",
                "meaning":  "<b>wouldn't</b> — “xohlamadi, rozi "
                            "boʻlmadi”: <i>He <b>would not take</b> a "
                            "tip</i> — pulni olishni rad etdi. "
                            "Hozirgi zamonda <b>won't</b>: "
                            "<i>The door <b>won't</b> open</i> — "
                            "hatto narsalar ham “rozi boʻlmaydi”.",
                "examples": ["For thirty years he would not take a tip.",
                             "She won't tell anybody the recipe."],
            },
            {
                "pattern":  "will for typical behaviour",
                "meaning":  "<b>will</b> faqat kelasi zamon emas — "
                            "odatiy, takrorlanuvchi xatti-harakat ham: "
                            "<i>Every tourist <b>will</b> put a note "
                            "under the plate, and he <b>will</b> bring "
                            "it back</i>. Oʻtgan zamondagi odat uchun "
                            "esa <b>would</b> (PE-25): <i>He <b>would "
                            "carry</b> twelve teapots on one tray</i>.",
                "examples": ["Tourists will always leave money under the plate.",
                             "When he was young he would carry twelve teapots at once."],
            },
            {
                "pattern":  "shall for offers, would for politeness",
                "meaning":  "<b>Shall I…?</b> / <b>Shall we…?</b> — "
                            "faqat <i>I</i> va <i>we</i> bilan: taklif "
                            "yoki maslahat soʻrash (<i>Shall I bring "
                            "another pot?</i>). <b>Would</b> esa "
                            "muloyimlik uchun: <i><b>Would</b> you "
                            "like green or black?</i>, <i>I <b>would</b> "
                            "say twenty years</i>.",
                "examples": ["Shall I bring you another pot?",
                             "Would you like green tea or black?"],
            },
        ],
        "body": '''<p>The <span class="cn-word" data-tr="choyxona">tea-house</span> by the old pool in Bukhara has eleven tables, and for thirty years it had one waiter in the afternoons: Nodir aka, in a white shirt, with a green <span class="cn-word" data-tr="patnis">tray</span>.</p>

<p>Every tourist <strong>will</strong> do the same thing. They <strong>will</strong> drink two pots of tea, they <strong>will</strong> photograph the <span class="cn-word" data-tr="choynak">teapot</span>, and they <strong>will</strong> leave a <span class="cn-word" data-tr="banknot">note</span> under the plate on the way out. And Nodir aka <strong>will</strong> pick it up, walk to the door, and give it back.</p>

<p>He <strong>would not</strong> take a <span class="cn-word" data-tr="choychaqa">tip</span>. Not from Germans, not from Japanese <span class="cn-word" data-tr="guruhlar">groups</span>, not from the president of a bank from Tashkent who <span class="cn-word" data-pos="verb" data-tr="qatʼiy turib oldi">insisted</span> for ten minutes. "<strong>Shall I</strong> bring you another pot?" he would say. "<strong>Would</strong> you like green or black?" And nothing else.</p>

<p>When he was young he <strong>would</strong> carry twelve teapots on one tray, and the old men <strong>would</strong> argue about it all evening.</p>

<p>In October 2019 a woman from Almaty left an <span class="cn-word" data-tr="konvert">envelope</span> on table four. He carried it to the door in two fingers, the way he always did.</p>

<p>She <strong>wouldn't</strong> take it back.</p>

<p>"In 1994 my mother and I sat at that table," she said. "We had come from the station and we had eleven thousand soʻm between us. You put two plates of plov in front of us and you said somebody had already paid for that table."</p>

<p>Nodir aka stood in the doorway with the envelope in his hand.</p>

<p>"Nobody had paid," she said. "I was nine. I have known that since I was about fifteen."</p>

<p>He took it. "Then it is not a tip," he said. "It is the <span class="cn-word" data-tr="hisob, chek">bill</span>."</p>

<p>The money went into the <span class="cn-word" data-tr="tom, ustki qism">roof</span> over the two tables by the water, which <span class="cn-word" data-pos="verb" data-tr="oqardi">leaked</span> every spring. The empty envelope is in a <span class="cn-word" data-tr="ramka">frame</span> by the door, with a date on it and nothing else, and Nodir aka <strong>will not</strong> explain it to anybody who asks.</p>''',
        "questions": [
            {
                "text": "Why did Nodir aka finally take the envelope?",
                "choices": [
                    "Because it was not a tip — it was the bill for the plov nobody had paid for in 1994",
                    "Because the woman was from Almaty",
                    "Because he needed money for a new tray",
                ],
                "answer": 0,
                "explanation": "1994-yilda u toʻlanmagan osh uchun "
                               "“kimdir toʻlab qoʻygan” degan edi. "
                               "Ayolning puli — choychaqa emas, oʻsha "
                               "hisob, shuning uchun u oldi.",
            },
            {
                "text": "\"He would not take a tip\" means:",
                "choices": [
                    "he was not able to take it",
                    "he refused to take it",
                    "he used to take it",
                ],
                "answer": 1,
                "explanation": "<b>wouldn't</b> — oʻtgan zamondagi "
                               "rad etish: “olishni xohlamadi”. "
                               "Imkoniyat yoʻqligi <i>couldn't</i>, "
                               "oʻtgan odat esa <i>used to</i>.",
            },
            {
                "text": "\"Every tourist will leave a note under the plate.\" Here `will` shows:",
                "choices": [
                    "a promise about the future",
                    "what typically happens, again and again",
                    "an order",
                ],
                "answer": 1,
                "explanation": "<b>will</b> ning ikkinchi ishi — odatiy, "
                               "takrorlanuvchi xatti-harakat. Bu kelasi "
                               "zamon emas: har kuni shunday boʻladi.",
            },
        ],
    },
]
