# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-47 … PR-49.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 47 — oʻyin (dialog), 48 — hikoya, 49 — kalendar
(roʻyxat shaklidagi matn). (44 sayohat qaydlari, 45 tajriba, 46 xat edi.)

Grammatika chegarasi (kumulyativ qoida):
  47-matn: soʻroq soʻzlarining kelishiklari. «Yigirma savol» oʻyini bu
           uchun ideal janr — matn deyarli butunlay savollardan iborat,
           va har bir savol boshqa kelishikda.
  48-matn: predloglar xaritasi. Metroda adashish hikoyasi — har bir
           jumlada boshqa predlog, va oxirida ularning barchasi bitta
           yoʻnalishga olib keladi.
  49-matn: vaqt ifodalari. Kalendar janri toʻrtta kelishikni tabiiy
           ravishda bir sahifaga sigʻdiradi: в январе · в субботу ·
           летом · пятого мая.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_47_49.py --author=prime
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
    # PR-47 — soʻroq soʻzlari                    OʻYIN
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Игра «Двадцать вопросов»",
        "summary": (
            "PR-47 matni. Sinf «Yigirma savol» oʻyinini oʻynaydi: bir kishi "
            "odamni oʻylaydi, qolganlar savol beradi. Butun matn savollardan "
            "iborat — va har biri boshqa kelishikda."
        ),
        "order":   47,
        "grammar": [
            {
                "pattern":  "Savol = javob kutilayotgan kelishik",
                "meaning":  "Кого ты ждёшь? — Брата. Кому ты пишешь? — Брату. "
                            "Savol qanday kelishikda boʻlsa, javob ham oʻsha "
                            "kelishikda. Predlog ham savoldan javobga koʻchadi.",
                "examples": ["Кого ты думаешь?", "С кем он работает?"],
            },
            {
                "pattern":  "кто → кого · что → чего",
                "meaning":  "КТО jonli otlar kabi turlanadi (Р.п. = В.п. = кого), "
                            "ЧТО esa jonsizlar kabi (Р.п. чего, lekin В.п. что). "
                            "PR-32 dagi jonlilik qoidasi bu yerda ham ishlaydi.",
                "examples": ["Кого вы знаете?", "О чём он пишет?"],
            },
            {
                "pattern":  "чей / чья / чьё / чьи",
                "meaning":  "«Kimniki?» — otga jins va son boʻyicha moslashadi, "
                            "xuddi мой kabi: чей дом, чья книга, чьё окно, чьи "
                            "ключи.",
                "examples": ["Чья это фотография?"],
            },
        ],
        "body": '''<p>В пятницу Марина Олеговна <span class="cn-word" data-pos="verb" data-tr="taklif qildi">предложила</span> <span class="cn-word" data-tr="oʻyin">игру</span>.</p>

<p>— Один человек думает о человеке. Другие <span class="cn-word" data-pos="verb" data-tr="topishadi">угадывают</span>. Двадцать вопросов. Ответы только «да» или «нет».</p>

<p><span class="cn-word" data-pos="verb" data-tr="oʻylaydi">Думает</span> Жасур. Класс спрашивает <span class="cn-word" data-tr="navbat bilan">по очереди</span>.</p>

<p>Афсона: — Это <span class="cn-word" data-tr="erkak">мужчина</span>?</p>

<p>Жасур: — Да.</p>

<p>Бекзод: — <strong>Кого</strong> он учит? Детей?</p>

<p>Марина Олеговна: — Бекзод, это не вопрос «да или нет».</p>

<p>Бекзод: — Извините. Он учит детей?</p>

<p>— Да.</p>

<p>Катя: — Он работает <strong>с ними</strong> каждый день?</p>

<p>— Да.</p>

<p>Дилноза: — <strong>О ком</strong> все говорят в нашем классе?</p>

<p>Класс <span class="cn-word" data-pos="verb" data-tr="kulishdi">засмеялся</span>.</p>

<p>— Это тоже не вопрос, — сказала Марина Олеговна. Но она <span class="cn-word" data-pos="verb" data-tr="jilmaydi">улыбнулась</span>.</p>

<p>Бекзод: — Он в этой <span class="cn-word" data-tr="xona">комнате</span>?</p>

<p>Жасур: — Да.</p>

<p>Тишина. Потом все посмотрели в одну <span class="cn-word" data-tr="tomon">сторону</span>.</p>

<p>— <strong>Чей</strong> это был <span class="cn-word" data-tr="fikr, gʻoya">вопрос</span>? — спросила Марина Олеговна.</p>

<p>— Бекзода, — сказал класс.</p>

<p>Шесть вопросов. Не двадцать.</p>''',
        "questions": [
            {
                "text": "Jasur kim haqida oʻylagan edi?",
                "choices": [
                    "Marina Olegovna — oʻqituvchining oʻzi haqida",
                    "Bekzod haqida",
                    "Oʻz akasi haqida",
                    "Maktab direktori haqida"
                ],
                "answer": 0,
                "explanation": "Savollar ketma-ket koʻrsatadi: erkak — bolalarni "
                               "oʻqitadi — har kuni ular bilan ishlaydi — shu xonada. "
                               "Shundan keyin «все посмотрели в одну сторону». "
                               "Oʻqituvchining oʻzi javob ekan.",
            },
            {
                "text": "Nega Bekzodning birinchi savoli qabul qilinmadi?",
                "choices": [
                    "«Кого он учит?» — bu «ha yoki yoʻq» savoli emas",
                    "Savol juda qiyin edi",
                    "Bekzod navbatini kutmadi",
                    "Savol notoʻgʻri tuzilgan edi"
                ],
                "answer": 0,
                "explanation": "Oʻyin qoidasi: «Ответы только „да“ или „нет“». "
                               "«Кого?» ochiq savol — unga «ha» deb javob berib "
                               "boʻlmaydi. Bekzod darrov tuzatdi: «Он учит детей?»",
            },
            {
                "text": "«Кого он учит?» va «О ком все говорят?» — nega bir xil "
                        "soʻz ikki xil koʻrinadi?",
                "choices": [
                    "Кого — Винительный, о ком — Предложный",
                    "Bittasi koʻplik",
                    "Bittasi oʻtgan zamon",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Soʻroq soʻzi javob kutilayotgan kelishikda beriladi. "
                               "«Учить кого?» — Винительный. «Говорить о ком?» — "
                               "Предложный, va predlog ham savolga koʻchadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-48 — predloglar xaritasi                HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Как я потерялся в метро",
        "summary": (
            "PR-48 matni. Metroda birinchi marta: chiqish, oʻtish, yana chiqish "
            "— va har bir qadam boshqa predlog. Yordam kutilmagan tomondan "
            "keladi."
        ),
        "order":   48,
        "grammar": [
            {
                "pattern":  "Predlog kelishikni tanlaydi",
                "meaning":  "в метро (П.п.), из метро (Р.п.), к выходу (Д.п.), "
                            "под землёй (Т.п.). Har bir predlog oʻz kelishigini "
                            "talab qiladi — bu butun tizimning kaliti.",
                "examples": ["Я стою в метро.", "Я иду к выходу."],
            },
            {
                "pattern":  "в ↔ из · на ↔ с · к ↔ от",
                "meaning":  "Antonim juftliklar. Soʻz В olsa, «dan» uchun ИЗ; НА "
                            "olsa — С; odam tomon К boʻlsa, odamdan ОТ.",
                "examples": ["Из метро на улицу.", "От станции к станции."],
            },
            {
                "pattern":  "Harakat bor / harakat yoʻq",
                "meaning":  "Bir xil predlog ikki kelishik olishi mumkin. Harakat "
                            "yoʻq — joy kelishigi (в метро), harakat bor — "
                            "Винительный (в метро — kirish).",
                "examples": ["Я иду через переход."],
            },
        ],
        "body": '''<p>Первый день <strong>в</strong> большом городе. Я <strong>в</strong> метро.</p>

<p>Здесь <strong>под</strong> <span class="cn-word" data-tr="yer">землёй</span> есть <span class="cn-word" data-tr="butun">целый</span> город. Люди идут <strong>по</strong> <span class="cn-word" data-tr="oʻtish yoʻli">переходу</span> быстро. Никто не стоит.</p>

<p>Я иду <strong>к</strong> <span class="cn-word" data-tr="chiqish">выходу</span>. Но выходов здесь <span class="cn-word" data-tr="sakkiz">восемь</span>.</p>

<p>Я иду <strong>из</strong> перехода <strong>на</strong> улицу. Это не моя улица.</p>

<p>Я иду <strong>с</strong> улицы обратно <strong>в</strong> метро.</p>

<p>Теперь я иду <strong>через</strong> другой переход. <strong>Рядом с</strong> ним <span class="cn-word" data-tr="xarita">карта</span>. Но <strong>на</strong> карте <span class="cn-word" data-tr="oʻttiz">тридцать</span> станций.</p>

<p>Я стою <strong>перед</strong> картой десять минут.</p>

<p><strong>Ко</strong> мне подходит <span class="cn-word" data-tr="keksa ayol">старая женщина</span> <strong>с</strong> <span class="cn-word" data-tr="paketlar">пакетами</span>.</p>

<p>— Вам куда? — спрашивает она.</p>

<p>Я говорю <span class="cn-word" data-tr="manzil">адрес</span>.</p>

<p>— А, это <strong>за</strong> рынком, — говорит она. — Идите <strong>до</strong> станции «Парк», потом <strong>от</strong> <span class="cn-word" data-tr="bekat">станции</span> <span class="cn-word" data-tr="chapga">налево</span>. Выход номер три.</p>

<p>Я иду. Станция «Парк». Выход номер три. Рынок.</p>

<p>И <strong>за</strong> рынком — мой дом.</p>

<p>Теперь я знаю: <strong>в</strong> большом городе карта помогает. Но человек помогает лучше.</p>''',
        "questions": [
            {
                "text": "Kim adashgan odamga yordam berdi?",
                "choices": [
                    "Paketlar koʻtargan keksa ayol",
                    "Metro xodimi",
                    "Devordagi xarita",
                    "Politsiyachi"
                ],
                "answer": 0,
                "explanation": "«Ко мне подходит старая женщина с пакетами». U "
                               "aniq yoʻriqnoma berdi: bekatgacha, keyin chapga, "
                               "uchinchi chiqish. Matn shu bilan tugaydi: «Человек "
                               "помогает лучше».",
            },
            {
                "text": "«Из перехода» va «с улицы» — nega ikki xil predlog?",
                "choices": [
                    "Переход В oladi (→ ИЗ), улица esa НА oladi (→ С)",
                    "Chunki bittasi ayol jinsida",
                    "Chunki bittasi koʻplik",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "PR-30 dagi В/НА roʻyxati bu yerda ham ishlaydi: «в "
                               "переходе» → «из перехода»; «на улице» → «с "
                               "улицы». Antonim juftliklar shu qoidaga tayanadi.",
            },
            {
                "text": "Matnda «за рынком» ikki marta uchraydi. Nega bu shakl "
                        "oʻzgarmadi?",
                "choices": [
                    "Ikkalasida ham harakat yoʻq — joy koʻrsatilyapti (Т.п.)",
                    "Chunki «рынок» erkak jinsida",
                    "Chunki bu ism",
                    "Ikkinchisi xato boʻlishi kerak"
                ],
                "answer": 0,
                "explanation": "ЗА ikki kelishik oladi. Harakat boʻlsa Винительный "
                               "(«идти за дом»), harakat boʻlmasa Творительный "
                               "(«за рынком» — bozor orqasida joylashgan). Matnda "
                               "ikkalasi ham joy maʼnosida.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-49 — vaqt ifodalari                     KALENDAR
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Календарь Нины",
        "summary": (
            "PR-49 matni. Ninaning bir yili — bitta sahifada. Har bir oyda bir "
            "voqea, va oxirida maʼlum boʻladiki, kalendarda bitta kun boʻsh "
            "qolgan."
        ),
        "order":   49,
        "grammar": [
            {
                "pattern":  "в + Предложный — oy va yil",
                "meaning":  "в январе, в мае, в 2026 году. Uzun vaqt joy kabi "
                            "koʻriladi: «uning ichida». ГОД -У oladi: в году.",
                "examples": ["В январе Нина начала работу.", "В 2026 году."],
            },
            {
                "pattern":  "в + Винительный — hafta kuni va soat",
                "meaning":  "в субботу, во вторник, в два часа. Qisqa vaqt nuqta "
                            "kabi koʻriladi. ВО — ikki undoshdan oldin.",
                "examples": ["В субботу — театр.", "Во вторник экзамен."],
            },
            {
                "pattern":  "Творительный — fasl va kun qismi",
                "meaning":  "летом, зимой, утром, вечером — predlogsiz. Bular "
                            "Творительный padejida qotib qolgan ravishlar.",
                "examples": ["Летом она была в деревне.", "Утром — работа."],
            },
        ],
        "body": '''<p>У Нины есть <span class="cn-word" data-tr="kalendar">календарь</span>. Один год — одна <span class="cn-word" data-tr="sahifa">страница</span>.</p>

<p><strong>В январе</strong> она начала новую работу. Было холодно и <span class="cn-word" data-tr="qiyin">трудно</span>.</p>

<p><strong>В феврале</strong> — <span class="cn-word" data-tr="hech narsa">ничего</span>. Просто работа.</p>

<p><strong>В марте</strong> она <span class="cn-word" data-pos="verb" data-tr="sotib oldi">купила</span> велосипед. <strong>Утром</strong> — работа, <strong>вечером</strong> — <span class="cn-word" data-tr="park">парк</span>.</p>

<p><strong>В апреле</strong> <strong>во вторник</strong> у неё был экзамен. Она <span class="cn-word" data-pos="verb" data-tr="topshirdi">сдала</span>.</p>

<p><strong>Летом</strong> Нина была в деревне. <strong>В июне</strong>, <strong>в июле</strong> и <strong>в августе</strong>. Три месяца без города.</p>

<p><strong>В сентябре</strong> — снова работа. <strong>В октябре</strong> она <span class="cn-word" data-pos="verb" data-tr="uchrashdi">познакомилась</span> с Олегом.</p>

<p><strong>В ноябре</strong> они ходили в <span class="cn-word" data-tr="teatr">театр</span> <strong>в субботу</strong>. Каждую субботу.</p>

<p><strong>В декабре</strong> <strong>ночью</strong> шёл снег. Нина смотрела в окно и думала о годе.</p>

<p>Один год. Один велосипед. Один экзамен. Один Олег.</p>

<p>Но в календаре есть один <span class="cn-word" data-tr="boʻsh">пустой</span> день. <strong>Пятое мая</strong>.</p>

<p><strong>Пятого мая</strong> Нина ничего не делала. Она сидела дома и читала.</p>

<p>Теперь она думает: это был <span class="cn-word" data-tr="eng yaxshi">самый лучший</span> день <strong>в году</strong>.</p>''',
        "questions": [
            {
                "text": "Nina uchun yilning eng yaxshi kuni qaysi boʻldi?",
                "choices": [
                    "Beshinchi may — hech narsa qilmagan kuni",
                    "Yangi ish boshlagan kuni yanvarda",
                    "Imtihon topshirgan kuni aprelda",
                    "Oleg bilan tanishgan kuni oktyabrda"
                ],
                "answer": 0,
                "explanation": "Kalendarda bitta boʻsh kun qolgan edi — «Пятого мая "
                               "Нина ничего не делала». Va oxirgi jumla: «это был "
                               "самый лучший день в году». Yilning eng yaxshi kuni "
                               "yozilmagan kun ekan.",
            },
            {
                "text": "Nega «в мае», lekin «в субботу»?",
                "choices": [
                    "Oy Предложный oladi, hafta kuni esa Винительный",
                    "Ikkalasi bir xil kelishik",
                    "Chunki «суббота» ayol jinsida",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Rus tili vaqtni joy kabi koʻradi: uzun vaqt (oy, yil) "
                               "— «ichida», demak Предложный. Qisqa vaqt (kun, soat) "
                               "— «nuqtaga», demak Винительный.",
            },
            {
                "text": "«Летом», «утром», «ночью» — bu shakllarda nega predlog "
                        "yoʻq?",
                "choices": [
                    "Bular Творительный padejida qotib qolgan ravishlar",
                    "Chunki ular qisqa soʻzlar",
                    "Chunki predlog tushirib qoldirilgan",
                    "Chunki bular sifat"
                ],
                "answer": 0,
                "explanation": "Fasllar va kun qismlari Творительный shaklida "
                               "ishlatiladi va predlog olmaydi: летом, зимой, "
                               "утром, вечером, ночью. Oʻquvchi ularni PR-20 dan "
                               "beri ishlatib kelgan — endi nega bunday ekanini "
                               "biladi.",
            },
        ],
    },
]
