# -*- coding: utf-8 -*-
"""Matematika olami — 26-matn: Foiz ustiga foiz: pul qanday oʻsadi.

Toc: corner/management/commands/toc_matematika_olami.txt
Kundalik hayotdagi matematika oilasidan — darsga bogʻlanmagan mustaqil matn.
PM-23/PM-24 foiz bloki yonida oʻqilsa yaxshi, lekin unga bogʻlanmagan.
⛔ AUDIO YOʻQ.

Arifmetika (verify_pm_22_24.py bilan tekshirilgan):
  1 000 000 × 1,1 = 1 100 000; × 1,1 = 1 210 000; × 1,1 = 1 331 000
  oddiy foiz bilan 3 yilda: 1 300 000 — farq 31 000
  1,1^10 ≈ 2,5937 → 10 yilda ≈ 2 593 700 soʻm
  72 qoidasi: 72 ÷ 10 = 7,2 yil; haqiqatda 1,1^7 ≈ 1,95 va 1,1^8 ≈ 2,14

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_10.py --author=prime
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
        "title":   "Foiz ustiga foiz: pul qanday oʻsadi",
        "summary": (
            "Nima uchun ikkinchi yilning foizi birinchi yilnikidan katta boʻladi va "
            "«72 qoidasi» pulning necha yilda ikki barobar boʻlishini qanday "
            "bashorat qiladi."
        ),
        "order":   26,
        "grammar": [
            {
                "pattern":  "Murakkab foiz: har yili YANGI summadan",
                "meaning":  "Oddiy foizda har yili bir xil miqdor qoʻshiladi. Murakkab "
                            "foizda esa foiz oʻtgan yilgi summadan olinadi, shuning "
                            "uchun qoʻshimcha har yili kattalashib boradi.",
                "examples": [
                    "1 000 000 × 1,1 = 1 100 000 (1-yil)",
                    "1 100 000 × 1,1 = 1 210 000 (2-yil) — qoʻshimcha 110 000",
                    "1 210 000 × 1,1 = 1 331 000 (3-yil) — qoʻshimcha 121 000",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nima uchun ikkinchi yilning foizi birinchi yilnikidan katta?",
                "choices": [
                    "Bank ikkinchi yili foiz stavkasini oshiradi",
                    "Foiz endi kattalashgan summadan olinadi",
                    "Birinchi yili foiz toʻliq toʻlanmaydi",
                    "Ikkinchi yilda kunlar koʻproq boʻladi",
                ],
                "answer": 1,
                "explanation": "Stavka oʻzgarmaydi — 10 foizligicha qoladi. Lekin u "
                               "endi 1 000 000 dan emas, 1 100 000 dan olinadi, "
                               "shuning uchun qoʻshimcha 100 000 emas, 110 000 boʻladi.",
            },
            {
                "text": "1 000 000 soʻm yiliga 10 foizdan oʻssa, ikki yildan keyin "
                        "qancha boʻladi?",
                "choices": ["1 200 000 soʻm", "1 210 000 soʻm", "1 300 000 soʻm",
                            "2 000 000 soʻm"],
                "answer": 1,
                "explanation": "Birinchi yil: 1 000 000 + 100 000 = 1 100 000. "
                               "Ikkinchi yil foizi yangi summadan: 1 100 000 ning "
                               "10% i — 110 000. Jami 1 210 000 soʻm.",
            },
            {
                "text": "«72 qoidasi»ga koʻra, yiliga 8 foiz oʻsadigan pul taxminan "
                        "necha yilda ikki barobar boʻladi?",
                "choices": ["4 yilda", "8 yilda", "9 yilda", "16 yilda"],
                "answer": 2,
                "explanation": "72 ni foizga boʻlamiz: 72 ÷ 8 = 9 yil. Bu aniq "
                               "formula emas, tez baho beradigan qoida — lekin "
                               "haqiqatga juda yaqin turadi.",
            },
        ],
        "body": """
<p>Bir million soʻmni bankka qoʻydingiz. Bank yiliga <strong>10 foiz</strong> — bu uning <span class="cn-word" data-tr="bank yiliga toʻlaydigan foiz miqdori">stavka</span>si — beradi.
Uch yildan keyin qancha boʻladi? Koʻpchilik darrov javob beradi: har yili 100 000 dan,
demak <strong>1 300 000</strong>. Bu — <span class="cn-word" data-tr="foiz har safar boshlangʻich summadan olinadigan hisob">oddiy foiz</span> bilan hisoblangan javob: yaqin, lekin notoʻgʻri.</p>

<p>Sabab shunda: ikkinchi yili foiz endi millionning emas, <b>million bir yuz
mingning</b> 10 foizi boʻladi. Buni
<span class="cn-word" data-tr="foiz oʻtgan davr oxiridagi summadan olinadigan hisob">murakkab foiz</span>
deyiladi.</p>

<p>Hisoblab koʻramiz. Birinchi yil oxirida: 1 000 000 + 100 000 =
<strong>1 100 000</strong>. Ikkinchi yil oxirida qoʻshimcha allaqachon 110 000 —
jami <strong>1 210 000</strong>. Uchinchi yilda esa <span class="cn-word" data-tr="asosiy summaga qoʻshiladigan foiz puli">qoʻshimcha</span> 121 000 boʻladi va summa
<strong>1 331 000</strong> soʻmga yetadi.</p>

<p>Farq atigi 31 000 soʻm koʻrinadi. Lekin bu farq har yili kattalashib boraveradi,
chunki har bir yangi foiz oʻzidan keyingi foizni ham koʻtaradi. Oʻn yildan keyin, yaʼni pul bankda turgan butun <span class="cn-word" data-tr="hisob yuritiladigan vaqt oraligʻi">muddat</span> oxirida,
<span class="cn-word" data-tr="foiz olinadigan asosiy summa">asosiy summa</span>
2 000 000 emas, taxminan <strong>2 594 000</strong> soʻm boʻladi.</p>

<p>Bunday oʻsishning oʻz nomi bor:
<span class="cn-word" data-tr="har qadamda oldingi natijadan koʻpaytiriladigan oʻsish">koʻrsatkichli oʻsish</span>.
U sekin boshlanadi va keyin tobora tezlashadi — shuning uchun uni koʻz bilan
bashorat qilib boʻlmaydi.</p>

<p>Moliyachilarning tez baho beradigan bir usuli bor —
<span class="cn-word" data-tr="pul necha yilda ikki barobar boʻlishini taxminlaydigan qoida">72 qoidasi</span>.
72 ni yillik foizga boʻlasiz va pul necha yilda ikki barobar boʻlishini taxminan
bilib olasiz. 10 foizda: 72 ÷ 10 ≈ <strong>7 yil</strong>. Haqiqatan ham,
yettinchi yilda summa ikki baravarga sal yetmaydi, sakkizinchisida esa undan oshib
ketadi.</p>

<p>Endi eng muhimi. Bu qoida <b>qarzga ham</b> xuddi shunday ishlaydi. Toʻlanmagan
<span class="cn-word" data-tr="bankdan olingan va foizi bilan qaytariladigan pul">kredit</span> ham har oy yangi summadan foiz oladi va xuddi shu tezlik bilan oʻsadi.
Murakkab foiz — kim tomonda turganingizga qarab, eng yaxshi doʻstingiz yoki eng
sabrsiz kreditoringiz.</p>
""",
    },
]
