# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-81, PM-82, PM-83 (Blok F).

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 81 — sharh, 82 — hikoya, 83 — ilmiy-ommabop.
Oldingi uchlik kundalik / ilmiy-ommabop / sport edi.

⚠️ Kumulyativ:
   • 81-matnda aldamchi diagramma; foiz oʻzgarishi (PM-25) ishlatiladi;
   • 82-matnda faqat sanash. ⛔ EHTIMOLLIK soʻzi YOʻQ;
   • 83-matnda ehtimollik gʻoyasi. Ob-havo foizi «koʻp yillik
     kuzatuvdan olinadi» deb ATALADI, lekin uni hisoblash usuli
     berilmaydi — u PM-84 ning mavzusi.
⚠️ Sonlar darsdagilardan boshqa.
⚠️ Savollar SAQLANGAN TARTIBDA koʻrsatiladi — `answer` indekslari:
   81 → 2/1/3, 82 → 0/2/1, 83 → 1/3/0.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_81_83.py --author=prime
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
    # PM-81 — aldamchi diagramma                                  SHARH
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Reklamadagi ustunlar",
        "summary": (
            "PM-81 matni. Sharh: televizordagi tish pastasi reklamasi "
            "«besh barobar samaraliroq» deydi. Bekzod chizmani tekshirib, "
            "haqiqiy farq oʻn foiz ekanini topadi."
        ),
        "order":   81,
        "grammar": [
            {
                "pattern":  "oʻq noldan boshlanmasa, ustunlar nisbati yolgʻon gapiradi",
                "meaning":  "Koʻz ustunning uzunligiga qaraydi, oʻqdagi "
                            "mayda raqamlarga emas. Oʻqning boshlanishini "
                            "tekshirmasdan hech qanday xulosa "
                            "chiqarmaslik kerak.",
                "examples": [
                    "koʻringan nisbat: (99 − 88) ÷ (90 − 88) = 5,5 marta",
                    "haqiqiy farq: (99 − 90) ÷ 90 × 100 = 10%",
                    "oʻq noldan boshlansa: 90 va 99 — deyarli teng",
                ],
            },
        ],
        "questions": [
            {
                "text": "Bekzod chizmada birinchi navbatda nimaga eʼtibor "
                        "berdi?",
                "choices": [
                    "Ustunlarning rangiga",
                    "Reklamadagi yozuvga",
                    "Sonlar oʻqi qayerdan boshlanganiga",
                    "Ustunlarning eniga",
                ],
                "answer": 2,
                "explanation": "Diagrammani oʻqishning birinchi qoidasi shu: "
                               "oʻq noldan boshlanganmi? Bu yerda u 88 dan "
                               "boshlangan edi va aynan shu butun aldovni "
                               "yaratgan.",
            },
            {
                "text": "Ikki pasta orasidagi haqiqiy farq necha foiz?",
                "choices": ["5%", "10%", "11%", "50%"],
                "answer": 1,
                "explanation": "Farq: 99 − 90 = 9. Asos — raqibning 90 tasi: "
                               "9 ÷ 90 × 100 = 10%. «11%» — asos qilib 99 "
                               "olinganda chiqadi; oshishda asos har doim "
                               "eski son boʻladi.",
            },
            {
                "text": "Ustunlar koʻzga necha marta farq qilib koʻringan?",
                "choices": ["1,1 marta", "2 marta", "4,5 marta", "5,5 marta"],
                "answer": 3,
                "explanation": "Oʻq 88 dan boshlangani uchun koʻringan "
                               "qismlar: 90 − 88 = 2 va 99 − 88 = 11. "
                               "Demak 11 ÷ 2 = 5,5 marta — reklamadagi «besh "
                               "barobar» shu yerdan olingan.",
            },
        ],
        "body": """
<p>Kecha kechqurun televizorda tish pastasi
<span class="cn-word" data-tr="mahsulotni maqtab tarqatiladigan xabar">reklama</span>si
koʻrsatildi. Ekranda katta yozuv turardi: «Besh barobar samaraliroq!»</p>

<p>Yonida esa ikkita
<span class="cn-word" data-tr="diagrammadagi tik toʻgʻri toʻrtburchak">ustun</span>
bor edi. Chapdagisi past, oʻngdagisi baland — haqiqatan besh barobarga
yaqin farq koʻrinardi.</p>

<p>Bekzod pultni oldi va tasvirni toʻxtatdi.</p>

<p>Birinchi navbatda u ustunlarga emas, chapdagi
<span class="cn-word" data-tr="sonlar va nomlar yozilgan chiziq">oʻq</span>qa
qaradi. Bu — PM-81 darsidan qolgan odat: har qanday
<span class="cn-word" data-tr="maʼlumotning chizmadagi koʻrinishi">diagramma</span>ga
qaraganda birinchi savol bitta boʻladi — <b>oʻq qayerdan
boshlangan?</b></p>

<p>Oʻq noldan emas, <strong>88</strong> dan boshlangan edi.</p>

<p>Endi <span class="cn-word" data-tr="oʻqdagi boʻlinishlar qadami">shkala</span>ga
qarab sonlarni ham topdi: raqib pastasi <strong>90</strong>, reklama
qilinayotgani <strong>99</strong>
<span class="cn-word" data-tr="oʻlchov birligi, ballarda ifodalangan natija">ball</span>.</p>

<p>Endi hisob oson. Oʻqdan yuqorida koʻringan qismlar: 90 − 88 =
<strong>2</strong> va 99 − 88 = <strong>11</strong>. Ularning nisbati:
11 ÷ 2 = <strong>5,5</strong> marta. Mana qayerdan «besh barobar»
chiqqan ekan.</p>

<p>Lekin haqiqiy farq butunlay boshqa. Pastalarning farqi 99 − 90 =
<strong>9</strong> ball. Buni
<span class="cn-word" data-tr="foiz nimadan hisoblanayotgani">asos</span>ga —
raqibning 90 tasiga — nisbatan olamiz: 9 ÷ 90 × 100 =
<strong>10</strong>
<span class="cn-word" data-tr="yuzdan boʻlak">foiz</span>.</p>

<p>Oʻn foiz. Reklama esa besh barobarni koʻrsatdi — bu allaqachon
<span class="cn-word" data-tr="rost sonlar bilan notoʻgʻri taassurot qoldiruvchi chizma">aldamchi diagramma</span>.</p>

<p>Eng qizigʻi shundaki, reklamada birorta ham
<span class="cn-word" data-tr="haqiqatga toʻgʻri kelmaydigan gap">yolgʻon</span>
son yoʻq. 90 ham rost, 99 ham rost, ustunlar ham toʻgʻri chizilgan.
Yolgʻon <b>oʻqda</b> yashiringan: 90 ning ustunidan 88 tasi kesib
tashlangan, qolgan ikkitagina koʻrsatilgan.</p>

<p>Bekzod buni singlisiga tushuntirmoqchi boʻldi. U eshitib turdi-da,
soʻradi: «Unda nega hamma bunday chizmaydi?»</p>

<p>«Chizadi, — dedi Bekzod. — Faqat ular bizni oʻqqa qaramaydi deb
oʻylashadi.»</p>

<p>Buni <span class="cn-word" data-tr="noldan boshlanmagan sonlar oʻqi">kesilgan oʻq</span>
deb atashadi. Shu kunlarda Bekzod yangi odat orttirdi: har qanday chizmani koʻrganda
avval eng pastdagi mayda raqamni topadi. Koʻpincha butun hikoya
oʻsha yerda turgan boʻladi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-82 — koʻpaytirish prinsipi                              HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Necha xil kiyim tanlash mumkin",
        "summary": (
            "PM-82 matni. Hikoya: Sherbek lagerga jomadon yigʻayotib, "
            "ikki hafta davomida takrorlanmasdan kiyinish uchun nechta "
            "narsa kerakligini hisoblab chiqadi."
        ),
        "order":   82,
        "grammar": [
            {
                "pattern":  "variantlar soni = 1-bosqich × 2-bosqich × …",
                "meaning":  "Har bir yangi tanlov bosqichi yangi "
                            "koʻpaytiruvchi qoʻshadi. «Va» — koʻpaytirish, "
                            "«yoki» — qoʻshish.",
                "examples": [
                    "4 × 3 = 12 (futbolka va shim)",
                    "12 × 2 = 24 (kepka ham qoʻshildi)",
                    "24 > 14 — ikki haftaga yetadi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sherbek jami necha xil kiyinishi mumkin?",
                "choices": ["24 xil", "9 xil", "14 xil", "48 xil"],
                "answer": 0,
                "explanation": "4 ta futbolka × 3 ta shim × 2 ta kepka = "
                               "24. Har bir bosqich koʻpaytiruvchi boʻlib "
                               "qoʻshiladi. «9 xil» — qoʻshib yuborilganda "
                               "chiqadi (4 + 3 + 2).",
            },
            {
                "text": "Nega Sherbekning onasi qoʻshish kerak deb oʻyladi?",
                "choices": [
                    "Chunki u matematikani bilmaydi",
                    "Chunki jomadonga hammasi sigʻmasdi",
                    "Chunki u har bir narsani alohida sanadi — har bir "
                    "futbolka har bir shim bilan kelishini hisobga olmadi",
                    "Chunki kepkalar hisobga olinmagan edi",
                ],
                "answer": 2,
                "explanation": "Qoʻshish «yo futbolka, yo shim, yo kepka "
                               "tanlayman» degan boshqa savolga javob "
                               "beradi. Bu yerda esa uchalasi birga "
                               "kiyiladi, shuning uchun koʻpaytiriladi.",
            },
            {
                "text": "Agar Sherbek yana bitta kepka olsa, nechta variant "
                        "boʻladi?",
                "choices": ["25 xil", "36 xil", "27 xil", "48 xil"],
                "answer": 1,
                "explanation": "Kepkalar 3 ta boʻladi: 4 × 3 × 3 = 36. "
                               "Bitta narsa qoʻshilishi variantlar sonini "
                               "12 taga oshirdi — chunki u butun "
                               "koʻpaytmani oʻzgartiradi.",
            },
        ],
        "body": """
<p>Sherbek yozgi lagerga borishga tayyorlanayotgan edi. Lager ikki hafta
davom etadi — <strong>14</strong> kun.</p>

<p>Onasi jomadonni ochib qoʻydi: «Kiyimni oʻzing yigʻ. Faqat har kuni
bir xil koʻrinmaslikka harakat qil.»</p>

<p>Sherbek shkafga qaradi va
<span class="cn-word" data-tr="variantlar sonini aniqlash">sanash</span>ni
boshladi. Toʻrtta
<span class="cn-word" data-tr="yengil ustki kiyim">futbolka</span>,
uchta <span class="cn-word" data-tr="oyoq kiyimi ustidan kiyiladigan kiyim">shim</span>
va ikkita <span class="cn-word" data-tr="boshga kiyiladigan quyoshdan saqlovchi bosh kiyim">kepka</span>
bor edi.</p>

<p>«Toʻqqizta narsa, — dedi onasi. — 4 + 3 + 2. Ikki haftaga
yetmaydi, yana olib beraman.»</p>

<p>«Shoshmang», — dedi Sherbek.</p>

<p>U daftarni oldi va
<span class="cn-word" data-tr="tanlovlarni shoxlar bilan koʻrsatuvchi chizma">daraxt diagrammasi</span>
chiza boshladi. Har bir futbolkadan uchta shox chiqdi — har bir shim
uchun bittadan. Toʻrtta futbolka, har birida uchtadan: 4 × 3 =
<strong>12</strong>.</p>

<p>Keyin har bir shoxdan yana ikkitaga tarmoqlanadi, chunki kepka ham
ikkita: 12 × 2 = <strong>24</strong>.</p>

<p>Bu — <span class="cn-word" data-tr="bosqichlarning imkoniyatlari koʻpaytiriladi">koʻpaytirish prinsipi</span>.
Har bir <span class="cn-word" data-tr="tanlovning bir qadami">bosqich</span>
yangi koʻpaytiruvchi qoʻshadi.</p>

<p>Daraxtning oxirgi
<span class="cn-word" data-tr="daraxt diagrammasining tugallangan uchi">uch</span>larini
sanadi. «Yigirma toʻrt xil kiyinish mumkin ekan, — dedi Sherbek. — Lagerga
esa atigi 14 kun. Yetadi, hatto oʻntasi ortib ham qoladi.»</p>

<p>Onasi ishonqiramadi: «Toʻqqizta narsadan yigirma toʻrtta
<span class="cn-word" data-tr="mumkin boʻlgan bir tanlov">variant</span>
chiqadimi?»</p>

<p>«Chiqadi. Chunki har bir futbolka har bir shim bilan kiyiladi.
Siz «yo futbolka, yo shim» deb sanadingiz — men esa hammasini birga
kiyaman.»</p>

<p>Onasi bir oz oʻylab turdi. «Unda yana bitta kepka
<span class="cn-word" data-tr="pul evaziga narsa olish">xarid</span>
qilsam?»</p>

<p>Sherbek darrov hisobladi: 4 × 3 × 3 = <strong>36</strong>.</p>

<p>Bitta arzon kepka variantlar sonini yana <b>oʻn ikkitaga</b> oshirdi.
Onasi kuldi: «Demak eng foydali xarid — eng koʻp narsa bilan
<span class="cn-word" data-tr="bir nechta tanlovning birgalikdagi natijasi">kombinatsiya</span>ga
kirishadigani ekan.»</p>

<p>Sherbek jomadonni yopdi. Ichida toʻqqizta narsa bor edi — va yigirma
toʻrt kunlik reja.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-83 — ehtimollik                                 ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Tanga, zar va ob-havo bashorati",
        "summary": (
            "PM-83 matni. Ilmiy-ommabop: tanga va zarda ehtimollikni "
            "sanab topsa boʻladi, ob-havo bashoratidagi «60 foiz» esa "
            "boshqa yoʻl bilan olinadi."
        ),
        "order":   83,
        "grammar": [
            {
                "pattern":  "P = qulay hollar ÷ jami hollar",
                "meaning":  "Formula faqat hamma natija TENG IMKONIYATLI "
                            "boʻlgandagina ishlaydi. Tanga va zarda "
                            "shunday, ob-havoda esa yoʻq.",
                "examples": [
                    "tangada gerb: 1 ÷ 2 = 0,5 = 50%",
                    "zarda 6: 1 ÷ 6 ≈ 0,17",
                    "zarda juft son: 3 ÷ 6 = 0,5",
                ],
            },
        ],
        "questions": [
            {
                "text": "Zarda juft son tushish ehtimolligi qancha?",
                "choices": ["0,17", "0,5", "0,33", "3"],
                "answer": 1,
                "explanation": "Juft sonlar 2, 4 va 6 — uchta qulay hol, "
                               "jami esa oltita yoq: 3 ÷ 6 = 0,5. Bu tanga "
                               "tashlash bilan bir xil ehtimollik.",
            },
            {
                "text": "Nega ob-havo bashoratidagi «60 foiz» ni tanga kabi "
                        "sanab topib boʻlmaydi?",
                "choices": [
                    "Chunki foiz kasr bilan yozilmaydi",
                    "Chunki ob-havo har kuni oʻzgaradi",
                    "Chunki bashorat faqat taxmin",
                    "Chunki yomgʻir yogʻishi va yogʻmasligi teng "
                    "imkoniyatli emas",
                ],
                "answer": 3,
                "explanation": "P = qulay ÷ jami formulasi faqat hamma "
                               "natija teng imkoniyatli boʻlganda ishlaydi. "
                               "Tangada ikkala tomon teng, ob-havoda esa "
                               "yoʻq — shuning uchun u koʻp yillik kuzatuv "
                               "maʼlumotidan olinadi.",
            },
            {
                "text": "Ehtimollik qanday chegaralar orasida boʻladi?",
                "choices": [
                    "0 bilan 1 orasida",
                    "1 bilan 6 orasida",
                    "0 bilan 6 orasida",
                    "Chegara yoʻq",
                ],
                "answer": 0,
                "explanation": "Qulay hollar jami hollardan koʻp boʻlishi "
                               "mumkin emas, shuning uchun boʻlinma 1 dan "
                               "oshmaydi. P = 0 — imkonsiz, P = 1 — aniq.",
            },
        ],
        "body": """
<p>«Ehtimol», «boʻlishi mumkin», «aniq» — bu soʻzlarni har kuni
ishlatamiz. Matematika esa ularni <b>songa</b> aylantiradi.</p>

<p>Eng oddiy misol —
<span class="cn-word" data-tr="ikki tomonli metall pul">tanga</span>.
Uni tashlaganda ikkita
<span class="cn-word" data-tr="roʻy berishi mumkin boʻlgan hol">natija</span>
boʻladi: gerb yoki raqam. Ikkalasi ham
<span class="cn-word" data-tr="hamma natijaning imkoniyati bir xil">teng imkoniyatli</span>.
Demak gerb tushish
<span class="cn-word" data-tr="hodisaning roʻy berish imkoniyati oʻlchovi">ehtimollik</span>i:
1 ÷ 2 = <strong>0,5</strong>, yaʼni 50 foiz.</p>

<p>Endi <span class="cn-word" data-tr="olti yoqli oʻyin kubigi">zar</span>ni
olaylik. Unda oltita yoq bor va toʻgʻri yasalgan zarda hammasi teng
imkoniyatli. Olti tushish ehtimolligi: 1 ÷ 6 ≈ <strong>0,17</strong>.</p>

<p>Juft son tushishi-chi?
<span class="cn-word" data-tr="bizni qiziqtirgan natija">Qulay hollar</span>
uchta — 2, 4 va 6. Demak 3 ÷ 6 = <strong>0,5</strong>. Bu tanga bilan
bir xil ekan.</p>

<p>Har qanday ehtimollik <strong>0</strong> bilan <strong>1</strong>
orasidagi
<span class="cn-word" data-tr="0 dan 1 gacha boʻlgan oʻlchov chizigʻi">shkala</span>da
yotadi. Nol — <span class="cn-word" data-tr="hech qachon roʻy bermaydigan hodisa">imkonsiz hodisa</span>
(oddiy zarda 7 tushishi). Bir — <span class="cn-word" data-tr="har doim roʻy beradigan hodisa">aniq hodisa</span>
(zarda 6 dan katta boʻlmagan son tushishi). Javob 1 dan katta chiqsa,
hisobda xato bor.</p>

<p>Endi eng qiziq savolga oʻtamiz. Ob-havo xabarida «ertaga yomgʻir
ehtimolligi 60 foiz» deyishadi. Bu sonni qayerdan olishadi?</p>

<p>Koʻpchilik shunday
<span class="cn-word" data-tr="asossiz qilingan xulosa">taxmin</span>
qiladi: «Yo yogʻadi, yo yogʻmaydi — ikkita
natija, demak 50 foiz». Bu <b>notoʻgʻri</b>.</p>

<p>Formula faqat natijalar teng imkoniyatli boʻlgandagina ishlaydi.
Tangada ikkala tomon teng, zarda oltala yoq teng. Yomgʻir yogʻishi va
yogʻmasligi esa teng emas — choʻl ustida ular butunlay boshqacha.</p>

<p>Shuning uchun ob-havo xizmati boshqa yoʻldan boradi: ular bugungiga
oʻxshash ob-havo koʻp yillar davomida qanday tugaganini
<span class="cn-word" data-tr="oʻlchov va natijalarni yozib borish">kuzatuv</span>
maʼlumotidan qidiradi. Agar shunday kunlarning oltmish foizida yomgʻir
yoqqan boʻlsa, bashoratda 60 foiz yoziladi.</p>

<p>Bu ham ehtimollik, faqat sanab emas, <b>tajriba</b> bilan topilgan.
Uni qanday hisoblashni keyingi darsda koʻramiz.</p>

<p>Bir narsa esa oʻzgarmaydi: son qanday olinishidan qatʼi nazar, u
baribir 0 bilan 1 orasida yotadi.</p>
""",
    },
]
