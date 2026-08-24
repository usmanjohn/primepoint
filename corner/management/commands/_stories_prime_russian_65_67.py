# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-65 … PR-67.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 65 — kundalik daftar, 66 — ilmiy-ommabop, 67 — intervyu.
(62 ilmiy-ommabop, 63 mahalla portreti, 64 voqea edi — demak uchta bir xil
shakl ketma-ket kelmayapti va intervyu bu blokda birinchi marta ishlatilyapti.)

Grammatika chegarasi (kumulyativ qoida):
  65-matn: если va когда. Kelasi zamon qoidasi ikki joyda koʻrsatilgan
           («Если ты найдёшь…, мы их зажжём», «Если завтра отключат…,
           я не буду сердиться») va когда + СВ ketma-ketligi.
  66-matn: потому что · так как · поэтому · из-за того что · благодаря,
           oxirida darsdagi «не потому, что… а потому, что…» qurilishi.
  67-matn: а · но · зато · хотя · однако · тем не менее — oltalasi bir
           intervyuda, har biri oʻz oʻrnida.

⚠️ ATAY QOCHILGAN (keyingi darslar): ли (PR-68), тот/кто (PR-69),
причастие va деепричастие (PR-70…72), qisqa sifat (PR-73), СИФАТ
ДАРАЖАЛАРИ — больше / шире / быстрее (PR-74), свой (PR-75),
кто-то / кто-нибудь (PR-78), никто … не (PR-79). Yagona istisno —
66-matndagi «самое глубокое», u Baykal haqidagi matnda muqarrar va
cn-word izohi bilan berilgan.

⚠️ FAKTLAR (66-matn tekshirilgan):
  · maksimal chuqurlik 1642 m; · yosh ~25 mln yil; · Baykal yorigʻi (rift)
    yiliga ~2 sm kengayadi; · 336 daryo quyiladi, faqat Angara oqib chiqadi;
  · dunyodagi suyuq holdagi chuchuk suvning ~1/5 qismi; · bahorda suv
    40 m gacha shaffof; · epishura raqchasi suvni filtrlaydi; · qishda muz
    1 m dan qalin, ustidan mashina yuradi; · nerpa — yagona chuchuk suv
    tyuleni. 65 va 67 — toʻqima voqealar, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_65_67.py --author=prime
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
    # PR-65 — если / когда                        KUNDALIK DAFTAR
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Когда отключили свет",
        "summary": (
            "PR-65 matni. Kundalik daftar sahifasi: seshanba kuni uyda chiroq "
            "oʻchdi va oila uch soat sham yorugʻida birga oʻtirdi. Matn "
            "«когда» bilan «если» ni yonma-yon koʻrsatadi."
        ),
        "order":   65,
        "grammar": [
            {
                "pattern":  "Когда + oʻtgan zamon (СВ) — ketma-ketlik",
                "meaning":  "Avval bir ish tugaydi, keyin ikkinchisi boshlanadi: "
                            "«Когда стало темно, я испугалась», «Когда свет "
                            "включили, все замолчали».",
                "examples": ["Когда стало темно, я испугалась.",
                             "Когда свет включили, все замолчали."],
            },
            {
                "pattern":  "Если + kelasi zamon",
                "meaning":  "Real shart. Voqea kelajakda boʻlgani uchun ikkala "
                            "qismda ham kelasi zamon turadi — oʻzbekcha «topsang» "
                            "zamonsiz, ruschada esa «найдёшь».",
                "examples": ["Если ты найдёшь спички, мы их зажжём.",
                             "Если завтра отключат свет, я не буду сердиться."],
            },
            {
                "pattern":  "Когда + hozirgi zamon — umumiy haqiqat",
                "meaning":  "Oxirgi jumlada «когда» bir marta boʻlgan voqeani "
                            "emas, har doim takrorlanadigan holatni bildiradi.",
                "examples": ["Когда в доме темно, люди начинают говорить."],
            },
        ],
        "body": '''<p><em>Вторник, восемь часов вечера.</em></p>

<p>Сегодня в нашем доме <span class="cn-word" data-pos="verb" data-tr="oʻchirishdi">отключили</span> свет. Это <span class="cn-word" data-pos="verb" data-tr="sodir boʻldi">случилось</span> ровно в семь. Я сидела за столом и делала уроки.</p>

<p><strong>Когда стало</strong> <span class="cn-word" data-tr="qorongʻi">темно</span>, я сначала <span class="cn-word" data-pos="verb" data-tr="qoʻrqib ketdim">испугалась</span>. Потом я <span class="cn-word" data-pos="verb" data-tr="esladim">вспомнила</span>, что на кухне лежат <span class="cn-word" data-tr="shamlar">свечи</span>.</p>

<p>Мама сказала: «<strong>Если ты найдёшь</strong> <span class="cn-word" data-tr="gugurt">спички</span>, мы их <span class="cn-word" data-pos="verb" data-tr="yoqamiz">зажжём</span>». Я нашла спички в <span class="cn-word" data-tr="quti, tortma">ящике</span>.</p>

<p>Мы зажгли три свечи и сели вместе на кухне. Телефоны остались в комнате.</p>

<p>Бабушка начала рассказывать о <span class="cn-word" data-tr="bolalik">детстве</span>. Она говорила, что раньше свет отключали каждую неделю. Тогда люди выходили во двор и <span class="cn-word" data-pos="verb" data-tr="suhbatlashardilar">разговаривали</span>.</p>

<p>Мы слушали бабушку два часа. Обычно вечером мы сидим в <span class="cn-word" data-tr="turli">разных</span> комнатах.</p>

<p><strong>Когда свет включили</strong>, все <span class="cn-word" data-pos="verb" data-tr="jim boʻlishdi">замолчали</span>. Бабушка <span class="cn-word" data-pos="verb" data-tr="kulib yubordi">засмеялась</span> и сказала: «Ну вот, <span class="cn-word" data-tr="ertak">сказка</span> <span class="cn-word" data-pos="verb" data-tr="tugadi">кончилась</span>».</p>

<p>Теперь я думаю так. <strong>Если завтра снова отключат</strong> свет, я не буду <span class="cn-word" data-pos="verb" data-tr="jahlim chiqmoq">сердиться</span>. <strong>Когда</strong> в доме темно, люди начинают говорить <span class="cn-word" data-tr="bir-biri bilan">друг с другом</span>.</p>''',
        "questions": [
            {
                "text": "Chiroq oʻchgach, oila nima qildi?",
                "choices": [
                    "Hamma oʻz xonasiga tarqaldi",
                    "Uch shamni yoqib, oshxonada birga oʻtirishdi",
                    "Telefon chirogʻida darsni davom ettirishdi",
                    "Qoʻshnilarnikiga chiqib ketishdi"
                ],
                "answer": 1,
                "explanation": "«Мы зажгли три свечи и сели вместе на кухне. "
                               "Телефоны остались в комнате». Aynan shundan keyin "
                               "buvining hikoyasi boshlanadi.",
            },
            {
                "text": "Nega matnda «Если ты найдёшь спички» deyilgan, «если ты находишь» emas?",
                "choices": [
                    "Chunki bu buyruq gap",
                    "Chunki «если» har doim kelasi zamon talab qiladi degan qoida bor",
                    "Chunki voqea kelajakda — shuning uchun ikkala qismda ham kelasi zamon",
                    "Chunki «найти» feʼlining hozirgi zamoni yoʻq"
                ],
                "answer": 2,
                "explanation": "Gugurtni topish ham, shamni yoqish ham hali "
                               "boʻlmagan — ikkalasi ham kelajakda. Rus tilida "
                               "bunday holatda ergash gapda ham kelasi zamon "
                               "turadi: найдёшь … зажжём. Oʻzbekcha «topsang» "
                               "zamonni koʻrsatmaydi, shuning uchun bu joy "
                               "oʻzbek oʻquvchisi uchun tuzoq.",
            },
            {
                "text": "Kundalikning oxirgi xulosasi nima?",
                "choices": [
                    "Chiroq oʻchsa, dars qilib boʻlmaydi",
                    "Sham chiroqdan koʻra xavfsizroq",
                    "Buvining hikoyalari juda uzun edi",
                    "Uy qorongʻi boʻlganda odamlar bir-biri bilan gaplasha boshlaydi"
                ],
                "answer": 3,
                "explanation": "«Когда в доме темно, люди начинают говорить "
                               "друг с другом». Bu yerdagi «когда» bir kechani "
                               "emas, umumiy qoidani bildiradi — shuning uchun "
                               "feʼl hozirgi zamonda.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-66 — sabab va natija                       ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Почему Байкал такой глубокий",
        "summary": (
            "PR-66 matni. Baykal nega dunyodagi eng chuqur koʻl ekanini "
            "tushuntiradi: u suv toʻlgan chuqurlik emas, yer poʻstlogʻidagi "
            "yoriq. Barcha faktlar haqiqiy. Oxirida darsning «не потому, "
            "что… а потому, что…» qurilishi."
        ),
        "order":   66,
        "grammar": [
            {
                "pattern":  "Потому что / так как — sabab",
                "meaning":  "Ikkalasi ham sababni aytadi. Farqi oʻrnida: «так как» "
                            "gapni boshlaydi, «потому что» esa asosiy gapdan keyin "
                            "turadi.",
                "examples": ["Байкал глубокий, потому что он лежит в трещине.",
                             "Так как кора расходится, берега Байкала отдаляются."],
            },
            {
                "pattern":  "Поэтому — natija",
                "meaning":  "Sababdan keyin xulosa chiqaradi: «shuning uchun». "
                            "Matnda uch marta uchraydi.",
                "examples": ["Лёд толстый, поэтому по озеру ездят машины."],
            },
            {
                "pattern":  "Из-за того что + gap · благодаря + Д.п.",
                "meaning":  "«Из-за» — yomon natija, «благодаря» — yaxshi natija. "
                            "«Из-за того что» butun gap bilan, «благодаря» esa "
                            "Дательный kelishigidagi ot bilan keladi.",
                "examples": ["Из-за того что реки приносят песок, дно поднимается.",
                             "Благодаря этому рачку вода остаётся чистой."],
            },
        ],
        "body": '''<p>Байкал — <span class="cn-word" data-tr="eng chuqur">самое глубокое</span> озеро на Земле. Его <span class="cn-word" data-tr="chuqurlik">глубина</span> — 1642 метра. Почему так?</p>

<p>Многие думают, что Байкал — это просто большая <span class="cn-word" data-tr="chuqurlik, oʻra">яма</span> с водой. Но это не так.</p>

<p>Байкал глубокий, <strong>потому что</strong> он лежит в <span class="cn-word" data-tr="yoriq">трещине</span> земной <span class="cn-word" data-tr="poʻstloq">коры</span>. Здесь кора <span class="cn-word" data-pos="verb" data-tr="ikki tomonga ajraladi">расходится</span> в разные стороны. Это происходит уже двадцать пять миллионов лет.</p>

<p><strong>Так как</strong> кора расходится каждый год примерно на два сантиметра, <span class="cn-word" data-tr="qirgʻoqlar">берега</span> Байкала медленно отдаляются друг от друга. <strong>Поэтому</strong> учёные говорят, что через миллионы лет здесь будет океан.</p>

<p>В Байкал <span class="cn-word" data-pos="verb" data-tr="quyiladi">впадают</span> 336 рек, а <span class="cn-word" data-pos="verb" data-tr="oqib chiqadi">вытекает</span> только одна — Ангара. <strong>Из-за того что</strong> реки приносят много <span class="cn-word" data-tr="qum">песка</span>, дно озера медленно поднимается. Но трещина продолжает <span class="cn-word" data-pos="verb" data-tr="chuqurlashmoq">углубляться</span>, <strong>поэтому</strong> Байкал остаётся глубоким.</p>

<p>Воды в Байкале очень много — примерно <span class="cn-word" data-tr="beshdan bir qismi">пятая часть</span> всей жидкой <span class="cn-word" data-tr="chuchuk">пресной</span> воды на Земле.</p>

<p>Вода здесь <span class="cn-word" data-tr="toza">чистая</span>. Весной в ней видно на сорок метров <span class="cn-word" data-tr="chuqurlikka">вглубь</span>. <strong>Так как</strong> в озере живёт крошечный <span class="cn-word" data-tr="qisqichbaqacha">рачок</span> — эпишура, вода постоянно <span class="cn-word" data-pos="verb" data-tr="tozalanadi">очищается</span>. Этот рачок <span class="cn-word" data-pos="verb" data-tr="filtrlaydi">фильтрует</span> воду, и <strong>благодаря</strong> ему Байкал остаётся прозрачным.</p>

<p>Зимой озеро <span class="cn-word" data-pos="verb" data-tr="muzlaydi">замерзает</span>. Лёд становится очень <span class="cn-word" data-tr="qalin">толстым</span> — от одного до двух метров. <strong>Поэтому</strong> зимой по Байкалу ездят машины.</p>

<p>Ещё в Байкале живёт <span class="cn-word" data-tr="Baykal tyuleni">нерпа</span> — единственный в мире пресноводный <span class="cn-word" data-tr="tyulen">тюлень</span>.</p>

<p>Итак, Байкал глубокий <strong>не потому, что</strong> он старый. Он глубокий <strong>потому, что</strong> земля под ним до сих пор движется.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra, Baykal nega bunchalik chuqur?",
                "choices": [
                    "U yer poʻstlogʻidagi yoriqda yotadi va yoriq hamon kengaymoqda",
                    "Unga 336 ta daryo quyiladi",
                    "U juda qadimiy koʻl, shuning uchun choʻkib ketgan",
                    "Qishda muz uning tubini bosib turadi"
                ],
                "answer": 0,
                "explanation": "«Байкал глубокий, потому что он лежит в "
                               "трещине земной коры». Matnning oxirgi jumlasi "
                               "buni yana bir bor taʼkidlaydi: yosh emas, harakat "
                               "sabab.",
            },
            {
                "text": "Nega matnda «благодаря ему» deyilgan, «из-за него» emas?",
                "choices": [
                    "Chunki «из-за» faqat odamlar haqida ishlatiladi",
                    "Chunki rachok kichkina",
                    "Chunki natija yaxshi — suv toza qoladi",
                    "Chunki «эпишура» ayol jinsida"
                ],
                "answer": 2,
                "explanation": "«Благодаря» ijobiy natijaga ishlatiladi va "
                               "Дательный kelishigini oladi (ему). Rachok suvni "
                               "tozalaydi — bu yaxshi natija, shuning uchun «из-за» "
                               "toʻgʻri kelmaydi.",
            },
            {
                "text": "Daryolar olib keladigan qum bilan yoriq oʻrtasida qanday kurash bor?",
                "choices": [
                    "Qum yoriqni butunlay toʻldirib boʻlgan",
                    "Qum tubni koʻtaradi, yoriq esa chuqurlashishda davom etadi",
                    "Yoriq qumni Angaraga surib chiqaradi",
                    "Qum faqat qishda toʻplanadi"
                ],
                "answer": 1,
                "explanation": "«Из-за того что реки приносят много песка, дно "
                               "озера медленно поднимается. Но трещина "
                               "продолжает углубляться, поэтому Байкал "
                               "остаётся глубоким». Bir sabab tubni koʻtaradi, "
                               "ikkinchisi tushiradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-67 — qarama-qarshilik                            INTERVYU
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Маленький город, большая библиотека",
        "summary": (
            "PR-67 matni. Sakkiz ming aholili kichik shaharda qirq ming kitobli "
            "kutubxona bor. Kutubxonachi Nina Petrovna bilan suhbat — har bir "
            "javobda kamchilik va uning oʻrnini bosadigan narsa yonma-yon turadi."
        ),
        "order":   67,
        "grammar": [
            {
                "pattern":  "Зато — kamchilikning oʻrnini bosadigan yaxshilik",
                "meaning":  "Avval minus, keyin plus. Oʻzbekchada bitta soʻzli "
                            "tarjimasi yoʻq: «buning evaziga», «buning oʻrniga».",
                "examples": ["Город маленький, зато у нас сорок тысяч книг.",
                             "Зимой здесь прохладно, зато тихо и светло."],
            },
            {
                "pattern":  "А — solishtirish · но — kutilganga zid",
                "meaning":  "«А» oʻzbekcha «esa» ning oʻrnida turadi va ikki "
                            "toʻgʻri gapni yonma-yon qoʻyadi. «Но» esa kutilgan "
                            "narsani buzadi.",
                "examples": ["Школьники приходят после уроков, а пенсионеры — утром.",
                             "Денег было мало, но люди приносили книги сами."],
            },
            {
                "pattern":  "Хотя · однако · тем не менее",
                "meaning":  "«Хотя» ergash gap boshlaydi (oʻzbekcha «…sa ham»). "
                            "«Однако» va «тем не менее» — shu maʼnoning kitobiy "
                            "va rasmiy variantlari.",
                "examples": ["Хотя здание старое, крыша не протекает.",
                             "Тем не менее я работаю здесь тридцать лет."],
            },
        ],
        "body": '''<p><em>Нина Петровна работает в библиотеке тридцать лет. Её город очень маленький, <strong>зато</strong> библиотека в нём большая. Мы поговорили с ней.</em></p>

<p>— Нина Петровна, сколько людей живёт в вашем городе?</p>

<p>— Восемь тысяч. Город маленький, <strong>зато</strong> у нас сорок тысяч книг.</p>

<p>— Сорок тысяч? Откуда?</p>

<p>— Мы <span class="cn-word" data-pos="verb" data-tr="toʻpladik">собирали</span> их сорок лет. Денег всегда было мало, <strong>но</strong> люди <span class="cn-word" data-pos="verb" data-tr="olib kelishardi">приносили</span> книги сами. Один <span class="cn-word" data-tr="muhandis">инженер</span> <span class="cn-word" data-pos="verb" data-tr="berib yubordi">отдал</span> нам всю домашнюю библиотеку.</p>

<p>— У вас новое <span class="cn-word" data-tr="bino">здание</span>?</p>

<p>— Нет. <strong>Хотя</strong> здание старое, <span class="cn-word" data-tr="tom, tomi">крыша</span> не <span class="cn-word" data-pos="verb" data-tr="oqmaydi">протекает</span>. Зимой здесь <span class="cn-word" data-tr="salqin">прохладно</span>, <strong>зато</strong> тихо и <span class="cn-word" data-tr="yorugʻ">светло</span>.</p>

<p>— Кто к вам ходит?</p>

<p>— Разные люди. Школьники приходят после уроков, <strong>а</strong> <span class="cn-word" data-tr="nafaqaxoʻrlar">пенсионеры</span> — утром. По вечерам приходят <span class="cn-word" data-tr="kattalar">взрослые</span>.</p>

<p>— Сейчас все читают в телефоне. Вам не <span class="cn-word" data-tr="qoʻrqinchli">страшно</span>?</p>

<p>— Мне говорили, что через десять лет библиотеки <span class="cn-word" data-pos="verb" data-tr="yopiladi">закроются</span>. <strong>Однако</strong> люди приходят к нам каждый день.</p>

<p>— Почему?</p>

<p>— Книгу можно <span class="cn-word" data-pos="verb" data-tr="buyurtma qilmoq">заказать</span> в интернете. <strong>Но</strong> в интернете нельзя сесть <span class="cn-word" data-tr="yonida">рядом</span> с человеком и поговорить с ним о книге. Люди приходят сюда не только за книгами.</p>

<p>— А что вам <span class="cn-word" data-tr="qiyin">трудно</span>?</p>

<p>— <span class="cn-word" data-tr="maosh">Зарплата</span> маленькая. Работы много. <strong>Тем не менее</strong> я работаю здесь тридцать лет и не хочу уходить.</p>

<p>— Почему?</p>

<p>— Потому что каждый день здесь человек находит книгу, которую долго <span class="cn-word" data-pos="verb" data-tr="qidirgan edi">искал</span>.</p>''',
        "questions": [
            {
                "text": "Kutubxonaga qirq ming kitob qayerdan kelgan?",
                "choices": [
                    "Davlat yangi bino bilan birga sovgʻa qilgan",
                    "Odamlar oʻzlari olib kelgan — qirq yil davomida toʻplangan",
                    "Boshqa shahardan koʻchirib keltirilgan",
                    "Nina Petrovna ularni internetdan buyurtma qilgan"
                ],
                "answer": 1,
                "explanation": "«Мы собирали их сорок лет. Денег всегда было "
                               "мало, но люди приносили книги сами». Bitta "
                               "muhandis butun uy kutubxonasini bergan.",
            },
            {
                "text": "Nega matnda «Школьники приходят после уроков, а пенсионеры — утром» deyilgan, «но» emas?",
                "choices": [
                    "Chunki bu ikki fikr solishtirilyapti — oʻzbekcha «esa»",
                    "Chunki «но» faqat inkor gaplarda ishlatiladi",
                    "Chunki «пенсионеры» koʻplikda",
                    "Chunki gapda kesim tushirilgan"
                ],
                "answer": 0,
                "explanation": "Ikkala gap ham toʻgʻri va ular shunchaki yonma-yon "
                               "qoʻyilgan — hech qanday zidlik yoʻq. Oʻzbekcha "
                               "«nafaqaxoʻrlar esa ertalab» degan joyda ruschada "
                               "har doim «а» turadi.",
            },
            {
                "text": "Nina Petrovna kutubxonaning kelajagi haqida nima deydi?",
                "choices": [
                    "Oʻn yildan keyin kutubxona yopiladi deb hisoblaydi",
                    "Yangi bino qurilishini kutmoqda",
                    "Kitoblarni internetga koʻchirmoqchi",
                    "Unga kutubxonalar yopiladi deyishgan, lekin odamlar har kuni kelmoqda"
                ],
                "answer": 3,
                "explanation": "«Мне говорили, что через десять лет библиотеки "
                               "закроются. Однако люди приходят к нам каждый "
                               "день». «Однако» — bu «но» ning kitobiy varianti va "
                               "aynan kutilganga zid narsani kiritadi.",
            },
        ],
    },
]
