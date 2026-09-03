# -*- coding: utf-8 -*-
"""Prime SAT Readings — SAT-1 … SAT-5 (batch 1).

Har bir matn oʻz darsiga tegishli, `order` = dars raqami.
Written with STYLE_GUIDE_CORNER.md + the overrides in toc_prime_sat_readings.txt

  1 — a cafe's order sheet          (SAT-1: like terms — same kind adds, different does not)
  2 — a school lab report           (SAT-2: a constant amount each week -> one equation)
  3 — a school trip budget          (SAT-3: flat fee + per-student cost, and the classic slip)
  4 — a bottling line's tolerance   (SAT-4: "differs from 500 by 8" -> two limit values)
  5 — a cooling afternoon           (SAT-5: rate of change, and what the number means)

⛔ NO ALGEBRAIC NOTATION IN THE BODY — no x, no equations. Quantities in English.
   Two reasons: it is the skill being trained, and an equation does not survive TTS.
   Units are spelled out (millilitres, degrees) so the narrator reads them properly.
⚠️ Til: matn inglizcha; summary, glossalar, meaning va explanation oʻzbekcha.
   Son SAT usulida: 3.5 va 1,200.

NARRATOR VOICE (toc'ning AUDIO boʻlimi — Matematika shelfining standart ovozi
INGLIZCHA EMAS, shuning uchun --voice har doim aniq beriladi):
    1 en-US-JennyNeural · 2 en-US-GuyNeural · 3 en-US-JennyNeural
    4 en-US-GuyNeural   · 5 en-US-JennyNeural

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_01_05.py --author=prime
    python manage.py gen_corner_audio --collection="Prime SAT Readings" \\
        --only <n> --voice en-US-JennyNeural
    python manage.py import_corner_audio \\
        corner/management/commands/audio/prime-sat-readings --collection="Prime SAT Readings"
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
    # SAT-1 — like terms                                        [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Counting the Same Thing Twice",
        "summary": (
            "SAT-1 matni. Kichkina kafening haftalik buyurtmasi: bir xil narsalarni "
            "birga qoʻshib, boshqa narsalarni alohida qoldirish — «oʻxshash hadlar» "
            "gʻoyasining hayotdagi koʻrinishi."
        ),
        "order":   1,
        "grammar": [
            {
                "pattern":  "in total / in all",
                "meaning":  "Jami. Savol <b>bitta</b> son soʻrayapti, demak avval bir xil "
                            "turdagi miqdorlarni qoʻshib olish kerak.",
                "examples": ["How many crates of milk did she order in total?",
                             "What did the delivery cost in all?"],
            },
            {
                "pattern":  "for each / per",
                "meaning":  "Har biri uchun. Bu son har doim <b>koʻpaytiriladi</b> — "
                            "sonini bilgach, narxga koʻpaytiring.",
                "examples": ["A crate of milk costs $8 for each crate.",
                             "She pays $22 per sack of coffee."],
            },
            {
                "pattern":  "which expression represents the total",
                "meaning":  "Qaysi ifoda jamini bildiradi. Javob <b>son emas, ifoda</b> "
                            "boʻladi — hisoblab oʻtirmang, tuzilishiga qarang.",
                "examples": ["Which expression represents the total cost of the order?"],
            },
        ],
        "body": '''<p>Nilufar has run a small cafe near the bus station for six years, and every Sunday evening she writes the same sheet of paper: the week's order.</p>

<p>The order arrives in three <span class="cn-word" data-tr="yetkazib berish">deliveries</span>. On Monday the <span class="cn-word" data-tr="kichik yuk mashinasi">van</span> brings 4 <span class="cn-word" data-tr="quti, yashik">crates</span> of milk and 3 <span class="cn-word" data-tr="qop">sacks</span> of <span class="cn-word" data-tr="qahva doni">coffee beans</span>. On Wednesday it brings 6 crates of milk. On Friday it brings 5 crates of milk and 2 more sacks of coffee.</p>

<p>Nilufar does not write nine numbers on her sheet. She writes two. Milk, she writes: 15 crates <strong>in total</strong>. Coffee: 5 sacks. Everything of the same kind goes together on one line, and the two kinds never meet.</p>

<p>Last spring a new <span class="cn-word" data-tr="yordamchi">assistant</span> wrote the sheet for her while she was away. He added every number on the page and wrote one line: <span class="cn-word" data-tr="jami">total</span>, 20 items. It was <span class="cn-word" data-pos="adj" data-tr="tashqi koʻrinishdan toʻgʻri">arithmetically</span> correct and completely <span class="cn-word" data-tr="foydasiz">useless</span>. Twenty of what? The <span class="cn-word" data-tr="yetkazib beruvchi">supplier</span> could not <span class="cn-word" data-tr="buyurtmani bajarmoq">fill the order</span>, the van came on Tuesday with nothing on it, and the cafe served tea for two days.</p>

<p>The prices make the same point. A crate of milk <span class="cn-word" data-tr="turadi, narxi">costs</span> $8 <strong>for each</strong> crate; a sack of coffee costs $22. So the milk cost her $120 that week and the coffee cost $110, and only at the very end, when both lines are finished, do the two numbers join into one: $230.</p>

<p>«You can add crates to crates,» she told the assistant, «and sacks to sacks. You cannot add a crate to a sack and call the answer a number.»</p>''',
        "questions": [
            {
                "text": "How many crates of milk did Nilufar order that week in total?",
                "choices": ["11", "15", "20"],
                "answer": 1,
                "explanation": "4 + 6 + 5 = <b>15</b>. <b>20</b> — yordamchining xatosi: "
                               "u sut va qahvani birga qoʻshgan (15 + 5). Har xil "
                               "turdagi miqdorlar bitta songa qoʻshilmaydi.",
            },
            {
                "text": "According to the text, what was the total cost of the week's order?",
                "choices": ["$110", "$120", "$230"],
                "answer": 2,
                "explanation": "Sut: 15 × $8 = $120. Qahva: 5 × $22 = $110. "
                               "Jami <b>$230</b>. $120 va $110 — yarim yoʻldagi javoblar; "
                               "SAT ularni har doim variantlar orasiga qoʻyadi.",
            },
            {
                "text": "Why was the assistant's single number useless?",
                "choices": [
                    "Because it combined two different kinds of item into one count.",
                    "Because he added the numbers incorrectly.",
                    "Because he forgot the Friday delivery.",
                ],
                "answer": 0,
                "explanation": "Matnda aytilgan: hisob <b>arifmetik jihatdan toʻgʻri</b> "
                               "edi. Xato hisobda emas — bir-biriga qoʻshib boʻlmaydigan "
                               "narsalarni qoʻshganda edi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-2 — linear equations                                    [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Week the Sunflower Passed the Fence",
        "summary": (
            "SAT-2 matni. Maktab biologiya sinfi kungaboqarni har hafta oʻlchaydi. "
            "Bir xil oʻsish + boshlangʻich balandlik = bitta chiziqli tenglama."
        ),
        "order":   2,
        "grammar": [
            {
                "pattern":  "at a constant rate",
                "meaning":  "Oʻzgarmas tezlikda. Bu ibora <b>chiziqli model</b>ni "
                            "eʼlon qiladi: har bir bosqichda bir xil miqdor "
                            "qoʻshiladi yoki ayriladi.",
                "examples": ["The plant grew at a constant rate.",
                             "The tank drains at a constant rate."],
            },
            {
                "pattern":  "at the start / initially",
                "meaning":  "Boshida. Bu son hech narsaga koʻpaymaydi — u <b>yolgʻiz</b> "
                            "turadigan boshlangʻich qiymat.",
                "examples": ["At the start of the study the plant was 32 centimetres tall."],
            },
            {
                "pattern":  "how many weeks did it take",
                "meaning":  "Necha hafta kerak boʻldi. Javob — <b>bosqichlar soni</b>, "
                            "balandlik emas. Savolning oxirgi soʻzini oʻqing.",
                "examples": ["How many weeks did it take to reach the top of the fence?"],
            },
        ],
        "body": '''<p>The biology class at School 24 keeps a <span class="cn-word" data-tr="dala daftari, kuzatuv daftari">field notebook</span> on the window side of the <span class="cn-word" data-tr="hovli">yard</span>. Last year it held one long <span class="cn-word" data-tr="tajriba, kuzatuv">study</span>: a single sunflower, measured every Monday morning for a whole <span class="cn-word" data-tr="chorak, semestr">term</span>.</p>

<p><strong>At the start</strong> the plant was 32 centimetres tall. After that the numbers came in a straight line: 41, then 50, then 59, then 68. Nine centimetres, every week, without one exception. Two pupils checked the <span class="cn-word" data-tr="oʻlchov lentasi">tape measure</span> twice because the <span class="cn-word" data-tr="qator, ketma-ketlik">sequence</span> looked too tidy to be real.</p>

<p>The interesting question came from the back of the room. The old wooden <span class="cn-word" data-tr="devor, panjara">fence</span> along the yard is 122 centimetres high. When would the sunflower look over it?</p>

<p>The class did not guess. They reasoned. The plant had to climb 90 centimetres to get from 32 to the top of the fence, and it climbed 9 centimetres each week <strong>at a constant rate</strong>. So it needed exactly ten weeks.</p>

<p>They wrote the date on the wall in <span class="cn-word" data-tr="boʻr">chalk</span>, and on that Monday in week ten the flower stood exactly <span class="cn-word" data-tr="baravar, teng balandlikda">level</span> with the top board. A week later it was above it, and by the end of the term it had passed the <span class="cn-word" data-tr="yomgʻir suvi trubasi">drainpipe</span>.</p>

<p>Their teacher wrote one line under the last <span class="cn-word" data-tr="oʻlchov natijasi">measurement</span>: <span class="cn-word" data-tr="uch soni yetarli boʻldi">Three numbers were enough</span> — where it began, how much it gained, and where it had to get to.</p>''',
        "questions": [
            {
                "text": "How tall was the sunflower six weeks after the study began?",
                "choices": ["68 centimetres", "86 centimetres", "122 centimetres"],
                "answer": 1,
                "explanation": "Boshlangʻich 32, har hafta 9: 32 + 6 × 9 = 32 + 54 = "
                               "<b>86</b>. <b>68</b> — toʻrtinchi haftadagi balandlik, "
                               "<b>122</b> — devorning balandligi.",
            },
            {
                "text": "How many weeks did it take for the plant to reach the top of the fence?",
                "choices": ["Ten weeks", "Twelve weeks", "Fourteen weeks"],
                "answer": 0,
                "explanation": "Koʻtarilishi kerak boʻlgan balandlik: 122 − 32 = 90 sm. "
                               "Har hafta 9 sm: 90 ÷ 9 = <b>10</b> hafta. Eʼtibor bering, "
                               "avval boshlangʻich balandlik <b>ayriladi</b>.",
            },
            {
                "text": "Which detail tells the reader that the growth was linear?",
                "choices": [
                    "The plant was measured on Monday mornings.",
                    "The plant gained the same nine centimetres every week.",
                    "Two pupils checked the tape measure.",
                ],
                "answer": 1,
                "explanation": "Chiziqli model — <b>har bosqichda bir xil miqdor</b>. "
                               "Oʻlchov kuni ham, tekshiruv ham modelga daxli yoʻq; "
                               "muhimi — oʻzgarish har safar bir xil boʻlgani.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-3 — word problems                                     [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Forty-One Seats and One Bus",
        "summary": (
            "SAT-3 matni. Sinf sayohatining byudjeti va kassirning klassik xatosi: "
            "bir martalik toʻlovni har bir oʻquvchiga qoʻshib yuborish."
        ),
        "order":   3,
        "grammar": [
            {
                "pattern":  "a flat fee of / a one-time charge",
                "meaning":  "Bir martalik toʻlov. U necha kishi borishidan qatʼi nazar "
                            "<b>bir marta</b> toʻlanadi — shuning uchun ifodada yolgʻiz "
                            "turadi.",
                "examples": ["The company charges a flat fee of $180 for the bus."],
            },
            {
                "pattern":  "per student / each",
                "meaning":  "Har bir oʻquvchi uchun. Bu son oʻquvchilar soniga "
                            "<b>koʻpayadi</b>.",
                "examples": ["The museum charges $6 per student."],
            },
            {
                "pattern":  "how many students can go",
                "meaning":  "Nechta oʻquvchi bora oladi. Javob — <b>odamlar soni</b>, "
                            "pul emas; va u butun son boʻlishi kerak.",
                "examples": ["How many students can go on the trip?"],
            },
        ],
        "body": '''<p>The <span class="cn-word" data-tr="qoʻmita">committee</span> for the ninth-year <span class="cn-word" data-tr="sayohat, ekskursiya">trip</span> met for eleven minutes, and the <span class="cn-word" data-tr="yigʻilish bayonnomasi">minutes</span> of that meeting are worth reading.</p>

<p>Two costs were on the table. The bus company charges <strong>a flat fee of</strong> $180 for the day, whether one pupil travels or forty. The museum charges $6 <strong>per student</strong> at the door. Families had already handed in $348 <span class="cn-word" data-tr="hammasi boʻlib">altogether</span>, and the question was simple: how many pupils could go?</p>

<p>The <span class="cn-word" data-tr="xazinachi, kassir">treasurer</span> answered first, and answered wrongly. He divided $348 by $6 and <span class="cn-word" data-tr="eʼlon qildi">announced</span> that fifty-eight pupils could travel. Somebody laughed, because the bus has forty-one <span class="cn-word" data-tr="oʻrindiq">seats</span>, and somebody else asked the better question: what happened to the $180?</p>

<p>The <span class="cn-word" data-tr="sinf rahbari">form teacher</span> took the chalk. The bus is paid once, she said, so take it off the top first: $348 minus $180 leaves $168. That money, and only that money, is <span class="cn-word" data-tr="boʻlinadi">divided</span> at $6 a head. It buys <span class="cn-word" data-tr="roppa-rosa">exactly</span> twenty-eight tickets.</p>

<p>Twenty-eight pupils went. The bus had thirteen empty seats, the museum gave the class a guide for nothing, and the treasurer wrote a sentence in the minutes that his teacher later pinned above the <span class="cn-word" data-tr="eʼlonlar taxtasi">noticeboard</span>:</p>

<p><span class="cn-word" data-tr="bir marta toʻlanadigan pul har bir kishiga boʻlinmaydi">A cost that is paid once does not belong to each person.</span></p>''',
        "questions": [
            {
                "text": "How many students could go on the trip?",
                "choices": ["28", "41", "58"],
                "answer": 0,
                "explanation": "$348 − $180 = $168, keyin $168 ÷ $6 = <b>28</b>. "
                               "<b>58</b> — kassirning xatosi (avtobus haqini "
                               "ayirmagan), <b>41</b> — avtobusdagi oʻrindiqlar soni.",
            },
            {
                "text": "If 30 students had gone, what would the total cost have been?",
                "choices": ["$180", "$360", "$540"],
                "answer": 1,
                "explanation": "Avtobus $180 (bir marta) + muzey 30 × $6 = $180. "
                               "Jami <b>$360</b>. Diqqat: bu ikki $180 turli narsa — "
                               "biri bir martalik toʻlov, ikkinchisi chiptalar puli.",
            },
            {
                "text": "What was the treasurer's mistake?",
                "choices": [
                    "He used the wrong ticket price.",
                    "He counted the seats on the bus incorrectly.",
                    "He treated the one-time bus fee as if it were part of each ticket.",
                ],
                "answer": 2,
                "explanation": "U $348 ni toʻgʻridan-toʻgʻri $6 ga boʻldi — yaʼni bir "
                               "martalik $180 ni ham chiptalar pulining ichida deb "
                               "hisobladi. Bir martalik toʻlov avval <b>ayriladi</b>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-4 — absolute value                                      [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Five Hundred Millilitres, Give or Take",
        "summary": (
            "SAT-4 matni. Suv quyish liniyasidagi nazorat: «meʼyordan 8 millilitrdan "
            "koʻp farq qilsa» degan jumla ikkita chegara sonini beradi."
        ),
        "order":   4,
        "grammar": [
            {
                "pattern":  "differs from … by",
                "meaning":  "…dan shuncha farq qiladi. Bu — <b>modul</b>ning soʻz bilan "
                            "aytilishi: farq ikki tomonga ham boʻlishi mumkin, "
                            "koʻproq ham, kamroq ham.",
                "examples": ["The bottle differs from 500 millilitres by 11 millilitres."],
            },
            {
                "pattern":  "the target value",
                "meaning":  "Moʻljaldagi qiymat — chegaralarning <b>oʻrtasida</b> "
                            "turadigan son. Ikkala chegara ham undan bir xil uzoqlikda.",
                "examples": ["The target value on this line is 500 millilitres."],
            },
            {
                "pattern":  "rejected / accepted",
                "meaning":  "Rad etilgan / qabul qilingan. SAT bunday savolda "
                            "koʻpincha <b>chegaraning oʻzini</b> soʻraydi, misolni emas.",
                "examples": ["Any bottle outside those two limits is rejected."],
            },
        ],
        "body": '''<p>The <span class="cn-word" data-tr="quyish liniyasi">filling line</span> at a small water <span class="cn-word" data-tr="zavod">plant</span> outside Chirchiq runs for eleven hours a day, and every bottle that leaves it is supposed to hold five hundred millilitres.</p>

<p>No machine is that <span class="cn-word" data-tr="aniq">exact</span>. So the <span class="cn-word" data-tr="sifat nazorati">quality control</span> rule is not written as a single number. It is written as a distance: a bottle is <strong>rejected</strong> if its <span class="cn-word" data-tr="hajm">volume</span> <strong>differs from</strong> five hundred millilitres <strong>by</strong> more than eight millilitres.</p>

<p>Read carefully, that one sentence names two numbers that are never printed on the paper. Eight millilitres below the <strong>target value</strong> is four hundred and ninety-two. Eight above is five hundred and eight. Everything between those two <span class="cn-word" data-tr="chegara">limits</span> goes into the <span class="cn-word" data-tr="quti">box</span>; everything outside them goes back to be filled again.</p>

<p>On Tuesday the <span class="cn-word" data-tr="nazoratchi, tekshiruvchi">inspector</span> pulled three bottles off the line. The first held five hundred and five millilitres, which is five away from the target, so it passed. The second held five hundred and eleven, which is eleven away, and it went back. The third held four hundred and ninety-three — seven away, on the low side, and still <span class="cn-word" data-tr="ruxsat etilgan">allowed</span>.</p>

<p>The <span class="cn-word" data-tr="smena">shift</span> <span class="cn-word" data-tr="boshliq, nazoratchi">supervisor</span> keeps one note taped to the machine, and it is the whole idea of the rule in eight words: <span class="cn-word" data-tr="muhimi qaysi tomon emas, qanchalik uzoq">Not which side. How far.</span></p>''',
        "questions": [
            {
                "text": "What are the two limit volumes on this line?",
                "choices": [
                    "492 and 508 millilitres",
                    "492 and 500 millilitres",
                    "500 and 508 millilitres",
                ],
                "answer": 0,
                "explanation": "500 − 8 = <b>492</b> va 500 + 8 = <b>508</b>. Faqat bir "
                               "tomonga qarash — bu mavzudagi eng koʻp uchraydigan xato: "
                               "«farq» ikki tomonga ham boʻladi.",
            },
            {
                "text": "Which of the three bottles was sent back?",
                "choices": [
                    "The one holding 505 millilitres",
                    "The one holding 511 millilitres",
                    "The one holding 493 millilitres",
                ],
                "answer": 1,
                "explanation": "511 moʻljaldan 11 millilitr uzoq — bu 8 dan koʻp, demak "
                               "rad etiladi. 505 (5 uzoq) va 493 (7 uzoq) chegara "
                               "ichida qoladi.",
            },
            {
                "text": "Why does the supervisor's note say «Not which side. How far.»?",
                "choices": [
                    "Because bottles below the target are more common than bottles above it.",
                    "Because the machine can only make mistakes in one direction.",
                    "Because the rule measures distance from the target, so above and below count the same.",
                ],
                "answer": 2,
                "explanation": "Qoida <b>uzoqlik</b>ni oʻlchaydi. Shuning uchun 7 kam ham, "
                               "7 koʻp ham bir xil baholanadi — aynan modulning maʼnosi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-5 — slope                                             [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Two Readings, One Rate",
        "summary": (
            "SAT-5 matni. Ikki ob-havo stansiyasi, bir kunning kechki sovishi: ikki "
            "oʻlchovdan «bir soatga necha daraja» qanday chiqariladi va u nimani "
            "bildiradi."
        ),
        "order":   5,
        "grammar": [
            {
                "pattern":  "the rate of change",
                "meaning":  "Oʻzgarish tezligi — qiyalikning ikkinchi nomi. Har doim "
                            "<b>«bir birlikka qancha»</b> degan savolga javob beradi.",
                "examples": ["The rate of change was two degrees per hour."],
            },
            {
                "pattern":  "steadily / at a steady rate",
                "meaning":  "Bir tekisda. Yaʼni oʻzgarish har soatda bir xil — chiziqli "
                            "model.",
                "examples": ["The temperature fell steadily all afternoon."],
            },
            {
                "pattern":  "steeper",
                "meaning":  "Tikroq. Grafikda tikroq chiziq — <b>tezroq</b> oʻzgarish "
                            "degani, kattaroq boshlangʻich qiymat emas.",
                "examples": ["The line for the first station is steeper than the second."],
            },
        ],
        "body": '''<p>Two <span class="cn-word" data-tr="ob-havo stansiyasi">weather stations</span> stand about nine kilometres <span class="cn-word" data-tr="bir-biridan uzoqlikda">apart</span>, one on the roof of a school in the city and one on a <span class="cn-word" data-tr="tepalik">hill</span> above the <span class="cn-word" data-tr="suv ombori">reservoir</span>. On the last Thursday of September they recorded the same afternoon, and the two <span class="cn-word" data-tr="qator, yozuv">records</span> read very differently.</p>

<p>The city station was at thirty-one degrees at two in the afternoon and nineteen degrees at eight in the evening. Six hours, twelve degrees. The <span class="cn-word" data-tr="byulleten, xabarnoma">bulletin</span> said the temperature had fallen <strong>steadily</strong>, so the fall belonged to each hour equally: two degrees an hour, <span class="cn-word" data-tr="har soatda">hour after hour</span>. At five o'clock, three hours in, the <span class="cn-word" data-tr="oʻlchov, koʻrsatkich">reading</span> was twenty-five degrees, exactly as that <strong>rate of change</strong> <span class="cn-word" data-tr="bashorat qiladi">predicts</span>.</p>

<p>The hill station started cooler and ended warmer: twenty-nine degrees at two, twenty-three at eight. The same six hours, but only six degrees — one degree an hour.</p>

<p>Drawn on the same <span class="cn-word" data-tr="oʻq, koordinata oʻqi">axes</span>, the two records are two straight lines going down, and the city's line is the <strong>steeper</strong> one. That word is doing real work. It does not say the city was hotter, although at two o'clock it was. It says the city <span class="cn-word" data-tr="sovidi">cooled</span> faster.</p>

<p>A <span class="cn-word" data-tr="meteorolog">forecaster</span> reading those two lines is not really looking at temperatures at all. She is looking at how fast each number is moving, which is the only part of the picture that tells her what tonight will be like.</p>''',
        "questions": [
            {
                "text": "What was the city station's rate of change that afternoon?",
                "choices": [
                    "A fall of 2 degrees per hour",
                    "A fall of 6 degrees per hour",
                    "A fall of 12 degrees per hour",
                ],
                "answer": 0,
                "explanation": "31 − 19 = 12 daraja, 6 soat ichida: 12 ÷ 6 = <b>2</b> "
                               "daraja soatiga. <b>12</b> — butun oʻzgarish, uni "
                               "vaqtga boʻlish kerak.",
            },
            {
                "text": "According to the text, what was the city reading at five o'clock?",
                "choices": ["23 degrees", "25 degrees", "27 degrees"],
                "answer": 1,
                "explanation": "Soat 14:00 dan 3 soat oʻtdi, har soat 2 daraja: "
                               "31 − 3 × 2 = <b>25</b>. <b>23</b> — tepalik "
                               "stansiyasining soat 20:00 dagi koʻrsatkichi.",
            },
            {
                "text": "What does it mean that the city's line is steeper?",
                "choices": [
                    "The city was warmer at two o'clock.",
                    "The city cooled more quickly than the hill.",
                    "The city was measured for a longer time.",
                ],
                "answer": 1,
                "explanation": "Tiklik — <b>tezlik</b>, boshlangʻich qiymat emas. "
                               "Shahar soat 14:00 da issiqroq ham edi, lekin tiklikning "
                               "aytayotgani bu emas: u tezroq sovigan.",
            },
        ],
    },
]
