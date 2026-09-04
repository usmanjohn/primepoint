# -*- coding: utf-8 -*-
"""Prime SAT Readings — SAT-26 … SAT-30 (batch 6).

  26 — why the radical moved upstairs   (SAT-26: rationalising, and its real reason)
  27 — two rooms and a corridor         (SAT-27: adding and subtracting expressions)
  28 — the garden that grew twice       (SAT-28: the area model of a product)
  29 — rows for the sports day          (SAT-29: a greatest common factor in a yard)
  30 — the trader's two squares         (SAT-30: 51² − 49² in his head)

Genre rotation — none of the twenty-five shapes used in batches 1–5 repeat here.

⛔ NO ALGEBRAIC NOTATION IN THE BODY — quantities in English, units spelled out.
NARRATOR VOICE (batch 5 ran 3 female / 2 male, so this one flips):
    26 en-US-GuyNeural   · 27 en-US-JennyNeural · 28 en-US-GuyNeural
    29 en-US-JennyNeural · 30 en-US-GuyNeural

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_26_30.py --author=prime
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
    # SAT-26 — why the radical moved                              [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Before the Calculator",
        "summary": (
            "SAT-26 matni. Maxrajdagi ildizdan qutulish odati goʻzallik uchun emas — "
            "u qoʻlda hisoblash zamonasining amaliy yechimi edi."
        ),
        "order":   26,
        "grammar": [
            {
                "pattern":  "by hand",
                "meaning":  "Qoʻlda, asbobsiz. Kalkulyatorgacha boʻlgan davrni "
                            "tasvirlashda doimiy ibora.",
                "examples": ["Dividing by 1.414 by hand took a minute; halving took seconds."],
            },
            {
                "pattern":  "the same number, written differently",
                "meaning":  "Bir xil son, boshqacha yozilgan. Ratsionallash "
                            "<b>qiymatni</b> emas, <b>shaklni</b> oʻzgartiradi.",
                "examples": ["Those two expressions are the same number, written differently."],
            },
            {
                "pattern":  "a convention, not a rule of arithmetic",
                "meaning":  "Qoida emas, kelishuv. Matematikada baʼzi narsalar "
                            "toʻgʻri-notoʻgʻri emas, <b>odat</b> masalasi.",
                "examples": ["Rationalising is a convention, not a rule of arithmetic."],
            },
        ],
        "body": '''<p>Open a mathematics <span class="cn-word" data-tr="darslik">textbook</span> printed in 1950 and you will not find a single answer with a <span class="cn-word" data-tr="kvadrat ildiz">square root</span> underneath a line. There is a reason, and it has nothing to do with beauty.</p>

<p>Before <span class="cn-word" data-tr="kalkulyator">calculators</span>, every division was done <strong>by hand</strong>. Suppose you needed one divided by the square root of two. You would look up the square root of two in a <span class="cn-word" data-tr="jadval">table</span> — 1.41421 — and then face the job of dividing 1 by 1.41421, which is a long division with a five-figure <span class="cn-word" data-tr="boʻluvchi">divisor</span> and plenty of room for a mistake.</p>

<p>Now move the root upstairs. The same quantity can be written as the square root of two divided by two, and that is 1.41421 <span class="cn-word" data-tr="ikkiga boʻlingan">halved</span>: 0.70711. A schoolchild can do it in five seconds and get it <span class="cn-word" data-tr="toʻgʻri">right</span>.</p>

<p>The two <span class="cn-word" data-tr="ifodalar">expressions</span> are <strong>the same number, written differently</strong> — but one of them took a minute of careful work and the other took a breath. Multiplied across a page of <span class="cn-word" data-tr="hisob-kitob">calculations</span>, that difference decided how long a <span class="cn-word" data-tr="muhandis">engineer</span> worked and how often he was wrong.</p>

<p>So the habit spread, and it stayed after the reason for it disappeared. Today it is <strong>a convention, not a rule of arithmetic</strong>: <span class="cn-word" data-tr="imtihon tuzuvchilar">examiners</span> still write answers with the radical on top, so a pupil who leaves it underneath may have the right value and still fail to find it among the choices.</p>

<p>Which is a small lesson about mathematics in general. Some of what looks like law is only <span class="cn-word" data-tr="odat">habit</span> — but habits are worth knowing, because the <span class="cn-word" data-tr="imtihon varaqasi">answer sheet</span> was written by somebody who has them.</p>''',
        "questions": [
            {
                "text": "Why was 1 divided by the square root of 2 difficult before calculators?",
                "choices": ["Because the square root of 2 was unknown",
                            "Because it meant long division by a five-figure number",
                            "Because tables did not include square roots"],
                "answer": 1,
                "explanation": "Jadvalda √2 = 1.41421 bor edi. Qiyinligi — <b>1 ni "
                               "1.41421 ga boʻlish</b>, yaʼni besh raqamli boʻluvchi "
                               "bilan uzun boʻlish.",
            },
            {
                "text": "What makes the rewritten form easier to compute?",
                "choices": ["It only requires halving a number from the table",
                            "It gives a smaller answer",
                            "It removes the need for the table"],
                "answer": 0,
                "explanation": "√2 ÷ 2 — bu jadvaldagi 1.41421 ni <b>ikkiga boʻlish</b>, "
                               "besh soniyalik ish. Jadval baribir kerak, va javob "
                               "ham oʻsha son.",
            },
            {
                "text": "According to the text, why does the habit still matter today?",
                "choices": [
                    "Because calculators cannot handle radicals in denominators.",
                    "Because the value of the expression changes if you do not rationalise.",
                    "Because examiners write the answer choices in that form.",
                ],
                "answer": 2,
                "explanation": "Qiymat oʻzgarmaydi va kalkulyator ham bemalol hisoblaydi. "
                               "Muhimi — <b>javoblar</b> shu shaklda yozilgani: aks holda "
                               "toʻgʻri javobni roʻyxatdan topib boʻlmaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-27 — adding and subtracting                           [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Two Rooms and a Corridor",
        "summary": (
            "SAT-27 matni. Meʼmor uzunligi hali maʼlum boʻlmagan binoni "
            "rejalashtiradi — va ifodalarni qoʻshib, ayirib ish koʻradi."
        ),
        "order":   27,
        "grammar": [
            {
                "pattern":  "in terms of the unknown length",
                "meaning":  "Nomaʼlum uzunlik orqali ifodalangan holda. Javob son "
                            "emas, <b>ifoda</b> boʻladi.",
                "examples": ["The area is given in terms of the unknown length."],
            },
            {
                "pattern":  "taken out of the total",
                "meaning":  "Umumiydan ayirib tashlanadi. Ayirishning kundalik "
                            "tildagi koʻrinishi.",
                "examples": ["The corridor is taken out of the total floor area."],
            },
            {
                "pattern":  "whatever the length turns out to be",
                "meaning":  "Uzunlik qanday chiqishidan qatʼi nazar. Ifoda bilan "
                            "ishlashning butun foydasi shu.",
                "examples": ["The answer holds whatever the length turns out to be."],
            },
        ],
        "body": '''<p>An <span class="cn-word" data-tr="meʼmor">architect</span> drawing a small <span class="cn-word" data-tr="poliklinika">clinic</span> had one number she did not yet have. The <span class="cn-word" data-tr="uchastka">plot</span> ran along a road whose width was still being <span class="cn-word" data-tr="bahslashilayotgan">argued about</span> at the <span class="cn-word" data-tr="shahar hokimiyati">town hall</span>, so the building's <span class="cn-word" data-tr="chuqurligi">depth</span> was, for the moment, simply «the unknown length».</p>

<p>She carried on anyway. The <span class="cn-word" data-tr="qabul xonasi">consulting room</span>, she wrote, would have a floor area of three times that length plus twelve square metres. The <span class="cn-word" data-tr="kutish xonasi">waiting room</span> would be five times the length plus five. Added together — and adding is nothing more than putting like with like — the two rooms come to eight times the length plus seventeen.</p>

<p>Then the corridor. It has to be <strong>taken out of the total</strong>, because it is not <span class="cn-word" data-tr="foydalanish mumkin boʻlgan">usable</span> floor space: two times the length plus three. Subtracting means every part of that expression changes sign, so what remains is six times the length plus fourteen.</p>

<p>Three weeks later the town hall <span class="cn-word" data-tr="hal qildi">settled</span> the road at a width that left the building six metres deep. She put six into her expression: six times six is thirty-six, plus fourteen, giving fifty <span class="cn-word" data-tr="kvadrat metr">square metres</span> of usable floor.</p>

<p>She checked it the slow way as well. The consulting room came to thirty square metres, the waiting room to thirty-five, and the corridor took away fifteen — which is also fifty.</p>

<p>The point of the expression was never the answer. It was that the whole <span class="cn-word" data-tr="loyiha">design</span> could be finished, argued over and <span class="cn-word" data-tr="tasdiqlangan">approved</span> <strong>whatever the length turned out to be</strong> — and the arithmetic waited quietly at the end.</p>''',
        "questions": [
            {
                "text": "What is the total floor area of the two rooms, before the corridor is removed?",
                "choices": ["Six times the length plus fourteen",
                            "Eight times the length plus seventeen",
                            "Two times the length plus three"],
                "answer": 1,
                "explanation": "Uch marta uzunlik + 12, qoʻshiladi besh marta uzunlik + 5: "
                               "3 + 5 = <b>8</b> marta uzunlik va 12 + 5 = <b>17</b>.",
            },
            {
                "text": "How much usable floor is there when the length is six metres?",
                "choices": ["Fifty square metres", "Sixty-five square metres",
                            "Thirty-six square metres"],
                "answer": 0,
                "explanation": "6 × 6 + 14 = 36 + 14 = <b>50</b> kv. metr. "
                               "<b>65</b> — koridor ayirilmagan holdagi qiymat "
                               "(30 + 35).",
            },
            {
                "text": "Why did the architect work with an expression instead of waiting for the number?",
                "choices": [
                    "Because the design could be finished whatever the length turned out to be.",
                    "Because the town hall asked for an expression.",
                    "Because the rooms had no fixed shape.",
                ],
                "answer": 0,
                "explanation": "Ifoda bilan ishlash butun loyihani <b>oldindan</b> "
                               "tugatishga imkon berdi; son kelganda esa faqat "
                               "oʻrniga qoʻyish qoldi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-28 — the area model                                     [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Garden That Grew Twice",
        "summary": (
            "SAT-28 matni. Kvadrat bogʻ ikki tomondan kengaytiriladi — va yangi "
            "yuza toʻrtta boʻlakdan iborat boʻlib chiqadi."
        ),
        "order":   28,
        "grammar": [
            {
                "pattern":  "extended by three metres on one side",
                "meaning":  "Bir tomondan uch metrga kengaytirilgan. Har bir "
                            "kengaytirish koʻpaytmadagi bitta qavsga mos keladi.",
                "examples": ["The plot was extended by three metres on one side and five on the other."],
            },
            {
                "pattern":  "four pieces, not two",
                "meaning":  "Toʻrtta boʻlak, ikkita emas — bu FOIL ning rasmdagi "
                            "koʻrinishi va oʻrtadagi hadning sababi.",
                "examples": ["The new garden is four pieces, not two."],
            },
            {
                "pattern":  "the corner is easy to forget",
                "meaning":  "Burchak esdan chiqadi — aynan shu boʻlak "
                            "x<sup>2</sup> + 25 xatosining sababi.",
                "examples": ["The little corner square is easy to forget."],
            },
        ],
        "body": '''<p>A family in a <span class="cn-word" data-tr="qishloq">village</span> outside Samarkand had a square <span class="cn-word" data-tr="sabzavot bogʻi">vegetable garden</span> and, one <span class="cn-word" data-tr="bahor">spring</span>, the room to make it bigger. The land to the east allowed three more metres; the land to the north allowed five.</p>

<p>The father, who had built walls all his life, drew the new garden in the <span class="cn-word" data-tr="chang">dust</span> with a <span class="cn-word" data-tr="tayoq">stick</span>, and what he drew was not one <span class="cn-word" data-tr="toʻrtburchak">rectangle</span> but <strong>four pieces, not two</strong>.</p>

<p>There is the old square, <span class="cn-word" data-tr="oʻzgarmagan">unchanged</span>. There is a long <span class="cn-word" data-tr="tasma, boʻlak">strip</span> three metres wide running down the <span class="cn-word" data-tr="sharqiy">eastern</span> side. There is a second strip five metres deep along the <span class="cn-word" data-tr="shimoliy">northern</span> edge. And there, in the top corner where the two extensions meet, is a small rectangle three metres by five — fifteen square metres that belongs to neither strip.</p>

<p>That corner is the whole point of the drawing. It is the piece people leave out when they multiply in their heads, and it is <strong>easy to forget</strong> precisely because nobody walked through it before.</p>

<p>The numbers came later. The old garden had been ten metres on a side, so it held one hundred square metres. The eastern strip added thirty, the northern one fifty, and the corner fifteen: one hundred and ninety-five square metres in all.</p>

<p>His daughter, who was doing algebra at school, <span class="cn-word" data-tr="oʻlchadi">measured</span> the finished garden instead — thirteen metres by fifteen — and multiplied. She got one hundred and ninety-five as well, and spent the walk home working out why the two methods could not <span class="cn-word" data-tr="farq qilmoq">disagree</span>.</p>''',
        "questions": [
            {
                "text": "How many square metres does the small corner piece add?",
                "choices": ["Eight", "Fifteen", "Thirty"],
                "answer": 1,
                "explanation": "Burchak boʻlagi 3 metrga 5 metr: 3 × 5 = <b>15</b> kv. "
                               "metr. Aynan shu boʻlak koʻpaytirishda esdan chiqadi.",
            },
            {
                "text": "What is the area of the finished garden?",
                "choices": ["180 square metres", "195 square metres", "210 square metres"],
                "answer": 1,
                "explanation": "Toʻrt boʻlak: 100 + 30 + 50 + 15 = <b>195</b>. Yoki "
                               "toʻgʻridan-toʻgʻri: 13 × 15 = 195 — ikki yoʻl bir xil "
                               "javob beradi.",
            },
            {
                "text": "Why can the two methods never disagree?",
                "choices": [
                    "Because the four pieces together are exactly the finished rectangle.",
                    "Because the garden was square to begin with.",
                    "Because both extensions were whole numbers of metres.",
                ],
                "answer": 0,
                "explanation": "Toʻrt boʻlakning yigʻindisi — bu tayyor toʻrtburchakning "
                               "oʻzi. Shuning uchun qavslarni ochish va toʻgʻridan-toʻgʻri "
                               "koʻpaytirish bir xil natija beradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-29 — a common factor in a yard                        [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Rows for the Sports Day",
        "summary": (
            "SAT-29 matni. Maktab hovlisida 48 oʻgʻil va 36 qiz teng qatorlarga "
            "tizilishi kerak — va javob ikki sonning umumiy koʻpaytuvchisi."
        ),
        "order":   29,
        "grammar": [
            {
                "pattern":  "the same number in every row",
                "meaning":  "Har bir qatorda bir xil son — bu shart ikkala sonni "
                            "ham boʻladigan bitta songa olib keladi.",
                "examples": ["The head teacher wanted the same number in every row."],
            },
            {
                "pattern":  "divides both numbers exactly",
                "meaning":  "Ikkala sonni ham qoldiqsiz boʻladi. Umumiy "
                            "koʻpaytuvchining taʼrifi.",
                "examples": ["Twelve divides both numbers exactly."],
            },
            {
                "pattern":  "the largest that works",
                "meaning":  "Ishlaydiganlarining eng kattasi — <b>eng katta</b> "
                            "umumiy koʻpaytuvchi (GCF).",
                "examples": ["Six works, but twelve is the largest that works."],
            },
        ],
        "body": '''<p>The sports day at a school of eighty-four pupils begins with a <span class="cn-word" data-tr="saf">parade</span>, and the parade begins with an <span class="cn-word" data-tr="bahs">argument</span> in the <span class="cn-word" data-tr="oʻqituvchilar xonasi">staff room</span>.</p>

<p>There are 48 boys and 36 girls. The <span class="cn-word" data-tr="direktor">head teacher</span> wants them in <span class="cn-word" data-tr="qator">rows</span>, boys with boys and girls with girls, and <strong>the same number in every row</strong> so that the lines look straight from the <span class="cn-word" data-tr="minbar">stand</span>.</p>

<p>Rows of ten are <span class="cn-word" data-tr="imkonsiz">impossible</span>: ten does not divide either number. Rows of eight fit the boys but leave four girls standing on their own. Rows of six work for both — eight rows of boys and six of girls — and for two years that is what the school did.</p>

<p>Then a mathematics teacher <span class="cn-word" data-tr="eʼtibor qaratdi">pointed out</span> that six is not the only number that <strong>divides both numbers exactly</strong>. Two does, three does, four does, six does — and so does twelve. Twelve is <strong>the largest that works</strong>: it gives four rows of boys and three of girls, seven rows in all, and a parade that takes half the time to <span class="cn-word" data-tr="tuzmoq, tartibga solmoq">form up</span>.</p>

<p>Anything larger <span class="cn-word" data-tr="ishlamaydi">fails</span>. Sixteen divides 48 but not 36; eighteen divides 36 but not 48. Twelve is the point where both numbers agree, and there is nothing above it.</p>

<p>The <span class="cn-word" data-tr="masala">problem</span> the school solved that morning has a name in every algebra book: the greatest common factor. It is the first thing you take out of an <span class="cn-word" data-tr="ifoda">expression</span>, and the reason is the same in both places — <span class="cn-word" data-tr="eng kattasini oling">take the largest piece that fits everything</span>, and what is left is as simple as it can be.</p>''',
        "questions": [
            {
                "text": "What is the largest row size that works for both groups?",
                "choices": ["Six", "Twelve", "Sixteen"],
                "answer": 1,
                "explanation": "48 va 36 ni ham qoldiqsiz boʻladigan eng katta son — "
                               "<b>12</b>. <b>16</b> 48 ni boʻladi, lekin 36 ni "
                               "boʻlmaydi.",
            },
            {
                "text": "How many rows are there in total when that size is used?",
                "choices": ["Seven", "Fourteen", "Twenty-one"],
                "answer": 0,
                "explanation": "48 ÷ 12 = 4 qator oʻgʻil va 36 ÷ 12 = 3 qator qiz, "
                               "jami <b>7</b> qator.",
            },
            {
                "text": "Why does the text say sixteen and eighteen both fail?",
                "choices": [
                    "Because each divides only one of the two numbers.",
                    "Because both are larger than the number of girls.",
                    "Because rows must contain an even number of pupils.",
                ],
                "answer": 0,
                "explanation": "Umumiy koʻpaytuvchi <b>ikkala</b> sonni ham boʻlishi "
                               "kerak. 16 faqat 48 ni, 18 faqat 36 ni boʻladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-30 — the trader's two squares                           [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Trader's Two Squares",
        "summary": (
            "SAT-30 matni. Bozordagi sotuvchi ikki kvadratning ayirmasini bir "
            "soniyada aytadi — va uning usuli maktabdagi formulaning oʻzi."
        ),
        "order":   30,
        "grammar": [
            {
                "pattern":  "in his head",
                "meaning":  "Ogʻzaki, yozmasdan. Formulaning kuchi aynan shunda "
                            "koʻrinadi.",
                "examples": ["He does it in his head, before you have found a pencil."],
            },
            {
                "pattern":  "the gap between them",
                "meaning":  "Ular orasidagi farq — kvadratlar ayirmasi "
                            "formulasidagi birinchi qavs.",
                "examples": ["Two metres is the gap between them."],
            },
            {
                "pattern":  "it works every time",
                "meaning":  "Har safar ishlaydi. Formulaning tasodif emasligini "
                            "taʼkidlaydi.",
                "examples": ["He was surprised that it works every time."],
            },
        ],
        "body": '''<p>A man who sells <span class="cn-word" data-tr="gilamlar">carpets</span> in the covered <span class="cn-word" data-tr="bozor">market</span> can tell you, without pausing, that a square of side fifty-one and a square of side forty-nine differ in <span class="cn-word" data-tr="yuza">area</span> by <span class="cn-word" data-tr="roppa-rosa">exactly</span> two hundred.</p>

<p>He does it <strong>in his head</strong>, and he does not know the two squares themselves. Ask him what fifty-one times fifty-one is and he will <span class="cn-word" data-tr="yelka qisadi">shrug</span>. Ask him the difference and he answers before you have found a <span class="cn-word" data-tr="qalam">pencil</span>.</p>

<p>His method is two <span class="cn-word" data-tr="qadam">steps</span>. Take <strong>the gap between them</strong> — two. Take the <span class="cn-word" data-tr="yigʻindi">sum</span> of them — one hundred. Multiply: two hundred. That is the answer, and it is exact.</p>

<p>He learned it from his father, who sold <span class="cn-word" data-tr="mato">cloth</span>, and who used it for the same practical reason: <span class="cn-word" data-tr="qirqim, boʻlak">offcuts</span>. When a square of cloth is trimmed down to a smaller square, the strip you lose is the difference of two squares, and a man who can price it instantly does not lose <span class="cn-word" data-tr="pul">money</span>.</p>

<p>The <span class="cn-word" data-tr="qoida">rule</span> is not a market <span class="cn-word" data-tr="hiyla">trick</span>. It is the formula every algebra course teaches — the difference of two squares — and it is the reason the middle terms <span class="cn-word" data-tr="yoʻqoladi">vanish</span> when you multiply two brackets that differ only in a sign.</p>

<p>He was pleased, when a student explained this to him, that <strong>it works every time</strong>. Twenty-five and twenty-four differ by forty-nine. A hundred and three and ninety-seven differ by one thousand two hundred. «Yes,» he said. «I know. I have never once had to check.»</p>''',
        "questions": [
            {
                "text": "How does the trader work out the difference between the two squares?",
                "choices": ["He multiplies the gap between the numbers by their sum",
                            "He squares each number and subtracts",
                            "He doubles the smaller number"],
                "answer": 0,
                "explanation": "Ikki qadam: farqi (2) va yigʻindisi (100), keyin "
                               "koʻpaytiriladi: 2 × 100 = <b>200</b>. Kvadratlarning "
                               "oʻzini bilish shart emas.",
            },
            {
                "text": "By how much do squares of side 25 and side 24 differ in area?",
                "choices": ["One", "Forty-nine", "Fifty"],
                "answer": 1,
                "explanation": "Farqi 1, yigʻindisi 49: 1 × 49 = <b>49</b>. Ketma-ket "
                               "ikki sonda ayirma har doim ularning yigʻindisiga teng.",
            },
            {
                "text": "What connects the trader's trick to the algebra taught in school?",
                "choices": [
                    "It is the difference-of-squares formula, which is why the middle terms vanish.",
                    "It only works for numbers near fifty.",
                    "It is a rounding method that is close enough in practice.",
                ],
                "answer": 0,
                "explanation": "Bu aynan kvadratlar ayirmasi formulasi va u <b>aniq</b>, "
                               "taxminiy emas. Oʻrtadagi hadlarning qisqarishi — "
                               "usulning sababi.",
            },
        ],
    },
]
