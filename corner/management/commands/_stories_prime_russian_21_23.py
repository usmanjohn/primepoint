# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-21 … PR-23.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 21 — intervyu, 22 — yotoqxona sahnasi (dialog),
23 — kundalik daftar. (19 anketa, 20 kunlik tartib edi — takror yoʻq.)

Grammatika chegarasi (kumulyativ qoida):
  21-matn: faqat hozirgi zamon. I (PR-20) va II (PR-21) tuslanish.
           Notoʻgʻri feʼllar YOʻQ — ular PR-22 da.
  22-matn: hozirgi zamon + PR-22 notoʻgʻri feʼllari (живёт, ест, едят,
           хочет/хотят, пьёт, пишет, едет, дам).
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
        "title":   "Я говорю на трёх языках",
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
                            "говор-ю, говор-ишь, говор-ит… «И qatori, oxirida Я». "
                            "Feʼl qaysi guruhda ekanini «они» shaklidan bilib olinadi.",
                "examples": ["Я говорю по-русски.", "Они говорят по-английски."],
            },
            {
                "pattern":  "-ат (не -ят) после ж ш щ ч",
                "meaning":  "Shivirlovchidan keyin Я yozilmaydi (PR-4). Shuning uchun "
                            "oʻzagi ж, ш, щ, ч ga tugagan II tuslanish feʼllari "
                            "koʻplikda -АТ oladi: учат, спешат, слышат.",
                "examples": ["Я учу слова.", "Мы не спешим."],
            },
            {
                "pattern":  "по-русски / по-узбекски",
                "meaning":  "«Ruschada», «oʻzbekchada» — bu ravish, u hech qachon "
                            "oʻzgarmaydi. Til nomi bilan adashtirmang: русский язык — "
                            "til, по-русски — qanday gapirish.",
                "examples": ["Ты говоришь по-русски?", "Бабушка говорит по-узбекски."],
            },
        ],
        "body": '''<p>Нина — <span class="cn-word" data-tr="jurnalist">журналист</span>. Сегодня она в школе. Нина делает <span class="cn-word" data-tr="intervyu">интервью</span>, а Афсона <span class="cn-word" data-pos="verb" data-tr="javob beradi">отвечает</span>.</p>

<p>— Афсона, ты <strong>говоришь</strong> по-русски?</p>

<p>— Да, я <strong>говорю</strong> по-русски. И по-узбекски. И <span class="cn-word" data-tr="ozgina">немного</span> по-английски.</p>

<p>— <span class="cn-word" data-tr="uch til">Три языка</span>! Почему три?</p>

<p>— Бабушка <strong>говорит</strong> только по-узбекски, — отвечает Афсона. — Моя <span class="cn-word" data-tr="dugona">подруга</span> Катя <strong>говорит</strong> по-русски. А интернет <strong>говорит</strong> по-английски.</p>

<p>— И какой язык трудный?</p>

<p>— Русский. Я понимаю хорошо, но <strong>говорю</strong> медленно.</p>

<p>— А что ты делаешь каждый день?</p>

<p>— Я <strong>учу</strong> <span class="cn-word" data-tr="soʻzlar">слова</span>. Пять слов — и всё. Я не <strong>спешу</strong>.</p>

<p>Нина слушает и думает. Она <strong>говорит</strong> только по-русски. Один язык.</p>

<p>— Афсона, а как по-узбекски «<span class="cn-word" data-tr="rahmat">спасибо</span>»?</p>

<p>— Рахмат.</p>

<p>Нина <strong>говорит</strong> медленно: «Рах-мат». <span class="cn-word" data-tr="Endi">Теперь</span> она тоже <strong>учит</strong> слова. <span class="cn-word" data-tr="birinchi soʻz">Первое слово</span> — «рахмат».</p>''',
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
                "text": "Matnda «Я учу слова» va «Я не спешу» bor. «Они» uchun bu "
                        "feʼllar qanday boʻladi?",
                "choices": [
                    "учат va спешат — Ч va Ш dan keyin -АТ yoziladi",
                    "учут va спешут",
                    "учят va спешят",
                    "учят va спешат"
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham II tuslanishda, demak koʻplikda -ЯТ kutilardi. "
                               "Lekin oʻzak Ч va Ш ga tugaydi, shivirlovchidan keyin esa "
                               "Я yozilmaydi (PR-4). Shuning uchun -АТ: учат, спешат. "
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
                               "«Теперь она тоже учит слова». Afsonaning «kuniga besh "
                               "soʻz» usuli unga ham yuqdi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-22 — notoʻgʻri feʼllar           YOTOQXONA SAHNASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Кухня в общежитии",
        "summary": (
            "PR-22 matni. Yotoqxona oshxonasida uch talaba — har biri oʻz ovqatini "
            "yeyapti. Jasur bir narsani sezadi va kechki ovqat birdan boshqacha "
            "tugaydi."
        ),
        "order":   22,
        "grammar": [
            {
                "pattern":  "есть — ем, ешь, ест, едим, едите, едят",
                "meaning":  "«Yemoq» feʼli hech qaysi tuslanishga oʻxshamaydi va "
                            "juftlab yodlanadi: дать — дам, дашь, даст, дадим… "
                            "Diqqat: едят = yeydilar (есть), едут = ketadilar (ехать).",
                "examples": ["Жасур ест плов.", "Они едят вместе."],
            },
            {
                "pattern":  "хотеть — birlikda Ч, koʻplikda Т",
                "meaning":  "Bitta feʼl ikkita tuslanishda: хочу, хочешь, хочет "
                            "(I) — lekin хотим, хотите, хотят (II). Rus tilida bunday "
                            "feʼl deyarli bitta.",
                "examples": ["Олег хочет плов.", "Они хотят плов."],
            },
            {
                "pattern":  "живёт · пьёт · пишет · едет",
                "meaning":  "Oʻzagi oʻzgaradigan feʼllar oddiy I tuslanish "
                            "qoʻshimchalarini oladi. Urgʻu qoʻshimchaga tushsa, "
                            "Е oʻrniga Ё yoziladi: живёшь, пьёт.",
                "examples": ["Катя пьёт чай.", "Олег едет домой."],
            },
        ],
        "body": '''<p>Вечер. <span class="cn-word" data-tr="yotoqxona">Общежитие</span>. <span class="cn-word" data-tr="oshxona">Кухня</span>. Здесь Жасур, Олег и Катя.</p>

<p>Жасур <strong>живёт</strong> здесь один <span class="cn-word" data-tr="oy">месяц</span>. Олег и Катя <strong>живут</strong> здесь <span class="cn-word" data-tr="ancha vaqtdan beri">давно</span>.</p>

<p>Жасур <strong>ест</strong> плов. Олег <strong>ест</strong> хлеб и <span class="cn-word" data-tr="pishloq">сыр</span>. Катя <strong>пьёт</strong> чай.</p>

<p>— Жасур, что это? — <span class="cn-word" data-pos="verb" data-tr="soʻraydi">спрашивает</span> Олег.</p>

<p>— Это плов. Моя мама готовит плов в субботу.</p>

<p>Олег <strong>хочет</strong> плов. Катя тоже <strong>хочет</strong> плов. Они <strong>хотят</strong> плов, но <span class="cn-word" data-pos="verb" data-tr="jim turishadi">молчат</span>.</p>

<p>Жасур <strong>видит</strong> это.</p>

<p>— Олег, Катя! Я <strong>дам</strong> плов. Вы <strong>хотите</strong>?</p>

<p>— <strong>Хотим</strong>! — говорят Олег и Катя.</p>

<p>Теперь Жасур, Олег и Катя <strong>едят</strong> плов <span class="cn-word" data-tr="birga">вместе</span>.</p>

<p>— Дома мы тоже <strong>едим</strong> вместе, — говорит Жасур. — Плов <strong>любит</strong> <span class="cn-word" data-tr="davra, hamrohlik">компанию</span>.</p>

<p>Катя <strong>пишет</strong> <span class="cn-word" data-tr="retsept">рецепт</span>: «Плов — это <span class="cn-word" data-tr="guruch">рис</span>, <span class="cn-word" data-tr="goʻsht">мясо</span>, <span class="cn-word" data-tr="sabzi">морковь</span> и <span class="cn-word" data-tr="piyoz">лук</span>».</p>

<p>— А в субботу я <strong>еду</strong> домой, — говорит Олег. — Завтра я <strong>готовлю</strong> <span class="cn-word" data-tr="borsh (rus shoʻrvasi)">борщ</span>. Борщ тоже <strong>любит</strong> компанию.</p>''',
        "questions": [
            {
                "text": "Nega Oleg va Katya oshdan soʻrashmadi?",
                "choices": [
                    "Ular xohlashardi, lekin jim turishdi — «молчат»",
                    "Ular osh yoqtirmaydi",
                    "Ular allaqachon toʻygan edi",
                    "Jasur ularga ruxsat bermadi"
                ],
                "answer": 0,
                "explanation": "«Они хотят плов, но молчат» — xohlash bor, soʻrash yoʻq. "
                               "Shuning uchun keyingi jumla muhim: «Жасур видит это» — "
                               "u aytilmagan narsani koʻrdi va oʻzi taklif qildi.",
            },
            {
                "text": "«Олег хочет плов» va «Они хотят плов» — nega bitta feʼlning "
                        "qoʻshimchasi bunchalik boshqa?",
                "choices": [
                    "Хотеть birlikda I, koʻplikda II tuslanishda tuslanadi",
                    "Chunki bittasi oʻtgan zamon",
                    "Chunki «Олег» erkak jinsida",
                    "Bu ikki xil feʼl"
                ],
                "answer": 0,
                "explanation": "Хотеть — rus tilidagi deyarli yagona feʼl, u guruhini gap "
                               "oʻrtasida almashtiradi: birlikda Ч (хочу, хочешь, "
                               "хочет), koʻplikda Т (хотим, хотите, хотят).",
            },
            {
                "text": "Matnda «они едят плов» va «я еду домой» bor. Bu ikki soʻz "
                        "nima farq qiladi?",
                "choices": [
                    "едят — yeydilar (есть), еду — ketaman transportda (ехать)",
                    "Ikkalasi ham «yemoq», faqat shaxsi boshqa",
                    "едят — kelasi zamon, еду — hozirgi",
                    "едят — koʻplik, еду — oʻsha feʼlning birligi"
                ],
                "answer": 0,
                "explanation": "Bu ikki feʼl bir-biriga juda oʻxshaydi, lekin butunlay "
                               "boshqa: есть (yemoq) → ем, ест, едят; ехать (transportda "
                               "ketmoq) → еду, едет, едут. Urgʻu ham yordam beradi: "
                               "[йидят] — [йеду].",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-23 — oʻtgan zamon                KUNDALIK DAFTAR
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Вчера был дождь",
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
                "examples": ["Я была дома.", "Бекзод ждал."],
            },
            {
                "pattern":  "был / была / было / были",
                "meaning":  "Hozirgi zamonda «быть» aytilmaydi (Он дома), oʻtgan zamonda "
                            "esa majburiy (Он был дома). Ayol jinsida urgʻu oxiriga "
                            "koʻchadi: была — xuddi жила, дала, пила kabi.",
                "examples": ["Вчера был дождь.", "В школе было тепло."],
            },
            {
                "pattern":  "шёл / шла / шли",
                "meaning":  "Идти feʼlining oʻtgan zamoni — butunlay boshqa oʻzak. "
                            "Ob-havo haqida ham shu feʼl ishlatiladi: ruschada yomgʻir "
                            "yogʻmaydi, u YURADI — шёл дождь.",
                "examples": ["Дождь шёл громко.", "Я шла быстро."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="chorshanba">Среда</span>.</p>

<p>Вчера <strong>был</strong> дождь.</p>

<p>Утром я <strong>шла</strong> <span class="cn-word" data-tr="maktabga">в школу</span>. <span class="cn-word" data-tr="soyabon">Зонт</span> <strong>был</strong> дома. Дождь <strong>шёл</strong> тихо, потом громко.</p>

<p>Автобус <strong>шёл</strong> медленно. Я <strong>шла</strong> быстро. И я <strong>была</strong> <span class="cn-word" data-tr="hoʻl">мокрая</span>.</p>

<p>В школе <strong>было</strong> <span class="cn-word" data-tr="issiq">тепло</span>. Марина Олеговна <strong>дала</strong> чай. Потом мы <strong>читали</strong> и <strong>писали</strong>. Я <span class="cn-word" data-pos="verb" data-tr="unutdim">забыла</span> дождь.</p>

<p>Вечером я <strong>была</strong> дома. Бекзод <strong>ждал</strong>.</p>

<p>— Дилноза, я <strong>ждал</strong> утром тоже, — <span class="cn-word" data-pos="verb" data-tr="dedi (erkak)">сказал</span> Бекзод. — Я <strong>шёл</strong> медленно. Ты <strong>шла</strong> быстро.</p>

<p>Зонт <strong>был</strong> <span class="cn-word" data-tr="uning yonida">у него</span>. Утром. А я не <strong>видела</strong>.</p>

<p>Сегодня <span class="cn-word" data-tr="quyosh">солнце</span>. Но зонт <span class="cn-word" data-tr="menda">у меня</span>.</p>

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
                               "— «А я не видела».",
            },
            {
                "text": "Nega matnda «я шла» va «я была» yozilgan, «я шёл» va «я был» "
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
                               "hamma «я» shakli -ЛА bilan: шла, была, забыла, видела. "
                               "Bekzod haqidagi feʼllar esa -Л bilan: ждал, шёл, сказал.",
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
                "explanation": "Идти feʼli ob-havo bilan ham ishlatiladi: шёл дождь, шёл "
                               "снег. Uni butun ibora sifatida yodlash kerak — "
                               "oʻzbekchaga «yomgʻir yogʻdi» deb tarjima qilinadi. "
                               "«Дождь» erkak jinsidagi ot, shuning uchun ШЁЛ.",
            },
        ],
    },
]
