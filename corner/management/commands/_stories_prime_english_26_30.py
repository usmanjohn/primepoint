# -*- coding: utf-8 -*-
"""Prime English Readings — PE-26 … PE-30 (batch 6). The FUTURE block.

PE-26 will · PE-27 be going to · PE-28 present continuous for future ·
PE-29 the three futures compared · PE-30 future continuous.

FIRST BATCH UNDER THE USER'S RULE (2026-08-04): life stories, folk tales, anything
with a hook — and the grammar must sit ON the turn of the story, so the pupil cannot
remember the story without the pattern. Five different shapes here:
  26 — a Nasreddin Afandi folk tale (the whole tale IS one `will` promise)
  27 — a life story: a shepherd reads the evidence and warns a village
  28 — a diary: the last week before a family moves (arrangements, day by day)
  29 — three phone messages about one Saturday, each choosing a different future
  30 — a life story with a one-year arc, told by the sentence her father said

Cumulative rule: everything up to PE-25 is free (both pasts, used to/would, present
simple and continuous). Each story uses ONLY the futures taught by its own lesson —
so PE-26 has no "going to" anywhere, and PE-27 no future arrangements. No perfect
tenses (PE-32+), no modals other than will (PE-42+), no comparatives (PE-67).
Length: 175–210 words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_26_30.py --author=prime
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
    # PE-26 — will: promises, decisions, predictions  (folk tale)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Afandi and the Emir's Donkey",
        "summary": (
            "PE-26 matni. Amir eshagini oʻqishga oʻrgatishni buyuradi va "
            "hech kim jurʼat qilmaydi — Afandi esa oʻn yil soʻraydi. "
            "Butun hikoya bitta “will” vaʼdasi ustida turadi."
        ),
        "order":   26,
        "grammar": [
            {
                "pattern":  "will = a promise you make now",
                "meaning":  "Gapirayotgan paytda beriladigan vaʼda yoki "
                            "qaror <b>will</b> bilan aytiladi. Afandining "
                            "butun hikoyasi shu bitta qolipga tayanadi: "
                            "<i>I will teach him</i> — “oʻrgataman”.",
                "examples": ["I will teach him, my lord.",
                             "I will give you a reading donkey."],
            },
            {
                "pattern":  "will / won't = a prediction about the future",
                "meaning":  "Kelajak haqidagi taxmin ham <b>will</b> bilan: "
                            "<i>They will kill you</i>, <i>A donkey won't "
                            "read</i>. Inkori — <b>won't</b> "
                            "(<i>will not</i>).",
                "examples": ["In ten years they will kill you.",
                             "A donkey won't read a book."],
            },
            {
                "pattern":  "I'll · Will you …?",
                "meaning":  "Gapirishda deyarli hamisha qisqartiriladi: "
                            "<i>I'll</i>, <i>he'll</i>, <i>we'll</i>. "
                            "Savolda <b>will</b> oldinga chiqadi: "
                            "<i>Will you listen to me?</i> Feʼl hamisha "
                            "asosiy shaklda qoladi — <i>will to teach</i> "
                            "xato.",
                "examples": ["Will you listen to me for one minute?",
                             "I'll be back in ten years."],
            },
        ],
        "body": '''<p>One morning the <span class="cn-word" data-tr="amir, hukmdor">emir</span> of Bukhara stood in front of his <span class="cn-word" data-tr="olimlar">scholars</span> with a small grey donkey.</p>

<p>"This animal <strong>will learn</strong> to read," he said. "Who <strong>will teach</strong> it?"</p>

<p>The scholars looked at the ground. Nobody <span class="cn-word" data-pos="verb" data-tr="jurʼat qildi">dared</span> to speak. A man who said no to the emir <span class="cn-word" data-tr="boshidan judo boʻldi">lost his head</span>. A man who said yes and <span class="cn-word" data-pos="verb" data-tr="uddalay olmadi">failed</span> lost it too.</p>

<p>Then Nasreddin Afandi <span class="cn-word" data-pos="verb" data-tr="oldinga chiqdi">stepped forward</span> and <span class="cn-word" data-pos="verb" data-tr="taʼzim qildi">bowed</span>.</p>

<p>"I <strong>will teach</strong> him, my lord. I <strong>will</strong> give you a reading donkey. But I need ten years and a bag of <span class="cn-word" data-tr="tilla">gold</span>."</p>

<p>The emir laughed and gave him the gold.</p>

<p>At home Afandi's wife counted the <span class="cn-word" data-tr="tangalar">coins</span> twice. Then she began to cry.</p>

<p>"In ten years they <strong>will kill</strong> you," she said. "A donkey <strong>won't</strong> read. It <strong>won't</strong> even open a book!"</p>

<p>"<strong>Will</strong> you <strong>listen</strong> to me for one minute?" Afandi said. "Ten years is a long road, and one of three things <strong>will happen</strong> on it. The emir <strong>will die</strong>. Or the donkey <strong>will die</strong>. Or I <strong>will die</strong>. And nobody in this city <strong>will remember</strong> my <span class="cn-word" data-tr="vaʼda">promise</span>."</p>

<p>Then he sat down and ate his dinner in <span class="cn-word" data-tr="jimlik">silence</span>.</p>

<p>The emir died in the seventh year. The donkey lived two years longer than the emir, in Afandi's own yard, and it ate very well.</p>

<p>People in Bukhara still tell this story. Afandi was not a <span class="cn-word" data-tr="yolgʻonchi">liar</span>, they say. He simply knew one thing the emir did not: nobody knows what <strong>will happen</strong> in ten years.</p>''',
        "questions": [
            {
                "text": "Why does Afandi ask for ten years?",
                "choices": [
                    "Because teaching a donkey to read is slow work",
                    "Because in ten years the promise will probably not matter to anybody",
                    "Because he wants to travel and come back",
                ],
                "answer": 1,
                "explanation": "“The emir will die. Or the donkey will die. Or I "
                               "will die. And nobody in this city will remember "
                               "my promise.” Vaqt — Afandining eng kuchli "
                               "quroli.",
            },
            {
                "text": "Which sentence from the story is a PROMISE, not a prediction?",
                "choices": [
                    "In ten years they will kill you.",
                    "I will teach him, my lord.",
                    "A donkey won't read.",
                ],
                "answer": 1,
                "explanation": "Vaʼda — gapirayotgan odam <b>oʻzi</b> "
                               "qiladigan ish. Qolgan ikkitasi kelajak "
                               "haqidagi taxmin.",
            },
            {
                "text": "Which line is correct English?",
                "choices": [
                    "Will you to listen to me?",
                    "Will you listen to me?",
                    "Will you listening to me?",
                ],
                "answer": 1,
                "explanation": "<b>will</b> dan keyin feʼl hamisha asosiy "
                               "shaklda: <i>listen</i>. <i>to</i> ham, "
                               "<i>-ing</i> ham qoʻshilmaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-27 — be going to: plans and evidence  (life story)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Shepherd Who Read the Sky",
        "summary": (
            "PE-27 matni. Botir bobo na soat, na telefon koʻrgan — lekin "
            "aprelning koʻk osmoni ostida qishloqni ogohlantiradi. "
            "“going to” — koʻz oldingizdagi dalilning tili."
        ),
        "order":   27,
        "grammar": [
            {
                "pattern":  "be going to = evidence you can see now",
                "meaning":  "Hozir <b>koʻrinib turgan dalil</b> asosida "
                            "aytilgan taxmin: chumolilar koʻchdi, qushlar "
                            "baland uya qurdi — <i>it is going to rain</i>. "
                            "Bu <i>will</i> emas: gapiruvchi taxmin "
                            "qilmaydi, <b>oʻqiydi</b>.",
                "examples": ["It is going to rain for three days.",
                             "The river is going to come into these houses."],
            },
            {
                "pattern":  "be going to = a plan already decided",
                "meaning":  "Ikkinchi vazifasi — <b>oldindan qaror "
                            "qilingan</b> reja: <i>I am going to read it "
                            "with numbers</i>. Qaror gapirishdan oldin "
                            "qabul qilingan boʻlsa, <i>going to</i> "
                            "ishlatiladi.",
                "examples": ["I am going to spend my life on this.",
                             "I am going to read the sky with numbers."],
            },
            {
                "pattern":  "Questions, negatives, and “gonna”",
                "meaning":  "Savol va inkor <i>be</i> feʼli bilan "
                            "yasaladi: <i>Are you going to read the "
                            "clouds?</i>, <i>It isn't going to stop</i>. "
                            "Gapirishda <i>going to</i> koʻpincha "
                            "“<b>gonna</b>” boʻlib eshitiladi — lekin "
                            "yozishda hech qachon.",
                "examples": ["Are you going to read the clouds for us?",
                             "This rain isn't going to stop tonight."],
            },
        ],
        "body": '''<p>Botir was seventy years old. He had no watch, no phone and no television. He had four hundred <span class="cn-word" data-tr="qoʻylar">sheep</span> and the sky.</p>

<p>On a Tuesday in April he walked down to the village and <span class="cn-word" data-pos="verb" data-tr="taqillatdi">knocked</span> on the first door.</p>

<p>"Take your animals up the hill," he said. "It <strong>is going to rain</strong> for three days. The <span class="cn-word" data-tr="soy, jilgʻa">stream</span> <strong>is going to come</strong> into these houses."</p>

<p>The sky was blue. People laughed at him in their <span class="cn-word" data-tr="eshik oldida">doorways</span>.</p>

<p>"How do you know, old man? <strong>Are</strong> you <strong>going to read</strong> the clouds for us?"</p>

<p>"The <span class="cn-word" data-tr="chumolilar">ants</span> left the <span class="cn-word" data-tr="pastqam yer">low ground</span> yesterday," Botir said. "The birds are building their <span class="cn-word" data-tr="uyalar">nests</span> high. My sheep didn't drink this morning. And my knee hurts."</p>

<p>Two families listened to him. His own, and a woman with three children.</p>

<p>The rain started that night. It rained on Wednesday. It rained on Thursday. On Friday morning the stream behind the school was a brown river, and it was inside the low houses.</p>

<p>Nobody died. But sixteen families slept in the school for a month, and the village lost two hundred animals.</p>

<p>Botir's <span class="cn-word" data-tr="nabira">grandson</span> was eleven that April. He is twenty-six now, and he works at the <span class="cn-word" data-tr="ob-havo stansiyasi">weather station</span> in the city, with three computers and a wall of maps.</p>

<p>People often ask him why he chose this work.</p>

<p>"My grandfather read the sky with his knee," he says. "I <strong>am going to read</strong> it with numbers. And next time, somebody in that village <strong>is going to believe</strong> the <span class="cn-word" data-tr="ogohlantirish">warning</span>."</p>''',
        "questions": [
            {
                "text": "What made Botir sure about the rain?",
                "choices": [
                    "The colour of the sky",
                    "The ants, the birds, his sheep and his knee",
                    "A weather report on the radio",
                ],
                "answer": 1,
                "explanation": "U dalillarni sanaydi: chumolilar past "
                               "yerdan koʻchdi, qushlar baland uya "
                               "quryapti, qoʻylar suv ichmadi, tizzasi "
                               "ogʻriyapti.",
            },
            {
                "text": "Why is \"It is going to rain\" better than \"It will rain\" in his warning?",
                "choices": [
                    "Because he can see the evidence in front of him",
                    "Because \"will\" is not correct with the weather",
                    "Because he decided it at that moment",
                ],
                "answer": 0,
                "explanation": "<b>going to</b> — koʻrinib turgan dalil "
                               "tili. <i>will</i> shu daqiqada qilingan "
                               "taxmin yoki qarorni bildiradi.",
            },
            {
                "text": "What does the grandson mean by \"I am going to read it with numbers\"?",
                "choices": [
                    "He has already decided to do his grandfather's work with science",
                    "He is reading a book about numbers now",
                    "He will decide about his job later",
                ],
                "answer": 0,
                "explanation": "<b>going to</b> ning ikkinchi vazifasi — "
                               "allaqachon qabul qilingan reja. U "
                               "ob-havo stansiyasida ishlaydi: qaror "
                               "ancha oldin qilingan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-28 — present continuous for future arrangements  (diary)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Last Week in the Village",
        "summary": (
            "PE-28 matni. Koʻchishdan oldingi oxirgi hafta — kundalik "
            "shaklida. Har bir kunda kelishilgan reja: yuk mashinasi "
            "oltida keladi, biz shanbada ketamiz."
        ),
        "order":   28,
        "grammar": [
            {
                "pattern":  "Present continuous = a FIXED arrangement",
                "meaning":  "Kelishib qoʻyilgan, kun va soati bor ish "
                            "davomli zamonda aytiladi — xuddi hozir "
                            "boʻlayotgandek: <i>We are moving on "
                            "Saturday</i>. Kundalikning har sahifasi "
                            "shunday gaplardan iborat.",
                "examples": ["We are moving on Saturday.",
                             "The truck is coming at six tomorrow morning."],
            },
            {
                "pattern":  "The time word tells you which meaning",
                "meaning":  "Bir xil shakl ikki maʼnoni beradi. "
                            "<i>I am writing this in the dark</i> — hozir. "
                            "<i>I am starting a new school on Monday</i> — "
                            "kelajak. Farqni <b>vaqt soʻzi</b> koʻrsatadi.",
                "examples": ["I am writing this in the dark.",
                             "On Monday I am starting a new school."],
            },
            {
                "pattern":  "Only for things people ARRANGE",
                "meaning":  "Inson kelishib qoʻyadigan ishlar uchun: "
                            "uchrashuv, safar, ish, dars. Ob-havo yoki "
                            "tabiat uchun ishlatilmaydi — “<i>It is "
                            "raining tomorrow</i>” xato, chunki yomgʻir "
                            "bilan kelishib boʻlmaydi (PE-27 ga qaraydi).",
                "examples": ["My father is starting his new job on the fifteenth.",
                             "My grandmother isn't coming with us."],
            },
        ],
        "body": '''<p><strong>Monday.</strong> It is <span class="cn-word" data-pos="adj" data-tr="rasmiy">official</span>: <strong>we are moving</strong> on Saturday. My father <strong>is starting</strong> his new job at a factory in Tashkent on the fifteenth.</p>

<p><strong>Tuesday.</strong> I told the class today. Dilnoza put her head on the desk and said nothing for a <span class="cn-word" data-pos="adj" data-tr="butun">whole</span> lesson. "<strong>Are</strong> you <strong>coming</strong> back in the summer?" she asked at the gate. "<strong>We are coming</strong> every July," I said. I <span class="cn-word" data-pos="verb" data-tr="umid qilaman">hope</span> that is true.</p>

<p><strong>Wednesday.</strong> Mother <strong>is selling</strong> the beds and the big <span class="cn-word" data-tr="karton qutilar">cardboard boxes</span> are already in the corridor. Our life is in eleven boxes. Eleven!</p>

<p><strong>Thursday.</strong> My grandmother <strong>isn't coming</strong> with us. She <strong>is staying</strong> in this house with the <span class="cn-word" data-tr="oʻrik">apricot</span> tree. "That tree <strong>isn't going</strong> anywhere either," she says.</p>

<p><strong>Friday.</strong> The <span class="cn-word" data-tr="yuk mashinasi">truck</span> <strong>is coming</strong> at six tomorrow morning. My <span class="cn-word" data-tr="amakivachcha">cousin</span> <strong>is driving</strong> it. We <strong>are taking</strong> the cat in a box with <span class="cn-word" data-tr="teshiklar">holes</span> in the top. My grandmother <strong>is making</strong> bread for the road tonight — she started at nine.</p>

<p><strong>Saturday, five o'clock.</strong> Nobody is asleep. The house is empty and it makes a strange sound when you walk. My grandmother <span class="cn-word" data-pos="verb" data-tr="quchoqladi">hugged</span> me at the door and put warm bread in my hands.</p>

<p><strong>I am writing</strong> this in the dark in the front of the truck. One thing is <span class="cn-word" data-pos="adj" data-tr="aniq">certain</span>: on Monday <strong>I am starting</strong> a new school where nobody knows my name.</p>

<p>And in July, <strong>I am coming</strong> back to that tree.</p>''',
        "questions": [
            {
                "text": "Who is staying in the village?",
                "choices": [
                    "The grandmother",
                    "The cousin with the truck",
                    "The cat",
                ],
                "answer": 0,
                "explanation": "“My grandmother isn't coming with us. She is "
                               "staying in this house with the apricot tree.”",
            },
            {
                "text": "In the diary, which sentence is about the FUTURE?",
                "choices": [
                    "I am writing this in the dark.",
                    "On Monday I am starting a new school.",
                    "The house is empty.",
                ],
                "answer": 1,
                "explanation": "Shakl bir xil, lekin <i>on Monday</i> vaqt "
                               "soʻzi bu gapni kelajakka olib chiqadi.",
            },
            {
                "text": "Which sentence is NOT possible in English?",
                "choices": [
                    "The truck is coming at six tomorrow.",
                    "My father is starting his job on the fifteenth.",
                    "It is raining tomorrow afternoon.",
                ],
                "answer": 2,
                "explanation": "Bu zamon faqat <b>kelishilgan</b> ishlar "
                               "uchun. Yomgʻir bilan kelishib boʻlmaydi — "
                               "u yerda <i>it is going to rain</i> yoki "
                               "<i>it will rain</i> kerak.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-29 — will vs going to vs present continuous  (three messages)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Three Ways to Say Tomorrow",
        "summary": (
            "PE-29 matni. Bitta shanba, uchta xabar, uchta boshqa kelasi "
            "zamon. Ingliz tili nima boʻlishini emas, qarorni QACHON "
            "qabul qilganingizni ham aytadi."
        ),
        "order":   29,
        "grammar": [
            {
                "pattern":  "Present continuous = arranged with other people",
                "meaning":  "Kelishilgan, chiptasi bor ish: "
                            "<i>We are meeting at six</i>. Eng "
                            "“qatʼiy” kelasi zamon — chunki reja "
                            "boshqalar bilan tuzilgan.",
                "examples": ["We are meeting at the bus station at six.",
                             "The bus leaves at 6:20."],
            },
            {
                "pattern":  "going to = decided before now",
                "meaning":  "Qaror gapirishdan oldin qabul qilingan, "
                            "lekin hali kelishilmagan: <i>I am going "
                            "to take the big bag</i> — “katta sumkani "
                            "olaman deb turganman”.",
                "examples": ["I am going to take the big bag.",
                             "My mother is going to make food for four people."],
            },
            {
                "pattern":  "will = decided in this second",
                "meaning":  "Shu daqiqada tugʻilgan qaror yoki vaʼda: "
                            "<i>I will come!</i> Shuning uchun "
                            "Sherbekning xabari kechqurun soat "
                            "oʻn birda keladi — u bir daqiqa oldin "
                            "hech narsa rejalashtirmagan edi.",
                "examples": ["I will come!", "I will buy a ticket on the bus."],
            },
        ],
        "body": '''<p>Three friends, one Saturday, three <span class="cn-word" data-tr="xabarlar">messages</span>. They are all about the same <span class="cn-word" data-tr="safar">trip</span> to the <span class="cn-word" data-tr="togʻlar">mountains</span> — and every message chooses a different future.</p>

<p><strong>Jasur, 9:14 p.m.</strong> "We <strong>are meeting</strong> at the bus <span class="cn-word" data-tr="bekat, vokzal">station</span> at six. The bus <strong>leaves</strong> at 6:20. I have three <span class="cn-word" data-tr="chiptalar">tickets</span> in my pocket."</p>

<p><strong>Dilnoza, 9:31 p.m.</strong> "OK. I <strong>am going to take</strong> the big bag — my mother <strong>is going to make</strong> food for four people, so we <strong>aren't going to be</strong> hungry on that hill."</p>

<p><strong>Sherbek, 11:02 p.m.</strong> "I <strong>will come</strong>!!"</p>

<p>An hour before that message, Sherbek was not going on this trip at all. Three tickets, three friends, and he was not one of them.</p>

<p>At six in the morning he was at the station with a small bag and no ticket. "Don't <span class="cn-word" data-tr="xavotir olmang">worry</span>," he said. "I <strong>will buy</strong> one on the bus."</p>

<p>The bus was full. There were no tickets left. The <span class="cn-word" data-tr="haydovchi">driver</span> looked at him and <span class="cn-word" data-pos="verb" data-tr="ishora qildi">pointed</span> at the road.</p>

<p>"It <strong>is going to be</strong> a long day for you, boy."</p>

<p>At eleven o'clock the three friends walked to the top of the <span class="cn-word" data-tr="tepalik">hill</span>. Sherbek was already sitting there with bread and two bottles of water.</p>

<p>"How?"</p>

<p>"A man with a <span class="cn-word" data-tr="yuk mashinasi">lorry</span> was going to the next village," he said. "He stopped because I was standing in the road."</p>

<p>Three futures, three sentences: <i>we are meeting</i> (arranged), <i>I am going to take</i> (decided yesterday), <i>I will come</i> (decided in that second). English tells you not only WHAT happens tomorrow, but WHEN you decided it.</p>''',
        "questions": [
            {
                "text": "How does Sherbek get to the top of the hill?",
                "choices": [
                    "He buys a ticket on the bus",
                    "A lorry driver stops for him",
                    "He walks all the way",
                ],
                "answer": 1,
                "explanation": "Avtobusda joy yoʻq edi. “A man with a lorry "
                               "was going to the next village… He stopped "
                               "because I was standing in the road.”",
            },
            {
                "text": "Why does Jasur use \"We are meeting at six\"?",
                "choices": [
                    "Because it is a plan he is deciding now",
                    "Because it is arranged: he already has the tickets",
                    "Because it is a prediction about tomorrow",
                ],
                "answer": 1,
                "explanation": "Chiptalar kissasida — reja kelishilgan. "
                               "Kelishilgan ishlar uchun davomli zamon.",
            },
            {
                "text": "Your friend asks for help and you decide at that moment. What do you say?",
                "choices": [
                    "I am helping you.",
                    "I am going to help you.",
                    "I will help you.",
                ],
                "answer": 2,
                "explanation": "Shu daqiqada qilingan qaror — <b>will</b>. "
                               "Aynan shu sababdan Sherbekning “I will "
                               "come!” xabari kechasi soat oʻn birda "
                               "keladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-30 — future continuous  (life story)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "This Time Next Year",
        "summary": (
            "PE-30 matni. Afsonaning ismi roʻyxatda yoʻq edi — uch ball "
            "kam. Otasi darvozada bitta gap aytdi, va oʻsha gap bir yilni "
            "koʻtardi."
        ),
        "order":   30,
        "grammar": [
            {
                "pattern":  "will be + verb-ing",
                "meaning":  "Kelajakning bir <b>daqiqasida</b> davom "
                            "etayotgan ish: <i>At nine tomorrow I "
                            "<b>will be sitting</b> in that room</i>. "
                            "Bu zamon suratni koʻrsatadi — nafaqat "
                            "voqeani.",
                "examples": ["This time next year you will be walking into that building.",
                             "In August you will be sitting in a room with two hundred people."],
            },
            {
                "pattern":  "Its favourite time words",
                "meaning":  "<b>this time next year</b>, <b>at nine "
                            "tomorrow</b>, <b>in five years</b> — "
                            "kelajakdagi aniq bir nuqtani beradigan "
                            "soʻzlar. Shuning uchun bu zamon rejalar va "
                            "orzular tilida koʻp uchraydi.",
                "examples": ["In five years I will be teaching in this school."],
            },
            {
                "pattern":  "Will you be …? · won't be …",
                "meaning":  "Savol: <i>Will you be thinking about "
                            "February?</i> Inkor: <i>I won't be "
                            "waiting</i>. Uchta soʻz bir tartibda: "
                            "<b>will + be + -ing</b>.",
                "examples": ["Will you be thinking about February?",
                             "I won't be standing here again."],
            },
        ],
        "body": '''<p>In August, Afsona's name was not on the list. She read it four times, from the top to the <span class="cn-word" data-tr="oxirigacha">bottom</span>. She was three <span class="cn-word" data-tr="ball">points</span> <span class="cn-word" data-tr="chiziqdan pastda">below the line</span>.</p>

<p>Her mother said nothing on the bus home. Her father said one sentence at the gate.</p>

<p>"<strong>This time next year</strong> you <strong>will be walking</strong> into that building."</p>

<p>A year is three hundred and sixty-five days. Afsona wrote his sentence on a piece of paper and put it above her desk.</p>

<p>From September she worked in the bakery on the corner from six to eleven every morning, carrying trays. In the afternoons she <span class="cn-word" data-pos="verb" data-tr="takrorladi">revised</span>. Her <span class="cn-word" data-tr="budilnik">alarm clock</span> <span class="cn-word" data-pos="verb" data-tr="jiringlardi">rang</span> at half past four.</p>

<p>In February she wanted to stop. Her little brother found her <span class="cn-word" data-pos="verb" data-tr="yigʻlab oʻtirgan">crying</span> at that desk at midnight, with the paper in her hand.</p>

<p>He was nine years old, and he used his father's <span class="cn-word" data-tr="usulini">trick</span> on her.</p>

<p>"In August you <strong>will be sitting</strong> in a room with two hundred people," he said. "<strong>Will</strong> you <strong>be thinking</strong> about February?"</p>

<p>In July she slept four hours a night. In the last week she didn't open one book: she walked <span class="cn-word" data-pos="adv" data-tr="buning oʻrniga">instead</span>.</p>

<p>On the first of August, at nine o'clock in the morning, she was walking into that building.</p>

<p>Her name was on the list in the second week. Number forty-one.</p>

<p>There is a new paper above that desk now, in her own writing: "In five years I <strong>will be teaching</strong> in the school in my street."</p>

<p>She is in her third year. Two more Augusts.</p>''',
        "questions": [
            {
                "text": "What did her little brother do in February?",
                "choices": [
                    "He said their father's sentence back to her in a new way",
                    "He told her to stop studying",
                    "He woke her at half past four",
                ],
                "answer": 0,
                "explanation": "“In August you will be sitting in a room "
                               "with two hundred people. Will you be "
                               "thinking about February?” — toʻqqiz "
                               "yoshli bola otasining usulini ishlatdi.",
            },
            {
                "text": "Which sentence is correct future continuous?",
                "choices": [
                    "This time next year you will walking into that building.",
                    "This time next year you will be walking into that building.",
                    "This time next year you are be walking into that building.",
                ],
                "answer": 1,
                "explanation": "Uchta qism bir tartibda: <b>will + be + "
                               "-ing</b>. Bittasi tushib qolsa, gap buziladi.",
            },
            {
                "text": "Why does the story end with \"Two more Augusts\"?",
                "choices": [
                    "Because she needs two more years to finish and become a teacher",
                    "Because she is going to take the exam twice again",
                    "Because August is her favourite month",
                ],
                "answer": 0,
                "explanation": "U uchinchi kursda. Devordagi yangi gap — "
                               "“In five years I will be teaching…” — va "
                               "unga yana ikki avgust qoldi.",
            },
        ],
    },
]
