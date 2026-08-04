# -*- coding: utf-8 -*-
"""Prime English Readings — PE-31 … PE-35 (batch 7). Time, and the PERFECT.

PE-31 ago/for/since/until/by/during · PE-32 present perfect (form + "it matters
now") · PE-33 perfect with for and since · PE-34 already/yet/just/still/ever/never ·
PE-35 present perfect vs past simple.

Shapes (the user's rule — life stories, tales, hooks; grammar ON the turn):
  31 — a life story: a father's two years and eleven days abroad, counted in days
  32 — a NEWS BRIEF with quotes: a bottle thrown into the Aral Sea in 1987, found
  33 — two dogs, one famous and one nobody knows: Hachiko + a hospital gate
  34 — LIVE COMMENTARY of the hare and the tortoise (the fable in the perfect)
  35 — a small mystery: a grandfather's watch, and two tenses telling it differently

Cumulative rule: PE-31 stays out of the perfect (it is the lesson before it).
PE-32 uses the bare perfect only — no for/since (PE-33), no already/yet/just
(PE-34). PE-34 may use them all. No modals other than will (PE-42+), no
comparatives (PE-67), no passive (PE-60).
Length: 195–215 words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_31_35.py --author=prime
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
    # PE-31 — ago · for · since · until · by · during   (life story)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Two Years and Eleven Days",
        "summary": (
            "PE-31 matni. Sherbekning otasi Koreyaga ketdi va uyda vaqtni "
            "hamma boshqacha sanadi. ago, for, since, until, by, during — "
            "bitta oilaning taqvimi."
        ),
        "order":   31,
        "grammar": [
            {
                "pattern":  "ago = counting back from now",
                "meaning":  "Hozirdan orqaga sanaladi va hamisha oddiy "
                            "oʻtgan zamon bilan keladi: <i>He left three "
                            "years <b>ago</b></i>. Oʻzbekchadagi "
                            "“uch yil <b>oldin</b>”.",
                "examples": ["Eleven days ago he sent a photo of the snow.",
                             "He left for Korea three years ago."],
            },
            {
                "pattern":  "for = how long · since = from when",
                "meaning":  "<b>for</b> — davomiylik (<i>for six weeks</i>, "
                            "<i>for two years</i>). <b>since</b> — "
                            "boshlangan nuqta (<i>since August</i>, "
                            "<i>since March 2022</i>). Ikkisini "
                            "almashtirish — eng koʻp uchraydigan xato.",
                "examples": ["The money stopped for six weeks.",
                             "Since August. I chose the colour."],
            },
            {
                "pattern":  "until · by · during",
                "meaning":  "<b>until</b> — shu paytga qadar davom etadi "
                            "(<i>until midnight</i>). <b>by</b> — shu "
                            "paytdan kechikmasdan (<i>by Navruz</i>). "
                            "<b>during</b> — biror davrning "
                            "<b>ichida</b> (<i>during those calls</i>).",
                "examples": ["They drank tea until midnight.",
                             "By the next Navruz, his grandmother said.",
                             "During those calls nobody cried."],
            },
        ],
        "body": '''<p>Sherbek's father left for Korea in March. Sherbek was nine years old. The plan was simple: two years <span class="cn-word" data-pos="adv" data-tr="chet elda">abroad</span>, a new roof, and a small car.</p>

<p>He stayed for two years and eleven days.</p>

<p>Nobody in that house counted the months. They counted <span class="cn-word" data-pos="adv" data-tr="boshqacha">differently</span>.</p>

<p>"How long?" the neighbours asked. "<strong>Until</strong> the roof is finished," his mother said. "<strong>By</strong> the next Navruz," his grandmother said. "Eleven days <strong>ago</strong> he sent a photo of the <span class="cn-word" data-tr="qor">snow</span>," Sherbek said.</p>

<p>His father called every Sunday at eight. <strong>During</strong> those calls nobody cried. They cried after.</p>

<p>Sherbek learned the name of a city: Ansan. He learned that a factory works at night too, and that a twelve-hour <span class="cn-word" data-tr="smena">shift</span> is called a shift in English, and that a <span class="cn-word" data-tr="maosh">wage</span> is not the same as money you keep.</p>

<p>In the second winter the money stopped <strong>for</strong> six weeks. A <span class="cn-word" data-tr="dastgoh, mashina">machine</span> broke his father's hand. He didn't tell them <strong>until</strong> the <span class="cn-word" data-tr="bogʻlam">bandage</span> came off, because a <span class="cn-word" data-pos="adj" data-tr="xavotirda">worried</span> family sends nothing but questions.</p>

<p>He came home on the fourteenth of March. He stood at the gate with two bags and looked up at the new green <span class="cn-word" data-tr="tom">roof</span>.</p>

<p>"<strong>Since</strong> when is it green?"</p>

<p>"<strong>Since</strong> August," Sherbek said. "I <span class="cn-word" data-pos="verb" data-tr="tanladim">chose</span> the colour."</p>

<p>They sat under that roof and drank tea <strong>until</strong> midnight. Nobody talked about Korea.</p>

<p>In this street people don't <span class="cn-word" data-pos="verb" data-tr="oʻlchamaydi">measure</span> a father's work in dollars. They measure it in days: two years and eleven days.</p>''',
        "questions": [
            {
                "text": "Why didn't the father tell his family about his hand?",
                "choices": [
                    "Because a worried family only sends questions",
                    "Because he forgot about it",
                    "Because the money stopped for six weeks",
                ],
                "answer": 0,
                "explanation": "“He didn't tell them until the bandage came "
                               "off, because a worried family sends nothing "
                               "but questions.”",
            },
            {
                "text": "Which line is correct?",
                "choices": [
                    "The money stopped since six weeks.",
                    "The money stopped for six weeks.",
                    "The money stopped ago six weeks.",
                ],
                "answer": 1,
                "explanation": "Olti hafta — <b>davomiylik</b>, shuning "
                               "uchun <i>for</i>. <i>since</i> boshlangan "
                               "nuqtani talab qiladi (<i>since March</i>).",
            },
            {
                "text": "What does the last paragraph mean?",
                "choices": [
                    "The family earned very little money",
                    "For the people in that street, the cost of the work is the time away",
                    "Nobody in the street knows how much he earned",
                ],
                "answer": 1,
                "explanation": "Ular otaning mehnatini dollarda emas, "
                               "kunlarda oʻlchaydi — chunki eng qimmat "
                               "narsa uyda boʻlmagan ikki yil edi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-32 — present perfect: form and "it matters now"  (news brief)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Somebody Has Found It",
        "summary": (
            "PE-32 matni. 1987-yilda oʻn uch yoshli bola Orol dengiziga "
            "shishada xat tashladi. Dengiz ketdi — shisha esa qoldi. "
            "Present perfect: oʻtmish, natijasi bugun."
        ),
        "order":   32,
        "grammar": [
            {
                "pattern":  "have / has + third form (V3)",
                "meaning":  "Oʻtmishda boʻlgan ish, lekin gap "
                            "<b>bugungi natija</b> haqida: <i>A letter "
                            "<b>has arrived</b></i> — xat keldi va "
                            "<b>hozir</b> stol ustida turibdi. Qachon "
                            "boʻlgani aytilmaydi; muhimi — natija.",
                "examples": ["A letter has arrived at a house in Muynak.",
                             "It has changed two lives."],
            },
            {
                "pattern":  "The third form is the one to learn",
                "meaning":  "Toʻgʻri feʼllarda u <i>-ed</i> "
                            "(<i>washed</i>, <i>answered</i>), notoʻgʻri "
                            "feʼllarda esa uchinchi shakl: "
                            "write → <b>written</b>, find → <b>found</b>, "
                            "go → <b>gone</b>, keep → <b>kept</b>, "
                            "read → <b>read</b>.",
                "examples": ["Mira has written to that address.",
                             "The sea has gone. The bottle hasn't."],
            },
            {
                "pattern":  "hasn't + V3 · Have you …?",
                "meaning":  "Inkor va savol yordamchi feʼl bilan "
                            "yasaladi: <i>They have not met</i>, "
                            "<i>Have you read it?</i> Qisqartmalar "
                            "gapirishda odatiy: <i>I've</i>, "
                            "<i>he's</i>, <i>hasn't</i>, <i>haven't</i>.",
                "examples": ["They have not met.", "Have you read his letter?"],
            },
        ],
        "body": '''<p><strong>Muynak, last month.</strong> A letter <strong>has arrived</strong> at a house in this town, and it <strong>has changed</strong> two lives.</p>

<p>In 1987 a thirteen-year-old boy here wrote four lines on a page of a school exercise book, put the page in a bottle and <span class="cn-word" data-pos="verb" data-tr="uloqtirdi">threw</span> it into the Aral Sea. His name was Timur.</p>

<p>Then the sea went away. The <span class="cn-word" data-tr="qayiqlar">boats</span> stayed on the <span class="cn-word" data-tr="qum">sand</span>. Timur <span class="cn-word" data-pos="verb" data-tr="ulgʻaydi">grew up</span>, became a driver and forgot the bottle.</p>

<p>Two hundred kilometres from that <span class="cn-word" data-tr="qirgʻoq">shore</span>, in the <span class="cn-word" data-tr="tuz">salt</span> and <span class="cn-word" data-tr="chang">dust</span> of the old <span class="cn-word" data-tr="dengiz tubi">sea bed</span>, a twelve-year-old girl found a <span class="cn-word" data-pos="adj" data-tr="zangli">rusty</span> bottle under a dead tree. Her name is Mira.</p>

<p>"I <strong>have washed</strong> it three times," she says. "The paper is brown, but the words are there. I <strong>have read</strong> it about fifty times."</p>

<p>The letter says: <i>My name is Timur. I am thirteen. Our sea is going away and the <span class="cn-word" data-tr="kattalar">grown-ups</span> are quiet about it. If you find this, please write to me.</i> Under the four lines there is an <span class="cn-word" data-tr="manzil">address</span>.</p>

<p>Mira <strong>has written</strong> to that address. The house is still there.</p>

<p>Timur is fifty-one now, and he <strong>has answered</strong> her.</p>

<p>"A boy threw a bottle into a sea," he says. "The sea <strong>has gone</strong>. The bottle <strong>hasn't</strong>."</p>

<p>They <strong>have not met</strong>. Mira <strong>has put</strong> the bottle on her windowsill. Timur <strong>has kept</strong> her letter in the frame with his mother's photograph.</p>

<p>Two letters, thirty-four years, one bottle. The sea <strong>has left</strong> — but somebody <strong>has answered</strong>.</p>''',
        "questions": [
            {
                "text": "What happened to the sea in this story?",
                "choices": [
                    "It went away and left the boats on the sand",
                    "It carried the bottle two hundred kilometres",
                    "It came back after thirty-four years",
                ],
                "answer": 0,
                "explanation": "Orol dengizi chekindi: “The boats stayed on "
                               "the sand.” Shisha esa quruq dengiz tubida "
                               "topildi.",
            },
            {
                "text": "Why does the report say \"A letter has arrived\" and not \"A letter arrived\"?",
                "choices": [
                    "Because it is news: the result matters right now",
                    "Because we know exactly when it arrived",
                    "Because it arrived a long time ago",
                ],
                "answer": 0,
                "explanation": "Present perfect natijani bugunga bogʻlaydi. "
                               "Vaqt aytilsa (<i>in 1987</i>), oddiy oʻtgan "
                               "zamon kerak boʻladi — matnda aynan shunday.",
            },
            {
                "text": "Which third form (V3) is correct?",
                "choices": [
                    "She has writed to that address.",
                    "She has written to that address.",
                    "She has wrote to that address.",
                ],
                "answer": 1,
                "explanation": "write – wrote – <b>written</b>. Perfektda "
                               "hamisha uchinchi shakl ishlatiladi, "
                               "ikkinchisi emas.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-33 — present perfect with for and since  (two dogs)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Dog Who Waited at the Station",
        "summary": (
            "PE-33 matni. Tokioda toʻqson yildan beri odamlar bir it "
            "haykali yonida uchrashadi. Toshkentda esa hech kim ismini "
            "bilmaydigan it fevraldan beri kutadi."
        ),
        "order":   33,
        "grammar": [
            {
                "pattern":  "for + a length of time",
                "meaning":  "Qancha vaqt davom etganini bildiradi: "
                            "<i>for nine years</i>, <i>for seventy "
                            "years</i>, <i>for two hours</i>. "
                            "Oʻzbekchada — “toʻqqiz yil <b>davomida</b>”.",
                "examples": ["He came to that exit every day for nine years.",
                             "People have met at that spot for seventy years."],
            },
            {
                "pattern":  "since + the starting point",
                "meaning":  "Ish qachondan boshlangani: <i>since 1948</i>, "
                            "<i>since February</i>, <i>since I was a "
                            "child</i>. Oʻzbekchada — “1948-yildan "
                            "<b>beri</b>”.",
                "examples": ["The statue has stood there since 1948.",
                             "He has slept at that gate since February."],
            },
            {
                "pattern":  "Started in the past, TRUE NOW",
                "meaning":  "<b>have/has + V3 + for/since</b> — ish "
                            "oʻtmishda boshlangan va hozir ham davom "
                            "etadi. Shuning uchun oʻzbek oʻquvchisining "
                            "klassik xatosi shu yerda: "
                            "“<i>I am living here for ten years</i>” "
                            "emas, <b>I have lived here for ten years</b>.",
                "examples": ["How long have you lived in this city?",
                             "The dog has waited for eight months."],
            },
        ],
        "body": '''<p>In Tokyo there is a <span class="cn-word" data-tr="temir yoʻl vokzali">railway station</span> with five million people a day, and a small bronze <span class="cn-word" data-tr="haykal">statue</span> of a dog beside one <span class="cn-word" data-tr="chiqish">exit</span>.</p>

<p>The dog's name was Hachiko. Every evening he walked to that exit and waited for his <span class="cn-word" data-tr="egasi">owner</span>, a teacher who came home on the train at the same hour.</p>

<p>One day in 1925 the teacher died at work. He never came to the station again.</p>

<p>Hachiko came to that exit every evening <strong>for</strong> nine years and nine months. Workers <span class="cn-word" data-pos="verb" data-tr="ovqatlantirdi">fed</span> him. <span class="cn-word" data-tr="Yoʻlovchilar">Passengers</span> stepped around him. He watched the doors.</p>

<p>His statue <strong>has stood</strong> at that exit <strong>since</strong> 1948, and people <strong>have used</strong> it as a <span class="cn-word" data-tr="uchrashuv joyi">meeting point</span> <strong>for</strong> seventy years. "Meet me at Hachiko," they say. Millions of friendships <strong>have started</strong> at the feet of a <span class="cn-word" data-pos="adj" data-tr="vafodor">faithful</span> dog.</p>

<p>Now walk to a hospital gate in Tashkent.</p>

<p>There is a brown <span class="cn-word" data-pos="adj" data-tr="egasiz, koʻcha">stray</span> dog there with one white ear. He <strong>has slept</strong> under that gate <strong>since</strong> February. The guards <strong>have given</strong> him a name: Malchik.</p>

<p>"An old man came here in an ambulance in February," a <span class="cn-word" data-tr="hamshira">nurse</span> says. "The dog ran behind the car. He <strong>has waited</strong> at this gate <strong>for</strong> eight months."</p>

<p>The <span class="cn-word" data-tr="veterinar">vet</span> from the next street <strong>has looked</strong> after him free of charge. Two families <strong>have offered</strong> to take him home. He <strong>has refused</strong> to go: he stands, <span class="cn-word" data-pos="verb" data-tr="likillatadi">wags</span> his <span class="cn-word" data-tr="dum">tail</span>, and stays.</p>

<p>Ninety years and four thousand kilometres between two dogs, and the same sentence works for both: <i>He has waited since the day his person did not come back.</i></p>''',
        "questions": [
            {
                "text": "How long did Hachiko come to the station?",
                "choices": [
                    "For seventy years",
                    "For nine years and nine months",
                    "Since 1948",
                ],
                "answer": 1,
                "explanation": "“Hachiko came to that exit every evening for "
                               "nine years and nine months.” 1948 — haykal "
                               "qoʻyilgan yil.",
            },
            {
                "text": "Which line is correct?",
                "choices": [
                    "He has slept there since eight months.",
                    "He has slept there for eight months.",
                    "He is sleeping there for eight months.",
                ],
                "answer": 1,
                "explanation": "Sakkiz oy — davomiylik → <b>for</b>. "
                               "<i>since</i> nuqta talab qiladi "
                               "(<i>since February</i>), va davomli "
                               "zamon bu maʼnoda ishlatilmaydi.",
            },
            {
                "text": "Why does the writer put the two dogs in one text?",
                "choices": [
                    "To show that one sentence describes both, ninety years apart",
                    "To show that Tokyo is bigger than Tashkent",
                    "To ask the reader to take Malchik home",
                ],
                "answer": 0,
                "explanation": "Oxirgi gap ikkisiga ham toʻgʻri keladi — va "
                               "aynan shu grammatika buni "
                               "mumkin qiladi: boshlangan oʻtmishda, "
                               "davom etadi bugun.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-34 — already / yet / just / still / ever / never  (commentary)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Has the Tortoise Finished Yet?",
        "summary": (
            "PE-34 matni. Quyon va toshbaqa poygasi — jonli sharh "
            "shaklida. already, yet, just, still, ever, never: hammasi "
            "sharhlovchining tilida."
        ),
        "order":   34,
        "grammar": [
            {
                "pattern":  "already (+) · yet (− and ?)",
                "meaning":  "<b>already</b> — kutilganidan tez, tasdiq "
                            "gapda, feʼl oldida. <b>yet</b> — hozirgacha "
                            "boʻlmagan; inkor va savolda, gap "
                            "<b>oxirida</b>: <i>He hasn't passed the "
                            "first tree <b>yet</b></i>.",
                "examples": ["The hare has already reached the top of the hill.",
                             "Has the tortoise finished yet?"],
            },
            {
                "pattern":  "just = a moment ago · still = it goes on",
                "meaning":  "<b>just</b> — hozirgina boʻldi "
                            "(<i>has just woken up</i>). <b>still</b> — "
                            "holat davom etadi; <i>still hasn't</i> "
                            "shakli hayrat qoʻshadi: hali ham emas!",
                "examples": ["The hare has just woken up!",
                             "The tortoise still hasn't looked back."],
            },
            {
                "pattern":  "ever / never = life experience",
                "meaning":  "Savolda <b>ever</b>: “umringizda biror "
                            "marta?” — <i>Have you ever seen…?</i> "
                            "Javobda <b>never</b>, va u oʻzi inkor: "
                            "<i>I have never lost</i> — "
                            "<i>haven't never</i> xato.",
                "examples": ["Have you ever seen a race like this?",
                             "The hare has never lost a race."],
            },
        ],
        "body": '''<p>Good afternoon from the forest road, and what an afternoon! The <span class="cn-word" data-tr="poyga">race</span> <strong>has just started</strong>, and the <span class="cn-word" data-tr="quyon">hare</span> is gone. Gone!</p>

<p>He <strong>has already reached</strong> the top of the hill. <strong>Have</strong> you <strong>ever seen</strong> anything like it? Behind him, the <span class="cn-word" data-tr="toshbaqa">tortoise</span> <strong>hasn't</strong> passed the first tree <strong>yet</strong>.</p>

<p>Ten minutes later. The hare <strong>has stopped</strong>. Yes — he <strong>has found</strong> a <span class="cn-word" data-pos="adj" data-tr="yumshoq">soft</span> place in the <span class="cn-word" data-tr="soya">shade</span> and he is lying down. He <strong>has never lost</strong> a race in his life, and today he <strong>has decided</strong> to sleep.</p>

<p>Half an hour later. The tortoise is <strong>still</strong> walking. He <strong>still hasn't</strong> looked back once. I <strong>have</strong> <span class="cn-word" data-pos="adv" data-tr="rostini aytsam">honestly</span> <strong>never</strong> watched anything so slow, and I <strong>have</strong> <span class="cn-word" data-pos="verb" data-tr="sharh berdim">commentated</span> on the <span class="cn-word" data-tr="shilliqqurt">snail</span> championship.</p>

<p>An hour later. Nothing <strong>has changed</strong>. The hare is asleep. The tortoise is walking.</p>

<p>Wait. Something <strong>has happened</strong>! The hare <strong>has just woken up</strong>! He <strong>has seen</strong> the sun — it is low — and he is running, he is flying, the <span class="cn-word" data-tr="chang">dust</span> is behind him like <span class="cn-word" data-tr="tutun">smoke</span> —</p>

<p>— but the tortoise <strong>has already crossed</strong> the <span class="cn-word" data-tr="marra chizigʻi">finish line</span>.</p>

<p>The forest is quiet. The hare <strong>hasn't</strong> said a word <strong>yet</strong>.</p>

<p>Friends, in forty years at this microphone I <strong>have never seen</strong> a fast runner lose to a slow one. But I <strong>have</strong> often <strong>seen</strong> a runner who stopped lose to a runner who didn't.</p>''',
        "questions": [
            {
                "text": "Why does the hare lose?",
                "choices": [
                    "The tortoise runs faster at the end",
                    "He stops to sleep in the shade",
                    "He takes the wrong road",
                ],
                "answer": 1,
                "explanation": "“He has found a soft place in the shade… "
                               "today he has decided to sleep.” Toshbaqa "
                               "esa bir marta ham orqasiga qaramaydi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "The tortoise hasn't finished already.",
                    "The tortoise hasn't finished yet.",
                    "The tortoise hasn't yet finish.",
                ],
                "answer": 1,
                "explanation": "Inkorda <b>yet</b> ishlatiladi va gap "
                               "oxirida turadi. <i>already</i> — tasdiq "
                               "gapda, feʼl oldida.",
            },
            {
                "text": "What is the commentator's last idea?",
                "choices": [
                    "Slow runners are better than fast ones",
                    "Stopping is what loses a race, not being slow",
                    "Nobody has ever won this race",
                ],
                "answer": 1,
                "explanation": "“I have never seen a fast runner lose to a "
                               "slow one. But I have often seen a runner "
                               "who stopped lose to a runner who didn't.”",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-35 — present perfect vs past simple  (small mystery)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Watch in the Second Drawer",
        "summary": (
            "PE-35 matni. “Bobomning soatini yoʻqotdim” — va ikki zamon "
            "orasidagi farq butun tergovni boshqaradi: natija bugun, "
            "tafsilotlar oʻtmishda."
        ),
        "order":   35,
        "grammar": [
            {
                "pattern":  "Perfect = the result · Past simple = the when",
                "meaning":  "<b>I have lost the watch</b> — hozir yoʻq, "
                            "muhimi shu. <b>I lost it on Tuesday</b> — "
                            "vaqt aytildi, demak oddiy oʻtgan zamon. "
                            "Bitta hikoyada ikkisi navbatma-navbat "
                            "ishlaydi.",
                "examples": ["I have lost Grandfather's watch.",
                             "I took it off at the river on Tuesday."],
            },
            {
                "pattern":  "The test question: does it say WHEN?",
                "meaning":  "Gapda <i>yesterday, on Tuesday, in 2019, "
                            "an hour ago, when I was small</i> kabi "
                            "tugagan vaqt bor boʻlsa — <b>oddiy oʻtgan "
                            "zamon</b>. Vaqt yoʻq va natija muhim "
                            "boʻlsa — <b>perfect</b>. Bu bitta savol "
                            "koʻp xatoni toʻgʻrilaydi.",
                "examples": ["Have you seen it? — Yes, I saw it on Tuesday."],
            },
            {
                "pattern":  "News in the perfect, details in the past",
                "meaning":  "Xabar perfektda beriladi, keyin tafsilotlar "
                            "oddiy oʻtgan zamonga oʻtadi: <i>They have "
                            "found the watch! Dilnoza put it in the "
                            "drawer on Tuesday.</i> Gazeta ham, oila "
                            "ham aynan shunday gapiradi.",
                "examples": ["We have found it! It sat in that drawer for four days."],
            },
        ],
        "body": '''<p>On Saturday evening Bekzod stood in the kitchen door and said six words: "I <strong>have lost</strong> Grandfather's watch."</p>

<p>The kitchen went quiet. That watch is <span class="cn-word" data-tr="kumush">silver</span>, older than the house, and there is a name <span class="cn-word" data-pos="adj" data-tr="oʻyib yozilgan">engraved</span> inside the back: his grandfather's father.</p>

<p>His mother asked the only useful question. "When <strong>did</strong> you <strong>lose</strong> it?"</p>

<p>"I <strong>took</strong> it off at the <span class="cn-word" data-tr="daryo boʻyi">riverbank</span> on Tuesday," Bekzod said. "The <span class="cn-word" data-tr="tasma">strap</span> is <span class="cn-word" data-pos="adj" data-tr="boʻsh">loose</span>. I <strong>put</strong> it in my shoe and then we <strong>played</strong> football."</p>

<p>So on Sunday four people <strong>searched</strong> the riverbank. They <strong>found</strong> a <span class="cn-word" data-tr="qoshiq">spoon</span>, a bicycle <span class="cn-word" data-tr="qoʻngʻiroq">bell</span> and half a <span class="cn-word" data-tr="varrak">kite</span>. No watch.</p>

<p>Bekzod <strong>didn't sleep</strong> that night. He was <span class="cn-word" data-pos="adj" data-tr="uyalgan">ashamed</span> in a way that has no words: his grandfather <strong>gave</strong> him that watch in May and <strong>showed</strong> him how to <span class="cn-word" data-pos="verb" data-tr="qurish, dam berish">wind</span> it, slowly, every morning.</p>

<p>On Monday his little sister came home from her music lesson and heard the story from the door.</p>

<p>"Oh," she said. "I <strong>have put</strong> it in the second <span class="cn-word" data-tr="tortmacha">drawer</span>. For <span class="cn-word" data-tr="ehtiyot uchun">safety</span>."</p>

<p>She <strong>found</strong> it in his shoe on Tuesday evening, and she <strong>carried</strong> it to the drawer with two hands.</p>

<p>It <strong>has stopped</strong>, of course. Nobody <strong>wound</strong> it for six days.</p>

<p>Bekzod <strong>has worn</strong> it every day since that Monday, and he <strong>hasn't</strong> taken it off once — not at the river, not for football, not in his shoe.</p>''',
        "questions": [
            {
                "text": "Where was the watch all week?",
                "choices": [
                    "At the riverbank",
                    "In the second drawer, where his sister put it",
                    "In his football shoe",
                ],
                "answer": 1,
                "explanation": "Singlisi uni seshanba kuni poyabzalidan "
                               "topib, “ehtiyot uchun” tortmachaga "
                               "qoʻygan edi.",
            },
            {
                "text": "Why does Bekzod say \"I have lost the watch\" but \"I took it off on Tuesday\"?",
                "choices": [
                    "Because the first is the result now, and the second says when",
                    "Because the first is about a thing and the second about a person",
                    "Because he is not sure about Tuesday",
                ],
                "answer": 0,
                "explanation": "Natija bugun → perfect. Tugagan vaqt "
                               "(<i>on Tuesday</i>) aytilsa → oddiy "
                               "oʻtgan zamon. Test savoli: gapda "
                               "“qachon” bormi?",
            },
            {
                "text": "Which pair is correct English?",
                "choices": [
                    "Have you seen it? — Yes, I have seen it on Tuesday.",
                    "Did you see it? — Yes, I have seen it on Tuesday.",
                    "Have you seen it? — Yes, I saw it on Tuesday.",
                ],
                "answer": 2,
                "explanation": "Savol natija haqida (perfect), javobda esa "
                               "vaqt paydo boʻldi — <i>on Tuesday</i> — "
                               "shuning uchun oddiy oʻtgan zamon.",
            },
        ],
    },
]
