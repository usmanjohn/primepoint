# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-27 … PR-28.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 27 — qoʻllanma / qoidalar matni, 28 — sharh (ikki
doʻstning bahsi). (24 xat, 25 biografiya, 26 oila portreti edi.)

Grammatika chegarasi (kumulyativ qoida):
  27-matn: мо́жно / нельзя́ / на́до / ну́жно / до́лжен (PR-27). «Не на́до» va
           «нельзя́» farqi oxirgi sahnada koʻrinadi. Нра́виться hali yoʻq.
  28-matn: кому + нра́вится + что (PR-28), нра́вится ↔ нра́вятся, oʻtgan
           zamonda нра́вились, va нра́виться ↔ люби́ть farqi.

Bu ikkala matn ham «мне / тебе́ / ему́» shakllarini ishlatadi. Ular PR-27 da
yopiq roʻyxat sifatida berilgan; kelishikning oʻzi PR-37 da tushuntiriladi.

Kelishiklar hali oʻrgatilmagan: matnlar bosh kelishikda, «кни́гу», «на
стене́» kabi iboralar butun boʻlak sifatida cn-word bilan izohlangan.

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
        "title":   "Пра́вила библиоте́ки",
        "summary": (
            "PR-27 matni. Kutubxona qoidalari — yettita qisqa band. Oxirida "
            "kutubxonachi Nina Petrovna devorda yozilmagan birinchi qoidani "
            "aytadi."
        ),
        "order":   27,
        "grammar": [
            {
                "pattern":  "мо́жно / нельзя́",
                "meaning":  "МО́ЖНО — mumkin, НЕЛЬЗЯ́ — mumkin emas. Diqqat: «не "
                            "мо́жно» degan soʻz rus tilida umuman yoʻq, нельзя́ — "
                            "alohida bitta soʻz.",
                "examples": ["Здесь мо́жно чита́ть.", "Здесь нельзя́ есть."],
            },
            {
                "pattern":  "на́до / ну́жно + infinitiv",
                "meaning":  "«Kerak». Shaxssiz qurilish — ega yoʻq. Kimga tegishli "
                            "ekanini мне / тебе́ / ему́ koʻrsatadi, xuddi oʻzbekchadagi "
                            "-GA kabi. НЕ НА́ДО = kerak emas (НЕЛЬЗЯ́ = taqiqlangan).",
                "examples": ["На́до прино́сить обра́тно.", "Здесь не на́до спеши́ть."],
            },
            {
                "pattern":  "до́лжен / должна́ / должны́",
                "meaning":  "Bu bittasi shaxssiz emas — yonida haqiqiy ega boʻladi va "
                            "sifat kabi jinsga moslashadi: телефо́н до́лжен, су́мка "
                            "должна́, ру́ки должны́.",
                "examples": ["Телефо́н до́лжен молча́ть.", "Ру́ки должны́ быть чи́стые."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="shahar (sifat)">Городска́я</span> <span class="cn-word" data-tr="kutubxona">библиоте́ка</span>. <span class="cn-word" data-tr="qoidalar">Пра́вила</span>.</p>

<p>1. Здесь <strong>мо́жно</strong> чита́ть, писа́ть и учи́ться. Это <span class="cn-word" data-tr="asosiy">гла́вное</span> пра́вило.</p>

<p>2. Здесь <strong>нельзя́</strong> есть. Чай пить тоже <strong>нельзя́</strong>. Вода́ — <strong>мо́жно</strong>.</p>

<p>3. Говори́ть <strong>мо́жно</strong>, но тихо. Громко <strong>нельзя́</strong>.</p>

<p>4. Телефо́н <strong>до́лжен</strong> молча́ть.</p>

<p>5. Ру́ки <strong>должны́</strong> быть <span class="cn-word" data-tr="toza">чи́стые</span>.</p>

<p>6. <span class="cn-word" data-tr="kitobni">Кни́гу</span> <strong>мо́жно</strong> чита́ть дома. Две <span class="cn-word" data-tr="hafta">неде́ли</span> — и <strong>на́до</strong> <span class="cn-word" data-pos="verb" data-tr="olib kelmoq">прино́сить</span> <span class="cn-word" data-tr="qaytarib">обра́тно</span>.</p>

<p>7. <span class="cn-word" data-tr="ruchka">Ру́чка</span> — <strong>нельзя́</strong>. <span class="cn-word" data-tr="qalam">Каранда́ш</span> — <strong>мо́жно</strong>.</p>

<p>Ни́на Петро́вна рабо́тает здесь давно́.</p>

<p>— Пра́вила <strong>ну́жно</strong> знать, — говори́т Ни́на Петро́вна. — Но пе́рвое пра́вило <span class="cn-word" data-tr="devorda">не на стене́</span>.</p>

<p>— А како́е? — спра́шивает Бекзод.</p>

<p>— Здесь <strong>мо́жно</strong> не спеши́ть, — говори́т Ни́на Петро́вна. — Дома <strong>на́до</strong> спеши́ть. В школе <strong>на́до</strong>. А здесь — <strong>не на́до</strong>.</p>

<p>Бекзод сиди́т и чита́ет. Ме́дленно.</p>''',
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
                "explanation": "«Здесь мо́жно не спеши́ть» — bu qoida devorda yozilmagan. "
                               "Uydayam, maktabdayam shoshish kerak, kutubxonada esa "
                               "kerak emas. Shuning uchun matn Bekzodning sekin "
                               "oʻqishi bilan tugaydi.",
            },
            {
                "text": "«Здесь нельзя́ есть» va «Здесь не на́до спеши́ть» — bu ikki "
                        "gap qanday farq qiladi?",
                "choices": [
                    "НЕЛЬЗЯ́ — taqiqlangan, НЕ НА́ДО — shart emas",
                    "Ikkalasi bir xil maʼnoda",
                    "НЕЛЬЗЯ́ — shart emas, НЕ НА́ДО — taqiqlangan",
                    "Birinchisi oʻtgan zamon"
                ],
                "answer": 0,
                "explanation": "Ovqatlanish taqiqlangan — «нельзя́». Shoshish esa "
                               "taqiqlanmagan, shunchaki kerak emas — «не на́до». Bu "
                               "farq muhim: «не мо́жно» degan soʻz esa umuman yoʻq, "
                               "нельзя́ oʻzi мо́жно ning inkori.",
            },
            {
                "text": "Nega matnda «телефо́н до́лжен», lekin «ру́ки должны́»?",
                "choices": [
                    "До́лжен sifat kabi moslashadi: телефо́н birlik erkak, ру́ки koʻplik",
                    "Chunki telefon jonsiz, qoʻllar jonli",
                    "Bu xato, ikkalasi ham «до́лжен» boʻlishi kerak",
                    "Chunki ikkinchisi oʻtgan zamon"
                ],
                "answer": 0,
                "explanation": "Boshqa qoida soʻzlaridan farqli oʻlaroq, до́лжен shaxssiz "
                               "emas — uning yonida haqiqiy ega boʻladi va u jinsga hamda "
                               "songa moslashadi: до́лжен / должна́ / должно́ / должны́.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-28 — мне нравится                          SHARH
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Что тебе́ нра́вится?",
        "summary": (
            "PR-28 matni. Afsona va Katya bitta filmni koʻrishdi va hamma narsada "
            "kelisha olmaydi. Oxirida ular nihoyat bitta narsada bir fikrga "
            "keladi."
        ),
        "order":   28,
        "grammar": [
            {
                "pattern":  "КОМУ + нра́вится + ЧТО",
                "meaning":  "Ega — yoqayotgan NARSA, «мне» emas. Oʻzbekchada ham "
                            "shunday: «menga bu film yoqadi» — film yoqyapti. Shuning "
                            "uchun bu qurilish oʻzbek oʻquvchi uchun teskari emas.",
                "examples": ["Мне нра́вится э́тот фильм.", "Тебе́ нра́вится чай?"],
            },
            {
                "pattern":  "нра́вится ↔ нра́вятся",
                "meaning":  "Feʼl narsaga moslashadi: bitta narsa — НРА́ВИТСЯ, koʻp "
                            "narsa — НРА́ВЯТСЯ. Infinitiv bilan har doim birlik: «мне "
                            "нра́вится чита́ть».",
                "examples": ["Мне нра́вятся актёры.", "Мне нра́вились коме́дии."],
            },
            {
                "pattern":  "нра́виться ↔ люби́ть",
                "meaning":  "НРА́ВИТЬСЯ — yoqadi, ega narsa; ЛЮБИ́ТЬ — yaxshi koʻradi, "
                            "ega odam. Odam haqida aytilganda farq katta: «ты мне "
                            "нра́вишься» va «я тебя́ люблю́» bir xil emas.",
                "examples": ["Ка́тя лю́бит смея́ться."],
            },
        ],
        "body": '''<p>Афсона и Катя смотре́ли фильм. Один фильм — два <span class="cn-word" data-tr="fikr">мне́ния</span>.</p>

<p>— <strong>Мне нра́вится</strong> э́тот фильм, — говори́т Афсона. — <strong>Мне нра́вится</strong> <span class="cn-word" data-tr="musiqa">му́зыка</span>. И <strong>мне нра́вятся</strong> <span class="cn-word" data-tr="aktyorlar">актёры</span>. Они игра́ют хорошо́.</p>

<p>— А <strong>мне</strong> фильм <strong>не нра́вится</strong>, — говори́т Катя. — Он <span class="cn-word" data-tr="uzun">до́лгий</span>. Мне бы́ло <span class="cn-word" data-tr="zerikarli">ску́чно</span>.</p>

<p>— <strong>Мне нра́вятся</strong> до́лгие фи́льмы, — говори́т Афсона. — До́лгий фильм — э́то до́лгая <span class="cn-word" data-tr="hikoya">исто́рия</span>.</p>

<p>— А <strong>мне нра́вятся</strong> <span class="cn-word" data-tr="komediyalar">коме́дии</span>, — говори́т Катя.</p>

<p>— <span class="cn-word" data-tr="ilgari">Ра́ньше</span> <strong>мне</strong> тоже <strong>нра́вились</strong> коме́дии, — говори́т Афсона. — Теперь — <span class="cn-word" data-tr="unchalik emas">не о́чень</span>.</p>

<p>Катя <strong>лю́бит</strong> смея́ться. Афсона <strong>лю́бит</strong> ду́мать.</p>

<p>Потом они пи́ли чай.</p>

<p>— Катя, а <strong>тебе́ нра́вится</strong> э́тот чай?</p>

<p>— Да. <strong>Мне</strong> очень <strong>нра́вится</strong>.</p>

<p>— <span class="cn-word" data-tr="nihoyat">Наконе́ц-то</span>! — говори́т Афсона. — Один фильм — два мне́ния. Один чай — одно́ мне́ние.</p>''',
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
                               "shuning uchun Afsona «Наконе́ц-то!» deydi.",
            },
            {
                "text": "«Мне нра́вится му́зыка» va «Мне нра́вятся актёры» — nega feʼl "
                        "har xil?",
                "choices": [
                    "Feʼl yoqayotgan narsaga moslashadi: му́зыка birlik, актёры koʻplik",
                    "Chunki birinchisi oʻtgan zamon",
                    "Chunki «мне» ikki xil maʼnoda ishlatilgan",
                    "Bu xato — ikkalasi ham «нра́вится» boʻlishi kerak"
                ],
                "answer": 0,
                "explanation": "Bu qurilishda ega — «мне» emas, yoqayotgan NARSA. "
                               "Shuning uchun feʼl oʻshanga qaraydi: bitta narsa — "
                               "нра́вится, koʻp narsa — нра́вятся. «Мне» ga qaramang, "
                               "u hech qachon feʼlga taʼsir qilmaydi.",
            },
            {
                "text": "«Ра́ньше мне нра́вились коме́дии» — nega -ЛИСЬ?",
                "choices": [
                    "Ega — коме́дии, koʻplik; qoʻshimcha gapirayotgan odamga qaramaydi",
                    "Chunki Afsona qiz",
                    "Chunki bu kelasi zamon",
                    "Chunki «мне» koʻplikda"
                ],
                "answer": 0,
                "explanation": "Oʻtgan zamonda ham feʼl egaga — yaʼni yoqqan NARSAGA — "
                               "moslashadi. Коме́дии koʻplik, demak нра́вились. Agar "
                               "bitta film boʻlganda «нра́вился фильм», kitob boʻlganda "
                               "«нра́вилась кни́га» boʻlardi. Bu PR-23 dan farq qiladi: "
                               "u yerda ega «я» edi.",
            },
        ],
    },
]
