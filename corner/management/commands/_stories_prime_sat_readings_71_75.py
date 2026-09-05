# -*- coding: utf-8 -*-
"""Prime SAT Readings — 71–75 (SAT-71 … SAT-75 darslariga · Blok D).

Written with the overrides in corner/management/commands/toc_prime_sat_readings.txt
⛔ MATNDA ALGEBRAIK BELGI YOʻQ — burchak va uzunlik soʻz bilan aytiladi.

Til: matn, sarlavha va savollar INGLIZCHA; summary, cn-word glosslari,
     "Exam English" izohlari va javob tushuntirishlari OʻZBEKCHA.

Ovozlar (15-batch ayoldan boshlanadi): 71 Jenny · 72 Guy · 73 Jenny ·
                                       74 Guy · 75 Jenny

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_71_75.py --author=prime
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

    # ── 71 · history of mathematics ──────────────────────────────────
    {
        "title": "The Diagonal That Broke the Rule",
        "order": 71,
        "summary": (
            "Tomoni bir boʻlgan kvadratning diagonalini hech qanday kasr bilan "
            "yozib boʻlmaydi — va bu kashfiyot butun bir maktabni larzaga soldi."
        ),
        "body": """
<p>An ancient <span class="cn-word" data-tr="maktab, taʼlimot">school</span> of mathematicians
held one idea above all others: that every length in the world could be written as one whole
number divided by another. A <span class="cn-word" data-tr="kasr">fraction</span>. Two lengths,
they believed, always shared some tiny common
<span class="cn-word" data-tr="oʻlchov birligi">measure</span> that fitted a whole number of
times into each.</p>

<p>Then someone looked at the simplest figure available: a square whose sides are one, and its
<span class="cn-word" data-tr="diagonal">diagonal</span>.</p>

<p>By the rule about right-angled triangles, that diagonal multiplied by itself must come to
exactly two. So the question is whether any fraction, multiplied by itself, gives two. It is a
short <span class="cn-word" data-tr="dalil, isbot">argument</span> to show that none does:
suppose such a fraction exists in its simplest form, and you can prove that both its numbers must
be even — which means it was not in its simplest form after all. The
<span class="cn-word" data-tr="taxmin">assumption</span> destroys itself.</p>

<p>The diagonal has a perfectly definite length. You can draw it with a
<span class="cn-word" data-tr="chizgʻich">ruler</span>. It simply cannot be written as one whole
number over another, and no amount of <span class="cn-word" data-tr="izlash">searching</span>
will ever produce one.</p>

<p>The number has a name now and a decimal expansion that never repeats and never <span class="cn-word" data-tr="tugamoq">ends</span>. Writing more digits of it is not progress towards a fraction; there is no fraction to reach.</p>

<p>The <span class="cn-word" data-tr="afsona">legend</span> says the man who found this was
punished for it, and the legend is probably not true. What is true is that the school's central
belief was <span class="cn-word" data-tr="notoʻgʻri">false</span>, and that the
<span class="cn-word" data-tr="qarshi misol">counterexample</span> was sitting in the corner of
every square anyone had ever drawn.</p>
""",
        "grammar": [
            {"pattern": "one whole number divided by another",
             "meaning": "bir butun son ikkinchisiga boʻlingan — kasr taʼrifi"},
            {"pattern": "the assumption destroys itself",
             "meaning": "taxmin oʻzini oʻzi inkor qiladi — teskaridan isbot"},
            {"pattern": "no amount of searching will produce one",
             "meaning": "qancha izlansa ham topilmaydi"},
        ],
        "questions": [
            {"text": "What did the school believe?",
             "choices": ["That squares are the simplest figure",
                         "That every length could be written as a fraction",
                         "That diagonals are always longer than sides",
                         "That numbers are infinite"],
             "answer": 1,
             "explanation": "Ularning markaziy eʼtiqodi shu edi: har qanday "
                            "uzunlikni ikki butun sonning nisbati bilan yozish "
                            "mumkin."},
            {"text": "How does the argument work?",
             "choices": ["It measures the diagonal very precisely",
                         "It assumes such a fraction exists and shows that assumption fails",
                         "It draws many squares",
                         "It uses a calculator"],
             "answer": 1,
             "explanation": "Kasr mavjud deb faraz qilinadi, va shu farazning "
                            "oʻzi ziddiyatga olib keladi."},
            {"text": "What is remarkable about where the counterexample was found?",
             "choices": ["It was in the corner of every square ever drawn",
                         "It was found in another country",
                         "It took centuries to find",
                         "It required new instruments"],
             "answer": 0,
             "explanation": "Eng oddiy shaklda — har kim chizgan kvadratning "
                            "burchagida turgan edi."},
        ],
    },

    # ── 72 · nature ──────────────────────────────────────────────────
    {
        "title": "Six Triangles in Every Cell",
        "order": 72,
        "summary": (
            "Asalari uyasining har bir katagi olti burchakli — va har bir "
            "oltiburchak oltita teng tomonli uchburchakdan iborat."
        ),
        "body": """
<p>Cut a honeycomb across and every cell is a
<span class="cn-word" data-tr="oltiburchak">hexagon</span>, the same shape repeated with no gaps
between the cells and no <span class="cn-word" data-tr="isrof, ortiqcha">waste</span>. Draw
lines from the centre of one cell to each of its six corners and the hexagon falls apart into six
<span class="cn-word" data-tr="teng tomonli">equilateral</span> triangles, all identical.</p>

<p>That is why the shape works. Six equilateral triangles fit around a point exactly, because
each contributes sixty degrees and six sixties make a full
<span class="cn-word" data-tr="burilish">turn</span>. Nothing is left over and nothing
<span class="cn-word" data-tr="ustma-ust tushmoq">overlaps</span>.</p>

<p>Squares also tile a surface without gaps, and so do triangles. What sets the hexagon apart is
the amount of <span class="cn-word" data-tr="devor">wall</span> required. For a given area, a
hexagonal grid needs less wall than a square grid, and much less than a triangular one — and wall
means <span class="cn-word" data-tr="mum">wax</span>, which the bees must make from
<span class="cn-word" data-tr="asal">honey</span>.</p>

<p>Mathematicians <span class="cn-word" data-tr="gumon qilmoq">suspected</span> for a very long
time that the hexagon is the best possible answer to this problem, and a complete
<span class="cn-word" data-tr="isbot">proof</span> arrived only in modern times. The bees did not
wait for it.</p>

<p>There is a second reason the shape suits a hive. A hexagon is close to a <span class="cn-word" data-tr="doira">circle</span>, which is the most efficient shape of all — but circles leave gaps between them, and a hexagon does not.</p>

<p>The <span class="cn-word" data-tr="foydali xulosa">useful part</span> for a student is
smaller and closer to hand. Any question about a regular hexagon can be turned into a question
about an equilateral triangle, and any question about an equilateral triangle becomes two
right-angled triangles the moment you drop a line from its
<span class="cn-word" data-tr="uchi">apex</span>.</p>
""",
        "grammar": [
            {"pattern": "six sixties make a full turn",
             "meaning": "oltita oltmish toʻliq burilishni beradi"},
            {"pattern": "for a given area",
             "meaning": "berilgan yuza uchun — taqqoslash sharti"},
            {"pattern": "can be turned into a question about",
             "meaning": "… haqidagi savolga aylantirish mumkin"},
        ],
        "questions": [
            {"text": "Why do six equilateral triangles fit around a point?",
             "choices": ["Because each contributes sixty degrees",
                         "Because they are small",
                         "Because bees arrange them",
                         "Because six is an even number"],
             "answer": 0,
             "explanation": "Oltita oltmish daraja toʻliq uch yuz oltmishni "
                            "beradi — ortiqcha ham, kam ham emas."},
            {"text": "What sets the hexagon apart from squares and triangles?",
             "choices": ["It is easier to build",
                         "It leaves fewer gaps",
                         "For a given area it needs less wall",
                         "It is stronger"],
             "answer": 2,
             "explanation": "Uchalasi ham boʻshliqsiz qoplaydi; farqi devor "
                            "miqdorida, va devor mum degani."},
            {"text": "What is the useful point for a student?",
             "choices": ["A hexagon question becomes an equilateral triangle question",
                         "Bees are good at geometry",
                         "Wax is expensive",
                         "Proofs take a long time"],
             "answer": 0,
             "explanation": "Oltiburchak uchburchakka, uchburchak esa ikkita "
                            "toʻgʻri burchakli uchburchakka aylanadi."},
        ],
    },

    # ── 73 · ancient history ─────────────────────────────────────────
    {
        "title": "Measuring a Pyramid With a Stick",
        "order": 73,
        "summary": (
            "Piramidaning balandligini oʻlchash uchun unga chiqish shart emas — "
            "tayoq, soya va nisbat yetadi."
        ),
        "body": """
<p>The story is told of a Greek traveller who was asked how tall the great
<span class="cn-word" data-tr="piramida">pyramid</span> was. Nobody knew. It was far too large to
<span class="cn-word" data-tr="koʻtarilmoq">climb</span> with a measuring line, and there was no
way to reach the top from the outside.</p>

<p>He pushed a <span class="cn-word" data-tr="tayoq">stick</span> upright into the sand, waited,
and measured two things: the length of the stick's
<span class="cn-word" data-tr="soya">shadow</span>, and the length of the pyramid's.</p>

<p>Suppose the stick stands two units tall and throws a shadow three units long, while the
pyramid's shadow reaches two hundred and ten. The sun is so far away that its rays arrive at the
same <span class="cn-word" data-tr="burchak">angle</span> everywhere in that field, so the stick
and its shadow form a triangle with exactly the same
<span class="cn-word" data-tr="shakl">shape</span> as the pyramid and its shadow — a small one
and a large one, otherwise identical.</p>

<p>Whatever the stick's height is compared with its shadow, the pyramid's height must be compared
with its own shadow in the same way. Two to three, and two hundred and ten to one hundred and
forty. The pyramid is a hundred and forty units
<span class="cn-word" data-tr="baland">tall</span>.</p>

<p>Notice what he never had to know: the length of the pyramid's sides, the size of its <span class="cn-word" data-tr="asos">base</span>, or how it was built. Two shadows and one stick were the whole of it.</p>

<p>The <span class="cn-word" data-tr="hiyla, usul">method</span> costs nothing and needs no
instrument. It is still used: a <span class="cn-word" data-tr="oʻrmonchi">forester</span>
measuring a tree, a <span class="cn-word" data-tr="talaba">student</span> measuring a school
building. The only <span class="cn-word" data-tr="talab">requirement</span> is that both shadows
be measured at the same <span class="cn-word" data-tr="lahza">moment</span>, because the angle
changes through the day.</p>
""",
        "grammar": [
            {"pattern": "the same shape, a small one and a large one",
             "meaning": "bir xil shakl, kichigi va kattasi — oʻxshashlik"},
            {"pattern": "compared with its shadow in the same way",
             "meaning": "soyasiga xuddi shunday nisbatda"},
            {"pattern": "at the same moment",
             "meaning": "bir vaqtning oʻzida — shart"},
        ],
        "questions": [
            {"text": "How tall is the pyramid in the example?",
             "choices": ["Two hundred and ten units", "A hundred and forty units",
                         "Three units", "Seventy units"],
             "answer": 1,
             "explanation": "Tayoq ikki, soyasi uch; demak balandlik soyaning "
                            "uchdan ikki qismi: ikki yuz oʻn ning uchdan "
                            "ikkisi."},
            {"text": "Why do the stick and the pyramid form the same shape?",
             "choices": ["They are the same height",
                         "The sun's rays arrive at the same angle everywhere in that field",
                         "Both are made of stone",
                         "Their shadows are equal"],
             "answer": 1,
             "explanation": "Quyosh juda uzoqda, shuning uchun nurlar bir xil "
                            "burchak ostida tushadi va uchburchaklar "
                            "oʻxshash boʻladi."},
            {"text": "What is the method's only requirement?",
             "choices": ["Both shadows must be measured at the same moment",
                         "The stick must be very tall",
                         "The ground must be sand",
                         "The pyramid must be square"],
             "answer": 0,
             "explanation": "Burchak kun davomida oʻzgaradi, shuning uchun "
                            "ikkala soya bir vaqtda oʻlchanishi shart."},
        ],
    },

    # ── 74 · biology ─────────────────────────────────────────────────
    {
        "title": "Why the Elephant Has Thick Legs",
        "order": 74,
        "summary": (
            "Hayvonni ikki barobar kattalashtirsangiz, ogʻirligi sakkiz barobar "
            "oshadi, suyagining kesimi esa atigi toʻrt barobar."
        ),
        "body": """
<p>Imagine an animal made twice as long, twice as wide and twice as tall — the same shape,
simply <span class="cn-word" data-tr="kattalashtirilgan">enlarged</span>. Its
<span class="cn-word" data-tr="ogʻirlik">weight</span> depends on how much
<span class="cn-word" data-tr="tana">body</span> there is, and body is a volume, so the weight
becomes eight times greater.</p>

<p>Now look at what has to <span class="cn-word" data-tr="koʻtarmoq">carry</span> that weight.
A bone holds a load across its <span class="cn-word" data-tr="kesim">cross-section</span>, and a
cross-section is an area, so it becomes only four times greater.</p>

<p>Eight times the weight on four times the
<span class="cn-word" data-tr="tayanch">support</span>. Every part of the bone now carries twice
what it did before. Double the animal again and the load doubles again. Long before an animal
reaches the size of a house, its legs must become
<span class="cn-word" data-tr="nomutanosib">disproportionately</span> thick, or they
<span class="cn-word" data-tr="sinmoq">break</span>.</p>

<p>That is exactly what large animals look like. An elephant's legs are thick
<span class="cn-word" data-tr="ustunlar">columns</span> held almost straight beneath it; a
<span class="cn-word" data-tr="sichqon">mouse</span> of the same shape would look absurd. The
mouse can afford thin bent legs because it weighs almost
<span class="cn-word" data-tr="hech narsa">nothing</span>.</p>

<p>Nothing in this argument is about bone. Swap in any material you like and the numbers do not change: eight against four, whatever the animal is made <span class="cn-word" data-tr="… dan yasalgan">of</span>.</p>

<p>The same rule limits <span class="cn-word" data-tr="hasharotlar">insects</span>, decides how
tall a tree can grow, and explains why a small
<span class="cn-word" data-tr="hayvon">creature</span> can fall a long way and walk off. It is
not biology. It is the fact that volume grows as the cube of length while area grows only as the
<span class="cn-word" data-tr="kvadrat">square</span>.</p>
""",
        "grammar": [
            {"pattern": "weight depends on volume",
             "meaning": "ogʻirlik hajmga bogʻliq — kub boʻyicha oshadi"},
            {"pattern": "a cross-section is an area",
             "meaning": "kesim — yuza, demak kvadrat boʻyicha oshadi"},
            {"pattern": "disproportionately thick",
             "meaning": "nomutanosib qalin — shakl saqlanmaydi"},
        ],
        "questions": [
            {"text": "If an animal is doubled in every direction, what happens to its "
                     "weight?",
             "choices": ["It doubles", "It becomes four times greater",
                         "It becomes eight times greater", "It stays the same"],
             "answer": 2,
             "explanation": "Ogʻirlik hajmga bogʻliq, hajm esa kub boʻyicha "
                            "oshadi: ikki kub sakkiz."},
            {"text": "What happens to the bone's cross-section?",
             "choices": ["It becomes four times greater", "It doubles",
                         "It becomes eight times greater", "It is unchanged"],
             "answer": 0,
             "explanation": "Kesim — yuza, va yuza kvadrat boʻyicha oshadi: "
                            "ikki kvadrat toʻrt."},
            {"text": "What does the reading say the rule really is?",
             "choices": ["Volume grows as the cube of length while area grows as the square",
                         "Big animals are stronger",
                         "Bones grow faster than muscle",
                         "Insects cannot grow large"],
             "answer": 0,
             "explanation": "Matnning oxirgi jumlasi: bu biologiya emas, "
                            "masshtab qoidasi."},
        ],
    },

    # ── 75 · navigation ──────────────────────────────────────────────
    {
        "title": "The Angle to the Star",
        "order": 75,
        "summary": (
            "Qutb yulduzining ufqdan balandligi — bu sizning kengligingiz. "
            "Bitta burchak bitta savolga javob beradi."
        ),
        "body": """
<p>For centuries a <span class="cn-word" data-tr="dengizchi">sailor</span> far from land could
answer one of the two questions that mattered, and only one. The question he could answer was how
far <span class="cn-word" data-tr="shimolda">north</span> he was.</p>

<p>The instrument was a <span class="cn-word" data-tr="sekstant">sextant</span>, and the
measurement took a minute. He looked at the star that sits almost exactly above the north
<span class="cn-word" data-tr="qutb">pole</span> and measured the angle between it and the
<span class="cn-word" data-tr="ufq">horizon</span>. That angle is his
<span class="cn-word" data-tr="kenglik">latitude</span>. Not roughly — that is what latitude
means.</p>

<p>Stand at the equator and the star sits on the horizon: an angle of nothing, and a latitude of
nothing. Stand at the pole itself and the star is straight
<span class="cn-word" data-tr="tepada">overhead</span>: a right angle, and the highest latitude
there is. In Tashkent it stands about forty-one degrees above the northern horizon, which is
exactly how far north Tashkent lies.</p>

<p>The second question — how far east or west — needed an accurate
<span class="cn-word" data-tr="soat">clock</span>, and for a long time no clock could keep time
on a moving ship. Ships were <span class="cn-word" data-tr="yoʻqolgan">lost</span> for want of
it.</p>

<p>What makes the first measurement work is that a triangle's angles do not care about its
<span class="cn-word" data-tr="oʻlcham">size</span>. The triangle joining the sailor, the centre
of the Earth and the direction of the star is
<span class="cn-word" data-tr="ulkan">enormous</span>, and he measures one of its angles from
the deck of a small <span class="cn-word" data-tr="kema">ship</span> with a piece of brass.</p>
""",
        "grammar": [
            {"pattern": "the angle between it and the horizon",
             "meaning": "u bilan ufq orasidagi burchak"},
            {"pattern": "not roughly — that is what latitude means",
             "meaning": "taxminan emas — kenglikning taʼrifi shu"},
            {"pattern": "angles do not care about size",
             "meaning": "burchaklar oʻlchamga bogʻliq emas"},
        ],
        "questions": [
            {"text": "What does the angle to the Pole Star give directly?",
             "choices": ["The distance to land", "The sailor's latitude",
                         "The time of day", "The ship's speed"],
             "answer": 1,
             "explanation": "Ufqdan yulduzgacha boʻlgan burchak — bu aynan "
                            "kenglik, taxminiy emas."},
            {"text": "What does a sailor at the equator see?",
             "choices": ["The star straight overhead",
                         "The star on the horizon",
                         "No star at all",
                         "The star at forty-one degrees"],
             "answer": 1,
             "explanation": "Ekvatorda burchak nol — kenglik ham nol."},
            {"text": "Why can the sailor measure an enormous triangle from a small ship?",
             "choices": ["Because a triangle's angles do not depend on its size",
                         "Because the sextant is very accurate",
                         "Because the star is close",
                         "Because the ship is stationary"],
             "answer": 0,
             "explanation": "Burchak nisbatdan chiqadi, nisbat esa oʻlchamga "
                            "bogʻliq emas — matnning oxirgi fikri."},
        ],
    },
]
