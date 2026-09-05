# -*- coding: utf-8 -*-
"""Prime SAT Readings — 76-80 (Blok D yakuni: burchak va aylana).

Overrides in corner/management/commands/toc_prime_sat_readings.txt.

⚠️ Matn INGLIZCHA · summary, cn-word glosses, explanation OʻZBEKCHA.
⚠️ ⛔ Tanada algebraik belgi YOʻQ — miqdorlar ingliz tilida aytiladi.
⚠️ SUBJECT/COLLECTION oldingi fayldan aynan koʻchirilgan.
⚠️ Faktlar rost: al-Xorazmiy, markaziy pivot sugʻorish, seysmik tarmoq.

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_76_80.py \\
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
# 76 — complementary angles (a trade / workplace text)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 76,
    "title": "Two Ways to Say the Same Roof",
    "summary": (
        "Bir tomni ikki usta ikki xil burchak bilan taʼriflaydi — va ikkala son "
        "ham toʻgʻri, chunki ular 90 ga toʻldiradi (SAT-76)."
    ),
    "body": """
<p>On the first morning of the job, the roofer and the surveyor gave the
<span class="cn-word" data-tr="arxitektor, loyihachi">architect</span> two different numbers for the same roof, and both of them were
right.</p>

<p>The roofer measures from the <span class="cn-word" data-tr="gorizontal
nur, koʻndalang boʻlak">beam</span> that runs along the top of the wall.
Standing on it, he looks up along the <span class="cn-word"
data-tr="qiyalik, nishab">slope</span> and reads thirty-five degrees.
That is the number his <span class="cn-word" data-tr="kasb, hunar">trade</span> has always used, because it tells him how
hard the climb will be.</p>

<p>The surveyor measures from the <span class="cn-word"
data-tr="tik ustun">post</span> that stands at the <span class="cn-word" data-tr="tom qirrasi, choʻqqi chizigʻi">ridge</span>. Looking down
along the same slope, her <span class="cn-word" data-tr="asbob">instrument</span> reads fifty-five degrees. That is
the number her office needs, because it tells her how much of the roof
will show on a plan drawn from above.</p>

<p>The architect wrote both in her notebook and drew a small triangle
beside them. The corner where the post meets the beam is a <span class="cn-word" data-tr="toʻgʻri burchak">right angle</span>,
and the three corners of any triangle come to one hundred and eighty
degrees. <strong>The two remaining angles must therefore add to
ninety.</strong> Thirty-five and fifty-five. Two names, one roof.</p>

<p>There is a second <span class="cn-word" data-tr="natija, oqibat">consequence</span>, and it is the one the calculator
cares about. The roofer's <span class="cn-word" data-tr="nisbat">ratio</span>
of the <span class="cn-word" data-tr="balandlik">height</span> of the
roof to the length of the slope is exactly the surveyor's ratio of the
same height to the same slope — the two of them are describing one pair
of sides from <span class="cn-word" data-tr="qarama-qarshi burchaklardan">opposite corners</span>. What one calls the sine, the other calls
the <span class="cn-word" data-tr="kosinus">cosine</span>, and the number
underneath is <span class="cn-word" data-tr="aynan bir xil">identical</span>.</p>

<p>"So we never have to convert," the roofer said.</p>

<p>"We never did," said the surveyor. "We just <span class="cn-word"
data-tr="taxmin qilmoq, oʻylab qoʻymoq">assumed</span> we disagreed."</p>
""",
    "grammar": [
        {"pattern": "the two remaining angles add to ninety",
         "meaning": "qolgan ikki burchak 90 ga toʻldiradi — toʻldiruvchi burchaklar taʼrifi.",
         "examples": ["In a right triangle, the two remaining angles add to ninety."]},
        {"pattern": "measured from the horizontal / from the vertical",
         "meaning": "gorizontaldan / vertikaldan oʻlchangan — bitta qiyalikning ikki burchagi.",
         "examples": ["The ramp rises at 8 degrees measured from the horizontal."]},
        {"pattern": "what one calls A, the other calls B",
         "meaning": "biri A desa, ikkinchisi B deydi — bir narsaning ikki nomi.",
         "examples": ["What the roofer calls the sine, the surveyor calls the cosine."]},
    ],
    "questions": [
        {"text": "Why are both measurements correct?",
         "choices": ["The instruments were poorly calibrated",
                     "They are measured from different starting lines",
                     "The roof changed during the morning",
                     "One of them rounded the number"],
         "answer": 1,
         "explanation": "Biri gorizontal beamdan, ikkinchisi tik postdan oʻlchagan — "
                        "bitta qiyalikning ikki burchagi."},
        {"text": "A third worker measures a different roof from the horizontal and "
                 "reads twenty-eight degrees. What would the surveyor read on that "
                 "same roof?",
         "choices": ["28 degrees", "56 degrees", "62 degrees", "152 degrees"],
         "answer": 2,
         "explanation": "Ikki burchak 90 ga toʻldiradi: 90 − 28 = 62."},
        {"text": "What does the last line mean?",
         "choices": ["Their numbers had never actually conflicted",
                     "One of them had been careless",
                     "They will use one instrument from now on",
                     "The architect made a mistake"],
         "answer": 0,
         "explanation": "Ular hech qachon qarama-qarshi narsa aytmagan — shunchaki "
                        "boshqa chiziqdan oʻlchashgan."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 77 — arc length (how things work)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 77,
    "title": "The Wheel That Counts the Road",
    "summary": (
        "Mashinaning yoʻl hisoblagichi masofani oʻlchamaydi — u gʻildirak "
        "aylanishlarini sanaydi, xolos (SAT-77)."
    ),
    "body": """
<p>No car has ever measured a road. What it measures is its own wheel.</p>

<p>A <span class="cn-word" data-tr="datchik, sezgich">sensor</span> on the <span class="cn-word" data-tr="oʻq, val">axle</span>
counts how many times the wheel comes round, and the display multiplies
that count by one number stored at the factory: the distance the wheel
covers in a single full turn. That distance is the way round the tyre,
and it depends on nothing but the tyre's <span class="cn-word" data-tr="radius">radius</span>.</p>

<p>The arithmetic is unglamorous and exact. A tyre with a radius of
thirty centimetres carries the car about 188 centimetres forward in one
<span class="cn-word" data-tr="toʻliq aylanish">complete turn</span>. Roll it half a turn and the car has moved half of that.
Roll it a <span class="cn-word" data-tr="chorak">quarter</span> turn and
it has moved a quarter. <strong>The distance travelled is the same
fraction of the way round as the turn is of a full circle</strong> —
which is why a wheel is such a convenient ruler.</p>

<p>It is also why the number can drift. As a tyre <span class="cn-word" data-tr="yeyiladi, ishqalanib kichrayadi">wears</span>, its radius
<span class="cn-word" data-tr="qisqaradi">shrinks</span> by a millimetre or two. A smaller wheel must turn more often to
cover the same road, so the <span class="cn-word" data-tr="hisoblagich">counter</span> <span class="cn-word"
data-tr="ortiqcha koʻrsatadi">over-reads</span>: the driver is told he
has gone further than he has. Fitting tyres of the wrong size does the
same thing, only faster. <span class="cn-word" data-tr="havosi kam puflangan">Under-inflated</span> tyres <span class="cn-word"
data-tr="bir oz">slightly</span> flatten and shorten the roll as <span class="cn-word" data-tr="quduq">well</span>.</p>

<p>Cyclists meet the honest version of this. A bicycle computer knows
nothing until you tell it your wheel size, and if you type in the size
of the wheel you used to own, every ride afterwards is wrong by the
same <span class="cn-word" data-tr="ulush, foiz">percentage</span> —
<span class="cn-word" data-tr="sabr bilan, toʻxtovsiz">patiently</span>, in the same direction, for as long as you keep the machine.</p>
""",
    "grammar": [
        {"pattern": "the way round",
         "meaning": "aylana uzunligi (circumference) — SAT baʼzan shu oddiy ibora bilan aytadi.",
         "examples": ["The way round the tyre is about 188 centimetres."]},
        {"pattern": "the same fraction of A as B is of C",
         "meaning": "A ning C ga nisbati B ning C ga nisbati bilan bir xil — yoy = ulush.",
         "examples": ["The arc is the same fraction of the circle as the angle is of 360 degrees."]},
        {"pattern": "over-reads / under-reads",
         "meaning": "asbob haqiqiy qiymatdan katta / kichik koʻrsatadi.",
         "examples": ["A worn tyre makes the odometer over-read."]},
    ],
    "questions": [
        {"text": "What does the car actually count?",
         "choices": ["Metres of road", "Turns of its own wheel",
                     "Minutes of driving", "Litres of fuel used"],
         "answer": 1,
         "explanation": "Sensor gʻildirak aylanishlarini sanaydi; masofa shundan "
                        "hisoblab chiqariladi."},
        {"text": "The tyre in the text carries the car about 188 centimetres in a "
                 "full turn. How far does it carry the car in a quarter turn?",
         "choices": ["About 47 centimetres", "About 94 centimetres",
                     "About 62 centimetres", "About 188 centimetres"],
         "answer": 0,
         "explanation": "Chorak aylanish — chorak masofa: 188 ÷ 4 ≈ 47 sm. "
                        "Yoy uzunligi ham xuddi shunday ulush bilan topiladi."},
        {"text": "Why does a worn tyre make the counter over-read?",
         "choices": ["The car drives faster on worn tyres",
                     "The sensor becomes less accurate with age",
                     "A smaller wheel turns more often over the same road",
                     "The factory number is recalculated each year"],
         "answer": 2,
         "explanation": "Radius kichrayadi, demak bir xil yoʻl uchun koʻproq "
                        "aylanish kerak boʻladi — hisoblagich esa eski sonni "
                        "ishlatadi."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 78 — sectors (popular science / agriculture)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 78,
    "title": "The Green Circles You See From a Plane",
    "summary": (
        "Samolyot oynasidan koʻringan yashil doiralar — markaziy pivot "
        "sugʻorish; burchaklari esa quruq qoladi (SAT-78)."
    ),
    "body": """
<p>Fly over <span class="cn-word" data-tr="ekin maydonlari">farmland</span> almost anywhere and you will see them: perfect green
circles, packed side by side inside square fields. They are not a design
choice. They are the shape a machine makes when it turns.</p>

<p>A centre-pivot <span class="cn-word" data-tr="sugʻorish
qurilmasi">irrigator</span> is a long pipe on wheels, <span class="cn-word" data-tr="mahkamlangan">anchored</span> at one
end to a well in the middle of the field. The pipe walks slowly around
that <span class="cn-word" data-tr="markaz, oʻq">pivot</span>, watering
everything it passes over. Frank Zybach <span class="cn-word" data-tr="patentlagan">patented</span> the idea in the United
States in 1952, and it changed the look of the <span class="cn-word" data-tr="qishloq manzarasi">countryside</span> from the air
within a generation.</p>

<p>The geometry is <span class="cn-word" data-tr="shafqatsiz, xato kechirmaydigan">unforgiving</span>. A pipe four hundred metres long waters a
circle of radius four hundred metres. Set that circle inside the square
<span class="cn-word" data-tr="yer uchastkasi">plot</span> that surrounds it, and about seventy-nine percent of the square is
green. <strong>The remaining corners get nothing</strong> — roughly a
fifth of the land, left to dry grass or planted with something that can
live without the machine.</p>

<p>Not every pivot goes all the way round. A road, a canal or a
neighbour's <span class="cn-word" data-tr="chegara">boundary</span> can
stop the pipe partway, and then the wet ground is a
<span class="cn-word" data-tr="sektor, boʻlak">wedge</span> instead of a
<span class="cn-word" data-tr="disk, toʻla doira">disc</span>. The rule for how much land is watered is the same in both cases:
the wedge is the same share of the circle as its turn is of a full turn.
A pipe that sweeps a quarter of the way round waters a quarter of the
circle.</p>

<p>Farmers learn the numbers quickly, because the <span class="cn-word" data-tr="nasos">pump</span> is paid for by
the hour and the <span class="cn-word" data-tr="hosil">crop</span> is paid for by the <span class="cn-word"
data-tr="gektar">hectare</span>.</p>
""",
    "grammar": [
        {"pattern": "the same share of the circle as its turn is of a full turn",
         "meaning": "sektor aylananing shu ulushini egallaydi — burchak/360.",
         "examples": ["A 90-degree wedge is the same share of the circle as 90 is of 360."]},
        {"pattern": "the remaining corners",
         "meaning": "qolgan burchaklar — «remaining» SAT'da «qolgan qism» maʼnosida keladi.",
         "examples": ["The remaining region is what is left after the sector is removed."]},
        {"pattern": "a circle of radius four hundred metres",
         "meaning": "radiusi 400 metrli aylana — SAT radiusni shu tartibda aytadi.",
         "examples": ["Draw a circle of radius 6 centimetres."]},
    ],
    "questions": [
        {"text": "Why are the fields circular?",
         "choices": ["Circles hold water better than squares",
                     "The law requires round fields",
                     "It is the shape traced by a pipe turning around a fixed end",
                     "Square fields are more expensive to plough"],
         "answer": 2,
         "explanation": "Quvur bir uchi mahkamlangan holda aylanadi — u chizadigan "
                        "shakl aylana."},
        {"text": "A pivot sweeps only a quarter of the way round a circle of radius "
                 "400 metres. What fraction of the full circle does it water?",
         "choices": ["One quarter", "One half", "One eighth", "Three quarters"],
         "answer": 0,
         "explanation": "Sektor aylananing oʻsha ulushini egallaydi: chorak "
                        "aylanish — chorak yuza."},
        {"text": "About how much of the square plot is left unwatered?",
         "choices": ["About half", "About a fifth", "About two thirds", "Almost none"],
         "answer": 1,
         "explanation": "Matn 79 foizi yashil deydi, demak taxminan beshdan biri "
                        "quruq qoladi."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 79 — circles as sets of points (popular science)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 79,
    "title": "Three Stations and One Earthquake",
    "summary": (
        "Bitta stansiya zilzilagacha boʻlgan masofani biladi, joyini emas — "
        "uchtasi kerak boʻladi (SAT-79)."
    ),
    "body": """
<p>When the ground moves somewhere, it sends out two kinds of <span class="cn-word" data-tr="toʻlqin">wave</span>. The
first kind travels faster and arrives first. The second is slower and
arrives behind it. Every <span class="cn-word" data-tr="seysmik
stansiya">seismic station</span> records both, and the gap between the
two <span class="cn-word" data-tr="yetib kelishlar">arrivals</span> is the useful part: the further away the <span class="cn-word" data-tr="manba, zilzila oʻchogʻi">source</span>, the more
the fast wave has pulled ahead, so the wider the gap.</p>

<p>From that gap a station can work out how far away the earthquake was.
What it cannot do is say where. A single station knows one thing only —
<strong>the source lies somewhere on a circle</strong> drawn around the
station, with that distance as the radius. Every point on the circle
fits the reading equally well.</p>

<p>A second station, somewhere else, draws its own circle. The two
circles usually <span class="cn-word" data-tr="kesishadi">cross</span> at two points, and the earthquake is at one of
them. It takes a third station, and a third circle, to say which. Where
the three meet is the <span class="cn-word" data-tr="epitsentr,
oʻchoq">epicentre</span>, and that is why seismic <span class="cn-word" data-tr="tarmoqlar">networks</span> are built as
networks rather than as single instruments.</p>

<p>The method is old, careful and quietly beautiful. Nothing is
<span class="cn-word" data-tr="taxmin qilingan">guessed</span>; each
station <span class="cn-word" data-tr="chegaralamoq">narrows</span> the
possibilities, and the answer is whatever <span class="cn-word" data-tr="omon qoladi, tekshiruvdan oʻtadi">survives</span> all three. Distance
alone is a circle. Two distances leave a choice. Three leave a place.</p>

<p>The same reasoning runs, in three dimensions, inside every satellite
navigation <span class="cn-word" data-tr="qabul qilgich">receiver</span> in every telephone — <span class="cn-word" data-tr="sferalar">spheres</span> instead of circles, and
rather more of them.</p>
""",
    "grammar": [
        {"pattern": "lies somewhere on a circle around the station",
         "meaning": "stansiya atrofidagi aylananing biror nuqtasida yotadi — markaz + radius.",
         "examples": ["Every point that is 5 units from the centre lies on the circle."]},
        {"pattern": "with that distance as the radius",
         "meaning": "oʻsha masofa radius sifatida olinadi.",
         "examples": ["Draw a circle centred at the station with 200 km as the radius."]},
        {"pattern": "narrows the possibilities",
         "meaning": "imkoniyatlar doirasini toraytiradi — har bir shart javobni qisadi.",
         "examples": ["Each new reading narrows the possibilities."]},
    ],
    "questions": [
        {"text": "What can one station determine on its own?",
         "choices": ["The exact location of the earthquake",
                     "How far away the earthquake was",
                     "The direction the ground moved",
                     "Nothing at all"],
         "answer": 1,
         "explanation": "Ikki toʻlqin orasidagi farq masofani beradi — lekin "
                        "yoʻnalishni emas."},
        {"text": "Station A is 200 kilometres from the earthquake and Station B is "
                 "350 kilometres from it. The two stations are 600 kilometres apart. "
                 "Could the earthquake lie on the straight line between them?",
         "choices": ["Yes, exactly halfway",
                     "Yes, closer to Station A",
                     "No, because 200 and 350 together fall short of 600",
                     "There is not enough information"],
         "answer": 2,
         "explanation": "200 + 350 = 550, va bu 600 dan kichik — ikki masofa "
                        "stansiyalar orasini bogʻlay olmaydi (SAT-73 dagi "
                        "uchburchak tengsizligi)."},
        {"text": "Why must networks contain many stations?",
         "choices": ["To record louder signals",
                     "Because instruments often fail",
                     "Because circles from separate places must cross at one point",
                     "To measure the two wave types separately"],
         "answer": 2,
         "explanation": "Bitta aylana — cheksiz nuqta; ikkitasi — ikki nuqta; "
                        "uchtasi bitta joyni qoldiradi."},
    ],
},

# ─────────────────────────────────────────────────────────────────────
# 80 — completing the square (history of mathematics)
# ─────────────────────────────────────────────────────────────────────
{
    "order": 80,
    "title": "The Square That al-Khwarizmi Completed",
    "summary": (
        "«Toʻliq kvadratga toʻldirish» iborasi majoziy emas — u aslida chizmada "
        "yetishmayotgan burchakni toʻldirish edi (SAT-80)."
    ),
    "body": """
<p>The phrase is nine hundred years older than the <span class="cn-word" data-tr="matematik belgilar tizimi">notation</span> it now
describes, and it once meant exactly what it says.</p>

<p>Around the year 820, in Baghdad, a <span class="cn-word" data-tr="olim">scholar</span> wrote a short book on
solving problems about <span class="cn-word" data-tr="nomaʼlum miqdorlar">unknown quantities</span>. His name points to
<span class="cn-word" data-tr="Xorazm">Khwarazm</span>, the region south
of the Aral Sea, and it has come down to us twice: the <span class="cn-word" data-tr="lotincha">Latin</span> form of
his name gave us the word <span class="cn-word"
data-tr="algoritm">algorithm</span>, and a word from the title of the
book gave us <span class="cn-word" data-tr="algebra">algebra</span>.</p>

<p>He had no <span class="cn-word" data-tr="belgilar">symbols</span>. There was no letter standing for the unknown, no
<span class="cn-word" data-tr="tenglik belgisi">equals sign</span>, not even a plus. Every problem was set out in
<span class="cn-word" data-tr="soʻzlar bilan">words</span>, and every
solution was <span class="cn-word" data-tr="isbotlangan">justified</span>
by a drawing.</p>

<p>Here is one of his, in his own shape. A square field of unknown side,
together with two <span class="cn-word" data-tr="tasmalar, uzun boʻlaklar">strips</span> five <span class="cn-word" data-tr="qadam (uzunlik oʻlchovi)">paces</span> wide laid along two of its edges,
covers thirty-nine square paces in all. Draw it: the square, a strip
down one side, a strip along the bottom. One corner of the picture is
empty — a small square, five paces by five paces, missing.
<strong>Complete it.</strong> Adding that corner adds twenty-five square
paces, so the finished <span class="cn-word" data-tr="shakl, chizma">figure</span> covers sixty-four. A square of sixty-four
square paces has a side of eight paces. Take away the five-pace strip,
and the field's side is three.</p>

<p>Nothing about that argument needs a symbol, and nothing about it has
changed. When a modern pupil adds a number to both sides of an equation
to make a <span class="cn-word" data-tr="toʻliq kvadrat">perfect square</span> appear, they are drawing his
<span class="cn-word" data-tr="burchak">corner</span> — in
<span class="cn-word" data-tr="belgilar, yozuv">notation</span> he never
had, for a reason he would recognise at once.</p>
""",
    "grammar": [
        {"pattern": "of unknown side",
         "meaning": "tomoni nomaʼlum — SAT «unknown» soʻzini shunday ishlatadi.",
         "examples": ["A square of unknown side has an area of 49."]},
        {"pattern": "together with",
         "meaning": "… bilan birgalikda — qoʻshiladigan qismlarni bogʻlaydi.",
         "examples": ["The square, together with two strips, covers 39 square paces."]},
        {"pattern": "covers thirty-nine square paces in all",
         "meaning": "jami 39 kvadrat qadamni egallaydi — «in all» = jami.",
         "examples": ["The two rooms cover 60 square metres in all."]},
    ],
    "questions": [
        {"text": "What did 'completing the square' originally mean?",
         "choices": ["Finishing a written proof",
                     "Filling in the missing corner of a drawing",
                     "Squaring a number twice",
                     "Measuring a field twice over"],
         "answer": 1,
         "explanation": "U chizmadagi yetishmayotgan kichik kvadratni "
                        "toʻldirish edi — soʻzma-soʻz."},
        {"text": "In the worked example, what is the area of the finished larger "
                 "square?",
         "choices": ["39 square paces", "25 square paces",
                     "64 square paces", "14 square paces"],
         "answer": 2,
         "explanation": "39 ga burchakdagi 25 qoʻshiladi: 39 + 25 = 64."},
        {"text": "How is the side of the original field found at the end?",
         "choices": ["By dividing sixty-four by two",
                     "By taking the square root of thirty-nine",
                     "By subtracting the strip's width from the larger square's side",
                     "By measuring the drawing"],
         "answer": 2,
         "explanation": "Katta kvadratning tomoni 8; besh qadamli tasma ayirilsa, "
                        "dala tomoni 3 qoladi."},
    ],
},

]
