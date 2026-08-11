# -*- coding: utf-8 -*-
"""Matematika olami — 2-matn: «Al-jabr» — algebra tugʻilgan kitob.

Toc: corner/management/commands/toc_matematika_olami.txt
Buyuk matematiklar oilasidan — 1-matnning (al-Xorazmiy) davomi, darsga
bogʻlanmagan mustaqil matn.
⛔ AUDIO YOʻQ.

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_05.py --author=prime
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
        "title":   "«Al-jabr» — algebra tugʻilgan kitob",
        "summary": (
            "Taxminan 1200 yil oldin Bagʻdodda yozilgan kitob butun dunyoga «algebra» "
            "soʻzini berdi. Qizigʻi shundaki, uning muallifi manfiy sonlarni "
            "ishlatmagan — va aynan shu narsa kitobning nomini belgilagan."
        ),
        "order":   2,
        "grammar": [
            {
                "pattern":  "al-jabr va al-muqobala",
                "meaning":  "«Al-jabr» — tenglamaning bir tomonidagi ayirilayotgan "
                            "hadni ikkinchi tomonga oʻtkazib, uni butunlash. "
                            "«Al-muqobala» — ikki tomondagi bir xil hadlarni "
                            "qisqartirib, tenglamani soddalashtirish.",
                "examples": [
                    "x − 5 = 7  →  al-jabr  →  x = 12",
                    "3x + 2 = x + 10  →  al-muqobala  →  2x = 8",
                ],
            },
        ],
        "questions": [
            {
                "text": "«Algebra» soʻzi qayerdan kelib chiqqan?",
                "choices": [
                    "Yunoncha «hisob» soʻzidan",
                    "Kitob nomidagi «al-jabr» soʻzidan",
                    "Bagʻdod shahrining eski nomidan",
                    "Lotincha «harf» soʻzidan",
                ],
                "answer": 1,
                "explanation": "Kitobning nomi «al-Kitob al-muxtasar fi hisob al-jabr "
                               "va-l-muqobala» edi. Yevropada undan faqat «al-jabr» "
                               "qismi qolib, «algebra» boʻlib ketdi.",
            },
            {
                "text": "Matnga koʻra, al-Xorazmiy nega tenglamalarni turlarga ajratishga "
                        "majbur boʻlgan?",
                "choices": [
                    "Chunki u faqat butun sonlarni bilgan",
                    "Chunki qogʻoz juda qimmat edi",
                    "Chunki u manfiy sonlarni ishlatmagan — koeffitsiyentlar musbat "
                    "boʻlishi kerak edi",
                    "Chunki shoh shunday buyurgan",
                ],
                "answer": 2,
                "explanation": "Manfiy son ishlatilmasa, «ax² + bx = c» va «ax² = bx + c» "
                               "boshqa-boshqa masala boʻlib qoladi. Shuning uchun bitta "
                               "umumiy qoida oʻrniga bir nechta tur paydo boʻlgan.",
            },
            {
                "text": "x − 5 = 7 tenglamasiga «al-jabr» qadamini qoʻllang. Nima "
                        "hosil boʻladi?",
                "choices": ["x = 2", "x = 5", "x = 7", "x = 12"],
                "answer": 3,
                "explanation": "Ayirilayotgan 5 ni ikkinchi tomonga oʻtkazamiz: "
                               "x = 7 + 5 = 12. Aynan shu «butunlash» harakati "
                               "al-jabr deb atalgan.",
            },
        ],
        "body": """
<p>Taxminan 1200 yil oldin Bagʻdoddagi «Bayt ul-hikma» — Donishmandlik uyi — dunyoning
eng katta ilmiy markazi edi. U yerda ishlagan olimlardan biri Muhammad ibn Muso
<span class="cn-word" data-tr="IX asrda yashagan buyuk matematik, «algoritm» va «algebra» soʻzlari uning nomi va kitobi bilan bogʻliq">al-Xorazmiy</span>
boʻlib, u bir kitob yozdi. Kitobning nomi uzun edi, lekin uning ichidagi ikki soʻz
butun dunyoga tarqaldi: <b>al-jabr</b> va <b>al-muqobala</b>.</p>

<p>«Al-jabr» — <i>butunlash</i>, <i>tiklash</i> degani. Bu hozir har bir oʻquvchi
qiladigan harakat: tenglamada ayirilayotgan sonni ikkinchi tomonga oʻtkazish.
<strong>x − 5 = 7</strong> boʻlsa, minusni yoʻqotib, <strong>x = 12</strong> deymiz.
«Al-muqobala» esa <i>tenglashtirish</i>: ikki tomonda takrorlangan bir xil
<span class="cn-word" data-tr="ifodadagi alohida qoʻshiluvchi qism">had</span>larni
qisqartirish.</p>

<p>Endi eng qizigʻi. Nega bu ikki oddiy harakat alohida nom oldi?</p>

<p>Chunki al-Xorazmiy davrida
<span class="cn-word" data-tr="noldan kichik son">manfiy son</span>lar hali qabul
qilinmagan edi. Son — bu miqdor: qoʻy, tanga, yer. «Minus uchta qoʻy» degan narsa
mavjud emas. Shuning uchun tenglamada minus qolib ketishiga yoʻl qoʻyib boʻlmasdi — uni
albatta ikkinchi tomonga «koʻchirib», ifodani butunlash kerak edi.</p>

<p>Buning oqibati katta boʻldi. Bugun biz ikkinchi darajali tenglamalarning barchasini
bitta koʻrinishga keltiramiz, al-Xorazmiy esa ularni <b>oltita alohida turga</b>
ajratishga majbur boʻlgan: <span class="cn-word" data-tr="tenglamada harf oldida turgan son">koeffitsiyent</span>lar
faqat musbat boʻlgani uchun «x<sup>2</sup> + 10x = 39» va «x<sup>2</sup> = 10x + 39»
uning uchun ikki boshqa masala edi.</p>

<p>Yana bir narsa: kitobda birorta ham
<span class="cn-word" data-tr="matematik amal yoki miqdorni ifodalovchi shartli yozuv">belgi</span>
yoʻq. Na <i>x</i>, na tenglik ishorasi. Hammasi soʻz bilan yozilgan: «bir mol va oʻn
ildiz oʻttiz toʻqqizga teng». Har bir
<span class="cn-word" data-tr="ikki ifodaning tengligini bildiruvchi yozuv">tenglama</span>
yechimi kichik bir hikoyaga oʻxshardi va oxirida
<span class="cn-word" data-tr="chizma yordamida keltirilgan asos">geometrik isbot</span>
berilardi.</p>

<p>XII asrda kitob lotin tiliga oʻgirildi. Yevropalik oʻquvchilar uzun nomni oxirigacha
aytishga eringan boʻlsa kerak — ular kitobni shunchaki «al-jabr» deb atashdi. Oradan
asrlar oʻtdi, soʻz shakli oʻzgardi va bugungi
<span class="cn-word" data-tr="harflar yordamida nomaʼlum miqdorlar bilan ishlaydigan matematika boʻlimi">algebra</span>
paydo boʻldi.</p>

<p>Demak, daftaringizdagi «algebra» soʻzi — aslida Xorazmdan chiqqan olimning
Bagʻdodda yozgan kitobining nomi.</p>
""",
    },
]
