# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-56 … PR-58.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 56 — sayohat qaydlari, 57 — ilmiy-ommabop,
58 — hikoya. (53 uchta xat, 54 biografik, 55 kundalik yoʻl edi.)

⚠️ SARLAVHA TUZATILDI (58). Toc'da «Кот, который ушёл и пришёл» yozilgan
edi, lekin КОТОРЫЙ PR-63 da oʻrgatiladi. Kumulyativ qoidaga koʻra
oʻrgatilmagan qurilish sarlavhada boʻlishi mumkin emas, shuning uchun
«Кот ушёл и пришёл» qilindi — maʼnosi bir xil, grammatikasi toza.

⚠️ FAKTLAR (56-matn). Transsibir temir yoʻli haqidagi daʼvolar
tekshirilgan va ehtiyotkorlik bilan tanlangan: Moskva—Vladivostok yoʻli
taxminan yetti kun davom etadi; Vladivostok Moskvadan yetti soat oldinda;
yoʻl Baykal koʻlining janubiy qirgʻogʻi boʻylab oʻtadi; yoʻl oxirida
Tinch okeani. Aniq kilometr raqami ATAY aytilmagan — manbalarda u biroz
har xil.

Grammatika chegarasi (kumulyativ qoida):
  56-matn: ехать ↔ ездить, лететь ↔ летать, нести ↔ носить.
           PREFIKSLI harakat feʼllari YOʻQ — ular PR-57 da.
  57-matn: prefikslar roʻyxati. Matn shakli — roʻyxat, chunki mavzu ham
           roʻyxat.
  58-matn: prefikslar hikoyada. Mushuk ketadi va qaytadi; ушёл/пришёл
           (СВ, bir marta) va уходил/приходил (НСВ, odat) yonma-yon.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_56_58.py --author=prime
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
    # PR-56 — harakat juftliklari               SAYOHAT QAYDLARI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Транссиб: семь дней в поезде",
        "summary": (
            "PR-56 matni. Moskvadan Vladivostokgacha yetti kun. Deraza ortida "
            "oʻrmon, keyin yana oʻrmon — va yoʻl oxirida okean. Hamsafarning "
            "bir jumlasi butun sayohatni tushuntiradi."
        ),
        "order":   56,
        "grammar": [
            {
                "pattern":  "ехал — bir tomonga",
                "meaning":  "Yetti kun davomida bir tomonga ketish — bu ЕХАТЬ. "
                            "Oʻzbekcha «ketayotgan edim». Agar «ЕЗДИЛ» boʻlsa, borib "
                            "qaytish maʼnosi chiqardi.",
                "examples": ["Я ехал семь дней.", "Поезд шёл на восток."],
            },
            {
                "pattern":  "летал — muntazam",
                "meaning":  "ЛЕТАТЬ — koʻp marta, muntazam: «Он летал в Москву "
                            "много раз». Bir marta, hozir uchayotgan boʻlsa — "
                            "ЛЕТИТ.",
                "examples": ["Мой сосед летал в Москву много раз."],
            },
            {
                "pattern":  "носил — muntazam olib yurish",
                "meaning":  "НОСИТЬ — takroriy: proyezdnik har soatda choy olib "
                            "keladi. Bir marta olib ketayotgan boʻlsa — НЁС.",
                "examples": ["Проводник носил чай каждый час."],
            },
        ],
        "body": '''<p>Транссиб — длинная <span class="cn-word" data-tr="temir yoʻl">железная дорога</span>. Очень длинная.</p>

<p>Москва — Владивосток. Семь дней в поезде.</p>

<p>Я <strong>ехал</strong> семь дней. Каждый день поезд <strong>шёл</strong> на <span class="cn-word" data-tr="sharq">восток</span>.</p>

<p>За окном — <span class="cn-word" data-tr="oʻrmon">лес</span>. Потом <span class="cn-word" data-tr="yana">опять</span> лес. Потом снова лес.</p>

<p>На третий день — Байкал. Поезд <strong>шёл</strong> <span class="cn-word" data-tr="boʻylab">вдоль</span> озера долго. Вода была <span class="cn-word" data-tr="quyuq koʻk">тёмно-синяя</span>.</p>

<p><span class="cn-word" data-tr="vagon xodimi">Проводник</span> <strong>носил</strong> чай каждый час. Это его работа.</p>

<p>Мой сосед <strong>летал</strong> в Москву много раз. Но <span class="cn-word" data-tr="poyezdda">поездом</span> — первый раз.</p>

<p>— Самолёт быстро, — говорит он. — Но самолёт не показывает страну. А поезд показывает.</p>

<p>Семь дней. Семь <span class="cn-word" data-tr="soat mintaqalari">часовых поясов</span>. Владивосток <span class="cn-word" data-tr="oldinda">впереди</span> Москвы на семь часов.</p>

<p>В <span class="cn-word" data-tr="oxirida">конце</span> пути — море. Тихий океан.</p>

<p>Я <strong>ехал</strong> семь дней. Теперь я знаю: страна очень большая.</p>''',
        "questions": [
            {
                "text": "Hamsafar samolyot va poyezdni qanday taqqoslaydi?",
                "choices": [
                    "Samolyot tez, lekin poyezd mamlakatni koʻrsatadi",
                    "Poyezd tezroq va arzonroq",
                    "Samolyotda ovqat yaxshiroq",
                    "Ikkalasi bir xil"
                ],
                "answer": 0,
                "explanation": "«Самолёт быстро… Но самолёт не показывает страну. "
                               "А поезд показывает». Matnning oxirgi jumlasi ham shu "
                               "fikrni tasdiqlaydi: «Теперь я знаю: страна очень "
                               "большая».",
            },
            {
                "text": "Nega matnda «я ехал», «я ездил» emas?",
                "choices": [
                    "Yetti kun bir tomonga ketildi — borib qaytish emas",
                    "Chunki poyezdda ketildi",
                    "Chunki bu uzoq yoʻl",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Ехал — bir tomonga, jarayon. Ездил «borib keldim» "
                               "degan boʻlardi, lekin matnda faqat Moskvadan "
                               "Vladivostokgacha boriladi.",
            },
            {
                "text": "«Проводник носил чай каждый час» — nega НОСИЛ?",
                "choices": [
                    "«Каждый час» takrorni bildiradi — muntazam harakat",
                    "Chunki choy ogʻir edi",
                    "Chunki u bir marta olib keldi",
                    "Chunki bu oʻtgan zamon"
                ],
                "answer": 0,
                "explanation": "НЕСТИ — bir marta, hozir olib ketish. НОСИТЬ — "
                               "muntazam, takroriy. «Каждый час» ikkinchisini "
                               "talab qiladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-57 — prefikslar                        ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Один глагол, десять дверей",
        "summary": (
            "PR-57 matni. Bitta feʼl — идти — va oʻnta prefiks. Har biri boshqa "
            "eshikni ochadi. Oxirida bitta soʻzning ichidan kutilmagan maʼno "
            "chiqadi."
        ),
        "order":   57,
        "grammar": [
            {
                "pattern":  "Prefiks yoʻnalishni bildiradi",
                "meaning":  "ПРИ- kelmoq, У- ketmoq, В- kirmoq, ВЫ- chiqmoq, ДО- "
                            "yetib bormoq, ПЕРЕ- kesib oʻtmoq, ПОД- yaqinlashmoq, "
                            "ОТ- uzoqlashmoq. Bitta oʻzak, sakkizta maʼno.",
                "examples": ["Прийти — быть здесь.", "Уйти — не быть здесь."],
            },
            {
                "pattern":  "идти → СВ, ходить → НСВ",
                "meaning":  "Prefiks ИДТИ ga qoʻshilsa СВ chiqadi (прийти), ХОДИТЬ "
                            "ga qoʻshilsa НСВ (приходить). Vid va harakat tizimi shu "
                            "yerda birlashadi.",
                "examples": ["прийти ↔ приходить"],
            },
            {
                "pattern":  "найти = на + идти",
                "meaning":  "«Topmoq» soʻzi aslida «yurib borib ustiga tushmoq» "
                            "degani. Shuning uchun u ИДТИ kabi turlanadi: найду, "
                            "нашёл, нашла.",
                "examples": ["Найти — идти и увидеть."],
            },
        ],
        "body": '''<p>Один <span class="cn-word" data-tr="feʼl">глагол</span>: <strong>идти</strong>.</p>

<p>Теперь <span class="cn-word" data-tr="prefiks">приставка</span> — и глагол <span class="cn-word" data-pos="verb" data-tr="oʻzgaradi">меняется</span>.</p>

<p><strong>Прийти</strong> — быть здесь.</p>

<p><strong>Уйти</strong> — не быть здесь.</p>

<p><strong>Войти</strong> — быть <span class="cn-word" data-tr="ichida">внутри</span>.</p>

<p><strong>Выйти</strong> — быть на улице.</p>

<p><strong>Подойти</strong> — быть <span class="cn-word" data-tr="yaqin">близко</span>.</p>

<p><strong>Отойти</strong> — быть далеко.</p>

<p><strong>Перейти</strong> — быть на другой <span class="cn-word" data-tr="tomon">стороне</span>.</p>

<p><strong>Дойти</strong> — быть в конце дороги.</p>

<p>Один <span class="cn-word" data-tr="oʻzak">корень</span>. Восемь <span class="cn-word" data-tr="eshiklar">дверей</span>. И это ещё не всё.</p>

<p>Есть <strong>зайти</strong> — быть недолго. Есть <strong>пройти</strong> — быть дальше. Есть <strong>пойти</strong> — начать идти.</p>

<p>И есть <strong>найти</strong>.</p>

<p><strong>Найти</strong> — это «на» плюс «идти». Идти — и <span class="cn-word" data-pos="verb" data-tr="uchratmoq">встретить</span>.</p>

<p>Поэтому в русском языке «найти» значит: ты шёл, шёл — и вот оно.</p>

<p>В узбекском языке для каждой двери есть <span class="cn-word" data-tr="alohida">отдельное</span> слово.</p>

<p>В русском языке дверь одна — это глагол. А приставки — это <span class="cn-word" data-tr="kalitlar">ключи</span>.</p>

<p>Один глагол. Десять ключей. Десять дверей.</p>''',
        "questions": [
            {
                "text": "«Найти» soʻzi qanday tuzilgan va bu nimani anglatadi?",
                "choices": [
                    "На + идти — yurib borib ustiga tushmoq",
                    "На + йти — yangi soʻz, tuzilishi yoʻq",
                    "Най + ти — qadimiy oʻzak",
                    "Bu boshqa feʼllardan olingan"
                ],
                "answer": 0,
                "explanation": "«Найти — это „на“ плюс „идти“… ты шёл, шёл — и вот "
                               "оно». Shuning uchun u ИДТИ kabi turlanadi: найду, "
                               "нашёл, нашла.",
            },
            {
                "text": "Matnga koʻra rus va oʻzbek tillari bu yerda qanday farq "
                        "qiladi?",
                "choices": [
                    "Oʻzbekchada har bir maʼno uchun alohida soʻz, ruschada bitta oʻzak va prefikslar",
                    "Oʻzbekchada prefikslar koʻproq",
                    "Ruschada har bir maʼno uchun alohida soʻz",
                    "Farqi yoʻq"
                ],
                "answer": 0,
                "explanation": "«В узбекском языке для каждой двери есть "
                               "отдельное слово. В русском языке дверь одна — "
                               "это глагол. А приставки — это ключи».",
            },
            {
                "text": "Matnning sarlavhasi nima uchun shunday tanlangan?",
                "choices": [
                    "Feʼl — eshik, prefikslar esa kalitlar: bitta eshik, oʻnta kalit",
                    "Chunki matnda oʻnta xona haqida gapiriladi",
                    "Chunki rus tilida oʻnta feʼl bor",
                    "Bu shunchaki chiroyli nom"
                ],
                "answer": 0,
                "explanation": "Matn oxirgi ikki jumlada obrazni ochadi: «дверь одна "
                               "— это глагол. А приставки — это ключи. Один "
                               "глагол. Десять ключей. Десять дверей».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-58 — prefikslar hikoyada               HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Кот ушёл и пришёл",
        "summary": (
            "PR-58 matni. Ryzhik chorshanba kuni ketdi va toʻrt kun qaytmadi. "
            "Butun oila uni qidirdi — buvidan boshqa hamma. Buvining aytgani "
            "toʻgʻri chiqdi."
        ),
        "order":   58,
        "grammar": [
            {
                "pattern":  "ушёл / пришёл — bir marta",
                "meaning":  "Prefiks + ИДТИ = СВ: bir marta tugagan harakat. «В "
                            "среду он ушёл» — aniq bir kuni, aniq bir voqea.",
                "examples": ["В среду вечером он ушёл.", "Но он не пришёл."],
            },
            {
                "pattern":  "уходил / приходил — odat",
                "meaning":  "Prefiks + ХОДИТЬ = НСВ: takroriy harakat. «Он уходил "
                            "каждый день и приходил» — bu uning odati edi.",
                "examples": ["Он уходил каждый день — и приходил."],
            },
            {
                "pattern":  "подошёл · вышел · сошёл",
                "meaning":  "ПОД- yaqinlashmoq, ВЫ- chiqmoq, С- pastga tushmoq. "
                            "Har bir prefiks harakatning yoʻnalishini aniq "
                            "koʻrsatadi.",
                "examples": ["Он подошёл к двери.", "Он сошёл вниз медленно."],
            },
        ],
        "body": '''<p>У нас есть кот. Его зовут <span class="cn-word" data-tr="Ryzhik (sarigʻ ism)">Рыжик</span>.</p>

<p>В <span class="cn-word" data-tr="chorshanba">среду</span> вечером он <strong>ушёл</strong>.</p>

<p>Сначала он <strong>подошёл</strong> к двери. Потом <strong>вышел</strong> во <span class="cn-word" data-tr="hovli">двор</span>. Потом — <span class="cn-word" data-tr="hech narsa">ничего</span>.</p>

<p>Мы думали: он <strong>зайдёт</strong> <span class="cn-word" data-tr="bir soatdan keyin">через час</span>.</p>

<p>Но он не <strong>пришёл</strong>.</p>

<p>В <span class="cn-word" data-tr="payshanba">четверг</span> мы <span class="cn-word" data-pos="verb" data-tr="qidirdik">искали</span> его во дворе. В пятницу Бекзод <strong>перешёл</strong> улицу и <strong>дошёл</strong> до рынка. Рыжика нет.</p>

<p>В субботу бабушка сказала:</p>

<p>— Он <strong>придёт</strong>. <span class="cn-word" data-tr="Mushuklar">Кошки</span> всегда <strong>приходят</strong>.</p>

<p>В воскресенье утром я <strong>вышел</strong> во двор.</p>

<p>Рыжик сидел на <span class="cn-word" data-tr="tom">крыше</span> и смотрел на меня.</p>

<p>Он <strong>сошёл</strong> вниз медленно. Потом <strong>подошёл</strong> и <span class="cn-word" data-pos="verb" data-tr="oʻtirdi">сел</span> рядом. <span class="cn-word" data-tr="Xuddi">Как будто</span> ничего не было.</p>

<p>Рыжик <strong>уходил</strong> каждый день — и каждый день <strong>приходил</strong>.</p>

<p>Только в этот раз он <strong>ушёл</strong> на четыре дня.</p>

<p>Бабушка была <span class="cn-word" data-tr="haqli">права</span>.</p>''',
        "questions": [
            {
                "text": "Ryzhik qayerdan qaytdi?",
                "choices": [
                    "Tomdan tushdi — hovlida edi",
                    "Bozordan keldi",
                    "Qoʻshnilarnikidan",
                    "Matnda aytilmagan"
                ],
                "answer": 0,
                "explanation": "«Рыжик сидел на крыше и смотрел на меня. Он "
                               "сошёл вниз медленно». Toʻrt kun qidirilgan mushuk "
                               "aslida yaqin joyda ekan.",
            },
            {
                "text": "«Он ушёл» va «он уходил» — nima farq qiladi?",
                "choices": [
                    "Ушёл — bir marta, aniq voqea; уходил — har kungi odat",
                    "Ушёл — hozirgi zamon",
                    "Уходил — kelasi zamon",
                    "Ikkalasi bir xil"
                ],
                "answer": 0,
                "explanation": "Prefiks + ИДТИ = СВ (bir marta), prefiks + ХОДИТЬ = "
                               "НСВ (takror). Matn ikkalasini yonma-yon qoʻyadi: har "
                               "kuni ketardi va qaytardi — bu safar esa toʻrt kunga "
                               "ketdi.",
            },
            {
                "text": "Nega matnda «подошёл», «вышел», «сошёл» — har xil "
                        "prefikslar?",
                "choices": [
                    "Har bir prefiks harakatning boshqa yoʻnalishini koʻrsatadi",
                    "Chunki ular har xil feʼllar",
                    "Chunki ular har xil zamonda",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "ПОД- yaqinlashish (eshik oldiga keldi), ВЫ- chiqish "
                               "(hovliga chiqdi), С- pastga tushish (tomdan tushdi). "
                               "Bitta oʻzak — uchta aniq yoʻnalish.",
            },
        ],
    },
]
