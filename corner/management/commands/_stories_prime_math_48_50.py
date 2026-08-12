# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-48, PM-49, PM-50.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 48 — yangilik (ob-havo xabari), 49 — ilmiy-ommabop (taksi hisoblagichi),
50 — sharh (ikki tarifni taqqoslash). Oldingi uchtasi tarix, hikoya va
ilmiy-ommabop edi; ketma-ket uchta bir xil shakl chiqmaydi.

⚠️ Kumulyativ: ikki chiziqning kesishishi ALGEBRA bilan yechilmaydi (PM-52) —
   50-matnda kesishuv faqat jadvaldan oʻqiladi.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_48_50.py --author=prime
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
    # PM-48 — jadvaldan grafikka                             YANGILIK
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bir haftalik harorat",
        "summary": (
            "PM-48 matni. Yangilik xabari: mahalliy gazeta bir haftalik "
            "haroratni jadval va grafik bilan beradi — va nega aynan grafik "
            "koʻproq narsa aytishini tushuntiradi."
        ),
        "order":   48,
        "grammar": [
            {
                "pattern":  "jadval → nuqtalar → chiziq",
                "meaning":  "Jadvalning har bir ustuni bitta (x; y) nuqta beradi. "
                            "Miqdor uzluksiz oʻzgarsa (harorat, vaqt), nuqtalar "
                            "chiziq bilan bogʻlanadi.",
                "examples": [
                    "(1; 3), (2; 5), (3; 8), (4; 6), (5; 2), (6; −1), (7; −4)",
                    "Eng katta farq: |8 − (−4)| = 12 daraja",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega tahririyat jadvalning yoniga grafik ham qoʻydi?",
                "choices": [
                    "Gazetada joy koʻp qolgani uchun",
                    "Grafik sonlarni aniqroq koʻrsatgani uchun",
                    "Oʻzgarish yoʻnalishi grafikda bir qarashda koʻringani uchun",
                    "Jadvalni oʻqish taqiqlangani uchun",
                ],
                "answer": 2,
                "explanation": "Matnda aytilganidek, koʻz sonlarni emas, shaklni "
                               "tez oʻqiydi: pasayish grafikda darrov koʻrinadi, "
                               "jadvalda esa har bir sonni solishtirish kerak.",
            },
            {
                "text": "Haftaning eng issiq va eng sovuq kunlari orasidagi farq "
                        "necha daraja?",
                "choices": ["4 daraja", "8 daraja", "12 daraja", "14 daraja"],
                "answer": 2,
                "explanation": "Eng yuqori 8° (chorshanba), eng past −4° "
                               "(yakshanba). |8 − (−4)| = 8 + 4 = 12 daraja. "
                               "«4 daraja» — minusni eʼtibordan chiqargan javob.",
            },
            {
                "text": "Qaysi ikki kun orasida harorat eng koʻp pasaydi?",
                "choices": [
                    "Chorshanbadan payshanbaga",
                    "Payshanbadan jumaga",
                    "Jumadan shanbaga",
                    "Shanbadan yakshanbaga",
                ],
                "answer": 1,
                "explanation": "Payshanba 6°, juma 2° — 4 daraja pasayish. "
                               "Qolganlari: 8° → 6° ikki daraja, 2° → −1° va "
                               "−1° → −4° uch darajadan.",
            },
        ],
        "body": """
<p><b>«Kuz bir haftada keldi»</b> — shunday sarlavha bilan chiqdi tuman
gazetasining dushanba soni.</p>

<p>Xabarda oʻtgan haftaning kunduzgi harorati berilgan edi. Avval
<span class="cn-word" data-tr="qatorlarga va ustunlarga joylashtirilgan maʼlumot">jadval</span>
koʻrinishida:</p>

<p>dushanba <strong>3°</strong>, seshanba <strong>5°</strong>, chorshanba
<strong>8°</strong>, payshanba <strong>6°</strong>, juma <strong>2°</strong>,
shanba <strong>−1°</strong>, yakshanba <strong>−4°</strong>.</p>

<p>Uning yonida esa <span class="cn-word" data-tr="maʼlumotning nuqtalar va chiziq bilan chizilgan koʻrinishi">grafik</span>
turardi. Tahririyat buni bejiz qilmagan edi.</p>

<p>Jadvalda ettita son bor. Ularni bir-biri bilan solishtirish uchun koʻz
oldinga-orqaga yugurishi kerak. Grafikda esa har bir kun bitta
<span class="cn-word" data-tr="(x; y) juftligi tekislikda belgilangan joy">nuqta</span>
boʻlib turadi: gorizontal
<span class="cn-word" data-tr="koordinata tekisligining sonlar qoʻyilgan chizigʻi">oʻq</span>da
kun, vertikal oʻqda daraja. Chorshanbada chiziq
eng tepaga koʻtarilgan, keyin esa toʻxtovsiz pastga ketgan.</p>

<p>Harorat <span class="cn-word" data-tr="oraliq qiymatlari ham boʻladigan miqdor">uzluksiz miqdor</span>
— soat oʻn birda ham, oʻn bir yarimda ham oʻz qiymati bor. Shuning uchun
nuqtalarni chiziq bilan bogʻlash mumkin. Sotilgan gazetalar sonini shunday
bogʻlab boʻlmaydi: yarimta gazeta yoʻq, u
<span class="cn-word" data-tr="faqat butun sonlarda boʻladigan miqdor">diskret miqdor</span>.</p>

<p>Grafikning eng gapiradigan joyi — payshanba bilan juma orasi. Ikki kunda
harorat <strong>6°</strong> dan <strong>2°</strong> ga tushgan: toʻrt daraja.
Chiziqning oʻsha boʻlagi eng tik.</p>

<p>Haftaning eng issiq va eng sovuq kuni orasidagi
<span class="cn-word" data-tr="ikki qiymat orasidagi uzoqlik">farq</span>ni ham
grafikdan oʻlchash mumkin: yuqoridagi nuqtadan pastdagisigacha
<strong>|8 − (−4)| = 12</strong> daraja.</p>

<p>Xabar oxirida bir eslatma bor edi. <b>«Grafikni oʻqiyotganda avval
<span class="cn-word" data-tr="bitta katakning qiymati">shkala</span>ga qarang»</b>
— deb yozilgandi. — <b>«Bizning grafikda bitta katak 2 daraja. Buni
sezmasangiz, hamma pasayish ikki barobar kichik koʻrinadi.»</b></p>

<p>Bu maslahat ob-havoga emas, hamma grafiklarga tegishli.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-49 — chiziqli funksiya                        ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Taksi hisobi grafikda",
        "summary": (
            "PM-49 matni. Ilmiy-ommabop: taksi hisoblagichidagi sonlar aslida "
            "toʻgʻri chiziq ekani — b oʻtirish haqi, k esa kilometr narxi."
        ),
        "order":   49,
        "grammar": [
            {
                "pattern":  "y = kx + b",
                "meaning":  "Chiziqli funksiya. b — boshlangʻich qiymat "
                            "(x = 0 dagi y), k — har bir birlikda qoʻshiladigan "
                            "miqdor. Grafigi har doim toʻgʻri chiziq.",
                "examples": [
                    "y = 3 000x + 8 000 → 12 km: 36 000 + 8 000 = 44 000 soʻm",
                    "29 000 soʻm: 3 000x = 21 000 → x = 7 km",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega taksi hisoblagichining grafigi noldan emas, 8 000 "
                        "dan boshlanadi?",
                "choices": [
                    "Chunki mashina bir kilometr yurib boʻlgan boʻladi",
                    "Chunki oʻtirish haqi yoʻlga chiqmasdan turib olinadi",
                    "Chunki hisoblagich notoʻgʻri ishlaydi",
                    "Chunki birinchi kilometr qimmatroq",
                ],
                "answer": 1,
                "explanation": "b — x = 0 dagi qiymat, yaʼni hech qayerga "
                               "bormasdan turibgi narx. Taksida bu oʻtirish haqi.",
            },
            {
                "text": "12 kilometrlik yoʻl qancha turadi?",
                "choices": [
                    "36 000 soʻm", "44 000 soʻm", "52 000 soʻm", "96 000 soʻm",
                ],
                "answer": 1,
                "explanation": "3 000 × 12 = 36 000, ustiga oʻtirish haqi 8 000: "
                               "jami 44 000 soʻm. «36 000» — oʻtirish haqi "
                               "qoʻshilmagan javob.",
            },
            {
                "text": "Bekzod 29 000 soʻm toʻladi. U necha kilometr yurgan?",
                "choices": ["5 km", "7 km", "9 km", "12 km"],
                "answer": 1,
                "explanation": "Avval oʻtirish haqi ayiriladi: "
                               "29 000 − 8 000 = 21 000. Keyin "
                               "21 000 ÷ 3 000 = 7 km. «9 km» — oʻtirish haqini "
                               "ayirmagan javob.",
            },
        ],
        "body": """
<p>Taksiga oʻtirasiz, eshikni yopasiz — va hisoblagich hali bir metr ham
yurmasdan turib <strong>8 000</strong> soʻmni koʻrsatadi.</p>

<p>Bu adolatsizlikka oʻxshaydi. Aslida esa bu oddiy matematik qoida.</p>

<p>Taksi narxi ikki qismdan iborat. Birinchisi —
<span class="cn-word" data-tr="foydalanmasa ham toʻlanadigan oʻzgarmas haq">oʻtirish haqi</span>:
mashinaning kelishi, kutishi, yoqilgʻisi. U yoʻlning uzunligiga bogʻliq emas.
Ikkinchisi — har bir kilometr uchun <strong>3 000</strong> soʻm.</p>

<p>Ikkalasini birga yozsak, <span class="cn-word" data-tr="grafigi toʻgʻri chiziq boʻladigan funksiya">chiziqli funksiya</span>
chiqadi:</p>

<p><strong>y = 3 000x + 8 000</strong></p>

<p>Bu yerda x — kilometrlar soni, y — toʻlov. Yozuvdagi 8 000 —
<span class="cn-word" data-tr="x = 0 dagi qiymat, chiziqning boshlanishi">boshlangʻich qiymat</span>,
matematikada <b>b</b> deb belgilanadi. 3 000 esa
<span class="cn-word" data-tr="x bir birlikka oshganda y ning oʻzgarishi">qadam</span>,
yaʼni <b>k</b>.</p>

<p>Endi buni <span class="cn-word" data-tr="maʼlumotning chizilgan koʻrinishi">grafik</span>ka
tushiring. Chiziq koordinata boshidan emas, <strong>(0; 8 000)</strong>
nuqtasidan boshlanadi — bu oʻtirish haqining oʻzi. Keyin har kilometrda 3 000 ga
koʻtariladi. Nuqtalar bir-biriga qoʻshilib, tep-tekis
<span class="cn-word" data-tr="egilmagan, bir tekis chiziq">toʻgʻri chiziq</span>
hosil qiladi.</p>

<p>Oʻn ikki kilometrlik yoʻl uchun: 3 000 × 12 = 36 000, ustiga 8 000 —
<strong>44 000</strong> soʻm.</p>

<p>Teskari savol ham xuddi shu chiziqdan oʻqiladi. Bekzod <strong>29 000</strong>
soʻm toʻladi — qancha yurgan? Avval oʻtirish haqini ayiramiz: 29 000 − 8 000 =
21 000. Qolganini kilometr narxiga boʻlamiz: 21 000 ÷ 3 000 = <strong>7</strong>
kilometr. Bu — <span class="cn-word" data-tr="nomaʼlumni topish uchun tuziladigan tenglik">tenglama</span>ning
oddiy koʻrinishi.</p>

<p>Shunga oʻxshash chiziqlar atrofimizda juda koʻp: elektr hisobi, internet
tarifi, ish haqi, kommunal toʻlov. Hammasining
<span class="cn-word" data-tr="chiziqning tikligi, k">qiyalik</span>i va
boshlanishi bor. Bittasini tushunsangiz, hammasini tushunasiz.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-50 — k va b ning maʼnosi                                SHARH
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ikki tarif, ikki chiziq",
        "summary": (
            "PM-50 matni. Sharh: telefon operatorining ikki tarifi jadval va "
            "grafik bilan taqqoslanadi — k va b ni bilgan odam reklamaga emas, "
            "oʻz sarfiga qarab tanlaydi."
        ),
        "order":   50,
        "grammar": [
            {
                "pattern":  "b — boshida qancha, k — har birlik uchun qancha",
                "meaning":  "Tarifni oʻqishning butun siri shu ikki sonda. Kam "
                            "foydalanadiganga past b, koʻp foydalanadiganga "
                            "kichik k foydali.",
                "examples": [
                    "A: y = 200x + 20 000 → 250 daqiqa: 50 000 + 20 000 = 70 000",
                    "B: y = 100x + 50 000 → 250 daqiqa: 25 000 + 50 000 = 75 000",
                ],
            },
        ],
        "questions": [
            {
                "text": "Muallif nega «reklamadagi katta harflarga ishonmang» "
                        "deydi?",
                "choices": [
                    "Chunki reklama faqat bitta sonni koʻrsatadi, ikkinchisini "
                    "emas",
                    "Chunki operatorlar narxni tez-tez oʻzgartiradi",
                    "Chunki reklamada sonlar umuman boʻlmaydi",
                    "Chunki jadval tuzish taqiqlangan",
                ],
                "answer": 0,
                "explanation": "Tarifni ikkita son belgilaydi: abonent haqi (b) "
                               "va daqiqa narxi (k). Reklama odatda faqat "
                               "bittasini — arzon koʻringanini — chiqaradi.",
            },
            {
                "text": "250 daqiqa gaplashadigan odam uchun qaysi tarif arzon?",
                "choices": [
                    "A tarif, 5 000 soʻmga arzon",
                    "B tarif, 5 000 soʻmga arzon",
                    "A tarif, 25 000 soʻmga arzon",
                    "Ikkalasi ham teng",
                ],
                "answer": 0,
                "explanation": "A: 200 × 250 + 20 000 = 70 000. "
                               "B: 100 × 250 + 50 000 = 75 000. Farq 5 000 soʻm, "
                               "A foydali.",
            },
            {
                "text": "400 daqiqada qaysi tarif arzon va qancha farq bilan?",
                "choices": [
                    "A tarif, 10 000 soʻmga",
                    "A tarif, 30 000 soʻmga",
                    "B tarif, 10 000 soʻmga",
                    "B tarif, 30 000 soʻmga",
                ],
                "answer": 2,
                "explanation": "A: 200 × 400 + 20 000 = 100 000. "
                               "B: 100 × 400 + 50 000 = 90 000. Endi B arzon, "
                               "farq 10 000 soʻm — chunki uzoq gaplashganda "
                               "kichik k yutadi.",
            },
        ],
        "body": """
<p>Operator ikkita yangi <span class="cn-word" data-tr="bir birlik xizmatning narxi">tarif</span>
eʼlon qildi va shahar reklama bilan toʻldi. Kattakon harflar bilan: <b>«Daqiqasi
atigi 100 soʻm!»</b></p>

<p>Bir qarashda ishonarli. Lekin bu — ikkita sondan faqat bittasi.</p>

<p><b>A tarif:</b> <span class="cn-word" data-tr="foydalanmasa ham har oy toʻlanadigan pul">abonent haqi</span>
20 000 soʻm, daqiqasi 200 soʻm. <b>B tarif:</b> abonent haqi 50 000 soʻm,
daqiqasi 100 soʻm.</p>

<p>Ikkalasi ham <span class="cn-word" data-tr="grafigi toʻgʻri chiziq boʻladigan funksiya">chiziqli funksiya</span>:
<strong>A: y = 200x + 20 000</strong> va <strong>B: y = 100x + 50 000</strong>.
Abonent haqi — <span class="cn-word" data-tr="x = 0 dagi qiymat">boshlangʻich qiymat</span>,
daqiqa narxi esa <span class="cn-word" data-tr="chiziqning tikligi, har birlikdagi oʻzgarish">qiyalik</span>.</p>

<p>Jadval tuzsak, hammasi koʻrinadi.</p>

<p>100 daqiqada A <strong>40 000</strong>, B <strong>60 000</strong> soʻm.
250 daqiqada A <strong>70 000</strong>, B <strong>75 000</strong>. 300 daqiqada
ikkalasi ham <strong>80 000</strong>. 400 daqiqada esa A <strong>100 000</strong>,
B <strong>90 000</strong> — endi B arzon.</p>

<p>Grafikda bu ikkita <span class="cn-word" data-tr="egilmagan chiziq">toʻgʻri chiziq</span>.
A pastroqdan boshlanadi, lekin tikroq koʻtariladi. B yuqoridan boshlanadi va
yotiqroq boradi. Uch yuzinchi daqiqada ular
<span class="cn-word" data-tr="ikki chiziq uchrashgan joy">kesishish nuqtasi</span>da
uchrashadi. (Bunday nuqtani jadvalsiz, hisoblab topishni PM-52 darsida
oʻrganamiz.)</p>

<p>Xulosa sodda. Kam gaplashadiganga <b>A</b> foydali — abonent haqi past. Koʻp
gaplashadiganga <b>B</b> — har daqiqasi arzon. Uch yuz daqiqa atrofida esa farq
yoʻq.</p>

<p>Shuning uchun reklamadagi katta harflarga emas, oʻz
<span class="cn-word" data-tr="bir oyda sarflangan miqdor">sarf</span>ingizga
qarang. Oʻtgan oy necha daqiqa gaplashgansiz? Shu sonni ikkala formulaga qoʻying
va taqqoslang. Besh daqiqalik hisob bir yillik ortiqcha toʻlovdan saqlaydi.</p>
""",
    },
]
