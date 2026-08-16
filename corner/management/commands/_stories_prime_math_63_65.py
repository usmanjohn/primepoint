# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-63, PM-64, PM-65 (Blok E: Geometriya).

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 63 — hikoya, 64 — tarix (haqiqiy material qayta hikoya qilingan),
      65 — hikoya. (62 jumboq edi, shuning uchun uchtasi bir shaklda emas.)

⚠️ 64-matndagi tarixiy faktlar:
  • Nil har yili toshib, dala chegaralarini yuvib ketardi va yerni qaytadan
    oʻlchash kerak boʻlardi — bu hujjatlashtirilgan;
  • yunonlar misrlik oʻlchovchilarni «arqon tortuvchilar» (harpedonapt)
    deb atagan — bu ham manbalarda bor;
  • 12 boʻlakli arqon bilan aynan 3-4-5 uchburchak yasalgani haqida
    Misr hujjati YOʻQ — matnda shu ochiq aytilgan, «rivoyat» deb;
  • bobilliklar Pifagor uchliklarini undan ming yil oldin bilgan
    (Plimpton 322 lavhasi) — bu ham toʻgʻri.
  ⚠️ Arqon HALQA qilib bogʻlanadi: yopiq halqada 12 ta tugun 12 ta teng
     boʻlak beradi (ochiq arqonda 13 ta tugun kerak boʻlardi). Matnda shu
     aniq yozilgan — off-by-one bu yerda haqiqiy xato boʻlardi.

⚠️ Kumulyativ: toʻrtburchaklar oilasi (PM-66), perimetr (PM-67), yuza
   (PM-68/69) va π (PM-70) YOʻQ.
⚠️ `grammar.pattern` va `examples` ekranlanadi — <sup> emas, Unicode ²
   yoziladi.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_63_65.py --author=prime
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
    # PM-63 — teng yonli uchburchak                              HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Uyning tomi",
        "summary": (
            "PM-63 matni. Hikoya: Karim aka tom yasayapti va yon "
            "yogʻochlarni bir xil uzunlikda kesadi. Bekzod esa uchidagi "
            "burchakni oʻlchamasdan hisoblab beradi."
        ),
        "order":   63,
        "grammar": [
            {
                "pattern":  "teng yonli uchburchak: asosdagi burchaklar teng",
                "meaning":  "Ikki yon tomon teng boʻlsa, asosdagi ikki "
                            "burchak ham teng boʻladi. Shuning uchun bitta "
                            "burchak bilinsa, qolgan ikkitasi hisoblab "
                            "topiladi.",
                "examples": [
                    "yogʻochlar gorizontal bilan 40°: 180 − 40 − 40 = 100°",
                    "tikroq tom, 55°: 55 + 55 = 110, 180 − 110 = 70°",
                    "peshtoqdagi teng tomonli uchburchak: 180 ÷ 3 = 60°",
                ],
            },
        ],
        "questions": [
            {
                "text": "Karim aka nega ikki yogʻochni bir xil uzunlikda "
                        "kesdi?",
                "choices": [
                    "Yogʻoch shunday sotilgani uchun",
                    "Tom simmetrik chiqishi va ikki tomonga bir xil "
                    "qiyalik berishi uchun",
                    "Bir xil uzunlikdagi yogʻoch arzonroq boʻlgani uchun",
                    "Mixlar yetmay qolgani uchun",
                ],
                "answer": 1,
                "explanation": "Karim aka Bekzodga tushuntirdi: yon "
                               "tomonlar teng boʻlsa, uchburchak teng "
                               "yonli boʻladi va asosdagi ikki burchak "
                               "tenglashadi — tom ikki tomonga bir xil "
                               "qiyalik bilan tushadi.",
            },
            {
                "text": "Yogʻochlar gorizontal bilan 40° burchak hosil "
                        "qilgan boʻlsa, tomning uchidagi burchak necha "
                        "gradus?",
                "choices": ["40°", "80°", "100°", "140°"],
                "answer": 2,
                "explanation": "Asosdagi ikki burchak ham 40° dan: "
                               "40 + 40 = 80. Uchidagi burchakka qolgani "
                               "esa 180 − 80 = 100°. «140°» — faqat bitta "
                               "40° ayrilganda chiqadigan xato.",
            },
            {
                "text": "Qoʻshni tikroq tom soʻradi — yogʻochlar 55° "
                        "ostida. Uchidagi burchak qanday oʻzgaradi?",
                "choices": [
                    "70° boʻladi — tom tikroq va uchi oʻtkirroq",
                    "110° boʻladi — oʻzgarishsiz qoladi",
                    "125° boʻladi — tom yassiroq boʻladi",
                    "Uchidagi burchak hech qachon oʻzgarmaydi",
                ],
                "answer": 0,
                "explanation": "55 + 55 = 110, keyin 180 − 110 = 70°. "
                               "Asosdagi burchaklar kattalashgani sari "
                               "uchidagi burchak kichrayadi — tom tikroq "
                               "koʻtariladi. Qor koʻp yogʻadigan joyda "
                               "aynan shunday qilinadi.",
            },
        ],
        "body": """
<p>Karim aka hovlida yogʻoch tayyorlayapti. Bekzod unga yordamlashgani
kelgan.</p>

<p>Usta ikkita uzun yogʻochni yonma-yon qoʻydi va bir xil uzunlikda kesdi.</p>

<p>«Nega ikkalasi ham teng boʻlishi kerak?» — soʻradi Bekzod.</p>

<p>«Chunki tom qiyshiq boʻlmasligi kerak», — dedi Karim aka. «Ikki
<span class="cn-word" data-tr="teng yonli uchburchakda teng boʻlgan tomonlardan biri">yon tomon</span>
teng boʻlsa, uchburchak
<span class="cn-word" data-tr="ikki tomoni teng boʻlgan uchburchak">teng yonli</span>
boʻladi. Unda ikki tomonga bir xil qiyalik tushadi.»</p>

<p>Yogʻochlarni koʻtarib, uchida tutashtirdi. Pastda ular gorizontal
<span class="cn-word" data-tr="teng yonli uchburchakning uchinchi, teng boʻlmagan tomoni">asos</span>ga
tayanardi. Usta
<span class="cn-word" data-tr="burchak oʻlchaydigan yarim doira shaklidagi asbob">transportir</span>
bilan oʻlchadi: har bir yogʻoch gorizontal bilan <strong>40</strong>° hosil
qilgan.</p>

<p>«Endi
<span class="cn-word" data-tr="ikki yon tomon orasidagi burchak">uchidagi burchak</span>ni
oʻlchayman», — dedi u va narvonga qoʻl uzatdi.</p>

<p>«Shart emas», — dedi Bekzod. «Oʻlchamasdan ham aytaman.»</p>

<p>U yerga chizib koʻrsatdi. Yon tomonlar teng, demak
<span class="cn-word" data-tr="asosga tegib turgan ikki burchak">asosdagi burchaklar</span>
ham teng: ikkalasi ham 40°. Uchala
<span class="cn-word" data-tr="umumiy boshlangʻich nuqtali ikki nur hosil qilgan shakl">burchak</span>ning
<span class="cn-word" data-tr="qoʻshish natijasi">yigʻindisi</span> esa
har doim 180°.</p>

<p>40 + 40 = 80, keyin 180 − 80 = <strong>100</strong>°.</p>

<p>Karim aka narvondan tushdi, transportirni qoʻydi va kuldi: «Roppa-rosa
yuz. Demak endi men sendan soʻrayman.»</p>

<p>Qoʻshni Nodira opa tikroq tom soʻragan edi — yogʻochlar
<strong>55</strong>° ostida. Bekzod darrov hisobladi: 55 + 55 = 110,
180 − 110 = <strong>70</strong>°.</p>

<p>«Uchidagi burchak kichraydi, tom esa
<span class="cn-word" data-tr="yerga nisbatan qiya turgan holat">qiyalik</span>ni
oshiradi», — dedi u. «Qor koʻp joyda shunday qilishadi: qor tikroq tomda
turmaydi.»</p>

<p>Peshtoqning tepasiga usta kichkina naqshli uchburchak oʻrnatdi. Uning
uchala tomoni ham teng edi —
<span class="cn-word" data-tr="uchala tomoni teng boʻlgan uchburchak">teng tomonli</span>
uchburchak. Bunday shaklda hisob ham qisqa: 180 ÷ 3 = <strong>60</strong>°,
uchala burchak ham.</p>

<p>«Sen bugun bitta ham yogʻoch koʻtarmading», — dedi Karim aka ketayotib,
«lekin
<span class="cn-word" data-tr="oʻlchov asbobisiz, hisob yoʻli bilan">hisob bilan</span>
menga bir soat vaqt tejab berding.»</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-64 — Pifagor teoremasi                                   TARIX
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Oʻn ikki tugunli arqon",
        "summary": (
            "PM-64 matni. Tarix (haqiqiy materialning qayta hikoyasi): "
            "qadimgi Misrda Nil toshgandan keyin dalalar qayta "
            "oʻlchanardi. «Arqon tortuvchilar» va 3-4-5 uchligi haqidagi "
            "mashhur rivoyat — va unda qaysi qismi hujjatlashtirilgani."
        ),
        "order":   64,
        "grammar": [
            {
                "pattern":  "a² + b² = c² — toʻgʻri burchakning belgisi",
                "meaning":  "Tomonlari uchun bu tenglik bajarilsa, "
                            "uchburchak toʻgʻri burchakli boʻladi. Shuning "
                            "uchun burchakni oʻlchamasdan, faqat uzunlik "
                            "bilan tekshirsa boʻladi.",
                "examples": [
                    "3² + 4² = 9 + 16 = 25 = 5²",
                    "arqon halqasi: 3 + 4 + 5 = 12 ta boʻlak",
                    "ikki barobari: 6² + 8² = 36 + 64 = 100 = 10²",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega qadimgi misrliklarga dalalarni har yili "
                        "qaytadan oʻlchashga toʻgʻri kelardi?",
                "choices": [
                    "Yer egalari har yili almashib turardi",
                    "Nil toshib, dala chegaralarini yuvib ketardi",
                    "Ular oʻlchov birligini tez-tez oʻzgartirardi",
                    "Firʼavn har yili yangi soliq joriy qilardi",
                ],
                "answer": 1,
                "explanation": "Nil har yili toshar va qaytganda chegara "
                               "belgilarini yuvib ketardi. Yer qayta "
                               "oʻlchanmasa, soliq ham, chegara ham "
                               "adashardi — shuning uchun oʻlchovchilar "
                               "davlatning eng kerakli odamlari edi.",
            },
            {
                "text": "Arqon halqasida 12 ta teng boʻlak bor. Uchburchak "
                        "yasash uchun tugunlar qanday taqsimlanadi?",
                "choices": ["2, 4 va 6", "3, 4 va 5", "4, 4 va 4", "1, 5 va 6"],
                "answer": 1,
                "explanation": "3 + 4 + 5 = 12 — halqadagi hamma boʻlak "
                               "ishlatiladi. «4, 4 va 4» ham 12 beradi, "
                               "lekin u teng tomonli uchburchak: undagi "
                               "burchaklar 60° dan, toʻgʻri burchak "
                               "chiqmaydi.",
            },
            {
                "text": "Nega aynan 3-4-5 uchburchakda burchak toʻgʻri "
                        "boʻladi?",
                "choices": [
                    "Chunki 3 + 4 = 7 va 7 soni maxsus hisoblanadi",
                    "Chunki 3, 4 va 5 ketma-ket sonlar",
                    "Chunki 9 + 16 = 25, yaʼni 3² + 4² = 5²",
                    "Chunki 5 soni 3 va 4 dan katta",
                ],
                "answer": 2,
                "explanation": "Tekshiruv shu: 3² + 4² = 9 + 16 = 25 va "
                               "5² = 25. Tenglik bajarilgani uchun eng "
                               "uzun tomon qarshisidagi burchak aynan 90° "
                               "boʻladi. Ketma-ket son boʻlishi esa "
                               "tasodif: 4-5-6 da 16 + 25 = 41, 36 esa "
                               "emas.",
            },
        ],
        "body": """
<p>Har yili yozda Nil daryosi toshardi. Suv qaytganda dalalar unumdor loy
bilan qoplanar, lekin chegara belgilari yoʻqolib ketardi. Kimning yeri
qayerda tugashini hech kim bilmasdi.</p>

<p>Shuning uchun Misrda alohida kasb bor edi. Yunonlar bu odamlarni
<span class="cn-word" data-tr="arqon bilan yer oʻlchagan qadimgi Misr mutaxassislari">arqon tortuvchilar</span>
deb atashgan. Ularning butun asbobi — bitta uzun arqon.</p>

<p>Arqonda teng masofada
<span class="cn-word" data-tr="arqondagi tugilgan belgi; oʻlchov nuqtasi">tugun</span>lar
bogʻlangan boʻlardi, ikki uchi esa bir-biriga ulanib
<span class="cn-word" data-tr="ikki uchi tutashtirilgan yopiq shakl">halqa</span>
hosil qilardi. Yopiq halqada oʻn ikkita tugun oʻn ikkita
<span class="cn-word" data-tr="teng qismlarga boʻlingan bir boʻlagi">teng boʻlak</span>
beradi.</p>

<p>Uch kishi halqani ushlaydi. Birinchisi <strong>3</strong> boʻlakni,
ikkinchisi <strong>4</strong> boʻlakni, uchinchisi <strong>5</strong>
boʻlakni oladi va arqonni tarang tortadi. 3 + 4 + 5 = 12 — hamma boʻlak
ishlatildi.</p>

<p>Natijada hosil boʻlgan uchburchakning eng katta burchagi aynan 90° —
<span class="cn-word" data-tr="90 gradusli burchak">toʻgʻri burchak</span>
boʻladi. Dala chegarasini shu burchakdan boshlash mumkin.</p>

<p>Nega ishonch bilan aytamiz? Sonlar tekshiradi:
3<sup>2</sup> + 4<sup>2</sup> = 9 + 16 = <strong>25</strong>, va
5<sup>2</sup> ham <strong>25</strong>. Ikkala
<span class="cn-word" data-tr="toʻgʻri burchakni hosil qiluvchi ikki tomondan biri">katet</span>ning
<span class="cn-word" data-tr="sonning oʻziga koʻpaytmasi">kvadrat</span>lari
yigʻindisi
<span class="cn-word" data-tr="toʻgʻri burchak qarshisidagi eng uzun tomon">gipotenuza</span>ning
kvadratiga teng.</p>

<p>Bu yerda bitta halollik kerak. Misrliklar aynan shu arqonni ishlatgani
haqida yozma <span class="cn-word" data-tr="fikrni tasdiqlovchi hujjat yoki topilma">dalil</span>
topilmagan — bu koʻproq
<span class="cn-word" data-tr="ogʻizdan ogʻizga oʻtgan hikoya">rivoyat</span>.
Aniq bilinadigani boshqacha: bobilliklar Pifagor
<span class="cn-word" data-tr="uchala tomoni butun son boʻlgan holat, masalan 3-4-5">uchlik</span>larini
undan ham ming yil oldin bilishgan — sopol lavhalarda ularning roʻyxati
saqlangan.</p>

<p>Pifagorning oʻzi bu tenglikni kashf qilmagan. U undan ancha muhimroq
narsani qoldirgan:
<span class="cn-word" data-tr="qoida nega toʻgʻri ekanini koʻrsatuvchi mulohaza">isbot</span>ni —
yaʼni tenglik <b>hamma</b> toʻgʻri burchakli uchburchakda ishlashining
sababini.</p>

<p>Arqon esa hamon ishlaydi. Bugungi quruvchi ham devor burchagini xuddi
shunday tekshiradi: 3 metr, 4 metr, 5 metr.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-65 — Pifagorning qoʻllanishi                            HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Narvon devorga suyalganda",
        "summary": (
            "PM-65 matni. Hikoya: Sherbek qoʻshnisiga lampochka "
            "almashtirishga yordam beradi. Narvonning oyogʻini qayerga "
            "qoʻyish kerakligi — hisob bilan hal qilinadi."
        ),
        "order":   65,
        "grammar": [
            {
                "pattern":  "narvon — gipotenuza; devor va yer — katetlar",
                "meaning":  "Devor yerga perpendikulyar boʻlgani uchun "
                            "narvon, devor va yer toʻgʻri burchakli "
                            "uchburchak hosil qiladi. Narvon qiya turadi, "
                            "demak u har doim gipotenuza.",
                "examples": [
                    "narvon 5, oyogʻi 3: 25 − 9 = 16, √16 = 4 m",
                    "oyogʻi 4 ga surilsa: 25 − 16 = 9, √9 = 3 m",
                    "elektrchining narvoni 13, oyogʻi 5: 169 − 25 = 144, √144 = 12 m",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sherbek nega narvonning oyogʻini devorga yaqinroq "
                        "surdi?",
                "choices": [
                    "Narvon uzunroq boʻlib qolishi uchun",
                    "Yer notekis boʻlgani uchun",
                    "Oyoq uzoqda boʻlsa, narvonning uchi pastroqqa yetadi "
                    "va lampaga qoʻl yetmaydi",
                    "Nodira opa shunday aytgani uchun",
                ],
                "answer": 2,
                "explanation": "Narvonning uzunligi oʻzgarmaydi. Oyoq "
                               "uzoqroqqa surilsa, narvon qiyaroq boʻladi "
                               "va uchi pastroqqa tushadi: oyoq 4 m da "
                               "balandlik bor-yoʻgʻi 3 m qoladi — bu esa "
                               "4 metrdagi lampaga yetmaydi.",
            },
            {
                "text": "Narvon 5 m, oyogʻi devordan 4 m narida boʻlsa, "
                        "uchi qanday balandlikka yetadi?",
                "choices": ["1 m", "3 m", "4,5 m", "6,4 m"],
                "answer": 1,
                "explanation": "Narvon — gipotenuza, shuning uchun "
                               "ayiramiz: 5² − 4² = 25 − 16 = 9, √9 = 3 m. "
                               "«1 m» — 5 − 4, kvadratlarsiz ayirish. "
                               "«6,4 m» esa narvonning oʻzidan uzun — "
                               "bunday boʻlishi mumkin emas.",
            },
            {
                "text": "Elektrchining narvoni 13 m, oyogʻi ustundan 5 m "
                        "narida. Uchi qanday balandlikka yetadi?",
                "choices": ["8 m", "12 m", "14 m", "18 m"],
                "answer": 1,
                "explanation": "13² − 5² = 169 − 25 = 144, √144 = 12 m. "
                               "Bu 5-12-13 uchligi. «8 m» — 13 − 5, "
                               "kvadratlarsiz ayirish; «14 m» esa "
                               "narvondan uzun.",
            },
        ],
        "body": """
<p>Nodira opaning yoʻlakdagi lampochkasi kuyib qoldi. Lampa
<strong>4</strong> metr balandlikda — stulga chiqib boʻlmaydi.</p>

<p>Sherbek qoʻshnining <strong>5</strong> metrli narvonini olib keldi va
devorga suyadi. Narvon oyogʻini devordan ancha uzoqqa — <strong>4</strong>
metr narida qoʻydi.</p>

<p>«Shu yerdan tursam boʻladimi?» — soʻradi u.</p>

<p>Nodira opa boshini chayqadi: «Avval hisobla.»</p>

<p>Sherbek daftar oldi. Devor yerga
<span class="cn-word" data-tr="90° ostida kesishuvchi">perpendikulyar</span>
turibdi, demak devor bilan yer
<span class="cn-word" data-tr="90 gradusli burchak">toʻgʻri burchak</span>
hosil qiladi. Uchalasi birgalikda
<span class="cn-word" data-tr="bitta burchagi 90° boʻlgan uchburchak">toʻgʻri burchakli uchburchak</span>
yasaydi. Narvon esa qiya —
u <span class="cn-word" data-tr="toʻgʻri burchak qarshisidagi eng uzun tomon">gipotenuza</span>.
Devorning <span class="cn-word" data-tr="pastdan yuqorigacha boʻlgan oʻlchov">balandlik</span>i
va yerdagi <span class="cn-word" data-tr="ikki nuqta orasidagi uzunlik">masofa</span> esa
<span class="cn-word" data-tr="toʻgʻri burchakni hosil qiluvchi tomonlar">katet</span>lar.</p>

<p>Narvon gipotenuza boʻlgani uchun
<span class="cn-word" data-tr="sonning oʻziga koʻpaytmasi">kvadrat</span>larni
<span class="cn-word" data-tr="kamaytirish amali">ayirish</span> kerak edi:
25 − 16 = 9. Soʻng
<span class="cn-word" data-tr="kvadratning teskari amali; √ belgisi">kvadrat ildiz</span>
chiqarildi: √9 = <strong>3</strong> metr.</p>

<p>«Uch metr», — dedi u ovoz chiqarib. «Lampa esa toʻrt metrda. Yetmaydi.»</p>

<p>U narvon oyogʻini devorga yaqinroq, <strong>3</strong> metr masofaga
surdi va qaytadan hisobladi: 25 − 9 = 16, √16 = <strong>4</strong> metr.
Endi aynan yetadi.</p>

<p>Chiqib, lampochkani almashtirdi.</p>

<p>Kechqurun Nodira opaning akasi — elektrchi — keldi. Uning narvoni ancha
uzun, <strong>13</strong> metr.</p>

<p>«Koʻcha ustuniga chiqqanimda oyogʻini besh metr narida qoʻyaman», —
dedi u. Sherbek hisobladi: 169 − 25 = 144, √144 = <strong>12</strong> metr.</p>

<p>«Bu <span class="cn-word" data-tr="uchala tomoni butun son boʻlgan holat: 5, 12, 13">Pifagor uchligi</span>»,
— dedi Sherbek. Elektrchi kuldi: «Men buni maktabda oʻrganganman, keyin esa
har kuni ishlataman. Narvonni haddan tashqari qiyalatib qoʻyish ham, juda
tik qoʻyish ham xavfli. Oʻrtasini hisob topadi.»</p>
""",
    },
]
