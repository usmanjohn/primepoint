# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-13 … PM-15.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 13 — hikoya (usta va supa), 14 — bozordagi dialog,
15 — kundalik (toc da «hikoya» deb belgilangan edi; ketma-ket uchta hikoya
boʻlmasligi uchun kundalikka aylantirildi).

⚠️ Oʻnlik kasr PM-20 da oʻrgatiladi — bu matnlarda vergulli son yoʻq.
   PM-15 matnida kasr qisqartirilmaydi (u PM-16 da).

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_13_15.py --author=prime
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
    # PM-13 — kvadrat ildiz                              HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Kvadrat maydonning tomoni",
        "summary": (
            "PM-13 matni. Ustaga loyihada faqat yuza berilgan, unga esa tomon kerak. "
            "Kvadrat ildiz — quruvchining kundalik asbobi."
        ),
        "order":   13,
        "grammar": [
            {
                "pattern":  "Yuzadan tomonga — kvadrat ildiz",
                "meaning":  "Kvadratning yuzasi tomonning oʻziga koʻpaytmasiga teng. "
                            "Shuning uchun yuza berilgan boʻlsa, tomon uning kvadrat "
                            "ildiziga teng boʻladi. Perimetr esa tomonning toʻrt "
                            "barobari.",
                "examples": [
                    "√81 = 9 m (tomon)",
                    "4 × 9 = 36 m (perimetr — atrofdagi panjara uzunligi)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Ustaga loyihadagi qaysi son yetarli boʻlmadi?",
                "choices": [
                    "Supaning balandligi",
                    "Gʻishtning narxi",
                    "Supaning yuzasi — unga tomon kerak edi",
                    "Ishchilar soni",
                ],
                "answer": 2,
                "explanation": "Loyihada yuza yozilgan edi, usta esa ip tortish uchun "
                               "tomonning uzunligini bilishi kerak edi.",
            },
            {
                "text": "Yuzasi 81 m² boʻlgan kvadrat supaning tomoni necha metr?",
                "choices": ["8 m", "9 m", "18 m", "40 m"],
                "answer": 1,
                "explanation": "√81 = 9, chunki 9 × 9 = 81. 40 javobi 81 ni ikkiga "
                               "boʻlishdan chiqadi — bu ildiz emas.",
            },
            {
                "text": "Supaning atrofiga panjara tortilsa, necha metr panjara kerak?",
                "choices": ["18 m", "27 m", "36 m", "81 m"],
                "answer": 2,
                "explanation": "Kvadratning toʻrt tomoni teng: 4 × 9 = 36 m.",
            },
        ],
        "body": """
<p>Karim aka hovliga <span class="cn-word" data-tr="toʻrt tomoni ham teng toʻrtburchak">kvadrat</span> shaklida supa qurmoqchi. Qogʻozda faqat bitta son bor edi:
<b>81 m²</b>.</p>

<p>— Yuzasi maʼlum, — dedi u nabirasi Bekzodga, — lekin menga bu son bilan ish qilib
boʻlmaydi. Men ip tortaman. Menga <b>tomon</b> kerak.</p>

<p>Bekzod daftarini ochdi. Maktabda <span class="cn-word" data-tr="bir sonni oʻziga qayta-qayta koʻpaytirish yozuvi">daraja</span>ni
yaqinda oʻtishgan edi: tomon 9 boʻlsa, <span class="cn-word" data-tr="shakl ichidagi joy oʻlchovi">yuza</span>
9 × 9 = 81 chiqadi. Endi savol teskari turardi. Bunday <span class="cn-word" data-tr="bajarilgan amalni bekor qiladigan amal">teskari amal</span>
<span class="cn-word" data-tr="oʻziga koʻpaytirilganda berilgan sonni beradigan manfiy boʻlmagan son">kvadrat ildiz</span>
deb ataladi: <strong>√81 = 9</strong>.</p>

<p>— Toʻqqiz metr, — dedi Bekzod. — Tekshirsa ham boʻladi: 9 × 9 = 81.</p>

<p>Karim aka ipni tortdi va toʻrtta qoziqni qoqdi. Har bir
<span class="cn-word" data-tr="koʻpburchakning bir cheti">tomon</span> toʻqqiz metrdan
chiqdi.</p>

<p>— Endi ikkinchi savol, — dedi u. — Atrofiga panjara olamiz. Necha metr kerak?</p>

<p>Bu <span class="cn-word" data-tr="shakl chegarasining umumiy uzunligi">perimetr</span>
edi: 4 × 9 = <strong>36 metr</strong>.</p>

<p>Kechqurun qoʻshni Nodira opa ham keldi. Uning yeri kattaroq — <b>100 m²</b>. Bekzod
hisoblab berdi: √100 = 10, demak tomoni 10 metr, panjara esa 40 metr.</p>

<p>— Yuza 19 metr kvadratga koʻpaydi, panjara esa atigi 4 metrga, — hayron boʻldi
Nodira opa.</p>

<p>— Shunday boʻladi, — dedi Bekzod. — Ildiz sonni juda sekin oʻstiradi. Masalan,
yuza <b>toʻrt barobar</b> katta boʻlsa, tomon faqat <b>ikki barobar</b> uzayadi:
√100 = 10, lekin √400 = 20, yuza esa 100 dan 400 ga chiqib ketgan.</p>

<p>Karim aka kulib qoʻydi: «Men buni oʻttiz yildan beri bilaman, faqat nomini
bilmasdim».</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-14 — yaxlitlash                                 BOZORDAGI DIALOG
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Buvijonning bozordagi taxmini",
        "summary": (
            "PM-14 matni. Buvijonda kalkulyator ham, daftar ham yoʻq — lekin pul "
            "yetishini sotuvchidan oldin biladi. Yaxlitlash shunday ishlaydi."
        ),
        "order":   14,
        "grammar": [
            {
                "pattern":  "Yaxlitlab qoʻshish — taxminiy javob (≈)",
                "meaning":  "Har bir sonni yaqin yumaloq songa almashtirib qoʻshsak, "
                            "javob bir soniyada chiqadi. U aniq emas, shuning uchun "
                            "≈ belgisi qoʻyiladi — lekin pul yetadimi degan savolga "
                            "javob berish uchun yetarli.",
                "examples": [
                    "3 800 + 2 100 + 1 450 ≈ 4 000 + 2 000 + 1 000 = 7 000",
                    "Aniq javob: 3 800 + 2 100 + 1 450 = 7 350",
                ],
            },
        ],
        "questions": [
            {
                "text": "Buvijon nima uchun sonlarni yaxlitladi?",
                "choices": [
                    "Sotuvchiga ishonmagani uchun",
                    "Narxlarni pasaytirish uchun",
                    "Aniq javobni yozib olish uchun",
                    "Hamyonidagi pul yetishini tez bilish uchun",
                ],
                "answer": 3,
                "explanation": "Unga aniq son kerak emas edi — unga faqat «yetadimi?» "
                               "degan savolga javob kerak edi.",
            },
            {
                "text": "Buvijonning ogʻzaki taxmini qancha chiqdi?",
                "choices": ["6 000 soʻm", "7 000 soʻm", "7 350 soʻm", "8 000 soʻm"],
                "answer": 1,
                "explanation": "4 000 + 2 000 + 1 000 = 7 000. Bu taxminiy javob, "
                               "shuning uchun ≈ belgisi bilan yoziladi.",
            },
            {
                "text": "Xariddan keyin hamyonda qancha pul qoldi?",
                "choices": ["650 soʻm", "1 000 soʻm", "1 350 soʻm", "7 350 soʻm"],
                "answer": 0,
                "explanation": "Aniq summa 3 800 + 2 100 + 1 450 = 7 350 soʻm. "
                               "8 000 − 7 350 = 650 soʻm qoldi.",
            },
        ],
        "body": """
<p>Shanba kuni bozor gavjum. Afsona buvijoni bilan yurar, xaltani u koʻtarardi.</p>

<p>Sotuvchi uch narsani tarozidan olib qoʻydi: guruch <b>3 800</b>, yogʻ <b>2 100</b>,
sabzi <b>1 450</b> soʻm.</p>

<p>— Hozir hisoblab beraman, opa, — dedi sotuvchi qalamni qidirib.</p>

<p>— Shoshmang, — kulib qoʻydi buvijon. — Yetti mingdan sal oshadi. Hamyonimda sakkiz
ming bor, yetadi.</p>

<p>Afsona hayron qoldi. Buvijon hech narsa yozmadi, kalkulyator ham ishlatmadi — hammasini <span class="cn-word" data-tr="qogʻozsiz, xayolan bajariladigan hisob">ogʻzaki hisob</span> bilan qildi.</p>

<p>— Buvijon, qanday hisobladingiz?</p>

<p>— Aniq hisoblaganim yoʻq, qizim. Men <span class="cn-word" data-tr="sonni yaqin yumaloq songa almashtirish">yaxlitladim</span>.
Uch ming sakkiz yuz — deyarli toʻrt ming. Ikki ming yuz — ikki ming. Ming toʻrt yuz
ellik — bir ming. Toʻrt qoʻshuv ikki qoʻshuv bir — yetti ming. Bu
<span class="cn-word" data-tr="aniq emas, lekin yetarlicha yaqin javob">taqribiy qiymat</span>,
lekin menga shuning oʻzi kerak edi.</p>

<p>Sotuvchi hisobni tugatdi: <strong>7 350 soʻm</strong>. Buvijonning
<span class="cn-word" data-tr="hisoblashdan oldin javobning kattaligini aytish">taxmin</span>i
atigi 350 soʻmga farq qilgan edi — bu farq <span class="cn-word" data-tr="taxmin bilan aniq javob orasidagi farq">xatolik</span> deyiladi.</p>

<p>— Koʻrdingmi, — dedi buvijon sakkiz ming soʻmni uzatarkan. — Menga sonning oxirgi
raqami emas, <span class="cn-word" data-tr="raqamning sondagi oʻrni: birlik, oʻnlik, yuzlik">razryad</span>i
kerak edi. Yetti mingmi yoki yetmish mingmi — mana shu muhim.</p>

<p>Sotuvchi <b>650 soʻm</b> qaytim berdi. Yoʻlda Afsona bir savol berdi:</p>

<p>— Taxminingiz aniq javobdan kichik chiqdi. Xato boʻlmaydimi?</p>

<p>— Xato emas, — dedi buvijon. — Men ikkitasini pastga tushirdim. Shuning uchun
<span class="cn-word" data-tr="toʻliq hisoblangan natija">aniq javob</span> taxmindan
sal katta chiqishini oldindan bilardim. Faqat pulim shu farqni koʻtarardi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-15 — kasr                                       KUNDALIK
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bitta non, olti kishi",
        "summary": (
            "PM-15 matni. Afsonaning kundaligi: mehmonlar keldi, non bitta edi. "
            "Kechqurun u kasrlarning eng gʻalati qoidasini oʻzi topdi."
        ),
        "order":   15,
        "grammar": [
            {
                "pattern":  "Maxraj katta — boʻlak kichik",
                "meaning":  "Maxraj butun nechta teng boʻlakka boʻlinganini aytadi. "
                            "Boʻlaklar soni oshsa, har biri kichrayadi. Shuning uchun "
                            "surat bir xil boʻlganda maxraji katta kasr kichikroq "
                            "boʻladi.",
                "examples": [
                    "Bitta non 6 kishiga: har kimga 1/6",
                    "1/8 boʻlagi 1/6 boʻlagidan kichik — sakkizga koʻproq kishi boʻlingan",
                ],
            },
        ],
        "questions": [
            {
                "text": "Afsona kechqurun nimani tushundi?",
                "choices": [
                    "Nonni bir xil boʻlaklarga boʻlish qiyin ekanini",
                    "Sakkizga boʻlingan boʻlak oltiga boʻlingandan kichik ekanini",
                    "Mehmonlar koʻp kelsa non yetmasligini",
                    "Pirogni nonga qoʻshib boʻlmasligini",
                ],
                "answer": 1,
                "explanation": "Maxraj katta boʻlsa, boʻlak kichik boʻladi — buni u "
                               "ikki boʻlakni yonma-yon qoʻyib koʻrdi.",
            },
            {
                "text": "Afsona nonning ikkita boʻlagini oldi. U nonning qanchasini "
                        "olgan boʻladi?",
                "choices": ["1/6", "2/6", "2/8", "6/2"],
                "answer": 1,
                "explanation": "Non oltita teng boʻlakka boʻlingan (maxraj 6), Afsona "
                               "ikkitasini olgan (surat 2).",
            },
            {
                "text": "Pirog sakkizta teng boʻlakka boʻlindi va uchtasi yeyildi. "
                        "Pirogning qanchasi qoldi?",
                "choices": ["3/8", "5/8", "5/3", "8/5"],
                "answer": 1,
                "explanation": "Boʻlaklar soni oʻzgarmaydi — maxraj baribir 8. Qolgan "
                               "boʻlaklar: 8 − 3 = 5 ta, demak 5/8.",
            },
        ],
        "body": """
<p><b>Shanba, kechqurun.</b></p>

<p>Bugun kutilmaganda mehmon keldi. Dasturxonda olti kishi oʻtirdik, non esa bitta edi.
Oyim pichoqni oldi va nonni oltita <span class="cn-word" data-tr="bir xil kattalikdagi qismlar">teng boʻlak</span>ka
boʻldi. <span class="cn-word" data-tr="boʻlinmagan bir dona">Butun</span> non oltiga boʻlindi va har kimga bittadan tegdi — yaʼni nonning <strong>1/6</strong> qismi.</p>

<p>Men shu yerda bir narsani tushundim. Pastdagi olti — <span class="cn-word" data-tr="kasrning pastki soni: nechta teng boʻlakka boʻlingani">maxraj</span>
— non nechta boʻlakka boʻlinganini aytadi. Yuqoridagi bir esa
<span class="cn-word" data-tr="kasrning yuqorigi soni: nechta boʻlak olingani">surat</span>
— menga nechtasi tekkanini. Ikkalasi birga <span class="cn-word" data-tr="butunning teng boʻlaklaridan biri yoki bir nechtasi">kasr</span>
deyilarkan.</p>

<p>Men ochqagan edim, shuning uchun ikkita boʻlak oldim — <strong>2/6</strong>. Oyim
hech narsa demadi, faqat kulib qoʻydi.</p>

<p>Keyin buvijon pirog olib chiqdi. Mehmonlar koʻpaygan edi, shuning uchun pirog
<b>sakkizta</b> boʻlakka boʻlindi. Har kimga <strong>1/8</strong>.</p>

<p>Va mana shu yerda gʻalati narsa boʻldi. Men nonning boʻlagini bir qoʻlimga, pirogning
boʻlagini ikkinchisiga oldim. <b>Pirogning boʻlagi kichikroq edi</b> — garchi 8 soni 6
dan katta boʻlsa ham!</p>

<p>Bir necha soniya oʻyladim va sabab oʻz-oʻzidan chiqdi. Sakkiz kishiga boʻlinsa,
har kimga kamroq tegadi. Kishilar koʻp — ulush kichik. Demak <strong>1/8 &lt; 1/6</strong>. Surati 1 boʻlgan bunday kasrlar <span class="cn-word" data-tr="surati 1 boʻlgan kasr: 1/3, 1/8">birlik kasr</span> deyilarkan, va ularni <span class="cn-word" data-tr="qaysi biri katta yoki kichikligini aniqlash">taqqoslash</span> uchun faqat maxrajga qarash yetarli ekan.
Butun sonlarda katta son koʻproqni bildiradi, kasrning pastki qavatida esa teskarisi
ishlaydi.</p>

<p>Pirogdan uchta boʻlak yeyildi, beshtasi qoldi — <strong>5/8</strong>. Boʻlaklar soni
oʻzgarmagani uchun maxraj baribir sakkiz boʻlib qolaverdi.</p>

<p>Kechqurun daftarimga yozib qoʻydim: <b>maxraj katta boʻlsa, boʻlak kichik</b>. Buni
darsda emas, dasturxonda oʻrgandim.</p>
""",
    },
]
