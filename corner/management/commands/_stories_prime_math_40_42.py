# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-40 … PM-42.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 40 — kundalik daftar, 41 — yangilik xabari (ob-havo),
42 — ilmiy-ommabop (koinot masofalari).

FAKTLAR (tekshirilgan):
  • Yorugʻlik tezligi ~300 000 km/s = 3 × 10^5 km/s.
  • Yerdan Quyoshgacha oʻrtacha masofa ~150 000 000 km = 1,5 × 10^8 km;
    nur 500 sekundda, yaʼni ~8 daqiqa 20 sekundda yetib keladi.
  • Yerdan Oygacha ~384 000 km; nur ~1,3 sekundda yetadi (384000/300000).

⚠️ Kumulyativ: modulli tengsizlik yoʻq; 42-matnda faqat musbat
   koʻrsatkichlar ishlatilgan.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_40_42.py --author=prime
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
    # PM-40 — tengsizlik                                     KUNDALIK
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Kamida qancha kerak",
        "summary": (
            "PM-40 matni. Kundalik: Sherbek sayohat byudjetini rejalashtiradi va "
            "«koʻpi bilan necha kun» degan savol tengsizlikka aylanadi. Javob "
            "kasr chiqadi — uni qaysi tomonga yaxlitlash kerakligi ham masala."
        ),
        "order":   40,
        "grammar": [
            {
                "pattern":  "«Koʻpi bilan» → ≤, «kamida» → ≥",
                "meaning":  "Xarajat butun puldan oshmasligi kerak boʻlsa, "
                            "tengsizlik ≤ belgisi bilan yoziladi. U tenglama kabi "
                            "yechiladi; javob esa bitta son emas, sonlar toʻplami "
                            "boʻladi.",
                "examples": [
                    "45 000 + 20 000k ≤ 200 000 → 20 000k ≤ 155 000",
                    "k ≤ 7,75 → kun butun boʻlgani uchun koʻpi bilan 7 kun",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sherbek nima uchun tenglama emas, tengsizlik yozdi?",
                "choices": [
                    "Aniq javobni bilmagani uchun",
                    "Puli yetmagani uchun",
                    "Savol «roppa-rosa qancha» emas, «koʻpi bilan qancha» boʻlgani "
                    "uchun",
                    "Kunlar sonini unutgani uchun",
                ],
                "answer": 2,
                "explanation": "Xarajat puldan oshmasligi kerak edi, yaʼni shart "
                               "tenglik emas, «katta emas» koʻrinishida — bu ≤ "
                               "belgisini talab qiladi.",
            },
            {
                "text": "45 000 + 20 000k ≤ 200 000 tengsizlikdan k uchun nima "
                        "chiqadi?",
                "choices": ["k ≤ 6,5", "k ≤ 7,75", "k ≤ 10", "k ≥ 7,75"],
                "answer": 1,
                "explanation": "45 000 ni ayiramiz: 20 000k ≤ 155 000; keyin "
                               "20 000 ga boʻlamiz: k ≤ 7,75.",
            },
            {
                "text": "Sherbek koʻpi bilan necha kun qola oladi?",
                "choices": ["6 kun", "7 kun", "8 kun", "9 kun"],
                "answer": 1,
                "explanation": "7,75 kun boʻlmaydi, shuning uchun pastga "
                               "yaxlitlanadi: 7 kun. 8 kun boʻlsa xarajat "
                               "205 000 soʻm — puldan oshib ketadi.",
            },
        ],
        "body": """
<p><b>Chorshanba, kech.</b></p>

<p>Yozgi sayohatni rejalashtiryapman. Butun jamgʻarmam — <strong>200 000</strong>
soʻm, undan koʻp pulim yoʻq.</p>

<p>Borish-kelish yoʻl kirasi <strong>45 000</strong> soʻm. Har bir kun uchun ovqat va
mayda xarajatlarga taxminan <strong>20 000</strong> soʻm ketadi.</p>

<p>Savolim oddiy: <b>koʻpi bilan necha kun qola olaman?</b></p>

<p>Avval tenglama yozmoqchi boʻldim, keyin toʻxtadim. Menga «roppa-rosa» kerak emas
— pulimni <b>oshirmasligim</b> kerak. Bunday shart tenglik bilan emas,
<span class="cn-word" data-tr="ikki ifoda orasidagi katta-kichik munosabat">tengsizlik</span>
bilan yoziladi. «Koʻpi bilan» degani —
<span class="cn-word" data-tr="katta emas belgisi">≤</span>.</p>

<p>Kunlar sonini <b>k</b> deb oldim: <strong>45 000 + 20 000k ≤ 200 000</strong>.</p>

<p>Yechish tenglamadagidek boʻldi. Ikki tomondan 45 000 ni ayirdim:
<strong>20 000k ≤ 155 000</strong>. Keyin 20 000 ga boʻldim — bu musbat son, demak
<span class="cn-word" data-tr="tengsizlikdagi katta-kichik belgisi">ishora</span>
oʻzgarmadi: <strong>k ≤ 7,75</strong>.</p>

<p>Mana shu yerda bir daqiqa oʻyladim. Yetti kun butun sakkizdan uch kun degan javob
yoʻq — kun butun son boʻlishi kerak. Va kattaroq tomonga
<span class="cn-word" data-tr="sonni yaqin butun songa keltirish">yaxlitlash</span>
mumkin emas, chunki sakkiz kunga pul yetmaydi.</p>

<p><span class="cn-word" data-tr="javobni asl shartga qoʻyib sinash">Tekshirdim</span>:
7 kun boʻlsa 45 000 + 140 000 = <strong>185 000</strong> soʻm — yetadi. 8 kun boʻlsa
205 000 soʻm — yetmaydi.</p>

<p>Demak <strong>7 kun</strong>. Va qoʻlimda yana 15 000 soʻm qoladi — sovgʻaga.</p>

<p>Bugun tushundimki, tengsizlikning javobi bitta son emas,
<span class="cn-word" data-tr="shartni qanoatlantiruvchi sonlar toʻplami">yechimlar toʻplami</span>
ekan. Hayotda esa koʻpincha aynan shunday: aniq javob emas, chegara kerak.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-41 — modul                                  YANGILIK XABARI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Noldan qancha uzoq",
        "summary": (
            "PM-41 matni. Ob-havo xabari: eng katta sutkalik harorat farqi qaysi "
            "kunda boʻlgani modul yordamida hisoblanadi. Nolning ikki tomonidagi "
            "sonlar orasidagi masofa — modullar yigʻindisi."
        ),
        "order":   41,
        "grammar": [
            {
                "pattern":  "|a − b| — ikki son orasidagi masofa",
                "meaning":  "Ayirmaning moduli har doim musbat chiqadi, shuning "
                            "uchun qaysi sonni birinchi yozish ahamiyatsiz. "
                            "Nolning ikki tomonidagi sonlar uchun masofa ularning "
                            "modullari yigʻindisiga teng.",
                "examples": [
                    "|8 − (−5)| = |13| = 13 (yaʼni 8 + 5)",
                    "|3 − (−1)| = |4| = 4",
                ],
            },
        ],
        "questions": [
            {
                "text": "Xabarda nima uchun modul ishlatilgan?",
                "choices": [
                    "Haroratni manfiy qilmaslik uchun",
                    "Ikki harorat orasidagi masofani oʻlchash uchun",
                    "Haroratni yaxlitlash uchun",
                    "Sovuq kunlarni sanash uchun",
                ],
                "answer": 1,
                "explanation": "Farq — bu masofa, uning yoʻnalishi ahamiyatsiz. "
                               "Modul aynan shuni beradi va javob doim musbat "
                               "chiqadi.",
            },
            {
                "text": "Kunduzi +8, kechasi −5 gradus. Sutkalik farq necha gradus?",
                "choices": ["3 gradus", "8 gradus", "13 gradus", "40 gradus"],
                "answer": 2,
                "explanation": "|8 − (−5)| = |13| = 13 gradus. Nolning ikki "
                               "tomonidagi sonlar boʻlgani uchun 8 + 5 qilsak ham "
                               "shu chiqadi.",
            },
            {
                "text": "Ikkinchi kunning farqi 4 gradus edi. Birinchi kunning farqi "
                        "undan qanchaga katta?",
                "choices": ["4 gradusga", "9 gradusga", "13 gradusga", "17 gradusga"],
                "answer": 1,
                "explanation": "13 − 4 = 9 gradus. Birinchi kun ancha keskin "
                               "boʻlgan.",
            },
        ],
        "body": """
<p><b>Ob-havo xabari.</b> Oʻtgan hafta havo keskin oʻzgardi. Sinoptiklar sutkalik
harorat farqiga eʼtibor qaratishmoqda.</p>

<p><b>Dushanba.</b> Kunduzi <strong>+8</strong> gradus, kechasi
<strong>−5</strong> gradus. <b>Seshanba.</b> Kunduzi <strong>+3</strong>, kechasi
<strong>−1</strong> gradus.</p>

<p>Qaysi kunda farq katta boʻlgan? Buni hisoblash uchun ikki harorat orasidagi
<span class="cn-word" data-tr="ikki nuqta orasidagi uzunlik">masofa</span> kerak.
Bunday masofani <span class="cn-word" data-tr="sonning noldan masofasi, |a|">modul</span>
bilan yozamiz.</p>

<p>Dushanba: <strong>|8 − (−5)|</strong>. Avval ichidagini hisoblaymiz —
<span class="cn-word" data-tr="noldan kichik son">manfiy son</span>ni ayirish uni
qoʻshish demakdir: 8 + 5 = 13. Demak farq <strong>13 gradus</strong>.</p>

<p>Seshanba: <strong>|3 − (−1)| = |4| = 4</strong> gradus.</p>

<p>Farqning farqi: 13 − 4 = <strong>9 gradus</strong>. Dushanbadagi oʻzgarish ancha
keskin boʻlgan.</p>

<p>Nima uchun bu yerda modul kerak? Chunki farqni qaysi tomondan hisoblash
ahamiyatsiz. |8 − (−5)| ham, |(−5) − 8| ham 13 beradi — biri +13, ikkinchisi −13
boʻladi, lekin
<span class="cn-word" data-tr="sonning plyus yoki minusi">ishora</span> masofaga
taʼsir qilmaydi. Masofa hech qachon
<span class="cn-word" data-tr="noldan kichik">manfiy</span> boʻlmaydi.</p>

<p>Shuning uchun ob-havo xabarlarida, zavod oʻlchovlarida va tibbiy tahlillarda
har doim modul ishlatiladi: u «qancha
<span class="cn-word" data-tr="haqiqiy qiymatdan chetlanish">chetlanish</span> bor»
degan savolga javob beradi, «qaysi tomonga» degan savolga emas.</p>

<p>Sinoptiklar keyingi hafta farq kamayishini aytishmoqda. Kiyimni esa baribir
kechasiga qarab tanlagan maʼqul.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-42 — daraja qonunlari                          ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Koinot masofalarini yozishning qisqa yoʻli",
        "summary": (
            "PM-42 matni. Ilmiy-ommabop: astronomiyadagi ulkan sonlar standart "
            "koʻrinishda yoziladi va quyosh nurining Yerga yetib kelish vaqti "
            "daraja qonunlari bilan bir qatorda hisoblanadi."
        ),
        "order":   42,
        "grammar": [
            {
                "pattern":  "Standart koʻrinish: a × 10ⁿ",
                "meaning":  "Ulkan sonlar 1 dan 10 gacha boʻlgan son va 10 ning "
                            "darajasi koʻrinishida yoziladi. Bunday sonlarni "
                            "boʻlishda sonlar alohida, darajalar alohida "
                            "hisoblanadi — koʻrsatkichlar ayiriladi.",
                "examples": [
                    "150 000 000 = 1,5 × 10⁸; 300 000 = 3 × 10⁵",
                    "(1,5 ÷ 3) × 10⁸⁻⁵ = 0,5 × 10³ = 500 sekund",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nima uchun astronomlar sonlarni standart koʻrinishda "
                        "yozishadi?",
                "choices": [
                    "Chiroyli koʻringani uchun",
                    "Kompyuter boshqa yozuvni tushunmagani uchun",
                    "Nollarni sanash xato va vaqt talab qilgani uchun",
                    "Sonlarni kichraytirish uchun",
                ],
                "answer": 2,
                "explanation": "Matnda aytilgan: nollar qatorini sanash oson emas, "
                               "koʻrsatkich esa bir qarashda oʻqiladi.",
            },
            {
                "text": "300 000 soni standart koʻrinishda qanday yoziladi?",
                "choices": ["3 × 10⁴", "3 × 10⁵", "3 × 10⁶", "30 × 10⁴"],
                "answer": 1,
                "explanation": "Uchdan keyin beshta nol bor: 3 × 10⁵. 30 × 10⁴ ham "
                               "shu songa teng, lekin standart koʻrinishda birinchi "
                               "son 1 dan 10 gacha boʻlishi kerak.",
            },
            {
                "text": "Quyosh nuri Yerga necha sekundda yetib keladi?",
                "choices": ["8 sekund", "50 sekund", "500 sekund", "5000 sekund"],
                "answer": 2,
                "explanation": "(1,5 × 10⁸) ÷ (3 × 10⁵) = 0,5 × 10³ = 500 sekund, "
                               "yaʼni 8 daqiqa 20 sekund.",
            },
        ],
        "body": """
<p>Astronomiyada sonlar juda katta boʻladi. Yerdan Quyoshgacha
<strong>150 000 000</strong> kilometr. Yorugʻlik sekundiga
<strong>300 000</strong> kilometr yuradi. Bunday sonlarni yozish ham, oʻqish ham
noqulay — nollarni sanashda xato qilish juda oson.</p>

<p>Shuning uchun olimlar <span class="cn-word" data-tr="a × 10 ning darajasi koʻrinishidagi yozuv">standart koʻrinish</span>dan
foydalanishadi: 1 dan 10 gacha boʻlgan son, keyin 10 ning
<span class="cn-word" data-tr="daraja koʻrsatkichi, necha marta koʻpaytirilishi">daraja</span>si.</p>

<p>150 000 000 = <strong>1,5 × 10<sup>8</sup></strong>. 300 000 =
<strong>3 × 10<sup>5</sup></strong>. Nollarni sanash oʻrniga
<span class="cn-word" data-tr="darajadagi yuqori son">koʻrsatkich</span>ga qarash
kifoya.</p>

<p>Endi savol beramiz: <b>Quyoshdan chiqqan nur Yerga qancha vaqtda yetib
keladi?</b></p>

<p>Vaqtni topish uchun masofani tezlikka boʻlamiz. Bunday sonlarni boʻlishda ish
ikkiga ajraladi: sonlar alohida, darajalar alohida.
<span class="cn-word" data-tr="koʻpaytiriladigan son, 10 ning darajasida 10">Asos</span>lar
bir xil boʻlgani uchun koʻrsatkichlar ayiriladi.</p>

<p>1,5 ÷ 3 = <strong>0,5</strong>, va 10<sup>8</sup> ÷ 10<sup>5</sup> =
<strong>10<sup>3</sup></strong>. Demak javob 0,5 × 1000 = <strong>500 sekund</strong>.</p>

<p>Buni daqiqaga aylantiramiz: 500 ÷ 60 = <strong>8 daqiqa 20 sekund</strong>. Yaʼni
hozir koʻrayotgan quyosh nuri sakkiz yarim daqiqa oldin yoʻlga chiqqan.</p>

<p>Taqqoslash uchun: Oy bizdan taxminan 384 000 kilometr <span class="cn-word" data-tr="ikki nuqta orasidagi uzunlik">masofa</span>da va undan kelayotgan
nur atigi bir yarim sekund yoʻl bosadi. Quyosh esa Oydan qariyb toʻrt yuz baravar
uzoqroq.</p>

<p>Standart koʻrinish shunchaki qisqartma emas. U ulkan sonlarni
<span class="cn-word" data-tr="ikki miqdorni yonma-yon qoʻyib baholash">taqqoslash</span>ni
ham osonlashtiradi: 10<sup>8</sup> va 10<sup>5</sup> ni koʻrsangiz, birinchisi
ikkinchisidan ming baravar katta ekani darrov maʼlum boʻladi — hech narsa
hisoblamasdan.</p>
""",
    },
]
