# -*- coding: utf-8 -*-
"""Matematika olami — birinchi uchta matn (1, 10, 15).

Toc: corner/management/commands/toc_matematika_olami.txt
Bu javon hech qaysi darsga bogʻlanmagan — mustaqil, zavq uchun oʻqiladi.
Uchta oiladan bittadan olindi, shunda javon boshidanoq rang-barang koʻrinadi:
  1  — buyuk matematiklar (al-Xorazmiy)
  10 — buyuk matematiklar (Gauss) … lekin janri boshqacha: sinfdagi voqea
  15 — tabiatdagi matematika (asalari uyasi)

⛔ AUDIO YOʻQ. Faktlar tekshirilgan; rivoyat boʻlsa, matnda shunday deyilgan.

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_01_03.py --author=prime
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
    # ══════════════════════════════════════════════════════════════════
    # 1 — Al-Xorazmiy                              BUYUK MATEMATIKLAR
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Al-Xorazmiy: «algoritm» soʻzi qayerdan kelgan",
        "summary": (
            "Har kuni ishlatiladigan ikkita soʻz — «algoritm» va «algebra» — "
            "bitta odam va bitta kitobdan qolgan. Tarixiy maʼlumotlarga asoslangan matn."
        ),
        "order":   1,
        "grammar": [
            {
                "pattern":  "algoritm ← Algoritmi ← al-Xorazmiy",
                "meaning":  "Olimning nomi lotinchada «Algoritmi» deb yozilgan. "
                            "Yevropada uning kitobidan hisob oʻrganganlar oʻzlarini "
                            "shu nom bilan atashgan, keyin esa soʻz «aniq qadamlar "
                            "ketma-ketligi» degan maʼnoni olgan.",
                "examples": [
                    "al-jabr → algebra",
                    "Algoritmi → algoritm",
                ],
            },
        ],
        "questions": [
            {
                "text": "«Algebra» soʻzi qayerdan kelib chiqqan?",
                "choices": [
                    "Olimning tugʻilgan joyi nomidan",
                    "Al-Xorazmiy kitobi nomidagi «al-jabr» soʻzidan",
                    "Yunoncha «son» soʻzidan",
                    "Lotincha «hisob» soʻzidan",
                ],
                "answer": 1,
                "explanation": "Kitob nomida ikki amal bor edi: <b>al-jabr</b> "
                               "(hadni bir tomondan ikkinchisiga oʻtkazish) va "
                               "al-muqobala (oʻxshash hadlarni qisqartirish). "
                               "Birinchisi butun fanning nomiga aylandi.",
            },
            {
                "text": "Kitob taxminan 820-yilda yozilgan. 2026-yilgacha necha yil oʻtdi?",
                "choices": ["846 yil", "1 106 yil", "1 206 yil", "1 216 yil"],
                "answer": 2,
                "explanation": "2026 − 820 = <b>1 206</b> yil. Ustunda ayirganda "
                               "oʻnliklardan qarz olish kerak boʻladi: "
                               "1 206 + 820 = 2 026 ✓",
            },
            {
                "text": "Al-Xorazmiyning hind raqamlari haqidagi kitobi nima uchun muhim boʻlgan?",
                "choices": [
                    "Unda birinchi marta geometriya taʼriflangan",
                    "Unda yulduzlar roʻyxati berilgan",
                    "U birinchi bosma kitob boʻlgan",
                    "U orqali oʻnlik sanoq tizimi va nol Yevropaga tarqalgan",
                ],
                "answer": 3,
                "explanation": "Rim raqamlari bilan hisoblash ogʻir edi. Oʻnta "
                               "raqamdan iborat, razryadga asoslangan tizim — biz "
                               "bugun ishlatadigan tizim — aynan shu yoʻl bilan "
                               "yoyilgan.",
            },
        ],
        "body": """
<p>Telefoningiz qaysi videoni koʻrsatishni tanlaganda, ekranda «algoritm» soʻzi paydo
boʻladi. Bu soʻz IT sohasidan emas — u kishining ismidan kelib chiqqan.</p>

<p>Muhammad ibn Muso <strong>al-Xorazmiy</strong> taxminan 780-yilda tugʻilgan. Nomining
oʻzi uning qayerdan ekanini aytib turibdi: Xorazm. Umrining katta qismini u Bagʻdodda,
<span class="cn-word" data-tr="Bagʻdoddagi ilm markazi va kutubxona (IX asr)">Bayt ul-hikma</span>
— «Donishmandlik uyi»da ishlab oʻtkazdi. U yerda olimlar butun dunyodan kelgan kitoblarni
tarjima qilar va oʻz asarlarini yozar edi.</p>

<p>Taxminan 820-yilda al-Xorazmiy bir kitob yozdi. Uning nomida ikkita amal bor edi:
<em>al-jabr</em> va <em>al-muqobala</em>. Birinchisi —
<span class="cn-word" data-tr="hadni tenglamaning bir tomonidan ikkinchisiga koʻchirish">al-jabr</span>,
ikkinchisi —
<span class="cn-word" data-tr="tenglamaning ikki tomonidagi oʻxshash hadlarni qisqartirish">al-muqobala</span>.
Kitob nomidagi birinchi soʻz butun bir fanning nomiga aylandi:
<strong>algebra</strong>.</p>

<p>Ikkinchi soʻz esa olimning oʻz ismidan qoldi. Uning asarlari Yevropaga yetib borganda,
nomi lotinchada <em>Algoritmi</em> deb yozilgan edi. Kitobdan hisob oʻrganganlar oʻzlarini
shu nom bilan atashardi, keyin esa soʻzning maʼnosi kengaydi:
<span class="cn-word" data-tr="masalani yechishning aniq, tartibli qadamlari">algoritm</span>
— natijaga olib boradigan aniq qadamlar ketma-ketligi.</p>

<p>Al-Xorazmiyning yana bir kitobi hind
<span class="cn-word" data-tr="0 dan 9 gacha boʻlgan belgilar">raqam</span>lari haqida edi.
Oʻsha paytda Yevropa rim raqamlari bilan hisoblardi: MCMXLVIII kabi yozuvda ustunda
qoʻshish deyarli imkonsiz. Oʻnta raqam va
<span class="cn-word" data-tr="raqamning sondagi oʻrni uning qiymatini belgilashi">razryad</span>ga
asoslangan tizim — biz bugun ishlatadigan tizim — aynan shu kitoblar orqali tarqaldi.
Uning ichida esa eng sokin, eng kuchli belgi bor edi:
<span class="cn-word" data-tr="boʻsh razryadni koʻrsatuvchi raqam">nol</span>.</p>

<p>Shunday qilib, bugun daftarda 2 350 000 deb yozganingizda ham, telefoningiz sizga video
tanlaganda ham — ikkalasining orqasida bitta xorazmlik olimning ishi turibdi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 10 — Gauss                                   SINFDAGI VOQEA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Karl Gauss: 1 dan 100 gacha bir daqiqada",
        "summary": (
            "Rivoyatga koʻra, oʻqituvchi sinfni tinchitmoqchi boʻlib bir soatlik "
            "vazifa berdi. Bir bola javobni bir daqiqada topdi — chunki u sanamadi, "
            "koʻrdi."
        ),
        "order":   10,
        "grammar": [
            {
                "pattern":  "1 + 2 + … + n = n × (n + 1) ÷ 2",
                "meaning":  "Ketma-ket sonlarni juftlab qoʻshish qoidasi: eng "
                            "chetdagilarni juft qilib olsangiz, har bir juftning "
                            "yigʻindisi bir xil chiqadi.",
                "examples": [
                    "1 + 100 = 101, juftlar soni 50 → 50 × 101 = 5 050",
                    "1 dan 20 gacha: 1 + 20 = 21, juftlar soni 10 → 10 × 21 = 210",
                ],
            },
        ],
        "questions": [
            {
                "text": "Gauss javobni nega tez topdi?",
                "choices": [
                    "Javobni oldindan yod olgan edi",
                    "Sonlarni juda tez qoʻsha olardi",
                    "Sonlarni chetdan juftlab, har bir juft bir xil yigʻindi berishini koʻrdi",
                    "Oʻqituvchi unga javobni aytib qoʻygan edi",
                ],
                "answer": 2,
                "explanation": "1 + 100, 2 + 99, 3 + 98 … — har bir juft 101 ga teng. "
                               "Bunday juftlar 50 ta, demak yigʻindi 50 × 101 = 5 050.",
            },
            {
                "text": "Xuddi shu usul bilan 1 dan 20 gacha boʻlgan sonlar yigʻindisini toping.",
                "choices": ["105", "200", "210", "220"],
                "answer": 2,
                "explanation": "1 + 20 = 21, juftlar soni 20 ÷ 2 = 10 ta, demak "
                               "10 × 21 = <b>210</b>. Tekshiring: 1+20, 2+19, 3+18 … "
                               "har biri 21.",
            },
            {
                "text": "Matnga koʻra, bu voqea haqida nima deyish toʻgʻri?",
                "choices": [
                    "Voqea kun-soatigacha hujjatlashtirilgan",
                    "Gaussning oʻzi buni kundaligida yozib qoldirgan",
                    "Bu butunlay toʻqib chiqarilgan",
                    "Bu rivoyat — qanday boʻlgani aniq maʼlum emas",
                ],
                "answer": 3,
                "explanation": "Matnda «rivoyatga koʻra» deyilgan. Hikoyaning tafsilotlari "
                               "turli manbalarda turlicha, lekin usulning oʻzi — haqiqiy "
                               "va bugun ham ishlatiladi.",
            },
        ],
        "body": """
<p>Rivoyatga koʻra, XVIII asr oxirida Germaniyaning bir maktabida oʻqituvchi shovqin
solayotgan sinfni tinchitmoqchi boʻldi va vazifa berdi:</p>

<p><strong>1 dan 100 gacha boʻlgan barcha sonlarni qoʻshinglar.</strong></p>

<p>Bu bir soatlik ish edi. Oʻqituvchi stulga oʻtirdi. Bir daqiqadan keyin toʻqqiz
yashar bola — <strong>Karl Fridrix Gauss</strong> (Carl Friedrich Gauss, 1777–1855) —
doskaga chiqib javobni yozdi: <strong>5 050</strong>.</p>

<p>U qanday qildi? Bittalab qoʻshgani yoʻq. U sonlarni chetlaridan
<span class="cn-word" data-tr="ikkitadan birga olib qarash">juftlab</span> qaradi:</p>

<p>1 + 100 = 101, 2 + 99 = 101, 3 + 98 = 101…</p>

<p>Har bir juftning <span class="cn-word" data-tr="qoʻshish natijasi">yigʻindi</span>si
bir xil — 101. Yuzta sondan nechta juft chiqadi? Ellikta. Demak javob:</p>

<p>50 × 101 = <strong>5 050</strong>.</p>

<p>Bu <span class="cn-word" data-tr="masalani yechishning qisqa va aniq yoʻli">usul</span>
har qanday ketma-ket sonlar uchun ishlaydi. Uni
<span class="cn-word" data-tr="harflar bilan yozilgan umumiy qoida">formula</span>
koʻrinishida ham yozish mumkin, lekin gap formulada emas — gap
<span class="cn-word" data-tr="berilganlarni yangicha koʻrish, boshqa tomondan qarash">nigoh</span>da.
Bittalab sanagan odam charchaydi; tuzilishni koʻrgan odam yechadi.</p>

<p>Gauss keyinchalik matematikaning deyarli har bir sohasida iz qoldirdi — sonlar
nazariyasi, geometriya, astronomiya, magnitizm. Uni «matematiklar shohi» deb atashadi.
Lekin uning eng mashhur hikoyasi hamon oʻsha sinf xonasidan: yechim koʻpincha koʻproq
mehnatda emas, boshqacha qarashda ekanini koʻrsatgani uchun.</p>

<p>Hikoyaning tafsilotlari turli kitoblarda turlicha aytiladi — bu rivoyat. Lekin usul
haqiqiy, va uni hozir siz ham ishlatishingiz mumkin.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 15 — Asalari uyasi                        TABIATDAGI MATEMATIKA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Nega asalarilar uyni olti burchakli quradi",
        "summary": (
            "Asalari geometriya oʻqimagan, lekin uning uyasi mumni eng tejaydigan "
            "shakldan iborat. Ilmiy-ommabop matn."
        ),
        "order":   15,
        "grammar": [
            {
                "pattern":  "Bir xil yuzada eng qisqa chegara",
                "meaning":  "Tekislikni boʻshliqsiz qoplay oladigan uchta muntazam "
                            "shakl bor: teng tomonli uchburchak, kvadrat va muntazam "
                            "olti burchak. Yuzalari teng boʻlsa, olti burchakning "
                            "perimetri eng qisqa — demak unga eng kam mum ketadi.",
                "examples": [
                    "Yuza 100 sm²: uchburchak ≈ 45,6 sm · kvadrat 40 sm · olti burchak ≈ 37,2 sm",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega aynan olti burchak — asalari uchun eng foydali shakl?",
                "choices": [
                    "Olti burchakli katak eng koʻp asal sigʻdiradi",
                    "Bu shaklni qurish eng oson",
                    "Boshqa shakllar boʻshliqsiz qoplanmaydi",
                    "Bir xil yuza uchun eng kam chegara, demak eng kam mum kerak boʻladi",
                ],
                "answer": 3,
                "explanation": "Uchala shakl ham tekislikni boʻshliqsiz qoplaydi. "
                               "Farq perimetrida: yuzalar teng boʻlganda olti "
                               "burchakning chegarasi eng qisqa, mum esa asalari uchun "
                               "qimmat.",
            },
            {
                "text": "Yuzasi 100 sm² boʻlgan kvadratning perimetri qancha?",
                "choices": ["20 sm", "40 sm", "50 sm", "400 sm"],
                "answer": 1,
                "explanation": "Yuzasi 100 sm² boʻlsa, tomoni 10 sm (10 × 10 = 100). "
                               "Perimetri 4 × 10 = <b>40</b> sm. Matnga koʻra olti "
                               "burchakniki taxminan 37,2 sm — undan qisqaroq.",
            },
            {
                "text": "Matnga koʻra, tekislikni boʻshliqsiz qoplay oladigan muntazam shakllar nechta?",
                "choices": ["Ikkita", "Uchta", "Beshta", "Cheksiz koʻp"],
                "answer": 1,
                "explanation": "Faqat uchta: teng tomonli uchburchak, kvadrat va "
                               "muntazam olti burchak. Masalan, muntazam beshburchaklar "
                               "orasida har doim boʻshliq qoladi.",
            },
        ],
        "body": """
<p>Asalari uyasini koʻrganmisiz? Yuzlab kataklar, hammasi bir xil, hammasi olti burchakli.
Asalari geometriya oʻqimagan. Unda nega aynan olti burchak?</p>

<p>Avval oddiy savol: qanday shakllar bilan tekislikni <em>boʻshliqsiz</em> qoplash
mumkin? Muntazam shakllar orasida bunga faqat uchtasi qodir: teng tomonli
<span class="cn-word" data-tr="uchta tomoni va uchta burchagi bor shakl">uchburchak</span>,
<span class="cn-word" data-tr="toʻrt tomoni teng, burchaklari toʻgʻri boʻlgan shakl">kvadrat</span>
va muntazam
<span class="cn-word" data-tr="olti tomoni va olti burchagi bor shakl">olti burchak</span>.
Muntazam beshburchaklarni qanchalik urinmang, orasida boʻshliq qoladi — boʻshliq esa
asalari uchun isrof.</p>

<p>Demak tanlov uchtadan iborat. Endi ikkinchi savol: qaysi biri eng arzon?</p>

<p>Asalari uchun eng qimmat narsa —
<span class="cn-word" data-tr="asalari ajratadigan modda; uyaning devori shundan quriladi">mum</span>.
Uni ishlab chiqarish juda koʻp asal talab qiladi. Demak katakning
<span class="cn-word" data-tr="shaklning chegarasi uzunligi">perimetr</span>i qancha qisqa
boʻlsa, shuncha yaxshi — chunki devor mumdan quriladi. Katakning
<span class="cn-word" data-tr="shakl ichidagi joy oʻlchovi">yuza</span>si esa, aksincha,
katta boʻlishi kerak: asal shu yerga sigʻadi.</p>

<p>Yuzasi bir xil — masalan, 100 sm² — boʻlgan uchta shaklning chegarasini oʻlchab
koʻraylik:</p>

<p>uchburchak ≈ <strong>45,6 sm</strong> · kvadrat = <strong>40 sm</strong> ·
olti burchak ≈ <strong>37,2 sm</strong></p>

<p>Olti burchak yutdi. Bir xil joy uchun unga eng kam devor kerak. Uyada minglab kataklar
borligini hisobga olsangiz, bu tejamkorlik bir necha kilogramm asalga teng.</p>

<p>Qizigʻi shundaki, «olti burchak eng tejamkor» degan fikr ikki ming yil davomida
<span class="cn-word" data-tr="isbotlanmagan, lekin toʻgʻri deb oʻylangan fikr">taxmin</span>
boʻlib qolgan edi. Uni matematik Tomas Xeyls faqat 1999-yilda toʻliq
<span class="cn-word" data-tr="shubhasiz toʻgʻri ekanini koʻrsatish">isbot</span>ladi.
Asalarilar esa buni undan ancha oldin bilishardi.</p>
""",
    },
]
