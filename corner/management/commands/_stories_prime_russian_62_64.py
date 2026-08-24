# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-62 … PR-64.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 62 — ilmiy-ommabop (til haqida), 63 — mahalla portreti
(hikoya), 64 — kichik voqea + xulosa. (59 qoʻllanma, 60 xat, 61 tarix edi —
demak uchta bir xil shakl ketma-ket kelmayapti.)

Grammatika chegarasi (kumulyativ qoida):
  62-matn: -ся ning oltita maʼnosi. ⚠️ КОТОРЫЙ bu matnda ATAY yoʻq —
           u faqat PR-63 da oʻrgatiladi, matn esa PR-62 ники.
  63-matn: который. Beshta kelishikda va predlog bilan: которого,
           который, у которого, к которому, с которым, в котором.
  64-matn: что va чтобы yonma-yon. Xat janri emas, xat HAQIDA voqea —
           shuning uchun «хотел, чтобы…» va «думал, что…» tabiiy
           ravishda bir matnga sigʻadi.

⚠️ FAKTLAR: 62-matndagi oʻzbek tili haqidagi daʼvo tekshirilgan —
oʻzbekchada -in- (oʻzlik), -ish- (birgalik) va -il- (majhul) uchta
alohida qoʻshimcha, ruschada esa bularning hammasi bitta -ся.
63 va 64 — toʻqima voqealar, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_62_64.py --author=prime
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
        "grammatikasini matn ichida koʻrsatadi. Lugʻat izohlari bilan."
    ),
    "order": 3,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PR-62 — -ся                                ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Шесть значений одной частицы",
        "summary": (
            "PR-62 matni. Ikki harf — «-ся» — va uning oltita vazifasi, "
            "bittadan misol bilan. Oxirida oʻzbek tili bilan solishtirish: "
            "bizda uchta qoʻshimcha, ruschada bitta."
        ),
        "order":   62,
        "grammar": [
            {
                "pattern":  "-ся ning oltita maʼnosi",
                "meaning":  "Oʻziga qaytish (моется), bir-biriga (встречаются), "
                            "majhul nisbat (строится), holat (спится), faqat -ся "
                            "bilan yashaydigan feʼllar (смеяться) va maʼno "
                            "oʻzgarishi (учить → учиться).",
                "examples": ["Он моется.", "Они встречаются."],
            },
            {
                "pattern":  "-ся feʼli obyekt olmaydi",
                "meaning":  "Он моет машину (obyekt bor) ↔ он моется (obyekt "
                            "yoʻq). Matnning ikkinchi bandi shu farq ustiga "
                            "qurilgan.",
                "examples": ["Он моет машину.", "Он моется."],
            },
            {
                "pattern":  "-ся ↔ oʻzbekcha -in-, -ish-, -il-",
                "meaning":  "Oʻzbekchada uchta alohida qoʻshimcha bor, ruschada "
                            "esa bitta. Shuning uchun oʻzbek oʻquvchisi bu "
                            "maʼnolarni rus bolasidan koʻra aniqroq ajratadi.",
                "examples": ["yuvinmoq → мыться", "koʻrishmoq → встречаться"],
            },
        ],
        "body": '''<p>В русском языке есть очень короткая <span class="cn-word" data-tr="qoʻshimcha, zarracha">частица</span> — <strong>-ся</strong>. Две буквы. Но работ у неё шесть.</p>

<p><strong>Первая работа.</strong> Человек делает что-то с собой. «Он моет машину» — здесь есть <span class="cn-word" data-tr="obyekt">объект</span>. «Он <strong>моется</strong>» — объекта нет, потому что объект — сам человек.</p>

<p><strong>Вторая.</strong> Люди делают что-то друг другу. Они <strong>встречаются</strong> в субботу. Они <strong>ссорятся</strong>, а потом <strong>мирятся</strong>. Один человек так не может — нужно как минимум двое.</p>

<p><strong>Третья.</strong> Кто делал — <span class="cn-word" data-tr="nomaʼlum">неизвестно</span> или не важно. Дом <strong>строится</strong>. Магазин <strong>открывается</strong> в девять. Кто именно открывает дверь, мы не говорим.</p>

<p><strong>Четвёртая.</strong> <span class="cn-word" data-tr="holat">Состояние</span>. «Мне не <strong>спится</strong>». «Мне <strong>хочется</strong> чая». Здесь никто не действует. Есть только человек и его состояние.</p>

<p><strong>Пятая.</strong> Есть глаголы, <span class="cn-word" data-tr="faqat">только</span> с -ся. <strong>Смеяться. Бояться. Надеяться. Улыбаться.</strong> Слова «смеять» в русском языке просто нет.</p>

<p><strong>Шестая.</strong> Значение <span class="cn-word" data-pos="verb" data-tr="oʻzgaradi">меняется</span>. <strong>Учить</strong> — так делает учитель. <strong>Учиться</strong> — так делает <span class="cn-word" data-tr="oʻquvchi">ученик</span>. Две буквы, и действие пошло в другую сторону.</p>

<p>Теперь <span class="cn-word" data-tr="eng qizigʻi">самое интересное</span>. В узбекском языке для этих значений есть <strong>три</strong> разных суффикса: один для <span class="cn-word" data-tr="birinchi">первого</span> значения, другой для второго, третий для третьего.</p>

<p>Русский язык в этом месте <span class="cn-word" data-tr="tejamkor">экономный</span>. Узбекский — <span class="cn-word" data-tr="aniqroq">точнее</span>.</p>

<p>Поэтому для вас эта тема не трудная. Вы уже знаете <span class="cn-word" data-tr="farqni">разницу</span> — вам нужно только запомнить, что здесь она пишется одинаково.</p>''',
        "questions": [
            {
                "text": "Nega «Он моется» gapida obyekt yoʻq?",
                "choices": [
                    "Chunki obyekt — odamning oʻzi",
                    "Chunki bu majhul nisbat",
                    "Chunki feʼl -ся bilan tugaydi va bu tasodifiy",
                    "Chunki gap toʻliq emas"
                ],
                "answer": 0,
                "explanation": "Matn buni ochiq aytadi: «объект — сам человек». "
                               "Bu -ся ning birinchi maʼnosi, oʻzbekcha "
                               "«yuvinmoq» dagi -in- bilan bir xil.",
            },
            {
                "text": "Matnga koʻra, «смеять» soʻzi haqida nima toʻgʻri?",
                "choices": [
                    "Bunday soʻz rus tilida umuman yoʻq",
                    "U eskirgan soʻz",
                    "U faqat kitobiy tilda ishlatiladi",
                    "U «смеяться» ning buyruq shakli"
                ],
                "answer": 0,
                "explanation": "«Слова „смеять“ в русском языке просто нет». Bu "
                               "beshinchi guruh — -ся siz yashamaydigan feʼllar.",
            },
            {
                "text": "Matnning oxirgi xulosasi nima?",
                "choices": [
                    "Oʻzbek tili farqlarni aniqroq koʻrsatadi, shuning uchun bu mavzu oʻzbek oʻquvchisi uchun qiyin emas",
                    "Rus tili oʻzbek tilidan qiyinroq",
                    "Oʻzbek tilida -ся ga oʻxshash qoʻshimcha yoʻq",
                    "Bu maʼnolarni yodlashning imkoni yoʻq"
                ],
                "answer": 0,
                "explanation": "«Русский язык экономный. Узбекский — точнее… вам "
                               "нужно только запомнить, что здесь она пишется "
                               "одинаково».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-63 — который                            MAHALLA PORTRETI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Человек, который чинил всё",
        "summary": (
            "PR-63 matni. Hovlida hamma taniydigan usta Shavkat-aka: u pul "
            "olmagan, lekin har kim undan biror narsa oʻrgangan. Koʻchib "
            "ketgach, hovli nima qilganini koʻrsatadigan hikoya."
        ),
        "order":   63,
        "grammar": [
            {
                "pattern":  "который — jins va son otdan",
                "meaning":  "Aniqlanayotgan ot erkak boʻlsa который, ayol boʻlsa "
                            "которая, koʻplik boʻlsa которые. Matnda uchalasi "
                            "ham bor.",
                "examples": ["человек, которого знали все",
                             "дверь, которая не закрывалась"],
            },
            {
                "pattern":  "который — kelishik oʻz gapidan",
                "meaning":  "Которого (koʻrdilar — kimni?), которому (bordilar — "
                            "kimga?), которым (bogʻlangan — kim bilan?). Kelishik "
                            "ergash gapdagi vazifaga qarab tanlanadi.",
                "examples": ["сосед, которому все звонили",
                             "мастер, которым гордился весь двор"],
            },
            {
                "pattern":  "Predlog который dan oldin",
                "meaning":  "У которого, в котором, с которым — predlog ergash "
                            "gap oxirida qolmaydi, u который bilan birga oldinga "
                            "koʻchadi. Vergul esa predlogdan oldin qoʻyiladi.",
                "examples": ["дом, в котором он жил", "старик, у которого был ключ"],
            },
        ],
        "body": '''<p>В нашем дворе жил человек, <strong>которого</strong> знали все. Его звали Шавкат-ака.</p>

<p>Шавкат-ака был <span class="cn-word" data-tr="usta">мастер</span>. Не тот мастер, <strong>который</strong> работает в мастерской и берёт деньги. Другой. Он просто чинил <span class="cn-word" data-tr="narsalar">вещи</span>, <strong>которые</strong> <span class="cn-word" data-pos="verb" data-tr="buzilardi">ломались</span> во дворе.</p>

<p>Дверь, <strong>которая</strong> не закрывалась. <span class="cn-word" data-tr="Kran">Кран</span>, <strong>который</strong> <span class="cn-word" data-pos="verb" data-tr="tomchilardi">капал</span>. Велосипед, <strong>у которого</strong> сломалась цепь. Лампа в подъезде, <strong>в котором</strong> всегда было темно.</p>

<p>Он был <span class="cn-word" data-tr="qoʻshni">сосед</span>, <strong>которому</strong> звонили первым. И он всегда приходил.</p>

<p>Денег Шавкат-ака не брал. Совсем. Но у него было одно <span class="cn-word" data-tr="shart">условие</span>: человек, <strong>которому</strong> он помогал, должен был стоять рядом и <span class="cn-word" data-pos="verb" data-tr="qaramoq">смотреть</span>.</p>

<p>— Смотри, — говорил он. — В следующий раз сделаешь сам.</p>

<p>Жасур, <strong>который</strong> жил на третьем этаже, так научился чинить кран. Дилноза, <strong>которая</strong> училась в школе, так научилась <span class="cn-word" data-pos="verb" data-tr="almashtirmoq">менять</span> лампу. Роза Каримовна, <strong>которой</strong> было семьдесят два года, так научилась <span class="cn-word" data-pos="verb" data-tr="ulamoq">клеить</span> мебель.</p>

<p>В прошлом году Шавкат-ака уехал к дочери в другой город.</p>

<p>Первую неделю двор ждал. Все думали, что теперь всё <span class="cn-word" data-pos="verb" data-tr="buziladi">сломается</span> и <span class="cn-word" data-pos="verb" data-tr="qoladi">останется</span> сломанным.</p>

<p>Но во вторую неделю Жасур починил кран у Нины Петровны. Дилноза <span class="cn-word" data-pos="verb" data-tr="almashtirdi">поменяла</span> лампу в подъезде. А Роза Каримовна <span class="cn-word" data-pos="verb" data-tr="tuzatdi">починила</span> стул, <strong>на котором</strong> сидела тридцать лет.</p>

<p>Мастер, <strong>которым</strong> гордился весь двор, уехал. А двор остался с руками.</p>

<p>Это и был его настоящий <span class="cn-word" data-tr="ish, mehnat">труд</span>.</p>''',
        "questions": [
            {
                "text": "Shavkat-akaning yagona sharti nima edi?",
                "choices": [
                    "U yordam bergan odam yonida turib qarab tursin",
                    "Ish haqi kichik boʻlsa ham toʻlansin",
                    "Uni oldindan telefon qilib chaqirishsin",
                    "Asboblarni qoʻshni bersin"
                ],
                "answer": 0,
                "explanation": "«Человек, которому он помогал, должен был стоять рядом и "
                               "смотреть». Va sababi keyingi qatorda: «В "
                               "следующий раз сделаешь сам».",
            },
            {
                "text": "Nima uchun matnda «у которого сломалась цепь» deyilgan, «которого» emas?",
                "choices": [
                    "Predlog «у» который bilan birga oldinga koʻchadi",
                    "Chunki velosiped jonsiz",
                    "Chunki bu koʻplik shakli",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Rus tilida predlog ergash gap oxirida qolmaydi — u "
                               "который bilan birga keladi. Vergul esa "
                               "predlogdan oldin qoʻyiladi.",
            },
            {
                "text": "Shavkat-aka ketgandan keyin hovlida nima boʻldi?",
                "choices": [
                    "Qoʻshnilar buzilgan narsalarni oʻzlari tuzata boshladi",
                    "Hovli yangi usta yolladi",
                    "Hech kim hech narsani tuzatmadi",
                    "Shavkat-aka har hafta qaytib kelib turdi"
                ],
                "answer": 0,
                "explanation": "Jasur kranni, Dilnoza lampani, Roza Karimovna esa "
                               "stulni tuzatdi — «двор остался с руками».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-64 — что / чтобы                        KICHIK VOQEA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Чтобы тебя поняли",
        "summary": (
            "PR-64 matni. Jasur maktab direktoriga xat yozadi va javob "
            "olmaydi. Sergey Petrovich xatni qayta yozdirmaydi — faqat uchta "
            "savol beradi."
        ),
        "order":   64,
        "grammar": [
            {
                "pattern":  "что — fakt",
                "meaning":  "Знать, думать, видеть, понимать feʼllaridan keyin "
                            "«что» keladi: bu axborot, sodir boʻlgan yoki "
                            "boʻladigan narsa.",
                "examples": ["Он думал, что письмо хорошее.",
                             "Теперь я знаю, что письмо было плохое."],
            },
            {
                "pattern":  "чтобы + oʻtgan zamon (ega boshqa)",
                "meaning":  "Хотеть, просить, нужно feʼllaridan keyin «чтобы», "
                            "va undan keyingi feʼl oʻtgan zamonda boʻladi — bu "
                            "oʻtmish emas, shunchaki shakl.",
                "examples": ["Он хотел, чтобы директор ответил.",
                             "Нужно, чтобы тебя поняли."],
            },
            {
                "pattern":  "чтобы + infinitiv (ega bir xil)",
                "meaning":  "Ikkala qismda ham ega bitta boʻlsa, «чтобы» dan keyin "
                            "infinitiv qoʻyiladi — oʻzbekcha «-sh uchun».",
                "examples": ["Он написал письмо, чтобы попросить новые мячи.",
                             "Пиши, чтобы тебя поняли."],
            },
        ],
        "body": '''<p>Жасур написал письмо <span class="cn-word" data-tr="direktorga">директору</span> школы. Он написал его, <strong>чтобы попросить</strong> новые мячи для спортзала. Старые мячи уже не <span class="cn-word" data-pos="verb" data-tr="sakramas edi">прыгали</span> — они стали <span class="cn-word" data-tr="yumshoq">мягкими</span>.</p>

<p>Он думал, <strong>что</strong> письмо хорошее. Оно было длинное — две <span class="cn-word" data-tr="sahifa">страницы</span>.</p>

<p>Он хотел, <strong>чтобы директор ответил</strong> быстро.</p>

<p>Директор не ответил. Ни через неделю, ни через две.</p>

<p>Тогда Жасур пошёл к Сергею Петровичу — учителю, который вёл у них русский язык.</p>

<p>— Прочитайте, пожалуйста. Я хочу, <strong>чтобы вы сказали</strong>, где ошибка.</p>

<p>Сергей Петрович прочитал письмо два раза. Потом он <span class="cn-word" data-pos="verb" data-tr="qoʻydi">положил</span> его на стол.</p>

<p>— Ошибок в <span class="cn-word" data-tr="grammatika">грамматике</span> нет, — сказал он. — Ни одной. Но я <span class="cn-word" data-pos="verb" data-tr="beraman">задам</span> три вопроса.</p>

<p>— Первый: что тебе нужно? Ответь одним <span class="cn-word" data-tr="jumla">предложением</span>.</p>

<p>Жасур <span class="cn-word" data-pos="verb" data-tr="oʻyladi">подумал</span> и сказал:</p>

<p>— Шесть мячей.</p>

<p>— Второй: в какой <span class="cn-word" data-tr="qatorda">строке</span> письма это написано?</p>

<p>Жасур посмотрел. Это было написано на второй странице, в конце.</p>

<p>— Третий: директор читает тридцать писем в день. До второй страницы он дошёл?</p>

<p>Жасур <span class="cn-word" data-pos="verb" data-tr="jim qoldi">замолчал</span>.</p>

<p>Вечером он написал новое письмо. Четыре строки. В первой строке — просьба. Во второй — <span class="cn-word" data-tr="sabab">причина</span>. В третьей — сколько стоит. В четвёртой — спасибо.</p>

<p>Ответ пришёл на следующий день.</p>

<p>Теперь Жасур знает, <strong>что</strong> длинное письмо — не всегда хорошее письмо.</p>

<p>Пиши не для того, <strong>чтобы сказать</strong>. Пиши для того, <strong>чтобы тебя поняли</strong>.</p>''',
        "questions": [
            {
                "text": "Nega direktor birinchi xatga javob bermadi?",
                "choices": [
                    "Xat uzun edi va asosiy iltimos ikkinchi sahifaning oxirida turardi",
                    "Xatda grammatik xatolar koʻp edi",
                    "Direktor xatni umuman olmadi",
                    "Iltimos juda qimmatga tushardi"
                ],
                "answer": 0,
                "explanation": "Sergey Petrovichning uchinchi savoli shuni "
                               "koʻrsatadi: «директор читает тридцать писем в "
                               "день. До второй страницы он дошёл?»",
            },
            {
                "text": "Nega matnda «Он хотел, чтобы директор ответил», lekin «Он думал, что письмо хорошее»?",
                "choices": [
                    "«Хотеть» istakni bildiradi — чтобы; «думать» faktni — что",
                    "Ikkalasi bir xil, farqi yoʻq",
                    "«Чтобы» faqat oʻtmish haqida ishlatiladi",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Xohlash, soʻrash, talab qilish — чтобы va undan "
                               "keyin oʻtgan zamon. Bilish, oʻylash, aytish — "
                               "что va oddiy zamonlar.",
            },
            {
                "text": "Ikkinchi xat qanday tuzilgan edi?",
                "choices": [
                    "Toʻrt qator: iltimos, sabab, narx, minnatdorchilik",
                    "Ikki sahifa, lekin xatosiz",
                    "Bir qator: «Menga olti dona toʻp kerak»",
                    "Direktorning savollariga javoblar"
                ],
                "answer": 0,
                "explanation": "«Четыре строки. В первой — просьба. Во второй — "
                               "причина. В третьей — сколько стоит. В "
                               "четвёртой — спасибо». Va javob ertasiga keldi.",
            },
        ],
    },
]
