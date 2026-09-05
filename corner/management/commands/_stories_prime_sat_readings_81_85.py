# -*- coding: utf-8 -*-
"""Prime SAT Readings — 81-85 (Blok E: taktika va Desmos).

Overrides in corner/management/commands/toc_prime_sat_readings.txt.

⚠️ Matn INGLIZCHA · summary, cn-word glosses, explanation OʻZBEKCHA.
⚠️ ⛔ Tanada algebraik belgi YOʻQ — miqdorlar ingliz tilida aytiladi.
⚠️ SUBJECT/COLLECTION oldingi fayldan aynan koʻchirilgan.

Blok E darslari usul haqida, shuning uchun matnlar ham fikrlash usuli
haqida: bitta aniq holatni sinash, oxiridan teskari yurish, ikki chiziq
kesishgan nuqta, bir vaqtda bitta narsani oʻzgartirish, va ikki cheklov.

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_81_85.py \\
        --author=prime
"""

SUBJECT = {
    "name": "Matematika",
    "summary": "Matematika: hayotdagi matnlar, atamalar va matematik hikoyalar.",
    "icon": "bi-calculator",
    "color": "#f59e0b",
    "order": 7,
}

COLLECTION = {
    "title": "Prime SAT Readings",
    "description": (
        "Prime SAT darslarining oʻqish matnlari — ingliz tilida, audio bilan. "
        "Har bir matn oʻz darsining matematikasini haqiqiy vaziyatda koʻrsatadi: "
        "asosiy mashq — inglizcha jumlani matematikaga aylantirish."
    ),
    "order": 3,
}


STORIES = [

# ─────────────────────────────────────────────────────────────────────
# 81 — testing one concrete case (a workshop's production note)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 81,
    "title": "The Batch of Fifty",
    "summary": (
        "Ikki ming bankani qilishdan oldin ellikta qilib koʻring — bitta aniq "
        "misol formula yashirgan narsani ochadi (SAT-81)."
    ),
    "body": """
<p>The order was for two thousand jars of apricot jam, and the <span class="cn-word" data-tr="ustaxona, sex">workshop</span>
had never made more than three hundred.</p>

<p>On paper the <span class="cn-word" data-tr="hisob-kitob">arithmetic</span> looked finished before it began. The old
<span class="cn-word" data-tr="retsept">recipe</span> made fifty jars from twelve kilos of fruit, so two thousand jars
would want forty times as much — four hundred and eighty kilos. The
owner wrote the number down, and then did not order the fruit.</p>

<p>Instead she made fifty jars again, and <span class="cn-word" data-tr="tortdi, oʻlchadi">weighed</span> everything.</p>

<p>Twelve kilos went into the <span class="cn-word" data-tr="qozon">pan</span>. What came out filled only forty-four
jars. Some fruit stayed on the stones, some <span class="cn-word" data-tr="yopishib qoldi">clung</span> to the sides, and a
good deal left as <span class="cn-word" data-tr="bugʻ">steam</span>. To
fill a true fifty she needed fourteen kilos, not twelve. Scaled up, the
order needed five hundred and sixty kilos — eighty more than the paper
had <span class="cn-word" data-tr="vaʼda qilgan edi">promised</span>, and enough to have stopped the line on the second day.</p>

<p>"The recipe is not wrong," she told the two women who work the
pans. "It is just not a <span class="cn-word" data-tr="oʻlchov, oʻlcham">
measurement</span>. Nobody ever weighed it."</p>

<p>There is a <span class="cn-word" data-tr="odat">habit</span> hidden in that morning, and it is worth more than the
eighty kilos. <strong>Before trusting a rule, run one concrete case
through it and see what comes out the other end.</strong> A single real
example costs an hour. A rule that has never met a real example can cost
a <span class="cn-word" data-tr="mavsum">season</span>.</p>

<p>The jam went out on time. The note she <span class="cn-word" data-tr="qadab qoʻygan">pinned</span> above the <span class="cn-word" data-tr="oʻchoq">stove</span> is still
there: <i>weigh the small batch first</i>.</p>
""",
    "grammar": [
        {"pattern": "forty times as much",
         "meaning": "qirq barobar koʻp — SAT nisbatni shu qurilma bilan aytadi.",
         "examples": ["Two thousand jars need forty times as much fruit as fifty."]},
        {"pattern": "run one case through it",
         "meaning": "bitta aniq holatni qoidadan oʻtkazib koʻring — son qoʻyish taktikasi.",
         "examples": ["Run one case through the formula before trusting it."]},
        {"pattern": "scaled up",
         "meaning": "kattalashtirilganda, koʻpaytirilganda.",
         "examples": ["Scaled up, the order needed 560 kilos."]},
    ],
    "questions": [
        {"text": "Why did the owner not order 480 kilos?",
         "choices": ["The supplier had none in stock",
                     "She wanted to test the recipe on a real batch first",
                     "The order had been cancelled",
                     "She could not afford it"],
         "answer": 1,
         "explanation": "U qoidaga ishonishdan oldin bitta haqiqiy holatni "
                        "sinab koʻrmoqchi boʻldi."},
        {"text": "The tested batch needed 14 kilos for 50 jars. At that rate, how "
                 "much fruit does an order of 500 jars need?",
         "choices": ["140 kilos", "120 kilos", "560 kilos", "700 kilos"],
         "answer": 0,
         "explanation": "500 — 50 ning oʻn barobari, demak 14 × 10 = 140 kilo."},
        {"text": "What is the point of the note above the stove?",
         "choices": ["Small batches taste better",
                     "Weighing is required by law",
                     "A rule should be tested on one real case before it is trusted",
                     "Recipes should never be changed"],
         "answer": 2,
         "explanation": "Bitta aniq misol qoidaning haqiqatda nima "
                        "berishini koʻrsatadi."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 82 — working backwards (a theatre call sheet)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 82,
    "title": "Backwards From the Curtain",
    "summary": (
        "Sahna boshqaruvchisi kunni boshidan emas, oxiridan — parda "
        "koʻtariladigan daqiqadan boshlab tuzadi (SAT-82)."
    ),
    "body": """
<p>Every <span class="cn-word" data-tr="jadval">schedule</span> in a theatre is written in the wrong <span class="cn-word" data-tr="yoʻnalish">direction</span> on
purpose.</p>

<p>There is exactly one time in the day that cannot move: the
<span class="cn-word" data-tr="parda">curtain</span> goes up at seven.
Everything else is worked out from there, backwards, one step at a
time. The doors open half an hour before the <span class="cn-word" data-tr="tomoshabinlar">audience</span> is <span class="cn-word" data-tr="joylashtirilgan">seated</span>, so the
doors open at half past six. The stage must be clear before the doors
open, so the sound check has to be finished by six. A sound check takes
forty-five minutes, so it begins at a quarter past five.</p>

<p>The actors are called an hour before that, at a quarter past four,
which means the set has to be built and the floor <span class="cn-word" data-tr="supurilgan">swept</span> by four — and
so, at last, the <span class="cn-word" data-tr="ishchi guruh">crew</span>'s start time appears at the bottom of the page:
one o'clock, four hours before anyone would have guessed.</p>

<p><strong>Nothing on that sheet was decided by starting at the
beginning.</strong> Had the <span class="cn-word" data-tr="boshqaruvchi">manager</span> begun at one and worked <span class="cn-word" data-tr="oldinga, boshidan">forwards</span>,
she would have had to <span class="cn-word" data-tr="taxmin qilmoq">guess</span> how long each job takes and <span class="cn-word" data-tr="umid qilmoq">hope</span> the total
landed on seven. Instead she started from the only fixed point she had
and let each step tell her the one before it.</p>

<p>It is the same move a good test-taker makes with a
<span class="cn-word" data-tr="variant, tanlov">multiple-choice</span>
question. The answer is already <span class="cn-word" data-tr="bosib chiqarilgan">printed</span> on the page. Rather than
building a solution forwards and hoping it lands on one of the four,
you can begin at the finish and check which one <span class="cn-word"
data-tr="mos keladi">fits</span>.</p>

<p>The curtain has never once gone up late.</p>
""",
    "grammar": [
        {"pattern": "worked out from there, backwards",
         "meaning": "oʻsha nuqtadan teskari yurib hisoblanadi.",
         "examples": ["The start time is worked out backwards from the curtain."]},
        {"pattern": "half an hour before / an hour before that",
         "meaning": "yarim soat oldin / undan bir soat oldin — vaqt zanjiri.",
         "examples": ["The doors open half an hour before the audience is seated."]},
        {"pattern": "the only fixed point",
         "meaning": "yagona qoʻzgʻalmas nuqta — hisob shundan boshlanadi.",
         "examples": ["Start from the only fixed point you have."]},
    ],
    "questions": [
        {"text": "Which time in the day cannot be moved?",
         "choices": ["The crew's start time", "The actors' call",
                     "The curtain at seven", "The sound check"],
         "answer": 2,
         "explanation": "Parda soat yettida koʻtariladi — qolgan hamma "
                        "narsa shundan hisoblanadi."},
        {"text": "The sound check must finish by six and takes forty-five minutes. "
                 "When does it start?",
         "choices": ["A quarter past five", "Half past five",
                     "A quarter to six", "Five o'clock"],
         "answer": 0,
         "explanation": "Oltidan 45 daqiqa orqaga: 5:15."},
        {"text": "What does the theatre's method have in common with a "
                 "multiple-choice question?",
         "choices": ["Both take exactly four hours",
                     "Both begin at the end and check backwards",
                     "Both require a written schedule",
                     "Both depend on guessing well"],
         "answer": 1,
         "explanation": "Javob allaqachon sahifada turibdi — oxiridan "
                        "boshlab tekshirish mumkin."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 83 — where two lines cross (a small business)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 83,
    "title": "The Cup That Paid the Rent",
    "summary": (
        "Choyxonachi har kuni bir savolga javob beradi: bugun nechanchi "
        "piyoladan keyin foyda boshlanadi (SAT-83)."
    ),
    "body": """
<p>Two numbers describe the <span class="cn-word" data-tr="rasta, doʻkoncha">stall</span>, and they <span class="cn-word" data-tr="oʻzini tutmoq">behave</span> completely
differently.</p>

<p>The first is the <span class="cn-word" data-tr="ijara">rent</span>.
It is ninety dollars a day, and it is ninety dollars whether she sells
four hundred cups or none at all. It does not care. The second is the
cost of the tea itself: two dollars a cup, every cup, and nothing when
the stall is <span class="cn-word" data-tr="yopiq">shut</span>.</p>

<p>Against those she sets one number going the other way. Each cup sells
for five dollars.</p>

<p>Draw the day on paper and you get two lines. One line is what she
<span class="cn-word" data-tr="qarzi bor, toʻlashi kerak">owes</span> — it starts high, at ninety, and climbs by two with every cup. The
other is what she takes — it starts at nothing and climbs by five. The
second line is <span class="cn-word" data-tr="tikroq">steeper</span>, so however far behind it begins,
<strong>it must eventually catch the first</strong>. The only question
is where.</p>

<p>Three dollars of every cup goes towards the rent, so it takes thirty
cups to cover it. Sell twenty-nine and she has lost money. Sell
thirty-one and the day is hers. That <span class="cn-word" data-tr="kesishish nuqtasi">crossing point</span> has a name in her
<span class="cn-word" data-tr="daftar">notebook</span> and in every business <span class="cn-word" data-tr="darslik">textbook</span>, and it is the number she
watches all morning.</p>

<p>What matters for a test is the <span class="cn-word" data-tr="fikrning shakli">shape of the thought</span>, not the tea.
Two quantities, each changing at its own <span class="cn-word" data-tr="barqaror, oʻzgarmas">steady</span> rate, and a question
about the moment they are <span class="cn-word" data-tr="teng">equal</span>
— that is one line crossing another, and it is the same picture whether
the answer is a price, a <span class="cn-word" data-tr="masofa">distance</span> or a day.</p>
""",
    "grammar": [
        {"pattern": "whether she sells four hundred cups or none at all",
         "meaning": "koʻp sotsa ham, hech sotmasa ham — oʻzgarmas xarajat belgisi.",
         "examples": ["The rent is $90 whether the stall is busy or empty."]},
        {"pattern": "climbs by two with every cup",
         "meaning": "har bir piyolada ikkiga ortadi — bu qiyalik.",
         "examples": ["The cost climbs by $2 with every cup she makes."]},
        {"pattern": "the moment they are equal",
         "meaning": "ular tenglashgan lahza — ikki chiziqning kesishishi.",
         "examples": ["The question asks for the moment the two totals are equal."]},
    ],
    "questions": [
        {"text": "Why does the second line always catch the first?",
         "choices": ["It starts higher", "It rises more steeply",
                     "The rent falls during the day", "It has no starting value"],
         "answer": 1,
         "explanation": "Har bir piyolada u beshga koʻtariladi, birinchisi esa "
                        "ikkiga — tikroq chiziq baribir yetib oladi."},
        {"text": "How much of each cup's price is left after the tea is paid for?",
         "choices": ["Two dollars", "Three dollars", "Five dollars", "Ninety cents"],
         "answer": 1,
         "explanation": "5 dollardan 2 dollar choyga ketadi, 3 dollar qoladi."},
        {"text": "If the rent rose to $120 and nothing else changed, how many cups "
                 "would she need to cover it?",
         "choices": ["24 cups", "60 cups", "40 cups", "30 cups"],
         "answer": 2,
         "explanation": "Har bir piyoladan 3 dollar qoladi, va 120 ÷ 3 = 40."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 84 — change one thing at a time (a trial report)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 84,
    "title": "Four Greenhouses, One Difference",
    "summary": (
        "Toʻrtta issiqxona, hamma narsa bir xil — faqat chiroq soatlari "
        "boshqa. Bir vaqtda bitta narsani oʻzgartirish (SAT-84)."
    ),
    "body": """
<p>The <span class="cn-word" data-tr="sinov, tajriba">trial</span> was designed to be boring, and that was the point.</p>

<p>Four greenhouses stood in a row, built to the same plan and planted on
the same morning with the same <span class="cn-word" data-tr="nav">variety</span> of tomato. They got the same
water, the same <span class="cn-word" data-tr="tuproq">soil</span>, the same <span class="cn-word" data-tr="issiqlik">warmth</span>. One thing, and only one thing,
was allowed to differ: the hours of extra
<span class="cn-word" data-tr="sunʼiy yoritish">artificial light</span>
given each evening. The first house got none, the second two hours, the
third four and the fourth six.</p>

<p>The <span class="cn-word" data-tr="hosil">harvest</span>, in kilograms for each square metre of floor, came out at
eighteen, twenty-two, twenty-six and twenty-seven.</p>

<p>Read that row slowly, because it says two separate things. The first
three steps each added four kilograms, which is a strong and steady
<span class="cn-word" data-tr="qaytim, natija">return</span>. The last step added one. Somewhere between four extra hours and
six, the plants stopped being able to use the light, and the grower is
now paying for <span class="cn-word" data-tr="elektr energiyasi">electricity</span> that the <span class="cn-word" data-tr="ekin, hosil">crop</span> cannot spend.</p>

<p>None of that could have been said if the trial had been run any other
way. <strong>Had the fourth house also been given richer soil, its
extra kilogram would have belonged to nobody</strong> — light or soil,
with no way to tell them apart. Holding everything steady and moving one
<span class="cn-word" data-tr="kattalik, sozlanadigan son">quantity</span>
across a range is the oldest <span class="cn-word" data-tr="ishonchli">reliable</span> trick in <span class="cn-word" data-tr="tajriba ishi">experimental work</span>, and
it is exactly what a slider does on a screen: one number moves, the
picture answers, and the answer belongs to that number alone.</p>
""",
    "grammar": [
        {"pattern": "one thing, and only one thing, was allowed to differ",
         "meaning": "faqat bitta narsa farq qilishiga ruxsat berildi.",
         "examples": ["Only one quantity was allowed to differ between the trials."]},
        {"pattern": "across a range",
         "meaning": "bir qator qiymatlar boʻylab — surgichni surish shu.",
         "examples": ["Move one quantity across a range and watch the result."]},
        {"pattern": "the answer belongs to that number alone",
         "meaning": "natija aynan oʻsha songa tegishli — sabab aniq.",
         "examples": ["If only one thing changed, the answer belongs to it alone."]},
    ],
    "questions": [
        {"text": "Why were the greenhouses built and planted identically?",
         "choices": ["To reduce the cost of the trial",
                     "So that any difference in harvest could only be caused by the light",
                     "Because the seeds required it",
                     "To make the harvest easier to collect"],
         "answer": 1,
         "explanation": "Bitta narsadan boshqasi bir xil boʻlsa, farq faqat "
                        "oʻsha narsadan kelib chiqadi."},
        {"text": "How much more did the third greenhouse yield than the first?",
         "choices": ["Four kilograms", "Eight kilograms",
                     "Twenty-six kilograms", "One kilogram"],
         "answer": 1,
         "explanation": "26 − 18 = 8 kilogramm har bir kvadrat metrga."},
        {"text": "What does the last step in the row suggest?",
         "choices": ["The measurement was taken wrongly",
                     "More light always gives more fruit",
                     "The extra light is no longer worth what it costs",
                     "The fourth house was planted later"],
         "answer": 2,
         "explanation": "Oxirgi ikki soat atigi bir kilogramm qoʻshdi — "
                        "elektr esa oʻsha narxda."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 85 — two constraints (school committee minutes)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 85,
    "title": "What Will Fit in the Hall",
    "summary": (
        "Ikkita cheklov bor — zal va budjet — va rejani ulardan kichigi "
        "belgilaydi (SAT-85)."
    ),
    "body": """
<p>Minutes of the concert <span class="cn-word" data-tr="qoʻmita">committee</span>, Tuesday evening. Present: four
teachers and two pupils.</p>

<p>The hall was measured last week. With the <span class="cn-word" data-tr="oʻtish yoʻlaklari">aisles</span> the fire officer
requires, it holds at most one hundred and eighty people. That number
was written at the top of the board and nobody <span class="cn-word" data-tr="bahslashdi">argued</span> with it.</p>

<p>The second number came from the <span class="cn-word" data-tr="gʻaznachi">treasurer</span>. Chairs must be
<span class="cn-word" data-tr="ijaraga olmoq">hired</span> from the
town at five dollars each, and the whole
<span class="cn-word" data-tr="budjet, mablagʻ">budget</span> for the
evening is eight hundred dollars. Eight hundred divided by five is one
hundred and sixty, and there the plan stopped.</p>

<p>The room allows a hundred and eighty. The money allows a hundred and
sixty. <strong>Both limits are real, and the smaller one is the one
that decides.</strong> Twenty seats the hall would happily hold will
stand <span class="cn-word" data-tr="boʻsh">empty</span> because nobody can pay for them. The committee agreed to
<span class="cn-word" data-tr="chop etmoq">print</span> one hundred and sixty <span class="cn-word" data-tr="chiptalar">tickets</span> and to keep forty of those for
families, which is a third limit and, as it happens, not a
<span class="cn-word" data-tr="cheklovchi, hal qiluvchi">binding</span>
one — forty is comfortably inside a hundred and sixty.</p>

<p>Any real plan is a small pile of <span class="cn-word" data-tr="shartlar">conditions</span> like these, all true at
once. A choice is only <span class="cn-word" data-tr="amalga oshadigan">workable</span> if it <span class="cn-word" data-tr="barcha shartlardan oʻtadi">survives</span> every one of them, and
the interesting part is almost never a single condition. It is finding
which of them is actually holding the plan back — and, sometimes,
discovering that the one everybody was arguing about was not.</p>
""",
    "grammar": [
        {"pattern": "at most one hundred and eighty",
         "meaning": "koʻpi bilan 180 — bu ≤ belgisi.",
         "examples": ["The hall holds at most 180 people."]},
        {"pattern": "the smaller one is the one that decides",
         "meaning": "ikki cheklovdan kichigi rejani belgilaydi.",
         "examples": ["Both limits are real, but the smaller one decides."]},
        {"pattern": "a choice is only workable if it survives every one of them",
         "meaning": "yechim barcha shartlarni birdan qanoatlantirishi kerak.",
         "examples": ["A plan is workable only if it satisfies every condition."]},
    ],
    "questions": [
        {"text": "How many chairs can the budget pay for?",
         "choices": ["One hundred and eighty", "One hundred and sixty",
                     "Eight hundred", "Forty"],
         "answer": 1,
         "explanation": "800 dollarni 5 ga boʻlsak, 160 ta stul chiqadi."},
        {"text": "Why will twenty places in the hall stay empty?",
         "choices": ["The fire officer forbids them",
                     "Nobody wants to sit at the back",
                     "There is no money to hire chairs for them",
                     "They are reserved for families"],
         "answer": 2,
         "explanation": "Zal 180 kishini sigʻdiradi, lekin pul faqat "
                        "160 ta stulga yetadi."},
        {"text": "Why is the rule about families called 'not binding'?",
         "choices": ["The committee voted against it",
                     "Forty is well inside the limit of one hundred and sixty",
                     "Families do not need seats",
                     "It was decided after the budget"],
         "answer": 1,
         "explanation": "Bu shart hech narsani cheklamayapti — 40 soni "
                        "160 ning ichida bemalol joylashadi."},
    ],
},

]
