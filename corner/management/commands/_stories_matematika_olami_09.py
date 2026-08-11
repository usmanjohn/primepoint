# -*- coding: utf-8 -*-
"""Matematika olami — 3-matn: Abu Rayhon Beruniy Yer radiusini qanday oʻlchagan.

Toc: corner/management/commands/toc_matematika_olami.txt
Buyuk matematiklar oilasidan — darsga bogʻlanmagan mustaqil matn.
⛔ AUDIO YOʻQ.

Faktlar: Beruniy 973-yilda Xorazmning Kat shahrida tugʻilgan, 1048-yilda
Gʻaznada vafot etgan. Yer radiusini Nandana qalʼasi yonidagi togʻdan
oʻlchagan; usuli «Al-Qonun al-Masʼudiy» kitobida yozilgan. Natijasi hozirgi
oʻlchovlarda taxminan 6340 km ga toʻgʻri keladi (hozirgi oʻrtacha radius
6371 km) — farq 1 foizdan kam.

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_09.py --author=prime
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
        "title":   "Beruniy Yer radiusini bir togʻdan turib oʻlchagan",
        "summary": (
            "Haqiqiy voqea: Abu Rayhon Beruniy ming yil oldin bitta togʻ, bitta "
            "burchak va sabr bilan Yerning radiusini hisoblagan. Natijasi hozirgi "
            "qiymatdan bir foizdan kam farq qiladi."
        ),
        "order":   3,
        "grammar": [
            {
                "pattern":  "Xatolikni foizda oʻlchash",
                "meaning":  "Ikki natija qanchalik yaqinligini bilish uchun farqni "
                            "haqiqiy qiymatga boʻlib, 100 ga koʻpaytiramiz. Shunda "
                            "«31 kilometr» degan quruq son «yarim foiz» degan "
                            "baholashga aylanadi.",
                "examples": [
                    "6371 − 6340 = 31 (km farq)",
                    "31 ÷ 6371 ≈ 0,005 → 0,5% — bir foizdan ham kam",
                ],
            },
        ],
        "questions": [
            {
                "text": "Beruniy Yer radiusini oʻlchash uchun nima qildi?",
                "choices": [
                    "Yer sharini kemada aylanib chiqdi",
                    "Togʻ balandligini va togʻ choʻqqisidan ufq burchagini oʻlchadi",
                    "Quduq tubidagi quyosh aksini kuzatdi",
                    "Ikki shahar orasini karvon bilan sanab chiqdi",
                ],
                "answer": 1,
                "explanation": "Matnda aytilgan: u avval togʻning balandligini "
                               "oʻlchagan, keyin choʻqqidan turib ufq gorizontdan "
                               "necha burchakka pastda koʻrinishini aniqlagan.",
            },
            {
                "text": "Beruniy oʻlchovi 6340 km, hozirgi qiymat esa 6371 km. Farq "
                        "necha kilometr?",
                "choices": ["3 km", "31 km", "310 km", "641 km"],
                "answer": 1,
                "explanation": "6371 − 6340 = 31 kilometr. Yerning oʻlchamiga "
                               "nisbatan bu juda kichik farq.",
            },
            {
                "text": "Bu farq taxminan necha foizni tashkil qiladi?",
                "choices": ["0,5% ga yaqin", "5% ga yaqin", "31% ga yaqin", "50% ga yaqin"],
                "answer": 0,
                "explanation": "Farqni haqiqiy qiymatga boʻlamiz: 31 ÷ 6371 ≈ 0,005, "
                               "yaʼni 0,5%. Ming yil oldingi asboblar uchun bu "
                               "hayratlanarli aniqlik.",
            },
        ],
        "body": """
<p>Yerning radiusini bilish uchun nima kerak? Kosmik kema? Sunʼiy yoʻldosh? Ming yil
oldin <b>Abu Rayhon Beruniy</b>ga bitta togʻ, bitta burchak oʻlchagich va koʻp sabr
yetarli boʻlgan.</p>

<p>Beruniy 973-yilda Xorazmning Kat shahrida tugʻilgan. U
<span class="cn-word" data-tr="osmon jismlarini oʻrganadigan fan">astronomiya</span>,
geografiya, tarix va matematika bilan shugʻullangan. Yerning
<span class="cn-word" data-tr="sharning markazidan sirtigacha boʻlgan masofa">radius</span>ini
oʻlchash gʻoyasi uni yoshligidan qiziqtirgan.</p>

<p>Avvaliga u eski usulni sinab koʻrdi: ikki shahar orasidagi masofani oʻlchab, ularda
quyoshning balandligini taqqoslash. Bu usul katta sahro va koʻp odam talab qilardi.
Beruniy undan voz kechdi va boshqa yoʻl oʻyladi.</p>

<p>Yangi usul ikki qadamdan iborat edi. Birinchi qadam — togʻning
<span class="cn-word" data-tr="yer sathidan choʻqqigacha boʻlgan masofa">balandlik</span>ini
aniqlash. Buning uchun u togʻga ikki xil joydan qarab
<span class="cn-word" data-tr="ikki yoʻnalish orasidagi ochilish oʻlchovi">burchak</span>
oʻlchadi va uchburchak yordamida balandlikni hisobladi.</p>

<p>Ikkinchi qadam — eng chiroyli qismi. U togʻ choʻqqisiga chiqdi va
<span class="cn-word" data-tr="yer bilan osmon tutashib koʻrinadigan chiziq">ufq</span>ga
qaradi. Yer yassi boʻlganida ufq roppa-rosa koʻz balandligida turardi. Lekin Yer
sharsimon boʻlgani uchun ufq <b>sal pastda</b> koʻrinadi. Beruniy oʻsha kichkina
ogʻishni oʻlchadi — u bir
<span class="cn-word" data-tr="burchak oʻlchov birligi, aylananing 360 dan bir boʻlagi">gradus</span>dan
ham kichik edi.</p>

<p>Shu ikki son — togʻning balandligi va ufqning ogʻish burchagi — Yerning radiusini
hisoblashga yetdi. Beruniy usulini «Al-Qonun al-Masʼudiy» kitobida yozib qoldirgan,
shuning uchun bu rivoyat emas, hujjat.</p>

<p>Uning javobi hozirgi oʻlchovlarda taxminan <strong>6340 kilometr</strong>ga toʻgʻri
keladi. Bugungi <span class="cn-word" data-tr="olimlar qabul qilgan eng aniq son">qiymat</span>
— <strong>6371 kilometr</strong>. Farq atigi <strong>31 kilometr</strong>, yaʼni
<span class="cn-word" data-tr="haqiqiy qiymatdan chetlanish">xatolik</span> yarim
foizga yaqin.</p>

<p>Sunʼiy yoʻldoshsiz, kompyutersiz, hatto teleskopsiz. Bitta togʻ, bitta oʻlchov
asbobi va yaxshi oʻylangan
<span class="cn-word" data-tr="masalani yechishning aniq tartibi">usul</span>. Yaxshi
matematika ana shunday ishlaydi: u yetishib boʻlmaydigan narsani oʻlchab beradi.</p>
""",
    },
]
