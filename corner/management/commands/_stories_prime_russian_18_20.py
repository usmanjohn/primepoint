# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-18 … PR-20.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Shakl xilma-xilligi: 18 — sinfdagi sahna, 19 — anketa/hujjat (yangi janr),
20 — kunlik tartib matni.

⚠️ ISTISNO TUGADI. PR-19 dan feʼl tizimi ochildi, shuning uchun 19-matndan
boshlab "narrative frame" istisnosi ishlatilmaydi — feʼllar oddiy grammatika
sifatida keladi. 18-matn hali eski qoidada (feʼl darsi undan keyin).
20-matnda faqat I tuslanish feʼllari (PR-20) ishlatiladi: рабо́тать, чита́ть,
знать, де́лать, ду́мать, понима́ть, слу́шать, гуля́ть, игра́ть + frame feʼllari.

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
        "title":   "Мы то́же!",
        "summary": (
            "PR-18 matni. Sinfda bitta bola qoʻlini koʻtaradi — keyin ikkinchisi, "
            "keyin hammasi. «Тоже» soʻzi qanday qilib butun sinfni harakatga "
            "keltirishini koʻrasiz."
        ),
        "order":   18,
        "grammar": [
            {
                "pattern":  "то́же",
                "meaning":  "«Men ham» — yangi ega qoʻshadi, kimdir yana shuni qilyapti. "
                            "Kundalik nutqda deyarli har doim ТО́ЖЕ ishlatiladi, "
                            "ТА́КЖЕ esa kitobiy va rasmiyroq.",
                "examples": ["Я то́же.", "Жасу́р то́же здесь."],
            },
            {
                "pattern":  "ещё / уже́",
                "meaning":  "ЕЩЁ — hali, yana. УЖЕ́ — allaqachon. Inkor shakllari ham "
                            "juftlik: ЕЩЁ НЕ (hali … emas) va УЖЕ́ НЕ (endi … emas).",
                "examples": ["Уже́ два́дцать!", "Ещё не все."],
            },
            {
                "pattern":  "Ravish: -ый → -о",
                "meaning":  "Ravish hech nimaga moslashmaydi. U sifatdan yasaladi: "
                            "ти́хий → ти́хо, гро́мкий → гро́мко. Sifat OTNI, ravish esa "
                            "HOLAT yoki HARAKATNI taʼriflaydi.",
                "examples": ["Здесь ти́хо.", "Гро́мко!"],
            },
        ],
        "body": '''<p>Уро́к. Здесь <span class="cn-word" data-tr="jimjit">ти́хо</span>. Мари́на Оле́говна <span class="cn-word" data-pos="verb" data-tr="dedi (ayol)">сказа́ла</span>: «Суббо́та — <span class="cn-word" data-tr="ekskursiya">экску́рсия</span>. Музе́й. Кто?»</p>

<p><span class="cn-word" data-tr="jimjitlik">Тишина́</span>.</p>

<p><span class="cn-word" data-tr="Keyin">Пото́м</span> Афсо́на: «Я».</p>

<p>Дилно́за: «Я <strong>то́же</strong>».</p>

<p>Шербе́к: «И я <strong>то́же</strong>».</p>

<p>Жасу́р сказа́л <strong>гро́мко</strong>: «Мы <strong>то́же</strong>!» — а <span class="cn-word" data-tr="yonida">ря́дом</span> Бекзо́д, и Бекзо́д <span class="cn-word" data-tr="hali">ещё</span> <span class="cn-word" data-tr="kichkina">ма́ленький</span>.</p>

<p>Мари́на Оле́говна: «Бекзо́д <strong>ещё не</strong> <span class="cn-word" data-tr="oʻquvchi">учени́к</span>».</p>

<p>Жасу́р: «Но он <strong>уже́ не</strong> ма́ленький!»</p>

<p>Здесь <strong>уже́</strong> не ти́хо. <span class="cn-word" data-tr="Hamma">Все</span> — «я <strong>то́же</strong>», «и я», «мы <strong>то́же</strong>».</p>

<p>Мари́на Оле́говна сказа́ла: «Хорошо́. <strong>Уже́</strong> два́дцать оди́н. И Бекзо́д — <strong>то́же</strong>».</p>''',
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
                "explanation": "Oʻqituvchi avval «Бекзо́д ещё не учени́к» dedi, lekin "
                               "oxirida «Уже́ два́дцать оди́н. И Бекзо́д — то́же» — yaʼni "
                               "u ham roʻyxatga kirdi.",
            },
            {
                "text": "«Бекзо́д ещё не учени́к» va «Он уже́ не ма́ленький» — bu ikki gap "
                        "nimani koʻrsatadi?",
                "choices": [
                    "ЕЩЁ НЕ — hali boshlanmagan, УЖЕ́ — allaqachon boshlangan",
                    "Ikkalasi bir xil maʼnoda",
                    "Birinchisi kelasi zamon, ikkinchisi oʻtgan",
                    "ЕЩЁ НЕ — endi emas, УЖЕ́ — hali emas"
                ],
                "answer": 0,
                "explanation": "Bu vaqt chizigʻining ikki nuqtasi. Bekzod hali maktabga "
                               "kirmagan (ещё не), lekin allaqachon kichkina emas "
                               "(уже́ не). Toʻliq toʻrtlik: ещё не → уже́ → ещё → уже́ не.",
            },
            {
                "text": "Matnda «Здесь ти́хо» va keyin «уже́ не ти́хо» bor. «Ти́хо» "
                        "qaysi soʻz turkumi?",
                "choices": [
                    "Ravish — u holatni taʼriflaydi, otni emas",
                    "Sifat — u sinfni taʼriflaydi",
                    "Feʼl",
                    "Ot"
                ],
                "answer": 0,
                "explanation": "Gapda taʼriflanadigan ot yoʻq — bu holat, demak ravish. "
                               "Sifat boʻlganda «ти́хий класс» boʻlardi. Ravish "
                               "sifatdan yasaladi: ти́хий → ти́хо.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-19 — infinitiv                   ANKETA (yangi janr)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Анке́та",
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
                "examples": ["чита́ть", "рисова́ть", "игра́ть"],
            },
            {
                "pattern":  "I va II tuslanish",
                "meaning":  "Feʼllar ikki guruhga boʻlinadi. Ishonchli belgi — «ты» "
                            "shakli: -ЕШЬ = I tuslanish (чита́ешь), -ИШЬ = II tuslanish "
                            "(говори́шь). Infinitiv oxiri faqat maslahat beradi.",
                "examples": ["чита́ть → чита́ешь (I)", "говори́ть → говори́шь (II)"],
            },
            {
                "pattern":  "Soʻz tartibi: ega → feʼl → toʻldiruvchi",
                "meaning":  "Oʻzbek gapida feʼl OXIRIDA turadi, rus gapida OʻRTADA. "
                            "«Men kitob oʻqiyman» → «Я чита́ю кни́гу». Bu kursdagi eng "
                            "muhim tartib farqi.",
                "examples": ["Я чита́ю.", "Бекзо́д рабо́тает."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Maktab toʻgaraklari">Шко́льные кружки́</span>. <span class="cn-word" data-tr="Anketa">Анке́та</span>.</p>

<p><span class="cn-word" data-tr="Ism">И́мя</span>: Афсо́на. <span class="cn-word" data-tr="Sinf">Класс</span>: 9 «А».<br>
Что <span class="cn-word" data-tr="qilmoq">де́лать</span>? — <strong>Чита́ть</strong> и <strong><span class="cn-word" data-tr="yozmoq">писа́ть</span></strong>.<br>
<span class="cn-word" data-tr="Nima uchun">Заче́м</span>? — <span class="cn-word" data-tr="Chunki">Потому́ что</span> я <strong>чита́ю</strong> ка́ждый день.</p>

<p>И́мя: Жасу́р. Класс: 9 «А».<br>
Что де́лать? — <strong>Игра́ть</strong>. <span class="cn-word" data-tr="Futbol">Футбо́л</span>.<br>
Заче́м? — Потому́ что я <strong>игра́ю</strong> хорошо́.</p>

<p>И́мя: Дилно́за. Класс: 9 «А».<br>
Что де́лать? — <strong><span class="cn-word" data-tr="rasm chizmoq">Рисова́ть</span></strong> и <strong><span class="cn-word" data-tr="qoʻshiq aytmoq">петь</span></strong>.<br>
Заче́м? — <strong>Не зна́ю</strong>. Про́сто хорошо́.</p>

<p>И <span class="cn-word" data-tr="yana bitta">ещё одна́</span> анке́та.</p>

<p>И́мя: Бекзо́д. Класс: — <span class="cn-word" data-tr="hali yoʻq">ещё нет</span>.<br>
Что де́лать? — <strong>Чита́ть</strong>, <strong>рисова́ть</strong>, <strong>игра́ть</strong>, <strong>петь</strong>. <span class="cn-word" data-tr="Hammasi">Всё</span>.<br>
Заче́м? — Потому́ что Афсо́на, Жасу́р и Дилно́за — <span class="cn-word" data-tr="u yerda">там</span>.</p>''',
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
                "explanation": "Bekzodning javobi: «Чита́ть, рисова́ть, игра́ть, петь. "
                               "Всё» — va sababi: «Потому́ что Афсо́на, Жасу́р и Дилно́за "
                               "— там». Uni toʻgarak emas, odamlar qiziqtiradi.",
            },
            {
                "text": "Nega anketadagi javoblar infinitivda (чита́ть, игра́ть) berilgan?",
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
                "text": "Matnda «я игра́ю хорошо́» bor. Nega «хоро́ший» emas?",
                "choices": [
                    "Chunki bu harakatni taʼriflaydi — demak ravish kerak",
                    "Chunki «я» erkak jinsida",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki «игра́ю» koʻplikda"
                ],
                "answer": 0,
                "explanation": "«Хорошо́» — ravish, u qanday oʻynashini aytadi. "
                               "«Хоро́ший» esa sifat va u otga kerak boʻlardi: "
                               "«хоро́ший футбо́л». Sifat otni, ravish harakatni "
                               "taʼriflaydi (PR-18).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-20 — I tuslanish                 KUNLIK TARTIB
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Оди́н день Жасу́ра",
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
                            "ishlaydi: чита́-ю, чита́-ешь, чита́-ет… Oʻzbekchadagi "
                            "oʻqi-y-man / oʻqi-y-san bilan bir xil tuzilma.",
                "examples": ["Я чита́ю.", "Он рабо́тает.", "Они́ гуля́ют."],
            },
            {
                "pattern":  "не + feʼl",
                "meaning":  "Inkor: НЕ har doim feʼlning OLDIDA turadi. Oʻzbekchada "
                            "inkor qoʻshimcha ichida boʻladi (bilma-y-man), ruschada esa "
                            "alohida soʻz sifatida oldinda.",
                "examples": ["Я не зна́ю.", "Он не понима́ет."],
            },
            {
                "pattern":  "Ravish + feʼl",
                "meaning":  "Ravish harakatni taʼriflaydi va oʻzgarmaydi: бы́стро, "
                            "ме́дленно, хорошо́, ча́сто. U odatda feʼldan oldin yoki "
                            "keyin turadi.",
                "examples": ["Он рабо́тает бы́стро.", "Мы ча́сто гуля́ем."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Ertalab">У́тро</span>. Жасу́р <span class="cn-word" data-pos="verb" data-tr="uygʻonadi">встаёт</span> <span class="cn-word" data-tr="erta">ра́но</span>. Бекзо́д <strong>ещё</strong> <span class="cn-word" data-pos="verb" data-tr="uxlaydi">спит</span>.</p>

<p>Жасу́р <strong>слу́шает</strong> <span class="cn-word" data-tr="radio">ра́дио</span> и <strong>де́лает</strong> <span class="cn-word" data-tr="nonushta">за́втрак</span>. Он <strong>де́лает</strong> э́то <span class="cn-word" data-tr="tez">бы́стро</span>, потому́ что уро́к <strong>уже́</strong> <span class="cn-word" data-tr="yaqin, tez orada">ско́ро</span>.</p>

<p>Шко́ла. Жасу́р <strong>чита́ет</strong>, <strong>слу́шает</strong>, <strong>ду́мает</strong>. Ру́сский язы́к — тру́дно. Мате́матика — легко́. Жасу́р <strong>понима́ет</strong> хорошо́, но ме́дленно.</p>

<p>Пото́м — футбо́л. Жасу́р <strong>игра́ет</strong> ка́ждый день. Шербе́к <strong>игра́ет</strong> то́же. Они́ <strong>игра́ют</strong> гро́мко и <span class="cn-word" data-tr="quvnoq">ве́село</span>.</p>

<p><span class="cn-word" data-tr="Kechqurun">Ве́чером</span> — <span class="cn-word" data-tr="doʻkon">магази́н</span>. Жасу́р <strong>рабо́тает</strong> <span class="cn-word" data-tr="oz">ма́ло</span>, два часа́. Ни́на Петро́вна <span class="cn-word" data-pos="verb" data-tr="deydi">говори́т</span>: «Жасу́р <strong>рабо́тает</strong> хорошо́».</p>

<p><span class="cn-word" data-tr="Kech">По́здно</span>. Дом. Бекзо́д <strong>не</strong> <span class="cn-word" data-pos="verb" data-tr="uxlaydi">спит</span>. Бекзо́д <strong>ждёт</strong>.</p>

<p>Бекзо́д: «Жасу́р, ты <strong>чита́ешь</strong>?»</p>

<p>Жасу́р <strong>ду́мает</strong>: у́тро — ра́но, шко́ла — тру́дно, футбо́л, магази́н. Он <span class="cn-word" data-tr="charchagan">уста́л</span>.</p>

<p>Жасу́р: «<strong>Чита́ю</strong>».</p>

<p>И они́ <strong>чита́ют</strong>. Ме́дленно, ти́хо. Ка́ждый день.</p>''',
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
                "explanation": "«Он уста́л» — charchagan. Lekin Bekzod kutib oʻtirgan edi "
                               "va Jasur «Чита́ю» dedi. Oxirgi jumla: «И они́ чита́ют. "
                               "Ме́дленно, ти́хо. Ка́ждый день» — bu har kungi odat.",
            },
            {
                "text": "Matnda «Они́ игра́ют» va «Жасу́р игра́ет» bor. Nega qoʻshimcha "
                        "boshqa?",
                "choices": [
                    "Chunki feʼl egaga moslashadi: они́ → -ют, он → -ет",
                    "Chunki bir joyda oʻtgan zamon",
                    "Chunki «Жасу́р» erkak jinsida",
                    "Bu xato"
                ],
                "answer": 0,
                "explanation": "I tuslanish qoʻshimchalari: -ю, -ешь, -ет, -ем, -ете, "
                               "-ют. 3-shaxs birlik uchun -ЕТ, koʻplik uchun -ЮТ. Bu "
                               "eng koʻp adashtiriladigan juftlik.",
            },
            {
                "text": "«Бекзо́д не спит» gapida НЕ qayerda turibdi va nega?",
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
