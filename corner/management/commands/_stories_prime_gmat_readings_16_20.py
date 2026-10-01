# -*- coding: utf-8 -*-
"""Prime GMAT Readings — GMAT-16 … GMAT-20 (sets, then algebra).

The third leg of each Prime GMAT lesson: the lesson's maths doing real work in an
ENGLISH business text, with Uzbek cn-word glosses, an "Exam English" block and audio.
Rules: corner/management/commands/toc_prime_gmat_readings.txt (overrides STYLE_GUIDE_CORNER).

No algebraic notation in the body — quantities in English words and plain numbers.

Import, then audio (always pass --voice; odd orders Jenny, even orders Guy):
    python manage.py import_corner corner/management/commands/_stories_prime_gmat_readings_16_20.py --author=prime
    python manage.py gen_corner_audio --collection="Prime GMAT Readings" --only 16 --voice en-US-GuyNeural
    …
    python manage.py import_corner_audio corner/management/commands/audio/prime-gmat-readings --collection="Prime GMAT Readings"
"""

SUBJECT = {
    "name":    "Matematika",
    "summary": "Matematika: hayotdagi matnlar, atamalar va matematik hikoyalar.",
    "icon":    "bi-calculator",
    "color":   "#f59e0b",
    "order":   7,
}

COLLECTION = {
    "title":       "Prime GMAT Readings",
    "description": (
        "Prime GMAT darslarining oʻqish matnlari — ingliz tilida, audio bilan. Har bir matn "
        "biznes vaziyatida oʻz darsining matematikasini koʻrsatadi: inglizcha jumlani "
        "hisobga aylantirish — GMAT'ning asosiy koʻnikmasi."
    ),
    "order":       5,
}

STORIES = [

    # ── GMAT-16 — overlapping sets                                  [Guy]
    {
        "title":   "Two Lists, One Customer Base",
        "summary": "GMAT-16 matni. Bank ikki roʻyxatdagi mijozlarni sanaydi — ikkala xizmatdan foydalanadiganlar ikki marta sanalmasligi kerak.",
        "order":   16,
        "grammar": [
            {"pattern": "use both services",
             "meaning": "Ikkala xizmatdan ham foydalanadi — kesishma.",
             "examples": ["Two hundred and fifty customers use both services."]},
            {"pattern": "use neither",
             "meaning": "Hech biridan foydalanmaydi — ikkala roʻyxatdan tashqarida.",
             "examples": ["How many customers use neither the app nor the call centre?"]},
        ],
        "body": '''<p>A small bank in Tashkent has 1,200 <span class="cn-word" data-tr="mijozlar">customers</span>. Last month its marketing team wanted to send a <span class="cn-word" data-tr="bosma">printed</span> letter to every customer who had not yet tried either of the bank's two <span class="cn-word" data-tr="raqamli">digital</span> services: the mobile app and the telephone <span class="cn-word" data-tr="aloqa markazi">call centre</span>.</p>

<p>The team had two lists. The app list showed 700 customers. The call centre list showed 650. A junior <span class="cn-word" data-tr="tahlilchi">analyst</span> added the two numbers, got 1,350, and reported that every customer already used at least one service. "We have more users than customers," he said proudly. "No letters needed."</p>

<p>His manager, Lola, laughed. The two lists <span class="cn-word" data-tr="bir-birini qoplaydi">overlap</span>, she explained. A customer who <strong>uses both services</strong> appears on both lists and is counted twice. She asked the IT <span class="cn-word" data-tr="boʻlim">department</span> for one more number: how many customers were on both lists. The answer was 250.</p>

<p>Now the <span class="cn-word" data-tr="hisob-kitob">calculation</span> was simple. Seven hundred plus 650 is 1,350, but 250 of those people were counted twice, so only 1,100 different customers used at least one service. That left 100 customers who <strong>use neither</strong>. Those were the people who should receive the letter.</p>

<p>Lola went one step further. Of the 700 app users, 250 also called the centre, so 450 used only the app. Of the 650 callers, 400 used only the phone. The bank decided to send those 400 customers a short <span class="cn-word" data-tr="qoʻllanma">guide</span> to the app, because they were already comfortable with the bank but were paying for every call in time.</p>

<p>The letters cost very little. The lesson, Lola told her team, was free: before you add two lists, ask who is on both.</p>''',
        "questions": [
            {"text": "How many customers used neither service?",
             "choices": ["150", "100", "250"], "answer": 1,
             "explanation": "1,200 − (700 + 650 − 250) = <b>100</b>. 250 — ikkala xizmatdan foydalanuvchilar."},
            {"text": "How many customers used only the app?",
             "choices": ["450", "400", "700"], "answer": 0,
             "explanation": "700 − 250 = <b>450</b>. 400 — faqat qoʻngʻiroq qiladiganlar."},
            {"text": "Why was the analyst's total of 1,350 wrong?",
             "choices": ["Some customers had closed their accounts.", "The call centre list was out of date.", "Customers on both lists were counted twice."], "answer": 2,
             "explanation": "Ikkala roʻyxatdagi 250 mijoz <b>ikki marta</b> sanalgan."},
        ],
    },

    # ── GMAT-17 — a system of two equations                         [Jenny]
    {
        "title":   "The Price of a Ticket",
        "summary": "GMAT-17 matni. Xivadagi muzey bir kunda sotilgan chiptalarni kattalar va talabalarga ajratadi — ikki nomaʼlumli masala tenglamasiz yechiladi.",
        "order":   17,
        "grammar": [
            {"pattern": "a total of 300 tickets",
             "meaning": "Jami 300 ta chipta — birinchi tenglama (soni).",
             "examples": ["The museum sold a total of 300 tickets on Saturday."]},
            {"pattern": "brought in 3,780 dollars",
             "meaning": "3,780 dollar tushum keltirdi — ikkinchi tenglama (puli).",
             "examples": ["The tickets brought in 3,780 dollars."]},
        ],
        "body": '''<p>The history museum in Khiva sells two kinds of tickets: an adult ticket for 15 dollars and a student ticket for 9 dollars. On a busy Saturday in spring, the museum sold <strong>a total of 300 tickets</strong>, and the <span class="cn-word" data-tr="kassa">ticket office</span> <strong>brought in 3,780 dollars</strong>.</p>

<p>On Monday the <span class="cn-word" data-tr="viloyat">regional</span> tourism office asked a simple question: how many of Saturday's visitors were students? The museum's ticket machine had broken that morning, and the <span class="cn-word" data-tr="kassir">cashier</span> had written down only the two totals.</p>

<p>The <span class="cn-word" data-tr="muzey direktori">museum director</span>, Shohida, solved it without writing a single equation. Suppose, she said, that every one of the 300 visitors had been a student. Then the office would have taken 300 times 9, which is 2,700 dollars. But it actually took 3,780 dollars, which is 1,080 dollars more.</p>

<p>Each adult ticket costs 6 dollars more than a student ticket, so each adult adds 6 dollars to that <span class="cn-word" data-tr="taxminiy">imaginary</span> total. To explain an extra 1,080 dollars, there must have been 1,080 divided by 6, or 180 adults. The other 120 visitors were students.</p>

<p>She checked the answer before sending it. One hundred and eighty adults at 15 dollars bring in 2,700 dollars, and 120 students at 9 dollars bring in 1,080 dollars. Together that is 3,780 dollars, and together they are 300 people. Both <span class="cn-word" data-tr="shartlar">conditions</span> were met.</p>

<p>The tourism office used the figure to plan a student <span class="cn-word" data-tr="chegirma">discount</span> week in the autumn. Shohida, meanwhile, asked for the ticket machine to be <span class="cn-word" data-tr="taʼmirlamoq">repaired</span> and for the cashier to keep a separate <span class="cn-word" data-tr="hisob, roʻyxat">tally</span> of each kind of ticket. "Two totals can tell you two numbers," she said, "but only if you know how to ask them."</p>''',
        "questions": [
            {"text": "How many adult tickets did the museum sell on Saturday?",
             "choices": ["120", "150", "180"], "answer": 2,
             "explanation": "(3,780 − 2,700) ÷ 6 = <b>180</b>. 120 — talabalar."},
            {"text": "How much more does an adult ticket cost than a student ticket?",
             "choices": ["6 dollars", "9 dollars", "15 dollars"], "answer": 0,
             "explanation": "15 − 9 = <b>6 dollar</b> — har bir katta tasavvurdagi jamiga shuncha qoʻshadi."},
            {"text": "How did Shohida begin her solution?",
             "choices": ["She asked the cashier to count again.", "She imagined that every visitor was a student.", "She divided the total by 300."], "answer": 1,
             "explanation": "U <b>hammasi talaba</b> deb faraz qilib, ortiqcha pulni narx farqiga boʻlgan."},
        ],
    },

    # ── GMAT-18 — absolute value as tolerance                       [Guy]
    {
        "title":   "Within Four Millilitres",
        "summary": "GMAT-18 matni. Ichimlik zavodi shishalarni 500 ml dan 4 ml chetlanish bilan toʻldiradi — modul aslida «ruxsat etilgan chetlanish».",
        "order":   18,
        "grammar": [
            {"pattern": "within 4 millilitres of 500",
             "meaning": "500 dan 4 ml dan oshmagan farq — 496 dan 504 gacha.",
             "examples": ["Every bottle must be within 4 millilitres of 500."]},
            {"pattern": "no more than",
             "meaning": "… dan oshmasin — ≤ belgisi.",
             "examples": ["The error may be no more than 4 millilitres."]},
        ],
        "body": '''<p>A <span class="cn-word" data-tr="ichimliklar zavodi">bottling plant</span> outside Tashkent fills half-litre <span class="cn-word" data-tr="shishalar">bottles</span> of apple juice. No machine fills every bottle to exactly 500 millilitres, so the plant works with a <span class="cn-word" data-tr="ruxsat etilgan chetlanish">tolerance</span>: every bottle must be <strong>within 4 millilitres of 500</strong>. In other words, the error may be <strong>no more than</strong> 4 millilitres in either direction.</p>

<p>That rule describes a range with a centre. The lowest acceptable bottle holds 496 millilitres and the highest holds 504. A bottle of 496 is fine; a bottle of 495 is not. A bottle of 504 is fine; a bottle of 505 is not.</p>

<p>Every hour, the <span class="cn-word" data-tr="sifat nazoratchisi">quality inspector</span>, Farrux, takes five bottles from the line and measures them. On Tuesday morning the five readings were 497, 503, 505, 495 and 501. He did not compare each number with two limits. He asked one question instead: how far is this bottle from 500? The answers were 3, 3, 5, 5 and 1. Two bottles were more than 4 away, so two of the five were <span class="cn-word" data-tr="yaroqsiz deb topildi">rejected</span>.</p>

<p>Two failures in five is far too many, so Farrux stopped the line. The problem was a <span class="cn-word" data-tr="eskirgan">worn</span> <span class="cn-word" data-tr="klapan">valve</span> that sometimes let too much juice through and sometimes too little. Notice that one bad bottle was over the limit and one was under it: the machine was not filling too much or too little, it was filling <span class="cn-word" data-tr="beqaror">unevenly</span>.</p>

<p>After the valve was replaced, the next sample read 499, 502, 500, 498 and 501. Every bottle was within 2 millilitres of the <span class="cn-word" data-tr="maqsad qiymat">target</span>, well inside the tolerance, and the line started again.</p>''',
        "questions": [
            {"text": "What is the smallest amount an acceptable bottle can hold?",
             "choices": ["495 millilitres", "496 millilitres", "500 millilitres"], "answer": 1,
             "explanation": "500 − 4 = <b>496</b>. 495 — chegaradan 5 ml uzoq."},
            {"text": "How many of the five bottles in Tuesday's first sample were rejected?",
             "choices": ["2", "1", "3"], "answer": 0,
             "explanation": "505 va 495 — 500 dan 5 ml uzoq: <b>2</b> ta."},
            {"text": "What did the two rejected bottles show about the machine?",
             "choices": ["It always filled too much.", "It always filled too little.", "It filled unevenly, sometimes too much and sometimes too little."], "answer": 2,
             "explanation": "Biri chegaradan yuqori, biri past — mashina <b>beqaror</b> toʻldirgan."},
        ],
    },

    # ── GMAT-19 — revenue as a quadratic                            [Jenny]
    {
        "title":   "The Price That Earns the Most",
        "summary": "GMAT-19 matni. Novvoy tort narxini oshirgan sari kamroq sotadi — eng koʻp tushum beradigan narx ikki «teng» narxning oʻrtasida.",
        "order":   19,
        "grammar": [
            {"pattern": "for every dollar she raised the price",
             "meaning": "Narxni har bir dollarga oshirganda — bir xil qadamli oʻzgarish.",
             "examples": ["For every dollar she raised the price, she sold one cake fewer."]},
            {"pattern": "brought in the most money",
             "meaning": "Eng koʻp pul keltirdi — eng katta tushum.",
             "examples": ["Which price brought in the most money?"]},
        ],
        "body": '''<p>Munisa bakes <span class="cn-word" data-tr="tortlar">cakes</span> to order in Samarkand. For a year she charged 10 dollars a cake and sold about 30 cakes a week, which brought in 300 dollars. When the price of <span class="cn-word" data-tr="un">flour</span> and <span class="cn-word" data-tr="sariyogʻ">butter</span> rose, she wondered whether she should raise her own price, and by how much.</p>

<p>She had kept careful <span class="cn-word" data-tr="yozuvlar">records</span>. Over several months of small changes, she noticed a pattern: <strong>for every dollar she raised the price</strong>, she sold one cake fewer each week. At 11 dollars she sold 29 cakes; at 12 dollars, 28.</p>

<p>She made a small table on the back of an order <span class="cn-word" data-tr="blank">form</span>. At 10 dollars, 30 cakes bring in 300 dollars. At 20 dollars, 20 cakes bring in 400 dollars. At 30 dollars, only 10 cakes sell, and the <span class="cn-word" data-tr="tushum">revenue</span> falls back to 300 dollars.</p>

<p>The table surprised her. Prices of 10 dollars and 30 dollars bring in exactly the same money, one by selling many cheap cakes and the other by selling a few expensive ones. The price that <strong>brought in the most money</strong> was 20 dollars, exactly halfway between them. Her son, who was studying for a business exam, explained why: the revenue rises and then falls in a <span class="cn-word" data-tr="simmetrik">symmetrical</span> curve, so its highest point always sits midway between two prices that give the same result.</p>

<p>Munisa did not jump straight to 20 dollars. She raised the price to 16 dollars first, to see whether her <span class="cn-word" data-tr="doimiy mijozlar">regular customers</span> would stay. They did, and revenue rose to 384 dollars a week. A month later she moved to 20, and the pattern held.</p>

<p>Better still, she now baked 20 cakes a week instead of 30, so her <span class="cn-word" data-tr="xarajatlar">costs</span> fell while her revenue rose.</p>''',
        "questions": [
            {"text": "Which price brought in the most money each week?",
             "choices": ["10 dollars", "30 dollars", "20 dollars"], "answer": 2,
             "explanation": "20 × 20 = <b>400</b> dollar — 10 va 30 dollarning oʻrtasi."},
            {"text": "How much revenue did a price of 30 dollars bring in?",
             "choices": ["300 dollars", "400 dollars", "900 dollars"], "answer": 0,
             "explanation": "30 dollarda 10 ta tort: <b>300 dollar</b>. 900 — 30 ta tort deb hisoblangan."},
            {"text": "How many cakes a week did Munisa sell at 16 dollars?",
             "choices": ["16", "24", "30"], "answer": 1,
             "explanation": "10 dollardan 6 dollar yuqori — 6 ta kam: <b>24</b> ta; 24 × 16 = 384."},
        ],
    },

    # ── GMAT-20 — a fare function                                    [Guy]
    {
        "title":   "A Formula for the Fare",
        "summary": "GMAT-20 matni. Taksi kompaniyasining narx formulasi bilan raqobatchi ilovaning formulasini solishtirish — qaysi masofada ikkalasi teng?",
        "order":   20,
        "grammar": [
            {"pattern": "a starting fee plus a charge per kilometre",
             "meaning": "Boshlangʻich toʻlov va har kilometr uchun haq — doimiy qism + oʻzgaruvchi qism.",
             "examples": ["The fare is a starting fee plus a charge per kilometre."]},
            {"pattern": "the two fares are equal",
             "meaning": "Ikki narx teng — ikki formulani tenglashtirish.",
             "examples": ["At five kilometres the two fares are equal."]},
        ],
        "body": '''<p>A taxi company in Tashkent sets its prices with a simple <span class="cn-word" data-tr="formula">formula</span>: <strong>a starting fee plus a charge per kilometre</strong>. The starting fee is 2 dollars and 50 cents, and every kilometre adds 1 dollar and 20 cents. A 15-kilometre ride from the airport to the city centre therefore costs 2.50 plus 18, which is 20 dollars and 50 cents.</p>

<p>Last year a new <span class="cn-word" data-tr="taksi chaqirish">ride-hailing</span> app arrived with a different <span class="cn-word" data-tr="tarif">tariff</span>: no starting fee at all, but 1 dollar and 70 cents for every kilometre. Its advertisements claimed the app was "always cheaper". The taxi company's manager, Akmal, did not believe it, so he compared the two formulas.</p>

<p>On a short ride the app does look cheaper, because it has no starting fee. On a 2-kilometre ride the app charges 3.40 dollars and the taxi charges 4.90. But the app's price per kilometre is 50 cents higher, so every kilometre <span class="cn-word" data-tr="qisqartiradi">closes the gap</span> by 50 cents. The taxi's <span class="cn-word" data-tr="oldinlik, ustunlik">head start</span> of 2.50 dollars disappears after 5 kilometres. At that distance <strong>the two fares are equal</strong>: 8.50 dollars each.</p>

<p>Beyond 5 kilometres, the taxi is cheaper, and the difference grows with every kilometre. On a 10-kilometre trip the taxi charges 14.50 dollars and the app charges 17. On the airport run the app would cost 25.50 dollars, five dollars more than the taxi.</p>

<p>Akmal printed a small card for his <span class="cn-word" data-tr="haydovchilar">drivers</span> with three lines: under 5 kilometres, the app is cheaper; at 5, they are equal; over 5, the taxi wins. Most <span class="cn-word" data-tr="aeroport">airport</span> passengers, he noticed, travel more than 5 kilometres.</p>

<p>The company's next <span class="cn-word" data-tr="reklama">advertisement</span> did not attack the app. It simply showed the price of the airport ride, side by side.</p>''',
        "questions": [
            {"text": "What does the taxi charge for a 15-kilometre ride?",
             "choices": ["18 dollars", "20 dollars and 50 cents", "25 dollars and 50 cents"], "answer": 1,
             "explanation": "2.50 + 15 × 1.20 = <b>20.50</b> dollar. 25.50 — ilovaning narxi."},
            {"text": "At what distance do the two fares become equal?",
             "choices": ["5 kilometres", "2 kilometres", "10 kilometres"], "answer": 0,
             "explanation": "2.50 ÷ 0.50 = <b>5 km</b>: ikkalasi ham 8.50 dollar."},
            {"text": "Which service is cheaper for a 10-kilometre trip?",
             "choices": ["The app", "Both cost the same", "The taxi"], "answer": 2,
             "explanation": "Taksi 14.50, ilova 17 dollar — 5 km dan keyin <b>taksi</b> arzon."},
        ],
    },
]
