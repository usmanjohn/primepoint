# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-38 … PR-40.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 38 — hikoya (qish), 39 — retsept, 40 — intervyu.
(35 xat, 36 ilmiy-ommabop, 37 sinf sahnasi edi.)

⚠️ SARLAVHA TUZATILDI. Toc'da «Как де́лают самса́» yozilgan edi — bu
grammatik jihatdan notoʻgʻri: де́лают feʼli Вини́тельный talab qiladi,
demak «самсу́». Grammatika kursida sarlavhaning oʻzi xato boʻlishi mumkin
emas, shuning uchun «Как де́лают самсу́» qilindi.

Uzviylik: 38-matn PR-35 dagi «Письмо́ из Сиби́ри» ning davomi — oʻsha
Sherbek, oʻsha Sibir, endi uning birinchi qishi. Oʻquvchi tanish odamni
qayta uchratadi.

Grammatika chegarasi (kumulyativ qoida):
  38-matn: Д.п. — мне хо́лодно, yosh, К va ПО predloglari.
  39-matn: Т.п. — asbob (predlogsiz: ножо́м, рука́ми) va hamroh (С bilan).
           Matnning butun mazmuni aynan shu farq ustiga qurilgan.
  40-matn: Т.п. — кем стать / рабо́тать. Oxirgi jumla hozirgi zamondagi
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
        "title":   "Пе́рвая зима́",
        "summary": (
            "PR-38 matni. «Письмо́ из Сиби́ри» ning davomi: Sherbekning Sibirdagi "
            "birinchi qishi. Minus oʻttiz, sotuvchi ayolning maslahati va "
            "hayotdagi birinchi marta yoqqan qish."
        ),
        "order":   38,
        "grammar": [
            {
                "pattern":  "Мне хо́лодно — holat",
                "meaning":  "Shaxssiz gap: ega yoʻq, olmosh Да́тельный'da. Oʻzbekcha "
                            "«menga sovuq» ning aynan oʻzi. Oʻtgan zamonda «бы́ло» — "
                            "har doim oʻrta jinsda.",
                "examples": ["Ему́ хо́лодно.", "Ему́ бы́ло хо́лодно."],
            },
            {
                "pattern":  "Yosh — Да́тельный bilan",
                "meaning":  "Rus tilida yosh «menga ... yil» shaklida aytiladi: Мне "
                            "два́дцать четы́ре го́да. Oʻzbekchada esa «men ... "
                            "yoshdaman» — ega bor. Ikkalasi ham gʻalati, lekin "
                            "boshqacha gʻalati.",
                "examples": ["Мне два́дцать четы́ре го́да."],
            },
            {
                "pattern":  "К va ПО + Да́тельный",
                "meaning":  "К — odam yoki narsa TOMON (к магази́ну). ПО — boʻylab "
                            "(по у́лице, по го́роду). Diqqat: joyga kirish uchun В "
                            "ishlatiladi, К emas.",
                "examples": ["Он идёт к магази́ну.", "Он идёт по у́лице."],
            },
        ],
        "body": '''<p>Шербек из Ташке́нта. Тепе́рь он живёт в Сиби́ри. Э́то его́ пе́рвая <span class="cn-word" data-tr="qish">зима́</span>.</p>

<p>В Ташке́нте зимо́й тоже хо́лодно. Но здесь друго́й хо́лод.</p>

<p>Пе́рвый день. <span class="cn-word" data-tr="minus oʻttiz">Ми́нус три́дцать</span>.</p>

<p><strong>Ему́</strong> хо́лодно. <strong>Ему́</strong> хо́лодно утром, днём и ве́чером.</p>

<p>Он идёт <strong>по</strong> у́лице ме́дленно. Он идёт <strong>к</strong> магази́ну.</p>

<p>В магази́не <strong>ему́</strong> тепло́. Он не хо́чет идти́ домо́й.</p>

<p><span class="cn-word" data-tr="sotuvchi ayol">Продавщи́ца</span> смо́трит и говори́т:</p>

<p>— Вы с ю́га?</p>

<p>— Да. Из Ташке́нта.</p>

<p>— <span class="cn-word" data-tr="Sizga ... kerak">Вам ну́жен</span> <span class="cn-word" data-tr="sharf">шарф</span>, — говори́т она́. — И <span class="cn-word" data-tr="qalpoq">ша́пка</span>. И <span class="cn-word" data-tr="qoʻlqoplar">рукави́цы</span>.</p>

<p>Шербек покупа́ет всё.</p>

<p><span class="cn-word" data-tr="Bir oydan keyin">Че́рез ме́сяц</span> он идёт <strong>по</strong> го́роду — и <strong>ему́</strong> не хо́лодно.</p>

<p>Он идёт <strong>к</strong> о́зеру. Там бе́лый лёд и <span class="cn-word" data-tr="quyosh">со́лнце</span>.</p>

<p>Ве́чером он пи́шет Афсо́не:</p>

<p>«<strong>Мне</strong> два́дцать четы́ре го́да. И зима́ <strong>мне</strong> нра́вится. Пе́рвый раз <span class="cn-word" data-tr="hayotda">в жи́зни</span>».</p>''',
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
                "explanation": "«В магази́не ему́ тепло́. Он не хо́чет идти́ домо́й» — "
                               "shundan keyin darrov sotuvchining savoli keladi: «Вы с "
                               "ю́га?». Sovuqqa oʻrganmagan odam koʻrinib turadi.",
            },
            {
                "text": "«Ему́ хо́лодно» va «Мне два́дцать четы́ре го́да» — bu ikki "
                        "gapda nima umumiy?",
                "choices": [
                    "Ikkalasida ham ega yoʻq va olmosh Да́тельный padejida",
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
                "explanation": "«И зима́ мне нра́вится. Пе́рвый раз в жи́зни». Matn "
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
        "title":   "Как де́лают самсу́",
        "summary": (
            "PR-39 matni. Samsa retsepti — xamir, goʻsht, piyoz. Har bir qadamda "
            "asbob koʻrsatiladi (ножо́м, рука́ми), va oxirida buvi eng muhim "
            "«bilan» ni aytadi."
        ),
        "order":   39,
        "grammar": [
            {
                "pattern":  "Asbob — predlogsiz",
                "meaning":  "«Nima bilan?» degan savolga javob predlogSIZ beriladi: "
                            "ре́зать ножо́м, де́лать рука́ми. Oʻzbekcha «bilan» bu "
                            "yerda ruschada hech qanday soʻz bilan tarjima qilinmaydi "
                            "— faqat qoʻshimcha.",
                "examples": ["Лук ре́жут ножо́м.", "Те́сто де́лают рука́ми."],
            },
            {
                "pattern":  "Hamroh va qoʻshimcha — С bilan",
                "meaning":  "«Kim bilan?» yoki «nima qoʻshib?» — С predlogi bilan: "
                            "с со́лью, с людьми́. Bu yerda predlog SHART.",
                "examples": ["Мя́со с со́лью и с пе́рцем.", "Самсу́ де́лают с людьми́."],
            },
            {
                "pattern":  "Qoʻshimchalar: -ом/-ем · -ой/-ей",
                "meaning":  "Erkak va oʻrta jins -ОМ/-ЕМ (ножо́м, пе́рцем), ayol jinsi "
                            "-ОЙ/-ЕЙ (ло́жкой). Ayol jinsidagi -Ь otlari -ЬЮ oladi: "
                            "соль → со́лью.",
                "examples": ["Ло́жкой. Ножо́м. Со́лью."],
            },
        ],
        "body": '''<p>Самса́ — э́то <span class="cn-word" data-tr="xamir">те́сто</span> и <span class="cn-word" data-tr="goʻsht">мя́со</span>. И ещё лук. Мно́го лу́ка.</p>

<p>Снача́ла де́лают те́сто. <span class="cn-word" data-tr="un">Мука́</span>, вода́, <span class="cn-word" data-tr="tuz">соль</span>. Всё.</p>

<p>Те́сто де́лают <strong>рука́ми</strong>. Не маши́ной. <strong>Рука́ми</strong> <span class="cn-word" data-tr="yaxshiroq">лу́чше</span>.</p>

<p>Пото́м лук. Лук <span class="cn-word" data-pos="verb" data-tr="kesishadi">ре́жут</span> <strong>ножо́м</strong>. <span class="cn-word" data-tr="mayda">Ме́лко</span>.</p>

<p>Мя́со тоже ре́жут <strong>ножо́м</strong>. Не маши́ной! Э́то ва́жно.</p>

<p>Пото́м мя́со и лук <strong>с</strong> со́лью и <strong>с</strong> <span class="cn-word" data-tr="qalampir">пе́рцем</span>.</p>

<p>Самсу́ де́лают <strong>рука́ми</strong>. Одна́ самса́ — одна́ мину́та.</p>

<p>Пото́м <span class="cn-word" data-tr="tandir">танды́р</span>. И́ли <span class="cn-word" data-tr="duxovka">духо́вка</span>. Два́дцать мину́т.</p>

<p>Бабушка говори́т так:</p>

<p>— Нож — э́то не гла́вное. Танды́р — тоже не гла́вное.</p>

<p>— А что гла́вное? — спра́шивает Бекзод.</p>

<p>— Лю́ди, — говори́т бабушка. — Самсу́ де́лают <strong>с людьми́</strong>. Оди́н челове́к и одна́ самса́ — э́то не пра́здник. Э́то про́сто <span class="cn-word" data-tr="ovqat">еда́</span>.</p>''',
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
                "explanation": "«Нож — э́то не гла́вное. Танды́р — тоже не гла́вное… "
                               "Лю́ди». Buvi asbobdan odamga oʻtadi: «Оди́н челове́к и "
                               "одна́ самса́ — э́то не пра́здник».",
            },
            {
                "text": "Nega matnda «ножо́м», lekin «с со́лью»?",
                "choices": [
                    "Pichoq — asbob (predlogsiz), tuz esa qoʻshiladigan narsa (С bilan)",
                    "Chunki «нож» erkak jinsida",
                    "Chunki tuz sanalmaydi",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Ikkalasi ham Твори́тельный padejida. Farqni predlog "
                               "qiladi: asbob qoʻlingizda — predlog qoʻyilmaydi; nimadir "
                               "qoʻshilsa yoki kimdir hamroh boʻlsa — С qoʻyiladi. "
                               "Oʻzbekcha «bilan» ikkalasini ham qoplaydi.",
            },
            {
                "text": "Oxirgi jumladagi «с людьми́» nega darsning eng yaxshi "
                        "misoli?",
                "choices": [
                    "Chunki bu matndagi yagona haqiqiy hamroh — qolgani asbob",
                    "Chunki bu koʻplik shakli",
                    "Chunki odamlarni sanash mumkin emas",
                    "Chunki bu buvining gapi"
                ],
                "answer": 0,
                "explanation": "Butun matn boʻyi asboblar sanaladi — рука́ми, ножо́м — "
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
        "title":   "Кем ты хо́чешь стать?",
        "summary": (
            "PR-40 matni. Jurnalist Nina maktabga qaytadi va bitta savol beradi. "
            "Javoblar oddiy — Jasurniki bundan mustasno, va u nega bobosidan "
            "boshqa yoʻlni tanlaganini tushuntiradi."
        ),
        "order":   40,
        "grammar": [
            {
                "pattern":  "стать / рабо́тать + Твори́тельный",
                "meaning":  "«Kim boʻlib?» degan savolga javob: хочу́ стать врачо́м, "
                            "рабо́тает стро́ителем. Oʻzbekchada bu «boʻlib» soʻzi "
                            "bilan beriladi.",
                "examples": ["Я хочу́ стать врачо́м.", "Оте́ц рабо́тает стро́ителем."],
            },
            {
                "pattern":  "Feʼl bor — Т.п., feʼl yoʻq — bosh kelishik",
                "meaning":  "Hozirgi zamonda «быть» aytilmaydi, shuning uchun kasb "
                            "bosh kelishikda qoladi: Я учени́к. Oʻtgan va kelasi "
                            "zamonda feʼl paydo boʻladi va u bilan Т.п. keladi.",
                "examples": ["Сейча́с я учени́к.", "Дед был стро́ителем."],
            },
            {
                "pattern":  "кто → кем",
                "meaning":  "Savol soʻzining oʻzi ham kelishikka kiradi. «Кем ты "
                            "хо́чешь стать?» — rus maktablarida har yili beriladigan "
                            "savol.",
                "examples": ["Кем ты хо́чешь стать?"],
            },
        ],
        "body": '''<p>Ни́на де́лает <span class="cn-word" data-tr="intervyu">интервью́</span> в школе. Оди́н <span class="cn-word" data-tr="savol">вопро́с</span>: «<strong>Кем</strong> ты хо́чешь <strong>стать</strong>?»</p>

<p>Афсона: «Я хочу́ <strong>стать врачо́м</strong>. Моя́ мама рабо́тает <strong>врачо́м</strong>».</p>

<p>Бекзод: «Я хочу́ <strong>стать футболи́стом</strong>».</p>

<p>Катя: «Я не зна́ю. <span class="cn-word" data-tr="Balki">Мо́жет быть</span>, <strong>учи́телем</strong>».</p>

<p>Жасур молчи́т.</p>

<p>— А ты? — спра́шивает Ни́на.</p>

<p>— Мой <span class="cn-word" data-tr="bobo">дед</span> был <strong>стро́ителем</strong>, — говори́т Жасур. — Мой оте́ц рабо́тает <strong>стро́ителем</strong>.</p>

<p>— И ты бу́дешь <strong>стро́ителем</strong>?</p>

<p>— Нет. Я хочу́ <strong>стать архите́ктором</strong>.</p>

<p>Ни́на <span class="cn-word" data-pos="verb" data-tr="hayron boʻladi">удивля́ется</span>.</p>

<p>— Э́то <span class="cn-word" data-tr="deyarli bir xil narsa">почти́ одно́ и то же</span>, — говори́т она́.</p>

<p>— Нет, — говори́т Жасур. — Дед <span class="cn-word" data-pos="verb" data-tr="qurgan">стро́ил</span> <strong>рука́ми</strong>. Оте́ц тоже. А я хочу́ стро́ить <strong>голово́й</strong>. Пото́м <strong>рука́ми</strong> — но уже́ <strong>с</strong> <span class="cn-word" data-tr="reja">пла́ном</span>.</p>

<p>Ни́на <span class="cn-word" data-pos="verb" data-tr="yozib oladi">запи́сывает</span>. Пото́м спра́шивает:</p>

<p>— А кто ты сейча́с?</p>

<p>— Сейча́с я <strong>учени́к</strong>, — говори́т Жасур.</p>

<p>И э́то <span class="cn-word" data-tr="toʻgʻri">пра́вильно</span>. Сейча́с — <strong>учени́к</strong>. Пото́м — <strong>архите́ктором</strong>.</p>''',
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
                "explanation": "«Дед стро́ил рука́ми. Оте́ц тоже. А я хочу́ стро́ить "
                               "голово́й. Пото́м рука́ми — но уже́ с пла́ном». U "
                               "oilasidan voz kechmayapti — oʻsha ishga boshqa "
                               "tomondan kirmoqchi.",
            },
            {
                "text": "«Сейча́с я учени́к» — nega bu yerda «учеником» emas?",
                "choices": [
                    "Hozirgi zamonda «быть» aytilmaydi, demak kelishik ham kerak emas",
                    "Chunki «учени́к» erkak jinsida",
                    "Chunki bu savolga javob",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Qoida: feʼl bor boʻlsa — Твори́тельный, feʼl yoʻq "
                               "boʻlsa — bosh kelishik. Shuning uchun oxirgi jumla ikki "
                               "shaklni yonma-yon qoʻyadi: «Сейча́с — учени́к. Пото́м — "
                               "архите́ктором».",
            },
            {
                "text": "Matnda «рука́ми» ham, «с пла́ном» ham bor. Nega biri "
                        "predlogsiz?",
                "choices": [
                    "Qoʻl — asbob (predlogsiz), reja esa qoʻshimcha narsa (С bilan)",
                    "Chunki «ру́ки» koʻplikda",
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
