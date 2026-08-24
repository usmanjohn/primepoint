# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-27 … PR-28.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 27 — qoʻllanma / qoidalar matni, 28 — sharh (ikki
doʻstning bahsi). (24 xat, 25 biografiya, 26 oila portreti edi.)

Grammatika chegarasi (kumulyativ qoida):
  27-matn: можно / нельзя / надо / нужно / должен (PR-27). «Не надо» va
           «нельзя» farqi oxirgi sahnada koʻrinadi. Нравиться hali yoʻq.
  28-matn: кому + нравится + что (PR-28), нравится ↔ нравятся, oʻtgan
           zamonda нравились, va нравиться ↔ любить farqi.

Bu ikkala matn ham «мне / тебе / ему» shakllarini ishlatadi. Ular PR-27 da
yopiq roʻyxat sifatida berilgan; kelishikning oʻzi PR-37 da tushuntiriladi.

Kelishiklar hali oʻrgatilmagan: matnlar bosh kelishikda, «книгу», «на
стене» kabi iboralar butun boʻlak sifatida cn-word bilan izohlangan.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_27_28.py --author=prime
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
    # PR-27 — можно / нельзя / надо / должен       QOʻLLANMA MATNI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Правила библиотеки",
        "summary": (
            "PR-27 matni. Kutubxona qoidalari — yettita qisqa band. Oxirida "
            "kutubxonachi Nina Petrovna devorda yozilmagan birinchi qoidani "
            "aytadi."
        ),
        "order":   27,
        "grammar": [
            {
                "pattern":  "можно / нельзя",
                "meaning":  "МОЖНО — mumkin, НЕЛЬЗЯ — mumkin emas. Diqqat: «не "
                            "можно» degan soʻz rus tilida umuman yoʻq, нельзя — "
                            "alohida bitta soʻz.",
                "examples": ["Здесь можно читать.", "Здесь нельзя есть."],
            },
            {
                "pattern":  "надо / нужно + infinitiv",
                "meaning":  "«Kerak». Shaxssiz qurilish — ega yoʻq. Kimga tegishli "
                            "ekanini мне / тебе / ему koʻrsatadi, xuddi oʻzbekchadagi "
                            "-GA kabi. НЕ НАДО = kerak emas (НЕЛЬЗЯ = taqiqlangan).",
                "examples": ["Надо приносить обратно.", "Здесь не надо спешить."],
            },
            {
                "pattern":  "должен / должна / должны",
                "meaning":  "Bu bittasi shaxssiz emas — yonida haqiqiy ega boʻladi va "
                            "sifat kabi jinsga moslashadi: телефон должен, сумка "
                            "должна, руки должны.",
                "examples": ["Телефон должен молчать.", "Руки должны быть чистые."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="shahar (sifat)">Городская</span> <span class="cn-word" data-tr="kutubxona">библиотека</span>. <span class="cn-word" data-tr="qoidalar">Правила</span>.</p>

<p>1. Здесь <strong>можно</strong> читать, писать и учиться. Это <span class="cn-word" data-tr="asosiy">главное</span> правило.</p>

<p>2. Здесь <strong>нельзя</strong> есть. Чай пить тоже <strong>нельзя</strong>. Вода — <strong>можно</strong>.</p>

<p>3. Говорить <strong>можно</strong>, но тихо. Громко <strong>нельзя</strong>.</p>

<p>4. Телефон <strong>должен</strong> молчать.</p>

<p>5. Руки <strong>должны</strong> быть <span class="cn-word" data-tr="toza">чистые</span>.</p>

<p>6. <span class="cn-word" data-tr="kitobni">Книгу</span> <strong>можно</strong> читать дома. Две <span class="cn-word" data-tr="hafta">недели</span> — и <strong>надо</strong> <span class="cn-word" data-pos="verb" data-tr="olib kelmoq">приносить</span> <span class="cn-word" data-tr="qaytarib">обратно</span>.</p>

<p>7. <span class="cn-word" data-tr="ruchka">Ручка</span> — <strong>нельзя</strong>. <span class="cn-word" data-tr="qalam">Карандаш</span> — <strong>можно</strong>.</p>

<p>Нина Петровна работает здесь давно.</p>

<p>— Правила <strong>нужно</strong> знать, — говорит Нина Петровна. — Но первое правило <span class="cn-word" data-tr="devorda">не на стене</span>.</p>

<p>— А какое? — спрашивает Бекзод.</p>

<p>— Здесь <strong>можно</strong> не спешить, — говорит Нина Петровна. — Дома <strong>надо</strong> спешить. В школе <strong>надо</strong>. А здесь — <strong>не надо</strong>.</p>

<p>Бекзод сидит и читает. Медленно.</p>''',
        "questions": [
            {
                "text": "Nina Petrovna aytgan «birinchi qoida» nima?",
                "choices": [
                    "Kutubxonada shoshilmasa ham boʻladi",
                    "Telefonni oʻchirish kerak",
                    "Kitobni ikki haftada qaytarish kerak",
                    "Faqat qalam bilan yozish kerak"
                ],
                "answer": 0,
                "explanation": "«Здесь можно не спешить» — bu qoida devorda yozilmagan. "
                               "Uydayam, maktabdayam shoshish kerak, kutubxonada esa "
                               "kerak emas. Shuning uchun matn Bekzodning sekin "
                               "oʻqishi bilan tugaydi.",
            },
            {
                "text": "«Здесь нельзя есть» va «Здесь не надо спешить» — bu ikki "
                        "gap qanday farq qiladi?",
                "choices": [
                    "НЕЛЬЗЯ — taqiqlangan, НЕ НАДО — shart emas",
                    "Ikkalasi bir xil maʼnoda",
                    "НЕЛЬЗЯ — shart emas, НЕ НАДО — taqiqlangan",
                    "Birinchisi oʻtgan zamon"
                ],
                "answer": 0,
                "explanation": "Ovqatlanish taqiqlangan — «нельзя». Shoshish esa "
                               "taqiqlanmagan, shunchaki kerak emas — «не надо». Bu "
                               "farq muhim: «не можно» degan soʻz esa umuman yoʻq, "
                               "нельзя oʻzi можно ning inkori.",
            },
            {
                "text": "Nega matnda «телефон должен», lekin «руки должны»?",
                "choices": [
                    "Должен sifat kabi moslashadi: телефон birlik erkak, руки koʻplik",
                    "Chunki telefon jonsiz, qoʻllar jonli",
                    "Bu xato, ikkalasi ham «должен» boʻlishi kerak",
                    "Chunki ikkinchisi oʻtgan zamon"
                ],
                "answer": 0,
                "explanation": "Boshqa qoida soʻzlaridan farqli oʻlaroq, должен shaxssiz "
                               "emas — uning yonida haqiqiy ega boʻladi va u jinsga hamda "
                               "songa moslashadi: должен / должна / должно / должны.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-28 — мне нравится                          SHARH
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Что тебе нравится?",
        "summary": (
            "PR-28 matni. Afsona va Katya bitta filmni koʻrishdi va hamma narsada "
            "kelisha olmaydi. Oxirida ular nihoyat bitta narsada bir fikrga "
            "keladi."
        ),
        "order":   28,
        "grammar": [
            {
                "pattern":  "КОМУ + нравится + ЧТО",
                "meaning":  "Ega — yoqayotgan NARSA, «мне» emas. Oʻzbekchada ham "
                            "shunday: «menga bu film yoqadi» — film yoqyapti. Shuning "
                            "uchun bu qurilish oʻzbek oʻquvchi uchun teskari emas.",
                "examples": ["Мне нравится этот фильм.", "Тебе нравится чай?"],
            },
            {
                "pattern":  "нравится ↔ нравятся",
                "meaning":  "Feʼl narsaga moslashadi: bitta narsa — НРАВИТСЯ, koʻp "
                            "narsa — НРАВЯТСЯ. Infinitiv bilan har doim birlik: «мне "
                            "нравится читать».",
                "examples": ["Мне нравятся актёры.", "Мне нравились комедии."],
            },
            {
                "pattern":  "нравиться ↔ любить",
                "meaning":  "НРАВИТЬСЯ — yoqadi, ega narsa; ЛЮБИТЬ — yaxshi koʻradi, "
                            "ega odam. Odam haqida aytilganda farq katta: «ты мне "
                            "нравишься» va «я тебя люблю» bir xil emas.",
                "examples": ["Катя любит смеяться."],
            },
        ],
        "body": '''<p>Афсона и Катя смотрели фильм. Один фильм — два <span class="cn-word" data-tr="fikr">мнения</span>.</p>

<p>— <strong>Мне нравится</strong> этот фильм, — говорит Афсона. — <strong>Мне нравится</strong> <span class="cn-word" data-tr="musiqa">музыка</span>. И <strong>мне нравятся</strong> <span class="cn-word" data-tr="aktyorlar">актёры</span>. Они играют хорошо.</p>

<p>— А <strong>мне</strong> фильм <strong>не нравится</strong>, — говорит Катя. — Он <span class="cn-word" data-tr="uzun">долгий</span>. Мне было <span class="cn-word" data-tr="zerikarli">скучно</span>.</p>

<p>— <strong>Мне нравятся</strong> долгие фильмы, — говорит Афсона. — Долгий фильм — это долгая <span class="cn-word" data-tr="hikoya">история</span>.</p>

<p>— А <strong>мне нравятся</strong> <span class="cn-word" data-tr="komediyalar">комедии</span>, — говорит Катя.</p>

<p>— <span class="cn-word" data-tr="ilgari">Раньше</span> <strong>мне</strong> тоже <strong>нравились</strong> комедии, — говорит Афсона. — Теперь — <span class="cn-word" data-tr="unchalik emas">не очень</span>.</p>

<p>Катя <strong>любит</strong> смеяться. Афсона <strong>любит</strong> думать.</p>

<p>Потом они пили чай.</p>

<p>— Катя, а <strong>тебе нравится</strong> этот чай?</p>

<p>— Да. <strong>Мне</strong> очень <strong>нравится</strong>.</p>

<p>— <span class="cn-word" data-tr="nihoyat">Наконец-то</span>! — говорит Афсона. — Один фильм — два мнения. Один чай — одно мнение.</p>''',
        "questions": [
            {
                "text": "Afsona va Katya nimada bir fikrga keldi?",
                "choices": [
                    "Choy haqida — ikkalasiga ham yoqdi",
                    "Film haqida — ikkalasiga ham yoqdi",
                    "Komediyalar haqida",
                    "Hech narsada kelisha olmadi"
                ],
                "answer": 0,
                "explanation": "Film, uning uzunligi va janri haqida ular butunlay "
                               "boshqacha oʻyladi. Faqat choy haqida bir fikr chiqdi — "
                               "shuning uchun Afsona «Наконец-то!» deydi.",
            },
            {
                "text": "«Мне нравится музыка» va «Мне нравятся актёры» — nega feʼl "
                        "har xil?",
                "choices": [
                    "Feʼl yoqayotgan narsaga moslashadi: музыка birlik, актёры koʻplik",
                    "Chunki birinchisi oʻtgan zamon",
                    "Chunki «мне» ikki xil maʼnoda ishlatilgan",
                    "Bu xato — ikkalasi ham «нравится» boʻlishi kerak"
                ],
                "answer": 0,
                "explanation": "Bu qurilishda ega — «мне» emas, yoqayotgan NARSA. "
                               "Shuning uchun feʼl oʻshanga qaraydi: bitta narsa — "
                               "нравится, koʻp narsa — нравятся. «Мне» ga qaramang, "
                               "u hech qachon feʼlga taʼsir qilmaydi.",
            },
            {
                "text": "«Раньше мне нравились комедии» — nega -ЛИСЬ?",
                "choices": [
                    "Ega — комедии, koʻplik; qoʻshimcha gapirayotgan odamga qaramaydi",
                    "Chunki Afsona qiz",
                    "Chunki bu kelasi zamon",
                    "Chunki «мне» koʻplikda"
                ],
                "answer": 0,
                "explanation": "Oʻtgan zamonda ham feʼl egaga — yaʼni yoqqan NARSAGA — "
                               "moslashadi. Комедии koʻplik, demak нравились. Agar "
                               "bitta film boʻlganda «нравился фильм», kitob boʻlganda "
                               "«нравилась книга» boʻlardi. Bu PR-23 dan farq qiladi: "
                               "u yerda ega «я» edi.",
            },
        ],
    },
]
