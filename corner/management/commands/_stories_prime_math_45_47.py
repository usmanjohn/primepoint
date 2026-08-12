# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-45, PM-46, PM-47. BLOK D BOSHI.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 45 — tarix (dengizda uzunlik masalasi), 46 — hikoya (uchrashuv joyi),
47 — ilmiy-ommabop (funksiya-mashina). Oldingi ikkitasi (43, 44) hikoya edi,
shuning uchun batch tarix bilan boshlanadi — uchta bir xil shakl ketma-ket
kelmaydi.

⚠️ Kumulyativ: qiya masofa hisoblanmaydi (Pifagor — PM-64); grafik yoʻq
   (PM-48 dan). 45-matndagi tarixiy faktlar haqiqiy: 1707 yilgi Silli
   halokati, 1714 yilgi mukofot toʻgʻrisidagi qonun, Jon Xarrisonning
   dengiz soati, Dekartning 1637 yilgi ishi.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_45_47.py --author=prime
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
    # PM-45 — koordinata tekisligi                              TARIX
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Kemadagi manzil — xarita katakchalari",
        "summary": (
            "PM-45 matni. Tarixiy epizod: 1707 yilda Britaniya kemalari oʻz "
            "oʻrnini bilmagani uchun halok boʻldi. Dengizda ham, xaritada ham "
            "manzil ikkita sondan iborat — bittasi yetmaydi."
        ),
        "order":   45,
        "grammar": [
            {
                "pattern":  "A(x; y) — nuqtaning manzili",
                "meaning":  "Tekislikdagi har bir nuqta ikkita son bilan "
                            "aniqlanadi: avval abssissa (gorizontal), keyin "
                            "ordinata (vertikal). Tartib muhim.",
                "examples": [
                    "(−4; 3) — chapda va yuqorida, yaʼni II chorakda",
                    "(2; −3) dan (2; 4) gacha: |4 − (−3)| = 7 katak",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega kemalar oʻz oʻrnini aniq bilmasdi?",
                "choices": [
                    "Uzunlikni aniqlash uchun juda aniq soat kerak edi, u esa "
                    "yoʻq edi",
                    "Xaritalar hali chizilmagan edi",
                    "Kenglikni oʻlchashni bilishmasdi",
                    "Kemalarda kompas yoʻq edi",
                ],
                "answer": 0,
                "explanation": "Kenglikni quyosh va yulduzlarga qarab oʻlchash "
                               "mumkin edi, uzunlik esa vaqtga bogʻliq edi. Aniq "
                               "dengiz soati boʻlmagani uchun ikkinchi son "
                               "taxminiy qolardi.",
            },
            {
                "text": "Xaritada kemaning oʻrni (−4; 3) deb yozilgan. Bu qaysi "
                        "chorak?",
                "choices": ["I", "II", "III", "IV"],
                "answer": 1,
                "explanation": "Abssissa manfiy — kema chapda; ordinata musbat — "
                               "yuqorida. Chap yuqori burchak II chorak boʻladi.",
            },
            {
                "text": "Kema (2; −3) nuqtadan (2; 4) nuqtaga koʻchdi. Har katak "
                        "10 km boʻlsa, u necha kilometr siljidi?",
                "choices": ["7 km", "20 km", "70 km", "100 km"],
                "answer": 2,
                "explanation": "Abssissa oʻzgarmadi, demak harakat vertikal: "
                               "|4 − (−3)| = 7 katak. 7 × 10 = 70 km. "
                               "«7 km» — katakni kilometr deb olgan javob.",
            },
        ],
        "body": """
<p>1707 yilning kuzida Britaniya harbiy floti Oʻrta yer dengizidan uyiga qaytardi.
Tunda, quyuq tumanda, kemalar Angliyaning janubi-gʻarbidagi Silli orollari
qoyalariga urildi. Toʻrtta kema choʻkdi. Mingdan ortiq dengizchi halok boʻldi.</p>

<p>Sabab jangda ham, boʻronda ham emas edi. Kemalar oʻz oʻrnini bilmasdi.</p>

<p>Dengizda manzil ikkita sondan iborat. Birinchisi —
<span class="cn-word" data-tr="nuqtaning ekvatordan shimol yoki janubga uzoqligi">kenglik</span>,
ikkinchisi — <span class="cn-word" data-tr="nuqtaning boshlangʻich meridiandan sharq yoki gʻarbga uzoqligi">uzunlik</span>.
Kenglikni oʻlchash oson edi: quyoshning yoki Qutb yulduzining balandligiga qarab
topilardi. Uzunlik esa vaqtga bogʻliq edi, dengizda toʻgʻri yuradigan soat esa hali
yoʻq edi.</p>

<p>Shunday qilib, bitta <span class="cn-word" data-tr="nuqtaning oʻrnini koʻrsatuvchi son">koordinata</span>
aniq, ikkinchisi taxminiy boʻlardi. Kema xaritada nuqta emas, butun bir chiziq
boʻylab «yoʻqolgan» hisoblanardi.</p>

<p>1714 yilda parlament bu masalani yechgan odamga katta mukofot eʼlon qildi.
Mukofotni duradgor Jon Xarrison yasagan
<span class="cn-word" data-tr="dengizda vaqtni juda aniq koʻrsatadigan soat">dengiz soati</span>
oldi — uning ustida yigirma yildan koʻproq ishlangan edi.</p>

<p>Qizigʻi shundaki, oʻsha yillarda matematiklar ham xuddi shu fikrga kelishgandi.
1637 yilda Rene Dekart tekislikdagi har bir nuqtani
<span class="cn-word" data-tr="tartibi muhim boʻlgan ikki son: (x; y)">tartiblangan juftlik</span>
bilan belgilash mumkinligini yozib qoldirgan edi.</p>

<p>Bugungi mashq xaritalarida ham shunday: kemaning oʻrni <strong>(−4; 3)</strong>
deb yoziladi. Birinchi son —
<span class="cn-word" data-tr="birinchi koordinata, gorizontal yoʻnalish">abssissa</span>,
ikkinchisi — <span class="cn-word" data-tr="ikkinchi koordinata, vertikal yoʻnalish">ordinata</span>.
Ishoralar esa <span class="cn-word" data-tr="koordinata oʻqlari ajratgan toʻrt sohadan biri">chorak</span>ni
aytib beradi: chapda va yuqorida — II chorak.</p>

<p>Agar har katak 10 km boʻlsa va kema <strong>(2; −3)</strong> dan
<strong>(2; 4)</strong> ga oʻtsa, uning
<span class="cn-word" data-tr="ikki nuqta orasidagi uzunlik">masofa</span>si
yetti katak, yaʼni <strong>70 kilometr</strong> boʻladi —
<span class="cn-word" data-tr="tik, pastdan yuqoriga">vertikal</span> yoʻnalishda.</p>

<p>Dengizchilar buni juda qimmatga tushunishdi: bitta son yetmaydi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-46 — masofa va oʻrta nuqta                             HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ikki uy orasidagi yoʻl",
        "summary": (
            "PM-46 matni. Hikoya: Afsona bilan Dilnoza «oʻrtada uchrashaylik» "
            "deb kelishadi, keyin oʻrtasi qayerdaligini xaritadagi "
            "koordinatalardan hisoblab topishadi."
        ),
        "order":   46,
        "grammar": [
            {
                "pattern":  "masofa = |x₂ − x₁|",
                "meaning":  "Gorizontal kesmaning uzunligi — abssissalar "
                            "ayirmasining moduli. Masofa hech qachon manfiy "
                            "boʻlmaydi.",
                "examples": [
                    "|5 − (−3)| = |5 + 3| = 8 katak",
                    "8 × 150 = 1200 metr",
                ],
            },
            {
                "pattern":  "oʻrta = (x₁ + x₂) ÷ 2",
                "meaning":  "Kesmaning oʻrtasi — koordinatalarning yarim "
                            "yigʻindisi. Ayirma emas, aynan yigʻindi olinadi.",
                "examples": [
                    "(−3 + 5) ÷ 2 = 1 → uchrashuv nuqtasi (1; 4)",
                    "Tekshirish: 1 − (−3) = 4 va 5 − 1 = 4",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega qizlar aynan (1; 4) nuqtasini tanlashdi?",
                "choices": [
                    "U Afsonaning uyiga yaqinroq edi",
                    "U ikkala uydan ham teng uzoqlikda edi",
                    "U maktabning yonida edi",
                    "Boshqa yoʻl yoʻq edi",
                ],
                "answer": 1,
                "explanation": "Ular teng yurishga kelishishdi, shuning uchun "
                               "uchrashuv joyi kesmaning oʻrtasi boʻlishi kerak "
                               "edi: har biriga 4 katakdan.",
            },
            {
                "text": "Afsona bilan Dilnozaning uylari orasi necha metr?",
                "choices": ["600 metr", "900 metr", "1200 metr", "1500 metr"],
                "answer": 2,
                "explanation": "|5 − (−3)| = 8 katak, har katak 150 metr: "
                               "8 × 150 = 1200 metr. «600 metr» — bu bitta "
                               "qizning yoʻli, ikkovining orasi emas.",
            },
            {
                "text": "Jasur kutubxonagacha necha metr yuradi?",
                "choices": ["450 metr", "600 metr", "750 metr", "900 metr"],
                "answer": 3,
                "explanation": "Uning abssissasi ham 1, demak yoʻl vertikal: "
                               "|4 − (−2)| = 6 katak. 6 × 150 = 900 metr.",
            },
        ],
        "body": """
<p>Afsona bilan Dilnoza shanba kuni uchrashmoqchi boʻlishdi.</p>

<p>— Menikiga kel, — dedi Dilnoza.</p>

<p>— Yoʻq, oʻrtada uchrashaylik, — dedi Afsona. — Shunda ikkalamiz ham teng
yuramiz.</p>

<p>Gap oson edi, lekin qayeri oʻrtasi ekanini hech biri bilmasdi. Afsona
telefondagi xaritani ochdi. Shahar koʻchalari katak boʻlib joylashgan edi, har
bir katakning tomoni <strong>150 metr</strong>.</p>

<p>U maktabni <span class="cn-word" data-tr="oʻqlar kesishgan nuqta, O(0; 0)">koordinata boshi</span>
qilib oldi. Shunda oʻzining uyi <strong>(−3; 4)</strong>, Dilnozaniki esa
<strong>(5; 4)</strong> nuqtaga tushdi.</p>

<p>— Ikkalamizning <span class="cn-word" data-tr="ikkinchi koordinata, vertikal yoʻnalish">ordinata</span>miz
bir xil, — dedi Afsona. — Toʻrt. Demak bitta koʻchada yashar ekanmiz.</p>

<p>Uylar orasidagi <span class="cn-word" data-tr="ikki nuqta orasidagi uzunlik">masofa</span>ni
u <span class="cn-word" data-tr="birinchi koordinata, gorizontal yoʻnalish">abssissa</span>lardan
hisobladi. Manfiy son bor edi, shuning uchun ayirmaning
<span class="cn-word" data-tr="sonning noldan uzoqligi, |a|">modul</span>ini oldi:
|5 − (−3)| = <strong>8</strong> katak, yaʼni 1200 metr.</p>

<p>— Endi <span class="cn-word" data-tr="uchlardan teng uzoqlikdagi nuqta">kesmaning oʻrtasi</span>ni
topamiz, — dedi Afsona.</p>

<p>Buning uchun ayirma emas,
<span class="cn-word" data-tr="ikki sonning yigʻindisining yarmi">yarim yigʻindi</span>
kerak edi: (−3 + 5) ÷ 2 = <strong>1</strong>. Ordinata oʻzgarmadi. Uchrashuv
nuqtasi — <strong>(1; 4)</strong>.</p>

<p>Afsona xaritani kattalashtirdi. Oʻsha nuqtada tuman kutubxonasi turardi.</p>

<p>— Toʻrt katakdan, — dedi u. — Har birimizga <strong>600 metr</strong>.</p>

<p>Kechqurun ular Jasurni ham chaqirishdi. Uning uyi <strong>(1; −2)</strong> da
edi.</p>

<p>— Mening abssissam ham bir, — dedi Jasur xaritaga qarab. — Demak menga
<span class="cn-word" data-tr="tik, pastdan yuqoriga">vertikal</span> yoʻl:
|4 − (−2)| = 6 katak. Toʻqqiz yuz metr. Sizlarnikidan koʻp!</p>

<p>— Lekin sen kutubxonaga eng yaqin yashaysan, — dedi Afsona. — Bizga shanba
kerak, senga esa har kuni ochiq.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-47 — funksiya gʻoyasi                        ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Mashina qanday ishlaydi: kirish va chiqish",
        "summary": (
            "PM-47 matni. Ilmiy-ommabop: suv avtomati, pochta tarifi va sinf "
            "roʻyxati misolida funksiya nima ekani — va nega har bir kirishga "
            "faqat bitta chiqish toʻgʻri kelishi kerak."
        ),
        "order":   47,
        "grammar": [
            {
                "pattern":  "N(x) = 6 000 + 4 000x",
                "meaning":  "Funksiya — kirish → qoida → chiqish. Bu yerda kirish "
                            "ogʻirlik (kg), chiqish narx (soʻm); 6 000 — har "
                            "qanday joʻnatmaga qoʻyiladigan oʻzgarmas had.",
                "examples": [
                    "N(3) = 6 000 + 12 000 = 18 000 soʻm",
                    "Teskari savol: 30 000 − 6 000 = 24 000; 24 000 ÷ 4 000 = 6 kg",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega «har bir yilga oʻsha yili tugʻilgan oʻquvchi» "
                        "qoidasi funksiya emas?",
                "choices": [
                    "Chunki bitta kirishga bir nechta javob toʻgʻri keladi",
                    "Chunki yillar juda katta sonlar",
                    "Chunki oʻquvchilar soni oʻzgarib turadi",
                    "Chunki javobni hisoblab boʻlmaydi",
                ],
                "answer": 0,
                "explanation": "Funksiyaning yagona sharti — har bir kirishga "
                               "faqat bitta chiqish. Bitta yilga oʻnlab oʻquvchi "
                               "toʻgʻri kelsa, mashina ishonchsiz boʻladi.",
            },
            {
                "text": "Besh kilogrammlik quti necha soʻm turadi?",
                "choices": [
                    "18 000 soʻm", "22 000 soʻm", "26 000 soʻm", "30 000 soʻm",
                ],
                "answer": 2,
                "explanation": "N(5) = 6 000 + 4 000 × 5 = 6 000 + 20 000 = "
                               "26 000 soʻm. «20 000 soʻm»ga oʻxshash javoblar "
                               "oʻzgarmas 6 000 ni qoʻshishni unutadi.",
            },
            {
                "text": "Bekzod 22 000 soʻm toʻladi. Uning qutisi necha kilogramm "
                        "edi?",
                "choices": ["3 kg", "4 kg", "5 kg", "5,5 kg"],
                "answer": 1,
                "explanation": "Avval oʻzgarmas haq ayiriladi: 22 000 − 6 000 = "
                               "16 000. Keyin 16 000 ÷ 4 000 = 4 kg. Tekshirish: "
                               "6 000 + 16 000 = 22 000 ✓",
            },
        ],
        "body": """
<p>Suv avtomatiga tanga tashlaysiz — stakan toʻladi. Yana tashlaysiz — yana
toʻladi. Har safar bir xil. Agar bir kuni oʻsha tangaga yarim stakan tushsa, siz
avtomatni buzilgan deysiz va boshqa yoniga bormaysiz.</p>

<p>Mana shu «buzilmagan» degan talab matematikada nom olgan. U
<span class="cn-word" data-tr="har bir kirishga faqat bitta chiqish beruvchi qoida">funksiya</span>
deyiladi.</p>

<p>Atrofimizda bunday mashinalar juda koʻp, faqat biz ularni shunday atamaymiz.</p>

<p>Pochta boʻlimini olaylik. Har bir joʻnatma uchun 6 000 soʻm olinadi, ustiga har
kilogramm uchun 4 000 soʻm qoʻshiladi.
<span class="cn-word" data-tr="funksiyaga kiritiladigan son">Kirish</span> — qutining
ogʻirligi, <span class="cn-word" data-tr="funksiya qaytaradigan son">chiqish</span>
— narx. <span class="cn-word" data-tr="kirishdan chiqishga oʻtish usuli">Qoida</span>si
esa bitta <span class="cn-word" data-tr="harflar bilan yozilgan umumiy qoida">formula</span>ga
sigʻadi:</p>

<p><strong>N(x) = 6 000 + 4 000x</strong></p>

<p>Bu yerda <span class="cn-word" data-tr="qiymati oʻzgarib turadigan harf">oʻzgaruvchi</span>
x — kilogramm soni; uni funksiyaning
<span class="cn-word" data-tr="funksiyaga kiritilgan son, x">argument</span>i ham
deyishadi. Uch kilogrammlik quti uchun:
<strong>6 000 + 4 000 × 3 = 18 000</strong> soʻm. Bu yozuvni qisqacha
<strong>N(3) = 18 000</strong> deb ham yozishadi — «uch kiritilsa, oʻn sakkiz ming
chiqadi» degani. Oʻn sakkiz ming — bu
<span class="cn-word" data-tr="funksiyaning berilgan kirishdagi chiqishi, f(x)">funksiyaning qiymati</span>.</p>

<p>Bunda 6 000 — <span class="cn-word" data-tr="kirishga bogʻliq boʻlmagan qism">oʻzgarmas had</span>:
quti yengil boʻlsa ham, ogʻir boʻlsa ham u oʻzgarmaydi.</p>

<p>Xuddi shu qoida teskari savolga ham javob beradi. Nodira opa 30 000 soʻm
toʻladi — qutisi necha kilogramm edi? Avval oʻzgarmas haqni ayiramiz:
30 000 − 6 000 = 24 000. Keyin qolganini bir kilogrammning narxiga boʻlamiz:
24 000 ÷ 4 000 = <strong>6</strong> kilogramm. Tekshirish oson —
6 000 + 24 000 = 30 000 ✓</p>

<p>Lekin har qanday qoida ham funksiya boʻlavermaydi. «Har bir oʻquvchiga uning
tugʻilgan yili» — funksiya, chunki javob bitta. «Har bir yilga oʻsha yili
tugʻilgan oʻquvchi» — funksiya emas, chunki bitta yilga oʻnlab ism toʻgʻri
keladi.</p>

<p>Shuning uchun matematika funksiyani shunchaki qoida deb emas, <b>ishonchli</b>
qoida deb taʼriflaydi. Ishonchsiz avtomatdan hech kim suv sotib olmaydi.</p>
""",
    },
]
