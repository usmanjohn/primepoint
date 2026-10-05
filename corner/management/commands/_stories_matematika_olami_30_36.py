# -*- coding: utf-8 -*-
"""Matematika olami — 16, 18, 19, 21, 22, 28 va 29-matnlar.

Toc: corner/management/commands/toc_matematika_olami.txt
  16. Qor parchasi: oltita nur, cheksiz naqsh             (tabiat)
  18. Chigʻanoqdagi spiral                                (tabiat)
  19. Daraxt shoxlari nega shunday tarmoqlanadi           (tabiat)
  21. Zebra chiziqlari: naqsh ortidagi qoida              (tabiat)
  22. Samolyot nega xaritada egri uchadi                  (tabiat)
  28. Bir xil ovoz, uch xil gʻolib — sanash usullari      (kundalik)
  29. Nega yoʻlda tirbandlik oʻz-oʻzidan paydo boʻladi    (kundalik)
⛔ AUDIO YOʻQ.

FAKTLAR (tekshirilgan; raqamlar scratchpad skripti bilan qayta hisoblangan):
  • Kepler 1611 «Olti burchakli qor parchasi haqida». Uilson Bentli 1885-yil
    15-yanvarda birinchi qor parchasini suratga olgan, umri davomida 5000 dan
    ortiq. Koch qor parchasi 1904; perimetr har qadamda × 4/3: 10 qadamda
    ≈ 17,76 marta; yuza esa dastlabki uchburchakning 8/5 qismidan oshmaydi.
  • Logarifmik spiral: har aylanishda masofa bir xil songa koʻpayadi.
    Yakob Bernulli (1654–1705) «ajoyib spiral», qabr toshiga «Oʻzgarib,
    yana oʻsha boʻlib tirilaman»; usta Arximed spiralini oʻyib qoʻygan
    (keng tarqalgan hikoya, Bazel soborida koʻrish mumkin). Nautilus
    spirali oltin nisbat EMAS — oltin spiral har aylanishda ~6,85 marta
    kengayadi, nautilus ancha kam (~3 atrofida).
  • Leonardo da Vinchi qoidasi (daftarlarida): shoxlar kesimlari yuzalari
    yigʻindisi tananing kesimiga teng. d² qoidasi: 20 sm → ikki teng shox
    ≈ 14,1 sm; 10 sm → 6 va 8 sm (36 + 64 = 100).
  • Alan Tyuring 1952 «Morfogenezning kimyoviy asoslari»; faollashtiruvchi
    + toʻsuvchi. Myurrey qoidasi: dogʻli hayvonning dumi yoʻl-yoʻl boʻlishi
    mumkin, aksi emas (J. D. Murray, «Mathematical Biology»).
  • Toshkent (41,3°N 69,2°E) – Nyu-York (40,7°N 74,0°W): katta doira
    ≈ 10 170 km, eng shimoliy nuqtasi ≈ 70°N; 41-parallel boʻylab ≈ 12 020 km.
    Merkator xaritasi 1569. Afrika 30,4 mln km², Grenlandiya 2,17 mln km² →
    ~14 marta.
  • Ovoz: 6 kishi A>C>B, 5 kishi B>C>A, 4 kishi C>B>A. Koʻpchilik → A (6);
    ikki tur → B (9 : 6); Borda (2–1–0) → C (19, B 14, A 12); C har bir
    juftlikda ham yutadi (9 : 6 va 10 : 5). Borda 1770, Kondorse 1785,
    Errou teoremasi 1951, Nobel 1972.
  • Sugiyama tajribasi (Yaponiya, 2008): 230 m aylana yoʻl, 22 mashina,
    tirbandlik toʻlqini oʻz-oʻzidan paydo boʻlgan va orqaga harakatlangan
    (~20 km/soat atrofida).

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_30_36.py --author=prime
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
    # 16 — qor parchasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Qor parchasi: nega doim olti nur",
        "summary": (
            "Qor parchasi har doim olti nurli, chunki suv muzlaganda olti burchakli "
            "panjara hosil qiladi. Matematiklar esa undan cheksiz uzun chegarali "
            "shakl — Koch qor parchasini yasashgan."
        ),
        "order":   16,
        "grammar": [
            {
                "pattern":  "Koch qor parchasi: perimetr × 4/3 har qadamda",
                "meaning":  "Har bir kesma uch boʻlakka boʻlinadi va oʻrtasiga "
                            "kichik uchburchak qoʻyiladi: 3 boʻlak oʻrniga 4 boʻlak. "
                            "Shuning uchun chegara har qadamda 4/3 marta uzayadi va "
                            "cheksiz oʻsadi, yuza esa chegaralangan qoladi.",
                "examples": [
                    "1 qadam: × 1,33; 2 qadam: × 1,78; 3 qadam: × 2,37",
                    "10 qadam: perimetr ≈ 17,8 marta uzun, yuza esa 1,6 martadan oshmaydi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega qor parchasining nurlari doim oltita?",
                "choices": [
                    "Chunki bulutlar olti burchakli",
                    "Chunki suv muzlaganda molekulalar olti burchakli panjaraga "
                    "terilib qotadi",
                    "Chunki shamol olti tomondan esadi",
                    "Bu tasodif, baʼzida beshta ham boʻladi",
                ],
                "answer": 1,
                "explanation": "Muzning ichki tuzilishi — olti burchakli panjara. "
                               "Kristal shu panjara boʻyicha oʻsadi, shuning uchun "
                               "oltita nur chiqadi.",
            },
            {
                "text": "Koch qor parchasining perimetri hozir 9 sm. Yana bir qadam "
                        "bajarilsa, perimetr qancha boʻladi?",
                "choices": ["12 sm", "18 sm", "16 sm", "13 sm"],
                "answer": 0,
                "explanation": "Har qadamda perimetr 4/3 marta oshadi: 9 × 4/3 = 12 sm.",
            },
            {
                "text": "Nega bir qor parchasining oltita nuri bir-biriga oʻxshash "
                        "boʻladi?",
                "choices": [
                    "Ularni bitta usta yasaydi",
                    "Ular doim bir xil kattalikda tugʻiladi",
                    "Oltita nur bir vaqtda, bir xil havo sharoitida oʻsadi",
                    "Muz oʻzini oʻzi koʻzguda koʻradi",
                ],
                "answer": 2,
                "explanation": "Parcha juda kichik, shuning uchun uning har bir "
                               "nuri bir xil harorat va namlikni «his qiladi» va "
                               "bir xil shoxlanadi.",
            },
        ],
        "body": """
<p>Qishda yengingizga tushgan bitta qor parchasiga qarang. Uning nechta nuri bor?
Oltita. Keyingisida ham oltita. Hech qachon beshta yoki sakkizta emas. Nega?</p>

<p>Bu savolni 1611-yilda nemis <span class="cn-word" data-tr="osmon jismlarini oʻrganuvchi olim">astronom</span>i <b>Iogann Kepler</b> (Johannes Kepler)
alohida kichik kitobda bergan. U javobni topa olmagan, chunki u davrda hech kim
<span class="cn-word" data-tr="moddaning eng kichik zarrasi">molekula</span>ni
bilmasdi.</p>

<p>Bugun javob maʼlum. Suv muzlaganda uning molekulalari tartibsiz qolmaydi:
ular asalari uyiga oʻxshash olti burchakli
<span class="cn-word" data-tr="takrorlanib turuvchi toʻr shaklidagi tuzilish">panjara</span>ga
terilib qotadi. Qor parchasi — shu panjaradan oʻsgan
<span class="cn-word" data-tr="toʻgʻri qirrali, tartibli tuzilgan qattiq jism">kristal</span>.
Shuning uchun u olti tomonga oʻsadi.</p>

<p>Ikkinchi sir: nega oltita nur bir-biriga shunchalik oʻxshaydi? Chunki parcha
juda kichik. Bulutdan tushayotganda uning oltita nuri bir vaqtning oʻzida bir xil
<span class="cn-word" data-tr="havoning iliq yoki sovuqlik darajasi">harorat</span>
va <span class="cn-word" data-tr="havodagi suv bugʻi miqdori">namlik</span>dan
oʻtadi va bir xil shoxlanadi.</p>

<p>Amerikalik dehqon <b>Uilson Bentli</b> (Wilson Bentley) 1885-yilda birinchi marta
qor parchasini suratga oldi. Umri davomida u 5000 dan ortiq parchani suratga
tushirdi va ikkita bir xilini topmadi.</p>

<p>Matematiklar esa oʻz qor parchasini oʻylab topishdi. 1904-yilda shved matematigi
<b>Xelge fon Kox</b> (Helge von Koch) teng tomonli uchburchakdan boshladi. Har bir
tomonni uch <span class="cn-word" data-tr="butunning bir qismi">boʻlak</span>ka boʻldi va oʻrtadagi boʻlak ustiga kichik uchburchak qurdi. Keyin
yangi tomonlarning har biri bilan xuddi shunday qildi — va bu cheksiz davom etadi.</p>

<p>Natija hayratlanarli. Har qadamda 3 boʻlak oʻrniga 4 boʻlak paydo boʻladi, demak
<span class="cn-word" data-tr="shaklning chegarasi uzunligi">perimetr</span>
<strong>4/3</strong> marta uzayadi. 10 qadamdan keyin u taxminan
<strong>18</strong> marta uzun. Cheksiz qadamdan keyin — cheksiz uzun. Yuzasi esa
dastlabki uchburchakning <strong>1,6</strong> marta kattasidan oshmaydi.</p>

<p>Qogʻozga sigʻadigan, lekin chegarasi cheksiz uzun shakl. Bunday shakllar
<span class="cn-word" data-tr="har qancha kattalashtirsa ham oʻziga oʻxshash boʻlib qoladigan shakl">fraktal</span>
deyiladi. Tabiatda ular hamma joyda: qirgʻoq chizigʻi, bulut, shoxlar — va
yengingizdagi qor parchasi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 18 — chigʻanoqdagi spiral
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Chigʻanoqdagi spiral: oʻsadi, lekin oʻzgarmaydi",
        "summary": (
            "Chigʻanoq shaklini buzmasdan qanday kattalashadi? Javob — logarifmik "
            "spiral. Shuningdek, «nautilus oltin nisbatda» degan mashhur gap "
            "nega notoʻgʻri ekani haqida."
        ),
        "order":   18,
        "grammar": [
            {
                "pattern":  "Logarifmik spiral: har aylanishda bir xil marta",
                "meaning":  "Oddiy (Arximed) spiralda har aylanishda masofa bir xil "
                            "songa qoʻshiladi. Logarifmik spiralda esa bir xil songa "
                            "koʻpayadi. Shuning uchun uning har bir oʻrami oldingisining "
                            "kattalashtirilgan nusxasi.",
                "examples": [
                    "Arximed: 1, 2, 3, 4, 5 — har gal + 1",
                    "Logarifmik (× 3): 1, 3, 9, 27, 81 — har gal × 3",
                ],
            },
        ],
        "questions": [
            {
                "text": "Logarifmik spiralning asosiy xossasi qaysi?",
                "choices": [
                    "U doim aylanaga aylanadi",
                    "Uning hamma oʻramlari bir xil kattalikda",
                    "U faqat qogʻozda boʻladi",
                    "Kattalashganda ham shakli oʻzgarmaydi",
                ],
                "answer": 3,
                "explanation": "Har bir oʻram oldingisining aynan kattalashtirilgan "
                               "nusxasi. Shuning uchun chigʻanoq oʻssa ham, shakli "
                               "oʻsha-oʻsha qoladi.",
            },
            {
                "text": "Spiral har aylanishda 3 marta kengayadi. Markazdan masofa "
                        "2 sm boʻlsa, ikki aylanishdan keyin qancha boʻladi?",
                "choices": ["8 sm", "18 sm", "12 sm", "6 sm"],
                "answer": 1,
                "explanation": "2 × 3 = 6, keyin 6 × 3 = 18 sm. Qoʻshilmaydi, "
                               "koʻpayadi.",
            },
            {
                "text": "Bernullining qabr toshida nima xato chiqqan?",
                "choices": [
                    "Usta logarifmik emas, oddiy Arximed spiralini oʻyib qoʻygan",
                    "Uning ismi notoʻgʻri yozilgan",
                    "Tosh teskari qoʻyilgan",
                    "Toshga aylana chizilgan",
                ],
                "answer": 0,
                "explanation": "Bernulli logarifmik spiralni xohlagan edi, lekin "
                               "usta oʻramlari teng masofali Arximed spiralini "
                               "oʻyib qoʻygan.",
            },
        ],
        "body": """
<p>Dengiz qirgʻogʻidan bitta <span class="cn-word" data-tr="ichida yumshoq jonivor yashaydigan qattiq qobiq">chigʻanoq</span>
olib, uning ichiga qarang. Kichkina markazdan boshlangan
<span class="cn-word" data-tr="markaz atrofida aylanib, undan uzoqlashib boruvchi chiziq">spiral</span>
aylanib-aylanib kengayib boradi. Bu chiroyli egri chiziq bitta muammoni hal qiladi:
qanday qilib <b>oʻsish</b>, lekin <b>shaklni oʻzgartirmaslik</b> kerak?</p>

<p>Chigʻanoq ichidagi jonivor oʻsadi va unga kattaroq uy kerak boʻladi. U eski uyini
tashlab ketmaydi — uning chetiga yangi qism qoʻshadi. Agar har safar yangi qism
eskisidan bir xil <b>marta</b> katta boʻlsa, butun chigʻanoq oʻzining kattalashgan
nusxasiga aylanadi.</p>

<p>Bunday spiral <span class="cn-word" data-tr="har aylanishda bir xil marta kengayadigan spiral">logarifmik spiral</span>
deyiladi. Uning sirri — <span class="cn-word" data-tr="bir songa qayta-qayta koʻpaytirish">koʻpaytirish</span>da.
Aytaylik, spiral har aylanishda 3 marta kengayadi. Markazdan masofa: 1, 3, 9, 27…
Oddiy, <b>Arximed spiral</b>ida esa har gal bir xil son qoʻshiladi: 1, 2, 3, 4…
Uning oʻramlari bir xil oraliqda, xuddi magnitofon tasmasi kabi.</p>

<p>Shveysariyalik matematik <b>Yakob Bernulli</b> (Jakob Bernoulli) logarifmik
spiralni shunchalik sevganki, uni <i>«ajoyib spiral»</i> deb atagan. U qabr
toshiga shu spiral va <i>«Oʻzgarib, yana oʻsha boʻlib tirilaman»</i> degan soʻzlar
oʻyilishini vasiyat qilgan. Hikoya qilinishicha, usta matematikani yaxshi
bilmagani uchun toshga oddiy Arximed spiralini oʻyib qoʻygan. Bu tosh bugun ham
Bazel soborida turibdi.</p>

<p>Bu spiralni boshqa joylarda ham koʻrasiz:
<span class="cn-word" data-tr="kuchli aylanma shamol, boʻron">dovul</span>ning
bulut qoʻllarida, ayrim <span class="cn-word" data-tr="milliardlab yulduzlar toʻplami">galaktika</span>larning
qoʻllarida.</p>

<p>Endi bitta mashhur <span class="cn-word" data-tr="koʻp takrorlanadigan, lekin notoʻgʻri fikr">afsona</span>.
Koʻp kitob va videolarda <b>nautilus</b> chigʻanogʻi «oltin nisbatga» boʻysunadi
deyiladi. Bu notoʻgʻri. «Oltin spiral» har aylanishda taxminan
<strong>6,85</strong> marta kengayishi kerak edi. Haqiqiy nautiluslarni
<span class="cn-word" data-tr="aniq kattalikni topish">oʻlcha</span>ganda bu son ancha
kichik chiqqan — 3 atrofida.</p>

<p>Bu ham matematikaning bir saboqi: chiroyli gapga ishonishdan oldin, oʻlchab
koʻring.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 19 — daraxt shoxlari
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Leonardo da Vinchi va daraxt shoxlari qoidasi",
        "summary": (
            "Leonardo da Vinchi daraxt tanasi qalinligi va shoxlari orasida "
            "qoida borligini payqagan. Bu qoida Pifagor teoremasiga juda "
            "oʻxshaydi."
        ),
        "order":   19,
        "grammar": [
            {
                "pattern":  "Shoxlar qoidasi: D² = d₁² + d₂²",
                "meaning":  "Kesimning yuzasi diametr kvadratiga bogʻliq. Shuning "
                            "uchun tana ikkiga boʻlinganda shoxlar diametrlari "
                            "kvadratlarining yigʻindisi tana diametrining kvadratiga "
                            "teng boʻladi.",
                "examples": [
                    "Tana 10 sm → shoxlar 6 sm va 8 sm: 36 + 64 = 100",
                    "Tana 20 sm, ikki teng shox: har biri ≈ 14,1 sm (200 + 200 = 400)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Leonardo qoidasiga koʻra, nima saqlanadi?",
                "choices": [
                    "Shoxlar soni",
                    "Shoxlarning uzunligi",
                    "Shoxlar kesimlari yuzalarining yigʻindisi",
                    "Barglar soni",
                ],
                "answer": 2,
                "explanation": "Tana boʻlinganda shoxlar kesimlarining umumiy yuzasi "
                               "tananing kesimiga teng boʻlib qoladi.",
            },
            {
                "text": "Tananing diametri 15 sm. U ikki shoxga boʻlindi, bittasi "
                        "9 sm. Ikkinchi shox diametri qancha?",
                "choices": ["6 sm", "12 sm", "24 sm", "10 sm"],
                "answer": 1,
                "explanation": "15² = 225, 9² = 81, 225 − 81 = 144, √144 = 12 sm. "
                               "Xuddi 9, 12, 15 uchburchagi kabi.",
            },
            {
                "text": "Nega ikki teng shox tanadan yarim marta ingichka boʻlmaydi?",
                "choices": [
                    "Chunki diametrni emas, yuzani teng boʻlish kerak, yuza esa "
                    "diametr kvadratiga bogʻliq",
                    "Chunki shoxlar keyin yoʻgʻonlashadi",
                    "Chunki daraxt bunga eʼtibor bermaydi",
                    "Chunki shoxlar doim tana bilan teng",
                ],
                "answer": 0,
                "explanation": "Yuza yarimga boʻlinadi, diametr esa √2 ≈ 1,41 marta "
                               "kichrayadi: 20 sm → 14,1 sm, 10 sm emas.",
            },
        ],
        "body": """
<p>Taxminan besh yuz yil oldin <b>Leonardo da Vinchi</b> oʻz
<span class="cn-word" data-tr="shaxsiy yozuvlar uchun kitobcha">kundalik</span>
daftarlarida daraxtlarni chizib, bir qiziq narsani yozib qoldirgan. Uning soʻzlariga
koʻra, daraxtning har bir qavatidagi barcha shoxlar birga olinsa, ular tananing
yoʻgʻonligiga teng boʻladi.</p>

<p>Bu nimani anglatadi? Daraxt tanasini arra bilan koʻndalang kesib koʻring — doira
chiqadi. Bu <span class="cn-word" data-tr="jismni kesganda hosil boʻlgan yuza">kesim</span>.
Endi tana ikki shoxga ajralgan joydan yuqorida ikkala shoxni ham kesing. Leonardo
qoidasi aytadi: ikki kichik doiraning <span class="cn-word" data-tr="shaklning ichki maydoni">yuza</span>lari
yigʻindisi katta doiraning yuzasiga teng.</p>

<p>Bu yerda bitta tuzoq bor. Tana ikki teng shoxga boʻlinsa, har bir shox tanadan
<b>yarim marta</b> ingichka boʻladimi? Yoʻq! Doiraning yuzasi uning
<span class="cn-word" data-tr="doira markazidan oʻtib, ikki chetini tutashtiruvchi kesma">diametr</span>i
<span class="cn-word" data-tr="sonni oʻziga koʻpaytirish">kvadrat</span>iga bogʻliq.
Yuzani yarimga boʻlish uchun diametrni taxminan <strong>1,41</strong> ga boʻlish
yetarli. 20 sm li tana ikki teng shoxga boʻlinsa, har biri taxminan
<strong>14,1 sm</strong> boʻladi.</p>

<p>Shuning uchun qoidani shunday yozish mumkin: tana diametrining kvadrati shoxlar
diametrlari kvadratlarining yigʻindisiga teng. Tanish tuyuldimi? Bu xuddi
<b>Pifagor teoremasi</b>! 10 sm li tana 6 sm va 8 sm li shoxlarga boʻlinishi mumkin:
36 + 64 = 100.</p>

<p>Olimlar bu qoidani haqiqiy daraxtlarda
<span class="cn-word" data-tr="toʻgʻriligini tekshirib koʻrmoq">sinab koʻr</span>ishdi
— koʻp daraxtlarda u ancha yaxshi bajariladi. Nega shunday ekani haqida bahslar
hali ham davom etadi. Fikrlardan biri: bunday shoxlanish daraxtni
<span class="cn-word" data-tr="kuchli shamol">boʻron</span>da sinishdan saqlaydi.</p>

<p>Shoxlanishning yana bir sirli tomoni bor. Kichik shoxni olib qarang: u oʻzi ham
kichkina daraxtga oʻxshaydi. Undagi yanada kichik shox — yanada kichik daraxt. Bunday
<span class="cn-word" data-tr="qismi butunga oʻxshash boʻlish xossasi">oʻz-oʻziga oʻxshashlik</span>
daryolar tarmogʻida, oʻpkadagi havo yoʻllarida va qon tomirlarida ham uchraydi.</p>

<p>Leonardo rassom edi, lekin u chizishdan oldin oʻlchar edi. Balki shuning uchun
uning daraxtlari bunchalik tirik koʻrinadi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 21 — zebra chiziqlari
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Zebra chiziqlari va Alan Tyuringning soʻnggi gʻoyasi",
        "summary": (
            "Kompyuter fanining otasi Alan Tyuring umrining oxirida hayvonlar "
            "terisidagi dogʻ va chiziqlarni tushuntiradigan matematika yaratgan."
        ),
        "order":   21,
        "grammar": [
            {
                "pattern":  "Tyuring naqshi: yaqinda yoq, uzoqda oʻchir",
                "meaning":  "Ikki modda tarqaladi. Birinchisi rangni «yoqadi» va "
                            "sekin tarqaladi; ikkinchisi rangni «oʻchiradi» va tez, "
                            "uzoqqa tarqaladi. Natijada rangli dogʻ atrofida rangsiz "
                            "halqa paydo boʻladi — va naqsh oʻz-oʻzidan tugʻiladi.",
                "examples": [
                    "Keng tana → dogʻlar yoki chiziqlar",
                    "Ingichka dum → faqat koʻndalang halqalar (chiziqlar)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Tyuring gʻoyasida ikkinchi modda — «oʻchiruvchi» — "
                        "qanday tarqaladi?",
                "choices": [
                    "Umuman tarqalmaydi",
                    "Birinchisidan sekinroq",
                    "Faqat dumda",
                    "Birinchisidan tezroq va uzoqroqqa",
                ],
                "answer": 3,
                "explanation": "Oʻchiruvchi uzoqqa yetib borgani uchun har bir "
                               "rangli dogʻ atrofida bir halqa boʻsh qoladi. Shu "
                               "naqshni tugʻdiradi.",
            },
            {
                "text": "Myurrey qoidasiga koʻra, qaysi hayvon boʻlishi mumkin "
                        "EMAS?",
                "choices": [
                    "Dogʻli tana va yoʻl-yoʻl dum",
                    "Yoʻl-yoʻl tana va dogʻli dum",
                    "Yoʻl-yoʻl tana va yoʻl-yoʻl dum",
                    "Dogʻli tana va dogʻli dum",
                ],
                "answer": 1,
                "explanation": "Ingichka dumda dogʻ uchun joy yetmaydi — u yerda "
                               "faqat koʻndalang halqalar chiqadi. Shuning uchun "
                               "yoʻl-yoʻl hayvonning dumi dogʻli boʻlmaydi.",
            },
            {
                "text": "Tyuring bu ishini qaysi yili chop etgan?",
                "choices": ["1912", "1936", "1952", "1985"],
                "answer": 2,
                "explanation": "«Morfogenezning kimyoviy asoslari» maqolasi "
                               "1952-yilda chiqqan, Tyuring vafotidan ikki yil oldin.",
            },
        ],
        "body": """
<p>Zebraning chiziqlari, leopardning dogʻlari, baliq terisidagi naqshlar — bularni
kim «chizadi»? Hayvon embrion boʻlganida uning terisida hech qanday chizma yoʻq.
Hujayralar naqshni qayerdan biladi?</p>

<p>Bu savolga <b>Alan Tyuring</b> (Alan Turing) javob topmoqchi boʻldi. Hayvon hali <span class="cn-word" data-tr="tirik organizmning eng kichik qurilish birligi">hujayra</span>lar toʻdasi boʻlgan paytda, naqsh qayerdan keladi? Biz uni
<span class="cn-word" data-tr="hisoblash mashinasi, kompyuter">kompyuter</span>
gʻoyasining otasi va Ikkinchi jahon urushida nemis
<span class="cn-word" data-tr="maxfiy yozuv">shifr</span>ini ochishga yordam bergan
olim sifatida bilamiz. 1952-yilda esa u butunlay boshqa mavzuda maqola chop etdi:
tirik mavjudotlarda <span class="cn-word" data-tr="shakl va naqshning paydo boʻlishi">shakl hosil boʻlish</span>i
haqida.</p>

<p>Tyuringning gʻoyasi ikkita
<span class="cn-word" data-tr="kimyoviy tarkibga ega narsa">modda</span> haqida. Birinchisi
— <b>yoquvchi</b>: u qayerda boʻlsa, teri qorayadi va u oʻzidan yana koʻproq hosil
qiladi. Ikkinchisi — <b>oʻchiruvchi</b>: u birinchisini toʻxtatadi. Eng muhimi:
oʻchiruvchi tezroq va uzoqroqqa
<span class="cn-word" data-tr="yoyilib, kengayib bormoq">tarqal</span>adi.</p>

<p>Endi tasavvur qiling: terining bir joyida tasodifan yoquvchi biroz koʻpayib
qoldi. U oʻsha joyni qoraytiradi. Lekin oʻchiruvchi undan tezroq qochib, atrofdagi
halqani «oʻchirib» qoʻyadi. Natijada qora dogʻ va uning atrofida oq hoshiya paydo
boʻladi. Keyingi dogʻ faqat shu hoshiyadan narida tugʻiladi. Hech kim chizmagan
<span class="cn-word" data-tr="takrorlanuvchi bezak, chizma">naqsh</span>
oʻz-oʻzidan paydo boʻladi.</p>

<p>Moddalar tezligi va teri shakliga qarab, natija dogʻ ham, chiziq ham boʻlishi
mumkin. Matematik <b>Jeyms Myurrey</b> (James Murray) bundan qiziq xulosa chiqardi:
ingichka dumda dogʻ uchun joy yetmaydi, u yerda faqat koʻndalang halqalar chiqadi.
Shuning uchun dogʻli hayvonning dumi yoʻl-yoʻl boʻlishi mumkin — gepardni eslang. Lekin
yoʻl-yoʻl hayvonning dumi dogʻli boʻlmaydi.</p>

<p>Tyuring bu ishning davomini koʻra olmadi: u 1954-yilda vafot etdi. Oʻnlab yillar
oʻtib, biologlar uning mexanizmini baliqlar terisida va hatto sichqon
<span class="cn-word" data-tr="embrion — rivojlanayotgan homila">embrion</span>ining
barmoqlari shakllanishida kuzatishdi.</p>

<p>Bitta formula — va zebradan leopardgacha butun bir hayvonot bogʻi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 22 — samolyot nega egri uchadi
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Samolyot nega xaritada egri uchadi",
        "summary": (
            "Yassi xaritada egri koʻringan yoʻl aslida yer sharidagi eng qisqa yoʻl. "
            "Toshkentdan Nyu-Yorkka shimol orqali uchish 1800 km dan koʻproq "
            "qisqa."
        ),
        "order":   22,
        "grammar": [
            {
                "pattern":  "Shardagi eng qisqa yoʻl — katta doira",
                "meaning":  "Shar sirtida ikki nuqta orasidagi eng qisqa yoʻl "
                            "markazi shar markazida boʻlgan aylanadan oʻtadi. Yassi "
                            "xaritada bu yoʻl egri boʻlib, qutbga qarab "
                            "bukilganday koʻrinadi.",
                "examples": [
                    "Toshkent → Nyu-York, 41-parallel boʻylab: ≈ 12 020 km",
                    "Toshkent → Nyu-York, katta doira boʻylab: ≈ 10 170 km",
                ],
            },
        ],
        "questions": [
            {
                "text": "Toshkentdan Nyu-Yorkka katta doira boʻylab uchish "
                        "parallel boʻylab uchishdan taxminan necha km qisqa?",
                "choices": ["Taxminan 185 km", "Taxminan 1850 km",
                            "Taxminan 10 170 km", "Taxminan 22 190 km"],
                "answer": 1,
                "explanation": "12 020 − 10 170 = 1850 km. Bu Toshkentdan "
                               "Moskvagacha boʻlgan masofaning yarmidan koʻp.",
            },
            {
                "text": "Nega Merkator xaritasida Grenlandiya juda katta koʻrinadi?",
                "choices": [
                    "Chunki u haqiqatan ham Afrikadan katta",
                    "Chunki xaritani chizgan odam xato qilgan",
                    "Chunki bu xarita qutblarga yaqin joylarni choʻzib koʻrsatadi",
                    "Chunki Grenlandiya muz bilan oʻsadi",
                ],
                "answer": 2,
                "explanation": "Shar sirtini tekislikka yoyish uchun Merkator "
                               "qutbga yaqin joylarni choʻzgan. Afrika aslida "
                               "Grenlandiyadan taxminan 14 marta katta.",
            },
            {
                "text": "Nima uchun shar sirtini buzmasdan yassi xaritaga tushirib "
                        "boʻlmaydi?",
                "choices": [
                    "Apelsin poʻstini yirtmasdan yoki choʻzmasdan stolga tekis "
                    "yoyib boʻlmaganidek, shar sirti tekislikka mos kelmaydi",
                    "Chunki yer sharining oʻlchamlari nomaʼlum",
                    "Chunki qogʻoz yetmaydi",
                    "Aslida boʻladi, faqat qimmat",
                ],
                "answer": 0,
                "explanation": "Har qanday yassi xarita nimanidir buzadi: masofani, "
                               "yuzani yoki shaklni. Bu matematik jihatdan isbotlangan.",
            },
        ],
        "body": """
<p>Samolyotda uchayotganingizda ekrandagi xaritaga qarang. Toshkentdan Nyu-Yorkka
yoʻl toʻgʻri chiziq emas — u shimolga qarab katta yoy chizadi, deyarli
Skandinaviya ustidan oʻtadi. Uchuvchi adashdimi? Yoʻq. Aslida xarita adashtiryapti.</p>

<p>Toshkent va Nyu-York deyarli bir xil
<span class="cn-word" data-tr="ekvatordan shimol yoki janubga uzoqlik">kenglik</span>da
joylashgan — taxminan 41° shimolda. Yassi xaritada eng qisqa yoʻl shu
<span class="cn-word" data-tr="ekvatorga parallel boʻlgan xayoliy aylana">parallel</span>
boʻylab toʻgʻri chiziqdek koʻrinadi. Uning uzunligi taxminan
<strong>12 020 km</strong>.</p>

<p>Lekin Yer — tekis qogʻoz emas, <span class="cn-word" data-tr="dumaloq jism, koptok">shar</span>.
Shar sirtidagi eng qisqa yoʻl <span class="cn-word" data-tr="markazi shar markazida boʻlgan eng katta aylana">katta doira</span>dan
oʻtadi — markazi Yer markazida boʻlgan aylanadan. Toshkent va Nyu-York orqali oʻtgan
katta doira shimolga, taxminan 70° kenglikkacha koʻtariladi. Bu yoʻl atigi
<strong>10 170 km</strong>. Farq — <strong>1850 km</strong>dan koʻproq, bir necha
soatlik parvoz va tonnalab <span class="cn-word" data-tr="dvigatelda yonadigan modda">yoqilgʻi</span>.</p>

<p>Buni uyda sinab koʻrish mumkin. <span class="cn-word" data-tr="Yer sharining kichik dumaloq nusxasi">Globus</span> va ip oling. Ipni ikki shahar orasida
taranglab torting — u oʻzi eng qisqa yoʻlni topadi va shimolga qarab bukiladi.</p>

<p>Unda nega xaritalar bizni aldaydi? Chunki shar sirtini yassi qogʻozga buzmasdan
tushirib boʻlmaydi. Apelsin poʻstini yirtmasdan va choʻzmasdan stolga tekis yoyib
koʻring — iloji yoʻq. Har bir xarita nimadir
<span class="cn-word" data-tr="asl holini oʻzgartirib koʻrsatmoq">buz</span>adi:
masofani, yuzani yoki shaklni.</p>

<p>Eng mashhur <span class="cn-word" data-tr="shar sirtini tekislikka tushirish usuli">proyeksiya</span>ni
1569-yilda flamand kartografi <b>Gerard Merkator</b> (Gerardus Mercator) yaratgan.
U <span class="cn-word" data-tr="dengizda kema haydovchi">dengizchi</span>lar uchun
qulay edi: unda <span class="cn-word" data-tr="shimolni koʻrsatuvchi asbob">kompas</span> yoʻnalishi toʻgʻri chiziq boʻlib chiqadi. Ammo u qutblarga
yaqin joylarni kuchli choʻzadi. Shuning uchun Grenlandiya unda Afrika bilan deyarli
teng koʻrinadi. Aslida Afrika Grenlandiyadan taxminan <strong>14</strong> marta
katta.</p>

<p>Demak, xarita — bu haqiqatning bir tomoni. Qaysi tomoni ekanini bilish uchun esa
matematika kerak.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 28 — ovoz berish usullari
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bir xil ovozlar, uch xil gʻolib",
        "summary": (
            "15 oʻquvchi sinf sardorini saylaydi. Ovozlar bitta — lekin sanash "
            "usuliga qarab gʻolib uch xil chiqadi. Saylov matematikasi haqida."
        ),
        "order":   28,
        "grammar": [
            {
                "pattern":  "Uch usul — uch gʻolib",
                "meaning":  "Koʻpchilik usuli faqat birinchi tanlovni sanaydi. Ikki "
                            "turli usul eng zaifini chiqarib, qolganlarni qayta "
                            "sanaydi. Borda usuli har bir oʻrinni ball bilan "
                            "baholaydi (1-oʻrin 2 ball, 2-oʻrin 1 ball).",
                "examples": [
                    "6: Aziz > Dilnoza > Bekzod; 5: Bekzod > Dilnoza > Aziz; "
                    "4: Dilnoza > Bekzod > Aziz",
                    "Koʻpchilik → Aziz (6); ikki tur → Bekzod (9 : 6); "
                    "Borda → Dilnoza (19 ball)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Koʻpchilik usulida kim gʻolib boʻladi?",
                "choices": ["Aziz", "Bekzod", "Dilnoza", "Durrang"],
                "answer": 0,
                "explanation": "Faqat birinchi oʻrinlar sanaladi: Aziz 6, Bekzod 5, "
                               "Dilnoza 4.",
            },
            {
                "text": "Borda usulida Bekzod necha ball oladi? (1-oʻrin 2 ball, "
                        "2-oʻrin 1 ball, 3-oʻrin 0 ball)",
                "choices": ["10", "12", "19", "14"],
                "answer": 3,
                "explanation": "5 kishi uni birinchi qoʻygan: 5 × 2 = 10. 4 kishi "
                               "ikkinchi qoʻygan: 4 × 1 = 4. Jami 14 ball.",
            },
            {
                "text": "Dilnozani Aziz bilan yakkama-yakka solishtirsak, kim "
                        "yutadi?",
                "choices": [
                    "Aziz, 9 : 6",
                    "Dilnoza, 9 : 6",
                    "Durrang",
                    "Aziz, 10 : 5",
                ],
                "answer": 1,
                "explanation": "Bekzodni va Dilnozani birinchi qoʻygan 5 + 4 = 9 kishi "
                               "Dilnozani Azizdan yuqori qoʻygan; faqat 6 kishi aksincha.",
            },
        ],
        "body": """
<p>Sinfda <strong>15</strong> oʻquvchi sardor saylamoqda. Uchta
<span class="cn-word" data-tr="saylovda qatnashuvchi kishi">nomzod</span> bor: <b>Aziz</b>, <b>Bekzod</b> va <b>Dilnoza</b>. Har bir oʻquvchi qogʻozga uchala
nomzodni ham yoqtirish tartibida yozadi. Natija shunday:</p>

<p>6 kishi: Aziz, keyin Dilnoza, keyin Bekzod.<br>
5 kishi: Bekzod, keyin Dilnoza, keyin Aziz.<br>
4 kishi: Dilnoza, keyin Bekzod, keyin Aziz.</p>

<p>Kim yutdi? Javob <span class="cn-word" data-tr="ovozlarni hisoblash yoʻli">sanash usuli</span>ga
bogʻliq ekanini koʻramiz.</p>

<p><b>1-usul: koʻpchilik.</b> Faqat birinchi oʻrinni sanaymiz. Aziz 6, Bekzod 5,
Dilnoza 4. Gʻolib — <b>Aziz</b>. Koʻp mamlakatlarda <span class="cn-word" data-tr="rahbarni ovoz berib tanlash">saylov</span> aynan shunday oʻtadi.</p>

<p><b>2-usul: ikki tur.</b> Eng kam ovoz olgan Dilnoza chiqib ketadi. Uning 4
<span class="cn-word" data-tr="saylovda ovoz beruvchi kishi">saylovchi</span>si
ikkinchi tanlovi Bekzodga oʻtadi. Endi Bekzod 9, Aziz 6. Gʻolib — <b>Bekzod</b>.</p>

<p><b>3-usul: ball.</b> Birinchi oʻringa 2 ball, ikkinchiga 1 ball beramiz. Aziz:
6 × 2 = 12. Bekzod: 5 × 2 + 4 × 1 = 14. Dilnoza: hamma uni kamida ikkinchi qoʻygan,
6 + 5 + 4 × 2 = <strong>19</strong>. Gʻolib — <b>Dilnoza</b>. Bu usulni 1770-yilda
fransuz olimi <b>Jan-Sharl de Borda</b> taklif qilgan.</p>

<p>Bir xil qogʻozlar, uch xil <span class="cn-word" data-tr="musobaqada yutgan kishi">gʻolib</span>.
Qaysi biri adolatli? Yana bir sinov qilamiz: nomzodlarni juftlab solishtiramiz.
Dilnoza Azizdan 9 : 6 hisobida, Bekzoddan 10 : 5 hisobida
<span class="cn-word" data-tr="yuqori qoʻyilgan, afzal koʻrilgan">ustun</span>. U har
qanday yakkama-yakka bahsda yutadi — lekin koʻpchilik usulida oxirgi oʻrinda!</p>

<p>Bunday nomzodni birinchi boʻlib fransuz matematigi
<b>Kondorse</b> (Condorcet) 1785-yilda oʻrgangan. U yana bir gʻalati narsani topdi:
baʼzan juftlikda A Bdan, B Cdan, C esa Adan yutadi — xuddi «tosh, qaychi, qogʻoz»
kabi. Bu <span class="cn-word" data-tr="aqlga zid koʻrinadigan, lekin toʻgʻri natija">paradoks</span>
uning nomi bilan ataladi.</p>

<p>1951-yilda amerikalik iqtisodchi <b>Kennet Errou</b> (Kenneth Arrow) bundan ham
kuchli <span class="cn-word" data-tr="isbotlangan matematik qoida">teorema</span>ni isbotladi: uch va undan koʻp nomzod boʻlganda, bir necha oddiy
<span class="cn-word" data-tr="toʻgʻri va xolis boʻlish">adolat</span> talabining
hammasini birdaniga bajaradigan mukammal usul <b>mavjud emas</b>. Bu kashfiyot unga
1972-yilda Nobel mukofotini keltirdi.</p>

<p>Demak, saylovda faqat «kim koʻproq yoqadi» emas, «qanday
<span class="cn-word" data-tr="hisobga olmoq">hisob</span>lanadi» degan savol ham
gʻolibni hal qiladi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 29 — tirbandlik
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Sababsiz tirbandlik: yoʻldagi sirli toʻlqin",
        "summary": (
            "Haqiqiy tajriba: yaponiyalik olimlar 22 ta mashinani aylana yoʻlda "
            "bir xil tezlikda haydashni soʻrashdi. Hech qanday sababsiz tirbandlik "
            "paydo boʻldi va orqaga qarab yura boshladi."
        ),
        "order":   29,
        "grammar": [
            {
                "pattern":  "Toʻlqin — narsa emas, holat harakati",
                "meaning":  "Tirbandlikda mashinalar oldinga yuradi, lekin "
                            "«tiqilinch joy» orqaga suriladi. Har bir haydovchi "
                            "oldingisidan biroz kechroq va biroz kuchliroq tormoz "
                            "bersa, kichik sekinlashish kattalashib, orqaga tarqaladi.",
                "examples": [
                    "1-mashina 5 km/soat sekinlashdi → 2-si 7 km/soat → 3-si 10 km/soat …",
                    "Stadiondagi «toʻlqin»: odamlar joyida, toʻlqin esa aylanib yuradi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Yaponiyadagi tajribada tirbandlik nimadan paydo boʻldi?",
                "choices": [
                    "Yoʻldagi chuqurdan",
                    "Svetofordan",
                    "Haydovchilar tezligidagi kichik farqlar kattalashib ketganidan",
                    "Avariyadan",
                ],
                "answer": 2,
                "explanation": "Yoʻlda hech qanday toʻsiq yoʻq edi. Kimdir biroz "
                               "sekinlashdi, orqadagilar kuchliroq tormoz berdi va "
                               "tiqilinch oʻz-oʻzidan tugʻildi.",
            },
            {
                "text": "Har bir haydovchi oldingisidan 2 marta kuchliroq tormoz "
                        "beradi. Birinchisi 1 km/soat sekinlashsa, toʻrtinchisi "
                        "necha km/soat sekinlashadi?",
                "choices": ["4 km/soat", "8 km/soat", "6 km/soat", "16 km/soat"],
                "answer": 1,
                "explanation": "1 → 2 → 4 → 8. Toʻrtinchi mashina 8 km/soat "
                               "sekinlashadi — mana shu kuchayish toʻlqinni "
                               "tugʻdiradi.",
            },
            {
                "text": "Matnga koʻra, tirbandlikni kamaytirish uchun haydovchi "
                        "nima qilishi mumkin?",
                "choices": [
                    "Oldingi mashinaga yaqinroq yurishi",
                    "Bir tekis tezlikda yurib, yetarli masofa saqlashi",
                    "Tez-tez qator almashtirishi",
                    "Signal chalishi",
                ],
                "answer": 1,
                "explanation": "Masofa boʻlsa, oldingi mashina sekinlashganda keskin "
                               "tormoz berish shart emas — toʻlqin «yutib» yuboriladi.",
            },
        ],
        "body": """
<p>Siz katta yoʻldasiz. Mashinalar birdan sekinlashadi, keyin toʻxtaydi. Oʻn daqiqa
asta-sekin oldinga siljiysiz. Keyin yoʻl birdan ochiladi — va hech narsa yoʻq:
<span class="cn-word" data-tr="yoʻl-transport hodisasi">avariya</span> ham,
taʼmirlash ham, svetofor ham. Unda tirbandlik nimadan edi?</p>

<p>2008-yilda yaponiyalik olimlar bu savolga tajriba bilan javob berishdi. Ular
<strong>230 metr</strong> uzunlikdagi aylana
<span class="cn-word" data-tr="yopiq, aylanma yoʻl">trassa</span>ga
<strong>22</strong> ta mashina qoʻyib, haydovchilarga oddiy topshiriq berishdi: «Bir xil
<span class="cn-word" data-tr="harakat jadalligi">tezlik</span>da, oldingi mashinadan
bir xil masofada yuring».</p>

<p>Avvaliga hammasi joyida edi. Lekin bir necha daqiqadan keyin bitta haydovchi
biroz sekinlashdi — atigi bir oz. Orqasidagi haydovchi buni kechroq sezdi va
kuchliroq <span class="cn-word" data-tr="mashinani sekinlatuvchi qism">tormoz</span>
berdi. Uning orqasidagisi yanada kuchliroq. Bir necha mashinadan keyin kimdir
butunlay toʻxtab qoldi.</p>

<p>Shunday qilib, hech qanday sababsiz <span class="cn-word" data-tr="mashinalar tiqilib qolishi">tirbandlik</span>
paydo boʻldi. Eng qizigʻi — u bir joyda turmadi. Mashinalar oldinga yurardi, lekin
tiqilinch joy <b>orqaga</b> qarab, taxminan soatiga 20 km tezlikda siljib bordi.</p>

<p>Bu <span class="cn-word" data-tr="bir joydan ikkinchisiga uzatiladigan harakat">toʻlqin</span>.
Stadiondagi «toʻlqin»ni eslang: odamlar joyidan qimirlamaydi, faqat turib-oʻtiradi,
toʻlqin esa butun stadionni aylanib chiqadi. Yoʻlda ham shunday: mashinalar
almashadi, toʻlqin qoladi.</p>

<p>Matematiklar buni <span class="cn-word" data-tr="oʻz-oʻzidan kuchayadigan, barqaror boʻlmagan holat">beqarorlik</span>
deyishadi. Har bir haydovchi oldingisidan biroz kuchliroq tormoz bersa, kichik
sekinlashish zanjir boʻylab <span class="cn-word" data-tr="kattalashib bormoq">kuchay</span>adi.
Agar har biri 2 marta kuchliroq tormoz bersa: 1, 2, 4, 8… Toʻrtinchi mashinaning
oʻzi allaqachon keskin toʻxtaydi.</p>

<p>Bundan amaliy saboq chiqadi. Oldingi mashinaga yopishib yurmang. Yetarli
masofa saqlasangiz, oldingi mashina sekinlashganda siz keskin tormoz bermay, ozgina
gazni qoʻyib yuborasiz. Toʻlqin sizda toʻxtaydi — va orqangizdagi yuzlab haydovchi buni
hech qachon bilmaydi.</p>
""",
    },
]
