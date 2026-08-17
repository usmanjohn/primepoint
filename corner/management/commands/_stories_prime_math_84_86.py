# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-84, PM-85, PM-86.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 84 — ilmiy-ommabop, 85 — qoʻllanma, 86 — hikoya.
Oldingi uchlik sharh / hikoya / ilmiy-ommabop edi; 83 va 84 ketma-ket
ilmiy-ommabop, lekin uchtasi ketma-ket emas — toc shunday belgilagan.

⚠️ Kumulyativ:
   • 84-matnda ehtimollikni sanab hisoblash, teskari hodisa (1 − P) va
     oʻrtacha qaytim. ⛔ Shartli ehtimollik yoʻq;
   • 85-matn butunlay toʻrt qadam haqida — hech qanday yangi formula
     yoʻq, faqat oʻqish tartibi;
   • 86-matnda nomaʼlumni tanlash. ⛔ Harakat/ish/aralashma masalalari
     (PM-88…91) YOʻQ.
⚠️ Sonlar darsdagilardan boshqa (85-matndagi 32 oʻquvchi masalasi
   darsda faqat pe-fix ichida, boshqa savol bilan uchraydi).
⚠️ Savollar SAQLANGAN TARTIBDA koʻrsatiladi — `answer` indekslari:
   84 → 2/3/1, 85 → 0/2/1, 86 → 3/2/1.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_84_86.py --author=prime
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
    # PM-84 — ehtimollik hisobi                          ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Lotereya nega yutqazadi",
        "summary": (
            "PM-84 matni. Ilmiy-ommabop: bahor bayramidagi lotereyaning "
            "hamma sonlari ochiq eʼlon qilingan. Sherbek ularni qogʻozga "
            "koʻchirib, biletning haqiqiy qiymatini hisoblab chiqadi."
        ),
        "order":   84,
        "grammar": [
            {
                "pattern":  "P(yutmaslik) = 1 − P(yutish)",
                "meaning":  "Teskari hodisa qoidasi. Hodisa yo roʻy "
                            "beradi, yo bermaydi — ikkisining ehtimolligi "
                            "birgalikda butun 1 ni beradi.",
                "examples": [
                    "P(yutish) = 56 ÷ 2000 = 0,028 = 2,8%",
                    "P(yutmaslik) = 1 − 0,028 = 0,972 = 97,2%",
                ],
            },
            {
                "pattern":  "oʻrtacha qaytim = yutuq fondi ÷ biletlar soni",
                "meaning":  "Bitta biletga toʻgʻri keladigan yutuq puli. "
                            "U bilet narxidan kichik boʻlsa, oʻyin uzoq "
                            "muddatda albatta yutqazadi.",
                "examples": [
                    "4 000 000 ÷ 2 000 = 2 000 soʻm",
                    "bilet narxi 5 000 soʻm — qaytim uning 40 foizi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sherbek biletning haqiqiy qiymatini qanday topdi?",
                "choices": [
                    "Bosh yutuq narxini bilet narxiga boʻlib",
                    "Yutuqli biletlar sonini sanab",
                    "Yutuq fondini biletlar soniga boʻlib",
                    "Tashkilotchining foydasini ikkiga boʻlib",
                ],
                "answer": 2,
                "explanation": "Oʻrtacha qaytim — yutuq fondi ÷ biletlar "
                               "soni: 4 000 000 ÷ 2 000 = 2 000 soʻm. "
                               "Ya'ni 5 000 soʻmlik biletning haqiqiy "
                               "qiymati 2 000 soʻm ekan.",
            },
            {
                "text": "Bitta bilet olgan odam hech narsa yutmaslik "
                        "ehtimolligi qancha?",
                "choices": ["2,8%", "40%", "56%", "97,2%"],
                "answer": 3,
                "explanation": "Yutuqli biletlar 1 + 5 + 50 = 56 ta, "
                               "demak P(yutish) = 56 ÷ 2000 = 0,028 = "
                               "2,8%. Teskari hodisa qoidasi bilan "
                               "P(yutmaslik) = 1 − 0,028 = 0,972 = 97,2%. "
                               "«2,8%» — yutish ehtimolligi, «56%» esa "
                               "yutuqli biletlar sonini foiz deb "
                               "oʻqiganda chiqadi.",
            },
            {
                "text": "Tashkilotchining qoʻlida qancha pul qoldi?",
                "choices": [
                    "4 000 000 soʻm",
                    "6 000 000 soʻm",
                    "8 000 000 soʻm",
                    "10 000 000 soʻm",
                ],
                "answer": 1,
                "explanation": "Tushum: 2 000 × 5 000 = 10 000 000 soʻm. "
                               "Yutuq fondi 4 000 000 soʻm. Farqi: "
                               "10 000 000 − 4 000 000 = 6 000 000 soʻm. "
                               "«10 000 000» — hamma tushum, yutuqlar "
                               "ayirilmagan.",
            },
        ],
        "body": """
<p>Bahor bayramida maktab hovlisida
<span class="cn-word" data-tr="tasodifiy yutuqqa asoslangan oʻyin">lotereya</span>
oʻtkazildi. Devorga katta varaq osib qoʻyilgan edi va unda hamma sonlar
ochiq yozilgandi.</p>

<p>Jami <strong>2 000</strong> ta
<span class="cn-word" data-tr="oʻyinda qatnashish huquqini beruvchi raqamli varaqa">bilet</span>
chiqarilgan. Har biri <strong>5 000</strong> soʻm.</p>

<p>Yutuqlar ham yozilgan edi: bitta velosiped — 1 500 000 soʻm; beshta
quloqchin — har biri 200 000 soʻm; ellikta kitob — har biri
30 000 soʻm.</p>

<p>Sherbek varaqni oʻqidi va daftariga koʻchira boshladi.</p>

<p>Avval <span class="cn-word" data-tr="hamma yutuqlarga ajratilgan umumiy pul">yutuq fondi</span>ni
topdi: 1 500 000 + 5 × 200 000 + 50 × 30 000 = 1 500 000 + 1 000 000 +
1 500 000 = <strong>4 000 000</strong> soʻm.</p>

<p>Keyin <span class="cn-word" data-tr="sotuvdan yigʻilgan umumiy pul">tushum</span>ni
hisobladi: 2 000 × 5 000 = <strong>10 000 000</strong> soʻm.</p>

<p>Yutuqli biletlar soni: 1 + 5 + 50 = <strong>56</strong> ta. Bular —
<span class="cn-word" data-tr="bizni qiziqtirgan natijalar">qulay hollar</span>.</p>

<p>Demak yutish
<span class="cn-word" data-tr="hodisaning roʻy berish imkoniyati oʻlchovi">ehtimollik</span>i
56 ÷ 2 000 = <strong>0,028</strong>, ya'ni 2,8
<span class="cn-word" data-tr="yuzdan boʻlak">foiz</span>.</p>

<p>Yutmaslik ehtimolligini Sherbek sanab oʻtirmadi.
<span class="cn-word" data-tr="berilgan hodisa roʻy bermasligi">Teskari hodisa</span>
qoidasi bir qatorda javob berdi: 1 − 0,028 = <strong>0,972</strong> —
97,2 foiz.</p>

<p>Lekin eng qiziq son oxirida chiqdi. Sherbek yutuq fondini biletlar
soniga boʻldi: 4 000 000 ÷ 2 000 = <strong>2 000</strong> soʻm. Bu —
bitta biletga toʻgʻri keladigan
<span class="cn-word" data-tr="bir biletga toʻgʻri keladigan yutuq puli">oʻrtacha qaytim</span>.</p>

<p>Bilet 5 000 soʻm turadi, qaytim esa 2 000 soʻm. Har 5 000 soʻmdan
2 000 soʻm qaytadi, qolgan 3 000 soʻm esa
<span class="cn-word" data-tr="oʻyinni oʻtkazuvchi tomon">tashkilotchi</span>da
qoladi. Hammasi boʻlib 10 000 000 − 4 000 000 = <strong>6 000 000</strong>
soʻm.</p>

<p>Sherbek daftarini yopdi va shunday deb yozib qoʻydi: «Lotereyada
yutqazish uchun omadsiz boʻlish shart emas. Yutqazish oʻyinning
<span class="cn-word" data-tr="oldindan qoʻyilgan talab, kelishuv">shart</span>iga
kiritib qoʻyilgan».</p>

<p>Shunga qaramay u bitta bilet oldi va kitob yutib chiqdi. Chunki
<span class="cn-word" data-tr="oldindan aytib boʻlmaydigan natija">tasodif</span>
2,8 foizni ham baʼzan tanlaydi — faqat unga tayanib boʻlmaydi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-85 — masalani oʻqishning toʻrt qadami                QOʻLLANMA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Masalani qanday oʻqish kerak",
        "summary": (
            "PM-85 matni. Qoʻllanma: Nodira opa sinfga toʻrt qadamni "
            "tushuntiradi va bitta masalani ular bilan yechib koʻrsatadi. "
            "Toʻrtinchi qadam eng koʻp xatoni ushlaydi."
        ),
        "order":   85,
        "grammar": [
            {
                "pattern":  "oʻqi → reja tuz → yech → tekshir",
                "meaning":  "Matnli masalani yechishning toʻrt qadami. "
                            "Birinchi qadam eng uzun, uchinchisi eng "
                            "qisqa boʻlishi kerak.",
                "examples": [
                    "berilgan: 32 oʻquvchi; qizlar oʻgʻillardan 6 taga kam",
                    "reja: x — oʻgʻillar, qizlar — x − 6",
                    "yechish: x + (x − 6) = 32 → 2x = 38 → x = 19",
                    "tekshirish: 19 + 13 = 32 ✓ va 19 − 13 = 6 ✓",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nodira opaning qoidasiga koʻra masalani oʻqiyotganda "
                        "birinchi navbatda nima qilinadi?",
                "choices": [
                    "Soʻralgan savol alohida yozib qoʻyiladi",
                    "Sonlar darrov qoʻshib chiqiladi",
                    "Javob taxmin qilinadi",
                    "Tenglama tuziladi",
                ],
                "answer": 0,
                "explanation": "Nodira opa taxtaga birinchi boʻlib savolni "
                               "koʻchirdi. Uning gapi: koʻp bola masalani "
                               "yecholmagani uchun emas, boshqa savolga "
                               "javob bergani uchun xato qiladi.",
            },
            {
                "text": "Sinfda nechta oʻgʻil bola bor?",
                "choices": ["13", "16", "19", "26"],
                "answer": 2,
                "explanation": "x — oʻgʻillar soni, qizlar — x − 6. "
                               "x + (x − 6) = 32 → 2x − 6 = 32 → 2x = 38 "
                               "→ x = 19. «13» — qizlar soni, «16» esa "
                               "32 ni shunchaki teng ikkiga boʻlganda "
                               "chiqadi va 6 talik farqni yoʻqotadi.",
            },
            {
                "text": "Bir oʻquvchi «32 ÷ 2 = 16» deb javob berdi. U qaysi "
                        "qadamda xato qilgan?",
                "choices": [
                    "Uchinchi qadamda — notoʻgʻri hisoblagan",
                    "Birinchi qadamda — 6 talik farqni oʻqimagan",
                    "Toʻrtinchi qadamda — javobni yozmagan",
                    "Ikkinchi qadamda — notoʻgʻri harf tanlagan",
                ],
                "answer": 1,
                "explanation": "32 ÷ 2 = 16 hisobi toʻgʻri, lekin u "
                               "«qizlar oʻgʻillardan 6 taga kam» degan "
                               "shartni umuman ishlatmaydi. Demak xato "
                               "hisobda emas, oʻqishda — birinchi "
                               "qadamda.",
            },
        ],
        "body": """
<p>Nodira opa taxtaga
<span class="cn-word" data-tr="vaziyat matn bilan berilgan masala">matnli masala</span>
yozdi: «Sinfda 32 oʻquvchi bor. Qizlar oʻgʻillardan 6 taga kam. Nechta
oʻgʻil bola bor?»</p>

<p>Sinf darrov shovqin koʻtardi. Kimdir «16!» dedi, kimdir «13!» dedi.</p>

<p>Nodira opa qoʻlini koʻtardi. «Toʻxtang. Bugun biz javobni emas,
<span class="cn-word" data-tr="yechishning oldindan tuzilgan yoʻli">reja</span>ni
oʻrganamiz. Toʻrtta qadam bor».</p>

<p><b>Birinchi qadam — oʻqish.</b> U masalani ikki marta oʻqidi.
Keyin taxtaning chetiga faqat savolni koʻchirdi: «Nechta oʻgʻil?»
«Koʻp bola masalani yecha olmagani uchun emas, boshqa savolga javob
bergani uchun xato qiladi», dedi u.</p>

<p>Soʻng <span class="cn-word" data-tr="masalada aytilgan maʼlumot">berilgan</span>
maʼlumotni yozdi: jami 32; farq 6.</p>

<p><b>Ikkinchi qadam — reja.</b> «Endi
<span class="cn-word" data-tr="topilishi kerak boʻlgan miqdor">nomaʼlum</span>ni
tanlaymiz. Savol oʻgʻillar haqida, demak x — oʻgʻillar soni. Qizlar
oʻgʻillardan 6 taga kam ekan: <strong>x − 6</strong>».</p>

<p>Shundan keyin
<span class="cn-word" data-tr="ikki ifodaning tengligi">tenglama</span>
oʻzi paydo boʻldi: <strong>x + (x − 6) = 32</strong>. Chap tomondagi
<span class="cn-word" data-tr="harf va sonlardan tuzilgan yozuv">ifoda</span>
sinfdagi hamma bolani sanab chiqardi.</p>

<p><b>Uchinchi qadam — yechish.</b> Bu eng qisqa qadam boʻldi. Avval
<span class="cn-word" data-tr="oʻxshash hadlarni birlashtirib qisqartirish">ixchamlash</span>:
2x − 6 = 32, keyin 2x = 38, demak <strong>x = 19</strong>. Qizlar esa
19 − 6 = <strong>13</strong> ta.</p>

<p><b>Toʻrtinchi qadam —
<span class="cn-word" data-tr="javobni masala shartlariga qaytarib qoʻyish">tekshirish</span>.</b>
Nodira opa javobni masalaning
oʻz gaplariga qaytarib qoʻydi. Jami: 19 + 13 = 32 ✓
<span class="cn-word" data-tr="«nechtaga koʻp» savolining javobi">Ayirma</span>:
19 − 13 = 6 ✓ Ikkala
<span class="cn-word" data-tr="bajarilishi kerak boʻlgan bogʻlanish">shart</span>
ham bajarildi.</p>

<p>«Endi qarang», dedi u. «Kim 16 degan boʻlsa, 32 ni teng ikkiga
boʻlgan. Hisobi toʻgʻri, lekin 6 talik farqni umuman ishlatmagan. Bu —
uchinchi qadamning emas,
<span class="cn-word" data-tr="masalani oʻqib, berilgan va soʻralganni ajratish">birinchi qadam</span>ning
xatosi.</p>

<p>«Kim 13 degan boʻlsa esa hammasini toʻgʻri hisoblagan — faqat
<span class="cn-word" data-tr="masalaning savoli">soʻralgan</span>
narsani emas, qizlar sonini aytgan».</p>

<p>Doskaga oxirgi qatorni yozdi va shu bilan darsni tugatdi:
«<b>Javob:</b> sinfda 19 ta oʻgʻil bola bor». Bitta son emas — butun
gap.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-86 — nomaʼlumni tanlash                                 HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Uch aka-uka va pul",
        "summary": (
            "PM-86 matni. Hikoya: uch aka-uka bogʻda ishlab, haqni "
            "soatiga qarab boʻlishmoqchi. Kim necha soat ishlaganini "
            "hech kim aniq eslay olmaydi — faqat bir-biriga nisbatan."
        ),
        "order":   86,
        "grammar": [
            {
                "pattern":  "x = qolganlari oʻzi orqali oʻlchanadigan miqdor",
                "meaning":  "Nomaʼlumni tanlash qoidasi. Boshqa "
                            "miqdorlar kimga qarab taʼriflangan boʻlsa, "
                            "oʻsha x boʻladi — odatda eng kichigi.",
                "examples": [
                    "Bekzod — x; Sherbek — 2x; Jasur — x + 3",
                    "x + 2x + (x + 3) = 23 → 4x = 20 → x = 5",
                    "5 + 10 + 8 = 23 ✓",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega aka-ukalar Bekzodning soatlarini x deb "
                        "olishdi?",
                "choices": [
                    "U eng katta aka boʻlgani uchun",
                    "U hisob-kitobni yaxshi bilgani uchun",
                    "U eng koʻp ishlagani uchun",
                    "Qolgan ikkovining soati unga qarab aytilgani uchun",
                ],
                "answer": 3,
                "explanation": "Sherbek «Bekzoddan 2 marta koʻp», Jasur "
                               "esa «Bekzoddan 3 soat koʻp» ishlagan. "
                               "Ikkala bogʻlanish ham Bekzoddan "
                               "oʻlchangani uchun uni x deb olish "
                               "hammasini bitta harf bilan yozish "
                               "imkonini beradi.",
            },
            {
                "text": "Sherbek necha soat ishlagan?",
                "choices": ["5 soat", "8 soat", "10 soat", "13 soat"],
                "answer": 2,
                "explanation": "x + 2x + (x + 3) = 23 → 4x + 3 = 23 → "
                               "4x = 20 → x = 5. Bekzod 5 soat, Sherbek "
                               "esa 2 × 5 = 10 soat. «8 soat» — "
                               "Jasurniki, «13» esa 23 dan 10 ni "
                               "ayirganda chiqadi.",
            },
            {
                "text": "Jasur qancha pul oldi?",
                "choices": [
                    "50 000 soʻm",
                    "80 000 soʻm",
                    "100 000 soʻm",
                    "230 000 soʻm",
                ],
                "answer": 1,
                "explanation": "Bir soatning haqi: 230 000 ÷ 23 = "
                               "10 000 soʻm. Jasur 8 soat ishlagan, "
                               "demak 8 × 10 000 = 80 000 soʻm. "
                               "«50 000» — Bekzodniki, «100 000» — "
                               "Sherbekniki.",
            },
        ],
        "body": """
<p>Karim aka bogʻidagi olmalarni yigʻish uchun uch jiyanini chaqirdi:
Bekzod, Sherbek va Jasur. Ish tugagach, u stol ustiga
<strong>230 000</strong> soʻm qoʻydi.</p>

<p>«Bu — hammangizning
<span class="cn-word" data-tr="bajarilgan ish uchun toʻlanadigan pul">haq</span>ingiz.
Kim qancha ishlagan boʻlsa, oʻshanga yarasha
<span class="cn-word" data-tr="butunni ulushlarga ajratish">taqsimlan</span>g»,
dedi u va uyga kirib ketdi.</p>

<p>Uch aka-uka bir-biriga qaradi. Muammo shu ediki, hech kim soatni
yozib bormagan edi.</p>

<p>«Men aniq bilaman, sendan ikki marta koʻp ishladim», dedi Sherbek
Bekzodga.</p>

<p>«Men esa sendan uch soat koʻp turdim», dedi Jasur ham Bekzodga.</p>

<p>«Hammamiz birga 23 soat ishladik — buni Karim aka aytdi», dedi
Bekzod.</p>

<p>Jasur daftar oldi. «Uchta
<span class="cn-word" data-tr="topilishi kerak boʻlgan miqdor">nomaʼlum</span>
bor, lekin uchta harf yozish shart emas. Qaranglar: Sherbekning ham,
mening ham soatim <b>Bekzodga qarab</b> aytilgan».</p>

<p>Shuning uchun ular Bekzodning soatlarini <strong>x</strong> deb
olishdi. Bu — eng kichik miqdor, va qolgan ikkovi undan
<span class="cn-word" data-tr="miqdorlarni bir-biriga ulovchi shart">bogʻlanish</span>
orqali chiqadi.</p>

<p>Jasur daftarga
<span class="cn-word" data-tr="maʼlumotni qator va ustunlarga joylash">jadval</span>
chizdi. Bekzod — x. Sherbek — <strong>2x</strong>. Jasur —
<strong>x + 3</strong>. Uchala
<span class="cn-word" data-tr="harf va sonlardan tuzilgan yozuv">ifoda</span>da
ham bitta harf ishlatilgani muhim edi.</p>

<p>Endi <span class="cn-word" data-tr="ikki ifodaning tengligi">tenglama</span>
oʻzi koʻrindi: <strong>x + 2x + (x + 3) = 23</strong>.</p>

<p><span class="cn-word" data-tr="koʻpaytuvchini qavs ichiga tarqatish">Qavsni ochib</span>,
<span class="cn-word" data-tr="bir xil harfli hadlarni birlashtirish">oʻxshash hadlar</span>ni
yigʻdilar: 4x + 3 = 23. Keyin 4x = 20, demak <strong>x = 5</strong>.
Javob <span class="cn-word" data-tr="kasrsiz, toʻliq son">butun son</span>
chiqqani ham nomaʼlum toʻgʻri tanlanganini koʻrsatib turardi.</p>

<p>Bekzod 5 soat, Sherbek 2 × 5 = <strong>10</strong> soat, Jasur
5 + 3 = <strong>8</strong> soat ishlagan ekan.</p>

<p><span class="cn-word" data-tr="javobni masala shartlariga qaytarib qoʻyish">Tekshirish</span>
darrov qilindi: 5 + 10 + 8 = 23 ✓ Sherbek Bekzoddan roppa-rosa ikki
marta koʻp ✓ Jasur uch soat koʻp ✓</p>

<p>Endi pul. Bir soatning haqi: 230 000 ÷ 23 = <strong>10 000</strong>
soʻm — bu hamma uchun bir xil
<span class="cn-word" data-tr="bir birlikka toʻgʻri keladigan miqdor">birlik qiymat</span>.
Demak Bekzod 50 000, Sherbek 100 000, Jasur 80 000 soʻm oladi.</p>

<p>Sherbek yana bir bor
<span class="cn-word" data-tr="qoʻshish amalining natijasi">yigʻindi</span>ni
chiqarib koʻrdi: 50 000 + 100 000 + 80 000 = 230 000 ✓</p>

<p>«Bir soat bahslashgan boʻlardik», dedi u. «Bitta harf yetti daqiqada
hal qildi».</p>
""",
    },
]
