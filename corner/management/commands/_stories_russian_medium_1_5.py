# Orta rus hikoyalari — stories 1-5 (Claude-authored, pre-intermediate/intermediate B1 level).
# Import: python manage.py import_corner corner/management/commands/_stories_russian_medium_1_5.py --author=<AUTHOR>

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
        "title":   "Потерянный кошелёк",
        "summary": "Timur koʻchada yoʻqolgan hamyonni topib, egasiga qaytarish yoki qaytarmaslik haqidagi ichki kurashni yengib oʻtadi.",
        "order":   1,
        "grammar": [
            {
                "pattern":  "найти (pf)",
                "meaning":  "topib olmoq — bir martalik, tugallangan harakatni bildiruvchi tugallangan (pf) fe'l shakli.",
                "examples": ["Тимур нашёл кошелёк на тротуаре.", "Наконец мы нашли дорогу домой."],
            },
            {
                "pattern":  "оказаться + instr.",
                "meaning":  "...boʻlib chiqdi — kutilmagan haqiqat ochilganda ishlatiladigan konstruksiya.",
                "examples": ["Он оказался старым другом.", "Кошелёк оказался очень тяжёлым."],
            },
            {
                "pattern":  "Если бы ..., я бы ...",
                "meaning":  "Agar ... boʻlganda, men ... qilardim — real boʻlmagan, shartli holatni bildiruvchi konstruksiya.",
                "examples": ["Если бы я потерял кошелёк, я бы очень расстроился.", "Если бы у меня было время, я бы помог тебе."],
            },
        ],
        "body": '''<p>Тимур <span class="cn-word" data-pos="verb" data-tr="ketayotgan edi">шёл</span> домой поздно вечером, когда вдруг <span class="cn-word" data-pos="verb" data-tr="payqab qoldi">заметил</span> на <span class="cn-word" data-tr="yoʻlak">тротуаре</span> что-то тёмное. Это был <span class="cn-word" data-tr="hamyon">кошелёк</span>, потерянный кем-то. Тимур открыл его, и содержимое <strong>оказалось</strong> неожиданным: внутри было много денег и <span class="cn-word" data-tr="hujjatlar">документы</span> на имя пожилой женщины.</p>
<p>Первая мысль, которая пришла ему в голову, была простой: «Никто не <span class="cn-word" data-pos="verb" data-tr="bilib qoladi">узнает</span>, если я оставлю деньги себе». Но потом он <span class="cn-word" data-pos="verb" data-tr="oʻyladi">подумал</span> о женщине, которая, наверное, сейчас дома <span class="cn-word" data-pos="verb" data-tr="tashvishlanmoqda">переживает</span> из-за потери.</p>
<p>— <strong>Если бы</strong> я потерял кошелёк, я <strong>бы</strong> очень хотел, чтобы его кто-то вернул, — сказал он сам себе.</p>
<p>По адресу, указанному в документах, Тимур <strong>нашёл</strong> дом пожилой женщины. Она открыла дверь и, увидев кошелёк, <span class="cn-word" data-pos="verb" data-tr="yigʻlab yubordi">расплакалась</span> от радости.</p>
<p>— Сынок, я весь вечер <span class="cn-word" data-pos="verb" data-tr="qidirdim">искала</span> этот кошелёк! Там были деньги на <span class="cn-word" data-tr="dori-darmon">лекарства</span> для моего мужа. Спасибо тебе огромное!</p>
<p>Она <span class="cn-word" data-pos="verb" data-tr="taklif qildi">предложила</span> ему часть денег в благодарность, но Тимур <span class="cn-word" data-pos="verb" data-tr="rad etdi">отказался</span>.</p>
<p>— Мне не нужна <span class="cn-word" data-tr="mukofot">награда</span>. Я просто рад, что смог помочь, — ответил он с улыбкой.</p>
<p>Женщина долго смотрела ему вслед и думала, что в этом городе, <span class="cn-word" data-tr="yaxshiyamki">к счастью</span>, всё ещё <span class="cn-word" data-pos="verb" data-tr="uchrab turadi">встречаются</span> такие честные люди.</p>''',
        "questions": [
            {
                "text": "Что Тимур нашёл на тротуаре вечером?",
                "choices": ["Телефон", "Кошелёк с деньгами и документами", "Ключи"],
                "answer": 1,
                "explanation": "Matnda \"внутри было много денег и документы на имя пожилой женщины\" deyiladi.",
            },
            {
                "text": "Почему Тимур решил вернуть кошелёк, а не оставить деньги себе?",
                "choices": ["Потому что он подумал о переживаниях хозяйки кошелька", "Потому что кошелёк был пустой", "Потому что за ним следила полиция"],
                "answer": 0,
                "explanation": "U \"подумал о женщине, которая... переживает из-за потери\" deb aytiladi.",
            },
            {
                "text": "Как Тимур отреагировал, когда женщина предложила ему деньги в благодарность?",
                "choices": ["Он взял половину денег", "Он отказался, сказав, что рад был помочь", "Он попросил больше денег"],
                "answer": 1,
                "explanation": "\"Тимур отказался... Мне не нужна награда\" deb javob beradi.",
            },
        ],
    },
    {
        "title":   "Собеседование",
        "summary": "Dilorom orzudagi ish uchun suhbatga tayyorlanib, hayajonini yengib, kutilmagan savolga hazil bilan javob beradi va ishga qabul qilinadi.",
        "order":   2,
        "grammar": [
            {
                "pattern":  "готовиться (impf) / подготовиться (pf)",
                "meaning":  "tayyorgarlik koʻrmoq (davomiy) / tayyorgarlik koʻrib boʻlmoq (yakunlangan) — aspekt jufti.",
                "examples": ["Она готовилась к экзамену весь день.", "Наконец она подготовилась и была готова."],
            },
            {
                "pattern":  "волноваться",
                "meaning":  "hayajonlanmoq, tashvishlanmoq — oʻzlik nisbatidagi (refleksiv) fe'l.",
                "examples": ["Не волнуйся, всё будет хорошо.", "Перед экзаменом я всегда волнуюсь."],
            },
            {
                "pattern":  "..., чтобы + infinitiv",
                "meaning":  "...uchun, ...maqsadida — maqsad ergash gapini bildiruvchi konstruksiya.",
                "examples": ["Она дышала глубоко, чтобы успокоиться.", "Я учу русский, чтобы найти хорошую работу."],
            },
        ],
        "body": '''<p>Дилором <strong>готовилась</strong> к собеседованию всю неделю. Это была её работа <span class="cn-word" data-pos="adj" data-tr="orzudagi">мечты</span> — <span class="cn-word" data-tr="marketing boʻyicha mutaxassis">специалист по маркетингу</span> в известной компании.</p>
<p>Утром в день собеседования она сильно <strong>волновалась</strong>. Руки <span class="cn-word" data-pos="verb" data-tr="titrayotgan edi">дрожали</span>, а сердце <span class="cn-word" data-pos="verb" data-tr="tez urardi">билось</span> очень быстро.</p>
<p>— Дыши глубоко, — сказала она себе, <strong>чтобы</strong> <span class="cn-word" data-pos="verb" data-tr="tinchlanmoq">успокоиться</span>.</p>
<p>В офисе её встретил менеджер по имени Рустам.</p>
<p>— Здравствуйте! Расскажите немного о себе, — <span class="cn-word" data-pos="verb" data-tr="soʻradi">попросил</span> он.</p>
<p>Дилором <span class="cn-word" data-pos="verb" data-tr="aytib berdi">рассказала</span> о своём образовании и <span class="cn-word" data-tr="tajriba">опыте</span> работы. Всё шло <span class="cn-word" data-pos="adv" data-tr="silliq">гладко</span>, пока Рустам вдруг не задал <span class="cn-word" data-pos="adj" data-tr="kutilmagan">неожиданный</span> вопрос:</p>
<p>— Если бы вы были фруктом, каким фруктом вы были бы и почему?</p>
<p>Дилором на секунду <span class="cn-word" data-pos="verb" data-tr="esankirab qoldi">растерялась</span>, но потом улыбнулась.</p>
<p>— Я была бы <span class="cn-word" data-tr="anor">гранатом</span>. Снаружи я выгляжу <span class="cn-word" data-pos="adj" data-tr="qattiq">твёрдой</span> и <span class="cn-word" data-pos="adj" data-tr="jiddiy">серьёзной</span>, но внутри у меня много энергии и идей, как <span class="cn-word" data-tr="donalar">зёрна</span> граната.</p>
<p>Рустам <span class="cn-word" data-pos="verb" data-tr="kuldi">рассмеялся</span> и сказал, что это лучший ответ, который он слышал за весь месяц.</p>
<p>Через два дня Дилором <span class="cn-word" data-pos="verb" data-tr="oldi">получила</span> звонок: её <span class="cn-word" data-pos="verb" data-tr="qabul qilishdi">приняли</span> на работу.</p>
<p>— Оказывается, — думала она по дороге домой, — иногда не нужно бояться необычных вопросов. Нужно просто быть собой.</p>''',
        "questions": [
            {
                "text": "Почему Дилором сильно волновалась утром перед собеседованием?",
                "choices": ["Потому что она проспала", "Потому что это была работа её мечты", "Потому что не знала адрес офиса"],
                "answer": 1,
                "explanation": "\"Это была её работа мечты\" deb aytiladi — shuning uchun juda hayajonlangan.",
            },
            {
                "text": "Какой неожиданный вопрос задал Рустам?",
                "choices": ["О зарплате", "Каким фруктом она была бы", "О её хобби"],
                "answer": 1,
                "explanation": "\"Если бы вы были фруктом, каким фруктом вы были бы и почему?\" deb soʻraydi.",
            },
            {
                "text": "Что поняла Дилором после собеседования?",
                "choices": ["Что нужно всегда бояться необычных вопросов", "Что не нужно бояться необычных вопросов и нужно быть собой", "Что собеседования всегда проходят легко"],
                "answer": 1,
                "explanation": "\"Не нужно бояться необычных вопросов. Нужно просто быть собой\" deb oʻylaydi.",
            },
        ],
    },
    {
        "title":   "Сюрприз для мамы",
        "summary": "Malika va Sardor onalarining tugʻilgan kuniga nonushta tayyorlashga urinib, oshxonani tartibsiz qilib qoʻyishadi, ammo ona buni eng yaxshi sюрприz deb ataydi.",
        "order":   3,
        "grammar": [
            {
                "pattern":  "успеть / успевать",
                "meaning":  "ulgurmoq — vaqtida biror ishni bajarib ulgurish (tugallangan/tugallanmagan jufti).",
                "examples": ["Мы успели купить билеты.", "Не волнуйся, ты ещё успеешь."],
            },
            {
                "pattern":  "чуть не + oʻtgan zamon fe'li",
                "meaning":  "deyarli ... boʻlib qolmoq — biror narsa sal boʻlmasa sodir boʻlishiga ishora qiluvchi konstruksiya.",
                "examples": ["Она чуть не упала.", "Я чуть не опоздал на поезд."],
            },
            {
                "pattern":  "..., пока ... не ...",
                "meaning":  "...gacha, ... boʻlmaguncha — salbiy shakldagi vaqt ergash gapi.",
                "examples": ["Подожди, пока я не приду.", "Он молчал, пока все не ушли."],
            },
        ],
        "body": '''<p>Малика и её младший брат Сардор <span class="cn-word" data-pos="verb" data-tr="uygʻonishdi">проснулись</span> очень рано, чтобы <strong>успеть</strong> приготовить завтрак маме на день рождения.</p>
<p>— Тише, <strong>пока</strong> мама <strong>не</strong> проснулась! — <span class="cn-word" data-pos="verb" data-tr="shivirladi">прошептала</span> Малика.</p>
<p>Они <span class="cn-word" data-pos="verb" data-tr="chiqarishdi">достали</span> сковороду и решили приготовить блины. Но Сардор случайно <span class="cn-word" data-pos="verb" data-tr="toʻkib yubordi">рассыпал</span> муку по всей кухне, а Малика <strong>чуть не</strong> <span class="cn-word" data-pos="verb" data-tr="kuydirib yubordi">сожгла</span> первый блин.</p>
<p>— Ой-ой-ой, дым! — <span class="cn-word" data-pos="verb" data-tr="baqirdi">закричал</span> Сардор, размахивая полотенцем перед <span class="cn-word" data-tr="tutun signalizatsiyasi">пожарным датчиком</span>.</p>
<p>Именно в этот момент на кухню <span class="cn-word" data-pos="verb" data-tr="kirib keldi">вошла</span> мама, разбуженная шумом.</p>
<p>— Что здесь происходит? — <span class="cn-word" data-pos="verb" data-tr="soʻradi">спросила</span> она, глядя на кухню, всю в муке и дыме.</p>
<p>Малика и Сардор, <span class="cn-word" data-pos="adj" data-tr="uyalgan holda">смущённые</span>, посмотрели друг на друга.</p>
<p>— Мы хотели сделать тебе сюрприз... — <span class="cn-word" data-pos="verb" data-tr="tan oldi">призналась</span> Малика.</p>
<p>Мама <span class="cn-word" data-pos="verb" data-tr="kulib yubordi">рассмеялась</span> и <span class="cn-word" data-pos="verb" data-tr="quchoqladi">обняла</span> обоих детей.</p>
<p>— Это лучший сюрприз, который у меня когда-либо был, даже с дымом на кухне!</p>
<p>Втроём они <span class="cn-word" data-pos="verb" data-tr="tozalashdi">убрали</span> муку и вместе <span class="cn-word" data-pos="verb" data-tr="pishirishdi">испекли</span> новые, уже не подгоревшие блины. Они завтракали и смеялись, вспоминая <span class="cn-word" data-pos="adj" data-tr="tartibsiz">хаотичное</span> утро.</p>
<p>— Не важно, что что-то <span class="cn-word" data-pos="verb" data-tr="notoʻgʻri ketdi">пошло не так</span>, — сказала мама. — Важно, что вы обо мне <span class="cn-word" data-pos="verb" data-tr="oʻylashgan">думали</span> с самого утра.</p>''',
        "questions": [
            {
                "text": "Почему дети хотели встать очень рано?",
                "choices": ["Чтобы успеть приготовить завтрак маме до того, как она проснётся", "Чтобы пойти в школу", "Чтобы посмотреть мультфильмы"],
                "answer": 0,
                "explanation": "\"проснулись очень рано, чтобы успеть приготовить завтрак маме\" deyiladi.",
            },
            {
                "text": "Что произошло, пока дети готовили завтрак?",
                "choices": ["Всё прошло идеально, мама ничего не узнала", "Сардор рассыпал муку, а Малика чуть не сожгла блин", "Дети быстро легли обратно спать"],
                "answer": 1,
                "explanation": "\"Сардор случайно рассыпал муку... Малика чуть не сожгла первый блин\" deyiladi.",
            },
            {
                "text": "Как мама отреагировала, увидев кухню в муке и дыме?",
                "choices": ["Она рассердилась на детей", "Она рассмеялась и сказала, что это лучший сюрприз", "Она ушла на работу, не позавтракав"],
                "answer": 1,
                "explanation": "\"Мама рассмеялась... Это лучший сюрприз, который у меня когда-либо был\" deydi.",
            },
        ],
    },
    {
        "title":   "Заблудились в лесу",
        "summary": "Elyor, Kamila va Sherzod tog' sayohatida adashib qolishadi, biroq Sherzodning bobosidan qolgan bir maslahati ularga yoʻl topishga yordam beradi.",
        "order":   4,
        "grammar": [
            {
                "pattern":  "заблудиться",
                "meaning":  "adashib qolmoq — oʻzlik nisbatidagi tugallangan fe'l.",
                "examples": ["Мы заблудились в лесу.", "Туристы иногда заблуждаются в горах."],
            },
            {
                "pattern":  "стало + qisqa sifat",
                "meaning":  "... boʻlib qoldi — shaxssiz holat/oʻzgarishni bildiruvchi konstruksiya (темно, страшно, холодно kabi soʻzlar bilan).",
                "examples": ["Стало темно.", "Ему стало страшно."],
            },
            {
                "pattern":  "тот, кто ...",
                "meaning":  "... kishi, kim — biror shaxsga ishora qiluvchi nisbiy gap.",
                "examples": ["Тот, кто помнит дорогу, пусть идёт первым.", "Я благодарен тому, кто мне помог."],
            },
        ],
        "body": '''<p>Элёр, Камила и Шерзод <span class="cn-word" data-pos="verb" data-tr="sayohatga chiqishdi">отправились</span> в поход в горы. Они <span class="cn-word" data-pos="verb" data-tr="yurishdi">шли</span> по <span class="cn-word" data-tr="soʻqmoq">тропинке</span> несколько часов, наслаждаясь свежим воздухом и <span class="cn-word" data-pos="adj" data-tr="ajoyib">великолепными</span> видами.</p>
<p>Но ближе к вечеру они вдруг поняли, что <strong>заблудились</strong>. Тропинка куда-то <span class="cn-word" data-pos="verb" data-tr="yoʻqoldi">исчезла</span>, а вокруг были только деревья.</p>
<p>— Что теперь делать? — <span class="cn-word" data-pos="adv" data-tr="tashvishlangan holda">взволнованно</span> спросила Камила, когда <strong>стало</strong> темно.</p>
<p>Шерзод <span class="cn-word" data-pos="verb" data-tr="chuqur nafas oldi">вздохнул</span> и <span class="cn-word" data-pos="verb" data-tr="eslab qoldi">вспомнил</span>, чему учил его дедушка в детстве.</p>
<p>— Мох <span class="cn-word" data-pos="verb" data-tr="oʻsadi">растёт</span> на <span class="cn-word" data-tr="shimoliy">северной</span> стороне деревьев. Если мы будем идти в одном направлении, то <span class="cn-word" data-pos="adv" data-tr="ertami-kechmi">рано или поздно</span> найдём дорогу.</p>
<p>— <strong>Тот, кто</strong> помнит такие вещи, должен идти первым, — с облегчением сказала Камила.</p>
<p>Они <span class="cn-word" data-pos="verb" data-tr="ergashishdi">последовали</span> за Шерзодом, внимательно <span class="cn-word" data-pos="verb" data-tr="kuzatib borishdi">наблюдая</span> за мхом на деревьях. Через час они <span class="cn-word" data-pos="verb" data-tr="eshitishdi">услышали</span> шум машин — это была дорога!</p>
<p>— Мы <span class="cn-word" data-pos="verb" data-tr="qutulib chiqdik">выбрались</span>! — <span class="cn-word" data-pos="verb" data-tr="quvonib ketishdi">обрадовались</span> все трое.</p>
<p>С тех пор Элёр и Камила всегда <span class="cn-word" data-pos="verb" data-tr="birga olishadi">берут</span> Шерзода с собой в походы — просто на всякий случай.</p>''',
        "questions": [
            {
                "text": "Что поняли друзья ближе к вечеру?",
                "choices": ["Что они заблудились в лесу", "Что дождь начался", "Что поход закончился слишком рано"],
                "answer": 0,
                "explanation": "\"Они вдруг поняли, что заблудились\" deb aniq aytiladi.",
            },
            {
                "text": "Что вспомнил Шерзод, чтобы найти дорогу?",
                "choices": ["Совет дедушки о мхе на деревьях", "Карту в телефоне", "Слова учителя географии"],
                "answer": 0,
                "explanation": "\"Мох растёт на северной стороне деревьев\" — buni bobosidan bilib olgan edi.",
            },
            {
                "text": "Как друзья поняли, что вышли к дороге?",
                "choices": ["Они увидели указатель", "Они услышали шум машин", "Позвонили спасатели"],
                "answer": 1,
                "explanation": "\"Через час они услышали шум машин — это была дорога!\" deyiladi.",
            },
        ],
    },
    {
        "title":   "Соседи сверху",
        "summary": "Nargiza tepadagi qoʻshnilarning shovqinidan shikoyat qilgani boradi, ammo bu oila qizining tugʻilgan kuniga tayyorgarlik koʻrayotganini bilib, ular bilan doʻstlashib qoladi.",
        "order":   5,
        "grammar": [
            {
                "pattern":  "переехать / переезжать",
                "meaning":  "koʻchib oʻtmoq — tugallangan/tugallanmagan fe'l jufti, yashash joyini oʻzgartirish maʼnosida.",
                "examples": ["Новая семья переехала в квартиру наверху.", "Мы переезжаем в новый дом каждые пять лет."],
            },
            {
                "pattern":  "не могу не + infinitiv",
                "meaning":  "...maslikka chidayolmayman, albatta ... qilaman — ikkilangan inkor orqali kuchli tasdiqni bildiruvchi konstruksiya.",
                "examples": ["Я не могу не сказать, что мне это нравится.", "Не могу не согласиться с тобой."],
            },
            {
                "pattern":  "оказалось, что ...",
                "meaning":  "maʼlum boʻldiki... — kutilmagan haqiqat ochilganda ishlatiladigan konstruksiya.",
                "examples": ["Оказалось, что стены очень тонкие.", "Оказалось, что мы соседи по школе."],
            },
        ],
        "body": '''<p>Наргиза уже неделю не могла нормально спать по ночам: соседи сверху постоянно <span class="cn-word" data-pos="verb" data-tr="shovqin qilishardi">шумели</span> — топот, музыка, <span class="cn-word" data-pos="adj" data-tr="baland">громкие</span> голоса.</p>
<p><strong>Оказалось, что</strong> новая семья недавно <strong>переехала</strong> в квартиру наверху. Наргиза <span class="cn-word" data-pos="verb" data-tr="qaror qildi">решила</span> подняться и <span class="cn-word" data-pos="verb" data-tr="shikoyat qilmoq">пожаловаться</span>.</p>
<p>Она <span class="cn-word" data-pos="verb" data-tr="qoʻngʻiroq qildi">позвонила</span> в дверь. Открыла женщина с <span class="cn-word" data-pos="adj" data-tr="uyalgan">смущённым</span> лицом.</p>
<p>— Здравствуйте, извините за беспокойство, но у вас очень <span class="cn-word" data-pos="adj" data-tr="shovqinli">шумно</span> каждый вечер, — сказала Наргиза, стараясь быть вежливой.</p>
<p>— Ой, простите нас, пожалуйста! Мы <span class="cn-word" data-pos="verb" data-tr="tayyorlanardik">готовились</span> к дню рождения дочери, — <span class="cn-word" data-pos="verb" data-tr="tushuntirdi">объяснила</span> женщина. — Мы не знали, что стены в доме такие тонкие.</p>
<p>В этот момент из комнаты <span class="cn-word" data-pos="verb" data-tr="chiqib keldi">выбежала</span> маленькая девочка.</p>
<p>— А вы придёте на мой день рождения завтра? Будет очень весело!</p>
<p>Наргиза <span class="cn-word" data-pos="verb" data-tr="jilmayib yubordi">улыбнулась</span>. <strong>Не могу не</strong> сказать, что шум ей всё ещё не нравился, но девочка была такой <span class="cn-word" data-pos="adj" data-tr="mehribon">искренней</span>, что она <span class="cn-word" data-pos="verb" data-tr="rozi boʻldi">согласилась</span>.</p>
<p>На следующий вечер Наргиза <span class="cn-word" data-pos="verb" data-tr="bordi">пришла</span> на праздник с тортом. Дети <span class="cn-word" data-pos="verb" data-tr="raqsga tushishdi">танцевали</span>, а взрослые смеялись за столом. Шум больше не <span class="cn-word" data-pos="verb" data-tr="bezovta qilmadi">беспокоил</span> её — теперь это были голоса друзей.</p>''',
        "questions": [
            {
                "text": "Почему Наргиза поднялась к соседям?",
                "choices": ["Чтобы пожаловаться на шум", "Чтобы познакомиться", "Чтобы попросить соль"],
                "answer": 0,
                "explanation": "\"Наргиза решила подняться и пожаловаться\" deb aytiladi.",
            },
            {
                "text": "Что оказалось причиной шума?",
                "choices": ["Ремонт в квартире", "Подготовка к дню рождения дочери", "Новая стиральная машина"],
                "answer": 1,
                "explanation": "\"Мы готовились к дню рождения дочери\" deb tushuntiradi.",
            },
            {
                "text": "Чем закончилась история?",
                "choices": ["Наргиза переехала в другую квартиру", "Наргиза пришла на праздник и подружилась с соседями", "Соседи извинились, но шум не прекратился"],
                "answer": 1,
                "explanation": "\"Наргиза пришла на праздник с тортом\" va shovqin endi doʻstlar ovoziga aylandi.",
            },
        ],
    },
]
