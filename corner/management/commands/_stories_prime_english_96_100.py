# -*- coding: utf-8 -*-
"""Prime English Readings — PE-96 … PE-100 (batch 20, the last). English at work, and goodbye.

PE-96 describing · PE-97 charts & trends · PE-98 apologies & excuses · PE-99 small talk ·
PE-100 the toolkit. With this batch the collection is complete: 100 readings, all with audio.

Shapes (varied on purpose):
  96 — a MEMOIR: the room in Kokand, the café it became, and the clock that ran fast
  97 — a REPORT WITH NUMBERS: a school librarian's ten years of borrowing figures
  98 — a STORY: the borrowed camera, the apology that failed and the one that worked
  99 — a SCENE: twenty minutes at a Manchester bus stop with a stranger
  100 — a LETTER TO THE READER: the people who finish, and what to do on day 101

NARRATOR VOICE (see the toc's AUDIO section):
    96 en-US-JennyNeural · 97 en-US-GuyNeural · 98 en-US-JennyNeural
    99 en-US-GuyNeural   · 100 en-US-JennyNeural
(Batch 19 ran 3 male / 2 female, so this one flips to 2 male / 3 female.)
Generate one story at a time:
    python manage.py gen_corner_audio --collection="Prime English Readings" \
        --only 96 --voice en-US-JennyNeural

Facts: 97's numbers are one school library's own records, presented as such (not national
statistics) and internally consistent — 4,200 → 2,600 is a 38% fall; 2,800 → 4,600 a 64%
rise; 4,600 → 5,100 about 11%. 100: the Harvard/MIT study of their free online courses
(Reich & Ruipérez-Valiente, Science, 2019) reported a completion rate of about 3 per cent
for the 2017–18 courses. Everything else is the stories' own.

Cumulative rule: the whole course is free now. Length: 300–370 words. Vocabulary: 16–22.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_96_100.py --author=prime
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
    # PE-96 — describing   (the room in Kokand)                       [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Room I Grew Up In",
        "summary": (
            "PE-96 matni. Esdalik: Qoʻqondagi bolalik xonasi — gilam, deraza, "
            "oʻn daqiqa oldinda yuradigan soat. Oʻn yildan keyin uy kafega "
            "aylangan, devorda esa oʻsha soat osilib turibdi."
        ),
        "order":   96,
        "grammar": [
            {
                "pattern":  "look like vs be like — appearance or personality",
                "meaning":  "<b>What does he look like?</b> — tashqi koʻrinish "
                            "(<i>He looks like a strict man</i>). <b>What is he "
                            "like?</b> — fe'l-atvor, xarakter (<i>He was like a child "
                            "with his grandchildren</i>). <b>look + sifat</b>: "
                            "<i>He looked strict.</i>",
                "examples": ["My grandfather looked like a strict man.",
                             "But he was like a child when we played.",
                             "The room looked smaller than I remembered."],
            },
            {
                "pattern":  "describing a place or thing: opinion → size → age → colour → material + noun",
                "meaning":  "Sifatlar tartibi: <i>a <b>beautiful old red</b> carpet</i>, "
                            "<i>a <b>small wooden</b> clock</i>. Joyni tasvirlashda "
                            "<b>there was / there were</b> va joy predloglari "
                            "(<i>under the window, opposite the door</i>).",
                "examples": ["a beautiful old red carpet", "a small square window",
                             "There was a clock opposite the door."],
            },
        ],
        "body": '''<p>The room I grew up in was in my grandparents' house in Kokand, at the end of a street of <span class="cn-word" data-tr="tut">mulberry</span> trees. It had one small square window that looked onto the <span class="cn-word" data-tr="hovli">courtyard</span>, a low ceiling with a wooden <span class="cn-word" data-tr="toʻsin">beam</span> across it.</p>

<p>On the floor there was <strong>a beautiful old red carpet</strong>, so <span class="cn-word" data-pos="adj" data-tr="eskirgan">worn</span> in the middle that you could see the threads. I slept on a <span class="cn-word" data-tr="toʻshak (koʻrpacha)">mattress</span> next to the window. Opposite the door hung <strong>a small wooden clock</strong> with a brass <span class="cn-word" data-tr="mayatnik">pendulum</span>. It always ran ten minutes fast. My grandfather said this was on purpose, so that nobody in the family would ever be late.</p>

<p>My grandfather <strong>looked like</strong> a strict man. He was tall and <span class="cn-word" data-pos="adj" data-tr="suyakdor, ozgʻin">bony</span>, with a grey <span class="cn-word" data-tr="moʻylov">moustache</span> and eyebrows that met in the middle. But at home he <strong>was like</strong> a child. He built <span class="cn-word" data-tr="varraklar">kites</span> for us from newspaper, and he <span class="cn-word" data-pos="verb" data-tr="aldamoq">cheated</span> at cards so badly that even the youngest of us could catch him.</p>

<p>When I was nineteen, my grandparents died within a year of each other, and the family sold the house. I did not go back for ten years.</p>

<p>Last spring I finally did. The street still had its mulberry trees, but the house had become a café. The courtyard was full of <span class="cn-word" data-tr="stollar">tables</span> under <span class="cn-word" data-tr="soyabonlar">umbrellas</span>, and my room — I knew it at once from the beam — was now a quiet corner with two <span class="cn-word" data-tr="kreslolar">armchairs</span> and a bookshelf.</p>

<p>It <strong>looked smaller</strong> than I remembered. Rooms always do.</p>

<p>On the wall opposite the door, in exactly the same place, hung a small wooden clock.</p>

<p>I asked the <span class="cn-word" data-tr="egasi">owner</span> about it. He was a young man with flour on his <span class="cn-word" data-tr="fartuk">apron</span>. He said he had found it in the attic when he bought the house, and he had not had the heart to throw it away. "It <strong>looked like</strong> it belonged there," he said. "It's a strange clock, though. It runs ten minutes fast, and I can't <span class="cn-word" data-pos="verb" data-tr="tuzatmoq">fix</span> it."</p>

<p>I told him not to try. Then I ordered a tea, sat where my mattress used to be, and stayed until the clock said it was time to go — ten minutes before it really was.</p>''',
        "questions": [
            {
                "text": "Why did the clock run ten minutes fast, according to the grandfather?",
                "choices": [
                    "Because it was broken and nobody could fix it",
                    "So that nobody in the family would ever be late",
                    "Because it came from another country",
                ],
                "answer": 1,
                "explanation": "Bobo uni ataylab oʻn daqiqa oldinga qoʻygan: "
                               "oiladagi hech kim kechikmasin, deb.",
            },
            {
                "text": "'He looked like a strict man, but he was like a child.' What does 'was like' describe?",
                "choices": [
                    "His appearance",
                    "His personality and behaviour",
                    "His age",
                ],
                "answer": 1,
                "explanation": "<b>look like</b> — tashqi koʻrinish; <b>be like</b> — "
                               "xarakter, xulq. Bobo qattiqqoʻl koʻrinardi, lekin "
                               "uyda boladek edi.",
            },
            {
                "text": "Which order of adjectives is correct?",
                "choices": ["a red old beautiful carpet", "a beautiful old red carpet", "an old red beautiful carpet"],
                "answer": 1,
                "explanation": "Tartib: <b>fikr → yosh → rang</b>: <i>beautiful</i> "
                               "(fikr), <i>old</i> (yosh), <i>red</i> (rang).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-97 — charts & trends   (a librarian's report)                 [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "What the Numbers Said About Reading",
        "summary": (
            "PE-97 matni. Maktab kutubxonachisining oʻn yillik hisoboti: "
            "olingan kitoblar soni tushdi, qulab tushdi, keyin keskin oʻsdi. "
            "Sabab yangi kitoblar emas edi — eski kitoblar boshqacha "
            "terib qoʻyilgan edi."
        ),
        "order":   97,
        "grammar": [
            {
                "pattern":  "trend verbs + adverbs: rise sharply · fall steadily · peak · level off · recover slightly",
                "meaning":  "Oʻsish: <b>rise, increase, climb</b>; tushish: <b>fall, "
                            "drop, decline, plunge</b>; choʻqqi: <b>peak at</b>; "
                            "barqarorlashish: <b>level off</b>. Qanchalik va qanday "
                            "tezlikda: <b>sharply, dramatically</b> (kuchli), "
                            "<b>steadily, gradually</b> (bir tekis), <b>slightly</b> "
                            "(ozgina).",
                "examples": ["Borrowing fell steadily between 2015 and 2019.",
                             "It rose sharply in 2023 and peaked at 5,100 in 2024."],
            },
            {
                "pattern":  "the three prepositions: rise TO (the new level) · rise BY (the change) · FROM … TO",
                "meaning":  "<b>to</b> — yangi qiymat; <b>by</b> — farq; <b>from … to</b> — "
                            "boshlangʻich va oxirgi. <i>It fell <b>from</b> 4,200 <b>to</b> "
                            "2,600</i> — yaʼni <i>it fell <b>by</b> about 38 per cent</i>.",
                "examples": ["It fell from 4,200 to 2,600.", "It rose by 64 per cent.",
                             "It levelled off at around 5,000."],
            },
        ],
        "body": '''<p><i>Every year I write a short report on our school library for the head teacher. This year I looked back over ten years of <span class="cn-word" data-tr="kitob olish (kutubxonadan)">borrowing</span> figures, and they told a story I want to share.</i></p>

<p>In 2015 our pupils borrowed 4,200 books. Over the next four years the number <strong>fell steadily</strong>, and by 2019 it had <strong>dropped to</strong> 2,600 — a <span class="cn-word" data-tr="kamayish">decline</span> <strong>of</strong> about 38 per cent. Nobody was <span class="cn-word" data-pos="adj" data-tr="hayron qolgan">surprised</span>. Phones had arrived in every pocket, and we all assumed the <span class="cn-word" data-pos="adj" data-tr="pasayuvchi">downward</span> <span class="cn-word" data-tr="tendensiya">trend</span> would continue.</p>

<p>Then 2020 came. The school was closed for months, and borrowing <strong>plunged</strong> to just 900. In 2021 it <strong>recovered slightly</strong>, <strong>to</strong> 1,400, but the line on my <span class="cn-word" data-tr="grafik">graph</span> still pointed firmly down.</p>

<p>In September 2022 we tried one cheap <span class="cn-word" data-tr="tajriba">experiment</span>. We did not buy new books; we had no money for that. Instead, we took the two shelves nearest the entrance and turned every book on them face out, so that pupils saw the <span class="cn-word" data-tr="muqovalar">covers</span> instead of the <span class="cn-word" data-tr="kitob qirralari">spines</span>. Every Monday a different class chose which books went on those shelves, and wrote a one-line <span class="cn-word" data-tr="taqriz">review</span> on a card for each.</p>

<p>The results were <span class="cn-word" data-pos="adj" data-tr="ajoyib, diqqatga sazovor">remarkable</span>. Borrowing for 2022 <strong>rose to</strong> 2,800. In 2023 it <strong>rose sharply</strong>, <strong>by</strong> 64 per cent, <strong>to</strong> 4,600 — more than in any year since we began keeping records. It <strong>peaked at</strong> 5,100 in 2024 and <strong>levelled off</strong> at around 5,000 last year.</p>

<p>Two details in the figures matter more than the <span class="cn-word" data-tr="jami miqdorlar">totals</span>. First, nearly half of all the books borrowed since 2022 came from the two face-out shelves, which hold fewer than one per cent of our <span class="cn-word" data-tr="toʻplam, fond">collection</span>. Second, the books that pupils borrowed most were not new. Many of them had stood on our shelves, spine out and <span class="cn-word" data-pos="adj" data-tr="tegilmagan">untouched</span>, for more than a decade.</p>

<p>I do not want to claim more than the numbers show. One school is not a country, and phones have not gone away. But the graph makes one point very clearly. For years we believed that our pupils had stopped wanting to read. The figures <span class="cn-word" data-pos="verb" data-tr="koʻrsatmoq, ishora qilmoq">suggest</span> something <span class="cn-word" data-pos="adj" data-tr="kamtarroq">humbler</span>: they had simply stopped being able to see the books.</p>''',
        "questions": [
            {
                "text": "What change did the library make in September 2022?",
                "choices": [
                    "It bought hundreds of new books",
                    "It turned the books on two shelves face out and let classes choose them",
                    "It banned phones in the library",
                ],
                "answer": 1,
                "explanation": "Yangi kitob sotib olinmadi — kirish yonidagi ikki javondagi "
                               "kitoblar muqovasi bilan qoʻyildi va har dushanba "
                               "bir sinf ularni tanladi.",
            },
            {
                "text": "Borrowing went from 2,800 to 4,600. Which sentence describes this correctly?",
                "choices": [
                    "It rose to 64 per cent.",
                    "It rose by 64 per cent, to 4,600.",
                    "It rose by 4,600.",
                ],
                "answer": 1,
                "explanation": "<b>by</b> — farq (64%), <b>to</b> — yangi qiymat (4,600). "
                               "4,600 − 2,800 = 1,800; 1,800 ÷ 2,800 ≈ 64%.",
            },
            {
                "text": "Which phrase best describes what happened after 2024?",
                "choices": ["It plunged.", "It levelled off.", "It rose dramatically."],
                "answer": 1,
                "explanation": "5,100 dan taxminan 5,000 ga — deyarli oʻzgarmadi: "
                               "<b>levelled off</b> (barqarorlashdi).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-98 — apologies & excuses   (the borrowed camera)            [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Apology That Worked",
        "summary": (
            "PE-98 matni. Kamola xolasining fotoapparatini safarga olib ketib, "
            "sindirib qoʻydi. Birinchi kechirimi bahonalarga toʻla edi va "
            "ishlamadi. Ikkinchisi esa bitta gapdan boshlandi."
        ),
        "order":   98,
        "grammar": [
            {
                "pattern":  "the three sorry structures: sorry FOR + -ing · sorry (THAT) + clause · sorry TO + verb",
                "meaning":  "<b>I'm sorry for breaking</b> your camera (oʻtgan ish). "
                            "<b>I'm sorry (that) I didn't tell you</b> (toʻliq gap). "
                            "<b>I'm sorry to hear</b> that / <b>sorry to bother</b> you "
                            "(hozirgi holat). Rasmiyda: <b>I apologise for…</b>",
                "examples": ["I'm sorry for breaking your camera.",
                             "I'm sorry that I didn't tell you straight away.",
                             "I'm sorry to ask, but could I borrow it?"],
            },
            {
                "pattern":  "owning it vs excusing it; promising; accepting",
                "meaning":  "Ishonchli kechirim: <b>it was my fault</b> + tushuntirish "
                            "(bahona emas) + taklif + vaʼda: <b>I'll make sure it "
                            "doesn't happen again</b>. Bahona belgilari: <i>it wasn't "
                            "really my fault, the bag…</i> Qabul qilish: <b>Don't worry "
                            "about it</b>, <b>Apology accepted</b>.",
                "examples": ["It was my fault. I should have used the strap.",
                             "I'll pay for the repair from my summer job.",
                             "Apology accepted."],
            },
        ],
        "body": '''<p>Kamola's aunt Gulnora is a <span class="cn-word" data-tr="toʻy fotografi">wedding photographer</span>, and her camera is the most <span class="cn-word" data-pos="adj" data-tr="qimmatbaho">valuable</span> thing she owns. So when Kamola asked to borrow it for a school trip to Khiva, Gulnora thought for a long time before she said yes. "Use the <span class="cn-word" data-tr="tasma (boʻyinga ilinadigan)">strap</span>," she said. "Always."</p>

<p>On the second day, on the wall of the Itchan Kala, Kamola took the strap off because it <span class="cn-word" data-pos="verb" data-tr="buzmoq">spoiled</span> her photos. Then the camera <span class="cn-word" data-pos="verb" data-tr="sirpanib tushmoq">slipped</span> out of her hand and fell onto the stones. The <span class="cn-word" data-tr="obyektiv">lens</span> <span class="cn-word" data-pos="verb" data-tr="yorilmoq">cracked</span>, and the screen went black.</p>

<p>At Gulnora's flat, her apology came out like this:</p>

<p>"I'm really sorry, but it wasn't really my fault. The bag was too small, and somebody pushed me. And the camera's quite old, isn't it?"</p>

<p>Gulnora said nothing at all. She took the camera, looked at the lens, and closed the door <span class="cn-word" data-pos="adv" data-tr="ohista">gently</span>. Kamola stood on the <span class="cn-word" data-tr="zinapoya maydonchasi">landing</span> and understood, slowly, that she had made things worse. She had said <i>sorry</i>, but every sentence after it had been an <span class="cn-word" data-tr="bahona">excuse</span>.</p>

<p>The next evening she came back and read a second apology from her phone.</p>

<p>"<strong>I'm sorry for breaking</strong> your camera. <strong>It was my fault.</strong> You told me to use the strap, and I took it off because I wanted better photos. <strong>I'm sorry that I</strong> made excuses yesterday — that was worse than dropping it. I've found out that the lens can be <span class="cn-word" data-pos="verb" data-tr="taʼmirlanmoq">repaired</span> for four hundred thousand sum. I'm working at the café this summer, and <strong>I'll pay</strong> for the repair from my <span class="cn-word" data-tr="ish haqi">wages</span>. <strong>I'll make sure</strong> nothing like this happens again."</p>

<p>Gulnora was quiet for a moment. Then she opened the door wider. "<strong>Apology accepted</strong>," she said. "Come in. I'll make tea."</p>

<p>In the kitchen she told Kamola a secret. When she was sixteen, she had broken her own mother's <span class="cn-word" data-tr="tikuv mashinasi">sewing machine</span> and <span class="cn-word" data-pos="verb" data-tr="aybni agʻdarmoq">blamed</span> it on the cat. "The machine was easy to fix," she said. "It took my mother much longer to <span class="cn-word" data-pos="verb" data-tr="ishonmoq">trust</span> me again."</p>

<p>Kamola paid for the repair by the end of August. In September, Gulnora <span class="cn-word" data-pos="verb" data-tr="qarzga bermoq">lent</span> her the camera again for her cousin's wedding — and, without a word, handed her a new strap first.</p>''',
        "questions": [
            {
                "text": "Why did Kamola's first apology fail?",
                "choices": [
                    "Because she did not say sorry",
                    "Because after saying sorry she made only excuses",
                    "Because she offered to pay too little",
                ],
                "answer": 1,
                "explanation": "U <i>sorry</i> dedi, lekin keyingi har bir gap bahona "
                               "edi: sumka kichik, kimdir itardi, kamera eski…",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "I'm sorry for break your camera.",
                    "I'm sorry for breaking your camera.",
                    "I'm sorry to breaking your camera.",
                ],
                "answer": 1,
                "explanation": "<b>sorry for + -ing</b> — oʻtgan ish uchun kechirim: "
                               "<i>sorry for breaking</i>.",
            },
            {
                "text": "What made the second apology believable?",
                "choices": [
                    "She admitted it was her fault, explained, offered to pay and promised",
                    "She blamed the strap and the bag",
                    "She bought her aunt a new camera",
                ],
                "answer": 0,
                "explanation": "Ishonchli kechirim formulasi: <b>tan olish</b> (It was my "
                               "fault) + tushuntirish + <b>taklif</b> (I'll pay) + <b>vaʼda</b>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-99 — small talk   (a Manchester bus stop)                     [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Waiting for the Bus with a Stranger",
        "summary": (
            "PE-99 matni. Manchesterda yomgʻirli tong. Toshkentlik talaba "
            "Bobur bekatda notanish kampir bilan yigirma daqiqa gaplashdi — "
            "va kichik suhbat aslida nima ekanini oʻrgandi."
        ),
        "order":   99,
        "grammar": [
            {
                "pattern":  "openers with question tags, and echo questions",
                "meaning":  "Kichik suhbat koʻpincha tasdiqni kutadigan savol bilan "
                            "boshlanadi: <b>Terrible weather, isn't it?</b> Javob: "
                            "<b>It is, isn't it?</b> Tinglayotganingizni koʻrsatish — "
                            "<b>echo question</b>: <i>I taught in Tashkent.</i> — "
                            "<b>Did you?</b> <i>It's my first winter here.</i> — <b>Is it?</b>",
                "examples": ["Terrible weather, isn't it?", "— I'm from Tashkent. — Are you?",
                             "— I taught there for two years. — Did you?"],
            },
            {
                "pattern":  "So do I / Neither do I — and ending politely",
                "meaning":  "Rozilik: <b>So do I</b> (tasdiq), <b>Neither do I</b> "
                            "(inkor) — yordamchi feʼl birinchi gapga mos: <i>I can't "
                            "stand the rain. — <b>Neither can I</b>.</i> Tugatish: "
                            "<b>Lovely to chat</b>, <b>Take care</b>, <b>Have a good day</b>.",
                "examples": ["— I love the markets here. — So do I.",
                             "— I can't stand this rain. — Neither can I.",
                             "Lovely to chat. Take care!"],
            },
        ],
        "body": '''<p>Bobur had been in Manchester for six weeks, and he had learned that the number 86 bus came every twelve minutes, except when it rained. It was raining.</p>

<p>He was standing at the stop with his <span class="cn-word" data-tr="kapyushon">hood</span> up when an <span class="cn-word" data-pos="adj" data-tr="keksa">elderly</span> woman with a <span class="cn-word" data-pos="adj" data-tr="katak naqshli">tartan</span> <span class="cn-word" data-tr="gʻildirakli xalta">shopping trolley</span> joined him. "<strong>Terrible weather, isn't it?</strong>"</p>

<p>Bobur began to explain that, in fact, it was only the third rainy day that week, and that the <span class="cn-word" data-tr="ob-havo maʼlumoti">forecast</span> said —</p>

<p>She was smiling. He stopped. A teacher had told him once that in England a question about the weather is not really a question. It is a <span class="cn-word" data-tr="salomlashish">greeting</span> with a question mark.</p>

<p>"<strong>It is, isn't it?</strong>" he said.</p>

<p>"Not from round here, are you?"</p>

<p>"No, I'm from Tashkent."</p>

<p>"Tashkent!" Her face changed. "I taught English there. Nineteen ninety-four and ninety-five."</p>

<p>"<strong>Did you?</strong>" said Bobur.</p>

<p>Her name was Margaret. She had taught at an <span class="cn-word" data-tr="institut">institute</span> near Amir Temur Square, and she still remembered the <span class="cn-word" data-tr="oʻriklar">apricots</span> in June. "I still love the Chorsu bazaar," she said.</p>

<p>"<strong>So do I</strong>. My grandmother sells <span class="cn-word" data-tr="quruq meva">dried fruit</span> there."</p>

<p>"I never got used to the summer heat, though."</p>

<p>"<strong>Neither did I</strong>," he admitted, "and I was born there." She laughed.</p>

<p>She asked what he was studying (<span class="cn-word" data-tr="qurilish muhandisligi">civil engineering</span>) and whether he was <span class="cn-word" data-pos="adj" data-tr="vatanini sogʻingan">homesick</span> (a little, on Sundays). He asked about her <span class="cn-word" data-tr="nevaralar">grandchildren</span>, and about the trolley, which held four <span class="cn-word" data-tr="karamlar">cabbages</span> for a neighbour.</p>

<p>The bus arrived eighteen minutes late. At the door, Margaret turned round.</p>

<p>"<strong>Lovely to chat</strong>, love. <strong>Take care</strong> of yourself."</p>

<p>"You too. Have a good day."</p>

<p>They had talked about rain, apricots and cabbages — nothing important at all. Yet for the first time in six weeks, he felt that someone in this city knew who he was. Small talk, he decided, is not about the weather. It is a way of saying: I see you; you are not <span class="cn-word" data-pos="adj" data-tr="koʻrinmas">invisible</span> here.</p>

<p>The next Monday, at the same stop, a tartan trolley appeared beside him. "<span class="cn-word" data-pos="adj" data-tr="dahshatli">Dreadful</span> morning, isn't it?"</p>

<p>"It is, isn't it?" said Bobur, smiling, and moved his bag so that she could <span class="cn-word" data-pos="verb" data-tr="panalamoq">shelter</span> under the roof.</p>''',
        "questions": [
            {
                "text": "What did Bobur's teacher mean when she said a question about the weather is 'a greeting with a question mark'?",
                "choices": [
                    "That the English are very interested in the forecast",
                    "That it is a friendly way to start talking, not a real request for information",
                    "That you should never answer questions about the weather",
                ],
                "answer": 1,
                "explanation": "Ob-havo haqidagi savol — aslida salomlashish, suhbatni "
                               "boshlash usuli. Unga maʼlumot bilan emas, tasdiq bilan "
                               "javob beriladi: <i>It is, isn't it?</i>",
            },
            {
                "text": "'I never got used to the summer heat.' Which reply means 'I didn't either'?",
                "choices": ["So did I.", "Neither did I.", "Neither didn't I."],
                "answer": 1,
                "explanation": "Inkor maʼnoli gapga rozilik — <b>Neither + yordamchi feʼl + I</b>. "
                               "<i>never got</i> → oʻtgan zamon yordamchisi <b>did</b>: "
                               "<b>Neither did I</b>. <i>didn't</i> qoʻshilmaydi — inkor <i>neither</i> da.",
            },
            {
                "text": "Which is an 'echo question' that shows you are listening?",
                "choices": [
                    "— I taught English there. — Did you?",
                    "— I taught English there. — What did you teach?",
                    "— I taught English there. — I see.",
                ],
                "answer": 0,
                "explanation": "<b>Echo question</b> — gapning yordamchi feʼlini qaytarish: "
                               "<i>taught</i> → <b>Did you?</b> U «qiziq, davom eting» degani.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-100 — the toolkit   (a letter to the reader)                 [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Three Per Cent Who Finish",
        "summary": (
            "PE-100 matni. Yakuniy matn — oʻquvchining oʻziga xat. Onlayn "
            "kurslarni boshlaganlarning kamdan-kam qismi oxirigacha yetadi. "
            "Siz yuzinchi matnni oʻqiyapsiz: bu matn — siz haqingizda."
        ),
        "order":   100,
        "grammar": [
            {
                "pattern":  "the whole toolkit in one text: the 12 tenses, modals, conditionals",
                "meaning":  "Bu matnda kursning asosiy qismlari yana bir bor uchraydi: "
                            "<b>present perfect</b> (<i>you have read</i>), <b>past "
                            "perfect</b> (<i>you had never seen</i>), <b>future "
                            "perfect</b> (<i>you will have forgotten</i>), modallar "
                            "(<i>you might, you should</i>), shartli gaplar va "
                            "inversiya (<i>Not until… did you…</i>).",
                "examples": ["By now you have read a hundred texts.",
                             "If you had stopped at lesson forty, you would not be reading this.",
                             "Not until the last page does a course really end."],
            },
            {
                "pattern":  "what to do next: keep using it",
                "meaning":  "Til — qoʻllanganda yashaydi. Har kuni oz-ozdan: oʻqish, "
                            "yozish, gapirish. Xatolar roʻyxatingizni (PE-92) qoʻlingizda "
                            "saqlang va har bir yozuvdan keyin tekshiring.",
                "examples": ["Read something in English every day.",
                             "Write five sentences, then check them."],
            },
        ],
        "body": '''<p>In 2019, two <span class="cn-word" data-tr="tadqiqotchilar">researchers</span> at Harvard and MIT published a study of the free online courses their universities had offered. Millions of people had <span class="cn-word" data-pos="verb" data-tr="roʻyxatdan oʻtmoq">signed up</span>. For the courses of 2017 and 2018, about three per cent of them had finished.</p>

<p>Out of every hundred people who <span class="cn-word" data-pos="verb" data-tr="roʻyxatdan oʻtmoq">enrolled</span>, ninety-seven stopped somewhere along the way — after the first video, after the first difficult <span class="cn-word" data-tr="topshiriq">assignment</span>, after a busy week that turned into a busy month. Life is full, and a course is easy to <span class="cn-word" data-pos="verb" data-tr="tashlab ketmoq">abandon</span>: nobody notices when you leave.</p>

<p>This is the hundredth reading in this collection, so let us be <span class="cn-word" data-pos="adj" data-tr="rostgoʻy">honest</span> about who is reading it.</p>

<p>When you began, a sentence like <i>The Rain Is Starting</i> was a <span class="cn-word" data-tr="qiyinchilik, sinov">challenge</span>. Since then you <strong>have read</strong> about a dog who waited at a station, a bridge that a woman finished, a comma that cost five million dollars and a clock that ran ten minutes fast. You <strong>have met</strong> twelve tenses, and you <strong>can</strong> explain why <i>I have lived here for ten years</i> is right. <strong>If you had stopped</strong> at lesson forty, you <strong>would not be reading</strong> this paragraph. You did not stop.</p>

<p>Here is the <span class="cn-word" data-pos="adj" data-tr="noqulay">uncomfortable</span> truth: you are no longer a <span class="cn-word" data-tr="boshlovchi">beginner</span>, and you <strong>should</strong> stop thinking of yourself as one. You are one of the three per cent.</p>

<p>What happens now? <strong>Not until</strong> you use a language <strong>does</strong> it become yours. A <span class="cn-word" data-tr="asboblar toʻplami">toolkit</span> that stays in the box <span class="cn-word" data-pos="verb" data-tr="zanglamoq">rusts</span>. So read something in English every day. Write five sentences and check them against your own list of <span class="cn-word" data-pos="adj" data-tr="sevimli">favourite</span> mistakes. Talk to someone — a stranger at a bus stop, if <span class="cn-word" data-pos="adj" data-tr="zarur">necessary</span>. You <strong>will make</strong> mistakes. You <strong>might</strong> feel <span class="cn-word" data-pos="adj" data-tr="ahmoqona">foolish</span>. Do it anyway.</p>

<p>A year from now, you <strong>will have forgotten</strong> some of the rules in these hundred lessons. That is fine. Rules are <span class="cn-word" data-tr="havoza">scaffolding</span>: they hold the building up while it is going up, and then they come down. What <span class="cn-word" data-pos="verb" data-tr="qolmoq">remains</span> is the building — the English you <strong>have built</strong>, sentence by sentence, text by text.</p>

<p>Most people who start never get here. You are here.</p>

<p>Well done. Now close this page, and go and use it.</p>''',
        "questions": [
            {
                "text": "What does the 'three per cent' in the title refer to?",
                "choices": [
                    "The share of English words that are difficult",
                    "The share of people who finished the free online courses in the study",
                    "The number of lessons the reader has missed",
                ],
                "answer": 1,
                "explanation": "Garvard va MIT tadqiqoti (2019): 2017–2018-yillardagi "
                               "bepul onlayn kurslarni boshlaganlarning taxminan "
                               "3 foizi oxirigacha yetgan.",
            },
            {
                "text": "'If you had stopped at lesson forty, you would not be reading this.' What kind of conditional is this?",
                "choices": [
                    "A first conditional about the future",
                    "A mixed conditional: an unreal past with a present result",
                    "A zero conditional about general truths",
                ],
                "answer": 1,
                "explanation": "<b>Mixed conditional</b> (PE-56): <i>had stopped</i> — "
                               "oʻtmishdagi sodir boʻlmagan holat, <i>would not be "
                               "reading</i> — uning hozirgi natijasi.",
            },
            {
                "text": "What does the writer compare grammar rules to?",
                "choices": ["A box of old tools", "Scaffolding that comes down when the building is finished", "A bus timetable"],
                "answer": 1,
                "explanation": "Qoidalar — havoza: bino qurilayotganda uni ushlab turadi, "
                               "keyin olinadi. Qoladigan narsa — siz qurgan ingliz tili.",
            },
        ],
    },
]
