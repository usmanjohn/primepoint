# -*- coding: utf-8 -*-
"""Prime English Readings — PE-1 … PE-5 (batch 1).

The third leg of each Prime English lesson: the tutorial teaches the pattern,
the practice drills it, the reading shows it living in a text. Story `order`
IS the lesson number, so PE-4's reading is order 4.

Language policy (the mirror of Prime Korean, which is taught in Uzbek):
story text and questions in ENGLISH, glosses / summaries / explanations in UZBEK.

Cumulative rule: these five readings sit before "to be" (PE-6), present simple
(PE-9) and any past tense (PE-19+), so they use the narrative-frame exception
allowed by the toc — is / are, a / an / the, and, but, has, in / on / at and
plural -s as plain frame vocabulary — and nothing else from later lessons.
Each focus pattern is <strong>bolded</strong> where it appears, with vocab marks
kept off the bolded words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_01_05.py --author=prime
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
    # PE-1 — subject + verb
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The First Day",
        "summary": (
            "PE-1 matni. Sherbek yangi maktabda birinchi kunini oʻtkazadi. "
            "Matndagi har bir gap eng sodda qolipda: EGA + KESIM."
        ),
        "order":   1,
        "grammar": [
            {
                "pattern":  "Subject + verb",
                "meaning":  "Ingliz gapining yuragi — ega va kesim. Matndagi "
                            "har bir gapda kim (yoki nima) va nima qilishi bor. "
                            "Qolgan hamma narsa — shu ikkitasining ustiga "
                            "qoʻshiladi.",
                "examples": ["Sherbek walks.", "Children run.", "The lesson starts."],
            },
            {
                "pattern":  "A sentence needs a verb",
                "meaning":  "Oʻzbekchada “Men oʻquvchiman” deyish mumkin — feʼl "
                            "qoʻshimcha ichida yashiringan. Inglizchada esa feʼl "
                            "koʻrinib turishi kerak: <b>I am a pupil</b>. Feʼlsiz "
                            "gap yoʻq.",
                "examples": ["Sherbek is a pupil.", "The gate is open."],
            },
            {
                "pattern":  "he / she / it + verb-s",
                "meaning":  "Uchinchi shaxs birlikda feʼlga <b>-s</b> qoʻshiladi. "
                            "Matnda buni koʻrishingiz mumkin: <i>he walks</i>, "
                            "<i>she smiles</i>, <i>the wind blows</i>. PE-9 da "
                            "batafsil oʻrganamiz.",
                "examples": ["She smiles.", "He opens his bag."],
            },
        ],
        "body": '''<p><strong>Sherbek walks</strong>. The road is long. The new school is at the end of the street.</p>

<p>The <span class="cn-word" data-tr="darvoza">gate</span> is open. <strong>Children run</strong>. A teacher <span class="cn-word" data-pos="verb" data-tr="kutadi">waits</span> near the door. She smiles.</p>

<p>Sherbek stops. He <span class="cn-word" data-pos="verb" data-tr="nafas oladi">breathes</span>. Then he walks in.</p>

<p>In class, a girl sits near the window. She reads. Her name is Afsona.</p>

<p>"Hello," she says. "Sit here."</p>

<p><strong>Sherbek sits</strong>. He opens his bag. He takes a pen. The lesson <span class="cn-word" data-pos="verb" data-tr="boshlanadi">starts</span>.</p>

<p>Outside, the <span class="cn-word" data-tr="shamol">wind</span> <span class="cn-word" data-pos="verb" data-tr="esadi">blows</span>. Inside, twenty children <span class="cn-word" data-pos="verb" data-tr="tinglaydi">listen</span>. <strong>Sherbek smiles</strong>. The first day is not <span class="cn-word" data-pos="adj" data-tr="qiyin">difficult</span>.</p>''',
        "questions": [
            {
                "text": "Where does Afsona sit?",
                "choices": [
                    "Near the door",
                    "Near the window",
                    "Near the teacher",
                ],
                "answer": 1,
                "explanation": "“In class, a girl sits near the window… Her name is "
                               "Afsona.” — u deraza yonida oʻtiradi.",
            },
            {
                "text": "In the sentence \"Children run.\", which word is the verb?",
                "choices": ["Children", "run", "There is no verb"],
                "answer": 1,
                "explanation": "<b>Children</b> — ega (kim?), <b>run</b> — kesim "
                               "(nima qiladi?). Ikkisi birga eng qisqa ingliz gapini "
                               "hosil qiladi.",
            },
            {
                "text": "How is the first day for Sherbek?",
                "choices": [
                    "It is not difficult",
                    "It is very long and hard",
                    "He goes home early",
                ],
                "answer": 0,
                "explanation": "Oxirgi gap: “The first day is not difficult.” "
                               "Sherbek kirishdan oldin qoʻrqadi, lekin kun oxirida "
                               "jilmayadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-2 — countable / uncountable nouns
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bread, Water and Two Eggs",
        "summary": (
            "PE-2 matni. Dilnoza onasining roʻyxati bilan doʻkonga boradi — va "
            "“ikki kilo guruch” bilan “ikkita guruch” orasidagi farqni doʻkondorning "
            "kulgisidan oʻrganadi."
        ),
        "order":   2,
        "grammar": [
            {
                "pattern":  "Countable: two eggs, three apples",
                "meaning":  "Sanaladigan otlar sanoqni yonida koʻtaradi va "
                            "koʻplik shakli bor: <i>egg → two eggs</i>, "
                            "<i>apple → three apples</i>.",
                "examples": ["Dilnoza takes two eggs.", "She buys three apples."],
            },
            {
                "pattern":  "Uncountable: bread, water, rice, tea",
                "meaning":  "Sanalmaydigan otlar oldida son turmaydi va "
                            "koʻplik qoʻshimchasi olmaydi: <i>bread</i>, "
                            "<i>water</i>, <i>rice</i>, <i>tea</i>. "
                            "“Two rices” — xato.",
                "examples": ["Rice is not a number.", "The tea is hot."],
            },
            {
                "pattern":  "a loaf of bread · a bottle of water · a kilo of rice",
                "meaning":  "Sanalmaydigan otni sanash kerak boʻlsa, oldiga "
                            "<b>oʻlchov soʻzi</b> qoʻyiladi. Oʻzbekchada ham "
                            "aynan shunday: <i>bir boʻlak non</i>, "
                            "<i>bir shisha suv</i>, <i>bir kilo guruch</i>.",
                "examples": ["a loaf of bread", "a bottle of water", "a kilo of rice"],
            },
        ],
        "body": '''<p>Dilnoza has a <span class="cn-word" data-tr="roʻyxat">list</span>. Her mother writes it every Saturday.</p>

<p>The list is short: <strong>bread</strong>, <strong>water</strong>, <strong>two eggs</strong>, <strong>rice</strong> and <strong>three apples</strong>.</p>

<p>In the shop, Dilnoza takes a <span class="cn-word" data-tr="savat">basket</span>. She finds the bread first and takes <strong>a loaf of bread</strong>. Then she takes <strong>a bottle of water</strong>.</p>

<p>"The eggs are here," a woman near the <span class="cn-word" data-tr="raf">shelf</span> says. Dilnoza takes two eggs. She <span class="cn-word" data-pos="verb" data-tr="sanaydi">counts</span> them <span class="cn-word" data-pos="adv" data-tr="ehtiyotkorlik bilan">carefully</span>.</p>

<p>The rice is in a big <span class="cn-word" data-tr="qop">sack</span>. "Two rices, please," Dilnoza says.</p>

<p>The <span class="cn-word" data-tr="doʻkondor">shopkeeper</span> <span class="cn-word" data-pos="verb" data-tr="kuladi">laughs</span>. "<strong>A kilo of rice</strong>," he says. "Rice is not a number."</p>

<p>At home her mother checks the bag. Bread, water, eggs, rice, apples. Nothing is <span class="cn-word" data-pos="adj" data-tr="yoʻq, kam">missing</span>. The tea is hot and the morning is <span class="cn-word" data-pos="adj" data-tr="tinch">quiet</span>.</p>''',
        "questions": [
            {
                "text": "Why does the shopkeeper laugh?",
                "choices": [
                    "Dilnoza's list is too long",
                    "Dilnoza says \"two rices\", but rice is uncountable",
                    "Dilnoza forgets the money at home",
                ],
                "answer": 1,
                "explanation": "“Two rices, please” — guruch sanalmaydi, shuning "
                               "uchun doʻkondor toʻgʻri shaklni aytadi: "
                               "<b>a kilo of rice</b>.",
            },
            {
                "text": "Which line is correct English?",
                "choices": [
                    "Three waters and two breads",
                    "A bottle of water and a loaf of bread",
                    "A water and a bread",
                ],
                "answer": 1,
                "explanation": "Sanalmaydigan otlar oʻlchov soʻzi bilan sanaladi: "
                               "<i>a bottle of water</i>, <i>a loaf of bread</i>.",
            },
            {
                "text": "What does the mother do at the end?",
                "choices": [
                    "She checks the bag and nothing is missing",
                    "She sends Dilnoza back to the shop",
                    "She writes a new list",
                ],
                "answer": 0,
                "explanation": "“At home her mother checks the bag… Nothing is "
                               "missing.” Roʻyxatdagi hamma narsa joyida.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-3 — plural nouns, regular and irregular
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Six Children, Three Buses",
        "summary": (
            "PE-3 matni. Maktab qishloqqa sayohatga boradi — va bir kunda "
            "buses, children, women, sheep, leaves, knives, feet: koʻplikning "
            "hamma turi bir matnda uchraydi."
        ),
        "order":   3,
        "grammar": [
            {
                "pattern":  "-s / -es (bus → buses, tomato → tomatoes)",
                "meaning":  "Oddiy koʻplik <b>-s</b> bilan yasaladi. Agar soʻz "
                            "-s, -ss, -sh, -ch, -x, -o bilan tugasa, talaffuz "
                            "uchun <b>-es</b> qoʻshiladi.",
                "examples": ["Three buses wait at the gate.",
                             "They eat sandwiches and tomatoes."],
            },
            {
                "pattern":  "-f / -fe → -ves (knife → knives, leaf → leaves)",
                "meaning":  "Bir guruh soʻzda oxirgi <i>-f</i> koʻplikda "
                            "<b>-ves</b> ga aylanadi: knife, leaf, wife, life, "
                            "half, shelf, wolf.",
                "examples": ["Two knives cut the bread.",
                             "Leaves fall on their heads."],
            },
            {
                "pattern":  "Irregular: child → children, woman → women, foot → feet",
                "meaning":  "Bir nechta soʻz butunlay oʻzgaradi — bularni "
                            "yodlash kerak: child–children, man–men, "
                            "woman–women, foot–feet, tooth–teeth. "
                            "Va <i>sheep</i>, <i>fish</i> hech qanday "
                            "oʻzgarmaydi.",
                "examples": ["Every bus has thirty children.",
                             "Their feet hurt.", "One sheep, ten sheep."],
            },
        ],
        "body": '''<p>On Friday, the school goes to a <span class="cn-word" data-tr="qishloq">village</span>. Three <strong>buses</strong> wait at the gate.</p>

<p>Every bus has thirty <strong>children</strong>. Two <strong>women</strong> and one man <span class="cn-word" data-pos="verb" data-tr="safar qiladi">travel</span> with them. The <strong>men</strong> in the village know the teacher well.</p>

<p>In the village there are <strong>sheep</strong> <span class="cn-word" data-pos="adv" data-tr="hamma yerda">everywhere</span>. "One sheep, ten sheep," Jasur says. "The word is the same."</p>

<p>The children walk under the trees. <strong>Leaves</strong> <span class="cn-word" data-pos="verb" data-tr="tushadi">fall</span> on their heads. Afsona counts them: ten, twenty, fifty.</p>

<p>At one o'clock they eat <strong>sandwiches</strong> and <strong>tomatoes</strong>. Two <strong>knives</strong> cut the bread. Nobody is <span class="cn-word" data-pos="adj" data-tr="och">hungry</span> after that.</p>

<p>At five o'clock their <strong>feet</strong> <span class="cn-word" data-pos="verb" data-tr="ogʻriydi">hurt</span> and their bags are heavy. But nobody <span class="cn-word" data-pos="verb" data-tr="shikoyat qiladi">complains</span>. The buses are <span class="cn-word" data-pos="adj" data-tr="iliq">warm</span>, and thirty children in every bus sleep all the way home.</p>''',
        "questions": [
            {
                "text": "How many children travel in each bus?",
                "choices": ["Six", "Thirty", "Fifty"],
                "answer": 1,
                "explanation": "“Every bus has thirty children.” Uchta avtobus "
                               "boʻlsa ham, savol bittasi haqida.",
            },
            {
                "text": "Which plural is written correctly?",
                "choices": [
                    "two knifes, ten sheeps, three womans",
                    "two knives, ten sheep, three women",
                    "two knive, ten sheeps, three womens",
                ],
                "answer": 1,
                "explanation": "knife → <b>knives</b> (-f → -ves), sheep → "
                               "<b>sheep</b> (oʻzgarmaydi), woman → <b>women</b> "
                               "(notoʻgʻri koʻplik).",
            },
            {
                "text": "Why does nobody complain at five o'clock?",
                "choices": [
                    "Because the day was good and the buses are warm",
                    "Because the teacher is angry",
                    "Because they are still hungry",
                ],
                "answer": 0,
                "explanation": "Oyoqlari ogʻriydi, sumkalari ogʻir — lekin "
                               "avtobuslar iliq va bolalar uyga qadar uxlaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-4 — a / an / the / zero article
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "A Dog in the Yard",
        "summary": (
            "PE-4 matni. Bekzodning hovlisiga bir kuchuk keladi — va matn "
            "davomida u “a dog” dan “the dog” ga aylanadi. Artikllar aynan "
            "shu tarzda ishlaydi."
        ),
        "order":   4,
        "grammar": [
            {
                "pattern":  "a / an — first mention",
                "meaning":  "Narsa <b>birinchi marta</b> tilga olinganda "
                            "<i>a</i> (yoki unli tovush oldidan <i>an</i>) "
                            "ishlatiladi: tinglovchi uni hali bilmaydi.",
                "examples": ["There is a dog in our yard.",
                             "Bekzod brings water in a bowl."],
            },
            {
                "pattern":  "the — we both know which one",
                "meaning":  "Ikkinchi martadan boshlab — yoki dunyoda "
                            "yakka boʻlgan narsalar oldida — <b>the</b> "
                            "keladi: gapiruvchi ham, tinglovchi ham "
                            "qaysi biri ekanini biladi.",
                "examples": ["The dog sits near the door.",
                             "The sun goes down."],
            },
            {
                "pattern":  "Zero article — Dogs are hungry in winter",
                "meaning":  "Umuman, hamma haqida gapirilsa, koʻplik ot "
                            "oldida <b>artikl yoʻq</b>. Oʻzbekchada ham "
                            "shunday: “Kuchuklar qishda och boʻladi”.",
                "examples": ["Dogs are hungry in winter.", "Winter is long here."],
            },
        ],
        "body": '''<p>One morning there is <strong>a dog</strong> in our <span class="cn-word" data-tr="hovli">yard</span>. It is small and <span class="cn-word" data-pos="adj" data-tr="jigarrang">brown</span>.</p>

<p><strong>The dog</strong> sits near the door. It does not <span class="cn-word" data-pos="verb" data-tr="huradi">bark</span>. Bekzod brings water in <strong>a bowl</strong>. <strong>The bowl</strong> is <span class="cn-word" data-pos="adj" data-tr="boʻsh">empty</span> in one minute.</p>

<p>"<strong>Dogs</strong> are hungry in winter," his grandmother says. "And winter here is long."</p>

<p>Bekzod's sister brings <strong>an old blanket</strong> from the house. The dog sleeps on it under the <span class="cn-word" data-tr="zinapoya">stairs</span>.</p>

<p>In the evening the dog is <span class="cn-word" data-pos="adv" data-tr="hamon">still</span> there. <strong>The sun</strong> goes down. The yard is quiet, and the small brown <span class="cn-word" data-tr="mehmon">guest</span> is not <span class="cn-word" data-pos="adj" data-tr="qoʻrqqan">afraid</span> any more.</p>

<p>Now the dog has a name: Bulut. It is not <strong>a</strong> dog in our yard. It is <strong>the</strong> dog of this house.</p>''',
        "questions": [
            {
                "text": "Why is it \"a dog\" in the first line but \"the dog\" in the second?",
                "choices": [
                    "Because the dog is small",
                    "Because the reader now knows which dog we mean",
                    "Because there are two different dogs",
                ],
                "answer": 1,
                "explanation": "Birinchi eslatishda <b>a</b>, keyin esa "
                               "oʻqigan odam qaysi kuchuk ekanini biladi — "
                               "shuning uchun <b>the</b>.",
            },
            {
                "text": "The grandmother says \"Dogs are hungry in winter.\" Why is there no article?",
                "choices": [
                    "Because she is talking about dogs in general",
                    "Because \"dogs\" is uncountable",
                    "Because she forgets the word \"the\"",
                ],
                "answer": 0,
                "explanation": "Umumiy gap — koʻplik ot oldida artikl "
                               "qoʻyilmaydi. Faqat oʻsha hovlidagi kuchuklar "
                               "haqida boʻlsa, <i>the dogs</i> boʻlar edi.",
            },
            {
                "text": "What changes for the dog at the end of the story?",
                "choices": [
                    "It gets a name and a home",
                    "It goes back to the street",
                    "It stops eating",
                ],
                "answer": 0,
                "explanation": "“Now the dog has a name: Bulut… It is <b>the</b> "
                               "dog of this house.” Artiklning oʻzgarishi "
                               "hikoyaning oʻzgarishini koʻrsatadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-5 — pronouns: subject, object, possessive
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "It Is Not Mine",
        "summary": (
            "PE-5 matni. Sinfda qolgan qora soyabon kimniki? Butun matn "
            "olmoshlar ustida quriladi: I – me – my – mine, she – her – hers."
        ),
        "order":   5,
        "grammar": [
            {
                "pattern":  "Subject pronouns: I, you, he, she, it, we, they",
                "meaning":  "Ega oʻrnida turadigan olmoshlar — feʼldan oldin "
                            "keladi. Inglizchada ega tushib qolmaydi: "
                            "oʻzbekcha “Uyda qoldirdim” — inglizcha "
                            "<b>I</b> left it at home.",
                "examples": ["I left it at home.", "We keep it near the door."],
            },
            {
                "pattern":  "Object pronouns: me, you, him, her, it, us, them",
                "meaning":  "Feʼldan yoki predlogdan <b>keyin</b> keladi: "
                            "<i>She looks at it</i>, <i>Afsona gives him the "
                            "umbrella</i>. “Gives he” deb aytilmaydi.",
                "examples": ["She looks at it.", "Afsona gives him the umbrella."],
            },
            {
                "pattern":  "my book / mine — the two possessive forms",
                "meaning":  "<b>my, your, his, her, our, their</b> — otdan "
                            "oldin turadi. <b>mine, yours, his, hers, ours, "
                            "theirs</b> — otning oʻzini almashtiradi va "
                            "yolgʻiz turadi: <i>My umbrella is blue</i> / "
                            "<i>It is not mine</i>.",
                "examples": ["My umbrella is blue.", "It is not mine.",
                             "That is ours!"],
            },
        ],
        "body": '''<p>After the lesson there is a black <span class="cn-word" data-tr="soyabon">umbrella</span> on the <span class="cn-word" data-tr="pol">floor</span>. Nobody takes it.</p>

<p>"Is it <strong>yours</strong>?" Afsona asks Jasur.</p>

<p>"No, it is not <strong>mine</strong>," he says. "<strong>My</strong> umbrella is blue. <strong>I</strong> leave <strong>it</strong> at home on sunny days."</p>

<p>Afsona shows the umbrella to Dilnoza. <strong>She</strong> looks at <strong>it</strong> and <span class="cn-word" data-pos="verb" data-tr="bosh chayqaydi">shakes her head</span>.</p>

<p>"It is not <strong>hers</strong> <span class="cn-word" data-pos="adv" data-tr="ham (inkorda)">either</span>," Jasur says. "<strong>Her</strong> umbrella is small and red."</p>

<p>Mr Karimov comes in. Afsona gives <strong>him</strong> the umbrella.</p>

<p>"Thank you," he says. "<strong>They</strong> <span class="cn-word" data-pos="verb" data-tr="yoʻqotadi">lose</span> everything, these children. Last month somebody leaves a <span class="cn-word" data-tr="poyabzal">shoe</span> in this room. One shoe!"</p>

<p>Two days <span class="cn-word" data-pos="adv" data-tr="keyinroq">later</span> Sherbek sees the umbrella in the teachers' room. "That is <strong>ours</strong>!" he says. "It is the class umbrella. <strong>We</strong> keep it near the door for <span class="cn-word" data-pos="adj" data-tr="yomgʻirli">rainy</span> days."</p>''',
        "questions": [
            {
                "text": "Whose umbrella is it?",
                "choices": [
                    "Jasur's",
                    "Dilnoza's",
                    "The class umbrella",
                ],
                "answer": 2,
                "explanation": "Oxirida Sherbek aytadi: “That is <b>ours</b>! "
                               "It is the class umbrella.” Yaʼni u butun sinfga "
                               "tegishli.",
            },
            {
                "text": "Jasur says: \"__ umbrella is blue. It is not __.\" Which pair is correct?",
                "choices": [
                    "My … mine",
                    "Mine … my",
                    "My … my",
                ],
                "answer": 0,
                "explanation": "<b>My</b> otdan oldin turadi (my umbrella), "
                               "<b>mine</b> esa yolgʻiz turadi va otni "
                               "almashtiradi (it is not mine).",
            },
            {
                "text": "Which sentence from the story uses an OBJECT pronoun?",
                "choices": [
                    "She looks at it.",
                    "My umbrella is blue.",
                    "Her umbrella is small and red.",
                ],
                "answer": 0,
                "explanation": "<i>at</i> — predlog, undan keyin obyekt shakli "
                               "keladi: <b>at it</b>. Qolgan ikkitasi — egalik "
                               "aniqlovchisi (<i>my</i>, <i>her</i>) + ot.",
            },
        ],
    },
]
