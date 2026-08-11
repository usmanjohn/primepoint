# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-34 … PM-36.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 34 — kundalik daftar, 35 — ilmiy-ommabop (jadval),
36 — ilmiy-ommabop (tarix + gʻoya).
⚠️ 34-matn tocda «hikoya» deb belgilangan edi, lekin 32 va 33-matnlar ham
   hikoya boʻlgani uchun janr KUNDALIK ga oʻzgartirildi — tocning oʻz
   qoidasi: ketma-ket uchta bir xil shakl boʻlmasin.

⚠️ Kumulyativ: 34 va 35-matnlarda tenglama yechilmaydi (PM-36); 36-matnda
   nomaʼlum faqat bir tomonda (ikki tomonli tenglama PM-37 da).

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_34_36.py --author=prime
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
    # PM-34 — qavsdan chiqarish                              KUNDALIK
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Sinf sovgʻasi",
        "summary": (
            "PM-34 matni. Afsonaning kundaligi: sinf sovgʻa uchun pul yigʻadi va "
            "uzun hisob umumiy koʻpaytuvchini qavsdan chiqarish bilan bitta "
            "koʻpaytirishga aylanadi."
        ),
        "order":   34,
        "grammar": [
            {
                "pattern":  "Umumiy koʻpaytuvchini chiqarish: ab + ac = a(b + c)",
                "meaning":  "Ikkala hadda ham uchraydigan koʻpaytuvchini qavsdan "
                            "tashqariga olamiz. Bu qavs ochishning teskarisi va "
                            "koʻpincha hisobni osonlashtiradi.",
                "examples": [
                    "25a + 25b = 25(a + b)",
                    "a = 12 000, b = 8000 → 25 × 20 000 = 500 000",
                ],
            },
        ],
        "questions": [
            {
                "text": "Afsona nima uchun hisobni qayta yozdi?",
                "choices": [
                    "Birinchi hisobda xato topgani uchun",
                    "Qisqaroq va osonroq yoʻl borligini koʻrgani uchun",
                    "Oʻqituvchi shunday talab qilgani uchun",
                    "Daftarida joy qolmagani uchun",
                ],
                "answer": 1,
                "explanation": "Birinchi hisob ham toʻgʻri edi, lekin unda ikkita "
                               "koʻpaytirish bor. Umumiy koʻpaytuvchini chiqargach, "
                               "bitta koʻpaytirish yetdi.",
            },
            {
                "text": "Har bir oʻquvchi jami necha soʻmdan qoʻshdi?",
                "choices": ["8000 soʻm", "12 000 soʻm", "20 000 soʻm", "25 000 soʻm"],
                "answer": 2,
                "explanation": "Gulga 12 000 va kitobga 8000: "
                               "12 000 + 8000 = 20 000 soʻm.",
            },
            {
                "text": "25 oʻquvchi jami qancha pul yigʻdi?",
                "choices": ["200 000 soʻm", "300 000 soʻm", "480 000 soʻm",
                            "500 000 soʻm"],
                "answer": 3,
                "explanation": "25 × 20 000 = 500 000 soʻm. Uzun yoʻl ham shu javobni "
                               "beradi: 300 000 + 200 000.",
            },
        ],
        "body": """
<p><b>Payshanba, kechqurun.</b></p>

<p>Bugun sinfimizda pul yigʻdik: oʻqituvchimizning bayramiga gul va kitob olmoqchimiz.
Kassir men boʻldim, shuning uchun hisobni ham men yuritdim.</p>

<p>Kelishuvimiz shunday edi: har bir oʻquvchi gulga <strong>12 000</strong> soʻmdan,
kitobga esa <strong>8000</strong> soʻmdan qoʻshadi. Sinfimizda <strong>25</strong>
oʻquvchi bor.</p>

<p>Avval shunday hisobladim: gulga 25 × 12 000 = <strong>300 000</strong>, kitobga
25 × 8000 = <strong>200 000</strong>. Jami <strong>500 000</strong> soʻm.</p>

<p>Hisob toʻgʻri chiqdi, lekin ikkita katta
<span class="cn-word" data-tr="koʻpaytirish amali">koʻpaytirish</span> qildim va
biroz vaqt ketdi. Keyin darsda oʻtganimiz esimga tushdi.</p>

<p>Ikkala <span class="cn-word" data-tr="ifodaning qoʻshish belgilari bilan ajratilgan boʻlagi">had</span>da
ham <strong>25</strong> bor ekan. Demak uni
<span class="cn-word" data-tr="hamma hadda uchraydigan koʻpaytuvchi">umumiy koʻpaytuvchi</span>
sifatida qavsdan chiqarsam boʻlarkan: <strong>25a + 25b = 25(a + b)</strong>.</p>

<p>Shunda hisob butunlay boshqacha koʻrindi. Avval bir kishining ulushini topdim:
12 000 + 8000 = <strong>20 000</strong> soʻm. Keyin bitta koʻpaytirish:
25 × 20 000 = <strong>500 000</strong> soʻm.</p>

<p>Bitta amal — va javob oʻsha. Buni
<span class="cn-word" data-tr="umumiy koʻpaytuvchini qavsdan tashqariga olish">qavsdan chiqarish</span>
deyilarkan, u qavs ochishning
<span class="cn-word" data-tr="qarama-qarshi amal">teskarisi</span>.</p>

<p>Bugun bir narsani tushundim: matematikada «toʻgʻri javob» yetarli emas ekan. Bir xil
javobga olib boradigan yoʻllar ichida ham qisqasi bor, va uni tanlash ham
<span class="cn-word" data-tr="masalani yechishning aniq tartibi">usul</span>ning bir
qismi.</p>

<p>Ertaga gulni Nodira opa bilan tanlab kelamiz.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-35 — formula                                   ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Poyezd jadvali va tezlik",
        "summary": (
            "PM-35 matni. Ilmiy-ommabop: poyezd jadvalidagi vaqtlar va masofalar "
            "S = v·t formulasi bilan oʻqiladi, tezlik hisoblanadi va keyingi bekat "
            "vaqti oldindan aytiladi."
        ),
        "order":   35,
        "grammar": [
            {
                "pattern":  "S = v · t oilasi",
                "meaning":  "Yoʻl tezlikni vaqtga koʻpaytirganga teng. Nomaʼlum "
                            "qaysi boʻlsa, teskari amal bilan topiladi: v = S ÷ t, "
                            "t = S ÷ v. Birliklar mos boʻlishi shart.",
                "examples": [
                    "180 ÷ 2 = 90 (km/soat — tezlik)",
                    "270 ÷ 90 = 3 (soat — keyingi bekatgacha vaqt)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Jadvaldan tezlikni topish uchun nima qilish kerak?",
                "choices": [
                    "Masofani vaqtga koʻpaytirish",
                    "Masofani vaqtga boʻlish",
                    "Vaqtni masofaga boʻlish",
                    "Bekatlar sonini sanash",
                ],
                "answer": 1,
                "explanation": "v = S ÷ t. Masofa jadval yonida, vaqt esa jadvaldagi "
                               "ikki soatning ayirmasidan topiladi.",
            },
            {
                "text": "Poyezd 180 kilometrni 2 soatda bosib oʻtdi. Tezligi qancha?",
                "choices": ["60 km/soat", "90 km/soat", "180 km/soat", "360 km/soat"],
                "answer": 1,
                "explanation": "180 ÷ 2 = 90 km/soat. Tekshirish: 90 × 2 = 180 ✓",
            },
            {
                "text": "Shu tezlikda keyingi 270 kilometr necha soat oladi?",
                "choices": ["2 soat", "2,5 soat", "3 soat", "4 soat"],
                "answer": 2,
                "explanation": "270 ÷ 90 = 3 soat. Poyezd 10:15 da joʻnasa, "
                               "13:15 da yetib boradi.",
            },
        ],
        "body": """
<p>Vokzaldagi jadvalga qaraysiz: joʻnash <b>08:00</b>, birinchi bekatga yetib borish
<b>10:00</b>. Yonida masofa yozilgan: <strong>180</strong> kilometr. Shu ikki
maʼlumot bilan poyezd haqida ancha koʻp narsani bilib olsa boʻladi.</p>

<p>Avval <span class="cn-word" data-tr="harakat davom etadigan muddat">vaqt</span>ni
topamiz — bu shunchaki ikki soatning ayirmasi: 10:00 − 08:00 = <strong>2 soat</strong>.</p>

<p>Endi <span class="cn-word" data-tr="harflar bilan yozilgan doimiy qoida">formula</span>ni
ishga solamiz: <strong>S = v · t</strong>. Bizda yoʻl va vaqt bor,
<span class="cn-word" data-tr="bir soatda bosib oʻtiladigan yoʻl">tezlik</span> esa
nomaʼlum. Demak <span class="cn-word" data-tr="koʻpaytirishga qarama-qarshi amal">teskari amal</span>
kerak: <strong>v = 180 ÷ 2 = 90</strong> km/soat.</p>

<p>Jadvalda yana bir qator bor: poyezd birinchi bekatda 15 daqiqa turadi va
<b>10:15</b> da joʻnaydi. Keyingi bekatgacha <strong>270</strong> kilometr.</p>

<p>Poyezd oʻsha tezlikda yursa, bu yoʻl qancha vaqt oladi? Endi
<span class="cn-word" data-tr="bosib oʻtilgan uzunlik">masofa</span> va tezlik maʼlum:
<strong>t = 270 ÷ 90 = 3 soat</strong>. Demak poyezd <b>13:15</b> da yetib boradi —
va jadvalda ham aynan shunday yozilgan.</p>

<p>Bir narsaga eʼtibor bering: <span class="cn-word" data-tr="oʻlchov nomi: km, soat, km/soat">birlik</span>lar
mos kelishi shart. Tezlik km/soatda boʻlsa, vaqt ham soatda boʻlishi kerak. Toʻxtash
15 daqiqa edi — uni yoʻl vaqtiga qoʻshib yubormaymiz, chunki oʻsha paytda poyezd
qimirlamagan.</p>

<p>Butun yoʻlni sanasak: 180 + 270 = 450 kilometr, harakatdagi vaqt 2 + 3 = 5 soat.
450 ÷ 5 = 90 km/soat — <span class="cn-word" data-tr="butun yoʻlni butun vaqtga boʻlgandagi tezlik">oʻrtacha tezlik</span>
ham oʻsha chiqdi, chunki poyezd tezligini oʻzgartirmadi.</p>

<p>Jadval — bu shunchaki sonlar roʻyxati emas. Uni oʻqishni bilsangiz, u sizga
poyezdning qayerda ekanini istalgan daqiqada aytib beradi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-36 — tenglama                                  ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Tarozi muvozanati",
        "summary": (
            "PM-36 matni. Ilmiy-ommabop: ikki pallali tarozi — tenglamaning eng "
            "qadimgi surati. «Algebra» soʻzining oʻzi ham shu muvozanat gʻoyasidan "
            "kelib chiqqan (tarixiy maʼlumot haqiqiy)."
        ),
        "order":   36,
        "grammar": [
            {
                "pattern":  "Muvozanat qoidasi: ikki tomonga bir xil amal",
                "meaning":  "Tenglamaning ikki tomoni teng. Bir tomondan biror "
                            "miqdorni olsak, ikkinchisidan ham xuddi shuncha olamiz "
                            "— shunda tenglik saqlanadi va nomaʼlum yolgʻiz qoladi.",
                "examples": [
                    "x + 3 = 12 → x + 3 − 3 = 12 − 3 → x = 9",
                    "3x = 27 → x = 27 ÷ 3 = 9 (tekshirish: 3 × 9 = 27)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Matnga koʻra, tarozi tenglamani qanday tushuntiradi?",
                "choices": [
                    "Ikki palla teng boʻlsa, ular bir xil ogʻirlikni bildiradi",
                    "Tarozi har doim ogʻir tomonga qarab ogʻadi",
                    "Tarozi faqat ogʻirlikni oʻlchaydi, hisobga aloqasi yoʻq",
                    "Tarozida faqat butun sonlar boʻladi",
                ],
                "answer": 0,
                "explanation": "Muvozanatdagi tarozi ikki tomon tengligini "
                               "koʻrsatadi — tenglama ham aynan shuni yozadi.",
            },
            {
                "text": "Chap pallada sandiq va 3 kg tosh, oʻng pallada 12 kg bor. "
                        "Sandiq necha kilogramm?",
                "choices": ["3 kg", "4 kg", "9 kg", "15 kg"],
                "answer": 2,
                "explanation": "x + 3 = 12; ikki tomondan 3 ni olamiz: x = 9 kg. "
                               "Tekshirish: 9 + 3 = 12 ✓",
            },
            {
                "text": "Xuddi shunday uchta sandiq qoʻyilsa, tarozining oʻng "
                        "pallasida necha kilogramm boʻlishi kerak?",
                "choices": ["12 kg", "18 kg", "27 kg", "36 kg"],
                "answer": 2,
                "explanation": "Har biri 9 kg dan uchta sandiq: 3 × 9 = 27 kg.",
            },
        ],
        "body": """
<p>Ikki pallali tarozi — insoniyat oʻylab topgan eng qadimgi asboblardan biri. Undan
Misrda ham, Mesopotamiyada ham ming yillar oldin foydalanishgan. Va u, aslida,
matematikaning bir butun boʻlimini tushuntirib beradi.</p>

<p>Tasavvur qiling: chap pallada nomaʼlum ogʻirlikdagi sandiq va yonida
<strong>3</strong> kilogramm tosh turibdi. Oʻng pallada <strong>12</strong> kilogramm
tosh. Tarozi tinch — ikki tomon <span class="cn-word" data-tr="ikki tomonning tengligi">muvozanat</span>da.</p>

<p>Buni yozib qoʻysak, <span class="cn-word" data-tr="ikki ifoda tenglik bilan bogʻlangan yozuv">tenglama</span>
hosil boʻladi: <strong>x + 3 = 12</strong>.</p>

<p>Sandiqning ogʻirligini bilish uchun uni <span class="cn-word" data-tr="nomaʼlumni bir tomonda yolgʻiz qoldirish">yolgʻizlash</span> kerak. Chap palladagi
3 kilogrammni olib tashlaymiz. Lekin shunda tarozi ogʻadi! Muvozanatni saqlash uchun
<b>oʻng palladan ham</b> 3 kilogrammni olamiz.</p>

<p>Qoladi: <strong>x = 9</strong>. Sandiq toʻqqiz kilogramm ekan. Tekshirish oson —
9 + 3 = 12 ✓</p>

<p>Mana shu <span class="cn-word" data-tr="ikki tomonga bir xil amal qilish qoidasi">muvozanat qoidasi</span>
butun algebraning asosi. Ikki tomonga bir xil amal qilsangiz, tenglik buzilmaydi.</p>

<p>Qizigʻi shundaki, «algebra» soʻzining oʻzi ham shu gʻoyadan kelib chiqqan.
Al-Xorazmiyning kitobi <i>«Al-jabr va al-muqobala»</i> deb atalgan. <b>Al-jabr</b> —
«tiklash», yaʼni ikki tomonga bir xil miqdor qoʻshib tenglikni tiklash;
<b>al-muqobala</b> esa «qiyoslash», ikki tomondagi bir xil hadlarni yoʻqotish.
Ming yildan keyin ham biz aynan shu ikki ishni qilyapmiz.</p>

<p>Endi tarozida uchta bir xil sandiq turibdi va oʻng pallada 27 kilogramm bor:
<strong>3x = 27</strong>. Bu safar qoʻshish emas,
<span class="cn-word" data-tr="koʻpaytma koʻrinishidagi bogʻlanish">koʻpaytirish</span>
bor — demak <span class="cn-word" data-tr="koʻpaytirishga qarama-qarshi amal">teskari amal</span>
ham boshqa: ikki tomonni 3 ga boʻlamiz va yana <strong>x = 9</strong> chiqadi.</p>

<p>Tarozi endi bozorlarda kamdan-kam uchraydi. Lekin uning gʻoyasi har bir tenglamada
yashab qolgan.</p>
""",
    },
]
