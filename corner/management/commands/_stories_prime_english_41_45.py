# -*- coding: utf-8 -*-
"""Prime English Readings — PE-41 … PE-45 (batch 9). Capstone + the first modals.

PE-41 the 12 tenses in one text · PE-42 can/could/be able to · PE-43 may/might/could
(possibility) · PE-44 must/have to/need to · PE-45 mustn't vs don't have to.

Shapes:
  41 — the capstone: one bakery, one morning, twelve tenses (a callback to PE-20's
       "The Day the Bakery Opened" — the son now opens it alone)
  42 — a life story: the girl who could not put her face in the water
  43 — a night mystery: three nights of scratching inside a wall (may/might/could)
  44 — a hostel notice with one strange rule, and the reason behind it
  45 — a coach with two sentences on the wall, and the final he lost to keep them

Cumulative rule: PE-41 uses NO modals at all except will (can/could arrive in PE-42).
PE-44's notice avoids `mustn't` on purpose — that pair is PE-45's whole lesson, and
PE-45 is built on it. No conditionals (PE-53+), no passive (PE-60), no reported
speech with backshift (PE-62), no comparatives (PE-67).
Length: 240–280 words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_41_45.py --author=prime
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
    # PE-41 — all twelve tenses in one story  (capstone)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "One Oven, Twelve Tenses",
        "summary": (
            "PE-41 matni. PE-20 dagi nonvoyxona — oʻn ikki yildan keyin. "
            "Bugun ertalab oʻgʻil birinchi marta yolgʻiz ishlaydi, va "
            "bitta ertalakda oʻn ikkita zamon uchraydi."
        ),
        "order":   41,
        "grammar": [
            {
                "pattern":  "The four PRESENT tenses",
                "meaning":  "<b>Simple</b>: he mixes it by hand (odat). "
                            "<b>Continuous</b>: Bekzod is mixing it now "
                            "(shu daqiqa). <b>Perfect</b>: he has always "
                            "mixed it by hand (natija bugun). "
                            "<b>Perfect continuous</b>: he has been mixing "
                            "it since March (davom etmoqda).",
                "examples": ["His father mixes the dough by hand.",
                             "Bekzod is mixing it now.",
                             "He has been mixing it every morning since March."],
            },
            {
                "pattern":  "The four PAST tenses",
                "meaning":  "<b>Simple</b>: he opened the bakery "
                            "(tugagan). <b>Continuous</b>: he was standing "
                            "at the door (fon). <b>Perfect</b>: he had "
                            "worked in three bakeries before that "
                            "(oldingi oʻtmish). <b>Perfect continuous</b>: "
                            "he had been carrying other men's bread for "
                            "nine years (oldin davom etgan).",
                "examples": ["Twelve years ago he opened this bakery.",
                             "At four this morning he was standing at the door.",
                             "He had been carrying other men's bread for nine years."],
            },
            {
                "pattern":  "The four FUTURE forms",
                "meaning":  "<b>will</b>: you will burn a tray (taxmin). "
                            "<b>going to</b>: he is going to keep the shop "
                            "(reja). <b>Future continuous</b>: at seven he "
                            "will be standing there (oʻsha daqiqada). "
                            "<b>Future perfect (continuous)</b>: by seven "
                            "he will have made two hundred loaves; by "
                            "August he will have been working here for six "
                            "months.",
                "examples": ["By seven o'clock he will have made two hundred loaves.",
                             "By August he will have been working here for six months."],
            },
        ],
        "body": '''<p>Twelve years ago Bekzod's father <strong>opened</strong> a bakery on our corner. He <strong>had worked</strong> in three other bakeries before that, and he <strong>had been carrying</strong> other men's bread for nine years.</p>

<p>At four o'clock this morning he <strong>was standing</strong> at the door with the <span class="cn-word" data-tr="kalit">key</span> in his hand, and he did not put it in the lock. He gave it to his son.</p>

<p>His father <strong>mixes</strong> the dough by hand. He <strong>has always mixed</strong> it by hand, because a <span class="cn-word" data-tr="dastgoh">machine</span> <strong>doesn't feel</strong> the <span class="cn-word" data-tr="xamirturush">yeast</span>.</p>

<p>Now, at half past four, Bekzod <strong>is mixing</strong> it. He <strong>has been mixing</strong> it every morning <strong>since</strong> March, but never alone, and never with his father outside in the yard.</p>

<p>The <span class="cn-word" data-tr="tarozi">scales</span> are old. The <span class="cn-word" data-tr="issiqlik">heat</span> from the oven fills the room by five. Bekzod's <span class="cn-word" data-tr="fartuk">apron</span> is white now and it will be grey at seven.</p>

<p>"You <strong>will burn</strong> a tray," his father said at the door. "Everybody burns a tray on the first morning. It <strong>isn't going to be</strong> <span class="cn-word" data-tr="dunyoning oxiri">the end of the world</span>."</p>

<p>By seven o'clock Bekzod <strong>will have made</strong> two hundred loaves. At seven he <strong>will be standing</strong> at the <span class="cn-word" data-tr="peshtaxta, lavha">counter</span> exactly where his father stood for twelve years, and the <span class="cn-word" data-tr="navbat">queue</span> <strong>will be waiting</strong> in the cold outside.</p>

<p>By August he <strong>will have been working</strong> in this bakery for six months. He <strong>is going to keep</strong> the shop. He told his father that in one sentence, in March, and his father said nothing for a long minute.</p>

<p>He did not burn the first tray.</p>

<p>He <strong>burnt</strong> the second one, because he <strong>was watching</strong> the first.</p>

<p>At ten past seven his father opened the <span class="cn-word" data-tr="panjur">shutters</span> from the outside. <span class="cn-word" data-tr="bugʻ">Steam</span> went out into the street, and eleven people came in.</p>

<p>One oven, one morning, twelve tenses — and the same question at four o'clock every day for twelve years: <i>is the bread ready?</i></p>''',
        "questions": [
            {
                "text": "What is different about this morning?",
                "choices": [
                    "The father gives his son the key and works outside",
                    "The bakery opens two hours late",
                    "They use a machine for the dough",
                ],
                "answer": 0,
                "explanation": "“…he did not put it in the lock. He gave it "
                               "to his son.” Bekzod birinchi marta yolgʻiz "
                               "ishlaydi.",
            },
            {
                "text": "Which sentence is in the FUTURE PERFECT?",
                "choices": [
                    "At seven he will be standing at the counter.",
                    "By seven o'clock he will have made two hundred loaves.",
                    "He is going to keep the shop.",
                ],
                "answer": 1,
                "explanation": "<b>will have + V3</b> — kelajakdagi nuqtadan "
                               "oldin tugaydigan ish. Birinchisi — future "
                               "continuous, uchinchisi — reja.",
            },
            {
                "text": "Why did he burn the second tray?",
                "choices": [
                    "The oven was too hot",
                    "He was watching the first one",
                    "His father called him outside",
                ],
                "answer": 1,
                "explanation": "“He burnt the second one, because he was "
                               "watching the first.” — birinchi kunning eng "
                               "insoniy xatosi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-42 — can / could / be able to  (life story)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Girl Who Could Not Swim",
        "summary": "PE-42 matni. Butun qishloq iyulda kanalda suzadi — Nilufar esa suvga yuzini ham tekkiza olmaydi. Uch hafta, har kuni kechqurun, beton labida.",
        "order":   42,
        "grammar": [
            {
                "pattern":  "can / can't = ability now · could / couldn't = ability then",
                "meaning":  "<b>can</b> hozirgi qobiliyat, <b>could</b> "
                            "oʻtmishdagi umumiy qobiliyat: <i>She "
                            "<b>couldn't</b> swim at fourteen; now she "
                            "<b>can</b> swim a kilometre</i>. Ikkisidan "
                            "keyin feʼl asosiy shaklda — <i>can to "
                            "swim</i> xato.",
                "examples": ["She could not put her face in the water.",
                             "Now she can swim a kilometre without stopping."],
            },
            {
                "pattern":  "was / were able to = managed it ONCE",
                "meaning":  "Bir marta, aniq bir holatda uddalash — "
                            "<b>was able to</b> (yoki <i>managed to</i>): "
                            "<i>In August she <b>was able to</b> swim to "
                            "the other side</i>. Bu yerda <i>could</i> "
                            "gʻalati eshitiladi. Inkorda esa "
                            "<i>couldn't</i> hamisha toʻgʻri.",
                "examples": ["In August she was able to swim to the other side.",
                             "She wasn't able to breathe out under the water at first."],
            },
            {
                "pattern":  "be able to fills the empty places",
                "meaning":  "<i>can</i> ning kelasi zamoni va perfekti "
                            "yoʻq, shuning uchun ularning oʻrniga "
                            "<b>be able to</b> keladi: "
                            "<i>will be able to</i>, <i>have been able "
                            "to</i>, <i>to be able to</i>.",
                "examples": ["Next summer they will be able to swim in the new pool.",
                             "Two hundred children have been able to learn there."],
            },
        ],
        "body": '''<p>In our village July means water. Everybody swims in the canal: boys, girls, grandfathers, two donkeys and a dog called Bulut.</p>

<p>At fourteen, Nilufar <strong>could not</strong> swim.</p>

<p>She <strong>could</strong> run faster than her brothers. She <strong>could</strong> carry two <span class="cn-word" data-tr="chelak">buckets</span> of water up a hill without stopping. But she <strong>could not</strong> put her face in the water, and everybody in that village knew it.</p>

<p>When she was six she <span class="cn-word" data-pos="verb" data-tr="choʻkdi">sank</span> in that canal for four seconds, and her uncle pulled her out by the arm. Four seconds. After that, water was not water any more. It was a hand.</p>

<p>Her cousin Zuhra came for the summer and made a plan of three weeks.</p>

<p>Week one: Nilufar sat on the <span class="cn-word" data-tr="beton">concrete</span> <span class="cn-word" data-tr="chetiga, labiga">edge</span> with her feet in the <span class="cn-word" data-pos="adj" data-tr="sayoz">shallow</span> water and blew <span class="cn-word" data-tr="pufakchalar">bubbles</span> from her mouth. Nothing else.</p>

<p>Week two: she held the edge and let her legs come up behind her. She <strong>wasn't able to</strong> keep her <span class="cn-word" data-tr="nafas">breath</span> quiet, and twice she stood up and cried with her hands over her face.</p>

<p>Week three: she <span class="cn-word" data-pos="verb" data-tr="qoʻlini uzdi">let go of</span> the concrete for two seconds. Then five. Then she <span class="cn-word" data-pos="verb" data-tr="suzib turdi">floated</span> <span class="cn-word" data-tr="chalqancha">on her back</span> and looked at the sky for a whole minute, which is longer than four seconds, and she understood that too.</p>

<p>In August she <strong>was able to</strong> swim to the other side of the canal, once, with Zuhra beside her all the way.</p>

<p>Nilufar is twenty-six now. She <strong>can</strong> swim a kilometre without stopping, but that is not the interesting part.</p>

<p>She works at the town <span class="cn-word" data-tr="basseyn">pool</span>. She teaches the children who arrive holding their mother's hand, the ones who <strong>can't</strong> put their faces in the water. Two hundred and forty of them <strong>have been able to</strong> learn in her <span class="cn-word" data-tr="yoʻlak (suzish)">lane</span> since 2019.</p>

<p>She starts every first lesson with the same sentence: "I <strong>couldn't</strong> do this until I was fourteen."</p>''',
        "questions": [
            {
                "text": "Why was Nilufar afraid of the water?",
                "choices": [
                    "She had sunk in the canal for four seconds when she was six",
                    "She had never seen the canal before",
                    "Her cousin Zuhra frightened her",
                ],
                "answer": 0,
                "explanation": "“…she sank in that canal for four seconds, "
                               "and her uncle pulled her out… After that, "
                               "water was not water any more.”",
            },
            {
                "text": "Which sentence is correct for one single success?",
                "choices": [
                    "In August she could swim to the other side, once.",
                    "In August she was able to swim to the other side, once.",
                    "In August she can swim to the other side, once.",
                ],
                "answer": 1,
                "explanation": "Bir martalik muvaffaqiyat uchun "
                               "<b>was able to</b> (yoki <i>managed to</i>) "
                               "ishlatiladi; <i>could</i> umumiy "
                               "qobiliyatni bildiradi.",
            },
            {
                "text": "Why does she begin every first lesson with that sentence?",
                "choices": [
                    "To show the children that the fear can end",
                    "To explain the rules of the pool",
                    "Because she still cannot swim well",
                ],
                "answer": 0,
                "explanation": "“I couldn't do this until I was fourteen.” "
                               "Uning oʻzi ham qoʻrqqan — shuning uchun "
                               "bolalar unga ishonadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-43 — may / might / could: possibility  (night mystery)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Something in the Wall",
        "summary": (
            "PE-43 matni. Uch kecha ketma-ket, ikkida, devor ichidan "
            "tirnash ovozi keladi. Har kim boshqa taxmin qiladi — va "
            "hech kim aniq bilmaydi. may, might, could."
        ),
        "order":   43,
        "grammar": [
            {
                "pattern":  "may / might / could + base verb = maybe",
                "meaning":  "Aniq bilmaganda taxmin qilish: <i>It "
                            "<b>might</b> be a mouse</i>. Uchtasi ham "
                            "“balki” degani. <b>may</b> — rasmiyroq, "
                            "<b>might</b> va <b>could</b> — gapirishda "
                            "koʻproq. Feʼl asosiy shaklda qoladi.",
                "examples": ["It might be a mouse.", "It may be water in a pipe.",
                             "It could be the wind in the chimney."],
            },
            {
                "pattern":  "may not / might not = maybe not",
                "meaning":  "Inkori: <i>It <b>might not</b> be an "
                            "animal</i>. Diqqat — <b>couldn't</b> bu "
                            "maʼnoda inkor emas: u “qila olmadi” "
                            "(PE-42) yoki “boʻlishi mumkin emas” "
                            "(PE-47) degani.",
                "examples": ["It may not be an animal at all.",
                             "We might not find anything tonight."],
            },
            {
                "pattern":  "Never “can” for one guess",
                "meaning":  "<i>can</i> umumiy imkoniyatni bildiradi "
                            "(<i>Mice can live in walls</i> — "
                            "sichqonlar devorda yashashi mumkin, "
                            "umuman). Aniq bir holat haqidagi taxmin "
                            "uchun <i>can</i> ishlatilmaydi: "
                            "“<i>It can be a mouse</i>” xato.",
                "examples": ["Mice can live inside a wall.",
                             "This one might be something else."],
            },
        ],
        "body": '''<p>It started on Monday at two o'clock in the morning: a small, dry <span class="cn-word" data-tr="tirnash ovozi">scratching</span> inside the wall of the front room, behind the shelf with the cups.</p>

<p>My mother sat up in bed. "It <strong>might</strong> be a mouse."</p>

<p>"It <strong>may</strong> be water in a <span class="cn-word" data-tr="quvur">pipe</span>," my father said, in the voice of a man who wants to sleep.</p>

<p>Tuesday, two o'clock. Scratch. Stop. Scratch.</p>

<p>"It <strong>could</strong> be the wind in the <span class="cn-word" data-tr="moʻri">chimney</span>," my father said.</p>

<p>"There is no wind," my mother said. "And a pipe <strong>may not</strong> scratch three nights at the same hour."</p>

<p>My little brother had his own idea, and he told it to us with the blanket up to his eyes. "It <strong>might</strong> be a hand."</p>

<p>My grandfather, who sleeps in the next room and hears everything, gave us the only calm sentence in the house. "It <strong>might</strong> be nothing. But something that comes at the same time every night <strong>could</strong> be alive."</p>

<p>On Wednesday my father came home with a <span class="cn-word" data-tr="bolgʻa">hammer</span> and a <span class="cn-word" data-tr="fonar">torch</span>.</p>

<p>He knocked on the wall with one finger, from the floor to the ceiling. Above the shelf the sound changed: <span class="cn-word" data-tr="boʻsh, gʻovak">hollow</span>. There was an old <span class="cn-word" data-tr="shamollatish teshigi">ventilation hole</span> there, painted over years ago.</p>

<p>He opened a square the size of a book.</p>

<p>A grey <span class="cn-word" data-tr="qaldirgʻoch">swallow</span> came out of the dark, hit the window twice, and sat on the top of the door with its <span class="cn-word" data-tr="qanot">wing</span> half open. My brother did not move for a full minute.</p>

<p>Inside the hole, on a bed of dry grass and one blue thread, there were three eggs.</p>

<p>The bird had come in through a <span class="cn-word" data-tr="gʻisht">brick</span> that had fallen out on the roof side.</p>

<p>My father did not close the wall. He put a small board under the hole, and we lived with an open wall for nineteen days, until three young swallows sat on the shelf with the cups and then went out through the window, one after another.</p>

<p>He closed it in October. My brother wrote the date on the new paint, and under the date, four words: <i>it was not nothing</i>.</p>''',
        "questions": [
            {
                "text": "What was making the sound?",
                "choices": [
                    "Water in an old pipe",
                    "A swallow in a painted-over ventilation hole",
                    "The wind in the chimney",
                ],
                "answer": 1,
                "explanation": "Devordan qaldirgʻoch chiqdi, teshik ichida "
                               "esa uch dona tuxum bor edi.",
            },
            {
                "text": "Which sentence is NOT correct English?",
                "choices": [
                    "It might be a mouse.",
                    "It can be a mouse.",
                    "It could be a mouse.",
                ],
                "answer": 1,
                "explanation": "Aniq bir holat haqidagi taxmin uchun "
                               "<i>can</i> ishlatilmaydi. <i>Mice can live "
                               "in walls</i> — umumiy imkoniyat, bu boshqa "
                               "maʼno.",
            },
            {
                "text": "What did the family do after they found the nest?",
                "choices": [
                    "They left the wall open for nineteen days",
                    "They closed the wall the same evening",
                    "They took the eggs outside",
                ],
                "answer": 0,
                "explanation": "Ota devorni yopmadi — uchta polapon "
                               "uchib ketguncha, oʻn toʻqqiz kun, "
                               "devor ochiq qoldi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-44 — must / have to / need to  (hostel rules)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Rule Nobody Understood",
        "summary": (
            "PE-44 matni. Yotoqxona devoridagi qoidalar roʻyxati oddiy — "
            "faqat oxirgisidan tashqari: “Siz kimdir bilan ovqatlanishingiz "
            "kerak.” Nima uchun?"
        ),
        "order":   44,
        "grammar": [
            {
                "pattern":  "must = the rule speaks",
                "meaning":  "Qoida, qonun, eʼlon — yozma va rasmiy tilda "
                            "<b>must</b>: <i>You <b>must</b> be in the "
                            "building by nine</i>. Uchinchi shaxsda ham "
                            "oʻzgarmaydi (<i>he must</i>) va oʻtgan "
                            "zamoni yoʻq — u yerda <i>had to</i> keladi.",
                "examples": ["You must be in the building by nine o'clock.",
                             "You must eat with somebody."],
            },
            {
                "pattern":  "have to = the situation demands it",
                "meaning":  "Tashqi majburiyat, va gapirishda eng koʻp "
                            "ishlatiladigan shakl: <i>I <b>have to</b> "
                            "wash my own plate</i>. <i>has to</i>, "
                            "oʻtgan zamonda <i>had to</i>, kelasida "
                            "<i>will have to</i>.",
                "examples": ["Everybody has to wash his own plate.",
                             "He had to learn the timetable in one week."],
            },
            {
                "pattern":  "need to = it is necessary",
                "meaning":  "Yumshoqroq zaruriyat: <i>You <b>need to</b> "
                            "tell the warden if you are ill</i>. Inkori "
                            "<i>don't need to</i> — “shart emas” "
                            "(PE-45 ga qaraydi).",
                "examples": ["You need to tell the warden if you are ill.",
                             "You don't need to ask about tea. Tea is free."],
            },
        ],
        "body": '''<p>Jasur won a place at a <span class="cn-word" data-tr="litsey">lyceum</span> in the city when he was fifteen, and in September he moved into a <span class="cn-word" data-tr="yotoqxona">hostel</span> with sixty other boys and a smell of wet floors.</p>

<p>There was a <span class="cn-word" data-tr="eʼlon">notice</span> on the wall of the corridor, in two languages, in old paint:</p>

<p><i>1. You <strong>must</strong> be in the building by nine o'clock. 2. Everybody <strong>has to</strong> wash his own plate. 3. You <strong>need to</strong> tell the <span class="cn-word" data-tr="tarbiyachi">warden</span> if you are ill, even a little ill. 4. You <strong>must</strong> eat with somebody.</i></p>

<p>The first three were normal. Jasur read the fourth one four times.</p>

<p>He asked the boys in his room about it. One of them said the <span class="cn-word" data-tr="oshpaz">cook</span> wrote it, because plates come back faster from a table of four. Another said it is an old rule from the Soviet time and nobody remembers.</p>

<p>In October, Jasur was <span class="cn-word" data-pos="adj" data-tr="uyni sogʻingan">homesick</span> in a way that had no bottom to it. He <strong>had to</strong> learn the <span class="cn-word" data-tr="dars jadvali">timetable</span>, the streets, the bus numbers, and a new kind of quiet. He took his plate to the end of the long table in the <span class="cn-word" data-tr="oshxona">canteen</span> and sat with his back to the room.</p>

<p>A hand put a glass of tea in front of him. The warden sat down <span class="cn-word" data-pos="adv" data-tr="roʻparasiga">opposite</span>, with his own plate.</p>

<p>"You know rule four," he said.</p>

<p>"I don't understand rule four."</p>

<p>The warden ate for a while. Then he told Jasur about a boy from a mountain village, two years before, who stopped eating with people in his second <span class="cn-word" data-tr="chorak, semestr">term</span>. Sixty boys in this building, and for five weeks nobody <span class="cn-word" data-pos="verb" data-tr="sezmadi">noticed</span>. He went home in February and he did not come back.</p>

<p>"After that we wrote rule four," the warden said. "You <strong>must</strong> eat with somebody. Not because of the plates."</p>

<p>Jasur is in his last year now. He does not sit at the end of the table any more. He sits in the middle, and when a new boy comes in with his plate and looks for the emptiest corner of the room, Jasur puts his hand up and says one word: "Here."</p>''',
        "questions": [
            {
                "text": "Why does rule four exist?",
                "choices": [
                    "So that the plates come back faster from the tables",
                    "Because a boy who ate alone left and nobody had noticed",
                    "Because it is an old rule and nobody remembers",
                ],
                "answer": 1,
                "explanation": "Tarbiyachi tushuntiradi: ikki yil oldin "
                               "bir bola yolgʻiz ovqatlanishni boshladi, "
                               "besh hafta hech kim sezmadi, va u "
                               "qaytmadi.",
            },
            {
                "text": "Which line is correct?",
                "choices": [
                    "Yesterday he must learn the timetable.",
                    "Yesterday he had to learn the timetable.",
                    "Yesterday he musted learn the timetable.",
                ],
                "answer": 1,
                "explanation": "<b>must</b> ning oʻtgan zamon shakli yoʻq — "
                               "uning oʻrniga <b>had to</b> ishlatiladi.",
            },
            {
                "text": "What does Jasur do in his last year?",
                "choices": [
                    "He sits in the middle and invites new boys to his table",
                    "He writes a fifth rule on the notice",
                    "He eats in his room",
                ],
                "answer": 0,
                "explanation": "Yangi bola eng boʻsh burchakni izlaganda, "
                               "Jasur qoʻlini koʻtarib bitta soʻz aytadi: "
                               "“Here.”",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-45 — mustn't vs don't have to  (the coach's two sentences)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "You Don't Have to Come",
        "summary": (
            "PE-45 matni. Murabbiyning kiyinish xonasida ikki gap yozilgan: "
            "kelishing shart emas — lekin yolgʻon gapirmasligingiz kerak. "
            "Ikkisining farqi bir finalga turdi."
        ),
        "order":   45,
        "grammar": [
            {
                "pattern":  "mustn't = it is forbidden",
                "meaning":  "<b>mustn't</b> — taqiq: qilma. "
                            "<i>You <b>mustn't</b> lie to me</i> — "
                            "yolgʻon gapirish taqiqlanadi. Bu "
                            "gapiruvchining qatʼiy chizigʻi.",
                "examples": ["You mustn't lie to me.",
                             "You mustn't touch another player's kit."],
            },
            {
                "pattern":  "don't have to = it is not necessary",
                "meaning":  "<b>don't have to</b> — majburiyat yoʻq, "
                            "xohlasang qil: <i>You <b>don't have to</b> "
                            "come to training</i>. Bu <b>ruxsat</b>, "
                            "taqiq emas — ikkisi bir-biriga umuman "
                            "teng emas.",
                "examples": ["You don't have to come to training.",
                             "You don't have to explain twice."],
            },
            {
                "pattern":  "The dangerous pair",
                "meaning":  "Oʻzbekcha “kelmasligingiz mumkin” va "
                            "“kelmasligingiz kerak” bir-biriga "
                            "juda yaqin eshitiladi, inglizchada esa "
                            "<b>don't have to</b> (shart emas) va "
                            "<b>mustn't</b> (mumkin emas) qarama-qarshi. "
                            "Oʻtgan zamonda: <i>didn't have to</i> "
                            "(shart emas edi) — taqiq uchun esa "
                            "<i>wasn't allowed to</i>.",
                "examples": ["You don't have to come — but you mustn't lie.",
                             "He didn't have to come that Tuesday.",
                             "He wasn't allowed to play in the final."],
            },
        ],
        "body": '''<p>Coach Rustam has two sentences painted on the wall of the <span class="cn-word" data-tr="kiyinish xonasi">changing room</span>, and nothing else. No cups, no photographs, no <span class="cn-word" data-tr="plakatlar">posters</span> of famous players.</p>

<p><i>1. You <strong>don't have to</strong> come to training. 2. You <strong>mustn't</strong> lie to me.</i></p>

<p>Boys arrive at that team and think the first sentence is a gift and the second one is nothing. It is the other way round.</p>

<p>Omar missed <span class="cn-word" data-tr="mashgʻulot">training</span> on a Tuesday in March, because his uncle's shop had no second pair of hands that week. On Wednesday he told the coach exactly that, in eleven words, and looked at the floor.</p>

<p>"You <strong>didn't have to</strong> come," Rustam said. "You <strong>don't have to</strong> explain twice, either. <span class="cn-word" data-tr="isinib ol">Warm up</span>."</p>

<p>Omar played on Saturday.</p>

<p>In April another boy — the fastest player in that team, a boy every coach in the city knew by name — missed two trainings and sent a message about a <span class="cn-word" data-tr="harorat">temperature</span> of thirty-nine.</p>

<p>On Sunday somebody put a photograph in the team group: a wedding, a loud song, and that boy dancing in the middle of it, on the Friday evening.</p>

<p>Rustam said nothing at all. He wrote the boy's name on the paper for the final, then he took a pen and <span class="cn-word" data-tr="chizib tashladi">put a line through</span> it.</p>

<p>They lost the final by one goal. The <span class="cn-word" data-tr="zapas oʻyinchi">substitute</span> ran until he could not stand, and it was not enough.</p>

<p>In the changing room <span class="cn-word" data-pos="adv" data-tr="keyin">afterwards</span> nobody looked up. Rustam stood by his two sentences with his hands in his pockets.</p>

<p>"We lost a match," he said. "We <strong>didn't</strong> lose the rule. A team without <span class="cn-word" data-tr="ishonch">trust</span> loses every Saturday <span class="cn-word" data-tr="umrining oxirigacha">for the rest of its life</span>."</p>

<p>The fastest boy in the city sat on that <span class="cn-word" data-tr="skameyka">bench</span> for the last twenty minutes of a final he <strong>wasn't allowed to</strong> play in, and he has thought about it for five years.</p>

<p>He is a coach himself now, at a school in Chirchiq. There are two sentences painted on the wall of his changing room. He <strong>doesn't have to</strong> explain them to anybody: the boys work it out by October.</p>''',
        "questions": [
            {
                "text": "What happened to the fastest player?",
                "choices": [
                    "He was not allowed to play in the final, because he had lied about being ill",
                    "He was ill and missed the final",
                    "He left the team in April",
                ],
                "answer": 0,
                "explanation": "U 39 daraja harorat haqida xabar yozdi — "
                               "keyin toʻydagi surat chiqdi. Murabbiy "
                               "uning ismini roʻyxatdan chizib tashladi.",
            },
            {
                "text": "\"You don't have to come to training\" means:",
                "choices": [
                    "Coming to training is forbidden",
                    "Coming to training is not necessary — it is your choice",
                    "You must come to training",
                ],
                "answer": 1,
                "explanation": "<b>don't have to</b> — majburiyat yoʻq. "
                               "Taqiq boʻlsa <b>mustn't</b> boʻlar edi, "
                               "va maʼno butunlay teskari.",
            },
            {
                "text": "Which sentence keeps the coach's meaning?",
                "choices": [
                    "You mustn't come to training, but you don't have to lie.",
                    "You don't have to come to training, but you mustn't lie.",
                    "You don't have to come to training, and you don't have to lie.",
                ],
                "answer": 1,
                "explanation": "Kelish — tanlov (<i>don't have to</i>); "
                               "yolgʻon — taqiq (<i>mustn't</i>). "
                               "Birinchi variant ikkisini almashtirib, "
                               "butun maʼnoni buzadi.",
            },
        ],
    },
]
