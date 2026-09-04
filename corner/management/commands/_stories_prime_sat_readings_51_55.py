# -*- coding: utf-8 -*-
"""Prime SAT Readings — 51–55 (SAT-51 … SAT-55 darslariga).

Written with the overrides in corner/management/commands/toc_prime_sat_readings.txt
⛔ MATNDA ALGEBRAIK BELGI YOʻQ — miqdorlar faqat ingliz tilida, soʻz bilan.

Til: matn, sarlavha va savollar INGLIZCHA; summary, cn-word glosslari,
     "Exam English" izohlari va javob tushuntirishlari OʻZBEKCHA.

Ovozlar (11-batch ayoldan boshlanadi): 51 Jenny · 52 Guy · 53 Jenny ·
                                       54 Guy · 55 Jenny

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_51_55.py --author=prime
    python manage.py gen_corner_audio --collection="Prime SAT Readings" \\
        --only <n> --voice en-US-JennyNeural       # ⚠️ --voice MAJBURIY
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

    # ── 51 · a school election ───────────────────────────────────────
    {
        "title": "Sixty Percent of Whom?",
        "order": 51,
        "summary": (
            "Gʻolib ovozlarning oltmish foizini oldi — lekin maktabning atigi "
            "oʻttiz foizini. Ikkala jumla ham rost."
        ),
        "body": """
<p>The school had four hundred pupils, and the notice on the
<span class="cn-word" data-tr="eʼlonlar taxtasi">board</span> the morning after the
<span class="cn-word" data-tr="saylov">election</span> said that Dilnoza had won with sixty
percent of the vote.</p>

<p>She had. Two hundred pupils voted, and a hundred and twenty of them chose her. Sixty percent
is <span class="cn-word" data-tr="aniq, roppa-rosa">exactly</span> right.</p>

<p>The other two hundred pupils did not vote at all. Some had a
<span class="cn-word" data-tr="mashgʻulot, dars">lesson</span> during the voting hour, some
forgot, and some did not <span class="cn-word" data-tr="ahamiyat bermoq">care</span>. So the
hundred and twenty who chose Dilnoza were sixty percent of those who voted — and thirty percent
of the school.</p>

<p>Neither number is <span class="cn-word" data-tr="yolgʻon, xato">false</span>. They answer
different questions, and the <span class="cn-word" data-tr="farq">difference</span> is not in
the arithmetic but in the words after the word <em>of</em>.</p>

<p>The <span class="cn-word" data-tr="direktor">head teacher</span> made this the subject of
assembly, which the pupils found <span class="cn-word" data-tr="gʻalati">odd</span> until she
put both sentences on the screen at once. <em>Sixty percent of those who voted.</em>
<em>Thirty percent of the school.</em> Then she asked which one Dilnoza should put in her
<span class="cn-word" data-tr="nutq">speech</span>, and which one the pupils who had not voted
should think about.</p>

<p>One boy put up his hand and asked which number was the real one. She said both were, and
that the <span class="cn-word" data-tr="koʻnikma">skill</span> he needed was not choosing
between them but noticing that they were answers to two different questions.</p>

<p>The following year the school moved the vote to the
<span class="cn-word" data-tr="tushlik tanaffusi">lunch break</span>. Three hundred and twenty
pupils voted. Nobody changed the way percentages work; they changed what the percentage was
being taken <span class="cn-word" data-tr="olinadigan">from</span>.</p>
""",
        "grammar": [
            {"pattern": "sixty percent of those who voted",
             "meaning": "ovoz berganlarning oltmish foizi — baza ovoz berganlar"},
            {"pattern": "thirty percent of the school",
             "meaning": "maktabning oʻttiz foizi — baza butun maktab"},
            {"pattern": "the words after the word 'of'",
             "meaning": "«of» dan keyingi soʻzlar — bazani belgilaydi"},
        ],
        "questions": [
            {"text": "How many pupils chose Dilnoza?",
             "choices": ["Two hundred", "A hundred and twenty", "Four hundred", "Sixty"],
             "answer": 1,
             "explanation": "Ikki yuz kishi ovoz berdi va ularning oltmish foizi — "
                            "bir yuz yigirma kishi."},
            {"text": "Why are both sixty percent and thirty percent correct?",
             "choices": ["The counting was done twice",
                         "They are taken from different bases",
                         "One is rounded",
                         "The head teacher made a mistake"],
             "answer": 1,
             "explanation": "Surat bir xil — 120. Maxraj boshqa: bir joyda "
                            "ovoz berganlar, boshqasida butun maktab."},
            {"text": "What changed the following year?",
             "choices": ["The way percentages are calculated",
                         "The number of candidates",
                         "The number of pupils who voted",
                         "The size of the school"],
             "answer": 2,
             "explanation": "Ovoz berish tushlik tanaffusiga koʻchirildi va uch "
                            "yuz yigirma kishi qatnashdi — baza kengaydi."},
        ],
    },

    # ── 52 · conservation science ────────────────────────────────────
    {
        "title": "Down Forty, Up Forty",
        "order": 52,
        "summary": (
            "Qushlar soni qirq foizga tushdi, keyin qirq foizga koʻtarildi — "
            "va hali ham avvalgidan kam."
        ),
        "body": """
<p>The <span class="cn-word" data-tr="qoʻriqxona">reserve</span> had counted five hundred nesting
birds in its first survey. Four years later, after two dry summers, the
<span class="cn-word" data-tr="hisob, sanoq">count</span> was three hundred. That is a fall of
forty percent, and it was reported as such in the annual
<span class="cn-word" data-tr="hisobot">report</span>.</p>

<p>Then the wet years returned and the birds came back. The next survey found four hundred and
twenty — a <span class="cn-word" data-tr="tiklanish">recovery</span> of forty percent on the
previous count.</p>

<p>A local newspaper ran the two figures together and wrote that the population had fallen forty
percent and <span class="cn-word" data-tr="tiklandi">recovered</span> forty percent, and was
therefore back where it started.</p>

<p>It was not. Four hundred and twenty is not five hundred. The reserve's
<span class="cn-word" data-tr="ekolog">ecologist</span> wrote a short letter explaining why,
and she did not use a single formula.</p>

<p>The first forty percent, she wrote, was forty percent
<span class="cn-word" data-tr="bir necha yuz">of five hundred</span> — two hundred birds. The
second forty percent was forty percent of <span class="cn-word"
data-tr="uch yuz">three hundred</span> — only a hundred and twenty. The loss and the
<span class="cn-word" data-tr="foyda, qoʻshimcha">gain</span> carry the same percentage and
completely different numbers of birds, because they are measured against different
<span class="cn-word" data-tr="boshlangʻich holat">starting points</span>.</p>

<p>She added one line at the end, because she knew it would be quoted: a percentage without
its <span class="cn-word" data-tr="asos">base</span> is not a fact, it is half of one.</p>

<p>The population is at eighty-four percent of the original. That is genuinely good
<span class="cn-word" data-tr="yangilik">news</span> after two dry summers. It is not the same
as <span class="cn-word" data-tr="tiklanish, qaytish">a return</span>, and the reserve's funding
depends on the difference.</p>
""",
        "grammar": [
            {"pattern": "a fall of forty percent",
             "meaning": "qirq foizga pasayish"},
            {"pattern": "forty percent on the previous count",
             "meaning": "oldingi hisobga nisbatan qirq foiz — baza oʻzgargan"},
            {"pattern": "measured against different starting points",
             "meaning": "turli boshlangʻich nuqtalarga nisbatan oʻlchangan"},
        ],
        "questions": [
            {"text": "How many birds did the reserve lose in the fall?",
             "choices": ["A hundred and twenty", "Two hundred", "Forty", "Four hundred and twenty"],
             "answer": 1,
             "explanation": "Besh yuzning qirq foizi — ikki yuz qush."},
            {"text": "Why did the same percentage bring back fewer birds?",
             "choices": ["The second survey was less careful",
                         "The recovery took less time",
                         "Forty percent of three hundred is smaller than forty percent of five hundred",
                         "Some birds moved away"],
             "answer": 2,
             "explanation": "Ikkinchi foiz kichikroq sondan olingan: uch yuzning "
                            "qirq foizi bir yuz yigirma."},
            {"text": "What is the population now, as a share of the original?",
             "choices": ["A hundred percent", "Eighty percent",
                         "Eighty-four percent", "Sixty percent"],
             "answer": 2,
             "explanation": "Toʻrt yuz yigirma — besh yuzning sakson toʻrt foizi, "
                            "va matn buni toʻgʻridan-toʻgʻri aytadi."},
        ],
    },

    # ── 53 · a town council meeting ──────────────────────────────────
    {
        "title": "The Chart on the Wall",
        "order": 53,
        "summary": (
            "Diagramma bir tomonni ikki barobar katta koʻrsatdi — sonlar esa "
            "besh foiz farq qilardi. Xato oʻqda edi."
        ),
        "body": """
<p>The <span class="cn-word" data-tr="shahar kengashi">town council</span> met to decide whether
to keep funding the evening bus. A slide went up on the wall showing
<span class="cn-word" data-tr="yoʻlovchilar">passengers</span> in two years, one bar beside the
other, and the second bar was <span class="cn-word" data-tr="qariyb">nearly</span> twice the
height of the first.</p>

<p>Somebody said it looked like the service had almost doubled. Several heads
<span class="cn-word" data-tr="bosh irgʻamoq">nodded</span>.</p>

<p>The council's <span class="cn-word" data-tr="hisobchi, moliyachi">treasurer</span> asked to
see the <span class="cn-word" data-tr="raqamlar">figures</span> rather than the picture. The
first bar was ninety-five thousand passengers. The second was one hundred thousand.</p>

<p>The <span class="cn-word" data-tr="oʻq">axis</span> did not start at zero. It started at
ninety thousand. So the visible part of the first bar stood for five thousand passengers and the
visible part of the second stood for ten — which is
<span class="cn-word" data-tr="albatta">indeed</span> twice as tall, and tells you nothing about
the two <span class="cn-word" data-tr="jami">totals</span>.</p>

<p>Nobody had done anything dishonest. The slide had been made by a
<span class="cn-word" data-tr="yordamchi">clerk</span> using the default settings of a
spreadsheet, which fits the bars to the data and starts the axis wherever it likes.</p>

<p>The real increase was about five percent. Whether that
<span class="cn-word" data-tr="oqlamoq">justifies</span> the funding is a fair question, and the
council spent an hour on it. But it is a different question from the one the picture had
<span class="cn-word" data-tr="taklif qilmoq">suggested</span>.</p>

<p>The treasurer asked for one change to the town's
<span class="cn-word" data-tr="qoidalar, tartib">rules</span>, and got it: every chart in a
council paper must either start its axis at zero or say, in
<span class="cn-word" data-tr="soʻzlar">words</span>, where it starts.</p>
""",
        "grammar": [
            {"pattern": "the axis did not start at zero",
             "meaning": "oʻq noldan boshlanmagan — shkala tuzogʻi"},
            {"pattern": "the visible part of the bar",
             "meaning": "ustunning koʻrinadigan qismi — jami emas"},
            {"pattern": "tells you nothing about the two totals",
             "meaning": "jami qiymatlar haqida hech narsa aytmaydi"},
        ],
        "questions": [
            {"text": "What were the two passenger figures?",
             "choices": ["Five thousand and ten thousand",
                         "Ninety-five thousand and one hundred thousand",
                         "Ninety thousand and one hundred thousand",
                         "Ninety-five thousand and ninety thousand"],
             "answer": 1,
             "explanation": "Ustunlar toʻqson besh ming va yuz ming yoʻlovchini "
                            "koʻrsatgan — koʻrinadigan qismlari esa besh va oʻn "
                            "ming."},
            {"text": "Why did the second bar look twice as tall?",
             "choices": ["The scale was wrong by a factor of two",
                         "The second year had twice the passengers",
                         "Only the part above ninety thousand was drawn",
                         "The slide was stretched"],
             "answer": 2,
             "explanation": "Oʻq toʻqson mingdan boshlangani uchun faqat undan "
                            "yuqoridagi qism chizilgan."},
            {"text": "What rule did the treasurer get accepted?",
             "choices": ["Charts must start at zero or say where they start",
                         "No charts in council papers",
                         "All figures must be rounded",
                         "The evening bus must be funded"],
             "answer": 0,
             "explanation": "Matnning oxirgi jumlasi: har bir diagramma yo noldan "
                            "boshlanishi, yo qayerdan boshlanganini soʻz bilan "
                            "aytishi kerak."},
        ],
    },

    # ── 54 · a school research project ───────────────────────────────
    {
        "title": "Breakfast and the Third Thing",
        "order": 54,
        "summary": (
            "Nonushta qiladiganlar yuqoriroq ball oladi — lekin bu nonushta "
            "sababmi yoki uchinchi narsaning belgisimi?"
        ),
        "body": """
<p>Three pupils ran a <span class="cn-word" data-tr="soʻrovnoma">survey</span> for the school
science fair. They asked everyone in their year whether they had eaten
<span class="cn-word" data-tr="nonushta">breakfast</span> that morning, and then compared the
answers with the term's test <span class="cn-word" data-tr="ballar">scores</span>.</p>

<p>The <span class="cn-word" data-tr="natija">result</span> was clear. Pupils who ate breakfast
scored higher on average, and the difference was too large to be
<span class="cn-word" data-tr="tasodif">chance</span>. Their first draft ended with the
sentence: <em>eating breakfast improves test scores</em>.</p>

<p>Their teacher asked them one question. What else is true of a pupil who eats breakfast on a
school morning?</p>

<p>They thought about it and produced a
<span class="cn-word" data-tr="roʻyxat">list</span>. That pupil probably went to bed at a
reasonable hour. That pupil probably was not
<span class="cn-word" data-tr="shoshilmoq">rushing</span>. That pupil lives in a household where
somebody has time in the morning. Any of those could raise a
<span class="cn-word" data-tr="ball">score</span> on its own, and none of them is
breakfast.</p>

<p>The survey could not separate them, because it had only
<span class="cn-word" data-tr="kuzatgan">observed</span> what pupils already did. To show that
breakfast itself does the work, somebody would have to
<span class="cn-word" data-tr="tayinlamoq">assign</span> it — and that is a different and much
harder study.</p>

<p>The teacher told them this was not a
<span class="cn-word" data-tr="muvaffaqiyatsizlik">failure</span> of their work. Noticing
what a study cannot show is part of doing the study.</p>

<p>They changed the last sentence to: <em>eating breakfast is associated with higher scores in
this year group</em>. It is a <span class="cn-word" data-tr="kamtarona">smaller</span> claim,
and it is the one their data can carry. It won the fair.</p>
""",
        "grammar": [
            {"pattern": "is associated with",
             "meaning": "… bilan bogʻliq — sabab daʼvo qilinmaydi"},
            {"pattern": "what else is true of …?",
             "meaning": "yana nima rost — uchinchi omilni izlash savoli"},
            {"pattern": "the claim its data can carry",
             "meaning": "maʼlumot koʻtara oladigan daʼvo"},
        ],
        "questions": [
            {"text": "What did the survey actually find?",
             "choices": ["Breakfast improves scores",
                         "Pupils who ate breakfast scored higher on average",
                         "Sleep improves scores",
                         "There was no difference"],
             "answer": 1,
             "explanation": "U faqat bogʻliqlikni kuzatgan — sababni emas."},
            {"text": "Why could the survey not show that breakfast causes the difference?",
             "choices": ["The sample was too small",
                         "Test scores are unreliable",
                         "It only observed what pupils already did",
                         "The pupils lied"],
             "answer": 2,
             "explanation": "Sababni koʻrsatish uchun nonushtani tayinlash kerak "
                            "boʻlardi, kuzatish yetarli emas."},
            {"text": "Why is the final sentence better?",
             "choices": ["It is a smaller claim that the data can support",
                         "It is longer",
                         "It mentions the year group",
                         "It avoids the word breakfast"],
             "answer": 0,
             "explanation": "Kamtaronaroq daʼvo — lekin aynan shu daʼvoni "
                            "maʼlumot tasdiqlay oladi."},
        ],
    },

    # ── 55 · the class-size paradox ──────────────────────────────────
    {
        "title": "The Average Nobody Is In",
        "order": 55,
        "summary": (
            "Maktab oʻrtacha sinf yigirma kishi deydi, oʻquvchi esa qirq kishilik "
            "sinfda oʻtiradi — ikkalasi ham rost."
        ),
        "body": """
<p>The school's <span class="cn-word" data-tr="broshyura">brochure</span> said that the average
class had twenty pupils. A parent who had seen her daughter's
<span class="cn-word" data-tr="sinf xonasi">classroom</span> did not believe it, and asked for
the <span class="cn-word" data-tr="tafsilotlar">details</span>.</p>

<p>She got them, and the brochure was right. There were five classes in that year:
<span class="cn-word" data-tr="toʻrtta">four</span> of them had ten pupils, and one had sixty.
That is a hundred pupils in five classes, and a hundred divided by five is twenty.</p>

<p>But now count the same year from a pupil's <span class="cn-word"
data-tr="nuqtai nazar">point of view</span>. Sixty of the hundred pupils are in the class of
sixty. Forty are in classes of ten. So the class size that the
<span class="cn-word" data-tr="odatiy">typical</span> pupil actually
<span class="cn-word" data-tr="boshdan kechirmoq">experiences</span> is forty — twice what the
brochure says.</p>

<p>Both numbers come from the same five classes and neither is
<span class="cn-word" data-tr="soxta, notoʻgʻri">wrong</span>. They average different things.
The brochure averages <span class="cn-word" data-tr="sinflar">classes</span>; the parent was
asking about <span class="cn-word" data-tr="oʻquvchilar">pupils</span>, and there are far more
pupils in the big class than in the small ones.</p>

<p>The <span class="cn-word" data-tr="mediana">median</span> class size tells a third story: line
the five classes up and the middle one has ten. Three sentences, three numbers, one set of
facts.</p>

<p>She pointed out that this is not only a school problem. Any average taken over
<span class="cn-word" data-tr="guruhlar">groups</span> of different sizes will differ from
the same average taken over the people inside them.</p>

<p>The parent's <span class="cn-word" data-tr="talab">request</span> to the school was not that
the brochure be corrected. It was that it should say <em>which</em> average it means.</p>
""",
        "grammar": [
            {"pattern": "the average class had twenty pupils",
             "meaning": "sinflar boʻyicha oʻrtacha — jami ÷ sinflar soni"},
            {"pattern": "from a pupil's point of view",
             "meaning": "oʻquvchi nuqtai nazaridan — baza oʻquvchilar"},
            {"pattern": "they average different things",
             "meaning": "ular boshqa-boshqa narsalarni oʻrtachalaydi"},
        ],
        "questions": [
            {"text": "How were the hundred pupils arranged?",
             "choices": ["Five classes of twenty",
                         "Four classes of ten and one of sixty",
                         "Ten classes of ten",
                         "Two classes of fifty"],
             "answer": 1,
             "explanation": "Toʻrtta sinfda oʻntadan, bittasida oltmish — jami "
                            "yuz oʻquvchi, besh sinf."},
            {"text": "Why does the typical pupil experience a class of forty?",
             "choices": ["Because sixty of the hundred pupils are in the big class",
                         "Because the school miscounted",
                         "Because forty is the median",
                         "Because the classes were merged"],
             "answer": 0,
             "explanation": "Katta sinfda oʻquvchilar koʻp, shuning uchun "
                            "oʻquvchilar boʻyicha oʻrtacha yuqori chiqadi."},
            {"text": "What did the parent ask the school to do?",
             "choices": ["Correct the brochure",
                         "Reduce the largest class",
                         "Say which average the brochure means",
                         "Publish the median instead"],
             "answer": 2,
             "explanation": "U raqamni notoʻgʻri demadi — qaysi oʻrtacha ekanini "
                            "aytishni soʻradi."},
        ],
    },
]
