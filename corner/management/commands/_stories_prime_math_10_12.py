# -*- coding: utf-8 -*-
"""Prime Math Readings — PM-10 … PM-12.

Toc: corner/management/commands/toc_prime_math_readings.txt
⛔ AUDIO YOʻQ.

Janr xilma-xilligi: 10 — hikoya (liftdagi sahna), 11 — doʻkondagi dialog
(daftar ustida), 12 — qadimiy rivoyatning qayta hikoyasi (tarix).

    python manage.py import_corner \\
        corner/management/commands/_stories_prime_math_10_12.py --author=prime
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
    # PM-10 — manfiy sonlarni qoʻshish va ayirish        HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Lift, qavatlar va yertoʻla",
        "summary": (
            "PM-10 matni. Yangi uydagi lift tugmalari tik turgan son oʻqiga oʻxshaydi: "
            "yuqorida musbat qavatlar, pastda manfiy yertoʻlalar, orasida nol."
        ),
        "order":   10,
        "grammar": [
            {
                "pattern":  "Yuqoriga — qoʻshish, pastga — ayirish",
                "meaning":  "Yer sathini nol deb olsak, har bir qavat son oʻqidagi bir "
                            "qadamga aylanadi. Yuqoriga chiqish musbat son qoʻshish, "
                            "pastga tushish esa ayirish demakdir.",
                "examples": [
                    "3 − 5 = −2 (uchinchi qavatdan besh qavat pastga)",
                    "−2 + 7 = 5 (ikkinchi yertoʻladan yetti qavat yuqoriga)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Bekzod nima uchun yertoʻlaga tushdi?",
                "choices": [
                    "Qoʻshnisini kutish uchun",
                    "Liftni sinab koʻrish uchun",
                    "Velosipedini olib chiqish uchun",
                    "Dilnozaning uyiga borish uchun",
                ],
                "answer": 2,
                "explanation": "Velosipedi ikkinchi yertoʻladagi omborxonada turardi.",
            },
            {
                "text": "Bekzod uchinchi qavatdan besh qavat pastga tushdi. Qaysi "
                        "qavatga keldi?",
                "choices": ["−2", "−1", "1", "2"],
                "answer": 0,
                "explanation": "3 − 5 = −2. Nolgacha uchta qadam ketdi, qolgan ikki "
                               "qadam uni nolning pastiga olib tushdi.",
            },
            {
                "text": "Ikkinchi yertoʻladan yetti qavat yuqoriga koʻtarilsa, lift "
                        "qaysi qavatda toʻxtaydi?",
                "choices": ["3", "5", "7", "9"],
                "answer": 1,
                "explanation": "−2 + 7 = 5. Nolgacha ikki qadam, undan keyin yana besh "
                               "qadam yuqoriga — beshinchi qavat.",
            },
        ],
        "body": """
<p>Bekzodlar yangi uyga koʻchib kelishdi. Liftga birinchi marta kirgan Dilnoza
tugmalarga qaradi-yu, kulib yubordi: «Bu lift bizning matematika daftarimizga
oʻxshaydi!»</p>

<p>Tugmalar ustma-ust turardi: 9, 8, 7 … 2, 1, keyin <b>0</b>, undan pastda esa
<b>−1</b> va <b>−2</b>. Nol — yer sathi, koʻchaga chiqadigan eshik. Undan yuqorisi
<span class="cn-word" data-tr="noldan katta son">musbat son</span>lar, pastdagi ikki
qavat esa <span class="cn-word" data-tr="noldan kichik son">manfiy son</span>lar bilan
belgilangan. Butun lift tik turgan
<span class="cn-word" data-tr="sonlar tartib bilan joylashgan chiziq">son oʻqi</span> edi.</p>

<p>Bekzod uchinchi qavatda yashaydi. U velosipedini ikkinchi yertoʻladagi omborxonada
qoldirgan edi. Liftga chiqib, besh qavat pastga tushdi: <strong>3 − 5 = −2</strong>.
Eshik ochilganda chiroq xira, havo salqin edi — velosiped joyida turardi.</p>

<p>«Qara, — dedi Bekzod telefonidagi hisobni koʻrsatib, — nolgacha uchta qadam bor edi,
menda esa beshta qadam. Ikkitasi ortdi va oʻsha ikkitasi meni noldan pastga olib
tushdi.» Bu yerda <span class="cn-word" data-tr="sonning oldidagi + yoki − belgisi">ishora</span>
yoʻnalishni aytardi, qadamlar soni esa masofani.</p>

<p>Keyin ikkalasi Dilnozaning uyiga chiqishdi. U beshinchi qavatda yashaydi, demak
yertoʻladan yetti qavat yuqoriga: <strong>−2 + 7 = 5</strong>. Bu safar musbat qadamlar
koʻp edi, shuning uchun
<span class="cn-word" data-tr="qoʻshish natijasi">yigʻindi</span> ham musbat chiqdi.</p>

<p>«Demak, — dedi Dilnoza liftdan chiqarkan, — pastga tushish
<span class="cn-word" data-tr="ayirish natijasi">ayirma</span>, yuqoriga chiqish
qoʻshish. Faqat 3 va −3 ni adashtirmaslik kerak: ular
<span class="cn-word" data-tr="noldan bir xil uzoqlikdagi, ishorasi teskari sonlar">qarama-qarshi sonlar</span>,
biri uchinchi qavat, ikkinchisi esa — agar bu uyda boʻlganda — uchinchi yertoʻla.»</p>

<p>Shu kuni lift ikkalasiga bir soatlik darsdan koʻra koʻproq narsa oʻrgatdi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-11 — koʻpaytirish va boʻlish                    DOʻKONDAGI DIALOG
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Doʻkon daftaridagi qarz",
        "summary": (
            "PM-11 matni. Karim akaning eski daftarida har kunlik qarz yozib boriladi. "
            "Bir xil qarz olti kun takrorlansa — bu koʻpaytirish, faqat manfiy tomonga."
        ),
        "order":   11,
        "grammar": [
            {
                "pattern":  "manfiy × musbat = manfiy · manfiy ÷ musbat = manfiy",
                "meaning":  "Bir xil qarz bir necha marta takrorlansa, jami qarzni "
                            "koʻpaytirish bilan topamiz. Qarzni bir necha kishiga teng "
                            "boʻlsak, boʻlish ham manfiy javob beradi — chunki har "
                            "kimga tegadigani baribir qarz.",
                "examples": [
                    "6 × (−2 500) = −15 000 (olti kunlik jami qarz)",
                    "−15 000 ÷ 3 = −5 000 (uch aka-ukaga teng boʻlinganda)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Karim aka daftariga nima yozib boradi?",
                "choices": [
                    "Har kuni sotilgan nonlar sonini",
                    "Pulsiz olingan mahsulotlarni — qarzni",
                    "Doʻkonning kunlik foydasini",
                    "Mahalladagi bolalarning ismlarini",
                ],
                "answer": 1,
                "explanation": "Kimdir pulsiz kelsa, Karim aka olingan narsani daftarga "
                               "yozib qoʻyadi — bu qarz daftari.",
            },
            {
                "text": "Sherbek olti kun ketma-ket 2 500 soʻmdan qarzga non oldi. "
                        "Jami qarz qancha?",
                "choices": ["−15 000 soʻm", "−12 500 soʻm", "−2 500 soʻm", "15 000 soʻm"],
                "answer": 0,
                "explanation": "6 × (−2 500) = −15 000. Manfiyni musbatga "
                               "koʻpaytirganda javob manfiy chiqadi — bu 15 000 soʻm "
                               "qarz.",
            },
            {
                "text": "Uch aka-uka jami qarzni oʻzaro teng boʻlishdi. Har biriga "
                        "qancha tushdi?",
                "choices": ["−15 000 soʻm", "−7 500 soʻm", "−5 000 soʻm", "−2 500 soʻm"],
                "answer": 2,
                "explanation": "−15 000 ÷ 3 = −5 000. Ishoralar har xil, demak "
                               "boʻlinma manfiy: har biriga 5 000 soʻm qarz.",
            },
        ],
        "body": """
<p>Karim akaning doʻkonida kassa yonida eski daftar turadi. Muqovasi yirtilgan, sahifalari
sargʻaygan. Kimdir pulsiz kelsa, u olingan narsani shu daftarga yozib qoʻyadi — mahallada
buni «qarz daftari» deyishadi.</p>

<p>Payshanba kuni Sherbek doʻkonga kirdi.</p>

<p>— Karim aka, otam kelib berib ketadi.</p>

<p>— Mayli, oʻgʻlim. Bugun ham nonmi?</p>

<p>Karim aka daftarni ochdi va barmogʻi bilan ustunni pastga yurgizdi. Sherbekning nomi
ostida bir xil son olti marta takrorlangan edi: har kuni <b>2 500 soʻm</b>.</p>

<p>— Qara, — dedi u kulib, — olti kun, har kuni ikki yarim ming. Buni birma-bir
qoʻshib oʻtirmaymiz. Bitta
<span class="cn-word" data-tr="bir sonni ikkinchisiga necha marta takrorlab qoʻshish amali">koʻpaytirish</span>
yetadi: <strong>6 × (−2 500) = −15 000</strong>.</p>

<p>Sherbek soʻradi: «Nega minus?»</p>

<p>— Chunki bu pul senda emas, mendan olingan. Daftarda pul emas,
<span class="cn-word" data-tr="manfiy son bilan yoziladigan yetishmovchilik">qarz</span>
turibdi. <span class="cn-word" data-tr="sonning oldidagi + yoki − belgisi">Ishora</span>
tomonni aytadi: musbat — kirim, manfiy — chiqim. Sonlarni ishorasiz koʻpaytiramiz, keyin
ishorani qoʻyamiz. Bir <span class="cn-word" data-tr="koʻpaytirilayotgan sonlarning biri">koʻpaytuvchi</span>
manfiy boʻlsa, <span class="cn-word" data-tr="koʻpaytirish natijasi">koʻpaytma</span> ham
manfiy chiqadi.</p>

<p>Kechqurun Sherbekning ikki akasi keldi. Uchalasi qarzni oʻzaro
<span class="cn-word" data-tr="bir xil ulushlarga ajratish">teng boʻlish</span>ga kelishdi.
Karim aka yana daftarga egildi: <strong>−15 000 ÷ 3 = −5 000</strong>.</p>

<p>— Ana, — dedi u, — har biringizga besh mingdan. <span class="cn-word" data-tr="boʻlish natijasi">Boʻlinma</span>
ham manfiy, chunki boʻlingani — foyda emas, qarz.</p>

<p>Ertasi kuni uchalasi beshtadan ming soʻm keltirdi. Karim aka daftardagi qatorni
chizib tashladi va sahifada nol qoldi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PM-12 — daraja                                     TARIX / RIVOYAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Shaxmat taxtasidagi bugʻdoy",
        "summary": (
            "PM-12 matni. Qadimiy rivoyatning qayta hikoyasi: shoh oddiy tuyulgan "
            "soʻrovga rozi boʻldi — har katakda donni ikkilantirish. Daraja qanchalik "
            "tez oʻsishini shundan yaxshiroq koʻrsatadigan misol yoʻq."
        ),
        "order":   12,
        "grammar": [
            {
                "pattern":  "Ikkilanish — 2ⁿ",
                "meaning":  "Son har qadamda ikki baravar ortsa, n qadamdan keyin u "
                            "2 ning n-darajasiga koʻpayadi. Shaxmat taxtasida birinchi "
                            "katakda 1 don boʻlgani uchun n-katakdagi donlar soni "
                            "2 ning (n − 1)-darajasiga teng.",
                "examples": [
                    "8-katak: 2⁷ = 128 don",
                    "Dastlabki 4 katak jami: 1 + 2 + 4 + 8 = 15 = 2⁴ − 1",
                ],
            },
        ],
        "open_question": (
            "Oxirgi — 64-katakdagi donlar oldingi 63 ta katakdagi donlarning "
            "hammasidan koʻpmi, kammi, yoki tengmi?"
        ),
        "questions": [
            {
                "text": "Rivoyatga koʻra, shoh nima uchun vaʼdasini bajara olmadi?",
                "choices": [
                    "Shaxmat taxtasi juda kichkina edi",
                    "Ixtirochi soʻrovidan voz kechdi",
                    "Xazinada oltin yetmadi",
                    "Soʻralgan don miqdori butun mamlakatdagidan koʻp edi",
                ],
                "answer": 3,
                "explanation": "Ikkilanish shu qadar tez oʻsadiki, oxirgi kataklarga "
                               "yetganda son butun dunyodagi hosildan oshib ketadi.",
            },
            {
                "text": "Sakkizinchi katakda nechta don boʻladi?",
                "choices": ["16", "64", "128", "256"],
                "answer": 2,
                "explanation": "Birinchi katakda 1 don, keyin har katakda ikkilanadi: "
                               "1, 2, 4, 8, 16, 32, 64, 128. Sakkizinchisi — "
                               "2<sup>7</sup> = 128.",
            },
            {
                "text": "Dastlabki toʻrtta katakdagi donlar jami nechta?",
                "choices": ["8", "15", "16", "32"],
                "answer": 1,
                "explanation": "1 + 2 + 4 + 8 = 15. Diqqat qiling: bu keyingi "
                               "katakdagi sondan (16 dan) roppa-rosa bittaga kam.",
            },
        ],
        "body": """
<p>Rivoyatga koʻra, qadimgi Hindistonda bir donishmand shohga yangi oʻyin — shaxmatni
koʻrsatibdi. Shoh oʻyinni shu qadar yoqtiribdiki, ixtirochiga: «Nima tilasang soʻra»,
debdi.</p>

<p>Donishmand kamtarona javob beribdi: «Taxtaning birinchi katagiga bitta bugʻdoy doni
qoʻying. Ikkinchisiga ikkita, uchinchisiga toʻrtta — har katakda oldingisidan ikki
baravar koʻp. Shu yoʻl bilan oltmish toʻrtinchi katakkacha.»</p>

<p>Shoh kulib yuboribdi. Bir hovuch don-ku bu!</p>

<p>Lekin <span class="cn-word" data-tr="har qadamda ikki baravar ortish">ikkilanish</span>
odamning tasavvuridan tezroq yuradi. Sakkizinchi katakda allaqachon
<strong>2<sup>7</sup> = 128</strong> don bor edi. Yigirma birinchi katakda son bir
milliondan oshdi. Oltmish toʻrtinchi katakdagi donlar soni esa 19
<span class="cn-word" data-tr="sondagi raqamlar soni; masalan 128 — uch xonali son">xonali son</span>
edi.</p>

<p>Bu yerda <span class="cn-word" data-tr="bir sonni oʻziga qayta-qayta koʻpaytirish yozuvi">daraja</span>
yozuvi qoʻl keladi. <span class="cn-word" data-tr="darajada koʻpaytirilayotgan son">Asos</span>
— 2, chunki har qadamda ikkiga koʻpaytiramiz;
<span class="cn-word" data-tr="necha marta koʻpaytirilishini bildiruvchi kichik son">koʻrsatkich</span>
esa nechanchi qadamda ekanimizni aytadi. Butun taxtadagi donlarning
<span class="cn-word" data-tr="qoʻshish natijasi">yigʻindi</span>si
<strong>2<sup>64</sup> − 1</strong> ga teng — yaʼni 18
<span class="cn-word" data-tr="bir va oʻn sakkizta nol: 10 ning 18-darajasi">kvintillion</span>dan
ortiq don.</p>

<p>Bugungi jahon hosili bilan hisoblaganda ham bunday
<span class="cn-word" data-tr="koʻpaytirish natijasi">koʻpaytma</span>ni yigʻish uchun
ming yillardan ortiq vaqt kerak boʻlardi. Shoh vaʼdasini bajara olmagan.</p>

<p>Rivoyatning oxiri turli kitoblarda turlicha aytiladi. Ammo matematik saboq bitta:
qoʻshib borish sekin oʻsadi, ikkilanish esa portlaydi. Shuning uchun ham daraja atigi
ikki belgi bilan yoziladi — aks holda uni yozishga qogʻoz yetmasdi.</p>
""",
    },
]
