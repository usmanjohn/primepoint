# -*- coding: utf-8 -*-
"""Prime SAT Readings — 91-95 (Blok E: tarjima, tuzilma, chekka, matn, yozuv).

Overrides in corner/management/commands/toc_prime_sat_readings.txt.

⚠️ Matn INGLIZCHA · summary, cn-word glosses, explanation OʻZBEKCHA.
⚠️ ⛔ Tanada algebraik belgi YOʻQ.
⚠️ SUBJECT/COLLECTION oldingi fayldan aynan koʻchirilgan.

FAKTLAR (gate ularni tekshiradi):
  91 — Meyn shtatidagi sut kompaniyasi ishi (2017): qonun roʻyxatida bitta
       vergul yetishmagani ~5 million dollarga tushdi. Sud haydovchilar
       foydasiga hal qildi. ⛔ Kompaniya nomi va sudya ismi yozilmaydi.
  92 — shaxmat ustalari haqiqiy pozitsiyani yaxshi eslaydi, TASODIFIY
       joylashtirilgan donalarni esa yangi boshlovchidan yaxshi emas
       (Chase va Simon, 1973). Sabab — «boʻlaklab» koʻrish.
  93 — samolyot qanoti sinovda xizmatda kutiladigan eng katta yukning
       taxminan bir yarim barobarigacha egiladi — sinishigacha.
  94 — retseptni kattalashtirish arifmetikasi (oʻz sonlarimiz).
  95 — laboratoriya daftari: muqovalangan, raqamlangan, sanalangan,
       oʻchirilmaydi; patent bahslarida dalil boʻlib xizmat qiladi.
       ⛔ Aniq sud ishi nomlanmaydi.

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_91_95.py \\
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
# 91 — a sentence read two ways, and what it cost
# ─────────────────────────────────────────────────────────────────────
{
    "order": 91,
    "title": "The Comma That Was Worth Five Million",
    "summary": (
        "Qonundagi roʻyxatda bitta vergul yetishmadi — va sud ikki xil "
        "oʻqishning qaysi biri toʻgʻriligini hal qilishi kerak boʻldi (SAT-91)."
    ),
    "body": """
<p>In 2017 an American <span class="cn-word" data-tr="apellyatsiya sudi">appeal court</span> had to decide what a single sentence
meant, and about five million dollars turned on the answer.</p>

<p>A state law listed the kinds of work that do not earn <span class="cn-word" data-tr="ish vaqtidan tashqari haq">overtime</span> pay.
Seven of them were plain enough — canning, processing, preserving,
freezing, drying, marketing, storing — and then the list ended:
<i>packing for <span class="cn-word" data-tr="joʻnatma">shipment</span> or distribution</i>. Read one
way, that last item is two separate <span class="cn-word" data-tr="faoliyat turlari">activities</span> — packing, and also
distributing. Read the other way, it is one: packing, done for either
shipment or <span class="cn-word" data-tr="tarqatish">distribution</span>.</p>

<p>The <span class="cn-word" data-tr="haydovchilar">drivers</span> who
brought the case did not pack anything. They only drove. If the <span class="cn-word" data-tr="ibora">phrase</span>
named two activities, their work was on the list and their overtime was
gone. If it named one, they had been
<span class="cn-word" data-tr="haqi toʻlanmagan">underpaid</span> for
years.</p>

<p><strong>Nothing in the sentence settled it.</strong> The court noted
that a comma before the last item would have made the two-activity
reading plain, and that the comma was not there. It <span class="cn-word" data-tr="hukm chiqardi">ruled</span> for the
drivers, and the company later
<span class="cn-word" data-tr="kelishuvga kelmoq">settled</span> for
about five million dollars.</p>

<p>The <span class="cn-word" data-tr="dars, saboq">lesson</span> is not
about <span class="cn-word" data-tr="tinish belgilari">punctuation</span>.
It is that an English sentence can carry two <span class="cn-word" data-tr="tuzilmalar">structures</span> at once, and
that the reader — not the writer — is the one who has to notice. Exam
questions are built by people who know this. When a sentence is
<span class="cn-word" data-tr="ikki maʼnoli">ambiguous</span>, slow
down and write out both readings before choosing one.</p>
""",
    "grammar": [
        {"pattern": "read one way … read the other way",
         "meaning": "bir xil oʻqilsa … boshqacha oʻqilsa — ikki maʼnoni ochish usuli.",
         "examples": ["Read one way it means two activities; read the other, only one."]},
        {"pattern": "turned on the answer",
         "meaning": "javobga bogʻliq edi — «turn on» = hal qiluvchi omil.",
         "examples": ["Five million dollars turned on the meaning of one phrase."]},
        {"pattern": "packing for shipment or distribution",
         "meaning": "joʻnatish yoki tarqatish uchun qadoqlash — ikki maʼnoli iboraning oʻzi.",
         "examples": ["The phrase 'packing for shipment or distribution' has two readings."]},
    ],
    "questions": [
        {"text": "Seven activities are named plainly before the final phrase. Under "
                 "the reading that treats that phrase as two activities, how many "
                 "does the list name in all?",
         "choices": ["Nine", "Eight", "Seven", "Fourteen"],
         "answer": 0,
         "explanation": "Yettitasi aniq, oxirgi ibora esa ikkita — jami "
                        "toʻqqizta. Bitta oʻqishda esa sakkizta boʻlardi."},
        {"text": "What did the court say would have removed the ambiguity?",
         "choices": ["A comma before the final item",
                     "A longer list", "A different verb", "A footnote"],
         "answer": 0,
         "explanation": "Oxirgi banddan oldingi vergul ikki ish degan oʻqishni "
                        "aniq qilib qoʻyardi."},
        {"text": "What does the reading advise when a sentence is ambiguous?",
         "choices": ["Choose the shorter reading",
                     "Ask the writer what was meant",
                     "Write out both readings before choosing",
                     "Ignore the punctuation"],
         "answer": 2,
         "explanation": "Ikkala oʻqishni yozib chiqing, keyin tanlang."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 92 — seeing groups instead of parts
# ─────────────────────────────────────────────────────────────────────
{
    "order": 92,
    "title": "What the Chess Master Actually Sees",
    "summary": (
        "Usta taxtani donama-dona emas, boʻlaklab koʻradi — va tasodifiy "
        "qoʻyilgan donalarda uning ustunligi yoʻqoladi (SAT-92)."
    ),
    "body": """
<p>Show a chess <span class="cn-word" data-tr="usta">master</span> a
<span class="cn-word" data-tr="pozitsiya, joylashuv">position</span> from a real game for five seconds, take the board away, and
ask for it back. Most of the pieces will come back correctly. A
<span class="cn-word" data-tr="yangi boshlovchi">beginner</span> given the same five seconds will place four or five.</p>

<p>The obvious explanation is memory, and the obvious explanation is
wrong. In an <span class="cn-word" data-tr="tajriba">experiment</span> first run in the nineteen seventies, the same
masters were shown boards with the pieces
<span class="cn-word" data-tr="tasodifiy">randomly</span> <span class="cn-word" data-tr="sochilgan">scattered</span> —
positions that could never <span class="cn-word" data-tr="yuz bermoq">occur</span> in a game.
<strong>Their advantage almost entirely disappeared.</strong> They
placed about as many pieces as the beginners did.</p>

<p>What the master has is not a bigger memory. It is a
<span class="cn-word" data-tr="lugʻat, toʻplam">vocabulary</span> of
familiar <span class="cn-word" data-tr="boʻlak">chunks</span> — a
<span class="cn-word" data-tr="rokirovka qilingan">castled</span> king with its three pawns, a knight and bishop working
together. Where the beginner is holding twenty-five separate facts, the
master is holding five or six <span class="cn-word"
data-tr="tanish">familiar</span> shapes. Take the shapes away and there
is nothing left to hold.</p>

<p>The same thing happens on a page of algebra. A beginner reads a long
<span class="cn-word" data-tr="ifoda">expression</span> symbol by symbol and runs out of room. Somebody who has met
the shapes before sees three or four
<span class="cn-word" data-tr="tanib olmoq">recognisable</span> groups
and works with those. That is not <span class="cn-word" data-tr="isteʼdod">talent</span>. It is
<span class="cn-word" data-tr="taʼsir, uchrashuv">exposure</span> —
the same shapes, met often enough that the eye stops spelling them
out.</p>
""",
    "grammar": [
        {"pattern": "their advantage almost entirely disappeared",
         "meaning": "ustunligi deyarli butunlay yoʻqoldi — tajribaning hal qiluvchi natijasi.",
         "examples": ["On random boards their advantage almost entirely disappeared."]},
        {"pattern": "symbol by symbol",
         "meaning": "belgima-belgi — boʻlaklab koʻrishning aksi.",
         "examples": ["A beginner reads the expression symbol by symbol."]},
        {"pattern": "met often enough that",
         "meaning": "shu qadar koʻp uchraganki … — koʻnikma qanday paydo boʻladi.",
         "examples": ["The same shapes, met often enough that you stop spelling them out."]},
    ],
    "questions": [
        {"text": "What happened when the masters were shown random positions?",
         "choices": ["They did better than before",
                     "Their advantage almost vanished",
                     "They refused to take part",
                     "They needed only two seconds"],
         "answer": 1,
         "explanation": "Tasodifiy taxtada boʻlaklar yoʻq — demak ustaning "
                        "ustunligi ham yoʻqoladi."},
        {"text": "A beginner holds about twenty-five separate facts and a master "
                 "about five. Roughly how many times fewer items is the master "
                 "holding?",
         "choices": ["Five times fewer", "Twice as few",
                     "Twenty times fewer", "The same number"],
         "answer": 0,
         "explanation": "25 ni 5 ga boʻlsak, besh barobar kam boʻlak."},
        {"text": "What does the reading say the master's skill really is?",
         "choices": ["A naturally larger memory",
                     "Faster reading", "Exposure to the same shapes",
                     "Better eyesight"],
         "answer": 2,
         "explanation": "Isteʼdod emas — bir xil shakllarni koʻp marta "
                        "koʻrish."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 93 — testing to destruction
# ─────────────────────────────────────────────────────────────────────
{
    "order": 93,
    "title": "They Bend the Wing Until It Breaks",
    "summary": (
        "Qanot oddiy yukda emas, sinishigacha sinaladi — chegara faqat "
        "chekkada koʻrinadi (SAT-93)."
    ),
    "body": """
<p>Before a new <span class="cn-word" data-tr="yoʻlovchi samolyoti">airliner</span> carries anybody, one of them is built to be
<span class="cn-word" data-tr="sindirilgan, yoʻq qilingan">destroyed</span>.</p>

<p>The aircraft is fixed to the floor of a hall and
<span class="cn-word" data-tr="tros, arqon">cables</span> are <span class="cn-word" data-tr="biriktirilgan">attached</span>
along both wings. Then the wings are pulled upward, slowly, past the
<span class="cn-word" data-tr="yuk, yuklama">load</span> of a normal flight, past the load of the worst
<span class="cn-word" data-tr="notinch havo">turbulence</span> anyone
expects, and on to about one and a half times the greatest load the
wing should ever meet in <span class="cn-word" data-tr="xizmat, foydalanish">service</span>. The wingtips rise several metres.
Eventually something gives, and the <span class="cn-word" data-tr="muhandislar">engineers</span> go to look at
<span class="cn-word" data-tr="aynan qayerda">exactly where</span> it
gave.</p>

<p>Nobody learns anything from a wing under a normal load. It holds,
which was already known. <strong>A design only reveals its limit at the
extreme</strong>, and the extreme is the one place a
<span class="cn-word" data-tr="kamchilik">weakness</span> cannot
hide.</p>

<p>The habit is worth borrowing. A rule that has only been tried on
easy, ordinary cases has not really been tried. Push it to the <span class="cn-word" data-tr="chekkalar">edges</span> —
the empty case, the case of exactly one, the
<span class="cn-word" data-tr="salbiy, manfiy">negative</span> case,
the case that is <span class="cn-word" data-tr="bir oz">slightly</span>
less than one — and it will either hold or show you precisely where it
does not. Either answer is useful, and only one of them can be found in
the <span class="cn-word" data-tr="qulay, xotirjam">comfortable</span> middle.</p>
""",
    "grammar": [
        {"pattern": "past the load of a normal flight",
         "meaning": "oddiy parvoz yukidan oshib — «past» chegaradan oʻtishni bildiradi.",
         "examples": ["The test goes past the load of any normal flight."]},
        {"pattern": "one and a half times the greatest load",
         "meaning": "eng katta yukning bir yarim barobari.",
         "examples": ["The wing is pulled to one and a half times the greatest load."]},
        {"pattern": "a rule that has only been tried on easy cases",
         "meaning": "faqat oson holatlarda sinalgan qoida — hali sinalmagan qoida.",
         "examples": ["A rule tried only on easy cases has not really been tested."]},
    ],
    "questions": [
        {"text": "Why is the wing loaded far beyond a normal flight?",
         "choices": ["To make the test faster",
                     "Because a design only shows its limit at the extreme",
                     "To use up the spare aircraft",
                     "Because normal loads are unknown"],
         "answer": 1,
         "explanation": "Oddiy yukda qanot bardosh beradi — bu allaqachon "
                        "maʼlum; chegara faqat chekkada koʻrinadi."},
        {"text": "If the greatest load expected in service is 100 units, to about "
                 "what load is the wing pulled in the test?",
         "choices": ["150 units", "100 units", "50 units", "300 units"],
         "answer": 0,
         "explanation": "Bir yarim barobar: 100 ning 1.5 barobari 150."},
        {"text": "Which cases does the reading say a rule should be pushed to?",
         "choices": ["Only the largest possible values",
                     "The empty case, one, negatives and values just under one",
                     "Cases chosen at random",
                     "The cases most likely to occur"],
         "answer": 1,
         "explanation": "Nol, bir, manfiy va birdan sal kichik — aynan "
                        "chekka holatlar."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 94 — a recipe scaled up
# ─────────────────────────────────────────────────────────────────────
{
    "order": 94,
    "title": "Cooking for Three Hundred",
    "summary": (
        "Oshxonada retsept qayta yozilmaydi — u koʻpaytiriladi, va bitta "
        "koʻpaytuvchi butun kunni belgilaydi (SAT-94)."
    ),
    "body": """
<p>The card pinned above the <span class="cn-word" data-tr="peshtaxta, ish stoli">counter</span> is the same one the cook has used
at home for years. It serves six people and asks for four hundred and
fifty grams of <span class="cn-word" data-tr="un">flour</span>, three eggs and half a <span class="cn-word" data-tr="litr">litre</span> of milk.</p>

<p>Today the hall <span class="cn-word" data-tr="joy bor, sigʻdiradi">seats</span> three hundred.</p>

<p>The first thing she writes on the pad is not a <span class="cn-word" data-tr="miqdor">quantity</span>. It is a
single number: <strong>three hundred divided by six is fifty.</strong>
Everything on the card is now multiplied by that one <span class="cn-word" data-tr="son, raqam">figure</span>, and
nothing else has to be thought about again. The flour becomes
twenty-two and a half kilograms. The eggs become a hundred and fifty.
The milk becomes twenty-five litres.</p>

<p>The <span class="cn-word" data-tr="omborchi">storekeeper</span> asks
whether she is sure about the flour, because twenty-two kilograms
sounds like a great deal. She checks it the other way round: fifty
lots of four hundred and fifty grams, and four hundred and fifty grams
is a little under half a kilo, so fifty of them is a little under
twenty-five kilos. The two answers <span class="cn-word"
data-tr="mos keladi">agree</span>, and she signs the
<span class="cn-word" data-tr="talabnoma">requisition</span>.</p>

<p>The whole method is in that first line. A word problem is rarely
hard <span class="cn-word" data-tr="oʻz-oʻzicha">in itself</span>; it is
hard because the numbers arrive in a
<span class="cn-word" data-tr="tartibsiz">jumbled</span> order and in
different units. Find the one <span class="cn-word" data-tr="bogʻlanish, munosabat">relationship</span> that <span class="cn-word" data-tr="boshqaradi">governs</span> everything,
write it down before anything else, and the rest is
<span class="cn-word" data-tr="koʻpaytirish">multiplication</span>.</p>
""",
    "grammar": [
        {"pattern": "it serves six people",
         "meaning": "olti kishiga yetadi — retsept miqdorini bildirish usuli.",
         "examples": ["The recipe serves six people."]},
        {"pattern": "multiplied by that one figure",
         "meaning": "oʻsha bitta songa koʻpaytiriladi — masshtab koeffitsiyenti.",
         "examples": ["Everything is multiplied by that one figure."]},
        {"pattern": "checks it the other way round",
         "meaning": "teskari yoʻldan tekshiradi — nazorat hisobi.",
         "examples": ["She checks it the other way round and the answers agree."]},
    ],
    "questions": [
        {"text": "What does the cook write down first?",
         "choices": ["The amount of flour", "The number of eggs",
                     "The number that everything will be multiplied by",
                     "The time the meal is needed"],
         "answer": 2,
         "explanation": "Avval koʻpaytuvchi: 300 ni 6 ga boʻlgan natija."},
        {"text": "The recipe serves 6 and uses 450 grams of flour. How much flour is "
                 "needed for 300 people?",
         "choices": ["22.5 kilograms", "13.5 kilograms",
                     "2.25 kilograms", "45 kilograms"],
         "answer": 0,
         "explanation": "300 ÷ 6 = 50, va 50 × 450 g = 22,500 g, yaʼni "
                        "22.5 kg."},
        {"text": "What does the reading say makes a word problem hard?",
         "choices": ["The arithmetic itself",
                     "The numbers arriving jumbled and in different units",
                     "The length of the sentences",
                     "The absence of a calculator"],
         "answer": 1,
         "explanation": "Arifmetika emas — sonlarning tartibsiz va turli "
                        "birlikda kelishi."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 95 — the notebook
# ─────────────────────────────────────────────────────────────────────
{
    "order": 95,
    "title": "The Notebook You May Not Erase",
    "summary": (
        "Laboratoriya daftarining qoidalari gʻalati koʻrinadi — toki uning "
        "vazifasi eslash emas, isbotlash ekani ayon boʻlguncha (SAT-95)."
    ),
    "body": """
<p>A laboratory notebook has rules that look, at first, like <span class="cn-word" data-tr="ortiqcha ehtiyotkorlik">fussiness</span>.
It must be <span class="cn-word" data-tr="muqovalangan">bound</span>,
not a <span class="cn-word" data-tr="papka">folder</span> of <span class="cn-word" data-tr="boʻsh, alohida">loose</span> sheets. The pages must be numbered before anything
is written on them. Every <span class="cn-word" data-tr="yozuv">entry</span> carries the date. Nothing may be
<span class="cn-word" data-tr="oʻchirmoq">erased</span> — a mistake is
struck through with one line, so that what was written underneath can
still be read.</p>

<p>A typical bound notebook holds two hundred numbered pages, and a
researcher who fills three a day works through one in a little over two
months.</p>

<p>The reason for the rules is not <span class="cn-word" data-tr="tartiblilik">tidiness</span>. A notebook kept that way can be produced
years later as <span class="cn-word" data-tr="dalil">evidence</span>:
in <span class="cn-word" data-tr="patent nizolari">patent disputes</span>
over who had an idea first, in
<span class="cn-word" data-tr="tekshiruv">investigations</span> when a
result cannot be repeated, in any argument about what was actually done
and when. Loose pages prove nothing. A page that has been rubbed out
proves less than nothing.</p>

<p><strong>The notebook is not there to help the scientist
remember.</strong> It is there to make the work
<span class="cn-word" data-tr="tekshirib boʻladigan">checkable</span> —
by a <span class="cn-word" data-tr="hamkasb">colleague</span>, by a court, and above all by the writer on the morning
after, when the <span class="cn-word" data-tr="mulohaza, fikr yuritish">reasoning</span> that seemed obvious at midnight has to be
followed step by step.</p>

<p>Working paper in an exam is a small version of the same idea. It is
not a place to <span class="cn-word" data-tr="tirnamoq">scratch</span>
numbers while you think. It is where the question you were actually
answering stays visible, so that ten minutes later, when you come back
to it, you do not have to <span class="cn-word" data-tr="qayta tiklamoq">reconstruct</span>
<span class="cn-word" data-tr="oʻz fikringiz">your own thinking</span>
from nothing.</p>
""",
    "grammar": [
        {"pattern": "struck through with one line",
         "meaning": "bir chiziq bilan chizib tashlangan — oʻchirilmagan.",
         "examples": ["A mistake is struck through with one line, never erased."]},
        {"pattern": "produced as evidence",
         "meaning": "dalil sifatida taqdim etilgan.",
         "examples": ["The notebook can be produced as evidence years later."]},
        {"pattern": "the morning after",
         "meaning": "ertasi kuni ertalab — fikr endi ravshan koʻrinmaydigan payt.",
         "examples": ["It has to make sense to the writer on the morning after."]},
    ],
    "questions": [
        {"text": "A notebook holds 200 numbered pages and a researcher fills 3 a "
                 "day. About how many days does one notebook last?",
         "choices": ["About 67", "About 200", "About 600", "About 30"],
         "answer": 0,
         "explanation": "200 ni 3 ga boʻlsak, taxminan 67 kun — matndagi "
                        "«ikki oydan sal koʻproq» shu."},
        {"text": "Why is a mistake struck through rather than erased?",
         "choices": ["Erasing damages the paper",
                     "So that what was written can still be read",
                     "Because ink cannot be erased",
                     "To save time"],
         "answer": 1,
         "explanation": "Ostidagi yozuv oʻqilishi kerak — oʻchirilgan sahifa "
                        "hech narsani isbotlamaydi."},
        {"text": "What does the reading say working paper in an exam is for?",
         "choices": ["Scratching numbers while you think",
                     "Copying the question",
                     "Keeping the question you are answering visible",
                     "Practising handwriting"],
         "answer": 2,
         "explanation": "Siz javob berayotgan savol koʻrinib turishi uchun — "
                        "shunda qaytganda fikringizni qaytadan "
                        "tiklamaysiz."},
    ],
},

]
