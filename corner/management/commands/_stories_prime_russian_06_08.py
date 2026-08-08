# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-6 … PR-8.

Har bir matn oʻz darsining grammatikasini kamida ikki marta koʻrsatadi va faqat
oʻsha darsgacha oʻrganilgan qoliplardan foydalanadi (kumulyativ qoida).
Toc: corner/management/commands/toc_prime_russian_readings.txt

Bu uch matnda hali feʼl tizimi ochilmagan (u PR-19 dan boshlanadi), shuning uchun
tocdagi "narrative frame" istisnosidan foydalanilgan: есть · нет · зову́т · живёт ·
рабо́тает · говори́т · сказа́л(а) · пришёл/пришла́ · дал(а) · был/была́ — hammasi
cn-word izohi bilan.

Shakl xilma-xilligi (versatility): 6 — sinf suhbati, 7 — bir kunda ikki suhbat,
8 — uydagi kichik sahna (hikoya).

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_06_08.py --author=prime
"""

SUBJECT = {
    "name":    "Russian",
    "summary": "Rus tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#b91c1c",
}

COLLECTION = {
    "title":       "Prime Russian Readings",
    "description": (
        "Prime Russian darslarining oʻqish matnlari — har biri oʻz darsining "
        "grammatikasini matn ichida koʻrsatadi. Lugʻat izohlari va audio bilan."
    ),
    "order": 3,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PR-6 — Это / Кто это? / Что это?      DIALOG (ikki ovoz)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Кто э́то?",
        "summary": (
            "PR-6 matni. Dilnoza Jasurga sinf fotosuratini koʻrsatadi. Har bir savol — "
            "«Кто э́то?» yoki «Что э́то?», va oxirida Jasur bitta narsani adashtiradi. "
            "Suhbat shaklidagi matn: audio ikki ovozda oʻqiladi."
        ),
        "order":   6,
        "grammar": [
            {
                "pattern":  "Э́то + ot",
                "meaning":  "«Bu — …». Rus tilida hozirgi zamonda “boʻlmoq” feʼli "
                            "qoʻyilmaydi, shuning uchun ikkita soʻz toʻliq gap boʻladi — "
                            "xuddi oʻzbekchadagi «Bu — uy» kabi.",
                "examples": ["Э́то шко́ла.", "Э́то Шербе́к.", "Э́то кот."],
            },
            {
                "pattern":  "Кто э́то? / Что э́то?",
                "meaning":  "Odam va hayvon haqida — КТО (kim). Buyum, joy va tushuncha "
                            "haqida — ЧТО (nima). Oʻzbekchadagi «kim?» va «nima?» bilan "
                            "bir xil boʻlinish; farqi shundaki, hayvon ruschada КТО "
                            "tomonda turadi.",
                "examples": ["Кто э́то? — Э́то Афсо́на.", "Что э́то? — Э́то шко́ла."],
            },
            {
                "pattern":  "Нет, э́то не …",
                "meaning":  "Rad javobi. НЕТ — «yoʻq» degan javob, НЕ esa inkor "
                            "qilinayotgan soʻzning OLDIDA turadi (oʻzbekchadagi «emas» "
                            "gap oxirida keladi, ruschada esa oldinda).",
                "examples": ["Нет, э́то не соба́ка.", "Нет, э́то не Жасу́р."],
            },
        ],
        "body": '''<p><strong>Дилно́за:</strong> Жасу́р, <strong>кто э́то</strong>?</p>

<p><strong>Жасу́р:</strong> <strong>Э́то</strong> Шербе́к. Шербе́к — <span class="cn-word" data-tr="doʻst">друг</span>.</p>

<p><strong>Дилно́за:</strong> А э́то кто?</p>

<p><strong>Жасу́р:</strong> Э́то Афсо́на. Афсо́на — <span class="cn-word" data-tr="opa-singil">сестра́</span>.</p>

<p><strong>Дилно́за:</strong> А <strong>что э́то</strong>?</p>

<p><strong>Жасу́р:</strong> Э́то <span class="cn-word" data-tr="maktab">шко́ла</span>. Здесь <span class="cn-word" data-pos="verb" data-tr="oʻqiydi, yashaydi (bu yerda: bor)">живёт</span> Афсо́на. Э́то Ташке́нт.</p>

<p><strong>Дилно́за:</strong> А э́то соба́ка?</p>

<p><strong>Жасу́р:</strong> <strong>Нет, э́то не</strong> <span class="cn-word" data-tr="it">соба́ка</span>. Э́то <span class="cn-word" data-tr="mushuk">кот</span>. Кота́ <span class="cn-word" data-pos="verb" data-tr="chaqirishadi, ismi">зову́т</span> Ба́рсик.</p>

<p><strong>Дилно́за:</strong> Ба́рсик — кот? Не соба́ка?</p>

<p><strong>Жасу́р:</strong> Да, Ба́рсик — кот. И Ба́рсик — то́же друг.</p>''',
        "questions": [
            {
                "text": "Sherbek kim?",
                "choices": [
                    "Jasurning doʻsti",
                    "Jasurning akasi",
                    "Oʻqituvchi",
                    "Mushuk"
                ],
                "answer": 0,
                "explanation": "Jasur «Шербе́к — друг» dedi, yaʼni “Sherbek — doʻst”. "
                               "Diqqat qiling: bu ikki soʻzli toʻliq gap, orasida hech "
                               "qanday feʼl yoʻq.",
            },
            {
                "text": "Nega Dilnoza maktab haqida «Кто э́то?» emas, «Что э́то?» deb "
                        "soʻradi?",
                "choices": [
                    "Chunki maktab — jonsiz narsa, jonsiz narsa haqida ЧТО soʻraladi",
                    "Chunki maktab — ayol jinsida",
                    "Chunki Dilnoza maktabni bilmasdi",
                    "Chunki maktab uzoqda edi"
                ],
                "answer": 0,
                "explanation": "Rus tilida КТО — odam va hayvon uchun, ЧТО — buyum, joy "
                               "va tushuncha uchun. Maktab — joy, shuning uchun «Что "
                               "э́то?». Aynan shuning uchun mushuk haqida esa «Кто "
                               "э́то?» soʻralar edi — hayvon КТО tomonda.",
            },
            {
                "text": "«Нет, э́то не соба́ка» gapida НЕ soʻzi qayerda turibdi?",
                "choices": [
                    "Inkor qilinayotgan soʻzning oldida",
                    "Gap oxirida",
                    "Gap boshida",
                    "Bu gapda НЕ umuman yoʻq"
                ],
                "answer": 0,
                "explanation": "НЕ har doim oʻzi inkor qilayotgan soʻzning OLDIDA turadi: "
                               "не соба́ка. Oʻzbekchadagi «emas» gap oxirida keladi "
                               "(«bu it emas»), ruschada esa oldinda — shuning uchun bu "
                               "joyda koʻp xato qilinadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-7 — ты / вы                        DIALOG (ikki ovoz)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Два разгово́ра",
        "summary": (
            "PR-7 matni. Afsona maktab yoʻlagida ikki marta salomlashadi: avval "
            "sinfdoshi Jasur bilan, keyin oʻqituvchisi Sergey Petrovich bilan. Bir "
            "xil vaziyat, ikki xil daraja — «ты» va «вы» farqi yonma-yon koʻrinadi."
        ),
        "order":   7,
        "grammar": [
            {
                "pattern":  "ты / вы",
                "meaning":  "Oʻzbekchadagi «sen» va «siz». ТЫ — tengdosh, doʻst, oila. "
                            "ВЫ — notanish odam, oʻqituvchi, katta yoshli, va shu bilan "
                            "birga koʻplik. Ikkilansangiz — ВЫ.",
                "examples": ["Как тебя́ зову́т? (doʻstga)",
                             "Как вас зову́т? (oʻqituvchiga)"],
            },
            {
                "pattern":  "Приве́т / Здра́вствуйте",
                "meaning":  "Salomlashishning ikki darajasi. ПРИВЕ́Т — doʻstga, "
                            "ЗДРА́ВСТВУЙТЕ — hurmat bilan. Talaffuzda oʻrtadagi В "
                            "aytilmaydi: [здра́ствуйт'е].",
                "examples": ["Приве́т, Жасу́р!", "Здра́вствуйте, Серге́й Петро́вич!"],
            },
            {
                "pattern":  "Пока́ / До свида́ния",
                "meaning":  "Xayrlashishning ikki darajasi, salomlashish bilan juftlashadi. "
                            "Bir suhbatda bitta darajada qolish kerak: Приве́т → Пока́, "
                            "Здра́вствуйте → До свида́ния.",
                "examples": ["Пока́, Жасу́р!", "До свида́ния!"],
            },
        ],
        "body": '''<p><strong>Жасу́р:</strong> <strong>Приве́т</strong>, Афсо́на! Как <span class="cn-word" data-tr="ishlar">дела́</span>?</p>

<p><strong>Афсо́на:</strong> Приве́т, Жасу́р! <span class="cn-word" data-tr="yaxshi">Хорошо́</span>. А <strong>ты</strong>?</p>

<p><strong>Жасу́р:</strong> <span class="cn-word" data-tr="normal, yomon emas">Норма́льно</span>. Афсо́на, э́то Дилно́за. Дилно́за — сестра́.</p>

<p><strong>Афсо́на:</strong> <span class="cn-word" data-tr="juda">О́чень</span> <span class="cn-word" data-tr="yoqimli">прия́тно</span>! Ну, <strong>пока́</strong>!</p>

<p><strong>Серге́й Петро́вич:</strong> <strong>Здра́вствуйте</strong>! <span class="cn-word" data-tr="kechirasiz">Извини́те</span>, как <strong>вас</strong> <span class="cn-word" data-pos="verb" data-tr="chaqirishadi, ismingiz">зову́т</span>?</p>

<p><strong>Афсо́на:</strong> Здра́вствуйте! <span class="cn-word" data-tr="meni">Меня́</span> зову́т Афсо́на.</p>

<p><strong>Серге́й Петро́вич:</strong> О́чень прия́тно, Афсо́на. Э́то <span class="cn-word" data-tr="lugʻat">слова́рь</span>. <span class="cn-word" data-tr="marhamat, iltimos">Пожа́луйста</span>.</p>

<p><strong>Афсо́на:</strong> <span class="cn-word" data-tr="rahmat">Спаси́бо</span>! <strong>До свида́ния</strong>, Серге́й Петро́вич!</p>''',
        "questions": [
            {
                "text": "Nega Afsona Jasurga «ты», Sergey Petrovichga esa «вы» dedi?",
                "choices": [
                    "Jasur — tengdoshi, Sergey Petrovich esa oʻqituvchi",
                    "Jasur — erkak, Sergey Petrovich — ayol",
                    "Jasurni yaxshi bilmaydi",
                    "Rus tilida «ты» faqat bolalarga aytiladi"
                ],
                "answer": 0,
                "explanation": "Tengdoshga va doʻstga — ТЫ, oʻqituvchiga va katta yoshdagi "
                               "odamga — ВЫ. Bu oʻzbekchadagi «sen» va «siz» bilan bir xil "
                               "tizim. Ikkilanganda har doim ВЫ tanlanadi.",
            },
            {
                "text": "Afsona Jasur bilan «Пока́», oʻqituvchi bilan «До свида́ния» deb "
                        "xayrlashdi. Bu nimani koʻrsatadi?",
                "choices": [
                    "Xayrlashish salomlashish bilan bir darajada boʻlishi kerak",
                    "«Пока́» faqat ertalab aytiladi",
                    "«До свида́ния» faqat maktabda aytiladi",
                    "Ikkalasi bir xil, farqi yoʻq"
                ],
                "answer": 0,
                "explanation": "Bir suhbatda bitta darajada qolinadi: Приве́т → Пока́ "
                               "(norasmiy), Здра́вствуйте → До свида́ния (rasmiy). "
                               "Rasmiy salomlashib, norasmiy xayrlashish gʻalati "
                               "eshitiladi.",
            },
            {
                "text": "Sergey Petrovich «Как вас зову́т?» dedi. Bu soʻzma-soʻz nima "
                        "degani?",
                "choices": [
                    "«Sizni qanday chaqirishadi?»",
                    "«Sizning ismingiz bormi?»",
                    "«Siz kimsiz?»",
                    "«Siz qayerdansiz?»"
                ],
                "answer": 0,
                "explanation": "Soʻzma-soʻz «sizni qanday chaqirishadi». Shuning uchun bu "
                               "iborada «ism» degan soʻz umuman yoʻq, va soʻz tartibi "
                               "hech qachon oʻzgarmaydi — «Как зову́т вас?» deyilmaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-8 — род                            HIKOYA (bitta ovoz)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Стол, кни́га и окно́",
        "summary": (
            "PR-8 matni. Bekzod hali kichkina va u har bir narsa haqida «он mi yoki "
            "она́ mi?» deb soʻrayveradi. Opasi Dilnoza javob beradi — va oxirida "
            "Bekzod qoidani oʻzi topadi. Bitta ovozda oʻqiladigan kichik uy sahnasi."
        ),
        "order":   8,
        "grammar": [
            {
                "pattern":  "он / она́ / оно́",
                "meaning":  "Ot oʻrniga turadigan olmosh, otning JINSIGA qarab tanlanadi: "
                            "erkak jinsi — он, ayol jinsi — она́, oʻrta jins — оно́. "
                            "Buyumlar uchun ham shunday: стол — он, кни́га — она́.",
                "examples": ["Стол — он.", "Кни́га — она́.", "Окно́ — оно́."],
            },
            {
                "pattern":  "Jinsni oxirgi harfdan aniqlash",
                "meaning":  "Undosh bilan tugasa — erkak jinsi (стол, кот). -а / -я bilan "
                            "tugasa — ayol jinsi (кни́га, ла́мпа). -о / -е bilan tugasa — "
                            "oʻrta jins (окно́, кре́сло).",
                "examples": ["стол → он", "ла́мпа → она́", "кре́сло → оно́"],
            },
            {
                "pattern":  "-ь bilan tugagan otlar",
                "meaning":  "Bu otlarning jinsini oxirgi harf aytmaydi — ularni jinsi "
                            "bilan birga yodlash kerak. Дверь — ayol jinsi, слова́рь — "
                            "erkak jinsi.",
                "examples": ["дверь — она́", "слова́рь — он"],
            },
        ],
        "body": '''<p>Э́то <span class="cn-word" data-tr="xona">ко́мната</span>. Здесь <span class="cn-word" data-pos="verb" data-tr="yashaydi">живёт</span> Дилно́за. Бекзо́д — <span class="cn-word" data-tr="uka">брат</span>. Бекзо́д <span class="cn-word" data-pos="verb" data-tr="keldi">пришёл</span> и <span class="cn-word" data-pos="verb" data-tr="dedi">сказа́л</span>: «Дилно́за, что э́то?»</p>

<p>Дилно́за <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказа́ла</span>: «Э́то <span class="cn-word" data-tr="stol">стол</span>. Стол — <strong>он</strong>».</p>

<p>«А кни́га?» — сказа́л Бекзо́д.</p>

<p>«Кни́га — <strong>она́</strong>».</p>

<p>«А <span class="cn-word" data-tr="deraza">окно́</span>?»</p>

<p>«Окно́ — <strong>оно́</strong>. Стол, кни́га, окно́ — три <span class="cn-word" data-tr="jins (grammatik)">ро́да</span>».</p>

<p>Бекзо́д сказа́л: «А Ба́рсик? Ба́рсик — он и́ли она́?»</p>

<p>Дилно́за сказа́ла: «Ба́рсик — кот. Кот — <strong>он</strong>».</p>

<p>Бекзо́д <span class="cn-word" data-pos="verb" data-tr="dedi">сказа́л</span>: «Тогда́ <span class="cn-word" data-tr="chiroq, lampa">ла́мпа</span> — она́. И <span class="cn-word" data-tr="kreslo">кре́сло</span> — оно́. И <span class="cn-word" data-tr="eshik">дверь</span> — она́!»</p>

<p>Дилно́за сказа́ла: «Да, Бекзо́д. Дверь — она́. Э́то <span class="cn-word" data-tr="toʻgʻri">пра́вильно</span>».</p>''',
        "questions": [
            {
                "text": "Nega Dilnoza stol haqida «он» dedi?",
                "choices": [
                    "Chunki «стол» undosh bilan tugaydi — bu erkak jinsi",
                    "Chunki stolni Bekzod yasagan",
                    "Chunki stol katta",
                    "Chunki barcha buyumlar haqida «он» deyiladi"
                ],
                "answer": 0,
                "explanation": "Jinsni soʻzning oxirgi harfi aytadi. Undosh bilan tugagan "
                               "ot — erkak jinsi, demak uning olmoshi «он». Bu buyumning "
                               "oʻziga emas, SOʻZGA tegishli: oʻzbekchada bunday boʻlinish "
                               "umuman yoʻq.",
            },
            {
                "text": "Bekzod oxirida qanday qoidani topdi?",
                "choices": [
                    "-а bilan tugasa она́, -о bilan tugasa оно́",
                    "Katta narsalar — он, kichiklari — она́",
                    "Xonadagi hamma narsa — оно́",
                    "Hayvonlar — она́, buyumlar — он"
                ],
                "answer": 0,
                "explanation": "Bekzod «ла́мпа — она́, кре́сло — оно́» dedi — yaʼni "
                               "oxirgi harfga qarab jinsni oʻzi aniqladi. Aynan shu "
                               "PR-8 darsining asosiy qoidasi.",
            },
            {
                "text": "Matndagi «дверь» soʻzi qaysi jinsda va nega uni alohida yodlash "
                        "kerak?",
                "choices": [
                    "Ayol jinsida — chunki -ь bilan tugagan otlarning jinsini oxirgi "
                    "harf aytmaydi",
                    "Erkak jinsida — chunki undosh bilan tugaydi",
                    "Oʻrta jinsda — chunki bu buyum",
                    "Uning jinsi yoʻq"
                ],
                "answer": 0,
                "explanation": "«Дверь» — ayol jinsi. -ь bilan tugagan otlar ham erkak "
                               "(слова́рь, день), ham ayol (дверь, ночь) jinsida boʻlishi "
                               "mumkin, shuning uchun ularni jinsi bilan birga yodlash "
                               "kerak — xuddi urgʻu kabi.",
            },
        ],
    },
]
