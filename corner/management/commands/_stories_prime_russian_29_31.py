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
  30-matn: предло́жный «где?» maʼnosida (PR-30). Har bir jumla boshqa joy —
           в/на tanlovi matnning oʻzida takrorlanib turadi.
  31-matn: предло́жный «о чём?» maʼnosida (PR-31), «об» shakli bilan birga.

Hali oʻrgatilmagan kelishiklar (В.п., Р.п., Т.п.) matnlarda ishlatilmaydi;
«ключе́й нет», «в друго́м карма́не» kabi bir nechta ibora butun boʻlak
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
        "title":   "Одно́ сло́во — шесть форм",
        "summary": (
            "PR-29 matni. Rus tilidagi kelishiklar haqida qisqa ilmiy-ommabop "
            "matn: nega bitta soʻzning oltita shakli bor, oʻzbek tilida ham "
            "nega shunday, va nima uchun bu tartibsizlik emas — tizim."
        ),
        "order":   29,
        "grammar": [
            {
                "pattern":  "паде́ж — kelishik",
                "meaning":  "Soʻzning oxiri uning gapdagi ishini koʻrsatadi. Rus "
                            "tilida oltita kelishik bor, oʻzbek tilida ham oltita — "
                            "shuning uchun tushuncha oʻzbek oʻquvchi uchun yangi emas.",
                "examples": ["Кни́га. Кни́ги. Кни́ге. Кни́гу.", "Одно́ сло́во — шесть форм."],
            },
            {
                "pattern":  "род — jins",
                "meaning":  "Rus tilida shakl otning jinsiga bogʻliq: «кни́га» va "
                            "«стол» boshqacha turlanadi. Oʻzbekchada esa qoʻshimcha "
                            "hamma soʻz uchun bitta — bu birinchi yangi qiyinchilik.",
                "examples": ["«Кни́га» и «стол» — фо́рмы ра́зные."],
            },
            {
                "pattern":  "предло́г — predlog",
                "meaning":  "Ikkinchi yangi narsa: ruschada koʻpincha predlog VA "
                            "qoʻshimcha birga ishlaydi. Bitta kelishik esa predlogsiz "
                            "umuman yashamaydi — предло́жный.",
                "examples": ["В шко́ле. На рабо́те. О кни́ге."],
            },
        ],
        "body": '''<p>Сло́во «кни́га» — одно́. Но <span class="cn-word" data-tr="shakllar">форм</span> у него́ шесть.</p>

<p>Кни́га. Кни́ги. Кни́ге. Кни́гу. Кни́гой. О кни́ге.</p>

<p>Это оди́н <span class="cn-word" data-tr="narsa, predmet">предме́т</span>. Но ка́ждая фо́рма — э́то друга́я <span class="cn-word" data-tr="ish, vazifa">рабо́та</span>.</p>

<p><strong>Кни́га</strong> лежи́т. <strong>Кни́гу</strong> чита́ет Афсона. Мы говори́м <strong>о кни́ге</strong>. Оди́н предме́т, три фо́рмы, три ро́ли.</p>

<p><span class="cn-word" data-tr="Yaxshi xabar">Хоро́шая но́вость</span>: в узбе́кском языке́ <strong>тоже</strong> есть <span class="cn-word" data-tr="kelishiklar">падежи́</span>. Тоже шесть. Поэ́тому <span class="cn-word" data-tr="fikr, gʻoya">иде́я</span> не но́вая.</p>

<p>Что но́вое? <span class="cn-word" data-tr="uch narsa">Три ве́щи</span>.</p>

<p>Пе́рвое: <span class="cn-word" data-tr="jins">род</span>. «Кни́га» и «стол» — фо́рмы ра́зные.</p>

<p>Второ́е: <span class="cn-word" data-tr="predloglar">предло́ги</span>. В. На. О. С. Из.</p>

<p>Тре́тье: оди́н паде́ж не живёт <span class="cn-word" data-tr="predlogsiz">без предло́га</span>. Э́то предло́жный. Он всегда́ с предло́гом: <strong>в шко́ле</strong>, <strong>на рабо́те</strong>, <strong>о кни́ге</strong>.</p>

<p>Шесть форм — э́то мно́го? Мо́жет быть.</p>

<p>Но э́то не <span class="cn-word" data-tr="tartibsizlik">хао́с</span>. Э́то <span class="cn-word" data-tr="tizim">систе́ма</span>. А систе́ма — э́то пра́вила. И пра́вила мо́жно знать.</p>''',
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
                "explanation": "«В узбе́кском языке́ тоже есть падежи́. Тоже шесть. "
                               "Поэ́тому иде́я не но́вая» — matnning eng muhim jumlasi. "
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
                "explanation": "Matn ularni raqamlab beradi: «Пе́рвое: род… Второ́е: "
                               "предло́ги… Тре́тье: оди́н паде́ж не живёт без "
                               "предло́га». Uchalasi ham oʻzbekchada yoʻq va aynan "
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
                "explanation": "«Э́то не хао́с. Э́то систе́ма. А систе́ма — э́то "
                               "пра́вила. И пра́вила мо́жно знать» — matnning butun "
                               "maqsadi shu: qoʻrqitmaslik. Tartibsizlikni yodlab "
                               "boʻlmaydi, qoidalarni esa boʻladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-30 — предложный «где?»              KICHIK SIRLI HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Где мои́ ключи́?",
        "summary": (
            "PR-30 matni. Jasur ertalab kalitlarini topa olmaydi. Butun oila "
            "qidiradi — va har bir qidirilgan joy предло́жный padejining yangi "
            "misoli. Javob eng oxirida, eng kutilmagan joyda."
        ),
        "order":   30,
        "grammar": [
            {
                "pattern":  "в + Предло́жный",
                "meaning":  "Ichi bor joy: в су́мке, в ко́мнате, в магази́не, в "
                            "авто́бусе. Qoʻshimcha deyarli har doim -Е. Oʻzbekchadagi "
                            "-DA ning oʻzi, faqat predlog qoʻshiladi.",
                "examples": ["Телефо́н в су́мке.", "Он был в магази́не."],
            },
            {
                "pattern":  "на + Предло́жный",
                "meaning":  "Yuza yoki ochiq joy: на столе́, на у́лице, на полу́. Va "
                            "yodlanadigan roʻyxat: на рабо́те, на ры́нке, на по́чте, "
                            "на уро́ке — bu yerda mantiq emas, odat ishlaydi.",
                "examples": ["Ключи́ бы́ли на столе́.", "И на ры́нке. И на по́чте."],
            },
            {
                "pattern":  "на полу́ — -У́ roʻyxati",
                "meaning":  "Kichik yopiq roʻyxat: в лесу́, в саду́, на полу́, в "
                            "шкафу́, на берегу́, в аэропорту́. Ularning urgʻusi har "
                            "doim qoʻshimchada.",
                "examples": ["Бекзо́д смо́трит на полу́."],
            },
        ],
        "body": '''<p>Утром Жасур <span class="cn-word" data-pos="verb" data-tr="qidiradi">и́щет</span> <span class="cn-word" data-tr="kalitlar">ключи́</span>.</p>

<p>— Ключи́ бы́ли <strong>на столе́</strong>, — говори́т Жасур.</p>

<p>Но <strong>на столе́</strong> то́лько чай.</p>

<p>Жасур смо́трит <strong>в</strong> <span class="cn-word" data-tr="sumkada">су́мке</span>. Там кни́ги, <span class="cn-word" data-tr="ruchka">ру́чка</span>, телефо́н. Но не ключи́.</p>

<p>Жасур смо́трит <strong>в</strong> <span class="cn-word" data-tr="kurtkada">ку́ртке</span>. <strong>В карма́не</strong> — <span class="cn-word" data-tr="pul">де́ньги</span>. Но не ключи́.</p>

<p>Бекзод смо́трит <strong>на полу́</strong>. Мама смо́трит <strong>в ко́мнате</strong> и <strong>на ку́хне</strong>.</p>

<p>— Ты был вчера́ <strong>в магази́не</strong>? — спра́шивает мама.</p>

<p>— Да. И <strong>на ры́нке</strong>. И <strong>на</strong> <span class="cn-word" data-tr="pochtada">по́чте</span>. И <strong>в библиоте́ке</strong>.</p>

<p>— <span class="cn-word" data-tr="Demak">Зна́чит</span>, ключи́ <strong>в Ташке́нте</strong>, — говори́т Бекзод.</p>

<p>Все смею́тся. Но <span class="cn-word" data-tr="kalitlar yoʻq">ключе́й нет</span>.</p>

<p>Пото́м Жасур идёт <strong>в шко́лу</strong>. <strong>В авто́бусе</strong> он ду́мает: «Где ключи́?»</p>

<p>И <strong>в авто́бусе</strong> он слы́шит: «<span class="cn-word" data-tr="jaranglagan tovush">Дзи́нь</span>».</p>

<p>Ключи́ <strong>в карма́не</strong>. Но <span class="cn-word" data-tr="boshqa choʻntakda">в друго́м карма́не</span>.</p>

<p>Жасур смея́лся <strong>в авто́бусе</strong>. Оди́н.</p>''',
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
                               "«в друго́м карма́не». Shuning uchun u avtobusda yolgʻiz "
                               "kuladi.",
            },
            {
                "text": "Nega matnda «в су́мке», lekin «на столе́»?",
                "choices": [
                    "Sumkaning ichi bor (В), stol esa yuza (НА)",
                    "Bu ikki xil kelishik",
                    "Chunki «стол» erkak jinsida",
                    "Bu xato — ikkalasi ham «в» boʻlishi kerak"
                ],
                "answer": 0,
                "explanation": "Kelishik bitta — предло́жный, va qoʻshimcha ikkalasida "
                               "ham -Е. Faqat predlog boshqa: В — ichida, НА — ustida "
                               "yoki ochiq joyda. Bu darsning asosiy tanlovi.",
            },
            {
                "text": "«На ры́нке» va «на по́чте» — nega bu yerda НА, garchi bozor va "
                        "pochta ichiga kiriladigan joylar boʻlsa ham?",
                "choices": [
                    "Bular yodlanadigan roʻyxatdan — mantiq emas, odat",
                    "Chunki ikkalasi ham ayol jinsida",
                    "Chunki ular shahar tashqarisida",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Bir guruh soʻz НА oladi va sababi yoʻq: на рабо́те, "
                               "на уро́ке, на ры́нке, на по́чте, на вокза́ле, на "
                               "экза́мене. Bularni soʻz bilan birga yodlash kerak. "
                               "Oʻzbekchada ham shunga oʻxshash mantiqsiz odatlar bor.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-31 — предложный «о чём?»            KITOB SHARHI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "О чём э́та кни́га?",
        "summary": (
            "PR-31 matni. Afsona doʻstiga oʻqigan kitobini tavsiya qilib yozadi. "
            "Savol bitta — «bu kitob nima haqida?» — va javob matnning oxirigacha "
            "oʻzgarib boradi."
        ),
        "order":   31,
        "grammar": [
            {
                "pattern":  "о + Предло́жный",
                "meaning":  "«Haqida». Qoʻshimcha PR-30 dagining oʻzi (-Е, -ИИ), faqat "
                            "predlog О. Oʻzbekchada «haqida» otdan KEYIN turadi, "
                            "ruschada esa OLDIN — va ot ham oʻzgaradi.",
                "examples": ["Кни́га о ма́льчике.", "Он ду́мает о дру́ге."],
            },
            {
                "pattern":  "об — unlidan oldin",
                "meaning":  "Об а, э, и, о, у tovushlaridan oldin qoʻyiladi: об окне́, "
                            "об уро́ке, об оди́ночестве. Е, ё, ю, я soʻz boshida "
                            "undosh tovushdan boshlanadi, shuning uchun ular О oladi.",
                "examples": ["Она́ об оди́ночестве."],
            },
            {
                "pattern":  "о чём? о ком?",
                "meaning":  "Savol soʻzining oʻzi ham kelishikka kiradi: что → о чём, "
                            "кто → о ком. Narsa haqida — о чём, odam haqida — о ком.",
                "examples": ["О чём э́та кни́га?", "О ком ты ду́маешь?"],
            },
        ],
        "body": '''<p>Катя спра́шивает: «<strong>О чём</strong> э́та кни́га?»</p>

<p>Отвеча́ю.</p>

<p>Э́то кни́га <strong>о ма́льчике</strong>. <span class="cn-word" data-tr="oʻgʻil bola">Ма́льчик</span> — Олег. Он живёт в дере́вне.</p>

<p>Кни́га <strong>о шко́ле</strong>, <strong>о ле́те</strong> и <strong>о реке́</strong>.</p>

<p>Но <strong>о чём</strong> она́ <span class="cn-word" data-tr="aslida">на са́мом де́ле</span>? Она́ <strong>об</strong> <span class="cn-word" data-tr="yolgʻizlik">оди́ночестве</span>.</p>

<p>У Оле́га есть друг. Друг живёт далеко́, в го́роде. Олег ду́мает <strong>о дру́ге</strong> ка́ждый день.</p>

<p>Олег пи́шет пи́сьма. Он пи́шет <strong>о реке́</strong>, о <span class="cn-word" data-tr="baliq">ры́бе</span>, о <span class="cn-word" data-tr="it">соба́ке</span>, о дожде́ и о <span class="cn-word" data-tr="oʻrmon">ле́се</span>.</p>

<p>Он никогда́ не пи́шет: «Мне <span class="cn-word" data-tr="gʻamgin">гру́стно</span>».</p>

<p>Но ка́ждое <span class="cn-word" data-tr="xat">письмо́</span> — <strong>о дру́ге</strong>.</p>

<p>Мне нра́вится э́та кни́га. Она́ <span class="cn-word" data-tr="tinch, sokin">ти́хая</span>. В ней нет <span class="cn-word" data-tr="urush">войны́</span>, нет <span class="cn-word" data-tr="sir">та́йны</span>. То́лько ма́льчик, <span class="cn-word" data-tr="daryo">река́</span> и пи́сьма.</p>

<p>Катя, ты лю́бишь коме́дии. Э́та кни́га не коме́дия. Но я ду́маю: тебе́ то́же <strong>бу́дет</strong> интере́сно.</p>

<p>Оди́н вопро́с — «<strong>о чём</strong> кни́га?» И оди́н отве́т: <strong>о дру́жбе</strong>.</p>''',
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
                               "дру́жбе». Oleg xatlarida daryo, baliq va it haqida "
                               "yozadi — lekin har bir xat doʻsti haqida.",
            },
            {
                "text": "Nega matnda «об оди́ночестве», lekin «о дру́жбе»?",
                "choices": [
                    "«Оди́ночество» unli tovush bilan boshlanadi, «дру́жба» esa undosh",
                    "Chunki birinchisi oʻrta jinsda",
                    "Chunki birinchisi uzunroq soʻz",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "ОБ shakli unli tovushdan (а, э, и, о, у) oldin qoʻyiladi "
                               "— talaffuzni osonlashtirish uchun. «Дру́жба» Д bilan "
                               "boshlanadi, demak oddiy О.",
            },
            {
                "text": "«Он никогда́ не пи́шет: „Мне гру́стно“» — bu jumla nima uchun "
                        "matnning eng muhim joyi?",
                "choices": [
                    "Oleg gʻamgin ekanini aytmaydi, lekin har bir xatidan bu bilinadi",
                    "Oleg aslida xursand ekanini koʻrsatadi",
                    "Oleg yozishni bilmasligini koʻrsatadi",
                    "Bu shunchaki qoʻshimcha maʼlumot"
                ],
                "answer": 0,
                "explanation": "Undan keyin darrov: «Но ка́ждое письмо́ — о дру́ге». "
                               "Oleg daryo, baliq va it haqida yozadi, lekin xatlarning "
                               "haqiqiy mavzusi boshqa. Kitob ham shu usulda "
                               "yozilgan — shuning uchun Afsona uni «ти́хая» deydi.",
            },
        ],
    },
]
