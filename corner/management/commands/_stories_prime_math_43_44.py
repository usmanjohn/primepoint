# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-43 va PM-44. BLOK C YAKUNI.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 43 — hikoya (bogʻdagi sahna), 44 — hikoya (ustaxonadagi suhbat).
Ketma-ket ikkita hikoya — tocning qoidasi buzilmaydi (uchtasi taqiqlangan);
oldingi uchtasi kundalik, yangilik va ilmiy-ommabop edi.

⚠️ Kumulyativ: kvadrat tenglama yechilmaydi; 44-matnda formulalar faqat
   SONLAR uchun ishlatiladi — bu ularning eng koʻrinarli foydasi.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_43_44.py --author=prime
"""

SUBJECT = {
    "name":    "Matematika",
    "summary": "Matematika: hayotdagi matnlar, atamalar va matematik hikoyalar.",
    "icon":    "bi-calculator",
    "color":   "#f59e0b",
    "order":   7,
}

COLLECTION = {
    "title":       "Prime Math Readings",
    "description": (
        "Prime Math darslarining oʻqish matnlari — har biri oʻz darsining "
        "matematikasini hayotdagi matn ichida koʻrsatadi. Atamalar izohi bilan."
    ),
    "order": 1,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PM-43 — koʻphadlar                                       HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bogʻ maydonini hisoblash",
        "summary": (
            "PM-43 matni. Hikoya: bobosi bogʻni kengaytirmoqchi, lekin aniq "
            "oʻlchamni bilmaydi. Nabirasi yuzani koʻphad bilan yozadi va javob "
            "har qanday oʻlcham uchun tayyor boʻlib qoladi."
        ),
        "order":   43,
        "grammar": [
            {
                "pattern":  "(a + b)(c + d) — toʻrtta koʻpaytma",
                "meaning":  "Birinchi qavsning har bir hadi ikkinchi qavsning har "
                            "bir hadiga koʻpaytiriladi. Toʻrtburchakning yuzasi "
                            "ham xuddi shunday toʻrtta boʻlakka ajraladi.",
                "examples": [
                    "(x + 3)(x + 5) = x² + 5x + 3x + 15 = x² + 8x + 15",
                    "x = 10 → 100 + 80 + 15 = 195; tekshiruv: 13 × 15 = 195",
                ],
            },
        ],
        "questions": [
            {
                "text": "Bobosi nima uchun aniq javob ololmadi?",
                "choices": [
                    "Bogʻning hozirgi enini oʻlchamagan edi",
                    "Hisoblashni bilmasdi",
                    "Bogʻ juda katta edi",
                    "Rulyetkasi yoʻq edi",
                ],
                "answer": 0,
                "explanation": "Eni nomaʼlum boʻlgani uchun aniq son chiqmasdi. "
                               "Shuning uchun nabirasi javobni koʻphad koʻrinishida "
                               "yozdi — u har qanday eni uchun ishlaydi.",
            },
            {
                "text": "Eni x, boʻyi x + 5 boʻlgan bogʻning eniga 3 metr "
                        "qoʻshilsa, yuza qanday yoziladi?",
                "choices": ["x² + 15", "x² + 8x + 15", "x² + 8x", "x² + 5x + 3"],
                "answer": 1,
                "explanation": "(x + 3)(x + 5) = x² + 5x + 3x + 15 = x² + 8x + 15. "
                               "Toʻrtta koʻpaytmadan ikkitasi oʻxshash — ular "
                               "yigʻiladi.",
            },
            {
                "text": "Eni 10 metr boʻlsa, yangi bogʻning yuzasi qancha?",
                "choices": ["150 m²", "180 m²", "195 m²", "225 m²"],
                "answer": 2,
                "explanation": "100 + 80 + 15 = 195 m². Tekshirish: eni 13 m, "
                               "boʻyi 15 m; 13 × 15 = 195 ✓",
            },
        ],
        "body": """
<p>Bobosi bogʻ chetida turib, qoʻli bilan yerni koʻrsatdi.</p>

<p>— Mana shu tomonga uch metr qoʻshsam, bogʻ qancha boʻladi? — soʻradi u
Bekzoddan.</p>

<p>— Hozirgi eni qancha? — dedi Bekzod.</p>

<p>Bobosi yelka qisdi. Rulyetka uyda qolgan, eni esa yodida yoʻq edi. Faqat bir
narsani aniq bilardi: <b>boʻyi enidan 5 metr uzun</b>.</p>

<p>Bekzod bir zum oʻyladi, keyin daftarini ochdi.</p>

<p>— Unda enini <span class="cn-word" data-tr="qiymati nomaʼlum boʻlgan miqdorning nomi">nomaʼlum</span> sifatida <b>x</b> deb olaman, — dedi u. — Boʻyi <b>x + 5</b> boʻladi. Uch
metr qoʻshsak, yangi eni <b>x + 3</b>.</p>

<p><span class="cn-word" data-tr="shaklning ichki oʻlchami">Yuza</span> — tomonlar koʻpaytmasi, demak <strong>(x + 3)(x + 5)</strong>. Bekzod bu
<span class="cn-word" data-tr="ikki qavsni bir-biriga koʻpaytirish">koʻpaytma</span>ni
ochdi: birinchi qavsning har bir hadi ikkinchisining har bir hadiga koʻpaytiriladi
— jami toʻrtta boʻlak.</p>

<p>x·x = x², x·5 = 5x, 3·x = 3x, 3·5 = 15. Oʻrtadagi ikkitasi
<span class="cn-word" data-tr="harf qismi bir xil hadlar">oʻxshash had</span>lar
edi, ularni yigʻdi: <strong>x² + 8x + 15</strong>.</p>

<p>— Bu nima degani? — soʻradi bobosi.</p>

<p>— Bu javob emas, bobo, bu <span class="cn-word" data-tr="bir necha haddan tuzilgan ifoda">koʻphad</span>.
Enini oʻlchab kelsangiz, javob bir zumda chiqadi.</p>

<p>Ertasi kuni bobosi rulyetka bilan qaytdi: eni roppa-rosa <strong>10</strong>
metr. Bekzod harf oʻrniga sonni qoʻydi: 100 + 80 + 15 =
<strong>195</strong> kvadrat metr.</p>

<p><span class="cn-word" data-tr="javobni asl shartga qoʻyib sinash">Tekshirish</span>
ham oson boʻldi: yangi eni 13, boʻyi 15; 13 × 15 = 195 ✓ Eski bogʻ esa
10 × 15 = 150 kvadrat metr edi — kengaytirish 45 kvadrat metr qoʻshgan.</p>

<p>— Qiziq, — dedi bobosi. — Sen javobni <b>oʻlchashdan oldin</b> topib
qoʻyibsan.</p>

<p>— Ha, — kuldi Bekzod. — Harf shuning uchun kerak ekan.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-44 — qisqa koʻpaytirish                              HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ustaning tez hisoblash hiylasi",
        "summary": (
            "PM-44 matni. Hikoya: ustaxonadagi usta 103 × 97 ni bir zumda "
            "hisoblaydi. Sir — kvadratlar ayirmasi formulasida, va uni maktabda "
            "oʻrgatishadi."
        ),
        "order":   44,
        "grammar": [
            {
                "pattern":  "(a − b)(a + b) = a² − b²",
                "meaning":  "Ikki son biror yumaloq sondan teng uzoqlikda boʻlsa, "
                            "ularning koʻpaytmasi oʻsha yumaloq sonning kvadratidan "
                            "farqning kvadratini ayirganga teng. Oʻrta hadlar "
                            "bir-birini yoʻq qiladi.",
                "examples": [
                    "103 × 97 = (100 + 3)(100 − 3) = 10 000 − 9 = 9991",
                    "51 × 49 = (50 + 1)(50 − 1) = 2500 − 1 = 2499",
                ],
            },
        ],
        "questions": [
            {
                "text": "Usta hisobni qanday tez bajardi?",
                "choices": [
                    "Kalkulyatordan foydalandi",
                    "Ikki sonni yuzdan teng uzoqlikda deb koʻrdi",
                    "Javobni yoddan bilardi",
                    "Gʻishtlarni birma-bir sanadi",
                ],
                "answer": 1,
                "explanation": "103 va 97 — yuzdan uch qadam narida. Shuning uchun "
                               "kvadratlar ayirmasi formulasi ishladi.",
            },
            {
                "text": "103 × 97 nechaga teng?",
                "choices": ["9909", "9991", "9997", "10 009"],
                "answer": 1,
                "explanation": "(100 + 3)(100 − 3) = 10 000 − 9 = 9991.",
            },
            {
                "text": "Shu usul bilan 51 × 49 nechaga teng?",
                "choices": ["2401", "2450", "2499", "2500"],
                "answer": 2,
                "explanation": "(50 + 1)(50 − 1) = 2500 − 1 = 2499. Yumaloq son "
                               "50, farq esa 1.",
            },
        ],
        "body": """
<p>Ustaxonada gʻisht sanashardi. Usta Karim aka daftarga qaradi va shunday dedi:</p>

<p>— Yuz uchta gʻishtdan toʻqson yetti qator. Jami toʻqqiz ming toʻqqiz yuz toʻqson
bir.</p>

<p>Jasur qoʻlidagi telefonni endi ochgan edi. Kalkulyator ham xuddi shu sonni
koʻrsatdi: <strong>9991</strong>.</p>

<p>— Qanday qildingiz? — soʻradi u.</p>

<p>— Yuz uch va toʻqson yetti, — dedi Karim aka. — Ikkalasi ham
<b>yuzdan uch qadam</b> narida. Biri koʻp, biri kam. Shunda yuzning kvadratidan
uchning kvadratini ayirasan: oʻn ming minus toʻqqiz.</p>

<p>Jasur hayron qoldi — bu ularning oʻtgan haftadagi darsi edi. Doskada <span class="cn-word" data-tr="harflar bilan yozilgan umumiy qoida">formula</span> turgan edi.
<span class="cn-word" data-tr="a² − b² koʻrinishidagi formula">Kvadratlar ayirmasi</span>:
<strong>(a + b)(a − b) = a² − b²</strong>.</p>

<p>Uni ochib koʻrsa, sabab koʻrinadi. Toʻrtta <span class="cn-word" data-tr="koʻpaytirish natijasi">koʻpaytma</span>dan ikkitasi — <b>+ab</b> va
<b>−ab</b> — bir-birini yoʻq qiladi. Qolgani ikkita
<span class="cn-word" data-tr="sonning oʻziga koʻpaytmasi">kvadrat</span> va
ularning ayirmasi.</p>

<p>— Yana bittasini ayting, — dedi Jasur.</p>

<p>— Ellik bir karra qirq toʻqqiz, — dedi usta darrov. — Ikki ming toʻrt yuz toʻqson
toʻqqiz.</p>

<p>Jasur daftarda tekshirdi: (50 + 1)(50 − 1) = 2500 − 1 = <strong>2499</strong>.
Toʻgʻri.</p>

<p>— Bu hiyla emas ekan, — dedi u. — Bu
<span class="cn-word" data-tr="har qanday qiymatda rost boʻladigan tenglik">formula</span>.</p>

<p>— Menga buni otam oʻrgatgan, — dedi Karim aka. — U maktabni tugatmagan, lekin
gʻishtni koʻp sanagan. Sen esa uni maktabda oʻrganyapsan. Ikkovimiz bir joyga
kelibmiz.</p>

<p>Jasur uyga qaytayotib yana bir necha
<span class="cn-word" data-tr="ogʻzaki, qogʻozsiz hisoblash">ogʻzaki hisob</span>
sinab koʻrdi: 102² = 10 404, 98² = 9604. Formulalar sonlar bilan ham xuddi harflar
bilangidek ishlar ekan.</p>

<p>Aslida ular <b>faqat sonlar uchun</b> oʻylab topilgan. Harflar keyin
qoʻshilgan — qoidani bir marta yozib qoʻyish uchun.</p>
""",
    },
]
