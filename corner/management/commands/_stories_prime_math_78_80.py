# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-78, PM-79, PM-80 (Blok F).

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 78 — kundalik, 79 — ilmiy-ommabop, 80 — sport.
Oldingi uchlik intervyu / ilmiy-ommabop / yangilik edi.

⚠️ Kumulyativ:
   • 78-matnda faqat oʻrta arifmetik. ⛔ MEDIANA va MODA soʻzlari YOʻQ;
   • 79-matnda oʻrtacha, mediana va moda birga;
   • 80-matnda tarqoqlik.
⚠️ Sonlar darsdagilardan boshqa — oʻquvchi tayyor javobni koʻchirmasligi
   uchun. Har uchala matnda ham yigʻindi qoʻlda tekshirilgan.
⚠️ Savollar SAQLANGAN TARTIBDA koʻrsatiladi — `answer` indekslari qoʻlda
   oʻzgartirilgan: 78 → 1/2/0, 79 → 2/0/1, 80 → 1/3/2.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_78_80.py --author=prime
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
    # PM-78 — oʻrta arifmetik                                 KUNDALIK
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Oʻrtacha baho — kundalik daftar",
        "summary": (
            "PM-78 matni. Kundalik: Dilnoza choraklik bahosini koʻtarmoqchi "
            "va hisoblab koʻradi — bitta «5» yetmasligi, ikkitasi ham "
            "yetmasligi uning uchun kutilmagan boʻladi."
        ),
        "order":   78,
        "grammar": [
            {
                "pattern":  "yigʻindi = oʻrtacha × sonlar soni",
                "meaning":  "Oʻrtacha maʼlum boʻlganda yigʻindini tiklash "
                            "mumkin. Kerakli yangi bahoni topish ham shu "
                            "yoʻl bilan: kelajakdagi yigʻindidan hozirgisini "
                            "ayirish kifoya.",
                "examples": [
                    "3 + 4 + 4 + 5 + 4 = 20; 20 ÷ 5 = 4",
                    "4,5 × 6 = 27; 27 − 20 = 7 — bunday baho yoʻq",
                    "20 + 5 + 5 = 30; 30 ÷ 7 ≈ 4,3",
                ],
            },
        ],
        "questions": [
            {
                "text": "Dilnozaning beshta bahosining oʻrtachasi qancha?",
                "choices": ["3,8", "4", "4,2", "20"],
                "answer": 1,
                "explanation": "Yigʻindi: 3 + 4 + 4 + 5 + 4 = 20, va "
                               "20 ÷ 5 = 4. «20» — yigʻindining oʻzi: "
                               "boʻlish qadami tushib qolganda shu chiqadi.",
            },
            {
                "text": "Nega bitta «5» oʻrtachani 4,5 ga koʻtara olmaydi?",
                "choices": [
                    "Chunki «5» eng yuqori baho emas",
                    "Chunki oʻqituvchi ruxsat bermaydi",
                    "Chunki buning uchun oltinchi baho 7 boʻlishi kerak, "
                    "bunday baho esa yoʻq",
                    "Chunki oʻrtacha faqat butun son boʻladi",
                ],
                "answer": 2,
                "explanation": "Oltita bahoning yigʻindisi 4,5 × 6 = 27 "
                               "boʻlishi kerak. Hozirgi yigʻindi 20, demak "
                               "yangi baho 27 − 20 = 7 boʻlishi kerak edi. "
                               "Bunday baho mavjud emas.",
            },
            {
                "text": "Dilnoza yana ikkita «5» olsa (jami yettita baho), "
                        "oʻrtachasi qancha boʻladi?",
                "choices": [
                    "taxminan 4,3",
                    "roppa-rosa 4,5",
                    "roppa-rosa 5",
                    "oʻzgarmaydi — 4",
                ],
                "answer": 0,
                "explanation": "Yangi yigʻindi: 20 + 5 + 5 = 30, baholar soni "
                               "esa 7. Demak 30 ÷ 7 = 4,28… — taxminan 4,3. "
                               "Ikkita aʼlo baho ham oʻrtachani 4,5 ga "
                               "yetkaza olmadi.",
            },
        ],
        "body": """
<p><b>12-noyabr.</b> Bugun matematika daftarimni oxirigacha varaqlab
chiqdim. Chorak tugashiga ikki hafta qoldi, men esa qanday baho
olishimni bilmayman.</p>

<p>Beshta <span class="cn-word" data-tr="oʻqituvchi qoʻygan natija">baho</span>
bor ekan: 3, 4, 4, 5 va yana 4. Bu mening butun
<span class="cn-word" data-tr="oʻquv yilining toʻrtdan bir qismi">chorak</span>lik
<span class="cn-word" data-tr="nechta qiymat borligi">sonlar soni</span>m.</p>

<p>Ularni qoʻshdim:
<span class="cn-word" data-tr="hamma sonning qoʻshilgani">yigʻindi</span>
<strong>20</strong> chiqdi. Beshta baho boʻlgani uchun 5 ga boʻldim:
20 ÷ 5 = <strong>4</strong>. Demak
<span class="cn-word" data-tr="yigʻindini sonlar soniga boʻlish">oʻrta arifmetik</span>im
toʻrt ekan.</p>

<p>Yomon emas. Lekin men 4,5 ni xohlayman — yaʼni
<span class="cn-word" data-tr="butun boʻlmagan, vergulli son">oʻnlik kasr</span>
bilan yozilgan bahoni.</p>

<p><b>13-noyabr.</b> Kecha kechqurun hisoblab koʻrdim va natija meni
hayratda qoldirdi.</p>

<p>Agar yana bitta baho olsam, baholar soni 6 ta boʻladi. Oʻrtacha 4,5
boʻlishi uchun yigʻindi qancha boʻlishi kerak? Buni
<span class="cn-word" data-tr="natijadan berilganni topish">teskari masala</span>
sifatida yechdim: yigʻindi = oʻrtacha × soni = 4,5 × 6 =
<strong>27</strong>.</p>

<p>Menda hozir 20 bor. Demak yangi baho 27 − 20 = <strong>7</strong>
boʻlishi kerak.</p>

<p>Yettilik baho yoʻq — bu
<span class="cn-word" data-tr="bajarib boʻlmaydigan shart">imkonsiz</span>
<span class="cn-word" data-tr="berilganidan javob topish topshirigʻi">masala</span>
ekan. Bitta baho bilan bu ishning iloji yoʻq.</p>

<p><b>14-noyabr.</b> Unda ikkita baho? Ikkita <b>5</b> olsam, yigʻindi
20 + 10 = <strong>30</strong>, baholar soni esa 7 ta boʻladi.
30 ÷ 7 = <strong>4,28</strong>… — taxminan <strong>4,3</strong>.</p>

<p>Yana yetmadi! Ikkita aʼlo baho ham meni 4,5 ga chiqara olmadi.</p>

<p>Endi tushundim: boshdagi «3» hali ham yigʻindining ichida oʻtiribdi va
u hech qayerga yoʻqolmaydi. Oʻrtacha —
<span class="cn-word" data-tr="hammasini baravar taqsimlash">tekislash</span>
degani, va bitta past baho butun qatorni pastga tortib turadi.</p>

<p><b>15-noyabr.</b> Bugun buvimga aytdim. U kuldi: «Demak dars
boshida yaxshi oʻqish kerak ekan-da, oxirida emas.»</p>

<p>Haq gap. Chorakning boshidagi bitta baho oxiridagi bahodan koʻra
koʻproq ogʻirlik qilar ekan — chunki keyin uni tuzatish uchun juda koʻp
<span class="cn-word" data-tr="birga qaraladigan sonlar roʻyxati">maʼlumot</span>
kerak boʻladi.</p>

<p>Baribir harakat qilaman. Hech boʻlmasa 4,3 ham 4 dan yaxshiroq.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-79 — mediana va moda                            ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "«Oʻrtacha maosh» qanday aldaydi",
        "summary": (
            "PM-79 matni. Ilmiy-ommabop: eʼlondagi «oʻrtacha maosh» rost "
            "boʻlishi va shu bilan birga chalgʻitishi mumkin — mediana va "
            "moda esa haqiqatni koʻrsatadi."
        ),
        "order":   79,
        "grammar": [
            {
                "pattern":  "mediana — saralangan qatorning oʻrtasidagi son",
                "meaning":  "Oʻrta arifmetikdan farqli oʻlaroq mediana "
                            "chetki songa deyarli berilmaydi: qanchalik "
                            "katta boʻlmasin, u faqat bitta oʻrin "
                            "egallaydi.",
                "examples": [
                    "4, 4, 4, 5, 5, 6, 6, 7, 49 — oʻrtadagisi 5",
                    "oʻrtacha: 90 ÷ 9 = 10",
                    "moda: 4 (uch marta uchradi)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Eʼlondagi «oʻrtacha maosh 10 million» degan jumla "
                        "haqidagi qaysi fikr toʻgʻri?",
                "choices": [
                    "Bu ochiqdan-ochiq yolgʻon",
                    "Bu toʻgʻri va hech qanday muammosi yoʻq",
                    "Bu rost, lekin toʻqqiz kishidan sakkiztasi bundan kam "
                    "oladi",
                    "Bu faqat direktorning maoshi",
                ],
                "answer": 2,
                "explanation": "Hisob toʻgʻri: 90 ÷ 9 = 10 million. Lekin "
                               "bu son bitta juda katta maosh hisobiga "
                               "koʻtarilgan, shuning uchun ishga kelayotgan "
                               "odam kutgan narsani koʻrsatmaydi.",
            },
            {
                "text": "Toʻqqiz maoshning medianasi qancha?",
                "choices": ["5 million", "6 million", "7 million",
                            "10 million"],
                "answer": 0,
                "explanation": "Maoshlar saralangan holda: 4, 4, 4, 5, 5, 6, "
                               "6, 7, 49. Toʻqqizta son bor, demak "
                               "oʻrtadagisi beshinchisi — 5 million. Yarmi "
                               "bundan koʻp, yarmi kam oladi.",
            },
            {
                "text": "Maoshlarning modasi qancha?",
                "choices": ["3 million", "4 million", "5 million",
                            "49 million"],
                "answer": 1,
                "explanation": "4 million uch marta uchradi — boshqa hech "
                               "bir qiymat bunchalik koʻp takrorlanmagan. "
                               "«3 million» — moda necha marta uchraganining "
                               "soni; moda esa qiymatning oʻzi.",
            },
        ],
        "body": """
<p>Ish eʼlonlarida tez-tez shunday jumlani uchratasiz: «Bizda oʻrtacha
maosh 10 million soʻm». Bu jumla rost boʻlishi mumkin — va shu bilan
birga sizni chalgʻitishi ham mumkin. Qanday qilib?</p>

<p>Kichik bir korxonani olaylik. U yerda toʻqqiz kishi ishlaydi. Maoshlar
(million soʻmda): <strong>4, 4, 4, 5, 5, 6, 6, 7</strong> va
<strong>49</strong>.</p>

<p>Oxirgisi —
<span class="cn-word" data-tr="korxonaga rahbarlik qiluvchi shaxs">direktor</span>niki.
Qolganlari oddiy
<span class="cn-word" data-tr="korxonada ishlaydigan kishi">xodim</span>lar.</p>

<p><span class="cn-word" data-tr="yigʻindini sonlar soniga boʻlish">Oʻrta arifmetik</span>ni
hisoblaymiz.
<span class="cn-word" data-tr="hamma qiymatning qoʻshilgani">Yigʻindi</span>:
4 + 4 + 4 + 5 + 5 + 6 + 6 + 7 + 49 = <strong>90</strong>. Toʻqqizta
odam: 90 ÷ 9 = <strong>10</strong> million.</p>

<p>Hisob mutlaqo toʻgʻri. Lekin endi diqqat qiling: toʻqqiz kishidan
<b>sakkiztasi</b> 10 milliondan kam oladi. Bitta juda katta maosh butun
<span class="cn-word" data-tr="birga qaraladigan qiymatlar">maʼlumot</span>ni
yuqoriga tortib ketdi. Bunday sonni
<span class="cn-word" data-tr="qolganlaridan keskin farq qiladigan qiymat">chetki son</span>
deyishadi.</p>

<p>Endi boshqa yoʻldan boramiz. Maoshlarni
<span class="cn-word" data-tr="oʻsish tartibida joylashtirish">saralab</span>
qoʻyamiz va roppa-rosa oʻrtadagisini olamiz. Toʻqqizta son bor, demak
beshinchisi oʻrtada turadi — bu <strong>5</strong> million. Bu son
<span class="cn-word" data-tr="saralangan qatorning oʻrtasidagi son">mediana</span>
deyiladi.</p>

<p>Mediananing kuchi shunda: direktorning maoshi 49 emas, 490 million
boʻlganida ham, mediana baribir 5 boʻlib qolardi. Chunki u faqat bitta
oʻrin egallaydi, oʻrtacha esa har bir soʻmni his qiladi.</p>

<p>Uchinchi son ham bor. Eng koʻp uchragan qiymat — <strong>4</strong>
million (uch marta). Bu
<span class="cn-word" data-tr="eng koʻp uchragan qiymat">moda</span>.
Ishga kirayotgan odam uchun bu ham foydali: «bu yerda koʻpchilik shuncha
oladi» degani.</p>

<p>Uchala son ham rost va uchalasi ham
<span class="cn-word" data-tr="maʼlumotni bitta son bilan tasvirlovchi kattalik">markaziy oʻlchov</span>
deb ataladi: oʻrtacha 10, mediana 5, moda 4. Lekin ular uch xil hikoya
aytadi.</p>

<p>Shuning uchun eʼlonni oʻqiganda savol bering:
<b>qaysi</b> oʻrtacha? Statistikada eng koʻp aldov yolgʻon sondan emas,
notoʻgʻri tanlangan rost sondan tugʻiladi.</p>

<p>Aynan shu sababdan davlat
<span class="cn-word" data-tr="bajarilgan ish haqidagi rasmiy maʼlumot">hisobot</span>larida
koʻpincha oʻrtacha maosh bilan birga mediana ham eʼlon qilinadi. Ikkalasi orasidagi farq qancha
katta boʻlsa, daromadlar shunchalik notekis taqsimlangan degani.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-80 — tarqoqlik                                          SPORT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ikki jamoa, bir xil oʻrtacha",
        "summary": (
            "PM-80 matni. Sport: ikkita basketbol jamoasining oʻrtacha "
            "ochkosi bir xil chiqadi, lekin murabbiy tarqoqlikka qarab "
            "butunlay boshqacha qaror qabul qiladi."
        ),
        "order":   80,
        "grammar": [
            {
                "pattern":  "tarqoqlik = eng katta − eng kichik",
                "meaning":  "Oʻrtacha maʼlumot qayerda turganini, tarqoqlik "
                            "esa u qanchalik yoyilganini aytadi. Ikki "
                            "toʻplamning oʻrtachasi teng boʻlsa ham, "
                            "tarqoqligi butunlay boshqa boʻlishi mumkin.",
                "examples": [
                    "Yulduz: 66 − 62 = 4",
                    "Shamol: 80 − 45 = 35",
                    "ikkalasining yigʻindisi ham 384, oʻrtachasi 64",
                ],
            },
        ],
        "questions": [
            {
                "text": "Ikki jamoaning oʻrtacha ochkosi qancha?",
                "choices": ["62", "64", "66", "384"],
                "answer": 1,
                "explanation": "Ikkalasining yigʻindisi ham 384, oʻyinlar "
                               "soni esa 6: 384 ÷ 6 = 64. Aynan shu tenglik "
                               "murabbiyni chalgʻitishi mumkin edi.",
            },
            {
                "text": "«Shamol» jamoasining tarqoqligi qancha?",
                "choices": ["4", "18", "25", "35"],
                "answer": 3,
                "explanation": "Eng koʻp ochkosi 80, eng kami 45: "
                               "80 − 45 = 35. «Yulduz»niki esa atigi "
                               "66 − 62 = 4.",
            },
            {
                "text": "Murabbiy nega finalga «Yulduz»ni tanladi?",
                "choices": [
                    "Chunki uning oʻrtacha ochkosi yuqoriroq",
                    "Chunki u koʻproq oʻyin oʻynagan",
                    "Chunki uning natijasi barqaror — eng yomon kuni ham "
                    "62 ochko",
                    "Chunki «Shamol» hech qachon 80 ochko urmagan",
                ],
                "answer": 2,
                "explanation": "Oʻrtachalar teng, shuning uchun tanlovni "
                               "tarqoqlik hal qildi. «Yulduz» har oʻyinda "
                               "62–66 ochko toʻplaydi; «Shamol»dan esa 80 "
                               "ham, 45 ham kutish mumkin.",
            },
        ],
        "body": """
<p>Viloyat basketbol
<span class="cn-word" data-tr="gʻolibni aniqlash uchun oʻtkaziladigan musobaqa">chempionat</span>ida
ikkita jamoa
<span class="cn-word" data-tr="musobaqaning eng soʻnggi, hal qiluvchi oʻyini">final</span>ga
daʼvogar edi: «Yulduz» va «Shamol».
<span class="cn-word" data-tr="jamoani tayyorlaydigan va boshqaradigan mutaxassis">Murabbiy</span>
ulardan birini tanlashi kerak edi.</p>

<p>Oltita oʻyindagi
<span class="cn-word" data-tr="sport oʻyinida toʻplangan ball">ochko</span>lar
shunday boʻldi.</p>

<p><b>Yulduz:</b> 62, 65, 64, 63, 66, 64.
<br><b>Shamol:</b> 45, 80, 50, 78, 62, 69.</p>

<p>Murabbiy avval
<span class="cn-word" data-tr="yigʻindini sonlar soniga boʻlish">oʻrta arifmetik</span>ni
hisobladi.</p>

<p>Yulduzning
<span class="cn-word" data-tr="hamma sonning qoʻshilgani">yigʻindi</span>si:
62 + 65 + 64 + 63 + 66 + 64 = <strong>384</strong>. Olti oʻyin:
384 ÷ 6 = <strong>64</strong>.</p>

<p>Shamolniki: 45 + 80 + 50 + 78 + 62 + 69 = <strong>384</strong>. Yana
oʻsha: 384 ÷ 6 = <strong>64</strong>.</p>

<p>Ikkala jamoaning oʻrtachasi <b>bir xil</b> chiqdi. Demak bu
<span class="cn-word" data-tr="birga qaraladigan sonlar guruhi">toʻplam</span>lar
teng kuchli?</p>

<p>Murabbiy sonlarga yana bir bor qaradi va boshqa savol berdi: bu
ochkolar qanchalik <b>yoyilgan</b>?</p>

<p>Yulduzda eng koʻpi 66, eng kami 62. Farqi: 66 − 62 = <strong>4</strong>.
Shamolda eng koʻpi 80, eng kami 45. Farqi: 80 − 45 = <strong>35</strong>.
Bu farq
<span class="cn-word" data-tr="eng katta va eng kichik qiymat farqi">tarqoqlik</span>
deb ataladi.</p>

<p>Mana endi hammasi oydinlashdi. Yulduz har oʻyinda deyarli bir xil
oʻynaydi — undan nima kutishni bilasiz. Bu
<span class="cn-word" data-tr="natijalarning bir-biriga yaqinligi">barqarorlik</span>.
Shamol esa bugun 80 ochko uradi, ertaga 45 — undan nima kutishni hech
kim bilmaydi.</p>

<p>Murabbiy finalga <b>Yulduz</b>ni oldi va sababini shunday
tushuntirdi: «Finalda bitta yomon kun butun mavsumni yoʻqqa chiqaradi.
Shamolning eng yaxshi kuni ajoyib, lekin men eng yomon kunidan
qoʻrqaman.»</p>

<p>Keyin qoʻshib qoʻydi: «Agar biz kuchliroq raqibga duch kelganimizda,
men Shamolni olardim. 64 ochko bilan ularni yengib boʻlmaydi —
80 kerak. Unda katta
<span class="cn-word" data-tr="qiymatlarning bir-biridan uzoqligi">yoyilganlik</span>
imkoniyat boʻlib qolardi.»</p>

<p>Demak katta tarqoqlik yomon ham, yaxshi ham emas. Savolga bogʻliq.
Aniq bir narsa bor: <b>bitta son</b> — oʻrtacha — ikki jamoani ajrata
olmadi. Ikkinchi son kerak boʻldi.</p>
""",
    },
]
