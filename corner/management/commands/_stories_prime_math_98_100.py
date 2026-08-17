# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-98, PM-99, PM-100. **KOLLEKSIYANING YAKUNI.**

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 98 — jumboq, 99 — tarix, 100 — xat.
95 jumboq, 96 jumboq, 97 ilmiy-ommabop edi; 98 yana jumboq, lekin
97 oraliqni uzgan — uchtasi ketma-ket bir xil shakl emas.

⚠️ Kumulyativ:
   • 98-matnda teskaridan yurish. Klassik «qopdagi yongʻoq» masalasi;
     sonlar darsdagilardan boshqa;
   • 99-matnda Gaussning bolaligi. ⚠️ FAKT: hikoyaning oʻzi rivoyat
     (manbalarda tafsilotlar har xil), shuning uchun matn buni ochiq
     aytadi — «rivoyat qilishlaricha». Matematikasi esa aniq:
     1..100 = 5050. Gauss 1777–1855, nemis matematigi — bu rost;
   • 100-matn — XAT. Butun kollektsiyaning oxirgi matni. Unda yangi
     matematika yoʻq; u oʻquvchiga qaratilgan va PM-100 darsining
     ohangini davom ettiradi.
⚠️ Savollar SAQLANGAN TARTIBDA koʻrsatiladi — `answer` indekslari:
   98 → 1/3/0, 99 → 2/0/3, 100 → 3/1/2.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_98_100.py --author=prime
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
    # PM-98 — teskaridan yurish                                  JUMBOQ
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Qopdagi yongʻoq",
        "summary": (
            "PM-98 matni. Jumboq: uch aka-uka qopdan navbat bilan "
            "yongʻoq oladi va oxirida 6 tasi qoladi. Boshida nechta "
            "edi? Oldinga yurib boʻlmaydi — orqaga yuriladi."
        ),
        "order":   98,
        "grammar": [
            {
                "pattern":  "oxiridan boshla, har amalni teskarisiga almashtir",
                "meaning":  "Boshlangʻich miqdor nomaʼlum, oxirgi "
                            "natija maʼlum boʻlsa, amallar teskari "
                            "tartibda va teskari maʼnoda bajariladi.",
                "examples": [
                    "6 + 2 = 8 → 8 × 2 = 16 (uchinchisidan oldin)",
                    "16 + 2 = 18 → 18 × 2 = 36 (ikkinchisidan oldin)",
                    "36 + 2 = 38 → 38 × 2 = 76 (boshida)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nima uchun bolalar masalani oldinga yurib yecha "
                        "olmadi?",
                "choices": [
                    "Sonlar juda katta edi",
                    "Boshlangʻich miqdor nomaʼlum edi",
                    "Qopni ochish mumkin emas edi",
                    "Uch aka-uka juda tez ishladi",
                ],
                "answer": 1,
                "explanation": "Oldinga yurish uchun boshlangʻich son "
                               "kerak, u esa aynan soʻralayotgan narsa "
                               "edi. Oxirgi natija maʼlum boʻlgani "
                               "uchun teskari yoʻl qoladi.",
            },
            {
                "text": "Uchinchi aka olishdan oldin qopda nechta yongʻoq "
                        "bor edi?",
                "choices": ["8 ta", "12 ta", "14 ta", "16 ta"],
                "answer": 3,
                "explanation": "Oxirida 6 ta qoldi. Uchinchi aka "
                               "«yarmini va yana 2 tasini» olgan, demak "
                               "orqaga: 6 + 2 = 8, keyin 8 × 2 = 16. "
                               "Tekshirish: 16 ning yarmi 8, yana "
                               "2 tasi — jami 10 ta olindi, 6 ta "
                               "qoldi ✓",
            },
            {
                "text": "Boshida qopda nechta yongʻoq bor edi?",
                "choices": ["76 ta", "54 ta", "38 ta", "36 ta"],
                "answer": 0,
                "explanation": "Orqaga uch qadam: 6 → 16 → 36 → 76. "
                               "Har safar avval 2 qoʻshiladi, keyin "
                               "ikkiga koʻpaytiriladi. Oldinga "
                               "tekshirish: 76 → 36 → 16 → 6 ✓",
            },
        ],
        "body": """
<p>Kuz edi. Bobo hovlida yongʻoq qoqdi va toʻla qopni ayvonga qoʻyib,
uch nevarasiga bitta shart aytdi.</p>

<p>«Ertalab har biringiz <span class="cn-word" data-tr="belgilangan tartibda ketma-ket">navbat</span>
bilan qopdan yongʻoq olasiz. Faqat
shunday: qopdagining <b>yarmini va yana 2 tasini</b> olasiz.
Kamroq ham, koʻproq ham emas».</p>

<p>Ertasi kuni hammasi shunday boʻldi. Katta aka birinchi boʻlib
oldi, oʻrtanchasi ikkinchi, kichigi uchinchi.</p>

<p>Kechqurun bobo qopga qaradi va u yerda
<span class="cn-word" data-tr="hamma amaldan keyin qolgan miqdor">oxirgi natija</span>
koʻrindi: roppa-rosa <strong>6</strong> ta yongʻoq.</p>

<p>«Endi ayting-chi», dedi u, «ertalab qopda nechta yongʻoq bor edi?»</p>

<p>Kichik nevara darrov hisoblay boshladi. «Aytaylik, 100 ta bor
edi…» — lekin natija 6 chiqmadi. «Unda 80 ta…» — bu ham
toʻgʻri kelmadi.</p>

<p>U bir necha <span class="cn-word" data-tr="tekshirilmagan, ehtimoliy fikr">taxmin</span>ni
sinab koʻrdi va har safar boshqa son chiqdi.</p>

<p>«Sen notoʻgʻri <span class="cn-word" data-tr="harakat yoʻnalishi">tomon</span>dan
yuryapsan», dedi bobo. «Boshlanishni
bilmaysan — lekin <b>oxirini</b> bilasan. Oʻsha tomondan yur».</p>

<p>Kichik nevara toʻxtadi. Qopda 6 ta qolgan. Uchinchi aka olishdan
oldin qancha bor edi?</p>

<p>U <span class="cn-word" data-tr="bajarilgan amalni bekor qiluvchi amal">teskari amal</span>ni
oʻyladi. Aka «yarmini va yana 2 tasini» olgan. Demak orqaga qaytishda
avval 2 ni <b>qaytarish</b> kerak: 6 + 2 = <strong>8</strong>.</p>

<p>Endi 8 — bu qopdagining roppa-rosa
<span class="cn-word" data-tr="butunning ikkiga boʻlingan qismi">yarmi</span>.
Demak <span class="cn-word" data-tr="hamma qismlardan iborat toʻliq miqdor">butun</span>
miqdor 8 × 2 = <strong>16</strong> ta boʻlgan.</p>

<p>«Toʻgʻri», dedi bobo. «Endi yana bir qadam».</p>

<p>Oʻrtancha aka olishdan oldin: 16 + 2 = 18, keyin 18 × 2 =
<strong>36</strong>.</p>

<p>Katta aka olishdan oldin: 36 + 2 = 38, keyin 38 × 2 =
<strong>76</strong>.</p>

<p>«Ertalab qopda 76 ta yongʻoq bor edi» — mana
<span class="cn-word" data-tr="izlanayotgan dastlabki miqdor">boshlangʻich qiymat</span>,
dedi kichik nevara.</p>

<p>Bobo bosh irgʻadi, lekin qoʻshib qoʻydi: «Javob topilgani
<span class="cn-word" data-tr="talabni qondiradigan darajada">yetarli</span> emas.
Endi <span class="cn-word" data-tr="javobni boshiga qoʻyib, amallarni qayta bajarish">oldinga yurib</span>
tekshir».</p>

<p>Nevara daftarga har bir <span class="cn-word" data-tr="sxemadagi bitta amal">qadam</span>ni
yozdi. 76 ta bor edi. Katta aka yarmini (38) va
yana 2 tasini oldi — jami 40 ta; qopda 36 ta qoldi. Oʻrtanchasi
18 + 2 = 20 ta oldi; 16 ta qoldi. Kichigi 8 + 2 = 10 ta oldi; qopda
<strong>6</strong> ta qoldi.</p>

<p>Masaladagi son bilan bir xil ✓</p>

<p>«Mana endi javob», dedi bobo.</p>

<p>«Lekin nega taxmin qilib topib boʻlmadi?» — soʻradi nevara.</p>

<p>«Topsa boʻlardi», dedi bobo. «Ertalabgacha sinab oʻtirsang. Lekin
<span class="cn-word" data-tr="oxirgi natijadan boshlanishga qaytish">teskaridan yurish</span>da
sinash yoʻq — har bir qadam <b>bitta</b> javob beradi. Shuning uchun u
qisqa».</p>

<p>Keyin u qopni koʻtardi va kuldi: «Aslida men ertalab sanagandim.
Yetmish olti. Lekin sen buni <span class="cn-word" data-tr="dalil bilan koʻrsatib topish">hisoblab</span>
topding — bu boshqacha».</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-99 — namuna izlash                                       TARIX
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Gaussning bolaligi — 1 dan 100 gacha",
        "summary": (
            "PM-99 matni. Tarix: nemis matematigi Karl Fridrix Gauss "
            "haqidagi mashhur rivoyat va uning ortidagi aniq "
            "matematika — juftlash usuli."
        ),
        "order":   99,
        "grammar": [
            {
                "pattern":  "1 + 2 + … + n = n × (n + 1) ÷ 2",
                "meaning":  "Sonlarni ikki uchidan juftlash usuli. Har "
                            "bir juftlik bir xil yigʻindi beradi; "
                            "juftliklar soni esa n ÷ 2 ta boʻladi.",
                "examples": [
                    "1 + 100 = 101, 2 + 99 = 101, 3 + 98 = 101 …",
                    "50 ta juftlik × 101 = 5050",
                    "formula bilan: 100 × 101 ÷ 2 = 5050",
                ],
            },
        ],
        "questions": [
            {
                "text": "Gauss javobni qanday topgan?",
                "choices": [
                    "Hamma sonni ketma-ket qoʻshib",
                    "Javobni oldindan yodlab olib",
                    "Sonlarni ikki uchidan juftlab",
                    "Yuzta sonning oʻrtachasini olib",
                ],
                "answer": 2,
                "explanation": "U 1 bilan 100 ni, 2 bilan 99 ni "
                               "juftlagan. Har bir juftlik 101 beradi "
                               "va bunday juftliklar 50 ta: "
                               "50 × 101 = 5050.",
            },
            {
                "text": "Nechta juftlik hosil boʻladi va har biri qanchaga "
                        "teng?",
                "choices": [
                    "50 ta juftlik, har biri 101",
                    "100 ta juftlik, har biri 101",
                    "50 ta juftlik, har biri 100",
                    "101 ta juftlik, har biri 50",
                ],
                "answer": 0,
                "explanation": "Yuzta son ikkitadan juftlanadi, demak "
                               "100 ÷ 2 = 50 ta juftlik. Har birining "
                               "yigʻindisi 1 + 100 = 101. Natija: "
                               "50 × 101 = 5050.",
            },
            {
                "text": "Xuddi shu usul bilan 1 dan 20 gacha yigʻindi "
                        "qancha boʻladi?",
                "choices": ["105", "190", "200", "210"],
                "answer": 3,
                "explanation": "10 ta juftlik, har biri 1 + 20 = 21: "
                               "10 × 21 = 210. Formula bilan ham xuddi "
                               "shunday: 20 × 21 ÷ 2 = 210.",
            },
        ],
        "body": """
<p>Karl Fridrix Gauss (1777–1855) — nemis matematigi. Uni koʻpincha
tarixdagi eng buyuk matematiklardan biri deb atashadi: u sonlar
nazariyasida, geometriyada, astronomiyada va fizikada ishlagan.</p>

<p>Uning bolaligi haqida bir <span class="cn-word" data-tr="ogʻizdan ogʻizga oʻtgan hikoya">rivoyat</span>
bor. Rivoyat qilishlaricha, u hali boshlangʻich sinfda oʻqiyotganda
oʻqituvchi sinfga uzoq davom etadigan vazifa bergan: <b>1 dan 100
gacha boʻlgan hamma sonni qoʻshing</b>.</p>

<p>Oʻqituvchining hisobiga koʻra bu bolalarni bir soatga band qilishi
kerak edi. Kichkina Gauss esa bir necha soniyadan keyin javobni
aytgan: <strong>5050</strong>.</p>

<p>Tafsilotlar turli manbalarda har xil aytiladi — bu rivoyatning
tabiati. Lekin uning ichidagi matematika aniq va uni har kim
tekshira oladi.</p>

<p>Gauss tezroq <span class="cn-word" data-tr="qoʻshish amalini bajarish">qoʻsh</span>magan.
U sonlarni boshqacha
<span class="cn-word" data-tr="maʼlum tartibda guruhlarga ajratish">joylashtir</span>gan.</p>

<p>Qatorni ikki uchidan olib
<span class="cn-word" data-tr="ikki uchidagi sonlarni birlashtirib qoʻshish">juftlash</span>
mumkin: birinchi son bilan oxirgisi, ikkinchi son bilan
oxiridan ikkinchisi va hokazo.</p>

<p>1 + 100 = <strong>101</strong>. 2 + 99 = <strong>101</strong>.
3 + 98 = <strong>101</strong>.</p>

<p>Bu tasodif emas. Bir tomondan son bittaga oshadi, ikkinchi tomondan
bittaga kamayadi — demak yigʻindi
<span class="cn-word" data-tr="qiymati oʻzgarmaydigan kattalik">oʻzgarmas</span>
qoladi. Bu — PM-96 dagi invariant gʻoyasining oʻzi.</p>

<p>Yuzta son ikkitadan juftlansa, <strong>50</strong> ta
<span class="cn-word" data-tr="ikki sondan iborat guruh">juftlik</span>
hosil boʻladi. Har birining
<span class="cn-word" data-tr="qoʻshish amalining natijasi">yigʻindi</span>si
101 ga teng.</p>

<p>Demak yigʻindi 50 × 101 = <strong>5050</strong>.</p>

<p>Endi eng qizigʻi. Bu usul faqat 100 uchun emas — istalgan son uchun
ishlaydi. Agar sonlar 1 dan n gacha boʻlsa, juftliklar soni n ÷ 2 ta,
har birining yigʻindisi esa n + 1 ga teng.</p>

<p>Shundan <span class="cn-word" data-tr="qoidaning harflar bilan yozuvi">formula</span>
chiqadi: <strong>n × (n + 1) ÷ 2</strong>.</p>

<p>Uni kichik sonlarda <span class="cn-word" data-tr="javobni bevosita hisoblab solishtirish">tekshir</span>ish
oson. n = 4 uchun: 4 × 5 ÷ 2 = 10, va haqiqatan 1 + 2 + 3 + 4 = 10 ✓
n = 10 uchun: 10 × 11 ÷ 2 = 55 ✓</p>

<p>Bu hikoyada eng muhimi tezlik emas. Muhimi shuki, Gauss savolni
oʻzgartirgan. Oʻqituvchi «qoʻshing» degan edi; bola esa oʻzidan
soʻragan: <b>bu sonlarda qanday
<span class="cn-word" data-tr="takrorlanadigan qonuniyat">namuna</span>
bor?</b></p>

<p>Aynan shu — <span class="cn-word" data-tr="bir necha holdan umumiy qoida chiqarish">umumlashtirish</span>
matematikaning yuragi. Bitta masalani yechish — bir masalani hal
qiladi. Namunani koʻrish esa cheksiz koʻp masalani birdaniga hal
qiladi.</p>

<p>Gauss keyinchalik shunday yozgan deb keltiriladi: matematika —
fanlar malikasi. Uning bu qarashi, ehtimol, ana shu darsdan
boshlangandir.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-100 — YAKUNIY XAT                                          XAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Yuz darsdan keyin — oʻquvchiga xat",
        "summary": (
            "PM-100 matni. Xat: kursni yozgan odamdan uni oxirigacha "
            "oʻqib chiqqan oʻquvchiga. Kollektsiyaning oxirgi matni."
        ),
        "order":   100,
        "grammar": [
            {
                "pattern":  "qoidani yodlash emas, sababini tushunish",
                "meaning":  "Kursning butun tuzilishi shu gʻoyaga "
                            "asoslangan. Yodlangan qoida unutiladi; "
                            "sababi tushunilgan qoida esa unutilsa "
                            "ham qayta tiklanadi.",
                "examples": [
                    "kasrga boʻlish — teskarisiga koʻpaytirish (PM-18)",
                    "1 m² = 10 000 sm², chunki yuza ikki uzunlik koʻpaytmasi (PM-94)",
                    "toq son juftga aylanmaydi, chunki oʻzgarish har doim juft (PM-96)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Xat muallifiga koʻra, kursning eng muhim savoli "
                        "qaysi?",
                "choices": [
                    "«Javob nechchi?»",
                    "«Qaysi formula kerak?»",
                    "«Bu qoidani yodlash kerakmi?»",
                    "«Javob mantiqiymi?»",
                ],
                "answer": 3,
                "explanation": "Bu savol hech qanday hisob talab "
                               "qilmaydi, lekin velosipedda "
                               "120 km/soat, 1,2 ga teng ehtimollik "
                               "yoki eritmadan ogʻir tuz kabi "
                               "xatolarning hammasini ushlaydi.",
            },
            {
                "text": "Muallif nima uchun qoidani yodlashni yetarli "
                        "deb hisoblamaydi?",
                "choices": [
                    "Yodlash juda koʻp vaqt oladi",
                    "Yodlangan qoida unutiladi, tushunilgani esa qayta tiklanadi",
                    "Qoidalar tez-tez oʻzgarib turadi",
                    "Imtihonda formulalar beriladi",
                ],
                "answer": 1,
                "explanation": "Xatda aynan shunday deyilgan: kasrga "
                               "boʻlishda nega teskarisiga "
                               "koʻpaytirilishini bilgan odam "
                               "formulani esdan chiqarsa ham, uni "
                               "oʻzi tiklay oladi.",
            },
            {
                "text": "Muallifning fikricha, «bilmayman» degan javob "
                        "qachon toʻgʻri boʻladi?",
                "choices": [
                    "Hech qachon — har doim javob berish kerak",
                    "Faqat imtihonda",
                    "Maʼlumot yetarli boʻlmaganda",
                    "Masala juda qiyin boʻlganda",
                ],
                "answer": 2,
                "explanation": "Kursda bu bir necha marta uchradi: "
                               "yetishmayotgan maʼlumotli masalada "
                               "(PM-94) va Dirixle prinsipida — u "
                               "bunday odam borligini isbotlaydi, "
                               "lekin kimligini aytmaydi (PM-97).",
            },
        ],
        "body": """
<p><i>Assalomu alaykum.</i></p>

<p>Agar siz bu matnni oʻqiyotgan boʻlsangiz, demak yuzta darsni
oxirigacha oʻqib chiqdingiz. Buni koʻp odam qilmaydi. Shuning uchun
birinchi gap oddiy: <b>rahmat</b>.</p>

<p>Bu xatni yozishdan maqsad — yangi narsa oʻrgatish emas. Faqat bir
necha gapni aytib qoʻyish.</p>

<p><b>Birinchisi.</b> Siz PM-1 da razryaddan boshlagansiz — 25 dagi
2 nima uchun ikkita emas, yigirmata ekanidan. Bu juda kichik savolga
oʻxshaydi. Lekin oʻsha savol yetmish beshinchi darsda ham qaytib
keldi: ikki xonali son <b>10a + b</b> boʻladi, a + b emas. Kursda
kichik gʻoyalar yoʻqolmaydi — ular keyin qurol boʻlib qaytadi.</p>

<p><b>Ikkinchisi.</b> Bu kursda bir
<span class="cn-word" data-tr="qoidaning harflar bilan yozuvi">formula</span>
uch marta uchradi.
Harakatda S = v × t, ishda ish = unumdorlik × vaqt, savdoda qiymat =
narx × miqdor. Uchalasida oʻrtadagi <span class="cn-word" data-tr="oʻlchanadigan miqdor">kattalik</span>
bitta maʼnoni bildiradi:
<b>bitta birlikka toʻgʻri keladigan miqdor</b>.</p>

<p>Agar siz buni koʻrgan boʻlsangiz, uch dars oʻrniga bitta gʻoya
oʻrgangansiz. Matematika aslida shunday ishlaydi — u qoidalarni
koʻpaytirmaydi, ularni <b>kamaytiradi</b>.</p>

<p><b>Uchinchisi.</b> Kursning eng foydali savoli hech qanday hisob
talab qilmaydi: <b>javob mantiqiymi?</b></p>

<p>Velosipedda 120 km/soat. Eritmadagi
<span class="cn-word" data-tr="aralashma ichidagi toza modda">sof tuz</span>
eritmaning oʻzidan ogʻir.
<span class="cn-word" data-tr="hodisaning roʻy berish imkoniyati oʻlchovi">Ehtimollik</span>
1,2. Yordamchi kelgach ish sekinlashdi. Bu
javoblarning hammasi bitta savol bilan ushlanadi va uni berish uchun
kalkulyator kerak emas.</p>

<p><b>Toʻrtinchisi.</b> Bu kursda «bilmayman» bir necha marta toʻgʻri
javob boʻldi.</p>

<p>Nokning <span class="cn-word" data-tr="bir birlik mahsulotning puli">narx</span>i
berilmagan masalada (PM-94) toʻgʻri javob —
<span class="cn-word" data-tr="yechish uchun kerakli berilganlar">maʼlumot</span>
yetarli emasligini aytish. Dirixle prinsipida (PM-97) toʻgʻri
javob — bunday ikki kishi borligini isbotlash, lekin kimligini
aytmaslik. Namunada (PM-99) toʻgʻri javob — bu hali
<span class="cn-word" data-tr="dalil bilan koʻrsatilgan haqiqat">isbot</span>
emas, faqat <span class="cn-word" data-tr="tekshirilmagan fikr">taxmin</span>
ekanini tan olish.</p>

<p>Nimani bilmasligini aniq bilish — koʻnikma. Va u matematikadan
tashqarida ham kerak boʻladi.</p>

<p><b>Beshinchisi.</b> Endi nima qilish haqida.</p>

<p>Agar imtihonga tayyorlanayotgan boʻlsangiz — SAT Math kursi
sizni kutmoqda. U inglizcha, lekin matematikasi tanish: har bir
darsning oxiridagi «Kalit soʻzlar» roʻyxati aynan shu oʻtish uchun
yozilgan edi. Siz inglizcha atamalarni bilmasdan yodlab
qoʻygansiz.</p>

<p>Agar shunchaki oʻqishni istasangiz — «Matematika olami» javoni
bor: al-Xorazmiy, Beruniy, Ulugʻbek, tabiatdagi
<span class="cn-word" data-tr="takrorlanadigan qonuniyat">namuna</span>lar,
jumboqlar.</p>

<p>Va yana bir yoʻl bor, u eng kam qadrlanadi:
<span class="cn-word" data-tr="oʻqilganni qaytadan koʻrib chiqish">qayta oʻqish</span>.
Ikkinchi marta oʻqilgan dars birinchisidan butunlay boshqacha
koʻrinadi — chunki endi siz undan keyingisini ham bilasiz.</p>

<p><b>Oxirgisi.</b> Yuz dars sizni tezroq hisoblaydigan qilgan
boʻlishi mumkin. Lekin men boshqa narsaga umid qilaman.</p>

<p>Umid qilamanki, endi siz
<span class="cn-word" data-tr="maʼlumotning chizmadagi koʻrinishi">diagramma</span>ga
qaraganda oʻqning qayerdan boshlanganini koʻrasiz. Reklamadagi «katta paket — tejamkor» degan
yozuvni oʻqiganda telefonni olib, narxni miqdorga boʻlasiz.
Kimdir «oʻrtacha maosh shuncha» deganda,
<span class="cn-word" data-tr="tartiblangan qatorning oʻrtasidagi son">mediana</span>ni
soʻraysiz.</p>

<p>Bu koʻnikmalar imtihon uchun emas. Ular hayot uchun — va ularni
yuzta darsdan olib chiqib ketish mumkin.</p>

<p>Yoʻlingiz ochiq boʻlsin.</p>

<p><i>Prime Math</i></p>
""",
    },
]
