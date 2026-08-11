# -*- coding: utf-8 -*-
"""Matematika olami — 27-matn: Gazetadagi diagrammaga nega ishonmaslik kerak.

Toc: corner/management/commands/toc_matematika_olami.txt
Kundalik hayotdagi matematika oilasidan — darsga bogʻlanmagan mustaqil matn.
PM-25/PM-26 foiz bloki yonida yaxshi oʻqiladi, lekin darsga bogʻlanmagan.
⛔ AUDIO YOʻQ.

Arifmetika: 240 → 252 sotuv, oʻsish 12 dona = 5%. Diagrammada oʻq 235 dan
boshlansa, ustunlarning koʻrinadigan qismi 5 va 17 birlik boʻladi —
17 ÷ 5 = 3,4 barobar. Ikkinchi misol: 40% va 44% ulush, farqi 4 punkt.

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_12.py --author=prime
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
        "title":   "Gazetadagi diagrammaga nega ishonmaslik kerak",
        "summary": (
            "Bitta va oʻsha maʼlumot ikki xil diagrammada butunlay boshqacha "
            "koʻrinishi mumkin. Oʻqning qayerdan boshlangani va foizning asosi — "
            "eng koʻp ishlatiladigan ikki hiyla."
        ),
        "order":   27,
        "grammar": [
            {
                "pattern":  "Diagrammani oʻqishdan oldin oʻqni tekshiring",
                "meaning":  "Ustunlarning balandligi faqat vertikal oʻq NOLDAN "
                            "boshlanganda haqiqiy nisbatni koʻrsatadi. Oʻq boshqa "
                            "sondan boshlansa, kichkina farq katta koʻrinadi.",
                "examples": [
                    "240 → 252: oʻsish 12 dona, yaʼni 12 ÷ 240 = 5%",
                    "oʻq 235 dan boshlansa: 5 va 17 birlik — 3,4 barobar farq koʻrinadi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Matnga koʻra, diagramma qanday qilib aldashi mumkin?",
                "choices": [
                    "Ustunlarga notoʻgʻri sonlar yozib qoʻyiladi",
                    "Vertikal oʻq noldan emas, boshqa sondan boshlanadi",
                    "Ustunlar rangi juda yorqin tanlanadi",
                    "Diagramma juda kichik chop etiladi",
                ],
                "answer": 1,
                "explanation": "Sonlar toʻgʻri boʻlishi mumkin. Oʻq 235 dan "
                               "boshlansa, koʻzga 3 barobardan koʻproq oʻsish "
                               "koʻrinadi, aslida esa oʻsish atigi 5 foiz.",
            },
            {
                "text": "Sotuv 240 tadan 252 taga chiqdi. Bu necha foizga oʻsish?",
                "choices": ["5 foiz", "10 foiz", "12 foiz", "17 foiz"],
                "answer": 0,
                "explanation": "Oʻzgarish 12 ta; asos — eski son 240: "
                               "12 ÷ 240 = 0,05, yaʼni 5 foiz.",
            },
            {
                "text": "Ikki firmaning ulushi 40 va 44 foiz. Farq qancha?",
                "choices": [
                    "4 foiz punkti — «ikki barobar» degani emas",
                    "4 barobar",
                    "44 foiz",
                    "Farqni aniqlab boʻlmaydi",
                ],
                "answer": 0,
                "explanation": "44 − 40 = 4 foiz punkti. Diagrammada ustunlar ikki "
                               "barobar farq qilib koʻrinishi mumkin, lekin sonlar "
                               "juda yaqin.",
            },
        ],
        "body": """
<p>Gazetada diagramma chiqdi: ikki ustun, biri ikkinchisidan uch barobar baland.
Sarlavha: «Sotuvlar keskin oʻsdi». Koʻz ishonadi — chunki koʻz sonlarni emas,
<span class="cn-word" data-tr="ustun yoki chiziqning koʻzga koʻrinadigan uzunligi">balandlik</span>ni
oʻqiydi.</p>

<p>Ustunlarning ustidagi sonlarga qarang: <strong>240</strong> va
<strong>252</strong>. Oʻsish atigi <strong>12 ta</strong>, yaʼni
12 ÷ 240 = <strong>5 foiz</strong>.</p>

<p>Unda nega bir ustun uch barobar baland? Chunki
<span class="cn-word" data-tr="diagrammaning tik chizigʻi, qiymatlar oʻlchanadigan chiziq">vertikal oʻq</span>
noldan emas, <strong>235</strong> dan boshlangan. Shunda birinchi ustunning
koʻrinadigan qismi 5 birlik, ikkinchisiniki 17 birlik boʻlib qoladi — koʻzga 3,4
barobar farq.</p>

<p>Bu <span class="cn-word" data-tr="oʻqning boshi koʻtarib qoʻyilgan diagramma">kesilgan oʻq</span>
deb ataladi va u eng koʻp uchraydigan hiyla. Diagramma yolgʻon yozmadi: sonlar rost,
faqat rasm boshqa narsani aytyapti.</p>

<p>Ikkinchi hiyla — <span class="cn-word" data-tr="foiz olinayotgan qiymat">asos</span>ni
aytmaslik. «Bizning mahsulotimizni tanlaganlar 44 foiz, raqiblarniki 40 foiz» degan
eʼlon ustunda ikki barobar farqday chizilishi mumkin. Aslida farq atigi <strong>4</strong>
<span class="cn-word" data-tr="ikki foiz orasidagi oddiy ayirma">foiz punkti</span>.
Ustiga-ustak, soʻrovda necha kishi qatnashgani koʻpincha yozilmaydi.</p>

<p>Uchinchi hiyla — <span class="cn-word" data-tr="gorizontal oʻqdagi ikki belgi orasidagi masofa">oraliq</span>larni teng olmaslik. Gorizontal oʻqda 2010, 2015, keyin 2016, 2017 yillar bir xil masofada turgan boʻlsa, chiziq oʻzi xohlagan tomonga egiladi. Baʼzan esa doira diagrammadagi <span class="cn-word" data-tr="butunning foizlarga boʻlingan qismi">sektor</span>lar yigʻindisi 100 foizdan oshib ketadi — buni faqat sonlarni qoʻshib koʻrgan odam sezadi.</p>

<p>Shuning uchun har qanday diagrammani uch savol bilan oʻqing: <b>oʻq qayerdan
boshlangan?</b> <b>Foiz nimadan olingan?</b> <b>Sonlarning oʻzi qani?</b></p>

<p>Diagramma — maʼlumotni koʻrsatish uchun oʻylab topilgan ajoyib narsa. Lekin u
<span class="cn-word" data-tr="fikrni maʼlum tomonga ogʻdirish usuli">ishontirish</span>
uchun ham xuddi shunday qulay. Farqni faqat hisob koʻrsatib beradi.</p>
""",
    },
]
