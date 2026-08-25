# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-80 … PR-82.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.
⛔ URGʻU BELGISI YOʻQ — 2026-08-24 dagi qaror. Bu birinchi batch, u
   boshidanoq belgisiz yozilgan. Darsliklar esa urgʻuni saqlaydi.

Janr xilma-xilligi: 80 — ilmiy-ommabop, 81 — qish kundaligi (sanali
yozuvlar), 82 — sayohat hikoyasi. (77 kundalik daftar, 78 sirli hikoya,
79 maktab hikoyasi edi.) 81 ham kundalik, lekin 77 dan farqli: u bitta
yakuniy yozuv edi, bu esa qish boʻyi choʻzilgan beshta qisqa yozuv.

Grammatika chegarasi (kumulyativ qoida):
  80-matn: vaqt qurilishlari — за / через / на, davomiylik Вин.п. da,
           yosh Дат.п. da, «раз в …» takrori va sanalar.
  81-matn: shaxssiz gaplar — темнеет, светает, мне холодно, не спится,
           хочется, времени нет, занесло снегом. Har bir yozuvda kamida
           bittasi bor.
  82-matn: jamlovchi va tartib sonlar — трое, вдвоём, втроём, оба/обе,
           первый / второй / третий день, полтора.

⚠️ ATAY QOCHILGAN (keyingi darslar): благодаря / несмотря на (PR-83),
частицы — же, ведь, лишь (PR-84), soʻzlashuv qisqartmalari (PR-85).

⚠️ FAKTLAR (80-matn tekshirilgan):
  · Quyosh nuri Yergacha ~8 daqiqa 20 soniyada yetadi;
  · qon tanachasi butun tanani ~1 daqiqada aylanib chiqadi;
  · XKS (ISS) Yer atrofini ~90 daqiqada aylanadi;
  · Proksima Kentavradan nur ~4,2 yilda keladi;
  · odat shakllanishi uchun oʻrtacha ~66 kun kerak (Lally va boshqalar,
    2009) — mashhur «21 kun» raqami ilmiy asosga ega emas;
  · «Voyager-1» eng yaqin yulduzgacha shu tezlikda ~70 000 yil yurardi.
  81 va 82 — toʻqima voqealar, real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_80_82.py --author=prime
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
    # PR-80 — vaqt qurilishlari                       ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Сколько времени нужно, чтобы…",
        "summary": (
            "PR-80 matni. Quyosh nuri Yergacha sakkiz daqiqada keladi, qon "
            "tanani bir daqiqada aylanadi, odat esa oʻrtacha oltmish olti "
            "kunda shakllanadi. Barcha raqamlar haqiqiy."
        ),
        "order":   80,
        "grammar": [
            {
                "pattern":  "За + Вин.п. — shuncha vaqt ichida",
                "meaning":  "Ish qancha vaqtda bajarilgani. Oʻzbekcha «sakkiz "
                            "daqiqada». Matnning butun tuzilishi shu predlog "
                            "ustiga qurilgan.",
                "examples": ["Свет доходит до Земли за восемь минут.",
                             "Кровь обходит всё тело за одну минуту."],
            },
            {
                "pattern":  "Через + Вин.п. — shuncha vaqtdan keyin",
                "meaning":  "«За» bilan adashtirmang: «за» — ichida bajarildi, "
                            "«через» — keyin sodir boʻladi.",
                "examples": ["Через полтора часа станция снова над нами."],
            },
            {
                "pattern":  "Davomiylik — predlogsiz Вин.п.",
                "meaning":  "«Три года», «весь день» — vaqt oddiy Вин.п. da "
                            "turadi, hech qanday predlog qoʻyilmaydi.",
                "examples": ["Учёные наблюдали за людьми двенадцать недель."],
            },
        ],
        "body": '''<p>Мы плохо <span class="cn-word" data-pos="verb" data-tr="tasavvur qilamiz">представляем</span> себе время. <span class="cn-word" data-tr="soniya">Секунда</span> кажется нам короткой, год — длинным. А на самом деле всё интереснее.</p>

<p><strong>Восемь минут двадцать секунд.</strong> <span class="cn-word" data-tr="shuncha">Столько</span> идёт свет от Солнца до Земли. Если Солнце вдруг <span class="cn-word" data-pos="verb" data-tr="oʻchib qolsa">погаснет</span>, мы узнаем об этом только <strong>через</strong> восемь минут.</p>

<p><strong>Одна минута.</strong> <strong>За</strong> это время <span class="cn-word" data-tr="qon">кровь</span> <span class="cn-word" data-pos="verb" data-tr="ulguradi">успевает</span> обойти всё <span class="cn-word" data-tr="tana">тело</span> и вернуться к <span class="cn-word" data-tr="yurakka">сердцу</span>. Пока вы читаете эту страницу, она сделает круг два или три раза.</p>

<p><strong>Полтора часа.</strong> Столько нужно <span class="cn-word" data-tr="kosmik stansiyaga">космической станции</span>, чтобы <span class="cn-word" data-pos="verb" data-tr="aylanib chiqmoq">облететь</span> Землю. Люди на ней видят <span class="cn-word" data-tr="quyosh chiqishi">восход солнца</span> шестнадцать <strong>раз в сутки</strong>.</p>

<p><strong>Шестьдесят шесть дней.</strong> Вот это самое <span class="cn-word" data-tr="kutilmagan">неожиданное</span>. Все слышали, что <span class="cn-word" data-tr="odat">привычка</span> появляется <strong>за</strong> двадцать один день. Учёные <span class="cn-word" data-pos="verb" data-tr="kuzatishdi">наблюдали</span> за людьми двенадцать недель и получили другое <span class="cn-word" data-tr="raqam, son">число</span>: <span class="cn-word" data-tr="oʻrtacha">в среднем</span> <strong>шестьдесят шесть дней</strong>. У кого-то сорок, у кого-то больше двухсот.</p>

<p>Двадцать один день — красивая цифра, но она <span class="cn-word" data-tr="hech narsani">ничего</span> не <span class="cn-word" data-pos="verb" data-tr="isbotlamaydi">доказывает</span>.</p>

<p><strong>Четыре года и два месяца.</strong> Столько летит свет от <span class="cn-word" data-tr="eng yaqin yulduzdan">ближайшей звезды</span> — Проксимы Центавра. Мы видим её такой, какой она была <strong>четыре года назад</strong>.</p>

<p><strong>Семьдесят тысяч лет.</strong> Столько шёл бы туда «Вояджер-1», если бы <span class="cn-word" data-pos="verb" data-tr="uchsa edi">летел</span> в её сторону. Он летит уже почти пятьдесят лет и пока не вышел даже <span class="cn-word" data-tr="qoʻshni yulduzgacha">до соседней звезды</span>.</p>

<p>Вот что <span class="cn-word" data-pos="verb" data-tr="qiziq boʻlib chiqadi">получается интересно</span>. Свет от Солнца — восемь минут. Привычка — шестьдесят шесть дней. Звезда — четыре года.</p>

<p>Самое короткое здесь — <span class="cn-word" data-tr="koinot">космос</span>. Самое долгое — человек.</p>''',
        "questions": [
            {
                "text": "Odat shakllanishi uchun aslida qancha vaqt kerak?",
                "choices": [
                    "Yigirma bir kun",
                    "Oʻrtacha oltmish olti kun",
                    "Oʻn ikki hafta",
                    "Ikki yuz kun"
                ],
                "answer": 1,
                "explanation": "Olimlar odamlarni oʻn ikki hafta kuzatib, "
                               "oʻrtacha 66 kun degan raqamni olishgan. "
                               "Mashhur «21 kun» esa chiroyli raqam, xolos — "
                               "matn buni ochiq aytadi.",
            },
            {
                "text": "Nega matnda «за восемь минут», lekin «через восемь минут»?",
                "choices": [
                    "Chunki birinchisi koʻplik",
                    "Ikkalasi bir xil, farqi yoʻq",
                    "Chunki «через» faqat kelasi zamonda ishlatiladi",
                    "«За» — nur shuncha vaqt ichida yetadi; «через» — shuncha vaqtdan keyin bilib qolamiz"
                ],
                "answer": 3,
                "explanation": "«За» ish qancha vaqtda bajarilganini, «через» "
                               "esa qancha vaqtdan keyin sodir boʻlishini "
                               "bildiradi. Oʻzbekcha «sakkiz daqiqada» ↔ "
                               "«sakkiz daqiqadan keyin».",
            },
            {
                "text": "Matnning oxirgi jumlasi nimani aytmoqchi?",
                "choices": [
                    "Koinot juda kichkina",
                    "Odam koinotdan tez oʻzgaradi",
                    "Koinotdagi masofalar odam odatidan tezroq bosib oʻtiladi",
                    "Yulduzgacha yetish oson"
                ],
                "answer": 2,
                "explanation": "«Самое короткое здесь — космос. Самое долгое — "
                               "человек». Quyoshdan nur sakkiz daqiqada "
                               "keladi, odat esa oltmish olti kun talab "
                               "qiladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-81 — shaxssiz gaplar                          QISH KUNDALIGI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Темнеет рано",
        "summary": (
            "PR-81 matni. Anna Norilskda ishlaydigan ukasining oldiga qishga "
            "kelgan va kundalik tutgan. Beshta qisqa yozuv — noyabrdan "
            "fevralgacha, qutb tuni boshlanib, tugagunicha."
        ),
        "order":   81,
        "grammar": [
            {
                "pattern":  "Tabiat: темнеет · светает · морозит",
                "meaning":  "Egasi umuman yoʻq. Kim qorongʻilashtiryapti — savol "
                            "berilmaydi. Oʻtgan zamonda oʻrta jins: стемнело.",
                "examples": ["В ноябре здесь темнеет в два часа дня.",
                             "К февралю снова начало светать."],
            },
            {
                "pattern":  "Holat: мне холодно · мне не спится",
                "meaning":  "Odam Дательный da turadi — oʻzbekcha «menga sovuq» "
                            "dagi -ga. Feʼl har doim oʻrta jinsda: было.",
                "examples": ["Мне было холодно даже в двух свитерах.",
                             "Мне не спится, когда за окном светло."],
            },
            {
                "pattern":  "Kuch Творительный da",
                "meaning":  "«Дорогу занесло снегом» — shamol yoki qor ega emas, "
                            "u qurol kabi Творительный da turadi, feʼl esa "
                            "oʻrta jinsda.",
                "examples": ["Ночью дорогу занесло снегом."],
            },
        ],
        "body": '''<p><em>12 ноября</em></p>

<p><span class="cn-word" data-pos="verb" data-tr="uchib keldim">Прилетела</span> вчера. Брат работает здесь второй год, а я приехала на два месяца — <span class="cn-word" data-pos="verb" data-tr="koʻrmoq">посмотреть</span>, как люди тут живут.</p>

<p>Первое, что я поняла: <strong>темнеет</strong> в два часа дня. Не вечером. Днём.</p>

<p><em>28 ноября</em></p>

<p>Сегодня началась <span class="cn-word" data-tr="qutb tuni">полярная ночь</span>. Солнце не <span class="cn-word" data-pos="verb" data-tr="chiqmaydi">встанет</span> до января.</p>

<p><strong>Мне было холодно</strong> даже в двух <span class="cn-word" data-tr="sviterda">свитерах</span>, и брат <span class="cn-word" data-pos="verb" data-tr="kuldi">засмеялся</span>. Он говорит, что <strong>к холоду привыкают</strong> за три недели, а к <span class="cn-word" data-tr="qorongʻilikka">темноте</span> — никогда.</p>

<p><em>19 декабря</em></p>

<p>Ночью <strong>дорогу занесло снегом</strong>, и утром <span class="cn-word" data-tr="avtobuslar">автобусы</span> не пошли. <span class="cn-word" data-tr="ishga">На работу</span> люди шли пешком, <span class="cn-word" data-tr="qator boʻlib">цепочкой</span>, по одной <span class="cn-word" data-tr="yoʻlakcha">тропинке</span>.</p>

<p><strong>Мне не спится</strong> здесь. Не потому, что <span class="cn-word" data-tr="shovqinli">шумно</span>. Просто <span class="cn-word" data-tr="tana">тело</span> не понимает, когда ночь, а когда день.</p>

<p>Брат дал мне <span class="cn-word" data-tr="maxsus chiroq">специальную лампу</span>. <strong>Говорят</strong>, она <span class="cn-word" data-pos="verb" data-tr="oʻrnini bosadi">заменяет</span> солнце. Не знаю. Но <strong>стало легче</strong>.</p>

<p><em>14 января</em></p>

<p>Сегодня в городе <span class="cn-word" data-tr="bayram">праздник</span>. Солнце вышло на сорок минут.</p>

<p>Все вышли на улицу. <span class="cn-word" data-tr="notanish">Незнакомые</span> люди <span class="cn-word" data-pos="verb" data-tr="tabriklashardi">поздравляли</span> друг друга. <strong>Мне хотелось</strong> <span class="cn-word" data-pos="verb" data-tr="yigʻlamoq">плакать</span>, и я не понимала почему.</p>

<p><em>3 февраля</em></p>

<p>Уезжаю через неделю. <strong>Светает</strong> уже в девять, и это кажется мне <span class="cn-word" data-tr="moʻjiza">чудом</span>.</p>

<p>Брат сказал одну вещь. <strong>Здесь не спрашивают</strong>, какая погода. Здесь спрашивают, есть ли свет.</p>''',
        "questions": [
            {
                "text": "Nima uchun Anna Norilskga kelgan?",
                "choices": [
                    "Ishga joylashish uchun",
                    "Qutb tunini oʻrganish uchun",
                    "Ukasining oldiga, odamlar u yerda qanday yashashini koʻrgani",
                    "Kasalxonada davolanish uchun"
                ],
                "answer": 2,
                "explanation": "«Брат работает здесь второй год, а я приехала "
                               "на два месяца — посмотреть, как люди тут "
                               "живут».",
            },
            {
                "text": "Nega matnda «мне было холодно», «мне не спится» — nega «я» emas?",
                "choices": [
                    "Chunki bular shaxssiz gaplar: odam Дательный da turadi",
                    "Chunki Anna ayol",
                    "Chunki gap oʻtgan zamonda",
                    "Bu kundalikdagi xato"
                ],
                "answer": 0,
                "explanation": "Holat gapida ega umuman yoʻq, odam esa chetda "
                               "«kimga?» shaklida turadi — xuddi oʻzbekcha "
                               "«men<b>ga</b> sovuq» kabi. Feʼl ham shuning "
                               "uchun oʻrta jinsda: «было», «была» emas.",
            },
            {
                "text": "Ukasining oxirgi gapi nimani anglatadi?",
                "choices": [
                    "Norilskda ob-havo hech qachon oʻzgarmaydi",
                    "U yerda odamlar ob-havo emas, yorugʻlik haqida soʻrashadi",
                    "Qishda gaplashish qiyin",
                    "Chiroq quyoshning oʻrnini bosadi"
                ],
                "answer": 1,
                "explanation": "«Здесь не спрашивают, какая погода. Здесь "
                               "спрашивают, есть ли свет». Qutb tunida asosiy "
                               "savol — sovuq emas, yorugʻlik.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-82 — jamlovchi va tartib sonlar             SAYOHAT HIKOYASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Трое в лодке",
        "summary": (
            "PR-82 matni. Uch doʻst daryoda uch kunlik qayiq sayohatiga "
            "chiqadi. Sarlavha Jerom K. Jeromning mashhur kitobiga ishora — "
            "voqea esa toʻqima."
        ),
        "order":   82,
        "grammar": [
            {
                "pattern":  "Jamlovchi sonlar: трое · вдвоём · втроём",
                "meaning":  "«Нас было трое» — bizlar uchta edik. «Втроём» esa "
                            "«uchovlashib» — feʼlni aniqlaydi. Oʻzbekcha "
                            "«-alasi / -ovlashib».",
                "examples": ["Нас было трое.", "Дальше мы гребли вдвоём."],
            },
            {
                "pattern":  "Оба / обе — «ikkalasi ham»",
                "meaning":  "Erkak va oʻrta jinsda «оба», ayol jinsida «обе». "
                            "Oddiy «два» dan kuchliroq: biri ham qolmadi.",
                "examples": ["Оба весла были старые.", "Обе карты оказались неточными."],
            },
            {
                "pattern":  "Tartib sonlar: первый · второй · третий",
                "meaning":  "Sifat kabi turlanadi. «Третий» — yagona istisno, "
                            "yumshoq namunada: третьего, третьем.",
                "examples": ["В первый день всё шло хорошо.",
                             "На третье утро мы проснулись от тишины."],
            },
        ],
        "body": '''<p>Нас было <strong>трое</strong>: Жасур, Бекзод и я. И одна лодка.</p>

<p>План был простой. <span class="cn-word" data-pos="verb" data-tr="suzib oʻtmoq">Пройти</span> по реке шестьдесят километров за три дня. <strong>Обе</strong> карты, которые мы взяли, показывали одно и то же: река спокойная, <span class="cn-word" data-tr="toʻsiqlar">препятствий</span> нет.</p>

<p><strong>В первый день</strong> всё шло хорошо. Мы гребли <strong>втроём</strong>, по очереди, и прошли двадцать два километра. Вечером <span class="cn-word" data-pos="verb" data-tr="chodir tikdik">поставили палатку</span> и съели <strong>полторы</strong> <span class="cn-word" data-tr="qozon">кастрюли</span> <span class="cn-word" data-tr="grechka boʻtqasi">гречки</span>.</p>

<p><strong>На второй день</strong> <span class="cn-word" data-pos="verb" data-tr="sindi">сломалось</span> весло. Бекзод сказал, что <strong>оба</strong> весла были старые и он это ещё в городе заметил. Жасур спросил, почему он тогда <span class="cn-word" data-pos="verb" data-tr="jim turgan">молчал</span>.</p>

<p>Дальше мы гребли <strong>вдвоём</strong>, а <strong>третий</strong> <span class="cn-word" data-pos="verb" data-tr="dam olardi">отдыхал</span>. Меняясь каждые полчаса, мы прошли ещё восемнадцать километров.</p>

<p><strong>На третье утро</strong> мы проснулись от <span class="cn-word" data-tr="jimlikdan">тишины</span>. Река стала <span class="cn-word" data-tr="keng">широкой</span> и почти не двигалась. Грести пришлось <span class="cn-word" data-tr="ikki baravar koʻp">вдвое больше</span>.</p>

<p>До моста оставалось двадцать километров, а времени — полдня.</p>

<p>Жасур предложил идти до темноты и не останавливаться на обед. <strong>Оба</strong> мы согласились, хотя есть хотелось всем <strong>троим</strong>.</p>

<p>Мы дошли в семь вечера — <span class="cn-word" data-tr="rejadan uch soat kech">на три часа позже плана</span>. <span class="cn-word" data-tr="uchalamiz ham">Все трое</span> <span class="cn-word" data-pos="verb" data-tr="jim edik">молчали</span> последний час, и не от <span class="cn-word" data-tr="janjaldan">ссоры</span>.</p>

<p><span class="cn-word" data-tr="qizigʻi shundaki">Смешно вот что</span>. Мы помним не реку и не мост. Мы помним, как <strong>втроём</strong> ели <strong>одну</strong> <span class="cn-word" data-tr="kosa">миску</span> гречки, потому что <strong>обе</strong> остальные <span class="cn-word" data-pos="verb" data-tr="suvga tushib ketdi">упали в воду</span>.</p>''',
        "questions": [
            {
                "text": "Nima uchun ikkinchi kundan boshlab ikki kishi eshkak eshdi?",
                "choices": [
                    "Uchinchisi kasal boʻlib qoldi",
                    "Daryo torayib qoldi",
                    "Eshkaklardan biri sindi",
                    "Ular tezroq yurmoqchi edi"
                ],
                "answer": 2,
                "explanation": "«На второй день сломалось весло». Bekzod ikkala "
                               "eshkak ham eski ekanini shaharda payqagan, "
                               "lekin aytmagan.",
            },
            {
                "text": "Nega matnda «обе карты», lekin «оба весла»?",
                "choices": [
                    "Chunki xaritalar ikkita, eshkaklar uchta edi",
                    "Chunki «карта» ayol jinsida, «весло» esa oʻrta jinsda",
                    "Chunki xaritalar muhimroq",
                    "Bu matndagi xato"
                ],
                "answer": 1,
                "explanation": "«Обе» — ayol jinsi uchun, «оба» — erkak va oʻrta "
                               "jins uchun. Eslatma: «обЕ» ichidagi Е — "
                               "«жЕнский» dagi Е.",
                },
            {
                "text": "Uchala doʻst bu sayohatdan nimani eslab qolishdi?",
                "choices": [
                    "Koʻprikni va daryoni",
                    "Oltmish kilometr masofani",
                    "Sinib qolgan eshkakni",
                    "Bitta kosadan uchovlashib grechka yeganlarini"
                ],
                "answer": 3,
                "explanation": "«Мы помним не реку и не мост. Мы помним, как "
                               "втроём ели одну миску гречки». Qolgan ikkala "
                               "kosa suvga tushib ketgan edi.",
            },
        ],
    },
]
