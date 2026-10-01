# -*- coding: utf-8 -*-
"""Prime GMAT Readings — GMAT-21 … GMAT-25 (sequences, counting, probability, statistics,
strategy). The last five readings of the Quant block.

The third leg of each Prime GMAT lesson: the lesson's maths doing real work in an
ENGLISH business text, with Uzbek cn-word glosses, an "Exam English" block and audio.
Rules: corner/management/commands/toc_prime_gmat_readings.txt (overrides STYLE_GUIDE_CORNER).

No algebraic notation in the body — quantities in English words and plain numbers.

Import, then audio (always pass --voice; odd orders Jenny, even orders Guy):
    python manage.py import_corner corner/management/commands/_stories_prime_gmat_readings_21_25.py --author=prime
    python manage.py gen_corner_audio --collection="Prime GMAT Readings" --only 21 --voice en-US-JennyNeural
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

    # ── GMAT-21 — two arithmetic sequences                          [Jenny]
    {
        "title":   "Two Salary Offers",
        "summary": "GMAT-21 matni. Bitiruvchi ikki ish taklifini solishtiradi: biri yuqori boshlanadi, biri tezroq oʻsadi — qaysi biri koʻproq pul beradi?",
        "order":   21,
        "grammar": [
            {"pattern": "rising by 3,000 dollars each year",
             "meaning": "Har yili 3,000 dollarga oshib — arifmetik ketma-ketlik.",
             "examples": ["The salary starts at 30,000 dollars, rising by 3,000 dollars each year."]},
            {"pattern": "over the first five years",
             "meaning": "Dastlabki besh yil davomida — yigʻindi.",
             "examples": ["Which offer pays more over the first five years?"]},
        ],
        "body": '''<p>Bobur finished his degree in finance in Tashkent and received two job <span class="cn-word" data-tr="takliflar">offers</span> on the same day. A bank offered a starting <span class="cn-word" data-tr="maosh">salary</span> of 30,000 dollars a year, <strong>rising by 3,000 dollars each year</strong>. A consulting firm offered 36,000 dollars to start, rising by 1,500 dollars each year.</p>

<p>His friends told him to take the higher number. Bobur wrote both offers out year by year instead. The bank would pay 30, 33, 36, 39 and then 42 thousand dollars. The firm would pay 36, 37.5, 39, 40.5 and then 42 thousand. The two salaries would be <span class="cn-word" data-tr="teng">equal</span> in the fifth year, at 42,000 dollars each.</p>

<p>Then he added them up. <strong>Over the first five years</strong>, the bank would pay five times the average of 30 and 42 thousand, which is 180,000 dollars. The firm would pay five times the average of 36 and 42 thousand, which is 195,000 dollars. The firm was 15,000 dollars ahead.</p>

<p>But Bobur did not plan to stay only five years. After the fifth year the bank's salary grows faster every year. In the tenth year the bank would pay 57,000 dollars and the firm 49,500. Over ten years the bank's total would be 435,000 dollars and the firm's 427,500. The bank would <span class="cn-word" data-tr="quvib oʻtmoq">overtake</span> the firm, though only by 7,500 dollars.</p>

<p>The choice, he realised, depended on a single question: how long would he stay? He also noticed that both <span class="cn-word" data-tr="oʻsish">raises</span> were only promises, while the starting salaries were <span class="cn-word" data-tr="kafolatlangan">guaranteed</span>.</p>

<p>He chose the consulting firm, which offered more <span class="cn-word" data-tr="tajriba">experience</span> early on, and wrote both sequences in a <span class="cn-word" data-tr="daftar">notebook</span>. In five years, he told himself, he would open it again and compare.</p>''',
        "questions": [
            {"text": "In which year would the two salaries be equal?",
             "choices": ["The third year", "The fifth year", "The seventh year"], "answer": 1,
             "explanation": "Bank: 30 + 4 × 3 = 42; firma: 36 + 4 × 1.5 = 42 — <b>beshinchi yil</b>."},
            {"text": "How much would the consulting firm pay in total over the first five years?",
             "choices": ["180,000 dollars", "210,000 dollars", "195,000 dollars"], "answer": 2,
             "explanation": "5 × (36,000 + 42,000) ÷ 2 = <b>195,000</b>. 180,000 — bankniki."},
            {"text": "Over ten years, which offer pays more in total?",
             "choices": ["The bank", "The consulting firm", "Both pay the same"], "answer": 0,
             "explanation": "Bank 435,000, firma 427,500 — <b>bank</b> 7,500 dollarga koʻp."},
        ],
    },

    # ── GMAT-22 — the multiplication principle                       [Guy]
    {
        "title":   "How Many Lunches?",
        "summary": "GMAT-22 matni. Restoran «100 dan ortiq tushlik» deb reklama qilmoqchi — qaysi taom qoʻshilsa, kombinatsiyalar soni shunchaga yetadi?",
        "order":   22,
        "grammar": [
            {"pattern": "one soup, one main course and one dessert",
             "meaning": "Bitta shoʻrva, bitta asosiy taom va bitta shirinlik — «va» koʻpaytirishni bildiradi.",
             "examples": ["Every set lunch has one soup, one main course and one dessert."]},
            {"pattern": "more than 100 different lunches",
             "meaning": "100 dan ortiq turli tushlik — chegara qatʼiy, 100 ning oʻzi yetmaydi.",
             "examples": ["The owner wanted to advertise more than 100 different lunches."]},
        ],
        "body": '''<p>Shahlo owns a small restaurant near the business <span class="cn-word" data-tr="tuman, mavze">district</span> in Tashkent. Every weekday she serves a set <span class="cn-word" data-tr="tushlik">lunch</span>: <strong>one soup, one main course and one dessert</strong>. Her <span class="cn-word" data-tr="menyu">menu</span> lists 4 soups, 5 main courses and 3 desserts.</p>

<p>Her <span class="cn-word" data-tr="jiyan">nephew</span>, who was studying for a business exam, told her that the restaurant already offered 60 different lunches, because each of the 4 soups can go with each of the 5 mains, and each of those 20 pairs can go with each of the 3 desserts. Shahlo liked the number. She wanted a new <span class="cn-word" data-tr="peshtaxta yozuvi">sign</span> for the window that said <strong>more than 100 different lunches</strong>.</p>

<p>Adding dishes costs money, so she asked which single addition would help most. One more soup would give 5 times 5 times 3, which is 75. One more main course would give 4 times 6 times 3, which is 72. One more dessert would give 4 times 5 times 4, which is 80. None of them was enough.</p>

<p>She tried two additions. A new soup and a new dessert would give 5 times 5 times 4, exactly 100, which is not more than 100. Two new desserts would also give exactly 100. Finally, one new dish in every <span class="cn-word" data-tr="toifa">category</span> would give 5 times 6 times 4, which is 120.</p>

<p>Shahlo chose that option. The new soup and dessert were cheap to make, and the new main course used <span class="cn-word" data-tr="masalliqlar">ingredients</span> she already bought. The <span class="cn-word" data-tr="reklama">advertisement</span> went up the following Monday: "120 different lunches, one price."</p>

<p>Her nephew pointed out the lesson. In a <span class="cn-word" data-tr="koʻpaytma">product</span>, adding one item to the smallest group gives the biggest jump: the third dessert raised the total by a third, while the sixth main course raised it by only a fifth.</p>''',
        "questions": [
            {"text": "How many different lunches did the original menu offer?",
             "choices": ["12", "60", "120"], "answer": 1,
             "explanation": "4 × 5 × 3 = <b>60</b>. 12 — qoʻshilgan javob."},
            {"text": "How many lunches would there be with only one more dessert?",
             "choices": ["72", "75", "80"], "answer": 2,
             "explanation": "4 × 5 × 4 = <b>80</b>. 75 — bitta shoʻrva qoʻshilganda."},
            {"text": "Why did a new soup and a new dessert not meet Shahlo's goal?",
             "choices": ["They gave exactly 100, not more than 100.", "They gave fewer than 80.", "The new dishes were too expensive."], "answer": 0,
             "explanation": "5 × 5 × 4 = 100 — «more than 100» uchun <b>yetmaydi</b>."},
        ],
    },

    # ── GMAT-23 — at least one, independence                         [Jenny]
    {
        "title":   "The Two Alarms",
        "summary": "GMAT-23 matni. Ombor bitta qimmat signalizatsiya yoki ikkita arzon, mustaqil signalizatsiya oʻrtasida tanlaydi — «kamida bittasi» ehtimoli.",
        "order":   23,
        "grammar": [
            {"pattern": "works 90 percent of the time",
             "meaning": "90% hollarda ishlaydi — ehtimollik 0.9.",
             "examples": ["Each cheaper alarm works 90 percent of the time."]},
            {"pattern": "at least one of them",
             "meaning": "Kamida bittasi — 1 minus «hech biri».",
             "examples": ["What is the chance that at least one of them works?"]},
        ],
        "body": '''<p>A <span class="cn-word" data-tr="ombor">warehouse</span> in Andijan stores <span class="cn-word" data-tr="elektronika">electronics</span>, and its <span class="cn-word" data-tr="sugʻurta kompaniyasi">insurance company</span> set a new condition: the fire-alarm system must work, when needed, with a probability of at least 98 percent.</p>

<p>The manager, Sardor, received two <span class="cn-word" data-tr="narx takliflari">quotes</span>. The first was a premium alarm that <span class="cn-word" data-tr="ishonchli">reliably</span> works 95 percent of the time and costs 1,200 dollars. The second was a pair of cheaper alarms, each of which <strong>works 90 percent of the time</strong>, at 450 dollars each, or 900 dollars for both.</p>

<p>At first the premium alarm looked safer: 95 is more than 90. But Sardor remembered how to think about <strong>at least one of them</strong>. The system with two alarms fails only if both alarms fail at the same moment. Each one fails 10 percent of the time, so both fail together one tenth of one tenth of the time, which is 1 time in 100. The pair therefore works 99 percent of the time.</p>

<p>The premium alarm fails 5 times in 100. The cheaper pair fails 1 time in 100, and it costs 300 dollars less. Only the pair met the insurance company's 98 percent rule.</p>

<p>There was one <span class="cn-word" data-tr="shart">condition</span> that Sardor almost missed. The calculation is correct only if the two alarms fail <span class="cn-word" data-tr="mustaqil ravishda">independently</span>. If both run on the same power line, a single power cut silences both at once, and the 1 in 100 figure becomes meaningless. He asked the installer to give each alarm its own <span class="cn-word" data-tr="batareya">battery</span> and to mount them in different parts of the building.</p>

<p>The insurance <span class="cn-word" data-tr="inspektor">inspector</span> approved the system the following week. Her report used the same arithmetic, and she added one line Sardor liked: two independent ninety-percent systems are better than one ninety-five-percent system.</p>''',
        "questions": [
            {"text": "How often do both cheaper alarms fail at the same time?",
             "choices": ["1 time in 100", "10 times in 100", "20 times in 100"], "answer": 0,
             "explanation": "0.1 × 0.1 = 0.01 — <b>100 tadan 1</b>. 20 — muvaffaqiyatsizliklarni qoʻshgan javob."},
            {"text": "Why did Sardor give each alarm its own battery?",
             "choices": ["Batteries are cheaper than power lines.", "So that the two alarms would fail independently.", "The insurance company asked for longer battery life."], "answer": 1,
             "explanation": "Hisob faqat signalizatsiyalar <b>mustaqil</b> ishdan chiqqandagina toʻgʻri."},
            {"text": "With what probability does the two-alarm system work when needed?",
             "choices": ["90 percent", "95 percent", "99 percent"], "answer": 2,
             "explanation": "1 − 0.01 = <b>99%</b> — sugʻurta talab qilgan 98% dan yuqori."},
        ],
    },

    # ── GMAT-24 — mean vs median                                     [Guy]
    {
        "title":   "The Average Salary",
        "summary": "GMAT-24 matni. Ish eʼlonida «oʻrtacha maosh 3,000 dollar» deyilgan — lekin xodimlarning koʻpi 2,000 oladi. Oʻrtacha va mediana farqi.",
        "order":   24,
        "grammar": [
            {"pattern": "an average salary of 3,000 dollars",
             "meaning": "Oʻrtacha maosh — barcha maoshlar yigʻindisi ÷ xodimlar soni.",
             "examples": ["The advertisement promised an average salary of 3,000 dollars."]},
            {"pattern": "the median salary",
             "meaning": "Mediana maosh — tartiblangan roʻyxatning oʻrtasidagi maosh.",
             "examples": ["What is the median salary at the firm?"]},
        ],
        "body": '''<p>Nilufar saw a job <span class="cn-word" data-tr="eʼlon">advertisement</span> from a small design studio in Samarkand. It promised "<strong>an average salary of 3,000 dollars</strong> a month", which was more than she earned at the time. Before the <span class="cn-word" data-tr="suhbat">interview</span>, she did what her statistics teacher had taught her: she asked for <strong>the median salary</strong>.</p>

<p>The answer surprised her. The studio had nine people. Eight designers earned 2,000 dollars a month each. The director earned 11,000 dollars. Eight times 2,000 is 16,000; with the director's 11,000 the total was 27,000; and 27,000 divided among nine people is exactly 3,000. The advertisement was <span class="cn-word" data-tr="aniq, toʻgʻri">accurate</span>.</p>

<p>But the median told a different story. If the nine salaries are written in order, the fifth one, in the middle, is 2,000 dollars. Eight of the nine people earned exactly the median and less than the mean. One large salary had pulled the average up by 1,000 dollars without changing what a typical designer was paid.</p>

<p>Nilufar went to the interview anyway, because she liked the studio's work. When the director offered her 2,000 dollars, she was ready. She explained, politely, that the advertised average did not <span class="cn-word" data-tr="aks ettirmoq">reflect</span> what designers earned, and she asked for 2,300 dollars, pointing to her experience with <span class="cn-word" data-tr="mijozlar">clients</span> abroad.</p>

<p>The director laughed and agreed to 2,200 dollars. He also changed the next advertisement. It now said "typical designer salary: 2,000 dollars", which was less <span class="cn-word" data-tr="jozibali">attractive</span> but more honest.</p>

<p>Nilufar's rule for any <span class="cn-word" data-tr="maʼlumot">data</span> about pay is simple: when one number is far from the others, the mean is a <span class="cn-word" data-tr="reklama">marketing</span> figure and the median is the real one.</p>''',
        "questions": [
            {"text": "What was the median salary at the studio?",
             "choices": ["3,000 dollars", "2,000 dollars", "11,000 dollars"], "answer": 1,
             "explanation": "Toʻqqiz maoshning oʻrtasidagisi (5-chi) — <b>2,000</b>. 3,000 — oʻrtacha."},
            {"text": "What was the total monthly salary of all nine people?",
             "choices": ["16,000 dollars", "18,000 dollars", "27,000 dollars"], "answer": 2,
             "explanation": "8 × 2,000 + 11,000 = <b>27,000</b>. 16,000 — direktorsiz."},
            {"text": "Why was the average higher than what a typical designer earned?",
             "choices": ["One very large salary pulled the average up.", "The designers worked part-time.", "The advertisement used last year's figures."], "answer": 0,
             "explanation": "Direktorning <b>bitta katta maoshi</b> oʻrtachani 1,000 dollarga koʻtargan."},
        ],
    },

    # ── GMAT-25 — pacing a section                                   [Jenny]
    {
        "title":   "Twenty-One Questions, Forty-Five Minutes",
        "summary": "GMAT-25 matni. Jasur birinchi sinov boʻlimida vaqtni yoʻqotadi, ikkinchisida reja bilan ishlaydi — nazorat nuqtalari, taxmin va uchta tahrir.",
        "order":   25,
        "grammar": [
            {"pattern": "fell behind",
             "meaning": "Ortda qoldi — vaqt rejasidan kechikdi.",
             "examples": ["By the thirtieth minute he had fallen behind."]},
            {"pattern": "made an educated guess",
             "meaning": "Aqlli taxmin qildi — notoʻgʻri variantlarni chiqarib tashlab tanladi.",
             "examples": ["After three minutes he made an educated guess and moved on."]},
        ],
        "body": '''<p>Jasur is preparing for the GMAT while working <span class="cn-word" data-tr="toʻliq stavkada">full-time</span> at a bank in Tashkent. On a Saturday morning he sat his first timed practice <span class="cn-word" data-tr="boʻlim">section</span>: 21 quantitative questions in 45 minutes, a little over two minutes for each.</p>

<p>The first five questions went well. Question 6 was a <span class="cn-word" data-tr="aralashma">mixture</span> problem, and he was sure he almost had it. Seven minutes later he still did not. By the thirtieth minute he was only on question 10, and he <strong>fell behind</strong> badly. When the <span class="cn-word" data-tr="taymer">timer</span> ran out, four questions were still unanswered.</p>

<p>His <span class="cn-word" data-tr="repetitor">tutor</span> looked at the sheet and made one point. Seven minutes on one question is the time of three ordinary questions. The mixture problem had cost him not one mark but several.</p>

<p>The next Saturday Jasur used a <span class="cn-word" data-tr="reja">plan</span>. He wrote three numbers at the top of his notes: question 7 by minute 15, question 14 by minute 30, and the end at minute 45. Whenever a question showed no clear path after about three minutes, he crossed out the choices he could rule out, <strong>made an educated guess</strong>, <span class="cn-word" data-tr="belgilab qoʻydi">bookmarked</span> the question and moved on.</p>

<p>He reached question 14 at minute 29. He finished all 21 questions with four minutes to spare, and he used them to <span class="cn-word" data-tr="qayta koʻrib chiqmoq">review</span> his three bookmarks. On two of them he found a clear slip in his arithmetic and changed the answer; the third he left alone, because he had no new reason to change it. The test allows up to three such changes in a section, and he did not waste one on a doubt.</p>

<p>His score on the second section was higher, though he had not learned any new mathematics during the week. What had changed was his <span class="cn-word" data-tr="intizom">discipline</span>: he no longer let one question decide the whole section.</p>''',
        "questions": [
            {"text": "How many questions did Jasur leave unanswered in his first practice section?",
             "choices": ["2", "3", "4"], "answer": 2,
             "explanation": "Vaqt tugaganda <b>4 ta</b> savol javobsiz qolgan."},
            {"text": "According to Jasur's plan, by which minute should he reach question 14?",
             "choices": ["Minute 15", "Minute 30", "Minute 45"], "answer": 1,
             "explanation": "Boʻlimning uchdan ikkisi — <b>30-daqiqa</b>."},
            {"text": "How many answers did Jasur change during his review?",
             "choices": ["Two", "Three", "None"], "answer": 0,
             "explanation": "Uchta belgilangan savoldan <b>ikkitasida</b> aniq xato topib, javobni oʻzgartirgan."},
        ],
    },
]
