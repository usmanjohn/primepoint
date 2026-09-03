# -*- coding: utf-8 -*-
"""Prime SAT Readings — SAT-6 … SAT-10 (batch 2).

Har bir matn oʻz darsiga tegishli, `order` = dars raqami.
Written with STYLE_GUIDE_CORNER.md + the overrides in toc_prime_sat_readings.txt

  6  — a museum notice about a ramp      (SAT-6: two points -> a gradient)
  7  — a community pool's pass notice    (SAT-7: a fixed fee plus a rate)
  8  — a radio show's running order      (SAT-8: two kinds of minute adding to a total)
  9  — a cycling coach's training log    (SAT-9: two dots and a straight line)
  10 — a newspaper answers a reader      (SAT-10: what the 62 cents actually means)

Genre rotation — batch 1 used: a cafe order sheet, a lab report, committee minutes,
a quality-control report, a news item. None of those repeat here.

⛔ NO ALGEBRAIC NOTATION IN THE BODY — quantities in English, units spelled out.
⚠️ Matn inglizcha; summary, glossalar, meaning va explanation oʻzbekcha.

NARRATOR VOICE (batch 1 ran 3 female / 2 male, so this one flips):
    6 en-US-GuyNeural   · 7 en-US-JennyNeural · 8 en-US-GuyNeural
    9 en-US-JennyNeural · 10 en-US-GuyNeural

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_06_10.py --author=prime
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
    # SAT-6 — slope from two points                               [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Ramp at the Side Door",
        "summary": (
            "SAT-6 matni. Muzey eshigi oldidagi pandus: koʻtarilish va uzunlik "
            "ikkita son, ular orasidagi nisbat esa qonun talab qiladigan qiyalik."
        ),
        "order":   6,
        "grammar": [
            {
                "pattern":  "for every … it rises …",
                "meaning":  "Har … uchun shuncha koʻtariladi. Qiyalikning soʻz bilan "
                            "aytilishi: birinchi son — <b>run</b>, ikkinchisi — "
                            "<b>rise</b>.",
                "examples": ["For every twelve centimetres of length, it rises one.",
                             "For every kilometre, the road climbs 25 metres."],
            },
            {
                "pattern":  "one in twelve",
                "meaning":  "Bir bo‘lak koʻtarilishga oʻn ikki boʻlak uzunlik — "
                            "yaʼni qiyalik 1 ÷ 12. Nisbat har doim "
                            "<b>koʻtarilish : uzunlik</b> tartibida oʻqiladi.",
                "examples": ["The gradient must not be steeper than one in twelve."],
            },
            {
                "pattern":  "steeper than",
                "meaning":  "…dan tikroq. Diqqat: 1 ÷ 8 nisbati 1 ÷ 12 dan "
                            "<b>tikroq</b>, garchi 8 soni 12 dan kichik boʻlsa ham.",
                "examples": ["A ramp of one in eight is steeper than one in twelve."],
            },
        ],
        "body": '''<p>A small local museum spent two years arguing about a door.</p>

<p>The side entrance, the one nearest the car park, sits 30 centimetres above the path. For anyone using a wheelchair, or pushing a pram, or carrying a heavy case, those 30 centimetres are a wall. The building's own front steps are protected, so the only place a <span class="cn-word" data-tr="pandus, qiya yoʻlak">ramp</span> could go was the side.</p>

<p>The first <span class="cn-word" data-tr="loyiha, chizma">design</span> was rejected in a single afternoon. It reached the door in 240 centimetres of <span class="cn-word" data-tr="uzunlik">length</span>, which sounded efficient and was, in fact, illegal. Thirty centimetres of <span class="cn-word" data-tr="koʻtarilish">rise</span> spread over 240 centimetres gives a <span class="cn-word" data-tr="qiyalik, nishablik">gradient</span> of one in eight: <strong>for every</strong> eight centimetres forward, the surface climbs one. That is <strong>steeper than</strong> a person can safely push themselves up, and steeper than the <span class="cn-word" data-tr="qurilish meʼyori">building code</span> allows.</p>

<p>The rule the <span class="cn-word" data-tr="meʼmor">architect</span> was working to is simple to say and expensive to obey: no ramp may be steeper than <strong>one in twelve</strong>. Thirty centimetres of rise therefore needs 360 centimetres of length — three and a half metres of concrete instead of two and a half, and a <span class="cn-word" data-tr="burilish maydonchasi">turning platform</span> at the bottom that the first design had no room for.</p>

<p>The finished ramp opened last spring. Two brass <span class="cn-word" data-tr="qadama, mixcha">studs</span> are set into it, one at the path and one at the door, and a small <span class="cn-word" data-tr="lavha, yozuv">plaque</span> between them gives their heights: 0 and 30. A visitor once asked the <span class="cn-word" data-tr="qorovul, qarovchi">attendant</span> what the studs were for.</p>

<p>«Two points,» he said. «Everything else about this ramp comes out of those two <span class="cn-word" data-tr="oʻlchov">measurements</span>.»</p>''',
        "questions": [
            {
                "text": "What is the gradient of the finished ramp?",
                "choices": ["One in eight", "One in twelve", "One in thirty"],
                "answer": 1,
                "explanation": "30 sm koʻtarilish 360 sm uzunlikka taqsimlanadi: "
                               "360 ÷ 30 = 12, yaʼni <b>bir in oʻn ikki</b>. "
                               "«Bir in sakkiz» — rad etilgan birinchi loyiha.",
            },
            {
                "text": "How much longer is the finished ramp than the rejected design?",
                "choices": ["120 centimetres", "30 centimetres", "240 centimetres"],
                "answer": 0,
                "explanation": "360 − 240 = <b>120</b> santimetr. Koʻtarilish oʻzgarmadi "
                               "(30 sm boʻlib qoldi) — faqat uzunlik uzaydi, chunki "
                               "qiyalikni yotiqroq qilishning yagona yoʻli shu.",
            },
            {
                "text": "Why is a gradient of one in eight steeper than one in twelve?",
                "choices": [
                    "Because eight is a smaller number than twelve.",
                    "Because the ramp is shorter than the door is high.",
                    "Because the same rise is spread over a shorter length.",
                ],
                "answer": 2,
                "explanation": "Ikkala pandusda ham koʻtarilish bir xil — 30 sm. Farqi "
                               "shundaki, birinchisida u <b>qisqaroq</b> masofaga "
                               "taqsimlanadi, shuning uchun har qadamga koʻproq "
                               "koʻtarilish toʻgʻri keladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-7 — slope-intercept in context                        [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Forty Dollars and Three More",
        "summary": (
            "SAT-7 matni. Basseyndagi eʼlon: yozgi abonement va har safargi toʻlov. "
            "Bir martalik son va takrorlanadigan son — modelning ikki qismi."
        ),
        "order":   7,
        "grammar": [
            {
                "pattern":  "a one-time fee of",
                "meaning":  "Bir martalik toʻlov. Modelda u <b>yolgʻiz</b> turadi va "
                            "hech narsaga koʻpaymaydi.",
                "examples": ["The pass costs a one-time fee of $40."],
            },
            {
                "pattern":  "each visit / per visit",
                "meaning":  "Har bir tashrif uchun. Bu son tashriflar soniga "
                            "<b>koʻpayadi</b> — modelning qiyaligi.",
                "examples": ["Pass holders pay $3 for each visit."],
            },
            {
                "pattern":  "works out cheaper",
                "meaning":  "Arzonroqqa tushadi. Ikki modelni taqqoslaganda javob "
                            "<b>nechta</b> ekaniga bogʻliq — bitta narx hamma uchun "
                            "toʻgʻri emas.",
                "examples": ["Above eight visits, the pass works out cheaper."],
            },
        ],
        "body": '''<p>The <span class="cn-word" data-tr="eʼlon">notice</span> taped to the glass at the community pool has been there since June, and it is the clearest piece of writing in the building.</p>

<p><span class="cn-word" data-tr="kirish, bir marta kirish">ENTRY</span> WITHOUT A PASS: $8 each visit.<br>
SUMMER <span class="cn-word" data-tr="abonement, chipta">PASS</span>: $40, then $3 each visit.</p>

<p>Underneath, somebody on the <span class="cn-word" data-tr="xodimlar">staff</span> has added a line in <span class="cn-word" data-tr="qoʻlyozma">handwriting</span>: <em>«Ask us which one is better for you. It depends how often you swim.»</em></p>

<p>That sentence is doing real mathematical work. The pass has two parts, and they behave completely differently. The $40 is <strong>a one-time fee of</strong> forty dollars: you pay it in June whether you swim once or fifty times, and it never comes back. The $3 is a <span class="cn-word" data-tr="stavka, narx meʼyori">rate</span> — it arrives again <strong>each visit</strong>, and it is the only part of the pass that grows.</p>

<p>So the <span class="cn-word" data-tr="hisob-kitob">arithmetic</span> is not one sum but two. A swimmer who comes twelve times over the summer pays forty dollars once and three dollars twelve times: $76 <span class="cn-word" data-tr="hammasi boʻlib">altogether</span>. Without the pass, twelve visits cost $96. Someone who comes only five times pays $55 with the pass and $40 without it, and has <span class="cn-word" data-tr="ortiqcha toʻlagan">overpaid</span> for the <span class="cn-word" data-tr="imtiyoz">privilege</span>.</p>

<p>The <span class="cn-word" data-tr="chegara nuqtasi">turning point</span> is exactly eight visits, where both routes cost $64 and the choice stops mattering. Below eight, pay at the door. Above eight, the pass <strong>works out cheaper</strong>, and every visit after that saves five dollars.</p>

<p>The <span class="cn-word" data-tr="qabulxona, kassa">reception</span> desk gets the same question forty times a week. The answer is never a number. It is another question: <em>how often?</em></p>''',
        "questions": [
            {
                "text": "What does a pass holder pay in total for twelve visits?",
                "choices": ["$36", "$76", "$96"],
                "answer": 1,
                "explanation": "$40 bir marta + 12 × $3 = $36, jami <b>$76</b>. "
                               "<b>$96</b> — abonementsiz narx (12 × $8), <b>$36</b> — "
                               "bir martalik $40 ni unutgan javob.",
            },
            {
                "text": "How much does a swimmer save with the pass on their twelfth visit compared with paying at the door?",
                "choices": ["$20", "$5", "$40"],
                "answer": 0,
                "explanation": "$96 − $76 = <b>$20</b>. <b>$5</b> — bitta tashrifdagi "
                               "farq ($8 − $3), butun yozniki emas: savol jami "
                               "tejamkorlikni soʻradi.",
            },
            {
                "text": "According to the notice, why can the staff not simply say which option is better?",
                "choices": [
                    "Because the prices change during the summer.",
                    "Because the pass is sold out after eight visits.",
                    "Because the answer depends on the number of visits.",
                ],
                "answer": 2,
                "explanation": "Modelda bir martalik toʻlov ham, har safargi toʻlov ham "
                               "bor. Sakkiz tashrifdan kam boʻlsa — eshikda toʻlash "
                               "arzon, koʻp boʻlsa — abonement. Javob <b>sonlar</b>ga "
                               "emas, <b>necha marta</b> degan savolga bogʻliq.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-8 — standard form in context                            [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Sixty Minutes, Two Kinds of Minute",
        "summary": (
            "SAT-8 matni. Radio koʻrsatuvining tartibi: qoʻshiq ikki daqiqa, suhbat "
            "besh daqiqa, jami oltmish. Ikki xil birlik bitta yigʻindiga qoʻshiladi."
        ),
        "order":   8,
        "grammar": [
            {
                "pattern":  "must add up to",
                "meaning":  "Yigʻindisi shunga teng boʻlishi shart. Ikki xil miqdor "
                            "bitta umumiy songa qoʻshilganda model "
                            "<b>Ax + By = C</b> koʻrinishida boʻladi.",
                "examples": ["The two kinds of item must add up to sixty minutes."],
            },
            {
                "pattern":  "each lasting",
                "meaning":  "Har biri shuncha davom etadigan. Bu son "
                            "<b>koeffitsient</b>: har bir birlik qancha vaqt "
                            "(yoki pul) olishini bildiradi.",
                "examples": ["Songs, each lasting two minutes, and interviews, each lasting five."],
            },
            {
                "pattern":  "whole number",
                "meaning":  "Butun son. Sanaladigan narsalarda javob butun boʻlishi "
                            "shart — yarim qoʻshiq efirga chiqmaydi.",
                "examples": ["The number of songs has to be a whole number."],
            },
        ],
        "body": '''<p>Every weekday at a small radio station, somebody has to solve the same <span class="cn-word" data-tr="jumboq">puzzle</span> before ten in the morning, and they solve it on the back of a <span class="cn-word" data-tr="konvert">envelope</span>.</p>

<p>The programme is sixty minutes long, and it is built out of exactly two things. Songs run two minutes each. <span class="cn-word" data-tr="suhbat, intervyu">Interviews</span> run five. The <span class="cn-word" data-tr="efir tartibi">running order</span> can hold any mixture of the two, but the total <strong>must add up to</strong> sixty minutes, because at eleven o'clock the news begins whether the <span class="cn-word" data-tr="boshlovchi">presenter</span> has finished or not.</p>

<p>Yesterday's show had four interviews. Four interviews, <strong>each lasting</strong> five minutes, take twenty minutes of the hour, which leaves forty minutes of music — and forty minutes of two-minute songs is twenty songs. The <span class="cn-word" data-tr="ishlab chiqarish, tayyorlash">production</span> assistant wrote «4 and 20» on the envelope and went to make tea.</p>

<p>Today there are only two interviews <span class="cn-word" data-tr="rejalashtirilgan">scheduled</span>. Ten minutes of talk leaves fifty minutes of music, which is twenty-five songs — five more <span class="cn-word" data-tr="yozuv, plastinka">records</span> to find before ten o'clock.</p>

<p>What the assistant never does is <span class="cn-word" data-tr="taxmin qilmoq">guess</span>. She is not choosing songs and interviews <span class="cn-word" data-tr="alohida, mustaqil ravishda">independently</span>: the moment the number of interviews is fixed, the number of songs is decided for her, because the hour cannot stretch.</p>

<p>Two things follow, and she has both written on the wall. The answer is always a <strong>whole number</strong> — nobody <span class="cn-word" data-tr="efirga uzatmoq">broadcasts</span> half a song. And there is a <span class="cn-word" data-tr="chegara">limit</span> to interviews: twelve of them would fill the hour by themselves and leave a programme with no music in it at all.</p>''',
        "questions": [
            {
                "text": "Today's show has two interviews. How many songs does it need?",
                "choices": ["20 songs", "30 songs", "25 songs"],
                "answer": 2,
                "explanation": "Ikki suhbat 2 × 5 = 10 daqiqa. Qolgan 60 − 10 = 50 "
                               "daqiqa musiqa, va 50 ÷ 2 = <b>25</b> ta qoʻshiq. "
                               "<b>20</b> — kechagi koʻrsatuvniki (toʻrt suhbat bilan).",
                
            },
            {
                "text": "How many interviews would fill the whole hour with no songs at all?",
                "choices": ["Twelve", "Ten", "Thirty"],
                "answer": 0,
                "explanation": "60 ÷ 5 = <b>12</b> ta suhbat. <b>30</b> — bu faqat "
                               "qoʻshiqlar bilan toʻldirilgan soat (60 ÷ 2), suhbatlar "
                               "emas: har bir birlikning oʻz uzunligi bor.",
            },
            {
                "text": "Why can the assistant not choose the number of songs freely once the interviews are fixed?",
                "choices": [
                    "Because the station owns a limited number of records.",
                    "Because the two amounts must together make exactly sixty minutes.",
                    "Because interviews are always recorded before the songs.",
                ],
                "answer": 1,
                "explanation": "Jami vaqt qatʼiy: 60 daqiqa. Suhbatlar soni "
                               "belgilangach, qolgan vaqt ham, demak qoʻshiqlar soni "
                               "ham oʻz-oʻzidan aniqlanadi — <b>ikkinchisi birinchisiga "
                               "bogʻliq</b>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-9 — two points, one line                              [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Coach Who Drew Two Dots",
        "summary": (
            "SAT-9 matni. Velosiped murabbiysi butun mavsumni ikki nuqta bilan "
            "chizadi — va uchinchi nuqtaga umuman ehtiyoj yoʻq."
        ),
        "order":   9,
        "grammar": [
            {
                "pattern":  "two points are enough",
                "meaning":  "Ikki nuqta yetarli. Chiziqli oʻsishda uchinchi "
                            "oʻlchov faqat <b>tekshiruv</b> uchun kerak.",
                "examples": ["For a straight line, two points are enough."],
            },
            {
                "pattern":  "at this rate",
                "meaning":  "Shu tezlikda davom etsa. Bu ibora modelning kelajakka "
                            "ham amal qilishini <b>faraz</b> qiladi — va bu faraz "
                            "har doim ham toʻgʻri emas.",
                "examples": ["At this rate, she will reach 100 kilometres in week 13."],
            },
            {
                "pattern":  "falls on the line",
                "meaning":  "Chiziq ustiga tushadi. Nuqta modelga mos kelsa shunday "
                            "deyiladi; mos kelmasa — <em>off the line</em>.",
                "examples": ["Week six falls exactly on the line."],
            },
        ],
        "body": '''<p>The cycling coach at a sports school keeps her whole season on one sheet of <span class="cn-word" data-tr="katakli qogʻoz">squared paper</span>, and she fills in almost none of it.</p>

<p>At the start of the season — week zero, before the first training block — her rider covered 20 kilometres in the week. In week ten she covered 80. Those are the only two numbers the coach wrote down before she picked up a <span class="cn-word" data-tr="chizgʻich">ruler</span>, put a dot at each of them and joined the dots with a single straight line.</p>

<p>«<strong>Two points are enough</strong>,» she says, when a new <span class="cn-word" data-tr="yordamchi">assistant</span> asks where the rest of the <span class="cn-word" data-tr="maʼlumot">data</span> is. «If the training is working, the weeks in between are already on that line.»</p>

<p>They mostly are. Sixty kilometres of increase, spread evenly over ten weeks, is six kilometres a week, and the rider's actual <span class="cn-word" data-tr="haftalik masofa">weekly distance</span> in week five was 50 — which <strong>falls on the line</strong> exactly. Week six was 55, one kilometre off, and the coach has drawn a small circle round it and written <em>«wind»</em> in the <span class="cn-word" data-tr="chekka, hoshiya">margin</span>.</p>

<p>The straight line does two jobs. It <span class="cn-word" data-tr="silliqlashtirmoq">smooths</span> the <span class="cn-word" data-tr="tasodifiy ogʻish">noise</span> of any single week — a cold morning, a <span class="cn-word" data-tr="teshilgan gʻildirak">puncture</span>, a school exam — and it makes a <span class="cn-word" data-tr="bashorat">prediction</span> that can be tested: <strong>at this rate</strong>, week fifteen should be 110 kilometres.</p>

<p>The coach is careful about that second job. A line drawn through two dots will happily run off the top of the page, she says, and no rider improves for ever. The line is a <span class="cn-word" data-tr="qoʻpol, taxminiy">rough</span> plan, not a promise. What it is very good at is showing, in one glance, the week when a rider stops keeping up with their own <span class="cn-word" data-tr="oʻsish sur'ati">rate of progress</span>.</p>''',
        "questions": [
            {
                "text": "By how many kilometres does the rider's weekly distance increase each week?",
                "choices": ["6 kilometres", "8 kilometres", "60 kilometres"],
                "answer": 0,
                "explanation": "Ikki nuqta: 0-hafta 20 km, 10-hafta 80 km. "
                               "Oʻsish 80 − 20 = 60 km, oʻtgan vaqt 10 hafta: "
                               "60 ÷ 10 = <b>6</b> km har haftada. <b>60</b> — butun "
                               "oʻsish, haftalik emas.",
            },
            {
                "text": "What distance does the line predict for week fifteen?",
                "choices": ["90 kilometres", "120 kilometres", "110 kilometres"],
                "answer": 2,
                "explanation": "Matnda aytilgan: <b>110</b> km. Tekshiruv: 10-haftada "
                               "80 km edi, yana besh hafta × 6 km = 30, "
                               "80 + 30 = 110.",
            },
            {
                "text": "Why has the coach circled week six?",
                "choices": [
                    "Because the rider did not train that week.",
                    "Because the distance did not fall exactly on the line.",
                    "Because it was the best week of the season.",
                ],
                "answer": 1,
                "explanation": "6-haftada 55 km — chiziq bashorat qilgan qiymatdan bir "
                               "kilometr chetda. Murabbiy uni <b>istisno</b> deb "
                               "belgilab, sababini («shamol») yozib qoʻygan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-10 — what a number means                                [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "What Does the 62 Cents Mean?",
        "summary": (
            "SAT-10 matni. Gazetaning savol-javob boʻlimi: oʻquvchi kuryerlik "
            "narxidagi ikki sonni tushunmaydi — va aynan shu savolni SAT ham beradi."
        ),
        "order":   10,
        "grammar": [
            {
                "pattern":  "the base fee",
                "meaning":  "Asosiy (boshlangʻich) toʻlov. Masofadan qatʼi nazar "
                            "toʻlanadi — modelda yolgʻiz turadigan son.",
                "examples": ["The base fee is $4.50, whatever the distance."],
            },
            {
                "pattern":  "for each additional kilometre",
                "meaning":  "Har bir qoʻshimcha kilometr uchun. Bu — "
                            "<b>oʻzgarish</b>, jami emas.",
                "examples": ["You pay 62 cents for each additional kilometre."],
            },
            {
                "pattern":  "that is not the same as",
                "meaning":  "Bu … bilan bir xil emas. Interpretatsiya savollarida "
                            "eng muhim jumla shu: ikki maʼnoni ajratadi.",
                "examples": ["62 cents a kilometre is not the same as 62 cents a delivery."],
            },
        ],
        "body": '''<p><em>Our readers ask.</em> A reader in the old town writes: «The courier's price list says $4.50 plus 62 cents a kilometre. My neighbour says that means a one-kilometre delivery costs 62 cents. That cannot be right, because I was charged more. Which of us has misread it?»</p>

<p>Your neighbour has, and it is the most common <span class="cn-word" data-tr="notoʻgʻri tushunish">misreading</span> of any price list in the city.</p>

<p>There are two numbers on that <span class="cn-word" data-tr="narxlar roʻyxati">price list</span> and they do completely different jobs. The $4.50 is <strong>the base fee</strong>. It pays for the <span class="cn-word" data-tr="chaqiruv, buyurtma">call-out</span> — the rider coming to your door at all — and you pay it once, whether the <span class="cn-word" data-tr="posilka">parcel</span> travels one kilometre or nine.</p>

<p>The 62 cents is a <span class="cn-word" data-tr="stavka, narx meʼyori">rate</span>. It is charged <strong>for each additional kilometre</strong>, and it is the only part of the bill that moves. <strong>That is not the same as</strong> the price of a delivery. A one-kilometre delivery costs $4.50 plus 62 cents — that is $5.12, which is very likely the <span class="cn-word" data-tr="raqam">figure</span> on your <span class="cn-word" data-tr="chek, kvitansiya">receipt</span>.</p>

<p>Ten kilometres, by the same reading, costs $4.50 plus $6.20, or $10.70 in total. Notice what that does to the <span class="cn-word" data-tr="oʻrtacha">average</span>: your ten-kilometre parcel travelled at $1.07 a kilometre, and your one-kilometre parcel at $5.12 a kilometre, from the same price list. Neither of those averages is the 62 cents.</p>

<p>So the number in the <span class="cn-word" data-tr="reklama, eʼlon">advertisement</span> answers one question only: what happens to the bill when the <span class="cn-word" data-tr="safar, yoʻl">journey</span> gets one kilometre longer. It is a statement about <span class="cn-word" data-tr="oʻzgarish">change</span>, not about <span class="cn-word" data-tr="jami, umumiy">total</span> — and every argument we get letters about comes from mixing up those two.</p>''',
        "questions": [
            {
                "text": "What is the total cost of a one-kilometre delivery?",
                "choices": ["$0.62", "$4.50", "$5.12"],
                "answer": 2,
                "explanation": "$4.50 + $0.62 = <b>$5.12</b>. <b>$0.62</b> — "
                               "qoʻshnining xatosi: u faqat stavkani olgan, asosiy "
                               "toʻlovni qoʻshmagan.",
            },
            {
                "text": "What is the total cost of a ten-kilometre delivery?",
                "choices": ["$6.20", "$10.70", "$45.00"],
                "answer": 1,
                "explanation": "$4.50 + 10 × $0.62 = 4.50 + 6.20 = <b>$10.70</b>. "
                               "<b>$6.20</b> — faqat masofa uchun toʻlov, asosiy "
                               "toʻlovsiz.",
            },
            {
                "text": "According to the column, what does the 62 cents actually describe?",
                "choices": [
                    "The amount the bill grows when the journey is one kilometre longer.",
                    "The average cost of every kilometre travelled.",
                    "The cheapest delivery the company offers.",
                ],
                "answer": 0,
                "explanation": "Matn buni aniq aytadi: bu <b>oʻzgarish</b> haqidagi son, "
                               "jami haqidagi emas. Oʻrtacha narx esa masofaga qarab "
                               "oʻzgaradi — 1 km da $5.12, 10 km da $1.07.",
            },
        ],
    },
]
