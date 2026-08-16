# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-75, PM-76, PM-77 (Blok F ning boshi).

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 75 — intervyu, 76 — ilmiy-ommabop, 77 — yangilik.
Oldingi uchlik tarix/sharh/hikoya edi.

⚠️ Kumulyativ:
   • 75-matnda DIAGRAMMA soʻzi ham YOʻQ — faqat soʻrov, jadval va foiz;
   • 76-matnda uchta tur va sektor burchagi;
   • 77-matnda diagrammani oʻqish. ⛔ «Oʻrtacha» atama sifatida
     ishlatilmaydi (PM-78), aldamchi diagramma ham yoʻq (PM-81).
⚠️ `grammar.pattern` va `examples` ekranlanadi — <sup> emas.
⚠️ Savollar SAQLANGAN TARTIBDA koʻrsatiladi — `answer` indekslari qoʻlda
   oʻzgartirilgan: 75 → 1/2/0, 76 → 2/0/1, 77 → 3/1/2.
⚠️ 77-matndagi yomgʻir sonlari maktabning oʻz yomgʻir oʻlchagichidan
   olingan qayd sifatida beriladi — rasmiy statistika deb koʻrsatilmaydi.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_75_77.py --author=prime
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
    # PM-75 — soʻrovnoma va jadval                             INTERVYU
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Sinfda kim nima yeydi — soʻrovnoma hisoboti",
        "summary": (
            "PM-75 matni. Intervyu: maktab gazetasi Afsonadan uning "
            "nonushta soʻrovi haqida soʻraydi — savolni qanday tuzgani, "
            "kimdan soʻragani va jadvalni qanday tekshirgani."
        ),
        "order":   75,
        "grammar": [
            {
                "pattern":  "foiz = ulush ÷ jami × 100",
                "meaning":  "Chastotani foizga aylantirish. Foiz har doim "
                            "soʻralganlarning umumiy soniga nisbatan "
                            "olinadi — shuning uchun jamini bilmasdan "
                            "foiz haqida gapirib boʻlmaydi.",
                "examples": [
                    "12 ÷ 30 × 100 = 40% (non va choy)",
                    "3 ÷ 30 × 100 = 10% (hech narsa yemaydiganlar)",
                    "tekshiruv: 40 + 30 + 20 + 10 = 100%",
                ],
            },
        ],
        "questions": [
            {
                "text": "Afsona nega «Sogʻlom ovqatlanasizmi?» degan savolni "
                        "tashlab yubordi?",
                "choices": [
                    "Chunki savol juda uzun edi",
                    "Chunki bunday savolga hamma «ha» deydi va sanab "
                    "boʻladigan javob chiqmaydi",
                    "Chunki oʻqituvchi ruxsat bermadi",
                    "Chunki nonushta haqida savol berish qiyin edi",
                ],
                "answer": 1,
                "explanation": "Soʻrovnoma savoli sanab boʻladigan javob "
                               "berishi kerak. «Sogʻlom ovqatlanasizmi?» ga "
                               "deyarli hamma «ha» deydi va hech qanday "
                               "maʼlumot chiqmaydi. «Bugun nonushtaga nima "
                               "yedingiz?» esa aniq toifalar beradi.",
            },
            {
                "text": "Nonushta qilmaydiganlar necha foizni tashkil "
                        "qiladi?",
                "choices": ["3%", "6%", "10%", "30%"],
                "answer": 2,
                "explanation": "Uch oʻquvchi hech narsa yemagan, jami esa "
                               "30 kishi: 3 ÷ 30 × 100 = 10%. «3%» — "
                               "chastotaning oʻzi foiz deb yozib yuborilgan "
                               "boʻlardi.",
            },
            {
                "text": "Non va choy tanlaganlar tuxum tanlaganlardan "
                        "nechtaga koʻp?",
                "choices": ["3 taga", "4 taga", "9 taga", "21 taga"],
                "answer": 0,
                "explanation": "12 − 9 = 3 ta. Diqqat: «nechtaga koʻp» — "
                               "ayirish. Agar «necha marta koʻp» deb "
                               "soʻralganida, boʻlish kerak boʻlardi.",
            },
        ],
        "body": """
<p><b>Maktab gazetasi:</b> Afsona, siz oʻtgan hafta butun sinfda
<span class="cn-word" data-tr="savol berib maʼlumot yigʻish">soʻrovnoma</span>
oʻtkazdingiz. Nimadan boshladingiz?</p>

<p><b>Afsona:</b> Savoldan. Bu eng qiyin qismi ekan. Avval
«Sogʻlom ovqatlanasizmi?» deb yozgandim. Keyin oʻyladim: bunga hamma
«ha» deydi-ku. Bunday savoldan hech qanday
<span class="cn-word" data-tr="yigʻilgan faktlar va sonlar">maʼlumot</span>
chiqmaydi.</p>

<p><b>Gazeta:</b> Nima deb oʻzgartirdingiz?</p>

<p><b>Afsona:</b> «Bugun nonushtaga nima yedingiz?» Bu savolga javoblar
sanab boʻladigan boʻlib chiqdi — har biri oʻz
<span class="cn-word" data-tr="javoblar ajratilgan guruh">toifa</span>siga
tushdi.</p>

<p><b>Gazeta:</b> Kimdan soʻradingiz?</p>

<p><b>Afsona:</b> 6-B sinfning hamma oʻquvchisidan — <strong>30</strong>
kishi. Bu mening
<span class="cn-word" data-tr="soʻrov oʻtkazilgan odamlar guruhi">soʻralganlar</span>
sonim. Buni alohida yozib qoʻydim, chunki «sinfning 40 foizi» degani
«maktabning 40 foizi» degani emas.</p>

<p><b>Gazeta:</b> Javoblarni qanday sanadingiz?</p>

<p><b>Afsona:</b>
<span class="cn-word" data-tr="beshtadan guruhlab sanash usuli">Chiziqcha</span>
bilan. Har beshinchisini qiya tortdim, keyin beshtalab sanab chiqdim.
Bittalab sanaganimda ikki marta adashgandim.</p>

<p><b>Gazeta:</b> Natija qanday?</p>

<p><b>Afsona:</b> Non va choy — <strong>12</strong> kishi, tuxum —
<strong>9</strong>, boʻtqa — <strong>6</strong>. Va uch kishi hech narsa
yemagan.</p>

<p><b>Gazeta:</b> Bu sonlarni qanday tekshirdingiz?</p>

<p><b>Afsona:</b> Ikki marta.
<span class="cn-word" data-tr="bir javob necha marta uchragani">Chastota</span>larni
qoʻshdim: 12 + 9 + 6 + 3 = <strong>30</strong> — soʻralganlar soniga
toʻgʻri keldi. Keyin
<span class="cn-word" data-tr="yuzdan boʻlak, %">foiz</span>larni
hisobladim: 40%, 30%, 20% va 10%. Ularning
<span class="cn-word" data-tr="qoʻshish natijasi">yigʻindi</span>si ham
<strong>100</strong> chiqdi. Ikkalasi ham toʻgʻri kelmasa,
<span class="cn-word" data-tr="javob va uning soni yozilgan jadval">jadval</span>da
xato bor degani.</p>

<p><b>Gazeta:</b> Sizni nima koʻproq hayratlantirdi?</p>

<p><b>Afsona:</b> Oʻsha uch kishi. Bu koʻp emasdek koʻrinadi, lekin bu
har oʻninchi oʻquvchi. Yalangʻoch son «uch» hech nima demaydi —
<span class="cn-word" data-tr="butundan tegishli qism">ulush</span>ni
bilganingizdan keyin u boshqacha eshitiladi.</p>

<p><b>Gazeta:</b> Endi nima qilasiz?</p>

<p><b>Afsona:</b> Xuddi shu savolni boshqa sinflarda ham beraman. Bitta
sinf — bu hali butun maktab emas.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-76 — diagramma turlari                          ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Qaysi diagramma toʻgʻri gapiradi",
        "summary": (
            "PM-76 matni. Ilmiy-ommabop: bitta doʻkonning maʼlumoti uch xil "
            "diagrammada — va nega har biri boshqa savolga javob berishi."
        ),
        "order":   76,
        "grammar": [
            {
                "pattern":  "sektor burchagi = ulush ÷ jami × 360°",
                "meaning":  "Doiraviy diagrammada butun doira 360 gradus. "
                            "Har bir ulushga oʻz ulushicha burchak tegadi, "
                            "va ularning yigʻindisi doim roppa-rosa 360.",
                "examples": [
                    "45% → 45 × 3,6 = 162° (non)",
                    "25% → 90° (sut) — chorak doira",
                    "tekshiruv: 162 + 90 + 72 + 36 = 360",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nodira opa oylik savdo qanday oʻzgarganini "
                        "koʻrsatish uchun qaysi diagrammani tanladi?",
                "choices": [
                    "Doiraviy diagrammani",
                    "Ustunli diagrammani",
                    "Chiziqli diagrammani",
                    "Hech qaysisini",
                ],
                "answer": 2,
                "explanation": "Savol vaqt boʻyicha oʻzgarish haqida edi — "
                               "oylar ketma-ket keladi va chiziqning "
                               "koʻtarilishi ana shu oʻzgarishni koʻrsatadi. "
                               "Doiraviy diagramma bu yerda ishlamaydi: "
                               "oylar butunning boʻlaklari emas.",
            },
            {
                "text": "Non sotuvining sektor burchagi necha gradus?",
                "choices": ["162°", "45°", "90°", "180°"],
                "answer": 0,
                "explanation": "Non butun savdoning 45 foizini tashkil "
                               "qiladi: 45 × 3,6 = 162°. «45°» — foizning "
                               "oʻzi gradus deb yozilgan boʻlardi; foizdan "
                               "burchakka oʻtish uchun 3,6 ga koʻpaytiriladi.",
            },
            {
                "text": "Nega haroratni doiraviy diagrammada koʻrsatib "
                        "boʻlmaydi?",
                "choices": [
                    "Chunki harorat manfiy boʻlishi mumkin",
                    "Chunki harorat butunning boʻlagi emas — kunlik "
                    "haroratlarni qoʻshishning maʼnosi yoʻq",
                    "Chunki yetti sektor juda koʻp",
                    "Chunki gradus soʻzi ikki xil maʼnoda ishlatiladi",
                ],
                "answer": 1,
                "explanation": "Doiraviy diagramma bir butunni boʻlaklarga "
                               "ajratadi. Haroratlar esa yigʻiladigan butun "
                               "hosil qilmaydi: 18° va 21° ni qoʻshib 39° "
                               "olishning hech qanday maʼnosi yoʻq.",
            },
        ],
        "body": """
<p>Bitta jadvalni uch xil chizish mumkin. Lekin uchalasi bir xil narsani
aytmaydi — har biri boshqa savolga javob beradi.</p>

<p>Nodira opaning kichik doʻkoni bor. U yil oxirida ikkita savolga javob
qidirdi.</p>

<p><b>Birinchi savol: savdo yil davomida qanday oʻzgardi?</b></p>

<p>Bu yerda maʼlumot vaqt boʻyicha yigʻilgan: yanvar, fevral, mart…
Oylar ketma-ket keladi, va ular orasida
<span class="cn-word" data-tr="ikki qiymat orasidagi masofa">oraliq</span>
bor. Shuning uchun Nodira opa
<span class="cn-word" data-tr="vaqt boʻyicha oʻzgarishni koʻrsatuvchi diagramma">chiziqli diagramma</span>
chizdi. Chiziq yozdan keyin koʻtarilib, qishda yana tushdi — bu
oʻzgarishni jadvaldan koʻrish uchun oʻn ikkita sonni oʻqish kerak
boʻlardi.</p>

<p><b>Ikkinchi savol: savdoning qanchasi qaysi mahsulotdan?</b></p>

<p>Bu butunlay boshqa savol. Endi vaqt yoʻq — bir butun bor, va u
<span class="cn-word" data-tr="butundan tegishli qism">ulush</span>larga
boʻlinadi: non <strong>45</strong>%, sut <strong>25</strong>%,
shirinlik <strong>20</strong>%, qolgani <strong>10</strong>%. Bunday
maʼlumot uchun
<span class="cn-word" data-tr="butunning boʻlaklarini koʻrsatuvchi diagramma">doiraviy diagramma</span>
ishlatiladi.</p>

<p>Har bir
<span class="cn-word" data-tr="doiraviy diagrammaning bir boʻlagi">sektor</span>ning
<span class="cn-word" data-tr="ikki nur orasidagi ochilish oʻlchovi">burchak</span>i
hisoblab chiqiladi. Butun doira <strong>360</strong>
<span class="cn-word" data-tr="burchak oʻlchov birligi">gradus</span>,
demak har bir foizga 3,6 gradusdan tegadi. Non uchun:
45 × 3,6 = <strong>162</strong>°. Sut uchun 90°, shirinlik uchun 72°,
qolgani uchun 36°.</p>

<p>Va majburiy
<span class="cn-word" data-tr="hisobning toʻgʻriligini qayta koʻrish">tekshiruv</span>:
162 + 90 + 72 + 36 = <strong>360</strong>°. Doira toʻliq yopildi. Agar
yigʻindi 360 dan farq qilsa, diagramma notoʻgʻri.</p>

<p>Uchinchi tur ham bor —
<span class="cn-word" data-tr="toifalarni solishtiruvchi diagramma">ustunli diagramma</span>.
U «qaysi biri koʻp?» degan savol uchun. Uning bitta qatʼiy qoidasi bor:
sonlar
<span class="cn-word" data-tr="diagrammaning sonlar yozilgan chizigʻi">oʻq</span>i
noldan boshlanishi shart. Aks holda kichik farq katta boʻlib
koʻrinadi.</p>

<p>Demak diagramma turini maʼlumot emas, <b>savol</b> tanlaydi.
«Qanday oʻzgardi?» — chiziqli. «Butundan qanchasi?» — doiraviy.
«Qaysi biri koʻp?» — ustunli. Notoʻgʻri turini tanlagan diagramma
yolgʻon gapirmaydi, lekin kerakli narsani ham koʻrsatmaydi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-77 — diagrammani oʻqish                              YANGILIK
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bir yillik yomgʻir",
        "summary": (
            "PM-77 matni. Yangilik: maktabning ob-havo toʻgaragi oʻz yomgʻir "
            "oʻlchagichi qaydlarini diagrammaga soldi — va yozgi ustunlar "
            "koʻrinmay qolgani eng muhim xulosaga aylandi."
        ),
        "order":   77,
        "grammar": [
            {
                "pattern":  "farq = katta qiymat − kichik qiymat",
                "meaning":  "Diagrammadan oʻqishning asosiy amali. Eng "
                            "katta va eng kichik ustunni topib, ayirish "
                            "kifoya. «Nechtaga» — ayirish, «necha marta» — "
                            "boʻlish.",
                "examples": [
                    "75 − 40 = 35 mm (aprel va may farqi)",
                    "60 + 75 + 40 = 175 mm (bahor)",
                    "10 + 3 + 2 = 15 mm (yoz)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Toʻgarak aʼzolari qanday xulosaga kelishdi?",
                "choices": [
                    "Yozda yomgʻir umuman yogʻmagan",
                    "Yomgʻir har oyda bir xil miqdorda yoqqan",
                    "Iyul eng yomgʻirli oy boʻlgan",
                    "Yomgʻirning deyarli hammasi bahorga toʻgʻri kelgan",
                ],
                "answer": 3,
                "explanation": "Bahordagi uch oyda 175 mm, yozdagi uch oyda "
                               "atigi 15 mm yomgʻir tushgan. «Umuman "
                               "yogʻmagan» degani notoʻgʻri boʻlardi — "
                               "avgustda ham 2 mm qayd etilgan; past ustun "
                               "boʻsh degani emas.",
            },
            {
                "text": "Aprel va may orasidagi farq necha millimetr?",
                "choices": ["15 mm", "35 mm", "40 mm", "115 mm"],
                "answer": 1,
                "explanation": "75 − 40 = 35 mm. «115 mm» — ayirish oʻrniga "
                               "qoʻshilgan boʻlardi. Farq har doim katta "
                               "qiymatdan kichigini ayirish bilan topiladi.",
            },
            {
                "text": "Uch bahor oyida jami qancha yomgʻir tushgan?",
                "choices": ["135 mm", "150 mm", "175 mm", "190 mm"],
                "answer": 2,
                "explanation": "60 + 75 + 40 = 175 mm. «190 mm» — bu olti "
                               "oyning hammasi, yozgi 15 mm ham qoʻshilgan "
                               "holat.",
            },
        ],
        "body": """
<p><b>Maktab yangiliklari.</b> 22-maktabning ob-havo toʻgaragi olti oy
davomida har kuni hovlidagi
<span class="cn-word" data-tr="tushgan yomgʻir miqdorini oʻlchaydigan asbob">yomgʻir oʻlchagich</span>ni
tekshirib bordi. Kecha ular birinchi hisobotini eʼlon qilishdi.</p>

<p>Har kungi
<span class="cn-word" data-tr="oʻlchov natijasi yozib qoʻyilgani">qayd</span>lar
<span class="cn-word" data-tr="maʼlumotning chizmadagi koʻrinishi">diagramma</span>ga
solindi. Pastdagi
<span class="cn-word" data-tr="sonlar va nomlar yozilgan chiziq">oʻq</span>da
oylar, chapdagi oʻqda yomgʻir miqdori — <strong>millimetr</strong>da.
Bu <span class="cn-word" data-tr="nima bilan oʻlchangani">birlik</span>ni
bilmasdan diagrammani oʻqib boʻlmaydi.</p>

<p>Natijalar: mart <strong>60</strong> mm, aprel <strong>75</strong> mm,
may <strong>40</strong> mm, iyun <strong>10</strong> mm, iyul
<strong>3</strong> mm, avgust <strong>2</strong> mm.</p>

<p>Eng baland ustun — aprel. Eng past — avgust. Ularning
<span class="cn-word" data-tr="ikki qiymatning ayirmasi">farq</span>i
73 millimetr.</p>

<p>Toʻgarak rahbari oʻquvchilardan qoʻshni oylarni solishtirishni
soʻradi. Aprel va may orasidagi farq: 75 − 40 = <strong>35</strong> mm.
Bu — eng katta
<span class="cn-word" data-tr="qoʻshni ikki qiymat orasidagi keskin oʻzgarish">sakrash</span>,
va diagrammada aynan oʻsha joyda ustunlar keskin pasayadi.</p>

<p>Keyin ular fasllar boʻyicha
<span class="cn-word" data-tr="bir nechta sonning qoʻshilishi">yigʻindi</span>ni
hisoblab chiqishdi. Bahor: 60 + 75 + 40 =
<strong>175</strong> mm. Yoz: 10 + 3 + 2 = <strong>15</strong> mm.
Olti oyda <strong>190</strong> mm.</p>

<p>«Diagrammaga qarang, — dedi rahbar. — Yozgi uchta ustun deyarli
koʻrinmayapti. Bu bizning eng muhim
<span class="cn-word" data-tr="maʼlumotdan chiqarilgan fikr">xulosa</span>miz.»</p>

<p>Bir oʻquvchi «yozda yomgʻir umuman yogʻmagan» dedi. Rahbar uni
tuzatdi: avgustda ham 2 millimetr qayd etilgan. Past
<span class="cn-word" data-tr="diagrammadagi tik toʻgʻri toʻrtburchak">ustun</span>
— bu «kam» degani, «yoʻq» degani emas.</p>

<p>Va yana bir ogohlantirish. Diagramma yomgʻir <b>qancha</b> tushganini
koʻrsatadi, lekin <b>nega</b> shunday boʻlganini aytmaydi. Buning uchun
iqlim haqidagi boshqa maʼlumot kerak boʻladi.</p>

<p>Toʻgarak kuzatishni davom ettiradi. Kelasi yil ikkita yilning
diagrammasini yonma-yon qoʻyish rejalashtirilgan.</p>
""",
    },
]
