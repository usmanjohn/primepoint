# -*- coding: utf-8 -*-
"""Matematika olami — 25-matn: Shtrix-koddagi oxirgi raqam nima uchun kerak.

Toc: corner/management/commands/toc_matematika_olami.txt
Kundalik hayotdagi matematika oilasidan — darsga bogʻlanmagan mustaqil matn.
⛔ AUDIO YOʻQ.

Faktlar: EAN-13 shtrix-kodi 13 ta raqamdan iborat; oxirgisi — nazorat raqami.
Hisob: 1-, 3-, 5-… oʻrindagi raqamlar 1 ga, 2-, 4-, 6-… oʻrindagilar 3 ga
koʻpaytiriladi; yigʻindi keyingi oʻnlikkacha toʻldiriladi. 476 — Oʻzbekiston
uchun GS1 prefiksi. Misoldagi 4761234567894 kodi shu qoida bilan
hisoblangan (verify_pm_25_27_olami.py bilan tekshirilgan).

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_11.py --author=prime
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
    {
        "title":   "Shtrix-koddagi oxirgi raqam nima uchun kerak",
        "summary": (
            "Har bir mahsulot yorligʻidagi 13 raqamning oxirgisi tasodifiy emas — u "
            "qolgan oʻn ikkitasidan hisoblanadi va kassa xato oʻqiganini shu raqam "
            "fosh qiladi."
        ),
        "order":   25,
        "grammar": [
            {
                "pattern":  "Nazorat raqami: 1 va 3 ga koʻpaytirib qoʻshish",
                "meaning":  "Birinchi 12 raqam navbatma-navbat 1 ga va 3 ga "
                            "koʻpaytiriladi, hammasi qoʻshiladi. Yigʻindini keyingi "
                            "oʻnlikkacha toʻldiradigan son — nazorat raqami.",
                "examples": [
                    "476123456789 → toq oʻrinlar: 4+6+2+4+6+8 = 30",
                    "juft oʻrinlar: (7+1+3+5+7+9) × 3 = 96; jami 126 → 130 − 126 = 4",
                ],
            },
        ],
        "questions": [
            {
                "text": "Shtrix-kodning oxirgi raqami nima uchun qoʻyilgan?",
                "choices": [
                    "Mahsulot narxini bildirish uchun",
                    "Kod xato oʻqilganini darrov aniqlash uchun",
                    "Ishlab chiqarilgan yilni koʻrsatish uchun",
                    "Mahsulot ogʻirligini yozib qoʻyish uchun",
                ],
                "answer": 1,
                "explanation": "U nazorat raqami: qolgan oʻn ikki raqamdan "
                               "hisoblanadi, shuning uchun bittasi notoʻgʻri oʻqilsa "
                               "hisob mos kelmay qoladi.",
            },
            {
                "text": "Matndagi kodda juft oʻrindagi raqamlar yigʻindisi 32 edi. Uni "
                        "3 ga koʻpaytirsak nechchi boʻladi?",
                "choices": ["35", "64", "96", "128"],
                "answer": 2,
                "explanation": "32 × 3 = 96. Toq oʻrinlardagi 30 bilan qoʻshilsa, "
                               "jami 126 chiqadi.",
            },
            {
                "text": "Yigʻindi 126 boʻlsa, nazorat raqami nechchi boʻladi?",
                "choices": ["2", "4", "6", "26"],
                "answer": 1,
                "explanation": "126 dan keyingi oʻnlik — 130. 130 − 126 = 4, demak "
                               "nazorat raqami 4.",
            },
        ],
        "body": """
<p>Kassir mahsulotni skanerga tutadi, «bip» degan ovoz chiqadi va ekranda nom paydo
boʻladi. Skaner chiziqlarni oʻqidi. Lekin u <b>notoʻgʻri</b> oʻqigan boʻlsa-chi?</p>

<p>Yorliqdagi <span class="cn-word" data-tr="mahsulotni raqamlar bilan belgilaydigan chiziqli belgi">shtrix-kod</span>
odatda 13 ta raqamdan iborat. Dastlabki uchtasi mamlakatni bildiradi —
Oʻzbekiston uchun bu <strong>476</strong>. Keyingilari ishlab chiqaruvchini va
mahsulotni koʻrsatadi.</p>

<p>Eng oxirgi raqam esa boshqacha. U hech qanday maʼlumot bermaydi:
<span class="cn-word" data-tr="qolgan raqamlardan hisoblanadigan tekshiruvchi raqam">nazorat raqami</span>
deyiladi va qolgan oʻn ikkitasidan <b>hisoblab chiqariladi</b>.</p>

<p>Hisob juda oddiy. Raqamlar navbatma-navbat 1 ga va 3 ga koʻpaytiriladi, keyin
hammasi qoʻshiladi. <strong>476123456789</strong> kodini olaylik:
<span class="cn-word" data-tr="1-, 3-, 5-… oʻrinlarda turgan raqamlar">toq oʻrin</span>dagilar
4 + 6 + 2 + 4 + 6 + 8 = <strong>30</strong>;
<span class="cn-word" data-tr="2-, 4-, 6-… oʻrinlarda turgan raqamlar">juft oʻrin</span>dagilar
esa (7 + 1 + 3 + 5 + 7 + 9) × 3 = <strong>96</strong>.</p>

<p>Jami <strong>126</strong>. Endi bu sonni keyingi
<span class="cn-word" data-tr="10 ga karrali son: 10, 20, 30…">oʻnlik</span>kacha
toʻldiramiz: 130 − 126 = <strong>4</strong>. Demak toʻliq kod —
<strong>4761234567894</strong>.</p>

<p>Endi eng qizigʻi. Agar skaner bitta raqamni xato oʻqisa,
<span class="cn-word" data-tr="qoʻshish natijasi">yigʻindi</span> oʻzgaradi va nazorat
raqami boshqa chiqadi. Kompyuter buni bir zumda sezadi va «bip» oʻrniga xato beradi.</p>

<p>Shu bitta raqam tufayli notoʻgʻri narx, adashgan mahsulot va yoʻqolgan buyurtma
kamayadi. Ayniqsa <span class="cn-word" data-tr="ikki raqamning oʻrni almashib ketishi">oʻrin almashish</span> xatosi — 45 oʻrniga 54 yozilishi — koʻp uchraydi va nazorat raqami uni ham tutadi, chunki toq va juft oʻrinlar har xil koʻpaytiriladi. Xuddi shunday
<span class="cn-word" data-tr="xatoni oʻzi fosh qiladigan raqamlar tizimi">nazorat tizimi</span>
bank kartalarida ham, pasport raqamlarida ham ishlaydi.</p>

<p>Yorliqdagi chiziqlarning qalin-ingichkaligi ham tasodifiy emas: ular oʻsha raqamlarning <span class="cn-word" data-tr="raqamlarni chiziq yoki belgiga aylantirish">yozuv</span>i, skaner esa ularni qaytadan raqamga aylantiradi.</p>

<p>Kassadagi «bip» — bu, aslida, bir necha
<span class="cn-word" data-tr="qoʻshish va koʻpaytirish kabi hisob amallari">amal</span>ning
tovushi.</p>
""",
    },
]
