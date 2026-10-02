# -*- coding: utf-8 -*-
"""Prime GMAT Readings — GMAT-26 … GMAT-30 (Data Sufficiency).

The third leg of each Prime GMAT lesson: the lesson's idea doing real work in an ENGLISH
business text, with Uzbek cn-word glosses, an "Exam English" block and audio. For Data
Sufficiency the idea is a manager's question: "Is this information enough to decide?"
Rules: corner/management/commands/toc_prime_gmat_readings.txt.

Import, then audio (always pass --voice; odd orders Jenny, even orders Guy):
    python manage.py import_corner corner/management/commands/_stories_prime_gmat_readings_26_30.py --author=prime
    python manage.py gen_corner_audio --collection="Prime GMAT Readings" --only 26 --voice en-US-GuyNeural
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

    # ── GMAT-26 — is it enough?                                     [Guy]
    {
        "title":   "Enough to Decide",
        "summary": "GMAT-26 matni. Logistika kompaniyasi rahbari hisob-kitobdan oldin bitta savol beradi: «bu maʼlumot javob uchun yetarlimi?»",
        "order":   26,
        "grammar": [
            {"pattern": "Is that enough to answer the question?",
             "meaning": "Bu savolga javob berish uchun yetarlimi? — Data Sufficiency'ning asosiy savoli.",
             "examples": ["Before you calculate anything, ask: is that enough to answer the question?"]},
            {"pattern": "on its own",
             "meaning": "Yolgʻiz, boshqasisiz — DS'dagi «alone».",
             "examples": ["Neither fact answers the question on its own."]},
        ],
        "body": '''<p>Rustam manages a <span class="cn-word" data-tr="logistika">logistics</span> company in Tashkent. One Monday the <span class="cn-word" data-tr="direktorlar kengashi">board</span> asked him a simple question: how many trucks did the company use last month?</p>

<p>His <span class="cn-word" data-tr="tahlilchi">analyst</span>, Sevara, came back with two facts. The first was the total fuel bill for the month: 36,000 dollars. The second was the fuel cost of a single truck for the month: 1,800 dollars, the same for every truck.</p>

<p>Rustam did not reach for a calculator. He asked a different question first: <strong>is that enough to answer the question?</strong> The total bill alone was not enough, because the same bill could come from twenty trucks or from forty trucks that drove less. The cost of one truck alone was not enough either, because it said nothing about how many trucks there were. Neither fact answered the question <strong>on its own</strong>.</p>

<p>Together, however, the two facts were enough. If the whole fleet cost 36,000 dollars and each truck cost 1,800, the company had used 20 trucks. Only then did Rustam do the <span class="cn-word" data-tr="boʻlish">division</span>.</p>

<p>A week later the board asked a second question: what was the average fuel cost per truck? This time Rustam answered at once. Sevara's second fact already said that every truck cost 1,800 dollars, so the average was 1,800. The total bill was not needed at all.</p>

<p>Rustam explained his habit to a new <span class="cn-word" data-tr="stajyor">trainee</span>. Collecting data costs time and money, he said, and in a busy week nobody wants a report that cannot answer the question it was written for. So he always asks which facts are <span class="cn-word" data-tr="zarur">necessary</span> before he asks anyone to find them. The GMAT, he added, tests exactly this <span class="cn-word" data-tr="koʻnikma">skill</span>, and calls it Data <span class="cn-word" data-tr="yetarlilik">Sufficiency</span>.</p>''',
        "questions": [
            {"text": "How many trucks did the company use last month?",
             "choices": ["18", "20", "36"], "answer": 1,
             "explanation": "36,000 ÷ 1,800 = <b>20</b> — ikkala maʼlumot birga kerak boʻldi."},
            {"text": "Which fact alone answered the board's second question about the average cost per truck?",
             "choices": ["The cost of one truck", "The total fuel bill", "Neither fact"], "answer": 0,
             "explanation": "Har bir yuk mashinasi 1,800 dollar — oʻrtacha ham <b>1,800</b>; jami hisob kerak emas."},
            {"text": "Why was the total fuel bill alone not enough to find the number of trucks?",
             "choices": ["It was paid late.", "It did not include drivers' wages.", "The same total could come from different numbers of trucks."], "answer": 2,
             "explanation": "Bir xil jami summa har xil miqdordagi mashinalardan chiqishi mumkin — <b>yagona javob yoʻq</b>."},
        ],
    },

    # ── GMAT-27 — one value or two                                  [Jenny]
    {
        "title":   "One Number or Two?",
        "summary": "GMAT-27 matni. Konsultant «tushum 300 dollar edi» deydi — lekin bu narxni aniqlash uchun yetarli emas: ikki xil narx bir xil tushum beradi.",
        "order":   27,
        "grammar": [
            {"pattern": "There are two possible prices.",
             "meaning": "Ikki xil narx boʻlishi mumkin — demak qiymat yagona emas, maʼlumot yetarli emas.",
             "examples": ["Revenue of 300 dollars fits two possible prices."]},
            {"pattern": "rules out",
             "meaning": "… ni istisno qiladi, chiqarib tashlaydi.",
             "examples": ["The second fact rules out the higher price."]},
        ],
        "body": '''<p>Madina owns a small <span class="cn-word" data-tr="qandolatxona">patisserie</span> in Samarkand. Over the years she has noticed a steady <span class="cn-word" data-tr="qonuniyat">pattern</span>: when she charges ten dollars for a cake, she sells thirty cakes a week, and for every dollar she adds to the price she sells one cake fewer.</p>

<p>She hired a <span class="cn-word" data-tr="maslahatchi">consultant</span> to review last month's <span class="cn-word" data-tr="hisob yozuvlari">records</span>, which a new <span class="cn-word" data-tr="kassir">cashier</span> had kept badly. The consultant's report had one line about cakes: weekly revenue from cakes was 300 dollars. Madina wanted to know what price the cashier had actually charged.</p>

<p>The answer was not as simple as it looked. At ten dollars she sells thirty cakes, which brings in 300 dollars. But at thirty dollars she sells only ten cakes, and that also brings in 300 dollars. <strong>There are two possible prices.</strong> The report's line, true as it was, could not tell her which one had been used.</p>

<p>Madina's daughter, who was preparing for the GMAT, recognised the situation at once. "In a value question," she said, "information is sufficient only if it gives exactly one value. Two prices means not sufficient, even if both are correct."</p>

<p>They looked for a second fact. The cashier's <span class="cn-word" data-tr="smena daftari">shift notes</span> showed that no cake had been priced above twenty dollars that month. That single line <strong>rules out</strong> the higher price. Together with the report, it left only one answer: ten dollars.</p>

<p>Madina added a column for prices to her <span class="cn-word" data-tr="jadval">spreadsheet</span> the same day. A total, she realised, hides the <span class="cn-word" data-tr="tafsilotlar">details</span> that produced it, and the same total can come from very different <span class="cn-word" data-tr="qarorlar">decisions</span>.</p>''',
        "questions": [
            {"text": "Which two prices give weekly cake revenue of 300 dollars?",
             "choices": ["10 dollars and 30 dollars", "15 dollars and 20 dollars", "10 dollars and 20 dollars"], "answer": 0,
             "explanation": "10 × 30 = 300 va 30 × 10 = 300 — <b>ikki</b> narx."},
            {"text": "What price had the cashier charged?",
             "choices": ["30 dollars", "20 dollars", "10 dollars"], "answer": 2,
             "explanation": "Smena yozuvlari 20 dollardan yuqori narxni istisno qildi — <b>10 dollar</b>."},
            {"text": "Why was the consultant's line about revenue not sufficient on its own?",
             "choices": ["It was written by a new cashier.", "It fitted two different prices.", "It gave monthly, not weekly, figures."], "answer": 1,
             "explanation": "Yetarli boʻlishi uchun <b>yagona</b> qiymat kerak edi."},
        ],
    },

    # ── GMAT-28 — a definite no is an answer                        [Guy]
    {
        "title":   "A Definite No",
        "summary": "GMAT-28 matni. Yosh kredit mutaxassisi «javob yoʻq» chiqqanini «maʼlumot yetarli emas» deb oʻylaydi — aslida aniq «yoʻq» ham toʻliq javob.",
        "order":   28,
        "grammar": [
            {"pattern": "Does the applicant qualify?",
             "meaning": "Arizachi talabga javob beradimi? — ha/yoʻq savoli.",
             "examples": ["The question was simple: does the applicant qualify?"]},
            {"pattern": "a definite answer",
             "meaning": "Aniq javob — «ha» ham, «yoʻq» ham boʻlishi mumkin.",
             "examples": ["A clear no is a definite answer."]},
        ],
        "body": '''<p>Kamron started work as a loan officer at a bank in Namangan in September. The bank had one main rule for small <span class="cn-word" data-tr="kreditlar">loans</span>: the monthly <span class="cn-word" data-tr="toʻlov">payment</span> must be less than 40 percent of the applicant's monthly <span class="cn-word" data-tr="daromad">income</span>.</p>

<p>His first file was a <span class="cn-word" data-tr="doʻkondor">shopkeeper</span> who wanted a loan with a monthly payment of 900 dollars. The question on the form was simple: <strong>does the applicant qualify?</strong> The file contained one more fact: the shopkeeper's income was exactly 2,000 dollars a month.</p>

<p>Kamron did the arithmetic. Nine hundred out of two thousand is 45 percent, which is above the limit. He wrote "information insufficient" on the file and asked the shopkeeper for more <span class="cn-word" data-tr="hujjatlar">documents</span>.</p>

<p>His <span class="cn-word" data-tr="rahbar">supervisor</span>, Gulnoza, returned the file the same afternoon. "The information was sufficient," she said. "You have <strong>a definite answer</strong>. It is no." Kamron had confused two different things: an answer he did not like and an answer he did not have.</p>

<p>She showed him a case that really was insufficient. Another applicant wanted a payment of 900 dollars and had written only that his income was "more than 2,000 dollars". If he earned 2,100, the payment was about 43 percent and he did not qualify. If he earned 3,000, it was 30 percent and he did. The same facts allowed both a yes and a no, so more information was truly needed.</p>

<p>Kamron kept that <span class="cn-word" data-tr="farq">distinction</span> on a card on his desk. Information is sufficient when every <span class="cn-word" data-tr="mumkin boʻlgan">possible</span> case gives the same answer, whether that answer is yes or no. It is insufficient only when the facts still leave room for both. The shopkeeper, meanwhile, received a polite letter and an offer of a smaller loan he could <span class="cn-word" data-tr="koʻtara oladi">afford</span>.</p>''',
        "questions": [
            {"text": "What share of the shopkeeper's income would the monthly payment be?",
             "choices": ["40 percent", "45 percent", "30 percent"], "answer": 1,
             "explanation": "900 ÷ 2,000 = <b>45%</b> — chegaradan yuqori."},
            {"text": "Why did Gulnoza say the information on the first file was sufficient?",
             "choices": ["It gave a definite answer: the applicant did not qualify.", "The shopkeeper had brought extra documents.", "The bank's rule had changed."], "answer": 0,
             "explanation": "Aniq «<b>yoʻq</b>» — toʻliq javob, yetarli maʼlumot."},
            {"text": "Why was the second applicant's information truly insufficient?",
             "choices": ["His payment was too high.", "He gave no income at all.", "His income could give either a yes or a no."], "answer": 2,
             "explanation": "«2,000 dan koʻp» — 2,100 da «yoʻq», 3,000 da «ha»: <b>ikkala javob</b> ham mumkin."},
        ],
    },

    # ── GMAT-29 — the same information twice                       [Jenny]
    {
        "title":   "The Second Report Said Nothing New",
        "summary": "GMAT-29 matni. Xarid boʻlimi ikki hisobot oladi — ikkinchisi birinchisining ikki baravari boʻlib chiqadi va hech qanday yangi maʼlumot bermaydi.",
        "order":   29,
        "grammar": [
            {"pattern": "exactly twice the first",
             "meaning": "Birinchisining aynan ikki baravari — yangi maʼlumot emas.",
             "examples": ["Every number in the second report was exactly twice the first."]},
            {"pattern": "a genuinely new fact",
             "meaning": "Haqiqatan yangi maʼlumot — mustaqil tenglama.",
             "examples": ["To find both prices, she needed a genuinely new fact."]},
        ],
        "body": '''<p>Feruza works in the <span class="cn-word" data-tr="xarid boʻlimi">purchasing department</span> of a hotel chain in Bukhara. She was asked to find the price of one box of printer paper from a new <span class="cn-word" data-tr="yetkazib beruvchi">supplier</span>, who sold paper and ink only in mixed orders.</p>

<p>The first report from the supplier said that an order of three boxes of paper and two <span class="cn-word" data-tr="kartrijlar">cartridges</span> of ink had cost 13 dollars. That was one <span class="cn-word" data-tr="tenglama">equation</span> with two unknown prices, so it could not give either price alone.</p>

<p>A second report arrived the next day, and her <span class="cn-word" data-tr="hamkasb">colleague</span> was delighted. "Now we have two equations," he said, "so we can solve for both prices." The second report said that six boxes of paper and four cartridges had cost 26 dollars.</p>

<p>Feruza looked more carefully. Every number in the second report was <strong>exactly twice the first</strong>. It described the same <span class="cn-word" data-tr="nisbat">proportion</span> of paper to ink, at the same prices, simply doubled. It was not a second piece of information at all, only the first one written again, and two copies of one fact leave the prices just as unknown as before.</p>

<p>To find both prices, she needed <strong>a genuinely new fact</strong>, one that described a different <span class="cn-word" data-tr="aralashma">mix</span>. She telephoned the supplier and asked for the price of ink on its own. The answer was two dollars a cartridge. Now the first report was enough: two cartridges cost four dollars, so three boxes of paper cost nine dollars, and one box cost three.</p>

<p>Her colleague asked how she had spotted it so quickly. "When two statements look different," she said, "divide one by the other. If every number <span class="cn-word" data-tr="qisqaradi">cancels</span> to the same ratio, they are the same statement in different <span class="cn-word" data-tr="kiyim">clothes</span>."</p>''',
        "questions": [
            {"text": "Why did the second report add no new information?",
             "choices": ["It was sent by a different supplier.", "Every number in it was exactly twice the first report.", "It gave prices in a different currency."], "answer": 1,
             "explanation": "Ikkinchi hisobot — birinchisining <b>ikki baravari</b>, mustaqil tenglama emas."},
            {"text": "What was the price of one box of printer paper?",
             "choices": ["2 dollars", "4 dollars", "3 dollars"], "answer": 2,
             "explanation": "13 − 2 × 2 = 9; 9 ÷ 3 = <b>3 dollar</b>."},
            {"text": "What kind of fact did Feruza need to find both prices?",
             "choices": ["One that described a different mix of paper and ink", "A third copy of the first report", "The supplier's total sales for the year"], "answer": 0,
             "explanation": "Mustaqil maʼlumot — <b>boshqa aralashma</b> yoki bitta narxning oʻzi."},
        ],
    },

    # ── GMAT-30 — percent change needs no base                      [Guy]
    {
        "title":   "What the Board Needed to Know",
        "summary": "GMAT-30 matni. Direktorlar kengashi tushumning foiz oʻzgarishini soʻraydi — moliya boʻlimi esa haqiqiy summani izlab vaqt yoʻqotadi. Foiz oʻzgarishi uchun baza kerak emas.",
        "order":   30,
        "grammar": [
            {"pattern": "by what percent did revenue change",
             "meaning": "Tushum necha foizga oʻzgardi — nisbat soʻralmoqda, summa emas.",
             "examples": ["The board asked by what percent revenue had changed."]},
            {"pattern": "regardless of",
             "meaning": "… ga qaramay, … dan qatʼi nazar.",
             "examples": ["The answer is the same regardless of last year's revenue."]},
        ],
        "body": '''<p>The <span class="cn-word" data-tr="direktorlar kengashi">board</span> of a <span class="cn-word" data-tr="roʻzgʻor buyumlari">household-goods</span> company in Tashkent met on a Friday afternoon. One director asked a short question about the company's most popular kettle: <strong>by what percent did revenue change</strong> from last year to this year?</p>

<p>The <span class="cn-word" data-tr="moliya boʻlimi">finance team</span> had two facts ready. First, the kettle's price had risen by 10 percent. Second, the number of kettles sold had fallen by 10 percent. A young <span class="cn-word" data-tr="tahlilchi">analyst</span> said they could not answer yet: they would need last year's actual revenue, and the <span class="cn-word" data-tr="buxgalteriya">accounts</span> department had gone home.</p>

<p>The finance director, Shahzod, disagreed. Revenue is price times quantity, he explained. If the price is multiplied by one point one and the quantity by zero point nine, revenue is multiplied by zero point nine nine. That is a fall of one percent, <strong>regardless of</strong> whether last year's revenue was fifty thousand dollars or five million.</p>

<p>The young analyst still thought the actual figure would help. Shahzod agreed that the board might want it for other reasons, but not for this question. A percent change compares two numbers; it does not need either of them, only the <span class="cn-word" data-tr="koʻpaytuvchilar">factors</span> that turn one into the other.</p>

<p>The board had its answer before the coffee arrived: revenue from the kettle had fallen by about one percent. The <span class="cn-word" data-tr="yuqori narx">higher price</span> had not quite made up for the lost <span class="cn-word" data-tr="sotuvlar">sales</span>.</p>

<p>The director who had asked the question added one more. "If we had raised the price by 10 percent and sold the same number, what then?" This time even the young analyst answered without hesitating: a ten percent rise, and still no need for last year's figure. The meeting moved on to the next <span class="cn-word" data-tr="kun tartibi bandi">item</span>.</p>''',
        "questions": [
            {"text": "By what percent did revenue from the kettle change?",
             "choices": ["It stayed the same.", "It fell by about 1 percent.", "It rose by about 1 percent."], "answer": 1,
             "explanation": "1.1 × 0.9 = 0.99 — taxminan <b>1% kamaydi</b>."},
            {"text": "Why did Shahzod not need last year's actual revenue?",
             "choices": ["A percent change depends only on the factors, not on the base.", "The board already knew the figure.", "The accounts department sent it by email."], "answer": 0,
             "explanation": "Foiz oʻzgarishi — <b>nisbat</b>; baza qisqarib ketadi."},
            {"text": "What would revenue have done with a 10 percent price rise and unchanged sales?",
             "choices": ["Fallen by 1 percent", "Stayed the same", "Risen by 10 percent"], "answer": 2,
             "explanation": "1.1 × 1 = 1.1 — <b>10% oshish</b>."},
        ],
    },
]
