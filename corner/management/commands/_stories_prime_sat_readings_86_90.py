# -*- coding: utf-8 -*-
"""Prime SAT Readings — 86-90 (Blok E: chizma, baho, vaqt, tuzoq, format).

Overrides in corner/management/commands/toc_prime_sat_readings.txt.

⚠️ Matn INGLIZCHA · summary, cn-word glosses, explanation OʻZBEKCHA.
⚠️ ⛔ Tanada algebraik belgi YOʻQ — miqdorlar ingliz tilida aytiladi.
⚠️ SUBJECT/COLLECTION oldingi fayldan aynan koʻchirilgan.

FAKTLAR (gate ularni tekshiradi):
  86 — Merkator proyeksiyasi burchakni saqlaydi, yuzani buzadi;
       Grenlandiya 2.17 mln km², Afrika 30.37 mln km² (≈ 14 barobar).
  87 — olomonni sanash: yuza × zichlik (Jacobs usuli, 1960-yillar).
  88 — marafon 42.195 km; 4 soatlik surʼat ≈ har km uchun 5 daqiqa 41 soniya.
  89 — Boeing Model 299, 1935-yil 30-oktabr, Wright Field: boshqaruv qulfi
       ochilmagan; javob — koʻproq mashq emas, TEKSHIRUV ROʻYXATI.
  90 — ISBN-13 nazorat raqami: 1 va 3 ga navbatma-navbat koʻpaytir,
       yigʻ, 10 dan qoldiqni ayir.
  ⛔ Kitob nomi, uchuvchi ismi, aniq narx — oʻylab topilmaydi.

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_86_90.py \\
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
# 86 — when a picture is honest about one thing and lying about another
# ─────────────────────────────────────────────────────────────────────
{
    "order": 86,
    "title": "The Map That Tells the Truth Sideways",
    "summary": (
        "Devordagi dunyo xaritasi burchaklar haqida rost, yuzalar haqida "
        "yolgʻon gapiradi — va u buni yashirmaydi (SAT-86)."
    ),
    "body": """
<p>Look at almost any world map on a classroom wall and Greenland will
appear to be about the size of Africa. It is not close. Africa covers
roughly thirty million <span class="cn-word" data-tr="maydon">square</span> kilometres and Greenland a little over two
million — <strong>about fourteen times larger</strong>, on a picture
where they look like neighbours.</p>

<p>This is not an error. The map was drawn in the sixteenth century for
<span class="cn-word" data-tr="dengizchilar">sailors</span>, and it does one thing superbly: it keeps
<span class="cn-word" data-tr="burchaklar">angles</span> honest. A
<span class="cn-word" data-tr="kompas yoʻnalishi">compass bearing</span> drawn as a straight line on that map is a real bearing
you can <span class="cn-word" data-tr="yoʻnaltirmoq, boshqarmoq">steer</span>. To buy that, the <span class="cn-word" data-tr="proyeksiya (xarita usuli)">projection</span> has to <span class="cn-word" data-tr="choʻzmoq">stretch</span> the world
sideways as it approaches the <span class="cn-word" data-tr="qutblar">poles</span>, and stretch it more the further
north or south you go. Greenland sits very far north. Africa sits on the
<span class="cn-word" data-tr="ekvator">equator</span>, where the
stretching is almost nothing.</p>

<p>So the map is not lying. It is answering a different question from
the one most readers ask it. A sailor reads it for
<span class="cn-word" data-tr="yoʻnalish">direction</span> and gets the
truth. A pupil reads it for <span class="cn-word"
data-tr="yuza, kattalik">area</span> and gets <span class="cn-word" data-tr="bemaʼnilik">nonsense</span> — and nothing on
the paper warns them, because the map was never
<span class="cn-word" data-tr="daʼvo qilmoq">claiming</span> to answer
that.</p>

<p>Every diagram carries the same <span class="cn-word" data-tr="koʻrinmas, jimgina">quiet</span> condition. A picture is drawn
to be accurate about something, and whatever it was not built to
preserve, it will quietly <span class="cn-word" data-tr="buzib koʻrsatmoq">distort</span>. The only safe habit is to ask, before
reading anything off a figure, which of its features are
<span class="cn-word" data-tr="ishonchli">reliable</span> and which are
merely <span class="cn-word" data-tr="bezak">decoration</span>.</p>
""",
    "grammar": [
        {"pattern": "about fourteen times larger",
         "meaning": "taxminan oʻn toʻrt barobar katta — SAT nisbatni shunday aytadi.",
         "examples": ["Africa is about fourteen times larger than Greenland."]},
        {"pattern": "it is answering a different question",
         "meaning": "u boshqa savolga javob beryapti — chizmaning cheklovi.",
         "examples": ["The figure is answering a different question from the one you asked."]},
        {"pattern": "drawn to be accurate about",
         "meaning": "… jihatidan aniq boʻlishi uchun chizilgan.",
         "examples": ["The map is drawn to be accurate about angles, not areas."]},
    ],
    "questions": [
        {"text": "What does the projection preserve correctly?",
         "choices": ["The area of every country", "The distance between cities",
                     "Angles, so a bearing can be steered", "The shape of the poles"],
         "answer": 2,
         "explanation": "U burchaklarni saqlaydi — dengizchilar uchun aynan "
                        "shu kerak edi."},
        {"text": "Africa covers about thirty million square kilometres and Greenland "
                 "a little over two million. Roughly how many Greenlands would fit "
                 "into Africa?",
         "choices": ["About three", "About fourteen", "About thirty", "About two"],
         "answer": 1,
         "explanation": "30 ni 2.17 ga boʻlsak, taxminan 14 chiqadi."},
        {"text": "What is the reading's advice about any diagram?",
         "choices": ["Never trust a printed figure",
                     "Ask which of its features it was built to preserve",
                     "Measure everything with a ruler",
                     "Prefer maps drawn after 1900"],
         "answer": 1,
         "explanation": "Chizma nimaga aniq boʻlishi uchun qilinganini bilish "
                        "kerak — qolgani bezak."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 87 — estimation done professionally
# ─────────────────────────────────────────────────────────────────────
{
    "order": 87,
    "title": "How to Count a Crowd You Cannot Count",
    "summary": (
        "Maydondagi olomonni hech kim birma-bir sanamaydi — uni yuza va "
        "zichlikdan chamalaydi (SAT-87)."
    ),
    "body": """
<p>When a square fills with people, two numbers usually appear in the
news the next morning, and they <span class="cn-word" data-tr="bir-biriga zid">disagree</span> by a factor of five. Neither
side counted anybody.</p>

<p>The method that serious estimates use was worked out in the nineteen
sixties by a journalism lecturer in California who could watch
<span class="cn-word" data-tr="norozilik namoyishi">demonstrations</span>
from his own window. He noticed that the paving of the <span class="cn-word" data-tr="maydon, skver">plaza</span> below was
a <span class="cn-word" data-tr="toʻr, katakcha">grid</span>, so he
counted the people in a few squares, took an <span class="cn-word" data-tr="oʻrtacha">average</span>, and <span class="cn-word" data-tr="koʻpaytirdi">multiplied</span> by
the number of squares. <strong>Area times density, and nothing
else.</strong></p>

<p>The density is where the <span class="cn-word" data-tr="bahs">argument</span> lives. A loose crowd, with room to
turn around, runs at roughly one person for every square metre. A
<span class="cn-word" data-tr="zich">dense</span> crowd waiting for a
<span class="cn-word" data-tr="sahna">stage</span> is nearer four people to the square metre. Choose the wrong
figure and your answer is out by four times before you have measured
anything — which is exactly how the same square produces two <span class="cn-word" data-tr="sarlavhalar">headlines</span>
that cannot both be right.</p>

<p>What the method does give you, reliably, is the
<span class="cn-word" data-tr="kattalik tartibi">order of magnitude</span>.
Nobody who has done the arithmetic will tell you a square holding
twenty thousand people held a million, because the space for a million
does not exist. An estimate that is honest about its own
<span class="cn-word" data-tr="aniqlik darajasi">precision</span> is
worth far more than a <span class="cn-word" data-tr="ishonch bilan aytilgan">confident</span> number with no <span class="cn-word" data-tr="hisob-kitob yoʻli">working</span> behind it.</p>
""",
    "grammar": [
        {"pattern": "out by four times",
         "meaning": "toʻrt barobar xato — «out by» xatoning kattaligini bildiradi.",
         "examples": ["Choose the wrong density and the answer is out by four times."]},
        {"pattern": "area times density",
         "meaning": "yuza × zichlik — chamalashning butun formulasi.",
         "examples": ["The estimate is simply area times density."]},
        {"pattern": "the order of magnitude",
         "meaning": "kattalik tartibi — javob mingdami, oʻn mingdami.",
         "examples": ["Estimation gives you the order of magnitude, not the exact number."]},
    ],
    "questions": [
        {"text": "What two quantities does the method multiply?",
         "choices": ["Length and width", "Area and density",
                     "Time and speed", "Height and weight"],
         "answer": 1,
         "explanation": "Yuza va zichlik — boshqa hech narsa emas."},
        {"text": "A plaza measures 60 metres by 50 metres and the crowd is loose, at "
                 "about one person to the square metre. About how many people are "
                 "there?",
         "choices": ["About 3,000", "About 110", "About 12,000", "About 300"],
         "answer": 0,
         "explanation": "Yuza 60 × 50 = 3,000 kvadrat metr, zichlik esa har "
                        "kvadrat metrga bir kishi."},
        {"text": "What does the reading say estimation reliably provides?",
         "choices": ["An exact headcount", "The order of magnitude",
                     "The mood of the crowd", "The number of squares"],
         "answer": 1,
         "explanation": "Aniq son emas — javobning kattalik tartibi."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 88 — pacing (sport)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 88,
    "title": "The Ten Minutes She Should Not Have Saved",
    "summary": (
        "Marafonchi yarim yoʻlni rejadan oʻn daqiqa oldin bosib oʻtdi — va "
        "bu yaxshi xabar emas edi (SAT-88)."
    ),
    "body": """
<p>The <span class="cn-word" data-tr="masofa">distance</span> is forty-two kilometres and a little more, and it does
not change for anybody. What changes is how a runner spends it.</p>

<p>Her <span class="cn-word" data-tr="reja">plan</span> was four hours, which works out at five minutes and
forty-one seconds for every kilometre — a number she had written on the
back of her hand. She reached the <span class="cn-word" data-tr="yarim yoʻl">halfway</span>
<span class="cn-word" data-tr="belgi, nuqta">mark</span> in one hour
and fifty minutes. Ten minutes ahead.</p>

<p>Her <span class="cn-word" data-tr="murabbiy">coach</span>, waiting there, did not look pleased.
<strong>Time saved early in a race is almost never kept.</strong> The
body is holding a fixed <span class="cn-word" data-tr="zaxira">store</span> of usable <span class="cn-word" data-tr="yoqilgʻi, quvvat">fuel</span>; spending it faster at the
start does not create more, it only moves the moment it runs out. Ten
minutes gained in the first half are <span class="cn-word" data-tr="odatda">typically</span> paid back with
<span class="cn-word" data-tr="foiz, ustama">interest</span> in the
last ten kilometres, where the pace <span class="cn-word" data-tr="keskin tushib ketadi">collapses</span> and every
<span class="cn-word" data-tr="chidamoq">endure</span>d kilometre costs
two minutes more than it should have.</p>

<p>The runners who finish near their plan are usually the ones who ran
the second half slightly faster than the first, which sounds impossible
and is mostly a matter of
<span class="cn-word" data-tr="intizom, oʻzini tuta bilish">discipline</span>
in the first hour, when everything feels easy and the <span class="cn-word" data-tr="vasvasa, istak">temptation</span> to
<span class="cn-word" data-tr="surʼatni oshirmoq">push</span> is strongest.</p>

<p>She finished in four hours and nineteen minutes. The ten minutes she
saved cost her twenty-nine.</p>
""",
    "grammar": [
        {"pattern": "works out at",
         "meaning": "hisoblanganda … chiqadi — natijani bildiradi.",
         "examples": ["Four hours works out at about five minutes forty per kilometre."]},
        {"pattern": "paid back with interest",
         "meaning": "ustama bilan qaytariladi — yoʻqotish kutilganidan katta.",
         "examples": ["Time saved early is paid back with interest at the end."]},
        {"pattern": "ten minutes ahead",
         "meaning": "rejadan oʻn daqiqa oldinda.",
         "examples": ["She reached halfway ten minutes ahead of her plan."]},
    ],
    "questions": [
        {"text": "Why was the coach not pleased?",
         "choices": ["She had taken the wrong route",
                     "Time saved early is usually lost again later",
                     "She had started too late",
                     "The distance had been measured wrongly"],
         "answer": 1,
         "explanation": "Erta tejalgan vaqt deyarli har doim oxirida "
                        "qaytariladi."},
        {"text": "She covered the first 21 kilometres in 105 minutes. What was her "
                 "pace per kilometre?",
         "choices": ["Six minutes", "Five minutes",
                     "Five minutes forty-one seconds", "Four minutes"],
         "answer": 1,
         "explanation": "105 ni 21 ga boʻlsak, har kilometrga 5 daqiqa."},
        {"text": "How much did the ten saved minutes finally cost her?",
         "choices": ["Ten minutes", "Nineteen minutes",
                     "Twenty-nine minutes", "Nothing at all"],
         "answer": 2,
         "explanation": "U rejadan 19 daqiqa kech tugatdi, oldinda esa "
                        "10 daqiqa bor edi: jami 29."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 89 — the predictable mistake and the two-second habit
# ─────────────────────────────────────────────────────────────────────
{
    "order": 89,
    "title": "The List That Was Written After the Crash",
    "summary": (
        "1935-yilda yangi samolyot halok boʻldi — va javob koʻproq mashq "
        "emas, qogʻozdagi roʻyxat boʻldi (SAT-89)."
    ),
    "body": """
<p>On the thirtieth of October 1935, at an <span class="cn-word" data-tr="aerodrom">airfield</span> in Ohio, the most
advanced aircraft in the world took off, climbed a little, <span class="cn-word" data-tr="koʻtarish kuchini yoʻqotdi">stalled</span> and
fell. Two of the five men on board died.</p>

<p>It had four engines where the aircraft it was competing against had
two, and a correspondingly longer list of things to set before it could
safely leave the ground.</p>

<p>The aeroplane was not <span class="cn-word" data-tr="nosoz">faulty</span>. The
<span class="cn-word" data-tr="tekshiruv">investigation</span> found
that a lock which holds the control surfaces still on the ground had
not been released. The <span class="cn-word" data-tr="ekipaj">crew</span> were among the most experienced pilots in
the service. They knew about the lock. They simply had one more thing
to remember than a person can reliably remember, and the thing they
forgot was the one that mattered.</p>

<p>The newspapers called the machine too complicated to fly. The pilots
disagreed, and their answer is why the story is still told.
<strong>They did not ask for more training. They wrote a
list.</strong></p>

<p>It fitted on an
<span class="cn-word" data-tr="konvert">envelope</span>: a short set of
checks for take-off, for flight, before landing, after landing.
<span class="cn-word" data-tr="oddiy, arzimas">Trivial</span> items,
every one of them already known to every pilot in the room. Aircraft of
that type went on to fly nearly two million miles without a comparable
accident, and the pre-flight
<span class="cn-word" data-tr="tekshiruv roʻyxati">checklist</span>
became <span class="cn-word" data-tr="meʼyor, qoida">standard</span> in
<span class="cn-word" data-tr="aviatsiya">aviation</span>.</p>

<p>The lesson has travelled a long way from aeroplanes. When a mistake
is <span class="cn-word" data-tr="oldindan aytsa boʻladigan">predictable</span>,
the <span class="cn-word" data-tr="davo, yechim">cure</span> is not more <span class="cn-word" data-tr="mahorat">skill</span>. It is a small fixed habit, performed the
same way every time, on the exact step where clever people are known to
slip.</p>
""",
    "grammar": [
        {"pattern": "the one that mattered",
         "meaning": "aynan muhimi — koʻpdan bittasi hal qiluvchi boʻlgan holat.",
         "examples": ["The step they forgot was the one that mattered."]},
        {"pattern": "when a mistake is predictable",
         "meaning": "xatoni oldindan aytish mumkin boʻlsa — tuzoqlar shunday.",
         "examples": ["When a mistake is predictable, a fixed habit beats more effort."]},
        {"pattern": "performed the same way every time",
         "meaning": "har safar bir xil bajariladigan — odatning taʼrifi.",
         "examples": ["A check performed the same way every time is worth more than talent."]},
    ],
    "questions": [
        {"text": "What was the pilots' response to the accident?",
         "choices": ["A written checklist of ordinary steps",
                     "A demand for longer training",
                     "A redesign of the controls",
                     "A ban on the aircraft"],
         "answer": 0,
         "explanation": "Ular koʻproq mashq emas, konvertga sigʻadigan "
                        "roʻyxat yozishdi."},
        {"text": "The new aircraft had four engines and the designs it was "
                 "competing against had two. How many times as many did it have?",
         "choices": ["Twice as many", "Four times as many",
                     "Half as many", "The same number"],
         "answer": 0,
         "explanation": "Toʻrtni ikkiga boʻlsak, ikki barobar — va har bir "
                        "qoʻshimcha dvigatel eslab qolinadigan narsani "
                        "koʻpaytiradi."},
        {"text": "What does the reading say is the cure for a predictable mistake?",
         "choices": ["Working more slowly", "Greater experience",
                     "A small fixed habit at the step where people slip",
                     "Checking every step twice"],
         "answer": 2,
         "explanation": "Kichik, oʻzgarmas odat — aynan xato qilinadigan "
                        "joyda."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 90 — a machine reads what you typed, not what you meant
# ─────────────────────────────────────────────────────────────────────
{
    "order": 90,
    "title": "The Last Digit Is Not a Digit",
    "summary": (
        "Kitob raqamining oxirgi raqami maʼlumot tashimaydi — u faqat "
        "boshqalarini tekshiradi (SAT-90)."
    ),
    "body": """
<p>The number printed under the <span class="cn-word" data-tr="shtrix-kod">barcode</span> of every book has thirteen
<span class="cn-word" data-tr="raqamlar">digits</span>, and the last one carries no information at all. Its only job is
to <span class="cn-word" data-tr="tutmoq, aniqlamoq">catch</span>
someone typing the other twelve wrongly.</p>

<p>The rule is fixed and public. Take the twelve digits in order and
multiply them <span class="cn-word" data-tr="navbatma-navbat">alternately</span> by one and by three — first digit by one,
second by three, third by one, and so on. Add the twelve results. The
check digit is whatever must be added to that <span class="cn-word" data-tr="yigʻindi">total</span> to reach the next
<span class="cn-word" data-tr="karrali">multiple</span> of ten.</p>

<p>Suppose the twelve digits give a weighted total of ninety-five. The
next multiple of ten is one hundred, so <strong>the check digit is
five</strong>. If the total already ends in zero, the check digit is
zero.</p>

<p>The point of the <span class="cn-word" data-tr="tartib, tuzilma">arrangement</span> is that almost any single mistyped
digit changes the total, and therefore fails the test. The number is
<span class="cn-word" data-tr="rad etiladi">rejected</span> before it ever reaches a
<span class="cn-word" data-tr="ombor, katalog">catalogue</span>, and
nobody spends an afternoon hunting for a book that does not exist.</p>

<p>There is a habit buried in that <span class="cn-word" data-tr="tuzilish, loyiha">design</span> worth carrying into any form
you fill in. A machine reads exactly what you typed, in the exact
<span class="cn-word" data-tr="shakl, koʻrinish">format</span> it
<span class="cn-word" data-tr="kutadi">expects</span>, and it has no way of knowing what you
<span class="cn-word" data-tr="nazarda tutmoq">meant</span>. A correct
value in the wrong shape is not a small problem. To the machine it is
simply <span class="cn-word" data-tr="notoʻgʻri">wrong</span>.</p>
""",
    "grammar": [
        {"pattern": "carries no information at all",
         "meaning": "hech qanday maʼlumot tashimaydi — faqat tekshiruv uchun.",
         "examples": ["The last digit carries no information; it only checks the rest."]},
        {"pattern": "the next multiple of ten",
         "meaning": "keyingi oʻnlik — 95 dan keyin 100.",
         "examples": ["Add whatever is needed to reach the next multiple of ten."]},
        {"pattern": "in the exact format it expects",
         "meaning": "u kutgan aniq koʻrinishda — grid-in qutisining qoidasi ham shu.",
         "examples": ["A machine reads what you typed, in the exact format it expects."]},
    ],
    "questions": [
        {"text": "What is the purpose of the last digit?",
         "choices": ["To identify the publisher",
                     "To detect a mistyped digit among the others",
                     "To show the year of printing",
                     "To make the number thirteen digits long"],
         "answer": 1,
         "explanation": "U maʼlumot bermaydi — faqat qolgan raqamlardagi "
                        "xatoni tutadi."},
        {"text": "The twelve digits give a weighted total of eighty-seven. What is "
                 "the check digit?",
         "choices": ["Seven", "Three", "Eight", "Zero"],
         "answer": 1,
         "explanation": "Keyingi oʻnlik — 90, va 90 dan 87 ni ayirsak, 3 "
                        "qoladi."},
        {"text": "What does the reading say about a correct value in the wrong "
                 "format?",
         "choices": ["The machine will usually accept it",
                     "It is a small problem, easily fixed later",
                     "To the machine it is simply wrong",
                     "It depends on the catalogue"],
         "answer": 2,
         "explanation": "Mashina siz nima nazarda tutganingizni bilmaydi — "
                        "notoʻgʻri shakl notoʻgʻri javob."},
    ],
},

]
