# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-89 … PR-91.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_89_91.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Russian",
    "description": "Rus tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#b91c1c",
}

DEFAULTS = {
    "level":                "hard",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PR-89 — Soʻz tartibi va maʼno urgʻusi
# =====================================================================

Q_PR89 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rus gapida eng muhim, yangi maʼlumot "
                "qayerda turadi?</p>",
        "choices": ["Gap boshida", "Feʼldan darrov oldin", "Gap oxirida", "Egadan keyin"],
        "correct": "Gap oxirida",
        "explanation": "<p>Rus tilida <strong>tanish narsa boshida, yangi narsa "
                       "oxirida</strong> turadi. Oʻzbekchada esa urgʻuli soʻz feʼldan oldin "
                       "keladi — instinkt bir xil, manzil boshqa.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rus tilida soʻz tartibi haqida qaysi gap "
                "toʻgʻri?</p>",
        "choices": [
            "Grammatik jihatdan erkin, lekin har bir tartib boshqa maʼno beradi",
            "Tartib qatʼiy: ega — kesim — toʻldiruvchi",
            "Tartib faqat sheʼrda oʻzgaradi",
            "Tartib toʻliq erkin — maʼno hech qachon oʻzgarmaydi",
        ],
        "correct": "Grammatik jihatdan erkin, lekin har bir tartib boshqa maʼno beradi",
        "explanation": "<p>Qanday tuzsangiz ham <strong>xato boʻlmaydi</strong>, lekin har "
                       "bir tartib <strong>boshqa savolga</strong> javob beradi. Tartib "
                       "grammatikaga emas, maʼnoga xizmat qiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Не</strong> qaysi soʻzni inkor "
                "qiladi?</p>",
        "choices": [
            "Oʻzidan keyingi soʻzni",
            "Oʻzidan oldingi soʻzni",
            "Gapdagi egani",
            "Gapdagi feʼlni, qayerda turishidan qatʼi nazar",
        ],
        "correct": "Oʻzidan keyingi soʻzni",
        "explanation": "<p><em>Я <strong>не</strong> говори́л</em> — «aytmadim»; "
                       "<em><strong>Не</strong> я говори́л</em> — «men emas». <em>Не</em> ni "
                       "koʻchirsangiz, gapning maʼnosi butunlay oʻzgaradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rus tilida artikl (<em>the / a</em>) yoʻq."
                " Uning vazifasini nima bajaradi?</p>",
        "choices": ["Kelishik", "Feʼl turi", "Soʻz tartibi", "Urgʻu belgisi"],
        "correct": "Soʻz tartibi",
        "explanation": "<p><em>Пришёл ма́льчик</em> — «bir bola keldi» (yangi); <em>Ма́льчик "
                       "пришёл</em> — «oʻsha bola keldi» (tanish). Oʻzbek tilida ham aynan "
                       "shunday hal qilinadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi qurilish <strong>erkin emas</strong>"
                " — hech qachon ajralmaydi?</p>",
        "choices": [
            "Predlog va undan keyingi ot",
            "Hol va feʼl",
            "Toʻldiruvchi va feʼl",
            "Ega va kesim",
        ],
        "correct": "Predlog va undan keyingi ot",
        "explanation": "<p><em>в шко́лу</em> har doim birga turadi. Shuningdek sifat otdan "
                       "oldin (<em>но́вый дом</em>) va soʻroq soʻzi gap boshida (<em>Куда́ ты"
                       " идёшь?</em>).</p>",
    },
    {
        "text": "<p>Savolga toʻgʻri tartibda javob bering.</p><p><strong>— Кто откры́л "
                "окно́?</strong></p>",
        "choices": [
            "Окно́ откры́л Бекзо́д.",
            "Откры́л Бекзо́д окно́.",
            "Окно́ Бекзо́д откры́л.",
            "Бекзо́д откры́л окно́.",
        ],
        "correct": "Окно́ откры́л Бекзо́д.",
        "explanation": "<p>Savol «kim» haqida, demak javob — <em>Бекзо́д</em> — gap "
                       "<strong>oxirida</strong> turishi kerak. <em>Бекзо́д откры́л "
                       "окно́</em> grammatik jihatdan toʻgʻri, lekin «u nima qildi?» degan "
                       "savolga javob berardi.</p>",
    },
    {
        "text": "<p>Savolga toʻgʻri tartibda javob bering.</p><p><strong>— Что написа́ла "
                "Дилно́за?</strong></p>",
        "choices": [
            "Письмо́ написа́ла Дилно́за.",
            "Написа́ла Дилно́за письмо́.",
            "Дилно́за письмо́ написа́ла.",
            "Дилно́за написа́ла письмо́.",
        ],
        "correct": "Дилно́за написа́ла письмо́.",
        "explanation": "<p>Savol «nima» haqida, demak <em>письмо́</em> oxirga tushadi. "
                       "<em>Письмо́ написа́ла Дилно́за</em> esa «kim yozgan?» degan savolga "
                       "javob berardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu gap qaysi savolga javob "
                "beradi?</p><p><strong>Э́ту статью́ Оле́г написа́л за оди́н "
                "ве́чер.</strong></p>",
        "choices": [
            "Кто написа́л э́ту статью́?",
            "Что написа́л Оле́г?",
            "За ско́лько вре́мени Оле́г написа́л статью́?",
            "Где Оле́г написа́л статью́?",
        ],
        "correct": "За ско́лько вре́мени Оле́г написа́л статью́?",
        "explanation": "<p>Oxirgi qism — <em>за оди́н ве́чер</em> — yangi maʼlumot. Maqola "
                       "ham, Oleg ham allaqachon maʼlum, shuning uchun ular oldinda "
                       "turibdi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Kitobni men olmadim, boshqa odam olgan» "
                "degan maʼnoni bering.</p>",
        "choices": [
            "Я не брал э́ту кни́гу.",
            "Не я брал э́ту кни́гу.",
            "Я брал не э́ту кни́гу.",
            "Э́ту кни́гу я не брал.",
        ],
        "correct": "Не я брал э́ту кни́гу.",
        "explanation": "<p><em>Не</em> inkor qilinayotgan soʻz — <em>я</em> — ning oldida "
                       "turishi kerak. <em>Я не брал</em> shunchaki «men olmadim», <em>не "
                       "э́ту кни́гу</em> esa «bu kitobni emas» degani.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Men unga bu haqda emas, boshqa narsa "
                "haqida aytdim» — qaysi gap?</p>",
        "choices": [
            "Я не говори́л ему́ об э́том.",
            "Не я говори́л ему́ об э́том.",
            "Я говори́л не ему́.",
            "Я говори́л ему́ не об э́том.",
        ],
        "correct": "Я говори́л ему́ не об э́том.",
        "explanation": "<p><em>Не</em> <strong>об э́том</strong> ning oldida turibdi, demak "
                       "aynan «bu mavzu» inkor qilinyapti. Bir soʻzni bir soʻz oʻngga "
                       "surganingizda kim aybdor ekani oʻzgaradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu ikki gapning farqi "
                "nimada?</p><p><strong>В ко́мнате стоя́л стол.</strong> / <strong>Стол стоя́л"
                " в ко́мнате.</strong></p>",
        "choices": [
            "Farqi yoʻq, ikkalasi bir xil",
            "Birinchisida stol yangi maʼlumot, ikkinchisida esa tanish",
            "Birinchisi savol, ikkinchisi darak gap",
            "Birinchisi oʻtgan zamon, ikkinchisi hozirgi",
        ],
        "correct": "Birinchisida stol yangi maʼlumot, ikkinchisida esa tanish",
        "explanation": "<p><em>В ко́мнате стоя́л стол</em> — «xonada bir stol turardi»; "
                       "<em>Стол стоя́л в ко́мнате</em> — «oʻsha stol xonada turardi». Artikl"
                       " yoʻq, shuning uchun bu farqni <strong>tartib</strong> "
                       "koʻrsatadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Urgʻuni <strong>«ertaga»</strong> ga "
                "qoʻying.</p><p><strong>Afsona imtihonni ertaga topshiradi.</strong></p>",
        "choices": [
            "За́втра Афсо́на сдаёт экза́мен.",
            "Афсо́на сдаёт за́втра экза́мен.",
            "Экза́мен Афсо́на сдаёт за́втра.",
            "Афсо́на за́втра сдаёт экза́мен.",
        ],
        "correct": "Экза́мен Афсо́на сдаёт за́втра.",
        "explanation": "<p>Urgʻu «ertaga» da boʻlgani uchun <em>за́втра</em> gap "
                       "<strong>oxiriga</strong> tushadi. Oʻzbekchada esa u feʼldan oldin "
                       "turibdi — ikkala tilda ham urgʻuli soʻzning oʻz joyi bor.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi gap «bir bola keldi» degan maʼnoni "
                "beradi?</p>",
        "choices": [
            "Ма́льчик пришёл.",
            "Пришёл ма́льчик.",
            "Ма́льчик не пришёл.",
            "Пришёл ли ма́льчик?",
        ],
        "correct": "Пришёл ма́льчик.",
        "explanation": "<p>Ega <strong>oxirda</strong> turgani uchun u yangi maʼlumot — «bir "
                       "bola». <em>Ма́льчик пришёл</em> esa «oʻsha bola keldi» degani, chunki"
                       " ega boshda va demak tanish.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi gapda soʻz tartibi "
                "<strong>buzilgan</strong>?</p>",
        "choices": [
            "Куда́ ты идёшь?",
            "Ты идёшь куда́?",
            "Но́вый дом стои́т на углу́.",
            "Кни́гу купи́л Жасу́р.",
        ],
        "correct": "Ты идёшь куда́?",
        "explanation": "<p>Soʻroq soʻzi <strong>gap boshida</strong> turishi kerak: <em>Куда́"
                       " ты идёшь?</em> Qolgan uch gapda tartib toʻgʻri — ular shunchaki "
                       "turli urgʻu beryapti.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ogʻzaki nutqda tartibni oʻzgartirmasdan "
                "urgʻu qoʻyish mumkinmi?</p>",
        "choices": [
            "Yoʻq, faqat tartib bilan",
            "Ha, ovoz bilan — bu логи́ческое ударе́ние",
            "Ha, lekin faqat savol gaplarda",
            "Ha, urgʻu belgisi qoʻyish orqali",
        ],
        "correct": "Ha, ovoz bilan — bu логи́ческое ударе́ние",
        "explanation": "<p>Gapirganda ovozni koʻtarish bilan urgʻu qoʻyiladi. Lekin "
                       "<strong>yozuvda ovoz yoʻq</strong> — shuning uchun yozma matnda "
                       "urgʻuni faqat tartib koʻrsatadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbek tilida urgʻuli soʻz qayerda "
                "turadi?</p>",
        "choices": ["Gap oxirida", "Gap boshida", "Egadan oldin", "Feʼldan darrov oldin"],
        "correct": "Feʼldan darrov oldin",
        "explanation": "<p><em>Jasur kecha <strong>kitobni</strong> sotib oldi</em> · "
                       "<em>Kitobni kecha <strong>Jasur</strong> sotib oldi</em> — urgʻuli "
                       "soʻz har doim feʼldan oldin. Ruschada esa <strong>gap "
                       "oxirida</strong>.</p>",
    },
    {
        "text": "<p>Qaysi javob savolga <strong>mos kelmaydi</strong>?</p><p><strong>— Когда́"
                " Жасу́р купи́л кни́гу?</strong></p>",
        "choices": [
            "— Вчера́ он купи́л её.",
            "— Кни́гу Жасу́р купи́л вчера́.",
            "— Жасу́р купи́л кни́гу вчера́.",
            "— Кни́гу вчера́ купи́л Жасу́р.",
        ],
        "correct": "— Кни́гу вчера́ купи́л Жасу́р.",
        "explanation": "<p>Savol <strong>vaqt</strong> haqida, demak <em>вчера́</em> oxirda "
                       "turishi kerak. Bu javobda esa oxirda <em>Жасу́р</em> turibdi — u «kim"
                       " sotib oldi?» degan savolga javob berardi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "Rus tilida tartib erkin, shuning uchun maʼno hech qachon oʻzgarmaydi.",
            "Не gapning oxiriga qoʻyiladi.",
            "Rus tilida sifat otdan keyin turadi.",
            "Rus tilida artikl yoʻq, uning vazifasini soʻz tartibi bajaradi.",
        ],
        "correct": "Rus tilida artikl yoʻq, uning vazifasini soʻz tartibi bajaradi.",
        "explanation": "<p>Qolgan uchtasi xato: tartib maʼnoni <em>oʻzgartiradi</em>; "
                       "<em>не</em> inkor qilinayotgan soʻz oldida turadi; sifat otdan "
                       "<strong>oldin</strong> keladi (<em>но́вый дом</em>).</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Кто взял мой "
                "телефо́н?</strong></p><p><strong>— ___</strong></p>",
        "choices": [
            "Твой телефо́н взяла́ Дилно́за.",
            "Дилно́за взяла́ твой телефо́н.",
            "Взяла́ Дилно́за телефо́н.",
            "Телефо́н Дилно́за взяла́.",
        ],
        "correct": "Твой телефо́н взяла́ Дилно́за.",
        "explanation": "<p>Savol «kim» haqida, demak <em>Дилно́за</em> gap oxirida. Telefon "
                       "allaqachon maʼlum, shuning uchun u boshda turadi — bu <strong>savol "
                       "testi</strong>ning aynan oʻzi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu gapni ruschaga oʻgiring: "
                "<strong>«Bogʻda bolalar oʻynayotgan edi»</strong> (bolalar birinchi marta "
                "tilga olinyapti).</p>",
        "choices": [
            "В саду́ де́ти игра́ли.",
            "Де́ти игра́ли в саду́.",
            "В саду́ игра́ли де́ти.",
            "Игра́ли де́ти в саду́.",
        ],
        "correct": "В саду́ игра́ли де́ти.",
        "explanation": "<p>Bolalar <strong>yangi</strong> maʼlumot, demak ular gap oxirida "
                       "turishi kerak. <em>Де́ти игра́ли в саду́</em> esa «oʻsha bolalar "
                       "bogʻda oʻynayotgan edi» degani boʻlardi.</p>",
    },
]


# =====================================================================
# PR-90 — Rasmiy va norasmiy uslub
# =====================================================================

Q_PR90 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bitta odamga yozilgan rasmiy xatda "
                "<strong>Вы</strong> qanday yoziladi?</p>",
        "choices": [
            "Bosh harf bilan — Вы, Вам, Ваш",
            "Har doim kichik harf bilan",
            "Faqat xat oxirida bosh harf bilan",
            "Qavs ichida",
        ],
        "correct": "Bosh harf bilan — Вы, Вам, Ваш",
        "explanation": "<p>Bu hurmat belgisi: <em>Сообща́ю <strong>Вам</strong>… Прошу́ "
                       "<strong>Вас</strong>…</em> Koʻpchilikka yozilsa (eʼlonda) — kichik "
                       "harf bilan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Сказа́ть</strong> soʻzining rasmiy"
                " jufti qaysi?</p>",
        "choices": ["говори́ть", "сообщи́ть", "рассказа́ть", "сказану́ть"],
        "correct": "сообщи́ть",
        "explanation": "<p><strong>Сообщи́ть</strong> — «xabar bermoq». Rasmiy variant "
                       "deyarli har doim uzunroq va kitobiyroq: <em>Сообща́ю Вам, "
                       "что…</em></p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rasmiy matnda qaysi biri "
                "<strong>boʻlmaydi</strong>?</p>",
        "choices": [
            "Toʻliq gaplar",
            "Majhul nisbat",
            "Yuklamalar: же, ведь, ну, вот",
            "«В связи́ с» predlogi",
        ],
        "correct": "Yuklamalar: же, ведь, ну, вот",
        "explanation": "<p>Yuklamalar (PR-84) — <strong>norasmiylik belgisi</strong>. Xuddi "
                       "jonli qisqarishlar (PR-85) va kichraytirish (PR-88) kabi: uchchalasi "
                       "rasmiy matnga kirmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>В связи́ с</strong> qaysi kundalik"
                " soʻzning rasmiy jufti?</p>",
        "choices": ["из-за", "вме́сто", "кро́ме", "по́сле"],
        "correct": "из-за",
        "explanation": "<p><em>Из-за дождя́</em> → <em>в связи́ с дождём</em>. Eʼtibor "
                       "bering: <em>из-за</em> Роди́тельный oladi, <em>в связи́ с</em> esa "
                       "<strong>Твори́тельный</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Канцеляри́т</strong> nima?</p>",
        "choices": [
            "Idora xodimining kasbi",
            "Rasmiy xat turi",
            "Rasmiylikning oshib ketgani — ogʻir, tushunarsiz til",
            "Eski imlo qoidasi",
        ],
        "correct": "Rasmiylikning oshib ketgani — ogʻir, tushunarsiz til",
        "explanation": "<p>Bu soʻzni yozuvchi Korney Chukovskiy 1962-yilda «Живо́й как жизнь»"
                       " kitobida oʻylab topgan. Belgisi: ketma-ket uchta «-ение / -ание» li "
                       "ot.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Купи́ть</strong> soʻzining rasmiy "
                "jufti qaysi?</p>",
        "choices": ["приобрести́", "покупа́ть", "предоста́вить", "получи́ть"],
        "correct": "приобрести́",
        "explanation": "<p><em>Компа́ния <strong>приобрела́</strong> но́вое "
                       "обору́дование.</em> Kundalik nutqda esa oddiy <em>купи́ла</em> "
                       "deyiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu gapni norasmiy uslubga "
                "oʻgiring.</p><p><strong>Бы́ло при́нято реше́ние перенести́ "
                "встре́чу.</strong></p>",
        "choices": [
            "Реше́ние встре́чи бы́ло перенесено́.",
            "Мы реши́ли перенести́ встре́чу.",
            "Встре́ча была́ перенесена́.",
            "Осуществлено́ перенесе́ние встре́чи.",
        ],
        "correct": "Мы реши́ли перенести́ встре́чу.",
        "explanation": "<p>Majhul nisbat shaxsni yashirardi; norasmiy uslubda esa "
                       "<strong>kim</strong> qilgani aytiladi. Qolgan variantlar yanada "
                       "rasmiyroq yoki канцеляри́т.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Boshliqqa yozilgan xatda qaysi soʻrov "
                "toʻgʻri?</p>",
        "choices": [
            "Дай, пожа́луйста, о́тпуск.",
            "Мне ну́жен о́тпуск.",
            "Прошу́ Вас предоста́вить о́тпуск.",
            "Хочу́ взять о́тпуск.",
        ],
        "correct": "Прошу́ Вас предоста́вить о́тпуск.",
        "explanation": "<p>Rasmiy soʻrov <strong>«Прошу́ Вас» + infinitiv</strong> qolipida "
                       "beriladi. <em>Хочу́</em> va <em>мне ну́жно</em> rasmiy matnda "
                       "ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Сейча́с</strong> soʻzining rasmiy "
                "jufti qaysi?</p>",
        "choices": ["в настоя́щее вре́мя", "в э́то вре́мя", "тепе́рь", "на да́нный час"],
        "correct": "в настоя́щее вре́мя",
        "explanation": "<p><em>В настоя́щее вре́мя</em> — «hozirgi vaqtda». Oʻzbekchada ham "
                       "xuddi shu ikkilik bor: <em>hozir</em> → <em>ayni paytda</em>.</p>",
    },
    {
        "text": "<p>Bu gapda nima notoʻgʻri?</p><p><strong>Прошу́ предоста́вить мне о́тпуск "
                "на неде́льку.</strong></p>",
        "choices": [
            "«Прошу́» oʻrniga «Хочу́» boʻlishi kerak",
            "«Предоста́вить» juda rasmiy",
            "«Неде́льку» — kichraytirish, rasmiy matnda boʻlmaydi",
            "«Мне» ortiqcha",
        ],
        "correct": "«Неде́льку» — kichraytirish, rasmiy matnda boʻlmaydi",
        "explanation": "<p>Toʻgʻrisi — <strong>на неде́лю</strong>. Qolgan hamma narsa "
                       "joyida: bitta norasmiy soʻz butun xatning ohangini buzadi "
                       "(PR-88).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Uslubning uch murvati qaysilar?</p>",
        "choices": [
            "Uzunlik, tezlik, ohang",
            "Murojaat, lugʻat, grammatika",
            "Zamon, nisbat, kelishik",
            "Ega, kesim, toʻldiruvchi",
        ],
        "correct": "Murojaat, lugʻat, grammatika",
        "explanation": "<p><strong>Murojaat</strong> (ты/Вы), <strong>lugʻat</strong> "
                       "(сказа́ть/сообщи́ть), <strong>grammatika</strong> (я реши́л / бы́ло "
                       "при́нято реше́ние). Uchchalasini birga burasiz.</p>",
    },
    {
        "text": "<p>Bu канцеляри́т ni tuzating.</p><p><strong>Осуществля́ем проведе́ние "
                "прове́рки докуме́нтов.</strong></p>",
        "choices": [
            "Прове́рка докуме́нтов осуществля́ется.",
            "Проверя́ем докуме́нты.",
            "Произво́дим прове́рку докуме́нтов.",
            "Осуществля́ем прове́рку докуме́нтов.",
        ],
        "correct": "Проверя́ем докуме́нты.",
        "explanation": "<p>Ketma-ket uchta «-ение» li ot kelgan edi — bu канцеляри́т belgisi."
                       " Ularning birini <strong>feʼlga</strong> aylantirsangiz, gap "
                       "tiklanadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Boʻlim boshligʻiga yozilgan xat qaysi biri"
                " bilan boshlanadi?</p>",
        "choices": [
            "Оль, слу́шай…",
            "Приве́т, О́льга Петро́вна!",
            "Здра́сьте!",
            "Уважа́емая О́льга Петро́вна!",
        ],
        "correct": "Уважа́емая О́льга Петро́вна!",
        "explanation": "<p>Rasmiy murojaat: <strong>Уважа́емая</strong> + ism va otasining "
                       "ismi. <em>Уважа́ем<strong>ый</strong></em> — erkakka, "
                       "<em>Уважа́ем<strong>ая</strong></em> — ayolga.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Но</strong> bogʻlovchisining "
                "rasmiy jufti qaysi?</p>",
        "choices": ["одна́ко", "зато́", "а", "хотя́"],
        "correct": "одна́ко",
        "explanation": "<p><em>Одна́ко</em> — «lekin, biroq», kitobiy variant. <em>Зато́</em>"
                       " va <em>а</em> esa aksincha, koʻproq soʻzlashuv nutqiga xos.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rasmiy uslub nega majhul nisbatni yaxshi "
                "koʻradi?</p>",
        "choices": [
            "U qisqaroq",
            "U shaxsni yashiradi",
            "U faqat oʻtgan zamonda ishlatiladi",
            "U yodlash oson",
        ],
        "correct": "U shaxsni yashiradi",
        "explanation": "<p><em>Бы́ло при́нято реше́ние</em> — kim qaror qilgani aytilmaydi. "
                       "Rasmiy matn koʻpincha aynan shuni xohlaydi: javobgarlik shaxsga emas,"
                       " muassasaga tegishli boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi juftlik "
                "<strong>notoʻgʻri</strong>?</p>",
        "choices": [
            "дать — предоста́вить",
            "сказа́ть — сообщи́ть",
            "о́чень — весьма́",
            "пото́м — одна́ко",
        ],
        "correct": "пото́м — одна́ко",
        "explanation": "<p><em>Пото́м</em> ning rasmiy jufti — <strong>впосле́дствии</strong>"
                       " yoki <em>зате́м</em>. <em>Одна́ко</em> esa <em>но</em> ning jufti — "
                       "bu bogʻlovchi, vaqt soʻzi emas.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "Прошу́ Вас рассмотре́ть моё заявле́ние.",
            "Уважа́емый Дми́трий Ива́нович! Не могли́ бы Вы посмотре́ть отчёт?",
            "Уважа́емый Дми́трий Ива́нович! Ты не мог бы посмотре́ть отчёт?",
            "Сообща́ю Вам, что докуме́нты гото́вы.",
        ],
        "correct": "Уважа́емый Дми́трий Ива́нович! Ты не мог бы посмотре́ть отчёт?",
        "explanation": "<p><em>Уважа́емый + ism va otasining ismi</em> bilan "
                       "<strong>ты</strong> birga kelmaydi. Murojaat rasmiy boʻlsa, olmosh "
                       "ham rasmiy boʻlishi shart: <strong>Вы</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "«Ну» soʻzi rasmiy xatni yumshatadi.",
            "Rasmiy uslubda kichraytirish muloyimlik uchun ishlatiladi.",
            "Rasmiy uslubni qanchalik ogʻirlashtirsangiz, shunchalik yaxshi.",
            "Rasmiy matnda yuklama, qisqarish va kichraytirish boʻlmaydi.",
        ],
        "correct": "Rasmiy matnda yuklama, qisqarish va kichraytirish boʻlmaydi.",
        "explanation": "<p>Uchchalasi ham norasmiylik belgisi (PR-84, PR-85, PR-88). "
                       "Ogʻirlashtirish esa канцеляри́т ga olib keladi — yaxshi rasmiy xat "
                       "<strong>qisqa</strong> xat.</p>",
    },
    {
        "text": "<p>Bu xabarni boshligʻingizga yozing.</p><p><strong>«Дим, я опозда́ю мину́т "
                "на два́дцать, про́бки».</strong></p>",
        "choices": [
            "Уважа́емый Дми́трий! Ну, я немно́жко опозда́ю.",
            "Дми́трий Ива́нович, я щас опозда́ю, про́бки.",
            "Дим, извини́, опозда́ю мину́т на два́дцать.",
            "Уважа́емый Дми́трий Ива́нович! Сообща́ю, что задержу́сь приме́рно на два́дцать мину́т в связи́ с зато́рами на доро́ге.",
        ],
        "correct": "Уважа́емый Дми́трий Ива́нович! Сообща́ю, что задержу́сь приме́рно на "
                   "два́дцать мину́т в связи́ с зато́рами на доро́ге.",
        "explanation": "<p>Uch murvat ham burildi: murojaat (Дим → Дми́трий Ива́нович), "
                       "lugʻat (про́бки → зато́ры на доро́ге), grammatika (uzuq gap → toʻliq "
                       "gap).</p>",
    },
    {
        "text": "<p>Rasmiy xatni qanday tugatasiz?</p>",
        "choices": [
            "Жду отве́та, целу́ю.",
            "Ну, до свя́зи!",
            "Дава́й, пока́!",
            "Зара́нее благодарю́. С уваже́нием, Жасу́р Кари́мов",
        ],
        "correct": "Зара́нее благодарю́. С уваже́нием, Жасу́р Кари́мов",
        "explanation": "<p>Rasmiy xat <strong>«С уваже́нием»</strong> va toʻliq ism-familiya "
                       "bilan tugaydi. <em>Дава́й</em> va <em>пока́</em> — jonli soʻzlashuv "
                       "(PR-85), bu yerda oʻrni yoʻq.</p>",
    },
]


# =====================================================================
# PR-91 — Xat, ariza va rasmiy hujjat tili
# =====================================================================

Q_PR91 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Arizaning shapkasida "
                "<strong>«kimga»</strong> satri qaysi kelishikda?</p>",
        "choices": ["Роди́тельный", "Да́тельный", "Вини́тельный", "Предло́жный"],
        "correct": "Да́тельный",
        "explanation": "<p><em>Дире́ктор<strong>у</strong> шко́лы "
                       "Ивано́в<strong>ой</strong></em> — «kimga?» degan savolga javob. "
                       "Oʻzbekchada bu joʻnalish kelishigi: "
                       "<em>direktor<strong>ga</strong></em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Shapkadagi <strong>«kimdan»</strong> satri"
                " qanday yasaladi?</p>",
        "choices": [
            "от + Роди́тельный",
            "от + Да́тельный",
            "из + Роди́тельный",
            "с + Твори́тельный",
        ],
        "correct": "от + Роди́тельный",
        "explanation": "<p><em><strong>от</strong> ученик<strong>а́</strong> "
                       "Кари́мов<strong>а</strong></em>. Oʻzbekchada bu chiqish kelishigi: "
                       "<em>oʻquvchi Karimov<strong>dan</strong></em>. Toʻliq moslik.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Заявле́ние</strong> sarlavhasidan "
                "keyin nuqta qoʻyiladimi?</p>",
        "choices": [
            "Ha, har doim",
            "Yoʻq, qoʻyilmaydi",
            "Faqat qoʻlda yozilganda",
            "Faqat maktab arizasida",
        ],
        "correct": "Yoʻq, qoʻyilmaydi",
        "explanation": "<p>Zamonaviy meʼyor: <strong>Заявле́ние</strong> — bosh harf bilan, "
                       "nuqtasiz, oʻrtada. Bu eng koʻp uchraydigan bezak xatolaridan "
                       "biri.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ariza matni qaysi soʻz bilan boshlanadi?</p>",
        "choices": ["Я хочу́…", "Мне ну́жно…", "Прошу́…", "Мо́жно ли…"],
        "correct": "Прошу́…",
        "explanation": "<p>Ariza har doim <strong>«Прошу́»</strong> bilan boshlanadi: "
                       "<em>Прошу́ Вас разреши́ть…</em>, <em>Прошу́ предоста́вить…</em> "
                       "«Xohlayman» emas, «soʻrayman».</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ish xatida murojaatdan keyin qaysi belgi "
                "qoʻyiladi?</p>",
        "choices": ["Nuqta", "Ikki nuqta", "Undov belgisi", "Hech qanday belgi"],
        "correct": "Undov belgisi",
        "explanation": "<p><em>Уважа́емый Дми́трий Ива́нович<strong>!</strong></em> — keyin "
                       "yangi qatordan bosh harf bilan davom etadi. Vergul ham uchraydi, "
                       "lekin undov belgisi rasmiyroq.</p>",
    },
    {
        "text": "<p>Shapkaning yuqori satrini yozing.</p><p><strong>Дире́ктор заво́да — "
                "Петро́в Ива́н Серге́евич</strong></p>",
        "choices": [
            "Дире́ктор заво́да Петро́в И. С.",
            "Дире́ктора заво́да Петро́ва И. С.",
            "Дире́ктору заво́да Петро́ву И. С.",
            "от дире́ктора заво́да Петро́ва И. С.",
        ],
        "correct": "Дире́ктору заво́да Петро́ву И. С.",
        "explanation": "<p>«Kimga?» → <strong>Да́тельный</strong>: "
                       "<em>дире́ктор<strong>у</strong></em>, "
                       "<em>Петро́в<strong>у</strong></em>. Oʻzbekchada: «zavod direktori "
                       "Petrov I. S.<strong>ga</strong>».</p>",
    },
    {
        "text": "<p>Shapkaning pastki satrini yozing.</p><p><strong>Студе́нтка Ю́лдашева "
                "Дилно́за</strong></p>",
        "choices": [
            "от студе́нтки Ю́лдашевой Дилно́зы",
            "от студе́нтка Ю́лдашева Дилно́за",
            "студе́нтке Ю́лдашевой Дилно́зе",
            "от студе́нткой Ю́лдашевой Дилно́зой",
        ],
        "correct": "от студе́нтки Ю́лдашевой Дилно́зы",
        "explanation": "<p>«Kimdan?» → <strong>от + Роди́тельный</strong>. Uchala soʻz ham "
                       "oʻzgaradi: <em>студе́нтка → студе́нтки</em>, <em>Ю́лдашева → "
                       "Ю́лдашевой</em>, <em>Дилно́за → Дилно́зы</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Довожу́ до Ва́шего све́дения, "
                "что…</strong> — oʻzbekchasi?</p>",
        "choices": [
            "Sizdan soʻrayman…",
            "Maʼlum qilamanki…",
            "Ruxsat berishingizni soʻrayman…",
            "Sizga rahmat aytaman…",
        ],
        "correct": "Maʼlum qilamanki…",
        "explanation": "<p>Bu — <strong>xabar berish</strong> qolipi. Soʻrov uchun esa "
                       "<em>Прошу́ Вас…</em> ishlatiladi. Ikkalasini aralashtirmang.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ayolga yozilgan xat qanday boshlanadi?</p>",
        "choices": [
            "Уважа́емый Мари́на Петро́вна!",
            "Уважа́емая Мари́на Петро́вна!",
            "Уважа́емую Мари́ну Петро́вну!",
            "Уважа́емой Мари́не Петро́вне!",
        ],
        "correct": "Уважа́емая Мари́на Петро́вна!",
        "explanation": "<p>Murojaat <strong>Имени́тельный</strong> da turadi va jinsga "
                       "moslashadi: <em>Уважа́ем<strong>ая</strong></em> — ayolga, "
                       "<em>Уважа́ем<strong>ый</strong></em> — erkakka.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Elektron xatning mavzu satri qaysi biri "
                "boʻlishi kerak?</p>",
        "choices": [
            "Те́ма: Здра́вствуйте",
            "Те́ма: Вопро́с",
            "Те́ма: Заявле́ние на о́тпуск с 12 по 19 ма́рта",
            "Те́ма: Сро́чно!!!",
        ],
        "correct": "Те́ма: Заявле́ние на о́тпуск с 12 по 19 ма́рта",
        "explanation": "<p>Mavzuda <strong>nima haqida</strong> ekani turishi kerak — qisqa "
                       "ot iborasi, salomsiz va feʼlsiz. Bunday xat topiladi va ochiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Arizada familiya va ism qanday tartibda "
                "yoziladi?</p>",
        "choices": [
            "Familiya ismdan oldin: Кари́мова Жасу́ра",
            "Ism familiyadan oldin: Жасу́ра Кари́мова",
            "Faqat familiya",
            "Faqat ism",
        ],
        "correct": "Familiya ismdan oldin: Кари́мова Жасу́ра",
        "explanation": "<p>Rasmiy hujjatda <strong>familiya birinchi</strong> keladi. "
                       "Ikkalasi ham shapkada Роди́тельный da turadi, chunki ular «от» dan "
                       "keyin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Прошу́ рассмотре́ть</strong> "
                "qachon ishlatiladi?</p>",
        "choices": [
            "Taʼtil soʻraganda",
            "Ariza yoki taklifni koʻrib chiqishni soʻraganda",
            "Xabar berganda",
            "Rahmat aytganda",
        ],
        "correct": "Ariza yoki taklifni koʻrib chiqishni soʻraganda",
        "explanation": "<p><em>Прошу́ Вас рассмотре́ть моё заявле́ние</em>. Taʼtil uchun "
                       "<em>прошу́ предоста́вить</em>, ruxsat uchun <em>прошу́ "
                       "разреши́ть</em> ishlatiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha arizadagi <strong>«-ga»</strong>"
                " qoʻshimchasi ruschada nimaga toʻgʻri keladi?</p>",
        "choices": ["Да́тельный", "от + Роди́тельный", "Вини́тельный", "Твори́тельный"],
        "correct": "Да́тельный",
        "explanation": "<p><em>Direktor<strong>ga</strong></em> = "
                       "<em>Дире́ктор<strong>у</strong></em>. Shapkaning yuqori satri ikkala "
                       "tilda ham bir xil mantiq bilan qurilgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha arizadagi "
                "<strong>«-dan»</strong> qoʻshimchasi ruschada nimaga toʻgʻri keladi?</p>",
        "choices": ["Предло́жный", "Да́тельный", "от + Роди́тельный", "из + Роди́тельный"],
        "correct": "от + Роди́тельный",
        "explanation": "<p><em>Karimov<strong>dan</strong></em> = <em><strong>от</strong> "
                       "Кари́мов<strong>а</strong></em>. Chiqish kelishigi va «от + "
                       "Роди́тельный» aynan bir vazifani bajaradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi ariza boshlanishi toʻgʻri?</p>",
        "choices": [
            "Я хочу́ уча́ствовать в олимпиа́де.",
            "Мне ну́жно на олимпиа́ду.",
            "Мо́жно я пойду́ на олимпиа́ду?",
            "Прошу́ Вас разреши́ть мне уча́ствовать в олимпиа́де.",
        ],
        "correct": "Прошу́ Вас разреши́ть мне уча́ствовать в олимпиа́де.",
        "explanation": "<p>Qolgan uchtasi — <strong>ogʻzaki nutq</strong>. Arizada xohish "
                       "emas, <strong>soʻrov</strong> yoziladi, va u har doim «Прошу́» bilan "
                       "boshlanadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ish xatining besh qismi qaysi tartibda "
                "keladi?</p>",
        "choices": [
            "xabar → murojaat → minnatdorchilik → soʻrov → imzo",
            "imzo → murojaat → xabar → soʻrov → minnatdorchilik",
            "murojaat → soʻrov → xabar → imzo → minnatdorchilik",
            "murojaat → xabar → soʻrov → minnatdorchilik → imzo",
        ],
        "correct": "murojaat → xabar → soʻrov → minnatdorchilik → imzo",
        "explanation": "<p><em>Уважа́емая…! → Довожу́ до Ва́шего све́дения… → Прошу́ Вас… → "
                       "Зара́нее благодарю́. → С уваже́нием, …</em> Bu tartib hech qachon "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Qaysi shapkada xato bor?</p>",
        "choices": [
            "от студе́нтки Ю́лдашевой Дилно́зы",
            "Дире́ктору шко́лы Ивано́вой М. П.",
            "от ученика́ 9-А кла́сса Кари́мова Жасу́ра",
            "Дире́ктор шко́лы Ивано́ва М. П.",
        ],
        "correct": "Дире́ктор шко́лы Ивано́ва М. П.",
        "explanation": "<p>Bu satr <strong>Имени́тельный</strong> da turibdi, lekin «kimga?» "
                       "degan savolga javob berishi kerak. Toʻgʻrisi: <strong>Дире́ктору "
                       "шко́лы Ивано́вой М. П.</strong></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "«Заявле́ние» soʻzidan keyin nuqta qoʻyiladi.",
            "Arizada ism familiyadan oldin yoziladi.",
            "Shapkaning ikki satri ham bitta kelishikda boʻladi.",
            "Murojaatdan keyin undov belgisi qoʻyiladi va yangi qator boshlanadi.",
        ],
        "correct": "Murojaatdan keyin undov belgisi qoʻyiladi va yangi qator boshlanadi.",
        "explanation": "<p>Qolgan uchtasi xato: nuqta qoʻyilmaydi; familiya birinchi keladi; "
                       "shapkaning satrlari <strong>ikki xil</strong> kelishikda — Да́тельный"
                       " va Роди́тельный.</p>",
    },
    {
        "text": "<p>Ariza matnini tanlang.</p><p><strong>Bekzod 3 apreldan 5 aprelgacha "
                "darsga kela olmaydi — akasining toʻyi bor.</strong></p>",
        "choices": [
            "Прошу́ Вас разреши́ть мне не посеща́ть заня́тия с 3 по 5 апре́ля в связи́ со сва́дьбой бра́та.",
            "Я не приду́ с 3 по 5 апре́ля, у бра́та сва́дьба.",
            "Мне ну́жно на сва́дьбу бра́та с 3 по 5 апре́ля.",
            "Хочу́ не ходи́ть в шко́лу с 3 по 5 апре́ля.",
        ],
        "correct": "Прошу́ Вас разреши́ть мне не посеща́ть заня́тия с 3 по 5 апре́ля в связи́"
                   " со сва́дьбой бра́та.",
        "explanation": "<p>Qolip: <em>Прошу́ Вас</em> + infinitiv + <em>в связи́ с</em> + "
                       "sabab (Твори́тельный). Eʼtibor bering: <strong>со</strong> сва́дьбой "
                       "— ikki undosh yonma-yon kelgani uchun <em>с</em> ga "
                       "<strong>о</strong> qoʻshiladi.</p>",
    },
    {
        "text": "<p>Rasmiy xatning oxirgi ikki satrini tanlang.</p>",
        "choices": [
            "Жду!<br>Кари́мов Ж.",
            "Пока́!<br>Жасу́р",
            "Зара́нее благодарю́.<br>Дава́й!",
            "Зара́нее благодарю́ за отве́т.<br>С уваже́нием, Жасу́р Кари́мов",
        ],
        "correct": "Зара́нее благодарю́ за отве́т.<br>С уваже́нием, Жасу́р Кари́мов",
        "explanation": "<p>Minnatdorchilik, keyin <strong>«С уваже́нием»</strong> va toʻliq "
                       "ism-familiya. <em>Пока́</em> va <em>дава́й</em> — jonli soʻzlashuv "
                       "(PR-85), rasmiy xatda ishlatilmaydi.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-89 Mashq: Soʻz tartibi va maʼno urgʻusi",
        "description": (
            "Yangi maʼlumot gap oxirida. Savol testi, artiklsiz «oʻsha/bir» "
            "farqi va «не» ni koʻchirib maʼnoni oʻzgartirish."
        ),
        "tutorial": "PR-89:",
        "questions": Q_PR89,
    },
    {
        "title": "PR-90 Mashq: Rasmiy va norasmiy uslub",
        "description": (
            "Uslubning uch murvati: murojaat, lugʻat, grammatika. Rasmiy "
            "matnda yuklama, qisqarish va kichraytirish boʻlmaydi. Канцеляри́т."
        ),
        "tutorial": "PR-90:",
        "questions": Q_PR90,
    },
    {
        "title": "PR-91 Mashq: Xat, ariza va rasmiy hujjat tili",
        "description": (
            "Arizaning shapkasi — tirik kelishik mashqi: «kimga» Да́тельный, "
            "«kimdan» от + Роди́тельный. Ish xatining besh qismi."
        ),
        "tutorial": "PR-91:",
        "questions": Q_PR91,
    },
]
