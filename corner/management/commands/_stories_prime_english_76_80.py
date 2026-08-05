# -*- coding: utf-8 -*-
"""Prime English Readings — PE-76 … PE-80 (batch 16). The small words that betray you.

PE-76 dependent prepositions · PE-77 phrasal verbs (how they work) · PE-78 phrasal verbs
by topic · PE-79 expressions of quantity · PE-80 articles, the advanced cases.

Shapes (varied on purpose — batch 15 was five third-person village stories):
  76 — the village pump man who was brilliant at machines and ashamed of his handwriting,
       and the fifteen-year-old who wrote the manual without writing a word
  77 — a bakery night in 2018 when the oven, the van and the family all broke down, told
       by the baker's daughter
  78 — a LETTER from a brother in Seoul to his sister, and the twenty phrasal verbs a
       roommate wrote on the wall by the door
  79 — a 1993 shopping list found inside a cookbook, and the line at the bottom of it
  80 — a home-made telescope on a school roof in 1998, and the night the word `the`
       changed meaning

NARRATOR VOICE (see the toc's AUDIO section):
    76 en-US-GuyNeural   · 77 en-US-JennyNeural · 78 en-US-GuyNeural
    79 en-US-JennyNeural · 80 en-US-JennyNeural
(Batch 15 ran 3 male / 2 female, so this one flips to 2 male / 3 female.)
Generate one story at a time:
    python manage.py gen_corner_audio --collection="Prime English Readings" \
        --only 76 --voice en-US-GuyNeural

Cumulative rule: everything through PE-75 is free — all twelve tenses, the modals,
conditionals, the passive, reported speech, relative clauses, comparison, the causative,
determiners, question tags, possession. Each reading owns its own lesson's material and
keeps off the NEXT ones: 76 uses no phrasal verbs as a subject (77/78), 79 owns the
container words, 80 owns the advanced article cases. Nothing from Block G (PE-83+):
no emphatic `do`, no inversion, no cleft sentences (`What this town needs is…`), no
participle clauses, no unreal past, and no heavy linkers (however / therefore / moreover
are PE-88) — plain and / but / so / because carry the prose.
Length: 300–360 words. Vocabulary: 16–22 cn-word marks (the toc asks 16–26 from PE-67).

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_76_80.py --author=prime
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
    # PE-76 — dependent prepositions   (the pump house)            [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Afraid of, Good at, Depend on",
        "summary": (
            "PE-76 matni. Yigirma ikki yil davomida butun koʻcha "
            "bir kishiga — nasoschi Nodir akaga — bogʻliq edi. "
            "U mashinalarni mukammal bilardi, lekin bir narsadan "
            "qoʻrqardi. Oʻn besh yoshli qiz esa yechimni topdi."
        ),
        "order":   76,
        "grammar": [
            {
                "pattern":  "adjective + preposition — fixed pairs",
                "meaning":  "Sifat oʻz predlogi bilan birga "
                            "yodlanadi, mantiq izlab boʻlmaydi: "
                            "<b>good / bad / brilliant <i>at</i></b>, "
                            "<b>afraid / proud / ashamed <i>of</i></b>, "
                            "<b>worried <i>about</i></b>, "
                            "<b>different <i>from</i></b>. "
                            "Soʻzni alohida emas — juftlik holida "
                            "eslab qoling.",
                "examples": ["He was brilliant at machines.",
                             "He was ashamed of his handwriting.",
                             "The village was worried about the water."],
            },
            {
                "pattern":  "verb + preposition — listen to, depend on, laugh at",
                "meaning":  "Bir qancha feʼl doim oʻz predlogini "
                            "talab qiladi: <b>depend / rely <i>on</i></b>, "
                            "<b>listen <i>to</i></b>, "
                            "<b>laugh / look <i>at</i></b>, "
                            "<b>wait / ask <i>for</i></b>, "
                            "<b>apologise <i>for</i></b>. "
                            "Oʻzbekchada “musiqa tinglash” predlogsiz, "
                            "ingliz tilida esa <i>to</i> shart.",
                "examples": ["The whole street depended on him.",
                             "He would listen to the engine for a minute.",
                             "He was afraid of somebody laughing at it."],
            },
            {
                "pattern":  "the verbs that take NO preposition",
                "meaning":  "Eng koʻp uchraydigan xato: oʻzbekchada "
                            "kelishik qoʻshimchasi borligi uchun "
                            "ingliz tilida ham predlog qoʻshib "
                            "yuboriladi. <b>discuss</b>, <b>answer</b>, "
                            "<b>enter</b>, <b>phone</b>, <b>tell</b>, "
                            "<b>reach</b>, <b>marry</b> — predlogsiz "
                            "toʻgʻridan-toʻgʻri toʻldiruvchi oladi "
                            "(<i>discuss about</i> ✗, "
                            "<i>enter into the room</i> ✗).",
                "examples": ["He never discussed the problem with anyone.",
                             "He answered the question in four words.",
                             "Somebody phoned him at two in the morning."],
            },
        ],
        "body": '''<p>Nodir aka could not read a page without his finger under the line, and he was <strong>afraid of</strong> talking to more than three people at once. Everybody in the village knew both of these things about him, and nobody cared, because for twenty-two years the whole street <strong>depended on</strong> him for its water.</p>

<p>The <span class="cn-word" data-tr="nasos">pump</span> house stood at the bottom of the road: a low brick building with a green door, an <span class="cn-word" data-tr="dvigatel, motor">engine</span> from 1981 inside it, and nothing written on any wall.</p>

<p>He was <strong>brilliant at</strong> machines and <strong>bad at</strong> explaining them. When the engine made a new sound at two in the morning, he would get out of bed, walk down the road and <strong>listen to</strong> it for a minute, and he would know which part was tired. He never <strong>discussed the problem</strong> with anybody. He opened the engine and <span class="cn-word" data-pos="verb" data-tr="taʼmirlamoq">mended</span> it.</p>

<p>In March 2016 he fell off a <span class="cn-word" data-tr="narvon">ladder</span> and broke his right arm in two places.</p>

<p>That was the week the village found out what it had really been <span class="cn-word" data-pos="verb" data-tr="tayanmoq">relying</span> on. Nobody else knew the order of the <span class="cn-word" data-tr="joʻmrak, kran">valves</span>, or which of the two <span class="cn-word" data-tr="tasma, kamar">belts</span> had to be changed first. The pump ran for four days and stopped, and three hundred houses carried water in <span class="cn-word" data-tr="chelak">buckets</span> for a <span class="cn-word" data-tr="ikki hafta">fortnight</span>.</p>

<p>When his arm came out of the <span class="cn-word" data-tr="gips">plaster</span>, somebody at the mahalla meeting asked him why he had never written any of it down.</p>

<p>He was quiet for a long time. Then he <strong>answered the question</strong> <span class="cn-word" data-pos="adv" data-tr="rostini aytib">honestly</span>, and it cost him something to do it: he was <strong>ashamed of</strong> his <span class="cn-word" data-tr="qoʻl yozuvi">handwriting</span>, and he had been <strong>afraid of</strong> a young man <strong>laughing at</strong> it.</p>

<p>The answer came from his neighbour's daughter. Dilnoza was fifteen and <strong>good at</strong> drawing, and she was not <strong>interested in</strong> anybody's handwriting.</p>

<p>For three weeks she sat on a wooden box in the pump house with a pencil and a <span class="cn-word" data-tr="varaq qogʻoz">sheet of paper</span> on her knees. She asked him to do everything slowly, twice. She drew the engine from the front and from above. She drew every <span class="cn-word" data-tr="ehtiyot qism">spare part</span> and numbered it, and she drew <span class="cn-word" data-tr="strelka, koʻrsatkich">arrows</span> where his hands went. She did not write one sentence in the whole book.</p>

<p>Twenty-nine pages of it hang on the pump-house wall now, behind glass, and two young men who <strong>look after</strong> the engine today learned the whole machine from those pages.</p>

<p>Nodir aka is sixty-one. He is still <strong>afraid of</strong> <span class="cn-word" data-tr="olomon">crowds</span> and still says he is <strong>bad at</strong> explaining things. He is wrong, and the wall <span class="cn-word" data-pos="verb" data-tr="isbotlamoq">proves</span> it. He explained the engine perfectly. He was just waiting for somebody who was not <strong>afraid of</strong> a pencil.</p>''',
        "questions": [
            {
                "text": "Why had Nodir aka never written instructions for the pump?",
                "choices": [
                    "He did not know how the engine worked",
                    "He was ashamed of his handwriting and afraid of being laughed at",
                    "The mahalla had told him not to",
                ],
                "answer": 1,
                "explanation": "U mashinani mukammal bilardi — muammo "
                               "bilimda emas edi. U qoʻl yozmasidan "
                               "uyalar va yosh yigit ustidan kulishidan "
                               "qoʻrqardi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "He never discussed about the problem with anybody.",
                    "He never discussed the problem with anybody.",
                    "He never discussed on the problem with anybody.",
                ],
                "answer": 1,
                "explanation": "<b>discuss</b> predlog olmaydi — "
                               "toʻldiruvchi toʻgʻridan-toʻgʻri keladi. "
                               "Xuddi shunday: <i>answer the question</i>, "
                               "<i>enter the room</i>, <i>phone me</i>.",
            },
            {
                "text": "Which pair of prepositions correctly completes: 'She was good ___ drawing, and he was afraid ___ crowds.'",
                "choices": [
                    "at … of",
                    "in … from",
                    "on … about",
                ],
                "answer": 0,
                "explanation": "<b>good <i>at</i></b> va "
                               "<b>afraid <i>of</i></b> — qatʼiy "
                               "juftliklar. Bu juftliklarni bir "
                               "butun soʻz kabi yodlash kerak.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-77 — phrasal verbs, how they work   (the bakery)        [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Day Everything Broke Down",
        "summary": (
            "PE-77 matni. Toʻygacha olti soat qoldi, uch yuz non "
            "kerak — va oʻsha kechada pech ham, mashina ham "
            "ishdan chiqdi. Yordam esa uch yildan beri gaplashmagan "
            "qoʻshnining eshigidan keldi."
        ),
        "order":   77,
        "grammar": [
            {
                "pattern":  "phrasal verb = verb + particle, new meaning",
                "meaning":  "Feʼl + kichik soʻz = <b>butunlay yangi "
                            "maʼno</b>, soʻzma-soʻz tarjima qilinmaydi. "
                            "<i>break</i> — sindirmoq, lekin "
                            "<b>break down</b> — ishdan chiqmoq; "
                            "<b>turn up</b> — kutilmaganda kelib "
                            "qolmoq; <b>make up</b> — yarashmoq. "
                            "Ularni yangi soʻz sifatida yodlang.",
                "examples": ["The oven broke down at ten o'clock.",
                             "He turned up at midnight.",
                             "They made up after three years."],
            },
            {
                "pattern":  "the pronoun rule — Take them out ✓ / Take out them ✗",
                "meaning":  "Ajraladigan (separable) frazali feʼlda "
                            "olmosh — <b>it, them, him, her, me, you</b> "
                            "— <b>doim oʻrtada</b> turadi: "
                            "<i>Take <b>them</b> out</i> ✓, "
                            "<i>Take out them</i> ✗. Ot boʻlsa ikki xil "
                            "ham boʻladi: <i>Take the trays out</i> = "
                            "<i>Take out the trays</i>.",
                "examples": ["Take them out now!",
                             "Turn it off before it burns.",
                             "He picked us up at five in the morning."],
            },
            {
                "pattern":  "inseparable ones never split",
                "meaning":  "Agar kichik soʻz haqiqiy predlog boʻlsa "
                            "(<i>for, after, with, to</i>) — feʼl "
                            "ajralmaydi: <b>look for</b>, "
                            "<b>look after</b>, <b>deal with</b>. "
                            "Uch soʻzlilar ham hech qachon "
                            "ajralmaydi: <b>run out of</b>, "
                            "<b>put up with</b>.",
                "examples": ["We were looking for the second key.",
                             "We had run out of flour by midnight.",
                             "She put up with all of it without one word."],
            },
        ],
        "body": '''<p>My father has been a baker since 1996, and he says a bakery only teaches you one lesson, but it teaches it about twice a year: everything breaks at once, or nothing breaks at all.</p>

<p>On the fourteenth of September 2018 we had an <span class="cn-word" data-tr="buyurtma">order</span> for three hundred <span class="cn-word" data-tr="non (bir dona)">loaves</span>. A wedding in the next street, six hundred <span class="cn-word" data-tr="mehmonlar">guests</span>, bread on the tables by seven in the morning.</p>

<p>The big <span class="cn-word" data-tr="pech">oven</span> <strong>broke down</strong> at ten o'clock that night, with the first ninety loaves inside it.</p>

<p>"<strong>Take them out</strong>," my father said. "All of them. Now."</p>

<p>We <strong>took them out</strong> and put them on the cold <span class="cn-word" data-tr="tovoq, laganda">trays</span> by the window, and my brother went to <strong>bring the van round</strong> so we could drive the <span class="cn-word" data-tr="xamir">dough</span> to the bakery in Yangiobod. The van <strong>broke down</strong> at the end of our own street. At half past eleven we <strong>ran out of</strong> gas as well, and at midnight my mother sat down on a chair in the middle of the floor and laughed, because there was nothing left to do about any of it.</p>

<p>That was when somebody <strong>turned up</strong> at the back door.</p>

<p>It was Rahim aka from number nine. We had <strong>fallen out with</strong> his family in 2015 over a metre and a half of <span class="cn-word" data-tr="hovli">yard</span>, and my father had not spoken to him since. He stood in the <span class="cn-word" data-tr="eshik ogʻzi">doorway</span> in his coat and said one sentence: "My oven is <span class="cn-word" data-pos="adj" data-tr="boʻsh">empty</span> until five."</p>

<p>We carried dough down the street in <span class="cn-word" data-tr="tog'ora, tos">basins</span>, forty kilos at a time. Rahim aka <strong>turned</strong> his oven <strong>on</strong> at ten past one. My father <strong>looked after</strong> the fire and never once <strong>looked at</strong> Rahim aka's face, and Rahim aka <strong>put up with</strong> that for four hours without one word about it.</p>

<p>The bread <strong>went out</strong> at ten past six. Three hundred and four loaves, because my mother <span class="cn-word" data-pos="verb" data-tr="hisoblab chiqmoq">worked out</span> that we would <span class="cn-word" data-pos="verb" data-tr="hisoblash">count</span> wrong somewhere and made four <span class="cn-word" data-pos="adj" data-tr="ortiqcha, zaxira">extra</span>.</p>

<p>The two men did not <span class="cn-word" data-pos="verb" data-tr="uzr soʻramoq">apologise</span> to each other. They did not <strong>make up</strong> with words at all. They <strong>made up</strong> with three hundred loaves of bread, and the metre and a half of yard has never been <span class="cn-word" data-pos="verb" data-tr="tilga olmoq">mentioned</span> again by anybody in either house.</p>''',
        "questions": [
            {
                "text": "How did the two families end their argument?",
                "choices": [
                    "Rahim aka apologised at the back door",
                    "Neither man spoke about it — they worked the night together instead",
                    "The father gave him the metre and a half of yard",
                ],
                "answer": 1,
                "explanation": "Hech kim uzr soʻramadi. Ular soʻz bilan "
                               "emas, birga ishlagan tun bilan yarashdi — "
                               "hikoyaning oxirgi jumlasi shuni aytadi.",
            },
            {
                "text": "Which sentence is correct English?",
                "choices": [
                    "Take out them now!",
                    "Take them out now!",
                    "Take them now out!",
                ],
                "answer": 1,
                "explanation": "Ajraladigan frazali feʼlda olmosh "
                               "(<i>them</i>) <b>doim oʻrtada</b> turadi. "
                               "<i>Take out them</i> ✗. Ot bilan esa "
                               "ikkala tartib ham toʻgʻri: "
                               "<i>Take the loaves out</i> / "
                               "<i>Take out the loaves</i>.",
            },
            {
                "text": "In the story, 'the van broke down' means that the van…",
                "choices": [
                    "stopped working",
                    "was broken into pieces by somebody",
                    "drove down the street",
                ],
                "answer": 0,
                "explanation": "<b>break down</b> — ishdan chiqmoq, "
                               "yurmay qolmoq. Frazali feʼlni soʻzma-soʻz "
                               "tarjima qilib boʻlmaydi: <i>break</i> + "
                               "<i>down</i> yangi maʼno beradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-78 — phrasal verbs by topic   (the letter from Seoul)     [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Getting Up, Getting Along, Getting By",
        "summary": (
            "PE-78 matni. Seuldagi akaning singlisiga yozgan xati: "
            "kunning tartibi, zavod, va uchinchi oyda uyga qaytmoqchi "
            "boʻlgani. Uni saqlab qolgan narsa — eshik yonidagi "
            "devorga yozilgan yigirmata frazali feʼl."
        ),
        "order":   78,
        "grammar": [
            {
                "pattern":  "phrasal verbs of the daily routine",
                "meaning":  "Kunlik tartib deyarli butunlay frazali "
                            "feʼllardan iborat: <b>wake up</b> "
                            "(uygʻonmoq), <b>get up</b> (oʻrnidan "
                            "turmoq), <b>put on</b> (kiymoq), "
                            "<b>set off</b> (yoʻlga chiqmoq), "
                            "<b>get on / get off</b> (chiqmoq / "
                            "tushmoq), <b>go to bed</b>.",
                "examples": ["I wake up at ten to five.",
                             "I put on the grey jacket and set off.",
                             "I get on the second bus at half past five."],
            },
            {
                "pattern":  "phrasal verbs about people",
                "meaning":  "Odamlar haqidagi guruh: "
                            "<b>get on with</b> (chiqishmoq), "
                            "<b>fall out with</b> (urishib qolmoq), "
                            "<b>make up</b> (yarashmoq), "
                            "<b>put up with</b> (chidamoq), "
                            "<b>look after</b> (qaramoq), "
                            "<b>take after</b> (oʻxshamoq). "
                            "Diqqat: <b>take after</b> “keyin olmoq” "
                            "emas, <i>oʻxshamoq</i> degani.",
                "examples": ["I get on well with everybody on my floor.",
                             "You take after our mother, not our father.",
                             "He looked after me for a whole month."],
            },
            {
                "pattern":  "get by, give up, find out — the ones that decide things",
                "meaning":  "<b>get by</b> — zoʻrgʻa boʻlsa ham "
                            "uddalamoq, kun koʻrmoq; "
                            "<b>give up</b> — tashlab qoʻymoq, "
                            "voz kechmoq; <b>find out</b> — bilib "
                            "olmoq; <b>work out</b> — hisoblab yoki "
                            "oʻylab topmoq; <b>catch up with</b> — "
                            "yetib olmoq.",
                "examples": ["By the sixth month I could get by.",
                             "In the third month I nearly gave up.",
                             "I found out what the job really was."],
            },
        ],
        "body": '''<p>Dilnoza,</p>

<p>You asked me what a day here is actually like, so here is one, from the beginning.</p>

<p>I <strong>wake up</strong> at ten to five. I <strong>get up</strong> <span class="cn-word" data-pos="adv" data-tr="darhol">straight away</span>, because if I lie there for four minutes I lie there for forty. I <strong>put on</strong> the grey jacket, I <strong>set off</strong> at twenty past, and I <strong>get on</strong> the second bus at the corner with about nine other men who all look exactly as tired as I do. We <strong>get off</strong> at the gate at twenty to six.</p>

<p>The work itself is easy to describe: boxes come in, boxes <strong>go out</strong>. I <span class="cn-word" data-pos="verb" data-tr="tekshirmoq">check</span> them, I <span class="cn-word" data-pos="verb" data-tr="belgi qoʻymoq">label</span> them, I <strong>put</strong> them <strong>away</strong> in the right <span class="cn-word" data-tr="qator, javon qatori">aisle</span>. On a good <span class="cn-word" data-tr="smena, navbat">shift</span> I move about four hundred of them.</p>

<p>Now the part I have not told anybody at home.</p>

<p>In the third month I nearly <strong>gave up</strong>. Not because of the work — the work was fine. I could not <strong>get on with</strong> anybody, because I could not say anything, and a man who cannot say anything slowly stops being a person in a room. I was <span class="cn-word" data-pos="adj" data-tr="uy sogʻinchidagi">homesick</span> in a way I had not expected, and I had already <span class="cn-word" data-pos="verb" data-tr="qidirib topmoq">looked up</span> the price of a ticket home.</p>

<p>My <span class="cn-word" data-tr="xonadosh">roommate</span> is called Ravi and he is from Sri Lanka and he has been here for nine years. He <span class="cn-word" data-pos="verb" data-tr="sezib qolmoq">noticed</span>. He did not <span class="cn-word" data-pos="verb" data-tr="maʼruza oʻqimoq">lecture</span> me and he did not <strong>cheer</strong> me <strong>up</strong>. He wrote twenty phrasal verbs on the wall by the door in black <span class="cn-word" data-tr="marker, flomaster">marker</span> — <i>get up, set off, hurry up, hand in, find out, catch up, get on with, fall out with, make up, look after, put up with, take after</i> and eight more — and he made me say one of them <span class="cn-word" data-pos="adv" data-tr="ovoz chiqarib">out loud</span>, in a whole sentence, every morning before I went out of that door.</p>

<p>It took about eleven weeks. By the sixth month I could <strong>get by</strong>. Not well. But I could <span class="cn-word" data-pos="verb" data-tr="hazillashmoq">joke</span> with the men on my floor, and I could <strong>put up with</strong> the ones I did not like, and one of them now <strong>looks after</strong> my <span class="cn-word" data-tr="kalitlar dastasi">bunch of keys</span> when I go anywhere.</p>

<p>At the bottom of the wall Ravi wrote one more line, not a phrasal verb: <i>get on with people — that is the whole job.</i> He was right, and it was the most useful English anybody has ever taught me.</p>

<p>So do not <span class="cn-word" data-pos="verb" data-tr="yodlamoq">memorise</span> them one by one out of a <span class="cn-word" data-tr="lugʻat">dictionary</span>. Six a week, by topic, out loud. And you <strong>take after</strong> our mother, so you will be faster at it than I was.</p>

<p>Your brother,<br>Bekzod</p>''',
        "questions": [
            {
                "text": "What nearly made Bekzod go home in his third month?",
                "choices": [
                    "The work in the warehouse was too heavy",
                    "He could not get on with anybody, because he could not speak",
                    "He had fallen out with his roommate Ravi",
                ],
                "answer": 1,
                "explanation": "Xatda aniq yozilgan: ish qiyin emas edi. "
                               "U hech kim bilan chiqisha olmasdi, chunki "
                               "gapira olmasdi.",
            },
            {
                "text": "In the letter, 'I could get by' means that he could…",
                "choices": [
                    "manage, even though his English was not good",
                    "walk past people without speaking",
                    "get a better job in the warehouse",
                ],
                "answer": 0,
                "explanation": "<b>get by</b> — mukammal boʻlmasa ham "
                               "uddalamoq, kun koʻrmoq. Uning oʻzi ham "
                               "shunday deydi: “Not well. But…”",
            },
            {
                "text": "'You take after our mother' means that Dilnoza…",
                "choices": [
                    "should follow her mother's advice",
                    "is like her mother",
                    "will look after her mother",
                ],
                "answer": 1,
                "explanation": "<b>take after</b> — <i>oʻxshamoq</i> "
                               "(xarakteri yoki koʻrinishi bilan). "
                               "Bu frazali feʼlni soʻzma-soʻz tarjima "
                               "qilish xatoga olib keladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-79 — expressions of quantity   (the 1993 list)          [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "A Slice, a Loaf, a Bottle",
        "summary": (
            "PE-79 matni. 1993-yilgi xarid roʻyxati eski oshpazlik "
            "kitobidan chiqdi: ikkita non, bir kilo guruch, bir "
            "plitka sovun. Roʻyxatning eng oxirgi qatori esa "
            "butun bir qishning tarixini aytib berdi."
        ),
        "order":   79,
        "grammar": [
            {
                "pattern":  "a loaf of / a bottle of / a bar of — counting the uncountable",
                "meaning":  "Sanalmaydigan otni sanash uchun "
                            "<b>idish yoki oʻlchov soʻzi</b> "
                            "qoʻshiladi: <i>a <b>loaf of</b> bread</i>, "
                            "<i>a <b>bottle of</b> oil</i>, "
                            "<i>a <b>bar of</b> soap</i>, "
                            "<i>a <b>packet of</b> tea</i>, "
                            "<i>a <b>kilo of</b> rice</i>. "
                            "Koʻplik <b>oʻlchov soʻziga</b> qoʻshiladi, "
                            "moddaga emas: <i>two loaves of bread</i> ✓, "
                            "<i>two breads</i> ✗.",
                "examples": ["Two loaves of bread.",
                             "Three bottles of sunflower oil.",
                             "A bar of soap and a packet of tea."],
            },
            {
                "pattern":  "a piece of — the universal rescue",
                "meaning":  "Kerakli soʻz esdan chiqsa, "
                            "<b>a piece of</b> deyarli har qanday "
                            "sanalmaydigan otni qutqaradi: "
                            "<i>a piece of advice / paper / news / "
                            "furniture</i>. Yana: <b>a sheet of</b> "
                            "paper, <b>a bunch of</b> keys, "
                            "<b>a drop of</b> water, "
                            "<b>a grain of</b> rice.",
                "examples": ["She gave me one piece of advice.",
                             "The list was on half a sheet of paper.",
                             "There was not a grain of rice left in the house."],
            },
            {
                "pattern":  "a pair of — the always-plural nouns",
                "meaning":  "Ikki qismdan iborat narsalar ingliz "
                            "tilida doim koʻplikda: <b>a pair of</b> "
                            "shoes / trousers / glasses / scissors. "
                            "Feʼl <b>pair</b> soʻziga qarab birlikda "
                            "boʻladi: <i>This <b>pair</b> of shoes "
                            "<b>is</b> new</i>.",
                "examples": ["A pair of shoes for Sherbek.",
                             "That pair of boots was two sizes too big.",
                             "He was wearing his sister's pair of winter boots."],
            },
        ],
        "body": '''<p>The list <span class="cn-word" data-pos="verb" data-tr="tushib ketmoq">fell out</span> of my grandmother's <span class="cn-word" data-tr="oshpazlik kitobi">cookbook</span> in the spring of 2019, twenty-six years after somebody wrote it. Half a <span class="cn-word" data-tr="varaq qogʻoz">sheet of paper</span>, <span class="cn-word" data-pos="adj" data-tr="oʻchib ketgan">faded</span> to grey, in pencil, in her handwriting.</p>

<p>It said: <strong>two loaves of</strong> bread. <strong>A kilo of</strong> rice. <strong>Half a kilo of</strong> sugar. <strong>Three bottles of</strong> oil. <strong>A packet of</strong> tea. <strong>A bar of</strong> <span class="cn-word" data-tr="sovun">soap</span>. <strong>A bunch of</strong> <span class="cn-word" data-tr="sabzi">carrots</span> if they are cheap.</p>

<p>Then, at the bottom, on its own line, in smaller letters: <strong>a pair of</strong> shoes for Sherbek — if there is money left.</p>

<p>My father is Sherbek. He was nine years old in 1993.</p>

<p>I took the paper to him in his shop that evening and put it on the <span class="cn-word" data-tr="peshtaxta">counter</span>, and he read it twice without saying anything, which is not like him at all.</p>

<p>Then he told me the whole winter in about four minutes. Prices were changing between the morning and the afternoon that year. My grandmother worked at a school and was paid <span class="cn-word" data-pos="adv" data-tr="kechikib">late</span>, and by January the family was buying food in <span class="cn-word" data-tr="kichik miqdor">small amounts</span> — a <span class="cn-word" data-tr="tilim">slice</span> of cheese at a time, one <span class="cn-word" data-tr="boʻlak">piece of</span> meat for a pot of soup that had to last three days.</p>

<p>There was no money left. He knew there would not be, he said, before she even went out of the door.</p>

<p>He wore his older sister's winter <span class="cn-word" data-tr="etik">boots</span> to school for the whole of that year. They were two sizes too big, they were <span class="cn-word" data-pos="adj" data-tr="qizil-jigarrang">reddish brown</span>, and the boys in his class had a name for them, which he told me and I am not going to write down.</p>

<p>My father has sold shoes in that shop since 2006. He is not a <span class="cn-word" data-pos="adj" data-tr="hissiyotli">sentimental</span> man and he does not tell this story to <span class="cn-word" data-tr="xaridorlar">customers</span>.</p>

<p>But the list is on the wall behind the counter now, in a black <span class="cn-word" data-tr="ramka">frame</span>, and there is one rule in that shop that he has never explained to anybody who works there. If a child comes in with no money and shoes that do not fit, that child goes out with a <strong>pair of</strong> shoes.</p>

<p>He gave me one <strong>piece of</strong> <span class="cn-word" data-tr="maslahat">advice</span> about the whole thing, and only one. Keep the list, he said. Not because it was hard. Because somebody counted, and we ate.</p>''',
        "questions": [
            {
                "text": "Why is the 1993 shopping list in a frame in the shop?",
                "choices": [
                    "It is the first list the grandmother ever wrote",
                    "It is the reason for the shop's unwritten rule about children's shoes",
                    "It shows what food cost in 1993",
                ],
                "answer": 1,
                "explanation": "Roʻyxatning oxirgi qatori — “agar pul "
                               "ortsa, Sherbekka tufli” — va pul "
                               "ortmagan edi. Doʻkondagi qoida aynan "
                               "shu qatordan kelib chiqqan.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "She bought two breads and three oils.",
                    "She bought two loaves of bread and three bottles of oil.",
                    "She bought two loafs of breads and three bottle of oil.",
                ],
                "answer": 1,
                "explanation": "Sanalmaydigan otni oʻlchov soʻzi bilan "
                               "sanaymiz va koʻplik <b>oʻlchov soʻziga</b> "
                               "qoʻshiladi: <i>two <b>loaves</b> of "
                               "bread</i>, <i>three <b>bottles</b> of "
                               "oil</i> — <i>bread</i> va <i>oil</i> "
                               "oʻzgarmaydi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "This pair of shoes is new.",
                    "This pair of shoes are new.",
                    "This pair of shoe is new.",
                ],
                "answer": 0,
                "explanation": "Feʼl <b>pair</b> soʻziga qarab birlikda "
                               "boʻladi, <i>shoes</i> ga emas. Shuning "
                               "uchun <i>is</i>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-80 — articles, advanced cases   (the telescope)         [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Moon, a Moon, Moons",
        "summary": (
            "PE-80 matni. 1998-yil, Qizilqum chetidagi qishloq "
            "maktabining tomida oʻqituvchi oʻzi yasagan teleskop "
            "turardi. Oʻsha kechada bir soʻz — <i>the</i> — "
            "oʻn bir yoshli qiz uchun maʼnosini oʻzgartirdi."
        ),
        "order":   80,
        "grammar": [
            {
                "pattern":  "the with rivers, ranges, deserts and plural countries",
                "meaning":  "Geografiyada qoida oddiy: nom "
                            "<b>guruh yoki koʻplik</b> maʼnosini "
                            "bersa — <b>the</b>: <i>the Kyzylkum, "
                            "the Tian Shan, the Amu Darya, the Aral "
                            "Sea, the USA</i>. Yagona nom boʻlsa — "
                            "<b>artiklsiz</b>: <i>Uzbekistan, "
                            "Tashkent, Lake Aral, Mount Everest</i>.",
                "examples": ["The village stood at the edge of the Kyzylkum.",
                             "He had never seen the Tian Shan or the USA.",
                             "He had never left Uzbekistan."],
            },
            {
                "pattern":  "the sun, the moon — and the piano, twice a week",
                "meaning":  "<b>the</b> — yagona narsalar bilan "
                            "(<i>the sun, the moon, the sky, the "
                            "internet</i>), cholgʻu asboblari bilan "
                            "(<i>play <b>the</b> piano</i>), "
                            "oʻn yilliklar bilan (<i>in the 1990s</i>) "
                            "va <i>the first time</i> kabi tartib "
                            "sonlar bilan. <b>a</b> esa “har”, "
                            "“-iga” maʼnosini beradi: "
                            "<i>twice <b>a</b> week</i>, "
                            "<i>sixty km <b>an</b> hour</i>.",
                "examples": ["He opened the roof twice a week.",
                             "In the 1990s there was no internet in that village.",
                             "It was the first time I had looked through a telescope."],
            },
            {
                "pattern":  "the + adjective = a whole group of people",
                "meaning":  "<b>the</b> + sifat = shu toifadagi "
                            "<b>hamma odamlar</b>, va feʼl "
                            "<b>koʻplikda</b> boʻladi: "
                            "<i><b>the young</b>, <b>the poor</b>, "
                            "<b>the old</b></i>. Ot ham, "
                            "<i>-s</i> ham qoʻshilmaydi "
                            "(<i>the poors</i> ✗, "
                            "<i>the young people's</i> ✗).",
                "examples": ["The young in that village had never seen a telescope.",
                             "The old came up to the roof too.",
                             "The poor need help."],
            },
        ],
        "body": '''<p>Our village sits at the <span class="cn-word" data-tr="chekka, chet">edge</span> of <strong>the Kyzylkum</strong>, and in 1998 that meant two things. It meant we had the blackest sky in the country, and it meant we had almost nothing else.</p>

<p>There was no internet. Nobody in my class had left <strong>Uzbekistan</strong>. I had heard of <strong>the USA</strong> and <strong>the Tian Shan</strong> and I could not have told you which of the two was further away.</p>

<p>Rustam aka taught physics. He was a small, <span class="cn-word" data-pos="adj" data-tr="sabrli">patient</span> man who played <strong>the</strong> <span class="cn-word" data-tr="garmon">accordion</span> badly at every wedding, and in the winter of 1997 he built a <span class="cn-word" data-tr="teleskop">telescope</span> out of a <span class="cn-word" data-pos="adj" data-tr="siniq">cracked</span> <span class="cn-word" data-tr="linza">lens</span> from a broken camera, a length of <span class="cn-word" data-tr="quvur">pipe</span> and the <span class="cn-word" data-tr="uch oyoq, shtativ">tripod</span> from the school's <span class="cn-word" data-tr="kinoapparat">film projector</span>.</p>

<p>He carried it up onto the school roof twice <strong>a</strong> week and let anybody stand in the line. <strong>The young</strong> came first, and after a month <strong>the old</strong> started coming up the <span class="cn-word" data-tr="narvon">ladder</span> too, slowly, in coats.</p>

<p>The first time I looked through it I was eleven. He had it pointed at <strong>the moon</strong>, and I saw the edge of it, and the edge was not <span class="cn-word" data-pos="adj" data-tr="silliq">smooth</span>. It had <span class="cn-word" data-tr="chuqurlik, krater">craters</span> on it and a broken grey <span class="cn-word" data-tr="soya">shadow</span> down one side.</p>

<p>Then he moved the pipe and said, look again.</p>

<p>There was a small white <span class="cn-word" data-tr="disk, doira">disc</span>, and beside it, in a line, four tiny points of light.</p>

<p>"Jupiter," he said. "And four of its moons."</p>

<p>I told him he was wrong. I was eleven and I told a physics teacher he was wrong, and I remember the sentence: there is only one moon, and it is <strong>the</strong> moon.</p>

<p>He did not laugh at me. He pointed up at the sky with one hand, and at the <span class="cn-word" data-tr="okulyar">eyepiece</span> with the other.</p>

<p>"That is <strong>the moon</strong>," he said. "These are <strong>moons</strong>. Ours has a name and a <strong>the</strong> because it is ours. It is not the only one."</p>

<p>I have thought about that answer for twenty-seven years, because it was not really about Jupiter. A word I had used every day of my life turned out to be a <span class="cn-word" data-tr="daʼvo, taʼkid">claim</span>: <strong>the</strong> means the one we both know about, and if you have only ever seen one of something, you will call it <strong>the</strong> one for your whole life.</p>

<p>Rustam aka died in 2016. He never saw <strong>the Alps</strong>, or <strong>the USA</strong>, or a real <span class="cn-word" data-tr="rasadxona">observatory</span>.</p>

<p>He showed about four hundred children <strong>a</strong> moon that was not <strong>the</strong> moon. Two of us do this for a living now.</p>''',
        "questions": [
            {
                "text": "What did the narrator understand that night, beyond the fact about Jupiter?",
                "choices": [
                    "That her village had the darkest sky in the country",
                    "That 'the' claims something is the only one you know about",
                    "That she wanted to become a physics teacher",
                ],
                "answer": 1,
                "explanation": "Oxirgi qismda aniq aytilgan: <b>the</b> — "
                               "“ikkalamiz biladigan yagona narsa” degan "
                               "daʼvo. Bir marta koʻrgan narsangizni umr "
                               "boʻyi <i>the</i> deb atayverasiz.",
            },
            {
                "text": "Which sentence uses articles correctly?",
                "choices": [
                    "We flew from the Uzbekistan to USA over Black Sea.",
                    "We flew from Uzbekistan to the USA over the Black Sea.",
                    "We flew from Uzbekistan to USA over the Black Sea.",
                ],
                "answer": 1,
                "explanation": "Yagona nom — artiklsiz "
                               "(<i>Uzbekistan</i>), koʻplik yoki guruh "
                               "nomi — <b>the</b> bilan "
                               "(<i>the USA</i> = Qoʻshma Shtatlar, "
                               "<i>the Black Sea</i>).",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "The young in that village had never seen a telescope.",
                    "The youngs in that village had never seen a telescope.",
                    "The young people's in that village had never seen a telescope.",
                ],
                "answer": 0,
                "explanation": "<b>the</b> + sifat butun toifani "
                               "bildiradi va <i>-s</i> qoʻshilmaydi: "
                               "<i>the young</i>, <i>the old</i>, "
                               "<i>the poor</i>. Feʼl koʻplikda boʻladi.",
            },
        ],
    },
]
