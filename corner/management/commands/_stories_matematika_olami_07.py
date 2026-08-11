# -*- coding: utf-8 -*-
"""Matematika olami — 30-matn: Musiqa ichidagi kasrlar.

Toc: corner/management/commands/toc_matematika_olami.txt
Kundalik hayotdagi matematika oilasidan — darsga bogʻlanmagan mustaqil matn.
PM-15…PM-18 (kasrlar) bilan yonma-yon oʻqishga qulay.
⛔ AUDIO YOʻQ.

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_07.py --author=prime
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
        "title":   "Musiqa ichidagi kasrlar",
        "summary": (
            "Torni yarmidan bosing — ovoz bir oktava koʻtariladi. Musiqa yoqimli "
            "eshitilishining ortida oddiy kasrlar turibdi, va buni ikki yarim ming "
            "yil oldin payqashgan."
        ),
        "order":   30,
        "grammar": [
            {
                "pattern":  "Tor uzunligi va ovoz balandligi",
                "meaning":  "Torning uzunligi qancha qisqarsa, ovoz shuncha baland "
                            "chiqadi. Yoqimli eshitiladigan juftliklar aynan sodda "
                            "kasrlarga toʻgʻri keladi: 1/2, 2/3, 3/4. Nota "
                            "davomiyliklari ham kasr — butun, yarim, chorak.",
                "examples": [
                    "1/2 — oktava · 2/3 — kvinta · 3/4 — kvarta",
                    "1/4 + 1/4 + 1/4 + 1/4 = 1 (toʻrt chorak — bitta takt)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Torni roppa-rosa yarmidan bosilsa, ovoz qanday oʻzgaradi?",
                "choices": [
                    "Ovoz pastroq chiqadi",
                    "Ovoz oʻzgarmaydi",
                    "Ovoz bir oktava balandroq chiqadi",
                    "Ovoz butunlay yoʻqoladi",
                ],
                "answer": 2,
                "explanation": "Tor ikki barobar qisqargani uchun ovoz aynan bir "
                               "oktava koʻtariladi — quloqqa u «xuddi shu nota, "
                               "faqat balandroq» boʻlib eshitiladi.",
            },
            {
                "text": "Toʻrtlik oʻlchovdagi bir taktga nechta chorak nota sigʻadi?",
                "choices": ["2 ta", "3 ta", "4 ta", "8 ta"],
                "answer": 2,
                "explanation": "1/4 + 1/4 + 1/4 + 1/4 = 4/4 = 1. Butun takt "
                               "toʻldirilishi uchun kasrlar yigʻindisi roppa-rosa "
                               "birga teng boʻlishi kerak.",
            },
            {
                "text": "Bir taktda ikkita chorak nota bor. Uni toʻldirish uchun yana "
                        "qancha kerak?",
                "choices": ["1/4", "1/2", "2/4 dan koʻproq", "3/4"],
                "answer": 1,
                "explanation": "2/4 = 1/2 toʻlgan. Qolgani 1 − 1/2 = 1/2 — masalan "
                               "bitta yarim nota yoki yana ikkita chorak.",
            },
        ],
        "body": """
<p>Bir tor torting va uni chertib koʻring. Endi barmogʻingiz bilan aynan
<b>oʻrtasidan</b> bosib, yana cherting. Ovoz balandroq chiqadi — va gʻalati tomoni
shundaki, u <i>oʻsha notaning oʻzi</i> boʻlib eshitiladi. Musiqachilar buni
<span class="cn-word" data-tr="ikki nota orasidagi masofa; tor yarmiga qisqarganda hosil boʻladi">oktava</span>
deb atashadi.</p>

<p>Rivoyatga koʻra, buni birinchi boʻlib qadimgi yunon olimi Pifagor va uning
shogirdlari sinchiklab tekshirishgan. Ular torni turli joydan bosib koʻrishdi va
kutilmagan qonuniyatni topishdi: quloqqa <b>yoqimli</b> eshitiladigan juftliklar
faqat <span class="cn-word" data-tr="katta boʻlmagan sonlardan tuzilgan kasr">sodda kasr</span>lar
chiqqanda paydo boʻlar ekan.</p>

<p>Torning <strong>1/2</strong> qismi — oktava. <strong>2/3</strong> qismi —
musiqada <span class="cn-word" data-tr="besh pogʻonalik masofa; tor uzunligining 2/3 qismi">kvinta</span>
deyiladi. <strong>3/4</strong> qismi esa
<span class="cn-word" data-tr="toʻrt pogʻonalik masofa; tor uzunligining 3/4 qismi">kvarta</span>.
Agar tor tasodifiy joydan bosilsa — masalan 7/13 qismidan — ovoz gʻalati va
noqulay eshitiladi.</p>

<p>Kasrlar musiqada yana bir joyda ishlaydi, va bu safar butunlay boshqa tomondan:
<b>vaqt</b>da.</p>

<p>Nota qancha davom etishi ham kasr bilan yoziladi. Eng uzuni —
<span class="cn-word" data-tr="eng uzun nota davomiyligi, butun takt">butun nota</span>.
Undan keyin yarim nota, chorak nota, sakkizlik va oʻn oltilik keladi. Har biri
oldingisining roppa-rosa yarmi.</p>

<p>Notalarni <span class="cn-word" data-tr="notalar guruhlanadigan teng vaqt boʻlagi">takt</span>
degan boʻlaklarga joylashtiriladi, va bu yerda qatʼiy qoida bor: bir taktdagi
davomiyliklarning <span class="cn-word" data-tr="qoʻshish natijasi">yigʻindi</span>si
belgilangan miqdorga <b>roppa-rosa</b> teng boʻlishi kerak. Eng koʻp uchraydigan
oʻlchov — toʻrtlik: <strong>1/4 + 1/4 + 1/4 + 1/4 = 1</strong>.</p>

<p>Musiqachi bitta chorak notani ikkita sakkizlikka almashtira oladi, chunki
<strong>1/8 + 1/8 = 1/4</strong>. Boʻlaklar mayda boʻladi, umumiy
<span class="cn-word" data-tr="bir notaning davom etish vaqti">davomiylik</span> esa
oʻzgarmaydi — bu aynan kasrlarni qoʻshish qoidasi.</p>

<p>Demak nota daftariga qarayotgan musiqachi, aslida, kasrlar bilan ishlaydi. Faqat u
buni tez, ovoz chiqarmasdan va qoʻli bilan qiladi.</p>
""",
    },
]
