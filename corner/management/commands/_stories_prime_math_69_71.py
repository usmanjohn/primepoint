# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-69, PM-70, PM-71 (Blok E: Geometriya).

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 69 — hikoya, 70 — tarix (haqiqiy voqealar qayta hikoya qilingan),
      71 — ilmiy-ommabop. Oldingi uchlik sharh/hikoya/kundalik edi.

⚠️ Kumulyativ — bu uchligida tartib qatʼiy:
   • 69-matnda DOIRA ham, π ham YOʻQ — faqat trapetsiya yuzasi;
   • 70-matnda faqat π = L ÷ d munosabati va doiraning qismlari.
     ⛔ Doira YUZASI bu matnda yoʻq;
   • 71-matnda ikkala formula ham: L = π × d va S = π × r².
⚠️ `grammar.pattern` va `examples` ekranlanadi — <sup> emas, Unicode ²
   yoziladi.
⚠️ Savollar SAQLANGAN TARTIBDA koʻrsatiladi (mashqlardan farqli) —
   `answer` indekslari qoʻlda oʻzgartirilgan: 69 → 2/1/1, 70 → 1/2/0,
   71 → 3/2/1.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_69_71.py --author=prime
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
    # PM-69 — trapetsiya yuzasi                                  HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Notekis dala",
        "summary": (
            "PM-69 matni. Hikoya: Bekzod otasi bilan dalani oʻlchaydi va "
            "trapetsiyani toʻgʻri toʻrtburchakdek hisoblab, urugʻni ortiqcha "
            "olishiga sal qoladi."
        ),
        "order":   69,
        "grammar": [
            {
                "pattern":  "S = (a + b) ÷ 2 × h",
                "meaning":  "Trapetsiyaning yuzasi: ikkala asosni qoʻshamiz, "
                            "ikkiga boʻlamiz, balandlikka koʻpaytiramiz. "
                            "Bitta asosning oʻzi yetarli emas.",
                "examples": [
                    "(34 + 26) ÷ 2 × 20 = 30 × 20 = 600 m²",
                    "xato yoʻl: 34 × 20 = 680 m² — 80 m² ortiqcha",
                    "urugʻ: 600 ÷ 100 × 3 = 18 kg",
                ],
            },
        ],
        "questions": [
            {
                "text": "Bekzodning birinchi hisobida qanday xato bor edi?",
                "choices": [
                    "Balandlikni notoʻgʻri oʻlchadi",
                    "Asoslarni bir-biriga qoʻshib yubordi",
                    "Faqat uzun asosni ishlatdi, qisqasini eʼtiborsiz "
                    "qoldirdi",
                    "Yuzani ikkiga boʻlishni unutdi",
                ],
                "answer": 2,
                "explanation": "Bekzod 34 × 20 deb hisobladi, yaʼni dalani "
                               "hamma joyida 34 metr keng deb oʻyladi. "
                               "Aslida ariqqa qaragan tomoni atigi 26 metr. "
                               "Trapetsiyada ikkala asos ham hisobga "
                               "olinadi.",
            },
            {
                "text": "Dalaning haqiqiy yuzasi qancha?",
                "choices": ["520 m²", "600 m²", "680 m²", "1200 m²"],
                "answer": 1,
                "explanation": "(34 + 26) ÷ 2 × 20 = 30 × 20 = 600 m². "
                               "«680 m²» — Bekzodning xato hisobi "
                               "(34 × 20), «1200 m²» esa ikkiga boʻlish "
                               "unutilgan holat.",
            },
            {
                "text": "Dalaga necha kilogramm urugʻ kerak?",
                "choices": ["6 kg", "18 kg", "20,4 kg", "36 kg"],
                "answer": 1,
                "explanation": "Har 100 m² ga 3 kg ketadi: 600 ÷ 100 = 6, "
                               "va 6 × 3 = 18 kg. «20,4 kg» — Bekzodning "
                               "katta hisobi boʻyicha chiqadigan miqdor, "
                               "yaʼni 2,4 kg ortiqcha urugʻ.",
            },
        ],
        "body": """
<p>Bekzod uchun bahor shanba kuni ertalab boshlandi: otasi uni dalaga
olib chiqdi va ruletkani qoʻliga tutqazdi.</p>

<p>«Urugʻ sotib olishdan oldin dalani oʻlchaymiz», — dedi otasi.</p>

<p>Dala toʻgʻri toʻrtburchak emas edi. Uning yoʻlga qaragan tomoni uzun,
ariqqa qaragan tomoni esa qisqa. Bu ikki tomon bir-biriga
<span class="cn-word" data-tr="hech qachon kesishmaydigan chiziqlar">parallel</span>
edi. Yon tomonlari qiya turardi.</p>

<p>«Bunday shaklning nomi bor, — dedi otasi. — Bu —
<span class="cn-word" data-tr="faqat bitta juft tomoni parallel toʻrtburchak">trapetsiya</span>.»</p>

<p>Bekzod oʻlchadi. Yoʻlga qaragan
<span class="cn-word" data-tr="trapetsiyaning parallel tomonlaridan biri">asos</span>
<strong>34</strong>
<span class="cn-word" data-tr="uzunlik birligi, 100 santimetr">metr</span>,
ariqqa qaragani <strong>26</strong> metr chiqdi. Ular orasidagi
<span class="cn-word" data-tr="ikki parallel tomon orasidagi perpendikulyar masofa">balandlik</span>
esa <strong>20</strong> metr edi.</p>

<p>U tez hisobladi: 34 × 20 = <strong>680</strong>
<span class="cn-word" data-tr="tomoni 1 metr boʻlgan kvadratning yuzasi">kvadrat metr</span>.</p>

<p>Otasi bosh chayqadi. «Sen dalani hamma joyida 34 metr keng deb
oʻyladingda. Qara — ariq tomonda atigi 26 metr bor.»</p>

<p>Toʻgʻri hisob boshqacha ekan. Trapetsiyada ikkala asos qoʻshiladi,
ikkiga boʻlinadi, keyin balandlikka koʻpaytiriladi:</p>

<p>(34 + 26) ÷ 2 × 20 = 30 × 20 = <strong>600</strong> kvadrat metr.</p>

<p>Bekzodning javobi <strong>80</strong> kvadrat metrga katta chiqqan
edi.</p>

<p>«Bu shunchaki sonmi?» — deb soʻradi Bekzod.</p>

<p>«Yoʻq, bu pul», — dedi otasi. Har 100 kvadrat metrga <strong>3</strong>
<span class="cn-word" data-tr="ogʻirlik birligi, 1000 gramm">kilogramm</span>
<span class="cn-word" data-tr="ekish uchun olinadigan don">urugʻ</span>
ketadi. Toʻgʻri
<span class="cn-word" data-tr="shakl egallagan joy oʻlchovi">yuza</span>
boʻyicha: 600 ÷ 100 × 3 = <strong>18</strong> kilogramm. Bekzodning
hisobi boʻyicha esa 680 ÷ 100 × 3 = <strong>20,4</strong> kilogramm —
ikki yarim kilogrammga yaqin ortiqcha.</p>

<p>«Bir dala uchun koʻp emas, — dedi otasi. — Lekin dala oʻnta boʻlsa,
yigirma besh kilogramm urugʻni yerga tashlagan boʻlasan.»</p>

<p>Kechqurun Bekzod daftariga
<span class="cn-word" data-tr="qoida qisqartirib yozilgan koʻrinishi">formula</span>ni
yozib qoʻydi. Uning tagiga esa oʻzi uchun bitta jumla qoʻshdi:
«Ikkala tomonga ham qara.»</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-70 — π ning tarixi                                       TARIX
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Arqon, gʻildirak va π ning tarixi",
        "summary": (
            "PM-70 matni. Tarix: π ni izlashning toʻrt ming yillik yoʻli — "
            "Bobildan Misr papirusigacha, Arximeddan Samarqanddagi Jamshid "
            "al-Koshiygacha. Haqiqiy voqealar qayta hikoya qilingan."
        ),
        "order":   70,
        "grammar": [
            {
                "pattern":  "π = L ÷ d ≈ 3,14",
                "meaning":  "Har qanday aylananing uzunligi oʻz diametridan "
                            "necha marta katta boʻlsa, oʻsha son — π. "
                            "Doiraning kattaligi ahamiyatsiz: natija doim "
                            "bir xil.",
                "examples": [
                    "157 ÷ 50 = 3,14 (gʻildirak: ip 157 sm, diametri 50 sm)",
                    "Arximed: π 3,1408 bilan 3,1429 orasida",
                    "al-Koshiy, 1424-yil: 16 xona aniqlikda",
                ],
            },
        ],
        "questions": [
            {
                "text": "Arximed π ni qanday usul bilan chegaralagan?",
                "choices": [
                    "Aylanaga arqon oʻrab, uni yozib oʻlchagan",
                    "Aylananing ichiga va tashqarisiga koʻp tomonli "
                    "shakllar chizgan",
                    "Koʻp sonli gʻildiraklarni oʻlchab, oʻrtasini olgan",
                    "Aylanani teng boʻlaklarga kesib chiqqan",
                ],
                "answer": 1,
                "explanation": "Ichkaridagi shaklning perimetri aylanadan "
                               "qisqa, tashqaridagisiniki uzun — demak "
                               "aylananing uzunligi shu ikkisining "
                               "orasida. Tomonlar sonini 96 taga yetkazib, "
                               "Arximed π ni 3,1408 va 3,1429 orasiga "
                               "siqib qoʻygan.",
            },
            {
                "text": "Diametri 80 santimetr boʻlgan gʻildirakning atrofi "
                        "taxminan qancha? (π ≈ 3,14)",
                "choices": ["125,6 sm", "160 sm", "251,2 sm", "502,4 sm"],
                "answer": 2,
                "explanation": "π = L ÷ d munosabatidan L = π × d = "
                               "3,14 × 80 = 251,2 sm. «125,6 sm» — diametr "
                               "oʻrniga radius (40 sm) ishlatilgan, "
                               "«160 sm» — π umuman qoʻllanmagan.",
            },
            {
                "text": "Bobilning 3,125 qiymati bilan Misrning 3,16 "
                        "qiymatidan qaysi biri haqiqiy π ga yaqinroq?",
                "choices": [
                    "Bobilniki",
                    "Misrniki",
                    "Ikkalasi bir xil darajada yaqin",
                    "Matndan aniqlab boʻlmaydi",
                ],
                "answer": 0,
                "explanation": "π ≈ 3,1416. Bobilning farqi: "
                               "3,1416 − 3,125 = 0,0166. Misrning farqi: "
                               "3,16 − 3,1416 = 0,0184. Demak Bobilniki "
                               "biroz yaqinroq — garchi u ancha oldin "
                               "olingan boʻlsa ham.",
            },
        ],
        "body": """
<p>Qadimgi ustalar bir narsani juda erta sezishgan: dumaloq narsaning
atrofiga
<span class="cn-word" data-tr="oʻralgan yoʻgʻon ip">arqon</span>
oʻrasang, arqon uning enidan taxminan uch marta uzun chiqadi.</p>

<p>Buni bugun ham tekshirish mumkin.
<span class="cn-word" data-tr="markazdan oʻtgan eng uzun kesma">Diametr</span>i
<strong>50</strong> santimetr boʻlgan gʻildirakka ip oʻrang, keyin ipni
yozib oʻlchang: <strong>157</strong> santimetr. Endi boʻling:
157 ÷ 50 = <strong>3,14</strong>.</p>

<p>Boshqa gʻildirak oling — natija oʻsha. Stakan oling — yana oʻsha.
Bu son har qanday
<span class="cn-word" data-tr="markazdan bir xil uzoqlikdagi nuqtalar chizigʻi">aylana</span>da
bir xil chiqadi va uni
<span class="cn-word" data-tr="aylana uzunligining diametrga nisbati, ≈ 3,14">π (pi)</span>
deb atashadi.</p>

<p>Uni aniq bilishga esa toʻrt ming yil ketgan.</p>

<p>Bobilliklar taxminan 3800 yil oldin π ni <strong>3,125</strong> deb
olishgan. Misrliklarning Ahmes
<span class="cn-word" data-tr="qadimda yozuv uchun ishlatilgan oʻsimlik varagʻi">papirus</span>ida
(taxminan 3700 yil oldin) <strong>3,16</strong> ga yaqin qiymat bor.
Ikkalasi ham oʻlchash yoʻli bilan topilgan — ip va chizgʻich bilan.</p>

<p>Yunon olimi
<span class="cn-word" data-tr="qadimgi yunon matematigi va muhandisi">Arximed</span>
birinchi boʻlib boshqacha yoʻl tutgan. U aylananing ichiga va tashqarisiga
96 tomonli shakl chizgan. Ichkaridagining
<span class="cn-word" data-tr="shakl chegarasining uzunligi">perimetr</span>i
aylanadan qisqa, tashqaridagisiniki esa uzun. Shu qisqichni siqib borib,
u π ning <strong>3,1408</strong> bilan <strong>3,1429</strong> orasida
ekanini isbotlagan — oʻlchamasdan, faqat mulohaza bilan.</p>

<p>Eng aniq natija bizga yaqin joyda olingan.
<span class="cn-word" data-tr="Samarqandda ishlagan matematik va astronom">Jamshid al-Koshiy</span>
Ulugʻbek
<span class="cn-word" data-tr="osmon jismlarini kuzatadigan ilmiy muassasa">rasadxona</span>sida
ishlagan va 1424-yilda π ni <strong>16</strong> xona aniqlikda hisoblab
chiqqan. Bu
<span class="cn-word" data-tr="eng yaxshi natija">rekord</span>
dunyoda qariyb 180 yil buzilmagan.</p>

<p>Bugun kompyuterlar π ning trillionlab xonasini biladi. Lekin
<span class="cn-word" data-tr="texnika sohasida ishlaydigan mutaxassis">muhandis</span>lar
amalda oʻn besh xonadan koʻpini ishlatmaydi — hatto sayyoralararo
uchishlarni hisoblashga ham shuncha yetadi.</p>

<p>Maktab uchun esa <strong>3,14</strong> kifoya. Toʻrt ming yillik
izlanish shu uch raqamda yashaydi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-71 — L va S ish boshida                          ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Gʻildirak necha marta aylanadi",
        "summary": (
            "PM-71 matni. Ilmiy-ommabop: velosiped gʻildiragi bir aylanishda "
            "qancha yoʻl bosadi, velosiped kompyuteri masofani qanday sanaydi "
            "va tormoz diskining yuzasi nega muhim."
        ),
        "order":   71,
        "grammar": [
            {
                "pattern":  "L = π × d va S = π × r²",
                "meaning":  "Bitta doirada ikkita savol bor: chegarasi qancha "
                            "uzun (L, metrlarda) va ichi qancha keng "
                            "(S, kvadrat metrlarda).",
                "examples": [
                    "gʻildirak: 3,14 × 0,5 = 1,57 m — bir aylanishdagi yoʻl",
                    "1570 ÷ 1,57 = 1000 marta aylanadi",
                    "tormoz diski: 3,14 × 8² = 200,96 sm²",
                ],
            },
        ],
        "questions": [
            {
                "text": "Velosiped kompyuteri bosib oʻtilgan masofani qanday "
                        "hisoblaydi?",
                "choices": [
                    "Vaqtni tezlikka koʻpaytiradi",
                    "Yoʻlni sunʼiy yoʻldosh orqali oʻlchaydi",
                    "Gʻildirakning diametrini aylanishlar soniga qoʻshadi",
                    "Aylanishlar sonini aylana uzunligiga koʻpaytiradi",
                ],
                "answer": 3,
                "explanation": "Datchik gʻildirakning har aylanishini "
                               "sanaydi, qurilma esa bu sonni bir "
                               "aylanishdagi yoʻlga — aylana uzunligiga — "
                               "koʻpaytiradi. Shuning uchun sozlashda "
                               "undan gʻildirak oʻlchami soʻraladi.",
            },
            {
                "text": "Diametri 50 santimetr boʻlgan gʻildirak 1570 metr "
                        "yoʻlda necha marta aylanadi?",
                "choices": ["314 marta", "500 marta", "1000 marta",
                            "3140 marta"],
                "answer": 2,
                "explanation": "Bir aylanishdagi yoʻl: 3,14 × 0,5 = 1,57 m. "
                               "Keyin 1570 ÷ 1,57 = 1000 marta. "
                               "«500 marta» — gʻildirak bir aylanishda "
                               "oʻz diametricha (0,5 m emas, 3,14 marta "
                               "koʻproq) yuradi deb oʻylashdan chiqadi.",
            },
            {
                "text": "Traktor gʻildiragining diametri 1,5 metr. U bir "
                        "aylanishda necha metr yuradi?",
                "choices": ["2,355 m", "4,71 m", "7,065 m", "9,42 m"],
                "answer": 1,
                "explanation": "L = π × d = 3,14 × 1,5 = 4,71 m. "
                               "«2,355 m» — diametr oʻrniga radius "
                               "ishlatilgan, «7,065 m» — yuza formulasi "
                               "(3,14 × 1,5²) bilan hisoblangan; u "
                               "kvadrat metr beradi, metr emas.",
            },
        ],
        "body": """
<p>Velosipedda ketayotib gʻildirak necha marta aylanishini
sanaganmisiz? Sanamasangiz ham boʻladi — buni hisoblab topsa
boʻladi.</p>

<p>Sherbekning velosipedi gʻildiragining diametri <strong>50</strong>
santimetr, yaʼni <strong>0,5</strong> metr.</p>

<p>Gʻildirak bir marta toʻliq aylanganda velosiped qancha yuradi?
Gʻildirakning atrofi qancha boʻlsa, shuncha — chunki u yerga xuddi
arqonni yozgandek tegib boradi. Demak kerakli kattalik —
<span class="cn-word" data-tr="aylananing atrofi, L = π × d">aylana uzunligi</span>:</p>

<p>L = 3,14 × 0,5 = <strong>1,57</strong> metr.</p>

<p>Sherbekning uyidan maktabgacha 1570 metr. Gʻildirak necha marta
aylanadi? 1570 ÷ 1,57 = <strong>1000</strong> marta.</p>

<p>Traktorning gʻildiragi kattaroq: diametri <strong>1,5</strong> metr.
Bir aylanishda u 3,14 × 1,5 = <strong>4,71</strong> metr yuradi — yaʼni
velosipednikidan roppa-rosa uch barobar koʻp. Shuning uchun katta
gʻildirak sekin aylansa ham, mashina tez yuradi.</p>

<p>Velosiped
<span class="cn-word" data-tr="masofa va tezlikni koʻrsatuvchi kichik qurilma">kompyuter</span>i
ham aynan shu hisobni bajaradi. Gʻildirakning bitta
<span class="cn-word" data-tr="gʻildirak markazini gardish bilan bogʻlovchi ingichka sim">spitsa</span>siga
kichkina
<span class="cn-word" data-tr="temirni oʻziga tortadigan jism">magnit</span>
qoʻyiladi, ramkaga esa
<span class="cn-word" data-tr="oʻzgarishni sezib, signal beradigan asbob">datchik</span>.
Gʻildirak har aylanganda magnit datchik yonidan oʻtadi va qurilma bitta
sanaydi. Soʻng u aylanishlar sonini aylana uzunligiga koʻpaytiradi —
<span class="cn-word" data-tr="bosib oʻtilgan yoʻl uzunligi">masofa</span>
tayyor.</p>

<p>Shuning uchun bunday kompyuterni sozlashda undan avval gʻildirak
oʻlchami soʻraladi. Notoʻgʻri oʻlcham kiritsangiz, u har kuni
notoʻgʻri masofa koʻrsatadi.</p>

<p>Gʻildirakda yana bitta doira bor —
<span class="cn-word" data-tr="tormozlashda ishqalanadigan dumaloq metall qism">tormoz diski</span>.
Uning <span class="cn-word" data-tr="markazdan aylanagacha masofa">radius</span>i
8 santimetr boʻlsa,
<span class="cn-word" data-tr="doira egallagan joy, S = π × r²">yuza</span>si
3,14 × 64 = <strong>200,96</strong> kvadrat santimetr. Tormozlaganda
hosil boʻlgan
<span class="cn-word" data-tr="haroratning koʻtarilishi natijasida chiqadigan energiya">issiqlik</span>
aynan shu yuza orqali havoga tarqaydi. Disk qancha katta boʻlsa, tormoz
shuncha yaxshi soviydi — poyga velosipedlarida disklar shuning uchun
kattaroq qilinadi.</p>

<p>Demak bitta gʻildirakda ikkita formula yashaydi: chegarasi uchun L,
ichi uchun S. Birinchisi metrda, ikkinchisi kvadrat metrda.</p>
""",
    },
]
