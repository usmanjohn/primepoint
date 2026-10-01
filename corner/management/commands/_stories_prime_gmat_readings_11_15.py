# -*- coding: utf-8 -*-
"""Prime GMAT Readings — GMAT-11 … GMAT-15 (word problems, part one).

The third leg of each Prime GMAT lesson: the lesson's maths doing real work in an
ENGLISH business text, with Uzbek cn-word glosses, an "Exam English" block and audio.
Rules: corner/management/commands/toc_prime_gmat_readings.txt (overrides STYLE_GUIDE_CORNER).

No algebraic notation in the body — quantities in English words and plain numbers.

Import, then audio (always pass --voice; odd orders Jenny, even orders Guy):
    python manage.py import_corner corner/management/commands/_stories_prime_gmat_readings_11_15.py --author=prime
    python manage.py gen_corner_audio --collection="Prime GMAT Readings" --only 11 --voice en-US-JennyNeural
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

    # ── GMAT-11 — weighted average                                [Jenny]
    {
        "title":   "The Average That Hid a Branch",
        "summary": "GMAT-11 matni. Restoranlar tarmogʻi mijozlar bahosini oʻrtachalaydi — oddiy oʻrtacha bitta zaif filialni yashirib qoʻyadi.",
        "order":   11,
        "grammar": [
            {"pattern": "an average rating of 4.5",
             "meaning": "Oʻrtacha baho 4.5 — yigʻindi ÷ baholar soni.",
             "examples": ["The new branch had an average rating of 4.5."]},
            {"pattern": "weighted by the number of reviews",
             "meaning": "Baholar soniga qarab tortilgan — katta guruh oʻrtachani oʻziga tortadi.",
             "examples": ["The true average is weighted by the number of reviews."]},
        ],
        "body": '''<p>A small <span class="cn-word" data-tr="restoranlar tarmogʻi">restaurant chain</span> in Tashkent has two branches. Every month its owner, Rustam, reads one number in the <span class="cn-word" data-tr="hisobot">report</span>: the average customer rating out of five.</p>

<p>In March the report said 4.0, the same as the month before. The new branch near the university had received 20 <span class="cn-word" data-tr="sharhlar">reviews</span> with <strong>an average rating of 4.5</strong>. The old branch in the city centre had received 80 reviews with an average of 3.5. The <span class="cn-word" data-tr="tahlilchi">analyst</span> had added 4.5 and 3.5 and divided by two.</p>

<p>Rustam's daughter, Zarina, who was studying for a business degree, looked at the same figures and frowned. "Your customers are not split half and half," she said. "Four out of five reviews came from the old branch. The average has to be <strong>weighted by the number of reviews</strong>."</p>

<p>She worked it out on a napkin. Twenty reviews at 4.5 are worth 90 points. Eighty reviews at 3.5 are worth 280 points. Together that is 370 points from 100 reviews, an average of 3.7, not 4.0.</p>

<p>The <span class="cn-word" data-tr="farq">difference</span> looked small, but it changed the story. The simple average said the chain was doing well. The weighted average said that most customers were eating at the weaker branch and were not very happy there. The bright new branch had been <span class="cn-word" data-tr="yashirmoq">hiding</span> the problem.</p>

<p>Rustam sent an <span class="cn-word" data-tr="nazoratchi">inspector</span> to the old branch the next week. The kitchen had a new cook and the <span class="cn-word" data-tr="kutish vaqti">waiting time</span> had doubled. By June, the weighted average had risen to 4.2, and the report now showed both branches on separate lines.</p>''',
        "questions": [
            {"text": "What was the chain's true average rating in March?",
             "choices": ["4.0", "3.7", "4.2"], "answer": 1,
             "explanation": "(20 × 4.5 + 80 × 3.5) ÷ 100 = 370 ÷ 100 = <b>3.7</b>. 4.0 — oddiy oʻrtacha."},
            {"text": "Why was the analyst's average of 4.0 misleading?",
             "choices": ["Most of the reviews came from the weaker branch.", "The new branch had too few customers.", "Some ratings were counted twice."], "answer": 0,
             "explanation": "Sharhlarning <b>beshdan toʻrti</b> eski filialdan — oddiy oʻrtacha uni hisobga olmaydi."},
            {"text": "What did Rustam find at the old branch?",
             "choices": ["The prices had gone up.", "The branch had fewer tables.", "A new cook and twice the waiting time."], "answer": 2,
             "explanation": "Oshxonada <b>yangi oshpaz</b>, kutish vaqti esa ikki baravar oshgan."},
        ],
    },

    # ── GMAT-12 — mixture ratio                                    [Guy]
    {
        "title":   "The Tea Blender",
        "summary": "GMAT-12 matni. Samarqanddagi choy savdogari ikki xil choyni aralashtirib, kerakli narxdagi aralashma tayyorlaydi — chalishtirish usuli.",
        "order":   12,
        "grammar": [
            {"pattern": "a blend that costs 8 dollars a kilogram",
             "meaning": "Kilogrami 8 dollar boʻlgan aralashma — maqsad narx.",
             "examples": ["The hotel wanted a blend that costs 8 dollars a kilogram."]},
            {"pattern": "in the ratio 2 to 1",
             "meaning": "2 : 1 nisbatda — har 3 kg dan 2 kg arzon, 1 kg qimmat.",
             "examples": ["She mixed the two teas in the ratio 2 to 1."]},
        ],
        "body": '''<p>Gulnora runs a tea shop in the old <span class="cn-word" data-tr="bozor">bazaar</span> of Samarkand. She sells two green teas: an <span class="cn-word" data-tr="kundalik">everyday</span> tea from Fergana at 6 dollars a kilogram and a fine tea from China at 12 dollars a kilogram.</p>

<p>One morning the manager of a large <span class="cn-word" data-tr="mehmonxona">hotel</span> came in with an <span class="cn-word" data-tr="buyurtma">order</span>. He needed 60 kilograms of tea for the season and had a firm <span class="cn-word" data-tr="byudjet">budget</span>: he wanted <strong>a blend that costs 8 dollars a kilogram</strong>, better than the everyday tea but cheaper than the fine one.</p>

<p>Gulnora did not reach for a calculator. Eight dollars is 2 dollars above the cheap tea and 4 dollars below the fine tea. The blend must lean toward the cheaper tea, she reasoned, because 8 is closer to 6 than to 12. So she <span class="cn-word" data-tr="almashtirmoq">swapped</span> the distances: the cheap tea gets the larger one, 4, and the fine tea gets the smaller one, 2. She would mix them <strong>in the ratio 2 to 1</strong>.</p>

<p>Sixty kilograms split in the ratio 2 to 1 is 40 kilograms of everyday tea and 20 kilograms of fine tea. She checked it the long way. Forty kilograms at 6 dollars cost 240 dollars, and twenty kilograms at 12 dollars cost another 240. That is 480 dollars for 60 kilograms, exactly 8 dollars a kilogram.</p>

<p>The hotel manager tasted a cup and signed the order. Gulnora wrote the blend's <span class="cn-word" data-tr="tarkib, retsept">recipe</span> on the back of a receipt and pinned it above the <span class="cn-word" data-tr="tarozi">scales</span>. Two months later the hotel asked for the same blend again, and she did not have to work anything out at all.</p>''',
        "questions": [
            {"text": "How many kilograms of the everyday tea were in the 60-kilogram blend?",
             "choices": ["20", "30", "40"], "answer": 2,
             "explanation": "2 : 1 nisbatda: 60 ning uchdan ikkisi — <b>40 kg</b>. 20 kg — qimmat choy."},
            {"text": "Why did the blend need more of the cheaper tea?",
             "choices": ["The hotel preferred the taste of Fergana tea.", "The target price of 8 dollars is closer to 6 than to 12.", "The fine tea was out of stock."], "answer": 1,
             "explanation": "Maqsad narx <b>arzon choyga yaqin</b> — demak arzon choy koʻproq boʻladi."},
        ],
    },

    # ── GMAT-13 — combined work                                    [Jenny]
    {
        "title":   "Two Printers, One Deadline",
        "summary": "GMAT-13 matni. Bosmaxonada ikki printer bitta buyurtmani birga chop etadi — birgalikdagi ish vaqti unumlarni qoʻshish bilan topiladi.",
        "order":   13,
        "grammar": [
            {"pattern": "working together",
             "meaning": "Birgalikda ishlab — vaqtlar emas, <b>unumlar</b> qoʻshiladi.",
             "examples": ["Working together, the two printers finish in 2 hours."]},
            {"pattern": "half of the job in an hour",
             "meaning": "Bir soatda ishning yarmi — unum, ishning soatlik qismi.",
             "examples": ["Together they do half of the job in an hour."]},
        ],
        "body": '''<p>A <span class="cn-word" data-tr="bosmaxona">print shop</span> in Bukhara received an <span class="cn-word" data-tr="shoshilinch">urgent</span> order on a Thursday morning: 3,000 <span class="cn-word" data-tr="risola, buklet">brochures</span> for a tourism <span class="cn-word" data-tr="koʻrgazma, yarmarka">fair</span> that opened at noon. The shop has two printers. The old one would need 6 hours to print the whole order alone. The new one would need 3 hours.</p>

<p>The <span class="cn-word" data-tr="smena boshligʻi">shift manager</span>, Sanjar, had a <span class="cn-word" data-tr="muddat">deadline</span>. The brochures had to be ready by 11 o'clock so that a van could deliver them before the fair opened. It was already 9.</p>

<p>A new employee said they would need four and a half hours, the average of 6 and 3. Sanjar laughed. "If the new printer can do it alone in 3 hours, adding a second printer cannot make it slower," he said.</p>

<p>He thought about each machine's <span class="cn-word" data-tr="unum, tezlik">rate</span> instead. In one hour the old printer does one sixth of the job and the new one does one third. <strong>Working together</strong>, they do one sixth plus two sixths, which is <strong>half of the job in an hour</strong>. The whole order would take 2 hours.</p>

<p>He started both printers at 9 o'clock. At 11, the last <span class="cn-word" data-tr="toʻplam, pachka">stack</span> of brochures came out warm, and the van left on time. On the way back, the driver asked why they had not simply used the new printer. "Then we would have finished at noon," Sanjar said, "and the fair would have opened without us."</p>

<p>Since that day, every urgent order in the shop starts with the same question: not how long each machine takes, but how much of the job each machine does in an hour.</p>''',
        "questions": [
            {"text": "How many hours did the two printers need working together?",
             "choices": ["2", "3", "4.5"], "answer": 0,
             "explanation": "1/6 + 1/3 = 1/2 ish soatiga — <b>2 soat</b>. 4.5 — vaqtlarning oddiy oʻrtachasi."},
            {"text": "What fraction of the job did the old printer do in one hour?",
             "choices": ["One third", "One half", "One sixth"], "answer": 2,
             "explanation": "Eski printer butun ishni 6 soatda bajaradi — soatiga <b>oltidan bir</b> qismi."},
            {"text": "Why was the new employee's answer impossible?",
             "choices": ["A second printer cannot make the job take longer.", "The printers cannot run at the same time.", "The order was too large for one van."], "answer": 0,
             "explanation": "Yangi printer yolgʻiz 3 soatda bajaradi — ikkinchi printer qoʻshilsa, ish <b>sekinlashmaydi</b>."},
        ],
    },

    # ── GMAT-14 — markup and discount                              [Guy]
    {
        "title":   "The Sale That Lost Money",
        "summary": "GMAT-14 matni. Kiyim doʻkoni avval 50% ustama qoʻyib, keyin 40% chegirma qiladi — va har bir koʻylakdan zarar koʻradi.",
        "order":   14,
        "grammar": [
            {"pattern": "marked up by 50 percent",
             "meaning": "50% ustama qoʻyildi — tannarx × 1.5.",
             "examples": ["The dresses were marked up by 50 percent."]},
            {"pattern": "40 percent off the marked price",
             "meaning": "Belgilangan narxdan 40% chegirma — belgilangan narx × 0.6.",
             "examples": ["The sign offered 40 percent off the marked price."]},
        ],
        "body": '''<p>Dilfuza owns a small clothing shop in Namangan. In September she bought 150 summer <span class="cn-word" data-tr="koʻylaklar">dresses</span> from a <span class="cn-word" data-tr="ulgurji sotuvchi">wholesaler</span> at 40 dollars each. As usual, the dresses were <strong>marked up by 50 percent</strong>, so each one went on the <span class="cn-word" data-tr="osma javon">rack</span> at 60 dollars.</p>

<p>The weather turned cold early, and the dresses did not sell. By November, all 150 were still in the <span class="cn-word" data-tr="ombor">storeroom</span>. Her assistant suggested a <span class="cn-word" data-tr="tugatish savdosi">clearance sale</span> and put a large sign in the window: <strong>40 percent off the marked price</strong>.</p>

<p>The sign worked, and the dresses were gone in a week. Dilfuza was pleased until she did the <span class="cn-word" data-tr="hisob-kitob">accounts</span>. Forty percent off 60 dollars is 24 dollars, so each dress sold for 36 dollars, four dollars less than it had cost. On 150 dresses, the sale had lost 600 dollars.</p>

<p>Her assistant was surprised. "We added fifty percent and took off only forty," she said. "Shouldn't we still be ten percent ahead?" Dilfuza explained that the two percentages were taken from different prices. The markup was half of 40 dollars, but the discount was four tenths of 60 dollars. One and a half times six tenths is nine tenths, so the sale price was only 90 percent of the cost: a ten percent <span class="cn-word" data-tr="zarar">loss</span>, not a ten percent profit.</p>

<p>For the next clearance, Dilfuza set a rule. The <span class="cn-word" data-tr="eng katta">largest</span> discount the shop can give without losing money on a 50 percent markup is one third, because one and a half times two thirds is exactly one. Anything more, and the shop pays its customers to take the clothes away.</p>''',
        "questions": [
            {"text": "What was the sale price of each dress?",
             "choices": ["$36", "$40", "$24"], "answer": 0,
             "explanation": "60 × 0.6 = <b>$36</b>. $24 — chegirmaning oʻzi; $40 — tannarx."},
            {"text": "How much money did the shop lose on the 150 dresses?",
             "choices": ["$150", "$600", "$900"], "answer": 1,
             "explanation": "Har biridan 40 − 36 = 4 dollar zarar; 150 × 4 = <b>$600</b>."},
            {"text": "What is the largest discount that avoids a loss on a 50 percent markup?",
             "choices": ["One half", "Fifty percent", "One third"], "answer": 2,
             "explanation": "1.5 × (1 − <b>1/3</b>) = 1 — tannarxga teng narx; undan katta chegirma zarar."},
        ],
    },

    # ── GMAT-15 — simple vs compound interest                      [Jenny]
    {
        "title":   "Simple or Compound?",
        "summary": "GMAT-15 matni. Kamola ikki bank taklifini solishtiradi: bir xil 10% stavka, lekin biri oddiy, biri murakkab foiz — uch yilda farq qancha?",
        "order":   15,
        "grammar": [
            {"pattern": "10 percent simple interest a year",
             "meaning": "Yillik 10% oddiy foiz — har yili bir xil summa.",
             "examples": ["The first bank offered 10 percent simple interest a year."]},
            {"pattern": "compounded annually",
             "meaning": "Har yili kapitallashtiriladi — foizga ham foiz hisoblanadi.",
             "examples": ["The second bank paid 10 percent, compounded annually."]},
        ],
        "body": '''<p>Kamola runs a small <span class="cn-word" data-tr="novvoyxona">bakery</span> in Tashkent and had saved 10 million sum for a new oven. She did not need the oven for three years, so she visited two banks to <span class="cn-word" data-tr="omonatga qoʻymoq">deposit</span> the money.</p>

<p>The first bank offered <strong>10 percent simple interest a year</strong>. Each year she would receive one million sum, always calculated on her original deposit. After three years she would have earned three million sum in <span class="cn-word" data-tr="foiz daromadi">interest</span>.</p>

<p>The second bank also offered 10 percent, but <strong>compounded annually</strong>. The <span class="cn-word" data-tr="bank xodimi">bank clerk</span> explained the difference with a pencil. In the first year, the interest is one million, just as in the first bank. In the second year, however, the interest is calculated on 11 million, so it comes to one million one hundred thousand. In the third year it is calculated on 12 million one hundred thousand, which gives one million two hundred and ten thousand.</p>

<p>Kamola added the three years together: one million, plus one million one hundred thousand, plus one million two hundred and ten thousand. The total interest was three million three hundred and ten thousand sum, which was 310 thousand more than at the first bank.</p>

<p>"It is the same rate," she said, "so why is it more?" The clerk smiled. "Because in the second and third years, your interest also earns interest."</p>

<p>Kamola chose the second bank. She also noticed something the clerk had not said: the extra money grew faster every year. Over three years the <span class="cn-word" data-tr="farq">difference</span> was small, but over ten or twenty years it would become large. She wrote the rule in her <span class="cn-word" data-tr="daftar">notebook</span>: when two offers have the same rate, read the next word. Simple means the interest stands still; compound means it grows.</p>

<p>Three years later, the <span class="cn-word" data-tr="pech">oven</span> cost a little more than she had planned, and the extra interest covered most of the <span class="cn-word" data-tr="narx oshishi">price rise</span>.</p>''',
        "questions": [
            {"text": "How much interest did the second bank pay over three years?",
             "choices": ["3 million sum", "3 million 310 thousand sum", "3 million 100 thousand sum"], "answer": 1,
             "explanation": "1,000,000 + 1,100,000 + 1,210,000 = <b>3,310,000</b> soʻm. 3 million — oddiy foiz."},
            {"text": "How much more did the compound offer earn than the simple one?",
             "choices": ["310 thousand sum", "210 thousand sum", "1 million sum"], "answer": 0,
             "explanation": "3,310,000 − 3,000,000 = <b>310,000</b> soʻm."},
            {"text": "Why did the second bank pay more at the same rate?",
             "choices": ["It charged a lower fee.", "Its rate rose each year.", "In later years the interest also earned interest."], "answer": 2,
             "explanation": "Murakkab foizda <b>foizga ham foiz</b> hisoblanadi."},
        ],
    },
]
