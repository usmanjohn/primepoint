# -*- coding: utf-8 -*-
"""Prime SAT Readings — 36–40 (SAT-36 … SAT-40 darslariga).

Written with the overrides in corner/management/commands/toc_prime_sat_readings.txt
⛔ MATNDA ALGEBRAIK BELGI YOʻQ — miqdorlar faqat ingliz tilida, soʻz bilan.

Til: matn, sarlavha va savollar INGLIZCHA; summary, cn-word glosslari,
     "Exam English" izohlari va javob tushuntirishlari OʻZBEKCHA.

Ovozlar (8-batch erkakdan boshlanadi): 36 Guy · 37 Jenny · 38 Guy ·
                                       39 Jenny · 40 Guy

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_36_40.py --author=prime
    python manage.py gen_corner_audio --collection="Prime SAT Readings" \\
        --only <n> --voice en-US-GuyNeural        # ⚠️ --voice MAJBURIY
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

    # ── 36 · a market-<span class="cn-word" data-tr="rasta, doʻkoncha">stall</span> diary ────────────────────────────────────
    {
        "title": "The Price of Apricots",
        "order": 36,
        "summary": (
            "Narxni oshirgan sayin daromad oshavermaydi — bozordagi ayol buni "
            "hisob daftaridan, formulasiz topgan."
        ),
        "body": """
<p>Nodira's <span class="cn-word" data-tr="oʻrik">apricots</span> were the best in the row, and
for three years she sold them at four thousand som a kilo. Then her son, who had begun studying
<span class="cn-word" data-tr="iqtisod">economics</span>, told her she was <span class="cn-word" data-tr="past baholamoq">undercharging</span>.
"Raise the price," he said. "You will earn more."</p>

<p>She did not argue. She kept a <span class="cn-word" data-tr="daftar">notebook</span> instead.</p>

<p>For one week she charged five thousand and sold one hundred kilos. The week after she charged six
and sold ninety. Then seven, and eighty. Her son was <span class="cn-word"
data-tr="xursand">delighted</span>: the price was climbing and the money was climbing with it.</p>

<p>Nodira kept going. At eight thousand she sold seventy kilos, and the week's
<span class="cn-word" data-tr="tushum, daromad">takings</span> were the same as the week before.
At nine thousand she sold sixty, and the takings <span class="cn-word"
data-tr="tushdi, kamaydi">fell</span>. At ten thousand she sold fifty, and they fell again,
harder.</p>

<p>She showed her son the two columns. Every time she added a thousand to the price, ten kilos
walked past her stall to the next one. For a while the extra thousand was worth more than the ten
lost kilos. Then, quite <span class="cn-word" data-tr="to'satdan">suddenly</span>, it was not.</p>

<p>"There is a <span class="cn-word" data-tr="cho'qqi, eng yuqori nuqta">peak</span> in the
middle," she said. "Before it, raising helps. After it, raising hurts. Your books tell you to
raise the price. They do not tell you when to stop."</p>

<p>Her son went back to the notebook that evening and drew the takings as a
<span class="cn-word" data-tr="egri chiziq">curve</span>. It rose, it
<span class="cn-word" data-tr="tekislandi">levelled off</span>, it came down — the same
<span class="cn-word" data-tr="shakl">shape</span> he had been drawing in class all year, in a
column of his mother's handwriting.</p>
""",
        "grammar": [
            {"pattern": "for a while … then, quite suddenly",
             "meaning": "bir muddat … keyin, toʻsatdan — burilish nuqtasining tili"},
            {"pattern": "raising helps / raising hurts",
             "meaning": "oshirish foyda / zarar keltiradi — cho'qqidan oldin va keyin"},
            {"pattern": "levelled off",
             "meaning": "tekislandi — oʻsish toʻxtagan joy"},
        ],
        "questions": [
            {"text": "At which price were the takings the same as the week before?",
             "choices": ["Seven thousand", "Eight thousand", "Nine thousand", "Six thousand"],
             "answer": 1,
             "explanation": "Matn buni toʻgʻridan-toʻgʻri aytadi: sakkiz mingda tushum "
                            "oldingi hafta bilan bir xil boʻlgan — demak cho'qqi shu "
                            "yerda yoki uning yonida."},
            {"text": "What did the son's advice leave out?",
             "choices": ["That apricots go bad quickly",
                         "That the price should never rise",
                         "That customers would complain",
                         "The point at which raising the price stops helping"],
             "answer": 3,
             "explanation": "Nasihat toʻgʻri edi — lekin faqat cho'qqigacha. Qachon "
                            "toʻxtash kerakligini u aytmagan."},
            {"text": "Why did the takings eventually fall?",
             "choices": ["The extra thousand stopped being worth the ten lost kilos",
                         "She raised the price too slowly",
                         "The apricots became smaller",
                         "Another seller lowered her price"],
             "answer": 0,
             "explanation": "Har qadamda ikki narsa oʻzgaradi: narx oshadi, miqdor "
                            "kamayadi. Bir nuqtadan keyin yoʻqotish yutuqdan katta "
                            "boʻladi."},
        ],
    },

    # ── 37 · an archaeology field note ───────────────────────────────
    {
        "title": "The Broken Arch",
        "order": 37,
        "summary": (
            "Arkning yarmi yiqilgan — simmetriya qolgan yarmidan yoʻqolganini "
            "tiklashga imkon beradi."
        ),
        "body": """
<p>The <span class="cn-word" data-tr="qazishma, ekspeditsiya">dig</span> had uncovered the base
of an old arch, and half of the arch itself. The other half had come down some <span class="cn-word" data-tr="asrlar">centuries</span> ago and
lay in pieces in the sand.</p>

<p>The team's youngest member wanted to know how tall it had been. The
<span class="cn-word" data-tr="arxeolog">archaeologist</span> leading the dig said they could
work it out from what was left, and she was
<span class="cn-word" data-tr="ishonchli">confident</span> about it.</p>

<p>She began with the two <span class="cn-word" data-tr="tayanch, poydevor">feet</span> of the
arch, both still in place. They stood twelve metres apart. The
<span class="cn-word" data-tr="eng baland nuqta">crown</span> of an arch, she explained, always
sits exactly halfway between its feet — six metres in from either side. That much they knew
without measuring anything at all.</p>

<p>Then she used the standing half. Three metres in from the left foot, the surviving <span class="cn-word" data-tr="toshdan qurilgan qism">stonework</span>
reached a height of four metres. By <span class="cn-word"
data-tr="simmetriya">symmetry</span>, the fallen half must have reached exactly four metres at
three metres in from the right foot. Every point had a <span class="cn-word"
data-tr="juftlik, hamroh">partner</span> on the other side, at the same height.</p>

<p>Those three <span class="cn-word" data-tr="oʻlchov">measurements</span> — two feet and one
point on the curve — were enough. She fitted the arch's curve to them and read off the height at
the crown.</p>

<p>The young man asked whether she was <span class="cn-word"
data-tr="taxmin qilmoq">guessing</span>. She said she was not: the shape of an arch is fixed by
three points, and they had three. "The <span class="cn-word" data-tr="yiqilgan">fallen</span>
half is not lost," she said. "It is <span class="cn-word" data-tr="aks etgan">mirrored</span> in
the half that stayed up."</p>
""",
        "grammar": [
            {"pattern": "exactly halfway between its feet",
             "meaning": "tayanchlarning aynan oʻrtasida — uch nollarning oʻrtasida"},
            {"pattern": "every point has a partner on the other side",
             "meaning": "har bir nuqtaning juftligi bor — simmetriya"},
            {"pattern": "fixed by three points",
             "meaning": "uch nuqta bilan aniqlanadi — parabolani belgilash uchun yetarli"},
        ],
        "questions": [
            {"text": "How far in from either foot is the crown of the arch?",
             "choices": ["Twelve metres", "Four metres", "Six metres", "Three metres"],
             "answer": 2,
             "explanation": "Tayanchlar orasi 12 metr, va eng baland nuqta ularning "
                            "aynan oʻrtasida — demak har ikkalasidan 6 metr."},
            {"text": "What did the surviving half tell her about the fallen half?",
             "choices": ["That it was four metres high three metres in from the right foot",
                         "That it was made of different stone",
                         "That it had fallen first",
                         "That it was shorter than the left half"],
             "answer": 0,
             "explanation": "Simmetriya tufayli chap tomondagi har bir nuqtaning "
                            "oʻng tomonda bir xil balandlikdagi juftligi bor."},
            {"text": "Why was she not guessing?",
             "choices": ["She had seen other arches like it",
                         "The shape is fixed by three points, and she had three",
                         "The sand preserved the outline",
                         "The young man measured it for her"],
             "answer": 1,
             "explanation": "Ikki tayanch va egri chiziqdagi bitta nuqta — bu shaklni "
                            "yagona qilib belgilaydi."},
        ],
    },

    # ── 38 · aviation ────────────────────────────────────────────────
    {
        "title": "The Ridge on the Approach",
        "order": 38,
        "summary": (
            "Tekis pasayish chizigʻi va tepalik yoyi — uchrashadimi yoki yoʻqmi. "
            "Uchta javob bor, va ikkitasi qabul qilinmaydi."
        ),
        "body": """
<p>The little airport in the valley had one problem, and every
<span class="cn-word" data-tr="uchuvchi">pilot</span> who flew there knew it by name. Between the
runway and the open sky there was a <span class="cn-word" data-tr="tizma, tepalik">ridge</span>,
and the way down to the runway went straight over it.</p>

<p>An aircraft coming in <span class="cn-word" data-tr="pasaymoq">descends</span> along a straight
line. The ridge is not straight: it rises, rounds off, and falls away again. So the question the
<span class="cn-word" data-tr="tekshiruvchi">inspector</span> came to answer was a simple one.
Where, if anywhere, do the two meet?</p>

<p>There are only three possible answers, and she wrote all three on the board at the
<span class="cn-word" data-tr="brifing xonasi">briefing room</span>.</p>

<p>The line may cross the ridge at two places. That is the
<span class="cn-word" data-tr="xavfli">dangerous</span> one: between those two places the
aircraft would be below the rock.</p>

<p>The line may <span class="cn-word" data-tr="tegmoq, urinmoq">touch</span> the ridge at exactly
one place. That is the <span class="cn-word" data-tr="chegara, qirra">borderline</span> case — the
aircraft grazes the highest stone and clears everything else. No airport in the world accepts
it.</p>

<p>Or the line may miss the ridge <span class="cn-word" data-tr="butunlay">entirely</span>. Then
the approach is <span class="cn-word" data-tr="xavfsiz">safe</span>, and the only remaining
question is by how much.</p>

<p>"You do not need to know <span class="cn-word" data-tr="qayerda">where</span> they meet to know
whether they meet," the inspector said. "One <span class="cn-word"
data-tr="hisob-kitob">calculation</span> tells you which of my three lines you are on, and that is
the one that decides whether we open the runway."</p>

<p>They were on the third line, with sixty metres to spare. The airport opened that
<span class="cn-word" data-tr="bahor">spring</span>.</p>
""",
        "grammar": [
            {"pattern": "where, if anywhere, do the two meet?",
             "meaning": "agar uchrashsa, qayerda — kesishish bormi degan savol"},
            {"pattern": "the borderline case",
             "meaning": "chegaraviy hol — aynan bitta uchrashuv, ya'ni urinish"},
            {"pattern": "whether they meet, not where",
             "meaning": "qayerda emas, uchrashadimi — diskriminant beradigan javob"},
        ],
        "questions": [
            {"text": "Why is meeting the ridge at two places the dangerous case?",
             "choices": ["The aircraft would turn twice",
                         "Between those two places the aircraft is below the rock",
                         "Two places are harder to measure",
                         "The ridge would be too steep"],
             "answer": 1,
             "explanation": "Ikki kesishish orasida tekis chiziq egri chiziqdan pastda "
                            "qoladi — yaʼni samolyot tosh ostida boʻladi."},
            {"text": "Why does no airport accept the borderline case?",
             "choices": ["It is too difficult to calculate",
                         "It costs more to maintain",
                         "It leaves no margin at all — the aircraft grazes the highest stone",
                         "The ridge would have to be removed"],
             "answer": 2,
             "explanation": "Bitta tegish nuqtasi — zaxira nol degani; xavfsizlikda "
                            "chegaraviy hol yetarli emas."},
            {"text": "What is the inspector's main point?",
             "choices": ["That one calculation says which of the three cases applies",
                         "That pilots should fly higher",
                         "That ridges should be measured every spring",
                         "That the runway was built in the wrong place"],
             "answer": 0,
             "explanation": "Kesishish joyini topish shart emas — faqat qaysi holat "
                            "ekanini bilish kifoya."},
        ],
    },

    # ── 39 · forensics ───────────────────────────────────────────────
    {
        "title": "Two Answers, One Road",
        "order": 39,
        "summary": (
            "Hisob ikkita javob berdi, lekin yoʻl faqat bittasini qabul qiladi — "
            "arifmetika toʻgʻri, javob esa mavjud emas."
        ),
        "body": """
<p>The <span class="cn-word" data-tr="tergovchi">investigator</span> arrived after the road had
been cleared, so all she had was a <span class="cn-word" data-tr="surat">photograph</span>, a
<span class="cn-word" data-tr="oʻlchov lentasi">tape measure</span>, and the marks the tyres had
left on the <span class="cn-word" data-tr="asfalt">asphalt</span>.</p>

<p>The driver's <span class="cn-word" data-tr="daʼvo, bayonot">claim</span> was that he had been
travelling slowly. From the length of the marks she could work backwards and test that.</p>

<p>She set up the arithmetic and it gave her two numbers. This did not
<span class="cn-word" data-tr="hayratlantirmoq">surprise</span> her. The step she had used —
removing a square root by squaring — always
<span class="cn-word" data-tr="xavf tugʻdirmoq">risks</span> handing back an answer that the
original situation never allowed.</p>

<p>One of the two numbers was <span class="cn-word" data-tr="manfiy">negative</span>. She crossed
it out without a second thought. A car cannot leave a mark of negative length, and it cannot
travel at a negative speed down a straight road in <span class="cn-word" data-tr="kunduz kuni">daylight</span>. The arithmetic did not know that. She
did.</p>

<p>Her <span class="cn-word" data-tr="hamkasb">colleague</span> asked whether crossing out an
answer was allowed. She said it was not only allowed, it was
<span class="cn-word" data-tr="majburiy">required</span>. "Squaring both sides is a
<span class="cn-word" data-tr="qadam">step</span>, not a truth. Whatever comes out of it has to
be taken back to the beginning and tried against the real thing."</p>

<p>She took the surviving number back to the marks on the road, and it fitted. The other one had
never been an answer at all — only a
<span class="cn-word" data-tr="soya, aks">shadow</span> left behind by the method she had used to
find it.</p>
""",
        "grammar": [
            {"pattern": "an answer the original situation never allowed",
             "meaning": "asl vaziyat qabul qilmaydigan javob — begona ildiz"},
            {"pattern": "squaring is a step, not a truth",
             "meaning": "kvadratga koʻtarish — usul, haqiqat emas"},
            {"pattern": "taken back to the beginning",
             "meaning": "boshiga qaytarilishi kerak — asl tenglamada tekshirish"},
        ],
        "questions": [
            {"text": "Why was the investigator not surprised to get two numbers?",
             "choices": ["Because the marks were unclear",
                         "Because two cars were involved",
                         "Because removing a square root by squaring can hand back an extra answer",
                         "Because the driver had changed his story"],
             "answer": 2,
             "explanation": "Kvadratga koʻtarish asl vaziyatda boʻlmagan javobni "
                            "qoʻshib yuborishi mumkin — bu usulning maʼlum xususiyati."},
            {"text": "On what grounds did she cross out the negative number?",
             "choices": ["It was smaller than the other one",
                         "A mark cannot have negative length and a car cannot have negative speed",
                         "The photograph did not show it",
                         "Her colleague told her to"],
             "answer": 1,
             "explanation": "Arifmetika uni qabul qiladi, vaziyat esa yoʻq — shuning "
                            "uchun u javob emas."},
            {"text": "What does she mean by calling the rejected number a shadow?",
             "choices": ["It was hard to see in the photograph",
                         "It was almost the right answer",
                         "It was left behind by her method, not by the event",
                         "It appeared only at night"],
             "answer": 2,
             "explanation": "U hodisadan emas, u ishlatgan usuldan paydo boʻlgan — "
                            "shuning uchun tekshiruvda yoʻqoladi."},
        ],
    },

    # ── 40 · a puzzle with a real punchline ──────────────────────────
    {
        "title": "The Journey That Cannot Be Averaged",
        "order": 40,
        "summary": (
            "Oʻrtacha tezlikni ikki barobar qilish uchun qaytishda qancha yurish "
            "kerak? Javob: hech qanday tezlik yetmaydi."
        ),
        "body": """
<p>A teacher gave her class a question that sounded <span class="cn-word" data-tr="zararsiz, oddiy">harmless</span>. A driver goes from one town to the
next at thirty kilometres an hour. He wants his <span class="cn-word"
data-tr="oʻrtacha">average</span> speed for the whole journey, there and back, to be sixty. How
fast must he drive on the way back?</p>

<p>Almost every hand went up with the same answer: ninety. Thirty and ninety, they said, average
sixty.</p>

<p>The teacher asked them to check it with the <span class="cn-word"
data-tr="soat">clock</span> instead of with their <span class="cn-word"
data-tr="ichki tuygʻu, sezgi">instinct</span>. Suppose the <span class="cn-word" data-tr="shaharlar">towns</span> are sixty kilometres apart. Going
there at thirty takes two hours. The whole journey is a hundred and twenty kilometres, and to
average sixty he must finish it in two hours.</p>

<p>The room went <span class="cn-word" data-tr="jim">quiet</span>. He has already used the two
hours. The return trip must take no time at all.</p>

<p>"So the answer is not ninety," she said. "The answer is that there is
<span class="cn-word" data-tr="hech qanday">no</span> speed. Not a large one, not an
<span class="cn-word" data-tr="ulkan">enormous</span> one. None."</p>

<p>One boy said that if the driver went fast enough he would surely get
<span class="cn-word" data-tr="yaqin">close</span>. The teacher <span class="cn-word" data-tr="roziligini bildirdi">agreed</span>, and said that was exactly
the interesting part. At a hundred and fifty the average is fifty. At three hundred it is a little over
fifty-four. At a thousand it is a little over fifty-eight. The average creeps towards sixty and
never <span class="cn-word" data-tr="yetmoq">arrives</span>.</p>

<p>"Some questions have an answer you cannot reach," she said, "and the arithmetic tells you so
before you waste a single <span class="cn-word" data-tr="litr">litre</span> of <span class="cn-word" data-tr="yoqilgʻi">fuel</span> finding
out."</p>
""",
        "grammar": [
            {"pattern": "check it with the clock, not with your instinct",
             "meaning": "sezgi bilan emas, soat bilan tekshiring — modelni tekshirish"},
            {"pattern": "must take no time at all",
             "meaning": "umuman vaqt olmasligi kerak — nolga boʻlish holati"},
            {"pattern": "creeps towards sixty and never arrives",
             "meaning": "oltmishga yaqinlashadi, lekin yetmaydi"},
        ],
        "questions": [
            {"text": "Why is ninety the wrong answer?",
             "choices": ["The two speeds must be equal",
                         "The whole journey time is already used up by the first half",
                         "Ninety is too fast to be legal",
                         "The towns are not sixty kilometres apart"],
             "answer": 1,
             "explanation": "Oʻrtacha tezlik masofani vaqtga boʻladi. Birinchi yarmi "
                            "butun ruxsat etilgan vaqtni yeb qoʻygan."},
            {"text": "What happens to the average as the return speed grows?",
             "choices": ["It passes sixty", "It stays at thirty",
                         "It gets closer to sixty but never reaches it", "It falls"],
             "answer": 2,
             "explanation": "Matn uch qiymat beradi — ellik, ellik toʻrt, ellik "
                            "sakkizdan sal koʻp — va ular oltmishga yaqinlashadi."},
            {"text": "What is the teacher's final point?",
             "choices": ["That some questions have an answer you cannot reach",
                         "That drivers should slow down",
                         "That averages are always misleading",
                         "That the class guessed too quickly"],
             "answer": 0,
             "explanation": "Baʼzi savollarning javobi mavjud emas, va buni "
                            "hisob-kitob oldindan aytadi."},
        ],
    },
]
