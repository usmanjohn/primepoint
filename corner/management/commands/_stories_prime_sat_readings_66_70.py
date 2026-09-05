# -*- coding: utf-8 -*-
"""Prime SAT Readings — 66–70 (SAT-66 … SAT-70 darslariga · Blok D).

Written with the overrides in corner/management/commands/toc_prime_sat_readings.txt
⛔ MATNDA ALGEBRAIK BELGI YOʻQ — miqdorlar faqat ingliz tilida, soʻz bilan.
   Geometriya matnlarida ham shunday: burchak va uzunlik soʻz bilan aytiladi.

Til: matn, sarlavha va savollar INGLIZCHA; summary, cn-word glosslari,
     "Exam English" izohlari va javob tushuntirishlari OʻZBEKCHA.

Ovozlar (14-batch erkakdan boshlanadi): 66 Guy · 67 Jenny · 68 Guy ·
                                        69 Jenny · 70 Guy

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_66_70.py --author=prime
    python manage.py gen_corner_audio --collection="Prime SAT Readings" \\
        --only <n> --voice en-US-GuyNeural         # ⚠️ --voice MAJBURIY
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

    # ── 66 · surveying ───────────────────────────────────────────────
    {
        "title": "The Check That Closes",
        "order": 66,
        "summary": (
            "Bir nuqta atrofidagi burchaklar 360 berishi kerak. Bermasa, "
            "xato bor — va u qayerdaligini shu tekshiruv aytadi."
        ),
        "body": """
<p>A <span class="cn-word" data-tr="yer oʻlchovchi">surveyor</span> standing in the middle of a
field turns her <span class="cn-word" data-tr="asbob">instrument</span> to each corner of the
plot in turn and records the angle between one corner and the next. When she has gone all the way
round she has a list of angles, and before she does anything else she adds them
<span class="cn-word" data-tr="birga, jamlab">together</span>.</p>

<p>They must come to three hundred and sixty. She has turned a
<span class="cn-word" data-tr="toʻliq aylanish">full circle</span> and stopped where she began.
There is no room for opinion about it.</p>

<p>If the total is three hundred and fifty-nine, or three hundred and sixty-one, she has made a
<span class="cn-word" data-tr="xato">mistake</span> somewhere, and she knows it before she leaves
the field. That is the whole <span class="cn-word" data-tr="qiymat">value</span> of the check: it
does not tell her which angle is wrong, but it tells her that one of them is, while the
<span class="cn-word" data-tr="asbob">equipment</span> is still set up and the light is still
good.</p>

<p>Her <span class="cn-word" data-tr="shogird">apprentice</span> asked why she bothered when the
instrument was <span class="cn-word" data-tr="aniq">accurate</span> to a fraction of a degree.
She said accuracy is not the point. Any single reading can be written down
<span class="cn-word" data-tr="notoʻgʻri">wrongly</span>, or taken to the wrong corner, or
recorded twice. The instrument cannot catch that. The
<span class="cn-word" data-tr="yigʻindi">total</span> can.</p>

<p>Surveyors call this closing, and every trade has its own version. A carpenter measures a
<span class="cn-word" data-tr="ramka">frame</span>'s two <span class="cn-word" data-tr="diagonal">diagonals</span>; an accountant balances two
columns. In each case a quantity that is
<span class="cn-word" data-tr="qatʼiy">fixed</span> in advance is compared with what the work
produced.</p>

<p>"Do the arithmetic that must come out," she told him. "It is the only kind that can tell you
you are <span class="cn-word" data-tr="noto'gri, xato">wrong</span>."</p>
""",
        "grammar": [
            {"pattern": "they must come to three hundred and sixty",
             "meaning": "yigʻindi 360 boʻlishi shart — toʻliq aylanish"},
            {"pattern": "a quantity fixed in advance",
             "meaning": "oldindan maʼlum boʻlgan miqdor — tekshiruv asosi"},
            {"pattern": "arithmetic that must come out",
             "meaning": "albatta toʻgʻri chiqishi kerak boʻlgan hisob"},
        ],
        "questions": [
            {"text": "Why must the angles total three hundred and sixty?",
             "choices": ["The instrument is set that way",
                         "She has turned a full circle and stopped where she began",
                         "The plot has four corners",
                         "It is a rule of surveying companies"],
             "answer": 1,
             "explanation": "Nuqta atrofini toʻliq aylanib chiqqan — bu geometrik "
                            "fakt, kelishuv emas."},
            {"text": "What does the check tell her, and what does it not tell her?",
             "choices": ["It tells her which angle is wrong",
                         "It tells her the plot's area",
                         "It tells her that one angle is wrong, but not which",
                         "It tells her nothing useful"],
             "answer": 2,
             "explanation": "Yigʻindi xatoning borligini koʻrsatadi, lekin "
                            "qaysi biri ekanini aytmaydi."},
            {"text": "Why does an accurate instrument not make the check unnecessary?",
             "choices": ["A reading can be written down wrongly or taken to the wrong corner",
                         "Instruments are never accurate",
                         "The field is too large",
                         "The apprentice might interfere"],
             "answer": 0,
             "explanation": "Asbob oʻlchaydi, lekin yozuvdagi yoki tartibdagi "
                            "xatoni tuta olmaydi — yigʻindi tutadi."},
        ],
    },

    # ── 67 · the loom ────────────────────────────────────────────────
    {
        "title": "The Thread That Crosses",
        "order": 67,
        "summary": (
            "Dastgohdagi iplar parallel; koʻndalang ip ularni bir xil burchak "
            "ostida kesib oʻtadi — va gilamning naqshi shundan chiqadi."
        ),
        "body": """
<p>On the <span class="cn-word" data-tr="toʻquv dastgohi">loom</span> the long threads run from
the top of the frame to the bottom, side by side, and they never meet. Keeping them
<span class="cn-word" data-tr="parallel">parallel</span> is the first job of the morning and the
one the weaver checks most often, because everything after it
<span class="cn-word" data-tr="bogʻliq">depends</span> on it.</p>

<p>The pattern comes from a thread that crosses them at a
<span class="cn-word" data-tr="qiya, burchak ostida">slant</span>. Where it passes the first long
thread it makes a certain angle; where it passes the second it makes exactly the same one, and it
goes on making that same angle at every thread it crosses, all the way across the
<span class="cn-word" data-tr="mato">cloth</span>.</p>

<p>That <span class="cn-word" data-tr="takrorlanish">repetition</span> is the pattern. A diagonal
stripe on a rug is not drawn stripe by stripe; it is one crossing angle, repeated because the
threads beneath it are parallel.</p>

<p>The weaver's <span class="cn-word" data-tr="oʻgʻli">son</span> once pulled the frame slightly
<span class="cn-word" data-tr="qiyshiq">out of square</span> while cleaning it, and the long
threads were no longer quite parallel. Nothing looked wrong at the top of the cloth. Half a metre
down, the stripe had begun to <span class="cn-word" data-tr="egilmoq">bend</span>, because the
angle it made was no longer the same at every thread.</p>

<p>They cut the piece out and started again, and the weaver used the
<span class="cn-word" data-tr="yoʻqotish">loss</span> to make the lesson stick. Parallel lines
give you one angle repeated for as long as you like. Lines that are
<span class="cn-word" data-tr="deyarli">almost</span> parallel give you an angle that changes so
slowly that you notice it only when the work is
<span class="cn-word" data-tr="tugagan">finished</span>.</p>
""",
        "grammar": [
            {"pattern": "makes exactly the same angle at every thread",
             "meaning": "har bir ipda aynan bir xil burchak — mos burchaklar"},
            {"pattern": "one crossing angle, repeated",
             "meaning": "bitta kesishish burchagi, takrorlangan"},
            {"pattern": "almost parallel",
             "meaning": "deyarli parallel — qoida ishlamaydi"},
        ],
        "questions": [
            {"text": "Where does the diagonal stripe come from?",
             "choices": ["One crossing angle, repeated at every parallel thread",
                         "The weaver drawing it stripe by stripe",
                         "The colour of the thread",
                         "The width of the frame"],
             "answer": 0,
             "explanation": "Iplar parallel boʻlgani uchun bitta burchak butun "
                            "mato boʻylab takrorlanadi."},
            {"text": "What happened when the frame was pulled out of square?",
             "choices": ["The threads broke",
                         "The colours changed",
                         "The stripe began to bend, because the angle was no longer the same",
                         "Nothing happened"],
             "answer": 2,
             "explanation": "Iplar parallel boʻlmay qolgach, kesishish burchagi "
                            "har bir ipda oʻzgara boshladi."},
            {"text": "Why was the fault not noticed at once?",
             "choices": ["The angle changed so slowly that it showed only later",
                         "The weaver was not watching",
                         "The light was poor",
                         "The son hid it"],
             "answer": 0,
             "explanation": "Deyarli parallel chiziqlarda burchak sekin "
                            "oʻzgaradi — xato ish tugaganda koʻrinadi."},
        ],
    },

    # ── 68 · geography of ideas ──────────────────────────────────────
    {
        "title": "A Triangle With Three Right Angles",
        "order": 68,
        "summary": (
            "Uchburchak burchaklari 180 beradi — tekislikda. Yer sharida esa "
            "uchta toʻgʻri burchakli uchburchak chizish mumkin."
        ),
        "body": """
<p>Every school teaches that the three angles of a triangle add to a hundred and eighty degrees,
and every school is right. What is usually left out is the
<span class="cn-word" data-tr="shart">condition</span> attached to it: the triangle has to be
drawn on a <span class="cn-word" data-tr="tekislik">flat surface</span>.</p>

<p>Here is a triangle that is not. Start at the North Pole and <span class="cn-word" data-tr="janubga yurmoq">walk south</span> until you reach the
<span class="cn-word" data-tr="ekvator">equator</span>. Turn left through a right angle and walk
along the equator for a <span class="cn-word" data-tr="chorak">quarter</span> of the way round
the world. Turn left through a right angle again and walk north, and you will arrive back at the
Pole.</p>

<p>You have walked a <span class="cn-word" data-tr="yopiq">closed</span> <span class="cn-word" data-tr="uch tomonli shakl">three-sided
figure</span>, and you turned through a right angle at the equator twice. The third angle, at the
Pole, is also a right angle, because the two southward paths left the Pole a quarter of the world
<span class="cn-word" data-tr="bir-biridan">apart</span>. Three right angles: two hundred and
seventy degrees.</p>

<p>Nothing is <span class="cn-word" data-tr="buzilgan">broken</span>. The hundred-and-eighty rule
was never a rule about triangles in general; it is a rule about triangles on a
<span class="cn-word" data-tr="tekis">plane</span>. On the
<span class="cn-word" data-tr="sirt">surface</span> of a sphere the total is always more than a
hundred and eighty, and how much more depends on how much of the sphere the triangle
<span class="cn-word" data-tr="qamraydi">covers</span>.</p>

<p>This matters to anyone who <span class="cn-word" data-tr="uchmoq">flies</span> or sails a long
way. It does not matter on an exam paper, where every triangle is flat — but knowing why the rule
holds is worth more than knowing that it does.</p>
""",
        "grammar": [
            {"pattern": "the condition attached to it",
             "meaning": "unga qoʻshilgan shart — qoida qachon ishlaydi"},
            {"pattern": "a closed three-sided figure",
             "meaning": "yopiq uch tomonli shakl"},
            {"pattern": "a rule about triangles on a plane",
             "meaning": "tekislikdagi uchburchaklar haqidagi qoida"},
        ],
        "questions": [
            {"text": "What condition does the hundred-and-eighty rule require?",
             "choices": ["The triangle must be small",
                         "The triangle must be drawn on a flat surface",
                         "The angles must be measured in degrees",
                         "The sides must be straight lines"],
             "answer": 1,
             "explanation": "Qoida tekislikdagi uchburchaklar uchun — matn buni "
                            "boshida aytadi."},
            {"text": "What do the three angles of the described triangle add to?",
             "choices": ["A hundred and eighty degrees", "Two hundred and seventy degrees",
                         "Three hundred and sixty degrees", "Ninety degrees"],
             "answer": 1,
             "explanation": "Uchta toʻgʻri burchak — har biri toʻqson, jami ikki "
                            "yuz yetmish."},
            {"text": "Why is nothing broken?",
             "choices": ["The rule was always about triangles on a plane",
                         "The walk was measured wrongly",
                         "The Earth is not really a sphere",
                         "The angles were not really right angles"],
             "answer": 0,
             "explanation": "Qoida umuman uchburchaklar haqida emas edi — u "
                            "tekislikdagilar haqida."},
        ],
    },

    # ── 69 · the kite ────────────────────────────────────────────────
    {
        "title": "Why the Kite Flies Straight",
        "order": 69,
        "summary": (
            "Varrakning ikki tomoni teng boʻlishi kerak — chunki teng "
            "tomonlar teng burchak beradi, va shamol shuni sezadi."
        ),
        "body": """
<p>The old man who made <span class="cn-word" data-tr="varrak">kites</span> for the children in
the square worked to one <span class="cn-word" data-tr="qoida">rule</span>, and he said it in the same words every time: the two sides must
be the <span class="cn-word" data-tr="bir xil">same</span>.</p>

<p>He measured them with a piece of string rather than a <span class="cn-word" data-tr="chizgʻich">ruler</span>, folding it in half to check.
Then he set the <span class="cn-word" data-tr="ko'ndalang tayoq">cross-piece</span> so that the
frame folded onto itself exactly. If it did, the two angles at the bottom
<span class="cn-word" data-tr="teng edi">matched</span>, and he did not need to measure them at
all.</p>

<p>A boy asked whether it really mattered, since the difference would be a
<span class="cn-word" data-tr="millimetr">millimetre</span> or two. The old man let him make one
that was <span class="cn-word" data-tr="bir oz">slightly</span> off, and they took it out
together.</p>

<p>It flew, and it <span class="cn-word" data-tr="tortmoq">pulled</span> to the left. The wind
pushed a little harder on the longer side, and the kite turned into that push, and kept turning,
and had to be brought down.</p>

<p>The old man's point was not about kites. Equal sides give equal angles, and the wind meets
both sides at the same <span class="cn-word" data-tr="qiyalik">slope</span>, so it pushes equally
and the kite goes where it is pointed. Unequal sides give unequal angles, and the wind
<span class="cn-word" data-tr="sezmoq">notices</span> a difference far too small for a boy's eye
to see.</p>

<p>"You cannot measure an angle in the sky," he said, giving the boy the string back. "You can
measure two sides on the <span class="cn-word" data-tr="stol">table</span>, and the angles look
after themselves."</p>
""",
        "grammar": [
            {"pattern": "equal sides give equal angles",
             "meaning": "teng tomonlar teng burchak beradi"},
            {"pattern": "the frame folded onto itself exactly",
             "meaning": "ramka oʻziga aynan buklandi — simmetriya tekshiruvi"},
            {"pattern": "the angles look after themselves",
             "meaning": "burchaklar oʻzini oʻzi hal qiladi"},
        ],
        "questions": [
            {"text": "How did the old man check the angles?",
             "choices": ["With a protractor",
                         "By measuring the two sides and folding the frame",
                         "By flying the kite",
                         "By eye"],
             "answer": 1,
             "explanation": "U burchaklarni umuman oʻlchamadi — teng tomonlarni "
                            "oʻlchadi, va burchaklar shundan chiqdi."},
            {"text": "What happened to the slightly uneven kite?",
             "choices": ["It would not fly",
                         "It flew but pulled to one side and kept turning",
                         "It flew perfectly",
                         "It broke in the air"],
             "answer": 1,
             "explanation": "Shamol uzunroq tomonga kuchliroq bosdi va varrak "
                            "oʻsha tomonga burila boshladi."},
            {"text": "What is his real point?",
             "choices": ["Measuring two sides on a table is easier than measuring angles in the sky",
                         "Kites should be small",
                         "String is better than a ruler",
                         "Children cannot make kites"],
             "answer": 0,
             "explanation": "Teng tomonlar teng burchakni kafolatlaydi, va "
                            "tomonlarni oʻlchash ancha oson."},
        ],
    },

    # ── 70 · the history of building ─────────────────────────────────
    {
        "title": "Twelve Knots",
        "order": 70,
        "summary": (
            "Oʻn ikki tugunli arqon — minglab yillar davomida qurilishchining "
            "toʻgʻri burchak yasash asbobi."
        ),
        "body": """
<p>Long before anyone wrote down a theorem about right-angled triangles, builders needed
<span class="cn-word" data-tr="toʻgʻri burchak">right angles</span>, and they had a tool for
making them that cost nothing: a loop of
<span class="cn-word" data-tr="arqon">rope</span> with twelve knots tied at equal
<span class="cn-word" data-tr="oraliq">intervals</span>.</p>

<p>Three people take hold of the loop, one at the first knot, one at the fourth, one at the
eighth, and pull it <span class="cn-word" data-tr="taranglashtirmoq">tight</span>. The rope
forms a triangle with sides of three, four and five
<span class="cn-word" data-tr="boʻlim">spaces</span>, and the angle between the short two is
exactly a right angle. Every time. Nobody has to measure anything.</p>

<p>It works because three multiplied by itself, plus four multiplied by itself, comes to exactly
the same number as five multiplied by itself. That is not a
<span class="cn-word" data-tr="taxminiy">rough</span> agreement, and the corner is not
<span class="cn-word" data-tr="deyarli">nearly</span> square. It is square.</p>

<p>The <span class="cn-word" data-tr="foydaliligi">usefulness</span> of the trick is that it
travels. It needs no instrument, no
<span class="cn-word" data-tr="daraja, gradus">degrees</span>, and no writing. A rope and three
pairs of hands will lay out the corner of a
<span class="cn-word" data-tr="poydevor">foundation</span> in a field with nothing else
available, and the corner will be true.</p>

<p>The rope is a theorem you can hold. Nothing about it needs to be believed on <span class="cn-word" data-tr="ishonch">trust</span>: pull it tight and the corner is there.</p>

<p>Modern builders still use it, usually with a
<span class="cn-word" data-tr="oʻlchov lentasi">tape measure</span> instead of knots and often
with larger numbers — six, eight and ten, or nine, twelve and fifteen. The
<span class="cn-word" data-tr="sonlar">numbers</span> change and the reason does not: any three
lengths in that proportion close into a right angle.</p>
""",
        "grammar": [
            {"pattern": "sides of three, four and five spaces",
             "meaning": "uch, toʻrt va besh boʻlimli tomonlar"},
            {"pattern": "not a rough agreement",
             "meaning": "taxminiy moslik emas — aniq tenglik"},
            {"pattern": "any three lengths in that proportion",
             "meaning": "shu nisbatdagi har qanday uch uzunlik"},
        ],
        "questions": [
            {"text": "How many knots does the loop have?",
             "choices": ["Three", "Nine", "Twelve", "Fifteen"],
             "answer": 2,
             "explanation": "Oʻn ikki tugun uch, toʻrt va besh boʻlimga "
                            "boʻlinadi — jami oʻn ikki."},
            {"text": "Why is the corner exactly square rather than nearly square?",
             "choices": ["The rope is very strong",
                         "Three and four multiplied by themselves total exactly what five does",
                         "The knots are tied carefully",
                         "Three people can pull evenly"],
             "answer": 1,
             "explanation": "Toʻqqiz qoʻshuv oʻn olti aynan yigirma beshga teng — "
                            "taxminiy emas."},
            {"text": "What makes the trick so useful?",
             "choices": ["It needs no instrument, no degrees and no writing",
                         "It is faster than a tape measure",
                         "It works only on flat ground",
                         "It was invented recently"],
             "answer": 0,
             "explanation": "Arqon va uch juft qoʻl yetarli — hech qanday "
                            "asbob kerak emas."},
        ],
    },
]
