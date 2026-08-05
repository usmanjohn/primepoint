# -*- coding: utf-8 -*-
"""Prime English Readings — PE-36 … PE-40 (batch 8). The rest of the PERFECT.

PE-36 present perfect continuous · PE-37 perfect simple vs continuous ·
PE-38 past perfect · PE-39 past perfect continuous · PE-40 future perfect (+ future
perfect continuous).

Shapes:
  36 — a true life story: the man who has been planting a forest since 1979 (India)
  37 — a kitchen mystery with a Goldilocks echo, where the two tenses ARE the detective
       logic: "Nobody has eaten the plov. But somebody has been eating it."
  38 — a life story that turns on a missed train in 1961
  39 — a life story: eleven months of saving, and a tin box nobody knew about
  40 — a teacher's time-capsule letters, posted ten years later

Cumulative rule: PE-37 must not reach for the past perfect (PE-38 is the next lesson),
so the plov mystery stays entirely in the present perfect pair. From PE-38 the past
perfect is free, and PE-39/40 use it. Still no modals other than will (PE-42+), no
comparatives (PE-67), no passive (PE-60), and only simple who/that clauses.
Length: 230–270 words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_36_40.py --author=prime
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
    # PE-36 — present perfect continuous  (true life story)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Man Who Has Been Planting Trees",
        "summary": (
            "PE-36 matni. 1979-yilda oʻn olti yoshli bola qumloq orolda "
            "oʻlgan ilonlarni koʻrdi — va oʻsha kundan beri har kuni "
            "daraxt ekadi. Bugun u yer oʻrmon."
        ),
        "order":   36,
        "grammar": [
            {
                "pattern":  "have / has been + verb-ing",
                "meaning":  "Oʻtmishda boshlangan va <b>hozir ham davom "
                            "etayotgan</b> ish. Odatda <i>for</i> yoki "
                            "<i>since</i> bilan: <i>He has been planting "
                            "trees since 1979</i> — ekkan va hali ham "
                            "ekmoqda.",
                "examples": ["He has been planting trees every day since that summer.",
                             "A herd of elephants has been coming every year."],
            },
            {
                "pattern":  "It looks at the ACTIVITY, not the result",
                "meaning":  "Perfect simple natijani sanaydi "
                            "(<i>he has planted a forest</i>), davomli "
                            "shakl esa <b>mehnatning oʻzini</b> "
                            "koʻrsatadi — va koʻpincha bugun "
                            "koʻrinadigan dalilni: uning qoʻllari, "
                            "belkuragi, orqasi.",
                "examples": ["He has been working with a spade and wet sand.",
                             "People have been asking me the same question for forty years."],
            },
            {
                "pattern":  "How long have you been …?",
                "meaning":  "“Qachondan beri?” degan savol shu shaklda "
                            "beriladi. Ammo holat feʼllari bilan "
                            "ishlatilmaydi: <i>I have known him for a "
                            "year</i> — <i>have been knowing</i> xato.",
                "examples": ["Have you been counting the trees?",
                             "How long have you been living here?"],
            },
        ],
        "body": '''<p>In 1979 a great river in India <span class="cn-word" data-pos="verb" data-tr="suv bosdi">flooded</span> an island called Majuli. When the water went down, a boy of sixteen walked out onto a <span class="cn-word" data-tr="qumloq orolcha">sandbar</span> and found hundreds of dead <span class="cn-word" data-tr="ilonlar">snakes</span> on the hot sand.</p>

<p>There were no trees on that sand. There was no shade. The snakes had come with the flood and the sun had finished them.</p>

<p>The boy walked to the forest office and asked the men there for trees. They gave him twenty <span class="cn-word" data-tr="bambuk">bamboo</span> plants and one sentence: "Plant them yourself."</p>

<p>His name is Jadav Payeng, and he <strong>has been planting</strong> trees on that sandbar every single day <strong>since</strong> that summer.</p>

<p>In the first years he carried water in two <span class="cn-word" data-tr="bidonlar">cans</span>, twice a day, in forty degrees. He put the <span class="cn-word" data-tr="koʻchatlar">seedlings</span> in the sand and walked back for more water. Nobody helped him. Nobody paid him.</p>

<p>"People <strong>have been asking</strong> me the same question <strong>for</strong> forty years," he says. "Why? And I say: the snakes died because nobody had planted anything."</p>

<p>That sandbar is now a forest of five hundred <span class="cn-word" data-tr="gektar">hectares</span>. It has a name — the Molai forest, from his own <span class="cn-word" data-tr="taxallus">nickname</span>.</p>

<p><span class="cn-word" data-tr="kiyiklar">Deer</span> live in it. <span class="cn-word" data-tr="kalxatlar">Vultures</span> came back after thirty years. A <span class="cn-word" data-tr="poda">herd</span> of wild elephants <strong>has been coming</strong> to the forest every year, and tigers walk in it at night.</p>

<p>He is in his sixties now. He plants in the morning and walks in the evening, and his hands tell the story: he <strong>has been working</strong> with a <span class="cn-word" data-tr="belkurak">spade</span> and wet sand for most of his life.</p>

<p>"<strong>Have</strong> you <strong>been counting</strong> the trees?" a <span class="cn-word" data-tr="jurnalist">journalist</span> asked him.</p>

<p>"No," he said. "I <strong>have been planting</strong> them. Counting is your job."</p>''',
        "questions": [
            {
                "text": "What made the boy start planting?",
                "choices": [
                    "The forest office paid him for it",
                    "He found hundreds of dead snakes on sand with no shade",
                    "His family owned the island",
                ],
                "answer": 1,
                "explanation": "“…the snakes died because nobody had planted "
                               "anything.” Suv qaytgach, quyosh soyasiz "
                               "qumda ilonlarni oʻldirgan edi.",
            },
            {
                "text": "Why is \"He has been planting trees since 1979\" better here than \"He planted trees in 1979\"?",
                "choices": [
                    "Because he is still planting them today",
                    "Because it happened a long time ago",
                    "Because we know exactly how many trees there are",
                ],
                "answer": 0,
                "explanation": "Davomli perfekt ishning <b>bugungacha</b> "
                               "davom etishini koʻrsatadi. Oddiy oʻtgan "
                               "zamon uni 1979-yilda tugatib qoʻyar edi.",
            },
            {
                "text": "What does his last answer tell you about him?",
                "choices": [
                    "He does not know how many trees he has planted, and it does not interest him",
                    "He is angry with journalists",
                    "He wants somebody to help him count",
                ],
                "answer": 0,
                "explanation": "“I have been planting them. Counting is your "
                               "job.” U natijani sanamaydi — u ishni "
                               "qiladi. Grammatika ham shuni aytadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-37 — perfect simple vs continuous  (kitchen mystery)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Somebody Has Been Eating My Plov",
        "summary": (
            "PE-37 matni. Yigirma mehmon uchun qilingan palov har kecha "
            "ozayadi. Buvim ikki zamon farqidan tergovchi mantiqini "
            "yasaydi — va oʻgʻrini emas, mehmonni topadi."
        ),
        "order":   37,
        "grammar": [
            {
                "pattern":  "Simple = the finished result",
                "meaning":  "<b>have/has + V3</b> tugagan ishni va bugungi "
                            "natijani beradi: <i>Somebody has eaten the "
                            "plov</i> — palov <b>yoʻq</b>. Savol “nima "
                            "boʻldi?” degan savolga javob beradi.",
                "examples": ["Nobody has eaten the plov — it is still here.",
                             "Now he has eaten at my table, so he is a guest."],
            },
            {
                "pattern":  "Continuous = the activity, maybe unfinished",
                "meaning":  "<b>have/has been + -ing</b> harakatning oʻziga "
                            "qaraydi: <i>Somebody has been eating it</i> — "
                            "har kecha bir oz, va palov hamon bor. "
                            "Buvimning butun tergovi shu farqqa tayanadi.",
                "examples": ["Somebody has been eating my plov. Every night a little.",
                             "I have been leaving the door open for eleven days."],
            },
            {
                "pattern":  "Numbers go with the SIMPLE form",
                "meaning":  "Necha marta, nechta — faqat oddiy perfekt "
                            "bilan: <i>I have made three pots</i>. "
                            "Davomli shakl sanamaydi, u faqat "
                            "davomiylikni koʻrsatadi. "
                            "<i>I have been making three pots</i> — xato.",
                "examples": ["I have slept. I have also been counting.",
                             "He takes one plate. Never two."],
            },
        ],
        "body": '''<p>On Thursday my grandmother made plov for twenty guests in a <span class="cn-word" data-tr="qozon">pot</span> the size of a bicycle <span class="cn-word" data-tr="gʻildirak">wheel</span>. She put the pot in the <span class="cn-word" data-tr="salqin ombor">cold room</span> and closed the door.</p>

<p>On Friday morning she stood in that doorway with her hands on her <span class="cn-word" data-tr="beli">hips</span>.</p>

<p>"Somebody <strong>has been eating</strong> my plov," she said.</p>

<p>My brother looked in the pot. "It's still full."</p>

<p>"Look at it properly," she said. "Nobody <strong>has eaten</strong> the plov — it is still here. But somebody <strong>has been eating</strong> it. Every night, a little. And that is a completely different person."</p>

<p>That was the <span class="cn-word" data-tr="ipuchi, dalil">clue</span>. A <span class="cn-word" data-tr="oʻgʻri">thief</span> takes everything once. A hungry person takes a little, often.</p>

<p>My brother said a cat. My grandmother pointed at the <span class="cn-word" data-tr="izlar">marks</span> on the top of the rice. "A cat doesn't use a spoon."</p>

<p>On Saturday night I <span class="cn-word" data-pos="verb" data-tr="yashirindim">hid</span> behind the door of the cold room with a blanket.</p>

<p>At eleven o'clock the door opened. A boy from the end of our street came in with a small <span class="cn-word" data-tr="likopcha">plate</span>. He is twelve. He <strong>has been living</strong> with his <span class="cn-word" data-tr="xola">aunt</span> since March, and his aunt works nights at the hospital.</p>

<p>He <span class="cn-word" data-pos="verb" data-tr="toʻldirdi">filled</span> the plate, closed the pot carefully and went out.</p>

<p>I ran to the kitchen. My grandmother was <span class="cn-word" data-pos="adj" data-tr="uygʻoq">awake</span> at the table with her tea.</p>

<p>"I know," she said. "I <strong>have been leaving</strong> that door open for eleven days."</p>

<p>"So you <strong>haven't been</strong> sleeping at all?"</p>

<p>"I <strong>have</strong> slept," she said. "I <strong>have</strong> also <strong>been counting</strong>. He takes one plate. Never two. That is a boy with a mother somewhere in his head."</p>

<p>On Sunday there were twenty-one places at our table. "I <strong>have made</strong> more rice," my grandmother said, and she said nothing else about it.</p>

<p>"I <strong>have been feeding</strong> a boy," she told me later. "Not a cat. And now he <strong>has eaten</strong> at my table, so he is a guest — and a guest comes back."</p>''',
        "questions": [
            {
                "text": "How did the grandmother know it was not a thief?",
                "choices": [
                    "The pot was still full: somebody had been taking a little every night",
                    "She saw the boy on Thursday",
                    "The door was closed every morning",
                ],
                "answer": 0,
                "explanation": "“A thief takes everything once. A hungry "
                               "person takes a little, often.” Ikki zamonning "
                               "farqi — tergovning kaliti.",
            },
            {
                "text": "Which pair of sentences is right for the story?",
                "choices": [
                    "Somebody has eaten the plov, so it is still here.",
                    "Nobody has eaten the plov, but somebody has been eating it.",
                    "Nobody has been eating the plov, but somebody has eaten it.",
                ],
                "answer": 1,
                "explanation": "Palov tugamagan → <i>nobody has eaten</i>; "
                               "lekin harakat davom etgan → <i>somebody has "
                               "been eating</i>.",
            },
            {
                "text": "Why does she lay twenty-one places on Sunday?",
                "choices": [
                    "Because one guest is coming from another city",
                    "Because she is inviting the boy to the table instead of the cold room",
                    "Because her family has grown by one person",
                ],
                "answer": 1,
                "explanation": "“Now he has eaten at my table, so he is a "
                               "guest — and a guest comes back.” U bolani "
                               "oʻgʻri qilib emas, mehmon qilib qoldiradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-38 — past perfect  (life story)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "By the Time the Train Came",
        "summary": (
            "PE-38 matni. 1961-yilda bir yigit poyezdga kechikdi — va "
            "shu sababdan qirq bir yil qishloqda dars berdi. Oʻtmishdan "
            "oldingi oʻtmish: had + V3."
        ),
        "order":   38,
        "grammar": [
            {
                "pattern":  "had + V3 = the past BEFORE the past",
                "meaning":  "Ikki oʻtmish voqeasidan <b>oldingisi</b> "
                            "<i>had</i> bilan aytiladi: <i>By the time he "
                            "reached the platform, the train <b>had "
                            "left</b></i> — poyezd oldin ketdi, u keyin "
                            "keldi.",
                "examples": ["By the time he reached the platform, the train had gone.",
                             "He had packed his bag the night before."],
            },
            {
                "pattern":  "Its favourite words: by the time · already · before · never",
                "meaning":  "<i>by the time</i>, <i>already</i>, "
                            "<i>before</i>, <i>after</i>, <i>when</i>, "
                            "va hayotdagi tajriba uchun <i>never</i>: "
                            "<i>He had never seen the sea</i> — oʻsha "
                            "kungacha koʻrmagan edi.",
                "examples": ["His mother had already told the whole street.",
                             "He had never seen the sea."],
            },
            {
                "pattern":  "Use it only when the ORDER matters",
                "meaning":  "Agar voqealar tartibi aniq boʻlsa, oddiy "
                            "oʻtgan zamon yetadi: <i>He came home and ate "
                            "dinner</i>. <i>had</i> faqat “bu undan oldin "
                            "boʻlgan” deb koʻrsatish kerak boʻlganda "
                            "ishlatiladi.",
                "examples": ["The director had lost two teachers that summer.",
                             "By the time he retired, he had taught two thousand children."],
            },
        ],
        "body": '''<p>My grandfather <span class="cn-word" data-pos="verb" data-tr="oʻtkazib yubordi">missed</span> one train in 1961, and that is the only reason I <span class="cn-word" data-tr="tugʻilganim">was born</span> in this village.</p>

<p>He was twenty-two. He <strong>had finished</strong> the <span class="cn-word" data-tr="bilim yurti">teachers' college</span> in June, and in August a letter came: a school in the city wanted him. A city school. His mother <strong>had already told</strong> the whole street.</p>

<p>The train left at six in the morning. He <strong>had</strong> <span class="cn-word" data-pos="verb" data-tr="yigʻib qoʻygan edi">packed</span> his bag the night before: two <span class="cn-word" data-tr="koʻylaklar">shirts</span>, a <span class="cn-word" data-tr="ustara">razor</span>, and forty-one books. Forty-one.</p>

<p>He left the house at four, because the station is nine kilometres away. But the little bridge over the canal <strong>had gone</strong> <span class="cn-word" data-tr="suv ostiga">under water</span> in the night, so he took the <span class="cn-word" data-tr="aylanma yoʻl">long way round</span>, through the fields, with the bag on his shoulder.</p>

<p>By the time he reached the <span class="cn-word" data-tr="perron">platform</span>, the train <strong>had left</strong>. Twenty minutes.</p>

<p>The next one was on Friday. He sat down on his bag and did not move for an hour.</p>

<p>An old man sat down next to him and asked why a young man with forty-one books was sitting on a platform with wet shoes.</p>

<p>That old man was the head of the school in the next village. He <strong>had lost</strong> two teachers that summer. He <strong>had been</strong> to the city twice and <strong>had found</strong> nobody.</p>

<p>"You have a bag and no train," he said. "I have a school and no teacher."</p>

<p>My grandfather taught in that village for forty-one years — one year for every book he <strong>had carried</strong> to the station that morning.</p>

<p>By the time he <span class="cn-word" data-pos="verb" data-tr="nafaqaga chiqdi">retired</span>, he <strong>had taught</strong> about two thousand children. Three of them <strong>had become</strong> teachers in the same school.</p>

<p>One of those three is my mother, and she has his forty-one books on a shelf that my father made.</p>''',
        "questions": [
            {
                "text": "Why did he miss the train?",
                "choices": [
                    "He got up too late",
                    "The bridge was under water, so he had to walk the long way round",
                    "He had lost his ticket",
                ],
                "answer": 1,
                "explanation": "“…the little bridge over the canal had gone "
                               "under water in the night, so he took the "
                               "long way round.” Yigirma daqiqa kechikdi.",
            },
            {
                "text": "Which sentence shows the correct order of events?",
                "choices": [
                    "By the time he reached the platform, the train had left.",
                    "By the time he had reached the platform, the train left.",
                    "By the time he reached the platform, the train has left.",
                ],
                "answer": 0,
                "explanation": "Oldin boʻlgan ish — poyezdning ketishi — "
                               "<b>had left</b>; keyingisi oddiy oʻtgan "
                               "zamonda.",
            },
            {
                "text": "What is the meaning of the last two paragraphs?",
                "choices": [
                    "One missed train produced two thousand pupils and three teachers",
                    "He always wanted to work in a village",
                    "The city school never found a teacher",
                ],
                "answer": 0,
                "explanation": "Hikoyaning burilishi shu: bir kechikish "
                               "butun bir umrni — va oʻsha qishloqdagi "
                               "ikki ming bolaning taʼlimini — yaratdi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-39 — past perfect continuous  (life story)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "She Had Been Saving for Eleven Months",
        "summary": (
            "PE-39 matni. Dilnoza velosiped uchun oʻn bir oy pul yigʻdi. "
            "Aprel oyida buvisining koʻzoynagi sindi. Iyunda darvoza "
            "oldida velosiped turgan edi."
        ),
        "order":   39,
        "grammar": [
            {
                "pattern":  "had been + verb-ing",
                "meaning":  "Oʻtmishdagi bir nuqtadan <b>oldin</b> uzoq "
                            "davom etgan ish: <i>She had been saving for "
                            "eleven months</i>. Odatda yonida "
                            "<i>for</i> + davomiylik turadi.",
                "examples": ["She had been saving for eleven months.",
                             "She had been walking to school instead of taking the bus."],
            },
            {
                "pattern":  "It explains WHY the past moment happened",
                "meaning":  "Bu zamon sababni koʻrsatadi: u oʻn bir oy "
                            "yiqqani uchun aprelda qoʻlida pul bor edi. "
                            "Hikoyada “nima uchun shunday boʻldi?” degan "
                            "savolga javob beradi.",
                "examples": ["Her grandmother had been reading with those glasses for nineteen years.",
                             "She had been holding the book at arm's length for two weeks."],
            },
            {
                "pattern":  "Simple = the result · Continuous = the long activity",
                "meaning":  "<i>She had saved 340,000</i> — natija, aniq "
                            "son. <i>She had been saving for eleven "
                            "months</i> — mehnat, davomiylik. "
                            "Sonlar oddiy shaklga, oylar davomli "
                            "shaklga boradi.",
                "examples": ["She had saved 340,000 som.",
                             "I had been saving for a day like this. For nine years."],
            },
        ],
        "body": '''<p>Dilnoza <strong>had been saving</strong> for eleven months, and everybody in that house knew it.</p>

<p>She <strong>had been walking</strong> to school instead of taking the bus. She <strong>had been collecting</strong> bottles from the street behind the shop. In July she <strong>had been selling</strong> apricots from their own tree at the gate, in a bucket, for two weeks.</p>

<p>The money sat in a <span class="cn-word" data-tr="banka">jar</span> behind the flour: three hundred and forty thousand som. A <span class="cn-word" data-pos="adj" data-tr="ishlatilgan">second-hand</span> bicycle in the bazaar cost three hundred and fifty.</p>

<p>In April her grandmother's <span class="cn-word" data-tr="koʻzoynak">glasses</span> fell on the floor and <span class="cn-word" data-pos="verb" data-tr="sindi">broke</span> in two places. She <strong>had been reading</strong> with them for nineteen years.</p>

<p>Her grandmother said nothing about it. She read the <span class="cn-word" data-tr="gazeta">newspaper</span> at the window, in the best light, holding it at <span class="cn-word" data-tr="qoʻl uzunligida">arm's length</span>. She <strong>had been holding</strong> it like that for two weeks when Dilnoza noticed.</p>

<p>New lenses cost three hundred and twenty thousand.</p>

<p>On Saturday Dilnoza took the jar to the <span class="cn-word" data-tr="optika doʻkoni">optician</span> on the main street and came home with a paper bag and twenty thousand som.</p>

<p>Her grandmother put the glasses on and read for four hours <span class="cn-word" data-tr="toʻxtamasdan">without stopping</span>. Nobody said one word about a bicycle.</p>

<p>Then, on the last day of school in June, Dilnoza came through the gate and there was a bicycle standing in the yard. Blue, old, and strong.</p>

<p>Her grandmother was sitting next to it with an empty <span class="cn-word" data-tr="tunuka quti">tin box</span> in her <span class="cn-word" data-tr="tizzasi ustida">lap</span>.</p>

<p>"You <strong>had been saving</strong> for a bicycle," she said. "And I <strong>had been saving</strong> for a day like this. For nine years. I never knew what it was for. Now I know."</p>

<p>That tin box lives on the kitchen shelf, and it is not empty any more. Dilnoza <strong>has been putting</strong> coins in it since June, and she doesn't know what it is for either.</p>''',
        "questions": [
            {
                "text": "What did Dilnoza do with her eleven months of savings?",
                "choices": [
                    "She bought the second-hand bicycle",
                    "She paid for her grandmother's new lenses",
                    "She put it in the tin box",
                ],
                "answer": 1,
                "explanation": "Yangi linzalar 320 000 turdi; u bankani "
                               "optikaga olib bordi va uyga 20 000 som "
                               "bilan qaytdi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "She had been saving 340,000 som.",
                    "She had saved 340,000 som, and she had been saving for eleven months.",
                    "She had saved for eleven months and had been saving 340,000 som.",
                ],
                "answer": 1,
                "explanation": "Son — oddiy shaklga (<i>had saved 340,000</i>), "
                               "davomiylik — davomli shaklga "
                               "(<i>had been saving for eleven months</i>).",
            },
            {
                "text": "Why did the grandmother have money for a bicycle?",
                "choices": [
                    "She had been saving in a tin box for nine years, without a plan",
                    "She sold her old glasses",
                    "She borrowed it from a neighbour",
                ],
                "answer": 0,
                "explanation": "“I had been saving for a day like this. For "
                               "nine years. I never knew what it was for.” "
                               "Ikki avlod bir vaqtda, bir-biridan "
                               "xabarsiz pul yiggan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-40 — future perfect (+ continuous)  (time capsule)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Letters They Will Have Forgotten",
        "summary": (
            "PE-40 matni. Har iyunda 12-xonaning bitiruvchilari oʻzlariga "
            "xat yozadi, va oʻqituvchi ularni oʻn yil saqlab, keyin "
            "joʻnatadi. Bu yil 2016-yilning xatlari ketdi."
        ),
        "order":   40,
        "grammar": [
            {
                "pattern":  "will have + V3",
                "meaning":  "Kelajakdagi bir nuqtadan <b>oldin</b> "
                            "tugaydigan ish: <i>By the time you read this, "
                            "you <b>will have finished</b> university</i>. "
                            "Oʻzbekchada — “tugatgan boʻlasan”.",
                "examples": ["By 2026 you will have forgotten the name of this street.",
                             "By next June I will have read my own handwriting to a class."],
            },
            {
                "pattern":  "will have been + verb-ing",
                "meaning":  "Oʻsha kelajak nuqtasiga qadar ish <b>qancha "
                            "vaqt</b> davom etgan boʻladi: <i>you will "
                            "have been working for three years</i>. "
                            "Davomiylikni oʻlchaydi, natijani emas.",
                "examples": ["In ten years you will have been living in another city for a long time.",
                             "I will have been teaching here for one year."],
            },
            {
                "pattern":  "by + time · by the time + PRESENT",
                "meaning":  "<b>by 2036</b>, <b>by the end of the "
                            "summer</b>, <b>by then</b> — bu zamonning "
                            "doimiy hamrohlari. Diqqat: "
                            "<i>by the time you <b>read</b> this</i> — "
                            "shu boʻlakda kelasi zamon ishlatilmaydi, "
                            "“<i>by the time you will read</i>” xato.",
                "examples": ["By the time you read this, you will have left this town."],
            },
        ],
        "body": '''<p>Every June, on the last day, the <span class="cn-word" data-tr="bitiruvchilar">leavers</span> of Room 12 write a letter. Not to their mothers. To themselves — to the person they <strong>will have become</strong> in ten years.</p>

<p>Their teacher puts the letters in a metal box with a broken <span class="cn-word" data-tr="qulf">lock</span>. She writes the year on the <span class="cn-word" data-tr="qopqoq">lid</span> in white <span class="cn-word" data-tr="boʻyoq">paint</span>. Then she keeps the box for ten years and <span class="cn-word" data-pos="verb" data-tr="joʻnatadi">posts</span> the letters.</p>

<p>She has been doing this since 1996.</p>

<p>"Write what you think you will be doing," she tells them every year. "Write the questions you want to ask yourself. And write the date, because you will not <span class="cn-word" data-pos="verb" data-tr="ishonmaysan">believe</span> it."</p>

<p>Last week she posted the letters of 2016: twenty-two <span class="cn-word" data-tr="konvertlar">envelopes</span> with new <span class="cn-word" data-tr="markalar">stamps</span> on old handwriting.</p>

<p>"By the time you read this you <strong>will have finished</strong> university and you <strong>will have been working</strong> for three years. Are you a doctor? If you are not, it is not <span class="cn-word" data-tr="juda kech">too late</span>." — Bekzod, aged 17.</p>

<p>"By 2026 you <strong>will have forgotten</strong> the name of this street. I hope you have not." — Nilufar, aged 16.</p>

<p>"In ten years you <strong>will have been living</strong> in another city for a long time. Please <span class="cn-word" data-pos="verb" data-tr="qoʻngʻiroq qil">telephone</span> Grandmother tonight. Tonight." — Sherbek, aged 17.</p>

<p>Nineteen letters arrived. Two came back to the school, because the addresses had gone.</p>

<p>And one letter she did not post at all. She gave it to the writer by hand — because the girl who wrote it in 2016 is standing in that same room this September, in front of thirty pupils, with a red pen and a <span class="cn-word" data-tr="qoʻl yozuvi">handwriting</span> that has not changed at all.</p>

<p>She teaches mathematics in Room 12 now.</p>

<p>"By next June," she says, "I <strong>will have read</strong> my own letter to a class of children, and I <strong>will have been teaching</strong> in this room for one year. And they <strong>will have written</strong> their own letters. That is the <span class="cn-word" data-tr="ishning butun mohiyati">whole job</span>, really."</p>

<p>The box is under her desk. It is not empty.</p>''',
        "questions": [
            {
                "text": "What happens to the letters after ten years?",
                "choices": [
                    "The teacher posts them to the people who wrote them",
                    "The pupils read them at school on the last day",
                    "The teacher keeps them in the box for ever",
                ],
                "answer": 0,
                "explanation": "“…she keeps the box for ten years and posts "
                               "the letters.” Oʻtgan hafta 2016-yilning "
                               "yigirma ikkita xati joʻnatildi.",
            },
            {
                "text": "Which line is correct English?",
                "choices": [
                    "By the time you will read this, you will have finished university.",
                    "By the time you read this, you will have finished university.",
                    "By the time you read this, you have finished university.",
                ],
                "answer": 1,
                "explanation": "<i>by the time</i> boʻlagida kelasi zamon "
                               "ishlatilmaydi — oddiy hozirgi zamon "
                               "keladi. Asosiy gapda esa "
                               "<b>will have + V3</b>.",
            },
            {
                "text": "Who is the teacher of Room 12 this September?",
                "choices": [
                    "The same teacher who started the box in 1996",
                    "A girl who wrote one of the 2016 letters",
                    "Bekzod, who became a doctor",
                ],
                "answer": 1,
                "explanation": "Bitta xat joʻnatilmadi: uni yozgan qiz "
                               "oʻsha xonada, qizil ruchka bilan turibdi — "
                               "endi u matematika oʻqituvchisi.",
            },
        ],
    },
]
