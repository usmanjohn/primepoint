# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-6 … PR-8.

Har bir matn oʻz darsining grammatikasini kamida ikki marta koʻrsatadi va faqat
oʻsha darsgacha oʻrganilgan qoliplardan foydalanadi (kumulyativ qoida).
Toc: corner/management/commands/toc_prime_russian_readings.txt

Bu uch matnda hali feʼl tizimi ochilmagan (u PR-19 dan boshlanadi), shuning uchun
tocdagi "narrative frame" istisnosidan foydalanilgan: есть · нет · зовут · живёт ·
работает · говорит · сказал(а) · пришёл/пришла · дал(а) · был/была — hammasi
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
        "title":   "Кто это?",
        "summary": (
            "PR-6 matni. Dilnoza Jasurga sinf fotosuratini koʻrsatadi. Har bir savol — "
            "«Кто это?» yoki «Что это?», va oxirida Jasur bitta narsani adashtiradi. "
            "Suhbat shaklidagi matn: audio ikki ovozda oʻqiladi."
        ),
        "order":   6,
        "grammar": [
            {
                "pattern":  "Это + ot",
                "meaning":  "«Bu — …». Rus tilida hozirgi zamonda “boʻlmoq” feʼli "
                            "qoʻyilmaydi, shuning uchun ikkita soʻz toʻliq gap boʻladi — "
                            "xuddi oʻzbekchadagi «Bu — uy» kabi.",
                "examples": ["Это школа.", "Это Шербек.", "Это кот."],
            },
            {
                "pattern":  "Кто это? / Что это?",
                "meaning":  "Odam va hayvon haqida — КТО (kim). Buyum, joy va tushuncha "
                            "haqida — ЧТО (nima). Oʻzbekchadagi «kim?» va «nima?» bilan "
                            "bir xil boʻlinish; farqi shundaki, hayvon ruschada КТО "
                            "tomonda turadi.",
                "examples": ["Кто это? — Это Афсона.", "Что это? — Это школа."],
            },
            {
                "pattern":  "Нет, это не …",
                "meaning":  "Rad javobi. НЕТ — «yoʻq» degan javob, НЕ esa inkor "
                            "qilinayotgan soʻzning OLDIDA turadi (oʻzbekchadagi «emas» "
                            "gap oxirida keladi, ruschada esa oldinda).",
                "examples": ["Нет, это не собака.", "Нет, это не Жасур."],
            },
        ],
        "body": '''<p><strong>Дилноза:</strong> Жасур, <strong>кто это</strong>?</p>

<p><strong>Жасур:</strong> <strong>Это</strong> Шербек. Шербек — <span class="cn-word" data-tr="doʻst">друг</span>.</p>

<p><strong>Дилноза:</strong> А это кто?</p>

<p><strong>Жасур:</strong> Это Афсона. Афсона — <span class="cn-word" data-tr="opa-singil">сестра</span>.</p>

<p><strong>Дилноза:</strong> А <strong>что это</strong>?</p>

<p><strong>Жасур:</strong> Это <span class="cn-word" data-tr="maktab">школа</span>. Здесь <span class="cn-word" data-pos="verb" data-tr="oʻqiydi, yashaydi (bu yerda: bor)">живёт</span> Афсона. Это Ташкент.</p>

<p><strong>Дилноза:</strong> А это собака?</p>

<p><strong>Жасур:</strong> <strong>Нет, это не</strong> <span class="cn-word" data-tr="it">собака</span>. Это <span class="cn-word" data-tr="mushuk">кот</span>. Кота <span class="cn-word" data-pos="verb" data-tr="chaqirishadi, ismi">зовут</span> Барсик.</p>

<p><strong>Дилноза:</strong> Барсик — кот? Не собака?</p>

<p><strong>Жасур:</strong> Да, Барсик — кот. И Барсик — тоже друг.</p>''',
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
                "explanation": "Jasur «Шербек — друг» dedi, yaʼni “Sherbek — doʻst”. "
                               "Diqqat qiling: bu ikki soʻzli toʻliq gap, orasida hech "
                               "qanday feʼl yoʻq.",
            },
            {
                "text": "Nega Dilnoza maktab haqida «Кто это?» emas, «Что это?» deb "
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
                               "это?». Aynan shuning uchun mushuk haqida esa «Кто "
                               "это?» soʻralar edi — hayvon КТО tomonda.",
            },
            {
                "text": "«Нет, это не собака» gapida НЕ soʻzi qayerda turibdi?",
                "choices": [
                    "Inkor qilinayotgan soʻzning oldida",
                    "Gap oxirida",
                    "Gap boshida",
                    "Bu gapda НЕ umuman yoʻq"
                ],
                "answer": 0,
                "explanation": "НЕ har doim oʻzi inkor qilayotgan soʻzning OLDIDA turadi: "
                               "не собака. Oʻzbekchadagi «emas» gap oxirida keladi "
                               "(«bu it emas»), ruschada esa oldinda — shuning uchun bu "
                               "joyda koʻp xato qilinadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-7 — ты / вы                        DIALOG (ikki ovoz)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Два разговора",
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
                "examples": ["Как тебя зовут? (doʻstga)",
                             "Как вас зовут? (oʻqituvchiga)"],
            },
            {
                "pattern":  "Привет / Здравствуйте",
                "meaning":  "Salomlashishning ikki darajasi. ПРИВЕТ — doʻstga, "
                            "ЗДРАВСТВУЙТЕ — hurmat bilan. Talaffuzda oʻrtadagi В "
                            "aytilmaydi: [здраствуйт'е].",
                "examples": ["Привет, Жасур!", "Здравствуйте, Сергей Петрович!"],
            },
            {
                "pattern":  "Пока / До свидания",
                "meaning":  "Xayrlashishning ikki darajasi, salomlashish bilan juftlashadi. "
                            "Bir suhbatda bitta darajada qolish kerak: Привет → Пока, "
                            "Здравствуйте → До свидания.",
                "examples": ["Пока, Жасур!", "До свидания!"],
            },
        ],
        "body": '''<p><strong>Жасур:</strong> <strong>Привет</strong>, Афсона! Как <span class="cn-word" data-tr="ishlar">дела</span>?</p>

<p><strong>Афсона:</strong> Привет, Жасур! <span class="cn-word" data-tr="yaxshi">Хорошо</span>. А <strong>ты</strong>?</p>

<p><strong>Жасур:</strong> <span class="cn-word" data-tr="normal, yomon emas">Нормально</span>. Афсона, это Дилноза. Дилноза — сестра.</p>

<p><strong>Афсона:</strong> <span class="cn-word" data-tr="juda">Очень</span> <span class="cn-word" data-tr="yoqimli">приятно</span>! Ну, <strong>пока</strong>!</p>

<p><strong>Сергей Петрович:</strong> <strong>Здравствуйте</strong>! <span class="cn-word" data-tr="kechirasiz">Извините</span>, как <strong>вас</strong> <span class="cn-word" data-pos="verb" data-tr="chaqirishadi, ismingiz">зовут</span>?</p>

<p><strong>Афсона:</strong> Здравствуйте! <span class="cn-word" data-tr="meni">Меня</span> зовут Афсона.</p>

<p><strong>Сергей Петрович:</strong> Очень приятно, Афсона. Это <span class="cn-word" data-tr="lugʻat">словарь</span>. <span class="cn-word" data-tr="marhamat, iltimos">Пожалуйста</span>.</p>

<p><strong>Афсона:</strong> <span class="cn-word" data-tr="rahmat">Спасибо</span>! <strong>До свидания</strong>, Сергей Петрович!</p>''',
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
                "text": "Afsona Jasur bilan «Пока», oʻqituvchi bilan «До свидания» deb "
                        "xayrlashdi. Bu nimani koʻrsatadi?",
                "choices": [
                    "Xayrlashish salomlashish bilan bir darajada boʻlishi kerak",
                    "«Пока» faqat ertalab aytiladi",
                    "«До свидания» faqat maktabda aytiladi",
                    "Ikkalasi bir xil, farqi yoʻq"
                ],
                "answer": 0,
                "explanation": "Bir suhbatda bitta darajada qolinadi: Привет → Пока "
                               "(norasmiy), Здравствуйте → До свидания (rasmiy). "
                               "Rasmiy salomlashib, norasmiy xayrlashish gʻalati "
                               "eshitiladi.",
            },
            {
                "text": "Sergey Petrovich «Как вас зовут?» dedi. Bu soʻzma-soʻz nima "
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
                               "hech qachon oʻzgarmaydi — «Как зовут вас?» deyilmaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-8 — род                            HIKOYA (bitta ovoz)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Стол, книга и окно",
        "summary": (
            "PR-8 matni. Bekzod hali kichkina va u har bir narsa haqida «он mi yoki "
            "она mi?» deb soʻrayveradi. Opasi Dilnoza javob beradi — va oxirida "
            "Bekzod qoidani oʻzi topadi. Bitta ovozda oʻqiladigan kichik uy sahnasi."
        ),
        "order":   8,
        "grammar": [
            {
                "pattern":  "он / она / оно",
                "meaning":  "Ot oʻrniga turadigan olmosh, otning JINSIGA qarab tanlanadi: "
                            "erkak jinsi — он, ayol jinsi — она, oʻrta jins — оно. "
                            "Buyumlar uchun ham shunday: стол — он, книга — она.",
                "examples": ["Стол — он.", "Книга — она.", "Окно — оно."],
            },
            {
                "pattern":  "Jinsni oxirgi harfdan aniqlash",
                "meaning":  "Undosh bilan tugasa — erkak jinsi (стол, кот). -а / -я bilan "
                            "tugasa — ayol jinsi (книга, лампа). -о / -е bilan tugasa — "
                            "oʻrta jins (окно, кресло).",
                "examples": ["стол → он", "лампа → она", "кресло → оно"],
            },
            {
                "pattern":  "-ь bilan tugagan otlar",
                "meaning":  "Bu otlarning jinsini oxirgi harf aytmaydi — ularni jinsi "
                            "bilan birga yodlash kerak. Дверь — ayol jinsi, словарь — "
                            "erkak jinsi.",
                "examples": ["дверь — она", "словарь — он"],
            },
        ],
        "body": '''<p>Это <span class="cn-word" data-tr="xona">комната</span>. Здесь <span class="cn-word" data-pos="verb" data-tr="yashaydi">живёт</span> Дилноза. Бекзод — <span class="cn-word" data-tr="uka">брат</span>. Бекзод <span class="cn-word" data-pos="verb" data-tr="keldi">пришёл</span> и <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span>: «Дилноза, что это?»</p>

<p>Дилноза <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказала</span>: «Это <span class="cn-word" data-tr="stol">стол</span>. Стол — <strong>он</strong>».</p>

<p>«А книга?» — сказал Бекзод.</p>

<p>«Книга — <strong>она</strong>».</p>

<p>«А <span class="cn-word" data-tr="deraza">окно</span>?»</p>

<p>«Окно — <strong>оно</strong>. Стол, книга, окно — три <span class="cn-word" data-tr="jins (grammatik)">рода</span>».</p>

<p>Бекзод сказал: «А Барсик? Барсик — он или она?»</p>

<p>Дилноза сказала: «Барсик — кот. Кот — <strong>он</strong>».</p>

<p>Бекзод <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span>: «Тогда <span class="cn-word" data-tr="chiroq, lampa">лампа</span> — она. И <span class="cn-word" data-tr="kreslo">кресло</span> — оно. И <span class="cn-word" data-tr="eshik">дверь</span> — она!»</p>

<p>Дилноза сказала: «Да, Бекзод. Дверь — она. Это <span class="cn-word" data-tr="toʻgʻri">правильно</span>».</p>''',
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
                    "-а bilan tugasa она, -о bilan tugasa оно",
                    "Katta narsalar — он, kichiklari — она",
                    "Xonadagi hamma narsa — оно",
                    "Hayvonlar — она, buyumlar — он"
                ],
                "answer": 0,
                "explanation": "Bekzod «лампа — она, кресло — оно» dedi — yaʼni "
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
                               "(словарь, день), ham ayol (дверь, ночь) jinsida boʻlishi "
                               "mumkin, shuning uchun ularni jinsi bilan birga yodlash "
                               "kerak — xuddi urgʻu kabi.",
            },
        ],
    },
]
