# English "Wonder" Readings — MEDIUM level (B1-B2). IELTS-style engaging short reads.
# Story text = English; vocab/grammar/explanations in Uzbek. ~10 vocab marks, 2 grammar
# points (useful IELTS structures), 3 inference questions per story.
# Import: python manage.py import_corner corner/management/commands/_stories_en_medium.py --author=<AUTHOR>

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
    # ── 1 ────────────────────────────────────────────────────────────────
    {
        "title":   "Why Is the Sea Salty?",
        "summary": "Daryolar toshdagi tuzni eritib dengizga olib boradi, suv bugʻlanadi-yu tuz qoladi — shu sabab dengiz shoʻr.",
        "order":   1,
        "body": '''<p>Have you ever <span class="cn-word" data-pos="verb" data-tr="oʻylab koʻrmoq, qiziqmoq">wondered</span> why <span class="cn-word" data-tr="dengiz suvi">seawater</span> tastes salty? The answer begins with rain. When rain falls on mountains and land, it flows into rivers. Along the way, the water <span class="cn-word" data-pos="verb" data-tr="eritadi">dissolves</span> tiny bits of salt that are hidden in rocks and <span class="cn-word" data-tr="tuproq">soil</span>. The rivers then <span class="cn-word" data-pos="verb" data-tr="olib boradi">carry</span> this salt all the way to the sea.</p>
<p>In the sea, the sun <strong>causes the water to</strong> <span class="cn-word" data-pos="verb" data-tr="bugʻlanadi">evaporate</span>, but the salt is left <span class="cn-word" data-pos="adv" data-tr="ortda, orqada">behind</span>. Only the water <span class="cn-word" data-pos="verb" data-tr="chiqib ketadi">escapes</span> into the air, while the salt <span class="cn-word" data-pos="verb" data-tr="toʻplanib boradi">builds up</span>. This <span class="cn-word" data-tr="jarayon">process</span> <strong>has been</strong> <span class="cn-word" data-pos="verb" data-tr="takrorlangan">repeated</span> for millions of years, and that is why the sea has become so salty. In fact, the ocean is still becoming a little saltier even today.</p>''',
        "grammar": [
            {
                "pattern":  "cause + something + to + verb",
                "meaning":  "Biror narsani ...ishiga sabab boʻlmoq / majbur qilmoq.",
                "examples": ["The sun causes the water to evaporate.", "The noise caused the baby to cry."],
            },
            {
                "pattern":  "has/have been + past participle (present perfect passive)",
                "meaning":  "...langan/qilingan — oʻtmishdan hozirgacha davom etgan majhul harakat.",
                "examples": ["This process has been repeated for millions of years.", "The bridge has been built."],
            },
        ],
        "questions": [
            {
                "text": "How does salt get from the land to the sea?",
                "choices": [
                    "Rain dissolves salt in rocks and soil, and rivers carry it to the sea",
                    "The wind blows salt from deserts into the sea",
                    "Fish carry salt into the sea",
                ],
                "answer": 0,
                "explanation": "Yomgʻir tosh va tuproqdagi tuzni eritadi, daryolar esa uni dengizga olib boradi.",
            },
            {
                "text": "Why does the sea keep getting saltier?",
                "choices": [
                    "Because both the water and the salt evaporate",
                    "Because water evaporates but the salt is left behind and builds up",
                    "Because rain adds new salt every day",
                ],
                "answer": 1,
                "explanation": "Quyosh taʼsirida suv bugʻlanadi, lekin tuz dengizda qolib toʻplanib boradi.",
            },
            {
                "text": "Which statement is true according to the text?",
                "choices": [
                    "The sea was saltier in the past than it is now",
                    "The sea is slowly becoming less salty",
                    "The ocean is still becoming slightly saltier today",
                ],
                "answer": 2,
                "explanation": "Matn oxirida okean hozir ham asta-sekin shoʻrroq boʻlib borayotgani aytilgan.",
            },
        ],
    },
    # ── 2 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Animal with Three Hearts",
        "summary": "Sakkizoyoqning uchta yuragi va koʻk qoni bor — suzganda asosiy yuragi toʻxtab, tez charchaydi.",
        "order":   2,
        "body": '''<p>The octopus is far more <span class="cn-word" data-pos="adj" data-tr="ajoyib, diqqatga sazovor">remarkable</span> than most people think. <span class="cn-word" data-pos="adv" data-tr="ajablanarlisi shundaki">Surprisingly</span>, it does not have one heart but three. Two of the hearts <span class="cn-word" data-pos="verb" data-tr="haydaydi">pump</span> blood to the <span class="cn-word" data-tr="jabralar">gills</span>, while the third pumps blood to the rest of the body. <span class="cn-word" data-pos="adv" data-tr="bundan tashqari">On top of that</span>, an octopus's blood is not red but blue.</p>
<p>The blue colour comes from what the blood <span class="cn-word" data-pos="verb" data-tr="tarkibida boʻladi">contains</span>. Human blood is red because of iron, but an octopus's blood contains <span class="cn-word" data-tr="mis">copper</span>, which makes it look blue. Here is the strangest part: when an octopus swims, the heart that pumps blood to its body <span class="cn-word" data-pos="verb" data-tr="toʻxtaydi">stops</span>. <strong>As a result</strong>, the octopus <span class="cn-word" data-pos="verb" data-tr="charchaydi">tires</span> quickly, so it <strong><span class="cn-word" data-pos="verb" data-tr="afzal koʻradi">prefers</span></strong> <span class="cn-word" data-pos="verb" data-tr="oʻrmalash">crawling</span> along the sea floor to swimming.</p>''',
        "grammar": [
            {
                "pattern":  "prefer A to B",
                "meaning":  "B ga qaraganda A ni afzal koʻrmoq. (Otlar yoki -ing shakli bilan.)",
                "examples": ["The octopus prefers crawling to swimming.", "I prefer tea to coffee."],
            },
            {
                "pattern":  "as a result",
                "meaning":  "Natijada, shuning oqibatida (oqibatni bogʻlaydi).",
                "examples": ["The heart stops; as a result, the octopus tires quickly.", "He didn't study. As a result, he failed."],
            },
        ],
        "questions": [
            {
                "text": "Why is an octopus's blood blue?",
                "choices": [
                    "Because it contains iron",
                    "Because it contains copper",
                    "Because it reflects the sea",
                ],
                "answer": 1,
                "explanation": "Odam qoni temir tufayli qizil, sakkizoyoq qonida esa mis boʻlgani uchun u koʻk koʻrinadi.",
            },
            {
                "text": "What happens when an octopus swims?",
                "choices": [
                    "All three of its hearts beat faster",
                    "The heart that pumps blood to its body stops",
                    "Its blood turns red",
                ],
                "answer": 1,
                "explanation": "Suzganda butun tanaga qon haydaydigan yurak toʻxtaydi.",
            },
            {
                "text": "Why does the octopus prefer crawling to swimming?",
                "choices": [
                    "Because it tires quickly when it swims",
                    "Because it cannot swim at all",
                    "Because the water is too cold",
                ],
                "answer": 0,
                "explanation": "Asosiy yuragi toʻxtagani uchun sakkizoyoq suzganda tez charchaydi, shuning uchun oʻrmalashni afzal koʻradi.",
            },
        ],
    },
    # ── 3 ────────────────────────────────────────────────────────────────
    {
        "title":   "The Far Side of the Moon",
        "summary": "Oy Yer atrofida aylanar ekan xuddi shu tezlikda oʻqi atrofida ham aylanadi — shu sabab bizga doim bir tomoni koʻrinadi.",
        "order":   3,
        "body": '''<p>When you look at the Moon at night, you always see the same face. The far side of the Moon can never be seen from Earth. Why is that?</p>
<p><strong>As the Moon</strong> <span class="cn-word" data-pos="verb" data-tr="aylanadi (atrofida)">orbits</span> the Earth, it also <span class="cn-word" data-pos="verb" data-tr="oʻz oʻqida aylanadi">spins</span> slowly on its own. Remarkably, the speed of its spin <span class="cn-word" data-pos="verb" data-tr="mos keladi">matches</span> the time it takes to go around the Earth <span class="cn-word" data-pos="adv" data-tr="aniq, xuddi">exactly</span>. As a result, the same side always <span class="cn-word" data-pos="verb" data-tr="qaraydi, yuz tutadi">faces</span> us. <strong>For this reason</strong>, people could not see the far side of the Moon for a very long time. When a <span class="cn-word" data-tr="kosmik kema">spacecraft</span> finally <span class="cn-word" data-pos="verb" data-tr="suratga oldi">photographed</span> it, the far side looked <span class="cn-word" data-pos="adv" data-tr="ancha, birmuncha">quite</span> different from the side we know.</p>''',
        "grammar": [
            {
                "pattern":  "as + subject + verb (while)",
                "meaning":  "...ayotganda, ... bilan bir vaqtda (bir vaqtdalik yoki sabab).",
                "examples": ["As the Moon orbits the Earth, it spins slowly.", "As I grew older, I understood more."],
            },
            {
                "pattern":  "for this reason",
                "meaning":  "Shu sababli, shuning uchun (sabab-natija bogʻlovchisi).",
                "examples": ["For this reason, we could not see the far side.", "It was raining; for this reason, we stayed home."],
            },
        ],
        "questions": [
            {
                "text": "Why do we always see the same side of the Moon?",
                "choices": [
                    "Because the Moon does not move at all",
                    "Because its spin exactly matches the time it takes to orbit the Earth",
                    "Because the Earth spins around the Moon",
                ],
                "answer": 1,
                "explanation": "Oyning oʻz oʻqida aylanish tezligi Yer atrofida aylanish vaqtiga aniq mos kelgani uchun doim bir tomoni koʻrinadi.",
            },
            {
                "text": "Why couldn't people see the far side for a long time?",
                "choices": [
                    "It can never be seen from Earth",
                    "It has no light at all",
                    "It is too small to see",
                ],
                "answer": 0,
                "explanation": "Oyning orqa tomoni Yerdan aslo koʻrinmaydi, shuning uchun uni uzoq vaqt koʻrishmagan.",
            },
            {
                "text": "What was the far side like when a spacecraft photographed it?",
                "choices": [
                    "Exactly the same as the near side",
                    "Quite different from the side we know",
                    "Completely covered in water",
                ],
                "answer": 1,
                "explanation": "Kosmik kema suratga olgan orqa tomon biz biladigan old tomondan ancha farq qilgan.",
            },
        ],
    },
    # ── 4 ────────────────────────────────────────────────────────────────
    {
        "title":   "When Salt Was Money",
        "summary": "Muzlatgich yoʻq davrda tuz oltinday qadrli edi — Rimda askarlarga maosh tuz bilan berilardi.",
        "order":   4,
        "body": '''<p>In the days before <span class="cn-word" data-tr="muzlatgichlar">refrigerators</span>, salt was an extremely <span class="cn-word" data-pos="adj" data-tr="qimmatbaho">valuable</span> thing. Salt allowed people to <span class="cn-word" data-pos="verb" data-tr="saqlab qolmoq">preserve</span> food <strong>so that it would not go bad</strong> for a long time. For this reason, people <span class="cn-word" data-pos="verb" data-tr="qadrlashardi, eʼzozlashardi">treasured</span> salt almost as much as gold.</p>
<p>In <span class="cn-word" data-pos="adj" data-tr="qadimgi">ancient</span> Rome, <span class="cn-word" data-tr="askarlar">soldiers</span> were sometimes <span class="cn-word" data-pos="verb" data-tr="toʻlanardi (maosh)">paid</span> in salt <strong>instead of coins</strong>. In fact, the English word 'salary' comes from the Latin word for salt. Today salt is cheap and <span class="cn-word" data-pos="adj" data-tr="keng tarqalgan">common</span>, and we <span class="cn-word" data-pos="adv" data-tr="deyarli ...emas">hardly</span> think about it. Yet long ago, it was a <span class="cn-word" data-tr="xazina, boylik">treasure</span> that was worth almost as much as money itself.</p>''',
        "grammar": [
            {
                "pattern":  "so that + clause",
                "meaning":  "...ishi uchun, shu maqsadda (maqsad/natija ergash gapi).",
                "examples": ["Salt preserved food so that it would last longer.", "Speak slowly so that everyone can understand."],
            },
            {
                "pattern":  "instead of + noun/-ing",
                "meaning":  "... oʻrniga (bir narsani boshqasiga almashtirish).",
                "examples": ["Soldiers were paid in salt instead of coins.", "Let's walk instead of driving."],
            },
        ],
        "questions": [
            {
                "text": "Why was salt so valuable long ago?",
                "choices": [
                    "Because it was very hard to find anywhere",
                    "Because it let people preserve food before refrigerators existed",
                    "Because only kings were allowed to eat it",
                ],
                "answer": 1,
                "explanation": "Muzlatgichlar boʻlmagan davrda ovqatni uzoq saqlashda tuz ishlatilgani uchun u qadrli edi.",
            },
            {
                "text": "How were Roman soldiers sometimes paid?",
                "choices": ["In gold jewellery", "In salt instead of coins", "In land"],
                "answer": 1,
                "explanation": "Qadimgi Rimda askarlarga baʼzan tanga oʻrniga tuz berilgan.",
            },
            {
                "text": "Where does the English word 'salary' come from?",
                "choices": ["A word meaning 'soldier'", "A word meaning 'gold'", "The Latin word for salt"],
                "answer": 2,
                "explanation": "‘salary’ soʻzi tuzni anglatuvchi lotincha soʻzdan kelib chiqqan.",
            },
        ],
    },
]
