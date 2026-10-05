# -*- coding: utf-8 -*-
"""Matematika olami — «Buyuk matematiklar» oilasining qolgan sakkiz matni.

Toc: corner/management/commands/toc_matematika_olami.txt
  5.  Umar Xayyom — ham shoir, ham tenglama yechuvchi
  7.  Pifagor maktabi: «hamma narsa son»
  8.  Arximed: toj, hammom va «Evrika!»
  9.  Evklid «Negizlar»i — 2300 yildan beri oʻqilayotgan darslik
  11. Leonard Eyler: koʻr boʻlgan, lekin yozishdan toʻxtamagan
  12. Srinivasa Ramanujan: daftarlardagi mislsiz formulalar
  13. Ada Lavleys: birinchi dastur qanday yozilgan
  14. Emmi Nyoter: fizikaning ildizidagi ayol
⛔ AUDIO YOʻQ.

FAKTLAR (tekshirilgan; raqamlar scratchpad skripti bilan qayta hisoblangan):
  • Xayyom 1048–1131, Nishopur. Algebra risolasini ~1070-yilda Samarqandda
    (qozi Abu Tohir homiyligida) yozgan; kub tenglamalarni turlarga ajratib,
    konus kesimlari (aylana, parabola, giperbola) kesishuvi bilan yechgan.
    Jaloliy taqvimi 1079-yil, Malikshoh buyrugʻi bilan. 33 yilda 8 kabisa
    (manbalarga koʻra) → 365 + 8/33 = 365,2424 kun; quyosh yili ~365,2422;
    xato ~4300 yilda 1 kun. Grigorian: 365,2425 → ~3200 yilda 1 kun.
  • Pifagor ~570–~495 m.a., Samos → Kroton. Teoremani bobilliklar ~1000 yil
    oldin bilgan (Plimpton 322, ~m.a. 1800). Temirchi bolgʻalari — RIVOYAT
    (fizik jihatdan notoʻgʻri ham). Tor nisbatlari 2:1 oktava, 3:2 kvinta —
    haqiqiy. Gippas va √2 — RIVOYAT. 3² + 4² = 25 = 5².
  • Arximed ~287–212 m.a., Sirakuza. Toj voqeasini ~200 yil keyin Vitruviy
    yozgan — RIVOYAT. 1 kg oltin ≈ 51,8 sm³ (zichlik 19,3); 700 g oltin +
    300 g kumush (10,5) ≈ 64,8 sm³. π: 223/71 ≈ 3,1408 < π < 22/7 ≈ 3,1429,
    96 burchakli koʻpburchak bilan. Sharning hajmi silindrning 2/3 qismi;
    qabrini m.a. 75-yilda Tsitseron topgan (oʻzi yozgan).
  • Evklid ~m.a. 300, Iskandariya. «Negizlar» — 13 kitob. Tub sonlar cheksiz:
    IX kitob, 20-tasdiq. 2·3·5+1 = 31 (tub); 2·3·5·7·11·13+1 = 30031 =
    59 × 509. Beshinchi postulat → 1829 Lobachevskiy, 1832 Boyai. Birinchi
    bosma nashr 1482, Venetsiya. «Qirollik yoʻli yoʻq» — RIVOYAT (Prokl).
  • Eyler 1707 Bazel – 1783 Sankt-Peterburg. Oʻng koʻzi ~1738-yilda koʻrmay
    qolgan, 1771-yildan deyarli butunlay koʻr. 800 dan ortiq ish. f(x), e, i,
    Σ belgilarini ommalashtirgan. V − E + F = 2: kub 8 − 12 + 6 = 2,
    tetraedr 4 − 6 + 4 = 2.
  • Ramanujan 1887 Erod – 1920 Kumbakonam (32 yosh). Xardiga xat 1913-yil
    yanvar, ~120 ta formula. 1914 Kembrij. 1918 Qirollik jamiyati aʼzosi.
    1729 = 1³ + 12³ = 9³ + 10³ — ikki usulda kublar yigʻindisi boʻladigan eng
    kichik son (skript tasdiqladi). Voqeani Xardining oʻzi yozgan.
    «Yoʻqolgan daftar» 1976-yilda Jorj Endryus topgan.
  • Ada Lavleys 1815–1852, Bayronning qizi. 1843-yil: Menabreaning Bebbij
    «Analitik mashina»si haqidagi maqolasini tarjima qilib, undan uch barobar
    uzun izohlar qoʻshgan; G izohi — Bernulli sonlarini hisoblash
    algoritmi. Mashina hech qachon qurilmagan. 1980-yilda «Ada» dasturlash
    tili uning nomi bilan atalgan.
  • Emmi Nyoter 1882 Erlangen – 1935 Brin-Mor. Teoremasi 1915-yilda
    topilgan, 1918-yilda chop etilgan: har bir simmetriya ↔ saqlanish
    qonuni. Gyottingenda yillar davomida maoshsiz, Hilbert nomi bilan dars
    bergan. 1933 natsistlar ishdan haydagan → AQSh. Eynshteynning 1935-yilgi
    «New York Times» maktubi — haqiqiy.

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_22_29.py --author=prime
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
    # 5 — Umar Xayyom
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Umar Xayyom: rubobiylar va kub tenglamalar",
        "summary": (
            "Haqiqiy voqea: dunyo uni shoir sifatida biladi, lekin Xayyom algebra "
            "risolasini Samarqandda yozgan va Grigorian taqvimidan aniqroq taqvim "
            "tuzgan."
        ),
        "order":   5,
        "grammar": [
            {
                "pattern":  "Oʻrtacha yil: 365 + 8/33 kun",
                "meaning":  "33 yilning 8 tasiga bittadan qoʻshimcha kun qoʻshilsa, "
                            "bir yilga oʻrtacha 8/33 kun toʻgʻri keladi. Shu kasr "
                            "quyosh yiliga qanchalik yaqin boʻlsa, taqvim shuncha "
                            "kam adashadi.",
                "examples": [
                    "8 ÷ 33 ≈ 0,2424 → oʻrtacha yil ≈ 365,2424 kun",
                    "Quyosh yili ≈ 365,2422 kun → farq 0,0002 kun, ~4300 yilda 1 kun",
                ],
            },
        ],
        "questions": [
            {
                "text": "Xayyom algebra risolasini qaysi shaharda yozgan?",
                "choices": ["Bagʻdodda", "Samarqandda", "Isfahonda", "Nishopurda"],
                "answer": 1,
                "explanation": "Xayyom Nishopurda tugʻilgan, lekin algebraga oid "
                               "mashhur risolasini taxminan 1070-yilda Samarqandda "
                               "yozgan.",
            },
            {
                "text": "Taqvimda 33 yilning 8 tasi kabisa yili boʻlsa, oʻrtacha "
                        "yil taxminan necha kun?",
                "choices": ["365,2424 kun", "365,25 kun", "365,33 kun", "365,08 kun"],
                "answer": 0,
                "explanation": "8 ÷ 33 ≈ 0,2424. Demak oʻrtacha yil 365,2424 kun — "
                               "haqiqiy quyosh yiliga (365,2422) juda yaqin.",
            },
            {
                "text": "Xayyom kub tenglamalarni qanday yechgan?",
                "choices": [
                    "Kompyuterda hisoblab",
                    "Tavakkal qilib sonlarni sinab koʻrib",
                    "Ikki egri chiziqni chizib, ularning kesishgan nuqtasini topib",
                    "Faqat jadvallardan qarab",
                ],
                "answer": 2,
                "explanation": "U aylana, parabola kabi egri chiziqlarni chizgan. "
                               "Ular kesishgan nuqta tenglamaning yechimini "
                               "koʻrsatgan — algebra va geometriya bitta masalada.",
            },
        ],
        "body": """
<p>Dunyoda <b>Umar Xayyom</b>ni (1048–1131) koʻpincha
<span class="cn-word" data-tr="toʻrt misrali sheʼr">rubobiy</span>lari orqali tanishadi.
Uning toʻrt satrli sheʼrlari oʻnlab tillarga tarjima qilingan. Lekin oʻz davrida u
birinchi navbatda <b>olim</b> sifatida mashhur edi — matematik va
<span class="cn-word" data-tr="osmon jismlarini oʻrganuvchi olim">munajjim</span>.</p>

<p>Xayyom Nishopurda tugʻilgan. Yigirma yoshlarida u Samarqandga keldi. Shu yerda,
mahalliy qozi Abu Tohirning homiyligida, u algebraga oid eng muhim
<span class="cn-word" data-tr="ilmiy asar, kitobcha">risola</span>sini yozdi.</p>

<p>Bu risolada u <span class="cn-word" data-tr="nomaʼlum son uchinchi darajada qatnashgan tenglama">kub tenglama</span>larni,
yaʼni x<sup>3</sup> qatnashgan tenglamalarni oʻrgandi. Ularni turlarga ajratib,
har biri uchun yoʻl topdi. Uning usuli juda chiroyli edi: u ikkita
<span class="cn-word" data-tr="toʻgʻri boʻlmagan, egilgan chiziq">egri chiziq</span> —
masalan, aylana va <span class="cn-word" data-tr="koptok otilganda chizadigan yoysimon chiziq">parabola</span> —
chizardi. Ular kesishgan nuqta tenglamaning yechimini koʻrsatardi. Algebra masalasi
geometriya chizmasiga aylanardi.</p>

<p>1079-yilda sulton Malikshoh unga yangi
<span class="cn-word" data-tr="kunlar, oylar va yillarni hisoblash tizimi">taqvim</span>
tuzishni topshirdi. Muammo shunda ediki, quyosh yili butun kun emas: taxminan
<strong>365,2422</strong> kun davom etadi. Ortib qolgan qismni
<span class="cn-word" data-tr="bir kun qoʻshilgan, 366 kunlik yil">kabisa yili</span>
bilan toʻldirish kerak.</p>

<p>Manbalarga koʻra, Xayyom va uning hamkorlari har <strong>33</strong> yilda
<strong>8</strong> ta kabisa yili qoʻyishni taklif qilishgan. Unda oʻrtacha yil
365 + 8/33 ≈ <strong>365,2424</strong> kun boʻladi. Bu
<b>Jaloliy taqvimi</b> deb ataldi.</p>

<p>Bugun biz foydalanadigan Grigorian taqvimi 500 yil keyin paydo boʻldi va taxminan
3200 yilda bir kun adashadi. Jaloliy taqvimi esa — taxminan 4300 yilda bir kun.
Yaʼni Samarqandda ishlagan shoir yanada
<span class="cn-word" data-tr="haqiqatga yaqinroq">aniqroq</span> hisoblagan.</p>

<p>Sheʼr va matematika bir odamda qanday sigʻgan? Balki ikkalasi ham bitta narsani
izlagandir: ortiqcha soʻzsiz, aniq va goʻzal
<span class="cn-word" data-tr="ichki tartib, oʻzaro moslik">uygʻunlik</span>.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 7 — Pifagor
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Pifagor maktabi: «hamma narsa son»",
        "summary": (
            "Pifagor va uning shogirdlari dunyoni sonlar bilan tushuntirmoqchi "
            "boʻlgan: musiqani ham, uchburchakni ham. Mashhur teorema esa ulardan "
            "ancha oldin maʼlum boʻlgan."
        ),
        "order":   7,
        "grammar": [
            {
                "pattern":  "a² + b² = c²",
                "meaning":  "Toʻgʻri burchakli uchburchakda ikki qisqa tomon "
                            "(katetlar) kvadratlarining yigʻindisi uzun tomon "
                            "(gipotenuza) kvadratiga teng.",
                "examples": [
                    "3² + 4² = 9 + 16 = 25 = 5²",
                    "5² + 12² = 25 + 144 = 169 = 13²",
                ],
            },
        ],
        "questions": [
            {
                "text": "Pifagorchilar musiqada qanday kashfiyot qilgan?",
                "choices": [
                    "Yoqimli ovozlar tor uzunliklarining oddiy nisbatlariga mos keladi",
                    "Baland ovoz har doim yoqimli boʻladi",
                    "Musiqani faqat bolgʻa bilan chalish mumkin",
                    "Torning rangi ovozni oʻzgartiradi",
                ],
                "answer": 0,
                "explanation": "Torni teng ikkiga boʻlsa (2 : 1) — oktava, 3 : 2 "
                               "nisbatda — kvinta chiqadi. Bu ularni «hamma narsa son» "
                               "degan fikrga olib kelgan.",
            },
            {
                "text": "Toʻgʻri burchakli uchburchakning katetlari 6 va 8. "
                        "Gipotenuza nechaga teng?",
                "choices": ["14", "12", "48", "10"],
                "answer": 3,
                "explanation": "6² + 8² = 36 + 64 = 100, √100 = 10. Bu 3, 4, 5 "
                               "uchburchakning ikki barobar kattasi.",
            },
            {
                "text": "Matnga koʻra, «Pifagor teoremasi» haqida qaysi gap toʻgʻri?",
                "choices": [
                    "Uni faqat Pifagor bilgan",
                    "Uni bobilliklar Pifagordan ming yilcha oldin bilgan",
                    "U XX asrda kashf etilgan",
                    "U faqat 3, 4, 5 sonlari uchun oʻrinli",
                ],
                "answer": 1,
                "explanation": "Taxminan m.a. 1800-yilga oid bobil loy taxtachasida "
                               "bu qoidaga mos sonlar yozilgan. Pifagor nomi teoremaga "
                               "keyinroq yopishgan.",
            },
        ],
        "body": """
<p>Miloddan avvalgi VI asr. Janubiy Italiyadagi Kroton shahrida gʻalati bir
<span class="cn-word" data-tr="ustoz va shogirdlar jamoasi">maktab</span> bor edi.
Aytishlaricha, uning aʼzolari goʻsht yemas, sirlarini begonalarga aytmas va bitta gʻoyaga
ishonardi: <b>«Hamma narsa — son»</b>. Bu maktabning asoschisi Samos orolidan
kelgan <b>Pifagor</b> edi.</p>

<p>Bu gʻoya qayerdan kelgan? Eng chiroyli javob — musiqadan. Rivoyatga koʻra, Pifagor
temirchi ustaxonasi yonidan oʻtib, bolgʻalarning ovozi uygʻun chiqayotganini
eshitgan. Bu rivoyat, ehtimol, toʻqilgan. Lekin uning ortidagi kashfiyot haqiqiy.</p>

<p>Bitta <span class="cn-word" data-tr="cholgʻu asbobidagi tortilgan ip">tor</span>ni
chertib koʻring. Endi uni oʻrtasidan bosib, yarmini chertang. Ovoz yuqoriroq, lekin
xuddi oʻsha nota boʻlib eshitiladi — bu
<span class="cn-word" data-tr="bir notaning ikki barobar baland takrori">oktava</span>,
<span class="cn-word" data-tr="ikki son orasidagi munosabat">nisbat</span>i
<strong>2 : 1</strong>. Torni <strong>3 : 2</strong> nisbatda boʻlsangiz, yana
yoqimli uygʻunlik chiqadi. Quloqqa yoqadigan ovozlar oddiy sonlarga boʻysunar ekan!</p>

<p>Pifagor nomi eng koʻp bitta
<span class="cn-word" data-tr="isbotlangan matematik qoida">teorema</span> bilan
bogʻliq: toʻgʻri burchakli uchburchakda ikki qisqa tomonning kvadratlari yigʻindisi
uzun tomon kvadratiga teng. Masalan, tomonlari 3, 4 va 5 boʻlsa:
<strong>9 + 16 = 25</strong>.</p>

<p>Ammo qiziq fakt: bu qoidani Pifagordan ming yilcha oldin
<b>bobilliklar</b> bilgan. Taxminan m.a. 1800-yilga oid loy
<span class="cn-word" data-tr="yozuv bitilgan qadimiy yassi buyum">taxtacha</span>da
bu qoidaga mos sonlar ustunlari yozilgan. Pifagorchilarning xizmati boshqa edi:
ular qoidani <span class="cn-word" data-tr="mantiq bilan shubhasiz koʻrsatib berish">isbot</span>lashni muhim deb bilishgan.</p>

<p>Va aynan shu isbot ularni dahshatga soldi. Tomoni 1 boʻlgan kvadratning
<span class="cn-word" data-tr="qarama-qarshi burchaklarni tutashtiruvchi kesma">diagonal</span>i
√2 ga teng. Uni hech qanday kasr bilan aniq yozib boʻlmasligi maʼlum boʻldi.
«Hamma narsa — son» deganlar oʻz sonlariga sigʻmaydigan uzunlikni topib olishdi.
Rivoyatga koʻra, bu sirni oshkor qilgan shogird Gippas dengizga choʻktirilgan.</p>

<p>Bugun biz bunday sonlarni
<span class="cn-word" data-tr="kasr koʻrinishida yozib boʻlmaydigan son">irratsional</span>
deymiz va ulardan qoʻrqmaymiz. Lekin ularni birinchi boʻlib uchratgan odamlar uchun
bu dunyoning tartibi buzilishi bilan barobar edi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 8 — Arximed
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Arximed: toj, hammom va «Evrika!»",
        "summary": (
            "Rivoyatga koʻra, Arximed hammomda yotib, oltin toj aldovini qanday "
            "fosh qilishni topgan. Rivoyat shubhali, lekin uning ortidagi hisob — "
            "va Arximedning π haqidagi ishi — mutlaqo haqiqiy."
        ),
        "order":   8,
        "grammar": [
            {
                "pattern":  "Hajm = massa ÷ zichlik",
                "meaning":  "Bir xil ogʻirlikdagi ikki narsadan zichligi kami koʻproq "
                            "joy egallaydi. Kumush oltindan yengil modda, shuning "
                            "uchun kumush aralashgan toj sof oltin tojdan kattaroq "
                            "boʻladi va koʻproq suv siqib chiqaradi.",
                "examples": [
                    "1000 g sof oltin: 1000 ÷ 19,3 ≈ 51,8 sm³",
                    "700 g oltin + 300 g kumush: 36,3 + 28,6 ≈ 64,8 sm³",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega kumush aralashgan toj koʻproq suv siqib chiqaradi?",
                "choices": [
                    "Chunki u ogʻirroq",
                    "Chunki kumush suvni yaxshi koʻradi",
                    "Chunki uning shakli boshqacha",
                    "Chunki kumush oltindan kamroq zich, bir xil ogʻirlikda koʻproq "
                    "joy egallaydi",
                ],
                "answer": 3,
                "explanation": "Ogʻirlik bir xil, lekin kumushning zichligi kichik — "
                               "u kattaroq hajm egallaydi. Suvga botirganda katta "
                               "hajm koʻproq suv siqib chiqaradi.",
            },
            {
                "text": "Arximed π sonini qaysi ikki son orasida ekanini isbotlagan?",
                "choices": [
                    "3 va 4 orasida",
                    "3,1408 va 3,1429 orasida",
                    "3,14 va 3,15 orasida",
                    "3,2 va 3,3 orasida",
                ],
                "answer": 1,
                "explanation": "U 96 burchakli koʻpburchaklar bilan π ni 223/71 ≈ "
                               "3,1408 va 22/7 ≈ 3,1429 orasiga «qamagan». Haqiqiy "
                               "qiymat 3,1416 aynan shu oraliqda.",
            },
            {
                "text": "Nega toj voqeasi «rivoyat» deb ataladi?",
                "choices": [
                    "Uni Arximeddan 200 yilcha keyin yashagan muallif yozgan",
                    "Arximed hech qachon hammomga bormagan",
                    "Oltin u davrda boʻlmagan",
                    "Arximedning oʻzi bu haqda kitob yozgan",
                ],
                "answer": 0,
                "explanation": "Voqeani Rim meʼmori Vitruviy taxminan ikki asr keyin "
                               "yozib qoldirgan. Arximedning oʻz asarlarida bu haqda "
                               "hech narsa yoʻq.",
            },
        ],
        "body": """
<p>Sitsiliya oroli, Sirakuza shahri, miloddan avvalgi III asr. Shoh Gieron zargarga
oltin beradi va undan <span class="cn-word" data-tr="shohning boshiga kiyiladigan bezak">toj</span>
yasashni buyuradi. Toj tayyor, ogʻirligi ham berilgan oltin bilan bir xil. Lekin
shohda shubha bor: zargar oltinning bir qismini oʻgʻirlab, oʻrniga arzon kumush
qoʻshmaganmikin?</p>

<p>Tojni eritib tekshirib boʻlmaydi — u buziladi. Shoh bu masalani shahardagi eng
aqlli odam — <b>Arximed</b>ga topshiradi.</p>

<p><b>Rivoyatga koʻra</b>, Arximed hammomga tushadi va
<span class="cn-word" data-tr="suv toʻldirilgan katta idish">vanna</span>dagi suv
koʻtarilib, toshib ketganini koʻradi. U yechimni tushunadi va yalangʻoch holda
koʻchaga yugurib chiqib, <i>«Evrika!»</i> — «Topdim!» deb baqiradi.</p>

<p>Bu voqeani Arximeddan 200 yilcha keyin Rim meʼmori Vitruviy yozgan. Uning qanchalik
toʻgʻri ekanini hech kim bilmaydi. Lekin gʻoyaning matematikasi
<span class="cn-word" data-tr="rost, chin">haqiqiy</span>.</p>

<p>Har bir moddaning <span class="cn-word" data-tr="bir sm³ moddaning necha gramm ekani">zichlik</span>i
bor. Oltin juda zich: bir kilogramm oltin atigi <strong>51,8 sm³</strong> joy
egallaydi. Kumush yengilroq. Agar tojning 300 grammi kumush boʻlsa, uning
<span class="cn-word" data-tr="jism egallagan joy kattaligi">hajm</span>i
taxminan <strong>64,8 sm³</strong> ga oʻsadi. Ogʻirligi bir xil, lekin hajmi
<strong>13 sm³</strong> katta! Tojni suvga botirsangiz, u koʻproq suv
<span class="cn-word" data-tr="bosib, oʻrnidan chiqarib yubormoq">siqib chiqar</span>adi.</p>

<p>Arximedning haqiqiy kashfiyotlari bundan ham ajoyib. U doiraning ichiga va
tashqarisiga <strong>96</strong> burchakli
<span class="cn-word" data-tr="koʻp tomonli yopiq shakl">koʻpburchak</span>
chizib, <b>π</b> sonini ikki tomondan «qamab» qoʻydi: π son 3,1408 dan katta va
3,1429 dan kichik. Bu ikki ming yil davomida eng yaxshi
<span class="cn-word" data-tr="taxminiy, lekin yaqin qiymat">yaqinlashish</span>lardan biri boʻlib qoldi.</p>

<p>U yana bir narsani isbotladi: shar oʻziga tashqi chizilgan
<span class="cn-word" data-tr="ikki doira asosli dumaloq jism">silindr</span>
hajmining aynan <strong>2/3</strong> qismini egallaydi. Arximed bu kashfiyotini
shunchalik sevganki, qabr toshiga shar va silindr chizilishini vasiyat qilgan.
Rim notigʻi Tsitseron m.a. 75-yilda bu qabrni chizmasidan tanib topganini yozib
qoldirgan.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 9 — Evklid
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Evklid «Negizlar»i: 2300 yoshli darslik",
        "summary": (
            "Iskandariyalik Evklid yozgan 13 kitob ikki ming yildan ortiq "
            "geometriya darsligi boʻlib keldi. Undagi eng chiroyli isbotlardan "
            "biri — tub sonlar hech qachon tugamasligi."
        ),
        "order":   9,
        "grammar": [
            {
                "pattern":  "Tub sonlar cheksiz: hammasini koʻpaytir va 1 qoʻsh",
                "meaning":  "Tub sonlar tugaydi deb faraz qilaylik. Ularning "
                            "hammasini koʻpaytirib, 1 qoʻshamiz. Hosil boʻlgan son "
                            "roʻyxatdagi birorta tub songa boʻlinmaydi (qoldiq "
                            "doim 1). Demak roʻyxatda yoʻq yangi tub son bor.",
                "examples": [
                    "2 × 3 × 5 + 1 = 31 — oʻzi yangi tub son",
                    "2 × 3 × 5 × 7 × 11 × 13 + 1 = 30031 = 59 × 509 — yangi tub "
                    "sonlar 59 va 509",
                ],
            },
        ],
        "questions": [
            {
                "text": "Evklid kitobining eng katta yangiligi nimada edi?",
                "choices": [
                    "U birinchi marta raqamlarni ixtiro qilgan",
                    "U bir necha oddiy haqiqatdan boshlab, qolgan hamma narsani "
                    "isbot bilan keltirib chiqargan",
                    "Unda rasmlar koʻp boʻlgan",
                    "U faqat masalalar toʻplami edi",
                ],
                "answer": 1,
                "explanation": "Evklid aksiomalardan boshlab har bir tasdiqni "
                               "oldingilaridan isbotlagan. Bu tartib keyin butun "
                               "fanning namunasiga aylangan.",
            },
            {
                "text": "2 × 3 × 7 + 1 qaysi songa teng va u tub sonmi?",
                "choices": [
                    "42, tub emas",
                    "41, tub emas",
                    "43, tub son",
                    "44, tub emas",
                ],
                "answer": 2,
                "explanation": "2 × 3 × 7 = 42, plyus 1 = 43. U 2 ga, 3 ga, 7 ga "
                               "boʻlinmaydi — va oʻzi tub son.",
            },
            {
                "text": "30031 = 59 × 509. Bu Evklid isbotiga zid emasmi?",
                "choices": [
                    "Zid — isbot notoʻgʻri ekan",
                    "Zid emas — chunki 30031 juft son",
                    "Zid — chunki 59 juda katta",
                    "Zid emas — hosil boʻlgan son tub boʻlmasa ham, uning "
                    "boʻluvchilari roʻyxatda yoʻq yangi tub sonlar",
                ],
                "answer": 3,
                "explanation": "Isbot «yangi son tub» demaydi. U «roʻyxatda yoʻq "
                               "tub son bor» deydi. 59 va 509 roʻyxatdagi 2, 3, 5, "
                               "7, 11, 13 ning birortasi emas.",
            },
        ],
        "body": """
<p>Qaysi darslik eng uzoq yashagan? Javob — taxminan miloddan avvalgi 300-yilda
Iskandariyada yozilgan <b>«Negizlar»</b>. Uni yunon matematigi <b>Evklid</b> yozgan.
Bu kitob ikki ming yildan ortiq Yevropa va Sharqda geometriya darsligi boʻlib keldi.
Aytilishicha, eng koʻp nashr qilingan kitoblar roʻyxatida u birinchilar qatorida.</p>

<p>Evklid haqida juda kam narsa maʼlum. Rivoyatga koʻra, shoh Ptolemey undan
geometriyani osonroq oʻrganish yoʻlini soʻragan. Evklid javob bergan: «Geometriyaga
shohlar uchun alohida yoʻl yoʻq».</p>

<p>«Negizlar» <strong>13</strong> kitobdan iborat. Uning kuchi yangi faktlarda emas,
<b>tartib</b>da edi. Evklid bir necha oddiy, shubhasiz haqiqatdan boshlaydi —
ularni <span class="cn-word" data-tr="isbotsiz qabul qilinadigan boshlangʻich haqiqat">aksioma</span>
deymiz. Masalan: «ikki nuqta orqali bitta toʻgʻri chiziq oʻtkazish mumkin». Keyin har
bir yangi <span class="cn-word" data-tr="isbotlanishi kerak boʻlgan fikr">tasdiq</span>ni
faqat oldingilardan <span class="cn-word" data-tr="mantiq bilan shubhasiz koʻrsatib berish">isbot</span>lab
chiqaradi. Hech narsa «koʻrinib turibdi» deb qabul qilinmaydi.</p>

<p>Bu kitobdagi eng goʻzal isbotlardan biri sonlar haqida.
<span class="cn-word" data-tr="faqat 1 ga va oʻziga boʻlinadigan son">Tub son</span>lar
— 2, 3, 5, 7, 11, 13… Ular tugaydimi?</p>

<p>Evklid shunday mulohaza qiladi. Tub sonlar tugaydi deb
<span class="cn-word" data-tr="vaqtincha haqiqat deb olmoq">faraz qil</span>aylik.
Ularning hammasini koʻpaytiramiz va <strong>1</strong> qoʻshamiz. Yangi son
roʻyxatdagi birorta tub songa boʻlinmaydi — har safar
<span class="cn-word" data-tr="boʻlishdan ortib qolgan son">qoldiq</span>
<strong>1</strong> chiqadi. Demak uning roʻyxatda yoʻq tub boʻluvchisi bor. Roʻyxat
toʻliq emas ekan!</p>

<p>Sinab koʻramiz: 2 × 3 × 5 + 1 = <strong>31</strong> — yangi tub son. Endi
2 × 3 × 5 × 7 × 11 × 13 + 1 = <strong>30031</strong>. Bu tub emas:
30031 = 59 × 509. Lekin 59 ham, 509 ham roʻyxatda yoʻq edi. Isbot yana ishladi.</p>

<p>Bitta aksioma — <span class="cn-word" data-tr="bir-biri bilan hech qachon kesishmaydigan chiziqlar">parallel</span>
toʻgʻri chiziqlar haqidagisi — boshqalardan murakkabroq koʻrinardi. Matematiklar uni
ikki ming yil isbotlashga urindi. 1829-yilda Lobachevskiy, 1832-yilda Boyai buning
iloji yoʻqligini koʻrsatdi va butunlay yangi
<span class="cn-word" data-tr="shakl va fazoni oʻrganuvchi fan">geometriya</span>
paydo boʻldi. Evklidning bitta savoli ham yangi olam ochgan.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 11 — Leonard Eyler
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Leonard Eyler: koʻr boʻlgan, lekin yozishdan toʻxtamagan",
        "summary": (
            "Haqiqiy voqea: tarixdagi eng sermahsul matematik umrining oxirgi oʻn "
            "yildan koʻprogʻida deyarli hech narsani koʻrmagan — va ishlashda "
            "davom etgan."
        ),
        "order":   11,
        "grammar": [
            {
                "pattern":  "Eyler formulasi: U − Q + Y = 2",
                "meaning":  "Teshigi yoʻq har qanday qavariq koʻpyoqda uchlar soni "
                            "(U) minus qirralar soni (Q) plyus yoqlar soni (Y) "
                            "doim 2 ga teng.",
                "examples": [
                    "Kub: 8 − 12 + 6 = 2",
                    "Uchburchakli piramida: 4 − 6 + 4 = 2",
                ],
            },
        ],
        "questions": [
            {
                "text": "Eyler koʻzi koʻrmay qolgach qanday ishlagan?",
                "choices": [
                    "Butunlay ishlashni toʻxtatgan",
                    "Faqat sheʼr yozgan",
                    "Hisoblarni xayolida qilib, oʻgʻillari va yordamchilariga "
                    "aytib yozdirgan",
                    "Boshqa olimlarning ishlarini koʻchirgan",
                ],
                "answer": 2,
                "explanation": "Uning xotirasi va xayoliy hisoblash qobiliyati "
                               "ajoyib edi. U yozdirib turgan va ishlari hatto "
                               "koʻpaygan.",
            },
            {
                "text": "Asosi kvadrat boʻlgan piramidada 5 ta uch va 8 ta qirra "
                        "bor. Eyler formulasiga koʻra, nechta yoq bor?",
                "choices": ["3", "4", "5", "6"],
                "answer": 2,
                "explanation": "U − Q + Y = 2 → 5 − 8 + Y = 2 → Y = 5. Haqiqatan: "
                               "1 kvadrat asos va 4 ta uchburchak yon yoq.",
            },
            {
                "text": "Qaysi belgilarni Eyler ommalashtirgan?",
                "choices": [
                    "+ va − belgilarini",
                    "f(x), e, i va Σ belgilarini",
                    "Rim raqamlarini",
                    "0 raqamini",
                ],
                "answer": 1,
                "explanation": "Funksiya uchun f(x), e soni, i va yigʻindi "
                               "belgisi Σ — bugun har bir darslikda bor, va "
                               "ularni Eyler keng tarqatgan.",
            },
        ],
        "body": """
<p>1771-yil, Sankt-Peterburg. Shahar boʻylab katta
<span class="cn-word" data-tr="koʻp joyni qamrab olgan yongʻin">yongʻin</span>
tarqaladi. Yonayotgan uylardan birida keksa bir odam bor — u deyarli hech narsani
koʻrmaydi. Uni olib chiqishadi. Bu odam — dunyodagi eng sermahsul matematik
<b>Leonard Eyler</b> (Leonhard Euler) edi.</p>

<p>Eyler 1707-yilda Shveysariyaning Bazel shahrida tugʻilgan. Yoshligidanoq uning
bir xususiyati hammani hayratda qoldirardi: u murakkab hisoblarni qogʻozsiz,
xayolida bajara olardi. Uning <span class="cn-word" data-tr="eslab qolish qobiliyati">xotira</span>si
ham afsonaviy edi.</p>

<p>Taxminan 1738-yilda Eylerning oʻng koʻzi koʻrmay qoldi. 1771-yilga kelib esa
<span class="cn-word" data-tr="koʻz gavharining xiralashishi">katarakta</span>
tufayli u deyarli butunlay <span class="cn-word" data-tr="koʻzi koʻrmaydigan">koʻr</span>
boʻlib qoldi. Boshqa odam uchun bu ishning tugashi boʻlardi.</p>

<p>Eyler esa ishlashda davom etdi. U formulalarni xayolida tuzar va oʻgʻillari hamda
yordamchilariga aytib <span class="cn-word" data-tr="birovga gapirib yozdirmoq">yozdirar</span>di.
Aytishlaricha, bir yilda u haftasiga oʻrtacha bitta
<span class="cn-word" data-tr="ilmiy jurnalda chop etilgan ish">maqola</span>
tayyorlagan. Umri davomida uning <strong>800</strong> dan ortiq ishi chiqdi.</p>

<p>Biz har kuni uning izidan yuramiz. Funksiyani <b>f(x)</b> deb yozish,
<b>e</b> soni, <b>i</b> belgisi, yigʻindini bildiruvchi <b>Σ</b> — bularni Eyler
ommalashtirgan.</p>

<p>Uning eng oddiy va eng chiroyli kashfiyotlaridan biri — koʻpyoqlar haqida.
<span class="cn-word" data-tr="yassi yuzalardan tuzilgan jism">Koʻpyoq</span>ni
oling: kub, piramida, tuz kristali. Uning uchlarini (U), qirralarini (Q) va
yoqlarini (Y) sanang. Kubda 8 ta uch, 12 ta qirra, 6 ta yoq bor:
<strong>8 − 12 + 6 = 2</strong>. Uchburchakli piramidada: 4 − 6 + 4 = 2. Yana 2!</p>

<p>Shakl qanday boʻlmasin, agar unda teshik boʻlmasa, javob doim
<strong>2</strong>. Bu son shaklning oʻlchamiga ham, burchaklariga ham bogʻliq emas.
Bu kuzatish keyinchalik shakllarning eng chuqur xossalarini oʻrganadigan yangi fan —
<span class="cn-word" data-tr="choʻzilsa ham oʻzgarmaydigan xossalarni oʻrganuvchi fan">topologiya</span>ning
urugʻlaridan biri boʻldi.</p>

<p>Eyler 1783-yilda vafot etdi. Oʻsha kuni ham u
<span class="cn-word" data-tr="issiq havo bilan osmonga koʻtariladigan katta shar">havo shari</span>ning
koʻtarilishini hisoblagan edi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 12 — Ramanujan
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ramanujan va 1729 raqamli taksi",
        "summary": (
            "Haqiqiy voqea: Hindistonning kambagʻal oilasidan chiqqan, deyarli "
            "oʻzi oʻqigan yigit Kembrij matematiklarini hayratga solgan. Uning "
            "daftarlari bugun ham oʻrganilmoqda."
        ),
        "order":   12,
        "grammar": [
            {
                "pattern":  "1729 = 1³ + 12³ = 9³ + 10³",
                "meaning":  "Ikkita kubning yigʻindisi sifatida ikki xil usulda "
                            "yozish mumkin boʻlgan eng kichik son — 1729.",
                "examples": [
                    "1³ + 12³ = 1 + 1728 = 1729",
                    "9³ + 10³ = 729 + 1000 = 1729",
                ],
            },
        ],
        "questions": [
            {
                "text": "Ramanujan Kembrijga qanday yoʻl topdi?",
                "choices": [
                    "Imtihonni aʼlo topshirib",
                    "Ingliz matematigi Xardiga formulalari yozilgan xat yuborib",
                    "Boy qarindoshlari yordamida",
                    "Kitob yozib mashhur boʻlib",
                ],
                "answer": 1,
                "explanation": "1913-yilda u Xardiga 100 dan ortiq formula yozilgan "
                               "xat yubordi. Xardi uni Angliyaga taklif qildi.",
            },
            {
                "text": "9³ + 10³ nechaga teng?",
                "choices": ["1000", "1900", "1729", "190"],
                "answer": 2,
                "explanation": "9 × 9 × 9 = 729, 10 × 10 × 10 = 1000. "
                               "729 + 1000 = 1729.",
            },
            {
                "text": "Nega Xardi «1729 zerikarli son» deganda Ramanujan bunga "
                        "qoʻshilmadi?",
                "choices": [
                    "U ikkita kubning yigʻindisi sifatida ikki usulda yoziladigan "
                    "eng kichik son",
                    "Bu yil u tugʻilgan yil edi",
                    "Bu son tub son",
                    "U 1000 dan katta",
                ],
                "answer": 0,
                "explanation": "1729 = 1³ + 12³ = 9³ + 10³. Bundan kichik birorta son "
                               "bu xossaga ega emas.",
            },
        ],
        "body": """
<p>1913-yil yanvar. Kembrij universitetidagi matematik <b>Godfri Xardi</b>
(G. H. Hardy) Hindistondan kelgan xatni ochadi. Xat muallifi — Madrasdagi
<span class="cn-word" data-tr="hisob-kitob ishlari bilan shugʻullanuvchi xodim">hisobchi</span>,
universitet diplomi yoʻq yigit. Xatda <strong>100</strong> dan ortiq
<span class="cn-word" data-tr="matematik qoida, harflar va belgilar bilan yozilgan">formula</span>
bor — koʻpi hech qanday isbotsiz.</p>

<p>Xardi avval uni tentaklik deb oʻyladi. Keyin qaytadan oʻqidi. Formulalarning bir
qismi unga tanish edi, bir qismini u oʻzi tekshirib koʻrdi, ayrimlari esa butunlay
tushunarsiz edi. Xardi keyinroq yozganidek, bunday formulalarni oʻylab topish uchun
eng yuqori darajadagi matematik boʻlish kerak edi.</p>

<p>Xat muallifi <b>Srinivasa Ramanujan</b> edi. U 1887-yilda Janubiy Hindistonda,
kambagʻal oilada tugʻilgan. Matematikani u asosan bitta eski
<span class="cn-word" data-tr="oʻqish uchun kitob">qoʻllanma</span>dan oʻrgangan va
oʻz kashfiyotlarini <span class="cn-word" data-tr="yozuv uchun varaqlar toʻplami">daftar</span>larga
yozib borgan.</p>

<p>1914-yilda u Kembrijga keldi. Xardi bilan birga ular sonlar haqida ajoyib
natijalar oldi. 1918-yilda Ramanujan Qirollik jamiyatiga aʼzo boʻldi — bu
olimlar uchun eng yuqori <span class="cn-word" data-tr="hurmat belgisi, mukofot">sharaf</span>lardan biri.</p>

<p>Lekin Angliyaning sovuq iqlimi va ovqati unga yoqmadi, u ogʻir kasal boʻlib qoldi.
Shu davrdan mashhur voqea qolgan — uni Xardining oʻzi yozib qoldirgan. Xardi
<span class="cn-word" data-tr="davolanish joyi">kasalxona</span>ga
<span class="cn-word" data-tr="pullik yengil avtomobil">taksi</span>da keladi va
deydi: «Taksining raqami <strong>1729</strong> edi. Juda zerikarli son».</p>

<p>Ramanujan darhol javob beradi: «Yoʻq, bu juda qiziq son! Bu ikkita
<span class="cn-word" data-tr="sonni oʻziga uch marta koʻpaytirish">kub</span>ning
yigʻindisi sifatida <b>ikki xil</b> usulda yoziladigan eng kichik son».</p>

<p>Tekshiramiz: 1 + 1728 = 1729, yaʼni <strong>1³ + 12³</strong>. Va
729 + 1000 = 1729, yaʼni <strong>9³ + 10³</strong>. Bundan kichik birorta son bunday
qila olmaydi.</p>

<p>Ramanujan 1920-yilda, atigi 32 yoshida vafot etdi. 1976-yilda kutubxonada
uning yana bir «yoʻqolgan daftari» topildi. Matematiklar uning
<span class="cn-word" data-tr="koʻp narsani oʻz ichiga olgan boylik">xazina</span>sini
bugun ham isbotlab tugata olmayapti.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 13 — Ada Lavleys
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ada Lavleys: hali yoʻq mashina uchun birinchi dastur",
        "summary": (
            "Haqiqiy voqea: 1843-yilda Ada Lavleys hech qachon qurilmagan "
            "mashina uchun hisoblash rejasini yozdi — va kompyuterlar faqat "
            "sonlar bilan cheklanmasligini birinchilardan boʻlib tushundi."
        ),
        "order":   13,
        "grammar": [
            {
                "pattern":  "Algoritm: qadamlar va takrorlash",
                "meaning":  "Dastur — mashina bajaradigan aniq qadamlar ketma-"
                            "ketligi. Bir xil ishni koʻp marta qilish kerak boʻlsa, "
                            "uni har safar qayta yozish shart emas: «shu qadamlarni "
                            "N marta takrorla» deyish kifoya.",
                "examples": [
                    "1 dan boshla; 5 marta takrorla: sonni 2 ga koʻpaytir → 32",
                    "Ada rejasida ham ayrim qadamlar takror-takror bajarilgan",
                ],
            },
        ],
        "questions": [
            {
                "text": "Ada Lavleysning eng mashhur ishi nima?",
                "choices": [
                    "Bebbij mashinasini oʻz qoʻli bilan qurgani",
                    "Birinchi telefonni ixtiro qilgani",
                    "Analitik mashina haqidagi maqolaga yozgan izohlari va "
                    "undagi hisoblash rejasi",
                    "Otasining sheʼrlarini nashr qilgani",
                ],
                "answer": 2,
                "explanation": "U maqolani tarjima qilib, undan uch barobar uzun "
                               "izohlar qoʻshgan. «G» izohida mashina uchun hisoblash "
                               "rejasi — birinchi dasturlardan biri bor.",
            },
            {
                "text": "Dastur: «3 dan boshla. 4 marta takrorla: sonni 2 ga "
                        "koʻpaytir». Natija qancha?",
                "choices": ["48", "24", "11", "12"],
                "answer": 0,
                "explanation": "3 → 6 → 12 → 24 → 48. Toʻrt marta ikki barobar: "
                               "3 × 16 = 48.",
            },
            {
                "text": "Ada mashina haqida qanday bashorat qilgan?",
                "choices": [
                    "U hech qachon ishlamaydi",
                    "U faqat qoʻshish va ayirishni biladi",
                    "U odamdan aqlliroq boʻladi",
                    "Agar musiqa qoidalari belgilar bilan yozilsa, u musiqa ham "
                    "tuza olishi mumkin",
                ],
                "answer": 3,
                "explanation": "Ada mashina sonlardan boshqa narsalar — masalan, "
                               "notalar — bilan ham ishlashi mumkinligini yozgan. "
                               "Bugungi kompyuterlar aynan shunday.",
            },
        ],
        "body": """
<p>1815-yil, London. Mashhur shoir <b>Lord Bayron</b>ning qizi Ada tugʻiladi.
Bir necha haftadan keyin Bayron oilani tashlab ketadi va qizini boshqa hech qachon
koʻrmaydi. Adaning onasi qizi otasiga oʻxshab «xayolparast» boʻlib qolishidan
qoʻrqadi va unga qatʼiy <span class="cn-word" data-tr="aniq fanlar boʻyicha taʼlim">matematika</span>
oʻrgatadi.</p>

<p>Ada 17 yoshida <b>Charlz Bebbij</b> (Charles Babbage) bilan tanishadi. Bebbij bir
<span class="cn-word" data-tr="hisoblash uchun qurilgan mexanizm">hisoblash mashinasi</span>
loyihasini oʻylab yurardi. U ogʻir tishli gʻildiraklardan iborat boʻlib, uni
<span class="cn-word" data-tr="teshikli kartochkalar">perfokarta</span>lar orqali
boshqarish rejalashtirilgan edi. Bebbij uni <b>«Analitik mashina»</b> deb atadi.</p>

<p>1843-yilda Ada italyan muhandisining bu mashina haqidagi fransuzcha maqolasini
inglizchaga tarjima qildi. Lekin u shunchaki tarjima qilmadi: maqolaga oʻzidan
<span class="cn-word" data-tr="matnga qoʻshilgan tushuntirish">izoh</span>lar qoʻshdi
va ular asl maqoladan <strong>uch barobar</strong> uzun boʻlib chiqdi.</p>

<p>Oxirgi, «G» izohida Ada mashina murakkab sonlar ketma-ketligini qanday hisoblashi
kerakligini qadam-baqadam yozib chiqdi. Qaysi qadam qaysi qadamdan keyin keladi,
qaysi natija qayerda saqlanadi, qaysi qadamlar
<span class="cn-word" data-tr="bir ishni qayta-qayta bajarish">takrorla</span>nadi.
Bugun biz bunday rejani <span class="cn-word" data-tr="kompyuter bajaradigan buyruqlar toʻplami">dastur</span>
deymiz. Shuning uchun Adani koʻpincha birinchi
<span class="cn-word" data-tr="dastur yozuvchi mutaxassis">dasturchi</span> deyishadi.</p>

<p>Eng ajablanarlisi shuki, mashina hech qachon qurilmadi. Ada mavjud boʻlmagan
kompyuter uchun dastur yozgan edi.</p>

<p>Ammo uning eng uzoqni koʻrgan fikri boshqa edi. U yozgan edi: agar musiqadagi
tovushlar orasidagi qoidalarni belgilar bilan ifodalash mumkin boʻlsa, mashina
<span class="cn-word" data-tr="musiqa asari">kuy</span> ham tuza oladi. Yaʼni
mashina faqat sonlarni emas, istalgan
<span class="cn-word" data-tr="qoidaga boʻysunadigan ishora">belgi</span>larni qayta
ishlay oladi. Yuz yildan keyin aynan shu gʻoya hamma kompyuterlarning asosiga
aylandi.</p>

<p>Ada 1852-yilda, atigi 36 yoshida vafot etdi. 1980-yilda dasturlash tillaridan biri
uning sharafiga <b>«Ada»</b> deb nomlandi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 14 — Emmi Nyoter
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Emmi Nyoter: fizikaning ildizidagi ayol",
        "summary": (
            "Haqiqiy voqea: universitet unga yillar davomida maosh bermagan, "
            "lekin u fizikaning eng chuqur qonunlaridan birini isbotlagan — "
            "simmetriya va saqlanish qonunlari aloqasini."
        ),
        "order":   14,
        "grammar": [
            {
                "pattern":  "Nyoter teoremasi: simmetriya → saqlanish",
                "meaning":  "Agar tabiat qonunlari biror oʻzgarishda bir xil qolsa "
                            "(simmetriya), unda albatta biror miqdor hech qachon "
                            "yoʻqolmaydi va paydo boʻlmaydi (saqlanadi).",
                "examples": [
                    "Qonunlar bugun va ertaga bir xil → energiya saqlanadi",
                    "Qonunlar bu yerda va u yerda bir xil → harakat miqdori saqlanadi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Gyottingen universitetida Nyoter dastlab qanday ishlagan?",
                "choices": [
                    "Rektor boʻlib",
                    "Yillar davomida maoshsiz, ayrim darslarini Hilbert nomi bilan "
                    "eʼlon qilib",
                    "Faqat kutubxonachi boʻlib",
                    "Talaba sifatida",
                ],
                "answer": 1,
                "explanation": "Oʻsha davrda ayolga professorlik berilmasdi. "
                               "Shuning uchun uning darslari Hilbert nomi bilan "
                               "eʼlon qilingan va u uzoq vaqt maosh olmagan.",
            },
            {
                "text": "Nyoter teoremasiga koʻra, fizika qonunlari vaqt oʻtishi "
                        "bilan oʻzgarmasligidan nima kelib chiqadi?",
                "choices": [
                    "Vaqt toʻxtaydi",
                    "Hamma narsa harakatlanadi",
                    "Energiya saqlanadi",
                    "Yer aylanadi",
                ],
                "answer": 2,
                "explanation": "Vaqt boʻyicha simmetriyaga energiyaning saqlanish "
                               "qonuni mos keladi.",
            },
        ],
        "body": """
<p>1915-yil, Germaniyaning Gyottingen universiteti. Matematiklar
<b>David Hilbert</b> va <b>Feliks Klein</b> bir ayolni professorlar qatoriga olishni
taklif qilishadi. Professorlarning bir qismi qarshi chiqadi: «Askarlarimiz urushdan
qaytib, ayoldan dars olishlari kerakmi?»</p>

<p>Aytishlaricha, Hilbert shunday javob bergan: «Janoblar, bu universitet
<span class="cn-word" data-tr="ilmiy kengash, majlis">senat</span>i, hammom emas».
Bu soʻzlar ehtimol keyin boʻyalgan. Lekin natija haqiqiy: <b>Emmi Nyoter</b>
(Emmy Noether) yillar davomida <span class="cn-word" data-tr="ish haqi">maosh</span>
olmay dars berdi. Uning darslari jadvalda Hilbert nomi bilan eʼlon qilinardi.</p>

<p>Aynan shu yillarda u fizikadagi eng chuqur gʻoyalardan birini isbotladi.</p>

<p>Avval ikkita tushunchani koʻraylik.
<span class="cn-word" data-tr="oʻzgartirilganda ham bir xil qolish xossasi">Simmetriya</span>
— biror narsani oʻzgartirsangiz ham, u oʻzgarmay qolishi. Kvadratni 90 gradusga
burang — u oʻsha-oʻsha kvadrat. <span class="cn-word" data-tr="miqdor yoʻqolmasligi va yoʻqdan paydo boʻlmasligi">Saqlanish</span>
esa — biror miqdor yoʻqolmasligi va yoʻqdan paydo boʻlmasligi. Masalan,
<span class="cn-word" data-tr="ish bajarish qobiliyati">energiya</span>.</p>

<p>Nyoter bu ikkisini bogʻladi: <b>har bir simmetriya ortida bitta saqlanish
<span class="cn-word" data-tr="tabiatda doim bajariladigan qoida">qonun</span>i
yashiringan</b>.</p>

<p>Misol. Fizika qonunlari bugun ham, ertaga ham bir xil. Koptok bugun qanday
tushsa, yuz yildan keyin ham shunday tushadi. Bu — vaqt boʻyicha simmetriya. Nyoter
teoremasi undan qatʼiy xulosa chiqaradi: demak energiya saqlanadi. Qonunlar
Toshkentda ham, Londonda ham bir xil — demak harakat miqdori saqlanadi.</p>

<p>Bu kashfiyot fiziklarga yangi
<span class="cn-word" data-tr="ish yoki fikrlash yoʻli">usul</span> berdi: yangi
saqlanish qonunini izlash oʻrniga, simmetriyani izlash kifoya. Bugungi zarralar
fizikasi deyarli butunlay shu gʻoyaga tayanadi.</p>

<p>1933-yilda natsistlar hukumati Nyoterni yahudiy boʻlgani uchun universitetdan
haydadi. U AQShga koʻchib ketdi va 1935-yilda vafot etdi. Oʻshanda
<b>Albert Eynshteyn</b> gazetaga maktub yozib, uni ayollar oliy taʼlim olishni
boshlagandan beri chiqqan eng buyuk
<span class="cn-word" data-tr="juda yuqori isteʼdod egasi">daho</span>
matematik deb atadi.</p>
""",
    },
]
