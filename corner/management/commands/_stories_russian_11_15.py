# Zamonaviy rus hikoyalari — stories 11-15 (Claude-authored, intermediate-advanced level).
# Import: python manage.py import_corner corner/management/commands/_stories_russian_11_15.py --author=<AUTHOR>

SUBJECT = {
    "name":    "Russian",
    "summary": "Rus tili: zamonaviy hikoyalar, lugʻat va grammatika bilan.",
    "icon":    "bi-translate",
    "color":   "#b91c1c",
}

COLLECTION = {
    "title":       "Zamonaviy rus hikoyalari",
    "description": "Zamonaviy rus tilida qiziqarli hikoyalar — lugʻat, grammatika, savollar va audio bilan.",
    "order":       1,
}

STORIES = [
    {
        "title":   "Ночная смена",
        "summary": "Tungi navbatchilikdagi hamshira Dilrabo qo'rqib yotgan yolg'iz bemor bilan protokoldan ortiq vaqt o'tkazadi va bu unga muhim saboq beradi.",
        "order":   11,
        "grammar": [
            {
                "pattern":  "деепричастие (-в / -я)",
                "meaning":  "Deepричастие — asosiy harakat bilan bir vaqtda yoki undan oldin sodir boʻlgan qoʻshimcha harakatni bildiradi.",
                "examples": ["Заступив на смену, она сразу поняла, что ночь будет непростой.", "Увидев его дрожащие руки, она не смогла уйти."],
            },
            {
                "pattern":  "Если бы не ..., ... бы",
                "meaning":  "Agar ... boʻlmaganida, ... boʻlmas edi (oʻtmishdagi noreal shart, sabab bildiruvchi).",
                "examples": ["Если бы не вы, я бы не сомкнул глаз.", "Если бы не помощь друга, я бы не справился."],
            },
            {
                "pattern":  "так и не + fe'l",
                "meaning":  "Oxir-oqibat ... qila olmadi/qilmadi — natijasizlikni taʼkidlaydi.",
                "examples": ["Она так и не научилась относиться к пациентам просто как к случаям.", "Он так и не позвонил."],
            },
            {
                "pattern":  "будто",
                "meaning":  "Xuddi ..., goʻyo (oʻxshatish bildiruvchi bogʻlovchi).",
                "examples": ["Он уснул, будто ребёнок, которому больше нечего бояться.", "Она молчала, будто ничего не случилось."],
            },
        ],
        "body": '''<p><span class="cn-word" data-pos="verb" data-tr="ishga kirib">Заступив</span> на <span class="cn-word" data-tr="tungi navbat">ночную смену</span>, медсестра Дилрабо сразу почувствовала, что эта ночь будет непростой. Больница была необычно <span class="cn-word" data-pos="adj" data-tr="jimjit">тихой</span>, и лишь из одной палаты доносился <span class="cn-word" data-tr="tashvishli shivir">тревожный шёпот</span>.</p>
<p>Там лежал пожилой мужчина, Акрам-ака, которого привезли накануне с сердечным приступом. Несмотря на то что его состояние уже <span class="cn-word" data-pos="verb" data-tr="barqarorlashgan edi">стабилизировалось</span>, он выглядел испуганным и одиноким.</p>
<p>— Дочка, посиди со мной немного, — <span class="cn-word" data-pos="verb" data-tr="soʻradi">попросил</span> он, когда Дилрабо зашла проверить <span class="cn-word" data-tr="asbob-uskunalar">приборы</span>.</p>
<p>По протоколу у неё было ещё пятнадцать пациентов, но, <strong>увидев</strong> его дрожащие руки, она не смогла уйти.</p>
<p>— Конечно, — сказала она, <span class="cn-word" data-pos="verb" data-tr="oʻtirib">присаживаясь</span> рядом.</p>
<p>Акрам-ака рассказал ей о своей покойной жене, о детях, которые жили далеко, и о страхе, который он <span class="cn-word" data-pos="verb" data-tr="hech qachon his qilmagan edi">никогда раньше не испытывал</span> так остро.</p>
<p>— <strong>Если бы не</strong> вы, я бы, наверное, всю ночь не сомкнул глаз от страха, — <span class="cn-word" data-pos="verb" data-tr="pichirladi">прошептал</span> он под утро.</p>
<p>Дилрабо оставалась с ним, <span class="cn-word" data-pos="verb" data-tr="tinchlantirib">успокаивая</span> его тихими словами, пока он, наконец, не уснул спокойным сном, <strong>будто</strong> ребёнок, которому больше нечего бояться.</p>
<p>Утром, сдавая смену, она <span class="cn-word" data-pos="verb" data-tr="tan oldi">призналась</span> коллеге, что за годы работы <strong>так и не</strong> научилась относиться к пациентам просто как к «случаям».</p>
<p>— И, кажется, — <span class="cn-word" data-pos="verb" data-tr="qoʻshib qoʻydi">добавила</span> она с улыбкой, — это, наверное, к лучшему.</p>
<p>Через неделю Акрам-ака <span class="cn-word" data-pos="verb" data-tr="chiqib ketdi">выписался</span> из больницы <span class="cn-word" data-pos="adj" data-tr="ancha yaxshi">значительно окрепшим</span> — врачи говорили, что спокойствие часто лечит не хуже лекарств.</p>''',
        "questions": [
            {
                "text": "Почему Дилрабо осталась с Акрамом-ака дольше, чем требовал протокол?",
                "choices": ["Начальство приказало ей это сделать", "Она увидела его дрожащие руки и не смогла уйти", "У неё не было других пациентов в ту ночь"],
                "answer": 1,
                "explanation": "\"Увидев его дрожащие руки, она не смогла уйти\" deyiladi — bu uning oʻz qarori edi.",
            },
            {
                "text": "Чего Дилрабо так и не научилась за годы работы?",
                "choices": ["Ставить уколы", "Относиться к пациентам просто как к «случаям»", "Работать в ночную смену"],
                "answer": 1,
                "explanation": "\"Так и не научилась относиться к пациентам просто как к случаям\" deb tan oladi.",
            },
            {
                "text": "Что, по мнению врачей, помогло Акраму-ака поправиться так быстро?",
                "choices": ["Новое лекарство", "Спокойствие, которое лечит не хуже лекарств", "Строгий постельный режим"],
                "answer": 1,
                "explanation": "\"Спокойствие часто лечит не хуже лекарств\" deyiladi hikoya oxirida.",
            },
        ],
    },
    {
        "title":   "Письмо в бутылке",
        "summary": "Timur qirg'oqdan o'n besh yil avval bolakay yozgan xatni topib, uni yozgan ayolni izlab topadi va bu unga unutilgan orzusini eslatadi.",
        "order":   12,
        "grammar": [
            {
                "pattern":  "деепричастие несовершенного вида (-я / -а)",
                "meaning":  "Nomukammal deepричастие — asosiy harakat bilan bir vaqtda davom etayotgan harakatni bildiradi.",
                "examples": ["Гуляя по берегу, он нашёл бутылку.", "Читая письмо, он улыбнулся."],
            },
            {
                "pattern":  "судя по всему",
                "meaning":  "Shundan koʻrinishicha, chamasi (taxmin bildiruvchi kirish soʻz birikmasi).",
                "examples": ["Судя по всему, оно пролежало здесь много лет.", "Судя по всему, дождь начнётся к вечеру."],
            },
            {
                "pattern":  "Стоило только ..., как",
                "meaning":  "Faqat ... qilish yetarli boʻldi, shu zahoti (kutilmagan tezkor natija).",
                "examples": ["Стоило только получить её номер, как сразу позвонил.", "Стоило только выйти на улицу, как начался дождь."],
            },
            {
                "pattern":  "Хотя ...",
                "meaning":  "Garchi ... boʻlsa-da (qarshi qoʻyish, ustuvor holatga qaramay).",
                "examples": ["Хотя дата на письме была пятнадцатилетней давности, он решил найти автора.", "Хотя было поздно, она позвонила бабушке."],
            },
        ],
        "body": '''<p><strong>Гуляя</strong> по <span class="cn-word" data-tr="qirgʻoq">берегу</span> моря, Тимур <span class="cn-word" data-pos="verb" data-tr="payqab qoldi">заметил</span> старую стеклянную бутылку, наполовину зарытую в песок.</p>
<p>Внутри было письмо, <span class="cn-word" data-pos="adj" data-tr="sargʻayib ketgan">пожелтевшее</span> от времени. <strong>Судя по всему</strong>, оно <span class="cn-word" data-pos="verb" data-tr="yotgan edi">пролежало</span> здесь много лет.</p>
<p>Письмо было написано детским почерком: «Меня зовут Севара, мне десять лет. Когда я вырасту, я хочу стать <span class="cn-word" data-tr="rassom">художницей</span> и нарисовать всё море целиком».</p>
<p><strong>Хотя</strong> дата на письме была пятнадцатилетней давности, Тимур <span class="cn-word" data-pos="verb" data-tr="qaror qildi">решил</span> найти эту женщину.</p>
<p>Он <span class="cn-word" data-pos="verb" data-tr="joylashtirdi">разместил</span> фотографию письма в социальных сетях, и уже через два дня кто-то <span class="cn-word" data-pos="verb" data-tr="tanidi">узнал</span> почерк.</p>
<p><strong>Стоило только</strong> Тимуру получить её номер, <strong>как</strong> он сразу позвонил.</p>
<p>— Здравствуйте, Севара? У меня для вас есть кое-что <span class="cn-word" data-pos="adj" data-tr="gʻayrioddiy">необычное</span>, — сказал он, немного волнуясь.</p>
<p>Когда женщина <span class="cn-word" data-pos="verb" data-tr="oʻqidi">прочитала</span> своё собственное детское письмо, она <span class="cn-word" data-pos="verb" data-tr="yigʻlab yubordi">расплакалась</span>.</p>
<p>— Я совсем забыла об этом дне на пляже... — <span class="cn-word" data-pos="verb" data-tr="pichirladi">прошептала</span> она.</p>
<p>Оказалось, что Севара <span class="cn-word" data-pos="verb" data-tr="voz kechgan edi">отказалась</span> от мечты стать художницей много лет назад, выбрав <span class="cn-word" data-pos="adj" data-tr="barqaror">более надёжную</span> профессию бухгалтера.</p>
<p>Письмо от самой себя <span class="cn-word" data-pos="verb" data-tr="eslatib qoʻydi">напомнило</span> ей о том, кем она когда-то мечтала стать. Через месяц Севара <span class="cn-word" data-pos="verb" data-tr="roʻyxatdan oʻtdi">записалась</span> на курсы живописи — просто для себя, по вечерам после работы.</p>''',
        "questions": [
            {
                "text": "Что было особенного в письме, найденном Тимуром?",
                "choices": ["Оно было написано на иностранном языке", "Оно было написано ребёнком пятнадцать лет назад", "Оно было адресовано самому Тимуру"],
                "answer": 1,
                "explanation": "\"Меня зовут Севара, мне десять лет\" deb yozilgan, va sana oʻn besh yil oldingi edi.",
            },
            {
                "text": "Как Тимур нашёл автора письма?",
                "choices": ["Через полицию", "Разместив фото письма в социальных сетях", "Письмо содержало точный адрес"],
                "answer": 1,
                "explanation": "\"Разместил фотографию письма в социальных сетях... кто-то узнал почерк\" deyiladi.",
            },
            {
                "text": "Что Севара решила сделать после получения письма?",
                "choices": ["Она проигнорировала его", "Она записалась на курсы живописи", "Она переехала жить на море"],
                "answer": 1,
                "explanation": "\"Севара записалась на курсы живописи — просто для себя\" deyiladi.",
            },
        ],
    },
    {
        "title":   "Потерянный ключ",
        "summary": "Nargiza kalitini uyda unutib qoladi, biroq qo'shni buvi bilan o'tkazgan kutilmagan chойxo'rlik unga yaqin do'stlik sovg'a qiladi.",
        "order":   13,
        "grammar": [
            {
                "pattern":  "не + деепричастие",
                "meaning":  "Ikkilanmasdan, oʻylab oʻtirmasdan — inkor shaklidagi deepричастie qoʻshimcha harakatning yoʻqligini bildiradi.",
                "examples": ["Не раздумывая, она позвонила мастеру.", "Не оглядываясь, он пошёл дальше."],
            },
            {
                "pattern":  "Придётся + infinitiv",
                "meaning":  "Majburiy zaruriyat: ...ishga toʻgʻri keladi (istaklardan qatʼi nazar).",
                "examples": ["Придётся вызывать мастера по замкам.", "Если не успеем, придётся возвращаться завтра."],
            },
            {
                "pattern":  "то ..., то ...",
                "meaning":  "Goh ..., goh ... (navbatlashib takrorlanadigan harakatlar).",
                "examples": ["Она то проверяла телефон, то тяжело вздыхала.", "Он то смеялся, то грустил."],
            },
            {
                "pattern":  "Несмотря на + Accusative",
                "meaning":  "...ga qaramasdan (qarshilik bildiruvchi konstruksiya, tushum kelishigi bilan).",
                "examples": ["Несмотря на позднее время, она приготовила чай.", "Несмотря на дождь, мы пошли гулять."],
            },
        ],
        "body": '''<p>Вернувшись домой поздно вечером, Наргиза <span class="cn-word" data-pos="verb" data-tr="angladi">поняла</span>, что забыла ключи внутри квартиры.</p>
<p>— Не может быть, — <span class="cn-word" data-pos="verb" data-tr="vahima ichida gʻoʻldiradi">пробормотала</span> она, проверяя карманы не раз, а несколько.</p>
<p>— <strong>Придётся</strong> вызывать мастера по замкам, — решила она, доставая телефон <span class="cn-word" data-pos="adj" data-tr="titroq qoʻllar bilan">дрожащими руками</span>.</p>
<p>Мастер сказал, что приедет только через час. Наргиза <span class="cn-word" data-pos="verb" data-tr="oʻtirdi">села</span> на ступеньки, <strong>то</strong> проверяя телефон, <strong>то</strong> тяжело вздыхая.</p>
<p>Дверь напротив вдруг <span class="cn-word" data-pos="verb" data-tr="ochildi">открылась</span>. Пожилая соседка, тётя Зухра, <span class="cn-word" data-pos="verb" data-tr="taklif qildi">пригласила</span> её внутрь.</p>
<p>— Заходи, милая, <strong>не</strong> <span class="cn-word" data-pos="verb" data-tr="oʻtirib qolib">сидя</span> на холодной лестнице. Выпьем чаю, пока ждёшь мастера.</p>
<p><strong>Несмотря на</strong> позднее время, тётя Зухра приготовила горячий чай и <span class="cn-word" data-pos="verb" data-tr="ko'rsatdi">показала</span> старые фотографии своей молодости.</p>
<p>Час пролетел незаметно за <span class="cn-word" data-pos="adj" data-tr="qiziqarli">увлекательными</span> историями о жизни в этом доме много лет назад.</p>
<p>Когда мастер наконец <span class="cn-word" data-pos="verb" data-tr="keldi">приехал</span> и открыл дверь, он <span class="cn-word" data-pos="verb" data-tr="tanidi">узнал</span> тётю Зухру.</p>
<p>— О, это же вы помогли мне найти собаку прошлым летом! Сегодня я возьму с вас только половину цены, — <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span> он с улыбкой.</p>
<p>Наргиза <span class="cn-word" data-pos="verb" data-tr="tushundi">поняла</span>, что потерянный ключ подарил ей нечто более ценное — тёплое знакомство с соседкой, о существовании которой она раньше почти не задумывалась.</p>''',
        "questions": [
            {
                "text": "Почему Наргиза оказалась перед закрытой дверью?",
                "choices": ["Она забыла ключи внутри квартиры", "Замок сломался", "Она потеряла квартиру"],
                "answer": 0,
                "explanation": "\"Поняла, что забыла ключи внутри квартиры\" deyiladi.",
            },
            {
                "text": "Как соседка тётя Зухра помогла Наргизе?",
                "choices": ["Дала ей запасной ключ", "Пригласила её к себе пить чай, пока ждёшь мастера", "Вызвала полицию"],
                "answer": 1,
                "explanation": "\"Заходи, милая... выпьем чаю, пока ждёшь мастера\" deb taklif qiladi.",
            },
            {
                "text": "Почему мастер по замкам снизил цену для тёти Зухры?",
                "choices": ["Потому что было поздно", "Потому что она раньше помогла ему найти собаку", "Потому что у него не было сдачи"],
                "answer": 1,
                "explanation": "\"Это же вы помогли мне найти собаку прошлым летом\" deb ustaxona xodimi eslaydi.",
            },
        ],
    },
    {
        "title":   "Мастерская отца",
        "summary": "Otabek otasining duradgorlik ustaxonasidagi ishni zerikarli deb hisoblardi, ammo bir mijozning hikoyasi unga hunarning qadrini ochib beradi.",
        "order":   14,
        "grammar": [
            {
                "pattern":  "деепричастие (-в / -я)",
                "meaning":  "Deepричастие — asosiy harakat bilan bir vaqtda yoki undan oldin sodir boʻlgan qoʻshimcha harakatni bildiradi.",
                "examples": ["Не выпуская инструмент из рук, отец улыбался.", "Увидев отремонтированный стул, женщина расплакалась."],
            },
            {
                "pattern":  "Чем дольше ..., тем ...",
                "meaning":  "Qancha uzoq ..., shuncha ... (nisbiy qiyoslash konstruksiyasi).",
                "examples": ["Чем дольше он работал над стулом, тем лучше понимал отца.", "Чем дольше мы ждали, тем сильнее волновались."],
            },
            {
                "pattern":  "для того чтобы ...",
                "meaning":  "Shu maqsadda, ...uchun (maqsad ergash gapining rasmiyroq shakli).",
                "examples": ["Для того чтобы сохранить оригинальную форму, придётся работать медленно.", "Для того чтобы успеть, мы вышли пораньше."],
            },
            {
                "pattern":  "так как / поскольку",
                "meaning":  "Chunki, sababli — rasmiy sabab bogʻlovchisi.",
                "examples": ["Так как мне некуда больше обратиться, я пришла к вам.", "Поскольку было поздно, мы решили остаться."],
            },
        ],
        "body": '''<p>Каждую субботу Отабек <span class="cn-word" data-pos="verb" data-tr="borishga majbur edi">был вынужден</span> проводить время в <span class="cn-word" data-tr="ustaxona">мастерской</span> отца, помогая с <span class="cn-word" data-tr="duradgorlik">столярными</span> работами.</p>
<p>— Мне это неинтересно, — <span class="cn-word" data-pos="verb" data-tr="shikoyat qilardi">жаловался</span> он друзьям. — Отец всегда занят своими старыми досками.</p>
<p><strong>Не выпуская</strong> инструмент из рук, отец лишь молча улыбался в ответ на его недовольство.</p>
<p>Однажды в мастерскую <span class="cn-word" data-pos="verb" data-tr="kirib keldi">зашла</span> пожилая женщина с сломанным деревянным стулом.</p>
<p>— Этот стул <span class="cn-word" data-pos="verb" data-tr="yasagan edi">сделал</span> мой покойный муж своими руками для нашей свадьбы, — <span class="cn-word" data-pos="verb" data-tr="tushuntirdi">объяснила</span> она. — <strong>Так как</strong> мне некуда больше обратиться, я пришла к вам.</p>
<p>Отабек с удивлением <span class="cn-word" data-pos="verb" data-tr="kuzatdi">наблюдал</span>, как отец <span class="cn-word" data-pos="adv" data-tr="ehtiyotkorlik bilan">бережно</span> взял стул, будто это была не мебель, а <span class="cn-word" data-pos="adj" data-tr="qadrli">драгоценная</span> вещь.</p>
<p>— <strong>Для того чтобы</strong> сохранить оригинальную форму, придётся работать очень медленно, — <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span> отец сыну. — Поможешь мне?</p>
<p><strong>Чем дольше</strong> Отабек работал над стулом рядом с отцом, <strong>тем</strong> лучше он понимал: это не просто дерево, а чья-то память.</p>
<p>Через неделю женщина, <strong>увидев</strong> отремонтированный стул, <span class="cn-word" data-pos="verb" data-tr="yigʻlab yubordi">расплакалась</span> от благодарности.</p>
<p>С того дня Отабек начал приходить в мастерскую уже не по принуждению, а потому что понял: руки отца хранят чужие истории.</p>''',
        "questions": [
            {
                "text": "Как Отабек относился к работе в мастерской отца в начале истории?",
                "choices": ["Ему очень нравилось", "Ему было неинтересно, он считал это скучным", "Он мечтал стать столяром"],
                "answer": 1,
                "explanation": "\"Мне это неинтересно... Отец всегда занят своими старыми досками\" deb shikoyat qiladi.",
            },
            {
                "text": "Почему стул женщины был для неё таким важным?",
                "choices": ["Он был очень дорогим", "Его сделал её покойный муж к их свадьбе", "Это был единственный стул в доме"],
                "answer": 1,
                "explanation": "\"Этот стул сделал мой покойный муж своими руками для нашей свадьбы\" deb tushuntiradi.",
            },
            {
                "text": "Что понял Отабек, помогая отцу чинить стул?",
                "choices": ["Что столярное дело — скучное занятие", "Что руки отца хранят чужие истории и это не просто дерево", "Что нужно поскорее продать мастерскую"],
                "answer": 1,
                "explanation": "\"Руки отца хранят чужие истории\" deb tushunadi hikoya oxirida.",
            },
        ],
    },
    {
        "title":   "Последний рейс автобуса",
        "summary": "Nafaqaga chiqish arafasidagi haydovchi Sobir-aka oxirgi ish kunida yolg'iz qolgan yo'lovchi bilan iliq lahzani boshdan kechiradi.",
        "order":   15,
        "grammar": [
            {
                "pattern":  "деепричастие несовершенного вида (-я / -а)",
                "meaning":  "Nomukammal deepричастие — asosiy harakat bilan bir vaqtda davom etayotgan harakatni bildiradi.",
                "examples": ["Ведя автобус в последний раз, он вспоминал пассажиров.", "Разбудив студента, он мягко улыбнулся."],
            },
            {
                "pattern":  "то и дело",
                "meaning":  "Tez-tez, doim — takrorlanadigan harakatni bildiruvchi ravish birikmasi.",
                "examples": ["Он то и дело вспоминал лица пассажиров.", "Она то и дело поглядывала на часы."],
            },
            {
                "pattern":  "вот уже + muddat",
                "meaning":  "Mana ... boʻldi — davomiylikni taʼkidlaydigan konstruksiya.",
                "examples": ["Вот уже тридцать лет он водит этот маршрут.", "Вот уже неделю идёт дождь."],
            },
            {
                "pattern":  "как ни ...",
                "meaning":  "Qanchalik ... boʻlmasin — qarshilikni taʼkidlovchi konstruksiya.",
                "examples": ["Как ни устал бы я, я никогда не сердился на пассажиров.", "Как ни старался, он не успел вовремя."],
            },
        ],
        "body": '''<p>Сегодня был <span class="cn-word" data-pos="adj" data-tr="oxirgi">последний</span> рабочий день Собира-ака за рулём автобуса — завтра он <span class="cn-word" data-pos="verb" data-tr="nafaqaga chiqadi">уходит на пенсию</span>.</p>
<p><strong>Вот уже</strong> тридцать лет он <span class="cn-word" data-pos="verb" data-tr="yurgan edi">водил</span> этот же маршрут через весь город.</p>
<p><strong>Ведя</strong> автобус в последний раз, он <strong>то и дело</strong> вспоминал лица тысяч <span class="cn-word" data-tr="yoʻlovchilar">пассажиров</span>, которых перевёз за эти годы.</p>
<p>Поздно вечером в автобусе <span class="cn-word" data-pos="verb" data-tr="qolgan edi">остался</span> только один пассажир — студент, <span class="cn-word" data-pos="verb" data-tr="uxlab qolgan edi">задремавший</span> у окна.</p>
<p>— Молодой человек, ваша остановка, — <span class="cn-word" data-pos="adv" data-tr="muloyimlik bilan">мягко</span> разбудил его Собир-ака.</p>
<p>— Простите, я, наверное, вас <span class="cn-word" data-pos="verb" data-tr="ushlab qoldim">задержал</span>, — <span class="cn-word" data-pos="verb" data-tr="tan oldi">признался</span> студент, <span class="cn-word" data-pos="adj" data-tr="uyalgan">смущённый</span>.</p>
<p>— Ничего страшного. <strong>Как ни</strong> устал бы я за эти годы, я никогда не <span class="cn-word" data-pos="verb" data-tr="jahli chiqmagan">сердился</span> на пассажиров, — <span class="cn-word" data-pos="verb" data-tr="dedi">ответил</span> водитель с улыбкой.</p>
<p>Приехав в парк, Собир-ака <span class="cn-word" data-pos="verb" data-tr="koʻrdi">увидел</span>, что его коллеги <span class="cn-word" data-pos="verb" data-tr="tayyorlashgan edilar">подготовили</span> для него небольшой прощальный вечер с тортом и цветами.</p>
<p>— Тридцать лет — это не просто работа, — <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span> ему начальник парка. — Это тридцать лет чужих историй, которые вы бережно довозили до дома.</p>
<p>Собир-ака, <span class="cn-word" data-pos="verb" data-tr="koʻzlariga yosh keldi">прослезившись</span>, понял, что его работа была куда важнее, чем он сам когда-либо думал.</p>''',
        "questions": [
            {
                "text": "Сколько лет Собир-ака водил один и тот же маршрут?",
                "choices": ["Десять лет", "Тридцать лет", "Пять лет"],
                "answer": 1,
                "explanation": "\"Вот уже тридцать лет он водил этот же маршрут\" deyiladi.",
            },
            {
                "text": "Что произошло со студентом в автобусе поздно вечером?",
                "choices": ["Он вышел не на той остановке", "Он задремал и чуть не проехал свою остановку", "Он поссорился с водителем"],
                "answer": 1,
                "explanation": "\"Студент, задремавший у окна\" — Sobir-aka uni yumshoqlik bilan uygʻotadi.",
            },
            {
                "text": "Что поняли коллеги Собира-ака, устраивая ему прощальный вечер?",
                "choices": ["Что его работа была важнее, чем просто вождение автобуса", "Что он плохо работал все эти годы", "Что автобус нужно списать"],
                "answer": 0,
                "explanation": "\"Тридцать лет чужих историй, которые вы бережно довозили до дома\" deyiladi.",
            },
        ],
    },
]
