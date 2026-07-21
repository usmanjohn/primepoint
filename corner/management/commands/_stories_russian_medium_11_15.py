# Orta rus hikoyalari — stories 11-15 (Claude-authored, pre-intermediate/intermediate B1 level).
# Import: python manage.py import_corner corner/management/commands/_stories_russian_medium_11_15.py --author=<AUTHOR>

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
        "title":   "Кулинарный конкурс",
        "summary": "Zamira kulinariya tanlovida torti kuyib qolgani sabab tashvishga tushadi, ammo aynan shu nuqson unga birinchi oʻrinni olib beradi.",
        "order":   11,
        "grammar": [
            {
                "pattern":  "как назло",
                "meaning":  "achinarlisi, aynan shu paytda — yomon vaziyat noqulay vaqtda yuz berganini bildiruvchi ibora.",
                "examples": ["Как назло, пошёл дождь.", "Как назло, автобус опоздал именно сегодня."],
            },
            {
                "pattern":  "Стоило только ..., как ...",
                "meaning":  "arzimagan fursatda ... boʻldiki — kutilmagan tez sodir boʻlgan voqeani bildiruvchi konstruksiya.",
                "examples": ["Стоило только выйти из дома, как начался дождь.", "Стоило только сесть, как зазвонил телефон."],
            },
            {
                "pattern":  "надеяться, что ...",
                "meaning":  "umid qilmoq, ...deb umid qilish.",
                "examples": ["Надеюсь, что всё получится.", "Я надеюсь, что вы придёте."],
            },
        ],
        "body": '''<p>Замира несколько недель готовилась к <span class="cn-word" data-tr="kulinariya tanlovi">кулинарному конкурсу</span>. Она хотела приготовить <span class="cn-word" data-pos="adj" data-tr="murakkab">сложный</span> торт с несколькими слоями.</p>
<p>Но, <strong>как назло</strong>, именно в день конкурса духовка на кухне начала работать неправильно.</p>
<p><strong>Стоило только</strong> Замире отвернуться на минуту, <strong>как</strong> верхний слой торта <span class="cn-word" data-pos="verb" data-tr="kuyib ketdi">подгорел</span>.</p>
<p>— Не может быть! — <span class="cn-word" data-pos="verb" data-tr="baqirib yubordi">воскликнула</span> она, глядя на <span class="cn-word" data-pos="adj" data-tr="notekis">неровный</span>, слегка тёмный торт.</p>
<p>Времени на новый торт уже не было. Замира <span class="cn-word" data-pos="verb" data-tr="qaror qildi">решила</span> просто <span class="cn-word" data-pos="verb" data-tr="bezashga">украсить</span> подгоревшие места ягодами и мятой, чтобы хоть немного <span class="cn-word" data-pos="verb" data-tr="yashirmoq">скрыть</span> проблему.</p>
<p>— <strong>Надеюсь, что</strong> судьи не заметят, — <span class="cn-word" data-pos="verb" data-tr="shivirladi">прошептала</span> она подруге.</p>
<p>Когда судьи <span class="cn-word" data-pos="verb" data-tr="tatib koʻrishdi">попробовали</span> торт, один из них удивлённо <span class="cn-word" data-pos="verb" data-tr="koʻtardi">поднял</span> брови.</p>
<p>— Этот <span class="cn-word" data-pos="adj" data-tr="mazali">насыщенный</span>, слегка карамелизованный вкус — очень интересное решение! Кто это придумал?</p>
<p>Замира <span class="cn-word" data-pos="verb" data-tr="hayron qoldi">растерялась</span>, а потом честно призналась, что торт просто подгорел.</p>
<p>Судьи <span class="cn-word" data-pos="verb" data-tr="kulishdi">рассмеялись</span> и всё равно <span class="cn-word" data-pos="verb" data-tr="berishdi">отдали</span> ей первое место — за смелость и находчивость.</p>
<p>— Иногда лучшие рецепты <span class="cn-word" data-pos="verb" data-tr="tugʻiladi">рождаются</span> из ошибок, — сказала она потом с улыбкой.</p>''',
        "questions": [
            {
                "text": "Что случилось с тортом Замиры перед конкурсом?",
                "choices": ["Он получился идеальным", "Верхний слой подгорел из-за духовки", "Она забыла его приготовить"],
                "answer": 1,
                "explanation": "\"Верхний слой торта подгорел\" из-за неисправной духовки deyiladi.",
            },
            {
                "text": "Как Замира попыталась исправить ситуацию?",
                "choices": ["Приготовила новый торт с нуля", "Украсила подгоревшие места ягодами и мятой", "Отказалась от участия в конкурсе"],
                "answer": 1,
                "explanation": "\"Решила украсить подгоревшие места ягодами и мятой\" deyiladi.",
            },
            {
                "text": "Почему судьи всё равно дали Замире первое место?",
                "choices": ["Им понравился необычный вкус и её честность", "Другие участники не пришли", "Замира была единственной участницей"],
                "answer": 0,
                "explanation": "Sudyalarga \"насыщенный, слегка карамелизованный вкус\" yoqadi va uning halolligini qadrlashadi.",
            },
        ],
    },
    {
        "title":   "Потерявшийся кот",
        "summary": "Malikaning mushugi gʻoyib boʻlganda butun mahalla uni qidirishga tushadi, va uni topishga uyatchan bir bola yordam beradi.",
        "order":   12,
        "grammar": [
            {
                "pattern":  "то ли ..., то ли ...",
                "meaning":  "...mi, ...mi — ikkilanish, aniq sababni bilmaslikni bildiruvchi konstruksiya.",
                "examples": ["То ли он забыл, то ли не хотел приходить.", "То ли дождь, то ли снег — трудно понять."],
            },
            {
                "pattern":  "благодаря + dativ",
                "meaning":  "...tufayli, ...sabab — odatda ijobiy natijani bildiruvchi konstruksiya.",
                "examples": ["Благодаря другу я нашёл работу.", "Благодаря дождю трава стала зелёной."],
            },
            {
                "pattern":  "продолжать + infinitiv",
                "meaning":  "davom ettirmoq.",
                "examples": ["Они продолжали искать до вечера.", "Она продолжает учить русский язык."],
            },
        ],
        "body": '''<p>Утром Малика <span class="cn-word" data-pos="verb" data-tr="payqadi">заметила</span>, что дверь балкона <span class="cn-word" data-pos="adj" data-tr="ochiq">открыта</span>, а её кот Пушок <span class="cn-word" data-pos="verb" data-tr="yoʻq boʻlib qolgan edi">исчез</span>.</p>
<p>— Пушок! Пушок! — <span class="cn-word" data-pos="verb" data-tr="chaqirdi">звала</span> она, бегая по двору.</p>
<p><strong>То ли</strong> кот испугался грозы ночью, <strong>то ли</strong> просто захотел погулять — никто не знал.</p>
<p>Малика <span class="cn-word" data-pos="verb" data-tr="yozdi">написала</span> в чат соседей, и уже через час весь двор <span class="cn-word" data-pos="verb" data-tr="qidirishga tushdi">искал</span> Пушка.</p>
<p>Соседи <strong>продолжали</strong> искать даже под вечер, хотя многие уже устали и хотели домой.</p>
<p>Вдруг маленький мальчик из соседнего подъезда, обычно очень <span class="cn-word" data-pos="adj" data-tr="uyatchan">застенчивый</span>, тихо подошёл к Малике.</p>
<p>— Я видел кота под старой машиной у гаражей, — <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span> он тихим голосом.</p>
<p><strong>Благодаря</strong> ему они быстро <span class="cn-word" data-pos="verb" data-tr="topishdi">нашли</span> Пушка — испуганного, но целого и невредимого.</p>
<p>— Спасибо тебе огромное! — <span class="cn-word" data-pos="verb" data-tr="quchoqladi">обняла</span> Малика мальчика.</p>
<p>Мальчик <span class="cn-word" data-pos="verb" data-tr="qizardi">покраснел</span> от смущения, но был явно <span class="cn-word" data-pos="adj" data-tr="baxtli">счастлив</span>, что помог. С того дня весь двор знал его как «того самого героя, который спас кота».</p>''',
        "questions": [
            {
                "text": "Почему кот Малики оказался на улице?",
                "choices": ["Причина точно неизвестна — то ли испугался грозы, то ли захотел погулять", "Малика сама его выпустила", "Кот сбежал от соседской собаки"],
                "answer": 0,
                "explanation": "\"То ли кот испугался грозы ночью, то ли просто захотел погулять — никто не знал\" deyiladi.",
            },
            {
                "text": "Кто помог найти кота?",
                "choices": ["Полицейский", "Застенчивый мальчик из соседнего подъезда", "Продавец из магазина"],
                "answer": 1,
                "explanation": "\"Я видел кота под старой машиной у гаражей\" deb aytgan bola yordam beradi.",
            },
            {
                "text": "Как изменилось отношение соседей к мальчику после этого случая?",
                "choices": ["Они его не заметили", "Он стал известен как герой, который спас кота", "Они разозлились на него"],
                "answer": 1,
                "explanation": "\"Весь двор знал его как того самого героя, который спас кота\" deyiladi.",
            },
        ],
    },
    {
        "title":   "Опоздание на самолёт",
        "summary": "Aziz aeroportga kechikib qolayotganda taksichi va aeroport xodimasining yordami tufayli reysga ulguradi.",
        "order":   13,
        "grammar": [
            {
                "pattern":  "вряд ли",
                "meaning":  "amin emasman, ehtimoli kam — shubha bildiruvchi kirish soʻz.",
                "examples": ["Вряд ли он придёт вовремя.", "Вряд ли это правда."],
            },
            {
                "pattern":  "Если что, ...",
                "meaning":  "agar biror narsa yuz bersa, ... — ehtiyot shart maʼnosidagi soʻzlashuv iborasi.",
                "examples": ["Если что, звони мне.", "Если что, я знаю короткую дорогу."],
            },
            {
                "pattern":  "Пора + infinitiv",
                "meaning":  "...ish vaqti keldi — zaruriy harakatga undash konstruksiyasi.",
                "examples": ["Пора бежать!", "Пора вставать, уже утро."],
            },
        ],
        "body": '''<p>Азиз <span class="cn-word" data-pos="verb" data-tr="ketayotgan edi">ехал</span> в аэропорт, когда машина попала в <span class="cn-word" data-pos="adj" data-tr="uzun">длинную</span> пробку.</p>
<p>— <strong>Вряд ли</strong> я успею на рейс, — <span class="cn-word" data-pos="verb" data-tr="tashvishlanib oʻyladi">подумал</span> он, глядя на часы.</p>
<p>Таксист, <span class="cn-word" data-pos="verb" data-tr="his qilib">почувствовав</span> его волнение, сказал:</p>
<p>— <strong>Если что</strong>, я знаю короткую дорогу через старый район.</p>
<p>Он <span class="cn-word" data-pos="verb" data-tr="burildi">свернул</span> на узкую улицу, и через десять минут они <span class="cn-word" data-pos="verb" data-tr="yetib kelishdi">подъехали</span> к аэропорту.</p>
<p>— <strong>Пора</strong> бежать! — <span class="cn-word" data-pos="verb" data-tr="baqirdi">крикнул</span> таксист, помогая достать чемодан.</p>
<p>Азиз <span class="cn-word" data-pos="verb" data-tr="yugurdi">побежал</span> к стойке регистрации, но она уже <span class="cn-word" data-pos="verb" data-tr="yopilgan edi">закрылась</span>.</p>
<p>— Пожалуйста, помогите! Мой рейс через пятнадцать минут! — <span class="cn-word" data-pos="verb" data-tr="yalinib soʻradi">взмолился</span> он сотруднице аэропорта.</p>
<p>Женщина <span class="cn-word" data-pos="verb" data-tr="qaradi">посмотрела</span> на его билет и, <span class="cn-word" data-pos="adj" data-tr="mehribonlik bilan">по-доброму</span> улыбнувшись, быстро <span class="cn-word" data-pos="verb" data-tr="roʻyxatdan oʻtkazdi">оформила</span> его багаж.</p>
<p>— Бегите скорее, пятый выход! Я предупрежу пилотов.</p>
<p>Азиз, <span class="cn-word" data-pos="adj" data-tr="nafas qisilib">запыхавшийся</span>, вбежал в самолёт последним — двери закрылись сразу за ним.</p>
<p>— Спасибо огромное всем, кто мне сегодня помог, — подумал он, наконец опускаясь в кресло с облегчением.</p>''',
        "questions": [
            {
                "text": "Почему Азиз боялся опоздать на рейс?",
                "choices": ["Машина попала в длинную пробку", "Он проспал", "Он забыл билет дома"],
                "answer": 0,
                "explanation": "\"Машина попала в длинную пробку\" deb aytiladi.",
            },
            {
                "text": "Кто помог Азизу срезать путь до аэропорта?",
                "choices": ["Полицейский", "Таксист, который знал короткую дорогу", "Друг на машине"],
                "answer": 1,
                "explanation": "\"Я знаю короткую дорогу через старый район\" deb taksichi yordam beradi.",
            },
            {
                "text": "Что сделала сотрудница аэропорта, увидев, что Азиз опаздывает?",
                "choices": ["Отказала ему в посадке", "Быстро оформила его багаж и разрешила пробежать к выходу", "Отправила его на следующий рейс"],
                "answer": 1,
                "explanation": "\"Быстро оформила его багаж... Бегите скорее, пятый выход!\" deydi.",
            },
        ],
    },
    {
        "title":   "Старая гитара",
        "summary": "Botir bozordan arzon narxda eski gitara sotib oladi va uning mashhur musiqachiga tegishli boʻlganini bilib, uni qizga qaytarish qarorini qabul qiladi.",
        "order":   14,
        "grammar": [
            {
                "pattern":  "стоить + narx",
                "meaning":  "qiymatga ega boʻlmoq, narxi bo'lmoq.",
                "examples": ["Сколько стоит эта гитара?", "Эта вещь стоит очень дорого."],
            },
            {
                "pattern":  "не задумываясь",
                "meaning":  "oʻylab oʻtirmasdan — tez, ikkilanmasdan qilingan harakatni bildiruvchi ravishdosh.",
                "examples": ["Он купил её, не задумываясь.", "Она согласилась, не задумываясь."],
            },
            {
                "pattern":  "оставаться / остаться + instr.",
                "meaning":  "...boʻlib qolmoq — holatning davom etishini bildiruvchi fe'l jufti.",
                "examples": ["Такая вещь должна оставаться в семье.", "Он остался её лучшим другом."],
            },
        ],
        "body": '''<p>На воскресном <span class="cn-word" data-tr="bozor">базаре</span> Ботир <span class="cn-word" data-pos="verb" data-tr="payqab qoldi">заметил</span> старую, <span class="cn-word" data-pos="adj" data-tr="chang bosgan">пыльную</span> гитару среди других вещей.</p>
<p>— Сколько она <strong>стоит</strong>? — <span class="cn-word" data-pos="verb" data-tr="soʻradi">спросил</span> он у продавца.</p>
<p>— Всего десять тысяч сум, забирай, — ответил тот <span class="cn-word" data-pos="adj" data-tr="beparvo">равнодушно</span>.</p>
<p>Ботир купил гитару, <strong>не задумываясь</strong>, просто потому что она ему понравилась.</p>
<p>Дома, <span class="cn-word" data-pos="verb" data-tr="tozalayotib">протирая</span> инструмент, он <span class="cn-word" data-pos="verb" data-tr="payqadi">заметил</span> внутри маленькую <span class="cn-word" data-tr="yozuv">гравировку</span> с именем известного музыканта, который играл в городе много лет назад.</p>
<p>Ботир <span class="cn-word" data-pos="verb" data-tr="qidirdi">поискал</span> информацию в интернете и <span class="cn-word" data-pos="verb" data-tr="bilib oldi">узнал</span>, что у музыканта осталась дочь, живущая недалеко.</p>
<p>Он мог бы <span class="cn-word" data-pos="verb" data-tr="sotmoq">продать</span> гитару коллекционерам за большие деньги, но <span class="cn-word" data-pos="verb" data-tr="qaror qildi">решил</span> иначе.</p>
<p>Ботир <span class="cn-word" data-pos="verb" data-tr="topdi">нашёл</span> дочь музыканта и <span class="cn-word" data-pos="verb" data-tr="qaytardi">вернул</span> ей гитару отца.</p>
<p>— Я не могу принять деньги за это, — сказал он. — Такая вещь должна <strong>оставаться</strong> в семье.</p>
<p>Женщина <span class="cn-word" data-pos="verb" data-tr="yigʻlab yubordi">расплакалась</span> от благодарности — гитара отца была для неё <span class="cn-word" data-pos="adj" data-tr="bebaho">бесценной</span>.</p>''',
        "questions": [
            {
                "text": "Где Ботир нашёл старую гитару?",
                "choices": ["В магазине музыкальных инструментов", "На воскресном базаре", "В доме бабушки"],
                "answer": 1,
                "explanation": "\"На воскресном базаре Ботир заметил старую... гитару\" deyiladi.",
            },
            {
                "text": "Что Ботир обнаружил на гитаре после того, как протёр её?",
                "choices": ["Трещину", "Гравировку с именем известного музыканта", "Цену от прошлого владельца"],
                "answer": 1,
                "explanation": "\"Заметил внутри маленькую гравировку с именем известного музыканта\" deyiladi.",
            },
            {
                "text": "Что решил сделать Ботир вместо продажи гитары коллекционерам?",
                "choices": ["Оставить гитару себе", "Продать её ещё дороже", "Найти и вернуть гитару дочери музыканта"],
                "answer": 2,
                "explanation": "\"Нашёл дочь музыканта и вернул ей гитару отца\" deyiladi.",
            },
        ],
    },
    {
        "title":   "Встреча выпускников",
        "summary": "Nodira bitiruvchilar uchrashuviga oʻzini boshqalar bilan solishtirib tashvish bilan boradi, ammo bir vaqtlar hasad qilgan doʻsti unga hayratini bildirib, muhim saboq beradi.",
        "order":   15,
        "grammar": [
            {
                "pattern":  "сравнивать себя с + instr.",
                "meaning":  "oʻzini ... bilan solishtirmoq.",
                "examples": ["Не сравнивай себя с другими.", "Она сравнивала себя с одноклассницей."],
            },
            {
                "pattern":  "признаться (себе), что ...",
                "meaning":  "(oʻziga) tan olmoq, ...ekanini eʼtirof etmoq.",
                "examples": ["Она должна была признаться себе, что была неправа.", "Признаюсь, что я тоже волновался."],
            },
            {
                "pattern":  "с тех пор как ...",
                "meaning":  "...dan beri, oʻsha paytdan boshlab — vaqt ergash gapi.",
                "examples": ["С тех пор как она услышала эти слова, всё изменилось.", "С тех пор как мы познакомились, прошло десять лет."],
            },
        ],
        "body": '''<p>Нодира <span class="cn-word" data-pos="verb" data-tr="tayyorlanardi">готовилась</span> к встрече выпускников с <span class="cn-word" data-pos="adj" data-tr="aralash">смешанными</span> чувствами. Она <span class="cn-word" data-pos="verb" data-tr="qoʻrqardi">боялась</span>, что все увидят, как мало она <span class="cn-word" data-pos="verb" data-tr="erishdi">добилась</span> по сравнению с одноклассниками.</p>
<p>Всю дорогу она <strong>сравнивала себя с</strong> Гульнорой, которая, как она слышала, стала успешным <span class="cn-word" data-tr="advokat">адвокатом</span>.</p>
<p>В зале ресторана Нодира <span class="cn-word" data-pos="verb" data-tr="koʻrdi">увидела</span> Гульнору, которая сразу подошла к ней с широкой улыбкой.</p>
<p>— Нодира! Как я рада тебя видеть! Ты стала <span class="cn-word" data-pos="adj" data-tr="ajoyib">потрясающим</span> учителем — мои соседи говорят, что их дети обожают твои уроки!</p>
<p>Нодира <span class="cn-word" data-pos="verb" data-tr="hayron qoldi">удивилась</span>. Она должна была <strong>признаться себе</strong>, что никогда не думала о своей работе как о чём-то важном.</p>
<p>— А я всегда тебе <span class="cn-word" data-pos="verb" data-tr="hasad qilardim">завидовала</span> в школе, — <span class="cn-word" data-pos="verb" data-tr="tan oldi">призналась</span> Гульнора. — Ты всегда была такой <span class="cn-word" data-pos="adj" data-tr="ijodkor">творческой</span> и <span class="cn-word" data-pos="adj" data-tr="mehribon">доброй</span>.</p>
<p><strong>С тех пор как</strong> она услышала эти слова, Нодира <span class="cn-word" data-pos="verb" data-tr="qaray boshladi">начала</span> смотреть на свою жизнь по-другому.</p>
<p>— Спасибо, что сказала это, — <span class="cn-word" data-pos="verb" data-tr="jilmayib qoʻydi">улыбнулась</span> она. — Кажется, я слишком долго сравнивала себя с другими, вместо того чтобы гордиться собой.</p>''',
        "questions": [
            {
                "text": "Почему Нодира нервничала перед встречей выпускников?",
                "choices": ["Она боялась опоздать", "Она сравнивала свои достижения с одноклассниками", "Она забыла, как выглядят одноклассники"],
                "answer": 1,
                "explanation": "\"Всю дорогу она сравнивала себя с Гульнорой\" deyiladi.",
            },
            {
                "text": "Что сказала Гульнора о работе Нодиры?",
                "choices": ["Что учителем быть скучно", "Что Нодира стала потрясающим учителем, которого любят ученики", "Что Нодире стоило выбрать другую профессию"],
                "answer": 1,
                "explanation": "\"Ты стала потрясающим учителем... их дети обожают твои уроки!\" deydi.",
            },
            {
                "text": "Что поняла Нодира к концу встречи?",
                "choices": ["Что нужно продолжать сравнивать себя с другими", "Что не стоит сравнивать себя с другими, а нужно гордиться собой", "Что она хочет стать адвокатом"],
                "answer": 1,
                "explanation": "\"Я слишком долго сравнивала себя с другими, вместо того чтобы гордиться собой\" deydi.",
            },
        ],
    },
]
