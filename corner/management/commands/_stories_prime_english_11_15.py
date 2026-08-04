# -*- coding: utf-8 -*-
"""Prime English Readings — PE-11 … PE-15 (batch 3).

PE-11 adverbs of frequency · PE-12 present continuous · PE-13 simple vs
continuous · PE-14 have / have got · PE-15 adjectives (meaning, position, order).

Cumulative rule: everything up to PE-10 is free (present simple + negatives and
questions, to be, there is/are, this/that, articles, plurals, pronouns).
PE-12 opens the continuous, so PE-11 stays entirely in the simple. Still NO past
tense (PE-19+), NO comparatives (PE-67) — PE-15's bicycle is never "faster than"
anything — and no modals (PE-42+).

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_11_15.py --author=prime
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
    # PE-11 — adverbs of frequency
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "He Never Says No",
        "summary": (
            "PE-11 matni. Jasur hech qachon “yoʻq” demaydi — lekin bir kuni "
            "qoʻlini koʻtarmaydi. Takrorlanish ravishlari: always, usually, "
            "often, sometimes, never."
        ),
        "order":   11,
        "grammar": [
            {
                "pattern":  "always · usually · often · sometimes · never",
                "meaning":  "Ish qanchalik tez-tez boʻlishini koʻrsatadi va "
                            "asosiy feʼldan <b>oldin</b> turadi: "
                            "<i>He <b>always</b> carries…</i>, "
                            "<i>He <b>often</b> lends…</i>",
                "examples": ["He always carries the water bottles.",
                             "He often lends his pen."],
            },
            {
                "pattern":  "But AFTER the verb \"to be\"",
                "meaning":  "“Boʻlmoq” feʼli bilan tartib teskari: ravish "
                            "<b>keyin</b> keladi — <i>He <b>is never</b> "
                            "late</i>, <i>She <b>is always</b> ready</i>. "
                            "“He never is late” — xato.",
                "examples": ["He is always the first pupil in the room.",
                             "He is never late."],
            },
            {
                "pattern":  "never = negative on its own",
                "meaning":  "Inglizchada bitta inkor yetarli: <i>He never "
                            "says no</i>. Oʻzbekchada esa “hech qachon” "
                            "feʼlga ham inkor talab qiladi — “hech qachon "
                            "<b>aytmaydi</b>”. Shuning uchun "
                            "<i>He doesn't never say</i> — xato.",
                "examples": ["Jasur never says no.", "He is never late."],
            },
        ],
        "body": '''<p>Jasur <strong>never says</strong> no.</p>

<p>He <strong>always carries</strong> the water bottles up to the third floor. He <strong>usually stays</strong> after the lesson and <span class="cn-word" data-pos="verb" data-tr="tozalaydi">cleans</span> the <span class="cn-word" data-tr="doska">blackboard</span>. He <strong>often lends</strong> his pen, and <strong>sometimes</strong> he <span class="cn-word" data-pos="verb" data-tr="qarz beradi">lends</span> two.</p>

<p>He <strong>is always</strong> the first pupil in the room, and he <strong>is never</strong> late.</p>

<p>"Do you <strong>ever</strong> say no?" Afsona asks him.</p>

<p>"I <strong>rarely</strong> think about it," Jasur says.</p>

<p>On Thursday the teacher needs one pupil for the school concert. Twenty hands go up. Jasur's hand <strong>stays</strong> down.</p>

<p>"You <strong>never say</strong> no," the teacher says. "Why now?"</p>

<p>"Because Dilnoza <strong>always sings</strong> at home and nobody <span class="cn-word" data-pos="verb" data-tr="eshitadi">hears</span> her," Jasur says. "Today she needs the answer, not me."</p>

<p>Dilnoza sings at the concert. Jasur <strong>usually sits</strong> in the last <span class="cn-word" data-tr="qator">row</span>, and that evening he sits there too. He <span class="cn-word" data-pos="verb" data-tr="qarsak chaladi">claps</span> the <span class="cn-word" data-pos="adj" data-tr="eng baland">loudest</span>.</p>''',
        "questions": [
            {
                "text": "Why does Jasur keep his hand down on Thursday?",
                "choices": [
                    "He does not like concerts",
                    "He wants Dilnoza to get the place",
                    "He is never in school on Thursdays",
                ],
                "answer": 1,
                "explanation": "“Dilnoza always sings at home and nobody hears "
                               "her… Today she needs the answer, not me.” "
                               "Yaʼni bu ham yordam — faqat boshqa shaklda.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "He never is late.",
                    "He is never late.",
                    "He is not never late.",
                ],
                "answer": 1,
                "explanation": "<i>be</i> feʼli bilan ravish <b>keyin</b> "
                               "keladi: <b>is never</b>. Boshqa feʼllar "
                               "bilan esa oldin: <i>never says</i>.",
            },
            {
                "text": "Where does Jasur usually sit at a concert?",
                "choices": ["In the first row", "On the stage", "In the last row"],
                "answer": 2,
                "explanation": "“Jasur usually sits in the last row.” "
                               "<i>usually</i> — odat, shuning uchun oddiy "
                               "hozirgi zamon.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-12 — present continuous
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Rain Is Starting",
        "summary": (
            "PE-12 matni. Soat toʻrtda osmon qorayadi, yomgʻir boshlanadi — "
            "va hamma bir daraxt tagida toʻxtaydi. Hammasi shu daqiqada "
            "sodir boʻlmoqda."
        ),
        "order":   12,
        "grammar": [
            {
                "pattern":  "am / is / are + verb-ing",
                "meaning":  "Aynan <b>shu daqiqada</b> davom etayotgan ish. "
                            "Ikki qismli: <i>be</i> feʼli shaxsga qarab "
                            "oʻzgaradi, asosiy feʼl esa <b>-ing</b> oladi. "
                            "Ikkinchisini tashlab ketish — eng koʻp "
                            "uchraydigan xato.",
                "examples": ["The rain is starting.",
                             "Six boys are playing football."],
            },
            {
                "pattern":  "Negative and question",
                "meaning":  "Inkor: <i>be</i> dan keyin <b>not</b> — "
                            "<i>She is not playing</i>. Savol: <i>be</i> "
                            "oldinga chiqadi — <i>Are you coming?</i> "
                            "<i>do/does</i> bu zamonda ishlatilmaydi.",
                "examples": ["She is not playing today.",
                             "Is anybody going home?"],
            },
            {
                "pattern":  "-ing spelling: run → running, lie → lying",
                "meaning":  "Qisqa unli + bitta undosh bilan tugasa, "
                            "undosh ikkilanadi: <i>run → running</i>, "
                            "<i>get → getting</i>, <i>sit → sitting</i>. "
                            "<i>-ie</i> esa <i>-y</i> ga aylanadi: "
                            "<i>lie → lying</i>. Oxirgi <i>-e</i> tushadi: "
                            "<i>come → coming</i>.",
                "examples": ["Sherbek is running with the ball.",
                             "The ball is lying in the water."],
            },
        ],
        "body": '''<p>Look at the <span class="cn-word" data-tr="osmon">sky</span>. It <strong>is getting</strong> <span class="cn-word" data-pos="adj" data-tr="qorongʻi">dark</span> at four o'clock.</p>

<p>"The rain <strong>is starting</strong>," Dilnoza says. "<strong>Are</strong> you <strong>coming</strong>?"</p>

<p>In the yard six boys <strong>are playing</strong> football. Nobody <strong>is listening</strong> to her. Sherbek <strong>is running</strong> with the ball and Jasur <strong>is</strong> <span class="cn-word" data-pos="verb" data-tr="baqiradi">shouting</span> his name.</p>

<p>Afsona <strong>is sitting</strong> under the tree. She <strong>is not playing</strong> today; she <strong>is reading</strong>.</p>

<p>Then the first big <span class="cn-word" data-tr="tomchilar">drops</span> <strong>are falling</strong> on her pages.</p>

<p>Now everybody <strong>is running</strong>, and they <strong>are all going</strong> in the same <span class="cn-word" data-tr="yoʻnalish">direction</span>: to the tree.</p>

<p>Eight pupils <strong>are standing</strong> under one tree. The ball <strong>is</strong> <span class="cn-word" data-pos="verb" data-tr="yotmoqda">lying</span> in the water. Afsona's book <strong>is getting</strong> wet and she <strong>is laughing</strong>.</p>

<p>"<strong>Is</strong> anybody <strong>going</strong> home?" Dilnoza asks.</p>

<p>Nobody <strong>is moving</strong>.</p>''',
        "questions": [
            {
                "text": "What is Afsona doing at the beginning of the story?",
                "choices": [
                    "She is playing football",
                    "She is reading under the tree",
                    "She is going home",
                ],
                "answer": 1,
                "explanation": "“Afsona is sitting under the tree… she is "
                               "reading.” Oʻyinda emas — kitob oʻqiyapti.",
            },
            {
                "text": "Which sentence is correct present continuous?",
                "choices": [
                    "The rain starting now.",
                    "The rain is starting now.",
                    "The rain is start now.",
                ],
                "answer": 1,
                "explanation": "Ikki qism kerak: <b>is</b> + <b>starting</b>. "
                               "Biri tushib qolsa, gap buziladi.",
            },
            {
                "text": "Why does nobody move at the end?",
                "choices": [
                    "They are enjoying the rain together",
                    "The gate is locked",
                    "They are waiting for the teacher",
                ],
                "answer": 0,
                "explanation": "Kitob hoʻl boʻlyapti, lekin Afsona kulyapti "
                               "va hech kim ketmayapti — yomgʻir ularga "
                               "yoqyapti.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-13 — present simple vs present continuous
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Usually She Walks, Today She Runs",
        "summary": (
            "PE-13 matni. Afsona har kuni sekin yuradi — bugun esa yugurib "
            "ketmoqda. Bir matnda ikki zaman: odat va shu daqiqa."
        ),
        "order":   13,
        "grammar": [
            {
                "pattern":  "Simple = usually · Continuous = now",
                "meaning":  "Oddiy hozirgi zamon — <b>odat</b>: "
                            "<i>She usually walks</i>. Davomli zamon — "
                            "<b>shu daqiqa</b>: <i>Today she is "
                            "running</i>. Bitta matnda ikkisi yonma-yon "
                            "kelsa, farq darhol koʻrinadi.",
                "examples": ["Afsona usually walks to school.",
                             "Today she is running."],
            },
            {
                "pattern":  "Signal words",
                "meaning":  "<b>every day, usually, always, never, on "
                            "Mondays</b> → oddiy zamon. "
                            "<b>now, today, at the moment, look!</b> → "
                            "davomli zamon. Signal soʻzni topsangiz, "
                            "zamonni tanlash oson.",
                "examples": ["Every morning he walks with her.",
                             "This morning he is waiting at the corner."],
            },
            {
                "pattern":  "State verbs take no -ing",
                "meaning":  "Bilish, xohlash, yoqtirish, kerak boʻlish — "
                            "harakat emas, <b>holat</b>. Shuning uchun "
                            "<i>know, want, like, need, have</i> "
                            "(egalik) davomli shaklga kirmaydi: "
                            "<i>I know</i>, hech qachon "
                            "<i>I am knowing</i> emas.",
                "examples": ["Do you know the time?", "Her brother wants new shoes."],
            },
        ],
        "body": '''<p>Afsona <strong>usually walks</strong> to school. She <strong>likes</strong> the long <span class="cn-word" data-pos="adj" data-tr="tor">narrow</span> street with the trees.</p>

<p><strong>Today she is running</strong>.</p>

<p>She <strong>is carrying</strong> two bags, and one of them is not hers. Her little brother <strong>is standing</strong> at the corner with a <span class="cn-word" data-pos="adj" data-tr="yirilgan, siniq">broken</span> shoe. <strong>Every morning he walks</strong> with her; <strong>this morning he is waiting</strong>.</p>

<p>"<strong>Do you know</strong> the time?" he asks. He <strong>knows</strong> the answer <span class="cn-word" data-pos="adv" data-tr="allaqachon">already</span>.</p>

<p>They arrive at five past eight. The lesson <strong>starts</strong> at eight. The teacher <strong>is writing</strong> the <span class="cn-word" data-tr="sana">date</span> on the blackboard.</p>

<p>"Afsona <strong>always comes</strong> early," she says. "Why <strong>are you coming</strong> late today?"</p>

<p>"Because today is not a <span class="cn-word" data-pos="adj" data-tr="odatdagi">usual</span> day," Afsona says.</p>

<p>In the evening her mother <strong>is</strong> <span class="cn-word" data-pos="verb" data-tr="tikmoqda">sewing</span> the shoe by the window with a long <span class="cn-word" data-tr="igna">needle</span>. Afsona <strong>is watching</strong> her.</p>

<p>"Every day <strong>looks</strong> the same," her mother says, "but no day <strong>is</strong> the same."</p>''',
        "questions": [
            {
                "text": "Why is Afsona late today?",
                "choices": [
                    "She is carrying her brother's bag because his shoe is broken",
                    "She usually gets up late",
                    "The lesson starts earlier today",
                ],
                "answer": 0,
                "explanation": "U ikki sumka koʻtarib yugurmoqda, ukasining "
                               "poyabzali yirilgan — shuning uchun bugun "
                               "odatdagi kun emas.",
            },
            {
                "text": "Which pair is correct?",
                "choices": [
                    "She is usually walking to school, but today she runs.",
                    "She usually walks to school, but today she is running.",
                    "She usually is walking to school, but today she runs.",
                ],
                "answer": 1,
                "explanation": "<i>usually</i> → oddiy zamon (<b>walks</b>), "
                               "<i>today</i> → davomli zamon "
                               "(<b>is running</b>). Signal soʻzlar zamonni "
                               "tanlaydi.",
            },
            {
                "text": "Which verb from the story never takes \"-ing\"?",
                "choices": ["carry", "know", "write"],
                "answer": 1,
                "explanation": "<b>know</b> — holat feʼli. “I am knowing” "
                               "deb aytilmaydi. <i>carry</i> va <i>write</i> "
                               "esa harakat, ular davomli shaklga kiradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-14 — have / have got
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Boy Who Has Everything",
        "summary": (
            "PE-14 matni. Sherbekning katta kulrang sumkasida hamma narsa "
            "bor — juma kuni esa sumka yoʻq. have va have got orasidagi "
            "farq shu matnda."
        ),
        "order":   14,
        "grammar": [
            {
                "pattern":  "have got = have (both mean “bor”)",
                "meaning":  "Maʼnosi bir xil — egalik. <b>have got</b> "
                            "gapirishda, ayniqsa Britaniya inglizchasida "
                            "koʻp uchraydi; <b>have</b> hamma joyda "
                            "toʻgʻri va yozma tilda odatiyroq.",
                "examples": ["He has got two pens.", "He has bread in a paper bag."],
            },
            {
                "pattern":  "Two question forms, two negatives",
                "meaning":  "<b>have got</b> savolda <i>have</i> ni oldinga "
                            "chiqaradi: <i>Have you got a pencil?</i> "
                            "<b>have</b> esa <i>do/does</i> talab qiladi: "
                            "<i>Do you have water?</i> Inkor ham shunday: "
                            "<i>hasn't got</i> / <i>doesn't have</i>.",
                "examples": ["Have you got a pencil?", "Do you have water?",
                             "He hasn't got his bag."],
            },
            {
                "pattern":  "he / she / it → has, has got",
                "meaning":  "Uchinchi shaxs birlikda <i>have</i> → "
                            "<b>has</b>: <i>He has a bag</i>, "
                            "<i>She has got a plaster</i>. "
                            "<i>He have</i> — xato.",
                "examples": ["Sherbek has got a big grey bag.",
                             "Jasur has got a plaster."],
            },
        ],
        "body": '''<p>Sherbek <strong>has got</strong> a big grey bag, and the class <strong>has</strong> a <span class="cn-word" data-tr="hazil">joke</span> about it: Sherbek <strong>has</strong> everything.</p>

<p>He <strong>has got</strong> two pens and a short <span class="cn-word" data-tr="chizgʻich">ruler</span>. He <strong>has got</strong> <span class="cn-word" data-tr="qaychi">scissors</span>, <span class="cn-word" data-tr="yelim">glue</span> and a <span class="cn-word" data-tr="plastir">plaster</span>. He <strong>has got</strong> bread in a paper bag, and he even <strong>has got</strong> a phone <span class="cn-word" data-tr="quvvatlagich">charger</span>.</p>

<p>"<strong>Have</strong> you <strong>got</strong> a pencil?" Dilnoza asks on Monday. He <strong>has</strong>.</p>

<p>"<strong>Do</strong> you <strong>have</strong> water?" the teacher asks on Tuesday. He <strong>does</strong>.</p>

<p>"<strong>Has</strong> he <strong>got</strong> a second bag at home?" Jasur asks. Nobody knows.</p>

<p>On Friday Sherbek <strong>hasn't got</strong> his bag. He <strong>has</strong> one pen in his <span class="cn-word" data-tr="kissa">pocket</span> and nothing else.</p>

<p>Twenty pupils open their bags. Afsona <strong>has got</strong> a pen for him. Dilnoza <strong>has</strong> bread. Jasur <strong>has got</strong> a plaster for his hand, and today he <strong>doesn't have</strong> a joke.</p>

<p>"Now I <strong>have</strong> everything too," Sherbek says.</p>''',
        "questions": [
            {
                "text": "What happens on Friday?",
                "choices": [
                    "Sherbek comes without his bag and the class shares things with him",
                    "Sherbek brings a second bag",
                    "The class stops making jokes about the bag",
                ],
                "answer": 0,
                "explanation": "“On Friday Sherbek hasn't got his bag.” "
                               "Yigirma oʻquvchi sumkasini ochadi — va shu "
                               "kuni Jasur hazil qilmaydi.",
            },
            {
                "text": "Which question is correct?",
                "choices": [
                    "Do you have got a pencil?",
                    "Have you got a pencil?",
                    "Have you a pencil got?",
                ],
                "answer": 1,
                "explanation": "<i>have got</i> savolida <b>have</b> oldinga "
                               "chiqadi. <i>do</i> faqat yolgʻiz <i>have</i> "
                               "bilan ishlatiladi: <i>Do you have a pencil?</i>",
            },
            {
                "text": "Which sentence is wrong English?",
                "choices": [
                    "He has got a charger.",
                    "He have got a charger.",
                    "He doesn't have a charger.",
                ],
                "answer": 1,
                "explanation": "<i>he / she / it</i> bilan <b>has</b> "
                               "ishlatiladi, <i>have</i> emas.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-15 — adjectives: meaning, position and order
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "A Small Old Blue Bicycle",
        "summary": (
            "PE-15 matni. Bekzod garajdagi eski velosipedni yoqtirmaydi — "
            "yakshanbaga borib fikri oʻzgaradi. Sifatlar tartibi jonli "
            "matnda."
        ),
        "order":   15,
        "grammar": [
            {
                "pattern":  "Before the noun, or after \"to be\"",
                "meaning":  "Sifat otdan <b>oldin</b> turadi — "
                            "<i>a blue bicycle</i> — yoki <i>be</i> "
                            "feʼlidan <b>keyin</b> kelib, egani "
                            "taʼriflaydi: <i>The bicycle is blue</i>. "
                            "Uchinchi joy yoʻq.",
                "examples": ["There is a small old blue bicycle in the garage.",
                             "It is old, and it is strong."],
            },
            {
                "pattern":  "Order: opinion – size – age – colour – origin – material",
                "meaning":  "Bir necha sifat birga kelsa, tartib qatʼiy: "
                            "fikr → hajm → yosh → rang → millat → "
                            "material. <i>a <b>beautiful little old "
                            "Russian</b> bicycle</i>. Tartibni "
                            "buzsangiz, gap notoʻgʻri “eshitiladi”.",
                "examples": ["a beautiful little Russian bicycle",
                             "a long metal pump", "new black mountain bikes"],
            },
            {
                "pattern":  "Adjectives never take -s",
                "meaning":  "Ot koʻplik boʻlsa ham, sifat oʻzgarmaydi: "
                            "<i>two <b>new</b> bikes</i>, hech qachon "
                            "<i>news bikes</i> emas. Va <i>a / an</i> "
                            "birinchi sifatning tovushiga qaraydi: "
                            "<b>an</b> old bicycle.",
                "examples": ["His friends have new black mountain bikes.",
                             "It is an old bicycle."],
            },
        ],
        "body": '''<p>In the corner of the garage there is <strong>a small old blue bicycle</strong>. Nobody rides it.</p>

<p>On Saturday Bekzod's father brings it into the yard. "It is <strong>a beautiful little Russian bicycle</strong>," he says.</p>

<p>Bekzod looks at the <span class="cn-word" data-tr="zang">rust</span> on the <span class="cn-word" data-tr="shinalar">tyres</span>. His friends have <strong>new black mountain bikes</strong>. This one is <strong>old</strong>, and it is <strong>small</strong>.</p>

<p>"Old is not the same as <span class="cn-word" data-pos="adj" data-tr="kuchsiz">weak</span>," his father says. He takes <strong>a long metal pump</strong> from the wall.</p>

<p>They work for two hours. The <span class="cn-word" data-tr="egar">saddle</span> is hard, the <span class="cn-word" data-tr="zanjir">chain</span> is <span class="cn-word" data-pos="adj" data-tr="kir">dirty</span>, but the <span class="cn-word" data-tr="rama">frame</span> is <span class="cn-word" data-pos="adj" data-tr="mustahkam">strong</span>.</p>

<p>On Sunday Bekzod <span class="cn-word" data-pos="verb" data-tr="minadi">rides</span> to the river and back. The bicycle does not stop, and it does not make a noise.</p>

<p>Now his friends ask a new question every evening: "Is your <strong>little blue bicycle</strong> free tomorrow?"</p>

<p>Bekzod's answer is always the same. "It is <strong>old</strong>, it is <strong>blue</strong>, and it is <strong>mine</strong>."</p>''',
        "questions": [
            {
                "text": "How does Bekzod feel about the bicycle on Saturday?",
                "choices": [
                    "He is happy about it at once",
                    "He is not happy: it is old and small",
                    "He gives it to his friends",
                ],
                "answer": 1,
                "explanation": "Shanba kuni u zang va shinalarga qaraydi, "
                               "doʻstlarining yangi velosipedlarini eslaydi. "
                               "Fikri yakshanbada oʻzgaradi.",
            },
            {
                "text": "Which order is correct English?",
                "choices": [
                    "a blue old small bicycle",
                    "a small old blue bicycle",
                    "an old blue small bicycle",
                ],
                "answer": 1,
                "explanation": "Hajm → yosh → rang: <b>small – old – blue</b>. "
                               "Shu tartib matnning sarlavhasida ham turgan.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "His friends have news black bikes.",
                    "His friends have new black bikes.",
                    "His friends have new blacks bikes.",
                ],
                "answer": 1,
                "explanation": "Sifatlar hech qachon <b>-s</b> olmaydi — ot "
                               "koʻplik boʻlsa ham: <i>new black bikes</i>.",
            },
        ],
    },
]
