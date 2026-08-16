# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-72, PM-73, PM-74 (Blok E ning yakuni).

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 72 — tarix (haqiqiy voqealar qayta hikoya qilingan), 73 — sharh,
      74 — hikoya. Oldingi uchlik hikoya/tarix/ilmiy-ommabop edi.

⚠️ Kumulyativ:
   • 72-matnda faqat oʻxshashlik va soya usuli;
   • 73-matnda simmetriya va burilish; ⛔ hajm yoʻq;
   • 74-matnda hajm, litr va silindr (asosi PM-71 dan).
⚠️ `grammar.pattern` va `examples` ekranlanadi — <sup> emas, Unicode ²
   va ³ yoziladi.
⚠️ Savollar SAQLANGAN TARTIBDA koʻrsatiladi — `answer` indekslari qoʻlda
   oʻzgartirilgan: 72 → 1/2/3, 73 → 2/1/0, 74 → 3/2/0.
⚠️ Faktlar haqiqiy: Fales (Milet, mil. avv. VI asr) piramidani soyasi
   bilan oʻlchagani qadimgi mualliflarning rivoyati sifatida beriladi,
   tayyor son sifatida emas.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_72_74.py --author=prime
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
    # PM-72 — oʻxshashlik, soya usuli                             TARIX
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Soya bilan minorani oʻlchash — Fales usuli",
        "summary": (
            "PM-72 matni. Tarix: qadimgi yunon olimi Fales piramidani "
            "soyasi bilan oʻlchagan degan rivoyat, va Sherbek shu usul "
            "bilan maktab hovlisidagi terakni oʻlchashi."
        ),
        "order":   72,
        "grammar": [
            {
                "pattern":  "boʻy ÷ soya — oʻxshash uchburchaklarda bir xil",
                "meaning":  "Quyosh nurlari parallel tushgani uchun bir "
                            "vaqtda oʻlchangan hamma soya bir xil burchak "
                            "beradi. Demak kichik narsaning nisbatini "
                            "kattasiga koʻchirish mumkin.",
                "examples": [
                    "1 ÷ 0,8 = 1,25 (tayoq va uning soyasi)",
                    "h = 14 × 1,25 = 17,5 m (terak)",
                    "tekshiruv: 17,5 ÷ 14 = 1,25",
                ],
            },
        ],
        "questions": [
            {
                "text": "Rivoyatga koʻra, Fales piramidani qanday oʻlchagan?",
                "choices": [
                    "Piramidaning tepasiga chiqib, arqon tushirgan",
                    "Tayoqning soyasi oʻz boʻyiga teng boʻlgan payt "
                    "piramidaning soyasini oʻlchagan",
                    "Piramidaning bir qirrasini sanab chiqqan",
                    "Uni suvda aks etgan koʻrinishi bilan solishtirgan",
                ],
                "answer": 1,
                "explanation": "Kunning shunday bir payti boʻladiki, har "
                               "qanday narsaning soyasi oʻz boʻyiga aynan "
                               "teng chiqadi. Oʻsha paytda piramidaning "
                               "soyasini oʻlchash kifoya — u ham "
                               "piramidaning balandligiga teng boʻladi.",
            },
            {
                "text": "Sherbekning hisobi boʻyicha terak necha metr?",
                "choices": ["11,2 m", "14 m", "17,5 m", "175 m"],
                "answer": 2,
                "explanation": "Tayoqning nisbati: 1 ÷ 0,8 = 1,25. Terak "
                               "uchun ham shu nisbat: 14 × 1,25 = 17,5 m. "
                               "«11,2 m» — nisbat teskari olingan "
                               "(14 × 0,8), u holda terak oʻz soyasidan "
                               "past chiqib qolardi.",
            },
            {
                "text": "Kechroq tayoqning soyasi 2 metr boʻldi. Shu payt "
                        "terakning soyasi qancha boʻladi?",
                "choices": ["8,75 m", "17,5 m", "28 m", "35 m"],
                "answer": 3,
                "explanation": "Endi soya boʻydan ikki barobar uzun: "
                               "1 metrlik tayoqning soyasi 2 metr. Demak "
                               "17,5 metrlik terakning soyasi ham ikki "
                               "barobar: 17,5 × 2 = 35 m. «28 m» — eski "
                               "soyani (14 m) ikkilantirish; lekin quyosh "
                               "pasaygani uchun nisbat oʻzgargan.",
            },
        ],
        "body": """
<p>Bugun Sherbek darslikda gʻalati bir hikoyani oʻqidi.</p>

<p>Bundan ikki yarim ming yil oldin Milet shahrida
<span class="cn-word" data-tr="qadimgi yunon olimi va faylasufi">Fales</span>
degan olim yashagan. U Misrga borganda undan piramidaning balandligini
soʻrashgan. Oʻsha paytda hech kim buni bilmagan:
<span class="cn-word" data-tr="asosi koʻpburchak, yon tomonlari uchburchak boʻlgan jism">piramida</span>ning
tepasiga chiqib boʻlmaydi, ichidan oʻlchash ham mumkin emas.</p>

<p>Qadimgi mualliflar rivoyat qilishicha, Fales yerga oddiy bir
<span class="cn-word" data-tr="tik qoʻyilgan uzun yogʻoch">tayoq</span>
qoqib qoʻygan va kutgan. Kunning shunday bir payti boʻladiki, tayoqning
<span class="cn-word" data-tr="yorugʻlik toʻsilganda hosil boʻlgan qorongʻi iz">soya</span>si
oʻz boʻyiga aynan teng chiqadi. Oʻsha paytda u piramidaning soyasini
oʻlchagan — chunki u ham piramidaning
<span class="cn-word" data-tr="pastdan tepagacha boʻlgan masofa">balandlik</span>iga
teng boʻlishi kerak edi.</p>

<p>Sherbek kitobni yopdi va hovliga chiqdi. Maktab hovlisida baland
<span class="cn-word" data-tr="tez oʻsadigan baland daraxt">terak</span>
bor edi.</p>

<p>U bir metrli chizgʻichni tik qoʻydi. Soyasi <strong>80</strong>
santimetr, yaʼni <strong>0,8</strong> metr chiqdi. Soya boʻydan qisqa —
demak kun hali Fales kutgan paytga yetmagan. Lekin Sherbek buni
kutmasa ham boʻlishini tushundi.</p>

<p>Quyosh juda uzoqda, uning
<span class="cn-word" data-tr="quyoshdan keladigan toʻgʻri chiziqli yorugʻlik">nur</span>lari
yerga
<span class="cn-word" data-tr="hech qachon kesishmaydigan chiziqlar">parallel</span>
tushadi. Demak chizgʻich va uning soyasi hosil qilgan
<span class="cn-word" data-tr="uch tomonli shakl">uchburchak</span>
terak va uning soyasi hosil qilgan uchburchakka
<span class="cn-word" data-tr="shakli bir xil, oʻlchami har xil">oʻxshash</span>.
Ikkalasida ham toʻgʻri burchak bor, ikkalasida ham quyosh nurining
burchagi bir xil.</p>

<p>Terakning soyasini oʻlchadi: <strong>14</strong> metr.</p>

<p>Endi
<span class="cn-word" data-tr="ikki sonning bir-biriga boʻlinmasi">nisbat</span>
ish boshladi. Chizgʻichda boʻy soyaning 1 ÷ 0,8 = <strong>1,25</strong>
barobari edi. Terakda ham xuddi shunday boʻlishi kerak:
14 × 1,25 = <strong>17,5</strong> metr.</p>

<p>Sherbek terakka qaradi. Beshqavatli uydek. Toʻgʻri chiqqanga
oʻxshaydi.</p>

<p>Bir metrli chizgʻich bilan yigirma metrlik daraxtni oʻlchash mumkin
ekan. Faqat quyosh kerak — va bitta nisbat.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-73 — simmetriya                                          SHARH
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Samarqand gumbazidagi naqsh",
        "summary": (
            "PM-73 matni. Sharh: Registondagi naqshlarga matematik koʻz "
            "bilan qarash — burilish simmetriyasi, takrorlanuvchi boʻlak "
            "va naqqoshning ishini toʻrt barobar yengillashtirgan qoida."
        ),
        "order":   73,
        "grammar": [
            {
                "pattern":  "burilish burchagi = 360° ÷ tartib",
                "meaning":  "Naqsh 360 gradus davomida necha marta oʻzidek "
                            "koʻrinsa, oʻsha son — tartib. Tartib bilinsa, "
                            "burilish burchagi darrov topiladi.",
                "examples": [
                    "sakkiz qirrali yulduz: 360 ÷ 8 = 45°",
                    "kvadrat plitka: 360 ÷ 4 = 90°",
                    "hoshiya: 300 ÷ 25 = 12 marta takrorlanadi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Naqqosh nega butun naqshni boshidan oxirigacha "
                        "chizmaydi?",
                "choices": [
                    "Chunki gumbaz juda baland va yetib boʻlmaydi",
                    "Chunki bir xil boʻyoq yetishmaydi",
                    "Chunki simmetriya tufayli bitta boʻlakni chizib, "
                    "qolganini burib yoki koʻchirib chiqish kifoya",
                    "Chunki naqsh har joyda boshqacha boʻladi",
                ],
                "answer": 2,
                "explanation": "Simmetriya — naqqosh uchun amaliy qurol. "
                               "Sakkizta bir xil boʻlakdan iborat yulduzda "
                               "faqat bitta boʻlakni chizib, qolgan "
                               "yettitasini burib chiqish yetarli. Ish "
                               "sakkiz barobar kamayadi.",
            },
            {
                "text": "Sakkiz qirrali yulduz necha gradusga burilganda "
                        "oʻzgarmaydi?",
                "choices": ["30°", "45°", "60°", "90°"],
                "answer": 1,
                "explanation": "Burilish burchagi = 360° ÷ tartib = "
                               "360 ÷ 8 = 45°. «90°» — tartibi 4 boʻlgan "
                               "naqshniki, masalan oddiy kvadrat "
                               "plitkaniki.",
            },
            {
                "text": "Boʻlagi 25 santimetr boʻlgan naqsh 3 metrlik "
                        "hoshiyada necha marta takrorlanadi?",
                "choices": ["12 marta", "25 marta", "75 marta", "120 marta"],
                "answer": 0,
                "explanation": "Avval birliklarni tenglashtiramiz: 3 m = "
                               "300 sm. Keyin 300 ÷ 25 = 12 marta. "
                               "«120 marta» — 3 metr 3000 santimetr deb "
                               "olingan; 1 metrda 100 santimetr bor, 1000 "
                               "emas.",
            },
        ],
        "body": """
<p>Registon maydonidagi
<span class="cn-word" data-tr="binoning yarim shar shaklidagi tomi">gumbaz</span>ga
odamlar odatda shunchaki qarab turishadi. Chiroyli, deyishadi. Lekin
unga boshqacha koʻz bilan ham qarash mumkin.</p>

<p>Gumbazning ustidagi
<span class="cn-word" data-tr="takrorlanuvchi bezak">naqsh</span>ga
diqqat bilan qarang. Uning oʻrtasida sakkiz nurli
<span class="cn-word" data-tr="uchli, nurli shakl">yulduz</span>
turadi. Sakkizta nur bir xil, sakkizta oraliq ham bir xil.</p>

<p>Endi shu yulduzni xayolan burib koʻring. Qancha bursangiz, u yana
oʻzidek boʻlib qoladi? Toʻliq bir aylanish 360
<span class="cn-word" data-tr="burchak oʻlchov birligi">gradus</span>,
va yulduz shu davomida sakkiz marta oʻzini takrorlaydi. Demak burchak
360 ÷ 8 = <strong>45</strong> gradus. Bu — naqshning
<span class="cn-word" data-tr="burilganda oʻzgarmaslik xossasi">burilish simmetriyasi</span>.</p>

<p>Shu yerda eng qizigʻi boshlanadi.</p>

<p>Bu naqshni chizgan
<span class="cn-word" data-tr="naqsh soluvchi usta">naqqosh</span>
uni sakkiz marta chizmagan. U faqat <b>bitta</b> boʻlakni chizgan,
qolgan yettitasi esa oʻsha boʻlakning
<span class="cn-word" data-tr="markaz atrofida burish">burilish</span>i.
Ish sakkiz barobar kamaygan — va aynan shuning uchun naqshning hamma
qismi bir-biriga shunchalik aniq oʻxshaydi. Qoʻl bilan sakkiz marta
chizilganida ular biroz farq qilardi.</p>

<p>Devor boʻylab ketgan
<span class="cn-word" data-tr="devor yoki gilamning chekkasidagi bezakli tasma">hoshiya</span>da
esa boshqa qoida ishlaydi. U yerda naqsh burilmaydi —
<span class="cn-word" data-tr="shaklni siljitish">koʻchiriladi</span>.
Bitta boʻlak olinadi va yonma-yon takrorlanadi. Agar boʻlak 25
santimetr boʻlsa, uch metrlik hoshiyaga u 300 ÷ 25 =
<strong>12</strong> marta tushadi.</p>

<p>Va nihoyat, ayvon peshtoqidagi katta naqsh oʻrtasidan tik chiziq
oʻtkazsangiz, chap tomon oʻng tomonning
<span class="cn-word" data-tr="koʻzgudagidek teskari nusxa">aksi</span>
ekanini koʻrasiz. Bu — <b>simmetriya oʻqi</b>.</p>

<p>Uchta oddiy harakat: burish, koʻchirish, aks ettirish. Olti yuz yil
oldin ishlagan ustalar bu soʻzlarni bizdek aytmagan boʻlishi mumkin.
Lekin ular bu qoidalarni bizdan yaxshiroq bilgan.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-74 — hajm, litr, silindr                                HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Suv baki necha chelak",
        "summary": (
            "PM-74 matni. Hikoya: Jasurning oilasi tomga suv baki oladi. "
            "Ikki bak koʻzga bir xil koʻrinadi, lekin hisob ularning "
            "farqini koʻrsatadi."
        ),
        "order":   74,
        "grammar": [
            {
                "pattern":  "V = π × r² × h  va  1 m³ = 1000 litr",
                "meaning":  "Silindrning hajmi — asosining yuzasi "
                            "balandlikka koʻpaytirilgani. Kub metrni litrga "
                            "oʻgirish uchun 1000 ga koʻpaytiriladi.",
                "examples": [
                    "3,14 × 0,25 × 1 = 0,785 m³ = 785 litr (dumaloq bak)",
                    "1 × 0,8 × 1 = 0,8 m³ = 800 litr (toʻrtburchak bak)",
                    "785 ÷ 10 = 78,5 — oʻnta litrlik chelak bilan",
                ],
            },
        ],
        "questions": [
            {
                "text": "Jasurning otasi nega ikkala bakni ham hisoblab "
                        "koʻrdi?",
                "choices": [
                    "Chunki sotuvchi narxni aytmagan edi",
                    "Chunki bakning rangini tanlash kerak edi",
                    "Chunki tomga ogʻir bak koʻtarib boʻlmaydi",
                    "Chunki ikkalasi koʻzga bir xil koʻringan, lekin "
                    "sigʻimi har xil boʻlishi mumkin edi",
                ],
                "answer": 3,
                "explanation": "Koʻz bilan solishtirish aldashi mumkin: "
                               "biri dumaloq, biri toʻrtburchak, "
                               "balandliklari esa deyarli bir xil. Faqat "
                               "hisob qaysi biriga koʻproq suv sigʻishini "
                               "aniq koʻrsatadi.",
            },
            {
                "text": "Dumaloq bakka necha litr suv sigʻadi?",
                "choices": ["78,5 litr", "157 litr", "785 litr", "7850 litr"],
                "answer": 2,
                "explanation": "Asos yuzasi: 3,14 × 0,5² = 3,14 × 0,25 = "
                               "0,785 m². Hajm: 0,785 × 1 = 0,785 m³. "
                               "Litrga: 0,785 × 1000 = 785 litr. "
                               "«78,5 litr» — 1000 emas, 100 ga "
                               "koʻpaytirilganda chiqadi.",
            },
            {
                "text": "Ikki bakning sigʻimi orasidagi farq necha litr?",
                "choices": ["15 litr", "85 litr", "150 litr", "215 litr"],
                "answer": 0,
                "explanation": "Toʻrtburchak bak: 1 × 0,8 × 1 = 0,8 m³ = "
                               "800 litr. Dumaloq bak 785 litr. Farqi: "
                               "800 − 785 = 15 litr — bir chelakdan "
                               "koʻproq, lekin koʻz bilan sezib "
                               "boʻlmaydigan darajada oz.",
            },
        ],
        "body": """
<p>Jasurlarning tomidagi eski suv baki teshildi. Shanba kuni otasi uni
bozorga olib bordi.</p>

<p>Doʻkonda ikkita bak turardi. Biri dumaloq —
<span class="cn-word" data-tr="asosi doira boʻlgan fazoviy jism">silindr</span>
shaklida, ikkinchisi toʻrtburchak
<span class="cn-word" data-tr="oddiy quti shaklidagi jism">quti</span>
shaklida. Ikkalasi ham bir boʻydek koʻrinardi.</p>

<p>«Qaysi biriga koʻproq suv sigʻadi?» — soʻradi otasi.</p>

<p>Jasur yelka qisdi. Koʻzga ikkalasi bir xil edi.</p>

<p>«Unda oʻlchaymiz», — dedi otasi va ruletkani chiqardi.</p>

<p>Dumaloq bakning
<span class="cn-word" data-tr="markazdan oʻtgan eng uzun kesma">diametr</span>i
<strong>1</strong> metr, balandligi ham <strong>1</strong> metr chiqdi.
Demak
<span class="cn-word" data-tr="markazdan aylanagacha masofa">radius</span>i
0,5 metr.</p>

<p>Silindrning
<span class="cn-word" data-tr="jism ichiga sigʻadigan joy">hajm</span>i
<span class="cn-word" data-tr="jismning pastki yoki yuqorigi yassi yuzasi">asos</span>ining
yuzasini balandlikka koʻpaytirish bilan topiladi. Asos —
<span class="cn-word" data-tr="aylana va uning ichi">doira</span>:
3,14 × 0,5 × 0,5 = <strong>0,785</strong> kvadrat metr. Hajmi esa
0,785 × 1 = <strong>0,785</strong>
<span class="cn-word" data-tr="tomoni 1 metr boʻlgan kubning hajmi">kub metr</span>.</p>

<p>«Bu qancha suv boʻladi?» — soʻradi Jasur.</p>

<p>Bir kub metr — ming
<span class="cn-word" data-tr="1000 kub santimetrga teng hajm birligi">litr</span>.
Demak 0,785 × 1000 = <strong>785</strong> litr.</p>

<p>Toʻrtburchak bakni ham oʻlchashdi: 1 metr, 0,8 metr va 1 metr.
Bu yerda hisob osonroq: 1 × 0,8 × 1 = <strong>0,8</strong> kub metr,
yaʼni <strong>800</strong> litr.</p>

<p>Farqi atigi <strong>15</strong> litr ekan — ikki bakning
<span class="cn-word" data-tr="idishga sigʻadigan suyuqlik miqdori">sigʻim</span>i
deyarli bir xil. Koʻzga ular haqiqatan ham
deyarli teng koʻringan.</p>

<p>Uyga qaytishda Jasur boshqa narsani hisoblab bordi. Oila kuniga
taxminan 150 litr suv sarflaydi. Demak toʻla bak besh kundan sal
koʻproqqa yetadi. Va agar suv oʻchsa, uni oʻn litrlik
<span class="cn-word" data-tr="suv tashiydigan idish">chelak</span>
bilan toʻldirish kerak boʻlsa — 785 ÷ 10, yaʼni yetmish sakkiztadan
koʻproq chelak koʻtarish kerak boʻlar ekan.</p>

<p>«Endi tushundingmi, nega hisoblab koʻrdik?» — dedi otasi.</p>
""",
    },
]
