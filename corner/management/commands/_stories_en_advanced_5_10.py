# English "Wonder" Readings — ADVANCED level, stories 5-10 (brings Advanced Reads to a pack of 10).
# Grammar pattern shown in BOLD (<strong>) where it appears in the story; vocab marks kept off
# the bolded words. Story text = English; vocab/grammar/explanations in Uzbek. ~10-13 marks each.
# Import: python manage.py import_corner corner/management/commands/_stories_en_advanced_5_10.py --author=<AUTHOR>

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
    # ── 5 ────────────────────────────────────────────────────────────────
    {
        "title":   "More Stars Than Grains of Sand",
        "summary": "Astronomlar kuzatiladigan koinotdagi yulduzlar soni Yerdagi barcha qumlardan koʻp deb hisoblaydi.",
        "order":   5,
        "body": '''<p>Imagine gathering every <span class="cn-word" data-tr="don, zarra">grain</span> of sand from every beach and desert on the entire planet. It sounds like an <span class="cn-word" data-pos="adj" data-tr="tasavvur qilib boʻlmas">unimaginable</span> number. <strong>And yet</strong>, <span class="cn-word" data-tr="astronomlar">astronomers</span> <span class="cn-word" data-pos="verb" data-tr="taxmin qiladi">estimate</span> that the number of stars in the <span class="cn-word" data-pos="adj" data-tr="kuzatiladigan">observable</span> universe is even greater than that.</p>
<p>The exact <span class="cn-word" data-tr="raqam">figure</span> is impossible to count, but scientists believe there are somewhere between 10^22 and 10^24 stars — a number so <span class="cn-word" data-pos="adj" data-tr="ulkan, bepoyon">vast</span> that the human mind can <span class="cn-word" data-pos="adv" data-tr="zoʻrgʻa">barely</span> <span class="cn-word" data-pos="verb" data-tr="anglab yetmoq">grasp</span> it. <strong>What is more</strong>, each of those stars may have its own planets <span class="cn-word" data-pos="verb" data-tr="aylanib turgan">circling</span> around it. When we look up at a clear night sky, we are seeing only a tiny <span class="cn-word" data-tr="ulush, boʻlak">fraction</span> of this <span class="cn-word" data-pos="adj" data-tr="cheksiz">endless</span> ocean of stars.</p>''',
        "grammar": [
            {
                "pattern":  "and yet (contrast)",
                "meaning":  "Shunga qaramay, ammo (kutilmagan qarama-qarshilikni kiritadi).",
                "examples": ["It sounds unimaginable, and yet the stars are even more.", "He is very rich, and yet he is not happy."],
            },
            {
                "pattern":  "what is more",
                "meaning":  "Bundan tashqari, ustiga-ustak (muhim qoʻshimcha maʼlumot).",
                "examples": ["What is more, each star may have its own planets.", "The room was small. What is more, it was cold."],
            },
        ],
        "questions": [
            {
                "text": "What comparison does the text make about the number of stars?",
                "choices": [
                    "There are fewer stars than planets",
                    "There are more stars than grains of sand on all of Earth's beaches and deserts",
                    "There are exactly as many stars as people",
                ],
                "answer": 1,
                "explanation": "Matnda kuzatiladigan koinotdagi yulduzlar soni Yerdagi barcha qum donalaridan koʻp ekani aytilgan.",
            },
            {
                "text": "Why can't scientists give an exact number of stars?",
                "choices": [
                    "The number is far too vast to count exactly",
                    "Telescopes are not allowed to look that far",
                    "The stars keep disappearing",
                ],
                "answer": 0,
                "explanation": "Yulduzlar soni shunchalik ulkanki, uni aniq sanab boʻlmaydi (10^22–10^24 orasida).",
            },
            {
                "text": "What extra point does the phrase ‘what is more’ add about the stars?",
                "choices": [
                    "Each of the stars may have its own planets",
                    "The stars are slowly going out",
                    "The stars are all the same size",
                ],
                "answer": 0,
                "explanation": "‘What is more’ orqali har bir yulduzning oʻz sayyoralari boʻlishi mumkinligi qoʻshiladi.",
            },
        ],
    },
    # ── 6 ────────────────────────────────────────────────────────────────
    {
        "title":   "A Day on Venus Is Longer Than Its Year",
        "summary": "Venera oʻz oʻqida shu qadar sekin aylanadiki, uning bir kuni bir yilidan uzoqroq davom etadi.",
        "order":   6,
        "body": '''<p>On Earth, we <span class="cn-word" data-pos="verb" data-tr="tabiiy deb bilmoq">take it for granted</span> that a day is much shorter than a year. On Venus, <strong>however</strong>, the <span class="cn-word" data-tr="aksincha, teskarisi">opposite</span> is true: a single day <span class="cn-word" data-pos="verb" data-tr="davom etadi">lasts</span> longer than a whole year. This strange fact comes from the way the planet moves.</p>
<p>Venus <span class="cn-word" data-pos="verb" data-tr="aylanadi (oʻqida)">spins</span> on its <span class="cn-word" data-tr="oʻq">axis</span> <span class="cn-word" data-pos="adv" data-tr="oʻta, nihoyatda">extremely</span> slowly, taking about 243 Earth days to turn just once. <strong>Meanwhile</strong>, it travels all the way around the Sun in only about 225 Earth days. As a result, one Venusian day is actually longer than one Venusian year. Stranger still, Venus <span class="cn-word" data-pos="verb" data-tr="aylanadi">rotates</span> in the opposite <span class="cn-word" data-tr="yoʻnalish">direction</span> to most planets, so on Venus the Sun would <span class="cn-word" data-pos="verb" data-tr="koʻrinardi">appear</span> to rise in the west.</p>''',
        "grammar": [
            {
                "pattern":  "however (mid-sentence contrast)",
                "meaning":  "Ammo, biroq (gap ichida qarama-qarshilikni bildiradi; vergul bilan ajratiladi).",
                "examples": ["On Venus, however, the opposite is true.", "The plan, however, did not work."],
            },
            {
                "pattern":  "meanwhile",
                "meaning":  "Shu bilan birga, shu paytda (bir vaqtda boshqa ish yuz beradi).",
                "examples": ["Meanwhile, it orbits the Sun in about 225 days.", "I cooked dinner; meanwhile, she set the table."],
            },
        ],
        "questions": [
            {
                "text": "What is unusual about time on Venus?",
                "choices": [
                    "A day on Venus is longer than a year on Venus",
                    "A year on Venus never ends",
                    "There is no day or night on Venus",
                ],
                "answer": 0,
                "explanation": "Venerada bir kun bir yildan uzoqroq davom etadi — bu Yerdagining aksi.",
            },
            {
                "text": "Why is a single day on Venus so long?",
                "choices": [
                    "Venus is very far from the Sun",
                    "Venus spins on its axis extremely slowly (about 243 Earth days per turn)",
                    "Venus does not move at all",
                ],
                "answer": 1,
                "explanation": "Venera oʻz oʻqida juda sekin — bir marta aylanishga taxminan 243 Yer kuni sarflaydi.",
            },
            {
                "text": "What else is strange about the way Venus spins?",
                "choices": [
                    "It rotates in the opposite direction, so the Sun would appear to rise in the west",
                    "It spins faster than any other planet",
                    "It stops spinning at night",
                ],
                "answer": 0,
                "explanation": "Venera koʻpchilik sayyoralarga teskari yoʻnalishda aylanadi, shu sabab Quyosh gʻarbdan chiqqandek koʻrinadi.",
            },
        ],
    },
    # ── 7 ────────────────────────────────────────────────────────────────
    {
        "title":   "Sharks Are Older Than Trees",
        "summary": "Akulalar taxminan 450 million yildan beri mavjud — yerda birinchi daraxtlar paydo boʻlishidan ancha avval.",
        "order":   7,
        "body": '''<p>Sharks are often seen as <span class="cn-word" data-pos="adj" data-tr="yovuz, vahshiy">fierce</span> hunters of the modern seas, but they are also <span class="cn-word" data-pos="adv" data-tr="hayratlanarli tarzda">astonishingly</span> <span class="cn-word" data-pos="adj" data-tr="qadimiy">ancient</span>. Sharks have existed for <span class="cn-word" data-pos="adv" data-tr="taxminan">roughly</span> 450 million years, <strong>which means</strong> they were already swimming in the oceans long before the first trees <span class="cn-word" data-pos="verb" data-tr="paydo boʻldi">appeared</span> on land.</p>
<p>To put this in <span class="cn-word" data-tr="nuqtai nazar">perspective</span>, trees are thought to have grown around 390 million years ago — some 60 million years after sharks. <strong>Despite</strong> surviving several mass <span class="cn-word" data-tr="qirilib ketishlar">extinctions</span> that <span class="cn-word" data-pos="verb" data-tr="yoʻq qildi">wiped out</span> countless other <span class="cn-word" data-tr="turlar">species</span>, sharks have changed remarkably little. Their ancient and highly <span class="cn-word" data-pos="adj" data-tr="samarali">efficient</span> design has allowed them to remain some of the ocean's most successful <span class="cn-word" data-tr="yirtqichlar">predators</span>.</p>''',
        "grammar": [
            {
                "pattern":  "which means (comment clause)",
                "meaning":  "Bu shuni anglatadiki — oldingi fikrdan xulosa chiqaradi.",
                "examples": ["Sharks are 450 million years old, which means they are older than trees.", "The shop is closed, which means we have to wait."],
            },
            {
                "pattern":  "despite + noun / -ing",
                "meaning":  "...ga qaramay (kutilgan natijaga zid holat).",
                "examples": ["Despite surviving many extinctions, sharks changed little.", "Despite the rain, they went out."],
            },
        ],
        "questions": [
            {
                "text": "Why are sharks described as ‘older than trees’?",
                "choices": [
                    "They existed about 450 million years ago, before the first trees (about 390 million years ago)",
                    "They live longer than any tree",
                    "They are found near very old trees",
                ],
                "answer": 0,
                "explanation": "Akulalar taxminan 450 million yil avval, daraxtlardan (taxminan 390 million yil) oldin paydo boʻlgan.",
            },
            {
                "text": "What have sharks survived over their long history?",
                "choices": [
                    "Several mass extinctions that wiped out many other species",
                    "The loss of all the world's oceans",
                    "Being hunted to near extinction by early humans",
                ],
                "answer": 0,
                "explanation": "Akulalar koʻplab boshqa turlarni yoʻq qilgan bir necha ommaviy qirilishlardan omon qolgan.",
            },
            {
                "text": "Why have sharks remained such successful predators?",
                "choices": [
                    "Their ancient, highly efficient design has changed very little",
                    "They keep growing much larger every century",
                    "They have no natural enemies at all",
                ],
                "answer": 0,
                "explanation": "Ularning qadimiy va juda samarali tuzilishi deyarli oʻzgarmagani uchun ular muvaffaqiyatli yirtqich boʻlib qolgan.",
            },
        ],
    },
    # ── 8 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Nose Can Smell a Trillion Scents",
        "summary": "Odam burni bir trillionga yaqin hidni farqlay oladi, deb taxmin qilinmoqda — va hid xotira bilan chambarchas bogʻliq.",
        "order":   8,
        "body": '''<p>For a long time, people believed that the human nose could <span class="cn-word" data-pos="verb" data-tr="farqlamoq">tell apart</span> only about 10,000 different smells. <strong>Recently, however</strong>, scientists have <span class="cn-word" data-pos="verb" data-tr="ilgari surdi, taklif qildi">suggested</span> that the true number may be closer to one trillion. In other words, our <span class="cn-word" data-tr="hissiyot, sezgi">sense</span> of smell is far more powerful than we once <span class="cn-word" data-pos="verb" data-tr="deb hisoblardik">assumed</span>.</p>
<p>Smell is also <span class="cn-word" data-pos="adv" data-tr="chuqur">deeply</span> <span class="cn-word" data-pos="adj" data-tr="bogʻliq">linked</span> to memory and <span class="cn-word" data-tr="hissiyot, tuygʻu">emotion</span>. A single <span class="cn-word" data-pos="adj" data-tr="tanish">familiar</span> <span class="cn-word" data-tr="hid">scent</span> — freshly baked bread, or the rain on a summer evening — can <span class="cn-word" data-pos="adv" data-tr="bir zumda">instantly</span> bring back a memory from years ago. <strong>This is because</strong> the part of the brain that <span class="cn-word" data-pos="verb" data-tr="qayta ishlaydi">processes</span> smell sits right next to the areas that <span class="cn-word" data-pos="verb" data-tr="boshqaradi">handle</span> memory and feeling. Our nose, it seems, is quietly connected to our past.</p>''',
        "grammar": [
            {
                "pattern":  "recently, however",
                "meaning":  "Biroq soʻnggi paytda / yaqinda esa (avvalgi qarash bilan zid yangi maʼlumot).",
                "examples": ["Recently, however, scientists have suggested a much bigger number.", "Recently, however, prices have started to fall."],
            },
            {
                "pattern":  "this is because ...",
                "meaning":  "Buning sababi shuki ... (sababni tushuntiradi).",
                "examples": ["This is because the smell area sits next to the memory area.", "This is because the roads were closed."],
            },
        ],
        "questions": [
            {
                "text": "What did people previously believe about the human nose?",
                "choices": [
                    "That it could tell apart only about 10,000 smells",
                    "That it could not smell anything at all",
                    "That it was stronger than a dog's nose",
                ],
                "answer": 0,
                "explanation": "Ilgari odamlar burun atigi 10 000 ga yaqin hidni farqlay oladi deb hisoblashgan.",
            },
            {
                "text": "What have scientists recently suggested?",
                "choices": [
                    "The nose may distinguish close to one trillion smells",
                    "The nose is losing its power over time",
                    "Only children can smell well",
                ],
                "answer": 0,
                "explanation": "Yaqinda olimlar burun bir trillionga yaqin hidni farqlay olishi mumkinligini taklif qilishgan.",
            },
            {
                "text": "Why can a single smell instantly bring back a memory?",
                "choices": [
                    "The brain's smell area sits right next to the areas for memory and emotion",
                    "Smells are stored in the nose forever",
                    "Every smell has a name we remember",
                ],
                "answer": 0,
                "explanation": "Miyaning hidni qayta ishlaydigan qismi xotira va hissiyotni boshqaradigan hududlar yonida joylashgani uchun.",
            },
        ],
    },
    # ── 9 ────────────────────────────────────────────────────────────────
    {
        "title":   "Sound Cannot Travel Through Space",
        "summary": "Tovush tarqalishi uchun havo yoki suv kabi muhit kerak; koinot deyarli vakuum boʻlgani uchun kosmos jimjit.",
        "order":   9,
        "body": '''<p>In science-fiction films, huge <span class="cn-word" data-tr="portlashlar">explosions</span> in space are usually <span class="cn-word" data-pos="verb" data-tr="hamroh boʻladi">accompanied</span> by a <span class="cn-word" data-pos="adj" data-tr="quloqni qomatga keltiradigan">deafening</span> <span class="cn-word" data-tr="gulduros">roar</span>. In reality, <strong>though</strong>, this could never happen, because space is completely <span class="cn-word" data-pos="adj" data-tr="jimjit">silent</span>. Sound simply cannot travel through the <span class="cn-word" data-tr="boʻshliq">emptiness</span> between the stars.</p>
<p>The reason lies in how sound works. Sound moves as a <span class="cn-word" data-tr="tebranish">vibration</span> that passes from one <span class="cn-word" data-tr="zarra">particle</span> to another, which is why it needs a <span class="cn-word" data-tr="muhit">medium</span> such as air or water. <strong>Since</strong> space is a near-vacuum with almost no particles, there is nothing for the vibrations to move through. So if a star exploded far away, no matter how <span class="cn-word" data-pos="adj" data-tr="shiddatli, kuchli">violent</span> the <span class="cn-word" data-tr="portlash">blast</span>, it would reach us in perfect silence.</p>''',
        "grammar": [
            {
                "pattern":  "though (mid/end-sentence contrast)",
                "meaning":  "Ammo, shunga qaramay — gap oʻrtasida yoki oxirida keluvchi ‘but’ maʼnosi.",
                "examples": ["In reality, though, this could never happen.", "It's cold today. It's sunny, though."],
            },
            {
                "pattern":  "since (reason)",
                "meaning":  "...ligi sababli, chunki (maʼlum sababni bildiradi).",
                "examples": ["Since space has almost no particles, sound cannot travel.", "Since it was late, we took a taxi."],
            },
        ],
        "questions": [
            {
                "text": "Why are explosions in space actually silent?",
                "choices": [
                    "Space is a near-vacuum, and sound cannot travel without a medium",
                    "Explosions in space are too far to hear",
                    "Sound in space is too high for humans to hear",
                ],
                "answer": 0,
                "explanation": "Koinot deyarli vakuum; muhitsiz tovush tarqala olmaydi, shuning uchun kosmos jimjit.",
            },
            {
                "text": "What does sound need in order to travel?",
                "choices": [
                    "A medium such as air or water, made of particles",
                    "Bright light",
                    "A very high temperature",
                ],
                "answer": 0,
                "explanation": "Tovush zarralardan iborat muhit (havo yoki suv) orqali tarqaladi.",
            },
            {
                "text": "What would happen if a distant star exploded?",
                "choices": [
                    "It would reach us in complete silence, no matter how violent",
                    "We would hear a loud roar a moment later",
                    "The sound would slowly fade in over hours",
                ],
                "answer": 0,
                "explanation": "Portlash qanchalik kuchli boʻlmasin, u bizga mutlaq sukunatda yetib keladi.",
            },
        ],
    },
    # ── 10 ───────────────────────────────────────────────────────────────
    {
        "title":   "The Sun Holds Almost All the Solar System",
        "summary": "Quyosh Quyosh sistemasi massasining qariyb 99.8 foizini oʻzida saqlaydi — qolgan hamma narsa atigi 0.2 foiz.",
        "order":   10,
        "body": '''<p>When we picture the solar system, we often imagine the Sun <span class="cn-word" data-pos="verb" data-tr="oʻralgan">surrounded</span> by eight important planets. <strong>In truth</strong>, however, the Sun is not just the centre — it is almost the <span class="cn-word" data-pos="adj" data-tr="butun">entire</span> system. The Sun alone <span class="cn-word" data-pos="verb" data-tr="oʻz ichiga oladi">contains</span> about 99.8 percent of all the <span class="cn-word" data-tr="massa">mass</span> in the solar system.</p>
<p>That leaves a <span class="cn-word" data-pos="adj" data-tr="atigi, boru-yoʻgʻi">mere</span> 0.2 percent for everything else: the planets, their moons, and <span class="cn-word" data-pos="adj" data-tr="son-sanoqsiz">countless</span> <span class="cn-word" data-tr="asteroidlar">asteroids</span> and <span class="cn-word" data-tr="kometalar">comets</span>. Most of that is taken up by the giant planet Jupiter, <strong>while</strong> tiny worlds like Earth <span class="cn-word" data-pos="verb" data-tr="tashkil qiladi">account for</span> only a <span class="cn-word" data-tr="juda kichik ulush">sliver</span>. It is a <span class="cn-word" data-pos="adj" data-tr="kishini kamtar qiladigan">humbling</span> thought: everything we know and everyone who has ever lived exists within that thin slice of <span class="cn-word" data-pos="adj" data-tr="ortib qolgan">leftover</span> material.</p>''',
        "grammar": [
            {
                "pattern":  "in truth (however)",
                "meaning":  "Aslida, haqiqatda esa (koʻrinishga zid haqiqatni taʼkidlaydi).",
                "examples": ["In truth, however, the Sun is almost the entire system.", "He seemed calm; in truth, he was worried."],
            },
            {
                "pattern":  "while (contrast)",
                "meaning":  "..., holbuki / ... esa (ikki narsani qarama-qarshi qoʻyadi).",
                "examples": ["Jupiter takes most of it, while Earth is only a sliver.", "Some people love winter, while others hate it."],
            },
        ],
        "questions": [
            {
                "text": "What percentage of the solar system's mass is held by the Sun?",
                "choices": ["About 50 percent", "About 99.8 percent", "About 25 percent"],
                "answer": 1,
                "explanation": "Quyosh Quyosh sistemasi massasining qariyb 99.8 foizini oʻzida saqlaydi.",
            },
            {
                "text": "What makes up most of the remaining 0.2 percent?",
                "choices": ["The giant planet Jupiter", "The planet Earth", "The Moon"],
                "answer": 0,
                "explanation": "Qolgan 0.2 foizning koʻp qismini ulkan Yupiter sayyorasi tashkil qiladi.",
            },
            {
                "text": "What is the ‘humbling thought’ at the end of the text?",
                "choices": [
                    "Everything we know exists within a thin slice of leftover material",
                    "Humans will one day leave the solar system",
                    "The Sun will soon run out of energy",
                ],
                "answer": 0,
                "explanation": "Biz biladigan hamma narsa va yashagan har bir inson shu ortib qolgan yupqa qatlam ichida mavjud — bu kishini kamtar qiladigan fikr.",
            },
        ],
    },
]
