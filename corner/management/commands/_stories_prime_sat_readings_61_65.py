# -*- coding: utf-8 -*-
"""Prime SAT Readings — 61–65 (SAT-61 … SAT-65 darslariga).

Written with the overrides in corner/management/commands/toc_prime_sat_readings.txt
⛔ MATNDA ALGEBRAIK BELGI YOʻQ — miqdorlar faqat ingliz tilida, soʻz bilan.

Til: matn, sarlavha va savollar INGLIZCHA; summary, cn-word glosslari,
     "Exam English" izohlari va javob tushuntirishlari OʻZBEKCHA.

Ovozlar (13-batch ayoldan boshlanadi): 61 Jenny · 62 Guy · 63 Jenny ·
                                       64 Guy · 65 Jenny

Import:
    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_61_65.py --author=prime
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

    # ── 61 · the armour problem ──────────────────────────────────────
    {
        "title": "Where the Bullet Holes Were Not",
        "order": 61,
        "summary": (
            "Qaytib kelgan samolyotlardagi teshiklar qayerda ekanini sanashdi — "
            "va zirhni notoʻgʻri joyga qoʻyishga oz qoldi."
        ),
        "body": """
<p>During the Second World War, engineers examined
<span class="cn-word" data-tr="samolyotlar">aircraft</span> returning from missions and recorded
where each one had been <span class="cn-word" data-tr="urilgan">hit</span>. The pattern was
clear: many holes along the wings and the body, far fewer around the
<span class="cn-word" data-tr="dvigatel">engines</span>.</p>

<p>The obvious <span class="cn-word" data-tr="tavsiya">recommendation</span> was to add
<span class="cn-word" data-tr="zirh">armour</span> where the holes were. That is where the
aircraft were being hit, so that is where the
<span class="cn-word" data-tr="himoya">protection</span> was needed.</p>

<p>A <span class="cn-word" data-tr="matematik">mathematician</span> working with the group asked
one question that changed the recommendation
<span class="cn-word" data-tr="butunlay">completely</span>. Which aircraft, he asked, are in
this <span class="cn-word" data-tr="maʼlumot">data</span>?</p>

<p>Only the ones that came back. An aircraft hit in the engines had a poor chance of returning at
all, so it never reached the yard where the counting was done. The
<span class="cn-word" data-tr="deyarli boʻsh">near-empty</span> areas on the diagram were not
the safe places. They were the places where a hit meant the aircraft was
<span class="cn-word" data-tr="yoʻqolgan">lost</span>.</p>

<p>The armour went on the engines.</p>

<p>The point was not that the engineers had counted badly. Their counting was exact. What they had not asked was which aircraft the yard could ever have received.</p>

<p>The <span class="cn-word" data-tr="xato">error</span> the engineers nearly made has a name now
— it is what happens whenever a group is studied after something has already
<span class="cn-word" data-tr="filtrlab olmoq">filtered</span> it. Successful companies,
finished buildings, patients who recovered enough to attend a follow-up: each of these is a
sample chosen by <span class="cn-word" data-tr="omon qolish">survival</span>, and the cases that
matter most are the ones that are <span class="cn-word" data-tr="yoʻq">absent</span>.</p>
""",
        "grammar": [
            {"pattern": "which aircraft are in this data?",
             "meaning": "bu maʼlumotda qaysi samolyotlar bor — tanlanma savoli"},
            {"pattern": "only the ones that came back",
             "meaning": "faqat qaytib kelganlari — ogʻishning manbai"},
            {"pattern": "the cases that matter most are absent",
             "meaning": "eng muhim holatlar yoʻq"},
        ],
        "questions": [
            {"text": "What did the engineers first recommend?",
             "choices": ["Armouring the engines",
                         "Armouring the places where the holes were",
                         "Flying at a different altitude",
                         "Building lighter aircraft"],
             "answer": 1,
             "explanation": "Teshiklar koʻp boʻlgan joylarga zirh qoʻyish — "
                            "tabiiy, lekin notoʻgʻri xulosa."},
            {"text": "Why were there few holes around the engines?",
             "choices": ["The engines were rarely hit",
                         "The engines were already armoured",
                         "Aircraft hit there usually did not return to be counted",
                         "The holes were hard to see"],
             "answer": 2,
             "explanation": "Dvigateliga tekkan samolyotlar qaytib kelmagan, "
                            "shuning uchun ular sanoqqa tushmagan."},
            {"text": "What do successful companies and recovered patients have in common "
                     "with the returning aircraft?",
             "choices": ["Each is a group already filtered by survival",
                         "Each is easy to measure",
                         "Each is a random sample",
                         "Each is very large"],
             "answer": 0,
             "explanation": "Ularning hammasi omon qolish orqali saralangan "
                            "guruh — eng muhim holatlar esa yoʻq."},
        ],
    },

    # ── 62 · medical history ─────────────────────────────────────────
    {
        "title": "Twelve Sailors, Six Pairs",
        "order": 62,
        "summary": (
            "1747-yilda bir kema shifokori oʻn ikki kasal dengizchini olti "
            "juftga boʻldi — va taqqoslash gʻoyasi shu yerdan boshlandi."
        ),
        "body": """
<p>In 1747 a naval <span class="cn-word" data-tr="shifokor">surgeon</span> named James Lind was
at sea with a crew suffering from <span class="cn-word" data-tr="singa (kasallik)">scurvy</span>,
a disease that killed more sailors in that century than
<span class="cn-word" data-tr="jang">battle</span> did. Nobody knew its cause. Everybody had a
<span class="cn-word" data-tr="davo, dori">remedy</span>, and all the remedies had
<span class="cn-word" data-tr="tarafdorlar">supporters</span>.</p>

<p>Lind did something unusual. He took twelve sick men whose cases were as
<span class="cn-word" data-tr="oʻxshash">similar</span> as he could find, kept them in the same
part of the ship on the same <span class="cn-word" data-tr="ovqat, ratsion">diet</span>, and
divided them into six pairs. Each pair received one of the six remedies, and nothing else was
allowed to <span class="cn-word" data-tr="farq qilmoq">differ</span>.</p>

<p>The pair given oranges and lemons recovered so quickly that one of them was back on duty
within a week.</p>

<p>What made this work was not the fruit. It was the
<span class="cn-word" data-tr="tuzilish, tartib">structure</span>. Six remedies had been argued
about for years by comparing them with <span class="cn-word" data-tr="hech narsa">nothing</span>
— each doctor remembering the patients who recovered under his own care. Lind compared them with
<span class="cn-word" data-tr="bir-biri">each other</span>, at the same time, under the same
conditions.</p>

<p>One piece was still missing. Lind chose which pair got which remedy; he did not decide it by
<span class="cn-word" data-tr="tasodif">chance</span>. That last idea — letting a coin
<span class="cn-word" data-tr="taqsimlamoq">assign</span> the groups, so that even the
differences nobody has thought of are spread evenly — arrived roughly two hundred years later,
and it is what turns a careful comparison into a
<span class="cn-word" data-tr="isbot, dalil">proof</span> of cause.</p>
""",
        "grammar": [
            {"pattern": "nothing else was allowed to differ",
             "meaning": "boshqa hech narsa farq qilmasligi kerak — nazorat"},
            {"pattern": "compared them with each other",
             "meaning": "bir-biri bilan taqqosladi — nazorat guruhlari"},
            {"pattern": "letting a coin assign the groups",
             "meaning": "guruhlarni tanga taqsimlasin — tasodifiy taqsimlash"},
        ],
        "questions": [
            {"text": "How did Lind organise the twelve men?",
             "choices": ["Six pairs, each pair given a different remedy",
                         "Two groups of six",
                         "Twelve separate treatments",
                         "One group, all given fruit"],
             "answer": 0,
             "explanation": "Oʻn ikki kishi olti juftga boʻlingan va har bir "
                            "juftga bitta davo berilgan."},
            {"text": "What made the trial work?",
             "choices": ["The fruit itself",
                         "The number of sailors",
                         "Comparing the remedies with each other under the same conditions",
                         "The length of the voyage"],
             "answer": 2,
             "explanation": "Matn buni aniq aytadi: ish qilgan narsa meva emas, "
                            "tuzilish — bir vaqtda, bir xil sharoitda "
                            "taqqoslash."},
            {"text": "What was still missing from Lind's method?",
             "choices": ["Assigning the pairs by chance rather than by choice",
                         "A larger number of patients",
                         "A written record",
                         "A second doctor"],
             "answer": 0,
             "explanation": "Lind kim nimani olishini oʻzi tanladi; tasodifiy "
                            "taqsimlash gʻoyasi ikki asr keyin keldi."},
        ],
    },

    # ── 63 · factory quality control ─────────────────────────────────
    {
        "title": "Two Percent, Give or Take",
        "order": 63,
        "summary": (
            "Nuqsonlar 3 foizdan 2 foizga tushdi — lekin ikkala natijaning "
            "oraliqlari kesishadi, demak yaxshilanish isbotlanmagan."
        ),
        "body": """
<p>The factory tests a random sample of a hundred items from each week's
<span class="cn-word" data-tr="ishlab chiqarish">production</span> and reports the share that
are <span class="cn-word" data-tr="nuqsonli">faulty</span>. Last month the figure was three
percent. This month it is two.</p>

<p>The <span class="cn-word" data-tr="menejer">manager</span> wrote to the team congratulating
them on a third fewer faults. The <span class="cn-word" data-tr="sifat nazorati">quality</span>
engineer asked him to look at the second column of the report first.</p>

<p>Each figure came with a margin of error of one and a half percent. So last month's true rate
was somewhere between one and a half and four and a half percent, and this month's is somewhere
between one half and three and a half. Those two
<span class="cn-word" data-tr="oraliqlar">ranges</span> overlap across most of their
<span class="cn-word" data-tr="uzunlik">length</span>. It is entirely possible that nothing at
all changed and the sample simply came out differently.</p>

<p>The engineer was not saying the improvement was
<span class="cn-word" data-tr="haqiqiy emas">unreal</span>. She was saying the numbers do not yet
show it, which is a different statement and the only honest one available.</p>

<p>The <span class="cn-word" data-tr="jamoa">team</span> had in fact worked hard that month, and the manager was right to notice. Being right and having <span class="cn-word" data-tr="dalil">evidence</span> are separate things.</p>

<p>Her <span class="cn-word" data-tr="taklif">proposal</span> was to test four hundred items a
week instead of a hundred. A larger sample narrows both ranges, and if the improvement is real it
will show as a <span class="cn-word" data-tr="boʻshliq">gap</span> between them within two
months.</p>

<p>She added one warning. Narrower ranges only help if the items are still chosen
<span class="cn-word" data-tr="tasodifiy">at random</span> from the whole week. Testing four
hundred items all from Monday morning would give a very
<span class="cn-word" data-tr="ishonchli koʻringan">confident</span> answer to the wrong
question.</p>
""",
        "grammar": [
            {"pattern": "give or take",
             "meaning": "u yoq-bu yogʻi bilan — xatolik chegarasi maʼnosida"},
            {"pattern": "the ranges overlap",
             "meaning": "oraliqlar kesishadi — farq isbotlanmagan"},
            {"pattern": "the numbers do not yet show it",
             "meaning": "raqamlar buni hali koʻrsatmayapti"},
        ],
        "questions": [
            {"text": "What are the two plausible ranges?",
             "choices": ["Three to four percent and two to three percent",
                         "One and a half to four and a half, and one half to three and a half",
                         "Exactly three percent and exactly two percent",
                         "They cannot be worked out"],
             "answer": 1,
             "explanation": "Har bir natijaga ikki tomondan bir yarim foizdan "
                            "qoʻshiladi va ayiriladi."},
            {"text": "What was the engineer actually saying?",
             "choices": ["The improvement is not real",
                         "The numbers do not yet show the improvement",
                         "The manager should be replaced",
                         "The margin of error was wrong"],
             "answer": 1,
             "explanation": "U yaxshilanishni inkor qilmadi — faqat raqamlar "
                            "uni hali tasdiqlamasligini aytdi."},
            {"text": "What was her warning about the larger sample?",
             "choices": ["It must still be chosen at random from the whole week",
                         "It would cost too much",
                         "Four hundred is not enough",
                         "It would take two months"],
             "answer": 0,
             "explanation": "Hammasi dushanba ertalabdan olinsa, oraliq tor "
                            "boʻladi, lekin javob notoʻgʻri savolga "
                            "tegishli boʻladi."},
        ],
    },

    # ── 64 · a business decision ─────────────────────────────────────
    {
        "title": "The Same Middle, a Different Tail",
        "order": 64,
        "summary": (
            "Ikki yetkazib berish xizmatining medianasi bir xil — biri esa "
            "baʼzan uch kun kechikadi. Farq quti diagrammada koʻrinadi."
        ),
        "body": """
<p>The shop had to choose between two <span class="cn-word"
data-tr="yetkazib berish xizmati">couriers</span>, and both had sent a year of delivery times.
Both had a <span class="cn-word" data-tr="mediana">median</span> of two days. On that number
there was nothing to choose between them.</p>

<p>The owner's daughter drew a box for each. The
<span class="cn-word" data-tr="quti">box</span> covers the middle half of the deliveries, and
for both couriers it ran from one day to three. Still
<span class="cn-word" data-tr="bir xil">identical</span>.</p>

<p>The difference was in the <span class="cn-word" data-tr="moʻylov, chiziqcha">whisker</span>
on the right. For the first courier it reached four days. For the second it reached
<span class="cn-word" data-tr="oʻn to'rt">fourteen</span>.</p>

<p>A quarter of every courier's deliveries lie in that upper whisker, however long it is. For the
first company that quarter is spread between three and four days — a
<span class="cn-word" data-tr="bir oz">slight</span> delay. For the second it is spread between
three and fourteen, which means some
<span class="cn-word" data-tr="mijozlar">customers</span> wait a fortnight.</p>

<p>She checked one more thing before recommending it: both companies had sent about the same <span class="cn-word" data-tr="miqdor">number</span> of deliveries, so the two pictures were built on comparable <span class="cn-word" data-tr="dalillar">evidence</span>.</p>

<p>The shop chose the first courier, and the owner explained why to his staff in one sentence:
the two companies are equally good on a
<span class="cn-word" data-tr="odatiy">typical</span> day, and only one of them is safe on a bad
one.</p>

<p>His daughter added a second reason. Nobody
<span class="cn-word" data-tr="shikoyat qilmoq">complains</span> about a typical delivery. The
<span class="cn-word" data-tr="obroʻ">reputation</span> of a shop is built almost entirely out
of its worst quarter.</p>
""",
        "grammar": [
            {"pattern": "the box covers the middle half",
             "meaning": "quti oʻrtadagi yarimni qamraydi"},
            {"pattern": "a quarter lie in that upper whisker",
             "meaning": "chorak qism yuqori moʻylovda yotadi"},
            {"pattern": "equally good on a typical day",
             "meaning": "odatiy kunda bir xil yaxshi — markaz bir xil"},
        ],
        "questions": [
            {"text": "What was identical about the two couriers?",
             "choices": ["Their medians and their boxes",
                         "Their maximum delivery times",
                         "Their whiskers",
                         "Their number of deliveries"],
             "answer": 0,
             "explanation": "Ikkalasining medianasi ikki kun, qutisi esa bir "
                            "kundan uch kungacha edi."},
            {"text": "What fraction of deliveries lie in the upper whisker?",
             "choices": ["A half", "A quarter", "A tenth", "It depends on its length"],
             "answer": 1,
             "explanation": "Har bir moʻylovda chorak qism yotadi — uzunligidan "
                            "qatʼi nazar."},
            {"text": "Why did the shop choose the first courier?",
             "choices": ["It was cheaper",
                         "Its median was lower",
                         "It was safe on a bad day, not just a typical one",
                         "It delivered more parcels"],
             "answer": 2,
             "explanation": "Odatiy kunda ikkalasi teng; farq eng yomon "
                            "chorakda — va obroʻ aynan oʻsha yerda quriladi."},
        ],
    },

    # ── 65 · public health ───────────────────────────────────────────
    {
        "title": "Two, Four, and Then What?",
        "order": 65,
        "summary": (
            "Ikki model birinchi ikki kunda bir xil sonni beradi. Uchinchi "
            "kunda ular ajraladi, oʻninchi kunda esa taqqoslab boʻlmaydi."
        ),
        "body": """
<p>The village clinic recorded two cases of an
<span class="cn-word" data-tr="yuqumli kasallik">infection</span> on Monday and four on Tuesday.
The nurse wrote both numbers on the board and asked the visiting
<span class="cn-word" data-tr="shifokor">doctor</span> what she expected on Wednesday.</p>

<p>The doctor said that was exactly the right question, and that two numbers were not enough to
answer it.</p>

<p>If the infection is adding two cases a day, Wednesday brings six, and by the tenth day the
<span class="cn-word" data-tr="jami">total</span> for that day is twenty. If it is doubling
instead, Wednesday brings eight, and by the tenth day it is more than a
<span class="cn-word" data-tr="ming">thousand</span>.</p>

<p>Both patterns produce two and four. They are
<span class="cn-word" data-tr="farqlab boʻlmaydigan">indistinguishable</span> on the first two
days, and they part company on the third. That is why the doctor wanted Wednesday's number
before she would say anything, and why she wanted Thursday's before she would
<span class="cn-word" data-tr="ishonmoq">trust</span> it.</p>

<p>She also warned the nurse against the opposite error. Three days of doubling does not mean the doubling <span class="cn-word" data-tr="davom etadi">continues</span>: infections run out of people to reach, just as the model runs out of <span class="cn-word" data-tr="asos">support</span> beyond the data.</p>

<p>The <span class="cn-word" data-tr="farq">difference</span> matters because the two answers
call for different <span class="cn-word" data-tr="tayyorgarlik">preparations</span>. Twenty
cases in a day is a busy clinic. A thousand is not a clinic
<span class="cn-word" data-tr="muammo">problem</span> at all; it is a district one, and the
request for help has to be sent while the numbers are still
<span class="cn-word" data-tr="kichik">small</span>.</p>

<p>Wednesday brought seven. That is one above the adding model and one below the doubling one, and it settles <span class="cn-word" data-tr="hech narsa">nothing</span> by itself. The doctor sent the <span class="cn-word" data-tr="xat, xabar">message</span> anyway, and said why: if she is wrong about doubling she has troubled the district office for nothing, and if she is right and waits, she has lost the only week in which the request was easy to answer.</p>
""",
        "grammar": [
            {"pattern": "adding two cases a day",
             "meaning": "kuniga ikkitadan qoʻshiladi — chiziqli"},
            {"pattern": "doubling instead",
             "meaning": "buning oʻrniga ikkilanadi — koʻrsatkichli"},
            {"pattern": "they part company on the third day",
             "meaning": "uchinchi kunda ajraladi — modellar farqlanadi"},
        ],
        "questions": [
            {"text": "What would each model predict for Wednesday?",
             "choices": ["Six if linear, eight if doubling",
                         "Six for both",
                         "Eight for both",
                         "It cannot be predicted"],
             "answer": 0,
             "explanation": "Kuniga ikkitadan qoʻshilsa olti; ikkilansa "
                            "sakkiz — uchinchi kunda modellar ajraladi."},
            {"text": "Why did the doctor refuse to answer on Tuesday?",
             "choices": ["The numbers were too small",
                         "Both patterns produce two and four",
                         "She needed to see the patients",
                         "The nurse had made an error"],
             "answer": 1,
             "explanation": "Birinchi ikki kunda ikkala model ham aynan bir xil "
                            "sonlarni beradi."},
            {"text": "Why did she send the message even though Wednesday's number settled "
                     "nothing?",
             "choices": ["The cost of waiting and being right is far worse than the cost of asking and being wrong",
                         "Seven proved the infection was doubling",
                         "The clinic was already full",
                         "She had promised to report weekly"],
             "answer": 0,
             "explanation": "Yetti ikkala modelga ham teng masofada — u hech "
                            "narsani hal qilmaydi. Qaror aniqlikdan emas, "
                            "ikki xatoning narxi teng emasligidan chiqadi."},
        ],
    },
]
