# -*- coding: utf-8 -*-
"""Matematika olami — 4, 6 va 33-matnlar.

Toc: corner/management/commands/toc_matematika_olami.txt
  4.  Mirzo Ulugʻbek rasadxonasi        (buyuk matematiklar)
  6.  Fales va piramidaning soyasi       (buyuk matematiklar)
  33. Oʻn ikki tanga va uch marta tortish (jumboq)
⛔ AUDIO YOʻQ.

FAKTLAR (tekshirilgan):
  • Mirzo Ulugʻbek 1394–1449. Samarqanddagi rasadxona qurilishi 1424-yilda
    boshlangan. Asosiy asbob — Fahriy sekstanti, radiusi taxminan 40 metr,
    yer ostidagi xandaqqa qurilgan. «Ziji jadidi Koʻragoniy» katalogida
    1018 ta yulduz. Yulduz yilining uzunligi 365 kun 6 soat 10 daqiqa
    8 sekund deb oʻlchangan; hozirgi qiymat 365 kun 6 soat 9 daqiqa
    ~10 sekund — farq 58 sekund, yaʼni bir daqiqadan kam. Rasadxona
    xarobalarini 1908-yilda V. L. Vyatkin topgan.
  • Fales (miloddan avvalgi ~624–546) — yunon faylasufi. Piramidani soya
    orqali oʻlchagani RIVOYAT (Diogen Laertskiy va Plutarx qaydlari),
    shuning uchun matnda «rivoyatga koʻra» deb aytilgan. Buyuk piramidaning
    dastlabki balandligi ~146,6 metr. Matndagi hisob: 195 × 1,8 ÷ 2,4 =
    146,25 metr.
  • 12 tanga jumbogʻi: 3 tortish 3^3 = 27 xil natija beradi; 12 tanga uchun
    24 ta holat (har biri ogʻir yoki yengil boʻlishi mumkin) — sigʻadi.
    14 tanga uchun 28 ta holat — sigʻmaydi.

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_13_15.py --author=prime
"""

SUBJECT = {
    "name":    "Matematika",
    "summary": "Matematika: hayotdagi matnlar, atamalar va matematik hikoyalar.",
    "icon":    "bi-calculator",
    "color":   "#f59e0b",
    "order":   7,
}

COLLECTION = {
    "title":       "Matematika olami",
    "description": (
        "Buyuk matematiklar, tabiatdagi matematika, kundalik hayotdagi hisob va "
        "jumboqlar. Darsga bogʻlanmagan — shunchaki qiziqarli oʻqish uchun."
    ),
    "order": 2,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # 4 — Mirzo Ulugʻbek rasadxonasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ulugʻbek bir yilning uzunligini qanday oʻlchagan",
        "summary": (
            "Haqiqiy voqea: Samarqand rasadxonasida oʻlchangan yil uzunligi hozirgi "
            "qiymatdan atigi 58 sekundga farq qiladi. Teleskopsiz — faqat ulkan "
            "yoy, sabr va matematika bilan."
        ),
        "order":   4,
        "grammar": [
            {
                "pattern":  "Aniqlikni farq bilan oʻlchash",
                "meaning":  "Ikki oʻlchov qanchalik yaqinligini bilish uchun ularni "
                            "bir xil birlikka keltirib ayiramiz. Sekundlarda "
                            "ishlansa, «bir daqiqadan kam» degan baho aniq songa "
                            "aylanadi.",
                "examples": [
                    "6 soat 10 daqiqa 8 sekund − 6 soat 9 daqiqa 10 sekund",
                    "10 daq 8 sek = 608 sek; 9 daq 10 sek = 550 sek; farq 58 sekund",
                ],
            },
        ],
        "questions": [
            {
                "text": "Ulugʻbekning rasadxonasidagi asosiy asbob nima edi?",
                "choices": [
                    "Katta teleskop",
                    "Suv soati",
                    "Kattalashtiruvchi oyna",
                    "Yer ostiga qurilgan ulkan yoy — sekstant",
                ],
                "answer": 3,
                "explanation": "Fahriy sekstanti — radiusi taxminan 40 metr boʻlgan "
                               "yoy. U yer ostidagi xandaqqa qurilgan, chunki asbob "
                               "qancha katta boʻlsa, burchak shuncha aniq "
                               "oʻlchanadi.",
            },
            {
                "text": "Ulugʻbek 6 soat 10 daqiqa 8 sekund deb oʻlchagan, hozirgi "
                        "qiymat esa 6 soat 9 daqiqa 10 sekund. Farq necha sekund?",
                "choices": ["18 sekund", "58 sekund", "62 sekund", "108 sekund"],
                "answer": 1,
                "explanation": "Daqiqalarni sekundga aylantiramiz: 608 − 550 = 58 "
                               "sekund. Bir yilning uzunligida bir daqiqadan kam "
                               "xatolik.",
            },
            {
                "text": "Nima uchun asbobni katta qilib qurish aniqlikni oshiradi?",
                "choices": [
                    "Katta asbob ogʻirroq va shamolda qimirlamaydi",
                    "Katta asbobni koʻproq odam koʻra oladi",
                    "Yoy uzun boʻlsa, bir gradus ham uzunroq boʻladi va uni "
                    "maydaroq boʻlaklarga boʻlish mumkin",
                    "Kattaligi yulduzlarni yaqinlashtiradi",
                ],
                "answer": 2,
                "explanation": "Radius katta boʻlsa, yoydagi bir gradusga toʻgʻri "
                               "keladigan masofa ham katta boʻladi — demak uni "
                               "daqiqa va sekundlarga boʻlib belgilash mumkin.",
            },
        ],
        "body": """
<p>Bir yil necha kun davom etadi? «365 kun» degan javob taxminiy. Aniq javobni bilish
uchun butun boshli rasadxona kerak — va olti asr oldin Samarqandda aynan shunday
rasadxona qurilgan edi.</p>

<p><b>Mirzo Ulugʻbek</b> (1394–1449) Amir Temurning nabirasi edi. U 1424-yilda Samarqandda <span class="cn-word" data-tr="osmon jismlarini kuzatish uchun qurilgan bino">rasadxona</span> qurishni boshladi — u yerda <span class="cn-word" data-tr="osmon jismlarini oʻrganadigan fan">astronomiya</span> bilan shugʻullanadigan olimlar toʻplandi.</p>

<p>Uning asosiy asbobi hayratlanarli edi: <b>Fahriy sekstanti</b> — radiusi taxminan
<strong>40 metr</strong> boʻlgan ulkan yoy. U yer ustiga emas, maxsus qazilgan
xandaqqa qurilgan, chunki bunday balandlikdagi asbobni shamol qimirlatib
yuborardi.</p>

<p>Nega bunchalik katta? Bu yerda sof matematika bor. Yoyning
<span class="cn-word" data-tr="markazdan yoygacha boʻlgan masofa">radius</span>i qancha
katta boʻlsa, undagi bir <span class="cn-word" data-tr="burchak oʻlchov birligi">gradus</span>ga
toʻgʻri keladigan masofa ham shuncha uzun boʻladi. Uzun boʻlagni esa daqiqa va
sekundlarga boʻlib belgilash mumkin. Kattalik — bu
<span class="cn-word" data-tr="oʻlchovning haqiqatga yaqinlik darajasi">aniqlik</span>
degani edi.</p>

<p>Ulugʻbek va uning olimlari oʻn yillar davomida osmonni kuzatishdi. Natijada
<i>«Ziji jadidi Koʻragoniy»</i> — <strong>1018</strong> ta yulduzning oʻrni yozilgan
<span class="cn-word" data-tr="tartib bilan tuzilgan roʻyxat">katalog</span> tuzildi.
U ikki asr davomida dunyodagi eng aniq jadval boʻlib qoldi.</p>

<p>Eng hayratlanarlisi — yulduz yilining uzunligi. Ulugʻbek uni <strong>365 kun
6 soat 10 daqiqa 8 sekund</strong> deb oʻlchagan. Hozirgi qiymat — 365 kun 6 soat
9 daqiqa 10 sekund atrofida.</p>

<p><span class="cn-word" data-tr="ikki qiymat orasidagi ayirma">Farq</span>ni
hisoblaymiz: 10 daqiqa 8 sekund — bu 608 sekund, 9 daqiqa 10 sekund — 550 sekund.
Ayirma <strong>58 sekund</strong>. Butun bir yilning uzunligida bir daqiqadan kam
<span class="cn-word" data-tr="haqiqiy qiymatdan chetlanish">xatolik</span>.</p>

<p>Rasadxona keyinchalik vayron boʻldi va uzoq vaqt uning oʻrni ham unutildi.
Faqat 1908-yilda arxeolog V. L. Vyatkin sekstantning yer ostida saqlanib qolgan
qismini topdi. U bugun ham oʻsha yerda turibdi.</p>

<p>Teleskop hali ixtiro qilinmagan edi. Bor-yoʻgʻi bitta ulkan yoy, koʻp yillik sabr
va yaxshi matematika.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 6 — Fales va piramidaning soyasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Fales piramidani soyasi bilan oʻlchagan",
        "summary": (
            "Rivoyatga koʻra, yunon olimi Fales Misr piramidasining balandligini "
            "unga tegmasdan topgan. Butun sir — bir vaqtda tushgan soyalar bir xil "
            "nisbatda boʻlishida."
        ),
        "order":   6,
        "grammar": [
            {
                "pattern":  "Soyalar nisbati = balandliklar nisbati",
                "meaning":  "Quyosh bir vaqtning oʻzida hamma narsaga bir xil "
                            "burchak ostida tushadi. Shuning uchun narsaning "
                            "balandligi va soyasining uzunligi doim bir xil "
                            "nisbatda boʻladi.",
                "examples": [
                    "Odam 1,8 m, soyasi 2,4 m → nisbat 1,8 : 2,4 = 3 : 4",
                    "Piramida soyasi 195 m → balandligi 195 × 3 ÷ 4 = 146,25 m",
                ],
            },
        ],
        "questions": [
            {
                "text": "Fales piramidaning balandligini qanday topgan?",
                "choices": [
                    "Oʻz boʻyi va soyasi nisbatidan foydalangan",
                    "Piramidaga chiqib, arqon bilan oʻlchagan",
                    "Qurilish yozuvlarini oʻqigan",
                    "Piramidaning tomonini sanagan",
                ],
                "answer": 0,
                "explanation": "U oʻz boʻyi bilan soyasining nisbatini oʻlchagan va "
                               "oʻsha nisbat piramida uchun ham oʻrinli ekanidan "
                               "foydalangan.",
            },
            {
                "text": "Odamning boʻyi 1,8 m, soyasi 2,4 m. Soya balandlikdan necha "
                        "marta uzun?",
                "choices": [
                    "Soya balandlikdan 2 marta uzun",
                    "Ular teng",
                    "Soya balandlikning uchdan bir qismi",
                    "Balandlik soyaning 3/4 qismi — har 4 metr soyaga 3 metr "
                    "balandlik",
                ],
                "answer": 3,
                "explanation": "1,8 : 2,4 = 3 : 4. Demak balandlik soyaning uchdan "
                               "toʻrt qismi: har 4 metr soyaga 3 metr balandlik.",
            },
            {
                "text": "Piramidaning soyasi 195 metr boʻlsa, balandligi qancha?",
                "choices": ["130 metr", "146,25 metr", "195 metr", "260 metr"],
                "answer": 1,
                "explanation": "195 × 3 ÷ 4 = 146,25 metr. Buyuk piramidaning "
                               "haqiqiy dastlabki balandligi ~146,6 metr — "
                               "hisob juda yaqin chiqdi.",
            },
        ],
        "body": """
<p>Miloddan avvalgi VI asr. Yunon olimi <b>Fales</b> Misrga keladi va piramidalarni
koʻradi. Unga savol berishadi: bu ulkan <span class="cn-word" data-tr="toʻrt yoqli, uchi choʻqqiga tomon torayadigan qadimiy inshoot">piramida</span> qanchalik baland?</p>

<p>Oʻsha davrda buni oʻlchashning yoʻli yoʻq edi. Piramidaga chiqib boʻlmaydi, ichida
oʻlchov oʻtkazib ham boʻlmaydi.</p>

<p><b>Rivoyatga koʻra</b>, Fales kutdi. U qumga tayoq qadab, oʻz
<span class="cn-word" data-tr="quyosh nuri toʻsilganda hosil boʻladigan qorongʻi iz">soya</span>sini
kuzatdi. Keyin bitta oddiy narsani aytdi: quyosh hozir hamma narsaga <b>bir xil
burchak</b> ostida tushyapti — menga ham, piramidaga ham.</p>

<p>Demak, balandlik va soya orasidagi
<span class="cn-word" data-tr="ikki miqdor orasidagi munosabat">nisbat</span> har
ikkalasida bir xil boʻlishi kerak.</p>

<p>Faraz qilaylik, Falesning boʻyi <strong>1,8</strong> metr, soyasi esa
<strong>2,4</strong> metr edi. Nisbatni <span class="cn-word" data-tr="nisbatdagi sonlarni bir xil songa boʻlish">qisqartir</span>sak,
<strong>3 : 4</strong> chiqadi — yaʼni har toʻrt metr soyaga uch metr balandlik
toʻgʻri keladi.</p>

<p>Keyin u piramidaning soyasini <span class="cn-word" data-tr="uzunlik yoki miqdorni aniqlash">oʻlchadi</span> — aytaylik, <strong>195</strong> metr.
Endi shu nisbatni qoʻllash kifoya: <strong>195 × 3 ÷ 4 = 146,25</strong> metr.</p>

<p>Buyuk piramidaning haqiqiy dastlabki
<span class="cn-word" data-tr="yer sathidan choʻqqigacha boʻlgan masofa">balandlik</span>i
taxminan <strong>146,6</strong> metr boʻlgan. Ikki mingdan ortiq yil oldin, faqat
soya va <span class="cn-word" data-tr="ikki teng nisbatning tengligi">proporsiya</span>
bilan — deyarli aniq javob.</p>

<p>Bu voqea haqiqatan boʻlganmi yoki keyin toʻqilganmi — tarixchilar bahslashadi.
Uni bizga Diogen Laertskiy va Plutarx yozib qoldirgan, yaʼni voqeadan ancha keyin.
Lekin <span class="cn-word" data-tr="masalani yechishning aniq tartibi">usul</span>ning
oʻzi mutlaqo haqiqiy va u bugun ham ishlaydi.</p>

<p>Ertaga quyoshli kunda sinab koʻring: oʻz boʻyingiz va soyangizni oʻlchang, keyin
maktab binosining soyasini. Binoning balandligini bir daqiqada bilib olasiz — unga
yaqinlashmasdan ham.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 33 — oʻn ikki tanga va uch marta tortish
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Oʻn ikki tanga va uch marta tortish",
        "summary": (
            "Mashhur jumboq: oʻn ikki tangadan biri qalbaki, lekin ogʻirmi yoki "
            "yengilmi — nomaʼlum. Tarozidan atigi uch marta foydalanib uni topish "
            "mumkinmi? Yechim gʻoyasi qoida blokida."
        ),
        "order":   33,
        "grammar": [
            {
                "pattern":  "Yechim gʻoyasi: 3 tortish = 27 xil natija",
                "meaning":  "Har bir tortishning uchta natijasi bor: chap ogʻir, "
                            "oʻng ogʻir, muvozanat. Uch tortish 3 × 3 × 3 = 27 xil "
                            "natija beradi. 12 tanganing har biri ogʻir yoki yengil "
                            "boʻlishi mumkin — 24 holat. 24 < 27, demak yetadi.",
                "examples": [
                    "1-tortish: 4 tanga va 4 tanga. Muvozanat boʻlsa — qalbaki "
                    "chetdagi 4 tada; boʻlmasa — tarozidagi 8 ta ichida",
                    "14 tanga uchun 28 holat kerak boʻlardi — 27 dan koʻp, demak "
                    "uch tortish yetmaydi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nima uchun bu jumboq oddiy «qalbaki yengil» masaladan "
                        "qiyinroq?",
                "choices": [
                    "Tangalar juda kichkina boʻlgani uchun",
                    "Qalbaki tanga ogʻirmi yoki yengilmi — bilinmagani uchun",
                    "Tarozi aniq ishlamagani uchun",
                    "Tangalar soni juft boʻlgani uchun",
                ],
                "answer": 1,
                "explanation": "Yoʻnalish nomaʼlum boʻlgani uchun har tanga uchun "
                               "ikkita holat bor — jami 24 ta, 12 ta emas.",
            },
            {
                "text": "Uch marta tortish jami nechta xil natija berishi mumkin?",
                "choices": ["9", "12", "24", "27"],
                "answer": 3,
                "explanation": "Har tortishda 3 xil natija bor (chap ogʻir, oʻng "
                               "ogʻir, muvozanat): 3 × 3 × 3 = 27.",
            },
            {
                "text": "Nima uchun 14 tanga bilan uch tortish yetmaydi?",
                "choices": [
                    "14 juft son boʻlgani uchun",
                    "14 ta tangani tarozi koʻtarmaydi",
                    "28 ta holat kerak, tortishlar esa 27 ta natija beradi",
                    "Toʻrt marta tortish har doim kerak",
                ],
                "answer": 2,
                "explanation": "14 × 2 = 28 ta holat. Uch tortish esa faqat 27 xil "
                               "natija ajrata oladi, shuning uchun bittasi "
                               "aniqlanmay qoladi.",
            },
        ],
        "body": """
<p>Stolda <strong>12</strong> ta bir xil koʻrinishdagi tanga yotibdi. Ulardan bittasi
<span class="cn-word" data-tr="soxta, haqiqiy emas">qalbaki</span>: uning <span class="cn-word" data-tr="narsaning tarozidagi kattaligi">ogʻirlik</span>i boshqalarnikidan farq qiladi. Ammo qanday farq
qilishi — <b>ogʻirroqmi yoki yengilroqmi</b> — nomaʼlum.</p>

<p>Qoʻlingizda ikki pallali <span class="cn-word" data-tr="ikki pallali oʻlchov asbobi">tarozi</span>
bor. U son koʻrsatmaydi, faqat qaysi palla ogʻirligini aytadi. Undan
<b>atigi uch marta</b> foydalanishingiz mumkin.</p>

<p>Qalbaki tangani topa olasizmi? Oʻylab koʻring — davomini keyin oʻqing.</p>

<p>Koʻpchilik tangalarni ikkiga boʻlishdan boshlaydi: 6 ta va 6 ta. Bu yomon
boshlanish, chunki tarozi albatta ogʻadi va sizga hech qanday yangi maʼlumot
bermaydi — qaysi tomon ogʻir ekani qalbaki tanganing ogʻirmi yoki yengilligiga ham
bogʻliq.</p>

<p>Yaxshi boshlanish — <strong>4 ta va 4 ta</strong>, qolgan 4 tasi chetda. Endi
ikki natijadan biri boʻladi. <b>Muvozanat</b> boʻlsa, qalbaki tanga chetdagi
toʻrttaning ichida. <b>Ogʻsa</b> — u tarozidagi sakkiztaning ichida, ustiga qaysi
tomon ogʻirligini ham bilib olasiz.</p>

<p>Har ikkala holatda ham <span class="cn-word" data-tr="javob izlanadigan variantlar toʻplami">qidiruv maydoni</span> keskin qisqaradi. Qolgan ikki tortishni
xuddi shunday puxta oʻylab tuzsangiz, jumboq yechiladi.</p>

<p>Lekin eng chiroyli qismi boshqa: <b>yechim borligini oldindan bilish mumkin</b>.
Har bir tortishning uchta natijasi bor — chap ogʻir, oʻng ogʻir yoki muvozanat.
Demak uch tortish jami <strong>3 × 3 × 3 = 27</strong> xil
<span class="cn-word" data-tr="tortishdan chiqishi mumkin boʻlgan xulosa">natija</span>
bera oladi.</p>

<p>Bizga nechta kerak? 12 tanganing har biri ogʻir yoki yengil boʻlishi mumkin —
<strong>24</strong> ta <span class="cn-word" data-tr="boʻlishi mumkin boʻlgan vaziyat">holat</span>.
24 son 27 dan kichik, demak <span class="cn-word" data-tr="tortishlar bergan xabar miqdori">maʼlumot</span>
yetadi.</p>

<p>Endi 14 ta tanga bilan sinab koʻring: 14 × 2 = 28 ta holat kerak boʻladi, tortish
esa baribir 27 ta natija beradi. Yechim <b>mavjud emas</b> — buni bitta tortish ham
qilmasdan aytish mumkin.</p>

<p>Mana shu matematikaning eng kuchli tomonlaridan biri: u masalani yechishdan oldin
uning <span class="cn-word" data-tr="masala umuman yechilishi mumkinligi">yechilishi</span>
haqida gapira oladi.</p>
""",
    },
]
