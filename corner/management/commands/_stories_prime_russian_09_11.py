# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-9 … PR-11.

Toc: corner/management/commands/toc_prime_russian_readings.txt

⛔ AUDIO YOʻQ. 2026-08-09 dan boshlab bu toʻplamda audio yaratilmaydi
   (edge-tts ning ruscha ovozlari sifatsiz — foydalanuvchi rad etdi).
   Shuning uchun bu matnlar endi qatʼiy navbatma-navbat dialog boʻlishi
   SHART EMAS: hikoya, tavsif va dialog erkin aralashadi.

Shakl xilma-xilligi: 9 — bozor sahnasi (hikoya), 10 — kichik sir (sinfda),
11 — birinchi shaxsdan tanishtiruv matni.

Feʼl tizimi hali ochilmagan (PR-19 dan), shuning uchun tocdagi "narrative frame"
istisnosi ishlatilgan: есть · нет · зовут · живёт · работает · говорит ·
сказал(а)/сказали · пришёл/пришла/пришли · дал(а) · был/была/было/были —
hammasi cn-word izohi bilan. Vaqt va joy ravishlari (сегодня, здесь, там,
в субботу) lugʻat sifatida izohlanadi: tocdagi CLARITY qoidasi sahna
oʻzgarganda vaqt/joy soʻzini TALAB qiladi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_09_11.py --author=prime
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
    # PR-9 — koʻplik            HIKOYA (bozor sahnasi)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Рынок в субботу",
        "summary": (
            "PR-9 matni. Shanba kuni bozor: stollar, olmalar, kitoblar, lugʻatlar — "
            "deyarli har bir soʻz koʻplikda. Dilnoza va Afsona meva olgani boradi, "
            "lekin uydan boshqa narsa bilan qaytadi."
        ),
        "order":   9,
        "grammar": [
            {
                "pattern":  "-ы / -и koʻplik qoʻshimchasi",
                "meaning":  "Erkak va ayol jinsidagi otlarning asosiy koʻplik shakli. "
                            "Undosh yoki -а dan keyin -ы, yumshoq oxirlardan keyin -и.",
                "examples": ["стол → столы", "лимон → лимоны", "тетрадь → тетради"],
            },
            {
                "pattern":  "Г К Х Ж Ч Ш Щ dan keyin -и",
                "meaning":  "Imlo qoidasi: bu yettita harfdan keyin -ы hech qachon "
                            "yozilmaydi. Shuning uchun книга → книги, ручка → ручки, "
                            "врач → врачи.",
                "examples": ["книга → книги", "врач → врачи"],
            },
            {
                "pattern":  "люди — istisno",
                "meaning":  "«человек» (odam) ning koʻpligi butunlay boshqa soʻz: "
                            "люди. «человеки» degan shakl yoʻq. Xuddi shunday "
                            "ребёнок → дети.",
                "examples": ["Здесь люди.", "Рынок — это люди."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="shanba">Суббота</span>. Это <span class="cn-word" data-tr="bozor">рынок</span>. Здесь <span class="cn-word" data-pos="verb" data-tr="ishlaydi">работает</span> Олег.</p>

<p>Вот <strong>столы</strong>. Здесь <strong><span class="cn-word" data-tr="olmalar">яблоки</span></strong>, <strong><span class="cn-word" data-tr="limonlar">лимоны</span></strong> и <strong><span class="cn-word" data-tr="pomidorlar">помидоры</span></strong>. Там <strong><span class="cn-word" data-tr="kitoblar">книги</span></strong>, <strong><span class="cn-word" data-tr="daftarlar">тетради</span></strong> и <strong><span class="cn-word" data-tr="lugʻatlar">словари</span></strong>.</p>

<p>Сегодня <span class="cn-word" data-pos="verb" data-tr="kelishdi">пришли</span> Дилноза и Афсона. Дилноза <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказала</span>: «Вот яблоки!»</p>

<p>Но Афсона там. Афсона сказала: «Дилноза, а это что? Это <strong>книги</strong>?»</p>

<p>Олег сказал: «Это не только книги. Это <strong>словари</strong>. И вот <strong>тетради</strong>».</p>

<p>Олег <span class="cn-word" data-pos="verb" data-tr="berdi">дал</span> словарь. Афсона сказала: «Спасибо!»</p>

<p>Дилноза сказала: «А яблоки?» Афсона сказала: «Яблоки — <span class="cn-word" data-tr="ertaga">завтра</span>».</p>

<p>Рынок: не только помидоры и лимоны. Здесь <strong>книги</strong> и <strong>словари</strong>. И здесь <strong><span class="cn-word" data-tr="odamlar">люди</span></strong>.</p>''',
        "questions": [
            {
                "text": "Afsona bozordan nima olib qaytdi?",
                "choices": [
                    "Lugʻat",
                    "Olmalar",
                    "Pomidorlar",
                    "Daftar"
                ],
                "answer": 0,
                "explanation": "«Олег дал словарь» — Oleg lugʻat berdi, Afsona esa "
                               "«Спасибо!» dedi. Olmalarni esa ertagaga qoldirishdi: "
                               "«Яблоки — завтра».",
            },
            {
                "text": "Nega matnda «книгы» emas, «книги» deb yozilgan?",
                "choices": [
                    "Chunki Г К Х Ж Ч Ш Щ dan keyin -ы hech qachon yozilmaydi",
                    "Chunki книга ayol jinsida",
                    "Chunki bu istisno soʻz",
                    "Chunki urgʻu birinchi boʻgʻinda"
                ],
                "answer": 0,
                "explanation": "Bu yettita harf qoidasi. «Книга» Г bilan tugaydi, shuning "
                               "uchun koʻplikda -и keladi. Xuddi shu sabab «ручки» va "
                               "«врачи» da ham ishlaydi.",
            },
            {
                "text": "Matnning oxirgi soʻzi «люди». Bu qaysi soʻzning koʻpligi?",
                "choices": [
                    "человек — va bu istisno, butunlay boshqa soʻz",
                    "люд",
                    "люд­ина",
                    "друг"
                ],
                "answer": 0,
                "explanation": "«Человек» (odam) ning koʻpligi «люди». Qoida boʻyicha "
                               "«человеки» boʻlishi kerak edi, lekin bunday shakl yoʻq — "
                               "bu yodlanadigan istisno, xuddi ребёнок → дети kabi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-10 — мой / твой / его / её        KICHIK SIR (sinfda)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Чей это телефон?",
        "summary": (
            "PR-10 matni. Sherbek sinfda telefon topib oladi va u kimniki ekanini "
            "hech kim bilmaydi. Javob ekrandagi suratda turgan edi — kichik sirli "
            "hikoya."
        ),
        "order":   10,
        "grammar": [
            {
                "pattern":  "Чей? Чья? Чьё? Чьи?",
                "meaning":  "«Kimning?» savoli otning jinsiga moslashadi: чей телефон "
                            "(m.), чья тетрадь (f.), чьё окно (oʻrta), чьи книги "
                            "(koʻplik).",
                "examples": ["Чей это телефон?", "Чья это тетрадь?"],
            },
            {
                "pattern":  "мой / моя / моё / мои",
                "meaning":  "Egalik soʻzi EGAGA emas, egalik qilingan NARSANING jinsiga "
                            "moslashadi. Shuning uchun bir odam «мой телефон» va «моя "
                            "тетрадь» deydi — oʻzgargani ot, ega emas.",
                "examples": ["Это не мой телефон.", "Моя тетрадь!"],
            },
            {
                "pattern":  "его / её / их",
                "meaning":  "«Uning» va «ularning» hech qachon oʻzgarmaydi. Talaffuzi "
                            "diqqat talab qiladi: его = [йиво], chunki -го oxiri "
                            "[во] boʻlib oʻqiladi.",
                "examples": ["Это её телефон.", "Может, его?"],
            },
        ],
        "body": '''<p>Вот класс. Вот стол. И вот <span class="cn-word" data-tr="telefon">телефон</span>. Шербек <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span>: «<strong>Чей</strong> это <strong>телефон</strong>?»</p>

<p>Дилноза <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказала</span>: «Это не <strong>мой</strong> телефон. <strong>Мой</strong> — здесь».</p>

<p>Шербек сказал: «А <strong>чья</strong> это <span class="cn-word" data-tr="daftar">тетрадь</span>?»</p>

<p>«<strong>Моя</strong>! Спасибо, Шербек».</p>

<p>Тетрадь — Дилноза. Но <strong>чей</strong> телефон?</p>

<p><span class="cn-word" data-tr="keyin, soʻng">Потом</span> <span class="cn-word" data-pos="verb" data-tr="keldi">пришёл</span> Жасур. Жасур сказал: «Это не <strong>мой</strong> телефон. Вот <strong>мой</strong>».</p>

<p>Шербек сказал: «А здесь <span class="cn-word" data-tr="surat">фото</span>. Это Афсона. И вот <strong>её</strong> кот Барсик».</p>

<p>Дилноза сказала: «<span class="cn-word" data-tr="demak">Значит</span>, это <strong>её</strong> телефон! Афсона — <span class="cn-word" data-tr="dugona">подруга</span>».</p>

<p>Телефон Афсона. Тетрадь Дилноза. А <span class="cn-word" data-tr="javob">ответ</span> <span class="cn-word" data-pos="verb" data-tr="edi">был</span> здесь, <span class="cn-word" data-tr="hamma vaqt, boshidan">всё время</span>.</p>''',
        "questions": [
            {
                "text": "Telefon kimniki ekanini nima aytdi?",
                "choices": [
                    "Telefondagi surat — unda Afsona va uning mushugi Barsik bor edi",
                    "Jasur aytdi",
                    "Telefonda ism yozilgan edi",
                    "Oʻqituvchi aytdi"
                ],
                "answer": 0,
                "explanation": "Sherbek suratni koʻrdi: «Это Афсона. И вот её кот». "
                               "Shundan keyin Dilnoza «Значит, это её телефон!» dedi. "
                               "Javob boshidanoq telefonning oʻzida turgan edi.",
            },
            {
                "text": "Nega «чей телефон» lekin «чья тетрадь»?",
                "choices": [
                    "Chunki телефон erkak jinsida, тетрадь esa ayol jinsida",
                    "Chunki telefon kattaroq narsa",
                    "Chunki тетрадь koʻplikda",
                    "Bu shunchaki ikki xil aytish usuli"
                ],
                "answer": 0,
                "explanation": "«Чей?» savoli ham otning jinsiga moslashadi. Телефон "
                               "undosh bilan tugaydi — erkak jinsi, demak чей. Тетрадь "
                               "esa -ь bilan tugagan ayol jinsidagi ot, demak чья.",
            },
            {
                "text": "Matnda «её телефон» va «её кот» bor. Nega «её» ikki marta bir "
                        "xil?",
                "choices": [
                    "Chunki его, её va их hech qachon oʻzgarmaydi",
                    "Chunki ikkala soʻz ham ayol jinsida",
                    "Bu xato, biri «его» boʻlishi kerak",
                    "Chunki ikkalasi ham koʻplikda"
                ],
                "answer": 0,
                "explanation": "«Кот» erkak jinsida, «телефон» ham erkak jinsida — lekin "
                               "bu ahamiyatsiz, chunki его/её/их umuman oʻzgarmaydi. "
                               "Мой/моя oʻzgaradi, её esa hech qachon. Bu darsning eng "
                               "oson qismi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-11 — feʼlsiz gaplar va tire        BIRINCHI SHAXS TANISHTIRUV
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Мой город — Ташкент",
        "summary": (
            "PR-11 matni. Afsona oʻz shahri haqida gapirib beradi. Matn ataylab "
            "feʼlsiz gaplarga qurilgan: qayerda tire turgani va qayerda turmaganiga "
            "diqqat qiling — bu darsning butun qoidasi shu yerda koʻrinadi."
        ),
        "order":   11,
        "grammar": [
            {
                "pattern":  "Ot + ot = tire",
                "meaning":  "Hozirgi zamonda «boʻlmoq» feʼli yoʻq. Agar gapning ikkala "
                            "tomoni ham ot boʻlsa, uning oʻrniga tire (—) qoʻyiladi.",
                "examples": ["Мой город — Ташкент.", "Мой папа — врач."],
            },
            {
                "pattern":  "Olmosh ega yoki sifat kesim → tire yoʻq",
                "meaning":  "Ega olmosh boʻlsa (Я ученица) yoki kesim sifat/ravish "
                            "boʻlsa (Кофе горячий, Мы дома) — tire qoʻyilmaydi.",
                "examples": ["Я ученица.", "Наш дом здесь."],
            },
            {
                "pattern":  "был / была / было / были",
                "meaning":  "Oʻtgan zamonda «boʻlmoq» qaytib keladi va otning jinsiga "
                            "moslashadi. Oʻzbekchadagi «edi» bilan bir xil vazifa, "
                            "faqat u jinsga qarab oʻzgaradi.",
                "examples": ["Здесь была школа.", "Это было давно."],
            },
        ],
        "body": '''<p>Меня зовут Афсона. Я <span class="cn-word" data-tr="oʻquvchi (qiz)">ученица</span>. <strong>Мой город — Ташкент.</strong></p>

<p>Ташкент — <span class="cn-word" data-tr="poytaxt">столица</span>. Здесь <span class="cn-word" data-tr="koʻchalar">улицы</span>, дома, <span class="cn-word" data-tr="bogʻlar">сады</span> и люди.</p>

<p><strong>Мой папа — врач.</strong> <strong>Моя мама — учитель.</strong> Мой брат Бекзод <span class="cn-word" data-tr="hali, hozircha">ещё</span> <span class="cn-word" data-tr="kichkina">маленький</span>.</p>

<p>Наш дом здесь. <span class="cn-word" data-tr="yaqin, yonida">Рядом</span> рынок, школа и <span class="cn-word" data-tr="kutubxona">библиотека</span>.</p>

<p><span class="cn-word" data-tr="ilgari, avval">Раньше</span> здесь <span class="cn-word" data-pos="verb" data-tr="edi (ayol)">была</span> <span class="cn-word" data-tr="kichkina">маленькая</span> школа. Теперь школа <span class="cn-word" data-tr="yangi">новая</span>. Это <span class="cn-word" data-tr="mening maktabim">моя школа</span>.</p>

<p>Моя школа — не только уроки. Моя школа — <span class="cn-word" data-tr="doʻstlar">друзья</span>: Дилноза, Жасур, Шербек.</p>

<p>Ташкент — не только улицы и дома. <strong>Ташкент — это люди.</strong> И <strong>Ташкент — мой город.</strong></p>''',
        "questions": [
            {
                "text": "Nega «Мой папа — врач» da tire bor, «Я ученица» da esa yoʻq?",
                "choices": [
                    "Birinchisida ikkala tomon ham ot; ikkinchisida ega — olmosh",
                    "Birinchisi uzunroq gap",
                    "Chunki «папа» -а bilan tugaydi",
                    "Bu shunchaki muallifning tanlovi"
                ],
                "answer": 0,
                "explanation": "Qoida: ot + ot = tire. «Мой папа» va «врач» — ikkalasi "
                               "ham ot, shuning uchun tire qoʻyiladi. «Я» esa olmosh, "
                               "olmoshdan keyin tire qoʻyilmaydi.",
            },
            {
                "text": "Matnda maktab haqida nima aytilgan?",
                "choices": [
                    "Ilgari kichkina maktab boʻlgan, hozir yangisi bor",
                    "Maktab hech qachon oʻzgarmagan",
                    "Maktab yopilgan",
                    "Maktab bozorning ichida"
                ],
                "answer": 0,
                "explanation": "«Раньше здесь была маленькая школа. Теперь школа "
                               "новая» — ilgari kichik maktab edi, endi yangisi. Diqqat: "
                               "oʻtgan zamonda «была» paydo boʻldi, hozirgi zamonda esa "
                               "feʼl yoʻq.",
            },
            {
                "text": "Nega «была», «был» emas?",
                "choices": [
                    "Chunki «школа» ayol jinsida",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki «школа» koʻplikda",
                    "Chunki muallif ayol kishi"
                ],
                "answer": 0,
                "explanation": "«Был» otning jinsiga moslashadi: был (m.) / была (f.) / "
                               "было (oʻrta) / были (koʻplik). «Школа» -а bilan tugaydi "
                               "— ayol jinsi, demak «была». Muallifning jinsi bu yerda "
                               "ahamiyatsiz.",
            },
        ],
    },
]
