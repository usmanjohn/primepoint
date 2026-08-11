# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-28 … PM-30.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 28 — sayohat qaydlari, 29 — jumboq (sinfdagi topishmoq),
30 — ilmiy-ommabop (taksi hisobi).

⚠️ Kumulyativ: 28-matnda harf yoʻq (u PM-29 da kiritiladi). 29 va 30-matnlarda
   tenglama yechilmaydi — nomaʼlum sinab koʻrish yoʻli bilan topiladi
   (tenglama PM-36 da).

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_28_30.py --author=prime
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
    # PM-28 — masshtab                                SAYOHAT QAYDLARI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Xaritadagi ikki santimetr",
        "summary": (
            "PM-28 matni. Sayohat qaydlari: Bekzod qogʻoz xarita bilan yoʻlni "
            "oʻlchaydi, masshtabni kilometrga aylantiradi va tezlik tushganda "
            "vaqt qanday oʻzgarishini hisoblaydi."
        ),
        "order":   28,
        "grammar": [
            {
                "pattern":  "Masshtab: 1 : n — xaritadagi 1 sm = n sm yerda",
                "meaning":  "Masshtabdagi son santimetrni bildiradi. Kilometrga "
                            "oʻtish uchun 100 000 ga boʻlamiz. Tezlik va vaqt esa "
                            "teskari proporsional: ularning koʻpaytmasi — yoʻl — "
                            "oʻzgarmaydi.",
                "examples": [
                    "1 : 1 000 000 → 1 sm = 1 000 000 sm = 10 km; 28 sm = 280 km",
                    "280 ÷ 80 = 3,5 soat; 280 ÷ 70 = 4 soat",
                ],
            },
        ],
        "questions": [
            {
                "text": "Bekzod nima uchun qogʻoz xaritani ochdi?",
                "choices": [
                    "Telefon aloqasi yoʻqolgani uchun",
                    "Xaritani otasi sovgʻa qilgani uchun",
                    "Yoʻlning uzunligini oʻzi hisoblamoqchi boʻlgani uchun",
                    "Mashina yoʻldan adashgani uchun",
                ],
                "answer": 2,
                "explanation": "Bekzod navigator aytgan sonni oʻzi tekshirib koʻrmoqchi "
                               "boʻldi — shuning uchun xaritani oʻlchadi.",
            },
            {
                "text": "Masshtab 1 : 1 000 000 boʻlsa, xaritadagi 1 santimetr yerda "
                        "necha kilometr?",
                "choices": ["1 km", "10 km", "100 km", "1000 km"],
                "answer": 1,
                "explanation": "1 000 000 sm = 10 000 m = 10 km. Masshtabdagi son "
                               "har doim santimetrda beriladi.",
            },
            {
                "text": "280 kilometr yoʻlni 70 km/soat tezlikda bosib oʻtish necha "
                        "soat oladi?",
                "choices": ["3 soat", "3,5 soat", "4 soat", "4,5 soat"],
                "answer": 2,
                "explanation": "280 ÷ 70 = 4 soat. Tezlik 80 dan 70 ga tushgani uchun "
                               "vaqt 3,5 soatdan 4 soatga chiqdi — teskari "
                               "proporsionallik.",
            },
        ],
        "body": """
<p><b>Yakshanba, ertalab soat sakkiz.</b></p>

<p>Toshkentdan Samarqandga yoʻlga chiqdik. Navigator «280 kilometr» deb koʻrsatdi.
Men bu sonni oʻzim tekshirib koʻrmoqchi boʻldim va bardachokdan otamning eski qogʻoz
xaritasini oldim.</p>

<p>Xaritaning pastida kichkina yozuv bor edi:
<span class="cn-word" data-tr="xaritadagi va haqiqiy uzunlik nisbati">masshtab</span>
<strong>1 : 1 000 000</strong>. Demak xaritadagi har santimetr yerdagi bir million
santimetrga toʻgʻri keladi. Buni boshqa <span class="cn-word" data-tr="uzunlik oʻlchovi: sm, m, km">oʻlchov birligi</span>ga aylantirdim:
1 000 000 sm = 10 000 m = <strong>10 km</strong>.</p>

<p>Chizgʻich bilan ikki shahar orasidagi <span class="cn-word" data-tr="ikki nuqta orasidagi uzunlik">masofa</span>ni oʻlchadim — <strong>28 santimetr</strong>
chiqdi. Demak yoʻl <strong>28 × 10 = 280 km</strong>. Navigator haq ekan.</p>

<p>Otam soatiga 80 kilometr tezlik bilan haydadi. Yoʻlni tezlikka boʻlib <span class="cn-word" data-tr="harakat davom etadigan muddat">vaqt</span>ni hisobladim:
<strong>280 ÷ 80 = 3,5 soat</strong>.</p>

<p>Tushdan keyin havo buzildi va otam <strong>70</strong> kilometrga tushdi. Yangi
hisob: <strong>280 ÷ 70 = 4 soat</strong>. Yarim soat koʻpaydi.</p>

<p>Shunda bir narsani payqadim.
<span class="cn-word" data-tr="bir soatda bosib oʻtiladigan yoʻl">Tezlik</span> va
vaqt <span class="cn-word" data-tr="biri oshsa, ikkinchisi kamayadigan bogʻlanish">teskari proporsional</span>
ekan: biri kamaysa, ikkinchisi ortadi. Lekin ularning
<span class="cn-word" data-tr="koʻpaytirish natijasi">koʻpaytma</span>si oʻzgarmaydi —
80 × 3,5 ham, 70 × 4 ham 280 beradi. Yoʻlning uzunligi esa oʻsha-oʻsha.</p>

<p>Samarqandga soat oʻn ikkida yetib keldik. Xaritani qaytarib qoʻyarkanman, oʻyladim:
bu qogʻozning quvvati tugamaydi va unga aloqa ham kerak emas.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-29 — nomaʼlum va oʻzgaruvchi                          JUMBOQ
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "X kim? — sinfdagi topishmoq",
        "summary": (
            "PM-29 matni. Jumboq: Nodira opa doskaga bitta harf yozadi va sinf "
            "uni topishga urinadi. Harf nima uchun kerakligi shu oʻyin ichida "
            "tushunarli boʻladi."
        ),
        "order":   29,
        "grammar": [
            {
                "pattern":  "Harf — sonning oʻrnida turuvchi nom",
                "meaning":  "Nomaʼlum sonni harf bilan belgilab, u haqidagi gapni "
                            "yozuvga aylantiramiz. Keyin harf oʻrniga son qoʻyib "
                            "sinab koʻrsak, qaysi qiymat toʻgʻri kelishi maʼlum "
                            "boʻladi.",
                "examples": [
                    "n — partalar soni; har partada 2 kishi → 2n oʻquvchi",
                    "n = 10 → 20; n = 12 → 24 ✓ (sinfda 24 oʻquvchi bor)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nodira opa doskaga nima yozdi?",
                "choices": [
                    "Sinfdagi oʻquvchilar sonini",
                    "Bitta harf — sirli sonning nomini",
                    "Uy vazifasining javobini",
                    "Partalarning chizmasini",
                ],
                "answer": 1,
                "explanation": "U bitta harf yozdi va uni «sirli son» deb atadi. "
                               "Sinf oʻsha harf nimaga tengligini topishi kerak edi.",
            },
            {
                "text": "Har partada 2 kishi oʻtirsa, n ta partada nechta oʻquvchi "
                        "boʻladi?",
                "choices": ["n + 2", "2n", "n/2", "n − 2"],
                "answer": 1,
                "explanation": "Har partada 2 tadan, partalar n ta — koʻpaytirish: "
                               "2n. Bu yozuv har qanday sinf uchun ishlaydi.",
            },
            {
                "text": "Sinfda 24 oʻquvchi bor. Unda partalar nechta?",
                "choices": ["10 ta", "11 ta", "12 ta", "24 ta"],
                "answer": 2,
                "explanation": "2n = 24 boʻlishi kerak. n = 10 boʻlsa 20 chiqadi — kam; "
                               "n = 12 boʻlsa 24 chiqadi ✓ Demak partalar 12 ta.",
            },
        ],
        "body": """
<p>Nodira opa doskaga bitta harf yozdi va sinfga qaradi.</p>

<p>— Bugun bizda sirli son bor, — dedi u. — Uning nomi <strong>n</strong>. Kim
topsa, uy vazifasidan ozod.</p>

<p>Sinf jonlandi. Sherbek qoʻl koʻtardi:</p>

<p>— Bu qanaqasi? Harf-ku, son emas.</p>

<p>— Toʻgʻri, — dedi Nodira opa. — <span class="cn-word" data-tr="sonning oʻrnida turuvchi nom">Harf</span>
sonning <b>oʻrnida</b> turibdi. Biz uni hali bilmaymiz, shuning uchun unga nom berdik.
Bunday songa <span class="cn-word" data-tr="qiymati bitta, lekin bizga maʼlum boʻlmagan son">nomaʼlum</span>
deyiladi. Agar u har safar boshqacha boʻlsa, <span class="cn-word" data-tr="qiymati oʻzgarib turadigan miqdor">oʻzgaruvchi</span> deyiladi.</p>

<p>— Birinchi maslahat, — davom etdi u. — <b>n</b> — sinfimizdagi partalar soni. Har
partada ikki kishidan oʻtiramiz. Sinfdagi oʻquvchilar sonini qanday yozamiz?</p>

<p>Afsona javob berdi:</p>

<p>— Har partada 2 tadan, partalar n ta. Demak <strong>2n</strong>.</p>

<p>— Ana shu — <span class="cn-word" data-tr="harf, son va amallardan tuzilgan yozuv">ifoda</span>, —
dedi Nodira opa. — Endi ikkinchi maslahat: sinfimizda 24 oʻquvchi bor.</p>

<p>Jasur harf oʻrniga son qoʻyib <span class="cn-word" data-tr="mumkin boʻlgan qiymatlarni birma-bir tekshirish">sinab koʻrish</span>ni boshladi. n = 10 boʻlsa, 2 × 10 = 20 — kam.
n = 11 boʻlsa, 22 — yana kam. n = <strong>12</strong> boʻlsa,
<strong>2 × 12 = 24</strong> ✓</p>

<p>— Oʻn ikkita parta! — deb qichqirdi u.</p>

<p>— Barakalla, — dedi Nodira opa. — Topgan soning n ning <span class="cn-word" data-tr="harf oʻrnida turgan aniq son">qiymat</span>i boʻladi. — Endi eng muhim savol: nega harf kerak boʻldi?</p>

<p>Sinf jim qoldi. Afsona sekin javob berdi:</p>

<p>— Chunki javobni bilmasdan turib ham u haqda <b>gapirish</b> mumkin ekan.</p>

<p>Nodira opa jilmaydi. <span class="cn-word" data-tr="sonlar oʻrniga harflar bilan ish koʻradigan matematika boʻlimi">Algebra</span> shu yerdan boshlanadi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-30 — ifoda tuzish                             ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Taksi hisobi",
        "summary": (
            "PM-30 matni. Ilmiy-ommabop: ikki taksi tarifi ifodaga aylantiriladi "
            "va qaysi biri arzon ekani masofaga bogʻliqligi jadval bilan "
            "koʻrsatiladi."
        ),
        "order":   30,
        "grammar": [
            {
                "pattern":  "Tarif = oʻzgarmas qism + oʻzgaruvchiga bogʻliq qism",
                "meaning":  "Gapdagi «bir marta olinadigan» summa ozod had boʻladi, "
                            "«har bir birlik uchun» olinadigani esa oʻzgaruvchiga "
                            "koʻpaytiriladi.",
                "examples": [
                    "«Oʻtirish 8000, har km 3000» → 8000 + 3000k",
                    "k = 6 → 8000 + 18 000 = 26 000",
                ],
            },
        ],
        "questions": [
            {
                "text": "Matnga koʻra, ikki tarifdan qaysi biri arzon ekani nimaga "
                        "bogʻliq?",
                "choices": [
                    "Kunning qaysi vaqti ekaniga",
                    "Bosib oʻtiladigan masofaga",
                    "Mashinaning rangiga",
                    "Yoʻlovchilar soniga",
                ],
                "answer": 1,
                "explanation": "Qisqa yoʻlda birinchi tarif, uzun yoʻlda ikkinchisi "
                               "arzon tushadi. Toʻrt kilometrda ikkalasi teng.",
            },
            {
                "text": "«Chaqmoq» tarifi bilan 6 kilometrlik yoʻl qancha turadi?",
                "choices": ["18 000 soʻm", "24 000 soʻm", "26 000 soʻm", "30 000 soʻm"],
                "answer": 2,
                "explanation": "8000 + 3000 × 6 = 8000 + 18 000 = 26 000 soʻm.",
            },
            {
                "text": "Necha kilometrda ikkala tarif bir xil pul chiqaradi?",
                "choices": ["2 km", "4 km", "6 km", "10 km"],
                "answer": 1,
                "explanation": "4 km da: 8000 + 12 000 = 20 000 va "
                               "12 000 + 8000 = 20 000. Undan qisqa yoʻlda «Chaqmoq», "
                               "uzunroqda «Salom» arzon.",
            },
        ],
        "body": """
<p>Telefonda ikki taksi ilovasi bor. Ikkalasi bir xil mashina yuboradi, lekin <span class="cn-word" data-tr="narx qanday hisoblanishini belgilovchi qoida">tarif</span>i
har xil. Qaysi biri arzon?</p>

<p>«Chaqmoq» shunday deydi: oʻtirganingiz uchun <strong>8000</strong> soʻm, keyin har
kilometr uchun <strong>3000</strong> soʻmdan. «Salom» esa boshqacha:
<strong>12 000</strong> soʻm oʻtirish haqi, har kilometr uchun <strong>2000</strong>
soʻm.</p>

<p>Bu ikki gapni <span class="cn-word" data-tr="harf, son va amallardan tuzilgan yozuv">ifoda</span>ga
aylantiramiz. Bosib oʻtilgan kilometrni <b>k</b> deb belgilaymiz —
u <span class="cn-word" data-tr="qiymati oʻzgarib turadigan miqdor">oʻzgaruvchi</span>,
chunki har safar boshqacha boʻladi.</p>

<p>«Chaqmoq»: <strong>8000 + 3000k</strong>. «Salom»:
<strong>12 000 + 2000k</strong>. Har ikkalasida oʻtirish haqi
<span class="cn-word" data-tr="harfsiz, oʻzgarmaydigan son">ozod had</span>, kilometr
puli esa oʻzgaruvchiga koʻpaytiriladi.</p>

<p>Endi bir necha <span class="cn-word" data-tr="oʻzgaruvchi qabul qiladigan aniq son">qiymat</span>ni sinab koʻramiz. <b>2 km:</b> 14 000 va 16 000 — «Chaqmoq»
arzon. <b>4 km:</b> 20 000 va 20 000 — <b>teng</b>. <b>6 km:</b> 26 000 va 24 000 —
endi «Salom» arzon. <b>12 km:</b> 44 000 va 36 000 — farq allaqachon katta.</p>

<p>Sabab koʻrinib turibdi: «Salom» boshida koʻproq oladi, lekin har kilometr uchun
<span class="cn-word" data-tr="harf oldidagi son">koeffitsient</span>i kichik. Yoʻl
uzaygan sari shu kichik son gʻalaba qiladi: ikki narx teng boʻladigan <span class="cn-word" data-tr="ikki hisob bir xil natija beradigan qiymat">teng nuqta</span> — toʻrtinchi kilometr.</p>

<p>Shuning uchun tarifni oʻqiyotganda bitta savol bering: qaysi son <b>bir marta</b>
olinadi va qaysi biri <b>har safar</b>? Telefon tarifi ham, elektr hisobi ham, ijara
ham xuddi shu shaklda tuziladi.</p>

<p>Bitta qisqa ifoda — va reklama emas, hisob gapiradi.</p>
""",
    },
]
