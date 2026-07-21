# Oson rus hikoyalari — stories 1-5 (Claude-authored, beginner A1-A2 level, dialogue-heavy).
# Import: python manage.py import_corner corner/management/commands/_stories_russian_easy_1_5.py --author=<AUTHOR>

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
        "title":   "Знакомство",
        "summary": "Parkda tasodifan tanishib qolgan ikki yosh — ismlar, yosh va kasb haqida sodda suhbat.",
        "order":   1,
        "grammar": [
            {
                "pattern":  "Меня зовут ...",
                "meaning":  "Mening ismim ... (soʻzma-soʻz: meni ... deb chaqirishadi) — oʻzini tanishtirishning eng asosiy iborasi.",
                "examples": ["Меня зовут Дина.", "Как тебя зовут?"],
            },
            {
                "pattern":  "Мне ... лет / года / год",
                "meaning":  "Yoshni bildirish: menga ... yosh (dativ + son + лет/года/год — son oxiriga qarab oʻzgaradi).",
                "examples": ["Мне двадцать лет.", "Ей десять лет."],
            },
            {
                "pattern":  "Откуда ...?",
                "meaning":  "Qayerdan? — kelib chiqish joyini soʻrash uchun soʻroq soʻz.",
                "examples": ["Откуда ты?", "Откуда вы приехали?"],
            },
        ],
        "body": '''<p>Дина <span class="cn-word" data-pos="verb" data-tr="sayr qilardi">гуляла</span> в парке в субботу. Там она <span class="cn-word" data-pos="verb" data-tr="tanishib qoldi">познакомилась</span> с молодым человеком.</p>
<p>— Привет! <strong>Меня зовут</strong> Данияр, — сказал он с <span class="cn-word" data-tr="tabassum bilan">улыбкой</span>.</p>
<p>— Привет, Данияр! Я Дина. Очень <span class="cn-word" data-pos="adj" data-tr="yoqimli">приятно</span>.</p>
<p>— <strong>Откуда</strong> ты, Дина?</p>
<p>— Я из Ташкента. А ты откуда?</p>
<p>— Я из Москвы, но сейчас <span class="cn-word" data-pos="verb" data-tr="yashayman">живу</span> здесь, в этом <span class="cn-word" data-tr="shahar">городе</span>.</p>
<p>— <span class="cn-word" data-pos="adv" data-tr="qancha">Сколько</span> тебе лет?</p>
<p>— <strong>Мне</strong> двадцать два <strong>года</strong>. А тебе?</p>
<p>— Мне двадцать лет.</p>
<p>— <span class="cn-word" data-tr="nima (kasb-koʻnikma haqida)">Чем</span> ты занимаешься?</p>
<p>— Я <span class="cn-word" data-pos="verb" data-tr="ishlayman">работаю</span> в кафе <span class="cn-word" data-pos="adv" data-tr="yaqin atrofda">неподалёку</span>. А ты?</p>
<p>— Я <span class="cn-word" data-pos="verb" data-tr="oʻrganaman">изучаю</span> <span class="cn-word" data-tr="iqtisodiyot">экономику</span> в <span class="cn-word" data-tr="universitet">университете</span>.</p>
<p>Они <span class="cn-word" data-pos="verb" data-tr="suhbatlashishdi">поговорили</span> ещё немного и решили <span class="cn-word" data-pos="verb" data-tr="uchrashmoq">встретиться</span> <span class="cn-word" data-pos="adv" data-tr="yana">снова</span> на следующей неделе. Так у Дины <span class="cn-word" data-pos="verb" data-tr="paydo boʻldi">появился</span> новый <span class="cn-word" data-tr="doʻst">друг</span>.</p>''',
        "questions": [
            {
                "text": "Как зовут молодого человека, которого встретила Дина?",
                "choices": ["Данияр", "Тимур", "Бахтиёр"],
                "answer": 0,
                "explanation": "Matnda u \"Меня зовут Данияр\" deb oʻzini tanishtiradi.",
            },
            {
                "text": "Откуда Данияр?",
                "choices": ["Из Ташкента", "Из Москвы", "Из Самарканда"],
                "answer": 1,
                "explanation": "Данияр \"Я из Москвы\" deb aytadi, garchi hozir boshqa shaharda yashasa ham.",
            },
            {
                "text": "Чем занимается Дина?",
                "choices": ["Она работает в кафе", "Она изучает экономику в университете", "Она врач"],
                "answer": 0,
                "explanation": "Dina \"Я работаю в кафе неподалёку\" deb javob beradi — economикani Данияр oʻrganadi, Dina emas.",
            },
        ],
    },
    {
        "title":   "В кафе",
        "summary": "Kafeda kofe va olma pirogi buyurtma qilib, karta bilan toʻlaydigan yigit haqida.",
        "order":   2,
        "grammar": [
            {
                "pattern":  "Что вы хотите + infinitiv?",
                "meaning":  "Nima qilishni xohlaysiz? — muloyim soʻroq, rasmiy muomalada («вы» bilan) ishlatiladi.",
                "examples": ["Что вы хотите заказать?", "Что вы хотите купить?"],
            },
            {
                "pattern":  "У нас есть ...",
                "meaning":  "Bizda ... bor (mavjudlikni bildiruvchi asosiy konstruksiya).",
                "examples": ["У нас есть шоколадный торт.", "У нас есть свободные места."],
            },
            {
                "pattern":  "Можно + infinitiv?",
                "meaning":  "...sa boʻladimi? — ruxsat soʻrash uchun ishlatiladi.",
                "examples": ["Можно оплатить картой?", "Можно войти?"],
            },
        ],
        "body": '''<p>Тимур <span class="cn-word" data-pos="verb" data-tr="kirdi">зашёл</span> в маленькое кафе после работы. Он хотел <span class="cn-word" data-pos="verb" data-tr="ichmoq">выпить</span> кофе и <span class="cn-word" data-pos="verb" data-tr="yemoq">съесть</span> что-нибудь вкусное.</p>
<p>— Здравствуйте! <strong>Что вы хотите</strong> заказать? — спросила <span class="cn-word" data-tr="ofitsiant ayol">официантка</span>.</p>
<p>— Здравствуйте! Один кофе с молоком, пожалуйста. А что у вас есть из <span class="cn-word" data-tr="shirinliklar">десертов</span>?</p>
<p>— <strong>У нас есть</strong> <span class="cn-word" data-pos="adj" data-tr="shokoladli">шоколадный</span> торт и <span class="cn-word" data-pos="adj" data-tr="olma...">яблочный</span> <span class="cn-word" data-tr="pirog">пирог</span>.</p>
<p>— Тогда, пожалуйста, <span class="cn-word" data-tr="boʻlak">кусочек</span> яблочного пирога.</p>
<p>— Хорошо. Это будет пятнадцать тысяч сум.</p>
<p>— Вот, пожалуйста. <strong>Можно</strong> <span class="cn-word" data-pos="verb" data-tr="toʻlamoq">оплатить</span> <span class="cn-word" data-tr="karta bilan">картой</span>?</p>
<p>— Да, конечно.</p>
<p>Через пять минут официантка <span class="cn-word" data-pos="verb" data-tr="olib keldi">принесла</span> кофе и пирог. Тимур сел у окна и <span class="cn-word" data-tr="zavq bilan">с удовольствием</span> начал есть. Пирог был <span class="cn-word" data-pos="adj" data-tr="issiqqina">тёплый</span> и очень <span class="cn-word" data-pos="adj" data-tr="mazali">вкусный</span>.</p>
<p>— Спасибо большое! Всё было очень вкусно, — сказал он, <span class="cn-word" data-pos="verb" data-tr="ketayotib">уходя</span>.</p>
<p>— Приходите ещё! — <span class="cn-word" data-pos="verb" data-tr="jilmayib qoʻydi">улыбнулась</span> официантка.</p>''',
        "questions": [
            {
                "text": "Что заказал Тимур?",
                "choices": ["Только кофе", "Кофе с молоком и кусочек яблочного пирога", "Шоколадный торт"],
                "answer": 1,
                "explanation": "Timur \"Один кофе с молоком\" va keyin \"кусочек яблочного пирога\" buyurtma qiladi.",
            },
            {
                "text": "Сколько стоил заказ Тимура?",
                "choices": ["Пять тысяч сум", "Пятнадцать тысяч сум", "Двадцать тысяч сум"],
                "answer": 1,
                "explanation": "Ofitsiant ayol \"Это будет пятнадцать тысяч сум\" deb aytadi.",
            },
            {
                "text": "Как Тимур оплатил заказ?",
                "choices": ["Наличными", "Картой", "Он не заплатил"],
                "answer": 1,
                "explanation": "U \"Можно оплатить картой?\" deb soʻraydi va \"Да, конечно\" javobini oladi.",
            },
        ],
    },
    {
        "title":   "Моя семья",
        "summary": "Yigit oʻz oilasi — ota-onasi, singlisi, buvisi va bobosi haqida hikoya qiladi.",
        "order":   3,
        "grammar": [
            {
                "pattern":  "У меня есть / У меня нет ...",
                "meaning":  "Menda ... bor / Menda ... yoʻq — egalikni bildiruvchi asosiy konstruksiya («нет» dan keyingi ot roditelniy kelishikda keladi).",
                "examples": ["У меня есть сестра.", "У меня нет братьев."],
            },
            {
                "pattern":  "Мою/Моего ... зовут ...",
                "meaning":  "Mening ...imni ... deb atashadi — oila aʼzosining ismini aytish uchun («мою» — ayol, «моего» — erkak).",
                "examples": ["Мою маму зовут Гульнора.", "Моего брата зовут Botir."],
            },
            {
                "pattern":  "Как часто ...?",
                "meaning":  "Qanchalik tez-tez? — takrorlanish/chastota haqidagi soʻroq.",
                "examples": ["Как часто вы видитесь?", "Как часто ты занимаешься спортом?"],
            },
        ],
        "body": '''<p>Меня зовут Амир, и я хочу <span class="cn-word" data-pos="verb" data-tr="aytib bermoq">рассказать</span> о своей семье.</p>
<p><strong>У меня есть</strong> мама, папа и <span class="cn-word" data-pos="adj" data-tr="kenja">младшая</span> сестра. <strong>Мою</strong> маму <strong>зовут</strong> Гульнора, она работает <span class="cn-word" data-tr="shifokor boʻlib">врачом</span>. <strong>Моего</strong> папу <strong>зовут</strong> Бахтиёр, он <span class="cn-word" data-tr="muhandis">инженер</span>.</p>
<p>Моя сестра, Мадина, ещё <span class="cn-word" data-pos="verb" data-tr="oʻqiydi">учится</span> в школе. Ей десять лет. Она очень любит <span class="cn-word" data-pos="verb" data-tr="rasm chizmoq">рисовать</span> и <span class="cn-word" data-pos="verb" data-tr="qoʻshiq aytmoq">петь</span>.</p>
<p>— Амир, а у тебя есть братья? — спросила меня подруга Лола.</p>
<p>— Нет, <span class="cn-word" data-tr="akalar-ukalar">братьев</span> <strong>у меня нет</strong>, только одна сестра, — ответил я.</p>
<p>— А кто твои <span class="cn-word" data-tr="buvi">бабушка</span> и <span class="cn-word" data-tr="bobo">дедушка</span>?</p>
<p>— Моя бабушка живёт с нами. Она <span class="cn-word" data-pos="verb" data-tr="pishiradi">готовит</span> очень вкусный плов. А мой дедушка, <span class="cn-word" data-tr="afsuski">к сожалению</span>, живёт в другом городе.</p>
<p>— <strong>Как часто</strong> вы видитесь?</p>
<p>— Мы <span class="cn-word" data-pos="verb" data-tr="koʻrishamiz">видимся</span> <span class="cn-word" data-pos="adv" data-tr="kamdan-kam">редко</span>, но каждое лето ездим к нему в гости.</p>
<p>Я очень люблю свою семью. Для меня семья — это самое <span class="cn-word" data-pos="adj" data-tr="muhim">важное</span> в жизни.</p>''',
        "questions": [
            {
                "text": "Сколько лет сестре Амира, Мадине?",
                "choices": ["Восемь лет", "Десять лет", "Двенадцать лет"],
                "answer": 1,
                "explanation": "Matnda \"Ей десять лет\" deb aniq aytilgan.",
            },
            {
                "text": "Кто живёт вместе с семьёй Амира?",
                "choices": ["Бабушка", "Дедушка", "Никто из них"],
                "answer": 0,
                "explanation": "\"Моя бабушка живёт с нами\", dedushka esa boshqa shaharda yashaydi.",
            },
            {
                "text": "Как часто Амир видится с дедушкой?",
                "choices": ["Каждый день", "Каждое лето", "Никогда"],
                "answer": 1,
                "explanation": "\"Мы видимся редко, но каждое лето ездим к нему в гости\" deyilgan.",
            },
        ],
    },
    {
        "title":   "Спрашиваем дорогу",
        "summary": "Notanish shaharga birinchi marta kelgan yigit muzeyga boruvchi yoʻlni soʻrab topadi.",
        "order":   4,
        "grammar": [
            {
                "pattern":  "Извините, вы не подскажете, где ...?",
                "meaning":  "Kechirasiz, ayta olasizmi, ... qayerda? — yoʻl yoki maʼlumot soʻrashning eng muloyim shakli.",
                "examples": ["Извините, вы не подскажете, где находится вокзал?", "Вы не подскажете, где ближайшая аптека?"],
            },
            {
                "pattern":  "Идите прямо / поверните налево-направо",
                "meaning":  "Toʻgʻriga yuring / chapga-oʻngga buriling — yoʻnalish koʻrsatishda ishlatiladigan buyruq fe'llari.",
                "examples": ["Идите прямо, потом поверните направо.", "Поверните налево на светофоре."],
            },
            {
                "pattern":  "Минут + son",
                "meaning":  "Taxminan ... daqiqa — aniq songa yaqin miqdorni bildirish uchun soʻz tartibi almashtiriladi (son otdan keyin keladi).",
                "examples": ["Минут десять пешком.", "Подожди минут пять."],
            },
        ],
        "body": '''<p>Жасур <span class="cn-word" data-pos="adv" data-tr="birinchi marta">впервые</span> <span class="cn-word" data-pos="verb" data-tr="kelib qoldi">приехал</span> в этот город и не мог <span class="cn-word" data-pos="verb" data-tr="topmoq">найти</span> музей. Он решил спросить у <span class="cn-word" data-tr="oʻtkinchi">прохожего</span>.</p>
<p>— <strong>Извините, вы не подскажете, где находится</strong> городской музей?</p>
<p>— Да, конечно! <strong>Идите прямо</strong>, потом <strong>поверните налево</strong> на следующем <span class="cn-word" data-tr="chorraha">перекрёстке</span>.</p>
<p>— Прямо, а потом налево. Понятно. А это <span class="cn-word" data-pos="adj" data-tr="uzoq">далеко</span> отсюда?</p>
<p>— Нет, <span class="cn-word" data-pos="adv" data-tr="unchalik uzoq emas">недалеко</span>. <strong>Минут десять</strong> <span class="cn-word" data-pos="adv" data-tr="piyoda">пешком</span>.</p>
<p>— А если я поверну <strong>направо</strong>?</p>
<p>— Тогда вы <span class="cn-word" data-pos="verb" data-tr="tushib qolasiz, yetib borasiz">попадёте</span> на рынок, а не в музей.</p>
<p>— Спасибо большое за <span class="cn-word" data-tr="yordam">помощь</span>!</p>
<p>— Пожалуйста! <span class="cn-word" data-tr="omad">Удачи</span>!</p>
<p>Жасур пошёл прямо, как и сказал мужчина. На перекрёстке он повернул налево и уже через десять минут увидел <span class="cn-word" data-pos="adj" data-tr="chiroyli">красивое</span> <span class="cn-word" data-pos="adj" data-tr="eski">старое</span> <span class="cn-word" data-tr="bino">здание</span> музея.</p>''',
        "questions": [
            {
                "text": "Куда попадёт Жасур, если повернёт направо?",
                "choices": ["В музей", "На рынок", "В парк"],
                "answer": 1,
                "explanation": "Yoʻlovchi \"Тогда вы попадёте на рынок, а не в музей\" deb ogohlantiradi.",
            },
            {
                "text": "Сколько времени нужно идти пешком до музея?",
                "choices": ["Около пяти минут", "Около десяти минут", "Около часа"],
                "answer": 1,
                "explanation": "\"Минут десять пешком\" deb aytiladi.",
            },
            {
                "text": "Как Жасур в итоге нашёл музей?",
                "choices": ["Он поехал на такси", "Он пошёл прямо и повернул налево, как ему сказали", "Он спросил ещё одного человека"],
                "answer": 1,
                "explanation": "\"Жасур пошёл прямо ... повернул налево\" — aynan yoʻlovchi aytgandek yurib, muzeyni topadi.",
            },
        ],
    },
    {
        "title":   "Покупки в магазине",
        "summary": "Qizaloq doʻkondan qishki kurtka tanlab, oʻlchab koʻrib, karta bilan sotib oladi.",
        "order":   5,
        "grammar": [
            {
                "pattern":  "Мне нужен/нужна/нужно ...",
                "meaning":  "Menga ... kerak — dativ + qisqa sifatdosh, ot jinsiga qarab нужен/нужна/нужно oʻzgaradi.",
                "examples": ["Мне нужен новый телефон.", "Мне нужна помощь."],
            },
            {
                "pattern":  "Мне нравится ...",
                "meaning":  "Menga ... yoqadi — dativ konstruksiyasi bilan yoqtirishni bildirish.",
                "examples": ["Мне нравится синий цвет.", "Мне нравится этот фильм."],
            },
            {
                "pattern":  "Сколько стоит ...?",
                "meaning":  "... qancha turadi? — narx soʻrashning asosiy iborasi.",
                "examples": ["Сколько стоит эта куртка?", "Сколько стоят билеты?"],
            },
        ],
        "body": '''<p>Севара пошла в магазин <span class="cn-word" data-tr="kiyim-kechak">одежды</span>, чтобы купить новую <span class="cn-word" data-tr="kurtka">куртку</span> на зиму.</p>
<p>— Здравствуйте! Могу я вам помочь? — спросила <span class="cn-word" data-tr="sotuvchi ayol">продавщица</span>.</p>
<p>— Да, пожалуйста. Я <span class="cn-word" data-pos="verb" data-tr="qidiryapman">ищу</span> тёплую куртку.</p>
<p>— Какой <span class="cn-word" data-tr="oʻlcham">размер</span> вам нужен?</p>
<p>— <strong>Мне нужен</strong> сорок второй размер.</p>
<p>— Вот, посмотрите эту куртку. Есть чёрный, синий и красный <span class="cn-word" data-tr="ranglar">цвета</span>.</p>
<p>— <strong>Мне нравится</strong> синий цвет. Можно её <span class="cn-word" data-pos="verb" data-tr="kiyib koʻrmoq">примерить</span>?</p>
<p>— Конечно, <span class="cn-word" data-tr="kiyinish xonasi">примерочная</span> вон там.</p>
<p>Через несколько минут Севара вышла из примерочной.</p>
<p>— Ну как? — спросила продавщица.</p>
<p>— Отлично! Куртка тёплая и очень <span class="cn-word" data-pos="adj" data-tr="qulay">удобная</span>. <strong>Сколько</strong> она <strong>стоит</strong>?</p>
<p>— Двести пятьдесят тысяч сум.</p>
<p>— Хорошо, я её <span class="cn-word" data-pos="verb" data-tr="olaman">беру</span>.</p>
<p>Севара <span class="cn-word" data-tr="xursandchilik bilan">с радостью</span> вышла из магазина в новой тёплой куртке — как раз к первому <span class="cn-word" data-tr="qor">снегу</span>.</p>''',
        "questions": [
            {
                "text": "Какой размер куртки нужен Севаре?",
                "choices": ["Сорок второй", "Сорок четвёртый", "Тридцать восьмой"],
                "answer": 0,
                "explanation": "\"Мне нужен сорок второй размер\" deb aytadi.",
            },
            {
                "text": "Какого цвета куртку выбрала Севара?",
                "choices": ["Чёрного", "Синего", "Красного"],
                "answer": 1,
                "explanation": "\"Мне нравится синий цвет\" deb aytadi va aynan shuni tanlaydi.",
            },
            {
                "text": "Сколько стоила куртка?",
                "choices": ["Сто пятьдесят тысяч сум", "Двести пятьдесят тысяч сум", "Триста тысяч сум"],
                "answer": 1,
                "explanation": "Sotuvchi \"Двести пятьдесят тысяч сум\" deb javob beradi.",
            },
        ],
    },
]
