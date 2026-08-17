# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-87, PM-88, PM-89.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 87 — qoʻllanma, 88 — kundalik, 89 — hikoya.
Oldingi uchlik ilmiy-ommabop / qoʻllanma / hikoya edi. Uchtasi
ketma-ket bir xil shakl emas.

⚠️ Kumulyativ:
   • 87-matnda faqat CHIZMA usuli — tasma model va «ortiqchani
     qirqish». ⛔ Tezlik yoʻq;
   • 88-matnda v = S ÷ t va birliklarni moslash (minut → soat).
     ⛔ Ikki harakatlanuvchi YOʻQ — u 89-matnniki;
   • 89-matnda uchrashuv: yaqinlashish tezligi v₁ + v₂.
⚠️ Sonlar darsdagilardan boshqa: 87 → 84/16, 88 → 6 km lik yoʻl,
   89 → 360 km va 55/65 km/soat (darsda 300 km, 60/40 edi).
⚠️ Savollar SAQLANGAN TARTIBDA koʻrsatiladi — `answer` indekslari:
   87 → 2/1/0, 88 → 2/0/3, 89 → 3/1/2.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_87_89.py --author=prime
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
    # PM-87 — chizma                                          QOʻLLANMA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Chizib yechilgan masala",
        "summary": (
            "PM-87 matni. Qoʻllanma: Jasur bir masalada yarim soat "
            "tiqilib qoladi. Akasi javobni aytmaydi — ikkita tasma "
            "chizib beradi, xolos."
        ),
        "order":   87,
        "grammar": [
            {
                "pattern":  "ortiqchani qirq → qolganini teng boʻl",
                "meaning":  "Jami va farq berilganda ishlatiladigan "
                            "tasma model usuli. Uzun tasmaning ortiqcha "
                            "uchi jamidan ayiriladi, qolgani ikkita teng "
                            "boʻlakka boʻlinadi.",
                "examples": [
                    "(84 − 16) ÷ 2 = 34 — kichigi",
                    "34 + 16 = 50 — kattasi",
                    "tekshirish: 34 + 50 = 84 va 50 − 34 = 16",
                ],
            },
        ],
        "questions": [
            {
                "text": "Akasi Jasurga qanday yordam berdi?",
                "choices": [
                    "Javobni aytib berdi",
                    "Kalkulyator berdi",
                    "Masalani ikkita tasma qilib chizdi",
                    "Formulani yozib berdi",
                ],
                "answer": 2,
                "explanation": "Akasi hech qanday son aytmadi. U faqat "
                               "ikkita tasma chizdi va ortiqcha uchini "
                               "koʻrsatdi — qolganini Jasur oʻzi topdi.",
            },
            {
                "text": "Kichik ulush nechta yongʻoqdan iborat?",
                "choices": ["24 ta", "34 ta", "42 ta", "50 ta"],
                "answer": 1,
                "explanation": "Ortiqchani qirqamiz: 84 − 16 = 68. "
                               "Qolgani ikkita teng tasma: 68 ÷ 2 = 34. "
                               "«42» — 84 ni shunchaki teng ikkiga "
                               "boʻlganda chiqadi va 16 talik farqni "
                               "yoʻqotadi; «50» esa katta ulush.",
            },
            {
                "text": "Katta ulush kichigidan necha marta koʻp emas, "
                        "balki nechta koʻp?",
                "choices": ["16 ta koʻp", "18 ta koʻp", "34 ta koʻp",
                            "50 ta koʻp"],
                "answer": 0,
                "explanation": "Farq masalada berilgan: 16 ta. Tekshirib "
                               "koʻramiz: 50 − 34 = 16 ✓ Diqqat: savol "
                               "«nechta koʻp» deb soʻragan — bu ayirma, "
                               "«necha marta» emas.",
            },
        ],
        "body": """
<p>Jasur stol ustida yarim soatdan beri bitta
<span class="cn-word" data-tr="vaziyat matn bilan berilgan masala">masala</span>ga
qarab oʻtiribdi.</p>

<p>Masala qisqa: «Ikki doʻst 84 ta yongʻoqni boʻlishdi. Biri
ikkinchisidan 16 ta koʻp oldi. Har biri nechtadan oldi?»</p>

<p>Jasur avval 84 ni ikkiga <span class="cn-word" data-tr="teng qismlarga ajratish">boʻldi</span> va 42 chiqdi. Lekin unda farq
yoʻqolib qolardi. Keyin 84 dan 16 ni ayirdi va 68 chiqdi. Bu
<span class="cn-word" data-tr="ayirish amalining natijasi">ayirma</span>
bilan nima qilishni esa bilmadi.</p>

<p>Akasi yonidan oʻtib ketayotib daftarga qaradi. Javobni aytmadi.
Uning oʻrniga qalam olib, ikkita
<span class="cn-word" data-tr="miqdorni koʻrsatuvchi choʻzinchoq toʻgʻri toʻrtburchak">tasma</span>
chizdi — biri pastda, biri tepada. Tepadagisi sal uzunroq edi.</p>

<p>«Mana bu — kichik <span class="cn-word" data-tr="butundan bir kishiga tegadigan qism">ulush</span>», dedi u pastdagini koʻrsatib. «Bu esa
katta ulush. Ular orasidagi
<span class="cn-word" data-tr="ikki miqdorning bir-biridan qanchaga koʻpligi">farq</span>
qayerda turibdi?»</p>

<p>Jasur uzun tasmaning oxiridagi ortiqcha uchni koʻrsatdi.</p>

<p>«Ana. Uni qirqib tashla».</p>

<p>Jasur bir zum jim qoldi. Keyin daftarga yozdi: agar ortiqcha 16 ni
olib tashlasa, ikkita <b>bir xil</b> tasma qoladi. Va ularning
<span class="cn-word" data-tr="qoʻshish amalining natijasi">yigʻindi</span>si
84 emas, <strong>68</strong> boʻladi.</p>

<p>Qolgani oson edi: 68 ÷ 2 = <strong>34</strong>. Bu — kichik ulush.
Katta ulush esa 34 + 16 = <strong>50</strong>.</p>

<p><span class="cn-word" data-tr="javobni masala shartlariga qaytarib qoʻyish">Tekshirish</span>ni
oʻzi qildi: 34 + 50 = 84 ✓ va 50 − 34 = 16 ✓ Ikkala
<span class="cn-word" data-tr="bajarilishi kerak boʻlgan bogʻlanish">shart</span>
ham bajarilgan.</p>

<p>«Men bu 68 ni oldin ham topgan edim», dedi Jasur biroz xafa boʻlib.
«Faqat u bilan nima qilishni bilmadim».</p>

<p>«Chunki u faqat son edi», dedi akasi. «Chizmada esa u
<span class="cn-word" data-tr="chizmaning teng qismlaridan biri">boʻlak</span>ka
aylandi. Sonlar bir-biriga oʻxshaydi, uzunliklar esa oʻxshamaydi —
koʻz ularni darrov ajratadi».</p>

<p>U ketayotib qoʻshib qoʻydi: «<span class="cn-word" data-tr="masaladagi miqdorlarning rasm koʻrinishi">Chizma</span>
javobni bermaydi. U shunchaki masalani koʻrinadigan qilib qoʻyadi.
Qolganini baribir oʻzing qilasan».</p>

<p>Jasur daftarning chetiga kichkina yozuv qoldirdi:
«<span class="cn-word" data-tr="tenglikdan oshgan qism">ortiqcha</span>ni
qirq, qolganini teng boʻl». Keyingi masalada u qalamni sondan oldin
oldi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-88 — tezlik                                          KUNDALIK
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Maktabga velosipedda",
        "summary": (
            "PM-88 matni. Kundalik: Sherbek bir hafta davomida maktabga "
            "ketgan vaqtini yozib boradi va bir xil yoʻlda tezligi nega "
            "har kuni boshqacha chiqishini tushunadi."
        ),
        "order":   88,
        "grammar": [
            {
                "pattern":  "v = S ÷ t (vaqt soatga oʻgirilgandan keyin)",
                "meaning":  "Tezlik — bir soatda bosiladigan masofa. "
                            "Masofa km da, vaqt esa minutda berilgan "
                            "boʻlsa, avval minut soatga oʻgiriladi: "
                            "minut ÷ 60.",
                "examples": [
                    "20 minut = 20 ÷ 60 = 1/3 soat → 6 ÷ (1/3) = 18 km/soat",
                    "30 minut = 0,5 soat → 6 ÷ 0,5 = 12 km/soat",
                    "24 minut = 0,4 soat → 6 ÷ 0,4 = 15 km/soat",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sherbek nima uchun har kuni vaqtni yozib bordi?",
                "choices": [
                    "Otasi shunday buyurgani uchun",
                    "Maktabga kechikmaslik uchun",
                    "Bir xil yoʻlda tezligi har xil chiqishini tekshirish uchun",
                    "Yangi velosiped sotib olish uchun",
                ],
                "answer": 2,
                "explanation": "Yoʻl har kuni oʻsha 6 km edi. Sherbekni "
                               "qiziqtirgani — masofa oʻzgarmasa ham "
                               "tezlik nega oʻzgarishi, ya'ni v = S ÷ t "
                               "da vaqtning roli.",
            },
            {
                "text": "Chorshanba kuni Sherbekning tezligi qancha "
                        "boʻlgan?",
                "choices": ["12 km/soat", "15 km/soat", "18 km/soat",
                            "30 km/soat"],
                "answer": 0,
                "explanation": "Chorshanbada yoʻlga 30 minut ketgan. "
                               "30 minut = 0,5 soat, demak "
                               "v = 6 ÷ 0,5 = 12 km/soat. «30 km/soat» "
                               "— 6 ni 0,2 ga boʻlganda yoki minutni "
                               "soatga oʻgirmaganda chiqadigan "
                               "bemaʼnilik.",
            },
            {
                "text": "Dushanba bilan chorshanba orasidagi tezlik farqi "
                        "qancha?",
                "choices": ["3 km/soat", "4 km/soat", "5 km/soat",
                            "6 km/soat"],
                "answer": 3,
                "explanation": "Dushanba 18 km/soat, chorshanba "
                               "12 km/soat. Farq: 18 − 12 = 6 km/soat. "
                               "Yoʻl bir xil boʻlsa ham, vaqt 20 dan "
                               "30 minutga chiqqani tezlikni ancha "
                               "tushirgan.",
            },
        ],
        "body": """
<p><b>Dushanba.</b> Bugundan boshlab maktabga velosipedda qatnayman.
Uydan maktabgacha <strong>6</strong> km — buni otam
<span class="cn-word" data-tr="mashinadagi bosib oʻtilgan yoʻl hisoblagichi">spidometr</span>
bilan oʻlchab bergan. Bugun yoʻlga <strong>20</strong> minut ketdi.</p>

<p>Hisobladim. Avval
<span class="cn-word" data-tr="oʻlchov nomi: km, soat, minut">birlik</span>ni
moslash kerak ekan: 20 minut = 20 ÷ 60 = <sup>1</sup>/<sub>3</sub>
soat. Keyin
<span class="cn-word" data-tr="bir soatda bosiladigan masofa">tezlik</span>ni
<span class="cn-word" data-tr="miqdorlar orasidagi doimiy bogʻlanish yozuvi">formula</span>ga
qoʻydim: 6 ÷ <sup>1</sup>/<sub>3</sub> = <strong>18</strong>
<span class="cn-word" data-tr="bir soatda bosiladigan kilometrlar">km/soat</span>.</p>

<p><b>Seshanba.</b> Yomgʻir yogʻdi, avtobusda ketdim. Hisob yoʻq.</p>

<p><b>Chorshanba.</b> Kuchli shamol — roppa-rosa yuzimga qarab esdi.
Yoʻlga <strong>30</strong> minut ketdi.</p>

<p>30 minut = 0,5 soat, demak tezligim 6 ÷ 0,5 = <strong>12</strong>
km/soat. Dushanbaga qaraganda 6 km/soat kam — sezilarli
<span class="cn-word" data-tr="ikki miqdorning bir-biridan qanchaga koʻpligi">farq</span>.</p>

<p>Bu meni ajablantirdi.
<span class="cn-word" data-tr="bosib oʻtilgan yoʻl uzunligi">Masofa</span>
oʻzgarmadi-ku — oʻsha 6 km. Demak tezlikni faqat
<span class="cn-word" data-tr="harakat davom etgan muddat">vaqt</span>
oʻzgartirgan ekan. Formulada ham shunday: v = S ÷ t, va t pastda
turibdi. t katta boʻlsa, v kichik boʻladi.</p>

<p><b>Payshanba.</b> Doʻstim Bekzod bilan birga ketdik, yoʻlda
gaplashib bordik. 40 minut. Tezlik: 40 minut =
<sup>2</sup>/<sub>3</sub> soat, 6 ÷ <sup>2</sup>/<sub>3</sub> =
<strong>9</strong> km/soat. Eng sekin kunim.</p>

<p><b>Juma.</b> Kechikayotgan edim.
<span class="cn-word" data-tr="tezlikni oshirish">Tezlashdim</span>
va <strong>24</strong> minutda yetib bordim. 24 minut = 24 ÷ 60 =
0,4 soat, demak 6 ÷ 0,4 = <strong>15</strong> km/soat.</p>

<p>Haftaning oxirida daftarga hammasini yozdim: 18, 12, 9 va 15
km/soat. Toʻrt kun, bitta yoʻl, toʻrt xil son.</p>

<p>Keyin bitta xatoni ham topdim. Dushanba kuni men avval 6 × 20 = 120
deb yozgan edim va «120 km/soat» chiqqanidan xursand boʻlgandim. Bu —
poyezdning tezligi. Velosipedda unday yurib boʻlmaydi: demak
<span class="cn-word" data-tr="hisob natijasi">javob</span>
<span class="cn-word" data-tr="aql bovar qiladigan, haqiqatga mos">mantiqiy</span> emas edi.</p>

<p>Xato oddiy ekan: <b>tezlik soatda, vaqt esa minutda</b> olingan.
Ikkalasini bir xil birlikka keltirmaguncha formulaga qoʻyib
boʻlmaydi.</p>

<p>Otam buni eshitib kuldi: «Javob mantiqiymi degan savolni har doim
ber. Velosipedda 120 km/soat — bu javob emas,
<span class="cn-word" data-tr="hisobda yoʻl qoʻyilgan notoʻgʻrilik">xato</span>ning
oʻzi baqirib turibdi».</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-89 — uchrashuv                                          HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ikki avtobus, bitta yoʻl",
        "summary": (
            "PM-89 matni. Hikoya: buvisining oldiga ketayotgan Dilnoza "
            "yoʻlda amakisining avtobusi bilan uchrashishi kerak. "
            "Uchrashuv soatini u avtobusda oʻtirib hisoblab chiqadi."
        ),
        "order":   89,
        "grammar": [
            {
                "pattern":  "t = ora ÷ (v₁ + v₂)",
                "meaning":  "Qarama-qarshi harakatda ikki jism orasidagi "
                            "masofa har soatda tezliklarning yigʻindisiga "
                            "teng miqdorda kamayadi.",
                "examples": [
                    "yaqinlashish tezligi: 55 + 65 = 120 km/soat",
                    "t = 360 ÷ 120 = 3 soat",
                    "07:00 + 3 soat = 10:00 — uchrashuv payti",
                ],
            },
        ],
        "questions": [
            {
                "text": "Dilnoza uchrashuv vaqtini qanday topdi?",
                "choices": [
                    "Amakisiga telefon qilib soʻradi",
                    "Yoʻlning oʻrtasini topib, uni 55 ga boʻldi",
                    "Ikki tezlikning oʻrtachasini oldi",
                    "Orani ikki tezlikning yigʻindisiga boʻldi",
                ],
                "answer": 3,
                "explanation": "Har soatda ora 55 + 65 = 120 km ga "
                               "kamayadi, shuning uchun "
                               "360 ÷ 120 = 3 soat. Yoʻlning oʻrtasini "
                               "olish notoʻgʻri boʻlardi — avtobuslar "
                               "oʻrtada uchrashmaydi.",
            },
            {
                "text": "Avtobuslar soat nechada uchrashadi?",
                "choices": ["09:00 da", "10:00 da", "11:00 da",
                            "12:00 da"],
                "answer": 1,
                "explanation": "Ikkalasi ham 07:00 da chiqqan va 3 soat "
                               "yurgan: 07:00 + 3 = 10:00.",
            },
            {
                "text": "Uchrashuv joyi Dilnozaning shahridan qancha "
                        "narida?",
                "choices": ["150 km", "160 km", "165 km", "195 km"],
                "answer": 2,
                "explanation": "Dilnozaning avtobusi 55 km/soat bilan "
                               "3 soat yurgan: 55 × 3 = 165 km. "
                               "Amakisiniki 65 × 3 = 195 km. "
                               "Tekshirish: 165 + 195 = 360 ✓ "
                               "«180 km» — yoʻlning oʻrtasi, lekin "
                               "uchrashuv oʻrtada emas.",
            },
        ],
        "body": """
<p>Dilnoza ertalab soat yettida avtobusga chiqdi. U buvisining oldiga
ketayotgan edi. Ikki shahar orasi — <strong>360</strong> km.</p>

<p>Yoʻlga chiqishdan oldin amakisi telefon qilgan edi: «Men ham
bugun ertalab yettida yoʻlga chiqaman, faqat qarshi tomondan. Bir-birimizni
yoʻlda koʻramiz — men oynadan qoʻl silkitaman».</p>

<p>Dilnoza oʻrindiqqa oʻtirib oldi va oʻyladi: qachon qaramoq kerak?
Uch soatdan keyinmi, besh soatdanmi?</p>

<p>Haydovchidan <span class="cn-word" data-tr="bir soatda bosiladigan masofa">tezlik</span>ni
soʻradi — <strong>55</strong> km/soat.
Amakisiga yozdi, u <strong>65</strong> km/soat bilan
ketayotgan ekan.</p>

<p>Dilnoza avval yoʻlning
<span class="cn-word" data-tr="kesmani teng ikkiga boʻluvchi nuqta">oʻrta nuqta</span>sini
hisoblamoqchi boʻldi: 360 ÷ 2 = 180 km. Lekin darrov toʻxtadi. Amakisining avtobusi tezroq ketyapti —
demak u koʻproq <span class="cn-word" data-tr="bosib oʻtilgan yoʻl uzunligi">masofa</span> bosadi va ular oʻrtada emas, Dilnozaga
<b>yaqinroq</b> joyda uchrashadi.</p>

<p>Shunda u boshqa savol berdi: <b>oramizdagi masofa har soatda
qanchaga kamayadi?</b></p>

<p>Javob oson edi. Har soatda Dilnozaning avtobusi 55 km, amakisiniki
65 km yaqinlashadi. Demak
<span class="cn-word" data-tr="ikki jism orasidagi masofa">ora</span>
soatiga 55 + 65 = <strong>120</strong> km ga qisqaradi. Bu —
<span class="cn-word" data-tr="orani kamaytirish tezligi, v₁ + v₂">yaqinlashish tezligi</span>.</p>

<p>Endi butun 360 km shu tezlikda yopiladi:
360 ÷ 120 = <strong>3</strong> soat.</p>

<p>Ular soat yettida chiqishgan edi, demak
<span class="cn-word" data-tr="ikki jismning bir nuqtada toʻqnash kelishi">uchrashuv</span>
soat <strong>10:00</strong> da boʻladi.</p>

<p>Dilnoza <span class="cn-word" data-tr="ikki jism toʻqnash keladigan nuqta">uchrashuv joyi</span>ni ham hisobladi. Uning avtobusi 55 × 3 =
<strong>165</strong> km, amakisiniki 65 × 3 = <strong>195</strong> km
bosadi. Qoʻshib
<span class="cn-word" data-tr="javobni masala shartlariga qaytarib qoʻyish">tekshirdi</span>:
165 + 195 = 360 ✓ Roppa-rosa ikki shahar orasi.</p>

<p>Demak uchrashuv joyi oʻrtadagi 180 km da emas, undan 15 km
berida ekan — u oʻylagandek, tezroq avtobus koʻproq yoʻl bosgan.</p>

<p>Soat 09:55 da Dilnoza oynaga yaqinroq surildi va qarshi
<span class="cn-word" data-tr="harakat yoʻnalishi">yoʻnalish</span>ga
tikildi.</p>

<p>10:02 da amakisining avtobusi oʻtib ketdi. Amakisi haqiqatan qoʻl
silkitdi. Ikki daqiqalik farq Dilnozani ajablantirmadi: avtobus
har doim ham roppa-rosa <span class="cn-word" data-tr="tezligi oʻzgarmaydigan harakat">tekis</span>
yurmaydi — yoʻlda bir marta sekinlashgan edi.</p>

<p>Buvisiga yetib borgach, u birinchi boʻlib shu hisobni aytib berdi.
Buvisi tinglab turdi-da, dedi: «Men bunday hisoblarni bilmayman. Lekin
sen kelishingni bilardim — hisobsiz ham».</p>
""",
    },
]
