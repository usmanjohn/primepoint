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
istisnosi ishlatilgan: есть · нет · зову́т · живёт · рабо́тает · говори́т ·
сказа́л(а)/сказа́ли · пришёл/пришла́/пришли́ · дал(а) · был/была́/бы́ло/бы́ли —
hammasi cn-word izohi bilan. Vaqt va joy ravishlari (сего́дня, здесь, там,
в суббо́ту) lugʻat sifatida izohlanadi: tocdagi CLARITY qoidasi sahna
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
        "title":   "Ры́нок в суббо́ту",
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
                "examples": ["стол → столы́", "лимо́н → лимо́ны", "тетра́дь → тетра́ди"],
            },
            {
                "pattern":  "Г К Х Ж Ч Ш Щ dan keyin -и",
                "meaning":  "Imlo qoidasi: bu yettita harfdan keyin -ы hech qachon "
                            "yozilmaydi. Shuning uchun кни́га → кни́ги, ру́чка → ру́чки, "
                            "врач → врачи́.",
                "examples": ["кни́га → кни́ги", "врач → врачи́"],
            },
            {
                "pattern":  "лю́ди — istisno",
                "meaning":  "«челове́к» (odam) ning koʻpligi butunlay boshqa soʻz: "
                            "лю́ди. «челове́ки» degan shakl yoʻq. Xuddi shunday "
                            "ребёнок → де́ти.",
                "examples": ["Здесь лю́ди.", "Ры́нок — э́то лю́ди."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="shanba">Суббо́та</span>. Э́то <span class="cn-word" data-tr="bozor">ры́нок</span>. Здесь <span class="cn-word" data-pos="verb" data-tr="ishlaydi">рабо́тает</span> Оле́г.</p>

<p>Вот <strong>столы́</strong>. Здесь <strong><span class="cn-word" data-tr="olmalar">я́блоки</span></strong>, <strong><span class="cn-word" data-tr="limonlar">лимо́ны</span></strong> и <strong><span class="cn-word" data-tr="pomidorlar">помидо́ры</span></strong>. Там <strong><span class="cn-word" data-tr="kitoblar">кни́ги</span></strong>, <strong><span class="cn-word" data-tr="daftarlar">тетра́ди</span></strong> и <strong><span class="cn-word" data-tr="lugʻatlar">словари́</span></strong>.</p>

<p>Сего́дня <span class="cn-word" data-pos="verb" data-tr="kelishdi">пришли́</span> Дилно́за и Афсо́на. Дилно́за <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказа́ла</span>: «Вот я́блоки!»</p>

<p>Но Афсо́на там. Афсо́на сказа́ла: «Дилно́за, а э́то что? Э́то <strong>кни́ги</strong>?»</p>

<p>Оле́г сказа́л: «Э́то не то́лько кни́ги. Э́то <strong>словари́</strong>. И вот <strong>тетра́ди</strong>».</p>

<p>Оле́г <span class="cn-word" data-pos="verb" data-tr="berdi">дал</span> слова́рь. Афсо́на сказа́ла: «Спаси́бо!»</p>

<p>Дилно́за сказа́ла: «А я́блоки?» Афсо́на сказа́ла: «Я́блоки — <span class="cn-word" data-tr="ertaga">за́втра</span>».</p>

<p>Ры́нок: не то́лько помидо́ры и лимо́ны. Здесь <strong>кни́ги</strong> и <strong>словари́</strong>. И здесь <strong><span class="cn-word" data-tr="odamlar">лю́ди</span></strong>.</p>''',
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
                "explanation": "«Оле́г дал слова́рь» — Oleg lugʻat berdi, Afsona esa "
                               "«Спаси́бо!» dedi. Olmalarni esa ertagaga qoldirishdi: "
                               "«Я́блоки — за́втра».",
            },
            {
                "text": "Nega matnda «кни́гы» emas, «кни́ги» deb yozilgan?",
                "choices": [
                    "Chunki Г К Х Ж Ч Ш Щ dan keyin -ы hech qachon yozilmaydi",
                    "Chunki кни́га ayol jinsida",
                    "Chunki bu istisno soʻz",
                    "Chunki urgʻu birinchi boʻgʻinda"
                ],
                "answer": 0,
                "explanation": "Bu yettita harf qoidasi. «Кни́га» Г bilan tugaydi, shuning "
                               "uchun koʻplikda -и keladi. Xuddi shu sabab «ру́чки» va "
                               "«врачи́» da ham ishlaydi.",
            },
            {
                "text": "Matnning oxirgi soʻzi «лю́ди». Bu qaysi soʻzning koʻpligi?",
                "choices": [
                    "челове́к — va bu istisno, butunlay boshqa soʻz",
                    "лю́д",
                    "люд­и́на",
                    "друг"
                ],
                "answer": 0,
                "explanation": "«Челове́к» (odam) ning koʻpligi «лю́ди». Qoida boʻyicha "
                               "«челове́ки» boʻlishi kerak edi, lekin bunday shakl yoʻq — "
                               "bu yodlanadigan istisno, xuddi ребёнок → де́ти kabi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-10 — мой / твой / его́ / её        KICHIK SIR (sinfda)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Чей э́то телефо́н?",
        "summary": (
            "PR-10 matni. Sherbek sinfda telefon topib oladi va u kimniki ekanini "
            "hech kim bilmaydi. Javob ekrandagi suratda turgan edi — kichik sirli "
            "hikoya."
        ),
        "order":   10,
        "grammar": [
            {
                "pattern":  "Чей? Чья? Чьё? Чьи?",
                "meaning":  "«Kimning?» savoli otning jinsiga moslashadi: чей телефо́н "
                            "(m.), чья тетра́дь (f.), чьё окно́ (oʻrta), чьи кни́ги "
                            "(koʻplik).",
                "examples": ["Чей э́то телефо́н?", "Чья э́то тетра́дь?"],
            },
            {
                "pattern":  "мой / моя́ / моё / мои́",
                "meaning":  "Egalik soʻzi EGAGA emas, egalik qilingan NARSANING jinsiga "
                            "moslashadi. Shuning uchun bir odam «мой телефо́н» va «моя́ "
                            "тетра́дь» deydi — oʻzgargani ot, ega emas.",
                "examples": ["Э́то не мой телефо́н.", "Моя́ тетра́дь!"],
            },
            {
                "pattern":  "его́ / её / их",
                "meaning":  "«Uning» va «ularning» hech qachon oʻzgarmaydi. Talaffuzi "
                            "diqqat talab qiladi: его́ = [йиво́], chunki -го oxiri "
                            "[во] boʻlib oʻqiladi.",
                "examples": ["Э́то её телефо́н.", "Мо́жет, его́?"],
            },
        ],
        "body": '''<p>Вот класс. Вот стол. И вот <span class="cn-word" data-tr="telefon">телефо́н</span>. Шербе́к <span class="cn-word" data-pos="verb" data-tr="dedi">сказа́л</span>: «<strong>Чей</strong> э́то <strong>телефо́н</strong>?»</p>

<p>Дилно́за <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказа́ла</span>: «Э́то не <strong>мой</strong> телефо́н. <strong>Мой</strong> — здесь».</p>

<p>Шербе́к сказа́л: «А <strong>чья</strong> э́то <span class="cn-word" data-tr="daftar">тетра́дь</span>?»</p>

<p>«<strong>Моя́</strong>! Спаси́бо, Шербе́к».</p>

<p>Тетра́дь — Дилно́за. Но <strong>чей</strong> телефо́н?</p>

<p><span class="cn-word" data-tr="keyin, soʻng">Пото́м</span> <span class="cn-word" data-pos="verb" data-tr="keldi">пришёл</span> Жасу́р. Жасу́р сказа́л: «Э́то не <strong>мой</strong> телефо́н. Вот <strong>мой</strong>».</p>

<p>Шербе́к сказа́л: «А здесь <span class="cn-word" data-tr="surat">фо́то</span>. Э́то Афсо́на. И вот <strong>её</strong> кот Ба́рсик».</p>

<p>Дилно́за сказа́ла: «<span class="cn-word" data-tr="demak">Зна́чит</span>, э́то <strong>её</strong> телефо́н! Афсо́на — <span class="cn-word" data-tr="dugona">подру́га</span>».</p>

<p>Телефо́н Афсо́на. Тетра́дь Дилно́за. А <span class="cn-word" data-tr="javob">отве́т</span> <span class="cn-word" data-pos="verb" data-tr="edi">был</span> здесь, <span class="cn-word" data-tr="hamma vaqt, boshidan">всё вре́мя</span>.</p>''',
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
                "explanation": "Sherbek suratni koʻrdi: «Э́то Афсо́на. И вот её кот». "
                               "Shundan keyin Dilnoza «Зна́чит, э́то её телефо́н!» dedi. "
                               "Javob boshidanoq telefonning oʻzida turgan edi.",
            },
            {
                "text": "Nega «чей телефо́н» lekin «чья тетра́дь»?",
                "choices": [
                    "Chunki телефо́н erkak jinsida, тетра́дь esa ayol jinsida",
                    "Chunki telefon kattaroq narsa",
                    "Chunki тетра́дь koʻplikda",
                    "Bu shunchaki ikki xil aytish usuli"
                ],
                "answer": 0,
                "explanation": "«Чей?» savoli ham otning jinsiga moslashadi. Телефо́н "
                               "undosh bilan tugaydi — erkak jinsi, demak чей. Тетра́дь "
                               "esa -ь bilan tugagan ayol jinsidagi ot, demak чья.",
            },
            {
                "text": "Matnda «её телефо́н» va «её кот» bor. Nega «её» ikki marta bir "
                        "xil?",
                "choices": [
                    "Chunki его́, её va их hech qachon oʻzgarmaydi",
                    "Chunki ikkala soʻz ham ayol jinsida",
                    "Bu xato, biri «его́» boʻlishi kerak",
                    "Chunki ikkalasi ham koʻplikda"
                ],
                "answer": 0,
                "explanation": "«Кот» erkak jinsida, «телефо́н» ham erkak jinsida — lekin "
                               "bu ahamiyatsiz, chunki его́/её/их umuman oʻzgarmaydi. "
                               "Мой/моя́ oʻzgaradi, её esa hech qachon. Bu darsning eng "
                               "oson qismi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-11 — feʼlsiz gaplar va tire        BIRINCHI SHAXS TANISHTIRUV
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Мой го́род — Ташке́нт",
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
                "examples": ["Мой го́род — Ташке́нт.", "Мой па́па — врач."],
            },
            {
                "pattern":  "Olmosh ega yoki sifat kesim → tire yoʻq",
                "meaning":  "Ega olmosh boʻlsa (Я учени́ца) yoki kesim sifat/ravish "
                            "boʻlsa (Ко́фе горя́чий, Мы до́ма) — tire qoʻyilmaydi.",
                "examples": ["Я учени́ца.", "Наш дом здесь."],
            },
            {
                "pattern":  "был / была́ / бы́ло / бы́ли",
                "meaning":  "Oʻtgan zamonda «boʻlmoq» qaytib keladi va otning jinsiga "
                            "moslashadi. Oʻzbekchadagi «edi» bilan bir xil vazifa, "
                            "faqat u jinsga qarab oʻzgaradi.",
                "examples": ["Здесь была́ шко́ла.", "Э́то бы́ло давно́."],
            },
        ],
        "body": '''<p>Меня́ зову́т Афсо́на. Я <span class="cn-word" data-tr="oʻquvchi (qiz)">учени́ца</span>. <strong>Мой го́род — Ташке́нт.</strong></p>

<p>Ташке́нт — <span class="cn-word" data-tr="poytaxt">столи́ца</span>. Здесь <span class="cn-word" data-tr="koʻchalar">у́лицы</span>, дома́, <span class="cn-word" data-tr="bogʻlar">сады́</span> и лю́ди.</p>

<p><strong>Мой па́па — врач.</strong> <strong>Моя́ ма́ма — учи́тель.</strong> Мой брат Бекзо́д <span class="cn-word" data-tr="hali, hozircha">ещё</span> <span class="cn-word" data-tr="kichkina">ма́ленький</span>.</p>

<p>Наш дом здесь. <span class="cn-word" data-tr="yaqin, yonida">Ря́дом</span> ры́нок, шко́ла и <span class="cn-word" data-tr="kutubxona">библиоте́ка</span>.</p>

<p><span class="cn-word" data-tr="ilgari, avval">Ра́ньше</span> здесь <span class="cn-word" data-pos="verb" data-tr="edi (ayol)">была́</span> <span class="cn-word" data-tr="kichkina">ма́ленькая</span> шко́ла. Тепе́рь шко́ла <span class="cn-word" data-tr="yangi">но́вая</span>. Э́то <span class="cn-word" data-tr="mening maktabim">моя́ шко́ла</span>.</p>

<p>Моя́ шко́ла — не то́лько уро́ки. Моя́ шко́ла — <span class="cn-word" data-tr="doʻstlar">друзья́</span>: Дилно́за, Жасу́р, Шербе́к.</p>

<p>Ташке́нт — не то́лько у́лицы и дома́. <strong>Ташке́нт — э́то лю́ди.</strong> И <strong>Ташке́нт — мой го́род.</strong></p>''',
        "questions": [
            {
                "text": "Nega «Мой па́па — врач» da tire bor, «Я учени́ца» da esa yoʻq?",
                "choices": [
                    "Birinchisida ikkala tomon ham ot; ikkinchisida ega — olmosh",
                    "Birinchisi uzunroq gap",
                    "Chunki «па́па» -а bilan tugaydi",
                    "Bu shunchaki muallifning tanlovi"
                ],
                "answer": 0,
                "explanation": "Qoida: ot + ot = tire. «Мой па́па» va «врач» — ikkalasi "
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
                "explanation": "«Ра́ньше здесь была́ ма́ленькая шко́ла. Тепе́рь шко́ла "
                               "но́вая» — ilgari kichik maktab edi, endi yangisi. Diqqat: "
                               "oʻtgan zamonda «была́» paydo boʻldi, hozirgi zamonda esa "
                               "feʼl yoʻq.",
            },
            {
                "text": "Nega «была́», «был» emas?",
                "choices": [
                    "Chunki «шко́ла» ayol jinsida",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki «шко́ла» koʻplikda",
                    "Chunki muallif ayol kishi"
                ],
                "answer": 0,
                "explanation": "«Был» otning jinsiga moslashadi: был (m.) / была́ (f.) / "
                               "бы́ло (oʻrta) / бы́ли (koʻplik). «Шко́ла» -а bilan tugaydi "
                               "— ayol jinsi, demak «была́». Muallifning jinsi bu yerda "
                               "ahamiyatsiz.",
            },
        ],
    },
]
