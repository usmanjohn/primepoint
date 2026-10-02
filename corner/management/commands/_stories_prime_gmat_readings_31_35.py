# -*- coding: utf-8 -*-
"""Prime GMAT Readings — GMAT-31 … GMAT-35 (Data Insights, part two).

Each reading puts one Data Insights format into a business decision: a table nobody sorted,
a chart that lied with its axis, a two-part order, three sources to combine, and a candidate
learning to pace the section. English body, Uzbek glosses and explanations, audio.
Rules: corner/management/commands/toc_prime_gmat_readings.txt.

Import, then audio (odd orders Jenny, even orders Guy):
    python manage.py import_corner corner/management/commands/_stories_prime_gmat_readings_31_35.py --author=prime
    python manage.py gen_corner_audio --collection="Prime GMAT Readings" --only 31 --voice en-US-JennyNeural
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

    # ── GMAT-31 — sort the table                                     [Jenny]
    {
        "title":   "The Spreadsheet Nobody Sorted",
        "summary": "GMAT-31 matni. Bank filiallari jadvali alifbo tartibida yuboriladi — eng samarali filial faqat «bir xodimga» ustuni boʻyicha saralanganda koʻrinadi.",
        "order":   31,
        "grammar": [
            {"pattern": "sales per employee",
             "meaning": "Bir xodimga toʻgʻri keladigan sotuv — sotuv ÷ xodimlar soni.",
             "examples": ["The board wanted to know sales per employee, not total sales."]},
            {"pattern": "sorted by",
             "meaning": "… boʻyicha saralangan.",
             "examples": ["The table was sorted by branch name."]},
        ],
        "body": '''<p>Every quarter the regional office of a bank in Tashkent sends the <span class="cn-word" data-tr="direktorlar kengashi">board</span> a <span class="cn-word" data-tr="elektron jadval">spreadsheet</span> of its branches. Each row shows a branch, its number of employees and its total sales. For years the rows were <strong>sorted by</strong> branch name, from A to Z, and nobody thought to change it.</p>

<p>This spring the board asked a new question: which branch is the most <span class="cn-word" data-tr="samarali">efficient</span>? The regional manager, Dilshod, looked at the table and named the branch at the top of the sales column. It had sold 900,000 dollars of products, far more than any other.</p>

<p>His assistant, Nargiza, was not so sure. The biggest branch also had the biggest <span class="cn-word" data-tr="xodimlar">staff</span>: thirty employees. She added one column, <strong>sales per employee</strong>, and divided each row. The big branch came to 30,000 dollars per person. A small branch in the suburbs, with only twelve employees and 480,000 dollars of sales, came to 40,000 dollars per person.</p>

<p>Then she sorted the whole table by the new column. The order changed completely. The small branch moved from near the bottom of the list to the top, and the famous big branch fell to the middle.</p>

<p>Dilshod changed his <span class="cn-word" data-tr="hisobot">report</span>. He explained to the board that "the biggest" and "the most efficient" are different questions, and that a table answers only the question its columns are built for. Total sales measure size; sales per employee measure <span class="cn-word" data-tr="unumdorlik">productivity</span>.</p>

<p>The board asked for the new column to stay. From the next quarter the spreadsheet arrived sorted by sales per employee, with the alphabetical version kept on a second sheet. Nargiza was asked to visit the small branch and write down what its team did <span class="cn-word" data-tr="boshqacha">differently</span>, so that other branches could <span class="cn-word" data-tr="nusxa olmoq">copy</span> it.</p>''',
        "questions": [
            {"text": "What were the small branch's sales per employee?",
             "choices": ["30,000 dollars", "40,000 dollars", "48,000 dollars"], "answer": 1,
             "explanation": "480,000 ÷ 12 = <b>40,000</b>. 30,000 — katta filialniki."},
            {"text": "Why did Dilshod first name the wrong branch?",
             "choices": ["He looked at total sales instead of sales per employee.", "The spreadsheet had a typing error.", "The small branch had not reported its sales."], "answer": 0,
             "explanation": "Jami sotuv — hajm; samaradorlik — <b>bir xodimga</b> sotuv."},
            {"text": "What did Nargiza do after adding the new column?",
             "choices": ["She deleted the alphabetical list.", "She sent the table to the branches.", "She sorted the whole table by the new column."], "answer": 2,
             "explanation": "Yangi ustun boʻyicha <b>saralash</b> tartibni butunlay oʻzgartirdi."},
        ],
    },

    # ── GMAT-32 — read the axis                                     [Guy]
    {
        "title":   "The Chart That Started at 100",
        "summary": "GMAT-32 matni. Reklama slaydidagi ustunli diagramma 9% oʻsishni ikki baravar oʻsishday koʻrsatadi — chunki oʻq noldan emas, 100 dan boshlangan.",
        "order":   32,
        "grammar": [
            {"pattern": "the axis starts at 100",
             "meaning": "Oʻq 100 dan boshlanadi — ustunlar balandligi farqni boʻrttiradi.",
             "examples": ["On this slide the axis starts at 100, not at zero."]},
            {"pattern": "about 9 percent",
             "meaning": "Taxminan 9 foiz — haqiqiy oʻsish.",
             "examples": ["Sales grew by about 9 percent."]},
        ],
        "body": '''<p>At a <span class="cn-word" data-tr="marketing yigʻilishi">marketing meeting</span> in Samarkand, a young designer showed a <span class="cn-word" data-tr="slayd">slide</span> that made the whole room smile. Two bars compared the company's sales of green tea in two years. The bar for this year was twice as tall as the bar for last year. "We doubled our sales," someone said.</p>

<p>The finance manager, Ulugʻbek, asked to see the numbers. Last year's sales were 110 thousand packs; this year's were 120 thousand. The <span class="cn-word" data-tr="oʻsish">increase</span> was 10 thousand packs, which is <strong>about 9 percent</strong>, not one hundred percent.</p>

<p>The secret was in the left edge of the chart. <strong>The axis starts at 100</strong>, not at zero. On such a chart the first bar shows only the 10 packs above 100, and the second shows the 20 above 100, so the second bar looks twice as tall even though the real numbers are close.</p>

<p>Ulugʻbek did not blame the designer. Charting software often chooses the starting point <span class="cn-word" data-tr="avtomatik ravishda">automatically</span>, to fill the space. But he asked that every chart shown to <span class="cn-word" data-tr="investorlar">investors</span> follow two rules: bars start at zero, and the number is written on top of every bar.</p>

<p>The redrawn chart was less exciting. The two bars looked almost the same height, which was the truth. Next to them, the designer wrote the actual change: up 10 thousand packs, about 9 percent.</p>

<p>Ulugʻbek told the team why this mattered. A reader who trusts the height of a bar can be <span class="cn-word" data-tr="chalgʻitilgan">misled</span> by a single setting; a reader who reads the axis and the numbers cannot. The GMAT, he added, tests exactly that habit: read the <span class="cn-word" data-tr="oʻq">axis</span> first, then the numbers, and only then the shapes.</p>

<p>The real <span class="cn-word" data-tr="yutuq">achievement</span>, nine percent growth in a crowded market, was still worth celebrating. It simply had to be celebrated honestly.</p>''',
        "questions": [
            {"text": "By about what percent did tea sales actually grow?",
             "choices": ["9 percent", "50 percent", "100 percent"], "answer": 0,
             "explanation": "10 ÷ 110 ≈ <b>9%</b>. 100% — ustunlar balandligidan chiqarilgan notoʻgʻri xulosa."},
            {"text": "Why did the second bar look twice as tall as the first?",
             "choices": ["The designer made a typing error.", "The axis started at 100 instead of zero.", "Sales really had doubled."], "answer": 1,
             "explanation": "Oʻq <b>100 dan</b> boshlangan: ustunlar faqat 10 va 20 ni koʻrsatgan."},
            {"text": "Which rule did Ulugʻbek set for charts shown to investors?",
             "choices": ["Charts must use two colours.", "Charts must show five years.", "Bars must start at zero and show their numbers."], "answer": 2,
             "explanation": "Ustunlar <b>noldan</b> boshlanadi va har birining ustida son yoziladi."},
        ],
    },

    # ── GMAT-33 — two conditions, two answers                       [Jenny]
    {
        "title":   "Two Answers, One Decision",
        "summary": "GMAT-33 matni. Qahvaxona katta va kichik quti stakanlarni buyuradi: aynan 500 ta stakan va aynan 8 ta quti — ikkala shart birga yagona javob beradi.",
        "order":   33,
        "grammar": [
            {"pattern": "exactly 500 cups",
             "meaning": "Aynan 500 ta stakan — birinchi shart.",
             "examples": ["The café needed exactly 500 cups."]},
            {"pattern": "both conditions at once",
             "meaning": "Ikkala shart bir vaqtda — ikki qismli javob.",
             "examples": ["Only one order met both conditions at once."]},
        ],
        "body": '''<p>Sevinch runs a busy <span class="cn-word" data-tr="qahvaxona">café</span> near a university in Tashkent. Every month she orders paper cups from a <span class="cn-word" data-tr="yetkazib beruvchi">supplier</span> that sells them in two box sizes. A large box holds 100 <span class="cn-word" data-tr="stakanlar">cups</span> and costs 12 dollars. A small box holds 40 cups and costs 6 dollars.</p>

<p>This month she needed <strong>exactly 500 cups</strong>, because her <span class="cn-word" data-tr="omborxona">storeroom</span> had space for no more. The supplier also had a rule: <span class="cn-word" data-tr="bepul yetkazib berish">free delivery</span> only for orders of exactly 8 boxes. The order form had two boxes to fill in: the number of large boxes and the number of small ones.</p>

<p>Her first idea was five large boxes: exactly 500 cups, but only 5 boxes, so she would pay for delivery. She needed <strong>both conditions at once</strong>.</p>

<p>She tried the numbers one by one. Two large boxes and six small ones made 8 boxes but only 440 cups. Four large boxes and four small ones made 8 boxes but 560 cups, too many for the storeroom. Three large boxes and five small ones made 8 boxes and 300 plus 200, exactly 500 cups, for 36 plus 30, or 66 dollars.</p>

<p>Only that order met both conditions. Each wrong order had one part right and one part wrong, and Sevinch realised that a <span class="cn-word" data-tr="yarim toʻgʻri">half-right</span> order was simply a wrong order.</p>

<p>Her brother, who was preparing for the GMAT, smiled when she told him. "That is a Two-Part Analysis question," he said. "Two answers, but only one <span class="cn-word" data-tr="qaror">decision</span>, and no credit for getting one of them right." Sevinch added a small <span class="cn-word" data-tr="jadval">table</span> of box combinations to her ordering notebook, so that next month the right answer would take a minute.</p>''',
        "questions": [
            {"text": "How many large boxes did Sevinch order?",
             "choices": ["2", "5", "3"], "answer": 2,
             "explanation": "Uchta katta va beshta kichik: 8 ta quti, 300 + 200 = 500 stakan — <b>3</b>."},
            {"text": "What was wrong with ordering four large boxes and four small ones?",
             "choices": ["It gave 560 cups, more than she could store.", "It was not 8 boxes.", "The supplier had no small boxes."], "answer": 0,
             "explanation": "8 ta quti — toʻgʻri, lekin stakanlar <b>560</b> — ortiqcha."},
            {"text": "Why did Sevinch call a half-right order a wrong order?",
             "choices": ["The supplier charged extra for mistakes.", "Both conditions had to be met together.", "Her brother told her so."], "answer": 1,
             "explanation": "Ikkala shart <b>bir vaqtda</b> bajarilishi kerak edi — bitta qism yetmaydi."},
        ],
    },

    # ── GMAT-34 — combine the sources                                [Guy]
    {
        "title":   "Three Emails and a Table",
        "summary": "GMAT-34 matni. Tadbir tashkilotchisi uchta xat va bitta jadvalni birlashtiradi — narx qoidasi bir manbada, odamlar soni boshqasida.",
        "order":   34,
        "grammar": [
            {"pattern": "more than 40 people",
             "meaning": "40 kishidan koʻp — qatʼiy shart, 40 ning oʻzi kirmaydi.",
             "examples": ["Groups of more than 40 people must book the large hall."]},
            {"pattern": "per person per day",
             "meaning": "Har bir kishiga har kuni — kishilar soni va kunlar soniga koʻpaytiriladi.",
             "examples": ["Lunch costs 12 dollars per person per day."]},
        ],
        "body": '''<p>Shahlo plans <span class="cn-word" data-tr="korporativ tadbirlar">corporate events</span> for a consulting firm in Tashkent. On Monday her manager asked for the cost of a two-day workshop for the sales team. The answer was not in any single place.</p>

<p>The first email, from the <span class="cn-word" data-tr="tadbir oʻtkaziladigan joy">venue</span>, gave the room prices: 250 dollars a day for a standard room, and 400 dollars a day for the large hall, which is required for groups of <strong>more than 40 people</strong>. The second email, from the <span class="cn-word" data-tr="ovqat yetkazuvchi">caterer</span>, said that lunch and coffee cost 12 dollars <strong>per person per day</strong>. The third email, from the sales director, said only that "the whole team" would attend.</p>

<p>The number of people was in a table: the company's <span class="cn-word" data-tr="xodimlar roʻyxati">staff list</span>, which showed 45 people in the sales team.</p>

<p>Shahlo put the sources together in order. Forty-five is more than forty, so the venue's rule sent the team to the large hall: two days at 400 dollars, or 800 dollars. The caterer's rule gave 45 people times 12 dollars times 2 days, or 1,080 dollars. The total came to 1,880 dollars.</p>

<p>Her colleague had <span class="cn-word" data-tr="taxmin qilmoq">estimated</span> the same event the week before and arrived at 1,040 dollars. He had used the standard room, because he had not opened the venue's email, and he had counted lunch for one day only. Each source on its own was simple; the mistakes came from reading one source and <span class="cn-word" data-tr="taxmin qilmoq">guessing</span> the rest.</p>

<p>Shahlo now keeps a one-line <span class="cn-word" data-tr="eslatma">note</span> for every source before she calculates anything: "venue — room rules", "caterer — price per person per day", "staff list — head count". Then she knows exactly where to look for each number.</p>

<p>The manager approved the <span class="cn-word" data-tr="byudjet">budget</span> the same afternoon and asked her to use the same method for the year-end party, which had five sources instead of three.</p>''',
        "questions": [
            {"text": "What does the room cost per day for the sales team's workshop?",
             "choices": ["250 dollars", "400 dollars", "540 dollars"], "answer": 1,
             "explanation": "45 kishi — 40 dan koʻp, demak katta zal: <b>400 dollar</b>."},
            {"text": "What is the total cost of the two-day workshop?",
             "choices": ["1,040 dollars", "1,380 dollars", "1,880 dollars"], "answer": 2,
             "explanation": "800 + 45 × 12 × 2 = 800 + 1,080 = <b>1,880</b>."},
            {"text": "What caused the colleague's lower estimate?",
             "choices": ["He used the standard room and counted lunch for one day.", "He used an old staff list.", "The caterer had lowered its prices."], "answer": 0,
             "explanation": "Joy xatini ochmagan va ovqatni <b>bir kunga</b> hisoblagan."},
        ],
    },

    # ── GMAT-35 — pace the section                                   [Jenny]
    {
        "title":   "Forty-Five Minutes of Data",
        "summary": "GMAT-35 matni. Nomzod Data Insights sinov boʻlimida vaqtni yoʻqotadi va qisman ball yoʻqligini anglaydi — keyingi safar reja bilan ishlaydi.",
        "order":   35,
        "grammar": [
            {"pattern": "no partial credit",
             "meaning": "Qisman ball yoʻq — koʻp qismli savolda hammasi toʻgʻri boʻlishi kerak.",
             "examples": ["There is no partial credit for multi-part questions."]},
            {"pattern": "a little over two minutes",
             "meaning": "Ikki daqiqadan biroz koʻp — bir savolga oʻrtacha vaqt.",
             "examples": ["Each question gets a little over two minutes."]},
        ],
        "body": '''<p>Feruza works as an <span class="cn-word" data-tr="tahlilchi">analyst</span> at a bank in Tashkent and is preparing for the GMAT in the evenings. Her strongest section is Quant, so she expected Data Insights to be easy. Her first timed practice section showed her otherwise.</p>

<p>The section had twenty questions in forty-five minutes, <strong>a little over two minutes</strong> for each. Early on she met a Multi-Source <span class="cn-word" data-tr="toʻplam">set</span> with three tabs and spent eight minutes on its first question, determined to get every detail right. Later, on a Table Analysis question, she judged two of the three statements correctly and the third one wrong. She was surprised to see that question marked as zero: there is <strong>no partial credit</strong> for multi-part questions. When time ran out, three questions were still unanswered.</p>

<p>Her <span class="cn-word" data-tr="repetitor">tutor</span> drew three lines on a sheet of paper. First, a plan for the clock: about seven questions by minute fifteen and about thirteen by minute thirty. Second, a rule for long questions: if one part of a multi-part question is still unclear after three minutes, choose the most likely answer, <span class="cn-word" data-tr="belgilab qoʻymoq">bookmark</span> it and move on. Third, a rule for the <span class="cn-word" data-tr="kalkulyator">calculator</span>: use it for awkward divisions, not for simple percentages that are faster in the head.</p>

<p>The tutor also pointed out that the first question of a Multi-Source set is the expensive one. The time spent learning the tabs is <span class="cn-word" data-tr="qaytarib olinadi">recovered</span> on the next questions, which use the same sources.</p>

<p>A week later Feruza sat a second practice section. She reached question thirteen at minute twenty-nine, answered every question, and used the last two minutes to change one answer through Question Review and Edit, which allows up to three changes in a section. Her <span class="cn-word" data-tr="natija">result</span> was clearly better, and she had not learned any new mathematics. She had only stopped letting one question <span class="cn-word" data-tr="hal qilmoq">decide</span> the whole section.</p>''',
        "questions": [
            {"text": "How many questions did Feruza leave unanswered in her first practice section?",
             "choices": ["Two", "Three", "Eight"], "answer": 1,
             "explanation": "Vaqt tugaganda <b>uchta</b> savol javobsiz qolgan."},
            {"text": "Why was the Table Analysis question marked as zero?",
             "choices": ["There is no partial credit for multi-part questions.", "She ran out of time on it.", "She used the calculator."], "answer": 0,
             "explanation": "Uchta bayonotdan ikkitasi toʻgʻri boʻlsa ham — <b>qisman ball yoʻq</b>."},
            {"text": "About how many questions should she finish by minute thirty, according to her tutor's plan?",
             "choices": ["Seven", "Twenty", "Thirteen"], "answer": 2,
             "explanation": "Boʻlimning uchdan ikkisi — taxminan <b>13</b> ta savol."},
        ],
    },
]
