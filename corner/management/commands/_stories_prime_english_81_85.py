# -*- coding: utf-8 -*-
"""Prime English Readings — PE-81 … PE-85 (batch 17). Marks on the page, then the written voice.

PE-81 punctuation · PE-82 capitals & spelling · PE-83 emphasis with do · PE-84 inversion ·
PE-85 cleft sentences. From PE-83 the readings switch to WRITTEN English (see the toc):
an opinion column, a travel essay, a letter to the editor.

Shapes (varied on purpose):
  81 — a TRUE court case: the Maine dairy drivers and the missing comma (2014–2018)
  82 — a job application to a Samarkand hotel, and the sign at the hotel's own door
  83 — an OPINION COLUMN by a headteacher, one year after the phone lockers
  84 — a TRAVEL ESSAY: a snow leopard at dawn in the Ugam-Chatkal mountains
  85 — a LETTER TO THE EDITOR: the town that needed a library, and the garage that became one

NARRATOR VOICE (see the toc's AUDIO section):
    81 en-US-GuyNeural   · 82 en-US-JennyNeural · 83 en-US-JennyNeural
    84 en-US-GuyNeural   · 85 en-US-GuyNeural
(Batch 16 ran 2 male / 3 female, so this one flips to 3 male / 2 female.)
Generate one story at a time:
    python manage.py gen_corner_audio --collection="Prime English Readings" \
        --only 81 --voice en-US-GuyNeural

Facts in 81 are true: O'Connor v. Oakhurst Dairy, U.S. Court of Appeals for the First
Circuit, March 2017 (Judge Barron's opinion opens "For want of a comma, we have this
case."); the $5 million settlement, 2018; Maine's amended law uses semicolons. 84: snow
leopards do live in Ugam-Chatkal National Park; the ranger and the walk are the essay's own.

Cumulative rule: everything through PE-80 is free. 81–82 use nothing from Block G.
83 adds emphatic do; 84 adds inversion; 85 adds cleft sentences. Still forbidden in all
five: participle clauses as sentence openers (PE-86), the unreal past "It's time we…"
(PE-87) and the heavy linkers however / therefore / moreover (PE-88).
Length: 300–360 words. Vocabulary: 16–22 cn-word marks.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_81_85.py --author=prime
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
    # PE-81 — punctuation   (the missing comma, Maine 2017)          [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Comma That Changed the Meaning",
        "summary": (
            "PE-81 matni. Haqiqiy voqea: AQShning Meyn shtatida uchta "
            "haydovchi bitta vergul uchun sudga bordi — va besh million "
            "dollar yutdi. Tinish belgisi bezak emasligining eng qimmat isboti."
        ),
        "order":   81,
        "grammar": [
            {
                "pattern":  "the list comma — and the 'Oxford comma' before and / or",
                "meaning":  "Roʻyxatda har bir element vergul bilan ajratiladi. "
                            "Oxirgi <b>and / or</b> oldidagi vergul (Oxford comma) "
                            "ixtiyoriy, lekin u boʻlmasa, oxirgi ikki element bitta "
                            "boʻlib oʻqilishi mumkin: <i>packing for shipment or "
                            "distribution</i> — bitta ishmi yoki ikkitami?",
                "examples": ["canning, processing, freezing, drying, and storing",
                             "packing for shipment, or distribution",
                             "I speak Uzbek, Russian, and English."],
            },
            {
                "pattern":  "colon before a list or an explanation; semicolon between two full sentences",
                "meaning":  "<b>Ikki nuqta (:)</b> — «mana u»: roʻyxat yoki tushuntirish "
                            "oldidan. <b>Nuqtali vergul (;)</b> — ikki toʻliq gapni "
                            "bogʻlaydi (vergul bu ishni qila olmaydi — bu "
                            "<i>comma splice</i> xatosi) yoki ichida vergul bor "
                            "roʻyxat elementlarini ajratadi.",
                "examples": ["The law listed the jobs: canning, processing, storing…",
                             "The drivers did not pack anything; they drove trucks."],
            },
            {
                "pattern":  "the apostrophe with plurals — drivers' / the company's",
                "meaning":  "Birlikda <b>'s</b>: <i>the company's lawyer</i>. "
                            "-s bilan tugagan koʻplikda faqat <b>'</b>: <i>the "
                            "drivers' lawyer</i> (uchta haydovchining advokati).",
                "examples": ["the drivers' complaint", "the company's lawyer", "in the workers' favour"],
            },
        ],
        "body": '''<p>In 2014, three delivery drivers for a <span class="cn-word" data-tr="sut mahsulotlari (korxonasi)">dairy</span> company in Maine, in the north-east of the United States, went to <span class="cn-word" data-tr="sud">court</span> over a missing comma.</p>

<p><strong>The drivers' complaint</strong> was simple. They often worked more than forty hours a week, and they believed the company <span class="cn-word" data-pos="verb" data-tr="qarzdor boʻlmoq">owed</span> them <span class="cn-word" data-tr="qoʻshimcha ish haqi">overtime</span> pay. The company disagreed, and it pointed to a state law. The law listed the jobs that did not earn overtime<strong>: canning, processing, preserving, freezing, drying, marketing, storing, packing for shipment or distribution</strong> of food.</p>

<p>Read the end of that list slowly. Is distribution a <span class="cn-word" data-pos="adj" data-tr="alohida">separate</span> job on the list? Or is the job "packing for <span class="cn-word" data-tr="joʻnatish (yuk)">shipment</span> or <span class="cn-word" data-tr="tarqatish, yetkazish">distribution</span>", which the drivers never did? With one more comma — <strong>packing for shipment, or distribution</strong> — the answer would be clear: distribution would be its own <span class="cn-word" data-tr="band, element">item</span>, and the drivers would get nothing. Without the comma, the sentence could mean either thing.</p>

<p>The drivers' <span class="cn-word" data-tr="advokat">lawyer</span> made one point again and again<strong>: the drivers did not pack anything; they drove trucks.</strong> <strong>The company's lawyer</strong> made the opposite point: everybody knew what the law meant.</p>

<p>In March 2017 a federal <span class="cn-word" data-tr="apellatsiya (sudi)">appeals</span> court agreed with the drivers. The judge wrote that the law was <span class="cn-word" data-pos="adj" data-tr="ikki maʼnoli, noaniq">ambiguous</span>, and that in such a case it had to be read <strong>in the workers' favour</strong>. His <span class="cn-word" data-tr="sud qarori matni">opinion</span> began with a sentence that newspapers all over the world <span class="cn-word" data-pos="verb" data-tr="iqtibos keltirmoq">quoted</span>: "For want of a comma, we have this case."</p>

<p>The next year the company agreed to pay the drivers five million dollars.</p>

<p>Maine changed the law soon <span class="cn-word" data-pos="adv" data-tr="keyinroq">afterwards</span>. The new version does not <span class="cn-word" data-pos="verb" data-tr="tayanmoq">rely</span> on commas at all. It puts a <strong>semicolon</strong> between every item on the list<strong>: canning; processing; preserving;</strong> and so on, to the end. Nobody can read it in two ways again.</p>

<p>Lawyers still tell this story to young <span class="cn-word" data-tr="hamkasblar">colleagues</span>, and teachers tell it to <span class="cn-word" data-pos="adj" data-tr="zerikkan">bored</span> pupils. Its lesson fits in one line. A comma is not <span class="cn-word" data-tr="bezak">decoration</span>; sometimes it is worth five million dollars.</p>''',
        "questions": [
            {
                "text": "Why did the court decide for the drivers?",
                "choices": [
                    "Because the law could be read in two ways, so it was read in the workers' favour",
                    "Because the drivers had packed food for shipment",
                    "Because the company had no lawyer",
                ],
                "answer": 0,
                "explanation": "Sudya qonunni ikki maʼnoli (<i>ambiguous</i>) deb "
                               "topdi — bunday holatda u ishchilar foydasiga oʻqiladi.",
            },
            {
                "text": "Which sentence uses the semicolon correctly?",
                "choices": [
                    "The drivers did not pack anything; they drove trucks.",
                    "The drivers did not pack; anything they drove trucks.",
                    "The drivers; did not pack anything, they drove trucks.",
                ],
                "answer": 0,
                "explanation": "Nuqtali vergul <b>ikki toʻliq gapni</b> bogʻlaydi: "
                               "«The drivers did not pack anything» va «they drove "
                               "trucks» — ikkalasi ham alohida gap boʻla oladi.",
            },
            {
                "text": "How do you write 'the lawyer of the three drivers'?",
                "choices": [
                    "the drivers lawyer",
                    "the drivers' lawyer",
                    "the drivers's lawyer",
                ],
                "answer": 1,
                "explanation": "-s bilan tugagan koʻplikka faqat apostrof qoʻshiladi: "
                               "<b>drivers'</b>. Birlikda esa <i>driver's</i>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-82 — capitals & spelling   (the hotel in Samarkand)       [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Uzbekistan, English, Monday",
        "summary": (
            "PE-82 matni. Afsona Samarqanddagi mehmonxonaga ishga ariza "
            "yozdi — kichik harflar va xato yozilgan soʻzlar bilan. "
            "Ikkinchi urinishda esa xatoni mehmonxonaning oʻz eshigida topdi."
        ),
        "order":   82,
        "grammar": [
            {
                "pattern":  "capital letters — names, places, nationalities, languages, days, months, I",
                "meaning":  "Ingliz tilida bosh harf bilan yoziladi: ismlar va "
                            "unvonlar (<b>Mr Rustamov</b>), shahar va davlatlar "
                            "(<b>Samarkand, Uzbekistan</b>), millat va tillar "
                            "(<b>Uzbek, English</b>), hafta kunlari va oylar "
                            "(<b>Monday, September</b>) va <b>I</b>. Oʻzbek tilida "
                            "tillar, kunlar va oylar kichik harf bilan yoziladi — "
                            "shuning uchun bu bizning eng koʻp xatomiz.",
                "examples": ["I can start on Monday.", "I speak Uzbek, Russian and English.",
                             "Dear Mr Rustamov,"],
            },
            {
                "pattern":  "spelling: i before e · doubling · words learners misspell",
                "meaning":  "<b>receive</b> (c dan keyin <i>ei</i>), "
                            "<b>beginning</b> (urgʻuli qisqa boʻgʻinda undosh "
                            "ikkilanadi), <b>accommodation</b> (ikki c, ikki m), "
                            "<b>definitely</b>, <b>necessary</b> (bitta c, ikki s).",
                "examples": ["I look forward to receiving your reply.",
                             "the beginning of September", "ACCOMMODATION — 24 HOURS"],
            },
        ],
        "body": '''<p>Afsona was nineteen, and she wanted the job more than anything. The hotel was in the old part of Samarkand, five minutes from the Registan, and it needed a <span class="cn-word" data-tr="qabulxona xodimi">receptionist</span> who spoke English.</p>

<p>She wrote her letter on her phone, late at night, and sent it before she could change her mind. It began like this:</p>

<p><i>dear sir, my name is afsona karimova. i am from samarkand, uzbekistan. i speak uzbek, russian and english, and i can start on monday. i hope to recieve your answer.</i></p>

<p>Two days later the letter came back. The <span class="cn-word" data-tr="boshqaruvchi, menejer">manager</span>, <strong>Mr Rustamov</strong>, had <span class="cn-word" data-pos="verb" data-tr="chop etmoq">printed</span> it and drawn red <span class="cn-word" data-tr="doira">circles</span> round fourteen letters and one word. At the bottom he had written: "Your English is good; your capitals are not. Try again."</p>

<p>Afsona was <span class="cn-word" data-pos="adj" data-tr="xijolat boʻlgan">embarrassed</span> for an hour and busy for a week. She learned that English gives a capital letter to things that Uzbek does not: to <strong>English</strong> and <strong>Uzbek</strong>, to <strong>Monday</strong> and <strong>September</strong>, and always to <strong>I</strong>. She learned "<strong>i</strong> before <strong>e</strong>, <span class="cn-word" data-tr="bundan mustasno">except</span> after <strong>c</strong>", so <strong>receive</strong> and not <i>recieve</i>. She made a list of the words that learners <span class="cn-word" data-pos="verb" data-tr="xato yozmoq">misspell</span> most: <strong>accommodation</strong>, <strong>beginning</strong>, <strong>definitely</strong>, <strong>necessary</strong>.</p>

<p>On <strong>Monday</strong> she took the new letter to the hotel <span class="cn-word" data-tr="shaxsan">in person</span>.</p>

<p>She stopped at the door. Above it <span class="cn-word" data-pos="verb" data-tr="osilib turmoq">hung</span> a large <span class="cn-word" data-tr="lavha, yozuv">sign</span> in gold letters: <i>ACCOMODATION — 24 HOURS</i>.</p>

<p>Then she went in, gave Mr Rustamov her letter, and said, very quietly, that the sign over his door had only one <i>m</i>.</p>

<p>He went outside and looked at it for a long time. When he came back, he was laughing.</p>

<p>"That sign has been there for six years," he said. "Thousands of guests have walked under it. Tour <span class="cn-word" data-tr="gidlar">guides</span>, teachers, two <span class="cn-word" data-tr="elchilar">ambassadors</span>. You are the first person who has told me."</p>

<p>He read her new letter, found nothing to circle, and gave her the job.</p>

<p>Her first <span class="cn-word" data-tr="vazifa">task</span> on the first day was not at the <span class="cn-word" data-tr="qabul stoli">reception desk</span>. It was a phone call to the <span class="cn-word" data-tr="lavha yasovchi usta">sign-maker</span>, and she <span class="cn-word" data-pos="verb" data-tr="harfma-harf aytmoq">spelt</span> the word for him, letter by letter, <span class="cn-word" data-pos="adv" data-tr="ikki marta">twice</span>.</p>''',
        "questions": [
            {
                "text": "Why did Mr Rustamov give Afsona the job?",
                "choices": [
                    "Because she spoke three languages",
                    "Because her new letter was correct and she noticed the mistake on his sign",
                    "Because she lived near the Registan",
                ],
                "answer": 1,
                "explanation": "Yangi xatida birorta xato yoʻq edi — va olti yil "
                               "ichida hech kim koʻrmagan lavhadagi xatoni u topdi.",
            },
            {
                "text": "Which sentence uses capital letters correctly?",
                "choices": [
                    "i can start on monday, and I speak english.",
                    "I can start on Monday, and I speak english.",
                    "I can start on Monday, and I speak English.",
                ],
                "answer": 2,
                "explanation": "<b>I</b>, hafta kunlari (<b>Monday</b>) va tillar "
                               "(<b>English</b>) — har doim bosh harf bilan. "
                               "Oʻzbekchada esa «dushanba», «ingliz tili» kichik harf bilan.",
            },
            {
                "text": "Which word is spelt correctly?",
                "choices": ["accomodation", "accommodation", "acommodation"],
                "answer": 1,
                "explanation": "<b>accommodation</b> — ikki <i>c</i> va ikki <i>m</i>. "
                               "Bu soʻzni hatto mehmonxonalar ham xato yozadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-83 — emphasis with do   (an opinion column)             [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "I Do Believe It Works",
        "summary": (
            "PE-83 matni. Maktab direktorining gazetadagi ustuni: telefonlar "
            "darvozadagi shkafda qolgan bir yildan keyin nima oʻzgardi — va "
            "qoidaga eng qattiq qarshi chiqqan oʻquvchi hozir nima qilyapti."
        ),
        "order":   83,
        "grammar": [
            {
                "pattern":  "emphatic do / does / did + base verb",
                "meaning":  "Tasdiq gapga <b>do / does / did</b> qoʻshilsa, u "
                            "kuchayadi — koʻpincha shubhaga yoki teskari fikrga "
                            "javob sifatida: <i>I <b>did</b> expect complaints</i> "
                            "(«ha, rostdan kutgandim»). Feʼl asosiy shaklda "
                            "qoladi: <i>it <b>does</b> work</i>, <i>works</i> emas.",
                "examples": ["I did expect complaints.", "The rule does work.",
                             "They do talk to each other now."],
            },
            {
                "pattern":  "do + imperative = a warm invitation",
                "meaning":  "Buyruq oldidagi <b>do</b> majburlash emas, samimiylik "
                            "bildiradi: <i><b>Do</b> come and see us</i> — "
                            "«albatta keling».",
                "examples": ["Do come and see us.", "Do sit down."],
            },
        ],
        "body": '''<p><i>The headteacher of a school in Tashkent writes about the rule that everybody said would fail.</i></p>

<p>A year ago this September, our school <span class="cn-word" data-pos="verb" data-tr="joriy etmoq">introduced</span> one simple rule. Pupils put their phones into a <span class="cn-word" data-tr="qulfli shkafcha">locker</span> at the gate in the morning, and they take them back at four o'clock.</p>

<p>I <strong>did expect</strong> complaints, and they <strong>did come</strong>. Parents wrote to say that their children needed to reach them. Teachers asked who would <span class="cn-word" data-pos="verb" data-tr="nazorat qilmoq">supervise</span> three hundred lockers. And a boy in the eleventh grade, Bekzod, collected two hundred <span class="cn-word" data-tr="imzolar">signatures</span> on a <span class="cn-word" data-tr="petitsiya, ariza">petition</span> against the rule and left it on my desk with a <span class="cn-word" data-pos="adj" data-tr="xushmuomala">polite</span> note.</p>

<p>I read every letter, and I answered every one. Parents can call the school office at any time, and they still do. But I kept the rule, because I wanted to see what one year would show.</p>

<p>Here is what it showed. I am not a scientist, and one school is not a study, so I offer these as <span class="cn-word" data-tr="kuzatuvlar">observations</span>, not <span class="cn-word" data-tr="isbot">proof</span>.</p>

<p>The library <span class="cn-word" data-pos="verb" data-tr="qarzga bermoq">lent</span> more books in the autumn <span class="cn-word" data-tr="chorak, semestr">term</span> than in the whole of the previous year. The two table-tennis tables in the hall, which had stood <span class="cn-word" data-pos="adj" data-tr="foydalanilmay">unused</span> for years, now have a <span class="cn-word" data-tr="navbat">queue</span> at every break. And the noise in the <span class="cn-word" data-tr="oshxona (maktab)">canteen</span> has changed. It is louder. Pupils <strong>do talk</strong> to each other now, across tables, between classes, in a way that I had <span class="cn-word" data-pos="verb" data-tr="unutmoq">forgotten</span> was possible.</p>

<p>Not everything worked. Lockers broke, keys went missing, and one cold morning in January the queue at the gate reached the street. We have <span class="cn-word" data-pos="verb" data-tr="tuzatmoq">fixed</span> most of these problems, but not all.</p>

<p>And Bekzod? In October he started a chess club. It meets every lunch break in Room 14, and it now has forty-one members. Last month he wrote a short article for the school magazine. Its last line was this: "I <strong>did hate</strong> the rule. I <strong>do not hate</strong> it now, and I am a little <span class="cn-word" data-pos="adj" data-tr="jahli chiqqan">annoyed</span> about that."</p>

<p>So, after one year, my answer to the people who wrote to me is careful but clear. I <strong>do believe</strong> it works. If you <span class="cn-word" data-pos="verb" data-tr="shubhalanmoq">doubt</span> it, <strong>do come</strong> and see us at lunchtime — but bring a chess board.</p>''',
        "questions": [
            {
                "text": "What did Bekzod do after the rule was introduced?",
                "choices": [
                    "He changed schools",
                    "He started a chess club, although he had written a petition against the rule",
                    "He became the person who supervises the lockers",
                ],
                "answer": 1,
                "explanation": "Avval qoidaga qarshi petitsiya yozgan Bekzod "
                               "oktyabrda shaxmat klubini ochdi — hozir unda 41 aʼzo bor.",
            },
            {
                "text": "Why does the writer say 'I did expect complaints' instead of 'I expected complaints'?",
                "choices": [
                    "To add emphasis — yes, she really expected them",
                    "Because the sentence is a question",
                    "Because 'did' is needed in every past sentence",
                ],
                "answer": 0,
                "explanation": "<b>did + asosiy feʼl</b> tasdiq gapni kuchaytiradi: "
                               "«ha, rostdan ham kutgandim». Bu shakl odatda "
                               "faqat savol va inkorda keladi — tasdiqda esa urgʻu beradi.",
            },
            {
                "text": "Which sentence uses emphatic 'do' correctly?",
                "choices": ["The rule does works.", "The rule do work.", "The rule does work."],
                "answer": 2,
                "explanation": "<b>does</b> dan keyin feʼl asosiy shaklda: "
                               "<i>does work</i>. «does works» — ikki marta -s.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-84 — inversion   (a travel essay, Ugam-Chatkal)           [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Never Have I Seen Anything Like It",
        "summary": (
            "PE-84 matni. Sayohat esesi: Ugom-Chatqol togʻlarida tong otishi "
            "bilan qor qoplonini koʻrgan yozuvchi. Oʻn toʻqqiz yilda ikki "
            "marta koʻrgan qoʻriqchi esa nima uchun hech narsani "
            "suratga olmaganini tushuntiradi."
        ),
        "order":   84,
        "grammar": [
            {
                "pattern":  "negative / limiting word first + auxiliary + subject",
                "meaning":  "Gap <b>Never, Rarely, Seldom, Not until, Only when</b> "
                            "kabi soʻz bilan boshlansa, savoldagidek tartib keladi: "
                            "yordamchi feʼl + ega. <i>I have <b>never</b> seen</i> → "
                            "<i><b>Never have I</b> seen</i>. Yordamchi feʼl boʻlmasa — "
                            "<b>do / does / did</b>: <i>Only when he stopped "
                            "<b>did I</b> understand</i>. Bu yozma, rasmiy uslub.",
                "examples": ["Never have I been so cold.",
                             "Only when the ranger stopped did I understand.",
                             "Rarely does anyone see one."],
            },
            {
                "pattern":  "conditional inversion — Had I…, Should you…",
                "meaning":  "<b>if</b> tushib qoladi va yordamchi feʼl boshga chiqadi: "
                            "<i>If I had blinked</i> → <i><b>Had I</b> blinked</i>; "
                            "<i>If you ever go</i> → <i><b>Should you</b> ever go</i>.",
                "examples": ["Had I blinked, I would have missed it.",
                             "Should you ever go there, walk slowly."],
            },
        ],
        "body": '''<p><i>A writer remembers one morning in the Ugam-Chatkal National Park.</i></p>

<p><strong>Never have I been</strong> so cold, and <strong>never have I been</strong> so happy to be cold. We left the <span class="cn-word" data-tr="qoʻriqchi uyi, kordon">ranger's hut</span> at four in the morning, three of us in a line: Saidakbar, the ranger, at the front; a <span class="cn-word" data-tr="fotograf">photographer</span> from Almaty behind him; and me at the back. I was <span class="cn-word" data-pos="verb" data-tr="nafas olmoq">breathing</span> hard, and I wished I had stayed in bed.</p>

<p>Saidakbar has worked in these mountains for nineteen years. He knows every <span class="cn-word" data-tr="soʻqmoq">path</span> and every <span class="cn-word" data-tr="buloq">spring</span>, and he walks without a <span class="cn-word" data-tr="fonar">torch</span>. He told us before we started that we were not going to see a snow leopard. "<strong>Rarely does anyone</strong> see one," he said. "I have seen two, in nineteen years. We are going to see the <span class="cn-word" data-tr="togʻ echkilari">ibex</span>, and the <span class="cn-word" data-tr="quyosh chiqishi">sunrise</span>, and that is a lot."</p>

<p>We climbed for two hours. <strong>Not until</strong> the sky turned grey <strong>did we stop</strong>, on a flat rock above a long <span class="cn-word" data-tr="vodiy, dara">valley</span>. Saidakbar lifted his hand, and we sat down without a word.</p>

<p>For a long time there was nothing. Then a small group of ibex <span class="cn-word" data-pos="verb" data-tr="paydo boʻlmoq">appeared</span> on the <span class="cn-word" data-pos="adj" data-tr="qarshi tomondagi">opposite</span> <span class="cn-word" data-tr="togʻ tizmasi">ridge</span>, and the photographer began to lift his camera <span class="cn-word" data-pos="adv" data-tr="ehtiyotkorlik bilan">carefully</span>.</p>

<p>Saidakbar put his hand on the camera and pushed it down. <strong>Only when</strong> he pointed, very slowly, at the rocks below the ibex <strong>did I understand</strong> why.</p>

<p>It lay on a <span class="cn-word" data-tr="toshli qoya">ledge</span> in the first light, the colour of the stone around it. Then, for perhaps three seconds, it turned its head and looked straight at us. <strong>Had I blinked</strong>, I would have missed it.</p>

<p>When I looked again, the ledge was <span class="cn-word" data-pos="adj" data-tr="boʻsh">empty</span>.</p>

<p>Nobody spoke on the way down. At the hut, the photographer asked Saidakbar why he had stopped him. The ranger's answer was short. "The sound of a camera <span class="cn-word" data-pos="verb" data-tr="choʻchitmoq">frightens</span> it. The picture would be for you. The quiet was for the cat."</p>

<p><strong>Should you ever go</strong> to those mountains, walk slowly, keep your camera in your bag, and do not expect anything. <strong>Seldom does</strong> the mountain give you what you came for — but now and then it gives you something better.</p>''',
        "questions": [
            {
                "text": "Why did the ranger push the photographer's camera down?",
                "choices": [
                    "Because the light was too weak for a photograph",
                    "Because the sound of the camera would frighten the snow leopard",
                    "Because photographs are not allowed in the park",
                ],
                "answer": 1,
                "explanation": "Qoʻriqchi: «Kamera ovozi uni choʻchitadi» — surat "
                               "odam uchun, sukunat esa qoplon uchun edi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "Only when the ranger pointed I understood.",
                    "Only when the ranger pointed did I understand.",
                    "Only when did the ranger point I understood.",
                ],
                "answer": 1,
                "explanation": "<b>Only when + gap</b> boshda turganda, <b>asosiy</b> "
                               "gapda inversiya boʻladi: <i>did I understand</i>. "
                               "<i>Only when</i> ichidagi gapda tartib oʻzgarmaydi.",
            },
            {
                "text": "What does 'Had I blinked, I would have missed it' mean?",
                "choices": [
                    "If I had blinked, I would have missed it.",
                    "I blinked, so I missed it.",
                    "I had to blink to see it.",
                ],
                "answer": 0,
                "explanation": "Shart inversiyasi: <b>Had I…</b> = <b>If I had…</b>. "
                               "U koʻz yummadi — shuning uchun qoplonni koʻrdi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-85 — cleft sentences   (a letter to the editor)          [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "What This Town Needs Is a Library",
        "summary": (
            "PE-85 matni. Gazetaga xat: bir yil oldin shaharga kutubxona "
            "kerak deb yozgan nafaqadagi muhandis. Kengash pul yoʻq dedi — "
            "javobni esa oʻn ikki yoshli nevarasi topdi."
        ),
        "order":   85,
        "grammar": [
            {
                "pattern":  "the it-cleft: It was X who / that …",
                "meaning":  "Gapning bir qismini «yoritish» uchun: <i>My granddaughter "
                            "changed my mind</i> → <i><b>It was</b> my granddaughter "
                            "<b>who</b> changed my mind</i> — «aynan nevaram». "
                            "Koʻpincha tuzatish uchun ishlatiladi: <i>It is not money "
                            "that we lack.</i>",
                "examples": ["It was my granddaughter who changed my mind.",
                             "It is not money that this town lacks.",
                             "It is on Saturdays that the door opens."],
            },
            {
                "pattern":  "the what-cleft: What + clause + is / was …",
                "meaning":  "Harakat yoki ehtiyojni yoritadi: <i>This town needs a "
                            "library</i> → <i><b>What</b> this town needs <b>is</b> a "
                            "library</i>. Shu shakl <b>All</b> bilan ham ishlaydi: "
                            "<i><b>All</b> we needed <b>was</b> a door.</i>",
                "examples": ["What this town needs is a library.",
                             "What surprised me was the queue.",
                             "All we needed was a key."],
            },
        ],
        "body": '''<p><i>To the Editor,</i></p>

<p>A year ago you were kind enough to print a letter of mine. Its first sentence was "<strong>What this town needs is</strong> a library," and many readers wrote to agree with me. I am writing again because I owe them, and you, an <span class="cn-word" data-tr="hisobot">account</span> of what happened next.</p>

<p>After my letter, I went to the town <span class="cn-word" data-tr="kengash">council</span>. The <span class="cn-word" data-tr="amaldorlar">officials</span> were polite. They agreed that a library would be a fine thing. Then they showed me the <span class="cn-word" data-tr="byudjet">budget</span>, and there was no line in it for books, or a building, or a librarian. I came home <span class="cn-word" data-pos="adj" data-tr="tushkun">discouraged</span>, and I told my family that the idea was dead.</p>

<p><strong>It was my granddaughter who</strong> changed my mind. Sevara is twelve, and she does not <span class="cn-word" data-pos="verb" data-tr="sabr qilmoq">tolerate</span> <span class="cn-word" data-tr="bahonalar">excuses</span>, from me or from anyone. She listened to my story about the council and then asked a question that I have not stopped thinking about. "Grandfather, is a library a building? Or is it books and somebody to open the door?"</p>

<p>I had no answer. Seldom have I felt so <span class="cn-word" data-pos="adj" data-tr="kamtarona, ojiz">humbled</span> by a child.</p>

<p>That week we emptied my <span class="cn-word" data-tr="garaj">garage</span>. A neighbour who is a <span class="cn-word" data-tr="duradgor">carpenter</span> built the <span class="cn-word" data-tr="javonlar">shelves</span>, and I put a <span class="cn-word" data-tr="eʼlon">notice</span> on the gate asking for books. <strong>What surprised me was</strong> not that people gave. <strong>It was</strong> how much they gave. In six weeks we had four hundred books: novels, children's stories, <span class="cn-word" data-tr="lugʻatlar">dictionaries</span>, old <span class="cn-word" data-tr="darsliklar">textbooks</span>, and one beautiful atlas from 1974.</p>

<p>The library opens on Saturdays from ten until two. <strong>It is</strong> Sevara <strong>who</strong> keeps the <span class="cn-word" data-tr="qayd daftari">register</span> of who has borrowed what, and she is far stricter about late returns than I would be. Last Saturday thirty-one people came, and eleven of them were children.</p>

<p>So I must <span class="cn-word" data-pos="verb" data-tr="tuzatmoq">correct</span> my letter of last year. <strong>It is not money that</strong> this town lacks. <strong>What it lacked was</strong> a door that somebody was willing to open. <strong>All we needed was</strong> a garage, a carpenter, and a twelve-year-old who asked the right question.</p>

<p>Readers are welcome on any Saturday. Please bring a book — and please return it on time.</p>

<p><i>Karim Toshev, retired engineer</i></p>''',
        "questions": [
            {
                "text": "What question made the writer change his mind?",
                "choices": [
                    "Whether the council had money for books",
                    "Whether a library is a building, or books and somebody to open the door",
                    "Whether his garage was large enough",
                ],
                "answer": 1,
                "explanation": "Sevaraning savoli: kutubxona — binomi, yoki kitoblar "
                               "va eshikni ochadigan odammi? Shu savol uni harakatga undadi.",
            },
            {
                "text": "Which is a correct cleft sentence?",
                "choices": [
                    "What we need is more shelves.",
                    "What do we need is more shelves.",
                    "What we need it is more shelves.",
                ],
                "answer": 0,
                "explanation": "<b>What + oddiy tartibdagi gap + is</b>: "
                               "<i>What we need is…</i> Savol tartibi (<i>do we</i>) "
                               "bu yerda ishlatilmaydi.",
            },
            {
                "text": "In 'It was my granddaughter who changed my mind', what does the it-cleft put in the spotlight?",
                "choices": ["the time when he changed his mind", "the person who changed his mind", "the place where it happened"],
                "answer": 1,
                "explanation": "<b>It was X who…</b> — X ni yoritadi: «aynan "
                               "nevaram» (kengash ham, qoʻshnilar ham emas).",
            },
        ],
    },
]
