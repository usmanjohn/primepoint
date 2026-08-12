# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-54, PM-55, PM-56.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 54 — hikoya (teatr kassasidagi ikki chek), 55 — tarix (qadimgi xitoy
masalasi, haqiqiy manba bilan), 56 — sport (mashgʻulotdagi oʻlchov). Oldingi
uchtasi sport, sharh va hikoya edi; ketma-ket uchta bir xil shakl chiqmaydi.

⚠️ Kumulyativ: kvadrat tenglamani yechish YOʻQ, parabolaning uchi formulasi
   YOʻQ. 54 va 55 — qoʻshish/ayirish usuli (PM-54), 56 — faqat y = x² ni
   oʻqish va simmetriya (PM-56).
⚠️ `grammar.pattern` va `examples` ekranlanadi — <sup> emas, Unicode ² yoziladi.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_54_56.py --author=prime
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
    # PM-54 — qoʻshish usuli                                     HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ikki xil chipta",
        "summary": (
            "PM-54 matni. Hikoya: teatr kassasida narxlar yozilgan taxta "
            "olib qoʻyilgan. Ikki sinfning cheklarida bir xil narsa — ikkita "
            "katta chipta — turgani Sherbekka narxlarni topish yoʻlini beradi."
        ),
        "order":   54,
        "grammar": [
            {
                "pattern":  "bir xil koeffitsient — ayiramiz, qarama-qarshi — qoʻshamiz",
                "meaning":  "Ikki tenglamada bir xil turgan qism ayirilganda "
                            "yoʻqoladi. Shundan keyin bitta nomaʼlumli oddiy "
                            "tenglama qoladi.",
                "examples": [
                    "7-B: 2k + 24b = 300 000",
                    "7-A: 2k + 20b = 260 000",
                    "ayiramiz: 4b = 40 000, demak b = 10 000",
                    "2k = 260 000 − 200 000 = 60 000, demak k = 30 000",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega Sherbek ikki chekni bir-biridan ayirdi?",
                "choices": [
                    "Ikkala sinf ham bir xil pul toʻlagani uchun",
                    "Ikkala chekda ham xuddi shu 2 ta katta chipta turgani uchun",
                    "Chiptalar soni ikkala chekda ham teng boʻlgani uchun",
                    "Kassir shunday qilishni aytgani uchun",
                ],
                "answer": 1,
                "explanation": "Ikkala chekda ham 2 ta katta chipta bor edi — "
                               "bu bir xil qism. Ayirilganda u yoʻqoladi va "
                               "faqat qoʻshimcha 4 ta bola chiptasi bilan "
                               "40 000 soʻm farq qoladi.",
            },
            {
                "text": "Bitta bola chiptasi necha soʻm turadi?",
                "choices": ["5 000 soʻm", "8 000 soʻm", "10 000 soʻm",
                            "12 000 soʻm"],
                "answer": 2,
                "explanation": "Ikki chekning farqi 300 000 − 260 000 = 40 000 "
                               "soʻm, farqni esa atigi 4 ta bola chiptasi hosil "
                               "qilgan: 40 000 ÷ 4 = 10 000 soʻm.",
            },
            {
                "text": "7-A sinf 20 ta bola chiptasi uchun jami qancha toʻladi?",
                "choices": ["200 000 soʻm", "240 000 soʻm", "260 000 soʻm",
                            "300 000 soʻm"],
                "answer": 0,
                "explanation": "Bitta bola chiptasi 10 000 soʻm, demak "
                               "20 × 10 000 = 200 000 soʻm. Qolgan 60 000 soʻm — "
                               "ikkita katta chiptaning puli, yaʼni bittasi "
                               "30 000 soʻm.",
            },
        ],
        "body": """
<p>Qoʻgʻirchoq teatri kassasi oldida ikki sinf navbatda turardi. Devordagi
narxlar taxtasi olib qoʻyilgan edi — uni boʻyashga olib ketishgan.</p>

<p>Nodira opa 7-A sinf uchun 2 ta katta va 20 ta bola chiptasini oldi.
Chekda <strong>260 000</strong> soʻm yozilgandi. Keyin Karim aka 7-B uchun
2 ta katta va 24 ta bola chiptasini oldi. Uning cheki
<strong>300 000</strong> soʻm boʻldi.</p>

<p>«Bitta chipta qancha ekan?» — soʻradi Bekzod. Kassir shoshib turardi.</p>

<p>Sherbek ikki chekni yonma-yon qoʻydi. Ikkalasida ham
<span class="cn-word" data-tr="nomaʼlum oldida turgan son">koeffitsient</span>
bir xil edi: ikkala sinf ham xuddi 2 tadan katta chipta olgan.</p>

<p>«Demak farqni faqat bola chiptalari hosil qilgan», — dedi u. Ikki
<span class="cn-word" data-tr="ikki ifoda tengligini bildiruvchi yozuv">tenglama</span>ni
qogʻozga tushirdi va ularni bir-biridan
<span class="cn-word" data-tr="tenglamalarni qoʻshib yoki ayirib nomaʼlumni yoʻqotish usuli">ayirdi</span>.
Katta chiptalar <span class="cn-word" data-tr="nomaʼlumni tenglamadan butunlay chiqarib yuborish">yoʻqoldi</span>:
4 ta bola chiptasi <strong>40 000</strong> soʻm.</p>

<p>Qolgani oson edi. Bitta bola chiptasi <strong>10 000</strong> soʻm. Uni
birinchi <span class="cn-word" data-tr="bir vaqtda bajarilishi kerak boʻlgan ikki tenglama">sistema</span>ga
qaytarib qoʻydi: 20 ta bola chiptasi 200 000 soʻm, demak ikkita katta chipta
60 000 soʻm — bittasi <strong>30 000</strong>.</p>

<p><span class="cn-word" data-tr="topilgan javobni dastlabki shartga qaytarib qoʻyish">Tekshirdi</span>:
2 × 30 000 + 24 × 10 000 = 300 000 ✓. Ikkinchi chek ham toʻgʻri chiqdi.</p>

<p>«Taxta kerak emas ekan», — kuldi Nodira opa. — «Ikkita chekning oʻzi
yetibdi.» Bu Sherbek topgan <span class="cn-word" data-tr="sistemani bajaradigan sonlar juftligi">yechim</span>
edi — ikkita <span class="cn-word" data-tr="qiymati topilishi kerak boʻlgan, harf bilan belgilangan miqdor">nomaʼlum</span>,
ikkita chek.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-55 — sistemali matnli masala                             TARIX
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Tovuq va quyon — qadimiy masala",
        "summary": (
            "PM-55 matni. Tarix: taxminan bir yarim ming yil avval xitoy "
            "kitobi «Sun-szi suan-szin»da yozilgan mashhur masala — 35 bosh, "
            "94 oyoq — va uning sistema bilan yechilishi."
        ),
        "order":   55,
        "grammar": [
            {
                "pattern":  "t + q = 35 va 2t + 4q = 94",
                "meaning":  "Ikki nomaʼlum — ikki tenglama, va ular matnning "
                            "<b>boshqa-boshqa</b> jumlalaridan olinadi: biri "
                            "boshlar soni haqida, ikkinchisi oyoqlar soni haqida.",
                "examples": [
                    "birinchisini 2 ga koʻpaytiramiz: 2t + 2q = 70",
                    "ikkinchisidan ayiramiz: 2q = 24, demak q = 12",
                    "t = 35 − 12 = 23",
                    "tekshirish: 23 × 2 + 12 × 4 = 46 + 48 = 94",
                ],
            },
        ],
        "questions": [
            {
                "text": "Bu masala birinchi marta qayerda yozib qoldirilgan?",
                "choices": [
                    "Qadimgi Misr papiruslarida",
                    "Yunon olimi Evklid kitobida",
                    "Xitoy kitobi «Sun-szi suan-szin»da",
                    "Al-Xorazmiyning algebra kitobida",
                ],
                "answer": 2,
                "explanation": "Matnda aytilgan: masala taxminan bir yarim ming "
                               "yil avval yozilgan xitoy kitobi «Sun-szi "
                               "suan-szin»da uchraydi. Yaponiyada u «turna va "
                               "toshbaqa masalasi» nomi bilan tanilgan.",
            },
            {
                "text": "Qafasda nechta quyon bor edi?",
                "choices": ["10 ta", "12 ta", "15 ta", "23 ta"],
                "answer": 1,
                "explanation": "t + q = 35 va 2t + 4q = 94. Birinchi tenglamani "
                               "2 ga koʻpaytirsak 2t + 2q = 70; ikkinchisidan "
                               "ayirsak 2q = 24, demak q = 12. Tovuqlar esa "
                               "35 − 12 = 23 ta.",
            },
            {
                "text": "Agar qafasdagi 35 ta jonivorning hammasi tovuq boʻlganida, "
                        "oyoqlar soni qancha boʻlardi?",
                "choices": ["70 ta", "94 ta", "105 ta", "140 ta"],
                "answer": 0,
                "explanation": "Har bir tovuqning 2 ta oyogʻi bor: 35 × 2 = 70. "
                               "Haqiqiy son esa 94 — ortiqcha 24 ta oyoq "
                               "quyonlarga tegishli, chunki har bir quyon "
                               "tovuqdan 2 ta oyoq koʻp: 24 ÷ 2 = 12 ta quyon.",
            },
        ],
        "body": """
<p>Taxminan bir yarim ming yil avval Xitoyda «Sun-szi suan-szin» degan hisob
kitobi yozilgan. Uning sahifalarida bugun ham maktablarda beriladigan bir
masala bor.</p>

<p>Masala shunday: qafasda tovuqlar va quyonlar bor. Yuqoridan qaraganda
<strong>35</strong> ta bosh koʻrinadi. Pastdan qaraganda
<strong>94</strong> ta oyoq. Nechta tovuq va nechta quyon bor?</p>

<p>Yaponiyada bu masalani «turna va toshbaqa masalasi» deb atashadi —
jonivorlar boshqa, matematikasi bir xil.</p>

<p>Yechish avval <span class="cn-word" data-tr="nomaʼlumga harf va birlik berish">belgilash</span>dan
boshlanadi: t — tovuqlar soni, q — quyonlar soni. Keyin matnning ikki
<span class="cn-word" data-tr="masaladagi berilgan maʼlumot">shart</span>i
ikki <span class="cn-word" data-tr="ikki ifoda tengligini bildiruvchi yozuv">tenglama</span>ga
aylanadi. Boshlar: t + q = 35. Oyoqlar: 2t + 4q = 94, chunki tovuqning ikkita,
quyonning toʻrtta oyogʻi bor.</p>

<p>Ikki tenglama birga — bu <span class="cn-word" data-tr="bir vaqtda bajarilishi kerak boʻlgan ikki tenglama">sistema</span>.
Birinchisini 2 ga <span class="cn-word" data-tr="tenglamaning har bir hadini songa koʻpaytirish">koʻpaytiramiz</span>:
2t + 2q = 70. Endi ikkala tenglamada ham 2t turibdi, demak
<span class="cn-word" data-tr="tenglamalarni ayirib nomaʼlumni yoʻqotish usuli">ayiramiz</span>
va t <span class="cn-word" data-tr="nomaʼlumni tenglamadan butunlay chiqarib yuborish">yoʻqoladi</span>:
2q = 24.</p>

<p><span class="cn-word" data-tr="sistemani bajaradigan sonlar juftligi">Yechim</span>:
<strong>12</strong> ta quyon va <strong>23</strong> ta tovuq.</p>

<p><span class="cn-word" data-tr="topilgan javobni dastlabki shartga qaytarib qoʻyish">Tekshiramiz</span>:
12 + 23 = 35 ta bosh ✓, 12 × 4 + 23 × 2 = 48 + 46 = 94 ta oyoq ✓. Bir yarim
ming yil oʻtib ham javob oʻsha-oʻsha.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-56 — parabola                                            SPORT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Toʻpning yoʻli",
        "summary": (
            "PM-56 matni. Sport: mashgʻulotda bolalar toʻpning balandligini "
            "har ikki metrda oʻlchashadi va oʻlchov qogʻozida agʻdarilgan "
            "parabola — simmetrik egri chiziq paydo boʻladi."
        ),
        "order":   56,
        "grammar": [
            {
                "pattern":  "y = x² parabolasi simmetrik: bitta y ga ikkita x",
                "meaning":  "Parabolaning ikki tarmogʻi <b>simmetriya oʻqi</b>ga "
                            "nisbatan koʻzguday teng. Shuning uchun bir xil "
                            "balandlik yoʻlning ikki joyida uchraydi: bir marta "
                            "koʻtarilishda, bir marta tushishda.",
                "examples": [
                    "2 m da 3 m balandlik, 6 m da yana 3 m balandlik",
                    "uchi 4 m masofada — eng baland nuqta",
                    "y = x² jadvali: 1, 4, 9, 16, 25 — oʻsishlar 3, 5, 7, 9",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega Karim aka toʻpning yoʻlini «agʻdarilgan parabola» "
                        "deb atadi?",
                "choices": [
                    "Toʻp juda tez uchgani uchun",
                    "Tarmoqlari pastga qaragani, uchi esa eng baland nuqta "
                    "boʻlgani uchun",
                    "Chiziq toʻgʻri boʻlmagani uchun",
                    "Oʻlchovlar notoʻgʻri chiqqani uchun",
                ],
                "answer": 1,
                "explanation": "y = x² parabolasining tarmoqlari yuqoriga "
                               "qaraydi va uchi eng past nuqta boʻladi. Toʻpning "
                               "yoʻlida esa buning aksi: tarmoqlar pastga, uchi "
                               "eng baland nuqta — yaʼni y = −x² shakli.",
            },
            {
                "text": "Toʻp qaysi ikki masofada 3 metr balandlikda boʻlgan?",
                "choices": [
                    "1 va 7 metrda",
                    "2 va 4 metrda",
                    "2 va 6 metrda",
                    "4 va 6 metrda",
                ],
                "answer": 2,
                "explanation": "Oʻlchov qogʻoziga koʻra 2 metrda 3 m va 6 metrda "
                               "yana 3 m. Ikkalasi eng baland nuqtadan (4 metr) "
                               "bir xil uzoqlikda — mana shu parabolaning "
                               "simmetriyasi.",
            },
            {
                "text": "y = x² jadvalida x = 5 dan x = 6 ga oʻtganda y qanchaga "
                        "oʻsadi?",
                "choices": ["1 ga", "7 ga", "9 ga", "11 ga"],
                "answer": 3,
                "explanation": "5² = 25 va 6² = 36, demak oʻsish 36 − 25 = 11. "
                               "Toʻgʻri chiziqda oʻsish har doim bir xil "
                               "boʻlardi; parabolada esa oʻsishlar 3, 5, 7, 9, 11 "
                               "— tobora kattalashadi.",
            },
        ],
        "body": """
<p>Shanba kuni mashgʻulotdan keyin Karim aka bolalarni maydon chetiga chaqirdi.
Qoʻlida uzun oʻlchov lentasi bor edi.</p>

<p>«Bekzod toʻpni tepadi, siz esa uning balandligini oʻlchaysiz», — dedi u.
Bolalar maydonga har ikki metrda bittadan turib chiqishdi.</p>

<p>Bekzod tepdi. Sherbek raqamlarni daftariga yozdi: tepilgan joyda 0,
2 metrda <strong>3</strong> metr, 4 metrda <strong>4</strong> metr, 6 metrda
yana <strong>3</strong> metr, 8 metrda esa toʻp yerga tegdi.</p>

<p>Keyin u bu <span class="cn-word" data-tr="qiymatlar yozib chiqilgan qator">jadval</span>ni
qogʻozdagi <span class="cn-word" data-tr="ikki oʻq bilan yasalgan tekislik">koordinata</span>
oʻqlariga <span class="cn-word" data-tr="(x; y) juftligi belgilangan joy">nuqta</span>lar
qilib qoʻydi va ularni silliq tutashtirdi. Toʻgʻri chiziq emas,
<span class="cn-word" data-tr="toʻgʻri boʻlmagan chiziq">egri chiziq</span> chiqdi.</p>

<p>«Buning nomi bor», — dedi murabbiy. — «<span class="cn-word" data-tr="y = x² koʻrinishidagi funksiyaning egri grafigi">Parabola</span>.
Faqat agʻdarilgani: <span class="cn-word" data-tr="uchidan ketgan ikki qanot">tarmoqlar</span>i
pastga qaragan, <span class="cn-word" data-tr="parabolaning burilish nuqtasi">uchi</span> esa
eng baland nuqta.»</p>

<p>Sherbek yana bir narsani sezdi: 2 metrdagi balandlik bilan 6 metrdagi
balandlik teng. Ikkalasi eng baland nuqtadan bir xil uzoqlikda edi. Bu —
<span class="cn-word" data-tr="grafikni ikki teng yarimga boʻluvchi chiziq">simmetriya oʻqi</span>.</p>

<p>Uyda u y = x² <span class="cn-word" data-tr="kirish → qoida → chiqish bogʻlanishi">funksiya</span>sining
jadvalini tuzdi: 1, 4, 9, 16, 25. Oʻsishlar esa 3, 5, 7, 9 — tobora katta.
Shuning uchun ham <span class="cn-word" data-tr="y = kx + b, grafigi toʻgʻri chiziq">chiziqli funksiya</span>dan
farqli oʻlaroq, parabola tikroq boʻlib boradi.</p>
""",
    },
]
