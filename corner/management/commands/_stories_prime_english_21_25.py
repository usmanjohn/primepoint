# -*- coding: utf-8 -*-
"""Prime English Readings — PE-21 … PE-25 (batch 5).

PE-21 irregular past · PE-22 past negatives and questions · PE-23 past continuous ·
PE-24 when and while · PE-25 used to / would.

Cumulative rule: PE-21's story is positive statements only — "did" questions and
"didn't" negatives arrive in PE-22, and that is exactly what PE-22's story is made
of. PE-23 sets scenes, PE-24 breaks them. Still no perfect tenses (PE-32+), no
modals (PE-42+), no comparatives (PE-67).
Length: 150–190 words — the scene stories can carry it now.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_21_25.py --author=prime
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
    # PE-21 — past simple: irregular verbs
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "He Took the Wrong Bus",
        "summary": (
            "PE-21 matni. Sherbek 21 oʻrniga 12-avtobusga chiqib oladi va "
            "notanish mahallada qoladi. Matndagi feʼllar deyarli hammasi "
            "notoʻgʻri feʼllar."
        ),
        "order":   21,
        "grammar": [
            {
                "pattern":  "Irregular verbs: take → took, see → saw, go → went",
                "meaning":  "Notoʻgʻri feʼllar <b>-ed</b> olmaydi — "
                            "ularning oʻz oʻtgan zamon shakli bor. "
                            "Ularni faqat yodlash kerak, va yaxshi "
                            "yangilik shu: eng koʻp ishlatiladigan "
                            "yuzta feʼl shu roʻyxatda.",
                "examples": ["On Tuesday Sherbek took the wrong bus.",
                             "He saw the number and got on."],
            },
            {
                "pattern":  "Some do not change at all",
                "meaning":  "<i>put – put</i>, <i>cut – cut</i>, "
                            "<i>let – let</i>, <i>read – read</i> "
                            "(faqat talaffuzi oʻzgaradi: /riːd/ → /red/). "
                            "Bu — sovgʻa: yodlash oson.",
                "examples": ["He put his bag on his knees."],
            },
            {
                "pattern":  "The story's list",
                "meaning":  "Matndan yigʻilgan shakllar: "
                            "took · ran · saw · got · left · sat · put · "
                            "knew · felt · came · gave · told · thought · "
                            "found · stood · had. Bir hikoyada oʻn "
                            "oltita notoʻgʻri feʼl.",
                "examples": ["He felt cold.", "She gave him one bag.",
                             "I found a new street."],
            },
        ],
        "body": '''<p>On Tuesday Sherbek <strong>took</strong> the <span class="cn-word" data-pos="adj" data-tr="notoʻgʻri">wrong</span> bus.</p>

<p>He <strong>ran</strong> to the bus stop in the rain, <strong>saw</strong> a number in the window and <strong>got</strong> on. The bus <strong>left</strong> the stop. He <strong>sat</strong> down and <strong>put</strong> his bag on his <span class="cn-word" data-tr="tizzalar">knees</span>.</p>

<p>After ten minutes he <strong>knew</strong> the <span class="cn-word" data-tr="haqiqat">truth</span>: bus 12 is not bus 21.</p>

<p>Outside the window everything was new. He <strong>saw</strong> a <span class="cn-word" data-tr="zavod">factory</span>, a <span class="cn-word" data-tr="ariq, kanal">canal</span> and a long grey wall.</p>

<p>He <strong>got</strong> off at the last stop and <strong>stood</strong> in the rain. He <strong>had</strong> no money and no umbrella. He <strong>felt</strong> cold.</p>

<p>An old woman with two heavy bags <strong>came</strong> to the same stop. For a minute she <strong>said</strong> nothing. Then she <strong>gave</strong> him one bag.</p>

<p>"Hold this. The 12 <strong>goes</strong> back in ten minutes."</p>

<p>They <strong>sat</strong> on the same <span class="cn-word" data-tr="skameyka">bench</span>. She <strong>told</strong> him the name of every street between the canal and the school. Sherbek <strong>thought</strong> about his mother's face at seven o'clock.</p>

<p>At half past seven he <strong>came</strong> home with two hot samsas in a paper bag.</p>

<p>"Where were you?" his mother said.</p>

<p>"I <strong>took</strong> the wrong bus," Sherbek said, "and I <strong>found</strong> a new street."</p>''',
        "questions": [
            {
                "text": "How does Sherbek get the samsas?",
                "choices": [
                    "The old woman gives them to him for holding her bag",
                    "He buys them near the canal",
                    "His mother sends money to him",
                ],
                "answer": 0,
                "explanation": "Uning puli yoʻq edi (“He had no money”). "
                               "Sumkani koʻtargani uchun keksa ayol unga "
                               "samsa beradi — matn buni ochiq aytmaydi, "
                               "lekin boshqa yoʻl yoʻq.",
            },
            {
                "text": "Which past forms are correct?",
                "choices": [
                    "taked, seed, getted",
                    "took, saw, got",
                    "took, seen, gotten",
                ],
                "answer": 1,
                "explanation": "take → <b>took</b>, see → <b>saw</b>, "
                               "get → <b>got</b>. <i>seen</i> va "
                               "<i>gotten</i> — uchinchi shakl, u "
                               "perfektga tegishli (PE-32).",
            },
            {
                "text": "Which verb has the same form in the past?",
                "choices": ["put", "know", "give"],
                "answer": 0,
                "explanation": "<b>put – put – put</b> oʻzgarmaydi. "
                               "know → knew, give → gave.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-22 — past simple: negatives and questions
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Nobody Locked the Door",
        "summary": (
            "PE-22 matni. Chorshanba tongida 12-xonaning eshigi ochiq "
            "qoladi. Hech narsa yoʻqolmaydi — lekin shkafda beshta mushuk "
            "topiladi. Matn boshdan-oyoq did/didn't ustida."
        ),
        "order":   22,
        "grammar": [
            {
                "pattern":  "didn't + base verb",
                "meaning":  "Inkorda <b>did not</b> yordamchisi oʻtgan "
                            "zamonni oʻziga oladi, asosiy feʼl esa "
                            "<b>asosiy shaklga qaytadi</b>: "
                            "<i>I didn't lock it</i> — hech qachon "
                            "<i>didn't locked</i> emas.",
                "examples": ["I didn't lock it.", "The money didn't disappear."],
            },
            {
                "pattern":  "Did + subject + base verb?",
                "meaning":  "Savolda ham xuddi shunday: <b>did</b> gap "
                            "boshiga chiqadi, feʼl asosiy shaklda qoladi. "
                            "Bu qoida notoʻgʻri feʼllarga ham tegishli: "
                            "<i>Did you see…?</i>, <i>Did he leave…?</i>",
                "examples": ["Did you lock it?", "Did anybody see a cat yesterday?"],
            },
            {
                "pattern":  "Who / What as subject → no “did”",
                "meaning":  "Agar soʻroq soʻzi eganing oʻrnida tursa, "
                            "<i>did</i> kerak emas va feʼl oʻtgan zamon "
                            "shaklida qoladi: <b>Who left last?</b>, "
                            "<b>Who opened the door?</b>",
                "examples": ["Who left last?", "Who opened the door?"],
            },
        ],
        "body": '''<p>On Wednesday morning the door of Room 12 was open. It was open all night.</p>

<p>"<strong>Did</strong> you <strong>lock</strong> it?" the caretaker asked Afsona.</p>

<p>"I <strong>didn't lock</strong> it," she said. "I <strong>didn't have</strong> the key. Jasur had the key."</p>

<p>"<strong>Did</strong> Jasur <strong>leave</strong> last?"</p>

<p>"No, he <strong>didn't</strong>. He left at four with me."</p>

<p>"<strong>Who left</strong> last?" the caretaker asked. Nobody knew.</p>

<p>He looked around the room. Nothing was gone. The computer <strong>didn't move</strong>. Nobody <strong>touched</strong> the exam papers on the desk, and the money in the <span class="cn-word" data-tr="tortma">drawer</span> <strong>didn't disappear</strong>.</p>

<p>Then Dilnoza opened the <span class="cn-word" data-tr="shkaf">cupboard</span>. On a <span class="cn-word" data-tr="uyum">pile</span> of old <span class="cn-word" data-tr="xaritalar">maps</span> a small grey cat was lying with four <span class="cn-word" data-tr="mushukchalar">kittens</span>.</p>

<p>"<strong>Did</strong> anybody <strong>see</strong> a cat here yesterday?" the caretaker asked.</p>

<p>Nobody answered. But now everybody understood one thing: somebody <strong>didn't forget</strong> the door. Somebody left it open <span class="cn-word" data-tr="ataylab">on purpose</span>.</p>

<p>The cat stayed in Room 12 until May. And <strong>who opened</strong> that door — nobody in this school says, not even today.</p>''',
        "questions": [
            {
                "text": "Why was the door open all night?",
                "choices": [
                    "Somebody forgot to lock it",
                    "Somebody left it open on purpose for the cat",
                    "The caretaker lost the key",
                ],
                "answer": 1,
                "explanation": "“Somebody didn't forget the door. Somebody "
                               "left it open on purpose.” Shkafda mushuk va "
                               "toʻrtta mushukcha bor edi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "I didn't locked it.",
                    "I didn't lock it.",
                    "I don't locked it.",
                ],
                "answer": 1,
                "explanation": "<b>did</b> allaqachon oʻtgan zamonni "
                               "koʻrsatadi, shuning uchun feʼl asosiy "
                               "shaklda: <i>lock</i>.",
            },
            {
                "text": "Which question needs NO \"did\"?",
                "choices": [
                    "___ Jasur leave last?",
                    "___ left last?",
                    "___ anybody see a cat?",
                ],
                "answer": 1,
                "explanation": "<b>Who left last?</b> — soʻroq soʻzi "
                               "eganing oʻzi, shuning uchun <i>did</i> "
                               "qoʻshilmaydi va feʼl oʻtgan zamonda qoladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-23 — past continuous
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "While the Others Were Sleeping",
        "summary": (
            "PE-23 matni. Qishloq maktabida tunning uchida yigirma "
            "oʻquvchi uxlayotgan edi — Bekzod esa uxlamayotgan edi. "
            "Oʻtgan zamon davomli: sahnaning kamerasi."
        ),
        "order":   23,
        "grammar": [
            {
                "pattern":  "was / were + verb-ing",
                "meaning":  "Oʻtgan zamonning bir <b>daqiqasida</b> davom "
                            "etayotgan ish. PE-12 dagi davomli zamonning "
                            "aynan oʻzi, faqat <i>am/is/are</i> oʻrniga "
                            "<b>was/were</b> keladi.",
                "examples": ["Twenty pupils were sleeping on the floor.",
                             "He was listening to the rain."],
            },
            {
                "pattern":  "wasn't / weren't · Was …ing?",
                "meaning":  "Inkor: <i>He wasn't sleeping</i>. Savol: "
                            "<i>Was it raining?</i> — <b>was</b> oldinga "
                            "chiqadi. <i>did</i> bu zamonda ishlatilmaydi.",
                "examples": ["Bekzod wasn't sleeping.",
                             "Was it raining in your dream too?"],
            },
            {
                "pattern":  "It paints the SCENE",
                "meaning":  "Bu zamonning vazifasi — hikoyaning "
                            "<b>fonini</b> chizish: soat uchda kim nima "
                            "qilayotgan edi. PE-24 da shu fonni "
                            "boʻlib yuboradigan qisqa harakat qoʻshiladi.",
                "examples": ["A light was burning in a small house.",
                             "The teacher was writing in red."],
            },
        ],
        "body": '''<p>At three o'clock in the morning the village school was quiet. Twenty pupils <strong>were sleeping</strong> on the floor of the big room, in <span class="cn-word" data-tr="paltolar">coats</span> and <span class="cn-word" data-tr="paypoqlar">socks</span>.</p>

<p>Bekzod <strong>wasn't sleeping</strong>. He <strong>was listening</strong> to the rain on the roof.</p>

<p>He walked to the window. Outside, a light <strong>was burning</strong> in a small house. A woman <strong>was making</strong> bread at a table, and two children <strong>were carrying</strong> water from the yard.</p>

<p>In the corridor the teacher <strong>was sitting</strong> on a low chair with thirty <span class="cn-word" data-tr="daftarlar">exercise books</span> on her knees. She <strong>was writing</strong> in red <span class="cn-word" data-tr="siyoh">ink</span>.</p>

<p>"Why <strong>aren't</strong> you <strong>sleeping</strong>?" she asked.</p>

<p>"The rain <strong>was making</strong> a noise," Bekzod said.</p>

<p>"<strong>Was</strong> it <strong>raining</strong> in your <span class="cn-word" data-tr="tush">dream</span> too?"</p>

<p>She <span class="cn-word" data-pos="verb" data-tr="quydi">poured</span> tea from a <span class="cn-word" data-tr="choynak">kettle</span> on the floor. At half past three Bekzod <strong>was drinking</strong> tea in a cold corridor and reading his classmates' names in red ink.</p>

<p>The light in the small house <strong>was still burning</strong> when he went back to his coat on the floor.</p>

<p>He understood something that night. While twenty people <strong>were sleeping</strong>, three people <strong>were working</strong>.</p>''',
        "questions": [
            {
                "text": "What was the teacher doing at three o'clock?",
                "choices": [
                    "She was sleeping in the big room",
                    "She was marking exercise books in the corridor",
                    "She was making bread in a small house",
                ],
                "answer": 1,
                "explanation": "“The teacher was sitting on a low chair with "
                               "thirty exercise books… She was writing in red "
                               "ink.”",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "Bekzod didn't sleeping.",
                    "Bekzod wasn't sleeping.",
                    "Bekzod not was sleeping.",
                ],
                "answer": 1,
                "explanation": "Davomli zamonda inkor <i>be</i> feʼliga "
                               "qoʻshiladi: <b>wasn't sleeping</b>. "
                               "<i>did</i> bu zamonga aralashmaydi.",
            },
            {
                "text": "What does Bekzod understand that night?",
                "choices": [
                    "That the rain always wakes him",
                    "That some people work while others sleep",
                    "That the village school is too cold",
                ],
                "answer": 1,
                "explanation": "Oxirgi gap: “While twenty people were "
                               "sleeping, three people were working.” — "
                               "oʻqituvchi va qoʻshni uydagi ona-bola.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-24 — past simple vs past continuous: when and while
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Goal He Did Not See",
        "summary": (
            "PE-24 matni. Jasur choyxonada oʻyinni telefonda koʻrayotgan "
            "edi — va suv olishga chiqqanida gol boʻldi. when qisqa "
            "harakatni, while uzun harakatni olib keladi."
        ),
        "order":   24,
        "grammar": [
            {
                "pattern":  "while + past continuous · when + past simple",
                "meaning":  "<b>while</b> uzun, davom etayotgan ish bilan "
                            "keladi; <b>when</b> qisqa, bir lahzada "
                            "boʻlgan ish bilan. Oʻzbekchada bu "
                            "“…ayotganda” va “…ganda” farqi.",
                "examples": ["While Jasur was walking to the shop, the crowd shouted.",
                             "When the ball went in, he was buying water."],
            },
            {
                "pattern":  "Background + interruption",
                "meaning":  "Davomli zamon — <b>fon</b>, oddiy oʻtgan "
                            "zamon — uni <b>boʻlib yuboradigan</b> "
                            "voqea. Shuning uchun hikoyalar shu ikki "
                            "zamonni birga ishlatadi.",
                "examples": ["While he was standing at the shop door, Uzbekistan scored."],
            },
            {
                "pattern":  "Comma when the clause comes first",
                "meaning":  "<i>While he was walking<b>,</b> the crowd "
                            "shouted.</i> Agar <i>while/when</i> boʻlagi "
                            "gap boshida tursa, vergul qoʻyiladi; "
                            "oxirida tursa — qoʻyilmaydi.",
                "examples": ["He ran back when he heard the noise."],
            },
        ],
        "body": '''<p>The <span class="cn-word" data-tr="oʻyin, uchrashuv">match</span> started at nine. Jasur <strong>was watching</strong> it on a small phone in his uncle's <span class="cn-word" data-tr="choyxona">tea house</span>.</p>

<p><strong>While</strong> the first <span class="cn-word" data-tr="taym, yarim">half</span> <strong>was going on</strong>, nothing happened. Eleven men <strong>were running</strong> and nobody <strong>was scoring</strong>.</p>

<p>In the second half his uncle asked for water. <strong>While</strong> Jasur <strong>was walking</strong> to the shop, the <span class="cn-word" data-tr="olomon">crowd</span> in the tea house <strong>shouted</strong>.</p>

<p>He <strong>ran</strong> back. <span class="cn-word" data-tr="juda kech">Too late</span>: <strong>while</strong> he <strong>was standing</strong> at the shop door, Uzbekistan <span class="cn-word" data-pos="verb" data-tr="gol urdi">scored</span>.</p>

<p>"<strong>When</strong> the ball <strong>went</strong> in, I <strong>was buying</strong> a bottle of water," he said. Everybody in the room laughed at him.</p>

<p>Ten minutes later, <strong>while</strong> everybody <strong>was talking</strong> about that goal, the second goal came.</p>

<p>Jasur <strong>saw</strong> it. He was the only person in the tea house with his eyes on the <span class="cn-word" data-tr="ekran">screen</span>.</p>

<p>"<strong>When</strong> I <strong>saw</strong> it, nobody else <strong>was looking</strong>," he said. And this time nobody laughed.</p>

<p>Now his uncle has one rule in the tea house: in the second half, nobody goes for water.</p>''',
        "questions": [
            {
                "text": "What was Jasur doing when the first goal happened?",
                "choices": [
                    "He was watching the phone",
                    "He was standing at the shop door",
                    "He was talking to his uncle",
                ],
                "answer": 1,
                "explanation": "“While he was standing at the shop door, "
                               "Uzbekistan scored.” Uzun harakat — fon, gol "
                               "— qisqa voqea.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "While the ball went in, he was buying water.",
                    "When the ball went in, he was buying water.",
                    "When the ball was going in, he bought water.",
                ],
                "answer": 1,
                "explanation": "Qisqa voqea (<i>the ball went in</i>) → "
                               "<b>when</b>; uzun harakat "
                               "(<i>was buying</i>) → davomli zamon.",
            },
            {
                "text": "Why does nobody laugh the second time?",
                "choices": [
                    "Because Jasur was the only one watching when the second goal came",
                    "Because the uncle made a new rule",
                    "Because the match finished",
                ],
                "answer": 0,
                "explanation": "Ikkinchi golda hamma gapirib turgan edi, "
                               "faqat Jasur ekranga qarayotgan edi — "
                               "endi kulish oʻrinsiz.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-25 — used to / would: past habits
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "My Grandfather Used to Walk to School",
        "summary": (
            "PE-25 matni. Bobo maktabga sakkiz kilometr yurib borardi va "
            "poyabzalini qoʻlida koʻtarardi. used to va would — "
            "oʻtmishdagi odatlar."
        ),
        "order":   25,
        "grammar": [
            {
                "pattern":  "used to + base verb",
                "meaning":  "Oʻtmishda <b>odat</b> boʻlgan, hozir esa "
                            "boʻlmagan ish: <i>He used to walk to "
                            "school</i>. Oʻzbekchadagi <b>-ardi / -edi</b> "
                            "qoʻshimchasi aynan shu vazifani bajaradi: "
                            "“yurib borardi”.",
                "examples": ["My grandfather used to walk to school.",
                             "Shoes used to cost a month of his father's work."],
            },
            {
                "pattern":  "Did you use to …? · didn't use to …",
                "meaning":  "Savol va inkorda <b>use</b> — <i>d</i> siz: "
                            "<i>Did you use to cry?</i>, "
                            "<i>I didn't use to think about it</i>. "
                            "<i>did</i> allaqachon oʻtgan zamonni "
                            "koʻrsatib turadi.",
                "examples": ["Did you use to cry?", "I didn't use to think about it."],
            },
            {
                "pattern":  "would = repeated ACTIONS only",
                "meaning":  "<b>would</b> ham takroriy odatni bildiradi, "
                            "lekin faqat <b>harakat</b> uchun. Holat "
                            "(bor boʻlish, yashash, yoqtirish) uchun "
                            "faqat <i>used to</i>: <i>There <b>used to "
                            "be</b> one book</i> — “There would be one "
                            "book” xato.",
                "examples": ["He would carry his shoes in his hand.",
                             "There used to be one book for six pupils."],
            },
        ],
        "body": '''<p>My grandfather <strong>used to walk</strong> to school. The school was eight kilometres from his village.</p>

<p>In winter he <strong>used to leave</strong> home before <span class="cn-word" data-tr="tong, quyosh chiqishi">sunrise</span>. He <strong>would carry</strong> his shoes in his hand for the first three kilometres and walk <span class="cn-word" data-pos="adj" data-tr="yalangoyoq">barefoot</span>, because the road <strong>used to be</strong> <span class="cn-word" data-tr="loy">mud</span> — and shoes <strong>used to cost</strong> a month of his father's work.</p>

<p>"<strong>Did</strong> you <strong>use to</strong> cry?" I asked him once.</p>

<p>"No. I <strong>didn't use to</strong> think about it," he said. "Everybody walked."</p>

<p>He <strong>would</strong> sit at the back of the class, next to the <span class="cn-word" data-tr="pechka">stove</span>, because his coat was wet every morning. In the evening he <strong>would</strong> read next to a small oil <span class="cn-word" data-tr="chiroq">lamp</span>.</p>

<p>There <strong>used to be</strong> one book for six pupils. They <strong>would</strong> <span class="cn-word" data-pos="verb" data-tr="koʻchiradi">copy</span> the pages <span class="cn-word" data-tr="qoʻlda">by hand</span> and change the book on Fridays.</p>

<p>Now a yellow bus stops at the end of our street at half past seven. My grandfather stands at the gate every morning and watches it.</p>

<p>"<strong>Did</strong> you <strong>use to</strong> like school?" I asked him last week.</p>

<p>"I <strong>used to love</strong> the walk," he said. "The school was only at the end of it."</p>''',
        "questions": [
            {
                "text": "Why did the grandfather carry his shoes in his hand?",
                "choices": [
                    "Because the road was mud and shoes were expensive",
                    "Because the shoes were too small",
                    "Because he walked with his brother",
                ],
                "answer": 0,
                "explanation": "“…the road used to be mud — and shoes used "
                               "to cost a month of his father's work.” "
                               "Shuning uchun u yalangoyoq yurardi.",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "Did you used to cry?",
                    "Did you use to cry?",
                    "Did you use to cried?",
                ],
                "answer": 1,
                "explanation": "<i>did</i> bor — shuning uchun <b>use</b>, "
                               "<i>used</i> emas, va asosiy feʼl ham "
                               "asosiy shaklda: <i>cry</i>.",
            },
            {
                "text": "Which sentence CANNOT use \"would\"?",
                "choices": [
                    "He would read next to a small lamp.",
                    "They would copy the pages by hand.",
                    "There used to be one book for six pupils.",
                ],
                "answer": 2,
                "explanation": "“Bor boʻlish” — holat, harakat emas. "
                               "Holat uchun faqat <b>used to</b> "
                               "ishlatiladi.",
            },
        ],
    },
]
