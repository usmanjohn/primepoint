# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-86 … PR-88.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.
⛔ URGʻU BELGISI YOʻQ — 2026-08-24 dagi qaror.

Janr xilma-xilligi: 86 — ilmiy-ommabop (til haqida), 87 — intervyu
(uch kishi, uch kasb), 88 — kundalik hikoya (mehr haqida).
Toc da 87 «ilmiy-ommabop» deb turgan edi; 86 bilan ikki marta ketma-ket
bir xil shakl chiqmasligi uchun intervyuga aylantirildi — mavzu oʻsha,
suffiksli kasb nomlari, lekin ovozlar orqali koʻrsatiladi.

Grammatika chegarasi (kumulyativ qoida):
  86-matn: soʻz yasalishi — bir oʻzakdan chiqqan soʻzlar oilasi,
           приставка/корень/суффикс, чередование.
  87-matn: -тель / -щик / -чик / -ник / -ница suffikslari kasb
           nomlarida; -ство va -ение ham uchraydi.
  88-matn: kichraytiruvchi va erkalash shakllari — -ик, -ок, -очка,
           -ушка, -ышко, ismlarning uch pogʻonasi.

⚠️ ATAY QOCHILGAN (keyingi darslar): soʻz tartibi bilan oʻynash
(PR-89), rasmiy uslub namunalari (PR-90–91), frazeologizmlar (PR-94),
maqollar (PR-95).

⚠️ FAKTLAR:
  86-matn — lingvistik faktlar. -ход- oʻzagidan chiqqan soʻzlar
  (вход, выход, переход, пешеход, пароход, вездеход, доход, расход,
  походка, происходить) — hammasi rus tilining oddiy lugʻat soʻzlari.
  Moskva metrosidagi «Выход в город» yozuvi haqiqiy va har bekatda
  turadi. «Нет выхода» / «Выхода нет» ham haqiqiy yozuv.
  87-matn — toʻqima intervyu; kasb nomlari va ularning suffikslari
  haqiqiy (сварщик, учительница, переводчик, строитель, водитель).
  88-matn — toʻqima oilaviy hikoya, real daʼvo yoʻq. Машенька /
  Мария, Ванечка / Иван ism zanjirlari haqiqiy.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_86_88.py --author=prime
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
    # PR-86 — soʻz yasalishi                        ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Один корень — сорок слов",
        "summary": (
            "PR-86 matni. Rus tilidagi «-ход-» oʻzagi haqida ilmiy-ommabop "
            "matn: bitta qisqa oʻzakdan qanday qilib oʻnlab soʻz oʻsib "
            "chiqqani va nega buni bilgan odam lugʻatsiz oʻqiy oladi."
        ),
        "order":   86,
        "grammar": [
            {
                "pattern":  "приставка + корень + суффикс + окончание",
                "meaning":  "Rus soʻzi toʻrtta boʻlakdan qurilgan. Matnda "
                            "har bir soʻz shu boʻlaklarga ajratib koʻrsatiladi.",
                "examples": ["вы + ход = выход",
                             "пеш + е + ход = пешеход"],
            },
            {
                "pattern":  "однокоренные слова",
                "meaning":  "Bir oʻzakli soʻzlar. Ularni yigʻish — oʻzakni "
                            "topishning eng ishonchli usuli.",
                "examples": ["ходить, вход, выход, переход, походка",
                             "У всех этих слов один корень — ход."],
            },
            {
                "pattern":  "чередование",
                "meaning":  "Oʻzakdagi tovush almashinuvi: ходить → хожу, "
                            "снег → снежок. Bu boshqa oʻzak emas.",
                "examples": ["ходить — хожу", "снег — снежок"],
            },
        ],
        "body": '''<p>В русском языке есть очень короткий <span class="cn-word" data-tr="oʻzak">корень</span>. Всего три буквы: <strong>ход</strong>. Он означает «идти».</p>

<p>Теперь посмотрите, что из него выросло.</p>

<p>Вы <span class="cn-word" data-pos="verb" data-tr="kirasiz">входите</span> в здание — это <strong>вход</strong>. Вы <span class="cn-word" data-pos="verb" data-tr="chiqasiz">выходите</span> — это <strong>выход</strong>. Вы <span class="cn-word" data-pos="verb" data-tr="oʻtasiz">переходите</span> улицу — это <strong>переход</strong>.</p>

<p>Три слова, один корень, три разные <span class="cn-word" data-tr="prefikslar">приставки</span>. Приставка не меняет корень. Она только <span class="cn-word" data-pos="verb" data-tr="buradi">поворачивает</span> его в другую сторону.</p>

<p>Дальше — интереснее. Человек, который идёт <span class="cn-word" data-tr="piyoda">пешком</span>, — это <strong>пешеход</strong>. Судно, которое идёт на <span class="cn-word" data-tr="bugʻ">пару</span>, — <strong>пароход</strong>. Машина, которая идёт <span class="cn-word" data-tr="hamma joyda">везде</span>, — <strong>вездеход</strong>.</p>

<p>Здесь два корня <span class="cn-word" data-pos="verb" data-tr="birlashadi">соединяются</span> в одно слово, а между ними ставится <strong>о</strong> или <strong>е</strong>.</p>

<p>И даже деньги живут в этом корне. Что приходит в дом — <strong>доход</strong>. Что уходит из дома — <strong>расход</strong>.</p>

<p>Есть слово <strong>походка</strong> — то, как человек идёт. По походке узнают друга издалека.</p>

<p>Есть <span class="cn-word" data-pos="verb" data-tr="sodir boʻlmoq">происходить</span> — «случаться». Что-то идёт, идёт и наконец <span class="cn-word" data-pos="verb" data-tr="sodir boʻladi">происходит</span>.</p>

<p>Лингвисты <span class="cn-word" data-pos="verb" data-tr="sanashgan">насчитали</span> у этого корня больше сорока слов.</p>

<p>И вот <span class="cn-word" data-tr="asosiysi">главное</span>. Человек, который знает корень <strong>ход</strong> и десять приставок, читает незнакомое слово и <span class="cn-word" data-pos="verb" data-tr="tushunadi">понимает</span> его без <span class="cn-word" data-tr="lugʻat">словаря</span>.</p>

<p>В московском метро на каждой станции висит <span class="cn-word" data-tr="yozuv">надпись</span>: «Выход в город». Иностранец, который выучил один корень, читает её и знает, куда идти.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra, приставка oʻzak bilan nima qiladi?",
                "choices": [
                    "Uni butunlay oʻzgartiradi",
                    "Uni boshqa tomonga buradi, lekin oʻzgartirmaydi",
                    "Uni qisqartiradi",
                    "Unga hech qanday taʼsir qilmaydi"
                ],
                "answer": 1,
                "explanation": "«Приставка не меняет корень. Она только "
                               "поворачивает его в другую сторону». Shuning "
                               "uchun <em>вход</em>, <em>выход</em> va "
                               "<em>переход</em> — bitta oʻzak, uch yoʻnalish.",
            },
            {
                "text": "«Пароход» va «вездеход» soʻzlarida oʻrtadagi «о» nima uchun turibdi?",
                "choices": [
                    "Bu okonchaniye",
                    "Bu suffiks",
                    "Bu ikki oʻzakni birlashtiruvchi unli",
                    "Bu приставка"
                ],
                "answer": 2,
                "explanation": "«Здесь два корня соединяются в одно слово, а "
                               "между ними ставится о или е». <em>пар + о + "
                               "ход</em>, <em>пеш + е + ход</em>.",
            },
            {
                "text": "Matnning asosiy fikri nima?",
                "choices": [
                    "Moskva metrosi juda katta",
                    "Rus tilida juda koʻp soʻz bor",
                    "Oʻzakni va prefikslarni bilgan odam notanish soʻzni lugʻatsiz tushunadi",
                    "Chet elliklar rus tilini oʻrgana olmaydi"
                ],
                "answer": 2,
                "explanation": "Matn shu fikr bilan tugaydi: «Человек, который "
                               "знает корень ход и десять приставок, читает "
                               "незнакомое слово и понимает его без словаря». "
                               "Metro haqidagi misol — shuning isboti.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-87 — suffikslar                                    INTERVYU
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Профессии на -тель и -щик",
        "summary": (
            "PR-87 matni. Uch kishilik intervyu: сварщик Сергей, "
            "учительница Нина Ивановна va переводчик Олег oʻz kasblari "
            "haqida gapiradi. Har bir kasb nomi oʻz suffiksini koʻrsatadi."
        ),
        "order":   87,
        "grammar": [
            {
                "pattern":  "-тель · -щик / -чик · -ник",
                "meaning":  "Odam yasovchi suffikslar. Uchchalasi ham "
                            "oʻzbekcha «-chi / -uvchi» ga toʻgʻri keladi va "
                            "uchchalasi ham мужской род.",
                "examples": ["строитель, водитель, преподаватель",
                             "сварщик, переводчик, работник"],
            },
            {
                "pattern":  "-ница / -чица — ayol shakli",
                "meaning":  "Kundalik nutqda ayol kasbi shu suffiks bilan "
                            "beriladi: учитель → учительница.",
                "examples": ["Я учительница уже тридцать лет.",
                             "Моя дочь — переводчица."],
            },
            {
                "pattern":  "-ство va -ение",
                "meaning":  "Jarayon va mavhum ot yasaydi, ikkalasi ham "
                            "средний род: строительство, терпение.",
                "examples": ["Строительство шло два года.",
                             "Это работа требует терпения."],
            },
        ],
        "body": '''<p>Мы спросили трёх людей об их работе. Их <span class="cn-word" data-tr="kasb nomlari">названия профессий</span> заканчиваются по-разному — и это не случайно.</p>

<p><strong>Сергей, 46 лет, сварщик.</strong></p>

<p>— Я работал на большой <span class="cn-word" data-tr="qurilish">стройке</span>. Там были <strong>строители</strong>, <strong>водители</strong>, <strong>каменщики</strong>. Все на «-тель» и на «-щик». <strong>Строительство</strong> шло два года.</p>

<p>— Я <strong>сварщик</strong> двадцать три года. Отец тоже был <strong>сварщиком</strong>. Люди думают, что это простая работа. Это не так. Хороший <strong>сварщик</strong> видит <span class="cn-word" data-tr="chok">шов</span> и сразу знает, <span class="cn-word" data-pos="verb" data-tr="chidaydi">выдержит</span> он или нет. Этому <span class="cn-word" data-pos="verb" data-tr="oʻrgatishmaydi">не учат</span> за месяц. Мой <span class="cn-word" data-tr="yordamchi">помощник</span> работает третий год и только сейчас начал понимать.</p>

<p><strong>Нина Ивановна, 58 лет, учительница.</strong></p>

<p>— Я <strong>учительница</strong> начальных классов. Тридцать лет. В <span class="cn-word" data-tr="hujjatlarda">документах</span> пишут «<strong>учитель</strong>», а дети говорят «<strong>учительница</strong>». Мне <span class="cn-word" data-tr="yoqadi">нравится</span> второе. Эта работа требует <span class="cn-word" data-tr="sabr">терпения</span> больше, чем <span class="cn-word" data-tr="bilim">знаний</span>. Знания есть у всех. А <strong>терпение</strong> — не у всех.</p>

<p><strong>Олег, 31 год, переводчик.</strong></p>

<p>— Я <strong>переводчик</strong>, работаю с корейским. Меня часто <span class="cn-word" data-pos="verb" data-tr="yozishadi">пишут</span> «переводщик» — через «щ». Это <span class="cn-word" data-tr="xato">ошибка</span>. После «д» всегда «ч»: перево<strong>д</strong> — перевод<strong>чик</strong>. Как лёт<strong>чик</strong>, как рассказ<strong>чик</strong>.</p>

<p>— А вы <span class="cn-word" data-pos="verb" data-tr="tuzatasizmi">поправляете</span> людей?</p>

<p>— Раньше поправлял. Теперь нет. Но <span class="cn-word" data-tr="qiziq narsa">интересная вещь</span>: моя сестра — <strong>переводчица</strong>, и её так пишут <span class="cn-word" data-tr="toʻgʻri">правильно</span>. Почему-то в женском <span class="cn-word" data-tr="shaklda">роде</span> никто не ошибается.</p>

<p>Три человека, три <span class="cn-word" data-tr="qoʻshimcha">суффикса</span>. Сварщик, учительница, переводчик. Все трое делают <span class="cn-word" data-tr="butunlay boshqa">совершенно разную</span> работу — но каждое название говорит одно и то же: <span class="cn-word" data-tr="bu — odam">это человек</span>.</p>''',
        "questions": [
            {
                "text": "Sergeyning fikricha, yaxshi payvandchini nima ajratib turadi?",
                "choices": [
                    "U tez ishlaydi",
                    "U chokka qarab uning chidashini biladi",
                    "U koʻp asboblarni biladi",
                    "U yordamchisiz ishlaydi"
                ],
                "answer": 1,
                "explanation": "«Хороший сварщик видит шов и сразу знает, "
                               "выдержит он или нет. Этому не учат за месяц». "
                               "Sergey bu kasb koʻrinishidan qiyinroq "
                               "ekanini aytmoqchi.",
            },
            {
                "text": "Nega «переводчик» soʻzida «ч» yoziladi, «щ» emas?",
                "choices": [
                    "Chunki soʻz uzun",
                    "Chunki oʻzak «д» bilan tugaydi",
                    "Chunki bu chet soʻz",
                    "Chunki ayol shakli ham shunday"
                ],
                "answer": 1,
                "explanation": "Olegning oʻzi tushuntiradi: «После „д“ всегда "
                               "„ч“: перево<strong>д</strong> — "
                               "перевод<strong>чик</strong>. Как лётчик, как "
                               "рассказчик». Qoida: <em>д · т · з · с · ж</em> "
                               "dan keyin -чик.",
            },
            {
                "text": "Nina Ivanovna nima uchun «учительница» shaklini afzal koʻradi?",
                "choices": [
                    "Chunki hujjatlarda shunday yoziladi",
                    "Chunki bu qisqaroq",
                    "Chunki bolalar shunday deydi va unga shu yoqadi",
                    "Chunki bu rasmiyroq"
                ],
                "answer": 2,
                "explanation": "«В документах пишут „учитель“, а дети говорят "
                               "„учительница“. Мне нравится второе». Rasmiy "
                               "shakl — erkak jinsida, kundalik shakl esa "
                               "<em>-ница</em> bilan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-88 — kichraytirish                          KUNDALIK HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Бабушкины слова",
        "summary": (
            "PR-88 matni. Nevara buvisining hamma narsani kichraytirib "
            "gapirishidan gʻashi kelardi. Bir kuni u buvisining nega "
            "shunday gapirishini tushunadi."
        ),
        "order":   88,
        "grammar": [
            {
                "pattern":  "-ик · -ок · -очка · -ушка · -ышко",
                "meaning":  "Kichraytiruvchi va erkalovchi suffikslar. "
                            "Kichiklikni ham, mehrni ham bildiradi — "
                            "qaysi biri ekanini kontekst aytadi.",
                "examples": ["Садись, сынок, вот тебе хлебушек.",
                             "Солнышко моё, ты замёрз?"],
            },
            {
                "pattern":  "Ismning uch pogʻonasi",
                "meaning":  "Мария → Маша → Машенька: rasmiy, kundalik, "
                            "mehrli shakl. Buvi har doim uchinchisini tanlaydi.",
                "examples": ["Ванечка, иди сюда.",
                             "Машенька приехала на выходные."],
            },
            {
                "pattern":  "Kichraytirish — muloyimlik vositasi",
                "meaning":  "«Одну минуточку», «водички», «чайку» — soʻrov "
                            "kichraytirilgan shaklda yumshoqroq eshitiladi.",
                "examples": ["Подожди минуточку.",
                             "Налей мне водички."],
            },
        ],
        "body": '''<p>Ване было четырнадцать лет, и его <span class="cn-word" data-pos="verb" data-tr="asabiylashtirardi">раздражало</span>, как говорит бабушка.</p>

<p>Она не говорила «хлеб». Она говорила «<strong>хлебушек</strong>». Не «вода», а «<strong>водичка</strong>». Не «Ваня», а «<strong>Ванечка</strong>».</p>

<p>— Ванечка, <span class="cn-word" data-tr="choygina">чайку</span>?</p>

<p>— Бабушка, мне четырнадцать лет. Я не <strong>Ванечка</strong>.</p>

<p>Бабушка ничего не отвечала. Она просто ставила на стол <span class="cn-word" data-tr="stakancha">стаканчик</span> и <span class="cn-word" data-tr="likopcha">тарелочку</span>.</p>

<p>Летом бабушка <span class="cn-word" data-pos="verb" data-tr="ketdi">уехала</span> к сестре на неделю. Ваня остался один и решил <span class="cn-word" data-pos="verb" data-tr="tozalamoq">убрать</span> в квартире.</p>

<p>В <span class="cn-word" data-tr="shkaf">шкафу</span>, на верхней <span class="cn-word" data-tr="tokchada">полке</span>, он <span class="cn-word" data-pos="verb" data-tr="topdi">нашёл</span> старую <span class="cn-word" data-tr="quticha">коробочку</span>. В ней лежали <span class="cn-word" data-tr="xatlar">письма</span>.</p>

<p>Он взял одно и <span class="cn-word" data-pos="verb" data-tr="oʻqidi">прочитал</span>. Письмо было <span class="cn-word" data-pos="verb" data-tr="yozilgan">написано</span> в 1974 году. Бабушке тогда было двадцать лет, и она писала своей матери из <span class="cn-word" data-tr="uzoq shahar">далёкого города</span>, где училась.</p>

<p>«Мамочка, у меня всё хорошо. Комнатка маленькая, но тёплая. Купила себе <span class="cn-word" data-tr="paltocha">пальтишко</span>. Не <span class="cn-word" data-pos="verb" data-tr="xavotir olmang">волнуйся</span>, солнышко моё».</p>

<p>Ваня <span class="cn-word" data-pos="verb" data-tr="oʻtirdi">сел</span> на пол и прочитал все письма. В каждом было то же самое: <strong>мамочка</strong>, <strong>комнатка</strong>, <strong>солнышко</strong>.</p>

<p>Он <span class="cn-word" data-pos="verb" data-tr="tushundi">понял</span>: бабушка так говорила всегда. Не потому, что он <span class="cn-word" data-tr="kichkina">маленький</span>. А потому, что она так <span class="cn-word" data-pos="verb" data-tr="sevadi">любит</span>.</p>

<p>Вечером она <span class="cn-word" data-pos="verb" data-tr="soʻradi">спросила</span>:</p>

<p>— Ванечка, чайку?</p>

<p>— Давай, бабушка. И <strong>хлебушка</strong> тоже.</p>

<p>Бабушка <span class="cn-word" data-pos="verb" data-tr="unga qaradi">посмотрела на него</span> и <span class="cn-word" data-pos="verb" data-tr="jilmaydi">улыбнулась</span>. Она ничего не сказала. Но чай в тот вечер был в <span class="cn-word" data-tr="eng yaxshi">самом лучшем</span> стаканчике.</p>''',
        "questions": [
            {
                "text": "Vanya avvaliga buvisining gapiga nega norozi edi?",
                "choices": [
                    "Buvisi juda sekin gapirardi",
                    "Buvisi hamma narsani kichraytirib aytardi va u oʻzini bola his qilardi",
                    "Buvisi uning ismini notoʻgʻri aytardi",
                    "Buvisi eski soʻzlarni ishlatardi"
                ],
                "answer": 1,
                "explanation": "«Бабушка, мне четырнадцать лет. Я не Ванечка». "
                               "U kichraytirilgan shaklni «kichiklik» deb "
                               "tushunardi — bu aynan darsda ogohlantirilgan "
                               "xato.",
            },
            {
                "text": "Xatlar Vanyaga nimani koʻrsatdi?",
                "choices": [
                    "Buvisi yoshligida boshqa shaharda oʻqiganini",
                    "Buvisi yigirma yoshida ham xuddi shunday gapirganini — demak bu yosh haqida emas",
                    "Buvisi xat yozishni yaxshi koʻrishini",
                    "Buvisining onasi qattiqqoʻl boʻlganini"
                ],
                "answer": 1,
                "explanation": "«В каждом было то же самое: мамочка, комнатка, "
                               "солнышко». Buvi oʻz onasiga ham shunday "
                               "yozgan — demak bu shakl <strong>mehr</strong> "
                               "bildiradi, oʻlcham emas.",
            },
            {
                "text": "Hikoyaning oxirida «И хлебушка тоже» degan javob nimani anglatadi?",
                "choices": [
                    "Vanya juda och edi",
                    "Vanya buvisining tilini qabul qildi",
                    "Vanya buvisining ustidan kulyapti",
                    "Vanya nonni yaxshi koʻradi"
                ],
                "answer": 1,
                "explanation": "Vanya birinchi marta buvisining oʻz soʻzini "
                               "ishlatadi — «хлебушка», «хлеба» emas. Shuning "
                               "uchun buvi jilmayadi: javob bitta soʻzda "
                               "berilgan.",
            },
        ],
    },
]
