# -*- coding: utf-8 -*-
"""Matematika olami — 17-matn: Fibonachchi sonlari gul va qaragʻay qubbasida.

Toc: corner/management/commands/toc_matematika_olami.txt
Tabiatdagi matematika oilasidan — darsga bogʻlanmagan mustaqil matn.
⛔ AUDIO YOʻQ.

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_08.py --author=prime
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
        "title":   "Fibonachchi sonlari gul va qaragʻay qubbasida",
        "summary": (
            "Bitta oddiy qoida — har bir sonni oldingi ikkitasini qoʻshib topish — "
            "va shu ketma-ketlik kungaboqar, qaragʻay qubbasi va gul bargida "
            "qayta-qayta paydo boʻladi."
        ),
        "order":   17,
        "grammar": [
            {
                "pattern":  "Har bir son — oldingi ikkitasining yigʻindisi",
                "meaning":  "Fibonachchi ketma-ketligi 1 va 1 dan boshlanadi. "
                            "Undan keyingi har bir son oʻzidan oldingi ikkita sonni "
                            "qoʻshish bilan topiladi. Qoida shu qadar oddiyki, uni "
                            "yodda saqlash uchun hech narsa yozish shart emas.",
                "examples": [
                    "1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89…",
                    "3 + 5 = 8 · 5 + 8 = 13 · 8 + 13 = 21",
                ],
            },
        ],
        "questions": [
            {
                "text": "Fibonachchi ketma-ketligida 21 dan keyin qaysi son keladi?",
                "choices": ["26", "31", "34", "42"],
                "answer": 2,
                "explanation": "Har bir son oldingi ikkitasining yigʻindisi: "
                               "13 + 21 = 34. 42 javobi 21 ni ikkiga koʻpaytirganda "
                               "chiqadi — bu boshqa qoida.",
            },
            {
                "text": "Matnga koʻra, qaragʻay qubbasidagi spirallar soni odatda "
                        "qanday boʻladi?",
                "choices": [
                    "Har doim teng va juft",
                    "Ketma-ketlikdagi ikkita qoʻshni son — masalan 8 va 13",
                    "Har doim oʻnta",
                    "Har bir qubbada boshqacha, qonuniyat yoʻq",
                ],
                "answer": 1,
                "explanation": "Bir tomonga buralgan spirallar bir sonni, teskari "
                               "tomonga buralganlari esa unga qoʻshni sonni beradi.",
            },
            {
                "text": "Ketma-ketlikning dastlabki oltita soni qoʻshilsa, qancha "
                        "chiqadi? (1, 1, 2, 3, 5, 8)",
                "choices": ["18", "20", "21", "34"],
                "answer": 1,
                "explanation": "1 + 1 + 2 + 3 + 5 + 8 = 20. Diqqat: bu yigʻindi "
                               "ketma-ketlikning oʻzidagi son emas — 21 juda yaqin "
                               "turgani sababli koʻpchilik shu javobni tanlaydi.",
            },
        ],
        "body": """
<p>Bitta qoidani olaylik, undan oddiyrogʻini oʻylab topish qiyin: <b>har bir son
oʻzidan oldingi ikkita sonning yigʻindisiga teng</b>.</p>

<p>1 va 1 dan boshlaymiz. 1 + 1 = 2. Keyin 1 + 2 = 3, soʻng 2 + 3 = 5, 3 + 5 = 8.
Shu tariqa <span class="cn-word" data-tr="maʼlum qoida boʻyicha ketma-ket yoziladigan sonlar">ketma-ketlik</span>
hosil boʻladi:</p>

<p><strong>1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144…</strong></p>

<p>Bu sonlarni Yevropaga XIII asrda Pizalik Leonardo — koʻproq
<span class="cn-word" data-tr="XIII asr italyan matematigi, hind-arab raqamlarini Yevropaga tanitgan">Fibonachchi</span>
nomi bilan tanilgan olim — keltirgan. U 1202-yilda yozgan kitobida quyonlar
koʻpayishi haqidagi masalani yechayotib shu qatorga duch kelgan. Aslida bu sonlar
undan bir necha asr oldin Hindiston olimlariga ham maʼlum edi.</p>

<p>Eng qizigʻi keyin boshlanadi. Bu sonlar <b>tabiatda</b> uchraydi.</p>

<p>Qaragʻay qubbasiga qarang. Uning tangachalari
<span class="cn-word" data-tr="markazdan burala-burala chiqadigan egri chiziq">spiral</span>lar
boʻylab joylashgan. Spirallarni bir tomonga sanasangiz sakkizta, teskari tomonga
sanasangiz oʻn uchta chiqadi. Sakkiz va oʻn uch — ketma-ketlikdagi
<span class="cn-word" data-tr="ketma-ketlikda yonma-yon turgan sonlar">qoʻshni sonlar</span>.</p>

<p>Kungaboqarda ham xuddi shunday, faqat sonlar kattaroq: koʻpincha 34 va 55, katta
gullarda esa 55 va 89.</p>

<p>Gul barglari ham koʻpincha shu qatordan son beradi: nilufarda 3 ta, ayiqtovonda
5 ta, isfaraqda 8 ta, qoqioʻtda koʻpincha 13, 21 yoki 34 ta.</p>

<p>Nega shunday? Sabab goʻzallikda emas, <b>joyni tejash</b>da. Urugʻlar markazdan
maʼlum bir burchak ostida navbatma-navbat chiqadi. Agar bu burchak
<span class="cn-word" data-tr="ikki miqdorning bir-biriga solishtirilishi">nisbat</span>i
sodda kasr boʻlsa, urugʻlar bir necha nur boʻylab tizilib qoladi va orada boʻsh joy
qoladi. Fibonachchi sonlaridan kelib chiqadigan burchak esa hech qachon takrorlanmaydi —
shuning uchun urugʻlar bir-birini qismay, eng zich joylashadi.</p>

<p>Yana bir narsa. Qoʻshni ikki sonni boʻlsangiz, natija har safar bir xil songa
yaqinlashib boradi: 5 ÷ 3 = 1,666… , 8 ÷ 5 = 1,6 , 13 ÷ 8 = 1,625 , 21 ÷ 13 ≈ 1,615.
Bu son taxminan <b>1,618</b> ga teng va
<span class="cn-word" data-tr="taxminan 1,618 ga teng mashhur nisbat">oltin nisbat</span>
deb ataladi.</p>

<p>Demak keyingi safar qaragʻay qubbasini qoʻlingizga olsangiz, spirallarni sanab
koʻring. Ehtimol, javobingiz shu qatordan chiqadi.</p>
""",
    },
]
