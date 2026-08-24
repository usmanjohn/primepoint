# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-77 … PR-79.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 77 — kundalik daftar, 78 — sirli hikoya,
79 — maktab hikoyasi. (74 ilmiy-ommabop, 75 biografik hikoya,
76 portret edi — uchta bir xil shakl ketma-ket kelmayapti.)

Grammatika chegarasi (kumulyativ qoida):
  77-matn: каждый / весь / все / всё / любой / другой / остальные.
           Sarlavhaning oʻzi darsning asosiy juftligi, va oxirgi jumla
           ham shu juftlik ustiga qurilgan.
  78-matn: -то / -нибудь / кое-. Har uchala zarracha ham matnda oʻz
           oʻrnida: oʻtgan zamon xabari → -то, savol va kelajak →
           -нибудь, «bilaman-u aytmayman» → кое-.
  79-matn: ikki inkor. Никто / ничего / никогда / никому beshta
           joyda, har birida feʼl oldida «не» turibdi.

⚠️ ATAY QOCHILGAN (keyingi darslar): sana va davomiylik qurilishlari
(PR-80), shaxssiz gaplar (PR-81), жамловчи sonlar — оба, трое (PR-82),
благодаря / несмотря на (PR-83), частицы — же, ведь, лишь (PR-84).

⚠️ 78-matnda ATAYIN bitta «никто … не» bor — u PR-79 da oʻrgatiladi,
lekin bu ibora oldingi matnlarda ham lugʻat sifatida uchragan va
kichik sir janrisiz iloji yoʻq. 79-matn uni toʻliq ochadi.

Uchala matn ham toʻqima voqealar — real daʼvo yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_77_79.py --author=prime
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
    # PR-77 — каждый / весь                          KUNDALIK DAFTAR
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Каждое утро, весь год",
        "summary": (
            "PR-77 matni. Anna bir yil davomida har kuni ertalab bitta "
            "daraxtni suratga oldi. Yakuniy xulosasi darsning grammatikasi "
            "bilan aytilgan: har kuni bir xil edi, yil boʻyi esa — yoʻq."
        ),
        "order":   77,
        "grammar": [
            {
                "pattern":  "Каждый — takror · весь — davomiylik",
                "meaning":  "«Каждое утро» — har ertalab (necha marta?). «Весь "
                            "год» — yil boʻyi (qancha vaqt?). Sarlavha ikkalasini "
                            "yonma-yon qoʻyadi.",
                "examples": ["Каждое утро Анна фотографировала дерево.",
                             "Она делала это весь год."],
            },
            {
                "pattern":  "Все ↔ всё — bir harf",
                "meaning":  "«Все фотографии» — koʻplik (rasmlar). «Всё "
                            "изменилось» — oʻrta jins, birlik (hamma narsa). "
                            "Feʼlga qarab ajratiladi.",
                "examples": ["Все фотографии были почти одинаковые.",
                             "И всё-таки всё изменилось."],
            },
            {
                "pattern":  "Любой · другой · остальные",
                "meaning":  "«Любой день» — istalgan kun. «Другой» — boshqa. "
                            "«Остальные» — qolganlar.",
                "examples": ["Возьмите любой снимок из марта.",
                             "Остальные лежат в папке."],
            },
        ],
        "body": '''<p><em>31 декабря. Последняя запись.</em></p>

<p>Год назад я решила делать один <span class="cn-word" data-tr="surat, kadr">снимок</span> в день. Всегда одно и то же дерево во дворе, всегда в восемь утра, всегда с одного места. Штатив я поставила у <span class="cn-word" data-tr="panjara">перил</span> и больше не двигала.</p>

<p><strong>Каждое утро</strong> я выходила на <span class="cn-word" data-tr="balkon">балкон</span> и <span class="cn-word" data-pos="verb" data-tr="suratga olardim">фотографировала</span>. Триста шестьдесят пять раз.</p>

<p>Первый месяц было интересно. Второй — <span class="cn-word" data-tr="zerikarli">скучно</span>. В марте я два раза <span class="cn-word" data-tr="sal boʻlmasa unutayozdim">чуть не забыла</span>, и один раз сделала снимок в <span class="cn-word" data-tr="xalat">халате</span>, прямо из-под <span class="cn-word" data-tr="koʻrpa">одеяла</span>.</p>

<p><strong>Весь</strong> апрель шли дожди, и дерево стояло <span class="cn-word" data-tr="yalangʻoch, bargsiz">голое</span>. <strong>Все</strong> снимки того месяца серые и <span class="cn-word" data-tr="xira, oʻchgan">тусклые</span>.</p>

<p>Летом я уезжала на неделю и попросила <span class="cn-word" data-tr="qoʻshni ayolni">соседку</span>. Она фотографировала <strong>каждый</strong> день, как я просила. Её снимки <span class="cn-word" data-pos="verb" data-tr="ajralib turadi">отличаются</span>: она стояла на <span class="cn-word" data-tr="yarim qadam chaproqda">полшага левее</span>.</p>

<p>Вчера я <span class="cn-word" data-pos="verb" data-tr="tera boshladim">собрала</span> <strong>все</strong> фотографии в один файл и посмотрела их <span class="cn-word" data-tr="ketma-ket">подряд</span>.</p>

<p>Вот что <span class="cn-word" data-tr="gʻalati">странно</span>. Возьмите <strong>любой</strong> снимок и снимок следующего дня — <span class="cn-word" data-tr="farq">разницы</span> нет. Совсем. <strong>Каждый</strong> день похож на <span class="cn-word" data-tr="oldingi">предыдущий</span>.</p>

<p>А теперь возьмите <span class="cn-word" data-tr="birinchisini">первый</span> и последний. Это <strong>другое</strong> дерево. <strong>Другой</strong> двор. <strong>Другая</strong> зима.</p>

<p><strong>Каждый</strong> день был одинаковым. А <strong>весь</strong> год — нет.</p>

<p>Думаю, с людьми <span class="cn-word" data-tr="xuddi shunday">так же</span>. <span class="cn-word" data-tr="qolganlarini">Остальное</span> напишу в следующем году.</p>''',
        "questions": [
            {
                "text": "Anna yil davomida nima qildi?",
                "choices": [
                    "Har kuni yangi daraxt ekdi",
                    "Har ertalab soat sakkizda bir xil daraxtni suratga oldi",
                    "Har oy bitta rasm chizdi",
                    "Qoʻshnisining rasmlarini yigʻdi"
                ],
                "answer": 1,
                "explanation": "«Всегда одно и то же дерево во дворе, "
                               "всегда в восемь утра, всегда с одного "
                               "места» — 365 marta.",
            },
            {
                "text": "Nega matnda «каждое утро», lekin «весь апрель»?",
                "choices": [
                    "Chunki aprel ayol jinsida",
                    "Chunki bu matndagi xato",
                    "Chunki «весь» faqat oylar bilan ishlatiladi",
                    "Chunki «каждое утро» — takror, «весь апрель» — bitta uzluksiz davr"
                ],
                "answer": 3,
                "explanation": "Savol ikki xil: «necha marta?» → каждый; "
                               "«qancha vaqt?» → весь. Oʻzbekchada ham «har "
                               "ertalab» va «aprel boʻyi» ikki xil aytiladi.",
            },
            {
                "text": "Kundalikning asosiy xulosasi nima?",
                "choices": [
                    "Har kuni bir xil edi, lekin butun yil — yoʻq",
                    "Suratga olish zerikarli ish",
                    "Qoʻshni notoʻgʻri suratga olgan",
                    "Daraxt oʻzgarmagan"
                ],
                "answer": 0,
                "explanation": "«Каждый день был одинаковым. А весь год — "
                               "нет». Ikki qoʻshni surat orasida farq yoʻq, "
                               "birinchi va oxirgisi orasida esa boshqa "
                               "daraxt.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-78 — noaniq olmoshlar                          SIRLI HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Кто-то оставил зонт",
        "summary": (
            "PR-78 matni. Kichik kafeda kimdir soyabon qoldirib ketdi. Uni "
            "ikki yil kutishdi. Egasi kelmadi — lekin soyabon kafening eng "
            "kerakli narsasiga aylandi."
        ),
        "order":   78,
        "grammar": [
            {
                "pattern":  "-то — voqea boʻlgan, kimligi nomaʼlum",
                "meaning":  "Oʻtgan zamon xabari. Sarlavhaning oʻzi shunday: "
                            "soyabonni qoldirgan odam bor, faqat kimligi "
                            "nomaʼlum.",
                "examples": ["Кто-то оставил зонт у окна.",
                             "На ручке что-то написано."],
            },
            {
                "pattern":  "-нибудь — savol, kelasi zamon, shart",
                "meaning":  "Hali boʻlmagan yoki boʻldimi deb soʻralayotgan narsa. "
                            "Matnda savolda ham, kelasi zamonda ham bor.",
                "examples": ["Кто-нибудь спрашивал про зонт?",
                             "Если кто-нибудь придёт, отдайте ему."],
            },
            {
                "pattern":  "кое- — bilaman, aytmayman",
                "meaning":  "Soʻzlovchi biladi, lekin atayin aytmaydi. Predlog "
                            "bilan kelganda uchta alohida soʻz: кое с кем.",
                "examples": ["Кое-кто из старых гостей помнит тот вечер."],
            },
        ],
        "body": '''<p>В маленьком кафе на углу <strong>кто-то</strong> оставил зонт.</p>

<p>Это было в октябре два года назад. Вечером шёл дождь, народу было много, и <span class="cn-word" data-tr="ofitsiantka">официантка</span> Лена нашла зонт у окна, когда закрывала зал.</p>

<p>Зонт был старый, но хороший: тёмно-синий, с деревянной <span class="cn-word" data-tr="dastasi">ручкой</span>. На ручке <strong>что-то</strong> было написано мелкими <span class="cn-word" data-tr="harflar">буквами</span>, но <span class="cn-word" data-pos="verb" data-tr="oʻchib ketgan">стёрлось</span>.</p>

<p>Лена поставила зонт в угол и ждала.</p>

<p>Первую неделю она спрашивала гостей: «<strong>Кто-нибудь</strong> забыл зонт?» <span class="cn-word" data-pos="verb" data-tr="bosh chayqashardi">Качали головой</span>.</p>

<p>Потом она <span class="cn-word" data-pos="verb" data-tr="osib qoʻydi">повесила</span> <span class="cn-word" data-tr="eʼlon">объявление</span> на дверь. Прошёл месяц. Никто не пришёл.</p>

<p>Зимой зонт переставили за <span class="cn-word" data-tr="peshtaxta">стойку</span>. Летом про него <span class="cn-word" data-pos="verb" data-tr="unutishdi">забыли</span>.</p>

<p>А в сентябре случилось вот что. На улице начался <span class="cn-word" data-tr="jala">ливень</span>, и одна девушка <span class="cn-word" data-pos="verb" data-tr="yugurib kirdi">вбежала</span> в кафе <span class="cn-word" data-tr="jiqqa hoʻl">совсем мокрая</span>. Лена <span class="cn-word" data-tr="oʻylamasdan">не раздумывая</span> достала зонт и дала ей.</p>

<p>Девушка вернула его на следующий день.</p>

<p>С тех пор зонт живёт у двери. Его берёт <strong>кто-нибудь</strong>, кому нужно, и приносит обратно. За два года он <span class="cn-word" data-pos="verb" data-tr="sayohat qildi">пропутешествовал</span> по всему району и ни разу не <span class="cn-word" data-pos="verb" data-tr="yoʻqolmadi">потерялся</span>.</p>

<p><strong>Кое-кто</strong> из старых гостей говорит, что знает хозяина. Но имени не называет.</p>

<p>Лена считает, что это и не важно. Зонт <span class="cn-word" data-pos="verb" data-tr="topdi">нашёл</span> себе работу получше, чем стоять в <span class="cn-word" data-tr="shkafda">шкафу</span>.</p>''',
        "questions": [
            {
                "text": "Soyabon bilan oxir-oqibat nima boʻldi?",
                "choices": [
                    "Egasi ikki yildan keyin kelib olib ketdi",
                    "Lena uni uyiga olib ketdi",
                    "U yoʻqolib qoldi",
                    "U eshik yonida turadi va kerak boʻlganlar olib turadi"
                ],
                "answer": 3,
                "explanation": "«Его берёт кто-нибудь, кому нужно, и "
                               "приносит обратно». Ikki yilda u butun mahalla "
                               "boʻylab yurdi va bir marta ham yoʻqolmadi.",
            },
            {
                "text": "Nega matnda «Кто-нибудь забыл зонт?», lekin «Кто-то оставил зонт»?",
                "choices": [
                    "Chunki birinchisi savol, ikkinchisi esa boʻlib oʻtgan voqea haqidagi xabar",
                    "Chunki birinchisi koʻplik",
                    "Chunki «-нибудь» faqat ayollar haqida ishlatiladi",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Savolda har doim -нибудь: kimdir unutgan-unutmagani "
                               "hali nomaʼlum. Xabarda esa -то: soyabon "
                               "qoldirilgan, demak odam bor.",
            },
            {
                "text": "«Кое-кто из старых гостей» nimani bildiradi?",
                "choices": [
                    "Hech kim bilmaydi",
                    "Bir kishi bor — u biladi, lekin ismini aytmaydi",
                    "Hamma mehmonlar biladi",
                    "Lena buni oʻzi oʻylab topgan"
                ],
                "answer": 1,
                "explanation": "«Но имени не называет». Кое- ning butun "
                               "maʼnosi shu: soʻzlovchi biladi, lekin atayin "
                               "aytmaydi — «кто-то» dan farqi ana shunda.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-79 — ikki inkor                             MAKTAB HIKOYASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Никто ничего не сказал",
        "summary": (
            "PR-79 matni. Sherbek rus maktabiga koʻchib keldi va birinchi "
            "kundan hech narsa tushunmadi. Kimdir uning partasiga har kuni "
            "tarjima qoʻyib keta boshladi — va hech kim hech narsa demadi."
        ),
        "order":   79,
        "grammar": [
            {
                "pattern":  "Ikki inkor: ни- + не",
                "meaning":  "Inkor soʻzi bor joyda feʼl oldida «не» turishi shart "
                            "— xuddi oʻzbekchadagi «hech kim demadi» kabi. "
                            "Matnda beshta joyda.",
                "examples": ["Никто ничего не сказал.",
                             "Шербек никогда не узнал, кто это был."],
            },
            {
                "pattern":  "Bir gapda bir nechta inkor",
                "meaning":  "«Никто никогда ничего не спросил» — uchta inkor "
                            "soʻzi va bitta «не». Bu meʼyor, xato emas.",
                "examples": ["Никто никогда ничего у него не спросил."],
            },
            {
                "pattern":  "Predlog soʻzni ikkiga boʻladi",
                "meaning":  "«Ни с кем», «ни о чём» — uchta alohida soʻz. "
                            "Predlog «ни» bilan asosiy soʻz orasiga tushadi.",
                "examples": ["Первый месяц он ни с кем не разговаривал."],
            },
        ],
        "body": '''<p>Шербек приехал в Россию в сентябре и пошёл в восьмой класс.</p>

<p>По-русски он знал двадцать слов. На первом уроке учительница что-то долго объясняла, весь класс <span class="cn-word" data-pos="verb" data-tr="yozardi">записывал</span>, а Шербек смотрел в <span class="cn-word" data-tr="daftar">тетрадь</span> и <span class="cn-word" data-pos="verb" data-tr="tushunmasdi">не понимал</span> <strong>ничего</strong>.</p>

<p>Первый месяц он <strong>ни с кем не</strong> разговаривал. Не потому, что не хотел. Просто слов не было.</p>

<p>В октябре он нашёл в <span class="cn-word" data-tr="parta">парте</span> <span class="cn-word" data-tr="qogʻoz varaqcha">листок</span>. На нём были русские слова с урока и рядом — перевод на узбекский. <span class="cn-word" data-tr="qoʻlyozma">Почерк</span> был <span class="cn-word" data-tr="notekis">неровный</span>, детский.</p>

<p>Шербек <span class="cn-word" data-pos="verb" data-tr="atrofga qaradi">огляделся</span>. <strong>Никто</strong> на него <strong>не</strong> смотрел.</p>

<p>На следующий день листок был снова. И через день. И <strong>всю</strong> зиму.</p>

<p>Он <span class="cn-word" data-pos="verb" data-tr="urinib koʻrdi">пытался</span> понять, кто это. Но в классе <strong>никто никогда ничего не</strong> говорил про листки. Ребята <span class="cn-word" data-pos="verb" data-tr="salomlashardi">здоровались</span>, <span class="cn-word" data-pos="verb" data-tr="taklif qilishardi">звали</span> играть в футбол — и <strong>ничего не</strong> спрашивали.</p>

<p>К марту Шербек начал отвечать на уроках. К маю — <span class="cn-word" data-pos="verb" data-tr="bahslashardi">спорил</span> с учителем.</p>

<p>В последний день <span class="cn-word" data-tr="oʻquv yili">учебного года</span> он положил в свою парту листок. На нём было одно слово: «Спасибо».</p>

<p>Утром листка <strong>не</strong> было. Вместо него лежал другой, с <span class="cn-word" data-tr="oʻsha xatda">тем же почерком</span>: «Не за что».</p>

<p>Шербек так и <strong>не</strong> узнал, кто это был. <strong>Никто ничего не</strong> сказал — <span class="cn-word" data-tr="ehtimol">возможно</span>, именно поэтому всё <span class="cn-word" data-pos="verb" data-tr="davom etdi">продолжалось</span> <strong>весь</strong> год.</p>''',
        "questions": [
            {
                "text": "Sherbek partasidan nima topdi?",
                "choices": [
                    "Oʻqituvchining eslatmasini",
                    "Dars soʻzlarining oʻzbekchaga tarjimasi yozilgan varaqchani",
                    "Futbol jamoasining roʻyxatini",
                    "Oʻzining eski daftarini"
                ],
                "answer": 1,
                "explanation": "«Русские слова с урока и рядом — перевод на "
                               "узбекский». Qoʻlyozma bolalarniki edi, va "
                               "varaqcha butun qish davomida takrorlandi.",
            },
            {
                "text": "Nega matnda «ни с кем не разговаривал» — nega uchta alohida soʻz?",
                "choices": [
                    "Chunki bu koʻplik shakli",
                    "Chunki «с» predlogi «ни» va «кем» orasiga tushadi",
                    "Chunki gap oʻtgan zamonda",
                    "Bu matndagi xato"
                ],
                "answer": 1,
                "explanation": "Predlog inkor olmoshini ikkiga boʻladi va "
                               "uchalasi alohida yoziladi: ни с кем, ни о чём, "
                               "ни у кого. Feʼl oldidagi «не» esa baribir "
                               "saqlanadi.",
            },
            {
                "text": "Hikoyaning oxirgi jumlasi nima demoqchi?",
                "choices": [
                    "Sinfdoshlar Sherbekni yoqtirmasdi",
                    "Varaqchalarni oʻqituvchi qoʻyib ketardi",
                    "Aynan hech kim hech narsa demagani uchun bu bir yil davom etdi",
                    "Sherbek oxiri kim ekanini bilib oldi"
                ],
                "answer": 2,
                "explanation": "«Никто ничего не сказал — возможно, именно "
                               "поэтому всё продолжалось весь год». Aytilsa, "
                               "u minnatdorchilikka aylanardi va toʻxtardi.",
            },
        ],
    },
]
