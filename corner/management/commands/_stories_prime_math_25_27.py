# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-25 … PM-27.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 25 — yangilik xabari, 26 — sharh (reklama tahlili),
27 — hikoya (uch doʻst va savat).

⚠️ Kumulyativ: nisbat matnida proporsiya ham, tenglama ham yoʻq — faqat
   «bir qism» usuli (PM-27). Foiz matnlarida asos har doim ESKI qiymat.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_25_27.py --author=prime
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
    # PM-25 — foiz oʻzgarishi                              YANGILIK
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Narx oshdi, keyin tushdi",
        "summary": (
            "PM-25 matni. Yangilik xabari: yozda qimmatlashgan yogʻ kuzda oʻshancha "
            "foizga arzonladi — lekin eski narxga qaytmadi. Nega bunday boʻlishi "
            "hisob bilan koʻrsatilgan."
        ),
        "order":   25,
        "grammar": [
            {
                "pattern":  "Ketma-ket oʻzgarishda koʻpaytuvchilar koʻpaytiriladi",
                "meaning":  "Oshish ×(1 + p/100), kamayish ×(1 − p/100). Ikkinchi "
                            "foiz allaqachon oʻzgargan sondan olinadi, shuning uchun "
                            "bir xil foizga oshib, keyin tushgan narx eskisiga "
                            "qaytmaydi.",
                "examples": [
                    "20 000 × 1,25 = 25 000 (yozda 25% oshdi)",
                    "25 000 × 0,75 = 18 750 (kuzda 25% tushdi) — 1,25 × 0,75 = 0,9375",
                ],
            },
        ],
        "questions": [
            {
                "text": "Xabarga koʻra, xaridorlar nimadan norozi boʻlishgan?",
                "choices": [
                    "Yogʻ doʻkonlardan butunlay yoʻqolib qolganidan",
                    "Chegirmadan keyin ham narx eski darajaga qaytmaganidan",
                    "Yangi narx eʼlon qilinmaganidan",
                    "Doʻkon kechqurun yopilib qolganidan",
                ],
                "answer": 1,
                "explanation": "Xaridorlar «25 foiz oshgan edi, 25 foiz tushdi» deb "
                               "hisoblashgan va eski narxni kutishgan. Lekin narx "
                               "18 750 soʻmda qoldi.",
            },
            {
                "text": "Yozda 20 000 soʻmlik yogʻ 25 foizga qimmatlashdi. Yangi narx "
                        "qancha boʻldi?",
                "choices": ["21 250 soʻm", "22 500 soʻm", "25 000 soʻm", "26 000 soʻm"],
                "answer": 2,
                "explanation": "20 000 × 1,25 = 25 000 soʻm. Qoʻshimcha 5000 soʻm "
                               "boʻldi.",
            },
            {
                "text": "Kuzda oʻsha narx 25 foizga tushdi. Yogʻ endi qancha turadi?",
                "choices": ["15 000 soʻm", "18 750 soʻm", "20 000 soʻm", "21 250 soʻm"],
                "answer": 1,
                "explanation": "Chegirma yangi narxdan olinadi: 25 000 × 0,75 = "
                               "18 750 soʻm. Bu eski narxdan 1250 soʻm arzon, yaʼni "
                               "atigi 6,25 foizga.",
            },
        ],
        "body": """
<p><b>Iqtisod xabari.</b> Yozda qimmatlashgan paxta yogʻi kuzda yana arzonladi, lekin
xaridorlar baribir norozi.</p>

<p>Iyun oyida bir litrlik yogʻ <strong>20 000</strong> soʻm turardi. Iyul oxirida
doʻkonlar narxni <strong>25 foizga</strong> koʻtardi va yogʻ <strong>25 000</strong>
soʻm boʻldi.</p>

<p>Oktyabrda hosil yaxshi boʻldi. Doʻkonlar «narxni <strong>25 foizga</strong>
tushirdik» deb eʼlon qilishdi. Koʻpchilik yogʻ yana 20 000 soʻm boʻladi deb oʻyladi.</p>

<p>Lekin yorliqda <strong>18 750</strong> soʻm turardi — eski narxdan atigi 1250 soʻm
arzon.</p>

<p>Sababi <span class="cn-word" data-tr="foiz olinayotgan qiymat">asos</span>da.
Iyuldagi <span class="cn-word" data-tr="qiymatning koʻpayishi">oshish</span> 20 000
dan hisoblangan, oktyabrdagi
<span class="cn-word" data-tr="qiymatning pasayishi">kamayish</span> esa 25 000 dan.
Katta sondan olingan 25 foiz — 6250 soʻm, kichigidan olingani esa atigi 5000 soʻm
edi.</p>

<p>Buni <span class="cn-word" data-tr="oʻzgarishni bir amalda beruvchi son">koʻpaytuvchi</span>lar
bilan tekshirish oson: <strong>1,25 × 0,75 = 0,9375</strong>. Demak yangi narx
eskining 93,75 foizi — <span class="cn-word" data-tr="biridan keyin ikkinchisi qoʻllanadigan oʻzgarish">ketma-ket oʻzgarish</span>dan
keyin narx atigi 6,25 foizga tushgan.</p>

<p>Mutaxassislar eslatadi: bir xil foizga oshib, keyin tushgan narx hech qachon eski
darajaga qaytmaydi. Buni bilgan xaridor eʼlonga emas,
<span class="cn-word" data-tr="mahsulotning hozirgi haqiqiy narxi">yorliqdagi narx</span>ga
qaraydi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-26 — chegirma va ustama                               SHARH
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "«Katta chegirma!» — reklama ortidagi hisob",
        "summary": (
            "PM-26 matni. Sharh: doʻkon avval narxni koʻtarib, keyin «30 foiz "
            "chegirma» eʼlon qildi. Hisob shuni koʻrsatadiki, xaridor aslida bor-yoʻgʻi "
            "9 foiz yutgan."
        ),
        "order":   26,
        "grammar": [
            {
                "pattern":  "Chegirma qaysi narxdan olinayotganini tekshiring",
                "meaning":  "Chegirma har doim eʼlon qilingan sotuv narxidan "
                            "hisoblanadi. Agar oʻsha narx oldin koʻtarilgan boʻlsa, "
                            "chegirmaning haqiqiy foydasi ancha kichik chiqadi.",
                "examples": [
                    "100 000 × 1,3 = 130 000 (sentyabrda ustama)",
                    "130 000 × 0,7 = 91 000 → eski narxdan atigi 9000 soʻm arzon (9%)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Muallif doʻkonning reklamasini nima uchun tanqid qilyapti?",
                "choices": [
                    "Chegirma umuman qilinmagani uchun",
                    "Chegirma koʻtarilgan narxdan hisoblangani uchun",
                    "Mahsulot sifati past boʻlgani uchun",
                    "Eʼlon juda mayda harflarda yozilgani uchun",
                ],
                "answer": 1,
                "explanation": "Doʻkon avgustda 100 000 soʻmlik krossovkani sentyabrda "
                               "130 000 soʻm qilgan va «30 foiz chegirma»ni oʻsha "
                               "yangi narxdan hisoblagan.",
            },
            {
                "text": "Krossovka noyabrda necha soʻm turdi?",
                "choices": ["70 000 soʻm", "91 000 soʻm", "100 000 soʻm", "109 000 soʻm"],
                "answer": 1,
                "explanation": "130 000 × 0,7 = 91 000 soʻm. Chegirmaning oʻzi 39 000 "
                               "soʻm boʻlgan, lekin u koʻtarilgan narxdan olingan.",
            },
            {
                "text": "Avgustdagi narx bilan solishtirganda xaridor necha foiz "
                        "yutgan?",
                "choices": ["30 foiz", "21 foiz", "9 foiz", "hech narsa yutmagan"],
                "answer": 2,
                "explanation": "100 000 − 91 000 = 9000 soʻm; 9000 ÷ 100 000 = 0,09, "
                               "yaʼni 9 foiz. Reklamadagi 30 foizdan uch baravardan "
                               "koʻproq kam.",
            },
        ],
        "body": """
<p><b>Sharh: «Mavsum oxiri — 30% chegirma!»</b></p>

<p>Bu eʼlonni shahardagi deyarli har bir doʻkon oynasida koʻrasiz. Biz bitta
doʻkondagi bitta krossovkani uch oy kuzatdik.</p>

<p><b>Avgust.</b> Yorliqda <strong>100 000</strong> soʻm. Xaridor koʻp emas, mahsulot
tokchada turibdi.</p>

<p><b>Sentyabr.</b> Doʻkon narxni <strong>30 foizga</strong> koʻtardi. Yangi
<span class="cn-word" data-tr="xaridorga eʼlon qilingan narx">sotuv narxi</span> —
<strong>130 000</strong> soʻm. Yorliq almashtirildi, boshqa hech narsa oʻzgarmadi.</p>

<p><b>Noyabr.</b> Oynada katta eʼlon paydo boʻldi: «30% chegirma».
<span class="cn-word" data-tr="narxdan tushiriladigan ulush">Chegirma</span> oʻsha
130 000 dan hisoblanadi: <strong>130 000 × 0,7 = 91 000</strong> soʻm.</p>

<p>Endi solishtiring. Avgustda 100 000 edi, hozir 91 000. Xaridorning
<span class="cn-word" data-tr="tejalgan pul">yutugʻi</span> — 9000 soʻm, yaʼni
<strong>9 foiz</strong>. Eʼlonda esa 30 foiz deyilgan.</p>

<p>Doʻkon yolgʻon yozmadi: chegirma haqiqatan ham 30 foiz. Faqat u
<span class="cn-word" data-tr="foiz olinayotgan qiymat">asos</span>ni oʻzgartirib
qoʻydi. <span class="cn-word" data-tr="tannarx ustiga qoʻshiladigan foyda">Ustama</span>
va chegirma bir-birini yoʻqqa chiqardi:
<strong>1,3 × 0,7 = 0,91</strong>.</p>

<p><b>Maslahat:</b> chegirmani emas,
<span class="cn-word" data-tr="hamma oʻzgarishdan keyingi toʻlov">yakuniy narx</span>ni
solishtiring. Foiz — bu vaʼda, narx esa fakt.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-27 — nisbat                                          HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Uch doʻst va bir savat olma",
        "summary": (
            "PM-27 matni. Uch doʻst savatni birga sotib oladi, lekin har xil pul "
            "qoʻshadi. Olmani teng boʻlish adolatli emasligi maʼlum boʻlgach, ular "
            "nisbatni eslashadi."
        ),
        "order":   27,
        "grammar": [
            {
                "pattern":  "Miqdorni nisbatda boʻlish — «bir qism» usuli",
                "meaning":  "Avval nisbatdagi sonlarni qoʻshib qismlar sonini "
                            "topamiz, keyin miqdorni shunga boʻlib bitta qismni "
                            "aniqlaymiz, oxirida har birini oʻz soniga koʻpaytiramiz.",
                "examples": [
                    "12 : 18 : 30 = 2 : 3 : 5 (hammasini 6 ga qisqartirdik)",
                    "2 + 3 + 5 = 10; 120 ÷ 10 = 12; 24, 36 va 60 ta olma",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nima uchun olmani teng boʻlish adolatli boʻlmadi?",
                "choices": [
                    "Bolalar har xil miqdorda pul qoʻshgan edi",
                    "Savatdagi olmalar har xil kattalikda edi",
                    "Sherbek olmani yoqtirmasdi",
                    "Savat bozordan uzoq joyda qolgan edi",
                ],
                "answer": 0,
                "explanation": "Afsona 12 000, Jasur 18 000, Sherbek 30 000 soʻm "
                               "qoʻshgan edi. Teng boʻlinsa, koʻp toʻlagan kishi "
                               "yutqazardi.",
            },
            {
                "text": "12 000 : 18 000 : 30 000 nisbati sodda koʻrinishda qanday "
                        "boʻladi?",
                "choices": ["1 : 2 : 3", "2 : 3 : 5", "3 : 4 : 5", "4 : 6 : 10"],
                "answer": 1,
                "explanation": "Uchala sonni ham 6000 ga boʻlamiz: 2 : 3 : 5. "
                               "4 : 6 : 10 ham teng nisbat, lekin toʻliq "
                               "qisqartirilmagan.",
            },
            {
                "text": "120 ta olma 2:3:5 nisbatda boʻlinsa, Sherbekka nechta tegadi?",
                "choices": ["24 ta", "36 ta", "40 ta", "60 ta"],
                "answer": 3,
                "explanation": "Qismlar 2 + 3 + 5 = 10; bir qism 120 ÷ 10 = 12 ta. "
                               "Sherbek 5 qism: 12 × 5 = 60 ta. 40 — teng boʻlinganda "
                               "chiqadigan son.",
            },
        ],
        "body": """
<p>Bozorda katta savat olma turardi. Uni bittalab olish qimmat edi, shuning uchun
Afsona, Jasur va Sherbek birga sotib olishga kelishdi.</p>

<p>Savat <strong>60 000</strong> soʻm turdi. Har kim boricha pul qoʻshdi: Afsona
<strong>12 000</strong>, Jasur <strong>18 000</strong>, Sherbek esa
<strong>30 000</strong> soʻm.</p>

<p>Savatda <strong>120</strong> ta olma bor edi. Uyga qaytishayotib Jasur taklif
qildi:</p>

<p>— Uchga boʻlamiz, har birimizga 40 tadan.</p>

<p>Sherbek toʻxtadi. U ikki barobar koʻp pul toʻlagan, lekin bir xil olma olishi
kerakmi?</p>

<p>Afsona daftar chiqardi. Pullarning
<span class="cn-word" data-tr="ikki yoki undan koʻp miqdor orasidagi munosabat">nisbat</span>i
12 000 : 18 000 : 30 000 ekan. Uchalasini 6000 ga
<span class="cn-word" data-tr="nisbatdagi sonlarni bir xil songa boʻlish">qisqartir</span>gach,
<span class="cn-word" data-tr="toʻliq qisqartirilgan nisbat">sodda koʻrinish</span> chiqdi: <strong>2 : 3 : 5</strong>.</p>

<p>— Demak <span class="cn-word" data-tr="nisbatdagi sonlar yigʻindisi">qismlar soni</span> oʻnta, har biri teng
<span class="cn-word" data-tr="nisbatdagi bitta teng boʻlak">qism</span>, —
dedi Afsona. — <strong>120 ÷ 10 = 12</strong>, yaʼni bitta qism oʻn ikkita olma.</p>

<p>Shundan keyin hisob oson boʻldi: Afsonaga <strong>24</strong> ta, Jasurga
<strong>36</strong> ta, Sherbekka <strong>60</strong> ta.</p>

<p>Ular olmalarni sanab chiqishdi — roppa-rosa 120 ta: <span class="cn-word" data-tr="qismlar yigʻindisi butunga teng ekanini sinash">nazorat</span> mos keldi.
<span class="cn-word" data-tr="hissaga qarab taqsimlash">Adolatli boʻlish</span>
degani teng boʻlish emas ekan: har kim qancha qoʻshgan boʻlsa, shuncha oladi.</p>
""",
    },
]
