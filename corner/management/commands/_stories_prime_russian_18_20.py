# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-18 … PR-20.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Shakl xilma-xilligi: 18 — sinfdagi sahna, 19 — anketa/hujjat (yangi janr),
20 — kunlik tartib matni.

⚠️ ISTISNO TUGADI. PR-19 dan feʼl tizimi ochildi, shuning uchun 19-matndan
boshlab "narrative frame" istisnosi ishlatilmaydi — feʼllar oddiy grammatika
sifatida keladi. 18-matn hali eski qoidada (feʼl darsi undan keyin).
20-matnda faqat I tuslanish feʼllari (PR-20) ishlatiladi: работать, читать,
знать, делать, думать, понимать, слушать, гулять, играть + frame feʼllari.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_18_20.py --author=prime
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
    # PR-18 — тоже / ещё / уже            SINFDAGI SAHNA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Мы тоже!",
        "summary": (
            "PR-18 matni. Sinfda bitta bola qoʻlini koʻtaradi — keyin ikkinchisi, "
            "keyin hammasi. «Тоже» soʻzi qanday qilib butun sinfni harakatga "
            "keltirishini koʻrasiz."
        ),
        "order":   18,
        "grammar": [
            {
                "pattern":  "тоже",
                "meaning":  "«Men ham» — yangi ega qoʻshadi, kimdir yana shuni qilyapti. "
                            "Kundalik nutqda deyarli har doim ТОЖЕ ishlatiladi, "
                            "ТАКЖЕ esa kitobiy va rasmiyroq.",
                "examples": ["Я тоже.", "Жасур тоже здесь."],
            },
            {
                "pattern":  "ещё / уже",
                "meaning":  "ЕЩЁ — hali, yana. УЖЕ — allaqachon. Inkor shakllari ham "
                            "juftlik: ЕЩЁ НЕ (hali … emas) va УЖЕ НЕ (endi … emas).",
                "examples": ["Уже двадцать!", "Ещё не все."],
            },
            {
                "pattern":  "Ravish: -ый → -о",
                "meaning":  "Ravish hech nimaga moslashmaydi. U sifatdan yasaladi: "
                            "тихий → тихо, громкий → громко. Sifat OTNI, ravish esa "
                            "HOLAT yoki HARAKATNI taʼriflaydi.",
                "examples": ["Здесь тихо.", "Громко!"],
            },
        ],
        "body": '''<p>Урок. Здесь <span class="cn-word" data-tr="jimjit">тихо</span>. Марина Олеговна <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказала</span>: «Суббота — <span class="cn-word" data-tr="ekskursiya">экскурсия</span>. Музей. Кто?»</p>

<p><span class="cn-word" data-tr="jimjitlik">Тишина</span>.</p>

<p><span class="cn-word" data-tr="Keyin">Потом</span> Афсона: «Я».</p>

<p>Дилноза: «Я <strong>тоже</strong>».</p>

<p>Шербек: «И я <strong>тоже</strong>».</p>

<p>Жасур сказал <strong>громко</strong>: «Мы <strong>тоже</strong>!» — а <span class="cn-word" data-tr="yonida">рядом</span> Бекзод, и Бекзод <span class="cn-word" data-tr="hali">ещё</span> <span class="cn-word" data-tr="kichkina">маленький</span>.</p>

<p>Марина Олеговна: «Бекзод <strong>ещё не</strong> <span class="cn-word" data-tr="oʻquvchi">ученик</span>».</p>

<p>Жасур: «Но он <strong>уже не</strong> маленький!»</p>

<p>Здесь <strong>уже</strong> не тихо. <span class="cn-word" data-tr="Hamma">Все</span> — «я <strong>тоже</strong>», «и я», «мы <strong>тоже</strong>».</p>

<p>Марина Олеговна сказала: «Хорошо. <strong>Уже</strong> двадцать один. И Бекзод — <strong>тоже</strong>».</p>''',
        "questions": [
            {
                "text": "Bekzod ekskursiyaga boradimi?",
                "choices": [
                    "Ha — oxirida oʻqituvchi uni ham qoʻshdi",
                    "Yoʻq, u hali oʻquvchi emas",
                    "Noaniq qoldi",
                    "Yoʻq, u kasal"
                ],
                "answer": 0,
                "explanation": "Oʻqituvchi avval «Бекзод ещё не ученик» dedi, lekin "
                               "oxirida «Уже двадцать один. И Бекзод — тоже» — yaʼni "
                               "u ham roʻyxatga kirdi.",
            },
            {
                "text": "«Бекзод ещё не ученик» va «Он уже не маленький» — bu ikki gap "
                        "nimani koʻrsatadi?",
                "choices": [
                    "ЕЩЁ НЕ — hali boshlanmagan, УЖЕ — allaqachon boshlangan",
                    "Ikkalasi bir xil maʼnoda",
                    "Birinchisi kelasi zamon, ikkinchisi oʻtgan",
                    "ЕЩЁ НЕ — endi emas, УЖЕ — hali emas"
                ],
                "answer": 0,
                "explanation": "Bu vaqt chizigʻining ikki nuqtasi. Bekzod hali maktabga "
                               "kirmagan (ещё не), lekin allaqachon kichkina emas "
                               "(уже не). Toʻliq toʻrtlik: ещё не → уже → ещё → уже не.",
            },
            {
                "text": "Matnda «Здесь тихо» va keyin «уже не тихо» bor. «Тихо» "
                        "qaysi soʻz turkumi?",
                "choices": [
                    "Ravish — u holatni taʼriflaydi, otni emas",
                    "Sifat — u sinfni taʼriflaydi",
                    "Feʼl",
                    "Ot"
                ],
                "answer": 0,
                "explanation": "Gapda taʼriflanadigan ot yoʻq — bu holat, demak ravish. "
                               "Sifat boʻlganda «тихий класс» boʻlardi. Ravish "
                               "sifatdan yasaladi: тихий → тихо.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-19 — infinitiv                   ANKETA (yangi janr)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Анкета",
        "summary": (
            "PR-19 matni. Maktabda toʻgaraklarga yozilish anketasi — uchta oʻquvchi "
            "toʻldirgan. Javoblarning hammasi infinitivda. Oxirgi anketa qoidani "
            "buzadi, va aynan shuning uchun eng yaxshisi."
        ),
        "order":   19,
        "grammar": [
            {
                "pattern":  "Infinitiv (-ть)",
                "meaning":  "Feʼlning lugʻat shakli, oʻzbekchadagi -moq ga toʻgʻri "
                            "keladi. U hech kimga tegishli emas — shunchaki harakatning "
                            "nomi. Shuning uchun roʻyxat va anketalarda aynan shu shakl "
                            "ishlatiladi.",
                "examples": ["читать", "рисовать", "играть"],
            },
            {
                "pattern":  "I va II tuslanish",
                "meaning":  "Feʼllar ikki guruhga boʻlinadi. Ishonchli belgi — «ты» "
                            "shakli: -ЕШЬ = I tuslanish (читаешь), -ИШЬ = II tuslanish "
                            "(говоришь). Infinitiv oxiri faqat maslahat beradi.",
                "examples": ["читать → читаешь (I)", "говорить → говоришь (II)"],
            },
            {
                "pattern":  "Soʻz tartibi: ega → feʼl → toʻldiruvchi",
                "meaning":  "Oʻzbek gapida feʼl OXIRIDA turadi, rus gapida OʻRTADA. "
                            "«Men kitob oʻqiyman» → «Я читаю книгу». Bu kursdagi eng "
                            "muhim tartib farqi.",
                "examples": ["Я читаю.", "Бекзод работает."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Maktab toʻgaraklari">Школьные кружки</span>. <span class="cn-word" data-tr="Anketa">Анкета</span>.</p>

<p><span class="cn-word" data-tr="Ism">Имя</span>: Афсона. <span class="cn-word" data-tr="Sinf">Класс</span>: 9 «А».<br>
Что <span class="cn-word" data-tr="qilmoq">делать</span>? — <strong>Читать</strong> и <strong><span class="cn-word" data-tr="yozmoq">писать</span></strong>.<br>
<span class="cn-word" data-tr="Nima uchun">Зачем</span>? — <span class="cn-word" data-tr="Chunki">Потому что</span> я <strong>читаю</strong> каждый день.</p>

<p>Имя: Жасур. Класс: 9 «А».<br>
Что делать? — <strong>Играть</strong>. <span class="cn-word" data-tr="Futbol">Футбол</span>.<br>
Зачем? — Потому что я <strong>играю</strong> хорошо.</p>

<p>Имя: Дилноза. Класс: 9 «А».<br>
Что делать? — <strong><span class="cn-word" data-tr="rasm chizmoq">Рисовать</span></strong> и <strong><span class="cn-word" data-tr="qoʻshiq aytmoq">петь</span></strong>.<br>
Зачем? — <strong>Не знаю</strong>. Просто хорошо.</p>

<p>И <span class="cn-word" data-tr="yana bitta">ещё одна</span> анкета.</p>

<p>Имя: Бекзод. Класс: — <span class="cn-word" data-tr="hali yoʻq">ещё нет</span>.<br>
Что делать? — <strong>Читать</strong>, <strong>рисовать</strong>, <strong>играть</strong>, <strong>петь</strong>. <span class="cn-word" data-tr="Hammasi">Всё</span>.<br>
Зачем? — Потому что Афсона, Жасур и Дилноза — <span class="cn-word" data-tr="u yerda">там</span>.</p>''',
        "questions": [
            {
                "text": "Bekzodning anketasi nega boshqalardan farq qiladi?",
                "choices": [
                    "U bitta toʻgarak emas, hammasini tanladi — chunki doʻstlari oʻsha yerda",
                    "U hech nima yozmadi",
                    "U anketani notoʻgʻri toʻldirdi",
                    "U faqat futbolni tanladi"
                ],
                "answer": 0,
                "explanation": "Bekzodning javobi: «Читать, рисовать, играть, петь. "
                               "Всё» — va sababi: «Потому что Афсона, Жасур и Дилноза "
                               "— там». Uni toʻgarak emas, odamlar qiziqtiradi.",
            },
            {
                "text": "Nega anketadagi javoblar infinitivda (читать, играть) berilgan?",
                "choices": [
                    "Chunki infinitiv hech kimga tegishli emas — u shunchaki harakatning nomi",
                    "Chunki bu oʻtgan zamon",
                    "Chunki bu buyruq shakli",
                    "Chunki anketada faqat koʻplik ishlatiladi"
                ],
                "answer": 0,
                "explanation": "Infinitiv — feʼlning lugʻat shakli, oʻzbekchadagi -moq. "
                               "U shaxsni koʻrsatmaydi, shuning uchun roʻyxat, anketa va "
                               "menyularda aynan shu shakl ishlatiladi.",
            },
            {
                "text": "Matnda «я играю хорошо» bor. Nega «хороший» emas?",
                "choices": [
                    "Chunki bu harakatni taʼriflaydi — demak ravish kerak",
                    "Chunki «я» erkak jinsida",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki «играю» koʻplikda"
                ],
                "answer": 0,
                "explanation": "«Хорошо» — ravish, u qanday oʻynashini aytadi. "
                               "«Хороший» esa sifat va u otga kerak boʻlardi: "
                               "«хороший футбол». Sifat otni, ravish harakatni "
                               "taʼriflaydi (PR-18).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-20 — I tuslanish                 KUNLIK TARTIB
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Один день Жасура",
        "summary": (
            "PR-20 matni. Jasurning oddiy kuni — ertalabdan kechgacha. Deyarli har "
            "bir jumlada I tuslanish feʼli bor, va oxirida kichik bir narsa "
            "oʻzgaradi."
        ),
        "order":   20,
        "grammar": [
            {
                "pattern":  "I tuslanish: -ю, -ешь, -ет, -ем, -ете, -ют",
                "meaning":  "Oʻzak = infinitiv minus -ть. Naqsh hamma feʼlda bir xil "
                            "ishlaydi: чита-ю, чита-ешь, чита-ет… Oʻzbekchadagi "
                            "oʻqi-y-man / oʻqi-y-san bilan bir xil tuzilma.",
                "examples": ["Я читаю.", "Он работает.", "Они гуляют."],
            },
            {
                "pattern":  "не + feʼl",
                "meaning":  "Inkor: НЕ har doim feʼlning OLDIDA turadi. Oʻzbekchada "
                            "inkor qoʻshimcha ichida boʻladi (bilma-y-man), ruschada esa "
                            "alohida soʻz sifatida oldinda.",
                "examples": ["Я не знаю.", "Он не понимает."],
            },
            {
                "pattern":  "Ravish + feʼl",
                "meaning":  "Ravish harakatni taʼriflaydi va oʻzgarmaydi: быстро, "
                            "медленно, хорошо, часто. U odatda feʼldan oldin yoki "
                            "keyin turadi.",
                "examples": ["Он работает быстро.", "Мы часто гуляем."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Ertalab">Утро</span>. Жасур <span class="cn-word" data-pos="verb" data-tr="uygʻonadi">встаёт</span> <span class="cn-word" data-tr="erta">рано</span>. Бекзод <strong>ещё</strong> <span class="cn-word" data-pos="verb" data-tr="uxlaydi">спит</span>.</p>

<p>Жасур <strong>слушает</strong> <span class="cn-word" data-tr="radio">радио</span> и <strong>делает</strong> <span class="cn-word" data-tr="nonushta">завтрак</span>. Он <strong>делает</strong> это <span class="cn-word" data-tr="tez">быстро</span>, потому что урок <strong>уже</strong> <span class="cn-word" data-tr="yaqin, tez orada">скоро</span>.</p>

<p>Школа. Жасур <strong>читает</strong>, <strong>слушает</strong>, <strong>думает</strong>. Русский язык — трудно. Математика — легко. Жасур <strong>понимает</strong> хорошо, но медленно.</p>

<p>Потом — футбол. Жасур <strong>играет</strong> каждый день. Шербек <strong>играет</strong> тоже. Они <strong>играют</strong> громко и <span class="cn-word" data-tr="quvnoq">весело</span>.</p>

<p><span class="cn-word" data-tr="Kechqurun">Вечером</span> — <span class="cn-word" data-tr="doʻkon">магазин</span>. Жасур <strong>работает</strong> <span class="cn-word" data-tr="oz">мало</span>, два часа. Нина Петровна <span class="cn-word" data-pos="verb" data-tr="deydi">говорит</span>: «Жасур <strong>работает</strong> хорошо».</p>

<p><span class="cn-word" data-tr="Kech">Поздно</span>. Дом. Бекзод <strong>не</strong> <span class="cn-word" data-pos="verb" data-tr="uxlaydi">спит</span>. Бекзод <strong>ждёт</strong>.</p>

<p>Бекзод: «Жасур, ты <strong>читаешь</strong>?»</p>

<p>Жасур <strong>думает</strong>: утро — рано, школа — трудно, футбол, магазин. Он <span class="cn-word" data-tr="charchagan">устал</span>.</p>

<p>Жасур: «<strong>Читаю</strong>».</p>

<p>И они <strong>читают</strong>. Медленно, тихо. Каждый день.</p>''',
        "questions": [
            {
                "text": "Jasur kechqurun charchagan boʻlsa ham nima qiladi?",
                "choices": [
                    "Bekzod bilan birga kitob oʻqiydi",
                    "Darrov uxlaydi",
                    "Yana ishga boradi",
                    "Futbol oʻynaydi"
                ],
                "answer": 0,
                "explanation": "«Он устал» — charchagan. Lekin Bekzod kutib oʻtirgan edi "
                               "va Jasur «Читаю» dedi. Oxirgi jumla: «И они читают. "
                               "Медленно, тихо. Каждый день» — bu har kungi odat.",
            },
            {
                "text": "Matnda «Они играют» va «Жасур играет» bor. Nega qoʻshimcha "
                        "boshqa?",
                "choices": [
                    "Chunki feʼl egaga moslashadi: они → -ют, он → -ет",
                    "Chunki bir joyda oʻtgan zamon",
                    "Chunki «Жасур» erkak jinsida",
                    "Bu xato"
                ],
                "answer": 0,
                "explanation": "I tuslanish qoʻshimchalari: -ю, -ешь, -ет, -ем, -ете, "
                               "-ют. 3-shaxs birlik uchun -ЕТ, koʻplik uchun -ЮТ. Bu "
                               "eng koʻp adashtiriladigan juftlik.",
            },
            {
                "text": "«Бекзод не спит» gapida НЕ qayerda turibdi va nega?",
                "choices": [
                    "Feʼlning oldida — ruschada НЕ har doim inkor qilinadigan soʻz oldida",
                    "Feʼldan keyin",
                    "Gap oxirida",
                    "Gap boshida"
                ],
                "answer": 0,
                "explanation": "Ruscha НЕ har doim oldinda. Oʻzbekchada esa inkor "
                               "qoʻshimcha ichiga kiradi: «uxla-MA-ydi». Shuning uchun "
                               "oʻzbek oʻquvchisi НЕ ni tushirib qoldirishga yoki "
                               "notoʻgʻri joyga qoʻyishga moyil.",
            },
        ],
    },
]
