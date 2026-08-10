# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-4 … PM-6.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 4 — kafedagi sahna (hikoya), 5 — sinfdagi bahs (dialog),
6 — mashgʻulotdagi reportaj (sport).

cn-word bu toʻplamda ATAMA: data-tr — oʻzbekcha qisqa taʼrif.
grammar bloki — matnda ishlatilgan QOIDA.
⚠️ Savollarning javob oʻrni qoʻlda aralashtiriladi (matn savollari
   saqlangan tartibda chiqadi, mashqlardan farqli oʻlaroq).

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_04_06.py --author=prime
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
    # PM-4 — qoldiqli boʻlish                 KAFEDAGI SAHNA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Oʻttiz yetti kishi, oltitadan stol",
        "summary": (
            "PM-4 matni. Sinf kafega bordi. Boʻlish toʻgʻri bajarildi, javob esa "
            "notoʻgʻri chiqdi — chunki qoldiqdagi bitta bola unutilgan edi."
        ),
        "order":   4,
        "grammar": [
            {
                "pattern":  "boʻlinma × boʻluvchi + qoldiq = boʻlinuvchi",
                "meaning":  "Qoldiqli boʻlishni tekshirish qoidasi. Qoldiq har doim "
                            "boʻluvchidan kichik boʻladi — aks holda yana bitta guruh "
                            "chiqar edi.",
                "examples": [
                    "37 ÷ 6 = 6 (qoldiq 1)",
                    "6 × 6 + 1 = 37 ✓",
                ],
            },
            {
                "pattern":  "«Kamida nechta kerak?» → qoldiq uchun yana bitta",
                "meaning":  "Masala hammani joylashtirishni talab qilsa, qoldiqni "
                            "tashlab boʻlmaydi: boʻlinmaga bitta qoʻshiladi.",
                "examples": ["6 toʻla stol + 1 bolaga stol = 7 ta stol"],
            },
        ],
        "questions": [
            {
                "text": "Sardorning hisobi toʻgʻri boʻlsa ham, javobi nega notoʻgʻri chiqdi?",
                "choices": [
                    "U 37 ni 6 ga notoʻgʻri boʻldi",
                    "U stollar sonini koʻpaytirib yubordi",
                    "U qoldiqdagi bitta bolani hisobga olmadi",
                    "U kafedagi stollar sonini bilmasdi",
                ],
                "answer": 2,
                "explanation": "37 ÷ 6 = 6 (qoldiq 1). Boʻlinma toʻgʻri, lekin qoldiqdagi "
                               "bola ham stolga muhtoj edi.",
            },
            {
                "text": "Hamma oʻtirishi uchun kamida nechta stol kerak?",
                "choices": ["6 ta", "7 ta", "8 ta", "37 ta"],
                "answer": 1,
                "explanation": "Oltita stol toʻladi (6 × 6 = 36), bitta bola qoladi. "
                               "Unga ham stol kerak: 6 + 1 = <b>7</b>.",
            },
            {
                "text": "Yettinchi stolda necha kishi oʻtiradi?",
                "choices": ["6", "5", "2", "1"],
                "answer": 3,
                "explanation": "Qoldiq 1 — demak oxirgi stolda atigi bitta bola "
                               "oʻtiradi. Bitta boʻlishdan uch xil javob chiqdi: 6, 7 "
                               "va 1.",
            },
        ],
        "body": """
<p>Nodira opa sinfni tushlikka kafega olib bordi. Bolalar oʻttiz yetti nafar edi.</p>

<p>Kafe eshigida ofitsiant kutib oldi.</p>

<p>— Bizda stollar olti kishilik, — dedi u. — Nechtasini tayyorlaymiz?</p>

<p>Sardor darrov hisobladi. U <span class="cn-word" data-tr="boʻlinayotgan son">boʻlinuvchi</span>
37 ni <span class="cn-word" data-tr="nechaga boʻlinayotgani">boʻluvchi</span> 6 ga boʻldi
va <strong>6</strong> deb javob berdi.</p>

<p>Bolalar oʻtira boshlashdi. Oltita stol toʻldi. Keyin Bekzod turgan joyida qoldi —
unga oʻrindiq yetmadi.</p>

<p>— Hisobing toʻgʻri edi, — dedi Nodira opa kulib. — Lekin sen
<span class="cn-word" data-tr="boʻlinmay ortib qolgan qism">qoldiq</span>ni unutding.</p>

<p>U qogʻozga yozdi: <strong>37 ÷ 6 = 6 (qoldiq 1)</strong>. Oltita stolda 36 bola
oʻtiribdi, bittasi esa hamon tik turibdi.</p>

<p>— Demak javob 6 emas, <strong>7</strong>, — dedi Afsona. — Bekzodga ham stol kerak.</p>

<p>Ofitsiant yettinchi stolni surdi. Bekzod yolgʻiz oʻzi oʻtirdi va hammani kulgi
bosdi.</p>

<p>Nodira opa <span class="cn-word" data-tr="boʻlish natijasi">boʻlinma</span>ni
<span class="cn-word" data-tr="javobni koʻpaytirish bilan qayta hisoblash">tekshirish</span>
usulini ham koʻrsatdi: 6 × 6 + 1 = 37. Hammasi joyida.</p>

<p>— Esda tutinglar, — dedi u. — Masala «kamida nechta kerak?» deb soʻrasa, qoldiq
uchun doim yana bitta qoʻshiladi. Bir savol — bir stol,
<span class="cn-word" data-tr="qoldiqsiz, ortmasdan boʻlinish">teng boʻlish</span> esa
har doim ham chiqavermaydi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-5 — amallar tartibi                  SINFDAGI BAHS (DIALOG)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bitta hisob, ikkita javob",
        "summary": (
            "PM-5 matni. Ikki oʻquvchi bitta ifodadan ikki xil javob chiqaradi. "
            "Kim haq? Bahs doʻkondagi haqiqiy hisob bilan hal boʻladi."
        ),
        "order":   5,
        "grammar": [
            {
                "pattern":  "qavslar → × va ÷ → + va −",
                "meaning":  "Amallar tartibi. Teng darajadagi amallar chapdan oʻngga "
                            "bajariladi. Shu tartib butun dunyoda bir xil — shuning "
                            "uchun bitta ifodaning bitta javobi boʻladi.",
                "examples": [
                    "2 + 3 × 4 = 2 + 12 = 14",
                    "(2 + 3) × 4 = 5 × 4 = 20",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sardor va Afsona nima ustida bahslashdi?",
                "choices": [
                    "Doskadagi misolni kim yechishi ustida",
                    "2 + 3 × 4 ifodasining javobi ustida",
                    "Kalkulyator kimniki ekani ustida",
                    "Doʻkonda nima olish kerakligi ustida",
                ],
                "answer": 1,
                "explanation": "Sardor 20, Afsona 14 dedi. Ikkalasi ham hisobni bilardi, "
                               "lekin tartibni turlicha qoʻlladi.",
            },
            {
                "text": "2 + 3 × 4 ifodasining toʻgʻri qiymati qancha?",
                "choices": ["9", "20", "14", "24"],
                "answer": 2,
                "explanation": "Avval koʻpaytirish: 3 × 4 = 12, keyin 2 + 12 = <b>14</b>. "
                               "20 — chapdan oʻngga hisoblaganda chiqadigan javob.",
            },
            {
                "text": "Matndagi doʻkon hisobi boʻyicha Afsona jami qancha toʻladi?",
                "choices": ["9 000 soʻm", "10 500 soʻm", "18 000 soʻm", "12 000 soʻm"],
                "answer": 3,
                "explanation": "2 × 3 000 + 4 × 1 500 = 6 000 + 6 000 = <b>12 000</b> "
                               "soʻm. Koʻpaytirishlar avval bajariladi, qavs kerak emas.",
            },
        ],
        "body": """
<p>Doskada bitta qator turardi: <strong>2 + 3 × 4</strong>.</p>

<p>— Yigirma, — dedi Sardor. — Ikkiga uchni qoʻshsang besh, beshni toʻrtga koʻpaytirsang
yigirma.</p>

<p>— Oʻn toʻrt, — dedi Afsona. — Avval koʻpaytirish bajariladi.</p>

<p>Ikkalasi ham qatʼiy turib oldi. Nodira opa aralashmadi, faqat bitta savol berdi:</p>

<p>— Afsona, kecha doʻkonda nima olding?</p>

<p>— Ikkita daftar, har biri uch ming soʻmdan. Va toʻrtta ruchka, har biri ming yarim
soʻmdan.</p>

<p>— Yaxshi. Kassir qanday hisobladi?</p>

<p>Afsona esladi: kassir avval daftarlarni — <strong>2 × 3 000 = 6 000</strong>, keyin
ruchkalarni — <strong>4 × 1 500 = 6 000</strong>, soʻng ikkita
<span class="cn-word" data-tr="koʻpaytirish natijasi">koʻpaytma</span>ni qoʻshdi. Chiqqan
<span class="cn-word" data-tr="qoʻshish natijasi">yigʻindi</span> — <strong>12 000</strong>
soʻm.</p>

<p>— Mana, — dedi opa. — Har bir koʻpaytirish
<span class="cn-word" data-tr="sonlar va amallardan tuzilgan yozuv">ifoda</span>da bitta
<em>butun narsani</em> bildiradi: daftarlar puli, ruchkalar puli. Shuning uchun ular
avval hisoblanadi. Bu —
<span class="cn-word" data-tr="qaysi amal oldin bajarilishi haqidagi qoida">amallar tartibi</span>,
va u butun dunyoda bir xil.</p>

<p>— Unda men xatomi? — soʻradi Sardor.</p>

<p>— Sening hisobing <span class="cn-word" data-tr="&quot;avval buni hisobla&quot; degan belgi">qavs</span>
qoʻyilgan ifodaning javobi: (2 + 3) × 4 = 20. Faqat doskada qavs yoʻq edi.</p>

<p>— Koʻpaytirish va boʻlish
<span class="cn-word" data-tr="bir xil navbatdagi, biri ikkinchisidan ustun boʻlmagan amallar">teng darajali amallar</span>,
— qoʻshimcha qildi opa. — Ular uchrashsa, chapdagisi birinchi bajariladi.</p>

<p>Sardor telefonini olib tekshirdi. Oddiy kalkulyator 20 ni koʻrsatdi, muhandislik
rejimi esa 14 ni. Ikkita turli
<span class="cn-word" data-tr="ifodani hisoblab chiqqan son">qiymat</span>, bitta
ifodadan.</p>

<p>— Kalkulyator ham adashadimi? — hayron boʻldi u.</p>

<p>— Yoʻq, u sendan boshqacha oʻqiydi, — dedi opa. — Shuning uchun uzun hisobni
kiritishdan oldin qavsni oʻzing qoʻyasan.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-6 — boʻlinish alomatlari             MASHGʻULOTDA (SPORT)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Guruhlarga boʻlinamiz",
        "summary": (
            "PM-6 matni. Murabbiy 84 bolani teng jamoalarga ajratadi va bitta ham "
            "boʻlish qilmaydi — boʻlinish alomatlari uning oʻrniga ishlaydi."
        ),
        "order":   6,
        "grammar": [
            {
                "pattern":  "6 ga boʻlinadi = 2 ga ham, 3 ga ham boʻlinadi",
                "meaning":  "Oltiga boʻlinish uchun ikkala shart ham kerak: son juft "
                            "boʻlsin va raqamlar yigʻindisi 3 ga boʻlinsin.",
                "examples": [
                    "84: juft ✓, 8 + 4 = 12 uchga boʻlinadi ✓ → 6 ga boʻlinadi",
                    "84 ÷ 6 = 14",
                ],
            },
            {
                "pattern":  "5 ga boʻlinish: oxirgi raqam 0 yoki 5",
                "meaning":  "Faqat oxirgi raqamga qaraladi. 3 va 9 uchun esa raqamlar "
                            "yigʻindisiga qaraladi.",
                "examples": ["84 → oxirgi raqam 4 → 5 ga boʻlinmaydi"],
            },
        ],
        "questions": [
            {
                "text": "Murabbiy nega hisob-kitob qilib oʻtirmadi?",
                "choices": [
                    "U javobni oldindan bilardi",
                    "U boʻlinish alomatlaridan foydalandi",
                    "Unga bolalar aytib yubordi",
                    "U kalkulyatordan foydalandi",
                ],
                "answer": 1,
                "explanation": "Alomat songa bir qarab «boʻlinadimi yoki yoʻqmi?» degan "
                               "savolga javob beradi — boʻlish shart emas.",
            },
            {
                "text": "84 bola 6 tadan boʻlinsa, nechta jamoa chiqadi?",
                "choices": ["12 ta", "13 ta", "14 ta", "16 ta"],
                "answer": 2,
                "explanation": "84 ÷ 6 = <b>14</b>. Tekshirish: 6 × 14 = 84 ✓ — hech kim "
                               "ortib qolmaydi.",
            },
            {
                "text": "Nega 84 bolani 5 tadan qilib teng ajratib boʻlmaydi?",
                "choices": [
                    "Chunki oxirgi raqami 0 ham, 5 ham emas",
                    "Chunki 84 juft son",
                    "Chunki raqamlar yigʻindisi 12",
                    "Chunki 84 juda katta son",
                ],
                "answer": 0,
                "explanation": "5 ga boʻlinish alomati faqat oxirgi raqamga qaraydi. "
                               "84 ÷ 5 = 16, qoldiq 4 — toʻrt bola jamoasiz qolardi.",
            },
        ],
        "body": """
<p>Shanba kuni maktab sport zalida oʻyin boshlanishi kerak edi. Murabbiy Karim aka
roʻyxatga qaradi: bugun mashgʻulotga <strong>84</strong> bola kelgan.</p>

<p>— Beshtadan jamoa qilaylik! — deb qichqirdi kimdir.</p>

<p>Karim aka roʻyxatdan koʻzini uzmay javob berdi:</p>

<p>— Beshtadan chiqmaydi. Oltitadan qilamiz.</p>

<p>Bolalar hayron boʻlishdi: u hech narsa hisoblamagan edi-ku. Sirni Karim aka oʻzi
ochdi.</p>

<p>— Songa qarab turib bilsa boʻladi. Bu
<span class="cn-word" data-tr="boʻlmasdan turib boʻlinishini aniqlash usuli">boʻlinish alomati</span>
deyiladi.</p>

<p>Beshtadan boʻlish uchun sonning oxirgi raqami 0 yoki 5 boʻlishi kerak. 84 ning oxirgi
raqami — 4. Demak beshtadan
<span class="cn-word" data-tr="qoldiqsiz, hech kim ortmasdan">teng</span> chiqmaydi:
toʻrt bola jamoasiz qolardi.</p>

<p>Oltitaga esa ikkita shart kerak. Birinchisi: son
<span class="cn-word" data-tr="2 ga boʻlinadigan son">juft</span> boʻlsin — 84 juft.
Ikkinchisi: <span class="cn-word" data-tr="sondagi raqamlarni qoʻshib chiqish">raqamlar yigʻindisi</span>
uchga boʻlinsin — 8 + 4 = 12, boʻlinadi. Ikkala shart bajarildi.</p>

<p>— Endi hisoblaymiz, — dedi Karim aka. — <strong>84 ÷ 6 = 14</strong>. Oʻn toʻrtta
jamoa.</p>

<p>Bolalar saf tortdi. Haqiqatan ham hech kim ortib qolmadi.</p>

<p>— Alomat «boʻlinadimi?» degan savolga javob beradi, — qoʻshib qoʻydi murabbiy. —
«Nechta chiqadi?» degan savolga esa baribir boʻlish kerak. Lekin kerakmi yoki
yoʻqmi — buni bir soniyada bilib olasan.</p>

<p>Oʻsha kuni Bekzod uyga qaytayotib avtobus raqamiga qaradi va ovoz chiqarib dedi:
«Yigirma yetti. Toq. Uchga boʻlinadi, toʻqqizga ham».
<span class="cn-word" data-tr="berilgan songa qoldiqsiz boʻlinadigan son">Karrali</span>
sonlarni koʻrish odati shu kundan boshlandi.</p>
""",
    },
]
