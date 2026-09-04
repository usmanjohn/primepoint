# -*- coding: utf-8 -*-
"""Prime SAT Readings — SAT-16 … SAT-20 (batch 4).

  16 — a canteen manager and two receipts   (SAT-16: two facts, two unknowns)
  17 — a warehouse balance, two weighings   (SAT-17: subtract and one load vanishes)
  18 — an inspector counts legs             (SAT-18: the classic two-equation count)
  19 — two signs, one offer                 (SAT-19: the same line written twice)
  20 — the fare that never catches up       (SAT-20: parallel prices)

Genre rotation — used already: cafe order sheet, lab report, committee minutes,
quality-control report, news item, museum notice, pool notice, radio running order,
coach's log, newspaper Q&A, survey note, workshop guide, school rule, park notice,
loading sheet. None of those repeat here.

⛔ NO ALGEBRAIC NOTATION IN THE BODY — quantities in English, units spelled out.
NARRATOR VOICE (batch 3 ran 3 female / 2 male, so this one flips):
    16 en-US-GuyNeural   · 17 en-US-JennyNeural · 18 en-US-GuyNeural
    19 en-US-JennyNeural · 20 en-US-GuyNeural

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_sat_readings_16_20.py --author=prime
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
    # SAT-16 — substitution                                       [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Two Receipts",
        "summary": (
            "SAT-16 matni. Oshxona mudiri narxlar roʻyxatini yoʻqotdi — lekin ikkita "
            "chek qoldi, va ikkita chek ikkita narxni tiklashga yetadi."
        ),
        "order":   16,
        "grammar": [
            {
                "pattern":  "two facts, two unknowns",
                "meaning":  "Ikki nomaʼlum uchun ikkita mustaqil maʼlumot kerak. "
                            "Bitta chek yetmaydi — u cheksiz koʻp narx juftligiga "
                            "toʻgʻri keladi.",
                "examples": ["One receipt was not enough; the second one settled it."],
            },
            {
                "pattern":  "work out / figure out",
                "meaning":  "Hisoblab topmoq. Testda «solve» soʻzining kundalik "
                            "muqobili.",
                "examples": ["She worked out the price of a tea from the second receipt."],
            },
            {
                "pattern":  "the price of one",
                "meaning":  "Bittasining narxi — javob <b>birlik</b> narxi, jami "
                            "emas.",
                "examples": ["What is the price of one sandwich?"],
            },
        ],
        "body": '''<p>The manager of a school <span class="cn-word" data-tr="oshxona">canteen</span> came back from a <span class="cn-word" data-tr="ikki hafta">fortnight</span>'s <span class="cn-word" data-tr="taʼtil">leave</span> to find that the <span class="cn-word" data-tr="narxlar roʻyxati">price list</span> had been taken down for painting and never put back. Nobody could remember what a tea cost.</p>

<p>What she did have were two <span class="cn-word" data-tr="chek, kvitansiya">receipts</span> left in the <span class="cn-word" data-tr="kassa">till</span> <span class="cn-word" data-tr="tortma, quti">drawer</span>. The first was for two teas and three sandwiches, and the total was 31,000 som. The second was smaller: one tea and one sandwich, 12,000 som.</p>

<p>The second receipt is the useful one, and the reason is worth understanding. It tells you that a tea and a sandwich <span class="cn-word" data-tr="birgalikda">together</span> cost 12,000 — so if you know one price, the other is <span class="cn-word" data-tr="hal boʻladi">settled</span> at once.</p>

<p>She used that on the first receipt. Two teas and three sandwiches can be read as two <span class="cn-word" data-tr="juftlik">pairs</span> — that is 24,000 som — plus one <span class="cn-word" data-tr="ortiqcha">extra</span> sandwich. The whole bill was 31,000, so the extra sandwich must have cost <span class="cn-word" data-tr="ayirma, farq">the difference</span>: 7,000 som. Then a tea is 12,000 minus 7,000, or 5,000.</p>

<p>She checked both receipts before writing the new list. Two teas and three sandwiches: 10,000 plus 21,000 is 31,000 ✓. One of each: 5,000 plus 7,000 is 12,000 ✓.</p>

<p>One receipt on its own would have proved nothing — a tea at 4,000 and a sandwich at 8,000 fits it just as well. It took two <span class="cn-word" data-tr="mustaqil">independent</span> facts to pin down two unknown prices, and that is not a coincidence about receipts. It is the rule.</p>''',
        "questions": [
            {
                "text": "What is the price of one sandwich?",
                "choices": ["5,000 som", "7,000 som", "12,000 som"],
                "answer": 1,
                "explanation": "Ikki juftlik 24,000 som; butun chek 31,000 som, demak "
                               "ortiqcha sendvich <b>7,000</b> som. "
                               "<b>5,000</b> — choyning narxi.",
            },
            {
                "text": "Why was one receipt on its own not enough?",
                "choices": [
                    "Because the till drawer was locked.",
                    "Because it did not show the date.",
                    "Because many different pairs of prices would fit it.",
                ],
                "answer": 2,
                "explanation": "Matnda aytilgan: choy 4,000 va sendvich 8,000 ham "
                               "birinchi chekka toʻgʻri kelardi. Ikki nomaʼlum uchun "
                               "<b>ikkita</b> mustaqil maʼlumot kerak.",
            },
            {
                "text": "How much would three teas and two sandwiches cost?",
                "choices": ["24,000 som", "29,000 som", "31,000 som"],
                "answer": 1,
                "explanation": "Choy 5,000, sendvich 7,000: 3 × 5,000 + 2 × 7,000 = "
                               "15,000 + 14,000 = <b>29,000</b> som. Diqqat: bu birinchi "
                               "chekning teskarisi, shuning uchun jami ham boshqa.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-17 — elimination                                      [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Balance and Two Weighings",
        "summary": (
            "SAT-17 matni. Omborchi ikki qutini alohida tortolmaydi — lekin ikkita "
            "tortish yetadi, chunki ikkinchisidan birinchisini ayirish mumkin."
        ),
        "order":   17,
        "grammar": [
            {
                "pattern":  "the difference between the two weighings",
                "meaning":  "Ikki tortish orasidagi farq. Aynan shu farq bitta "
                            "nomaʼlumni <b>yoʻqotadi</b> — yoʻqotish usulining "
                            "amaldagi koʻrinishi.",
                "examples": ["The difference between the two weighings was 17 kilograms."],
            },
            {
                "pattern":  "identical crates",
                "meaning":  "Bir xil qutilar — ularning ogʻirligi teng deb "
                            "hisoblanadi, shuning uchun bitta nomaʼlum yetadi.",
                "examples": ["The small crates are identical, so each weighs the same."],
            },
            {
                "pattern":  "without opening anything",
                "meaning":  "Hech narsani ochmasdan. Matematikaning butun foydasi shu: "
                            "javobni <b>bilvosita</b> topish.",
                "examples": ["He found both weights without opening anything."],
            },
        ],
        "body": '''<p>The <span class="cn-word" data-tr="ombor">warehouse</span> at the edge of the market has one old <span class="cn-word" data-tr="tarozi">balance</span>, and it will take a <span class="cn-word" data-tr="yuk taxtasi">pallet</span> but not a single crate: the <span class="cn-word" data-tr="tortish maydonchasi">platform</span> is too wide to hold one <span class="cn-word" data-tr="qimirlamay">steady</span>.</p>

<p>So when a <span class="cn-word" data-tr="yetkazilgan yuk">delivery</span> arrived as one large crate and several <strong>identical</strong> small ones, the <span class="cn-word" data-tr="omborchi">storekeeper</span> could not simply weigh them one at a time. He weighed them in <span class="cn-word" data-tr="guruhlar">groups</span> instead, and wrote two lines in the book.</p>

<p>The large crate together with one small crate came to 42 kilograms. The large crate together with two small ones came to 59.</p>

<p>Look at what changed between the two weighings. The large crate was on the platform both times, so it cannot explain the difference. Only one extra small crate was added — and the <span class="cn-word" data-tr="koʻrsatkich">reading</span> went up by 17 kilograms. That is the weight of a small crate, and it was found <strong>without opening anything</strong>.</p>

<p>The rest follows in one step. If the large crate and one small crate are 42, and the small crate is 17, then the large crate is 25 kilograms.</p>

<p>The storekeeper does this so often that he has stopped thinking of it as arithmetic. He calls it <span class="cn-word" data-tr="ayirib tashlamoq">taking the first weighing away</span> from the second, and the phrase is exactly right: the load that appears in both <span class="cn-word" data-tr="oʻlchov">measurements</span> <span class="cn-word" data-tr="bekor boʻladi">cancels</span>, and what is left is the thing you wanted to know.</p>''',
        "questions": [
            {
                "text": "How much does one small crate weigh?",
                "choices": ["17 kilograms", "25 kilograms", "42 kilograms"],
                "answer": 0,
                "explanation": "59 − 42 = <b>17</b> kg. Katta quti ikkala tortishda ham "
                               "bor edi, shuning uchun farq faqat qoʻshilgan kichik "
                               "qutiga tegishli.",
            },
            {
                "text": "How much does the large crate weigh?",
                "choices": ["17 kilograms", "25 kilograms", "34 kilograms"],
                "answer": 1,
                "explanation": "42 − 17 = <b>25</b> kg. Kichik qutining ogʻirligi "
                               "topilgach, birinchi tortishdan uni ayirish yetadi.",
            },
            {
                "text": "Why does subtracting one weighing from the other help?",
                "choices": [
                    "Because the balance is more accurate with heavier loads.",
                    "Because the small crates are lighter than the large one.",
                    "Because the load present in both weighings cancels out.",
                ],
                "answer": 2,
                "explanation": "Ikkala tortishda ham qatnashgan yuk <b>bekor "
                               "boʻladi</b> — shuning uchun farqda faqat oʻzgargan "
                               "narsa qoladi. Bu yoʻqotish usulining oʻzi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-18 — word problems                                      [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Inspector Counts Legs",
        "summary": (
            "SAT-18 matni. Nazoratchi hayvonlarni sanashning eski usulini "
            "ishlatadi: boshlarni sanaydi, keyin oyoqlarni — va ikki son yetadi."
        ),
        "order":   18,
        "grammar": [
            {
                "pattern":  "a total of twenty animals",
                "meaning":  "Jami yigirmata hayvon — bu <b>soni</b> haqidagi jumla, "
                            "birinchi tenglama.",
                "examples": ["The yard held a total of twenty animals."],
            },
            {
                "pattern":  "between them",
                "meaning":  "Hammasi birgalikda. Ikkinchi jumla odatda shu ibora "
                            "bilan keladi va <b>qiymat</b> tenglamasini beradi.",
                "examples": ["They had fifty-six legs between them."],
            },
            {
                "pattern":  "suppose they were all …",
                "meaning":  "Faraz qilaylik, hammasi … boʻlsin. Tez yechishning eng "
                            "sodda yoʻli: bir chekkadan boshlab, farqni oʻlchash.",
                "examples": ["Suppose they were all chickens: that is forty legs."],
            },
        ],
        "body": '''<p>A veterinary <span class="cn-word" data-tr="nazoratchi">inspector</span> visiting small farms is required to record how many <span class="cn-word" data-tr="parrandalar">birds</span> and how many <span class="cn-word" data-tr="qoramol">cattle</span> each <span class="cn-word" data-tr="hovli">yard</span> holds. On a wet Tuesday she reached a yard where the owner had gone to town, and the gate was <span class="cn-word" data-tr="qulflangan">locked</span>.</p>

<p>She could see the animals through the <span class="cn-word" data-tr="panjara">railings</span> but could not walk among them, and from where she stood the chickens and the cows kept moving behind one another. Counting each kind <span class="cn-word" data-tr="alohida">separately</span> was <span class="cn-word" data-tr="umidsiz">hopeless</span>. Two things, though, she could count <span class="cn-word" data-tr="aniq">exactly</span>: <strong>a total of twenty animals</strong>, and — with the <span class="cn-word" data-tr="poda">herd</span> standing still in the <span class="cn-word" data-tr="loy">mud</span> — fifty-six legs <strong>between them</strong>.</p>

<p>Two counts, two kinds of animal. That is enough.</p>

<p><strong>Suppose they were all</strong> chickens. Twenty birds would show forty legs, and she had counted fifty-six — sixteen legs more than the <span class="cn-word" data-tr="faraz">supposition</span> allows. Every cow she puts back in place of a chicken adds exactly two legs to the yard, so sixteen extra legs mean eight cows. The other twelve animals are chickens.</p>

<p>She wrote «12 and 8» in the <span class="cn-word" data-tr="daftar, jurnal">register</span>, and checked it at the gate: twelve chickens and eight cows is twenty animals ✓, and twenty-four legs plus thirty-two legs is fifty-six ✓.</p>

<p>The farmer, when he came back, asked how she had managed it through a locked gate. «I counted twice,» she said, «and the second count asked a different question.»</p>''',
        "questions": [
            {
                "text": "How many cows are in the yard?",
                "choices": ["8", "12", "16"],
                "answer": 0,
                "explanation": "Hammasi tovuq boʻlsa 40 ta oyoq boʻlardi; haqiqiy son "
                               "56, ortiqcha 16 ta oyoq. Har bir sigir 2 ta oyoq "
                               "qoʻshadi: 16 ÷ 2 = <b>8</b> ta sigir.",
            },
            {
                "text": "How many chickens are there?",
                "choices": ["8", "12", "20"],
                "answer": 1,
                "explanation": "20 − 8 = <b>12</b> ta tovuq. Tekshiruv: 12 × 2 + "
                               "8 × 4 = 24 + 32 = 56 ta oyoq ✓",
            },
            {
                "text": "Why were two counts necessary?",
                "choices": [
                    "Because the gate was locked and she counted twice to be sure.",
                    "Because chickens are harder to count than cows.",
                    "Because one count cannot separate two kinds of animal.",
                ],
                "answer": 2,
                "explanation": "Faqat boshlar soni (20) tovuq va sigirni ajratmaydi — "
                               "koʻp juftlik unga toʻgʻri keladi. Oyoqlar soni "
                               "<b>ikkinchi, boshqacha</b> savol beradi va shu ikkalasi "
                               "javobni belgilaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-19 — the same line twice                              [Jenny]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Two Signs, One Offer",
        "summary": (
            "SAT-19 matni. Doʻkonda ikkita eʼlon osilgan va xaridorlar qaysi biri "
            "arzon deb bahslashadi — lekin ikkalasi bitta narxni aytadi."
        ),
        "order":   19,
        "grammar": [
            {
                "pattern":  "the same offer written twice",
                "meaning":  "Bitta taklif ikki xil yozilgan. Tenglamalar tilida: "
                            "<b>bitta chiziq</b>, ikki xil koʻrinishda.",
                "examples": ["Those are not two offers; it is the same offer written twice."],
            },
            {
                "pattern":  "works out at",
                "meaning":  "…ga tushadi, yaʼni birlik narxi shuncha chiqadi. "
                            "Taqqoslashning yagona toʻgʻri yoʻli.",
                "examples": ["Both signs work out at eight thousand som a kilogram."],
            },
            {
                "pattern":  "no extra information",
                "meaning":  "Qoʻshimcha maʼlumot yoʻq. Ikkinchi tenglama birinchisining "
                            "karrasi boʻlsa, u hech narsa qoʻshmaydi.",
                "examples": ["The second sign adds no extra information."],
            },
        ],
        "body": '''<p>A dried-fruit <span class="cn-word" data-tr="rasta">stall</span> in the <span class="cn-word" data-tr="usti yopiq bozor">covered market</span> has two <span class="cn-word" data-tr="eʼlon, taxta">boards</span> hanging above it, and for a week the <span class="cn-word" data-tr="xaridorlar">customers</span> <span class="cn-word" data-tr="bahslashdi">argued</span> about which one was the better <span class="cn-word" data-tr="taklif, narx">offer</span>.</p>

<p>The first board says: three kilograms for 24,000 som. The second says: six kilograms for 48,000 som. People who buy a lot pointed at the second board; people buying a little pointed at the first, and both sides felt they had found something.</p>

<p>Neither had. <span class="cn-word" data-tr="boʻling">Divide</span>, and the first board <strong>works out at</strong> 8,000 som a kilogram. Divide the second, and it works out at 8,000 som a kilogram. They are not two prices at all — they are <strong>the same offer written twice</strong>, once at three kilograms and once at double that.</p>

<p>The <span class="cn-word" data-tr="sotuvchi">trader</span> put the second board up because customers buying for a <span class="cn-word" data-tr="toʻy">wedding</span> asked what six kilograms would cost, and he was tired of doing the sum. It was never meant to be a <span class="cn-word" data-tr="chegirma">discount</span>.</p>

<p>There is a small lesson hiding in the argument. If you are told two things and the second is only the first multiplied by two, you have been told <strong>no extra information</strong>. Anything the first board can settle, it settles alone; anything it cannot settle, the second board cannot settle either.</p>

<p>The stall now has one board. Under the price the <span class="cn-word" data-tr="sotuvchi">trader</span> has written, in smaller letters: <span class="cn-word" data-tr="istalgan miqdor uchun, kilogrammi shu narxda">any quantity, at this rate</span>.</p>''',
        "questions": [
            {
                "text": "How much does one kilogram cost under each sign?",
                "choices": ["8,000 som under both", "8,000 under the first and 6,000 under the second",
                            "24,000 under the first and 48,000 under the second"],
                "answer": 0,
                "explanation": "24,000 ÷ 3 = 8,000 va 48,000 ÷ 6 = 8,000 — <b>ikkalasi "
                               "ham</b> bir xil. Ikkinchi eʼlon birinchisining aynan "
                               "ikki barobari.",
            },
            {
                "text": "What would nine kilograms cost at this rate?",
                "choices": ["64,000 som", "72,000 som", "81,000 som"],
                "answer": 1,
                "explanation": "9 × 8,000 = <b>72,000</b> som. Narx nisbati oʻzgarmagani "
                               "uchun istalgan miqdorni bir xil koʻpaytiruvchi bilan "
                               "hisoblash mumkin.",
            },
            {
                "text": "Why does the second board add nothing to what the first one tells you?",
                "choices": [
                    "Because it is simply the first offer multiplied by two.",
                    "Because it is written in smaller letters.",
                    "Because most customers buy less than six kilograms.",
                ],
                "answer": 0,
                "explanation": "Ikkinchi eʼlon — birinchisining karrasi. Tenglamalar "
                               "tilida bu «cheksiz koʻp yechim» holati: ikkita tenglama, "
                               "lekin <b>bitta</b> maʼlumot.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # SAT-20 — parallel prices                                    [Guy]
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "The Fare That Never Catches Up",
        "summary": (
            "SAT-20 matni. Ikki taksi firmasi bir xil kilometr narxini oladi, lekin "
            "chaqiruv haqi har xil — shuning uchun ular hech qachon tenglashmaydi."
        ),
        "order":   20,
        "grammar": [
            {
                "pattern":  "catch up with",
                "meaning":  "Yetib olmoq. Ikki narx tenglashishi uchun biri "
                            "ikkinchisidan <b>tezroq</b> oʻsishi kerak.",
                "examples": ["The cheaper fare never catches up with the dearer one."],
            },
            {
                "pattern":  "the gap stays the same",
                "meaning":  "Oraliq oʻzgarmaydi. Parallel chiziqlarning kundalik "
                            "tildagi taʼrifi.",
                "examples": ["However far you travel, the gap stays the same."],
            },
            {
                "pattern":  "break-even point",
                "meaning":  "Tenglashish nuqtasi — ikki narx teng boʻladigan joy. "
                            "Bu misolda u <b>umuman yoʻq</b>.",
                "examples": ["People kept looking for a break-even point that does not exist."],
            },
        ],
        "body": '''<p>Two taxi firms work the road between the town and the airport, and a local newspaper spent a whole <span class="cn-word" data-tr="maqola">column</span> comparing them last spring.</p>

<p>The first firm charges 5,000 som to come to your door, then 1,200 som for each kilometre. The second charges 10,000 som to come out, then — and this is the part that surprised the paper's <span class="cn-word" data-tr="oʻquvchilar">readers</span> — also 1,200 som a kilometre.</p>

<p>Everybody <span class="cn-word" data-tr="deb oʻyladi">assumed</span> there would be a distance at which the second firm became the better <span class="cn-word" data-tr="tanlov">choice</span>. There is not. For a ten-kilometre <span class="cn-word" data-tr="safar">trip</span> the first firm asks 17,000 som and the second asks 22,000. For a fifty-kilometre trip the first asks 65,000 and the second asks 70,000. The difference is 5,000 som at ten kilometres and 5,000 som at fifty, because the two firms charge the same for every kilometre travelled: only the <span class="cn-word" data-tr="chaqiruv haqi">call-out fee</span> differs, and a fee you pay once does not shrink with distance.</p>

<p>Drawn on a <span class="cn-word" data-tr="grafik">chart</span>, the two fares are two straight lines climbing at exactly the same <span class="cn-word" data-tr="tiklik">steepness</span>, one always five thousand som above the other. <strong>The gap stays the same</strong>, so the lower line never <strong>catches up with</strong> the upper one, and there is no <span class="cn-word" data-tr="kesishish">crossing point</span>.</p>

<p>The column ended with a sentence the <span class="cn-word" data-tr="muharrir">editor</span> liked enough to put in <span class="cn-word" data-tr="qalin harflar">bold</span>: a cheaper <span class="cn-word" data-tr="haq, toʻlov">rate</span> can be caught up with, but a cheaper starting fee, at the same rate, never can.</p>''',
        "questions": [
            {
                "text": "What does a twenty-kilometre trip cost with the first firm?",
                "choices": ["24,000 som", "29,000 som", "34,000 som"],
                "answer": 1,
                "explanation": "5,000 + 20 × 1,200 = 5,000 + 24,000 = <b>29,000</b> som. "
                               "<b>24,000</b> — faqat kilometrlar uchun toʻlov, chaqiruv "
                               "haqisiz.",
            },
            {
                "text": "By how much do the two firms' fares differ on a forty-kilometre trip?",
                "choices": ["5,000 som", "10,000 som", "It depends on the distance"],
                "answer": 0,
                "explanation": "Kilometr narxi bir xil boʻlgani uchun farq har doim "
                               "chaqiruv haqlarining ayirmasi: 10,000 − 5,000 = "
                               "<b>5,000</b> som — masofadan qatʼi nazar.",
            },
            {
                "text": "Why is there no distance at which the two firms cost the same?",
                "choices": [
                    "Because the second firm is always faster.",
                    "Because both charge the same amount per kilometre, so the gap never closes.",
                    "Because the newspaper only compared short trips.",
                ],
                "answer": 1,
                "explanation": "Ikkala narx bir xil tezlikda oʻsadi — grafikda ular "
                               "<b>parallel</b>. Oraliq yopilishi uchun biri tezroq "
                               "oʻsishi kerak edi.",
            },
        ],
    },
]
