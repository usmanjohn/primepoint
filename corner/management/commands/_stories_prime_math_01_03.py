# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-1 … PM-3.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ — formula va sonlar ovozda oʻqilmaydi.

Janr xilma-xilligi: 1 — doʻkondagi sahna (hikoya), 2 — kundalik daftar,
3 — omborda ish kuni (hikoya).

cn-word bu toʻplamda ATAMA: data-tr — oʻzbekcha qisqa taʼrif, tarjima emas.
grammar bloki — matnda ishlatilgan QOIDA/FORMULA.

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_01_03.py --author=prime
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
    # PM-1 — razryadlar                     DOʻKONDAGI SAHNA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Narxdagi nollar",
        "summary": (
            "PM-1 matni. Sherbek doʻkonda ikkita narxni bir xil deb oʻylaydi — "
            "raqamlari ham bir xil-ku. Dadasi unga sonni sinflarga ajratib "
            "oʻqishni koʻrsatadi."
        ),
        "order":   1,
        "grammar": [
            {
                "pattern":  "Sonni oʻngdan uchtalik sinflarga ajratib oʻqing",
                "meaning":  "Har uchta razryad bitta sinfni hosil qiladi: birliklar, "
                            "minglar, millionlar. Avval boʻshliqlarni qoʻying, keyin "
                            "oʻqing — shunda katta son adashtirmaydi.",
                "examples": [
                    "2 350 000 → 2 | 350 | 000 → ikki million uch yuz ellik ming",
                    "235 000 → 235 | 000 → ikki yuz oʻttiz besh ming",
                ],
            },
            {
                "pattern":  "Bitta nol — 10 marta",
                "meaning":  "Son oxiriga bitta nol qoʻshilsa, har bir raqam bitta "
                            "razryad chapga suriladi. Har bir razryad esa 10 marta "
                            "ogʻirroq, shuning uchun butun son 10 marta kattalashadi.",
                "examples": ["235 000 × 10 = 2 350 000"],
            },
        ],
        "questions": [
            {
                "text": "Sherbek nega ikkala telefonning narxini bir xil deb oʻyladi?",
                "choices": [
                    "Telefonlar bir xil koʻrinar edi",
                    "Dadasi shunday degan edi",
                    "Narxlardagi raqamlar bir xil edi: 2, 3, 5",
                    "Ikkala yorliqda ham bir xil son yozilgan edi",
                ],
                "answer": 2,
                "explanation": "Sherbek raqamlarga qaradi, ularning <b>razryadiga</b> "
                               "emas. 2, 3, 5 raqamlari ikkala narxda ham bor, lekin "
                               "birinchi narxda ular bittadan razryad chapda turibdi.",
            },
            {
                "text": "Qimmat telefon arzoniga qaraganda necha marta qimmat?",
                "choices": ["2 marta", "5 marta", "10 marta", "100 marta"],
                "answer": 2,
                "explanation": "2 350 000 va 235 000 — farq bitta nolda. "
                               "235 000 × 10 = 2 350 000, demak <b>10 marta</b>. "
                               "Har bir raqam bitta razryad chapga surilgan.",
            },
            {
                "text": "2 350 000 sonida 3 raqami qaysi razryadda turibdi?",
                "choices": ["Minglik", "Oʻn minglik", "Yuz minglik", "Million"],
                "answer": 2,
                "explanation": "Oʻngdan sanaymiz: 0 — birlik, 0 — oʻnlik, 0 — yuzlik, "
                               "0 — minglik, 5 — oʻn minglik, <b>3 — yuz minglik</b>, "
                               "2 — million. Demak 3 ning qiymati 300 000.",
            },
        ],
        "body": """
<p>Sherbek dadasi bilan telefon doʻkoniga kirdi. Peshtaxtada ikkita telefon yonma-yon
turardi.</p>

<p>Birinchisining yorligʻida <strong>2 350 000</strong> soʻm, ikkinchisinikida
<strong>235 000</strong> soʻm deb yozilgan edi.</p>

<p>— Ikkalasining narxi deyarli bir xil-ku, — dedi Sherbek. — Qarang,
<span class="cn-word" data-tr="0 dan 9 gacha boʻlgan belgi">raqam</span>lari bir xil:
2, 3, 5.</p>

<p>Dadasi kulib qoʻydi.</p>

<p>— Raqamlar bir xil, lekin ularning
<span class="cn-word" data-tr="raqamning sondagi oʻrni va vazni">razryad</span>i boshqacha,
— dedi u. — <span class="cn-word" data-tr="raqamlardan yozilgan miqdor">son</span>ni
oʻngdan boshlab uchtalikka ajratib koʻr.</p>

<p>Sherbek barmogʻi bilan boʻshliqlarni koʻrsatdi. Har uchtalik — bitta
<span class="cn-word" data-tr="sondagi uchtalik guruh: birliklar, minglar, millionlar">sinf</span>
ekan.</p>

<p>— Birinchisi ikki <span class="cn-word" data-tr="ming ming, yaʼni 1 000 000">million</span>
uch yuz ellik ming, ikkinchisi esa ikki yuz oʻttiz besh ming, — dedi u sekin. — Demak
birinchisi <strong>10 marta</strong> qimmat.</p>

<p>— Mana endi toʻgʻri oʻqiding, — dedi dadasi. — Doʻkonda odamlar eng koʻp shu xatoga
aldanadi. Narxni oʻqishda birinchi ish —
<span class="cn-word" data-tr="qaysi son katta ekanini aniqlash">taqqoslash</span> emas,
<span class="cn-word" data-tr="sonni razryadlarga ajratib yozish: 2 350 000 = 2 000 000 + 300 000 + 50 000">yoyilma yozuv</span>ni
koʻrish.</p>

<p>Sherbek arzonrogʻini tanladi. Uydagi hisob daftariga esa oʻsha kuni bitta qator yozib
qoʻydi: <em>«Bitta nol — oʻn marta.»</em></p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-2 — qoʻshish va ayirish            KUNDALIK DAFTAR
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Sinf kassasi",
        "summary": (
            "PM-2 matni. Dilnoza sinf kassasining daftarini yuritadi. Uch kunlik "
            "yozuvda kirim, chiqim va qoldiq qanday hisoblanishi koʻrinadi."
        ),
        "order":   2,
        "grammar": [
            {
                "pattern":  "qoldiq = bor edi − sarflandi + qoʻshildi",
                "meaning":  "Kassa masalasida amallar hodisalar tartibida bajariladi: "
                            "avval nima boʻlgan boʻlsa, avval oʻsha hisoblanadi.",
                "examples": [
                    "85 000 − 47 500 = 37 500",
                    "37 500 + 30 000 = 67 500",
                ],
            },
            {
                "pattern":  "Ayirmani qoʻshish bilan tekshiring",
                "meaning":  "Ayirma + ayiriluvchi = kamayuvchi. Bu tekshiruv ikki "
                            "soniya vaqt oladi va xatoning yarmini tutib qoladi.",
                "examples": ["37 500 + 47 500 = 85 000 ✓"],
            },
        ],
        "questions": [
            {
                "text": "Dilnoza nima uchun har bir harakatni daftarga yozib boradi?",
                "choices": [
                    "Sinfdoshlari undan shuni talab qilgani uchun",
                    "Pul qayerga ketganini aniq koʻrsata olishi uchun",
                    "Daftar yozuvi baholanadigani uchun",
                    "Kalkulyatori boʻlmagani uchun",
                ],
                "answer": 1,
                "explanation": "Matnda aytilgan: har bir kirim va chiqim yozilsa, "
                               "qoldiqni istalgan payt tekshirish mumkin.",
            },
            {
                "text": "Shar va shirinlik olingandan keyin kassada qancha pul qolgan edi?",
                "choices": ["42 500 soʻm", "47 500 soʻm", "37 500 soʻm", "67 500 soʻm"],
                "answer": 2,
                "explanation": "85 000 − 47 500 = <b>37 500</b> soʻm. Tekshiruv: "
                               "37 500 + 47 500 = 85 000 ✓",
            },
            {
                "text": "Uchinchi kun oxirida kassada qancha pul bor?",
                "choices": ["115 000 soʻm", "37 500 soʻm", "62 500 soʻm", "67 500 soʻm"],
                "answer": 3,
                "explanation": "Qoldiqqa ota-onalarning puli qoʻshiladi: "
                               "37 500 + 30 000 = <b>67 500</b> soʻm. 115 000 — bu "
                               "umumiy kirim (85 000 + 30 000), qoldiq emas.",
            },
        ],
        "body": """
<p><strong>1-kun.</strong> Bugun sinf kassasini menga topshirishdi. Sanab chiqdim:
<strong>85 000</strong> soʻm. Daftarning birinchi qatoriga shuni yozdim. Nodira opa
aytdi: har bir <span class="cn-word" data-tr="kassaga tushgan pul">kirim</span> va
<span class="cn-word" data-tr="kassadan chiqqan pul">chiqim</span> yozilib borsa,
<span class="cn-word" data-tr="hisobdan keyin qolgan pul">qoldiq</span>ni istalgan payt
tekshirish mumkin ekan.</p>

<p><strong>2-kun.</strong> Bayramga tayyorgarlik. Shar va shirinlikka
<strong>47 500</strong> soʻm ketdi. Uyda ustunda yozib hisobladim:</p>

<p>85 000 − 47 500 = <strong>37 500</strong>.</p>

<p>Birliklardan
<span class="cn-word" data-tr="chapdagi razryaddan bitta birlik olish">qarz olish</span>
kerak boʻldi, chunki 0 dan 5 ni ayirib boʻlmaydi. Keyin
<span class="cn-word" data-tr="ayirish natijasi">ayirma</span>ni qoʻshish bilan
tekshirdim: 37 500 + 47 500 = 85 000. Toʻgʻri.</p>

<p><strong>3-kun.</strong> Ota-onalar yigʻilishdan keyin yana <strong>30 000</strong> soʻm
qoʻshildi. Bu safar ogʻzaki hisobladim: 37 500 ga avval 30 000 ni qoʻshdim —
<strong>67 500</strong>. Sardor ishonmadi, kalkulyatorda tekshirdi. Bir xil chiqdi.</p>

<p>Ertalab Nodira opa soʻradi: «Kassada qancha bor?» Men daftarni ochib, uch qatorni
koʻrsatdim. Opa bir qarab: «Toʻgʻri, chunki
<span class="cn-word" data-tr="kirimlarning umumiy soni">yigʻindi</span> 115 000, xarajat
47 500, farqi ham 67 500», — dedi. Demak bir xil javobga ikki xil yoʻldan kelish mumkin
ekan.</p>

<p>Bugun bir narsani tushundim: eng foydali odat —
<span class="cn-word" data-tr="javobning kattaligini oldindan chamalash">taxminiy hisob</span>.
Kassada 85 mingga yaqin pul bor edi, yarmi sarflandi, keyin 30 ming qoʻshildi — javob
70 ming atrofida chiqishi kerak edi. Chiqdi ham.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-3 — koʻpaytirish                   OMBORDA BIR KUN
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bir qutida nechta?",
        "summary": (
            "PM-3 matni. Bekzod omborda choynaklarni bittalab sanab adashadi. "
            "Usta unga koʻpaytirish nima uchun oʻylab topilganini koʻrsatadi."
        ),
        "order":   3,
        "grammar": [
            {
                "pattern":  "«har birida … tadan» → koʻpaytirish",
                "meaning":  "Matnda bir xil miqdor takrorlansa, qoʻshish oʻrniga "
                            "koʻpaytirish ishlatiladi. Bu — matnli masalada eng koʻp "
                            "uchraydigan ishora.",
                "examples": [
                    "6 yashik × 24 ta = 144 ta",
                    "6 × 24 = 6 × 20 + 6 × 4 = 120 + 24 = 144",
                ],
            },
            {
                "pattern":  "Yakka qolganlarni oxirida qoʻshing",
                "meaning":  "Koʻpaytmaga kirmagan qism alohida qoʻshiladi. Masalaning "
                            "oxirgi jumlasini oʻqimaslik — eng koʻp uchraydigan xato.",
                "examples": ["144 + 3 = 147"],
            },
        ],
        "questions": [
            {
                "text": "Bekzod nega sanashni ikki marta boshlashga majbur boʻldi?",
                "choices": [
                    "Yashiklar sonini bilmasdi",
                    "Daftarini yoʻqotib qoʻydi",
                    "Bittalab sanayotib adashib ketdi",
                    "Usta unga boshqa ish topshirdi",
                ],
                "answer": 2,
                "explanation": "Bir xil sonni koʻp marta qoʻshish uzoq va xavfli — "
                               "koʻpaytirish aynan shuning uchun oʻylab topilgan.",
            },
            {
                "text": "Omborda jami nechta choynak bor?",
                "choices": ["144 ta", "147 ta", "150 ta", "33 ta"],
                "answer": 1,
                "explanation": "6 × 24 = 144 — yashiklardagilar. Yakka turgan 3 tasini "
                               "qoʻshamiz: 144 + 3 = <b>147</b>. 144 — oxirgi jumlani "
                               "oʻqimaganda chiqadigan javob.",
            },
            {
                "text": "Ertaga yana bitta toʻla yashik kelsa, omborda nechta choynak boʻladi?",
                "choices": ["151 ta", "168 ta", "174 ta", "171 ta"],
                "answer": 3,
                "explanation": "Toʻla yashikda 24 ta bor: 147 + 24 = <b>171</b>. "
                               "168 — yakka turgan 3 ta hisobga olinmagan javob.",
            },
        ],
        "body": """
<p>Bekzod yozgi taʼtilda amakisining omborida ishladi. Birinchi vazifa oddiy edi:
choynaklarni sanash.</p>

<p>Omborda oltita yashik turardi, har birida yigirma toʻrttadan choynak. Bekzod bittalab
sanay boshladi: 24, 48, 72… Uchinchi yashikda kimdir uni chaqirdi va u adashib ketdi.
Boshidan sanadi. Yana adashdi.</p>

<p>Usta Karim aka kulib, qogʻoz uzatdi.</p>

<p>— Bir xil sonni takror qoʻshayapsan-ku, — dedi u. — Buning qisqa yoʻli bor. U
<span class="cn-word" data-tr="bir xil sonni takror qoʻshishning qisqa yoʻli">koʻpaytirish</span>
deyiladi.</p>

<p>Qogʻozda ikkita
<span class="cn-word" data-tr="koʻpaytirilayotgan sonlar">koʻpaytuvchi</span> paydo
boʻldi: 6 va 24. Karim aka ularni ikki boʻlakka ajratdi:</p>

<p>6 × 24 = 6 × 20 + 6 × 4 = 120 + 24 = <strong>144</strong>.</p>

<p>— Bu <span class="cn-word" data-tr="koʻpaytirish natijasi">koʻpaytma</span>, —
dedi u. — Endi taxminni tekshir: 24 yigirma beshga yaqin, 25 ta oltitadan — 150.
Bizda 144 chiqdi, demak
<span class="cn-word" data-tr="raqamning sondagi oʻrni">razryad</span>da xato yoʻq.</p>

<p>Bekzod qogʻozga «144» deb yozib qoʻydi va omborni aylanib chiqdi. Burchakda yana uchta
choynak turardi — ular hech qaysi yashikka sigʻmagan ekan.</p>

<p>— Unda jami 144 emas, — dedi Bekzod. — 144 + 3 = <strong>147</strong>.</p>

<p>— Mana buni ish deydilar, — dedi Karim aka. — Koʻpchilik oxirgi jumlani oʻqimaydi.
<span class="cn-word" data-tr="masalada berilgan barcha maʼlumot">Shart</span>ni
oxirigacha oʻqigan odam esa doim toʻgʻri javob beradi.</p>
""",
    },
]
