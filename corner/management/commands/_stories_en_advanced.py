# English "Wonder" Readings — ADVANCED level (B2-C1, "a little higher than medium").
# IELTS-style engaging short reads. Story text = English; vocab/grammar/explanations in
# Uzbek. Richer vocabulary (~13 marks), complex sentences, 2 higher-level grammar points,
# 3 inference questions per story.
# Import: python manage.py import_corner corner/management/commands/_stories_en_advanced.py --author=<AUTHOR>

SUBJECT = {
    "name":    "English",
    "summary": "Ingliz tili: IELTS uslubidagi qiziqarli oʻqish matnlari — lugʻat va grammatika bilan.",
    "icon":    "bi-globe2",
    "color":   "#2563eb",
    "order":   2,
}

COLLECTION = {
    "title":       "Advanced Reads",
    "description": "Oʻrtadan yuqori daraja (B2-C1) — boy lugʻat va murakkab jumlalar.",
    "order":       3,
}

STORIES = [
    # ── 1 ────────────────────────────────────────────────────────────────
    {
        "title":   "We Are Made of Stardust",
        "summary": "Tanamizdagi atomlar milliardlab yil avval yulduzlar ichida yaratilgan — biz tom maʼnoda yulduz changidanmiz.",
        "order":   1,
        "body": '''<p>Where did the <span class="cn-word" data-tr="elementlar, unsurlar">elements</span> that make up our bodies come from? <span class="cn-word" data-pos="adv" data-tr="hayratlanarli tarzda">Astonishingly</span>, the carbon, oxygen and iron inside us were originally <span class="cn-word" data-pos="verb" data-tr="yaratilgan, quyilgan">forged</span> deep within stars. In the <span class="cn-word" data-pos="adj" data-tr="olis, uzoq">distant</span> past, <span class="cn-word" data-pos="adj" data-tr="ulkan, bahaybat">enormous</span> stars reached the end of their lives and <span class="cn-word" data-pos="verb" data-tr="portladi">exploded</span> with <span class="cn-word" data-pos="adj" data-tr="dahshatli, ulkan">tremendous</span> force.</p>
<p>Through these explosions, the elements that <strong>had been</strong> <span class="cn-word" data-pos="verb" data-tr="qamalgan">trapped</span> inside the stars were <span class="cn-word" data-pos="verb" data-tr="sochilib ketdi">scattered</span> across space. Over billions of years, they <span class="cn-word" data-pos="adv" data-tr="asta-sekin">gradually</span> <span class="cn-word" data-pos="verb" data-tr="jipslashdi, birlashdi">clumped</span> together to form planets and living things. So when we <span class="cn-word" data-pos="verb" data-tr="tikilmoq">gaze</span> up at the stars at night, we are, <strong>in a sense</strong>, looking at distant <span class="cn-word" data-tr="qarindoshlar">relatives</span>. Every one of us was born from the <span class="cn-word" data-pos="adj" data-tr="yaltiroq, porloq">shining</span> dust of long-dead stars.</p>''',
        "grammar": [
            {
                "pattern":  "had been + past participle (past perfect passive)",
                "meaning":  "...langan edi — oʻtmishdagi boshqa ishdan avval sodir boʻlgan majhul harakat.",
                "examples": ["The elements had been trapped inside the stars.", "By the time we arrived, the food had been eaten."],
            },
            {
                "pattern":  "in a sense",
                "meaning":  "Maʼlum maʼnoda, bir jihatdan (fikrni yumshatuvchi ibora).",
                "examples": ["In a sense, we are looking at distant relatives.", "In a sense, he was right."],
            },
        ],
        "questions": [
            {
                "text": "Where were the elements in our bodies originally created?",
                "choices": ["In the oceans of the early Earth", "Deep inside stars", "In the centre of the Sun today"],
                "answer": 1,
                "explanation": "Matnda tanamizdagi uglerod, kislorod va temir dastlab yulduzlar ichida yaratilgani aytilgan.",
            },
            {
                "text": "How were these elements spread across space?",
                "choices": [
                    "Through the explosions of enormous dying stars",
                    "By comets carrying them from planet to planet",
                    "By the light of the Sun",
                ],
                "answer": 0,
                "explanation": "Ulkan yulduzlar umri tugab portlaganda, ular ichidagi elementlar koinotga sochilgan.",
            },
            {
                "text": "Why does the writer call the stars our 'relatives'?",
                "choices": [
                    "Because the stars watch over us like family",
                    "Because our bodies and the stars are made of the same elements",
                    "Because humans first lived on other stars",
                ],
                "answer": 1,
                "explanation": "Tanamiz ham, yulduzlar ham bir xil elementlardan tashkil topgani uchun muallif ularni ‘qarindosh’ deb ataydi.",
            },
        ],
    },
    # ── 2 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Smell of Space",
        "summary": "Koinotning oʻzi vakuum boʻlsa-da, kosmosdan qaytgan astronavtlar skafandrlaridan gʻalati hid kelishini aytishadi.",
        "order":   2,
        "body": '''<p>Because space is a <span class="cn-word" data-tr="vakuum, boʻshliq">vacuum</span>, it is impossible to smell anything directly out there. <span class="cn-word" data-pos="adv" data-tr="shunga qaramay">Nevertheless</span>, astronauts returning from <span class="cn-word" data-tr="ochiq kosmosga chiqish">spacewalks</span> <span class="cn-word" data-pos="adv" data-tr="bir ovozdan">unanimously</span> report that their suits give off a <span class="cn-word" data-pos="adj" data-tr="oʻziga xos, gʻalati">peculiar</span> smell.</p>
<p><strong>According to their</strong> <span class="cn-word" data-tr="aytishlaricha, guvohliklari">accounts</span>, the smell <span class="cn-word" data-pos="verb" data-tr="oʻxshaydi">resembles</span> burning metal, <span class="cn-word" data-tr="porox">gunpowder</span>, or <span class="cn-word" data-pos="verb" data-tr="qovurilgan">seared</span> meat. Scientists <span class="cn-word" data-pos="verb" data-tr="taxmin qiladi">suspect</span> that this mysterious <span class="cn-word" data-tr="hid">odour</span> <strong>may be caused by</strong> high-energy <span class="cn-word" data-tr="zarralar">particles</span> <span class="cn-word" data-pos="verb" data-tr="chiqarilgan, taratilgan">emitted</span> by distant dying stars. In other words, the smell we notice is, in fact, a <span class="cn-word" data-tr="iz, asorat">trace</span> of stars that <span class="cn-word" data-pos="verb" data-tr="yoʻqolib ketgan">vanished</span> billions of years ago.</p>''',
        "grammar": [
            {
                "pattern":  "according to + noun",
                "meaning":  "...ga koʻra, ...ning aytishicha (manbaga tayanish).",
                "examples": ["According to the astronauts, the smell is strong.", "According to the report, sales rose."],
            },
            {
                "pattern":  "may be + past participle (modal passive)",
                "meaning":  "...langan / ... boʻlishi mumkin (ehtimollik + majhul nisbat).",
                "examples": ["The smell may be caused by dying stars.", "The problem may be solved soon."],
            },
        ],
        "questions": [
            {
                "text": "Why is it impossible to smell space directly?",
                "choices": ["Because space is a vacuum", "Because it is too cold", "Because there are no stars nearby"],
                "answer": 0,
                "explanation": "Koinot vakuum (boʻshliq) boʻlgani uchun u yerda hidni bevosita hidlab boʻlmaydi.",
            },
            {
                "text": "What does the smell on the astronauts' suits resemble?",
                "choices": [
                    "Fresh flowers and fruit",
                    "Burning metal, gunpowder, or seared meat",
                    "Salt water",
                ],
                "answer": 1,
                "explanation": "Astronavtlarning aytishicha, hid yonayotgan metall, porox yoki qovurilgan goʻshtga oʻxshaydi.",
            },
            {
                "text": "What do scientists suspect causes the smell?",
                "choices": [
                    "High-energy particles emitted by distant dying stars",
                    "The astronauts' own food",
                    "Old fuel from the spacecraft",
                ],
                "answer": 0,
                "explanation": "Olimlar hidni uzoqdagi oʻlayotgan yulduzlar taratayotgan yuqori energiyali zarralar keltirib chiqargan boʻlishi mumkin deb taxmin qiladi.",
            },
        ],
    },
    # ── 3 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Green Sahara",
        "summary": "Bugungi cheksiz qumli Sahara bir necha ming yil avval koʻllar va daryolarga toʻla yashil dasht boʻlgan.",
        "order":   3,
        "body": '''<p>Could you believe that the Sahara, the largest <span class="cn-word" data-tr="choʻl, sahro">desert</span> in the world, <strong>was once</strong> a green <span class="cn-word" data-tr="dasht, yaylov">grassland</span>? Today it is <span class="cn-word" data-pos="verb" data-tr="qoplangan">covered</span> in <span class="cn-word" data-pos="adj" data-tr="cheksiz">endless</span> <span class="cn-word" data-tr="kengliklar, choʻzilgan maydonlar">stretches</span> of dry sand, yet only a few thousand years ago, <span class="cn-word" data-tr="koʻllar">lakes</span> and rivers flowed here and <span class="cn-word" data-tr="begemotlar">hippos</span> lived in the water.</p>
<p><span class="cn-word" data-pos="adv" data-tr="ajablanarlisi shundaki">Remarkably</span>, ancient <span class="cn-word" data-tr="gʻor rasmlari">cave paintings</span> in the Sahara even show people swimming. <span class="cn-word" data-tr="olimlar">Scholars</span> explain that as the tilt of the Earth slowly <span class="cn-word" data-pos="verb" data-tr="oʻzgardi, siljidi">shifted</span>, the <span class="cn-word" data-tr="yoʻnalishlar, koʻrinishlar">patterns</span> of the rain clouds changed, and the grassland <strong><span class="cn-word" data-pos="verb" data-tr="aylandi">turned into</span></strong> desert. Interestingly, they believe that in the far future the Sahara may <span class="cn-word" data-pos="verb" data-tr="qayta tiklamoq">regain</span> its green colour once again.</p>''',
        "grammar": [
            {
                "pattern":  "once (formerly)",
                "meaning":  "Bir vaqtlar, ilgari (oʻtmishdagi holatni bildiradi).",
                "examples": ["The Sahara was once a green grassland.", "This town was once very small."],
            },
            {
                "pattern":  "turn into + noun",
                "meaning":  "...ga aylanmoq (bir holatdan boshqasiga oʻzgarish).",
                "examples": ["The grassland turned into a desert.", "The rain turned into snow."],
            },
        ],
        "questions": [
            {
                "text": "What was the Sahara like a few thousand years ago?",
                "choices": [
                    "A green grassland with lakes, rivers, and hippos",
                    "An ocean full of fish",
                    "A land covered in ice",
                ],
                "answer": 0,
                "explanation": "Bir necha ming yil avval Saharada koʻllar va daryolar boʻlib, begemotlar yashagan — u yashil dasht boʻlgan.",
            },
            {
                "text": "What do the cave paintings of swimmers suggest?",
                "choices": [
                    "That there was once plenty of water in the Sahara",
                    "That ancient people could not really swim",
                    "That the paintings are very recent",
                ],
                "answer": 0,
                "explanation": "Choʻl oʻrtasidagi suzuvchilar rasmi oʻsha yerda bir vaqtlar suv koʻp boʻlganini koʻrsatadi.",
            },
            {
                "text": "According to scholars, why did the grassland become a desert?",
                "choices": [
                    "People cut down all the trees",
                    "The Earth's tilt shifted and the rain cloud patterns changed",
                    "A huge volcano erupted",
                ],
                "answer": 1,
                "explanation": "Olimlar Yer oʻqining qiyaligi oʻzgarib, yomgʻir bulutlari yoʻnalishi oʻzgargani sabab dasht choʻlga aylandi deb tushuntiradi.",
            },
        ],
    },
    # ── 4 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Deepest Place on Earth",
        "summary": "Marian botigʻi shunchalik chuqurki, Everestni unga solsangiz choʻqqisi hali ham 2 km suv ostida qoladi.",
        "order":   4,
        "body": '''<p>Where is the deepest place on Earth? It is the Mariana <span class="cn-word" data-tr="botiq, chuqurlik">Trench</span> in the Pacific Ocean, which <span class="cn-word" data-pos="verb" data-tr="yetadi">reaches</span> a <span class="cn-word" data-tr="chuqurlik">depth</span> of about eleven kilometres. <strong>If you placed</strong> Mount Everest, the tallest mountain in the world, into the trench, its <span class="cn-word" data-tr="choʻqqi">peak</span> would still be two kilometres <span class="cn-word" data-pos="adv" data-tr="suv ostida">underwater</span>.</p>
<p>This deep world is a place of <span class="cn-word" data-pos="adj" data-tr="qop-qorongʻi">pitch-black</span> darkness where not a single <span class="cn-word" data-tr="nur">ray</span> of sunlight <span class="cn-word" data-pos="verb" data-tr="kirib boradi, oʻtib boradi">penetrates</span>. Moreover, the water <span class="cn-word" data-tr="bosim">pressure</span> is about a thousand times greater than at the surface — <strong>strong enough to</strong> <span class="cn-word" data-pos="verb" data-tr="ezib tashlamoq">crush</span> a human body in an instant. <span class="cn-word" data-pos="adv" data-tr="hayratlanarlisi">Astonishingly</span>, living creatures still <span class="cn-word" data-pos="verb" data-tr="omon qoladi, yashaydi">survive</span> in this <span class="cn-word" data-pos="adj" data-tr="oʻta ogʻir, ekstremal">extreme</span> environment. In fact, more people have travelled to the Moon than to the bottom of this trench.</p>''',
        "grammar": [
            {
                "pattern":  "If + past, ... would + verb (second conditional)",
                "meaning":  "Faraziy/xayoliy shart: agar ...sa edi, ... boʻlardi (hozir yoki umuman haqiqatga zid).",
                "examples": ["If you placed Everest here, its peak would still be underwater.", "If I had more time, I would travel."],
            },
            {
                "pattern":  "adjective + enough to + verb",
                "meaning":  "...gulik darajada (yetarlicha) ... — natijani bildiradi.",
                "examples": ["The pressure is strong enough to crush a body.", "He is old enough to drive."],
            },
        ],
        "questions": [
            {
                "text": "How deep is the Mariana Trench?",
                "choices": [
                    "About eleven kilometres — deep enough that Everest's peak would still be underwater",
                    "About two kilometres, the same as Mount Everest",
                    "Only a few hundred metres",
                ],
                "answer": 0,
                "explanation": "Botiq taxminan 11 km chuqur; Everestni unga solsangiz ham choʻqqisi hali 2 km suv ostida qoladi.",
            },
            {
                "text": "What is the environment at the bottom of the trench like?",
                "choices": [
                    "Bright and warm, like a shallow sea",
                    "Pitch-black, with pressure about a thousand times that at the surface",
                    "Completely empty, with no life at all",
                ],
                "answer": 1,
                "explanation": "Botiq tubi zim-ziyo, suv bosimi yer yuzasidan taxminan ming barobar kuchli; shunga qaramay u yerda hayot bor.",
            },
            {
                "text": "What does the last sentence mainly emphasise?",
                "choices": [
                    "That reaching the bottom is so hard that more people have been to the Moon",
                    "That the Moon is deeper than the ocean",
                    "That nobody has ever explored the trench",
                ],
                "answer": 0,
                "explanation": "Dengiz tubiga borgan odam Oyga borganlardan kam — bu chuqurlikni tekshirish nechogʻlik qiyinligini koʻrsatadi.",
            },
        ],
    },
]
