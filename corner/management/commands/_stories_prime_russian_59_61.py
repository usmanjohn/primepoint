# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-59 … PR-61.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 59 — qoʻllanma (buyruq shakllari bilan), 60 — maslahat
xati, 61 — tarixiy matn. (56 sayohat qaydlari, 57 ilmiy-ommabop, 58 hikoya
edi.) 59 PR-27 dagi «Правила библиотеки» ga oʻxshaydi, lekin shakli
boshqa: u qoidalar roʻyxati edi, bu esa odamga qaratilgan yoʻriqnoma.

⚠️ FAKTLAR (61-matn). Peterburg haqidagi daʼvolar tekshirilgan va ehtiyot
bilan tanlangan: shahar 1703-yilda Pyotr I tomonidan asos solingan;
Neva deltasidagi botqoq yerda qurilgan; birinchi qurilgan narsa qalʼa
boʻlgan; 1712-yilda poytaxtga aylangan; qurilish ogʻir sharoitda kechgan
va koʻp odam halok boʻlgan. ANIQ qurbonlar soni ATAY aytilmagan —
manbalarda u juda har xil va bahsli.

Grammatika chegarasi (kumulyativ qoida):
  59-matn: buyruq mayli. НСВ (умумий taklif) va СВ (aniq vazifa) yonma-yon,
           va inkor buyruqda НСВ.
  60-matn: бы. Xat janri ideal — maslahat, afsus va muloyim taklif
           hammasi shartli maylda beriladi.
  61-matn: majhul nisbat. Tarixiy matnda bajaruvchi koʻpincha muhim emas,
           shuning uchun «был построен» tabiiy chiqadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_59_61.py --author=prime
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
    # PR-59 — buyruq mayli                       QOʻLLANMA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Инструкция для нового сотрудника",
        "summary": (
            "PR-59 matni. Yangi xodim uchun eslatma varaqasi: qachon kelish, "
            "kalitni kimdan olish, kofe qoidasi. Oxirgi band eslatmaning oʻzi "
            "haqida."
        ),
        "order":   59,
        "grammar": [
            {
                "pattern":  "Buyruq: -Й / -И / -Ь",
                "meaning":  "«Они» shaklidan yasaladi: читают → читай, говорят → "
                            "говори, готовят → готовь. ВЫ shakli -ТЕ qoʻshadi. "
                            "Oʻzbekcha oʻqi! / oʻqing! bilan bir xil tizim.",
                "examples": ["Приходите в девять.", "Возьмите ключ."],
            },
            {
                "pattern":  "Inkor buyruqda НСВ",
                "meaning":  "Не опаздывайте, не теряйте, не бойтесь — inkor "
                            "buyruqda deyarli har doim tugallanmagan feʼl. Bu "
                            "taqiq maʼnosini beradi.",
                "examples": ["Не опаздывайте.", "Не бойтесь ошибаться."],
            },
            {
                "pattern":  "НСВ ↔ СВ buyruqda",
                "meaning":  "Спрашивайте (umumiy taklif — har doim shunday qiling) "
                            "va прочитайте (aniq vazifa — bir marta, oxirigacha). "
                            "Oxirgi band ikkalasini yonma-yon qoʻyadi.",
                "examples": ["Спрашивайте. Это нормально.", "Прочитайте один раз."],
            },
        ],
        "body": '''<p>Здравствуйте! Вы — новый <span class="cn-word" data-tr="xodim">сотрудник</span>. Вот <span class="cn-word" data-tr="eslatma varaqasi">памятка</span>.</p>

<p><strong>Приходите</strong> в девять. <strong>Не опаздывайте</strong> — это важно только в первую неделю. Потом уже не очень.</p>

<p><strong>Возьмите</strong> <span class="cn-word" data-tr="kalit">ключ</span> у Нины Петровны. <strong>Не теряйте</strong> его.</p>

<p>Кофе — на кухне. <strong>Пейте</strong> сколько хотите. Но <strong>помойте</strong> <span class="cn-word" data-tr="chashka">чашку</span>.</p>

<p><strong>Пишите</strong> письма <span class="cn-word" data-tr="qisqa">коротко</span>. <span class="cn-word" data-tr="Uzun">Длинные</span> письма никто не читает.</p>

<p>Что-то <span class="cn-word" data-tr="tushunarsiz">непонятно</span>? <strong>Спрашивайте</strong>. Это нормально.</p>

<p><strong>Не бойтесь</strong> <span class="cn-word" data-pos="verb" data-tr="xato qilmoq">ошибаться</span>. В первый месяц ошибка — это не ошибка, а <span class="cn-word" data-tr="oʻqish">учёба</span>.</p>

<p>В <span class="cn-word" data-tr="juma">пятницу</span> мы пьём чай вместе в четыре. <strong>Приходите</strong>.</p>

<p>И <span class="cn-word" data-tr="oxirgisi">последнее</span>.</p>

<p><strong>Не читайте</strong> эту памятку каждый день.</p>

<p><strong>Прочитайте</strong> один раз — и <strong>работайте</strong>.</p>''',
        "questions": [
            {
                "text": "Eslatmaning oxirgi bandi nima deydi?",
                "choices": [
                    "Eslatmani bir marta oʻqib, ishga kirishing kerak",
                    "Eslatmani har kuni oʻqish kerak",
                    "Eslatmani saqlab qoʻyish kerak",
                    "Eslatma keraksiz"
                ],
                "answer": 0,
                "explanation": "«Не читайте эту памятку каждый день. Прочитайте "
                               "один раз — и работайте». Ikki buyruq, ikki vid: "
                               "takrorni taqiqlaydi (НСВ) va bitta aniq vazifa "
                               "beradi (СВ).",
            },
            {
                "text": "Nega matnda «не читайте», lekin «прочитайте»?",
                "choices": [
                    "Inkor buyruqda НСВ, aniq vazifada esa СВ ishlatiladi",
                    "Ikkalasi bir xil",
                    "Birinchisi hurmat shakli",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Inkor buyruq deyarli har doim НСВ oladi — bu taqiq. "
                               "«Прочитайте один раз» esa bir martalik aniq vazifa, "
                               "demak СВ.",
            },
            {
                "text": "Eslatma xatolar haqida nima deydi?",
                "choices": [
                    "Birinchi oyda xato — bu xato emas, oʻqish",
                    "Xato qilish taqiqlanadi",
                    "Xatolar uchun jarima bor",
                    "Xatolar haqida hech narsa aytilmagan"
                ],
                "answer": 0,
                "explanation": "«Не бойтесь ошибаться. В первый месяц ошибка — "
                               "это не ошибка, а учёба». Eslatmaning ohangi qatʼiy "
                               "emas — u yangi odamni tinchlantirmoqchi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-60 — бы                                 MASLAHAT XATI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Если бы я знал раньше",
        "summary": (
            "PR-60 matni. Oleg amaki jiyaniga maslahat soʻragan xatiga javob "
            "yozadi. Uchta maslahat beradi — va oxirida ularning barchasini "
            "bekor qiladi."
        ),
        "order":   60,
        "grammar": [
            {
                "pattern":  "если бы …, … бы",
                "meaning":  "Noreal shart: ikkala qismda ham БЫ va oʻtgan zamon. "
                            "«Если бы я мог вернуться, я бы сделал» — qaytib "
                            "bora olmayman, shuning uchun qilmadim ham.",
                "examples": ["Если бы я мог вернуться, я бы сделал три вещи."],
            },
            {
                "pattern":  "я бы + oʻtgan zamon",
                "meaning":  "Shartli mayl faqat oʻtgan zamon bilan yasaladi va "
                            "tuslanmaydi. Jinsga qaraydi: я бы сделал (erkak), "
                            "я бы сделала (ayol).",
                "examples": ["Я бы больше слушал.", "Я бы звонил чаще."],
            },
            {
                "pattern":  "на твоём месте",
                "meaning":  "Maslahat berishning eng muloyim yoʻli — chunki bu buyruq "
                            "emas. Rasmiy shakli: на вашем месте.",
                "examples": ["На твоём месте я бы не спрашивал совета."],
            },
        ],
        "body": '''<p>Дорогой Жасур!</p>

<p>Ты <span class="cn-word" data-pos="verb" data-tr="soʻrayapsan">просишь</span> <span class="cn-word" data-tr="maslahat">совета</span>. Я не знаю, что сказать. Но я скажу так.</p>

<p><strong>Если бы</strong> я мог <span class="cn-word" data-pos="verb" data-tr="qaytmoq">вернуться</span> в двадцать лет, я <strong>бы</strong> сделал три вещи.</p>

<p><span class="cn-word" data-tr="Birinchidan">Первое</span>. Я <strong>бы</strong> <span class="cn-word" data-tr="koʻproq">больше</span> слушал и <span class="cn-word" data-tr="kamroq">меньше</span> говорил.</p>

<p>Второе. Я <strong>бы</strong> не боялся ошибаться. <span class="cn-word" data-tr="Xato">Ошибка</span> — это не <span class="cn-word" data-tr="oxir">конец</span>. Это <span class="cn-word" data-tr="shunchaki">просто</span> день.</p>

<p>Третье. Я <strong>бы</strong> звонил бабушке <span class="cn-word" data-tr="tez-tezroq">чаще</span>.</p>

<p>Но я не могу вернуться. И ты не можешь взять мой <span class="cn-word" data-tr="tajriba">опыт</span> — он не работает в чужих руках.</p>

<p><strong>На твоём месте</strong> я <strong>бы</strong> не спрашивал совета. Я <strong>бы</strong> просто начал.</p>

<p>И вот ещё что.</p>

<p><strong>Если бы</strong> мне сказали всё это в двадцать лет, я <strong>бы</strong> не понял.</p>

<p>Поэтому не слушай меня. Иди и делай.</p>

<p>Твой дядя Олег</p>''',
        "questions": [
            {
                "text": "Xat oxirida Oleg amaki nima deydi?",
                "choices": [
                    "Meni tinglama — borib qil",
                    "Har kuni menga yoz",
                    "Buvingga qoʻngʻiroq qil",
                    "Universitetga kir"
                ],
                "answer": 0,
                "explanation": "«Не слушай меня. Иди и делай». U uchta maslahat "
                               "beradi, keyin oʻzi ularni bekor qiladi — chunki yigirma "
                               "yoshda oʻzi ham bunday gaplarni tushunmagan boʻlardi.",
            },
            {
                "text": "«Если бы мне сказали всё это в двадцать лет, я бы не "
                        "понял» — bu jumla nimani anglatadi?",
                "choices": [
                    "Maslahat faqat tajriba orttirgandan keyin tushuniladi",
                    "Hech kim unga hech narsa aytmagan",
                    "U yigirma yoshda emas edi",
                    "U maslahatni yomon koʻradi"
                ],
                "answer": 0,
                "explanation": "Bu xatning butun mantigʻi: maslahat berish oson, lekin "
                               "u qabul qilinishi uchun odam tayyor boʻlishi kerak. "
                               "Shuning uchun oxirgi maslahat — maslahat "
                               "soʻramaslik.",
            },
            {
                "text": "Nega matnda «я бы сделал», «я бы сделаю» emas?",
                "choices": [
                    "БЫ faqat oʻtgan zamon bilan ishlatiladi",
                    "Chunki bu koʻplik",
                    "Chunki gapirayotgan odam erkak",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Shartli mayl — oʻtgan zamon + БЫ. Boshqa zamon bilan "
                               "ishlatilmaydi. Shakl faqat jinsga qaraydi: erkak "
                               "«сделал бы», ayol «сделала бы».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-61 — majhul nisbat                      TARIXIY MATN
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Как был построен Петербург",
        "summary": (
            "PR-61 matni. 1703-yil, Neva deltasidagi botqoq — va uning ustida "
            "qurilgan shahar. Matn oxirida botqoq hali ham oʻsha yerda ekani "
            "eslatiladi."
        ),
        "order":   61,
        "grammar": [
            {
                "pattern":  "был построен — natija",
                "meaning":  "Qisqa sifatdosh + БЫТЬ. Egaga moslashadi: был "
                            "построен (erkak), была построена (ayol), были "
                            "построены (koʻplik).",
                "examples": ["Петербург был построен на болоте.", "Была построена крепость."],
            },
            {
                "pattern":  "строился — jarayon",
                "meaning":  "НСВ + -СЯ majhul nisbatning jarayon shakli: «город "
                            "строился много лет» — qurilish davom etgan, natija "
                            "hali yoʻq.",
                "examples": ["Город строился много лет."],
            },
            {
                "pattern":  "Bajaruvchi — Творительный",
                "meaning":  "Kim qilgani aytilsa, u Творительный'ga kiradi: "
                            "«построен людьми». Oʻzbekchada bu «odamlar TOMONIDAN» "
                            "boʻlardi.",
                "examples": ["Город был построен людьми."],
            },
        ],
        "body": '''<p>Петербург <strong>был построен</strong> на <span class="cn-word" data-tr="botqoq">болоте</span>.</p>

<p>В 1703 году Пётр Первый <span class="cn-word" data-pos="verb" data-tr="asos soldi">основал</span> здесь город.</p>

<p><span class="cn-word" data-tr="Joy">Место</span> было <span class="cn-word" data-tr="yomon">плохое</span>: вода, болото, холод, <span class="cn-word" data-tr="shamol">ветер</span>.</p>

<p>Но место было важное: здесь река Нева идёт в море.</p>

<p>Сначала <strong>была построена</strong> <span class="cn-word" data-tr="qalʼa">крепость</span>. Потом <strong>были построены</strong> дома, улицы, <span class="cn-word" data-tr="kanallar">каналы</span>.</p>

<p>Город <strong>строился</strong> много лет. Работа была тяжёлая: люди работали в воде и в холоде. Много людей <span class="cn-word" data-pos="verb" data-tr="halok boʻldi">погибло</span>.</p>

<p>В 1712 году Петербург стал <span class="cn-word" data-tr="poytaxt">столицей</span>.</p>

<p>Сегодня это большой город: каналы, мосты, <span class="cn-word" data-tr="saroylar">дворцы</span>.</p>

<p>Но под каждым домом — всё то же болото.</p>

<p>Город <strong>был построен</strong> людьми — не природой. И он стоит уже три <span class="cn-word" data-tr="asr">века</span>.</p>''',
        "questions": [
            {
                "text": "Nega shunday yomon joyda shahar qurildi?",
                "choices": [
                    "Neva daryosi shu yerda dengizga chiqadi — joy muhim edi",
                    "U yerda koʻp tosh bor edi",
                    "Bu yer arzon edi",
                    "Matnda aytilmagan"
                ],
                "answer": 0,
                "explanation": "«Место было плохое… Но место было важное: здесь "
                               "река Нева идёт в море». Ikki jumla bir-biriga "
                               "qarama-qarshi qoʻyilgan: yomon, lekin muhim.",
            },
            {
                "text": "«Была построена крепость» va «были построены дома» — "
                        "nega shakl har xil?",
                "choices": [
                    "Qisqa sifatdosh egaga moslashadi: крепость ayol, дома koʻplik",
                    "Chunki qalʼa avval qurilgan",
                    "Chunki ular har xil zamonda",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Qisqa sifatdosh sifat kabi ishlaydi: jins va son "
                               "boʻyicha moslashadi — построен / построена / "
                               "построено / построены.",
            },
            {
                "text": "Matnning oxirgi jumlasi nimani taʼkidlaydi?",
                "choices": [
                    "Shaharni tabiat emas, odamlar qurgan",
                    "Shahar juda eski",
                    "Botqoq quritilgan",
                    "Shahar hali qurilmoqda"
                ],
                "answer": 0,
                "explanation": "«Город был построен людьми — не природой». "
                               "Undan oldingi jumla ham shuni tayyorlaydi: «под "
                               "каждым домом — всё то же болото». Botqoq hali "
                               "ham oʻsha yerda, lekin shahar uch asr turibdi.",
            },
        ],
    },
]
