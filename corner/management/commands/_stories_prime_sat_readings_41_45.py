# -*- coding: utf-8 -*-
"""Prime SAT Readings — 41–45 (SAT-41 … SAT-45 darslariga).

Written with the overrides in corner/management/commands/toc_prime_sat_readings.txt
⛔ MATNDA ALGEBRAIK BELGI YOʻQ — miqdorlar faqat ingliz tilida, soʻz bilan.

Til: matn, sarlavha va savollar INGLIZCHA; summary, cn-word glosslari,
     "Exam English" izohlari va javob tushuntirishlari OʻZBEKCHA.

Ovozlar (9-batch ayoldan boshlanadi): 41 Jenny · 42 Guy · 43 Jenny ·
                                      44 Guy · 45 Jenny

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_41_45.py --author=prime
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

    # ── 41 · a tailor's workshop ─────────────────────────────────────
    {
        "title": "What the Bolt Would Not Give",
        "order": 41,
        "summary": (
            "Bir toʻp matodan nechta koʻylak chiqadi va nima ortib qoladi — "
            "qoldiqning ustaxonadagi maʼnosi."
        ),
        "body": """
<p>The <span class="cn-word" data-tr="tikuvchi">tailor</span> had one
<span class="cn-word" data-tr="toʻp (mato)">bolt</span> of grey wool, forty metres of it, and an
order for coats. Each coat took six metres. The
<span class="cn-word" data-tr="shogird">apprentice</span> did the division in his head and said
six coats.</p>

<p>"Six coats," the tailor agreed, "and four metres."</p>

<p>The boy had stopped at the whole number, the way people do. But in a workshop the
<span class="cn-word" data-tr="qoldiq">remainder</span> is not a leftover detail; it is
<span class="cn-word" data-tr="mato">cloth</span>, and cloth is money. Four metres of grey wool
would make two <span class="cn-word" data-tr="jilet">waistcoats</span>, or the linings of three
jackets, or nothing at all if it sat on the shelf until the moths found it.</p>

<p>"Every division has two answers," the tailor said. "How many, and what is left. If you
<span class="cn-word" data-tr="eʼtiborsiz qoldirmoq">ignore</span> the second one you will run
this shop for thirty years and never know where your money went."</p>

<p>He kept a <span class="cn-word" data-tr="daftar, hisob kitobi">ledger</span> with a column for
offcuts. At the end of a good year the column showed enough wool for eleven waistcoats, all of
them made from cloth the apprentice would have called
<span class="cn-word" data-tr="ortiqcha, keraksiz">scrap</span>.</p>

<p>There was one more lesson in it. When the order changed to
<span class="cn-word" data-tr="palto">coats</span> of eight metres, the same bolt gave five coats
and nothing at all left over. The tailor liked those orders least. A
<span class="cn-word" data-tr="toza, aniq">clean</span> division looks tidy on paper, but it
means the bolt has been used to the last centimetre and there is no
<span class="cn-word" data-tr="zaxira">margin</span> if a sleeve is cut wrong.</p>
""",
        "grammar": [
            {"pattern": "every division has two answers",
             "meaning": "har bir boʻlishda ikki javob bor — butun qism va qoldiq"},
            {"pattern": "how many, and what is left",
             "meaning": "nechta va nima qoldi — boʻlinma va qoldiq"},
            {"pattern": "a clean division",
             "meaning": "qoldiqsiz boʻlinish"},
        ],
        "questions": [
            {"text": "What did the apprentice leave out of his answer?",
             "choices": ["The price of the wool", "The four metres left over",
                         "The number of coats", "The width of the bolt"],
             "answer": 1,
             "explanation": "U butun sonda toʻxtadi; qoldiq esa ustaxonada haqiqiy "
                            "mato va haqiqiy pul."},
            {"text": "Why did the tailor keep a column for offcuts?",
             "choices": ["Because the moths destroyed them",
                         "Because customers asked for them",
                         "Because the leftovers added up to eleven waistcoats a year",
                         "Because the ledger required it"],
             "answer": 2,
             "explanation": "Yil davomida yigʻilgan qoldiqlar oʻn bitta jiletga "
                            "yetgan — «keraksiz» deb hisoblangan matodan."},
            {"text": "Why did the tailor dislike an order that used the bolt exactly?",
             "choices": ["It left no margin if a cut went wrong",
                         "It took longer to sew",
                         "It wasted cloth",
                         "It was harder to calculate"],
             "answer": 0,
             "explanation": "Qoldiqsiz boʻlinish qogʻozda chiroyli, lekin xato "
                            "qilinsa tuzatishga mato qolmaydi."},
        ],
    },

    # ── 42 · a newspaper column ──────────────────────────────────────
    {
        "title": "The Test That Takes One Line",
        "order": 42,
        "summary": (
            "Sonni toʻqqizga boʻlish uchun uzun boʻlish shart emas — "
            "raqamlarni qoʻshish yetadi. Arzon sinov, aniq javob."
        ),
        "body": """
<p>A reader wrote in to the newspaper's puzzle column with a
<span class="cn-word" data-tr="shikoyat">complaint</span>. She had been given a list of
<span class="cn-word" data-tr="ombor">warehouse</span> totals and asked which of them could be
shared out evenly among nine people. She had done nine long
<span class="cn-word" data-tr="boʻlish">divisions</span> and it had taken her the whole
<span class="cn-word" data-tr="kech, oqshom">evening</span>.</p>

<p>The <span class="cn-word" data-tr="jurnal muallifi">columnist</span> wrote back that there was a test for it, and that it took one line. He added that he was not being clever: the test is older than the newspaper, and every accountant of her grandmother's generation had known it by heart.</p>

<p>Add up the <span class="cn-word" data-tr="raqamlar">digits</span> of the number. If that
<span class="cn-word" data-tr="yigʻindi">sum</span> can be divided by nine, so can the number
itself. If it cannot, neither can the number.</p>

<p>Take four thousand seven hundred and twenty-five. Its digits add to
<span class="cn-word" data-tr="oʻn sakkiz">eighteen</span>, and eighteen is nine twos.
So the number divides evenly, and indeed it is nine times five hundred and twenty-five. Take three
thousand one hundred and forty-two. Its digits add to ten, which is not a
<span class="cn-word" data-tr="karrali">multiple</span> of nine, so no
<span class="cn-word" data-tr="miqdorda">amount</span> of long division will make it come out
even.</p>

<p>What the columnist wanted his reader to notice was not the trick itself but its
<span class="cn-word" data-tr="shakl, tuzilish">shape</span>. The question "does this divide
evenly?" and the question "what is the answer?" are
<span class="cn-word" data-tr="turli">different</span> questions, and the first one is far
cheaper than the second.</p>

<p>"You do not need to open the box to know it is empty," he finished. "Sometimes you can
<span class="cn-word" data-tr="tortmoq, oʻlchamoq">weigh</span> it."</p>
""",
        "grammar": [
            {"pattern": "does this divide evenly?",
             "meaning": "bu qoldiqsiz boʻlinadimi — koʻpaytuvchi savoli"},
            {"pattern": "if it cannot, neither can the number",
             "meaning": "u boʻlinmasa, son ham boʻlinmaydi — sinovning ikki tomoni"},
            {"pattern": "far cheaper than",
             "meaning": "ancha arzon — kamroq mehnat talab qiladi"},
        ],
        "questions": [
            {"text": "What do the digits of four thousand seven hundred and twenty-five add "
                     "up to?",
             "choices": ["Ten", "Nine", "Eighteen", "Twenty-five"],
             "answer": 2,
             "explanation": "Matn buni aytadi: oʻn sakkiz — va oʻn sakkiz toʻqqizga "
                            "boʻlinadi, demak son ham boʻlinadi."},
            {"text": "Why does the test settle the second number so quickly?",
             "choices": ["Because ten is not a multiple of nine",
                         "Because the number is odd",
                         "Because three thousand is too large",
                         "Because the digits are all different"],
             "answer": 0,
             "explanation": "Raqamlar yigʻindisi oʻn — toʻqqizga boʻlinmaydi, demak "
                            "sonning oʻzi ham boʻlinmaydi."},
            {"text": "What is the columnist's real point?",
             "choices": ["That long division is always wrong",
                         "That 'does it divide?' is a cheaper question than 'what is the answer?'",
                         "That readers should not write in",
                         "That nine is a special number"],
             "answer": 1,
             "explanation": "Ikki savol bir xil emas: biri faqat ha yoki yoʻq "
                            "soʻraydi va shuning uchun ancha arzon."},
        ],
    },

    # ── 43 · nature writing ──────────────────────────────────────────
    {
        "title": "Reading the Ridge Line",
        "order": 43,
        "summary": (
            "Yoʻlning balandlik profili: bir joyda daryoga tegib qaytadi, "
            "boshqasida kesib oʻtadi — va ikki chekkasi hammasini aytadi."
        ),
        "body": """
<p>The <span class="cn-word" data-tr="qoʻllanma, yoʻriqnoma">guidebook</span> printed a picture
of the walk before it printed a word about it. It was not a map. It was the
<span class="cn-word" data-tr="qiya kesim, profil">profile</span> — the height of the path drawn
against the distance walked, so that the whole day appeared as a single line rising and
falling.</p>

<p>Experienced walkers read that line before anything else, and they read it in three
places.</p>

<p>First the two <span class="cn-word" data-tr="chekka">ends</span>. If the line leaves the page
high on the left and high on the right, the walk begins and finishes on high ground, whatever
happens between. If it leaves low on one side and high on the other, you are climbing all day in
one <span class="cn-word" data-tr="yoʻnalish">direction</span> and the return will not be the
same walk.</p>

<p>Then the places where the line meets the river. At one point on this walk the path comes down,
<span class="cn-word" data-tr="tegmoq">touches</span> the water and turns back up without
crossing — a <span class="cn-word" data-tr="tosh, tayanch">stone</span> beach where you stop for
lunch and go back the way you came. At another the line goes straight
<span class="cn-word" data-tr="kesib oʻtmoq">through</span> the water and out the other side.
That is a <span class="cn-word" data-tr="kechuv">ford</span>, and you need dry socks in your
bag.</p>

<p>The <span class="cn-word" data-tr="farq">difference</span> matters more than it looks. Both
places touch the river on the page. Only one of them gets you wet.</p>

<p>Last the <span class="cn-word" data-tr="burilishlar">turns</span>. Every time the line stops
rising and begins to fall you have reached a <span class="cn-word"
data-tr="cho'qqi">summit</span>, and a line with four turns has four of them, whatever the
guidebook's <span class="cn-word" data-tr="matn">text</span> promises about a gentle
afternoon.</p>
""",
        "grammar": [
            {"pattern": "touches the water and turns back up",
             "meaning": "suvga tegib qaytadi — juft karralilikdagi urinish"},
            {"pattern": "goes straight through and out the other side",
             "meaning": "kesib oʻtadi — toq karralilikdagi kesish"},
            {"pattern": "high on the left and high on the right",
             "meaning": "ikki chekka ham yuqorida — juft darajaning chekka xatti-harakati"},
        ],
        "questions": [
            {"text": "What does the profile show?",
             "choices": ["The height of the path against the distance walked",
                         "A map of the route", "The weather for the day",
                         "The river's depth"],
             "answer": 0,
             "explanation": "Bu xarita emas — balandlik bosib oʻtilgan masofaga "
                            "nisbatan chizilgan."},
            {"text": "What is the difference between the two places where the line meets the "
                     "river?",
             "choices": ["One is deeper than the other",
                         "One is at the start and one at the end",
                         "At one the path touches and turns back; at the other it goes through",
                         "One is on the map and one is not"],
             "answer": 2,
             "explanation": "Ikkalasi ham qogʻozda suvga tegadi, lekin biri qaytadi, "
                            "ikkinchisi kesib oʻtadi — faqat bittasida oyoq hoʻl "
                            "boʻladi."},
            {"text": "What do the two ends of the line tell a walker?",
             "choices": ["How long the walk is",
                         "Whether the walk starts and finishes on high ground",
                         "Where the river is",
                         "How many summits there are"],
             "answer": 1,
             "explanation": "Chekkalar oʻrtada nima boʻlishidan qatʼi nazar, "
                            "boshlanish va tugash balandligini koʻrsatadi."},
        ],
    },

    # ── 44 · a legend ────────────────────────────────────────────────
    {
        "title": "The Squares of the Chessboard",
        "order": 44,
        "summary": (
            "Shohga arzon koʻringan sovgʻa: birinchi katakka bir donadan, "
            "keyin har safar ikki barobar."
        ),
        "body": """
<p>The story is old and told in many countries, and the details change, but the arithmetic never
does. An <span class="cn-word" data-tr="ixtirochi">inventor</span> brings a new game to a
<span class="cn-word" data-tr="shoh, hukmdor">king</span>, who is delighted with it and offers
him any <span class="cn-word" data-tr="mukofot">reward</span> he likes.</p>

<p>The inventor asks for <span class="cn-word" data-tr="don, guruch donasi">grains</span> of
rice. One on the first square of the board, two on the second, four on the third, and so on:
each square carrying twice what the square before it carried, to the sixty-fourth.</p>

<p>The king laughs and agrees. It sounds like a <span class="cn-word"
data-tr="kamtarona">modest</span> request. On the tenth square there are only five hundred and
twelve grains — not yet a <span class="cn-word" data-tr="hovuch">handful</span>.</p>

<p>By the twentieth square the number has passed half a million. By the twenty-first it is over a
million, and the <span class="cn-word" data-tr="omborchi">granary keeper</span> has begun to
count in sacks rather than grains. Long before the last square, the sums have run past every
<span class="cn-word" data-tr="omborxona">store</span> in the <span class="cn-word" data-tr="podsholik">kingdom</span>, and past every <span class="cn-word" data-tr="hosil">harvest</span>
that kingdom would ever gather.</p>

<p>What makes the story last is not the size of the final number. It is the
<span class="cn-word" data-tr="birinchi yarmi">first half</span>, where nothing appears to be
happening. Anyone watching the early squares would have agreed with the king. The mistake was not
in the arithmetic. It was in judging a doubling by its beginning.</p>

<p>A gift of a thousand grains a square, on every square, would have cost sixty-four thousand
grains — a <span class="cn-word" data-tr="qop">sack</span> or two. The inventor asked for
something that starts at one, and it broke the
<span class="cn-word" data-tr="xazina">treasury</span>.</p>
""",
        "grammar": [
            {"pattern": "twice what the square before it carried",
             "meaning": "oldingisidan ikki barobar — koʻrsatkichli oʻsishning taʼrifi"},
            {"pattern": "a thousand grains on every square",
             "meaning": "har katakka ming donadan — chiziqli variant, taqqoslash uchun"},
            {"pattern": "judging a doubling by its beginning",
             "meaning": "ikkilanishni boshlanishiga qarab baholash — asosiy xato"},
        ],
        "questions": [
            {"text": "How many grains are on the tenth square?",
             "choices": ["One thousand", "Five hundred and twelve", "Ten", "Half a million"],
             "answer": 1,
             "explanation": "Matn buni aytadi: besh yuz oʻn ikki — hali bir hovuch "
                            "ham emas."},
            {"text": "At which square does the number first pass a million?",
             "choices": ["The tenth", "The twentieth", "The twenty-first", "The sixty-fourth"],
             "answer": 2,
             "explanation": "Yigirmanchida yarim milliondan oshadi, yigirma "
                            "birinchida esa milliondan."},
            {"text": "What does the story say the king's real mistake was?",
             "choices": ["Judging a doubling by how it begins",
                         "Making a promise in public",
                         "Not counting the squares",
                         "Trusting the granary keeper"],
             "answer": 0,
             "explanation": "Arifmetikada xato yoʻq edi — xato birinchi yarmiga, "
                            "hech narsa sodir boʻlmayotgandek koʻringan qismiga "
                            "qarab hukm chiqarishda edi."},
        ],
    },

    # ── 45 · a cautionary tale about a rate ──────────────────────────
    {
        "title": "Only Three Percent a Month",
        "order": 45,
        "summary": (
            "Oyiga uch foiz yiliga oʻttiz olti foiz emas — chunki har oy foiz "
            "kattaroq summadan olinadi."
        ),
        "body": """
<p>The man who came to the shop was polite and unhurried, and his offer was simple. He would
<span class="cn-word" data-tr="qarz bermoq">lend</span> Zarina the money for the new
<span class="cn-word" data-tr="muzlatgich">freezer</span>, and she would pay him back over a
year, at <span class="cn-word" data-tr="foiz">interest</span> of only three percent a
month.</p>

<p>Three a month, she thought. Twelve months. That is thirty-six percent a year. High, but she
knew what the freezer would earn her, and thirty-six she could
<span class="cn-word" data-tr="koʻtarmoq, toʻlay olmoq">carry</span>.</p>

<p>Her daughter, who was home from <span class="cn-word" data-tr="universitet">university</span>,
asked to see the paper before her mother <span class="cn-word"
data-tr="imzolamoq">signed</span> it. Then she asked one question: in the second month, is the
three percent taken from what I <span class="cn-word" data-tr="qarz olmoq">borrowed</span>, or
from what I still owe?</p>

<p>From what she still owed. Which meant the second month's three percent was larger than the
first month's, and the third larger again.</p>

<p>The daughter worked it through on the back of a
<span class="cn-word" data-tr="chek, kvitansiya">receipt</span>. Over twelve months the
<span class="cn-word" data-tr="qarz">debt</span> did not grow by thirty-six percent. It grew by
just under <span class="cn-word" data-tr="qirq uch">forty-three</span>. On a large enough loan,
that <span class="cn-word" data-tr="farq">gap</span> was most of a month's profit from the
freezer.</p>

<p>Zarina did take the loan, in the end, from a
<span class="cn-word" data-tr="bank">bank</span>, at a rate she could compare properly. What her
daughter had given her was not an answer about freezers. It was the habit of asking what a
percentage is <span class="cn-word" data-tr="olinadi">taken</span> from, before agreeing to
it.</p>
""",
        "grammar": [
            {"pattern": "taken from what I still owe",
             "meaning": "qolgan qarzdan olinadi — shuning uchun foiz oʻsib boradi"},
            {"pattern": "it grew by just under forty-three",
             "meaning": "qirq uchdan sal kam oʻsdi — oyma-oy koʻpayishning natijasi"},
            {"pattern": "what a percentage is taken from",
             "meaning": "foiz nimadan olinadi — savolning oʻzagi"},
        ],
        "questions": [
            {"text": "Why is three percent a month not thirty-six percent a year?",
             "choices": ["Because a year has more than twelve months",
                         "Because each month's percentage is taken from a larger amount",
                         "Because the shop charged a fee",
                         "Because the freezer lost value"],
             "answer": 1,
             "explanation": "Har oy foiz qolgan qarzdan olinadi, va qarz oʻsib "
                            "borgani uchun har oygi qoʻshimcha ham oʻsadi."},
            {"text": "By roughly how much did the debt grow over the year?",
             "choices": ["Thirty-six percent", "Forty percent",
                         "Just under forty-three percent", "Fifty percent"],
             "answer": 2,
             "explanation": "Matn buni aniq aytadi: qirq uchdan sal kam — oʻttiz "
                            "oltidan ancha koʻp."},
            {"text": "What did the daughter really give her mother?",
             "choices": ["The habit of asking what a percentage is taken from",
                         "A cheaper freezer",
                         "A loan from the bank",
                         "A better receipt"],
             "answer": 0,
             "explanation": "Matn oxirida aytilgani: javob emas, balki kelishuvdan "
                            "oldin beriladigan savol."},
        ],
    },
]
