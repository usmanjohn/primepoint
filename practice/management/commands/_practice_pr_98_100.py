# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-98 … PR-100. KURSNING OXIRGI MASHQLARI.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
PR-100 mashqi — yakuniy takror: savollar butun kurs boʻylab tarqalgan
(alifbo, kelishik, feʼl turi, sifatdosh, uslub, tinish belgisi).
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_98_100.py --master=prime \\
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
# PR-98 — Matn qurish
# =====================================================================

Q_PR98 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Insho qaysi uch qismdan iborat?</p>",
        "choices": [
            "Вступле́ние — основна́я часть — заключе́ние",
            "Нача́ло — середи́на — коне́ц",
            "Вопро́с — отве́т — вы́вод",
            "Те́зис — аргуме́нт — цита́та",
        ],
        "correct": "Вступле́ние — основна́я часть — заключе́ние",
        "explanation": "<p>Oʻzbekcha <em>kirish — asosiy qism — xulosa</em> bilan aynan bir "
                       "xil. Siz arxitekturani bilasiz — sizga faqat ruscha bogʻlovchilar "
                       "kerak edi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Те́зис</strong> nima?</p>",
        "choices": [
            "Kirishdagi asosiy fikringiz",
            "Ikkinchi abzats",
            "Dalilga misol",
            "Xulosadagi maqol",
        ],
        "correct": "Kirishdagi asosiy fikringiz",
        "explanation": "<p>Тезис kirishda aytiladi, asosiy qismda <strong>аргументы</strong> "
                       "bilan isbotlanadi, xulosada esa <strong>вывод</strong> boʻlib "
                       "qaytadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Таки́м о́бразом…</strong> "
                "inshoning qaysi qismida turadi?</p>",
        "choices": ["Kirishda", "Birinchi dalilda", "Qarshi fikrda", "Xulosada"],
        "correct": "Xulosada",
        "explanation": "<p><em>Таки́м о́бразом…</em> va <em>Подводя́ ито́г…</em> — xulosa "
                       "bogʻlovchilari. Kirish uchun <em>На мой взгляд…</em>, dalil uchun "
                       "<em>Во-пе́рвых…</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Abzats qoidasi qanday?</p>",
        "choices": [
            "Bir abzats — bir fikr",
            "Bir abzats — besh gap",
            "Har bir gap yangi abzatsdan",
            "Butun insho bitta abzats",
        ],
        "correct": "Bir abzats — bir fikr",
        "explanation": "<p>Tekshiruv: <strong>har bir abzatsni bitta jumlada aytib bera "
                       "olasizmi?</strong> Aytolmasangiz — abzatsda ikki fikr bor, uni "
                       "boʻling.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Во-пе́рвых</strong> dan keyin "
                "vergul qoʻyiladimi?</p>",
        "choices": ["Ha — bu kirish soʻz", "Yoʻq", "Faqat gap boshida", "Faqat uzun gapda"],
        "correct": "Ha — bu kirish soʻz",
        "explanation": "<p><em>Во-пе́рвых<strong>,</strong> э́то до́рого.</em> Xuddi shunday:"
                       " <em>кро́ме того́</em>, <em>таки́м о́бразом</em>, <em>наприме́р</em> "
                       "(PR-97).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu bogʻlovchi qaysi vazifani "
                "bajaradi?</p><p><strong>С друго́й стороны́…</strong></p>",
        "choices": ["Misol keltirish", "Qarshi fikrni kiritish", "Birinchi dalil", "Xulosa"],
        "correct": "Qarshi fikrni kiritish",
        "explanation": "<p>Qarshi fikr guruhida yana: <em>одна́ко</em>, <em>тем не "
                       "ме́нее</em>. Ular inshoni bir tomonlama boʻlishdan saqlaydi.</p>",
    },
    {
        "text": "<p>Vergulni toʻgʻri qoʻying.</p><p><strong>Одна́ко есть и друга́я "
                "сторона́.</strong></p>",
        "choices": [
            "Одна́ко, есть и друга́я сторона́.",
            "Одна́ко есть, и друга́я сторона́.",
            "Одна́ко есть и друга́я сторона́.",
            "Одна́ко, есть, и друга́я сторона́.",
        ],
        "correct": "Одна́ко есть и друга́я сторона́.",
        "explanation": "<p>Gap boshida <em>одна́ко</em> «lekin» degani va vergul "
                       "<strong>olmaydi</strong>. Gap oʻrtasida esa kirish soʻz boʻlib, ikki "
                       "tomondan vergul oladi (PR-97).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Xulosada nima qilish <strong>mumkin "
                "emas</strong>?</p>",
        "choices": [
            "Tezisga boshqa soʻzlar bilan qaytish",
            "Maqol bilan tugatish",
            "Savol bilan tugatish",
            "Yangi dalil qoʻshish",
        ],
        "correct": "Yangi dalil qoʻshish",
        "explanation": "<p>Dalillar asosiy qismda tugaydi. Xulosa faqat "
                       "<strong>yigʻadi</strong>. Yana ikki taqiq: kechirim soʻrash va "
                       "kirishni soʻzma-soʻz takrorlash.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu xulosada nima "
                "notoʻgʻri?</p><p><strong>Таки́м о́бразом, чита́ть поле́зно. Кро́ме того́, "
                "кни́ги сейча́с о́чень дороги́е.</strong></p>",
        "choices": [
            "Xulosaga yangi dalil qoʻshilgan",
            "«Таки́м о́бразом» notoʻgʻri ishlatilgan",
            "Juda qisqa",
            "Vergul yetishmayapti",
        ],
        "correct": "Xulosaga yangi dalil qoʻshilgan",
        "explanation": "<p>«Kitoblar qimmat» — butunlay yangi fikr. U asosiy qismda boʻlishi "
                       "kerak edi yoki umuman kerak emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Kirish nechta gapdan iborat boʻladi?</p>",
        "choices": ["Bitta", "2–3", "5–6", "Yarim bet"],
        "correct": "2–3",
        "explanation": "<p>Mavzuni ochish + <strong>тезис</strong>. Uzun kirish asosiy "
                       "qismdan joy oʻgʻirlaydi — baholovchi esa dalillarni qidiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu abzatsda nechta fikr "
                "bor?</p><p><strong>Спорт поле́зен для здоро́вья. Он у́чит дисципли́не. А ещё"
                " в на́шем го́роде ма́ло стадио́нов.</strong></p>",
        "choices": [
            "Bitta",
            "Ikkita — oxirgi gap boshqa mavzuda",
            "Uchta",
            "Hech qanday fikr yoʻq",
        ],
        "correct": "Ikkita — oxirgi gap boshqa mavzuda",
        "explanation": "<p>Birinchi ikki gap — sportning foydasi. Uchinchisi — shahardagi "
                       "sharoit. Uni <strong>alohida abzatsga</strong> chiqarish kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Yaxshi insho nimadan tugʻiladi?</p>",
        "choices": [
            "Qiyin grammatik qurilishlardan",
            "Uzun gaplardan",
            "Toʻgʻri tartib va bogʻlovchilardan",
            "Koʻp iboradan",
        ],
        "correct": "Toʻgʻri tartib va bogʻlovchilardan",
        "explanation": "<p>Darsdagi namuna insho PR-30 gacha oʻrganilgan bilim bilan "
                       "yozilgan. Oddiy yozing, lekin <strong>bogʻlab</strong> yozing.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi bogʻlovchi <strong>kirish</strong> "
                "uchun?</p>",
        "choices": [
            "Во-вторы́х…",
            "Подводя́ ито́г…",
            "Тем не ме́нее…",
            "Мно́гие счита́ют, что…",
        ],
        "correct": "Мно́гие счита́ют, что…",
        "explanation": "<p>Kirish uchun yana: <em>В на́ше вре́мя…</em>, <em>На мой "
                       "взгляд…</em>. Qolgan uchtasi asosiy qism yoki xulosa uchun.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Xulosani qanday kuchaytirish mumkin?</p>",
        "choices": [
            "Kechirim soʻrash bilan",
            "Yangi mavzu ochish bilan",
            "Maqol, savol yoki qisqa qatʼiy gap bilan",
            "Kirishni takrorlash bilan",
        ],
        "correct": "Maqol, savol yoki qisqa qatʼiy gap bilan",
        "explanation": "<p><em>Неда́ром говоря́т: век живи́ — век учи́сь</em> (PR-95) · <em>А"
                       " что вы́брали бы вы?</em> · <em>Вы́бор всегда́ остаётся за "
                       "на́ми.</em></p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "Во-пе́рвых, э́то до́рого.",
            "Во-пе́рвых э́то до́рого.",
            "Кро́ме того́, э́то до́лго.",
            "Таки́м о́бразом, вы́вод я́сен.",
        ],
        "correct": "Во-пе́рвых э́то до́рого.",
        "explanation": "<p>Kirish soʻzdan keyin <strong>vergul</strong> boʻlishi kerak: "
                       "<em>Во-пе́рвых, э́то до́рого.</em></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "Xulosa kirishni soʻzma-soʻz takrorlashi kerak.",
            "Bir abzatsda qancha fikr boʻlsa, shuncha yaxshi.",
            "Xulosa tezisga boshqa soʻzlar bilan qaytadi.",
            "«Одна́ко» gap boshida vergul oladi.",
        ],
        "correct": "Xulosa tezisga boshqa soʻzlar bilan qaytadi.",
        "explanation": "<p>Qolgan uchtasi xato: takror — aylanma; bir abzats — bir fikr; "
                       "<em>одна́ко</em> gap boshida vergulsiz.</p>",
    },
    {
        "text": "<p>Toʻgʻri kirishni tanlang.</p><p><strong>Mavzu: «Ну́жен ли шко́льнику "
                "телефо́н?»</strong></p>",
        "choices": [
            "Телефо́н — э́то пло́хо. Во-пе́рвых, он меша́ет.",
            "В на́ше вре́мя телефо́н есть почти́ у ка́ждого шко́льника. На мой взгляд, де́ло в том, как им по́льзоваться.",
            "Таки́м о́бразом, телефо́н ну́жен.",
            "Я не зна́ю, ну́жен и́ли нет.",
        ],
        "correct": "В на́ше вре́мя телефо́н есть почти́ у ка́ждого шко́льника. На мой взгляд,"
                   " де́ло в том, как им по́льзоваться.",
        "explanation": "<p>Mavzuni ochish + <strong>тезис</strong>. Birinchi variantda dalil "
                       "kirishga kirib ketgan, uchinchisi — xulosa, toʻrtinchisida tezis "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rus oʻqituvchisi ishni birinchi qarashda "
                "nimaga qarab baholaydi?</p>",
        "choices": [
            "Qoʻlyozma chiroyliligiga",
            "Uzunligiga",
            "Matn abzatslarga boʻlinganiga",
            "Qiyin soʻzlar soniga",
        ],
        "correct": "Matn abzatslarga boʻlinganiga",
        "explanation": "<p>Abzatslarga boʻlinmagan matn — fikr tartibga solinmaganining "
                       "birinchi belgisi. Bu grammatikadan oldin koʻzga tashlanadi.</p>",
    },
    {
        "text": "<p>Ushbu xulosani toʻgʻri tugating.</p><p><strong>Kirish: «Я счита́ю, что "
                "чита́ть ну́жно ка́ждый день.»</strong></p>",
        "choices": [
            "Ита́к, я счита́ю, что чита́ть ну́жно ка́ждый день.",
            "Кро́ме того́, кни́ги сейча́с дороги́е.",
            "Я, наве́рное, не о́чень хорошо́ объясни́л.",
            "Таки́м о́бразом, ежедне́вное чте́ние — э́то не привы́чка, а рабо́чий инструме́нт.",
        ],
        "correct": "Таки́м о́бразом, ежедне́вное чте́ние — э́то не привы́чка, а рабо́чий "
                   "инструме́нт.",
        "explanation": "<p>Oʻsha fikr, lekin <strong>boshqa soʻzlar</strong> bilan va "
                       "dalillardan chiqqan qoʻshimcha bilan. Qolgan uchtasi: takror, yangi "
                       "dalil, kechirim.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega bu dars oʻzbek oʻquvchi uchun oson?</p>",
        "choices": [
            "Chunki grammatika kerak emas",
            "Chunki rus inshosi qisqa boʻladi",
            "Chunki bogʻlovchilar oʻzbekchada ham bir xil",
            "Chunki insho arxitekturasi oʻzbekchada ham uch qismli",
        ],
        "correct": "Chunki insho arxitekturasi oʻzbekchada ham uch qismli",
        "explanation": "<p><em>Kirish — asosiy qism — xulosa</em> = <em>вступле́ние — "
                       "основна́я часть — заключе́ние</em>. Meʼmorchilik tayyor, faqat ruscha"
                       " gʻisht kerak edi.</p>",
    },
]


# =====================================================================
# PR-99 — Rus tilining qatlamlari
# =====================================================================

Q_PR99 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Здра́вствуйте»</strong> qaysi "
                "soʻzdan kelib chiqqan?</p>",
        "choices": ["здесь", "здоро́вье", "здра́вый смысл", "звать"],
        "correct": "здоро́вье",
        "explanation": "<p>Soʻzma-soʻz — «<strong>sogʻ boʻling</strong>». <em>Здоро́вье</em> "
                       "da <em>-оро-</em> (ruscha shakl), <em>здра́вствуйте</em> da "
                       "<em>-ра-</em> (kitobiy shakl).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>-ОРО- / -ОЛО- / -ЕРЕ-</strong> "
                "qanday shakl?</p>",
        "choices": [
            "Kitobiy shakl",
            "Ruscha shakl, maʼnosi aniq va moddiy",
            "Turkiy shakl",
            "Yevropa shakli",
        ],
        "correct": "Ruscha shakl, maʼnosi aniq va moddiy",
        "explanation": "<p><em>го́род, голова́, здоро́вье, бе́рег</em>. Kitobiy shakl esa "
                       "<strong>-РА- / -ЛА- / -РЕ-</strong> boʻladi va maʼnosi mavhum: "
                       "<em>град, глава́, здра́вствуйте, брег</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Каранда́ш»</strong> soʻzi "
                "qayerdan?</p>",
        "choices": [
            "Fransuz tilidan",
            "Yunon tilidan",
            "Turkiy tillardan — «qora tosh»",
            "Asl slavyan soʻzi",
        ],
        "correct": "Turkiy tillardan — «qora tosh»",
        "explanation": "<p><em>qora</em> + <em>tosh</em>: qadimgi qalam qora toshdan "
                       "yasalgan. Xuddi shunday turkiy: <em>изю́м</em> (uzum), "
                       "<em>сунду́к</em> (sandiq), <em>богаты́рь</em> (bahodir).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Богаты́рь»</strong> ning "
                "oʻzbekcha qarindoshi qaysi?</p>",
        "choices": ["boy", "bogʻbon", "bahodir", "botir emas, boshqa soʻz"],
        "correct": "bahodir",
        "explanation": "<p>Rus ertaklarining qahramoni <strong>turkiy nom</strong> bilan "
                       "yuradi. Bu — kursning PR-1 dagi vaʼdasining isboti: siz yuzlab ruscha"
                       " soʻzni allaqachon bilasiz.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rus tilining toʻrt qatlami qaysilar?</p>",
        "choices": [
            "Slavyan, turkiy, yunon-lotin, yevropa",
            "Slavyan, arab, xitoy, yevropa",
            "Faqat slavyan va yevropa",
            "Yunon, lotin, fransuz, ingliz",
        ],
        "correct": "Slavyan, turkiy, yunon-lotin, yevropa",
        "explanation": "<p>Slavyan — eng qadimiy (<em>мать, дом, хлеб</em>); turkiy — X–XV "
                       "asrlar; yunon-lotin — cherkov va fan; yevropa — XVIII asrdan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Глава́</strong> va "
                "<strong>голова́</strong> — maʼnolari qanday ajralgan?</p>",
        "choices": [
            "Farqi yoʻq, ikkalasi «bosh»",
            "Глава́ = bob, rahbar; голова́ = bosh (tana)",
            "Глава́ = tana, голова́ = bob",
            "Глава́ eskirgan, ishlatilmaydi",
        ],
        "correct": "Глава́ = bob, rahbar; голова́ = bosh (tana)",
        "explanation": "<p>Kitobiy shakl <strong>mavhum</strong> maʼno oldi, ruscha shakl "
                       "<strong>moddiy</strong>. Shuning uchun <s>он уда́рился главо́й</s> "
                       "kulgili chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri shaklni tanlang.</p><p><strong>___ содержа́ние кни́ги</strong> "
                "(qisqacha mazmun)</p>",
        "choices": ["Кра́ткое", "Коро́ткое", "Кра́ткий", "Коро́ткий"],
        "correct": "Кра́ткое",
        "explanation": "<p>Mazmun — <strong>mavhum</strong>, demak kitobiy shakl. Shim esa "
                       "moddiy: <em>коро́ткие брю́ки</em>. Jinsi ср.р., chunki "
                       "<em>содержа́ние</em> <em>-ение</em> bilan (PR-87).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega shahar nomlarida "
                "<strong>-град</strong> turibdi (Волгогра́д, Белгра́д)?</p>",
        "choices": [
            "Bu turkiy qatlamdan",
            "Bu qisqaroq",
            "Bu boshqa soʻz",
            "Chunki nom tantanali boʻlishi kerak — kitobiy shakl",
        ],
        "correct": "Chunki nom tantanali boʻlishi kerak — kitobiy shakl",
        "explanation": "<p>Kundalik nutqda <em>го́род</em>, tantanali nomda esa "
                       "<em>-град</em>. Bir soʻzning ikki shakli, ikki vazifa.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Изю́м</strong> soʻzining oʻzbekcha"
                " qarindoshi va maʼno farqi?</p>",
        "choices": [
            "«uzum» — ruschada maʼnosi torayib «mayiz» boʻlgan",
            "«uzum» — maʼnosi bir xil",
            "«tuz» — maʼnosi butunlay boshqa",
            "Qarindoshi yoʻq",
        ],
        "correct": "«uzum» — ruschada maʼnosi torayib «mayiz» boʻlgan",
        "explanation": "<p>Turkiy <em>uzum</em> = uzum; rus tilida esa <em>изю́м</em> faqat "
                       "quritilgan uzumni — mayizni — bildiradi. Oʻzlashma soʻzda maʼno "
                       "torayishi odatiy hodisa.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Pyotr I davrida rus tiliga koʻproq qaysi "
                "tillardan soʻz kirgan?</p>",
        "choices": [
            "Fransuz va italyan",
            "Golland va nemis",
            "Ingliz va ispan",
            "Turkiy va arab",
        ],
        "correct": "Golland va nemis",
        "explanation": "<p>Kema va harbiy ish sohasida: <em>матро́с, ко́мпас, флаг, шторм, "
                       "штраф</em>. Fransuz qatlami keyinroq — XVIII–XIX asr saroy va sanʼat "
                       "tili.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Вокза́л»</strong> soʻzi qayerdan "
                "kelgan?</p>",
        "choices": [
            "Turkiy tildan",
            "Nemischa «Bahnhof» dan",
            "Fransuzcha «voix» dan",
            "Londondagi Vauxhall bogʻining nomidan",
        ],
        "correct": "Londondagi Vauxhall bogʻining nomidan",
        "explanation": "<p>U yerda musiqa yangraydigan zal bor edi. Soʻz Rossiyada avval "
                       "«koʻngilochar zal», keyin «temiryoʻl bekati» maʼnosini olgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Зонт»</strong> soʻzi qanday paydo"
                " boʻlgan?</p>",
        "choices": [
            "Bu asl slavyan soʻzi",
            "Golland «zonnedek» dan toʻgʻridan-toʻgʻri",
            "«Зо́нтик» dan — ruslar «-ик» ni kichraytiruvchi deb oʻylashgan",
            "Fransuz tilidan",
        ],
        "correct": "«Зо́нтик» dan — ruslar «-ик» ni kichraytiruvchi deb oʻylashgan",
        "explanation": "<p>Golland <em>zonnedek</em> → <em>зо́нтик</em>. Keyin <em>-ик</em> "
                       "kichraytiruvchi suffiks (PR-88) deb hisoblanib, undan «katta» shakl "
                       "<em>зонт</em> yasalgan. Til xatoni qoidaga aylantirgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi soʻz <strong>turkiy qatlamdan "
                "emas</strong>?</p>",
        "choices": ["сунду́к", "база́р", "сара́й", "тетра́дь"],
        "correct": "тетра́дь",
        "explanation": "<p><em>Тетра́дь</em> — <strong>yunon</strong> tilidan "
                       "(<em>tetradion</em>). Qolgan uchtasi turkiy: sandiq, bozor, "
                       "saroy.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi juftlikda ruscha va kitobiy shakl "
                "toʻgʻri koʻrsatilgan?</p>",
        "choices": [
            "сторона́ / страна́",
            "страна́ / сторона́",
            "го́род / го́рода",
            "глава́ / гла́вный",
        ],
        "correct": "сторона́ / страна́",
        "explanation": "<p><em>Сторона́</em> — ruscha (<em>-оро-</em>), «tomon»; "
                       "<em>страна́</em> — kitobiy (<em>-ра-</em>), «mamlakat». Bitta oʻzak, "
                       "ikki taqdir.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Siz bu soʻzni koʻrmagansiz: "
                "<strong>здравоохране́ние</strong>. Maʼnosi?</p>",
        "choices": [
            "Kasalxona",
            "Salomlashish odobi",
            "Sogʻliqni saqlash",
            "Sogʻlom turmush tarzi",
        ],
        "correct": "Sogʻliqni saqlash",
        "explanation": "<p><em>здрав-</em> (← здоро́вье) + <em>о</em> + <em>охране́ние</em> "
                       "(← охраня́ть). Uch dars bir joyda: PR-86 (ikki oʻzak), PR-87 "
                       "(<em>-ение</em>) va PR-99 (kitobiy shakl).</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": [
            "Он уда́рился главо́й о дверь.",
            "Пе́рвая глава́ кни́ги о́чень дли́нная.",
            "Он уда́рился голово́й о дверь.",
            "Он — глава́ на́шей семьи́.",
        ],
        "correct": "Он уда́рился главо́й о дверь.",
        "explanation": "<p>Moddiy bosh haqida <strong>ruscha</strong> shakl ishlatiladi: "
                       "<em>голово́й</em>. <em>Глава́</em> faqat mavhum maʼnoda — bob yoki "
                       "rahbar.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": [
            "«Каранда́ш» — asl slavyan soʻzi.",
            "«Здра́вствуйте» ichida hech qanday maʼno yoʻq.",
            "Kitobiy shaklni har doim ishlatish mumkin.",
            "«-Ра-» li shakl mavhum, «-оро-» li shakl moddiy maʼno beradi.",
        ],
        "correct": "«-Ра-» li shakl mavhum, «-оро-» li shakl moddiy maʼno beradi.",
        "explanation": "<p>Qolgan uchtasi xato: <em>каранда́ш</em> turkiy; "
                       "<em>здра́вствуйте</em> = «sogʻ boʻling»; kitobiy shakl moddiy narsaga"
                       " toʻgʻri kelmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega oʻzbek oʻquvchida ingliz oʻquvchida "
                "yoʻq imkoniyat bor?</p>",
        "choices": [
            "Chunki rus tili oson",
            "Chunki oʻzbek tili slavyan tili",
            "Chunki rus tilida turkiy qatlam bor va u oʻzbekchaga tanish",
            "Chunki oʻzbek alifbosi lotincha",
        ],
        "correct": "Chunki rus tilida turkiy qatlam bor va u oʻzbekchaga tanish",
        "explanation": "<p>Rus bolasi <em>каранда́ш, изю́м, богаты́рь</em> ni "
                       "<strong>yodlaydi</strong>. Oʻzbek oʻquvchi ularni "
                       "<strong>taniydi</strong>. Ikki til bir necha asr yonma-yon "
                       "yashagan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Soʻzning kelib chiqishi nimani aytadi?</p>",
        "choices": [
            "Uning kelishigini",
            "Uning urgʻusini",
            "Uning jinsini",
            "Uning uslubini — qayerda ishlatilishini",
        ],
        "correct": "Uning uslubini — qayerda ishlatilishini",
        "explanation": "<p>Slavyan qatlami — eng issiq va kundalik; kitobiy shakl — rasmiy va"
                       " tantanali; yevropa qatlami — texnika va yangi sohalar.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu turkiy soʻzlarning oʻzbekcha "
                "qarindoshini toping.</p><p><strong>сара́й · казна́ · амба́р</strong></p>",
        "choices": [
            "shahar · xazina · ombor",
            "saroy · xazina · ombor",
            "saroy · kassa · anbor",
            "sara · xazina · ambar",
        ],
        "correct": "saroy · xazina · ombor",
        "explanation": "<p>Uchtasi ham deyarli oʻzgarmagan. Faqat <em>сара́й</em> ning "
                       "maʼnosi rus tilida pasaygan: «saroy» emas, «omborxona».</p>",
    },
]


# =====================================================================
# PR-100 — Yakuniy takror: butun kurs boʻylab
# =====================================================================

Q_PR100 = [
    {
        "text": "<p><strong>Blok A · alifbo.</strong> Bu harf qanday "
                "oʻqiladi?</p><p><strong>Р р</strong></p>",
        "choices": ["«rahmat» dagi r", "«b» kabi", "«n» kabi", "«p» kabi"],
        "correct": "«rahmat» dagi r",
        "explanation": "<p><strong>Р</strong> — soxta doʻst (PR-1): lotincha «P» ga "
                       "oʻxshaydi, lekin <strong>r</strong> deb oʻqiladi. Yettita soxta "
                       "doʻst: В Н Р С У Х Ы.</p>",
    },
    {
        "text": "<p><strong>Blok B · jins.</strong> Toʻgʻri shaklni "
                "tanlang.</p><p><strong>___ кни́га</strong></p>",
        "choices": ["но́вый", "но́вое", "но́вая", "но́вые"],
        "correct": "но́вая",
        "explanation": "<p><em>Кни́га</em> <strong>-а</strong> bilan tugaydi → же́нский род →"
                       " sifat ham <em>-ая</em> (PR-8, PR-12). Oʻzbek tilida jins yoʻq — "
                       "shuning uchun bu eng koʻp xato qilinadigan joy.</p>",
    },
    {
        "text": "<p><strong>Blok C · oʻtgan zamon.</strong> Boʻsh joyga nima "
                "tushadi?</p><p><strong>Афсо́на ___ письмо́.</strong> (написа́ть)</p>",
        "choices": ["написа́л", "написа́ло", "написа́ли", "написа́ла"],
        "correct": "написа́ла",
        "explanation": "<p>Oʻtgan zamonda feʼl <strong>egasining jinsiga</strong> moslashadi "
                       "(PR-23). Afsona — ayol → <em>-ла</em>.</p>",
    },
    {
        "text": "<p><strong>Blok D · kelishik.</strong> Boʻsh joyga nima "
                "tushadi?</p><p><strong>Я иду́ в ___ .</strong> (шко́ла)</p>",
        "choices": ["шко́лу", "шко́лы", "шко́лой", "шко́ле"],
        "correct": "шко́лу",
        "explanation": "<p><strong>Куда́?</strong> → в + <strong>Вини́тельный</strong> "
                       "(PR-33). <em>В шко́ле</em> esa «qayerda?» degan savolga javob berardi"
                       " — Предло́жный.</p>",
    },
    {
        "text": "<p><strong>Blok D · kelishik.</strong> Boʻsh joyga nima "
                "tushadi?</p><p><strong>У меня́ нет ___ .</strong> (вре́мя)</p>",
        "choices": ["вре́мени", "вре́менем", "вре́мени emas, вре́ме", "вре́мя"],
        "correct": "вре́мени",
        "explanation": "<p><em>Нет</em> dan keyin <strong>Роди́тельный</strong> (PR-34). "
                       "<em>Вре́мя</em> — notoʻgʻri turlanadigan ot: Р.п. "
                       "<em>вре́мени</em>.</p>",
    },
    {
        "text": "<p><strong>Blok E · feʼl turi.</strong> Qaysi biri "
                "toʻgʻri?</p><p><strong>Вчера́ я ___ э́ту кни́гу до конца́.</strong></p>",
        "choices": ["прочита́л", "чита́ю", "бу́ду чита́ть", "чита́л"],
        "correct": "прочита́л",
        "explanation": "<p>«Oxirigacha» — <strong>natija</strong> bor, demak "
                       "<strong>СВ</strong> (PR-51). <em>Чита́л</em> faqat jarayonni "
                       "bildirardi.</p>",
    },
    {
        "text": "<p><strong>Blok E · harakat feʼllari.</strong> Qaysi biri «har kuni maktabga"
                " boraman» degani?</p>",
        "choices": [
            "Я иду́ в шко́лу.",
            "Я хожу́ в шко́лу ка́ждый день.",
            "Я пошёл в шко́лу.",
            "Я е́ду в шко́лу.",
        ],
        "correct": "Я хожу́ в шко́лу ка́ждый день.",
        "explanation": "<p><strong>Ходи́ть</strong> — takroriy harakat, "
                       "<strong>идти́</strong> — hozir, bir yoʻnalishda (PR-55). Bu farq "
                       "oʻzbekchada yoʻq.</p>",
    },
    {
        "text": "<p><strong>Blok F · murakkab gap.</strong> Boʻsh joyga nima "
                "tushadi?</p><p><strong>Э́то кни́га, ___ я прочита́л ле́том.</strong></p>",
        "choices": ["кото́рый", "кото́рая", "кото́рую", "кото́рой"],
        "correct": "кото́рую",
        "explanation": "<p><em>Кни́га</em> — ж.р. (shakl <em>-ая</em>), lekin ergash gapda u "
                       "<strong>toʻldiruvchi</strong> — «nimani oʻqidim?» → "
                       "<strong>Вини́тельный</strong>: <em>кото́рую</em> (PR-63).</p>",
    },
    {
        "text": "<p><strong>Blok F · ravishdosh.</strong> Bu nima?</p><p><strong>Прочита́в "
                "сто уро́ков, он ви́дит текст ина́че.</strong></p>",
        "choices": [
            "Причастие",
            "Деепричастие — «oʻqib chiqib, keyin»",
            "Buyruq mayli",
            "Majhul nisbat",
        ],
        "correct": "Деепричастие — «oʻqib chiqib, keyin»",
        "explanation": "<p><strong>Деепричастие</strong> (PR-72): asosiy harakatdan "
                       "<strong>oldin</strong> boʻlgan ish. СВ shaklda <em>-в</em> "
                       "qoʻshimchasi bilan yasaladi.</p>",
    },
    {
        "text": "<p><strong>Blok G · свой.</strong> Toʻgʻri shaklni tanlang.</p><p><strong>Он"
                " лю́бит ___ рабо́ту.</strong></p>",
        "choices": ["его́", "свою́", "её", "их"],
        "correct": "свою́",
        "explanation": "<p>Ish <strong>egaga tegishli</strong>, demak <strong>свой</strong> "
                       "(PR-75). <em>Он лю́бит его́ рабо́ту</em> — «boshqa odamning ishini "
                       "yaxshi koʻradi» degani boʻlardi.</p>",
    },
    {
        "text": "<p><strong>Blok G · ikki inkor.</strong> Toʻgʻri gapni tanlang.</p>",
        "choices": [
            "Никто́ ничего́ не сказа́л.",
            "Никто́ ничего́ сказа́л.",
            "Кто-то ничего́ не сказа́л.",
            "Никто́ что-то не сказа́л.",
        ],
        "correct": "Никто́ ничего́ не сказа́л.",
        "explanation": "<p>Rus tilida <strong>ikki inkor majburiy</strong> (PR-79): "
                       "<em>никто́</em> boʻlsa ham <em>не</em> qoʻyiladi. Oʻzbekchada ham "
                       "shunday: «hech kim hech narsa <b>aytmadi</b>».</p>",
    },
    {
        "text": "<p><strong>Blok G · soʻz yasalishi.</strong> <strong>«Подсне́жник»</strong> "
                "nimani anglatadi?</p>",
        "choices": [
            "Qor ustidagi",
            "Qorsiz",
            "Qor tagidan chiquvchi — boychechak",
            "Qorga oʻxshagan",
        ],
        "correct": "Qor tagidan chiquvchi — boychechak",
        "explanation": "<p><em>под</em> + <em>снеж</em> + <em>ник</em> (PR-86). Oʻzbekcha "
                       "nomi ham tasvir bilan qurilgan: <em>boy-chechak</em>.</p>",
    },
    {
        "text": "<p><strong>Blok G · suffiks.</strong> <strong>«Но́вость»</strong> qaysi "
                "jinsda?</p>",
        "choices": ["Jinsi yoʻq", "Мужско́й", "Сре́дний", "Же́нский"],
        "correct": "Же́нский",
        "explanation": "<p><strong>-ость</strong> istisnosiz <strong>же́нский род</strong> "
                       "(PR-87) va <em>дверь</em> kabi turlanadi. Shuning uchun <em>хоро́шая "
                       "но́вость</em>.</p>",
    },
    {
        "text": "<p><strong>Blok H · soʻz tartibi.</strong> Savolga toʻgʻri javobni "
                "tanlang.</p><p><strong>— Кто откры́л окно́?</strong></p>",
        "choices": [
            "— Бекзо́д откры́л окно́.",
            "— Окно́ откры́л Бекзо́д.",
            "— Откры́л Бекзо́д окно́.",
            "— Окно́ Бекзо́д откры́л.",
        ],
        "correct": "— Окно́ откры́л Бекзо́д.",
        "explanation": "<p>Yangi maʼlumot — <strong>gap oxirida</strong> (PR-89). Oʻzbekchada"
                       " esa urgʻuli soʻz feʼldan oldin turadi.</p>",
    },
    {
        "text": "<p><strong>Blok H · uslub.</strong> Qaysi gapda uslub buzilgan?</p>",
        "choices": [
            "Уважа́емая Мари́на Петро́вна! Сообща́ю Вам, что…",
            "Прошу́ предоста́вить о́тпуск на неде́льку.",
            "Прошу́ Вас рассмотре́ть моё заявле́ние.",
            "С уваже́нием, Жасу́р Кари́мов",
        ],
        "correct": "Прошу́ предоста́вить о́тпуск на неде́льку.",
        "explanation": "<p>Toʻgʻrisi — <strong>на неде́лю</strong>. Rasmiy matnda "
                       "kichraytirish boʻlmaydi (PR-88, PR-90).</p>",
    },
    {
        "text": "<p><strong>Blok H · ariza.</strong> Arizaning «kimdan» satri qanday "
                "yoziladi?</p>",
        "choices": [
            "Ученику́ 9-А кла́сса Кари́мову",
            "от учени́к 9-А кла́сса Кари́мов",
            "Учени́к 9-А кла́сса Кари́мов",
            "от ученика́ 9-А кла́сса Кари́мова",
        ],
        "correct": "от ученика́ 9-А кла́сса Кари́мова",
        "explanation": "<p><strong>от + Роди́тельный</strong> (PR-91). Oʻzbekcha "
                       "<em>-dan</em> qoʻshimchasi bilan aynan bir xil ishlaydi.</p>",
    },
    {
        "text": "<p><strong>Blok H · juftliklar.</strong> Toʻgʻri feʼlni "
                "qoʻying.</p><p><strong>___ ша́пку, на у́лице хо́лодно.</strong></p>",
        "choices": ["Одева́й", "Оде́нь", "Наде́нь", "Ложи́"],
        "correct": "Наде́нь",
        "explanation": "<p>Shapka — <strong>narsa</strong> (что?), demak <em>наде́ть</em> "
                       "(PR-96). Oʻzbekcha «kiy», «kiydir» emas.</p>",
    },
    {
        "text": "<p><strong>Blok H · tinish belgisi.</strong> Odamni qutqarish uchun vergul "
                "qayerga qoʻyiladi?</p><p><strong>Казни́ть нельзя́ поми́ловать</strong></p>",
        "choices": [
            "Казни́ть, нельзя́ поми́ловать.",
            "Vergul kerak emas",
            "Казни́ть, нельзя́, поми́ловать.",
            "Казни́ть нельзя́, поми́ловать.",
        ],
        "correct": "Казни́ть нельзя́, поми́ловать.",
        "explanation": "<p>Vergul <em>нельзя́</em> dan keyin tursa, odam tirik qoladi "
                       "(PR-97). Uchta soʻz, bitta belgi, ikki xil taqdir.</p>",
    },
    {
        "text": "<p><strong>Blok H · til tarixi.</strong> <strong>«Здра́вствуйте»</strong> "
                "soʻzma-soʻz nima degani?</p>",
        "choices": [
            "«Kelganingiz yaxshi»",
            "«Sizni koʻrganimdan xursandman»",
            "«Sogʻ boʻling»",
            "«Xayrli kun»",
        ],
        "correct": "«Sogʻ boʻling»",
        "explanation": "<p>U <strong>здоро́вье</strong> dan (PR-99). Siz bu soʻzni PR-7 dan "
                       "beri aytib kelasiz — endi maʼnosini ham bilasiz.</p>",
    },
    {
        "text": "<p><strong>Yakuniy savol.</strong> Kurs oxirida eng muhim narsa nima?</p>",
        "choices": [
            "Yangi kurs boshlash",
            "Barcha qoidalarni yodlash",
            "Lugʻatni boshdan-oxir oʻqib chiqish",
            "Har kuni oz-ozdan davom ettirish va til bilan biror ish qilish",
        ],
        "correct": "Har kuni oz-ozdan davom ettirish va til bilan biror ish qilish",
        "explanation": "<p>Haftada bir marta uch soat ishlamaydi; kuniga 15 daqiqa ishlaydi. "
                       "Va til — maqsad emas, <strong>vosita</strong>: unda oʻqing, yozing, "
                       "gaplashing. <strong>Ни пу́ха ни пера́!</strong></p>",
    },
]


PRACTICES = [
    {
        "title": "PR-98 Mashq: Matn qurish",
        "description": (
            "Kirish — asosiy qism — xulosa, 15 ta bogʻlovchi, abzats qoidasi "
            "va xulosada qilinmaydigan uchta ish."
        ),
        "tutorial": "PR-98:",
        "questions": Q_PR98,
    },
    {
        "title": "PR-99 Mashq: Rus tili qayerdan kelgan",
        "description": (
            "Toʻrt qatlam, -оро-/-ра- kaliti (здоровье → здравствуйте) va "
            "turkiy qatlam: карандаш = qora tosh, богатырь = bahodir."
        ),
        "tutorial": "PR-99:",
        "questions": Q_PR99,
    },
    {
        "title": "PR-100 Mashq: Yakuniy takror — butun kurs",
        "description": (
            "Kursning oxirgi testi. Savollar sakkizta blokning hammasidan: "
            "alifbodan tinish belgilarigacha. Oʻzingizni tekshiring."
        ),
        "tutorial": "PR-100:",
        "questions": Q_PR100,
    },
]
