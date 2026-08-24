# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-29 … PR-31.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 29 — ilmiy-ommabop (tilning oʻzi haqida), 30 — kichik
sirli hikoya, 31 — kitob sharhi (yozma tavsiya). 28 ham «sharh» edi, lekin
u ikki doʻstning ogʻzaki bahsi — 31 esa yozma matn, shakli boshqa.

Grammatika chegarasi (kumulyativ qoida):
  29-matn: kelishik tizimining oʻzi haqida — shuning uchun matn ichida
           kelishik shakllari MISOL sifatida keladi. Bu istisno emas:
           matnning mavzusi aynan shu.
  30-matn: предложный «где?» maʼnosida (PR-30). Har bir jumla boshqa joy —
           в/на tanlovi matnning oʻzida takrorlanib turadi.
  31-matn: предложный «о чём?» maʼnosida (PR-31), «об» shakli bilan birga.

Hali oʻrgatilmagan kelishiklar (В.п., Р.п., Т.п.) matnlarda ishlatilmaydi;
«ключей нет», «в другом кармане» kabi bir nechta ibora butun boʻlak
sifatida cn-word bilan izohlangan.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_29_31.py --author=prime
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
    # PR-29 — kelishik xaritasi              ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Одно слово — шесть форм",
        "summary": (
            "PR-29 matni. Rus tilidagi kelishiklar haqida qisqa ilmiy-ommabop "
            "matn: nega bitta soʻzning oltita shakli bor, oʻzbek tilida ham "
            "nega shunday, va nima uchun bu tartibsizlik emas — tizim."
        ),
        "order":   29,
        "grammar": [
            {
                "pattern":  "падеж — kelishik",
                "meaning":  "Soʻzning oxiri uning gapdagi ishini koʻrsatadi. Rus "
                            "tilida oltita kelishik bor, oʻzbek tilida ham oltita — "
                            "shuning uchun tushuncha oʻzbek oʻquvchi uchun yangi emas.",
                "examples": ["Книга. Книги. Книге. Книгу.", "Одно слово — шесть форм."],
            },
            {
                "pattern":  "род — jins",
                "meaning":  "Rus tilida shakl otning jinsiga bogʻliq: «книга» va "
                            "«стол» boshqacha turlanadi. Oʻzbekchada esa qoʻshimcha "
                            "hamma soʻz uchun bitta — bu birinchi yangi qiyinchilik.",
                "examples": ["«Книга» и «стол» — формы разные."],
            },
            {
                "pattern":  "предлог — predlog",
                "meaning":  "Ikkinchi yangi narsa: ruschada koʻpincha predlog VA "
                            "qoʻshimcha birga ishlaydi. Bitta kelishik esa predlogsiz "
                            "umuman yashamaydi — предложный.",
                "examples": ["В школе. На работе. О книге."],
            },
        ],
        "body": '''<p>Слово «книга» — одно. Но <span class="cn-word" data-tr="shakllar">форм</span> у него шесть.</p>

<p>Книга. Книги. Книге. Книгу. Книгой. О книге.</p>

<p>Это один <span class="cn-word" data-tr="narsa, predmet">предмет</span>. Но каждая форма — это другая <span class="cn-word" data-tr="ish, vazifa">работа</span>.</p>

<p><strong>Книга</strong> лежит. <strong>Книгу</strong> читает Афсона. Мы говорим <strong>о книге</strong>. Один предмет, три формы, три роли.</p>

<p><span class="cn-word" data-tr="Yaxshi xabar">Хорошая новость</span>: в узбекском языке <strong>тоже</strong> есть <span class="cn-word" data-tr="kelishiklar">падежи</span>. Тоже шесть. Поэтому <span class="cn-word" data-tr="fikr, gʻoya">идея</span> не новая.</p>

<p>Что новое? <span class="cn-word" data-tr="uch narsa">Три вещи</span>.</p>

<p>Первое: <span class="cn-word" data-tr="jins">род</span>. «Книга» и «стол» — формы разные.</p>

<p>Второе: <span class="cn-word" data-tr="predloglar">предлоги</span>. В. На. О. С. Из.</p>

<p>Третье: один падеж не живёт <span class="cn-word" data-tr="predlogsiz">без предлога</span>. Это предложный. Он всегда с предлогом: <strong>в школе</strong>, <strong>на работе</strong>, <strong>о книге</strong>.</p>

<p>Шесть форм — это много? Может быть.</p>

<p>Но это не <span class="cn-word" data-tr="tartibsizlik">хаос</span>. Это <span class="cn-word" data-tr="tizim">система</span>. А система — это правила. И правила можно знать.</p>''',
        "questions": [
            {
                "text": "Matn oʻzbek tili haqida nima deydi?",
                "choices": [
                    "Oʻzbek tilida ham oltita kelishik bor, shuning uchun gʻoya yangi emas",
                    "Oʻzbek tilida kelishik yoʻq",
                    "Oʻzbek tilida oʻn ikkita kelishik bor",
                    "Oʻzbek tili rus tilidan kelishikni olgan"
                ],
                "answer": 0,
                "explanation": "«В узбекском языке тоже есть падежи. Тоже шесть. "
                               "Поэтому идея не новая» — matnning eng muhim jumlasi. "
                               "Kelishik tushunchasi oʻzbek oʻquvchi uchun tanish; "
                               "faqat qoʻshimchalar boshqa.",
            },
            {
                "text": "Matnga koʻra rus tilida oʻzbek tilidan farqli uch narsa nima?",
                "choices": [
                    "Jins, predloglar va predlogsiz yashamaydigan kelishik",
                    "Alifbo, urgʻu va soʻz tartibi",
                    "Feʼl, sifat va ravish",
                    "Koʻplik, inkor va savol"
                ],
                "answer": 0,
                "explanation": "Matn ularni raqamlab beradi: «Первое: род… Второе: "
                               "предлоги… Третье: один падеж не живёт без "
                               "предлога». Uchalasi ham oʻzbekchada yoʻq va aynan "
                               "shu joylarda xato qilinadi.",
            },
            {
                "text": "Matn nima bilan tugaydi va bu nega muhim?",
                "choices": [
                    "Bu tartibsizlik emas, tizim — tizimni esa bilib olsa boʻladi",
                    "Oltita shakl juda koʻp va uni yodlash mumkin emas",
                    "Kelishiklarni faqat bolalikdan oʻrganish mumkin",
                    "Rus tilida kelishiklar yoʻqolib bormoqda"
                ],
                "answer": 0,
                "explanation": "«Это не хаос. Это система. А система — это "
                               "правила. И правила можно знать» — matnning butun "
                               "maqsadi shu: qoʻrqitmaslik. Tartibsizlikni yodlab "
                               "boʻlmaydi, qoidalarni esa boʻladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-30 — предложный «где?»              KICHIK SIRLI HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Где мои ключи?",
        "summary": (
            "PR-30 matni. Jasur ertalab kalitlarini topa olmaydi. Butun oila "
            "qidiradi — va har bir qidirilgan joy предложный padejining yangi "
            "misoli. Javob eng oxirida, eng kutilmagan joyda."
        ),
        "order":   30,
        "grammar": [
            {
                "pattern":  "в + Предложный",
                "meaning":  "Ichi bor joy: в сумке, в комнате, в магазине, в "
                            "автобусе. Qoʻshimcha deyarli har doim -Е. Oʻzbekchadagi "
                            "-DA ning oʻzi, faqat predlog qoʻshiladi.",
                "examples": ["Телефон в сумке.", "Он был в магазине."],
            },
            {
                "pattern":  "на + Предложный",
                "meaning":  "Yuza yoki ochiq joy: на столе, на улице, на полу. Va "
                            "yodlanadigan roʻyxat: на работе, на рынке, на почте, "
                            "на уроке — bu yerda mantiq emas, odat ishlaydi.",
                "examples": ["Ключи были на столе.", "И на рынке. И на почте."],
            },
            {
                "pattern":  "на полу — -У roʻyxati",
                "meaning":  "Kichik yopiq roʻyxat: в лесу, в саду, на полу, в "
                            "шкафу, на берегу, в аэропорту. Ularning urgʻusi har "
                            "doim qoʻshimchada.",
                "examples": ["Бекзод смотрит на полу."],
            },
        ],
        "body": '''<p>Утром Жасур <span class="cn-word" data-pos="verb" data-tr="qidiradi">ищет</span> <span class="cn-word" data-tr="kalitlar">ключи</span>.</p>

<p>— Ключи были <strong>на столе</strong>, — говорит Жасур.</p>

<p>Но <strong>на столе</strong> только чай.</p>

<p>Жасур смотрит <strong>в</strong> <span class="cn-word" data-tr="sumkada">сумке</span>. Там книги, <span class="cn-word" data-tr="ruchka">ручка</span>, телефон. Но не ключи.</p>

<p>Жасур смотрит <strong>в</strong> <span class="cn-word" data-tr="kurtkada">куртке</span>. <strong>В кармане</strong> — <span class="cn-word" data-tr="pul">деньги</span>. Но не ключи.</p>

<p>Бекзод смотрит <strong>на полу</strong>. Мама смотрит <strong>в комнате</strong> и <strong>на кухне</strong>.</p>

<p>— Ты был вчера <strong>в магазине</strong>? — спрашивает мама.</p>

<p>— Да. И <strong>на рынке</strong>. И <strong>на</strong> <span class="cn-word" data-tr="pochtada">почте</span>. И <strong>в библиотеке</strong>.</p>

<p>— <span class="cn-word" data-tr="Demak">Значит</span>, ключи <strong>в Ташкенте</strong>, — говорит Бекзод.</p>

<p>Все смеются. Но <span class="cn-word" data-tr="kalitlar yoʻq">ключей нет</span>.</p>

<p>Потом Жасур идёт <strong>в школу</strong>. <strong>В автобусе</strong> он думает: «Где ключи?»</p>

<p>И <strong>в автобусе</strong> он слышит: «<span class="cn-word" data-tr="jaranglagan tovush">Дзинь</span>».</p>

<p>Ключи <strong>в кармане</strong>. Но <span class="cn-word" data-tr="boshqa choʻntakda">в другом кармане</span>.</p>

<p>Жасур смеялся <strong>в автобусе</strong>. Один.</p>''',
        "questions": [
            {
                "text": "Kalitlar qayerda ekan?",
                "choices": [
                    "Jasurning kurtkasida — lekin boshqa choʻntagida",
                    "Stol ustida",
                    "Sumkaning ichida",
                    "Bozorda qolib ketgan"
                ],
                "answer": 0,
                "explanation": "Jasur kurtkasining choʻntagiga qaragan edi va u yerdan "
                               "pul chiqqandi. Kalitlar esa ikkinchi choʻntakda ekan — "
                               "«в другом кармане». Shuning uchun u avtobusda yolgʻiz "
                               "kuladi.",
            },
            {
                "text": "Nega matnda «в сумке», lekin «на столе»?",
                "choices": [
                    "Sumkaning ichi bor (В), stol esa yuza (НА)",
                    "Bu ikki xil kelishik",
                    "Chunki «стол» erkak jinsida",
                    "Bu xato — ikkalasi ham «в» boʻlishi kerak"
                ],
                "answer": 0,
                "explanation": "Kelishik bitta — предложный, va qoʻshimcha ikkalasida "
                               "ham -Е. Faqat predlog boshqa: В — ichida, НА — ustida "
                               "yoki ochiq joyda. Bu darsning asosiy tanlovi.",
            },
            {
                "text": "«На рынке» va «на почте» — nega bu yerda НА, garchi bozor va "
                        "pochta ichiga kiriladigan joylar boʻlsa ham?",
                "choices": [
                    "Bular yodlanadigan roʻyxatdan — mantiq emas, odat",
                    "Chunki ikkalasi ham ayol jinsida",
                    "Chunki ular shahar tashqarisida",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Bir guruh soʻz НА oladi va sababi yoʻq: на работе, "
                               "на уроке, на рынке, на почте, на вокзале, на "
                               "экзамене. Bularni soʻz bilan birga yodlash kerak. "
                               "Oʻzbekchada ham shunga oʻxshash mantiqsiz odatlar bor.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-31 — предложный «о чём?»            KITOB SHARHI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "О чём эта книга?",
        "summary": (
            "PR-31 matni. Afsona doʻstiga oʻqigan kitobini tavsiya qilib yozadi. "
            "Savol bitta — «bu kitob nima haqida?» — va javob matnning oxirigacha "
            "oʻzgarib boradi."
        ),
        "order":   31,
        "grammar": [
            {
                "pattern":  "о + Предложный",
                "meaning":  "«Haqida». Qoʻshimcha PR-30 dagining oʻzi (-Е, -ИИ), faqat "
                            "predlog О. Oʻzbekchada «haqida» otdan KEYIN turadi, "
                            "ruschada esa OLDIN — va ot ham oʻzgaradi.",
                "examples": ["Книга о мальчике.", "Он думает о друге."],
            },
            {
                "pattern":  "об — unlidan oldin",
                "meaning":  "Об а, э, и, о, у tovushlaridan oldin qoʻyiladi: об окне, "
                            "об уроке, об одиночестве. Е, ё, ю, я soʻz boshida "
                            "undosh tovushdan boshlanadi, shuning uchun ular О oladi.",
                "examples": ["Она об одиночестве."],
            },
            {
                "pattern":  "о чём? о ком?",
                "meaning":  "Savol soʻzining oʻzi ham kelishikka kiradi: что → о чём, "
                            "кто → о ком. Narsa haqida — о чём, odam haqida — о ком.",
                "examples": ["О чём эта книга?", "О ком ты думаешь?"],
            },
        ],
        "body": '''<p>Катя спрашивает: «<strong>О чём</strong> эта книга?»</p>

<p>Отвечаю.</p>

<p>Это книга <strong>о мальчике</strong>. <span class="cn-word" data-tr="oʻgʻil bola">Мальчик</span> — Олег. Он живёт в деревне.</p>

<p>Книга <strong>о школе</strong>, <strong>о лете</strong> и <strong>о реке</strong>.</p>

<p>Но <strong>о чём</strong> она <span class="cn-word" data-tr="aslida">на самом деле</span>? Она <strong>об</strong> <span class="cn-word" data-tr="yolgʻizlik">одиночестве</span>.</p>

<p>У Олега есть друг. Друг живёт далеко, в городе. Олег думает <strong>о друге</strong> каждый день.</p>

<p>Олег пишет письма. Он пишет <strong>о реке</strong>, о <span class="cn-word" data-tr="baliq">рыбе</span>, о <span class="cn-word" data-tr="it">собаке</span>, о дожде и о <span class="cn-word" data-tr="oʻrmon">лесе</span>.</p>

<p>Он никогда не пишет: «Мне <span class="cn-word" data-tr="gʻamgin">грустно</span>».</p>

<p>Но каждое <span class="cn-word" data-tr="xat">письмо</span> — <strong>о друге</strong>.</p>

<p>Мне нравится эта книга. Она <span class="cn-word" data-tr="tinch, sokin">тихая</span>. В ней нет <span class="cn-word" data-tr="urush">войны</span>, нет <span class="cn-word" data-tr="sir">тайны</span>. Только мальчик, <span class="cn-word" data-tr="daryo">река</span> и письма.</p>

<p>Катя, ты любишь комедии. Эта книга не комедия. Но я думаю: тебе тоже <strong>будет</strong> интересно.</p>

<p>Один вопрос — «<strong>о чём</strong> книга?» И один ответ: <strong>о дружбе</strong>.</p>''',
        "questions": [
            {
                "text": "Afsonaning fikricha, kitob aslida nima haqida?",
                "choices": [
                    "Doʻstlik haqida",
                    "Baliq ovi haqida",
                    "Qishloq maktabi haqida",
                    "Urush haqida"
                ],
                "answer": 0,
                "explanation": "Javob matn davomida oʻzgarib boradi: avval «oʻgʻil bola "
                               "haqida», keyin «yolgʻizlik haqida», oxirida esa «о "
                               "дружбе». Oleg xatlarida daryo, baliq va it haqida "
                               "yozadi — lekin har bir xat doʻsti haqida.",
            },
            {
                "text": "Nega matnda «об одиночестве», lekin «о дружбе»?",
                "choices": [
                    "«Одиночество» unli tovush bilan boshlanadi, «дружба» esa undosh",
                    "Chunki birinchisi oʻrta jinsda",
                    "Chunki birinchisi uzunroq soʻz",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "ОБ shakli unli tovushdan (а, э, и, о, у) oldin qoʻyiladi "
                               "— talaffuzni osonlashtirish uchun. «Дружба» Д bilan "
                               "boshlanadi, demak oddiy О.",
            },
            {
                "text": "«Он никогда не пишет: „Мне грустно“» — bu jumla nima uchun "
                        "matnning eng muhim joyi?",
                "choices": [
                    "Oleg gʻamgin ekanini aytmaydi, lekin har bir xatidan bu bilinadi",
                    "Oleg aslida xursand ekanini koʻrsatadi",
                    "Oleg yozishni bilmasligini koʻrsatadi",
                    "Bu shunchaki qoʻshimcha maʼlumot"
                ],
                "answer": 0,
                "explanation": "Undan keyin darrov: «Но каждое письмо — о друге». "
                               "Oleg daryo, baliq va it haqida yozadi, lekin xatlarning "
                               "haqiqiy mavzusi boshqa. Kitob ham shu usulda "
                               "yozilgan — shuning uchun Afsona uni «тихая» deydi.",
            },
        ],
    },
]
