# -*- coding: utf-8 -*-
"""Prime SAT Readings — 96-100. OXIRGI BESHTA. Javon shu yerda toʻladi.

Overrides in corner/management/commands/toc_prime_sat_readings.txt.

⚠️ Matn INGLIZCHA · summary, cn-word glosses, explanation OʻZBEKCHA.
⚠️ ⛔ Tanada algebraik belgi YOʻQ.
⚠️ SUBJECT/COLLECTION oldingi fayldan aynan koʻchirilgan.

FAKTLAR (gate ularni tekshiradi):
  96 — terapevtik oyna: dorining taʼsir qiladigan eng kam miqdori bilan
       xavfli boʻladigan miqdori orasidagi oraliq; baʼzi dorilarda u tor
       va qon tekshiruvi talab qilinadi. ⛔ Dori nomi va doza yozilmaydi.
  97 — Simpson paradoksi: 1973-yilgi mashhur qabul maʼlumotlari. Matndagi
       ikki fakultetli misol OʻZIMIZNIKI va arifmetikasi toʻliq toʻgʻri.
       ⛔ Universitet nomi yozilmaydi.
  98 — davriy jadval sinf devorida turadi: 118 element yodlanmaydi,
       18 ustunning xatti-harakati oʻrganiladi.
  99 — balandlikka sakrash: planka koʻtarilib boradi va har bir sportchi
       oʻz darajasida toʻxtaydi — moslashuvchi testning aynan oʻzi.
  100 — togʻda baxtsiz hodisalarning koʻpi TUSHISHDA sodir boʻladi.
       ⛔ Aniq foiz va choʻqqi nomi yozilmaydi.

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_96_100.py \\
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
# 96 — the allowed interval
# ─────────────────────────────────────────────────────────────────────
{
    "order": 96,
    "title": "The Window Between Too Little and Too Much",
    "summary": (
        "Har bir dorining ikkita chegarasi bor — taʼsir qilmaydigan va "
        "xavfli boʻladigan. Ular orasidagi oraliq domain (SAT-96)."
    ),
    "body": """
<p>Every medicine has two numbers, and neither of them is the <span class="cn-word" data-tr="doza, miqdor">dose</span>.</p>

<p>The first is the amount below which nothing happens: the drug is in
the body, but too thinly spread to do the work it was given for. The
second is the amount above which it stops being a <span class="cn-word" data-tr="davolash">treatment</span> and starts
being a <span class="cn-word" data-tr="zaharlanish">poisoning</span>.
The <span class="cn-word" data-tr="oraliq, tirqish">gap</span> between
those two numbers is what doctors call the therapeutic window, and
<span class="cn-word" data-tr="dori tayinlash">prescribing</span> is the art of landing inside it.</p>

<p>For most medicines the window is comfortably wide. A little more or
a little less makes no practical difference, which is why a
<span class="cn-word" data-tr="og'riq qoldiruvchi">painkiller</span>
can be sold with a single <span class="cn-word" data-tr="koʻrsatma">instruction</span> on the box.</p>

<p>For a few, it is <span class="cn-word" data-tr="tor">narrow</span> —
narrow enough that <span class="cn-word" data-tr="bemorlar">patients</span> taking them have their blood tested
<span class="cn-word" data-tr="muntazam">regularly</span>, because the difference between the useful amount and the
<span class="cn-word" data-tr="xavfli">dangerous</span> one is smaller than the difference between one person's body
and another's. <strong>The same dose is right for one patient and wrong
for the next.</strong></p>

<p>What the window really describes is a set of
<span class="cn-word" data-tr="ruxsat etilgan">permitted</span> values.
Outside it the <span class="cn-word" data-tr="miqdor">quantity</span> is not merely a poor choice; it is the wrong
kind of number altogether — one that the <span class="cn-word" data-tr="vaziyat">situation</span> cannot
<span class="cn-word" data-tr="qabul qilmoq">accept</span>. Every
formula that describes something real carries a window like this, and
the values outside it are not answers at all.</p>
""",
    "grammar": [
        {"pattern": "the amount below which nothing happens",
         "meaning": "undan pastda hech narsa boʻlmaydigan miqdor — pastki chegara.",
         "examples": ["There is an amount below which the drug does nothing."]},
        {"pattern": "a set of permitted values",
         "meaning": "ruxsat etilgan qiymatlar toʻplami — domain taʼrifining oʻzi.",
         "examples": ["The window is simply a set of permitted values."]},
        {"pattern": "not answers at all",
         "meaning": "umuman javob emas — notoʻgʻri javob emas, balki mumkin boʻlmagan.",
         "examples": ["Values outside the window are not answers at all."]},
    ],
    "questions": [
        {"text": "What do the two numbers describe?",
         "choices": ["The cost and the strength of the medicine",
                     "The lowest useful amount and the lowest dangerous amount",
                     "How long the medicine lasts",
                     "How often it should be taken"],
         "answer": 1,
         "explanation": "Biri — taʼsir boshlanadigan miqdor, ikkinchisi — xavf "
                        "boshlanadigan miqdor."},
        {"text": "A medicine begins to work at 10 units and becomes unsafe above 30. "
                 "How wide is its window?",
         "choices": ["20 units", "30 units", "10 units", "40 units"],
         "answer": 0,
         "explanation": "30 dan 10 ni ayiring: oyna 20 birlik keng."},
        {"text": "Why are some patients' blood tested regularly?",
         "choices": ["Because the medicine is expensive",
                     "Because the window is narrower than the difference between people",
                     "Because the dose changes every day",
                     "Because the test is required by law"],
         "answer": 1,
         "explanation": "Oyna tor boʻlsa, bir odamga toʻgʻri kelgan doza "
                        "ikkinchisiga toʻgʻri kelmasligi mumkin."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 97 — the denominator decides
# ─────────────────────────────────────────────────────────────────────
{
    "order": 97,
    "title": "Both Numbers Were True",
    "summary": (
        "Umumiy jadval bir narsani, fakultetlar boʻyicha jadval boshqasini "
        "koʻrsatdi — va ikkalasi ham rost edi (SAT-97)."
    ),
    "body": """
<p>In 1973 a large American university looked at its own <span class="cn-word" data-tr="qabul">admission</span>
figures and found something that looked indefensible. Across the whole
<span class="cn-word" data-tr="muassasa">institution</span>, men were <span class="cn-word" data-tr="qabul qilingan">admitted</span> at a noticeably higher rate than women.</p>

<p>Then somebody broke the same
<span class="cn-word" data-tr="maʼlumotlar">data</span> down by
department, and the picture <span class="cn-word" data-tr="teskarisiga aylandi">reversed</span>. In most departments women were
admitted at the same rate as men or a slightly higher one. Nothing had
been <span class="cn-word" data-tr="notoʻgʻri sanalgan">miscounted</span>. <strong>Both figures came from the same table.</strong></p>

<p>The explanation is entirely arithmetic, and a small invented example
shows it. Suppose one department admits sixty percent of <span class="cn-word" data-tr="ariza berganlar">applicants</span> and
another admits twenty. Eighty men apply to the easy department and
twenty to the hard one; for women it is the other way <span class="cn-word" data-tr="bosqich, tur">round</span>. Every
applicant of either sex faces exactly the same chance in whichever
department they chose — and yet fifty-two of the hundred men are
admitted and twenty-eight of the hundred women.</p>

<p>Nobody was treated differently. The two groups had simply applied to
different places, and the <span class="cn-word" data-tr="umumiy">overall</span>
<span class="cn-word" data-tr="ulush, nisbat">rate</span> was an <span class="cn-word" data-tr="oʻrtacha">average</span>
of departments weighted by who applied where.</p>

<p>This is the whole of what a table question tests. A
<span class="cn-word" data-tr="surat">numerator</span> means nothing
until you know its <span class="cn-word" data-tr="maxraj">denominator</span>,
and the same <span class="cn-word" data-tr="son, hisob">count</span> can be divided by three different totals to give
three <span class="cn-word" data-tr="bir-biriga zid">contradictory</span>
answers, every one of them correct.</p>
""",
    "grammar": [
        {"pattern": "at a higher rate than",
         "meaning": "… ga qaraganda yuqori ulushda — foizlarni solishtirish.",
         "examples": ["Men were admitted at a higher rate than women overall."]},
        {"pattern": "broke the data down by department",
         "meaning": "maʼlumotni fakultetlar boʻyicha ajratdi — guruhlarga boʻlish.",
         "examples": ["Break the data down by group and the picture may reverse."]},
        {"pattern": "weighted by who applied where",
         "meaning": "kim qayerga ariza berganiga qarab ogʻirlangan — oʻrtachaning siri.",
         "examples": ["The overall rate is weighted by who applied where."]},
    ],
    "questions": [
        {"text": "Why did the two views of the data disagree?",
         "choices": ["One of them was miscounted",
                     "The groups had applied to different departments",
                     "The departments changed their rules",
                     "The figures came from different years"],
         "answer": 1,
         "explanation": "Ikki guruh turli fakultetlarga ariza bergan — "
                        "maxrajlar boshqa edi."},
        {"text": "In the example, 80 men apply to a department that admits 60 percent. "
                 "How many of them are admitted?",
         "choices": ["48", "60", "20", "80"],
         "answer": 0,
         "explanation": "80 ning 60 foizi — 48 nafar."},
        {"text": "What does the reading say a numerator means on its own?",
         "choices": ["It is always the more important number",
                     "It gives the rate directly",
                     "It means nothing until you know the denominator",
                     "It should be converted to a percentage first"],
         "answer": 2,
         "explanation": "Surat maxrajsiz hech narsa aytmaydi — jadval "
                        "savolining butun mazmuni shu."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 98 — what hangs on the wall so the mind can be free
# ─────────────────────────────────────────────────────────────────────
{
    "order": 98,
    "title": "The Chart on the Classroom Wall",
    "summary": (
        "Kimyogar 118 ta elementni yodlamaydi — u devordagi jadvalni "
        "oʻqishni biladi (SAT-98)."
    ),
    "body": """
<p>There is a <span class="cn-word" data-tr="jadval, plakat">chart</span> on the wall of every chemistry classroom in the
world, and its presence there is a <span class="cn-word" data-tr="qaror">decision</span> about
<span class="cn-word" data-tr="xotira">memory</span>.</p>

<p>It lists more than a hundred <span class="cn-word" data-tr="elementlar">elements</span> with their
<span class="cn-word" data-tr="belgilar">symbols</span> and their
<span class="cn-word" data-tr="massalar">masses</span>. Nobody is expected to learn those masses. They are on the wall
precisely so that they need not be in anyone's head, and a student who
spends a month
<span class="cn-word" data-tr="yodlash">memorising</span> them has spent
a month on the one part of the <span class="cn-word" data-tr="fan">subject</span> that is permanently available.</p>

<p>What a chemist does carry is smaller and far more useful: the
<span class="cn-word" data-tr="xulq-atvor">behaviour</span> of the
eighteen columns. Everything in the first column reacts <span class="cn-word" data-tr="shiddat bilan">violently</span> with
water. Everything in the last is almost <span class="cn-word" data-tr="sust, reaksiyaga kirishmaydigan">inert</span>. Elements in the same
column behave alike because of how their outer
<span class="cn-word" data-tr="elektronlar">electrons</span> are
<span class="cn-word" data-tr="joylashgan">arranged</span>, and that single idea explains more chemistry than any list of
numbers.</p>

<p><strong>The chart was designed to be looked at, not
learnt.</strong></p>

<p>Any subject with a reference table makes the same
<span class="cn-word" data-tr="taklif">offer</span>, and the same <span class="cn-word" data-tr="tuzoq">trap</span>
comes with it. The thing <span class="cn-word" data-tr="bilishga arziydigan">worth knowing</span> by heart is never the part
printed on the wall. It is the part that tells you which line of the
wall to read.</p>
""",
    "grammar": [
        {"pattern": "designed to be looked at, not learnt",
         "meaning": "yodlash uchun emas, qarash uchun tuzilgan.",
         "examples": ["The reference sheet is designed to be looked at, not learnt."]},
        {"pattern": "permanently available",
         "meaning": "doimo qoʻl ostida — yodlashning maʼnosi yoʻqligining sababi.",
         "examples": ["Do not memorise what is permanently available."]},
        {"pattern": "behave alike",
         "meaning": "bir xil xatti-harakat qiladi — guruhlash gʻoyasi.",
         "examples": ["Elements in the same column behave alike."]},
    ],
    "questions": [
        {"text": "Why are the masses printed on the wall?",
         "choices": ["To decorate the room",
                     "So that nobody has to keep them in their head",
                     "Because they change often",
                     "Because students copy them into notebooks"],
         "answer": 1,
         "explanation": "Ular doimo qoʻl ostida — shuning uchun yodlash "
                        "vaqtni yoʻqotish."},
        {"text": "A chemist learns the behaviour of 18 columns instead of more than "
                 "100 elements. Roughly how many times fewer things is that?",
         "choices": ["About six times fewer", "About two times fewer",
                     "About twenty times fewer", "The same number"],
         "answer": 0,
         "explanation": "118 ni 18 ga boʻlsak, taxminan olti — oʻrganiladigan "
                        "narsa olti barobar kam."},
        {"text": "What does the reading say is always worth knowing by heart?",
         "choices": ["The longest list in the subject",
                     "The part that tells you which line of the chart to read",
                     "The first column only",
                     "Everything not printed in colour"],
         "answer": 1,
         "explanation": "Devordagi qismi emas — qaysi qatorni oʻqish "
                        "kerakligini aytadigan qismi."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 99 — the bar that rises until it finds you
# ─────────────────────────────────────────────────────────────────────
{
    "order": 99,
    "title": "The Bar Rises Until It Finds You",
    "summary": (
        "Balandlikka sakrashda hech kim bir xil balandlikda sakramaydi — "
        "planka har bir sportchini oʻz darajasida topadi (SAT-99)."
    ),
    "body": """
<p>A high jump competition does not ask everybody the same question.</p>

<p>The <span class="cn-word" data-tr="planka, koʻndalang tayoq">bar</span>
starts low enough that most of the field will <span class="cn-word" data-tr="undan oshib oʻtmoq">clear it</span>, and after each
round it goes up. Jumpers who clear it stay in. Jumpers who fail three
times at one height are finished, and the height they last cleared is
their result. Nobody jumps a hundred times; the
<span class="cn-word" data-tr="musobaqa">competition</span> finds each
<span class="cn-word" data-tr="sportchi">athlete</span>'s level in a handful of <span class="cn-word" data-tr="urinishlar">attempts</span>, because every attempt is
chosen in the light of the last one.</p>

<p>The <span class="cn-word" data-tr="samaradorlik">efficiency</span> of
that is easy to miss. To measure everyone <span class="cn-word" data-tr="aniq">accurately</span> with a fixed set
of heights you would need dozens of them: low ones that tell you nothing
about the leaders, high ones that tell you nothing about anybody else.
<strong>An attempt only carries information when it might go either
way.</strong></p>

<p>Modern computer-based tests are built on the same <span class="cn-word" data-tr="tamoyil">principle</span>. A
question far below a <span class="cn-word" data-tr="imtihon topshiruvchi">candidate</span>'s level, or far above it, uses up time
and <span class="cn-word" data-tr="koʻrsatib beradi">reveals</span> almost nothing. So the test watches the early answers and
chooses what comes next — harder if the early work was
<span class="cn-word" data-tr="ishonchli">solid</span>, easier if it was
not.</p>

<p>Which means a hard second half is not bad news. It is the
<span class="cn-word" data-tr="belgi, alomat">sign</span> that the bar
has been raised, and it is raised for exactly one reason.</p>
""",
    "grammar": [
        {"pattern": "in the light of the last one",
         "meaning": "oldingisiga qarab — moslashuvning taʼrifi.",
         "examples": ["Each attempt is chosen in the light of the last one."]},
        {"pattern": "might go either way",
         "meaning": "ikki tomonga ham ketishi mumkin — maʼlumot beradigan sinov.",
         "examples": ["An attempt is informative only when it might go either way."]},
        {"pattern": "the height they last cleared",
         "meaning": "oxirgi marta oshib oʻtgan balandligi — natijaning taʼrifi.",
         "examples": ["Their result is the height they last cleared."]},
    ],
    "questions": [
        {"text": "Why does the bar start low and rise?",
         "choices": ["To make the competition longer",
                     "To find each athlete's level in few attempts",
                     "Because the rules require ten rounds",
                     "To let the crowd warm up"],
         "answer": 1,
         "explanation": "Har bir urinish oldingisiga qarab tanlanadi — daraja "
                        "bir necha urinishda topiladi."},
        {"text": "The bar starts at 1.60 metres and rises 5 centimetres each round. "
                 "How many rises does it take to reach 1.90 metres?",
         "choices": ["Six", "Five", "Thirty", "Ten"],
         "answer": 0,
         "explanation": "1.90 dan 1.60 ni ayirsak 30 sm, va 30 ni 5 ga "
                        "boʻlsak — olti marta koʻtariladi."},
        {"text": "According to the reading, what does a hard second half mean?",
         "choices": ["The test has gone wrong",
                     "The bar has been raised because the early work was solid",
                     "The candidate is running out of time",
                     "The questions were chosen at random"],
         "answer": 1,
         "explanation": "Planka faqat bitta sababga koʻra koʻtariladi — "
                        "boshlanishi yaxshi boʻlgani uchun."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 100 — the descent (the last reading on the shelf)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 100,
    "title": "The Mountain Is Not Finished at the Top",
    "summary": (
        "Togʻda baxtsiz hodisalarning koʻpi choʻqqida emas, tushishda "
        "sodir boʻladi — ish bajarilgandan keyin (SAT-100)."
    ),
    "body": """
<p>Climbers have a saying that sounds like a
<span class="cn-word" data-tr="qarama-qarshilik">contradiction</span>
until you look at the <span class="cn-word" data-tr="yozuvlar, hisobotlar">records</span>: the <span class="cn-word" data-tr="choʻqqi">summit</span> is the halfway point.</p>

<p>On the highest <span class="cn-word" data-tr="choʻqqilar">peaks</span>, accident reports show that most deaths happen
on the way down rather than on the way up. The reasons are not
mysterious. The hardest work is behind, the goal has been reached, and
the <span class="cn-word" data-tr="eʼtibor">attention</span> that
carried the climber up quietly lets go. <span class="cn-word" data-tr="charchoq">Fatigue</span> is at its worst. The
<span class="cn-word" data-tr="ob-havo">weather</span> has had all day to change. And the one thing that had been
holding every decision together — <i>we are still climbing</i> — is
gone.</p>

<p>Experienced parties answer this with a rule made before anybody sets
off: a <span class="cn-word" data-tr="qaytish vaqti">turnaround
time</span>. At that hour the <span class="cn-word" data-tr="guruh, jamoa">party</span> goes down, summit or no summit, and
the decision is not <span class="cn-word" data-tr="qayta koʻrib
chiqmoq">revisited</span> on the mountain, where tired people make
generous arguments for carrying on.</p>

<p><strong>The last stretch of any piece of work is where it is most
often lost.</strong> The <span class="cn-word" data-tr="hisob">calculation</span> is finished, the answer is on the
page, and the mind is already somewhere else — which is precisely when
the wrong line gets marked, the unit gets dropped, or a correct number
answers a question nobody asked.</p>

<p>Thirty seconds, at the end, after the thinking is done. Not because
the work was poor, but because that is where the
<span class="cn-word" data-tr="tushish, pastga qaytish">descent</span>
begins.</p>
""",
    "grammar": [
        {"pattern": "the summit is the halfway point",
         "meaning": "choʻqqi — yoʻlning yarmi, oxiri emas.",
         "examples": ["Climbers say the summit is the halfway point."]},
        {"pattern": "made before anybody sets off",
         "meaning": "yoʻlga chiqishdan oldin qabul qilingan — sovuq boshda qaror.",
         "examples": ["The rule is made before anybody sets off."]},
        {"pattern": "where it is most often lost",
         "meaning": "koʻpincha aynan shu yerda yoʻqotiladi.",
         "examples": ["The last stretch is where the work is most often lost."]},
    ],
    "questions": [
        {"text": "Why do climbers say the summit is the halfway point?",
         "choices": ["The descent takes exactly as long as the climb",
                     "Most accidents happen on the way down",
                     "The summit is measured from sea level",
                     "Half the party usually turns back"],
         "answer": 1,
         "explanation": "Hisobotlar koʻrsatadi: koʻpchilik baxtsiz hodisa "
                        "tushishda sodir boʻladi."},
        {"text": "A party leaves at 4 a.m. with a turnaround time of 2 p.m. How many "
                 "hours do they have to reach the summit?",
         "choices": ["Ten", "Eight", "Twelve", "Six"],
         "answer": 0,
         "explanation": "Ertalabki 4 dan kunduzgi 2 gacha — oʻn soat."},
        {"text": "What does the reading say the last thirty seconds are for?",
         "choices": ["Repeating the whole calculation",
                     "Catching what attention lets go of once the work feels done",
                     "Reading the next question early",
                     "Resting before the next section"],
         "answer": 1,
         "explanation": "Ish tugagandek tuyulganda eʼtibor boʻshashadi — "
                        "aynan oʻsha joyda ball yoʻqoladi."},
    ],
},

]
