# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-21 … PR-23.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 21 — intervyu, 22 — yotoqxona sahnasi (dialog),
23 — kundalik daftar. (19 anketa, 20 kunlik tartib edi — takror yoʻq.)

Grammatika chegarasi (kumulyativ qoida):
  21-matn: faqat hozirgi zamon. I (PR-20) va II (PR-21) tuslanish.
           Notoʻgʻri feʼllar YOʻQ — ular PR-22 da.
  22-matn: hozirgi zamon + PR-22 notoʻgʻri feʼllari (живёт, ест, едя́т,
           хо́чет/хотя́т, пьёт, пи́шет, е́дет, дам).
  23-matn: oʻtgan zamon (PR-23) — birinchi marta. Hikoyachi qiz (Дилноза),
           shuning uchun «я» shakllari -ла bilan keladi va jins farqi
           matnning oʻzida koʻrinadi.

Kelishiklar hali oʻrgatilmagan (PR-29 dan), shuning uchun matnlar deyarli
butunlay bosh kelishikda yozilgan; «в школу», «у меня» kabi bir nechta ibora
butun boʻlak sifatida cn-word bilan izohlangan.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_21_23.py --author=prime
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
    # PR-21 — II tuslanish                INTERVYU
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Я говорю́ на трёх языка́х",
        "summary": (
            "PR-21 matni. Jurnalist Nina maktabga keladi va uch tilda gapiradigan "
            "Afsonadan intervyu oladi. Oxirida savol beradigan odam oʻzi "
            "oʻrganuvchiga aylanadi."
        ),
        "order":   21,
        "grammar": [
            {
                "pattern":  "II tuslanish: -ю, -ишь, -ит, -им, -ите, -ят",
                "meaning":  "Ikkinchi tuslanish. Oʻzak = infinitiv minus -ить/-еть: "
                            "говор-ю́, говор-и́шь, говор-и́т… «И qatori, oxirida Я». "
                            "Feʼl qaysi guruhda ekanini «они́» shaklidan bilib olinadi.",
                "examples": ["Я говорю́ по-ру́сски.", "Они́ говоря́т по-англи́йски."],
            },
            {
                "pattern":  "-ат (не -ят) после ж ш щ ч",
                "meaning":  "Shivirlovchidan keyin Я yozilmaydi (PR-4). Shuning uchun "
                            "oʻzagi ж, ш, щ, ч ga tugagan II tuslanish feʼllari "
                            "koʻplikda -АТ oladi: у́чат, спеша́т, слы́шат.",
                "examples": ["Я учу́ слова́.", "Мы не спеши́м."],
            },
            {
                "pattern":  "по-ру́сски / по-узбе́кски",
                "meaning":  "«Ruschada», «oʻzbekchada» — bu ravish, u hech qachon "
                            "oʻzgarmaydi. Til nomi bilan adashtirmang: русский язык — "
                            "til, по-русски — qanday gapirish.",
                "examples": ["Ты говори́шь по-ру́сски?", "Ба́бушка говори́т по-узбе́кски."],
            },
        ],
        "body": '''<p>Нина — <span class="cn-word" data-tr="jurnalist">журнали́ст</span>. Сегодня она в школе. Нина делает <span class="cn-word" data-tr="intervyu">интервью́</span>, а Афсона <span class="cn-word" data-pos="verb" data-tr="javob beradi">отвеча́ет</span>.</p>

<p>— Афсона, ты <strong>говори́шь</strong> по-ру́сски?</p>

<p>— Да, я <strong>говорю́</strong> по-ру́сски. И по-узбе́кски. И <span class="cn-word" data-tr="ozgina">немно́го</span> по-англи́йски.</p>

<p>— <span class="cn-word" data-tr="uch til">Три языка́</span>! Почему́ три?</p>

<p>— Бабушка <strong>говори́т</strong> только по-узбе́кски, — отвеча́ет Афсона. — Моя <span class="cn-word" data-tr="dugona">подру́га</span> Катя <strong>говори́т</strong> по-ру́сски. А интерне́т <strong>говори́т</strong> по-англи́йски.</p>

<p>— И какой язык трудный?</p>

<p>— Ру́сский. Я понимаю хорошо, но <strong>говорю́</strong> медленно.</p>

<p>— А что ты делаешь каждый день?</p>

<p>— Я <strong>учу́</strong> <span class="cn-word" data-tr="soʻzlar">слова́</span>. Пять слов — и всё. Я не <strong>спешу́</strong>.</p>

<p>Нина слушает и думает. Она <strong>говори́т</strong> только по-ру́сски. Один язык.</p>

<p>— Афсона, а как по-узбе́кски «<span class="cn-word" data-tr="rahmat">спаси́бо</span>»?</p>

<p>— Рахмат.</p>

<p>Нина <strong>говори́т</strong> медленно: «Рах-мат». <span class="cn-word" data-tr="Endi">Тепе́рь</span> она тоже <strong>у́чит</strong> слова́. <span class="cn-word" data-tr="birinchi soʻz">Пе́рвое сло́во</span> — «рахмат».</p>''',
        "questions": [
            {
                "text": "Nega Afsona uch tilda gapiradi?",
                "choices": [
                    "Har bir til hayotidagi bir odam yoki joy bilan bogʻliq",
                    "Maktabda uchta til majburiy",
                    "U tarjimon boʻlmoqchi",
                    "Oilasi uch mamlakatda yashaydi"
                ],
                "answer": 0,
                "explanation": "Afsona uchta sababni sanaydi: buvisi faqat oʻzbekcha "
                               "gapiradi, dugonasi Katya ruscha, internet esa inglizcha. "
                               "Yaʼni tillar unga darsdan emas, hayotdan kelgan.",
            },
            {
                "text": "Matnda «Я учу́ слова́» va «Я не спешу́» bor. «Они́» uchun bu "
                        "feʼllar qanday boʻladi?",
                "choices": [
                    "у́чат va спеша́т — Ч va Ш dan keyin -АТ yoziladi",
                    "у́чут va спешу́т",
                    "у́чят va спешя́т",
                    "у́чят va спеша́т"
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham II tuslanishda, demak koʻplikda -ЯТ kutilardi. "
                               "Lekin oʻzak Ч va Ш ga tugaydi, shivirlovchidan keyin esa "
                               "Я yozilmaydi (PR-4). Shuning uchun -АТ: у́чат, спеша́т. "
                               "Bu imlo qoidasi — talaffuzda farq deyarli sezilmaydi.",
            },
            {
                "text": "Intervyuning oxirida nima oʻzgardi?",
                "choices": [
                    "Savol beruvchi Nina oʻzi oʻrganuvchiga aylandi",
                    "Afsona ruschada gapirishni tashladi",
                    "Nina maqolani yozishdan voz kechdi",
                    "Afsona toʻrtinchi tilni boshladi"
                ],
                "answer": 0,
                "explanation": "Nina faqat bir tilda gapirardi. Oxirida u oʻzbekcha "
                               "«rahmat» soʻzini soʻradi va uni sekin takrorladi — "
                               "«Тепе́рь она тоже у́чит слова́». Afsonaning «kuniga besh "
                               "soʻz» usuli unga ham yuqdi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-22 — notoʻgʻri feʼllar           YOTOQXONA SAHNASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ку́хня в общежи́тии",
        "summary": (
            "PR-22 matni. Yotoqxona oshxonasida uch talaba — har biri oʻz ovqatini "
            "yeyapti. Jasur bir narsani sezadi va kechki ovqat birdan boshqacha "
            "tugaydi."
        ),
        "order":   22,
        "grammar": [
            {
                "pattern":  "есть — ем, ешь, ест, еди́м, еди́те, едя́т",
                "meaning":  "«Yemoq» feʼli hech qaysi tuslanishga oʻxshamaydi va "
                            "juftlab yodlanadi: дать — дам, дашь, даст, дади́м… "
                            "Diqqat: едя́т = yeydilar (есть), е́дут = ketadilar (е́хать).",
                "examples": ["Жасу́р ест пло́в.", "Они́ едя́т вме́сте."],
            },
            {
                "pattern":  "хоте́ть — birlikda Ч, koʻplikda Т",
                "meaning":  "Bitta feʼl ikkita tuslanishda: хочу́, хо́чешь, хо́чет "
                            "(I) — lekin хоти́м, хоти́те, хотя́т (II). Rus tilida bunday "
                            "feʼl deyarli bitta.",
                "examples": ["Оле́г хо́чет пло́в.", "Они́ хотя́т пло́в."],
            },
            {
                "pattern":  "живёт · пьёт · пи́шет · е́дет",
                "meaning":  "Oʻzagi oʻzgaradigan feʼllar oddiy I tuslanish "
                            "qoʻshimchalarini oladi. Urgʻu qoʻshimchaga tushsa, "
                            "Е oʻrniga Ё yoziladi: живёшь, пьёт.",
                "examples": ["Ка́тя пьёт чай.", "Оле́г е́дет домо́й."],
            },
        ],
        "body": '''<p>Вечер. <span class="cn-word" data-tr="yotoqxona">Общежи́тие</span>. <span class="cn-word" data-tr="oshxona">Ку́хня</span>. Здесь Жасур, Олег и Катя.</p>

<p>Жасур <strong>живёт</strong> здесь один <span class="cn-word" data-tr="oy">ме́сяц</span>. Олег и Катя <strong>живу́т</strong> здесь <span class="cn-word" data-tr="ancha vaqtdan beri">давно́</span>.</p>

<p>Жасур <strong>ест</strong> плов. Олег <strong>ест</strong> хлеб и <span class="cn-word" data-tr="pishloq">сыр</span>. Катя <strong>пьёт</strong> чай.</p>

<p>— Жасур, что это? — <span class="cn-word" data-pos="verb" data-tr="soʻraydi">спра́шивает</span> Олег.</p>

<p>— Это плов. Моя мама готовит плов в субботу.</p>

<p>Олег <strong>хо́чет</strong> плов. Катя тоже <strong>хо́чет</strong> плов. Они <strong>хотя́т</strong> плов, но <span class="cn-word" data-pos="verb" data-tr="jim turishadi">молча́т</span>.</p>

<p>Жасур <strong>ви́дит</strong> это.</p>

<p>— Олег, Катя! Я <strong>дам</strong> плов. Вы <strong>хоти́те</strong>?</p>

<p>— <strong>Хоти́м</strong>! — говорят Олег и Катя.</p>

<p>Теперь Жасур, Олег и Катя <strong>едя́т</strong> плов <span class="cn-word" data-tr="birga">вме́сте</span>.</p>

<p>— Дома мы тоже <strong>еди́м</strong> вместе, — говорит Жасур. — Плов <strong>лю́бит</strong> <span class="cn-word" data-tr="davra, hamrohlik">компа́нию</span>.</p>

<p>Катя <strong>пи́шет</strong> <span class="cn-word" data-tr="retsept">реце́пт</span>: «Плов — это <span class="cn-word" data-tr="guruch">рис</span>, <span class="cn-word" data-tr="goʻsht">мя́со</span>, <span class="cn-word" data-tr="sabzi">морко́вь</span> и <span class="cn-word" data-tr="piyoz">лук</span>».</p>

<p>— А в субботу я <strong>е́ду</strong> домой, — говорит Олег. — Завтра я <strong>гото́влю</strong> <span class="cn-word" data-tr="borsh (rus shoʻrvasi)">борщ</span>. Борщ тоже <strong>лю́бит</strong> компанию.</p>''',
        "questions": [
            {
                "text": "Nega Oleg va Katya oshdan soʻrashmadi?",
                "choices": [
                    "Ular xohlashardi, lekin jim turishdi — «молча́т»",
                    "Ular osh yoqtirmaydi",
                    "Ular allaqachon toʻygan edi",
                    "Jasur ularga ruxsat bermadi"
                ],
                "answer": 0,
                "explanation": "«Они хотя́т плов, но молча́т» — xohlash bor, soʻrash yoʻq. "
                               "Shuning uchun keyingi jumla muhim: «Жасур ви́дит это» — "
                               "u aytilmagan narsani koʻrdi va oʻzi taklif qildi.",
            },
            {
                "text": "«Олег хо́чет плов» va «Они хотя́т плов» — nega bitta feʼlning "
                        "qoʻshimchasi bunchalik boshqa?",
                "choices": [
                    "Хоте́ть birlikda I, koʻplikda II tuslanishda tuslanadi",
                    "Chunki bittasi oʻtgan zamon",
                    "Chunki «Олег» erkak jinsida",
                    "Bu ikki xil feʼl"
                ],
                "answer": 0,
                "explanation": "Хоте́ть — rus tilidagi deyarli yagona feʼl, u guruhini gap "
                               "oʻrtasida almashtiradi: birlikda Ч (хочу́, хо́чешь, "
                               "хо́чет), koʻplikda Т (хоти́м, хоти́те, хотя́т).",
            },
            {
                "text": "Matnda «они едя́т плов» va «я е́ду домой» bor. Bu ikki soʻz "
                        "nima farq qiladi?",
                "choices": [
                    "едя́т — yeydilar (есть), е́ду — ketaman transportda (е́хать)",
                    "Ikkalasi ham «yemoq», faqat shaxsi boshqa",
                    "едя́т — kelasi zamon, е́ду — hozirgi",
                    "едя́т — koʻplik, е́ду — oʻsha feʼlning birligi"
                ],
                "answer": 0,
                "explanation": "Bu ikki feʼl bir-biriga juda oʻxshaydi, lekin butunlay "
                               "boshqa: есть (yemoq) → ем, ест, едя́т; е́хать (transportda "
                               "ketmoq) → е́ду, е́дет, е́дут. Urgʻu ham yordam beradi: "
                               "[йидя́т] — [йе́ду].",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-23 — oʻtgan zamon                KUNDALIK DAFTAR
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Вчера́ был дождь",
        "summary": (
            "PR-23 matni. Dilnozaning kundalik daftaridan bir sahifa: yomgʻirli "
            "ertalab, sekin avtobus va ukasi Bekzod bilan bogʻliq kichkina bir "
            "narsa. Hikoyachi qiz, shuning uchun feʼllar -ЛА bilan keladi."
        ),
        "order":   23,
        "grammar": [
            {
                "pattern":  "-л / -ла / -ло / -ли",
                "meaning":  "Oʻtgan zamon shaxsga emas, JINSga qaraydi. Erkak -Л, ayol "
                            "-ЛА, oʻrta -ЛО, koʻplik -ЛИ. Oʻzbekchada bunday narsa yoʻq "
                            "(oʻqidim / oʻqiding — jins koʻrinmaydi), shuning uchun har "
                            "safar ega kimligini tekshiring.",
                "examples": ["Я была́ дома.", "Бекзо́д ждал."],
            },
            {
                "pattern":  "был / была́ / бы́ло / бы́ли",
                "meaning":  "Hozirgi zamonda «быть» aytilmaydi (Он дома), oʻtgan zamonda "
                            "esa majburiy (Он был дома). Ayol jinsida urgʻu oxiriga "
                            "koʻchadi: была́ — xuddi жила́, дала́, пила́ kabi.",
                "examples": ["Вчера́ был дождь.", "В школе бы́ло тепло́."],
            },
            {
                "pattern":  "шёл / шла / шли",
                "meaning":  "Идти́ feʼlining oʻtgan zamoni — butunlay boshqa oʻzak. "
                            "Ob-havo haqida ham shu feʼl ishlatiladi: ruschada yomgʻir "
                            "yogʻmaydi, u YURADI — шёл дождь.",
                "examples": ["Дождь шёл гро́мко.", "Я шла бы́стро."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="chorshanba">Среда́</span>.</p>

<p>Вчера́ <strong>был</strong> дождь.</p>

<p>Утром я <strong>шла</strong> <span class="cn-word" data-tr="maktabga">в шко́лу</span>. <span class="cn-word" data-tr="soyabon">Зонт</span> <strong>был</strong> дома. Дождь <strong>шёл</strong> тихо, потом громко.</p>

<p>Автобус <strong>шёл</strong> медленно. Я <strong>шла</strong> быстро. И я <strong>была́</strong> <span class="cn-word" data-tr="hoʻl">мо́края</span>.</p>

<p>В школе <strong>бы́ло</strong> <span class="cn-word" data-tr="issiq">тепло́</span>. Марина Олеговна <strong>дала́</strong> чай. Потом мы <strong>чита́ли</strong> и <strong>писа́ли</strong>. Я <span class="cn-word" data-pos="verb" data-tr="unutdim">забы́ла</span> дождь.</p>

<p>Вечером я <strong>была́</strong> дома. Бекзод <strong>ждал</strong>.</p>

<p>— Дилноза, я <strong>ждал</strong> утром тоже, — <span class="cn-word" data-pos="verb" data-tr="dedi (erkak)">сказа́л</span> Бекзод. — Я <strong>шёл</strong> медленно. Ты <strong>шла</strong> быстро.</p>

<p>Зонт <strong>был</strong> <span class="cn-word" data-tr="uning yonida">у него́</span>. Утром. А я не <strong>ви́дела</strong>.</p>

<p>Сегодня <span class="cn-word" data-tr="quyosh">со́лнце</span>. Но зонт <span class="cn-word" data-tr="menda">у меня́</span>.</p>

<p>Спасибо, Бекзод.</p>''',
        "questions": [
            {
                "text": "Nega Bekzod ertalab Dilnozaga soyabonni bera olmadi?",
                "choices": [
                    "Bekzod sekin yurdi, Dilnoza esa tez ketib qoldi",
                    "Bekzod soyabonni uyda unutdi",
                    "Dilnoza soyabonni olishni istamadi",
                    "Bekzod maktabga bormadi"
                ],
                "answer": 0,
                "explanation": "Bekzodning oʻz gapi: «Я ждал утром… Я шёл медленно. Ты "
                               "шла быстро». U soyabon bilan chiqqan edi, lekin ulgurmadi "
                               "— «А я не ви́дела».",
            },
            {
                "text": "Nega matnda «я шла» va «я была́» yozilgan, «я шёл» va «я был» "
                        "emas?",
                "choices": [
                    "Chunki hikoyachi — qiz; oʻtgan zamon jinsga qaraydi",
                    "Chunki «я» har doim -ЛА oladi",
                    "Chunki bu koʻplik shakli",
                    "Chunki bu hurmat shakli"
                ],
                "answer": 0,
                "explanation": "Rus tilida oʻtgan zamon shaxsni koʻrsatmaydi, JINSni "
                               "koʻrsatadi. Kundalikni Dilnoza yozyapti, shuning uchun "
                               "hamma «я» shakli -ЛА bilan: шла, была́, забы́ла, ви́дела. "
                               "Bekzod haqidagi feʼllar esa -Л bilan: ждал, шёл, сказа́л.",
            },
            {
                "text": "«Дождь шёл тихо, потом громко» — bu jumla ruscha haqida nimani "
                        "koʻrsatadi?",
                "choices": [
                    "Ruschada yomgʻir «yogʻmaydi», u yuradi — шёл дождь",
                    "Yomgʻir jonli narsa deb hisoblanadi",
                    "Bu xato, toʻgʻrisi «дождь был»",
                    "Шёл bu yerda «boshlandi» degani"
                ],
                "answer": 0,
                "explanation": "Идти́ feʼli ob-havo bilan ham ishlatiladi: шёл дождь, шёл "
                               "снег. Uni butun ibora sifatida yodlash kerak — "
                               "oʻzbekchaga «yomgʻir yogʻdi» deb tarjima qilinadi. "
                               "«Дождь» erkak jinsidagi ot, shuning uchun ШЁЛ.",
            },
        ],
    },
]
