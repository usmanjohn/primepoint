# -*- coding: utf-8 -*-
"""Prime SAT Readings — 31–35 (SAT-31 … SAT-35 darslariga).

Written with the overrides in corner/management/commands/toc_prime_sat_readings.txt
⛔ MATNDA ALGEBRAIK BELGI YOʻQ — miqdorlar faqat ingliz tilida, soʻz bilan.
   Bu ikki ishni bir vaqtda qiladi: ingliz jumlasini matematikaga oʻgirish
   koʻnikmasini mashq qiladi va matnni TTS oʻqiy oladigan holda saqlaydi.

Til: matn, sarlavha va savollar INGLIZCHA; summary, cn-word glosslari,
     "Exam English" izohlari va javob tushuntirishlari OʻZBEKCHA.

Ovozlar (7-batch ayoldan boshlanadi): 31 Jenny · 32 Guy · 33 Jenny ·
                                      34 Guy · 35 Jenny

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_31_35.py --author=prime
    python manage.py gen_corner_audio --collection="Prime SAT Readings" \\
        --only <n> --voice en-US-JennyNeural        # ⚠️ --voice MAJBURIY
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

    # ── 31 · theatre ─────────────────────────────────────────────────
    {
        "title": "The Stage That Had To Fit",
        "order": 31,
        "summary": (
            "Teatr sahnasi uchun yuzasi va perimetri berilgan toʻrtburchak "
            "izlanadi — yaʼni koʻpaytmasi va yigʻindisi maʼlum ikki son."
        ),
        "body": """
<p>The new play needed a raised <span class="cn-word" data-tr="sahna, platforma">platform</span>
in the middle of the stage. The <span class="cn-word" data-tr="rejissyor">director</span> gave
the <span class="cn-word" data-tr="duradgor">carpenter</span> two numbers and nothing else. The platform had to <span class="cn-word"
data-tr="qoplamoq">cover</span> forty square metres of floor, because that was how much space
the dancers needed. And it had to have a <span class="cn-word"
data-tr="chekka, hoshiya">border</span> of twenty-six metres of wooden edging, because that was
exactly how much edging was left in the store.</p>

<p>"Give me the length and the width," the carpenter said. The director did not know them. She
only knew the two numbers she had been given.</p>

<p>The carpenter sat down with a pencil. Twenty-six metres of edging went all the way round, so
one length plus one width came to thirteen metres — half of the border. And length times width
came to forty. He needed two numbers that <span class="cn-word" data-tr="qoʻshilmoq">added</span>
to thirteen and <span class="cn-word" data-tr="koʻpaytirilmoq">multiplied</span> to forty.</p>

<p>He wrote the <span class="cn-word" data-tr="juftlik">pairs</span> in order, the way he always
did. One and forty: too far apart. Two and twenty: still too far. Four and ten: their sum was
fourteen, very close. Five and eight: their sum was thirteen. That was it.</p>

<p>He cut the platform five metres by eight metres. When the edging went on, the last piece
<span class="cn-word" data-tr="tugadi, aynan yetdi">ran out</span> at the corner where he had
started, with nothing <span class="cn-word" data-tr="ortiqcha, zaxira">to spare</span>.</p>

<p>The director was <span class="cn-word" data-tr="hayratda qolgan">amazed</span>. The carpenter
was not. "You did not give me a <span class="cn-word" data-tr="jumboq">puzzle</span>," he said.
"You gave me a sum and a product. There is only one <span class="cn-word"
data-tr="juftlik">pair</span> that fits, and it takes four lines to find."</p>
""",
        "grammar": [
            {"pattern": "added to … and multiplied to …",
             "meaning": "yigʻindisi … va koʻpaytmasi … — ajratishning ikki sharti"},
            {"pattern": "half of the border",
             "meaning": "perimetrning yarmi = uzunlik + eni"},
            {"pattern": "too far apart",
             "meaning": "juda uzoq (juftlikning ikki soni bir-biridan)"},
        ],
        "questions": [
            {"text": "Why did the carpenter work with thirteen rather than twenty-six?",
             "choices": ["Because half the border is one length plus one width",
                         "Because thirteen is half of the area",
                         "Because he had only thirteen metres of edging",
                         "Because the stage was thirteen metres wide"],
             "answer": 0,
             "explanation": "Perimetr ikkita uzunlik va ikkita enni oʻz ichiga oladi, "
                            "demak uning yarmi — bitta uzunlik va bitta en."},
            {"text": "Which pair did he try just before he found the answer?",
             "choices": ["Two and twenty", "One and forty", "Four and ten", "Five and eight"],
             "answer": 2,
             "explanation": "U juftliklarni tartib bilan sanadi: 1 va 40, 2 va 20, "
                            "4 va 10 (yigʻindisi 14), keyin 5 va 8."},
            {"text": "What is the carpenter's point at the end?",
             "choices": ["That the director should have measured the stage",
                         "That the answer needed guessing",
                         "That forty is a difficult number",
                         "That a sum and a product together fix the two numbers"],
             "answer": 3,
             "explanation": "Faqat yuza berilsa koʻp javob boʻlardi; yuza va perimetr "
                            "birgalikda yagona juftlikni belgilaydi."},
        ],
    },

    # ── 32 · a workplace anecdote ────────────────────────────────────
    {
        "title": "Sixty and Seventeen",
        "order": 32,
        "summary": (
            "Bir ishchi taxmin qiladi, ikkinchisi juftliklarni tartib bilan yozadi — "
            "AC usulining butun gʻoyasi shu tartibda."
        ),
        "body": """
<p>In the <span class="cn-word" data-tr="ombor">warehouse</span> there was an old
<span class="cn-word" data-tr="oʻyin, koʻngilochar mashgʻulot">game</span> the older workers
played with the new ones. The <span class="cn-word" data-tr="boshliq">supervisor</span> would
call out two numbers, and whoever found the answer first did not have to <span class="cn-word" data-tr="polni supurmoq">sweep the floor</span>.</p>

<p>That morning she called out: "Sixty and seventeen. Two numbers that multiply to sixty and add
to seventeen."</p>

<p>Rustam started <span class="cn-word" data-tr="taxmin qilmoq">guessing</span> at once. Ten and
six? Their sum was sixteen. Twenty and three? Twenty-three. Thirty and two? Far too big. He tried
ten and six again, having <span class="cn-word" data-tr="unutmoq">forgotten</span> he had already
tried it.</p>

<p>Malika did not guess. She wrote a short <span class="cn-word" data-tr="roʻyxat">list</span>,
starting from the smallest. One and sixty. Two and thirty. Three and twenty. Four and fifteen.
Five and twelve. She wrote the sum beside each pair as she went: sixty-one, thirty-two,
twenty-three, nineteen, seventeen.</p>

<p>She stopped at the fifth line and put down the pencil. It had taken her under a minute, and
she had not repeated a single <span class="cn-word" data-tr="urinish">attempt</span>.</p>

<p>The supervisor smiled, because this was the point of the game. "Rustam is faster than Malika,"
she told the room. "But he has no <span class="cn-word" data-tr="tartib, izchillik">order</span>.
He will find the answer <span class="cn-word" data-tr="oxir-oqibat">eventually</span>, and he will never know how close he was, and sometimes he
will try the same pair twice. Malika is slower for the first ten seconds and finished before
him."</p>

<p>Then she added the sentence they all remembered afterwards: "A
<span class="cn-word" data-tr="tizimli, tartibli">systematic</span> search is not clever. It is
just a search you can <span class="cn-word" data-tr="tugatmoq, oxiriga yetkazmoq">finish</span>."</p>
""",
        "grammar": [
            {"pattern": "multiply to … and add to …",
             "meaning": "koʻpaytmasi … va yigʻindisi … — AC usulining izlash sharti"},
            {"pattern": "starting from the smallest",
             "meaning": "eng kichigidan boshlab — juftliklarni tartib bilan yozish"},
            {"pattern": "a search you can finish",
             "meaning": "tugatib boʻladigan izlanish (tasodifiy urinishdan farqli)"},
        ],
        "questions": [
            {"text": "How many pairs did Malika write before she found the answer?",
             "choices": ["Four", "Five", "Six", "Three"],
             "answer": 1,
             "explanation": "U 1·60, 2·30, 3·20, 4·15 va 5·12 juftliklarini yozdi — "
                            "javob beshinchisida chiqdi."},
            {"text": "What was wrong with Rustam's method?",
             "choices": ["He used the wrong two numbers",
                         "He worked in no order, so he repeated himself",
                         "He wrote his pairs down",
                         "He was slower than Malika from the start"],
             "answer": 1,
             "explanation": "U tezroq ishladi, lekin tartibsiz: bitta juftlikni ikki "
                            "marta sinab koʻrdi va qayerga yetganini bilmasdi."},
            {"text": "What does the supervisor mean by her last sentence?",
             "choices": ["That clever workers do not need a method",
                         "That searching takes a long time",
                         "That an ordered search has an end, while guessing may not",
                         "That Malika is cleverer than Rustam"],
             "answer": 2,
             "explanation": "Tartibli izlanishning chegarasi bor — juftliklar tugaydi; "
                            "taxmin qilish esa cheksiz davom etishi mumkin."},
        ],
    },

    # ── 33 · biography, history of mathematics ───────────────────────
    {
        "title": "The Man from Khwarazm",
        "order": 33,
        "summary": (
            "Al-Xorazmiy kvadrat tenglamalarni soʻz bilan yechgan — bu matn ham "
            "shunday yozilgan. «Algebra» va «algoritm» soʻzlari undan qolgan."
        ),
        "body": """
<p>About twelve hundred years ago a <span class="cn-word" data-tr="olim">scholar</span> was born
in Khwarazm, in what is now Uzbekistan. We know very little about his life. We know his work
better than almost any other book of its age.</p>

<p>He worked in Baghdad, at the library the <span class="cn-word" data-tr="xalifa">caliph</span>
had built, and some time around the year eight hundred and twenty he finished a book about
solving equations. Its title contained the word <em>al-jabr</em>, which meant moving a
<span class="cn-word" data-tr="had (ifodaning qismi)">term</span> from one side of an equation to
the other. Europe <span class="cn-word" data-tr="oʻzlashtirdi, oldi">borrowed</span> that word and never gave it back. We call the whole
<span class="cn-word" data-tr="fan, soha">subject</span> algebra.</p>

<p>His name gave us a second word. He wrote a book of step-by-step
<span class="cn-word" data-tr="usul, tartib">procedures</span> for calculating, and Latin writers
called such a procedure by his name. Every time a programmer says
<span class="cn-word" data-tr="algoritm">algorithm</span>, they are saying "al-Khwarizmi" with
the corners worn off.</p>

<p>Here is the part that surprises students. He had no
<span class="cn-word" data-tr="belgi, simvol">symbols</span>. There was no letter standing for
<span class="cn-word" data-tr="nomaʼlum miqdor">the unknown</span>, no plus sign, no equals sign — none of these had been
<span class="cn-word" data-tr="ixtiro qilingan">invented</span> yet. He wrote every equation as a
sentence, in words, exactly the way this reading is written.</p>

<p>And he had no negative numbers, so he could not write one general
<span class="cn-word" data-tr="qoida, retsept">recipe</span>. He had to treat several
<span class="cn-word" data-tr="hol, holat">cases</span> separately, and he proved each one with a
<span class="cn-word" data-tr="chizma">diagram</span> — a real square, drawn on the page, with
smaller rectangles added to its sides until it was complete.</p>

<p>That drawing is the reason the method is still called completing the square. He was
completing an actual square.</p>
""",
        "grammar": [
            {"pattern": "moving a term from one side to the other",
             "meaning": "hadni bir tomondan ikkinchisiga oʻtkazish — al-jabr"},
            {"pattern": "a step-by-step procedure",
             "meaning": "bosqichma-bosqich usul — «algoritm» soʻzining maʼnosi"},
            {"pattern": "completing the square",
             "meaning": "toʻliq kvadratga toʻldirish — kvadrat tenglamani yechish usuli"},
        ],
        "questions": [
            {"text": "Why could al-Khwarizmi not write one general method?",
             "choices": ["He did not know how to solve every case",
                         "His book was too short",
                         "He had no negative numbers, so the cases had to be separated",
                         "He preferred drawings to words"],
             "answer": 2,
             "explanation": "Manfiy sonlarsiz bitta umumiy formula yozib boʻlmasdi — "
                            "har bir hol alohida koʻrib chiqilgan."},
            {"text": "What does the phrase 'with the corners worn off' suggest about the word "
                     "algorithm?",
             "choices": ["That it is a mistake",
                         "That it is his name, changed by centuries of use",
                         "That it was invented in Latin",
                         "That it has a different meaning now"],
             "answer": 1,
             "explanation": "Soʻz uning ismidan kelib chiqqan va asrlar davomida "
                            "shakli oʻzgargan — «burchaklari yeyilgan»."},
            {"text": "Why is the phrase 'completing the square' more than a figure of speech?",
             "choices": ["Because squares are used in every equation",
                         "Because the answer is always a square number",
                         "Because a square has four equal sides",
                         "Because he really drew a square and added pieces to it"],
             "answer": 3,
             "explanation": "U isbotni chizma bilan qilgan: haqiqiy kvadrat chizib, "
                            "tomonlariga toʻrtburchaklar qoʻshib toʻldirgan."},
        ],
    },

    # ── 34 · a fire-service demonstration ────────────────────────────
    {
        "title": "Will It Reach the Window?",
        "order": 34,
        "summary": (
            "Oʻt oʻchiruvchilar suv shovqini qaysi balandlikka yetishini soʻraydi — "
            "diskriminant «yeta oladimi» degan savolga hisoblamasdan javob beradi."
        ),
        "body": """
<p>Every autumn the fire service came to the school. They parked the
<span class="cn-word" data-tr="oʻt oʻchirish mashinasi">engine</span> in the yard, let the
children hold the <span class="cn-word" data-tr="dubulgʻa">helmet</span>, and finished with the
part everyone waited for: they sent a <span class="cn-word" data-tr="oqim, shovqin">jet</span> of
water straight up into the air.</p>

<p>This year the officer turned it into a question. "That jet leaves the hose at twenty metres a
second," he said, pointing at the school wall. "The top-floor windows are twenty metres up. The
<span class="cn-word" data-tr="anten, ustun">mast</span> on the roof is twenty-five metres up.
Which of them can we <span class="cn-word" data-tr="yetmoq">reach</span>?"</p>

<p>The children <span class="cn-word" data-tr="taxmin qilishdi">guessed</span>. Some said both. Most said the windows only. Nobody could say why.</p>

<p>The officer had done the <span class="cn-word" data-tr="hisob-kitob">arithmetic</span> the night before, and he did not need to
<span class="cn-word" data-tr="hisoblamoq">calculate</span> how high the water went to answer
him. He had asked a smaller question instead: is there any moment at all when the water is
twenty-five metres up? The arithmetic of that question ended in a
<span class="cn-word" data-tr="manfiy">negative</span> number, and a negative number there means
there is no such moment. Not later, not sooner, not ever. The mast was
<span class="cn-word" data-tr="xavfsiz, tegilmagan">safe</span>.</p>

<p>He asked the same small question about the windows, and this time the arithmetic ended in
<span class="cn-word" data-tr="nol">zero</span>. Not a negative, not a comfortable positive —
exactly zero. The water reaches the top-floor windows at one single
<span class="cn-word" data-tr="lahza">instant</span> and then falls away.</p>

<p>"So we can reach them," he told the class, "but only just, and only for a moment. If your
window is on the top floor, do not <span class="cn-word" data-tr="tayanmoq, ishonmoq">rely</span>
on us hosing it from the yard. We will come up the stairs."</p>
""",
        "grammar": [
            {"pattern": "is there any moment when …",
             "meaning": "shunday lahza bormi — «yechim bormi» degan savolning tili"},
            {"pattern": "ended in a negative number",
             "meaning": "manfiy chiqdi → yechim yoʻq (diskriminant manfiy)"},
            {"pattern": "exactly zero",
             "meaning": "aynan nol → aynan bitta yechim, ya'ni eng yuqori nuqta"},
        ],
        "questions": [
            {"text": "Why can the water never reach the mast?",
             "choices": ["The hose is pointed at the wrong angle",
                         "The mast is on the roof",
                         "There is no moment at which the water is that high",
                         "The engine is parked too far away"],
             "answer": 2,
             "explanation": "Savol «qachon 25 metrda boʻladi» edi, va uning javobi "
                            "yoʻq — hech qanday lahzada."},
            {"text": "What does the zero tell the officer about the windows?",
             "choices": ["The water passes them twice",
                         "The water just barely reaches them, at one instant",
                         "The water cannot reach them",
                         "The windows are exactly as high as the mast"],
             "answer": 1,
             "explanation": "Nol — chegaraviy hol: suv shu balandlikka faqat bir "
                            "lahza yetadi, ya'ni bu uning eng yuqori nuqtasi."},
            {"text": "What is clever about the officer's approach?",
             "choices": ["He measured the school wall first",
                         "He asked the children to guess",
                         "He used the fire engine's own instruments",
                         "He answered 'can it?' without working out how high it goes"],
             "answer": 3,
             "explanation": "U maksimal balandlikni umuman hisoblamadi — kichikroq "
                            "savol («shunday lahza bormi») yetarli boʻldi."},
        ],
    },

    # ── 35 · city engineering ────────────────────────────────────────
    {
        "title": "The Fountain in the Square",
        "order": 35,
        "summary": (
            "Favvora yoyining eng yuqori nuqtasi — parabolaning uchi; nasos "
            "sozlanganda uch siljiydi, shakli esa oʻzgarmaydi."
        ),
        "body": """
<p>The <span class="cn-word" data-tr="favvora">fountain</span> in the town square had been broken
for two years, and when the <span class="cn-word" data-tr="muhandis">engineer</span> finally came
to repair it, half the town came to watch.</p>

<p>She set the <span class="cn-word" data-tr="nasos">pump</span> and stood back. The water left
the <span class="cn-word" data-tr="jumrak, forsunka">nozzle</span>, rose in a long
<span class="cn-word" data-tr="egri chiziq, yoy">curve</span>, and came down into the pool. She
watched it for a while and then took out a notebook.</p>

<p>"Three metres out from the nozzle," she said, "it reaches its highest point, and there it is
nine metres above the water. Six metres out, it comes back down to the
<span class="cn-word" data-tr="sath, yuza">surface</span>. That is all I need to know about this
fountain."</p>

<p>A boy watching asked how she could be so sure about the far side, since she had only measured
the near one. She said the curve was <span class="cn-word" data-tr="simmetrik">symmetrical</span>.
Whatever the water does on the way up, it does again in
<span class="cn-word" data-tr="teskari, orqaga">reverse</span> on the way down. The highest point
sits exactly <span class="cn-word" data-tr="oʻrtasida">midway</span> between the place it leaves
the water and the place it returns to it.</p>

<p>Then the <span class="cn-word" data-tr="shahar hokimi">mayor</span> asked her to make it
<span class="cn-word" data-tr="balandroq">taller</span>. She turned the pump up, and the whole
curve grew: the top climbed higher and the water landed further out. But the shape did not
change, and the highest point stayed exactly halfway along. Every setting of that pump gave a
different <span class="cn-word" data-tr="cho'qqi, eng yuqori nuqta">peak</span>, and the peak was
always in the middle.</p>

<p>"That is the useful thing about this curve," she told the mayor, closing the notebook. "You
only ever have to find one point on it. The rest of the
<span class="cn-word" data-tr="yoy, ark">arch</span> is folded around that point."</p>
""",
        "grammar": [
            {"pattern": "it reaches its highest point",
             "meaning": "eng yuqori nuqtasiga yetadi — parabolaning uchi"},
            {"pattern": "exactly midway between",
             "meaning": "aynan oʻrtasida — uch ikki nolning oʻrtasida turadi"},
            {"pattern": "folded around that point",
             "meaning": "shu nuqta atrofida buklangan — simmetriya oʻqi"},
        ],
        "questions": [
            {"text": "How far from the nozzle does the water come back down?",
             "choices": ["Nine metres", "Six metres", "Three metres", "Twelve metres"],
             "answer": 1,
             "explanation": "Matn buni toʻgʻridan-toʻgʻri aytadi: olti metrda suv "
                            "sathga qaytadi. Toʻqqiz — balandlik, masofa emas."},
            {"text": "Why was the engineer sure about the far side of the curve?",
             "choices": ["Because the curve is symmetrical about its highest point",
                         "Because she had measured it before",
                         "Because the pool is round",
                         "Because the pump was set low"],
             "answer": 0,
             "explanation": "Yoy simmetrik: koʻtarilishdagi harakat tushishda "
                            "teskari takrorlanadi."},
            {"text": "What stayed the same when the pump was turned up?",
             "choices": ["The height of the peak",
                         "The distance the water landed",
                         "The peak stayed midway between the two ends",
                         "Nothing at all"],
             "answer": 2,
             "explanation": "Balandlik ham, masofa ham oshdi; oʻzgarmagani — "
                            "cho'qqining ikki chekka oʻrtasida turishi."},
        ],
    },
]
