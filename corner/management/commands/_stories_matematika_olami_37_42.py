# -*- coding: utf-8 -*-
"""Matematika olami — 32, 34, 35, 39, 40 va 42-matnlar (shelfning oxirgisi).

Toc: corner/management/commands/toc_matematika_olami.txt
  32. Telefoningiz xabarni qanday yashiradi                 (kundalik)
  34. Koʻprikdan oʻtish: toʻrt kishi, bitta fonar           (jumboq)
  35. Kyonigsberg koʻpriklari: bir chiziq bilan chizib boʻladimi (jumboq)
  39. Boʻri, echki va karam — daryodan oʻtish               (jumboq)
  40. Yolgʻonchilar oroli: kim rost gapiryapti              (jumboq)
  42. Cheksizlik bir xil emas: sanaladigan va sanalmaydigan (jumboq)
⛔ AUDIO YOʻQ.

FAKTLAR (tekshirilgan; jumboq javoblari scratchpad skriptida brute force/BFS
bilan topilgan):
  • Sezar shifri (Svetoniy): har harf 3 ga suriladi. OTA → RWD. 26 harfli
    alifboda 25 ta foydali kalit. Diffi–Xellman 1976, RSA 1977 (Rivest,
    Shamir, Adleman). 61 × 67 = 4087.
  • Fonar: 1, 2, 5, 10 daqiqa → eng kami 17 (Dijkstra). Oddiy usul
    (eng tez hammani kuzatadi): 10 + 1 + 5 + 1 + 2 = 19.
  • Kyonigsberg: 7 koʻprik, quruqliklar darajalari 5, 3, 3, 3. Eyler 1736.
    Yoʻl mavjud ⇔ toq darajali nuqtalar 0 yoki 2 ta. «Uycha» (kvadrat +
    diagonallar + tom): darajalar 3, 3, 4, 4, 2 → pastki burchakdan boshlash.
    Bugungi Kaliningradda koʻpriklarning bir qismi urushda vayron boʻlgan.
  • Boʻri–echki–karam: Alkuin (Alcuin of York), ~800-yil, «Yoshlarni
    charxlash uchun masalalar». Eng kami 7 marta oʻtish (BFS).
  • Rostgoʻy/yolgʻonchi: Raymond Smallian (1919–2017), «Bu kitobning nomi
    nima?» (1978). «Ikkalamiz ham yolgʻonchimiz» → A yolgʻonchi, B rostgoʻy
    (yagona izchil holat). Ichma-ich savol ikkala turda ham haqiqatni beradi.
  • Kantor 1845–1918; 1874 birinchi isbot, diagonal usul 1891. Hilbert 1926:
    «Kantor yaratgan jannatdan bizni hech kim haydab chiqara olmaydi».

    python manage.py import_corner \\
        corner/management/commands/_stories_matematika_olami_37_42.py --author=prime
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
    # 32 — shifrlash
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Telefoningiz xabarni qanday yashiradi",
        "summary": (
            "Sezar shifridan ochiq qulfgacha: notanish odam bilan butun dunyo "
            "eshitib turgan holda qanday sir saqlash mumkin? Javob — bir tomonga "
            "oson, orqaga juda qiyin hisob."
        ),
        "order":   32,
        "grammar": [
            {
                "pattern":  "Bir tomonlama hisob: koʻpaytirish oson, ajratish qiyin",
                "meaning":  "Ikki tub sonni koʻpaytirish bir zumlik ish. Natijadan "
                            "esa oʻsha ikki sonni topish juda qiyin — sonlar yuzlab "
                            "xonali boʻlsa, eng kuchli kompyuterlarga ham juda koʻp "
                            "vaqt kerak boʻladi. Ochiq kalitli shifrlash shu farqqa "
                            "tayanadi.",
                "examples": [
                    "Oson: 61 × 67 = 4087",
                    "Qiyin: 4087 = ? × ? (javob 61 va 67 ni topish uchun koʻp sinash kerak)",
                ],
            },
        ],
        "questions": [
            {
                "text": "Sezar shifrida har bir harf 3 ga surilsa, «OTA» soʻzi "
                        "qanday yoziladi?",
                "choices": ["RWD", "PUB", "QVC", "LQX"],
                "answer": 0,
                "explanation": "O → R, T → W, A → D. Natija: RWD.",
            },
            {
                "text": "Nega Sezar shifri bugun xavfsiz emas?",
                "choices": [
                    "Uni faqat rimliklar tushunadi",
                    "Harflar juda katta",
                    "Kompyuter uni telefonda koʻrsata olmaydi",
                    "Kalitlar soni juda kam — hammasini sinab chiqish mumkin",
                ],
                "answer": 3,
                "explanation": "26 harfli alifboda bor-yoʻgʻi 25 ta foydali kalit "
                               "bor. Qoʻlda ham bir necha daqiqada sinab chiqiladi.",
            },
            {
                "text": "Ochiq qulf misolida server sizga nima yuboradi?",
                "choices": [
                    "Qulfning kalitini",
                    "Ochiq qulfni — kaliti esa oʻzida qoladi",
                    "Yopiq qutini",
                    "Parolingizni",
                ],
                "answer": 1,
                "explanation": "Qulfni hamma koʻrishi mumkin, lekin kaliti faqat "
                               "egasida. Siz qulflaysiz, faqat u ochadi.",
            },
        ],
        "body": """
<p>Siz telefondan bankka parol yuboryapsiz. Xabar havoda uchadi, oʻnlab
<span class="cn-word" data-tr="aloqani uzatuvchi qurilma">server</span>lardan oʻtadi
va uni yoʻlda istalgan odam «eshitishi» mumkin. Shunga qaramay, parolingiz sir
qoladi. Qanday qilib?</p>

<p>Xabarni yashirish gʻoyasi juda qadimiy. Rivoyatlarga koʻra,
<b>Yuliy Sezar</b> maktublarida har bir harfni alifboda <strong>3</strong> ta oldinga
surgan: A oʻrniga D, B oʻrniga E. «OTA» soʻzi «RWD» boʻlib qoladi. Bu
<span class="cn-word" data-tr="matnni begonalar oʻqiy olmaydigan qilib oʻzgartirish usuli">shifr</span>
deyiladi, «3» esa uning <span class="cn-word" data-tr="shifrni ochish uchun kerak boʻladigan sir">kalit</span>i.</p>

<p>Muammo shundaki, 26 harfli alifboda bunday kalitlar bor-yoʻgʻi 25 ta. Ularni
bittalab sinab koʻrish bir necha daqiqa oladi. Kompyuter esa bir zumda
<span class="cn-word" data-tr="shifrlangan matnni oʻqiladigan holga keltirmoq">ochib</span> qoʻyadi.</p>

<p>Bugungi shifrlar ancha kuchli, lekin ularning ham eski muammosi bor: kalitni qanday
<b>berish</b> kerak? Siz bank bilan avval hech qachon uchrashmagansiz. Kalitni
internet orqali yuborsangiz, uni ham hamma eshitadi.</p>

<p>1976-yilda amerikalik olimlar <b>Uitfild Diffi</b> va <b>Martin Xellman</b> bu
muammoning yechimini eʼlon qilishdi. Uni <b>ochiq qulf</b> bilan tushuntirish oson.
Bank sizga kalitni emas, <b>ochiq</b> <span class="cn-word" data-tr="eshik yoki qutini berkitadigan moslama">qulf</span>ni
yuboradi. Uni hamma koʻrishi mumkin — zarari yoʻq. Siz xabaringizni qutiga solib, shu
qulf bilan qulflaysiz. Endi qutini hech kim ocha olmaydi, hatto siz ham. Kalit
faqat bankning oʻzida.</p>

<p>Bunday «qulf» matematikada qanday yasaladi? Bir tomonga oson, orqaga juda qiyin
hisob kerak. Masalan, koʻpaytirish: 61 × 67 = <strong>4087</strong> — bir daqiqalik
ish. Endi teskarisini qiling: 4087 qaysi ikki
<span class="cn-word" data-tr="faqat 1 ga va oʻziga boʻlinadigan son">tub son</span>ning
koʻpaytmasi? Buning uchun koʻp sinash kerak.</p>

<p>1977-yilda <b>Rivest, Shamir va Adleman</b> shu gʻoyaga asoslangan
<span class="cn-word" data-tr="aniq qadamlar ketma-ketligi">algoritm</span>
yaratishdi — uni bosh harflari bilan <b>RSA</b> deyishadi. Unda sonlar yuzlab
xonali boʻladi. Ularni koʻpaytirish telefon uchun oson, ajratish esa eng kuchli
kompyuterlarga ham imkonsiz darajada uzoq.</p>

<p>Brauzer manzilida kichkina <span class="cn-word" data-tr="qulf belgisi — ulanish shifrlangan">qulf belgisi</span>ni
koʻrsangiz, bilingki, xuddi shu daqiqada sizning telefoningiz ulkan tub sonlar bilan
ishlayapti.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 34 — koʻprik va fonar
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Tungi koʻprik: toʻrt kishi va bitta fonar",
        "summary": (
            "Toʻrt kishi tunda tor koʻprikdan oʻtishi kerak, fonar esa bitta. Eng tez "
            "kishi hammani kuzatib qoʻysa — 19 daqiqa. Lekin 17 daqiqada ham "
            "boʻladi. Yechim gʻoyasi qoida blokida."
        ),
        "order":   34,
        "grammar": [
            {
                "pattern":  "Yechim gʻoyasi: ikki eng sekinni BIRGA yubor",
                "meaning":  "Eng sekin ikkita kishi alohida-alohida oʻtsa, ikkala "
                            "vaqt ham sarflanadi (10 + 5). Ular birga oʻtsa, "
                            "faqat 10 daqiqa ketadi. Buning uchun narigi tomonda "
                            "fonarni qaytaradigan tez odam oldindan turishi kerak.",
                "examples": [
                    "Jasur + Afsona oʻtadi (2) → Jasur qaytadi (1) → Sherbek + bobo "
                    "oʻtadi (10)",
                    "→ Afsona qaytadi (2) → Jasur + Afsona oʻtadi (2). Jami: "
                    "2 + 1 + 10 + 2 + 2 = 17",
                ],
            },
        ],
        "questions": [
            {
                "text": "Jasur hammani kuzatib qoʻysa, necha daqiqa ketadi?",
                "choices": ["17", "18", "19", "20"],
                "answer": 2,
                "explanation": "Bobo bilan 10, qaytish 1, Sherbek bilan 5, qaytish 1, "
                               "Afsona bilan 2: 10 + 1 + 5 + 1 + 2 = 19.",
            },
            {
                "text": "17 daqiqalik yechimning asosiy hiylasi nima?",
                "choices": [
                    "Fonarni koʻprikdan otib yuborish",
                    "Ikki eng sekin kishini birga oʻtkazish",
                    "Uch kishini birdaniga oʻtkazish",
                    "Bobo fonarni qaytarib olib keladi",
                ],
                "answer": 1,
                "explanation": "Sherbek va bobo birga oʻtsa, 5 daqiqa bobo vaqtiga "
                               "«yashirinadi». Ikkala sekin kishi uchun faqat 10 "
                               "daqiqa sarflanadi.",
            },
            {
                "text": "Agar koʻprik 16 daqiqadan keyin qulasa, toʻrttalasi "
                        "ham oʻta oladimi?",
                "choices": [
                    "Yoʻq — eng kam vaqt 17 daqiqa",
                    "Ha, 15 daqiqada",
                    "Ha, 16 daqiqada",
                    "Ha, agar Jasur ikki marta yugursa",
                ],
                "answer": 0,
                "explanation": "Barcha imkoniyatlarni sinab chiqsa, 17 dan kam yoʻl "
                               "yoʻqligi maʼlum boʻladi.",
            },
        ],
        "body": """
<p>Tun. Toʻrt kishi tor osma <span class="cn-word" data-tr="daryo ustidan oʻtish uchun qurilgan yoʻl">koʻprik</span>
oldida turibdi: <b>Jasur</b>, <b>Afsona</b>, <b>Sherbek</b> va ularning
<b>bobosi</b>. Ular narigi tomonga oʻtishlari kerak.</p>

<p><span class="cn-word" data-tr="bajarilishi shart boʻlgan talab">Shart</span>lar
shunday. Koʻprik bir vaqtda faqat <strong>ikki</strong> kishini koʻtaradi. Atrof
qop-qorongʻi, ularda esa bitta <span class="cn-word" data-tr="qoʻlda koʻtariladigan chiroq">fonar</span>
bor. Fonarsiz koʻprikka chiqib boʻlmaydi, uni otib ham boʻlmaydi — kimdir olib
qaytishi kerak.</p>

<p>Har kim oʻz <span class="cn-word" data-tr="harakat jadalligi">tezlig</span>ida
yuradi. Jasur koʻprikdan <strong>1</strong> daqiqada oʻtadi, Afsona —
<strong>2</strong>, Sherbek — <strong>5</strong>, bobo esa
<strong>10</strong> daqiqada. Ikki kishi birga yursa, ular sekinroq
<span class="cn-word" data-tr="birga yuruvchi, hamroh">sherig</span>ining tezligida
yuradi.</p>

<p>Eng tez yoʻl qancha vaqt oladi? Qogʻoz va qalam oling.</p>

<p>Birinchi oʻyga keladigan reja: eng tez yuradigan Jasur hammani bittalab kuzatib
qoʻyadi. Jasur bobo bilan oʻtadi — 10 daqiqa. Qaytadi — 1. Sherbek bilan oʻtadi —
5. Qaytadi — 1. Afsona bilan oʻtadi — 2. Jami: <strong>19</strong> daqiqa.</p>

<p>Mantiqiy koʻrinadi: fonarni har safar eng tez odam qaytaradi, vaqt tejaladi.
Ammo bu rejada bitta <span class="cn-word" data-tr="foydasiz sarflangan narsa">isrof</span>
bor. Bobo va Sherbek alohida-alohida oʻtyapti, shuning uchun ularning ikkala sekin
vaqti ham — 10 va 5 — toʻliq hisobga kiryapti.</p>

<p>Aslida toʻrttalasi <strong>17</strong> daqiqada oʻta oladi. Bundan tez esa —
hech qanday usul bilan boʻlmaydi. Javobni koʻrishdan oldin oʻzingiz topishga
urining. Bitta <span class="cn-word" data-tr="yechimga yoʻl koʻrsatuvchi kichik maslahat">ishora</span>:
kim kim bilan birga yurishi kerakligini oʻylang.</p>

<p>Bu jumboq faqat oʻyin emas. Kompyuter olimlari uni
<span class="cn-word" data-tr="eng yaxshi variantni tanlash">optimallash</span>
masalalarining namunasi sifatida koʻrsatishadi: bu yerda «har qadamda eng yaxshisini
qil» degan oddiy qoida eng yaxshi natijani bermaydi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 35 — Kyonigsberg koʻpriklari
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Kyonigsbergning yetti koʻprigi",
        "summary": (
            "Haqiqiy voqea: shahar aholisi yetti koʻprikdan bir martadan oʻtib "
            "sayr qilishning yoʻlini topa olmagan. Eyler 1736-yilda buning iloji "
            "yoʻqligini isbotladi — va graflar nazariyasi tugʻildi."
        ),
        "order":   35,
        "grammar": [
            {
                "pattern":  "Eyler qoidasi: toq nuqtalar 0 yoki 2 ta",
                "meaning":  "Har bir chiziqdan bir martadan oʻtib, qalamni "
                            "koʻtarmasdan chizish uchun toq sondagi chiziq "
                            "tutashgan nuqtalar 0 ta yoki 2 ta boʻlishi kerak. "
                            "2 ta boʻlsa, yoʻl ulardan birida boshlanib, "
                            "ikkinchisida tugaydi.",
                "examples": [
                    "Kyonigsberg: 5, 3, 3, 3 — toʻrttasi ham toq → yoʻl yoʻq",
                    "«Uycha» rasm: 3, 3, 4, 4, 2 — ikkita toq → pastki burchakdan "
                    "boshlansa, chiziladi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Kyonigsbergdagi orolga nechta koʻprik tutashgan?",
                "choices": ["3", "4", "7", "5"],
                "answer": 3,
                "explanation": "Orolga shimoliy qirgʻoqdan 2, janubiy qirgʻoqdan 2 va "
                               "sharqiy quruqlikdan 1 koʻprik tutashgan: 5 ta.",
            },
            {
                "text": "Nega toq sonli koʻprik tutashgan joy faqat yoʻlning boshi "
                        "yoki oxiri boʻla oladi?",
                "choices": [
                    "Chunki u yerda koʻprik eng uzun",
                    "Har kirish uchun bitta chiqish kerak; toq boʻlsa, bitta "
                    "koʻprik juftsiz qoladi",
                    "Chunki u yerga suzib borish mumkin",
                    "Chunki u yer eng katta",
                ],
                "answer": 1,
                "explanation": "Oʻrtadan oʻtib ketadigan joyda koʻpriklar «kirish-"
                               "chiqish» juftlariga boʻlinadi, demak ularning soni "
                               "juft. Toq boʻlsa, sayr shu yerda boshlanadi yoki tugaydi.",
            },
            {
                "text": "Bir rasmda toq chiziqli nuqtalar 4 ta. Uni qalamni "
                        "koʻtarmasdan, har chiziqdan bir marta oʻtib chizish mumkinmi?",
                "choices": [
                    "Ha, istalgan nuqtadan boshlab",
                    "Ha, faqat toq nuqtadan boshlab",
                    "Ha, agar tez chizilsa",
                    "Yoʻq, mumkin emas",
                ],
                "answer": 3,
                "explanation": "Yoʻlning faqat bitta boshi va bitta oxiri bor, yaʼni "
                               "toq nuqtalar koʻpi bilan 2 ta boʻla oladi. 4 ta boʻlsa — "
                               "iloji yoʻq.",
            },
        ],
        "body": """
<p>XVIII asr. Prussiyaning Kyonigsberg shahri Pregel <span class="cn-word" data-tr="oqib turuvchi katta suv">daryo</span>si boʻyida joylashgan.
Daryo shaharni toʻrt qismga boʻladi: shimoliy va janubiy
<span class="cn-word" data-tr="daryo yoki dengiz boʻyi">qirgʻoq</span>lar, oʻrtadagi
<span class="cn-word" data-tr="atrofi suv bilan oʻralgan quruqlik">orol</span> va
sharqdagi yana bir quruqlik. Ularni <strong>yetti</strong> koʻprik bogʻlaydi.</p>

<p>Shahar <span class="cn-word" data-tr="bir joyda yashovchi odamlar">aholi</span>si yakshanba kunlari bir oʻyin oʻynardi: shunday sayr qilish
kerakki, har bir koʻprikdan <b>bir martadan</b> oʻtilsin — na ikki marta, na
tashlab ketilsin. Hech kim uddalay olmasdi. Lekin hech kim buning iloji yoʻqligini
ham isbotlay olmasdi.</p>

<p>1736-yilda masala <b>Leonard Eyler</b>ga yetib keldi. Uning birinchi qadami
daho edi: u xaritani <b>tashlab yubordi</b>. Koʻchalar, uylar, koʻpriklarning
uzunligi — hammasi ahamiyatsiz. Muhimi faqat bitta narsa: qaysi quruqlik qaysi
quruqlik bilan nechta koʻprik orqali bogʻlangan. Har bir quruqlik —
<span class="cn-word" data-tr="chizmadagi belgi qoʻyilgan joy">nuqta</span>, har bir
koʻprik — <span class="cn-word" data-tr="ikki nuqtani tutashtiruvchi chiziq">chiziq</span>.</p>

<figure class="pm-fig">
<svg viewBox="0 0 340 280" role="img" aria-label="Toʻrt nuqta va yetti chiziqli graf">
  <path class="pm-ln" d="M170 40 Q95 60 90 140"/>
  <path class="pm-ln" d="M170 40 Q165 115 90 140"/>
  <path class="pm-ln" d="M170 240 Q95 220 90 140"/>
  <path class="pm-ln" d="M170 240 Q165 165 90 140"/>
  <path class="pm-ln" d="M170 40 L270 140"/>
  <path class="pm-ln" d="M170 240 L270 140"/>
  <path class="pm-ln" d="M90 140 L270 140"/>
  <circle class="pm-pt" cx="170" cy="40" r="8"/>
  <circle class="pm-pt" cx="170" cy="240" r="8"/>
  <circle class="pm-pt" cx="90" cy="140" r="8"/>
  <circle class="pm-pt" cx="270" cy="140" r="8"/>
  <text class="pm-lbl" x="184" y="30">Shimol · 3</text>
  <text class="pm-lbl" x="184" y="262">Janub · 3</text>
  <text class="pm-lbl pm-lbl--hl" x="12" y="128">Orol · 5</text>
  <text class="pm-lbl" x="262" y="168">Sharq · 3</text>
</svg>
<figcaption>Eylerning chizmasi: quruqliklar — nuqtalar, koʻpriklar — chiziqlar.
Raqam — har bir nuqtaga nechta koʻprik tutashgani.</figcaption>
</figure>

<p>Endi Eyler oddiy narsani payqadi. Sayr davomida biror quruqlikka
<b>kirsangiz</b>, undan <b>chiqishingiz</b> ham kerak. Har bir kirish bitta koʻprik,
har bir chiqish yana bitta. Demak, sayr shunchaki oʻtib ketadigan joyga
<span class="cn-word" data-tr="2 ga qoldiqsiz boʻlinadigan">juft</span> sonli
koʻprik tutashgan boʻlishi kerak. <span class="cn-word" data-tr="2 ga boʻlinmaydigan">Toq</span>
sonli koʻprik faqat sayrning <b>boshi</b> yoki <b>oxiri</b>da boʻla oladi — demak bunday
joylar koʻpi bilan ikkita.</p>

<p>Kyonigsbergda esa orolga <strong>5</strong> ta, qolgan uchta quruqlikka
<strong>3</strong> tadan koʻprik tutashgan. Toʻrttalasi ham toq! Demak bunday sayr
<b>mavjud emas</b>. <span class="cn-word" data-tr="mantiq bilan shubhasiz koʻrsatib berish">Isbot</span> tugadi — birorta qadam ham yurmasdan.</p>

<p>Shu kichik masaladan matematikaning yangi boʻlimi —
<span class="cn-word" data-tr="nuqtalar va ularni tutashtiruvchi chiziqlar haqidagi fan">graflar nazariyasi</span>
tugʻildi. Bugun u navigator yoʻl tanlashida, internet tarmoqlarida va hatto
ijtimoiy tarmoqlardagi «doʻstlar»ni hisoblashda ishlaydi.</p>

<p>Sinab koʻring: kvadrat, uning ikkita diagonali va ustida tom — «uycha» rasmini
qalamni koʻtarmasdan chizing. Eyler qoidasi qayerdan boshlashni aytib beradi:
toq chiziq tutashgan pastki burchaklarning biridan.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 39 — boʻri, echki va karam
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Boʻri, echki va karam: 1200 yillik jumboq",
        "summary": (
            "Qayiqqa dehqondan tashqari faqat bitta yuk sigʻadi. Boʻri echkini, "
            "echki karamni yeb qoʻymasligi kerak. Jumboq taxminan 800-yilda "
            "yozilgan. Yechim gʻoyasi qoida blokida."
        ),
        "order":   39,
        "grammar": [
            {
                "pattern":  "Yechim gʻoyasi: yukni ORQAGA olib kelish mumkin",
                "meaning":  "Hamma faqat oldinga tashishni oʻylaydi. Hiyla — "
                            "echkini bir marta qaytarib olib kelish. Jami 7 marta "
                            "suzish kerak, bundan kami mumkin emas.",
                "examples": [
                    "1) echkini olib oʻtadi 2) boʻsh qaytadi 3) boʻrini olib oʻtadi "
                    "4) echkini QAYTARIB keladi",
                    "5) karamni olib oʻtadi 6) boʻsh qaytadi 7) echkini olib oʻtadi",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega dehqon birinchi boʻlib echkini olib oʻtishi kerak?",
                "choices": [
                    "Echki eng yengil",
                    "Echki suzishni bilmaydi",
                    "Boʻri bilan karam birga qolsa, hech narsa boʻlmaydi",
                    "Echki eng qimmat",
                ],
                "answer": 2,
                "explanation": "Boʻri karam yemaydi. Echki esa ikkalasi bilan ham "
                               "«muammoli» — shuning uchun avval uni olib ketadi.",
            },
            {
                "text": "Jumboqni yechish uchun qayiq eng kamida necha marta "
                        "daryodan suzib oʻtishi kerak?",
                "choices": ["7", "3", "5", "9"],
                "answer": 0,
                "explanation": "Barcha holatlarni tekshirsa, 7 tadan kam yoʻl yoʻq. "
                               "Echkini bir marta orqaga olib kelish shart.",
            },
            {
                "text": "Bu jumboqni birinchi boʻlib kim yozib qoldirgan?",
                "choices": [
                    "Al-Xorazmiy",
                    "Leonard Eyler",
                    "Pifagor",
                    "Alkuin, taxminan 800-yilda",
                ],
                "answer": 3,
                "explanation": "U Alkuinga nisbat beriladigan «Yoshlarni charxlash "
                               "uchun masalalar» toʻplamida bor.",
            },
        ],
        "body": """
<p>Bir <span class="cn-word" data-tr="yer haydab, ekin ekadigan kishi">dehqon</span>
bozordan qaytmoqda. U bilan uchta <span class="cn-word" data-tr="tashiladigan narsa">yuk</span> bor: <b>boʻri</b>, <b>echki</b> va bir
bosh <b>karam</b>. Oldida daryo, qirgʻoqda kichik
<span class="cn-word" data-tr="eshkak bilan yuradigan kichik kema">qayiq</span>.</p>

<p>Qayiq juda kichik: dehqondan tashqari faqat <b>bitta</b> yuk sigʻadi. Lekin
muammo boshqa joyda. Dehqon yoʻqligida <span class="cn-word" data-tr="yovvoyi yirtqich hayvon">boʻri</span> echkini yeb qoʻyadi. Echki esa karamni
yeb qoʻyadi. Dehqon yonida boʻlsa — hech kim hech kimga tegmaydi.</p>

<p>Uchala yukni ham butun-sogʻ narigi qirgʻoqqa qanday olib oʻtish mumkin? Toʻxtang
va sinab koʻring. Uchta tanga yoki qogʻoz parchasi bilan stol ustida oʻynash
osonroq.</p>

<p>Bu jumboq juda qadimiy. U taxminan <strong>800</strong>-yilda yozilgan
<i>«Yoshlarni charxlash uchun masalalar»</i> toʻplamida uchraydi. Toʻplam Buyuk
Karl saroyidagi olim <b>Alkuin</b>ga (Alcuin) nisbat beriladi. Demak bu masala bilan
odamlar <strong>1200</strong> yildan beri bosh qotiradi.</p>

<p>Koʻpchilik shunday boshlaydi: «Avval boʻrini olib oʻtaman». Lekin shunda echki
karam bilan qoladi — karam yoʻq. «Avval karamni» — boʻri echki bilan qoladi. Demak
birinchi qadam bitta: <b>echkini</b> olib oʻtish. Boʻri va karam birga xavfsiz.</p>

<p>Ikkinchi <span class="cn-word" data-tr="borib-kelish">qatnov</span>da esa dehqon <span class="cn-word" data-tr="chiqish yoʻli yoʻq holat">boshi berk</span>
koʻchaga kiradi. Boʻrini olib oʻtsa — narigi qirgʻoqda boʻri echki bilan qoladi.
Karamni olib oʻtsa — echki karam bilan. Hamma shu yerda
<span class="cn-word" data-tr="nima qilishni bilmay qolmoq">dovdirab qol</span>adi.</p>

<p>Bir <span class="cn-word" data-tr="yechimga yoʻl koʻrsatuvchi kichik maslahat">ishora</span>:
qoidalarda hech qayerda «yukni faqat oldinga tashish mumkin» deyilmagan.</p>

<p>Bunday masalalarni matematiklar <span class="cn-word" data-tr="bir holatdan boshqasiga oʻtish ketma-ketligi">holatlar</span>
grafi bilan yechishadi: har bir vaziyat — nuqta, har bir suzish — chiziq. Shunda
eng qisqa yoʻlni kompyuter ham topadi: <strong>7</strong> marta suzish. Bu
gʻoya bugun robotlarga yoʻl topishni oʻrgatishda ham ishlatiladi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 40 — yolgʻonchilar oroli
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Rostgoʻylar va yolgʻonchilar oroli",
        "summary": (
            "Orolda ikki xil odam yashaydi: biri doim rost, biri doim yolgʻon "
            "gapiradi. Bitta gapdan kim kimligini, bitta savoldan esa toʻgʻri "
            "yoʻlni bilish mumkin. Yechim gʻoyasi qoida blokida."
        ),
        "order":   40,
        "grammar": [
            {
                "pattern":  "Yechim gʻoyasi: har ehtimolni sinab, ziddiyatni izla",
                "meaning":  "1) Agar A rostgoʻy boʻlsa, uning «ikkalamiz ham "
                            "yolgʻonchimiz» degan gapi uni ham yolgʻonchi qiladi — "
                            "ziddiyat. Demak A yolgʻonchi, gapi yolgʻon, yaʼni "
                            "ikkalasi yolgʻonchi EMAS → B rostgoʻy. 2) Ichma-ich "
                            "savolda yolgʻonchi ikki marta yolgʻon gapiradi, va "
                            "ikki yolgʻon bir-birini yoʻqqa chiqaradi.",
                "examples": [
                    "Savol: «Agar men sendan "
                    "„bu yoʻl qishloqqa olib boradimi?“ deb soʻrasam, „ha“ "
                    "deysanmi?»",
                    "Rostgoʻy ham, yolgʻonchi ham — yoʻl toʻgʻri boʻlsa «ha», "
                    "notoʻgʻri boʻlsa «yoʻq» deydi",
                ],
            },
        ],
        "questions": [
            {
                "text": "A: «Ikkalamiz ham yolgʻonchimiz». Kim kim?",
                "choices": [
                    "A rostgoʻy, B yolgʻonchi",
                    "Ikkalasi ham yolgʻonchi",
                    "A yolgʻonchi, B rostgoʻy",
                    "Ikkalasi ham rostgoʻy",
                ],
                "answer": 2,
                "explanation": "Rostgoʻy oʻzini yolgʻonchi demaydi, demak A yolgʻonchi. "
                               "Unda gapi yolgʻon — ikkalasi yolgʻonchi emas, demak B "
                               "rostgoʻy.",
            },
            {
                "text": "Yolgʻonchi bilan uchrashdingiz, yoʻl qishloqqa OLIB "
                        "BORADI. Ichma-ich savolga u nima deydi?",
                "choices": [
                    "«Ha»",
                    "«Yoʻq»",
                    "Hech narsa demaydi",
                    "«Bilmayman»",
                ],
                "answer": 0,
                "explanation": "Toʻgʻridan-toʻgʻri soʻralsa u «yoʻq» derdi. Siz "
                               "«„ha“ deysanmi?» deb soʻraysiz — bu ham yolgʻon "
                               "boʻlishi kerak, demak «ha» deydi. Ikki yolgʻon "
                               "haqiqatni beradi.",
            },
            {
                "text": "B: «A yolgʻonchi». A: «B yolgʻonchi». Nima deyish mumkin?",
                "choices": [
                    "Ikkalasi ham rostgoʻy",
                    "Ikkalasi ham yolgʻonchi",
                    "Hech narsa aniq emas",
                    "Biri rostgoʻy, biri yolgʻonchi — lekin qaysi biri ekani nomaʼlum",
                ],
                "answer": 3,
                "explanation": "Ikkalasi rostgoʻy boʻlsa, gaplari yolgʻon chiqadi; "
                               "ikkalasi yolgʻonchi boʻlsa, gaplari rost chiqadi. "
                               "Faqat «biri u, biri bu» izchil — ikki xil tartibda.",
            },
        ],
        "body": """
<p>Siz kemadan tushib, gʻalati bir <span class="cn-word" data-tr="atrofi suv bilan oʻralgan quruqlik">orol</span>ga
chiqdingiz. Bu yerda ikki xil odam yashaydi. <b>Rostgoʻylar</b> doim faqat rost
gapiradi. <b>Yolgʻonchilar</b> doim faqat yolgʻon gapiradi. Tashqi koʻrinishdan ularni
ajratib boʻlmaydi.</p>

<p>Bunday jumboqlarni amerikalik matematik va
<span class="cn-word" data-tr="mantiq bilan shugʻullanuvchi olim">mantiqchi</span>
<b>Raymond Smallian</b> (Raymond Smullyan) mashhur qilgan. Uning 1978-yilgi
<i>«Bu kitobning nomi nima?»</i> kitobi butun bir orolni shunday jumboqlar bilan
toʻldirgan.</p>

<p><b>Birinchi uchrashuv.</b> Yoʻlda ikki kishi turibdi, A va B. A sizga deydi:
<i>«Ikkalamiz ham yolgʻonchimiz»</i>. Kim rostgoʻy, kim yolgʻonchi? Bitta gapdan
bilish mumkinmi?</p>

<p>Mana usul: har bir <span class="cn-word" data-tr="boʻlishi mumkin boʻlgan variant">ehtimol</span>ni
bittalab sinab koʻring va qaysi biri <span class="cn-word" data-tr="bir-biriga qarshi chiqish">ziddiyat</span>ga
olib kelishini qidiring. Masalan: «A rostgoʻy» deb
<span class="cn-word" data-tr="vaqtincha haqiqat deb olmoq">faraz qil</span>sak,
nima boʻladi? Uning gapi rost boʻlishi kerak… Davom ettiring.</p>

<p><b>Ikkinchi uchrashuv.</b> Endi yoʻl ikkiga ajraladi. Biri qishloqqa olib boradi,
biri — botqoqqa. Yoʻl ayrilgan joyda bitta orol aholisi turibdi, lekin u rostgoʻymi yoki
yolgʻonchimi — bilmaysiz. Unga faqat <b>bitta</b> «ha yoki yoʻq» savoli berishingiz
mumkin.</p>

<p>«Bu yoʻl qishloqqa olib boradimi?» deb soʻrasangiz, foydasi yoʻq: «ha» degan
javob rost ham, yolgʻon ham boʻlishi mumkin. Sizga shunday
<span class="cn-word" data-tr="soʻroq gap">savol</span> kerakki, javob
kim soʻralganiga <b>bogʻliq boʻlmasin</b>.</p>

<p>Bunday savol bor. U <b>ichma-ich</b> tuzilgan: savolning ichida yana bir savol
bor. Bir <span class="cn-word" data-tr="yechimga yoʻl koʻrsatuvchi kichik maslahat">ishora</span>:
ikki marta yolgʻon gapirish nimaga teng?</p>

<p>Bunday mulohazalar oʻyin emas. Kompyuter
<span class="cn-word" data-tr="«rost» va «yolgʻon» bilan ishlovchi mantiq">mantiq</span>i
aynan shu «rost» va «yolgʻon» ustiga qurilgan: telefoningizdagi har bir chip
soniyasiga milliardlab shunday xulosa chiqaradi.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 42 — cheksizliklar
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Cheksizlik bir xil emas: Kantorning diagonali",
        "summary": (
            "Natural sonlar ham cheksiz, nuqtalar ham cheksiz. Ammo Georg Kantor "
            "1891-yilda ikkinchisi «kattaroq» ekanini oddiy bir hiyla — diagonal "
            "bilan isbotladi."
        ),
        "order":   42,
        "grammar": [
            {
                "pattern":  "Kantor diagonali: har qatordan bitta raqamni oʻzgartir",
                "meaning":  "Cheksiz 0–1 ketma-ketliklarning har qanday roʻyxatini "
                            "olaylik. 1-qatorning 1-raqamini, 2-qatorning 2-raqamini "
                            "va hokazo olib, har birini teskarisiga oʻzgartiramiz. "
                            "Yangi ketma-ketlik har bir qatordan kamida bitta "
                            "raqamda farq qiladi — demak u roʻyxatda yoʻq.",
                "examples": [
                    "1: 0110…  2: 1101…  3: 0001…  4: 1011…",
                    "Diagonal: 0, 1, 0, 1 → oʻzgartirsak 1, 0, 1, 0 — roʻyxatda yoʻq",
                ],
            },
        ],
        "questions": [
            {
                "text": "Roʻyxat: 1: 1001…, 2: 0011…, 3: 1110…, 4: 0100… Diagonalni "
                        "teskarisiga oʻzgartirsak, yangi ketma-ketlik qanday "
                        "boshlanadi?",
                "choices": ["1010…", "0101…", "1001…", "0011…"],
                "answer": 1,
                "explanation": "Diagonal raqamlari: 1, 0, 1, 0. Har birini "
                               "oʻzgartirsak: 0, 1, 0, 1. Bu ketma-ketlik roʻyxatdagi "
                               "birorta qator bilan mos kelmaydi.",
            },
            {
                "text": "Natural sonlar (1, 2, 3, …) va juft sonlar (2, 4, 6, …) "
                        "haqida qaysi gap toʻgʻri?",
                "choices": [
                    "Natural sonlar ikki marta koʻp",
                    "Juft sonlar koʻproq",
                    "Ularni taqqoslab boʻlmaydi",
                    "Ular bir xil «koʻp»: har n ga 2n juft keladi",
                ],
                "answer": 3,
                "explanation": "1 ↔ 2, 2 ↔ 4, 3 ↔ 6… Har biriga roppa-rosa bitta jufti "
                               "bor — demak bu ikki cheksizlik teng.",
            },
            {
                "text": "Diagonal usul nimani isbotlaydi?",
                "choices": [
                    "Cheksiz 0–1 ketma-ketliklarni bitta roʻyxatga terib chiqib "
                    "boʻlmaydi",
                    "Hamma cheksizliklar teng",
                    "Natural sonlar tugaydi",
                    "Kasrlar sanab boʻlmaydigan darajada koʻp",
                ],
                "answer": 0,
                "explanation": "Qanday roʻyxat tuzmang, diagonaldan undan tashqarida "
                               "qolgan ketma-ketlik yasaladi. Demak bunday "
                               "ketma-ketliklar natural sonlardan «koʻproq».",
            },
        ],
        "body": """
<p>Qaysi biri koʻp: natural sonlarmi (1, 2, 3, …) yoki
<span class="cn-word" data-tr="2 ga qoldiqsiz boʻlinadigan son">juft son</span>larmi
(2, 4, 6, …)? Birinchi javob: natural sonlar, ikki marta koʻp! Lekin ikkalasi ham
<span class="cn-word" data-tr="oxiri yoʻq, tugamaydigan">cheksiz</span>. Cheksizlikni
qanday solishtiramiz?</p>

<p>Nemis matematigi <b>Georg Kantor</b> (Georg Cantor, 1845–1918) javobni
oddiy narsadan boshladi. Kichik bola sanashni bilmasa ham, qaysi qatorda
<span class="cn-word" data-tr="bolalar oʻynaydigan kichik shar">sharcha</span> koʻp
ekanini bilib oladi: ularni bittadan
<span class="cn-word" data-tr="har biriga roppa-rosa bitta sherik topmoq">juftlash</span>
kifoya. Kimda ortib qolsa — oʻsha koʻp.</p>

<p>Natural va juft sonlarni juftlaymiz: 1 ↔ 2, 2 ↔ 4, 3 ↔ 6, … Har bir songa roppa-rosa
bitta jufti bor, hech kim ortib qolmaydi. Demak ular <b>teng</b>! «Hilbert
mehmonxonasi»ni eslang — u yerda ham aynan shu hiyla ishlagan edi. Kantor hatto
barcha <span class="cn-word" data-tr="ikki butun sonning nisbati">kasr</span>larni ham
bitta roʻyxatga terib chiqish mumkinligini koʻrsatdi.</p>

<p>Unda hamma cheksizliklar tengmi? Kantorning eng mashhur kashfiyoti — <b>yoʻq</b>.</p>

<p>Faqat 0 va 1 dan iborat cheksiz <span class="cn-word" data-tr="tartib bilan joylashgan sonlar qatori">ketma-ketlik</span>larni
olaylik: 0110…, 1101… va hokazo. Kimdir «Men ularning hammasini roʻyxatga terib
chiqdim» deydi. Kantor buni tekshirmaydi ham — u bitta yangi ketma-ketlik yasaydi.</p>

<p>Birinchi qatordan 1-raqamni, ikkinchi qatordan 2-raqamni, uchinchidan 3-raqamni
oladi — roʻyxat boʻylab qiya chiziq, <span class="cn-word" data-tr="qiya chiziq, burchakdan burchakka">diagonal</span>
boʻylab yuradi. Keyin har bir raqamni teskarisiga
<span class="cn-word" data-tr="boshqacha qilmoq">oʻzgartir</span>adi: 0 ni 1 ga, 1 ni 0 ga.</p>

<p>Yangi ketma-ketlik birinchi qatordan birinchi raqamda farq qiladi. Ikkinchi
qatordan — ikkinchi raqamda. Yuzinchi qatordan — yuzinchi raqamda. Demak u
roʻyxatning <b>hech qayerida</b> yoʻq! Roʻyxat qanday tuzilmasin, undan nimadir
doim tashqarida qoladi.</p>

<p>Xulosa: bunday ketma-ketliklar natural sonlardan <b>koʻproq</b>. Cheksizliklarning
ham <span class="cn-word" data-tr="pastdan yuqoriga qadamlar">pogʻona</span>lari bor.
Kantor bu <span class="cn-word" data-tr="isbot yoʻli">usul</span>ni 1891-yilda eʼlon
qildi.</p>

<p>Koʻp zamondoshlari uning gʻoyalarini rad etdi. Ammo vaqt Kantorni oqladi.
1926-yilda David Hilbert shunday degan: <i>«Kantor yaratgan jannatdan bizni hech
kim haydab chiqara olmaydi»</i>.</p>
""",
    },
]
