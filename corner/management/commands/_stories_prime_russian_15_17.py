# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-15 … PR-17.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Shakl xilma-xilligi: 15 — xat (yangi janr), 16 — tanlov sahnasi,
17 — dasturxon ustidagi suhbat.

Feʼl tizimi hali ochilmagan (PR-19 dan), shuning uchun tocdagi "narrative frame"
istisnosi ishlatilgan: есть · нет · зовут · живёт · работает · говорит ·
сказал(а)/сказали · пришёл/пришла/пришли · дал(а) · был/была/было/были.
Kelishik talab qiladigan hech narsa ishlatilmagan — javoblar ravish bilan
beriladi (здесь, там, домой, завтра), xuddi PR-15 darsi oʻrgatgandek.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_15_17.py --author=prime
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
    # PR-15 — savol soʻzlari              XAT (yangi janr)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Кто? Что? Где?",
        "summary": (
            "PR-15 matni. Buvijon Dilnozaga xat yozadi — va xat deyarli butunlay "
            "savollardan iborat. Oxirida buvijon oʻzi bitta javob beradi, va aynan "
            "oʻsha javob xatning maʼnosini ochadi."
        ),
        "order":   15,
        "grammar": [
            {
                "pattern":  "Savol soʻzi + gap",
                "meaning":  "Rus tilida savol berish uchun yordamchi feʼl kerak emas. "
                            "Savol soʻzi oldinga chiqadi, qolgan gap oʻz joyida qoladi — "
                            "xuddi oʻzbekchadagidek.",
                "examples": ["Как дела?", "Где Бекзод?", "Когда урок?"],
            },
            {
                "pattern":  "где / куда / откуда",
                "meaning":  "Joyning uch savoli: ГДЕ — qayerda (harakat yoʻq), "
                            "КУДА — qayerga (harakat bor), ОТКУДА — qayerdan. "
                            "Oʻzbekcha qayerda/qayerga/qayerdan bilan aynan mos.",
                "examples": ["Где ты?", "Куда?", "Откуда?"],
            },
            {
                "pattern":  "почему / зачем",
                "meaning":  "ПОЧЕМУ sababni soʻraydi (javobi «Потому что…»), "
                            "ЗАЧЕМ esa maqsadni. Oʻzbekchadagi «nega» va «nima uchun» "
                            "farqiga oʻxshaydi.",
                "examples": ["Почему не здесь?", "Зачем это?"],
            },
        ],
        "body": '''<p>Дилноза, <span class="cn-word" data-tr="salom (xatda)">здравствуй</span>!</p>

<p><strong>Как</strong> дела? <strong>Как</strong> школа? <strong>Кто</strong> твой новый сосед — Жасур? <strong>Какой</strong> он?</p>

<p><strong>Где</strong> Бекзод? <strong>Почему</strong> он не здесь? Он <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span>: «Завтра, бабушка, завтра». А <strong>когда</strong> это «завтра»?</p>

<p>Афсона <span class="cn-word" data-pos="verb" data-tr="keldi (ayol)">пришла</span> сегодня. <strong>Откуда</strong> у неё <span class="cn-word" data-tr="shunday, bunaqa">такой</span> <span class="cn-word" data-tr="katta">большой</span> <span class="cn-word" data-tr="sumka">рюкзак</span>? И <strong>зачем</strong>? <span class="cn-word" data-tr="U yerda">Там</span> книги, тетради, ручки. <strong>Какие</strong> <span class="cn-word" data-tr="ogʻir">тяжёлые</span> книги!</p>

<p><span class="cn-word" data-tr="Va yana">И ещё</span>. <strong>Куда</strong> вы <span class="cn-word" data-tr="hammangiz">все</span>? Дом <span class="cn-word" data-tr="jimjit">тихий</span>. <span class="cn-word" data-tr="Bogʻ">Сад</span> тихий. Кот Тиша — тоже тихий.</p>

<p>Вот <span class="cn-word" data-tr="mening savolim">мой вопрос</span>: <strong>когда</strong> вы здесь?</p>

<p>А вот мой <span class="cn-word" data-tr="javob">ответ</span>: <span class="cn-word" data-tr="uy">дом</span> не тихий, <span class="cn-word" data-tr="qachon">когда</span> вы здесь.</p>

<p>Бабушка Роза.</p>''',
        "questions": [
            {
                "text": "Buvijon xatni nima uchun yozdi?",
                "choices": [
                    "U nabiralarini sogʻingan — uy ular kelmaganda jimjit",
                    "U Bekzoddan pul soʻramoqchi",
                    "U Afsonaning ryukzagi haqida shikoyat qilyapti",
                    "U yangi maktab haqida bilmoqchi"
                ],
                "answer": 0,
                "explanation": "Xat savollarga toʻla, lekin oxirida buvijon oʻzi javob "
                               "beradi: «дом не тихий, когда вы здесь» — “siz "
                               "kelganingizda uy jimjit boʻlmaydi”. Barcha savollar aslida "
                               "shu bitta gapga olib boradi.",
            },
            {
                "text": "Buvijon «Откуда у неё такой большой рюкзак?» deb soʻradi. "
                        "«Откуда» nimani soʻraydi?",
                "choices": [
                    "Qayerdan — narsaning kelib chiqishini",
                    "Qayerda — narsaning turgan joyini",
                    "Qayerga — yoʻnalishni",
                    "Qachon — vaqtni"
                ],
                "answer": 0,
                "explanation": "Joyning uch savoli: ГДЕ (qayerda) — harakat yoʻq, "
                               "КУДА (qayerga) — harakat bor, ОТКУДА (qayerdan) — "
                               "chiqish nuqtasi. Oʻzbekchada ham aynan shu uchlik bor, "
                               "shuning uchun bu farq sizga tanish.",
                            },
            {
                "text": "Xatda «Почему он не здесь?» va «Зачем?» ikkalasi ham bor. "
                        "Farqi nima?",
                "choices": [
                    "Почему sababni soʻraydi, зачем esa maqsadni",
                    "Почему rasmiy, зачем norasmiy",
                    "Farqi yoʻq",
                    "Почему faqat odam haqida ishlatiladi"
                ],
                "answer": 0,
                "explanation": "«Почему он не здесь?» — nima sababdan kelmadi (orqaga "
                               "qaraydi). «Зачем?» — ryukzak nima maqsadda kerak "
                               "(oldinga qaraydi). Ikkalasini «nega» deb tarjima qilsa "
                               "boʻladi, lekin rus tilida bu ikki xil savol.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-16 — этот / тот                  TANLOV SAHNASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Этот или тот?",
        "summary": (
            "PR-16 matni. Dilnoza va Bekzod uydan mushukcha tanlab olishga borishadi. "
            "Bekzod «bu» deb turadi, Dilnoza «anavi» deydi — va tanlovni oxirida "
            "mushukchaning oʻzi qiladi."
        ),
        "order":   16,
        "grammar": [
            {
                "pattern":  "этот / эта / это / эти",
                "meaning":  "Otga yopishadigan «bu» — otning jinsi va soniga moslashadi. "
                            "Mustaqil «это» (PR-6) dan farq qiladi: «Это кот» = "
                            "“bu — mushuk”, «Этот кот» = “bu mushuk”.",
                "examples": ["этот кот", "эта кошка", "эти котята"],
            },
            {
                "pattern":  "тот / та / то / те",
                "meaning":  "Uzoqdagi yoki boshqa narsani koʻrsatadi. Oʻzbekchadagi "
                            "«anavi». Rus tilida faqat ikki daraja bor (этот / тот), "
                            "oʻzbekchada esa uchta (bu / shu / u).",
                "examples": ["Этот или тот?", "Не эта, а та."],
            },
            {
                "pattern":  "вот / там",
                "meaning":  "ВОТ — «mana» (koʻrsatasiz), ТАМ — «ana u yerda» (uzoq). "
                            "ЗДЕСЬ esa joyni bildiradi, koʻrsatmaydi.",
                "examples": ["Вот он!", "Там маленький кот."],
            },
        ],
        "body": '''<p>Это <span class="cn-word" data-tr="boshpana, mushuklar uyi">приют</span>. Здесь <span class="cn-word" data-pos="verb" data-tr="yashaydi">живёт</span> Нина Петровна. И здесь <span class="cn-word" data-tr="mushukchalar">котята</span>.</p>

<p>Дилноза и Бекзод <span class="cn-word" data-pos="verb" data-tr="kelishdi">пришли</span> сюда. Нина Петровна <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказала</span>: «Вот <strong>эти</strong> котята. <strong>Этот</strong> — <span class="cn-word" data-tr="oq">белый</span>. <strong>Та</strong> — <span class="cn-word" data-tr="qora">чёрная</span>. А <strong>тот</strong> — <span class="cn-word" data-tr="kulrang">серый</span>».</p>

<p>Бекзод сказал: «<strong>Этот</strong>! Белый!»</p>

<p>Дилноза сказала: «Нет, не <strong>этот</strong>, а <strong>тот</strong>. Серый — <span class="cn-word" data-tr="tinch">спокойный</span>».</p>

<p>«Но белый — <span class="cn-word" data-tr="chiroyli">красивый</span>!»</p>

<p>«А серый — <span class="cn-word" data-tr="aqlli">умный</span>».</p>

<p><strong>Этот</strong> или <strong>тот</strong>? Бекзод — <strong>этот</strong>. Дилноза — <strong>тот</strong>. Нина Петровна <span class="cn-word" data-pos="verb" data-tr="dedi">говорит</span>: «<span class="cn-word" data-tr="Vaqt bor">Время есть</span>».</p>

<p><span class="cn-word" data-tr="Keyin">Потом</span> — <span class="cn-word" data-tr="jimjitlik">тишина</span>. <span class="cn-word" data-tr="kichkina">Маленький</span> серый кот — <span class="cn-word" data-tr="yonida">рядом</span>. Не белый. Серый.</p>

<p>Бекзод сказал: «<strong>Этот</strong>».</p>

<p>Дилноза сказала: «Бекзод, это <strong>тот</strong>! Мой <strong>тот</strong>».</p>

<p>Бекзод сказал: «Теперь он <strong>этот</strong>».</p>''',
        "questions": [
            {
                "text": "Nihoyat qaysi mushukcha tanlandi?",
                "choices": [
                    "Kulrang — u oʻzi Bekzodning yoniga keldi",
                    "Oq — Bekzod shuni xohlagan edi",
                    "Qora — Nina Petrovna shuni maslahat berdi",
                    "Hech qaysisi"
                ],
                "answer": 0,
                "explanation": "Bekzod oqni («этот»), Dilnoza esa kulrangni («тот») "
                               "xohlardi. Oxirida kulrang mushukcha oʻzi Bekzodning "
                               "yoniga keldi va Bekzod «Этот» dedi — chunki endi u "
                               "yaqin turibdi.",
            },
            {
                "text": "Nega bitta mushukcha matnda avval «тот», keyin «этот» deb "
                        "atalgan?",
                "choices": [
                    "Chunki u uzoqda edi, keyin yaqin keldi — «этот» yaqin, «тот» uzoq",
                    "Chunki uning rangi oʻzgardi",
                    "Chunki Dilnoza va Bekzod turli tillarda gapiryapti",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Bu hikoyaning butun hazili shunda. «Этот» — yaqindagi, "
                               "«тот» — uzoqdagi. Mushukcha yaqin kelgach, u avtomatik "
                               "«этот» boʻlib qoldi. Shuning uchun Bekzodning oxirgi "
                               "gapi: «Теперь он этот» — “endi u bu”.",
            },
            {
                "text": "«Вот эти котята» va «Это котята» — farqi nima?",
                "choices": [
                    "Birinchisi «mana bu mushukchalar», ikkinchisi «bular — mushukchalar»",
                    "Farqi yoʻq",
                    "Birinchisi koʻplik, ikkinchisi birlik",
                    "Ikkinchisi notoʻgʻri"
                ],
                "answer": 0,
                "explanation": "«Эти» otga yopishgan va unga moslashgan — u mushukchalarni "
                               "aniqlaydi. Mustaqil «это» esa nomlaydi va hech qachon "
                               "oʻzgarmaydi. Tekshiruv: oʻzbekchada «bu» dan keyin "
                               "toʻxtalsangiz — «это», toʻxtalmasangiz — «этот».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-17 — inkor                       DASTURXON USTIDA SUHBAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Нет, спасибо",
        "summary": (
            "PR-17 matni. Sergey Petrovich mehmonga keladi va muloyim rad javobini "
            "berishga urinadi — buvijonning dasturxoni esa boshqa fikrda. Yumshoq "
            "hazil bilan tugaydigan suhbat."
        ),
        "order":   17,
        "grammar": [
            {
                "pattern":  "нет / не",
                "meaning":  "НЕТ — savolga javob («yoʻq») va yoʻqlik; u oʻzi turadi. "
                            "НЕ — bitta soʻzni inkor qiladi va uning OLDIDA turadi. "
                            "Oʻzbekcha «emas» soʻzdan keyin keladi, ruscha «не» esa "
                            "oldin.",
                "examples": ["Нет, спасибо.", "Это не чай, а кофе."],
            },
            {
                "pattern":  "не X, а Y",
                "meaning":  "Tuzatish qurilmasi: «X emas, balki Y». А tuzatadi, "
                            "НО esa qarshilik bildiradi — ularni adashtirmaslik kerak.",
                "examples": ["Не чай, а кофе.", "Не я, а он."],
            },
            {
                "pattern":  "ни … ни …",
                "meaning":  "«Na … na …» — oʻzbekcha bilan aynan bir xil ishlaydi, "
                            "juftlikda keladi va ikkala qismni birdan inkor qiladi.",
                "examples": ["Ни чай, ни кофе.", "Ни это, ни то."],
            },
        ],
        "body": '''<p>Сергей Петрович — <span class="cn-word" data-tr="mehmon">гость</span>. Бабушка Роза и Бекзод — дома.</p>

<p><strong>Бабушка:</strong> Чай?</p>

<p><strong>Сергей Петрович:</strong> <strong>Нет</strong>, спасибо.</p>

<p><strong>Бабушка:</strong> Кофе?</p>

<p><strong>Сергей Петрович:</strong> <strong>Нет</strong>, спасибо. <strong>Ни</strong> чай, <strong>ни</strong> кофе. Спасибо, <span class="cn-word" data-tr="hamma narsa yaxshi">всё хорошо</span>.</p>

<p>Бабушка <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказала</span>: «Хорошо». <span class="cn-word" data-tr="Keyin">Потом</span> — <span class="cn-word" data-tr="non">хлеб</span>, <span class="cn-word" data-tr="pishiriq">лепёшка</span>, <span class="cn-word" data-tr="uzum">виноград</span>, <span class="cn-word" data-tr="qovun">дыня</span>.</p>

<p><strong>Сергей Петрович:</strong> Роза Каримовна, <strong>нет</strong>, спасибо! Это <strong>не</strong> <span class="cn-word" data-tr="tushlik">обед</span>, это <span class="cn-word" data-tr="ziyofat">пир</span>!</p>

<p><strong>Бабушка:</strong> Это <strong>не</strong> пир, <strong>а</strong> хлеб.</p>

<p>Бекзод <span class="cn-word" data-pos="verb" data-tr="dedi">сказал</span>: «Бабушка, он <strong>не</strong> <span class="cn-word" data-tr="och">голодный</span>».</p>

<p>Бабушка сказала: «Он <strong>не</strong> голодный, <strong>а</strong> <span class="cn-word" data-tr="odobli">вежливый</span>. Это <span class="cn-word" data-tr="ikki xil narsa">две разные вещи</span>».</p>

<p><span class="cn-word" data-tr="Bir soatdan keyin">Через час</span>: <strong>ни</strong> хлеба, <strong>ни</strong> дыни. Сергей Петрович сказал: «Спасибо. Всё <span class="cn-word" data-tr="mazali edi">было вкусно</span>».</p>

<p>Бабушка сказала: «<strong>Не</strong> “спасибо”, <strong>а</strong> “<span class="cn-word" data-tr="yana keling">до завтра</span>”».</p>''',
        "questions": [
            {
                "text": "Buvijon Sergey Petrovichning rad javobini qanday tushuntirdi?",
                "choices": [
                    "U och emas emas — u shunchaki odobli",
                    "U kasal boʻlgan",
                    "Unga ovqat yoqmagan",
                    "U shoshib turgan"
                ],
                "answer": 0,
                "explanation": "«Он не голодный, а вежливый. Это две разные вещи» — "
                               "“u och emas, balki odobli. Bu ikki xil narsa”. Bu yerda "
                               "«не X, а Y» qurilmasi hazilning oʻzagi boʻlib turibdi.",
            },
            {
                "text": "«Это не пир, а хлеб» — bu qanday qurilma?",
                "choices": [
                    "«Не X, а Y» — tuzatish: X emas, balki Y",
                    "«Не X, но Y» — qarshilik",
                    "Ikki inkor",
                    "Savol"
                ],
                "answer": 0,
                "explanation": "«Не X, а Y» tuzatadi. Bu yerda «но» ishlatilmaydi — «но» "
                               "qarshilik bildiradi («Школа новая, но маленькая»), «а» "
                               "esa notoʻgʻri fikrni almashtiradi.",
            },
            {
                "text": "Matnda «Ни чай, ни кофе» bor. Oʻzbekchada bu qanday aytiladi?",
                "choices": [
                    "Na choy, na qahva",
                    "Choy yoki qahva",
                    "Choy ham, qahva ham",
                    "Choy emas, qahva"
                ],
                "answer": 0,
                "explanation": "Ruscha «ни … ни …» va oʻzbekcha «na … na …» aynan bir xil "
                               "ishlaydi: ikkalasi ham juftlikda keladi va ikkala qismni "
                               "birdan inkor qiladi. Tarjimada hech nima oʻzgartirish "
                               "kerak emas.",
            },
        ],
    },
]
