# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-95 … PR-97.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.
⛔ URGʻU BELGISI YOʻQ — 2026-08-24 dagi qaror.

Janr xilma-xilligi: 95 — xat (buvidan nevaraga), 96 — ilmiy-ommabop
(til haqida), 97 — maktab hikoyasi.

Grammatika chegarasi (kumulyativ qoida):
  95-matn: maqollar — matn ichida toʻrtta maqol tabiiy joylashgan,
           bittasi yarmigacha aytilgan (yarmini aytish odati).
  96-matn: надеть / одеть farqi va «Надевают одежду, одевают
           Надежду» eslatmasi; класть / положить.
  97-matn: tinish belgilari — «Казнить нельзя помиловать»,
           ega-kesim tiresi, undalma va kirish soʻzdagi vergul.

⚠️ ATAY QOCHILGAN (keyingi darslar): insho qurilishi (PR-98),
rus tilining kelib chiqishi (PR-99).

⚠️ FAKTLAR:
  95 va 96 — toʻqima matnlar. 95-dagi maqollar haqiqiy rus
  maqollari; 96-dagi «Надевают одежду, одевают Надежду» — rus
  maktablarida haqiqatan ishlatiladigan eslatma.
  97-matn — toʻqima maktab sahnasi, LEKIN ichidagi adabiy havola
  haqiqiy: «Казнить нельзя помиловать» jumlasi rus madaniyatida
  Liya Geraskinaning «В Стране невыученных уроков» (1965) qissasi
  va shu asosda ishlangan «Союзмультфильм» multfilmi (1969) bilan
  bogʻliq. Qahramoni — Виктор (Витя) Перестукин; u aynan shu
  jumlada vergulni qoʻyib, oʻz taqdirini hal qiladi. Tekshirildi.
  Jumlaning qirol yoki podshoh haqidagi «tarixiy» rivoyati esa
  hujjatlashtirilmagan — shuning uchun matnda daʼvo qilinmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_95_97.py --author=prime
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
    # PR-95 — maqollar                                            XAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Письмо из кишлака",
        "summary": (
            "PR-95 matni. Dilnoza ikki universitet orasida tanlay olmayapti. "
            "Buvisi qishloqdan xat yozadi — va maslahatning har biri maqol "
            "bilan tugaydi."
        ),
        "order":   95,
        "grammar": [
            {
                "pattern":  "Семь раз отмерь, один раз отрежь",
                "meaning":  "Oʻzbekchasi «Yetti oʻlchab, bir kes» — raqamigacha "
                            "bir xil. Xatning asosiy maslahati shu.",
                "examples": ["Не спеши. Семь раз отмерь, один раз отрежь.",
                             "Yetti oʻlchab, bir kes."],
            },
            {
                "pattern":  "Язык до Киева доведёт",
                "meaning":  "Soʻrab-soʻrab istagan joyingga yetasan. "
                            "Oʻzbekcha jufti — «Soʻrab-soʻrab Makkani topibdi».",
                "examples": ["Спрашивай у всех. Язык до Киева доведёт."],
            },
            {
                "pattern":  "Половина пословицы",
                "meaning":  "Rus nutqida maqolning yarmi aytiladi, qolganini "
                            "tinglovchi oʻzi biladi. Xatda ham shunday.",
                "examples": ["Ты же знаешь: не всё то золото…"],
            },
        ],
        "body": '''<p>Дилноза, здравствуй, моя хорошая.</p>

<p>Мама написала мне, что ты не можешь <span class="cn-word" data-pos="verb" data-tr="tanlamoq">выбрать</span> между двумя университетами. Один ближе к дому, другой <span class="cn-word" data-tr="mashhurroq">известнее</span>, но в другом городе.</p>

<p>Я <span class="cn-word" data-tr="oʻn bir sinf">одиннадцать классов</span> в жизни не кончала, <span class="cn-word" data-tr="maslahat">совета</span> учёного дать не могу. Но одно скажу: не <span class="cn-word" data-pos="verb" data-tr="shoshilma">спеши</span>. <strong>Семь раз отмерь, один раз отрежь.</strong> Твой дед так всю жизнь работал и ни одной доски зря не <span class="cn-word" data-pos="verb" data-tr="kesmadi">испортил</span>.</p>

<p>Ты <span class="cn-word" data-pos="verb" data-tr="yozgansan">писала</span>, что во втором университете <span class="cn-word" data-tr="chiroyli">красивое</span> здание и новые <span class="cn-word" data-tr="kompyuterlar">компьютеры</span>. Это хорошо. Но ты же сама знаешь: <strong>не всё то золото…</strong></p>

<p><span class="cn-word" data-pos="verb" data-tr="soʻra">Спроси</span> у тех, кто там учится. Спроси у <span class="cn-word" data-tr="oʻqituvchilar">преподавателей</span>. Не <span class="cn-word" data-pos="verb" data-tr="uyalma">стесняйся</span> — <strong>язык до Киева доведёт</strong>.</p>

<p>И ещё. Ты <span class="cn-word" data-pos="verb" data-tr="qoʻrqasan">боишься</span>, что в чужом городе будет <span class="cn-word" data-tr="qiyin">трудно</span>. Будет. Первый год всегда трудный. <strong>Первый блин комом</strong> — это про всё, не только про еду.</p>

<p>Но <span class="cn-word" data-tr="sabr">терпение</span> и <span class="cn-word" data-tr="mehnat">труд</span> всё <span class="cn-word" data-pos="verb" data-tr="yengadi">перетрут</span>. Это не я придумала, это люди до меня <span class="cn-word" data-pos="verb" data-tr="yashab koʻrishgan">прожили</span>.</p>

<p>Про деньги тоже не забудь <span class="cn-word" data-pos="verb" data-tr="soʻramoq">спросить</span>: сколько стоит <span class="cn-word" data-tr="yotoqxona">общежитие</span>, сколько дорога домой. Дед всегда говорил, что <span class="cn-word" data-tr="hisob">счёт</span> дружбу не <span class="cn-word" data-pos="verb" data-tr="buzadi">портит</span>.</p>

<p>И <span class="cn-word" data-pos="verb" data-tr="qidir">поищи</span> там наших. В большом городе один <span class="cn-word" data-tr="yerlik">земляк</span> дороже ста <span class="cn-word" data-tr="tanishlar">знакомых</span>. Недаром говорят: <strong>не имей сто рублей, а имей сто друзей</strong>.</p>

<p><span class="cn-word" data-pos="verb" data-tr="qaror qil">Решай</span> сама. Что бы ты ни выбрала, я <span class="cn-word" data-tr="xursand boʻlaman">буду рада</span>.</p>

<p>Приезжай <span class="cn-word" data-tr="kuzda">осенью</span>. <span class="cn-word" data-tr="oʻriklar">Абрикосы</span> уже будут сухие, я тебе <span class="cn-word" data-pos="verb" data-tr="tayyorlab qoʻyaman">приготовлю</span> целый мешок.</p>

<p>Твоя бабушка.</p>''',
        "questions": [
            {
                "text": "Buvi Dilnozaga qanday asosiy maslahat beradi?",
                "choices": [
                    "Uyga yaqin universitetni tanla",
                    "Shoshilma — qaror qilishdan oldin yaxshilab oʻylab koʻr",
                    "Mashhurroq universitetni tanla",
                    "Umuman oʻqishga kirma"
                ],
                "answer": 1,
                "explanation": "«Не спеши. Семь раз отмерь, один раз отрежь». "
                               "Buvi qaysi universitetni tanlashni aytmaydi — u "
                               "faqat <em>qanday</em> tanlashni aytadi. Oxirida "
                               "esa: «Решай сама».",
            },
            {
                "text": "«Не всё то золото…» — nega buvi gapni tugatmadi?",
                "choices": [
                    "U maqolni unutib qoʻygan",
                    "Xatda joy qolmagan",
                    "Bu xato",
                    "Rus nutqida maqolning yarmi aytiladi — tinglovchi qolganini oʻzi biladi"
                ],
                "answer": 3,
                "explanation": "Toʻliq maqol — «Не всё то золото, что блестит». "
                               "Buvi «ты же сама знаешь» deb, yarmini aytdi. Bu "
                               "rus nutqining odatiy usuli va u maqol "
                               "ikkalasiga ham maʼlum ekanini koʻrsatadi.",
            },
            {
                "text": "«Первый блин комом» buvining fikricha nima haqida?",
                "choices": [
                    "Faqat ovqat haqida",
                    "Birinchi yil har doim qiyin boʻlishi haqida",
                    "Non pishirish haqida",
                    "Universitet oshxonasi haqida"
                ],
                "answer": 1,
                "explanation": "«Первый год всегда трудный. Первый блин комом — "
                               "это про всё, не только про еду». Buvi maqolning "
                               "obrazidan chiqib, uni hayotga qoʻllaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-96 — adashtiriladigan juftlar               ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Одеть или надеть?",
        "summary": (
            "PR-96 matni. Rus tilida shunday xatolar borki, ularni ruslarning "
            "oʻzi ham qiladi. Ikkitasi haqida: надеть/одеть juftligi va "
            "umuman mavjud boʻlmagan «ложить» feʼli."
        ),
        "order":   96,
        "grammar": [
            {
                "pattern":  "надеть что? · одеть кого?",
                "meaning":  "Narsani kiyasan — надеть; odamni kiydirasan — "
                            "одеть. Oʻzbekcha: kiymoq / kiydirmoq.",
                "examples": ["Я надел пальто.", "Я одел ребёнка."],
            },
            {
                "pattern":  "Надевают одежду, одевают Надежду",
                "meaning":  "Rus maktablaridagi eslatma. Одежда — narsa, "
                            "Надежда — odam ismi.",
                "examples": ["Надевают одежду, одевают Надежду."],
            },
            {
                "pattern":  "класть без приставки, положить с приставкой",
                "meaning":  "«Ложить» degan feʼl adabiy tilda mavjud emas.",
                "examples": ["Я кладу книгу на стол.",
                             "Я положил книгу на стол."],
            },
        ],
        "body": '''<p>Есть <span class="cn-word" data-tr="xatolar">ошибки</span>, которые делают <span class="cn-word" data-tr="chet elliklar">иностранцы</span>. А есть такие, которые делают сами русские — и <span class="cn-word" data-pos="verb" data-tr="bahslashishadi">спорят</span> о них в интернете <span class="cn-word" data-tr="yillar davomida">годами</span>.</p>

<p>Самая <span class="cn-word" data-tr="mashhur">известная</span> — <strong>одеть</strong> и <strong>надеть</strong>.</p>

<p><span class="cn-word" data-pos="verb" data-tr="tasavvur qiling">Представьте</span>: мать говорит сыну «одень шапку». Все <span class="cn-word" data-pos="verb" data-tr="tushunishadi">понимают</span>, что она <span class="cn-word" data-pos="verb" data-tr="demoqchi">имеет в виду</span>. И всё-таки по <span class="cn-word" data-tr="qoidaga koʻra">правилу</span> это ошибка.</p>

<p><span class="cn-word" data-tr="qoida">Правило</span> короткое. <strong>Надеть</strong> — <span class="cn-word" data-tr="nimani">что</span>: шапку, пальто, очки. Ты <span class="cn-word" data-pos="verb" data-tr="kiyasan">надеваешь</span> вещь на себя.</p>

<p><strong>Одеть</strong> — <span class="cn-word" data-tr="kimni">кого</span>: ребёнка, куклу, больного. Ты <span class="cn-word" data-pos="verb" data-tr="kiydirasan">одеваешь</span> человека.</p>

<p>В школе это <span class="cn-word" data-pos="verb" data-tr="yodlashadi">запоминают</span> одной <span class="cn-word" data-tr="ibora">фразой</span>: <strong>«Надевают одежду, одевают Надежду»</strong>. Одежда — вещь, Надежда — <span class="cn-word" data-tr="ayol ismi">женское имя</span>. Слова как будто <span class="cn-word" data-pos="verb" data-tr="oʻrin almashgan">поменялись местами</span>, и <span class="cn-word" data-tr="aynan shuning uchun">именно поэтому</span> фраза <span class="cn-word" data-pos="verb" data-tr="esda qoladi">запоминается</span>.</p>

<p>Вторая ошибка <span class="cn-word" data-tr="jiddiyroq">серьёзнее</span>. Многие говорят <em>«я ложу книгу на стол»</em>.</p>

<p>Такого <span class="cn-word" data-tr="feʼl">глагола</span> в русском языке <span class="cn-word" data-tr="yoʻq">нет</span>.</p>

<p>Правило тоже короткое. Без <span class="cn-word" data-tr="prefiks">приставки</span> — только <strong>класть</strong>: я кладу, ты кладёшь, он клал. С приставкой — только <strong>-ложить</strong>: положить, сложить, вложить.</p>

<p>Поэтому «положил» — <span class="cn-word" data-tr="toʻgʻri">правильно</span>, «ложил» — нет. А «покласть» тоже нет.</p>

<p>На улице вы <span class="cn-word" data-pos="verb" data-tr="eshitasiz">услышите</span> и «ложить», и «одень шапку». Но на письме и на <span class="cn-word" data-tr="imtihonda">экзамене</span> это <span class="cn-word" data-pos="verb" data-tr="hisoblanadi">считается</span> ошибкой.</p>

<p><span class="cn-word" data-tr="qiziq narsa">Интересно</span> вот что. Для <span class="cn-word" data-tr="oʻzbek">узбека</span> первая пара <span class="cn-word" data-tr="osonroq">легче</span>, чем для англичанина. В узбекском языке эта же <span class="cn-word" data-tr="farq">разница</span> есть, только она <span class="cn-word" data-pos="verb" data-tr="beriladi">выражается</span> одним <span class="cn-word" data-tr="qoʻshimcha">суффиксом</span> внутри слова.</p>''',
        "questions": [
            {
                "text": "«Надеть» va «одеть» orasidagi farq nimada?",
                "choices": [
                    "Birinchisi kelasi zamon, ikkinchisi oʻtgan zamon",
                    "Birinchisi narsaga (что?), ikkinchisi odamga (кого?) ishlatiladi",
                    "Birinchisi rasmiy, ikkinchisi norasmiy",
                    "Farqi yoʻq"
                ],
                "answer": 1,
                "explanation": "«Надеть — что: шапку, пальто… Одеть — кого: "
                               "ребёнка, куклу». Oʻzbekchada bu farq bitta "
                               "qoʻshimcha bilan beriladi: <em>kiymoq</em> va "
                               "<em>kiy<strong>dir</strong>moq</em>.",
            },
            {
                "text": "Nega «Надевают одежду, одевают Надежду» iborasi esda qoladi?",
                "choices": [
                    "Chunki u qofiyalangan sheʼr",
                    "Chunki u juda qisqa",
                    "Chunki soʻzlar oʻrin almashgandek koʻrinadi — наде- одежда bilan, оде- Надежда bilan ketadi",
                    "Chunki uni har kuni takrorlashadi"
                ],
                "answer": 2,
                "explanation": "«Слова как будто поменялись местами, и именно "
                               "поэтому фраза запоминается». Kutilmagan "
                               "joylashuv xotirani ushlab turadi.",
            },
            {
                "text": "Matnga koʻra, «ложить» feʼli haqida nima deyish mumkin?",
                "choices": [
                    "U faqat oʻtgan zamonda ishlatiladi",
                    "U eskirgan, lekin toʻgʻri",
                    "U faqat prefiks bilan ishlatiladi",
                    "U adabiy rus tilida umuman mavjud emas"
                ],
                "answer": 3,
                "explanation": "«Такого глагола в русском языке нет». Qoida: "
                               "prefikssiz — faqat <em>класть</em>, prefiks "
                               "bilan — faqat <em>-ложить</em> (положить, "
                               "сложить, вложить).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-97 — punktuatsiya                            MAKTAB HIKOYASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Запятая на доске",
        "summary": (
            "PR-97 matni. Oʻqituvchi doskaga uch soʻz yozadi va sinfdan "
            "vergul qoʻyishni soʻraydi. Bekzod bir joyga, Afsona boshqa "
            "joyga qoʻyadi — va ikkalasi ham toʻgʻri."
        ),
        "order":   97,
        "grammar": [
            {
                "pattern":  "Казнить нельзя помиловать",
                "meaning":  "Vergulning oʻrni butun gapning maʼnosini "
                            "oʻzgartiradigan mashhur misol.",
                "examples": ["Казнить, нельзя помиловать.",
                             "Казнить нельзя, помиловать."],
            },
            {
                "pattern":  "Тире между подлежащим и сказуемым",
                "meaning":  "Ot bilan ot orasida tire turadi, chunki hozirgi "
                            "zamonda «boʻlmoq» feʼli aytilmaydi.",
                "examples": ["Запятая — маленький знак.",
                             "Москва — столица России."],
            },
            {
                "pattern":  "Обращение и вводное слово",
                "meaning":  "Undalma va kirish soʻz har doim vergul bilan "
                            "ajratiladi — oʻzbekchada ham xuddi shunday.",
                "examples": ["Бекзод, иди к доске.",
                             "Конечно, я знаю."],
            },
        ],
        "body": '''<p>Марина Петровна <span class="cn-word" data-pos="verb" data-tr="yozdi">написала</span> на <span class="cn-word" data-tr="doska">доске</span> три слова:</p>

<p><strong>Казнить нельзя помиловать</strong></p>

<p>— <span class="cn-word" data-tr="tinish belgisi">Знаков препинания</span> нет, — сказала она. — Бекзод, иди к доске и <span class="cn-word" data-pos="verb" data-tr="qoʻy">поставь</span> запятую.</p>

<p>Бекзод <span class="cn-word" data-pos="verb" data-tr="oʻyladi">подумал</span> и поставил её после первого слова.</p>

<p><strong>Казнить, нельзя помиловать.</strong></p>

<p>— <span class="cn-word" data-pos="verb" data-tr="oʻqi">Прочитай</span>, что получилось.</p>

<p>— «Казнить, нельзя помиловать»… — Бекзод <span class="cn-word" data-pos="verb" data-tr="toʻxtadi">остановился</span>. — Получается, человека <span class="cn-word" data-pos="verb" data-tr="qatl qilishadi">казнят</span>.</p>

<p>— <span class="cn-word" data-tr="hammasi toʻgʻri">Всё верно</span>, — сказала учительница. — Запятая <span class="cn-word" data-pos="verb" data-tr="ajratadi">отделяет</span> первое слово, и оно <span class="cn-word" data-pos="verb" data-tr="buyruqqa aylanadi">становится приказом</span>. Афсона, теперь ты.</p>

<p>Афсона <span class="cn-word" data-pos="verb" data-tr="oʻchirdi">стёрла</span> запятую и поставила её на одно слово <span class="cn-word" data-tr="oʻngga">правее</span>.</p>

<p><strong>Казнить нельзя, помиловать.</strong></p>

<p>— А теперь его <span class="cn-word" data-pos="verb" data-tr="kechirishadi">милуют</span>, — сказала она <span class="cn-word" data-tr="sekin">тихо</span>.</p>

<p>В классе стало <span class="cn-word" data-tr="jimjit">тихо</span>.</p>

<p>— Три слова, — сказала Марина Петровна. — Вы их не <span class="cn-word" data-pos="verb" data-tr="oʻzgartirmadingiz">меняли</span>. Вы <span class="cn-word" data-pos="verb" data-tr="koʻchirdingiz">передвинули</span> один <span class="cn-word" data-tr="belgi">знак</span> — и человек <span class="cn-word" data-pos="verb" data-tr="tirik qoldi">остался жив</span>.</p>

<p>Она села за стол.</p>

<p>— <span class="cn-word" data-tr="vergul">Запятая</span> — маленький знак. Но <span class="cn-word" data-tr="hazil">шутки</span> с ней <span class="cn-word" data-tr="yomon">плохие</span>. Кто <span class="cn-word" data-pos="verb" data-tr="oʻqigan">читал</span> «В Стране невыученных уроков»?</p>

<p><span class="cn-word" data-tr="bir necha qoʻl">Несколько рук</span> поднялись.</p>

<p>— Там <span class="cn-word" data-tr="qahramon">герой</span>, Витя Перестукин, <span class="cn-word" data-pos="verb" data-tr="qoʻyadi">ставит</span> эту самую запятую. И <span class="cn-word" data-pos="verb" data-tr="hal qiladi">решает</span> свою <span class="cn-word" data-tr="taqdir">судьбу</span>. Конечно, это <span class="cn-word" data-tr="ertak">сказка</span>. Но правило в ней <span class="cn-word" data-tr="haqiqiy">настоящее</span>.</p>

<p><span class="cn-word" data-tr="qoʻngʻiroq">Звонок</span> уже <span class="cn-word" data-pos="verb" data-tr="chalindi">прозвенел</span>, но никто не <span class="cn-word" data-pos="verb" data-tr="oʻrnidan turmadi">встал</span>. Три слова так и <span class="cn-word" data-pos="verb" data-tr="turardi">стояли</span> на доске, и запятая в них была на <span class="cn-word" data-tr="yaxshi joyda">хорошем месте</span>.</p>''',
        "questions": [
            {
                "text": "Bekzod va Afsona doskada nima qilishdi?",
                "choices": [
                    "Soʻzlarni oʻzgartirishdi",
                    "Yangi gap yozishdi",
                    "Bitta vergulni ikki xil joyga qoʻyishdi",
                    "Gapni oʻchirib tashlashdi"
                ],
                "answer": 2,
                "explanation": "«Вы их не меняли. Вы передвинули один знак». "
                               "Bekzod «казнить» dan keyin, Afsona esa "
                               "«нельзя» dan keyin qoʻydi — natija "
                               "qarama-qarshi chiqdi.",
            },
            {
                "text": "Qaysi variantda odam tirik qoladi?",
                "choices": [
                    "Казнить, нельзя помиловать",
                    "Казнить нельзя, помиловать",
                    "Ikkalasida ham",
                    "Hech qaysisida"
                ],
                "answer": 1,
                "explanation": "Vergul <em>нельзя</em> dan keyin tursa — «qatl "
                               "qilib boʻlmaydi, kechiring». Afsona aynan "
                               "shunday qoʻydi va «теперь его милуют» dedi.",
            },
            {
                "text": "Marina Petrovna nima uchun «В Стране невыученных уроков» ni tilga oldi?",
                "choices": [
                    "Chunki bu kitobni sinf oʻqishi kerak edi",
                    "Chunki u yozuvchi haqida gapirmoqchi edi",
                    "Chunki kitob qahramoni ham xuddi shu vergulni qoʻyib, oʻz taqdirini hal qiladi",
                    "Chunki kitobda maktab haqida yozilgan"
                ],
                "answer": 2,
                "explanation": "«Там герой, Витя Перестукин, ставит эту самую "
                               "запятую. И решает свою судьбу». Oʻqituvchi "
                               "darsdagi misolni bolalarga tanish kitob bilan "
                               "bogʻlaydi — «это сказка, но правило в ней "
                               "настоящее».",
            },
        ],
    },
]
