# -*- coding: utf-8 -*-
"""Prime GMAT Readings — GMAT-1 … GMAT-5 (pilot).

The third leg of each Prime GMAT lesson: the lesson's maths doing real work in an
ENGLISH business text, with Uzbek cn-word glosses, an "Exam English" block and audio.
Rules: corner/management/commands/toc_prime_gmat_readings.txt (overrides STYLE_GUIDE_CORNER).

No algebraic notation in the body — quantities in English words and plain numbers, so
the text survives TTS and trains turning a business sentence into maths.

Import, then audio (always pass --voice; the Matematika subject's default is not English):
    python manage.py import_corner corner/management/commands/_stories_prime_gmat_readings_01_05.py --author=prime
    python manage.py gen_corner_audio --collection="Prime GMAT Readings" --only 1 --voice en-US-JennyNeural
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

    # ── GMAT-1 — arithmetic without a calculator                  [Jenny]
    {
        "title":   "The Invoice Nobody Checked",
        "summary": "GMAT-1 matni. Kichik konsalting firmasi hisob-fakturani kalkulyatorsiz tekshiradi — sonni qulay boʻlaklarga ajratish va javobga qarab taxmin qilish.",
        "order":   1,
        "grammar": [
            {"pattern": "per hour / per license",
             "meaning": "Har soat / har litsenziya uchun — bu son <b>koʻpaytiriladi</b>.",
             "examples": ["The firm bills $45 per hour.", "Each license costs $25 per year."]},
            {"pattern": "in total",
             "meaning": "Jami — savol bitta yakuniy son soʻraydi.",
             "examples": ["How much did the company pay in total?"]},
            {"pattern": "closest to",
             "meaning": "Eng yaqin — taxmin qilishga ruxsat, aniq hisob shart emas.",
             "examples": ["The total is closest to which of the following?"]},
        ],
        "body": '''<p>Dilnoza runs the office of a small <span class="cn-word" data-tr="maslahat (konsalting) firmasi">consulting firm</span> in Tashkent. Every month a software <span class="cn-word" data-tr="yetkazib beruvchi">supplier</span> sends an <span class="cn-word" data-tr="hisob-faktura">invoice</span>, and every month someone pays it without reading it.</p>

<p>This month Dilnoza read it. The firm had bought licenses for 198 employees at 25 dollars <strong>per license</strong>. The invoice asked for 5,500 dollars.</p>

<p>She did not reach for a <span class="cn-word" data-tr="kalkulyator">calculator</span>. Two hundred licenses at 25 dollars would be 5,000 dollars, she thought, because 25 is a quarter of 100. The firm had bought two fewer, so the real figure was 50 dollars less: 4,950 dollars <strong>in total</strong>. Even without the correction, the invoice was <span class="cn-word" data-tr="aniq, ravshan">clearly</span> too high.</p>

<p>She called the supplier. A clerk had typed 220 licenses instead of 198. The <span class="cn-word" data-tr="tuzatilgan">corrected</span> invoice arrived the same afternoon.</p>

<p>Dilnoza then checked the second line of the invoice: 36 hours of <span class="cn-word" data-tr="texnik yordam">technical support</span> at 45 dollars <strong>per hour</strong>. She split the 36 hours into 30 and 6. Thirty hours cost 1,350 dollars and six hours cost 270, so the support came to 1,620 dollars. That line was right.</p>

<p>Her <span class="cn-word" data-tr="rahbar">manager</span> asked how she had found the <span class="cn-word" data-tr="xato">error</span> so quickly. "I didn't calculate it exactly at first," she said. "I only asked which number the answer should be <strong>closest to</strong>. When the invoice was far from that, I knew something was wrong."</p>

<p>Since then, the firm checks every invoice the same way: <span class="cn-word" data-tr="taxmin qilmoq">estimate</span> first, then calculate the lines that look <span class="cn-word" data-tr="shubhali">suspicious</span>.</p>''',
        "questions": [
            {"text": "What was the correct cost of the licenses?",
             "choices": ["$5,500", "$5,000", "$4,950"], "answer": 2,
             "explanation": "198 × 25 = 5,000 − 50 = <b>$4,950</b>. $5,000 — yaxlitlangan, tuzatilmagan javob; $5,500 — xato hisob-faktura."},
            {"text": "How did Dilnoza calculate the cost of 36 hours of support?",
             "choices": ["She split 36 into 30 and 6.", "She rounded 45 up to 50.", "She used a calculator."], "answer": 0,
             "explanation": "Matnda: 36 soatni <b>30 va 6</b> ga ajratgan: 1,350 + 270 = 1,620."},
            {"text": "Why did the original invoice ask for $5,500?",
             "choices": ["The price per license had risen.", "A clerk typed 220 licenses instead of 198.", "The support hours were added twice."], "answer": 1,
             "explanation": "Xodim 198 oʻrniga <b>220</b> litsenziya yozgan: 220 × 25 = 5,500."},
        ],
    },

    # ── GMAT-2 — factors and multiples                            [Guy]
    {
        "title":   "Twelve to a Carton",
        "summary": "GMAT-2 matni. Ombor mahsulotlarni teng qutilarga joylashtiradi — qaysi quti oʻlchamida hech narsa ortib qolmasligi boʻluvchilar bilan aniqlanadi.",
        "order":   2,
        "grammar": [
            {"pattern": "with none left over",
             "meaning": "Hech narsa ortib qolmasdan — son <b>boʻluvchi</b> boʻlishi kerak.",
             "examples": ["The jars must be packed with none left over."]},
            {"pattern": "at least / at most",
             "meaning": "Kamida / koʻpi bilan — chegaralarning <b>oʻzi ham</b> kiradi.",
             "examples": ["Each carton holds at least 10 and at most 20 jars."]},
        ],
        "body": '''<p>A small <span class="cn-word" data-tr="ombor">warehouse</span> near Samarkand packs jars of apricot jam for a <span class="cn-word" data-tr="supermarketlar tarmogʻi">supermarket chain</span>. This week a single order arrived: 252 jars, to be packed into identical <span class="cn-word" data-tr="karton quti">cartons</span> <strong>with none left over</strong>.</p>

<p>The warehouse has cartons in several sizes, but the supermarket set a rule: each carton must hold <strong>at least</strong> 10 jars and <strong>at most</strong> 20, because heavier cartons are hard to lift and lighter ones waste space on the <span class="cn-word" data-tr="yuk mashinasi">truck</span>.</p>

<p>Sardor, the <span class="cn-word" data-tr="smena boshligʻi">shift supervisor</span>, wrote the number 252 on a board and began to look for the sizes that <span class="cn-word" data-tr="qoldiqsiz boʻlinadi">divide it evenly</span>. Two and three came first, since the number is even and its digits add up to nine. Seven followed, because seven times thirty-six is 252.</p>

<p>From there he listed the pairs: twelve cartons of twenty-one, fourteen of eighteen, eighteen of fourteen, twenty-one of twelve. Only three sizes fitted the supermarket's rule: 12, 14 and 18 jars per carton.</p>

<p>He chose 12. "Twelve is the size our <span class="cn-word" data-tr="mijozlar">customers</span> already know," he said, "and it gives us exactly 21 cartons." A carton of 15 would have been easier to <span class="cn-word" data-tr="koʻtarmoq">carry</span>, but 252 jars would have left 12 jars over.</p>

<p>The order left on Friday, every carton full and none half empty.</p>''',
        "questions": [
            {"text": "How many carton sizes from 10 to 20 jars could pack all 252 jars with none left over?",
             "choices": ["2", "3", "4"], "answer": 1,
             "explanation": "252 ning 10 dan 20 gacha boʻluvchilari: 12, 14, 18 — <b>3</b> ta."},
            {"text": "How many cartons did Sardor use?",
             "choices": ["21", "18", "12"], "answer": 0,
             "explanation": "252 ÷ 12 = <b>21</b>. 12 — bitta qutidagi bankalar soni, qutilar soni emas."},
            {"text": "Why could Sardor not use cartons of 15 jars?",
             "choices": ["Fifteen is more than the supermarket allowed.", "The cartons of 15 were too heavy.", "252 is not divisible by 15, so jars would be left over."], "answer": 2,
             "explanation": "252 ÷ 15 = 16, qoldiq <b>12</b> — 15 boʻluvchi emas."},
        ],
    },

    # ── GMAT-3 — LCM in a schedule                                [Jenny]
    {
        "title":   "When the Two Machines Stop Together",
        "summary": "GMAT-3 matni. Fabrikada ikki mashina turli oraliqda toʻxtatiladi — ikkalasi birga toʻxtaydigan kun eng kichik umumiy karrali (EKUK) bilan topiladi.",
        "order":   3,
        "grammar": [
            {"pattern": "every 6 days / every 8 days",
             "meaning": "Har 6 kunda / har 8 kunda — bu takrorlanish, demak savol <b>EKUK</b> haqida.",
             "examples": ["The press is cleaned every 6 days."]},
            {"pattern": "on the same day again",
             "meaning": "Yana bir kunda — birinchi umumiy karrali, eng kichigi.",
             "examples": ["When will both machines stop on the same day again?"]},
        ],
        "body": '''<p>At a textile factory in Fergana, two machines need regular <span class="cn-word" data-tr="texnik xizmat koʻrsatish">maintenance</span>. The <span class="cn-word" data-tr="toʻquv dastgohi">loom</span> is stopped for cleaning <strong>every 6 days</strong>. The <span class="cn-word" data-tr="boʻyash mashinasi">dyeing machine</span> is stopped for inspection every 8 days. Both were stopped on the first of the month.</p>

<p>Each stop costs the factory a <span class="cn-word" data-tr="smena">shift</span> of work, and the <span class="cn-word" data-tr="ishlab chiqarish boshligʻi">production manager</span>, Malika, wanted the two stops to happen <strong>on the same day again</strong> as soon as possible, so that the workers could be moved to other tasks once instead of twice.</p>

<p>A junior engineer suggested multiplying: six times eight is forty-eight, so the machines would meet again in 48 days. Malika shook her head. "That is a day they meet," she said, "but not the first one."</p>

<p>She wrote the stops for the loom: days 6, 12, 18, 24. Then for the dyeing machine: days 8, 16, 24. The first number on both lists was 24. Six and eight share a <span class="cn-word" data-tr="koʻpaytuvchi">factor</span> of two, so the product counts that two twice.</p>

<p>The factory now plans one <span class="cn-word" data-tr="birlashtirilgan">combined</span> stop every 24 days, and one separate stop for each machine in between. Over a year, the change saves several shifts of <span class="cn-word" data-tr="ishlab chiqarish">production</span>. The junior engineer now checks for a shared factor before he multiplies any two schedules together.</p>''',
        "questions": [
            {"text": "After how many days did both machines first stop on the same day again?",
             "choices": ["14", "24", "48"], "answer": 1,
             "explanation": "EKUK(6, 8) = <b>24</b>. 48 — koʻpaytma: umumiy kun, lekin birinchisi emas; 14 — qoʻshilgan."},
            {"text": "Why was the junior engineer's answer of 48 days wrong?",
             "choices": ["Six and eight share a factor of two, so 48 is not the first common day.", "The machines are not stopped on the first of the month.", "He added the numbers instead of multiplying."], "answer": 0,
             "explanation": "6 va 8 ning <b>umumiy boʻluvchisi 2</b> — koʻpaytma uni ikki marta hisoblaydi."},
            {"text": "On which day of the cycle was the dyeing machine stopped for the second time?",
             "choices": ["Day 12", "Day 16", "Day 24"], "answer": 1,
             "explanation": "Har 8 kunda: 8, <b>16</b>, 24. 12 — dastgohning ikkinchi toʻxtashi."},
        ],
    },

    # ── GMAT-4 — positive and negative                             [Guy]
    {
        "title":   "Red Numbers on the Ledger",
        "summary": "GMAT-4 matni. Kichik doʻkonning haftalik daftari: foyda va zarar musbat va manfiy sonlar sifatida qoʻshiladi.",
        "order":   4,
        "grammar": [
            {"pattern": "a loss of / a gain of",
             "meaning": "Zarar — manfiy son, foyda — musbat son.",
             "examples": ["Monday showed a loss of $40.", "Thursday brought a gain of $60."]},
            {"pattern": "net result",
             "meaning": "Sof natija — barcha musbat va manfiy sonlarning yigʻindisi.",
             "examples": ["What was the net result for the week?"]},
        ],
        "body": '''<p>Jasur owns a small <span class="cn-word" data-tr="kanselyariya doʻkoni">stationery shop</span>. In his <span class="cn-word" data-tr="hisob daftari">ledger</span> he writes each day's profit in black <span class="cn-word" data-tr="siyoh">ink</span> and each day's <span class="cn-word" data-tr="zarar">loss</span> in red, just as his father did.</p>

<p>The first week of the school holidays was difficult. Monday showed <strong>a loss of</strong> 40 dollars after a <span class="cn-word" data-tr="yetkazib berilgan yuk">delivery</span> of notebooks arrived <span class="cn-word" data-tr="shikastlangan">damaged</span>. Tuesday brought a small <span class="cn-word" data-tr="foyda">profit</span> of 25 dollars. On Wednesday the shop lost another 15 dollars, because Jasur paid for a broken window. On Thursday a school ordered pens for its new teachers, and the shop made 60 dollars.</p>

<p>On Friday evening his daughter asked how the week had gone. "Two red days and two black days," Jasur said. "So we <span class="cn-word" data-tr="na foyda, na zarar qildik">broke even</span>?"</p>

<p>She added the black numbers first, 25 and 60, which made 85. Then the red numbers, 40 and 15, which made 55. The difference was 30 dollars in black. "Not even," she said. "We are 30 dollars ahead."</p>

<p>Jasur had counted the days instead of the money. Two losses and two gains say nothing about the <strong>net result</strong>; only the <span class="cn-word" data-tr="miqdorlar">amounts</span> do. A single large gain can <span class="cn-word" data-tr="qoplamoq">cover</span> several small losses, and a single large loss can <span class="cn-word" data-tr="yoʻq qilib yubormoq">wipe out</span> a good week.</p>

<p>From then on, Jasur wrote the weekly <span class="cn-word" data-tr="jami">total</span> at the bottom of every page, in black or red, so the number would speak for itself.</p>''',
        "questions": [
            {"text": "What was the shop's net result for the four days?",
             "choices": ["A loss of $30", "A profit of $30", "A profit of $140"], "answer": 1,
             "explanation": "25 + 60 − 40 − 15 = <b>+30</b>. $140 — barcha sonlarni ishorasiz qoʻshgan javob."},
            {"text": "Why did Jasur think the shop had broken even?",
             "choices": ["He counted two red days and two black days.", "He forgot Thursday's order.", "He subtracted the gains from the losses."], "answer": 0,
             "explanation": "U <b>kunlarni</b> sanagan, pulni emas — ikki qizil va ikki qora kun."},
        ],
    },

    # ── GMAT-5 — percent change                                   [Jenny]
    {
        "title":   "Up Twenty, Down Twenty",
        "summary": "GMAT-5 matni. Doʻkon narxni avval 20% oshiradi, keyin 20% kamaytiradi — va narx boshlangʻich darajaga qaytmaydi.",
        "order":   5,
        "grammar": [
            {"pattern": "raised the price by 20 percent",
             "meaning": "Narxni 20 foizga oshirdi — foiz <b>eski</b> narxdan olinadi.",
             "examples": ["The shop raised the price by 20 percent."]},
            {"pattern": "what percent of the original price",
             "meaning": "Boshlangʻich narxning necha foizi — yangi narx ÷ eski narx.",
             "examples": ["The final price was what percent of the original price?"]},
        ],
        "body": '''<p>In March, a shop selling <span class="cn-word" data-tr="maishiy texnika">kitchen appliances</span> in Bukhara <strong>raised the price by 20 percent</strong> on its best-selling <span class="cn-word" data-tr="choynak">kettle</span>. The kettle had cost 50 dollars, so the new price was 60.</p>

<p><span class="cn-word" data-tr="sotuvlar">Sales</span> fell <span class="cn-word" data-tr="keskin">sharply</span>. In May, the owner, Kamola, decided to <span class="cn-word" data-tr="bekor qilmoq">undo</span> the change and told her <span class="cn-word" data-tr="yordamchi">assistant</span> to cut the price by 20 percent. The assistant changed the price tag to 48 dollars.</p>

<p>A <span class="cn-word" data-tr="doimiy xaridor">regular customer</span> noticed at once. "In February this kettle cost 50," he said. "You raised it by twenty percent and lowered it by twenty percent. Why is it 48?"</p>

<p>Kamola explained that the two percentages were taken from different numbers. The <span class="cn-word" data-tr="oshish">increase</span> was 20 percent of 50, which is 10 dollars. The <span class="cn-word" data-tr="kamayish">decrease</span> was 20 percent of 60, which is 12 dollars. The second change was larger because it started from a larger price.</p>

<p>She worked out what <strong>percent of the original price</strong> the kettle now cost: 48 out of 50, or 96 percent. To return to exactly 50 dollars, the price should have been reduced by 10 dollars, which is only about 16.7 percent of 60.</p>

<p>The customer bought the kettle at 48, pleased to have <span class="cn-word" data-tr="tejamoq">saved</span> two dollars on a <span class="cn-word" data-tr="hisob-kitob xatosi">pricing mistake</span>. Kamola changed her rule the same day: every price change in the shop is now written as a new price, not as a percentage.</p>''',
        "questions": [
            {"text": "After the increase and the decrease, the kettle's price was what percent of its original price?",
             "choices": ["100%", "96%", "80%"], "answer": 1,
             "explanation": "48 ÷ 50 = <b>96%</b>. 100% — ikki foiz bir-birini yoʻqotadi deb oʻylagan javob."},
            {"text": "By how many dollars did the May decrease lower the price?",
             "choices": ["$10", "$12", "$2"], "answer": 1,
             "explanation": "60 ning 20 foizi = <b>$12</b>. $10 — 50 ning 20 foizi, mart oʻsishi."},
            {"text": "Why was the decrease larger than the increase?",
             "choices": ["The decrease was taken from a larger price.", "The assistant made a typing error.", "The decrease was a larger percentage."], "answer": 0,
             "explanation": "Ikkalasi ham 20%, lekin kamayish <b>kattaroq narxdan</b> (60) olingan."},
        ],
    },
]
