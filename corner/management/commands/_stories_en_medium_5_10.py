# English "Wonder" Readings — MEDIUM level, stories 5-10 (brings Medium Reads to a pack of 10).
# Grammar pattern shown in BOLD (<strong>) where it appears in the story; vocab marks kept off
# the bolded words. Story text = English; vocab/grammar/explanations in Uzbek. ~9-11 marks each.
# Import: python manage.py import_corner corner/management/commands/_stories_en_medium_5_10.py --author=<AUTHOR>

SUBJECT = {
    "name":    "English",
    "summary": "Ingliz tili: IELTS uslubidagi qiziqarli oʻqish matnlari — lugʻat va grammatika bilan.",
    "icon":    "bi-globe2",
    "color":   "#2563eb",
    "order":   2,
}

COLLECTION = {
    "title":       "Medium Reads",
    "description": "Oʻrta daraja (B1-B2) — biroz murakkabroq lugʻat va jumlalar.",
    "order":       2,
}

STORIES = [
    # ── 5 ────────────────────────────────────────────────────────────────
    {
        "title":   "Bananas Don't Grow on Trees",
        "summary": "Banan ‘daraxti’ aslida daraxt emas — yogʻoch poyasi yoʻq, u dunyodagi eng katta ‘oʻt’.",
        "order":   5,
        "body": '''<p>Most of us believe that bananas grow on trees, but in fact the banana ‘tree’ is not a real tree at all. A true tree has a hard, <span class="cn-word" data-pos="adj" data-tr="yogʻochsimon">woody</span> <span class="cn-word" data-tr="tana, poya">trunk</span>, <strong>whereas</strong> the banana plant has a <span class="cn-word" data-pos="adj" data-tr="yumshoq">soft</span> <span class="cn-word" data-tr="poya">stem</span> made <span class="cn-word" data-pos="adv" data-tr="asosan">mostly</span> of water. In other words, the banana is really a fruit that grows on the largest ‘grass’ in the world.</p>
<p>There is another surprising fact. Bananas hang <span class="cn-word" data-pos="adv" data-tr="pastga">downwards</span>, <strong>yet</strong> as they grow, they <span class="cn-word" data-pos="verb" data-tr="egiladi">curve</span> upwards towards the <span class="cn-word" data-tr="quyosh nuri">sunlight</span>. This is why bananas have their famous curved <span class="cn-word" data-tr="shakl">shape</span>. Even the <span class="cn-word" data-pos="adj" data-tr="oddiy">ordinary</span> banana you eat every day <span class="cn-word" data-pos="verb" data-tr="yashiradi">hides</span> an interesting story.</p>''',
        "grammar": [
            {
                "pattern":  "whereas (contrast)",
                "meaning":  "Holbuki, ...ning aksicha (ikki narsani qarama-qarshi qoʻyadi).",
                "examples": ["A real tree has a woody trunk, whereas a banana plant has a soft stem.", "He is quiet, whereas his brother is loud."],
            },
            {
                "pattern":  "yet (but, however)",
                "meaning":  "Ammo, shunga qaramay (kutilmagan qarama-qarshilik).",
                "examples": ["Bananas hang down, yet they curve upwards as they grow.", "It was cold, yet she wore no coat."],
            },
        ],
        "questions": [
            {
                "text": "Why is the banana ‘tree’ not a real tree?",
                "choices": [
                    "It has a soft stem, not a hard woody trunk",
                    "It is too short to be a tree",
                    "It does not produce fruit",
                ],
                "answer": 0,
                "explanation": "Banan oʻsimligida qattiq yogʻoch poya emas, asosan suvdan iborat yumshoq poya boʻladi.",
            },
            {
                "text": "How do bananas get their famous curved shape?",
                "choices": [
                    "They curve upwards towards the sunlight as they grow",
                    "Farmers bend them by hand",
                    "They grow inside a curved shell",
                ],
                "answer": 0,
                "explanation": "Bananlar oʻsayotganda quyosh nuriga qarab yuqoriga egilib oʻsadi, shu sabab egri shaklga ega boʻladi.",
            },
            {
                "text": "What is the banana really, according to the text?",
                "choices": [
                    "A vegetable that grows underground",
                    "A fruit that grows on a giant ‘grass’",
                    "The seed of a large tree",
                ],
                "answer": 1,
                "explanation": "Matnda banan dunyodagi eng katta ‘oʻt’da oʻsadigan meva ekani aytilgan.",
            },
        ],
    },
    # ── 6 ────────────────────────────────────────────────────────────────
    {
        "title":   "How Trees Talk to Each Other",
        "summary": "Oʻrmondagi daraxtlar ildizlari orqali bogʻlangan — ozuqani boʻlishadi va xavf haqida bir-birini ogohlantiradi.",
        "order":   6,
        "body": '''<p>The trees in a forest may look as if they are standing <span class="cn-word" data-pos="adv" data-tr="jimgina">silently</span> on their own, <strong>but in reality</strong> they are <span class="cn-word" data-pos="verb" data-tr="bogʻlangan">connected</span> under the ground. Through their <span class="cn-word" data-tr="ildizlar">roots</span> and tiny <span class="cn-word" data-tr="qoʻziqorinlar">fungi</span>, trees can <span class="cn-word" data-pos="verb" data-tr="boʻlishmoq">share</span> food and even send messages, almost as if they were having a <span class="cn-word" data-tr="suhbat">conversation</span>.</p>
<p>For example, a healthy tree can pass <span class="cn-word" data-tr="oziq moddalar">nutrients</span> to a <span class="cn-word" data-pos="adj" data-tr="zaifroq">weaker</span> tree nearby. <strong>Moreover</strong>, when insects <span class="cn-word" data-pos="verb" data-tr="hujum qiladi">attack</span>, a tree can send <span class="cn-word" data-tr="ogohlantiruvchi">warning</span> signals to other trees so that they can <span class="cn-word" data-pos="verb" data-tr="himoya qilmoq">protect</span> themselves. In this way, a forest works like one large family in which every member helps the others.</p>''',
        "grammar": [
            {
                "pattern":  "but in reality",
                "meaning":  "Ammo aslida (tashqi koʻrinishga zid haqiqatni aytadi).",
                "examples": ["They look separate, but in reality they are connected.", "He seems calm, but in reality he is nervous."],
            },
            {
                "pattern":  "moreover",
                "meaning":  "Bundan tashqari, qolaversa (qoʻshimcha maʼlumot qoʻshadi).",
                "examples": ["Moreover, trees can warn each other of danger.", "The hotel was cheap. Moreover, it was clean."],
            },
        ],
        "questions": [
            {
                "text": "How are the trees in a forest connected?",
                "choices": [
                    "Through their roots and tiny fungi under the ground",
                    "Through their leaves touching in the wind",
                    "They are not connected at all",
                ],
                "answer": 0,
                "explanation": "Daraxtlar yer ostida ildizlari va mayda qoʻziqorinlar orqali bir-biriga bogʻlangan.",
            },
            {
                "text": "What does a healthy tree do for a weaker tree nearby?",
                "choices": ["It gives it more sunlight", "It passes nutrients to it", "It moves closer to it"],
                "answer": 1,
                "explanation": "Sogʻlom daraxt yaqinidagi zaif daraxtga oziq moddalarni uzatadi.",
            },
            {
                "text": "What does a tree do when insects attack?",
                "choices": [
                    "It sends warning signals to other trees",
                    "It falls down on purpose",
                    "It grows new leaves at once",
                ],
                "answer": 0,
                "explanation": "Hasharotlar hujum qilganda daraxt boshqa daraxtlarga ogohlantiruvchi signal yuboradi.",
            },
        ],
    },
    # ── 7 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Day Is Getting Longer",
        "summary": "Oyning tortishishi Yerning aylanishini sekinlashtiradi — shu sabab har bir kun juda oz miqdorda uzayib bormoqda.",
        "order":   7,
        "body": '''<p>Is a day always exactly 24 hours long? In fact, the Earth's day is very slowly getting longer, and the <span class="cn-word" data-tr="sabab">cause</span> is the Moon. The Moon's <span class="cn-word" data-tr="tortishish kuchi">gravity</span> <span class="cn-word" data-pos="verb" data-tr="tortadi">pulls</span> on the oceans and creates the <span class="cn-word" data-tr="qalqish-qaytish">tides</span>. <strong>As a result</strong>, it very <span class="cn-word" data-pos="adv" data-tr="ohista">gently</span> <span class="cn-word" data-pos="verb" data-tr="sekinlashtiradi">slows down</span> the speed at which the Earth spins.</p>
<p>The change is tiny — about 1.7 milliseconds every hundred years — so it is far too small to <span class="cn-word" data-pos="verb" data-tr="sezmoq">notice</span> in a lifetime. However, over a very long time it <span class="cn-word" data-pos="verb" data-tr="toʻplanib boradi">adds up</span>. <strong>When</strong> <span class="cn-word" data-tr="dinozavrlar">dinosaurs</span> lived on Earth, a day was only about 23 hours long. Even at this very moment, our day is quietly growing a little longer.</p>''',
        "grammar": [
            {
                "pattern":  "as a result",
                "meaning":  "Natijada, shuning oqibatida (oqibatni bogʻlaydi).",
                "examples": ["The Moon pulls the oceans; as a result, the Earth spins slower.", "He didn't study. As a result, he failed."],
            },
            {
                "pattern":  "when + clause (past time)",
                "meaning":  "...ganda, ... vaqtida (oʻtmishdagi davrni koʻrsatadi).",
                "examples": ["When dinosaurs lived, a day was about 23 hours.", "When I was young, I lived in a village."],
            },
        ],
        "questions": [
            {
                "text": "Why is the Earth's day slowly getting longer?",
                "choices": [
                    "The Sun is pulling the Earth closer",
                    "The Moon's gravity slows the Earth's spin through the tides",
                    "The Earth is getting heavier",
                ],
                "answer": 1,
                "explanation": "Oyning tortishish kuchi qalqish-qaytish orqali Yerning aylanishini sekinlashtiradi.",
            },
            {
                "text": "Why don't we notice this change?",
                "choices": [
                    "It only happens at night",
                    "It is far too small to notice in a lifetime",
                    "Clocks hide it from us",
                ],
                "answer": 1,
                "explanation": "Oʻzgarish (100 yilda 1.7 millisekund) shunchalik kichikki, uni bir umr davomida sezib boʻlmaydi.",
            },
            {
                "text": "How long was a day when dinosaurs lived on Earth?",
                "choices": ["About 23 hours", "Exactly 24 hours", "About 30 hours"],
                "answer": 0,
                "explanation": "Matnda dinozavrlar davrida Yer kuni taxminan 23 soat boʻlgani aytilgan.",
            },
        ],
    },
    # ── 8 ────────────────────────────────────────────────────────────────
    {
        "title":   "Spider Silk: Stronger Than Steel",
        "summary": "Vazniga nisbatan oʻrgimchak toʻri poʻlatdan mustahkam va choʻziluvchan — olimlar uni nusxalashga urinmoqda.",
        "order":   8,
        "body": '''<p>Spider <span class="cn-word" data-tr="ipak, tola">silk</span> looks thin and <span class="cn-word" data-pos="adj" data-tr="nozik">delicate</span>, but it is one of the strongest <span class="cn-word" data-tr="materiallar">materials</span> in nature. Weight for weight, spider silk is actually stronger than <span class="cn-word" data-tr="poʻlat">steel</span>, and at the same time it can <span class="cn-word" data-pos="verb" data-tr="choʻzilmoq">stretch</span> without breaking. <strong>Because of</strong> these amazing <span class="cn-word" data-tr="xususiyatlar">qualities</span>, scientists have studied spider silk for many years.</p>
<p>Some <span class="cn-word" data-tr="mutaxassislar">experts</span> say that <strong>if</strong> a <span class="cn-word" data-tr="tola">strand</span> of spider silk were as thick as a pencil, it could stop a flying <span class="cn-word" data-tr="samolyot">aeroplane</span>. Of course, that is only in <span class="cn-word" data-tr="nazariya">theory</span>. Still, <span class="cn-word" data-tr="muhandislar">engineers</span> hope to create new materials — from stronger ropes to safer clothing — by copying the secret of the spider.</p>''',
        "grammar": [
            {
                "pattern":  "because of + noun",
                "meaning":  "... tufayli, ... sababli (otdan oldin keladi).",
                "examples": ["Because of these qualities, scientists study spider silk.", "The flight was delayed because of the fog."],
            },
            {
                "pattern":  "if + past, could + verb (second conditional)",
                "meaning":  "Faraziy shart: agar ...sa edi, ... boʻlishi mumkin edi (haqiqatga zid taxmin).",
                "examples": ["If a strand were as thick as a pencil, it could stop a plane.", "If I had wings, I could fly."],
            },
        ],
        "questions": [
            {
                "text": "How strong is spider silk compared to steel?",
                "choices": [
                    "Much weaker than steel",
                    "Weight for weight, stronger than steel",
                    "Exactly the same as steel",
                ],
                "answer": 1,
                "explanation": "Bir xil vaznda olganda oʻrgimchak toʻri poʻlatdan mustahkamroq boʻladi.",
            },
            {
                "text": "What could a pencil-thick strand of spider silk do, in theory?",
                "choices": ["Lift a house", "Stop a flying aeroplane", "Cut through steel"],
                "answer": 1,
                "explanation": "Mutaxassislarning aytishicha, qalam yoʻgʻonligidagi tola nazariy jihatdan uchayotgan samolyotni toʻxtata olardi.",
            },
            {
                "text": "Why do scientists and engineers study spider silk?",
                "choices": [
                    "To copy it and create new, stronger materials",
                    "To sell it as expensive cloth",
                    "To keep spiders as pets",
                ],
                "answer": 0,
                "explanation": "Ular oʻrgimchak toʻrini nusxalab, arqondan tortib xavfsizroq kiyimgacha yangi mustahkam materiallar yaratishni umid qiladi.",
            },
        ],
    },
    # ── 9 ────────────────────────────────────────────────────────────────
    {
        "title":   "Bees Can Remember Faces",
        "summary": "Miyasi guruch donidan kichik boʻlsa-da, asalarilar inson yuzlarini oʻrganib, eslab qola oladi.",
        "order":   9,
        "body": '''<p>We usually think that only humans and a few <span class="cn-word" data-pos="adj" data-tr="aqlli">clever</span> animals can <span class="cn-word" data-pos="verb" data-tr="tanimoq">recognise</span> faces. <strong>Surprisingly</strong>, honeybees can do it too, even though their <span class="cn-word" data-tr="miya">brains</span> are smaller than a <span class="cn-word" data-tr="don">grain</span> of rice. In <span class="cn-word" data-tr="tajribalar">experiments</span>, bees learned to <span class="cn-word" data-pos="verb" data-tr="farqlamoq">tell</span> one human face from another in order to find a <span class="cn-word" data-tr="mukofot">reward</span> of sugar water.</p>
<p>How is this possible with such a tiny brain? Bees seem to <span class="cn-word" data-pos="verb" data-tr="birlashtirmoq">put together</span> different parts of a face, such as the eyes and mouth, <strong>just as</strong> people do. Scientists study this <span class="cn-word" data-tr="qobiliyat">ability</span> because it may help us understand how the brain recognises faces — a question that is still not <span class="cn-word" data-pos="adv" data-tr="toʻliq">fully</span> answered.</p>''',
        "grammar": [
            {
                "pattern":  "surprisingly (sentence adverb)",
                "meaning":  "Ajablanarlisi shundaki — butun gapga munosabat bildiradi.",
                "examples": ["Surprisingly, bees can recognise faces.", "Surprisingly, the test was quite easy."],
            },
            {
                "pattern":  "just as + clause",
                "meaning":  "Xuddi ...ganidek (oʻxshatish/qiyoslash).",
                "examples": ["Bees combine parts of a face just as people do.", "She sings just as her mother did."],
            },
        ],
        "questions": [
            {
                "text": "What surprising thing can honeybees do?",
                "choices": [
                    "Recognise and remember human faces",
                    "Speak simple words",
                    "Live for many years",
                ],
                "answer": 0,
                "explanation": "Kichik miyasiga qaramay, asalarilar inson yuzlarini tanib, eslab qola oladi.",
            },
            {
                "text": "How do bees seem to recognise a face?",
                "choices": [
                    "By smelling the person",
                    "By putting together parts such as the eyes and mouth",
                    "By listening to the person's voice",
                ],
                "answer": 1,
                "explanation": "Asalarilar xuddi odamlar kabi yuzning koʻz va ogʻiz kabi qismlarini birlashtirib tanigandek koʻrinadi.",
            },
            {
                "text": "Why do scientists study this ability of bees?",
                "choices": [
                    "It may help us understand how the brain recognises faces",
                    "It helps bees make more honey",
                    "It makes bees easier to catch",
                ],
                "answer": 0,
                "explanation": "Bu qobiliyat miya yuzlarni qanday tanishini tushunishga yordam berishi mumkin.",
            },
        ],
    },
    # ── 10 ───────────────────────────────────────────────────────────────
    {
        "title":   "Lightning Is Hotter Than the Sun",
        "summary": "Chaqmoq 30 000 darajagacha qiziydi — Quyosh yuzasidan taxminan besh barobar issiqroq.",
        "order":   10,
        "body": '''<p>When we think of the hottest things in nature, we usually <span class="cn-word" data-pos="verb" data-tr="tasavvur qilmoq">imagine</span> the Sun. <strong>However</strong>, a <span class="cn-word" data-tr="chaqmoq, yashin">bolt</span> of lightning can actually be far hotter. The <span class="cn-word" data-tr="yuza">surface</span> of the Sun is about 5,500 degrees, <strong>whereas</strong> a lightning bolt can reach around 30,000 degrees — <span class="cn-word" data-pos="adv" data-tr="taxminan">roughly</span> five times hotter.</p>
<p>Lightning <span class="cn-word" data-pos="verb" data-tr="qizdiradi">heats</span> the air around it so quickly that the air suddenly <span class="cn-word" data-pos="verb" data-tr="kengayadi">expands</span> and creates a <span class="cn-word" data-pos="adj" data-tr="baland (ovoz)">loud</span> sound. That sound is what we call <span class="cn-word" data-tr="momaqaldiroq">thunder</span>. So the next time you see a <span class="cn-word" data-tr="boʻron">storm</span>, remember that the <span class="cn-word" data-tr="chaqnash">flash</span> in the sky is, for a tiny moment, one of the hottest things on Earth.</p>''',
        "grammar": [
            {
                "pattern":  "however (contrast connector)",
                "meaning":  "Ammo, biroq (oldingi fikrga zid fikr kiritadi).",
                "examples": ["We imagine the Sun. However, lightning can be hotter.", "It was expensive. However, it was worth it."],
            },
            {
                "pattern":  "whereas (contrast)",
                "meaning":  "Holbuki, ...ning aksicha (ikki holatni qarshi qoʻyadi).",
                "examples": ["The Sun's surface is 5,500 degrees, whereas lightning reaches 30,000.", "I like tea, whereas she prefers coffee."],
            },
        ],
        "questions": [
            {
                "text": "How hot can a lightning bolt be?",
                "choices": [
                    "About 5,500 degrees, like the Sun's surface",
                    "Around 30,000 degrees, about five times hotter than the Sun's surface",
                    "Cooler than boiling water",
                ],
                "answer": 1,
                "explanation": "Chaqmoq taxminan 30 000 darajaga yetadi — Quyosh yuzasidan qariyb besh barobar issiqroq.",
            },
            {
                "text": "What causes thunder?",
                "choices": [
                    "Lightning heats the air so fast that it expands and makes a loud sound",
                    "Clouds crashing into each other",
                    "Rain hitting the ground",
                ],
                "answer": 0,
                "explanation": "Chaqmoq havoni shu qadar tez qizdiradiki, havo kengayib baland ovoz — momaqaldiroq hosil qiladi.",
            },
            {
                "text": "According to the text, which is hotter?",
                "choices": ["The surface of the Sun", "A lightning bolt", "They are exactly the same"],
                "answer": 1,
                "explanation": "Matnda chaqmoq Quyosh yuzasidan ancha issiqroq ekani aytilgan.",
            },
        ],
    },
]
