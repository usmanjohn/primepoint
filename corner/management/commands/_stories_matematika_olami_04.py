# -*- coding: utf-8 -*-
"""Matematika olami — 23-matn: «Nega lyuk qopqogʻi dumaloq».

Toc: corner/management/commands/toc_matematika_olami.txt
Kundalik hayotdagi matematika oilasidan — darsga bogʻlanmagan, mustaqil matn.
⛔ AUDIO YOʻQ.

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_04.py --author=prime
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
        "title":   "Nega lyuk qopqogʻi dumaloq",
        "summary": (
            "Koʻchadagi eng oddiy narsalardan biri — va uning ortida aniq geometrik "
            "sabab turibdi. Ish suhbatlarida beriladigan mashhur savol."
        ),
        "order":   23,
        "grammar": [
            {
                "pattern":  "Doiraning «eni» hamma tomondan bir xil",
                "meaning":  "Doirada istalgan ikki nuqta orasidagi eng katta masofa — "
                            "diametr, va u qaysi tomondan oʻlchansa ham oʻzgarmaydi. "
                            "Kvadratda esa diagonal tomondan uzun, shuning uchun kvadrat "
                            "qopqoq oʻz teshigiga tushib ketishi mumkin.",
                "examples": [
                    "Kvadrat tomoni 60 sm → diagonali ≈ 85 sm",
                    "85 > 60, demak qopqoq qiyshaytirilsa teshikdan oʻtadi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Matnga koʻra, dumaloq qopqoqning asosiy ustunligi nima?",
                "choices": [
                    "U arzonroq ishlab chiqariladi",
                    "U hech qanday holatda oʻz teshigiga tushib ketmaydi",
                    "U kamroq joy egallaydi",
                    "Uni bo'yash osonroq",
                ],
                "answer": 1,
                "explanation": "Doiraning kengligi hamma yoʻnalishda bir xil, shuning "
                               "uchun uni qanday burasangiz ham teshikdan oʻtkazib "
                               "boʻlmaydi.",
            },
            {
                "text": "Tomoni 60 sm boʻlgan kvadrat qopqoq nega xavfli?",
                "choices": [
                    "Uning diagonali tomonidan uzun — taxminan 85 sm",
                    "Uning yuzasi juda katta",
                    "Uning perimetri doiranikidan uzun",
                    "U juda ogʻir boʻladi",
                ],
                "answer": 0,
                "explanation": "Diagonal ≈ 85 sm, teshikning eni esa 60 sm. Qopqoqni "
                               "qiyshaytirib qoʻysangiz, u teshikka tushib ketadi.",
            },
            {
                "text": "Matnda aytilishicha, dumaloq shakl yana qanday amaliy foyda beradi?",
                "choices": [
                    "U qorda tez eriydi",
                    "Uni ikki kishi koʻtarishi shart",
                    "Uni koʻtarish shart emas — dumalatib olib borish mumkin",
                    "U hech qachon zanglamaydi",
                ],
                "answer": 2,
                "explanation": "Ogʻir qopqoqni koʻtarish oʻrniga uni yon tomonga "
                               "agʻdarib dumalatish mumkin.",
            },
        ],
        "body": """
<p>Koʻchadan yurib ketayotib oyogʻingiz ostiga qarang: temir lyuk qopqoqlari deyarli
har doim <strong>dumaloq</strong>. Kvadrat yoki uchburchak qopqoqni juda kam
uchratasiz. Bu tasodif emas.</p>

<p>Tasavvur qiling, qopqoq kvadrat boʻlsin va uning tomoni 60 sm boʻlsin. Ishchi uni
koʻtardi, yon tomonga qoʻydi, keyin qaytarib yopmoqchi boʻldi. Agar qopqoqni sal
qiyshaytirsa, u <span class="cn-word" data-tr="kvadratning qarama-qarshi burchaklarini tutashtiruvchi kesma">diagonal</span>i
boʻylab tushib ketadi — chunki diagonal tomondan uzunroq, taxminan
<strong>85 sm</strong>. Teshikning eni esa atigi 60 sm.</p>

<p>Doirada bunday zaif joy yoʻq. Uning eng katta «eni» —
<span class="cn-word" data-tr="doirani markazidan kesib oʻtuvchi eng uzun kesma">diametr</span> —
qaysi tomondan oʻlchasangiz ham bir xil. Shuning uchun dumaloq qopqoqni qanday burang,
qanday qiyshaytiring — u oʻz teshigidan oʻtmaydi. Matematiklar bunday shaklni
<span class="cn-word" data-tr="hamma yoʻnalishda kengligi bir xil boʻlgan shakl">doimiy kenglikdagi shakl</span>
deb atashadi.</p>

<p>Sabablar shu bilan tugamaydi.</p>

<p>Dumaloq qopqoqni yopish uchun uni burchakma-burchak toʻgʻrilash shart emas — qaysi
tomonga qoʻysangiz ham tushadi. Ogʻir temirni koʻtarish oʻrniga uni yon tomonga agʻdarib
<span class="cn-word" data-tr="yumaloq shaklni agʻdarib yurgizish">dumalatish</span> mumkin.
Quvur ham koʻpincha dumaloq, chunki bir xil
<span class="cn-word" data-tr="shakl chegarasining uzunligi">perimetr</span>da doira eng
katta <span class="cn-word" data-tr="shakl ichidagi joy oʻlchovi">yuza</span>ni beradi va
yerning bosimiga bir tekis qarshilik koʻrsatadi.</p>

<p>Bu savolni bir paytlar ish suhbatlarida berishardi. Undan kutilgani —
tayyor javob emas, fikrlash yoʻli edi: shaklga qarab, uning
<span class="cn-word" data-tr="shaklning oʻlchov va munosabatlari haqidagi fan">geometriya</span>si
qanday amaliy natija berishini koʻra olish.</p>

<p>Endi koʻchada lyukka duch kelsangiz, bir soniya toʻxtang. Oyogʻingiz ostida geometriya
yotibdi — va u sizni ochiq quduqqa tushib ketishdan asrab turibdi.</p>
""",
    },
]
