# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-53 … PR-55.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 53 — uchta xat (yangi shakl: bitta kun, uch qalam),
54 — biografik hikoya, 55 — kundalik yoʻl. (50 yakuniy matn, 51
ilmiy-ommabop, 52 kundalik hikoya edi.)

Grammatika chegarasi (kumulyativ qoida):
  53-matn: vid TANLOV ekanini koʻrsatadi. Uch odam bitta kunni yozadi:
           biri jarayonni, biri natijani, uchinchisi ikkalasini. Matnning
           oxiri buni ochiq aytadi.
  54-matn: signal soʻzlar amalda — каждый день, часто, редко (НСВ)
           va наконец, за три дня (СВ). Biografik janr bu uchun ideal.
  55-matn: идти ↔ ходить. Matnda uchala maʼno ham bor: hozir (иду),
           muntazam (хожу), borib-kelish (ходил) va qobiliyat (ходит).

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_53_55.py --author=prime
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
    # PR-53 — vid va zamon                       UCHTA XAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Три письма об одном дне",
        "summary": (
            "PR-53 matni. Uch doʻst bitta shanba haqida yozadi. Kun bitta, "
            "lekin xatlar uchta — chunki har biri boshqa narsani tanlagan."
        ),
        "order":   53,
        "grammar": [
            {
                "pattern":  "НСВ — jarayon haqida yozish",
                "meaning":  "Гуляли, сидели, говорили — nima QILGANI aytiladi, "
                            "natija emas. Bu shakl kunni ichkaridan koʻrsatadi.",
                "examples": ["Мы гуляли в парке. Долго."],
            },
            {
                "pattern":  "СВ — natija haqida yozish",
                "meaning":  "Посмотрели, купила, написала — nima TUGAGANI "
                            "aytiladi. Bu shakl kunni roʻyxat sifatida koʻrsatadi.",
                "examples": ["Мы посмотрели фильм. Я купила книгу."],
            },
            {
                "pattern":  "Ikkalasi bir gapda",
                "meaning":  "«Я читала, но не прочитала» — jarayon boʻldi, natija "
                            "boʻlmadi. Bu ziddiyat emas: vid tizimining butun kuchi "
                            "aynan shunda.",
                "examples": ["Я читала в автобусе, но не прочитала."],
            },
        ],
        "body": '''<p>Одна <span class="cn-word" data-tr="shanba">суббота</span>. Три <span class="cn-word" data-tr="xat">письма</span>.</p>

<p><strong>Бекзод пишет:</strong></p>

<p>«Мы <strong>гуляли</strong> в парке. Долго. Потом <strong>сидели</strong> в кафе и <strong>говорили</strong>. О школе, о лете, о <span class="cn-word" data-tr="filmlar">фильмах</span>. Хороший был день».</p>

<p><strong>Катя пишет:</strong></p>

<p>«Мы <strong>посмотрели</strong> новый фильм. Потом я <strong>купила</strong> книгу и <strong>вернулась</strong> домой. Вечером <strong>написала</strong> два письма и <strong>сделала</strong> <span class="cn-word" data-tr="uy vazifasi">уроки</span>».</p>

<p><strong>Афсона пишет:</strong></p>

<p>«Сначала мы долго <strong>гуляли</strong>, потом <strong>посмотрели</strong> фильм. В автобусе я <strong>читала</strong> — но не <strong>прочитала</strong>. <span class="cn-word" data-pos="verb" data-tr="Qoldi">Осталось</span> три <span class="cn-word" data-tr="sahifa">страницы</span>».</p>

<p>Один день. Три письма. И <span class="cn-word" data-tr="xuddi">как будто</span> три разных дня.</p>

<p>Бекзод пишет о <span class="cn-word" data-tr="jarayon">процессе</span>: что они <strong>делали</strong>.</p>

<p>Катя пишет о <span class="cn-word" data-tr="natija">результате</span>: что они <strong>сделали</strong>.</p>

<p>Афсона пишет о двух вместе.</p>

<p>Кто прав? <span class="cn-word" data-tr="Hammasi">Все</span>.</p>

<p>Вид — это не правило. Это <span class="cn-word" data-tr="tanlov">выбор</span>: что ты хочешь сказать.</p>''',
        "questions": [
            {
                "text": "Nega bitta kun haqidagi uchta xat shunchalik boshqacha "
                        "chiqdi?",
                "choices": [
                    "Har biri boshqa narsani tanlagan: jarayon, natija yoki ikkalasi",
                    "Ular boshqa-boshqa kunlarda uchrashgan",
                    "Bekzod hammasini unutgan",
                    "Katya kinoga bormagan"
                ],
                "answer": 0,
                "explanation": "Matn buni oxirida ochiq aytadi: Bekzod jarayon haqida "
                               "(делали), Katya natija haqida (сделали), Afsona esa "
                               "ikkalasi haqida yozgan. Kun bitta — tanlov uchta.",
            },
            {
                "text": "«Я читала — но не прочитала» nimani anglatadi?",
                "choices": [
                    "Oʻqidi, lekin kitobni tugatmadi",
                    "Umuman oʻqimadi",
                    "Kitobni ikki marta oʻqidi",
                    "Kitobni yoʻqotdi"
                ],
                "answer": 0,
                "explanation": "Jarayon boʻldi (НСВ — читала), natija boʻlmadi (СВ — "
                               "не прочитала). Keyingi jumla buni tasdiqlaydi: "
                               "«Осталось три страницы».",
            },
            {
                "text": "Matnning oxirgi jumlasi vid haqida nima deydi?",
                "choices": [
                    "Vid — qoida emas, balki nima aytmoqchi ekaningizni tanlash",
                    "Vid faqat yozuvda ishlatiladi",
                    "НСВ har doim toʻgʻriroq",
                    "СВ har doim toʻgʻriroq"
                ],
                "answer": 0,
                "explanation": "«Вид — это не правило. Это выбор: что ты хочешь "
                               "сказать». Uch xat ham toʻgʻri — ular shunchaki "
                               "kunning boshqa tomonini koʻrsatadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-54 — vidni tanlash                      BIOGRAFIK HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Как я готовился к экзамену",
        "summary": (
            "PR-54 matni. Uch oylik tayyorgarlik: har kuni ikki soatdan, keyin "
            "aprelda uch kunlik yakuniy takror. Oxirida bir jumlalik xulosa."
        ),
        "order":   54,
        "grammar": [
            {
                "pattern":  "НСВ signallari",
                "meaning":  "Каждый день, иногда, часто, редко, два часа — "
                            "hammasi takror yoki davomiylikni bildiradi va НСВ "
                            "talab qiladi.",
                "examples": ["Каждый день я читал два часа.", "Редко смотрел фильмы."],
            },
            {
                "pattern":  "СВ signallari",
                "meaning":  "Наконец, за три дня, один раз — natija yoki muddatni "
                            "bildiradi va СВ talab qiladi. Diqqat: «два часа» НСВ, "
                            "«за два часа» esa СВ.",
                "examples": ["Прочитал их за три дня.", "Наконец я понял."],
            },
            {
                "pattern":  "Ketma-ketlik → СВ",
                "meaning":  "«Взял … прочитал … понял … сдал» — birin-ketin tugagan "
                            "ishlar. Hikoyaning oxirgi qismi shu naqshda quriladi.",
                "examples": ["Я взял все тетради и прочитал их."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="imtihon">Экзамен</span> был в мае. Я <strong>готовился</strong> три <span class="cn-word" data-tr="oy">месяца</span>.</p>

<p><strong>Каждый день</strong> я <strong>читал</strong> два часа. <strong>Иногда</strong> три.</p>

<p><strong>Часто</strong> я <strong>писал</strong> слова в тетрадь. <strong>Редко</strong> <strong>смотрел</strong> фильмы. <span class="cn-word" data-tr="Deyarli">Почти</span> не <strong>гулял</strong>.</p>

<p>Это было <span class="cn-word" data-tr="zerikarli">скучно</span>. И <span class="cn-word" data-tr="uzoq">долго</span>.</p>

<p>В апреле я <strong>решил</strong>: <span class="cn-word" data-tr="Yetadi, boʻldi">хватит</span>.</p>

<p>Я <strong>взял</strong> все <span class="cn-word" data-tr="daftarlar">тетради</span> и <strong>прочитал</strong> их <strong>за три дня</strong>.</p>

<p><strong>Наконец</strong> я <strong>понял</strong>: я знаю не <span class="cn-word" data-tr="hammasi">всё</span>, но много.</p>

<p>В мае я <strong>сдал</strong> экзамен.</p>

<p>Теперь я знаю один <span class="cn-word" data-tr="sir">секрет</span>.</p>

<p><strong>Каждый день</strong> — это <strong>читал</strong>. Три дня в апреле — это <strong>прочитал</strong>.</p>

<p>И <span class="cn-word" data-tr="ikkinchisi">второе</span> не работает без <span class="cn-word" data-tr="birinchisi">первого</span>.</p>''',
        "questions": [
            {
                "text": "Matnning oxirgi jumlasi nimani anglatadi?",
                "choices": [
                    "Uch kunlik yakuniy takror faqat uch oylik mehnat ustiga qurilgani uchun ishladi",
                    "Aprelda oʻqish yetarli edi",
                    "Har kuni oʻqish foydasiz boʻldi",
                    "Imtihon oson edi"
                ],
                "answer": 0,
                "explanation": "«Каждый день — это читал. Три дня в апреле — это "
                               "прочитал. И второе не работает без первого». "
                               "Natija (СВ) jarayonsiz (НСВ) boʻlmaydi — bu ham "
                               "grammatik, ham hayotiy xulosa.",
            },
            {
                "text": "Nega matnda «читал два часа», lekin «прочитал за три "
                        "дня»?",
                "choices": [
                    "«Два часа» davomiylik (НСВ), «за три дня» esa muddat (СВ)",
                    "Chunki uchinchisi koʻproq vaqt",
                    "Chunki birinchisi takroriy",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Bitta predlog butun maʼnoni oʻzgartiradi: «два часа» "
                               "— qancha vaqt ketgani; «за три дня» — qancha vaqtda "
                               "tugagani. Birinchisi НСВ, ikkinchisi СВ chaqiradi.",
            },
            {
                "text": "Matnning oxirgi qismida nega hamma feʼl СВ da?",
                "choices": [
                    "Chunki bu ketma-ketlik: взял → прочитал → понял → сдал",
                    "Chunki bular takroriy ishlar",
                    "Chunki ular kelasi zamonda",
                    "Chunki ular uzoq davom etdi"
                ],
                "answer": 0,
                "explanation": "Birin-ketin tugagan ishlar har doim СВ talab qiladi. "
                               "Matnning boshi (НСВ — takror va davomiylik) va oxiri "
                               "(СВ — ketma-ketlik) bir-biriga qarama-qarshi "
                               "qoʻyilgan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-55 — идти / ходить                      KUNDALIK YOʻL
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Дорога в школу",
        "summary": (
            "PR-55 matni. Har kungi yigirma daqiqalik yoʻl — va buvining "
            "oʻn kilometri. Matn oxirida oʻquvchi yomgʻirdan shikoyat qilishni "
            "bas qiladi."
        ),
        "order":   55,
        "grammar": [
            {
                "pattern":  "хожу — muntazam",
                "meaning":  "Takror yoki odat: «Я хожу в школу пешком» — har kuni "
                            "shunday qilaman. Oʻzbekcha «borib turaman».",
                "examples": ["Я хожу в школу пешком.", "Он уже ходит."],
            },
            {
                "pattern":  "иду / шёл — hozir, bir tomonga",
                "meaning":  "Aynan hozir yoʻldaman: «Сегодня я иду медленно». "
                            "Oʻtgan zamonda «шёл» — yoʻlda edim, yetib bordimmi "
                            "nomaʼlum.",
                "examples": ["Сегодня я иду медленно.", "Утром я шёл и думал."],
            },
            {
                "pattern":  "ходил — borib kelish",
                "meaning":  "Bordim VA qaytdim — tugagan safar. «Вчера я ходил в "
                            "магазин» = doʻkonga borib keldim. Oʻzbekcha «borib "
                            "keldim».",
                "examples": ["Вчера я ходил в магазин."],
            },
        ],
        "body": '''<p>Я <strong>хожу</strong> в школу <span class="cn-word" data-tr="piyoda">пешком</span>. Каждый день, пять лет.</p>

<p>Сегодня я <strong>иду</strong> <span class="cn-word" data-tr="sekin">медленно</span>. <strong>Идёт</strong> <span class="cn-word" data-tr="yomgʻir">дождь</span>.</p>

<p>Вчера я <strong>ходил</strong> в магазин после школы. <span class="cn-word" data-pos="verb" data-tr="sotib oldim">Купил</span> хлеб и <span class="cn-word" data-pos="verb" data-tr="qaytdim">вернулся</span> домой.</p>

<p>Мой брат Бекзод ещё маленький. Но он уже <strong>ходит</strong>. Медленно, но <span class="cn-word" data-tr="oʻzi">сам</span>.</p>

<p>Бабушка говорит:</p>

<p>— Раньше я <strong>ходила</strong> в школу десять <span class="cn-word" data-tr="kilometr">километров</span>. Каждый день. И зимой тоже.</p>

<p>Я не знаю, правда это или нет. Бабушка <span class="cn-word" data-pos="verb" data-tr="yaxshi koʻradi">любит</span> такие <span class="cn-word" data-tr="hikoyalar">истории</span>.</p>

<p>Но сегодня утром я <strong>шёл</strong> и думал о бабушке.</p>

<p>Десять километров. Каждый день. Зимой.</p>

<p>Моя <span class="cn-word" data-tr="yoʻl">дорога</span> — двадцать минут.</p>

<p>Теперь я не <span class="cn-word" data-pos="verb" data-tr="shikoyat qilaman">жалуюсь</span> на дождь.</p>''',
        "questions": [
            {
                "text": "Matn nima bilan tugaydi va nega?",
                "choices": [
                    "Muallif endi yomgʻirdan shikoyat qilmaydi — buvining yoʻli ancha ogʻir edi",
                    "Muallif maktabga bormaslikka qaror qildi",
                    "Buvi yolgʻon aytgani maʼlum boʻldi",
                    "Bekzod maktabga bora boshladi"
                ],
                "answer": 0,
                "explanation": "«Десять километров… Моя дорога — двадцать "
                               "минут». Taqqoslash oʻz-oʻzidan xulosa chiqaradi. "
                               "Buvining hikoyasi rostmi yoki yoʻqmi — matn buni ham "
                               "aytmaydi, va bu muhim emas.",
            },
            {
                "text": "«Я хожу в школу» va «Сегодня я иду» — nega ikki xil "
                        "feʼl?",
                "choices": [
                    "Хожу — muntazam odat, иду — aynan hozir yoʻldaman",
                    "Bittasi oʻtgan zamon",
                    "Bittasi СВ, boshqasi НСВ",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham НСВ — farq vid emas, yoʻnalish. "
                               "Oʻzbekcha tekshiruv: «borib turaman» (хожу) va "
                               "«boryapman» (иду).",
            },
            {
                "text": "«Вчера я ходил в магазин» nimani anglatadi?",
                "choices": [
                    "Doʻkonga bordim va qaytdim — safar tugagan",
                    "Doʻkonga ketayotgan edim",
                    "Doʻkonga har kuni boraman",
                    "Doʻkonga bormoqchi edim"
                ],
                "answer": 0,
                "explanation": "Ходил — borib-kelish. Keyingi jumla buni tasdiqlaydi: "
                               "«Купил хлеб и вернулся домой». Agar «шёл» boʻlsa, "
                               "gap faqat yoʻl haqida boʻlardi.",
            },
        ],
    },
]
