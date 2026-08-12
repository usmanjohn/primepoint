# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-60, PM-61, PM-62 (Blok E: Geometriya).

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr: 60 — hikoya/sayohat qaydlari, 61 — ilmiy-ommabop, 62 — jumboq.
⚠️ 60-matn tocda «ilmiy-ommabop» deb rejalashtirilgan edi, lekin 59-matn ham
   ilmiy-ommabop — ketma-ket uchtasi bir xil shakl boʻlib qolardi. Mavzu
   (temir yoʻl, shpallar, koʻz aldanishi) saqlandi, shakli hikoyaga
   oʻzgartirildi. Tocdagi janr yorligʻi ham yangilandi.

⚠️ Kumulyativ: teng yonli uchburchak xossalari (PM-63), Pifagor (PM-64),
   perimetr (PM-67), yuza (PM-68) va π (PM-70) YOʻQ. 61-matnda toʻrtburchak
   faqat KUZATUV sifatida tilga olinadi, xossalari oʻrgatilmaydi (PM-66).
⚠️ `grammar.pattern` va `examples` ekranlanadi — <sup> emas, Unicode ² yoziladi.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_60_62.py --author=prime
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
    # PM-60 — parallel chiziqlar                                 HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Poyezd derazasidan — relslar qayerda tutashadi?",
        "summary": (
            "PM-60 matni. Sayohat qaydlari: Bekzod poyezd derazasidan "
            "relslarga qaraydi va ular uzoqda tutashgandek koʻrinadi. "
            "Tutashmaydi — bu koʻz aldanishi; relslar parallel, shpallar esa "
            "kesuvchi."
        ),
        "order":   60,
        "grammar": [
            {
                "pattern":  "parallel + kesuvchi: mos va almashinuvchi — teng, bir tomonli — 180°",
                "meaning":  "Ikki <b>parallel</b> chiziqni kesuvchi kesib "
                            "oʻtganda sakkizta burchak hosil boʻladi, lekin "
                            "ularning bor-yoʻgʻi ikkita qiymati boʻladi.",
                "examples": [
                    "tayanch relslar bilan 65° burchak hosil qildi",
                    "bir tomonli ichki burchak: 180 − 65 = 115°",
                    "ikkinchi relsdagi mos burchak: yana 65°",
                    "shpal relsga perpendikulyar: toʻrttala burchak ham 90°",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega relslar uzoqda tutashgandek koʻrinadi?",
                "choices": [
                    "Ular haqiqatan ham gorizontda tutashadi",
                    "Bu koʻz aldanishi — relslar parallel va kesishmaydi",
                    "Relslar issiqda qisqarib qoladi",
                    "Poyezd tez yurgani uchun shunday tuyuladi",
                ],
                "answer": 1,
                "explanation": "Amaki tushuntirdi: uzoqdagi narsalar kichik "
                               "koʻrinadi, shuning uchun relslar orasidagi "
                               "masofa ham kichrayib boradi. Aslida u hamma "
                               "joyda bir xil — parallel chiziqlar hech qachon "
                               "kesishmaydi.",
            },
            {
                "text": "Tayanch relslar bilan 65° burchak hosil qilgan boʻlsa, "
                        "bir tomonli ichki burchak necha gradus?",
                "choices": ["25°", "65°", "115°", "125°"],
                "answer": 2,
                "explanation": "Bir tomonli ichki burchaklarning yigʻindisi "
                               "180°: 180 − 65 = 115°. «65°» — bu mos "
                               "burchak, «25°» esa toʻldiruvchisi.",
            },
            {
                "text": "Shpal relsga perpendikulyar yotqizilgan boʻlsa, u "
                        "hosil qilgan burchaklar qanday boʻladi?",
                "choices": [
                    "Toʻrttasi ham 90°",
                    "Ikkitasi 90°, ikkitasi 180°",
                    "Ikkitasi 45°, ikkitasi 135°",
                    "Har xil — aniqlab boʻlmaydi",
                ],
                "answer": 0,
                "explanation": "Perpendikulyar degani 90° ostida kesishish. "
                               "Bitta burchak 90° boʻlsa, qoʻshnisi ham "
                               "180 − 90 = 90°, vertikallari ham 90° — "
                               "demak toʻrttasi ham teng.",
            },
        ],
        "body": """
<p>Bekzod birinchi marta poyezdda ketyapti. U deraza yonidagi joyni oldi va
tashqariga qaradi.</p>

<p>Relslar oldinga choʻzilgan. Uzoqda ular bir-biriga yaqinlashib, gorizontda
tutashib ketgandek koʻrinardi.</p>

<p>«Amaki, relslar u yerda birlashadimi?» — soʻradi u.</p>

<p>Karim amaki kuldi: «Birlashsa poyezd agʻdarilib ketardi. Ular
<span class="cn-word" data-tr="hech qachon kesishmaydigan chiziqlar">parallel</span> —
orasidagi masofa hamma joyda bir xil. Uzoqdagi narsa kichik koʻrinadi, xolos.»</p>

<p>Bekzod pastga qaradi. Relslar tagida yogʻoch shpallar yotardi, har biri
relslarni kesib oʻtardi. Har bir shpal — bitta
<span class="cn-word" data-tr="ikkala chiziqni ham kesib oʻtuvchi uchinchi chiziq">kesuvchi</span>.</p>

<p>Shpallar relslarga <span class="cn-word" data-tr="90° ostida kesishuvchi">perpendikulyar</span>
yotqizilgandi, shuning uchun hosil boʻlgan burchaklarning hammasi
<strong>90</strong>° edi.</p>

<p>Bekat yaqinida esa boshqa manzara chiqdi: qiya tayanch relslarni
<span class="cn-word" data-tr="burchak oʻlchov birligi">gradus</span>lab kesib
oʻtardi. Amaki uni <strong>65</strong>° deb chamaladi.</p>

<p>«Ikkinchi relsdagi burchak-chi?» — soʻradi Bekzod.</p>

<p>«Oʻsha yerda ikkita javob bor», — dedi amaki.
<span class="cn-word" data-tr="ikkala kesishishda bir xil oʻrinda turgan teng burchaklar">Mos burchak</span>
yana <strong>65</strong>°, chunki relslar parallel. Uning yonidagi,
relslar orasidagi
<span class="cn-word" data-tr="chiziqlar orasida, kesuvchining bir tomonida; yigʻindisi 180°">bir tomonli ichki burchak</span>
esa 180 − 65 = <strong>115</strong>°.</p>

<p>Bekzod daftariga chizib koʻrdi. Ikki rels orasidagi
<span class="cn-word" data-tr="ikki parallel chiziq orasidagi qism">ichki soha</span>da
toʻrtta burchak bor edi. Haqiqatan ham sakkizta
<span class="cn-word" data-tr="umumiy boshlangʻich nuqtali ikki nur">burchak</span>
hosil boʻlgan, lekin ularning faqat ikkita qiymati bor edi: 65° va 115°.</p>

<p>«Bitta oʻlchov — butun chizma», — dedi u. Amaki bosh irgʻadi: «Quruvchilar
ham shunday ishlaydi. Agar
<span class="cn-word" data-tr="chiziqlar orasida, kesuvchining har xil tomonlarida; teng">almashinuvchi ichki burchaklar</span>
teng chiqmasa, demak relslar
<span class="cn-word" data-tr="ikki chiziqning umumiy nuqtasi">kesishib</span>
ketyapti — va buni darhol tuzatish kerak.»</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-61 — uchburchak                                 ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Nega uchburchak eng mustahkam shakl",
        "summary": (
            "PM-61 matni. Ilmiy-ommabop: koʻprik fermalari, kran strelalari, "
            "tom yogʻochlari va elektr ustunlari — hammasida uchburchak bor. "
            "Sababi burchaklar yigʻindisi qoidasidan kelib chiqadi."
        ),
        "order":   61,
        "grammar": [
            {
                "pattern":  "uchta tomon uchburchakni bir qiymatli aniqlaydi",
                "meaning":  "Uchburchakning tomonlari berilsa, burchaklari "
                            "oʻz-oʻzidan aniqlanadi va oʻzgara olmaydi. "
                            "Shuning uchun uchburchakli ramka qiyshaymaydi.",
                "examples": [
                    "ferma burchaklari: 50° + 60° + 70° = 180°",
                    "teng tomonli uchburchak: 180 ÷ 3 = 60°",
                    "tom yogʻochi: 35° + 35° + 110° = 180°",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega toʻrt tomonli ramka qiyshayib ketadi?",
                "choices": [
                    "Yogʻochi ingichka boʻlgani uchun",
                    "Mixlari yetarli boʻlmagani uchun",
                    "Tomonlari oʻzgarmagan holda ham burchaklari oʻzgara olgani uchun",
                    "Toʻrtta burchakning yigʻindisi 180° boʻlmagani uchun",
                ],
                "answer": 2,
                "explanation": "Toʻrt tomonli ramkani bosganda tomonlar "
                               "uzunligi oʻzgarmaydi, lekin burchaklar "
                               "siljiydi. Uchburchakda esa bunga imkon "
                               "yoʻq — uchta tomon shaklini bir qiymatli "
                               "aniqlaydi.",
            },
            {
                "text": "Koʻprik fermasining ikki burchagi 50° va 60° boʻlsa, "
                        "uchinchisi qancha?",
                "choices": ["60°", "70°", "80°", "110°"],
                "answer": 1,
                "explanation": "Uchburchak burchaklarining yigʻindisi 180°: "
                               "180 − 50 − 60 = 70°. «110°» — ikki burchakning "
                               "yigʻindisi, ayirish bajarilmagan.",
            },
            {
                "text": "Tom yogʻochining pastki ikki burchagi 35° dan. "
                        "Tepadagi burchak qancha va bu qanday uchburchak?",
                "choices": [
                    "70°, oʻtkir burchakli",
                    "110°, oʻtkir burchakli",
                    "145°, oʻtmas burchakli",
                    "110°, oʻtmas burchakli",
                ],
                "answer": 3,
                "explanation": "Pastki ikkitasi birga 35 + 35 = 70°, demak "
                               "tepadagisi 180 − 70 = 110°. 110° > 90°, "
                               "shuning uchun uchburchak oʻtmas burchakli va "
                               "tom yassi chiqadi. «70°» — bu pastki "
                               "ikkitasining yigʻindisi.",
            },
        ],
        "body": """
<p>Koʻprikka, portal kranga, tom ostidagi yogʻochlarga yoki elektr uzatish
ustuniga qarang. Hammasida bitta shakl takrorlanadi:
<span class="cn-word" data-tr="uchta tomoni va uchta burchagi bor shakl">uchburchak</span>.</p>

<p>Bu did masalasi emas. Buni uyda tekshirish mumkin.</p>

<p>Toʻrtta yogʻoch tayoqchani uchlaridan mix bilan biriktiring — toʻrt tomonli
ramka chiqadi. Endi bir chetidan bosing: ramka qiyshayib, yonboshlab ketadi.
<span class="cn-word" data-tr="uchburchakning kesmalaridan biri">Tomon</span>lari
oʻzgarmadi, lekin <span class="cn-word" data-tr="umumiy uchdan chiqqan ikki nur orasidagi burilish">burchak</span>lari
oʻzgardi.</p>

<p>Endi uchta tayoqchadan uchburchak yasang va bosib koʻring. Qimirlamaydi.</p>

<p>Sababi oddiy: uchta tomon uzunligi berilsa, uchburchakning
<span class="cn-word" data-tr="uchburchakning ikki tomoni orasidagi burchak">ichki burchak</span>lari
oʻz-oʻzidan aniqlanadi. Boshqa shakl chiqarishning iloji yoʻq. Muhandislar buni
<b>qattiqlik</b> deb atashadi.</p>

<p>Shuning uchun koʻprik <b>fermasi</b> uchburchaklardan yigʻiladi. Har bir
uchburchakning <span class="cn-word" data-tr="uchta burchakning qoʻshilishi; har doim 180°">burchaklar yigʻindisi</span>
oʻzgarmas: masalan 50° + 60° + <strong>70</strong>° = 180°.</p>

<p>Elektr ustunlari koʻpincha
<span class="cn-word" data-tr="uchala tomoni teng uchburchak">teng tomonli uchburchak</span>lardan
tuziladi — ularning har bir burchagi <strong>60</strong>°, shuning uchun
kuch uchala tomonga barobar taqsimlanadi.</p>

<p>Tom yogʻochlari esa odatda
<span class="cn-word" data-tr="ikki tomoni teng uchburchak">teng yonli uchburchak</span>:
pastki ikki burchak teng, masalan 35° va 35°, tepasidagi esa
<strong>110</strong>°. Bunday uchburchak
<span class="cn-word" data-tr="bitta burchagi 90° dan katta">oʻtmas burchakli</span>
boʻladi va tom yassi chiqadi. Qorli joylarda tomni tikroq qilishadi — u holda
tepadagi burchak kichrayib, uchburchak
<span class="cn-word" data-tr="hamma burchagi 90° dan kichik">oʻtkir burchakli</span>ga
aylanadi.</p>

<p>Qaysi shaklni tanlash — hisob masalasi. Lekin uchburchakning oʻzini tanlash
allaqachon hal qilingan: u
<span class="cn-word" data-tr="uchala tomoni har xil uchburchak">turli tomonli</span>
boʻladimi yoki teng yonli — baribir qiyshaymaydi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-62 — uchburchak tengsizligi                            JUMBOQ
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Uch tayoq — uchburchak chiqadimi?",
        "summary": (
            "PM-62 matni. Jumboq: 12 sm lik tayoqni uch boʻlakka sindirishdi. "
            "Baʼzi boʻlaklardan uchburchak chiqdi, baʼzilaridan yoʻq — va "
            "bolalar qoidani oʻzlari topishdi."
        ),
        "order":   62,
        "grammar": [
            {
                "pattern":  "ikki qisqa boʻlak yigʻindisi eng uzunidan katta boʻlsin",
                "meaning":  "12 sm ni uchga boʻlganda eng uzun boʻlak "
                            "<b>6 sm dan kichik</b> boʻlishi shart — aks holda "
                            "qolgan ikkitasi uni tutashtira olmaydi.",
                "examples": [
                    "2 + 4 + 6: 2 + 4 = 6, kattaroq emas — chiqmaydi",
                    "1 + 2 + 9: 1 + 2 = 3 < 9 — chiqmaydi",
                    "3 + 4 + 5: 3 + 4 = 7 > 5 — chiqadi",
                    "eng uzun boʻlak < 12 ÷ 2 = 6",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega 2 sm, 4 sm va 6 sm li boʻlaklardan uchburchak "
                        "chiqmadi?",
                "choices": [
                    "Boʻlaklar juda kichik boʻlgani uchun",
                    "Ikki qisqasining yigʻindisi uzuniga aynan teng boʻlgani uchun",
                    "Boʻlaklar teng boʻlmagani uchun",
                    "Uchtasining yigʻindisi 12 dan kichik boʻlgani uchun",
                ],
                "answer": 1,
                "explanation": "2 + 4 = 6, bu esa uchinchi boʻlakka aynan "
                               "teng. Tayoqlar uzun tayoq ustiga yotib qoladi "
                               "va yassi chiziq hosil boʻladi — yigʻindi "
                               "qatʼiy katta boʻlishi shart.",
            },
            {
                "text": "3 sm, 4 sm va 5 sm li boʻlaklardan uchburchak "
                        "chiqadimi?",
                "choices": [
                    "Yoʻq, chunki 3 + 4 = 7 > 5",
                    "Yoʻq, chunki boʻlaklar teng emas",
                    "Ha, chunki 3 + 4 = 7 > 5",
                    "Aniqlab boʻlmaydi",
                ],
                "answer": 2,
                "explanation": "Eng qisqa ikkitasini qoʻshamiz: 3 + 4 = 7, bu "
                               "eng uzuni 5 dan katta. Demak tayoqlar yetadi "
                               "va uchburchak yopiladi.",
            },
            {
                "text": "12 sm lik tayoqdan uchburchak chiqishi uchun eng uzun "
                        "boʻlak qanday boʻlishi kerak?",
                "choices": [
                    "6 sm dan kichik",
                    "6 sm ga teng",
                    "6 sm dan katta",
                    "4 sm ga teng",
                ],
                "answer": 0,
                "explanation": "Eng uzun boʻlakni L desak, qolgan ikkitasi "
                               "birga 12 − L boʻladi. Shart: 12 − L > L, "
                               "yaʼni 12 > 2L va L < 6. Aynan shuning uchun "
                               "2 + 4 + 6 da uchburchak chiqmadi.",
            },
        ],
        "body": """
<p>Mehnat darsida Nodira opa har bir partaga <strong>12</strong> santimetrlik
yogʻoch tayoqcha tarqatdi.</p>

<p>«Tayoqchani uchga sindiring va uchala boʻlakdan
<span class="cn-word" data-tr="uchta tomoni va uchta burchagi bor shakl">uchburchak</span>
yasang», — dedi u.</p>

<p>Afsona tayoqchani 3, 4 va 5 sm qilib sindirdi. Uchburchak darrov chiqdi.</p>

<p>Jasur esa 2, 4 va 6 sm qilib sindirdi. Qancha urinmasin, boʻlaklar
yopilmadi — ular uzun boʻlak ustiga yotib qolaverdi.</p>

<p>Sherbekniki yanada yomon boʻldi: 1, 2 va 9 sm. Ikki qisqa boʻlak birga
atigi 3 sm, uzunining
<span class="cn-word" data-tr="kesmaning ikki uchidan biri">uch</span>lariga
yaqin ham kelmadi.</p>

<p>«Nega birida chiqdi, boshqasida yoʻq?» — soʻradi Nodira opa.</p>

<p>Bolalar sonlarni yozib chiqishdi. Afsonada 3 + 4 = <strong>7</strong>, bu
esa 5 dan katta. Jasurda 2 + 4 = <strong>6</strong> — uchinchi boʻlakka aynan
teng. Sherbekda 1 + 2 = <strong>3</strong>, bu 9 dan ancha kichik.</p>

<p>Shunday qilib ular
<span class="cn-word" data-tr="ikki tomon yigʻindisi uchinchisidan katta boʻlishi sharti">uchburchak tengsizligi</span>ni
oʻzlari topishdi: ikki qisqa
<span class="cn-word" data-tr="uchburchakning kesmalaridan biri">tomon</span>ning
<span class="cn-word" data-tr="qoʻshish natijasi">yigʻindisi</span>
eng uzunidan <b>katta</b> boʻlishi kerak. Teng ham yaramaydi — Jasurniki shuni
koʻrsatdi.</p>

<p>Uning shakli
<span class="cn-word" data-tr="uchala uchi bitta toʻgʻri chiziqda yotgan uchburchak">yassilangan uchburchak</span>
boʻlib qoldi, yaʼni umuman uchburchak emas. Demak belgisi
<span class="cn-word" data-tr="≥ emas, faqat &gt; belgisi ishlatiladi">qatʼiy tengsizlik</span>
boʻlishi shart.</p>

<p>Nodira opa yana bir savol berdi: «Ikki boʻlak 5 va 4 sm boʻlsa, uchinchisi
qanday <span class="cn-word" data-tr="qiymat tushishi mumkin boʻlgan chegaralar">oraliq</span>da
boʻlishi kerak?» Bolalar hisoblashdi: yuqori
<span class="cn-word" data-tr="oraliqning eng chetki qiymati">chegara</span> —
yigʻindi, 5 + 4 = 9; quyisi esa
<span class="cn-word" data-tr="ayirish natijasi">farq</span>, 5 − 4 = 1.
Demak 1 dan katta va 9 dan kichik.</p>

<p>Oxirida Afsona yanada qisqa qoida topdi. Uzunligi 12 sm boʻlgani uchun eng
uzun boʻlakni L desak, qolgan ikkitasi 12 − L boʻladi. Shart: 12 − L &gt; L,
yaʼni L &lt; <strong>6</strong>.</p>

<p>«Eng uzun boʻlak yarmidan qisqa boʻlsin», — dedi u. Uchta boʻlakni tekshirish
oʻrniga bitta savol qoldi.</p>
""",
    },
]
