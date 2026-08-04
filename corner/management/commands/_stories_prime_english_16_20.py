# -*- coding: utf-8 -*-
"""Prime English Readings — PE-16 … PE-20 (batch 4).

PE-16 prepositions of place · PE-17 prepositions of time · PE-18 question words ·
PE-19 was / were · PE-20 past simple, regular verbs.

Two cumulative traps in this batch:
  * PE-19 teaches ONLY was / were, so its story keeps the narrating frame in the
    PRESENT (the grandfather "says", Dilnoza "asks") and puts the past inside the
    photograph, where was / were can carry it alone. No -ed verb appears yet.
  * PE-20 opens regular -ed past — but questions with "did" belong to PE-22, so the
    bakery story never asks one; it states.
Length curve steps up here: PE-19 and PE-20 run 130–170 words.

Rules: corner/management/commands/STYLE_GUIDE_CORNER.md
Story list: corner/management/commands/toc_prime_english_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_english_16_20.py --author=prime
"""

SUBJECT = {
    "name":    "English",
    "summary": "Ingliz tili: IELTS uslubidagi qiziqarli oʻqish matnlari — lugʻat va grammatika bilan.",
    "icon":    "bi-globe2",
    "color":   "#2563eb",
    "order":   2,
}

COLLECTION = {
    "title":       "Prime English Readings",
    "description": (
        "Prime English darslarining oʻqish matnlari — har bir matn oʻz darsining "
        "grammatikasini jonli holda koʻrsatadi. Lugʻat izohlari va audio bilan."
    ),
    "order":       6,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PE-16 — prepositions of place: in, on, at
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Shop on the Corner",
        "summary": (
            "PE-16 matni. Qizil jomadonli ayol nonvoyxonani soʻraydi va "
            "Afsona uni aniq yoʻlga soladi: in, on, at — va oxirida ayolning "
            "oʻz tuzatishi."
        ),
        "order":   16,
        "grammar": [
            {
                "pattern":  "in = inside · on = surface · at = point",
                "meaning":  "<b>in</b> — ichida (in the shop, in a bag). "
                            "<b>on</b> — ustida yoki chizigʻida (on the "
                            "shelf, on the corner). <b>at</b> — nuqta, "
                            "faoliyat joyi (at the bus stop, at the "
                            "bakery).",
                "examples": ["The shop is on the corner.",
                             "The bread is in the shop, on the second shelf.",
                             "A woman stands at the bus stop."],
            },
            {
                "pattern":  "next to · behind · under · in front of · between",
                "meaning":  "Aniq joyni koʻrsatadigan boshqa predloglar. "
                            "Bir gapda bir nechtasi ketma-ket kelishi "
                            "mumkin — yoʻl koʻrsatish shunday ishlaydi.",
                "examples": ["At the end of this street, next to the pharmacy.",
                             "On the second shelf, behind the sweets."],
            },
            {
                "pattern":  "Uzbek has one suffix for all three",
                "meaning":  "Oʻzbekchada <b>-da</b> hamma holatga yetadi: "
                            "doʻkon<b>da</b>, raf<b>da</b>, bekat<b>da</b>. "
                            "Inglizchada esa uchta boshqa soʻz. Shuning "
                            "uchun bu — oʻzbek oʻquvchisi eng koʻp xato "
                            "qiladigan joy: “<i>in</i> the corner” "
                            "burchakning <b>ichi</b> degani.",
                "examples": ["at the bus stop", "on the corner", "in the shop"],
            },
        ],
        "body": '''<p>A woman with a red <span class="cn-word" data-tr="jomadon">suitcase</span> stands <strong>at</strong> the <span class="cn-word" data-tr="bekat">bus stop</span>. She has a piece of paper <strong>in</strong> her hand.</p>

<p>"Excuse me. Is there a <span class="cn-word" data-tr="nonvoyxona">bakery</span> <strong>in</strong> this street?"</p>

<p>"The shop is <strong>on</strong> the corner," Afsona says. "<strong>At</strong> the end of this street, <strong>next to</strong> the <span class="cn-word" data-tr="dorixona">pharmacy</span>."</p>

<p>"And the bread? Is it <strong>in</strong> the shop, or <strong>on</strong> a table <strong>outside</strong>?"</p>

<p>"<strong>In</strong> the shop, <strong>on</strong> the second shelf, <strong>behind</strong> the <span class="cn-word" data-tr="shirinliklar">sweets</span>," Afsona says. "The hot bread is <strong>under</strong> a white <span class="cn-word" data-tr="mato">cloth</span>."</p>

<p>"You know this shop well."</p>

<p>"My brother works <strong>at</strong> the bakery <strong>behind</strong> the school," Afsona says. "Every morning he carries the trays to that corner."</p>

<p>The woman walks to the corner. Five minutes later she comes back with two loaves <strong>in</strong> a paper bag and one <strong>under</strong> her <span class="cn-word" data-tr="bilak">arm</span>.</p>

<p>"You are wrong about one thing," she says. "The hot bread is not <strong>under</strong> a cloth today. It is <strong>in</strong> my bag."</p>''',
        "questions": [
            {
                "text": "Where exactly is the bread in the shop?",
                "choices": [
                    "On a table outside the shop",
                    "On the second shelf, behind the sweets",
                    "Next to the pharmacy",
                ],
                "answer": 1,
                "explanation": "“In the shop, on the second shelf, behind the "
                               "sweets… under a white cloth.” Uchta predlog "
                               "birga aniq joyni beradi.",
            },
            {
                "text": "Which line is correct?",
                "choices": [
                    "She stands in the bus stop.",
                    "She stands at the bus stop.",
                    "She stands on the bus stop.",
                ],
                "answer": 1,
                "explanation": "Bekat — nuqta, faoliyat joyi → <b>at</b>. "
                               "<i>in</i> ichida boʻlishni, <i>on</i> "
                               "ustida turishni bildiradi.",
            },
            {
                "text": "Why is the woman's last sentence a joke?",
                "choices": [
                    "The bread is now in her bag, not under the cloth",
                    "She does not find the shop",
                    "She buys sweets instead of bread",
                ],
                "answer": 0,
                "explanation": "Afsona toʻgʻri aytgan edi — lekin bir "
                               "necha daqiqada joy oʻzgardi: issiq non "
                               "endi ayolning sumkasida.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-17 — prepositions of time: in, on, at
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "On Sunday, in April, at Nine",
        "summary": (
            "PE-17 matni. Buvining devordagi taqvimida butun xonadonning "
            "muhim kunlari bor. Toʻy — yakshanba kuni, aprelda, toʻqqizda."
        ),
        "order":   17,
        "grammar": [
            {
                "pattern":  "at + clock time · on + day/date · in + month/season",
                "meaning":  "<b>at</b> nine, at noon, at night, at the "
                            "weekend. <b>on</b> Sunday, on the first of "
                            "March, on my birthday. <b>in</b> April, in "
                            "summer, in 1961, in the morning.",
                "examples": ["The wedding is on Sunday, in April, at nine.",
                             "Our exams are in June."],
            },
            {
                "pattern":  "Big box → small box: in › on › at",
                "meaning":  "Eng katta boʻlak <b>in</b> (yil, oy, fasl), "
                            "oʻrtasi <b>on</b> (kun, sana), eng kichigi "
                            "<b>at</b> (soat, daqiqa). Shuni eslasangiz, "
                            "tanlash oson boʻladi.",
                "examples": ["in April → on Sunday → at nine o'clock"],
            },
            {
                "pattern":  "No preposition with next / last / this / every",
                "meaning":  "<i>next Sunday</i>, <i>last April</i>, "
                            "<i>this morning</i>, <i>every evening</i> — "
                            "bu soʻzlardan keyin predlog "
                            "<b>qoʻyilmaydi</b>. “<i>in</i> this morning” "
                            "— xato.",
                "examples": ["Every evening she reads the calendar.",
                             "This morning the yard is cool."],
            },
        ],
        "body": '''<p>My grandmother has a small <span class="cn-word" data-tr="taqvim">calendar</span> on the wall. Every important day in our family is on it.</p>

<p>My sister's <span class="cn-word" data-tr="toʻy">wedding</span> is <strong>on</strong> Sunday, <strong>in</strong> April, <strong>at</strong> nine <strong>in</strong> the morning.</p>

<p>"Why <strong>at</strong> nine?" I ask. "Nobody in this street gets up early <strong>at</strong> the weekend."</p>

<p>"<strong>In</strong> the morning the yard is <span class="cn-word" data-pos="adj" data-tr="salqin">cool</span>," she says. "<strong>In</strong> summer this yard is an oven <strong>at</strong> <span class="cn-word" data-tr="tush payti">noon</span>."</p>

<p>She writes the plan on the paper: bread <strong>at</strong> seven, <span class="cn-word" data-tr="mehmonlar">guests</span> <strong>at</strong> half past eight, music <strong>at</strong> nine.</p>

<p>My grandmother <span class="cn-word" data-pos="verb" data-tr="eslab qoladi">remembers</span> everything: my father's birthday <strong>in</strong> January, the school concert <strong>on</strong> the first of March, our exams <strong>in</strong> June.</p>

<p>"And your birthday?" I ask.</p>

<p>"It is on the calendar too. <strong>In</strong> December I am seventy."</p>

<p>"<strong>On</strong> which day?"</p>

<p>She <span class="cn-word" data-pos="verb" data-tr="yelka qisadi">shrugs</span>. "<strong>At</strong> my <span class="cn-word" data-tr="yosh">age</span> you count years, not days."</p>''',
        "questions": [
            {
                "text": "Why does the grandmother want the wedding at nine in the morning?",
                "choices": [
                    "Because the yard is cool in the morning",
                    "Because the guests get up early",
                    "Because the music starts at nine",
                ],
                "answer": 0,
                "explanation": "“In the morning the yard is cool… In summer "
                               "this yard is an oven at noon.”",
            },
            {
                "text": "Which line is correct?",
                "choices": [
                    "in Sunday, on April, at nine",
                    "on Sunday, in April, at nine",
                    "at Sunday, on April, in nine",
                ],
                "answer": 1,
                "explanation": "Kun — <b>on</b>, oy — <b>in</b>, soat — "
                               "<b>at</b>. Katta boʻlakdan kichigiga: "
                               "in April → on Sunday → at nine.",
            },
            {
                "text": "What does \"At my age you count years, not days\" mean here?",
                "choices": [
                    "She does not remember any dates",
                    "The exact day is not important to her any more",
                    "She has two birthdays",
                ],
                "answer": 1,
                "explanation": "U butun xonadonning sanalarini yoddan "
                               "biladi — faqat oʻzining kuni uning "
                               "uchun ahamiyatsiz.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-18 — question words
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Twenty Questions",
        "summary": (
            "PE-18 matni. Juma kuni oxirgi dars — oʻyin. Oʻqituvchining "
            "kissasidagi soʻzni topish uchun sinfda yigirmata savol bor."
        ),
        "order":   18,
        "grammar": [
            {
                "pattern":  "Wh- word + do/does + subject + verb?",
                "meaning":  "Soʻroq soʻzi eng oldinga chiqadi, keyin "
                            "PE-10 dagi qolip takrorlanadi: "
                            "<i>Where do we find it?</i>, "
                            "<i>Why do we use it?</i>",
                "examples": ["Where do we find it?", "How does it work?"],
            },
            {
                "pattern":  "How + another word",
                "meaning":  "<b>how much</b> (narx, sanalmaydigan), "
                            "<b>how many</b> (sanaladigan), "
                            "<b>how often</b> (qanchalik tez-tez), "
                            "<b>how long</b> (qancha vaqt), "
                            "<b>how old</b> (necha yosh).",
                "examples": ["How much does it cost?",
                             "How many parts does it have?",
                             "How often do people use it?"],
            },
            {
                "pattern":  "Who as subject needs no “do”",
                "meaning":  "Agar soʻroq soʻzi <b>eganing oʻzi</b> boʻlsa, "
                            "<i>do/does</i> kerak emas va feʼl oddiy "
                            "shaklda qoladi: <i>Who uses it?</i> — "
                            "“<i>Who does use it?</i>” xato.",
                "examples": ["Who uses it?", "What is the answer?"],
            },
        ],
        "body": '''<p>On Friday the last lesson is a game. The teacher writes one word on a small paper and puts it in her pocket.</p>

<p>"You have twenty questions," she says. "The <span class="cn-word" data-tr="qoidalar">rules</span> are simple: I answer only with short sentences."</p>

<p>"<strong>Where do</strong> we find it?" Dilnoza asks. "In every house."</p>

<p>"<strong>How much does</strong> it <span class="cn-word" data-pos="verb" data-tr="turadi (narx)">cost</span>?" "<span class="cn-word" data-pos="adv" data-tr="deyarli">Almost</span> nothing."</p>

<p>"<strong>How often do</strong> people use it?" "Every evening."</p>

<p>"<strong>Who uses</strong> it?" "Everybody in the room."</p>

<p>"<strong>How many</strong> parts does it have?" "Two."</p>

<p>"<strong>When do</strong> we use it?" "When the sun goes down."</p>

<p>"<strong>Why do</strong> we use it?" "Because the room is dark."</p>

<p>"<strong>How does</strong> it work?" "With <span class="cn-word" data-tr="elektr">electricity</span>."</p>

<p>Nineteen questions and no answer. The class is quiet. Sherbek <span class="cn-word" data-pos="verb" data-tr="taxmin qiladi">guesses</span> a lamp, a phone, a television — all wrong.</p>

<p>Then Afsona asks the <span class="cn-word" data-tr="yigirmanchi">twentieth</span> question, and it is the best one: "<strong>Where</strong> in the room <strong>is</strong> it?"</p>

<p>The teacher looks at the wall next to the door.</p>

<p>"A light <span class="cn-word" data-tr="kalit (vyklyuchatel)">switch</span>," Afsona says. "Two parts: on and off."</p>''',
        "questions": [
            {
                "text": "What is the word in the teacher's pocket?",
                "choices": ["A lamp", "A light switch", "A television"],
                "answer": 1,
                "explanation": "Afsona topadi: ikki qismi bor — “on and "
                               "off” — va u eshik yonidagi devorda.",
            },
            {
                "text": "Which question is correct English?",
                "choices": [
                    "Who does use it?",
                    "Who uses it?",
                    "Who do use it?",
                ],
                "answer": 1,
                "explanation": "<i>Who</i> shu gapda eganing oʻzi, shuning "
                               "uchun <i>do/does</i> kerak emas: "
                               "<b>Who uses it?</b>",
            },
            {
                "text": "Why does the last question win the game?",
                "choices": [
                    "It asks about the place in the room, so the teacher looks at the wall",
                    "It asks for the answer directly",
                    "It is the twentieth question, so the teacher must answer",
                ],
                "answer": 0,
                "explanation": "Afsona narsaning nomini emas, "
                               "<b>joyini</b> soʻraydi — va oʻqituvchining "
                               "koʻzlari devorga qaraydi. Yaxshi savol "
                               "javobni oʻzi olib keladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-19 — was / were
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "It Was Only a Photo",
        "summary": (
            "PE-19 matni. Karavot tagidagi qutida 1961-yilning surati: "
            "toʻqqiz bola, bitta toʻp, poyabzalsiz oyoqlar. Bobo "
            "gapirganda surat hikoyaga aylanadi."
        ),
        "order":   19,
        "grammar": [
            {
                "pattern":  "was (I, he, she, it) · were (you, we, they)",
                "meaning":  "“Boʻlmoq” feʼlining oʻtgan zamoni ikki "
                            "shaklga boʻlinadi. Ikkinchi shaxs "
                            "<i>you</i> — birlikda ham <b>were</b> "
                            "oladi.",
                "examples": ["The year was 1961. I was fourteen.",
                             "They were on a football field."],
            },
            {
                "pattern":  "wasn't / weren't · Was …? Were …?",
                "meaning":  "Inkor uchun <b>not</b> qoʻshiladi "
                            "(<i>wasn't</i>, <i>weren't</i>), savolda "
                            "esa feʼl ega bilan joy almashadi: "
                            "<i>Were you the goalkeeper?</i> "
                            "<i>do/did</i> bu yerda kerak emas.",
                "examples": ["No, I wasn't.", "They weren't rich boys.",
                             "Were you the goalkeeper?"],
            },
            {
                "pattern":  "There was / There were",
                "meaning":  "PE-7 dagi <i>there is / there are</i> ning "
                            "oʻtgan zamoni: birlikda <b>there was</b>, "
                            "koʻplikda <b>there were</b>.",
                "examples": ["There was a field behind the old mosque.",
                             "There were no lines on the grass."],
            },
        ],
        "body": '''<p>The box under the bed is full of photos. Dilnoza takes one and looks at it for a long time. Nine boys in white shirts stand on dry grass.</p>

<p>"Who <strong>were</strong> these boys?" she asks.</p>

<p>Her grandfather takes the photo in both hands. "That <strong>was</strong> our team," he says. "The year <strong>was</strong> 1961. I <strong>was</strong> fourteen."</p>

<p>"<strong>Were</strong> you the goalkeeper?"</p>

<p>"No, I <strong>wasn't</strong>. My brother <strong>was</strong> the goalkeeper. He <strong>was</strong> tall, and he <strong>wasn't</strong> afraid of the ball."</p>

<p>"<strong>Where was</strong> the field?"</p>

<p>"<strong>There was</strong> a field behind the old <span class="cn-word" data-tr="masjid">mosque</span>. <strong>There were</strong> no <span class="cn-word" data-tr="chiziqlar">lines</span> on the grass, and the goals <strong>were</strong> two <span class="cn-word" data-tr="tayoqlar">sticks</span>. The ball <strong>was</strong> <span class="cn-word" data-pos="adj" data-tr="ogʻir">heavy</span>. In the rain it <strong>was</strong> a <span class="cn-word" data-tr="tosh">stone</span>."</p>

<p>"And these two boys <strong>were</strong> your friends?"</p>

<p>"They <strong>were</strong>. Anvar <strong>was</strong> a good <span class="cn-word" data-tr="chopqir">runner</span>. Timur <strong>was</strong> our <span class="cn-word" data-tr="sardor">captain</span>. They <strong>weren't</strong> <span class="cn-word" data-pos="adj" data-tr="boy">rich</span> boys — nobody in that street <strong>was</strong> rich."</p>

<p>Dilnoza looks at the photo again: nine boys, one ball, and not one pair of football <span class="cn-word" data-tr="butinkalar">boots</span>.</p>

<p>"This morning it <strong>was</strong> only a photo," she says. "Now it is a story."</p>''',
        "questions": [
            {
                "text": "Who was the goalkeeper in the photo?",
                "choices": [
                    "The grandfather",
                    "The grandfather's brother",
                    "Timur, the captain",
                ],
                "answer": 1,
                "explanation": "“No, I wasn't. My brother was the goalkeeper. "
                               "He was tall…”",
            },
            {
                "text": "Which sentence is correct?",
                "choices": [
                    "There was no lines on the grass.",
                    "There were no lines on the grass.",
                    "There are no lines on the grass in 1961.",
                ],
                "answer": 1,
                "explanation": "<i>lines</i> — koʻplik, oʻtgan zamon → "
                               "<b>there were</b>. Uchinchi variant zamonni "
                               "1961-yil bilan qarama-qarshi qoʻyadi.",
            },
            {
                "text": "What does the last line mean?",
                "choices": [
                    "The photo is now more valuable than money",
                    "The photo becomes a story when her grandfather explains it",
                    "Dilnoza wants to keep the photo",
                ],
                "answer": 1,
                "explanation": "Surat oʻzgarmadi — Dilnozaning bilgani "
                               "oʻzgardi. Boboning gaplari qogʻozni "
                               "hikoyaga aylantirdi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PE-20 — past simple: regular verbs and the -ed ending
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Day the Bakery Opened",
        "summary": (
            "PE-20 matni. Oʻn ikki yil oldin burchakdagi xona boʻsh edi. "
            "Bekzodning otasi devorlarni oqladi, kutdi — va bitta chol "
            "kirdi. Barcha feʼllar -ed bilan."
        ),
        "order":   20,
        "grammar": [
            {
                "pattern":  "verb + -ed for every person",
                "meaning":  "Oddiy oʻtgan zamonda shakl <b>bitta</b>: "
                            "<i>I worked, he worked, they worked</i>. "
                            "Uchinchi shaxs <b>-s</b> si bu zamonda "
                            "butunlay yoʻqoladi.",
                "examples": ["He painted the walls white.",
                             "Thirty people waited at the door."],
            },
            {
                "pattern":  "Spelling: live → lived · stop → stopped · carry → carried",
                "meaning":  "Oxirgi <i>-e</i> tushadi (<i>live → lived</i>); "
                            "qisqa unli + bitta undosh ikkilanadi "
                            "(<i>stop → stopped</i>); undoshdan keyingi "
                            "<i>-y</i> esa <i>-ied</i> boʻladi "
                            "(<i>carry → carried</i>).",
                "examples": ["He carried the old oven into the room.",
                             "He stopped only twice."],
            },
            {
                "pattern":  "Three sounds, one spelling",
                "meaning":  "<b>-ed</b> uch xil talaffuz qilinadi: "
                            "jarangsizdan keyin /t/ (<i>worked</i>, "
                            "<i>stopped</i>), jarangli tovushdan keyin "
                            "/d/ (<i>opened</i>, <i>cleaned</i>), "
                            "va <i>t/d</i> dan keyin /ɪd/ "
                            "(<i>waited</i>, <i>painted</i>) — faqat "
                            "shu holatda qoʻshimcha boʻgʻin qoʻshiladi.",
                "examples": ["worked /t/ · opened /d/ · waited /ɪd/"],
            },
        ],
        "body": '''<p>Twelve years <span class="cn-word" data-pos="adv" data-tr="avval">ago</span> there was no bakery on our corner. There was an empty room with grey walls and one small window.</p>

<p>Bekzod's father <strong>painted</strong> the walls white. He <strong>cleaned</strong> the floor three times. He <strong>carried</strong> an old oven from his brother's house and <strong>repaired</strong> it with his own hands.</p>

<p>The bakery <strong>opened</strong> on a Monday in March. At six o'clock the bread was ready and the room was warm. Nobody <strong>arrived</strong>.</p>

<p>He <strong>waited</strong>. At seven o'clock one old man <strong>walked</strong> in and <strong>asked</strong> for two loaves. At eight the same man <strong>returned</strong> with his neighbour.</p>

<p>On the second day thirty people <strong>waited</strong> at the door before six.</p>

<p>That week Bekzod's father <strong>worked</strong> nineteen hours a day and <strong>finished</strong> at <span class="cn-word" data-tr="yarim tun">midnight</span>. He <strong>stopped</strong> only <span class="cn-word" data-pos="adv" data-tr="ikki marta">twice</span>: for tea, and for the evening <span class="cn-word" data-tr="namoz">prayer</span>.</p>

<p>Bekzod's mother <strong>helped</strong> him with the <span class="cn-word" data-tr="xamir">dough</span>. On Sunday she <strong>counted</strong> the money on the table and <strong>laughed</strong>: it was <span class="cn-word" data-pos="adj" data-tr="yetarli">enough</span> for <span class="cn-word" data-tr="un">flour</span>, and nothing else.</p>

<p>Twelve years later the room is warm every morning and the walls are still white. Bekzod's father says one sentence about that first Monday.</p>

<p>"One man <strong>walked</strong> in. That was enough."</p>''',
        "questions": [
            {
                "text": "How many customers came on the first morning?",
                "choices": [
                    "Nobody came at all",
                    "One old man, and later the same man with his neighbour",
                    "Thirty people before six o'clock",
                ],
                "answer": 1,
                "explanation": "Birinchi kuni bitta chol keldi, keyin "
                               "qoʻshnisi bilan qaytdi. Oʻttiz kishi — "
                               "ikkinchi kuni.",
            },
            {
                "text": "Which past form is spelled correctly?",
                "choices": [
                    "carryed, stoped, painted",
                    "carried, stopped, painted",
                    "carried, stoped, paintd",
                ],
                "answer": 1,
                "explanation": "carry → <b>carried</b> (y → ied), "
                               "stop → <b>stopped</b> (undosh "
                               "ikkilanadi), paint → <b>painted</b>.",
            },
            {
                "text": "Which verb has the extra /ɪd/ syllable?",
                "choices": ["worked", "cleaned", "waited"],
                "answer": 2,
                "explanation": "<i>t</i> yoki <i>d</i> bilan tugagan "
                               "feʼllarda <b>-ed</b> alohida boʻgʻin "
                               "boʻlib eshitiladi: wait-<b>ed</b>. "
                               "<i>worked</i> = /t/, <i>cleaned</i> = /d/.",
            },
        ],
    },
]
