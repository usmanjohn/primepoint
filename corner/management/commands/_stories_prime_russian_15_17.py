# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-15 … PR-17.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Shakl xilma-xilligi: 15 — xat (yangi janr), 16 — tanlov sahnasi,
17 — dasturxon ustidagi suhbat.

Feʼl tizimi hali ochilmagan (PR-19 dan), shuning uchun tocdagi "narrative frame"
istisnosi ishlatilgan: есть · нет · зову́т · живёт · рабо́тает · говори́т ·
сказа́л(а)/сказа́ли · пришёл/пришла́/пришли́ · дал(а) · был/была́/бы́ло/бы́ли.
Kelishik talab qiladigan hech narsa ishlatilmagan — javoblar ravish bilan
beriladi (здесь, там, домо́й, за́втра), xuddi PR-15 darsi oʻrgatgandek.

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
                "examples": ["Как дела́?", "Где Бекзо́д?", "Когда́ уро́к?"],
            },
            {
                "pattern":  "где / куда́ / отку́да",
                "meaning":  "Joyning uch savoli: ГДЕ — qayerda (harakat yoʻq), "
                            "КУДА́ — qayerga (harakat bor), ОТКУ́ДА — qayerdan. "
                            "Oʻzbekcha qayerda/qayerga/qayerdan bilan aynan mos.",
                "examples": ["Где ты?", "Куда́?", "Отку́да?"],
            },
            {
                "pattern":  "почему́ / заче́м",
                "meaning":  "ПОЧЕМУ́ sababni soʻraydi (javobi «Потому́ что…»), "
                            "ЗАЧЕ́М esa maqsadni. Oʻzbekchadagi «nega» va «nima uchun» "
                            "farqiga oʻxshaydi.",
                "examples": ["Почему́ не здесь?", "Заче́м э́то?"],
            },
        ],
        "body": '''<p>Дилно́за, <span class="cn-word" data-tr="salom (xatda)">здра́вствуй</span>!</p>

<p><strong>Как</strong> дела́? <strong>Как</strong> шко́ла? <strong>Кто</strong> твой но́вый сосе́д — Жасу́р? <strong>Како́й</strong> он?</p>

<p><strong>Где</strong> Бекзо́д? <strong>Почему́</strong> он не здесь? Он <span class="cn-word" data-pos="verb" data-tr="dedi">сказа́л</span>: «За́втра, ба́бушка, за́втра». А <strong>когда</strong> э́то «за́втра»?</p>

<p>Афсо́на <span class="cn-word" data-pos="verb" data-tr="keldi (ayol)">пришла́</span> сего́дня. <strong>Отку́да</strong> у неё <span class="cn-word" data-tr="shunday, bunaqa">тако́й</span> <span class="cn-word" data-tr="katta">большо́й</span> <span class="cn-word" data-tr="sumka">рюкза́к</span>? И <strong>заче́м</strong>? <span class="cn-word" data-tr="U yerda">Там</span> кни́ги, тетра́ди, ру́чки. <strong>Каки́е</strong> <span class="cn-word" data-tr="ogʻir">тяжёлые</span> кни́ги!</p>

<p><span class="cn-word" data-tr="Va yana">И ещё</span>. <strong>Куда́</strong> вы <span class="cn-word" data-tr="hammangiz">все</span>? Дом <span class="cn-word" data-tr="jimjit">ти́хий</span>. <span class="cn-word" data-tr="Bogʻ">Сад</span> ти́хий. Кот Ти́ша — то́же ти́хий.</p>

<p>Вот <span class="cn-word" data-tr="mening savolim">мой вопро́с</span>: <strong>когда́</strong> вы здесь?</p>

<p>А вот мой <span class="cn-word" data-tr="javob">отве́т</span>: <span class="cn-word" data-tr="uy">дом</span> не ти́хий, <span class="cn-word" data-tr="qachon">когда́</span> вы здесь.</p>

<p>Ба́бушка Роза́.</p>''',
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
                               "beradi: «дом не ти́хий, когда́ вы здесь» — “siz "
                               "kelganingizda uy jimjit boʻlmaydi”. Barcha savollar aslida "
                               "shu bitta gapga olib boradi.",
            },
            {
                "text": "Buvijon «Отку́да у неё тако́й большо́й рюкза́к?» deb soʻradi. "
                        "«Отку́да» nimani soʻraydi?",
                "choices": [
                    "Qayerdan — narsaning kelib chiqishini",
                    "Qayerda — narsaning turgan joyini",
                    "Qayerga — yoʻnalishni",
                    "Qachon — vaqtni"
                ],
                "answer": 0,
                "explanation": "Joyning uch savoli: ГДЕ (qayerda) — harakat yoʻq, "
                               "КУДА́ (qayerga) — harakat bor, ОТКУ́ДА (qayerdan) — "
                               "chiqish nuqtasi. Oʻzbekchada ham aynan shu uchlik bor, "
                               "shuning uchun bu farq sizga tanish.",
                            },
            {
                "text": "Xatda «Почему́ он не здесь?» va «Заче́м?» ikkalasi ham bor. "
                        "Farqi nima?",
                "choices": [
                    "Почему́ sababni soʻraydi, заче́м esa maqsadni",
                    "Почему́ rasmiy, заче́м norasmiy",
                    "Farqi yoʻq",
                    "Почему́ faqat odam haqida ishlatiladi"
                ],
                "answer": 0,
                "explanation": "«Почему́ он не здесь?» — nima sababdan kelmadi (orqaga "
                               "qaraydi). «Заче́м?» — ryukzak nima maqsadda kerak "
                               "(oldinga qaraydi). Ikkalasini «nega» deb tarjima qilsa "
                               "boʻladi, lekin rus tilida bu ikki xil savol.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-16 — этот / тот                  TANLOV SAHNASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Э́тот и́ли тот?",
        "summary": (
            "PR-16 matni. Dilnoza va Bekzod uydan mushukcha tanlab olishga borishadi. "
            "Bekzod «bu» deb turadi, Dilnoza «anavi» deydi — va tanlovni oxirida "
            "mushukchaning oʻzi qiladi."
        ),
        "order":   16,
        "grammar": [
            {
                "pattern":  "э́тот / э́та / э́то / э́ти",
                "meaning":  "Otga yopishadigan «bu» — otning jinsi va soniga moslashadi. "
                            "Mustaqil «э́то» (PR-6) dan farq qiladi: «Э́то кот» = "
                            "“bu — mushuk”, «Э́тот кот» = “bu mushuk”.",
                "examples": ["э́тот кот", "э́та ко́шка", "э́ти котя́та"],
            },
            {
                "pattern":  "тот / та / то / те",
                "meaning":  "Uzoqdagi yoki boshqa narsani koʻrsatadi. Oʻzbekchadagi "
                            "«anavi». Rus tilida faqat ikki daraja bor (э́тот / тот), "
                            "oʻzbekchada esa uchta (bu / shu / u).",
                "examples": ["Э́тот и́ли тот?", "Не э́та, а та."],
            },
            {
                "pattern":  "вот / там",
                "meaning":  "ВОТ — «mana» (koʻrsatasiz), ТАМ — «ana u yerda» (uzoq). "
                            "ЗДЕСЬ esa joyni bildiradi, koʻrsatmaydi.",
                "examples": ["Вот он!", "Там ма́ленький кот."],
            },
        ],
        "body": '''<p>Э́то <span class="cn-word" data-tr="boshpana, mushuklar uyi">прию́т</span>. Здесь <span class="cn-word" data-pos="verb" data-tr="yashaydi">живёт</span> Ни́на Петро́вна. И здесь <span class="cn-word" data-tr="mushukchalar">котя́та</span>.</p>

<p>Дилно́за и Бекзо́д <span class="cn-word" data-pos="verb" data-tr="kelishdi">пришли</span> сюда́. Ни́на Петро́вна <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказа́ла</span>: «Вот <strong>э́ти</strong> котя́та. <strong>Э́тот</strong> — <span class="cn-word" data-tr="oq">бе́лый</span>. <strong>Та</strong> — <span class="cn-word" data-tr="qora">чёрная</span>. А <strong>тот</strong> — <span class="cn-word" data-tr="kulrang">се́рый</span>».</p>

<p>Бекзо́д сказа́л: «<strong>Э́тот</strong>! Бе́лый!»</p>

<p>Дилно́за сказа́ла: «Нет, не <strong>э́тот</strong>, а <strong>тот</strong>. Се́рый — <span class="cn-word" data-tr="tinch">споко́йный</span>».</p>

<p>«Но бе́лый — <span class="cn-word" data-tr="chiroyli">краси́вый</span>!»</p>

<p>«А се́рый — <span class="cn-word" data-tr="aqlli">у́мный</span>».</p>

<p><strong>Э́тот</strong> и́ли <strong>тот</strong>? Бекзо́д — <strong>э́тот</strong>. Дилно́за — <strong>тот</strong>. Ни́на Петро́вна <span class="cn-word" data-pos="verb" data-tr="dedi">говори́т</span>: «<span class="cn-word" data-tr="Vaqt bor">Вре́мя есть</span>».</p>

<p><span class="cn-word" data-tr="Keyin">Пото́м</span> — <span class="cn-word" data-tr="jimjitlik">тишина́</span>. <span class="cn-word" data-tr="kichkina">Ма́ленький</span> се́рый кот — <span class="cn-word" data-tr="yonida">ря́дом</span>. Не бе́лый. Се́рый.</p>

<p>Бекзо́д сказа́л: «<strong>Э́тот</strong>».</p>

<p>Дилно́за сказа́ла: «Бекзо́д, э́то <strong>тот</strong>! Мой <strong>тот</strong>».</p>

<p>Бекзо́д сказа́л: «Тепе́рь он <strong>э́тот</strong>».</p>''',
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
                "explanation": "Bekzod oqni («э́тот»), Dilnoza esa kulrangni («тот») "
                               "xohlardi. Oxirida kulrang mushukcha oʻzi Bekzodning "
                               "yoniga keldi va Bekzod «Э́тот» dedi — chunki endi u "
                               "yaqin turibdi.",
            },
            {
                "text": "Nega bitta mushukcha matnda avval «тот», keyin «э́тот» deb "
                        "atalgan?",
                "choices": [
                    "Chunki u uzoqda edi, keyin yaqin keldi — «э́тот» yaqin, «тот» uzoq",
                    "Chunki uning rangi oʻzgardi",
                    "Chunki Dilnoza va Bekzod turli tillarda gapiryapti",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Bu hikoyaning butun hazili shunda. «Э́тот» — yaqindagi, "
                               "«тот» — uzoqdagi. Mushukcha yaqin kelgach, u avtomatik "
                               "«э́тот» boʻlib qoldi. Shuning uchun Bekzodning oxirgi "
                               "gapi: «Тепе́рь он э́тот» — “endi u bu”.",
            },
            {
                "text": "«Вот э́ти котя́та» va «Э́то котя́та» — farqi nima?",
                "choices": [
                    "Birinchisi «mana bu mushukchalar», ikkinchisi «bular — mushukchalar»",
                    "Farqi yoʻq",
                    "Birinchisi koʻplik, ikkinchisi birlik",
                    "Ikkinchisi notoʻgʻri"
                ],
                "answer": 0,
                "explanation": "«Э́ти» otga yopishgan va unga moslashgan — u mushukchalarni "
                               "aniqlaydi. Mustaqil «э́то» esa nomlaydi va hech qachon "
                               "oʻzgarmaydi. Tekshiruv: oʻzbekchada «bu» dan keyin "
                               "toʻxtalsangiz — «э́то», toʻxtalmasangiz — «э́тот».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-17 — inkor                       DASTURXON USTIDA SUHBAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Нет, спаси́бо",
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
                "examples": ["Нет, спаси́бо.", "Э́то не чай, а ко́фе."],
            },
            {
                "pattern":  "не X, а Y",
                "meaning":  "Tuzatish qurilmasi: «X emas, balki Y». А tuzatadi, "
                            "НО esa qarshilik bildiradi — ularni adashtirmaslik kerak.",
                "examples": ["Не чай, а ко́фе.", "Не я, а он."],
            },
            {
                "pattern":  "ни … ни …",
                "meaning":  "«Na … na …» — oʻzbekcha bilan aynan bir xil ishlaydi, "
                            "juftlikda keladi va ikkala qismni birdan inkor qiladi.",
                "examples": ["Ни чай, ни ко́фе.", "Ни э́то, ни то."],
            },
        ],
        "body": '''<p>Серге́й Петро́вич — <span class="cn-word" data-tr="mehmon">гость</span>. Ба́бушка Роза́ и Бекзо́д — до́ма.</p>

<p><strong>Ба́бушка:</strong> Чай?</p>

<p><strong>Серге́й Петро́вич:</strong> <strong>Нет</strong>, спаси́бо.</p>

<p><strong>Ба́бушка:</strong> Ко́фе?</p>

<p><strong>Серге́й Петро́вич:</strong> <strong>Нет</strong>, спаси́бо. <strong>Ни</strong> чай, <strong>ни</strong> ко́фе. Спаси́бо, <span class="cn-word" data-tr="hamma narsa yaxshi">всё хорошо́</span>.</p>

<p>Ба́бушка <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказа́ла</span>: «Хорошо́». <span class="cn-word" data-tr="Keyin">Пото́м</span> — <span class="cn-word" data-tr="non">хлеб</span>, <span class="cn-word" data-tr="pishiriq">лепёшка</span>, <span class="cn-word" data-tr="uzum">виногра́д</span>, <span class="cn-word" data-tr="qovun">ды́ня</span>.</p>

<p><strong>Серге́й Петро́вич:</strong> Роза́ Каримо́вна, <strong>нет</strong>, спаси́бо! Э́то <strong>не</strong> <span class="cn-word" data-tr="tushlik">обе́д</span>, э́то <span class="cn-word" data-tr="ziyofat">пир</span>!</p>

<p><strong>Ба́бушка:</strong> Э́то <strong>не</strong> пир, <strong>а</strong> хлеб.</p>

<p>Бекзо́д <span class="cn-word" data-pos="verb" data-tr="dedi">сказа́л</span>: «Ба́бушка, он <strong>не</strong> <span class="cn-word" data-tr="och">голо́дный</span>».</p>

<p>Ба́бушка сказа́ла: «Он <strong>не</strong> голо́дный, <strong>а</strong> <span class="cn-word" data-tr="odobli">ве́жливый</span>. Э́то <span class="cn-word" data-tr="ikki xil narsa">две ра́зные ве́щи</span>».</p>

<p><span class="cn-word" data-tr="Bir soatdan keyin">Че́рез час</span>: <strong>ни</strong> хлеба, <strong>ни</strong> ды́ни. Серге́й Петро́вич сказа́л: «Спаси́бо. Всё <span class="cn-word" data-tr="mazali edi">бы́ло вку́сно</span>».</p>

<p>Ба́бушка сказа́ла: «<strong>Не</strong> “спаси́бо”, <strong>а</strong> “<span class="cn-word" data-tr="yana keling">до за́втра</span>”».</p>''',
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
                "explanation": "«Он не голо́дный, а ве́жливый. Э́то две ра́зные ве́щи» — "
                               "“u och emas, balki odobli. Bu ikki xil narsa”. Bu yerda "
                               "«не X, а Y» qurilmasi hazilning oʻzagi boʻlib turibdi.",
            },
            {
                "text": "«Э́то не пир, а хлеб» — bu qanday qurilma?",
                "choices": [
                    "«Не X, а Y» — tuzatish: X emas, balki Y",
                    "«Не X, но Y» — qarshilik",
                    "Ikki inkor",
                    "Savol"
                ],
                "answer": 0,
                "explanation": "«Не X, а Y» tuzatadi. Bu yerda «но» ishlatilmaydi — «но» "
                               "qarshilik bildiradi («Шко́ла но́вая, но ма́ленькая»), «а» "
                               "esa notoʻgʻri fikrni almashtiradi.",
            },
            {
                "text": "Matnda «Ни чай, ни ко́фе» bor. Oʻzbekchada bu qanday aytiladi?",
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
