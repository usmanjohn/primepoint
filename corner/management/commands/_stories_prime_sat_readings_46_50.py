# -*- coding: utf-8 -*-
"""Prime SAT Readings — 46–50 (SAT-46 … SAT-50 darslariga).

Written with the overrides in corner/management/commands/toc_prime_sat_readings.txt
⛔ MATNDA ALGEBRAIK BELGI YOʻQ — miqdorlar faqat ingliz tilida, soʻz bilan.

Til: matn, sarlavha va savollar INGLIZCHA; summary, cn-word glosslari,
     "Exam English" izohlari va javob tushuntirishlari OʻZBEKCHA.

Ovozlar (10-batch erkakdan boshlanadi): 46 Guy · 47 Jenny · 48 Guy ·
                                        49 Jenny · 50 Guy

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_46_50.py --author=prime
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

    # ── 46 · a museum archive ────────────────────────────────────────
    {
        "title": "The Passbook in the Drawer",
        "order": 46,
        "summary": (
            "Yuz yil oldin qoʻyilgan kichik summa: birinchi oʻn yilda deyarli "
            "hech narsa, oxirida esa kutilmagan raqam."
        ),
        "body": """
<p>The <span class="cn-word" data-tr="muzey xodimi">curator</span> was cataloguing a box of
papers left to the museum by a family who had run a mill, and near the bottom she found a
<span class="cn-word" data-tr="omonat daftarchasi">passbook</span>. It had been opened for a
child, with a hundred units of the old currency, and the account had earned five percent a year
ever since. Nobody had touched it.</p>

<p>She was curious, so she worked out what it had done, decade by decade.</p>

<p>The first ten years were <span class="cn-word" data-tr="hafsalani pir qiladigan">disappointing</span>.
The hundred had become a hundred and sixty-two — not yet two hundred, after a whole
<span class="cn-word" data-tr="oʻn yillik">decade</span>. Anyone watching would have concluded
that this was a slow and rather <span class="cn-word" data-tr="ahamiyatsiz">pointless</span>
arrangement.</p>

<p>By the fiftieth year it had passed a thousand. That is ten times the original, and it had
taken half a century to get there.</p>

<p>By the hundredth year it was over thirteen thousand. The curator checked her arithmetic
twice, because the number looked like a <span class="cn-word" data-tr="xato">mistake</span>
beside the modest figure written on the first page.</p>

<p>The <span class="cn-word" data-tr="yarmi">second half</span> of the century had added more
than a hundred times what the first decade added, and the
<span class="cn-word" data-tr="foiz stavkasi">rate</span> had never changed. What changed was the
amount the five percent was <span class="cn-word" data-tr="olinadigan">taken from</span>. Five
percent of a hundred is five. Five percent of twelve thousand is six hundred — the same rule, a hundred
and twenty times the <span class="cn-word" data-tr="natija">result</span>.</p>

<p>The curator put a small <span class="cn-word" data-tr="yorliq">label</span> beside the
passbook in the display case. It reads: <em>this account was
<span class="cn-word" data-tr="eʼtiborsiz qoldirilgan">ignored</span> for a hundred years, and
that is exactly why it is here.</em></p>
""",
        "grammar": [
            {"pattern": "decade by decade",
             "meaning": "oʻn yillik boʻyicha — davrma-davr kuzatish"},
            {"pattern": "the rate had never changed",
             "meaning": "stavka oʻzgarmagan — oʻzgargani asos summa"},
            {"pattern": "taken from",
             "meaning": "… dan olinadi — murakkab foizning oʻzagi"},
        ],
        "questions": [
            {"text": "What had the hundred become after ten years?",
             "choices": ["A thousand", "Two hundred", "A hundred and sixty-two",
                         "Thirteen thousand"],
             "answer": 2,
             "explanation": "Matn buni aytadi — hali ikki yuzga ham yetmagan, "
                            "shuning uchun birinchi oʻn yil hafsalani pir qilgan."},
            {"text": "Why did the second half of the century add so much more?",
             "choices": ["The rate was increased",
                         "The family added money",
                         "The five percent was being taken from a much larger amount",
                         "The currency changed"],
             "answer": 2,
             "explanation": "Stavka oʻzgarmagan; oʻzgargani — foiz olinadigan "
                            "summa, va u yildan yilga oʻsib borgan."},
            {"text": "Why did the curator put the passbook on display?",
             "choices": ["Because it was ignored for a hundred years",
                         "Because the mill was famous",
                         "Because the currency is rare",
                         "Because the child had signed it"],
             "answer": 0,
             "explanation": "Yorliqda aynan shu yozilgan: unga tegilmagani "
                            "uchun u shu yerda."},
        ],
    },

    # ── 47 · everyday technology ─────────────────────────────────────
    {
        "title": "What the Machine Will Not Accept",
        "order": 47,
        "summary": (
            "Chipta avtomati raqam qabul qiladi va narx qaytaradi — lekin har "
            "qanday raqamni emas. Rad etilganlar roʻyxati ham maʼlumot."
        ),
        "body": """
<p>The ticket machine at the bus station does one thing. You
<span class="cn-word" data-tr="kiritmoq">enter</span> how many passengers are travelling, and it
gives you a price. Five thousand som for the
<span class="cn-word" data-tr="band qilish haqi">booking</span>, and twelve thousand for each
seat.</p>

<p>Three passengers, then, cost forty-one thousand. The machine works this out in the time it
takes the <span class="cn-word" data-tr="ekran">screen</span> to change.</p>

<p>But watch what it <span class="cn-word" data-tr="rad etadi">refuses</span>. Type nothing and
press the green button, and it waits. Type a
<span class="cn-word" data-tr="nuqta, kasr belgisi">decimal point</span> and it will not let you
— there is no such thing as half a passenger. Try to enter a
<span class="cn-word" data-tr="manfiy">negative</span> number and the keypad has no way to do it.
Type seven and it tells you that the maximum
<span class="cn-word" data-tr="guruh">group</span> booking at this machine is six.</p>

<p>So the machine accepts the <span class="cn-word" data-tr="butun son">whole numbers</span> from
one to six, and nothing else. That short list is not a
<span class="cn-word" data-tr="cheklov, kamchilik">limitation</span> the engineers forgot to
remove. It is a description of what the question means. A price for two and a half passengers
would be an <span class="cn-word" data-tr="javob">answer</span> to a question nobody asked.</p>

<p>The <span class="cn-word" data-tr="muhandis">engineer</span> who wrote the software had to
decide each of those refusals deliberately. None of them came from the arithmetic; the
arithmetic would happily multiply twelve thousand by minus two. They came from the
<span class="cn-word" data-tr="vaziyat, sharoit">situation</span> the machine sits in.</p>

<p>The prices it can give are just as <span class="cn-word" data-tr="qatʼiy, aniq">fixed</span>:
seventeen, twenty-nine, forty-one, fifty-three, sixty-five and seventy-seven thousand. Six
possible inputs, six possible <span class="cn-word" data-tr="natijalar">outputs</span>, and
nothing in between will ever appear on that screen.</p>
""",
        "grammar": [
            {"pattern": "what the machine will not accept",
             "meaning": "mashina qabul qilmaydigan narsa — aniqlanish sohasi"},
            {"pattern": "six possible inputs, six possible outputs",
             "meaning": "olti kirish, olti chiqish — soha va qiymatlar sohasi"},
            {"pattern": "an answer to a question nobody asked",
             "meaning": "hech kim bermagan savolga javob — kontekstsiz qiymat"},
        ],
        "questions": [
            {"text": "What does the machine charge for three passengers?",
             "choices": ["Thirty-six thousand", "Forty-one thousand",
                         "Seventeen thousand", "Twelve thousand"],
             "answer": 1,
             "explanation": "Besh ming band qilish haqi va uch oʻrindiq uchun "
                            "oʻttiz olti ming — jami qirq bir ming."},
            {"text": "Why does the machine refuse a decimal point?",
             "choices": ["The keypad is broken",
                         "There is no such thing as half a passenger",
                         "Prices must be whole numbers",
                         "It would be too expensive"],
             "answer": 1,
             "explanation": "Cheklov texnik emas, maʼnoviy: yarim yoʻlovchi "
                            "mavjud emas."},
            {"text": "How many different prices can the screen ever show?",
             "choices": ["Six", "Twelve", "An unlimited number", "Three"],
             "answer": 0,
             "explanation": "Olti kirish qabul qilinadi, va har biriga bitta narx "
                            "toʻgʻri keladi."},
        ],
    },

    # ── 48 · transport administration ────────────────────────────────
    {
        "title": "Ten Minutes Later, Every Day",
        "order": 48,
        "summary": (
            "Butun jadval oʻn daqiqaga surildi — shakl oʻzgarmadi, faqat vaqt "
            "koʻchdi. Odamlar sezgan narsa esa boshqa edi."
        ),
        "body": """
<p>The bus company made one change to the winter
<span class="cn-word" data-tr="jadval">timetable</span>. Every departure from the central
station would leave ten minutes later than before. Nothing else was
<span class="cn-word" data-tr="oʻzgartirilgan">altered</span>: the same number of buses, the same
<span class="cn-word" data-tr="oraliq">gaps</span> between them, the same routes.</p>

<p>On paper it was the simplest change the <span class="cn-word"
data-tr="rejalashtiruvchi">planner</span> had ever made. She did not redraw the timetable. She
took the old one and added ten minutes to every line.</p>

<p>The <span class="cn-word" data-tr="shakl">shape</span> of the service was untouched. If two
buses had been twenty minutes apart in the old timetable, they were twenty minutes apart in the
new one. The <span class="cn-word" data-tr="tirbandlik, gavjum payt">busy period</span> still
lasted the same two hours; it simply began ten minutes later and
<span class="cn-word" data-tr="tugadi">ended</span> ten minutes later.</p>

<p>What surprised her was the <span class="cn-word" data-tr="shikoyatlar">complaints</span>. They
did not come from people who had lost a bus. They came from people at one particular
<span class="cn-word" data-tr="bekat">stop</span>, where the new departure time now fell just
after the school bell instead of just before it.</p>

<p>The <span class="cn-word" data-tr="siljish">shift</span> was the same everywhere. Its
<span class="cn-word" data-tr="oqibat">effect</span> was not. A change that moves everything by
the same amount can still land differently, because the world outside the timetable did not
move with it.</p>

<p>She checked the other forty stops before she decided anything, and none of them had the
same problem. The <span class="cn-word" data-tr="tuzatish">fix</span> had to be as narrow as
the fault.</p>

<p>She kept the ten minutes, and moved that one departure back to where it had been. It was the
only line on the page that no longer <span class="cn-word"
data-tr="mos keladi">matched</span> the rest.</p>
""",
        "grammar": [
            {"pattern": "ten minutes later than before",
             "meaning": "avvalgidan oʻn daqiqa kechroq — gorizontal siljish"},
            {"pattern": "the shape of the service was untouched",
             "meaning": "xizmatning shakli oʻzgarmadi — siljish shaklni buzmaydi"},
            {"pattern": "the same gaps between them",
             "meaning": "oraliqlar oʻsha-oʻsha — nisbiy masofalar saqlanadi"},
        ],
        "questions": [
            {"text": "What stayed the same after the change?",
             "choices": ["The departure times",
                         "The gaps between buses and the length of the busy period",
                         "The routes were shortened",
                         "The number of buses was reduced"],
             "answer": 1,
             "explanation": "Hamma narsa bir xil miqdorga surilgani uchun ular "
                            "orasidagi oraliqlar oʻzgarmagan."},
            {"text": "Where did the complaints come from?",
             "choices": ["From people who had lost a bus",
                         "From the drivers",
                         "From one stop where the new time fell just after the school bell",
                         "From people at the central station"],
             "answer": 2,
             "explanation": "Siljish hamma joyda bir xil edi, lekin bitta bekatda "
                            "u maktab qoʻngʻirogʻining narigi tomoniga tushib "
                            "qolgan."},
            {"text": "What is the planner's lesson?",
             "choices": ["A uniform shift can still land differently in different places",
                         "Timetables should never change",
                         "Ten minutes is too long",
                         "The busy period should be shortened"],
             "answer": 0,
             "explanation": "Siljish bir xil, lekin tashqi dunyo u bilan birga "
                            "surilmagani uchun natija har joyda boshqacha."},
        ],
    },

    # ── 49 · construction ────────────────────────────────────────────
    {
        "title": "One, Two, Three",
        "order": 49,
        "summary": (
            "Beton aralashmasi nisbat bilan beriladi, chelak bilan emas — "
            "shuning uchun u har qanday hajmga koʻchadi."
        ),
        "body": """
<p>The <span class="cn-word" data-tr="usta">foreman</span> gave the new boy one instruction
before leaving him with the <span class="cn-word" data-tr="beton aralashtirgich">mixer</span>:
one, two, three. One part <span class="cn-word" data-tr="sement">cement</span>, two parts
<span class="cn-word" data-tr="qum">sand</span>, three parts
<span class="cn-word" data-tr="shagʻal">gravel</span>.</p>

<p>The boy asked how many <span class="cn-word" data-tr="chelak">buckets</span> that was. The
foreman said that was the wrong question, and that this was why the
<span class="cn-word" data-tr="retsept, qoida">recipe</span> was given as a ratio and not as a
number of buckets.</p>

<p>Six parts make a <span class="cn-word" data-tr="to'liq, butun">complete</span> mix. If the job
needs thirty buckets, one part is five buckets: five of cement, ten of sand, fifteen of gravel.
If it needs twelve, one part is two. If it needs a lorry-load, the same three numbers still
describe it. The ratio does not say how much
<span class="cn-word" data-tr="beton">concrete</span> to make. It says what concrete
<span class="cn-word" data-tr="… dan iborat">is</span>.</p>

<p>The boy asked what happens on a big pour, where nobody counts buckets at all. The foreman
said the <span class="cn-word" data-tr="tarozi">scales</span> on the plant do the same sum in
kilograms, and the three numbers do not change.</p>

<p>Then he explained what happens when the ratio is wrong, because that is the part apprentices
remember. Too little cement and the mix will not
<span class="cn-word" data-tr="qotmoq">set</span> properly; it looks finished and
<span class="cn-word" data-tr="qulamoq, sinmoq">crumbles</span> under load a year later. Too much
cement and it sets hard, then cracks as it dries, because there is not enough sand and gravel
holding it together.</p>

<p>"Nobody will ever be able to see the ratio in the finished wall," he said. "That is why you
have to get it right while it is still in the
<span class="cn-word" data-tr="chelak, idish">bucket</span>."</p>
""",
        "grammar": [
            {"pattern": "one part cement, two parts sand",
             "meaning": "bir qism sement, ikki qism qum — nisbat qismlarni sanaydi"},
            {"pattern": "six parts make a complete mix",
             "meaning": "olti qism butun aralashmani beradi — jami qismlar soni"},
            {"pattern": "it says what concrete is, not how much to make",
             "meaning": "nisbat miqdorni emas, tarkibni belgilaydi"},
        ],
        "questions": [
            {"text": "For a job needing thirty buckets, how much sand is used?",
             "choices": ["Five buckets", "Ten buckets", "Fifteen buckets", "Two buckets"],
             "answer": 1,
             "explanation": "Olti qism, har biri besh chelak; qum ikki qism — "
                            "demak oʻn chelak."},
            {"text": "Why is the recipe given as a ratio rather than a number of buckets?",
             "choices": ["Because buckets vary in size",
                         "Because the foreman could not count",
                         "So that it describes any quantity of concrete",
                         "Because cement is sold by weight"],
             "answer": 2,
             "explanation": "Nisbat har qanday hajmga koʻchadi — oʻn ikki "
                            "chelakka ham, yuk mashinasiga ham."},
            {"text": "What happens if there is too much cement?",
             "choices": ["It sets hard and then cracks as it dries",
                         "It never sets at all",
                         "It becomes cheaper",
                         "It sets faster and is stronger"],
             "answer": 0,
             "explanation": "Qum va shagʻal yetarli boʻlmagani uchun qotgan beton "
                            "quriyotganda yorilib ketadi."},
        ],
    },

    # ── 50 · space engineering history ───────────────────────────────
    {
        "title": "The Orbiter That Came In Too Low",
        "order": 50,
        "summary": (
            "1999-yilda Marsga yuborilgan kemani yoʻqotgan sabab hisob xatosi "
            "emas edi — ikki jamoa ikki xil birlikda ishlagan."
        ),
        "body": """
<p>In September 1999 a <span class="cn-word" data-tr="kosmik kema">spacecraft</span> called the
Mars Climate Orbiter reached Mars after a journey of nine months, went behind the planet as
planned, and was never <span class="cn-word" data-tr="eshitilmadi">heard from</span> again.</p>

<p>The <span class="cn-word" data-tr="tekshiruv">investigation</span> that followed did not find
a broken part or a bad line of arithmetic. It found two teams, both careful, both correct within
their own <span class="cn-word" data-tr="tizim">system</span>.</p>

<p>One team's software reported the small <span class="cn-word" data-tr="turtki, kuch">pushes</span>
used to steer the craft in <span class="cn-word" data-tr="imperial birliklar">imperial</span>
units. The other team's software read those same numbers as if they were in
<span class="cn-word" data-tr="metrik">metric</span> units. Neither figure was wrong. They simply
did not mean the same thing, and nothing in the numbers themselves said so.</p>

<p>The <span class="cn-word" data-tr="farq">discrepancy</span> was small on any single
correction, and it built up across the whole journey. When the orbiter arrived it was on a path
far lower into the atmosphere than intended, and at that
<span class="cn-word" data-tr="balandlik">altitude</span> it could not survive.</p>

<p>What makes the case worth telling is how <span class="cn-word" data-tr="oddiy">ordinary</span>
the failure was. No single person did anything wrong.</p>

<p>The board's <span class="cn-word" data-tr="tavsiya">recommendation</span> was not that
engineers should be more careful with their sums. It was that units must
<span class="cn-word" data-tr="hamroh boʻlmoq">travel with</span> the numbers, at every
<span class="cn-word" data-tr="chegara, oʻtish joyi">boundary</span> between one piece of
software and the next.</p>

<p>Which is the same rule a pupil is given for a two-line conversion question: write the unit
beside the number, every time, and check that what is
<span class="cn-word" data-tr="qolgan">left</span> at the end is the unit you were actually
asked for.</p>
""",
        "grammar": [
            {"pattern": "both correct within their own system",
             "meaning": "har biri oʻz tizimida toʻgʻri — xato birlikda edi"},
            {"pattern": "units must travel with the numbers",
             "meaning": "birliklar son bilan birga yurishi kerak"},
            {"pattern": "the unit you were actually asked for",
             "meaning": "sizdan soʻralgan birlik — yakuniy tekshiruv"},
        ],
        "questions": [
            {"text": "What did the investigation find?",
             "choices": ["A broken part on the spacecraft",
                         "An arithmetic mistake",
                         "Two teams using two different systems of units",
                         "A navigation error made on the final day"],
             "answer": 2,
             "explanation": "Hech kim hisobda adashmagan — ikki jamoa bir xil "
                            "sonlarni ikki xil birlikda tushungan."},
            {"text": "Why was the problem not noticed earlier?",
             "choices": ["The difference was small on any single correction",
                         "Nobody checked the software",
                         "The journey was too short",
                         "The teams never spoke to each other"],
             "answer": 0,
             "explanation": "Har bir tuzatishda farq kichik edi va u butun "
                            "sayohat davomida toʻplanib bordi."},
            {"text": "What was the board's actual recommendation?",
             "choices": ["That units must travel with the numbers at every boundary",
                         "That engineers should double-check their arithmetic",
                         "That only metric units should exist",
                         "That the mission should be repeated"],
             "answer": 0,
             "explanation": "Tavsiya ehtiyotkorlik haqida emas edi: birlik son "
                            "bilan birga, har bir oʻtish joyida yozilishi kerak."},
        ],
    },
]
