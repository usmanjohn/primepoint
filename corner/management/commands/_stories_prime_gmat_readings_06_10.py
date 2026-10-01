# -*- coding: utf-8 -*-
"""Prime GMAT Readings — GMAT-6 … GMAT-10.

The third leg of each Prime GMAT lesson: the lesson's maths doing real work in an
ENGLISH business text, with Uzbek cn-word glosses, an "Exam English" block and audio.
Rules: corner/management/commands/toc_prime_gmat_readings.txt (overrides STYLE_GUIDE_CORNER).

No algebraic notation in the body — quantities in English words and plain numbers.

Import, then audio (always pass --voice; odd orders Jenny, even orders Guy):
    python manage.py import_corner corner/management/commands/_stories_prime_gmat_readings_06_10.py --author=prime
    python manage.py gen_corner_audio --collection="Prime GMAT Readings" --only 6 --voice en-US-GuyNeural
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

    # ── GMAT-6 — fractions of a budget                            [Guy]
    {
        "title":   "Three-Eighths of the Budget",
        "summary": "GMAT-6 matni. Marketing boʻlimi byudjetni kasrlarga boʻladi — qolgan zaxira beshdan bir qismdan katta-kichikligi kalkulyatorsiz aniqlanadi.",
        "order":   6,
        "grammar": [
            {"pattern": "three-eighths of the budget",
             "meaning": "Byudjetning sakkizdan uch qismi — <b>of</b> koʻpaytirishni bildiradi.",
             "examples": ["Three-eighths of the budget went to online advertising."]},
            {"pattern": "what is left / the remainder",
             "meaning": "Qolgan qism — butundan sarflangan kasrlar ayiriladi.",
             "examples": ["What is left goes into a reserve."]},
            {"pattern": "more than one fifth",
             "meaning": "Beshdan bir qismdan koʻp — ikki kasrni solishtirish.",
             "examples": ["Is the reserve more than one fifth of the budget?"]},
        ],
        "body": '''<p>Every January, the <span class="cn-word" data-tr="marketing boʻlimi">marketing department</span> of a furniture company in Tashkent receives its <span class="cn-word" data-tr="yillik">annual</span> budget of 24,000 dollars. This year its head, Nodira, divided it on a single sheet of paper.</p>

<p><strong>Three-eighths of the budget</strong> went to online <span class="cn-word" data-tr="reklama">advertising</span>. She did not need a calculator: one eighth of 24,000 is 3,000, so three-eighths is 9,000 dollars. One quarter went to printing <span class="cn-word" data-tr="katalog">catalogues</span>, which is 6,000 dollars. One sixth went to two <span class="cn-word" data-tr="koʻrgazma">trade fairs</span>, which is 4,000 dollars.</p>

<p><strong>What is left</strong> goes into a <span class="cn-word" data-tr="zaxira">reserve</span> for surprises. Nodira added the three amounts: 9,000, 6,000 and 4,000 make 19,000, so the reserve was 5,000 dollars, or five twenty-fourths of the budget.</p>

<p>The <span class="cn-word" data-tr="moliya direktori">finance director</span> had one rule: the reserve must be <strong>more than one fifth</strong> of the budget. One fifth of 24,000 is 4,800, and 5,000 is larger, so the plan passed. Nodira noticed how narrow the <span class="cn-word" data-tr="farq, oraliq">margin</span> was. If printing had taken one third instead of one quarter, the reserve would have <span class="cn-word" data-tr="yoʻqolib ketmoq">disappeared</span> completely.</p>

<p>She kept the sheet on her desk all year. Whenever a <span class="cn-word" data-tr="yetkazib beruvchi">supplier</span> asked for more money, she looked at the fractions first and the dollars second. "A fraction tells you how big a piece is," she told a new colleague. "A dollar figure only tells you how big it looks."</p>''',
        "questions": [
            {"text": "How much did the department spend on online advertising?",
             "choices": ["$6,000", "$9,000", "$3,000"], "answer": 1,
             "explanation": "24,000 ÷ 8 = 3,000; uch qismi <b>$9,000</b>. $3,000 — sakkizdan bir qism."},
            {"text": "How much money went into the reserve?",
             "choices": ["$5,000", "$4,800", "$4,000"], "answer": 0,
             "explanation": "24,000 − 9,000 − 6,000 − 4,000 = <b>$5,000</b>. $4,800 — byudjetning beshdan bir qismi, yaʼni chegara."},
            {"text": "Why did the plan pass the finance director's rule?",
             "choices": ["The reserve was exactly one quarter of the budget.", "Printing took one third of the budget.", "The reserve was larger than one fifth of the budget."], "answer": 2,
             "explanation": "Zaxira 5,000 — beshdan bir qism (4,800) dan <b>katta</b>."},
        ],
    },

    # ── GMAT-7 — remainders in packing and schedules              [Jenny]
    {
        "title":   "The Bottles That Did Not Fit",
        "summary": "GMAT-7 matni. Ombor 1,000 ta shishani qutilarga joylaydi va yetkazib berish kunlarini rejalashtiradi — ikkala savolga ham qoldiq javob beradi.",
        "order":   7,
        "grammar": [
            {"pattern": "left over",
             "meaning": "Ortib qolgan — boʻlishdagi <b>qoldiq</b>.",
             "examples": ["Sixteen bottles were left over."]},
            {"pattern": "every 9 days",
             "meaning": "Har 9 kunda — hafta kunini topish uchun 7 ga boʻlib, qoldiqni olamiz.",
             "examples": ["A truck arrives every 9 days."]},
        ],
        "body": '''<p>A <span class="cn-word" data-tr="mineral suv">mineral water</span> plant near Namangan received an order for 1,000 bottles. The <span class="cn-word" data-tr="shishalar">bottles</span> are packed 24 to a <span class="cn-word" data-tr="karton quti">carton</span>, and the customer, a hotel chain, accepts only full cartons.</p>

<p>Bekzod, the packing supervisor, divided 1,000 by 24 in his head. Forty cartons hold 960 bottles, and one more carton makes 984. That left 16 bottles <strong>left over</strong>, not enough for another carton. He had two choices: send 984 bottles and explain the <span class="cn-word" data-tr="kamomad">shortfall</span>, or add 8 bottles from the next batch and send 42 full cartons. He called the hotel, and the <span class="cn-word" data-tr="xarid boʻyicha menejer">purchasing manager</span> agreed to take 1,008 bottles.</p>

<p>The second problem was the <span class="cn-word" data-tr="jadval">schedule</span>. The hotel wanted a delivery <strong>every 9 days</strong>, and the first truck would leave on a Monday. The drivers do not work on Sundays, so Bekzod needed to know which day each delivery would fall on.</p>

<p>He did not open a calendar. Nine days is one week and two days, so each delivery moves two days later in the week: Monday, then Wednesday, then Friday, then Sunday. The fourth delivery fell on a Sunday, the drivers' <span class="cn-word" data-tr="dam olish kuni">day off</span>. The fifth would come 36 days after the first, and 36 days is five weeks and one day, so it would fall on a Tuesday.</p>

<p>Bekzod moved the fourth delivery to Saturday and wrote a short note for the planning office: "Whenever a period is not a whole number of weeks, check the <span class="cn-word" data-tr="qoldiq">remainder</span> before you promise a date."</p>''',
        "questions": [
            {"text": "How many bottles were left over after the full cartons were packed?",
             "choices": ["8", "16", "24"], "answer": 1,
             "explanation": "24 × 41 = 984; 1,000 − 984 = <b>16</b>. 8 — qutini toʻldirish uchun yetishmagan shishalar."},
            {"text": "On what day of the week would the fifth delivery fall?",
             "choices": ["Monday", "Sunday", "Tuesday"], "answer": 2,
             "explanation": "36 kun = 5 hafta va 1 kun: dushanba + 1 = <b>seshanba</b>."},
            {"text": "Why did Bekzod move the fourth delivery?",
             "choices": ["It fell on a Sunday, when the drivers do not work.", "The hotel asked for an earlier date.", "The cartons were not full."], "answer": 0,
             "explanation": "Toʻrtinchi yetkazib berish <b>yakshanbaga</b> toʻgʻri kelgan — haydovchilarning dam olish kuni."},
        ],
    },

    # ── GMAT-8 — exponential growth                                [Guy]
    {
        "title":   "Doubling Every Year",
        "summary": "GMAT-8 matni. Startapning foydalanuvchilari har yili ikki baravar oshadi — investor bu oʻsish oʻn yil davom etsa nima boʻlishini hisoblaydi.",
        "order":   8,
        "grammar": [
            {"pattern": "doubled every year",
             "meaning": "Har yili ikki baravar oshdi — har yil 2 ga koʻpaytiriladi, 2 qoʻshilmaydi.",
             "examples": ["The number of users doubled every year."]},
            {"pattern": "by a factor of about a thousand",
             "meaning": "Taxminan ming baravar — 2 ning oʻninchi darajasi 1,024.",
             "examples": ["Ten doublings multiply a number by a factor of about a thousand."]},
        ],
        "body": '''<p>In 2021 two friends in Tashkent launched a <span class="cn-word" data-tr="ilova">mobile app</span> that helps small shops keep track of their <span class="cn-word" data-tr="tovar zaxirasi">stock</span>. At the end of the first year it had 1,500 users.</p>

<p>After that, the number of users <strong>doubled every year</strong>: 3,000 at the end of 2022, 6,000 in 2023, 12,000 in 2024 and 24,000 in 2025. In four years the app had grown sixteen times, because doubling four times means multiplying by two, then two, then two, then two.</p>

<p>This year the founders met an <span class="cn-word" data-tr="investor, sarmoyador">investor</span>. Their <span class="cn-word" data-tr="taqdimot">presentation</span> ended with a bold slide: if the app kept doubling for ten more years, it would have more than 24 million users. The investor did the <span class="cn-word" data-tr="hisob-kitob">arithmetic</span> with them. Ten doublings multiply a number <strong>by a factor of about a thousand</strong>, since two multiplied by itself ten times is 1,024. So the slide was correct as arithmetic: about 24.6 million users.</p>

<p>"The arithmetic is fine," she said. "The <span class="cn-word" data-tr="taxmin, faraz">assumption</span> is the problem. There are not 24 million small shops in this country." Doubling is easy when a number is small, she explained, and almost impossible when it is large, because the <span class="cn-word" data-tr="bozor">market</span> runs out.</p>

<p>The founders rewrote the slide. The new plan doubled the users for two more years and then grew by a fifth each year after that. It was less exciting, and the investor <span class="cn-word" data-tr="sarmoya kiritdi">invested</span> the same afternoon.</p>''',
        "questions": [
            {"text": "How many users did the app have at the end of 2025?",
             "choices": ["12,000", "6,000", "24,000"], "answer": 2,
             "explanation": "1,500 × 2 × 2 × 2 × 2 = <b>24,000</b>. 12,000 — 2024 yil oxiri."},
            {"text": "By about what factor do ten doublings multiply a number?",
             "choices": ["About a thousand", "About twenty", "About a hundred"], "answer": 0,
             "explanation": "2 ning oʻninchi darajasi 1,024 — <b>taxminan ming</b>. 20 — ikkini oʻnga koʻpaytirgan xato."},
            {"text": "Why did the investor object to the first slide?",
             "choices": ["The arithmetic on the slide was wrong.", "The market is too small for that many users.", "The app had stopped growing."], "answer": 1,
             "explanation": "Hisob toʻgʻri edi, lekin mamlakatda 24 million doʻkon <b>yoʻq</b> — bozor tugaydi."},
        ],
    },

    # ── GMAT-9 — units-digit check                                [Jenny]
    {
        "title":   "The Last Digit Check",
        "summary": "GMAT-9 matni. Hisobchi katta buyurtma summasini faqat oxirgi raqam bilan tekshiradi va xatoni bir zumda topadi.",
        "order":   9,
        "grammar": [
            {"pattern": "the last digit",
             "meaning": "Oxirgi raqam — koʻpaytmaning oxirgi raqami faqat koʻpaytuvchilarning oxirgi raqamlaridan chiqadi.",
             "examples": ["The last digit of the total must be 4."]},
            {"pattern": "ends in",
             "meaning": "… bilan tugaydi.",
             "examples": ["The figure in the report ends in 6."]},
        ],
        "body": '''<p>Malika works as an <span class="cn-word" data-tr="hisobchi">accountant</span> for a building-materials <span class="cn-word" data-tr="ulgurji sotuvchi">wholesaler</span> in Andijan. One Friday a sales <span class="cn-word" data-tr="hisobot">report</span> reached her desk with a large order: 37 pallets of tiles, each pallet holding 48 boxes, each box priced at 59 dollars. The total in the report was 104,816 dollars.</p>

<p>The <span class="cn-word" data-tr="mijoz">client</span> was waiting for the <span class="cn-word" data-tr="hisob-faktura">invoice</span>, and Malika had only a minute. She did not multiply the three numbers. Instead she looked only at <strong>the last digit</strong> of each one. Seven times eight is fifty-six, so the last digit so far was six. Six times nine is fifty-four, so the last digit of the true total had to be four.</p>

<p>The figure in the report <strong>ends in</strong> six. It could not be right.</p>

<p>She then multiplied properly. Thirty-seven pallets of 48 boxes make 1,776 boxes, and 1,776 boxes at 59 dollars cost 104,784 dollars. The report was 32 dollars too high. A colleague had typed the box count as 1,776 but used an old price for some of the boxes.</p>

<p>Thirty-two dollars is a small <span class="cn-word" data-tr="xato">error</span> on an order of over a hundred thousand, but the client was a <span class="cn-word" data-tr="davlat tashkiloti">public agency</span> that checks every invoice, and a wrong total would have delayed the <span class="cn-word" data-tr="toʻlov">payment</span> by weeks.</p>

<p>The last-digit check does not prove that a total is right. It only proves, very quickly, that some totals are wrong. Malika now runs it on every report before anything else.</p>''',
        "questions": [
            {"text": "What is the last digit of the correct total?",
             "choices": ["6", "4", "9"], "answer": 1,
             "explanation": "7 × 8 → 6, 6 × 9 = 54 → <b>4</b>. 6 — xato hisobotdagi oxirgi raqam."},
            {"text": "What was the correct total of the order?",
             "choices": ["$104,784", "$104,816", "$105,000"], "answer": 0,
             "explanation": "37 × 48 = 1,776; 1,776 × 59 = <b>$104,784</b>. $104,816 — xato hisobot."},
            {"text": "What does the last-digit check prove?",
             "choices": ["That a total is correct.", "That the price per box is correct.", "That some totals are wrong."], "answer": 2,
             "explanation": "Tekshiruv toʻgʻriligini isbotlamaydi — faqat ayrim summalarning <b>xato</b> ekanini tez koʻrsatadi."},
        ],
    },

    # ── GMAT-10 — dividing in a ratio                              [Guy]
    {
        "title":   "Two to Three to Four",
        "summary": "GMAT-10 matni. Kompaniya oʻquv byudjetini uchta filial orasida xodimlar soniga qarab boʻladi — nisbat, qismlar va bir xodimga toʻgʻri keladigan summa.",
        "order":   10,
        "grammar": [
            {"pattern": "in the ratio 2 to 3 to 4",
             "meaning": "2 : 3 : 4 nisbatda — jami 9 qism.",
             "examples": ["The budget was divided in the ratio 2 to 3 to 4."]},
            {"pattern": "in proportion to",
             "meaning": "… ga mutanosib ravishda.",
             "examples": ["Money is shared in proportion to the number of staff."]},
        ],
        "body": '''<p>A logistics company has three <span class="cn-word" data-tr="filial">branches</span>: Bukhara with 20 employees, Navoi with 30 and Samarkand with 40. This year the <span class="cn-word" data-tr="bosh ofis">head office</span> set aside 36,000 dollars for <span class="cn-word" data-tr="malaka oshirish">staff training</span>.</p>

<p>The first idea was to give each branch 12,000 dollars. The Samarkand manager <span class="cn-word" data-tr="eʼtiroz bildirdi">objected</span>: his branch had twice as many people as Bukhara, so an equal split would give each of his employees half as much training. The director agreed that money should be shared <strong>in proportion to</strong> the number of staff.</p>

<p>The staff numbers 20, 30 and 40 are <strong>in the ratio 2 to 3 to 4</strong>, which makes nine <span class="cn-word" data-tr="qism">parts</span> in total. The director divided 36,000 by nine and got 4,000 dollars per part. Bukhara received two parts, or 8,000 dollars. Navoi received three parts, or 12,000. Samarkand received four parts, or 16,000.</p>

<p>The <span class="cn-word" data-tr="bosh hisobchi">chief accountant</span> checked the split in a second way. The company has 90 employees, and 36,000 dollars for 90 people is 400 dollars per person. Twenty people at 400 dollars is 8,000, thirty is 12,000 and forty is 16,000. Both methods gave the same answer, and the three amounts added up to 36,000.</p>

<p>The Navoi manager noticed something <span class="cn-word" data-tr="qiziq">interesting</span>: his branch received exactly the same amount as under the first, equal plan. The change had only moved money from Bukhara to Samarkand. "A fair <span class="cn-word" data-tr="taqsimot">split</span>," the director said, "is not always an equal one."</p>''',
        "questions": [
            {"text": "How much did the Samarkand branch receive?",
             "choices": ["$12,000", "$16,000", "$18,000"], "answer": 1,
             "explanation": "Bir qism 4,000; Samarqand 4 qism — <b>$16,000</b>. $12,000 — teng boʻlinganda."},
            {"text": "How much training money is there per employee?",
             "choices": ["$400", "$4,000", "$1,200"], "answer": 0,
             "explanation": "36,000 ÷ 90 = <b>$400</b>. $4,000 — bir qism, bir xodim emas."},
            {"text": "Which branch received the same amount under both plans?",
             "choices": ["Bukhara", "Samarkand", "Navoi"], "answer": 2,
             "explanation": "<b>Navoiy</b>: 3 qism × 4,000 = 12,000 — teng boʻlishdagi bilan bir xil."},
        ],
    },
]
