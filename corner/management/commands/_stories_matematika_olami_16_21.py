# -*- coding: utf-8 -*-
"""Matematika olami — 20, 24, 36, 37, 38 va 41-matnlar.

Toc: corner/management/commands/toc_matematika_olami.txt
  20. Nega katta hayvon sekin nafas oladi — oʻlcham matematikasi (tabiat)
  24. GPS uchta masofadan joyni qanday topadi                      (kundalik)
  36. Monti Xoll: eshikni almashtirasizmi?                          (jumboq)
  37. Tugʻilgan kun paradoksi: 23 kishi yetarli                     (jumboq)
  38. Hilbert mehmonxonasi: cheksiz xona, yana bitta mehmon         (jumboq)
  41. Bir varaq qogʻozni qirq marta buklasa nima boʻladi            (jumboq)
⛔ AUDIO YOʻQ.

FAKTLAR (tekshirilgan, raqamlar scratchpad skripti bilan qayta hisoblangan):
  • Kub: 1 sm → sirt 6, hajm 1; 2 sm → 24 va 8 (nisbat 3); 10 sm → 600 va 1000.
    Galiley kuch/ogʻirlik masalasini 1638-yilgi «Ikki yangi fan» kitobida yozgan.
    Sichqon yuragi daqiqasiga ~500 marta, fil yuragi ~30 marta uradi.
  • GPS: yoʻldoshlar ~20 200 km balandlikda, signal ~0,067 s yoʻl yuradi;
    1 mikrosekund xato = 300 m. Nisbiylik tufayli yoʻldosh soatlari kuniga
    ~38 mikrosekund oldinga ketadi → tuzatilmasa kuniga ~11 km xato.
  • Monti Xoll: almashtirsa 2/3 (100 000 marta simulyatsiya: 0,667).
    1990-yil, Merilin vos Savant, «Parade» jurnali; ~10 000 xat, ~1000 tasi
    ilmiy darajali odamlardan. Erdyosh haqidagi gap — «aytishlaricha».
  • Tugʻilgan kun: 23 kishi → 50,7 %; 30 → 70,6 %; 70 → 99,9 %.
    23 kishida 23 × 22 ÷ 2 = 253 juftlik. «Mening» tugʻilgan kunimni
    50 % ehtimol bilan kimdir baham koʻrishi uchun 253 kishi kerak.
  • Hilbert: g'oya David Hilbertning 1924-yilgi maʼruzasidan.
  • Qogʻoz 0,1 mm: 7 bukish → 128 qavat, 1,28 sm; 10 → 1024 qavat ~10 sm;
    14 → 1,6 m; 20 → ~105 m; 27 → ~13,4 km; 30 → ~107 km; 42 → ~440 000 km
    (Oy 384 400 km). Britni Gallivan 2002-yilda 12 marta buklagan.

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_16_21.py --author=prime
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
    # 20 — oʻlcham matematikasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Nega sichqonning yuragi tez, filniki sekin uradi",
        "summary": (
            "Kichik hayvon tez nafas oladi, katta hayvon sekin — sababi biologiyada "
            "emas, oddiy kubning sirti va hajmida."
        ),
        "order":   20,
        "grammar": [
            {
                "pattern":  "Sirt kvadrat bilan, hajm kub bilan oʻsadi",
                "meaning":  "Narsa har tomondan 2 marta kattalashsa, uning sirti "
                            "2 × 2 = 4 marta, hajmi esa 2 × 2 × 2 = 8 marta oshadi. "
                            "Shuning uchun katta jismning har bir grammiga kamroq "
                            "sirt toʻgʻri keladi.",
                "examples": [
                    "1 sm kub: sirt 6 sm², hajm 1 sm³ → har 1 sm³ ga 6 sm² teri",
                    "10 sm kub: sirt 600 sm², hajm 1000 sm³ → har 1 sm³ ga 0,6 sm²",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega sichqon tez-tez ovqatlanishi va tez nafas olishi kerak?",
                "choices": [
                    "Uning tanasiga nisbatan terisi koʻp, shuning uchun issiqlikni "
                    "tez yoʻqotadi",
                    "Uning suyaklari ogʻir",
                    "U doim yugurib yuradi",
                    "Uning yuragi katta",
                ],
                "answer": 0,
                "explanation": "Issiqlik teri orqali chiqib ketadi. Kichik hayvonning "
                               "har bir grammiga koʻp teri toʻgʻri keladi — u "
                               "issiqlikni tez yoʻqotadi va uni tez-tez tiklashi kerak.",
            },
            {
                "text": "Qirrasi 2 sm boʻlgan kubning sirti 24 sm², hajmi 8 sm³. Har "
                        "1 sm³ hajmga necha sm² sirt toʻgʻri keladi?",
                "choices": ["2 sm²", "6 sm²", "3 sm²", "8 sm²"],
                "answer": 2,
                "explanation": "24 ÷ 8 = 3. Kichik kubda bu son 6 edi, kattasida 3 ga "
                               "tushdi — jism kattalashgani sari nisbat kamayadi.",
            },
            {
                "text": "Odam 2 marta kattalashsa, suyaklari 4 marta kuchli, ogʻirligi "
                        "esa necha marta oshadi?",
                "choices": ["2 marta", "4 marta", "6 marta", "8 marta"],
                "answer": 3,
                "explanation": "Ogʻirlik hajmga bogʻliq: 2 × 2 × 2 = 8. Kuch faqat 4 "
                               "marta oshgani uchun gigant oʻz ogʻirligini koʻtara "
                               "olmaydi.",
            },
        ],
        "body": """
<p>Sichqonning yuragi daqiqasiga taxminan <strong>500</strong> marta uradi. Filning
yuragi esa — atigi <strong>30</strong> marta. Sichqon daqiqasiga yuz martadan ortiq
nafas oladi, fil esa bir necha marta. Nega? Javob biologiya kitobida emas, oddiy
<span class="cn-word" data-tr="olti teng kvadrat yoqli jism">kub</span>ning ichida.</p>

<p>Qirrasi 1 santimetr boʻlgan kichik kubni olaylik. Uning oltita yogʻi bor, demak
<span class="cn-word" data-tr="jismni tashqaridan oʻrab turgan yuza">sirt</span>i
<strong>6 sm²</strong>. <span class="cn-word" data-tr="jism egallagan joy kattaligi">Hajm</span>i
esa <strong>1 sm³</strong>.</p>

<p>Endi qirrasi 10 santimetr boʻlgan katta kubni olamiz. Sirti 6 × 10 × 10 =
<strong>600 sm²</strong>, hajmi esa 10 × 10 × 10 = <strong>1000 sm³</strong>. Hajm
mingga sakradi, sirt esa faqat yuz marta oshdi.</p>

<p>Mana butun sir: jism kattalashganda hajmi sirtidan ancha tez oʻsadi.</p>

<p>Endi hayvonlarga qaytamiz. Tana <span class="cn-word" data-tr="harorat, tana chiqaradigan iliqlik">issiqlik</span>ni
butun hajmi bilan ishlab chiqaradi. Lekin uni teri orqali, yaʼni sirti orqali
yoʻqotadi. Sichqonning har bir grammiga juda koʻp teri toʻgʻri keladi. Shuning uchun u
issiqlikni tez yoʻqotadi va yashash uchun tinmay
<span class="cn-word" data-tr="ovqatni energiyaga aylantirish jarayoni">modda almashinuvi</span>ni
tezlatishi kerak: tez yeydi, tez nafas oladi, yuragi tez uradi.</p>

<p>Fil buning teskarisi. Uning har bir kilogrammiga kam teri toʻgʻri keladi va u
issiqlikni yaxshi saqlaydi — hatto ortiqcha saqlaydi. Afrika filining ulkan quloqlari
bezak emas: ular issiqlikni chiqarib yuboradigan
<span class="cn-word" data-tr="issiqlikni tashqariga chiqaruvchi qism">radiator</span> vazifasini bajaradi.</p>

<p>Bu qoidaning ikkinchi tomonini 1638-yilda <b>Galileo Galiley</b> (Galileo Galilei)
yozgan. Suyakning <span class="cn-word" data-tr="narsaning koʻndalang kesimga bogʻliq chidamliligi">mustahkamlik</span>i
uning kesimiga, yaʼni kvadratga bogʻliq. Ogʻirlik esa hajmga — kubga. Odamni ikki
marta kattalashtirsak, suyaklari <strong>4</strong> marta kuchayadi, ogʻirligi esa
<strong>8</strong> marta oshadi.</p>

<p>Shuning uchun ertaklardagi ulkan <span class="cn-word" data-tr="juda katta boʻyli afsonaviy odam">dev</span>
haqiqatda oʻz ogʻirligi ostida sinib ketardi. Chumoli esa oʻz vaznidan oʻn
barobarlab ogʻir yukni koʻtaradi — u kuchli boʻlgani uchun emas, kichik boʻlgani uchun.
Bu <span class="cn-word" data-tr="oʻlcham oʻzgarganda xossalar qanday oʻzgarishi">oʻlcham qonuni</span>
deyiladi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 24 — GPS
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "GPS sizni qanday topadi",
        "summary": (
            "Telefon osmondagi yoʻldoshlargacha boʻlgan masofani vaqt orqali "
            "hisoblaydi, aylanalar kesishgan nuqta esa sizning joyingiz. Toʻrtinchi "
            "yoʻldosh soat xatosini tuzatadi."
        ),
        "order":   24,
        "grammar": [
            {
                "pattern":  "Masofa = tezlik × vaqt",
                "meaning":  "Yoʻldosh xabarni qachon yuborganini aytadi, telefon uni "
                            "qachon olganini biladi. Vaqt farqini signal tezligiga "
                            "koʻpaytirsak, masofa chiqadi. Uchta masofa — uchta "
                            "aylana, ular kesishgan nuqta — joyingiz.",
                "examples": [
                    "300 000 km/s × 0,067 s ≈ 20 100 km — yoʻldoshgacha masofa",
                    "300 000 km/s × 0,000001 s = 0,3 km — bir mikrosekund 300 metr xato",
                ],
            },
        ],
        "questions": [
            {
                "text": "Telefon yoʻldoshgacha boʻlgan masofani qanday biladi?",
                "choices": [
                    "Yoʻldoshni kamera bilan koʻradi",
                    "Signal qancha vaqt uchganini oʻlchab, uni tezlikka koʻpaytiradi",
                    "Masofani xaritadan oʻqiydi",
                    "Yoʻldosh telefonning joyini oʻzi aytadi",
                ],
                "answer": 1,
                "explanation": "Signal har bir yoʻldoshdan yuborilgan vaqti bilan "
                               "keladi. Telefon kechikishni yorugʻlik tezligiga "
                               "koʻpaytiradi: masofa = tezlik × vaqt.",
            },
            {
                "text": "Signal sekundiga 300 000 km uchadi. Telefon soati 2 "
                        "mikrosekund (0,000002 s) xato qilsa, masofadagi xato qancha?",
                "choices": ["60 metr", "300 metr", "2 kilometr", "600 metr"],
                "answer": 3,
                "explanation": "300 000 × 0,000002 = 0,6 km = 600 metr. Shuning uchun "
                               "soat aniqligi GPS uchun hal qiluvchi.",
            },
            {
                "text": "Nega joyni topish uchun uchta emas, toʻrtta yoʻldosh kerak?",
                "choices": [
                    "Bittasi buzilib qolsa, zaxira boʻlsin deb",
                    "Toʻrtinchisi balandlikni aytadi",
                    "Telefonning arzon soati xato qiladi, toʻrtinchi yoʻldosh shu "
                    "xatoni topishga yordam beradi",
                    "Toʻrtinchisi internet beradi",
                ],
                "answer": 2,
                "explanation": "Yoʻldoshlarda atom soatlari bor, telefonda yoʻq. "
                               "Nomaʼlumlar toʻrtta boʻladi: joyning uch oʻlchami va "
                               "soat xatosi — ularni topish uchun toʻrt masofa kerak.",
            },
        ],
        "body": """
<p>Siz notanish shaharda turibsiz va telefon bir zumda «Siz shu yerdasiz» deb
koʻrsatadi. U buni qayerdan biladi? Telefon hech kimga «qayerdaman?» deb
soʻramaydi. U shunchaki tinglaydi va hisoblaydi. Bu tizim <span class="cn-word" data-tr="sunʼiy yoʻldoshlar orqali joyni aniqlash tizimi">GPS</span> deyiladi.</p>

<p>Yer atrofida 30 dan ortiq <span class="cn-word" data-tr="Yer atrofida aylanuvchi sunʼiy qurilma">yoʻldosh</span>
aylanib yuradi — ular taxminan <strong>20 200 km</strong> balandlikda. Har bir
yoʻldosh tinmay bir xil <span class="cn-word" data-tr="radio toʻlqinida yuborilgan xabar">signal</span> yuboradi: «Men hozir mana shu nuqtadaman, soat esa
aynan shuncha».</p>

<p>Xabar <span class="cn-word" data-tr="sekundiga 300 000 km — eng katta tezlik">yorugʻlik tezligi</span>da
uchadi va telefonga taxminan <strong>0,07</strong> sekundda yetib keladi. Telefon
xabar qachon yuborilganini va qachon kelganini solishtiradi. Bu
<span class="cn-word" data-tr="ikki vaqt orasidagi farq">kechikish</span>ni tezlikka
koʻpaytirsa — yoʻldoshgacha boʻlgan masofa chiqadi.</p>

<p>Bitta masofa nima beradi? Faqat «men shu yoʻldoshdan 20 ming km uzoqdaman». Xaritada
bu bitta <span class="cn-word" data-tr="markazdan bir xil uzoqlikdagi nuqtalar chizigʻi">aylana</span>:
siz uning istalgan joyida boʻlishingiz mumkin. Ikkinchi yoʻldosh ikkinchi aylanani
beradi. Ikki aylana odatda ikki nuqtada
<span class="cn-word" data-tr="chiziqlarning bir-birini kesib oʻtishi">kesish</span>adi.
Uchinchisi shu ikkitadan bittasini tanlaydi. Bu usul <span class="cn-word" data-tr="uch masofa orqali joyni topish">trilateratsiya</span> deyiladi.</p>

<figure class="pm-fig">
<svg viewBox="-30 -40 400 350" role="img" aria-label="Uch aylana bitta nuqtada kesishadi">
  <circle class="pm-fill" cx="80" cy="70" r="103"/>
  <circle class="pm-fill" cx="260" cy="80" r="98.5"/>
  <circle class="pm-fill" cx="180" cy="210" r="90.6"/>
  <circle class="pm-ln" cx="80" cy="70" r="103"/>
  <circle class="pm-ln" cx="260" cy="80" r="98.5"/>
  <circle class="pm-ln" cx="180" cy="210" r="90.6"/>
  <circle class="pm-pt" cx="80" cy="70" r="4"/>
  <circle class="pm-pt" cx="260" cy="80" r="4"/>
  <circle class="pm-pt" cx="180" cy="210" r="4"/>
  <circle class="pm-fill--hl" cx="170" cy="120" r="9"/>
  <text class="pm-lbl" x="62" y="60">1-yoʻldosh</text>
  <text class="pm-lbl" x="238" y="70">2-yoʻldosh</text>
  <text class="pm-lbl" x="158" y="232">3-yoʻldosh</text>
  <text class="pm-lbl pm-lbl--hl" x="182" y="125">Siz</text>
</svg>
<figcaption>Har bir masofa — bitta aylana. Uchtasi faqat bitta nuqtada uchrashadi.</figcaption>
</figure>

<p>Lekin bitta muammo bor. Signal shu qadar tez uchadiki, soatdagi
<strong>bir milliondan bir sekund</strong> xato masofani <strong>300 metr</strong>ga
buzadi. Yoʻldoshlarda juda aniq <span class="cn-word" data-tr="atom tebranishi bilan vaqt oʻlchaydigan eng aniq soat">atom soati</span>
bor, telefoningizda esa yoʻq. Shuning uchun telefon <b>toʻrtinchi</b> yoʻldoshni
ham tinglaydi: toʻrtta masofa joyni ham, oʻz soatining xatosini ham birdaniga
topishga yetadi.</p>

<p>Yana bir qiziq tafsilot: <b>Albert Eynshteyn</b> (Albert Einstein) nazariyasiga
koʻra, balandda va tez harakatlanayotgan soat Yerdagidan boshqacha yuradi. Yoʻldosh
soatlari kuniga taxminan <strong>38</strong> mikrosekund oldinga ketadi. Muhandislar
buni oldindan <span class="cn-word" data-tr="xatoni toʻgʻrilash">tuzatish</span>
kiritmaganida, xato har kuni taxminan 11 km ga oʻsib borardi.</p>

<p>Demak, choʻntagingizdagi xarita har soniyada aylanalar, tezlik va hatto nisbiylik
nazariyasi bilan ishlaydi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 36 — Monti Xoll
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Monti Xoll: eshikni almashtirasizmi?",
        "summary": (
            "Haqiqiy voqea: uch eshik, bitta mashina va boshlovchining taklifi. "
            "1990-yilda minglab odamlar, jumladan olimlar ham, notoʻgʻri javobni "
            "himoya qilgan. Yechim gʻoyasi qoida blokida."
        ),
        "order":   36,
        "grammar": [
            {
                "pattern":  "Yechim gʻoyasi: almashtirsangiz — 2/3",
                "meaning":  "Birinchi tanlovingiz 1/3 ehtimol bilan toʻgʻri. Demak "
                            "2/3 ehtimol bilan mashina qolgan ikki eshik ortida. "
                            "Boshlovchi ulardan echkilisini ochib beradi — va oʻsha "
                            "2/3 butunicha yopiq qolgan bitta eshikka oʻtadi.",
                "examples": [
                    "Mashina siz tanlagan eshikda (1/3) → almashtirsangiz yutqazasiz",
                    "Mashina boshqa eshikda (2/3) → boshlovchi echkini ochadi, "
                    "almashtirsangiz yutasiz",
                ],
            },
        ],
        "questions": [
            {
                "text": "Bu oʻyinda boshlovchi haqida eng muhim narsa nima?",
                "choices": [
                    "U mashina qayerdaligini biladi va doim echkili eshikni ochadi",
                    "U eshikni tasodifan ochadi",
                    "U oʻyinchiga yordam berishni xohlaydi",
                    "U har doim uchinchi eshikni ochadi",
                ],
                "answer": 0,
                "explanation": "Boshlovchi bilib turib echkini ochadi. Aynan shu uning "
                               "harakatini maʼlumotga aylantiradi — tasodifiy eshik "
                               "ochilganida bu jumboq boshqacha boʻlardi.",
            },
            {
                "text": "Oʻyin 300 marta oʻynalsa va oʻyinchi har safar eshikni "
                        "almashtirsa, taxminan necha marta mashina yutadi?",
                "choices": ["100 marta", "150 marta", "200 marta", "300 marta"],
                "answer": 2,
                "explanation": "Almashtirish 2/3 ehtimol bilan yutadi: 300 × 2/3 = 200. "
                               "Almashtirmasa — 300 × 1/3 = 100 marta.",
            },
            {
                "text": "Nega yuz eshikli variant yechimni tushunishni osonlashtiradi?",
                "choices": [
                    "Eshiklar koʻp boʻlsa, mashina koʻproq boʻladi",
                    "Birinchi tanlov deyarli har doim notoʻgʻri ekani yaqqol koʻrinadi",
                    "Yuz eshikda boshlovchi xato qiladi",
                    "Yuz eshikda ehtimol 50 % ga teng boʻladi",
                ],
                "answer": 1,
                "explanation": "Yuzta eshikdan toʻgʻrisini topish ehtimoli 1/100. "
                               "Boshlovchi 98 tasini ochgach, qolgan bitta eshik "
                               "99/100 ehtimol bilan mashinali ekani sezgiga ham "
                               "ravshan boʻladi.",
            },
        ],
        "body": """
<p>Siz teleoʻyindasiz. Oldingizda uchta yopiq <span class="cn-word" data-tr="xona yoki bino kirish joyi">eshik</span>.
Bittasining ortida yangi mashina, qolgan ikkitasining ortida — echki. Oʻyinni <span class="cn-word" data-tr="koʻrsatuvni olib boruvchi odam">boshlovchi</span> Monti Xoll (Monty Hall) olib boradi.</p>

<p>Siz <b>1-eshik</b>ni tanlaysiz. Boshlovchi mashina qayerdaligini
<b>biladi</b>. U eshiklardan birini, aytaylik <b>3-eshik</b>ni ochadi — u yerda echki
turibdi. Keyin sizga taklif qiladi: «Xohlasangiz, 2-eshikka almashtiring».</p>

<p><span class="cn-word" data-tr="birinchi qarorni boshqasiga oʻzgartirish">Almashtir</span>asizmi?
Toʻxtang va oʻzingiz javob bering. Koʻpchilik shunday deydi: «Ikkita eshik qoldi,
demak imkoniyat yarmi-yarmi. Farqi yoʻq».</p>

<p>1990-yilda amerikalik yozuvchi <b>Merilin vos Savant</b> (Marilyn vos Savant)
«Parade» jurnalidagi <span class="cn-word" data-tr="gazeta yoki jurnaldagi doimiy boʻlim">rukn</span>ida bu savolga javob berdi: <b>almashtiring</b>, shunda
yutish <span class="cn-word" data-tr="hodisaning roʻy berish imkoniyati darajasi">ehtimol</span>i
<strong>2/3</strong> boʻladi.</p>

<p>Javob <span class="cn-word" data-tr="qizgʻin bahs va shov-shuv">boʻron</span> koʻtardi. Jurnalga taxminan <strong>10 000</strong> ta xat keldi,
ularning mingga yaqini ilmiy darajasi bor odamlardan edi. Ularning aksariyati
Merilinni xato qilganlikda aybladi. Aytishlaricha, mashhur matematik
<b>Pol Erdyosh</b> (Paul Erdős) ham kompyuterdagi
<span class="cn-word" data-tr="hodisani koʻp marta sunʼiy takrorlab sinash">simulyatsiya</span>ni
koʻrmaguncha ishonmagan.</p>

<p>Lekin Merilin haq edi. Buni sezish uchun oʻyinni kattalashtiramiz. Endi eshik
<strong>yuzta</strong>. Siz bittasini tanlaysiz. Boshlovchi qolgan 99 tadan
<strong>98</strong> tasini ochadi — hammasida echki. Bitta eshik yopiq qoldi.</p>

<p>Endi oʻylang: birinchi urinishda yuzta eshikdan toʻgʻrisini topdingizmi? Deyarli
yoʻq — <span class="cn-word" data-tr="kasr bilan ifodalangan imkoniyat">imkoniyat</span>
bor-yoʻgʻi 1/100. Demak mashina deyarli albatta boshlovchi
<b>ataylab</b> yopiq qoldirgan eshik ortida.</p>

<p>Uch eshikda ham xuddi shu narsa roʻy beradi, faqat koʻzga kamroq tashlanadi.
Muhim <span class="cn-word" data-tr="hal qiluvchi kichik tafsilot">nozik nuqta</span>:
boshlovchi tasodifan ochmaydi. Uning tanlovi — bu sizga berilgan
<span class="cn-word" data-tr="vaziyat haqida yangi bilim">maʼlumot</span>.</p>

<p>Ishonmasangiz, doʻstingiz bilan uchta qogʻoz stakan va bitta tanga bilan yigirma
marta oʻynab koʻring. Natijani sanang.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 37 — tugʻilgan kun paradoksi
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Futbol maydonida ikki kishining tugʻilgan kuni bir kunda",
        "summary": (
            "Maydonda 23 kishi — 22 futbolchi va hakam. Ulardan ikkitasining tugʻilgan "
            "kuni bir kunga toʻgʻri kelishi ehtimoli yarmidan koʻp. Sababi — "
            "juftliklar soni."
        ),
        "order":   37,
        "grammar": [
            {
                "pattern":  "Juftliklar soni: n × (n − 1) ÷ 2",
                "meaning":  "Har bir odam qolgan har biri bilan juft tuzadi. "
                            "Har juftni ikki marta sanamaslik uchun 2 ga boʻlamiz. "
                            "Odamlar sekin koʻpaysa ham, juftliklar tez koʻpayadi.",
                "examples": [
                    "10 kishi → 10 × 9 ÷ 2 = 45 juftlik → ehtimol ~12 %",
                    "23 kishi → 23 × 22 ÷ 2 = 253 juftlik → ehtimol ~51 %",
                ],
            },
        ],
        "questions": [
            {
                "text": "23 kishidan nechta turli juftlik tuzish mumkin?",
                "choices": ["46", "253", "23", "529"],
                "answer": 1,
                "explanation": "23 × 22 ÷ 2 = 253. Har juftlik — tugʻilgan kuni mos "
                               "kelishi uchun yana bitta imkoniyat.",
            },
            {
                "text": "Nega koʻpchilik bu ehtimolni juda kichik deb oʻylaydi?",
                "choices": [
                    "Chunki yilda 365 kun borligini unutadi",
                    "Chunki kabisa yilini hisobga oladi",
                    "Chunki «kimdir aynan mening kunimda tugʻilganmi?» deb oʻylaydi, "
                    "barcha juftliklarni emas",
                    "Chunki futbolchilar bir yilda tugʻiladi",
                ],
                "answer": 2,
                "explanation": "Biz savolni oʻzimizga bogʻlaymiz. Lekin mos kelish "
                               "istalgan ikki kishi orasida boʻlishi mumkin — va "
                               "bunday juftliklar 253 ta.",
            },
            {
                "text": "Sinfda 30 oʻquvchi bor. Tugʻilgan kuni bir xil ikki oʻquvchi "
                        "topilishi ehtimoli taxminan qancha?",
                "choices": ["3 %", "10 %", "30 %", "71 %"],
                "answer": 3,
                "explanation": "30 kishida ehtimol taxminan 70,6 % ga yetadi. Har "
                               "uchta sinfdan ikkitasida shunday juftlik bor.",
            },
        ],
        "body": """
<p>Futbol oʻyini boshlanmoqda. Maydonda 22 futbolchi va bitta hakam — jami
<strong>23</strong> kishi. Savol: ularning ichida <span class="cn-word" data-tr="dunyoga kelgan sana">tugʻilgan kun</span>i
bir xil boʻlgan ikki kishi bormi?</p>

<p>Taxmin qilib koʻring. Yilda 365 kun bor, odam esa atigi 23 ta. Koʻpchilik
«juda kam <span class="cn-word" data-tr="hodisaning roʻy berish imkoniyati darajasi">ehtimol</span>, balki 5–6 <span class="cn-word" data-tr="yuzdan bir qism">foiz</span>» deydi.</p>

<p>Toʻgʻri javob esa — <strong>50 foizdan koʻp</strong>. Har ikki oʻyindan birida
maydonda bir kunda tugʻilgan ikki kishi bor. Bu shunchalik gʻalati tuyuladiki, uni
«tugʻilgan kun <span class="cn-word" data-tr="toʻgʻri, lekin aqlga zid tuyuladigan xulosa">paradoks</span>i»
deb atashadi. Aslida bu yerda hech qanday ziddiyat yoʻq — faqat bizning <span class="cn-word" data-tr="hisobsiz, ichki his bilan bilish">sezgi</span>miz
adashadi.</p>

<p>Adashish qayerda? Biz savolni beixtiyor oʻzimizga bogʻlaymiz: «Kimdir aynan
<b>mening</b> kunimda tugʻilganmi?» Bunday savol uchun haqiqatan koʻp odam kerak —
50 % ehtimolga yetish uchun 253 kishi.</p>

<p>Lekin savol boshqa edi: <b>istalgan ikki kishi</b>. Hujumchi va darvozabon,
hakam va himoyachi — har bir <span class="cn-word" data-tr="ikki kishidan iborat guruh">juftlik</span>
yangi imkoniyat. 23 kishidan nechta juftlik chiqadi? Har bir odam qolgan 22 kishi
bilan juft boʻladi: 23 × 22. Lekin shunda har juft ikki marta
<span class="cn-word" data-tr="bir narsani qayta hisoblash">sanaladi</span>, shuning
uchun ikkiga boʻlamiz: <strong>253</strong> juftlik.</p>

<p>Qiziq tasodif: «mening kunim» uchun kerak boʻlgan 253 kishi va 23 kishidagi
253 juftlik — bir xil son. Har ikki holatda ham taxminan 253 ta imkoniyat bor.</p>

<p>Odamlar koʻpaygani sari ehtimol tez oʻsadi. Aniq
<span class="cn-word" data-tr="aniq qoida asosidagi hisob">hisob</span> shunday:
10 kishida — taxminan <strong>12 %</strong>, 23 kishida — <strong>50,7 %</strong>,
30 kishida — <strong>71 %</strong>, 70 kishida esa — <strong>99,9 %</strong>.</p>

<p>Bu matematika hayotda ham ishlaydi. Kompyuterlar maʼlumotni qisqa
<span class="cn-word" data-tr="maʼlumotdan olingan qisqa raqamli iz">kod</span>larga
aylantiradi. Muhandislar kodlarning ikkitasi tasodifan bir xil chiqishini xuddi shu
usul bilan baholaydi.</p>

<p>Ertaga sinfingizda tekshirib koʻring. Agar oʻquvchilar 30 ta boʻlsa, mos
<span class="cn-word" data-tr="bir xil boʻlib chiqish">tushish</span> topilishi
ehtimoli topilmasligidan ancha yuqori.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 38 — Hilbert mehmonxonasi
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Hilbert mehmonxonasi: hamma xona band, lekin joy bor",
        "summary": (
            "Nemis matematigi David Hilbert oʻylab topgan mehmonxonada xonalar "
            "cheksiz va hammasi band. Shunda ham yangi mehmonga — hatto cheksiz "
            "avtobusga ham — joy topiladi."
        ),
        "order":   38,
        "grammar": [
            {
                "pattern":  "Yechim gʻoyasi: siljitish va ikkiga koʻpaytirish",
                "meaning":  "Cheksiz toʻplamda «hamma joy band» degani «joy yoʻq» "
                            "degani emas. Har bir mehmonni yangi xonaga koʻchirish "
                            "qoidasi berilsa — hech kim koʻchada qolmaydi.",
                "examples": [
                    "Bitta mehmon: n-xonadagi odam → n + 1-xonaga. 1-xona boʻshaydi",
                    "Cheksiz avtobus: n-xonadagi odam → 2n-xonaga. Barcha toq "
                    "xonalar (1, 3, 5, …) boʻshaydi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Bitta yangi mehmon kelganda menejer qanday buyruq beradi?",
                "choices": [
                    "Hamma bir xona oldinga siljisin: 1 → 2, 2 → 3 va hokazo",
                    "Oxirgi xonadagi mehmon chiqib ketsin",
                    "Ikki mehmon bitta xonada yashasin",
                    "Mehmonxona yopilsin",
                ],
                "answer": 0,
                "explanation": "Har kim keyingi xonaga oʻtadi. Cheksiz mehmonxonada "
                               "«oxirgi xona» yoʻq, shuning uchun hamma joy topadi va "
                               "1-xona boʻshaydi.",
            },
            {
                "text": "Cheksiz avtobus kelganda 7-xonadagi mehmon qaysi xonaga "
                        "koʻchadi?",
                "choices": ["8-xonaga", "7-xonada qoladi", "14-xonaga", "49-xonaga"],
                "answer": 2,
                "explanation": "Qoida: n-xonadan 2n-xonaga. 7 × 2 = 14. Eski mehmonlar "
                               "juft xonalarga oʻtadi, toq xonalar yangilarga qoladi.",
            },
            {
                "text": "Bu jumboq nimani koʻrsatadi?",
                "choices": [
                    "Mehmonxonalar har doim kichik boʻladi",
                    "Cheksiz toʻplamlar oddiy, chekli toʻplamlar qoidalariga "
                    "boʻysunmaydi",
                    "Hilbert mehmonxona qurgan",
                    "Toq sonlar juft sonlardan koʻp",
                ],
                "answer": 1,
                "explanation": "Chekli mehmonxonada band boʻlsa — joy yoʻq. Cheksizda "
                               "esa qism butunga teng boʻla oladi: juft xonalar ham "
                               "barcha mehmonlarga yetadi.",
            },
        ],
        "body": """
<p>Kechasi charchagan yoʻlovchi mehmonxonaga kiradi. Qabulxonada yozuv: «Barcha
xonalar band». Odatda bu suhbatning oxiri. Ammo bu oddiy mehmonxona emas.</p>

<p>Bu — <b>Hilbert mehmonxonasi</b>. Uni nemis matematigi <b>David Hilbert</b>
(David Hilbert) 1924-yildagi bir maʼruzasida oʻylab topgan. Mehmonxonada
<span class="cn-word" data-tr="oxiri yoʻq, tugamaydigan">cheksiz</span> koʻp xona
bor: 1, 2, 3, 4 va shunday davom etadi, hech qachon tugamaydi. Va har bir xonada
mehmon yashaydi.</p>

<p>Yangi yoʻlovchi uchun joy bormi? Oʻylab koʻring.</p>

<p><span class="cn-word" data-tr="mehmonxonani boshqaruvchi odam">Menejer</span>
mikrofonni oladi va bitta buyruq beradi: «Har kim oʻz xonasining
<span class="cn-word" data-tr="raqami bittaga katta">keyingi</span>siga koʻchsin».
1-xonadagi mehmon 2-xonaga, 2-xonadagisi 3-xonaga oʻtadi va hokazo. Hech kim
koʻchada qolmaydi, chunki «eng oxirgi xona» degan narsa yoʻq. Natijada
<b>1-xona boʻshaydi</b> — yoʻlovchi kirib yotadi.</p>

<p>Ertasiga yanada qiyinroq: mehmonxona oldiga cheksiz uzun
<span class="cn-word" data-tr="koʻp yoʻlovchi tashiydigan mashina">avtobus</span>
keladi. Unda cheksiz koʻp yoʻlovchi bor. Endi har kimni bittadan siljitish yetmaydi.</p>

<p>Menejer yangi buyruq beradi: «Har kim oʻz xona raqamini <b>ikkiga
koʻpaytirsin</b> va oʻsha xonaga koʻchsin». 1 → 2, 2 → 4, 3 → 6… Eski mehmonlar
hammasi <span class="cn-word" data-tr="2 ga qoldiqsiz boʻlinadigan">juft</span>
xonalarga joylashadi. Barcha <span class="cn-word" data-tr="2 ga boʻlinmaydigan">toq</span>
xonalar — 1, 3, 5, 7… — boʻshab qoladi. Ular ham cheksiz koʻp, demak avtobusdagi
hammaga joy yetadi.</p>

<p>Bu kulgili ertak emas, jiddiy gʻoya. Chekli
<span class="cn-word" data-tr="bir guruhga birlashtirilgan narsalar">toʻplam</span>da
qism hech qachon butunga teng boʻlmaydi: savatdagi olmalarning yarmi butun savatdan
kam. Cheksizlikda esa juft sonlarning oʻzi barcha natural sonlar bilan bittadan
<span class="cn-word" data-tr="har biriga roppa-rosa bitta juft topish">mos qoʻyiladi</span>:
1 ↔ 2, 2 ↔ 4, 3 ↔ 6…</p>

<p>Hilbert shu bilan bir narsani koʻrsatmoqchi edi: cheksizlik — bu shunchaki «juda
katta son» emas. U oʻzining qoidalari bilan yashaydigan butunlay boshqa olam.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 41 — qogʻozni buklash
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Qogʻozni 42 marta buklasangiz, Oyga yetasiz",
        "summary": (
            "Qalinligi 0,1 mm boʻlgan qogʻoz har buklashda ikki barobar qalinlashadi. "
            "42 bukishdan keyin u Oygacha yetadi — ikki marta oshishning kuchi "
            "haqida."
        ),
        "order":   41,
        "grammar": [
            {
                "pattern":  "Ikki barobar oshish: 2 × 2 × 2 × … (n marta)",
                "meaning":  "Har qadamda miqdor ikki barobar oshsa, n qadamdan keyin "
                            "u 2<sup>n</sup> marta katta boʻladi. Boshida sekin "
                            "koʻrinadi, keyin esa har qadam oldingi hamma "
                            "qadamlardan koʻproq qoʻshadi.",
                "examples": [
                    "10 bukish → 2<sup>10</sup> = 1024 qavat ≈ 10 sm",
                    "42 bukish → 2<sup>42</sup> qavat × 0,1 mm ≈ 440 000 km",
                ],
            },
        ],
        "questions": [
            {
                "text": "Qogʻoz 10 marta buklansa, nechta qavat hosil boʻladi?",
                "choices": ["20", "100", "512", "1024"],
                "answer": 3,
                "explanation": "Har bukish qavatlarni ikki barobar oshiradi: "
                               "2<sup>10</sup> = 1024. Qalinligi 1024 × 0,1 mm ≈ "
                               "10 sm.",
            },
            {
                "text": "27 bukishdan keyin qogʻoz qalinligi taxminan 13 km boʻladi. "
                        "28-bukishdan keyin-chi?",
                "choices": ["Taxminan 14 km", "Taxminan 26 km", "Taxminan 27 km",
                            "Taxminan 130 km"],
                "answer": 1,
                "explanation": "Har bukish qalinlikni ikki barobar oshiradi: "
                               "13 × 2 = 26 km. Bitta qadam oldingi 27 qadamning "
                               "hammasicha qoʻshadi.",
            },
            {
                "text": "Nega haqiqatda qogʻozni 7–8 martadan koʻp buklash qiyin?",
                "choices": [
                    "Qogʻoz har safar ikki barobar qalin va kalta boʻlib, tez orada "
                    "egilmaydigan boʻlib qoladi",
                    "Qogʻoz 7 bukishdan keyin yirtiladi",
                    "Bu qonun bilan taqiqlangan",
                    "Qogʻoz har bukishda yupqalashadi",
                ],
                "answer": 0,
                "explanation": "7 bukishda 128 qavat — yupqa daftar qalinligi, uzunligi "
                               "esa juda qisqa. Britni Gallivan 12 marta buklash uchun "
                               "1 km dan uzun qogʻoz ishlatgan.",
            },
        ],
        "body": """
<p>Oddiy daftar varagʻini oling. Uning
<span class="cn-word" data-tr="narsaning bir yuzidan ikkinchisigacha masofa">qalinlik</span>i
taxminan <strong>0,1 millimetr</strong>. Uni ikkiga buklang — ikki qavat. Yana
buklang — toʻrt qavat. Agar shunday <strong>42</strong> marta buklay olsangiz, uning
qalinligi qancha boʻladi?</p>

<p>Koʻpchilik «bir necha santimetr, nari borsa bir metr» deydi. Toʻgʻri javob:
<b>Oygacha yetadi</b>. Keling, qadam-baqadam koʻraylik.</p>

<p>Har bir buklash qavatlar sonini <span class="cn-word" data-tr="ikki marta koʻp">ikki barobar</span>
oshiradi. 7 bukishdan keyin 128 qavat — taxminan <strong>1,3 sm</strong>, yupqa
daftar qalinligi. Hali hech qanday moʻjiza yoʻq.</p>

<p>10 bukish — 1024 qavat, taxminan <strong>10 sm</strong>, gʻisht qalinligi.
14 bukish — <strong>1,6 metr</strong>, sizning boʻyingiz. 20 bukish —
<strong>105 metr</strong>, 30 qavatli bino.</p>

<p>Endi tezlik keskin oshadi. 27 bukish — taxminan <strong>13 km</strong>: Everest
choʻqqisidan ham, <span class="cn-word" data-tr="yoʻlovchi tashiydigan katta samolyot">laynerlar</span>
uchadigan balandlikdan ham baland. 30 bukish — <strong>107 km</strong>, bu esa
allaqachon <span class="cn-word" data-tr="Yer havosidan tashqaridagi boʻshliq">koinot</span>.</p>

<p>42 bukish esa — taxminan <strong>440 000 km</strong>. Oygacha boʻlgan
<span class="cn-word" data-tr="ikki nuqta orasidagi uzunlik">masofa</span>
384 400 km. Qogʻoz uni ortda qoldiradi.</p>

<p>Bu qanday mumkin? Sir — <span class="cn-word" data-tr="har qadamda bir xil marta koʻpayib boradigan oʻsish">eksponensial oʻsish</span>da.
Har yangi bukish oʻzidan oldingi <b>hamma</b> bukishlar yigʻindisicha qalinlik
qoʻshadi. 41-bukishdan 42-ga oʻtishning oʻzi 220 ming km qoʻshadi.</p>

<p>Amalda esa qogʻozni 7–8 martadan koʻp buklash qiyin: u har safar ikki barobar
qalin va ikki barobar kalta boʻladi. 2002-yilda amerikalik maktab oʻquvchisi
<b>Britni Gallivan</b> (Britney Gallivan) buning
<span class="cn-word" data-tr="hisoblash yoʻli bilan topilgan qoida">formula</span>sini
topdi va 1 km dan uzun qogʻoz tasmasini <strong>12</strong> marta buklab,
<span class="cn-word" data-tr="avval hech kim erisha olmagan natija">rekord</span> qoʻydi.</p>

<p>Bu hikoyaning saboqi qogʻoz haqida emas. Har kuni ikki barobar koʻpayadigan narsa —
mikrob, mish-mish yoki jamgʻarma — boshida arzimas koʻrinadi. Keyin esa bir
zumda hammasini egallab oladi.</p>
""",
    },
]
