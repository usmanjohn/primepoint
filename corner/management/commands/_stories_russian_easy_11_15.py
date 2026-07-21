# Oson rus hikoyalari — stories 11-15 (Claude-authored, beginner A1-A2 level, dialogue-heavy).
# Import: python manage.py import_corner corner/management/commands/_stories_russian_easy_11_15.py --author=<AUTHOR>

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
        "title":   "В библиотеке",
        "summary": "Amina kutubxonaga kitobni kechiktirib qaytarganidan tashvishlanadi, ammo koʻp oʻqigani uchun jarimasiz qoladi.",
        "order":   11,
        "grammar": [
            {
                "pattern":  "Могу я + infinitiv?",
                "meaning":  "...sam boʻladimi? — ruxsat soʻrash uchun muloyim konstruksiya.",
                "examples": ["Могу я взять эту книгу?", "Могу я задать вопрос?"],
            },
            {
                "pattern":  "Когда нужно + infinitiv?",
                "meaning":  "Qachon ... qilish kerak? — muddat yoki vaqt soʻrash uchun.",
                "examples": ["Когда нужно вернуть книгу?", "Когда нужно прийти?"],
            },
            {
                "pattern":  "Простите за ...",
                "meaning":  "... uchun kechirasiz — uzr soʻrash iborasi.",
                "examples": ["Простите за опоздание.", "Простите за беспокойство."],
            },
        ],
        "body": '''<p>Амина <span class="cn-word" data-pos="verb" data-tr="shoshildi">торопилась</span> в <span class="cn-word" data-tr="kutubxona">библиотеку</span>, потому что нужно было <span class="cn-word" data-pos="verb" data-tr="qaytarmoq">вернуть</span> книгу.</p>
<p>— Здравствуйте! <strong>Простите за</strong> опоздание, я должна была вернуть книгу ещё вчера, — сказала она библиотекарю.</p>
<p>— Ничего страшного, — <span class="cn-word" data-pos="verb" data-tr="jilmayib qoʻydi">улыбнулась</span> женщина. — <strong>Могу я</strong> спросить, какую книгу вы читали?</p>
<p>— «Приключения в горах». Очень <span class="cn-word" data-pos="adj" data-tr="qiziqarli">интересная</span> книга!</p>
<p>— <strong>Могу я</strong> взять ещё одну книгу? — спросила Амина. — Мне очень понравилось читать.</p>
<p>— Конечно! Вот вторая часть этой же истории.</p>
<p>— <strong>Когда нужно</strong> вернуть эту книгу?</p>
<p>— Через две недели. И не волнуйтесь насчёт <span class="cn-word" data-tr="jarima">штрафа</span> — вы наш <span class="cn-word" data-pos="adj" data-tr="eng sodiq">самый преданный</span> читатель в этом месяце!</p>
<p>Амина <span class="cn-word" data-pos="verb" data-tr="hayron qoldi">удивилась</span> и <span class="cn-word" data-pos="verb" data-tr="rahmat aytdi">поблагодарила</span> библиотекаря. Она вышла из библиотеки с новой книгой и большой <span class="cn-word" data-pos="adj" data-tr="mamnun">довольной</span> улыбкой.</p>''',
        "questions": [
            {
                "text": "Почему Амина волновалась, придя в библиотеку?",
                "choices": ["Она забыла книгу дома", "Она вернула книгу с опозданием", "Библиотека была закрыта"],
                "answer": 1,
                "explanation": "\"Я должна была вернуть книгу ещё вчера\" deb uzr soʻraydi.",
            },
            {
                "text": "Как библиотекарь отреагировала на опоздание Амины?",
                "choices": ["Она рассердилась", "Она не стала брать штраф, потому что Амина много читает", "Она запретила брать новые книги"],
                "answer": 1,
                "explanation": "\"Не волнуйтесь насчёт штрафа — вы наш самый преданный читатель\" deydi.",
            },
            {
                "text": "Что взяла Амина из библиотеки в конце?",
                "choices": ["Ничего не взяла", "Вторую часть той же истории", "Журнал"],
                "answer": 1,
                "explanation": "\"Вот вторая часть этой же истории\" deb beriladi.",
            },
        ],
    },
    {
        "title":   "На почте",
        "summary": "Jasur pochtadan opasiga posilka joʻnatayotib xato bilan oʻz manzilini yozib qoʻyadi, lekin xodim buni vaqtida payqab qoladi.",
        "order":   12,
        "grammar": [
            {
                "pattern":  "Сколько это будет стоить?",
                "meaning":  "Bu qancha turadi? — narx soʻrash iborasi.",
                "examples": ["Сколько это будет стоить?", "Сколько будет стоить доставка?"],
            },
            {
                "pattern":  "Нужно + infinitiv",
                "meaning":  "... qilish kerak — zaruriyatni bildiruvchi konstruksiya.",
                "examples": ["Нужно заполнить форму.", "Нужно прийти пораньше."],
            },
            {
                "pattern":  "Подождите, пожалуйста",
                "meaning":  "Iltimos, kuting — muloyim soʻrov iborasi.",
                "examples": ["Подождите, пожалуйста, минуту.", "Подождите, пожалуйста, здесь."],
            },
        ],
        "body": '''<p>Жасур пришёл на почту, чтобы <span class="cn-word" data-pos="verb" data-tr="joʻnatmoq">отправить</span> <span class="cn-word" data-tr="posilka">посылку</span> своей сестре в другой город.</p>
<p>— Здравствуйте! Мне нужно отправить эту коробку, — сказал он <span class="cn-word" data-tr="pochta xodimi">сотруднику</span>.</p>
<p>— Хорошо. <strong>Сколько это будет стоить</strong>, зависит от веса. Давайте <span class="cn-word" data-pos="verb" data-tr="oʻlchaylik">взвесим</span>.</p>
<p>Сотрудник положил коробку на весы.</p>
<p>— Это будет пятнадцать тысяч сум. <strong>Нужно</strong> заполнить эту форму с адресом.</p>
<p>Жасур быстро <span class="cn-word" data-pos="verb" data-tr="toʻldirdi">заполнил</span> форму, но по ошибке написал свой собственный адрес вместо адреса сестры.</p>
<p>— <strong>Подождите, пожалуйста</strong>, — сказал сотрудник, <span class="cn-word" data-pos="verb" data-tr="tekshirib koʻrib">проверяя</span> форму. — Кажется, здесь ваш адрес, а не адрес получателя.</p>
<p>Жасур <span class="cn-word" data-pos="verb" data-tr="kuldi">рассмеялся</span> над своей <span class="cn-word" data-pos="adj" data-tr="tarqoq">невнимательностью</span> и быстро <span class="cn-word" data-pos="verb" data-tr="tuzatdi">исправил</span> ошибку.</p>
<p>— Спасибо, что заметили! Иначе посылка вернулась бы ко мне же!</p>
<p>— Такое часто <span class="cn-word" data-pos="verb" data-tr="sodir boʻladi">случается</span>, — <span class="cn-word" data-pos="verb" data-tr="tinchlantirdi">успокоил</span> его сотрудник. — Через три дня посылка будет у вашей сестры.</p>''',
        "questions": [
            {
                "text": "Что хотел сделать Жасур на почте?",
                "choices": ["Купить марки", "Отправить посылку сестре", "Получить письмо"],
                "answer": 1,
                "explanation": "\"Мне нужно отправить эту коробку\" deb aytadi — opasiga posilka joʻnatmoqchi edi.",
            },
            {
                "text": "Какую ошибку совершил Жасур при заполнении формы?",
                "choices": ["Написал неправильный вес", "Написал свой адрес вместо адреса сестры", "Забыл имя сестры"],
                "answer": 1,
                "explanation": "\"Здесь ваш адрес, а не адрес получателя\" deb xodim payqaydi.",
            },
            {
                "text": "Через сколько дней посылка должна дойти до сестры Жасура?",
                "choices": ["Через один день", "Через три дня", "Через неделю"],
                "answer": 1,
                "explanation": "\"Через три дня посылка будет у вашей сестры\" deyiladi.",
            },
        ],
    },
    {
        "title":   "Урок плавания",
        "summary": "Kamron birinchi suzish darsida suvdan qoʻrqadi, ammo murabbiy yordamida qoʻrquvini yengib, suzishni oʻrganadi.",
        "order":   13,
        "grammar": [
            {
                "pattern":  "Не бойся / не бойтесь",
                "meaning":  "Qoʻrqma / qoʻrqmang — tinchlantirish uchun buyruq shakli.",
                "examples": ["Не бойся, всё будет хорошо.", "Не бойтесь, я рядом."],
            },
            {
                "pattern":  "Я не умею + infinitiv",
                "meaning":  "Men ... qila olmayman — koʻnikma yoʻqligini bildirish.",
                "examples": ["Я не умею плавать.", "Я не умею готовить."],
            },
            {
                "pattern":  "У тебя получается!",
                "meaning":  "Senda chiqyapti! — ragʻbatlantirish undovi.",
                "examples": ["У тебя получается!", "Смотри, у тебя уже получается!"],
            },
        ],
        "body": '''<p>Камрон впервые пришёл на <span class="cn-word" data-tr="suzish darsi">урок плавания</span>. Он стоял у бассейна и <span class="cn-word" data-pos="verb" data-tr="qoʻrqardi">боялся</span> зайти в воду.</p>
<p>— <strong>Я не умею</strong> плавать, — <span class="cn-word" data-pos="verb" data-tr="tan oldi">признался</span> он тренеру.</p>
<p>— <strong>Не бойся</strong>, — <span class="cn-word" data-pos="verb" data-tr="jilmayib qoʻydi">улыбнулся</span> тренер. — Сегодня мы просто научимся держаться на воде.</p>
<p>Камрон <span class="cn-word" data-pos="adv" data-tr="asta-sekin">медленно</span> зашёл в воду. Она была <span class="cn-word" data-pos="adj" data-tr="iliq">тёплой</span>, и он немного <span class="cn-word" data-pos="verb" data-tr="tinchlandi">успокоился</span>.</p>
<p>— Теперь ляг на спину и <span class="cn-word" data-pos="verb" data-tr="dam ol">расслабься</span>. Я буду держать тебя, — сказал тренер.</p>
<p>Камрон <span class="cn-word" data-pos="verb" data-tr="qildi">сделал</span>, как сказал тренер, и вдруг понял, что вода сама <span class="cn-word" data-pos="verb" data-tr="ushlab turibdi">держит</span> его тело.</p>
<p>— <strong>У тебя получается!</strong> — <span class="cn-word" data-pos="verb" data-tr="baqirdi">закричал</span> тренер. — Ты плывёшь!</p>
<p>Камрон <span class="cn-word" data-pos="verb" data-tr="kuldi">рассмеялся</span> от радости. Страх <span class="cn-word" data-pos="verb" data-tr="yoʻqoldi">исчез</span>, и он почувствовал себя <span class="cn-word" data-pos="adj" data-tr="jasur">смелым</span>.</p>
<p>— Спасибо! Теперь я хочу прийти на урок ещё раз! — сказал он, выходя из бассейна с большой улыбкой.</p>''',
        "questions": [
            {
                "text": "Почему Камрон боялся заходить в бассейн?",
                "choices": ["Вода была холодной", "Он не умел плавать", "Бассейн был закрыт"],
                "answer": 1,
                "explanation": "\"Я не умею плавать\" deb tan oladi.",
            },
            {
                "text": "Что сказал тренер, чтобы успокоить Камрона?",
                "choices": ["Не бойся, сегодня мы просто научимся держаться на воде", "Плавать очень легко, попробуй сам", "Приходи в другой раз"],
                "answer": 0,
                "explanation": "\"Не бойся... сегодня мы просто научимся держаться на воде\" deydi.",
            },
            {
                "text": "Что почувствовал Камрон после урока?",
                "choices": ["Он всё ещё боялся воды", "Страх исчез, и он почувствовал себя смелым", "Он решил больше не приходить"],
                "answer": 1,
                "explanation": "\"Страх исчез, и он почувствовал себя смелым\" deyiladi.",
            },
        ],
    },
    {
        "title":   "Новый телефон",
        "summary": "Elmira doʻkonda yangi telefon tanlashda texnik xususiyatlarni tushunmay, oxiri rangiga qarab tanlaydi va natijadan mamnun boʻladi.",
        "order":   14,
        "grammar": [
            {
                "pattern":  "Какой ... вы посоветуете?",
                "meaning":  "Qaysi ...ni tavsiya qilasiz? — maslahat soʻrash konstruksiyasi.",
                "examples": ["Какой телефон вы посоветуете?", "Какую книгу вы посоветуете?"],
            },
            {
                "pattern":  "Мне важно, чтобы ...",
                "meaning":  "Menga ... muhim — talab yoki istakni bildirish.",
                "examples": ["Мне важно, чтобы телефон был быстрым.", "Мне важно, чтобы вы пришли вовремя."],
            },
            {
                "pattern":  "Я возьму ...",
                "meaning":  "Men ...ni olaman — tanlovni bildirish.",
                "examples": ["Я возьму этот телефон.", "Я возьму синий цвет."],
            },
        ],
        "body": '''<p>Эльмира пришла в магазин <span class="cn-word" data-tr="elektronika">электроники</span>, чтобы купить новый телефон.</p>
<p>— Здравствуйте! <strong>Какой</strong> телефон вы <strong>посоветуете</strong>? — спросила она продавца.</p>
<p>— У нас много моделей. Расскажите, что для вас важно?</p>
<p>— <strong>Мне важно, чтобы</strong> у телефона была хорошая <span class="cn-word" data-tr="kamera">камера</span> и большая <span class="cn-word" data-tr="xotira">память</span>.</p>
<p>Продавец <span class="cn-word" data-pos="verb" data-tr="koʻrsatdi">показал</span> ей три модели и долго <span class="cn-word" data-pos="verb" data-tr="tushuntirdi">объяснял</span> технические <span class="cn-word" data-tr="xususiyatlar">характеристики</span> каждой.</p>
<p>Эльмира <span class="cn-word" data-pos="verb" data-tr="tinglardi">слушала</span> внимательно, но, <span class="cn-word" data-pos="adj" data-tr="halol">честно</span> говоря, почти ничего не поняла из цифр и терминов.</p>
<p>— А какой из них... <span class="cn-word" data-pos="adj" data-tr="chiroyli">красивее</span>? — вдруг спросила она.</p>
<p>Продавец <span class="cn-word" data-pos="verb" data-tr="kuldi">рассмеялся</span>. — Вот этот, синий, самый популярный по дизайну.</p>
<p>— Отлично! <strong>Я возьму</strong> его, — <span class="cn-word" data-pos="verb" data-tr="qaror qildi">решила</span> Эльмира.</p>
<p>Дома она была очень <span class="cn-word" data-pos="adj" data-tr="mamnun">довольна</span> — и камера, и память оказались отличными. Иногда лучший выбор делается <span class="cn-word" data-pos="adv" data-tr="yurak bilan">сердцем</span>, а не только цифрами.</p>''',
        "questions": [
            {
                "text": "Что было важно для Эльмиры при выборе телефона?",
                "choices": ["Цена и вес", "Хорошая камера и большая память", "Только цвет"],
                "answer": 1,
                "explanation": "\"Мне важно, чтобы у телефона была хорошая камера и большая память\" deydi.",
            },
            {
                "text": "Почему Эльмира в итоге выбрала синий телефон?",
                "choices": ["Потому что он был самым дешёвым", "Потому что он показался ей самым красивым", "Потому что продавец настоял"],
                "answer": 1,
                "explanation": "\"А какой из них красивее?\" deb soʻraydi va shu asosda tanlaydi.",
            },
            {
                "text": "Осталась ли Эльмира довольна своим выбором дома?",
                "choices": ["Нет, телефон оказался плохим", "Да, камера и память оказались отличными", "Она сразу вернула телефон"],
                "answer": 1,
                "explanation": "\"Дома она была очень довольна — и камера, и память оказались отличными\" deyiladi.",
            },
        ],
    },
    {
        "title":   "Пикник у реки",
        "summary": "Farux va doʻstlari daryo boʻyida piknik qilib, kutilmagan katta baliq tutib olishadi va uni birga pishirishadi.",
        "order":   15,
        "grammar": [
            {
                "pattern":  "Пойдём + infinitiv",
                "meaning":  "Keling, ... qilamiz — birgalikda taklif qilish konstruksiyasi.",
                "examples": ["Пойдём гулять!", "Пойдём ловить рыбу!"],
            },
            {
                "pattern":  "Осторожно!",
                "meaning":  "Ehtiyot boʻling! — ogohlantirish undovi.",
                "examples": ["Осторожно, там горячо!", "Осторожно, скользко!"],
            },
            {
                "pattern":  "Получилось!",
                "meaning":  "Chiqdi! Muvaffaqiyat boʻldi! — natijadan xursandchilikni bildiruvchi undov.",
                "examples": ["Получилось! Мы сделали это!", "Наконец получилось!"],
            },
        ],
        "body": '''<p>В субботу утром Фарух и его друзья <span class="cn-word" data-pos="verb" data-tr="qaror qilishdi">решили</span> устроить <span class="cn-word" data-tr="piknik">пикник</span> у реки.</p>
<p>— <strong>Пойдём</strong> ловить рыбу! — <span class="cn-word" data-pos="verb" data-tr="taklif qildi">предложил</span> Фарух, доставая удочки.</p>
<p>Друзья <span class="cn-word" data-pos="verb" data-tr="oʻtirishdi">сели</span> на берегу и стали <span class="cn-word" data-pos="verb" data-tr="kutishdi">ждать</span>.</p>
<p>Через несколько минут удочка Фаруха вдруг <span class="cn-word" data-pos="verb" data-tr="tortila boshladi">задёргалась</span>.</p>
<p>— <strong>Осторожно!</strong> Там что-то <span class="cn-word" data-pos="adj" data-tr="katta">большое</span>! — <span class="cn-word" data-pos="verb" data-tr="baqirdi">закричал</span> его друг Аброр.</p>
<p>Фарух <span class="cn-word" data-pos="verb" data-tr="kuch bilan tortdi">потянул</span> удочку изо всех сил. Все друзья <span class="cn-word" data-pos="verb" data-tr="yordamlashdi">помогали</span> ему.</p>
<p>— <strong>Получилось!</strong> — <span class="cn-word" data-pos="verb" data-tr="quvonib ketdi">обрадовался</span> Фарух, когда огромная рыба наконец оказалась на берегу.</p>
<p>Все <span class="cn-word" data-pos="verb" data-tr="hayron qolib qarashdi">смотрели</span> на рыбу с удивлением — она была самой большой, которую они когда-либо видели.</p>
<p>— Давайте <span class="cn-word" data-pos="verb" data-tr="pishiramiz">приготовим</span> её прямо здесь, на костре! — <span class="cn-word" data-pos="verb" data-tr="taklif qildi">предложила</span> Дилноза.</p>
<p>Вечером друзья ели <span class="cn-word" data-pos="adj" data-tr="mazali">вкусную</span> рыбу и смеялись, вспоминая, как Фарух чуть не упал в реку во время борьбы с рыбой.</p>''',
        "questions": [
            {
                "text": "Что предложил сделать Фарух в субботу утром?",
                "choices": ["Пойти в кино", "Устроить пикник и ловить рыбу", "Остаться дома"],
                "answer": 1,
                "explanation": "\"Пойдём ловить рыбу!\" deb taklif qiladi.",
            },
            {
                "text": "Что произошло, когда удочка Фаруха задёргалась?",
                "choices": ["Удочка сломалась", "Фарух поймал очень большую рыбу", "Ничего не поймали"],
                "answer": 1,
                "explanation": "\"Получилось! ...огромная рыба наконец оказалась на берегу\" deyiladi.",
            },
            {
                "text": "Что друзья решили сделать с пойманной рыбой?",
                "choices": ["Отпустить её обратно в реку", "Приготовить её на костре", "Продать её"],
                "answer": 1,
                "explanation": "\"Давайте приготовим её прямо здесь, на костре!\" deb taklif qilinadi.",
            },
        ],
    },
]
