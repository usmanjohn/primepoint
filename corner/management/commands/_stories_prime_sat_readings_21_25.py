# -*- coding: utf-8 -*-
"""Prime SAT Readings — SAT-21 … SAT-25 (batch 5).

  21 — a blood-donation notice     (SAT-21: two conditions at once)
  22 — a piano tuner's ear         (SAT-22: within one hertz of the standard)
  23 — the chessboard and the rice (SAT-23: doubling, and why it runs away)
  24 — why A4 is that shape        (SAT-24: halving areas and the root-two ratio)
  25 — the square that was paved   (SAT-25: area 200, diagonal exactly 20)

Genre rotation — none of the twenty shapes used in batches 1–4 repeat here.

⛔ NO ALGEBRAIC NOTATION IN THE BODY — quantities in English, units spelled out.
   Powers are written in words ("doubles again", "a thousand and twenty-four").
NARRATOR VOICE (batch 4 ran 3 male / 2 female, so this one flips):
    21 en-US-JennyNeural · 22 en-US-GuyNeural · 23 en-US-JennyNeural
    24 en-US-GuyNeural   · 25 en-US-JennyNeural

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_21_25.py --author=prime
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
    # SAT-21 — two conditions                                  [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Two Boxes on the Form",
        "summary": (
            "SAT-21 matni. Qon topshirish shartlari ikkita — va ikkalasi ham "
            "bajarilishi kerak. Bitta shartga mos kelish yetarli emas."
        ),
        "order":   21,
        "grammar": [
            {
                "pattern":  "you must be both … and …",
                "meaning":  "Ikkala shart ham bajarilishi kerak. Tengsizliklar "
                            "sistemasining kundalik tildagi koʻrinishi: yechim — "
                            "<b>kesishma</b>.",
                "examples": ["You must be both over fifty kilograms and under sixty-one."],
            },
            {
                "pattern":  "meets one condition but not the other",
                "meaning":  "Bir shartga mos keladi, ikkinchisiga yoʻq — demak "
                            "<b>umuman mos emas</b>.",
                "examples": ["He met one condition but not the other, so he was turned away."],
            },
            {
                "pattern":  "eligible",
                "meaning":  "Huquqli, mos keladigan. Tibbiy va rasmiy matnlarda "
                            "«shartlarga javob beradi» degani.",
                "examples": ["Only donors who meet both rules are eligible."],
            },
        ],
        "body": '''<p>The <span class="cn-word" data-tr="qon topshirish markazi">blood donation centre</span> in the city hospital keeps a short <span class="cn-word" data-tr="eʼlon">notice</span> taped beside its door, and the whole notice is two lines long.</p>

<p>«To give blood you must weigh at least 50 kilograms, and you must be aged between 18 and 60.»</p>

<p>The <span class="cn-word" data-tr="hamshira">nurse</span> who works the <span class="cn-word" data-tr="qabul stoli">front desk</span> says the same sentence forty times a day, because people read one line and stop. A strong seventeen-year-old who weighs 62 kilograms meets the weight rule easily and is still <span class="cn-word" data-tr="qaytariladi, rad etiladi">turned away</span>. A woman of thirty who weighs 48 kilograms is exactly the right age and is also turned away — kindly, and with an invitation to come back.</p>

<p>Neither of them has been treated <span class="cn-word" data-tr="adolatsiz">unfairly</span>. The notice does not offer two ways of <span class="cn-word" data-tr="malakaga ega boʻlmoq">qualifying</span>; it sets two <span class="cn-word" data-tr="shart">conditions</span> that must hold <strong>at the same time</strong>.</p>

<p>Both rules exist for a reason the nurse is happy to explain. The <span class="cn-word" data-tr="ogʻirlik chegarasi">weight limit</span> protects the donor: the <span class="cn-word" data-tr="hajm">volume</span> taken is fixed, so a lighter body loses a larger share of its blood. The age range protects the donor too, at both ends.</p>

<p>A woman of thirty who weighs 55 kilograms <strong>meets</strong> both, and gives <span class="cn-word" data-tr="qon">blood</span> in eleven minutes.</p>

<p>If you drew the two rules on a chart — weight along one side, age along the other — the <span class="cn-word" data-tr="ruxsat etilgan soha">permitted area</span> would be a neat <span class="cn-word" data-tr="toʻrtburchak">rectangle</span>, and every person turned away that morning would be a dot just outside one of its edges.</p>''',
        "questions": [
            {
                "text": "Why is the seventeen-year-old turned away?",
                "choices": ["He does not weigh enough", "He is below the age range",
                            "Both rules are broken"],
                "answer": 1,
                "explanation": "U 62 kg — ogʻirlik sharti bajarilgan. Lekin yoshi 18 dan "
                               "kichik, demak <b>ikkinchi</b> shart buzilgan. Bitta "
                               "buzilgan shart yetarli.",
            },
            {
                "text": "Which person in the text is eligible to give blood?",
                "choices": ["The seventeen-year-old weighing 62 kilograms",
                            "The thirty-year-old weighing 48 kilograms",
                            "The thirty-year-old weighing 55 kilograms"],
                "answer": 2,
                "explanation": "55 ≥ 50 ✓ va yoshi 18 bilan 60 orasida ✓ — ikkala shart "
                               "ham bajarildi. Qolgan ikkisi bittadan shartni buzadi.",
            },
            {
                "text": "What shape would the permitted region make on a chart of weight against age?",
                "choices": ["A rectangle", "A straight line", "Two separate areas"],
                "answer": 0,
                "explanation": "Ogʻirlik pastdan chegaralangan, yosh esa ikki tomondan — "
                               "shuning uchun ruxsat etilgan soha <b>toʻrtburchak</b>. "
                               "Bu tengsizliklar sistemasining grafigidir.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-22 — within one hertz                                   [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "One Hertz Either Way",
        "summary": (
            "SAT-22 matni. Pianino sozlovchisi 440 gerts atrofidagi tor yoʻlakni "
            "quloq bilan topadi — modulli tengsizlikning eng aniq misoli."
        ),
        "order":   22,
        "grammar": [
            {
                "pattern":  "within one hertz of",
                "meaning":  "…dan bir gerts uzoq emas. <b>Oraliq</b>: 439 dan 441 "
                            "gacha, ikki tomonga bir xil.",
                "examples": ["The note must be within one hertz of the standard."],
            },
            {
                "pattern":  "either way",
                "meaning":  "Ikki tomonga ham — yuqoriga ham, pastga ham. Modul "
                            "yoʻnalishni emas, <b>uzoqlikni</b> oʻlchashini "
                            "koʻrsatadi.",
                "examples": ["One hertz either way is close enough."],
            },
            {
                "pattern":  "out of tune",
                "meaning":  "Sozlanmagan. Chegaradan chiqqan nota — modulli "
                            "tengsizlikning buzilishi.",
                "examples": ["Two and a half hertz high is clearly out of tune."],
            },
        ],
        "body": '''<p>The A above middle C on a piano is supposed to <span class="cn-word" data-tr="tebranmoq">vibrate</span> 440 times a second. That number is an international <span class="cn-word" data-tr="andoza, meʼyor">standard</span>, agreed so that an oboe in Tashkent and a piano in Berlin can play the same note.</p>

<p>No string sits exactly on 440, and no <span class="cn-word" data-tr="sozlovchi">tuner</span> expects it to. The working rule in most <span class="cn-word" data-tr="ustaxona">workshops</span> is that a note is acceptable if it is <strong>within one hertz of</strong> the standard — anywhere from 439 to 441.</p>

<p>Notice what that rule does not say. It does not say the note must be a little <span class="cn-word" data-tr="past (ovoz)">flat</span>, or a little <span class="cn-word" data-tr="baland (ovoz)">sharp</span>. One hertz <strong>either way</strong> is close enough, because the ear does not care which side of 440 the string is on; it cares how far away it is.</p>

<p>A <span class="cn-word" data-tr="tor, sim">string</span> measured at 442.5 hertz is two and a half hertz above the standard, which is outside the <span class="cn-word" data-tr="qoida">rule</span> and clearly <strong>out of tune</strong>. A string at 439.2 is eight <span class="cn-word" data-tr="oʻndan bir">tenths</span> below it, and passes.</p>

<p>The remarkable part is that a good tuner needs no <span class="cn-word" data-tr="asbob, oʻlchagich">meter</span> to hear this. When two strings are close but not equal, the sound <span class="cn-word" data-tr="tebranib, pulsatsiya bilan">pulses</span> — and the pulses come at exactly the rate of the difference. Two hertz apart gives two <span class="cn-word" data-tr="urish, puls">beats</span> a second, one hertz apart gives one, and a string dead on the note gives none at all.</p>

<p>So the tuner is not guessing. She is <span class="cn-word" data-tr="sanamoq">counting</span> a distance she can hear, and stopping when it <span class="cn-word" data-tr="tushmoq">falls</span> below one.</p>''',
        "questions": [
            {
                "text": "Which range of frequencies is acceptable?",
                "choices": ["Below 440 hertz only", "439 to 441 hertz",
                            "438 to 442 hertz"],
                "answer": 1,
                "explanation": "«Within one hertz of 440» — 440 dan bir gerts uzoq "
                               "emas: <b>439 dan 441 gacha</b>. Modul ikki tomonga "
                               "bir xil ishlaydi.",
            },
            {
                "text": "A string measures 439.2 hertz. Is it acceptable?",
                "choices": ["Yes — it is 0.8 away, which is less than one",
                            "No — it is below the standard",
                            "No — it is more than one hertz away"],
                "answer": 0,
                "explanation": "|439.2 − 440| = 0.8, va bu 1 dan kichik ✓. Pastda "
                               "boʻlishi oʻzi ayb emas — qoida <b>uzoqlikni</b> "
                               "oʻlchaydi.",
            },
            {
                "text": "How many beats a second would a string two hertz away from the standard produce?",
                "choices": ["None", "One", "Two"],
                "answer": 2,
                "explanation": "Matnda aytilganidek, urishlar soni aynan farqqa teng: "
                               "ikki gerts farq — sekundiga <b>ikki</b> urish. Notaga "
                               "aniq tushgan tor esa umuman urish bermaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-23 — doubling                                        [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Chessboard and the Rice",
        "summary": (
            "SAT-23 matni. Shohga arzon koʻringan talab: birinchi katakka bitta "
            "donni, keyingisiga ikkitasini… Ikkilanish qanchalik tez oʻsishi."
        ),
        "order":   23,
        "grammar": [
            {
                "pattern":  "doubling",
                "meaning":  "Ikkilanish — har qadamda ikkiga koʻpaytirish. Bu "
                            "qoʻshish emas: oʻsish har safar <b>tezlashadi</b>.",
                "examples": ["Doubling looks slow for ten squares and then runs away."],
            },
            {
                "pattern":  "sounds modest",
                "meaning":  "Kamtarona eshitiladi. Matnda odatda «lekin aslida "
                            "unday emas» degan davomi bor.",
                "examples": ["One grain, then two, sounds modest enough."],
            },
            {
                "pattern":  "more than … put together",
                "meaning":  "…ning hammasini qoʻshgandan koʻra koʻproq. Eksponensial "
                            "oʻsishning odatiy taqqoslashi.",
                "examples": ["The last square holds more than all the others put together."],
            },
        ],
        "body": '''<p>The story is told in a dozen countries and is almost certainly a <span class="cn-word" data-tr="afsona">legend</span>, but the arithmetic inside it is real, and that is why it has lasted.</p>

<p>A <span class="cn-word" data-tr="topqir, zukko">clever</span> man shows a king a new game played on sixty-four squares. The king offers him any <span class="cn-word" data-tr="mukofot">reward</span>. The man asks for rice: one <span class="cn-word" data-tr="don">grain</span> on the first <span class="cn-word" data-tr="katak">square</span>, two on the second, four on the third, and so on, <strong>doubling</strong> to the end of the board.</p>

<p>It <strong>sounds modest</strong>, and the king agrees without thinking. For the first ten squares he is right to feel calm — the tenth square takes only 512 <span class="cn-word" data-tr="donalar">grains</span>, less than a <span class="cn-word" data-tr="hovuch">handful</span>.</p>

<p>By the twenty-first square the <span class="cn-word" data-tr="uyum">pile</span> has passed a million grains. By the fortieth it is more rice than the kingdom's <span class="cn-word" data-tr="ombor">granaries</span> hold. The sixty-fourth square alone would need <span class="cn-word" data-tr="milliard">billions</span> of <span class="cn-word" data-tr="tonna">tonnes</span> — <strong>more than</strong> every square before it <strong>put together</strong>, because each square doubles everything that came before.</p>

<p>That last sentence is the whole idea, and it is worth reading twice. In doubling, the newest step is always bigger than the entire <span class="cn-word" data-tr="tarix, oʻtmish">history</span> of the process.</p>

<p>It is also why the king's mistake is so easy to make. He judged the <span class="cn-word" data-tr="taklif">offer</span> by its first few terms, which is exactly how people judge a small <span class="cn-word" data-tr="foiz">percentage</span> of growth today — and exactly why compound growth surprises them thirty steps later.</p>''',
        "questions": [
            {
                "text": "How many grains are on the tenth square?",
                "choices": ["20 grains", "512 grains", "1,024 grains"],
                "answer": 1,
                "explanation": "Birinchi katakda 1 dona, keyin har safar ikkilanadi — "
                               "oʻninchi katakda ikki toʻqqiz marta koʻpaytirilgan: "
                               "<b>512</b>. 1,024 — oʻn birinchi katak.",
            },
            {
                "text": "Why does the last square hold more than all the earlier squares together?",
                "choices": ["Because the board has sixty-four squares",
                            "Because each square doubles the whole amount that came before",
                            "Because rice grains vary in size"],
                "answer": 1,
                "explanation": "Har bir katak oʻzidan oldingi <b>hammasini</b> "
                               "ikkilantiradi — shuning uchun oxirgi qadam butun "
                               "tarixdan kattaroq boʻladi.",
            },
            {
                "text": "What mistake did the king make?",
                "choices": ["He judged the whole offer by its first few squares",
                            "He miscounted the squares on the board",
                            "He forgot that rice can be weighed"],
                "answer": 0,
                "explanation": "Dastlabki qadamlar kichik boʻlgani uchun u butun taklifni "
                               "arzon deb hisobladi. Matn buni bugungi foizli oʻsishni "
                               "baholashdagi xato bilan taqqoslaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-24 — halving and the root-two ratio                     [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Why A4 Is That Shape",
        "summary": (
            "SAT-24 matni. A4 qogʻozning oʻlchami tasodifiy emas: butun tizim bitta "
            "shartdan — «ikkiga boʻlinganda shakl oʻzgarmasin» — kelib chiqadi."
        ),
        "order":   24,
        "grammar": [
            {
                "pattern":  "halved again and again",
                "meaning":  "Qayta-qayta ikkiga boʻlinadi. Har boʻlish yuzani "
                            "yarmiga tushiradi — manfiy darajaning amaliy "
                            "koʻrinishi.",
                "examples": ["A0 is halved again and again to give A1, A2, A3 and A4."],
            },
            {
                "pattern":  "keeps the same proportions",
                "meaning":  "Nisbatlarini saqlaydi. Bu butun tizimning yagona "
                            "sharti.",
                "examples": ["Folded in half, the sheet keeps the same proportions."],
            },
            {
                "pattern":  "scales without distortion",
                "meaning":  "Shakli buzilmasdan kattalashadi yoki kichrayadi — "
                            "shuning uchun nusxa olishda hech narsa "
                            "choʻzilmaydi.",
                "examples": ["A drawing scales from A3 to A4 without distortion."],
            },
        ],
        "body": '''<p>Pick up any <span class="cn-word" data-tr="varaq">sheet</span> of A4 paper. It is 210 millimetres wide and 297 long, and neither number looks like anything a person would choose.</p>

<p>They are both <span class="cn-word" data-tr="natija">consequences</span> of a single <span class="cn-word" data-tr="qaror">decision</span>. The <span class="cn-word" data-tr="tizim">system</span> begins with a sheet called A0 whose area is exactly one square metre. A1 is A0 folded in half; A2 is A1 folded in half; and so on. A4 is the fourth <span class="cn-word" data-tr="buklash">fold</span>, so its area is a sixteenth of a square metre — about 625 square centimetres.</p>

<p>The <span class="cn-word" data-tr="topqirona">clever</span> part is the <span class="cn-word" data-tr="nisbat">ratio</span>. The <span class="cn-word" data-tr="loyihachilar">designers</span> wanted a sheet that, <strong>halved again and again</strong>, always <strong>keeps the same proportions</strong> — so that a page designed for one size <strong>scales without distortion</strong> to any other.</p>

<p>Only one shape can do that, and it is the shape whose long side is the <span class="cn-word" data-tr="kvadrat ildiz">square root</span> of two times its short side. Check the sheet in your hand: 297 divided by 210 is 1.414, and the square root of two is 1.414.</p>

<p>Two everyday facts fall straight out of this. A <span class="cn-word" data-tr="nusxa koʻchirish moslamasi">photocopier</span>'s «A4 to A3» button <span class="cn-word" data-tr="kattalashtiradi">enlarges</span> by 141 percent, not 200, because doubling the <span class="cn-word" data-tr="yuza">area</span> means multiplying each side by only the square root of two. And an A4 sheet is thinner and longer than a sheet of American Letter paper, which was chosen by <span class="cn-word" data-tr="odat">custom</span> rather than by arithmetic.</p>

<p>A whole industry, in other words, is standing on one <span class="cn-word" data-tr="irratsional son">irrational number</span>.</p>''',
        "questions": [
            {
                "text": "What is the area of a sheet of A4 paper?",
                "choices": ["One square metre", "A quarter of a square metre",
                            "A sixteenth of a square metre"],
                "answer": 2,
                "explanation": "A0 bir kvadrat metr, va A4 toʻrt marta ikkiga "
                               "boʻlingan: yarmi, choragi, sakkizdan biri, "
                               "<b>oʻn oltidan biri</b> — taxminan 625 sm².",
            },
            {
                "text": "Why does the photocopier enlarge from A4 to A3 by 141 percent rather than 200?",
                "choices": [
                    "Because the paper is thinner at the larger size.",
                    "Because doubling the area multiplies each side by only the square root of two.",
                    "Because the machine loses a little at the edges.",
                ],
                "answer": 1,
                "explanation": "Yuza ikkilanganda <b>tomonlar</b> faqat √2 ≈ 1.414 "
                               "marta ortadi. 200 foiz tomonlarni ikkilantirardi va "
                               "yuza toʻrt barobar boʻlardi.",
            },
            {
                "text": "What single requirement produced the whole A-series?",
                "choices": [
                    "That every sheet keeps the same proportions when halved.",
                    "That every sheet has whole-number dimensions in millimetres.",
                    "That A4 should fit a standard envelope.",
                ],
                "answer": 0,
                "explanation": "Butun tizim shu bitta shartdan kelib chiqadi — va "
                               "faqat uzun tomoni qisqasining √2 barobari boʻlgan "
                               "shakl bu shartni bajaradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-25 — the square that was paved                       [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Two Hundred Square Metres",
        "summary": (
            "SAT-25 matni. Shahar maydonini toshbosish rejasi: yuzasi 200 kvadrat "
            "metr boʻlgan kvadratning tomoni chirkin son, diagonali esa aniq 20 metr."
        ),
        "order":   25,
        "grammar": [
            {
                "pattern":  "works out to",
                "meaning":  "Hisoblanganda … chiqadi. Amaliy matnlarda javobning "
                            "qiymatini keltirish uchun ishlatiladi.",
                "examples": ["The side works out to just over fourteen metres."],
            },
            {
                "pattern":  "to the nearest centimetre",
                "meaning":  "Santimetrgacha yaxlitlangan holda. Amaliyotda "
                            "irratsional son har doim yaxlitlanadi.",
                "examples": ["Fourteen point one four metres, to the nearest centimetre."],
            },
            {
                "pattern":  "comes out exactly",
                "meaning":  "Roppa-rosa chiqadi. Ildizli hisobda ba'zan javob "
                            "butun son boʻladi — va bu tasodif emas.",
                "examples": ["The diagonal comes out exactly twenty metres."],
            },
        ],
        "body": '''<p>When the old <span class="cn-word" data-tr="bozor maydoni">market square</span> in a small town was rebuilt, the <span class="cn-word" data-tr="reja, chizma">plan</span> gave the <span class="cn-word" data-tr="toshbosilgan">paved</span> area as 200 square metres and said the shape was a perfect square. Everything else the builders needed had to come out of those two facts.</p>

<p>The side of the square is the number that, multiplied by itself, gives 200. It <strong>works out to</strong> a little over fourteen metres — 14.14 <strong>to the nearest centimetre</strong> — and it is not a tidy number, which is why the <span class="cn-word" data-tr="pudratchi">contractor</span> wrote it on the plan in exact form instead: ten <span class="cn-word" data-tr="ildiz ostidagi ifoda">roots</span> of two.</p>

<p>The <span class="cn-word" data-tr="diagonal">diagonal</span> is where the arithmetic turns friendly. The diagonal of any square is its side multiplied by the square root of two — and multiplying ten roots of two by another root of two gives twenty. The path across the corner of that square <strong>comes out exactly</strong> twenty metres, with no <span class="cn-word" data-tr="qoldiq, dum">remainder</span> at all.</p>

<p>The builders used it. A diagonal <span class="cn-word" data-tr="ip, arqon">string line</span> of exactly twenty metres is far easier to <span class="cn-word" data-tr="oʻlchab belgilamoq">set out</span> on <span class="cn-word" data-tr="notekis yer">rough ground</span> than a side of 14.14, and once both diagonals are equal and twenty metres long, the <span class="cn-word" data-tr="burchaklar">corners</span> are square without anybody measuring an angle.</p>

<p>The paving <span class="cn-word" data-tr="usta, toshbosar">mason</span> put it more plainly. The side, he said, is a number you round; the diagonal is a number you can <span class="cn-word" data-tr="ishonmoq">trust</span>.</p>''',
        "questions": [
            {
                "text": "What is the length of one side of the square?",
                "choices": ["10 metres", "About 14.14 metres", "20 metres"],
                "answer": 1,
                "explanation": "Tomoni √200 = 10√2, taxminan <b>14.14</b> metr. "
                               "<b>20</b> — diagonalning uzunligi.",
            },
            {
                "text": "Why is the diagonal exactly twenty metres?",
                "choices": [
                    "Because ten roots of two multiplied by another root of two gives twenty.",
                    "Because the diagonal is always twice the side.",
                    "Because 200 divided by 10 is 20.",
                ],
                "answer": 0,
                "explanation": "Diagonal = tomon × √2 = 10√2 × √2 = 10 × 2 = <b>20</b>. "
                               "Ikki ildiz koʻpaytirilib butun son berdi — SAT-25 "
                               "darsidagi eng chiroyli hodisa.",
            },
            {
                "text": "Why did the builders prefer to set out the diagonal rather than the side?",
                "choices": [
                    "Because a diagonal is shorter than a side.",
                    "Because twenty metres is exact, while 14.14 has to be rounded.",
                    "Because the plan did not give the length of the side.",
                ],
                "answer": 1,
                "explanation": "Aniq son bilan ishlash osonroq: 20 metrlik ip "
                               "yaxlitlashsiz oʻlchanadi, va ikkala diagonal teng "
                               "boʻlsa burchaklar oʻz-oʻzidan toʻgʻri chiqadi.",
            },
        ],
    },
]
