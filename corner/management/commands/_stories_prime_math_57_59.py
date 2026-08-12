# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-57, PM-58, PM-59 (Blok E: Geometriya boshlanishi).

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 57 — hikoya (xona rejasi chizilyapti), 58 — jumboq (soat millari),
59 — ilmiy-ommabop (chorraha va yoʻl muhandisligi). Oldingi uchtasi hikoya,
tarix va sport edi.

⚠️ Kumulyativ: parallel chiziq (PM-60), uchburchak burchaklari yigʻindisi
   (PM-61), Pifagor (PM-64), perimetr (PM-67), yuza (PM-68) va π (PM-70) YOʻQ.
   Masshtab (PM-28) va sistema (PM-54) esa erkin ishlatiladi.
⚠️ `grammar.pattern` va `examples` ekranlanadi — <sup> emas, Unicode ² yoziladi.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_57_59.py --author=prime
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
    # PM-57 — geometriya alifbosi                                HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Chizgʻich va qalam — birinchi chizma",
        "summary": (
            "PM-57 matni. Hikoya: Dilnoza xonasining rejasini 1 : 50 "
            "masshtabda chizadi va chizmada nuqta, kesma va toʻgʻri chiziq "
            "bir-biridan nimasi bilan farq qilishini oʻz qoʻli bilan koʻradi."
        ),
        "order":   57,
        "grammar": [
            {
                "pattern":  "1 : 50 masshtab — rejadagi 1 sm haqiqatda 50 sm",
                "meaning":  "Chizmadagi <b>kesma</b> oʻlchanadi, keyin masshtabga "
                            "koʻpaytiriladi. Toʻgʻri chiziqni esa oʻlchab "
                            "boʻlmaydi — u ikki tomonga cheksiz.",
                "examples": [
                    "12 sm × 50 = 600 sm = 6 m (uzun devor)",
                    "8 sm × 50 = 400 sm = 4 m (eshikkacha)",
                    "12 − 8 = 4 sm, demak eshikdan burchakkacha 4 × 50 = 200 sm = 2 m",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega Dilnoza chiziq chizishdan oldin ikkita nuqta "
                        "qoʻydi?",
                "choices": [
                    "Chizgʻich ikkita nuqtasiz sirpanib ketgani uchun",
                    "Qalamni oʻtkirlash oson boʻlishi uchun",
                    "Ikki nuqta orqali faqat bitta toʻgʻri chiziq oʻtgani uchun",
                    "Rejada ikkita devor boʻlgani uchun",
                ],
                "answer": 2,
                "explanation": "Matnda otasi aytdi: bitta nuqta orqali cheksiz "
                               "koʻp chiziq oʻtadi, ikkitasi esa chiziqni "
                               "qotirib qoʻyadi. Shuning uchun usta ham taxtani "
                               "ikkita mix bilan qoqadi.",
            },
            {
                "text": "Rejadagi 12 sm lik uzun devor haqiqatda necha metr?",
                "choices": ["2,4 metr", "6 metr", "12 metr", "24 metr"],
                "answer": 1,
                "explanation": "Masshtab 1 : 50, demak rejadagi har bir "
                               "santimetr haqiqatda 50 sm. 12 × 50 = 600 sm, "
                               "yaʼni 6 metr.",
            },
            {
                "text": "Eshikdan xonaning ikkinchi burchagigacha haqiqatda "
                        "necha metr?",
                "choices": ["0,5 metr", "1 metr", "1,5 metr", "2 metr"],
                "answer": 3,
                "explanation": "Rejada devor 12 sm, eshikkacha esa 8 sm. "
                               "Kesmalar qoʻshiladi, demak qolgani "
                               "12 − 8 = 4 sm. Haqiqatda: 4 × 50 = 200 sm = "
                               "2 metr.",
            },
        ],
        "body": """
<p>Dilnoza xonasiga yangi javon olishni soʻradi. Otasi bir varaq qogʻoz, chizgʻich
va qalam olib keldi.</p>

<p>«Avval reja chizamiz», — dedi u. — «Boʻlmasa javon sigʻmay qolishi mumkin.»</p>

<p>Dilnoza devorni chizmoqchi boʻlib qalamni qogʻozga tegizdi. Otasi toʻxtatdi:
«Bitta <span class="cn-word" data-tr="oʻlchamsiz, faqat oʻrinni koʻrsatuvchi shakl">nuqta</span>dan
cheksiz koʻp chiziq oʻtadi. Qalamni aylantirib koʻr — har safar yangisi chiqadi.
Lekin <b>ikkita</b> nuqta qoʻysang, ular orqali faqat bitta
<span class="cn-word" data-tr="ikki tomonga cheksiz davom etuvchi chiziq">toʻgʻri chiziq</span>
oʻtadi.»</p>

<p>Dilnoza ikkita nuqta qoʻydi va ularni tutashtirdi. Qogʻozda
<span class="cn-word" data-tr="ikki uchi bor, oʻlchanadigan chiziq boʻlagi">kesma</span>
paydo boʻldi — ikkala
<span class="cn-word" data-tr="kesma yoki nurning boshlangʻich nuqtasi">uch</span>i ham
bor, demak uni oʻlchash mumkin.</p>

<p>«Rejamiz <span class="cn-word" data-tr="chizmadagi 1 sm haqiqatda qanchaligi">masshtab</span>i
1 : 50 boʻlsin», — dedi otasi. Uzun devor rejada <strong>12</strong> sm chiqdi.
Dilnoza hisobladi: 12 × 50 = 600 sm, yaʼni <strong>6</strong> metr.</p>

<p>Keyin eshikni belgiladi. U burchakdan <strong>8</strong> sm narida edi —
haqiqatda 4 metr. Qolgan boʻlak esa 12 − 8 = <strong>4</strong> sm, yaʼni
<strong>2</strong> metr. Kesmalar xuddi sonlardek qoʻshilardi.</p>

<p>Ikkinchi devorni chizganda ikki chiziq xonaning burchagida uchrashdi. Otasi
oʻsha joyni qalam bilan bosdi: «Mana bu —
<span class="cn-word" data-tr="ikki chiziqning umumiy nuqtasi">kesishish nuqtasi</span>.
Ikki chiziq bundan koʻproq joyda uchrasha olmaydi.»</p>

<p>Butun <span class="cn-word" data-tr="shakllarning aniq oʻlchovli tasviri">chizma</span>
bir varaq qogʻozda yotardi — geometriyada uni
<span class="cn-word" data-tr="cheksiz tekis yuza — chizmalar shu yerda yotadi">tekislik</span>
deyishadi.</p>

<p>Oxirida Dilnoza xonaning
<span class="cn-word" data-tr="kesmani teng ikkiga boʻluvchi nuqta">oʻrta nuqta</span>siga
belgi qoʻydi va qalamni deraza tomon
<span class="cn-word" data-tr="boshi bor, oxiri yoʻq chiziq">nur</span> qilib
uzatdi: yorugʻlik shu tomondan tushardi.</p>

<p>«Bu chiziqning oxiri yoʻqmi?» — soʻradi u. «Yoʻq», — kuldi otasi. — «Lekin
javonning oʻlchami bor. Mana shuning uchun biz kesmalarni oʻlchaymiz —
nurlarni emas.»</p>

<p>Ertasi kuni ular javon bilan qaytishdi. U aynan joyiga tushdi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-58 — burchak                                            JUMBOQ
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Soat millari orasidagi burchak",
        "summary": (
            "PM-58 matni. Jumboq: soat 3:00 da millar orasidagi burchak 90°. "
            "Xoʻsh, 3:30 da-chi? Koʻpchilik «yana 90°» deydi — va adashadi, "
            "chunki soat mili ham joyida turmaydi."
        ),
        "order":   58,
        "grammar": [
            {
                "pattern":  "daqiqa mili — daqiqasiga 6°, soat mili — daqiqasiga 0,5°",
                "meaning":  "Toʻla burchak 360°. Daqiqa mili uni 60 daqiqada "
                            "aylanadi, soat mili esa 12 soatda — shuning uchun "
                            "soat mili ancha sekin, lekin <b>hech qachon "
                            "toʻxtamaydi</b>.",
                "examples": [
                    "siferblatdagi bir boʻlim: 360 ÷ 12 = 30°",
                    "3:00 — soat mili 90°, daqiqa mili 0°, orasi 90°",
                    "3:30 — soat mili 90 + 15 = 105°, daqiqa mili 180°, orasi 75°",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega soat 3:30 da millar orasidagi burchak 90° emas?",
                "choices": [
                    "Soat mili ham yarim boʻlimga siljib ulgurgani uchun",
                    "Daqiqa mili 180° dan oshib ketgani uchun",
                    "Soat 3:30 da millar ustma-ust tushgani uchun",
                    "Siferblatdagi boʻlimlar teng boʻlmagani uchun",
                ],
                "answer": 0,
                "explanation": "Yarim soatda soat mili 3 bilan 4 ning oʻrtasiga "
                               "keladi, yaʼni 15° qoʻshimcha yuradi. Shuning "
                               "uchun burchak 90° emas, 75° boʻlib qoladi.",
            },
            {
                "text": "Soat 3:30 da millar orasidagi burchak necha gradus?",
                "choices": ["60°", "75°", "90°", "105°"],
                "answer": 1,
                "explanation": "Daqiqa mili 6 raqamida — 180°. Soat mili "
                               "3 × 30 + 15 = 105°. Farqi: 180 − 105 = 75°. "
                               "«105°» — bu soat milining oʻrni, millar orasidagi "
                               "burchak emas.",
            },
            {
                "text": "Soat aynan 6:00 boʻlganda millar orasidagi burchak "
                        "qanday nomlanadi?",
                "choices": [
                    "Oʻtkir burchak",
                    "Toʻgʻri burchak",
                    "Oʻtmas burchak",
                    "Yoyiq burchak",
                ],
                "answer": 3,
                "explanation": "6:00 da millar orasida 6 ta boʻlim bor: "
                               "6 × 30 = 180°. 180° li burchak yoyiq burchak "
                               "deyiladi — millar bir toʻgʻri chiziqda "
                               "yotadi.",
            },
        ],
        "body": """
<p>Sinfda devor soati chiqillab turardi. Bekzod unga qarab qoldi.</p>

<p>«Hozir uch boʻldi», — dedi u. — «Millar orasidagi
<span class="cn-word" data-tr="umumiy boshlangʻich nuqtali ikki nur">burchak</span>
aniq toʻqson.»</p>

<p>Nodira opa boshini qimirlatdi. Ikkala mil ham soatning markazidan chiqadi —
demak oʻsha markaz burchakning
<span class="cn-word" data-tr="nurlar chiqqan nuqta">uch</span>i, millar esa uning
<span class="cn-word" data-tr="uchdan chiqqan nurlardan biri">tomon</span>lari.</p>

<p>Siferblatda 12 ta boʻlim bor,
<span class="cn-word" data-tr="toʻliq aylanish, 360° li burchak">toʻla burchak</span> esa
<strong>360</strong>
<span class="cn-word" data-tr="burchak oʻlchov birligi, aylananing 360 dan biri">gradus</span>.
Demak bitta boʻlim 360 ÷ 12 = <strong>30</strong>°. Soat 3:00 da millar orasida
uchta boʻlim bor: 3 × 30 = <strong>90</strong>° —
<span class="cn-word" data-tr="aniq 90° li burchak">toʻgʻri burchak</span>.</p>

<p>«Endi jumboq», — dedi u. — «Soat 3:30 boʻlsa-chi?»</p>

<p>Sherbek darrov javob berdi: «Yana toʻqson. Daqiqa mili pastga tushdi,
soat mili esa uchda turibdi.»</p>

<p>«Soat mili turibdimi?» — soʻradi Nodira opa.</p>

<p>Sinf jimib qoldi. Soat mili bir joyda turmaydi — u ham asta suriladi. Yarim
soatda u 3 bilan 4 ning oʻrtasiga yetadi, yaʼni yana 15° yuradi.</p>

<p>Bekzod hisoblay boshladi. Daqiqa mili 6 raqamida:
6 × 30 = <strong>180</strong>°. Soat mili esa 90 + 15 = <strong>105</strong>°.
Millar orasidagi burchak — ularning farqi: 180 − 105 = <strong>75</strong>°.</p>

<p>«Yetmish besh!» — dedi u. Bu 90 dan kichik, demak
<span class="cn-word" data-tr="90° dan kichik burchak">oʻtkir burchak</span>,
<span class="cn-word" data-tr="90° bilan 180° orasidagi burchak">oʻtmas</span> emas.</p>

<p>Nodira opa
<span class="cn-word" data-tr="burchak oʻlchaydigan asbob">transportir</span>ni
koʻtardi: «Oʻlchab koʻrsak ham shu chiqadi. Lekin hisob bilan topgan aniqroq —
chunki chizmada qoʻl qaltiraydi, sonda esa qaltiramaydi.»</p>

<p>Uyga vazifa oddiy edi: soat 6:00 da millar orasida nechta boʻlim bor va u
qanday <span class="cn-word" data-tr="180° li burchak">yoyiq burchak</span>
ekanini tushuntirish.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-59 — burchak juftliklari                        ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Chorrahadagi burchaklar",
        "summary": (
            "PM-59 matni. Ilmiy-ommabop: yoʻl muhandislari nega chorrahani "
            "toʻgʻri burchakka yaqin qilishga harakat qiladi va nega ular "
            "toʻrtta burchakning faqat bittasini oʻlchashadi."
        ),
        "order":   59,
        "grammar": [
            {
                "pattern":  "qoʻshni — 180°, vertikal — teng, toʻrttasi — 360°",
                "meaning":  "Ikki toʻgʻri chiziq kesishganda toʻrtta burchak "
                            "hosil boʻladi, lekin <b>mustaqil</b> qiymat "
                            "bittagina: qolgan uchtasi undan kelib chiqadi.",
                "examples": [
                    "berilgan: 65°",
                    "qoʻshnisi: 180 − 65 = 115°",
                    "vertikallari: yana 65° va 115°",
                    "tekshirish: 65 + 115 + 65 + 115 = 360°",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega yoʻl muhandislari chorrahani toʻgʻri burchakka "
                        "yaqin qilishga harakat qiladi?",
                "choices": [
                    "Juda oʻtkir burchakda haydovchining koʻrish sohasi "
                    "yomonlashadi",
                    "Toʻgʻri burchakli chorraha kamroq joy egallaydi",
                    "Asfalt toʻgʻri burchakda tez quriydi",
                    "Yoʻl belgilarini faqat 90° da oʻrnatish mumkin",
                ],
                "answer": 0,
                "explanation": "Matnda aytilgan: oʻtkir burchak ostida "
                               "kesishgan yoʻlda haydovchi yon tomonni koʻrish "
                               "uchun boshini juda burishi kerak boʻladi va bir "
                               "qism yoʻl koʻrinmay qoladi.",
            },
            {
                "text": "Chorrahaning bitta burchagi 65° boʻlsa, unga qoʻshni "
                        "burchak necha gradus?",
                "choices": ["25°", "65°", "115°", "295°"],
                "answer": 2,
                "explanation": "Qoʻshni burchaklar birgalikda yoyiq burchakni "
                               "toʻldiradi: 180 − 65 = 115°. «25°» — bu "
                               "toʻldiruvchisi (90 − 65), «65°» esa "
                               "qarama-qarshi yotgan vertikal burchak.",
            },
            {
                "text": "Chorrahadagi toʻrtta burchakning yigʻindisi qancha?",
                "choices": ["180°", "270°", "300°", "360°"],
                "answer": 3,
                "explanation": "Toʻrtala burchak kesishish nuqtasi atrofini "
                               "toʻliq aylanib chiqadi: 65 + 115 + 65 + 115 = "
                               "360°. Muhandislar buni tekshiruv sifatida "
                               "ishlatadi — yigʻindi 360 chiqmasa, oʻlchovda "
                               "xato bor.",
            },
        ],
        "body": """
<p>Shahar chetida yangi yoʻl qurilyapti. U eski koʻchani kesib oʻtadi — demak
yangi chorraha paydo boʻladi.</p>

<p>Loyihachilar avval bitta savolni hal qilishadi: ikki koʻcha qanday burchak
ostida <span class="cn-word" data-tr="ikki chiziqning umumiy nuqtasi">kesishsin</span>?
Javob koʻpincha bir xil: iloji boricha
<span class="cn-word" data-tr="aniq 90° li burchak">toʻgʻri burchak</span>ka yaqin.</p>

<p>Sababi xavfsizlikda. Agar yoʻllar juda
<span class="cn-word" data-tr="90° dan kichik burchak">oʻtkir burchak</span>
ostida kesishsa, haydovchi yon tomonni koʻrish uchun boshini deyarli orqasiga
burishi kerak boʻladi. Bir qism yoʻl esa umuman koʻrinmay qoladi. Toʻgʻri
burchakka yaqin chorrahada esa ikkala tomon ham bir qarashda koʻrinadi.
Shuning uchun bunday chiziqlarni
<span class="cn-word" data-tr="toʻgʻri burchak ostida kesishuvchi">perpendikulyar</span>
deyishadi.</p>

<p>Eski chorrahalar har doim ham shunday emas. Xaritada oʻlchangan bittasi
<strong>65</strong>°
<span class="cn-word" data-tr="burchak oʻlchov birligi, aylananing 360 dan biri">gradus</span>
chiqdi.</p>

<p>Muhandis qolgan uchtasini oʻlchamadi. Unga hojat yoʻq edi.
<span class="cn-word" data-tr="yigʻindisi 180° boʻlgan yonma-yon burchaklar">Qoʻshni burchak</span>
birgalikda <span class="cn-word" data-tr="180° li burchak">yoyiq burchak</span>ni
toʻldiradi: 180 − 65 = <strong>115</strong>°. Qarama-qarshi yotganlari esa
<span class="cn-word" data-tr="kesishgan chiziqlarda qarama-qarshi yotgan teng burchaklar">vertikal burchaklar</span> —
ular teng, demak yana <strong>65</strong>° va <strong>115</strong>°.</p>

<p>Oxirida u tekshirdi: 65 + 115 + 65 + 115 = <strong>360</strong>° — nuqta
atrofidagi <span class="cn-word" data-tr="360° li burchak">toʻla burchak</span>.
Yigʻindi 360 chiqmasa, oʻlchovda xato bor degani.</p>

<p>Chorrahaning shakli faqat qogʻozda qolmaydi. Oʻtkir burchak tomonidagi
piyodalar yoʻlagi uzunroq boʻladi, chunki koʻchani kesib oʻtish yoʻli qiyshiq
tushadi. Svetofor ustuni ham shu burchakka qarab oʻrnatiladi — haydovchi uni
oʻz yoʻlidan koʻrishi kerak.</p>

<p>Shuning uchun yangi mahallalarni loyihalashda koʻchalar imkon qadar
<strong>90</strong>° ostida kesishtiriladi. Bu shunchaki chiroyli koʻrinish
emas — bu xavfsizlik hisobi.</p>

<p>Mana shu — geometriyaning eng foydali odati. Bitta oʻlchov, uchta
<span class="cn-word" data-tr="maʼlum qoidalardan yangi qoidani keltirib chiqarish">isbot</span>langan
xulosa va nol qoʻshimcha ish.</p>
""",
    },
]
