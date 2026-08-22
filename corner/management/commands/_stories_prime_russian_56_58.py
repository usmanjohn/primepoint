# -*- coding: utf-8 -*-
"""Prime Russian Readings — PR-56 … PR-58.

Toc: corner/management/commands/toc_prime_russian_readings.txt
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

Janr xilma-xilligi: 56 — sayohat qaydlari, 57 — ilmiy-ommabop,
58 — hikoya. (53 uchta xat, 54 biografik, 55 kundalik yoʻl edi.)

⚠️ SARLAVHA TUZATILDI (58). Toc'da «Кот, кото́рый ушёл и пришёл» yozilgan
edi, lekin КОТО́РЫЙ PR-63 da oʻrgatiladi. Kumulyativ qoidaga koʻra
oʻrgatilmagan qurilish sarlavhada boʻlishi mumkin emas, shuning uchun
«Кот ушёл и пришёл» qilindi — maʼnosi bir xil, grammatikasi toza.

⚠️ FAKTLAR (56-matn). Transsibir temir yoʻli haqidagi daʼvolar
tekshirilgan va ehtiyotkorlik bilan tanlangan: Moskva—Vladivostok yoʻli
taxminan yetti kun davom etadi; Vladivostok Moskvadan yetti soat oldinda;
yoʻl Baykal koʻlining janubiy qirgʻogʻi boʻylab oʻtadi; yoʻl oxirida
Tinch okeani. Aniq kilometr raqami ATAY aytilmagan — manbalarda u biroz
har xil.

Grammatika chegarasi (kumulyativ qoida):
  56-matn: е́хать ↔ е́здить, лете́ть ↔ лета́ть, нести́ ↔ носи́ть.
           PREFIKSLI harakat feʼllari YOʻQ — ular PR-57 da.
  57-matn: prefikslar roʻyxati. Matn shakli — roʻyxat, chunki mavzu ham
           roʻyxat.
  58-matn: prefikslar hikoyada. Mushuk ketadi va qaytadi; ушёл/пришёл
           (СВ, bir marta) va уходи́л/приходи́л (НСВ, odat) yonma-yon.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_russian_56_58.py --author=prime
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
    # PR-56 — harakat juftliklari               SAYOHAT QAYDLARI
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Тра́нссиб: семь дней в по́езде",
        "summary": (
            "PR-56 matni. Moskvadan Vladivostokgacha yetti kun. Deraza ortida "
            "oʻrmon, keyin yana oʻrmon — va yoʻl oxirida okean. Hamsafarning "
            "bir jumlasi butun sayohatni tushuntiradi."
        ),
        "order":   56,
        "grammar": [
            {
                "pattern":  "е́хал — bir tomonga",
                "meaning":  "Yetti kun davomida bir tomonga ketish — bu ЕХАТЬ. "
                            "Oʻzbekcha «ketayotgan edim». Agar «ЕЗДИЛ» boʻlsa, borib "
                            "qaytish maʼnosi chiqardi.",
                "examples": ["Я е́хал семь дней.", "По́езд шёл на восто́к."],
            },
            {
                "pattern":  "лета́л — muntazam",
                "meaning":  "ЛЕТА́ТЬ — koʻp marta, muntazam: «Он лета́л в Москву́ "
                            "мно́го раз». Bir marta, hozir uchayotgan boʻlsa — "
                            "ЛЕТИ́Т.",
                "examples": ["Мой сосе́д лета́л в Москву́ мно́го раз."],
            },
            {
                "pattern":  "носи́л — muntazam olib yurish",
                "meaning":  "НОСИ́ТЬ — takroriy: proyezdnik har soatda choy olib "
                            "keladi. Bir marta olib ketayotgan boʻlsa — НЁС.",
                "examples": ["Проводни́к носи́л чай ка́ждый час."],
            },
        ],
        "body": '''<p>Тра́нссиб — дли́нная <span class="cn-word" data-tr="temir yoʻl">желе́зная доро́га</span>. О́чень дли́нная.</p>

<p>Москва́ — Владивосто́к. Семь дней в по́езде.</p>

<p>Я <strong>е́хал</strong> семь дней. Ка́ждый день по́езд <strong>шёл</strong> на <span class="cn-word" data-tr="sharq">восто́к</span>.</p>

<p>За окно́м — <span class="cn-word" data-tr="oʻrmon">лес</span>. Пото́м <span class="cn-word" data-tr="yana">опя́ть</span> лес. Пото́м сно́ва лес.</p>

<p>На тре́тий день — Байка́л. По́езд <strong>шёл</strong> <span class="cn-word" data-tr="boʻylab">вдоль</span> о́зера до́лго. Вода́ была́ <span class="cn-word" data-tr="quyuq koʻk">тёмно-си́няя</span>.</p>

<p><span class="cn-word" data-tr="vagon xodimi">Проводни́к</span> <strong>носи́л</strong> чай ка́ждый час. Э́то его́ рабо́та.</p>

<p>Мой сосе́д <strong>лета́л</strong> в Москву́ мно́го раз. Но <span class="cn-word" data-tr="poyezdda">по́ездом</span> — пе́рвый раз.</p>

<p>— Самолёт бы́стро, — говори́т он. — Но самолёт не пока́зывает страну́. А по́езд пока́зывает.</p>

<p>Семь дней. Семь <span class="cn-word" data-tr="soat mintaqalari">часовы́х поясо́в</span>. Владивосто́к <span class="cn-word" data-tr="oldinda">впереди́</span> Москвы́ на семь часо́в.</p>

<p>В <span class="cn-word" data-tr="oxirida">конце́</span> пути́ — мо́ре. Ти́хий океа́н.</p>

<p>Я <strong>е́хал</strong> семь дней. Тепе́рь я зна́ю: страна́ о́чень больша́я.</p>''',
        "questions": [
            {
                "text": "Hamsafar samolyot va poyezdni qanday taqqoslaydi?",
                "choices": [
                    "Samolyot tez, lekin poyezd mamlakatni koʻrsatadi",
                    "Poyezd tezroq va arzonroq",
                    "Samolyotda ovqat yaxshiroq",
                    "Ikkalasi bir xil"
                ],
                "answer": 0,
                "explanation": "«Самолёт бы́стро… Но самолёт не пока́зывает страну́. "
                               "А по́езд пока́зывает». Matnning oxirgi jumlasi ham shu "
                               "fikrni tasdiqlaydi: «Тепе́рь я зна́ю: страна́ о́чень "
                               "больша́я».",
            },
            {
                "text": "Nega matnda «я е́хал», «я е́здил» emas?",
                "choices": [
                    "Yetti kun bir tomonga ketildi — borib qaytish emas",
                    "Chunki poyezdda ketildi",
                    "Chunki bu uzoq yoʻl",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "Е́хал — bir tomonga, jarayon. Е́здил «borib keldim» "
                               "degan boʻlardi, lekin matnda faqat Moskvadan "
                               "Vladivostokgacha boriladi.",
            },
            {
                "text": "«Проводни́к носи́л чай ка́ждый час» — nega НОСИ́Л?",
                "choices": [
                    "«Ка́ждый час» takrorni bildiradi — muntazam harakat",
                    "Chunki choy ogʻir edi",
                    "Chunki u bir marta olib keldi",
                    "Chunki bu oʻtgan zamon"
                ],
                "answer": 0,
                "explanation": "НЕСТИ́ — bir marta, hozir olib ketish. НОСИ́ТЬ — "
                               "muntazam, takroriy. «Ка́ждый час» ikkinchisini "
                               "talab qiladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-57 — prefikslar                        ILMIY-OMMABOP
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Оди́н глаго́л, де́сять двере́й",
        "summary": (
            "PR-57 matni. Bitta feʼl — идти́ — va oʻnta prefiks. Har biri boshqa "
            "eshikni ochadi. Oxirida bitta soʻzning ichidan kutilmagan maʼno "
            "chiqadi."
        ),
        "order":   57,
        "grammar": [
            {
                "pattern":  "Prefiks yoʻnalishni bildiradi",
                "meaning":  "ПРИ- kelmoq, У- ketmoq, В- kirmoq, ВЫ- chiqmoq, ДО- "
                            "yetib bormoq, ПЕРЕ- kesib oʻtmoq, ПОД- yaqinlashmoq, "
                            "ОТ- uzoqlashmoq. Bitta oʻzak, sakkizta maʼno.",
                "examples": ["Прийти́ — быть здесь.", "Уйти́ — не быть здесь."],
            },
            {
                "pattern":  "идти́ → СВ, ходи́ть → НСВ",
                "meaning":  "Prefiks ИДТИ ga qoʻshilsa СВ chiqadi (прийти́), ХОДИТЬ "
                            "ga qoʻshilsa НСВ (приходи́ть). Vid va harakat tizimi shu "
                            "yerda birlashadi.",
                "examples": ["прийти́ ↔ приходи́ть"],
            },
            {
                "pattern":  "найти́ = на + идти́",
                "meaning":  "«Topmoq» soʻzi aslida «yurib borib ustiga tushmoq» "
                            "degani. Shuning uchun u ИДТИ kabi turlanadi: найду́, "
                            "нашёл, нашла́.",
                "examples": ["Найти́ — идти́ и уви́деть."],
            },
        ],
        "body": '''<p>Оди́н <span class="cn-word" data-tr="feʼl">глаго́л</span>: <strong>идти́</strong>.</p>

<p>Тепе́рь <span class="cn-word" data-tr="prefiks">приста́вка</span> — и глаго́л <span class="cn-word" data-pos="verb" data-tr="oʻzgaradi">меня́ется</span>.</p>

<p><strong>Прийти́</strong> — быть здесь.</p>

<p><strong>Уйти́</strong> — не быть здесь.</p>

<p><strong>Войти́</strong> — быть <span class="cn-word" data-tr="ichida">внутри́</span>.</p>

<p><strong>Вы́йти</strong> — быть на у́лице.</p>

<p><strong>Подойти́</strong> — быть <span class="cn-word" data-tr="yaqin">бли́зко</span>.</p>

<p><strong>Отойти́</strong> — быть далеко́.</p>

<p><strong>Перейти́</strong> — быть на друго́й <span class="cn-word" data-tr="tomon">стороне́</span>.</p>

<p><strong>Дойти́</strong> — быть в конце́ доро́ги.</p>

<p>Оди́н <span class="cn-word" data-tr="oʻzak">ко́рень</span>. Во́семь <span class="cn-word" data-tr="eshiklar">двере́й</span>. И э́то ещё не всё.</p>

<p>Есть <strong>зайти́</strong> — быть недо́лго. Есть <strong>пройти́</strong> — быть да́льше. Есть <strong>пойти́</strong> — на́чать идти́.</p>

<p>И есть <strong>найти́</strong>.</p>

<p><strong>Найти́</strong> — э́то «на» плюс «идти́». Идти́ — и <span class="cn-word" data-pos="verb" data-tr="uchratmoq">встре́тить</span>.</p>

<p>Поэ́тому в ру́сском языке́ «найти́» зна́чит: ты шёл, шёл — и вот оно́.</p>

<p>В узбе́кском языке́ для ка́ждой две́ри есть <span class="cn-word" data-tr="alohida">отде́льное</span> сло́во.</p>

<p>В ру́сском языке́ дверь одна́ — э́то глаго́л. А приста́вки — э́то <span class="cn-word" data-tr="kalitlar">ключи́</span>.</p>

<p>Оди́н глаго́л. Де́сять ключе́й. Де́сять двере́й.</p>''',
        "questions": [
            {
                "text": "«Найти́» soʻzi qanday tuzilgan va bu nimani anglatadi?",
                "choices": [
                    "На + идти́ — yurib borib ustiga tushmoq",
                    "На + йти — yangi soʻz, tuzilishi yoʻq",
                    "Най + ти — qadimiy oʻzak",
                    "Bu boshqa feʼllardan olingan"
                ],
                "answer": 0,
                "explanation": "«Найти́ — э́то „на“ плюс „идти́“… ты шёл, шёл — и вот "
                               "оно́». Shuning uchun u ИДТИ kabi turlanadi: найду́, "
                               "нашёл, нашла́.",
            },
            {
                "text": "Matnga koʻra rus va oʻzbek tillari bu yerda qanday farq "
                        "qiladi?",
                "choices": [
                    "Oʻzbekchada har bir maʼno uchun alohida soʻz, ruschada bitta oʻzak va prefikslar",
                    "Oʻzbekchada prefikslar koʻproq",
                    "Ruschada har bir maʼno uchun alohida soʻz",
                    "Farqi yoʻq"
                ],
                "answer": 0,
                "explanation": "«В узбе́кском языке́ для ка́ждой две́ри есть "
                               "отде́льное сло́во. В ру́сском языке́ дверь одна́ — "
                               "э́то глаго́л. А приста́вки — э́то ключи́».",
            },
            {
                "text": "Matnning sarlavhasi nima uchun shunday tanlangan?",
                "choices": [
                    "Feʼl — eshik, prefikslar esa kalitlar: bitta eshik, oʻnta kalit",
                    "Chunki matnda oʻnta xona haqida gapiriladi",
                    "Chunki rus tilida oʻnta feʼl bor",
                    "Bu shunchaki chiroyli nom"
                ],
                "answer": 0,
                "explanation": "Matn oxirgi ikki jumlada obrazni ochadi: «дверь одна́ "
                               "— э́то глаго́л. А приста́вки — э́то ключи́. Оди́н "
                               "глаго́л. Де́сять ключе́й. Де́сять двере́й».",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PR-58 — prefikslar hikoyada               HIKOYA
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Кот ушёл и пришёл",
        "summary": (
            "PR-58 matni. Ryzhik chorshanba kuni ketdi va toʻrt kun qaytmadi. "
            "Butun oila uni qidirdi — buvidan boshqa hamma. Buvining aytgani "
            "toʻgʻri chiqdi."
        ),
        "order":   58,
        "grammar": [
            {
                "pattern":  "ушёл / пришёл — bir marta",
                "meaning":  "Prefiks + ИДТИ = СВ: bir marta tugagan harakat. «В "
                            "сре́ду он ушёл» — aniq bir kuni, aniq bir voqea.",
                "examples": ["В сре́ду ве́чером он ушёл.", "Но он не пришёл."],
            },
            {
                "pattern":  "уходи́л / приходи́л — odat",
                "meaning":  "Prefiks + ХОДИТЬ = НСВ: takroriy harakat. «Он уходи́л "
                            "ка́ждый день и приходи́л» — bu uning odati edi.",
                "examples": ["Он уходи́л ка́ждый день — и приходи́л."],
            },
            {
                "pattern":  "подошёл · вы́шел · сошёл",
                "meaning":  "ПОД- yaqinlashmoq, ВЫ- chiqmoq, С- pastga tushmoq. "
                            "Har bir prefiks harakatning yoʻnalishini aniq "
                            "koʻrsatadi.",
                "examples": ["Он подошёл к две́ри.", "Он сошёл вниз ме́дленно."],
            },
        ],
        "body": '''<p>У нас есть кот. Его́ зову́т <span class="cn-word" data-tr="Ryzhik (sarigʻ ism)">Ры́жик</span>.</p>

<p>В <span class="cn-word" data-tr="chorshanba">сре́ду</span> ве́чером он <strong>ушёл</strong>.</p>

<p>Снача́ла он <strong>подошёл</strong> к две́ри. Пото́м <strong>вы́шел</strong> во <span class="cn-word" data-tr="hovli">двор</span>. Пото́м — <span class="cn-word" data-tr="hech narsa">ничего́</span>.</p>

<p>Мы ду́мали: он <strong>зайдёт</strong> <span class="cn-word" data-tr="bir soatdan keyin">че́рез час</span>.</p>

<p>Но он не <strong>пришёл</strong>.</p>

<p>В <span class="cn-word" data-tr="payshanba">четве́рг</span> мы <span class="cn-word" data-pos="verb" data-tr="qidirdik">иска́ли</span> его́ во дворе́. В пя́тницу Бекзод <strong>перешёл</strong> у́лицу и <strong>дошёл</strong> до ры́нка. Ры́жика нет.</p>

<p>В суббо́ту ба́бушка сказа́ла:</p>

<p>— Он <strong>придёт</strong>. <span class="cn-word" data-tr="Mushuklar">Ко́шки</span> всегда́ <strong>прихо́дят</strong>.</p>

<p>В воскресе́нье у́тром я <strong>вы́шел</strong> во двор.</p>

<p>Ры́жик сиде́л на <span class="cn-word" data-tr="tom">кры́ше</span> и смотре́л на меня́.</p>

<p>Он <strong>сошёл</strong> вниз ме́дленно. Пото́м <strong>подошёл</strong> и <span class="cn-word" data-pos="verb" data-tr="oʻtirdi">сел</span> ря́дом. <span class="cn-word" data-tr="Xuddi">Как бу́дто</span> ничего́ не бы́ло.</p>

<p>Ры́жик <strong>уходи́л</strong> ка́ждый день — и ка́ждый день <strong>приходи́л</strong>.</p>

<p>То́лько в э́тот раз он <strong>ушёл</strong> на четы́ре дня.</p>

<p>Ба́бушка была́ <span class="cn-word" data-tr="haqli">права́</span>.</p>''',
        "questions": [
            {
                "text": "Ryzhik qayerdan qaytdi?",
                "choices": [
                    "Tomdan tushdi — hovlida edi",
                    "Bozordan keldi",
                    "Qoʻshnilarnikidan",
                    "Matnda aytilmagan"
                ],
                "answer": 0,
                "explanation": "«Ры́жик сиде́л на кры́ше и смотре́л на меня́. Он "
                               "сошёл вниз ме́дленно». Toʻrt kun qidirilgan mushuk "
                               "aslida yaqin joyda ekan.",
            },
            {
                "text": "«Он ушёл» va «он уходи́л» — nima farq qiladi?",
                "choices": [
                    "Ушёл — bir marta, aniq voqea; уходи́л — har kungi odat",
                    "Ушёл — hozirgi zamon",
                    "Уходи́л — kelasi zamon",
                    "Ikkalasi bir xil"
                ],
                "answer": 0,
                "explanation": "Prefiks + ИДТИ = СВ (bir marta), prefiks + ХОДИТЬ = "
                               "НСВ (takror). Matn ikkalasini yonma-yon qoʻyadi: har "
                               "kuni ketardi va qaytardi — bu safar esa toʻrt kunga "
                               "ketdi.",
            },
            {
                "text": "Nega matnda «подошёл», «вы́шел», «сошёл» — har xil "
                        "prefikslar?",
                "choices": [
                    "Har bir prefiks harakatning boshqa yoʻnalishini koʻrsatadi",
                    "Chunki ular har xil feʼllar",
                    "Chunki ular har xil zamonda",
                    "Bu matndagi xato"
                ],
                "answer": 0,
                "explanation": "ПОД- yaqinlashish (eshik oldiga keldi), ВЫ- chiqish "
                               "(hovliga chiqdi), С- pastga tushish (tomdan tushdi). "
                               "Bitta oʻzak — uchta aniq yoʻnalish.",
            },
        ],
    },
]
