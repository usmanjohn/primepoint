# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-38 … PR-40.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 38 — hikoya (qish), 39 — retsept, 40 — intervyu.
(35 xat, 36 ilmiy-ommabop, 37 sinf sahnasi edi.)

⚠️ SARLAVHA TUZATILDI. Toc'da «Как делают самса» yozilgan edi — bu
grammatik jihatdan notoʻgʻri: делают feʼli Винительный talab qiladi,
demak «самсу». Grammatika kursida sarlavhaning oʻzi xato boʻlishi mumkin
emas, shuning uchun «Как делают самсу» qilindi.

Uzviylik: 38-matn PR-35 dagi «Письмо из Сибири» ning davomi — oʻsha
Sherbek, oʻsha Sibir, endi uning birinchi qishi. Oʻquvchi tanish odamni
qayta uchratadi.

Grammatika chegarasi (kumulyativ qoida):
  38-matn: Д.п. — мне холодно, yosh, К va ПО predloglari.
  39-matn: Т.п. — asbob (predlogsiz: ножом, руками) va hamroh (С bilan).
           Matnning butun mazmuni aynan shu farq ustiga qurilgan.
  40-matn: Т.п. — кем стать / работать. Oxirgi jumla hozirgi zamondagi
           bosh kelishik bilan kelasi zamondagi Т.п. ni yonma-yon qoʻyadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_38_40.py --author=prime
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
    # PR-38 — Д.п. holat, yosh, К, ПО            HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Первая зима",
        "summary": (
            "PR-38 matni. «Письмо из Сибири» ning davomi: Sherbekning Sibirdagi "
            "birinchi qishi. Minus oʻttiz, sotuvchi ayolning maslahati va "
            "hayotdagi birinchi marta yoqqan qish."
        ),
        "order":   38,
        "grammar": [
            {
                "pattern":  "Мне холодно — holat",
                "meaning":  "Shaxssiz gap: ega yoʻq, olmosh Дательный'da. Oʻzbekcha "
                            "«menga sovuq» ning aynan oʻzi. Oʻtgan zamonda «было» — "
                            "har doim oʻrta jinsda.",
                "examples": ["Ему холодно.", "Ему было холодно."],
            },
            {
                "pattern":  "Yosh — Дательный bilan",
                "meaning":  "Rus tilida yosh «menga ... yil» shaklida aytiladi: Мне "
                            "двадцать четыре года. Oʻzbekchada esa «men ... "
                            "yoshdaman» — ega bor. Ikkalasi ham gʻalati, lekin "
                            "boshqacha gʻalati.",
                "examples": ["Мне двадцать четыре года."],
            },
            {
                "pattern":  "К va ПО + Дательный",
                "meaning":  "К — odam yoki narsa TOMON (к магазину). ПО — boʻylab "
                            "(по улице, по городу). Diqqat: joyga kirish uchun В "
                            "ishlatiladi, К emas.",
                "examples": ["Он идёт к магазину.", "Он идёт по улице."],
            },
        ],
        "body": '''<p>Шербек из Ташкента. Теперь он живёт в Сибири. Это его первая <span class="cn-word" data-tr="qish">зима</span>.</p>

<p>В Ташкенте зимой тоже холодно. Но здесь другой холод.</p>

<p>Первый день. <span class="cn-word" data-tr="minus oʻttiz">Минус тридцать</span>.</p>

<p><strong>Ему</strong> холодно. <strong>Ему</strong> холодно утром, днём и вечером.</p>

<p>Он идёт <strong>по</strong> улице медленно. Он идёт <strong>к</strong> магазину.</p>

<p>В магазине <strong>ему</strong> тепло. Он не хочет идти домой.</p>

<p><span class="cn-word" data-tr="sotuvchi ayol">Продавщица</span> смотрит и говорит:</p>

<p>— Вы с юга?</p>

<p>— Да. Из Ташкента.</p>

<p>— <span class="cn-word" data-tr="Sizga ... kerak">Вам нужен</span> <span class="cn-word" data-tr="sharf">шарф</span>, — говорит она. — И <span class="cn-word" data-tr="qalpoq">шапка</span>. И <span class="cn-word" data-tr="qoʻlqoplar">рукавицы</span>.</p>

<p>Шербек покупает всё.</p>

<p><span class="cn-word" data-tr="Bir oydan keyin">Через месяц</span> он идёт <strong>по</strong> городу — и <strong>ему</strong> не холодно.</p>

<p>Он идёт <strong>к</strong> озеру. Там белый лёд и <span class="cn-word" data-tr="quyosh">солнце</span>.</p>

<p>Вечером он пишет Афсоне:</p>

<p>«<strong>Мне</strong> двадцать четыре года. И зима <strong>мне</strong> нравится. Первый раз <span class="cn-word" data-tr="hayotda">в жизни</span>».</p>''',
        "questions": [
            {
                "text": "Sotuvchi ayol nega Sherbekning janubdan ekanini payqadi?",
                "choices": [
                    "U doʻkonda isinib turgan va uyga ketishni istamagan",
                    "U ruscha gapira olmagan",
                    "U sharf soʻragan",
                    "U koʻlga borishni soʻragan"
                ],
                "answer": 0,
                "explanation": "«В магазине ему тепло. Он не хочет идти домой» — "
                               "shundan keyin darrov sotuvchining savoli keladi: «Вы с "
                               "юга?». Sovuqqa oʻrganmagan odam koʻrinib turadi.",
            },
            {
                "text": "«Ему холодно» va «Мне двадцать четыре года» — bu ikki "
                        "gapda nima umumiy?",
                "choices": [
                    "Ikkalasida ham ega yoʻq va olmosh Дательный padejida",
                    "Ikkalasi ham oʻtgan zamon",
                    "Ikkalasi ham savol",
                    "Ikkalasida ham feʼl bor"
                ],
                "answer": 0,
                "explanation": "Rus tilida holat ham, yosh ham shaxssiz qurilish bilan "
                               "aytiladi: «unga sovuq», «menga yigirma toʻrt yil». "
                               "Oʻzbekchada birinchisi bir xil («menga sovuq»), "
                               "ikkinchisi esa boshqacha («men yoshdaman»).",
            },
            {
                "text": "Matnning oxirgi jumlasi nega muhim?",
                "choices": [
                    "Sherbek hayotida birinchi marta qish unga yoqyapti",
                    "Sherbek Toshkentga qaytmoqchi",
                    "Sherbek sovuqni yomon koʻradi",
                    "Sherbek yigirma toʻrt yoshini nishonlayapti"
                ],
                "answer": 0,
                "explanation": "«И зима мне нравится. Первый раз в жизни». Matn "
                               "boshida unga har vaqt sovuq edi; oxirida esa u koʻl "
                               "tomon yuradi va qish unga yoqadi. Oʻzgargan narsa — "
                               "sharf emas, odamning oʻzi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-39 — Т.п. asbob va hamroh                RETSEPT
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Как делают самсу",
        "summary": (
            "PR-39 matni. Samsa retsepti — xamir, goʻsht, piyoz. Har bir qadamda "
            "asbob koʻrsatiladi (ножом, руками), va oxirida buvi eng muhim "
            "«bilan» ni aytadi."
        ),
        "order":   39,
        "grammar": [
            {
                "pattern":  "Asbob — predlogsiz",
                "meaning":  "«Nima bilan?» degan savolga javob predlogSIZ beriladi: "
                            "резать ножом, делать руками. Oʻzbekcha «bilan» bu "
                            "yerda ruschada hech qanday soʻz bilan tarjima qilinmaydi "
                            "— faqat qoʻshimcha.",
                "examples": ["Лук режут ножом.", "Тесто делают руками."],
            },
            {
                "pattern":  "Hamroh va qoʻshimcha — С bilan",
                "meaning":  "«Kim bilan?» yoki «nima qoʻshib?» — С predlogi bilan: "
                            "с солью, с людьми. Bu yerda predlog SHART.",
                "examples": ["Мясо с солью и с перцем.", "Самсу делают с людьми."],
            },
            {
                "pattern":  "Qoʻshimchalar: -ом/-ем · -ой/-ей",
                "meaning":  "Erkak va oʻrta jins -ОМ/-ЕМ (ножом, перцем), ayol jinsi "
                            "-ОЙ/-ЕЙ (ложкой). Ayol jinsidagi -Ь otlari -ЬЮ oladi: "
                            "соль → солью.",
                "examples": ["Ложкой. Ножом. Солью."],
            },
        ],
        "body": '''<p>Самса — это <span class="cn-word" data-tr="xamir">тесто</span> и <span class="cn-word" data-tr="goʻsht">мясо</span>. И ещё лук. Много лука.</p>

<p>Сначала делают тесто. <span class="cn-word" data-tr="un">Мука</span>, вода, <span class="cn-word" data-tr="tuz">соль</span>. Всё.</p>

<p>Тесто делают <strong>руками</strong>. Не машиной. <strong>Руками</strong> <span class="cn-word" data-tr="yaxshiroq">лучше</span>.</p>

<p>Потом лук. Лук <span class="cn-word" data-pos="verb" data-tr="kesishadi">режут</span> <strong>ножом</strong>. <span class="cn-word" data-tr="mayda">Мелко</span>.</p>

<p>Мясо тоже режут <strong>ножом</strong>. Не машиной! Это важно.</p>

<p>Потом мясо и лук <strong>с</strong> солью и <strong>с</strong> <span class="cn-word" data-tr="qalampir">перцем</span>.</p>

<p>Самсу делают <strong>руками</strong>. Одна самса — одна минута.</p>

<p>Потом <span class="cn-word" data-tr="tandir">тандыр</span>. Или <span class="cn-word" data-tr="duxovka">духовка</span>. Двадцать минут.</p>

<p>Бабушка говорит так:</p>

<p>— Нож — это не главное. Тандыр — тоже не главное.</p>

<p>— А что главное? — спрашивает Бекзод.</p>

<p>— Люди, — говорит бабушка. — Самсу делают <strong>с людьми</strong>. Один человек и одна самса — это не праздник. Это просто <span class="cn-word" data-tr="ovqat">еда</span>.</p>''',
        "questions": [
            {
                "text": "Buvining fikricha, samsada eng muhimi nima?",
                "choices": [
                    "Odamlar — samsa birga tayyorlanadi",
                    "Tandir",
                    "Pichoq",
                    "Xamirning sifati"
                ],
                "answer": 0,
                "explanation": "«Нож — это не главное. Тандыр — тоже не главное… "
                               "Люди». Buvi asbobdan odamga oʻtadi: «Один человек и "
                               "одна самса — это не праздник».",
            },
            {
                "text": "Nega matnda «ножом», lekin «с солью»?",
                "choices": [
                    "Pichoq — asbob (predlogsiz), tuz esa qoʻshiladigan narsa (С bilan)",
                    "Chunki «нож» erkak jinsida",
                    "Chunki tuz sanalmaydi",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham Творительный padejida. Farqni predlog "
                               "qiladi: asbob qoʻlingizda — predlog qoʻyilmaydi; nimadir "
                               "qoʻshilsa yoki kimdir hamroh boʻlsa — С qoʻyiladi. "
                               "Oʻzbekcha «bilan» ikkalasini ham qoplaydi.",
            },
            {
                "text": "Oxirgi jumladagi «с людьми» nega darsning eng yaxshi "
                        "misoli?",
                "choices": [
                    "Chunki bu matndagi yagona haqiqiy hamroh — qolgani asbob",
                    "Chunki bu koʻplik shakli",
                    "Chunki odamlarni sanash mumkin emas",
                    "Chunki bu buvining gapi"
                ],
                "answer": 0,
                "explanation": "Butun matn boʻyi asboblar sanaladi — руками, ножом — "
                               "va ularning hech birida предлог yoʻq. Oxirida esa "
                               "odamlar keladi, va u yerda С paydo boʻladi. Grammatika "
                               "matnning maʼnosini takrorlaydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-40 — Т.п. кем стать                      INTERVYU
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Кем ты хочешь стать?",
        "summary": (
            "PR-40 matni. Jurnalist Nina maktabga qaytadi va bitta savol beradi. "
            "Javoblar oddiy — Jasurniki bundan mustasno, va u nega bobosidan "
            "boshqa yoʻlni tanlaganini tushuntiradi."
        ),
        "order":   40,
        "grammar": [
            {
                "pattern":  "стать / работать + Творительный",
                "meaning":  "«Kim boʻlib?» degan savolga javob: хочу стать врачом, "
                            "работает строителем. Oʻzbekchada bu «boʻlib» soʻzi "
                            "bilan beriladi.",
                "examples": ["Я хочу стать врачом.", "Отец работает строителем."],
            },
            {
                "pattern":  "Feʼl bor — Т.п., feʼl yoʻq — bosh kelishik",
                "meaning":  "Hozirgi zamonda «быть» aytilmaydi, shuning uchun kasb "
                            "bosh kelishikda qoladi: Я ученик. Oʻtgan va kelasi "
                            "zamonda feʼl paydo boʻladi va u bilan Т.п. keladi.",
                "examples": ["Сейчас я ученик.", "Дед был строителем."],
            },
            {
                "pattern":  "кто → кем",
                "meaning":  "Savol soʻzining oʻzi ham kelishikka kiradi. «Кем ты "
                            "хочешь стать?» — rus maktablarida har yili beriladigan "
                            "savol.",
                "examples": ["Кем ты хочешь стать?"],
            },
        ],
        "body": '''<p>Нина делает <span class="cn-word" data-tr="intervyu">интервью</span> в школе. Один <span class="cn-word" data-tr="savol">вопрос</span>: «<strong>Кем</strong> ты хочешь <strong>стать</strong>?»</p>

<p>Афсона: «Я хочу <strong>стать врачом</strong>. Моя мама работает <strong>врачом</strong>».</p>

<p>Бекзод: «Я хочу <strong>стать футболистом</strong>».</p>

<p>Катя: «Я не знаю. <span class="cn-word" data-tr="Balki">Может быть</span>, <strong>учителем</strong>».</p>

<p>Жасур молчит.</p>

<p>— А ты? — спрашивает Нина.</p>

<p>— Мой <span class="cn-word" data-tr="bobo">дед</span> был <strong>строителем</strong>, — говорит Жасур. — Мой отец работает <strong>строителем</strong>.</p>

<p>— И ты будешь <strong>строителем</strong>?</p>

<p>— Нет. Я хочу <strong>стать архитектором</strong>.</p>

<p>Нина <span class="cn-word" data-pos="verb" data-tr="hayron boʻladi">удивляется</span>.</p>

<p>— Это <span class="cn-word" data-tr="deyarli bir xil narsa">почти одно и то же</span>, — говорит она.</p>

<p>— Нет, — говорит Жасур. — Дед <span class="cn-word" data-pos="verb" data-tr="qurgan">строил</span> <strong>руками</strong>. Отец тоже. А я хочу строить <strong>головой</strong>. Потом <strong>руками</strong> — но уже <strong>с</strong> <span class="cn-word" data-tr="reja">планом</span>.</p>

<p>Нина <span class="cn-word" data-pos="verb" data-tr="yozib oladi">записывает</span>. Потом спрашивает:</p>

<p>— А кто ты сейчас?</p>

<p>— Сейчас я <strong>ученик</strong>, — говорит Жасур.</p>

<p>И это <span class="cn-word" data-tr="toʻgʻri">правильно</span>. Сейчас — <strong>ученик</strong>. Потом — <strong>архитектором</strong>.</p>''',
        "questions": [
            {
                "text": "Jasurning fikricha, quruvchi va arxitektor nima bilan farq "
                        "qiladi?",
                "choices": [
                    "Bobosi qoʻl bilan qurgan, u esa avval boshi bilan qurmoqchi",
                    "Arxitektor koʻproq pul oladi",
                    "Quruvchi maktabda oʻqimaydi",
                    "Farqi yoʻq"
                ],
                "answer": 0,
                "explanation": "«Дед строил руками. Отец тоже. А я хочу строить "
                               "головой. Потом руками — но уже с планом». U "
                               "oilasidan voz kechmayapti — oʻsha ishga boshqa "
                               "tomondan kirmoqchi.",
            },
            {
                "text": "«Сейчас я ученик» — nega bu yerda «учеником» emas?",
                "choices": [
                    "Hozirgi zamonda «быть» aytilmaydi, demak kelishik ham kerak emas",
                    "Chunki «ученик» erkak jinsida",
                    "Chunki bu savolga javob",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Qoida: feʼl bor boʻlsa — Творительный, feʼl yoʻq "
                               "boʻlsa — bosh kelishik. Shuning uchun oxirgi jumla ikki "
                               "shaklni yonma-yon qoʻyadi: «Сейчас — ученик. Потом — "
                               "архитектором».",
            },
            {
                "text": "Matnda «руками» ham, «с планом» ham bor. Nega biri "
                        "predlogsiz?",
                "choices": [
                    "Qoʻl — asbob (predlogsiz), reja esa qoʻshimcha narsa (С bilan)",
                    "Chunki «руки» koʻplikda",
                    "Chunki reja jonli hisoblanadi",
                    "Ikkalasi ham predlogsiz boʻlishi kerak"
                ],
                "answer": 0,
                "explanation": "PR-39 dagi farq bu yerda ham ishlaydi. Qoʻl bilan "
                               "quriladi — u asbob. Reja esa yonida boʻladigan narsa — "
                               "«qurmoqchiman, lekin rejam bor holda».",
            },
        ],
    },
]
