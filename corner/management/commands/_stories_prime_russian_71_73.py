# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-71 … PR-73.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 71 — biografiya, 72 — hikoya, 73 — maktub-javob.
(68 sirli hikoya, 69 hayot hikoyasi, 70 ilmiy-ommabop edi. Maktub-javob
bu blokda birinchi marta ishlatilyapti.)

Grammatika chegarasi (kumulyativ qoida):
  71-matn: страдательные причастия — toʻliq shaklda (написанная,
           записанная, переведённая) va qisqa shaklda (написана,
           издана, забыта). «Кем?» Творительный bilan ikki joyda.
  72-matn: деепричастия — возвращаясь, увидев, не зная, купив,
           улыбаясь, выйдя. Har birida ega asosiy feʼlniki bilan bir xil —
           darsning qatʼiy qoidasi matnda buzilmagan.
  73-matn: qisqa sifatlar — прав, виноват, рад, должен, занят,
           согласен, нужен, свободен. Xat janri bu toʻplam uchun ideal.

⚠️ ATAY QOCHILGAN (keyingi darslar): SIFAT DARAJALARI — самый /
больше / лучше / хуже (PR-74), свой (PR-75), себя / сам (PR-76),
каждый / весь ning nozik farqi (PR-77), кто-то / кто-нибудь (PR-78),
никто … не (PR-79), шахссиз gaplar (PR-81), жамловчи sonlar — оба,
трое (PR-82).

⚠️ FAKTLAR (71-matn — HAQIQIY ODAM):
  Marko Polo (Marco Polo), venetsiyalik savdogar, taxminan 1271–1295
  yillarda Osiyoda boʻlgan va Xubilayxon xizmatida yigirma yilga yaqin
  yashagan. 1298-yil atrofida Venetsiya–Genuya urushida asirga tushib,
  Genuyada qamoqqa olingan. Kamerada u bilan birga yozuvchi Rustikello
  da Piza oʻtirgan va Markoning hikoyalarini yozib olgan — shu tariqa
  «Dunyoning xilma-xilligi haqida kitob» paydo boʻlgan. Marko 1299-yilda
  ozod qilingan. Kitob koʻp tillarga tarjima qilingan; Xristofor Kolumbning
  shaxsiy nusxasi chetlariga yozgan izohlari bilan Sevilyada saqlanadi.
  72 va 73 — toʻqima voqealar, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_71_73.py --author=prime
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
    # PR-71 — страдательные причастия                    BIOGRAFIYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Книга, написанная в тюрьме",
        "summary": (
            "PR-71 matni. Marko Polo Genuya qamoqxonasida kamerdoshiga oʻz "
            "sayohatlarini aytib bergan — shundan dunyoning eng mashhur "
            "sayohat kitobi tugʻilgan. Faktlar haqiqiy."
        ),
        "order":   71,
        "grammar": [
            {
                "pattern":  "Toʻliq shakl: -нн- / -енн- / -т-",
                "meaning":  "Otni aniqlaydi va unga moslashadi. Sarlavhaning oʻzi "
                            "shunday: «книга, написанная в тюрьме».",
                "examples": ["книга, написанная в тюрьме",
                             "истории, записанные Рустикелло"],
            },
            {
                "pattern":  "Qisqa shakl: bitta Н",
                "meaning":  "Gapning kesimi boʻladi: «книга издана», «Марко "
                            "был освобождён». Toʻliqda ikkita Н, qisqada bitta.",
                "examples": ["Книга была переведена на многие языки.",
                             "Марко был освобождён в 1299 году."],
            },
            {
                "pattern":  "Кем? — Творительный",
                "meaning":  "Ishni kim bajarganini predlogsiz Творительный "
                            "bildiradi — oʻzbekcha «tomonidan».",
                "examples": ["записанные Рустикелло",
                             "прочитанная Колумбом"],
            },
        ],
        "body": '''<p>В 1298 году в <span class="cn-word" data-tr="Genuya (shahar)">Генуе</span> сидел в тюрьме человек по имени Марко Поло.</p>

<p>До этого он двадцать лет <span class="cn-word" data-pos="verb" data-tr="sayohat qilgan">путешествовал</span>. Он выехал из Венеции ещё <span class="cn-word" data-tr="oʻsmir">подростком</span>, дошёл до Китая и много лет служил при <span class="cn-word" data-tr="saroy">дворе</span> Хубилай-хана. Он видел бумажные деньги, <span class="cn-word" data-tr="koʻmir">уголь</span>, который горит как дерево, и города, <strong>построенные</strong> на воде.</p>

<p>Когда Марко вернулся домой, началась война между Венецией и Генуей. Марко пошёл на войну, и его <span class="cn-word" data-pos="verb" data-tr="asirga olishdi">взяли в плен</span>.</p>

<p>В камере с ним сидел <span class="cn-word" data-tr="pizalik">пизанец</span> Рустикелло — писатель. Ему было <span class="cn-word" data-tr="zerikarli">скучно</span>. Марко начал рассказывать.</p>

<p>Так появилась книга, <strong>написанная в тюрьме</strong>. Точнее — <strong>рассказанная</strong> одним человеком и <strong>записанная</strong> другим.</p>

<p>В 1299 году Марко был <strong>освобождён</strong> и вернулся в Венецию. А книга начала <span class="cn-word" data-pos="verb" data-tr="dunyo boʻylab tarqalmoq">расходиться по миру</span>.</p>

<p>Она была <strong>переведена</strong> на <span class="cn-word" data-tr="oʻnlab">десятки</span> языков. Её <span class="cn-word" data-pos="verb" data-tr="koʻchirib yozishardi">переписывали</span> от руки двести лет, пока не появилась печать.</p>

<p>Многие ей не верили. Рассказы о Китае казались <span class="cn-word" data-tr="uydirma">выдумкой</span>, и книга получила <span class="cn-word" data-tr="masxaralab qoʻyilgan laqab">насмешливое прозвище</span> — «Миллион».</p>

<p>Но одна копия попала к <span class="cn-word" data-tr="genuyalik">генуэзскому</span> моряку. Его звали Христофор Колумб. Этот <span class="cn-word" data-tr="nusxa">экземпляр</span>, <strong>прочитанный</strong> им от начала до конца, сохранился до наших дней. На <span class="cn-word" data-tr="chetlarida">полях</span> — сотни <span class="cn-word" data-tr="izohlar">заметок</span>, <strong>сделанных</strong> его рукой.</p>

<p>Книга, <strong>написанная</strong> в камере от <span class="cn-word" data-tr="zerikkanlikdan">скуки</span>, через двести лет отправила человека через океан.</p>''',
        "questions": [
            {
                "text": "Kitob qanday paydo boʻldi?",
                "choices": [
                    "Marko Polo uni Xitoyda yozgan",
                    "Rustikello Markoning hikoyalarini qamoqxona kamerasida yozib olgan",
                    "Kolumb uni Markoning xatlaridan tuzgan",
                    "Venetsiya hukumati uni buyurtma qilgan"
                ],
                "answer": 1,
                "explanation": "«Рассказанная одним человеком и записанная "
                               "другим». Marko gapirdi, yozuvchi Rustikello "
                               "yozdi — ikkalasi ham asirlikda edi.",
            },
            {
                "text": "Nega matnda «книга была переведена», lekin «книга, переведённая…» emas?",
                "choices": [
                    "Chunki bu koʻplik shakli",
                    "Chunki gap oʻtgan zamonda",
                    "Ikkalasi ham bir xil, farqi yoʻq",
                    "Chunki bu yerda kesim kerak — demak qisqa shakl, bitta Н bilan"
                ],
                "answer": 3,
                "explanation": "Toʻliq shakl otni aniqlaydi («qanday kitob?»), "
                               "qisqa shakl esa gapning kesimi boʻladi («kitob "
                               "nima boʻldi?»). Toʻliqda ikkita Н, qisqada "
                               "bitta.",
            },
            {
                "text": "Matnning oxirgi jumlasi nima demoqchi?",
                "choices": [
                    "Zerikish har doim yomon",
                    "Kolumb Markoni shaxsan bilgan",
                    "Zerikkanlikdan aytilgan hikoya ikki asrdan keyin Kolumbni okeanga joʻnatdi",
                    "Kitob juda uzoq yozilgan"
                ],
                "answer": 2,
                "explanation": "«Книга, написанная в камере от скуки, через "
                               "двести лет отправила человека через океан». "
                               "Kolumbning oʻz nusxasi, chetlariga yozgan "
                               "izohlari bilan, hozir ham saqlanadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-72 — деепричастия                                    HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Возвращаясь домой",
        "summary": (
            "PR-72 matni. Marina har kuni ishdan qaytayotib bir xil skameykani "
            "koʻradi. Bir kuni skameyka boʻsh qoladi — va u nima qilish "
            "kerakligini biladi."
        ),
        "order":   72,
        "grammar": [
            {
                "pattern":  "НСВ → -я / -ясь: bir vaqtda",
                "meaning":  "Ikki ish bir paytda ketadi — oʻzbekcha «-ib»: "
                            "возвращаясь (qaytayotib), улыбаясь (jilmayib).",
                "examples": ["Возвращаясь домой, Марина проходит мимо скамейки.",
                             "Он кормил голубей, тихо разговаривая с ними."],
            },
            {
                "pattern":  "СВ → -в / -вшись: avval bu, keyin u",
                "meaning":  "Bir ish tugab, keyin ikkinchisi boshlanadi — "
                            "oʻzbekcha «-gach»: увидев (koʻrgach), купив "
                            "(sotib olgach).",
                "examples": ["Увидев пустую скамейку, Марина остановилась.",
                             "Купив хлеб, она пошла в парк."],
            },
            {
                "pattern":  "Ega bir xil boʻlishi shart",
                "meaning":  "Ravishdoshning egasi asosiy feʼlning egasi bilan bir "
                            "xil. Matndagi har bir oborot shu qoidaga boʻysunadi: "
                            "kim qaytdi — oʻsha koʻrdi, oʻsha toʻxtadi.",
                "examples": ["Не зная, что сказать, Марина просто села рядом."],
            },
        ],
        "body": '''<p>Марина работает в аптеке. <strong>Возвращаясь домой</strong>, она каждый день проходит мимо маленького <span class="cn-word" data-tr="skver, boqcha">сквера</span>.</p>

<p>На крайней <span class="cn-word" data-tr="skameyka">скамейке</span> всегда сидит старик. Его зовут Пётр Ильич. Он <span class="cn-word" data-pos="verb" data-tr="boqadi">кормит</span> <span class="cn-word" data-tr="kaptarlar">голубей</span>, тихо <span class="cn-word" data-pos="verb" data-tr="gaplashib">разговаривая</span> с ними.</p>

<p>Сначала Марина просто <span class="cn-word" data-pos="verb" data-tr="bosh irgʻardi">кивала</span>. Потом начала здороваться. Потом — останавливаться на минуту.</p>

<p>В четверг на скамейке не было старика.</p>

<p><strong>Увидев</strong> пустую скамейку, Марина остановилась. Голуби ходили рядом и <span class="cn-word" data-pos="verb" data-tr="kutishardi">ждали</span>.</p>

<p>Она зашла в <span class="cn-word" data-tr="doʻkoncha">киоск</span> на углу и спросила про старика. Продавщица сказала, что Пётр Ильич в больнице: он <span class="cn-word" data-pos="verb" data-tr="yiqilib tushdi">упал</span> и <span class="cn-word" data-pos="verb" data-tr="shikastladi">повредил</span> <span class="cn-word" data-tr="oyogʻini">ногу</span>. Врачи сказали, что через две недели он будет дома.</p>

<p><strong>Купив</strong> буханку хлеба, Марина вернулась в сквер. Она села на крайнюю скамейку и начала <span class="cn-word" data-pos="verb" data-tr="maydalamoq">ломать</span> хлеб на маленькие <span class="cn-word" data-tr="boʻlaklar">кусочки</span>.</p>

<p>Голуби <span class="cn-word" data-pos="verb" data-tr="uchib tushishdi">слетелись</span> сразу. Они не удивились: хлеб есть хлеб.</p>

<p>Так она делала десять дней. В дождь тоже.</p>

<p>В понедельник, <strong>подходя</strong> к скверу, Марина увидела на скамейке знакомую <span class="cn-word" data-tr="qomat, siluet">фигуру</span>.</p>

<p>Пётр Ильич сидел с <span class="cn-word" data-tr="hassa">палкой</span>. Голуби уже были вокруг него.</p>

<p><strong>Не зная</strong>, что сказать, Марина просто села рядом.</p>

<p>Старик посмотрел на неё и сказал: «Спасибо. Они не <span class="cn-word" data-pos="verb" data-tr="ozib ketishdi">похудели</span>».</p>

<p>Марина засмеялась. И, <strong>улыбаясь</strong>, достала из сумки <span class="cn-word" data-tr="yarim non">полбуханки</span> хлеба.</p>''',
        "questions": [
            {
                "text": "Marina Pyotr Ilyich kasalxonaga tushganini bilgach nima qildi?",
                "choices": [
                    "Uni kasalxonada ziyorat qildi",
                    "Boshqa yoʻldan yura boshladi",
                    "Non sotib olib, oʻn kun kaptarlarni oʻzi boqdi",
                    "Qoʻshnilarga xabar berdi"
                ],
                "answer": 2,
                "explanation": "«Купив буханку хлеба, Марина вернулась в "
                               "сквер… Так она делала десять дней». Chol "
                               "qaytgach, buni «они не похудели» degan "
                               "hazil bilan tan oladi.",
            },
            {
                "text": "Nega matnda «Увидев пустую скамейку», lekin «разговаривая с ними» — biri -в, ikkinchisi -я?",
                "choices": [
                    "Chunki birinchisi СВ (avval koʻrdi, keyin toʻxtadi), ikkinchisi НСВ (bir vaqtda)",
                    "Chunki birinchisi koʻplik",
                    "Chunki ikkinchisi inkor gap",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "СВ → -в: bir ish tugaydi, keyin ikkinchisi "
                               "boshlanadi. НСВ → -я: ikkala ish bir paytda "
                               "ketadi. Chol bir vaqtning oʻzida ham boqadi, "
                               "ham gaplashadi.",
            },
            {
                "text": "Hikoyaning oxirgi jumlasi nimani koʻrsatadi?",
                "choices": [
                    "Marina kaptarlarni yoqtirmaydi",
                    "Pyotr Ilyich yana kasal boʻladi",
                    "Marina non olib kelishni unutgan",
                    "Endi kaptarlarni ikkovlashib boqishadi — Marina bekorga oʻtirmagan"
                ],
                "answer": 3,
                "explanation": "U sumkasidan yarim non chiqaradi — demak "
                               "kelishga tayyorlanib kelgan. Oʻn kunlik odat "
                               "endi ikki kishining odatiga aylandi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-73 — qisqa sifatlar                            MAKTUB-JAVOB
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Он был прав",
        "summary": (
            "PR-73 matni. Jasur Samarqandga koʻchib ketishidan oldin ikki "
            "doʻst janjallashib qolgan. Endi xat va unga javob keladi. "
            "Qisqa sifatlar — прав, виноват, рад, должен — shu yerda yashaydi."
        ),
        "order":   73,
        "grammar": [
            {
                "pattern":  "Прав · виноват · рад",
                "meaning":  "Kundalik nutqda faqat qisqa shaklda keladi: «ты был "
                            "прав», «я виноват», «я рад». «Радый» degan soʻz "
                            "umuman yoʻq.",
                "examples": ["Ты был прав, а я виноват.",
                             "Я очень рад, что ты написал."],
            },
            {
                "pattern":  "Должен — odamga moslashadi",
                "meaning":  "Erkak «должен», ayol «должна», koʻplik «должны». "
                            "Oʻzbekcha «…ishim kerak» dagi shaxs qoʻshimchasi "
                            "kabi.",
                "examples": ["Я должен был позвонить тебе раньше.",
                             "Мы должны были поговорить, а не молчать."],
            },
            {
                "pattern":  "Нужен — narsaga moslashadi",
                "meaning":  "«Мне нужен совет» (erkak), «мне нужна помощь» "
                            "(ayol). Должен bilan aynan teskari tomonga qaraydi.",
                "examples": ["Мне нужен был твой совет.",
                             "Мне нужна была твоя помощь."],
            },
        ],
        "body": '''<p><em>Самарканд, 12 марта</em></p>

<p>Бекзод, привет.</p>

<p>Я долго не писал. <span class="cn-word" data-pos="verb" data-tr="kechir">Прости</span>. Сначала был <strong>занят</strong>, потом <strong>не готов</strong>. Теперь пишу.</p>

<p>Ты был <strong>прав</strong>. Тогда, в апреле, ты сказал, что я <span class="cn-word" data-pos="verb" data-tr="shoshilyapman">спешу</span> и что <span class="cn-word" data-tr="koʻchish, joy oʻzgartirish">переезд</span> — это не <span class="cn-word" data-tr="yechim">решение</span>. Я <span class="cn-word" data-pos="verb" data-tr="jahlim chiqdi">разозлился</span> и уехал, не ответив на твоё <span class="cn-word" data-tr="xabar">сообщение</span>.</p>

<p>Я <strong>виноват</strong>. Я <strong>должен</strong> был позвонить тебе ещё в мае.</p>

<p>Здесь <span class="cn-word" data-tr="yomon emas">неплохо</span>. Работа есть, квартира маленькая, зато <span class="cn-word" data-tr="tinch">тихая</span>. Но в тот вечер мне <strong>нужен</strong> был не билет на поезд, а <span class="cn-word" data-tr="suhbat">разговор</span>. Я тогда этого не понимал.</p>

<p>В апреле у меня будет неделя <span class="cn-word" data-tr="taʼtil">отпуска</span>. Ты <strong>свободен</strong> в первых числах?</p>

<p>Жасур</p>

<p>———</p>

<p><em>Ташкент, 19 марта</em></p>

<p>Жасур!</p>

<p>Я очень <strong>рад</strong>, что ты написал. <span class="cn-word" data-tr="rostini aytsam">Честно говоря</span>, я <span class="cn-word" data-pos="verb" data-tr="kutgandim">ждал</span> этого письма одиннадцать месяцев.</p>

<p>И я <strong>не согласен</strong> с одним. Ты пишешь, что <strong>виноват</strong> ты. Но я тогда говорил <span class="cn-word" data-tr="qattiq, qoʻpol">резко</span>. Я был <strong>прав</strong> по <span class="cn-word" data-tr="mohiyat">сути</span>, но <strong>неправ</strong> по <span class="cn-word" data-tr="ohang, uslub">тону</span>. Это тоже <span class="cn-word" data-tr="xato">ошибка</span>, и она моя.</p>

<p>Так что <strong>виноваты</strong> и ты, и я. <span class="cn-word" data-pos="verb" data-tr="boʻlishamiz">Разделим</span> <span class="cn-word" data-tr="teng ikkiga">поровну</span>.</p>

<p>В апреле я <strong>свободен</strong> с первого числа. <span class="cn-word" data-pos="verb" data-tr="kel, kelib qol">Приезжай</span>. Мама уже спрашивает, сколько дней ты будешь у нас.</p>

<p>И ещё. Мне <strong>нужна</strong> твоя помощь с одним делом. Расскажу при встрече.</p>

<p>Бекзод</p>''',
        "questions": [
            {
                "text": "Nega Jasur Bekzodga xat yozdi?",
                "choices": [
                    "Yangi ish soʻrash uchun",
                    "Samarqandga koʻchishni maslahat berish uchun",
                    "Bir yil oldingi janjal uchun uzr soʻrash va uchrashuvni taklif qilish uchun",
                    "Bekzodning onasidan xabar olish uchun"
                ],
                "answer": 2,
                "explanation": "«Ты был прав… Я виноват. Я должен был позвонить "
                               "тебе ещё в мае». Xat oxirida u aprel oyida "
                               "taʼtilga chiqishini aytib, uchrashuvni taklif "
                               "qiladi.",
            },
            {
                "text": "Nega Bekzod «Я не согласен» deydi?",
                "choices": [
                    "Chunki u Jasurni koʻrmoqchi emas",
                    "Chunki aybni faqat Jasur oʻz ustiga olayotganiga qarshi — u ham xato qilgan",
                    "Chunki Jasur notoʻgʻri sanani yozgan",
                    "Chunki u Samarqandga koʻchishni maʼqullamaydi"
                ],
                "answer": 1,
                "explanation": "«Я был прав по сути, но неправ по тону. Это "
                               "тоже ошибка, и она моя». Shuning uchun "
                               "«виноваты и ты, и я».",
            },
            {
                "text": "Nega «мне нужен был не билет», lekin «мне нужна твоя помощь»?",
                "choices": [
                    "Chunki birinchisi oʻtgan zamon, ikkinchisi hozirgi",
                    "Chunki birinchisi inkor gap",
                    "Chunki ikkinchi xatni boshqa odam yozgan",
                    "Chunki «нужен» kerak boʻlgan NARSAGA moslashadi: билет erkak, помощь ayol jinsida"
                ],
                "answer": 3,
                "explanation": "Bu darsning eng katta tuzogʻi. «Нужен» odamga "
                               "emas, kerak boʻlgan narsaga qaraydi. «Должен» "
                               "esa aksincha — odamga: «я должен был "
                               "позвонить».",
            },
        ],
    },
]
