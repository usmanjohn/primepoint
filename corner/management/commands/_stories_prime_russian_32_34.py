# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-32 … PR-34.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 32 — vokzal sahnasi, 33 — sayohat qaydlari, 34 — oila
tarixi. (29 ilmiy-ommabop, 30 sirli hikoya, 31 kitob sharhi edi.)

Grammatika chegarasi (kumulyativ qoida):
  32-matn: В.п. toʻldiruvchi sifatida. Matn butunlay jonli/jonsiz farqi
           ustiga qurilgan — odamlar odamni kutadi, odamlar narsani kutadi.
           Yoʻnalish maʼnosi (в школу) hali YOʻQ — u PR-33 da.
  33-matn: В.п. yoʻnalish sifatida + «где?» bilan qarama-qarshiligi.
  34-matn: Р.п. egalik va «нет». Egalik zanjiri matnning oxirini quradi:
           дом деда → дом отца → наш дом.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_32_34.py --author=prime
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
    # PR-32 — В.п. jonli/jonsiz                VOKZAL SAHNASI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Кто кого ждёт?",
        "summary": (
            "PR-32 matni. Vokzalda hamma kimnidir yoki nimanidir kutyapti — va "
            "aynan shu «kimni / nimani» farqi rus tilida soʻz shaklini "
            "oʻzgartiradi. Oxirida bittasi eng uzoq kutgani maʼlum boʻladi."
        ),
        "order":   32,
        "grammar": [
            {
                "pattern":  "Винительный — jonli erkak",
                "meaning":  "Odam yoki hayvon boʻlsa, erkak jinsidagi ot -А / -Я "
                            "oladi: Жасур → Жасура, брат → брата. Oʻzbekchadagi "
                            "-NI ning oʻzi, faqat shakl jonlilikka qaraydi.",
                "examples": ["Бекзод ждёт Жасура.", "Нина видит сестру."],
            },
            {
                "pattern":  "Винительный — jonsiz erkak",
                "meaning":  "Narsa boʻlsa, shakl UMUMAN oʻzgarmaydi: поезд → поезд, "
                            "автобус → автобус. Shuning uchun «ждёт поезд», lekin "
                            "«ждёт брата».",
                "examples": ["Олег ждёт поезд.", "Афсона ждёт автобус."],
            },
            {
                "pattern":  "Ayol jinsi — har doim -У",
                "meaning":  "Ayol jinsida jonlilik umuman ishlamaydi: сестра → "
                            "сестру, Афсона → Афсону, книга → книгу. Bitta "
                            "qoʻshimcha, hech qanday shart yoʻq.",
                "examples": ["Жасур ждёт Афсону."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="vokzal">Вокзал</span>. Вечер. Здесь все ждут.</p>

<p>Нина ждёт <strong>сестру</strong>. Олег ждёт <strong>поезд</strong>.</p>

<p>Жасур ждёт <strong>Афсону</strong>. Афсона ждёт <strong>автобус</strong>.</p>

<p>А Бекзод ждёт <strong>Жасура</strong>. И Жасур этого не знает.</p>

<p>Здесь есть один <span class="cn-word" data-tr="muhim">важный</span> вопрос. Почему «сестру», но «поезд»?</p>

<p>Ответ <span class="cn-word" data-tr="oddiy">простой</span>. <span class="cn-word" data-tr="singil, opa">Сестра</span> — <span class="cn-word" data-tr="odam">человек</span>. Поезд — <span class="cn-word" data-tr="narsa, buyum">вещь</span>. Русский язык видит эту <span class="cn-word" data-tr="farq">разницу</span>.</p>

<p>Вот поезд. Все смотрят.</p>

<p>Нина видит <strong>сестру</strong>. Сестра видит <strong>Нину</strong>.</p>

<p>Олег видит <strong>поезд</strong> — и <span class="cn-word" data-pos="verb" data-tr="yugurmoq">бежит</span>.</p>

<p>Афсона видит <strong>автобус</strong>. Жасур видит <strong>Афсону</strong>.</p>

<p>А Бекзод уже давно видит <strong>Жасура</strong>. И молчит.</p>

<p>Бекзод ждал <span class="cn-word" data-tr="uzoqroq">дольше</span> всех. Бекзод любит <span class="cn-word" data-tr="syurprizlar">сюрпризы</span>.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra kim eng uzoq kutdi?",
                "choices": [
                    "Bekzod — u Jasurni kutdi va jim turdi",
                    "Nina — u singlisini kutdi",
                    "Oleg — u poyezdni kutdi",
                    "Afsona — u avtobusni kutdi"
                ],
                "answer": 0,
                "explanation": "«Бекзод ждал дольше всех». Matn boshida ham aytilgan "
                               "edi: «Бекзод ждёт Жасура. И Жасур этого не знает» — "
                               "u koʻrinmasdan kutib turgan, chunki syurprizlarni "
                               "yaxshi koʻradi.",
            },
            {
                "text": "Nega matnda «ждёт сестру», lekin «ждёт поезд»?",
                "choices": [
                    "Сестра ayol jinsida (-У), поезд esa jonsiz erkak (oʻzgarmaydi)",
                    "Chunki bittasi oʻtgan zamon",
                    "Chunki «поезд» koʻplikda",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham Винительный padejida. Ayol jinsi har doim "
                               "-У oladi. Erkak jinsida esa jonlilik hal qiladi: poyezd "
                               "— narsa, demak shakl bosh kelishik bilan bir xil "
                               "qoladi.",
            },
            {
                "text": "«Бекзод видит Жасура» — nega -А qoʻshilgan?",
                "choices": [
                    "Jasur — odam, demak jonli erkak: -А oladi",
                    "Chunki Jasur akasi",
                    "Chunki bu koʻplik",
                    "Chunki «видит» feʼli har doim -А talab qiladi"
                ],
                "answer": 0,
                "explanation": "Jonli erkak otlar Винительный'da -А / -Я oladi va "
                               "shakli Родительный bilan bir xil boʻladi. Agar Bekzod "
                               "avtobusni koʻrayotgan boʻlsa, hech narsa "
                               "qoʻshilmasdi: «видит автобус».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-33 — В.п. yoʻnalish                    SAYOHAT QAYDLARI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Куда идёт этот автобус?",
        "summary": (
            "PR-33 matni. Yangi shaharda birinchi hafta: bozor, pochta, "
            "kutubxona, ish. Bitta xato haydovchini kuldiradi — va aynan shu "
            "xato «где?» bilan «куда?» farqini bir umrga eslatib qoladi."
        ),
        "order":   33,
        "grammar": [
            {
                "pattern":  "куда? — в / на + Винительный",
                "meaning":  "Harakatning manzili. Predlog PR-30 dagidek qoladi, faqat "
                            "qoʻshimcha oʻzgaradi: на работе → на работу, в школе → "
                            "в школу. Oʻzbekchadagi -DA ↔ -GA farqi.",
                "examples": ["Я иду на рынок.", "Я еду на работу."],
            },
            {
                "pattern":  "Jonsiz erkak — oʻzgarmaydi",
                "meaning":  "«Куда?» maʼnosida ham jonsiz erkak otlar bosh kelishikda "
                            "qoladi: в магазин, на рынок, на урок. Faqat predlog "
                            "qoʻshiladi.",
                "examples": ["Потом в магазин и в библиотеку."],
            },
            {
                "pattern":  "дома ↔ домой",
                "meaning":  "Ravishlar juftligi: где? — дома, здесь, там. Куда? — "
                            "домой, сюда, туда. Ular hech qachon aralashmaydi.",
                "examples": ["Вечером — домой."],
            },
        ],
        "body": '''<p>Я ещё не знаю этот город. Я только спрашиваю: «Куда?»</p>

<p>Утром я иду <strong>на рынок</strong>. Там громко и <span class="cn-word" data-tr="mazali">вкусно</span>.</p>

<p>Потом я иду <strong>на почту</strong>. Потом <strong>в магазин</strong> и <strong>в библиотеку</strong>.</p>

<p><span class="cn-word" data-tr="soat ikkida">В два часа</span> я еду <strong>на работу</strong>. Вечером — <strong>домой</strong>.</p>

<p>Вот всё <span class="cn-word" data-tr="qoida">правило</span>. «Где?» — я <strong>на работе</strong>. «Куда?» — я еду <strong>на работу</strong>. Один предлог, два <span class="cn-word" data-tr="qoʻshimchalar">окончания</span>.</p>

<p>Один раз я говорю <span class="cn-word" data-tr="notoʻgʻri">неправильно</span>.</p>

<p>Я в <span class="cn-word" data-tr="taksi">такси</span> и говорю: «Я еду <strong>в Москве</strong>».</p>

<p><span class="cn-word" data-tr="haydovchi">Водитель</span> смеётся.</p>

<p>— Вы уже <strong>в Москве</strong>, — говорит он. — А <strong>куда</strong> вы едете?</p>

<p>Теперь я помню это <span class="cn-word" data-tr="butun umr">всю жизнь</span>. <strong>-Е</strong> — это «здесь». <strong>-У</strong> — это «туда».</p>

<p><strong>В субботу</strong> я еду <strong>в деревню</strong>. В <span class="cn-word" data-tr="yakshanba">воскресенье</span> — <strong>домой</strong>.</p>

<p>Я ещё не знаю город. Но я уже знаю <span class="cn-word" data-tr="asosiy savol">главный вопрос</span>: «Куда?»</p>''',
        "questions": [
            {
                "text": "Taksida qanday xato qilindi?",
                "choices": [
                    "«В Москве» deyildi — bu «Moskvada», «Moskvaga» emas",
                    "Manzil notoʻgʻri aytildi",
                    "Haydovchiga salom berilmadi",
                    "Pul yetmadi"
                ],
                "answer": 0,
                "explanation": "«Я еду в Москве» soʻzma-soʻz «Moskva ichida "
                               "ketyapman» degani. Haydovchining javobi shuning uchun "
                               "kulgili: «Вы уже в Москве. А куда вы едете?»",
            },
            {
                "text": "Matndagi qoidani oʻz soʻzingiz bilan ayting: -Е va -У nima "
                        "farq qiladi?",
                "choices": [
                    "-Е joyni bildiradi (qayerda), -У manzilni (qayerga)",
                    "-Е koʻplik, -У birlik",
                    "-Е oʻtgan zamon, -У hozirgi",
                    "-Е erkak jinsi, -У ayol jinsi"
                ],
                "answer": 0,
                "explanation": "Matnning oʻzi buni aytadi: «-Е — это „здесь“. -У — "
                               "это „туда“». Predlog ikkala holatda ham bir xil, "
                               "shuning uchun maʼnoni faqat qoʻshimcha hal qiladi — "
                               "xuddi oʻzbekchadagi -DA va -GA kabi.",
            },
            {
                "text": "Nega «в библиотеку», lekin «в магазин»?",
                "choices": [
                    "Библиотека ayol jinsida (-У), магазин esa jonsiz erkak (oʻzgarmaydi)",
                    "Chunki kutubxona kattaroq",
                    "Chunki «магазин» chet soʻzi",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham Винительный, ikkalasi ham «куда?». Ayol "
                               "jinsi -У oladi, jonsiz erkak esa umuman oʻzgarmaydi — "
                               "unga faqat predlog qoʻshiladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-34 — Р.п. egalik va нет                OILA TARIXI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Дом моего деда",
        "summary": (
            "PR-34 matni. Qishloqdagi eski uy — bobodan otaga, otadan bizga. "
            "Uyda koʻp narsa yoʻq, lekin buvining bir jumlasi nima borligini "
            "aytib beradi."
        ),
        "order":   34,
        "grammar": [
            {
                "pattern":  "Egalik: книга брата",
                "meaning":  "Egasi HAR DOIM orqada turadi va u kelishikka kiradi. "
                            "Oʻzbekchaning teskarisi: «akaning kitobi» → «книга "
                            "брата». Birinchi soʻz bosh kelishikda qoladi.",
                "examples": ["Это дом деда.", "Окно кухни смотрит на восток."],
            },
            {
                "pattern":  "нет + Родительный",
                "meaning":  "«Yoʻq» dan keyin ot har doim Родительный'da: есть "
                            "книга → нет книги. Oʻzbekchada ot oʻzgarmaydi, "
                            "ruschada oʻzgaradi.",
                "examples": ["Здесь нет телевизора.", "В городе нет времени."],
            },
            {
                "pattern":  "время → времени",
                "meaning":  "-МЯ ga tugaydigan kichik guruh (время, имя) alohida "
                            "turlanadi. «Нет времени» — rus tilida eng koʻp "
                            "aytiladigan iboralardan biri.",
                "examples": ["В городе нет времени. А здесь время есть."],
            },
        ],
        "body": '''<p>В деревне есть старый дом. Это дом <strong>деда</strong>.</p>

<p><span class="cn-word" data-tr="bobo">Дед</span> <span class="cn-word" data-pos="verb" data-tr="qurgan">строил</span> этот дом долго. Три года.</p>

<p>Дом <strong>деда</strong> не большой. Две комнаты и <span class="cn-word" data-tr="oshxona">кухня</span>. Окно <strong>кухни</strong> смотрит на <span class="cn-word" data-tr="sharq">восток</span>.</p>

<p>Здесь нет <strong>телевизора</strong>. Нет <strong>интернета</strong>. Зимой <span class="cn-word" data-tr="baʼzan">иногда</span> нет <strong>воды</strong>.</p>

<p>Но здесь есть <span class="cn-word" data-tr="sukunat">тишина</span>. И <span class="cn-word" data-tr="hid">запах</span> <strong>хлеба</strong>.</p>

<p>Каждое лето мы едем в деревню.</p>

<p>Бабушка сидит на <span class="cn-word" data-tr="ayvonda">веранде</span> и говорит медленно.</p>

<p>— В городе нет <strong>времени</strong>, — говорит бабушка. — А здесь время есть.</p>

<p>Я думаю об этом <span class="cn-word" data-tr="uzoq">долго</span>. Бабушка <span class="cn-word" data-tr="haqli">права</span>.</p>

<p>В городе у нас есть телевизор, интернет и вода. Но нет <strong>времени</strong>.</p>

<p>Здесь нет <strong>телевизора</strong>. Но есть время, тишина и хлеб.</p>

<p><span class="cn-word" data-tr="avvaliga">Сначала</span> это был дом <strong>деда</strong>. Потом — дом <strong>отца</strong>. Теперь это наш дом.</p>''',
        "questions": [
            {
                "text": "Buvining gapi nimani anglatadi?",
                "choices": [
                    "Shaharda hamma narsa bor, lekin vaqt yoʻq; qishloqda teskarisi",
                    "Qishloqda hayot qiyinroq",
                    "Shaharda yashash yaxshiroq",
                    "Buvi shaharga koʻchmoqchi"
                ],
                "answer": 0,
                "explanation": "«В городе нет времени. А здесь время есть» — matn "
                               "shu jumla atrofida qurilgan. Keyingi xatboshi uni "
                               "ochib beradi: shaharda televizor, internet va suv "
                               "bor, lekin vaqt yoʻq.",
            },
            {
                "text": "«Дом деда» nega «деда дом» emas?",
                "choices": [
                    "Ruschada egalik bildiruvchi soʻz har doim orqada turadi",
                    "Chunki «дед» erkak jinsida",
                    "Chunki uy kattaroq",
                    "Ikkala variant ham toʻgʻri"
                ],
                "answer": 0,
                "explanation": "Bu oʻzbekchaning teskarisi. Oʻzbekchada «bobo-NING "
                               "uy-I» — egasi oldinda va ikkala soʻz belgilanadi. "
                               "Ruschada «дом деда» — egasi orqada va faqat u "
                               "kelishikka kiradi.",
            },
            {
                "text": "«Здесь нет телевизора» — nega «телевизор» emas?",
                "choices": [
                    "«Нет» dan keyin ot har doim Родительный padejida boʻladi",
                    "Chunki televizor jonli hisoblanadi",
                    "Chunki bu koʻplik",
                    "Chunki bu oʻtgan zamon"
                ],
                "answer": 0,
                "explanation": "Solishtiring: «есть телевизор» (bosh kelishik) va «нет "
                               "телевизора» (Родительный). Oʻzbekchada ot ikkala "
                               "gapda ham oʻzgarmaydi — «televizor bor / televizor "
                               "yoʻq» — shuning uchun bu qoidani alohida yodlash "
                               "kerak.",
            },
        ],
    },
]
