# -*- coding: utf-8 -*-
"""Prime SAT Readings — SAT-11 … SAT-15 (batch 3).

  11 — a survey note on two canals      (SAT-11: same gradient, never meeting)
  12 — a carpenter's guide              (SAT-12: the right angle you can measure)
  13 — a school's attendance rule       (SAT-13: at least, as a rule people live by)
  14 — a national park's camping notice (SAT-14: a permitted region, in words)
  15 — a coach driver's loading sheet   (SAT-15: what is left after the weight is taken)

Genre rotation — used already: cafe order sheet, lab report, committee minutes,
quality-control report, news item, museum notice, pool notice, radio running order,
coach's training log, newspaper Q&A. None of those repeat here.

⛔ NO ALGEBRAIC NOTATION IN THE BODY — quantities in English, units spelled out.
NARRATOR VOICE (batch 2 ran 3 male / 2 female, so this one flips back):
    11 en-US-JennyNeural · 12 en-US-GuyNeural · 13 en-US-JennyNeural
    14 en-US-GuyNeural   · 15 en-US-JennyNeural

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_11_15.py --author=prime
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

    # ══════════════════════════════════════════════════════════════════
    # SAT-11 — parallel                                        [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Two Canals, One Fall",
        "summary": (
            "SAT-11 matni. Ikki ariq bir xil nishablik bilan qazilgan — shuning uchun "
            "ular yonma-yon boradi va hech qachon uchrashmaydi."
        ),
        "order":   11,
        "grammar": [
            {
                "pattern":  "falls one metre in every four hundred",
                "meaning":  "Har toʻrt yuz metrga bir metr pasayadi — nishablikning "
                            "soʻz bilan aytilishi. Ikki ariqda bu nisbat bir xil "
                            "boʻlsa, ular <b>parallel</b>.",
                "examples": ["Each canal falls one metre in every four hundred."],
            },
            {
                "pattern":  "run side by side",
                "meaning":  "Yonma-yon boradi. Parallel chiziqlarning kundalik tildagi "
                            "tavsifi: oralaridagi masofa oʻzgarmaydi.",
                "examples": ["The two channels run side by side for three kilometres."],
            },
            {
                "pattern":  "the same gradient",
                "meaning":  "Bir xil nishablik (qiyalik). Uzunliklari har xil boʻlishi "
                            "mumkin — muhimi <b>nisbat</b>.",
                "examples": ["Different lengths, but the same gradient."],
            },
        ],
        "body": '''<p>The two irrigation <span class="cn-word" data-tr="ariq, kanal">canals</span> east of the village were dug in different <span class="cn-word" data-tr="oʻn yilliklar">decades</span> by different teams, and on the <span class="cn-word" data-tr="tuproq surati; yon koʻrinish">profile drawing</span> pinned up in the water office they look like one shape copied twice.</p>

<p>The older channel is 2.4 kilometres long and drops six metres from the <span class="cn-word" data-tr="suv olish joyi">intake</span> to the last field. The newer one is 3.2 kilometres long and drops eight. Those look like different numbers until you do the only division that matters: both canals <strong>fall one metre in every four hundred</strong> metres of length.</p>

<p>That is not a <span class="cn-word" data-tr="tasodif">coincidence</span>. Water moving too slowly leaves <span class="cn-word" data-tr="loyqa, choʻkma">silt</span> behind; water moving too fast eats the <span class="cn-word" data-tr="qirgʻoq">bank</span>. The <span class="cn-word" data-tr="suv xoʻjaligi muhandisi">water engineer</span> who set out the second canal in 1994 copied the <span class="cn-word" data-tr="nishablik">gradient</span> of the first exactly, because forty years of use had proved it right.</p>

<p>Because the two channels have <strong>the same gradient</strong>, they <strong>run side by side</strong> and the gap between them never changes. Anyone walking the <span class="cn-word" data-tr="xizmat yoʻli">service path</span> can see it: 90 metres apart at the intake, 90 metres apart at the far end, 90 metres apart everywhere in between.</p>

<p>The office keeps one warning on the wall for new <span class="cn-word" data-tr="oʻlchovchi, geodezist">surveyors</span>. If a proposed branch is drawn at even a slightly different fall, the two lines are no longer parallel — and a channel that slowly <span class="cn-word" data-tr="yaqinlashmoq">converges</span> on its neighbour will, sooner or later, meet it.</p>

<p>On this <span class="cn-word" data-tr="pasttekislik">plain</span> that has happened twice, and both times it flooded the same three fields.</p>''',
        "questions": [
            {
                "text": "What do the two canals have in common?",
                "choices": ["Their length", "Their total drop", "Their gradient"],
                "answer": 2,
                "explanation": "Uzunliklari (2.4 va 3.2 km) ham, umumiy pasayishi "
                               "(6 va 8 metr) ham har xil. Bir xil boʻlgan narsa — "
                               "<b>nisbat</b>: har 400 metrga 1 metr.",
            },
            {
                "text": "How far apart are the two canals at the far end?",
                "choices": ["90 metres", "It depends on the length", "400 metres"],
                "answer": 0,
                "explanation": "Matnda aytilganidek, oraliq hech qayerda oʻzgarmaydi — "
                               "boshida ham, oxirida ham <b>90 metr</b>. Parallel "
                               "chiziqlarning belgisi aynan shu.",
            },
            {
                "text": "Why does the office warn surveyors about a slightly different fall?",
                "choices": [
                    "Because a shallower canal costs more to dig.",
                    "Because lines that are not parallel will eventually meet.",
                    "Because the older canal must always be longer.",
                ],
                "answer": 1,
                "explanation": "Nishabliklar bir xil boʻlmasa, chiziqlar parallel "
                               "boʻlmaydi va sekin-asta yaqinlashib, oxir-oqibat "
                               "kesishadi — matn buni ikki marta sodir boʻlgan deb "
                               "aytadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-12 — perpendicular                                     [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Carpenter's Diagonal",
        "summary": (
            "SAT-12 matni. Duradgor toʻgʻri burchakni transportirsiz tekshiradi: "
            "uch, toʻrt va besh — mingyillik yoshidagi usul."
        ),
        "order":   12,
        "grammar": [
            {
                "pattern":  "at a right angle to",
                "meaning":  "…ga toʻgʻri burchak ostida, yaʼni <b>perpendikulyar</b>. "
                            "Testda «perpendicular» soʻzining oʻrniga tez-tez "
                            "ishlatiladi.",
                "examples": ["The second wall must be at a right angle to the first."],
            },
            {
                "pattern":  "out of square",
                "meaning":  "Toʻgʻri burchakdan chetlangan. Duradgorlar tilida "
                            "«burchak toʻgʻri emas» degani.",
                "examples": ["If the diagonal is longer, the corner is out of square."],
            },
            {
                "pattern":  "check, then cut",
                "meaning":  "Avval tekshir, keyin kes. Matematikada ham: javobni "
                            "olishdan oldin tekshiruvni bajarish — bu kursning "
                            "doimiy odati.",
                "examples": ["The rule in the workshop is simple: check, then cut."],
            },
        ],
        "body": '''<p>There is a <span class="cn-word" data-tr="ustaxona">workshop</span> in the old part of town where the owner has never owned a <span class="cn-word" data-tr="burchak oʻlchagich">protractor</span>, and every corner he has made in thirty years is true.</p>

<p>His method is older than his tools. When a new <span class="cn-word" data-tr="rom, gardish">frame</span> has to sit <strong>at a right angle to</strong> the wall, he measures three metres along one edge and marks it. He measures four metres along the other edge and marks that. Then he measures the <span class="cn-word" data-tr="diagonal, qiyalik">diagonal</span> between the two marks.</p>

<p>If that diagonal is exactly five metres, the corner is <span class="cn-word" data-tr="toʻgʻri, aniq">true</span>. If it comes out at 5.2 metres, the corner is open — <strong>out of square</strong> — and the frame will rock for the rest of its life. If it comes out short, at 4.8, the corner is too tight and the door will <span class="cn-word" data-tr="ishqalanmoq">bind</span> every winter.</p>

<p>Three, four, five is the smallest set of whole numbers that does this, and it works at any <span class="cn-word" data-tr="masshtab, oʻlcham">scale</span>: 30 centimetres and 40 centimetres give a 50-centimetre diagonal; six metres and eight give ten. The <span class="cn-word" data-tr="shogird">apprentice</span> is taught to use the biggest triangle the room allows, because a small error in a short measurement becomes a large error across a long wall.</p>

<p>Two things are worth noticing. The carpenter never measures the <span class="cn-word" data-tr="burchak">angle</span> itself — he measures three lengths and lets them <span class="cn-word" data-tr="isbotlamoq">prove</span> the angle. And he does it before the <span class="cn-word" data-tr="mixlar">nails</span> go in, not after.</p>

<p>The sign above his <span class="cn-word" data-tr="ish stoli">bench</span> says only this: <span class="cn-word" data-tr="avval tekshir, keyin kes">Check, then cut.</span></p>''',
        "questions": [
            {
                "text": "What does the carpenter actually measure to test a right angle?",
                "choices": ["The angle itself", "Three lengths", "The width of the door"],
                "answer": 1,
                "explanation": "U burchakni <b>oʻlchamaydi</b> — uchta uzunlikni "
                               "oʻlchaydi (3 metr, 4 metr va diagonal) va ular burchakni "
                               "isbotlaydi.",
            },
            {
                "text": "If the two edges are 30 centimetres and 40 centimetres, what should the diagonal be?",
                "choices": ["35 centimetres", "45 centimetres", "50 centimetres"],
                "answer": 2,
                "explanation": "Nisbat oʻzgarmaydi: 3–4–5 → 30–40–<b>50</b>. Usul "
                               "istalgan masshtabda ishlaydi, faqat uchala son ham "
                               "bir xil koʻpaytuvchiga koʻpaytiriladi.",
            },
            {
                "text": "Why does the apprentice use the biggest triangle the room allows?",
                "choices": [
                    "Because a small measuring error matters less over a long distance.",
                    "Because the diagonal is easier to reach.",
                    "Because short walls cannot have right angles.",
                ],
                "answer": 0,
                "explanation": "Matnda aytilgan: qisqa oʻlchovdagi kichik xato uzun devor "
                               "boʻylab katta xatoga aylanadi. Katta uchburchak "
                               "aniqlikni oshiradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-13 — inequalities                                    [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Eighty-Five Percent",
        "summary": (
            "SAT-13 matni. Maktabning davomat qoidasi «kamida» degan soʻz ustiga "
            "qurilgan — va oʻsha bitta soʻz nechta darsni oʻtkazib yuborish "
            "mumkinligini hal qiladi."
        ),
        "order":   13,
        "grammar": [
            {
                "pattern":  "at least",
                "meaning":  "Kamida. Chegaraning <b>oʻzi ham</b> qabul qilinadi — "
                            "roppa-rosa 85 foiz yetarli.",
                "examples": ["Pupils must attend at least 85 percent of lessons."],
            },
            {
                "pattern":  "no more than",
                "meaning":  "Koʻpi bilan. Yuqori chegara, va u ham qoidaning "
                            "<b>ichida</b>.",
                "examples": ["That means missing no more than eighteen lessons."],
            },
            {
                "pattern":  "the same rule, read from the other end",
                "meaning":  "Bitta qoidani ikki tomondan oʻqish: «kamida qatnashish» "
                            "va «koʻpi bilan qoldirish» — bir xil chegara.",
                "examples": ["Attend at least 102, or miss no more than 18."],
            },
        ],
        "body": '''<p>The <span class="cn-word" data-tr="qoidalar toʻplami">rulebook</span> at School 24 gives one page to <span class="cn-word" data-tr="davomat">attendance</span>, and the whole page turns on two words.</p>

<p>«To sit the end-of-year <span class="cn-word" data-tr="imtihon">examination</span>, a pupil must attend <strong>at least</strong> 85 percent of the year's lessons.» There are 120 lessons in the year, so the rule asks for 102 of them. A pupil who attends exactly 102 has met it — <em>at least</em> includes the number itself, and the <span class="cn-word" data-tr="ish yurituvchi, kotib">registrar</span> is careful to say so when parents telephone.</p>

<p>Read from the other end, the same rule says something friendlier: a pupil may miss <strong>no more than</strong> 18 lessons. Both sentences draw the same line in the same place; one counts what you have, the other counts what you have spent.</p>

<p>Two cases from last year show how <span class="cn-word" data-tr="tor">narrow</span> that line is. A pupil who missed 15 lessons attended 105, comfortably above the <span class="cn-word" data-tr="chegara">threshold</span>, and sat the paper. A pupil who missed 19 attended 101 — one lesson short — and did not. She <span class="cn-word" data-tr="shikoyat qildi">appealed</span>, and the appeal was <span class="cn-word" data-tr="rad etilgan">refused</span>, because a rule that <span class="cn-word" data-tr="bukilmoq, egilmoq">bends</span> for one lesson has no edge at all.</p>

<p>The registrar's <span class="cn-word" data-tr="maslahat">advice</span> to every new class is not about mathematics. Do not aim for the <span class="cn-word" data-tr="chegara chizigʻi">boundary</span>, he says. Aim well inside it, because <span class="cn-word" data-tr="gripp">flu</span> does not consult the rulebook, and neither does a delayed bus.</p>''',
        "questions": [
            {
                "text": "How many of the 120 lessons must a pupil attend?",
                "choices": ["85", "102", "105"],
                "answer": 1,
                "explanation": "120 ning 85 foizi: 120 × 0.85 = <b>102</b>. "
                               "<b>85</b> — foiz, darslar soni emas; <b>105</b> — "
                               "matndagi bir oʻquvchining natijasi.",
            },
            {
                "text": "A pupil has missed 19 lessons. May they sit the examination?",
                "choices": [
                    "Yes — 19 is fewer than 20.",
                    "Yes — they attended 101, which rounds to 102.",
                    "No — they attended 101, one short of the threshold.",
                ],
                "answer": 2,
                "explanation": "120 − 19 = 101, va qoida kamida 102 ni talab qiladi. "
                               "Bir dars yetmadi — chegara masalasida yaxlitlash "
                               "yoʻq.",
            },
            {
                "text": "Why does the registrar say the two sentences draw the same line?",
                "choices": [
                    "Because attending at least 102 and missing no more than 18 are the same limit.",
                    "Because 85 percent is close to 100 percent.",
                    "Because both sentences use the word «percent».",
                ],
                "answer": 0,
                "explanation": "102 ta qatnashish va 18 tadan koʻp qoldirmaslik — bitta "
                               "chegaraning ikki xil aytilishi (102 + 18 = 120). Biri "
                               "borini sanaydi, ikkinchisi sarflanganini.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-14 — a permitted region                                [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Where You May Camp",
        "summary": (
            "SAT-14 matni. Milliy bogʻning eʼloni ikkita shartni qoʻyadi — va "
            "xaritadagi ruxsat etilgan soha aynan shu ikki shartning kesishmasi."
        ),
        "order":   14,
        "grammar": [
            {
                "pattern":  "at least fifty metres from",
                "meaning":  "…dan kamida ellik metr narida. Bu <b>pastki</b> chegara: "
                            "yaqinroq boʻlish mumkin emas.",
                "examples": ["Pitch at least fifty metres from the water."],
            },
            {
                "pattern":  "within three hundred metres of",
                "meaning":  "…dan uch yuz metr ichida. Bu <b>yuqori</b> chegara: "
                            "uzoqroq ketish mumkin emas.",
                "examples": ["Stay within three hundred metres of a marked path."],
            },
            {
                "pattern":  "both conditions must hold",
                "meaning":  "Ikkala shart ham bajarilishi kerak. Ruxsat etilgan soha — "
                            "ikki shartning <b>umumiy</b> qismi.",
                "examples": ["A site is legal only if both conditions hold."],
            },
        ],
        "body": '''<p>The <span class="cn-word" data-tr="eʼlon">notice</span> at the entrance to the national park is a small masterpiece of plain writing, and it fits on one board.</p>

<p>«You may camp only where <strong>both conditions</strong> below <span class="cn-word" data-tr="amal qilmoq">hold</span>. <span class="cn-word" data-tr="chodir tiking">Pitch your tent</span> <strong>at least fifty metres from</strong> the lake, and stay <strong>within three hundred metres of</strong> a marked path.»</p>

<p>The first rule protects the water. Tents pitched at the <span class="cn-word" data-tr="suv chekkasi">water's edge</span> wear away the bank and frighten the birds that <span class="cn-word" data-tr="uya qurmoq">nest</span> in the <span class="cn-word" data-tr="qamish">reeds</span>. The second rule protects the campers: a <span class="cn-word" data-tr="qutqaruv guruhi">rescue team</span> looking for someone in <span class="cn-word" data-tr="tuman">fog</span> can search a strip beside a path far faster than a whole valley.</p>

<p>Together they carve out a <span class="cn-word" data-tr="tasma, yoʻlak">band</span> of ground — not too close to the lake, not too far from the path — and the <span class="cn-word" data-tr="qoʻriqchi, boshqaruvchi">warden</span>'s map has it shaded in green.</p>

<p>Last August she turned away two groups on the same evening. The first had pitched 45 metres from the shore: a beautiful spot, and 5 metres inside the <span class="cn-word" data-tr="taqiq">prohibition</span>. The second was 65 metres from the water, which was fine, but 380 metres from the nearest path, which was not. Each group had obeyed one rule and broken the other.</p>

<p>A site 65 metres from the lake and 240 metres from a path breaks neither, and that is the whole test. The green ground on the map is not a <span class="cn-word" data-tr="taklif, tavsiya">suggestion</span> — it is simply every point where both sentences are true at once.</p>''',
        "questions": [
            {
                "text": "A tent is pitched 45 metres from the lake and 200 metres from a path. Is the site allowed?",
                "choices": [
                    "Yes — it is close to a path.",
                    "No — it is too close to the lake.",
                    "No — it is too far from the path.",
                ],
                "answer": 1,
                "explanation": "Yoʻlga nisbatan shart bajarilgan (200 &lt; 300), lekin "
                               "koʻlgacha kamida 50 metr kerak edi. <b>Ikkala</b> shart "
                               "ham bajarilishi shart.",
            },
            {
                "text": "Which of these sites satisfies both conditions?",
                "choices": [
                    "65 metres from the lake, 380 metres from a path",
                    "65 metres from the lake, 240 metres from a path",
                    "45 metres from the lake, 240 metres from a path",
                ],
                "answer": 1,
                "explanation": "65 ≥ 50 ✓ va 240 ≤ 300 ✓. Birinchisi yoʻldan juda uzoq "
                               "(380), uchinchisi koʻlga juda yaqin (45).",
            },
            {
                "text": "What does the green area on the warden's map show?",
                "choices": [
                    "Every point where both rules are true at the same time.",
                    "The places with the best view of the lake.",
                    "The area the rescue team has already searched.",
                ],
                "answer": 0,
                "explanation": "Matnning oxirgi jumlasi: yashil yer — ikkala jumla bir "
                               "vaqtda rost boʻlgan <b>har bir nuqta</b>. Bu tengsizlik "
                               "grafigidagi shtrixlangan sohaning oʻzi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-15 — modelling with a limit                          [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Nine Boxes and a Coach",
        "summary": (
            "SAT-15 matni. Haydovchi yuk bagajining chegarasini biladi va qolgan "
            "joyni sanaydi — javob esa har doim butun songa yaxlitlanadi."
        ),
        "order":   15,
        "grammar": [
            {
                "pattern":  "a maximum load of",
                "meaning":  "Eng koʻp yuk. Bu <b>≤</b> chegara: undan oshib boʻlmaydi, "
                            "lekin unga yetish mumkin.",
                "examples": ["The hold has a maximum load of 900 kilograms."],
            },
            {
                "pattern":  "that leaves",
                "meaning":  "Shuncha qoladi. Chegaradan band boʻlgan qismni ayirgach, "
                            "qolgan joy — javobning asosi.",
                "examples": ["That leaves 180 kilograms for equipment."],
            },
            {
                "pattern":  "you cannot load part of a box",
                "meaning":  "Qutini boʻlaklab yuklab boʻlmaydi — shuning uchun javob "
                            "butun son, va u <b>pastga</b> yaxlitlanadi.",
                "examples": ["Nine and a half boxes is not an answer."],
            },
        ],
        "body": '''<p>Before a school trip leaves, the coach driver does a piece of <span class="cn-word" data-tr="hisob-kitob">arithmetic</span> on a <span class="cn-word" data-tr="qisqichli planshet">clipboard</span>, and he does it in the same order every time.</p>

<p>The luggage <span class="cn-word" data-tr="bagaj boʻlimi">hold</span> under the floor has <strong>a maximum load of</strong> 900 kilograms. That figure is not the driver's opinion; it is on a <span class="cn-word" data-tr="yorliq, taxtacha">plate</span> beside the door, and an <span class="cn-word" data-tr="oʻta yuklangan">overloaded</span> coach handles badly on a mountain road, brakes late and fails its <span class="cn-word" data-tr="tekshiruv">inspection</span>.</p>

<p>Forty-eight pupils are travelling, and each has been told to bring one bag of 15 kilograms. Forty-eight bags at fifteen kilograms is 720 kilograms — the largest single number on his sheet. <strong>That leaves</strong> 180 kilograms of the limit unused.</p>

<p>Then come the <span class="cn-word" data-tr="jihoz, anjom">equipment</span> boxes: tents, cooking gear, a first-aid <span class="cn-word" data-tr="quti, sandiq">chest</span>, all packed to a standard 20 kilograms each. Divide 180 by 20 and the answer is nine.</p>

<p>Nine, and not a box more. The driver is <span class="cn-word" data-tr="qatʼiy">firm</span> about this even when a teacher points out that a tenth box would only add twenty kilograms to a nine-hundred-kilogram <span class="cn-word" data-tr="chegara">limit</span>. The plate says 900, the sum says 900, and <span class="cn-word" data-tr="qutini boʻlaklab boʻlmaydi">you cannot load part of a box</span>.</p>

<p>What his clipboard shows, in the end, is the shape of every problem of this kind: a fixed <span class="cn-word" data-tr="chegara">ceiling</span>, one large amount already spent, and a whole number of whatever is left.</p>''',
        "questions": [
            {
                "text": "How many kilograms do the pupils' bags take up?",
                "choices": ["180 kilograms", "720 kilograms", "900 kilograms"],
                "answer": 1,
                "explanation": "48 × 15 = <b>720</b> kg. <b>180</b> — qolgan joy, "
                               "<b>900</b> — bagajning umumiy chegarasi.",
            },
            {
                "text": "How many equipment boxes can the coach carry?",
                "choices": ["9", "10", "12"],
                "answer": 0,
                "explanation": "900 − 720 = 180 kg qoladi, va 180 ÷ 20 = <b>9</b> ta "
                               "quti. Oʻninchi quti chegaradan chiqarib yuboradi "
                               "(920 kg).",
            },
            {
                "text": "Why does the driver refuse a tenth box?",
                "choices": [
                    "Because the boxes would not fit through the door.",
                    "Because a limit that is exceeded by a little is still exceeded.",
                    "Because the pupils' bags might be heavier than stated.",
                ],
                "answer": 1,
                "explanation": "Chegara — chegara: 920 kg 900 dan koʻp. «Ozgina oshdi» "
                               "degan narsa yoʻq, xuddi maktabning davomat qoidasidagi "
                               "bir dars kabi.",
            },
        ],
    },
]
