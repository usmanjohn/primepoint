# Orta rus hikoyalari — stories 6-10 (Claude-authored, pre-intermediate/intermediate B1 level).
# Import: python manage.py import_corner corner/management/commands/_stories_russian_medium_6_10.py --author=<AUTHOR>

SUBJECT = {
    "name":    "Russian",
    "summary": "Rus tili: zamonaviy hikoyalar, lugʻat va grammatika bilan.",
    "icon":    "bi-translate",
    "color":   "#b91c1c",
}

COLLECTION = {
    "title":       "Orta rus hikoyalari",
    "description": "Orta daraja (B1) — kengroq lugʻat va grammatika bilan qiziqarli hikoyalar, oson va zamonaviy toʻplamlar orasidagi bosqich.",
    "order":       2,
}

STORIES = [
    {
        "title":   "Первый день на работе",
        "summary": "Odil yangi ish joyidagi birinchi kunida stolni chalkashtirib qoʻyadi, ammo bu kulgili hodisa uni jamoaga yaqinlashtiradi.",
        "order":   6,
        "grammar": [
            {
                "pattern":  "перепутать",
                "meaning":  "adashtirib yubormoq — ikki narsani bir-biriga aralashtirib qoʻyish (tugallangan fe'l).",
                "examples": ["Он перепутал стол.", "Извини, я перепутал твоё имя."],
            },
            {
                "pattern":  "как только ...",
                "meaning":  "...gan zahoti — ikki harakat orasidagi zudlikni bildiruvchi vaqt ergash gapi.",
                "examples": ["Как только он вошёл, все замолчали.", "Позвони мне, как только придёшь."],
            },
            {
                "pattern":  "чувствовать себя + qanday",
                "meaning":  "oʻzini qanday his qilmoq — holat yoki kayfiyatni ifodalash konstruksiyasi.",
                "examples": ["Я чувствую себя хорошо.", "Он чувствовал себя уверенно."],
            },
        ],
        "body": '''<p>Одил <span class="cn-word" data-pos="verb" data-tr="uygʻondi">проснулся</span> рано утром — сегодня был его <span class="cn-word" data-pos="adj" data-tr="birinchi">первый</span> день на новой работе. Он очень <span class="cn-word" data-pos="verb" data-tr="hayajonlanardi">волновался</span> и несколько раз <span class="cn-word" data-pos="verb" data-tr="tekshirdi">проверил</span> будильник ночью.</p>
<p><strong>Как только</strong> он вошёл в офис, к нему подошла девушка и сказала: — Здравствуйте! Меня зовут Севиль, я покажу вам ваше рабочее место.</p>
<p>Одил <span class="cn-word" data-pos="verb" data-tr="ergashdi">последовал</span> за ней, но, к сожалению, <strong>перепутал</strong> стол: он сел за стол коллеги по имени Жасур, который в этот момент был на встрече.</p>
<p>Через десять минут Жасур <span class="cn-word" data-pos="verb" data-tr="qaytib keldi">вернулся</span> и с удивлением <span class="cn-word" data-pos="verb" data-tr="qaradi">посмотрел</span> на Одила, сидящего за его компьютером.</p>
<p>— Извините, кажется, это ваше место? — <span class="cn-word" data-pos="adj" data-tr="uyalgan holda">смущённо</span> спросил Одил, вставая.</p>
<p>Жасур <span class="cn-word" data-pos="verb" data-tr="kuldi">рассмеялся</span>. — Ничего страшного, у нас тут все столы <span class="cn-word" data-pos="adj" data-tr="oʻxshash">похожи</span> друг на друга! Даже я в первый день сел не на своё место.</p>
<p>Все <span class="cn-word" data-pos="verb" data-tr="kulishdi">засмеялись</span>, и Одил сразу <span class="cn-word" data-pos="verb" data-tr="his qildi">почувствовал</span> себя <span class="cn-word" data-pos="adj" data-tr="qulay">комфортно</span> в новом коллективе.</p>
<p>К обеду он уже <span class="cn-word" data-pos="verb" data-tr="bilib oldi">запомнил</span> имена всех коллег и понял, что <strong>чувствует себя</strong> здесь на удивление <span class="cn-word" data-pos="adj" data-tr="uyda kabi">по-домашнему</span>.</p>
<p>— Первый день оказался не таким страшным, как я думал, — сказал он себе вечером, идя домой с улыбкой.</p>''',
        "questions": [
            {
                "text": "Что перепутал Одил в первый день?",
                "choices": ["Время встречи", "Стол коллеги", "Название компании"],
                "answer": 1,
                "explanation": "\"Перепутал стол: он сел за стол коллеги по имени Жасур\" deyiladi.",
            },
            {
                "text": "Как отреагировал Жасур, увидев Одила за своим столом?",
                "choices": ["Он рассердился", "Он рассмеялся и успокоил Одила", "Он пожаловался начальнику"],
                "answer": 1,
                "explanation": "\"Жасур рассмеялся. Ничего страшного...\" deb aytadi.",
            },
            {
                "text": "Как Одил чувствовал себя к концу первого дня?",
                "choices": ["Он чувствовал себя очень неловко", "Он почувствовал себя комфортно в коллективе", "Он решил уволиться"],
                "answer": 1,
                "explanation": "\"Одил сразу почувствовал себя комфортно в новом коллективе\" deyiladi.",
            },
        ],
    },
    {
        "title":   "Ночной поезд",
        "summary": "Madina tungi poyezdda hayajondan uxlay olmay, keksa hamroh bilan suhbatlashib, hayotiy saboq oladi.",
        "order":   7,
        "grammar": [
            {
                "pattern":  "не мочь + infinitiv",
                "meaning":  "... olmaslik — imkoniyat yoki holat yoʻqligini bildiruvchi konstruksiya.",
                "examples": ["Я не могла уснуть.", "Он не мог понять решение."],
            },
            {
                "pattern":  "чем ..., тем ...",
                "meaning":  "qancha ..., shuncha ... — mutanosib qiyoslashni bildiruvchi konstruksiya.",
                "examples": ["Чем больше читаешь, тем больше знаешь.", "Чем раньше, тем лучше."],
            },
            {
                "pattern":  "стать / становиться + instr.",
                "meaning":  "...boʻlib qolmoq — holat oʻzgarishini bildiruvchi fe'l jufti (tugallangan/tugallanmagan).",
                "examples": ["Он стал моим другом.", "Она становится увереннее с каждым днём."],
            },
        ],
        "body": '''<p>Мадина <span class="cn-word" data-pos="verb" data-tr="oʻtirdi">села</span> в ночной поезд, направляясь в другой город на важную конференцию. Она была так <span class="cn-word" data-pos="adj" data-tr="tashvishlangan">взволнована</span> предстоящим выступлением, что <strong>не могла</strong> уснуть.</p>
<p>Напротив неё сидел пожилой мужчина, который спокойно <span class="cn-word" data-pos="verb" data-tr="oʻqiyotgan edi">читал</span> книгу.</p>
<p>— Не спится? — <span class="cn-word" data-pos="verb" data-tr="soʻradi">спросил</span> он с доброй улыбкой.</p>
<p>— Да, я слишком <span class="cn-word" data-pos="verb" data-tr="tashvishlanaman">переживаю</span> из-за завтрашнего доклада, — <span class="cn-word" data-pos="verb" data-tr="tan oldi">призналась</span> Мадина.</p>
<p>— Знаете, — <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span> мужчина, — <strong>чем</strong> больше мы <span class="cn-word" data-pos="verb" data-tr="tashvishlanamiz">волнуемся</span>, <strong>тем</strong> хуже мы себя чувствуем. Я сам раньше был таким же.</p>
<p>Он <span class="cn-word" data-pos="verb" data-tr="aytib berdi">рассказал</span> ей о своей молодости, о том, как он <span class="cn-word" data-pos="verb" data-tr="qoʻrqib yashagan">боялся</span> каждого важного момента в жизни, пока не понял, что жизнь <span class="cn-word" data-pos="adj" data-tr="qisqa">коротка</span>, чтобы тратить её на страх.</p>
<p>— <span class="cn-word" data-tr="ertaga">Завтра</span> вы просто расскажете о том, что хорошо знаете, — <span class="cn-word" data-pos="verb" data-tr="tinchlantirdi">успокоил</span> он её.</p>
<p>Мадина <span class="cn-word" data-pos="verb" data-tr="chuqur nafas oldi">вздохнула</span> спокойнее и, наконец, <span class="cn-word" data-pos="verb" data-tr="uxlab qoldi">уснула</span> под мерный стук колёс.</p>
<p>Утром, выходя из поезда, она поблагодарила незнакомца, который <strong>стал</strong> для неё <span class="cn-word" data-tr="tasodifiy ustoz">случайным учителем</span> на одну ночь.</p>''',
        "questions": [
            {
                "text": "Почему Мадина не могла уснуть в поезде?",
                "choices": ["Ей было холодно", "Она сильно переживала из-за завтрашнего доклада", "В вагоне было шумно"],
                "answer": 1,
                "explanation": "\"Я слишком переживаю из-за завтрашнего доклада\" deb tan oladi.",
            },
            {
                "text": "Что посоветовал пожилой мужчина Мадине?",
                "choices": ["Отменить доклад", "Не волноваться и просто рассказать то, что она хорошо знает", "Прочитать его книгу"],
                "answer": 1,
                "explanation": "\"Завтра вы просто расскажете о том, что хорошо знаете\" deb tinchlantiradi.",
            },
            {
                "text": "Кем стал пожилой мужчина для Мадины к концу поездки?",
                "choices": ["Случайным учителем на одну ночь", "Её начальником", "Незнакомцем, о котором она сразу забыла"],
                "answer": 0,
                "explanation": "\"Незнакомец, который стал для неё случайным учителем на одну ночь\" deyiladi.",
            },
        ],
    },
    {
        "title":   "Бабушкин секрет",
        "summary": "Dilnoza chordoqdan topilgan eski xat orqali buvisining yoshligidagi katta tanlovi haqida bilib oladi va u bilan yanada yaqinlashadi.",
        "order":   8,
        "grammar": [
            {
                "pattern":  "хотя ...",
                "meaning":  "...ga qaramasdan, garchi... — qarshilik/ziddiyat ergash gapini bildiruvchi konstruksiya.",
                "examples": ["Хотя он любил её, она осталась.", "Хотя было поздно, они продолжали работать."],
            },
            {
                "pattern":  "быть готовым / готова + infinitiv",
                "meaning":  "biror ish qilishga tayyor boʻlmoq.",
                "examples": ["Она не была готова оставить семью.", "Мы готовы начать прямо сейчас."],
            },
            {
                "pattern":  "никогда не + fe'l",
                "meaning":  "hech qachon ... qilmaslik — kuchli inkorni bildiruvchi konstruksiya.",
                "examples": ["Я никогда не жалела о своём решении.", "Он никогда не опаздывает."],
            },
        ],
        "body": '''<p>Дилноза <span class="cn-word" data-pos="verb" data-tr="tozalayotgan edi">убирала</span> чердак бабушкиного дома, когда наткнулась на старую <span class="cn-word" data-tr="quti">коробку</span> с письмами.</p>
<p>Среди них было одно <span class="cn-word" data-pos="adj" data-tr="sargʻayib ketgan">пожелтевшее</span> письмо, <span class="cn-word" data-pos="adj" data-tr="ellik yillik">пятидесятилетней</span> давности. Дилноза <span class="cn-word" data-pos="verb" data-tr="ochib oʻqidi">развернула</span> его и начала читать.</p>
<p>Письмо было от молодого человека, который <span class="cn-word" data-pos="verb" data-tr="taklif qilgan edi">приглашал</span> её бабушку уехать с ним за границу. <strong>Хотя</strong> он очень любил её, бабушка <span class="cn-word" data-pos="verb" data-tr="rad etgan edi">отказалась</span> — она не была <strong>готова</strong> оставить свою семью.</p>
<p>Дилноза <span class="cn-word" data-pos="verb" data-tr="tushib qoldi">спустилась</span> вниз с письмом в руках.</p>
<p>— Бабушка, кто это? — <span class="cn-word" data-pos="verb" data-tr="soʻradi">спросила</span> она.</p>
<p>Бабушка долго <span class="cn-word" data-pos="verb" data-tr="jim qoldi">молчала</span>, а потом улыбнулась с <span class="cn-word" data-tr="qayg'u aralash yoqimlilik">лёгкой грустью</span>.</p>
<p>— Это был мой первый друг детства. Он звал меня в другую страну, но я <strong>никогда не</strong> жалела о своём решении остаться. Здесь была моя семья, и здесь родилась твоя мама.</p>
<p>Дилноза <span class="cn-word" data-pos="verb" data-tr="quchoqladi">обняла</span> бабушку, <span class="cn-word" data-pos="verb" data-tr="his qilib">почувствовав</span>, насколько <span class="cn-word" data-pos="adj" data-tr="qiyin">сложным</span> был этот выбор много лет назад.</p>
<p>— Спасибо, что осталась, бабушка, — <span class="cn-word" data-pos="verb" data-tr="pichirladi">прошептала</span> она.</p>''',
        "questions": [
            {
                "text": "Что нашла Дилноза на чердаке?",
                "choices": ["Старую фотографию", "Старое письмо от друга детства бабушки", "Дневник бабушки"],
                "answer": 1,
                "explanation": "\"Наткнулась на старую коробку с письмами\", ular orasida ellik yillik xat bor edi.",
            },
            {
                "text": "Почему бабушка отказалась уехать за границу?",
                "choices": ["Она не любила молодого человека", "Она не была готова оставить свою семью", "У неё не было денег на поездку"],
                "answer": 1,
                "explanation": "\"Она не была готова оставить свою семью\" deyiladi.",
            },
            {
                "text": "Что почувствовала Дилноза, узнав эту историю?",
                "choices": ["Разочарование в бабушке", "Насколько сложным был выбор бабушки много лет назад", "Желание уехать за границу"],
                "answer": 1,
                "explanation": "\"Почувствовав, насколько сложным был этот выбор много лет назад\" deyiladi.",
            },
        ],
    },
    {
        "title":   "Финал турнира",
        "summary": "\"Барс\" jamoasi finalda kutilmagan gʻalaba qozonadi — kapitan yakkaxon oʻynashdan voz kechib, jamoaviy ishonchni oʻrganadi.",
        "order":   9,
        "grammar": [
            {
                "pattern":  "несмотря на то что ...",
                "meaning":  "...ga qaramay — qarshilikni bildiruvchi ergash gap konstruksiyasi.",
                "examples": ["Несмотря на то что было поздно, они продолжали работать.", "Несмотря на то что он устал, он не сдался."],
            },
            {
                "pattern":  "начать / начинать + infinitiv",
                "meaning":  "boshlamoq — harakatning boshlanishini bildiruvchi fe'l jufti.",
                "examples": ["Матч начался тяжело.", "Он начал отдавать мяч партнёрам."],
            },
            {
                "pattern":  "друг другу / друг для друга",
                "meaning":  "bir-biriga, bir-biri uchun — ikki taraflama harakatni bildiruvchi konstruksiya.",
                "examples": ["Они помогают друг другу.", "Команда играет друг для друга."],
            },
        ],
        "body": '''<p>Команда «Барс» <span class="cn-word" data-pos="verb" data-tr="chiqdi">вышла</span> в финал турнира, <strong>несмотря на то что</strong> считалась <span class="cn-word" data-pos="adj" data-tr="eng zaif">самой слабой</span> командой в лиге.</p>
<p>Капитан команды, Отабек, всегда <span class="cn-word" data-pos="verb" data-tr="oʻynardi">играл</span> в одиночку, не <span class="cn-word" data-pos="verb" data-tr="ishonmasdi">доверяя</span> партнёрам мяч.</p>
<p>Перед финальным матчем тренер <span class="cn-word" data-pos="verb" data-tr="chaqirdi">собрал</span> команду.</p>
<p>— Мы можем <span class="cn-word" data-pos="verb" data-tr="yutmoq">выиграть</span> только если будем помогать <strong>друг другу</strong>, — <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span> он, глядя прямо на Отабека.</p>
<p>Матч <strong>начался</strong> тяжело: соперники были быстрее и <span class="cn-word" data-pos="adj" data-tr="kuchliroq">сильнее</span>. К перерыву счёт был 1:0 не в пользу «Барса».</p>
<p>В раздевалке Отабек, наконец, <span class="cn-word" data-pos="verb" data-tr="tushundi">понял</span>: одному человеку весь матч не <span class="cn-word" data-pos="verb" data-tr="yutib boʻlmaydi">выиграть</span>.</p>
<p>Во втором тайме он <strong>начал</strong> <span class="cn-word" data-pos="verb" data-tr="uzatmoq">отдавать</span> мяч партнёрам, <span class="cn-word" data-pos="verb" data-tr="ishonib">доверяя</span> им больше, чем когда-либо. Команда стала играть слаженно, как единое целое.</p>
<p>На последней минуте именно партнёр, которому Отабек <span class="cn-word" data-pos="verb" data-tr="uzatgan edi">отдал</span> мяч, <span class="cn-word" data-pos="verb" data-tr="urib kiritdi">забил</span> победный гол.</p>
<p>Команда «Барс» <span class="cn-word" data-pos="verb" data-tr="quvonib ketishdi">торжествовала</span>, а Отабек понял: настоящая победа приходит, когда команда играет <strong>друг для друга</strong>.</p>''',
        "questions": [
            {
                "text": "Почему команду «Барс» считали слабой перед финалом?",
                "choices": ["У них не было тренера", "Капитан привык играть в одиночку и не доверял партнёрам", "Команда была новая в лиге"],
                "answer": 1,
                "explanation": "\"Отабек всегда играл в одиночку, не доверяя партнёрам мяч\" deyiladi.",
            },
            {
                "text": "Что изменилось во втором тайме?",
                "choices": ["Отабек начал отдавать мяч партнёрам вместо игры в одиночку", "Тренер заменил всю команду", "Игра была остановлена из-за дождя"],
                "answer": 0,
                "explanation": "\"Он начал отдавать мяч партнёрам, доверяя им больше, чем когда-либо\" deyiladi.",
            },
            {
                "text": "Какой урок понял Отабек в конце матча?",
                "choices": ["Что нужно всегда играть в одиночку", "Что настоящая победа приходит, когда команда играет друг для друга", "Что тренер всегда неправ"],
                "answer": 1,
                "explanation": "Hikoya oxirida aynan shu xulosa aytiladi.",
            },
        ],
    },
    {
        "title":   "Потерянное письмо",
        "summary": "Pochta xodimi Davron yigirma yil avval yoʻqolgan xatni topib, uni Zarinaga yetkazadi — va aynan shu kuni akasi qoʻngʻiroq qilib, nihoyat qaytib kelayotganini aytadi.",
        "order":   10,
        "grammar": [
            {
                "pattern":  "потеряться",
                "meaning":  "yoʻqolib qolmoq — oʻzlik nisbatidagi tugallangan fe'l.",
                "examples": ["Письмо потерялось двадцать лет назад.", "Ключи потерялись где-то дома."],
            },
            {
                "pattern":  "должен был / должна была + infinitiv",
                "meaning":  "... qilishi kerak edi — oʻtmishda bajarilmagan burch/rejani bildiruvchi konstruksiya.",
                "examples": ["Письмо должно было прийти раньше.", "Я должен был позвонить тебе вчера."],
            },
            {
                "pattern":  "как раз в тот момент, когда ...",
                "meaning":  "aynan oʻsha payt, qachonki... — ikki voqeaning vaqt jihatdan mos kelishini bildiruvchi konstruksiya.",
                "examples": ["Как раз в тот момент, когда я вышел, зазвонил телефон.", "Он пришёл как раз в тот момент, когда мы уже уходили."],
            },
        ],
        "body": '''<p>Даврон работал на почте и <span class="cn-word" data-pos="verb" data-tr="tartibga solayotgan edi">разбирал</span> старый архив, когда <span class="cn-word" data-pos="verb" data-tr="topib oldi">обнаружил</span> конверт, который <strong>потерялся</strong> двадцать лет назад. Письмо <strong>должно было</strong> прийти к женщине по имени Зарина, но по ошибке осталось в архиве все эти годы.</p>
<p>Даврон нашёл её <span class="cn-word" data-tr="manzil">адрес</span> в старой базе данных и лично <span class="cn-word" data-pos="verb" data-tr="olib bordi">принёс</span> письмо.</p>
<p>— Здравствуйте, у меня для вас очень <span class="cn-word" data-pos="adj" data-tr="gʻayrioddiy">необычная</span> посылка, — сказал он, протягивая конверт. — Это письмо <span class="cn-word" data-pos="verb" data-tr="kutgan edi">ждало</span> вас двадцать лет.</p>
<p>Зарина <span class="cn-word" data-pos="verb" data-tr="hayron qoldi">удивилась</span>, увидев почерк своего брата, который много лет назад <span class="cn-word" data-pos="verb" data-tr="koʻchib ketdi">уехал</span> жить за границу.</p>
<p>Она <span class="cn-word" data-pos="verb" data-tr="ochdi">открыла</span> письмо дрожащими руками. Брат писал, что очень <span class="cn-word" data-pos="verb" data-tr="sogʻingan">скучает</span> и обещал когда-нибудь <span class="cn-word" data-pos="verb" data-tr="qaytib kelmoq">вернуться</span> домой.</p>
<p>Зарина <span class="cn-word" data-pos="verb" data-tr="yigʻladi">заплакала</span> от эмоций — письмо было написано ещё до того, как связь с братом почти <span class="cn-word" data-pos="verb" data-tr="uzilgan edi">прервалась</span>.</p>
<p><strong>Как раз в тот момент, когда</strong> она дочитала последнюю строчку, зазвонил телефон. Это был её брат — впервые за пять лет.</p>
<p>— Зарина, — сказал он взволнованно, — я наконец купил билет. Я возвращаюсь домой на следующей неделе!</p>
<p>Зарина <span class="cn-word" data-pos="verb" data-tr="kulib yubordi">рассмеялась</span> сквозь слёзы, держа в одной руке телефон, а в другой — письмо, которое ждало этого дня двадцать лет.</p>''',
        "questions": [
            {
                "text": "Что обнаружил Даврон в старом архиве почты?",
                "choices": ["Посылку с деньгами", "Письмо, которое потерялось двадцать лет назад", "Старую фотографию"],
                "answer": 1,
                "explanation": "\"Конверт, который потерялся двадцать лет назад\" deyiladi.",
            },
            {
                "text": "От кого было письмо, которое получила Зарина?",
                "choices": ["От её брата, уехавшего жить за границу", "От незнакомого человека", "От почты с извинениями"],
                "answer": 0,
                "explanation": "\"Увидев почерк своего брата, который много лет назад уехал жить за границу\" deyiladi.",
            },
            {
                "text": "Что произошло сразу после того, как Зарина дочитала письмо?",
                "choices": ["Она пошла на почту с жалобой", "Ей позвонил брат и сказал, что возвращается домой", "Письмо оказалось поддельным"],
                "answer": 1,
                "explanation": "\"Как раз в тот момент, когда она дочитала... зазвонил телефон. Это был её брат\" deyiladi.",
            },
        ],
    },
]
