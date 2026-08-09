# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-12 … PR-14.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Shakl xilma-xilligi: 12 — kundalik daftar (yangi janr), 13 — doʻkondagi suhbat,
14 — buvijon haqidagi kichik hayot lavhasi.

Feʼl tizimi hali ochilmagan (PR-19 dan), shuning uchun tocdagi "narrative frame"
istisnosi ishlatilgan: есть · нет · зову́т · живёт · рабо́тает · говори́т ·
сказа́л(а)/сказа́ли · пришёл/пришла́/пришли́ · дал(а) · был/была́/бы́ло/бы́ли.
Vaqt/joy ravishlari va turgʻun iboralar (ско́лько сто́ит, спаси́бо, пожа́луйста)
lugʻat sifatida izohlanadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_12_14.py --author=prime
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
    # PR-12 — sifat                    KUNDALIK DAFTAR (yangi janr)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Но́вая шко́ла",
        "summary": (
            "PR-12 matni. Dilnozaning kundalik daftaridan bir sahifa: yangi maktabdagi "
            "birinchi kun. Har bir jumlada sifat bor, va har bir sifat oʻz otiga "
            "moslashgan — oxirlariga qarab boring."
        ),
        "order":   12,
        "grammar": [
            {
                "pattern":  "Sifat + ot (moslashuv)",
                "meaning":  "Sifat otning jinsi va soniga qarab shakl oladi: "
                            "но́вый (m.) / но́вая (f.) / но́вое (oʻrta) / но́вые "
                            "(koʻplik). Sifat otdan oldin turadi — oʻzbekchadagidek.",
                "examples": ["но́вая шко́ла", "большо́й класс", "но́вые дру́зья"],
            },
            {
                "pattern":  "Г К Х Ж Ч Ш Щ dan keyin -ий",
                "meaning":  "Bu yettita harfdan keyin sifat -ый emas, -ий bilan "
                            "tugaydi. Shuning uchun ру́сский, ма́ленький, хоро́ший.",
                "examples": ["ру́сский язы́к", "ма́ленький кот", "хоро́ший день"],
            },
            {
                "pattern":  "Sifat kesim sifatida — tiresiz",
                "meaning":  "Sifat otdan keyin ham tura oladi. Bunda tire QOʻYILMAYDI "
                            "(PR-11) va maʼno oʻzgaradi: «но́вая шко́ла» nomlaydi, "
                            "«шко́ла но́вая» esa xabar beradi.",
                "examples": ["Шко́ла но́вая.", "Класс большо́й."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="sentabr">Сентя́брь</span>. Сего́дня — <span class="cn-word" data-tr="yangi">но́вая</span> шко́ла.</p>

<p>Шко́ла <strong>больша́я</strong> и <strong>све́тлая</strong>. Наш класс <strong>большо́й</strong>. Окна́ <strong><span class="cn-word" data-tr="katta (koʻplik)">больши́е</span></strong>, и здесь <strong><span class="cn-word" data-tr="yangi (koʻplik)">но́вые</span></strong> столы́.</p>

<p><span class="cn-word" data-tr="oʻqituvchi (ayol)">Учи́тельница</span> — <span class="cn-word" data-tr="yosh">молода́я</span>. Её зову́т Мари́на Оле́говна. Она́ <strong><span class="cn-word" data-tr="mehribon">до́брая</span></strong>.</p>

<p><span class="cn-word" data-tr="birinchi dars">Пе́рвый уро́к</span> — <strong>ру́сский</strong> язы́к. Уро́к <strong><span class="cn-word" data-tr="qiziqarli">интере́сный</span></strong>, но <strong><span class="cn-word" data-tr="qiyin">тру́дный</span></strong>.</p>

<p>Мой сосе́д — Жасу́р. Жасу́р <strong><span class="cn-word" data-tr="quvnoq">весёлый</span></strong>. Его́ <span class="cn-word" data-tr="ryukzak">рюкза́к</span> <strong>ста́рый</strong>, а ру́чки <strong>но́вые</strong>.</p>

<p>Пото́м <span class="cn-word" data-pos="verb" data-tr="keldi (ayol)">пришла́</span> Афсо́на. Афсо́на сказа́ла: «Шко́ла <strong>но́вая</strong>, но лю́ди <strong>хоро́шие</strong>».</p>

<p>Да. Шко́ла <strong>но́вая</strong>. Класс <strong>большо́й</strong>. И дру́зья <strong><span class="cn-word" data-tr="yangi (koʻplik)">но́вые</span></strong>.</p>''',
        "questions": [
            {
                "text": "Dilnoza kunini qanday yakunlaydi?",
                "choices": [
                    "Maktab yangi, lekin unda allaqachon yangi doʻstlari bor",
                    "Maktab yoqmadi",
                    "Darslar juda oson edi",
                    "U eski maktabini sogʻindi"
                ],
                "answer": 0,
                "explanation": "Oxirgi jumla: «Шко́ла но́вая. Класс большо́й. И дру́зья "
                               "но́вые». Afsonaning gapi ham shuni tayyorlaydi: "
                               "«Шко́ла но́вая, но лю́ди хоро́шие».",
            },
            {
                "text": "Nega «ру́сский язы́к», «ру́сскый» emas?",
                "choices": [
                    "Chunki oʻzak К bilan tugaydi — Г К Х Ж Ч Ш Щ dan keyin -ий keladi",
                    "Chunki язы́к erkak jinsida",
                    "Chunki bu tilning nomi",
                    "Chunki urgʻu oxirda"
                ],
                "answer": 0,
                "explanation": "Yettita harf qoidasi — xuddi PR-9 dagi «кни́ги» kabi. "
                               "Bu roʻyxat rus imlosining koʻp joyida ishlaydi, shuning "
                               "uchun uni bir marta yodlash arziydi.",
            },
            {
                "text": "Matnda «Шко́ла но́вая» bor, lekin tire yoʻq. Nega?",
                "choices": [
                    "Chunki kesim — sifat, ot emas",
                    "Chunki gap qisqa",
                    "Chunki bu kundalik daftar",
                    "Bu xato, tire boʻlishi kerak"
                ],
                "answer": 0,
                "explanation": "PR-11 qoidasi: tire faqat ikkala tomon ham OT boʻlganda "
                               "qoʻyiladi. Bu yerda kesim sifat (но́вая), shuning uchun "
                               "tire yoʻq. Solishtiring: «Мой го́род — Ташке́нт» — ot + ot.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-13 — sonlar                   DOʻKONDAGI SUHBAT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Ско́лько сто́ит?",
        "summary": (
            "PR-13 matni. Sherbek maktabga daftar va ruchka olgani boradi, lekin puli "
            "yetmaydi. Sotuvchi ayol bitta narsani boshqacha hisoblaydi — sonlar bilan "
            "toʻla kichik doʻkon suhbati."
        ),
        "order":   13,
        "grammar": [
            {
                "pattern":  "Ско́лько сто́ит? / Ско́лько?",
                "meaning":  "«Qancha turadi?» va «Nechta?». Doʻkondagi eng kerakli "
                            "savol — uni turgʻun ibora sifatida yodlang, soʻz tartibi "
                            "oʻzgarmaydi.",
                "examples": ["Ско́лько сто́ит тетра́дь?", "Ско́лько у вас ру́чек?"],
            },
            {
                "pattern":  "два / две",
                "meaning":  "Faqat 2 sonining ayol jinsi uchun alohida shakli bor: "
                            "две тетра́ди, lekin два карандаша́. Uch va undan keyingi "
                            "sonlar jinsga qarab oʻzgarmaydi.",
                "examples": ["две тетра́ди", "два карандаша́", "три ру́чки"],
            },
            {
                "pattern":  "оди́н / одна́ / одно́",
                "meaning":  "«Bir» soni sifat kabi otga moslashadi: оди́н каранда́ш, "
                            "одна́ ру́чка, одно́ сло́во.",
                "examples": ["одна́ ру́чка", "оди́н рюкза́к"],
            },
        ],
        "body": '''<p>Э́то <span class="cn-word" data-tr="doʻkon">магази́н</span>. Здесь <span class="cn-word" data-pos="verb" data-tr="ishlaydi">рабо́тает</span> Ни́на Петро́вна. <span class="cn-word" data-pos="verb" data-tr="keldi">Пришёл</span> Шербе́к.</p>

<p><strong>Шербе́к:</strong> Здра́вствуйте! <strong>Ско́лько сто́ит</strong> тетра́дь?</p>

<p><strong>Ни́на Петро́вна:</strong> <span class="cn-word" data-tr="besh">Пять</span> <span class="cn-word" data-tr="ming">ты́сяч</span>.</p>

<p><strong>Шербе́к:</strong> А ру́чка?</p>

<p><strong>Ни́на Петро́вна:</strong> <span class="cn-word" data-tr="uch">Три</span> ты́сячи.</p>

<p>Шербе́к сказа́л: «<strong>Две</strong> тетра́ди и <strong>две</strong> ру́чки, пожа́луйста».</p>

<p><strong>Ни́на Петро́вна:</strong> Хорошо́. <span class="cn-word" data-tr="oʻn olti">Шестна́дцать</span> ты́сяч.</p>

<p>У него́ <span class="cn-word" data-tr="oʻn besh">пятна́дцать</span> ты́сяч. Шербе́к сказа́л: «<span class="cn-word" data-tr="kechirasiz">Извини́те</span>. Тогда́ <strong>одна́</strong> ру́чка».</p>

<p>Ни́на Петро́вна <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказа́ла</span>: «Нет. <strong>Две</strong> тетра́ди и <strong>две</strong> ру́чки — <span class="cn-word" data-tr="oʻn besh">пятна́дцать</span>».</p>

<p><strong>Шербе́к:</strong> Но э́то <span class="cn-word" data-tr="oʻn olti">шестна́дцать</span>!</p>

<p><strong>Ни́на Петро́вна:</strong> Сего́дня — пятна́дцать. Пе́рвый день, но́вая шко́ла.</p>

<p>Шербе́к сказа́л: «Спаси́бо!» У него́ есть <strong>две</strong> тетра́ди, <strong>две</strong> ру́чки — и <span class="cn-word" data-tr="yaxshi kun">хоро́ший день</span>.</p>''',
        "questions": [
            {
                "text": "Nega Nina Petrovna narxni oʻn olti emas, oʻn besh dedi?",
                "choices": [
                    "Sherbekda faqat oʻn besh ming bor edi, va u birinchi kun uchun "
                    "chegirma qildi",
                    "U hisobda xato qildi",
                    "Daftarlar arzonlashgan edi",
                    "Sherbek bitta ruchka oldi"
                ],
                "answer": 0,
                "explanation": "Sherbek bitta ruchkadan voz kechmoqchi boʻldi, lekin "
                               "sotuvchi «Нет» dedi va narxni pasaytirdi: «Сего́дня — "
                               "пятна́дцать. Пе́рвый день, но́вая шко́ла». Bu hikoyaning "
                               "yumshoq yakuni.",
            },
            {
                "text": "Nega matnda «две тетра́ди», lekin «два карандаша́» boʻlar edi?",
                "choices": [
                    "Chunki тетра́дь ayol jinsida, каранда́ш esa erkak jinsida",
                    "Chunki тетра́дь koʻplikda",
                    "Chunki daftar qimmatroq",
                    "Bu ikki xil aytish usuli, farqi yoʻq"
                ],
                "answer": 0,
                "explanation": "Faqat 2 sonida jins farqi bor: ayol jinsi uchun "
                               "«две», erkak va oʻrta jins uchun «два». Uch va undan "
                               "keyingi sonlarda bu farq yoʻq: «три тетра́ди», "
                               "«три карандаша́».",
            },
            {
                "text": "Sherbek «одна́ ру́чка» dedi. Nega «оди́н» emas?",
                "choices": [
                    "Chunki ру́чка ayol jinsida, «оди́н» esa otga moslashadi",
                    "Chunki ruchka bitta edi",
                    "Chunki u kechirim soʻradi",
                    "Chunki narx past edi"
                ],
                "answer": 0,
                "explanation": "Sonlar orasida faqat «оди́н» sifat kabi oʻzgaradi: "
                               "оди́н (m.) / одна́ (f.) / одно́ (oʻrta). «Ру́чка» -а "
                               "bilan tugaydi — ayol jinsi, demak «одна́».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-14 — У меня есть           KICHIK HAYOT LAVHASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "У меня́ есть всё",
        "summary": (
            "PR-14 matni. Bekzod buvisidan nega uyi kichkina ekanini soʻraydi. "
            "Buvijon javob bermaydi — u shunchaki sanay boshlaydi, va sanoq oxirida "
            "savolning oʻzi yoʻqoladi."
        ),
        "order":   14,
        "grammar": [
            {
                "pattern":  "У меня́ / у тебя́ / у неё есть …",
                "meaning":  "Rus tilida «ega boʻlmoq» feʼli yoʻq. Uning oʻrniga "
                            "«у + olmosh + есть + narsa» ishlatiladi — bu oʻzbekchadagi "
                            "«Menda … bor» bilan aynan bir xil qurilma.",
                "examples": ["У меня́ есть сад.", "У тебя́ есть телефо́н?"],
            },
            {
                "pattern":  "У dan keyin н- qoʻshiladi",
                "meaning":  "его́ → у него́, её → у неё, их → у них. Bu faqat predlog "
                            "bilan boʻladi. Talaffuz: у него́ = [у н'иво́], chunki -го "
                            "oxiri [во] boʻlib oʻqiladi.",
                "examples": ["У него́ есть кот.", "У них есть дом."],
            },
            {
                "pattern":  "есть — «bor», nomlash emas",
                "meaning":  "«Э́то дом» da есть qoʻyilmaydi (nomlash), «У меня́ есть дом» "
                            "da esa qoʻyiladi (mavjudlik). Tekshiruv: oʻzbekcha "
                            "tarjimada «bor» soʻzi bormi?",
                "examples": ["Э́то дом. (есть yoʻq)", "У меня́ есть дом. (есть bor)"],
            },
        ],
        "body": '''<p>Э́то <span class="cn-word" data-tr="kichkina">ма́ленький</span> дом. Здесь <span class="cn-word" data-pos="verb" data-tr="yashaydi">живёт</span> ба́бушка. Её зову́т Роза́ Каримо́вна.</p>

<p>Бекзо́д <span class="cn-word" data-pos="verb" data-tr="keldi">пришёл</span> и <span class="cn-word" data-pos="verb" data-tr="dedi">сказа́л</span>: «Ба́бушка, дом ма́ленький. У тебя́ <span class="cn-word" data-tr="oz, kam">ма́ло</span>?»</p>

<p>Ба́бушка сказа́ла: «Ма́ло? <strong>У меня́ есть</strong> <span class="cn-word" data-tr="bogʻ">сад</span>».</p>

<p>«И <strong>у меня́ есть</strong> <span class="cn-word" data-tr="olma daraxti">я́блоня</span>. <span class="cn-word" data-tr="eski">Ста́рая</span>, но хоро́шая».</p>

<p>«<strong>У меня́ есть</strong> кот. Его́ зову́т Ти́ша. <strong>У него́ есть</strong> <span class="cn-word" data-tr="joy">ме́сто</span> — вот <span class="cn-word" data-tr="mana shu yerda">здесь</span>».</p>

<p>«<strong>У меня́ есть</strong> сосе́ди. Ни́на Петро́вна и Оле́г. <strong>У них есть</strong> <span class="cn-word" data-tr="bolalar">де́ти</span>, и де́ти <span class="cn-word" data-tr="tez-tez">ча́сто</span> здесь».</p>

<p>«<strong>У меня́ есть</strong> <span class="cn-word" data-tr="nevaralar">вну́ки</span>. Ты, Дилно́за и Афсо́на».</p>

<p>Бекзо́д сказа́л: «А <span class="cn-word" data-tr="pul">де́ньги</span>?»</p>

<p>Ба́бушка сказа́ла: «Де́ньги — э́то не всё. Сад есть, кот есть, сосе́ди есть, вну́ки есть».</p>

<p>«Дом ма́ленький, Бекзо́д. А <strong>у меня́ есть всё</strong>».</p>''',
        "questions": [
            {
                "text": "Buvijon Bekzodning savoliga qanday javob berdi?",
                "choices": [
                    "Javob bermadi — u shunchaki bor narsalarini sanab chiqdi",
                    "U uyning kichikligini tan oldi va xafa boʻldi",
                    "U katta uy olmoqchi ekanini aytdi",
                    "U pul haqida gapirmadi"
                ],
                "answer": 0,
                "explanation": "Buvijon «Ма́ло?» deb qaytarib soʻradi va sanay boshladi: "
                               "bogʻ, olma daraxti, mushuk, qoʻshnilar, nevaralar. "
                               "Oxirida esa: «Дом ма́ленький, Бекзо́д. А у меня́ есть "
                               "всё». Sanoq javobning oʻzi boʻldi.",
            },
            {
                "text": "Matnda «У него́ есть ме́сто» bor. Nega «у его́» emas?",
                "choices": [
                    "Chunki «у» predlogidan keyin н- qoʻshiladi",
                    "Chunki кот erkak jinsida",
                    "Chunki bu koʻplik",
                    "Bu xato"
                ],
                "answer": 0,
                "explanation": "«У» predlogidan keyin его́ → у него́, её → у неё, "
                               "их → у них. Egalik sifatida esa «его́ ме́сто» deb "
                               "qolaveradi — н- faqat predlog bilan paydo boʻladi. "
                               "Talaffuz: [у н'иво́].",
            },
            {
                "text": "Nega «У меня́ есть сад» da «есть» bor, «Дом ма́ленький» da esa "
                        "yoʻq?",
                "choices": [
                    "Birinchisi mavjudlikni aytadi («bogʻim bor»), ikkinchisi esa uyning "
                    "qanaqaligini",
                    "Chunki сад erkak jinsida",
                    "Chunki birinchisi uzunroq gap",
                    "Bu shunchaki uslub"
                ],
                "answer": 0,
                "explanation": "Tekshiruv oddiy: oʻzbekcha tarjimada «bor» soʻzi bormi? "
                               "«Bogʻim bor» — bor, demak есть kerak. «Uy kichkina» — "
                               "«bor» yoʻq, demak есть ham yoʻq. Bu PR-6 va PR-11 dagi "
                               "qoidalar bilan bir tizim.",
            },
        ],
    },
]
