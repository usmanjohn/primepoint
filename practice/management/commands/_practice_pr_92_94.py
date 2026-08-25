# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-92 … PR-94.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_92_94.py --master=prime \\
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
# PR-92 — Telefon, elektron pochta va xabar tili
# =====================================================================

Q_PR92 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Telefonda notanish odam adashib sizga "
                "qoʻngʻiroq qildi. Nima deysiz?</p>",
        "choices": [
            "Вы не туда́ попа́ли.",
            "Вы взя́ли непра́вильный но́мер.",
            "Э́то не мой но́мер.",
            "Вы оши́блись телефо́ном.",
        ],
        "correct": "Вы не туда́ попа́ли.",
        "explanation": "<p><strong>Вы не туда́ попа́ли</strong> — soʻzma-soʻz «siz u yerga "
                       "tushmadingiz». Bu ibora butunligicha yodlanadi, qismlarga ajratib "
                       "tarjima qilinmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Telefonni koʻtarib <strong>«Кто "
                "э́то?»</strong> deyish qanday eshitiladi?</p>",
        "choices": ["Muloyim", "Rasmiy", "Qoʻpol", "Neytral"],
        "correct": "Qoʻpol",
        "explanation": "<p>Goʻyo siz emas, qoʻngʻiroq qilgan odam tushuntirishi kerakdek. "
                       "Muloyim shakli: <strong>Прости́те, с кем я говорю́?</strong> yoki "
                       "<em>Предста́вьтесь, пожа́луйста.</em></p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Chat qisqartmasi <strong>крч</strong> "
                "nimani anglatadi?</p>",
        "choices": ["коро́че", "кра́сный", "кричи́", "круго́м"],
        "correct": "коро́че",
        "explanation": "<p>Qoida bitta: <strong>unlilar tashlab ketiladi</strong>, undoshlar "
                       "qoladi. Xuddi shunday: <em>спс</em> = спаси́бо, <em>пжл</em> = "
                       "пожа́луйста.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rasmiy qoʻngʻiroqda kim birinchi boʻlib "
                "oʻzini tanishtiradi?</p>",
        "choices": [
            "Telefonni koʻtargan odam",
            "Qoʻngʻiroq qilgan odam",
            "Hech kim tanishtirmaydi",
            "Ikkalasi bir vaqtda",
        ],
        "correct": "Qoʻngʻiroq qilgan odam",
        "explanation": "<p><em>Здра́вствуйте, э́то Жасу́р Кари́мов. Могу́ я поговори́ть "
                       "с…</em> — avval salom, keyin oʻzini tanishtirish, undan keyin "
                       "soʻrov.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Chatda qisqa javob oxiriga nuqta "
                "qoʻysangiz, xabar qanday eshitiladi?</p>",
        "choices": ["Rasmiyroq", "Iliqroq", "Sovuq yoki xafa", "Muloyimroq"],
        "correct": "Sovuq yoki xafa",
        "explanation": "<p><em>Хорошо</em> — mayli; <strong>Хорошо.</strong> — «mayli, gapni "
                       "yopdik». Bu faqat qisqa chat xabarlariga tegishli — xatda va hujjatda"
                       " nuqta oʻz oʻrnida turadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p>Aloqa yomon. <strong>Вас ___ "
                "слы́шно.</strong></p>",
        "choices": ["нет", "тру́дно", "пло́хо", "ма́ло"],
        "correct": "пло́хо",
        "explanation": "<p><strong>Вас пло́хо слы́шно</strong> — «sizni yomon eshityapman». "
                       "Yonidagi ibora: <em>Связь плоха́я</em> — aloqa yomon.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rahbaringiz band. Uning hamkasbi nima deb "
                "soʻraydi?</p>",
        "choices": [
            "Что ему́ переда́ть?",
            "Что вы хоти́те?",
            "Заче́м вы звони́те?",
            "Кто вы тако́й?",
        ],
        "correct": "Что ему́ переда́ть?",
        "explanation": "<p><em>Он сейча́с за́нят. <strong>Что ему́ переда́ть?</strong></em> —"
                       " «Unga nima yetkazay?» Bu telefon suhbatining odatiy qolipi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Chat qisqartmalarida qaysi harflar tashlab"
                " ketiladi?</p>",
        "choices": ["Undoshlar", "Oxirgi harflar", "Unlilar", "Bosh harflar"],
        "correct": "Unlilar",
        "explanation": "<p><em>спасибо → спс</em>, <em>пожалуйста → пжл</em>, <em>короче → "
                       "крч</em>. Oʻzbek yozishmasida ham xuddi shunday: <em>salom → "
                       "slm</em>, <em>rahmat → rhmt</em>.</p>",
    },
    {
        "text": "<p>Bu rasmiy xatni tuzating.</p><p><strong>Уважа́емый Оле́г Никола́евич! "
                "Крч, я не смогу́ прийти́.</strong></p>",
        "choices": [
            "Уважа́емый Оле́г Никола́евич! Сообща́ю, что не смогу́ прису́тствовать.",
            "Оле́г Никола́евич, крч, не смогу́.",
            "Уважа́емый Оле́г! Крч, не приду́.",
            "Приве́т! Не смогу́ прийти́.",
        ],
        "correct": "Уважа́емый Оле́г Никола́евич! Сообща́ю, что не смогу́ прису́тствовать.",
        "explanation": "<p><em>Крч</em> — chat qisqartmasi, rasmiy xatga kirmaydi (PR-90). "
                       "Bitta bunday soʻz butun xatning ohangini buzadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Elektron xatning <strong>yarim "
                "rasmiy</strong> darajasi qanday boshlanadi?</p>",
        "choices": [
            "Уважа́емая Мари́на Петро́вна!",
            "Здра́вствуйте, Мари́на Петро́вна!",
            "Приве́т, Мари́на!",
            "Мари́на Петро́вна, слу́шайте…",
        ],
        "correct": "Здра́вствуйте, Мари́на Петро́вна!",
        "explanation": "<p>Yarim rasmiy — kundalik ishda eng koʻp kerak boʻladigan daraja: "
                       "<em>Здра́вствуйте</em> bilan boshlanadi, <em>С уваже́нием</em> bilan "
                       "tugaydi, lekin ogʻir qoliplar yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ruscha yozishmada <strong>«))»</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Savol", "Kulgi va iliqlik", "Norozilik", "Xabar tugadi"],
        "correct": "Kulgi va iliqlik",
        "explanation": "<p>Bu ruscha chatning oʻz belgisi; qavslar soni kuchni koʻrsatadi. "
                       "<em>Спасибо))</em> — «katta rahmat», <em>Спасибо.</em> esa «rahmat, "
                       "lekin xafaman».</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rasmiy telefon suhbatini qanday "
                "tugatasiz?</p>",
        "choices": [
            "Дава́й! Пока́!",
            "Всё, побежа́л!",
            "Ну, до свя́зи!",
            "Всего́ до́брого! До свида́ния!",
        ],
        "correct": "Всего́ до́брого! До свида́ния!",
        "explanation": "<p>Qolgan uchtasi — norasmiy. <em>Дава́й</em> va <em>пока́</em> "
                       "doʻstlar bilan, <em>до свя́зи</em> esa yozishmada ishlatiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Chatdagi nuqta qoidasi qayerda "
                "<strong>ishlamaydi</strong>?</p>",
        "choices": [
            "Qisqa javoblarda",
            "Bir soʻzli xabarlarda",
            "Doʻstlar bilan yozishmada",
            "Elektron xatda va hujjatda",
        ],
        "correct": "Elektron xatda va hujjatda",
        "explanation": "<p>Rasmiy xatda, arizada va hujjatda nuqta oddiy tinish belgisi. "
                       "Qoida faqat <strong>qisqa chat xabarlariga</strong> tegishli.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu iboraning maʼnosi "
                "nima?</p><p><strong>Оста́вьтесь на ли́нии.</strong></p>",
        "choices": [
            "Chiziqda turing",
            "Navbatga turing",
            "Liniyada qoling — telefonni qoʻymang",
            "Keyinroq qoʻngʻiroq qiling",
        ],
        "correct": "Liniyada qoling — telefonni qoʻymang",
        "explanation": "<p>Telefon suhbatining odatiy qolipi. Yonidagi ibora: <em>Подожди́те "
                       "мину́точку</em> — «bir daqiqagina kuting» (PR-88).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi juftlik "
                "<strong>notoʻgʻri</strong>?</p>",
        "choices": [
            "спс — спаси́бо",
            "пжл — пожа́луйста",
            "др — день рожде́ния",
            "сек — секре́т",
        ],
        "correct": "сек — секре́т",
        "explanation": "<p><strong>Сек</strong> = <em>секу́нду</em> — «bir soniya», «hozir». "
                       "<em>Секре́т</em> ning qisqartmasi emas.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "Уважа́емая Мари́на Петро́вна! Спс за отве́т.",
            "Здра́вствуйте! Э́то Дилно́за Ю́лдашева.",
            "Извини́те, вы не туда́ попа́ли.",
            "Прости́те, с кем я говорю́?",
        ],
        "correct": "Уважа́емая Мари́на Петро́вна! Спс за отве́т.",
        "explanation": "<p>Toʻgʻrisi — <strong>Спаси́бо за отве́т</strong>. Chat qisqartmasi "
                       "rasmiy xatga kirmaydi; qolgan uch gap joyida.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "Chatdagi nuqta xabarni muloyimroq qiladi.",
            "Rasmiy qoʻngʻiroqda telefonni koʻtargan odam oʻzini tanishtiradi.",
            "Uslubni faqat oluvchi tanlaydi, kanal taʼsir qilmaydi.",
            "Chat qisqartmalari rasmiy xatga kirmaydi.",
        ],
        "correct": "Chat qisqartmalari rasmiy xatga kirmaydi.",
        "explanation": "<p>Qolgan uchtasi xato: nuqta xabarni <em>sovuq</em> qiladi; rasmiy "
                       "qoʻngʻiroqda <em>qoʻngʻiroq qilgan</em> odam oʻzini tanishtiradi; "
                       "kanal ham til qoʻyadi.</p>",
    },
    {
        "text": "<p>Rasmiy qoʻngʻiroqni boshlang. Siz — Dilnoza Yuldasheva, Marina Petrovna "
                "bilan gaplashmoqchisiz.</p>",
        "choices": [
            "Алло́? Мари́ну мо́жно?",
            "Здра́вствуйте! Э́то Дилно́за Ю́лдашева. Могу́ я поговори́ть с Мари́ной Петро́вной?",
            "Алло́, а э́то кто? Мне Мари́ну.",
            "Приве́т! Мари́на Петро́вна там?",
        ],
        "correct": "Здра́вствуйте! Э́то Дилно́за Ю́лдашева. Могу́ я поговори́ть с Мари́ной "
                   "Петро́вной?",
        "explanation": "<p>Tartib muhim: salom → oʻzini tanishtirish → soʻrov. <em>А э́то "
                       "кто?</em> qoʻpol, <em>Мари́ну мо́жно?</em> esa norasmiy.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Ты придёшь на "
                "др?</strong></p><p><strong>— ___</strong> (oddiy rozilik)</p>",
        "choices": ["Да.", "Да", "Да!!!", "Да…"],
        "correct": "Да",
        "explanation": "<p>Nuqtasiz <strong>Да</strong> — oddiy rozilik. <em>Да.</em> sovuq "
                       "eshitiladi, <em>Да…</em> ikkilanishni bildiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikkilanyapsiz: xat rasmiy boʻlsinmi yoki "
                "doʻstona? Nima qilasiz?</p>",
        "choices": [
            "Doʻstona yozaman — iliqroq",
            "Umuman salom yozmayman",
            "Chat qisqartmalarini ishlataman",
            "Bir daraja rasmiyroq yozaman",
        ],
        "correct": "Bir daraja rasmiyroq yozaman",
        "explanation": "<p>Ortiqcha hurmatdan hech kim xafa boʻlmaydi, ortiqcha yaqinlikdan "
                       "esa boʻlishi mumkin. Shubhalansangiz — rasmiyroq tomonni tanlang.</p>",
    },
]


# =====================================================================
# PR-93 — Ish va oʻqish leksikasi
# =====================================================================

Q_PR93 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Я сдал экза́мен</strong> — bu "
                "nimani anglatadi?</p>",
        "choices": [
            "Imtihondan oʻtdim",
            "Imtihonga kirdim, natija nomaʼlum",
            "Imtihonga tayyorlanyapman",
            "Imtihondan yiqildim",
        ],
        "correct": "Imtihondan oʻtdim",
        "explanation": "<p><strong>Сдать</strong> — СВ, natija bor va u yaxshi. "
                       "<em>Сдава́л</em> esa faqat jarayonni bildiradi: kirdim va yozdim, "
                       "natija nomaʼlum.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«imtihon "
                "topshirdim»</strong> ruschada qaysi shakl?</p>",
        "choices": [
            "сдал экза́мен",
            "сдава́л экза́мен",
            "подгото́вился к экза́мену",
            "провали́л экза́мен",
        ],
        "correct": "сдава́л экза́мен",
        "explanation": "<p>«Topshirmoq» — <strong>jarayon</strong>, demak НСВ: "
                       "<em>сдава́ть</em>. «Imtihondan oʻtmoq» esa natija — "
                       "<em>сдать</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я хочу́ стать ___ .</strong> "
                "(перево́дчик)</p>",
        "choices": ["перево́дчик", "перево́дчика", "перево́дчиком", "перево́дчику"],
        "correct": "перево́дчиком",
        "explanation": "<p>«Кем?» degan savol <strong>Твори́тельный</strong> oladi (PR-40): "
                       "<em>стать перево́дчиком</em>, <em>рабо́тать учи́телем</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Зачёт</strong> "
                "<strong>экза́мен</strong> dan nimasi bilan farq qiladi?</p>",
        "choices": [
            "Zachyotda baho qoʻyilmaydi — faqat «oʻtdi / oʻtmadi»",
            "Zachyot faqat birinchi kursda boʻladi",
            "Zachyot yozma, ekzamen ogʻzaki",
            "Farqi yoʻq, ikkalasi bir xil",
        ],
        "correct": "Zachyotda baho qoʻyilmaydi — faqat «oʻtdi / oʻtmadi»",
        "explanation": "<p><em>Зачёт / незачёт</em>. Ekzamenda esa baho qoʻyiladi. Ikkalasi "
                       "ham <strong>се́ссия</strong> davrida topshiriladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rezyumening qaysi boʻlimida dasturlar va "
                "malakalar yoziladi?</p>",
        "choices": ["Цель", "О́пыт рабо́ты", "Навы́ки", "Образова́ние"],
        "correct": "Навы́ки",
        "explanation": "<p><strong>Навы́ки</strong> — koʻnikmalar. <em>Цель</em> — qaysi "
                       "lavozimga daʼvogarsiz, <em>о́пыт рабо́ты</em> — ish tajribasi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я занима́лся ___ .</strong> "
                "(перево́ды)</p>",
        "choices": ["перево́ды", "перево́дов", "перево́дам", "перево́дами"],
        "correct": "перево́дами",
        "explanation": "<p><em>Занима́ться</em> <strong>Твори́тельный</strong> talab qiladi. "
                       "Tajriba feʼllarini kelishigi bilan birga yodlang — alohida yodlansa, "
                       "rezyumeda xato chiqadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я отвеча́л ___ .</strong> "
                "(докуме́нты)</p>",
        "choices": ["за докуме́нты", "о докуме́нтах", "докуме́нтами", "для докуме́нтов"],
        "correct": "за докуме́нты",
        "explanation": "<p><em>Отвеча́ть за</em> + <strong>Вини́тельный</strong> (PR-83) — "
                       "«…uchun javob bermoq». Rezyumeda eng koʻp ishlatiladigan qoliplardan "
                       "biri.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Suhbatda oʻzingiz haqingizda gapirsangiz, "
                "«imtihondan yiqildim» ni qanday aytasiz?</p>",
        "choices": [
            "Я завали́л экза́мен.",
            "Я не сдал экза́мен.",
            "Я сдава́л экза́мен.",
            "Я потеря́л экза́мен.",
        ],
        "correct": "Я не сдал экза́мен.",
        "explanation": "<p><strong>Не сдал</strong> — eng xotirjam va xavfsiz shakl. "
                       "<em>Завали́л</em> — soʻzlashuv uslubi (PR-85), suhbatda juda ochiq "
                       "eshitiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rezyumeda tillar qanday koʻrsatiladi?</p>",
        "choices": [
            "Ру́сский — свобо́дно.",
            "По-ру́сски — хорошо́.",
            "Ру́сскому — свобо́дно.",
            "На ру́сском — свобо́дно.",
        ],
        "correct": "Ру́сский — свобо́дно.",
        "explanation": "<p>Til nomi <strong>sifat</strong> shaklida turadi: <em>Узбе́кский — "
                       "родно́й. Ру́сский — свобо́дно. Англи́йский — ба́зовый "
                       "у́ровень.</em></p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Suhbatda soʻrashdi: <strong>«Кем вы "
                "ви́дите себя́ че́рез пять лет?»</strong> Qaysi javob toʻgʻri?</p>",
        "choices": [
            "Я хоте́л бы стать руководи́тель отде́ла.",
            "Я хоте́л бы стать руководи́теля отде́ла.",
            "Я хоте́л бы стать руководи́телем отде́ла.",
            "Я хоте́л бы стать руководи́телю отде́ла.",
        ],
        "correct": "Я хоте́л бы стать руководи́телем отде́ла.",
        "explanation": "<p>«Кем?» → <strong>Твори́тельный</strong>. <em>Хоте́л бы</em> "
                       "(PR-60) javobni muloyimroq qiladi — <em>я ста́ну</em> juda qatʼiy "
                       "eshitilardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ в университе́т в 2024 году́"
                " и сейча́с учу́сь на второ́м ку́рсе.</strong></p>",
        "choices": ["поступа́л", "поступи́л", "поступа́ю", "буду поступа́ть"],
        "correct": "поступи́л",
        "explanation": "<p>Qabul qilingansiz — natija bor, demak <strong>СВ</strong>. "
                       "<em>Поступа́л</em> faqat «hujjat topshirdim» degan jarayonni "
                       "bildirardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>До́лжность</strong> nimani "
                "anglatadi?</p>",
        "choices": ["Qarz", "Maosh", "Lavozim", "Majburiyat"],
        "correct": "Lavozim",
        "explanation": "<p><strong>До́лжность</strong> — lavozim. Eʼtibor bering: "
                       "<em>-ость</em> demak <strong>же́нский род</strong> (PR-87): "
                       "<em>но́вая до́лжность</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi juftlik "
                "<strong>notoʻgʻri</strong>?</p>",
        "choices": [
            "сдава́ть — сдать",
            "поступа́ть — поступи́ть",
            "устра́иваться — устро́иться",
            "гото́виться — провали́ть",
        ],
        "correct": "гото́виться — провали́ть",
        "explanation": "<p><em>Гото́виться</em> ning СВ jufti — "
                       "<strong>подгото́виться</strong>. <em>Провали́ть</em> esa butunlay "
                       "boshqa feʼl: «yiqilmoq».</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Испыта́тельный срок</strong> "
                "nima?</p>",
        "choices": ["Imtihon davri", "Sinov muddati", "Taʼtil", "Ish tajribasi"],
        "correct": "Sinov muddati",
        "explanation": "<p>Yangi ishga kirganda beriladigan <strong>sinov muddati</strong>. "
                       "<em>Се́ссия</em> esa oliygohdagi imtihon davri — ikkalasini "
                       "aralashtirmang.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi feʼl <strong>Предло́жный</strong> "
                "oladi?</p>",
        "choices": ["отвеча́ть за", "занима́ться", "руководи́ть", "уча́ствовать в"],
        "correct": "уча́ствовать в",
        "explanation": "<p><em>Уча́ствовал <strong>в олимпиа́де</strong></em> — в + П.п. "
                       "<em>Занима́ться</em> va <em>руководи́ть</em> Твори́тельный, "
                       "<em>отвеча́ть за</em> esa Вини́тельный oladi.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "Я отвеча́л за докуме́нты гру́ппы.",
            "Я сдал экза́мен и поступи́л в университе́т.",
            "Я занима́лся перево́дами два го́да.",
            "Я сдава́л экза́мен, тепе́рь я студе́нт.",
        ],
        "correct": "Я сдава́л экза́мен, тепе́рь я студе́нт.",
        "explanation": "<p>Talaba boʻlgan boʻlsangiz, imtihondan <strong>oʻtgansiz</strong> —"
                       " demak <em>сдал</em> kerak. <em>Сдава́л</em> natija haqida hech narsa"
                       " aytmaydi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "«Сдава́ть» va «сдать» — bir xil maʼnodagi ikki soʻz.",
            "Rezyumeda tillar «по-ру́сски» shaklida yoziladi.",
            "«Зачёт» da baho qoʻyiladi.",
            "«Кем стать?» degan savol Твори́тельный oladi.",
        ],
        "correct": "«Кем стать?» degan savol Твори́тельный oladi.",
        "explanation": "<p>Qolgan uchtasi xato: <em>сдава́ть</em> jarayon, <em>сдать</em> "
                       "natija; tillar sifat shaklida yoziladi; зачётda baho qoʻyilmaydi.</p>",
    },
    {
        "text": "<p>Rezyumening «Языки́» boʻlimini yozing.</p><p><strong>oʻzbekcha — ona "
                "tili, ruscha — erkin, inglizcha — boshlangʻich</strong></p>",
        "choices": [
            "Узбе́кский — родно́й. Ру́сский — свобо́дно. Англи́йский — ба́зовый у́ровень.",
            "Узбе́кский — ро́дина. Ру́сский — свобо́да. Англи́йский — база.",
            "По-узбе́кски — родно́й. По-ру́сски — свобо́дно.",
            "Узбе́кским — родно́й. Ру́сским — свобо́дно.",
        ],
        "correct": "Узбе́кский — родно́й. Ру́сский — свобо́дно. Англи́йский — ба́зовый "
                   "у́ровень.",
        "explanation": "<p>Til nomlari sifat shaklida, daraja esa tayyor qoliplar bilan: "
                       "<em>родно́й · свобо́дно · хорошо́ · ба́зовый у́ровень</em>.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Есть ли у вас "
                "вопро́сы?</strong></p><p><strong>— ___</strong></p>",
        "choices": [
            "Нет, я всё зна́ю.",
            "Да, скажи́те, пожа́луйста, како́й у вас испыта́тельный срок?",
            "Не зна́ю.",
            "А ско́лько вы мне заплати́те?",
        ],
        "correct": "Да, скажи́те, пожа́луйста, како́й у вас испыта́тельный срок?",
        "explanation": "<p>Suhbat oxirida savol berish yaxshi belgi — qiziqishni koʻrsatadi. "
                       "<em>Скажи́те, пожа́луйста</em> qolipi savolni muloyim qiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu ikki gapning farqi "
                "nimada?</p><p><strong>Афсо́на сдава́ла экза́мен. / Афсо́на сдала́ "
                "экза́мен.</strong></p>",
        "choices": [
            "Farqi yoʻq",
            "Birinchisi kelasi zamon, ikkinchisi oʻtgan",
            "Birinchisi jarayon (topshirdi), ikkinchisi natija (oʻtdi)",
            "Birinchisida bir imtihon, ikkinchisida koʻp",
        ],
        "correct": "Birinchisi jarayon (topshirdi), ikkinchisi natija (oʻtdi)",
        "explanation": "<p>Ikkalasi ham oʻtgan zamon, farq <strong>feʼl turida</strong>. "
                       "Oʻzbekchada ham ikki ibora: «imtihon topshirdi» va «imtihondan "
                       "oʻtdi».</p>",
    },
]


# =====================================================================
# PR-94 — Фразеологизмы
# =====================================================================

Q_PR94 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Бить баклу́ши</strong> nimani "
                "anglatadi?</p>",
        "choices": ["Bekorchilik qilmoq", "Qattiq ishlamoq", "Yogʻoch yormoq", "Janjal qilmoq"],
        "correct": "Bekorchilik qilmoq",
        "explanation": "<p><em>Баклу́ши</em> — yogʻoch qoshiq yasash uchun yorib qoʻyilgan "
                       "boʻlaklar. Ularni yorish eng oson, malaka talab qilmaydigan ish edi —"
                       " shundan «bekorchilik» maʼnosi chiqqan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Frazeologizmning maʼnosi qayerdan "
                "chiqadi?</p>",
        "choices": [
            "Har bir soʻzning maʼnosini qoʻshishdan",
            "Faqat birinchi soʻzdan",
            "Butun birikmadan — qismlaridan chiqmaydi",
            "Gapdagi feʼldan",
        ],
        "correct": "Butun birikmadan — qismlaridan chiqmaydi",
        "explanation": "<p><em>Сел в лу́жу</em> soʻzma-soʻz «koʻlmakka oʻtirdi», aslida esa "
                       "«sharmanda boʻldi». Shuning uchun ibora lugʻatdan <strong>butun "
                       "holda</strong> qidiriladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Зару́бить на носу́»</strong> dagi"
                " <strong>нос</strong> nima?</p>",
        "choices": [
            "Burun",
            "Kema burni",
            "Oʻzi bilan olib yuriladigan hisob taxtachasi",
            "Pichoq",
        ],
        "correct": "Oʻzi bilan olib yuriladigan hisob taxtachasi",
        "explanation": "<p>Bu <em>нос</em> <strong>носи́ть</strong> feʼlidan — oʻzi bilan "
                       "olib yuriladigan taxtacha. Unga oʻyiq (<em>зару́бка</em>) qilib hisob"
                       " yuritishardi. Burunga aloqasi yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Ни пу́ха ни пера́!»</strong> ga "
                "qanday javob beriladi?</p>",
        "choices": ["Спаси́бо!", "И тебе́!", "Пожа́луйста!", "К чёрту!"],
        "correct": "К чёрту!",
        "explanation": "<p>Yagona toʻgʻri javob. <em>Спаси́бо</em> deyilmaydi — ishonchga "
                       "koʻra bu omadni qaytaradi. Ibora ovchilardan qolgan: «na moʻyna, na "
                       "pat».</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«yeng shimarib»</strong>"
                " iborasining ruscha jufti qaysi?</p>",
        "choices": ["засучи́в рукава́", "сложа́ ру́ки", "рука́ о́б руку", "спустя́ рукава́"],
        "correct": "засучи́в рукава́",
        "explanation": "<p>Ikkala til ham bir xil obrazni tanlagan. <em>Спустя́ рукава́</em> "
                       "esa aksincha — «beparvo», chunki tushirilgan yeng bilan ishlab "
                       "boʻlmasdi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«qoʻl qovushtirib "
                "oʻtirmoq»</strong> ruschada qanday?</p>",
        "choices": [
            "держа́ть язы́к за зуба́ми",
            "води́ть за́ нос",
            "сиде́ть сложа́ ру́ки",
            "тяну́ть кота́ за хвост",
        ],
        "correct": "сиде́ть сложа́ ру́ки",
        "explanation": "<p>Yana bir soʻzma-soʻz moslik — ikkala tilda ham «qoʻlni qovushtirib"
                       " oʻtirish» obrazi. Maʼnosi: hech narsa qilmay oʻtirmoq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Спустя́ рукава́</strong> nimani "
                "anglatadi?</p>",
        "choices": ["Beparvo, sovuqqonlik bilan", "Tez", "Yashirincha", "Jon-jahdi bilan"],
        "correct": "Beparvo, sovuqqonlik bilan",
        "explanation": "<p>Eski rus kiyimining yenglari juda uzun edi — yeng tushirilgan "
                       "holda ishlab boʻlmasdi. Teskarisi: <strong>засучи́в "
                       "рукава́</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Води́ть за́ нос</strong> iborasi "
                "qayerdan kelgan?</p>",
        "choices": [
            "Yarmarkalarda ayiqlarni burniga halqa oʻtkazib yetaklashdan",
            "Bolalarni qoʻlidan yetaklashdan",
            "Dengizchilarning odatidan",
            "Otlarni yuganidan yetaklashdan",
        ],
        "correct": "Yarmarkalarda ayiqlarni burniga halqa oʻtkazib yetaklashdan",
        "explanation": "<p>Ayiq halqa tufayli qayerga yetaklansa, oʻsha yerga borardi. "
                       "Shundan «aldab yurmoq, oʻz xohishiga boʻysundirmoq» maʼnosi "
                       "chiqqan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga qaysi ibora tushadi?</p><p><strong>Он обеща́л зако́нчить в "
                "понеде́льник, пото́м в сре́ду, пото́м в пя́тницу. У него́ ___ .</strong></p>",
        "choices": [
            "как снег на́ голову",
            "семь пя́тниц на неде́ле",
            "как с гу́ся вода́",
            "не в свое́й таре́лке",
        ],
        "correct": "семь пя́тниц на неде́ле",
        "explanation": "<p>Fikri tez-tez oʻzgaradigan, soʻzida turmaydigan odam haqida. "
                       "Soʻzma-soʻz: «haftada yetti juma».</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Де́лать из му́хи слона́</strong> "
                "nimani anglatadi?</p>",
        "choices": [
            "Sehrgarlik qilmoq",
            "Yolgʻon gapirmoq",
            "Hayvonlarni yaxshi koʻrmoq",
            "Kichik narsani kattalashtirmoq",
        ],
        "correct": "Kichik narsani kattalashtirmoq",
        "explanation": "<p>Soʻzma-soʻz «pashshadan fil yasamoq». Oʻzbekchada oʻsha maʼno "
                       "boshqa obraz bilan beriladi — shuning uchun iborani tarjima qilmang, "
                       "<strong>juftini toping</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Не в свое́й таре́лке»</strong> "
                "iborasi qanday paydo boʻlgan?</p>",
        "choices": [
            "Rus xalq ertagidan",
            "Fransuzcha soʻzning notoʻgʻri tarjimasidan",
            "Dasturxon odobidan",
            "Harbiy atamadan",
        ],
        "correct": "Fransuzcha soʻzning notoʻgʻri tarjimasidan",
        "explanation": "<p>Fransuzcha <em>assiette</em> ning ikki maʼnosi bor: «likopcha» va "
                       "«holat». Tarjimon notoʻgʻri maʼnoni tanlagan, xato esa qolib ketgan —"
                       " ibora shu tarzda yashab qolgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«tilini tiymoq»</strong>"
                " ruschada qanday?</p>",
        "choices": [
            "сесть в лу́жу",
            "валя́ть дурака́",
            "как с гу́ся вода́",
            "держа́ть язы́к за зуба́ми",
        ],
        "correct": "держа́ть язы́к за зуба́ми",
        "explanation": "<p>Uchinchi soʻzma-soʻz moslik: ikkala til ham <strong>til</strong> "
                       "obrazini tanlagan. Maʼnosi: jim turmoq, sir saqlamoq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Как снег на́ голову</strong> "
                "nimani anglatadi?</p>",
        "choices": ["Sovuq havoda", "Kutilmaganda, toʻsatdan", "Bosh ogʻrigʻi bilan", "Qishda"],
        "correct": "Kutilmaganda, toʻsatdan",
        "explanation": "<p><em>Он прие́хал как снег на́ голову</em> — «u toʻsatdan keldi». "
                       "Obraz aniq: tomdan tushgan qor hech kimni ogohlantirmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi ikki ibora <strong>bir-birining "
                "teskarisi</strong>?</p>",
        "choices": [
            "бить баклу́ши — сиде́ть сложа́ ру́ки",
            "спустя́ рукава́ — засучи́в рукава́",
            "води́ть за́ нос — зару́бить на носу́",
            "сесть в лу́жу — как с гу́ся вода́",
        ],
        "correct": "спустя́ рукава́ — засучи́в рукава́",
        "explanation": "<p>Ikkalasi ham bitta uzun yengdan chiqqan: tushirilgan yeng — "
                       "beparvolik, shimarilgan yeng — jon-jahdi bilan ish. Ularni birga "
                       "yodlang.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi shakl <strong>toʻgʻri</strong>?</p>",
        "choices": ["бить баклу́шу", "бить баклу́ши", "бить по баклу́шам", "бить баклу́шей"],
        "correct": "бить баклу́ши",
        "explanation": "<p>Ibora shakli <strong>qotib qolgan</strong> — soʻzlarini "
                       "almashtirib ham, kelishigini oʻzgartirib ham boʻlmaydi. Xuddi "
                       "shunday: <em>сиде́ть сложа́ ру́ки</em>.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>uslub</strong> xatosi bor?</p>",
        "choices": [
            "Она́ пришла́ как снег на́ голову.",
            "Он рабо́тал спустя́ рукава́, поэ́тому его́ уво́лили.",
            "Прошу́ Вас не тяну́ть кота́ за хвост.",
            "Не волну́йся, ему́ как с гу́ся вода́.",
        ],
        "correct": "Прошу́ Вас не тяну́ть кота́ за хвост.",
        "explanation": "<p>Grammatika toʻgʻri, lekin bu — <strong>ariza</strong> tili. Rasmiy"
                       " matnda ibora ishlatilmaydi (PR-90, PR-91). Toʻgʻrisi: <em>в "
                       "кратча́йший срок</em>.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "Не де́лай из му́хи слона́.",
            "Он взя́лся за де́ло засучи́в рукава́ и всё сде́лал за день.",
            "Он рабо́тал засучи́в рукава́, поэ́тому ничего́ не сде́лал.",
            "Зару́би себе́ на носу́: экза́мен в пя́тницу.",
        ],
        "correct": "Он рабо́тал засучи́в рукава́, поэ́тому ничего́ не сде́лал.",
        "explanation": "<p>Maʼno qarama-qarshi: <em>засучи́в рукава́</em> — «jon-jahdi "
                       "bilan». Bu yerda <strong>спустя́ рукава́</strong> boʻlishi kerak "
                       "edi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "Iboralarni soʻzma-soʻz tarjima qilish kerak.",
            "Iboradagi soʻzlarni erkin almashtirish mumkin.",
            "«Ни пу́ха ни пера́!» ga «спаси́бо» deb javob beriladi.",
            "Iboralar arizada va ilmiy matnda ishlatilmaydi.",
        ],
        "correct": "Iboralar arizada va ilmiy matnda ishlatilmaydi.",
        "explanation": "<p>Qolgan uchtasi xato: ibora shakli qotib qolgan; javob faqat <em>«К"
                       " чёрту!»</em>; iborani tarjima qilmasdan <strong>juftini</strong> "
                       "topish kerak.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— За́втра у меня́ "
                "экза́мен.</strong></p><p><strong>— ___</strong></p>",
        "choices": [
            "Ни пу́ха ни пера́!",
            "Как с гу́ся вода́!",
            "Семь пя́тниц на неде́ле!",
            "У чёрта на кули́чках!",
        ],
        "correct": "Ни пу́ха ни пера́!",
        "explanation": "<p>Imtihon, suhbat yoki muhim ish oldidan aytiladigan omad tilash. "
                       "Javobi esa har doim bitta: <strong>«К чёрту!»</strong></p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega <em>засучи́в рукава́</em>, "
                "<em>сиде́ть сложа́ ру́ки</em> va <em>держа́ть язы́к за зуба́ми</em> "
                "oʻzbekchaga soʻzma-soʻz tushadi?</p>",
        "choices": [
            "Ular oʻzbek tilidan olingan",
            "Ular rus tilidan oʻzbekchaga tarjima qilingan",
            "Bu tasodif",
            "Ular tana va mehnat obraziga tayanadi — bunday obrazlar koʻp tilda bir xil",
        ],
        "correct": "Ular tana va mehnat obraziga tayanadi — bunday obrazlar koʻp tilda bir xil",
        "explanation": "<p>Yeng, qoʻl, til — odam hamma joyda bir xil ishlaydi, shuning uchun"
                       " obraz ham bir xil chiqadi. Lekin <strong>koʻpchilik iboralar mos "
                       "tushmaydi</strong>.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-92 Mashq: Telefon, elektron pochta va xabar tili",
        "description": (
            "Telefon qoliplari, «вы не туда попали», elektron xatning uch "
            "darajasi, chat qisqartmalari va chatdagi nuqta qoidasi."
        ),
        "tutorial": "PR-92:",
        "questions": Q_PR92,
    },
    {
        "title": "PR-93 Mashq: Ish va oʻqish leksikasi",
        "description": (
            "Сдава́ть = topshirmoq, сдать = oʻtmoq. Rezyume qismlari, tajriba "
            "feʼllari kelishigi bilan va собеседование savollari."
        ),
        "tutorial": "PR-93:",
        "questions": Q_PR93,
    },
    {
        "title": "PR-94 Mashq: Фразеологизмы",
        "description": (
            "Iboralarning ichki mantigʻi: баклуши, нос — hisob taxtachasi, "
            "uzun yeng. Uchta ibora oʻzbekchaga soʻzma-soʻz tushadi."
        ),
        "tutorial": "PR-94:",
        "questions": Q_PR94,
    },
]
