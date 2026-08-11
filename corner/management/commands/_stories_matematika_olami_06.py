# -*- coding: utf-8 -*-
"""Matematika olami — 31-matn: A4 qogʻozning sirli oʻlchami.

Toc: corner/management/commands/toc_matematika_olami.txt
Kundalik hayotdagi matematika oilasidan — darsga bogʻlanmagan mustaqil matn.
PM-13 (kvadrat ildiz) bilan yonma-yon oʻqishga qulay: butun A qatori √2 ustiga
qurilgan.
⛔ AUDIO YOʻQ.

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_06.py --author=prime
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
        "title":   "A4 qogʻozning sirli oʻlchami",
        "summary": (
            "Printerdagi eng oddiy varaq — aslida ehtiyotkorlik bilan tanlangan "
            "matematik shakl. Uni ikkiga buksangiz, yana oʻziga oʻxshagan varaq "
            "chiqadi. Bunga faqat bitta nisbat qodir."
        ),
        "order":   31,
        "grammar": [
            {
                "pattern":  "A qatorining nisbati: uzun tomon ÷ qisqa tomon = √2",
                "meaning":  "Varaqni uzun tomoni boʻylab ikkiga buksak, tomonlar "
                            "nisbati oʻzgarmasligi kerak. Bunga faqat √2 nisbati mos "
                            "keladi — shuning uchun A4 dan A5, A5 dan A6 chiqaveradi.",
                "examples": [
                    "A4: 297 ÷ 210 — natija √2 ga juda yaqin",
                    "A4 ni buksak → A5: 210 × 148 mm",
                ],
            },
        ],
        "questions": [
            {
                "text": "A4 varaqni uzun tomoni boʻylab ikkiga buksak, nima hosil "
                        "boʻladi?",
                "choices": [
                    "Kvadrat shaklidagi varaq",
                    "Nisbati butunlay boshqacha varaq",
                    "Aynan shu nisbatdagi kichikroq varaq — A5",
                    "Nisbati ikki barobar oʻzgargan varaq",
                ],
                "answer": 2,
                "explanation": "A qatorining butun gʻoyasi shu: buklanganda shakl "
                               "oʻziga oʻxshab qolaveradi.",
            },
            {
                "text": "A0 varaqning yuzasi taxminan qancha?",
                "choices": ["1 dm²", "1 m²", "2 m²", "16 m²"],
                "answer": 1,
                "explanation": "Butun qator A0 dan boshlanadi, uning yuzasi taxminan "
                               "1 m² qilib tanlangan. Har keyingi oʻlcham yuzani "
                               "ikkiga boʻladi.",
            },
            {
                "text": "A0 dan A4 gacha necha marta buklanadi va A4 ning yuzasi "
                        "A0 nikidan necha marta kichik?",
                "choices": [
                    "2 marta buklanadi, 4 marta kichik",
                    "4 marta buklanadi, 8 marta kichik",
                    "4 marta buklanadi, 16 marta kichik",
                    "8 marta buklanadi, 16 marta kichik",
                ],
                "answer": 2,
                "explanation": "A0 → A1 → A2 → A3 → A4 — toʻrtta qadam. Har qadamda "
                               "yuza ikkiga boʻlinadi: 2 × 2 × 2 × 2 = 16 marta.",
            },
        ],
        "body": """
<p>Printerdan bir varaq oling. Ehtimol, u <b>A4</b> — dunyodagi eng koʻp ishlatiladigan
qogʻoz oʻlchami. Uning tomonlari <b>210 mm</b> va <b>297 mm</b>. Gʻalati sonlar, shunday
emasmi? Nega 200 va 300 emas?</p>

<p>Chunki bu sonlar tanlanmagan — ular <b>hisoblab chiqarilgan</b>.</p>

<p>Talab bitta edi: varaqni uzun tomoni boʻylab ikkiga buklaganda, hosil boʻlgan yangi
varaq <span class="cn-word" data-tr="ikki miqdorning bir-biriga solishtirilishi">nisbat</span>
jihatidan avvalgisining aynan oʻzi boʻlsin. Faqat kichikroq.</p>

<p>Bu shart koʻrinishdan oddiy, lekin uni qanoatlantiradigan
<span class="cn-word" data-tr="tomonlar nisbati bir xil boʻlgan shakllar">oʻxshash shakl</span>
bitta: uzun tomonning qisqa tomonga nisbati
<span class="cn-word" data-tr="oʻziga koʻpaytirilganda 2 ni beradigan son">√2</span>
boʻlgan toʻrtburchak. Bu son butun ham emas,
<span class="cn-word" data-tr="butunning teng boʻlaklari bilan yoziladigan son">kasr</span>
ham emas — u 1 bilan 2 orasida turadi, chunki 1 × 1 = 1, 2 × 2 = 4, kerakli son esa
oʻziga koʻpaytirilganda 2 ni berishi kerak. Bunday sonni topish amali <span class="cn-word" data-tr="oʻziga koʻpaytirilganda berilgan sonni beradigan manfiy boʻlmagan son">kvadrat ildiz</span> chiqarish deyiladi.</p>

<p>Tekshirib koʻring: <strong>297 ÷ 210</strong> — javob √2 ga juda yaqin chiqadi.</p>

<p>Butun qator <b>A0</b> dan boshlanadi. Uning
<span class="cn-word" data-tr="shakl ichidagi joy oʻlchovi">yuza</span>si taxminan
<b>1 m²</b> qilib olingan. A0 ni buksangiz A1, uni buksangiz A2 chiqadi va hokazo.
A0 dan A4 gacha toʻrtta buklash bor, demak yuza <strong>2 × 2 × 2 × 2 = 16</strong>
marta kichrayadi.</p>

<p>Bundan juda amaliy narsalar kelib chiqadi.</p>

<p>Birinchidan, nusxa koʻchirgichdagi tugmalar. A4 ni A5 ga kichraytirish uchun
apparat 71% ni tanlaydi — bu √2 ning teskarisi. Ikkinchidan, qogʻoz sotib olish.
Qutida «80 g/m²» deb yozilgan boʻlsa — bu qogʻozning <span class="cn-word" data-tr="bir kvadrat metr qogʻozning ogʻirligi">yuza zichligi</span> — bitta A4 ning ogʻirligini hisoblash oson:
u A0 dan 16 marta kichik, demak taxminan 5 gramm.</p>

<p>Uchinchidan — hech narsa <span class="cn-word" data-tr="foydasiz qolgan qism">isrof</span>
boʻlmaydi. Katta rulondan A qatorining varaqlarini kesganda chekka qolmaydi, chunki har
bir oʻlcham oldingisining roppa-rosa yarmi.</p>

<p>Bu tizim 1922-yilda Germaniyada qabul qilingan va bugun deyarli butun dunyo shundan
foydalanadi. Qoʻlingizdagi oddiy varaq — aslida bir asrlik matematik qarorning
natijasi.</p>
""",
    },
]
