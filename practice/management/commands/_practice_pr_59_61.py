# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-59 … PR-61.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_59_61.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Russian",
    "description": "Rus tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#b91c1c",
}

DEFAULTS = {
    "level":                "medium",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PR-59 — Buyruq mayli
# =====================================================================

Q_PR59 = [
    # 1–5 tanish
    {
        "text": "<p>Buyruq shakli qaysi shakldan yasaladi?</p>",
        "choices": ["Infinitivdan", "«Я» shaklidan", "«Они́» shaklidan", "Oʻtgan zamondan"],
        "correct": "«Они́» shaklidan",
        "explanation": "<p><em>чита́<strong>ют</strong> → чита́й</em>, "
                       "<em>говор<strong>я́т</strong> → говори́</em>. Qoʻshimcha olib "
                       "tashlanadi va -Й / -И / -Ь qoʻyiladi.</p>",
    },
    {
        "text": "<p><strong>де́лать</strong> feʼlining buyruq shakli qaysi?</p>",
        "choices": ["де́лай", "де́ли", "делай́те", "де́лать"],
        "correct": "де́лай",
        "explanation": "<p>«Они́» shakli <em>де́лают</em>, oʻzak <em>де́ла-</em> unli "
                       "bilan tugaydi — demak <strong>-Й</strong>.</p>",
    },
    {
        "text": "<p><strong>писа́ть</strong> feʼlining buyruq shakli qaysi?</p>",
        "choices": ["пиша́й", "пи́шь", "пиши́", "пи́шите"],
        "correct": "пиши́",
        "explanation": "<p>Oʻzak <em>пиш-</em> undosh bilan; «я» shaklida urgʻu "
                       "qoʻshimchada (<em>пишу́</em>) — demak <strong>-И</strong>.</p>",
    },
    {
        "text": "<p>Inkor buyruqda qaysi vid ishlatiladi?</p>",
        "choices": ["СВ", "НСВ", "Ikkalasi teng", "Farqi yoʻq"],
        "correct": "НСВ",
        "explanation": "<p><em>Не чита́й, не де́лай, не опа́здывай</em> — taqiq. СВ "
                       "bilan bu <strong>ogohlantirish</strong> boʻlardi: <em>не "
                       "упади́!</em></p>",
    },
    {
        "text": "<p><strong>е́хать</strong> feʼlining buyruq shakli qaysi?</p>",
        "choices": ["е́хай", "е́зди", "поезжа́й", "е́дь"],
        "correct": "поезжа́й",
        "explanation": "<p><em>«Е́хай»</em> degan shakl rus tilida <strong>yoʻq</strong>. "
                       "Buyruq <em>-езжа́й</em> dan yasaladi: <strong>поезжа́й, "
                       "поезжа́йте</strong>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ мне пра́вду.</strong> "
                "(сказа́ть, «ayt» maʼnosida)</p>",
        "choices": ["Говори́", "Скажи́", "Сказа́й", "Ска́жь"],
        "correct": "Скажи́",
        "explanation": "<p>«Они́» shakli <em>ска́жут</em>, oʻzak <em>скаж-</em>; «я» "
                       "shaklida urgʻu qoʻshimchada (<em>скажу́</em>) — demak "
                       "<strong>-И</strong>. Va aniq vazifa, demak СВ.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Не ___ э́ту "
                "кни́гу!</strong></p>",
        "choices": ["прочита́й", "чита́й", "прочита́йте", "чита́ть"],
        "correct": "чита́й",
        "explanation": "<p>Inkor buyruqda <strong>НСВ</strong>. <em>Не прочита́й</em> "
                       "boshqa maʼno berardi — ogohlantirish.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ пря́мо, пото́м "
                "напра́во.</strong> (идти́, «boring» maʼnosida)</p>",
        "choices": ["Иди́те", "Ходи́те", "Идти́те", "Пойди́те"],
        "correct": "Иди́те",
        "explanation": "<p>«Они́» shakli <em>иду́т</em>, oʻzak <em>ид-</em>, urgʻu "
                       "qoʻshimchada — <strong>иди́</strong>, va ВЫ uchun "
                       "<strong>-те</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ начнём!</strong></p>",
        "choices": ["Дава́й", "Дава́йте", "Да́й", "Дава́ть"],
        "correct": "Дава́йте",
        "explanation": "<p><em>Дава́йте начнём</em> — «boshlaylik», hurmat yoki "
                       "koʻplik shakli. Yaqin doirada <em>дава́й начнём</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ добры́, "
                "помоги́те.</strong> (быть)</p>",
        "choices": ["Будь", "Бу́дьте", "Бу́дете", "Быть"],
        "correct": "Бу́дьте",
        "explanation": "<p><em>Бу́дьте добры́</em> — muloyim soʻrovning tayyor "
                       "iborasi. <em>Быть</em> ning buyrugʻi: <strong>будь · "
                       "бу́дьте</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ ка́ждый день — и "
                "уви́дишь результа́т.</strong></p>",
        "choices": ["Прочита́й", "Чита́й", "Прочита́йте", "Чита́ть"],
        "correct": "Чита́й",
        "explanation": "<p>«Ка́ждый день» — takror va umumiy maslahat, demak "
                       "<strong>НСВ</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ ча́шку по́сле "
                "себя́.</strong> (помы́ть)</p>",
        "choices": ["Мо́йте", "Помо́йте", "Помы́ть", "Помы́йте"],
        "correct": "Помо́йте",
        "explanation": "<p>«Они́» shakli <em>помо́ют</em>, oʻzak <em>помо́-</em> unli "
                       "bilan — demak <strong>-Й</strong>: <em>помо́й, "
                       "помо́йте</em>. Aniq vazifa, demak СВ.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki buyruqning farqi nima?</p><p><strong>Не де́лай э́то! · "
                "Не сде́лай оши́бку!</strong></p>",
        "choices": ["Taqiq · ogohlantirish", "Ogohlantirish · taqiq",
                    "Ikkalasi bir xil", "Ikkinchisi xato"],
        "correct": "Taqiq · ogohlantirish",
        "explanation": "<p>Inkor buyruqda НСВ — <b>taqiq</b> («buni qilma»), СВ esa "
                       "<b>ogohlantirish</b> («xato qilib qoʻyma, ehtiyot "
                       "boʻl»).</p>",
    },
    {
        "text": "<p>Bu ikki buyruqning farqi nima?</p><p><strong>Чита́й! · "
                "Прочита́й э́то!</strong></p>",
        "choices": ["Umumiy taklif · aniq vazifa", "Aniq vazifa · umumiy taklif",
                    "Ikkalasi bir xil", "Birinchisi hurmat shakli"],
        "correct": "Umumiy taklif · aniq vazifa",
        "explanation": "<p>НСВ — takror, odat, umumiy maslahat. СВ — bir marta, "
                       "aniq natija kutilyapti.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida buyruqning hurmat shakli qanday yasaladi?</p>",
        "choices": ["-ng qoʻshimchasi bilan: oʻqing",
                    "Alohida feʼl bilan", "Yasalmaydi", "Ohang bilan"],
        "correct": "-ng qoʻshimchasi bilan: oʻqing",
        "explanation": "<p><em>oʻqi → oʻqi<strong>ng</strong></em>, ruschada esa "
                       "<em>чита́й → чита́й<strong>те</strong></em>. Ikkala tilda ham "
                       "bir xil tizim, faqat qoʻshimcha boshqa.</p>",
    },
    {
        "text": "<p>Oʻzak undosh bilan tugasa va urgʻu <strong>oʻzakda</strong> "
                "boʻlsa, qaysi qoʻshimcha qoʻyiladi?</p>",
        "choices": ["-Й", "-И", "-Ь", "-ТЕ"],
        "correct": "-Ь",
        "explanation": "<p><em>гото́вят → готовь</em>, <em>отве́тят → отве́ть</em>. "
                       "Urgʻu qoʻshimchada boʻlsa esa <strong>-И</strong>: "
                       "<em>говори́</em>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Иди́те пря́мо.", "Дава́йте начнём.",
                    "Е́хай в Москву́!", "Не опа́здывай."],
        "correct": "Е́хай в Москву́!",
        "explanation": "<p>Toʻgʻrisi — <strong>Поезжа́й в Москву́</strong>. "
                       "<em>Е́хать</em> ning buyruq shakli alohida.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Чита́ть э́ту страни́цу!", "Прочита́й э́ту страни́цу!",
                    "Прочита́ть э́ту страни́цу!", "Чита́ешь э́ту страни́цу!"],
        "correct": "Прочита́й э́ту страни́цу!",
        "explanation": "<p>Infinitiv buyruq emas. Aniq vazifa — СВ buyruq shakli: "
                       "<strong>прочита́й</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Мо́жно войти́?</strong></p>",
        "choices": ["— Заходи́те, пожа́луйста.", "— Войди́те ка́ждый день.",
                    "— Не входи́те, пожа́луйста.", "— Входи́ть, пожа́луйста."],
        "correct": "— Заходи́те, пожа́луйста.",
        "explanation": "<p><em>Заходи́те!</em> — НСВ buyruq, taklif va xushmuomalalik "
                       "maʼnosida. Bu rus tilidagi standart javob.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Kechikmang va kalitni "
                "yoʻqotmang.</strong></p>",
        "choices": ["Не опозда́йте и не потеря́йте ключ.",
                    "Не опа́здывайте и не теря́йте ключ.",
                    "Опа́здывайте и теря́йте ключ.",
                    "Не опа́здывать и не теря́ть ключ."],
        "correct": "Не опа́здывайте и не теря́йте ключ.",
        "explanation": "<p>Ikkala inkor buyruq ham <strong>НСВ</strong> — bu taqiq. "
                       "Va ВЫ shakli <strong>-те</strong> bilan.</p>",
    },
]


# =====================================================================
# PR-60 — Shartli mayl (бы)
# =====================================================================

Q_PR60 = [
    # 1–5 tanish
    {
        "text": "<p>Shartli mayl qanday yasaladi?</p>",
        "choices": ["Hozirgi zamon + бы", "Oʻtgan zamon + бы",
                    "Infinitiv + бы", "Kelasi zamon + бы"],
        "correct": "Oʻtgan zamon + бы",
        "explanation": "<p>Butun qoida shu. Tuslanish yoʻq, zamon yoʻq. Shakl faqat "
                       "jinsga qaraydi, chunki u oʻtgan zamon.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Е́сли бы я ___, я бы "
                "сказа́л.</strong> (знать)</p>",
        "choices": ["зна́ю", "знал", "бу́ду знать", "знать"],
        "correct": "знал",
        "explanation": "<p><em>Бы</em> faqat oʻtgan zamon bilan ishlaydi. <em>«Е́сли "
                       "бы я зна́ю»</em> — xato.</p>",
    },
    {
        "text": "<p>Noreal shart gapida <strong>бы</strong> nechta qismda "
                "boʻladi?</p>",
        "choices": ["Faqat birinchisida", "Faqat ikkinchisida",
                    "Ikkala qismda ham", "Hech qaysisida"],
        "correct": "Ikkala qismda ham",
        "explanation": "<p><em><strong>Е́сли бы</strong> я знал, я <strong>бы</strong> "
                       "сказа́л.</em> Birinchisida <em>е́сли бы</em>, ikkinchisida "
                       "yolgʻiz <em>бы</em>.</p>",
    },
    {
        "text": "<p>«Kofe xohlardim» ruschada qanday boʻladi?</p>",
        "choices": ["Я бы хочу́ ко́фе.", "Я хоте́л бы ко́фе.",
                    "Я хочу́ бы ко́фе.", "Я бу́ду хоте́ть ко́фе."],
        "correct": "Я хоте́л бы ко́фе.",
        "explanation": "<p><strong>Я хоте́л бы</strong> — muloyim soʻrovning standart "
                       "shakli (ayol kishi: <em>я хоте́ла бы</em>). Restoran va "
                       "doʻkonda har kuni kerak.</p>",
    },
    {
        "text": "<p><strong>Е́сли</strong> va <strong>е́сли бы</strong> — farqi "
                "nima?</p>",
        "choices": ["Haqiqiy shart · noreal shart", "Noreal · haqiqiy",
                    "Ikkalasi bir xil", "Birinchisi kelasi zamon uchun emas"],
        "correct": "Haqiqiy shart · noreal shart",
        "explanation": "<p><em>Е́сли я узна́ю, я скажу́</em> — hali boʻlishi mumkin. "
                       "<em>Е́сли бы я знал, я бы сказа́л</em> — bilmadim, "
                       "aytmadim.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Е́сли бы я знал, я ___ "
                "помо́г.</strong></p>",
        "choices": ["бы", "не", "уже́", "то́же"],
        "correct": "бы",
        "explanation": "<p>Ikkinchi qismda ham <strong>бы</strong> kerak — bu shart "
                       "gapining majburiy qismi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>На твоём ме́сте я бы не "
                "___.</strong> (пойти́)</p>",
        "choices": ["пойду́", "пошёл", "иду́", "идти́"],
        "correct": "пошёл",
        "explanation": "<p><em>Бы</em> oʻtgan zamon bilan: <strong>пошёл</strong>. "
                       "«На твоём ме́сте» — maslahat berishning muloyim yoʻli.</p>",
    },
    {
        "text": "<p>Bu gapni muloyimroq qiling.</p><p><strong>Вы помо́жете?</strong></p>",
        "choices": ["Вы помо́жете бы?", "Вы не помогли́ бы?",
                    "Вы бы помо́жете?", "Вы помога́ете бы?"],
        "correct": "Вы не помогли́ бы?",
        "explanation": "<p>Oʻtgan zamon + <em>бы</em> soʻrovni ancha muloyim qiladi. "
                       "Inkor shakli esa yanada muloyimroq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Что бы ты "
                "___?</strong> (сде́лать)</p>",
        "choices": ["сде́лаешь", "сде́лал", "де́лаешь", "сде́лать"],
        "correct": "сде́лал",
        "explanation": "<p><em>Что бы ты сде́лал?</em> — «sen nima qilarding?». "
                       "<em>Бы</em> har doim oʻtgan zamon bilan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ за́втра бу́дет "
                "дождь, мы не пойдём.</strong></p>",
        "choices": ["Е́сли бы", "Е́сли", "Бы", "Что́бы"],
        "correct": "Е́сли",
        "explanation": "<p>Bu <strong>haqiqiy</strong> shart — ertaga hali boʻlishi "
                       "mumkin. Demak oddiy zamonlar va <em>бы</em> siz.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ ко́фе, "
                "пожа́луйста.</strong> (ayol kishi gapiryapti)</p>",
        "choices": ["хоте́л бы", "хоте́ла бы", "хочу́ бы", "бы хочу́"],
        "correct": "хоте́ла бы",
        "explanation": "<p>Shakl oʻtgan zamon boʻlgani uchun <strong>jinsga "
                       "qaraydi</strong>: erkak <em>хоте́л бы</em>, ayol <em>хоте́ла "
                       "бы</em>.</p>",
    },
    {
        "text": "<p><strong>бы</strong> gapda qayerda turadi?</p>",
        "choices": ["Faqat gap oxirida", "Faqat gap boshida",
                    "Feʼldan keyin yoki birinchi urgʻuli soʻzdan keyin",
                    "Faqat feʼldan oldin"],
        "correct": "Feʼldan keyin yoki birinchi urgʻuli soʻzdan keyin",
        "explanation": "<p><em>Я <strong>бы</strong> сказа́л</em> va <em>Я сказа́л "
                       "<strong>бы</strong></em> — ikkalasi ham toʻgʻri. Joyi "
                       "erkin.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Е́сли я узна́ю, я "
                "скажу́. · Е́сли бы я знал, я бы сказа́л.</strong></p>",
        "choices": ["Hali boʻlishi mumkin · boʻlmadi",
                    "Boʻlmadi · hali boʻlishi mumkin",
                    "Ikkalasi bir xil", "Ikkinchisi xato"],
        "correct": "Hali boʻlishi mumkin · boʻlmadi",
        "explanation": "<p>Birinchisi — kelajakka ochiq haqiqiy shart. Ikkinchisi — "
                       "oʻtmish haqida: bilmadim, shuning uchun aytmadim.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida shart mayli qanday beriladi?</p>",
        "choices": ["Bir necha shakl bilan: -sa, -ganda, -sa edi, -ardi",
                    "Faqat bitta shakl bilan", "Berilmaydi", "Faqat ohang bilan"],
        "correct": "Bir necha shakl bilan: -sa, -ganda, -sa edi, -ardi",
        "explanation": "<p>Oʻzbekchada bir necha shakl bor, ruschada esa bittasi — "
                       "<em>oʻtgan zamon + бы</em>. <strong>Bu safar ruscha "
                       "osonroq.</strong></p>",
    },
    {
        "text": "<p>Shartli mayl shakli nimaga qaraydi?</p>",
        "choices": ["Shaxsga", "Zamonga", "Jinsga va songa", "Hech narsaga"],
        "correct": "Jinsga va songa",
        "explanation": "<p>Chunki u oʻtgan zamon: <em>сказа́л бы / сказа́ла бы / "
                       "сказа́ли бы</em>. Shaxs va zamon koʻrsatilmaydi.</p>",
    },
    {
        "text": "<p>«На твоём ме́сте я бы…» iborasi nima uchun ishlatiladi?</p>",
        "choices": ["Maslahat berish uchun — buyruqdan muloyimroq",
                    "Buyruq berish uchun", "Savol berish uchun", "Rad etish uchun"],
        "correct": "Maslahat berish uchun — buyruqdan muloyimroq",
        "explanation": "<p><em>На твоём ме́сте я бы не пошёл</em> — «sening oʻrningda "
                       "boʻlsam, bormasdim». Bu buyruq emas, shuning uchun ancha "
                       "yumshoq. Rasmiy shakli: <em>на ва́шем ме́сте</em>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я бы не сказа́л.", "Е́сли бы я знал, я бы помо́г.",
                    "Я бы хочу́ ко́фе.", "На ва́шем ме́сте я бы подожда́л."],
        "correct": "Я бы хочу́ ко́фе.",
        "explanation": "<p>Toʻgʻrisi — <strong>Я хоте́л бы ко́фе</strong>. <em>Бы</em> "
                       "hozirgi zamon bilan ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Е́сли бы я знал, я сказа́л.", "Е́сли я знал, я бы сказа́л.",
                    "Е́сли бы я знал, я бы сказа́л.", "Е́сли бы я зна́ю, я бы сказа́л."],
        "correct": "Е́сли бы я знал, я бы сказа́л.",
        "explanation": "<p>Ikkala qismda ham <strong>бы</strong>, va ikkalasida ham "
                       "<strong>oʻtgan zamon</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Что мне де́лать?</strong></p>",
        "choices": ["— На твоём ме́сте я бы подожда́л.",
                    "— На твоём ме́сте я бы подожду́.",
                    "— На твоём ме́сте я подожда́л.",
                    "— На твоём ме́сте бы я жду."],
        "correct": "— На твоём ме́сте я бы подожда́л.",
        "explanation": "<p>Maslahat — <em>на твоём ме́сте</em> + <em>бы</em> + oʻtgan "
                       "zamon. Bu buyruqdan ancha muloyim.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Bilganimda "
                "aytardim.</strong></p>",
        "choices": ["Е́сли я зна́ю, я скажу́.", "Е́сли бы я знал, я бы сказа́л.",
                    "Е́сли бы я зна́ю, я бы сказа́л.", "Е́сли я знал, я сказа́л."],
        "correct": "Е́сли бы я знал, я бы сказа́л.",
        "explanation": "<p>Oʻzbekcha «bilganimda» noreal shartni bildiradi, demak "
                       "<strong>е́сли бы</strong> + oʻtgan zamon, va ikkinchi qismda "
                       "ham <strong>бы</strong>.</p>",
    },
]


# =====================================================================
# PR-61 — Majhul nisbat
# =====================================================================

Q_PR61 = [
    # 1–5 tanish
    {
        "text": "<p>Rus tilida majhul nisbatning nechta shakli bor?</p>",
        "choices": ["Bitta", "Ikkita", "Uchta", "Toʻrtta"],
        "correct": "Ikkita",
        "explanation": "<p><strong>-ся</strong> bilan (jarayon, НСВ — <em>дом "
                       "стро́ится</em>) va <strong>qisqa sifatdosh</strong> bilan "
                       "(natija, СВ — <em>дом постро́ен</em>).</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Дом стро́ится. · Дом "
                "постро́ен.</strong></p>",
        "choices": ["Jarayon · natija", "Natija · jarayon",
                    "Ikkalasi bir xil", "Birinchisi kelasi zamon"],
        "correct": "Jarayon · natija",
        "explanation": "<p>Bu PR-51 dagi vid farqining majhul nisbatdagi koʻrinishi: "
                       "qurilyapti ↔ qurilgan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Дверь ___.</strong> "
                "(закры́ть)</p>",
        "choices": ["закры́т", "закры́та", "закры́то", "закры́ты"],
        "correct": "закры́та",
        "explanation": "<p>Qisqa sifatdosh egaga moslashadi, <em>дверь</em> esa "
                       "<strong>ayol jinsida</strong>.</p>",
    },
    {
        "text": "<p>Bajaruvchi (kim qilgani) qaysi kelishikda boʻladi?</p>",
        "choices": ["Роди́тельный", "Да́тельный", "Твори́тельный", "Предло́жный"],
        "correct": "Твори́тельный",
        "explanation": "<p><em>Дом постро́ен <strong>рабо́чими</strong></em>. "
                       "Oʻzbekchada bu «ishchilar <b>tomonidan</b>» boʻlardi — "
                       "alohida soʻz bilan.</p>",
    },
    {
        "text": "<p>Majhul nisbatning <strong>-ся</strong> shakli qaysi shaxsda "
                "ishlaydi?</p>",
        "choices": ["Faqat birinchi shaxsda", "Faqat uchinchi shaxsda",
                    "Hamma shaxsda", "Faqat koʻplikda"],
        "correct": "Faqat uchinchi shaxsda",
        "explanation": "<p><em>Стро́ится, стро́ятся</em>. <em>«Я строюсь»</em> majhul "
                       "nisbat emas. Va bu shakl faqat <strong>НСВ</strong> "
                       "feʼllardan yasaladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Кни́га ___ "
                "Толсты́м.</strong> (написа́ть)</p>",
        "choices": ["напи́сан", "напи́сана", "напи́сано", "напи́саны"],
        "correct": "напи́сана",
        "explanation": "<p><em>Кни́га</em> — ayol jinsida, demak "
                       "<strong>напи́сана</strong>. Va bajaruvchi Твори́тельный'da: "
                       "<em>Толсты́м</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ключи́ ___.</strong> "
                "(найти́)</p>",
        "choices": ["на́йден", "на́йдена", "на́йдено", "на́йдены"],
        "correct": "на́йдены",
        "explanation": "<p><em>Ключи́</em> — koʻplik, demak "
                       "<strong>на́йдены</strong>.</p>",
    },
    {
        "text": "<p>Bu gapni oʻtgan zamonga oʻtkazing.</p><p><strong>Дом "
                "постро́ен.</strong></p>",
        "choices": ["Дом постро́ился.", "Дом был постро́ен.",
                    "Дом бу́дет постро́ен.", "Дом стро́ился."],
        "correct": "Дом был постро́ен.",
        "explanation": "<p><em>Быть</em> odatdagidek ishlaydi: hozirgi zamonda "
                       "aytilmaydi, oʻtgan va kelasi zamonda paydo boʻladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Го́род ___ мно́го "
                "лет.</strong> («qurilgan edi, jarayon» maʼnosida)</p>",
        "choices": ["постро́ен", "стро́ился", "был постро́ен", "стро́ит"],
        "correct": "стро́ился",
        "explanation": "<p>«Мно́го лет» — davomiylik, jarayon. Demak "
                       "<strong>-ся</strong> shakli, НСВ.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Магази́н ___ в "
                "де́вять.</strong> (откры́ть, «ochiladi» maʼnosida)</p>",
        "choices": ["откры́т", "открыва́ется", "откры́та", "откры́то"],
        "correct": "открыва́ется",
        "explanation": "<p>Har kuni takrorlanadigan harakat — jarayon, demak "
                       "<strong>-ся</strong> shakli. <em>Откры́т</em> «hozir ochiq» "
                       "degan holatni bildirardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Петербу́рг ___ в 1703 "
                "году́.</strong> (основа́ть)</p>",
        "choices": ["осно́ван", "был осно́ван", "основа́лся", "осно́вана"],
        "correct": "был осно́ван",
        "explanation": "<p>Aniq oʻtgan sana bor, demak <em>быть</em> kerak: "
                       "<strong>был осно́ван</strong>. <em>Петербу́рг</em> erkak "
                       "jinsida.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Всё ___.</strong> "
                "(сде́лать, «hammasi bajarildi»)</p>",
        "choices": ["сде́лан", "сде́лана", "сде́лано", "сде́ланы"],
        "correct": "сде́лано",
        "explanation": "<p><em>Всё</em> — oʻrta jins, demak "
                       "<strong>сде́лано</strong>. Bu juda koʻp ishlatiladigan "
                       "ibora.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qisqa sifatdosh nimaga moslashadi?</p>",
        "choices": ["Bajaruvchiga", "Egaga — jins va son boʻyicha",
                    "Feʼlga", "Hech narsaga"],
        "correct": "Egaga — jins va son boʻyicha",
        "explanation": "<p><em>Магази́н закры́т · дверь закры́та · окно́ закры́то · "
                       "две́ри закры́ты</em>. U sifat kabi ishlaydi.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida majhul nisbat qanday yasaladi?</p>",
        "choices": ["-il- / -in- qoʻshimchasi bilan: qurildi, yozilgan",
                    "Alohida feʼl bilan", "Yasalmaydi", "Prefiks bilan"],
        "correct": "-il- / -in- qoʻshimchasi bilan: qurildi, yozilgan",
        "explanation": "<p>Va oʻzbekchada ham jarayon/natija ajratiladi: "
                       "<em>qurilyapti</em> → <em>стро́ится</em>, <em>qurilgan</em> → "
                       "<em>постро́ен</em>. Bir xil gʻoya.</p>",
    },
    {
        "text": "<p>Majhul nisbat nima uchun ishlatiladi?</p>",
        "choices": ["Kim qilgani muhim boʻlmaganda yoki nomaʼlum boʻlganda",
                    "Faqat oʻtgan zamon uchun",
                    "Faqat rasmiy tilda",
                    "Bajaruvchini taʼkidlash uchun"],
        "correct": "Kim qilgani muhim boʻlmaganda yoki nomaʼlum boʻlganda",
        "explanation": "<p>Shuning uchun eʼlonlar (<em>откры́то</em>), tarix "
                       "(<em>был осно́ван</em>) va xabarlarda koʻp uchraydi — u yerda "
                       "faktning oʻzi muhim.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Магази́н "
                "открыва́ется в де́вять. · Магази́н откры́т.</strong></p>",
        "choices": ["Har kuni ochiladi · hozir ochiq",
                    "Hozir ochiq · har kuni ochiladi",
                    "Ikkalasi bir xil", "Ikkinchisi xato"],
        "correct": "Har kuni ochiladi · hozir ochiq",
        "explanation": "<p>Birinchisi — takrorlanadigan jarayon (НСВ + -ся). "
                       "Ikkinchisi — hozirgi holat, natija (qisqa sifatdosh).</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Магази́н закры́т.", "Кни́га напи́сана Толсты́м.",
                    "Дверь закры́т.", "Ключи́ на́йдены."],
        "correct": "Дверь закры́т.",
        "explanation": "<p>Toʻgʻrisi — <strong>Дверь закры́та</strong>. "
                       "<em>Дверь</em> ayol jinsida, va qisqa sifatdosh egaga "
                       "moslashadi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Дом стро́ится рабо́чих.", "Дом стро́ится рабо́чими.",
                    "Дом стро́ится рабо́чим.", "Дом стро́ится рабо́чие."],
        "correct": "Дом стро́ится рабо́чими.",
        "explanation": "<p>Bajaruvchi <strong>Твори́тельный</strong>'da, va koʻplikda "
                       "<strong>-ими</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Магази́н рабо́тает?</strong></p>",
        "choices": ["— Нет, закры́т.", "— Нет, закры́та.",
                    "— Нет, закры́ты.", "— Нет, закрыва́ю."],
        "correct": "— Нет, закры́т.",
        "explanation": "<p><em>Магази́н</em> — erkak jinsida, demak "
                       "<strong>закры́т</strong>. Bu eng koʻp uchraydigan qisqa "
                       "javoblardan biri.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Uy ishchilar tomonidan "
                "qurilgan.</strong></p>",
        "choices": ["Дом стро́ится рабо́чими.", "Дом постро́ен рабо́чими.",
                    "Дом постро́ен рабо́чих.", "Дом построи́лся рабо́чими."],
        "correct": "Дом постро́ен рабо́чими.",
        "explanation": "<p>«Qurilgan» — natija, demak <strong>qisqa "
                       "sifatdosh</strong>. «Tomonidan» — ruschada alohida soʻz emas, "
                       "<strong>Твори́тельный</strong> kelishigi.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-59 Mashq: Buyruq mayli: читай! читайте! давай пойдём! не опаздывай!",
        "description": (
            "«Они́» shaklidan -Й / -И / -Ь; ВЫ shakli -ТЕ; НСВ umumiy taklif ↔ СВ "
            "aniq vazifa; inkor buyruqda НСВ."
        ),
        "tutorial": "PR-59:",
        "questions": Q_PR59,
    },
    {
        "title": "PR-60 Mashq: Shartli mayl — бы: если бы, я хотел бы, на твоём месте я бы…",
        "description": (
            "Oʻtgan zamon + БЫ. Е́сли бы …, … бы — ikkala qismda ham. Muloyim "
            "soʻrov «я хоте́л бы» va maslahat «на твоём ме́сте»."
        ),
        "tutorial": "PR-60:",
        "questions": Q_PR60,
    },
    {
        "title": "PR-61 Mashq: Majhul nisbat: дом строится / дом построен",
        "description": (
            "Ikki shakl: -ся (jarayon) va qisqa sifatdosh (natija). Egaga "
            "moslashish, zamon «быть» bilan, bajaruvchi Твори́тельный'da."
        ),
        "tutorial": "PR-61:",
        "questions": Q_PR61,
    },
]
