# -*- coding: utf-8 -*-
"""Prime SAT Readings — 56–60 (SAT-56 … SAT-60 darslariga).

Written with the overrides in corner/management/commands/toc_prime_sat_readings.txt
⛔ MATNDA ALGEBRAIK BELGI YOʻQ — miqdorlar faqat ingliz tilida, soʻz bilan.

Til: matn, sarlavha va savollar INGLIZCHA; summary, cn-word glosslari,
     "Exam English" izohlari va javob tushuntirishlari OʻZBEKCHA.

Ovozlar (12-batch erkakdan boshlanadi): 56 Guy · 57 Jenny · 58 Guy ·
                                        59 Jenny · 60 Guy

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_56_60.py --author=prime
    python manage.py gen_corner_audio --collection="Prime SAT Readings" \\
        --only <n> --voice en-US-GuyNeural         # ⚠️ --voice MAJBURIY
    python manage.py import_corner_audio \\
        corner/management/commands/audio/prime-sat-readings \\
        --collection="Prime SAT Readings"
"""

SUBJECT = {
    "name":    "Matematika",
    "summary": "Matematika: hayotdagi matnlar, atamalar va matematik hikoyalar.",
    "icon":    "bi-calculator",
    "color":   "#f59e0b",
    "order":   7,
}

COLLECTION = {
    "title":       "Prime SAT Readings",
    "description": (
        "Prime SAT darslarining oʻqish matnlari — ingliz tilida, audio bilan. "
        "Har bir matn oʻz darsining matematikasini haqiqiy vaziyatda koʻrsatadi: "
        "asosiy mashq — inglizcha jumlani matematikaga aylantirish."
    ),
    "order":       3,
}

STORIES = [

    # ── 56 · a seismology station ────────────────────────────────────
    {
        "title": "The Day the Needle Moved",
        "order": 56,
        "summary": (
            "Yil davomidagi yozuvlarning deyarli hammasi bir xil — bittasidan "
            "tashqari. Va oʻsha bittasi butun yozuvning maqsadi."
        ),
        "body": """
<p>The <span class="cn-word" data-tr="seysmologiya stansiyasi">seismic station</span> in the
hills records ground movement every day of the year, and for three hundred and sixty-four days
the record is almost <span class="cn-word" data-tr="zerikarli">dull</span>. The
<span class="cn-word" data-tr="koʻrsatkich">readings</span> sit between one and three on the
station's scale, day after day, and the most common reading by far is two.</p>

<p>Then, on one afternoon in March, the needle moved to sixty-one.</p>

<p>Look at what that single day does to the year's
<span class="cn-word" data-tr="statistika, raqamlar">statistics</span>. The most common reading
is still two; it was two before March and it was two after. The middle reading, if you line the
whole year up in order, is still two. Neither of those numbers notices the
<span class="cn-word" data-tr="zilzila">earthquake</span> at all.</p>

<p>The <span class="cn-word" data-tr="oraliq">range</span>, though, went from two to sixty. And
the year's average, which had been sitting quietly at about two, was
<span class="cn-word" data-tr="tortmoq">dragged</span> upward by a single value some thirty
times the typical reading.</p>

<p>A student on <span class="cn-word" data-tr="amaliyot">placement</span> at the station asked
whether the March value should be <span class="cn-word" data-tr="chiqarib tashlamoq">excluded</span>
as an outlier, since it was making the year look
<span class="cn-word" data-tr="odatiy boʻlmagan">unrepresentative</span>.</p>

<p>The station's director gave the answer he gives every year to every student. The other three
hundred and sixty-four readings are the ones you could have
<span class="cn-word" data-tr="taxmin qilmoq">guessed</span>. This station was built, staffed and
paid for because of days like that one. "An outlier is not
<span class="cn-word" data-tr="shovqin, keraksiz maʼlumot">noise</span> by definition," he said.
"Sometimes it is the whole <span class="cn-word" data-tr="nuqta, maqsad">point</span>."</p>
""",
        "grammar": [
            {"pattern": "the most common reading",
             "meaning": "eng koʻp uchraydigan koʻrsatkich — moda"},
            {"pattern": "the middle reading, lined up in order",
             "meaning": "tartiblanganda oʻrtadagi — mediana"},
            {"pattern": "an outlier is not noise by definition",
             "meaning": "chetdagi qiymat taʼrifiga koʻra shovqin emas"},
        ],
        "questions": [
            {"text": "Which two measures did the March reading not affect?",
             "choices": ["The range and the average",
                         "The most common and the middle reading",
                         "Only the average",
                         "None of them"],
             "answer": 1,
             "explanation": "Moda ham, mediana ham ikki boʻlib qoldi — ular "
                            "qiymatning kattaligiga qaramaydi."},
            {"text": "What happened to the range?",
             "choices": ["It stayed at two", "It went from two to sixty",
                         "It became sixty-one", "It cannot be worked out"],
             "answer": 1,
             "explanation": "Eng katta koʻrsatkich oltmish bir, eng kichigi bir — "
                            "matn oraliq ikkidan oltmishga oʻzgarganini aytadi."},
            {"text": "Why did the director refuse to exclude the value?",
             "choices": ["The station exists because of days like that one",
                         "Excluding values is against the rules",
                         "The average would fall too far",
                         "The student had no authority"],
             "answer": 0,
             "explanation": "Qolgan yozuvlarni oldindan taxmin qilish mumkin edi; "
                            "stansiya aynan shunday kunlar uchun qurilgan."},
        ],
    },

    # ── 57 · a clinic ────────────────────────────────────────────────
    {
        "title": "Two Thermometers",
        "order": 57,
        "summary": (
            "Ikkala termometr ham oʻrtacha toʻgʻri koʻrsatadi — lekin bittasiga "
            "ishonib boʻlmaydi, chunki u har safar boshqacha oʻqiydi."
        ),
        "body": """
<p>The <span class="cn-word" data-tr="qishloq shifoxonasi">village clinic</span> was sent two
new thermometers and asked to test them before the old ones were thrown away. The
<span class="cn-word" data-tr="hamshira">nurse</span> did it properly: she put both into water
held at exactly thirty-seven degrees, took ten readings from each, and wrote them down.</p>

<p>The first thermometer read thirty-seven every time except twice, when it read thirty-six point
nine and thirty-seven point one. The second read thirty-four, then forty, then thirty-six, then
thirty-nine, and so on.</p>

<p>She worked out the <span class="cn-word" data-tr="oʻrtacha">average</span> of each set. Both
came to thirty-seven. On that number alone the two instruments were
<span class="cn-word" data-tr="bir xil">identical</span>.</p>

<p>The <span class="cn-word" data-tr="shifokor">doctor</span> looked at the two columns and did
not need a calculation. The first thermometer is
<span class="cn-word" data-tr="ishonchli, barqaror">reliable</span>: whatever it says, the true
temperature is within a tenth of a degree. The second is
<span class="cn-word" data-tr="foydasiz">useless</span>: it reads thirty-four for a patient who
is at thirty-seven, and forty for the next one.</p>

<p>Averaging <span class="cn-word" data-tr="yashirmoq">hides</span> exactly the thing a clinic
needs to know. A thermometer is not used ten times on ten patients and then averaged. It is used
once, on one patient, and the <span class="cn-word" data-tr="qaror">decision</span> is made from
that single reading.</p>

<p>She kept the ten readings anyway, in the back of the <span class="cn-word" data-tr="daftar">ledger</span>, because a <span class="cn-word" data-tr="taʼminotchi">supplier</span> who disputes a return will ask to see the numbers rather than the conclusion.</p>

<p>She sent the second one back with a note that said its average was
<span class="cn-word" data-tr="mukammal">perfect</span> and that this was not the
<span class="cn-word" data-tr="tegishli">relevant</span> question.</p>
""",
        "grammar": [
            {"pattern": "on that number alone",
             "meaning": "faqat oʻsha songa qarab — oʻrtacha yetarli emas"},
            {"pattern": "within a tenth of a degree",
             "meaning": "oʻndan bir daraja doirasida — kichik tarqalish"},
            {"pattern": "averaging hides exactly the thing you need",
             "meaning": "oʻrtachalash aynan kerakli narsani yashiradi"},
        ],
        "questions": [
            {"text": "What was the same about the two thermometers?",
             "choices": ["Their average reading", "Their price",
                         "Their reliability", "Their range of readings"],
             "answer": 0,
             "explanation": "Ikkalasining oʻrtachasi ham oʻttiz yetti — va aynan "
                            "shu narsa hech nimani hal qilmaydi."},
            {"text": "Why is the second thermometer useless in a clinic?",
             "choices": ["Its average is wrong",
                         "It is used once on one patient, and a single reading may be far off",
                         "It is too slow",
                         "It cannot measure high temperatures"],
             "answer": 1,
             "explanation": "Shifoxonada bitta koʻrsatkichga qarab qaror "
                            "qilinadi, oʻn marta oʻlchab oʻrtachalanmaydi."},
            {"text": "What did the nurse's note mean?",
             "choices": ["The thermometer was broken",
                         "The average was wrong",
                         "A perfect average was not the relevant question",
                         "The clinic needed more thermometers"],
             "answer": 2,
             "explanation": "Oʻrtacha mukammal edi — lekin savol tarqalish "
                            "haqida edi, oʻrtacha haqida emas."},
        ],
    },

    # ── 58 · history: the gambler's fallacy ──────────────────────────
    {
        "title": "Twenty-Six Times",
        "order": 58,
        "summary": (
            "1913-yilda bir stolda qora ketma-ket yigirma olti marta tushdi — "
            "va odamlar qizil «kelishi kerak» deb oʻylab, hammasini yoʻqotdi."
        ),
        "body": """
<p>On an evening in the summer of 1913, at a
<span class="cn-word" data-tr="qimorxona">casino</span> in Monte Carlo, a wheel came up black.
Then black again. It kept coming up black, and by the time the
<span class="cn-word" data-tr="ketma-ketlik">run</span> ended it had done so twenty-six times in
a row.</p>

<p>What happened around that table is the reason the evening is still written about. As the run
went on, more and more people <span class="cn-word" data-tr="pul tikmoq">bet</span> on red, and
they bet more and more heavily, because red was surely
<span class="cn-word" data-tr="kutilayotgan, muqarrar">due</span>. It had been so long. It could
not stay black.</p>

<p>It could. The wheel has no <span class="cn-word" data-tr="xotira">memory</span>. On every
single spin the chance of black was the same as it had been on the first, and the twenty-five
spins already behind it changed <span class="cn-word" data-tr="hech narsa">nothing</span> about
the twenty-sixth. A very long run is
<span class="cn-word" data-tr="kam uchraydigan">rare</span> — but once you are standing inside
one, it is no less likely to continue than it ever was.</p>

<p>The <span class="cn-word" data-tr="xato, adashish">mistake</span> was so clearly displayed
that evening that it took the name of the town. It is
<span class="cn-word" data-tr="atalgan">called</span> the Monte Carlo fallacy, or simply the
gambler's fallacy, and it has nothing to do with
<span class="cn-word" data-tr="qimor">gambling</span> in particular. It is the belief that
independent events somehow <span class="cn-word" data-tr="hisob yuritmoq">keep score</span>.</p>

<p>A coin that has landed heads five times has a
<span class="cn-word" data-tr="teng, aynan">precisely</span> even chance on the sixth throw. So
does a coin that has landed tails five times. So does a coin nobody has thrown yet.</p>
""",
        "grammar": [
            {"pattern": "red was surely due",
             "meaning": "qizil albatta kelishi kerak — bu xato fikr"},
            {"pattern": "the wheel has no memory",
             "meaning": "gʻildirakda xotira yoʻq — hodisalar bogʻliqsiz"},
            {"pattern": "independent events keep score",
             "meaning": "bogʻliqsiz hodisalar hisob yuritadi — xato ishonch"},
        ],
        "questions": [
            {"text": "Why did the gamblers bet on red?",
             "choices": ["The wheel was faulty",
                         "They believed red was due after so much black",
                         "Red pays more",
                         "The casino advised it"],
             "answer": 1,
             "explanation": "Uzoq davom etgan qora ketma-ketlikdan keyin qizil "
                            "«kelishi kerak» deb oʻylashgan — bu aynan gambler's "
                            "fallacy."},
            {"text": "What was true of the twenty-sixth spin?",
             "choices": ["Black was less likely than before",
                         "Red was more likely than before",
                         "The chance was the same as on the first spin",
                         "The chance cannot be known"],
             "answer": 2,
             "explanation": "Har bir aylanish bogʻliqsiz — oldingi yigirma "
                            "beshtasi hech narsani oʻzgartirmaydi."},
            {"text": "What is the fallacy really about?",
             "choices": ["Believing independent events keep score",
                         "Betting too much money",
                         "Casinos being dishonest",
                         "Rare events never happening"],
             "answer": 0,
             "explanation": "Matn buni aniq aytadi: bu qimorga emas, bogʻliqsiz "
                            "hodisalar hisob yuritadi degan ishonchga tegishli."},
        ],
    },

    # ── 59 · medical screening ───────────────────────────────────────
    {
        "title": "The Test Came Back Positive",
        "order": 59,
        "summary": (
            "Test 99 foiz aniq va natija musbat chiqdi — lekin kasallik ehtimoli "
            "hali ham oltidan bir. Sabab maxrajda."
        ),
        "body": """
<p>A <span class="cn-word" data-tr="skrining, ommaviy tekshiruv">screening</span> programme
tests ten thousand people for a condition that one person in a hundred actually has. The test is
good. It <span class="cn-word" data-tr="aniqlamoq">detects</span> ninety-nine percent of the
people who have the condition, and it wrongly returns a positive result for only five percent of
the people who do not.</p>

<p>Count the results. A hundred people have the condition, and ninety-nine of them test positive.
Nine thousand nine hundred people do not have it, and five percent of them — four hundred and
ninety-five people — test positive anyway.</p>

<p>So five hundred and ninety-four people receive a positive
<span class="cn-word" data-tr="natija">result</span>, and only ninety-nine of them are ill. If
you are one of those five hundred and ninety-four, your chance of having the condition is
ninety-nine out of five hundred and ninety-four — about one in
<span class="cn-word" data-tr="olti">six</span>.</p>

<p>Nothing here is a <span class="cn-word" data-tr="hiyla, aldov">trick</span>, and the test is
not bad. The number that surprises people comes from the
<span class="cn-word" data-tr="maxraj">denominator</span>. "Ninety-nine percent accurate"
describes the people who <span class="cn-word" data-tr="kasal">have</span> the condition.
Whether you have it, given a positive result, is a
<span class="cn-word" data-tr="butunlay">completely</span> different question, and its answer
depends on how <span class="cn-word" data-tr="kam tarqalgan">rare</span> the condition is.</p>

<p>The programme is still worth running. Before it, ten thousand people were <span class="cn-word" data-tr="tekshirilmagan">unexamined</span>; after it, the search has a manageable shape.</p>

<p>This is why a positive screening result is normally followed by a second, more
<span class="cn-word" data-tr="aniqroq">specific</span> test rather than by treatment. The first
test narrows ten thousand people down to six hundred. The second one is
<span class="cn-word" data-tr="ish">work</span> that only has to be done on six hundred.</p>
""",
        "grammar": [
            {"pattern": "detects ninety-nine percent of the people who have it",
             "meaning": "kasallar orasida 99 foizni aniqlaydi — shart kasallar"},
            {"pattern": "given a positive result",
             "meaning": "natija musbat boʻlsa — shart endi musbat chiqqanlar"},
            {"pattern": "the number comes from the denominator",
             "meaning": "javob maxrajdan chiqadi"},
        ],
        "questions": [
            {"text": "How many people receive a positive result in total?",
             "choices": ["Ninety-nine", "Four hundred and ninety-five",
                         "Five hundred and ninety-four", "One hundred"],
             "answer": 2,
             "explanation": "Toʻqson toʻqqiz haqiqiy kasal va toʻrt yuz toʻqson "
                            "besh sogʻlom — jami besh yuz toʻqson toʻrt."},
            {"text": "Why is the chance only about one in six?",
             "choices": ["The test is inaccurate",
                         "Most positive results come from the very large healthy group",
                         "The condition is not real",
                         "The sample was too small"],
             "answer": 1,
             "explanation": "Sogʻlomlar juda koʻp boʻlgani uchun ulardagi besh "
                            "foiz xato natija haqiqiy kasallar sonidan ancha "
                            "koʻp chiqadi."},
            {"text": "Why is a second test used?",
             "choices": ["The first test narrows ten thousand down to six hundred",
                         "The first test is worthless",
                         "Doctors prefer two opinions",
                         "The second test is cheaper"],
             "answer": 0,
             "explanation": "Birinchi test ishni keskin kamaytiradi, ikkinchisi "
                            "esa faqat olti yuz kishi ustida bajariladi."},
        ],
    },

    # ── 60 · the history of polling ──────────────────────────────────
    {
        "title": "Two Million Wrong Answers",
        "order": 60,
        "summary": (
            "Ikki milliondan ortiq javob toʻplagan soʻrov adashdi; ancha kichik, "
            "lekin toʻgʻri tanlangan soʻrov toʻgʻri chiqdi."
        ),
        "body": """
<p>In 1936 an American <span class="cn-word" data-tr="jurnal">magazine</span> ran what was, at
the time, the largest opinion <span class="cn-word" data-tr="soʻrov">poll</span> ever attempted.
It sent out millions of ballots and received more than two million replies, which is an
<span class="cn-word" data-tr="hayratlanarli">extraordinary</span> number even now. On that
basis it announced <span class="cn-word" data-tr="ishonch bilan">confidently</span> that the
challenger would win the presidential election.</p>

<p>He lost, and he lost by an enormous
<span class="cn-word" data-tr="farq">margin</span>. The magazine's
<span class="cn-word" data-tr="obroʻ">reputation</span> never recovered.</p>

<p>The <span class="cn-word" data-tr="sabab">reason</span> was not the size of the sample. It was
where the names had come from. The magazine had built its
<span class="cn-word" data-tr="roʻyxat">list</span> from telephone directories, car
<span class="cn-word" data-tr="roʻyxatga olish">registrations</span> and its own subscribers —
and in 1936, in the middle of a
<span class="cn-word" data-tr="iqtisodiy inqiroz">depression</span>, owning a telephone or a car
meant something about your <span class="cn-word" data-tr="daromad">income</span>. The two
million people who replied were a real and enormous group. They were simply not the
<span class="cn-word" data-tr="saylovchilar">electorate</span>.</p>

<p>There was a second problem underneath the first. Ballots were posted out, and the people who took the trouble to fill one in and post it back were not a random half of those who received one. Choosing to reply is itself a choice.</p>

<p>In the same year a young researcher named Gallup predicted the result correctly, using a
sample a small <span class="cn-word" data-tr="ulush">fraction</span> of the size, chosen to
<span class="cn-word" data-tr="aks ettirmoq">reflect</span> the country rather than to be as
large as possible.</p>

<p>The lesson has been taught in every statistics course since, in one sentence: a
<span class="cn-word" data-tr="ogʻishgan">biased</span> sample does not become less biased by
getting bigger. It only becomes more
<span class="cn-word" data-tr="ishonarli">convincing</span>.</p>
""",
        "grammar": [
            {"pattern": "on that basis it announced confidently",
             "meaning": "shunga asoslanib ishonch bilan eʼlon qildi"},
            {"pattern": "chosen to reflect the country",
             "meaning": "mamlakatni aks ettirish uchun tanlangan — vakillik"},
            {"pattern": "does not become less biased by getting bigger",
             "meaning": "kattalashgani bilan ogʻishi kamaymaydi"},
        ],
        "questions": [
            {"text": "How many replies did the magazine receive?",
             "choices": ["A few thousand", "More than two million",
                         "Ten thousand", "Fifty thousand"],
             "answer": 1,
             "explanation": "Matn buni aytadi — ikki milliondan ortiq javob, "
                            "hozir ham juda katta raqam."},
            {"text": "What was actually wrong with the poll?",
             "choices": ["The sample was too small",
                         "The questions were unclear",
                         "The names came from lists of wealthier households",
                         "The votes were counted incorrectly"],
             "answer": 2,
             "explanation": "Telefon, avtomobil va obuna roʻyxatlari 1936-yilda "
                            "daromad haqida maʼlumot berardi — tanlanma "
                            "ogʻishgan edi."},
            {"text": "What is the lesson in one sentence?",
             "choices": ["A biased sample does not improve by getting bigger",
                         "Large samples are always better",
                         "Polls should not be published",
                         "Telephone directories are unreliable"],
             "answer": 0,
             "explanation": "Matnning oxirgi jumlasi: ogʻishgan tanlanma "
                            "kattalashsa faqat ishonarliroq koʻrinadi, "
                            "toʻgʻriroq emas."},
        ],
    },
]
