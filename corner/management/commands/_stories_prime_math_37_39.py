# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-37 … PM-39.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 37 — hikoya, 38 — yangilik xabari (maktab musobaqasi),
39 — hikoya.
⚠️ Tocda 38-matn ham «hikoya» deb belgilangan edi, lekin 37 va 39 hikoya
   boʻlgani uchun janr YANGILIK XABARI ga oʻzgartirildi — tocning oʻz
   qoidasi: ketma-ket uchta bir xil shakl boʻlmasin.

⚠️ Kumulyativ: hamma masala BITTA harf bilan yechiladi; tengsizlik (PM-40)
   va modul (PM-41) yoʻq.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_37_39.py --author=prime
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
    # PM-37 — ikki tomonli tenglama                            HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ikki doʻkon, bitta narx",
        "summary": (
            "PM-37 matni. Hikoya: maktabga daftar buyurtma qilinadi va ikki "
            "doʻkonning narxi tenglashadigan nuqta tenglama bilan topiladi. "
            "Javob «qancha olasiz» degan savolga bogʻliq chiqadi."
        ),
        "order":   37,
        "grammar": [
            {
                "pattern":  "Ikki ifodani tenglashtirish",
                "meaning":  "Ikki variant qachon bir xil pul chiqarishini bilish "
                            "uchun ularning ifodalarini tenglashtiramiz. Hosil "
                            "boʻlgan tenglamada nomaʼlum ikkala tomonda boʻladi.",
                "examples": [
                    "30 000 + 6000n = 10 000 + 8000n",
                    "20 000 = 2000n → n = 10 (ikkalasida ham 90 000 soʻm)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nodira opa nima uchun darrov qaror qila olmadi?",
                "choices": [
                    "Doʻkonlar narxni aytmagani uchun",
                    "Bir doʻkon yetkazib berishni arzon, daftarni qimmat sotgani uchun",
                    "Maktabda pul boʻlmagani uchun",
                    "Daftarlar sifati har xil boʻlgani uchun",
                ],
                "answer": 1,
                "explanation": "Bir doʻkonda yetkazib berish qimmat, lekin daftar "
                               "arzon; ikkinchisida aksincha. Shuning uchun javob "
                               "nechta daftar olinishiga bogʻliq edi.",
            },
            {
                "text": "Necha daftar olinganda ikki doʻkonning narxi tenglashadi?",
                "choices": ["5 ta", "8 ta", "10 ta", "20 ta"],
                "answer": 2,
                "explanation": "30 000 + 6000n = 10 000 + 8000n → 20 000 = 2000n → "
                               "n = 10 ta daftar.",
            },
            {
                "text": "Oʻsha nuqtada har ikki doʻkonda ham qancha toʻlanadi?",
                "choices": ["60 000 soʻm", "80 000 soʻm", "90 000 soʻm",
                            "100 000 soʻm"],
                "answer": 2,
                "explanation": "30 000 + 6000 × 10 = 90 000 va "
                               "10 000 + 8000 × 10 = 90 000 soʻm.",
            },
        ],
        "body": """
<p>Maktabga daftar kerak boʻlib qoldi. Nodira opa ikki doʻkonga qoʻngʻiroq qildi va
javoblarni daftariga yozib oldi.</p>

<p>«Bilim» doʻkoni: yetkazib berish <strong>30 000</strong> soʻm, har bir daftar
<strong>6000</strong> soʻm. «Zamon» doʻkoni: yetkazib berish atigi
<strong>10 000</strong> soʻm, lekin har daftar <strong>8000</strong> soʻm.</p>

<p>— Qaysi biri arzon? — soʻradi Jasur.</p>

<p>— Nechta olishimizga qarab, — dedi Nodira opa. — Keling, hisoblaymiz.</p>

<p>Daftarlar sonini — u hozircha <span class="cn-word" data-tr="qiymati oʻzgarib turadigan miqdor">oʻzgaruvchi</span> — <b>n</b> deb belgilashdi va ikki
<span class="cn-word" data-tr="harf, son va amallardan tuzilgan yozuv">ifoda</span>
yozishdi: <strong>30 000 + 6000n</strong> va <strong>10 000 + 8000n</strong>.</p>

<p>— Ular qachon teng boʻladi? — dedi Nodira opa va ikkala ifodani tenglik belgisi
bilan bogʻladi. Doskada nomaʼlumi <b>ikkala tomonda</b> turgan
<span class="cn-word" data-tr="ikki ifodaning tengligi">tenglama</span> paydo
boʻldi.</p>

<p>Afsona yechdi. Avval ikki tomondan <strong>6000n</strong> ni ayirdi — chunki
<span class="cn-word" data-tr="ikki tomonga bir xil amal qilish qoidasi">muvozanat qoidasi</span>
harfli hadga ham xuddi shunday ishlaydi. Qoldi:
<strong>30 000 = 10 000 + 2000n</strong>. Keyin 10 000 ni ayirdi:
<strong>20 000 = 2000n</strong>. Demak <strong>n = 10</strong>.</p>

<p>— Oʻn daftarda ikkalasi ham <strong>90 000</strong> soʻm, — dedi Afsona va
<span class="cn-word" data-tr="javobni asl shartga qoʻyib sinash">tekshirdi</span>:
30 000 + 60 000 = 90 000, 10 000 + 80 000 = 90 000. Toʻgʻri.</p>

<p>— Mana shu <span class="cn-word" data-tr="ikki variant tenglashadigan qiymat">chegara nuqta</span>, —
dedi Nodira opa. — Undan kam olsak, «Zamon» arzon; koʻp olsak, «Bilim».</p>

<p>Maktabga 30 ta daftar kerak edi. Buyurtma «Bilim» doʻkoniga berildi — va u yerda
210 000 soʻm chiqdi, «Zamon»da esa 250 000 boʻlardi. Qirq mingga yaqin pul
tenglamaning bir necha qatori evaziga tejaldi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-38 — matnli masala 1                        YANGILIK XABARI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Jasur va Afsona necha yigʻdi",
        "summary": (
            "PM-38 matni. Yangilik xabari: maktabdagi qogʻoz yigʻish musobaqasi "
            "natijalari faqat qisman eʼlon qilinadi va qolganini oʻquvchilar "
            "tenglama bilan tiklashadi."
        ),
        "order":   38,
        "grammar": [
            {
                "pattern":  "Ikki miqdorni bitta harf bilan yozish",
                "meaning":  "Tayanch miqdorni x deb olamiz, ikkinchisini esa uning "
                            "orqali yozamiz. Shunda bitta shart bitta tenglama "
                            "beradi va masala yechiladi.",
                "examples": [
                    "Afsona x, Jasur x + 12; x + (x + 12) = 60",
                    "2x + 12 = 60 → 2x = 48 → x = 24, Jasur esa 36",
                ],
            },
        ],
        "questions": [
            {
                "text": "Xabarda nima uchun ikkala natija ham yozilmagan edi?",
                "choices": [
                    "Musobaqa hali tugamagani uchun",
                    "Eʼlonda faqat jami va farq berilgan edi",
                    "Oʻqituvchi natijalarni yoʻqotib qoʻygani uchun",
                    "Oʻquvchilar natijani aytishni istamagani uchun",
                ],
                "answer": 1,
                "explanation": "Eʼlonda ikkalasining jami (60 kg) va ular "
                               "orasidagi farq (12 kg) berilgan edi — qolganini "
                               "hisoblab topish kerak boʻldi.",
            },
            {
                "text": "Afsona necha kilogramm qogʻoz yigʻdi?",
                "choices": ["12 kg", "24 kg", "30 kg", "36 kg"],
                "answer": 1,
                "explanation": "x + (x + 12) = 60 → 2x = 48 → x = 24 kg. Bu — "
                               "Afsonaning natijasi.",
            },
            {
                "text": "Jasur necha kilogramm yigʻdi?",
                "choices": ["24 kg", "30 kg", "36 kg", "48 kg"],
                "answer": 2,
                "explanation": "Jasur Afsonadan 12 kg koʻp: 24 + 12 = 36 kg. "
                               "Tekshirish: 24 + 36 = 60 ✓",
            },
        ],
        "body": """
<p><b>Maktab xabari.</b> Bu hafta 7-«B» sinfida eski qogʻoz yigʻish musobaqasi
boʻlib oʻtdi. Gʻoliblar aniqlandi, lekin eʼlon qiziq tarzda yozilgan edi.</p>

<p>Devordagi varaqda shunday deb yozilgandi: «Birinchi oʻrinni Jasur va Afsona
egalladi. Ular birgalikda <strong>60</strong> kilogramm qogʻoz topshirishdi. Jasur
Afsonadan <strong>12</strong> kilogramm koʻp yigʻdi».</p>

<p>Har birining natijasi yozilmagan edi. Sinf rahbari buni ataylab qilgan ekan.</p>

<p>— Bu sizga uy vazifasi, — dedi Nodira opa. — Kim birinchi boʻlib aniq sonlarni
aytsa, gʻolib oʻsha.</p>

<p>Sherbek doskaga chiqdi va masalani <span class="cn-word" data-tr="shartni tenglik koʻrinishida yozish">tenglama tuzish</span> yoʻli bilan yechishga kirishdi. U avval
<span class="cn-word" data-tr="qaysi miqdorni x deb olish">nomaʼlumni tanladi</span>:
Afsonaning natijasi <b>x</b> boʻlsin. Nega Afsona? Chunki Jasur unga nisbatan
oʻlchangan — Afsona bu yerda
<span class="cn-word" data-tr="boshqalari oʻlchanadigan asosiy miqdor">tayanch miqdor</span>.</p>

<p>Unda Jasurning natijasi <strong>x + 12</strong> boʻladi. Ikkalasi
<span class="cn-word" data-tr="qoʻshish natijasi">yigʻindi</span>si 60 kilogramm:
<strong>x + (x + 12) = 60</strong>.</p>

<p>Sherbek <span class="cn-word" data-tr="oʻxshash hadlarni qoʻshib yozuvni qisqartirish">ixchamladi</span>:
<strong>2x + 12 = 60</strong>. Keyin ikki tomondan 12 ni ayirdi:
<strong>2x = 48</strong>, demak <strong>x = 24</strong>.</p>

<p>— Afsona 24 kilogramm! — dedi u va joyiga oʻtirmoqchi boʻldi.</p>

<p>— Shoshmang, — dedi Nodira opa. — Savol Jasur haqida ham edi.</p>

<p>Sherbek qizarib qaytdi va oxirgi qadamni bajardi: Jasur 24 + 12 =
<strong>36</strong> kilogramm.
<span class="cn-word" data-tr="javobni asl shartga qoʻyib sinash">Tekshiruv</span>
ham darrov: 24 + 36 = 60 ✓ va 36 − 24 = 12 ✓</p>

<p>— Mana endi toʻliq javob, — dedi Nodira opa. — Esda tuting: x ni topish yechimning
oxiri emas, oʻrtasi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-39 — matnli masala 2                                  HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ikki chelak suv",
        "summary": (
            "PM-39 matni. Hikoya: bobosi nevarasiga chelaklar jumbogʻini beradi. "
            "Sir «quyilgan suv farqni ikki barobar kamaytiradi» degan gapda "
            "yashiringan."
        ),
        "order":   39,
        "grammar": [
            {
                "pattern":  "Quyish farqni ikki barobar kamaytiradi",
                "meaning":  "Bir idishdan olingan miqdor ikkinchisiga qoʻshiladi, "
                            "shuning uchun ikki idish orasidagi farq quyilgan "
                            "miqdorning ikki barobariga qisqaradi.",
                "examples": [
                    "5 litr quyilib teng boʻlsa → boshlangʻich farq 10 litr",
                    "x + (x + 10) = 30 → x = 10; chelaklarda 20 va 10 litr",
                ],
            },
        ],
        "questions": [
            {
                "text": "Bekzod birinchi urinishda nima uchun xato qildi?",
                "choices": [
                    "Jami suv miqdorini notoʻgʻri oʻqigani uchun",
                    "Farqni 5 litr deb olgani uchun",
                    "Chelaklarni sanamagani uchun",
                    "Qoʻshish oʻrniga ayirish qilgani uchun",
                ],
                "answer": 1,
                "explanation": "Bekzod «5 litr quyilsa teng boʻladi» degan gapdan "
                               "farq 5 litr deb oʻyladi. Aslida farq 10 litr edi.",
            },
            {
                "text": "Birinchi chelakda necha litr suv bor edi?",
                "choices": ["10 litr", "15 litr", "17,5 litr", "20 litr"],
                "answer": 3,
                "explanation": "x + (x + 10) = 30 → 2x = 20 → x = 10; kattasi "
                               "10 + 10 = 20 litr.",
            },
            {
                "text": "5 litr quyilgandan keyin har chelakda necha litr qoladi?",
                "choices": ["12,5 litr", "15 litr", "17,5 litr", "20 litr"],
                "answer": 1,
                "explanation": "20 − 5 = 15 va 10 + 5 = 15. Ikkala chelakda ham "
                               "15 litr — teng.",
            },
        ],
        "body": """
<p>Bobosi hovlida ikkita chelakni koʻrsatdi. Ikkalasida ham suv bor edi, lekin har xil
miqdorda.</p>

<p>— Jami <strong>30</strong> litr, — dedi bobosi. — Birinchisidan ikkinchisiga
<strong>5</strong> litr quysam, ular <b>teng</b> boʻladi. Aytchi, hozir qaysi birida
qancha?</p>

<p>Bekzod darrov <span class="cn-word" data-tr="qaysi miqdorni x deb olish">nomaʼlumni tanlab</span>, hisoblay boshladi. «Besh litr quyilsa teng boʻladi — demak
<span class="cn-word" data-tr="ikki miqdor orasidagi ayirma">farq</span> besh litr»,
deb oʻyladi u. Shunday qilib x va x + 5 deb yozdi va 12,5 hamda 17,5 degan javob
oldi.</p>

<p>— Tekshirib koʻr, — dedi bobosi.</p>

<p>Bekzod tekshirdi: 17,5 − 5 = 12,5 va 12,5 + 5 = 17,5. Teng chiqmadi — biri hamon
kattaroq edi.</p>

<p>— Xatoing qayerda ekanini oʻzing top, — dedi bobosi va choyini quydi.</p>

<p>Bekzod uzoq oʻyladi. Keyin tushundi: quyilgan suv bir chelakdan
<b>kamayadi</b> va ikkinchisiga <b>qoʻshiladi</b>. Demak farq besh emas,
<strong>oʻn</strong> litrga qisqaradi.</p>

<p>U qaytadan yozdi. Kichik chelak <b>x</b>, kattasi <strong>x + 10</strong> boʻlsin.
<span class="cn-word" data-tr="ikki ifodaning tengligi">Tenglama</span>:
<strong>x + (x + 10) = 30</strong>.</p>

<p><span class="cn-word" data-tr="oʻxshash hadlarni qoʻshib yozuvni qisqartirish">Ixchamlagach</span>
<strong>2x + 10 = 30</strong>, undan <strong>2x = 20</strong> va
<strong>x = 10</strong> chiqdi. Demak kichik chelakda 10 litr, kattasida
<strong>20</strong> litr.</p>

<p>Bu safar <span class="cn-word" data-tr="javobni asl shartga qoʻyib sinash">tekshiruv</span>
toʻgʻri chiqdi: 20 − 5 = 15 va 10 + 5 = 15. Ikkalasida ham oʻn besh litr.</p>

<p>— Bobo, siz buni qayerdan bilasiz? — soʻradi Bekzod.</p>

<p>— Men chelak koʻtarib katta boʻlganman, — kuldi bobosi. — Sen esa
<span class="cn-word" data-tr="masalani yechishning aniq tartibi">usul</span>ni
oʻrgan. U ogʻirroq, lekin uzoqroqqa olib boradi.</p>
""",
    },
]
