# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-12 … PR-14.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Shakl xilma-xilligi: 12 — kundalik daftar (yangi janr), 13 — doʻkondagi suhbat,
14 — buvijon haqidagi kichik hayot lavhasi.

Feʼl tizimi hali ochilmagan (PR-19 dan), shuning uchun tocdagi "narrative frame"
istisnosi ishlatilgan: есть · нет · зовут · живёт · работает · говорит ·
сказал(а)/сказали · пришёл/пришла/пришли · дал(а) · был/была/было/были.
Vaqt/joy ravishlari va turgʻun iboralar (сколько стоит, спасибо, пожалуйста)
lugʻat sifatida izohlanadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_12_14.py --author=prime
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
    # PR-12 — sifat                    KUNDALIK DAFTAR (yangi janr)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Новая школа",
        "summary": (
            "PR-12 matni. Dilnozaning kundalik daftaridan bir sahifa: yangi maktabdagi "
            "birinchi kun. Har bir jumlada sifat bor, va har bir sifat oʻz otiga "
            "moslashgan — oxirlariga qarab boring."
        ),
        "order":   12,
        "grammar": [
            {
                "pattern":  "Sifat + ot (moslashuv)",
                "meaning":  "Sifat otning jinsi va soniga qarab shakl oladi: "
                            "новый (m.) / новая (f.) / новое (oʻrta) / новые "
                            "(koʻplik). Sifat otdan oldin turadi — oʻzbekchadagidek.",
                "examples": ["новая школа", "большой класс", "новые друзья"],
            },
            {
                "pattern":  "Г К Х Ж Ч Ш Щ dan keyin -ий",
                "meaning":  "Bu yettita harfdan keyin sifat -ый emas, -ий bilan "
                            "tugaydi. Shuning uchun русский, маленький, хороший.",
                "examples": ["русский язык", "маленький кот", "хороший день"],
            },
            {
                "pattern":  "Sifat kesim sifatida — tiresiz",
                "meaning":  "Sifat otdan keyin ham tura oladi. Bunda tire QOʻYILMAYDI "
                            "(PR-11) va maʼno oʻzgaradi: «новая школа» nomlaydi, "
                            "«школа новая» esa xabar beradi.",
                "examples": ["Школа новая.", "Класс большой."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="sentabr">Сентябрь</span>. Сегодня — <span class="cn-word" data-tr="yangi">новая</span> школа.</p>

<p>Школа <strong>большая</strong> и <strong>светлая</strong>. Наш класс <strong>большой</strong>. Окна <strong><span class="cn-word" data-tr="katta (koʻplik)">большие</span></strong>, и здесь <strong><span class="cn-word" data-tr="yangi (koʻplik)">новые</span></strong> столы.</p>

<p><span class="cn-word" data-tr="oʻqituvchi (ayol)">Учительница</span> — <span class="cn-word" data-tr="yosh">молодая</span>. Её зовут Марина Олеговна. Она <strong><span class="cn-word" data-tr="mehribon">добрая</span></strong>.</p>

<p><span class="cn-word" data-tr="birinchi dars">Первый урок</span> — <strong>русский</strong> язык. Урок <strong><span class="cn-word" data-tr="qiziqarli">интересный</span></strong>, но <strong><span class="cn-word" data-tr="qiyin">трудный</span></strong>.</p>

<p>Мой сосед — Жасур. Жасур <strong><span class="cn-word" data-tr="quvnoq">весёлый</span></strong>. Его <span class="cn-word" data-tr="ryukzak">рюкзак</span> <strong>старый</strong>, а ручки <strong>новые</strong>.</p>

<p>Потом <span class="cn-word" data-pos="verb" data-tr="keldi (ayol)">пришла</span> Афсона. Афсона сказала: «Школа <strong>новая</strong>, но люди <strong>хорошие</strong>».</p>

<p>Да. Школа <strong>новая</strong>. Класс <strong>большой</strong>. И друзья <strong><span class="cn-word" data-tr="yangi (koʻplik)">новые</span></strong>.</p>''',
        "questions": [
            {
                "text": "Dilnoza kunini qanday yakunlaydi?",
                "choices": [
                    "Maktab yangi, lekin unda allaqachon yangi doʻstlari bor",
                    "Maktab yoqmadi",
                    "Darslar juda oson edi",
                    "U eski maktabini sogʻindi"
                ],
                "answer": 0,
                "explanation": "Oxirgi jumla: «Школа новая. Класс большой. И друзья "
                               "новые». Afsonaning gapi ham shuni tayyorlaydi: "
                               "«Школа новая, но люди хорошие».",
            },
            {
                "text": "Nega «русский язык», «русскый» emas?",
                "choices": [
                    "Chunki oʻzak К bilan tugaydi — Г К Х Ж Ч Ш Щ dan keyin -ий keladi",
                    "Chunki язык erkak jinsida",
                    "Chunki bu tilning nomi",
                    "Chunki urgʻu oxirda"
                ],
                "answer": 0,
                "explanation": "Yettita harf qoidasi — xuddi PR-9 dagi «книги» kabi. "
                               "Bu roʻyxat rus imlosining koʻp joyida ishlaydi, shuning "
                               "uchun uni bir marta yodlash arziydi.",
            },
            {
                "text": "Matnda «Школа новая» bor, lekin tire yoʻq. Nega?",
                "choices": [
                    "Chunki kesim — sifat, ot emas",
                    "Chunki gap qisqa",
                    "Chunki bu kundalik daftar",
                    "Bu xato, tire boʻlishi kerak"
                ],
                "answer": 0,
                "explanation": "PR-11 qoidasi: tire faqat ikkala tomon ham OT boʻlganda "
                               "qoʻyiladi. Bu yerda kesim sifat (новая), shuning uchun "
                               "tire yoʻq. Solishtiring: «Мой город — Ташкент» — ot + ot.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-13 — sonlar                   DOʻKONDAGI SUHBAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Сколько стоит?",
        "summary": (
            "PR-13 matni. Sherbek maktabga daftar va ruchka olgani boradi, lekin puli "
            "yetmaydi. Sotuvchi ayol bitta narsani boshqacha hisoblaydi — sonlar bilan "
            "toʻla kichik doʻkon suhbati."
        ),
        "order":   13,
        "grammar": [
            {
                "pattern":  "Сколько стоит? / Сколько?",
                "meaning":  "«Qancha turadi?» va «Nechta?». Doʻkondagi eng kerakli "
                            "savol — uni turgʻun ibora sifatida yodlang, soʻz tartibi "
                            "oʻzgarmaydi.",
                "examples": ["Сколько стоит тетрадь?", "Сколько у вас ручек?"],
            },
            {
                "pattern":  "два / две",
                "meaning":  "Faqat 2 sonining ayol jinsi uchun alohida shakli bor: "
                            "две тетради, lekin два карандаша. Uch va undan keyingi "
                            "sonlar jinsga qarab oʻzgarmaydi.",
                "examples": ["две тетради", "два карандаша", "три ручки"],
            },
            {
                "pattern":  "один / одна / одно",
                "meaning":  "«Bir» soni sifat kabi otga moslashadi: один карандаш, "
                            "одна ручка, одно слово.",
                "examples": ["одна ручка", "один рюкзак"],
            },
        ],
        "body": '''<p>Это <span class="cn-word" data-tr="doʻkon">магазин</span>. Здесь <span class="cn-word" data-pos="verb" data-tr="ishlaydi">работает</span> Нина Петровна. <span class="cn-word" data-pos="verb" data-tr="keldi">Пришёл</span> Шербек.</p>

<p><strong>Шербек:</strong> Здравствуйте! <strong>Сколько стоит</strong> тетрадь?</p>

<p><strong>Нина Петровна:</strong> <span class="cn-word" data-tr="besh">Пять</span> <span class="cn-word" data-tr="ming">тысяч</span>.</p>

<p><strong>Шербек:</strong> А ручка?</p>

<p><strong>Нина Петровна:</strong> <span class="cn-word" data-tr="uch">Три</span> тысячи.</p>

<p>Шербек сказал: «<strong>Две</strong> тетради и <strong>две</strong> ручки, пожалуйста».</p>

<p><strong>Нина Петровна:</strong> Хорошо. <span class="cn-word" data-tr="oʻn olti">Шестнадцать</span> тысяч.</p>

<p>У него <span class="cn-word" data-tr="oʻn besh">пятнадцать</span> тысяч. Шербек сказал: «<span class="cn-word" data-tr="kechirasiz">Извините</span>. Тогда <strong>одна</strong> ручка».</p>

<p>Нина Петровна <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказала</span>: «Нет. <strong>Две</strong> тетради и <strong>две</strong> ручки — <span class="cn-word" data-tr="oʻn besh">пятнадцать</span>».</p>

<p><strong>Шербек:</strong> Но это <span class="cn-word" data-tr="oʻn olti">шестнадцать</span>!</p>

<p><strong>Нина Петровна:</strong> Сегодня — пятнадцать. Первый день, новая школа.</p>

<p>Шербек сказал: «Спасибо!» У него есть <strong>две</strong> тетради, <strong>две</strong> ручки — и <span class="cn-word" data-tr="yaxshi kun">хороший день</span>.</p>''',
        "questions": [
            {
                "text": "Nega Nina Petrovna narxni oʻn olti emas, oʻn besh dedi?",
                "choices": [
                    "Sherbekda faqat oʻn besh ming bor edi, va u birinchi kun uchun "
                    "chegirma qildi",
                    "U hisobda xato qildi",
                    "Daftarlar arzonlashgan edi",
                    "Sherbek bitta ruchka oldi"
                ],
                "answer": 0,
                "explanation": "Sherbek bitta ruchkadan voz kechmoqchi boʻldi, lekin "
                               "sotuvchi «Нет» dedi va narxni pasaytirdi: «Сегодня — "
                               "пятнадцать. Первый день, новая школа». Bu hikoyaning "
                               "yumshoq yakuni.",
            },
            {
                "text": "Nega matnda «две тетради», lekin «два карандаша» boʻlar edi?",
                "choices": [
                    "Chunki тетрадь ayol jinsida, карандаш esa erkak jinsida",
                    "Chunki тетрадь koʻplikda",
                    "Chunki daftar qimmatroq",
                    "Bu ikki xil aytish usuli, farqi yoʻq"
                ],
                "answer": 0,
                "explanation": "Faqat 2 sonida jins farqi bor: ayol jinsi uchun "
                               "«две», erkak va oʻrta jins uchun «два». Uch va undan "
                               "keyingi sonlarda bu farq yoʻq: «три тетради», "
                               "«три карандаша».",
            },
            {
                "text": "Sherbek «одна ручка» dedi. Nega «один» emas?",
                "choices": [
                    "Chunki ручка ayol jinsida, «один» esa otga moslashadi",
                    "Chunki ruchka bitta edi",
                    "Chunki u kechirim soʻradi",
                    "Chunki narx past edi"
                ],
                "answer": 0,
                "explanation": "Sonlar orasida faqat «один» sifat kabi oʻzgaradi: "
                               "один (m.) / одна (f.) / одно (oʻrta). «Ручка» -а "
                               "bilan tugaydi — ayol jinsi, demak «одна».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-14 — У меня есть           KICHIK HAYOT LAVHASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "У меня есть всё",
        "summary": (
            "PR-14 matni. Bekzod buvisidan nega uyi kichkina ekanini soʻraydi. "
            "Buvijon javob bermaydi — u shunchaki sanay boshlaydi, va sanoq oxirida "
            "savolning oʻzi yoʻqoladi."
        ),
        "order":   14,
        "grammar": [
            {
                "pattern":  "У меня / у тебя / у неё есть …",
                "meaning":  "Rus tilida «ega boʻlmoq» feʼli yoʻq. Uning oʻrniga "
                            "«у + olmosh + есть + narsa» ishlatiladi — bu oʻzbekchadagi "
                            "«Menda … bor» bilan aynan bir xil qurilma.",
                "examples": ["У меня есть сад.", "У тебя есть телефон?"],
            },
            {
                "pattern":  "У dan keyin н- qoʻshiladi",
                "meaning":  "его → у него, её → у неё, их → у них. Bu faqat predlog "
                            "bilan boʻladi. Talaffuz: у него = [у н'иво], chunki -го "
                            "oxiri [во] boʻlib oʻqiladi.",
                "examples": ["У него есть кот.", "У них есть дом."],
            },
            {
                "pattern":  "есть — «bor», nomlash emas",
                "meaning":  "«Это дом» da есть qoʻyilmaydi (nomlash), «У меня есть дом» "
                            "da esa qoʻyiladi (mavjudlik). Tekshiruv: oʻzbekcha "
                            "tarjimada «bor» soʻzi bormi?",
                "examples": ["Это дом. (есть yoʻq)", "У меня есть дом. (есть bor)"],
            },
        ],
        "body": '''<p>Это <span class="cn-word" data-tr="kichkina">маленький</span> дом. Здесь <span class="cn-word" data-pos="verb" data-tr="yashaydi">живёт</span> бабушка. Её зовут Роза Каримовна.</p>

<p>Бекзод <span class="cn-word" data-pos="verb" data-tr="keldi">пришёл</span> и <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span>: «Бабушка, дом маленький. У тебя <span class="cn-word" data-tr="oz, kam">мало</span>?»</p>

<p>Бабушка сказала: «Мало? <strong>У меня есть</strong> <span class="cn-word" data-tr="bogʻ">сад</span>».</p>

<p>«И <strong>у меня есть</strong> <span class="cn-word" data-tr="olma daraxti">яблоня</span>. <span class="cn-word" data-tr="eski">Старая</span>, но хорошая».</p>

<p>«<strong>У меня есть</strong> кот. Его зовут Тиша. <strong>У него есть</strong> <span class="cn-word" data-tr="joy">место</span> — вот <span class="cn-word" data-tr="mana shu yerda">здесь</span>».</p>

<p>«<strong>У меня есть</strong> соседи. Нина Петровна и Олег. <strong>У них есть</strong> <span class="cn-word" data-tr="bolalar">дети</span>, и дети <span class="cn-word" data-tr="tez-tez">часто</span> здесь».</p>

<p>«<strong>У меня есть</strong> <span class="cn-word" data-tr="nevaralar">внуки</span>. Ты, Дилноза и Афсона».</p>

<p>Бекзод сказал: «А <span class="cn-word" data-tr="pul">деньги</span>?»</p>

<p>Бабушка сказала: «Деньги — это не всё. Сад есть, кот есть, соседи есть, внуки есть».</p>

<p>«Дом маленький, Бекзод. А <strong>у меня есть всё</strong>».</p>''',
        "questions": [
            {
                "text": "Buvijon Bekzodning savoliga qanday javob berdi?",
                "choices": [
                    "Javob bermadi — u shunchaki bor narsalarini sanab chiqdi",
                    "U uyning kichikligini tan oldi va xafa boʻldi",
                    "U katta uy olmoqchi ekanini aytdi",
                    "U pul haqida gapirmadi"
                ],
                "answer": 0,
                "explanation": "Buvijon «Мало?» deb qaytarib soʻradi va sanay boshladi: "
                               "bogʻ, olma daraxti, mushuk, qoʻshnilar, nevaralar. "
                               "Oxirida esa: «Дом маленький, Бекзод. А у меня есть "
                               "всё». Sanoq javobning oʻzi boʻldi.",
            },
            {
                "text": "Matnda «У него есть место» bor. Nega «у его» emas?",
                "choices": [
                    "Chunki «у» predlogidan keyin н- qoʻshiladi",
                    "Chunki кот erkak jinsida",
                    "Chunki bu koʻplik",
                    "Bu xato"
                ],
                "answer": 0,
                "explanation": "«У» predlogidan keyin его → у него, её → у неё, "
                               "их → у них. Egalik sifatida esa «его место» deb "
                               "qolaveradi — н- faqat predlog bilan paydo boʻladi. "
                               "Talaffuz: [у н'иво].",
            },
            {
                "text": "Nega «У меня есть сад» da «есть» bor, «Дом маленький» da esa "
                        "yoʻq?",
                "choices": [
                    "Birinchisi mavjudlikni aytadi («bogʻim bor»), ikkinchisi esa uyning "
                    "qanaqaligini",
                    "Chunki сад erkak jinsida",
                    "Chunki birinchisi uzunroq gap",
                    "Bu shunchaki uslub"
                ],
                "answer": 0,
                "explanation": "Tekshiruv oddiy: oʻzbekcha tarjimada «bor» soʻzi bormi? "
                               "«Bogʻim bor» — bor, demak есть kerak. «Uy kichkina» — "
                               "«bor» yoʻq, demak есть ham yoʻq. Bu PR-6 va PR-11 dagi "
                               "qoidalar bilan bir tizim.",
            },
        ],
    },
]
