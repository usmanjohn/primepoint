# Oson rus hikoyalari — stories 6-10 (Claude-authored, beginner A1-A2 level, dialogue-heavy).
# Import: python manage.py import_corner corner/management/commands/_stories_russian_easy_6_10.py --author=<AUTHOR>

SUBJECT = {
    "name":    "Russian",
    "summary": "Rus tili: zamonaviy hikoyalar, lugʻat va grammatika bilan.",
    "icon":    "bi-translate",
    "color":   "#b91c1c",
}

COLLECTION = {
    "title":       "Oson rus hikoyalari",
    "description": "Boshlangʻich daraja (A1-A2) — sodda dialoglar va kundalik iboralar bilan qisqa oʻqish matnlari.",
    "order":       1,
}

STORIES = [
    {
        "title":   "В гостинице",
        "summary": "Aziz mehmonxonaga band qilingan xonasiga keladi, lekin kutilmagan xato tufayli yanada yaxshi xonaga koʻchiriladi.",
        "order":   6,
        "grammar": [
            {
                "pattern":  "Я хотел(а) бы ...",
                "meaning":  "... qilmoqchi edim / ...ni istardim — muloyim, rasmiy iltimos bildirish uchun ishlatiladi.",
                "examples": ["Я хотел бы забронировать номер.", "Я хотела бы задать вопрос."],
            },
            {
                "pattern":  "У вас есть свободный/свободная ...?",
                "meaning":  "Sizda boʻsh ... bormi? — biror narsaning mavjudligini soʻrash uchun.",
                "examples": ["У вас есть свободный номер?", "У вас есть свободное место?"],
            },
            {
                "pattern":  "К сожалению, ...",
                "meaning":  "Afsuski, ... — yoqimsiz xabar yoki uzr bilan gapni boshlashda ishlatiladi.",
                "examples": ["К сожалению, номер уже занят.", "К сожалению, я не смогу прийти."],
            },
        ],
        "body": '''<p>Азиз <span class="cn-word" data-pos="verb" data-tr="yetib keldi">приехал</span> в гостиницу поздно вечером, после долгой <span class="cn-word" data-tr="sayohat">поездки</span>. Он был очень <span class="cn-word" data-pos="adj" data-tr="charchagan">уставший</span>.</p>
<p>— Добрый вечер! <strong>Я хотел бы</strong> получить номер. Я <span class="cn-word" data-pos="verb" data-tr="band qilgan edim">забронировал</span> его на сайте, — сказал он <span class="cn-word" data-tr="qabulxona xodimi">администратору</span>.</p>
<p>— Ваше имя, пожалуйста?</p>
<p>— Азиз Каримов.</p>
<p>Администратор <span class="cn-word" data-pos="verb" data-tr="tekshirdi">проверил</span> компьютер и вдруг сделал <span class="cn-word" data-pos="adj" data-tr="ajablangan">удивлённое</span> лицо.</p>
<p>— <strong>К сожалению</strong>, произошла маленькая <span class="cn-word" data-tr="xato">ошибка</span>. У нас сегодня два гостя с именем Азиз Каримов, и ваш номер уже <span class="cn-word" data-pos="verb" data-tr="berildi">отдали</span> другому человеку!</p>
<p>Азиз очень <span class="cn-word" data-pos="verb" data-tr="hayron qoldi">удивился</span>. — Ого! И что теперь делать?</p>
<p>— Не <span class="cn-word" data-pos="verb" data-tr="tashvishlanmang">волнуйтесь</span>. <strong>У нас есть свободный</strong> номер, но он немного дороже — с видом на город.</p>
<p>— А сколько он стоит?</p>
<p>— Не беспокойтесь, для вас это будет <span class="cn-word" data-pos="adj" data-tr="bepul">бесплатно</span>, за наше <span class="cn-word" data-tr="noqulaylik">неудобство</span>.</p>
<p>Азиз улыбнулся. — Ну что ж, повезло мне сегодня!</p>
<p>Он поднялся на девятый <span class="cn-word" data-tr="qavat">этаж</span>, открыл дверь и увидел <span class="cn-word" data-pos="adj" data-tr="ajoyib">потрясающий</span> вид на ночной город. — Может, эта ошибка была не такой уж плохой, — подумал он с улыбкой.</p>''',
        "questions": [
            {
                "text": "Почему администратор извинился перед Азизом?",
                "choices": ["Потому что номер был грязный", "Потому что номер уже отдали другому гостю с таким же именем", "Потому что гостиница была закрыта"],
                "answer": 1,
                "explanation": "\"У нас сегодня два гостя с именем Азиз Каримов, и ваш номер уже отдали другому человеку\" deyiladi.",
            },
            {
                "text": "Сколько стоил новый номер для Азиза?",
                "choices": ["Дороже, чем обычный номер", "Бесплатно, за неудобство гостиницы", "Азиз вообще не заплатил и ушёл"],
                "answer": 1,
                "explanation": "Administrator \"это будет бесплатно, за наше неудобство\" deb aytadi.",
            },
            {
                "text": "Что увидел Азиз из окна нового номера?",
                "choices": ["Потрясающий вид на город", "Море", "Горы"],
                "answer": 0,
                "explanation": "\"Увидел потрясающий вид на ночной город\" deyilgan.",
            },
        ],
    },
    {
        "title":   "У врача",
        "summary": "Bahrom internetdan oʻqib jiddiy kasal boʻlib qolganiga ishonadi, lekin bu oddiy shamollash ekan.",
        "order":   7,
        "grammar": [
            {
                "pattern":  "У меня болит ...",
                "meaning":  "Mening ... ogʻriyapti — tana aʼzosi bilan bogʻliq shikoyat bildirish uchun asosiy konstruksiya.",
                "examples": ["У меня болит горло.", "У меня болит живот."],
            },
            {
                "pattern":  "Не нужно + infinitiv",
                "meaning":  "... qilish shart emas — birovni tinchlantirish yoki maslahat berishda ishlatiladi.",
                "examples": ["Не нужно паниковать.", "Не нужно так волноваться."],
            },
            {
                "pattern":  "Всё будет хорошо",
                "meaning":  "Hammasi yaxshi boʻladi — tasalli beruvchi optimistik ibora.",
                "examples": ["Не переживай, всё будет хорошо.", "Скоро всё будет хорошо."],
            },
        ],
        "body": '''<p>Бахром <span class="cn-word" data-pos="verb" data-tr="tumov boʻldi">простудился</span> и всю ночь не мог спать. Утром он <span class="cn-word" data-pos="verb" data-tr="qidirdi">искал</span> в интернете, что у него за <span class="cn-word" data-tr="alomat">симптомы</span>, и очень <span class="cn-word" data-pos="verb" data-tr="qoʻrqib ketdi">испугался</span>.</p>
<p>— Кажется, у меня что-то <span class="cn-word" data-pos="adj" data-tr="jiddiy">серьёзное</span>! — подумал он и быстро <span class="cn-word" data-pos="verb" data-tr="bordi">пошёл</span> к врачу.</p>
<p>— Здравствуйте, доктор! <strong>У меня болит</strong> голова, и ещё горло, и вообще всё тело! В интернете написано, что это может быть очень <span class="cn-word" data-pos="adj" data-tr="xavfli">опасно</span>!</p>
<p>Врач <span class="cn-word" data-pos="verb" data-tr="jilmayib qoʻydi">улыбнулся</span> и <span class="cn-word" data-pos="verb" data-tr="tekshirdi">осмотрел</span> его.</p>
<p>— Спокойно, молодой человек. <strong>Не нужно</strong> так волноваться. У вас обычная <span class="cn-word" data-tr="shamollash">простуда</span>, ничего страшного.</p>
<p>— Правда? А в интернете писали про <span class="cn-word" data-tr="dahshatli kasalliklar">страшные болезни</span>!</p>
<p>— Интернету верить не стоит, — <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span> врач. — Вам нужно <span class="cn-word" data-pos="verb" data-tr="dam olmoq">отдыхать</span>, пить много <span class="cn-word" data-tr="issiq choy">горячего чая</span> и, конечно, пить <span class="cn-word" data-tr="dorilar">лекарства</span>, которые я выпишу.</p>
<p>— Сколько дней мне нужно лежать дома?</p>
<p>— Три-четыре дня. <strong>Всё будет хорошо</strong>, обещаю.</p>
<p>Бахром вышел из кабинета и <span class="cn-word" data-pos="verb" data-tr="chuqur nafas oldi">вздохнул</span> с <span class="cn-word" data-tr="yengillik">облегчением</span>. — В следующий раз лучше сразу идти к врачу, а не читать интернет! — подумал он, смеясь над собой.</p>''',
        "questions": [
            {
                "text": "Почему Бахром сильно испугался перед визитом к врачу?",
                "choices": ["Потому что прочитал в интернете о страшных болезнях", "Потому что врач ему позвонил", "Потому что у него не было денег"],
                "answer": 0,
                "explanation": "U internetdan \"страшные болезни\" haqida oʻqib qoʻrqib ketgan edi.",
            },
            {
                "text": "Что на самом деле было у Бахрома?",
                "choices": ["Обычная простуда", "Серьёзная болезнь", "Ничего, он был здоров"],
                "answer": 0,
                "explanation": "Vrach \"У вас обычная простуда, ничего страшного\" deb aytadi.",
            },
            {
                "text": "Что понял Бахром в конце истории?",
                "choices": ["Что лучше сразу идти к врачу, а не читать интернет", "Что нужно больше спать", "Что доктора всегда ошибаются"],
                "answer": 0,
                "explanation": "U oxirida \"лучше сразу идти к врачу, а не читать интернет\" deb oʻyladi.",
            },
        ],
    },
    {
        "title":   "Погода и планы",
        "summary": "Doʻstlar piknikka borishni rejalashtiradi, lekin kutilmagan yomgʻir sabab reja oʻzgarib, kulgili uy oʻyinlari kechasiga aylanadi.",
        "order":   8,
        "grammar": [
            {
                "pattern":  "Какая сегодня/завтра погода?",
                "meaning":  "Bugun/ertaga ob-havo qanday? — ob-havo haqida soʻroq berish konstruksiyasi.",
                "examples": ["Какая сегодня погода?", "Какая погода будет завтра?"],
            },
            {
                "pattern":  "Если ..., то ...",
                "meaning":  "Agar ..., unda ... — shart ergash gapini bildiruvchi asosiy konstruksiya.",
                "examples": ["Если будет дождь, то мы останемся дома.", "Если ты устал, то отдохни."],
            },
            {
                "pattern":  "Лучше + infinitiv",
                "meaning":  "... qilgani afzal/yaxshiroq — tavsiya yoki taklif berishda ishlatiladi.",
                "examples": ["Лучше взять зонт.", "Лучше остаться дома."],
            },
        ],
        "body": '''<p>Нигора и её друзья <span class="cn-word" data-pos="verb" data-tr="rejalashtirishdi">планировали</span> поехать на <span class="cn-word" data-tr="piknik">пикник</span> за город в субботу.</p>
<p>— <strong>Какая</strong> завтра <strong>погода</strong>? — спросила Нигора у Санжара.</p>
<p>— Я <span class="cn-word" data-pos="verb" data-tr="tekshirdim">проверил</span> телефон — обещают <span class="cn-word" data-tr="quyoshli">солнце</span> весь день.</p>
<p>Но в субботу утром небо стало <span class="cn-word" data-pos="adj" data-tr="bulutli">пасмурным</span>, а потом начался <span class="cn-word" data-pos="adj" data-tr="kuchli">сильный</span> дождь.</p>
<p>— Вот это да! — <span class="cn-word" data-pos="verb" data-tr="xoʻrsindi">вздохнула</span> Нигора. — <strong>Если</strong> дождь не <span class="cn-word" data-pos="verb" data-tr="toʻxtaydi">закончится</span>, <strong>то</strong> пикника не будет.</p>
<p>Санжар немного <span class="cn-word" data-pos="verb" data-tr="oʻyladi">подумал</span> и сказал:</p>
<p>— <strong>Лучше</strong> не <span class="cn-word" data-pos="verb" data-tr="xafa boʻlmoq">расстраиваться</span>. Давайте останемся у меня дома и поиграем в <span class="cn-word" data-tr="stol oʻyinlari">настольные игры</span>!</p>
<p>Все друзья <span class="cn-word" data-pos="verb" data-tr="rozi boʻlishdi">согласились</span>. Они пришли к Санжару, приготовили горячий чай и <span class="cn-word" data-pos="adj" data-tr="mazali">вкусные</span> закуски.</p>
<p>Весь день они играли, смеялись и рассказывали <span class="cn-word" data-tr="hikoyalar">истории</span>. Дождь стучал в окно, но никому не было <span class="cn-word" data-pos="adj" data-tr="zerikarli">скучно</span>.</p>
<p>— Знаете, — сказала Нигора вечером, — этот день получился даже <span class="cn-word" data-pos="adj" data-tr="qiziqroq">интереснее</span>, чем обычный пикник!</p>''',
        "questions": [
            {
                "text": "Какая погода была обещана в телефоне?",
                "choices": ["Дождь", "Солнце", "Снег"],
                "answer": 1,
                "explanation": "Sanjar \"обещают солнце весь день\" deb aytgan edi.",
            },
            {
                "text": "Что предложил сделать Санжар вместо пикника?",
                "choices": ["Поехать в кино", "Остаться дома и поиграть в настольные игры", "Пойти в кафе"],
                "answer": 1,
                "explanation": "\"Давайте останемся у меня дома и поиграем в настольные игры\" deb taklif qiladi.",
            },
            {
                "text": "Как Нигора оценила этот день в конце?",
                "choices": ["Он был скучным", "Он получился интереснее, чем обычный пикник", "Она пожалела, что осталась дома"],
                "answer": 1,
                "explanation": "\"Этот день получился даже интереснее, чем обычный пикник\" deydi.",
            },
        ],
    },
    {
        "title":   "В автобусе",
        "summary": "Kamola avtobusda telefoniga berilib bekatini oʻtkazib yuborishiga oz qoladi, lekin yordam bergan notanish yigit uning sinfdoshi boʻlib chiqadi.",
        "order":   9,
        "grammar": [
            {
                "pattern":  "Во сколько отправляется/приходит ...?",
                "meaning":  "... soat nechada joʻnaydi/keladi? — jadval yoki vaqt haqida soʻrash konstruksiyasi.",
                "examples": ["Во сколько отправляется автобус?", "Во сколько приходит поезд?"],
            },
            {
                "pattern":  "Следующая остановка ...",
                "meaning":  "Keyingi bekat ... — jamoat transportida eʼlon qilinadigan standart ibora.",
                "examples": ["Следующая остановка — центр города.", "Следующая остановка через две минуты."],
            },
            {
                "pattern":  "Давно не виделись!",
                "meaning":  "Koʻpdan beri koʻrishmagandik! — uzoq vaqtdan keyin uchrashganda ishlatiladigan ibora.",
                "examples": ["Ой, давно не виделись!", "Мы давно не виделись, как дела?"],
            },
        ],
        "body": '''<p>Камола <span class="cn-word" data-pos="verb" data-tr="oʻtirdi">села</span> в автобус и сразу <span class="cn-word" data-pos="verb" data-tr="qaradi">посмотрела</span> в телефон. Ей нужно было <span class="cn-word" data-pos="verb" data-tr="tushmoq">выйти</span> на остановке «Театр».</p>
<p>— <strong>Во сколько</strong> автобус <strong>приходит</strong> в центр? — спросила она у <span class="cn-word" data-tr="haydovchi">водителя</span> в начале поездки.</p>
<p>— Минут через двадцать, — ответил он.</p>
<p>Камола так <span class="cn-word" data-pos="adj" data-tr="berilib ketgan">увлечена</span> была перепиской с подругой, что не <span class="cn-word" data-pos="verb" data-tr="eshitmadi">услышала</span> объявление: «<strong>Следующая остановка</strong> — Театр».</p>
<p>Вдруг кто-то мягко <span class="cn-word" data-pos="verb" data-tr="tegdi">тронул</span> её за плечо.</p>
<p>— Извините, кажется, это ваша остановка?</p>
<p>Камола <span class="cn-word" data-pos="verb" data-tr="koʻtarildi">подняла</span> глаза и <span class="cn-word" data-pos="verb" data-tr="tanidi">узнала</span> лицо.</p>
<p>— Бекзод?! Это ты?</p>
<p>— Камола! <strong>Давно не виделись!</strong> Мы же <span class="cn-word" data-pos="verb" data-tr="oʻqiganmiz">учились</span> вместе в школе!</p>
<p>Камола быстро <span class="cn-word" data-pos="verb" data-tr="tushdi">вышла</span> на своей остановке, а Бекзод вышел вместе с ней, чтобы <span class="cn-word" data-pos="verb" data-tr="davom ettirmoq">продолжить</span> разговор.</p>
<p>— Спасибо, что <span class="cn-word" data-pos="verb" data-tr="ogohlantirdi">предупредил</span> меня! Я бы точно <span class="cn-word" data-pos="verb" data-tr="oʻtkazib yuborardim">пропустила</span> свою остановку.</p>
<p>Они <span class="cn-word" data-pos="adj" data-tr="xursand">радостные</span> пошли пить кофе и вспоминать школьные годы. Иногда телефон заставляет забыть про мир вокруг — хорошо, что рядом оказался старый друг.</p>''',
        "questions": [
            {
                "text": "Почему Камола чуть не пропустила свою остановку?",
                "choices": ["Она уснула", "Она была занята перепиской в телефоне", "Автобус поехал не по маршруту"],
                "answer": 1,
                "explanation": "\"Так увлечена была перепиской с подругой, что не услышала объявление\" deyiladi.",
            },
            {
                "text": "Кто помог Камоле не пропустить остановку?",
                "choices": ["Водитель автобуса", "Её старый школьный друг Бекзод", "Незнакомая женщина"],
                "answer": 1,
                "explanation": "Bekzod uni yelkasidan tegib ogohlantiradi — u bilan birga oʻqigan sinfdoshi ekan.",
            },
            {
                "text": "Что Камола с Бекзодом решили сделать после автобуса?",
                "choices": ["Пойти пить кофе и вспоминать школу", "Сразу разойтись", "Поехать дальше вместе на автобусе"],
                "answer": 0,
                "explanation": "\"Пошли пить кофе и вспоминать школьные годы\" deyiladi.",
            },
        ],
    },
    {
        "title":   "День рождения",
        "summary": "Doʻstlar Odilaga sirli tugʻilgan kun ziyofati tayyorlaydi, lekin reja fosh boʻlib qolishiga oz qoladi — Odila baribir hazil bilan hayron boʻlgandek qiladi.",
        "order":   10,
        "grammar": [
            {
                "pattern":  "С днём рождения!",
                "meaning":  "Tugʻilgan kuningiz bilan! — tabriklashda ishlatiladigan asosiy ibora.",
                "examples": ["С днём рождения, дорогая!", "Поздравляю тебя с днём рождения!"],
            },
            {
                "pattern":  "Хочу подарить тебе ...",
                "meaning":  "Senga ... sovgʻa qilmoqchiman — sovgʻa berish niyatini bildirish.",
                "examples": ["Хочу подарить тебе книгу.", "Я хочу подарить тебе цветы."],
            },
            {
                "pattern":  "Как здорово, что ...!",
                "meaning":  "...gani qanday ajoyib! — xursandchilik yoki hayajonni ifodalash uchun ishlatiladi.",
                "examples": ["Как здорово, что вы пришли!", "Как здорово, что сегодня выходной!"],
            },
        ],
        "body": '''<p>У Одилы скоро был <span class="cn-word" data-tr="tugʻilgan kun">день рождения</span>, и её друзья решили <span class="cn-word" data-pos="verb" data-tr="tayyorlamoq">подготовить</span> для неё <span class="cn-word" data-pos="adj" data-tr="sirli">сюрприз</span>.</p>
<p>— Только никому не говори! — <span class="cn-word" data-pos="verb" data-tr="ogohlantirdi">предупредила</span> Дилноза остальных. — Это должно быть <span class="cn-word" data-tr="sir">секретом</span>.</p>
<p>Друзья <span class="cn-word" data-pos="verb" data-tr="bezashdi">украсили</span> квартиру Дилнозы шарами и приготовили торт. Но накануне вечером Фарух случайно <span class="cn-word" data-pos="verb" data-tr="yozib yubordi">написал</span> Одиле не в тот чат: «Не забудь купить шары для завтрашней вечеринки!»</p>
<p>Одила прочитала сообщение и всё <span class="cn-word" data-pos="verb" data-tr="tushundi">поняла</span>. Но она <span class="cn-word" data-pos="verb" data-tr="qaror qildi">решила</span> ничего не говорить и просто подождать.</p>
<p>На следующий день, когда Одила <span class="cn-word" data-pos="verb" data-tr="kirdi">вошла</span> в квартиру Дилнозы, все друзья закричали:</p>
<p>— <strong>С днём рождения!</strong> Сюрприз!</p>
<p>Одила <span class="cn-word" data-pos="verb" data-tr="oʻzini qildi">сделала</span> <span class="cn-word" data-pos="adj" data-tr="hayron boʻlgandek">удивлённое</span> лицо, хотя уже всё знала.</p>
<p>— Ничего себе! Вот это <span class="cn-word" data-tr="ajablanish">сюрприз</span>! Спасибо вам огромное!</p>
<p>Фарух подошёл с подарком. — <strong>Хочу подарить тебе</strong> вот это, — сказал он, немного <span class="cn-word" data-pos="adj" data-tr="tashvishlangan">волнуясь</span>, не зная, что Одила уже видела его сообщение.</p>
<p>— <strong>Как здорово, что</strong> у меня такие заботливые друзья! — <span class="cn-word" data-pos="verb" data-tr="dedi">сказала</span> она, обнимая всех по очереди.</p>
<p>Только через неделю Одила со смехом <span class="cn-word" data-pos="verb" data-tr="tan oldi">призналась</span> Дилнозе, что всё знала заранее — но не хотела <span class="cn-word" data-pos="verb" data-tr="buzmoq">портить</span> друзьям праздник.</p>''',
        "questions": [
            {
                "text": "Как Одила узнала о сюрпризе заранее?",
                "choices": ["Фарух случайно написал ей сообщение не в тот чат", "Дилноза сама рассказала ей", "Она увидела украшенную квартиру"],
                "answer": 0,
                "explanation": "Farux xato bilan Odilaga \"Не забудь купить шары для завтрашней вечеринки!\" deb yozib yuboradi.",
            },
            {
                "text": "Почему Одила сделала вид, что удивлена?",
                "choices": ["Она забыла про сообщение", "Она не хотела портить друзьям праздник", "Она не поняла сообщение"],
                "answer": 1,
                "explanation": "Oxirida \"не хотела портить друзьям праздник\" deb tushuntiriladi.",
            },
            {
                "text": "Когда Одила призналась, что всё знала заранее?",
                "choices": ["Сразу на вечеринке", "Через неделю", "Она никогда не призналась"],
                "answer": 1,
                "explanation": "\"Только через неделю Одила со смехом призналась\" deyiladi.",
            },
        ],
    },
]
